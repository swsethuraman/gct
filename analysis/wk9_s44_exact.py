#!/usr/bin/env python3
"""
Session 44 -- exact (characteristic-zero) rank of M_7 at determinantal points,
and the Schwartz-Zippel certificate that upgrades "measured drop" to "drop with
an explicit failure probability".

A rank measured modulo p is a LOWER bound on the rank over Q, so a mod-p drop
does not by itself prove that the generic determinantal rank drops.  Two steps
close the gap:

 1. exact rank over Z at an explicit integer pencil (fmpz_mat), which decides
    rank_Q at that pencil;
 2. Schwartz-Zippel: the entries of M_d(F) are linear in the coefficients of F,
    which are degree-n in the pencil entries, so every rho x rho minor is a
    polynomial of degree n*rho in the 96 pencil entries.  If the generic
    determinantal rank were rho, some such minor would be a nonzero polynomial
    of that degree, and a uniform random integer pencil from a box of side
    2*BOX+1 would kill it with probability at most n*rho/(2*BOX+1).

usage: wk9_s44_exact.py [seed] [logbox] [pencils] [n] [r] [d]
"""
import sys, os, random, time
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from wk9_s44_poly import *

SEED = int(sys.argv[1]) if len(sys.argv) > 1 else 20260903
LOGBOX = int(sys.argv[2]) if len(sys.argv) > 2 else 6
NPEN = int(sys.argv[3]) if len(sys.argv) > 3 else 2
N = int(sys.argv[4]) if len(sys.argv) > 4 else 4
R = int(sys.argv[5]) if len(sys.argv) > 5 else 6
D = int(sys.argv[6]) if len(sys.argv) > 6 else 7
BOX = 10 ** LOGBOX

if __name__ == '__main__':
    rho = rho_generic(D, N, R)
    deg = N * rho
    print(f"[s44 exact] n={N} r={R} d={D}, rho={rho}, box +-10^{LOGBOX}, {NPEN} pencils")
    print(f"  a rho x rho minor is a polynomial of degree n*rho = {deg} in the "
          f"{R*N*N} pencil entries")
    print(f"  Schwartz-Zippel failure probability per pencil <= {deg}/{2*BOX+1} "
          f"= {deg/(2*BOX+1):.3e}")
    allok = True
    for t in range(NPEN):
        rnd = random.Random(SEED + 777007 * t)
        F = det_point(N, R, rnd, BOX)
        t0 = time.time()
        rp = [macaulay_rank(F, N, D, R, p) for p in PRIMES]
        t1 = time.time()
        rq = macaulay_rank_exact(F, N, D, R)
        t2 = time.time()
        ok = rq < rho
        allok &= ok
        print(f"  pencil {t}: rank mod primes {rp} [{t1-t0:.1f}s] | "
              f"EXACT rank over Z = {rq} (rho {rho}, drop {rho-rq}) [{t2-t1:.1f}s] "
              f"{'DROP PROVED AT THIS POINT' if ok else 'NO DROP'}")
        sys.stdout.flush()
    if allok:
        p1 = deg / (2 * BOX + 1)
        print(f"\n  every 666-minor vanishes at {NPEN} independent uniform pencils; "
              f"if the generic determinantal rank were {rho} this has probability "
              f"<= {p1**NPEN:.3e}")
