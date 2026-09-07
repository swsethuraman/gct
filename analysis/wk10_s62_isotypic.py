"""Session 62 — P3/P3': the highest-weight vectors carried to H^{S_lambda} lie in the
lambda-isotypic component (n = 4, delta = 2, 3, where the full Hecke projectors of
session 56 can be rebuilt on |H| x |H|).

    python3 analysis/wk10_s62_isotypic.py <delta>

For every constituent lambda:
  P3  : P_lambda v = v for every v in M_lambda (embedded in H as v[pi] = v_{orbit(pi)}),
        and P_nu v = 0 for every other constituent nu;
  P3' : for every orbital d the Rayleigh quotient  (v^T A_d v)/(v^T v)  equals the
        eigenvalue theta_lambda(d) = |H| dsize_d coef_lambda[d] / (a f) of A_d on the
        lambda-component (a = 1 at delta <= 3, so the block is a scalar).
Writes results/s62_isotypic_d<delta>.json.
"""
import itertools
import json
import os
import sys
import time
from fractions import Fraction
from math import factorial

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.join(ROOT, "tools", "verify"))
import wk10_s62_gram as G                 # noqa: E402
import wk9_s56_core as C56                # noqa: E402
from pleth import ambient_multiplicity    # noqa: E402

n = 4
delta = int(sys.argv[1])
N = n * delta
lab = G.enum_H(n, delta)
nH = lab.shape[0]
orb = G.Orbitals(n, delta)
G.log(f"delta={delta} |H|={nH} orbitals={orb.n_orb}")

# relation matrix D[pi, pi'] = orbital, on all of H
D = np.zeros((nH, nH), dtype=np.int16)
for i in range(nH):
    D[i] = orb.lookup(orb.codes_of(lab, lab[i]))
std_i = int(np.nonzero((lab == G.standard_labels(n, delta)[None, :]).all(axis=1))[0][0])
dsize = np.bincount(D[std_i].astype(np.int64), minlength=orb.n_orb)
G.log("relation matrix built; dsize", dsize.tolist())

# W = S_4 wr S_delta as permutations of range(N), and one coset rep per orbital
blocks0 = [list(range(n * j, n * j + n)) for j in range(delta)]
perms_n = list(itertools.permutations(range(n)))
W = []
for sigma in itertools.permutations(range(delta)):
    for choice in itertools.product(perms_n, repeat=delta):
        w = [0] * N
        for j in range(delta):
            src, dst = blocks0[j], blocks0[sigma[j]]
            for t in range(n):
                w[src[t]] = dst[choice[j][t]]
        W.append(tuple(w))
assert len(W) == factorial(n) ** delta * factorial(delta)


def coset_rep_from_labels(lab_row):
    """g with g(standard block j) = block j of the decomposition, increasing."""
    g = [0] * N
    for j in range(delta):
        dst = [int(p) for p in np.nonzero(lab_row == j)[0]]
        for t in range(n):
            g[n * j + t] = dst[t]
    return tuple(g)


classes = list(C56.partitions(N))
class_id = {rho: i for i, rho in enumerate(classes)}
hist = np.zeros((orb.n_orb, len(classes)), dtype=object)
t = time.time()
for d in range(orb.n_orb):
    g = coset_rep_from_labels(orb.rep_labels[d])
    for w in W:
        gw = tuple(g[w[i]] for i in range(N))
        hist[d, class_id[C56.cycle_type(gw)]] += 1
G.log(f"coset cycle-type histograms done ({time.time()-t:.1f}s)")

lams = [lam for lam in C56.partitions(N, maxlen=delta) if ambient_multiplicity(lam, delta, n=n) > 0]
d_id = orb.index[G.canonical_matrix(tuple(tuple(n if j == b else 0 for b in range(delta)) for j in range(delta)))]
coef = {}
for lam in lams:
    f = C56.hook_length_f(lam)
    chi = [C56.mn_char(lam, rho) for rho in classes]
    c = []
    for d in range(orb.n_orb):
        s = sum(int(hist[d, k]) * chi[k] for k in range(len(classes)))
        c.append(Fraction(f * s, factorial(N)))
    coef[lam] = c
    a_tr = nH * c[d_id] / f
    assert a_tr == ambient_multiplicity(lam, delta, n=n), (lam, a_tr)

# projectors P_lambda = Pnum / den with den = N!; integer numerators fit int64 (bounds asserted)
den = factorial(N)
Dl = D.astype(np.int64)


def projector_numerators(lam):
    lut = np.array([int(c * den) for c in coef[lam]], dtype=np.int64)
    assert all(abs(int(c * den)) < 2 ** 40 for c in coef[lam])
    return lut[Dl]


out = {"delta": delta, "H": nH, "orbitals": orb.n_orb, "cells": {}}
allpass = True
for lam in lams:
    r = len(lam)
    wo = G.weight_orbits(lab, lam, n, r)
    basis, vecs = G.hwv_basis_Q(n, r, delta, lam)
    a = len(vecs)
    V = G.to_orbit_coords(wo["monos"], vecs) if not os.environ.get("S62_DROP_FACTOR") else [list(v) for v in vecs]
    f = C56.hook_length_f(lam)
    rec = {"lambda": list(lam), "a": a, "f": f, "n_lam": wo["n_lam"], "P3": [], "P3_others_zero": [], "P3prime": []}
    Plam = projector_numerators(lam)
    for v in V:
        vH = np.array([v[int(o)] for o in wo["orbit_id"]], dtype=np.int64)
        assert np.abs(vH).max() < 2 ** 20
        # exact: split the projector into 20-bit limbs (Pn = hi*2^20 + lo, lo in [0, 2^20));
        # |x| < 2^20 and nH < 2^13 keep every partial dot below 2^53
        def exact_dot(Pn, x):
            lo = Pn & ((1 << 20) - 1); hi = Pn >> 20
            return lo.dot(x).astype(object) + hi.dot(x).astype(object) * (1 << 20)
        Pv = exact_dot(Plam, vH)
        ok = bool(np.all(Pv == vH.astype(object) * den))
        rec["P3"].append(ok)
        others = []
        for nu in lams:
            if nu == lam:
                continue
            Pnv = exact_dot(projector_numerators(nu), vH)
            others.append(bool(np.all(Pnv == 0)))
        rec["P3_others_zero"].append(all(others))
        # P3': Rayleigh quotients against the eigenvalues (a = 1 here)
        vv = int(np.dot(vH, vH))
        quotients = []
        for d in range(orb.n_orb):
            Ad = (D == d).astype(np.int64)
            Adv = Ad.dot(vH)                      # < nH * 2^20 < 2^34
            vAv = int(np.dot(vH.astype(object), Adv.astype(object)))
            theta = Fraction(nH * int(dsize[d])) * coef[lam][d] / (a * f)
            quotients.append(Fraction(vAv, vv) == theta)
        rec["P3prime"].append(all(quotients))
        allpass &= ok and all(others) and all(quotients)
    G.log(f"lambda={lam} a={a} f={f} P3 {rec['P3']} others-zero {rec['P3_others_zero']} P3' {rec['P3prime']}")
    out["cells"][str(lam)] = rec
out["all_pass"] = bool(allpass)
os.makedirs(os.path.join(ROOT, "results"), exist_ok=True)
with open(os.path.join(ROOT, "results", f"s62_isotypic_d{delta}.json"), "w") as fh:
    json.dump(out, fh, indent=1)
G.log("ALL PASS" if allpass else "FAILURES PRESENT")
