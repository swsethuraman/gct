# s87 — the positive control, and the three-point test where the statistic works

`board_numbering: batch13`.  Read `docs/batch13_worker_preamble.md` first.

## Mission

The programme has exactly one `D > 0` in its record, and the padded comparison
has never been run there.  Run it.

## What is true going in

At `n = 3`, `λ = (19,7,2⁵)`, `δ = 12`, `r = 7`, `a = 6`, the **unpadded**
comparison gives `mult_det = 5` and `mult_per = 6` at both house primes, so
`D = +1` — a multiplicity obstruction, both multiplicities nonzero (batch 11
pre-batch; `analysis/wk11_int_p0a.py`, `results/wk11_int_p0a.json`).  It is the
programme's only positive control and the only end-to-end `D > 0` its machinery
has produced.

Batch 12 measured `mult_pad = mult_red` at `r = 5`, at `r = 6` on 682 cells, and
at `r = 9` at degrees 13 and 24.  Three lengths, four instruments, no exception.
**Nobody has asked whether it also holds at the one cell where the statistic
separates.**

## Why this is worth a session

`docs/brief_wording.md` §5 fixes a committed three-point test set: a `det` pencil,
a reducible point `ℓ·c`, and the **true** padded form — not a length-reduced
restriction.  §5 says: *where (2) and (3) disagree, that disagreement is the
result.*  At the goal cell they agree exactly, at every rung, at both primes.

- If they agree here too, then the padded comparison is degenerate **wherever it
  has been tried**, including where the unpadded one works.  The negative of the
  batch is then a property of the padding, not of the LMR cell — a much stronger
  and much more publishable statement.
- If they disagree here, that is the **first permanent-specific equation in the
  record**, at `a = 6`, on a cell small enough to study exactly.

Either way the answer changes what batch 14 is for.

## Task

1. Reproduce the banked `mult_det = 5`, `mult_per = 6` at `(19,7,2⁵)₁₂`, both
   primes, on the current engine.  This is the calibration and it must pass
   before anything else counts.
2. Run the §5 three-point test at that cell: `det₃` pencils; reducible `ℓ·c` at
   `n = 3` (that is `ℓ` times a quadratic); and the true padded `ℓ·per₂` — state
   the padded form you use and why it is the right one at `n = 3`, since the
   programme's padded family is defined at `n = 4`.  **If no honest padded form
   exists at `n = 3`, say so and report the reducible comparison alone**; that
   is a real finding about the control, not a failure.
3. Then the neighbours: the `n = 3` ladder cells around it, and the `a = 1`
   members of the same family, so the answer is a pattern and not one point.
4. Report `i_red` alongside `i_per` at every cell.  `mult_per ≤ mult_red` is not
   automatic at `n = 3` in the way it is at `n = 4` — check the containment you
   are relying on and state it.

## Falsifiers

- The banked `D = +1` not reproducing → stop, report; that is a defect in the
  record and it outranks everything else in this brief.
- A padded form whose containment in the reducible locus you cannot state → do
  not report a `mult_pad = mult_red` comparison from it.

## Deliverables

`results/PREREG_s87.md`; the calibration; the three-point table at the cell and
its neighbours; a plain statement of whether the padded comparison is degenerate
at the one cell where the unpadded one separates; `docs/s87_report.md`;
bundle + `.md5`.
