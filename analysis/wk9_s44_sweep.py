#!/usr/bin/env python3
"""
Session 44, Phase 4.4 -- the first-drop degree and the size of the drop across
(n, r).  For each (n, r) walk d upward from n-1 and report the first d at which
det_n(sum_{i=1}^{r} s_i A_i) has rank M_d < rho_d, with the corank, together
with the Gulliksen-Negard forced degree (the smallest d with h_d < H_GN(d),
which proves a drop without computation).

usage: wk9_s44_sweep.py [seed] [trials] [maxcols]
"""
import sys, os, random, time
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from wk9_s44_poly import *

SEED = int(sys.argv[1]) if len(sys.argv) > 1 else 20260903
TRIALS = int(sys.argv[2]) if len(sys.argv) > 2 else 2
MAXCOLS = int(sys.argv[3]) if len(sys.argv) > 3 else 3500
BOX = 10 ** 6


def forced_degree(n, r, dmax=30):
    for d in range(n - 1, dmax):
        if h_smooth(d, n, r) < H_GN(d, n, r):
            return d
    return None


def first_drop(n, r):
    """smallest d with a strict drop at every trial, both primes; None if not found."""
    for d in range(n - 1, 4 * n):
        cols = dim_sym(d, r); rows = r * dim_sym(d - n + 1, r)
        if cols > MAXCOLS or rows > 4 * MAXCOLS:
            return ('too big', d, cols, rows, None, None)
        rho = rho_generic(d, n, r)
        # control
        rnd = random.Random(SEED + 31 * n + 17 * r + d)
        Fs = randform(n, r, rnd, BOX)
        ctl = [macaulay_rank(Fs, n, d, r, p) for p in PRIMES]
        if any(x != rho for x in ctl):
            return ('control fails', d, cols, rows, ctl, rho)
        ranks = []
        for t in range(TRIALS):
            rnd = random.Random(SEED + 1000003 * t + 31 * n + 17 * r + d)
            F = det_point(n, r, rnd, BOX)
            ranks += [macaulay_rank(F, n, d, r, p) for p in PRIMES]
        if all(x < rho for x in ranks):
            if len(set(ranks)) != 1:
                return ('inconsistent', d, cols, rows, ranks, rho)
            return ('drop', d, cols, rows, ranks[0], rho)
        if any(x < rho for x in ranks):
            return ('inconsistent', d, cols, rows, ranks, rho)
    return ('none', None, None, None, None, None)


if __name__ == '__main__':
    t0 = time.time()
    print(f"[s44 sweep] seed {SEED}, {TRIALS} det trials, maxcols {MAXCOLS}, primes {PRIMES}")
    print(f"{'n':>2} {'r':>2} | {'d*':>3} {'rho_d*':>7} {'rank':>6} {'drop':>5} "
          f"{'corank':>7} {'h_d*':>5} | {'GN forced d':>11} {'rho at forced':>13} | status")
    for n in (3, 4, 5):
        for r in (5, 6, 7, 8):
            st, d, cols, rows, rk, rho = first_drop(n, r)
            fd = forced_degree(n, r)
            frho = rho_generic(fd, n, r) if fd else None
            if st == 'drop':
                print(f"{n:2d} {r:2d} | {d:3d} {rho:7d} {rk:6d} {rho-rk:5d} {cols-rk:7d} "
                      f"{h_smooth(d,n,r):5d} | {fd:11d} {frho:13d} | drop")
            else:
                print(f"{n:2d} {r:2d} | {'-':>3} {'-':>7} {'-':>6} {'-':>5} {'-':>7} {'-':>5} | "
                      f"{fd if fd else '-':>11} {frho if frho else '-':>13} | {st} at d={d} "
                      f"(cols {cols}, rows {rows}, ranks {rk}, rho {rho})")
            sys.stdout.flush()
    print(f"[s44 sweep] done in {time.time()-t0:.1f}s")
