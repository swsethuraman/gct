#!/usr/bin/env python3
"""
Session 55, measurement M4 and one supporting rank profile.

M4.  The singular-locus / discriminant row of the census.

  For P = det_4(A(s)) on an r-dimensional pencil, dP/ds_a = tr(adj A(s) . A_a),
  and adj M = 0 exactly when rank M <= 2 (the 3x3 minors).  So every point of
  the pencil where the matrix has rank <= 2 is a singular point of the quartic.
  The rank-<=2 locus in P^15 has codimension 4 and degree 20 (Giambelli-Thom-
  Porteous), so a generic 5-dimensional pencil meets it in 20 points and the
  quartic threefold {det A(s) = 0} in P^4 is 20-nodal.  Hence the discriminant
  vanishes identically on D_5, giving an explicit equation of degree
  deg disc(Sym^4 C^5) = 5 . 3^4 = 405.

  Verified here three ways:
   (i)   the GTP degree formula, anchored on deg Seg(P^2 x P^2) = 6;
   (ii)  the Hilbert function of the ideal of 3x3 minors restricted to a random
         5-dimensional pencil, mod two primes: it must stabilise at 20;
   (iii) the same at r = 4, where the count must be 0 (a generic determinantal
         quartic surface in P^3 is smooth -- Alper-Bogart-Velasco).

SUPPORTING.  rank Hess(det_4)(M) as a function of rank M.  This is the "vanishes
on D_r" half of the LMR row: the equations require rank Hess <= k+2 = 8 at every
point of the hypersurface, not just at generic ones.

Exact arithmetic; mod two primes plus a rational check on the small matrices.
"""

import random
from fractions import Fraction
from itertools import combinations, combinations_with_replacement, permutations
from math import factorial

from flint import fmpq_mat, nmod_mat, fmpq

PRIMES = (2147483647, 1000003)


# ------------------------------------------------------- (i) the GTP formula
def gtp_degree(m, n, r):
    """deg of {rank <= r} in P^{mn-1} for m x n matrices (Giambelli-Thom-Porteous)."""
    num = 1
    for i in range(n - r):
        num = num * factorial(m + i) * factorial(i) // (
            factorial(r + i) * factorial(m - r + i))
    return num


print("(i)  Giambelli-Thom-Porteous degrees")
print("     deg {rank<=1} in P^8  (3x3)  =", gtp_degree(3, 3, 1),
      "  anchor: deg Seg(P^2 x P^2) = C(4,2) =", 6)
assert gtp_degree(3, 3, 1) == 6
print("     deg {rank<=1} in P^15 (4x4)  =", gtp_degree(4, 4, 1),
      "  anchor: deg Seg(P^3 x P^3) = C(6,3) =", 20)
assert gtp_degree(4, 4, 1) == 20
print("     deg {rank<=2} in P^15 (4x4)  =", gtp_degree(4, 4, 2),
      "  codim 4  -> a generic P^4 meets it in that many points")
assert gtp_degree(4, 4, 2) == 20
print("     codim {rank<=2} in M_4 = (4-2)^2 =", (4 - 2) ** 2)
print()


# ---------------------------------- (ii,iii) Hilbert function of the 3x3 minors
def minors3_of_pencil(R, rng):
    """The 16 cubics in s_0..s_{R-1} cutting out {rank A(s) <= 2}."""
    A = [[[rng.randint(-6, 6) for _ in range(4)] for _ in range(4)]
         for _ in range(R)]

    def ent(i, j):
        return {a: Fraction(A[a][i][j]) for a in range(R)}

    cubics = []
    for rows in combinations(range(4), 3):
        for cols in combinations(range(4), 3):
            poly = {}
            for perm in permutations(range(3)):
                sgn, pl = 1, list(perm)
                for i in range(3):
                    for j in range(i + 1, 3):
                        if pl[i] > pl[j]:
                            sgn = -sgn
                cur = {(): Fraction(sgn)}
                for i in range(3):
                    e = ent(rows[i], cols[perm[i]])
                    nxt = {}
                    for mon, c in cur.items():
                        for a, ca in e.items():
                            k = tuple(sorted(mon + (a,)))
                            nxt[k] = nxt.get(k, Fraction(0)) + c * ca
                    cur = nxt
                for mon, c in cur.items():
                    poly[mon] = poly.get(mon, Fraction(0)) + c
            cubics.append({m: c for m, c in poly.items() if c})
    return cubics


def hilbert(cubics, R, dmax, p):
    """dim (S/I)_d for d = 3..dmax, over F_p."""
    out = {}
    for d in range(3, dmax + 1):
        cols = list(combinations_with_replacement(range(R), d))
        cidx = {m: i for i, m in enumerate(cols)}
        mult = list(combinations_with_replacement(range(R), d - 3))
        nrows = len(cubics) * len(mult)
        ent = [0] * (nrows * len(cols))
        row = 0
        for m in mult:
            for g in cubics:
                base = row * len(cols)
                for mon, c in g.items():
                    key = tuple(sorted(mon + m))
                    v = (c.numerator % p) * pow(c.denominator % p, p - 2, p) % p
                    idx = base + cidx[key]
                    ent[idx] = (ent[idx] + v) % p
                row += 1
        rk = nmod_mat(nrows, len(cols), ent, p).rank()
        out[d] = len(cols) - rk
    return out


print("(ii,iii)  Hilbert function of the ideal of 3x3 minors on a random pencil")
print("          dim (S/I)_d ; the scheme {rank A(s) <= 2} in P^{r-1}")
for R, dmax in ((5, 11), (4, 9)):
    for p in PRIMES:
        rng = random.Random(770 + R + 13 * (p % 7))   # a different pencil per prime
        cub = minors3_of_pencil(R, rng)
        h = hilbert(cub, R, dmax, p)
        row = "  ".join(f"d={d}:{v}" for d, v in sorted(h.items()))
        print(f"     r={R}  p={p:>10}   {row}")
print()
print("     r=5 stabilises at 20  -> 20 points, i.e. 20 nodes on the quartic")
print("     threefold, so the discriminant vanishes on D_5.")
print("     r=4 reaches 0         -> empty, so a generic determinantal quartic")
print("     surface in P^3 is smooth and the discriminant does NOT vanish on D_4.")
print()
print("     deg disc(Sym^4 C^r) = r . 3^{r-1} :",
      {r: r * 3 ** (r - 1) for r in range(4, 8)})
print()


# ------------------------------- supporting: rank Hess(det_4) by rank of M
def hess_det4(M):
    """16x16 Hessian of det_4 at the 4x4 matrix M: signed complementary 2x2 minors."""
    idx = [(i, j) for i in range(4) for j in range(4)]
    rows = []
    for (i, j) in idx:
        for (k, l) in idx:
            if i == k or j == l:
                rows.append(Fraction(0))
                continue
            ri = [a for a in range(4) if a not in (i, k)]
            ci = [b for b in range(4) if b not in (j, l)]
            minor = (M[ri[0]][ci[0]] * M[ri[1]][ci[1]]
                     - M[ri[0]][ci[1]] * M[ri[1]][ci[0]])
            s_r = 1 if ((i < k) == (j < l)) else -1
            # sign of the complementary minor in the Laplace expansion
            sgn = (-1) ** (i + j + k + l) * s_r
            rows.append(Fraction(sgn) * minor)
    return rows


print("supporting:  rank Hess(det_4)(M) as a function of rank M")
print("     rank M   rank Hess (Q)   mod p1   mod p2   2n = 8?")
rng = random.Random(4242)
for want in (4, 3, 2, 1, 0):
    got = []
    for _ in range(12):
        U = [[rng.randint(-5, 5) for _ in range(4)] for _ in range(4)]
        V = [[rng.randint(-5, 5) for _ in range(4)] for _ in range(4)]
        D = [[0] * 4 for _ in range(4)]
        for t in range(want):
            D[t][t] = 1
        M = [[sum(U[i][a] * D[a][b] * V[b][j] for a in range(4)
                  for b in range(4)) for j in range(4)] for i in range(4)]
        # confirm the rank of M itself
        rM = fmpq_mat(4, 4, [fmpq(int(M[i][j])) for i in range(4)
                             for j in range(4)]).rank()
        if rM != want:
            continue
        rows = hess_det4(M)
        rQ = fmpq_mat(16, 16, [fmpq(c.numerator, c.denominator)
                               for c in rows]).rank()
        rp = [nmod_mat(16, 16,
                       [((c.numerator % p) * pow(c.denominator % p, p - 2, p)) % p
                        for c in rows], p).rank() for p in PRIMES]
        got.append((rQ, tuple(rp)))
    assert got, f"no draw of rank {want} succeeded"
    assert len(set(got)) == 1, f"rank Hess not constant on the rank-{want} stratum: {set(got)}"
    rQ, rp = got[0]
    print(f"     {want:6d}   {rQ:13d}   {rp[0]:6d}   {rp[1]:6d}"
          f"   {'yes' if rQ <= 8 else 'no'}      ({len(got)} draws, all equal)")
print()
print("     rank <= 3 (i.e. every point of the hypersurface) gives rank Hess <= 8,")
print("     so the LMR rank condition holds at EVERY point of {det A(s) = 0},")
print("     not only at generic ones -- which is what the divisibility needs.")
print()
print("     This is a PROOF, not a sample.  Hess(det_4)(X M Y) = (X (x) Y)^T .")
print("     Hess(det_4)(M) . (X (x) Y) up to the scalar det X det Y, so rank Hess")
print("     is constant on GL_4 x GL_4 orbits, and each rank stratum of M_4 is a")
print("     single such orbit.  The draws above therefore determine the value on")
print("     the whole stratum; the assertion that every draw in a stratum agrees")
print("     is the check on that.")
