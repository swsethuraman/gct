"""Integrator check of B18-01 section 8.

Claim: five-row cells first appear at degree 5; there are exactly 23 of them;
all have ambient multiplicity a = 1.

Ambient at degree d is Sym^d(Sym^4 C^5); cells are lambda |- 4d with at most 5 rows,
and a = multiplicity of the Schur module S_lambda(C^5), i.e. the coefficient of
s_lambda in the plethysm h_d[h_4] in five variables.

Computed here from scratch: monomial expansion of h_d[h_4] by dynamic programming
over multisets of the degree-4 monomials, then Schur coefficients by the
alternant  a_lambda = sum_sigma sgn(sigma) M[lambda + rho - sigma(rho)].
"""
import itertools
from functools import lru_cache

NVAR = 5
RHO  = (4,3,2,1,0)

def monomials(deg, n=NVAR):
    if n == 1: return [(deg,)]
    out=[]
    for k in range(deg+1):
        for rest in monomials(deg-k, n-1): out.append((k,)+rest)
    return out

def plethysm_monomial_coeffs(d, inner=4):
    """coeffs of h_d[h_inner] in NVAR variables, as {exponent tuple: multiplicity}"""
    base = monomials(inner)                       # the degree-4 monomials, 70 of them
    # dp[c] = {exponent vector : count} using multisets of size c from base processed so far
    dp = [dict() for _ in range(d+1)]
    dp[0][(0,)*NVAR] = 1
    for m in base:
        new = [dict(x) for x in dp]
        for c in range(d):                        # add 1..(d-c) copies of m
            for vec,cnt in dp[c].items():
                acc = vec
                for extra in range(1, d-c+1):
                    acc = tuple(a+b for a,b in zip(acc,m))
                    tgt = new[c+extra]
                    tgt[acc] = tgt.get(acc,0) + cnt
        dp = new
    return dp[d]

def schur_coeff(M, lam):
    """sum over S_5 of sgn(sigma) * M[lam + rho - sigma(rho)]"""
    tot = 0
    for perm in itertools.permutations(range(NVAR)):
        sgn = 1; p=list(perm)
        for a in range(NVAR):
            for b in range(a+1,NVAR):
                if p[a]>p[b]: sgn=-sgn
        alpha = tuple(lam[i]+RHO[i]-RHO[perm[i]] for i in range(NVAR))
        if min(alpha) < 0: continue
        tot += sgn * M.get(alpha, 0)
    return tot

def partitions_into_at_most(n, parts, maxpart=None):
    if maxpart is None: maxpart = n
    if parts == 0:
        if n == 0: yield ()
        return
    for first in range(min(n,maxpart), -1, -1):
        for rest in partitions_into_at_most(n-first, parts-1, first):
            yield (first,)+rest

for d in (2,3,4,5):
    M = plethysm_monomial_coeffs(d)
    lams = list(partitions_into_at_most(4*d, NVAR))
    rows5 = [l for l in lams if l[4] > 0]                 # exactly five rows
    live5 = [(l, schur_coeff(M,l)) for l in rows5]
    live5 = [(l,a) for l,a in live5 if a > 0]
    a1 = [l for l,a in live5 if a == 1]
    print(f"d={d}  lambda |- {4*d}:  5-row partitions {len(rows5):4}   "
          f"with a>0: {len(live5):4}   of those a==1: {len(a1):4}"
          + ("   <-- five-row cells first appear here" if live5 and d>2 and not prev else ""))
    prev = bool(live5)
    if d == 5:
        print("\n  the 23 five-row cells at degree 5 (lambda, a):")
        for l,a in sorted(live5):
            print("   ", l, " a =", a)
        print("\n  all a == 1:", all(a==1 for _,a in live5))
        print("  (4,4,4,4,4) present:", any(l==(4,4,4,4,4) for l,_ in live5))
