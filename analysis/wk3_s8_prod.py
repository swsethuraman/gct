"""Product route to the conductor: amb multiplicities for the (a,a,a,b^6) family
members that could multiply to lambda' = (8,8,8,6^6) at degree 20."""
import math, sys
from fractions import Fraction
from functools import lru_cache
from collections import defaultdict
sys.setrecursionlimit(1000000)

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
@lru_cache(maxsize=None)
def h_pleth(delta):
    total = defaultdict(Fraction)
    for mu in partitions(delta):
        term = {(): Fraction(1)}
        for part in mu:
            term = dict_mul_p(term, h3_scaled(part))
        zm = zval(mu)
        for m, c in term.items():
            total[m] += c/zm
    return dict(total)

def conj(lam):
    if not lam: return ()
    m = lam[0]
    return tuple(sum(1 for x in lam if x > j) for j in range(m))

def amb(lam, delta):
    n = 3*delta
    lamT = conj(lam)
    P = h_pleth(delta)
    val = Fraction(0)
    for nu, c in P.items():
        if c == 0: continue
        val += c * ((-1)**(n - len(nu))) * chi(lamT, nu)
    assert val.denominator == 1
    return int(val)

CANDS = [((2,2,2,1,1,1,1,1,1), 4), ((3,3,3,2,2,2,2,2,2), 7),
         ((4,4,4,3,3,3,3,3,3), 10), ((5,5,5,4,4,4,4,4,4), 13),
         ((6,6,6,5,5,5,5,5,5), 16)]
for lam, d in CANDS:
    print(f"amb({lam}, delta={d}) = {amb(lam, d)}"); sys.stdout.flush()
