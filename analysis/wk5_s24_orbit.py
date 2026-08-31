#!/usr/bin/env python3
"""
Session 24 -- general exact tool: the coordinate ring of ANY GL_2-orbit
closure in Sym^d C^2.

The orbit map is  A |-> v(a1 x + b1 y, a2 x + b2 y)  with A = (a|b) a 2x2
matrix of indeterminates.  Column 1 carries left-weight (1,0), column 2
carries (0,1), so the coefficient of x^{d-i} y^i is bihomogeneous of
bidegree (d-i, i) -- the same weight as z_i.  Hence

    dim C[closure(G.v)]_{delta, weight (a,b)}
        = rank of { image of the degree-delta monomials in z of weight (a,b) }

and mult_(a,b) = dim Im_(a,b) - dim Im_(a+1,b-1).
Rank is computed EXACTLY over Q by fraction-free (Bareiss) elimination.
"""
from fractions import Fraction
from functools import lru_cache
import itertools

def pmul(p, q):
    r = {}
    for e1, c1 in p.items():
        for e2, c2 in q.items():
            e = (e1[0]+e2[0], e1[1]+e2[1], e1[2]+e2[2], e1[3]+e2[3])
            r[e] = r.get(e, 0) + c1 * c2
    return {e: c for e, c in r.items() if c}

def subs_from_form(coeffs):
    """coeffs[i] = coefficient of x^{d-i} y^i in v.  Returns z_i |-> poly in
    (a1,a2,b1,b2), where v(a1 x+b1 y, a2 x+b2 y) is expanded."""
    d = len(coeffs) - 1
    z = [dict() for _ in range(d + 1)]
    from math import comb
    for j, c in enumerate(coeffs):          # term c * X^{d-j} Y^j
        if c == 0:
            continue
        # X = a1 x + b1 y ;  Y = a2 x + b2 y
        for u in range(d - j + 1):          # X^{d-j}: a1^u b1^{d-j-u} x^u y^{d-j-u}
            for w in range(j + 1):          # Y^j    : a2^w b2^{j-w} x^w y^{j-w}
                xd = u + w
                i = d - xd                  # y-degree
                e = (u, w, d - j - u, j - w)   # (a1,a2,b1,b2)
                z[i][e] = z[i].get(e, 0) + c * comb(d - j, u) * comb(j, w)
    return [{k: v for k, v in zi.items() if v} for zi in z]

def bareiss_rank(rows, cols):
    """exact rank over Q of an integer matrix given as dict-rows."""
    idx = {c: j for j, c in enumerate(cols)}
    M = [[0] * len(cols) for _ in rows]
    for i, r in enumerate(rows):
        for c, v in r.items():
            M[i][idx[c]] = v
    m, n = len(M), len(cols)
    rank, prev = 0, 1
    for col in range(n):
        piv = None
        for i in range(rank, m):
            if M[i][col]:
                piv = i; break
        if piv is None:
            continue
        M[rank], M[piv] = M[piv], M[rank]
        for i in range(rank + 1, m):
            if M[i][col] == 0 and all(M[i][k] == 0 for k in range(col, n)):
                continue
            for k in range(col + 1, n):
                M[i][k] = (M[rank][col] * M[i][k] - M[i][col] * M[rank][k]) // prev
            M[i][col] = 0
        prev = M[rank][col]
        rank += 1
        if rank == m:
            break
    return rank

def orbit_mult(coeffs, delta):
    """dict b -> mult of S_(d*delta-b, b) in C[closure(G.v)]_delta."""
    d = len(coeffs) - 1
    z = subs_from_form(coeffs)
    groups = {}
    for n in itertools.combinations_with_replacement(range(d + 1), delta):
        groups.setdefault(sum(n), []).append(n)
    dims = {}
    for b, mons in groups.items():
        rows = []
        for n in mons:
            p = {(0, 0, 0, 0): 1}
            for i in n:
                p = pmul(p, z[i])
            rows.append(p)
        cols = sorted({c for r in rows for c in r})
        dims[b] = bareiss_rank(rows, cols)
    return {b: dims.get(b, 0) - dims.get(b - 1, 0)
            for b in range(0, (d * delta) // 2 + 1)}
