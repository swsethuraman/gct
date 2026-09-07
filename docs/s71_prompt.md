# Session 71 (C4) — the `r = 5` containment falsifier, in cost order

Batch 11, **ungated, runnable immediately**.  **Read
`docs/batch11_worker_preamble.md` first**, then `docs/batch11_plan.md` §3 (your
row) and §4B, `docs/s67_report.md` Parts B and C, `docs/s60_report.md`,
`docs/l5_containment.md`, `docs/d5_ideal.md`, and
`analysis/wk10_s67_degeneration.py`.

## The question, and why one cell decides it

The open question is whether `R₅ ⊆ D₅` — the reducible variety inside the
determinant orbit closure at `r = 5`.  Containment is a strong statement and it
has a cheap consequence:

    R₅ ⊆ D₅  ⟹  I(D₅) ⊆ I(R₅)  ⟹  i_det ≤ i_red  at every cell

So **one exact cell with `i_det > i_red` refutes containment.**  That is an
unusually clean falsifier, and unlike session 72 and Sol's S3 it needs no exhaustion
theorem — it needs one number at one cell.

## What the falsifier concretely is

Every one of the 419 `r = 5` cells session 60 measured has `mult_det = a`, hence
`i_det = 0`, hence `i_det ≤ i_red` trivially.  So the falsifier you are looking
for is precisely:

> **the first `r = 5` cell with `i_det ≥ 1` and `i_red = 0`** — equivalently, a
> length-5 equation of `I(D₅)`, which the record expects to live above degree 9
> and has never exhibited.

`dim D₅ = 50` inside `dim Sym⁴C⁵ = 70`, so `I(D₅)` is certainly nonempty; the
open part is where its equations sit and whether any of them is reachable.  That
framing, not "sweep and hope", is the session.

## The cost ordering

Session 67 widened the int64 monomial code and made **all 1 075 stable closing
cells buildable**, up from 892, bit-identically on every already-reachable cell.
Buildable is not overnight-cheap, so exhaust them in **increasing certified cost
order**, not in index order:

1. **Degeneration first.**  Session 67's initial-term certifier is sound and
   one-directional (`rank(in Θ) ≤ rank Θ`): it certifies *full rank* at
   `O(nnz)`, thousands of times cheaper than the rank it replaces, with zero
   false certifications on 27 of 32 tested cells.  Full rank means `i_det = 0`,
   which is exactly "this cell is not the falsifier".  **So degeneration removes
   cells from your search list at almost no cost, and can never evidence the
   drop you are looking for.**  Use it as the cheap sieve, never as evidence.
2. **Hybrid for the residue.**  Where degeneration covers 99.4–99.9% of the
   columns and no more — an intrinsic limit, so a pure-degeneration engine is
   not worth building — finish with the sparse rank.  Session 67 says the hybrid
   is the only version worth a successor's time; this is that successor.
3. **Exact ranks last**, only on what survives, in ascending `n_χ`.

Record the certified cost of each cell before you run it, and report the curve.

## Free third column

While a cell is being evaluated you already have the source and the raising
kernel.  Adding the **unpadded `per₄`** evaluation family there costs one more
evaluation row set and no new build (plan §1.1).  It is favourably directed
(`dim{det₄ forms in r vars} = 16r − 30` against `16r − 6` for `per₄`) and it is
the `n = 4` positive control the programme has never had.  **Add it wherever you
are already evaluating a cell**, and report `i_{per₄}` alongside `i_det` and
`i_red`.

## Tasks

1. Pre-register the cost model and the ordering it induces, before running.
2. Sieve with degeneration; report how many of the 1 075 it closes and at what
   total cost.
3. Hybrid and exact ranks on the residue, in cost order, banking per cell.
4. Add the `per₄` column wherever a cell is evaluated.
5. Stop immediately on any cell with `i_det > i_red`, and take it through the
   verification protocol before reporting it anywhere, including in
   conversation.
6. If no falsifier appears, report **where the information rate flattened** —
   the cost curve, the fraction of the 1 075 closed, and what a further night
   would buy.  That is the deliverable in the negative case and it is a real
   one.

## Success

Either one verified cell with `i_det > i_red`, or the affordable prefix
exhausted with a cost curve and an explicit statement of the residue.

## Stopping rules

- A `D > 0` or `i_det > i_red` cell halts the sweep; the verification protocol
  takes over.
- Do not burn compute after the information rate has flattened.  This is a
  falsifier sweep, not an obligation to finish 1 075 cells.
- Any disagreement with a banked `mult_det` or `mult_red` halts the sweep and is
  reported as a defect, not worked around.

## Deliverables

`results/PREREG_s71.md` with the cost model; `docs/s71_report.md`; the per-cell
table with `a`, `h_pad`, `i_det`, `i_red`, `i_{per₄}`, certified cost, route and
primes as `results/s71_sweep.md` and `.jsonl`; certificates in `results/certs/`;
code under `analysis/wk11_s71_*.py`; bundle `s71_falsifier.bundle` + `.md5`.
