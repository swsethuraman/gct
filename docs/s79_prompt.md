# Session 79 — the two independent frontiers

*(the reconciled proposal's s78 and s79, merged.  Read the preamble first.)*

## First 30 minutes

    git rev-parse main
    ls docs/batch12_s1_s2_consolidated.md    # if absent, STOP: you have an old tree
    python3 tools/verify/selftest.py

    # the five blocks you are about to test, and the census behind them
    python3 analysis/wk12_int_w13_census.py

Expect 57 shapes, 10 with `a_∞ = 0`, 47 with a nonempty stable block, 11 closed
at `a_∞ ≤ 3`, and **5 at `a_∞ = 4`** — your part 1 in full.  The distribution and
the shape list are in `results/wk12_int_w13_census.json`.

## Why one session

The stable frontier was scoped as a full session on the strength of "44 of 47
weight-13 shapes are open."  Recounted exhaustively
(`analysis/wk12_int_w13_census.py`):

    57 partitions of 13 into at most 5 parts
    10 with a_∞ = 0   (not 11 — the record's 47 stands)
    47 with a nonempty stable block

    a_∞ ≤ 3 :  11 blocks   all closed, including (5,3,3,2) in batch 11
    a_∞ = 4 :   5 blocks   ← the entire open frontier for this session
    a_∞ ≥ 4 :  36 blocks

**Five blocks on a validated instrument is an afternoon**, not a night — the
batch-10 stable pullback ran `(5,3,3,2)` in 26.5 seconds.  So this session does
the bounded piece first and spends the rest of its budget on the open-ended one.

**Order matters and is not negotiable: the stable test first.**  It is bounded
and it banks a result either way.  The `ℓ = 6` frontier is open-ended and could
absorb an entire night without returning anything.

## Part 1 — the stable `a_∞ = 4` frontier at weight 13

Enumerate the five `a_∞ = 4` weight-13 cells in increasing raw-space cost and run
the validated stable pullback (`analysis/wk10_int_stable_hwv.py`, then
`wk10_int_stable_subst.py`).  Distribution and shape list in
`results/wk12_int_w13_census.json`.

**Stop at the first nonzero stable determinant ideal.**  If all five die, bank
the stronger theorem: `a_∞ ≤ 4` implies no weight-13 stable determinant equation.
Do not continue into an `a_∞ = 5` census in this batch.

The covariance check is mandatory and is the reason a negative here can be
trusted: a non-highest-weight vector evaluates nonzero generically, so without
invariance under `A_{i+1} → A_{i+1} + ε A_i` at several `ε` a wrong convention
produces an unfalsifiable negative.  This check caught a normalization error in
batch 10.

If the raw spaces at `a_∞ = 4` turn out an order of magnitude larger than the
`a_∞ = 1` ones, say so and stop — that is the trigger to give this its own slot
in batch 13 rather than let it consume the `ℓ = 6` half.

## Part 2 — the first non-washout padded frontier at `ℓ = 6`

The washout theorem says nothing at length `≤ 5` bears on the permanent, so
`ℓ = 6` is the first length that can.  It was priced out until batch 11 changed
the source-side cost.

Seek, in the cheapest tractable `ℓ = 6` cells, either

    i_det ≥ 1        or        mult_pad < mult_red

using s71's hybrid (initial-term cover plus an exact Schur complement on the
uncovered residual — 10 s where the Wiedemann route took 3,094 s, and bounded by
`N_S · δ` rather than `n_χ²`) and, where justified, the compact circuit.

**The constraint that governs this half.**  s69's circuit economics are a result
about *two-tall-column* shapes: the contraction network has favourable pathwidth
there.  **Do not extrapolate that cost model to an arbitrary `ℓ = 6` shape class
without first exhibiting the contraction representation and a pathwidth bound for
it.**  If you cannot, price the cell under the hybrid instead and say which model
you used for every number you report.

Remember the distinction that has caught this programme twice: **true padded is
`ℓ · per₃`**, the reducible comparison is `ℓ · c` with `c` a general cubic.  They
are different varieties and no claim about one substitutes for the other.  And
check that both varieties in any comparison are proper — the `per₄` column at
`r = 5` is vacuous because `per₄` is dominant there (`74 ≥ 70`), which is a
mistake this integrator has now made twice.

## Success

Part 1: five blocks resolved, or the first nonzero stable ideal with its
certificate.  Part 2: a new `ℓ = 6` cell with either inequality strict — which
would give the programme a laboratory other than LMR.

## Stopping rules

- Part 1 exceeds its expected cost by an order of magnitude: report the measured
  raw-space sizes and stop; do not let it eat part 2.
- Part 2's frontier is bounded by the build rather than the rank: report where,
  at what `N_S · δ`, and under which cost model.
- Any `D > 0` or any `i_det ≥ 1` at a new cell: the verification protocol takes
  over before it is reported anywhere.

## Deliverables

`results/PREREG_s79.md`; the five stable blocks with their covariance checks;
the `ℓ = 6` cells attempted with their measured costs and the model used;
`docs/s79_report.md`.
