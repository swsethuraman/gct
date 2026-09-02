#!/usr/bin/env python3
"""Session 36 -- POST-HOC extension (labelled): the a = 1 cells, which the a >= 2
ambient gate excludes (they cannot carry multiplicity obstructions) but which
date the pad ideal's onset.  ell = r weights, a = 1, n_chi <= CAP, r = 5 at
delta 6 and r = 6 at delta 6, 7; both sides, both primes, plus mult_red."""
import sys, os, pickle
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
from wk8_s30_pleth import amb
from wk9_s36_stabred import measure_reduced, monomials, n_chi_of
from wk9_s36_census import N_S, stab_order
from wk9_s36_red import mult_red
CAP = int(sys.argv[1]) if len(sys.argv) > 1 else 3000
LO = int(sys.argv[2]) if len(sys.argv) > 2 else 0
out_md = '/root/s36/aone.md'
for r, delta in ((5, 6), (6, 6), (6, 7)):
    A = amb(delta, 4, r)
    cells = [(l, N_S(4, r, delta, l), stab_order(l)) for l, a in A.items() if len(l) == r and a == 1]
    cells.sort(key=lambda x: x[1] / x[2])
    for lam, ns, so in cells:
        if ns / so > CAP or ns / so <= LO: continue
        out = measure_reduced(4, r, delta, lam, 1, verbose=False)
        mr, _, _ = mult_red(out)
        line = f"| {r} | {delta} | `{lam}` | 1 | {out['N_S']} | {out['n_chi']} | {out['mult_det']} | {out['mult_pad']} | {mr} | {out['mult_pad']-out['mult_det']:+d} |"
        print(line, flush=True)
        with open(out_md, 'a') as fh: fh.write(line + "\n")
        pickle.dump(out, open(f"/root/s36/aone_{'_'.join(map(str, lam))}_d{delta}.pkl", 'wb'))
        monomials.cache_clear()
