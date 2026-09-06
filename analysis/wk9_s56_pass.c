/* Session 56 — the Foulkes engine: exact passes over H_{4,delta}.

   usage:  wk9_s56_pass delta mu_1,mu_2,...  outfile   [mode]
           mode = "weight" (default): the weight-space Gram matrices
                  b(O,O') = sum_{pi in O} K(pi, rep(O'))^2      (sign-free)
                  k(O,O') = sum_{pi in O} K(pi, rep(O'))        (signed)
                  for the S_mu-orbits O (weight-mu monomials) of H_{4,delta},
                  written as decimal integers, one matrix row per line.
           mode = "krow": write K(pi0, pi) (signed) for every pi in H, in
                  enumeration order (validation against the Python row).

   The kernel.  K(pi,pi') = <eps_pi, eps_pi'> with eps_pi the product of the
   4x4x4x4 alternating tensor over the blocks (each block in increasing position
   order).  |K| depends only on the double coset rel(pi,pi') and is computed
   once per class by the transparent tensor sum over the 24^delta support of
   eps_pi0.  The sign is recovered from the coset decomposition
   g_pi = w g_d w', w,w' in W = Stab(pi0):  K(pi0,pi) = chi(w) chi(w') K(pi0,pi_d),
   chi(w) = product over blocks of pi0 of the sorting sign of w on the block.
   For a general pair, K(pi,pi') = sigma(h,pi0) K(pi0, h pi0), h = g_pi^{-1} g_pi'.

   All arithmetic is integer; accumulators are unsigned/signed 128-bit.  */

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdint.h>
#include <time.h>

#define MAXD 6
#define MAXN 24
static int delta, N;
static int mu[MAXD + 2], ncol;          /* the weight: colours per position */
static int colour[MAXN];

/* ---------------------------------------------------------- permutations */
static int perm4[24][4];
static int sgn4[24];
static int nperm_d;                     /* delta! */
static int permd[720][MAXD];

static void init_perms(void) {
    int cnt = 0;
    int a[4];
    for (a[0] = 0; a[0] < 4; a[0]++) for (a[1] = 0; a[1] < 4; a[1]++)
    for (a[2] = 0; a[2] < 4; a[2]++) for (a[3] = 0; a[3] < 4; a[3]++) {
        if (a[0] == a[1] || a[0] == a[2] || a[0] == a[3] || a[1] == a[2] || a[1] == a[3] || a[2] == a[3]) continue;
        int s = 1;
        for (int i = 0; i < 4; i++) for (int j = i + 1; j < 4; j++) if (a[i] > a[j]) s = -s;
        memcpy(perm4[cnt], a, sizeof a); sgn4[cnt] = s; cnt++;
    }
    /* permutations of delta */
    int p[MAXD];
    for (int i = 0; i < delta; i++) p[i] = i;
    nperm_d = 0;
    /* Heap's algorithm is overkill: use next_permutation */
    for (;;) {
        memcpy(permd[nperm_d++], p, sizeof(int) * delta);
        int i = delta - 2;
        while (i >= 0 && p[i] >= p[i + 1]) i--;
        if (i < 0) break;
        int j = delta - 1;
        while (p[j] <= p[i]) j--;
        int t = p[i]; p[i] = p[j]; p[j] = t;
        for (int a2 = i + 1, b2 = delta - 1; a2 < b2; a2++, b2--) { t = p[a2]; p[a2] = p[b2]; p[b2] = t; }
    }
}

/* sign table for 4 values in 0..3 (code base 4) : 0 if repeated */
static int8_t sign_tab[256];
static void init_sign_tab(void) {
    memset(sign_tab, 0, sizeof sign_tab);
    for (int k = 0; k < 24; k++)
        sign_tab[perm4[k][0] * 64 + perm4[k][1] * 16 + perm4[k][2] * 4 + perm4[k][3]] = (int8_t)sgn4[k];
}

/* -------------------------------------------- labelled margin-4 matrices */
typedef struct { uint64_t code; int64_t K; int cls; int8_t rho[MAXD]; int8_t tau[MAXD]; int used; } entry_t;
static entry_t *table; static uint64_t tabmask;
static int nlab = 0;

static uint64_t code_of(int M[MAXD][MAXD]) {
    uint64_t c = 0;
    for (int j = 0; j < delta; j++) for (int i = 0; i < delta; i++) c = c * 5 + (uint64_t)M[j][i];
    return c;
}
static entry_t *lookup(uint64_t code, int insert) {
    uint64_t h = (code * 0x9E3779B97F4A7C15ULL) >> 20;
    for (;;) {
        entry_t *e = &table[h & tabmask];
        if (!e->used) { if (!insert) return NULL; e->used = 1; e->code = code; nlab++; return e; }
        if (e->code == code) return e;
        h++;
    }
}

/* canonical form under row & column permutations: min over column perms of the
   lexicographically sorted rows (entries compared as integers, delta x delta only) */
static int cmp_rows(const int *a, const int *b) { for (int i = 0; i < delta; i++) if (a[i] != b[i]) return a[i] < b[i] ? -1 : 1; return 0; }
static int cmp_mats(int A[MAXD][MAXD], int B[MAXD][MAXD]) { for (int j = 0; j < delta; j++) { int c = cmp_rows(A[j], B[j]); if (c) return c; } return 0; }
static void canon_of(int M[MAXD][MAXD], int out[MAXD][MAXD]) {
    int best[MAXD][MAXD]; int have = 0;
    memset(best, 0, sizeof best);
    for (int c = 0; c < nperm_d; c++) {
        int rows[MAXD][MAXD]; memset(rows, 0, sizeof rows);
        for (int j = 0; j < delta; j++) for (int i = 0; i < delta; i++) rows[j][i] = M[j][permd[c][i]];
        for (int a = 1; a < delta; a++) {
            int tmp[MAXD]; memcpy(tmp, rows[a], sizeof tmp);
            int b = a - 1;
            while (b >= 0 && cmp_rows(rows[b], tmp) > 0) { memcpy(rows[b + 1], rows[b], sizeof tmp); b--; }
            memcpy(rows[b + 1], tmp, sizeof tmp);
        }
        if (!have || cmp_mats(rows, best) < 0) { memcpy(best, rows, sizeof best); have = 1; }
    }
    memset(out, 0, sizeof(int) * MAXD * MAXD);
    memcpy(out, best, sizeof best);
}

/* the tensor-sum kernel K(pi0, pi) for pi given by block masks */
static int64_t kernel_direct(uint32_t *blocks) {
    int pos[MAXD][4];
    for (int k = 0; k < delta; k++) { int t = 0; for (int p = 0; p < N; p++) if (blocks[k] >> p & 1) pos[k][t++] = p; }
    int64_t total = 0;
    int idx[MAXD]; for (int j = 0; j < delta; j++) idx[j] = 0;
    int x[MAXN];
    for (;;) {
        int s = 1;
        for (int j = 0; j < delta; j++) { s *= sgn4[idx[j]]; for (int t = 0; t < 4; t++) x[4 * j + t] = perm4[idx[j]][t]; }
        for (int k = 0; k < delta && s; k++) {
            int c = x[pos[k][0]] * 64 + x[pos[k][1]] * 16 + x[pos[k][2]] * 4 + x[pos[k][3]];
            s *= sign_tab[c];
        }
        total += s;
        int j = 0;
        while (j < delta && ++idx[j] == 24) { idx[j] = 0; j++; }
        if (j == delta) break;
    }
    return total;
}

/* build the partition pi_M realising labelled matrix M against pi0: block i of
   pi takes M[j][i] lowest unused elements of block j of pi0 */
static void partition_of_matrix(int M[MAXD][MAXD], uint32_t *blocks) {
    int next[MAXD]; for (int j = 0; j < delta; j++) next[j] = 4 * j;
    for (int i = 0; i < delta; i++) { blocks[i] = 0; for (int j = 0; j < delta; j++) for (int t = 0; t < M[j][i]; t++) blocks[i] |= 1u << next[j]++; }
}

static int ncls = 0; static int64_t clsK[1 << 16]; static int clsM[1 << 16][MAXD][MAXD];
static uint64_t clscode[1 << 16];
static int class_of_canonical(int C[MAXD][MAXD]) {
    uint64_t cc = code_of(C);
    for (int c = 0; c < ncls; c++) if (clscode[c] == cc) return c;
    uint32_t blocks[MAXD]; partition_of_matrix(C, blocks);
    int cls = ncls++;
    clscode[cls] = cc;
    memcpy(clsM[cls], C, sizeof(int) * MAXD * MAXD);
    clsK[cls] = kernel_direct(blocks);
    return cls;
}

static int rows_[130][MAXD]; static int nrows_ = 0; static int r_[MAXD];
static void rec_rows(int i, int rem) {
    if (i == delta) { if (rem == 0) memcpy(rows_[nrows_++], r_, sizeof r_); return; }
    for (int v = 0; v <= rem; v++) { r_[i] = v; rec_rows(i + 1, rem - v); }
}
static int M_[MAXD][MAXD]; static int colsum_[MAXD];
static void rec_lab(int j) {
    if (j == delta) {
        for (int i = 0; i < delta; i++) if (colsum_[i] != 4) return;
        int C[MAXD][MAXD]; canon_of(M_, C);
        int cls = class_of_canonical(C);
        entry_t *e = lookup(code_of(M_), 1);
        e->cls = cls; e->K = clsK[cls];
        int found = 0;
        for (int a = 0; a < nperm_d && !found; a++) for (int b = 0; b < nperm_d && !found; b++) {
            int ok = 1;
            for (int jj = 0; jj < delta && ok; jj++) for (int ii = 0; ii < delta; ii++)
                if (C[jj][ii] != M_[permd[a][jj]][permd[b][ii]]) { ok = 0; break; }
            if (ok) { for (int t = 0; t < delta; t++) { e->rho[t] = permd[a][t]; e->tau[t] = permd[b][t]; } found = 1; }
        }
        if (!found) { fprintf(stderr, "no (rho,tau) found\n"); exit(2); }
        return;
    }
    for (int k = 0; k < nrows_; k++) {
        int ok = 1;
        for (int i = 0; i < delta; i++) if (colsum_[i] + rows_[k][i] > 4) { ok = 0; break; }
        if (!ok) continue;
        for (int i = 0; i < delta; i++) { M_[j][i] = rows_[k][i]; colsum_[i] += rows_[k][i]; }
        rec_lab(j + 1);
        for (int i = 0; i < delta; i++) colsum_[i] -= rows_[k][i];
    }
}
static void enumerate_labelled(void) { rec_rows(0, 4); rec_lab(0); }

/* -------------------------------------------------- signed K(pi0, pi) */
static int sorting_sign(int *img) {           /* sign of the permutation sorting 4 values */
    int s = 1;
    for (int i = 0; i < 4; i++) for (int j = i + 1; j < 4; j++) if (img[i] > img[j]) s = -s;
    return s;
}

/* K(pi0, pi) with pi given by its canonical blocks; returns via the coset decomposition */
static int64_t kernel_signed_row(uint32_t *blocks, int check) {
    int M[MAXD][MAXD];
    for (int j = 0; j < delta; j++) for (int i = 0; i < delta; i++) M[j][i] = __builtin_popcount(blocks[i] & (0xFu << (4 * j)));
    entry_t *e = lookup(code_of(M), 0);
    if (!e) { fprintf(stderr, "matrix not in table\n"); exit(3); }
    int C[MAXD][MAXD]; memcpy(C, clsM[e->cls], sizeof C);
    /* pi_d realising C; g_d its coset rep; g_pi the coset rep of pi */
    uint32_t bd[MAXD]; partition_of_matrix(C, bd);
    int gd[MAXN], gpi[MAXN];
    for (int i = 0; i < delta; i++) { int t = 0; for (int p = 0; p < N; p++) if (bd[i] >> p & 1) gd[4 * i + t++] = p; }
    for (int i = 0; i < delta; i++) { int t = 0; for (int p = 0; p < N; p++) if (blocks[i] >> p & 1) gpi[4 * i + t++] = p; }
    /* w: cell (j,i) of (pi0,pi_d) -> cell (rho j, tau i) of (pi0, pi), increasing */
    int w[MAXN];
    for (int j = 0; j < delta; j++) for (int i = 0; i < delta; i++) {
        uint32_t src = bd[i] & (0xFu << (4 * j));
        uint32_t dst = blocks[e->tau[i]] & (0xFu << (4 * e->rho[j]));
        if (__builtin_popcount(src) != __builtin_popcount(dst)) { fprintf(stderr, "cell size mismatch\n"); exit(4); }
        while (src) { int a = __builtin_ctz(src), b = __builtin_ctz(dst); w[a] = b; src &= src - 1; dst &= dst - 1; }
    }
    /* chi(w) */
    int chi_w = 1;
    for (int j = 0; j < delta; j++) { int img[4]; for (int t = 0; t < 4; t++) img[t] = w[4 * j + t]; chi_w *= sorting_sign(img); }
    /* w' = g_d^{-1} w^{-1} g_pi */
    int winv[MAXN], gdinv[MAXN], wp[MAXN];
    for (int p = 0; p < N; p++) { winv[w[p]] = p; gdinv[gd[p]] = p; }
    for (int p = 0; p < N; p++) wp[p] = gdinv[winv[gpi[p]]];
    int chi_wp = 1;
    for (int j = 0; j < delta; j++) {
        int img[4]; for (int t = 0; t < 4; t++) img[t] = wp[4 * j + t];
        if (check) { for (int t = 0; t < 4; t++) if (img[t] / 4 != img[0] / 4) { fprintf(stderr, "w' not in W\n"); exit(5); } }
        chi_wp *= sorting_sign(img);
    }
    return (int64_t)chi_w * chi_wp * e->K;
}

/* ------------------------------------------------- enumeration of H */
typedef void (*visit_t)(uint32_t *blocks);
static uint32_t cur[MAXD];
static void rec_part(uint32_t remaining, int depth, visit_t visit) {
    if (!remaining) { visit(cur); return; }
    uint32_t first = remaining & -remaining;
    uint32_t rest = remaining ^ first;
    /* choose 3 of rest */
    for (uint32_t a = rest; a; a &= a - 1) {
        uint32_t ba = a & -a;
        for (uint32_t b = a ^ ba; b; b &= b - 1) {
            uint32_t bb = b & -b;
            for (uint32_t c = b ^ bb; c; c &= c - 1) {
                uint32_t bc = c & -c;
                cur[depth] = first | ba | bb | bc;
                rec_part(remaining ^ cur[depth], depth + 1, visit);
            }
        }
    }
}

/* ------------------------------------------------- weight-space pass */
#define MAXORB 65536
static int norb = 0;
static uint64_t orbkey[MAXORB]; static uint32_t orbrep[MAXORB][MAXD]; static uint64_t orbsize[MAXORB];
static int orbcontent[MAXORB][MAXD];   /* block content codes (sorted) */
static int64_t *orbidx_hash; static uint64_t orbmask = (1 << 20) - 1;

static uint64_t orbit_key(uint32_t *blocks, int *codes) {
    for (int k = 0; k < delta; k++) {
        int cnt[MAXD + 2] = {0};
        uint32_t m = blocks[k];
        while (m) { int p = __builtin_ctz(m); cnt[colour[p]]++; m &= m - 1; }
        int c = 0; for (int q = 0; q < ncol; q++) c = c * 5 + cnt[q];
        codes[k] = c;
    }
    /* sort codes */
    for (int a = 1; a < delta; a++) { int v = codes[a], b = a - 1; while (b >= 0 && codes[b] > v) { codes[b + 1] = codes[b]; b--; } codes[b + 1] = v; }
    uint64_t key = 1469598103934665603ULL;
    for (int k = 0; k < delta; k++) key = (key ^ (uint64_t)codes[k]) * 1099511628211ULL;
    return key;
}
static int orbit_index(uint32_t *blocks, int insert) {
    int codes[MAXD];
    uint64_t key = orbit_key(blocks, codes);
    uint64_t h = key & orbmask;
    for (;;) {
        int64_t v = orbidx_hash[h];
        if (v < 0) {
            if (!insert) { fprintf(stderr, "unknown orbit\n"); exit(6); }
            int id = norb++;
            if (norb > MAXORB) { fprintf(stderr, "too many orbits\n"); exit(7); }
            orbkey[id] = key; memcpy(orbrep[id], blocks, sizeof(uint32_t) * delta); memcpy(orbcontent[id], codes, sizeof(int) * delta);
            orbidx_hash[h] = id; return id;
        }
        if (orbkey[v] == key) return (int)v;
        h = (h + 1) & orbmask;
    }
}

static uint64_t nvisited = 0;
static void visit_pass1(uint32_t *blocks) { int id = orbit_index(blocks, 1); orbsize[id]++; nvisited++; }

static __int128 *acc_b; static __int128 *acc_k;
static int do_signed = 1;
static void visit_pass2(uint32_t *blocks) {
    int id = orbit_index(blocks, 0);
    nvisited++;
    for (int o = 0; o < norb; o++) {
        int M[MAXD][MAXD];
        uint32_t *rb = orbrep[o];
        for (int j = 0; j < delta; j++) for (int i = 0; i < delta; i++) M[j][i] = __builtin_popcount(blocks[j] & rb[i]);
        entry_t *e = lookup(code_of(M), 0);
        int64_t K = e->K;
        acc_b[(size_t)id * norb + o] += (__int128)K * K;
    }
}
/* signed k(O,O'): needs K(pi, rep) signed = sigma(h,pi0) K(pi0, h pi0), h = g_pi^{-1} g_rep.
   h pi0 = g_pi^{-1}(rep); sigma(h,pi0) = product of sorting signs of g_pi^{-1} on rep's blocks. */
static void visit_pass2_signed(uint32_t *blocks) {
    int id = orbit_index(blocks, 0);
    nvisited++;
    int gpi_inv[MAXN];
    for (int i = 0; i < delta; i++) { int t = 0; uint32_t m = blocks[i]; while (m) { int p = __builtin_ctz(m); gpi_inv[p] = 4 * i + t++; m &= m - 1; } }
    for (int o = 0; o < norb; o++) {
        uint32_t *rb = orbrep[o];
        uint32_t hb[MAXD]; int sig = 1;
        for (int i = 0; i < delta; i++) {
            int img[4]; int t = 0; uint32_t m = rb[i]; hb[i] = 0;
            while (m) { int p = __builtin_ctz(m); img[t++] = gpi_inv[p]; hb[i] |= 1u << gpi_inv[p]; m &= m - 1; }
            sig *= sorting_sign(img);
        }
        /* canonical order of hb by lowest element */
        for (int a = 1; a < delta; a++) { uint32_t v = hb[a]; int b = a - 1; while (b >= 0 && (hb[b] & -hb[b]) > (v & -v)) { hb[b + 1] = hb[b]; b--; } hb[b + 1] = v; }
        int64_t K = sig * kernel_signed_row(hb, 0);
        acc_k[(size_t)id * norb + o] += (__int128)K;
        acc_b[(size_t)id * norb + o] += (__int128)K * K;
    }
}

static void print128(FILE *f, __int128 v) {
    char buf[64]; int n = 0; int neg = v < 0; unsigned __int128 u = neg ? -(unsigned __int128)v : (unsigned __int128)v;
    if (u == 0) { fputc('0', f); return; }
    while (u) { buf[n++] = '0' + (int)(u % 10); u /= 10; }
    if (neg) fputc('-', f);
    while (n) fputc(buf[--n], f);
}

static void visit_krow(uint32_t *blocks) {
    int64_t K = kernel_signed_row(blocks, 1);
    printf("%lld\n", (long long)K);
}

int main(int argc, char **argv) {
    if (argc < 4) { fprintf(stderr, "usage: %s delta mu outfile [weight|krow|nosign]\n", argv[0]); return 1; }
    delta = atoi(argv[1]); N = 4 * delta;
    const char *mode = argc > 4 ? argv[4] : "weight";
    ncol = 0; int pos = 0;
    { char *s = strdup(argv[2]); for (char *tok = strtok(s, ","); tok; tok = strtok(NULL, ",")) { mu[ncol] = atoi(tok); for (int t = 0; t < mu[ncol]; t++) colour[pos++] = ncol; ncol++; } }
    if (pos != N && strcmp(mode, "krow") != 0) { fprintf(stderr, "weight does not sum to N\n"); return 1; }
    init_perms(); init_sign_tab();
    tabmask = (delta >= 5) ? ((1u << 24) - 1) : ((1u << 16) - 1);
    table = calloc(tabmask + 1, sizeof(entry_t));
    clock_t t0 = clock();
    enumerate_labelled();
    fprintf(stderr, "labelled matrices %d, classes %d, %.1fs\n", nlab, ncls, (double)(clock() - t0) / CLOCKS_PER_SEC);
    if (strcmp(mode, "krow") == 0) { rec_part((1u << N) - 1, 0, visit_krow); return 0; }
    orbidx_hash = malloc(sizeof(int64_t) * (orbmask + 1)); for (uint64_t i = 0; i <= orbmask; i++) orbidx_hash[i] = -1;
    t0 = clock();
    rec_part((1u << N) - 1, 0, visit_pass1);
    double t1 = (double)(clock() - t0) / CLOCKS_PER_SEC;
    fprintf(stderr, "pass1: |H| = %llu, orbits (nb) = %d, %.1fs\n", (unsigned long long)nvisited, norb, t1);
    acc_b = calloc((size_t)norb * norb, sizeof(__int128)); acc_k = calloc((size_t)norb * norb, sizeof(__int128));
    nvisited = 0; t0 = clock();
    do_signed = strcmp(mode, "nosign") != 0;
    rec_part((1u << N) - 1, 0, do_signed ? visit_pass2_signed : visit_pass2);
    double t2 = (double)(clock() - t0) / CLOCKS_PER_SEC;
    fprintf(stderr, "pass2: %.1fs (%.1f ns per partition per orbit)\n", t2, t2 * 1e9 / ((double)nvisited * norb));
    FILE *f = fopen(argv[3], "w");
    fprintf(f, "delta %d N %d weight %s\nH %llu nb %d labelled %d classes %d signed %d\npass1_seconds %.3f pass2_seconds %.3f\n",
            delta, N, argv[2], (unsigned long long)nvisited, norb, nlab, ncls, do_signed, t1, t2);
    fprintf(f, "orbits\n");
    for (int o = 0; o < norb; o++) { fprintf(f, "%llu", (unsigned long long)orbsize[o]); for (int k = 0; k < delta; k++) fprintf(f, " %d", orbcontent[o][k]); fprintf(f, "\n"); }
    fprintf(f, "b\n");
    for (int o = 0; o < norb; o++) { for (int p = 0; p < norb; p++) { if (p) fputc(' ', f); print128(f, acc_b[(size_t)o * norb + p]); } fputc('\n', f); }
    if (do_signed) { fprintf(f, "k\n");
        for (int o = 0; o < norb; o++) { for (int p = 0; p < norb; p++) { if (p) fputc(' ', f); print128(f, acc_k[(size_t)o * norb + p]); } fputc('\n', f); } }
    fclose(f);
    return 0;
}
