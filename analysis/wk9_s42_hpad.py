#!/usr/bin/env python3
"""
Session 42 -- h_pad(lam, delta): the multiplicity of S_lam in the degree-delta
part of the NORMALISATION of C[R_r], R_r = {l . c} in Sym^4 C^r.

Proved (docs/reducible_engine.md, section B).  The Kempf collapsing
q : Tot(O(-1) (x) Sym^3 V^*) -> W has H^0(Z, O_Z) = (+)_delta Sym^delta V (x)
Sym^delta(Sym^3 V) =: D, the Segre-product ring = the normalisation of
C[R_r] (finite + birational + normal source).  Hence, for every cell,

    mult_red(lam, delta) <= h_pad(lam, delta)
                         := mult of S_lam in Sym^delta V (x) Sym^delta(Sym^3 V)
                         =  sum_{nu} c_nu( Sym^delta(Sym^3 C^r) ),

the sum over nu with lam_{i+1} <= nu_i <= lam_i for every i (lam/nu a
horizontal delta-strip; Pieri), |nu| = 3 delta.  This is the bound of
docs/theory_directions.md B(ii)(c); it needs no rank, no points, and no
frontier.  h_pad < a proves the reducible ideal bites at (lam, delta).

usage: python3 wk9_s42_hpad.py delta lam_1 lam_2 ...     (one cell)
       python3 wk9_s42_hpad.py --banked                  (all 91 s36 cells)
"""
import sys, os, re
from functools import lru_cache
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
from wk8_s30_pleth import amb

@lru_cache(maxsize=None)
def cubic_pleth(delta, maxrows):
    """{nu: c_nu} for Sym^delta(Sym^3 C^maxrows), nu without trailing zeros."""
    return amb(delta, 3, maxrows)

def pieri_strips(lam, delta):
    """all nu (tuples of length len(lam)) with lam_{i+1} <= nu_i <= lam_i and
    |nu| = |lam| - delta."""
    lam = tuple(lam); r = len(lam); target = sum(lam) - delta
    out = []
    def rec(i, cur, s):
        if i == r:
            if s == target: out.append(tuple(cur))
            return
        lo = lam[i + 1] if i + 1 < r else 0
        hi = lam[i]
        # remaining capacity pruning
        for v in range(lo, hi + 1):
            rec(i + 1, cur + [v], s + v)
    rec(0, [], 0)
    return out

def h_pad(lam, delta):
    lam = tuple(x for x in lam if x)
    r = len(lam)
    if sum(lam) != 4 * delta: return 0
    C = cubic_pleth(delta, r)
    tot = 0
    for nu in pieri_strips(lam, delta):
        key = tuple(x for x in nu if x)
        tot += C.get(key, 0)
    return tot

def banked():
    rows = []
    for line in open(os.path.join(HERE, '..', 'results', 's36_red_table.md')):
        m = re.match(r"\| `\((.*?)\)` \| (\d+) \| (\d+) \| (\d+) \| (\d+) \| (\d+) \| (\d+) \|", line)
        if m:
            lam = tuple(int(x) for x in m.group(1).split(','))
            rows.append((lam, int(m.group(2)), int(m.group(4)), int(m.group(5)), int(m.group(6)), int(m.group(7))))
    return rows

if __name__ == '__main__':
    if sys.argv[1:] == ['--banked']:
        print("| lam | delta | a | mult_det | mult_pad | mult_red | h_pad | h_pad - mult_red | h_pad < a |")
        print("|---|---|---|---|---|---|---|---|---|")
        n_eq = n_gt = n_lt_a = 0
        for lam, delta, a, mdet, mpad, mred in banked():
            h = h_pad(lam, delta)
            assert h >= mred, ("h_pad below mult_red -- BUG", lam, delta, h, mred)
            n_eq += (h == mred); n_gt += (h > mred); n_lt_a += (h < a)
            print(f"| `{lam}` | {delta} | {a} | {mdet} | {mpad} | {mred} | {h} | {h - mred} | {'yes' if h < a else ''} |")
        print(f"\ncells: {n_eq + n_gt}; h_pad = mult_red at {n_eq}; h_pad > mult_red at {n_gt}; h_pad < a at {n_lt_a}")
    else:
        delta = int(sys.argv[1]); lam = tuple(int(x) for x in sys.argv[2:])
        print(h_pad(lam, delta))
