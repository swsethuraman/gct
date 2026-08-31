#!/usr/bin/env python3
"""
Session 25 -- QUESTION B: the race between m_det and the ambient cap a.

The prize profile is  m_det(lam) < a(lam,delta):  the determinant lacking the
orbit functions to fill the ambient room.  NOTE (registered in PREREG_s25):
this is HALF-free, not free.  It caps mult_det below a by group theory alone,
but an obstruction still needs mult_per > mult_det, i.e. a lower bound on
mult_per, i.e. an upper bound on def_per.  It removes the deficit's work on one
side only.

Reported per (n, delta), over the ambient support a >= 1 and over the live
locus a >= 2:  sum a, sum m_det, the ratio, #(m_det < a), #(m_det = a),
and the worst margin min(m_det - a).
"""
import sys, time
sys.path.insert(0, '/root/gct/analysis')
from wk6_s25_core import parts, m_det, amb_row

def race(n, delta):
    A = amb_row(delta, n, n * n)
    sup = sorted(A.items())
    rows = [(lam, a, m_det(lam, n, delta)) for lam, a in sup]
    def agg(sel):
        R = [r for r in rows if sel(r[1])]
        if not R: return None
        sa = sum(r[1] for r in R); sm = sum(r[2] for r in R)
        return (len(R), sa, sm, sm / sa,
                sum(1 for r in R if r[2] < r[1]),
                sum(1 for r in R if r[2] == r[1]),
                min(r[2] - r[1] for r in R))
    return rows, agg(lambda a: a >= 1), agg(lambda a: a >= 2)

if __name__ == '__main__':
    CASES = eval(sys.argv[1]) if len(sys.argv) > 1 else \
        [(3,2),(3,3),(3,4),(3,5),(3,6),(3,7),(4,2),(4,3),(4,4),(5,2),(5,3)]
    print(" n  delta | supp(a>=1)  sum a  sum m_det   ratio | m<a  m=a  min(m-a)"
          " || live(a>=2) suma summ  ratio  m<a")
    wins = []
    for (n, delta) in CASES:
        t0 = time.time()
        rows, s1, s2 = race(n, delta)
        w = [r for r in rows if r[2] < r[1]]
        wins += [(n, delta) + r for r in w]
        s2s = ("  %5d   %5d %4d %6.3f  %3d" % (s2[0], s2[1], s2[2], s2[3], s2[4])
               if s2 else "      -")
        print(" %d   %2d   |   %6d  %6d   %6d  %6.3f | %3d  %3d    %+d    ||%s   [%.0fs]"
              % (n, delta, s1[0], s1[1], s1[2], s1[3], s1[4], s1[5], s1[6], s2s,
                 time.time() - t0))
        sys.stdout.flush()
    print()
    if wins:
        print("*** WEIGHTS WITH m_det < a  (STOP AND REPORT):")
        for x in wins: print("   ", x)
    else:
        print("no weight anywhere in this range has m_det < a.")
