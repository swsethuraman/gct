# Batch 13 — what the reasoning side corrected, and what I checked

My batch-13 plan had a wrong central premise.  This records the corrections, the
checks I ran on them, and the one thing the corrected picture says that neither
plan stated.

## 1. The premise was wrong: the cubic screen is not the gate for `D > 0`

I organised the batch on "`mult_pad < mult_red` requires `I(D_r^{per₃})_δ ≠ 0`,
therefore the cubic screen is the necessary condition for everything else."  The
second clause does not follow.  The two questions are different:

    mult_pad < mult_red     permanent-specific equations
    mult_pad > mult_det     the obstruction

`P ⊆ D` forces `mult_pad ≤ mult_det` at every weight, so `mult_pad > mult_det`
refutes containment **whether or not the equation is permanent-specific**.
Equality of the padded and reducible multiplicities does not stand in the way of
a positive obstruction; it only means the obstruction, if found, would also
separate `ℓ·c` from the determinant.  The cubic screen detects permanent-specific
information and makes the padded side computable by the cheap reducible route.
It is not a prerequisite for a determinant-side search.  **Correction accepted.**

### What the corrected logic actually says, measured

`mult_pad ≤ mult_red`, so

    D > 0  ⟹  mult_red > mult_det  ⟹  i_det > i_red.

I checked that against session 79's 682 six-row cells (`results/s79_cells.jsonl`):

| | |
|---|---|
| cells with `i_red < i_det` — the direction an obstruction needs | **0** |
| cells with `i_det ≥ 1` | **0** |
| cells with `i_red ≥ 1` | 59 |
| `D_R` distribution | `0` at 623, and `−1, −2, −3, −4, −5, −7, −25` at the rest |

`mult_red ≤ mult_det` at every one of the 682, and the determinant side is
full-rank at every one.  So **the binding constraint on `D > 0` is `i_det`, not
`i_pad`** — the determinant ideal must be *larger* than the reducible one at some
weight, and that has never been observed anywhere in the record.  The only cell
in the programme with `i_det ≥ 1` is the LMR cell, where `i_det = 1` and
`i_red = 5`.

Neither plan said this.  It follows from the correction, not from my premise, and
it is the honest statement of where the programme is stuck.

## 2. The 365 shorter weights are covered by an inherited theorem

`docs/washout_lemma.md` **Theorem 2 (proved)**: for `r ≤ 5` the map
`Φ_r : (A_i) ↦ per₃(Σ s_i A_i)` is dominant, `D_r^{per₃} = Sym³Cʳ`, by an exact
full-Jacobian-rank witness — rank 35 = `dim Sym³C⁵` at both house primes, banked
by session 26 and re-verified by session 37.  So `I(D_r^{per₃})` vanishes
identically at length ≤ 5, and by the restriction lemma every weight of length
≤ 5 inherits it at every degree.

My s81 brief would have spent a session recomputing 365 weights that a theorem in
my own tree already excludes.  **Correction accepted**, and the dependency is
`docs/washout_lemma.md` Theorem 2 plus Theorem 3(1); auditing that chain is worth
a fraction of a session and recomputing it is worth none.

The consequence for session 79: its 210 length-six degree-9 checks, together with
the inherited exclusion, do establish the full degree-9 statement.  My
`docs/s79_part2_review.md` §2 called that a gap.  **It is not a gap; it is an
undeclared dependency**, and the review is corrected accordingly.

## 3. Fifteen predecessors are a targeted screen

My s83 brief said "`I(D₉^{per₃})₁₃` in full: fifteen weights".  Wrong wording.
The fifteen horizontal-13-strip predecessors of `λ₁₃` are the cubic constituents
that could contribute to that one quartic cell through Prop. 8(2).  They do not
exhaust `I(D₉^{per₃})₁₃`.  The targeted result is still worth having — it settles
`mult_pad = mult_red` at `λ₁₃` — but its scope must be stated as targeted.
**Correction accepted.**

## 4. `D = 1 − i_pad(24)` is the unconditional form — and here is my argument for the rest

Agreed that `D = i_det(24) − i_pad(24) = 1 − i_pad(24)` is what stands
unconditionally.  I claimed `i_pad(24) = i_pad(23)`, and the argument is not
"the measurements suggest it" — it is this, and it should be audited rather than
dropped:

1. `I(pad) ∩ M₂₄ ⊆ ker(T_pad)` for **any** point set, since an ideal element
   vanishes everywhere.
2. All five kernel vectors have coefficient exactly 0 on the δ=24 native row at
   both primes (computed, `results/wk12_int_s74_final.json`).  The source basis is
   273 transported rows spanning `uM₂₃` plus that one native row, so
   `ker(T_pad) ⊆ uM₂₃`.
3. Hence `I(pad) ∩ M₂₄ ⊆ uM₂₃`, and the birth-quotient proposition gives
   `I(pad) ∩ M₂₄ = u·(I(pad) ∩ M₂₃)`, so `i_pad(24) = i_pad(23)`.

**The one gap, stated precisely:** step 2 is computed mod `p`.  A rational ideal
element with a nonzero birth coefficient would have to have that coefficient
divisible by **both** house primes to reduce to zero at both — possible only for
a primitive integral vector with a coefficient of absolute value at least
`4.6·10¹⁸`.  That is not a proof, and I withdraw the word "proved".  It is a
statement conditional on one divisibility, and B13-07 should audit it as such.

Note the consequence for B13-01: a certified element of `I(V_red) ∩ M₁₃` gives
`i_pad(13) ≥ 1`, hence `i_pad(24) ≥ 1` by monotonicity, hence `D ≤ 0` — through
the **unconditional** formula, with no ε_pad claim needed.  The review's framing
is cleaner than mine and I adopt it.

Also accepted: session 74's bracket fillings are integral polynomials, so S3 is
not the only source over `Q`.  My s85 brief overstated its uniqueness; S3's
contribution is a structured rational convention, not the only rational one.

## 5. The `n = 3` padded control is degenerate

For `det₃` the padded form is `ℓ·per₂`, with at most five essential variables, so
the seven-row cell `(19,7,2⁵)` has zero padded multiplicity by the variable-count
restriction.  The unpadded positive control does not transfer into a padded test
at that cell.  **Correction accepted**; my s87 rested on an assumption I did not
check.  It becomes a short exact control and a documented note, not a session.

## 6. Global padded/reducible equality at six variables is refuted already

`dim P₆ = 55 < 61 = dim R₆`, so the ideals differ somewhere and no global
equality theorem exists.  My S7 brief asked for one.  **Correction accepted**:
the useful question is a finite-degree equality range or a specific-family
theorem.

## What survives from my plan

The sharper transfer question, the structural-restriction route, higher-length
cubic exploration, the row builder, and the concrete pricing — the fifteen
predecessors of `λ₁₃` with their `a` and `N_S`, the builder's acceptance suite,
and the cross-checks that `rank S` must satisfy.  Those are folded into the
consolidated board at their proper scope.

Author: Swami Sethuraman, swsethuraman@beneficus.ai, Beneficus AI.
board_numbering: batch13
