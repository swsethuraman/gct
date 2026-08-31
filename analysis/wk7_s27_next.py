#!/usr/bin/env python3
"""Session 27 -- D: where the gate goes next.  The containment argument closes
every length-4 weight at every degree, so the next open cells are ell >= 5."""
import sys, time
sys.path.insert(0, '/root/gct/analysis')
from wk7_s27_pleth import amb
from wk7_s27_rank import monomials, measure, det_form, per_padded

A6 = amb(6, 4, 16)
g4 = [(l, v) for l, v in A6.items() if v >= 2 and len(l) == 4]
g5 = [(l, v) for l, v in A6.items() if v >= 2 and len(l) >= 5]
print("delta = 6, n = 4:  a>=2 and ell == 4 : %d  (closed by the containment theorem)"
      % len(g4))
print("                   a>=2 and ell >= 5 : %d  (GENUINELY OPEN)" % len(g5))
sizes = []
for lam, v in g5:
    r = len(lam)
    sizes.append((len(monomials(4, r, 6, lam)), lam, v, r))
sizes.sort()
print("\nthe ten cheapest open cells (weight-space dimension, lam, a, ell):")
for s in sizes[:10]: print("   %7d  %-22s a=%d ell=%d" % s)

f4, N4 = det_form(4); fp, Np = per_padded(3)
CAP = int(sys.argv[1]) if len(sys.argv) > 1 else 4000
print("\nmeasuring every open cell with weight space <= %d:" % CAP)
print("lam                      ell  a  |basis|  mult_det  mult_pad   D")
hits = []
for nb, lam, v, r in sizes:
    if nb > CAP: break
    t0 = time.time()
    md = measure(f4, N4, 4, r, 6, lam)
    mp = measure(fp, Np, 4, r, 6, lam, seed=29)
    assert md['a'] == v == mp['a'], (lam, v, md, mp)
    assert md['mult'] == md['mult_p2'] and mp['mult'] == mp['mult_p2'], (lam, md, mp)
    D = mp['mult'] - md['mult']
    if D > 0: hits.append((lam, v, md['mult'], mp['mult']))
    print("%-24s %2d  %2d  %6d    %2d        %2d      %+d   %s  [%.0fs]"
          % (str(lam), r, v, nb, md['mult'], mp['mult'], D,
             "*** OBSTRUCTION ***" if D > 0 else "", time.time() - t0))
    sys.stdout.flush()
print()
print("obstructions found: %d" % len(hits))
for h in hits: print("   ", h)
