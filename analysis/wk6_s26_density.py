"""Session 26 -- where the determinantal / permanental r-ary cubics are dense.

The short-weight reduction turns the whole question into:

    is  (A_1,...,A_r) -> f( s_1 A_1 + ... + s_r A_r )   dominant onto Sym^3 C^r ?

If it is, no nonzero polynomial on Sym^3 C^r vanishes on the image, hence no
highest-weight vector of length r lies in the ideal, hence mult = a at every
weight of that length and every degree.

Dominance is decided exactly by the rank of the differential at one point:

    d/d(A_k)_{ij}  f(M)  =  s_k * cof_{ij}(M),      M = sum_k s_k A_k,

with cof the (signed) cofactor for det and the unsigned permanental cofactor
for per.  So the Jacobian rows are the 9r cubics s_k * cof_{ij}(M) and the
columns are the C(r+2,3) coefficients.  Exact integer rank.
"""
import random
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from wk6_s26_core import cubic_exponents
from wk6_s26_hwv import rank_int, BIGP


def _mul(p, q):
    out = {}
    for a, ca in p.items():
        for b, cb in q.items():
            k = tuple(x + y for x, y in zip(a, b))
            out[k] = out.get(k, 0) + ca * cb
    return {k: v for k, v in out.items() if v}


def _add(p, q, sign=1):
    out = dict(p)
    for k, v in q.items():
        out[k] = out.get(k, 0) + sign * v
    return {k: v for k, v in out.items() if v}


def jacobian_rank(r, kind='det', seed=1, spread=7, trials=3):
    """Rank of the differential of (A_1..A_r) -> f(sum s_i A_i) at random
    points.  Returns (best rank, target dimension)."""
    exps = cubic_exponents(r)
    tgt = len(exps)
    best = 0
    for t in range(trials):
        rng = random.Random(seed + 1000 * t)
        As = [[[rng.randint(-spread, spread) for _ in range(3)] for _ in range(3)]
              for _ in range(r)]

        def lin(i, j):
            return {(0,) * k + (1,) + (0,) * (r - 1 - k): As[k][i][j]
                    for k in range(r) if As[k][i][j]}

        M = [[lin(i, j) for j in range(3)] for i in range(3)]
        rows = []
        for k in range(r):
            sk = {(0,) * k + (1,) + (0,) * (r - 1 - k): 1}
            for i in range(3):
                for j in range(3):
                    a, b = [x for x in range(3) if x != i]
                    c, d = [x for x in range(3) if x != j]
                    m1 = _mul(M[a][c], M[b][d])
                    m2 = _mul(M[a][d], M[b][c])
                    if kind == 'det':
                        cof = _add(m1, m2, -1)
                        if (i + j) % 2:
                            cof = {kk: -vv for kk, vv in cof.items()}
                    else:
                        cof = _add(m1, m2, 1)
                    row = _mul(sk, cof)
                    rows.append([row.get(e, 0) for e in exps])
        rk = rank_int(rows, mod=BIGP)
        rkq = rank_int(rows)
        assert rk == rkq, (r, kind, rk, rkq)
        best = max(best, rk)
    return best, tgt


if __name__ == '__main__':
    print("dominance of (A_1..A_r) -> f(sum s_i A_i) onto Sym^3 C^r")
    print("  the effective group {(P,Q) : det P det Q = 1} / scalars has dim 16,")
    print("  so the image dimension is at most min( C(r+2,3), 9r - 16 + slack ).")
    print()
    print("  %-4s %-6s %-8s %-8s %-8s %s" % ("r", "kind", "9r", "rank", "target", "dominant?"))
    for kind in ('det', 'per'):
        for r in range(2, 7):
            rk, tgt = jacobian_rank(r, kind)
            print("  %-4d %-6s %-8d %-8d %-8d %s"
                  % (r, kind, 9 * r, rk, tgt, "YES" if rk == tgt else "no"))


# ---------------------------------------------------------------------------
# General n: where does the crossover sit for det_n / per_n?
# W = Sym^n C^{n^2}; a weight of length r sees only f(s_1 A_1 + ... + s_r A_r),
# an r-ary form of degree n.  Effective group dimension: 2n^2 - 2 for det,
# 2n - 2 for per.  Target dimension C(r+n-1, n).
# ---------------------------------------------------------------------------
from math import comb


def _dict_det(rows, cols, M, kind):
    """det / per of the submatrix M[rows][cols], entries being poly dicts."""
    k = len(rows)
    if k == 0:
        return {(): 1} if False else {tuple(): 1}
    if k == 1:
        return dict(M[rows[0]][cols[0]])
    tot = {}
    for j in range(k):
        sub = _dict_det(rows[1:], cols[:j] + cols[j + 1:], M, kind)
        if not sub or not M[rows[0]][cols[j]]:
            continue
        t = _mul(M[rows[0]][cols[j]], sub)
        sgn = 1 if (kind == 'per' or j % 2 == 0) else -1
        tot = _add(tot, t, sgn)
    return tot


def jacobian_rank_n(n, r, kind='det', seed=5, spread=5):
    exps = []
    from itertools import combinations_with_replacement as cwr
    for c in cwr(range(r), n):
        a = [0] * r
        for i in c:
            a[i] += 1
        exps.append(tuple(a))
    exps = sorted(set(exps), reverse=True)
    rng = random.Random(seed)
    As = [[[rng.randint(-spread, spread) for _ in range(n)] for _ in range(n)]
          for _ in range(r)]

    def lin(i, j):
        return {(0,) * k + (1,) + (0,) * (r - 1 - k): As[k][i][j]
                for k in range(r) if As[k][i][j]}

    M = [[lin(i, j) for j in range(n)] for i in range(n)]
    rows = []
    for k in range(r):
        sk = {(0,) * k + (1,) + (0,) * (r - 1 - k): 1}
        for i in range(n):
            for j in range(n):
                rr = [x for x in range(n) if x != i]
                cc = [x for x in range(n) if x != j]
                cof = _dict_det(rr, cc, M, kind)
                if kind == 'det' and (i + j) % 2:
                    cof = {kk: -vv for kk, vv in cof.items()}
                row = _mul(sk, cof)
                rows.append([row.get(e, 0) for e in exps])
    return rank_int(rows, mod=BIGP), len(exps)


def crossover_table(nmax=5, rmax=7):
    print("\ncrossover length by n:  the largest r with D_r^f = everything")
    print("  %-3s %-6s %-4s %-8s %-8s %-8s %s"
          % ("n", "kind", "r", "n^2 r", "rank", "target", "dense?"))
    for n in range(2, nmax + 1):
        for kind in ('det', 'per'):
            last = None
            for r in range(2, rmax + 1):
                tgt = comb(r + n - 1, n)
                if tgt > 4000:
                    break
                rk, t2 = jacobian_rank_n(n, r, kind)
                dense = (rk == tgt)
                print("  %-3d %-6s %-4d %-8d %-8d %-8d %s"
                      % (n, kind, r, n * n * r, rk, tgt, "YES" if dense else "no"))
                if not dense:
                    break
