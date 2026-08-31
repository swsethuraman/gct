#!/usr/bin/env python3
"""
Session 24 -- exact coordinate rings of the PARAMETRISED orbit closures in
Sym^4 C^2:  Gam = {l^4},  tau = {l^3 m},  Q = {q^2}.

C[X]_delta = image of Sym^delta(W^*) under the substitution.  We compute the
image dimension in each GL_2-weight space by exact integer rank, then
   mult_(a,b) = dim Im_(a,b) - dim Im_(a+1,b-1).
Independent of every closed form quoted in the paper.
"""
from fractions import Fraction
from functools import lru_cache
import itertools

# ---- polynomials as dict: exponent tuple -> int coefficient
def pmul(p, q):
    r = {}
    for e1, c1 in p.items():
        for e2, c2 in q.items():
            e = tuple(x + y for x, y in zip(e1, e2))
            r[e] = r.get(e, 0) + c1 * c2
    return {e: c for e, c in r.items() if c}

def binom(n, k):
    from math import comb
    return comb(n, k)

# ---- the three substitutions: z_i |-> polynomial in the parameters
def subs_Gam():
    # l = a*x + b*y  ;  l^4 ;  params (a,b) with weights (1,0),(0,1)
    return [{(4 - i, i): binom(4, i)} for i in range(5)], [(1, 0), (0, 1)]

def subs_tau():
    # l = a x + b y, m = c x + d y ; l^3 m ; params a,b,c,d
    z = []
    for i in range(5):
        p = {}
        # coefficient of x^{4-i} y^i in (ax+by)^3 (cx+dy)
        for k in range(4):           # from l^3: a^{3-k} b^k -> x^{3-k}y^k
            for t in range(2):       # from m: c^{1-t} d^t -> x^{1-t} y^t
                if k + t == i:
                    e = (3 - k, k, 1 - t, t)
                    p[e] = p.get(e, 0) + binom(3, k)
        z.append(p)
    return z, [(1, 0), (0, 1), (1, 0), (0, 1)]

def subs_Q():
    # q = a x^2 + b x y + c y^2 ; q^2 ; params a,b,c weights (2,0),(1,1),(0,2)
    q = {(1, 0, 0): 1, (0, 1, 0): 1, (0, 0, 1): 1}
    # build q^2 coefficient of x^{4-i}y^i explicitly
    mono = {0: (1, 0, 0), 1: (0, 1, 0), 2: (0, 0, 1)}   # a->x^2, b->xy, c->y^2
    xdeg = {0: 0, 1: 1, 2: 2}                            # y-degree contributed
    z = [dict() for _ in range(5)]
    for u in range(3):
        for v in range(3):
            i = xdeg[u] + xdeg[v]
            e = tuple(mono[u][t] + mono[v][t] for t in range(3))
            z[i][e] = z[i].get(e, 0) + 1
    return z, [(2, 0), (1, 1), (0, 2)]

SUBS = {'Gam': subs_Gam, 'tau': subs_tau, 'Q': subs_Q}

def rank_int(rows):
    """exact rank over Q of a list of dict-rows (col-key -> int)."""
    cols = sorted({c for r in rows for c in r})
    idx = {c: j for j, c in enumerate(cols)}
    mat = [[Fraction(r.get(c, 0)) for c in cols] for r in rows]
    m, n, rk = len(mat), len(cols), 0
    for j in range(n):
        piv = None
        for i in range(rk, m):
            if mat[i][j] != 0:
                piv = i; break
        if piv is None:
            continue
        mat[rk], mat[piv] = mat[piv], mat[rk]
        pv = mat[rk][j]
        for i in range(rk + 1, m):
            if mat[i][j] != 0:
                f = mat[i][j] / pv
                for k in range(j, n):
                    mat[i][k] -= f * mat[rk][k]
        rk += 1
        if rk == m:
            break
    return rk

@lru_cache(maxsize=None)
def image_dims(name, delta):
    """dict b -> dim of the weight-(4delta-b, b) part of C[X]_delta."""
    zsub, pw = SUBS[name]()
    nv = len(pw)
    # enumerate degree-delta monomials in z_0..z_4, grouped by b
    groups = {}
    for n in itertools.combinations_with_replacement(range(5), delta):
        b = sum(n)
        groups.setdefault(b, []).append(n)
    out = {}
    for b, mons in groups.items():
        rows = []
        for n in mons:
            p = {tuple([0] * nv): 1}
            for i in n:
                p = pmul(p, zsub[i])
            rows.append(p)
        out[b] = rank_int(rows)
    return out

@lru_cache(maxsize=None)
def mult_param(name, delta):
    """dict b -> mult of S_(4delta-b,b) in C[X]_delta."""
    d = image_dims(name, delta)
    return {b: d.get(b, 0) - d.get(b - 1, 0) for b in range(0, 2 * delta + 1)}

if __name__ == '__main__':
    for name in ['Gam', 'tau', 'Q']:
        print("==", name)
        for delta in range(1, 9):
            mm = mult_param(name, delta)
            print("  delta=%2d :" % delta,
                  " ".join("b=%d:%d" % (b, mm[b]) for b in sorted(mm) if mm[b]))
