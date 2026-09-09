#!/usr/bin/env python3
"""s76 -- the invariant form on the recursion's coordinates, and the spherical
operator T = P_W tau |_W with its spectral identity.

The seminormal basis is orthogonal for the S_n-invariant form, with

    <e_T, e_T> = gamma_T = prod_{i<j, j strictly above i} (d-1)/(d+1),
    d = c(j) - c(i),

(verified: the 2x2 ratio rule gamma_{s_i T}/gamma_T = (1+rho)/(1-rho) holds on
every transposition pair of assorted partition and skew diagrams).  Because
every entry of a tableau's eta-part is smaller than every entry of a skew
filling on top of it, gamma factorises along the branching chain:
gamma_{T_0 u S} = gamma_{T_0} . w_eta(S) . gamma_S, where w_eta(S) collects the
pairs (x in eta below a strip cell).  Hence the form on
W_d(nu) = (+)_xi M_{d-1}(xi) (x) c^{nu/xi} is block diagonal with blocks
G_{d-1}(xi) . N(nu/xi; xi), N = ||c^{nu/xi}||^2 in the form restricted from
S^nu, and the Gram matrix of the stored basis of M_d(nu) is

    G_d(nu) = E_d(nu) . blockdiag_xi( G_{d-1}(xi) N(nu/xi; xi) ) . E_d(nu)^T.

On (S^nu)^{K'} the (xi, eta) block has Gram G_{d-2}(eta) . N(xi/eta; eta) N(nu/xi; xi).

The spherical operator on W (S3's "actual spherical operator"):
T = G_W^{-1} J^T G' tau J, and the identity I + (d-1) T = d P_H|_W gives
(T - I)((d-1) T + I) = 0, spectrum 1 (mult a_d) and -1/(d-1) (mult B_d - a_d),
ker(T - I) = M_d(nu).  This script computes the Gram recursion over the DAG
from the saved levels and checks the identity at chosen nodes.
"""
import argparse
import ast
import json
import os
import sys
import time
from fractions import Fraction

import numpy as np
import flint

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
ROOT = os.path.normpath(os.path.join(HERE, ".."))
from wk11_int_bdelta import lam_of, horiz_strips                              # noqa: E402
from wk12_s76_seminormal import (skew_cells, cells_of, strip_invariant,       # noqa: E402
                                 recoupling_modp, intermediate_shapes)
from wk12_s76_recursion import build_dag, P1, P2                              # noqa: E402


def fmod(x, p):
    return (x.numerator % p) * pow(x.denominator % p, -1, p) % p


def strip_norm(nu, xi):
    """||c^{nu/xi}||^2 in the invariant form of S^nu restricted to the
    tableaux whose xi-part is fixed (exact Fraction)."""
    S = skew_cells(nu, xi)
    r0 = min(r for r, _ in S)
    c0 = min(c for _, c in S)
    D = frozenset((r - r0, c - c0) for r, c in S)
    cA = strip_invariant(D)
    below = list(cells_of(xi))
    tot = Fraction(0)
    for T, coef in cA.items():
        cells = [(r + r0, c + c0) for r, c in T]
        g = Fraction(1)
        for a in range(4):
            ra, ca = cells[a]
            for b in range(a + 1, 4):
                rb, cb = cells[b]
                if rb < ra:
                    d = (cb - rb) - (ca - ra)
                    g *= Fraction(d - 1, d + 1)
            cj = ca - ra
            for (rx, cx) in below:
                if rx > ra:
                    d = cj - (cx - rx)
                    g *= Fraction(d - 1, d + 1)
        tot += coef * coef * g
    return tot


class Gram:
    def __init__(self, p, dagdir):
        self.p = p
        self.dagdir = dagdir
        dims = json.load(open(os.path.join(dagdir, f"dims_p{p}.json")))
        self.a = {int(d): {tuple(ast.literal_eval(k)): v for k, v in dd.items()} for d, dd in dims["a"].items()}
        self.G = {0: {(): np.array([[1]], dtype=np.int64)}}
        self._norm = {}

    def norm(self, nu, xi):
        key = (nu, xi)
        if key not in self._norm:
            self._norm[key] = fmod(strip_norm(nu, xi), self.p)
        return self._norm[key]

    def load_level(self, d):
        z = np.load(os.path.join(self.dagdir, f"level_{d:02d}_p{self.p}.npz"))
        return {tuple(ast.literal_eval(k)): z[k] for k in z.files}

    def gram_W(self, nu, d, aprev):
        """block-diagonal Gram of W_d(nu) as a list of (xi, block) in
        horiz_strips order (only xi with a > 0), plus offsets."""
        p = self.p
        blocks = []
        off = 0
        for xi in horiz_strips(nu, 4):
            w = aprev.get(xi, 0)
            if w == 0:
                continue
            Gxi = self.G[d - 1][xi]
            N = self.norm(nu, xi)
            blocks.append((xi, off, (Gxi * N) % p))
            off += w
        return blocks, off

    def level(self, d, E):
        p = self.p
        Gd = {}
        aprev = self.a[d - 1]
        for nu, Enu in E.items():
            blocks, B = self.gram_W(nu, d, aprev)
            assert B == Enu.shape[1], (nu, B, Enu.shape)
            Ei = Enu.astype(np.int64)
            # G = E . blockdiag . E^T  computed block by block with flint
            a = Ei.shape[0]
            acc = flint.nmod_mat(a, a, [0] * (a * a), p)
            for xi, off, blk in blocks:
                w = blk.shape[0]
                Eb = flint.nmod_mat(Ei[:, off:off + w].tolist(), p)
                acc = acc + Eb * flint.nmod_mat(blk.tolist(), p) * Eb.transpose()
            Gd[nu] = np.array([[int(acc[i, j]) for j in range(a)] for i in range(a)], dtype=np.int64)
        self.G[d] = Gd

    def spherical_check(self, nu, d, Eprev, Enu):
        """build T = G_W^{-1} J^T G' tau J on W_d(nu) and test the identities."""
        p = self.p
        aprev, aprev2 = self.a[d - 1], self.a[d - 2]
        preds = [xi for xi in horiz_strips(nu, 4) if aprev.get(xi, 0)]
        col0, B = {}, 0
        for xi in preds:
            col0[xi] = B
            B += aprev[xi]
        # sub-block layout of each E_{d-1}(xi) over eta
        sub = {}
        etas = set()
        for xi in preds:
            off, blocks = 0, {}
            for eta in horiz_strips(xi, 4):
                w = aprev2.get(eta, 0)
                if w:
                    blocks[eta] = (off, off + w)
                    etas.add(eta)
                off += w
            sub[xi] = blocks
        # Y = sum_eta J_eta^T (D_eta R_eta (x) G_{d-2}(eta)) J_eta, block by block:
        # block [xi1, xi2] = ||u_xi1||^2 R[t1, t2] . piece_t1^T G_eta piece_t2
        Ynp = np.zeros((B, B), dtype=np.int64)
        for eta in sorted(etas, reverse=True):
            cells = skew_cells(nu, eta)
            r0, c0 = min(r for r, _ in cells), min(c for _, c in cells)
            D = frozenset((r - r0, c - c0) for r, c in cells)
            subsets, R = recoupling_modp(D, p)
            xis = intermediate_shapes(nu, eta)
            Geta = flint.nmod_mat(self.G[d - 2][eta].tolist(), p)
            pieces, PG = {}, {}
            for t, xi in enumerate(xis):
                if xi in sub and eta in sub[xi]:
                    lo, hi = sub[xi][eta]
                    pc = flint.nmod_mat(Eprev[xi][:, lo:hi].astype(np.int64).T.tolist(), p)  # a_eta x a_xi
                    pieces[t] = pc
                    PG[t] = pc.transpose() * Geta                                           # a_xi x a_eta
            unorm = {t: self.norm(xi, eta) * self.norm(nu, xi) % p for t, xi in enumerate(xis)}
            for t1, xi1 in enumerate(xis):
                if t1 not in pieces:
                    continue
                for t2, xi2 in enumerate(xis):
                    if t2 not in pieces or R[t1][t2] == 0:
                        continue
                    coef = unorm[t1] * R[t1][t2] % p
                    blk = (PG[t1] * pieces[t2]) * flint.nmod(coef, p)
                    c1, c2 = col0[xi1], col0[xi2]
                    n1, n2 = blk.nrows(), blk.ncols()
                    Ynp[c1:c1 + n1, c2:c2 + n2] = (Ynp[c1:c1 + n1, c2:c2 + n2]
                                                   + np.array(blk.tolist(), dtype=np.int64)) % p
        Y = flint.nmod_mat(Ynp.tolist(), p)
        # G_W
        blocks, Bw = self.gram_W(nu, d, aprev)
        GWnp = np.zeros((B, B), dtype=np.int64)
        for xi, off, blk in blocks:
            w = blk.shape[0]
            GWnp[off:off + w, off:off + w] = blk
        GW = flint.nmod_mat(GWnp.tolist(), p)
        sym = (Y == Y.transpose())
        T = GW.inv() * Y
        I = flint.nmod_mat(B, B, [int(i == j) for i in range(B) for j in range(B)], p)
        lhs = (T - I) * (T * flint.nmod(d - 1, p) + I)
        zero = (lhs == flint.nmod_mat(B, B, [0] * (B * B), p))
        rk = (T - I).rank()
        Ef = flint.nmod_mat(Enu.astype(np.int64).tolist(), p)
        fixed = (T * Ef.transpose() == Ef.transpose())
        rk2 = (T * flint.nmod(d - 1, p) + I).rank()
        return dict(nu=list(nu), delta=d, B=B, a=Enu.shape[0], Y_symmetric=bool(sym),
                    identity_zero=bool(zero), rank_T_minus_I=int(rk), rank_dT_plus_I=int(rk2),
                    E_fixed_by_T=bool(fixed))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--prime", type=int, default=P1)
    ap.add_argument("--top", type=int, default=24)
    ap.add_argument("--dag", default=os.path.join(ROOT, "results", "s76_dag"))
    ap.add_argument("--check", default="12,16,20,24", help="levels at which to run the spherical check")
    ap.add_argument("--per-level", type=int, default=3)
    ap.add_argument("--out", default=None)
    args = ap.parse_args()
    p = args.prime
    g = Gram(p, args.dag)
    top = tuple(lam_of(args.top))
    levels = build_dag(top)
    check_levels = {int(x) for x in args.check.split(",") if x}
    import random
    rng = random.Random(76)
    results = {"prime": p, "checks": [], "gram_secs": {}}
    Eprev = None
    t_all = time.time()
    for d in range(1, args.top + 1):
        E = g.load_level(d)
        t = time.time()
        g.level(d, E)
        results["gram_secs"][d] = round(time.time() - t, 1)
        if d in check_levels and d >= 2:
            cand = [nu for nu in levels[d] if nu in E]
            picks = [top] if d == args.top else []
            if tuple(lam_of(d)) in E and d >= 12 and tuple(lam_of(d)) not in picks:
                picks.append(tuple(lam_of(d)))
            rng.shuffle(cand)
            for nu in cand:
                if len(picks) >= args.per_level:
                    break
                if nu not in picks:
                    picks.append(nu)
            for nu in picks:
                t = time.time()
                r = g.spherical_check(nu, d, Eprev, E[nu])
                r["secs"] = round(time.time() - t, 1)
                results["checks"].append(r)
                print(r, flush=True)
        print(f"delta={d:2d}: Gram of {len(E)} nodes in {results['gram_secs'][d]}s", flush=True)
        Eprev = E
    results["total_secs"] = round(time.time() - t_all, 1)
    # bank the top Gram matrix
    Gtop = g.G[args.top][top]
    np.savez_compressed(os.path.join(ROOT, "results", f"s76_gram24_p{p}.npz"), G24=Gtop)
    results["G24_shape"] = list(Gtop.shape)
    results["G24_rank"] = int(flint.nmod_mat(Gtop.tolist(), p).rank())
    out = args.out or os.path.join(ROOT, "results", f"s76_spherical_p{p}.json")
    json.dump(results, open(out, "w"), indent=1)
    print("written", out)


if __name__ == "__main__":
    main()
