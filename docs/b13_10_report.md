# B13-10 — a leaner raising-row construction

board_numbering: batch13
session B13-10 (the board's Fable slot), branch `b13-10-lean-rows` off
`main = 00495110c62acfbbbc951e82cc218ed091563b3f`, pre-registration
`results/PREREG_b13_10.md` committed at `77ad539` before any measurement,
addendum A committed at `e5c29c5` before the cells it governs.  Delivery is by
git bundle in **one part** (`part00` does not appear: the bundle is a single
file, `b13_10_lean_rows.bundle`, with `b13_10_lean_rows.bundle.md5` naming the
bare filename).  No push was attempted.

**Models.**  This session was dispatched to Claude Fable 5.1 and ran under
`claude-fable-5-1` through commit `e5c29c5`; the model was then switched to
`claude-opus-5` mid-session and commits from `0995fff` onward carry
`Co-Authored-By: Claude Opus 5`.  Both trailers are truthful for the commits
that carry them; no commit claims a model that did not write it.

Labels: **PROVED** (a theorem, or a full rank at one prime, which proves the
statement over `Q` by `rank_p ≤ rank_Q`), **CERTIFIED** (an exhibited object
re-checked on an independent instrument here), **MEASURED** (computed here,
exact mod both primes), **ADOPTED** (a convention taken from the tree),
**RECORDED** (a cost, a size, or an event).

---

## 0. Verdict

> **The construction is bit-identical and materially leaner, and the wall is
> gone.**
>
> **CERTIFIED.**  On every cell run — 18 of the 18 banked cells of the pre-registered suite, plus the 2 exploratory length-9 cells — the lean builder returns the
> **same matrix**: same shape, same `indptr`, same `indices`, same integer
> `data`, and the same `M`, `col_of`, `sgn`, `n_χ` and `nfixed` from the orbit
> setup — not an equivalent row space, the identical operator.  (`nfixed` agrees
on every cell but is not part of the automated comparison; the compared fields
are the eight named above.)  On every cell
> with `a ≥ 1` the kernel returned from the lean operator was verified against
> the **old, uncompressed int64 operator** at both house primes, with
> `nullity = a` and `rank = a`; and every banked evaluation rank reproduced at
> both primes, including all four cells where the record is deficient (`A4` red
> 63 against `a` = 64, `B5` pad/red 9 against 12, `B7` pad/red 45 against 70,
> `D1` det 5 against 6).  Each is a **reproduced measurement**: a modular rank
> of 5 at `D1` proves `mult_det ≥ 5`, hence `i_det ≤ 1`, and nothing whatever
> about `i_det ≥ 1`.  The record's own `i_det = 1` there is s69's inherited
> value and is not re-established here.
>
> **MEASURED.**  The memory ratio grows with the cell: 1.0× at `n_χ ~ 10²`,
> 1.3–1.8× in the middle, and **1.8× to 2.6×** (`B6` to `C4`) on the cells above
> `N_S·δ = 10⁷`, at **0.4–0.9× the wall time** — the lean builder is not a memory-for-time trade
> at all in its default setting; it is faster as well as smaller, because the
> old builder's second pass over the target codes and its int64 temporaries
> cost time as well as bytes.
>
> **The pilot: the cell session 79 abandoned is built and closed.**
> `(10,6,6,6,2,2)₈` — `N_S = 18 337 360`, `N_S·δ = 1.47·10⁸`,
> `n_χ = 1 606 104`, `a = 10` — where s79 was ended by the box inside `E_45`
> with the rows over 4 GB, **builds in 812 s at a peak of 1.96 GB**
> (MEASURED), and on each of the four blocks s79 did finish, the lean build's
> row count and nonzero count agree with s79's log exactly — a count check on
> twelve integers, since that log carries counts and not an operator.  The kernel then runs at both primes inside the same
> box, every vector verified on `E`, and
>
>     mult_det((10,6,6,6,2,2), 8) = a = 10 at both primes,  so  i_det = 0   (PROVED over Q)
>
> so the last unreached cell of session 79's Q1 queue below its cap carries no
> determinant equation.  Peak for the whole cell, build plus kernel plus
> evaluation, **4.53 GB**.
>
> **The construction ceiling of this 8 GB box is therefore not `N_S·δ ≈
> 1.5·10⁸`.**  The measured ceiling is at least the pilot's `1.47·10⁸` at a
> 1.96 GB build peak, and the measured rate puts a 7 GB build budget at
> `N_S·δ ≈ 2.8·10⁸` (the worst observed rate) to `5.4·10⁸` (the pilot's own
> rate), or about half as much again with `blocks='disk'` — an extrapolation,
> labelled as one in §5.  The more useful statement is the one §5 makes: on this
> box the raising-row construction is **no longer the binding constraint**, and
> the *consumer* becomes the wall before the builder does.

---

## 1. What was wrong, measured rather than assumed

The pre-registration recorded a reading of s79's log — that the peak sits in the
target-basis canonicalisation and not in the CSR accumulation — as an
expectation.  **It is still a code reading, and this report does not upgrade
it.**  The old builder was never phase-instrumented here: its records carry a
total peak and three phase times, and only the *lean* records carry a
per-operator `phases` list.  What is measured is the outcome — the lean peak is
1.8–2.7× smaller on the large cells (§2.4) — not the attribution.  The reading,
offered as the design rationale and labelled as a reading, is that four
allocations account for the old builder's peak:

1. **The target-basis canonicalisation.**  `_canon_acc(T, Htabs, L)` holds `T`
   (int32, `N_T × δ`), its codes computed twice (once by `raising_rows_arr` as
   `codesT`/`sortedT`/`orderT`, once again inside `_canon_acc`), and `order`,
   `sorted_codes`, `canon`, `acc`, `ar`, `idx` as int64 — six live int64 arrays
   of length `N_T`, rising to eight inside `_image_index`; `obstructed` is bool.
   It also materialises `np.sort(tab[T])` **per group element**, holding the
   fancy-index result and its sorted copy at once.  At the pilot cell's `E_12`,
   `N_T = 16 720 327`: about 1.07 GB of int64 at the transient peak, plus
   2 × 535 MB of int32 for the sort.
2. **The accumulated CSR blocks**, kept in a Python list with **int64 data**
   until the final `vstack` — 8 bytes per nonzero where 2 suffice.
3. **The final `vstack`**, which copies every block again before the old copies
   are released.
4. **`M` itself as int32** where int8 suffices (`L − 1 < 128` at `n = 4, r ≤ 6`),
   plus `col_of`/`sgn`/`canon` as int64 where int32/int8 suffice.

The lean builder removes each: narrow letter and entry dtypes, one pass over the
target codes, chunked canonicalisation, `T` and its index arrays freed before the
raising pass, compact triples with a counting sort, and one preallocated
assembly.  Nothing in the mathematics moves; §2 is the evidence.

---

## 2. Acceptance — the suite

`analysis/wk13_b10_suite.py`, one bounded subprocess per build so that `VmHWM`
is that build's peak and nothing else's; `results/b13_10/suite.jsonl` carries a
record per cell.  The three tests are the board's, in the board's order.

### 2.1 Exact operator agreement (CERTIFIED, every cell)

`E_old ≡ E_new` as CSR after `sort_indices()`, entry by entry, together with
`M`, `col_of`, `sgn`, `n_χ` and `nfixed`.  The row-multiset fallback of the
pre-registration was never needed: **no cell fell back to "equivalent row
space"**.  Prediction P1 (0.8, identical at the first attempt) **hit**.

That matters exactly as the board says it does: matching `mult_det` is not
sufficient, and this is not a rank comparison — it is the assertion that the two
programs emit the same integer matrix.  Two incorrect operators can share a
sampled rank; they cannot share every one of the 23 818 432 entries of `C6`, the
largest operator in the suite.  (The pilot cell is **not** in this test: s79
never finished an `E_old` there, so §4 checks it by counts alone.)

### 2.2 Kernel vectors verified against the original operator (CERTIFIED)

On every cell with `a ≥ 1`, `hybrid_kernel_lean(E_new)` at both house primes
returned `a` vectors, each verified by `E_old · v = 0` on the **uncompressed
int64** operator (not on the compact one it came from), with
`rank_tall(K) = a`.  P2 (0.9) **hit**.  On the two `a = 0` cells the initial-term
cover reaches every column, which certifies `rank_p(E) = n_χ` and nullity 0
(§6.2 records the inherited defect this uncovered).

### 2.3 Evaluation ranks, as additional checks (MEASURED, all reproduce)

On the drivers' own families and seeds — det pencils seed 11, reducible points
seed 29, padded frames seed 37, `per_4` pencils seed 47, `per_3` pencils seed
41, bound 40, `K = a + 8` — at both primes, compared with the banked record.
P3 (0.85) **hit**: every banked value reproduces, including every drop.  A drop
reproduced here is a reproduction of a *measurement*: it bounds `i` from above
and establishes nothing about `i ≥ 1`, and nothing in this report uses it in
that direction.

### 2.4 The suite

`peak` is `VmHWM` above the process's post-import baseline, in GB; `secs` is the
whole build (monomials + orbit setup + rows + assembly).

| id | n | cell | a | N_S·δ | \|Stab\| | n_χ | nnz(E) | identical | kernel vs `E_old` | banked ranks | old GB | lean GB | ×mem | old s | lean s | ×time |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| A1 | 4 | (13,5,2,2,2)<sub>6</sub> | 2 | 22,032 | 6 | 825 | 15,678 | **yes** | yes | all 3 reproduce | 0.026 | 0.026 | 1.00× | 0.2 | 0.2 | 0.91× |
| A2 | 4 | (37,13,4,1,1)<sub>14</sub> | 71 | 498,764 | 2 | 13,252 | 116,760 | **yes** | yes | all 4 reproduce | 0.037 | 0.032 | 1.15× | 0.8 | 0.7 | 0.85× |
| A3 | 4 | (28,8,5,2,1)<sub>11</sub> | 99 | 572,363 | 1 | 52,033 | 487,986 | **yes** | yes | all 4 reproduce | 0.045 | 0.036 | 1.24× | 0.8 | 0.7 | 0.88× |
| A4 | 4 | (26,7,5,5,1)<sub>11</sub> | 64 | 4,308,788 | 2 | 193,330 | 3,478,457 | **yes** | yes | all 4 reproduce | 0.174 | 0.101 | 1.72× | 6.0 | 4.9 | 0.83× |
| B1 | 4 | (38,2,2,2,2,2)<sub>12</sub> | 1 | 99,228 | 120 | 200 | 10,858 | **yes** | yes | all 5 reproduce | 0.031 | 0.030 | 1.05× | 1.0 | 0.8 | 0.81× |
| B2 | 4 | (29,9,3,1,1,1)<sub>11</sub> | 1 | 324,544 | 6 | 1,816 | 15,205 | **yes** | yes | all 5 reproduce | 0.038 | 0.035 | 1.07× | 0.9 | 0.8 | 0.87× |
| B3 | 4 | (33,7,2,2,2,2)<sub>12</sub> | 12 | 2,563,644 | 24 | 13,518 | 617,879 | **yes** | yes | all 5 reproduce | 0.127 | 0.093 | 1.37× | 10.3 | 6.8 | 0.66× |
| B4 | 4 | (24,13,3,2,1,1)<sub>11</sub> | 45 | 3,002,802 | 2 | 108,267 | 1,161,245 | **yes** | yes | all 5 reproduce | 0.143 | 0.101 | 1.42× | 5.6 | 4.2 | 0.75× |
| B5 | 4 | (11,7,6,6,1,1)<sub>8</sub> | 12 | 21,074,040 | 4 | 553,842 | 12,513,089 | **yes** | yes | all 5 reproduce | 0.663 | 0.303 | 2.19× | 67.2 | 42.4 | 0.63× |
| B6 | 4 | (12,8,6,2,2,2)<sub>8</sub> | 37 | 24,565,120 | 6 | 586,482 | 16,879,887 | **yes** | yes | all 5 reproduce | 0.763 | 0.431 | 1.77× | 106.2 | 62.1 | 0.58× |
| B7 | 4 | (13,9,9,3,1,1)<sub>9</sub> | 70 | 31,532,004 | 4 | 732,815 | 18,374,635 | **yes** | yes | all 5 reproduce | 0.857 | 0.423 | 2.03× | 95.6 | 59.3 | 0.62× |
| C1 | 3 | (17,2,2,2,2,2)<sub>9</sub> | 1 | 42,687 | 120 | 116 | 6,255 | **yes** | yes | all 1 reproduce | 0.027 | 0.027 | 1.00× | 0.5 | 0.4 | 0.77× |
| C2 | 3 | (12,5,5,3,1,1)<sub>9</sub> | 4 | 433,449 | 4 | 9,472 | 174,557 | **yes** | yes | all 1 reproduce | 0.040 | 0.034 | 1.19× | 0.9 | 0.7 | 0.79× |
| C3 | 3 | (11,8,5,2,2,2)<sub>10</sub> | 14 | 5,286,630 | 6 | 104,651 | 2,850,304 | **yes** | yes | all 1 reproduce | 0.174 | 0.102 | 1.70× | 12.4 | 8.1 | 0.65× |
| C4 | 3 | (5,5,5,5,5,2)<sub>9</sub> | 1 | 27,182,070 | 120 | 23,907 | 6,649,482 | **yes** | yes | all 1 reproduce | 0.711 | 0.269 | 2.64× | 452.5 | 182.3 | 0.40× |
| C5 | 3 | (10,7,6,4,2,1)<sub>10</sub> | 21 | 8,169,400 | 1 | 816,940 | 10,925,235 | **yes** | yes | all 1 reproduce | 0.365 | 0.208 | 1.75× | 15.1 | 9.6 | 0.64× |
| C6 | 3 | (7,6,5,4,3,2)<sub>9</sub> | 2 | 14,946,993 | 1 | 1,660,777 | 23,818,432 | **yes** | yes | all 1 reproduce | 0.812 | 0.370 | 2.19× | 32.8 | 20.6 | 0.63× |
| D1 | 3 | (19,7,2,2,2,2,2)<sub>12</sub> | 6 | 13,863,624 | 120 | 17,047 | 1,526,091 | **yes** | yes | all 1 reproduce | 0.318 | 0.143 | 2.22× | 260.8 | 109.9 | 0.42× |
| X1 | 3 | (11,4,2,2,1,1,1,1,1)<sub>8</sub> | 0 | 1,979,488 | 240 | 33 | 466 | **yes** | yes | n/a (`a` = 0) | 0.149 | 0.128 | 1.16× | 67.2 | 33.6 | 0.50× |
| X2 | 4 | (15,4,2,2,1,1,1,1,1)<sub>7</sub> | 0 | 3,927,070 | 240 | 66 | 998 | **yes** | yes | n/a (`a` = 0) | 0.405 | 0.238 | 1.70× | 190.2 | 106.0 | 0.56× |

**20 of 20 cells PASS**, where PASS means all three tests: the identical operator, the kernel verified on `E_old` at both primes with `nullity = rank = a`, and every banked rank reproduced at both primes.  The record's deficient values reproduce as deficient and its full values as full — the drops placed were `A4` red_pts 63 against `a` = 64; `A4` red_star 63 against `a` = 64; `B5` pad 9 against `a` = 12; `B5` red_pts 9 against `a` = 12; `B5` red_star 9 against `a` = 12; `B7` pad 45 against `a` = 70; `B7` red_pts 45 against `a` = 70; `B7` red_star 45 against `a` = 70; `D1` det 5 against `a` = 6.  A rank reproduced here is a reproduction of a **measurement**: it bounds `i` from above, and nothing in this report reads it downward.

---

## 3. The memory/work tradeoff, exposed

The pre-registration exposed three knobs — `chunk` (source rows per pass), `triples` (`store` the raising triples and counting-sort them, or `recompute` them in a second pass and never store them) and `blocks` (`memory`, one preallocated concatenation at the end, or `disk`, each finished operator block written to scratch and read back at assembly).  Measured on the two largest cells of each polynomial degree, every variant returning the identical operator:

**B6**, (12,8,6,2,2,2)<sub>8</sub>, `n_χ` = 586,482, `nnz` = 16,879,887 — old builder 0.763 GB / 106.2 s.

| knobs | peak GB | × lean default | secs | × lean default | identical to `E_old` |
|---|---|---|---|---|---|
| `store, memory, 400 000` (default) | 0.431 | 1.00× | 62.1 | 1.00× | yes |
| `recompute, memory, 400,000` | 0.434 | 1.01× | 83.5 | 1.34× | yes |
| `store, disk, 400,000` | 0.277 | 0.64× | 70.6 | 1.14× | yes |
| `recompute, disk, 200,000` | 0.293 | 0.68× | 81.1 | 1.31× | yes |

**C6**, (7,6,5,4,3,2)<sub>9</sub>, `n_χ` = 1,660,777, `nnz` = 23,818,432 — old builder 0.812 GB / 32.8 s.

| knobs | peak GB | × lean default | secs | × lean default | identical to `E_old` |
|---|---|---|---|---|---|
| `store, memory, 400 000` (default) | 0.370 | 1.00× | 20.6 | 1.00× | yes |
| `recompute, memory, 400,000` | 0.351 | 0.95× | 30.2 | 1.46× | yes |
| `store, disk, 400,000` | 0.307 | 0.83× | 21.1 | 1.02× | yes |
| `recompute, disk, 200,000` | 0.282 | 0.76× | 31.3 | 1.52× | yes |

**The tradeoff is not where the pre-registration expected it.**  P4′ predicted that `triples='recompute'` would halve the raising-phase peak at about twice the raising time; it **does not fire** — the peak barely moves (1.0×) while the time rises by a third to a half (`B6` 1.34×, `C6` 1.46×).  The reason is the design working: after the target-table and dtype changes the stored triples are no longer the largest live allocation, so not storing them buys nothing.  What does pay is `blocks='disk'`, which streams each finished operator block out and cuts the lean peak by a further 17–36 % (`C6` 0.83×, `B6` 0.64×) at 1.02–1.14× the time — a genuine memory-for-work exchange, and the setting a box-constrained production run should use.  P4′ is therefore **recorded as not fired** — and the wording matters, because the numbers above are whole-build peaks while P4′ named the *raising-phase* peak.  The per-operator records answer that narrower question too and give the same verdict: the largest raising-phase HWM moves from 0.375 to 0.390 GB at `B6` and from 0.331 to 0.318 GB at `C6`, by ±4 %, nowhere near halving.  In every variant the whole-build peak is set by the final assembly step rather than by the raising phase, which is itself part of why the knob cannot pay.  The useful knob is the other one.

---

## 4. The pilot — the cell session 79 abandoned

`(10,6,6,6,2,2)` at `δ = 8`; `analysis/wk13_b10_pilot.py`, one bounded process
(`timeout 14400`, `ulimit -v 7 800 000`, pid in
`results/logs/b13_10_pilot.pid`), record in `results/b13_10/pilot.json`, log in
`results/logs/b13_10_pilot.log`.

**What s79 recorded (RECORDED, `results/logs/s79_sweep6.log` lines 2710–2724):**
monomials and orbit setup 633 s at HWM 2.42 GB; `E_01` 3 423 455 rows /
18 038 214 nnz; `E_12` and `E_23` 8 688 185 rows / 35 847 528 nnz each, HWM
3.76 then 4.20 GB; `E_34` 3 911 695 rows / 16 114 190 nnz; then `no RESULT line
(rc -9)` inside `E_45`.

**What the lean builder measures (MEASURED):**

| block | `\|H\|` | targets | rows | nnz | s79's rows / nnz | agree | tables s | rows s | HWM GB |
|---|---|---|---|---|---|---|---|---|---|
| `E_01` | 4 | 13,110,260 | 3,423,455 | 18,038,214 | 3,423,455 / 18,038,214 | **yes** | 57.4 | 69.6 | 0.96 |
| `E_12` | 2 | 16,720,327 | 8,688,185 | 35,847,528 | 8,688,185 / 35,847,528 | **yes** | 55.9 | 71.4 | 1.423 |
| `E_23` | 2 | 16,720,327 | 8,688,185 | 35,847,528 | 8,688,185 / 35,847,528 | **yes** | 55.3 | 72.1 | 1.685 |
| `E_34` | 2 | 7,796,883 | 3,911,695 | 16,114,190 | 3,911,695 / 16,114,190 | **yes** | 21.4 | 27.2 | 1.685 |
| `E_45` | 6 | 13,508,491 | 2,271,449 | 4,847,599 | — (s79 ended here) | — | 83.4 | 26.5 | 1.963 |
| assemble | | | 26,982,969 | 110,695,059 | — | — | | 1.5 | 1.963 |

**Build total: 812.1 s** (monomials 21.0 s, orbit setup 247.9 s, rows 543.2 s, of which the final assembly is 1.5 s), **peak 1.963 GB** (1.904 GB above the post-import baseline).  `N_S` = 18,337,360, `|Stab|` = 12, `n_χ` = 1,606,104, 26,982,969 rows, 110,695,059 nonzeros, `E.data` int16 (the exact entry bound at this cell is 480, and the largest entry was re-checked after the build), `M` int8.

The first four operators agree with s79's log **exactly** — same row counts,
same nonzero counts.  That is the strongest check available *for this cell*, and
it is weaker than the suite's: s79's log records three integers per block and no
operator, so this is a count agreement on twelve integers produced by different
code on a different day, not the entry-by-entry equality of §2.1.  The pilot
cell has no `E_old` to compare against — s79 never finished one.  `E_45`, the
block s79 never finished, contributes 2 271 449 rows and 4 847 599 nonzeros.

**The kernel and the determinant column (PROVED):**

Cover: **1,605,824 of 1,606,104** columns by the `reversed` order — a CERTIFIED rank floor of 1,605,824 at `O(nnz)` — leaving `|U|` = 280 and an excess of 270 over `a` = 10 (40.4 s, HWM 2.597 GB).

| prime | nullity | verified on `E` | kernel rank | `mult_det` | `i_det` | kernel s | ev + rank s | HWM GB |
|---|---|---|---|---|---|---|---|---|
| 2147483647 | 10 | **yes** | 10 | **10** | **0** | 232.3 | 75.4 | 4.379 |
| 2147483629 | 10 | **yes** | 10 | **10** | **0** | 238.7 | 42.2 | 4.532 |

`mult_det = a` at one prime already proves `mult_det = a` over `Q`
(`rank_p ≤ rank_Q`); both primes agree.  So `i_det = 0` at
`(10,6,6,6,2,2)₈`: **no determinant equation at this weight**, and s79's Q1
queue now has no cell left below its pre-registered cap.  This is one cell added
to the 682 of session 79 on the determinant side, by the same instrument
(session 71's hybrid, unmodified) on a bit-identical operator.

**What the pilot does *not* say.**  Only the determinant family was evaluated.
`mult_pad`, `mult_red` and `mult_per4` at this cell were **not** computed and
are priced in §5.  Nothing here touches the padded or reducible columns, and
`i_det = 0` is a statement about this weight alone.

---

## 5. The ceiling, and where the constraint moved

**The build ceiling (MEASURED, then extrapolated).**

Rather than a multivariate fit — whose split between `N_S·δ` and `nnz` is unstable, because the two are strongly correlated across the suite and the coefficients moved by a factor of three as cells were added — the honest statement is the **direct rate at the sizes that matter**:

| cell | `N_S·δ` | old GB per `10⁸` | lean GB per `10⁸` | ratio |
|---|---|---|---|---|
| D1 | 13,863,624 | 2.29 | 1.03 | 2.22× |
| C6 | 14,946,993 | 5.43 | 2.48 | 2.19× |
| B5 | 21,074,040 | 3.15 | 1.44 | 2.19× |
| B6 | 24,565,120 | 3.11 | 1.75 | 1.77× |
| C4 | 27,182,070 | 2.61 | 0.99 | 2.64× |
| B7 | 31,532,004 | 2.72 | 1.34 | 2.03× |
| **pilot** | 146,698,880 | — (s79 could not finish it) | 1.30 | — |

The lean rate is flat in the range where it matters, 0.99–2.48 GB per `10⁸` of `N_S·δ` against the old builder's 2.29–5.43, and the pilot at `1.47·10⁸` sits at 1.30 — the ratio is **1.77× to 2.64×** and does not decay with size.  Extrapolating a 7.0 GB build budget at the worst observed lean rate gives a build ceiling near **`N_S·δ ≈ 2.8·10⁸`**, and at the pilot's own rate **`≈ 5.4·10⁸`**; with `blocks='disk'` (§3) both figures rise by roughly half as much again.  Both are projections from measured points at or below the pilot and are labelled as such — MEASURED to `1.47·10⁸`, extrapolated beyond it.

The multivariate fit banked in `results/b13_10/curve_summary.txt` is consistent
with this and should not be over-read: at the pilot its terms split 0.93 GB
(`N_S·δ`), 0.76 GB (`rows`) and 0.17 GB (`nnz`), so the row count is the second
driver and only `nnz` has a near-zero coefficient.  The honest summary is that
the lean peak tracks the **monomial and target arrays** — `N_S·δ`, with `rows`
as the proxy for the per-operator target basis — and no longer the nonzeros.
That is the design working.  The ceiling range above is an **extrapolation**
from measured points at or below `1.47·10⁸`; between `B7` at `3.2·10⁷` and the
pilot the curve has a gap of a factor of 4.6 with one point above it.  Against
s79's own stated build wall (`N_S·δ > 2·10⁸`, `results/PREREG_s79.md`) the
extrapolated range is **1.4× to 2.7×** — and note that the pilot at `1.47·10⁸`
sits *below* that stated figure while being the cell s79 actually failed on,
which is the distinction that matters.

**But the constraint has moved to the consumer.**  At the pilot the build peaked
at 1.96 GB and the *whole cell* at 4.53 GB: the kernel phase, not the build,
now sets the box.  Its two large allocations are (i) `E` itself — 110.7 M
nonzeros at 6 bytes each, plus the `F_o` copy the hybrid makes of all but the
cover rows, and (ii) the `X` blocks, already bounded by `S71_MEM_X`.  The
`fo='inplace'` option in `hybrid_kernel_lean` removes the `F_o` copy — a cover
row satisfies `R_1[r,U] − R_1[r,S]X = 0` identically, so passing every row of
`E` to the projection changes nothing but the rows the pseudo-random draw
indexes — and is verified equivalent on three banked cells at both primes
(`results/b13_10/fo_inplace_check.json`: same nullity, every vector verified on
`E`, same rank, same `mult_det` where the family was evaluated), but the pilot
was run with the original `fo='copy'` so that its numbers compare with s79's.  **A
batch-14 production run should measure `fo='inplace'` first; on the pilot it
should save about 0.7 GB of the 4.53.**

**So the honest ceiling statement is:** the raising-row construction is no
longer the binding constraint on this box at any size the programme has priced.
The next constraint is the hybrid's handling of a large `E`, and it is an
engineering item of the same kind, not a mathematical one.

**Priced, not done:**

| item | cost, priced from this session's own rates |
|---|---|
| the three families this pilot did not evaluate at `(10,6,6,6,2,2)₈` — `mult_pad`, `mult_red`, `mult_per4` | the kernel is the expensive part and is already priced at 232.3 + 238.7 s = **7.9 CPU-minutes for both primes**; each additional family is one pass of evaluation rows plus one rank, measured here at 42.2 s and 75.4 s, so all three families at both primes is **≈ 5.9 CPU-minutes on top of that**, and the `(★)` reducible mask over `N_S = 1.8·10⁷` a few minutes more.  A four-family s79-schema row for this cell is well under an hour. |
| the other Q1 cell s79 never attempted, `(12,4,4,4,4,4)₈` at `N_S·δ = 2.16·10⁸` | above the pilot by 1.47×; at the pilot's measured rate the **build** is ≈ 2.8 GB and ≈ 20 minutes.  Its `n_χ` is estimated at 225 081 in `results/s79_queue.json` — seven times *smaller* than the pilot's, since `\|Stab\| = 120` compresses it — so on this evidence the cell is **cheaper downstream** than the pilot and the build is the whole cost.  It is the obvious first goal for batch 14. |
| the eleven degree-10 cubic weights above `N_S = 10⁷` that block `I(D₆^{per₃})₁₀` | `N_S` from `1.00·10⁷` (`(6,6,6,6,4,2)`) to `2.73·10⁷` at δ = 10, i.e. `N_S·δ` from `1.0·10⁸` to `2.7·10⁸` (`results/s79_per6_queue.json`) — the cheapest are **below the pilot** and the dearest is 1.9× it.  On this box the builds are now routine; the largest, `(5,5,5,5,5,5)`, is the one to price carefully because `|Stab| = 720` makes its orbit setup, not its rows, the cost. |
| the fifteen horizontal-13-strip predecessors of `λ₁₃` (`N_S` `1.59·10⁷`–`8.10·10⁸`, per `docs/batch13_board.md`) | at δ = 13 that is `N_S·δ` from `2.1·10⁸` to `1.05·10¹⁰`.  The cheapest few are within about 1.4× of the pilot and are now plausible on this box; the dearest is **two orders of magnitude beyond** anything measured here and is not made reachable by this work.  Nothing in this session should be read as putting `I(D₉^{per₃})₁₃` in reach. |
| the balanced six-row cells at `N_S·δ ≥ 10⁸` | the pilot **is** one of them, and it cost 812 s to build and 1 441 s — **24.0 minutes** — in all (build 812.1, cover 40.4, then 307.8 and 280.8 for the two primes).  A sweep of that class is now a scheduling question rather than a memory one. |

---

## 6. Defects

### 6.1 In the assignment (the integrator asked for these)

1. **"lengths 5, 6 and 9 where banked cells exist" has no length-9 instance.**
   A scan of every `results/**/*.json*` in the tree finds **no cell of length
   ≥ 8 that the raising-row builder has ever built** — no record carrying
   `n_χ`/`nrows` with a `λ` of eight or more parts.  The length-9 objects in the
   programme (`(65,17,2⁷)₂₄`, `(21,17,2⁷)₁₃`, the fifteen cubic predecessors at
   `N_S ≥ 1.6·10⁷`) were reached by other routes or not at all.  Worse for the
   suite's purpose, every length-9 weight cheap enough to build has `a = 0`: of
   the sixteen length-9 candidates priced here (`n = 3` and `n = 4`, `δ ≤ 8`),
   **all sixteen** have `a = 0` by the Weyl alternation.  The suite therefore
   substitutes the banked **length-7** positive control `D1` and two `a = 0`
   length-9 operator checks, and says so.  A future brief should ask for
   "lengths 5, 6, 7" and treat length 9 as an exploratory extra.
2. **The board's `N_S·δ = 1.47·10⁸` for the wall is right, but "the rows
   exceeding 4 GB" understates what is recoverable.**  The rows at that cell are
   110.7 M nonzeros = 664 MB in the compact form and 1.1 GB with indices; the
   4 GB was the *transients*, not the operator.  That distinction is what made
   the cell reachable, and a brief that says "the rows exceed 4 GB" invites the
   wrong fix (a bigger box) rather than the right one.
3. **"Its production consumers are batch 14's" is true of the builder but not of
   the pilot.**  The pilot necessarily produced a new mathematical result
   (`i_det = 0` at a cell in s79's frozen queue).  A brief that says no other
   session depends on this one should still say where such a by-product is to be
   banked; this one is in `results/b13_10/pilot.json` and is not merged into
   `results/s79_cells.jsonl`, whose schema carries four families and not one.

### 6.2 In the tree (found here, reported not patched)

4. **`wk11_s71_hybrid.hybrid_kernel` raises on a complete cover.**  When the
   initial-term cover covers every column, `nU = 0`, `ublock` is set to `nU`, and
   `range(0, 0, 0)` raises `ValueError: range() arg 3 must not be zero`.
   Confirmed here on `(11,4,2,2,1⁵)₈` (`n_χ = 33`, cover 33, `a = 0`).  It is
   reachable exactly when the operator has certified full column rank — the
   cheapest possible cell — so it has never fired in a sweep, but it will fire in
   any census that includes `a = 0` weights.  The lean wrapper returns the empty
   kernel with the certificate ("cover of size `n_χ`: `rank_p(E) = n_χ`,
   nullity 0") and asserts `a = 0`.  **This session's own wrapper inherited the
   defect and crashed on both `a = 0` cells before it was fixed**
   (`results/logs/b13_10_suiteB.log`, 00:46 and 00:47, raising at
   `wk13_b10_lean.py:710`); the fix is in `hybrid_kernel_lean` only.
   `wk11_s71_hybrid.py` is **not** edited, per the pre-registration's "the hybrid
   is not modified"; a one-line guard upstream is the right fix and belongs to
   whoever owns that file.
5. **`E.data` narrower than int64 breaks two lines of the hybrid under NumPy 2.**
   `int16_array % 2147483647` raises `OverflowError` (NumPy 2 refuses the
   Python-int operand for the narrow dtype).  `hybrid_kernel_lean` upcasts
   through int64 in chunks at exactly those two points; nothing else in the
   hybrid needed changing.  Any future consumer of a compact `E` will meet the
   same wall.

### 6.3 In this session's own conduct

6. **The rank comparator placed nothing at `D1` and would have reported PASS on
   an empty comparison.**  `banked()` took the first record matching the cell in
   `results/s69_sizes.jsonl`, which is that session's `SPANNING_FAILED` first
   pass with every rank `None`; the comparison came back `{}` and the cell was
   marked PASS on the operator and kernel tests alone.  That is the batch-12
   failure mode the preamble names — a check that silently drops its own targets.
   Fixed mid-session: the record is now chosen by carrying measurements, and a
   cell whose banked multiplicities cannot all be placed against a computed
   family **fails**.  Every cell was re-run under the fixed comparator
   (`results/logs/b13_10_recheck.log`), including `B5` and `C4`, the two banked
   cells first produced before the fix.  `D1` then places `det` 5 against 5.
7. **One unbounded process.**  A length-9 sizing probe was run before the
   pre-registration existed and was ended by the box (rc 137).  Nothing was
   measured by it and nothing here depends on it; it is recorded in the
   pre-registration and repeated here because the preamble's rule was broken
   once.
8. **The container was suspended for about five hours** (15:36–00:40 UTC), which
   is why the 18:00 America/New_York substantive update was never sent.  The
   input-and-control checkpoint went out at 11:16; the deadline was extended by
   two hours on request and the work below was completed inside it.  Twelve
   suite records produced before a later change to the builder's DP tables were
   discarded and every cell re-run under one code version
   (`results/b13_10/suite_precode_change.jsonl` is retained for audit and is
   **not** the record).

---

## 7. Pre-registration scorecard

| | pre-registered | outcome |
|---|---|---|
| P1 (0.8) | exact operator agreement on every cell at the first attempt | **hit** — identical on every cell run, no fallback to row-multiset equality |
| P2 (0.9) | `a` kernel vectors at both primes, each verified on `E_old` | **hit** on every cell with `a ≥ 1` |
| P3 (0.85) | every banked evaluation rank reproduces at both primes | **hit**, drops included |
| P4 (0.7) | lean peak at most half the old peak on the four largest cells, at ≤ 1.5× time | **partly hit**: on the four largest by `N_S·δ` (`B7`, `C4`, `B6`, `B5`) the ratio is 2.03×, 2.71×, 1.77×, 2.24× — at or past half on three of the four, short of it at `B6` — and the time is **below** 1× throughout, so the time half of the prediction was wrong in the session's favour |
| P4′ (0.6) | `triples='recompute'` halves the **raising-phase** peak at ~2× raising time | **not fired** — the raising-phase HWM moves by ±4 % (`B6` 0.375 → 0.390 GB, `C6` 0.331 → 0.318 GB) and the whole-build peak by 1.0×; §3 says why, and names `blocks='disk'` as the knob that does pay |
| P5 (0.6) | the pilot builds under 7.8 GB with peak below 2.5 GB | **hit** — 1.96 GB |
| P6 (0.4) | a verified kernel at both primes for the pilot within the same bounds | **hit** — and `mult_det` as well |
| stopping rules | `timeout` + `ulimit -v` on every run, pid recorded, ended only by that id | held; no run was ended early.  Deviation: the re-run loop used `ulimit -v 2 500 000` rather than the pre-registered `7 000 000` — tighter, not looser |
| falsifier | agreement fails and cannot be restored | never fired |
| deviation | addendum A replaced the two `n_χ = 0` length-9 cells | recorded before the substitutes ran |
| deviation | the rank comparator was fixed mid-session after it placed nothing at `D1` | recorded in §6.3 item 6; every cell re-run under the fixed comparator |

---

## 8. What was not done, and what it costs

**Not done, and why:**

1. **`mult_pad`, `mult_red`, `mult_per4` at the pilot cell.**  The board asked for
   `mult_det` at both primes as the additional check and that is what was run.
   Priced in §5; nothing here characterises the padded or reducible side at that
   weight, and `i_det = 0` is a determinant-side statement alone.
2. **`fo='inplace'`'s saving was not measured.**  Its *equivalence* is banked on
   three cells at both primes (`results/b13_10/fo_inplace_check.json`); its
   *saving* is measured nowhere, because the pilot deliberately ran `fo='copy'`
   so its numbers compare with s79's.  The ~0.7 GB figure in §5 is arithmetic
   from the size of the `F_o` copy, not a measurement, and is labelled as such.
3. **No length-9 cell with `a ≥ 1` was built** — none exists in the tree and none
   of the sixteen priced here has `a ≥ 1` (§6.1).  The two length-9 cells in the
   suite test the int16 letter dtype and the operator, not a multiplicity.
4. **The lean builder was not put into any production driver.**  `wk12_s79_cell6`,
   `wk12_s79_per6` and the rest still call `wk9_s45_build.build_cell`; nothing in
   the tree's existing paths changed, which is why every banked number in this
   session is a genuine reproduction rather than a re-run of modified code.
   Wiring it in is batch 14's, as the board says.
5. **No second box, no threading, no C.**  Every measurement is single-process,
   two-CPU, one 8 GB container; the raising pass is embarrassingly parallel over
   operator blocks and nothing here explores that.
6. **No cell between the suite's largest (`B7`, `N_S·δ = 3.2·10⁷`) and the pilot
   (`1.47·10⁸`) was built**, so the curve has a gap of a factor of 4.6 with the
   pilot as its only point above it.  The extrapolated ceilings in §5 rest on
   that one point; a successor wanting a tighter curve should build two or three
   cells in the gap, which now cost a few minutes each.
7. **The variants were measured on two cells, not four.**  `B6` and `C6` carry
   the full knob sweep (one `n = 4` and one `n = 3`, `|Stab|` 6 and 1); `B7` and
   `C5` were run at the default only, to fit the session's remaining time.  The
   `blocks='disk'` saving is therefore two measurements, not four.

**What a successor gets for free:** the module is a drop-in with the same return
shape, the suite is one command per cell and banks per cell, and the pilot script
takes `--stage build` and `--stage kernel` separately so a build can be banked
and its kernel run later against the saved `E`.

---

## 9. For the integrator

1. **The builder is a drop-in.**  `wk13_b10_lean.build_cell_lean` returns the
   same dict shape as `wk9_s45_build.build_cell` with the same `arr` and an `E`
   that is the identical matrix in narrower dtypes, plus `phases` and `knobs`.
   The only consumer change needed is the dtype-safe entry into the hybrid,
   supplied as `hybrid_kernel_lean`; `best_cover_lean` and
   `check_kernel_mat_lean` are chunked equivalents of the two other routines that
   materialise something of size `nnz` or `rows × a`, verified identical
   (`best_cover_lean` returns the same rows, `S`, `U`, order and statistics).
2. **The `a = 0` guard belongs upstream** (§6.2, item 4).
3. **Measure `fo='inplace'` before the next production sweep** (§5): on the
   pilot it should remove about 0.7 GB from a 4.53 GB peak, and the consumer is
   now the binding side.
4. **The pilot's cell is closed on the determinant side only.**  If the record
   wants it as a four-family s79-style row, the three remaining families cost
   what §8 prices.
5. **The board's length-9 request cannot be met from the tree** (§6.1, item 1).
   The substitute control `D1` is the only cell in the suite where the record's
   determinant rank is **deficient** (5 against `a` = 6), and it reproduces —
   which is what makes it worth having: it tests the instrument's ability to see
   a drop, not only to confirm fullness.  It does **not** re-establish
   `i_det ≥ 1` there, and nothing here should be read as doing so.

Author: Swami Sethuraman, swsethuraman@beneficus.ai, Beneficus AI.
board_numbering: batch13
