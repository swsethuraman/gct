#!/usr/bin/env python3
"""Write the fixed degeneracy-direction test set (docs/brief_wording.md, the
pre-check): three evaluation points in the declared point format, all in ten
variables so that any statistic sees the same ambient space at each.

  det_pencil.json        F = det_4(sum_{i=1}^{10} s_i A_i), A_i integer 4x4
  reducible.json         F = l(s) * c(s), c a random cubic in ten variables
  padded_permanent.json  F = x_0 * per_3(x_1..x_9): the full ten-variable padded
                         permanent, the identity substitution -- NOT a restriction

plus six-variable companions (suffix _r6) for statistics only affordable there;
those are restrictions and are labelled as such.  Entries from
random.Random(20260905 + 4900), box +-100.  Run once; the files are committed
and never regenerated silently (re-running must reproduce them byte for byte).
"""
import os, json, random, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, ".."))
from points import fresh_point, form_of_point   # noqa: E402

SEED = 20260905 + 4900


def main():
    rnd = random.Random(SEED)
    out = {}
    for r in (10, 6):
        suf = "" if r == 10 else "_r6"
        out["det_pencil" + suf] = fresh_point("det_pencil", r, rnd, box=100)
        out["reducible" + suf] = fresh_point("reducible", r, rnd, box=100)
        if r == 10:
            ident = [[1 if i == j else 0 for j in range(10)] for i in range(10)]
            out["padded_permanent"] = {"type": "padded_permanent", "linear_forms": ident}
        else:
            out["padded_permanent_r6"] = fresh_point("padded_permanent", r, rnd, box=100)
    for name, pt in out.items():
        r = 6 if name.endswith("_r6") else 10
        F = form_of_point(pt, r)           # must rebuild
        path = os.path.join(HERE, name + ".json")
        with open(path, "w") as f:
            json.dump(pt, f)
        print(f"{name}: r = {r}, {len(F)} monomials, written {os.path.relpath(path)}")


if __name__ == "__main__":
    main()
