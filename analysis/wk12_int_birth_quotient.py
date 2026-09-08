#!/usr/bin/env python3
"""Batch-12 pre-batch -- the birth quotient, checked, and what it forces on the ideals.

S1 (Astra, 8 September 2026) proves: with u = c_(n,0,...,0) and M_d the
weight-(nd - |rho|, rho) highest-weight space in degree d,

    ker( M_d --u=0--> R/(u) ) = u M_{d-1},     so   M_d / u M_{d-1} = rho_d(M_d).

u M_{d-1} is exactly Lemma L's ladder transport (s57, same u), so the quotient is
the BIRTH space of rung d and has dimension b_d = a_d - a_{d-1}.  A candidate can
therefore be tested for newness by evaluating it at points with u = 0, against a
b_d x b_d matrix, instead of eliminating it against the whole a_d-dimensional
transported source.  The theorem is correct; I checked it line by line.  u is a
highest-weight vector because E_ij c_alpha = (alpha_i + 1) c_{alpha+e_i-e_j} for
i < j vanishes when alpha_j = 0, and u's alpha is zero in every coordinate past
the first.

WHAT S1 DOES NOT SAY, AND WHAT FOLLOWS.  Let I be a PRIME ideal with u not in I.
Then

    (I ^ M_d) ^ u M_{d-1}  =  u (I ^ M_{d-1}),

since v = uw in I with u not in I forces w in I.  Two consequences:

  (1) i_X(d) - i_X(d-1) is a BIRTH count -- the ideal grows only by births, and
      an ideal vector born at rung d is nonzero mod u.  So the obstruction can be
      found and certified entirely inside the birth quotient.
  (2) i_X(d) - i_X(d-1) <= b_d.  At the LMR cell b_24 = 1, so
      i_det(24) = i_det(23) + eps with eps in {0,1}, and eps = 1 exactly when the
      determinant ideal contains a vector with nonzero u-restriction at delta=24.
      With LMR's i_det(24) >= 1: either i_det(23) >= 1, or i_det(23) = 0 and the
      single delta=24 birth direction IS the determinant ideal vector.

Both hypotheses hold on both sides of the programme.  I(Det_4) and I(l . per_3)
are orbit closures, hence irreducible, hence prime.  And u is not in either: the
coefficient of s_1^n in det_4(sum s_i A_i) is det(A_1), and in l . per_3 it is
a_1 . per(B_1), both generically nonzero.

THE CHECK.  On banked data, at the n=3 cell where the determinant ideal vector is
known exactly (session 62 via session 69, 17,047 chi-coordinates, delta = 12,
b_12 = 1), the proposition predicts the vector is NOT divisible by u.  Verified
here: 54 of its 3,900 nonzero chi-coordinates are u-free, so its restriction to
u = 0 is nonzero and it is a birth direction, as the proposition requires.

The run also measures a second economy nobody has stated: only 729 of the 17,047
chi-coordinates are u-free, so restricting to u = 0 compresses the COORDINATE
SPACE 23-fold as well as shrinking the rank matrix.

CONVENTION TRAP, recorded because it cost a wrong answer here first:
wk8_s30_core.exps and tools/verify/chi_build.exps order the degree-n exponent
tuples OPPOSITELY.  u = c_(n,0,...,0) is index 0 in the chi_build ordering and
index 83 (the last) in the wk8_s30_core ordering at n=3, r=7.  The orbit machinery
uses wk8_s30_core.  Always resolve u by E.index(...), never by a literal.

usage: python3 analysis/wk12_int_birth_quotient.py [--out results/wk12_int_birth_quotient.json]
"""
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, ".."))
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.join(ROOT, "tools/verify"))

import numpy as np

import wk9_s42_orbits as orb

BANKED = "results/artefacts/s69_banked_n3_d12.json"


def u_split(n, r, delta, lam):
    """(has_u per chi coordinate, N_S, count of u-containing monomials).

    u is resolved by lookup in the SAME exps ordering the orbit machinery uses.
    """
    E = orb.exps(n, r)
    iu = E.index(tuple([n] + [0] * (r - 1)))
    _, _, _, arr = orb.orbit_setup_fast(n, r, delta, lam, verbose=False,
                                        want_vecs=False, arrays=True)
    M, col_of, n_chi = arr["M"], arr["col_of"], arr["n_chi"]
    has_u_mono = (M == iu).any(axis=1)
    kept = col_of >= 0
    cols, hu = col_of[kept], has_u_mono[kept]
    lo = np.ones(n_chi, bool)
    hi = np.zeros(n_chi, bool)
    np.logical_and.at(lo, cols, hu)
    np.logical_or.at(hi, cols, hu)
    # lambda_1 is unique on this ladder, so no stabiliser element moves variable 1
    # and u-containment must be constant on each orbit.  Asserted, not assumed.
    assert np.all(lo == hi), "u-containment is not constant on a chi orbit"
    return hi, int(M.shape[0]), int(has_u_mono.sum()), iu


def main(argv):
    out = argv[argv.index("--out") + 1] if "--out" in argv else "results/wk12_int_birth_quotient.json"
    d = json.load(open(os.path.join(ROOT, BANKED), encoding="utf-8"))
    lam, n, r, delta = tuple(d["lambda_"]), d["n"], d["r"], d["delta"]
    vec = [int(x) for x in d["vector_chi_coords"]]
    has_u, N_S, n_mono_u, iu = u_split(n, r, delta, lam)
    assert len(vec) == len(has_u) == d["n_chi"]
    nz = np.array([x != 0 for x in vec])
    free_nz = int((nz & ~has_u).sum())
    rec = {
        "cell": {"n": n, "r": r, "delta": delta, "lambda": list(lam), "n_chi": d["n_chi"]},
        "u": {"alpha": [n] + [0] * (r - 1), "letter_index_wk8_s30_core": iu,
              "note": "chi_build.exps orders letters oppositely; index 0 there"},
        "N_S": N_S, "monomials_containing_u": n_mono_u,
        "chi_u_containing": int(has_u.sum()), "chi_u_free": int((~has_u).sum()),
        "coordinate_compression": round(len(has_u) / max(1, int((~has_u).sum())), 2),
        "banked_vector": {"support": int(nz.sum()), "support_u_free": free_nz,
                          "support_u_containing": int((nz & has_u).sum()),
                          "provenance": d.get("provenance", "")[:160]},
        "verdict": ("nonzero mod u -- a BIRTH direction, as the primality proposition requires"
                    if free_nz else "zero mod u -- lies in u*M_{d-1}, CONTRADICTING the proposition"),
        "proposition": "I prime and u not in I  =>  (I ^ M_d) ^ uM_{d-1} = u(I ^ M_{d-1}); "
                       "hence i_X grows only by births and i_X(d) - i_X(d-1) <= b_d",
    }
    print(json.dumps(rec, indent=1))
    with open(os.path.join(ROOT, out), "w", encoding="utf-8") as f:
        json.dump(rec, f, indent=1)
    return 0 if free_nz else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
