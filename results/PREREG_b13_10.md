# Pre-registration — B13-10, leaner raising-row construction

board_numbering: batch13
session: B13-10 (Fable) — branch `b13-10-lean-rows`
base: `main = 00495110c62acfbbbc951e82cc218ed091563b3f` (`git rev-parse main` at clone, 2026-09-09 14:5x UTC)
model that ran the session: Claude Fable 5.1 (`claude-fable-5-1`)
written 2026-09-09 15:30 UTC (11:30 America/New_York), before any measurement that this document governs.

## 0. Preflight (RECORDED)

| item | found | action |
|---|---|---|
| `python3` | 3.11.15 | — |
| `numpy`, `scipy` | 2.4.4, 1.17.1 present | — |
| `python-flint` | **missing** | `pip install python-flint` → 0.9.0 |
| `sympy` | **missing** | `pip install sympy` → 1.14.0 (mpmath 1.3.0) |
| `gcc` | /usr/bin/gcc present (the hybrid's `wk11_s71_schur.c` compiles at first use) | — |
| `Singular`, `msolve` | absent | not needed by this assignment |
| freeze markers | `docs/batch13_board.md`, `docs/batch13_corrections.md`, `docs/stocktake_batch12.md`, `docs/batch13_worker_preamble.md`, `docs/brief_wording.md` all present | — |

**Host resources, declared.**  One cloud container: 2 CPUs, 8.2 GB RAM (`MemTotal 8 216 192 kB`, 7.6 GB available at start), **no swap**, ~30 GB of writable disk.  This is the same class of box as session 79's "7 GB box", so the pilot below is a like-for-like re-run of s79's wall.  Every run of this session is bounded at launch (`timeout`, `ulimit -v`), its pid written to `results/logs/<run>.pid`.  The two CPUs are shared by everything this session runs; no other session shares this container.

One unbounded process was run before this document was written (a length-9 sizing probe, `monomials_array` at N_S ≈ 2.9·10⁷): it was killed by the box (rc 137).  Nothing was measured by it and nothing below depends on it; it is recorded because the preamble's rule was broken once.

## 1. The question

**Q1 (construction).**  Can the raising-row construction of `wk9_s45_build.raising_rows_arr` (with `monomials_array` and `orbit_setup_arr` in front of it) be re-implemented so that it returns the **same matrix `E`** — the same rows in the same order with the same integer entries, over the same χ-columns — at a materially lower peak memory, and what is the memory/work tradeoff of the choices that achieve it?

**Q2 (ceiling).**  With the leaner construction, does the cell s79 abandoned, `(10,6,6,6,2,2)₈` (`N_S = 18 337 360`, `N_S·δ = 1.47·10⁸`, `n_χ = 1 606 104`, `a = 10`), build on an 8 GB box; and if the build completes, what does the kernel phase then cost?

**What is measured going in (RECORDED from `results/logs/s79_sweep6.log`).**  s79's build of that cell: monomials + orbit setup 633 s, HWM 2.42 GB; `E_01` 3 423 455 rows / 18.0 M nnz (HWM 2.76 GB); `E_12` and `E_23` 8 688 185 rows / 35.8 M nnz each (HWM 3.76, 4.20 GB); `E_34` 3 911 695 rows / 16.1 M nnz; killed (rc −9) inside `E_45`.  Reading the current code against those numbers, the peak of each operator sits in the **target-basis canonicalisation** (`_canon_acc` on `T`: `T` as int32, its codes/order/sorted computed twice, `canon`/`acc`/`ar` as int64, and a full `np.sort(tab[T])` copy per group element), not in the CSR accumulation; the accumulated blocks (int64 data) and the final `vstack` copy add to it.  That reading is what the design below targets; it is an expectation, not a measurement, until §4 measures it.

## 2. The instrument

### 2.1 The lean builder — `analysis/wk13_b10_lean.py`

Same mathematics, same conventions, same outputs as `wk9_s45_build`; only storage and pass structure change:

- **Conventions kept verbatim.**  Monomial order = the lexicographic DFS order of `wk8_s30_core.monomials` (as `monomials_array`); exponent letters resolved by `exps(n, r)` **of the module being called** (`wk8_s30_core.exps`), never by literal; the multiset combinadic code of `wk9_s42_orbits._codes` (with `wk11_s71_codes.install()` where the caller installs it); the χ-isotypic partition, columns and signs of `orbit_setup_arr`; the raising rule `E_{i,i+1} c_α = (α_i + 1) c_{α + e_i − e_{i+1}}`; one canonical representative per `H`-orbit of target monomials with `H = Stab(λ) ∩ Stab(λ + e_i − e_{i+1})`, chi-obstructed fixed targets asserted to cancel; rows ordered as in `raising_rows_arr` (operator blocks `i = 0 … r−2` in order, rows within a block in the lexicographic order of the target basis, obstructed and empty rows removed).
- **Storage.**  `M` and every target basis in the narrowest integer dtype that holds `L − 1` (int8 / int16 / int32); `col_of` int32, `sgn` int8; codes int64 (unchanged, injectivity asserted); `canon`, `acc`, row ids int32; `E.data` int16 when the exact bound `|Stab(λ)| · δ · (n + 1) < 2¹⁵` on any summed entry holds, else int32 (the bound is asserted, and every value is also checked after the build); `E.indices` int32, `E.indptr` int32 where nnz < 2³¹.
- **Pass structure.**  (a) monomials level by level into arrays whose exact size is known before allocation (from the feasibility DP), no list-and-concatenate; (b) the stabiliser image index computed in row chunks (no full `np.sort(tab[M])` copy); (c) per operator: the target codes computed once, canonicalisation in chunks, then `T` and its index arrays freed before the raising pass, leaving one sorted code table plus one row-id table; (d) the raising triples stored compactly (`rid` int32, `col` int32, `val` int8) per chunk and turned into CSR by a counting sort — or, with `triples='recompute'`, not stored at all and generated twice (once to count, once to fill); (e) duplicates summed in place, obstructed/empty rows removed by re-indexing `indptr` only (they have zero length by then); (f) blocks either kept in memory and concatenated once into preallocated arrays, or written to a scratch directory as they complete and assembled at the end (`blocks='memory' | 'disk'`).
- **Knobs exposed** (the memory/work tradeoff): `chunk` (source rows per pass), `triples` (`store` / `recompute`), `blocks` (`memory` / `disk`).  The default is `chunk = 400 000`, `triples = 'store'`, `blocks = 'memory'`; §4 measures the alternatives on the large cells.
- **Consumers.**  `E.data` narrower than int64 breaks two lines of `wk11_s71_hybrid` under NumPy 2 (`int16_array % 2147483647` raises `OverflowError`, checked here).  The lean module therefore also provides `hybrid_kernel_lean`, a wrapper around the unchanged `wk11_s71_hybrid.hybrid_kernel` that presents the compact `E` with its data upcast only where the hybrid touches it.  The hybrid's own arithmetic, cover, projection, lifting and verification are not modified; `wk11_s71_hybrid.py` is not edited.

### 2.2 The measurement harness — `analysis/wk13_b10_run.py`, `analysis/wk13_b10_suite.py`

Every build is its own subprocess (so that `VmHWM` is that build's peak and nothing else's), launched with `timeout` and `ulimit -v`, pid written to `results/logs/b13_10_<run>.pid`.  Each run records: `VmHWM` after imports (baseline) and at exit (peak), wall seconds per phase (monomials, orbits, rows per operator, assembly), `N_S`, `|Stab|`, `n_χ`, rows, nnz, and writes `E` (indptr/indices/data, compact) and `arr` (`M`, `col_of`, `sgn`) to a scratch directory for the comparison step.  The comparison step loads both matrices and tests, in this order:

1. **exact operator agreement**: same shape, same `indptr`, same `indices`, same `data` (as integers) — `E_new` and `E_old` identical as CSR after `sort_indices()`; same `col_of`, `sgn`, `M` (as integers) from the orbit setup;
2. if 1 fails: **equivalent row space** by row-multiset equality (each row as a canonical tuple of `(col, value)` pairs, compared as multisets) — reported as a deviation, never silently accepted;
3. **kernel**: `hybrid_kernel_lean` on `E_new` at both house primes, `nullity = a` (`a` from `wk9_s42_census.a_weyl`), and every kernel vector verified against **`E_old`** (`check_kernel_mat(E_old, K, p)` on the uncompressed int64 operator), and the kernel's rank `= a` (`rank_tall`);
4. **evaluation ranks** as the additional check: `mult_det` (and for `n = 3` the `per_3` multiplicity; for `n = 4` also `mult_pad`, `mult_per4`, `mult_red` where banked) at both primes on the recorded point families (the drivers' seeds: det 11, red 29, pad 37, per4 47, per3 41; bound 40; `K = a + 8`), compared with the banked values.

A check that cannot place one of its targets **fails**; nothing is skipped.

### 2.3 The pilot — `(10,6,6,6,2,2)₈`

The lean builder in one bounded subprocess: `timeout 14400`, `ulimit -v 7 800 000` (kB), pid recorded, phases logged with `VmHWM` after each operator, `E` written to scratch on completion.  If the build completes: `hybrid_kernel_lean` at the first prime with `S71_MEM_X = 2.5·10⁸`, the same bounds, then the second prime; `mult_det` at both primes if a kernel is obtained (`a = 10`, det pencils seed 11, `K = 18`).  If time allows, one intermediate unbanked cell between `N_S·δ = 3·10⁷` and `1.5·10⁸`, taken from `results/s79_queue.json` in `N_S·δ` order, for a middle point on the curve; that choice is made after the suite and is recorded in a dated addendum before it runs.

## 3. The objects — the representative suite

Eighteen banked cells (`n_χ` from 116 to 1 660 777; `n = 3` and `n = 4`; lengths 5, 6, 7), chosen from the record before any build here, spanning stabiliser sizes 1 to 120, degrees 6 to 14, and every column the record carries.  Banked values are quoted from `results/s60_cells.jsonl`, `results/s71_sweep.jsonl`, `results/s79_cells.jsonl`, `results/s79_per6.jsonl`, `results/s69_sizes.jsonl`.

| id | n | cell | a | N_S | Stab | n_χ | N_S·δ | banked (both primes) | source |
|---|---|---|---|---|---|---|---|---|---|
| A1 | 4 | (13,5,2,2,2)₆ | 2 | 3 672 | 6 | 825 | 2.2·10⁴ | det 2, red 2 | s60 |
| A2 | 4 | (37,13,4,1,1)₁₄ | 71 | 35 626 | 2 | 13 252 | 5.0·10⁵ | det 71, red 71, per4 71 | s71 |
| A3 | 4 | (28,8,5,2,1)₁₁ | 99 | 52 033 | 1 | 52 033 | 5.7·10⁵ | det 99, red 99, per4 99 | s71 |
| A4 | 4 | (26,7,5,5,1)₁₁ | 64 | 391 708 | 2 | 193 330 | 4.3·10⁶ | det 64, **red 63**, per4 64 | s71 |
| B1 | 4 | (38,2,2,2,2,2)₁₂ | 1 | 8 269 | 120 | 200 | 9.9·10⁴ | det/pad/red/per4 1 | s79 |
| B2 | 4 | (29,9,3,1,1,1)₁₁ | 1 | 29 504 | 6 | 1 816 | 3.2·10⁵ | all 1 | s79 |
| B3 | 4 | (33,7,2,2,2,2)₁₂ | 12 | 213 637 | 24 | 13 518 | 2.6·10⁶ | all 12 | s79 |
| B4 | 4 | (24,13,3,2,1,1)₁₁ | 45 | 272 982 | 2 | 108 267 | 3.0·10⁶ | all 45 | s79 |
| B5 | 4 | (11,7,6,6,1,1)₈ | 12 | 2 634 255 | 4 | 553 842 | 2.1·10⁷ | det 12, **pad 9, red 9**, per4 12 | s79 |
| B6 | 4 | (12,8,6,2,2,2)₈ | 37 | 3 070 640 | 6 | 586 482 | 2.5·10⁷ | all 37 | s79 |
| B7 | 4 | (13,9,9,3,1,1)₉ | 70 | 3 503 556 | 4 | 732 815 | 3.2·10⁷ | det 70, **pad 45, red 45**, per4 70 | s79 |
| C1 | 3 | (17,2,2,2,2,2)₉ | 1 | 4 743 | 120 | 116 | 4.3·10⁴ | per3 mult 1 | s79 per6 |
| C2 | 3 | (12,5,5,3,1,1)₉ | 4 | 48 161 | 4 | 9 472 | 4.3·10⁵ | mult 4 | s79 per6 |
| C3 | 3 | (11,8,5,2,2,2)₁₀ | 14 | 528 663 | 6 | 104 651 | 5.3·10⁶ | mult 14 | s79 per6 |
| C4 | 3 | (5,5,5,5,5,2)₉ | 1 | 3 020 230 | 120 | 23 907 | 2.7·10⁷ | mult 1 (467 s build in s79) | s79 per6 |
| C5 | 3 | (10,7,6,4,2,1)₁₀ | 21 | 816 940 | 1 | 816 940 | 8.2·10⁶ | mult 21 | s79 per6 |
| C6 | 3 | (7,6,5,4,3,2)₉ | 2 | 1 660 777 | 1 | 1 660 777 | 1.5·10⁷ | mult 2 (whole-cell HWM 5.07 GB in s79) | s79 per6 |
| D1 | 3 | (19,7,2,2,2,2,2)₁₂ | 6 | 1 155 302 | 120 | 17 047 | 1.4·10⁷ | kernel dim 6, **det rank 5, i_det = 1** | s69 (sparse-det instrument) |

Exploratory, not banked, operator agreement only (`E_old` vs `E_new`, plus `nullity = a`): **X1** `n = 3`, `(10,1⁸)₆` (`a = 0`, `N_S = 2 751`, `L = 165`) and **X2** `n = 4`, `(16,1⁸)₆` (`a = 0`, `L = 495`) — the two length-9 cells exercise the int16 letter dtype; **X3** the pilot cell.

**A defect in the assignment, recorded here rather than worked around.**  The board asks for banked cells at "lengths 5, 6 and 9 where banked cells exist".  A scan of every `results/**/*.json*` file finds **no cell of length ≥ 8 that the raising-row builder has ever built** (no record with `n_χ`/`nrows` and a `λ` of eight or more parts); the length-9 objects in the tree (`(65,17,2⁷)₂₄`, `(21,17,2⁷)₁₃`, the fifteen cubic predecessors at `N_S ≥ 1.6·10⁷`) were reached by other routes or not at all, and every length-9 cubic weight through δ = 7 has `a = 0`.  The suite therefore substitutes the banked length-7 positive control D1 and two `a = 0` length-9 operator checks, and says so.

## 4. What is measured, and the predictions

**M1 — exact agreement.**  `E_new ≡ E_old` on all 18 + 2 cells.  Prediction P1 (0.8): identical on every cell at the first attempt; if a cell differs, the row-multiset check of §2.2(2) decides whether it is a row-order or a value defect, and the defect is fixed and *all* cells re-run under a dated addendum.

**M2 — kernel.**  On every banked cell with `a ≥ 1`, `hybrid_kernel_lean(E_new)` returns `a` vectors at both primes, each verified on `E_old`.  P2 (0.9).

**M3 — evaluation ranks.**  Banked values reproduce at both primes on all 18 cells, including the four reducible/padded drops (A4 red 63, B5 pad/red 9, B7 pad/red 45) and D1's `det rank 5`.  P3 (0.85).  A mismatch is a defect of the lean pipeline *or* of the point reconstruction; it is investigated, not banked.

**M4 — the memory curve.**  For each suite cell and each builder: peak `VmHWM` above the import baseline, and wall time per phase, in `results/b13_10/memcurve.jsonl`; a fit `peak ≈ α·N_S·δ + β·nnz(E) + γ·N_T,max` per builder.  P4 (0.7): on the four largest cells (B6, B7, C6, C4) the lean builder's peak is at most **half** of the old builder's, at a time cost at most 1.5× with `triples='store'`; P4′ (0.6): `triples='recompute'` halves the raising-phase peak again at about 2× the raising time.

**M5 — the pilot.**  P5 (0.6): the lean build of `(10,6,6,6,2,2)₈` completes under 7.8 GB, with peak below 2.5 GB; P6 (0.4): a verified kernel at both primes is then obtained within the same bounds (the hybrid at `n_χ = 1.6·10⁶` is expected to need 1–3 GB beyond `E` at `S71_MEM_X = 2.5·10⁸`, from the record's whole-cell peaks at C5/C6).

## 5. Stopping rules

- Suite builds: `timeout 1800 s` and `ulimit -v 7 000 000 kB` per subprocess for the old builder, `3600 s` for the lean one (the old builder's banked build times are ≤ 105 s; the margin is for this box).  A suite cell whose old build cannot finish inside the bound is reported as such with the lean result alone.
- Pilot: `timeout 14400 s`, `ulimit -v 7 800 000 kB`, build first; the kernel phase only after a completed build, under the same bounds per prime.
- The suite runs alone on the box except where a run's predicted peak (from the record) plus the concurrent run's is below 6 GB; the pilot runs alone.
- Any run that must be ended early is ended by the pid in `results/logs/b13_10_<run>.pid`.
- Hard stop for measurements at 20:00 America/New_York; report and bundle by 20:30.

## 6. What counts as a negative

- **A construction negative:** the lean builder's peak is not below the old builder's on the large cells (M4 fails), or exact agreement fails and cannot be restored (M1).  Then the deliverable is the measured curve, the identified allocation, and the priced remaining bottleneck (the fallback the board names).
- **A ceiling negative:** the pilot build does not complete under the bound.  Then the construction ceiling of this box is stated as the largest completed `N_S·δ` with its peak, and the wall cell is priced by extrapolating the lean curve (with the fit's residual stated).
- **A kernel negative:** a build that completes but a kernel phase that does not fit.  Then the allocation that fails is named with its size, from the hybrid's own logged phases.
- A sampled rank is never promoted: every `mult` here is a rank at a prime, and equality with `a` at one prime proves `mult = a` over `Q`; a drop reproduces a *measured* record value and proves nothing new.  No decision-table branch is entered anywhere in this session; the kernel vectors are verified objects, the ranks are floors.
- Anything not listed above is exploratory and will be labelled so.

Author: Swami Sethuraman, swsethuraman@beneficus.ai, Beneficus AI.
board_numbering: batch13

## Addendum A — 2026-09-09 15:35 UTC (11:35 America/New_York), before the cells it governs ran

1. **The two exploratory length-9 cells are replaced.**  `(10,1⁸)₆` and `(16,1⁸)₆` have `n_χ = 0` (the sign character on eight equal parts empties the isotypic part; verified here in a 40 320-element stabiliser loop), so they check nothing.  X1 is now `n = 3`, `(11,4,2,2,1⁵)₈` (`a = 0`, `N_S = 247 436`, `|Stab| = 240`, `L = 165`) and X2 is `n = 4`, `(15,4,2,2,1⁵)₇` (`a = 0`, `L = 495`); both are operator-agreement checks with `a = 0` (the hybrid then certifies full column rank), exploratory as before.  Every length-9 cubic weight through δ = 8 that was priced has `a = 0`.
2. **Instrument detail.**  The suite is run by `analysis/wk13_b10_suite.py`; the large cells (B5, B6, B7, C4, C5, C6, D1, X1, X2) each in their own driver process so that the driver's `VmHWM` is that cell's consumer-side peak (old `E` loaded as int64 + lean `E` + hybrid + evaluation rows); the small cells in one loop.  Both loops bounded (`ulimit -v 7 000 000`, `timeout 7200 / 3600` per driver), pids in `results/logs/b13_10_suiteA.pid`, `b13_10_suiteB.pid`, and one pid file per build subprocess.  The consumer runs with `S71_MEM_X = 2.5·10⁸` as session 79 did.
3. **The tradeoff variants** run on B6, B7, C5, C6 only: `(recompute, memory, 400 000)`, `(store, disk, 400 000)`, `(recompute, disk, 200 000)`, each a separate bounded build, each checked identical to the old operator.
4. Three cells (A1, B2, C1) were run once as a smoke test of the driver before this addendum (all PASS, identical operators); they are re-run in the loop and the smoke records are discarded.
