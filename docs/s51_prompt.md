# Session 51 — The `Λ^5` structure, derived from the resolution rather than guessed

## 0. Standing constraints

- Deliver by git bundle only.  Do not push.
- Do not edit `paper/det3-conductor.tex`, `paper/det4-onset.tex`,
  `PROJECT_NOTES.md`, or `docs/boundary_deficit.html`.  Those have a single
  writer.  If you believe one is wrong, say so in your report.
- Commit messages carry a `Co-Authored-By` trailer only.  No session-link
  trailer, in commits or in any script that commits.  No session-link URL in
  any file you write.
- Bound every run with `timeout` and `ulimit -v`.  Record the process id to
  `results/logs/<run>.pid` and end a run only by that recorded id.  Do not
  select processes by name pattern.
- No committed file over 5 MB.  Logs under `results/logs/`.  Config is
  append-only.
- Pre-registration first: state what will be measured and what would count as a
  positive result before running it.  Bank the result per cell.
- `python-flint` only for exact linear algebra.
- Any cell reporting `D > 0` goes through the verification protocol before it is
  written down as a claim.
- Before developing any statistic meant to characterise determinant type, run
  the degeneracy-direction pre-check in `docs/brief_wording.md` §5.

## 1. The observation to be explained

For `F = det_n` restricted to an `r`-dimensional pencil, `M_d(F)` has rows the
degree-`(d−3)` multiples of the `r` partial derivatives.  Its generic rank is
`ρ_d = dim Sym^d C^r − h_d` with `h_d = [t^d]((1−t^{n−1})/(1−t))^r`.  At
`d = 3n − 5` the determinantal specialisation drops below the generic rank, and
the measured drop is

    drop = C(r,5) = dim Λ^5 C^r,

confirmed at `r = 4, 5, 6, 7`.  In particular the drop at `(n,r) = (5,7)` is
**21**, which refuted the earlier alternative `(r−4)(2r−9) = 15`.

Session 48 spent itself on a one-adjugate ansatz for the syzygy at `r = 6` (a
six-dimensional space of unknowns) and found nothing.  **Do not extend that ansatz.**  The
instruction is to stop guessing the syzygy and derive it.

Two corrections to carry, both from session 48: the Macaulay matrix shape at
`(n,r) = (5,7)` is `6468 × 8008`, not `12012 × 8008` (12012 is the `d = 11` row
count); and the washout table's orbit term `2m − 2` was missing from one row.

## 2. The route

Derive the drop from the **resolution**, not from measured ranks.

The ideal of `3×3` minors of a `4×4` matrix has the Gulliksen–Négård resolution

    0 → S(−8) → S(−5)^16 → S(−4)^30 → S(−3)^16 → S,

(Gulliksen–Négård, *C. R. Acad. Sci. Paris Sér. A* **274** (1972), 16–19), and
`H_{S/J(M)}(d) = 20d − 20` for `d ≥ 5`.

The cokernel of `M_d(F)` is the degree-`d` piece of `S/J(F)`.  The drop at
`d = 3n − 5` is therefore the degree-`d` piece of the syzygy module of the `r`
partials **beyond the Koszul syzygies**.  Compute that piece from the resolution
and its Koszul cohomology, restricted along the pencil, rather than reading it
off a rank.

## 3. Start at `r = 5`, where the space of unknowns is one-dimensional

At `r = 5` the extra syzygy is unique up to scale, by a node-defect count in
Dimca's sense: the 20 nodes of the relevant discriminant impose only 19
conditions on cubics in `P^4`, leaving a one-dimensional space.

A one-dimensional space of unknowns is a far better place to look than the
six-dimensional one session 48 exhausted.  Get the `r = 5` syzygy in **closed form** —
explicit coefficients in the pencil parameters.

Verification, non-negotiable: substitute the closed form back into `M_d(F)` over
`ℤ` and confirm exact annihilation, not annihilation modulo a prime.  Hand the
check to the session-49 verifier.

## 4. Then the equivariant family

Ask whether the family is `GL_r`-equivariant with `Λ^5 C^r` the module
explaining `drop = C(r,5)`: does the `r = 5` syzygy extend to a
`GL_r`-equivariant map `Λ^5 C^r → syzygies`?  If so, the drop formula follows by
dimension count rather than by measurement.

**Consistency test.**  The construction must predict the measured drop of 21 at
`(n,r) = (5,7)`.  If it predicts anything else it is the wrong module, however
well it fits `r = 4, 5, 6`.  Run this before writing up.

## 4b. The step that matters most: turn the module into equations

Identifying the module is not the deliverable.  **Converting it into a closed
condition on the coefficients of the quartic is.**  This is the step with the
best chance in the programme of producing a determinant equation below degree 24,
and it should be attempted even if §4 only reaches a partial answer.

The shape of it.  If determinant pencils are forced to carry a distinguished
syzygy module — `Λ^5 V` or whatever §4 identifies —

    f = det M  ⟹  Λ^5 V ↪ Syz(J_f),

then build the universal presentation map `Ψ_f` whose rank detects that
embedding, and impose

    rank Ψ_f ≤ R.

The Fitting minors of `Ψ_f` are then honest polynomial equations **in the
coefficients of `f`**, of a degree set by the size of `Ψ_f` rather than by the
`1148 × 1148` Macaulay condition.  Report that degree.  It is the number the
session is for.

Three requirements, none negotiable:

1. `Ψ_f` must be built from `f` alone, not from the pencil `M`.  An equation in
   the coefficients of `f` that needs `M` to write down is not an equation for
   `D_r`; eliminating `M` is what inflates the degree, and it is the barrier that
   has defeated every previous route.
2. `rank Ψ_f ≤ R` is a closed condition, so it passes to the border
   automatically.  Say so explicitly, and check it — this is what makes the
   construction a candidate obstruction rather than an observation about exact
   determinants.
3. Run the degeneracy-direction pre-check (`docs/brief_wording.md` §5) on the
   rank condition before developing it: evaluate at a `det_4` pencil, at a
   reducible `ℓ·c`, and at the full ten-variable `ℓ·per_3`.  If the padded
   permanent has rank at least as degenerate as the determinant, the condition
   separates in the wrong direction and the work stops there.

**A warning about the tempting shortcut.**  "The graded Betti numbers differ" is
not by itself a border obstruction.  Graded Betti numbers are upper
semicontinuous in flat families with constant Hilbert function; the Jacobian
ideals of a degenerating family of hypersurfaces are not automatically such a
family.  If you argue by semicontinuity you must first prove the family it
applies to.  The safe route is the one above: determinant structure forces a rank
condition on an explicit universal map, and a rank condition is closed with no
flatness hypothesis at all.

## 5. What it buys

- a coefficient-space equation of the degree reported in §4b, which is the
  single number most likely to change the programme's shape;
- `cap(n,r)` becomes provable rather than measured;
- the certified bound `≤ 661` becomes a theorem;
- the exact minor sizes follow from the construction rather than being read off
  measured ranks — removing the last place where our cap statements depend on a
  rank computation we cannot independently confirm.

## 6. Success and partial success

**Success:** the `r = 5` syzygy in closed form, verified over `ℤ`, **and the
Fitting degree of §4b reported** even if only as a bound.

**Partial success worth having:** the equivariant type identified — a proof that
the syzygy space at `r = 5` carries the claimed `GL`-structure — even without the
closed form.

**Negative worth reporting:** the resolution route giving a degree-`d` piece of
the wrong dimension.  That would mean the drop is not a syzygy phenomenon at all,
and we want to know it.

## 7. Report

`docs/s51_report.md` with the resolution computation written out, the closed form
if obtained, the `ℤ` verification, and the `(5,7)` consistency test.  Deliver as
a bundle.
