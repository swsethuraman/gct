/*
 * Session 42 -- sparse full-column-rank / kernel certificates by Wiedemann over F_p.
 *
 * Input: a sparse matrix E (nrows x n, CSR, entries mod p) and optionally k extra
 * dense random rows R (generated here from a seed) -- the matrix tested is
 * F = [E; R].  Let M = F^T D F with D a random diagonal (and a random diagonal
 * column scaling D2, so M = D2 F^T D F D2, symmetric).  For random D the rank of
 * M equals the rank of F with probability >= 1 - n/p (Cauchy-Binet +
 * Schwartz-Zippel).  A Wiedemann sequence s_i = u^T M^i b, i < 2n, with minimal
 * polynomial f (Berlekamp-Massey) of degree exactly n and f(0) != 0 PROVES M
 * nonsingular (the sequence's minimal polynomial divides M's, which divides the
 * characteristic polynomial; degree n forces equality, and f(0) = +-det M), hence
 * F injective, hence E has no kernel vector killed by R.  "M nonsingular => F
 * injective" uses no randomness.  If instead f = x^s g with s >= 1, the vector
 * y = M^{s-1} g(M) b is a candidate kernel vector of M; it is VERIFIED here by
 * the sparse products E y = 0 and R y = 0 before being reported.
 *
 * Every number reported is therefore backed by an object checkable with sparse
 * products (a kernel vector) or by the BM minimal polynomial, which is also
 * checked here to annihilate the whole sequence.
 *
 * usage: wied <csrfile> <p> <seed> <k_extra> [maxhorner]
 * csrfile (little-endian): int64 n, int64 nrows, int64 nnz, then
 *   int64 rowptr[nrows+1], int32 col[nnz], uint32 val[nnz] (already reduced mod p)
 * output lines: "SEQ ..." diagnostics, then one of
 *   NONSINGULAR deg=n f0=<f(0)>
 *   KERNEL <n entries>            (a verified vector y with E y = 0, R y = 0, y != 0)
 *   INCONCLUSIVE <reason>
 */
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <string.h>
#include <time.h>

typedef uint64_t u64; typedef int64_t i64; typedef unsigned __int128 u128;
static u64 P;

static u64 rng_state;
static u64 rng64(void) {           /* splitmix64 */
    u64 z = (rng_state += 0x9E3779B97F4A7C15ULL);
    z = (z ^ (z >> 30)) * 0xBF58476D1CE4E5B9ULL;
    z = (z ^ (z >> 27)) * 0x94D049BB133111EBULL;
    return z ^ (z >> 31);
}
static u64 rnd_nonzero(void) { u64 v; do { v = rng64() % P; } while (v == 0); return v; }
static u64 rnd_mod(void) { return rng64() % P; }

static u64 mulmod(u64 a, u64 b) { return (u64)(((u128)a * b) % P); }
static u64 powmod(u64 a, u64 e) { u64 r = 1; while (e) { if (e & 1) r = mulmod(r, a); a = mulmod(a, a); e >>= 1; } return r; }
static u64 inv(u64 a) { return powmod(a % P, P - 2); }

static i64 n, nrows, nnz, kx;
static i64 *rowptr; static int32_t *col; static uint32_t *val;      /* CSR of E */
static i64 *colptr; static int32_t *rowi; static uint32_t *valc;    /* CSC of E, values pre-scaled by D1[row] */
static u64 *R;      /* kx x n dense extra rows */
static u64 *D1;     /* nrows + kx */
static u64 *D2;     /* n */
static u64 *tmp_r;  /* nrows + kx */
static u64 PSHIFT;  /* P << 32, < 2^63 for P < 2^31: subtracting it keeps a u64 accumulator of products < 2^62 below 2^63 */

/* accumulate products a*b (< 2^62) into a u64 kept below 2^63 */
#define ACC(acc, prod) do { (acc) += (prod); if ((acc) >> 63) (acc) -= PSHIFT; } while (0)

static void build_csc(void) {
    colptr = calloc(n + 1, sizeof(i64)); rowi = malloc(sizeof(int32_t) * (nnz + 1)); valc = malloc(sizeof(uint32_t) * (nnz + 1));
    for (i64 t = 0; t < nnz; t++) colptr[col[t] + 1]++;
    for (i64 j = 0; j < n; j++) colptr[j + 1] += colptr[j];
    i64 *fill = malloc(sizeof(i64) * (n + 1)); memcpy(fill, colptr, sizeof(i64) * (n + 1));
    for (i64 i = 0; i < nrows; i++)
        for (i64 t = rowptr[i]; t < rowptr[i + 1]; t++) {
            i64 q = fill[col[t]]++; rowi[q] = (int32_t)i; valc[q] = (uint32_t)mulmod(val[t], D1[i]);
        }
    free(fill);
}

/* y = M x, M = D2 F^T D1 F D2, F = [E; R] */
static void matvec(const u64 *x, u64 *y, u64 *xs) {
    for (i64 j = 0; j < n; j++) xs[j] = mulmod(x[j], D2[j]);
    for (i64 i = 0; i < nrows; i++) {
        u64 acc = 0;
        for (i64 t = rowptr[i]; t < rowptr[i + 1]; t++) ACC(acc, (u64)val[t] * xs[col[t]]);
        tmp_r[i] = acc % P;                       /* D1 is folded into valc */
    }
    for (i64 e = 0; e < kx; e++) {
        const u64 *rr = R + e * n; u64 acc = 0;
        for (i64 j = 0; j < n; j++) ACC(acc, rr[j] * xs[j]);
        tmp_r[nrows + e] = mulmod(acc % P, D1[nrows + e]);
    }
    for (i64 j = 0; j < n; j++) {
        u64 acc = 0;
        for (i64 t = colptr[j]; t < colptr[j + 1]; t++) ACC(acc, (u64)valc[t] * tmp_r[rowi[t]]);
        y[j] = acc % P;
    }
    for (i64 e = 0; e < kx; e++) {
        u64 z = tmp_r[nrows + e]; if (!z) continue; const u64 *rr = R + e * n;
        for (i64 j = 0; j < n; j++) { u64 v = y[j] + mulmod(rr[j], z); if (v >= P) v -= P; y[j] = v; }
    }
    for (i64 j = 0; j < n; j++) y[j] = mulmod(y[j], D2[j]);
}

/* F x: returns 1 if E x == 0 and R x == 0 */
static int check_kernel(const u64 *x) {
    for (i64 i = 0; i < nrows; i++) {
        u64 acc = 0;
        for (i64 t = rowptr[i]; t < rowptr[i + 1]; t++) ACC(acc, (u64)val[t] * x[col[t]]);
        if (acc % P) return 0;
    }
    for (i64 e = 0; e < kx; e++) {
        const u64 *rr = R + e * n; u64 acc = 0;
        for (i64 j = 0; j < n; j++) ACC(acc, rr[j] * x[j]);
        if (acc % P) return 0;
    }
    return 1;
}

/* Berlekamp-Massey: s[0..N-1] -> connection polynomial C (C[0]=1), length L.
   minimal polynomial f(x) = x^L + C[1] x^{L-1} + ... + C[L]. */
static i64 berlekamp_massey(const u64 *s, i64 N, u64 *C) {
    u64 *B = malloc(sizeof(u64) * (N + 1)); u64 *T = malloc(sizeof(u64) * (N + 1));
    memset(C, 0, sizeof(u64) * (N + 1)); memset(B, 0, sizeof(u64) * (N + 1));
    C[0] = 1; B[0] = 1; i64 L = 0, m = 1; u64 b = 1;
    for (i64 i = 0; i < N; i++) {
        u128 acc = s[i];
        for (i64 j = 1; j <= L; j++) { acc += (u128)C[j] * s[i - j]; }
        u64 d = (u64)(acc % P);
        if (d == 0) { m++; continue; }
        u64 coef = mulmod(d, inv(b));
        if (2 * L <= i) {
            memcpy(T, C, sizeof(u64) * (L + 1));
            for (i64 j = 0; j + m <= N; j++) { if (!B[j]) continue; u64 v = C[j + m] + P - mulmod(coef, B[j]); if (v >= P) v -= P; C[j + m] = v; }
            i64 Lnew = i + 1 - L;
            memcpy(B, T, sizeof(u64) * (L + 1)); memset(B + L + 1, 0, sizeof(u64) * (N - L));
            L = Lnew; b = d; m = 1;
        } else {
            for (i64 j = 0; j + m <= N; j++) { if (!B[j]) continue; u64 v = C[j + m] + P - mulmod(coef, B[j]); if (v >= P) v -= P; C[j + m] = v; }
            m++;
        }
    }
    free(B); free(T);
    return L;
}

int main(int argc, char **argv) {
    if (argc < 5) { fprintf(stderr, "usage: wied csrfile p seed k_extra [maxhorner]\n"); return 2; }
    FILE *f = fopen(argv[1], "rb"); if (!f) { perror("open"); return 2; }
    P = strtoull(argv[2], 0, 10); if (P <= (1ULL << 30) || P >= (1ULL << 31)) { fprintf(stderr, "need 2^30 < p < 2^31\n"); return 2; } u64 seed = strtoull(argv[3], 0, 10); kx = atoll(argv[4]);
    rng_state = seed * 0x9E3779B97F4A7C15ULL + P;
    if (fread(&n, 8, 1, f) != 1 || fread(&nrows, 8, 1, f) != 1 || fread(&nnz, 8, 1, f) != 1) return 2;
    rowptr = malloc(sizeof(i64) * (nrows + 1)); col = malloc(sizeof(int32_t) * (nnz + 1)); val = malloc(sizeof(uint32_t) * (nnz + 1));
    if (fread(rowptr, 8, nrows + 1, f) != (size_t)(nrows + 1)) return 2;
    if (nnz && fread(col, 4, nnz, f) != (size_t)nnz) return 2;
    if (nnz && fread(val, 4, nnz, f) != (size_t)nnz) return 2;
    fclose(f);
    i64 N = 2 * n;
    D1 = malloc(sizeof(u64) * (nrows + kx)); D2 = malloc(sizeof(u64) * n); tmp_r = malloc(sizeof(u64) * (nrows + kx));
    R = kx ? malloc(sizeof(u64) * kx * n) : NULL;
    for (i64 i = 0; i < nrows + kx; i++) D1[i] = rnd_nonzero();
    for (i64 j = 0; j < n; j++) D2[j] = rnd_nonzero();
    for (i64 t = 0; t < kx * n; t++) R[t] = rnd_mod();
    PSHIFT = P << 32;
    build_csc();
    u64 *u = malloc(sizeof(u64) * n), *b0 = malloc(sizeof(u64) * n), *x = malloc(sizeof(u64) * n), *y = malloc(sizeof(u64) * n), *xs = malloc(sizeof(u64) * n);
    for (i64 j = 0; j < n; j++) { u[j] = rnd_mod(); b0[j] = rnd_mod(); }
    u64 *s = malloc(sizeof(u64) * (N + 1));
    clock_t t0 = clock();
    memcpy(x, b0, sizeof(u64) * n);
    for (i64 i = 0; i < N; i++) {
        u128 acc = 0;
        for (i64 j = 0; j < n; j++) { acc += (u128)u[j] * x[j]; }
        s[i] = (u64)(acc % P);
        if (i + 1 < N) { matvec(x, y, xs); u64 *t = x; x = y; y = t; }
    }
    fprintf(stdout, "SEQ n=%lld nrows=%lld nnz=%lld k=%lld len=%lld secs=%.1f\n", (long long)n, (long long)nrows, (long long)nnz, (long long)kx, (long long)N, (double)(clock() - t0) / CLOCKS_PER_SEC);
    u64 *C = malloc(sizeof(u64) * (N + 2));
    i64 L = berlekamp_massey(s, N, C);
    /* verify: C annihilates the sequence: s[i] + sum_{j=1..L} C[j] s[i-j] = 0 for all i >= L */
    for (i64 i = L; i < N; i++) {
        u128 acc = s[i];
        for (i64 j = 1; j <= L; j++) { acc += (u128)C[j] * s[i - j]; }
        if (acc % P) { fprintf(stdout, "INCONCLUSIVE bm-verify-failed\n"); return 0; }
    }
    /* f(x) = x^L + C[1] x^{L-1} + ... + C[L];  f(0) = C[L] (or 1 if L = 0) */
    u64 f0 = (L == 0) ? 1 : C[L];
    fprintf(stdout, "BM deg=%lld f0=%llu secs=%.1f\n", (long long)L, (unsigned long long)f0, (double)(clock() - t0) / CLOCKS_PER_SEC);
    if (L == n && f0 != 0) { fprintf(stdout, "NONSINGULAR deg=%lld f0=%llu\n", (long long)L, (unsigned long long)f0); return 0; }
    if (f0 != 0) { fprintf(stdout, "INCONCLUSIVE deg<n f0!=0 (minpoly of sequence not full; retry)\n"); return 0; }
    /* f = x^s g: s = number of trailing zero coefficients of f, i.e. C[L], C[L-1], ... zero */
    i64 sdeg = 0; while (sdeg < L && C[L - sdeg] == 0) sdeg++;
    /* g(x) = x^{L-s} + C[1] x^{L-s-1} + ... + C[L-s]; Horner over M: w = g(M) b */
    i64 dg = L - sdeg;
    i64 maxh = (argc > 5) ? atoll(argv[5]) : n + 5;
    if (dg + sdeg > maxh) { fprintf(stdout, "INCONCLUSIVE horner-too-long\n"); return 0; }
    u64 *w = malloc(sizeof(u64) * n);
    memcpy(w, b0, sizeof(u64) * n);                   /* coefficient of x^{dg} is 1 */
    for (i64 j = 1; j <= dg; j++) {                   /* w = M w + C[j] b */
        matvec(w, y, xs);
        u64 c = C[j];
        for (i64 t = 0; t < n; t++) { u64 v = y[t] + mulmod(c, b0[t]); if (v >= P) v -= P; w[t] = v; }
    }
    for (i64 j = 1; j < sdeg; j++) { matvec(w, y, xs); memcpy(w, y, sizeof(u64) * n); }
    /* M w = 0 with M = D2 F^T D1 F D2  =>  F (D2 w) = 0 for generic D1: unscale */
    for (i64 t = 0; t < n; t++) w[t] = mulmod(w[t], D2[t]);
    int nz = 0; for (i64 t = 0; t < n; t++) if (w[t]) { nz = 1; break; }
    if (!nz) { fprintf(stdout, "INCONCLUSIVE kernel-candidate-zero\n"); return 0; }
    if (!check_kernel(w)) { fprintf(stdout, "INCONCLUSIVE candidate-not-in-kernel (D unlucky or derogatory)\n"); return 0; }
    fprintf(stdout, "KERNEL");
    for (i64 t = 0; t < n; t++) fprintf(stdout, " %llu", (unsigned long long)w[t]);
    fprintf(stdout, "\n");
    fprintf(stdout, "DONE secs=%.1f\n", (double)(clock() - t0) / CLOCKS_PER_SEC);
    return 0;
}
