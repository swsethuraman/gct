# Session 40 — theory: the onset conjecture, the n = 3 twin, and three write-ups

You are **session 40** of the gct programme, working for the integrator.  Date
your work 2026-09-02 onward.  This is a theory session with four deliverables;
computation is limited to exact checks that fit in minutes.  If the
repository already shows a session 40, do not renumber; flag it and carry on.

## Rules (standing)

- Fresh clone of `github.com/swsethuraman/gct`, branch `s40-onset`, container
  only.  **Ancestry gate**: `git merge-base --is-ancestor 48bbdc3 HEAD` must
  pass, **and** `docs/s36_review.md` must exist.
- Single-writer files — never touch: `paper/det3-conductor.tex`,
  `PROJECT_NOTES.md`, `docs/boundary_deficit.html`.  Text intended for the
  paper goes in a docs file for the integrator to place.
- Delivery by git bundle (`git bundle create onsetconj.bundle s40-onset`,
  single ref).  No pushes.  Logs under `results/logs/`; nothing over 5 MB.
- `results/PREREG_s40.md` first: for each deliverable, the statement you
  expect to prove and what would show it false.  Label every claim proved /
  measured / adopted-from-literature / expectation.

## Required reading

`docs/theory_directions.md` §C (the defect route), `docs/blindness_slab.md`
(s37's literature pin: Dimca 2013 Thm 3.1 and the Koszul bookkeeping),
`docs/d5_ideal.md` and `docs/paper_section4_draft.md` (the `n = 3` six-nodal
story and Theorem E), `docs/s35_review.md`, `docs/s36_review.md`,
`docs/stabiliser_reduction.md`, `docs/e4_hunt.md` §4, and paper 1's
Question 8.5 as it stands in `paper/det3-conductor.tex` (read only).

## The observation this session makes rigorous

Session 35 showed at `n = 4` that the generic five-variable determinantal
quartic threefold has 20 nodes with defect 1, so its Jacobian ring in degree
`3d − 5 = 7` has dimension 31 against the smooth 30, hence the size-300
minors of the degree-7 Macaulay matrix of the partials vanish on `D_5^det` —
an equation of degree 300.  The integrator has verified this morning that the
identical mechanism operates at **`n = 3`**: determinantal quinary cubics
have Jacobian corank 6 in degree `3·3 − 5 = 4` against the smooth 5 (three
random pencils, exact), so the size-65 minors of the degree-4 Macaulay matrix
vanish on `D_5^{det_3}`.  And at `n = 2` the same recipe gives the 5×5
symmetric matrix of a quadric, whose determinant — the discriminant, degree 5
— is *exactly* the generator of the ideal of rank-≤4 quinary quadrics.

So one formula gives 5, 65, 300 at `n = 2, 3, 4`:

    cap(n) = dim Sym^{3n−5} C^5 − μ_{3n−5}(n),   μ_k(n) = [t^k] ((1 − t^{n−1})/(1 − t))^5,

exact at `n = 2`, a valid cap at `n = 3` and `n = 4`.

## Deliverable 1 — `docs/onset_conjecture.md`

State and prove what is provable, conjecture the rest:

- **Theorem (the cap at every n).**  For every `n ≥ 2`, `I(D_5^{det_n})`
  contains the size-`cap(n)` minors of the degree-`(3n−5)` Macaulay matrix.
  Route: every member of `D_5^{det_n}` is singular along the pencil's
  intersection with the rank-`≤ n−2` locus (adjugate vanishes there; Jacobi);
  for the generic member these are `ν(n)` ordinary double points (Kleiman
  transversality — state it as the one step you adopt); the nodes fail to
  impose independent conditions on forms of degree `2n − 5` by at least one
  (prove this: at `n = 3`, six points in `P^4` cannot impose six conditions
  on linear forms; at `n = 4` it is s35's measured defect — give a reason or
  leave it measured); Dimca's theorem then gives corank `≥ μ + 1`, so the
  minors vanish on a dense subset, hence on the closure.  Re-verify the
  `n = 3` corank drop yourself at fresh pencils, both primes.
- **Conjecture.**  The onset of `I(D_5^{det_n})` equals `cap(n)` — i.e. the
  Jacobian minors are the *first* equations.  Record: proved at `n = 2`;
  what kills it (any length-5 bite below 65 at `n = 3`, below 300 at
  `n = 4`); what supports it (the empty record through degree 7 at both `n`,
  session 38's silence of the occurrence route, s35's Fitting-degree
  observation that minor-type covariants cost their size).
- **The n = 5 anomaly.**  `ν(5) = 50` (Giambelli) but `codim D_5^{det_5} =
  126 − 77 = 49`: the "nodes = codimension" coincidence of `n = 3, 4` fails.
  Say what this means (the 50 nodes impose dependent conditions; is
  `D_5^{det_5}` a component of the 50-nodal locus?) and whether it threatens
  the cap theorem there (it should not — the defect only grows).

## Deliverable 2 — `docs/paper1_delta0_patch.md`

The exact replacement text, in paper 1's voice and notation, for every place
the bracket `8 ≤ δ_0 ≤ 80` appears (the length-theorem subsection's closing
paragraph and Question 8.5): the new bracket `8 ≤ δ_0 ≤ 65`, the one-paragraph
argument, the honest labelling of the Kleiman step, and one sentence placing
the conjecture.  Keep it to the minimum the paper needs; the integrator
places it.  Do not touch the tex.

## Deliverable 3 — `docs/reducible_ideal.md`

Session 36's (★) criterion written as a general theorem: for any `n`, `r`,
`δ`, a highest-weight vector of weight `λ` in `C[Sym^n C^r]_δ` vanishes on
`{l·c}` iff every monomial has, for every `i`, a factor `c_α` with `α_i = 0`
— the Bruhat proof in full; the corollary `mult_red(λ, δ) = a − dim(HWV ∩
span M_★)`; the Kadish–Landsberg corollary `λ_1 < δ ⇒ mult_red = 0`; and the
onset statements `I(R_5)` at degree 5, `I(R_6)` at degree 6, with the
generators s36 named.  Check the literature once: is (★) known (Chipalkatti
on reducible forms, or older)?  Cite or state novelty honestly.

## Deliverable 4 — `results/n3_length5_plan.md`

The conjecture is testable from below on paper 1's own object.  Using
`analysis/wk9_s36_census.py` adapted to `n = 3`, list the length-5 cells at
`n = 3` for `δ = 8..12` with `a ≥ 1` and their reduced sizes `n_χ`; mark what
fits a 7 GB container; and run the cheapest three or four on the det side
(`D_5^{det_3}`, corrected raising rule, two primes) if they fit in your
budget.  Any bite below 65 kills the conjecture; each empty cell is evidence.
This is the plan a follow-up compute session would execute.

## Deliverables

The four documents, `results/PREREG_s40.md`, exact checks as
`analysis/wk9_s40_*.py` with outputs under `results/logs/`.  End with the one
sentence the integrator should carry forward and the bundle head hash.
