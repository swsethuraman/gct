# PREREG — B14-12: `(12,4,4,4,4,4)` at `δ = 8`, the last cell of session 79's Q1 queue

board_numbering: batch14
session B14-12, branch `b14-12-q1-last-cell`.

**Base.** `batch14-base`, an annotated tag. Resolved with the two commands the
packet names, **not** `git rev-parse`:

| | |
|---|---|
| `git log -1 --format=%H batch14-base` (commit) | `9898e56941a7665f231873481dae956f08509995` |
| `git log -1 --format=%T batch14-base` (tree) | `cb688cd3fe454d638f3202e759e2eaa0c629739f` |
| `git rev-parse batch14-base` (**tag object** — not to be used as a base) | `4bda8a12433c5965a5df82fef35b4c7220b76756` |

**The dispatch did not state the expected commit and tree.** The packet says
"Your dispatch message states the expected commit and tree … Record both values
in your pre-registration and check they match what the tag resolves to." No such
message reached this session, so the cross-check the packet asks for could not
be performed against a dispatch. It was performed against a second, independent
copy instead: the tag object hash in the laptop clone at
`C:\Users\swami\Projects\gct\work\.git\refs\tags\batch14-base` is
`4bda8a12433c5965a5df82fef35b4c7220b76756`, identical to the value this clone
gets from `origin`. Recorded as a defect in §9, and the check is labelled for
what it is: agreement between two clones of the same remote, which is weaker
than agreement with a value fixed at dispatch.

**Model.** The runtime reports the serving model as `claude-opus-5`; the packet
named "Claude". Commit trailers carry `Claude Opus 5`. If any part of this
session were served by a different model the runtime did not disclose it, and
this line is the runtime's report rather than an independent observation.

**Host (declared, as the packet requires).** One cloud container, **not** an
independent twelfth of anything: `MemTotal` 8,216,192 kB ≈ **7.84 GB**,
`MemAvailable` ≈ 7.2 GB at start, **2 cores**, 30 GB writable disk, no cgroup
memory cap below the VM's. `gcc` 13.3.0, `python-flint` 0.9.0, numpy 2.4.4,
scipy 1.17.1, sympy 1.14.0 — python-flint, numpy, scipy and sympy were **not**
preinstalled and were installed by this session (`pip install --break-system-packages`);
gcc was present. This is the same class of box as B13-10's (8 GB / 2 cores) and
the A1 container (7 GB / 2 cores), so B13-10's peaks transfer directly.

---

## 1. The question

Does `(12,4,4,4,4,4)` at `δ = 8`, `n = 4`, `r = 6` carry a **determinant
equation** — is `i_det = a − mult_det ≥ 1`?

**Why determinant-first closes the cell.** `D = mult_pad − mult_det` and
`mult_pad ≤ a`, so

    i_det = 0  ⟹  mult_det = a  ⟹  D = mult_pad − a ≤ 0.

So `i_det = 0` settles `D ≤ 0` at this weight **without evaluating the padded
family at all**. That is the whole economy of the determinant-first order and it
is the reason this slot is one cell rather than four families.

**Why this cell.** `results/PREREG_s79.md` §2.4 freezes Q1 as 123 six-row cells
ordered by `N_S·δ`, "from `(13,7,4,2,1,1)₇` at `4.5·10⁵` to `(12,4,4,4,4,4)₈` at
`2.2·10⁸`". This is the **last and largest** of the 123. The same section sets
s79's build wall at `N_S·δ > 2·10⁸`, "not attempted"; at `2.16·10⁸` this cell is
**above** that wall and was never attempted by s79, by B13-10, or by anyone. It
is unblocked by `PROVED.md: build_no_longer_binding` (B13-10), which measures the
raising-row build at 1.96 GB on `N_S·δ = 1.47·10⁸` and moves the ceiling to
`N_S·δ ≈ 2.8–5.4·10⁸`.

**What it does not decide.** `i_det = 0` here bears on this weight alone. It is
not a statement about `D_6^{per₃}`, not a contribution to `i_red(13)` or
`i_red(14)`, and not a step toward `D = −4` at LMR. Per the board's own §3, this
slot is deprioritised and kept only because the strategy memo retired it on "no
known family lives there" — an absence of mechanism treated as a bound. The
deliverable is a closed cell and a priced negative, nothing larger.

---

## 2. The instrument

The integrated (lean) production path accepted by A1 (`results/b14_a1/report.md`,
all twelve cells PASS), driven exactly as B13-10's pilot drove it
(`analysis/wk13_b10_pilot.py`):

| step | routine |
|---|---|
| build | `wk13_b10_lean.build_cell_lean` (monomials → orbit setup → raising rows) |
| cover | `wk13_b10_lean.best_cover_lean` |
| kernel | `wk13_b10_lean.hybrid_kernel_lean`, both house primes, **every vector verified on `E`** |
| rank | `wk12_s79_cell6.ev_rows_from_coeffs` → `wk11_s71_hybrid.matmul_mod` → `rank_mod_p` |

Primes `2147483647` and `2147483629`. `rank_p ≤ rank_ℚ`, so `mult_det = a` at
**one** prime proves `mult_det = a` over `ℚ`; a *drop* is a ceiling on `mult_det`
and a floor on `i_det` in the wrong direction — it bounds `i` from above and
**never** establishes `i ≥ 1` (`PROVED.md: rank_floor`,
`evaluation_cannot_certify_i_ge_1`). This cell has no `complete_interpolation`
certificate and none is attempted, so the exception does not apply here and no
deficient rank measured in this session will be read as `i_det ≥ 1`.

Determinant family: session 79's own — `det_4` pencils of length `R = 6`,
**seed 11**, **bound 40**, `K = a + 8` points, via
`wk12_s79_cell6.det_pencils` / `det_coeffs`.

**Letter ordering.** Every letter is resolved through `wk8_s30_core.exps(n, r)`
**by index**, never by a literal, because two opposite `exps` orderings exist in
this tree. `ev_rows_from_coeffs` is called with `n=4` explicitly; the default in
that module is already `N = 4` but it is passed anyway.

**Knobs, chosen from B13-10 §3 and §5 rather than defaults:**

- `blocks='disk'` — measured to cut the lean build peak by a further 17–36 % at
  1.02–1.14× the time; "the setting a box-constrained production run should use".
- `triples='store'` (default) — `recompute` was measured **not** to pay.
- `chunk=400000` (default).
- `fo='inplace'` in the kernel — B13-10: "A batch-14 production run should
  measure `fo='inplace'` first; on the pilot it should save about 0.7 GB of the
  4.53." Verified equivalent on three banked cells at both primes
  (`results/b13_10/fo_inplace_check.json`). **This is a deviation from the
  pilot's recorded `fo='copy'` and is pre-registered as one**; §7-S3 governs it.
- `S71_MEM_X=250000000`, as the pilot.

**Staged, so that a kernel failure does not cost the build.** `--stage build`
writes `E` and the orbit arrays to a scratch `.npz`; `--stage kernel` reloads
them. Driver: `analysis/b14_12_cell.py` (new; a length/`n`-general
re-parametrisation of `wk13_b10_pilot.py` with the knob and control changes
above — it introduces no new mathematics and calls only tree routines).

**Bounds.** Every run launched under `timeout` and `ulimit -v`, pid written to
`results/logs/<run>.pid`, and ended only by that recorded id. Build:
`timeout 10800`, `ulimit -v 7000000` (7.0 GB). Kernel: `timeout 10800`,
`ulimit -v 7300000`.

---

## 3. The objects, and which numbers are already observed

**Already in the tree — these are NOT blind predictions** (`results/s79_queue.json`,
frozen before s79's first cell):

| quantity | value | provenance |
|---|---|---|
| `λ` | `(12,4,4,4,4,4)`, `δ = 8`, `n = 4`, `r = 6`, `\|λ\| = 32 = nδ` | queue |
| `N_S` | 27,009,659 | queue (exact, from `results/s57_cells/`) |
| `\|Stab\|` | 120 `( = 5!, the five equal parts)` | queue |
| `N_S·δ` | 216,077,272 = `2.16·10⁸` | queue |
| `a` | 4 | queue — **to be re-derived here by `wk9_s42_census.a_weyl`, not inherited** |
| `a_∞` | 13 | queue (so this is not a first stable cell) |
| `nchi_est` | 225,081 | queue — **a forbidden quotient; see §4. Not used.** |

**Open, to be measured here:** `n_χ`, `nrows`, `nnz`, `nfixed`, build peak,
whole-cell peak, cover size and `\|U\|`, `mult_det` at both primes, `i_det`.

**Derived, static, checked at run time:** `L = |exps(4,6)| = C(9,4) = 126`, so
the letter dtype is `int8`; `entry_dtype(120, 8, 4)` has bound
`|Stab|·δ·(n+1) = 4800 < 2^15`, so `E.data` is `int16` — and the builder asserts
it and re-checks every value after the build.

---

## 4. `n_χ` will be MEASURED, not derived — and the assignment's own estimate is a quotient the index forbids

`PROVED.md: nchi_2_21_guard` and the board's §1 both say: **`n_χ` is not
`N_S/|Stab|`**; that quotient is "neither an upper nor a lower bound"; the
invariant is `n_χ ≤ N_S`; "measure `n_χ` rather than deriving it".

**Every one of the 123 `nchi_est` values in `results/s79_queue.json` is exactly
`ceil(N_S/|Stab|)`** — checked here, 123 of 123. So the 225,081 quoted for this
cell in B13-10 §5 *is* the forbidden quotient, and the board's slot-12 sentence
"`|Stab| = 120` compresses `n_χ` sevenfold", together with B13-10's conclusion
that the cell is "cheaper downstream than the pilot", rests on it.

The one Q1 cell whose true `n_χ` has since been measured is the pilot,
`(10,6,6,6,2,2)₈`: queue estimate 1,528,114, **measured 1,606,104** — the
quotient **under**-estimates by **5.1 %**. Direction as well as magnitude is
unknown in general, which is the index's point.

This changes nothing structural (`225,081·1.051 ≈ 236,600`, still 8.9× under
`2²¹ = 2,097,152`, so `matmul_mod`'s correctness guard is not approached and
`matmul_mod_wide` is not needed — and the guard binds on the **inner dimension**
of the multiplication, `n_χ`, which is the quantity named here). It is recorded
because the sizing claim in the assignment is built on a number the index says
must not be used that way, and because a 5 % surprise in the measured direction
would still be a 5 % surprise. **`n_χ` as measured by `orbit_setup_lean` is the
only value this session will use or report.** Control R (§5) tests that
measurement path against a banked value before the cell is built.

---

## 5. Controls, each with an input that must make it fail

The packet: "**Feed every control an input that must make it fail, and report
that you did.**" Each control below is run twice — once on its intended input,
once on an input for which the assertion is false. A control whose deliberate
failure does **not** fire is a dead control and stops the session (§7-S1).

### Control N — the forced negative (`PROVED.md: negative_control_forced`), at `n = 4`

`A_i = diag(d_{i0},…,d_{i3})` gives
`det_4(Σ_i s_i A_i) = ∏_{c=0}^{3} (Σ_i s_i d_{ic})` — a product of **four**
linear forms in the six variables `s`. The coordinate ring of a product of four
linear forms carries no constituent of more than **four** rows; `ℓ(λ) = 6 > 4`.
So the evaluation rank on this family **must be 0**, forced by representation
theory and independent of any banked history. `K = a + 8` points, seed
`20260909`, bound 40, both primes.

- **N.a (identity check, and its failure input).** The restricted coefficient
  dict of each diagonal pencil is compared against the explicit fourfold product
  of its linear forms, built by independent repeated multiplication (the `n = 3`
  version of this check is `analysis/wk13_b08_control.py`). **Must fail on:** the
  same check run against a *generic* (non-diagonal) `det_4` pencil.
- **N.b (rank-zero assertion, and its failure input).** `rank == 0` on the
  diagonal family. **Must fail on:** the same assertion applied to the generic
  `det_4` family on the same kernel `K` — where the rank is `mult_det ≥ 1`
  whenever `K ≠ 0`. If it does not fail, the evaluation-and-rank path is not
  computing and no rank from this session means anything.
- **N.c (rank machinery liveness).** `rank_mod_p` on matrices of known rank
  (identity-with-padding and a deliberately rank-deficient product), both primes.

### Control R — the `n_χ` measurement path, against a banked value

The board: "**Control** the already-closed `(10,6,6,6,2,2)₈` as a reference check
only — **not as new work**." Rebuilding that cell end to end is 24 CPU-minutes
and 4.53 GB and would be new work on a closed cell. Instead the **orbit-setup
half alone** is re-run — `monomials_array_lean` + `orbit_setup_lean`, ≈ 270 s and
≈ 1.0 GB by B13-10's own phase record — and its `N_S`, `|Stab|` and **`n_χ`** are
compared field by field with `results/b13_10/pilot.json`
(18,337,360 / 12 / 1,606,104). No raising rows, no kernel, no evaluation.

This is the control that matters for §4: it tests the exact code path that will
produce this cell's `n_χ`, on a cell where the right answer is banked.

- **Must fail on:** the same comparison run against the queue's *estimate*
  1,528,114 in place of the banked 1,606,104. If that comparison passes, the
  comparator is not comparing.

### Control S — the driver against banked suite cells

`analysis/b14_12_cell.py` is run end to end on two banked `n = 4` cells of
B13-10's suite before it is pointed at the target, and every field is compared
with `results/b13_10/suite.jsonl`:

- **B1** `(38,2,2,2,2,2)₁₂`, `a = 1`, **`|Stab| = 120`** — the same stabiliser
  order as the target, so the `|Stab| = 120` orbit path is exercised on a banked
  cell; banked `n_χ = 200`, `nnz = 10,858`.
- **A1** `(13,5,2,2,2)₆`, `a = 2`, `|Stab| = 6`, banked `n_χ = 825`,
  `nnz = 15,678`.

Compared: `a`, `N_S`, `|Stab|`, `n_χ`, `nrows`, `nnz`, cover size, `|U|`, and
`mult_det` at both primes.

- **Must fail on:** a one-field mutation of the banked record (`n_χ + 1`). If the
  comparator still reports PASS, it is the batch-12 failure mode B13-10 §6.3
  records — a comparator that silently drops its own targets.
- **Empty-comparison guard.** The comparator asserts a **non-zero count** of
  fields actually placed, and asserts the target cell was found in the banked
  file, *before* it reports anything. `all()` and `not any()` over nothing are
  vacuously true — the seventh instance of `check_must_be_able_to_fail`, the
  integrator's own, was exactly this.

### Control K — the kernel is verified, not asserted

Every returned null vector is checked `E·v = 0` on the **full** `E`
(`check_kernel_mat_lean`), and `rank_tall(K) = nullity` at both primes. A kernel
of the wrong dimension, or one vector failing on `E`, stops the cell (§7-S2).

- **Must fail on:** the same verification applied to a deliberately perturbed
  kernel matrix (one entry incremented).

### Control F — `fo='inplace'` is not free

Because §2 deviates from the pilot's `fo='copy'`, the two settings are run
against each other **on banked cell A1** and required to give the same nullity,
the same rank, the same `mult_det`, and vectors that all verify on `E`. B13-10
banked this equivalence on three cells; it is re-checked here on the driver that
will use it.

- **Must fail on:** comparing `fo='inplace'`'s result against a mutated
  `fo='copy'` result.

---

## 6. Decision table

Let `a` be the value `a_weyl` returns here (expected 4, checked not inherited),
`m₁, m₂` the `mult_det` at the two primes, `m = m₁ = m₂` when they agree.

| observation | conclusion | label |
|---|---|---|
| `m = a` at **either** prime, kernel verified, Control N reads 0 | `mult_det = a` over `ℚ`; `i_det = 0`; hence `D ≤ 0` at this weight; **Q1 is complete through its largest cell** | **PROVED** (over `ℚ`, by `rank_p ≤ rank_ℚ`) |
| `m < a` at both primes, agreeing, everything verified | `mult_det ≥ m`, so `i_det ≤ a − m`. **A candidate determinant equation, not an established one.** The verification protocol of `results/PREREG_s79.md` §2.5 takes over *before* the result is reported anywhere: second point family at seed + 1000, kernel vector exhibited in χ-coordinates and verified, both primes already in | **MEASURED**; `i_det ≥ 1` is **NOT REACHED** by evaluation alone |
| `m₁ ≠ m₂` | primes disagree — an instrument fault, not a result. Report as such; no mathematical claim | **halt the cell** |
| build exceeds the `ulimit -v` bound or the `timeout` | the cell is not closed. Report the measured phase peaks and the phase reached, and re-price the ceiling from them | **NOT REACHED**, priced |
| Control N reads non-zero at either prime | every rank from this instrument on this cell is void | **halt the sweep; the verification protocol takes over** |

**No branch of this table concludes `i_det ≥ 1` from a deficient rank.** The only
route to `i_det ≥ 1` is a certificate this session does not build.

---

## 7. Stopping rules

- **S1.** Any control that does not fail on its deliberate-failure input: stop,
  report the dead control, and treat every measurement it was supposed to guard
  as unestablished.
- **S2.** A null vector that does not verify on the full `E`, or
  `rank_tall(K) ≠ nullity`, or `nullity ≠ a`: stop the cell.
- **S3.** Control F disagreeing between `fo='inplace'` and `fo='copy'`: revert to
  `fo='copy'` for the target cell and re-price the memory budget. The deviation
  is abandoned, not argued with.
- **S4.** The build exceeding 7.0 GB (`ulimit -v`) or 3 hours: no retry at a
  larger bound on this host — the box is 7.84 GB total and a larger bound would
  be answered by the kernel, not the allocator. Report the phase reached, the
  measured per-phase peaks, and the implied ceiling.
- **S5.** `a_weyl` returning a value other than 4: stop and report the
  disagreement with `results/s79_queue.json` before computing anything else. A
  frozen queue entry that is wrong is a bigger finding than this cell.
- **S6.** The primes disagreeing on any quantity: stop the cell.
- **S7 (budget).** The three non-determinant families (§8) are a stretch and are
  attempted **only** after the determinant column is complete, committed and
  banked. They are abandoned without argument if the determinant column takes
  more than half the window.

---

## 8. What is core and what is stretch

**Core (this slot's deliverable).** The determinant column at
`(12,4,4,4,4,4)₈`: `N_S`, `|Stab|`, measured `n_χ`, `nrows`, `nnz`, cover, kernel
at both primes with every vector verified, `mult_det`, `i_det`, and the full
phase-by-phase cost and memory record — which is also the first measurement of
the lean build **above** `N_S·δ = 2·10⁸`, where B13-10's ceiling was an
extrapolation with a factor-4.6 gap below it and one point above.

**Stretch, in order, each abandoned without argument if the budget binds:**

1. The remaining three families — `mult_pad`, `mult_red` (both the point-free
   `(★)` mask and the sampled points) and `mult_per4` — giving a complete
   **s79-schema row** for this cell in `results/s79_cells.jsonl`'s own field set.
   This also addresses B13-10 §6.1 defect 3, which records that the pilot's
   result was left in `results/b13_10/pilot.json` and never merged into the
   four-family schema. If reached, the same row is produced for the pilot cell
   from its banked record where the fields exist, and the gaps named where they
   do not.
2. The measured build point itself written up against B13-10 §5's extrapolated
   ceiling — a single measured point at `2.16·10⁸` inside a range that was
   projected from `1.47·10⁸`.

**Explicitly not attempted:** any `complete_interpolation` certificate; any
rebuild of `(10,6,6,6,2,2)₈` beyond its orbit-setup half; any claim about
`D_6^{per₃}`, `i_red`, Lemma T, or LMR.

---

## 9. Expectations, labelled, with the observed/blind distinction stated

`n_χ`'s *estimate*, `a`, `N_S` and `|Stab|` are already in the tree (§3), so
E2's subject is the **direction and size of the estimator's error**, which is not
observed for this cell, and E3's prior is s79's own P3.

| id | statement | prior | why |
|---|---|---|---|
| **E1** | the build completes inside `ulimit -v 7000000` | **0.85** | B13-10's lean rate 0.99–2.48 GB per `10⁸` of `N_S·δ` puts `2.16·10⁸` at 2.1–5.4 GB, and `blocks='disk'` takes a further 17–36 % off; the risk is the 4.6× extrapolation gap, not the central estimate |
| **E2** | measured `n_χ` **exceeds** `ceil(N_S/\|Stab\|) = 225,081` | **0.70** | the one Q1 cell with a measured value has it 5.1 % above the quotient; the mechanism (twisted orbits, incompatible ones discarded) has no sign guarantee, which is exactly why the index forbids the quotient |
| **E2′** | measured `n_χ ∈ [225,081, 250,000]` | **0.60** | a 0–11 % excess bracket around the pilot's 5.1 % |
| **E3** | `i_det = 0` | **0.75** | s79's own P3 at 0.75, plus 682 six-row cells and the B13-10 pilot all at `i_det = 0`, against which this is the largest and least-sampled cell of the queue |
| **E4** | Control N reads rank 0 at both primes, and all five deliberate-failure inputs fire | **0.95** | forced by representation theory; the 0.05 is the machinery, which is what the failure inputs test |
| **E5** | whole-cell peak **below** the pilot's 4.53 GB | **0.55** | `n_χ` ≈ 7× smaller should shrink the kernel phase that set the pilot's peak, and `fo='inplace'` saves ≈ 0.7 GB — against `N_S` 1.47× larger, which grows `E` and the build |
| **E6** | at least one stretch family reached | **0.50** | priced at ≈ 6 CPU-minutes on top by B13-10, but the budget is the window, not the CPU |
| **E7** | `nnz(E)` exceeds the pilot's 110,695,059 | **0.65** | `nnz` tracked `N_S` across B13-10's suite and `N_S` is 1.47× larger here; `n_χ` bounds columns, not nonzeros |

A prediction that misses is reported as missed, with the number.

---

## 10. Defects in the assignment, as found at pre-registration time

Reported here because §9's expectations depend on two of them. Carried into the
report with anything found later.

1. **No dispatch message stated the expected commit and tree**, though the packet
   says it does and instructs this session to check them. Substituted a
   two-clone comparison and labelled it as weaker (§Base).
2. **The slot's own sizing rests on `N_S/|Stab|`**, which `PROVED.md:
   nchi_2_21_guard` and board §1 both forbid as a bound — and which
   under-estimates by 5.1 % on the only Q1 cell where the truth is known (§4).
   "Compresses `n_χ` sevenfold" is an estimate of a ratio of estimates.
3. **`build_no_longer_binding` is cited as an input, and it is an
   extrapolation above `1.47·10⁸`.** This cell at `2.16·10⁸` sits in the
   extrapolated region, not the measured one. The board's "budget for the
   kernel, not the builder" is right about the pilot and is being applied to a
   cell whose `n_χ` is ~7× smaller and whose `N_S` is 1.47× larger — i.e. to a
   cell where the two phases scale in **opposite** directions from the case the
   advice was drawn from. Both are budgeted here; neither is assumed.

---

**Committed before any measurement.** Dated addenda, if any, are committed before
the measurements they govern.
