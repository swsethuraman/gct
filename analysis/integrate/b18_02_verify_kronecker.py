"""Integrator check of B18-02's headline warning, at d = 3, rectangle mu = (3,3,3,3), lambda |- 12.
   g = [S^lambda : S^mu (x) S^mu]        (ordinary rectangular Kronecker)
   s = [S^lambda : Sym^2(S^mu)]          (symmetric one; transposition is the swap)
Characters of S_12 by Murnaghan-Nakayama on beta-numbers, written from the rule."""
from fractions import Fraction
from functools import lru_cache
from collections import Counter

N = 12

def partitions(n, maxp=None):
    if maxp is None: maxp = n
    if n == 0: yield (); return
    for k in range(min(n, maxp), 0, -1):
        for rest in partitions(n-k, k): yield (k,)+rest
PARTS = list(partitions(N))

def z(rho):
    c = Counter(rho); r = 1
    for i, m in c.items():
        r *= i**m
        for j in range(1, m+1): r *= j
    return r

@lru_cache(maxsize=None)
def chi(lam, rho):
    if not rho:  return 1 if not lam else 0
    if not lam:  return 0
    k, rest = rho[0], rho[1:]
    L = len(lam)
    beta = [lam[i] + (L-1-i) for i in range(L)]
    bset = set(beta)
    total = 0
    for b in beta:
        nb = b - k
        if nb < 0 or nb in bset: continue
        crossed = sum(1 for x in beta if nb < x < b)          # standard MN sign
        sign = -1 if crossed % 2 else 1
        newb = sorted([x for x in beta if x != b] + [nb], reverse=True)
        L2 = len(newb)
        newlam = tuple(x for x in (newb[i] - (L2-1-i) for i in range(L2)) if x > 0)
        total += sign * chi(newlam, rest)
    return total

def sq_type(rho):
    out = []
    for k in rho:
        if k % 2: out.append(k)
        else: out += [k//2, k//2]
    return tuple(sorted(out, reverse=True))

MU = (3,3,3,3)
print(f"rectangle mu = {MU},  lambda |- {N}\n")
for lam in [(6,3,1,1,1), (5,3,2,1,1)]:
    g = s = Fraction(0)
    for rho in PARTS:
        cm, cl, cm2 = chi(MU, rho), chi(lam, rho), chi(MU, sq_type(rho))
        g += Fraction(cm*cm*cl, z(rho))
        s += Fraction((cm*cm + cm2)*cl, 2*z(rho))
    print(f"  lambda = {lam}:   g = {g}   s = {s}   (skew part g - s = {g-s})")

f = {lam: chi(lam, (1,)*N) for lam in PARTS}
tot = sum(sum(Fraction(chi(MU,r)**2*chi(lam,r), z(r)) for r in PARTS) * f[lam] for lam in PARTS)
print(f"\n  control  sum_lambda g*f^lambda = {tot}   (f^mu)^2 = {f[MU]**2}   {'OK' if tot==f[MU]**2 else 'FAIL'}")
print(f"  control  g(mu,mu,(12))         = {sum(Fraction(chi(MU,r)**2*chi((N,),r), z(r)) for r in PARTS)}   (must be 1)")
print(f"  control  f^(3,3,3,3)           = {f[MU]}   (standard tableaux of the 4x3 rectangle)")
