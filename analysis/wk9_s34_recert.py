#!/usr/bin/env python3
"""
Session 34 -- re-certification of three s30 cells, chosen by the pre-registered
deterministic rule (results/PREREG_s34.md section 1.3): SHA-256 of
"s34-recert-2026-09-01" mod 34, step 11 -> ledger rows 13, 24, 1.

Code path: wk8_s30_core.measure with a_expect from the plethysm, det seed 11,
pad seed 29, bound 40, npts = a+8 -- the exact call pattern of
wk8_s30_run62c.py, at delta = 6.  Every field must reproduce
results/sweep62_ledger.md exactly; any deviation is kill criterion 3.
"""
import sys, time, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from wk8_s30_core import measure, det_form, per_padded, monomials
from wk8_s30_pleth import amb

# (lam, expected: ell, a, N_S, mult_det, mult_pad, D) -- transcribed from the ledger
EXPECT = [
    ((13, 4, 4, 2, 1), (5, 2, 3199, 2, 2, 0)),   # ledger row 13
    ((9, 8, 5, 1, 1),  (5, 2, 5159, 2, 2, 0)),   # ledger row 24
    ((13, 5, 4, 1, 1), (5, 2, 1824, 2, 2, 0)),   # ledger row 1 (one of the nine)
]

if __name__ == '__main__':
    d4, N4 = det_form(4); pd, Np = per_padded(3, 4)
    A6 = amb(6, 4, 16)
    ok = True
    print("lam                     ell  a   N_S   mult_det  mult_pad   D    verdict")
    for lam, (ell_w, a_w, ns_w, md_w, mp_w, D_w) in EXPECT:
        t0 = time.time()
        r = len(lam)
        av = A6[lam]
        ns = len(monomials(4, r, 6, lam))
        md = measure(d4, N4, 4, r, 6, lam, a_expect=av)
        mp = measure(pd, Np, 4, r, 6, lam, seed=29, a_expect=av)
        got = (r, av, ns, md['mult'], mp['mult'], mp['mult'] - md['mult'])
        want = (ell_w, a_w, ns_w, md_w, mp_w, D_w)
        good = got == want
        ok &= good
        print("%-24s %2d %3d %6d    %2d        %2d      %+2d    %s  [%.0fs]"
              % (str(lam), r, av, ns, md['mult'], mp['mult'],
                 mp['mult'] - md['mult'],
                 "EXACT" if good else "*** DEVIATION *** got=%s want=%s" % (got, want),
                 time.time() - t0))
        sys.stdout.flush()
    print()
    print("RE-CERTIFICATION: %s" % ("all three EXACT -- P1 confirmed" if ok
          else "*** DEVIATION -- KILL CRITERION 3: STOP EVERYTHING ***"))
    sys.exit(0 if ok else 1)
