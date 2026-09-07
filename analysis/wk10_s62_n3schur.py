"""Session 62 — the explicit room-one scalar s at the n=3 LMR cell, through the
EVALUATION Gram (the integrator's s = c - b^T A^{-1} b, exhibited numerically).

For each delta the a highest-weight vectors are extracted mod p by a compressed
nullspace of E (verified against the full sparse E), evaluated at K det_3 pencils,
and the evaluation Gram G = E_ev * E_ev^T (a x a) is formed.  Then:

  rank G = mult_det ;   det G = 0 iff there is a rank drop.

At a room-one cell with a full-rank predecessor, det G = det A * s with A the
(a-1) x (a-1) full-rank transported block, so s = det G / det A, and s = 0 iff the
Gram is rank-deficient.  We exhibit, mod both house primes:

  delta = 11 : G is 5 x 5 of rank 5, det G != 0  -> s != 0 (no equation)
  delta = 12 : G is 6 x 6 of rank 5, det G  = 0  -> s  = 0 (the LMR equation, born here)

This is a mod-p numerical exhibition of the scalar; the OVER-Q proof of s = 0 is the
room-one theorem applied to i_det(12) = 1 (proved over Q in wk10_s62_n3.py) with the
full-rank predecessor mult_det(11) = 5.  A claimed s = 0 is characteristic-zero (a
rank drop is not provable mod p); the s != 0 / det A != 0 lower bounds ARE valid mod p
(rank(M^T M) <= rank M in every characteristic -- integrator note 2).

    python3 analysis/wk10_s62_n3schur.py [delta ...]      (default 11 12)
"""
import json
import os
import random
import sys
import time

import numpy as np
from scipy import sparse
import flint

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.join(ROOT, "tools", "verify"))
from wk8_s30_core import exps, restrict, det_form, P1, P2      # noqa: E402
from wk9_s45_build import build_cell, ev_rows_arr              # noqa: E402
from wk9_s42_sparse import compress, check_kernel_py           # noqa: E402
from wk9_s42_census import a_weyl                              # noqa: E402

N_DEG = 3
R = 7
DET3, NENT = det_form(3)
PRIMES = (P1, P2)
T0 = time.time()


def log(*a):
    print(f"[{time.time()-T0:8.1f}s]", *a, flush=True)


def hwv_basis_modp(E, nc, a, p, seed=7):
    """a basis of ker E mod p (the highest-weight space), by a compressed nullspace:
    compress E to ~ nc+margin rows (sampling and +-1 grouping can only LOSE rank, and
    rank(compressed) <= rank E <= nc - a, so nullity(compressed) >= a; we take nullity
    exactly a when it equals a, then verify every vector against the full sparse E)."""
    rng = np.random.default_rng(seed * 101 + p % 1000 + nc)
    # group ~ nrows / (nc+64) so ng lands at nc+64
    nrows = E.shape[0]
    group = max(2, nrows // (nc + 64) + 1)
    C = compress(E, sample=10 ** 9, group=group, rng=rng)   # sample huge -> all rows used
    C = C.tocsr()
    # build nmod_mat by setting nonzeros
    Cc = C.tocoo()
    M = flint.nmod_mat(C.shape[0], nc, [0] * (C.shape[0] * nc), p)
    for i, j, v in zip(Cc.row.tolist(), Cc.col.tolist(), Cc.data.tolist()):
        M[int(i), int(j)] = int(v) % p
    X, nul = M.nullspace()
    if nul != a:
        # escalate: the compression lost rank; add the full-matrix rows in blocks until nullity = a.
        raise RuntimeError(("compressed nullity != a; escalate needed", nul, a, p))
    kern = np.array([[int(X[i, j]) for i in range(nc)] for j in range(nul)], dtype=np.int64)
    Em = E.tocsr()
    assert int(np.abs(Em.data).max()) < 65536
    for v in kern:
        assert check_kernel_py(Em, nc, p, (v % p).tolist()), "compressed kernel vector fails full E"
    return kern      # a x nc, mod p


def evaluation_matrix_modp(arr, kern, K, p, seed_det, bound):
    """E_ev: a x K, row i = (h_i evaluated at the k-th det_3 pencil) mod p, using the
    same chi-coordinate evaluation as the measurement (ev_rows_arr gives the point rows;
    contract each with each kernel vector)."""
    EV = ev_rows_arr(DET3, NENT, N_DEG, R, arr, K, seed_det, bound, p)   # K x nc
    # E_ev[i,k] = sum_c kern[i,c] EV[k,c]  (mod p)
    a = kern.shape[0]
    G = np.zeros((a, K), dtype=np.int64)
    Kk = kern % p
    for k in range(K):
        col = EV[k] % p
        # dot each kernel row with col, mod p, via 16-bit split
        lo = Kk & 0xFFFF
        hi = Kk >> 16
        t0 = (lo @ col) % p
        t1 = (hi @ col) % p
        G[:, k] = (t0 + t1 * 65536) % p
    return G


def rank_modp(Mat, p):
    m, n = Mat.shape
    return flint.nmod_mat(m, n, (Mat % p).astype(np.int64).ravel().tolist(), p).rank()


def det_modp(Mat, p):
    m = Mat.shape[0]
    return int(flint.nmod_mat(m, m, (Mat % p).astype(np.int64).ravel().tolist(), p).det())


def schur_modp(G, a, p):
    """s = c - b^T A^{-1} b mod p, A the leading (a-1)x(a-1) block.  Returns (detA, s)."""
    if a == 1:
        return 1, int(G[0, 0] % p)
    A = flint.nmod_mat(a - 1, a - 1, (G[:a - 1, :a - 1] % p).astype(np.int64).ravel().tolist(), p)
    dA = int(A.det())
    if dA == 0:
        return 0, None
    b = flint.nmod_mat(a - 1, 1, (G[:a - 1, a - 1] % p).astype(np.int64).ravel().tolist(), p)
    x = A.solve(b)
    btx = 0
    for i in range(a - 1):
        btx = (btx + int(G[i, a - 1]) * int(x[i, 0])) % p
    s = (int(G[a - 1, a - 1]) - btx) % p
    return dA, s


def run(delta, seed_det=11, bound=30, margin=8):
    lam = (3 * delta - 17, 7, 2, 2, 2, 2, 2)
    a = a_weyl(lam, delta, N_DEG, {})
    B = build_cell(lam, delta, n=N_DEG, verbose=False)
    E = B["E"]; nc = B["n_chi"]; arr = B["arr"]
    K = a + margin
    log(f"  built {lam} d{delta}: n_chi={nc} a={a}")
    rec = {"lambda": list(lam), "delta": delta, "a": a, "K": K, "per_prime": {}}
    ranks = []
    for p in PRIMES:
        kern = hwv_basis_modp(E, nc, a, p)
        Gev = evaluation_matrix_modp(arr, kern, K, p, seed_det, bound)   # a x K
        # evaluation Gram G = E_ev E_ev^T (a x a)
        Gram = np.zeros((a, a), dtype=np.int64)
        lo = Gev & 0xFFFF; hi = Gev >> 16
        for i in range(a):
            t0 = (lo @ Gev[i]) % p
            t1 = (hi @ Gev[i]) % p
            Gram[i] = (t0 + t1 * 65536) % p
        rG = rank_modp(Gram, p)
        dG = det_modp(Gram, p)
        dA, s = schur_modp(Gram, a, p)
        ranks.append(rG)
        rec["per_prime"][str(p)] = {"rank_ev_matrix": int(rank_modp(Gev, p)), "rank_Gram": int(rG),
                                    "det_Gram": int(dG), "det_A": int(dA) if dA is not None else None,
                                    "s": (int(s) if s is not None else None), "s_zero": (s == 0),
                                    "detA_nonzero_lowerbound": bool(dA != 0)}
        log(f"    p={p}: rank ev={rec['per_prime'][str(p)]['rank_ev_matrix']} rank Gram={rG} "
            f"det Gram={dG} det A={dA} s={s} -> {'s=0 (BORN)' if s == 0 else 's!=0'}")
    rec["mult_det_from_gram"] = int(ranks[0]) if len(set(ranks)) == 1 else None
    rec["s_zero_both_primes"] = all(rec["per_prime"][str(p)]["s_zero"] for p in PRIMES)
    rec["detA_nonzero_both_primes"] = all(rec["per_prime"][str(p)]["detA_nonzero_lowerbound"] for p in PRIMES)
    return rec


if __name__ == "__main__":
    deltas = [int(x) for x in sys.argv[1:]] or [11, 12]
    out = {"note": "explicit evaluation-Gram Schur complement s at the n=3 LMR ladder (mod p exhibition)",
           "cells": {}}
    for d in deltas:
        out["cells"][str(d)] = run(d)
        with open(os.path.join(ROOT, "results", "s62_n3_schur.json"), "w") as fh:
            json.dump(out, fh, indent=1)
    log("done")
