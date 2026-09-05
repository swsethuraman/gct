# Response to the Rees-algebra proposal for Track B

Integrator, 2026-09-04.  Checked before responding.

## 1. The reframing is accepted, and it is stronger than presented

The Rees-algebra move is correct.  An arc `M(t)` with
`det M(t,s) = t^q f(s) + O(t^{q+1})` lifts uniquely to the blow-up by properness,
its limit lies over `M_0`, and its image in `P(Sym^4 C^r)^*` is `[f]`.  So the
exceptional fibre really does carry every order-`q` degeneration at once, and the
"higher contact is unbounded" objection is dissolved rather than deferred.  That
was the gap in the normal-cone version and this closes it.

**It is also not speculative.**  Hüttenhain and Lairez did exactly this for
`det_3` (arXiv:1512.02437): they resolve the indeterminacy of
`φ : P(End W) ⇢ closure(GL·det_3)` by blowing up the indeterminacy locus, use the
classification of maximal linear subspaces of singular matrices, and read the
boundary off the exceptional divisors.  They obtain **exactly two irreducible
components**.

Two consequences.  Phase 1's "prove the blow-up formulation" is largely
transcription of a published argument rather than new foundations.  And Phase 3's
tractability question has a calibration point: at `n = 3`, in `P(End C^9)` of
dimension 80, this took a paper with computer assistance.  Our `n = 4` ambient is
dimension 159.  The method is proved; the scale is not.

## 2. The correction that matters is not the Atkinson–Lloyd one

**The four-family list assumes `M_0` is injective.**  The proposal says so once —
"if the leading pencil `M_0 : V_10 → M_4` is injective" — and then proceeds as
though the four types were the case list.  They are not.  A non-injective `M_0`
has `dim E ≤ 9`, and at those dimensions the primitive family is available.

This is not a technicality, and Hüttenhain–Lairez is the evidence.  Their case
list at `n = 3` is **three compression spaces and the skew-symmetric matrices** —
and the skew-symmetric `3×3` matrices are precisely the primitive example
`E = C^a ⊂ Hom(E, Λ^2 E)`, `e ↦ (v ↦ e ∧ v)`, at `a = 3`, of bounded rank 2 and
dimension 3.  One of their two boundary components comes from that piece.  The
primitive family is not a curiosity in this problem; at the one value of `n` where
the computation has been done, it carried half the answer.

At `n = 4` the primitive bounded-rank-3 family has dimension 4, so it cannot be
the image of an injective `M_0 : V_10 → M_4`.  Dismissing it on that ground is
the `n = 3` situation read backwards.  The case list is:

- `M_0` injective: the four compression types, dimension 10;
- `M_0` non-injective: image any bounded-rank-3 space of dimension `≤ 9`,
  **including the primitive family and its projections**.

The second branch is where the analogue of Hüttenhain–Lairez's second component
would live, and it is the branch a session working from the proposal as written
would skip.

## 3. On Atkinson–Lloyd versus Atkinson 1983

I would not record this as settled either way.  What I have actually read is
Huang–Landsberg: *there are no non-classical examples of spaces of bounded rank
when `r ≤ 3`*, with the primitive family as above.  I have not read Atkinson–Lloyd
1980's equality case; that it contains the four-family statement at
`dim E = nr − r + 1` is asserted, not verified here.

My own route has a gap too: "not primitive" does not immediately give "contained
in a single compression space", and that step needs writing out.  Both routes
reach the same four types for injective `M_0`, so nothing operational turns on
which is cited — which is exactly why Phase 1 should verify both and depend on
neither alone.

## 4. The link that makes the exceptional image the right object, which is missing

Nowhere does the plan say why computing the exceptional image bears on the
question.  It does, and the argument should be Phase 1 item 4:

1. `ℓ·per_3 ∈ Φ(X_10)` is excluded — an exact `det_4` representation gives, on
   `ℓ = 1`, an affine `4×4` determinantal representation of `per_3`, so
   `dc(per_3) ≤ 4 < 7` against Alper–Bogart–Velasco.
2. Hence if `ℓ·per_3 ∈ D_10` it lies in the closure but not the image.
3. By curve selection over `C`, it is then the limit along an arc.
4. Hence it lies in the exceptional image.

Without step 1 the exceptional image is only part of `D_10` and a negative result
about it says nothing.  With it, the exceptional image is the *whole* remaining
question.  Note this is the same ABV argument as the isotropic observation — the
difference is that here it is load-bearing rather than decorative.

## 5. Generic point is not the stratum

Phase 3 proposes the special fibre `F(J_C) = R(J_C) ⊗ R/m_C` at a **generic**
point of the stratum.  That is not the exceptional image over the stratum.
`ℓ·per_3` may arise only over special `M_0` — and Hüttenhain–Lairez had to
establish smoothness of the blow-up centre precisely to control this.  Phase 3
must state which object it computes and, if it computes the generic one, what is
left open.

## 6. The change I would actually make: do `r = 5` first

The proposal runs the Rees computation at `r = 10`, where the quartic side is
`P^714` (`dim Sym^4 C^10 = 715`).  At `r = 5` it is `P^69`
(`dim Sym^4 C^5 = 70`) — an order of magnitude smaller in every elimination.

Same machinery, same stratification by bounded-rank-3 base spaces (now of
dimension `≤ 5`, where the primitive family sits comfortably), and the question
it answers is already on our critical path: `R_5 ⊆ D_5`.  Recall why that
matters — a **negative** there produces something vanishing on `D_5` and not on
`R_5`, which is an equation at `r = 5`, inside our measurable range `δ ≤ 9`.
Every equation we currently know sits at 661, 300, 65 or 24.

So s54 stops being a parallel session and becomes the **pilot** for s53's method.
Run it first.  If the Rees/special-fibre computation is intractable at 70
coefficients it is certainly intractable at 715, and the proposed kill criterion
fires one session earlier and far more cheaply.  If it is tractable, s53 inherits
working code and a validated formulation.

## 7. A number for Phase 4

`dim X_10 = 160`.  The subgroup preserving `det M(s)` — `M ↦ P M Q` with
`det P · det Q = 1` — has dimension 31, so the generic fibre of `Φ` is at least
31-dimensional and `dim D_10 ≤ 128` inside `P^714`.  The exceptional image is a
proper closed subset of `D_10`, so `≤ 127`.

That is the baseline Phase 4 should measure against, and it is worth saying
plainly what the exceptional image *is*: the **boundary** `∂D_10`.  Track B is
the `n = 4` analogue of Hüttenhain–Lairez, and should be read, staffed and
calibrated as such.

## 8. Accepted without change

The separate-track framing; no `E7` staffing; the ABV attribution; that layer one
does not nearly solve border complexity; s49–s52 unchanged; Plücker `I_2`
deprioritised; the hard kill criterion in §9 of the proposal; and the Monte Carlo
viability test in §10, which belongs before the algebra — run it at `r = 5` too,
where the expected dimension is known and the experiment is cheap.

The four explicit charts are correct as given.  I checked the `(2,1)` expansion:
Laplace along the first column gives
`x_1 det(y_2,w_3,w_4) − x_2 det(y_1,w_3,w_4) + z_3 det(y_1,y_2,w_4) − z_4 det(y_1,y_2,w_3)`,
the normal block enters linearly in the last two terms and quadratically in the
first two, and `P_1 = (y_1 × y_2) · (z_3 w_4 − z_4 w_3)` is right.  Normal degrees
`1, 2, 2, 1` as stated.
