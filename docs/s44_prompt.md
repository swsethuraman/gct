# Session 44 — a six-row cap theorem: bracketing the onset from above, without measuring cells

You are session 44 of the gct programme, working for the integrator.  Date your
work 2026-09-03 onward.  This is a theory-and-small-computation session, and it
is the one that could make the expensive half of the programme unnecessary.  If
the repository already shows a session 44, do not renumber; flag it and carry
on.

## Why this session exists

Everything at `n = 4` now turns on one unknown.  An obstruction requires
`mult_det < a` — the determinant's six-row ideal `I(D_6^{det_4})` must be
nonzero at the cell — and sessions 36 and 41 measured 90 six-row cells through
`δ = 8` with `mult_det = a` at every one.  The cells where the ideal would
plausibly start (balanced `λ`) sit two to three orders of magnitude beyond any
rank computation we can run.  So the measurement route cannot answer it.

The five-row case was answered *geometrically instead*, and the argument is in
the repository: `docs/onset_conjecture.md` and `docs/s40_review.md`, with the
`n = 3` instance written up as Proposition `prop:jaccap` in
`paper/det3-conductor.tex`.  This session asks whether the same argument runs
one row up.

## The mechanism, stated so you can check it in five minutes

Let `F ∈ Sym^n C^r` be a form of degree `n` in `r` variables, and let
`M_d(F)` be the Macaulay matrix of its `r` partial derivatives in degree `d`:

    M_d : ⊕_{i=1}^{r} Sym^{d-n+1}(C^r) → Sym^d(C^r),   (g_i) ↦ Σ_i g_i ∂F/∂x_i .

Its entries are **linear in the coefficients of `F`**, so every `k × k` minor of
`M_d` is a polynomial of degree `k` on `Sym^n C^r`.  For a *smooth* `F` the
partials are a regular sequence, so `rank M_d = dim Sym^d(C^r) − h_d` with `h_d`
the coefficient of `t^d` in `(1 + t + … + t^{n-2})^r`.  A form singular along a
positive-dimensional locus has a larger Milnor algebra, hence **smaller rank**.
So if `rank M_d` drops on the determinantal locus, the maximal minors of the
generic size are nonzero polynomials vanishing on it:

> **`I(D_r^{det_n})` is nonzero in degree `ρ_d = rank M_d(generic)`, for every
> `d` at which the rank drops on `D_r^{det_n}`.**  The cap is the smallest such
> `ρ_d`.

**Anchors — reproduce both before anything else** (both are arithmetic, seconds):

| case | `d` | rows | cols | generic `h_d` | generic rank |
|---|---|---|---|---|---|
| `n=3, r=5` (cubic in 5 vars) | 4 | 75 | 70 | 5 | **65** |
| `n=4, r=5` (quartic in 5 vars) | 7 | 350 | 330 | 30 | **300** |

65 is exactly paper 1's `δ_0 ≤ 65`; 300 is exactly `cap(4)` of the five-row cap
theorem.  So the cap theorem *is* this construction, and the rank drop at those
`(n, r, d)` is the fact to re-verify numerically (a random smooth form versus a
random `det_n(Σ_{i=1}^{r} s_i A_i)`, integer `A_i`, ranks mod a house prime).

## The target: `n = 4`, `r = 6` — quartics in six variables

Generic ladder (verify it yourself; `h_d` = coefficient of `t^d` in
`(1+t+t^2)^6`):

| `d` | rows | cols | `h_d` | generic rank | full row rank? |
|---|---|---|---|---|---|
| 4 | 36 | 126 | 90 | 36 | yes |
| 5 | 126 | 252 | 126 | 126 | yes |
| 6 | 336 | 462 | 141 | 321 | no |
| 7 | 756 | 792 | 126 | 666 | no |
| 8 | 1512 | 1287 | 90 | 1197 | no |

So the possible caps, in order, are **36, 126, 321, 666, 1197, …**  A drop at
`d = 4` would put an element of `I(D_6^{det_4})` in degree 36 — below every
degree the programme has ever measured, and it would make the six-row onset
question answerable by direct computation.  A drop first at `d = 6` gives 321.
Note the structural reason a drop is *expected somewhere*: a generic member of
`D_6^{det_4}` is singular along the locus where the `4×4` pencil has rank `≤ 2`,
which has codimension 4 in the space of matrices and so cuts a curve in `P^5`
(expected degree 20).  Height 4 < 6 means the partials are **not** a regular
sequence, so non-Koszul syzygies exist; the only question is in which degree the
first one appears.  Koszul syzygies alone would first act at `d = 2(n−1) = 6`.

## What to do

**Phase 1 — validate.**  Reproduce the two anchor rows above numerically: build
`M_d` for a random smooth form and for `det_n(Σ s_i A_i)`, take ranks at both
house primes, and confirm the generic ranks 65 and 300 and that the
determinantal rank is strictly smaller in each case.  Also confirm the generic
rank equals `dim Sym^d − h_d` at several `(n, r, d)`, so the formula is not
being taken on trust.

**Phase 2 — the ladder at `n = 4`, `r = 6`.**  For `d = 4, 5, 6, 7, 8` compute
`rank M_d` for (i) several random quartics, (ii) several `det_4(Σ_{i=1}^{6} s_i
A_i)` with independent random integer `A_i`, at both primes and with fresh
seeds.  Report the smallest `d` with a strict drop, and the corank.  A drop that
appears at one seed and not another is a bug or an unlucky prime — chase it
down, do not average.

**Phase 3 — what the drop gives.**  At the smallest such `d`, the generic rank
`ρ` is the cap.  State it as a proposition with proof: the `ρ × ρ` minors of
`M_d` are degree-`ρ` forms on `Sym^4 C^6`, not identically zero
(nonzero at a smooth quartic — exhibit one), and vanishing on `D_6^{det_4}`
(the rank drop — exhibit that too).  Hence `I(D_6^{det_4})_ρ ≠ 0` and the
six-row onset is `≤ ρ`.  Combined with sessions 36 and 41 (`= 0` through
`δ = 8` at every measured cell) this brackets the onset.

**Phase 4 — sharpen, as budget allows, in this order.**

1. *Does the same element vanish on the padded permanent?*  Evaluate the
   construction at true padded-permanent points `l(s)·per_3(A(s))`, `r = 6`.  If
   the minors vanish there too, the cap is a bound on the determinant ideal but
   the element is not a separator — say so plainly.  If they do **not** vanish
   on padded permanents, that is a separating equation and a much larger result:
   stop and report it as a candidate, with the verification protocol of
   `docs/s41_prompt.md` applied.
2. *Which weights?*  If `ρ` is small enough to be tractable, find the `GL_6`
   weights `λ` occurring in the module generated by these minors — that turns
   the cap into a pointer at specific cells for a future measuring session.
3. *The singular locus.*  Confirm the rank-`≤ 2` locus of a generic six-parameter
   `4×4` pencil is a curve, compute its degree (expected 20) and, if you can,
   its arithmetic genus and the Hilbert function of its ideal — this is the
   input a Dimca-style defect computation would need for a sharper cap.
4. *General `(n, r)`.*  If the mechanism gives a clean smallest-`d` rule, state
   the cap as a formula in `n` and `r` and check it against 65 and 300.

**Phase 5 — literature.**  Search for this construction: Jacobian/Macaulay rank
drops as equations for determinantal hypersurface loci; the ideal of the variety
of determinantal hypersurfaces; syzygies of the Jacobian ideal of `det` of a
linear matrix pencil.  Report per claim whether it is known, with a citation, or
not found.  If the six-row cap is already in the literature, that is a *good*
outcome — record it.

## Rules (standing)

- Fresh clone of `github.com/swsethuraman/gct`, branch `s44-sixrowcap`,
  container only.  **Clone check**: `docs/onset_conjecture.md`,
  `docs/s40_review.md`, `docs/sixrow_frontier.md` must exist (absence ⇒ stale
  clone; stop and report).
- Single-writer files — never edit: `paper/det3-conductor.tex`,
  `paper/det4-onset.tex`, `PROJECT_NOTES.md`, `docs/boundary_deficit.html`.
  You may read `paper/det3-conductor.tex` for Proposition `prop:jaccap`.
- Delivery by git bundle (`git bundle create sixrowcap.bundle s44-sixrowcap`,
  single ref).  Do not push.  Checkpoint bundle every few hours.
- **Commit messages carry `Co-Authored-By` only** — no session-link trailer,
  in commits or in any script that commits.  No `claude.ai/...` URL in any file.
- No file over 5 MB committed; logs under `results/logs/`; append-only config.
- Bound long runs with `timeout` and `ulimit -v`, and record each run's process
  id in `results/logs/<run>.pid`; end a run only by that recorded id, never by
  name-pattern matching.
- `results/PREREG_s44.md` first, before any rank is computed: your predicted
  smallest `d` with the drop and the resulting cap, with reasoning; your
  prediction for Phase 4.1 (separator or not); stopping rules.  Ranks by
  `python-flint`, two primes, several seeds.

## Deliverables

`results/PREREG_s44.md`, `results/s44_ladder.md` (the full rank table, generic
versus determinantal versus padded-permanent, both primes, all seeds),
`docs/sixrow_cap.md` (house style: the mechanism, the two anchors reproduced,
the theorem as you can state it, what is proved versus measured versus adopted
from literature, the honest boundary), code `analysis/wk9_s44_*.py`.  End with
the cap as you leave it — a number, or a precise statement of what blocks one —
and the bundle head hash.
