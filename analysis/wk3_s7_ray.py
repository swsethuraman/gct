"""Conductor bound at the first deficit weight of det_3.
def((2,2,2), 2) = 1 (orb 1, closure 0 since ambient 0).
The Phi18-ray: (lam + 6k*1^9, delta + 18k). k=1: lam' = (8,8,8,6,6,6,6,6,6), delta' = 20.
closure mult at k=1  <=  amb(lam', 20).  If amb = 0: conductor >= 2.
amb via <h_20[h3], s_lam'> = sum_nu c_nu eps(nu) chi^{lam'^T}(nu), lam'^T = (9^6, 3, 3).
Also factor Phi18(perm3) and the det/perm ratio.
"""
import math, sys
from fractions import Fraction
from functools import lru_cache
from collections import defaultdict
sys.setrecursionlimit(1000000)

from sympy import factorint, Rational
print("Phi18(perm3) = 50536120320 =", factorint(50536120320))
print("Phi18(det3)/Phi18(perm3) =", Rational(-877879296000, 50536120320))
sys.stdout.flush()

@lru_cache(maxsize=None)
def chi(lam, mu):
    if sum(lam) == 0: return 1
    t, rest = mu[0], mu[1:]
    k = len(lam)
    beta = [lam[i] + (k-1-i) for i in range(k)]
    S = set(beta); tot = 0
    for f in beta:
        g = f - t
        if g >= 0 and g not in S:
            between = sum(1 for x in S if g < x < f)
            nb = sorted((S - {f}) | {g}, reverse=True)
            kk = len(nb)
            nl = tuple(x - (kk-1-i) for i, x in enumerate(nb))
            nl = tuple(p for p in nl if p > 0)
            tot += (-1)**between * chi(nl, rest)
    return tot

def partitions(n, maxp=None):
    if maxp is None: maxp = n
    if n == 0:
        yield (); return
    for k in range(min(n, maxp), 0, -1):
        for rest in partitions(n-k, k):
            yield (k,) + rest

def zval(mu):
    from collections import Counter
    cc = Counter(mu); r = 1
    for k, m in cc.items(): r *= k**m*math.factorial(m)
    return r

H3 = {(1,1,1): Fraction(1,6), (2,1): Fraction(1,2), (3,): Fraction(1,3)}
def h3_scaled(k):
    return {tuple(sorted((k*a for a in part), reverse=True)): c for part, c in H3.items()}
def dict_mul_p(P, Q):
    R = defaultdict(Fraction)
    for m1, c1 in P.items():
        for m2, c2 in Q.items():
            m = tuple(sorted(m1+m2, reverse=True))
            R[m] += c1*c2
    return R

delta = 20
total = defaultdict(Fraction)
cnt = 0
for mu in partitions(delta):
    term = {(): Fraction(1)}
    for part in mu:
        term = dict_mul_p(term, h3_scaled(part))
    zm = zval(mu)
    for m, c in term.items():
        total[m] += c/zm
    cnt += 1
print(f"h_20[h3]: {cnt} outer partitions, {len(total)} power-sum classes")
sys.stdout.flush()

lamT = (9,9,9,9,9,9,3,3)   # conjugate of (8,8,8,6,6,6,6,6,6)
n = 60
def eps(nu):
    return (-1)**(n - len(nu))
val = Fraction(0)
done = 0
for nu, c in total.items():
    if c == 0: continue
    val += c*eps(nu)*chi(lamT, nu)
    done += 1
    if done % 100000 == 0:
        print(f"  ... {done} classes"); sys.stdout.flush()
assert val.denominator == 1
amb = int(val)
print(f"amb((8,8,8,6,6,6,6,6,6), delta=20) = {amb}")
if amb == 0:
    print("=> closure mult still 0 after one Phi18-step: CONDUCTOR of ((2,2,2),2) >= 2")
else:
    print(f"=> ambient supplies {amb} copies at k=1; closure mult <= {amb}; conductor >= 1, k=1 step undecided without closure computation")
