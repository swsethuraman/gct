# Batch 12 — standing conditions for every worker session

Read this once.  Every brief in this batch (`docs/s74_prompt.md` …
`docs/s79_prompt.md`) assumes it.  It is batch 11's preamble with the batch-12
changes marked **new**.

## new — session numbering

Two boards were reconciled and their numbering does not line up.  **Your brief's
number is the one below.**  If a document you read uses the other, this table is
the translation; never infer an assignment from a number alone.

| this batch | the reconciled proposal | mission |
|---|---|---|
| s74 | s74 | the LMR source by births, then the decision |
| s75 | s75, first half | the `δ = 12` compact control |
| s76 | s75, second half | scale the recursion to `δ = 24`, and exact `C₂₄` |
| s77 | s76 | deterministic basis — the bridge, then straightening |
| s78 | s77 | r = 5 by bounded elimination |
| s79 | s78 + s79 | the two independent frontiers |

## The repository

Clone `https://github.com/swsethuraman/gct.git`.  The base commit is the tip of
`main` when you clone; record `git rev-parse main` in your pre-registration.

**Before anything else, check that your clone contains
`docs/batch12_s1_s2_consolidated.md` and this file.  If it does not, stop and say
so** — you have an older tree and your bundle will not apply.

## new — what to read, in tiers

Read tier 1 in full before you write any code.  Read tier 2 only when your own
brief sends you to a specific section of it.  **Do not read tier 3 unless
something you are doing depends on it**; it is the historical record and it is
large.

    tier 1, required, ~23 KB total
      docs/batch12_worker_preamble.md          this file, 8 KB
      docs/batch12_s1_s2_consolidated.md      10 KB -- the batch in one document
      docs/brief_wording.md                    5 KB -- binding on your report
      your own brief

    tier 2, on demand, named by your brief section by section
      docs/batch12_claude_board.md            15 KB
      results/astra/S1/S1_report.md           27 KB
      results/astra/S2/S2_report.md           33 KB
      results/astra/S2/HANDOFF_s77.md         15 KB
      docs/lmr_cell.md, docs/compact_circuit.md   13 KB each

    tier 3, reference only
      docs/stocktake_batch11.md               28 KB
      docs/s1_batch12_review.md, docs/batch12_integrator_note2.md
      PROJECT_NOTES.md

If you find yourself reconstructing context from tier 3 to answer a question your
brief should have answered, **say so in your report** — that is a defect in the
brief and the integrator wants to know.

## new — the Astra theory deliverables are in the tree

S1 and S2 ran on a different host and wrote outside the repository.  Their
deliverables are staged at `results/astra/S1/` and `results/astra/S2/`; read
`results/astra/README.md` first.  Paths *inside* those files point at the
original Windows directory — resolve them against `results/astra/` instead.
They are session deliverables, not integrator-verified results: treat every
number in them as MEASURED-by-that-session until this repository's own code has
re-derived it.

## Delivery

You do not push.  Work on a branch named for your session and deliver a **git
bundle** made against your recorded base:

    git bundle create s7N_<name>.bundle <base>..HEAD

with an accompanying `.md5`; split into `.part00`/`.part01` if it exceeds the
transfer limit.  The integrator verifies every load-bearing claim with
independent code before merging.

**The git proxy refuses pushes.  That refusal is an access control.  Do not
attempt to work around it by any means.**

## Discipline

- **Pre-registration first.**  `results/PREREG_s7N.md`: question, instrument,
  cells or objects, stopping rules, and what counts as a negative.  Commit it,
  then compute.  Anything not pre-registered is reported as exploratory.
- **Bank per unit.**  Commit each cell, block or object as it completes.
- `python-flint` for exact linear algebra.  Both house primes, `2147483647` and
  `2147483629`, wherever a modular route is used.
- **`rank_p ≤ rank_Q`.**  Full rank mod one prime proves full rank over `Q`; a
  modular rank *drop* proves nothing.
- **The verification protocol applies to any `D > 0` cell** before it is reported
  anywhere, including in conversation.
- Files over 5 MB are not committed.  Logs under `results/logs/`.  Repository
  configuration is append-only.

## new — no prime below 97, anywhere in the S5 route

`|λ₂₄| = 96`.  Both house primes exceed 96, so `F_p[S_96]` is semisimple by
Maschke and every characteristic-zero statement about `S^λ`, its invariants and
the projectors onto them holds verbatim mod `p`.  That is what licenses sizing a
mod-`p` computation with `a_δ`, `B_δ`, `C_δ` and the DAG counts, all computed by
characteristic-zero plethysm.  It is legitimate exactly when `p > |λ|`.  A small
prime at the `δ = 12` control (`|λ₁₂| = 48`) is tempting for speed and is not
allowed.

## new — a probabilistic bound stays labelled

s72's interior value 31, the recorded 19 on `P ∩ C21`, and every other sampled
image value were obtained by pointwise Jacobian ranks plus a Schwartz–Zippel
argument.  They are source-recorded evidence, not deterministic theorems.  **Do
not promote one into a proof**, and do not build a proof on one without saying
that you have.  A slice dimension with a few reconstructed points is not a
component certificate.

## new — two `exps` orderings exist, and they are opposite

`wk8_s30_core.exps` and `tools/verify/chi_build.exps` order the degree-`n`
exponent tuples in opposite directions: `u = c_{(n,0,…,0)}` is index 0 in the
second and the **last** index in the first.  The orbit machinery uses the first.
This cost a wrong answer here before it cost one anywhere else.  **Always resolve
a letter by `E.index(...)` in the ordering the module you are calling uses, never
by a literal.**

## new — the tools that exist in your environment

`Singular`, `msolve`, `sympy`, `python-flint`, `numpy`, `scipy` are all installed
and working.  Check before assuming; a missing import is an environment gap and
never a mathematical result.  (A batch-12 theory session recorded
`ModuleNotFoundError: flint` on a different host; that is not a calibration
failure and must not be reported as one.)

## new — the verifier, and which dialect to emit

`tools/verify/selftest.py` has **twelve** cases and passes.  `sparse_nullity`
accepts two dialects; batch 11's merge left the re-derivation layer reading only
one and every certificate in the other died with `KeyError('field')`.  Fixed by
`layer3.sparse_nullity_view`.  **Emit the session-67 spelling** — `field: "F_p"`,
top-level `nullity`, `recipe`, `basis` — so that batch 12 is uniform.  If your
claim needs `reduction` or `run` or `kernel_certificates`, add them; they are
checked, and `reduction.N_S` is now compared against the verifier's own count.
`split_rank` and `hybrid_kernel` are still reported RECORDED, not re-derived.

## Running long jobs

Bound every long run at launch: `timeout <seconds>` for wall clock and
`ulimit -v` for memory, and write the run's process id to
`results/logs/<run>.pid`.  A run that must be ended early is ended by that
recorded id; runs are never ended by name-pattern matching.  Checkpoint per unit
so an interrupted run loses nothing.

## Files you do not touch

`paper/det3-conductor.tex`, `paper/det4-onset.tex`, `PROJECT_NOTES.md`,
`docs/boundary_deficit.html`.  The integrator is the single writer for these.

## Commit messages

Plain prose describing what changed and why.  End with exactly:

    Co-Authored-By: Claude Opus 5 <noreply@anthropic.com>

**No session-link trailer, no `claude.ai/...` URL, in any commit or in any script
that writes a commit.**

## Wording

`docs/brief_wording.md` §2 and §4 are binding on your report.  Stopping rules,
not the other word; searches, not the other word.

## new — the LMR decision table, pre-registered

At the goal cell `a = 274`, `i_X = 274 − rank(T_X)`, `D = rank(T_pad) − rank(T_det)`,
and LMR gives `rank(T_det) ≤ 273`.

| observed | consequence | action |
|---|---|---|
| det 273, pad 274 | `i_det = 1`, `i_pad = 0`, `D = +1` | the verification protocol takes over before it is reported anywhere |
| det 273, pad 273 | `D = 0` | compare kernel orientation in common coordinates; no multiplicity obstruction in this cell |
| pad < det | `D < 0` | an exact negative result; retain the orientation information |
| det < 273 | `i_det ≥ 2` | a structural surprise; resolve the full determinant kernel dimension before interpreting the padded side |
| span < 274 but det rank 273 on the span reached | `i_det = 1` exactly | **the determinant column is finished**, not stalled; report it as a completed half |
| partial source, no full-rank half | rank lower bounds only | do not infer nullity from a sampling shortfall; preserve certified lower bounds and the missing directions |

**The outcomes are not equally expensive, and this is not obvious.**  `rank_p ≤
rank_Q`, so a nonzero minor certifies a rank *floor* cheaply while a rank *drop*
certifies nothing.  `D = +1` needs only two floors — `rank T_det|_{M₂₃} = 273`
(which with LMR forces `i_det(24) = 1`) and `rank T_pad|_{M₂₄} = 274` — both
nonzero minors, neither a vanishing claim.  **Every other outcome needs a
certified `i_pad ≥ 1`**, which is a membership proof and needs an exact identity
or a justified determining set, not a solve against finitely many points.  So if
you reach `D ≤ 0`, report certified rank floors and the observed shortfall, and
do not present the shortfall as a theorem.

## What this batch does not fund

Native carrier construction at `n_χ` scale; support-restricted carrier ladders;
full Foulkes enumeration; Gram/support carrier realization; another broad
length-5 census for coverage; generic higher-order `r = 5` arc sweeps;
`F₄`/`E₆`/`E₇` numerology; standard `q = 2` replication; a broad minimality search
over arbitrary partitions unless the contraction representation and a pathwidth
bound are exhibited for that shape class first.  **s69's circuit economics are a
result about two-tall-column shapes and do not transfer to an arbitrary
partition family without that check.**

## Your report

`docs/s7N_report.md`: what you pre-registered, what you ran, what the numbers
are, what is certified and what is evidence, what you did not finish and where
it stopped.  Separate MEASURED from PROVED from RECORDED in every claim.  A
negative characterised over a stated, priced region is a full deliverable.

## Provenance

Author block where one is needed: Swami Sethuraman / swsethuraman@beneficus.ai /
Beneficus AI.
