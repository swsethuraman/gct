#!/usr/bin/env python3
"""Session 24 -- is the World A negative structural?  Test co-monotonicity."""
import sys
sys.path.insert(0, '/root/gct/analysis')
from wk5_s24_worldA import *
tab = build(); D = DMAX

fwd = bwd = 0; fwdbad = []; bwdbad = []
for A in NAMES:
    for B in NAMES:
        if A == B: continue
        for d in range(1, D + 1):
            for b in range(0, 2 * d + 1):
                mA, uA, _ = tab[(A, d, b)]; mB, uB, _ = tab[(B, d, b)]
                if uB > uA:
                    fwd += 1
                    if not (mB > mA): fwdbad.append((A,B,d,b))
                if mB > mA:
                    bwd += 1
                    if not (uB >= uA): bwdbad.append((A,B,d,b,mA,uA,mB,uB))

print("cells with mult_B > mult_A : %5d ;  of these  m_B > m_A fails in %d"
      % (fwd, len(fwdbad)))
print("cells with m_B > m_A       : %5d ;  of these  mult_B >= mult_A fails in %d"
      % (bwd, len(bwdbad)))
print("  first failures of the converse:", bwdbad[:6])
print()
print("=> the two invariants induce the SAME preorder on the seven closures"
      if not fwdbad and not bwdbad else
      "=> the preorders differ; the negative is not pure order-degeneracy")
print()

# Conductor-window theorem, tested on the pair (tau, Jz) and (Q, Jz):
# common ray step for the two boundary semiinvariants.
print("conductor-window check: along the I-ray (delta+2, b+4) of {J=0},")
print("m must be constant and def must fall to 0:")
for (d, b) in [(3, 1), (5, 2), (7, 3), (6, 0)]:
    row = []
    for k in range(0, 8):
        dd, bb = d + 2 * k, b + 4 * k
        mm = N_Jz(4 * dd - bb, bb); uu = MULT['Jz'](dd, bb)
        row.append((mm, mm - uu))
    print("   lam=(%2d,%d) delta=%2d : (m,def) along ray = %s" % (4*d-b, b, d, row))
