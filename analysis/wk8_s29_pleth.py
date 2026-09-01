#!/usr/bin/env python3
"""Session 29 -- plethysm a(lam,delta) for Sym^delta(Sym^n), independent route."""
from fractions import Fraction
from functools import lru_cache
from math import factorial

@lru_cache(maxsize=None)
def parts(n, mx=None):
    if mx is None: mx = n
    if n == 0: return ((),)
    o = []
    for k in range(min(n, mx), 0, -1):
        for r in parts(n - k, k): o.append((k,) + r)
    return tuple(o)

@lru_cache(maxsize=None)
def zr(rho):
    z, c = 1, {}
    for p in rho: c[p] = c.get(p, 0) + 1
    for p, m in c.items(): z *= p ** m * factorial(m)
    return z

@lru_cache(maxsize=None)
def chi(lam, rho):
    lam = tuple(x for x in lam if x)
    if not rho: return 1 if not lam else 0
    r, rest, L = rho[0], rho[1:], len(lam)
    beta = [lam[j] + (L - 1 - j) for j in range(L)]
    bs, tot = set(beta), 0
    for b in beta:
        nb = b - r
        if nb < 0 or nb in bs: continue
        ht = sum(1 for x in beta if nb < x < b)
        nbeta = sorted([x for x in beta if x != b] + [nb], reverse=True)
        mu = tuple(nbeta[j] - (L - 1 - j) for j in range(L))
        mu = tuple(x for x in mu if x)
        if any(mu[j] < mu[j + 1] for j in range(len(mu) - 1)): continue
        tot += (-1) ** ht * chi(mu, rest)
    return tot

@lru_cache(maxsize=None)
def pleth_p(delta, n):
    base = {rho: Fraction(1, zr(rho)) for rho in parts(n)}
    out = {}
    for rho in parts(delta):
        term = {(): Fraction(1)}
        for r in rho:
            pr = {}
            for s, c in base.items():
                k = tuple(sorted([r * x for x in s], reverse=True))
                pr[k] = pr.get(k, Fraction(0)) + c
            new = {}
            for x, cx in term.items():
                for y, cy in pr.items():
                    k = tuple(sorted(x + y, reverse=True))
                    new[k] = new.get(k, Fraction(0)) + cx * cy
            term = new
        for k, v in term.items(): out[k] = out.get(k, Fraction(0)) + v / zr(rho)
    return out

@lru_cache(maxsize=None)
def amb(delta, n, maxrows):
    P = pleth_p(delta, n); res = {}
    for lam in parts(n * delta):
        if len(lam) > maxrows: continue
        v = sum(c * chi(lam, rho) for rho, c in P.items())
        assert v.denominator == 1
        if v: res[lam] = int(v)
    return res

def a_of(lam, delta, n, maxrows):
    return amb(delta, n, maxrows).get(tuple(x for x in lam if x), 0)
