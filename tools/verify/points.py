"""Evaluation points: parsing the recorded ones and drawing fresh ones.

A recorded point is a dict with a "type" and the data that pins the form:

  {"type": "det_pencil",       "pencil": [A_1, ..., A_r]}       A_i integer n x n
  {"type": "permanent_pencil", "pencil": [A_1, ..., A_r]}       A_i integer n x n, UNPADDED per_n
  {"type": "padded_permanent", "linear_forms": [x_0, ..., x_9]} each a length-r int vector
  {"type": "reducible",        "l": [..r ints..], "cubic": [[alpha, coeff], ...]}
  {"type": "form",             "coefficients": [[alpha, coeff], ...]}   degree n

The matrix size of a pencil and the degree of an explicit form follow the cell's
n, which the caller passes; n = 4 is the default, so nothing written before the
n = 3 extension changes meaning.  "padded_permanent" is x_0 * per_3 and exists
only at n = 4; it is refused at any other n.  "permanent_pencil" is the unpadded per_n
and is a different variety -- see the batch-11 plan section 1.1 for why the two
must never be conflated.

The verifier rebuilds the form from that data (forms.py) -- that is the
semantic check that the point lies on the claimed variety -- and evaluates the
certificate's vectors at it.  Fresh points are drawn from random.Random(seed)
with integer entries in [-box, box]; the seed is recorded in the certificate
and every drawn object is reproducible from it.
"""
import random
from forms import (det_pencil_form, permanent_pencil_form, padded_permanent_form,
                   reducible_form, poly_degree_check)

# The order fixes the fresh-point seed offsets (seed + 1000*k).  permanent_pencil
# is APPENDED, not inserted: session 73 pointed out that inserting it (as the
# integrator's first version did) silently shifts the offsets of
# padded_permanent, reducible and generic, so a certificate's "fresh points of
# family X" would be drawn from a different stream than when it was written.
# The regression that was run missed it because every cert it touched used
# det_pencil, which is index 0 either way.  Do not reorder this tuple.
FAMILIES = ("det_pencil", "padded_permanent", "reducible", "generic", "permanent_pencil")


def _int_vec(v, length, what):
    if not (isinstance(v, list) and len(v) == length
            and all(isinstance(x, int) and not isinstance(x, bool) for x in v)):
        raise ValueError(f"{what}: expected a list of {length} integers")
    return v


def _form_from_pairs(pairs, r, deg, what):
    F = {}
    if not isinstance(pairs, list) or not pairs:
        raise ValueError(f"{what}: expected a nonempty list of [alpha, coeff]")
    for e in pairs:
        if not (isinstance(e, list) and len(e) == 2):
            raise ValueError(f"{what}: entry must be [alpha, coeff]")
        alpha, c = e
        _int_vec(alpha, r, what)
        if any(x < 0 for x in alpha) or sum(alpha) != deg:
            raise ValueError(f"{what}: exponent {alpha} not of degree {deg}")
        if not isinstance(c, int) or isinstance(c, bool) or c == 0:
            raise ValueError(f"{what}: coefficient must be a nonzero integer")
        if tuple(alpha) in F:
            raise ValueError(f"{what}: exponent recorded twice")
        F[tuple(alpha)] = c
    return F


def _check_pencil(pt, r, n, tag):
    if set(pt) != {"type", "pencil"}:
        raise ValueError(f"{tag} point: keys must be exactly type, pencil")
    P = pt["pencil"]
    if not (isinstance(P, list) and len(P) == r):
        raise ValueError(f"{tag} point: need r = {r} matrices")
    for A in P:
        if not (isinstance(A, list) and len(A) == n):
            raise ValueError(f"{tag} point: matrices must be {n}x{n}")
        for row in A:
            _int_vec(row, n, f"{tag} point")
    return P


def form_of_point(pt, r, n=4):
    """Rebuild the degree-n form from a recorded point.  Raises ValueError on any
    malformed data (never guesses)."""
    if not isinstance(pt, dict) or "type" not in pt:
        raise ValueError("point must be a dict with a type")
    t = pt["type"]
    if t == "det_pencil":
        return det_pencil_form(_check_pencil(pt, r, n, "det_pencil"), r, n)
    if t == "permanent_pencil":
        return permanent_pencil_form(_check_pencil(pt, r, n, "permanent_pencil"), r, n)
    if t == "padded_permanent":
        if n != 4:
            raise ValueError("padded_permanent point: the padded family is defined only at n = 4")
        if set(pt) != {"type", "linear_forms"}:
            raise ValueError("padded_permanent point: keys must be exactly type, linear_forms")
        L = pt["linear_forms"]
        if not (isinstance(L, list) and len(L) == 10):
            raise ValueError("padded_permanent point: need ten linear forms")
        for v in L:
            _int_vec(v, r, "padded_permanent point")
        return padded_permanent_form(L, r)
    if t == "reducible":
        if n != 4:
            raise ValueError("reducible point: the reducible family is defined only at n = 4")
        if set(pt) != {"type", "l", "cubic"}:
            raise ValueError("reducible point: keys must be exactly type, l, cubic")
        l = _int_vec(pt["l"], r, "reducible point")
        c = _form_from_pairs(pt["cubic"], r, 3, "reducible point cubic")
        return reducible_form(l, c, r)
    if t == "form":
        if set(pt) != {"type", "coefficients"}:
            raise ValueError("form point: keys must be exactly type, coefficients")
        F = _form_from_pairs(pt["coefficients"], r, n, "form point")
        poly_degree_check(F, n, r)
        return F
    raise ValueError(f"unknown point type {t!r}")


def _exps(deg, r):
    if r == 1:
        return [(deg,)]
    out = []
    for a in range(deg, -1, -1):
        for rest in _exps(deg - a, r - 1):
            out.append((a,) + rest)
    return out


def fresh_point(family, r, rnd, box=1000, n=4):
    """A recorded-style point dict drawn from rnd (so it can be written down)."""
    if family in ("det_pencil", "permanent_pencil"):
        return {"type": family,
                "pencil": [[[rnd.randint(-box, box) for _ in range(n)] for _ in range(n)]
                           for _ in range(r)]}
    if family == "padded_permanent":
        if n != 4:
            raise ValueError("padded_permanent is defined only at n = 4")
        return {"type": "padded_permanent",
                "linear_forms": [[rnd.randint(-box, box) for _ in range(r)] for _ in range(10)]}
    def nz():
        v = rnd.randint(-box, box)
        return v if v else 1
    if family == "reducible":
        if n != 4:
            raise ValueError("reducible is defined only at n = 4")
        return {"type": "reducible",
                "l": [rnd.randint(-box, box) for _ in range(r)],
                "cubic": [[list(a), nz()] for a in _exps(3, r)]}
    if family == "generic":
        return {"type": "form",
                "coefficients": [[list(a), nz()] for a in _exps(n, r)]}
    raise ValueError(f"unknown family {family!r}")
