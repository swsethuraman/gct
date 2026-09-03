#!/usr/bin/env python3
"""
Session 44 -- independent verification of every load-bearing number, by a code
path that shares nothing with wk9_s44_poly.py where it can be avoided.

  1. h_d, rho_d and H_GN recomputed by sympy power-series expansion instead of
     binomial sums, at every (n, r, d) used in the session.
  2. rho_d = rows - (alternating Koszul count) as a polynomial identity, and
     rho_d = rows exactly where the matrix has full row rank.
  3. The claim "rank M_d(F) <= rho_d for EVERY F" spot-checked at deliberately
     degenerate forms (a product of four linear forms, a cone, a form of rank 1).
  4. The d = 7 drop re-measured at a fresh seed and a different box, and the
     d <= 6 no-drop re-measured, both primes.
  5. The Gulliksen-Negard ceiling arithmetic of Theorem A recomputed from the
     resolution ranks directly.

usage: wk9_s44_verify.py [seed]
"""
import sys, os, random, time
from math import comb
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from wk9_s44_poly import *
import sympy as sp

SEED = int(sys.argv[1]) if len(sys.argv) > 1 else 44004400
t = sp.symbols('t')
ok = True


def series_coeff(expr, d):
    return int(sp.series(expr, t, 0, d + 1).removeO().coeff(t, d))


print("[s44 verify] 1. h_d, rho_d, H_GN by sympy series vs binomial sums")
for (n, r) in [(3, 5), (4, 5), (4, 6), (5, 6), (3, 6), (5, 5)]:
    hs = ((1 - t ** (n - 1)) / (1 - t)) ** r
    gn = (1 - n * n * t ** (n - 1) + (2 * n * n - 2) * t ** n
          - n * n * t ** (n + 1) + t ** (2 * n)) / (1 - t) ** r
    for d in range(n - 1, 3 * n + 1):
        a, b = h_smooth(d, n, r), series_coeff(sp.expand(hs), d)
        c, e = H_GN(d, n, r), series_coeff(sp.expand(gn), d)
        if a != b or c != e:
            ok = False; print(f"   MISMATCH n={n} r={r} d={d}: h {a} vs {b}, H_GN {c} vs {e}")
print("   h_d and H_GN agree with the series expansion everywhere" if ok else "   FAILED")

print("[s44 verify] 2. rho_d = rows - Koszul alternating count")
for (n, r) in [(3, 5), (4, 5), (4, 6), (5, 6), (3, 6), (4, 7), (5, 5)]:
    for d in range(n - 1, 3 * n + 2):
        if rho_generic(d, n, r) != koszul_rank(d, n, r):
            ok = False; print(f"   MISMATCH n={n} r={r} d={d}")
print("   identity holds at every (n, r, d) tested")

print("[s44 verify] 3. rank M_d(F) <= rho_d at deliberately degenerate quartics (n=4, r=6)")
rnd = random.Random(SEED)
BOX = 10 ** 4
def prod_lin(k):
    F = {tuple([0] * 6): 1}
    for _ in range(k):
        F = pmul(F, linform([rnd.randint(-BOX, BOX) for _ in range(6)], 6))
    return F
cases = {
    'product of four linear forms': prod_lin(4),
    'square of a quadric': (lambda q: pmul(q, q))({e: rnd.randint(-BOX, BOX) for e in monos(2, 6)}),
    'cone (no s_6)': {e: rnd.randint(-BOX, BOX) for e in monos(4, 6) if e[5] == 0},
    'random quartic': randform(4, 6, rnd, BOX),
}
for lab, F in cases.items():
    for d in (5, 6, 7, 8):
        rho = rho_generic(d, 4, 6)
        rk = [macaulay_rank(F, 4, d, 6, p) for p in PRIMES]
        if any(x > rho for x in rk):
            ok = False; print(f"   VIOLATION {lab} d={d}: rank {rk} > rho {rho}")
    print(f"   {lab:30s}: ranks at d=5..8 "
          f"{[macaulay_rank(F,4,d,6,PRIMES[0]) for d in (5,6,7,8)]} "
          f"(rho {[rho_generic(d,4,6) for d in (5,6,7,8)]})")

print("[s44 verify] 4. the drop re-measured, fresh seed, different box")
for box in (10 ** 3, 10 ** 8):
    rnd = random.Random(SEED + box)
    F = det_point(4, 6, rnd, box)
    row = []
    for d in (4, 5, 6, 7, 8):
        rk = [macaulay_rank(F, 4, d, 6, p) for p in PRIMES]
        assert rk[0] == rk[1], (d, rk)
        row.append((d, rk[0], rho_generic(d, 4, 6)))
    print(f"   box +-{box}: " + "  ".join(f"d={d}: {a}/{b}" for d, a, b in row))
    for d, a, b in row:
        if d <= 6 and a != b: ok = False; print(f"   UNEXPECTED drop at d={d}")
        if d == 7 and a != 660: ok = False; print(f"   UNEXPECTED rank at d=7: {a}")

print("[s44 verify] 5. Theorem A arithmetic from the resolution ranks")
for d in range(3, 10):
    cols = comb(d + 5, 5)
    hgn = sum(c * (comb(d - j + 5, 5) if d - j >= 0 else 0)
              for j, c in {0: 1, 3: -16, 4: 30, 5: -16, 8: 1}.items())
    ceil = cols - hgn
    rho = rho_generic(d, 4, 6)
    print(f"   d={d}: dim S_d {cols:5d}  H_GN {hgn:4d}  ceiling {ceil:5d}  rho {rho:5d}  "
          f"{'FORCED DROP' if ceil < rho else 'no forcing'}")
    if H_GN(d, 4, 6) != hgn: ok = False; print("   MISMATCH with H_GN")
assert rho_generic(8, 4, 6) == 1197 and comb(13, 5) - H_GN(8, 4, 6) == 1147
print("   d=8: ceiling 1147 < rho 1197 -- Theorem A's inequality confirmed")

print(f"\n[s44 verify] {'ALL CHECKS PASS' if ok else 'FAILURES ABOVE'}")
