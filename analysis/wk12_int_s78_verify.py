#!/usr/bin/env python3
"""Independent verification of session 78's two structural claims.

s78 reports (a) a certified reduction of S2's 149-variable chart job to 98
variables with the f0-saturation removed, and (b) that the ker/coker component's
image has dimension exactly 28 projective, at every contact order.  Neither is
checked here by running s78's code; both are re-derived from scratch on random
points chosen here.

  1. THE GRADING.  det(s5 I4 + sum_{k<=4} s_k B_k) has s5^(4-j) coefficient
     homogeneous of degree j in s1..s4, so the coefficient counts are
     1, 4, 10, 20, 35.  Hence 4 + 10 + 20 = 34 good coordinates and 35 bad ones,
     totalling S2's 69 ratio coordinates exactly, and the W condition y_bad = 0
     is P_4 = 0 -- the 4-pencil spans a space of singular matrices.

  2. THE KER COMPONENT, EXACTLY.  With the kernel vector first,
     B_k = [[0, r_k^T], [0, C_k]], the first column of s5 I4 + sum s_k B_k is
     s5 e_1, so the determinant factors as s5 * det(s5 I3 + sum s_k C_k)
     IDENTICALLY.  The off-diagonal r_k do not appear at all -- which is what
     makes the component image exact at every contact order rather than an
     order-two or arc statement.  Checked here by changing every r_k and
     confirming the determinant is unmoved.

  3. THE DIMENSION, BY MATCHING BOUNDS.  The component map is
     (C_1..C_4) in A^36 -> the 34 char coefficients.
       upper: conjugation C_k -> g C_k g^-1 is in the fibre; the commutator map
              gl_3 -> A^36 has rank 8 at a random point (centralizer = scalars),
              so the generic orbit is 8-dimensional and the image is <= 36-8 = 28;
       lower: the 34 x 36 Jacobian has rank 28.  s78 does this mod both house
              primes; done here over Q, which is the stronger direction.
     Both meet at 28.  This sharpens S2 Theorem 5.1, which bounded only
     order-two fixed-factor leading forms by 29, to the whole component.

usage: python3 analysis/wk12_int_s78_verify.py [--seed 7801]
"""
import itertools
import json
import os
import random
import sys

import sympy as sp

ROOT = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
s1, s2, s3, s4, s5 = sp.symbols("s1 s2 s3 s4 s5")
SS = [s1, s2, s3, s4]


def char_coeffs(mats, n):
    """the s5-graded coefficients of det(s5 I_n + sum s_k mats[k])."""
    m = sp.eye(n) * s5 + sum((SS[k] * mats[k] for k in range(4)), sp.zeros(n, n))
    p = sp.Poly(sp.expand(m.det()), s1, s2, s3, s4, s5)
    by = {}
    for mono, c in p.terms():
        by.setdefault(mono[4], {})[mono[:4]] = c
    return by


def good_keys():
    return sorted({tuple(m) for d in (1, 2, 3)
                   for m in itertools.product(range(4), repeat=4) if sum(m) == d})


def main(argv):
    seed = int(argv[argv.index("--seed") + 1]) if "--seed" in argv else 7801
    rng = random.Random(seed)
    rnd = lambda a, b: sp.Matrix(a, b, lambda i, j: rng.randint(-4, 4))    # noqa: E731

    B = [rnd(4, 4) for _ in range(4)]
    by = char_coeffs(B, 4)
    grading = {int(e): sorted({sum(k) for k in by[e]}) for e in by}
    counts = {int(e): len(by[e]) for e in by}
    grading_ok = all(grading[e] == [4 - e] for e in grading)

    C = [rnd(3, 3) for _ in range(4)]
    r = [rnd(1, 3) for _ in range(4)]
    blk = lambda rr: [sp.Matrix(sp.BlockMatrix([[sp.zeros(1, 1), rr[k]],       # noqa: E731
                                                [sp.zeros(3, 1), C[k]]])) for k in range(4)]
    m4 = sp.eye(4) * s5 + sum((SS[k] * blk(r)[k] for k in range(4)), sp.zeros(4, 4))
    m3 = sp.eye(3) * s5 + sum((SS[k] * C[k] for k in range(4)), sp.zeros(3, 3))
    factors = sp.expand(m4.det() - s5 * m3.det()) == 0
    r2 = [rnd(1, 3) for _ in range(4)]
    m4b = sp.eye(4) * s5 + sum((SS[k] * blk(r2)[k] for k in range(4)), sp.zeros(4, 4))
    r_free = sp.expand(m4.det() - m4b.det()) == 0

    keys = good_keys()
    eps = sp.Symbol("eps")

    def vec(mats):
        b = char_coeffs(mats, 3)
        flat = {}
        for e in b:
            if e < 3:
                flat.update(b[e])
        return [flat.get(k, 0) for k in keys]

    cols = []
    for k in range(4):
        for i in range(3):
            for j in range(3):
                Cs = [x.copy() for x in C]
                Cs[k] = Cs[k] + eps * sp.Matrix(3, 3, lambda a, b: 1 if (a, b) == (i, j) else 0)
                cols.append([sp.expand(x).coeff(eps, 1) for x in vec(Cs)])
    J = sp.Matrix(cols).T
    jrank = J.rank()

    L = []
    for i in range(3):
        for j in range(3):
            g = sp.Matrix(3, 3, lambda a, b: 1 if (a, b) == (i, j) else 0)
            L.append([x for k in range(4) for x in (g * C[k] - C[k] * g)])
    orbit = sp.Matrix(L).T.rank()

    # The COUNT claim (1, 4, 10, 20, 35) is the combinatorial fact that there are
    # binom(d+3,3) monomials of degree d in four variables; it needs no computation.
    # What a random point can show is only the GRADING, and its observed counts are
    # a lower bound: at seed 991 one of the four traces tr(B_k) is accidentally
    # zero, so the s5^3 coefficient shows 3 of its 4 monomials.  Checking equality
    # there would be exactly the sampling-versus-generic error this programme
    # refuses elsewhere, so it is not checked that way.
    expected = {4: 1, 3: 4, 2: 10, 1: 20, 0: 35}
    counts_ok = all(counts.get(e, 0) <= expected[e] for e in expected)
    ok = (grading_ok and counts_ok
          and factors and r_free and J.shape == (34, 36) and jrank == 28 and orbit == 8)
    out = {
        "seed": seed,
        "grading_degrees": grading, "coefficient_counts": counts,
        "coefficient_counts_generic": {"1": 4, "2": 10, "3": 20, "4": 35},
        "good": 34, "bad": 35, "total_ratio_coordinates": 69,
        "ker_component_factors_as_s5_times_3x3": bool(factors),
        "determinant_independent_of_every_r_k": bool(r_free),
        "jacobian_shape": list(J.shape), "jacobian_rank_over_Q": int(jrank),
        "commutator_map_rank_generic_orbit": int(orbit),
        "image_upper_bound": 36 - int(orbit), "image_lower_bound": int(jrank),
        "ker_coker_image_projective": 28 if jrank == 36 - orbit else None,
        "verdict": ("s78's reduction grading and its exact ker/coker dimension 28 both reproduce "
                    "on independently chosen points" if ok else "DISCREPANCY"),
    }
    print(json.dumps(out, indent=1))
    with open(os.path.join(ROOT, "results/wk12_int_s78_verify.json"), "w", encoding="utf-8") as f:
        json.dump(out, f, indent=1)
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
