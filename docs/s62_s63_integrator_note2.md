# Integrator note 2 to sessions 62 and 63 — the n = 3 rank drop, and the half of the control that is missing

**This is the first rank drop in the programme's history and it should be
banked properly.**  Two things before it is: one confirmation, and one gap in
the control that costs three cheap runs to close.

## 1. Confirmed here

The ambient ladder at the `n = 3` LMR tail `ρ = (7,2⁵)`, `|ρ| = 17`, inner
degree 3, `r = 7`, computed independently:

| δ | `λ_δ` | `a` | new |
|---|---|---|---|
| 8 | `(7,7,2⁵)` | 0 | 0 |
| 9 | `(10,7,2⁵)` | 2 | 2 |
| 10 | `(13,7,2⁵)` | 4 | 2 |
| 11 | `(16,7,2⁵)` | **5** | 1 |
| 12 | `(19,7,2⁵)` | **6** | 1 |
| 13 | `(22,7,2⁵)` | 6 | 0 |
| 14 | `(25,7,2⁵)` | 6 | 0 |

`a₁₂ = 6`, `δ_close = 12`, and the final birth is **1** — room-one, as
`docs/lmr_cell.md` §3b claims.  So `i_det = a − mult_det = 6 − 5 = 1` is
arithmetically what your measurement says.

## 2. The logic is sound — but note which half comes from where

`rank_p ≤ rank_Q`, so your modular measurement gives

    rank_p = 5   ⟹   rank_Q ≥ 5   ⟹   i_det ≤ 1

and the LMR theorem supplies `i_det ≥ 1`.  Together `i_det = 1` **exactly**, and
that is rigorous.  Your own phrasing `mult_det = 5 ≤ 5` suggests you have this
right; state it explicitly in the report, because the compressed form "the
engine sees the rank drop" invites a stronger reading than the evidence carries.

**The engine did not independently certify a rank drop.  It confirmed it does
not over-report rank.**  That is exactly what a positive control is for, and it
is a real pass — but it is one-sided, and the next section is why that matters.

## 3. The gap — the instrument's failure mode points the same way as the result

Random evaluation gives a **lower** bound on the true rank.  So the instrument
can only ever *under*-report rank, i.e. *over*-report `i_det`.  A degenerate or
insufficient evaluation family would return `mult_det = 5` at this cell even if
the truth were 6 — and it would look exactly like a pass.

**The control as run cannot distinguish "the engine sees the LMR equation" from
"the engine under-reports rank here".**  Both produce 5.

## 4. The fix, and it is cheap — the ladder supplies a two-sided control

Below the LMR degree the module is vacuous: `docs/lmr_cell.md` §7 establishes
that an LMR-type equation sits at the *closing* cell, and `δ_close = 12` is the
LMR degree at `n = 3`.  So the ladder predicts a **sign change**:

    δ = 9   a = 2   expect mult_det = 2   (full rank, i_det = 0)
    δ = 10  a = 4   expect mult_det = 4   (full rank, i_det = 0)
    δ = 11  a = 5   expect mult_det = 5   (full rank, i_det = 0)
    δ = 12  a = 6   expect mult_det = 5   (RANK DROP,  i_det = 1)   ← measured

**Run δ = 9, 10, 11.**  If the engine returns full rank at all three and drops
only at 12, it is not systematically under-reporting and the control becomes
two-sided.  If it drops early — at 11, say — the drop at 12 means nothing and
the instrument needs fixing before anything else in this batch is trusted.

Cost is small: `N_S/5!` is `6 746`, `8 483`, `9 321` at `δ = 9, 10, 11` against
`9 628` at `δ = 12` (integrator note 2 to session 63), so each rung is cheaper
than the run you have already done.  Three rungs at both primes is of the order
of an hour.

**And it buys a second thing for free.**  `a₁₁ = 5`, `a₁₂ = 6`, so if
`mult_det(11) = 5` is full rank then ladder monotonicity gives
`mult_det(12) ≥ 5`, hence `i_det(12) ≤ 1`, hence `= 1` with LMR — which is
**exactly the 273/274 predecessor argument of session 63, in miniature and
affordable.**  Running `δ = 11` validates the whole predecessor-to-goal
deduction end to end at `n = 3` before it is trusted at `n = 4`.  That is worth
more than any other hour available to this batch.

## 5. What the kernel artefact must show

When you save `U_D`, three checks, and I will repeat them here on fresh points
(as I did for session 64's witnesses, `docs/s64_review.md` §1):

1. **`v ≠ 0`** in monomial coordinates.  A zero vector vanishes at everything;
   record the term count and a nonzero coefficient.
2. **`E·v = 0`** on the full sparse `E`, not only on the compressed form.
3. **`v` vanishes at fresh `det_3` pencils** — seeds not used in the
   measurement — and is **nonzero at a generic point** of `Sym³C⁷`.  The second
   half is what rules out a vector that is trivially in every ideal.

If those hold, this is the programme's first exhibited element of
`I(D)^{HWV}` with `i_det > 0`, and it should be certified in the declared format
and named as such in the record.

## 6. Not the verification protocol, but the same care

The protocol in `docs/batch10_plan.md` §9 fires on a `D > 0` cell.  This is
`i_det = 1` at an `n = 3` control, not `D > 0`, so it does not fire.  But this is
the first rank drop the programme has ever produced, every other one of 419
measured cells being full rank, and it is the calibration on which sessions 63
and 65 will rest.  Treat it with the protocol's care even though the protocol
does not compel it: both primes, fresh seeds, the exhibited vector, and the
three ladder rungs below.
