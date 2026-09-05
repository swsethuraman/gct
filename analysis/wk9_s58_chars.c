/* Session 58 -- Murnaghan-Nakayama character blocks on bead masks (C accelerator).
 *
 * One depth-first pass over the trie of partitions rho of m with parts ascending,
 * carrying the vector D[state] = signed count of strip-addition paths from the empty
 * partition, restricted to a given set of allowed states (bead masks with L beads).
 * At a leaf (a full partition rho of m) D[target] = chi^target(rho).
 *
 * The same algorithm as char_block() in wk9_s58_sk.py; the Python routine stays the
 * reference and the two are compared on every calibration sample.
 *
 * Exact integers: the DP runs in __int128 and every output is written as (lo, hi)
 * 64-bit halves of the two's-complement 128-bit value.
 *
 * Build:  gcc -O2 -shared -fPIC -o <build>/wk9_s58_chars.so analysis/wk9_s58_chars.c
 */
#include <stdint.h>
#include <stdlib.h>
#include <string.h>

typedef __int128 i128;

static int nst, Lb, mm, ntgt, maxleaves;
static uint64_t *masks;          /* allowed states, sorted ascending */
static int *tgt;                 /* target state ids */
static int *tr_off;              /* transitions: for k in 1..m, state s: entries in [tr_off[k*nst+s], tr_off[k*nst+s+1]) */
static int *tr_to;
static int8_t *tr_sg;
static int64_t *out_lo, *out_hi; /* leaves x ntgt */
static int *out_parts;           /* leaves x m (ascending parts, 0-padded) */
static int nleaves, overflow;
static int parts[256];

static int find_state(uint64_t mk) {
    int lo = 0, hi = nst - 1;
    while (lo <= hi) {
        int mid = (lo + hi) >> 1;
        if (masks[mid] == mk) return mid;
        if (masks[mid] < mk) lo = mid + 1; else hi = mid - 1;
    }
    return -1;
}

static void build_transitions(void) {
    /* count first */
    int *cnt = (int *)calloc((size_t)(mm + 1) * nst + 1, sizeof(int));
    long total = 0;
    for (int k = 1; k <= mm; k++)
        for (int s = 0; s < nst; s++) {
            uint64_t mk = masks[s];
            int c = 0;
            for (int b = 0; b + k < 64; b++) {
                if (!((mk >> b) & 1)) continue;
                if ((mk >> (b + k)) & 1) continue;
                uint64_t nw = mk ^ (1ULL << b) ^ (1ULL << (b + k));
                if (find_state(nw) >= 0) c++;
            }
            cnt[k * nst + s] = c;
            total += c;
        }
    tr_off = (int *)malloc(((size_t)(mm + 1) * nst + 1) * sizeof(int));
    tr_to = (int *)malloc((total + 1) * sizeof(int));
    tr_sg = (int8_t *)malloc((total + 1) * sizeof(int8_t));
    long pos = 0;
    for (int k = 0; k <= mm; k++)
        for (int s = 0; s < nst; s++) {
            tr_off[k * nst + s] = (int)pos;
            if (k == 0) continue;
            uint64_t mk = masks[s];
            for (int b = 0; b + k < 64; b++) {
                if (!((mk >> b) & 1)) continue;
                if ((mk >> (b + k)) & 1) continue;
                uint64_t nw = mk ^ (1ULL << b) ^ (1ULL << (b + k));
                int t = find_state(nw);
                if (t < 0) continue;
                /* beads strictly between b and b+k */
                uint64_t between = mk & ((1ULL << (b + k)) - 1) & ~((1ULL << (b + 1)) - 1);
                int ht = __builtin_popcountll(between);
                tr_to[pos] = t;
                tr_sg[pos] = (ht & 1) ? -1 : 1;
                pos++;
            }
        }
    tr_off[(mm + 1) * nst] = (int)pos;
    free(cnt);
}

static void dfs(int depth, int total, int minp, i128 *D) {
    if (total == mm) {
        if (nleaves >= maxleaves) { overflow |= 2; return; }
        for (int i = 0; i < ntgt; i++) {
            i128 v = D[tgt[i]];
            out_lo[(size_t)nleaves * ntgt + i] = (int64_t)(uint64_t)(v & 0xFFFFFFFFFFFFFFFFULL);
            out_hi[(size_t)nleaves * ntgt + i] = (int64_t)(v >> 64);
        }
        for (int i = 0; i < mm; i++) out_parts[(size_t)nleaves * mm + i] = (i < depth) ? parts[i] : 0;
        nleaves++;
        return;
    }
    i128 *D2 = (i128 *)malloc(nst * sizeof(i128));
    for (int k = minp; k <= mm - total; k++) {
        memset(D2, 0, nst * sizeof(i128));
        int nz = 0;
        for (int s = 0; s < nst; s++) {
            i128 v = D[s];
            if (v == 0) continue;
            int a = tr_off[k * nst + s], b = tr_off[k * nst + s + 1];
            for (int e = a; e < b; e++) {
                int t = tr_to[e];
                if (tr_sg[e] > 0) D2[t] += v; else D2[t] -= v;
            }
        }
        for (int s = 0; s < nst; s++) if (D2[s] != 0) { nz = 1; break; }
        if (!nz) continue;
        parts[depth] = k;
        dfs(depth + 1, total + k, k, D2);
    }
    free(D2);
}

/* returns number of leaves written; sets *flags: bit 1 = leaf buffer too small */
int s58_char_block(int m, int L, int nstates, const uint64_t *states_in, int ntargets, const int *targets_in,
                   int64_t *o_lo, int64_t *o_hi, int *o_parts, int max_leaves, int *flags) {
    mm = m; Lb = L; nst = nstates; ntgt = ntargets; maxleaves = max_leaves;
    masks = (uint64_t *)malloc(nst * sizeof(uint64_t));
    memcpy(masks, states_in, nst * sizeof(uint64_t));
    for (int i = 1; i < nst; i++) if (masks[i] <= masks[i - 1]) { *flags = 4; free(masks); return 0; }  /* must be sorted, distinct */
    tgt = (int *)malloc((ntgt + 1) * sizeof(int));
    memcpy(tgt, targets_in, ntgt * sizeof(int));
    out_lo = o_lo; out_hi = o_hi; out_parts = o_parts;
    nleaves = 0; overflow = 0;
    build_transitions();
    i128 *D = (i128 *)calloc(nst, sizeof(i128));
    uint64_t empty = (L >= 64) ? ~0ULL : ((1ULL << L) - 1);
    int e = find_state(empty);
    if (e < 0) { *flags = 8; free(D); free(masks); free(tgt); free(tr_off); free(tr_to); free(tr_sg); return 0; }
    D[e] = 1;
    if (m == 0) {
        for (int i = 0; i < ntgt; i++) { o_lo[i] = (tgt[i] == e); o_hi[i] = 0; }
        nleaves = 1;
    } else {
        dfs(0, 0, 1, D);
    }
    *flags = overflow;
    free(D); free(masks); free(tgt); free(tr_off); free(tr_to); free(tr_sg);
    return nleaves;
}
