# Pre-registration — session 79, the two independent frontiers

Batch 12 (`docs/s79_prompt.md`, the reconciled proposal's s78 + s79).
Base: `main` = `afb8c33` at clone time (2026-09-08 22:32 UTC); branch
`s79-frontiers`; tree carries `docs/batch12_s1_s2_consolidated.md` and
`docs/batch12_worker_preamble.md`.  `tools/verify/selftest.py`: 12 cases, PASS
(51 s).  `analysis/wk12_int_w13_census.py`: 57 / 10 / 47 / 11 / 5 — the brief's
numbers, reproduced.  Committed before any measurement.

Labels used throughout: **PROVED** (a theorem in the tree, cited), **MEASURED**
(computed here, both house primes unless stated), **ADOPTED** (taken from the
record without re-derivation), **EXPECTATION** (a prior).  Anything not written
here is exploratory when it appears in the report.

---

## Part 1 — the stable `a_∞ = 4` frontier at weight 13

### 1.1 The question

For each weight-13 tail `ρ` with `a_∞(ρ) = 4`, is the ρ-isotypic highest-weight
part of `I(M_6)` zero?  `M_6` = closure of the characteristic-polynomial
coefficients `(e_2, e_3, e_4)` of traceless 5-pencils of `4×4` matrices, in
`Z = Sym^2 U ⊕ Sym^3 U ⊕ Sym^4 U`, `U = C^5` (Proposition S, `docs/s57_report.md`,
PROVED).  Write `i_det^∞(ρ) = dim I(M_6)^{hw}_ρ` and `mult_det^∞ = a_∞ − i_det^∞`.

**What a negative proves (PROVED, Prop. S):** `i_det((4δ−13, ρ), δ) ≤ i_det^∞(ρ)`
for every `δ`, with equality for `δ ≥ 13` and at every cell with `a = a_∞`.  So
`i_det^∞(ρ) = 0` closes the whole ladder `{(4δ−13, ρ)}` at every degree.  If all
five blocks die the banked theorem is

> `|ρ| = 13` and `a_∞(ρ) ≤ 4` ⟹ `i_det^∞(ρ) = 0`   (16 blocks: 4+5+2 from
> batches 10–11, 5 here)

and every weight-13 stable determinant equation needs `a_∞ ≥ 5`.

### 1.2 The five blocks, in raw-space cost order (sizing MEASURED here, 0.2 s each)

| # | `ρ` | `a_∞` (census) | raw weight space | raising targets (sum) |
|---|---|---|---|---|
| 1 | (6,3,3,1) | 4 | 1 668 | 3 166 |
| 2 | (4,4,3,2) | 4 | 3 716 | 8 389 |
| 3 | (6,2,2,2,1) | 4 | 4 636 | 11 406 |
| 4 | (5,3,2,2,1) | 4 | 6 922 | 17 541 |
| 5 | (5,2,2,2,2) | 4 | 9 166 | 25 402 |

Reference: the `a_∞ = 1` blocks were 2 182 – 5 240, the largest batch-11 block
`(4,3,2,2,2)` was 12 479.  **The order-of-magnitude stopping rule of the brief
does not fire** (largest here 9 166 < 12 479); Part 1 is expected to cost
minutes per block.  Blocks 1 and 2 have four parts (`ℓ = 5` shapes); Prop. S
covers them at `ℓ = 6` verbatim, and a weight with a zero last part sees only
the coordinates of `Sym^d C^4`, so `i_det^∞` there is the `ℓ = 5` value.

### 1.3 The instrument

`analysis/wk12_s79_stable.py`, the batch-10 stable pullback
(`wk10_int_stable_hwv.py` + `wk10_int_stable_subst.py`, integrator code,
unchanged in its conventions) extended to kernels of dimension `a_∞ > 1` and
to both house primes:

1. raw weight space = multisets of the 120 generators `y_{(d,α)}`
   (`d = 2,3,4`, `α` a degree-`d` exponent in 5 variables) with exponent sum `ρ`;
2. raising `E_{i,i+1} y_{(d,α)} = (α_i + 1) y_{(d, α + e_i − e_{i+1})}` (the
   coefficient convention of the record, `CONVENTIONS` of `wk9_s60_cell.py`);
   the kernel `K = ∩_i ker E_{i,i+1}` computed exactly mod `p` by sequential
   intersection (dense `python-flint` nullspaces, no randomness), every kernel
   vector re-verified on the sparse operators, `rank_p K = dim K` asserted;
3. **nullity check (must hold):** `dim K = a_∞(ρ)` at both primes, `a_∞` from
   `wk9_s57_stable.a_inf` (characteristic-zero Weyl alternation).  Since
   `nullity_p ≥ nullity_Q = a_∞`, equality says the mod-`p` kernel is the
   reduction of the integral HWV lattice.
4. evaluation at `K_pts = a_∞ + 8 = 12` integer points of `M_6`: the coefficients
   of `det(tI − A(s'))` for `A(s') = Σ_{k=1}^5 s_k A_k`, `A_k` random traceless
   integer `4×4` matrices (entries in `[−10^6, 10^6]`, seed stream recorded),
   reduced mod each prime; `G = ev·K` (`12 × 4`); `mult_det^∞ = rank_p G`.
5. **the covariance check (mandatory, per kernel vector, per prime):**
   `F(A') = F(A)` for `A'_{i+1} = A_{i+1} + ε A_i`, all four `i`, `ε ∈ {1, 7, 999}`
   (the batch-10 check that caught a normalisation error).  A **negative
   control** is run alongside: a vector in `ker E_{12} ∩ ker E_{23} ∩ ker E_{34}`
   but not in `ker E_{45}` (or, failing that, a random weight-space vector)
   must FAIL the check at the corresponding raising, so the check is shown to
   have teeth.
6. certificates: `results/certs/s79_stable_<ρ>_p<prime>.json` (`gct-cert/1`
   `full_rank` on `G` where the format allows) plus the kernel basis, the
   points and `G` as artefacts, and an independent checker
   `analysis/wk12_s79_stable_check.py` that recomputes `E·K = 0`, the
   evaluations and the rank from the artefact with none of the engine's code.

**Soundness of a full rank (PROVED, `docs/sparse_det_route.md` Lemma 2 /
preamble):** `rank_p ≤ rank_Q`; with (3) the kernel is the reduction of the
integral HWV lattice, so `rank_p G = 4` at one prime proves that no nonzero
HWV of weight `ρ` vanishes at all twelve points, hence `i_det^∞(ρ) = 0` over
`Q`.  A rank drop mod `p` proves nothing (a candidate).

### 1.4 Calibration before the five (MEASURED, must reproduce)

The eleven closed blocks, on the same code: `a_∞ = 1`: (7,2,2,1,1), (5,5,1,1,1),
(5,3,3,2), (5,3,3,1,1) — nonzero at every point; `a_∞ = 2`: (11,1,1), (9,2,1,1),
(6,3,2,1,1), (5,4,2,1,1), (4,3,2,2,2) — rank 2; `a_∞ = 3`: (5,5,3), (4,4,2,2,1)
— rank 3; raw sizes 36 … 12 479 as in `docs/sol/sol_batch11_report.md` §4.2 and
`results/wk11_int_stable_5332.json`.  Any disagreement stops Part 1 (F1-P1).

### 1.5 Predictions and falsifiers

- **P1 (EXPECTATION, 0.85):** all five blocks have `mult_det^∞ = 4`, `i_det^∞ = 0`;
  the theorem of §1.1 is banked.
- **P2 (EXPECTATION, 0.15):** some block has `rank_p G < 4` at both primes with
  the same rank, and with a second, independent point family (seed + 1000) —
  the first candidate stable determinant equation at weight 13.  Then the
  verification protocol takes over before anything is reported: (i) a third
  point family and 4× the points; (ii) rational reconstruction of the kernel
  vector over `Z` from both primes, exact `E·v = 0` over `Z`; (iii) exact
  vanishing at fresh integer points of `M_6` and **nonvanishing** at a generic
  point of `Z` (so `v ≠ 0` as a polynomial); (iv) the covariance check on `v`;
  (v) the degeneracy pre-check of `docs/brief_wording.md` §5 is not applicable
  (this is a determinant-side ideal element, not a statistic); the finding is
  reported as a candidate with its certificate.  **Stop at the first such
  block** (brief).
- **F1-P1 (instrument):** `dim K ≠ a_∞` at either prime, or a calibration block
  disagrees with the record, or the covariance check fails on a kernel vector
  → Part 1 stops, the defect is diagnosed, nothing is reported as a result.
- **F2-P1 (instrument):** the negative control PASSES the covariance check
  (the check has no teeth) → same.
- Primes disagree on `rank G` → recorded, more points, both primes re-run
  with a fresh seed; no verdict until they agree.

### 1.6 Stopping rules (Part 1)

- Any block whose raw space exceeds 10× the `a_∞ = 1` maximum (52 400) or whose
  kernel does not finish in 2 h wall or 6 GB: report the measured sizes and
  stop Part 1 (the brief's trigger for a batch-13 slot).  Not expected.
- Do not continue into an `a_∞ = 5` census (brief).

---

## Part 2 — the first non-washout padded frontier at `ℓ = 6`

### 2.1 The question and what is already known

At `r = ℓ = 6`, `P_6 ⊊ R_6` (`55 < 61`, PROVED, `docs/transfer_lemma.md` Lemma 1;
MEASURED s64 §5b), so `mult_pad < mult_red` is possible for the first time; and
`I(D_6^{per_3})_δ = 0` for `δ ≤ 8` (PROVED s37/s43/s47, `docs/exactness.md` §7),
so by Prop. 8(1) of the transfer lemma **`mult_pad = mult_red` at every six-row
weight with `δ ≤ 8` is a theorem** — those cells are consistency checks, and
the first cell where `mult_pad < mult_red` can occur has `δ ≥ 9`.  The six-row
negative record (`wk9_s57_lib.negative_record`, ADOPTED): 210 cells, all
`mult_det = a`, at `δ = 6..10`, every one skewed; `I(M_6)` has no component of
tail weight `≤ 12` (s57, PROVED given the record).

Sought, at six-row cells not in the record: `i_det ≥ 1`, or `mult_pad < mult_red`.

### 2.2 The instrument

`analysis/wk12_s79_cell6.py`: session 71's hybrid cell driver
(`wk11_s71_cell.py`) made length-general (`R = len(λ)`), on the unchanged
engine — `wk9_s45_build.build_cell` (monomials, χ-isotypic reduction, raising
rows), `wk11_s71_hybrid.hybrid_kernel` (initial-term cover + exact Schur
complement, every kernel vector verified on the full `E`), session 60's
evaluation rows.  Four families at every cell, both primes, `K_pts = a + 8`:

- `det`: `det_4(Σ_{i≤6} s_i A_i)`, seed 11 (session 60's stream, length 6);
- `red`: `(★)` point-free (`K[non-red rows]`, Theorem (★), length-general mask)
  and reducible points `l·c`, seed 29;
- `pad`: the TRUE padded permanent `x_0·per_3` restricted to a generic 6-plane,
  `wk10_s64_pad.pad_frames(K, 37, bound, 6)` / `pad_coeffs` (session 64's
  family, `ev_pad = restrict(PAD34)`; `dim P_6 = 55` separation MEASURED s64);
- `per4`: unpadded `per_4` pencils of length 6, seed 47 — **proper at `r = 6`**
  (`16·6 − 6 = 90 < C(9,4) = 126`; at `r = 5` it is vacuous, s71), so this is
  the column's first non-vacuous use.

`mult_X = rank_p(ev_X·K)`; `i_X = a − mult_X`; `D = mult_pad − mult_det`
(`docs/brief_wording.md` §7 direction; `D > 0` refutes containment).  Full rank
at one prime proves `mult_X = a` over `Q`; a drop is MEASURED until the
protocol.  Cost model, stated per number: **the hybrid model** (s71 re-fit):
build `2.1·10⁻⁶ s · N_S·δ`, evaluation rows `2.7·10⁻⁸ s · N_S·δ` per point,
hybrid never the cost below `n_χ ~ 10⁵`.  The compact circuit is **not** used
at any cell of this session: no `ℓ = 6` shape class here is two-tall-column,
and the brief forbids the s69 cost model without an exhibited contraction
representation and pathwidth bound.

### 2.3 Calibration (MEASURED, must reproduce, before the queue)

Both primes at every cell:

| cell | `a` | banked | source |
|---|---|---|---|
| (12,9,8,1,1,1)_8 | 6 | `mult_red = 4`, `mult_det = 6` | s47 exactness, integer certs |
| (14,8,7,1,1,1)_8 | 9 | `mult_red = 8` | s47 |
| (17,12,4,1,1,1)_9 | 8 | `mult_red = 7`, `mult_det = 8` | s47 / s43 |
| (16,13,4,1,1,1)_9 | 7 | `mult_red = 6`, `mult_det = 7` | s47 / s43 |
| (22,6,2,2,2,2)_9 | 8 | `mult_det = 8` | s43 |
| (19,9,5,1,1,1)_9 | 12 | `mult_det = 12` | s43 |

plus `mult_pad = mult_red` at the two `δ = 8` cells (theorem) and
`mult_per4 ≤ a` with the per4 family shown to be proper (Jacobian rank of the
length-6 `per_4` parametrisation `< 126`, both primes).  **Cross-instrument
check (PROVED to be required, Prop. S):** at `(27,5,3,2,2,1)_10` — a T2 first
stable cell, `a = a_∞ = 4` — the quartic `i_det` must equal Part 1's
`i_det^∞((5,3,2,2,1))`.  A disagreement stops both halves (F1-P2).

### 2.4 The region, in cost order

- **Q1 (123 cells):** the six-row cells of session 57's nominees T1 (room-one)
  and T2 (first stable cells of open tails of weight 13–16) not in the record,
  ordered by `N_S·δ` (exact `N_S` from `results/s57_cells/`), from
  `(13,7,4,2,1,1)_7` at `4.5·10⁵` to `(12,4,4,4,4,4)_8` at `2.2·10⁸`; 62 at
  `δ = 10`, 27 at 9, 25 at 8, 6 at 11, 2 at 7, 1 at 12.  List frozen in
  `results/s79_queue.json` before the first cell.  Cells whose tail Part 1
  closes (`(5,2,2,2,2)`, `(5,3,2,2,1)`, `(6,2,2,2,1)` if they die) keep their
  place — they are then the cross-instrument check, not new information on the
  determinant side, and their padded side is still new.
- **Q2:** every other six-row cell with `a ≥ 1` at `δ ≤ 12` in the s57 tables,
  not in the record and not implied dead (same `a` as a lower measured
  full-rank cell of its ladder, Lemma L), by `N_S·δ`, after Q1.
- Build wall: `N_S·δ > 2·10⁸` (the s71 wall in a 7 GB box) is not attempted;
  reported as the boundary with its `N_S·δ`.

### 2.5 Predictions and falsifiers

- **P3 (EXPECTATION, 0.75):** `i_det = 0` at every Q1 cell reached.
- **P4 (EXPECTATION, 0.6):** `mult_pad = mult_red` at every cell reached with
  `δ ≥ 9` (no permanent-specific equation of `D_6^{per_3}` in the degrees
  reached); the negative is characterised over the priced region.
- **P5:** `i_per4 = 0` at every cell (per4 proper but its ideal starts high) —
  EXPECTATION 0.7; a drop here is recorded as a `Per_6` result, not the goal.
- **Success (either):** a cell with `i_det ≥ 1` (a six-row determinant equation
  — the successor laboratory), or with `mult_pad < mult_red` (the first
  permanent-specific equation at `r = 6`).  Either triggers the protocol before
  it is reported anywhere: second prime already in; a second point family
  (seeds + 1000); the kernel vector exhibited in χ-coordinates and verified
  `E·v = 0`; for `mult_pad < mult_red` the consistency check with Prop. 8
  (impossible at `δ ≤ 8` — a drop there is an instrument defect, F2-P2) and a
  vector shown to vanish at fresh padded points and not at reducible points;
  for `i_det ≥ 1` the s63-style two-sided control (full rank on the same
  engine at a record cell of the same ladder or a neighbour).
- **`D > 0` at any cell:** halt the sweep; the verification protocol takes over.
- **F1-P2:** a calibration cell disagrees with the record at either prime, or
  the cross-instrument check fails → the sweep does not start / stops.
- Primes disagree → recorded, cell re-run with a fresh hybrid seed; no verdict
  until they agree.

### 2.6 Stopping rules (Part 2)

- Wall-clock: the queue runs until 08:00 UTC 2026-09-09 at the latest; what is
  reached is reported with its cost, what is not with its `N_S·δ`.
- Build wall as in §2.4.
- Information rate (s71's rule): 60 consecutive cells with `i_det = 0`,
  `mult_pad = mult_red`, `i_per4 = 0` and the per-cell cost above 10 min →
  stop and characterise.
- Memory: any cell whose build exceeds 5.5 GB RSS is abandoned and recorded.

---

## Deliverables

`results/PREREG_s79.md` (this file); `analysis/wk12_s79_stable.py`,
`wk12_s79_stable_check.py`, `wk12_s79_cell6.py`, `wk12_s79_sweep6.py`;
`results/s79_stable/` (the five blocks, calibration, covariance checks,
certificates and artefacts); `results/s79_cells.jsonl` (every cell, both
primes, all four families, cost and model); `results/s79_queue.json`;
`docs/s79_report.md`; bundle `s79_frontiers.bundle` + `.md5`.
