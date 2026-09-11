# A1 — shared production-path acceptance: PASS

Run on the frozen batch-14 base `7a47e2b0`, integrator container, 7 GB / 2 cores.
Pre-registered at `results/PREREG_b14_a1.md` before any measurement.

## Result

**All eleven cells PASS.** Every one: operator-identical between the old and the
lean builder, kernel verified at both house primes with every null vector
re-checked against the uncompressed int64 operator, and every evaluation rank
equal to B13-10's banked value.

| id | ident | kernel | ranks | mem old→lean | ×   | time old→lean | ×    | nnz |
|----|-------|--------|-------|--------------|-----|---------------|------|-----|
| A1 | True | True | True | 0.0257→0.0257 | 1.00 | 0.30→0.22 | 0.73 | 15,678 |
| A3 | True | True | True | 0.0451→0.0362 | 1.25 | 0.85→0.69 | 0.81 | 487,986 |
| B2 | True | True | True | 0.0383→0.0352 | 1.09 | 0.82→0.73 | 0.89 | 15,205 |
| B3 | True | True | True | 0.1234→0.0925 | 1.33 | 10.07→6.60 | 0.66 | 617,879 |
| B4 | True | True | True | 0.1458→0.1008 | 1.45 | 5.25→4.20 | 0.80 | 1,161,245 |
| C1 | True | True | True | 0.0269→0.0267 | 1.01 | 0.37→0.36 | 0.97 | 6,255 |
| C2 | True | True | True | 0.0413→0.0341 | 1.21 | 0.68→0.62 | 0.91 | 174,557 |
| C3 | True | True | True | 0.1667→0.0994 | 1.68 | 12.05→8.12 | 0.67 | 2,850,304 |
| C5 | True | True | True | 0.3953→0.2087 | 1.89 | 13.65→9.89 | 0.72 | 10,925,235 |
| X1 | True | True | — | 0.1513→0.1280 | 1.18 | 60.67→31.78 | 0.52 | 466 |
| X2 | True | True | — | 0.4051→0.2378 | 1.70 | 187.52→97.45 | 0.52 | 998 |

C3 and C5 are `ℓ = 6, δ = 10` — the family batch-14 A3 targets. X1 and X2 are
the length-9 `a = 0` cells: zero multiplicity reported as zero multiplicity with
certified full rank, not an empty kernel mistaken for a failure.

## Components the suite does not reach — 17/17

`analysis/a1_acceptance.py`, checked against **python-flint** as an independent
exact reference rather than against numpy, which is the thing under test.

- `matmul_mod_wide` exact at every seam: `K` = 1,000, `INNER_BLOCK ± 1`,
  `INNER_BLOCK`, `2²¹ − 1`, `2²¹`, `2²¹ + 1`, 3,000,000, at both house primes.
- Below the ceiling it **delegates bit-identically** to `matmul_mod`, as its
  docstring claims — verified at 524,287 / 524,288 / 524,289 and at 2,097,151.
- At and above `2²¹ = 2,097,152`, `matmul_mod` **raises AssertionError**. It
  fails loudly rather than returning a silently wrong answer, which is the one
  outcome this check exists to exclude.
- dtype discipline: int32, uint32, object, Fortran-ordered, entries shifted by
  `+p`, and negative representatives all return the int64 baseline exactly.

## One finding: the headline speedup is not a property of the builder

The ratios reproduce B13-10's own measurements cell by cell across two different
containers — 1.00/1.00, 1.24/1.25, 1.07/1.09, 1.37/1.33, 1.42/1.45, 1.00/1.01,
1.19/1.21, 1.70/1.68, 1.75/1.89, 1.16/1.18, 1.70/1.70. The instrument is stable.

But B13-10's headline — **1.77–2.64× less memory** — holds on **one of these
eleven cells**. On its own numbers for these same cells the range is 1.00–1.75×,
and on two of them the lean builder saves *nothing at all* (A1 1.00×, C1 1.01×).
The headline was computed over B13-10's larger cells and is accurate there; as a
stated property of the builder it is not. Correlation with `log₁₀ nnz` is only
+0.50 — X2 gets 1.70× at 998 nnz while A1 gets 1.00× at 15,678 — so cell size
does not predict it either.

**A batch-14 session sizing memory from "1.77–2.64×" will under-provision.** The
honest figure is 1.00–1.89× on this set, cell-dependent, and the lean builder's
reliable advantage is *time*: faster on all eleven, 0.52–0.97×.

## What this does and does not establish

It says the merged production path reproduces the banked numbers on these eleven
cells, and that the wide matmul is exact where the narrow one refuses to run. It
re-derives no mathematical result. It is not evidence about the 58 open
`ℓ = 6, δ = 10` cells, whose `n_χ` has never been measured because they were
never built — B13-08 reports 17 of its 95 degree-10 weights exceed `2²¹`, so
some of the 58 will need the wide path, and which ones is unknown.

**Batch 14 may launch on this path.**
