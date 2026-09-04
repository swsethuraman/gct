# Session 45 — validation

Branch `s45-sparsedet`, clone tip `0c229c1`.  Pre-registration
`results/PREREG_s45.md` (commit `bbd7d06`, before any measurement); the battery
below is exactly the one pre-registered there (§2), with the pre-registered
expected outcome in every case.  Both house primes `P1 = 2147483647`,
`P2 = 2147483629` throughout; the lifts add
`2147483587, 2147483579, 2147483563`.  Raw records:
`results/s45_v5.jsonl`, `results/s45_v2.jsonl`, `results/s45_v3.jsonl`,
`results/s45_v4.json`; logs under `results/logs/`.

## 0. Verdict

> **All five parts pass, with no exception and no retry that changed a
> verdict.**  The part that decides the session is **V2**: a route that answered
> "full column rank" unconditionally would pass every determinant-side test in
> the repository, because `mult_det = a` at every cell the programme has ever
> measured.  V2 is six cells where the answer is **not** full rank, and the
> sparse route returns the drop at every one, with an exhibited rational vector
> verified over `Z` and against Theorem (★).  V3 then reproduces **all 14**
> determinant-side `D = 0` rows of `results/s41_ledger.md`, up to and including
> the session-41 frontier cell `(12,9,3,2,1,1)_7` — which took session 41
> **2500 s and 4.68 GB** and takes this route **62 s at `O(nnz)` memory**.

| # | test | pre-registered expectation | outcome |
|---|---|---|---|
| V1 | `l^3 m` witness + the 48-cell battery (`analysis/wk8_s30_calib.py` as-is) | `CALIBRATION PASSED`, kernel `(12,−3,1)`, `mult = 0` | **PASS** — all five lines, 41/48 discriminating |
| V2 | all six pad-side bites, drop returned, vectors verified | the drop at both primes; `E v = 0`; (★) | **PASS** 6/6 |
| V3 | ≥ 8 banked det-side `D = 0` rows | `nullity_p([E; ev]) = 0` at every one | **PASS** 14/14 |
| V4 | 200 synthetic sparse matrices, planted nullity 0–6, vs `python-flint` | 200/200 | **PASS** 200/200 (+ 100/100 on the s45 level set) |
| V5 | the memory-lean build against the s36/s42 build | identical at every cell | **PASS** 16/16 |

## 1. V1 — the witness and the discriminating battery *(proved / measured)*

`analysis/wk8_s30_calib.py` run unmodified (`results/logs/s45_v1_calib.log`):

```
PASS witness {l^3 m} lam=(4,4) delta=2 : mult = 0
PASS witness kernel == (12,-3,1)
PASS discriminating battery: 48 World A cells, 41 with mult < a
PASS session 26's five cells
PASS mult_det = a at all 20 weights, n=3, delta<=4

CALIBRATION PASSED
```

The corrected raising rule is what makes the witness kernel `(12, −3, 1)` and
`mult = 0`; the wrong rule gives `(1, −4, 3)` and `mult = 1`.  41 of the 48
World A cells have `mult < a`, so the battery is dominated by non-full-rank
answers.

## 2. V5 — the memory-lean build is the same object *(proved by direct comparison)*

For each cell: (a) the monomial array equals `wk8_s30_core.monomials` in content
**and order**; (b) the orbit partition and the twisted signs equal
`wk9_s42_orbits.orbit_setup_fast`'s up to the per-orbit global sign (a
basis-vector convention no rank depends on) — so identical `n_χ`, identical
orbits, identical column map up to a permutation and a sign per column;
(c) `wk9_s45_build.raising_rows_arr` has the same row count, the same `nnz` and
the same obstructed-row count as **both** `wk9_s36_stabred.reduced_rows` and
`wk9_s42_orbits.reduced_rows_fast`, and the same **row space** (flint rank of
each and of the stack, after undoing the column permutation and signs) wherever
`n_χ ≤ 1600`; (d) the vectorised `χ`-coordinate evaluation rows equal
`wk9_s36_stabred.point_rows` **entrywise** on the same random stream, on the det
and the pad points.  `analysis/wk9_s45_validate.py`.

| λ | δ | `N_S` | \|Stab\| | `n_χ` | rows | `nnz` | obstructed | row space |
|---|---|---|---|---|---|---|---|---|
| `(8, 4, 4, 4, 4)` | 6 | 94675 | 24 | 4562 | 136845 | 425759 | 0 | sizes equal (rank check skipped, n_chi > 1600) |
| `(10, 8, 7, 1, 1, 1)` | 7 | 75689 | 6 | 5740 | 17190 | 58992 | 12951 | sizes equal (rank check skipped, n_chi > 1600) |
| `(11, 11, 2, 2, 1, 1)` | 7 | 26710 | 8 | 2806 | 18757 | 58275 | 2548 | sizes equal (rank check skipped, n_chi > 1600) |
| `(4, 4, 4, 4, 4)` | 5 | 19834 | 120 | 264 | 12496 | 35596 | 0 | equal (rank 263) |
| `(22, 2, 2, 2, 2, 2)` | 8 | 8253 | 120 | 197 | 5797 | 10816 | 0 | equal (rank 196) |
| `(9, 9, 8, 1, 1)` | 7 | 20299 | 4 | 3969 | 17072 | 69475 | 2166 | sizes equal (rank check skipped, n_chi > 1600) |
| `(8, 8, 8, 2, 2)` | 7 | 127004 | 12 | 11778 | 169257 | 685533 | 0 | sizes equal (rank check skipped, n_chi > 1600) |
| `(12, 4, 4, 4, 4)` | 7 | 205616 | 24 | 9738 | 292567 | 933637 | 0 | sizes equal (rank check skipped, n_chi > 1600) |
| `(13, 5, 4, 1, 1)` | 6 | 1824 | 2 | 658 | 1592 | 4658 | 180 | equal (rank 656) |
| `(10, 10, 2, 2, 2, 2)` | 7 | 201554 | 48 | 6269 | 147220 | 358162 | 0 | sizes equal (rank check skipped, n_chi > 1600) |
| `(12, 10, 3, 1, 1, 1)` | 7 | 19488 | 6 | 1282 | 4357 | 11294 | 3528 | equal (rank 1281) |
| `(19, 5, 5, 1, 1, 1)` | 8 | 19664 | 12 | 645 | 3957 | 10155 | 3097 | equal (rank 644) |
| `(21, 3, 2, 2, 2, 2)` | 8 | 19634 | 24 | 1366 | 27850 | 54609 | 0 | equal (rank 1365) |
| `(16, 10, 3, 1, 1, 1)` | 8 | 28410 | 6 | 1850 | 6173 | 16243 | 5187 | sizes equal (rank check skipped, n_chi > 1600) |
| `(11, 9, 2, 2, 2, 2)` | 7 | 192776 | 24 | 11538 | 255176 | 567001 | 0 | sizes equal (rank check skipped, n_chi > 1600) |
| `(12, 12, 2, 2, 2, 2)` | 8 | 424582 | 48 | 12942 | 306134 | 764934 | 0 | sizes equal (rank check skipped, n_chi > 1600) |

Row counts and `n_χ` agree with `results/s41_ledger.md` wherever a cell appears
there (e.g. `(12,10,3,1,1,1)_7`: `n_χ = 1282`, rows `4357`;
`(11,9,2,2,2,2)_7`: `11538`, `255176`; `(12,12,2,2,2,2)_8`: `12942`, `306134`).

## 3. V4 — Berlekamp–Massey and the whole sparse route on synthetic matrices *(measured)*

`analysis/wk9_s45_v4.py`.  Battery A is `wk9_s42_sparse.selftest` as written
(s42's own level set); battery B runs the same generator through the level set
this session actually uses, `((3,2), (12,2), (None,1))`, with a pinned dense
block standing in for the evaluation rows.  Nullities are planted 0–6 (the
realised nullity is whatever the construction gives and is read from a flint
rank of the dense matrix, not from the plant).  Every reported kernel vector is
re-verified by a sparse product.

| battery | levels | matrices | agreement with `python-flint` |
|---|---|---|---|
| A | s42 default ((12,2),(None,1)) | 200 | **200/200** |
| B | s45 'cheap' ((3,2),(12,2),(None,1)) + pinned dense rows | 100 | **100/100** |

## 4. V2 — every pad-side bite the programme has *(the discriminating test)*

`analysis/wk9_s45_v23.py` → `analysis/wk9_s45_lift.py`.  Each cell is measured
on the pad side at true padded-permanent points (`per_padded(3,4)` through
`restrict()`) at **five** primes; the two house primes must agree on the
nullity, the kernel is put in canonical RREF at each prime, the pivot columns
are asserted equal across primes, the entries are CRT'd and rationally
reconstructed, and the resulting integer vectors are verified **over `Z`**
(python integers, no modular arithmetic) against every raising-operator row,
and checked for independence by a flint rank.  Theorem (★) is then checked on
**every monomial in the support**.

| λ | δ | `a` | ledger `mult_pad` | `n_χ` | `nnz` | nullity | `mult_pad` | exact vectors | max \|coeff\| | support | (★) | primes | s |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| `(8, 4, 4, 4, 4)` | 6 | 2 | 1 | 4562 | 425759 | 1 | 1 | 1 | 41472 | 1021 | yes | 5 | 102.1 |
| `(9, 9, 8, 1, 1)` | 7 | 2 | 1 | 3969 | 69475 | 1 | 1 | 1 | 2880 | 3323 | yes | 5 | 33.6 |
| `(8, 8, 8, 2, 2)` | 7 | 3 | 2 | 11778 | 685533 | 1 | 2 | 1 | 276480 | 9283 | yes | 5 | 256.7 |
| `(12, 4, 4, 4, 4)` | 7 | 4 | 3 | 9738 | 933637 | 1 | 3 | 1 | 41472 | 1021 | yes | 5 | 519.8 |
| `(10, 8, 7, 1, 1, 1)` | 7 | 3 | 2 | 5740 | 58992 | 1 | 2 | 1 | 768 | 2724 | yes | 5 | 60.4 |
| `(13, 10, 6, 1, 1, 1)` | 8 | 9 | 8 | 10682 | 111832 | 1 | 8 | 1 | 1280 | 4708 | yes | 5 | 278.3 |

Every drop is the one banked in `results/s36_ledger.md` / `results/s41_ledger.md`;
every exhibited vector satisfies `E v = 0` over `Z` and (★) on all of its
support, so at each of these cells `mult_pad = a − 1` is **proved on both
sides**, not measured.  `(13,10,6,1,1,1)_8` — session 41's `D = −1` bite, and
the largest of them — reproduces with a vector of 4708 monomials and
coefficients bounded by 1280.

## 5. V3 — the banked determinant side, reproduced sparsely *(proved)*

`analysis/wk9_s45_v23.py`.  Every `D = 0` row of `results/s41_ledger.md` — all
14, not the 8 required — measured on the determinant side by
`nullity_p([E; ev_det])` at both house primes.  `a` is the plethysm value and is
additionally asserted equal to the full-`E` nullity at the 11 cells where that
is affordable.  Column `level` is the compression level that produced the
verdict (0 = `(3,2)`, 1 = `(12,2)`, 2 = uncompressed).

| λ | δ | `n_χ` | `nnz` | `a` | full-`E` nullity | nullity `[E; ev]` | `mult_det` | ledger | level | s | HWM GB |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `(22, 2, 2, 2, 2, 2)` | 8 | 197 | 10816 | 1 | 1 | 0 | 1 | 1 | [0] | 51.0 | 0.8 |
| `(19, 5, 5, 1, 1, 1)` | 8 | 645 | 10155 | 1 | 1 | 0 | 1 | 1 | [0] | 0.7 | 0.8 |
| `(12, 10, 3, 1, 1, 1)` | 7 | 1282 | 11294 | 1 | 1 | 0 | 1 | 1 | [0] | 9.3 | 0.87 |
| `(16, 10, 3, 1, 1, 1)` | 8 | 1850 | 16243 | 2 | 2 | 0 | 2 | 2 | [0] | 2.1 | 0.87 |
| `(20, 4, 2, 2, 2, 2)` | 8 | 2725 | 113571 | 3 | 3 | 0 | 3 | 3 | [1] | 15.7 | 0.88 |
| `(12, 12, 5, 1, 1, 1)` | 8 | 3923 | 69601 | 3 | 3 | 0 | 3 | 3 | [0] | 15.0 | 0.9 |
| `(15, 7, 7, 1, 1, 1)` | 8 | 3985 | 77773 | 5 | 5 | 0 | 5 | 5 | [0] | 21.1 | 0.9 |
| `(12, 10, 2, 2, 1, 1)` | 7 | 5282 | 72243 | 1 | 1 | 0 | 1 | 1 | [0] | 11.6 | 0.9 |
| `(14, 9, 6, 1, 1, 1)` | 8 | 9159 | 93392 | 10 | 10 | 0 | 10 | 10 | [0] | 209.6 | 0.91 |
| `(13, 10, 6, 1, 1, 1)` | 8 | 10682 | 111832 | 9 | 9 | 0 | 9 | 9 | [0] | 247.1 | 0.91 |
| `(11, 9, 2, 2, 2, 2)` | 7 | 11538 | 567001 | 1 | 1 | 0 | 1 | 1 | [1] | 216.7 | 0.93 |
| `(12, 12, 2, 2, 2, 2)` | 8 | 12942 | 764934 | 5 | — | 0 | 5 | 5 | [1] | 173.1 | 0.89 |
| `(12, 8, 3, 3, 1, 1)` | 7 | 18716 | 306938 | 5 | — | 0 | 5 | 5 | [0] | 63.1 | 0.9 |
| `(12, 9, 3, 2, 1, 1)` | 7 | 19985 | 199780 | 5 | — | 0 | 5 | 5 | [0] | 62.1 | 0.9 |

Every row agrees with the banked dense answer, at both primes, with
`nullity_p = 0` — so at each of these 14 cells `mult_det = a` is **proved** by a
single-prime certificate, independently of session 41's dense computation.

**The cost comparison that motivates the session.**  `(12,9,3,2,1,1)_7`,
`n_χ = 19,985`, was session 41's frontier and its most expensive cell: **2500 s
and 4.68 GB** by the dense in-place `rref`.  Here: **62 s**, peak resident
0.90 GB, of which the raising-operator build is 0.4 s and 0.1 GB — the rest is
interpreter and library.  `(12,8,3,3,1,1)_7` (`n_χ = 18,716`) falls from 1857 s
and 4.17 GB to 63 s.

## 6. What the battery does not cover

The certificates are one-sided by construction and the session's honest boundary
is the same as session 42's.  `nullity_p = 0` proves `mult = a`; a positive
nullity is a measurement until its kernel is exhibited and verified, which V2
does at six cells and the sweep does at any cell that shows one.  The row
sampling of levels 0 and 1 is rigorous only in the direction that matters
(sampling can only lose rank, so a nonsingularity certificate at any level
proves the full matrix injective); a kernel vector found at a compressed level is
never reported until it is checked against the **full** `[E; ev]`, and V2's six
cells are exactly the population where that check is exercised — it fired and
escalated correctly at `(8,4,4,4,4)_6` and at the full-`E` checks of the sweep.
Berlekamp–Massey remains the one hand-written exact routine; V4 is its
validation, and its output is additionally checked inside the C helper to
annihilate the whole sequence before any verdict is emitted.
