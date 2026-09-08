# Session 74 — the LMR source by births, then the decision

*(the reconciled proposal's s74.  Read `docs/batch12_worker_preamble.md` first.)*

## What changed under you

This was a sampling session.  It is not one any more.

S1 proved that restricting to `u = 0`, where `u = c_{(4,0,…,0)}`, realises the
ladder birth quotient exactly:

    ker( M_d --|u=0--> R/(u) ) = u M_{d−1},      M_d / u M_{d−1} ≅ ρ_d(M_d)

and `u M_{d−1}` is Lemma L's own transport, so that quotient is the space of
directions *born* at rung `d`, of dimension `b_d = a_d − a_{d−1}`.  The birth
profile is

    δ    12  13  14  15  16  17  18  19  20  21  22  23  24
    b_δ   2  37  54  52  43  31  22  14   9   5   3   1   1     (sums to 274)

So a candidate is tested for newness against a `b_d`-dimensional quotient, not
against a source climbing to 274.  Worst retained work matrix `55 × 62` at
`d = 14`; `2 × 9` at the last two rungs.

Two consequences the integrator added and checked
(`docs/batch12_s1_s2_consolidated.md` §1):

- For a prime ideal `I` with `u ∉ I` — true of `I(Det₄)` and `I(ℓ·per₃)` —
  `(I ∩ M_d) ∩ uM_{d−1} = u(I ∩ M_{d−1})`.  Hence
  **`rank T_det |_{uM₂₃} = 273 − i_det(23)`**.
- Therefore `i_det(23) = 0` gives `rank T_det = 273` on the transported `δ = 23`
  source alone, with **no `δ = 24` candidate at all**, and forces `i_det(24) = 1`.

**Careful, and this is the correction that matters:** the quotient certifies
*newness*, not ideal membership.  A filling with nonzero class spans the birth
quotient when `b_d = 1`; it is not thereby an element of any ideal.  An ideal
element of that class differs from it by a transported `u w`, `w ∈ M_{d−1}`.
Do not conflate the two anywhere in your report.

## What is already banked for you

Run `analysis/wk12_int_birth_probe.py` before you write code; it is the working
example of everything below.

- **`δ = 24` is done.**  Of s69's 113 saved fillings, 108 carry a pure-`u` letter
  and vanish identically in the birth test; of the five that do not, **filling 57
  is nonzero mod `u` at both primes, 24/24 points each**.  So
  `M₂₄ = uM₂₃ ⊕ ⟨F₅₇⟩`, and `F₅₇` is banked at
  `results/wk12_int_lmr_birth24.json`.  A nonzero residue at an integer point is
  a certificate over `Q`, not sampling.
- **`δ = 20, 21, 22, 23` are done** on fresh streams — `9/9`, `5/5`, `3/3`, `1/1`,
  in 31 s, 42 s, 32 s, 6 s respectively, single prime, seeds in
  `results/wk12_int_birth_probe.json`.  Re-derive them at the second prime as
  part of your first hour.
- **The free filter.**  A letter occupying only its `n` singleton columns makes
  `F_T = n! · u · F_deleted`, an identity, so the filling vanishes in the
  quotient.  Reject those syntactically, before any evaluation.  It removed 96%
  of the saved candidates.  It is necessary and far from sufficient — four of the
  five survivors at `δ = 24` still vanished.
- **The normalization, and it is where a silent error would live.**  Transporting
  a native degree-`d` filling to degree `D` gives
  `F_{T^up} = (n!)^{D−d} u^{D−d} F_T`.  Omitting the scalar preserves individual
  row ranks and corrupts kernel coefficients when normalized and literal rows are
  mixed.  Declare one row system and use it for the generic, determinant,
  reducible and true-padded columns alike.
- s69's checkpoints: `results/s69_lmr_state.json` (113 fillings, `113 × 300`
  generic matrix), `results/s69_ladder_n4.json` (34 saved: two native `δ = 12`,
  32 native `δ = 13`), `results/s69_n4_seed.json`.  **The 113-filling checkpoint
  and the ladder-source checkpoint are different collections; their ranks must
  not be added.**

## Tasks, in this order

1. **Pre-register**, then reproduce the four banked rungs at both primes.  If any
   disagrees, stop and report — that is a defect in what you were handed.
2. **`i_det(23)` first.**  Build the `δ = 23` source by births — rungs 13 to 23,
   `b_d` classes each — and evaluate the determinant column on it.  `i_det(23) = 0`
   finishes the determinant side at `rank T_det = 273` outright.  This is the
   cheapest path to half the answer and it comes before anything at `δ = 24`.
3. **The middle rungs are the work.**  `b_14 = 54`, `b_15 = 52`, `b_16 = 43`,
   `b_13 = 37` — 186 of the 274 directions.  Budget accordingly; the top of the
   ladder is already yours.
4. **Assemble.**  Transport each rung's births up with the correct
   `(n!)^{D−d}u^{D−d}` factors and check the assembled system's generic rank.
   Assembly, not discovery, is the risk now.
5. **Evaluate at four families on the same vectors**: `det₄` pencils, reducible
   `ℓ·c`, **true padded `ℓ·per₃`** (not `ℓ·c`), and unpadded `per₄`.  Report
   `i_det`, `i_pad`, `i_red`, `U_D`, `U_P`, `dim(U_D ∩ U_P)` and `D`.

## Success

`rank T_det = 273` and `rank T_pad = 274`, hence `D = +1`, under the
pre-registered decision table in the preamble — and the verification protocol
before it is reported anywhere.  A completed determinant half alone is a full
result.

## Stopping rules

- The span stalls below 274: report the rank curve, the per-rung birth counts
  reached, the missing directions, and the four columns **on the span reached**.
  A rank on a proper subspace is a lower bound on `mult`, which is the useful
  direction.
- A rung's birth rank will not fill within budget: report which rung, how many
  draws, how many passed the filter, and the observed hit rate.  Do not enlarge
  the stream automatically.
- Any `D > 0`: the verification protocol takes over.

## Deliverables

`results/PREREG_s74.md`; per-rung birth bases with their nonzero minors and the
points used; the assembled source with its declared row system; the four
evaluation columns; `sparse_nullity` certificates in the session-67 spelling;
`docs/s74_report.md`.
