#!/usr/bin/env python3
"""
Session 55, measurement M1.  The Landsberg-Manivel-Ressayre weight arithmetic,
re-derived rather than quoted.

LMR (arXiv:1004.4802, Comment. Math. Helv. 88 (2013) 469-484) Theorem 2.3.1:
Dual_{k,d,N} subset P(S^d C^N) -- the degree-d hypersurfaces in P^{N-1} whose
dual variety has dimension at most k -- carries equations spanning a copy of the
SL_N-module of highest weight

    Omega(k,d) = (d-1)(d-2)(k+2) w_1 + (d(k+2) - 2k - 5) w_2 + 2 w_{k+3},

"of degree (k+2)(d-1)".  The printed Theorem 1.0.2 of the same paper instead says
the module for det_n sits in degree n(n-1), which at n = 4 would be 12.  The two
cannot both be right, and this script decides which by an internal consistency
check that uses nothing but the highest weight:

    an equation of degree delta on S^d C^N is an element of S^delta(S^d C^N),
    so every irreducible summand has |lambda| = delta * d.

Hence delta = |lambda(k,d)| / d, computed from Omega(k,d) alone.

Exact integer arithmetic; the (k,d) identity is verified symbolically in sympy.
"""

import sympy as sp

k, d = sp.symbols('k d', integer=True, positive=True)


def partition_from_fundamental(coeffs, length):
    """lambda_i - lambda_{i+1} = coeffs[i] (1-indexed fundamental weights)."""
    lam = [0] * length
    for i in range(length - 1, -1, -1):
        lam[i] = coeffs.get(i + 1, 0) + (lam[i + 1] if i + 1 < length else 0)
    return lam


def omega_partition(kk, dd):
    """lambda(k,d) as an explicit partition, from Omega(k,d)."""
    a1 = (dd - 1) * (dd - 2) * (kk + 2)
    a2 = dd * (kk + 2) - 2 * kk - 5
    coeffs = {1: a1, 2: a2, kk + 3: 2}
    return partition_from_fundamental(coeffs, kk + 3)


# ---------------------------------------------------------------- symbolic
# lambda_1 = a1 + a2 + 2, lambda_2 = a2 + 2, lambda_3..lambda_{k+3} = 2.
a1 = (d - 1) * (d - 2) * (k + 2)
a2 = d * (k + 2) - 2 * k - 5
size = sp.expand((a1 + a2 + 2) + (a2 + 2) + 2 * (k + 1))
delta = sp.simplify(sp.cancel(size / d))

print("SYMBOLIC")
print("  a_1 = (d-1)(d-2)(k+2)          =", sp.factor(a1))
print("  a_2 = d(k+2) - 2k - 5          =", sp.expand(a2))
print("  |lambda(k,d)| = a1 + 2a2 + 2k + 6 =", sp.factor(size))
print("  |lambda| / d                   =", sp.factor(delta))
assert sp.simplify(size - (k + 2) * d * (d - 1)) == 0
assert sp.simplify(delta - (k + 2) * (d - 1)) == 0
print("  CHECK  |lambda| = (k+2) d (d-1) and delta = (k+2)(d-1): PASS")
print("  ell(lambda) = k+3 (the last nonzero part is the 2 at position k+3)")
print()

# ---------------------------------------------------------------- instances
print("INSTANCES  (det_n: hypersurface of degree d = n in N = n^2 variables,")
print("            dual variety of dimension k = 2n-2)")
print()
hdr = "  n    k   d   lambda                                    |lambda|  delta  ell"
print(hdr)
print("  " + "-" * (len(hdr) - 2))
for n in (2, 3, 4, 5, 6):
    kk, dd = 2 * n - 2, n
    lam = omega_partition(kk, dd)
    s = sum(lam)
    dl, rem = divmod(s, dd)
    assert rem == 0, (n, s, dd)
    assert dl == (kk + 2) * (dd - 1)
    # compact partition string
    out, i = [], 0
    while i < len(lam):
        j = i
        while j + 1 < len(lam) and lam[j + 1] == lam[i]:
            j += 1
        out.append(f"{lam[i]}^{j-i+1}" if j > i else f"{lam[i]}")
        i = j + 1
    print(f"  {n}   {kk:2d}   {dd}   ({', '.join(out)})"
          f"{'':<{max(0, 40 - len(', '.join(out)))}}{s:6d}  {dl:5d}  {len(lam):3d}")
print()

# the two published instances
lam3 = omega_partition(4, 3)
lam4 = omega_partition(6, 4)
print("  LMR's own n = 3 instance : lambda =", lam3,
      "  |lambda| =", sum(lam3), " delta =", sum(lam3) // 3)
assert lam3 == [19, 7, 2, 2, 2, 2, 2], lam3
assert sum(lam3) == 36 and sum(lam3) // 3 == 12
print("    matches the paper's (19, 7, 2^5) at delta = 12: PASS")
print("  our n = 4 instance       : lambda =", lam4,
      "  |lambda| =", sum(lam4), " delta =", sum(lam4) // 4)
assert lam4 == [65, 17, 2, 2, 2, 2, 2, 2, 2], lam4
assert sum(lam4) == 96 and sum(lam4) // 4 == 24
print("    matches the repository reading (65, 17, 2^7) at delta = 24: PASS")
print()

print("VERDICT")
print("  degree = (k+2)(d-1); at n = 4 this is 2n(n-1) = 24, NOT n(n-1) = 12.")
print("  The printed Theorem 1.0.2 degree n(n-1) is inconsistent with the")
print("  highest weight printed in the same theorem; Theorem 2.3.1 and")
print("  Landsberg's survey (Thm 4.2, 'of degree 2n(n-1)') agree with 24.")
print()
print("  ell(lambda(6,4)) = 9, so S_lambda C^r = 0 for r <= 8: the LMR module")
print("  is identically zero on Sym^4 C^r for r <= 8, and gives no equation at")
print("  all for D_r with r <= 8.  Geometrically forced: a hypersurface in")
print("  P^{r-1} has dual of dimension at most r-2, so 'dual dim <= 6' is")
print("  vacuous unless r >= 9.")
