#!/usr/bin/env python3
"""
Session 64 (batch 10, wave 2, C3) -- the padded evaluation family, in the SAME
source coordinates and the SAME chi-coordinate pipeline the determinant and
reducible sides already use.

The one missing family (docs/batch10_plan.md, this brief):

    mult_pad = a - nullity_Q [E; ev_pad],   ev_pad at points  l(s) . per_3(A(s))

with l a random linear form and A a random 3x3 matrix of linear forms, in r
variables.  This is exactly the TRUE padded permanent

    per_3^pad = x_0 . per_3(x_1 .. x_9)   in   Sym^4 C^10     (analysis/pad.py,
    wk8_s30_core.per_padded(3, 4) = (PAD34, N_PAD=10))

restricted to a generic r-plane:  restrict(PAD34, 10, 4, r, V) with V the r
source vectors v_1..v_r in C^10 gives PAD34(sum_i s_i v_i) = l(s) . per_3(A(s)),
where l(s) = sum_i s_i (v_i)_0 and A(s)_{ab} = sum_i s_i (v_i)_{1+3a+b} are ten
independent random linear forms in s.  So this is not a hand-built l.per_3(A) but
the real object of the programme, evaluated by the same restrict() that produces
ev_det (det_4 pencils) and ev_red (l . generic cubic).

This module gives:
  * pad_points(K, seed, bound)  -> K source frames V (each r x 10 int)
  * pad_coeffs(V)               -> {alpha (|alpha|=4 in r vars): coeff}, the
                                    quartic l(s).per_3(A(s)) in Sym^4 C^r,
                                    identical in shape to det_coeffs / red_coeffs
  * point_record_pad(V)         -> a tools/verify "padded_permanent" record
                                    (linear_forms layout, r-vectors), so the
                                    verifier can rebuild the exact point
  * a self-check (main) tying pad_coeffs to analysis/pad.py's own permanent and
    to wk8_s30_core.restrict(PAD34).

Nothing here computes a rank; it only builds points and coefficient dicts.  The
cell engine (wk10_s64_cell.py) feeds pad_coeffs through ev_rows_from_coeffs, the
same contraction wk9_s60_cell uses for det and red.
"""
import os, sys, random, itertools
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
from wk8_s30_core import exps, restrict, per_padded

PAD34, N_PAD = per_padded(3, 4)      # x_0 . per_3(x_1..x_9) in Sym^4 C^10
assert N_PAD == 10
# the 10 padded-permanent variables: index 0 is x_0 (the pad), 1..9 are the
# permanent entries y_{ab} = index 1 + 3a + b
PAD_VARS = 10


def pad_points(K, seed, bound):
    """K random source frames.  Each frame is an r-independent choice of a point
    in C^10 -- returned as an r x 10 integer matrix V (row i = v_i), entries in
    [-bound, bound].  restrict(PAD34, 10, 4, r, V) is then l(s).per_3(A(s))."""
    def _draw(r, rnd):
        return [[rnd.randint(-bound, bound) for _ in range(PAD_VARS)] for _ in range(r)]
    return _DrawList(K, seed, _draw)


class _DrawList:
    """Lazily-materialised list of K frames for a given r, from one seeded stream
    (so the r is supplied at call time, exactly as reducible_points fixes r=R at
    construction -- here we keep it r-agnostic for reuse across lengths)."""
    def __init__(self, K, seed, draw):
        self.K = K; self.seed = seed; self.draw = draw
    def for_r(self, r):
        rnd = random.Random(self.seed)
        return [self.draw(r, rnd) for _ in range(self.K)]


def pad_frames(K, seed, bound, r):
    """K explicit r x 10 integer frames from random.Random(seed)."""
    rnd = random.Random(seed)
    return [[[rnd.randint(-bound, bound) for _ in range(PAD_VARS)] for _ in range(r)]
            for _ in range(K)]


def pad_coeffs(V):
    """Coefficient dict of l(s).per_3(A(s)) = PAD34(sum_i s_i v_i) in Sym^4 C^r,
    with V = [v_1, .., v_r], each v_i in Z^10.  Uses the validated restrict()."""
    r = len(V)
    return restrict(PAD34, N_PAD, 4, r, V)


def point_record_pad(V):
    """A tools/verify 'padded_permanent' point: linear_forms is the list of the
    ten padded-permanent variables, each written as its length-r linear form in
    s (the c-th linear form has coefficient V[i][c] on s_i).  This is the
    transpose of the frame V and is exactly what points.form_of_point expects."""
    r = len(V)
    linear_forms = [[int(V[i][c]) for i in range(r)] for c in range(PAD_VARS)]
    return {"type": "padded_permanent", "linear_forms": linear_forms}


# --------------------------------------------------------------- self-check
def _per3_direct(A, r):
    """per_3 of a 3x3 matrix A of linear forms (A[a][b] a length-r int vector),
    as a cubic dict, computed independently of restrict()."""
    def lin(vec):
        d = {}
        for i in range(r):
            if vec[i]:
                d[tuple(1 if k == i else 0 for k in range(r))] = vec[i]
        return d
    def pmul(X, Y):
        o = {}
        for e1, c1 in X.items():
            for e2, c2 in Y.items():
                e = tuple(e1[k] + e2[k] for k in range(r)); o[e] = o.get(e, 0) + c1 * c2
        return o
    def padd(X, Y):
        o = dict(X)
        for e, c in Y.items(): o[e] = o.get(e, 0) + c
        return o
    Lin = [[lin(A[a][b]) for b in range(3)] for a in range(3)]
    acc = {}
    for s in itertools.permutations(range(3)):
        acc = padd(acc, pmul(pmul(Lin[0][s[0]], Lin[1][s[1]]), Lin[2][s[2]]))
    return {e: c for e, c in acc.items() if c}


def _selfcheck():
    ok = True
    for r in (3, 4, 5, 6):
        for seed in (0, 1, 2):
            V = pad_frames(1, seed, 6, r)[0]
            # via restrict(PAD34)
            got = {k: v for k, v in pad_coeffs(V).items() if v}
            # independent: l(s) * per_3(A(s)) built by hand from the same frame
            l_vec = [V[i][0] for i in range(r)]           # x_0 coordinate as linear form
            A = [[[V[i][1 + 3 * a + b] for i in range(r)] for b in range(3)] for a in range(3)]
            per = _per3_direct(A, r)
            def lin(vec):
                d = {}
                for i in range(r):
                    if vec[i]:
                        d[tuple(1 if k == i else 0 for k in range(r))] = vec[i]
                return d
            def pmul(X, Y):
                o = {}
                for e1, c1 in X.items():
                    for e2, c2 in Y.items():
                        e = tuple(e1[k] + e2[k] for k in range(r)); o[e] = o.get(e, 0) + c1 * c2
                return o
            want = {e: c for e, c in pmul(lin(l_vec), per).items() if c}
            # degree-4 monomials only, in r vars
            assert all(sum(e) == 4 and len(e) == r for e in got), ("bad support", r, seed)
            if got != want:
                ok = False
                print(f"  MISMATCH r={r} seed={seed}: restrict != l*per3 by hand", file=sys.stderr)
            # point record round-trips through the r-plane layout
            rec = point_record_pad(V)
            assert rec["type"] == "padded_permanent" and len(rec["linear_forms"]) == 10
            assert all(len(lf) == r for lf in rec["linear_forms"])
    print("pad self-check:", "PASS -- restrict(PAD34) == l(s).per_3(A(s)) at r=3..6, seeds 0..2, and point records well-formed" if ok else "FAIL")
    return ok


if __name__ == '__main__':
    ok = _selfcheck()
    sys.exit(0 if ok else 1)
