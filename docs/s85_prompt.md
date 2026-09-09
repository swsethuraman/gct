# s85 — the three rung-13 relations over `Q`

`board_numbering: batch13`.  Read `docs/batch13_worker_preamble.md` first.

## Mission

One certified element of `I(V_red) ∩ M₁₃` over `Q` settles the LMR cell against a
multiplicity obstruction, with no sampling anywhere in the chain.

## The chain, and why one element is enough

`V_pad = {ℓ·per₃(B)} ⊆ V_red = {ℓ·c}`, so `I(red) ⊆ I(pad)` and `i_red ≤ i_pad`
at every rung.  `i_pad` is nondecreasing along the ladder
(`u·(I ∩ M_{d−1}) ⊆ I ∩ M_d` and `u` is a nonzerodivisor).  And
`D = 1 − i_pad(23)` is proved.  So

    i_red(13) ≥ 1  ⟹  i_pad(13) ≥ 1  ⟹  i_pad(23) ≥ 1  ⟹  D ≤ 0.

## What is measured going in, and what it is worth

The integrator measured, on its own point stream, its own bound and the
repository's s69 evaluator rather than s74's compact DP
(`docs/rung13_reducible.md`):

| | P1 | P2 |
|---|---|---|
| generic rank at rung 13 — the control | 39/39 | 39/39 |
| padded rank, s74's data | 36/39 | 36/39 |
| padded rank, an independent stream, held 40 points past saturation | 36/39 | 36/39 |
| **reducible** rank, `ℓ · generic cubic`, 43 points | **36/39** | **36/39** |
| s74's three padded relations escaping at a reducible point | **0 of 3** | **0 of 3** |
| the two kernels are the same space | **yes** | **yes** |

Every line of that is a **sampled ceiling**.  It says the three relations are
reducible relations if they are relations at all.  It does not say they are.

## The instrument

Session S3's rung-13 source is **rational** by a specified convention — "this
defines actual rational vectors", not reconstruction from residues — and it is
the only place in the programme where rung 13 exists over `Q`
(`results/astra/S3/`, and S3's continuation report).  Its 39 vectors and s74's
39 rung-13 rows span the same `M₁₃` (`a₁₃ = 39`, re-derived three ways), so the
three candidates can be written exactly in S3's basis.

Membership: `F ∈ I(V_red)` iff `F` is in the kernel of the pullback along the
multiplication map `(C⁹)* × S³(C⁹)* → S⁴(C⁹)*` — a linear map between
finite-dimensional spaces.  **Session S8 is producing a computable test for
exactly this**; consume it if it has landed, and otherwise build the pullback
yourself and say so.

## Task

1. Write s74's three rung-13 padded kernel directions exactly in S3's rational
   basis.  Verify the change of basis: the transported images must agree with
   s74's mod-`p` kernel at both primes.
2. Decide membership in `I(V_red)` for each, over `Q`.
3. If one is a member: `i_red(13) ≥ 1`, hence `D ≤ 0`.  The verification
   protocol applies before it is reported anywhere.
4. If none is: `i_red(13) = 0`, the sampled 36 was an artefact of the point
   family, and the whole padded ladder — including the 5 at rung 24 — has to be
   redone.  Say so loudly; it is the more surprising outcome and the more
   consequential.

## Falsifiers

- The change of basis not reproducing s74's kernel at both primes → stop.
- The generic rank at rung 13 coming out below 39 on any instrument → stop; the
  39 rows are independent and a smaller generic rank is an evaluator fault.
- A membership verdict that disagrees between the two routes (S8's test and your
  own pullback) → recorded, both exhibited, no verdict.

## Deliverables

`results/PREREG_s85.md`; the three candidates in S3's rational basis with the
change-of-basis check; the membership verdicts with their certificates;
`docs/s85_report.md`; bundle + `.md5`.
