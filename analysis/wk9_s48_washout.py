#!/usr/bin/env python3
"""
Session 48, target C -- the washout threshold as a function of m.

P_r = R_r requires {per_m(A(s))} to be dense in Sym^m C^r, A(s) an m x m matrix
of linear forms in r variables.  Two ingredients:

 (necessary, free)   dim D_r^{per_m} <= m^2 r - dim(generic orbit of the
                     permanent's symmetry torus) = m^2 r - (2m - 2)  for m >= 3,
                     by Lemma 4 + Prop. 5 of docs/washout_lemma.md, whose
                     argument is m-general.  (m = 2 is exceptional: per_2 is a
                     NONDEGENERATE QUADRATIC FORM in 4 variables, whose
                     stabiliser is O(4) of dimension 6, not the 2m-2 = 2 torus.)

 (sufficient, one    rank d(Phi_{m,r}) = C(r+m-1, m) at ONE point proves
  exact point)       density (Lemma 1: a rank at a point is a LOWER bound on
                     the generic rank -- the right direction here).

d per_m(A(s)) / d (A_k)_{ij} = s_k * per_{m-1}( A(s)^{(i,j)} ), so the Jacobian
row space is S_1 * span{ per of the m^2 minors }, and

    rank dPhi_{m,r} = dim ( S_1 * span{q_ij} )_m ,   q_ij = per A^{(i,j)}.

usage: wk9_s48_washout.py [mmax]
"""
import sys, os, time, random
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from wk9_s44_poly import P1, P2, PRIMES, dim_sym, monos, mono_index, ideal_rows, rank_rows
from math import comb
import numpy as np

MMAX = int(sys.argv[1]) if len(sys.argv) > 1 else 12
BOX = 10 ** 6


# ---------- homogeneous polys as numpy coefficient vectors, graded by degree
class Graded:
    """multiplication tables for Sym^d C^r, d = 0..dmax."""
    def __init__(self, r, dmax, p):
        self.r, self.dmax, self.p = r, dmax, p
        self.mon = [monos(d, r) for d in range(dmax + 2)]
        self.idx = [mono_index(d, r) for d in range(dmax + 2)]
        # shift[d][v][i] = index in degree d+1 of x_v * (i-th monomial of degree d)
        self.shift = []
        for d in range(dmax + 1):
            tab = []
            for v in range(r):
                nxt = self.idx[d + 1]
                tab.append(np.array([nxt[e[:v] + (e[v] + 1,) + e[v+1:]]
                                     for e in self.mon[d]], dtype=np.int64))
            self.shift.append(tab)

    def mul_lin(self, P, d, lin):
        """P (array over degree-d monomials) times the linear form lin (len r)."""
        out = np.zeros(len(self.mon[d + 1]), dtype=np.int64)
        for v in range(self.r):
            c = lin[v] % self.p
            if c:
                out[self.shift[d][v]] = (out[self.shift[d][v]] + (c * P) % self.p) % self.p
        return out


def minor_permanents(A, m, r, G, p):
    """A[k] is the m x m integer matrix of the k-th pencil slot; entry (i,j) of
    A(s) is the linear form ( A[0][i][j], ..., A[r-1][i][j] ).
    Returns q[i][j] = per( A(s) with row i and column j deleted ), a coefficient
    array over degree m-1 monomials."""
    lin = [[[A[k][i][j] for k in range(r)] for j in range(m)] for i in range(m)]
    full = (1 << m) - 1
    q = [[None] * m for _ in range(m)]
    for i0 in range(m):                       # delete row i0
        rows = [i for i in range(m) if i != i0]
        cur = {0: np.array([1], dtype=np.int64)}   # subsets of columns used
        for t, i in enumerate(rows):
            nxt = {}
            for S, P in cur.items():
                for j in range(m):
                    b = 1 << j
                    if S & b:
                        continue
                    term = G.mul_lin(P, t, lin[i][j])
                    S2 = S | b
                    if S2 in nxt:
                        nxt[S2] = (nxt[S2] + term) % p
                    else:
                        nxt[S2] = term
            cur = nxt
        for j in range(m):                    # columns used = all but j
            q[i0][j] = cur[full ^ (1 << j)]
    return q


def jac_rank(m, r, p, rnd):
    G = Graded(r, m, p)
    A = [[[rnd.randrange(1, BOX) for _ in range(m)] for _ in range(m)] for _ in range(r)]
    q = minor_permanents(A, m, r, G, p)
    mons = G.mon[m - 1]
    gens = []
    for i in range(m):
        for j in range(m):
            v = q[i][j]
            gens.append({e: int(c) for e, c in zip(mons, v) if c})
    rows, nc = ideal_rows(gens, m - 1, m, r)
    return rank_rows(rows, nc, p), nc


def orbit_dim(m):
    """dim of the generic orbit of the permanent's symmetry group on r-tuples.
    m >= 3: the torus {(D1,D2): det D1 det D2 = 1} has dim 2m-1, the scalar
    subgroup {(uI, u^{-1}I)} acts trivially, and the stabiliser of a generic
    tuple is trivial (Prop. 5 argument, verbatim in m).  m = 2: per_2 is a
    nondegenerate quadratic form on C^4, stabiliser O(4), dim 6."""
    return 6 if m == 2 else 2 * m - 2


def main():
    print("# s48 target C -- washout threshold.  Jacobian rank of "
          "Phi_{m,r}: (M_m)^r -> Sym^m C^r at a random point, both house primes.")
    print("#   naive  bound: m^2 r            >= C(r+m-1, m)")
    print("#   sharp  bound: m^2 r - orbit(m) >= C(r+m-1, m),  orbit = 2m-2 (m>=3), 6 (m=2)")
    print(f"{'m':>3} {'r':>3} {'m^2 r':>7} {'orbit':>6} {'sharp':>7} {'dimSym':>8} "
          f"{'count?':>7} {'rank p1':>8} {'rank p2':>8} {'dense?':>7} {'codim':>6}  time")
    for m in range(2, MMAX + 1):
        ob = orbit_dim(m)
        rmax = 8 if m == 2 else (7 if m <= 4 else 6)
        for r in range(2, rmax + 1):
            dimS = comb(r + m - 1, m)
            sharp = m * m * r - ob
            counts = sharp >= dimS
            t = time.time()
            rks = []
            for p in PRIMES:
                rnd = random.Random(90000 + 131 * m + r)
                rk, nc = jac_rank(m, r, p, rnd)
                rks.append(rk)
            rk = max(rks)
            dense = (rk == dimS)
            print(f"{m:>3} {r:>3} {m*m*r:>7} {ob:>6} {sharp:>7} {dimS:>8} "
                  f"{str(counts):>7} {rks[0]:>8} {rks[1]:>8} {str(dense):>7} "
                  f"{dimS-rk:>6}  {time.time()-t:.1f}s", flush=True)
            if not dense and r >= 4:
                break   # density fails and cannot return at larger r


if __name__ == "__main__":
    main()
