# Session 54 — Is `R_5 ⊆ D_5`?  The one open item on the critical path

This session settles, or gives the obstruction to, the single question session 49
will isolate as open.  It has an upside that lands directly inside our measurable
range, which most of the batch does not.

## 0. Standing constraints

- Deliver by git bundle only.  Do not push.
- Do not edit `paper/det3-conductor.tex`, `paper/det4-onset.tex`,
  `PROJECT_NOTES.md`, or `docs/boundary_deficit.html`.  Those have a single
  writer.  If you believe one is wrong, say so in your report.
- Commit messages carry a `Co-Authored-By` trailer only.  No session-link
  trailer, in commits or in any script that commits.  No `claude.ai/...` URL in
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
  the degeneracy-direction pre-check in `docs/brief_wording.md` §6.

## 1. The question

`D_r = closure{det_4(Σ s_i A_i)} ⊆ Sym^4 C^r` and `R_r = {ℓ·c}` the reducible
quartics.  We have proved `R_r ⊆ D_r` for `r ≤ 4`, via the 72 determinantal
representation classes of a smooth cubic surface, with the parameter count
exactly tight: `9·4 − 16 = 20 = dim Sym^3 C^4`.

At `r = 5` the same count gives `9·5 − 16 = 29 < 35 = dim Sym^3 C^5`.  So a
general cubic in five variables is **not** a `3×3` determinant, and the block
construction `diag(ℓ, N)` fails.

That rules out the construction.  It does not settle the question, because `D_5` is a
**closure**: `R_5 ⊆ D_5` asks whether `ℓ·c` is a *limit* of `det_4` pencils, not
whether it is one.

## 2. Why it is on the critical path

Two reasons, and the second is the one that matters.

**First.**  The transfer lemma says `P_r ⊆ R_r` implies `mult_pad ≤ mult_red`, so
`D < 0` transfers.  If `R_5 ⊆ D_5` holds, the `ℓ = 5` region is *provably* clean
rather than merely measured clean, and our exclusion of `ℓ ≤ 5` stops resting on
measurement.

**Second, and better.**  If `R_5 ⊄ D_5`, then there is something vanishing on
`D_5` and not on `R_5` — an equation for the determinantal locus at `r = 5`.
Our measured range is `δ ≤ 9` at `r ≤ 6`.  An equation at `r = 5` is *inside*
the range we can actually work in, unlike every other equation we know
(661, 300, 65, and LMR's 24).  That upside is the reason this session is worth a
slot.

So the brief has two success conditions and both are good.  Do not treat the
negative as the failure case.

## 3. Route A — construct the limit

Try to exhibit `ℓ·c` as an explicit limit of `det_4` pencils in five variables.
A single explicit one-parameter family settling generic `c` is enough: the set
of `c` for which it works is constructible and contains a dense open set, and
closure does the rest.

Concretely: the obstruction to the exact construction is that `c` is not a
`3×3` determinant.  But `c` may still be a *border* `3×3` determinant, and border
determinantal representations of cubics in five variables are a small, studied
object.  Establish first whether a general cubic in `C^5` is a border `3×3`
determinant.  If yes, Route A very likely closes the question affirmatively and
cheaply — check it before doing anything else.

## 4. Route B — the base-locus analysis, as in session 53

The same technology as session 53 applies, with one important difference.

A degeneration `M(t,s) = M_0(s) + t M_1(s) + ...` with `det M_0 ≡ 0` has
`E = M_0(V) ⊆ M_4` of bounded rank `3` and now `dim E ≤ 5`.

At `dim E ≤ 5` the **primitive** family is dimensionally available, unlike at
`dim E = 10`.  By Atkinson (1983) and Huang–Landsberg (*On linear spaces of
matrices of bounded rank*), the only primitive bounded-rank-`3` family is

    E = C^a ⊂ Hom(E, Λ^2 E),   e ↦ (v ↦ e ∧ v),

of bounded rank `a − 1`, so `a = 4` and `dim E = 4` — inside our range.  So the
case list here is: subspaces of the four compression types (dimensions 12, 10,
10, 12), **and** the four-dimensional primitive space and its projections.

Verify this against the sources before using it.  It is an imported
classification and it is load-bearing.

For each case, compute the leading term and ask which reducible quartics `ℓ·c`
arise.  Use the reducibility screen first: `ℓ·c` factors as (linear)·(cubic), and
most leading-quartic normal forms will not factor at all.

## 5. Task 0 — order `≥ 2`

As in session 53: if `det(M_0 + tM_1 + ...)` vanishes to order `k > 1`, the
leading quartic is not the first polar.  State what happens at order `≥ 2` before
starting the case analysis.  If Route A closes the question affirmatively, this
is moot and you should say so and stop.

## 6. If the answer is negative

If you establish `R_5 ⊄ D_5`, do not stop at the fact.  Extract the equation:

- identify what vanishes on `D_5` and not on `R_5`;
- give its degree in the coefficients of the quartic, and its `GL_5`-weight if it
  is equivariant;
- check whether that degree is inside `δ ≤ 9`;
- evaluate it at the three fixed points of the degeneracy-direction test set
  (`det_4` pencil, reducible `ℓ·c`, full ten-variable `ℓ·per_3` restricted to
  five variables) and report all three, exactly.

An equation at `r = 5` of low degree would reset the batch, and it should be
handed to the session-49 verifier before it is written down as a claim.

## 7. Success

Either outcome is a success:

- `R_5 ⊆ D_5` established, which upgrades the `ℓ ≤ 5` exclusion from measured to
  proved;
- `R_5 ⊄ D_5` established **with the equation extracted**, which puts an
  equation inside our measurable range for the first time.

A third acceptable outcome is a clear statement of exactly which case in the
classification resists, with the rest closed.

## 8. Report

`docs/s54_report.md`.  Deliver as a bundle.
