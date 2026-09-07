# Session 72 (C5) — the `r = 5` upper bound: exhaust the normal cone

Batch 11, **ungated, runnable immediately**.  **Read
`docs/batch11_worker_preamble.md` first**, then `docs/batch11_plan.md` §6 —
which contains the target statement you and Sol session S3 share, fixed before
either of you starts — then `docs/s66_report.md` in full (especially §4 the
contact-order lemma, §5 the non-reducedness measurement, §6 the reducible
exceptional images, and §8 the honest boundary), and `docs/s32_singspaces.md`,
`docs/excess_singularity.md`.

## What this session is not

It is **not another lower-bound arc search**.  Session 66 pushed every measured
primitive and compression exceptional image to at most `29 < 31 < 35` through
the reachable orders, and removed the last mechanism the roadmap had for a
climb.  Another "does something climb?" survey adds nothing.

The remaining work is the other direction: **prove that nothing unmeasured can
climb.**

## The target statement, verbatim

> Let `R` be the coordinate ring of the `r = 5` model and `J` the ideal of the
> base scheme of `Φ`.  For **every irreducible component `E` of the exceptional
> divisor `Proj gr_J R`** of the blow-up of `Spec R` along `J` that is supported
> over `Sing V(J)` — including components supported over *proper subloci* of an
> irreducible singular component, over the incidence and rank-degeneration
> strata, and components arising from the *embedded, non-reduced* structure of
> the base scheme — the fixed-factor image of `E` has dimension `< 35`.
> Together with session 66's contact-order lemma, which disposes of every
> component supported over the smooth locus of `V(J)` (there the exceptional
> fibre is `P(im dΦ)` at every order), this exhausts `Proj gr_J R` and yields
> `R₅ ⊄ D₅`.

**The quantifier is over the normal cone, not over `Sing V(J)`**, and that is
not pedantry.  Session 66 §5 measured `in(J) ⊊ in(I₁ ∩ I₂)` at a generic point
of every pairwise incidence — `dim Q₂ = 12 < 16` at `P ∩ SP`, `41 < 69` at
`P ∩ coker`, `25 < 49` at `c21 ∩ c32`, `59 < 144` at `ker ∩ coker` — and
concluded that the base scheme is generically reduced along every component and
**non-reduced along every pairwise incidence**.  That is the precise sense in
which the normal cone of `J` differs from the normal cone of the reduced base
locus, and it is why the exceptional fibre over an incidence is larger than
`P(im dΦ)`.  A statement quantified over components of the reduced singular
locus therefore has a real gap: a component of `E` can sit over a proper
sublocus or over embedded structure and be invisible at the generic point of any
component.

## The residue is finite and already named

Session 66 §8 lists exactly four places a component of `E` could still hide:

1. `P ∩ c21`, whose order-2 image did not finish in the 25-minute box — the one
   number of the primitive world not on the table.  The reduced `Q₂` is 18
   quadrics in 30 variables; `Q₂^π` is 9 quadrics and finished in neither
   Singular nor Macaulay2's `minimalPrimes` inside 25 minutes.  Order 1 there is
   10; the locus is 33-dimensional.
2. the rank-drop strata of `M(a)` at `ker ∩ coker`;
3. contact order `≥ 4` at the incidences, and order `≥ 3` with `M₁` outside the
   tangent spaces where `V(Q₂)` has an extra component (`P ∩ c32`, `SP ∩ c21`);
4. deeper strata of the rank-`≤ 2` world — incidences of the four rank-2 types
   with each other.

By the contact-order lemma none of the four can be a smooth point of `V(J)`, and
each is a proper closed subset of a locus already measured.  **You close this
list.**  That is a finite obligation, not an open-ended survey, and saying so is
the main thing this brief adds to the previous one.

## Tasks

1. Pre-register the target statement above verbatim and the decomposition of the
   proof into the four residues plus the smooth locus.
2. Compute the special-fibre / normal-cone algebra of `J` far enough to
   enumerate the components of `Proj gr_J R` over `Sing V(J)`, including
   embedded structure.  Say explicitly which components are new relative to
   session 66's eight-component list plus the 49-dimensional semi-primitive
   component session 66 found.
3. Bound the fixed-factor image on each.  `< 35` on all of them is the theorem.
4. Give `P ∩ c21` a genuine budget — it is residue 1, it is the known gap, and a
   longer box or a better ordering may simply settle it.
5. Coordinate with S3, which is attacking the same statement theoretically.  You
   share the statement; you should not share a method.

## Success

The bound on every component, which is `R₅ ⊄ D₅`.  Short of that: the component
enumeration of the normal cone with the residue list reduced from four to fewer,
each remaining one stated precisely.

## Stopping rules

- **Discovering a rank-35 component settles the question the other way** and is
  a first-class result: stop, verify it, report it as such.
- Do not spend the session re-measuring images session 66 already has.  Its
  table is the input, not the work.
- A component you cannot bound is named and left named, with its dimension and
  what is known about it.  An unnamed gap is worse than a named one.

## Deliverables

`results/PREREG_s72.md` carrying the target statement verbatim;
`docs/s72_report.md`; the component enumeration and per-component bounds as
`results/s72_normal_cone.md` and `.jsonl`; code under `analysis/wk11_s72_*.py`;
bundle `s72_upperbound.bundle` + `.md5`.
