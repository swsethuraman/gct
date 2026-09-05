#!/usr/bin/env python3
"""
Session 51, section 4b GATE -- the degeneracy-direction pre-check
(docs/brief_wording.md sec 5 / s51 brief sec 4b.3), run BEFORE developing the
rank condition.

The statistic that Psi_f refines is the degree-d Macaulay rank-drop of the
Jacobian ideal of the quartic f:
    drop_d(f) = rho_d - rank M_d(f),   rho_d = dim Sym^d C^r - h_d(4,r).
Evaluate it at the committed test set, all quartics in the SAME r variables:
  (1) det_4 pencil            seed 5107
  (2) reducible l*c, c generic cubic   seed 5108
  (3) the full ten-variable l*per_3    seed 5109   (r = 10, not a restriction)
  (0) generic quartic control seed 5100
Gate (wording sec 5): if the padded permanent (3) is AT LEAST as degenerate as
the determinant (1) -- drop(3) >= drop(1) at equal r -- the statistic separates
in the wrong direction and section 4b stops there.

We use r = 10 (the natural variable count of the full l*per_3) and d = 3*4-5 = 7.
"""
import sys, os, random, time, gc
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from wk9_s44_poly import (dim_sym, h_smooth, rho_generic, monos, mono_index, pderiv,
   rand_pencil, pencil_entries, det_form, per_form, H_GN, linform, pmul, randform, P1, P2)
from flint import nmod_mat
from math import comb

N = 4       # degree of the quartic
R = 10      # variable count (natural for full l*per_3)
D = 7       # 3n-5

def macaulay_drop(F, r, d, p):
    rho = rho_generic(d, N, r)
    idx = mono_index(d, r); mult = monos(d - N + 1, r)
    nc, nr = len(idx), r * len(mult)
    A = nmod_mat(nr, nc, p); i = 0
    for k in range(r):
        g = [(e, c % p) for e, c in pderiv(F, k).items() if c % p]
        for m in mult:
            for e, c in g:
                A[i, idx[tuple(x + y for x, y in zip(e, m))]] = c
            i += 1
    rk = A.rank(); del A; gc.collect()
    return rho - rk, rk, rho

def det4_pencil(r, seed):
    rnd = random.Random(seed); A = rand_pencil(4, r, rnd, 10 ** 5)
    return det_form(pencil_entries(A, 4, r), 4)

def reducible_lc(r, seed):
    """l * c, l linear and c a generic cubic, both in r variables -> quartic."""
    rnd = random.Random(seed)
    l = linform([rnd.randint(-10 ** 5, 10 ** 5) for _ in range(r)], r)
    c = randform(3, r, rnd, 10 ** 5)
    return pmul(l, c)

def padded_per3(seed):
    """the full ten-variable l * per_3(X): X a 3x3 matrix of 9 distinct variables,
    l = the 10th variable.  r = 10 exactly."""
    r = 10; rnd = random.Random(seed)
    # X_{ij} = variable x_{3i+j} (j=0..2), i=0..2 -> vars 0..8; l = var 9
    ent = [[{tuple(1 if t == 3 * i + j else 0 for t in range(r)): 1} for j in range(3)] for i in range(3)]
    per = per_form(ent, 3)
    l = {tuple(1 if t == 9 else 0 for t in range(r)): 1}
    return pmul(l, per)

def generic_quartic(r, seed):
    rnd = random.Random(seed); return randform(4, r, rnd, 10 ** 5)

def main():
    p = P1
    print(f"# S51 sec 4b GATE -- degeneracy-direction pre-check, r={R}, d={D}, prime={p}", flush=True)
    rho = rho_generic(D, N, R); ceil_ = dim_sym(D, R) - H_GN(D, N, R)
    print(f"# rho_{D}(4,{R}) = {rho}   GN ceiling = {ceil_} (binds={ceil_<rho})   C({R},5)={comb(R,5)}", flush=True)
    tests = [
        ("(0) generic quartic  ", generic_quartic(R, 5100)),
        ("(1) det_4 pencil      ", det4_pencil(R, 5107)),
        ("(2) reducible l*c     ", reducible_lc(R, 5108)),
        ("(3) full 10-var l*per3", padded_per3(5109)),
    ]
    res = {}
    for name, F in tests:
        t = time.time(); drop, rk, rho = macaulay_drop(F, R, D, p); dt = time.time() - t
        res[name.strip()] = drop
        print(f"  {name}: drop={drop}  (rank={rk}, rho={rho})   {dt:.0f}s", flush=True)
    d_det = res["(1) det_4 pencil"]; d_per = res["(3) full 10-var l*per3"]
    print(f"\n# GATE: drop(det_4)={d_det}   drop(l*per_3)={d_per}", flush=True)
    if d_per >= d_det:
        print("# GATE FAILED: padded permanent at least as degenerate as the determinant.", flush=True)
        print("# The rank-drop statistic separates in the WRONG direction -> section 4b stops.", flush=True)
    else:
        print("# GATE PASSED: determinant strictly more degenerate than l*per_3.", flush=True)
        print(f"# margin = {d_det - d_per}; the statistic points the right way at r={R}.", flush=True)

if __name__ == "__main__":
    main()
