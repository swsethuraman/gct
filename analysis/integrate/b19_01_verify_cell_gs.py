"""Check B19-01's counterexample cell: d = 6, lambda = (4^6), claimed g = 13, s = 10.
Rectangle mu = (6,6,6,6) |- 24.  Characters of S_24 by Murnaghan-Nakayama."""
from fractions import Fraction
from functools import lru_cache
from collections import Counter
import sys
sys.setrecursionlimit(100000)
N = 24

def partitions(n, maxp=None):
    if maxp is None: maxp = n
    if n == 0: yield (); return
    for k in range(min(n, maxp), 0, -1):
        for rest in partitions(n-k, k): yield (k,)+rest
PARTS = list(partitions(N))
print("partitions of 24:", len(PARTS))

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
    bset = set(beta); tot = 0
    for b in beta:
        nb = b - k
        if nb < 0 or nb in bset: continue
        crossed = sum(1 for x in beta if nb < x < b)
        sgn = -1 if crossed % 2 else 1
        newb = sorted([x for x in beta if x != b] + [nb], reverse=True)
        L2 = len(newb)
        newlam = tuple(x for x in (newb[i] - (L2-1-i) for i in range(L2)) if x > 0)
        tot += sgn * chi(newlam, rest)
    return tot

def sq(rho):
    out = []
    for k in rho:
        if k % 2: out.append(k)
        else: out += [k//2, k//2]
    return tuple(sorted(out, reverse=True))

MU  = (6,6,6,6)
LAM = (4,4,4,4,4,4)
g = s = Fraction(0)
for i, rho in enumerate(PARTS):
    cm, cl, cm2 = chi(MU, rho), chi(LAM, rho), chi(MU, sq(rho))
    g += Fraction(cm*cm*cl, z(rho))
    s += Fraction((cm*cm + cm2)*cl, 2*z(rho))
print(f"\nlambda = {LAM}, mu = {MU}:")
print(f"   ordinary  g = {g}        (B19-01 claims 13)")
print(f"   symmetric s = {s}        (B19-01 claims 10)")
print(f"   skew part   = {g-s}")
print(f"\ncontrols:")
print(f"   g(mu,mu,(24)) = {sum(Fraction(chi(MU,r)**2*chi((N,),r), z(r)) for r in PARTS)}   (must be 1)")
print(f"   f^(6,6,6,6)   = {chi(MU,(1,)*N)}   (SYT of the 4x6 rectangle)")
print(f"   f^(4^6)       = {chi(LAM,(1,)*N)}   (SYT of the 6x4 rectangle - must equal the above by transpose)")
