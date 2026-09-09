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


def record_closed_tails(vals):
    """tails closed on the QUARTIC side: a recorded cell (lam, delta) with
    mult_det = a and a = a_inf(tail(lam)) closes its whole ladder by Prop. S.

    Session 79 reported that this join was missing and that it changes the
    frontier count; a frontier should mean open on both instruments.
    """
    try:
        from wk9_s57_lib import negative_record, tail_of
    except Exception as e:                                       # noqa: BLE001
        print(f"  [record cross-reference unavailable: {e}]")
        return set()
    rec_ = negative_record()
    srcs = sorted({v[2] for v in rec_.values()})
    print(f"  [quartic record: {len(rec_)} cells from {', '.join(srcs)}]")
    print("  [WARNING: negative_record() stops at session 54.  Sessions 57, 60, 63,")
    print("   71 and 79 measured cells it does not carry -- s60's (19,6,3,3,1)_8 and")
    print("   (19,4,4,3,2)_8, for two -- so this cross-reference UNDERSTATES what is")
    print("   closed.  Extending the ledger list is a batch-13 task.]")
    closed = set()
    for (lam, delta), row in rec_.items():
        a, mdet = row[0], row[1]
        if mdet != a:
            continue
        t = tuple(tail_of(lam))
        while t and t[-1] == 0:
            t = t[:-1]
        if t in vals and vals[t] == a:
            closed.add(t)
    return closed


def main(argv):
    weight = int(argv[argv.index("--weight") + 1]) if "--weight" in argv else 13
    # The default output path is a function of every argument that changes the
    # computation.  A fixed path plus a variable parameter is how session 75's
    # delta = 12 run silently destroyed the banked delta = 24 row in
    # wk11_int_bdelta.json.  That was a trap in the script, not a fault of the
    # session, and this is the class fix.
    out = (argv[argv.index("--out") + 1] if "--out" in argv
           else f"results/wk12_int_w{weight}_census.json")
    vals, secs = census(weight)
    nz = {k: v for k, v in vals.items() if v}
    dist = dict(sorted(Counter(nz.values()).items()))
    print(f"weight {weight}, at most 5 parts: {len(vals)} shapes")
    print(f"  a_inf = 0 : {len(vals) - len(nz)}")
    print(f"  a_inf > 0 : {len(nz)}")
    print(f"  a_inf <= 3: {sum(c for v, c in dist.items() if v <= 3)}  (closed)")
    print(f"  a_inf =  4: {dist.get(4, 0)}")
    # OPEN MEANS OPEN ON BOTH INSTRUMENTS.  Session 79 found that four of the
    # five a_inf = 4 blocks this script called "the first open frontier" were
    # already closed by the QUARTIC record: Proposition S closes a tail whenever
    # a recorded cell with a = a_inf has mult_det = a.  Counting "open" against
    # the stable instrument's own history overstates the frontier, and the same
    # cross-reference must precede any a_inf = 5 slot.
    closed_by_record = record_closed_tails(vals)
    still_open = {k: v for k, v in nz.items() if k not in closed_by_record}
    print(f"  closed by the quartic record (Prop. S, a = a_inf and mult_det = a): "
          f"{len(closed_by_record & set(nz))}")
    for lev in sorted(set(nz.values())):
        o = sorted(k for k, v in still_open.items() if v == lev)
        print(f"  a_inf = {lev:2d}: {len(o)} open on BOTH instruments" + (f"  {o}" if o and lev >= 4 else ""))
    print(f"  a_inf =  1: {sorted(k for k, v in nz.items() if v == 1)}")
    rec = {
        "weight": weight, "max_parts": 5,
        "shapes": len(vals), "a_inf_zero": len(vals) - len(nz), "a_inf_positive": len(nz),
        "distribution": {str(k): v for k, v in dist.items()},
        "closed_a_inf_le_3": sum(c for v, c in dist.items() if v <= 3),
        "frontier_a_inf_eq_4": dist.get(4, 0),
        "closed_by_quartic_record": [list(k) for k in sorted(closed_by_record & set(nz))],
        "open_on_both_instruments": {str(list(k)): v for k, v in sorted(still_open.items())},
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
