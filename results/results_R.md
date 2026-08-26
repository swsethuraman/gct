# Point R = (x3+=x0, x7+=x1): the second-point k=1 certificate (session 12, 2026-08-25/26)

Factored scheme-1 evaluation of the k=1 HWV (lambda' = (8,8,8,6^6), delta = 20)
at the DD-class point R — PROVEN H-inequivalent to the original certificate
point C (the intersection algebra s(u) = h ∩ Ad(u)h transports by Ad along
double cosets H·u·H; exact rational computation gives s(u_C) 4-dim
non-abelian, bracket span 2, vs s(u_R) 4-dim ABELIAN; s(u_P) is 8-dim).

## Headline

    TOTAL_R = 1,152,144,000 = TOTAL_f1C   (nonzero; identical to C)

11 runs (8 extended-orbit reps + 3 relation-validating duplicates), engine
dp2g evalopts (checkpointed), all final states 1, ~90–105 min/run.

## Values (orbit-weighted assembly)

| rep | (s6,s7) rel class | orbit wt | VALUE |
|-----|-------------------|----------|-------|
| 00  | id                | 4        | +108,712,800 |
| 01  | (1 2)             | 8        | −21,772,800 |
| 02  | (0 1)             | 4        | −21,772,800 |
| 03  | 3-cycle           | 8        | +301,870,800 |
| 04  | 3-cycle           | 4        | +301,870,800 |
| 05  | (0 2)             | 4        | −476,884,800 |
| 07  | id                | 2        | +108,712,800 |
| 09  | (0 2)             | 2        | −476,884,800 |

Gates (all MATCH): pre V(14) = V(00) = +108,712,800; swap V(06) = V(01) =
−21,772,800 (this one executed twice by independent processes, agreeing);
post V(34) = V(02) = −21,772,800.

TOTAL_R = 4·V00 + 8·V01 + 4·V02 + 8·V03 + 4·V04 + 4·V05 + 2·V07 + 2·V09
        = 6·W_id + 12·W_small + 12·W_3cyc + 6·W_(02) = 1,152,144,000.

## Prediction ledger (all logged before the values landed)

23:20Z 2026-08-25, with 6/11 done: V(07) = +108,712,800 HIT; V(09) =
−476,884,800 HIT; three gates equal their reps — ALL HIT; TOTAL_R =
1,152,144,000 (6/12/12/6 profile echo) HIT. Earlier same evening, the four
W-class values themselves were open questions (explicitly NOT predicted,
per the DD-class novelty) — all four landed equal to C's table.

## What this establishes

1. **Second-point certificate**: the k=1 HWV h1 is nonzero at two
   H-INEQUIVALENT orbit points (C: cyclic class; R: diagonal class).
   Combined with the 2026-08-24 grind, its 4-fold validation, this
   container's exact f1C_00 reproduction, and Q's conjugate-point
   reproduction, the c((2,2,2),2) = 1 verdict's computational leg is
   hardened to the standard the programme set.
2. **Universality (empirical, 11/11 + C's 36 + Q's 2)**: the per-subproblem
   values V(sigma6,sigma7) are identical across every live balanced
   two-transvection point tested, spanning both H-classes. Conjecture: the
   functional N -> V((I+N)·det3) factors as (universal W-table) × Psi(N),
   Psi an H-invariant vanishing exactly on rank-1 directions (P's exact
   zeros) and constant on the live classes. Formulation caveats and the
   amb(lambda',20) = 3 multiplicity are recorded in PROJECT_NOTES
   (rigidity is a matrix-element statement, not a naive covariant one).
3. **Taxonomy**: feasible balanced two-transvection points = rank-1 (3 pts,
   exact vanishing) ∪ cyclic H-class (6 pts ~ C) ∪ diagonal H-class
   (6 pts ~ R). Two live classes, both now measured, equal totals.

## Companion controls (same night)

- f1D_00 = VALUE 0 (final states 0): engine-level confirmation of the
  weight-infeasible negative control D, through the same factored route.
- P-point: 4/4 exact zeros by terminal L19 cancellation (results_P.md).
- Q-point: p_Q = colperm(0 2 1)·p_C proven; its two runs reproduced C's
  W-values exactly through independent input files (pipeline validation).
