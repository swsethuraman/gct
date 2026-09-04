# Session 48 — two theorems within reach: the six-row cap closed, and the washout threshold in m

You are session 48 of the gct programme, working for the integrator.  Date your
work 2026-09-04 onward.  This is a theory-and-small-computation session with
three independent targets, in priority order; none needs a large container and
each can be dropped without harming the others.  If the repository already shows
a session 48, do not renumber; flag it and carry on.

## Rules (standing)

- Fresh clone of `github.com/swsethuraman/gct`, branch `s48-theorems`, container
  only.  **Clone check**: `docs/sixrow_cap.md`, `results/s44_ladder.md`,
  `analysis/wk9_s44_syzygy.py`, `analysis/wk9_s44_probe.py`,
  `docs/washout_lemma.md`, `docs/brief_wording.md` must all exist (absence ⇒
  stale clone; stop and report).
- Single-writer files — never edit: `paper/det3-conductor.tex`,
  `paper/det4-onset.tex`, `PROJECT_NOTES.md`, `docs/boundary_deficit.html`.
- Delivery by git bundle (`git bundle create theorems.bundle s48-theorems`,
  single ref).  Do not push.  Checkpoint bundle every few hours.
- **Commit messages carry `Co-Authored-By` only** — no session-link trailer, in
  commits or in any script that commits.  No `claude.ai/...` URL in any file.
- No file over 5 MB committed; logs under `results/logs/`; append-only config.
- Bound long runs with `timeout` and `ulimit -v`; record each process id in
  `results/logs/<run>.pid`; end a run only by that recorded id.
- `results/PREREG_s48.md` first, before any computation, with a prediction for
  each of A, B and C.

## Target A — close the six-row cap *(the standing gap)*

`docs/sixrow_cap.md` establishes `onset I(D_6^{det_4}) ≤ 1197` as a theorem
(Theorem A, from the Gulliksen–Négård ceiling) and `≤ 666` as **certified but
not proved**: the Macaulay rank of the six partials of `det_4(Σ_{i=1}^6 s_i A_i)`
at `d = 7` is 660 against the generic 666, verified exactly over `Q` at three
explicit integer pencils by a multimodular argument, with Schwartz–Zippel putting
the chance of a generic rank of 666 at `2.4·10⁻²⁷`.  That is not a proof.

**What a proof needs.**  The drop of six is `dim H_1(K(∂F; S))_7 = 6`: six
syzygies `Σ_k G_k ∂_k F = 0` with `G_k ∈ S_4` that are not Koszul — equivalently
six degree-4 **logarithmic derivations** `δ = Σ_k G_k ∂/∂s_k` with `δ(F) = 0`
beyond the trivial ones.  Find them in closed form, valid for every pencil, and
`≤ 666` becomes a theorem.

What session 44 already established, so you do not repeat it: the search space is
`{ 𝒳M + M𝒴 : tr(𝒳 + 𝒴) = 0 } ∩ (L ⊗ S_4)` modulo the Koszul span, and it is
six-dimensional; `W(s) = Σ_k G_k A_k` has full rank 4 at generic `s`, so the
syzygies do **not** factor through a degenerate part of the pencil; and the first
family anyone writes down, `W_i = F·A_i − ¼(∂_i F)·M(s)`, is entirely Koszul by
Euler's identity.  The numerics are written (`analysis/wk9_s44_syzygy.py`,
`analysis/wk9_s44_probe.py`) and cheap.  Useful orientation: at `r = n²` the
determinant is a linear free divisor whose logarithmic derivations are generated
in degree 1 by `gl_n ⊕ gl_n` — the 30 linear syzygies of the Gulliksen–Négård
complex — and cutting `L` down to six dimensions destroys those generators and
pushes the first non-trivial derivations up to degree 4.  Compute the six
explicitly at a random pencil first, in coordinates; look for the pattern; then
try to write them for a general pencil and verify symbolically.

## Target B — the discriminating rank at `(n, r) = (5, 7)`

Session 44 measured the drop at `d = 3n−5` to be `0, 1, 6` at `r = 4, 5, 6`
across `n = 3, 4, 5`, and proposed `C(r,5) = 0, 1, 6, 21`.  **The data does not
pin the formula**: `(r−4)(2r−9)` fits the same three points and gives **15** at
`r = 7`, not 21.  `C(r−3,2)` fits two of the three.  So `(n, r) = (5, 7)` — the
one case in the ladder that is neither ceiling-limited nor already measured — is
a *discriminating* test, not merely the next data point.

It needs the rank of a `12012 × 8008` Macaulay matrix at a determinantal pencil
and at a random quintic control, both house primes, several seeds.  Note the
direction of inference (`docs/sixrow_cap.md` §4): a rank at a point mod `p` is a
lower bound on the generic rank, so a *drop* is only certified, never proved, by
this route; report it with the same labels session 44 used, and if the drop is
large enough that a multimodular certificate is affordable, run one.

If the answer is 21, `C(r,5)` survives and `cap(n, 6) = dim Sym^{3n−5} C^6 −
h_{3n−5}(n,6)` becomes statable as a general conjecture with the same proof shape
as `cap(n)`.  If it is 15, say so plainly and give the corrected formula.

## Target C — the washout threshold as a function of m

`docs/washout_lemma.md` proves `P_r = R_r` for `r ≤ 5` at `m = 3`: the padded
permanent restrictions are dense in the reducible locus below length 6, so the
permanent is invisible there.  The general statement is a dimension count and
should be written as a theorem in `m`.

`P_r = R_r` requires `{per_m(A(s))}` to be dense in `Sym^m C^r`, where `A(s)` is
an `m × m` matrix of linear forms in `r` variables.  The parameter count is
`m² r` against `dim Sym^m C^r = C(r+m−1, m)`, so density **requires**

    m² r  ≥  C(r + m − 1, m),

which is free and gives the *failure* direction with no computation: above the
threshold the permanent must become visible.  The integrator's table:

| `m` | washout holds up to `r*` | permanent first visible at | deficit there |
|---|---|---|---|
| 2 | 7 | 8 | 4 |
| 3 | **5** | **6** | **2** |
| 4 | 5 | 6 | 30 |
| 5–11 | 4 | 5 | 1, 30, 85, 175, 310, 501, 760 |

The `m = 3` row is the programme's own case and the deficit 2 at `r = 6` is
exactly what session 37 measured.  Your job: (i) re-derive the table
independently; (ii) at each `(m, r)` with `r ≤ r*`, check the Jacobian of
`A ↦ per_m(A(s))` has full rank `C(r+m−1, m)` at a random point — the dimension
count is necessary, the Jacobian is what makes density sufficient (as session 35
did at `m = 3`, `r = 5`, Jacobian 35); (iii) state the result as a theorem with
both directions and the exact threshold; (iv) say what it means — that any
length-reduced model must work at length `> r*(m)` to see the permanent at all,
and that the deficit at `r*(m)+1` measures how faintly it shows.

Say plainly whether this is a limitation on the *length-reduced model* or
something stronger; do **not** describe it as a natural-proofs barrier, which it
is not (natural proofs is constructivity plus largeness; the known GCT barriers
are Bürgisser–Ikenmeyer–Panova on occurrence obstructions).  Search the
literature for the threshold and for the density of permanental pencils, and
report per claim whether it is known.

## A fourth thing, if any time is left

Session 44 showed the Macaulay minors vanish on padded permanents as well as on
determinants, and the reason is structural: `ℓ·c` is singular in codimension 2
(a threefold in `P^5`) against the determinantal curve, so the pad-side Milnor
algebra grows like `d³` where the determinantal one grows like `d`.  That is
provable with an explicit threshold, and it generalises to: **no construction
that reads excess singularity can produce `D > 0` at `n = 4`.**  Write it as a
proposition with the degree bound made explicit.  It closes a whole family of
approaches permanently and belongs in paper 2 as a named result.

## Pre-registration (minimum)

A prediction and a prior for each of A (do you find the six in closed form?),
B (21 or 15?), C (does the Jacobian have full rank at every `(m, r)` below the
threshold?).  Stopping rules: A is the standing gap and gets the first half of
the session, but if it stalls, move to B and C, which are both short — do not
let A consume the whole session.

## Deliverables

`results/PREREG_s48.md`; `docs/sixrow_cap_closed.md` (A: the six syzygies as you
leave them — closed form, or the search narrowed with what is now ruled out — and
B: the `(5,7)` rank with the formula it selects); `docs/washout_threshold.md`
(C: the theorem, the table, the Jacobian checks, the literature verdict);
`results/s48_*.md` for the raw ranks; code `analysis/wk9_s48_*.py`.  End with
each target's status in one line and the bundle head hash.
