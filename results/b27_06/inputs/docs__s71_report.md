# Session 71 — the `r = 5` containment falsifier, in cost order (C4, batch 11)

Branch `s71-falsifier` off `main` at `226b4ef1` (ancestry gate passed); bundle
`s71_falsifier.bundle` (single ref, prerequisite `226b4ef1`) + `.md5`.
Pre-registration `results/PREREG_s71.md` (commit `b331e34`, **before any new
measurement**) with the frozen queue `results/s71_queue.json`.  Calibration
`results/s71_calibration.{md,jsonl}`; the per-cell table `results/s71_sweep.md`
with raw records `results/s71_sweep.jsonl`; certificates `results/certs/s71/`;
independent re-derivations `results/s71_verify.jsonl`; cost curve
`results/s71_cost_curve.{json,png}`; per-4 dominance
`results/s71_per4_dominance.json`; code `analysis/wk11_s71_*.py` and the C
helper `analysis/wk11_s71_schur.c`; logs `results/logs/s71_*`.  Labels:
**proved** / **measured** / **adopted** / **expectation**.  Single-writer files
untouched; no session-link trailer (standing rule).

**Provenance (stated up front, PREREG §0).** Session 67's bundle
(`s67_certification.bundle`) was on neither the public clone nor the laptop's
`Projects\gct`, and the desktop app was unavailable to grant access elsewhere.
Its two contributions this session rests on — the monomial code widened past the
int64 wall, and the initial-term full-rank certifier — are **re-implemented from
the session-67 record** as `analysis/wk11_s71_codes.py` and
`analysis/wk11_s71_hybrid.py`.  The widened code is asserted bit-identical to the
int64 code below `δ = 20` (self-test in the module) and the two implementations
of session 67's ideas have not been compared line for line.
`docs/batch11_worker_preamble.md` and `docs/batch11_plan.md` are, as for
batch 10, in neither tree; the session ran from the brief.

## 0. Verdict

> **No falsifier.  The sweep reached the 151 cheapest of the 976 open closing
> cells — every closing cell whose `n_χ ≤ 1.9·10⁵` — and `i_det = 0` at every one
> of them, proved: full column rank of `[E; ev_det]` at both house primes gives
> `mult_det = a` over `Q` (`docs/sparse_det_route.md` Lemma 2).  With
> session 60's 99, **250 of the 1 075 length-5 tails (23.3 %) are now closed for
> `D > 0` in every degree**, 513 census rungs settled, and the first length-5
> cells at `δ = 18, 19, 20` are measured.  `I(D_5^{det_4})` still has no length-5
> element anywhere it has been looked for — now through `δ = 20` and `a` up to
> 640.  Containment `R_5 ⊆ D_5` survives the whole affordable prefix.**
>
> * The reducible side bit at **25** of the newly closed tails, `i_red(∞)` from 1
>   to **26** (`(40,11,11,1,1)_16`), always in the direction containment predicts
>   (`0 = i_det < i_red`, so `D < 0`).  Every one has a tail of the shape
>   `(x, y, 1, 1)` or `(x, y, z, 1)` — the family where session 60 found its
>   bites; no reducible-first tail of any other shape appeared.  **E2 confirmed.**
> * The `per_4` column is a **theorem, not a measurement**: the unpadded `per_4`
>   pencil map is dominant on `Sym^4 C^5` (Jacobian rank 70 at three integer
>   points, both primes; the `det_4` control gives 50 = dim D₅ = 16r − 30), so
>   `I(Per_5) = 0` and `i_per4 = 0` everywhere.  The engine returned `i_per4 = 0`
>   at all 151 cells and all 72 calibration cells — a two-sided control passed
>   223 times.  **E3 confirmed.**
> * The instrument is new and it is the session's second deliverable.  Session
>   67's initial-term cover, finished by an **exact Schur-complement kernel** on
>   the uncovered ~0.1 % of the columns, produces the full mod-`p` kernel of the
>   raising operator — session 60's dense route run on the residual instead of
>   the whole space.  On the 72 banked calibration cells it reproduces every
>   session-60 number exactly, the eleven `mult_red < a` cells included; on the
>   two large cells re-derived by session 60's Wiedemann route it agrees exactly,
>   at **1/300 of the wall time**.
> * Where the rate flattened: the sweep was stopped by the pre-registered
>   information-rate rule (§6), not by a wall.  151 consecutive `i_det = 0`, the
>   cost per closed tail climbing from seconds to ~10 min while the signal stayed
>   flat.  The residue is the balanced corner, `n_χ` from `1.6·10⁵` up; §6 states
>   what a further night buys and why the determinant side cannot be sieved.

## 1. The question and the falsifier (proved inputs)

`R_5 ⊆ D_5 ⟹ I(D_5) ⊆ I(R_5) ⟹ i_det ≤ i_red` at every cell, with
`i_det = a − mult_det`, `i_red = a − mult_red` the `λ`-highest-weight slices of
the two ideals (functoriality, `docs/brief_wording.md` §7).  One exact cell with
`i_det > i_red` refutes containment — `D = mult_red − mult_det = i_det − i_red >
0`, the programme's first `D > 0` with no transfer gap (`P_5 = R_5`, washout
Thm 2).  Since every length-5 cell ever measured has `mult_det = a`, hence
`i_det = 0`, the falsifier is the first cell with `i_det ≥ 1` and `i_red = 0`: a
length-5 highest-weight vector of `I(D_5)` at a weight where `I(R_5)` has none.
No length-5 element of `I(D_5^{det_4})` has ever been exhibited (the singularity
lemma gives the quinary-quartic discriminant, degree `5·3^4 = 405`, weight
`(324^5)`; nothing below it is named).

**Why the closing cells, and only they.** By the ladder theorem (session 60 §4;
session 57's Lemma L / Proposition S, adopted, proof re-derived there) the
quantities `a, mult_det, mult_red, i_det, i_red` are non-decreasing along a tail
`ρ` and constant from `δ_close(ρ)` on.  So the closing cell `(λ_close, δ_close)`
carries the tail's stable `i_det` and `i_red`; `i_det = 0` there closes the tail
for `D > 0` in **every** degree, and if any rung of a tail is the falsifier its
closing cell is one.  The queue is therefore the 976 closing cells session 60
did not reach — its 99 closed tails re-derived from `results/s60_cells.jsonl` at
queue construction (exactly 99, all at `δ_close`, all `i_det = 0`).

## 2. The instrument

### 2.1 The sieve and its honest limit

For a column order `σ`, rows with pairwise distinct `σ`-leading columns are
independent (order by leading column: triangular with nonzero diagonal on those
columns), so `#distinct leading columns ≤ rank F` for every `σ`, every field —
session 67's initial-term certifier.  Five orders per cell (natural, reversed,
fill ascending/descending, one random); **the reversed order gave the largest
cover at all 151 cells and all 72 calibration cells.**

What it certifies: on `E_red`, reaching `n_red` proves `mult_red = a`
(`i_red = 0`) point-free at `O(nnz)`.  On `E`, reaching `n_χ − a` certifies
`rank_p E = n_χ − a`.  What it cannot certify — **the determinant side**, at any
cell with `a ≥ 2`: the `a + 8` evaluation rows are dense and share at most one
leading column, so the count stops short by `a − 1`.  This is session 67's
"defeated by the dense evaluation rows", structural, not a matter of a better
order.  So on the determinant side "sieve first, hybrid for the residue" is the
hybrid at every cell; the sieve's role there is the **cover** it hands the
hybrid (`|S|` rows, `|U| = a + excess` columns left).  On the reducible side the
sieve closed 8 of the 72 tiny calibration cells outright and **none** of the 151
sweep cells (B5 refuted): a balanced weight's (★) columns are not cover-complete,
so `i_red` came from the exhibited kernel instead — which is why the eleven
`mult_red < a` calibration cells are the load-bearing test of the engine.

### 2.2 The hybrid: the exact kernel on the residual

With `T = R_1[:, S]` upper-triangular (invertible mod `p`) and
`X = T^{-1} R_1[:, U]`, every kernel vector has `y_S = −X y_U`, so
`nullity(F) = nullity(S_U)` for the Schur complement
`S_U = F_o[:, U] − F_o[:, S] X` on the uncovered columns.  `S_U` is projected by
a random sparse `±1` matrix with `|U| + 64` rows (nullity can only rise under
projection), its kernel is taken exactly by `python-flint`, every vector is
lifted by a triangular solve and **verified on the full sparse `E`**; the
projected nullity must equal the number of verified vectors (it did, first
attempt, every cell and prime).  The result is the full mod-`p` kernel `K`
(`n_χ × a`), and session 60's dense route runs on it: `mult_det =
rank_p(ev_det·K)`, `mult_per4 = rank_p(ev_per4·K)`, `mult_red(pts) =
rank_p(ev_red·K)`, and `mult_red(★) = rank_p(K[non-red rows])` — the last exactly,
by a `±1` projection that either attains `a` (a proof) or hands over `a − r`
combinations verified to vanish on `K[non-red]` (so the rank is `r`).  `X` is
never held whole — formed in column blocks of `U`, each block's Schur columns
projected and discarded — so the only memory wall left is the build.  Both primes
at every cell; a full rank at one prime proves `mult = a` over `Q`.  The 27
`δ_close = 20` cells build through the widened monomial code
(`analysis/wk11_s71_codes.py`: int64 combinadic bit-identical below `δ = 20`, a
two-part mixed code with an injectivity assertion above it).

### 2.3 Calibration and independent verification

**Calibration (`results/s71_calibration.md`, E5 confirmed):** 72 banked
session-60 cells — the 60 closing cells with `n_χ ≤ 6 000`, the eleven
`mult_red < a` cells with `(24,4,4,4,4)_10`, the three largest closed cells —
reproduced **exactly** at both primes (`a`, `mult_det`, `mult_red(★)`,
`mult_red(pts)`), `mult_per4 = a` at all.

**Independent re-derivation (`results/s71_verify.jsonl`):** session 60's
Wiedemann route (`wk9_s60_cell.py`, unchanged, same point seeds — the matrices
are identical, only the rank algorithm differs) reproduced the hybrid at
`(43,15,4,1,1)_16` (`mult_det/★ = 107/106`, 3 094 s vs the hybrid's 10 s) and
`(32,9,9,1,1)_13` (`60/57`, 2 481 s vs 13 s) — both reducible-first cells, so
both the determinant full rank and the reducible drop cross-checked.  No
disagreement with any banked `a`, `mult_det` or `mult_red` anywhere; stopping
rule 3 never fired.

## 3. The cost model and the order (PREREG §2, `results/s71_calibration.md`)

The pre-registered form was `t = t_build + t_sieve + t_hybrid`.  Calibration
showed the hybrid term is **never** the cost (≤ 1.5 s at `n_χ = 22 000`; ≤ 55 s
one-prime at the largest sweep cell) and that two terms the prior did not carry
dominate: the build (`2.1·10⁻⁶ s` per `N_S·δ`) and the evaluation rows
(`2.7·10⁻⁸ s` per point per `N_S·δ`, three families of `a + 8` points).  The
re-fit added them; **the queue order was frozen at the prior and not changed by
the re-fit** (PREREG §2).  Actual cost ran at a median 0.49 of the re-fitted
prediction (the re-fit's `f = 0.013` uncovered fraction was the worst
calibration cell; the sweep's excess-fraction median was 0.10 %, p90 0.25 %,
max 0.48 %).  **C1 refuted** (the prior `c_h` was pessimistic, not optimistic —
it priced the wrong term).  **C2 confirmed in the strongest form:** the hybrid is
not `5×` but two-to-three orders of magnitude cheaper than the Wiedemann route at
every cell with `n_χ ≥ 2·10⁴` (`(43,15,4,1,1)_16`: 10 s against 3 094 s, the
Wiedemann route needing all three escalation levels at one prime).

A per-cell and per-phase timing table is in `results/s71_calibration.md`; the
sweep table `results/s71_sweep.md` carries prior, re-fitted and actual cost for
every cell.

## 4. Results (`results/s71_sweep.md`)

151 cells measured (queue ranks 1–151), every one:

* `i_det = 0` — **proved** (full column rank of `[E; ev_det]` at both primes ⟹
  `mult_det = a` over `Q`), the tail closed for `D > 0` in every degree;
* `i_per4 = 0` — the dominance theorem, reproduced by the engine;
* both primes agree, `(★) = points` on the reducible side (E4 confirmed);
* `n_χ` from 13 252 to 193 330, `a` from 2 to 640, `N_S` up to 1 139 653,
  `δ` up to 20; total compute 3.40 h (both primes), peak 5.48 GB.

**No cell had `i_det ≥ 1` (F2 not observed), `D > 0` (F1 not observed) or
`i_per4 > 0`.**  E1 confirmed.

**The reducible side (25 newly closed reducible-first tails, `i_red(∞) ≥ 1`).**
Read with the ladder theorem each `i_red(∞)` is the exact stable dimension of
`I(R_5)`'s highest-weight slice on that tail, biting where `I(D_5)` does not:

| λ_close | δ | tail ρ | a_∞ | h_pad | i_red(∞) | census rungs settled |
|---|---|---|---|---|---|---|
| `(40,11,11,1,1)` | 16 | `(11,11,1,1)` | 187 | 202 | **26** | [9,10] |
| `(41,13,8,1,1)` | 16 | `(13,8,1,1)` | 510 | 724 | 24 | [9,10] |
| `(37,11,10,1,1)` | 15 | `(11,10,1,1)` | 248 | 327 | 20 | [9,10] |
| `(48,15,7,1,1)` | 18 | `(15,7,1,1)` | 640 | 924 | 17 | [10] |
| `(38,11,9,1,1)` | 15 | `(11,9,1,1)` | 273 | 372 | 16 | [9,10] |
| `(38,12,8,1,1)` | 15 | `(12,8,1,1)` | 338 | 527 | 10 | [9,10] |
| `(45,14,7,1,1)` | 17 | `(14,7,1,1)` | 493 | 746 | 7 | [10] |
| `(35,10,9,1,1)` | 14 | `(10,9,1,1)` | 137 | 208 | 6 | [8,9,10] |
| `(35,11,8,1,1)` | 14 | `(11,8,1,1)` | 234 | 367 | 6 | [8,9,10] |
| `(45,15,6,1,1)` | 17 | `(15,6,1,1)` | 393 | 650 | 4 | [10] |
| `(48,16,6,1,1)` | 18 | `(16,6,1,1)` | 469 | 780 | 4 | [10] |
| `(32,9,9,1,1)` | 13 | `(9,9,1,1)` | 60 | 82 | 3 | [8,9,10] |
| `(34,10,10,1,1)` | 14 | `(10,10,1,1)` | 83 | 138 | 3 | [9,10] |
| `(29,9,8,1,1)` | 12 | `(9,8,1,1)` | 71 | 126 | 2 | [7,8,9,10] |
| `(42,13,7,1,1)` | 16 | `(13,7,1,1)` | 379 | 587 | 2 | [9,10] |
| 10 further tails | | `(15,4,1,1)`,`(10,8,1,1)`,`(17,4,1,1)`,`(16,5,1,1)`,`(12,7,1,1)`,`(15,5,1,1)`,`(15,3,3,1)`,`(8,8,2,1)`,`(16,3,3,1)`,`(7,5,5,1)` | | | 1 | |

The `(4,4,4,4)` tail (session 60) remains the only reducible-first tail whose
shape is not `(x, y, ·, 1)`; every one found here ends in a 1, consistent with
session 60's record (`(9,8,1,1)`, `(11,8,1,1)`, `(9,9,1,1)`, `(13,8,1,1)`,
`(15,4,1,1)`).

**Firsts.** The first length-5 cells at `δ = 18` (`(50,17,2,2,1)`, …),
`δ = 19` (`(54,16,2,2,2)`, `(53,17,3,2,1)`) and `δ = 20`
(`(57,17,2,2,2)`, built through the widened code with exact `n_χ = 36 488`
against the census estimate 28 222) — session 60 stopped at `δ = 17`.  Cells
with `a` to 640 and `N_S` past `10^6`.

## 5. Pre-registration scorecard

| id | statement | prior | outcome |
|---|---|---|---|
| F1 | a reached cell with `i_det > i_red` (containment refuted) | 0.03 | **not observed** (151 cells) |
| F2 | a reached cell with `i_det ≥ 1` | 0.07 | **not observed** |
| E1 | `mult_det = a` at every reached cell | 0.93 | **confirmed** |
| E2 | a newly closed reducible-first tail | 0.55 | **confirmed** (25) |
| E3 | `per_4` dominant, `i_per4 = 0` everywhere | 0.90 | **confirmed** (proved; 223 reproductions) |
| E4 | `(★) = points`, primes agree everywhere | 0.97 | **confirmed** |
| E5 | calibration exact | 0.90 | **confirmed** (72/72) |
| B1 | ≥ 40 tails newly closed | 0.70 | **confirmed** (151) |
| B2 | ≥ 100 | 0.35 | **confirmed** (151) |
| B3 | a hybrid cell with `n_χ ≥ 10⁵` | 0.60 | **confirmed** (max 193 330) |
| B4 | excess ≤ 0.6 % `n_χ` at every hybrid cell | 0.60 | **confirmed** (max 0.48 %) |
| B5 | sieve closes the reducible side outright at ≥ 50 % | 0.50 | **refuted** (0 of 151 sweep cells; 8 of 72 tiny calibration cells) |
| C1 | prior `c_h` optimistic by ≥ 5× | 0.60 | **refuted** (pessimistic; the cost is build + evaluation, not the hybrid) |
| C2 | hybrid ≥ 5× cheaper than `t_wied` at `n_χ ≥ 2·10⁴` | 0.65 | **confirmed** (two-to-three orders) |
| C3 | the affordable prefix ends below rank 200 | 0.80 | **confirmed** (stopped at 151 by the rate rule) |

Unregistered: none of substance; the reducible-first count and the `δ = 18–20`
firsts are consequences of the coverage the queue reached.

## 6. Where the information rate flattened, and what a further night buys

**The cost curve (`results/s71_cost_curve.{json,png}`).** Cumulative wall: 0.2 h
at rank 62 (`n_χ = 42 169`), 0.5 h at rank 88 (`n_χ = 89 664`), 1.0 h at rank
109 (`n_χ = 97 814`), 2.0 h at rank 128 (`n_χ = 108 108`), 3.4 h at rank 151
(`n_χ = 193 330`).  Per-cell cost is now `≈ c_b · N_S · δ` — the build — and
`N_S` grows steeply into the balanced corner: rank 151 cost ~6 min, the next
cells ~8–15 min each, all for one more `i_det = 0`.  The information rate — new
determinant equations per hour — has been exactly zero since cell 1; the sweep
was stopped by the pre-registered rule (PREREG §6.5), not by a wall.

**The residue, stated.** 825 of the 976 open closing cells remain, `n_χ` from
159 884 up.  The cheapest is `(47,14,4,2,1)_17` (`a = 406`, `n_χ = 159 884`,
rank 152), then `(34,8,6,2,2)_14`, `(41,12,9,1,1)_16`, `(23,7,4,3,3)_10`.  The
build wall of this container (`N_S · δ > 2·10⁸`, ~2-core / 7 GB) is not reached
until queue rank 393 (`(45,11,4,4,4)_17`, `N_S = 1.28·10⁷`); the 407 cells below
that wall but above rank 151 are reachable in principle but each costs minutes to
tens of minutes of build, with `n_χ` to `1.4·10⁷`.

**What a further night buys.** ~150–200 more tails closed (coverage from 23 % to
~35 % of the 1 075), no new signal expected — the determinant ideal is empty on
everything measured through `δ = 20`.  The honest read: the multiplicity route
**cannot** decide the closure question (session 54/59: the balanced corner is
only ever sampled by multiplicities, and no determinant equation appears below
degrees far out of reach), and this sweep is one more, now large, prefix of the
negative record.  A successor that wants coverage walks `results/s71_queue.json`
from rank 152; a successor that wants the closure question decided needs the
geometric route (s54/s59), not more cells.

## 7. Honest boundary

* **Proved:** every `i_det = 0` (full rank at both primes, Lemma 2); every
  `mult_red = a`; `per_4` dominance; the widened code's injectivity on every
  basis it touched (asserted, never failed).
* **Measured, exact mod both primes, kernel exhibited:** every `i_red > 0`.
* **Adopted:** the ladder theorem (session 60 §4 / session 57), Theorem (★),
  `h_pad` (Cor. B2), washout `P_5 = R_5`.
* **Not proved:** `R_5 ⊆ D_5` — a clean sweep is one more prefix of the negative
  record; the cheapest unclosed tail is now `(47,14,4,2,1)_17`.
* **Not this session's:** session 67's actual code — re-implemented from the
  record, not compared line for line.  The `hybrid_kernel` certificate kind is
  defined here (`results/certs/s71/`, recipe-style: cover order, `S`, `U`,
  projection seed, points, claims, and the kernel basis when `n_χ · a ≤ 400 000`)
  and is **not** verifiable by this tree's `tools/verify` (which predates
  session 67's format extensions); the independent check is the Wiedemann
  re-derivation of §2.3, not the format verifier.
* **Defect in this session's own workflow (no measured value affected):** an
  edit to `analysis/wk11_s71_hybrid.py` while the sweep was running made ~58
  queued cells fail at import (recorded as `not reached` in 0 s); the sweep was
  ended by its recorded pid, the spurious records removed, the module fixed and
  re-validated on the twelve `mult_red < a` cells through the new blocked path,
  and the sweep resumed from the same queue position.  Separately, running both
  primes concurrently oversubscribed the 2-core box on large-`a` cells (OpenBLAS
  threads, then memory); pinning BLAS to one thread and running primes
  sequentially for large cells fixed it — a speed matter only, never correctness.

## 8. For the integrator

* The closing-cell record: 99 → **250** tails closed (513 census rungs); the
  frozen queue `results/s71_queue.json` carries the order for a successor to
  continue from **rank 152**.
* **The hybrid should replace the Wiedemann route as the house instrument below
  the build wall:** identical numbers on everything banked, `10²–10³×` cheaper,
  and it hands back the kernel basis `K` — session 65's `U_D` in source
  coordinates is a by-product wherever the build fits.  It is bounded by the
  build (`N_S · δ`), not by `n_χ²`, so it reaches `n_χ ~ 2·10⁵` in minutes.
* **The determinant side cannot be sieved** (the dense evaluation rows); the
  batch plan should say so — "sieve first" closes only reducible sides, and at
  length 5 not even those on balanced weights.
* **`per_4` at `r = 5` is a control, not a variety** (dominant, `I(Per_5) = 0`);
  a genuine `per_4` third column needs `r ≥ 6`, where `dim{per_4 forms} = 16r − 6
  < C(r+3,4) = dim Sym^4 C^r` (90 < 126 at `r = 6`).  It is a clean positive
  control the programme lacked and it passed 223 times.
