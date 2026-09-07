"""Session 62 — P5, the n = 2 PROVED rank drop.

det_2 is itself a quadratic form of RANK 4 on the 4 entries of a 2x2 matrix
(x11 x22 - x12 x21, the hyperbolic form).  D_r^{det_2} = closure { det_2(A(s)) :
A a linear map C^r -> C^{2x2} } is the set of pullbacks of that rank-4 form along
linear maps C^r -> C^4, so EVERY quadric in it has symmetric-matrix rank <= 4.

At lambda = (2^delta), r = delta, Sym^delta(Sym^2 C^delta) contains S_{(2^delta)}
with a = 1, and its highest-weight vector is the DISCRIMINANT: the determinant of
the delta x delta symmetric matrix of the quadric.  Hence, PROVED:

    mult_det((2^delta), delta) = 1  for delta <= 4   (rank 4 matrix, disc generically != 0)
                               = 0  for delta >= 5   (rank <= 4 < delta, disc == 0)

so delta = 5 and 6 are theorem-guaranteed rank DROPS (i_det = a = 1) and delta = 3, 4
are theorem-guaranteed FULL rank -- the engine must reproduce both sides of the
boundary at delta = 4/5.  (This is the n = 2 shadow of Theorem P at the peaked tail
(2^{ell-1}); the rank bound is codim of the rank-4 locus, n-independent 4 here.)

Run at delta = 3, 4, 5, 6.  |H_{2,delta}| = (2delta-1)!!.
Prints the block rank and writes results/s62_n2.json.
"""
import json, os, sys, time
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "tools", "verify"))
import numpy as np
import wk10_s62_gram as G
from pleth import ambient_multiplicity

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
n = 2
out = {"n": n, "cells": {}}
for delta in (int(x) for x in (sys.argv[1:] or [5, 6])):
    lam = (2,) * delta
    r = delta
    t = time.time()
    lab = G.enum_H(n, delta)
    orb = G.Orbitals(n, delta, verbose=True)
    a = ambient_multiplicity(lam, delta, n=n)
    wo = G.weight_orbits(lab, lam, n, r)
    Nc, cost = G.pair_counts(lab, wo, orb, verbose=False)
    B = G.B_from_counts(Nc, wo["size"], orb.beta)
    basis, vecs = G.hwv_basis_Q(n, r, delta, lam)
    assert len(vecs) == a
    V = G.to_orbit_coords(wo["monos"], vecs)
    Gm = G.gram_block(V, B)
    rQ = G.rank_Q(Gm)
    rec = {"lambda": list(lam), "a": a, "n_lam": wo["n_lam"], "H": int(lab.shape[0]),
           "orbitals": orb.n_orb, "rank_Q_G": rQ, "i_det": a - rQ, "G": [[str(x) for x in row] for row in Gm],
           "rank_Q_B": G.rank_Q(B), "B_full_rank": G.rank_Q(B) == wo["n_lam"], "secs": round(time.time() - t, 1),
           "expected_rank": (1 if delta <= 4 else 0),
           "expected": ("rank 1 = a (disc of a rank-4 symmetric matrix, delta<=4)" if delta <= 4
                        else "rank 0 < a = 1 (disc of a rank-<=4 matrix in delta>=5 variables vanishes)"),
           "matches_theorem": (rQ == (1 if delta <= 4 else 0))}
    assert rec["matches_theorem"], ("n=2 control disagrees with the theorem", delta, rQ)
    out["cells"][str(lam)] = rec
    G.log(f"delta={delta} lam={lam} |H|={lab.shape[0]} n_lam={wo['n_lam']} a={a} rank_Q G={rQ} "
          f"(expected 0) B full rank={rec['B_full_rank']}")
with open(os.path.join(ROOT, "results", "s62_n2.json"), "w") as fh:
    json.dump(out, fh, indent=1)
