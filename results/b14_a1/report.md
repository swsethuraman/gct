# A1 — shared production-path acceptance: PASS

Revision 2 — two gaps closed after Astra's `interoperability.md` was read.

Run on the frozen batch-14 base `7a47e2b0`, integrator container, 7 GB / 2 cores.
Pre-registered at `results/PREREG_b14_a1.md` before any measurement.

## Result

**All twelve cells PASS.** Every one: operator-identical between the old and the
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
| D1 | True | True | True | 0.3290→0.1430 | 2.30 | 299.13→133.52 | 0.45 | 1,526,091 |

C3 and C5 are `ℓ = 6, δ = 10` — the family batch-14 A3 targets. X1 and X2 are
the length-9 `a = 0` cells: zero multiplicity reported as zero multiplicity with
certified full rank, not an empty kernel mistaken for a failure. D1 is `ℓ = 7`.

## The two gaps revision 1 had, and why they existed

Astra's `results/integrate/astra_reconciliation/review_only/docs/interoperability.md`
specifies a production integration gate of five items, written independently of
this run. Revision 1 covered three of them. It missed:

- **a length-7/8 positive cell** — the eleven cells covered lengths 5, 6 and 9
  only, and length 7 is where B13-09 did its degree-8 work and where half the
  remaining degree-9 frontier sits;
- **a known deficient control** — every cell in the set returned rank `= a`, so
  nothing in the run would have detected a path that *always* reports full rank.

A suite of twelve all-positive cells cannot distinguish a working rank
computation from one that has stopped computing. That is the gap Astra's
independently written spec caught and my own pre-registration did not.

**Both are now closed.** D1 above is the length-7 cell. The deficient control is
B13-08's Control C, re-run here in full:

| control | result |
|---|---|
| A — s43's two `a = 2` degree-8 records | `mult = a = 2`, both |
| B — two banked degree-10 records, field by field | `all_equal = True`, both |
| **C — diagonal pencils, both weights, both primes** | **`rank_diagonal_pencils = 0`**, `diag_all_rows_zero = true`; `det₃` rank `= a`; `per₃` rank `= a` |
| D — lean driver on the same weights | bit-identical, both |

Control C is the one that matters: diagonal pencils make `per₃` a product of
three linear forms, whose coordinate ring carries no constituent of more than
three rows, so a length-6 weight **must** read rank 0. It does, at both primes,
for `(11,6,5,3,3,2)` at `a = 5` and `(9,8,5,4,3,1)` at `a = 13` — while the same
kernels read exactly `a` on `per₃` pencils. The path can tell the difference.

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

But B13-10's headline — **1.77–2.64× less memory** — holds on **two of these
twelve cells** (C5 at 1.89×, D1 at 2.30×). On two others the lean builder saves
*nothing at all* (A1 1.00×, C1 1.01×). The headline was computed over B13-10's
larger cells and is accurate there; as a stated property of the builder it is
not. Cell size does not predict it either: X2 gets 1.70× at 998 nnz while A1
gets 1.00× at 15,678.

**A batch-14 session sizing memory from "1.77–2.64×" will under-provision.** The
honest figure is 1.00–2.30× across these twelve, cell-dependent, and the lean
builder's reliable advantage is *time*: faster on all twelve, 0.45–0.97×.

## What this does and does not establish

It says the merged production path reproduces the banked numbers on these twelve
cells, distinguishes a deficient evaluation from a full one, and that the wide
matmul is exact where the narrow one refuses to run. It
re-derives no mathematical result. It is not evidence about the 58 open
`ℓ = 6, δ = 10` cells, whose `n_χ` has never been measured because they were
never built — B13-08 reports 17 of its 95 degree-10 weights exceed `2²¹`, so
some of the 58 will need the wide path, and which ones is unknown.

**Batch 14 may launch on this path** — now against all five items of Astra's
gate, not the three revision 1 happened to cover.
