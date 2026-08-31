"""Session 23(b): ambient multiplicities amb(lambda', delta) = <h_delta[h_3], s_lambda'>
for the candidate odd-q weights.  Same machinery as wk3_s7_ray.py, parametrised,
with two independent validations (delta = 1 and delta = 2, where the plethysm is
classical: h_1[h_3] = s_3 and h_2[h_3] = s_6 + s_42)."""
import math, sys
from fractions import Fraction
from functools import lru_cache
from collections import defaultdict
sys.setrecursionlimit(100000)

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
def dmulp(P, Q):
    R = defaultdict(Fraction)
    for m1, c1 in P.items():
        for m2, c2 in Q.items():
            R[tuple(sorted(m1+m2, reverse=True))] += c1*c2
    return R

_cache = {}
def plethysm_pclasses(delta):
    if delta in _cache: return _cache[delta]
    total = defaultdict(Fraction)
    for mu in partitions(delta):
        term = {(): Fraction(1)}
        for part in mu:
            term = dmulp(term, h3_scaled(part))
        zm = zval(mu)
        for m, c in term.items(): total[m] += c/zm
    _cache[delta] = total
    return total

def conj(lam):
    if not lam: return ()
    return tuple(sum(1 for p in lam if p >= j) for j in range(1, lam[0]+1))

def amb(lam, delta):
    assert sum(lam) == 3*delta, (sum(lam), 3*delta)
    total = plethysm_pclasses(delta)
    lamT = conj(lam); n = 3*delta
    val = Fraction(0)
    for nu, c in total.items():
        if c == 0: continue
        val += c*(-1)**(n - len(nu))*chi(lamT, nu)
    assert val.denominator == 1, val
    return int(val)

if __name__ == '__main__':
    print("=== validation: delta = 1 (h_1[h_3] = s_3) and delta = 2 (h_2[h_3] = s_6 + s_42) ===")
    print("  amb((3),1)      =", amb((3,), 1), " [expect 1]")
    print("  amb((2,1),1)    =", amb((2,1), 1), " [expect 0]")
    print("  amb((6),2)      =", amb((6,), 2), " [expect 1]")
    print("  amb((4,2),2)    =", amb((4,2), 2), " [expect 1]")
    print("  amb((5,1),2)    =", amb((5,1), 2), " [expect 0]")
    print("  amb((3,3),2)    =", amb((3,3), 2), " [expect 0]")
    print("  amb((2,2,2),2)  =", amb((2,2,2), 2), " [expect 0: the deficit weight, ambient 0]")
    print()
    print("=== candidate odd-q weights lambda' = (p,p,p,q^6) ===")
    for p, q in [(3,1), (5,3), (7,5), (4,1), (6,3), (5,1), (4,3), (6,1), (7,3), (8,5)]:
        lam = tuple([p]*3 + [q]*6)
        delta = p + 2*q
        m = p - q
        if m <= 0: continue
        v = amb(lam, delta)
        print(f"  ({p},{p},{p},{q}^6)  delta = {delta:>3}  m = p-q = {m}   amb = {v}", flush=True)
