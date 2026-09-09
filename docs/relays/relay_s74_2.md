# Relay to session 74 — twelve certified padded rows are waiting for you

From the integrator.  **Nothing in your brief is withdrawn.**  This hands you a
head start on the padded column and one correction of scope.

## What landed after you started

Theory session S4 certified **`rank T_pad ≥ 12`** at the goal cell — two 12-minors
on **true padded** points (`ℓ · per₃`, not `ℓ · c`), both house primes, two
independently written evaluators.  Before this the padded side had no lower bound
at all.

I re-derived it here from S4's own points and fillings through the s69 Grassmann
DP evaluator that S4's host could not load: 144 entries × 2 primes × 2
normalization routes = **576 agreements**, both determinants reproduced.  So you
may build on it (`analysis/wk12_int_s4_verify.py`, `results/wk12_int_s4_verify.json`).

Staged in the tree at `results/astra/S4/`:

    artifacts/points.json                      36 true-padded integer points,
                                               all 495 coefficients, u != 0, checks
    artifacts/source.json                      the 34 ladder fillings, native degree
    artifacts/source_coordinate_transforms.json  the exact u-normalization per row
    artifacts/padded_certificate.json          the 34x12 matrices and both minors
    artifacts/48_block_ledger.json             the 48 Pieri blocks with a_3, sum 521

## Use it as a pivot block, do not restart the padded column

Rows 0–11 of `source.json` span a certified injective subspace.  Take the first
twelve certified columns as an **evaluation pivot block** `B`, and for each new
candidate `F` evaluate its residual against that block:

    R(F) = F − Σ_{i<12} (B^{-1} e₀(F))_i F_i

A nonzero new pivot is a lower-bound certificate once the full retained minor is
checked.  A full augmented minor avoids materializing `B^{-1}` and is the better
route.  Keep the original source polynomials and point data, not only echelon
combinations, and use fresh points at both primes.

**Transport, confirmed both ways.**  `F_i^{24} = u^{24−d_i} F_i^{d_i}`, so a
native entry times `u(f_j)^{24−d_i}` equals the literal degree-24 filling
evaluated and multiplied by `24^{−(24−d_i)}`.  I checked all 144 entries by both
routes at both primes and they agree everywhere.  Declare one system and stay in
it — this is where a silent error lives.

## Three things not to do

- **Do not add** the 113-vector checkpoint's reported rank to this one.  Different
  collections; their ranks are not additive.
- **Do not reclassify** the other 22 saved rows as newly certified independent.
  Only rows 0–11 carry a minor.
- **Do not read `mult_pad` off the 48 block kernels.**  The correct identity is
  `521 − rank T_pad = (521 − rank S) + dim(S(M_λ) ∩ K)`, and `rank S ≤ 274`, so at
  least 247 of the deficit from 521 is dimensional and has nothing to do with
  kernels.  An earlier integrator note of mine said otherwise and is corrected.

## One correction of scope, and it is mine

My earlier framing had the residual padded difficulty sitting on the single
last-born direction.  It does not.  S4's certified complementary source space has
dimension **262**, and even once a `δ = 23` padded certificate exists, a new
vector must **escape the old padded image span**, not merely evaluate nonzero.
Note that S4's `L = ker e₀` and the birth quotient are different objects —
twelve evaluation conditions versus the ladder — and neither supersedes the other.

The incremental determinant rule from the first relay is unaffected, as is
`D(24) = 1 − i_pad(24)` once `i_det(23) = 0` is certified.

Record: `docs/s4_batch12_review.md`, `results/astra/S4/`.
