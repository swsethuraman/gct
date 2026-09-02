#!/usr/bin/env python3
"""
Session 40, check 1 -- the numbers of the cap theorem, exactly.

  mu_k(n)   = [t^k] ((1 - t^{n-1})/(1 - t))^5          (smooth Milnor algebra)
  cap(n)    = C(3n-1, 4) - mu_{3n-5}(n)                  (rank of M_{3n-5})
  nu(n)     = deg {rank <= n-2} in P(M_n)               (Harris-Tu product)
  H_J(k)    = [t^k] (1 - n^2 t^{n-1} + (2n^2-2) t^n - n^2 t^{n+1} + t^{2n})/(1-t)^5
              (Gulliksen-Negard Hilbert function of S/J, J = (n-1)-minors)
  codim(n)  = C(n+4, 4) - (3n^2 + 2)                     (n >= 3)

Identities checked symbolically (polynomial in n) and numerically:
  cap(n) = 5 C(2n,4) - 10 C(n+1,4) = 5 n (n-1)^2 (7n-8) / 12
  nu(n)  = n^2 (n^2 - 1) / 12
  H_J(2n-5) = nu(n) - 1                    (the defect >= 1 at every n >= 3)
  H_J(n)    = codim(n)                     (tangent space of D_5 = J_n)
  nu(n) - H_J(n) = C(n-1, 4)               (the n = 5 anomaly and beyond)
"""
from math import comb, factorial
from fractions import Fraction
import sympy as sp

def mu(k, n):
    # [t^k] (1 - t^{n-1})^5 (1-t)^{-5}
    return sum((-1) ** j * comb(5, j) * comb(k - j * (n - 1) + 4, 4)
               for j in range(6) if k - j * (n - 1) >= 0)

def cap(n):
    return comb(3 * n - 1, 4) - mu(3 * n - 5, n)

def nu_harris_tu(n):
    # degree of {rank <= r} in M_{m x n} : prod_{i=0}^{n-r-1} (m+i)! i! / ((r+i)! (m-r+i)!)
    m, r = n, n - 2
    v = Fraction(1)
    for i in range(n - r):
        v *= Fraction(factorial(m + i) * factorial(i), factorial(r + i) * factorial(m - r + i))
    assert v.denominator == 1
    return int(v)

def H_J(k, n):
    N = {0: 1, n - 1: -n * n, n: 2 * n * n - 2, n + 1: -n * n, 2 * n: 1}
    return sum(c * comb(k - j + 4, 4) for j, c in N.items() if k - j >= 0)

def codim(n):
    return comb(n + 4, 4) - (3 * n * n + 2)

if __name__ == '__main__':
    print("n  | 3n-5 | dim S_{3n-5} | mu | cap(n) | closed form | nu(n) | n^2(n^2-1)/12 | codim D_5 | H_J(2n-5) | H_J(n) | nu-H_J(n) | C(n-1,4) | disc deg")
    for n in range(2, 13):
        c = cap(n); cf = Fraction(5 * n * (n - 1) ** 2 * (7 * n - 8), 12)
        assert cf.denominator == 1 and int(cf) == c, (n, c, cf)
        assert c == 5 * comb(2 * n, 4) - 10 * comb(n + 1, 4)
        nu = nu_harris_tu(n); assert nu * 12 == n * n * (n * n - 1)
        h25 = H_J(2 * n - 5, n) if n >= 3 else None
        hn = H_J(n, n) if n >= 3 else None
        cd = codim(n) if n >= 3 else None
        if n >= 3:
            assert h25 == nu - 1, (n, h25, nu)
            assert hn == cd, (n, hn, cd)
            assert nu - hn == comb(n - 1, 4), (n, nu, hn)
        print(f"{n:2d} | {3*n-5:4d} | {comb(3*n-1,4):12d} | {mu(3*n-5,n):4d} | {c:6d} | {int(cf):6d} | {nu:5d} | "
              f"{n*n*(n*n-1)//12:5d} | {cd if cd is not None else '-':>9} | {h25 if h25 is not None else '-':>9} | "
              f"{hn if hn is not None else '-':>6} | {nu-hn if hn is not None else '-':>9} | {comb(n-1,4):8d} | {5*(n-1)**4:8d}")
    # symbolic identities, as polynomials in n (valid for n >= 3; the binomials
    # C(m,4) are the polynomial m(m-1)(m-2)(m-3)/24, which agrees with the
    # true binomial for m >= 0 and vanishes at m = 0..3, so every term that
    # is absent for small n is absent as a polynomial too; the t^{2n} term
    # never contributes to degrees < 2n and is omitted)
    n = sp.symbols('n')
    C4 = lambda m: sp.expand(m * (m - 1) * (m - 2) * (m - 3) / 24)
    nu_s = n ** 2 * (n ** 2 - 1) / 12
    H = lambda k: sp.expand(C4(k + 4) - n ** 2 * C4(k - (n - 1) + 4) + (2 * n ** 2 - 2) * C4(k - n + 4) - n ** 2 * C4(k - (n + 1) + 4))
    id1 = sp.simplify(H(2 * n - 5) - (nu_s - 1))
    id2 = sp.simplify(H(n) - (C4(n + 4) - 3 * n ** 2 - 2))
    id3 = sp.simplify(nu_s - H(n) - C4(n - 1))
    id4 = sp.simplify(H(2 * n - 4) - nu_s)          # def_{2n-4}(N) = 0: the Milnor drop starts exactly at 3n-5
    cap_s = sp.expand(5 * C4(2 * n) - 10 * C4(n + 1) - sp.Rational(5, 12) * n * (n - 1) ** 2 * (7 * n - 8))
    print("\nsymbolic: H_J(2n-5) - (nu-1) =", id1, "| H_J(n) - codim =", id2,
          "| nu - H_J(n) - C(n-1,4) =", id3, "| H_J(2n-4) - nu =", id4, "| cap closed form residual =", cap_s)
    assert id1 == 0 and id2 == 0 and id3 == 0 and id4 == 0 and cap_s == 0
    for n_ in range(3, 13):
        assert H_J(2 * n_ - 4, n_) == nu_harris_tu(n_), n_
    # the term -n^2 C4(n-2) (j = n+1) is a polynomial vanishing at n = 2..5,
    # so the identities hold verbatim for n = 3, 4, 5 where that term is absent.
    print("all identities hold (symbolic, and numerically n = 2..12)")
