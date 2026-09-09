/* Session 74 -- the s69 Grassmann DP evaluator (wk11_s69_dp.c) with COMPACT state
 * storage.  Same recursion, same sign conventions, same interface and result; the
 * only change is the indexing of the state vector.
 *
 * In wk11_s69_dp.c the state lives in an array over ALL (mask1, mask2, open) --
 * 2^h * 2^h * 2^W entries, 16 MB at h = 9, W = 3 -- and the whole array is cleared
 * at every letter, although after processing t letters of which p sit in C1 and q
 * in C2 only masks of popcount exactly p (resp. q) are populated: at most
 * C(h,p) C(h,q) 2^W <= 126 * 126 * 8 = 127 008 entries (1 MB).  The full-array
 * clears and strided writes made the evaluator memory-bandwidth bound, so two
 * concurrent evaluations on this box ran at half speed each (measured 0.128 s
 * alone, 0.244 s each in a pair).  Here masks are ranked within their popcount
 * class and the arrays hold only the populated block.
 *
 * Validated against dp_eval on random (filling, point) pairs by
 * analysis/wk12_s74_dp.py (exact equality mod p).  Arithmetic mod p < 2^31 in 64-bit.
 */
#include <stdint.h>
#include <stdlib.h>
#include <string.h>

typedef unsigned long long u64;
typedef long long i64;

static inline u64 mulmod(u64 a, u64 b, u64 p) { return (a * b) % p; }

i64 dp_eval_compact(int h, int d, int n2, int W, i64 pp,
            const int32_t *inC1, const int32_t *inC2, const int32_t *d2,
            const int32_t *eid, const int32_t *side, int maxd2,
            const i64 *off, const i64 *tens,
            const int32_t *slot, const int32_t *first, const int32_t *firstside)
{
    u64 p = (u64)pp;
    const int NM = 1 << h;
    const size_t NO = (size_t)1 << W;
    /* masks by popcount, and the rank of every mask within its class */
    int *masks = (int *)malloc(sizeof(int) * NM);
    int *rank = (int *)malloc(sizeof(int) * NM);
    int cnt[16]; int start[17];
    { int c = 0;
      for (int pc = 0; pc <= h; pc++) {
          start[pc] = c;
          for (int m = 0; m < NM; m++) if (__builtin_popcount(m) == pc) { rank[m] = c - start[pc]; masks[c++] = m; }
          cnt[pc] = c - start[pc];
      }
      start[h + 1] = c; }
    int maxc = 0; for (int pc = 0; pc <= h; pc++) if (cnt[pc] > maxc) maxc = cnt[pc];
    size_t SZ = (size_t)maxc * maxc * NO;
    u64 *cur = (u64 *)calloc(SZ, sizeof(u64));
    u64 *nxt = (u64 *)calloc(SZ, sizeof(u64));
    if (!cur || !nxt) { free(cur); free(nxt); free(masks); free(rank); return -1; }
    cur[0] = 1;                                   /* (mask 0, mask 0, no open): rank 0, rank 0 */
    int p1 = 0, q1 = 0;
    int *openmask_at = (int *)calloc(d + 1, sizeof(int));
    { int om = 0;
      for (int l = 0; l < d; l++) {
          openmask_at[l] = om;
          for (int q = 0; q < d2[l]; q++) { int e = eid[l * maxd2 + q]; if (first[e] != l) om &= ~(1 << slot[e]); }
          for (int q = 0; q < d2[l]; q++) { int e = eid[l * maxd2 + q]; if (first[e] == l) om |= 1 << slot[e]; }
      }
      openmask_at[d] = om; }
    for (int l = 0; l < d; l++) {
        int c1 = inC1[l], c2 = inC2[l];
        int nj = c2 ? h : 1;
        int dd = d2[l];
        const i64 *T = tens + off[l];
        int om = openmask_at[l];
        int nopen = 0, opens[8], opens_side[8], closes[8], closes_slot[8], closes_fside[8], nclose = 0, qpos_open[8], qpos_close[8];
        for (int q = 0; q < dd; q++) {
            int e = eid[l * maxd2 + q];
            if (first[e] == l) { opens[nopen] = slot[e]; opens_side[nopen] = side[l * maxd2 + q]; qpos_open[nopen] = q; nopen++; }
            else { closes[nclose] = e; closes_slot[nclose] = slot[e]; closes_fside[nclose] = firstside[e]; qpos_close[nclose] = q; nclose++; }
        }
        int np1 = p1 + c1, nq1 = q1 + c2;
        const int cq = cnt[q1], ncq = cnt[nq1];
        memset(nxt, 0, (size_t)cnt[np1] * ncq * NO * sizeof(u64));
        for (int a = 0; a < cnt[p1]; a++) {
            int m1 = masks[start[p1] + a];
            for (int b = 0; b < cq; b++) {
                int m2 = masks[start[q1] + b];
                size_t base = ((size_t)a * cq + b) * NO;
                for (size_t o = 0; o < NO; o++) {
                    if ((int)(o & ~(size_t)om) != 0) continue;
                    u64 val = cur[base + o];
                    if (!val) continue;
                    int bits_close = 0; int sgn = 0;
                    for (int t = 0; t < nclose; t++) {
                        int x = (int)((o >> closes_slot[t]) & 1);
                        int myidx = 1 - x;
                        bits_close |= myidx << qpos_close[t];
                        int row1bit = (closes_fside[t] == 0) ? x : myidx;
                        sgn ^= row1bit;
                    }
                    size_t o2base = o;
                    for (int t = 0; t < nclose; t++) o2base &= ~((size_t)1 << closes_slot[t]);
                    for (int br = 0; br < (1 << nopen); br++) {
                        int bits = bits_close; size_t o2 = o2base;
                        for (int t = 0; t < nopen; t++) {
                            int x = (br >> t) & 1;
                            bits |= x << qpos_open[t];
                            if (x) o2 |= (size_t)1 << opens[t];
                        }
                        if (c1) {
                            for (int i = 0; i < h; i++) {
                                if ((m1 >> i) & 1) continue;
                                int s1 = __builtin_popcount(m1 >> (i + 1)) & 1;
                                int ra = rank[m1 | (1 << i)];
                                if (c2) {
                                    for (int j = 0; j < h; j++) {
                                        if ((m2 >> j) & 1) continue;
                                        int s2 = __builtin_popcount(m2 >> (j + 1)) & 1;
                                        int rb = rank[m2 | (1 << j)];
                                        u64 tv = (u64)T[(((i * nj) + j) << dd) | bits];
                                        if (!tv) continue;
                                        u64 term = mulmod(val, tv, p);
                                        if (sgn ^ s1 ^ s2) term = term ? p - term : 0;
                                        size_t idx = ((size_t)ra * ncq + rb) * NO + o2;
                                        nxt[idx] += term; if (nxt[idx] >= p) nxt[idx] -= p;
                                    }
                                } else {
                                    u64 tv = (u64)T[((i * nj) << dd) | bits];
                                    if (!tv) continue;
                                    u64 term = mulmod(val, tv, p);
                                    if (sgn ^ s1) term = term ? p - term : 0;
                                    size_t idx = ((size_t)ra * ncq + b) * NO + o2;
                                    nxt[idx] += term; if (nxt[idx] >= p) nxt[idx] -= p;
                                }
                            }
                        } else if (c2) {
                            for (int j = 0; j < h; j++) {
                                if ((m2 >> j) & 1) continue;
                                int s2 = __builtin_popcount(m2 >> (j + 1)) & 1;
                                int rb = rank[m2 | (1 << j)];
                                u64 tv = (u64)T[(j << dd) | bits];
                                if (!tv) continue;
                                u64 term = mulmod(val, tv, p);
                                if (sgn ^ s2) term = term ? p - term : 0;
                                size_t idx = ((size_t)a * ncq + rb) * NO + o2;
                                nxt[idx] += term; if (nxt[idx] >= p) nxt[idx] -= p;
                            }
                        } else {
                            u64 tv = (u64)T[bits];
                            if (!tv) continue;
                            u64 term = mulmod(val, tv, p);
                            if (sgn) term = term ? p - term : 0;
                            size_t idx = ((size_t)a * ncq + b) * NO + o2;
                            nxt[idx] += term; if (nxt[idx] >= p) nxt[idx] -= p;
                        }
                    }
                }
            }
        }
        u64 *t = cur; cur = nxt; nxt = t;
        p1 = np1; q1 = nq1;
    }
    /* (full, full, no open) is rank 0 in the class cnt[h] = 1 */
    u64 res = (p1 == h && q1 == h) ? cur[0] : 0;
    free(cur); free(nxt); free(masks); free(rank); free(openmask_at);
    return (i64)res;
}
