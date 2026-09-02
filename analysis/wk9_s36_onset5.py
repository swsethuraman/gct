#!/usr/bin/env python3
"""Session 36 -- is delta = 6 the FIRST degree of I(D_5^pad) = I(X_5)?  Every
ell = 5 weight with a >= 1 at delta <= 5 (r = 5), through the reduced pipeline
(both sides, both primes) and the point-free mult_red.  Also the ell = 6
weights at delta <= 6 with a >= 1 for I(X_6) (r = 6)."""
import sys, os, pickle
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
from wk8_s30_pleth import amb
from wk9_s36_stabred import measure_reduced, monomials
from wk9_s36_red import mult_red
rows = []
for r, deltas in ((5, (2, 3, 4, 5)), (6, (2, 3, 4, 5))):
    for delta in deltas:
        for lam, a in sorted(amb(delta, 4, r).items()):
            if len(lam) != r or a < 1: continue
            out = measure_reduced(4, r, delta, lam, a, verbose=False)
            mr, _, _ = mult_red(out)
            rows.append((r, delta, lam, a, out['N_S'], out['n_chi'], out['mult_det'], out['mult_pad'], mr))
            print(f"| {r} | {delta} | `{lam}` | {a} | {out['N_S']} | {out['n_chi']} | {out['mult_det']} | {out['mult_pad']} | {mr} |", flush=True)
            monomials.cache_clear()
pickle.dump(rows, open('/root/s36/onset5.pkl', 'wb'))
