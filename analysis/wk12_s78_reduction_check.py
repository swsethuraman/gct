"""s78: certify the A5=I reduction against the direct ratio definition.

Direct definition (S2 report sec 3): Phi(A1..A5)_alpha = [s^alpha] det(sum s_k A_k).
Target chart y0=1: ratios r_alpha = F_alpha / F_0, F_0 = det A5.

Claim (algebraic reduction): the ratios are invariant under A_k -> P A_k Q, so on
the chart F_0 != 0 we may set A5 = I. Then
  F_0 = 1,
  good ratios r_alpha (alpha5>0) = [s^alpha] det(s5 I + sum_{k<=4} s_k B_k),  B_k = A5^{-1} A_k,
  bad  coeffs (alpha5=0)        = [s^alpha] det(sum_{k<=4} s_k B_k).
So D5 cap W cap {y0!=0} = image of { (B1..B4): det(sum_{k<=4} s_k B_k) == 0 }
under the 34 good char-poly coefficients. No f0 saturation; f0 == 1.

We verify at random points that:
  (1) r_alpha(A1..A5) == coeff_alpha(det(s5 I + sum s_k B_k)) for alpha5>0, and
  (2) F_alpha(A1..A5)/F0 == that, i.e. the normalization is exact,
over Q and both house primes.
"""
import sympy as sp, random, json
from itertools import permutations, product

def exps(deg, n):
    if n == 1: return [(deg,)]
    out = []
    for first in range(deg + 1):
        for rest in exps(deg - first, n - 1):
            out.append((first,) + rest)
    return out
E = exps(4, 5); anchor = E.index((0,0,0,0,4)); assert anchor == 0
good = [i for i,e in enumerate(E) if e[4] > 0 and i != anchor]
bad  = [i for i,e in enumerate(E) if e[4] == 0]

s = sp.symbols('s1 s2 s3 s4 s5')

def coeffs_of_det(mats):
    """mats: list of 5 sympy 4x4 matrices; return dict alpha->coeff of det(sum s_k mats[k])."""
    M = sp.zeros(4,4)
    for k in range(5): M += s[k]*mats[k]
    d = sp.expand(M.det())
    p = sp.Poly(d, *s)
    out = {e: 0 for e in E}
    for monom, co in zip(p.monoms(), p.coeffs()):
        out[tuple(monom)] = co
    return out

P1, P2 = 2147483647, 2147483629
rng = random.Random(20260908)
def randmat():
    return sp.Matrix(4,4, lambda i,j: rng.randint(-4,4))

all_ok = True
report = {"points": [], "primes": [P1, P2]}
for trial in range(4):
    A = [randmat() for _ in range(5)]
    while sp.Matrix(A[4]).det() == 0:
        A[4] = randmat()
    F = coeffs_of_det(A)                       # direct Phi
    F0 = F[(0,0,0,0,4)]
    assert F0 == A[4].det()
    # normalized B_k = A5^{-1} A_k
    A5inv = A[4].inv()
    B = [A5inv*A[k] for k in range(4)] + [sp.eye(4)]
    G = coeffs_of_det(B)                        # normalized
    assert G[(0,0,0,0,4)] == 1
    # check good ratios match normalized good coeffs, and bad ratio == normalized bad coeff
    ok_good = all(sp.nsimplify(F[E[i]]/F0 - G[E[i]]) == 0 for i in good)
    ok_bad  = all(sp.nsimplify(F[E[i]]/F0 - G[E[i]]) == 0 for i in bad)
    # prime checks: reduce the rational normalized coeff G (denominators are powers
    # of det A5) mod p properly, compare to F/F0 mod p.
    def rat_mod(q, p):
        q = sp.nsimplify(q); num, den = sp.fraction(sp.together(q))
        return (int(num) % p) * pow(int(den) % p, p-2, p) % p
    okp = True
    for p in (P1,P2):
        F0p = int(F0) % p; inv = pow(F0p, p-2, p)
        for i in good:
            lhs = (int(F[E[i]]) * inv) % p
            rhs = rat_mod(G[E[i]], p)
            if lhs != rhs: okp = False
    all_ok = all_ok and ok_good and ok_bad and okp
    report["points"].append(dict(trial=trial, F0=int(F0), good_ratio_match=bool(ok_good),
                                 bad_ratio_match=bool(ok_bad), prime_match=bool(okp)))
report["reduction_certified"] = bool(all_ok)
print(json.dumps(report, indent=2))
assert all_ok, "A5=I reduction failed"
print("\nA5=I REDUCTION CERTIFIED at random points (Q and both house primes).")
