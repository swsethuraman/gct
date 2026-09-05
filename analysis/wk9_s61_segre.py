#!/usr/bin/env python3
"""Session 61, M1: the polar degrees of the smooth Segre variety P^3 x P^3 in P^15,
exactly, from its Chern classes (Piene/Holme formula for a smooth m-fold X in P^N):

    mu_k = sum_{i=0}^{k} (-1)^i C(m-i+1, k-i) * deg c_i(X),   deg c_i := int c_i(T_X) h^{m-i}.

The conormal variety of the determinant hypersurface {det_4 = 0} is the conormal
variety of its dual, the Segre P^3 x P^3, with the two factors swapped; so the
determinant's polar profile (delta_0, ..., delta_6) must be (mu_6, ..., mu_0).

Pure integer arithmetic (python-flint fmpz_poly for the bivariate bookkeeping via a
dictionary; nothing floating).  Also prints the same formula for P^2 x P^2 (the
3 x 3 determinant, whose profile (3,6,12,12,6) is classical) and P^1 x P^1.
"""
from math import comb
import sys

def segre_polar_degrees(a_dim, b_dim):
    """Polar degrees mu_0..mu_m of P^a x P^b in its Segre embedding, m = a + b."""
    m = a_dim + b_dim
    # Chern class of T = (1+A)^{a+1} (1+B)^{b+1}, truncated at A^{a+1}=0, B^{b+1}=0.
    # Represent classes as dict {(i,j): coeff} for A^i B^j.
    def mul(P, Q):
        R = {}
        for (i1, j1), c1 in P.items():
            for (i2, j2), c2 in Q.items():
                i, j = i1 + i2, j1 + j2
                if i <= a_dim and j <= b_dim:
                    R[(i, j)] = R.get((i, j), 0) + c1 * c2
        return R
    def power(P, n):
        R = {(0, 0): 1}
        for _ in range(n):
            R = mul(R, P)
        return R
    onepA = {(0, 0): 1, (1, 0): 1}
    onepB = {(0, 0): 1, (0, 1): 1}
    cT = mul(power(onepA, a_dim + 1), power(onepB, b_dim + 1))
    h = {(1, 0): 1, (0, 1): 1}
    def integrate(P):
        # int A^a B^b = 1
        return P.get((a_dim, b_dim), 0)
    def c_i(i):
        return {k: v for k, v in cT.items() if k[0] + k[1] == i}
    deg_c = []
    for i in range(m + 1):
        deg_c.append(integrate(mul(c_i(i), power(h, m - i))))
    mu = []
    for k in range(m + 1):
        s = 0
        for i in range(k + 1):
            s += (-1) ** i * comb(m - i + 1, k - i) * deg_c[i]
        mu.append(s)
    return deg_c, mu

if __name__ == "__main__":
    for (a, b) in [(1, 1), (2, 2), (3, 3)]:
        deg_c, mu = segre_polar_degrees(a, b)
        n = a + 1
        print(f"P^{a} x P^{b}  (dual of det_{n} in P^{n*n-1}):")
        print(f"   deg c_i(T) . h^(m-i), i=0..m : {deg_c}")
        print(f"   polar degrees mu_0..mu_m       : {mu}")
        print(f"   => predicted det_{n} profile     : {list(reversed(mu))} then zeros")
        print(f"   sum (generic ED degree)        : {sum(mu)}")
    deg_c, mu = segre_polar_degrees(3, 3)
    target = [4, 12, 36, 68, 84, 60, 20]
    ok = list(reversed(mu)) == target
    print()
    print("M1 check: reversed mu == (4,12,36,68,84,60,20)?", ok)
    sys.exit(0 if ok else 1)
