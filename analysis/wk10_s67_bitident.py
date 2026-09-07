#!/usr/bin/env python3
"""
Session 67, Part C2 -- bit-identity of the widened monomial code.

The stopping rule: widening the int64 multiset combinadic (wk9_s42_orbits._codes)
must not alter any banked value.  This test builds a spread of already-reachable
cells (delta_close <= 18, well inside the old int64 range) TWICE -- once forcing
the int64 code path, once forcing the exact Python-integer (object) path -- and
asserts the two builds are bit-identical in every quantity a banked result rests
on: N_S, |Stab|, n_chi, the per-monomial column map col_of, the twisted signs
sgn, and the full raising-operator matrix E (shape, indptr, indices, data) and
its nfixed count.

Because the object path returns the SAME integer values as int64 wherever int64
did not overflow, the two must agree exactly; a single mismatch would mean the
widening is a defect and the run fails (the session then reports the discrepancy
rather than shipping the widening).

usage: python3 analysis/wk10_s67_bitident.py
"""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import numpy as np
import wk9_s42_orbits as orb
from wk9_s45_build import build_cell

# reachable length-5 cells spanning trivial, small and large stabilisers and a
# range of delta; all delta_close-style sizes inside the old int64 range.
CELLS = [
    (6, (12, 5, 5, 1, 1)),     # |Stab| = 4
    (6, (9, 9, 4, 1, 1)),      # two equal-part blocks
    (6, (8, 4, 4, 4, 4)),      # |Stab| = 24, the first pad-side bite cell
    (7, (12, 4, 4, 4, 4)),     # |Stab| = 24, larger
    (6, (11, 7, 3, 2, 1)),     # |Stab| = 1, all parts distinct
    (8, (13, 9, 8, 1, 1)),     # a s60 reducible-bite cell
    (6, (7, 6, 5, 4, 2)),      # the largest s60 delta=6 census cell region shape
]


def build_forced(lam, delta, wide):
    orb._CODES_WIDE_OVERRIDE = wide
    try:
        B = build_cell(lam, delta, n=4, verbose=False)
    finally:
        orb._CODES_WIDE_OVERRIDE = None
    E = B['E'].tocsr(); E.sort_indices()
    return B, E


def compare(lam, delta):
    Bi, Ei = build_forced(lam, delta, False)      # int64 path
    Bo, Eo = build_forced(lam, delta, True)       # object (wide) path
    checks = []
    for key in ('N_S', 'stab', 'n_chi', 'nrows', 'nnz', 'nfixed'):
        checks.append((key, Bi[key] == Bo[key], f"{Bi[key]} vs {Bo[key]}"))
    ai, ao = Bi['arr'], Bo['arr']
    checks.append(('col_of', np.array_equal(ai['col_of'], ao['col_of']), ''))
    checks.append(('sgn', np.array_equal(ai['sgn'], ao['sgn']), ''))
    checks.append(('E.shape', Ei.shape == Eo.shape, f"{Ei.shape} vs {Eo.shape}"))
    checks.append(('E.indptr', np.array_equal(Ei.indptr, Eo.indptr), ''))
    checks.append(('E.indices', np.array_equal(Ei.indices, Eo.indices), ''))
    checks.append(('E.data', np.array_equal(Ei.data, Eo.data), ''))
    ok = all(c[1] for c in checks)
    return ok, checks, Bi


def main():
    allok = True
    for delta, lam in CELLS:
        ok, checks, B = compare(lam, delta)
        allok &= ok
        tag = f"{lam} d{delta}: N_S={B['N_S']} |Stab|={B['stab']} n_chi={B['n_chi']} nnz={B['nnz']}"
        print(f"{'ok ' if ok else 'BAD'} {tag}")
        if not ok:
            for name, good, detail in checks:
                if not good:
                    print(f"      [MISMATCH] {name} {detail}")
    # also assert the boundary: int64 fits through delta=19 at r=5, overflows at 20
    assert orb._codes_fit_int64(70, 19) and not orb._codes_fit_int64(70, 20), "int64 boundary at r=5 moved"
    print("int64 boundary at r=5 (L=70): fits delta<=19, overflows delta>=20  [confirmed]")

    # the unblock: a delta=20 closing cell (over the old int64 wall) must now build.
    # The old code asserted comb(L+delta-1,delta) < 2^63 and could not reach it.
    lam20, d20 = (57, 17, 2, 2, 2), 20     # smallest delta_close=20 tail (17,2,2,2)
    assert not orb._codes_fit_int64(70, d20), "delta=20 should not fit int64 at r=5"
    B = build_cell(lam20, d20, n=4, verbose=False)
    E = B['E'].tocsr()
    cols_hit = int((np.diff(E.tocsc().indptr) > 0).sum())
    unblocked = (E.shape[1] == B['n_chi'] and cols_hit == B['n_chi'] and B['n_chi'] > 0)
    allok &= unblocked
    print(f"{'ok ' if unblocked else 'BAD'} delta=20 unblock: {lam20} builds, "
          f"N_S={B['N_S']} n_chi={B['n_chi']} nnz={B['nnz']} (every column reached: {cols_hit}/{B['n_chi']})")

    print("bit-identity + unblock", "PASSED" if allok else "FAILED")
    return 0 if allok else 1


if __name__ == '__main__':
    sys.exit(main())
