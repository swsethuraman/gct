#!/usr/bin/env python3
"""The degeneracy-direction pre-check (docs/brief_wording.md).

Any statistic proposed to characterise "determinant type" is evaluated at the
three committed points before anything is proved about it:

    1. det_pencil.json         a det_4 pencil in ten variables
    2. reducible.json          a reducible l * c in ten variables, c random
    3. padded_permanent.json   the full ten-variable x_0 * per_3 (no restriction)

If the statistic is at least as degenerate at 3 as at 1, it separates in the
wrong direction and the work stops.  Where 2 and 3 disagree, that disagreement
is the result.

usage: python3 tools/verify/testset/degeneracy_check.py                  # the worked example
       python3 tools/verify/testset/degeneracy_check.py module:function  # your statistic

The function is called as f(F, r) with F the quartic as {exponent tuple: int}
and r the number of variables, and must return a number where LARGER means
MORE DEGENERATE (a corank, a dimension of a singular locus, a defect); return
a tuple to report several numbers at once.  The worked example is the Macaulay
corank dim (S/J_F)_d of Proposition D (docs/excess_singularity.md), d = 4..7 at
ten variables and d = 4..8 at six, modulo the first house prime.
"""
import os, sys, json, importlib
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, ".."))
from points import form_of_point               # noqa: E402
from layer1 import macaulay_matrix, rank_mod, monomials   # noqa: E402

P1 = 2147483647
POINTS = [("det_pencil", 10), ("reducible", 10), ("padded_permanent", 10)]
POINTS_R6 = [("det_pencil_r6", 6), ("reducible_r6", 6), ("padded_permanent_r6", 6)]


def load_point(name, r):
    with open(os.path.join(HERE, name + ".json")) as f:
        return form_of_point(json.load(f), r)


def macaulay_corank(F, r, degrees=None):
    if degrees is None:
        degrees = range(4, 8) if r == 10 else range(4, 9)
    out = []
    for d in degrees:
        M = macaulay_matrix(F, 4, r, d)
        out.append(len(monomials(r, d)) - rank_mod(M, P1))
    return tuple(out)


def run(stat, points):
    vals = {}
    for name, r in points:
        F = load_point(name, r)
        vals[name] = stat(F, r)
        print(f"  {name:22s} (r = {r}): {vals[name]}", flush=True)
    det, red, pad = [vals[n] for n, _ in points]
    # componentwise comparison when tuples are returned
    as_tuple = lambda v: v if isinstance(v, tuple) else (v,)   # noqa: E731
    d, p, q = as_tuple(det), as_tuple(pad), as_tuple(red)
    wrong = all(pi >= di for pi, di in zip(p, d))
    print("  verdict:", "WRONG DIRECTION -- the padded permanent is at least as degenerate as the "
          "determinant in every component; stop here" if wrong else
          "the determinant is more degenerate in some component; the statistic may point the right way "
          "(this is necessary, not sufficient)")
    if any(pi != qi for pi, qi in zip(p, q)):
        print("  note: the reducible point and the full padded permanent DISAGREE -- that disagreement is the result")
    return vals


def main():
    if len(sys.argv) > 1:
        mod, fn = sys.argv[1].split(":")
        stat = getattr(importlib.import_module(mod), fn)
        title = sys.argv[1]
    else:
        stat = macaulay_corank
        title = "Macaulay corank dim (S/J_F)_d (worked example, Proposition D)"
    print(f"degeneracy-direction pre-check: {title}")
    print("ten-variable points (the test set proper):")
    run(stat, POINTS)
    print("six-variable companions (restrictions; labelled as such):")
    run(stat, POINTS_R6)


if __name__ == "__main__":
    main()
