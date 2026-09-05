"""
Session 50 validation — the engine on cases with known answers, before the n=4 run.

  V1  det_3 (n=3): LMR theorem => det_3 | det_7(H|_F).  Expect DIVIDES.
  V2  generic cubic in 9 vars: dual is a hypersurface.   Expect NOT_DIVIDES.
  V3  Katz rank audit: rank H_{det_3} at a rank-2 point = 2n = 6;
      generic rank = 9.
  V4  det_4 rank audit: rank H_{det_4} at a rank-3 point = 2n = 8; generic 16.
"""
import random, sys
import wk9_s50_lmr as L

P1 = 2147483647          # 2^31-1
P2 = 2147483629          # another 31-bit prime

def det3_idx():  return [[0,1,2],[3,4,5],[6,7,8]]
def det4_idx():  return [[0,1,2,3],[4,5,6,7],[8,9,10,11],[12,13,14,15]]

def build_det(idx, N):
    return L.normalise(L.det_form(idx), N)

def build_generic(N, deg, nmon, seed, active=None):
    rng = random.Random(seed)
    if active is None: active = list(range(N))
    from collections import defaultdict
    acc = defaultdict(int)
    import itertools
    # random monomials of total degree `deg` in active vars
    combos = list(itertools.combinations_with_replacement(active, deg))
    rng.shuffle(combos)
    for c in combos[:nmon]:
        e=[0]*N
        for v in c: e[v]+=1
        acc[tuple(e)] += rng.randrange(1, 50)
    return [(cc,ee) for ee,cc in acc.items()]

def randmat_rank(n, r, p, rng):
    """Random n x n matrix of rank r as a flat length-n^2 vector (row-major)."""
    import itertools
    M=[[0]*n for _ in range(n)]
    for _ in range(r):
        u=[rng.randrange(1,p) for _ in range(n)]
        v=[rng.randrange(1,p) for _ in range(n)]
        for i in range(n):
            for j in range(n):
                M[i][j]=(M[i][j]+u[i]*v[j])%p
    return [M[i][j] for i in range(n) for j in range(n)]

def randB(N, F, seed):
    rng=random.Random(seed)
    return [[rng.randrange(1,40) for _ in range(F)] for _ in range(N)]

def main():
    print("=== V1/V2  n=3 engine validation (F=7, d=3, edeg=7) ===")
    det3 = build_det(det3_idx(), 9)
    print("det_3 monomials:", len(det3))
    B9 = randB(9, 7, seed=101)
    r = L.test_divisibility(det3, 9, B9, F=7, dform=3, p=P1, nsamples=6, seed=11)
    print("  det_3 divisibility, p1:", r['verdict'], "| any_nonzero_r=", r['any_nonzero_r'], "| gdegs=", sorted({d['gdeg'] for d in r['results']}))
    r2 = L.test_divisibility(det3, 9, B9, F=7, dform=3, p=P2, nsamples=6, seed=11)
    print("  det_3 divisibility, p2:", r2['verdict'])

    gcub = build_generic(9, 3, 40, seed=7)
    rg = L.test_divisibility(gcub, 9, B9, F=7, dform=3, p=P1, nsamples=4, seed=13)
    print("  generic cubic divisibility:", rg['verdict'], "| gdegs=", sorted({d['gdeg'] for d in rg['results']}),
          "| sample r nonzero coeffs:", [len(d['r_coeffs']) for d in rg['results']][:3])

    print("=== V3  Katz rank audit, det_3 (expect on-zero rank 6 = 2n, generic 9) ===")
    rng=random.Random(5)
    pt_rank2 = randmat_rank(3, 2, P1, rng)     # det=0 point
    print("  rank H_det3 at rank-2 matrix:", L.rank_H_at_point(det3, 9, P1, pt_rank2), "(expect 6)")
    print("  rank H_det3 generic:", L.rank_H_generic(det3, 9, P1, seed=3)[0], "(expect 9)")

    print("=== V4  Katz rank audit, det_4 (expect on-zero rank 8 = 2n, generic 16) ===")
    det4 = build_det(det4_idx(), 16)
    print("  det_4 monomials:", len(det4))
    rng=random.Random(6)
    pt_rank3 = randmat_rank(4, 3, P1, rng)     # det=0 point
    print("  rank H_det4 at rank-3 matrix:", L.rank_H_at_point(det4, 16, P1, pt_rank3), "(expect 8)")
    print("  rank H_det4 generic:", L.rank_H_generic(det4, 16, P1, seed=4)[0], "(expect 16)")

if __name__ == "__main__":
    main()
