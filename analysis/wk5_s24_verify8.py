#!/usr/bin/env python3
"""Session 24 -- independent verification of the Sym^8 witness at lam=(26,6)."""
import sys, itertools
sys.path.insert(0, '/root/gct/analysis')
from wk5_s24_orbit import subs_from_form, pmul
from wk5_s24_sym8 import m_K
import sympy as sp

def rank_mod(rows, cols, p):
    idx = {c: j for j, c in enumerate(cols)}
    M = [[0]*len(cols) for _ in rows]
    for i, r in enumerate(rows):
        for c, v in r.items(): M[i][idx[c]] = v % p
    m, n, rk = len(M), len(cols), 0
    for col in range(n):
        piv = next((i for i in range(rk, m) if M[i][col]), None)
        if piv is None: continue
        M[rk], M[piv] = M[piv], M[rk]
        inv = pow(M[rk][col], p-2, p)
        for i in range(rk+1, m):
            if M[i][col]:
                f = M[i][col]*inv % p
                for k in range(col, n): M[i][k] = (M[i][k]-f*M[rk][k]) % p
        rk += 1
        if rk == m: break
    return rk

def rank_QQ(rows, cols):
    """rank over Q by sympy (fully independent of the Bareiss implementation)."""
    idx = {c: j for j, c in enumerate(cols)}
    M = sp.zeros(len(rows), len(cols))
    for i, r in enumerate(rows):
        for c, v in r.items(): M[i, idx[c]] = v
    return M.rank()

def imdim(t, delta, b):
    cf = [1,0,0,0,t,0,0,0,1]
    z = subs_from_form(cf)
    rows = []
    for n in itertools.combinations_with_replacement(range(9), delta):
        if sum(n) != b: continue
        p = {(0,0,0,0): 1}
        for i in n: p = pmul(p, z[i])
        rows.append(p)
    cols = sorted({c for r in rows for c in r})
    return rows, cols

print("independent ranks for the witness weight lam=(26,6), delta=4")
print("(mult = dim Im_b - dim Im_{b-1}); primes 2147483647 and 1000000007")
for t in (1, 2):
    vals = {}
    for b in (5, 6):
        rows, cols = imdim(t, 4, b)
        r1 = rank_mod(rows, cols, 2147483647)
        r2 = rank_mod(rows, cols, 1000000007)
        r3 = rank_QQ(rows, cols)
        assert r1 == r2 == r3, (t, b, r1, r2, r3)
        vals[b] = r3
        print("   t=%d b=%d : %d rows x %d cols, rank = %d (3 routes agree)"
              % (t, b, len(rows), len(cols), r3))
    print("   => mult_(26,6) C[closure(f_%d)]_4 = %d" % (t, vals[6]-vals[5]))
print()
print("m_K((26,6)) by eigenbasis count =", m_K(26, 6))

# character-average cross-check of m_K
I = sp.I
mu8 = [sp.exp(2*sp.pi*I*k/8) for k in range(8)]
els = []
for al in mu8:
    for be in mu8:
        if sp.simplify(sp.expand_complex((al/be)**4)) == 1:
            els.append(('d', al, be)); els.append(('a', al, be))
def chi(g, a, b):
    ty, al, be = g
    if ty == 'd': e1, e2 = al, be
    else:
        r = sp.sqrt(al*be); e1, e2 = r, -r
    s = a-b
    return sp.simplify(((e1*e2)**(-b)) * sum(e1**(-j)*e2**(-(s-j)) for j in range(s+1)))
tot = sum(chi(g, 26, 6) for g in els)
print("|K| =", len(els), "; character average m_K((26,6)) =",
      sp.nsimplify(sp.simplify(sp.expand_complex(tot/len(els)))))
