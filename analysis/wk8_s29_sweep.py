#!/usr/bin/env python3
"""
Session 29 -- A: the first strict multiplicity inequality.

At length 3 the determinant is DENSE (D_3^{det_4} = all ternary quartics,
Jacobian rank 15 of 15), so mult_det = a at every length-3 weight.  The padded
permanent's stratum D_3^pad is the reducible ternary quartics {ell.c}, of
dimension 12 in 15 -- codimension 3.  Any length-3 weight with mult_pad < a is
therefore an immediate strict D < 0.  Sweep by ascending weight-space size.
"""
import sys, time
sys.path.insert(0, '/root/gct/analysis')
from wk8_s29_core import measure, det_form, per_padded, monomials
from wk8_s29_pleth import amb

d4, N4 = det_form(4)
pd, Np = per_padded(3, 4)
p2, Np2 = per_padded(2, 4)          # x_0^2 . per_2, the m=2 padded permanent

ELL = int(sys.argv[1]) if len(sys.argv) > 1 else 3
DMAX = int(sys.argv[2]) if len(sys.argv) > 2 else 5
CAP = int(sys.argv[3]) if len(sys.argv) > 3 else 6000

cells = []
for delta in range(2, DMAX + 1):
    for lam, av in amb(delta, 4, 16).items():
        if len(lam) != ELL: continue
        cells.append((len(monomials(4, ELL, delta, lam)), delta, lam, av))
cells.sort()
print("length-%d weights with a >= 1, delta <= %d : %d   (sweeping those with"
      " weight space <= %d)" % (ELL, DMAX, len(cells), CAP))
print("delta lam                dim    a  mult_det  mult_pad3  mult_pad2   D=pad3-det")
first = None
for nb, delta, lam, av in cells:
    if nb > CAP: break
    t0 = time.time()
    md = measure(d4, N4, 4, ELL, delta, lam)
    m3 = measure(pd, Np, 4, ELL, delta, lam, seed=29)
    m2 = measure(p2, Np2, 4, ELL, delta, lam, seed=53)
    assert md['a'] == av == m3['a'] == m2['a'], (lam, av, md, m3, m2)
    # the containment direction is a hard gate
    assert m3['mult'] <= md['mult'], ("CONTAINMENT VIOLATED", lam, delta, md, m3)
    assert m2['mult'] <= m3['mult'], ("CHAIN VIOLATED", lam, delta, m3, m2)
    D = m3['mult'] - md['mult']
    flag = ""
    if m3['mult'] < av and first is None:
        first = (delta, lam, av, md['mult'], m3['mult']); flag = "  <-- FIRST"
    print("  %d   %-18s %5d %3d   %3d %-6s %3d %-6s %3d %-6s %+3d%s   [%.0fs]"
          % (delta, str(lam), nb, av, md['mult'], "(=a)" if md['mult'] == av else "(<a)",
             m3['mult'], "(=a)" if m3['mult'] == av else "(<a)",
             m2['mult'], "(=a)" if m2['mult'] == av else "(<a)", D, flag,
             time.time() - t0))
    sys.stdout.flush()
print()
print("first cell with mult_pad3 < a :", first)
