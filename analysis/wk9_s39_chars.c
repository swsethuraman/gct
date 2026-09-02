/*
 * Session 39 -- Murnaghan-Nakayama characters on beta-sets, memoised, in C.
 *
 * Independent implementation (written from the rule, not ported from
 * scripts/ambient_screen.py) of chi^lam(rho) for lam with at most L rows:
 *
 *   chi^lam(rho) = sum over rim hooks h of size rho_1 removable from lam of
 *                  (-1)^{ht(h)} chi^{lam - h}(rho_2, rho_3, ...)
 *
 * on beta-numbers beta_i = lam_i + (L-1-i): removing a rim hook of size r is
 * beta_i -> beta_i - r (allowed iff beta_i - r >= 0 and not already a beta
 * number), with sign (-1)^{#beta_j strictly between beta_i - r and beta_i}.
 * Values are exact in __int128 (|chi| <= f^lam <= sqrt(N!) < 2^127 for N <= 48).
 *
 * The memo is keyed on (packed beta-set, suffix id) where the suffix id is the
 * combinatorial rank of the remaining multiset (rho_{j+1}, ...) among all
 * partitions of its size, so identical suffixes of different rho share entries.
 *
 * Exposed to python (ctypes):
 *   chi_batch     : exact chi^lam(rho) for a list of rho (lo/hi 64-bit words)
 *   weighted_sums : sum_rho chi^lam(rho) * W_k(rho) mod two primes, for several
 *                   class functions W_k given mod the primes (plethysm a, the
 *                   Kronecker g, the transpose-twist T)
 *   memo_reset / memo_entries / memo_set_cap
 */
#include <stdint.h>
#include <stdlib.h>
#include <string.h>

typedef __int128 i128;
typedef unsigned __int128 u128;

/* ------------------------------------------------------------ memo table */
typedef struct { uint64_t key; uint32_t sid; uint32_t used; i128 val; } Entry;
static Entry *tab = NULL;
static size_t cap = 0, cnt = 0, cap_max = (size_t)1 << 26;   /* 64M entries ~ 2 GB */
static uint64_t n_clears = 0;

static inline uint64_t hsh(uint64_t k, uint32_t s) {
    uint64_t h = k ^ ((uint64_t)s * 0xC2B2AE3D27D4EB4FULL);
    h *= 0x9E3779B97F4A7C15ULL; h ^= h >> 29; h *= 0xBF58476D1CE4E5B9ULL; h ^= h >> 32;
    return h;
}
static void tab_alloc(size_t c) {
    if (tab) free(tab);
    cap = c; cnt = 0;
    tab = (Entry *)calloc(cap, sizeof(Entry));
}
void memo_reset(void) {
    if (!tab) tab_alloc((size_t)1 << 20);
    else { memset(tab, 0, cap * sizeof(Entry)); cnt = 0; }
}
void memo_set_cap(uint64_t c) { cap_max = (size_t)c; }
uint64_t memo_entries(void) { return (uint64_t)cnt; }
uint64_t memo_clears(void) { return n_clears; }

static void tab_insert_raw(uint64_t key, uint32_t sid, i128 val) {
    size_t i = hsh(key, sid) & (cap - 1);
    while (tab[i].used) i = (i + 1) & (cap - 1);
    tab[i].key = key; tab[i].sid = sid; tab[i].used = 1; tab[i].val = val; cnt++;
}
static void tab_grow(void) {
    Entry *old = tab; size_t oc = cap;
    cap = oc * 2; cnt = 0;
    tab = (Entry *)calloc(cap, sizeof(Entry));
    for (size_t i = 0; i < oc; i++)
        if (old[i].used) tab_insert_raw(old[i].key, old[i].sid, old[i].val);
    free(old);
}
static inline int tab_find(uint64_t key, uint32_t sid, i128 *out) {
    size_t i = hsh(key, sid) & (cap - 1);
    while (tab[i].used) {
        if (tab[i].key == key && tab[i].sid == sid) { *out = tab[i].val; return 1; }
        i = (i + 1) & (cap - 1);
    }
    return 0;
}
static inline void tab_put(uint64_t key, uint32_t sid, i128 val) {
    if (2 * (cnt + 1) > cap) {
        if (cap >= cap_max) { memset(tab, 0, cap * sizeof(Entry)); cnt = 0; n_clears++; }
        else tab_grow();
    }
    tab_insert_raw(key, sid, val);
}

/* --------------------------------------------- partition ranking (suffix ids) */
#define NMAX 64
static uint64_t Pc[NMAX + 1][NMAX + 1];   /* Pc[m][b] = #partitions of m with parts <= b */
static uint64_t OFF[NMAX + 2];
static int rank_ready = 0;
static void rank_init(void) {
    for (int m = 0; m <= NMAX; m++)
        for (int b = 0; b <= NMAX; b++) {
            if (m == 0) Pc[m][b] = 1;
            else if (b == 0) Pc[m][b] = 0;
            else Pc[m][b] = Pc[m][b - 1] + (b <= m ? Pc[m - b][b] : 0);
        }
    OFF[0] = 0;
    for (int m = 0; m <= NMAX; m++) OFF[m + 1] = OFF[m] + Pc[m][m];
    rank_ready = 1;
}
/* rank of (p[0] >= p[1] >= ... >= p[k-1]) (sum m) among partitions of m with
   parts <= b, ordered by first part ascending then recursively. */
static uint64_t prank(const int32_t *p, int k, int m, int b) {
    uint64_t r = 0;
    for (int j = 0; j < k; j++) {
        int q = p[j];
        for (int t = 1; t < q; t++) r += Pc[m - t][t];
        m -= q; b = q;
    }
    (void)b;
    return r;
}
uint32_t suffix_id(const int32_t *p, int k, int m) {   /* global id of a partition of m */
    if (!rank_ready) rank_init();
    return (uint32_t)(OFF[m] + prank(p, k, m, m));
}

/* ------------------------------------------------------------ the recursion */
static int L;                       /* number of beta numbers (rows incl. zeros) */
static const int32_t *cur_parts;    /* parts of the current rho, descending */
static const uint32_t *cur_sids;    /* suffix ids: cur_sids[j] = id of (parts[j], parts[j+1], ...) */
static int cur_k;

static inline uint64_t pack(const int *beta) {
    uint64_t k = 0;
    for (int i = 0; i < L; i++) k |= ((uint64_t)beta[i]) << (6 * i);
    return k;
}

static i128 chi_rec(int *beta, int j) {
    if (j == cur_k) return (i128)1;          /* sizes always match: lam' is empty */
    uint64_t key = pack(beta);
    uint32_t sid = cur_sids[j];
    i128 v;
    if (tab_find(key, sid, &v)) return v;
    int r = cur_parts[j];
    i128 tot = 0;
    int nb[16];
    for (int i = 0; i < L; i++) {
        int b = beta[i] - r;
        if (b < 0) continue;
        int clash = 0, ht = 0;
        for (int t = 0; t < L; t++) {
            if (beta[t] == b) { clash = 1; break; }
            if (beta[t] > b && beta[t] < beta[i]) ht++;
        }
        if (clash) continue;
        /* new beta set, kept sorted descending */
        int m = 0;
        for (int t = 0; t < L; t++) {
            if (t == i) continue;
            nb[m++] = beta[t];
        }
        /* insert b into the descending array nb[0..L-2] */
        int pos = L - 1;
        while (pos > 0 && nb[pos - 1] < b) { nb[pos] = nb[pos - 1]; pos--; }
        nb[pos] = b;
        i128 sub = chi_rec(nb, j + 1);
        if (ht & 1) tot -= sub; else tot += sub;
    }
    tab_put(key, sid, tot);
    return tot;
}

/* lam: L parts (descending, zeros allowed).  rho list: flat parts, offsets, lengths.
   sids_flat: for each rho, k+1 suffix ids (position off[r] + r extra slot).  We
   compute suffix ids internally to keep the interface simple. */
static uint32_t *sid_buf = NULL; static size_t sid_cap = 0;

static int last_L = -1;
static int prepare(int Lrows, const int32_t *lam, int *beta) {
    if (Lrows < 1 || Lrows > 10) return -1;
    L = Lrows;
    for (int i = 0; i < L; i++) {
        beta[i] = lam[i] + (L - 1 - i);
        if (beta[i] < 0 || beta[i] >= 64) return -2;
        if (i && lam[i] > lam[i - 1]) return -3;
    }
    if (!tab) tab_alloc((size_t)1 << 20);
    if (!rank_ready) rank_init();
    if (L != last_L) { memo_reset(); last_L = L; }   /* keys depend on L */
    return 0;
}

static void compute_sids(const int32_t *parts, int k, int N) {
    if ((size_t)(k + 1) > sid_cap) { sid_cap = k + 64; sid_buf = (uint32_t *)realloc(sid_buf, sid_cap * sizeof(uint32_t)); }
    int m = N;
    for (int j = 0; j <= k; j++) {
        sid_buf[j] = (uint32_t)(OFF[m] + prank(parts + j, k - j, m, m));
        if (j < k) m -= parts[j];
    }
}

/* exact characters: out_lo/out_hi receive the two 64-bit words of each chi (two's complement) */
int chi_batch(int Lrows, const int32_t *lam, int nrho, const int32_t *flat,
              const int32_t *off, const int32_t *len, int64_t *out_lo, int64_t *out_hi) {
    int beta[16];
    int rc = prepare(Lrows, lam, beta); if (rc) return rc;
    int N = 0; for (int i = 0; i < L; i++) N += lam[i];
    if (N > NMAX) return -4;
    for (int r = 0; r < nrho; r++) {
        const int32_t *p = flat + off[r]; int k = len[r];
        int s = 0; for (int j = 0; j < k; j++) s += p[j];
        if (s != N) { out_lo[r] = 0; out_hi[r] = 0; continue; }
        compute_sids(p, k, N);
        cur_parts = p; cur_sids = sid_buf; cur_k = k;
        int b2[16]; memcpy(b2, beta, sizeof(int) * L);
        i128 v = chi_rec(b2, 0);
        out_lo[r] = (int64_t)(uint64_t)(v & 0xFFFFFFFFFFFFFFFFULL);
        out_hi[r] = (int64_t)(v >> 64);
    }
    return 0;
}

/* weighted sums: W has nw class functions, each stored as nrho residues mod p1
   then nrho residues mod p2 (layout: W[(k*2 + which)*nrho + r]).  out[k*2+which]. */
int weighted_sums(int Lrows, const int32_t *lam, int nrho, const int32_t *flat,
                  const int32_t *off, const int32_t *len, int nw, const uint64_t *W,
                  uint64_t p1, uint64_t p2, uint64_t *out) {
    int beta[16];
    int rc = prepare(Lrows, lam, beta); if (rc) return rc;
    int N = 0; for (int i = 0; i < L; i++) N += lam[i];
    if (N > NMAX) return -4;
    if (nw > 64) return -5;
    uint64_t pr[2] = {p1, p2};
    u128 acc[64][2];
    for (int k = 0; k < nw; k++) { acc[k][0] = 0; acc[k][1] = 0; }
    for (int r = 0; r < nrho; r++) {
        const int32_t *p = flat + off[r]; int k = len[r];
        int s = 0; for (int j = 0; j < k; j++) s += p[j];
        if (s != N) continue;
        compute_sids(p, k, N);
        cur_parts = p; cur_sids = sid_buf; cur_k = k;
        int b2[16]; memcpy(b2, beta, sizeof(int) * L);
        i128 v = chi_rec(b2, 0);
        if (v == 0) continue;
        for (int w = 0; w < 2; w++) {
            i128 m = v % (i128)pr[w]; if (m < 0) m += pr[w];
            uint64_t vm = (uint64_t)m;
            for (int q = 0; q < nw; q++) {
                uint64_t wv = W[((size_t)q * 2 + w) * nrho + r];
                if (!wv) continue;
                acc[q][w] += (u128)vm * wv;
                if (acc[q][w] >> 120) acc[q][w] %= pr[w];
            }
        }
    }
    for (int q = 0; q < nw; q++)
        for (int w = 0; w < 2; w++) out[q * 2 + w] = (uint64_t)(acc[q][w] % pr[w]);
    return 0;
}
