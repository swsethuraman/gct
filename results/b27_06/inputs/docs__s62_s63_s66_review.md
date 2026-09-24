# Integrator review — sessions 62, 63 and 66

All three bundles: md5 matches, ancestry against `226b4ef1` passes.
s62 13 commits / 79 files, s63 4 / 20, s66 7 / 227.  All three merged.

## Session 62 (C1) — accepted; its proved control is the batch's best calibration

**Verified here independently — the `n = 2` control.**  This is the strongest
thing in the session because both sides are theorems, not measurements.
`det_2(M(s)) = m₁₁m₂₂ − m₁₂m₂₁` lies in the span of four linear forms, so its
symmetric matrix has rank ≤ 4 and the `(2^δ)` highest-weight vector — the
`δ × δ` discriminant — must vanish identically from `δ = 5`.  Reproduced here
from scratch, two seeds × two primes:

    a((2^d), d) = 1  at d = 3,4,5,6                     (plethysm, independent)
    d = 3, 4 : discriminant nonzero at all four runs    FULL RANK
    d = 5, 6 : discriminant = 0 at all four runs        DROP, identically

**The Gram/Schur machinery is shown to return a rank drop exactly where a
theorem forces one and full rank exactly where a theorem forbids one.**  The
record had no such end-to-end validation before.

**The centrality falsifier is answered.**  `β_4` is **not** central: at every one
of the five multiplicity-2 cells `G_λ` is not proportional to the standard inner
product.  The cheapest instance is `(12,4)` — the one I nominated in
`docs/s62_s63_integrator_note1.md` §4, and it does double duty as a
Proposition S stable-boundary check.  The `δ = 4` commutant is
`23·(1×1) ⊕ 5·(2×2)`, dimension 43, confirming the bookkeeping again.

**A correction to me, and it is a large one.**  My note 3 withdrew note 2's
"both walls are measured, stop" on the grounds that the support exponent was
still falling and three points could not carry the extrapolation.  **The
sessions now measure the answer and note 2 was right.**  The density does not
keep falling: s62 finds `|S| = n_λ` at **11 of 28** `δ = 4` cells (the
rectangular and near-rectangular ones — the highest-weight vectors reach the
whole weight space), and s63 finds a plateau at `0.20–0.26` of `n_χ` that cannot
fall to zero.  My fitted `|S| ≈ 10⁵` was low by one and a half to two orders
against `n_χ`, and the withdrawal was premature.  Recorded.

**One discrepancy between the two reports that must not propagate.**  s62 quotes
`|S| ~ n_λ ~ 10¹¹`; s63 quotes `|S| ≥ 6×10⁶`.  These are **the same measurement
against different bases** — s62's `n_λ` is the raw weight space `N_S =
1.56×10¹¹`, s63's is the stabiliser-reduced `n_χ = 3.10×10⁷`, and `5040 ·
6×10⁶ ≈ 3×10¹⁰` reconciles them to within the plateau's width.  s62 explicitly
says it separated the three scales after an adversarial review; s63 does not
restate the basis.  **Any future citation of `|S|` must name its basis.**

## Session 63 (C2) — accepted; the wall is quantified and the control is two-sided

**The foundation is reproduced three ways** — `a₂₃ = 273`, `a₂₄ = 274` by a
from-scratch Weyl alternation, anchored to the plethysm *definition* at ten
cells and cross-checked against `a_weyl`.  Its `K_exact` also reproduces `N_S`
at `δ = 23` (156 419 279 221) and `δ = 24` (156 438 903 314) — matching the
table I computed in `docs/s63_integrator_note2.md` §1 exactly, by a different
engine.  The full ladder matches s57/s58.

**The two-sided control came back exactly as predicted.**  Note 2 §4 asked for
`δ = 9, 10, 11` and predicted full rank at all three with a drop only at 12.
Measured, both primes: `mult_det = 2, 4, 5` (full) and `5 < 6` at `δ = 12`.
**The instrument does not under-report rank; the drop is genuine.**  And
`δ = 11` delivers the predecessor argument in miniature — full rank at the
predecessor plus ladder monotonicity plus LMR pins `i_det(12) = 1`, which is the
273/274 deduction validated end to end before it is trusted at `n = 4`.

**The honesty about the exhibited vector is exactly right and should be kept.**
s62 states that the finite-point vanishing of `U_D` is Schwartz–Zippel evidence
of ideal membership, **not a proof of it**; the rigorous `i_det ≥ 1` remains the
LMR theorem.  That is the correct standard and the phrase "first exhibited
element of `I(D)^{HWV}`" should always travel with it.

**The wall, in three routes:** native HWV build 14.4 TB / ≈ 415 days; Foulkes
column `|H_{4,24}| = 1.2×10⁹³`; Gram/Schur `|S| ≥ 6×10⁶`.  Reported rather than
forced past the time-box, as the stopping rule required.

## Session 66 (C5) — accepted; the largest single delivery of the batch

**It reproduces my own audit exactly as calibration** before anything new:
`c21 ∩ c32` → `16 / 64 / 57 / 57 / 50 / 64 / 0` and `ker ∩ coker` →
`5 / 75 / 63 / 63 / 75 / 0`, matching `docs/rees_boundary_audit.md` term for
term, and s59's order-1 row `29, 29, 28, 28, 24`.

**Two corrections to the record that I should have caught and did not.**

1. **A missing component.**  The `k = 3` stratum — the semi-primitive type
   `SP = {[φN(x) | c]}`, 49-dimensional, in no compression space — was absent
   from the five strata s54 and s59 used, and therefore absent from my audit's
   framing.  It is measured here at every order.
2. **`P ∩ ker` is not a rank-3 incidence.**  A primitive pencil with a common
   kernel has rank ≤ 2, so `dΦ ≡ 0` there and "transverse quotient" is void.
   That locus is the padded `3×3` skew type — **the genuine `n = 4` analogue of
   the Hüttenhain–Lairez component that motivated the whole primitive track** —
   and it needed its own treatment, which it gets (four explicit components from
   a UFD factorisation; images `28, 28, 26, 26`).

**The contact-order lemma (§4) is the session's best result and it is proved.**
At a smooth point of `V(J)` the exceptional fibre is `P(im dΦ)` at every contact
order.  That turns s59's measured "invariance of contact order" into a theorem
*and* localises any hidden component of the exceptional divisor to `Sing V(J)` —
the incidences and the rank-≤2 loci — which is exactly the locus the session
then measured.  It is the statement that makes the enumeration in §6 an argument
rather than a survey.

**Every reducible image is `≤ 29 < 31`, far from 35**, at orders 1, 2 and 3, at
every listed incidence, both primes, two seeds, with every spanning vector
checked to annihilate `dΦ` before being counted.

**The honest boundary is properly drawn.**  `P ∩ c21` at order 2 did not finish;
orders `≥ 4`; the rank-drop strata at `ker ∩ coker`; deeper rank-2 strata.  Each
is a proper closed subset of a measured locus, and the session says plainly that
none of this proves `R_5 ⊄ D_5` — that still needs the upper bound, and nothing
here changes what that object is.  The bilinear reduction (§5) is the
engineering result worth carrying: `minAssGTZ` finishes in seconds after
dropping the intersection coordinates and does not finish at all before.

**One finding for the single-writer files**, which I will place: the base scheme
of `Φ` at `r = 5` is generically reduced along every component and **non-reduced
along every pairwise incidence** (`dim Q_2 = 12 < 16` at `P∩SP`, `25 < 49` at
`c21∩c32`, `59 < 144` at `ker∩coker`).  That is the precise sense in which the
normal cone of `J` differs from that of the reduced base locus, and it is why
the exceptional fibre over an incidence exceeds `P(im dΦ)`.

## Standing note

Sessions 62 and 66 both record that `docs/batch10_plan.md` and
`docs/batch10_worker_preamble.md` were not in the tree they cloned.  They were
committed here but the merge had not reached the public repository when those
sessions started.  Both worked from the brief and both folded the integrator
notes in correctly, so nothing was lost — but the ordering should be fixed for
batch 11: **push the plan and preamble before the briefs go out.**
