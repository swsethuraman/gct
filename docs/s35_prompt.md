# Session 35 — theory session: new attacks on the onset window, degrees 9 and above

You are **session 35** of the gct programme, working for the integrator.  Date
your work 2026-09-01 onward.  This is a **thinking session, not a sweeping
session**: the deliverable is ranked theoretical directions with falsifiable
first steps, and the only computations permitted are literature checks and
cheap in-container sanity tests (hours, not days).  If the repository shows a
session already claiming 35, do not renumber; flag it and carry on.

## Rules (standing)

- Fresh clone of `github.com/swsethuraman/gct`.  Branch `s35-theory`,
  container only.  **Ancestry gate**: `git merge-base --is-ancestor 63fe705
  HEAD` must pass (ancestry, not equality).  If it fails, stop and report.
- Single-writer files — never touch: `paper/det3-conductor.tex`,
  `PROJECT_NOTES.md`, `docs/boundary_deficit.html`.
- Delivery by git bundle (`git bundle create theory.bundle s35-theory`,
  single ref).  No pushes; the proxy refuses them by design.
- **Pre-register the rubric, not predictions**: before generating a single
  direction, commit `results/PREREG_s35.md` containing the scoring rubric you
  will rank directions by (impact if true × probability of working ÷ cost of
  finding out), your criteria for discarding a direction, and this rule:
  every direction you keep must name **a falsifiable first test** and **what
  would kill it**.  Ranking against a rubric committed in advance is this
  session's analogue of prediction discipline.

## Required reading, in order (fresh eyes, but informed eyes)

`docs/s33_review.md` §4 (the onset window), `docs/e4_hunt.md`,
`docs/sweep62.md` §4–5, `docs/s30_review.md`, `docs/l5_containment.md`,
`docs/singular_spaces.md` (s32), `docs/quiver_route.md` (s31),
`docs/d5_ideal.md` (s28 — the `n = 3` mirror of everything below),
`docs/s34_prompt.md` (the conventions), and the house failure classes in the
reviews: regime transfer, quotient-blindness, shared-spec correlation,
lowest-invariant bias.  Do not re-derive banked results; do not re-propose
counting routes (session 31 killed them at `n = 3`, and the same Hilbert
comparison kills them here) or rung-climbing at `r = 4` (session 33 closed
that door at degree ~3.2×10⁵).

## The problem state, precisely

Objects, inside `Sym^4 C^5`: `D_5^det` = closure of `det_4(s_1A_1 + ... +
s_5A_5)` (dim 50, codim 20) and `D_5^pad` = closure of the restrictions of
the padded permanent = `{l · c}`, `l` linear, `c` any quinary cubic (dim 39,
codim 31).  Proved: the varieties differ in both directions (`39 < 50`, and
`D_5^pad` is not inside `D_5^det` — s32's Theorem 5).  Convention:
`D(lam, delta) = mult_pad − mult_det = det_units − pad_units`, where "units"
counts copies of `S_lam` in the respective ideal in degree `delta`.  **An
obstruction is a single cell with `D > 0`** — the determinant's ideal
strictly bigger than the padded permanent's at one weight.

Known constraints on where it can live:

- The det-side ideal is empty through `delta = 6` (measured, s30) and — so
  far uniformly — at `delta = 7` on the reachable cells (s34, in flight).
- The det-side onset at `r = 5` is **capped at 405**: every member of
  `D_5^det` is singular (pencil meets the rank-`<= 2` locus of `M_4`,
  adjugate dies, Jacobi kills the partials), so the quartic-threefold
  discriminant (degree `5·3^4 = 405`, weight `(324^5)`) lies in
  `I(D_5^det)`.  It also lies in `I(D_5^pad)` (`l·c` is singular along
  `l = 0` meet `c = 0`), so the discriminant itself separates nothing.
- Below degree ~3.2×10⁵ the det-side ideal has **no length-4 part** (the
  `r = 4` reduction is the principal ideal of degree `e = 320112`), so a
  `D > 0` cell in any humanly reachable degree has `ell(lam) >= 5`.
- **Compute owns `delta <= 8` at best.**  At `delta = 7` only 46 of 433
  gate-passing cells fit in 7.2 GB; `ell >= 6` strata start at ~24 GB.  The
  window you are attacking is `delta in [9, 405]`, `ell >= 5`, where no
  sweep will ever go on current hardware.
- **Open in both directions, and say so**: set-level separation does not
  force a multiplicity witness.  It is consistent with everything known that
  `det_units <= pad_units` at every weight in the window — call this
  *multiplicity blindness*, the padded-small-scale shadow of
  Bürgisser–Ikenmeyer–Panova.  Proving blindness over a degree range is as
  valuable as finding a witness; treat the two as rival hypotheses, not as
  hope versus failure.

## Seeds — known to the programme; your job is to go past them

You may develop, sharpen, or demolish these, but a report that contains only
these four has added nothing:

**(A) The nodal-locus mirror.**  At `n = 3`, the generic member of
`D_5^{det_3}` is a cubic threefold with exactly six nodes — six = the degree
of the Segre = the codimension — and the six-nodal question drives the
`delta_0` bracket.  At `n = 4`: the generic pencil `P^4` meets the
rank-`<= 2` locus (projective dim 11) in `nu` points, `nu` = the classical
Giambelli/Thom–Porteous degree of that locus — compute it.  Check: are the
`nu` points generically nodes; is `nu` equal to the codimension 20 (the
`n = 3` pattern says the analogue should be exact); is `D_5^det` a component
of the `nu`-nodal locus?  Vainsencher's multi-nodal degree formulas chart
nearby territory.  A covariant tuned to `nu` coincident conditions of degree
well under 405 would collapse the ceiling.

**(B) The pad side is classical — use it.**  `I(D_5^pad)` is the ideal of
the *reducible* quartics `l · c`, a classical object (decomposable/split
forms; Chipalkatti and others).  Its lowest equations and their weights are
plausibly known or derivable.  Every weight where pad is provably blind
(`pad_units = 0`) and det sees (`det_units >= 1`) is an obstruction —
knowing pad's ideal weight-by-weight converts the hunt from two unknowns to
one.

**(C) Schofield structure, not Schofield counting.**  `C[D_5^det]` sits
inside the semi-invariant ring of the 5-arrow Kronecker quiver for `M_4`,
where Derksen–Weyman say every semi-invariant is a Schofield determinant.
Counting dies (s31's lesson transfers), but the *structure* may identify
which isotypic pieces the subalgebra misses — a weight-explicit handle on
the ideal that no dimension count gives.

**(D) Mine the matmul-obstruction literature.**  Multiplicity and occurrence
obstructions have actually been exhibited in neighbouring settings
(Bürgisser–Ikenmeyer on matrix multiplication; Ikenmeyer–Panova's vanishing
technology; obstruction designs).  What transfers is technique — explicit
HWV evaluation at structured points, Young-tableau combinatorics for
vanishing — not conclusions.  A genuine pass over that literature with our
two specific varieties in hand has never been done.

## Deliverable

`docs/theory_directions.md`: five to eight directions, ranked by the
pre-registered rubric, each stated in at most a page with (i) the precise
claim or object, (ii) the mechanism — why it could work, (iii) the
falsifiable first test costing at most a day in-container, (iv) what kills
it, (v) what changes if it works.  Develop the **top two** in depth, and if
either's first test is runnable here, run it and bank the outcome (exact
arithmetic, house rules).  Label every statement proved / measured /
expectation.  An honest boundary section; the bundle head hash at the end of
your report.
