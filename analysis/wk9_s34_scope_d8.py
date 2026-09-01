#!/usr/bin/env python3
"""
Session 34 -- post-sweep scoping appendix (NOT pre-registered, NOT a
measurement): size the delta = 8 gate the way the census sized delta = 7, so
the next session's brief can be written from numbers rather than guesses.
Pure enumeration: plethysm + the exact N_S DP.  No variety is touched.
"""
import sys, os, json
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from wk8_s30_pleth import amb
from wk9_s34_census import ns_dp
import wk9_s34_census as C

C.DELTA = 8
if __name__ == '__main__':
    A8 = amb(8, 4, 16)
    gate = sorted([(lam, av) for lam, av in A8.items() if av >= 2 and len(lam) >= 5],
                  key=lambda c: tuple(-x for x in c[0]))
    print("delta=8 gate (ell>=5, a>=2): %d cells, %d ambient units"
          % (len(gate), sum(av for _, av in gate)))
    rows = []
    for lam, av in gate:
        ns = ns_dp(lam)
        rows.append((ns, lam, av, lam[0] - lam[-1]))
    rows.sort()
    ell5 = [r for r in rows if len(r[1]) == 5]
    print("ell=5: %d cells; cheapest ten:" % len(ell5))
    for ns, lam, av, bal in ell5[:10]:
        print("   %-26s a=%-3d bal=%-2d N_S=%-8d %.2f GB @5.6e-8"
              % (str(lam), av, bal, ns, 5.6e-8 * ns * ns))
    fit72 = [r for r in rows if 5.6e-8 * r[0] * r[0] <= 7.2]
    fit38 = [r for r in rows if 5.6e-8 * r[0] * r[0] <= 38.0]
    print("within 7.2 GB (this container class): %d cells, %d units"
          % (len(fit72), sum(r[2] for r in fit72)))
    print("within 38 GB (the s30-flagged bigger-box size): %d cells, %d units"
          % (len(fit38), sum(r[2] for r in fit38)))
    with open(os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                           'results', 'd8_scope.json'), 'w') as fh:
        json.dump([dict(lam=list(l), a=a, ns=n, bal=b) for n, l, a, b in rows], fh)
