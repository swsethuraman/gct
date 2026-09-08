/* Session 71 -- dense-residual helpers for the hybrid route, mod p < 2^31.
 *
 * All matrices are row-major uint32 (values in [0, p)); sparse matrices are CSR
 * with int64 indptr, int32 indices and uint32 data already reduced mod p.
 * Every product of two residues is < 2^62 and every accumulation adds one
 * residue (< 2^31) to it, so uint64 arithmetic never overflows.
 *
 *   trisolve       X := T^{-1} B in place, T upper triangular in CSR over the
 *                  cover positions (row i has its diagonal at column i and every
 *                  other entry at a column > i; dinv[i] = T[i,i]^{-1} mod p).
 *   schur_project  G += sum_r  sign_{r,q} * ( F_r[U] - F_r[S] X )  over the
 *                  rows r of F (global column indices, colS/colU give the
 *                  position of a column in S / U or -1) and the nproj
 *                  pseudo-random (row, sign) pairs of a fixed-seed generator:
 *                  G is the +-1 sparse projection of the Schur complement.
 *   spmm_mod       Y := A X for CSR A (global columns, int32 data of any sign)
 *                  and dense X (n x m), used for the sparse-times-dense products.
 */
#include <stdint.h>
#include <stdlib.h>
#include <string.h>

static inline uint64_t splitmix(uint64_t *z) {
    uint64_t x = (*z += 0x9E3779B97F4A7C15ULL);
    x = (x ^ (x >> 30)) * 0xBF58476D1CE4E5B9ULL;
    x = (x ^ (x >> 27)) * 0x94D049BB133111EBULL;
    return x ^ (x >> 31);
}

int trisolve(int64_t nS, int64_t m, const int64_t *indptr, const int32_t *indices,
             const uint32_t *data, const uint32_t *dinv, uint32_t *B, uint64_t p)
{
    if (p >= (1ULL << 31)) return -2;
    for (int64_t i = nS - 1; i >= 0; i--) {
        uint32_t *xi = B + i * m;
        for (int64_t k = indptr[i]; k < indptr[i + 1]; k++) {
            int64_t j = indices[k];
            if (j == i) continue;
            if (j < i) return -1;
            uint64_t t = data[k] % p;
            if (t == 0) continue;
            uint64_t nt = p - t;
            const uint32_t *xj = B + j * m;
            for (int64_t u = 0; u < m; u++)
                xi[u] = (uint32_t)((xi[u] + nt * (uint64_t)xj[u]) % p);
        }
        uint64_t di = dinv[i];
        if (di != 1)
            for (int64_t u = 0; u < m; u++)
                xi[u] = (uint32_t)(((uint64_t)xi[u] * di) % p);
    }
    return 0;
}

int schur_project(int64_t nrows, const int64_t *indptr, const int32_t *indices,
                  const uint32_t *data, const int32_t *colS, const int32_t *colU,
                  const uint32_t *X, int64_t nU, int64_t mrows, uint32_t *G,
                  uint64_t p, uint64_t seed, int nproj)
{
    if (p >= (1ULL << 31)) return -2;
    uint32_t *s = (uint32_t *)malloc((size_t)nU * sizeof(uint32_t));
    if (!s) return -3;
    for (int64_t r = 0; r < nrows; r++) {
        memset(s, 0, (size_t)nU * sizeof(uint32_t));
        int any = 0;
        for (int64_t k = indptr[r]; k < indptr[r + 1]; k++) {
            int64_t c = indices[k];
            uint64_t v = data[k] % p;
            if (!v) continue;
            int32_t u = colU[c];
            if (u >= 0) { s[u] = (uint32_t)((s[u] + v) % p); any = 1; continue; }
            int32_t j = colS[c];
            if (j < 0) { free(s); return -4; }
            uint64_t nv = p - v;
            const uint32_t *xj = X + (int64_t)j * nU;
            for (int64_t uu = 0; uu < nU; uu++)
                s[uu] = (uint32_t)((s[uu] + nv * (uint64_t)xj[uu]) % p);
            any = 1;
        }
        if (!any) continue;
        uint64_t z = seed ^ (0xD1B54A32D192ED03ULL * (uint64_t)(r + 1));
        for (int q = 0; q < nproj; q++) {
            uint64_t x = splitmix(&z);
            int64_t t = (int64_t)(x % (uint64_t)mrows);
            int sign = (int)((x >> 40) & 1);
            uint32_t *g = G + t * nU;
            if (sign) {
                for (int64_t uu = 0; uu < nU; uu++) { uint64_t val = (uint64_t)g[uu] + s[uu]; g[uu] = (uint32_t)(val >= p ? val - p : val); }
            } else {
                for (int64_t uu = 0; uu < nU; uu++) { uint64_t val = (uint64_t)g[uu] + p - s[uu]; g[uu] = (uint32_t)(val >= p ? val - p : val); }
            }
        }
    }
    free(s);
    return 0;
}

int spmm_mod(int64_t nrows, const int64_t *indptr, const int32_t *indices, const int32_t *data,
             const uint32_t *X, int64_t m, uint32_t *Y, uint64_t p)
{
    if (p >= (1ULL << 31)) return -2;
    for (int64_t r = 0; r < nrows; r++) {
        uint32_t *y = Y + r * m;
        memset(y, 0, (size_t)m * sizeof(uint32_t));
        for (int64_t k = indptr[r]; k < indptr[r + 1]; k++) {
            int64_t c = indices[k];
            int64_t vraw = data[k];
            uint64_t v = (uint64_t)(((vraw % (int64_t)p) + (int64_t)p) % (int64_t)p);
            if (!v) continue;
            const uint32_t *x = X + c * m;
            for (int64_t u = 0; u < m; u++)
                y[u] = (uint32_t)((y[u] + v * (uint64_t)x[u]) % p);
        }
    }
    return 0;
}
