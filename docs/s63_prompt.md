# Session 63 (C2) — the LMR determinant block

Batch 10, wave 2, but **runnable now**: the plan gates this on session 62's
engine choice, and the route below does not require it.  Base commit `226b4ef1`.
**Read `docs/batch10_worker_preamble.md` first**, then `docs/batch10_plan.md`
§4 (C1, C2), `docs/lmr_cell.md` in full, `docs/s58_review.md` §1, and
`docs/s56_report.md`.

## The question

Is `i_det = 1` at the LMR cell?

## Why this cell and no other

`λ = (65,17,2⁷)`, `δ = 24`, `ℓ = 9`, `|λ| = 96 = 4δ`.  This is the
Landsberg–Manivel–Ressayre weight at `n = 4`, `k = 6`.  Session 55's census
shows the family is empty for `r ≤ 8` (containment forces `k ≥ min(6, r−2)`,
non-vacuity forces `k ≤ r−3`), and at `r = 9` the two conditions pinch to
`k = 6` exactly.  **So `r = 9` is the smallest length at which any equation the
programme knows of is non-vacuous, and this is the only cell in the record with
a theorem-guaranteed `i_det ≥ 1`.**  Every one of the 419 measured cells has
`i_det = 0`, and all of them have `r ≤ 6`, where the family is empty.

## The two goals, and either one settles it

    A.  predecessor   (61,17,2⁷),  δ = 23,  source a₂₃ = 273
    B.  goal cell     (65,17,2⁷),  δ = 24,  source a₂₄ = 274

Target dimension `sk((65,17,2⁷), 24⁴) = 48 825`, already constant from `δ = 23`.

    rank₂₃ = 273  (full)  ⟹  mult_det,24 ≥ 273  (ladder monotonicity)
                          ⟹  i_det,24 ≤ 1
                          ⟹  i_det,24 = 1        (LMR gives ≥ 1)

or, directly at `δ = 24`, `rank₂₄ ≥ 273` suffices — the known equation already
gives `rank₂₄ ≤ 273`, so the two together pin `rank₂₄ = 273`.

**You never need rank 274, and you never need a rank drop.  You need a lower
bound of 273.**  That is the whole shape of this session and it is what makes it
tractable.

## The architectural point — do not materialise 48 825 rows

`rank(PA) ≤ rank(A)` for any linear `P`.  So if `P` is a projection of the
48 825-dimensional target onto a few hundred coordinates or functionals and the
projected block has rank 273, then the original has rank **at least** 273 — and
that is exactly the bound you need.  The inequality runs in the safe direction;
a rank *drop* in a projection proves nothing and must never be reported as one.

Three ways to realise `P`, and part of this session is deciding which is
cheapest — **cost them before committing**:

1. **Evaluation at random `det_4` pencils.**  This is already a projection of
   the target, and it is the programme's native instrument:
   `mult_det = a − nullity_Q [E; ev_det]` as in `analysis/wk9_s60_cell.py`, with
   `E` the stacked simple raising operators on the `χ_λ`-isotypic reduction and
   `ev_det` the evaluation rows at `a + 8` random pencils.  At `r = 9` the
   question is whether the highest-weight build is reachable; that is the
   `n_χ` wall and it is the first thing to measure.
2. **Random functionals on the `Θ⁺` target**, taking `Θ⁺` columns one at a time.
   Session 56's engine is quadratic in `|H_{4,δ}|` and `|H_{4,5}|` alone is
   2 546 168 625, so the whole-module route is closed; the question is whether a
   single `λ`-block column is reachable without it.
3. **Session 62's Gram/Schur route**, if its cost curve says so.  Check for
   `docs/s62_report.md` and `results/s62_cost.md` in the repository when you
   start and again at the halfway mark; use them if present, proceed without
   them if not.  Note that route is characteristic-zero only.

## Read session 66's territory carefully — the single-source dependency

`sk = (g + T)/2` with `g = 92 000` confirmed by three independent routes.
**`T = A = 5 650` is single-source**: session 58's reduction plus the external
Manivel route, validated at thirteen smaller cells but not at the goal cell,
where the direct partition sum is out of reach at `p(96) = 1.18 × 10⁸`.  Worse,
**at `δ = 23` Manivel's reduction does not apply at all** (`2δ = 46 < 48 =
|ρ| + ρ₁`), so there the target dimension rests on session 58 alone.

You do not need `sk` for a lower-bound-of-273 argument by projection — say
explicitly in your report which of your claims depend on it and which do not.
A Sol session is auditing `A` independently in parallel.

## Tasks

1. Independently reproduce `a₂₃ = 273` and `a₂₄ = 274` before anything else.
   The whole deduction rests on these two integers and on ladder monotonicity.
   `docs/lmr_cell.md` §2 and §3 record the route.
2. Measure the cost of each of the three projections above at `r = 9`.  Report
   the numbers even if you then proceed by only one.
3. Certify `rank₂₃ = 273` if reachable.  Otherwise certify `rank₂₄ ≥ 273`.
4. If a rank *drop* appears anywhere — that is, a projection where the rank is
   below what the ladder predicts — **stop, and treat it under the verification
   protocol.**  A modular rank drop is not a rank drop.  Re-run at the second
   house prime and over `Q` before it goes into a report or a message.
5. Preserve the source basis and, if you obtain one, the kernel vector.
   Session 65 needs `U_D = ker T_det` in explicit source coordinates, and
   session 67's audit needs it representation-theoretically.

## Success

An exact, certified conclusion for `i_det` at the LMR cell — preferably
`i_det = 1` — with a reproducible certificate and an independent check.

## Stopping rules

- Do not insist on materialising all 48 825 target rows.  If you find yourself
  building them, the projection argument above has been abandoned; stop and
  reconsider.
- If the predecessor is inconclusive, **preserve the partial compressed
  operators, write what the cost curve says, and stop.**  Direct degree-24
  completion is reserve E1 and is not this session's to force.
- Time-box the `n_χ` build.  If it does not close within the budget you
  pre-registered, report the measured wall rather than extending.

## Deliverables

`results/PREREG_s63.md`; `docs/s63_report.md`; the cost comparison of the three
projections as `results/s63_routes.md`; certificates in the declared format for
every rank claim, stating the prime or characteristic-zero status of each;
source basis and any kernel vector as machine-readable artefacts; code under
`analysis/wk10_s63_*.py`; bundle `s63_lmr_det.bundle` + `.md5`.
