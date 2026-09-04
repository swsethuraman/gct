#!/usr/bin/env python3
"""
Session 44, Phase 1 -- validate the mechanism at the two anchors.

  (n, r, d) = (3, 5, 4): generic rank 65  (= paper 1's delta_0 <= 65)
  (n, r, d) = (4, 5, 7): generic rank 300 (= cap(4) of the five-row theorem)

For each: several random integer forms (expect rank == rho_d exactly, which is
simultaneously the check of h_d = [t^d]((1-t^{n-1})/(1-t))^r) and several
det_n(sum s_i A_i) points (expect rank < rho_d).  Both house primes.

Also checks rho_d = dim Sym^d - h_d against a direct rank at several (n,r,d)
away from the anchors, so the formula is not taken on trust.

usage: wk9_s44_anchor.py [seed] [trials]
"""
import sys, os, random, time
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from wk9_s44_poly import *

SEED = int(sys.argv[1]) if len(sys.argv) > 1 else 20260903
TRIALS = int(sys.argv[2]) if len(sys.argv) > 2 else 3
BOX = 10 ** 6


def measure(F, n, d, r):
    return [macaulay_rank(F, n, d, r, p) for p in PRIMES]


def anchor(n, r, d, label):
    rho = rho_generic(d, n, r)
    rows = r * dim_sym(d - n + 1, r); cols = dim_sym(d, r)
    print(f"\n=== anchor {label}: n={n} r={r} d={d} | rows {rows} cols {cols} "
          f"h_d {h_smooth(d,n,r)} rho {rho} ===")
    ok = True
    for t in range(TRIALS):
        rnd = random.Random(SEED + 1000 * t + 7 * n + r)
        F = randform(n, r, rnd, BOX)
        rk = measure(F, n, d, r)
        flag = "OK" if all(x == rho for x in rk) else "MISMATCH"
        ok &= all(x == rho for x in rk)
        print(f"  smooth  trial {t}: rank {rk}  (expect {rho})  {flag}")
    for t in range(TRIALS):
        rnd = random.Random(SEED + 5000 * t + 13 * n + r)
        F = det_point(n, r, rnd, BOX)
        rk = measure(F, n, d, r)
        drop = [rho - x for x in rk]
        flag = "DROP" if all(x < rho for x in rk) else "NO DROP"
        ok &= all(x < rho for x in rk)
        print(f"  det     trial {t}: rank {rk}  corank {[cols-x for x in rk]}  "
              f"drop {drop}  {flag}")
    print(f"  anchor {label}: {'PASS' if ok else 'FAIL'}")
    return ok


def formula_check():
    print("\n=== rho_d = dim Sym^d - h_d, checked by direct rank at random forms ===")
    cases = [(3, 4, 3), (3, 4, 4), (3, 5, 3), (3, 5, 5), (4, 4, 5), (4, 4, 6),
             (4, 5, 5), (4, 5, 6), (4, 6, 4), (4, 6, 5), (5, 4, 8), (3, 6, 3)]
    ok = True
    for (n, r, d) in cases:
        rnd = random.Random(SEED + 91 * n + 7 * r + d)
        F = randform(n, r, rnd, BOX)
        rho = rho_generic(d, n, r)
        rk = measure(F, n, d, r)
        good = all(x == rho for x in rk)
        ok &= good
        print(f"  n={n} r={r} d={d}: dimS={dim_sym(d,r):5d} h={h_smooth(d,n,r):5d} "
              f"rho={rho:5d} measured {rk}  {'OK' if good else 'MISMATCH'}")
    print(f"  formula check: {'PASS' if ok else 'FAIL'}")
    return ok


if __name__ == '__main__':
    t0 = time.time()
    print(f"[s44 anchors] seed {SEED}, {TRIALS} trials, box +-{BOX}, primes {PRIMES}")
    a = formula_check()
    b = anchor(3, 5, 4, "A (cubic in 5 vars, 65)")
    c = anchor(4, 5, 7, "B (quartic in 5 vars, 300)")
    print(f"\n[s44 anchors] {'ALL PASS' if (a and b and c) else 'FAILURE'} "
          f"in {time.time()-t0:.1f}s")
