#!/usr/bin/env python3
"""Session 24 -- ROUTE 2 for the Peter-Weyl counts of the finite stabilisers:
exact character averaging  m(lam) = (1/|H|) sum_{g in H} chi_{S_lam^*}(g),
with chi_{S_(a,b)}^*(g) = (al be)^{-b} sum_{j=0..a-b} al^{-j} be^{-(a-b-j)}
evaluated in Q(zeta_8) via sympy.  Compared against the eigenbasis counts.
"""
import sys
sys.path.insert(0, '/root/gct/analysis')
import sympy as sp
from wk5_s24_worldA import N_Jz, m_Ac, m_D

I = sp.I
mu4 = [sp.Integer(1), I, sp.Integer(-1), -I]

def diag(al, be):   return ('d', al, be)
def anti(al, be):   return ('a', al, be)   # [[0,al],[be,0]]

def eigen(g):
    t, al, be = g
    if t == 'd':
        return al, be
    r = sp.sqrt(al * be)
    return r, -r            # eigenvalues of [[0,al],[be,0]]

def chi_dual(g, a, b):
    al, be = eigen(g)
    s = a - b
    tot = sum((al ** (-j)) * (be ** (-(s - j))) for j in range(s + 1))
    return sp.simplify(((al * be) ** (-b)) * tot)

def group(name):
    if name == 'Jz':   # mu_4^2 |x S_2
        G = [diag(x, y) for x in mu4 for y in mu4]
        G += [anti(x, y) for x in mu4 for y in mu4]
        return G
    if name == 'Ac':   # {al^4=be^4=1,(al be)^2=1} |x S_2
        dd = [(x, y) for x in mu4 for y in mu4 if sp.simplify((x*y)**2) == 1]
        return [diag(*p) for p in dd] + [anti(*p) for p in dd]
    if name == 'D':    # {al^4=1,(al be)^2=1}, diagonal only
        dd = [(x, y) for x in mu4 for y in mu4 if sp.simplify((x*y)**2) == 1]
        return [diag(*p) for p in dd]
    raise KeyError(name)

FUN = {'Jz': N_Jz, 'Ac': m_Ac, 'D': m_D}
DMAX = 7
ok = True
for name in ['Jz', 'Ac', 'D']:
    G = group(name)
    bad = []
    for d in range(1, DMAX + 1):
        for b in range(0, 2 * d + 1):
            a = 4 * d - b
            tot = sum(chi_dual(g, a, b) for g in G)
            val = sp.simplify(tot / len(G))
            val = sp.nsimplify(val)
            if val != FUN[name](a, b):
                bad.append((d, a, b, val, FUN[name](a, b)))
    print(("PASS " if not bad else "FAIL ") +
          "R2 character average == eigenbasis count for H_%s (|H|=%d, delta<=%d)"
          % (name, len(G), DMAX), bad[:4])
    ok &= not bad
print("ALL CHARACTER CROSS-CHECKS PASSED" if ok else "MISMATCH")
