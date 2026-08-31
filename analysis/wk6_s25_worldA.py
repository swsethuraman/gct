#!/usr/bin/env python3
"""
Session 25 -- World A tables, rederived from scratch (not imported from
analysis/wk5_s24_worldA.py, which is used only as a cross-check).

Ambient Sym^delta(Sym^4 C^2); lam = (4delta-b, b), 0 <= b <= 2delta.
Seven nonzero GL_2-orbit closures.  S_lam^* = Sym^s V^* (x) det^-b, s = a-b,
basis  x^i y^(s-i);  diag(al,be) acts by al^{-(i+b)} be^{-(s-i+b)}.
"""
import sys
from functools import lru_cache
sys.path.insert(0, '/root/gct/analysis')
from wk6_s25_core import a_of

@lru_cache(maxsize=None)
def _box(delta):
    """N(b) = #partitions of b into at most 4 parts each <= delta, as a list.
    Counted as (n1,n2,n3,n4) >= 0 with sum n_i <= delta and sum i n_i = b
    (the conjugate description).  Validated against the plethysm route below."""
    W = 4 * delta
    dp = [[0] * (W + 1) for _ in range(delta + 1)]
    dp[0][0] = 1
    for v in (1, 2, 3, 4):
        nd = [[0] * (W + 1) for _ in range(delta + 1)]
        for c in range(delta + 1):
            for w in range(W + 1):
                if dp[c][w]:
                    k = 0
                    while c + k <= delta and w + v * k <= W:
                        nd[c + k][w + v * k] += dp[c][w]
                        k += 1
        dp = nd
    return [sum(dp[c][w] for c in range(delta + 1)) for w in range(W + 1)]

def aA(delta, b):
    if delta < 0 or b < 0 or b > 4 * delta: return 0
    N = _box(delta)
    return N[b] - (N[b - 1] if b else 0)

# ------------------------------------------------------------------ mult
def mult(X, d, b):
    if b < 0 or b > 2 * d: return 0
    if X == 'Gam': return 1 if b == 0 else 0
    if X == 'tau': return 1 if (b <= d and b != 1) else 0
    if X == 'Q':   return 0 if (d == 1 and b == 2) else (1 if b % 2 == 0 else 0)
    if X == 'Iz':  return aA(d, b) - aA(d - 2, b - 4)
    if X == 'Jz':  return aA(d, b) - aA(d - 3, b - 6)
    if X in ('Ac', 'D'): return aA(d, b) - aA(d - 6, b - 12)
    raise KeyError(X)

# ------------------------------------------------------- Peter-Weyl counts
def _pairs(idx, s, b):
    """collapse an index set under i <-> s-i with the det^-b sign."""
    n = 0
    for i in idx:
        j = s - i
        if i < j: n += 1
        elif i == j: n += 1 if b % 2 == 0 else 0
    return n

def m_of(X, d, b):
    a = 4 * d - b
    s = a - b
    if X == 'Gam': return 1 if b == 0 else 0
    if X == 'tau': return 1 if b <= d else 0
    if X == 'Q':   return 1 if b % 2 == 0 else 0
    if X == 'Jz':                       # mu_4^2 |x S_2, order 32
        idx = [i for i in range(s + 1) if (i + b) % 4 == 0 and (s - i + b) % 4 == 0]
        return _pairs(idx, s, b)
    if X in ('Ac', 'D'):                # be = eps al^-1, eps = +-1, al in mu_4
        idx = [i for i in range(s + 1)
               if (s - 2 * i) % 4 == 0 and (s - i + b) % 2 == 0]
        return _pairs(idx, s, b) if X == 'Ac' else len(idx)   # D is diagonal only
    if X == 'Iz':                       # order 48; via the J-ray of {I=0}
        seen = []
        for k in range(40):
            seen.append(mult('Iz', d + 3 * k, b + 6 * k))
            if len(seen) >= 6 and len(set(seen[-5:])) == 1: return seen[-1]
        raise RuntimeError('Iz ray did not stabilise')
    raise KeyError(X)

NAMES = ['Gam', 'tau', 'Q', 'Iz', 'Jz', 'Ac', 'D']
# X is contained in every member of SUB[X]
SUB = {'Gam': {'Gam','tau','Q','Iz','Jz','Ac','D'}, 'tau': {'tau','Iz','Jz','Ac','D'},
       'Q': {'Q','D'}, 'Iz': {'Iz'}, 'Jz': {'Jz'}, 'Ac': {'Ac'}, 'D': {'D'}}
DMAX = 14

def table(dmax=DMAX):
    T = {}
    for X in NAMES:
        for d in range(1, dmax + 1):
            for b in range(0, 2 * d + 1):
                mm, uu = m_of(X, d, b), mult(X, d, b)
                assert uu >= 0 and mm - uu >= 0, (X, d, b, mm, uu)
                assert uu <= aA(d, b), ("AMBIENT CAP VIOLATED", X, d, b, uu, aA(d, b))
                T[(X, d, b)] = (mm, uu, mm - uu)
    return T

if __name__ == '__main__':
    T = table()
    print("built %d cells; def >= 0 and mult <= a hold everywhere" % len(T))
    bad0 = [(d, b) for d in range(1, 15) for b in range(0, 2 * d + 1)
            if aA(d, b) != a_of((4 * d - b, b), d, 4, 2)]
    print("World A ambient: box DP vs plethysm, %d disagreements (delta<=14, b<=2delta;\n   beyond b=2delta lam is not a partition and the two conventions differ by design)" % len(bad0))
    sys.path.insert(0, '/root/gct/analysis')
    import wk5_s24_worldA as OLD
    Told = OLD.build()
    bad = [(k, T[k], Told[k]) for k in T if T[k] != Told[k]]
    print("cross-check against the committed session-24 tables: %d disagreements" % len(bad))
    for x in bad[:6]: print("   ", x)
