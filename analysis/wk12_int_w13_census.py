#!/usr/bin/env python3
"""Weight-13 stable census, reconciled through batch 12 by B13-11.

Exact integer Weyl counting gives 57 shapes, 10 zero and 47 positive blocks.
The stable and quartic records close 28 positive blocks. The other 19 have
quartic length <=4 and are excluded for a positive padded gap by the inherited
containment theorem. Rank-record openness and gap openness are separate fields.
The five a_inf=4 blocks are all closed; they are no longer a frontier.

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

from b13_11_math import a_inf_exact as a_inf


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
    from wk9_s57_lib import negative_record
    from b13_11_ledger import quartic_closed_tails
    rec_ = negative_record()
    srcs = sorted({s for v in rec_.values() for s in v[2].split(';')})
    print(f"  [quartic record: {len(rec_)} cells from {', '.join(srcs)}]")
    print("  [B13-11: full-rank record through s79; imported certificates are adopted, not all replayed]")
    return quartic_closed_tails(vals, rec_)


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
    print(f"  a_inf <= 3: {sum(c for v, c in dist.items() if v <= 3)}")
    print(f"  a_inf =  4: {dist.get(4, 0)}")
    # OPEN MEANS OPEN ON BOTH INSTRUMENTS.  Session 79 found that four of the
    # five a_inf = 4 blocks this script called "the first open frontier" were
    # already closed by the QUARTIC record: Proposition S closes a tail whenever
    # a recorded cell with a = a_inf has mult_det = a.  Counting "open" against
    # the stable instrument's own history overstates the frontier, and the same
    # cross-reference must precede any a_inf = 5 slot.
    closed_by_record = record_closed_tails(vals)
    from b13_11_ledger import stable_closed_tails
    closed_by_stable = stable_closed_tails(vals)
    still_open = {k: v for k, v in nz.items() if k not in closed_by_record | closed_by_stable}
    from b13_11_ledger import partition
    inherited_containment = {k for k in nz if len(partition(k)) + 1 <= 4}
    open_for_gap = {k:v for k,v in still_open.items() if k not in inherited_containment}
    print(f"  closed by the quartic record (Prop. S, a = a_inf and mult_det = a): "
          f"{len(closed_by_record & set(nz))}")
    for lev in sorted(set(nz.values())):
        o = sorted(k for k, v in still_open.items() if v == lev)
        print(f"  a_inf = {lev:2d}: {len(o)} open on BOTH instruments" + (f"  {o}" if o and lev >= 4 else ""))
    print(f"  a_inf =  1: {sorted(k for k, v in nz.items() if v == 1)}")
    print(f"  open in the two rank records: {len(still_open)}; open for D > 0 after "
          f"inherited length <= 4 containment: {len(open_for_gap)}")
    rec = {
        "board_numbering": "batch13", "session_id": "B13-11",
        "weight": weight, "max_parts": 5,
        "shapes": len(vals), "a_inf_zero": len(vals) - len(nz), "a_inf_positive": len(nz),
        "distribution": {str(k): v for k, v in dist.items()},
        "closed_a_inf_le_3": sum(v <= 3 and k in closed_by_record | closed_by_stable for k,v in nz.items()),
        "frontier_a_inf_eq_4": sum(v == 4 for v in still_open.values()),
        "total_a_inf_eq_4": dist.get(4, 0),
        "closed_by_stable_record": [list(k) for k in sorted(closed_by_stable & set(nz))],
        "inherited_padded_containment": [list(k) for k in sorted(inherited_containment)],
        "inherited_padded_containment_source": "docs/n4_gate.md section 1; D <= 0, does not assert i_det = 0",
        "open_on_all_instruments": {str(list(k)):v for k,v in sorted(open_for_gap.items())},
        "open_on_both_scope": "Only the quartic and stable rank records; apply inherited containment separately",
        "closure_status": "ADOPTED: source claims and exact Proposition S; per-source replay flags in B13-11 inventory",
        "closed_by_quartic_record": [list(k) for k in sorted(closed_by_record & set(nz))],
        "open_on_both_instruments": {str(list(k)): v for k, v in sorted(still_open.items())},
        "a_inf_one_tails": [list(k) for k in sorted(k for k, v in nz.items() if v == 1)],
        "a_inf_by_shape": {str(list(k)): v for k, v in sorted(vals.items())},
        "supersedes": "docs/s1_s6_batch11_review.md section 2's count of 46; the record's 47 stands",
        "engine": "b13_11_math.a_inf_exact -- Weyl alternation and independent object-integer stable DP; no modular sizing",
        "secs": round(secs, 1),
    }
    with open(os.path.join(ROOT, out), "w", encoding="utf-8") as f:
        json.dump(rec, f, indent=1)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
