/* Session 69 -- exact expansion of a two-tall-column bracket monomial into the
 * weight-lambda monomial basis (the Leibniz sum, literally):
 *
 *   F_T = sum_{sigma_1, sigma_2 in S_h} sum_{s in {0,1}^{n2}}
 *           sgn(sigma_1) sgn(sigma_2) (-1)^{|s|}  prod_letters  alpha_l! . c_{alpha_l}
 *
 * Every term is one monomial  prod_l c_{alpha_l}  of the weight-lambda space; its index in
 * the house basis (wk9_s45_build.monomials_array order) is found by the multiset
 * combinadic code of wk9_s42_orbits._codes and a binary search in the sorted codes.
 * Coefficients are accumulated exactly in 128-bit integers.
 *
 * Inputs (all arrays little-endian native ints):
 *   h, d (letters), n (legs per letter), n2, r (variables, = h here), L (= |exps(n, r)|)
 *   cellcol[l*n + q], cellrow[l*n + q]: the n cells of letter l (col 0 = C1, 1 = C2,
 *        2..2+n2-1 = two-columns (row 0/1), >= 2+n2 = one-columns)
 *   tup2a[]: A-index of the sorted n-tuple (i_1<=...<=i_n), flattened base r
 *   afact[a]: alpha! for A-index a
 *   binom[k*L + m] = C(m + k, k + 1)   (k < d, m < L)
 *   sorted_codes[N] ascending, order[N]: row in the house basis of sorted_codes[pos]
 *   out[N] (int64 low/high pairs via two arrays lo[], hi[] = value as __int128 split)
 */
#include <stdint.h>
#include <stdlib.h>
#include <string.h>

typedef long long i64;
typedef __int128 i128;

static int perm_next(int *a, int h) {   /* next permutation in lexicographic order; 0 at the end */
    int i = h - 2;
    while (i >= 0 && a[i] >= a[i + 1]) i--;
    if (i < 0) return 0;
    int j = h - 1;
    while (a[j] <= a[i]) j--;
    int t = a[i]; a[i] = a[j]; a[j] = t;
    for (int l = i + 1, rr = h - 1; l < rr; l++, rr--) { t = a[l]; a[l] = a[rr]; a[rr] = t; }
    return 1;
}

static int perm_sign(const int *a, int h) {
    int s = 1;
    for (int i = 0; i < h; i++) for (int j = i + 1; j < h; j++) if (a[i] > a[j]) s = -s;
    return s;
}

static inline void sort_small(int *v, int k) {
    for (int i = 1; i < k; i++) { int x = v[i], j = i - 1; while (j >= 0 && v[j] > x) { v[j + 1] = v[j]; j--; } v[j + 1] = x; }
}

i64 expand_filling(int h, int d, int n, int n2, int r, int L,
                   const int32_t *cellcol, const int32_t *cellrow,
                   const int32_t *tup2a, const i64 *afact, const i64 *binom,
                   const i64 *sorted_codes, const int64_t *order, i64 N,
                   i64 *out_lo, i64 *out_hi)
{
    i128 *acc = (i128 *)calloc((size_t)N, sizeof(i128));
    if (!acc) return -1;
    int fact_h = 1; for (int i = 2; i <= h; i++) fact_h *= i;
    /* permutation tables */
    int *P = (int *)malloc(sizeof(int) * (size_t)fact_h * h);
    int *PS = (int *)malloc(sizeof(int) * (size_t)fact_h);
    { int a[16]; for (int i = 0; i < h; i++) a[i] = i; int c = 0;
      do { memcpy(P + (size_t)c * h, a, sizeof(int) * h); PS[c] = perm_sign(a, h); c++; } while (perm_next(a, h));
      if (c != fact_h) { free(acc); free(P); free(PS); return -2; } }
    i64 nterms = 0;
    int ids[8]; int aidx[64]; int idxsorted[64];
    /* powers of r for tup2a flattening */
    int rp[8]; rp[0] = 1; for (int q = 1; q < 8; q++) rp[q] = rp[q - 1] * r;
    for (int s = 0; s < (1 << n2); s++) {
        int ssign = (__builtin_popcount(s) & 1) ? -1 : 1;
        for (int p1 = 0; p1 < fact_h; p1++) {
            const int *sig1 = P + (size_t)p1 * h;
            for (int p2 = 0; p2 < fact_h; p2++) {
                const int *sig2 = P + (size_t)p2 * h;
                int sign = ssign * PS[p1] * PS[p2];
                i64 fprod = 1;
                for (int l = 0; l < d; l++) {
                    for (int q = 0; q < n; q++) {
                        int col = cellcol[l * n + q], row = cellrow[l * n + q];
                        int id;
                        if (col == 0) id = sig1[row];
                        else if (col == 1) id = sig2[row];
                        else if (col < 2 + n2) { int e = col - 2; int bit = (s >> e) & 1; id = (row == 0) ? bit : 1 - bit; }
                        else id = 0;
                        ids[q] = id;
                    }
                    sort_small(ids, n);
                    int key = 0; for (int q = 0; q < n; q++) key += ids[q] * rp[q];
                    int a = tup2a[key];
                    aidx[l] = a;
                    fprod *= afact[a];
                }
                memcpy(idxsorted, aidx, sizeof(int) * d);
                sort_small(idxsorted, d);
                i64 code = 0;
                for (int k = 0; k < d; k++) code += binom[(size_t)k * L + idxsorted[k]];
                /* binary search */
                i64 lo = 0, hi = N - 1, pos = -1;
                while (lo <= hi) { i64 mid = (lo + hi) >> 1; i64 c = sorted_codes[mid];
                    if (c == code) { pos = mid; break; } else if (c < code) lo = mid + 1; else hi = mid - 1; }
                if (pos < 0) { free(acc); free(P); free(PS); return -3; }
                i64 rowidx = order[pos];
                acc[rowidx] += (i128)(sign * fprod);
                nterms++;
            }
        }
    }
    for (i64 i = 0; i < N; i++) {
        i128 v = acc[i];
        out_lo[i] = (i64)(v & 0xFFFFFFFFFFFFFFFFLL);   /* low 64 bits as unsigned pattern */
        out_hi[i] = (i64)(v >> 64);
    }
    free(acc); free(P); free(PS);
    return nterms;
}
