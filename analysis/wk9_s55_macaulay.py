#!/usr/bin/env python3
"""
Session 55: re-derivation of the Macaulay-minor rows of the census.

The construction.  For F of degree n in r variables, M_d(F) has rows the
degree-(d-3) multiples of the r partials (each of degree n-1 = 3) and columns
the monomials of degree d.  For a SMOOTH hypersurface the partials are a regular
sequence, so

    dim (S/J_F)_d  =  h_d  =  [t^d] ((1 - t^{n-1})/(1 - t))^r  =  [t^d](1+t+t^2)^r

and the generic rank is rho_d = dim Sym^d C^r - h_d.  On D_r the corank is
larger by the measured drop, so the determinantal rank is rho_d - drop, and

    smallest minor that vanishes on D_r  =  (determinantal rank) + 1
                                         =  rho_d - drop + 1,

which is also its degree in the coefficients of F (entries of M_d are linear
in F).  Quoting rho_d itself -- the generic rank -- is the slip s49 corrects.

Everything below is integer arithmetic.
"""

from math import comb


def hilb_smooth(r, d, n=4):
    """[t^d] ((1-t^{n-1})/(1-t))^r  = [t^d] (1 + t + ... + t^{n-2})^r."""
    poly = [1]
    unit = [1] * (n - 1)
    for _ in range(r):
        new = [0] * (len(poly) + len(unit) - 1)
        for i, a in enumerate(poly):
            for j, b in enumerate(unit):
                new[i + j] += a * b
        poly = new
    return poly[d] if d < len(poly) else 0


print("n = 4, d = 3n - 5 = 7 unless stated")
print()
print("  r   d   dim Sym^d C^r   h_d   rho_d   drop   det rank   minor size = degree")
rows = [
    (5, 7, 1,  "drop = C(5,5) = 1;  measured (R/J)_7 = 31 vs 30"),
    (6, 7, 6,  "drop = C(6,5) = 6;  certified"),
    (6, 8, 50, "d = 8; drop 50 is BACK-SOLVED from the repository's 1148, NOT re-derived here"),
    (7, 10, 21, "the (n,r) = (5,7) consistency row is at n = 5; shown for shape only"),
]
for (r, d, drop, note) in rows[:3]:
    N = comb(d + r - 1, r - 1)
    h = hilb_smooth(r, d)
    rho = N - h
    detrank = rho - drop
    print(f"  {r}   {d}   {N:13d}   {h:3d}   {rho:5d}   {drop:4d}   {detrank:8d}"
          f"   {detrank + 1:6d}     ({note})")
print()
print("  So: r = 5 -> 300, r = 6 -> 661 at d = 7 and 1148 at d = 8.")
print("  HONEST BOUNDARY: rho_d and dim Sym^d C^r are re-derived here; the drops")
print("  are not.  drop = C(r,5) = 6 at (r,d) = (6,7) is the repository's measured")
print("  value and matches; the d = 8 drop of 50 is back-solved from the quoted")
print("  1148 and is NOT independently checked by this session.")
print("  The two numbers the brief quotes as '661 certified, 1148 proved' and")
print("  '300' are reproduced.  Note the r = 5 value is unchanged by the s49")
print("  correction only because rho_7 - drop + 1 = 300 - 1 + 1 = 300 there;")
print("  the coincidence is not a general one (r = 6 moves 666 -> 661).")
print()
print("  The discriminant, for comparison: deg disc(Sym^4 C^r) = r . 3^{r-1}")
for r in range(4, 11):
    print(f"    r = {r:2d}   {r * 3 ** (r - 1):>10d}")
print()
print("  And the LMR module, for comparison: degree 24 for every r >= 9,")
print("  identically zero for r <= 8.")
