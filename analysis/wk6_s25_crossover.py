#!/usr/bin/env python3
"""
Session 25 -- the race, resolved by a dimension count.

m_det(lam) >= a(lam,delta) pointwise CANNOT persist.  Summing against Weyl
dimensions,

   Sigma_a(delta) = sum_lam a(lam,delta) dim S_lam(C^{n^2})
                  = dim Sym^delta(Sym^n C^{n^2}) = binom(A+delta-1, delta),
                    A = binom(n^2+n-1, n)                      -- grows like delta^{A-1}

   Sigma_m(delta) = sum_lam m_det(lam) dim S_lam(C^{n^2})      -- the degree-delta
                    part of C[GL_{n^2} . det_n], a cone of dimension
                    d = n^4 - (2n^2 - 2)                       -- grows like delta^{d-1}

and A >> d.  If m_det >= a pointwise then supp(a) is inside supp(m_det) and
Sigma_m >= Sigma_a.  So the pointwise inequality must FAIL once
Sigma_a > Sigma_m, and the crossover degree is a computable UPPER BOUND on the
first weight with m_det < a -- the "half-free" profile the programme wants.
"""
import sys
from math import comb
sys.path.insert(0, '/root/gct/analysis')
from wk6_s25_core import parts, m_det, amb_row, dimS

def sigmas(n, delta):
    N2 = n * n
    A = comb(N2 + n - 1, n)
    Sa = comb(A + delta - 1, delta)
    Sm = sum(m_det(lam, n, delta) * dimS(lam, N2)
             for lam in parts(n * delta) if len(lam) <= N2)
    return A, Sa, Sm

if __name__ == '__main__':
    for n in (3, 4):
        N2, A = n * n, comb(n * n + n - 1, n)
        d = n ** 4 - (2 * n * n - 2)
        print("n=%d : ambient Sym^delta(Sym^%d C^%d), A = dim Sym^%d C^%d = %d"
              % (n, n, N2, n, N2, A))
        print("       dim closure(det_%d) = %d, so Sigma_a ~ delta^%d and Sigma_m ~ delta^%d"
              % (n, d, A - 1, d - 1))
        print("  delta |        Sigma_a |        Sigma_m | Sigma_m / Sigma_a")
        for delta in range(2, 8 if n == 3 else 5):
            A_, Sa, Sm = sigmas(n, delta)
            print("   %2d   | %14d | %14d | %s"
                  % (delta, Sa, Sm, ("%.4g" % (Sm / Sa)) if Sa else "-"))
            sys.stdout.flush()
        print()
