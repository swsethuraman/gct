#!/usr/bin/env python3
"""
Session 72 -- the INTERIOR of D_5 cap W, as an exact upper bound.

  W_int := Phi(X_5) cap W = { genuine determinants det M(s) that are divisible
           by s_5 }.

  s_5 | det M(s)  <=>  det M(s)|_{s_5=0} = det( s_1 A_1 + ... + s_4 A_4 ) == 0
                  <=>  (A_1,...,A_4) in B_4  (the base locus of Phi_4),
  with A_5 free.  So

     W_int = { det M(s) / s_5 : (A_1..A_4) in B_4, A_5 in M_4 }  subset Sym^3 C^5,

  a finite union of images of irreducible parametrised families (one per
  component of B_4).  dim W_int = max_C (generic Jacobian rank of the cubic map
  over component C of B_4), an EXACT value, hence an exact upper bound on the
  interior part of D_5 cap W with no closure gap.

Under the relabelling s_5 <-> s_1 this is EXACTLY session 32's branch
measurement: M = s_1 A_1 + M_0(y), A_1 the free 4x4 matrix, M_0(y) the singular
4-space, G = det M / s_1 in Sym^3 C^5.  Session 32 measured max = 31 over the
complete branch list (compressions 29,31,31,29; exceptional strata 27,25;
E_1 22), certified over Q and at wide random points.  So dim W_int = 31.

This module (a) re-confirms the max via wk8_s32_branches (imported, not
re-derived), and (b) closes the one gap in "all of B_4": the generic-rank-<=2
4-spaces, which s32 Corollary 3 excluded from the *cubic* question because they
force s_1^2 | det.  Here they are IN B_4 and must be bounded: their image lies
in s_1 . Sym^2 C^5, dimension <= 15 < 31, and this is verified explicitly.
"""
import sys, json, itertools, random
sys.path.insert(0, 'analysis')
import wk8_s32_branches as S32
from wk8_s32_branches import (mask_branch, kernel_branch, skew_pad_branch,
                              measure, lin, det4_dual, div_s1, IDX, NC, rank_mod,
                              PRIME, PRIME2)

P1, P2 = 2147483647, 2147483629

def branch_rank(maker, seeds=(11, 12, 13)):
    best = 0; detail = None
    for s in seeds:
        mats, tang = maker(s)
        rq, rp, rp2, npar = measure(mats, tang, "s72_int", check_Q=False)
        assert rp == rp2, "prime disagreement"
        if rp > best: best = rp; detail = (rp, npar)
    return best

def rank_le2_image(zero_cols, seeds=(21, 22, 23)):
    """A 4-space with the given columns identically zero (rank <= 4-|zero_cols|).
    With two zero columns the space is rank <= 2.  Measure the image of the cubic
    map; expect the determinant divisible by s_1^2 so the 'cubic' det/s_1 is s_1
    times a quadric, image <= dim Sym^2 C^5 = 15."""
    best = 0
    s1sq = True
    for s in seeds:
        rnd = random.Random(s)
        HI = 9
        free = [[q not in zero_cols for q in range(4)] for _ in range(4)]
        A1 = [[rnd.randint(-HI, HI) for _ in range(4)] for _ in range(4)]
        mats = [A1]
        for _ in range(4):
            mats.append([[rnd.randint(-HI, HI) if free[p][q] else 0 for q in range(4)] for p in range(4)])
        M0 = lin(mats)
        Zt = lin([[[0]*4 for _ in range(4)] for _ in range(5)])
        # det and whether s_1^2 | det
        v, _ = det4_dual(M0, Zt)
        min_s1 = min((e[0] for e in v), default=99) if v else 99
        if min_s1 < 2: s1sq = False
        # image of det/s_1
        rows = []
        for i in range(5):
            for p in range(4):
                for q in range(4):
                    if i >= 1 and not free[p][q]: continue
                    T = [[[0]*4 for _ in range(4)] for _ in range(5)]; T[i][p][q] = 1
                    _, d = det4_dual(M0, lin(T))
                    if not d: rows.append([0]*NC); continue
                    dG = {(e[0]-1,)+e[1:]: c for e, c in d.items()}  # divide by s_1 once
                    row = [0]*NC
                    for e, c in dG.items():
                        if e in IDX: row[IDX[e]] += c
                    rows.append(row)
        rp = rank_mod(rows, PRIME2)
        best = max(best, rp)
    return best, s1sq

if __name__ == '__main__':
    print("Session 72 -- interior bound dim W_int (= s32 branch max, reframed)\n")
    rec = {}
    rec['ker']   = branch_rank(lambda s: mask_branch({0,1,2,3}, {3}, s))
    rec['coker'] = branch_rank(lambda s: mask_branch({3}, {0,1,2,3}, s))
    rec['c21']   = branch_rank(lambda s: mask_branch({1,2,3}, {2,3}, s))
    rec['c32']   = branch_rank(lambda s: mask_branch({2,3}, {1,2,3}, s))
    rec['SP (rank L=3)'] = branch_rank(lambda s: kernel_branch(3, s))
    rec['P  (rank L=4)'] = branch_rank(lambda s: kernel_branch(4, s))
    rec['SP^T'] = branch_rank(lambda s: kernel_branch(3, s, transpose=True))
    rec['P^T']  = branch_rank(lambda s: kernel_branch(4, s, transpose=True))
    rec['E_1 skew-pad'] = branch_rank(skew_pad_branch)
    for nm, v in rec.items():
        print(f"  {nm:22s} image dim = {v}")
    mx = max(rec.values())
    print(f"\n  MAX over generic-rank-3 components of B_4:  dim W_int = {mx}")
    # rank <= 2 gap
    r2, s1sq = rank_le2_image({2, 3})
    print(f"\n  generic-rank-<=2 4-space (two zero columns): image dim = {r2}, "
          f"s_1^2 | det : {s1sq}  (<= 15 = dim Sym^2 C^5, well below {mx})")
    out = dict(components=rec, dim_W_int=mx, rank_le2_image=r2, rank_le2_s1squared=s1sq,
               interpretation="exact upper bound on the interior Phi(X_5) cap W")
    json.dump(out, open('results/s72_interior.json', 'w'), indent=1)
    print("\n  wrote results/s72_interior.json")
    print(f"\n  INTERIOR: dim W_int = {mx} < 35  (exact, certified over Q by s32).")
