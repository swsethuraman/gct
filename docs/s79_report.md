# Session 79 — the two independent frontiers (batch 12)

2026-09-08/09, branch `s79-frontiers` off `main = afb8c33`, pre-registration
`results/PREREG_s79.md` (commit `51dcd0f`, before any measurement; addendum A
after the calibration and before the queues).  Delivery by bundle
`s79_frontiers.bundle`; no push.  Both house primes everywhere.

Labels: **PROVED** (theorem in the tree or a full-rank certificate, cited),
**MEASURED** (computed here), **RECORDED** (a mod-`p` kernel or a cost, not a
characteristic-zero statement), **ADOPTED** (the record), **EXPECTATION**.

---

## 0. Verdict

> **Part 1.**  The five `a_∞ = 4` weight-13 stable blocks — `(6,3,3,1)`,
> `(4,4,3,2)`, `(6,2,2,2,1)`, `(5,3,2,2,1)`, `(5,2,2,2,2)` — are all
> **determinant-full**: kernel dimension `4 = a_∞` at both primes, evaluation
> rank `4` at both primes, covariance check PASS on every kernel vector, both
> negative controls failing as they must, every record re-derived by an
> independent checker.  **PROVED** (a full rank at one prime proves it over `Q`):
>
>     |ρ| = 13  and  a_∞(ρ) ≤ 4   ⟹   i_det^∞(ρ) = 0        (16 blocks)
>
> — no weight-13 stable determinant equation with `a_∞ ≤ 4`; the first possible
> one needs `a_∞ ≥ 5`, and by Proposition S every cell `(4δ − 13, ρ)` of those
> sixteen ladders has `i_det = 0` at **every** degree `δ`.  Cost: 13 to 747 s
> per block; the brief's order-of-magnitude trigger did not fire.
>
> **A correction to the census while sizing it:** four of the five blocks were
> already closed by the quartic record via Proposition S before this session
> (`(19,6,3,3,1)_8`, `(19,4,4,3,2)_8` in s60; `(19,6,2,2,2,1)_8`,
> `(23,5,2,2,2,2)_9` in s43 — all `a = a_∞ = 4`, `mult_det = 4`).  Only
> `(5,3,2,2,1)` was open on both instruments, and the two instruments agree on
> it.  The census counted "open" against the stable instrument's own history
> rather than the quartic record; the cross-reference should be part of any
> future stable-frontier count (§5).
>
> **Part 2.**  Session 71's hybrid, made length-general and given session 64's
> padded family, runs `ℓ = 6` cells in **seconds** that batches 9–10 priced in
> hours — the reducible drops of s47 at `δ = 8, 9` reproduce exactly, and
> `mult_pad = mult_red` at every `δ ≤ 8` cell as the theorem requires.  On the
> frozen Q1 queue (session 57's 123 six-row nominees not in the record, by
> `N_S·δ`): **`i_det = 0`, `mult_pad = mult_red`, `i_per4 = 0` at every cell
> reached** (QQ1 of 123; §2.3) — no six-row determinant equation, no
> permanent-specific equation, at tail weights 13–16 through `δ = 12`.
> The per4 column is proper at length 6 for the first time (dim 90 < 126) and
> also empty.
>
> **The theorem route (addendum A.3):** on the cubic side,
> **`I(D_6^{per_3})_9 = 0`** — all 210 length-6 weights `μ ⊢ 27` with
> `a(μ,9) ≥ 1` have `mult = a` at both primes (QQ2) — so by Prop. 8(1) of the
> transfer lemma **`mult_pad = mult_red` at every six-row weight of degree 9 is
> a theorem**, extending s37/s43/s47's `δ ≤ 8` by one degree with no points in
> it; and at `δ = 10`, QQ3 of 402 weights (§2.4).
>
> So the `ℓ = 6` padded frontier is characterised as a **negative over a stated,
> priced region** (§2.5): the permanent is invisible on the reducible side
> through degree 9 at length 6, and no cell of the nominee queue carries a
> determinant equation.  The first cell where a `mult_pad < mult_red` could now
> appear has `δ ≥ 10` (§2.4 says how far `δ = 10` was pushed).

---

## 1. Part 1 — the stable `a_∞ = 4` frontier at weight 13

### 1.1 What was pre-registered

`results/PREREG_s79.md` §1: the five blocks in raw-space cost order; the
batch-10 stable pullback extended to `a_∞ > 1` and both primes; the nullity
check `dim ker = a_∞`; `K_pts = a_∞ + 8` integer points of `M_6`; the
covariance check per kernel vector with two negative controls; calibration on
the eleven closed blocks; falsifiers F1-P1/F2-P1; P1 (0.85) all five die.

### 1.2 The instrument (`analysis/wk12_s79_stable.py`)

Conventions are the batch-10 instrument's, verbatim: the 120 generators
`y_{(d,α)}`; the raising rule `E_{i,i+1} y_{(d,α)} = (α_i+1) y_{(d,α+e_i−e_{i+1})}`
extended as a derivation; the point map = the coefficients `(e_2, e_3, e_4)` of
`det(tI − A(s'))` for a traceless integer 5-pencil (computed through power sums
as in the record).  What is new: the kernel of the stacked raising operator is
the exact `python-flint` nullspace of a random dense projection `R·E`
(`nc + 24` rows), **every vector re-verified on the sparse `E`**, and its
dimension compared with the characteristic-zero `a_∞`
(`wk9_s57_stable.a_inf`) — `ker(R·E) ⊇ ker_p(E) ⊇ (L mod p)` with
`dim(L mod p) = a_∞`, so equality of the count pins `ker_p(E)` exactly and
identifies it with the reduction of the integral HWV lattice (addendum A.5
records that the pre-registration's wording said "sequential intersections";
the soundness argument is the same and the randomness can only make a run
inconclusive).  Then `G = ev·K` (`12 × a_∞`) at the same twelve integer
pencils reduced mod each prime, `mult_det^∞ = rank_p G`; `rank_p G = a_∞` at
one prime proves `i_det^∞ = 0` over `Q` (`rank_p ≤ rank_Q`, Lemma 2 of
`docs/sparse_det_route.md`).

**Calibration (MEASURED, all reproduce):** the eleven closed blocks —
`a_∞ = 1`: (7,2,2,1,1), (5,5,1,1,1), (5,3,3,2), (5,3,3,1,1); `a_∞ = 2`:
(11,1,1), (9,2,1,1), (6,3,2,1,1), (5,4,2,1,1), (4,3,2,2,2); `a_∞ = 3`: (5,5,3),
(4,4,2,2,1) — nullity `= a_∞` and rank `= a_∞` at both primes, raw spaces
36 … 12 479 exactly as in Sol S4 §4.2 and `results/wk11_int_stable_5332.json`
(`results/s79_stable/calibration/`).

**The covariance check has teeth (MEASURED):** on every block a random
weight-space vector FAILS the invariance at every raising with a nonzero
target; and a vector killed by three of the four raisings (the projected
nullspace of the three-raising operator; three-raising nullities 24–60 on the
calibration blocks, 27–46 on the five) is invariant under exactly those three
and NOT under the fourth (`negative_control_partial` in every record).

### 1.3 The five blocks (MEASURED; `results/s79_stable/`, `results/s79_stable_blocks.md`)

| `ρ` | `a_∞` | raw space | nullity (P1 / P2) | `mult_det^∞` (P1 / P2) | `i_det^∞` | covariance | secs |
|---|---|---|---|---|---|---|---|
| (6,3,3,1) | 4 | 1 668 | 4 / 4 | 4 / 4 | **0** | PASS | 13 |
| (4,4,3,2) | 4 | 3 716 | 4 / 4 | 4 / 4 | **0** | PASS | 80 |
| (6,2,2,2,1) | 4 | 4 636 | 4 / 4 | 4 / 4 | **0** | PASS | 135 |
| (5,3,2,2,1) | 4 | 6 922 | 4 / 4 | 4 / 4 | **0** | PASS | 358 |
| (5,2,2,2,2) | 4 | 9 166 | 4 / 4 | 4 / 4 | **0** | PASS | 747 |

Every block: twelve points, seed 20260908, entries in `[−10^6, 10^6]`, the
`12 × 4` matrix `G` recorded with the kernel basis, the points and every
check.  Independent checker `analysis/wk12_s79_stable_check.py` (its own
enumeration, its own Weyl alternation over `S_5`, its own raising rule, a
**Leibniz-expansion point map** — `det(tI − A(s))` over the 24 permutations,
not the power sums — and a hand-written mod-`p` elimination): weight spaces
match as sets, `a_∞` matches, every kernel vector killed by all four raisings,
`G` matches **entry by entry**, ranks match, covariance passes on the
recomputed values — **ALL CHECKS PASS** on all five and on the calibration
records.

**What the negative proves (PROVED, Prop. S):** `i_det((4δ−13, ρ), δ) ≤
i_det^∞(ρ) = 0` for every `δ` on each of the five ladders, and with the eleven
earlier blocks the dead region `|ρ| = 13, a_∞ ≤ 4` is complete.  The
predictions of the pre-registration: **P1 hit**, P2 not observed, F1/F2 never
fired.  The brief's stopping rule ("raw spaces an order of magnitude larger
than the `a_∞ = 1` ones") did not fire: largest 9 166 against 5 240 (`a_∞ = 1`)
and 12 479 (batch 11's largest).

**Format-verifiable counterparts.**  The stable picture has no `gct-cert/1`
kind; the record is the JSON artefact plus the checker.  But Proposition S makes
the first stable cell of each ladder the same statement in the quartic
picture, and Part 2's driver wrote `full_rank` certificates there — for the
new block, `(19,5,3,2,2,1)_8`, `(23,5,3,2,2,1)_9` and `(27,5,3,2,2,1)_10`
(`a = a_∞ = 4`, verifier PASS, `results/certs/s79_calib6/`); for the other
four, the record's own cells already carried the statement (§0).  The two
instruments agree on every block where both have run.

### 1.4 The census defect

The brief's five "open" blocks came from `analysis/wk12_int_w13_census.py`,
which counts against the stable instrument's history (Sol S4 + the
integrator's `(5,3,3,2)`).  The quartic record closes a tail whenever a cell
with `a = a_∞` has `mult_det = a` (Prop. S; the argument s57 used for its 34
permanently dead ladders).  Cross-referencing the record's `mult_det = a`
cells with `a(λ,δ) = a_∞(tail)` closes `(6,3,3,1)`, `(4,4,3,2)`,
`(6,2,2,2,1)`, `(5,2,2,2,2)` before any stable computation.  The stable
computation is not wasted — it is the first independent-instrument
reproduction of the quartic record at `a_∞ = 4`, and the stable instrument is
cheaper per tail than any quartic cell — but "open" should mean open on both.
The same cross-reference at `a_∞ = 5` would tell batch 13 how many of the four
`a_∞ = 5` weight-13 blocks are actually open.

---

## 2. Part 2 — the `ℓ = 6` padded frontier

### 2.1 The instrument (`analysis/wk12_s79_cell6.py`)

Session 71's driver was fixed at `R = 5`; this is the same driver with
`R = len(λ)`, on the unchanged engine (`wk9_s45_build.build_cell`,
`wk11_s71_hybrid.hybrid_kernel`, session 60's evaluation rows), the length-general
`(★)` mask, and session 64's padded family (`wk10_s64_pad`: the TRUE padded
permanent `x_0·per_3` in `Sym^4 C^{10}` restricted to a generic 6-plane).
Four families at every cell, `K = a + 8` points each, both primes:

    mult_det   det_4 pencils of length 6, seed 11        mult_pad   padded frames, seed 37
    mult_per4  unpadded per_4 pencils, seed 47           mult_red   (★) point-free, and l·c points, seed 29

`D = mult_pad − mult_det` (the programme's sign), `D_R = mult_red − mult_det`
(the reducible screen), `pad<red` the padded-frontier flag.  Cost model for
every number below: **the s71 hybrid model** (build `2.1·10⁻⁶ s · N_S·δ`,
evaluation rows `2.7·10⁻⁸ s` per point per `N_S·δ`, hybrid never the cost).
The compact circuit was not used anywhere: no shape class here is
two-tall-column and the brief forbids s69's cost model without an exhibited
contraction representation and pathwidth bound.

**A latent defect of s71's driver, fixed.**  `wk11_s71_cell.py` extracted the
ideal vectors on a rank drop as `nullspace(G^T)` — combinations of *points*,
not of kernel vectors — and then multiplied a `(a−mult) × K_pts` matrix by the
`a × n_χ` kernel; it never ran in session 71 because no drop occurred there.
Here it crashed on the first padded drop (`(8,4,4,4,4)_6`) and is corrected
(`nullspace(G)`, the vectors verified `E·v = 0`).  No s71 number is affected.

**The per4 column is proper at length 6 (MEASURED,
`results/s79_per4_dimension_R6.json`):** s71's Jacobian at `R = 6` gives rank
`90 = 16R − 6` for `per_4` (the 4-torus fibre) and `66 = 16R − 30` for `det_4`
at both primes at two integer points, against `dim Sym^4 C^6 = 126`; at `R = 5`
the same code gives 70 = everything (s71).  So `i_per4` is a genuine column
here — its first non-vacuous use.

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

Every banked value reproduces; `mult_pad = mult_red` at all four `δ = 8/9`
cells (at `δ = 8` the theorem, at `δ = 9` new and consistent with §2.4); 1.6 –
7 s per cell against the record's hours.  The `full_rank` certificates for
det / pad / per4 verify with `tools/verify` (`results/certs/s79_calib6/`).

### 2.3 Q1 — session 57's six-row nominees (MEASURED, `results/s79_cells.jsonl`, `results/s79_cells.md`)

QQ1

### 2.4 Q3 — the cubic side, `I(D_6^{per_3})_δ` (MEASURED → PROVED per degree)

QQ2

### 2.5 The negative, characterised and priced

QQ4

### 2.6 What was not done

QQ5

---

## 3. Pre-registration scorecard

QQ6

## 4. Honest boundary

QQ7

## 5. For the integrator

QQ8
