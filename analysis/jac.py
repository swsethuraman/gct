#!/usr/bin/env python3
"""Independent check of session 26's Jacobian ranks.

Map  phi: (A_1..A_r) in (M_n)^r  ->  f(s_1 A_1 + ... + s_r A_r) in Sym^n C^r,
f = det or per.  d(phi)/d(A_i[p][q]) = s_i * (p,q)-cofactor of M, where
M = sum s_j A_j is an n x n matrix of linear forms in s.  Rank of the
9r x C(r+n-1,n) coefficient matrix = rank of the differential.
"""
import random, itertools
from math import comb

P = (1 << 61) - 1          # Mersenne prime

def pmul(a, b, r):
    out = {}
    for e1, c1 in a.items():
        for e2, c2 in b.items():
            e = tuple(e1[k] + e2[k] for k in range(r))
            out[e] = (out.get(e, 0) + c1 * c2) % P
    return {e: c for e, c in out.items() if c}

def padd(a, b):
    out = dict(a)
    for e, c in b.items():
        out[e] = (out.get(e, 0) + c) % P
    return {e: c for e, c in out.items() if c}

def minor_expand(M, rows, cols, r, signed):
    """det (signed=True) or per (signed=False) of the submatrix, entries are polys."""
    k = len(rows)
    if k == 0:
        return {tuple([0]*r): 1}
    acc = {}
    for idx, j in enumerate(cols):
        sub = minor_expand(M, rows[1:], cols[:idx]+cols[idx+1:], r, signed)
        if not sub: continue
        term = pmul(M[rows[0]][j], sub, r)
        if signed and idx % 2:
            term = {e: (-c) % P for e, c in term.items()}
        acc = padd(acc, term)
    return acc

def jac_rank(n, r, signed, seed=0):
    rnd = random.Random(seed)
    A = [[[rnd.randint(-6, 6) for _ in range(n)] for _ in range(n)] for _ in range(r)]
    # M[p][q] = sum_i s_i A[i][p][q]  as a polynomial in s
    M = [[{} for _ in range(n)] for _ in range(n)]
    for p in range(n):
        for q in range(n):
            d = {}
            for i in range(r):
                v = A[i][p][q] % P
                if v:
                    e = [0]*r; e[i] = 1
                    d[tuple(e)] = v
            M[p][q] = d
    monos = [e for e in itertools.product(range(n+1), repeat=r) if sum(e) == n]
    assert len(monos) == comb(r+n-1, n), (len(monos), comb(r+n-1, n))
    idx = {e: k for k, e in enumerate(monos)}
    rows = []
    allr, allc = list(range(n)), list(range(n))
    for p in range(n):
        for q in range(n):
            cof = minor_expand(M, [x for x in allr if x != p],
                               [x for x in allc if x != q], r, signed)
            if signed and (p + q) % 2:
                cof = {e: (-c) % P for e, c in cof.items()}
            for i in range(r):
                e_i = [0]*r; e_i[i] = 1
                row = [0]*len(monos)
                for e, c in cof.items():
                    ee = tuple(e[k] + e_i[k] for k in range(r))
                    row[idx[ee]] = (row[idx[ee]] + c) % P
                rows.append(row)
    # rank mod P
    rk, ncols = 0, len(monos)
    for col in range(ncols):
        piv = next((i for i in range(rk, len(rows)) if rows[i][col]), None)
        if piv is None: continue
        rows[rk], rows[piv] = rows[piv], rows[rk]
        inv = pow(rows[rk][col], P-2, P)
        rows[rk] = [(x*inv) % P for x in rows[rk]]
        for i in range(len(rows)):
            if i != rk and rows[i][col]:
                f = rows[i][col]
                rows[i] = [(rows[i][c] - f*rows[rk][c]) % P for c in range(ncols)]
        rk += 1
    return rk

if __name__ == "__main__":
    STAB = {2: 6, 3: 16, 4: 30}          # dim Stab(det_n) = 2n^2-2
    PER  = {2: 6, 3: 4,  4: 6}           # dim Stab(per_n) (per_2 ~ det_2)
    print("%3s %3s %6s %8s %8s %8s   %s" % ("n","r","n^2 r","target","det","per","predicted det = n^2 r - dimStab"))
    for n, rs in ((3,(2,3,4,5,6)), (4,(2,3,4)), (2,(3,4,5))):
        for r in rs:
            tgt = comb(r+n-1, n)
            d = max(jac_rank(n,r,True,s) for s in (0,1))
            p = max(jac_rank(n,r,False,s) for s in (0,1))
            pred = min(tgt, n*n*r - STAB[n])
            print("%3d %3d %6d %8d %8d %8d   det bound %d %s"
                  % (n, r, n*n*r, tgt, d, p, pred, "OK" if d == pred else "<-- differs"))
