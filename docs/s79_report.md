# Session 79 — the two independent frontiers (batch 12)

2026-09-08/09, branch `s79-frontiers` off `main = afb8c33`, pre-registration
`results/PREREG_s79.md` (committed 22:47 UTC before any measurement; addendum A
after the calibration and before the queues; A.5 after Part 1 ran).  Delivery by
bundle `s79_frontiers.bundle`; no push.  Both house primes everywhere.

Labels: **PROVED** (a theorem in the tree or a full rank at one prime, cited),
**MEASURED** (computed here), **RECORDED** (a mod-`p` kernel or a cost, not a
characteristic-zero statement), **ADOPTED** (the record), **EXPECTATION**.

---

## 0. Verdict

> **Part 1.**  The five `a_∞ = 4` weight-13 stable blocks — `(6,3,3,1)`,
> `(4,4,3,2)`, `(6,2,2,2,1)`, `(5,3,2,2,1)`, `(5,2,2,2,2)` — are all
> **determinant-full**: kernel dimension `4 = a_∞` at both primes, evaluation
> rank `4` at both primes, the covariance check PASS on every kernel vector,
> both negative controls failing as they must, every record re-derived by an
> independent checker.  **PROVED** (a full rank at one prime proves it over `Q`):
>
>     |ρ| = 13,  ℓ(ρ) ≤ 5  (i.e. at ℓ = 6)  and  a_∞(ρ) ≤ 4   ⟹   i_det^∞(ρ) = 0        (16 blocks: 4 + 5 + 2 + 5)
>
> No weight-13 stable determinant equation with `a_∞ ≤ 4`; the first possible
> one needs `a_∞ ≥ 5`; and by Proposition S every cell `(4δ − 13, ρ)` of those
> sixteen ladders has `i_det = 0` at **every** degree.  13 to 747 s per block;
> the brief's order-of-magnitude trigger did not fire (largest raw space 9 166
> against 12 479 in batch 11).
>
> **A correction to the census found while sizing it (§1.4):** four of the five
> blocks were already closed by the quartic record via Proposition S before this
> session — `(19,6,3,3,1)_8`, `(19,4,4,3,2)_8` (s60), `(19,6,2,2,2,1)_8`,
> `(23,5,2,2,2,2)_9` (s43), all `a = a_∞ = 4`, `mult_det = 4`.  Only
> `(5,3,2,2,1)` was open on both instruments, and the two instruments agree on
> it.  "Open" was counted against the stable instrument's own history, not the
> quartic record.
>
> **Part 2.**  Session 71's hybrid, made length-general and given session 64's
> padded family, runs `ℓ = 6` cells in **seconds** that batches 9–10 priced in
> hours: s47's four reducible drops at `δ = 8, 9` reproduce exactly, and
> `mult_pad = mult_red` at every `δ ≤ 8` cell as the theorem requires.  On the
> frozen Q1 queue — session 57's 123 six-row nominees (room-one cells and first
> stable cells of the open tails of weight 13–16) — **121 cells reached, and at
> every one `i_det = 0`, `mult_pad = mult_red`, `i_per4 = 0`** (§2.3): no
> six-row determinant equation, no permanent-specific equation, at tail weights
> 13–23 through `δ = 12`; 69 of them are first stable cells (`a = a_∞`), which
> by Proposition S close **63 tails** for every degree on every side.  One cell
> hit the build wall of the 7 GB box (`N_S·δ = 1.5·10⁸`) and one above the
> pre-registered cap (`2.2·10⁸`) was not attempted.  The
> broader Q2 census (every other six-row cell at `δ ≤ 12`, by cost) added
> **561 cells, all empty on every side** (§2.5) — 682 six-row cells in all.
>
> **The theorem route (addendum A.3):** on the cubic side,
> **`I(D_6^{per_3})_9 = 0`** — all 210 length-6 weights `μ ⊢ 27` with
> `a(μ,9) ≥ 1` have `mult = a` at both primes — so by Prop. 8(1) of the
> transfer lemma **`mult_pad = mult_red` at every six-row weight of degree 9 is
> a theorem**, one degree beyond s37/s43/s47 and with no points in it.  At
> `δ = 10`, 296 of the 402 weights (the `N_S`-cheapest, `N_S ≤ 1.70·10⁶`) are
> empty; the remaining 106 are priced and not reached (§2.4).
>
> **So the `ℓ = 6` padded frontier is a negative characterised over a stated,
> priced region:** the permanent is invisible on the reducible side through
> degree 9 at length 6 (and on the 296 cheapest degree-10 weights); no cell of
> the nominee queue or of the 561 cheapest census cells carries a determinant
> equation, a permanent-specific equation, or a `per_4` equation.  The first
> cell where `mult_pad < mult_red` can now occur has `δ ≥ 10`; at `δ = 10` it
> must contain one of the 106 unreached cubic weights (Prop. 8(2)), and at
> `δ = 11, 12` any weight `μ ⊢ 3δ` of length 6 is still possible.
>
> Every `mult_pad = mult_red` above is an equality of two ranks at both primes;
> it is a theorem at `δ ≤ 9` (Prop. 8(1)) and a measurement at `δ ≥ 10`.

---

## 1. Part 1 — the stable `a_∞ = 4` frontier at weight 13

### 1.1 What was pre-registered

PREREG §1: the five blocks in raw-space cost order; the batch-10 stable pullback
extended to `a_∞ > 1` and both primes; the nullity check `dim ker = a_∞`;
`K_pts = a_∞ + 8 = 12` integer points of `M_6`; the covariance check per kernel
vector with two negative controls; calibration on the eleven closed blocks
first; falsifiers F1-P1 (nullity or calibration or covariance fails) and F2-P1
(a control passes); P1 (0.85): all five die; stop at the first nonzero ideal.

### 1.2 The instrument (`analysis/wk12_s79_stable.py`)

Conventions are the batch-10 instrument's, verbatim: the 120 generators
`y_{(d,α)}` (`d = 2,3,4`, five variables); the raising rule
`E_{i,i+1} y_{(d,α)} = (α_i+1) y_{(d,α+e_i−e_{i+1})}` extended as a derivation;
the point map = the coefficients `(e_2, e_3, e_4)` of `det(tI − A(s'))` for a
traceless integer 5-pencil, through power sums as in the record.  New: the
kernel of the stacked raising operator is the exact `python-flint` nullspace of
a random dense projection `R·E` (`nc + 24` rows), **every vector re-verified on
the sparse `E`**, its dimension compared with the characteristic-zero `a_∞`
(`wk9_s57_stable.a_inf`).  `ker(R·E) ⊇ ker_p(E) ⊇ (L mod p)` with
`dim(L mod p) = a_∞`, so equality of the count pins `ker_p(E)` exactly and
identifies it with the reduction of the integral HWV lattice (PREREG A.5: the
pre-registration's wording was "sequential intersections"; the soundness
argument is the same and the randomness can only make a run inconclusive).
Then `G = ev·K` (`12 × 4`) at the twelve integer pencils reduced mod each
prime; `mult_det^∞ = rank_p G`; `rank_p G = a_∞` at one prime proves
`i_det^∞ = 0` over `Q` (`rank_p ≤ rank_Q`, Lemma 2 of
`docs/sparse_det_route.md`).

**Calibration (MEASURED, all reproduce; `results/s79_stable/calibration/`):**
the eleven closed blocks — `a_∞ = 1`: (7,2,2,1,1), (5,5,1,1,1), (5,3,3,2),
(5,3,3,1,1); `a_∞ = 2`: (11,1,1), (9,2,1,1), (6,3,2,1,1), (5,4,2,1,1),
(4,3,2,2,2); `a_∞ = 3`: (5,5,3), (4,4,2,2,1) — nullity `= a_∞` and rank `= a_∞`
at both primes, raw spaces 36 … 12 479 exactly as in Sol S4 §4.2 and
`results/wk11_int_stable_5332.json`.

**The covariance check has teeth (MEASURED):** on every block a random
weight-space vector FAILS the invariance at every raising with a nonzero
target; and a vector killed by three of the four raisings (three-raising
nullities 24–60 on three calibration blocks, 27–46 on the five) is invariant
under exactly those three and NOT under the fourth — run on the five blocks and
on the (11,1,1), (9,2,1,1), (5,5,3) calibration blocks (`negative_control_partial`
in those eight records; the dropped raising is the last one with a nonzero
target, since for a four-part `ρ` the raising `E_45` is vacuous — a small
deviation from the PREREG's wording).  F2-P1 did not fire.

### 1.3 The five blocks (MEASURED; `results/s79_stable/`, `results/s79_stable_blocks.md`)

| `ρ` | `a_∞` | raw space | nullity (P1 / P2) | `mult_det^∞` (P1 / P2) | `i_det^∞` | covariance | secs |
|---|---|---|---|---|---|---|---|
| (6,3,3,1) | 4 | 1 668 | 4 / 4 | 4 / 4 | **0** | PASS | 13 |
| (4,4,3,2) | 4 | 3 716 | 4 / 4 | 4 / 4 | **0** | PASS | 80 |
| (6,2,2,2,1) | 4 | 4 636 | 4 / 4 | 4 / 4 | **0** | PASS | 135 |
| (5,3,2,2,1) | 4 | 6 922 | 4 / 4 | 4 / 4 | **0** | PASS | 358 |
| (5,2,2,2,2) | 4 | 9 166 | 4 / 4 | 4 / 4 | **0** | PASS | 747 |

Twelve points, seed 20260908, entries in `[−10⁶, 10⁶]`; each record carries the
kernel basis, the points, `G` and every check (0.2–0.45 MB).  The independent
checker `analysis/wk12_s79_stable_check.py` — its own enumeration, its own Weyl
alternation over `S_5`, its own raising rule, a **Leibniz-expansion point map**
(`det(tI − A(s))` over the 24 permutations, not the power sums) and a
hand-written mod-`p` elimination — finds: weight spaces match as sets, `a_∞`
matches, every kernel vector killed by all four raisings, `G` matches **entry
by entry**, ranks match, covariance passes on the recomputed values; and (added
after the adversarial audit, `--nullity`) the load-bearing count itself is
re-derived — the checker's own sparse `E`, its own random projection (a
different seed) and a `flint` rank give `nullity_p(E) ≤ nc − rank = 4 = a_∞` at
both primes on all five blocks: **ALL CHECKS PASS** on the five and on the
calibration records (`results/logs/s79_stable_check_final.log`).

**What the negative proves (PROVED, Prop. S):** `i_det((4δ−13, ρ), δ) ≤
i_det^∞(ρ) = 0` for every `δ` on each of the five ladders; with the eleven
earlier blocks the dead region `|ρ| = 13, a_∞ ≤ 4` is complete.  **P1 hit**, P2
not observed, F1/F2 never fired.

**Format-verifiable counterparts.**  The stable picture has no `gct-cert/1`
kind; its record is the artefact plus the checker.  But Proposition S makes the
first stable cell of each ladder the same statement in the quartic picture, and
Part 2's driver wrote verifier-PASS `full_rank` certificates there for the new
block — `(19,5,3,2,2,1)_8`, `(23,5,3,2,2,1)_9`, `(27,5,3,2,2,1)_10`,
`a = a_∞ = 4` (`results/certs/s79_calib6/`); for the other four the record's
own cells already carried it (§0).  The two instruments agree on every block
where both have run.

### 1.4 The census defect

`analysis/wk12_int_w13_census.py` counted "open" against the stable
instrument's history (Sol S4 + the integrator's `(5,3,3,2)`).  The quartic
record closes a tail whenever a cell with `a = a_∞` has `mult_det = a`
(Prop. S — the argument s57 used for its 34 permanently dead ladders).
Cross-referencing the record's `mult_det = a` cells against
`a(λ,δ) = a_∞(tail)` closes `(6,3,3,1)`, `(4,4,3,2)`, `(6,2,2,2,1)`,
`(5,2,2,2,2)` before any stable computation.  The stable run was still worth
doing — it is the first independent-instrument reproduction of the quartic
record at `a_∞ = 4`, and the stable instrument is cheaper per tail than any
quartic cell — but a frontier count should mean open on both.  The same
cross-reference at `a_∞ = 5` (four weight-13 blocks) is a five-minute task for
batch 13 before that slot is scoped; this session did not run it (the brief:
no `a_∞ = 5` census).

---

## 2. Part 2 — the `ℓ = 6` padded frontier

### 2.1 The instrument (`analysis/wk12_s79_cell6.py`)

Session 71's driver was fixed at `R = 5`; this is the same driver with
`R = len(λ)` on the unchanged engine (`wk9_s45_build.build_cell`,
`wk11_s71_hybrid.hybrid_kernel`, session 60's evaluation rows), the
length-general `(★)` mask, and session 64's padded family (`wk10_s64_pad`: the
TRUE padded permanent `x_0·per_3` in `Sym^4 C^{10}` restricted to a generic
6-plane).  Four families at every cell, `K = a + 8` points each, both primes:

    mult_det   det_4 pencils of length 6, seed 11        mult_pad   padded frames, seed 37
    mult_per4  unpadded per_4 pencils, seed 47           mult_red   (★) point-free, and l·c points, seed 29

`D = mult_pad − mult_det` (the programme's sign), `D_R = mult_red − mult_det`
(the reducible screen), `pad<red` the padded-frontier flag.  Cost model for
every number below: **the s71 hybrid model** — build `2.1·10⁻⁶ s · N_S·δ`,
evaluation rows `2.7·10⁻⁸ s` per point per `N_S·δ`, hybrid never the cost — and
it holds at length 6: over all 682 cells the build ran at a median 0.99× the
model (p90 1.82×) and the rows at `2.3·10⁻⁸ s` per point per `N_S·δ`; the
hybrid phase was at most 202 s at one prime (`(13,9,9,3,1,1)_9`,
`n_χ = 732 815`, `|U| = 1 277`).  The compact circuit was not used anywhere: no shape class here is
two-tall-column, and the brief forbids s69's cost model without an exhibited
contraction representation and pathwidth bound.

**A latent defect of s71's driver, fixed.**  `wk11_s71_cell.py` extracted the
ideal vectors on a rank drop as `nullspace(G^T)` — combinations of *points*,
not of kernel vectors — and multiplied a `(a−mult) × K_pts` matrix by the
`a × n_χ` kernel; it never executed in session 71 because no drop occurred
there.  It crashed here on the first padded drop (`(8,4,4,4,4)_6`) and is
corrected (`nullspace(G)`, the vectors verified `E·v = 0`).  No s71 number is
affected.

**Two memory fixes** after three cells were killed by the box while the cubic
scan ran alongside: the `X` blocks of the hybrid are sized by `S71_MEM_X`
(`2.5·10⁸` bytes here; the `int64` temporaries of a `|S| × |U|` block were the
peak), and the evaluation rows are formed eight points at a time.  Every killed
cell was re-run alone and banked; the `a = 70` cell `(13,9,9,3,1,1)_9` peaked
at 4.35 GB alone.

**The per4 column is proper at length 6 (MEASURED,
`results/s79_per4_dimension_R6.json`):** s71's Jacobian at `R = 6` has rank
`90 = 16R − 6` for `per_4` and `66 = 16R − 30` for `det_4`, both primes, two
integer points, against `dim Sym^4 C^6 = 126` (at `R = 5` it is 70 =
everything, s71).  `i_per4` is a genuine column here — its first non-vacuous
use; and `16R = 96 < 126` makes properness a dimension count, not a rank.

### 2.2 Calibration (MEASURED, `results/s79_calibration6.jsonl`, both primes)

| cell | `a` | det | red (★ = pts) | pad | per4 | banked |
|---|---|---|---|---|---|---|
| (12,9,8,1,1,1)_8 | 6 | 6 | **4** | 4 | 6 | s47: red 4 (two integer certs); pad = red by theorem |
| (14,8,7,1,1,1)_8 | 9 | 9 | **8** | 8 | 9 | s47: red 8 |
| (17,12,4,1,1,1)_9 | 8 | 8 | **7** | 7 | 8 | s47: red 7; s43: det 8 |
| (16,13,4,1,1,1)_9 | 7 | 7 | **6** | 6 | 7 | s47: red 6; s43: det 7 |
| (19,9,5,1,1,1)_9 | 12 | 12 | 12 | 12 | 12 | s43: det 12 |
| (22,6,2,2,2,2)_9 | 8 | 8 | 8 | 8 | 8 | s43: det 8 |
| (19,6,2,2,2,1)_8 | 4 | 4 | 4 | 4 | 4 | s43: det 4 |
| (19,5,3,2,2,1)_8, (23,…)_9, (27,…)_10 | 4 | 4 | 4 | 4 | 4 | cross-instrument: Part 1 block 4 |

Every banked value reproduces; 1.6–7 s per cell against the record's hours.
`full_rank` certificates for det / pad / per4 (the per4 ones regenerated after
the audit noticed the calibration run predated that branch) verify with
`tools/verify`.

### 2.3 Q1 — session 57's six-row nominees (MEASURED; `results/s79_cells.jsonl`, `results/s79_cells.md`)

Frozen at pre-registration (`results/s79_queue.json`): the six-row cells of
session 57's T1 (room-one cells) and T2 (first stable cells of the open tails
of weight 13–16) not in the record, 123 cells by `N_S·δ` from `4.5·10⁵` to
`2.2·10⁸`.  **121 reached** (`δ = 7`: 2, 8: 23, 9: 27, 10: 62, 11: 6, 12: 1;
`a` from 1 to 70, `Σa = 1 796`; `n_χ` to 732 815; tail weights 13–23), 5 336 s
in all, median 8.5 s per cell.  At every one of the 121:

    i_det = 0      (mult_det = a at both primes: PROVED, no six-row determinant equation)
    mult_pad = mult_red   ((★) and the l·c points agree at every cell; an equality of ranks at both primes,
                           a theorem at δ ≤ 9 by §2.4, a measurement at δ ≥ 10)
    i_per4 = 0     (mult_per4 = a: PROVED, Per_6 has no equation at these weights)

**Nineteen reducible drops** (`D_R < 0`, `mult_red < a`), every one with at
least two trailing 1s — fifteen of shape `(x,y,z,1,1,1)`, four of shape
`(x,y,z,w,1,1)` — extending s60/s71's "bite family" `(x,y,1,1)/(x,y,z,1)` to
six rows; the largest is `D_R = −25` at `(13,9,9,3,1,1)_9` (`a = 70`,
`red = pad = 45`), then `−7` at `(15,10,8,1,1,1)_9`, `−5` at `(15,9,9,1,1,1)_9`.
At each of the nineteen the padded rank equals the reducible rank: consistent
with, and at `δ = 9` implied by, §2.4.  The initial-term sieve certified
`i_red = 0` outright at none of the 121 cells (B5 of s71 again: balanced
weights' `(★)` columns are not cover-complete).

**69 of the 121 are first stable cells** (`a = a_∞`), so by Proposition S they
close **63 distinct tails** (weight 13: 2, 14: 10, 15: 19, 16: 27, 17: 3, 18: 2)
for every degree, on every side: `i_det^∞ = 0`, `i_per4^∞ = 0`, and
`mult_pad^∞ = mult_red^∞ = a_∞` at those tails (every one of the 69 has all
four ranks equal to `a`, so these are full-rank statements over `Q`).  With s57's closure of every tail of weight
`≤ 12` and Part 1, the six-row determinant frontier at tail weights 13–16 is
now closed on every tail that reaches its stable value by `δ ≤ 12`.

**Not reached:** `(10,6,6,6,2,2)_8` (`N_S·δ = 1.47·10⁸`, `n_χ = 1.53·10⁶`): the
raising rows exceed 4 GB in the build (killed at `E_45`) — the build wall of
this box, at the `N_S·δ` s71 named; `(12,4,4,4,4,4)_8` (`2.16·10⁸`): above the
pre-registered cap, not attempted (one cell hit the wall, one was never tried).

### 2.4 Q3 — the cubic side, `I(D_6^{per_3})_δ` (MEASURED → PROVED per degree; `results/s79_per6.jsonl`, `results/s79_per6_d9.md`, `_d10.md`)

`analysis/wk12_s79_per6.py`: the same build with `n = 3`, the hybrid kernel,
session 41's family `per_3(Σ_{i≤6} s_i A_i)` (seed 41, bound 40, `a + 8`
points), both primes; a drop is re-checked in the same call at `3a + 24` fresh
points (seed 907).  Control: s47's `(7,5,4,4,2,2)_8`, `mult = a = 1` in 10.5 s
against 2 420 s, with a verifier-PASS `full_rank` certificate at `n = 3` /
`permanent_pencil`.

**`δ = 9`: all 210 length-6 weights `μ ⊢ 27` with `a(μ,9) ≥ 1` in
`Sym^9(Sym^3 C^6)` have `mult = a` at both primes** (`Σa = 592`, `a ≤ 9`,
`N_S` from 4 743 to 3 299 214, `n_χ` to 1 660 777; 5 884 s in all, at most
496 s per weight).  Hence

> **`I(D_6^{per_3})_9 = 0`** (PROVED: a full rank at one prime proves
> `mult = a`, and both primes agree at every weight), and by Prop. 8(1) of
> `docs/transfer_lemma.md` **`mult_pad = mult_red` at every six-row weight of
> degree 9** — a theorem with no points in it, one degree beyond s47.

284 `full_rank` certificates (`n = 3`, `permanent_pencil`) were written for
the 142 weights whose expanded basis fits the size rule; the shipping cut of
§4 applies.  Two weights (`(6,6,6,5,2,2)`, `(7,7,4,4,3,2)`) were killed by the
box on the first pass (a concurrent `a = 70` quartic cell) and re-run alone.

**`δ = 10`: 296 of the 402 length-6 weights `μ ⊢ 30` with `a(μ,10) ≥ 1`
(`Σa = 2 225`, `a ≤ 24`) — the `N_S`-cheapest, `N_S ≤ 1 698 457`, `Σa = 1 846`
— have `mult = a` at both primes** (7 259 s in all, at most 293 s per weight).
The remaining 106 weights (`Σa = 379`) are priced at `N_S` from 1 706 497 to
27 294 676 (`(5,5,5,5,5,5)`): 69 below `5·10⁶`, 26 between `5·10⁶` and `10⁷`,
and eleven above `10⁷`, the last at or beyond this box's build wall.  So
`I(D_6^{per_3})_{10}` is **open**, with every weight below `N_S = 1.7·10⁶`
empty.  (The container was stopped at about 05:45 UTC, before the 06:20
deadline, with the scan at this point; nothing was lost, the records are
complete, and the two weights the restarts had recorded twice with identical
results were deduplicated.)

**Controls (added after the adversarial audit, `results/s79_per6_control.json`):**
`per_form(3)` equals a hand permanent at a numeric matrix, the recorded
`per_3` coefficient dicts differ from the `det_3` restriction of the same
pencils at all ten points, and two `a = 2` weights of degree 8 from session
43's record — `(11,4,4,2,2,1)_8`, `(10,6,4,2,1,1)_8` — reproduce `mult = a = 2`
(a nonvanishing test at `a = 1` cannot tell one family from another; a rank-2
test can fail).

### 2.5 Q2 — the broader six-row census (MEASURED; same file)

Every other six-row cell with `a ≥ 1` at `δ ≤ 12` from the s57 tables — 10 513
cells not in the record or Q1 — by `N_S·δ` (`results/s79_queue2.json`), with
`N_S·δ ≤ 10⁷` and the `full_rank` expansion off (the hybrid records stay).
**561 cells reached** (`δ = 6`: 42, 7: 79, 8: 68, 9: 75, 10: 69, 11: 116,
12: 112; `a` to 80, `Σa = 7 088`; `N_S·δ` to `3.87·10⁶`; 7 146 s): **`i_det = 0`,
`mult_pad = mult_red`, `i_per4 = 0` at every one**; 40 reducible drops
(`D_R` to `−7`; 31 of them at `δ ≥ 10`, where the equality `pad = red` is a
measurement).  With Q1 that is **682 six-row cells** this session, 59 with a
reducible drop, none with a determinant, padded or `per_4` one.  These are the
cheap — i.e. skewed — cells: the balanced cells (T4 of s57, `n_χ ≥ 10⁶`) remain
the place a six-row determinant equation of degree `≤ 12` could hide, exactly as
s57 said, and remain priced at `N_S·δ ≥ 10⁸`.  The next unreached Q2 cell is
`(11,7,4,2,2,2)_7` at `N_S·δ = 3.87·10⁶`; 444 more cells lie below `10⁷`.

### 2.6 The negative, characterised and priced

At length 6 through `δ = 12` on the 682 cells reached, the three ideals
`I(D_6)`, `I(P_6)/I(R_6)`, `I(Per_6)` are empty in every weight measured; the
permanent is invisible on the reducible side in every weight of every degree
`≤ 9` (theorem) and in the 296 cheapest weights of degree 10.  The region not
reached is stated by cost: the 9 952 Q2 cells above `N_S·δ = 3.87·10⁶` (444 of
them below `10⁷`, the rest to `1.9·10⁹`), the two Q1 cells above `1.4·10⁸`, and
the 106 degree-10 cubic weights above `N_S = 1.7·10⁶`.  Under the hybrid model
a further night buys the 444 Q2 cells below `10⁷` and the 95 degree-10 weights
below `10⁷` (minutes each); the degree-10 theorem needs the eleven weights
above `10⁷`, which need a box with more than 7 GB or a leaner row builder (the
raising rows, not the kernel, are the wall).

### 2.7 What was not done

- No `ℓ = 6` cell with `i_det ≥ 1` or `mult_pad < mult_red` was found — the
  brief's success criterion for Part 2 is not met; the negative above is the
  deliverable the brief names for that case.
- The compact circuit was not priced for any `ℓ = 6` class (no pathwidth bound
  was exhibited; not attempted).
- `I(D_6^{per_3})_{10}` is open (106 weights, 11 of them beyond this box).
- The two build-walled Q1 cells and the `(12,4,4,4,4,4)_8` cell.

---

## 3. Pre-registration scorecard

| | pre-registered | outcome |
|---|---|---|
| P1 | all five `a_∞ = 4` blocks determinant-full (0.85) | **hit** |
| P2 | a candidate stable equation (0.15) | not observed |
| F1-P1 / F2-P1 | instrument falsifiers | never fired; calibration 11/11, controls behave |
| stopping rule (Part 1) | raw space 10× the `a_∞ = 1` max, or 2 h / 6 GB | did not fire (max 9 166, 747 s, < 2 GB) |
| calibration §2.3 | six record cells reproduce | **all reproduce**, plus four more |
| cross-instrument | quartic `i_det` at `(27,5,3,2,2,1)_10` = Part 1's `i_det^∞((5,3,2,2,1))` | **agree** (0 = 0), also at `δ = 8, 9` |
| P3 | `i_det = 0` at every Q1 cell (0.75) | **hit** (121/121) |
| P4 | `mult_pad = mult_red` at every cell reached with `δ ≥ 9` (0.6) | **hit**, and at `δ = 9` now a theorem |
| P5 | `i_per4 = 0` everywhere (0.7) | **hit** |
| P6 (A.3) | `I(D_6^{per_3})_9 = 0` (0.6) | **hit**; `δ = 10` not decided (296 of 402 empty) |
| success | a cell with `i_det ≥ 1` or `mult_pad < mult_red` | **not observed** |
| `D > 0` | halt, protocol | never |
| F1-P2 / F2-P2 | calibration or theorem-contradicting drop | never fired |
| information-rate rule | 60 consecutive negatives at > 10 min/cell | never reached 10 min/cell; the container stop (05:45 UTC) ended the sweeps |
| deviation | PREREG §1.3(2) wording vs the projected nullspace | recorded (A.5) |
| deviation | branch history rewritten once (§4) | recorded |

## 4. Honest boundary, certificates, and the rewrite

- **PROVED** here: the sixteen-block stable theorem (full ranks at both
  primes, one suffices); `mult_det = a` and `mult_per4 = a` at all 682 cells;
  `mult_red = a` and `mult_pad = a` wherever they are full (623 cells);
  `I(D_6^{per_3})_9 = 0`, hence `mult_pad = mult_red` in every weight of degree
  `≤ 9`.
- **MEASURED (exact mod both primes, characteristic zero only as a bound):**
  every `mult_red < a` and `mult_pad < a` value (59 cells) — a mod-`p` kernel
  bounds the ideal codimension from below only (`i ≥ 1` needs an integer
  vector, which was not lifted here); and the equalities `mult_pad = mult_red`
  at the 35 drop cells with `δ ≥ 10` [CORRECTED: 31 counted Q2 alone; Q1 contributes four more — 15 at degree 10, 12 at 11, 8 at 12. B13-07], where no theorem covers them.
- **Certificates.**  `full_rank` (verifier PASS) for det / pad / per4 at the
  calibration cells and for the cubic side; `hybrid_kernel` recorded
  certificates (points, cover, attempts, and the kernel in χ-coordinates where
  it is small) at every Q1/Q2 cell.  The full set (2066 files, 838 MB)
  cannot travel in a bundle: the tree ships every file at or below 60 KB (the
  hybrid records of most cells) plus the verifier-PASS `full_rank` certificates
  of the cross-instrument and s47 calibration cells at the first prime (1 200
  files, 27.2 MB);
  `results/s79_cert_manifest.json` lists ALL files with size and md5, the rest
  sit outside the tree on the session box, and every file is regenerable from
  the recorded seeds by the recorded command (`analysis/wk12_s79_certs_manifest.py`).
- **The branch history was rewritten once** (03:45 UTC): the two directories
  `results/certs/s79_cells` and `results/certs/s79_per6` were dropped from
  every commit with `git filter-branch --index-filter` — nothing else changed,
  author and committer timestamps are preserved, so the pre-registration
  commit (`51dcd0f` → `94af0bf`) still carries its 22:47 UTC timestamp before
  the first measurement.  Checkpoint bundle 1 (`03aa29df…`, hashes
  `51dcd0f … 616264c`) is superseded by the final bundle.
- Commit trailers: the preamble asks for `Co-Authored-By: Claude Opus 5`; this
  session's commits carry the model that ran it (`Claude Fable 5.1`), no
  session-link trailer, per the standing rule.

## 5. For the integrator

1. **Cross-reference before counting a frontier.**  §1.4: a tail is closed on
   the quartic side by any record cell with `a = a_∞`, `mult_det = a`.  Four of
   the five "open" `a_∞ = 4` blocks were closed that way.  A five-line addition
   to `wk12_int_w13_census.py` (join against `negative_record()` and the
   per-cell `a`) would have shown it; the same check should precede the
   `a_∞ = 5` slot.
2. **The stable instrument is validated at `a_∞ = 4`** on four record-closed
   tails and agrees with the quartic driver on the fifth; its cost is minutes
   per tail against seconds-to-minutes per quartic cell, but it sees only the
   determinant side.  For padded questions the cubic side (n = 3) is the
   cheap theorem route: one degree per scan, every six-row weight at once.
3. **Length-6 hybrid: the cost model transfers unchanged**, and the wall is the
   build (raising rows) at `N_S·δ ≈ 1.5·10⁸` in 7 GB, and the hybrid's `X`
   blocks before `S71_MEM_X` — set it to `2.5·10⁸` by default.  The
   `nullspace(G^T)` defect in `wk11_s71_cell.py` should be patched in the
   length-5 driver too (it is only reached on a drop).
4. **The degree-10 cubic theorem** needs the eleven weights with
   `N_S > 10⁷` (§2.4); everything below is either done or priced at minutes.
   That is one session on a larger box, or a leaner row builder.
5. **The reducible-first pattern at length 6** (§2.3, §2.5): 58 of the 59
   drops have at least two trailing 1s (36 of the Q2 ones have three); the one
   exception is `(7,4,4,4,4,1)_6` (`a = 1`, `mult_red = 0`), the `(4,4,4,4)`
   family s71 already knew as the only reducible-first tail of another shape.
   `(13,9,9,3,1,1)_9` at `D_R = −25` is the largest reducible bite at any
   length in the record.  All 59 are `pad = red` (a theorem at `δ ≤ 9`, a
   measurement at `δ ≥ 10`); none says anything about the permanent.
6. Defects in the brief, per the preamble's request: the "five open blocks"
   count (§1.4); and the batch-12 files were all present (unlike batch 11),
   so no tier-3 reconstruction was needed.
