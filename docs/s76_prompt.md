# Session 76 — scale the recursion to `δ = 24`, and measure `C₂₄`

*(the reconciled proposal's s75, second half — a session of its own.  Read the
preamble first.)*

## First 30 minutes

    git rev-parse main
    ls docs/batch12_s1_s2_consolidated.md    # if absent, STOP: you have an old tree
    python3 tools/verify/selftest.py

    # the C_delta engine, and the saturated path structure you will build against
    python3 analysis/wk11_int_cdelta.py 12 60 /tmp/c12.pkl
    python3 -c "import sys;sys.path.insert(0,'analysis');\
from wk11_int_cdelta import two_strip_paths;\
p=two_strip_paths(24);print(len(p),'paths,',len({n for _,n in p}),'shapes')"

Expect 160 paths over 42 shapes at `δ = 24` — identical to `δ = 14`, which is the
saturation that makes this tractable.  Start the `C₂₄` run early and checkpointed;
it is the deliverable that lands regardless of how the rest goes.

## Why this is separate from s75

The `δ = 12` control is an *operator-correctness* problem in a 239-dimensional
recoupling space.  This is a *build-and-memoise* problem in a 2168-dimensional
precursor with a recoupling space near `1.7 × 10⁴`.  Different failure modes,
different instruments.  Merging them puts a gate inside a session, and a night
spent on the first half would produce nothing for the second.

**You are not gated on s75.**  If its control lands, take its interface.  If it
has not reported, build against the specification below — and note that this
session has a deliverable that does not depend on the control at all.

## The deliverable that lands either way: `C₂₄` exactly

`C_δ = Σ_{μ a one-strip predecessor of λ_δ} B_{δ−1}(μ)` is the dimension of the
space the block swap actually works in.  Nobody has `C₂₄`.  Estimated at
`≈ 1.7 × 10⁴` from two independent one-level ratios (`C₁₂/B₁₂ = 7.71` exact,
`B₂₄/a₂₄ = 7.91` exact); that estimate is the honest cost model for the entire S5
route and it should be replaced by a measurement.

The path structure is exact and **saturates at `δ = 14`**, constant to 24:

    12 one-strip predecessors,  160 two-strip paths,  42 distinct shapes,
    maximum path multiplicity 10

So the recoupling combinatorics at the top of the ladder are identical to those
at `δ = 14`; only the multiplicities `a_{δ−2}(ν)` grow.  The engine is
`analysis/wk11_int_cdelta.py` — the same pruned-Weyl / tail-census route that
produced `B₂₄`, with a per-key checkpoint.  Roughly 90 chunked evaluations of the
`B₂₄` cost class.  Checkpoint per shape; an interrupted run must lose nothing.

## The main task

Build `M_λ` as the fixed space of the projected block swap on the
`B₂₄ = 2168`-dimensional precursor, and recover a deterministic 274-dimensional
source.  Then carry the same four evaluation columns as s74 — `det₄`, reducible
`ℓ·c`, **true padded `ℓ·per₃`**, unpadded `per₄` — and the decision table.

Inputs: `docs/s1_s6_batch11_review.md` §3, `results/wk11_int_b24.json` (the twelve
channels, one of which is the goal cell's own ladder predecessor and must return
the banked 273 — it does, and that is the build's self-check), the 7,656-node
memoised shape DAG.

## Constraints

- **No prime below 97.**
- `B₂₄ = 2168` is a dimension, not a map.  S1 says so explicitly and it is worth
  believing before you build on it.
- If s75's interface is unavailable, record what you assumed about the Pieri
  embeddings and evaluation map, so a later session can tell which of your
  results depend on that assumption.
- An independent re-derivation of `B₂₄` falls out of a correct build.  If yours
  does not reproduce 2168 by a route different from `wk11_int_b24.py`, say so —
  that number now sizes the whole route and has one implementation behind it.

## Success

A deterministic 274-dimensional source at the goal cell, evaluable, with the four
columns; **or** exact `C₂₄` plus a characterised account of where the scaling
stopped.  Both are full results.

## Stopping rules

- Exact recoupling or evaluation at `δ = 24` requires carrier-scale data: name
  the step and the quantity, deliver `C₂₄`, stop.
- Memory or time on the memoised DAG: report the peak weighted state count, not
  just the node count — the 7,656 nodes are cheap and the multiplicities are not.
- Any `D > 0`: the verification protocol takes over.

## Deliverables

`results/PREREG_s76.md`; `C₂₄` exact with its per-shape channels; the precursor
and the operator at `δ = 24` as far as they were built; whatever source was
recovered, with its declared row system; `docs/s76_report.md`.
