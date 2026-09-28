/* B28-01 verifier -- its own upper-triangular solve mod p (p < 2^31).
 *
 * Written for analysis/b28_01_verify.py; shares no code with the producer's
 * analysis/wk11_s71_schur.c.  T is given as a strictly-upper CSR part
 * (up_ptr/up_idx/up_val, every column index > its row, values in [0, p))
 * plus the diagonal inverses dinv[i]; Y (nS x w, row-major uint64 values in
 * [0, p)) is overwritten by T^{-1} Y.  Every term is (p-1)^2 + (p-1) < 2^62,
 * so the uint64 accumulator reduced after each term cannot overflow.
 */
#include <stdint.h>
#include <stdlib.h>

int vfy_upper_solve(int64_t nS, int64_t w, const int64_t *up_ptr, const int64_t *up_idx,
                    const uint64_t *up_val, const uint64_t *dinv, uint64_t *Y, uint64_t p)
{
    if (p >= (1ULL << 31) || p < 2) return -2;
    uint64_t *acc = (uint64_t *)malloc((size_t)(w > 0 ? w : 1) * sizeof(uint64_t));
    if (!acc) return -3;
    for (int64_t i = nS - 1; i >= 0; i--) {
        uint64_t *yi = Y + i * w;
        for (int64_t c = 0; c < w; c++) acc[c] = yi[c];
        for (int64_t k = up_ptr[i]; k < up_ptr[i + 1]; k++) {
            int64_t j = up_idx[k];
            if (j <= i || j >= nS) { free(acc); return -1; }
            uint64_t neg = (p - up_val[k] % p) % p;
            if (!neg) continue;
            const uint64_t *yj = Y + j * w;
            for (int64_t c = 0; c < w; c++) acc[c] = (acc[c] + neg * yj[c]) % p;
        }
        uint64_t d = dinv[i];
        for (int64_t c = 0; c < w; c++) yi[c] = (acc[c] * d) % p;
    }
    free(acc);
    return 0;
}
