#!/usr/bin/env python3
"""
Session 44, Phase 2 -- the ladder at n = 4, r = 6 (quartics in six variables).

For each d: rank M_d at (i) random quartics, (ii) det_4(sum_{i=1}^{6} s_i A_i),
(iii) padded permanents l(s) * per_3(A(s)) (Phase 4.1), at both house primes
with fresh seeds.  Report the smallest d with a strict drop below rho_d, and
the corank.

usage: wk9_s44_ladder.py [seed] [trials] [dmin] [dmax] [n] [r]
"""
import sys, os, random, time
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from wk9_s44_poly import *

SEED = int(sys.argv[1]) if len(sys.argv) > 1 else 20260903
TRIALS = int(sys.argv[2]) if len(sys.argv) > 2 else 3
DMIN = int(sys.argv[3]) if len(sys.argv) > 3 else 4
DMAX = int(sys.argv[4]) if len(sys.argv) > 4 else 8
N = int(sys.argv[5]) if len(sys.argv) > 5 else 4
R = int(sys.argv[6]) if len(sys.argv) > 6 else 6
BOX = 10 ** 6


def run():
    print(f"[s44 ladder] n={N} r={R} d={DMIN}..{DMAX}, seed {SEED}, {TRIALS} trials/kind, "
          f"box +-{BOX}, primes {PRIMES}")
    print(f"{'d':>3} {'rows':>6} {'cols':>6} {'h_d':>5} {'rho_d':>6} {'ceil':>6} "
          f"{'kind':>8} {'t':>2} {'rank p1':>8} {'rank p2':>8} {'corank':>7} {'drop':>6}")
    first = {}
    for d in range(DMIN, DMAX + 1):
        rho = rho_generic(d, N, R)
        rows = R * dim_sym(d - N + 1, R); cols = dim_sym(d, R)
        ceil = cols - H_GN(d, N, R)
        for kind in ('smooth', 'det', 'pad'):
            if kind == 'pad' and N != 4:
                continue
            for t in range(TRIALS):
                rnd = random.Random(SEED + 100003 * t + 1009 * d + 17 * N + R
                                    + {'smooth': 0, 'det': 1, 'pad': 2}[kind] * 7919)
                if kind == 'smooth':
                    F = randform(N, R, rnd, BOX)
                elif kind == 'det':
                    F = det_point(N, R, rnd, BOX)
                else:
                    F = pad_per_point(3, R, rnd, BOX, 1)
                t0 = time.time()
                rk = [macaulay_rank(F, N, d, R, p) for p in PRIMES]
                tag = ''
                if kind != 'smooth' and all(x < rho for x in rk):
                    tag = ' *DROP*'
                    first.setdefault(kind, d)
                if kind == 'smooth' and any(x != rho for x in rk):
                    tag = ' *CONTROL FAILS*'
                print(f"{d:3d} {rows:6d} {cols:6d} {h_smooth(d,N,R):5d} {rho:6d} {ceil:6d} "
                      f"{kind:>8} {t:2d} {rk[0]:8d} {rk[1]:8d} {cols-rk[0]:7d} "
                      f"{rho-rk[0]:6d}{tag}  [{time.time()-t0:.1f}s]")
        sys.stdout.flush()
    print()
    for kind in ('det', 'pad'):
        if kind in first:
            d = first[kind]
            print(f"first strict drop, {kind}: d = {d}, rho_d = {rho_generic(d,N,R)}")
        else:
            print(f"first strict drop, {kind}: none in d = {DMIN}..{DMAX}")


if __name__ == '__main__':
    t0 = time.time()
    run()
    print(f"[s44 ladder] done in {time.time()-t0:.1f}s")
