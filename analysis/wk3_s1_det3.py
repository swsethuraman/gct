"""Week 3, session 1 — det_3 reconnaissance.
(A) parity: det_9(transpose-flip) = -1  => odd det-weight semiinvariants vanish on the orbit closure.
(B) orbit cone-dimensions of det_3 and the two Huettenhain-Lairez boundary representatives.
(C) census: dim of degree-3 and degree-6 SL_9-invariants of cubics in 9 variables
    (mult of (1^9) in Sym^3(Sym^3 C^9), of (2^9) in Sym^6(Sym^3 C^9)) via plethysm + MN.
(D) Kronecker starter table g_{lam,(d^3),(d^3)} for d = 1,2,3.
"""
import itertools, math
from fractions import Fraction
from functools import lru_cache
from collections import defaultdict
import numpy as np

# ---------- (A) ----------
perm = {}
for i in range(3):
    for j in range(3):
        perm[3*i+j] = 3*j+i
sign = 1
seen = [False]*9
for s in range(9):
    if not seen[s]:
        l = 0; t = s
        while not seen[t]:
            seen[t] = True; t = perm[t]; l += 1
        if l % 2 == 0: sign = -sign
print("(A) det_9(transpose flip) =", sign, " => semiinvariants of ODD det-weight vanish on the det_3 orbit closure")

# ---------- (B) ----------
def cubic_dict(expr_terms):
    return dict(expr_terms)
import sympy as sp
X = sp.symbols('x1:10')
det3 = sp.expand(sp.Matrix(3, 3, lambda i, j: X[3*i+j]).det())
M_tr = sp.Matrix(3, 3, lambda i, j: X[3*i+j])
M_tr[2, 2] = -X[0] - X[4]
P1 = sp.expand(M_tr.det())
P2 = sp.expand(X[3]*X[0]**2 + X[4]*X[1]**2 + X[5]*X[2]**2
               + X[6]*X[0]*X[1] + X[7]*X[1]*X[2] + X[8]*X[0]*X[2])
mons9 = [m for m in itertools.combinations_with_replacement(range(9), 3)]
mon_ix = {m: i for i, m in enumerate(mons9)}
def to_vec(f):
    P = sp.Poly(f, *X)
    v = np.zeros(len(mons9))
    for mono, cf in P.terms():
        if cf == 0 or sum(mono) != 3: continue
        idx = tuple(sorted([i for i in range(9) for _ in range(mono[i])]))
        v[mon_ix[idx]] = float(cf)
    return v
def orbit_cone_dim(f):
    vecs = []
    for s in range(9):
        for t in range(9):
            d = sp.expand(X[s]*sp.diff(f, X[t]))
            vecs.append(to_vec(d))
    return np.linalg.matrix_rank(np.array(vecs), tol=1e-8)
for name, f, expect in [("det3", det3, 65), ("P1 (traceless det)", P1, 64), ("P2 (universal quadric)", P2, 64)]:
    d = orbit_cone_dim(f)
    print(f"(B) cone-dim of G.{name} = {d} (expected {expect})", "OK" if d == expect else "SURPRISE")

# ---------- MN characters ----------
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
    c = Counter(mu); r = 1
    for k, m in c.items(): r *= k**m*math.factorial(m)
    return r

# ---------- (C) plethysm census ----------
# h3 in power sums: {(1,1,1):1/6, (2,1):1/2, (3,):1/3}
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
def h_pleth_h3(delta):
    total = defaultdict(Fraction)
    for mu in partitions(delta):
        term = {(): Fraction(1)}
        for part in mu:
            term = dict_mul_p(term, h3_scaled(part))
        zm = zval(mu)
        for m, c in term.items():
            total[m] += c/zm
    return total
for delta, k in [(3, 1), (6, 2)]:
    P = h_pleth_h3(delta)
    lam = tuple([k]*9)
    val = sum(c*chi(lam, nu) for nu, c in P.items())
    assert val.denominator == 1
    print(f"(C) dim of degree-{delta} SL_9-invariants of cubics in 9 vars (weight det^{k}): {val}")

# ---------- (D) Kronecker starter ----------
print("(D) Kronecker table g_(lam, (d^3), (d^3)), the orbit-side skeleton:")
for d in (1, 2, 3):
    n = 3*d
    rect = tuple(sorted([d]*3, reverse=True))
    fact = math.factorial(n)
    rows = []
    for lam in partitions(n):
        if len(lam) > 9: continue
        tot = 0
        for nu in partitions(n):
            tot += (fact//zval(nu))*chi(lam, nu)*chi(rect, nu)**2
        g = tot//fact
        if g: rows.append((lam, g))
    print(f"  delta={d}: nonzero g for", rows)
