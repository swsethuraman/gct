#!/usr/bin/env python3
"""s76 -- the OBJECT check the dimension checks cannot make.

For small cells (delta <= 4, dim S^nu up to a few thousand) build M_d(nu) two
ways inside the ambient seminormal module S^nu and compare the subspaces:

  (a) directly: the joint fixed space of generators of S_4 wr S_d in S^nu --
      the s_i inside blocks (i not a multiple of 4) and the adjacent block
      swaps (4k-3 4k+1)(4k-2 4k+2)(4k-1 4k+3)(4k 4k+4), k = 1..d-1;
  (b) by unfolding the recursion's coordinates: a stored basis vector of
      M_d(nu) is sum_xi sum_j c_{xi,j} (unfold(e_{xi,j}) (x) c^{nu/xi}), where
      (v (x) c^{nu/xi}) on tableaux is T_0 u S with coefficient v_{T_0} c_S
      (the strip filling S shifted by |xi|), recursively down to delta = 0.

Equality of the two subspaces (both primes) certifies the coefficients of the
stored E_d(nu) -- the conventions of the strip invariants, the recoupling
matrices and the column layout -- at these cells, not only their ranks.
The recursion is re-run here from scratch for the shapes checked (it is
seconds at delta <= 4), so nothing is read from the saved levels.

Usage: python3 analysis/wk12_s76_objectcheck.py [--maxdelta 4] [--maxdim 4000] [--prime P]
"""
import argparse
import json
import os
import sys
import time

import numpy as np
import flint

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
ROOT = os.path.normpath(os.path.join(HERE, ".."))
from wk11_int_bdelta import horiz_strips                                   # noqa: E402
from wk12_s76_seminormal import (cells_of, skew_cells, standard_fillings,  # noqa: E402
                                 strip_invariant, _s_action)
from wk12_s76_recursion import Recursion, P1                               # noqa: E402


def fmod(x, p):
    return (x.numerator % p) * pow(x.denominator % p, -1, p) % p


def perm_word(perm):
    word = []
    p = list(perm)
    changed = True
    while changed:
        changed = False
        for i in range(len(p) - 1):
            if p[i] > p[i + 1]:
                p[i], p[i + 1] = p[i + 1], p[i]
                word.append(i + 1)
                changed = True
    return word


def s_sparse(D, i, p):
    """s_i on S^D as (diag, off, offc): out = diag*v, out[off[mask]] += offc[mask]*v[mask]."""
    fills = standard_fillings(D)
    n = len(fills)
    dg = np.zeros(n, dtype=np.int64)
    of = np.full(n, -1, dtype=np.int64)
    oc = np.zeros(n, dtype=np.int64)
    for (r, c), v in _s_action(D, i).items():
        if r == c:
            dg[c] = fmod(v, p)
        else:
            of[c] = r
            oc[c] = fmod(v, p)
    return dg, of, oc


def apply_s(sp, M, p):
    """apply s_i (sparse triple) to the columns of the matrix M (n x k)."""
    dg, of, oc = sp
    out = (dg[:, None] * M) % p
    mk = of >= 0
    out[of[mk]] = (out[of[mk]] + oc[mk][:, None] * M[mk]) % p
    return out


def intersect_fixed(K, g_of, p):
    """K: n x k basis (columns) of a subspace; return a basis of the vectors of
    K fixed by the operator g (given as a function on n x k matrices)."""
    n, k = K.shape
    if k == 0:
        return K
    Mx = (g_of(K) - K) % p                       # n x k
    A = flint.nmod_mat(Mx.tolist(), p)
    X, nul = A.nullspace()
    Y = np.array([[int(X[i, j]) for j in range(nul)] for i in range(k)], dtype=np.int64)  # k x nul
    Kn = np.zeros((n, nul), dtype=np.int64)
    for j in range(nul):
        Kn[:, j] = ((K.astype(object) @ Y[:, j].astype(object)) % p).astype(np.int64)
    return Kn


def direct_invariants(nu, d, p):
    """(a): fixed space of S_4 wr S_d generators in S^nu, as rref rows over the
    standard tableaux of nu.  Iterative intersection, sparse generators."""
    D = frozenset((r - 1, c - 1) for r, c in cells_of(nu))
    fills = standard_fillings(D)
    n = len(fills)
    N = 4 * d
    sps = {i: s_sparse(D, i, p) for i in range(1, N)}
    K = np.eye(n, dtype=np.int64)
    for i in range(1, N):
        if i % 4 != 0:
            K = intersect_fixed(K, lambda M, i=i: apply_s(sps[i], M, p), p)
    for k in range(1, d):
        perm = list(range(1, N + 1))
        for t in range(4):
            a, b = 4 * (k - 1) + 1 + t, 4 * k + 1 + t
            perm[a - 1], perm[b - 1] = b, a
        word = perm_word(tuple(perm))

        def swap(M, word=word):
            for i in word:
                M = apply_s(sps[i], M, p)
            return M
        K = intersect_fixed(K, swap, p)
    R, rk = flint.nmod_mat(K.T.tolist(), p).rref()
    assert rk == K.shape[1]
    return fills, np.array([[int(R[i, j]) for j in range(n)] for i in range(rk)], dtype=np.int64)


def unfold(rec, nu, d, p, cache):
    """(b): rows of the recursion's basis of M_d(nu) as vectors over the
    standard tableaux of nu (in the order of standard_fillings)."""
    key = (nu, d)
    if key in cache:
        return cache[key]
    D = frozenset((r - 1, c - 1) for r, c in cells_of(nu))
    fills = standard_fillings(D)
    index = {T: k for k, T in enumerate(fills)}
    if d == 0:
        out = np.ones((1, 1), dtype=np.int64)
        cache[key] = (fills, out)
        return cache[key]
    E = rec.E_all[d][nu]                       # a x B
    a = E.shape[0]
    out = np.zeros((a, len(fills)), dtype=np.int64)
    off = 0
    for xi in horiz_strips(nu, 4):
        w = rec.a[d - 1].get(xi, 0)
        if w == 0:
            continue
        fx, U = unfold(rec, xi, d - 1, p, cache)   # w x (#tableaux of xi)
        S = skew_cells(nu, xi)
        r0, c0 = min(r for r, _ in S), min(c for _, c in S)
        cS = strip_invariant(frozenset((r - r0, c - c0) for r, c in S))
        # target index of T_0 u S
        for j in range(w):
            coeffs = E[:, off + j].astype(np.int64)          # a
            for t0, T0 in enumerate(fx):
                v = int(U[j, t0])
                if v == 0:
                    continue
                T0abs = tuple((r, c) for r, c in T0)
                for TS, cs in cS.items():
                    TSabs = tuple((r + r0 - 1, c + c0 - 1) for r, c in TS)
                    k = index[T0abs + TSabs]
                    out[:, k] = (out[:, k] + coeffs * (v * fmod(cs, p) % p)) % p
        off += w
    cache[key] = (fills, out)
    return cache[key]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--maxdelta", type=int, default=4)
    ap.add_argument("--maxdim", type=int, default=4000)
    ap.add_argument("--prime", type=int, default=P1)
    args = ap.parse_args()
    p = args.prime
    # rerun the recursion on the lambda_12 sub-DAG up to maxdelta, keeping every level
    from wk11_int_bdelta import lam_of
    rec = Recursion(tuple(lam_of(12)), p, os.path.join("/tmp", "s76_objcheck"), open(os.devnull, "w"))
    rec.E_all = {}
    orig_run = rec.run

    class Keep:
        pass
    # run level by level, capturing E matrices
    rec.a[0][()] = 1
    Eprev, aprev2, aprev = {}, {}, {(): 1}
    for d in range(1, args.maxdelta + 1):
        Ecur, acur = {}, {}
        for nu in rec.levels.get(d, []):
            if d == 1:
                if nu == (4,):
                    E, a = np.ones((1, 1), dtype=np.uint32), 1
                else:
                    E, a = None, 0
            else:
                E, a, B, rows, C = rec.node(nu, d, Eprev, aprev, aprev2)
            acur[nu] = a
            if a:
                Ecur[nu] = E
        rec.a[d] = acur
        rec.E_all[d] = Ecur
        aprev2, aprev, Eprev = aprev, acur, Ecur
    cache = {}
    results = []
    t0 = time.time()
    for d in range(1, args.maxdelta + 1):
        for nu in sorted(rec.E_all[d], reverse=True):
            D = frozenset((r - 1, c - 1) for r, c in cells_of(nu))
            n = len(standard_fillings(D))
            if n > args.maxdim:
                continue
            t = time.time()
            fills, direct = direct_invariants(nu, d, p)
            fills2, unf = unfold(rec, nu, d, p, cache)
            assert fills == fills2
            a = rec.a[d][nu]
            ok_dim = direct.shape[0] == a == unf.shape[0]
            stacked = flint.nmod_mat(np.vstack([direct, unf]).tolist(), p)
            same_space = (stacked.rank() == a)
            Ru, rk = flint.nmod_mat(unf.tolist(), p).rref()
            entrywise = (rk == a) and all(int(Ru[i, j]) == int(direct[i, j])
                                          for i in range(a) for j in range(n))
            results.append(dict(nu=list(nu), delta=d, dim_S=n, a=a, dims_agree=bool(ok_dim),
                                same_subspace=bool(same_space), rref_entrywise=bool(entrywise),
                                secs=round(time.time() - t, 2)))
            print(results[-1], flush=True)
    out = {"prime": p, "cells": results, "n_cells": len(results),
           "all_same_subspace": all(r["same_subspace"] for r in results),
           "all_rref_entrywise": all(r["rref_entrywise"] for r in results),
           "secs": round(time.time() - t0, 1)}
    json.dump(out, open(os.path.join(ROOT, "results", f"s76_objectcheck_p{p}.json"), "w"), indent=1)
    print(f"{len(results)} cells; all same subspace: {out['all_same_subspace']}; "
          f"rref entrywise: {out['all_rref_entrywise']}; {out['secs']}s")


if __name__ == "__main__":
    main()
