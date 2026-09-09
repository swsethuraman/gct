# Batch 13 — worker preamble

Binding on every session of this batch.  Read it in full before you write code.

## Session numbering

`board_numbering: batch13`.  There is one board this batch and the numbers below
are it.  **Every report and every manifest carries a `board_numbering` field** —
in the report's front matter and as a top-level JSON key in every manifest.  A
reviewer who sees the field never has to guess, and a reviewer who does not see
it must ask rather than reject.

| | mission |
|---|---|
| s80 | a leaner raising-row builder; then extend `negative_record()` to sessions 55–79 |
| s81 | close `I(D₆^{per₃})₉` — the 365 length-≤5 weights — then degree 10 completely |
| s82 | `I(D₇^{per₃})_δ` and `I(D₈^{per₃})_δ`, by degree |
| s83 | `I(D₉^{per₃})₁₃` in full; `I(D₉^{per₃})₂₃` priced, then as far as it fits |
| s84 | `i_pad(23)` exactly, by S4's factorization on s74's 274-row source |
| s85 | the three rung-13 reducible relations over `Q`, on S3's rational source |
| s86 | the balanced six-row cells, on s80's builder |
| s87 | the `n = 3` positive control: the §5 three-point test where `D > 0` |

## The one question this batch asks

`mult_pad = mult_red` was measured at three lengths on four instruments in batch
12 with no exception.  The transfer lemma says why that is the whole question:

> **Prop. 8(2)** `mult_pad < mult_red` at length `r`, degree `δ` **requires**
> `I(D_r^{per₃})_δ ≠ 0`.
> **Prop. 8(1)** `I(D_r^{per₃})_δ = 0` gives `mult_pad = mult_red` at **every**
> weight of that length and degree.

So the batch asks it once per `(r, δ)` instead of once per weight, on the cubic
side, with no padded points.  **No quartic sweep at a new length runs before the
cubic screen at that length has.**  If your brief seems to ask you to break that
order, say so in your report before you do.

`docs/stocktake_batch12.md` is the context in one document; read it, and
`docs/batch13_plan.md` §0 for the reasoning.

## The repository

Clone `https://github.com/swsethuraman/gct.git`.  Record `git rev-parse main` in
your pre-registration.

**Check that your clone contains `docs/batch13_plan.md`,
`docs/stocktake_batch12.md` and this file.  If it does not, stop and say so** —
you have an older tree and your bundle will not apply.

## What to read, in tiers

    tier 1, required
      docs/batch13_worker_preamble.md      this file
      docs/stocktake_batch12.md            the batch in one document
      docs/brief_wording.md                binding on your report
      your own brief

    tier 2, on demand, named by your brief
      docs/batch13_plan.md                 the board and the protocols
      docs/transfer_lemma.md               Prop. 8 -- read it if you touch the cubic side
      docs/s74_final_review.md             the goal cell's verified state
      docs/rung13_reducible.md             the rung-13 measurement
      docs/s79_part2_review.md             what the degree-9 scan does and does not cover
      docs/lmr_cell.md, docs/compact_circuit.md, docs/sparse_det_route.md

    tier 3, reference only
      PROJECT_NOTES.md, the batch stock-takes, the per-session reviews

If you reconstruct context from tier 3 to answer a question your brief should
have answered, **say so in your report** — that is a defect in the brief.

## Delivery — read this twice, batch 12 lost a part

You do not push.  Work on a branch named for your session and deliver a git
bundle made against your recorded base:

    git bundle create s8N_<name>.bundle <base>..HEAD

with an accompanying `.md5`.  Then:

- **Parts are numbered from `part00`**, contiguously, with no gaps.
- **Your report states how many parts there are**, in the first paragraph.
- **The `.md5` names the bare filename**, never a path — `md5sum -c` has to work
  on a different machine.  Include a digest for the whole file **and one per
  part**, so a mismatch says which part to resend.
- If you rewrite branch history, say so in the report and say what was dropped.

Batch 12 delivered a two-part bundle that was really three parts, and a digest
file that named a container path.  Both cost a round trip.

**The git proxy refuses pushes.  That refusal is an access control.  Do not
attempt to work around it by any means.**

## Discipline

- **Pre-registration first.**  `results/PREREG_s8N.md`: question, instrument,
  cells or objects, stopping rules, and what counts as a negative.  Commit it,
  then compute.  Anything not pre-registered is reported as exploratory.  Dated
  addenda are fine and are committed before the measurements they govern.
- **Bank per unit.**  Commit each cell, weight or object as it completes.
- **`rank_p ≤ rank_Q`.**  A full rank mod one prime proves full rank over `Q`.
  A modular rank **drop** proves nothing: a nonzero minor is a rank *floor* and
  gives only `i ≤ a − k`.  **Nothing proves `i ≥ 1` except a membership
  statement.**  No report enters a negative decision-table branch on a sampled
  kernel; batch 12 did once and withdrew it.
- Both house primes, `2147483647` and `2147483629`, wherever a modular route is
  used.  Both exceed every `|λ|` this batch touches, so `F_p[S_{|λ|}]` is
  semisimple and characteristic-zero plethysm may be used to size a mod-`p`
  computation.  A smaller prime is tempting for speed at a small control and is
  not permitted anywhere the sizing argument is used.
- **The verification protocol applies to any `D > 0` cell, and to any nonzero
  `I(D_r^{per₃})_δ`,** before it is reported anywhere, including in
  conversation: second prime on every rank, two independent point families,
  characteristic zero where a kernel is claimed, an independent source, and the
  degeneracy pre-check of `docs/brief_wording.md` §5.
- Files over 5 MB are not committed.  Logs under `results/logs/`.  Repository
  configuration is append-only.
- Runs bounded at launch with `timeout` and `ulimit -v`, the process id written
  to `results/logs/<run>.pid`; a run that must end early is ended by that
  recorded id, never by name-pattern matching.

## The tools your environment may or may not have

`Singular`, `msolve`, `sympy`, `python-flint`, `numpy`, `scipy` are the ones this
programme uses.  **Check, then install what is missing** — do not assume any of
them is present.  Three batch-12 containers had no `python-flint` and one had no
C compiler.  Open your run with

    python3 -c "import flint, sympy, numpy, scipy; print('ok')" \
      || pip install python-flint sympy numpy scipy

and record what you had to install in the preflight table.  A missing import is
never a mathematical result; equally, a gap you could have closed with one `pip
install` is not a reason to downgrade an exact computation to a sampled one.

## Two conventions batch 12 paid for

**Stored value matrices say what transform they are under.**  If a file holds
values that are scaled, normalised or transported at read time, it carries a
`values_are` field naming the transform, **next to the numbers** and not only in
a sibling string.  Session 74's `rows_native` held native values that the row
system scales by `msym_u^{24−d}`; the integrator read them as the rows and got a
determinant rank of 274, contradicting LMR.

**A transported certificate ships its points and its `u`-values.**  If a minor
is carried by `u^k` scaling, deliver the points — or the seed and the generator
that made them — and record `u(P_j)` at every one.  A single `u`-zero point
voids every transported row in its column, silently.  S1's transported artefact
verified only because its own control matrix happened to be in the package.

## Two `exps` orderings exist, and they are opposite

`wk8_s30_core.exps` runs the **first** exponent up from 0; several other modules
run it **down** from `n`.  Resolve a letter by `E.index(...)` in the ordering the
module you are calling uses, **never by a literal**.  This has now cost three
sessions, most recently the integrator's own verifier — where it was hidden by a
check that skipped the targets it could not place and reported PASS on nothing.
**A check that can silently drop its own terms is not a check.**

## Your report

`docs/s8N_report.md`.  Label every statement **PROVED** / **CERTIFIED** /
**MEASURED** / **ADOPTED** / **RECORDED**, say what you did not do, and give the
cost of what you did not reach so the next batch can price it.  A negative
characterised over a stated, priced region is a deliverable; an unstated gap is
not.  Report defects in your brief — the integrator wants them.

Author: Swami Sethuraman, swsethuraman@beneficus.ai, Beneficus AI.
board_numbering: batch13
