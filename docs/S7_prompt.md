# S7 — is `mult_pad = mult_red` a theorem for this family?

`board_numbering: batch13`.  A reasoning session.  Deliverables are proofs,
refutations, or a precisely stated obstruction — not a scan.

## The observation to explain or refute

| length | degree | finding | status |
|---|---|---|---|
| `r = 5` | — | `mult_pad = mult_red` | s64 |
| `r = 6` | `δ ≤ 9`, length-6 weights | `mult_pad = mult_red` | theorem via `I(D₆^{per₃})₉ = 0` (s79; a 365-weight hole, s81 is closing it) |
| `r = 6` | `δ ≤ 12`, 682 cells | `mult_pad = mult_red` | measured, verified |
| `r = 9` | `δ = 13` | the padded kernel **is** the reducible kernel | measured, integrator |
| `r = 9` | `δ = 24` | `U_R = U_P`, and `i_per4 = 0` | measured, s74, verified |

Four instruments, three lengths, every weight measured, no exception.

## The question

Is there a structural reason?  Three shapes an answer could take:

1. **`I(D_r^{per₃})_δ = 0` in a range, for a reason.**  Prop. 8(1) then gives
   `mult_pad = mult_red` at every weight of that length and degree, and the
   scanning stops.  This is the most valuable outcome: it converts an empirical
   pattern into a theorem and retires four sessions of the batch.
2. **A containment or degeneration argument** that forces the two ideals to agree
   in the degrees this family reaches — perhaps through `2N + 1 ≤ m² + 1`
   (S5's scope limit), perhaps through the `ℓ·` factor dominating the isotypic
   decomposition.
3. **A cell where they must differ**, exhibited.  That redirects the batch and
   is worth as much as (1).

## What you have

- `docs/transfer_lemma.md` — Prop. 8 in both directions, and Lemma 1
  (`P_6 ⊊ R_6`, `55 < 61`).
- `docs/stocktake_batch12.md` — the measurements and their status.
- `docs/s74_final_review.md` §1 — the goal-cell statement and the screen it
  hands the programme.
- `docs/rung13_reducible.md` — the rung-13 coincidence, with a generic control.
- s64's `dim P_6 = 55` separation; s79's `I(D₆^{per₃})₉` on the length-6 weights.

## What would settle it

A statement of the form: *for `r ≤ R` and `δ ≤ Δ`, `I(D_r^{per₃})_δ = 0`*, with
`R` and `Δ` as large as you can prove and a reason that is not a computation.
Or the negation, with a witness.

Note the asymmetry the programme now runs on: a nonzero minor is a rank floor and
proves `i ≤ a − k`; **nothing proves `i ≥ 1` except a membership statement.**  A
theory session is the cheapest source of membership statements the programme has.

## Deliverable

A report with the argument in full, its hypotheses stated, and — if it does not
close — the precise obstruction, so batch 14 can price it.
