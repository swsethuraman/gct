# Integrator assessment — the external slot-6 algebraisation session

**Verdict agreed: park it.**  The conclusion matches session 61's own §6 and the
carry-forward in `docs/s61_review.md` §8, and the session reaches it by a better
route than s61's — it names the mechanism rather than only estimating a degree.
Two corrections, one of which invalidates its closing recommendation.

## 1. Where it improves on session 61

s61 §6 said "unknown, and no route to anything near LMR's 24 is visible", with a
resultant-degree estimate (`3^8 = 6561`) as the only quantitative anchor.  This
session supplies the reason, and it is the right one:

> dual defect is locally determinantal; dual **degree** is enumerative.

A rank condition on the Hessian is what makes LMR's degree-24 module possible; a
polar degree is the degree of a **saturated** conormal cycle, and saturation is
what destroys every cheap presentation.  That is a real conceptual gain and it
should be recorded whether or not the branch is ever revisited.

The `21×21` Fitting-minor route is the only construction anyone has produced
that would land below 24, and its failure is correctly diagnosed: the
coefficient-linear Macaulay matrix computes the *unsaturated* length, which on a
hypersurface as singular as `det_4` counts points supported on the Jacobian base
scheme, excess intersection and embedded components.  Session 61 measured
exactly that inflation at the cells in question — the `P^4`-section of `det_4`
has 20 nodes correcting `4·27 = 108` down to 68, and the `P^5`-section has a
degree-20 curve of `A_1` points correcting `4·81 = 324` down to 84.  **Those
corrections are 37 % and 74 % of the naive count**, at the exact object of
interest, which is direct evidence against the "unexpected cancellation" the
session's proposed toy experiment would look for.  If the branch is ever
revisited, that experiment can start from s61's numbers rather than from a new
toy.

## 2. Correction — the programme already holds the witness §4 asks for

§4 says that knowing `dim X_f^∨ ≤ 6` does not bound `deg X_f^∨` by 20, and
treats the point as a general principle with no explicit example.  There is one,
it is a quartic in `P^15`, and it is already in the record: **the cone over a
smooth quartic of `P^7`**.  Its dual has dimension 6, so `δ_7 = 0` — it is
dual-defective in exactly LMR's sense — while `δ_6 = 4·3^6 = 2916`, since a
smooth hypersurface has `δ_k = d(d−1)^k` and the cone lemma transports slots
`k ≤ 6` unchanged.  I verified the smooth-quartic profile directly
(`4, 12, 36, 108` at slots 0–3, `= 4·3^k`) during the s61 review, and the same
cone is s61 §5's second incomparability witness, which stands.

So the statement is not merely unsupported by a general principle — it is
**explicitly false, with a witness inside the representation the programme cares
about, exceeding the bound by a factor of 146**.  Worth using: it is a sharper
way to say why slot 6 carries information the dual-defect condition does not.

## 3. Correction — the closing recommendation rests on a number that is zero

The session ends by naming two fertile directions, the second being *"the
four-transverse-direction special normal-cone problem at `r = 5`"*.

**That four is zero.**  `docs/rees_boundary_audit.md` records the measurement: at
a generic point of `C_{21} ∩ C_{32}` the tangent spaces of the two compression
components are 57-dimensional each (not 50 — the omitted 7 is the flag motion in
`Gr(2,4) × Gr(1,4)`), they span the full 64-dimensional `ker dΦ`, and the
transverse quotient is 0.  The same holds at a generic point of `C_{21}` alone
(`ker = TC_{21} = 57`) and at `ker ∩ coker` (`ker = 75 = dim(T(ker) + T(coker))`).
Every spanning vector was checked to annihilate `dΦ`.

So there is no four-dimensional transverse quadratic problem to carry into a
session.  The compression world has produced **no** exotic first-order direction
at any incidence tested.  What survives, and what the Rees audit itself ranked
third, is the right target: **the primitive family and its incidences** — the
analogue of the `n = 3` skew-symmetric component that Hüttenhain–Lairez show
compression analysis misses, and the only base-locus type at `r = 5` where
nobody has yet looked for a transverse direction.

## 4. Where that leaves the two fertile directions

1. **`Θ⁺` rank / determinant kernel birth** — agreed, and it now has three
   concrete first steps in cost order: the `6 × 10` positive control at the
   `n = 3` LMR cell (`docs/lmr_cell.md` §3b), which must return rank ≤ 5 and is
   the first rank-drop the engine would ever have been shown; the `δ = 23` LMR
   predecessor `C^273 → C^{48825}`, which pins `i_det = 1` at the LMR cell if it
   is full rank (§3a); and the LMR cell itself.
2. **The `r = 5` normal cone** — re-scoped from the compression incidences to the
   primitive family, per §3 above.

Both stand.  The slot-6 branch stays banked as geometry: two independent
conormal certificates that `x_0·per_3 ∉ closure(GL_16·det_4)`, no stronger
bound, and now a named reason why it does not algebraise cheaply.
