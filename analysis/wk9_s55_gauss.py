#!/usr/bin/env python3
"""
Session 55: an independent second route to dim X^*(det_4 pencil) = 6, using no
Hessian at all.

At a point s with rank A(s) = 3, let w span ker A(s) and z^T span the left
kernel.  Then adj A(s) = c . w z^T, and

    dP/ds_a  =  tr(adj A(s) . A_a)  =  c . z^T A_a w ,

so the affine cone over X^* is the image of

    mu : (z, w) |-> [ z^T A_a w ]_{a=1..r}

restricted to the ADMISSIBLE pairs (z,w) -- those for which some s satisfies
A(s)w = 0 and z^T A(s) = 0.  That is 8 linear conditions on s in C^r, so:

  * for r >= 9 a nonzero s exists for EVERY (z,w): admissibility is automatic,
    the Gauss image is the full linear projection of the Segre cone of rank-1
    4x4 matrices, and dim X^* = rank d(mu) - 1 at a general (z,w);
  * for r <= 8 a general (z,w) is NOT admissible, so the unconstrained Jacobian
    computes the projection of the whole Segre and is only an UPPER bound on the
    Gauss image.  The route says nothing there and this script does not use it.

The r >= 9 range is exactly where the LMR module is non-vacuous, which is the
range the census needs.  Exact arithmetic; rank over Q and mod two primes.
"""

import random
from fractions import Fraction

from flint import fmpq_mat, nmod_mat, fmpq

PRIMES = (2147483647, 1000003)

print("valid range (admissibility automatic): r >= 9")
print()
print("  r   rank d(mu) (Q)   mod p1   mod p2   dim cone X^*   dim X^*   "
      "Hessian route (wk9_s55_ranks2)")
HESS = {9: 6, 10: 6, 11: 6, 12: 6}
ok = True
for r in range(9, 13):
    vals = []
    for seed in (1, 2, 3):
        rng = random.Random(9100 + 17 * r + seed)
        A = [[[Fraction(rng.randint(-6, 6)) for _ in range(4)]
              for _ in range(4)] for _ in range(r)]
        z = [Fraction(rng.randint(-7, 7)) for _ in range(4)]
        w = [Fraction(rng.randint(-7, 7)) for _ in range(4)]
        rows = []
        for a in range(r):
            M = A[a]
            for i in range(4):                       # d/dz_i = (A_a w)_i
                rows.append(sum(M[i][j] * w[j] for j in range(4)))
            for j in range(4):                       # d/dw_j = (z^T A_a)_j
                rows.append(sum(z[i] * M[i][j] for i in range(4)))
        rQ = fmpq_mat(r, 8, [fmpq(c.numerator, c.denominator)
                             for c in rows]).rank()
        rp = [nmod_mat(r, 8,
                       [((c.numerator % p) * pow(c.denominator % p, p - 2, p)) % p
                        for c in rows], p).rank() for p in PRIMES]
        assert all(t == rQ for t in rp), (r, seed, rQ, rp)
        vals.append((rQ, rp))
    rQ = max(v[0] for v in vals)
    rp = [max(v[1][i] for v in vals) for i in (0, 1)]
    agree = (rQ - 1) == HESS[r]
    ok = ok and agree
    print(f"  {r:2d}   {rQ:13d}   {rp[0]:6d}   {rp[1]:6d}   {rQ:12d}   {rQ-1:7d}"
          f"   {HESS[r]:14d}   {'agree' if agree else 'DISAGREE'}")
assert ok, "the two routes disagree"
print()
print("  The two routes agree at every r in the valid range.  The Jacobian has")
print("  only 8 columns, so the rank saturates at 7 and dim X^* at 6 = 2n-2 --")
print("  because the Gauss image is a linear projection of the 6-dimensional")
print("  Segre variety of rank-1 4x4 matrices.  That is the geometric reason")
print("  k = 6 cannot be lowered: it is the dual dimension of det_4 itself, and")
print("  once r >= 9 the projection is generically finite so no linear section")
print("  makes it smaller.")
print()
print("  NOTE the Hessian-route column is quoted from results/logs/s55_ranks2.log")
print("  and asserted against, not recomputed here.")
