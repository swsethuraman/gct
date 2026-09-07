# Pre-registration — session 63, the LMR determinant block (C2)

Branch `s63-lmrdet` off `226b4ef1` (ancestry gate passed:
`git merge-base --is-ancestor 226b4ef1 HEAD` is true). Committed before any
measurement, per the standing rule. Container: 2 cores, 7 GB RAM, python-flint
0.9.0, numpy 2.4, scipy 1.17.

## 0. The question and the deduction it feeds

Cell: `λ = (65,17,2⁷)`, `δ = 24`, `ℓ = 9`, `|λ| = 96 = 4δ` — the
Landsberg–Manivel–Ressayre weight at `n = 4`, `k = 6`. This is the smallest
length (`r = 9`) at which any equation the programme knows of is non-vacuous
(`docs/equation_census.md`, `docs/lmr_cell.md` §1), and the only cell in the
record with a theorem-guaranteed `i_det ≥ 1`.

**Question.** Is `i_det = 1` at the LMR cell?

**The deduction (proved, modulo the one rank fact this session targets).**
With `a₂₃ = a((61,17,2⁷),23) = 273` and `a₂₄ = a((65,17,2⁷),24) = 274` the
source multiplicities, and the ladder theorem (s57 Lemma L / Proposition S:
`mult_det` non-decreasing along the ladder):

```
rank Θ⁺₂₃ = 273 (full)  ⟹  mult_det,23 = 273
                         ⟹  mult_det,24 ≥ 273         (ladder monotonicity)
                         ⟹  i_det,24 = 274 − mult_det,24 ≤ 1
                         ⟹  i_det,24 = 1               (LMR gives i_det,24 ≥ 1)
```

Equivalently, directly at `δ = 24`: `rank Θ⁺₂₄ ≥ 273` together with the known
equation's `rank ≤ 273` pins `rank₂₄ = 273`, hence `i_det,24 = 1`.

**We need a lower bound of 273 on a rank. We never need rank 274 and never need
a rank drop.** A projection `P` of the 48 825-dim target onto few coordinates
obeys `rank(PA) ≤ rank(A)`, so a projected block of rank 273 forces the original
`≥ 273` — the inequality runs in the safe direction. A rank drop in a projection
proves nothing and is never reported as one (Task 4 protocol below).

## 1. Regimes and what is proved where

| quantity | status entering the session | this session |
|---|---|---|
| `a₂₃ = 273`, `a₂₄ = 274` | measured, s57/s58 (integrator reproduced) | **independently reproduce (Task 1)** — the whole deduction rests on these two integers |
| ladder monotonicity of `mult_det` | proved (s57 Lemma L) | adopted |
| `i_det,24 ≥ 1` | proved (LMR, non-vacuity at `r ≥ 9`) | adopted |
| `sk = 48 825` | measured, single-source (s58 + Manivel) | **not used** by the projection deduction; see §5 |
| `rank Θ⁺₂₃` (or `rank Θ⁺₂₄`) | unknown | **target** |

**Claims that do NOT depend on `sk`.** The entire projection deduction:
`a₂₃`, `a₂₄`, monotonicity, LMR non-vacuity, and any rank lower bound obtained by
evaluation/projection. The target dimension `48 825` is not an input to
`rank(PA) ≤ rank(A)` — a nonvanishing 273-minor of a projected evaluation block
needs no target dimension at all.

**Claims that DO depend on `sk`.** None required for `i_det = 1`. `sk` enters
only if a full Foulkes-`Θ⁺` rank is attempted (routes 2/3 below) as the
codomain dimension; it is single-source and will be flagged wherever it is used.

## 2. Instruments and the three projections (Task 2)

`mult_det(λ,δ) = a − nullity_Q[E; ev_det]` where `E` is the stacked simple
raising operators on the `χ_λ`-isotypic reduction `V_χ` and `ev_det` are
evaluation rows at `K = a + 8` random `det₄` pencils (the native instrument,
`analysis/wk9_s60_cell.py` generalised from `r = 5` to `r = 9`). Equivalently
`mult_det = rank G`, `G = [f_i(det₄(P_j))]` over an HWV basis `{f_i}` and pencils
`{P_j}`; `rank G ≤ mult_det ≤ a`, with equality for generic/enough points, and a
nonvanishing `mult_det`-minor of `G` certifies the lower bound exactly over `Q`.

Three ways to realise the projection `P`, to be costed at `r = 9` before
committing:

1. **Evaluation at random `det₄` pencils** — the native HWV route above. Cost is
   dominated by the `χ_λ` build: enumerate the weight-`λ` monomials
   (`N_S,23 = 156 419 279 221`), reduce by `Stab_W(λ) = S₇` (`|Stab| = 5040`) to
   `n_χ ≈ 3·10⁷` columns, assemble `E`, solve for the `a`-dim kernel. **The
   `n_χ`/`N_S` wall is the first thing to measure.**
2. **Random functionals on `Θ⁺`, one `λ`-block column at a time** — the Foulkes
   route (s56) restricted to a single `λ`-column rather than the whole module.
   s56's engine is quadratic in `|H_{4,δ}|`; `|H_{4,23}|` is the cost to state.
3. **s62 Gram/Schur route**, if `docs/s62_report.md` / `results/s62_cost.md`
   exist. **Checked at start: ABSENT.** Re-check at the halfway mark. char-0 only.

Deliverable `results/s63_routes.md`: the three costs at `r = 9`, reported even
if only one is pursued.

## 3. Seeds, primes, box (fixed here, before any run)

- House primes `P1 = 2147483647`, `P2 = 2147483629` for every modular rank.
- Random `det₄` pencils: `random.Random(SEED_DET + offset)`, entries in
  `[−BOX, BOX]`, `BOX = 40` (the s60 default; a second draw at `BOX = 10⁶` if any
  rank is marginal). **`SEED_DET = 20260907`** (session date). `K = a + 8` pencils.
- Any second/independent evaluation draw: **`SEED_DET2 = 20260907 + 4900`**.
- A rank that appears at one seed or one prime and not another is treated as a
  bug (the s44/s49 randomised protocol, `docs/randomised_protocol.md`).

## 4. Falsifiers, verification protocol, kill criteria

- **F1 (the anchor).** If Task 1 does not reproduce `a₂₃ = 273` and `a₂₄ = 274`
  by a route independent of the integrator's, **stop** — the deduction has no
  foundation and every downstream claim is void. Named sub-check: the LMR
  `a`-ladder `2, 39, 93, 145, 188, 219, 241, 255, 264, 269, 272, 273, 274`
  (`δ = 12…24`), monotone, final increment exactly 1, `a_∞ = 274` at `δ ≥ 31`.
- **F2 (rank-drop discipline).** If a projection returns a rank **below** what the
  ladder predicts (a "rank drop"), it is NOT reported as a drop. A modular rank
  drop is not a rank drop: re-run at the second house prime and over `Q` before
  it enters any report or message. Only a rank drop surviving both primes and `Q`
  is real, and it triggers the full re-derivation protocol (`D > 0` is
  STOP-EVERYTHING; here a genuine `rank₂₃ < 273` would contradict either `a₂₃` or
  monotonicity and must be re-derived, not reported).
- **F3 (points on the variety).** Every `det_pencil` point is given by
  substitution data (the pencil matrices), so the verifier rebuilds
  `det₄(Σ sᵢAᵢ)` and confirms the point lies on `D_r^{det}`. A bare coefficient
  list is never accepted as a det point.
- **Kill / time-box (the `n_χ` build).** The `χ_λ` build at `δ = 23` is
  pre-budgeted at **90 minutes wall and 6 GB RSS**. If the build (monomial
  enumeration + orbit reduction + `E` assembly) does not complete within that
  budget, **report the measured wall** — the point of `N_S` and `n_χ` reached,
  the extrapolated cost — preserve any partial compressed operators, and stop.
  Direct degree-24 completion is reserve E1 and is **not** this session's to
  force. Do not materialise all 48 825 target rows; if the code is building them,
  the projection argument has been abandoned — stop and reconsider.

## 5. Success and deliverables

**Success.** An exact, certified conclusion for `i_det` at the LMR cell —
preferably `i_det = 1` — with a reproducible certificate and an independent
check. An honest "the `n_χ` build is out of reach at `δ = 23` in a 7 GB / 2-core
container, here is the measured wall and the reproduced anchors" is an acceptable
outcome (the standing rule: a measured wall reported rather than an extended
budget).

**Deliverables.** `results/PREREG_s63.md` (this file); `docs/s63_report.md`;
`results/s63_routes.md`; certificates in `gct-cert/1` for every rank claim,
each stating its prime or char-0 status; the source basis and any kernel vector
`U_D = ker T_det` as machine-readable artefacts (for s65/s67); code under
`analysis/wk10_s63_*.py`; bundle `s63_lmr_det.bundle` + `.md5`.

**Prediction ledger (pre-registered).**

| id | prediction | prior |
|---|---|---|
| P1 | `a₂₃ = 273`, `a₂₄ = 274` reproduced by ≥ 2 independent routes | 0.97 |
| P2 | LMR `a`-ladder matches s57/s58 at every `δ = 12…24`, `a_∞ = 274` | 0.95 |
| P3 | the `n_χ` native build at `δ = 23` does NOT close in 90 min / 6 GB | 0.80 |
| P4 | the Foulkes single-`λ`-column route is infeasible (`|H_{4,23}|` wall) | 0.90 |
| P5 | if any rank is measured, both house primes agree | 0.98 |
| P6 | no genuine rank drop (F2) is observed | 0.97 |
