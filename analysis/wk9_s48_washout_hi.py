#!/usr/bin/env python3
"""Session 48, target C -- Jacobian checks at the r* = 4 -> 3 transition (m = 13..18,
r = 3, 4).  Same machinery as wk9_s48_washout.py; separated because the DP cost
grows like m^2 2^m.  usage: wk9_s48_washout_hi.py [mlo] [mhi]"""
import sys, os, time, random
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from wk9_s48_washout import jac_rank, orbit_dim
from wk9_s44_poly import PRIMES
from math import comb

MLO = int(sys.argv[1]) if len(sys.argv) > 1 else 13
MHI = int(sys.argv[2]) if len(sys.argv) > 2 else 18
print(f"{'m':>3} {'r':>3} {'m^2 r':>7} {'orbit':>6} {'sharp':>7} {'dimSym':>8} "
      f"{'count?':>7} {'rank p1':>8} {'rank p2':>8} {'dense?':>7} {'codim':>6}  time", flush=True)
for m in range(MLO, MHI + 1):
    ob = orbit_dim(m)
    for r in (3, 4):
        dimS = comb(r + m - 1, m); sharp = m * m * r - ob
        t = time.time(); rks = []
        for p in PRIMES:
            rnd = random.Random(90000 + 131 * m + r)
            rk, nc = jac_rank(m, r, p, rnd); rks.append(rk)
        rk = max(rks)
        print(f"{m:>3} {r:>3} {m*m*r:>7} {ob:>6} {sharp:>7} {dimS:>8} "
              f"{str(sharp>=dimS):>7} {rks[0]:>8} {rks[1]:>8} {str(rk==dimS):>7} "
              f"{dimS-rk:>6}  {time.time()-t:.1f}s", flush=True)
