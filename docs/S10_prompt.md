# S10 — scope: what family could see the permanent, and at what cost?

`board_numbering: batch13`.  A reasoning session.  An honest "none in reach" is
an acceptable and useful answer.

## The situation

Batch 12's result is a negative with an unusually clean shape:

- `mult_pad = mult_red` at `r = 5`, `r = 6` (682 cells, and a theorem at degree 9
  on the length-6 weights) and `r = 9` (at degrees 13 and 24, verified).
- At the LMR goal cell the **unpadded** `per₄` has no equation at all in the
  weight `(65,17,2⁷)`: `i_per4 = 0`.
- So in every cell measured, `D = mult_pad − mult_det` equals
  `mult_red − mult_det`.  **The statistic is measuring reducibility, not
  permanence.**

And S5 already fixed this family's ceiling: `2N + 1 ≤ m² + 1` gives `N ≤ m²/2`,
`n = 4` is the last `ℓ·per₃`-admissible rung, and the family probes a quadratic
scale — so even a positive here would be a first working instance of a
multiplicity obstruction, not a Valiant-level separation.

## The question

Is there a family in which the multiplicity statistic can see the permanent at
all — and what would one cell of it cost on the instruments the programme now
has?

Three directions, and you are not limited to them:

1. **More variables.**  The padding `ℓ^{n−m}·per_m` with `r > m²`, so that `ℓ` is
   a genuinely new variable rather than a linear form in the same `m²`.  At
   `r = m²` — which is where this programme sits — every padded form is a
   reducible form in the *same* variables, which may be the whole explanation for
   `mult_pad = mult_red`.  Does `r = m² + 1` break it?  What does one cell cost?
2. **A different pair of orbits.**  The obstruction needs a functorial statistic
   (`docs/brief_wording.md` §7) and a containment in the right direction.  Is
   there a pair where the reducible locus does not sit between them?
3. **A different statistic on the same orbits**, still functorial under closed
   immersion.  §7's test is the gate: if it is neither functorial nor controlled
   under degeneration, "the two objects differ" says nothing about containment.

## What would make this session pay

A costed comparison: for each candidate family, the smallest cell where the
statistic could differ, its `a`, `N_S`, `n_χ` and `N_S·δ`, priced against the
instruments in the tree — session 71's hybrid model (`2.1·10⁻⁶ s · N_S·δ` build,
`2.7·10⁻⁸ s` per point), the `u`-transport, and s80's new build ceiling.  The
programme can then choose between finishing the negative and starting again
somewhere it can win.

## What you have

`docs/stocktake_batch12.md`, `docs/batch13_plan.md`, `docs/transfer_lemma.md`,
`docs/brief_wording.md` §5 and §7, S5's scope argument, s64's `dim P_6 = 55`.

## Deliverable

The costed comparison, the recommendation, and the argument for it — including,
if that is the answer, the argument that nothing is in reach and the programme's
right move is to write the negative up.
