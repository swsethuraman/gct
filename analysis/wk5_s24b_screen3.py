#!/usr/bin/env python3
"""
Session 24b -- STEP 1, final form.  Three necessary conditions, not one.

An obstruction to closure(per^pad) subset closure(det_n) at lam needs
   mult_lam C[per^pad] > mult_lam C[det_n] >= 0,
and  mult_lam C[X]_delta  <=  min( m_X(lam) , amb_delta(lam) )  for every
orbit closure X in the ambient, where amb = mult of S_lam in the plethysm
Sym^delta(Sym^n C^{n^2}).  So a weight can carry an obstruction only if

   (1) amb_delta(lam) > 0          -- else EVERY closure has mult 0
   (2) m_perpad(lam) > 0           -- else mult_B = 0
   (3) ell(lam) <= m^2 + 1         -- the row bound (implies (2) fails otherwise)

and it can carry a DEFICIT-DRIVEN one only if in addition

   (4) P(lam) = m_perpad(lam) - m_det(lam) <= 0.

Condition (1) is the cheap one and it is very restrictive: the plethysm
Sym^delta(Sym^n) has few constituents.  This screen applies (1) first.
"""
import sys, time
sys.path.insert(0, '/root/gct/analysis')
from wk5_s24b_sf import plethysm_schur, m_det
from wk5_s24b_per import m_perpad

def run(n, m, delta):
    t0 = time.time()
    amb = plethysm_schur(delta, n, n * n)
    u = m * m + 1
    rows, passes = [], []
    for lam, a in sorted(amb.items()):
        if len(lam) > u:
            continue                       # m_perpad = 0 by the row bound
        mp = m_perpad(lam, delta, n, 2)
        if mp == 0:
            continue                       # mult_B = 0
        md = m_det(lam, n, delta)
        rows.append((lam, a, md, mp))
        if mp <= md:
            passes.append((lam, a, md, mp))
    print("=== n=%d m=%d delta=%d : lam |- %d ; EXHAUSTIVE over all lam" % (n, m, delta, n*delta))
    print("    ambient constituents of Sym^%d(Sym^%d C^%d) : %d"
          % (delta, n, n*n, len(amb)))
    print("    of those with ell(lam) <= %d and m_perpad > 0 (LIVE): %d" % (u, len(rows)))
    if rows:
        print("    lam                          amb  m_det  m_perpad    P")
        for lam, a, md, mp in rows:
            print("    %-27s %4d %6d %9d %5d" % (str(lam), a, md, mp, mp - md))
    print("    of the live weights, P <= 0 (screen passes): %d" % len(passes))
    for lam, a, md, mp in passes:
        cap_B = min(mp, a); cap_A_lo = 0
        print("      *** %s : amb=%d m_det=%d m_perpad=%d -> mult_B <= %d;"
              % (str(lam), a, md, mp, cap_B))
        print("          an obstruction needs mult_A = 0 < mult_B, i.e. an")
        print("          OCCURRENCE obstruction (m_det = %d so def_det would be full)." % md)
    print("    [%.0fs]" % (time.time() - t0))
    sys.stdout.flush()
    return passes

if __name__ == '__main__':
    for c in eval(sys.argv[1]):
        run(*c)
