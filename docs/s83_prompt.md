# s83 — the cubic side at `r = 9`, at the goal cell's rungs

`board_numbering: batch13`.  Read `docs/batch13_worker_preamble.md` first.

## Mission

The LMR goal cell's whole remaining question is whether the padded ideal is ever
more than the reducible one, and Prop. 8(2) says that needs
`I(D₉^{per₃})_δ ≠ 0`.  Two rungs matter: 13, where the integrator measured three
reducible relations, and 23, where `D = 1 − i_red(23)` is decided.

## What is true going in

- At rung 13 of the LMR ladder the three padded kernel directions **are** the
  reducible kernel — same three-space at both primes, 0 escapes at 43 reducible
  points, a 39/39 generic control (`docs/rung13_reducible.md`).
- `D = 1 − i_pad(23)` and `i_pad(24) = i_pad(23)` are proved
  (`docs/s74_final_review.md` §2).
- `λ₁₃ = (21,17,2⁷)`, `λ₂₃ = (61,17,2⁷)`, `λ₂₄ = (65,17,2⁷)`.

## Task 1 — `I(D₉^{per₃})₁₃`, in full

**Fifteen weights**: the horizontal-13-strip predecessors of `λ₁₃`, priced by the
integrator — `a` from 1 to 9, `N_S` from `1.59·10⁷` at `(21,6,2⁷)` to
`3.70·10⁸` at `(19,6,2⁷,2)`.  Re-derive the fifteen and their `a` yourself; do
not take the list from this brief.

Run them in `N_S` order, both primes.  Most are above session 79's `1.5·10⁸`
build wall, so this task is priced against s80's builder; if s80 has not landed,
run what fits and price the rest.

**Prediction (0.6):** `I(D₉^{per₃})₁₃ = 0`, which by Prop. 8(1) makes
`mult_pad = mult_red` at rung 13 a **theorem** and turns the integrator's
measurement into one.

**If instead it is nonzero:** that weight is the first place the permanent
becomes visible in this model.  The protocol takes over before it is reported
anywhere, and the quartic confirmation is at `λ₁₃` itself.

## Task 2 — `I(D₉^{per₃})₂₃`, priced first

Enumerate the horizontal-23-strip predecessors of `λ₂₃` (`|μ| = 69`), compute
`a(μ,23,3)` and `N_S` for each, and **report the price before attempting any of
it**.  Then run what fits, cheapest first.

This is the rung that decides `D` at the goal cell, and it is very likely out of
reach in this box.  A complete, honest price list is the deliverable the batch
needs from it; a partial scan is a bonus.

## Falsifiers

- Your fifteen-weight enumeration disagreeing with the integrator's count or
  `a`-values: report it as a defect in this brief and use your own.
- Any weight where the two primes disagree: recorded, re-run with a fresh seed,
  no verdict until they agree.

## Deliverables

`results/PREREG_s83.md`; `results/s83_per9_d13.jsonl` and, for rung 23,
`results/s83_per9_d23_price.json` plus whatever ran; `docs/s83_report.md`;
bundle + `.md5`.
