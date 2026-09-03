# Session 42 — the reducible-locus multiplicity engine (the pad side, by table lookup)

You are **session 42** of the gct programme, working for the integrator.  Date
your work 2026-09-02 onward.  This is a build session: make
`mult_λ C[R_r]` — the multiplicity of `S_λ` in the coordinate ring of the
reducible locus `{ℓ·c}` — computable across the whole obstruction-eligible
region, so that every future obstruction hunt reduces to a det-side-only
computation.  If the repository already shows a session 42, do not renumber;
flag it and carry on.

## Rules (standing)

- Fresh clone of `github.com/swsethuraman/gct`, branch `s42-redengine`,
  container only.  **Ancestry gate**: `git merge-base --is-ancestor 5aa564b
  HEAD` must pass, **and** `docs/reducible_ideal.md` and
  `analysis/wk9_s36_red.py` must exist (absence ⇒ stale clone; stop).
- Single-writer files — never touch: `paper/det3-conductor.tex`,
  `paper/det4-onset.tex`, `PROJECT_NOTES.md`, `docs/boundary_deficit.html`.
- Delivery by git bundle (`git bundle create redengine.bundle s42-redengine`,
  single ref).  No pushes.  No file over 5 MB; logs under `results/logs/`;
  kill by explicit PID.
- `results/PREREG_s42.md` first: for each route, what you expect to compute and
  what would show it wrong.  Label proved / measured / adopted / expectation.

## Required reading

`docs/reducible_ideal.md` (the (★) theorem and point-free `mult_red`),
`docs/theory_directions.md` Direction 1 (the Kempf-collapsing proposal),
`docs/transfer_lemma.md` (what a reducible-side number proves — read this
carefully, it governs the whole deliverable), `docs/s35_review.md` §1,
`docs/s36_review.md`, `docs/stabiliser_reduction.md`, `docs/washout_lemma.md`.

## What the engine is for, and what it does and does not prove

By the transfer lemma, `mult_λ\bC[R_r] ≥ mult_λ\bC[P_r]` (the true padded
permanent), with equality for `r ≤ 5` (washout).  So a reducible-side value is:

- at **r = 5**, exactly `mult_pad` — a complete pad side;
- at **r ≥ 6**, an *upper bound* on `mult_pad`.  Its use there is twofold:
  where `mult_red ≤ mult_det` it proves `mult_pad ≤ mult_det`, i.e. `D ≤ 0`
  (**a blindness certificate**, no pad-point computation needed); where
  `mult_red > mult_det` it flags a **candidate** for the expensive true-pad
  recheck of session 41's protocol.  It never confirms `D > 0` on its own.

State this contract in the prereg verbatim.  The engine is a blindness prover
and a candidate filter, not an obstruction confirmer at r ≥ 6.

## Route A — push the (★)/point-free route to its frontier (guaranteed deliverable)

`docs/reducible_ideal.md`'s Corollary gives
`mult_red(λ,δ) = a − dim(HWV ∩ span M_★)`, computed by linear algebra on
monomial supports of the reduced highest-weight space (`analysis/wk9_s36_red.py`).
This is already validated and needs no evaluation points.  Run it over the
**entire obstruction-eligible region** reachable under the stabiliser
reduction: `n = 4`, `6 ≤ ℓ(λ) ≤ 10`, `λ_1 ≥ δ`, `a ≥ 1`, for `δ = 7 … 12` as
far as `n_χ` allows.  Publish `results/mult_red_table.md` — a lookup table of
`mult_red` for every reachable cell — with the feasibility frontier named.
Cross-check against s36's banked cells (where `mult_red = mult_pad` was
verified) before trusting the table.  This table alone, cross-referenced with
session 41's `mult_det` values, converts the six-row hunt into a filter: only
cells with `mult_red > mult_det` need true-pad measurement.

## Route B — the Kempf collapsing (the frontier-breaker; stretch goal)

`D_5^{pad} = R_5` (and the ℓ ≤ 5 reducible loci generally) is the image of the
total space of the rank-`\binom{r+2}{3}` subbundle `S = O(-1) ⊗ Sym^3\bC^r`
over `\bP^{r-1}` under multiplication, generically finite of degree 1
(birational).  This is Weyman's geometric technique with two gifts: the base
`\bP^{r-1}` has trivial higher cohomology in the relevant twists, and the
Koszul terms resolve by `Sym^b(Sym^3)^* ⊗ Λ^{k-b}(Sym^4)^* ⊗ O(b)` with all
twists `b ≥ 0`, so all higher sheaf cohomology vanishes and the hypercohomology
reduces to Koszul homology of explicit `GL_r`-maps in **multiplicity-sized
blocks** (tens to hundreds), with no `N_S` wall.

Implement it for `r = 5` first and **validate against three banked `mult_pad`
values at `δ = 6` (s30) and the (★) table** — same span, exact — before any new
cell.  If it validates, compute `mult_red` at `r = 6` for the cells Route A
could not reach (the balanced, large-`a` cells past the reduction frontier),
extending the blindness/candidate map into the region no rank computation can
touch.  If a bookkeeping obstacle blocks it (e.g. `R_r` not normal, so the
collapsing computes the normalisation's multiplicities plus a correction),
document exactly where and stop — a precise obstacle is a valid deliverable.

## Route C — the classical literature (cheap, do alongside)

`I(R_r)` is the ideal of forms with a linear factor — a classical object.
Check Chipalkatti, Abdesselam–Chipalkatti, and the CGGHMNS line on ideals of
reducible/decomposable forms for a generating set or the low-degree
multiplicities in the `GL`-graded form this needs.  A published description
would validate (or correct) the (★) table for free.  Record the verdict:
known, or new.

## Pre-registration (minimum)

P1: the (★) table reproduces s36's banked `mult_red = mult_pad` cells.  P2:
whether Route B validates at `r = 5` against s30 and the (★) table (your prior
and its basis).  P3: the literature verdict.  Kill criteria: (★) table
disagreeing with a banked cell → stop, the pipeline is wrong; Route B
disagreeing with (★) at `r = 5` → Route B has a bug, fall back to the
delivered table.

## Deliverables

`results/PREREG_s42.md`, `results/mult_red_table.md` (the guaranteed
deliverable), `docs/reducible_engine.md` (the (★) frontier, Route B's outcome
or precise obstacle, the literature verdict, and the blindness certificates the
table already proves — every `ℓ=6` cell with `mult_red ≤` the s36-measured
`mult_det`), code `analysis/wk9_s42_*.py`.  End with the one sentence the
integrator should carry forward and the bundle head hash.
