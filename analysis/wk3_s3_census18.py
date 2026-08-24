"""Week 3, session 3 — (A) degree-18 census: mult of (6^9) in Sym^18(Sym^3 C^9),
via <h_18[h_3], s_{(6^9)}> = sum_nu c_nu eps(nu) chi^{(9^6)}(nu).
(B) P1 transversal velocity and its x9-torus weight."""
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

def census(delta, k):
    n = 3*delta
    total = defaultdict(Fraction)
    t0 = time.time()
    mus = list(partitions(delta))
    for i, mu in enumerate(mus):
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
        val += c*((-1)**(n-len(nu)))*chi(lamc, nu)
    assert val.denominator == 1
    print(f"  [{len(total)} distinct classes; {time.time()-t0:.1f}s]")
    return int(val)

print("(A) degree-18 census (det^6):")
a18 = census(18, 6)
print(f"  dim of degree-18 SL_9-invariants of cubics in 9 vars = {a18}")
if a18 == 0:
    print("  => e(det_3) >= 21, and >= 24 by parity")
else:
    print(f"  => degree 18 is the candidate: e(det_3) = 18 iff some such invariant is nonzero on the closure (open for odd m)")

# ---------- (B) P1 transversal velocity ----------
import itertools
import numpy as np
import sympy as sp
X = sp.symbols('x1:10')
M_tr = sp.Matrix(3, 3, lambda i, j: X[3*i+j]); M_tr[2, 2] = -X[0]-X[4]
P1 = sp.expand(M_tr.det())
v1 = sp.expand(X[8]*(X[0]*X[4]-X[1]*X[3]))   # x9 * cofactor_33 = velocity of restoring the trace
mons9 = [m for m in itertools.combinations_with_replacement(range(9), 3)]
mon_ix = {m: i for i, m in enumerate(mons9)}
def to_vec(f):
    Pd = sp.Poly(f, *X)
    v = np.zeros(len(mons9))
    for mono, cf in Pd.terms():
        if cf == 0 or sum(mono) != 3: continue
        idx = tuple(sorted([i for i in range(9) for _ in range(mono[i])]))
        v[mon_ix[idx]] = float(cf)
    return v
rows = []
for s in range(9):
    for t in range(9):
        rows.append(to_vec(sp.expand(X[s]*sp.diff(P1, X[t]))))
A = np.array(rows)
r0 = np.linalg.matrix_rank(A, tol=1e-8)
r1 = np.linalg.matrix_rank(np.vstack([A, to_vec(v1)]), tol=1e-8)
print(f"\n(B) dim g.P1 = {r0}; with velocity v1 added: {r1}",
      "=> v1 is transversal (a normal-direction representative)" if r1 == r0+1 else "=> v1 NOT transversal")
# x9-torus weight of v1: substitution x9 -> t x9 scales v1 by t^1 (v1 has x9-degree 1)
print("   x9-scaling torus in stab(P1): v1 has weight 1;  mu_max(lambda) under this torus = lambda_1")
print("   conductor-formula P1-contribution (prediction, untested): floor(max x9-degree / 1) — e.g. at (2^9): 2")
