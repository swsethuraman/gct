# Pre-registration — session 71 (C4, batch 11): the `r = 5` containment falsifier, in cost order

Branch `s71-falsifier` off `main` at `226b4ef1` (the tip of the public clone and
of the laptop's `work/` at session start; `git merge-base --is-ancestor 226b4ef1
HEAD` passes).  Written and committed **before any new cell is measured**.  The
only computations preceding this file are a re-reading of the repository and the
queue construction of §3, which uses banked session-60 values only.  Labels in
the report: **proved** / **measured** / **adopted** / **expectation**, per
`docs/brief_wording.md`.

Standing constraints in force: delivery by git bundle, no push; single-writer
files untouched (`paper/*.tex`, `PROJECT_NOTES.md`, `docs/boundary_deficit.html`);
`Co-Authored-By` trailer only, no session-link trailer; every long run bounded by
`timeout` and `ulimit -v` with its process id in `results/logs/<run>.pid`, ended
only by that id; logs under `results/logs/`; nothing over 5 MB committed;
`python-flint` for every dense rank; both house primes `P1 = 2147483647`,
`P2 = 2147483629` at every cell; every cell banked with a commit as it completes;
any `D > 0` cell through the verification protocol (§7) before it is written as
a claim anywhere, including in conversation.

**Provenance note (stated up front).**  Session 67's bundle
(`s67_certification.bundle`, head `c1fe211`) is on neither the public clone nor
the laptop's `Projects\gct`, and the desktop app was not available to grant
access to any other folder.  Its two contributions this session depends on —
the widened monomial code (`wk9_s42_orbits._codes`, int64 wall at `δ = 20`) and
the initial-term full-rank certifier — are **re-implemented here from the
session-67 record** (`docs/session_67.md` in the project), under the names
`analysis/wk11_s71_codes.py` and `analysis/wk11_s71_hybrid.py`.  Bit-identity of
the widened code with the int64 code below the wall is asserted (the int64 path
is unchanged below `δ = 20`); nothing of session 67's code is claimed to be
reproduced verbatim.  `docs/batch11_worker_preamble.md` and `docs/batch11_plan.md`
are, as for batch 10, in neither tree; the session runs from the brief.

## 0. The question (proved inputs; nothing new is proved here)

`D_5 := D_5^{det_4} = closure{det_4(Σ s_i A_i)} ⊆ Sym^4 C^5`, `dim D_5 = 50`
in `dim Sym^4 C^5 = 70`; `R_5 = {ℓ·c}`, `dim 39`; `P_5 = R_5` (washout Thm 2),
so `mult_pad = mult_red` at every length-5 cell (Thm 3(1)).  Functoriality
(`docs/brief_wording.md` §7):

    R_5 ⊆ D_5  ⟹  I(D_5) ⊆ I(R_5)  ⟹  i_det ≤ i_red   at every cell,

with `i_det = a − mult_det`, `i_red = a − mult_red` the dimensions of the
`λ`-highest-weight slices of the two ideals.  **One exact cell with
`i_det > i_red` refutes `R_5 ⊆ D_5`** — equivalently `D = mult_red − mult_det =
i_det − i_red > 0` (the house convention).  It needs no exhaustion theorem.

Every one of the 419 length-5 cells session 60 measured (and the 326 of
session 57's record, and every cell of sessions 54, 28, 32) has `mult_det = a`,
hence `i_det = 0`, hence `i_det ≤ i_red` trivially.  So the falsifier sought
is precisely **the first `r = 5` cell with `i_det ≥ 1` and `i_red = 0`** — a
length-5 highest-weight vector of `I(D_5)` at a weight where `I(R_5)` has none.
No length-5 element of `I(D_5)` has ever been exhibited below degree 80
(`docs/d5_ideal.md` is the `det_3` analogue; at `det_4` the singularity lemma
gives the quinary-quartic discriminant, degree `5·3^4 = 405`, weight `(324^5)`).

**Why the closing cells, and only they.**  By the ladder theorem (session 60
§4, proved; session 57's Lemma L / Proposition S), along a tail `ρ` the
quantities `a, mult_det, mult_red, i_det, i_red` are non-decreasing in `δ` and
constant from `δ_close(ρ)` on.  Hence at the closing cell `(λ_close, δ_close)`:

* `i_det = 0` closes the tail for `D > 0` in every degree (session 60);
* `i_det ≥ 1` there is the stable determinant-ideal dimension of the tail, and
  is the largest `i_det` the tail ever has — if any rung of a tail is the
  falsifier, the closing cell is one (`i_red` is also stable there, so
  `i_det − i_red` at the closing cell is the ladder's stable `D`, and `D` is
  non-decreasing along the ladder only in the sense that both terms are; a
  rung below `δ_close` with `D > 0` would force `i_det ≥ 1` at the closing cell
  too).  **So a closing cell with `i_det = 0` is never the falsifier and
  neither is any rung of its tail; a closing cell with `i_det ≥ 1` is the only
  place a length-5 determinant equation can first be seen by this sweep.**

The census of tails is session 60's (`results/s60_tail_census.json`): 1 075
tails, 1 075 closing cells.  Session 60 closed 99 of them (57 closing cells run,
42 closed by census cells at or above `δ_close`, all `i_det = 0`; re-derived
from `results/s60_cells.jsonl` at queue construction: exactly 99, all at
`δ = δ_close`).  **The queue is the 976 open closing cells.**

## 1. Instruments

Fix a closing cell `(λ, δ)`, `ℓ(λ) = 5`, `n = 4`.  `V_χ` the `χ_λ`-isotypic
reduction (`docs/stabiliser_reduction.md`), `dim V_χ = n_χ`; `E` the stacked
simple raising operators on `V_χ` (`analysis/wk9_s45_build.py`, unchanged
except for the monomial code widening below); `dim ker_Q E = a` (Weyl
alternation, `wk9_s42_census.a_weyl`, asserted equal to the census value).

**Three evaluation families, one build.**

| column | family | value | what a full rank proves |
|---|---|---|---|
| `mult_det` | `K = a + 8` random `det_4` pencils, seed 11, entries in `[−40, 40]` (session 60's points, so re-derivations are comparable) | `a − nullity_Q[E; ev_det]` (Lemma 1, `docs/sparse_det_route.md`) | `nullity_p = 0` at one prime ⟹ `mult_det = a` over `Q` (Lemma 2) |
| `mult_red` | point-free by (★) (`docs/reducible_ideal.md` Thm 1): `a − nullity_Q(E_red)`; and by `K` reducible points `ℓ·c`, seed 29 | exact by (★); points give `mult_red ≥ rank` | `nullity_p(E_red) = 0` ⟹ `mult_red = a`; `mult_red ≤ h_pad` (Cor. B2) is asserted |
| `mult_per4` | `K` random **unpadded `per_4`** pencils, seed 47 (new, fixed here), entries in `[−40, 40]` | `a − nullity_Q[E; ev_per4]` (Lemma 1 verbatim for the variety `Per_5 = closure{per_4(Σ s_i A_i)}`) | `nullity_p = 0` ⟹ `mult_per4 = a` over `Q` |

The `per_4` column is the brief's free third column.  `dim{per_4 forms in 5
variables} = 16·5 − 6 = 74 ≥ 70 = dim Sym^4 C^5` if the pencil map is
dominant; whether it is, is settled **before the sweep** by the rank of its
Jacobian at a random integer point mod both primes (`rank_p ≤ rank_Q`, so
`rank_p = 70` proves dominance).  If dominant, `I(Per_5) = 0`, `i_per4 = 0` is
a theorem at every cell, and the column is a **two-sided engine control**: any
`i_per4 > 0` is an engine defect and halts the sweep (§6).  If not dominant, the
column is a third variety and is reported as such.

**Routes (chosen by size, recorded per cell).**

1. **Degeneration sieve (re-implemented initial-term certifier).**  For a
   column order `σ`, rows of a matrix `F` with pairwise distinct `σ`-leading
   columns are linearly independent (echelon argument), so
   `#distinct leading columns ≤ rank F` for every `σ`.  Applied to `E_red`:
   reaching `n_red` **certifies `nullity_p(E_red) = 0`, hence `mult_red = a`,
   `i_red = 0`, at `O(nnz)`** — the cell's reducible side is closed without a
   rank.  Applied to `E`: reaching `n_χ − a` certifies `rank_p E = n_χ − a`
   (already known over `Q`); it never certifies the determinant side, because
   the `a + 8` evaluation rows are dense and contribute at most one leading
   column between them (session 67 Part B, "defeated by the dense evaluation
   rows").  The sieve is therefore expected to close **reducible** sides
   outright and to leave every determinant side to route 2 with a residual.
   Orders tried per cell: natural, reversed, column-fill ascending, column-fill
   descending, one random order (seed 20260908); the best cover is kept.  The
   sieve is used as a sieve and never as evidence of a drop (a shortfall is
   uninformative).
2. **Hybrid (the session-67 successor).**  Let `S` be the covered columns
   (`|S|` cover rows `R_1` in echelon form, `T = R_1[:, S]` triangular with
   nonzero diagonal, hence invertible mod `p`) and `U` the uncovered columns.
   With `X = T^{-1} R_1[:, U]` (a triangular solve, `O(nnz(T)·|U|)`), every
   kernel vector satisfies `y_S = −X y_U`, and `nullity(F) = nullity(S_U)` for
   the Schur complement `S_U = F_o[:, U] − F_o[:, S] X` of the remaining rows
   `F_o`.  `S_U` is projected by a random sparse `±1` matrix `P` with
   `|U| + 64` rows (seed `20260908 + prime`), its kernel is computed exactly by
   `python-flint`, and **every kernel vector is lifted and verified against
   the full sparse `E`**.  For `F = E` this exhibits the full mod-`p` kernel
   basis `K` (`n_χ × a`): `nullity_p(E) ≥ a` from the verified vectors,
   `≤ nullity_p(P S_U)` from the projection; equality is required, and a
   projection with `nullity_p(P S_U) > a` is retried with more rows, never
   accepted.  Then `mult_det = rank_p(ev_det · K)`, `mult_per4 =
   rank_p(ev_per4 · K)`, `mult_red(pts) = rank_p(ev_red · K)` (small `K × a`
   matrices, exact), and `mult_red(★) = rank_p(K[non-red rows])` (exact tall
   rank, or its random projection when that already attains `a`).  All of
   this is the dense route of session 60 (`wk9_s41_kernel` semantics) run on the
   residual instead of the full space; a full rank at one prime is a proof by
   Lemma 2; a drop is a measurement until §7.  Both primes at every cell.
3. **Wiedemann (session 45/60 route, unchanged code `wk9_s45_cell.nullity_stacked`
   / `wk9_s60_cell.nullity_floor`).**  Fallback where the hybrid's memory
   bound (§2) is exceeded, and the independent instrument of §7.  Nothing in
   this session changes it.

**Calibration before the sweep (banked cells only, no new information).**  The
hybrid must reproduce session 60's values **exactly** — `a, mult_det,
mult_red(★), mult_red(pts)` at both primes — on: every closing cell of the
session-60 closing table with `n_χ ≤ 6 000` (dense-route and sparse-route
cells), the eleven `mult_red < a` cells of session 60 §3 (the only nontrivial
reducible kernels at length 5 — a route that always answers full rank would
pass everything else), and the three largest closed cells (`(24,4,4,4,4)_10`
with `i_red(∞) = 1`, `(22,5,4,4,1)_9`, `(16,7,3,3,3)_8`).  The
`per_4` column is calibrated on the same cells (expected `a` everywhere if
dominant).  **Any disagreement with a banked value halts the session** and is
reported as a defect, not worked around.

## 2. The cost model (pre-registered form and prior constants)

For a closing cell with `N_S, n_χ, a, δ` from the census (`n_χ` exact where
`close_n_chi_exact`, else the `N_S/|Stab|` estimate), with `nnz(E) ≈ ρ n_χ`,
`ρ = 10` (session-60 median 11.0, range 6.6–96), and the uncovered residual
`|U| ≈ a + f n_χ`, `f = 0.005` (session 67: 99.4–99.9 % covered):

    t_build   = c_b · N_S · δ                    c_b = 1.5e-6 s   (s60 median on N_S > 5e4)
    t_sieve   = c_c · nnz · 5 orders             c_c = 2e-7 s
    t_hybrid  = c_h · nnz · |U| + c_v · nnz · a  c_h = 1e-7 s, c_v = 2e-8 s   (prior, no measurement yet)
    mem_hyb   = 8 · n_χ · |U| + 8 · (|U| + 64) · n_χ   bytes     (X and the projected rows)
    t_wied    = 3 · 1e-8 · n_χ² · (14.5 + a)     per prime (s60's law; det + (★) + one retry)

Route by prediction: hybrid if `mem_hyb ≤ 5·10^9`; else Wiedemann if
`t_wied < 7 days`; else **beyond reach** of this container.  **The certified
cost of a cell is `t_build + t_sieve + t_hybrid` (hybrid) or `t_build +
t_wied` (Wiedemann), computed from the census before the cell is run and
recorded in `results/s71_queue.json` (frozen with this file).**  After the
calibration run the constants are re-fitted and the re-fitted prediction is
recorded beside the prior one; **the order is not changed by the re-fit**.

**The induced order (frozen).**  Ascending prior certified cost, ties by
`n_χ`.  Under the prior constants: 171 cells route hybrid (through rank 171,
`(50,15,4,2,1)_19`, `n_χ ≈ 2·10^5`), 24 route Wiedemann, **781 are beyond
reach** (`n_χ` from `2.4·10^5` to `3.6·10^9`; every one of the 27 `δ_close = 20`
cells except `(57,17,2,2,2)_20`, rank 28, is among them).  The first cells are
`(37,13,4,1,1)_14` (`a = 71`, `n_χ = 13 252`), `(29,9,3,2,1)_11`,
`(26,7,4,2,1)_10`, `(25,6,6,2,1)_10`, `(22,6,5,2,1)_9`, `(34,11,5,1,1)_13`.
The prior cumulative curve reaches one hour of predicted cost at rank 117
(`n_χ ≈ 1.3·10^5`); the prior is expected to be optimistic by an order of
magnitude in its constants (P-C1 below) — the order is what is frozen, not
the numbers.

## 3. Sweep protocol

For each cell in queue order: (i) build (`wk9_s45_build.build_cell` with the
widened code); (ii) `a` by the Weyl alternation, asserted equal to the census
`a_∞`; exact `n_χ`, `N_S`, `|Stab|` recorded (the census estimate is replaced by
the exact value in the ledger; the position in the queue is not changed);
(iii) sieve on `E_red` and on `E`; (iv) hybrid on `E` (both primes,
concurrently on the two cores) giving `K`; (v) `mult_det`, `mult_per4`,
`mult_red(pts)`, `mult_red(★)`; (vi) `i_det, i_red, i_per4, D`; (vii) one
JSON line appended to `results/s71_sweep.jsonl`, the certificate written, one
commit.  Wall clock per cell bounded by `timeout` at `10 × predicted`, floor
20 min, ceiling 4 h; memory by `ulimit -v 6.5 GB`.  A cell that hits its
bound is recorded as `not reached` with the bound, and the sweep continues.

## 4. Named falsifiers and expectations (priors)

| id | statement | prior | what confirms / refutes |
|---|---|---|---|
| F1 | some reached closing cell has `i_det > i_red` (`D > 0`): **the containment `R_5 ⊆ D_5` is refuted** — the sweep's object | 0.03 | one such cell, through §7 |
| F2 | some reached closing cell has `i_det ≥ 1` (a length-5 element of `I(D_5)` exhibited, at any `i_red`) | 0.07 | one such cell, through §7 |
| E1 | `mult_det = a` at every reached cell (the record continues) | 0.93 | complement of F2 |
| E2 | at least one newly closed tail is reducible-first (`i_red(∞) ≥ 1`, `i_det(∞) = 0`) | 0.55 | session 60 saw 1 in 99, on the most repeated-part tail |
| E3 | `per_4` pencils are dominant in `Sym^4 C^5` (Jacobian rank 70 mod both primes) and `i_per4 = 0` at every reached cell | 0.90 | the pre-sweep Jacobian; any `i_per4 > 0` afterwards is an engine defect (halt) |
| E4 | `mult_red(★) = mult_red(pts)` wherever both are computed, both primes agree everywhere | 0.97 | a disagreement halts (defect) |
| E5 | calibration reproduces every banked session-60 value exactly | 0.90 | a disagreement halts the session |

Coverage and cost:

| id | statement | prior |
|---|---|---|
| B1 | ≥ 40 tails newly closed tonight (`i_det = 0` at the closing cell) | 0.70 |
| B2 | ≥ 100 tails newly closed | 0.35 |
| B3 | the hybrid reaches a cell with `n_χ ≥ 10^5` | 0.60 |
| B4 | `|U| ≤ a + 0.006 n_χ` at every hybrid cell (session 67's 99.4 % lower figure holds on `E`) | 0.60 |
| B5 | the sieve closes the reducible side outright (`E_red` cover `= n_red`) at ≥ 50 % of reached cells | 0.50 |
| C1 | the prior hybrid constant `c_h` is optimistic by ≥ 5× | 0.60 |
| C2 | the hybrid is ≥ 5× cheaper than `t_wied` at every reached cell with `n_χ ≥ 2·10^4` | 0.65 |
| C3 | the affordable prefix ends (information rate flattens, §6) below rank 200 of 976 | 0.80 |

## 5. What is and is not claimed by each outcome

* `i_det = 0` at a closing cell (one prime suffices): **proved**, `mult_det = a`
  over `Q`; the tail is closed for `D > 0` in every degree (ladder theorem).
* `i_red = 0` by the sieve or by (★) at one prime: **proved**, `mult_red = a`.
* `mult_red < a` by (★) at both primes with the kernel exhibited: **measured,
  exact mod both primes**; `mult_red ≥ rank` proved.
* `i_det ≥ 1`: a **measurement** until §7 has run; then **measured at both
  primes, two instruments, fresh points**, with the vector exhibited; the
  char-0 statement is Schwartz–Zippel evidence plus the rigorous lower bound
  `mult_det ≥ rank`, exactly as session 63's `n = 3` control was labelled.
* Nothing here proves `R_5 ⊆ D_5`; a clean sweep is one more prefix of the
  negative record, and the report states where it stopped.

## 6. Stopping rules

1. A cell with `D > 0` (`i_det > i_red`) halts the sweep; §7 takes over; the
   result is written nowhere — not in the ledger's claim column, not in
   conversation — until §7 has run.
2. A cell with `i_det ≥ 1` and `i_red ≥ i_det` also halts the sweep for §7
   (it is F2, a first); the sweep resumes only after §7.
3. Any disagreement with a banked `mult_det`, `mult_red`, or `a` (calibration
   or sweep) halts the session; it is reported as a defect.
4. Any `i_per4 > 0` after E3 is proved, any prime disagreement, any
   `(★) ≠ points`, any kernel vector failing verification after the retry
   budget: halt, defect.
5. Information rate: the sweep ends when the next cell's re-fitted predicted
   cost exceeds the remaining wall budget (sweep budget: until 12:00 UTC on
   2026-09-08, then the report), or when the last three cells together cost
   more than everything before them and each closed one tail.  No compute
   is spent after that; the residue is stated.
6. Runs are bounded at launch (§3); nothing is ended by name matching.

## 7. Verification protocol for a drop (`i_det ≥ 1`), before it is reported

1. Both house primes agree on `mult_det` (already required).
2. Independent instrument: session 60's Wiedemann route (`wk9_s60_cell.py`,
   unchanged) at both primes on the same cell reproduces `mult_det` and
   `mult_red`.
3. Fresh evaluation points: `det_4` pencils at seed `20260908` and at
   `20260909`, bound `10^6` (not 40); the drop persists.
4. The ideal vector(s): `U_D = {K c : ev_det K c = 0}` exhibited in χ- and in
   monomial coordinates; verified `E·U_D = 0` on the full `E`; vanishing at 6
   fresh `det_4` pencils; **non-vanishing** at fresh reducible points `ℓ·c`
   (this is what `i_det > i_red` means: a point of `R_5` outside `D_5`) and
   at the ten-variable `ℓ·per_3` restricted to a generic 5-plane; nonzero at
   generic quartics.
5. Degeneracy pre-check (`docs/brief_wording.md` §5) on the committed test set
   (`tools/verify/testset`): the vector vanishes at the `det_4` pencil and at
   neither of the other two — the correct direction — or the claim stops there.
6. Independent source basis: the dense route's exact kernel of `E`
   (`wk9_s60_cell.kernel_dense`) where `n_χ` allows, else the Wiedemann
   kernel vectors, compared as subspaces with `K`.
7. Only then: `docs/s71_report.md` §"falsifier", the certificate, and the
   conversation.

## 8. Seeds and constants (fixed here)

`det` pencils seed 11 (s60), reducible points seed 29 (s60), `per_4` pencils
seed 47, bound 40, `K = a + 8`; hybrid projection seed `20260908 + p`, 64 extra
projection rows, retry ×2 rows up to 4 times; cover orders as in §1; fresh
seeds for §7: `20260908`, `20260909`, bound `10^6`.  Dense cap 4 000 (no open
closing cell is below 13 252, so every sweep cell runs the hybrid).

## 9. Deliverables

`results/PREREG_s71.md` (this file), `results/s71_queue.json` (frozen order),
`results/s71_calibration.md`, `results/s71_sweep.{md,jsonl}` (per cell: `a`,
`h_pad`, `i_det`, `i_red`, `i_per4`, `D`, certified cost prior and re-fitted,
actual cost, route, primes, cover sizes), `results/certs/s71/` (one JSON per
cell and prime, recipe-style: cover order, `S`, `U`, projection seed, points,
claims; kernel basis included when `n_χ · a ≤ 400 000`), code
`analysis/wk11_s71_{codes,hybrid,cell,sweep,calib,per4,report}.py`,
`docs/s71_report.md`, bundle `s71_falsifier.bundle` + `.md5`.
