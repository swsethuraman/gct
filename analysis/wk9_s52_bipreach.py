#!/usr/bin/env python3
"""
Session 52, Task 0 -- the reach of the Buergisser-Ikenmeyer-Panova machinery as
a function of n, evaluated at n = 4.

Nothing here is a re-derivation of BIP.  Every hypothesis below is transcribed
from the paper (arXiv:1604.06431; v3 numbering, with the v1/authors'-copy
numbering in brackets) and this script only evaluates those hypotheses at small
n, which the paper never does.

  Thm 2.5  [Thm 2.8]   n >= s*k  =>  X^(n-s) (phi_1^s + ... + phi_k^s) in Omega_n
  Prop 2.3             n >= k*l, l even  =>  (k x l)^{#nk} occurs in C[Omega_n]_k
                       (the weight is a body of k rows of length l, plus a first
                       row, so ell(lam) = k+1)
  Lemma 2.2            semigroup: lam, lam' occur => lam + lam' occurs
  Prop 2.4 [Prop 5.1]  |lam-bar| <= m d and m d^2 <= n  =>  every HWV of weight
                       lam in Sym^d Sym^n V is non-vanishing on Omega_n
  Prop 5.2             ell(lam) <= m^2, lam_2 <= s, m^2 s^2 <= n, m^2 s <= d
                       =>  every nonzero HWV of weight lam non-vanishing on Omega_n
  Prop 5.5             ell(lam) <= m^2, m^10 <= |lam-bar| <= m d, n >= 24 m^6,
                       d > 4 m^6  =>  lam occurs in C[Omega_n]_d

`m` in Props 2.4/5.2/5.5 is a free auxiliary parameter, not the permanent size;
the script optimises over it, which is the generous reading.

usage: python3 wk9_s52_bipreach.py [--n 4] [--dmax 12]
"""
import sys, json


def thm25_points(n):
    """(s, k, support bound) for every padded power sum Thm 2.5 supplies at
    this n.  The point is X^(n-s)(phi_1^s + ... + phi_k^s); its linear span is
    <= k+1 forms, and for s = 1 the sum collapses to a single form, so the
    span is <= 2 there."""
    out = []
    for s in range(1, n + 1):
        for k in range(1, n // s + 1):
            if s * k > n: continue
            span = 2 if s == 1 else (k + 1 if s < n else 1)
            if s == n: span = 1 if n - s == 0 else 2
            out.append((s, k, span))
    return out


def prop23_lengths(n):
    """ell(lam) = k+1 for every (k, l) with n >= k*l and l even."""
    out = []
    for l in range(2, n + 1, 2):
        for k in range(1, n // l + 1):
            out.append((k, l, k + 1))
    return out


def prop24_ok(n, d):
    """is there a free m >= 1 with m d^2 <= n?  returns the largest such m
    (0 if none), which also caps |lam-bar| <= m d."""
    return n // (d * d)


def prop52_reach(n):
    """best (m, s): maximise the length reach m^2 subject to m^2 s^2 <= n,
    remembering lam_2 <= s and d >= m^2 s."""
    best = []
    m = 1
    while m * m <= n:
        s = 1
        while m * m * s * s <= n:
            best.append(dict(m=m, s=s, ell_max=m * m, lam2_max=s, d_min=m * m * s))
            s += 1
        m += 1
    return best


def prop55_ok(n):
    return [m for m in range(2, 40) if n >= 24 * m ** 6]


def least_n_for(ell, lam2):
    """least n at which some BIP tool can reach a weight with this length and
    this lam_2, over the three propositions.  Prop 5.2 needs m^2 >= ell and
    m^2 s^2 <= n with s >= lam_2, so n >= ell_ceil * lam2^2 where ell_ceil is
    the least square >= ell.  Prop 2.3 + semigroup reaches length k+1 with
    n >= k*l >= 2k, so n >= 2(ell-1) but only for bodies that are sums of even
    rectangles.  Prop 5.5 needs n >= 24 m^6 with m^2 >= ell."""
    sq = 1
    while sq * sq < ell: sq += 1
    p52 = sq * sq * lam2 * lam2
    p23 = 2 * (ell - 1)
    p55 = 24 * sq ** 6
    return dict(prop52=p52, prop23=p23, prop55=p55, best=min(p52, p23, p55))


if __name__ == '__main__':
    n = int(sys.argv[sys.argv.index('--n') + 1]) if '--n' in sys.argv else 4
    dmax = int(sys.argv[sys.argv.index('--dmax') + 1]) if '--dmax' in sys.argv else 12
    print(f"=== BIP machinery at n = {n} ===\n")

    P = thm25_points(n)
    print(f"Thm 2.5 padded power sums, n >= s*k:  {len(P)} shapes")
    for s, k, span in P:
        print(f"   s={s} k={k}   X^{n-s}(phi_1^{s} + ... + phi_{k}^{s})   linear span <= {span}")
    print(f"   MAX LINEAR SPAN = {max(x[2] for x in P)}\n")

    L = prop23_lengths(n)
    print(f"Prop 2.3 row-extended even rectangles, n >= k*l, l even:  {len(L)} shapes")
    for k, l, e in L:
        print(f"   k={k} l={l}   ell(lam) = {e}")
    print(f"   MAX ell(lam) = {max(x[2] for x in L)}   (semigroup sums preserve this)\n")

    print("Prop 2.4 [5.1] small degrees, need m*d^2 <= n:")
    for d in range(1, dmax + 1):
        mm = prop24_ok(n, d)
        print(f"   d={d:2d}  largest admissible m = {mm}"
              + ("   -- VACUOUS (no m >= 1)" if mm == 0 else f"   (then |lam-bar| <= {mm*d})"))
    print()

    R = prop52_reach(n)
    print("Prop 5.2 extremely long first rows, need m^2 s^2 <= n:")
    for r in R:
        print(f"   m={r['m']} s={r['s']}   ell(lam) <= {r['ell_max']}, lam_2 <= {r['lam2_max']}, d >= {r['d_min']}")
    print(f"   MAX ell(lam) = {max(r['ell_max'] for r in R)}\n")

    print(f"Prop 5.5 splitting, need n >= 24 m^6 (m >= 2):  admissible m = {prop55_ok(n)}"
          + ("   -- VACUOUS" if not prop55_ok(n) else "") + "\n")

    print("Least n at which some BIP tool reaches a weight of length ell with lam_2 = L:")
    print("  ell  L   Prop5.2   Prop2.3   Prop5.5    best")
    for ell in (3, 4, 5, 6):
        for L in (1, 2, 4, 8):
            v = least_n_for(ell, L)
            print(f"  {ell:3d} {L:2d}   {v['prop52']:7d}   {v['prop23']:7d}   {v['prop55']:7d}   {v['best']:5d}")
