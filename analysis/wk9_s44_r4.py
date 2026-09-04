#!/usr/bin/env python3
"""
Session 44, Phase 4.4 -- the r = 4 column, which the guess `drop = C(r,5)`
predicts to be identically zero.

For r = 4 the rank-<= n-2 locus of the pencil has codimension 4 in P(M_n) and
P^3 has dimension 3, so by Kleiman a generic four-parameter pencil MISSES it
entirely: F = det M(s) is a SMOOTH hypersurface in P^3 (classically, the
generic determinantal cubic surface and quartic surface are smooth).  So the
partials are a regular sequence and rank M_d = rho_d at every d -- no drop, at
any degree, ever.  C(4,5) = 0 predicts exactly that, and C(5,5) = 1, C(6,5) = 6
are the measured drops at r = 5 and r = 6.  This run is the r = 4 leg.

usage: wk9_s44_r4.py [seed] [trials]
"""
import sys, os, random, time
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from wk9_s44_poly import *

SEED = int(sys.argv[1]) if len(sys.argv) > 1 else 20260903
TRIALS = int(sys.argv[2]) if len(sys.argv) > 2 else 3
BOX = 10 ** 6

if __name__ == '__main__':
    t0 = time.time()
    print(f"[s44 r=4] seed {SEED}, {TRIALS} pencils, box +-{BOX}, primes {PRIMES}")
    ok = True
    for n in (3, 4, 5):
        print(f"\n  n = {n}, r = 4 (3n-5 = {3*n-5}):")
        for d in range(n - 1, 3 * n + 1):
            rho = rho_generic(d, n, 4)
            rks = []
            for t in range(TRIALS):
                rnd = random.Random(SEED + 4404 * t + 31 * n + d)
                F = det_point(n, 4, rnd, BOX)
                rks += [macaulay_rank(F, n, d, 4, p) for p in PRIMES]
            drop = rho - min(rks)
            if drop: ok = False
            star = '  *** DROP ***' if drop else ''
            print(f"    d={d:2d}: cols {dim_sym(d,4):5d}  rho {rho:5d}  "
                  f"determinantal ranks {sorted(set(rks))}  drop {drop}{star}")
        sys.stdout.flush()
    print(f"\n  C(4,5) = 0 predicts no drop at any d: "
          f"{'CONFIRMED' if ok else 'REFUTED'}")
    print(f"[s44 r=4] done in {time.time()-t0:.1f}s")
