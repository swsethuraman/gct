# PREREG — A1, the shared production-path acceptance

Committed before any measurement. Integrator run, on the frozen batch-14 base
`7a47e2b0`.

## Question

Batch 13 merged twelve branches with zero conflicts. **A conflict-free merge
proves the text does not collide; it does not prove the composition runs.** The
lean builder (B13-10), `matmul_mod_wide` (B13-08) and the dtype fixes (B13-09)
were each written and tested in a different isolated container, each against the
*old* path. No one has run them together.

Does the merged tree still produce the banked numbers?

## Instrument

`analysis/wk13_b10_suite.py`, unmodified, at `7a47e2b0`. For each cell it runs
the old builder and the lean builder in separate bounded subprocesses, then
checks:

1. **operator agreement** — `E_old == E_new` on indptr, indices and data, plus
   `M`, `col_of`, `sgn`, `n_chi` from the orbit setup;
2. **kernel** — `hybrid_kernel_lean` on `E_new` at both house primes, nullity
   `= a`, and **every** null vector re-verified against `E_old`, the
   uncompressed int64 operator;
3. **evaluation ranks** — on the drivers' recorded point families and seeds,
   compared against the banked record.

Plus `analysis/a1_acceptance.py` (written for this run) for the two components
the suite does not reach: the wide matmul across the 16-bit-limb ceiling, and
dtype discipline at the consumer boundary.

## Benchmark set — eleven cells, chosen before running

`A1, A3, B2, B3, B4, C1, C2, C3, C5, X1, X2`

Covering the quartic side (A, B), the cubic side (C), **degree 10 at length 6**
(C3, C5 — the family batch-14 A3 targets), and the **`a = 0` zero-multiplicity**
case (X1, X2, length 9). Banked total ≈ 680 s on a box of this class.

## Expectations, labelled before measurement

- **Expected**: all eleven PASS, `identical = True`, `kernel_ok = True`, ranks
  matching the banked record. B13-10 ran every one of them twice and banked PASS.
- **What would falsify the premise that the merge is safe**: any cell where
  `identical` is False, or `kernel_ok` is False, or a rank differs from the
  banked value. Any one of those means the merged path computes something the
  component paths did not, and batch 14 does not launch on it.
- **`matmul_mod_wide`**: correct against exact integer arithmetic at `K` both
  below and above `2²¹ = 2,097,152`.
- **`matmul_mod`**: correct below the ceiling, and **fails loudly above it**.
  A silent wrong answer there is the worst outcome available and is the thing
  this check exists to exclude.
- **`a = 0`**: X1 and X2 must report zero multiplicity and certified full rank,
  not an empty kernel mistaken for an error.

## Stopping rules

- Any FAIL: stop, do not continue the set, report the cell and the mismatch.
- A cell exceeding 6 GB or 1,800 s: record as BOUNDED, continue to the next.
- The run is bounded with `timeout` and `ulimit -v`; the pid is recorded to
  `results/logs/b14_a1.pid` and the run is ended only by that recorded id.

## What a PASS does and does not establish

A PASS says the merged production path reproduces the banked numbers on these
eleven cells. It does not re-derive any mathematical result, and it is not
evidence about cells outside the set — in particular not about the 58 open
`ℓ=6, δ=10` cells, whose `n_χ` has never been measured because they were never
built.
