# s80 — the raising-row builder, and the record

`board_numbering: batch13`.  Read `docs/batch13_worker_preamble.md` first.

## Mission

Two of batch 13's six open questions are blocked by the same wall, and it is not
the one anybody assumed.  Remove it.  Then bring the negative record current.

## Task 1 — a leaner raising-row builder

**The wall, measured.**  Session 79 abandoned `(10,6,6,6,2,2)₈` at
`N_S·δ = 1.47·10⁸` with the raising rows exceeding 4 GB in the build, killed at
`E_45`.  Its *kernels* were never the constraint: the largest hybrid phase in
682 cells was 202 s at `n_χ = 732 815`.  So the wall is
`wk9_s45_build.build_cell`'s row construction, and it blocks

- `I(D₉^{per₃})₁₃` (s83): fifteen weights, `a` only 1 to 9, but `N_S` from
  `1.59·10⁷` to `3.70·10⁸`, so `N_S·δ` from `2.1·10⁸` to `4.8·10⁹`;
- the balanced six-row cells (s86): `n_χ ≥ 10⁶`, `N_S·δ ≥ 10⁸`.

**What to build.**  The raising rows in blocks — streamed to disk, or accumulated
sparsely, or generated on demand for the elimination that consumes them —
with a **stated peak-memory model** as a function of `N_S`, `δ` and `r`.  You
choose the mechanism; the brief asks for the ceiling, not a particular design.

**Acceptance, all of it:**

1. entry-for-entry agreement with the existing builder on **at least fifteen
   banked cells** spanning `n_χ` from `10³` to `10⁶`, both `n = 3` and `n = 4`,
   and lengths 5, 6 and 9 where banked cells exist;
2. the same `mult_det` at those cells, both primes;
3. a measured `N_S·δ` ceiling in this box with the memory curve behind it,
   reported as a number;
4. the ceiling demonstrated: one cell above the old wall built and its rank read.
   `(10,6,6,6,2,2)₈` is the natural candidate.

**Falsifier.**  Any disagreement with the existing builder on a banked cell:
stop, report, and no later session runs on the new builder.  Say so plainly —
the batch is sequenced on your answer.

## Task 2 — extend `negative_record()`

`analysis/wk9_s57_lib.negative_record()` reads the ledgers of sessions 36–54 and
stops.  It holds 326 cells.  Sessions 57, 60, 63, 71, 74 and 79 measured cells it
does not carry — s60's `(19,6,3,3,1)₈` and `(19,4,4,3,2)₈`, for two — so every
cross-reference against it understates what is closed.  Add 55–79.

**Acceptance:** the count rises from 326; no ledger disagreement raised by the
existing consistency check; and `analysis/wk12_int_w13_census.py` re-run prints a
corrected open-on-both-instruments frontier at every `a_∞` level.  Report the
before-and-after frontier table.

## Pre-registration

`results/PREREG_s80.md` before any code: the design you will try, the fifteen
calibration cells by name, the acceptance thresholds above, and what you will
report if the ceiling does not move.

## Deliverables

The builder and its tests; `results/s80_builder_calibration.json` (the fifteen
cells, both builders, both primes, entry-for-entry); the ceiling and memory
curve; the extended `negative_record()` and the corrected frontier table;
`docs/s80_report.md`; bundle + `.md5`, parts from `part00`.
