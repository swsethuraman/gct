#!/usr/bin/env python3
"""
Session 79 -- controls for the cubic-side driver (after the adversarial audit):
  (i) the evaluation family is the PERMANENT, not the determinant or a reducible cubic:
      per3_coeffs(pt) differs from the det_3 restriction of the same pencil at every
      recorded point (and per_form(3) itself is checked against a hand permanent);
  (ii) two a = 2 weights of degree 8 from session 43's record reproduce mult = a = 2
      (a nonvanishing test at a = 1 cannot tell one family from another; a rank-2 test can
      at least fail).
"""
import sys, os, random, json
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import itertools
from wk8_s30_core import per_form, det_form, restrict
from wk12_s79_per6 import per3_pencils, per3_coeffs, measure_weight, SEED, BOUND, R, n3

PER3, N3 = per_form(3); DET3, _ = det_form(3)
# (i) per_form(3) is the permanent: compare with a hand permanent at a numeric matrix
M = [[2, 3, 5], [7, 11, 13], [17, 19, 23]]
hand = sum(M[0][s[0]] * M[1][s[1]] * M[2][s[2]] for s in itertools.permutations(range(3)))
val = sum(c * (M[0][0] ** b[0]) * (M[0][1] ** b[1]) * (M[0][2] ** b[2]) * (M[1][0] ** b[3]) * (M[1][1] ** b[4]) * (M[1][2] ** b[5]) * (M[2][0] ** b[6]) * (M[2][1] ** b[7]) * (M[2][2] ** b[8]) for b, c in PER3.items())
print("per_form(3) at a numeric matrix:", val, "hand permanent:", hand, "det:", 2*(11*23-13*19) - 3*(7*23-13*17) + 5*(7*19-11*17))
assert val == hand
pts = per3_pencils(10, SEED, BOUND)
diff = 0
for pt in pts:
    As = [[pt[i][a][b] for a in range(3) for b in range(3)] for i in range(R)]
    if per3_coeffs(pt) != restrict(DET3, 9, 3, R, As): diff += 1
print(f"per_3 vs det_3 coefficient dicts differ at {diff} of {len(pts)} recorded points")
assert diff == len(pts)
out = []
for mu in ((11, 4, 4, 2, 2, 1), (10, 6, 4, 2, 1, 1)):
    r = measure_weight(mu, 8, verbose=False, a_given=2)
    print(f"  control {mu} d8: a={r['a']} mult={r['mult']} units={r['units']} ({r['secs']}s)  [s43 record: mult = a = 2]")
    assert r['mult'] == 2
    out.append(r)
json.dump(dict(per_form_is_permanent=True, per3_ne_det3_points=diff, controls=[{k: v for k, v in r.items() if k != 'per_prime'} for r in out]),
          open(os.path.join(HERE, '..', 'results', 's79_per6_control.json'), 'w'), indent=1)
print("controls PASS")
