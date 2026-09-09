#!/usr/bin/env python3
"""Gelfand-Tsetlin realization of gl_N irreps, exact rational, for the s75 local
   block-swap recoupling.  Small shapes only (after collapse |rho_c|<=16, N<=4).

GT pattern for top row la (length N): rows la^(N)=la >= la^(N-1) >= ... >= la^(1),
interlacing.  l_{k,i} = la^(k)_i - i.  Chevalley generators (Molev conventions):
  e_k (=E_{k,k+1}) raises row k:  coeff  prod_{j<=k-1}(l_{k-1,j}-l_{k,i}) / prod_{j!=i}(l_{k,j}-l_{k,i})
  f_k (=E_{k+1,k}) lowers row k:  coeff -prod_{j<=k+1}(l_{k+1,j}-l_{k,i}) / prod_{j!=i}(l_{k,j}-l_{k,i})
Weight w_k = (sum row k) - (sum row k-1).  Verified below by dim, weights, and
[e_k,f_k]=h_k.
"""
from fractions import Fraction as Fr
from itertools import product


def gt_patterns(la):
    """all GT patterns with top row la (tuple length N). pattern = tuple of rows,
       row k (1..N) has length k, rows[k-1]."""
    N = len(la)
    rows = [None] * N
    rows[N - 1] = tuple(la)
    res = []
    def rec(k):
        if k == 0:
            res.append(tuple(rows)); return
        above = rows[k]           # row k+1 (length k+1)
        # row k (length k): above[i] >= row[i] >= above[i+1]
        def build(i, cur):
            if i == k:
                rows[k - 1] = tuple(cur); rec(k - 1); return
            lo = above[i + 1]; hi = above[i]
            for v in range(lo, hi + 1):
                build(i + 1, cur + [v])
        build(0, [])
    rec(N - 1)
    return res


def weight(patt):
    N = len(patt)
    s = [sum(patt[k]) for k in range(N)]   # s[k]=sum row k+1
    w = [s[0]] + [s[k] - s[k - 1] for k in range(1, N)]
    return tuple(w)


class GTirrep:
    def __init__(self, la):
        self.la = tuple(la)
        self.N = len(la)
        self.patts = gt_patterns(la)
        self.idx = {p: i for i, p in enumerate(self.patts)}
        self.dim = len(self.patts)
        self.wt = [weight(p) for p in self.patts]

    def _l(self, patt, k):
        # l_{k,i} = la^(k)_i - i  (0-indexed i -> use i+1)
        return [patt[k - 1][i] - (i + 1) for i in range(k)]

    def e(self, patt, k):
        """E_{k,k+1} on pattern; returns dict pattern->coeff (raises row k, 1<=k<=N-1)."""
        out = {}
        lk = self._l(patt, k)
        lkm1 = self._l(patt, k - 1) if k - 1 >= 1 else []
        for i in range(k):
            # raise la^(k)_i by 1 -> must stay interlacing
            new = [list(r) for r in patt]
            new[k - 1][i] += 1
            # check interlacing with rows k-1 and k+1
            if not self._ok(new, k - 1):
                continue
            num = 1
            for j in range(len(lkm1)):
                num *= (lkm1[j] - lk[i])
            den = 1
            for j in range(k):
                if j != i:
                    den *= (lk[j] - lk[i])
            if den == 0:
                continue
            c = Fr(num, den)
            if c != 0:
                key = tuple(tuple(r) for r in new)
                out[key] = out.get(key, Fr(0)) + c
        return out

    def f(self, patt, k):
        """E_{k+1,k} on pattern; lowers row k."""
        out = {}
        lk = self._l(patt, k)
        lkp1 = self._l(patt, k + 1)
        for i in range(k):
            new = [list(r) for r in patt]
            new[k - 1][i] -= 1
            if not self._ok(new, k - 1):
                continue
            num = 1
            for j in range(len(lkp1)):
                num *= (lkp1[j] - lk[i])
            den = 1
            for j in range(k):
                if j != i:
                    den *= (lk[j] - lk[i])
            if den == 0:
                continue
            c = -Fr(num, den)
            if c != 0:
                key = tuple(tuple(r) for r in new)
                out[key] = out.get(key, Fr(0)) + c
        return out

    def _ok(self, rows, krow):
        """check interlacing around modified row index krow (0-indexed row = krow, i.e. row krow+1)."""
        N = self.N
        # row r (1-indexed) length r; interlacing row r+1 >= row r >= shifted
        for r in range(1, N):
            up = rows[r]      # row r+1 length r+1
            dn = rows[r - 1]  # row r   length r
            for i in range(r):
                if not (up[i] >= dn[i] >= up[i + 1]):
                    return False
        return True


def apply_op(irr, op, k, vec):
    """apply gl_N operator (op='e'/'f') index k to a vector (dict idx->coeff)."""
    out = {}
    for i, c in vec.items():
        patt = irr.patts[i]
        d = irr.e(patt, k) if op == 'e' else irr.f(patt, k)
        for p2, c2 in d.items():
            j = irr.idx[p2]
            out[j] = out.get(j, Fr(0)) + c * c2
    return {i: c for i, c in out.items() if c != 0}


if __name__ == "__main__":
    # self-tests
    from collections import defaultdict
    def kostka_weights(irr):
        d = defaultdict(int)
        for w in irr.wt:
            d[tuple(sorted(w, reverse=True))] += 1
        return d
    for la in [(2, 1, 0), (3, 1, 1), (2, 2, 0), (4, 0, 0), (2, 2, 1)]:
        irr = GTirrep(la)
        # dim via Weyl formula
        N = len(la)
        num = 1; den = 1
        for i in range(N):
            for j in range(i + 1, N):
                num *= (la[i] - la[j] + j - i); den *= (j - i)
        wdim = num // den
        ok = irr.dim == wdim
        # Chevalley [e_k,f_k]=h_k on a random basis vector
        chev = True
        for bi in range(irr.dim):
            v = {bi: Fr(1)}
            for k in range(1, N):
                ef = apply_op(irr, 'e', k, apply_op(irr, 'f', k, v))
                fe = apply_op(irr, 'f', k, apply_op(irr, 'e', k, v))
                comm = defaultdict(Fr)
                for i, c in ef.items(): comm[i] += c
                for i, c in fe.items(): comm[i] -= c
                w = irr.wt[bi]
                hk = w[k - 1] - w[k]
                exp = {bi: Fr(hk)} if hk != 0 else {}
                allkeys = set(comm) | set(exp)
                for key in allkeys:
                    if comm.get(key, Fr(0)) != exp.get(key, Fr(0)):
                        chev = False
        print(f"la={la}: dim {irr.dim} (Weyl {wdim}) {'ok' if ok else 'FAIL'}, "
              f"Chevalley {'ok' if chev else 'FAIL'}")
