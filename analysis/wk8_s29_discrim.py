#!/usr/bin/env python3
"""
Session 29 -- the DISCRIMINATING calibration the programme never had.

Every mult ever reported by this machinery (sessions 26, 27) equals a.  A
measurement that returns the maximum cannot detect a wrong kernel basis, since
a wrong basis of the right-dimensional space still generically has full rank.
So the convention was never tested.  Here it is tested against closed forms
that have mult < a in many places -- session 24's World A tables, which were
derived by a completely different route (substitution ranks and Gaussian
binomials, no highest-weight vectors at all).

In Sym^4 C^2 (n = 4, r = 2), writing lam = (4d-b, b):
    tau  = {l^3 m}    (x_0^3 x_1 , i.e. per_1 padded) : mult = [b <= d and b != 1]
    Gam  = {l^4}      (x_0^4)                          : mult = [b == 0]
and the ambient a is the Gaussian-binomial difference.
"""
import sys
sys.path.insert(0, '/root/gct/analysis')
from wk8_s29_core import measure, per_padded
from wk8_s29_pleth import a_of

f1, N1 = per_padded(1, 4)                  # x_0^3 x_1  -> {l^3 m} = tau
G = ({(4, 0): 1}, 2)                       # x_0^4      -> {l^4}   = Gamma

ok, ncells, ndisc = True, 0, 0
print("delta  b   a   mult_tau (want)   mult_Gam (want)")
for d in range(1, 8):
    for b in range(0, 2 * d + 1):
        lam = (4 * d - b, b)
        a = a_of(lam, d, 4, 2)
        if a == 0: continue
        ncells += 1
        mt = measure(f1, N1, 4, 2, d, lam)['mult']
        mg = measure(G[0], G[1], 4, 2, d, lam)['mult']
        wt = 1 if (b <= d and b != 1) else 0
        wg = 1 if b == 0 else 0
        if wt < a or wg < a: ndisc += 1
        good = (mt == wt and mg == wg)
        ok &= good
        print("  %d   %2d  %2d      %d (%d)          %d (%d)   %s"
              % (d, b, a, mt, wt, mg, wg, "" if good else "  *** MISMATCH ***"))
print()
print("cells: %d, of which DISCRIMINATING (some mult < a): %d" % (ncells, ndisc))
print("DISCRIMINATING CALIBRATION PASSED" if ok else "*** FAILED ***")
