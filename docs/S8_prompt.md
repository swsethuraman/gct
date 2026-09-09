# S8 — the ideal of `V_red = {ℓ·c}`, and a computable membership test

`board_numbering: batch13`.  A reasoning session with a computational
deliverable that session s85 consumes directly.

## The object

`V_red ⊂ Sym⁴C⁹` is the affine cone of reducible quartics with a linear factor:
the image of the multiplication map

    m : (C⁹)* × S³(C⁹)* → S⁴(C⁹)*,   (ℓ, c) ↦ ℓ·c.

It is classical, irreducible, `GL₉`-stable, and it contains the padded permanent
locus `V_pad = {ℓ·per₃(B)}`.  It has **no permanent in it**, which is exactly why
the programme's remaining question was moved onto it.

## What is needed, concretely

1. **The `λ`-isotypic pieces of `I(V_red)`** in the degrees the programme needs:
   at minimum `λ₁₃ = (21,17,2⁷)` in degree 13, and if it generalises, the LMR
   ladder `λ_δ = (4δ−31, 17, 2⁷)`.  Dimensions, and a description.
2. **A computable membership test.**  `F ∈ I(V_red)` iff `F∘m ≡ 0`, and `F ↦ F∘m`
   is a linear map between finite-dimensional spaces — so membership is a kernel
   computation, not a sampling question.  Give the map explicitly in coordinates
   a session can build: source `M_λ`, target the bidegree-`(δ,δ)` part of the
   polynomial ring on `(C⁹)* × S³(C⁹)*`, with its dimension and a construction.
   Use `GL₉`-equivariance to cut the target down; the naive target is enormous
   and the equivariant one should not be.
3. **A worked check** at a size a session can verify by hand or by a small
   computation: a known element of `I(V_red)` in some small `(r, δ)` that your
   test accepts, and a known non-element that it rejects.  Without both, the test
   has no teeth — the programme has already had one check this batch that passed
   by silently dropping the terms it could not place.

## Why it is worth a session

s85's whole task is: are s74's three rung-13 padded kernel directions genuine
elements of `I(V_red) ∩ M₁₃` over `Q`?  One certified element gives
`i_red(13) ≥ 1`, hence `i_pad(23) ≥ 1`, hence `D ≤ 0` at the LMR goal cell — the
first exact settlement of the cell in either direction.  Everything else about it
is a sampled ceiling.

## Context

`docs/rung13_reducible.md` (the measurement and the containment chain),
`docs/s74_final_review.md` §2 (`D = 1 − i_pad(23)`), `docs/transfer_lemma.md`.
`a₁₃ = 39`, re-derived three independent ways.

## Deliverable

The isotypic description, the map, its dimensions, the worked check in both
directions, and — if you can — the answer for the three candidates themselves.
