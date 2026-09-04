#!/usr/bin/env python3
"""
Session 48, target B -- the discriminating rank at (n, r) = (5, 7), d = 3n-5 = 10.

Session 44 measured the drop at d = 3n-5 to be 0, 1, 6 at r = 4, 5, 6 across
n = 3, 4, 5, and proposed C(r,5) = 0, 1, 6, 21.  But (r-4)(2r-9) fits the same
three points and gives 15 at r = 7.  (5, 7) is the one ladder case that is
neither ceiling-limited nor already measured, so it discriminates.

Protocol (PREREG_s48 B2): the random-quintic control must return rho_d at both
house primes BEFORE any determinantal rank is read.  A rank mod p at a point is
a LOWER bound on the generic rank, so a drop is certified, never proved, here.

usage: wk9_s48_ladder57.py [d] [nseeds]
"""
import sys, os, time, random, gc
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from wk9_s44_poly import (P1, P2, PRIMES, dim_sym, h_smooth, rho_generic, H_GN,
                          monos, mono_index, pderiv, rand_pencil, pencil_entries,
                          det_form, randform)
from flint import nmod_mat
from math import comb

N, R = 5, 7
D = int(sys.argv[1]) if len(sys.argv) > 1 else 10
NSEEDS = int(sys.argv[2]) if len(sys.argv) > 2 else 3
BOX = 10 ** 6


def macaulay_rank_lean(F, n, d, r, p):
    """rank of M_d(F) building the nmod_mat entrywise -- never materialises a
    dense python list of nrows*ncols ints (51.8M at (5,7,10))."""
    idx = mono_index(d, r)
    mult = monos(d - n + 1, r)
    nc, nr = len(idx), r * len(mult)
    A = nmod_mat(nr, nc, p)
    i = 0
    for k in range(r):
        g = [(e, c % p) for e, c in pderiv(F, k).items() if c % p]
        for m in mult:
            for e, c in g:
                A[i, idx[tuple(x + y for x, y in zip(e, m))]] = c
            i += 1
    rk = A.rank()
    del A; gc.collect()
    return rk, nr, nc


def main():
    dimS, h, rho = dim_sym(D, R), h_smooth(D, N, R), rho_generic(D, N, R)
    ceil_ = dimS - H_GN(D, N, R)
    print(f"# s48 target B -- (n,r,d) = ({N},{R},{D})", flush=True)
    print(f"# dim S_{D} = {dimS}   h_{D} = {h}   rho_{D} = {rho}", flush=True)
    print(f"# GN ceiling dim J(M)_{D} = {ceil_}   slack over rho = {ceil_ - rho}"
          f"   -> ceiling {'BINDS' if ceil_ < rho else 'does not bind'}", flush=True)
    print(f"# rows = {R} * dim S_{D-N+1} = {R * dim_sym(D-N+1, R)}   cols = {dimS}", flush=True)
    print(f"# C(7,5) = {comb(7,5)} predicts rank {rho - comb(7,5)};"
          f"  (r-4)(2r-9) = 15 predicts rank {rho - 15}", flush=True)

    # ---- Phase 1: random-quintic control (must hit rho before anything else)
    ok = True
    for sd in range(NSEEDS):
        rnd = random.Random(70000 + sd)
        F = randform(N, R, rnd, BOX)
        for p in PRIMES:
            t = time.time()
            rk, nr, nc = macaulay_rank_lean(F, N, D, R, p)
            good = (rk == rho)
            ok &= good
            print(f"control  seed={sd} p={p}  {nr}x{nc}  rank={rk}  rho={rho}  "
                  f"{'OK' if good else 'FAIL'}  {time.time()-t:.1f}s", flush=True)
    if not ok:
        print("# CONTROL FAILED -- determinantal ranks not read (PREREG B2)", flush=True)
        return
    print("# control passed at every seed and prime; reading determinantal ranks", flush=True)

    # ---- Phase 2: determinantal pencils
    for sd in range(NSEEDS):
        rnd = random.Random(80000 + sd)
        A = rand_pencil(N, R, rnd, BOX)
        F = det_form(pencil_entries(A, N, R), N)
        for p in PRIMES:
            t = time.time()
            rk, nr, nc = macaulay_rank_lean(F, N, D, R, p)
            print(f"det      seed={sd} p={p}  {nr}x{nc}  rank={rk}  rho={rho}  "
                  f"drop={rho - rk}  {time.time()-t:.1f}s", flush=True)


if __name__ == "__main__":
    main()
