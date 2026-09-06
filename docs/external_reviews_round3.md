# The five overnight reviews — assessment

Integrator. Checkable claims re-derived before writing.

## Scorecard

| session | their verdict | mine | reason |
|---|---|---|---|
| low-multiplicity (`a=1`) | KEEP, upgrade | **DEAD** | its headline cell was measured by s52 and died; I now show why structurally |
| moment polytopes | KILL facets, KEEP holes | **KILL both** | the hole search has run exhaustively since s38, with the *symmetric* coefficient |
| symmetry-restricted | KILL | **KILL — agreed, cleanly** | explicit counterexample verified |
| conormal border | KEEP narrowly | **KEEP, one bounded run** | right direction; one genuinely open sub-question |
| quiver / Foulkes | KEEP narrowly | **KEEP — the best of the five** | a new engine for the quantity we cannot compute |

## 1. The two multiplicity-side sessions collapse into each other, and both die

The low-multiplicity session and the moment-polytope session converge on the
same dream cell: `a(λ,δ) = 1`, `m_pad > 0`, and the determinant side empty.
Both name `(30,2^5)` at `δ = 10`.

**s52 already measured that cell.** `mult_det = mult_pad = mult_red = 1 = a`, so
`i_det = 0` and `D = 0`. Twelve more `δ = 10` `a = 1` cells with it. Dead.

The moment session's sharper proposal — find `sk(λ, 4×δ) = 0` with `m_pad > 0`,
which gives `D = 1` with no HWV evaluation at all — is correct logic
(`mult_det ≤ sk`, so `sk = 0` forces `mult_det = 0`). Two problems:

**It is not new.** `results/occurrence_screen.md` has used the **symmetric**
rectangular Kronecker coefficient since session 38 — not the ordinary `g`, which
is the gap the session hoped to exploit. That screen is exhaustive over
`δ = 5..10` at `ℓ = 5`: **2585 cells, zero fires.**

**And it fails at their own cells.** I computed `sk` directly (calibrating first
against s38's ℓ=5 peaked family, reproducing `sk = 8` at every degree):

| cell | `a` | `sk` |
|---|---|---|
| `(30,2^5)/10` | 1 | **13** |
| `(29,4,2,2,2,1)/10` | 1 | **78** |
| `(29,3,2,2,2,2)/10` | 1 | **30** |

Every one positive, every one far above `a`. And s38's reading explains why in
general: **`sk` dominates `a` everywhere and the gap widens fast** — at `δ = 10`
the largest-`a` cell is `a = 1421` against `sk = 389644`. The tightest family
never closes; its margin is 7 at every degree.

So the finite-hole route is not merely unproductive, it is running away from us:
the quantity that must reach zero grows while `a` stays at 1. **The `a = 1`
direction is now closed from three sides** — measured (s52), screened (s38), and
structural (the margin widens).

The one item worth keeping from the low-multiplicity session is `a = 274`, which
matches my own computation exactly and corrects s50 §2.

## 2. Symmetry — a clean kill, and I verified the counterexample

`det diag(x, x, y+sx, y−sx) = x²(y² − s²x²)`, which at `s = 0` becomes `x²y²` —
invariant under `(x,y) ↦ (tx, y/t)`. Verified symbolically. **A fixed-size
determinant pencil with finite symmetry degenerates to a limit with a torus.**
So symmetry cannot be transported backward through a degeneration, and the
Landsberg–Ressayre `n ≥ 2^m − 1 = 7` half-equivariant bound cannot be promoted
to a border bound.

The stabilizer-dimension test is worse than useless here, and I confirmed the
count: the padded point in 16 variables has projective stabilizer dimension
`6 + 36 + 60 = 102` against `dim G_{det_4} = 31`. Semicontinuity requires
`102 ≥ 31` — satisfied with **slack 71**. No obstruction, by a wide margin.

This is the correct kind of session: it closes a tempting route with a
two-line counterexample rather than a survey.

## 3. Conormal — the right direction, but it lands on LMR again

This session independently reconstructs the taxonomy from my batch assessment
and reaches the same table: singular-locus dimension, Milnor numbers, raw Betti
numbers all KILL (wrong direction); dual dimension and conormal multidegrees
KEEP (right direction). Independent arrival at the same organising fact.

Its determinant conormal sequence `(4, 12, 36, 68, 84, 60, 20)` has both
endpoints right — `δ_0 = deg det_4 = 4`, `δ_6 = deg(P³×P³) = C(6,3) = 20` — and
`δ_7 = 0` because the dual has dimension 6. The padded permanent has
`δ_7 > 0` because its dual has dimension 7. That separates.

**But that is exactly LMR again**, as the session says plainly: `δ_7 > 0 ⟺
dim X^∨ ≥ 7`, and the complementary closed condition is the dual-defect locus
whose equations are LMR's degree-24 module. No new separator, and no route to a
lower degree.

**Caveat carried forward:** this rests on a June 2026 Sheshadri preprint I have
now failed to locate in four searches across two sessions. The session claims to
have read the body. Its *conclusion* does not depend on the citation — the `δ_7`
separation is LMR's, independently established — so nothing propagates. But the
specialization theorem itself remains unverified here, and no session should
build on it until someone produces the arXiv number.

**Correction (session 61, confirmed by the integrator).** The preprints exist:
`arXiv:2606.13628` and `arXiv:2606.15970`, both Karthik Sheshadri. Every one of
my searches used `arxiv.org/abs/<id>`, which returns an empty document through
the fetch tool; `arxiv.org/html/<id>` and the search index resolve normally. The
title, abstract, Lemma 15 and Theorem 3 of the first were read here directly.
**The failure was mine and it was a tooling false negative, not a missing
paper.** For future citation checks: an empty `abs` page proves nothing — try
`html` before concluding the identifier is invalid. The rule below — that no
session's mathematics may depend on an unread citation — was right and stands;
session 61 followed it and proves the one statement it needs (`docs/s61_review.md`
§4).

**The one thing worth running:** the full polar profile `(δ_0..δ_7)` of `per_3`,
compared componentwise against `(4,12,36,68,84,60,20)`. If some slot `k ≤ 6`
violates the determinant bound, there is a conormal inequality independent of
dual defect, which might algebraize differently from degree 24. If every lower
slot is fine and only `δ_7` differs, then conormal geometry has told us the
whole microlocal signal at `(3,4)` collapses to LMR — and we park the branch
knowing why. Either answer is worth one bounded session. This is the only
concrete new computation in the five.

**Answered (session 61, verified by the integrator).** Slot 6 violates:
`δ(per_3) = (3, 6, 12, 24, 48, 48, 30, 6)`, so the padded quartic has
`δ_6 = 30 > 20` as well as `δ_7 = 6 > 0`. The branch does **not** collapse to
LMR — the two conditions are incomparable — but the reach of the whole profile
is still exactly `dc̄(per_3) ≥ 5`, because `det_5` dominates every slot. A second
certificate at size 4, not a stronger bound. `docs/s61_review.md`.

## 4. Quiver — the best of the five, and the only genuinely new engine

Strip the survey and one object remains:

    Θ_δ : H_{4,δ} = Ind_{S_4≀S_δ}^{S_{4δ}} 1  ⟶  [δ^4] ⊗ [δ^4]

with **`mult_det(λ,δ) = rank Hom_{S_{4δ}}([λ], Θ_δ)`**.

Why this matters, in one line: `a(λ,δ)` is the **source** dimension,
`sk(λ,δ^4)` is the **target** dimension, and `mult_det` is the **rank**. Our
entire programme has been bounding a rank by two dimensions and then measuring
it by building highest-weight vectors and evaluating them on pencils. This is
the same number computed in a completely different category — finite symmetric
groups, tableaux and Plücker straightening, no pencils anywhere.

Two consequences I would bank:

- **Their Deduction 2 is right and it indicts our own search.** Because
  `mult_det` is a rank, the map can be deficient even when `a ≤ sk`. Searching
  for `a > sk` — which is what s38 did, exhaustively, finding nothing — detects
  only kernels *forced by dimension*. It cannot see a rank drop. That is the
  same orientation-versus-dimension distinction s50 exposed at the LMR cell,
  now visible as a defect in the screening method rather than in the statistic.
- The `λ`-block of `Θ_δ` is an `a × sk` matrix. At `(30,2^5)/10` that is
  **1 × 13** — trivial. At the LMR cell it is `274 × sk((65,17,2^7), 24^4)`,
  which nobody has computed but which is now a well-posed finite question.

The honest caution: implementing `Θ_δ` and straightening is real work, and the
session correctly notes the literature (Ivanyos–Qiao–Subrahmanyam) presents the
*full* multilinear invariant target, not the kernel of the degree-4-generated
subalgebra we need. The machinery gets us to the doorstep, not through it.

**This is the one I would fund**, and the first task is calibration, not
ambition: build `Θ_δ` at `δ = 2,3,4,5`, compute ranks, and check against cells
where the existing engine already has exact answers. Kill criterion:
disagreement anywhere. If it agrees, we own a second independent
multiplicity engine — and after 55 sessions with one engine, that is worth
more than another sweep.

## 5. What I would do with tonight

1. **Fund the quiver/Foulkes engine** — one implementation session, calibration
   first. It is the only proposal that computes something we currently cannot.
2. **Fund the `per_3` polar profile** — one bounded session, decides whether the
   microlocal branch is parked or has a second signal.
3. **Retire the `a = 1` / finite-hole direction** — closed from three sides.
4. **Do not open** symmetry, moment polytopes, or a broad conormal programme.
5. Correct s50 §2 (`a = 274`) at merge, per the batch assessment.

The through-line across all five: every one of them, arriving independently,
lands on the same wall — the separation is real, it is visible at degree 24 and
length 9, and no cheaper or shorter route to it has survived contact. The
quiver engine is the first proposal in a while that attacks the *measurement*
problem rather than looking for a cheaper equation.
