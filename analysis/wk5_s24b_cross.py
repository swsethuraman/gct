#!/usr/bin/env python3
"""
Session 24b -- does the screen's failure survive larger delta?

m_det_n(lam) is a symmetric rectangular Kronecker coefficient in n^2 variables;
m_perpad(lam) is bounded by a count in only m^2+1 = 10 variables.  Kronecker
coefficients of rectangles grow fast, so in principle m_det could overtake
m_perpad at large delta and REOPEN the line.  This probes the det-favourable
weight families -- the ones nearest the rectangle (delta^n), where the
Kronecker coefficient is largest -- as delta grows, and reports the margin
P = m_perpad - m_det.  A margin that shrinks would be the warning sign.
"""
import sys, time
sys.path.insert(0, '/root/gct/analysis')
from wk5_s24b_sf import m_det
from wk5_s24b_per import m_perpad

n, m = 4, 3
print("n=%d, m=%d.  det-favourable weight families, margin P = m_perpad - m_det" % (n, m))
print("delta  lam                       m_det   m_perpad   P        time")
for delta in range(2, 7):
    fams = [tuple([delta] * 4),                       # the rectangle itself
            (2 * delta, delta, delta) if delta else None,
            (4 * delta,),                             # one row
            tuple([2 * delta] * 2),                   # two rows
            ]
    for lam in fams:
        if lam is None or sum(lam) != n * delta: continue
        if len(lam) > 10: continue
        t0 = time.time()
        try:
            md = m_det(lam, n, delta)
            mp = m_perpad(lam, delta, n, 2)
        except (RecursionError, MemoryError) as e:
            print("%5d  %-24s  ABORTED (%s)" % (delta, str(lam), type(e).__name__)); continue
        print("%5d  %-24s %7d %10d %5d   %6.0fs"
              % (delta, str(lam), md, mp, mp - md, time.time() - t0))
        sys.stdout.flush()
