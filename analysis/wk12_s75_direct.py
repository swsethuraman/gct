#!/usr/bin/env python3
"""Direct realization of M_lambda = HWV_lambda(Sym^delta(Sym^4 C^r)) and its
determinant evaluation, in the honest coordinate model -- used as ground-truth
control for the recursion and as the n=4 seed evaluator (r small).

Blocks 1..delta are Sym^4(C^r) monomials; gl_r acts diagonally; the delta blocks
are symmetrized (S_delta) to land in Sym^delta.  A highest-weight vector of weight
lambda that is S_delta-symmetric is an element of M_lambda; dim = a(lambda,delta).

Evaluation at a form f (a quartic given by coefficients f_alpha) sets every block
to f and contracts -- Sym^delta(Sym^4) -> C, F |-> F(f).  A determinant point is
f = det_r-restricted... here f = a genuine quartic in r variables.  i_det = a -
rank over a family of determinant points.
"""
import sys, os
from itertools import product as iproduct
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)


def comps(tot, N):
    if N == 1:
        yield (tot,); return
    for f in range(tot + 1):
        for r in comps(tot - f, N - 1):
            yield (f,) + r


def monos(deg, N):
    return list(comps(deg, N))


class SymDelta:
    """Sym^delta(Sym^4 C^r) highest-weight-lambda space, mod p."""
    def __init__(self, delta, r, p):
        self.delta = delta; self.r = r; self.p = p
        self.mon = monos(4, r)                       # Sym^4 monomials
        self.mpos = {m: i for i, m in enumerate(self.mon)}
        self.M = len(self.mon)

    def hw_space(self, lam):
        """fully-symmetric weight-lambda hw vectors, as list of dicts
           state=sorted-delta-tuple-of-monomial-indices -> coeff."""
        p = self.p; r = self.r
        target = tuple(list(lam) + [0] * (r - len(lam)))
        # enumerate multisets of delta monomials with total weight = target
        # state = sorted tuple of monomial indices (S_delta-symmetric)
        states = []
        def rec(start, chosen, wt):
            if len(chosen) == self.delta:
                if wt == target:
                    states.append(tuple(chosen))
                return
            rem = self.delta - len(chosen)
            for mi in range(start, self.M):
                m = self.mon[mi]
                nw = tuple(wt[k] + m[k] for k in range(r))
                if all(nw[k] <= target[k] for k in range(r)):
                    rec(mi, chosen + [mi], nw)
        rec(0, [], tuple([0] * r))
        spos = {s: i for i, s in enumerate(states)}
        n = len(states)
        if n == 0:
            return [], []
        # raising E_{a,a+1} on a symmetric monomial state: sum over blocks, on that
        # block's Sym^4 monomial.  E_{a,a+1} y^m = m_{a+1} y^{m - e_{a+1} + e_a}.
        Mcols = [dict() for _ in range(n)]
        for si, s in enumerate(states):
            for a in range(r - 1):
                for pos in range(self.delta):
                    m = self.mon[s[pos]]
                    if m[a + 1] > 0:
                        m2 = list(m); m2[a + 1] -= 1; m2[a] += 1; m2 = tuple(m2)
                        s2 = tuple(sorted(s[:pos] + (self.mpos[m2],) + s[pos + 1:]))
                        rk = (a, s2)
                        Mcols[si][rk] = (Mcols[si].get(rk, 0) + m[a + 1]) % p
        allkeys = sorted({rk for col in Mcols for rk in col}, key=lambda x: (x[0], x[1]))
        kpos = {rk: i for i, rk in enumerate(allkeys)}
        Mat = [[0] * n for _ in range(len(allkeys))]
        for si in range(n):
            for rk, c in Mcols[si].items():
                Mat[kpos[rk]][si] = c
        ker = nullspace_modp(Mat, n, p)
        hs = []
        for kv in ker:
            st = {states[i]: kv[i] for i in range(n) if kv[i]}
            hs.append(st)
        return hs, states

    def eval_at(self, hwvec, fcoef):
        """evaluate a hw vector (state->coeff) at a quartic f (dict monomial->coef), mod p.
           F(f) = sum_state coeff * multinomial(state) * prod_blocks f_{mono(block)}."""
        p = self.p
        from math import prod
        total = 0
        for state, c in hwvec.items():
            # symmetric monomial: product of f-coefficients, times the number of
            # ordered tuples giving this multiset (multinomial) -- but since the
            # embedding Sym^delta uses the symmetrised basis, the pairing with f^{⊗δ}
            # is prod f_{m} * (multiset permutations). Use multinomial of the multiset.
            val = c % p
            # multinomial coefficient of the multiset `state`
            from collections import Counter
            cnt = Counter(state)
            mult = 1
            rem = self.delta
            import math
            num = math.factorial(self.delta)
            den = 1
            for v in cnt.values():
                den *= math.factorial(v)
            mult = num // den
            val = (val * mult) % p
            for mi in state:
                val = (val * (fcoef.get(self.mon[mi], 0))) % p
            total = (total + val) % p
        return total % p


def nullspace_modp(M, ncols, p):
    A = [row[:] for row in M]; rows = len(A); piv = 0; pc = []
    for col in range(ncols):
        sel = None
        for rr in range(piv, rows):
            if A[rr][col] % p:
                sel = rr; break
        if sel is None:
            continue
        A[piv], A[sel] = A[sel], A[piv]
        inv = pow(A[piv][col] % p, p - 2, p)
        A[piv] = [(x * inv) % p for x in A[piv]]
        for rr in range(rows):
            if rr != piv and A[rr][col] % p:
                f = A[rr][col] % p
                A[rr] = [(A[rr][t] - f * A[piv][t]) % p for t in range(ncols)]
        pc.append(col); piv += 1
    free = [c for c in range(ncols) if c not in pc]
    out = []
    for fc in free:
        v = [0] * ncols; v[fc] = 1
        for ri, pcol in enumerate(pc):
            v[pcol] = (-A[ri][fc]) % p
        out.append(v)
    return out


if __name__ == "__main__":
    P = 2147483647
    from wk9_s42_census import a_weyl
    for lam, delta, r in [((8, 4, 4), 4, 3), ((8, 4), 3, 2), ((10, 6), 4, 2), ((6, 6), 3, 2)]:
        sd = SymDelta(delta, r, P)
        hs, states = sd.hw_space(lam)
        aw = a_weyl(lam, delta, 4, {})
        print(f"lam={lam} delta={delta} r={r}: dim M={len(hs)} (a_weyl={aw}) "
              f"states={len(states)} {'ok' if len(hs)==aw else 'FAIL'}")
