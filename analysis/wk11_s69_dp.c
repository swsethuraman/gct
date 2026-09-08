/* Session 69 -- the exterior-algebra (Grassmann) evaluator of a two-tall-column bracket
 * monomial, docs/compact_circuit.md section 4 (the second evaluator; the first is the
 * mixed-discriminant one in wk11_s69_eval.c).
 *
 * The two tall columns are Berezin integrals:  det[v_1..v_h] = coefficient of
 * theta_1...theta_h in prod_k (sum_i v_k(i) theta_i).  Letters are processed one at a time in
 * a chosen order; the state is the coefficient vector over (mask1, mask2, open) where mask1
 * (mask2) is the set of C1 (C2) indices already used -- an element of Lambda^p(C^h) tensor
 * Lambda^q(C^h) -- and `open` records the index chosen at the first-processed endpoint of
 * every 2-column whose second endpoint is still to come.  A letter multiplies the state by its
 * symbol tensor: it wedges theta_i (i not in mask1) and eta_j (j not in mask2) at the END of
 * the products (sign (-1)^{#used indices above i}), branches on the index of every 2-column it
 * opens, and closes the 2-columns whose partner is already processed (index forced, sign
 * (-1)^{s_e} with s_e = 0 iff the row-1 letter of that column got index 1).
 *
 * The final coefficient at (full, full, no open) times the signs of the two row-order
 * permutations of the processing order is F_T (same definition, same value as wk11_s69_eval.c).
 * Cost: sum over letters of |populated states| x h^2 x 2^{#opened}, with |populated| <=
 * C(h,p) C(h,q) 2^{W}, W the maximum number of simultaneously open 2-columns.
 *
 * Arithmetic mod p < 2^31 in 64-bit.  Compiled by wk11_s69_circuit._dplib().
 */
#include <stdint.h>
#include <stdlib.h>
#include <string.h>

typedef unsigned long long u64;
typedef long long i64;

static inline u64 mulmod(u64 a, u64 b, u64 p) { return (a * b) % p; }

/* letters in PROCESSING order (the caller permutes everything):
 *   inC1[l], inC2[l]; d2[l] = number of 2-legs; for q < d2[l]: eid[l*maxd2+q] = edge id,
 *   side[l*maxd2+q] = 0/1 (row of the letter in that 2-column);
 *   tensor at tens[off[l] + ((i*nj)+j) << d2 | bits], ni = h or 1, nj = h or 1;
 * edges: slot[e] in [0, W), first[e] = processing index of the first endpoint,
 *   firstside[e] = side of that endpoint.
 * Returns the coefficient at (full, full, 0); the caller multiplies by the row-order signs. */
i64 dp_eval(int h, int d, int n2, int W, i64 pp,
            const int32_t *inC1, const int32_t *inC2, const int32_t *d2,
            const int32_t *eid, const int32_t *side, int maxd2,
            const i64 *off, const i64 *tens,
            const int32_t *slot, const int32_t *first, const int32_t *firstside)
{
    u64 p = (u64)pp;
    const int NM = 1 << h;
    const size_t NO = (size_t)1 << W;
    size_t SZ = (size_t)NM * NM * NO;
    u64 *cur = (u64 *)calloc(SZ, sizeof(u64));
    u64 *nxt = (u64 *)calloc(SZ, sizeof(u64));
    if (!cur || !nxt) { free(cur); free(nxt); return -1; }
    cur[0] = 1;
    int p1 = 0, q1 = 0;             /* popcounts of the populated masks */
    /* lists of masks by popcount */
    int *masks = (int *)malloc(sizeof(int) * NM); int cnt[16]; int start[17];
    { int c = 0; for (int pc = 0; pc <= h; pc++) { start[pc] = c; for (int m = 0; m < NM; m++) if (__builtin_popcount(m) == pc) masks[c++] = m; cnt[pc] = c - start[pc]; } start[h + 1] = c; }
    /* open-slot occupancy is implied by the edges: at letter l, the set of open slots is known */
    int *openmask_at = (int *)calloc(d + 1, sizeof(int));   /* which slots are open BEFORE processing letter l */
    { int om = 0;
      for (int l = 0; l < d; l++) {
          openmask_at[l] = om;
          for (int q = 0; q < d2[l]; q++) {          /* closes first, then opens */
              int e = eid[l * maxd2 + q];
              if (first[e] != l) om &= ~(1 << slot[e]);
          }
          for (int q = 0; q < d2[l]; q++) {
              int e = eid[l * maxd2 + q];
              if (first[e] == l) om |= 1 << slot[e];
          }
      }
      openmask_at[d] = om; }
    for (int l = 0; l < d; l++) {
        memset(nxt, 0, SZ * sizeof(u64));
        int c1 = inC1[l], c2 = inC2[l];
        int nj = c2 ? h : 1;
        int dd = d2[l];
        const i64 *T = tens + off[l];
        int om = openmask_at[l];
        /* classify this letter's edges */
        int nopen = 0, opens[8], opens_side[8], closes[8], closes_slot[8], closes_fside[8], nclose = 0, qpos_open[8], qpos_close[8];
        for (int q = 0; q < dd; q++) {
            int e = eid[l * maxd2 + q];
            if (first[e] == l) { opens[nopen] = slot[e]; opens_side[nopen] = side[l * maxd2 + q]; qpos_open[nopen] = q; nopen++; }
            else { closes[nclose] = e; closes_slot[nclose] = slot[e]; closes_fside[nclose] = firstside[e]; qpos_close[nclose] = q; nclose++; }
        }
        int np1 = p1 + c1, nq1 = q1 + c2;
        for (int a = 0; a < cnt[p1]; a++) {
            int m1 = masks[start[p1] + a];
            for (int b = 0; b < cnt[q1]; b++) {
                int m2 = masks[start[q1] + b];
                size_t base = ((size_t)m1 * NM + m2) * NO;
                for (size_t o = 0; o < NO; o++) {
                    if ((int)(o & ~(size_t)om) != 0) continue;       /* only the open slots may be set */
                    u64 val = cur[base + o];
                    if (!val) continue;
                    /* closing edges: indices forced, sign accumulated */
                    int bits_close = 0; int sgn = 0;
                    for (int t = 0; t < nclose; t++) {
                        int x = (int)((o >> closes_slot[t]) & 1);          /* index bit of the first endpoint */
                        int myidx = 1 - x;
                        bits_close |= myidx << qpos_close[t];
                        /* s_e = 0 iff the row-1 letter got index 1 (bit 0) */
                        int row1bit = (closes_fside[t] == 0) ? x : myidx;
                        sgn ^= row1bit;
                    }
                    size_t o2base = o;
                    for (int t = 0; t < nclose; t++) o2base &= ~((size_t)1 << closes_slot[t]);
                    /* opening edges: branch */
                    for (int br = 0; br < (1 << nopen); br++) {
                        int bits = bits_close; size_t o2 = o2base;
                        for (int t = 0; t < nopen; t++) {
                            int x = (br >> t) & 1;
                            bits |= x << qpos_open[t];
                            if (x) o2 |= (size_t)1 << opens[t];
                        }
                        /* tall legs */
                        if (c1) {
                            for (int i = 0; i < h; i++) {
                                if ((m1 >> i) & 1) continue;
                                int s1 = __builtin_popcount(m1 >> (i + 1)) & 1;
                                int nm1 = m1 | (1 << i);
                                if (c2) {
                                    for (int j = 0; j < h; j++) {
                                        if ((m2 >> j) & 1) continue;
                                        int s2 = __builtin_popcount(m2 >> (j + 1)) & 1;
                                        int nm2 = m2 | (1 << j);
                                        u64 tv = (u64)T[(((i * nj) + j) << dd) | bits];
                                        if (!tv) continue;
                                        u64 term = mulmod(val, tv, p);
                                        if (sgn ^ s1 ^ s2) term = term ? p - term : 0;
                                        size_t idx = ((size_t)nm1 * NM + nm2) * NO + o2;
                                        nxt[idx] += term; if (nxt[idx] >= p) nxt[idx] -= p;
                                    }
                                } else {
                                    u64 tv = (u64)T[((i * nj) << dd) | bits];
                                    if (!tv) continue;
                                    u64 term = mulmod(val, tv, p);
                                    if (sgn ^ s1) term = term ? p - term : 0;
                                    size_t idx = ((size_t)nm1 * NM + m2) * NO + o2;
                                    nxt[idx] += term; if (nxt[idx] >= p) nxt[idx] -= p;
                                }
                            }
                        } else if (c2) {
                            for (int j = 0; j < h; j++) {
                                if ((m2 >> j) & 1) continue;
                                int s2 = __builtin_popcount(m2 >> (j + 1)) & 1;
                                int nm2 = m2 | (1 << j);
                                u64 tv = (u64)T[(j << dd) | bits];
                                if (!tv) continue;
                                u64 term = mulmod(val, tv, p);
                                if (sgn ^ s2) term = term ? p - term : 0;
                                size_t idx = ((size_t)m1 * NM + nm2) * NO + o2;
                                nxt[idx] += term; if (nxt[idx] >= p) nxt[idx] -= p;
                            }
                        } else {
                            u64 tv = (u64)T[bits];
                            if (!tv) continue;
                            u64 term = mulmod(val, tv, p);
                            if (sgn) term = term ? p - term : 0;
                            size_t idx = base + o2;
                            nxt[idx] += term; if (nxt[idx] >= p) nxt[idx] -= p;
                        }
                    }
                }
            }
        }
        u64 *t = cur; cur = nxt; nxt = t;
        p1 = np1; q1 = nq1;
    }
    u64 res = cur[(((size_t)(NM - 1)) * NM + (NM - 1)) * NO + 0];
    free(cur); free(nxt); free(masks); free(openmask_at);
    return (i64)res;
}
