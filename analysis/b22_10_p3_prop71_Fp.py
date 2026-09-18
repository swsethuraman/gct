"""B22-10 pilot 3 — replay of the transverse values behind the F_P form of arc_target Prop. 7.1.

Input (pinned): routeA_signfilter_20260917/certificates/transverse_triple_rank3.json at archive
82633a60, read from a `git show` copy.  Imports no project code.
  1. Recompute the 3x3 matrix (C2, C4_S1S2, C4_S1S4) x (q3, q7, n02) from the pencil values and
     the stated integer formulas, mod P; compare with the shipped matrix; recompute det (225843).
  2. With (alpha, beta) = (265391, 275398): C2(n̄), C4_S1S2(n̄), C4_S1S4(n̄) for
     n̄ = n02 - alpha q3 - beta q7, mod P.  Expected 0, 499917, 487898.
"""
import hashlib
import json
import re
import sys
from pathlib import Path

P = 524287
ALPHA, BETA = 265391, 275398
PIN = "4ac3f89688e3515e4252e51192b70307ac600c4a9e20ae1f8d491c1ebf3d2804"
src = Path(sys.argv[1])
raw = src.read_bytes()
got = hashlib.sha256(raw).hexdigest()
d = json.loads(raw)
out = {"pilot": "b22_10_p3_prop71_Fp", "input_sha256": got, "pin": PIN, "pin_matches": got == PIN}


def apply(formula, vals):
    tot = 0
    for coef, key in re.findall(r"([+-]?\s*\d+)\s*z\(([^)]+)\)", formula):
        tot += int(coef.replace(" ", "")) * vals[key]
    return tot % P


cols = d["columns"]
rows = d["row_order"]
mine = [[apply(d["formulas"][r], d["pencil_values"][c]) for c in cols] for r in rows]


def det3(m):
    return (m[0][0] * (m[1][1] * m[2][2] - m[1][2] * m[2][1])
            - m[0][1] * (m[1][0] * m[2][2] - m[1][2] * m[2][0])
            + m[0][2] * (m[1][0] * m[2][1] - m[1][1] * m[2][0])) % P


nbar = {r: (mine[i][2] - ALPHA * mine[i][0] - BETA * mine[i][1]) % P for i, r in enumerate(rows)}
out.update({
    "matrix_recomputed": mine,
    "matrix_equals_shipped": mine == d["matrix"],
    "det_recomputed": det3(mine),
    "det_equals_225843": det3(mine) == 225843,
    "transverse_on_nbar": nbar,
    "C2_nbar_is_0": nbar["C2"] == 0,
    "C4_S1S2_nbar_is_499917": nbar["C4_S1S2"] == 499917,
    "C4_S1S4_nbar_is_487898": nbar["C4_S1S4"] == 487898,
})
Path(sys.argv[2]).write_text(json.dumps(out, indent=1) + "\n")
print(json.dumps(out, indent=1))
