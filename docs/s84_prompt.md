# s84 — `i_pad(23)` exactly, by S4's factorization

`board_numbering: batch13`.  Read `docs/batch13_worker_preamble.md` first.

## Mission

Decide `D` at the LMR goal cell by exact linear algebra.  This is the only route
in the programme that can prove any value of `D` other than `+1`.

## What is true going in (all verified by the integrator)

    rank T_det(24) = 273  exactly, i_det(24) = 1        PROVED
    i_pad(24) = i_pad(23), eps_pad = 0                  PROVED
    D = 1 - i_pad(23),   -4 <= D <= +1                  PROVED
    rank T_pad(24) >= 269                               CERTIFIED (nonzero minor, both primes)
    U_R = U_P at the goal cell, i_per4 = 0              MEASURED, both primes

`rank T_pad = 269` and `i_pad = 5` are **sampled ceilings**, not theorems.  A
nonzero minor is a rank floor and can only push `i` down; nothing proves
`i_pad ≥ 1` except a membership statement.  See `docs/s74_final_review.md`.

## The instrument

S4's factorization (`results/astra/S4/`, and the integrator's
`docs/s4_batch12_review.md`):

    M_λ  --S-->  ⊕_μ M^{(3)}_μ  --Q-->  ⊕_μ N_μ
    rank T_pad = rank S − dim( S(M_λ) ∩ ker Q )

Finite exact linear algebra over `Q`.  No points, no orbit closure, no
membership argument left over.  **The input it has never had is a source** —
session 74's 274 rows, `results/s74/source.json`, generic nullity 0 verified, are
that input.

## Task 1 — `rank S`, the screen pre-registered in batch 11

`docs/batch11_plan.md` C3: `mult_pad ≤ mult_red = rank S`, so

> `rank S < 274` ⟹ `i_pad ≥ 1` ⟹ **`D ≤ 0`**, with no padded points at all.

`S` is the `274 × 521` reducible-normalisation split — an exact rank of a
structural matrix, not a sampled evaluation.  It is the cheapest possible
settlement of the cell and it has never been run for want of a source.  **Run it
first**, and report it before anything else in your report.

Do the same at rung 23 on the 273 transported rows, which is where
`D = 1 − i_pad(23)` actually lives.

## Task 2 — `dim(S(M_λ) ∩ ker Q)`, if `rank S = 274`

Compute it exactly over `Q`.  That is `i_pad`, and `D = 1 − i_pad` decides the
cell.  Report the dimension, a basis if it is small, and the degree of exactness
(`Q` throughout, or `Q` with a modular certificate — say which).

## Cross-checks that must hold

- `rank S ≥ mult_pad ≥ 269` (s74's certified floor).  A `rank S` below 269
  contradicts a nonzero minor and is an instrument defect, not a result.
- `rank S ≤ 274` and `≤ h_pad = 521`.
- If Task 2 returns `i_pad(24) ≠ i_pad(23)`, that contradicts the proved
  `eps_pad = 0` — an instrument defect.
- s74's 12-minor cross-check (`results/s74/s4_crosscheck.json`, 144/144) must
  reproduce on your build of `S` and `Q`.

## Predictions

- **P1 (0.5):** `rank S = 274`, so the screen does not fire and Task 2 decides.
- **P2 (0.3):** `rank S < 274`, so `D ≤ 0` is proved and the cell is settled
  against a multiplicity obstruction with no padded points.
- **P3 (0.2):** the factorization does not close at this size and the deliverable
  is the price of the two ranks.

Any outcome with `D > 0` triggers the verification protocol before it is
reported anywhere.

## Deliverables

`results/PREREG_s84.md`; `rank S` at rungs 23 and 24, both primes and over `Q`;
`dim(S(M_λ) ∩ ker Q)` if reached; the cross-checks; `docs/s84_report.md`;
bundle + `.md5`.
