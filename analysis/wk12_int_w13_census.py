#!/usr/bin/env python3
"""Batch-12 pre-batch -- the weight-13 stable census, recounted rather than flagged.

The record has said "47 weight-13 shapes" since batch 10.  The batch-11 review of
Sol S4 (docs/s1_s6_batch11_review.md section 2) got 46 -- "57 partitions of 13
into at most five parts, of which 11 have a_inf = 0" -- and asked that whoever
next quotes the number recount rather than inherit it.  This is that recount.

It is exhaustive and cheap: every partition of 13 into at most 5 parts, padded to
length 5, through wk9_s57_stable.a_inf (Weyl alternation over the stable Kostant
count at both house primes, then CRT).  Seconds, not minutes.

RESULT.  57 shapes; 10 with a_inf = 0, not 11; so 47 with a nonempty stable
block.  The record's 47 stands and the review's 46 is the one that was off, by a
single shape in the a_inf = 0 count.  The review's substantive correction is
untouched and confirmed here: there are FOUR tails with a_inf = 1, not three --
(7,2,2,1,1), (5,5,1,1,1), (5,3,3,2), (5,3,3,1,1) -- and (5,3,3,2) is the one no
session of either batch had tested.

The full distribution is banked because the successor session needs it: a_inf <= 3
is eleven blocks, all closed, and the first open frontier a_inf = 4 is exactly
FIVE blocks.  That is the size of the next stable determinant-equation test, and
neither board had the number.

usage: python3 analysis/wk12_int_w13_census.py [--weight 13] [--out results/wk12_int_w13_census.json]
"""
import json
import os
import sys
import time
from collections import Counter

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, ".."))
sys.path.insert(0, HERE)

from wk9_s57_stable import a_inf


def partitions(n, maxpart, maxlen):
    if n == 0:
        yield ()
        return
    if maxlen == 0:
        return
    for p in range(min(n, maxpart), 0, -1):
        for rest in partitions(n - p, p, maxlen - 1):
            yield (p,) + rest


def census(weight=13, maxlen=5):
    shapes = [p + (0,) * (maxlen - len(p)) for p in partitions(weight, weight, maxlen)]
    cache = {}
    t0 = time.time()
    vals = {rho: a_inf(rho, cache) for rho in shapes}
    return vals, time.time() - t0


def main(argv):
    weight = int(argv[argv.index("--weight") + 1]) if "--weight" in argv else 13
    out = argv[argv.index("--out") + 1] if "--out" in argv else "results/wk12_int_w13_census.json"
    vals, secs = census(weight)
    nz = {k: v for k, v in vals.items() if v}
    dist = dict(sorted(Counter(nz.values()).items()))
    print(f"weight {weight}, at most 5 parts: {len(vals)} shapes")
    print(f"  a_inf = 0 : {len(vals) - len(nz)}")
    print(f"  a_inf > 0 : {len(nz)}")
    print(f"  a_inf <= 3: {sum(c for v, c in dist.items() if v <= 3)}  (closed)")
    print(f"  a_inf =  4: {dist.get(4, 0)}  (the first open frontier)")
    print(f"  a_inf =  1: {sorted(k for k, v in nz.items() if v == 1)}")
    rec = {
        "weight": weight, "max_parts": 5,
        "shapes": len(vals), "a_inf_zero": len(vals) - len(nz), "a_inf_positive": len(nz),
        "distribution": {str(k): v for k, v in dist.items()},
        "closed_a_inf_le_3": sum(c for v, c in dist.items() if v <= 3),
        "frontier_a_inf_eq_4": dist.get(4, 0),
        "a_inf_one_tails": [list(k) for k in sorted(k for k, v in nz.items() if v == 1)],
        "a_inf_by_shape": {str(list(k)): v for k, v in sorted(vals.items())},
        "supersedes": "docs/s1_s6_batch11_review.md section 2's count of 46; the record's 47 stands",
        "engine": "wk9_s57_stable.a_inf -- Weyl alternation over the stable Kostant count, both house primes, CRT",
        "secs": round(secs, 1),
    }
    with open(os.path.join(ROOT, out), "w", encoding="utf-8") as f:
        json.dump(rec, f, indent=1)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
