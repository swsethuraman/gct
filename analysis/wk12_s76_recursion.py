#!/usr/bin/env python3
"""s76 -- the S5 one-block recursion, memoised over the shape DAG below lambda_24.

At node (nu, d):

    W_d(nu) = (S^nu)^{K_d} = (+)_{xi} M_{d-1}(xi) (x) c^{nu/xi}        dim B_d(nu)
    M_d(nu) = W_d(nu) ^ Fix(tau),  tau the block swap, an involution on
    (S^nu)^{K'} = (+)_{(xi,eta)} M_{d-2}(eta) (x) u_xi                  dim C_d(nu)

A vector of W_d(nu) is a coefficient vector c over the stored bases of the
M_{d-1}(xi) (rows of E_{d-1}(xi), themselves coordinates over the M_{d-2}(eta));
tau - I acts block-diagonally over eta through the recoupling matrices
R^{nu/eta} (analysis/wk12_s76_seminormal.py).  M_d(nu) is the kernel of that
system, stored in reduced row echelon form as E_d(nu), an a_d(nu) x B_d(nu)
matrix over F_p.  Only the nonzero rows of rref(R - I) are used, so the
system has sum_eta q_eta a_{d-2}(eta) rows, q_eta = m_eta - dim Fix(R).

Everything is mod p (p = 2147483647 by default; both house primes exceed
|lambda_24| = 96, which is what makes the seminormal form and Maschke apply).

Usage: python3 analysis/wk12_s76_recursion.py [--top 24] [--prime P] [--upto D]
       [--out results/s76_dag] [--check-amb 8]
"""
import argparse
import json
import os
import sys
import time
from collections import Counter, defaultdict
from fractions import Fraction

import numpy as np
import flint

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
ROOT = os.path.normpath(os.path.join(HERE, ".."))
from wk11_int_bdelta import lam_of, horiz_strips                   # noqa: E402
from wk12_s76_seminormal import recoupling_modp, intermediate_shapes, skew_cells   # noqa: E402

P1, P2 = 2147483647, 2147483629


def build_dag(top):
    """levels[d] = sorted shapes reachable from `top` by removing horizontal
    4-strips, d = |shape|/4."""
    seen = {tuple(top)}
    stack = [tuple(top)]
    while stack:
        nu = stack.pop()
        for xi in horiz_strips(nu, 4):
            if xi not in seen:
                seen.add(xi)
                stack.append(xi)
    levels = defaultdict(list)
    for nu in seen:
        levels[sum(nu) // 4].append(nu)
    for d in levels:
        levels[d].sort(reverse=True)
    return dict(levels)


def frac_mod(x, p):
    return (x.numerator % p) * pow(x.denominator % p, -1, p) % p


def rref_rows(M, p):
    """nonzero rows of the reduced row echelon form of the integer matrix M mod p."""
    A = flint.nmod_mat(M.tolist(), p)
    R, rank = A.rref()
    rows = [[int(R[i, j]) for j in range(R.ncols())] for i in range(rank)]
    return rows


class Recursion:
    def __init__(self, top, p, out, log):
        self.top = tuple(top)
        self.p = p
        self.out = out
        self.log = log
        self.levels = build_dag(self.top)
        self.a = defaultdict(dict)        # a[d][nu]
        self.E = {}                        # E[nu] for the current level only
        self.stats = {}
        self._rcache = {}
        os.makedirs(out, exist_ok=True)

    # ---- recoupling, reduced to the rows of rref(R - I) mod p, cached by
    #      the normalised skew diagram (the per-pair data is only the xi order)
    def reduced_recoupling(self, nu, eta):
        cells = skew_cells(nu, eta)
        r0 = min(r for r, _ in cells)
        c0 = min(c for _, c in cells)
        D = frozenset((r - r0, c - c0) for r, c in cells)
        if D not in self._rcache:
            subsets, R = recoupling_modp(D, self.p)
            m = len(subsets)
            RmI = np.array([[(R[i][j] - (1 if i == j else 0)) % self.p
                             for j in range(m)] for i in range(m)], dtype=np.int64)
            Q = rref_rows(RmI, self.p)
            self._rcache[D] = (subsets, Q, m)
        subsets, Q, m = self._rcache[D]
        pos = {S: k for k, S in enumerate(subsets)}
        xis = intermediate_shapes(nu, eta)
        order = [pos[frozenset((r - r0, c - c0) for r, c in skew_cells(xi, eta))]
                 for xi in xis]
        assert order == list(range(m)), (nu, eta, order)
        return xis, Q, m

    def node(self, nu, d, Eprev, aprev, aprev2):
        """E_d(nu) from the level-(d-1) matrices Eprev and dims aprev, aprev2."""
        p = self.p
        preds = horiz_strips(nu, 4)
        col0 = {}
        B = 0
        for xi in preds:
            col0[xi] = B
            B += aprev.get(xi, 0)
        if B == 0:
            return None, 0, 0, 0, 0
        # column layout of each E_{d-1}(xi): blocks over horiz_strips(xi, 4)
        sub = {}
        etas = set()
        for xi in preds:
            if aprev.get(xi, 0) == 0:
                continue
            off = 0
            blocks = {}
            for eta in horiz_strips(xi, 4):
                w = aprev2.get(eta, 0)
                if w:
                    blocks[eta] = (off, off + w)
                    etas.add(eta)
                off += w
            sub[xi] = blocks
        etas = sorted(etas, reverse=True)
        # count rows
        rowblocks = []
        C_full = 0
        nrows = 0
        for eta in etas:
            xis, Q, m = self.reduced_recoupling(nu, eta)
            a_eta = aprev2[eta]
            C_full += m * a_eta
            for q in Q:
                rowblocks.append((eta, q, nrows))
                nrows += a_eta
        if nrows == 0:
            # tau - I vanishes on the whole precursor: M = W
            E = np.zeros((B, B), dtype=np.uint32)
            E[np.arange(B), np.arange(B)] = 1
            return E, B, B, 0, C_full
        A = np.zeros((nrows, B), dtype=np.int64)
        for eta, q, r0 in rowblocks:
            xis, Q, m = self.reduced_recoupling(nu, eta)
            a_eta = aprev2[eta]
            for t, xi in enumerate(xis):
                coef = q[t]
                if coef == 0 or aprev.get(xi, 0) == 0:
                    continue
                blk = sub[xi].get(eta)
                if blk is None:
                    continue
                Exi = Eprev[xi]                       # a_xi x B_xi, uint32
                piece = Exi[:, blk[0]:blk[1]].astype(np.int64).T   # a_eta x a_xi
                c0 = col0[xi]
                A[r0:r0 + a_eta, c0:c0 + piece.shape[1]] = (
                    A[r0:r0 + a_eta, c0:c0 + piece.shape[1]] + (piece * coef) % p) % p
        M = flint.nmod_mat(nrows, B, A.reshape(-1).tolist(), p)
        X, nul = M.nullspace()
        if nul == 0:
            return None, 0, B, nrows, C_full
        K = np.array([[int(X[i, j]) for j in range(nul)] for i in range(B)],
                     dtype=np.int64).T                 # nul x B
        Kf = flint.nmod_mat(K.tolist(), p)
        Rf, rank = Kf.rref()
        assert rank == nul
        E = np.array([[int(Rf[i, j]) for j in range(B)] for i in range(nul)],
                     dtype=np.uint32)
        return E, nul, B, nrows, C_full

    def run(self, upto, refs, save_levels=True):
        p = self.p
        # level 0: the empty shape, a_0 = 1 (no coordinates)
        self.a[0][()] = 1
        Eprev = {}
        aprev2 = {}
        aprev = {(): 1}
        for d in range(1, upto + 1):
            t0 = time.time()
            shapes = self.levels.get(d, [])
            Ecur = {}
            acur = {}
            n_nonzero = 0
            sumaB = 0
            maxB = maxrows = maxC = 0
            worst = None
            mism = []
            for nu in shapes:
                if d == 1:
                    # (S^nu)^{S_4} is one-dimensional for nu = (4) and zero otherwise
                    if nu == (4,):
                        E, a, B, rows, C = np.ones((1, 1), dtype=np.uint32), 1, 1, 0, 0
                    else:
                        E, a, B, rows, C = None, 0, 1, 0, 0
                else:
                    E, a, B, rows, C = self.node(nu, d, Eprev, aprev, aprev2)
                acur[nu] = a
                if a:
                    Ecur[nu] = E
                    n_nonzero += 1
                    sumaB += a * B
                maxB = max(maxB, B)
                maxrows = max(maxrows, rows)
                if C > maxC:
                    maxC = C
                    worst = (nu, a, B, rows, C)
                ref = refs.get((nu, d))
                if ref is not None and ref != a:
                    mism.append((nu, d, a, ref))
            self.a[d] = acur
            el = time.time() - t0
            nchecked = sum(1 for nu in shapes if (nu, d) in refs)
            self.stats[d] = dict(delta=d, shapes=len(shapes), nonzero=n_nonzero,
                                 sum_a=sum(acur.values()), sum_aB=sumaB, max_B=maxB,
                                 max_rows=maxrows, max_C=maxC, worst=worst,
                                 checked=nchecked, mismatches=mism, secs=round(el, 1))
            msg = (f"delta={d:2d}: {len(shapes):4d} shapes, {n_nonzero:4d} nonzero, "
                   f"sum a={sum(acur.values()):7d}, sum aB={sumaB:10d}, max B={maxB:5d}, "
                   f"max rows={maxrows:6d}, max C={maxC:6d}, checked {nchecked}, "
                   f"mismatches {len(mism)}  [{el:.1f}s]")
            print(msg, flush=True)
            self.log.write(msg + "\n")
            self.log.flush()
            if mism:
                for x in mism[:20]:
                    print("   MISMATCH", x, flush=True)
                    self.log.write(f"   MISMATCH {x}\n")
                self.dump_dims()
                raise SystemExit(f"dimension mismatch at delta={d}: stopping rule")
            if save_levels:
                np.savez_compressed(os.path.join(self.out, f"level_{d:02d}_p{p}.npz"),
                                    **{str(nu): E for nu, E in Ecur.items()})
            self.dump_dims()
            aprev2 = aprev
            aprev = acur
            Eprev = Ecur
        self.E = Eprev
        return Eprev

    def dump_dims(self):
        json.dump({"top": list(self.top), "prime": self.p,
                   "a": {str(d): {str(nu): a for nu, a in self.a[d].items()}
                         for d in sorted(self.a)},
                   "stats": {str(d): s for d, s in self.stats.items()}},
                  open(os.path.join(self.out, f"dims_p{self.p}.json"), "w"), indent=1)


def load_refs(root, top_delta):
    """independent a-values to check the recursion against."""
    refs = {}
    src = Counter()
    # the LMR ladder (s57 / s63, banked in wk11_int_bdelta and lmr_cell)
    ladder = {12: 2, 13: 39, 14: 93, 15: 145, 16: 188, 17: 219, 18: 241, 19: 255,
              20: 264, 21: 269, 22: 272, 23: 273, 24: 274, 25: 274}
    for d, a in ladder.items():
        if d <= top_delta:
            refs[(tuple(lam_of(d)), d)] = a
            src["ladder"] += 1
    try:
        for row in json.load(open(os.path.join(root, "results", "wk11_int_bdelta.json"))):
            d = row["delta"]
            refs[(tuple(row["lam"]), d)] = row["a"]
            for mu, v in row["parts"]:
                refs[(tuple(mu), d - 1)] = v
                src["bdelta"] += 1
    except FileNotFoundError:
        pass
    try:
        b24 = json.load(open(os.path.join(root, "results", "wk11_int_b24.json")))
        for pr in b24["predecessors"]:
            refs[(tuple(pr["mu"]), 23)] = pr["a_23"]
            src["b24"] += 1
    except FileNotFoundError:
        pass
    try:
        c12 = json.load(open(os.path.join(root, "results", "wk11_int_c12.json")))
        for k, v in c12["a_10_by_shape"].items():
            refs[(tuple(eval(k)), 10)] = v
            src["c12"] += 1
    except FileNotFoundError:
        pass
    # this session's C_24 channels
    import glob
    for f in glob.glob(os.path.join(root, "results", "s76_c24", "shape_*.json")):
        r = json.load(open(f))
        refs[(tuple(r["nu"]), 22)] = r["a22"]
        src["c24"] += 1
    return refs, src


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--top", type=int, default=24)
    ap.add_argument("--prime", type=int, default=P1)
    ap.add_argument("--upto", type=int, default=None)
    ap.add_argument("--out", default=None)
    ap.add_argument("--check-amb", type=int, default=8,
                    help="check every node at delta <= this against the "
                         "symmetric-function plethysm (wk8_s30_pleth.amb)")
    ap.add_argument("--no-save", action="store_true")
    args = ap.parse_args()
    top = tuple(lam_of(args.top))
    upto = args.upto or args.top
    out = args.out or os.path.join(ROOT, "results", "s76_dag")
    os.makedirs(os.path.join(ROOT, "results", "logs"), exist_ok=True)
    log = open(os.path.join(ROOT, "results", "logs", f"s76_recursion_top{args.top}_p{args.prime}.log"), "a")
    refs, src = load_refs(ROOT, args.top)
    if args.check_amb:
        # the symmetric-function plethysm for delta <= check_amb, computed once
        # and cached on disk (its character cache is memory-hungry)
        cache = os.path.join(ROOT, "results", "s76_amb_refs.json")
        if os.path.exists(cache):
            amb_refs = json.load(open(cache))
        else:
            amb_refs = {}
        t = time.time()
        for d in range(1, min(args.check_amb, upto) + 1):
            if str(d) not in amb_refs:
                from wk8_s30_pleth import amb
                A = amb(d, 4, 9)
                amb_refs[str(d)] = {str(list(lam)): v for lam, v in A.items()}
                json.dump(amb_refs, open(cache, "w"))
            for k, v in amb_refs[str(d)].items():
                refs[(tuple(eval(k)), d)] = v
            src[f"amb{d}"] = len(amb_refs[str(d)])
        print(f"amb references for delta <= {min(args.check_amb, upto)} in {time.time() - t:.0f}s")
    print("reference sources:", dict(src), flush=True)
    rec = Recursion(top, args.prime, out, log)
    # zero references: every DAG node at delta <= check_amb absent from amb has a = 0
    if args.check_amb:
        for d in range(1, min(args.check_amb, upto) + 1):
            for nu in rec.levels.get(d, []):
                refs.setdefault((nu, d), 0)
    print(f"DAG: {sum(len(v) for v in rec.levels.values())} nodes; per level",
          {d: len(rec.levels[d]) for d in sorted(rec.levels)}, flush=True)
    t = time.time()
    rec.run(upto, refs, save_levels=not args.no_save)
    print(f"total {time.time() - t:.0f}s")
    if upto == args.top:
        a_top = rec.a[args.top].get(top, 0)
        print(f"a_{args.top}(top) = {a_top}")


if __name__ == "__main__":
    main()
