"""Integrator check of B19-02 Lemma 4.1 and its pilot table.

r_n(d) = sum over rho |- 4d of  n^{ell(rho)} * chi_{(d^4)}(rho)^2 / z_rho
A_n(d) = dim Sym^d(Sym^4 C^n) = C(dim Sym^4(C^n) - 1 + d, d)
"""
from fractions import Fraction
from functools import lru_cache
from collections import Counter
from math import comb
import sys
sys.setrecursionlimit(100000)

def partitions(n, maxp=None):
    if maxp is None: maxp = n
    if n == 0: yield (); return
    for k in range(min(n, maxp), 0, -1):
        for r in partitions(n-k, k): yield (k,)+r

def z(rho):
    c = Counter(rho); r = 1
    for i, m in c.items():
        r *= i**m
        for j in range(1, m+1): r *= j
    return r

@lru_cache(maxsize=None)
def chi(lam, rho):
    if not rho: return 1 if not lam else 0
    if not lam: return 0
    k, rest = rho[0], rho[1:]
    L = len(lam)
    beta = [lam[i] + (L-1-i) for i in range(L)]
    bs = set(beta); tot = 0
    for b in beta:
        nb = b - k
        if nb < 0 or nb in bs: continue
        crossed = sum(1 for x in beta if nb < x < b)
        sgn = -1 if crossed % 2 else 1
        newb = sorted([x for x in beta if x != b] + [nb], reverse=True)
        L2 = len(newb)
        nl = tuple(x for x in (newb[i] - (L2-1-i) for i in range(L2)) if x > 0)
        tot += sgn * chi(nl, rest)
    return tot

def r_n(n, d):
    R = tuple([d]*4)
    tot = Fraction(0)
    for rho in partitions(4*d):
        tot += Fraction(n**len(rho) * chi(R, rho)**2, z(rho))
    assert tot.denominator == 1, f"non-integral at n={n}, d={d}"
    return int(tot)

def A_n(n, d):
    return comb(comb(n+3, 4) - 1 + d, d)

claim5 = {1:(70,70), 2:(2485,3585), 3:(59640,156080), 4:(1088430,5639705)}
print(f"{'n':>2} {'d':>2} {'A(d)':>12} {'r(d) mine':>14} {'B19-02':>14} {'r/A':>8}")
for d in (1,2,3,4):
    A, r = A_n(5,d), r_n(5,d)
    ca, cr = claim5[d]
    ok = (A == ca and r == cr)
    print(f"{5:>2} {d:>2} {A:>12} {r:>14} {cr:>14} {r/A:>8.3f}  {'OK' if ok else 'MISMATCH'}")
print()
r4 = {}
for d in (1,2,3,4):
    A, r = A_n(4,d), r_n(4,d)
    r4[d] = r/A
    print(f"{4:>2} {d:>2} {A:>12} {r:>14} {'':>14} {r/A:>8.3f}")
print(f"\nB19-02's n=4 ratios, first four: 1.000, 1.222, 1.739, 2.695")
print(f"mine:                             " + ", ".join(f"{r4[d]:.3f}" for d in (1,2,3,4)))
print(f"\ncontrols:")
print(f"  r_5(1) = {r_n(5,1)}  (must be 70 = dim Sym^4(C^5))")
print(f"  r_4(1) = {r_n(4,1)}  (must be 35 = dim Sym^4(C^4))")
R3 = (1,1,1)
bad = sum(Fraction(5**len(rho) * chi(R3,rho)**2, z(rho)) for rho in partitions(3))
print(f"  wrong rectangle (d^3) at d=1 gives {bad}, not 70 -> the formula does test the 4-row condition")
