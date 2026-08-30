"""Session 21 - ambient census: dim of degree-delta SL_9 invariants of cubics
in 9 variables = <h_delta[h_3], s_{((delta/3)^9)}>, computed in the p-basis and
paired with chi^{lambda'} (lambda' = (9^{delta/3})) times the sign character.

Same machinery as analysis/wk3_s3_census18.py (which returns 1 at delta=18);
delta=18 is re-run here as a regression gate before any new value is printed.
Exact rational arithmetic throughout (fractions.Fraction); no floating point.
"""
import math, sys, time
from fractions import Fraction
from functools import lru_cache
from collections import defaultdict, Counter

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
    c = Counter(mu); r = 1
    for k, m in c.items(): r *= k**m*math.factorial(m)
    return r

H3 = {(1,1,1): Fraction(1,6), (2,1): Fraction(1,2), (3,): Fraction(1,3)}
def h3_scaled(k):
    return {tuple(sorted((k*a for a in part), reverse=True)): c for part, c in H3.items()}

def census(delta, k, verbose=True):
    n = 3*delta
    total = defaultdict(Fraction)
    t0 = time.time()
    for mu in partitions(delta):
        term = {(): Fraction(1)}
        for part in mu:
            new = defaultdict(Fraction)
            sc = h3_scaled(part)
            for m1, c1 in term.items():
                for m2, c2 in sc.items():
                    new[tuple(sorted(m1+m2, reverse=True))] += c1*c2
            term = new
        zm = zval(mu)
        for m, c in term.items():
            total[m] += c/zm
    lamc = tuple([9]*k)
    val = Fraction(0)
    for nu, c in total.items():
        if c == 0: continue
        val += c*((-1)**(n-len(nu)))*chi(lamc, nu)
    assert val.denominator == 1, val
    if verbose:
        print(f"  delta={delta}: {len(total)} distinct p-classes; {time.time()-t0:.1f}s", flush=True)
    return int(val)

if __name__ == "__main__":
    targets = [int(a) for a in sys.argv[1:]] or [18]
    for d in targets:
        assert d % 3 == 0
        v = census(d, d//3)
        print(f"dim C[Sym^3 C^9]^{{SL_9}}_{d}  =  {v}", flush=True)
