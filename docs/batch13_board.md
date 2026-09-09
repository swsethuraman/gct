# Batch 13 — the consolidated board

**Controlling document.**  Session identifiers are **B13-01 … B13-12**.
Historical session numbers (s80…, S7…) are provenance, not assignment labels, and
the twelve `*_prompt.md` files of the first draft are withdrawn.
Read `docs/batch13_worker_preamble.md` and `docs/batch13_corrections.md` first.

Six Astra sessions and six Claude Fable 5.1 sessions, including three exact-math
assignments for Fable.  **Every session starts from artefacts that already
exist; no deliverable waits on another batch-13 session.**

## Objectives — two of them, and they are not the same question

    1.  a positive multiplicity obstruction      D = mult_P - mult_D > 0
    2.  permanent-specific equations             mult_P < mult_R

The second is **not** necessary for the first.  `P ⊆ D` forces
`mult_P ≤ mult_D` at every weight, so `mult_P > mult_D` refutes containment
whether or not the equation is permanent-specific.  Padded/reducible equality
does not obstruct objective 1; it makes the padded side computable by the cheap
reducible route.  My first draft got this backwards and organised the batch on
it; `docs/batch13_corrections.md` §1 records the correction.

**What the corrected logic says, measured.**  `mult_P ≤ mult_R`, so
`D > 0 ⟹ i_det > i_red`.  Across session 79's 682 six-row cells: `i_det = 0` at
**every one**, `i_red ≥ 1` at 59, and `i_red < i_det` at **none**.  So the
binding constraint on objective 1 is the **determinant** ideal being empty, not
the padded one being full.  The only cell in the record with `i_det ≥ 1` is the
LMR cell, where `i_det = 1` and `i_red = 5`.

**At the LMR cell.**  `rank T_det = 273` exactly (certified floor plus LMR's
upper bound), `rank T_pad ≥ 269` certified.  `D = 1 − i_pad(24)`, the justified
interval is `[−4, +1]`, the measured value is `−4` and is not certified.

## The twelve

### B13-01 — Fable — exact degree-13 reducible identity

**Inputs** S3's completed 39-dimensional rational source; session 74's native
fillings, which are integral polynomials and a rational source in their own
right; s74's modular candidate relations; the existing pullback formulas.

Deliver **one explicit nonzero rational polynomial** in `M₁₃` whose restriction
to a general product `ℓ·c` vanishes identically.  Stretch: all three degree-13
directions.

Use the existing pullback directly.  **Do not wait for B13-03.**  Modular
candidates may guide the search; they do not establish membership.

*Why it settles the cell:* a certified element gives `i_red(13) ≥ 1`, hence
`i_pad(13) ≥ 1`, hence `i_pad(24) ≥ 1` by monotonicity along the ladder, hence
`D = 1 − i_pad(24) ≤ 0` — through the unconditional formula, with no `ε_pad`
claim needed.

*What is measured going in, and what it is worth:* the integrator measured, on
its own points and its own evaluator, that s74's three degree-13 padded kernel
directions vanish at all 43 reducible points, span the same 3-space as the
reducible kernel at both primes, with a 39/39 generic control
(`docs/rung13_reducible.md`).  Every line of that is a sampled ceiling.

**Success** one identity with a nonzero witness and an exact replay certificate.
**Fallback** exact partial restriction matrices, the supported candidate
coordinates, and the smallest unresolved symbolic calculation.

### B13-02 — Astra — structural restriction of the LMR source

**Inputs** session 74's complete integral 274-row source (`results/s74/source.json`,
generic nullity 0 verified) and S4's factorization through the reducible
parameter space.

Construct the actual structural restriction map on the degree-24 source, from
validated small controls upward through a bounded target pilot.  **The reported
521-dimensional intermediate is an input to verify, not evidence that its entries
are cheap.**

**Primary success** an exact upper bound `rank S ≤ 273`, hence padded rank at
most 273, hence `i_pad ≥ 1` and `D ≤ 0` — the screen pre-registered in
`docs/batch11_plan.md` C3 and never runnable for want of a source.
**Stretch** exact reducible rank 269.

*Cross-checks that must hold:* `rank S ≥ mult_pad ≥ 269` (s74's certified floor);
`rank S ≤ 274` and `≤ h_pad = 521`; s74's 12-minor cross-check
(`results/s74/s4_crosscheck.json`, 144/144) reproducing on your build of `S`
and `Q`.  A `rank S` below 269 contradicts a nonzero minor and is an instrument
defect, not a result.

**Do not** require reconstruction of the degree-24 determinant kernel.  **Do
not** identify the degree-23 and degree-24 padded nullities without proof; the
integrator's argument for that identification, and its one gap, are in
`docs/batch13_corrections.md` §4 and belong to B13-07.

Independent of B13-01: full integral source and structural map, not a
small-degree candidate identity.

### B13-03 — Astra — reusable exact reducible membership method

**Inputs** the `(★)` criterion, the batch-10 / S4 factorization, known small
reducible-drop controls.

Derive and implement a finite restriction map that computes the reducible ideal
in a specified highest-weight space.  `V_red` is the image of
`(Cʳ)* × S³(Cʳ)* → S⁴(Cʳ)*`, so `F ∈ I(V_red)` iff `F` is in the kernel of the
pullback — a linear map between finite-dimensional spaces.  Clarify image,
normalisation, multiplicity and coefficient conventions.

**A worked check in both directions is part of the deliverable**: a known element
the test accepts and a known non-element it rejects.  Without both, the test has
no teeth — this batch has already had one check that passed by silently dropping
the terms it could not place.

**Success** a complete exact control and a reusable algorithm with explicit
dimensions and costs.  **Fallback** a narrower method for a stated family with a
completed example.  **Do not wait for B13-01 or B13-02.**

### B13-04 — Fable — sharpen the cubic-to-quartic transfer

**Inputs** Proposition 8 of `docs/transfer_lemma.md`; existing small exact
controls.

When does a cubic ideal constituent actually contribute an additional padded
equation?  Express it through the **intersection of the multiplication pullback's
image with the cubic ideal**, not through Pieri compatibility, which is only
necessary.

**Audit the horizontal-strip predecessor enumeration for the degree-13 LMR
cell.**  The integrator priced fifteen horizontal-13-strip predecessors of
`λ₁₃ = (21,17,2⁷)`, `a` from 1 to 9, `N_S` from `1.59·10⁷` at `(21,6,2⁷)` to
`3.70·10⁸` at `(19,6,2⁷,2)`.  Check the enumeration, and **state clearly that a
predecessor screen is targeted at one quartic cell and does not exhaust
`I(D₉^{per₃})₁₃`** — the first draft's brief said "in full" and was wrong.

State the length quantifier once, precisely, in a form a brief can quote: `μ`
interlaces `λ`, so `μ_r` may be 0 and a shorter `μ` pairs with `λ`; and say when
a shorter `μ` may be **ignored** because its `i` is the length-`k` value and that
value is already known — which, by `docs/washout_lemma.md` Theorem 2, it is for
every `k ≤ 5`.

**Success** a sufficient condition, an exact image/intersection criterion with a
computable example, or a counterexample to a proposed converse.
**Fallback** a rigorous necessary-condition refinement and an explicit small test.

### B13-05 — Fable — finite-range padded/reducible equality

**Inputs** the permanent-dominance theorem through five variables
(`docs/washout_lemma.md` Theorem 2: `D_r^{per₃} = Sym³Cʳ` for `r ≤ 5`, by an
exact full-Jacobian-rank witness, rank 35 at both primes), the inherited
six-variable exclusions, Proposition 8.

Structural pruning for the cubic equation problem at lengths seven and eight
through degree nine.  **Separate what is inherited automatically from shorter
lengths from what is genuinely new** — Theorem 2 plus the restriction lemma
excludes every constituent of length ≤ 5 at every degree, which is a large part
of any naive census.

**Do not seek global equality at six variables**: `dim P₆ = 55 < 61 = dim R₆`, so
proper containment already implies equality fails eventually.  A finite-degree
range or a specific-family theorem is the target.

**Success** a new exact exclusion or bounded equality theorem, or a rigorously
specified smaller set of constituents that must still be computed.
**Fallback** a proved reduction and a complete finite census with the unresolved
components named.

### B13-06 — Astra — a mechanism for a positive gap beyond the LMR cell

**Inputs** the certified LMR determinant line; s74's reducible findings; the
batch-10/11 record of transport methods that did not work.

Study the components obtained by multiplying the LMR module by coefficient
polynomials of degrees one and two.  Do degree-25/26 components improve the
determinant-versus-padded comparison?

**The fact this session must explain.**  `D > 0` needs `i_det > i_red`.  In the
682 six-row cells `i_det = 0` at every one, in the 326-cell record `mult_det = a`
at every one, and at the LMR cell `i_det = 1 < 5 = i_red`.  So any proposed
mechanism has to say **how `i_det` becomes positive** somewhere the reducible
ideal is smaller.  That is the gate, and no plan before this one named it.

**Success** a finite list of justified components, each with the precise rank or
membership question that decides it; or a rigorous limitation showing why the
products cannot help.  **Fallback** explicit decomposition and image data with a
bounded costed continuation.

**Do not** revive standard Adams, wreath or block-diagonal replication as an
established transport to larger determinants.

### B13-07 — Astra — independent audit of session 79

**Inputs** the complete final s79 bundle, manifests, checkers, and the inherited
dominance certificates.

In priority order:

1. **The five-variable permanent-dominance witness and the shorter-weight
   restriction argument.**  `docs/washout_lemma.md` Theorem 2 and Theorem 3(1)
   are the dependency that turns s79's 210 length-six degree-9 checks into the
   full degree-9 statement.  The integrator's `docs/s79_part2_review.md` §2
   called the shorter weights a gap; they are an **undeclared dependency**, and
   the review is corrected.  Audit the chain rather than recomputing 365 weights.
2. Completeness and full ranks of the 210 length-six degree-9 weights.  (The
   integrator verified completeness among the 331 length-6 candidates and
   reproduced every `a`; 17 of 18 checks passed, the eighteenth being the flag
   now withdrawn.)
3. The stable-family exclusions — the sixteen-block weight-13 theorem, verified
   60/60 by the integrator on an independent instrument.
4. The distinction between full-rank quartic results and sampled deficient ranks.
5. **The `ε_pad` argument** of `docs/batch13_corrections.md` §4: the containment
   `ker(T_pad) ⊆ uM₂₃` is computed mod `p` at both primes, and lifting it to `Q`
   requires that no rational ideal element has a birth coefficient divisible by
   both house primes.  Audit that, and say whether `i_pad(24) = i_pad(23)` may be
   used or must be carried as conditional.

**Success** a claim-by-claim verified ledger with exact inherited dependencies.
**Fallback** a verified prefix and the certificates needing regeneration.
**Do not** replace a short inherited proof with hundreds of redundant
computations unless its supporting certificate cannot be recovered.

### B13-08 — Fable — the moderate degree-10 cubic remainder

**Inputs** s79's frozen list, the existing validated engine, the recorded seeds.

The remaining **95 length-six weights with `N_S < 10⁷`**, in recorded cost order.
Use the current engine; **do not wait for B13-10.**

At a deficiency: investigate with fresh points and exact source checks.  **Do not
promote sampled vanishing to a rational identity.**

**Success** full-rank certificates for the completed list, or a reproducible
candidate deficiency with explicit vectors.  **Fallback** a completed, resumable
prefix.  The eleven largest cases are batch 14's.

### B13-09 — Fable — higher-length cubic exploration

**Inputs** the current cubic evaluator, exact census routines, inherited
lower-length results.

A bounded investigation at lengths seven and eight through degree nine.
Enumerate and price the relevant new components **before** selecting the
executable queue.

**Account for shorter components explicitly** — by citing Theorem 2 and the
restriction lemma where they apply, and by computing only what they do not cover.
Do not silently omit them, and do not rerun all of them.  This is the exact
failure mode of both the first draft (which would have recomputed 365 excluded
weights) and of s79's report (which omitted them without declaring the
dependency).

Use the existing builder.  If its resource limit is reached, **return the
boundary** with its `N_S·δ`; do not wait for B13-10 and do not request an
unbounded degree extension.

**Success** an exact completed range or the first verified candidate deficiency.
**Fallback** a complete costed census and a certified prefix.

### B13-10 — Fable — leaner raising-row construction

**Inputs** the current builder; s79's measured memory failures; banked
cubic and quartic controls.

Reduce peak memory in the raising-row construction, preserving mathematical
semantics, and expose the real memory/work tradeoff.

*The wall, measured.*  s79 abandoned `(10,6,6,6,2,2)₈` at `N_S·δ = 1.47·10⁸`
with the rows exceeding 4 GB, killed at `E_45`, while its kernels were never the
constraint — the largest hybrid phase in 682 cells was 202 s at
`n_χ = 732 815`.

**Acceptance** exact agreement on a pre-registered representative suite spanning
both polynomial degrees and both problem sizes — at least fifteen banked cells,
`n_χ` from `10³` to `10⁶`, `n = 3` and `n = 4`, lengths 5, 6 and 9 where banked
cells exist — the same `mult_det` at those cells at both primes, then a measured
difficult-cell pilot.

**Success** a validated construction ceiling and a reproducible memory curve.
**Fallback** a working improvement on a bounded range with the remaining
allocation bottleneck identified.

**No other daytime session depends on this.**  Its production consumers are
batch 14's.

### B13-11 — Astra — reconciled research ledger and control semantics

**Inputs** the batch-10 to batch-12 records, the final s74 and s79 artefacts, the
stable and quartic closure rules.

Extend the record beyond the older sessions, deduplicate cells, and separate
independently certified results from reported measurements.  Recompute
"open on all instruments" **without launching new searches**.

*Concretely:* `analysis/wk9_s57_lib.negative_record()` reads the ledgers of
sessions 36–54 and stops, holding 326 cells; sessions 57, 60, 63, 71, 74 and 79
measured cells it does not carry — s60's `(19,6,3,3,1)₈` and `(19,4,4,3,2)₈`,
for two.  `analysis/wk12_int_w13_census.py` now joins against it and prints a
staleness warning; extend the ledger list and re-run it.

**Include a short control audit** explaining the unpadded `n = 3` positive
example and the variable-count obstruction to using the seven-row cell for
`ℓ·per₂`: the padded form has at most five essential variables, so a seven-row
weight has zero padded multiplicity and the cell carries no padded test.  The
first draft proposed a whole session on that comparison; it is a documented
control.

**Success** a machine-readable candidate inventory with provenance, inherited
closures, resource estimates and unresolved verification flags.
**Fallback** a reconciled subset with the conflicting records named.
Final candidate ranking is batch 14's decision.

### B13-12 — Astra — repair the five-variable orbit-closure formulation

**Inputs** S2's exact controls, the reviewed s78 reduction, the batch-11
normal-cone / Rees formulation.

A correct bounded global formulation retaining the limits that normalisation
omits on the actual parametrised image.  Identify the remaining singular supports
and the precise equations or bounds required.

**Success** a valid global reduction with one completed nontrivial control or
component.  **Fallback** exact residual ideals and a sharply specified next
elimination job.

**No** generic higher-contact sampling campaign.  **No** actual-image statement
promoted to an orbit-closure theorem.

## Why all twelve launch together

- B13-01 and B13-02 are independent exact routes to the LMR sign.
- B13-03 builds a reusable method; neither route waits for it.
- B13-04 and B13-05 are theory on existing examples.
- B13-08 and B13-09 use the existing builder.
- B13-10 supplies batch 14, not batch 13.
- B13-07 verifies mathematics; B13-11 reconciles the record, keeping the
  verification labels.
- B13-12 is an independent geometry track.

Messages between sessions are useful; **no deliverable requires another batch-13
session to finish.**

## Deferred to batch 14

Degree-14 completion of the remaining LMR relations; final candidate selection
and the genuinely open stable blocks; balanced six-row production searches; the
eleven largest degree-10 cubic cases; expensive nine-variable cubic predecessor
computations; production use of the new structural-restriction and memory
methods; full degree-24 recursive interoperability and larger-`n` construction if
the day's results justify it.

## Verification and delivery rules

The preamble's rules stand.  In addition, for this batch:

- State the exact polynomial family, degree, variable count, representation and
  source convention.
- A nonzero modular minor proves a rank **lower bound** at a valid prime.
  Sampled deficiency does **not** prove ideal membership.
- A positive gap needs a justified determinant-rank **upper** bound below a
  certified padded-rank **lower** bound.
- Exact identities carry a proof of nonzeroness and an independently replayable
  membership certificate.
- Both house primes for cross-checking; agreement alone does not reconstruct a
  rational vector.
- Pre-register bounded computations and resource limits.  Check installed
  dependencies; do not assume them.
- Isolated working copies, single-writer output paths.
- Record transformations beside stored values and keep the original integer point
  data.
- Complete manifests and replay instructions.  A split bundle is numbered from
  `part00` and the report states the total part count.
- Record the model that actually ran the session.
- No external announcement or publication is part of any assignment.

## Checkpoints

An early input and control checkpoint; a substantive update around 18:00; a
usable report or resumable handoff by about 20:30 America/New_York.  The evening
stock-take chooses batch 14's twelve for a 21:00–22:00 launch.  A credible new
candidate gets independent proof and verification capacity before any further
broad search.

**Heavy jobs declare their actual host resources.**  Twelve sessions do not imply
twelve independent memory budgets.

Author: Swami Sethuraman, swsethuraman@beneficus.ai, Beneficus AI.
board_numbering: batch13
