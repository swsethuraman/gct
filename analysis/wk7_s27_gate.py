#!/usr/bin/env python3
"""Session 27 -- B: the n=4 gate.  Two conditions must both hold:
   ambient room a >= 2, and length ell(lam) >= 4 (session 26's reduction:
   det_4 restricted to any 3-plane is EVERY ternary quartic, so mult_det = a
   at ell <= 3 and no obstruction is possible there)."""
import sys
sys.path.insert(0, '/root/gct/analysis')
from wk7_s27_pleth import amb, parts

print(" delta | weights | a>=2 | and ell>=4 | and ell>=5")
GATE = {}
for delta in range(2, 7):
    A = amb(delta, 4, 16)
    nw = sum(1 for l in parts(4 * delta) if len(l) <= 16)
    ge2 = [(l, v) for l, v in A.items() if v >= 2]
    g4 = [(l, v) for l, v in ge2 if len(l) >= 4]
    g5 = [(l, v) for l, v in ge2 if len(l) >= 5]
    GATE[delta] = g4
    print("   %d   |  %5d  | %4d |    %4d    |    %4d"
          % (delta, nw, len(ge2), len(g4), len(g5)))
    sys.stdout.flush()
print()
print("the delta=5, ell>=4 gate, all of them:")
for lam, v in sorted(GATE[5], key=lambda x: (-x[1], x[0])):
    print("   %-16s ell=%d  a=%d" % (str(lam), len(lam), v))
