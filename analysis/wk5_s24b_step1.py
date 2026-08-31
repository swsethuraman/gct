#!/usr/bin/env python3
"""
Session 24b -- STEP 1: the Peter-Weyl pre-screen for the PADDED permanent.

A = closure(GL_{n^2} . det_n),  B = closure(GL_{n^2} . x_0^{n-m} per_m),
both in W = Sym^n C^{n^2}.  P(lam) = m_B(lam) - m_A(lam).

LEMMA (row bound, proved not assumed).  Let U* = span(x_0, y_11..y_mm) be the
span of the first partials of v = x_0^p per_m (p = n-m >= 1), Z = (U*)^perp,
u = dim V/Z = m^2+1.  Stab(v) preserves Z, contains all of GL(Z) and the whole
Hom-block, and acts on V/Z through Stab_{GL(U)}(v).  Restricting to the Levi,
   (S_lam V)^{Stab}  subset  (S_lam V)^{GL(Z) x Stab_{GL(U)}(v)}
                     =  (S_lam(U))^{Stab_{GL(U)}(v)} ,
which is 0 unless ell(lam) <= u.  Only this UPPER BOUND is used below, so the
screen's conclusion is rigorous even where the bound is not tight.

Stab_{GL(U)}(x_0^p per_m) is derived in results/PREREG_s24b.md: it is monomial,
{x_0 -> c x_0, y -> L y : per_m . L = c^{-p} per_m}, a 6-torus times the
order-72 finite part (S_3 x S_3) |x Z/2, of dimension 2m-1 = 5.
"""
import sys, time
sys.path.insert(0, '/root/gct/analysis')
from wk5_s24b_sf import partitions, m_det
from wk5_s24b_per import m_perpad

def screen(n, m, delta, route=2, verbose=True):
    assert m == 3
    N = n * delta
    u = m * m + 1
    live, pwobs, defonly, rows = 0, [], [], []
    for lam in partitions(N):
        if len(lam) > n * n:
            continue
        mp = m_perpad(lam, delta, n, route) if len(lam) <= u else 0
        if mp == 0:
            continue                      # no obstruction possible: mult_B <= m_B = 0
        live += 1
        md = m_det(lam, n, delta)
        rows.append((lam, md, mp))
        (pwobs if mp > md else defonly).append(lam)
    return rows, live, pwobs, defonly

if __name__ == '__main__':
    CASES = eval(sys.argv[1]) if len(sys.argv) > 1 else [(4,3,1),(4,3,2),(5,3,1),(5,3,2)]
    for (n, m, delta) in CASES:
        t0 = time.time()
        rows, live, pwobs, defonly = screen(n, m, delta)
        N = n * delta
        print("=== n=%d m=%d delta=%d  (lam |- %d, ell <= %d; exhaustive)  %.1fs"
              % (n, m, delta, N, n*n, time.time()-t0))
        print("    live weights (m_perpad > 0): %d" % live)
        print("    of these, m_per > m_det  (Peter-Weyl can separate): %d" % len(pwobs))
        print("    of these, m_per <= m_det (any obstruction must be")
        print("                              deficit-driven)          : %d" % len(defonly))
        if rows:
            print("    lam                         m_det      m_perpad    P")
            for lam, md, mp in rows[:24]:
                print("    %-26s %9d %11d %6d" % (str(lam), md, mp, mp - md))
            if len(rows) > 24:
                print("    ... %d more" % (len(rows) - 24))
        if pwobs:
            print("    *** PETER-WEYL OBSTRUCTION WEIGHTS:", pwobs[:10])
        print()
