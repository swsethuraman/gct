#!/usr/bin/env python3
"""s76 -- independent Weyl-alternation values a_d(nu) at DAG nodes not covered
by any banked file, to check the recursion's kernel dimensions.

Picks `per_level` nodes per requested level from the shape DAG below lambda_24
(seeded, so the sample is reproducible) and computes a_d(nu) by
wk9_s42_census.a_weyl (pruned Weyl alternation + tail DP), the same instrument
that produced B_24.  Writes results/s76_weyl_spotchecks.json incrementally.
"""
import ast
import json
import os
import random
import sys
import time

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
ROOT = os.path.normpath(os.path.join(HERE, ".."))
from wk9_s42_census import a_weyl                       # noqa: E402
from wk11_int_bdelta import lam_of                      # noqa: E402
from wk12_s76_recursion import build_dag, load_refs     # noqa: E402

levels_wanted = [int(x) for x in (sys.argv[1] if len(sys.argv) > 1 else "9,11,13,14,16,18,19,20,21").split(",")]
per_level = int(sys.argv[2]) if len(sys.argv) > 2 else 3
out = os.path.join(ROOT, "results", "s76_weyl_spotchecks.json")
res = json.load(open(out)) if os.path.exists(out) else {}
dag = build_dag(tuple(lam_of(24)))
refs, _ = load_refs(ROOT, 24)
rng = random.Random(76)
for d in levels_wanted:
    cands = [nu for nu in dag[d] if (nu, d) not in refs]
    rng.shuffle(cands)
    for nu in cands[:per_level]:
        key = f"{d}:{nu}"
        if key in res:
            continue
        t = time.time()
        a = a_weyl(nu, d, 4, {})
        res[key] = {"delta": d, "nu": list(nu), "a": a, "secs": round(time.time() - t, 1),
                    "instrument": "wk9_s42_census.a_weyl"}
        json.dump(res, open(out, "w"), indent=1)
        print(f"delta={d} {nu}: a = {a}  [{time.time() - t:.0f}s]", flush=True)
