# Session 55 — Equations for the determinantal locus below degree 24

A literature session with small confirming computations.  It answers the number
that governs whether this programme is reachable at all.

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

## 1. The gap that defines the difficulty

| construction | lowest degree with a known equation for `D_r` |
|---|---|
| Macaulay minors, `r = 6` | 661 certified, 1148 proved |
| Macaulay minors, `r = 5`, `n = 4` | 300 |
| Macaulay minors, `r = 5`, `n = 3` (paper 1) | 65 |
| Landsberg–Manivel–Ressayre | 24 |
| **our measured range** | **`δ ≤ 9`** |

Every plan we have made has been shaped by this gap, usually implicitly.  The
question for this session is explicit: **is there any construction producing
equations for the determinantal locus below degree 24 — and is there one below
degree 9?**

An answer either way changes what the programme should do.  If something exists
below 9, we measure it directly and the programme becomes an experiment rather
than a search.  If a documented argument says nothing can go below 24, the
measured range and the equation range never meet by this route, and the
programme's shape has to change accordingly.

## 2. Candidates to examine

Work through these, and record for each: the construction, the lowest degree it
produces at `n = 4`, whether the equation is **explicit** or merely
**existential**, and whether the degree is proved or measured.

1. **The LMR family itself.**  Their construction is one member of a family of
   equations for hypersurfaces with degenerate duals.  What do the other members
   give — other `k`, other dual defects?  Is 24 the minimum over the family at
   `n = 4`, or an artefact of one choice?
2. **Mignon–Ressayre.**  Their Hessian/dual-variety argument is normally quoted
   as a *rank bound*.  What does the same geometry give as **equations**?  A rank
   condition on a bordered Hessian is a determinantal condition, so it has a
   degree; compute it at `n = 4` and compare with 24.
3. **Landsberg–Ressayre.**  Their Cayley–Bacharach method for equations of
   determinantal loci.  Does it transfer to our setting, and at what degree?
4. **Young and Koszul flattenings.**  The standard low-degree equation families
   for quartics.  Do any of them vanish on `D_r`?  Most will not — check and
   record, since this is the cheapest family to rule in or out.
5. **Boundary equations.**  Hüttenhain–Lairez classified the boundary of the
   `det_3` orbit closure.  Does the analogous `det_4` boundary analysis produce
   equations, and at what degree?
6. **The Plücker route from session 53.**  The common-isotropic-4-plane condition
   is closed, and the external session reports `I_1(B_9) = I_1(B_10) = 0`, so the
   first equations there are at Plücker degree `≥ 2`.  Include this only with the
   caveat that stated clearly: those are equations of the **section** locus in
   `Gr(r, Λ^2 W)`, not of the quartic in `Sym^4 C^r`.  Converting one to the
   other means eliminating the pencil, and elimination is what inflates degree.
   Estimate that elimination degree rather than quoting the Plücker degree as if
   it were ours.

## 3. Standing checks

- For every candidate, run the degeneracy-direction pre-check from
  `docs/brief_wording.md` §5 before spending time on it: evaluate at a `det_4`
  pencil, a reducible `ℓ·c`, and the full ten-variable `ℓ·per_3`.  Two external
  sessions in a row produced invariants that were *more* degenerate at the padded
  permanent than at the determinant; that check costs minutes.
- Distinguish sharply between an equation that vanishes on `D_r` (which is what
  we need) and an invariant that merely detects some special structure of
  determinant-type objects (which is usually satisfied by the padded permanent
  too).
- Re-derive any degree you quote.  Both of our own cap degrees were wrong for two
  sessions because a generic rank was quoted where a determinantal rank was
  needed.

## 4. Deliverable

A single table in `docs/equation_census.md`, one row per construction, with
columns: construction, reference, lowest degree at `n = 4`, explicit or
existential, proved or measured, and whether the degeneracy-direction check
passes.  Plus a short paragraph per row saying what it would take to bring the
degree down.

## 5. Success

**Success:** the census completed and every degree re-derived rather than
quoted.

**Best outcome:** any equation below degree 24, or — nearly as valuable — a
documented argument that the dual-degeneracy family cannot go lower at `n = 4`.

**Acceptable outcome:** a clear statement that the answer is unknown for a named
subset, with the reason.

## 6. Report

`docs/s55_report.md` plus `docs/equation_census.md`.  Deliver as a bundle.
