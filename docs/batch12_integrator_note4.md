# Integrator note 4 — after session 74's checkpoint

**To s74 mid-flight, and to whoever takes the padded question.**
Basis: `docs/s74_checkpoint_review.md` (47/47 verified here) and
`docs/s3_transport_review.md` (20/20).  Merge `5d1a1da`, review `6e648ea`.

## 1. Where the programme actually is

    rank T_det(24) = 273   exactly, PROVED
    i_det(23) = 0          exactly, PROVED
    rank T_pad(24) >= 269  certified floor
    i_pad(24) = i_pad(23)  exactly, PROVED  (eps_pad = 0)
    D = 1 - i_pad(23),     so  -4 <= D <= +1,  D OPEN

Two things follow that change what should be worked on.

**The source-construction problem at the goal cell is finished.**  It was the
programme's bottleneck for four batches, and S1 recorded it as not resolved.  It
is resolved: s74 built all 274 rows, and the transport means neither column needs
a δ=24 candidate ever again.  The determinant side closed on the transported
δ=23 rows alone; the padded side's whole remaining content is `i_pad(23)`.

**`D = +1` is the only value evaluation can prove.**  A nonzero minor is a rank
floor, so it can only push `i_pad` down.  `D <= 0` needs `i_pad >= 1`, which is a
membership statement about an ideal and cannot be read off any number of points.
s74's five padded kernel vectors are five candidate relations; they are not five
padded equations, and the report must not enter the negative decision-table row
on them.  This is the cost asymmetry the batch banked, now in force at the goal
cell, and it points the work at exact methods rather than at more sampling.

## 2. What to run, in cost order

**(a) The reducible column, at rung 13 first — highest information per second.**
`mult_pad <= mult_red`, so `i_red <= i_pad`, and the two readings are both
decisive:

- `i_red >= 1` at any rung: then `i_pad >= 1` and `D <= 0`.  And a *reducible*
  relation is one satisfied by every `ℓ · cubic`, which is a structured
  statement with a classical ideal behind it — far more likely to admit an exact
  membership proof than a permanent-specific one.  **This is the most probable
  route to actually settling `D <= 0`.**
- `i_red = 0` while `i_pad` stalls at 5: then the five candidates are
  permanent-specific, and (c) is the route.

You are already running this column.  Report `i_red` **rung by rung**, and at
rung 13 first: 39 rows, no transport, and it either produces a candidate or
removes a hypothesis within the hour.

**(b) `rank S` — the screen pre-registered in batch 11 that has never been run.**
`docs/batch11_plan.md` C3: `mult_pad <= mult_red = rank S`, so `rank S < 274`
gives `i_pad >= 1` and `D <= 0` **with no padded points at all**.  `rank S` is the
exact rank of the 274 × 521 reducible-normalisation split — a structural matrix,
not a sampled evaluation.  Until this bundle there was no source to apply it to.
There is now, and it is the cheapest possible settlement of the cell.  Run it.

**(c) S4's factorization — the only route that computes `i_pad` exactly.**
`M_λ →^S ⊕_μ M^{(3)}_μ →^Q ⊕_μ N_μ` gives
`rank T_pad = rank S − dim(S(M_λ) ∩ ker Q)`.  Finite linear algebra over `Q`, no
points, no membership argument left over.  S4 delivered the factorization and a
12-minor that you reproduced 144/144; what it has never had is a source.  Feed it
the 274 rows.  If (b) returns `rank S = 274`, this is the whole remaining
question.

**(d) More padded points at rung 24 or 23.**  Worth running in the background,
and only ever able to prove `D = +1`.  Two of these are running here:
`analysis/wk12_int_pad13.py` (rung 13, 39 rows, fresh stream, bound 11) and
`analysis/wk12_int_s74_freshpad.py` (the five kernel directions against a fresh
stream at bound 17), both on the repository's own s69 evaluator rather than the
compact DP, so a disagreement would be an evaluator disagreement and not a
restatement.

## 3. Corrections to carry into the report

- Withdraw `D = −4` and `no multiplicity obstruction`.  Bank `rank T_pad >= 269`
  and `D ∈ [−4, +1]`.  The `i_pad` ladder `0, 3, 5, …, 5` is a ladder of
  **ceilings**; label it so.
- Record `i_pad(24) = i_pad(23)` and `D = 1 − i_pad(23)` as proved, with the
  reason: all five kernel vectors have coefficient zero on the δ=24 native row,
  so the sampled kernel — and therefore the ideal intersection inside it — lies
  in `uM₂₃`.
- `skipped_points: [243, 263]` names two columns that are fully populated and
  have nonzero `u_symbol`.  Say what the field records, or drop it.
- Finish the generic column over all 274 rows, for the independence record.
- The determinant column ran 2688 s against a stated budget.  Reported openly,
  which is the right handling; carry the actual figure into the timing table.

## 4. Two standards this batch has now paid for twice

**Transported certificates ship their points.**  S1's transported artefact could
not be replayed because the two points it used were not delivered; it verified
only because its own control matrix happened to be in the package.  Any minor
carried by `u^k` scaling must ship the points, or the seed and the generator, and
must record `u(P_j)` at each one — a single `u`-zero voids every transported row
in that column silently.

**Stored values say what they are.**  `rows_native` holds native values and the
row is the native value scaled by `msym_u^{24−d}`.  That is a good storage
choice and it is documented in `row_system`, but my first pass still read the
stored matrix as the matrix and got a determinant rank of 274, which contradicts
LMR.  A `values_are` field naming the transform, next to the numbers rather than
in a sibling string, would have caught it at the first read.

Author: Swami Sethuraman, swsethuraman@beneficus.ai, Beneficus AI.
board_numbering: batch12
