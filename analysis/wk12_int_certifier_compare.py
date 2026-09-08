#!/usr/bin/env python3
"""Batch-12 pre-batch -- pay the certification debt: compare session 67's
initial-term certifier with session 71's re-implementation, line for line and
then empirically.

Session 71's hybrid says of itself: "session 67's initial-term certifier,
re-implemented here from its record."  It was written from s67's REPORT, not
from s67's code -- s71 branched before s67's tree was merged.  Two independent
implementations of a rank lower bound, never compared.  This script compares
them.

THE READING (line for line):

  s67  analysis/wk10_s67_degeneration.py :: leading_columns(F, key)
       leading column of a row = the column of MAXIMUM key.
       returns d = #distinct leading columns.  certify() maximises d over a
       family of key arrays and reports certified iff d == n_chi.

  s71  analysis/wk11_s71_hybrid.py :: cover(F, nc, pos)
       leading column of a row = the column of MINIMUM position.
       returns the same count as `size`, and additionally the chosen rows (the
       sparsest per lead) and the covered/uncovered column split, which the
       Schur-complement residual needs.

  The two conventions are the same object under order reversal: with
  pos = (nc - 1) - key, argmin(pos) = argmax(key) row by row, so the leads
  agree row by row and the counts agree exactly.  Both families of orders are
  closed under reversal (s67: arange and its reverse, colsup ascending and
  descending, random; s71: natural, reversed, fill_asc, fill_desc, random), so
  neither searches a strictly better family in principle.  DIFFERENCES that are
  real but not defects: s67 tries more random orders (its `orders` argument,
  default 6, on top of the four deterministic ones) so its best d can only be
  >=; s71 stops at five orders because a shortfall costs it a bigger residual
  rather than a failed certification.  s71 also picks, among rows sharing a
  lead, the one with fewest nonzeros -- irrelevant to the count, useful to the
  solve.  Neither reverses the inequality: both certify only rank >= d, and a
  shortfall is uninformative in both.

THE TEST (empirical): for every cell and every key array in s67's own family,

    s67.leading_columns(F, key)  ==  s71.cover(F, nc, (nc-1)-key)['size']

exactly -- per order, not merely at the maximum.  Any single disagreement is a
defect in one of the two and the run fails.

usage: python3 analysis/wk12_int_certifier_compare.py [--out results/wk12_int_certifier_compare.json]
"""
import json
import os
import sys
import time

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, ".."))
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.join(ROOT, "tools/verify"))

import numpy as np

import wk10_s67_degeneration as s67
import wk11_s71_hybrid as s71
from wk9_s45_build import build_cell

# Small cells, spanning trivial / small / large stabilisers, from s67's own
# bit-identity list so the comparison runs on matrices both sessions could see.
CELLS = [
    (6, (12, 5, 5, 1, 1)),
    (6, (9, 9, 4, 1, 1)),
    (6, (8, 4, 4, 4, 4)),
    (6, (11, 7, 3, 2, 1)),
    (7, (12, 4, 4, 4, 4)),
]


def compare_one(lam, delta, n_random=4, seed=0):
    b = build_cell(lam, delta, n=4, verbose=False)
    F, nc = b["E"], b["n_chi"]
    rows = []
    for i, key in enumerate(s67._orders(F, nc, n_random, seed)):
        key = np.asarray(key, dtype=np.int64)
        d67 = s67.leading_columns(F, key)
        pos = (nc - 1) - key
        d71 = s71.cover(F, nc, pos.astype(np.int64))["size"]
        rows.append(dict(order=i, d_s67=int(d67), d_s71=int(d71), agree=bool(d67 == d71)))
    return dict(lam=list(lam), delta=delta, n_chi=int(nc),
                nrows=int(F.shape[0]), nnz=int(F.nnz),
                orders=rows,
                best_d=max(r["d_s67"] for r in rows),
                certified=bool(max(r["d_s67"] for r in rows) == nc),
                all_agree=all(r["agree"] for r in rows))


def main(argv):
    out = "results/wk12_int_certifier_compare.json"
    if "--out" in argv:
        out = argv[argv.index("--out") + 1]
    recs = []
    t0 = time.time()
    for delta, lam in CELLS:
        rec = compare_one(lam, delta)
        recs.append(rec)
        mark = "agree" if rec["all_agree"] else "DISAGREE"
        print(f"  {lam} d{delta}: n_chi={rec['n_chi']:6d} best_d={rec['best_d']:6d} "
              f"{len(rec['orders'])} orders {mark}"
              f"{'  (full column rank certified)' if rec['certified'] else ''}", flush=True)
    ok = all(r["all_agree"] for r in recs)
    result = dict(
        claim="s67's initial-term certifier and s71's re-implementation compute the "
              "same rank lower bound, per order, under the reversal pos = (nc-1) - key",
        cells=recs,
        orders_per_cell=len(recs[0]["orders"]) if recs else 0,
        comparisons=sum(len(r["orders"]) for r in recs),
        agree=ok,
        secs=round(time.time() - t0, 1),
    )
    os.makedirs(os.path.dirname(os.path.join(ROOT, out)), exist_ok=True)
    with open(os.path.join(ROOT, out), "w", encoding="utf-8") as f:
        json.dump(result, f, indent=1)
    print(f"{result['comparisons']} comparisons over {len(recs)} cells: "
          f"{'ALL AGREE' if ok else 'DISAGREEMENT -- stop'}")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
