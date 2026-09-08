/* Session 69 -- exact mod-p evaluation of a two-tall-column bracket monomial
 * (docs/compact_circuit.md, Identity 3):
 *
 *   F_T = sgn(pi) * sum_{s in {0,1}^{n2}} (-1)^{|s|} N(s)
 *                 * sum_{S subset [h]} (-1)^{h-|S|} det( sum_{k in S} M_k(s) )
 *
 * with M_k(s) the h x h symbol matrix of the k-th row-unit of C1 (a shared letter's
 * tensor, or the rank-one product v w^T of a C1-only letter and its C2-only partner)
 * and N(s) the scalar product of the letters in neither tall column.  The sign
 * sgn(pi) (relative row order of C2) is applied by the caller.
 *
 * Arithmetic: p < 2^31, so every product of two residues fits in 64 bits.
 * Determinants by Gaussian elimination mod p; subset sums in Gray-code order.
 * Compiled by wk11_s69_circuit._clib():  gcc -O3 -march=native -shared -fPIC
 */
#include <stdint.h>
#include <string.h>

typedef unsigned long long u64;
typedef long long i64;

static inline u64 mulmod(u64 a, u64 b, u64 p) { return (a * b) % p; }

static u64 invmod(u64 a, u64 p) {
    i64 t = 0, newt = 1;
    i64 r = (i64)p, newr = (i64)(a % p);
    while (newr) {
        i64 q = r / newr, tmp;
        tmp = t - q * newt; t = newt; newt = tmp;
        tmp = r - q * newr; r = newr; newr = tmp;
    }
    if (t < 0) t += (i64)p;
    return (u64)t;
}

#define HMAX 9

static u64 det_mod(u64 A[HMAX][HMAX], int h, u64 p) {
    u64 M[HMAX][HMAX];
    memcpy(M, A, sizeof(M));
    u64 det = 1;
    for (int c = 0; c < h; c++) {
        int piv = -1;
        for (int r = c; r < h; r++) if (M[r][c]) { piv = r; break; }
        if (piv < 0) return 0;
        if (piv != c) {
            for (int j = 0; j < h; j++) { u64 t = M[c][j]; M[c][j] = M[piv][j]; M[piv][j] = t; }
            det = p - det; if (det == p) det = 0;
        }
        det = mulmod(det, M[c][c], p);
        u64 inv = invmod(M[c][c], p);
        for (int r = c + 1; r < h; r++) {
            if (!M[r][c]) continue;
            u64 f = mulmod(M[r][c], inv, p);
            for (int j = c; j < h; j++) {
                u64 t = mulmod(f, M[c][j], p);
                M[r][j] = (M[r][j] + p - t) % p;
            }
        }
    }
    return det;
}

/* letters: l_inC1[l], l_inC2[l], l_d2[l] (number of 2-legs), l_edge[l*maxd2+q] (edge id),
 * l_side[l*maxd2+q] (0 = row-1 letter of that 2-column, 1 = row-2), tensor at
 * tens[l_off[l] + ((i*nj)+j) << d2 | bits], ni = h if inC1 else 1, nj = h if inC2 else 1.
 * units: u_type[k] (0 shared: letter u_a[k]; 1 pair: C1-only u_a[k], C2-only u_b[k]).
 * nei: letters in neither tall column.  Returns the value without sgn(pi). */
i64 eval_filling(int h, int d, int n2, i64 pp,
                 const int32_t *l_inC1, const int32_t *l_inC2, const int32_t *l_d2,
                 const int32_t *l_edge, const int32_t *l_side, int maxd2,
                 const i64 *l_off, const i64 *tens,
                 const int32_t *u_type, const int32_t *u_a, const int32_t *u_b,
                 int nnei, const int32_t *nei)
{
    u64 p = (u64)pp;
    u64 total = 0;
    int bits[64];
    u64 M[HMAX][HMAX][HMAX];   /* M[k][i][j] */
    u64 Ssum[HMAX][HMAX];
    u64 vtmp[HMAX], wtmp[HMAX];
    for (u64 s = 0; s < (1ULL << n2); s++) {
        int par = __builtin_popcountll(s) & 1;
        for (int l = 0; l < d; l++) {
            int b = 0;
            for (int q = 0; q < l_d2[l]; q++) {
                int e = l_edge[l * maxd2 + q];
                int se = (int)((s >> e) & 1ULL);
                int idx = l_side[l * maxd2 + q] == 0 ? se : 1 - se;
                b |= idx << q;
            }
            bits[l] = b;
        }
        u64 N = 1;
        for (int t = 0; t < nnei; t++) {
            int l = nei[t];
            N = mulmod(N, (u64)tens[l_off[l] + bits[l]], p);
            if (!N) break;
        }
        if (!N) continue;
        for (int k = 0; k < h; k++) {
            if (u_type[k] == 0) {
                int l = u_a[k]; int d2 = l_d2[l];
                const i64 *T = tens + l_off[l];
                for (int i = 0; i < h; i++)
                    for (int j = 0; j < h; j++)
                        M[k][i][j] = (u64)T[(((i * h) + j) << d2) | bits[l]];
            } else {
                int la = u_a[k], lb = u_b[k];
                const i64 *Ta = tens + l_off[la]; const i64 *Tb = tens + l_off[lb];
                int da = l_d2[la], db = l_d2[lb];
                for (int i = 0; i < h; i++) vtmp[i] = (u64)Ta[(i << da) | bits[la]];      /* nj = 1 */
                for (int j = 0; j < h; j++) wtmp[j] = (u64)Tb[(j << db) | bits[lb]];      /* ni = 1 */
                for (int i = 0; i < h; i++)
                    for (int j = 0; j < h; j++)
                        M[k][i][j] = mulmod(vtmp[i], wtmp[j], p);
            }
        }
        /* subset sum in Gray-code order */
        memset(Ssum, 0, sizeof(Ssum));
        u64 acc = 0;
        u64 gray_prev = 0;
        /* S = 0: det of zero matrix = 0 (h >= 1), sign irrelevant */
        for (u64 g = 1; g < (1ULL << h); g++) {
            u64 gray = g ^ (g >> 1);
            u64 diff = gray ^ gray_prev;
            int k = __builtin_ctzll(diff);
            int add = (gray >> k) & 1;
            for (int i = 0; i < h; i++)
                for (int j = 0; j < h; j++) {
                    if (add) { Ssum[i][j] += M[k][i][j]; if (Ssum[i][j] >= p) Ssum[i][j] -= p; }
                    else     { Ssum[i][j] = (Ssum[i][j] + p - M[k][i][j]) % p; }
                }
            gray_prev = gray;
            u64 dS = det_mod(Ssum, h, p);
            if ((h - __builtin_popcountll(gray)) & 1) dS = dS ? p - dS : 0;
            acc += dS; if (acc >= p) acc -= p;
        }
        u64 term = mulmod(N, acc, p);
        if (par) term = term ? p - term : 0;
        total += term; if (total >= p) total -= p;
    }
    return (i64)total;
}
