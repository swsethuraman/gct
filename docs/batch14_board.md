# Batch 14 — the consolidated board

Base: **`3efc3973`** on `main` = `integration/batch13`. Every session branches
from it and delivers by bundle against it.

Twelve slots. The weighting shifts again toward the determinant side and toward
the two capabilities everything there waits on.

---

## Read this before selecting work

Four figures that appeared in batch-13 documents are **retired**. A session that
quotes any of them is working from a withdrawn number.

| retired | replacement | why |
|---|---|---|
| `ℓ(μ) ≤ min(r, δ, 9)` | **`min(r, δ)`** | the `9` was never proved; B13-05's own proof argues Pieri, `S_μ(Cʳ) = 0`, and washout Thm 2, and nothing about 9 |
| lean builder "1.77–2.64× less memory" | **1.00–2.30×, cell-dependent** | holds on 2 of 12 A1 cells; 2 others save nothing. Not predicted by `nnz`. Sizing from the headline under-provisions |
| "≥ 1,100 CPU-hours" for the degree-9 remainder | **no figure** | fitted over 197 cells, not 99; predates B13-09's refit and B13-10's build path |
| 197 degree-9 cells | **99** (47 at `ℓ=7`, 52 at `ℓ=8`) | the union of B13-05's and B13-09's remainders, which no single session states |

Two `PROVED.md` entries changed status and both matter to planning:

- **`ladder_converse`** (Theorem F) now carries the hypotheses `a(κ,p) ≥ 1` and
  `a(ν,q) ≥ 1`. Without them `i(κ,p) = 0` holds vacuously when the ambient
  multiplicity is zero and the product argument has no vectors to multiply. All
  18 existing closures stand — every witness factor was re-checked and has
  `a ≥ 1` — but a new closure must check the hypothesis.
- **`orbit_stabiliser_silent`** dropped from PROVED + MEASURED to **MEASURED**.
  The measurement stands; the clause *"not rescued by the full stabiliser"* is
  withdrawn, because its argument (finite factors, so `b` falls by at most a
  bounded factor) is false — invariants under a larger group are an intersection
  of eigenspaces and a finite extension can annihilate them outright.

**`docs/PROVED.md` is tier-1 reading for every session.** Board entries below
cite it by id. Batch 13's single largest waste was three sessions independently
re-deriving one lemma that was already proved, because no entry named it.

**Every measurement sweep carries a control that can fail.** A1's first pass ran
eleven cells that all returned rank `= a`; nothing in it could have told a
working rank computation from one that had stopped computing. Use
`negative_control_forced` — diagonal pencils force rank 0 at length ≥ 4 — on
every evaluation-rank sweep. It is cheap and it is the only check in the set that
can fail for the right reason.

---

## Objectives

Unchanged, and still two distinct questions that must not be merged:

1. **Is `D = 1` at LMR?** `D = 1 − i_pad(24) ∈ [−4, +1]`, with `mult_det = 273`
   exact and `mult_pad ≥ 269` measured. Settling it needs one exact degree-24 or
   degree-13 identity with a fixed-factor vanishing certificate — B14-06, which
   is the decisive slot and is blocked on the two Tier C capabilities.
2. **Is there a positive gap anywhere else?** B13-06's product-image mechanism at
   the 392- and 531-dimensional targets — B14-05.

`degree8_global` closes the cubic side below degree 9 entirely. What remains
bounded and finite is 58 six-row cells at degree 10 and 99 cells at degree 9.

---

## The twelve

### B14-01 — needs the production path — the 58 six-row degree-10 cells

**Inputs** `degree8_global`, `length_bound` (corrected), `nchi_2_21_guard`,
`cost_model`, B13-08's 344 closures, `results/integrate/batch13_reconciliation.json`.

Close the remaining 58 of 402 `ℓ = 6, δ = 10` cubic cells. This is the **nearest
completable frontier theorem** — 86% is already done — and it is named in batch
13's own success criteria.

**Size before you build.** The `n_χ` of these 58 has never been measured, because
they were never built. B13-08 reports 17 of its 95 degree-10 weights exceed
`2²¹ = 2,097,152`, and two measured cells in this family sit at 2,422,004 and
2,287,905. Any cell at or above the ceiling **must** use `matmul_mod_wide`;
`matmul_mod` asserts rather than returning a wrong answer, so the failure is
loud, but it costs the run. Note also that `n_χ = N_S/|Stab|` is a lower bound,
not the exact reduced dimension — check it rather than substituting it.

**Success** the 58 closed, or a proper subset closed with the remainder priced by
phase on measured builds. **Fallback** the sizing table alone is worth the slot:
nobody has one.

### B14-02 — needs the production path — a chosen portion of the 99 degree-9 cells

**Inputs** the same, plus B13-05's structural closures and B13-09's measurements.

47 at `ℓ = 7`, 52 at `ℓ = 8`. **A chosen portion on deduplicated inputs**, with a
phase-measured cost record — not a universal curve, and not a sweep. Choose by
measured cost, cheapest first, and stop at the slot boundary with the remainder
priced.

**Scope boundary with B14-01**: B14-01 owns degree 10 at length 6; B14-02 owns
degree 9 at lengths 7 and 8. Neither runs the other's queue. Cross-check each
other's cell list against the reconciler **before** dispatching a cell — batch 13
spent 2,940 s on a cell another session had closed in 0.01 s.

**Success** a named subset closed with per-phase costs. **Fallback** the cost
record on whatever completed.

### B14-03 — needs the production path — `(12,4,4,4,4,4)₈`, the last Q1 cell

**Inputs** B13-10's pilot record, `build_no_longer_binding`, `cost_model`.

The one remaining open cell of s79's Q1 queue, determinant-first on the
integrated engine. `|Stab| = 120` compresses `n_χ` sevenfold, so it is cheaper
downstream than B13-10's pilot despite `N_S·δ = 2.16×10⁸`.

**Sizing, carefully.** The ≈2.8 GB estimate scales linearly from B13-10's
*measured* 1.96 GB build peak — it does not come from the withdrawn memory
headline. But B13-10 also records the **whole cell at 4.53 GB with the kernel
phase binding, not the build**. Budget for the kernel, not the builder.

**Success** the cell decided. **Fallback** a measured build with the kernel phase
priced, which closes the sizing question even if the decision does not land.

### B14-04 — no production path needed — the evidence base, audited

**Inputs** `results/integrate/astra_reconciliation/review_only/results/integration/`,
`unstaged_artefacts.json`, `tools/integrate/scan_unstaged.py`.

Two counted gaps, one job: **make the evidence base say what is actually there.**

- **874 uninterpreted result files** (806 `.json`, 68 `.jsonl`) in Astra's
  `unparsed_sources.json`. Register each as result / metadata / superseded, with
  its cell key where it carries one. Fold the exact identities, containment and
  stability rules and negative results into `PROVED.md` and
  `inherited_exclusions.json` — **a result that excludes a family belongs in
  both**, and keeping them apart is what let batch 13 close the same cells twice.
- **837 absent s79 certificates.** s79's manifests list 2,066 certificate paths;
  1,229 are in the tree. Classify each absence: never written, written and
  dropped by a size guard, or superseded. Regenerate what is cheap; record an
  explicit missing status for the rest. A record is not a replay.

**Success** every file registered and every listed certificate resolved to one of
the three states. **Fallback** a complete classification with the regeneration
cost of the recoverable ones priced.

### B14-05 — needs the production path — the product image at 392 and 531

**Inputs** B13-06's construction, `cartan_ladder_invariance`, and the standing
conditionality: **391 and 529 hold only if product-image ranks 2 and 3 are first
proved; otherwise the numbers are 392 and 531.**

Exact product-image construction at the 392-dimensional target, with a
reducible/padded feasibility check **before** committing to a full evaluation.
One 1,200 s / 768 MiB pilot per `B` column, banking an exact prefix.

**Success** ranks 2 and 3 proved and the sufficient padded minor falling to 391,
or a proof that it stays at 392. Either settles a conditional that four documents
currently carry. **Fallback** the feasibility check alone, which tells batch 15
whether the full evaluation is worth funding.

### B14-06 — capability-limited — one exact identity with a vanishing certificate

**Inputs** B13-01/02/03 on what it needs, `fixed_factor`, `eps_pad_inference_dead`.

**This is the decisive slot.** One exact degree-13 or degree-24 identity with a
complete fixed-factor vanishing certificate — the deliverable that would settle
`D = 1` at LMR after valid transport.

It is honestly blocked on B14-08 and B14-09, which are in this same batch and
which it **must not wait on**. So the mandate is: take the identity as far as the
current capability reaches, and deliver a precise statement of the first step
that the compact coordinates would unblock. A partial result that names its own
blocker exactly is worth more here than a broad attempt.

**If it lands, it does not stand alone.** An exact identity settling `D = 1`
would be the most load-bearing claim in the programme, and a single session's
word is not enough for that. Deliver it with an independent verification path
specified, and expect batch 15 to replicate it before it is adopted.

**Success** the identity with its certificate, or the blocker stated precisely
enough to be a batch-15 target. **Fallback** the blocker statement.

### B14-07 — no production path needed — the padded birth certificate

**Inputs** B13-07's three routes, `eps_pad_inference_dead`, `rank_floor`.

A separate, precise question: find a genuine padded point with `u = 0` and a
nonzero degree-24 native birth value. It does **not** count the old exact
equations and it does **not** depend on B14-06.

**The standing trap.** `rank_p ≤ rank_ℚ`: a sampled deficient rank is a floor on
the rank and a ceiling on `i`, and never establishes `i ≥ 1`. That inequality was
stated backwards in prose four times before batch 13. B13-07's own counterexample
— `q = 2147483647 × 2147483629`, matrix `[q,1]`, modular kernel at both primes
and rational kernel outside — is the concrete reason.

**Success** a genuine padded birth point, or a proof that the route is closed.
**Fallback** the search space characterised and bounded.

### B14-08 — mixed — the compact 521-coordinate conversion at degree 24

**Inputs** B13-02's retained fixed-factor slice, B13-03's exact membership
method, `fixed_factor`.

A certified source exported into ordinary coefficient coordinates, or coefficient
queries answered on the retained slice. **Treat this as a research objective with
intermediate deliverables, not as a routine conversion preceding the real work** —
that framing is what the first roadmap revision got wrong, and what B13-01, 02
and 03 collectively demonstrate.

**Acceptance test** recover a known LMR coefficient from the compact form and
match the banked value.

**Distinct from B14-09.** Same research problem — compact coordinates for a small
multiplicity space with an enormous ambient expansion — two different jobs, two
different degrees, two acceptance tests. Do not merge them.

### B14-09 — mixed — the 73-dimensional strip coupling at degree 13

**Inputs** B13-01's and B13-04's naming of it, `wk11_s69` for ten of fifteen
blocks.

Turn a cubic HWV `h(c)` into a target element `g(ℓ,c)` evaluable at reducible
points. Five of the fifteen blocks need a two-height Berezin evaluator; ten reuse
`wk11_s69`.

**Acceptance test** reproduce `Σ_ν a⁽³⁾ = 73` as a spanned basis and evaluate one
branching vector at a reducible point.

### B14-10 — no production path needed — a compact certificate kind

**Inputs** B13-08 §6, `certificate_ceiling`, `tools/verify/FORMAT.md`.

Design and implement a compact `hybrid_kernel` certificate kind to B13-08's
costing, verified by checking one representative large hybrid result
independently.

**This is also where B13-08's "absent standalone certificates" live, and they are
impossible rather than missing.** `full_rank` stores an `N_S`-sized basis per
vector, gated at `N_S·a ≤ 3×10⁶`; the cheapest of its 95 weights is
`N_S = 1,706,497` at `a = 2`. `sparse_nullity` is compact but keyed to
Wiedemann's Berlekamp–Massey record, which the hybrid route does not produce and
which it would be **fabrication** to write. A new kind is the only route.

Without it every result above `N_S·a = 3×10⁶` is producer-attested only, and the
verification backlog grows faster than the mathematics. That is why this is a
named success criterion and not a housekeeping item.

**Success** a kind that a third party can check without re-deriving the kernel.
**Fallback** a precise statement of what a hybrid run would have to record for
such a kind to exist.

### B14-11 — no production path needed — global elimination, narrowly

**Inputs** B13-12's repair, `rank_one_universal`.

One bounded 600 s pilot on `full_monic_Q.sing`, **contraction before
restriction**; or the certificate shortcut — one `F(y)` with `F(p(B)) = 0`
identically and `F(y_good, 0) ≠ 0`, which suffices without finishing a Gröbner
basis.

**Narrow, certificate-oriented mandate. No open-ended classification of
exceptional supports** — B13-12 shows why that route is expensive and why
restricted actual-image non-dominance does not prove noncontainment.

### B14-12 — no production path needed — `(POLE)` divisibility for `(16,6,6)`

**Inputs** B13-04's witness, `pieri_not_sufficient`.

Prove `s^{2δ} | P` symbolically. If it holds, `R₃` is not seminormal *in the
geometric sense* in that graded piece, and no fibre-type condition characterises
descent.

**This is unrelated to B13-02's work.** B13-04's seminormality is geometric
seminormalisation of `R₃`; B13-02's is Young's seminormal form. I connected them
once from a shared word, in a review and again in a roadmap. They are two
research jobs and one coincidence of vocabulary.

---

## Why all twelve launch together

**No slot waits on another slot in this batch.** I checked the text for
cross-references and there are none. B14-06 is the one place a dependency would
be natural — it wants B14-08's and B14-09's compact coordinates — and it is
written to run without them and report its blocker instead. Batch 13 carried one
such dependency (`A4 needs A1`) and the fix was to satisfy it *before* the batch,
not to renumber around it; A1 was run to completion at integration for exactly
that reason.

**The runtime split is a hard constraint, not a preference.** Batch 13 found it
nine-for-nine: Astra's runtime lacks SciPy and `python-flint`, and six Astra
sessions were blocked at the toolchain. Slots marked *needs the production path*
require a host with `python-flint`, `gcc` and SciPy together — the integrator
container has all three and `wk11_s71_schur.c` compiles there. Allocate on that
line first and on subject-matter fit second.

## What I am not funding

- **The whole degree-9 remainder as a sweep.** B14-02 takes a chosen portion. No
  replacement for the withdrawn 1,100-hour figure should be quoted until B14-01
  and B14-02 produce phase-measured costs.
- **The fifteen degree-13 predecessors as a screen.** The cheapest few are now
  buildable, but the screen needs all fifteen and the dearest is
  `N_S·δ = 1.05×10¹⁰`.
- **Further measurement up the LMR Cartan ladder.** `cartan_ladder_invariance`:
  every later rung inherits `i_X` unchanged. Those rungs are not independent
  opportunities.
- **Orbit-stabiliser work at `ℓ ≤ 8`.** Margins of 29 to 691 with a structural
  reason. *Not* extended to `ℓ = 9` any more — see the pre-flight item below.

## One pre-flight item, before dispatch

**The full-stabiliser bound at `ℓ = 9`.** B13-05's Theorem E used only the proved
part of the stabiliser, `H′ = T ⋊ F` with `|F| = 72`; the Marcus–May full
stabiliser was ADOPTED and never computed with, because the withdrawn clause said
it could not help. At `ℓ = 9, δ = 9` the margin `b − a` is **4**, at `(11,2⁸)`.

Run the Burnside computation of `analysis/wk13_b13_05_bound.py` over the full
stabiliser at the eight measured `ℓ = 9, δ = 9` cells first. All eight are
measured `i = 0`, so `b < a` there would put two PROVED-labelled things in
contradiction and must be resolved before anything else launches. If `b ≥ a`, the
withdrawn dismissal is corroborated by an independent route and the `δ ≥ 10`
extension is worth a look. A dimension computation, not a rank computation — it
belongs to the integrator, like A1, not to a slot.

## Verification and delivery rules

Unchanged from batch 13, plus what batch 13 cost us:

- **Pre-register before computing.** Question, instrument, decision table,
  falsifiers, stopping rules, labelled expectations — committed before the first
  measurement.
- **Run `tools/delivery/check_delivery.py --branch … --base 3efc3973 --bundle …`
  before building the bundle.** Six checks. It now refuses a base it cannot
  resolve rather than reporting on nothing.
- **Bundle must carry the named ref**, not just HEAD. Use the worker tips as
  negatives — bundles are never thin, and on the batch-13 delivery that was the
  difference between 135 KB and 35.7 MB.
- **Checksums are taken after the file is in the repository, or the file ships
  binary.** Eight of nine batch-13 recovery checksums failed against the tree
  because they hashed CRLF originals that git normalised to LF. The one that
  verified was gzipped.
- Commit messages carry `Co-Authored-By:` only. No session-link trailer, in
  messages or in any script that writes commits — batch 13 lost a rewrite to one
  hardcoded line in a sweep script.
- Never touch `paper/det3-conductor.tex`, `paper/det4-onset.tex`,
  `PROJECT_NOTES.md`, `docs/boundary_deficit.html`.
- No file over 5 MB. Gzip and ship a README beside it giving the original name,
  original size, both checksums and the decompression command.
- Bound every run with `timeout` and `ulimit -v`; record the pid to
  `results/logs/<run>.pid`; **end runs only by recorded id, never by name
  pattern.**
- Record the model that actually ran the session.

## Checkpoints

Judge this batch by decisive outputs, not cells visited. Two of these four would
change the position more than another broad collection of partial searches:

1. **One exact LMR-related identity**, settling `D = 1` (B14-06).
2. **One genuinely promising gap calculation** — enough determinant equations and
   a plausible padded-rank threshold (B14-05).
3. **One completed frontier theorem** — the 58 six-row degree-10 cells are the
   nearest (B14-01).
4. **One scalable independent certificate workflow** (B14-10).
