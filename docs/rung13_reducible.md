# The rung-13 relations are reducible relations

**The finding.**  Session 74's three padded kernel directions at rung 13 vanish
on **every** `ℓ · cubic`, not only on `ℓ · per₃`.  The padded kernel and the
reducible kernel at rung 13 are the **same three-dimensional space**, at both
house primes.  The permanent is not involved in them.

`analysis/wk12_int_rung13_kernels.py`, my own points, my own evaluator (the s69
circuit, not s74's compact DP), 43 usable reducible points:

| | P1 | P2 |
|---|---|---|
| generic rank at rung 13 (the control) | **39 / 39** | **39 / 39** |
| padded rank at rung 13 (s74's data, my elimination) | 36 / 39 | 36 / 39 |
| padded rank at rung 13, my own independent stream | 36 / 39 | 36 / 39 |
| **reducible** rank at rung 13, `ℓ · generic cubic` | **36 / 39** | **36 / 39** |
| s74's three padded relations escaping on a reducible point | **0 of 3** | **0 of 3** |
| the two kernels are the same space | **yes** | **yes** |

The generic control is what makes the rest readable: 39 of 39 says the 39 source
rows are independent and the evaluator is sound, so a stall at 36 is a property
of the locus and not of the instrument.  The padded stall was reproduced on a
point stream with a different seed, a different coefficient bound and a
different evaluator from s74's, and held for 40 consecutive points past
saturation; two reducible draws and one padded draw were discarded for
`msym_u = 0`, which is the hazard the transport note names and the reason the
guard is there.

## Why this changes the remaining work

`V_pad = {ℓ·per₃(B)} ⊆ V_red = {ℓ·C}`, so `I(red) ⊆ I(pad)` and
`i_red ≤ i_pad` at every rung.  Three things follow.

**1. The remaining question has no permanent in it.**  `V_red` is the image of
the multiplication map `(C⁹)* × S³(C⁹)* → S⁴(C⁹)*` — a classical variety of
reducible quartics.  Deciding whether a given `λ₁₃` highest-weight vector lies in
`I(V_red)` is a finite exact linear-algebra question: `F ∈ I(V_red)` iff `F` is
in the kernel of the pullback along that map, and the pullback is a linear map
between finite-dimensional spaces.  No sampling, no per₃, no orbit closure.

**2. One proved relation settles the cell.**  `i_red(13) ≥ 1` gives
`i_pad(13) ≥ 1`; `i_pad` is nondecreasing along the ladder, so `i_pad(23) ≥ 1`;
and `D = 1 − i_pad(23)` (`docs/s74_checkpoint_review.md` §4) then gives
**`D ≤ 0`** — the LMR cell settled against a multiplicity obstruction, by a route
with no sampling anywhere in it.

**3. The screen pre-registered in batch 11 is pointed at exactly this.**
`docs/batch11_plan.md` C3: `mult_pad ≤ mult_red = rank S`, so `rank S < a` gives
`i_pad ≥ 1` and `D ≤ 0` with no padded points at all.  `S` is the
reducible-normalisation split, `274 × 521` at rung 24 and much smaller at
rung 13.  It has never been run for want of a source; s74 supplied the source,
and this measurement says what it will find.  **Run it at rung 13 first.**

## What is and is not established

- `i_red(13) ≤ 3` and `i_pad(13) ≤ 3` are **certified** — a nonzero 36×36 minor
  is a rank floor, and the floor caps the nullity.
- `i_red(13) ≥ 1` is **not established**.  A stalled sampled rank is a ceiling,
  and a ceiling never proves a relation exists.  That is the whole remaining
  content, and §1 above says where to get it.
- The kernels coinciding is a statement about the **sampled** kernels.  Both are
  three-dimensional and equal at both primes over 43 reducible and 76 padded
  points; the true ideal intersections sit inside them, so
  `I(red) ∩ M₁₃ ⊆ I(pad) ∩ M₁₃ ⊆` that same 3-space, which is a genuine
  containment and is all the argument needs.

## Cost note

The rung-13 question is 39 rows and about 0.2 s per row per point on the
repository's own evaluator — roughly 16 s a point for both primes, or 33 s with
the reducible and generic families run together.  The whole measurement above
took 21 minutes.  The rung-24 equivalent is 274 rows and s74 spent 2688 s on one
column.  **Everything the padded question still needs can be asked at rung 13.**

Author: Swami Sethuraman, swsethuraman@beneficus.ai, Beneficus AI.
board_numbering: batch12
