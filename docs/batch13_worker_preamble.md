# Batch 13 — worker preamble

Binding on every session of this batch.  Read it in full before you write code.

## Session numbering

`board_numbering: batch13`.  There is one board this batch and the numbers below
are it.  **Every report and every manifest carries a `board_numbering` field** —
in the report's front matter and as a top-level JSON key in every manifest.  A
reviewer who sees the field never has to guess, and a reviewer who does not see
it must ask rather than reject.

| | model | mission |
|---|---|---|
| B13-01 | Fable | exact degree-13 reducible identity |
| B13-02 | Astra | structural restriction of the LMR source |
| B13-03 | Astra | reusable exact reducible membership method |
| B13-04 | Fable | sharpen the cubic-to-quartic transfer |
| B13-05 | Fable | finite-range padded/reducible equality |
| B13-06 | Astra | a mechanism for a positive gap beyond the LMR cell |
| B13-07 | Astra | independent audit of session 79 |
| B13-08 | Fable | the moderate degree-10 cubic remainder |
| B13-09 | Fable | higher-length cubic exploration |
| B13-10 | Fable | leaner raising-row construction |
| B13-11 | Astra | reconciled research ledger and control semantics |
| B13-12 | Astra | repair the five-variable orbit-closure formulation |

The full assignments are in `docs/batch13_board.md`, which is the controlling
document.  The twelve `s8*_prompt.md` / `S*_prompt.md` files of the first draft
are withdrawn; `docs/batch13_corrections.md` records why.

## Two objectives, and they are not the same question

    1.  a positive multiplicity obstruction      D = mult_P - mult_D > 0
    2.  permanent-specific equations             mult_P < mult_R

**The second is not necessary for the first.**  `P ⊆ D` forces
`mult_P ≤ mult_D` at every weight, so `mult_P > mult_D` refutes containment
whether or not the equation is permanent-specific.  Padded/reducible equality
does not obstruct objective 1.

Since `mult_pad ≤ mult_red`, objective 1 needs `i_det > i_red`.  Across session
79's 682 six-row cells the determinant side is at **full rank at both primes**,
so `i_det = 0` there is CERTIFIED over `Q` — and **that alone rules out `D > 0`
in those cells**, since `D = mult_pad − mult_det ≤ a − a = 0`.  s79 also measured
positive reducible nullities at 59 of them; a sampled deficiency bounds `i` from
above, so it does **not** establish `i_red ≥ 1`, and nothing here rests on it.

At the degree-24 `n = 4` LMR target, `i_det = 1` is exact while the reducible
nullity 5 is **measured** and the exact reducible nullity is unresolved.  So the
binding constraint is the **determinant** ideal being empty wherever it has been
measured, and that target is the one place in this programme's measured `n = 4`
region where `i_det ≥ 1` is established.

An earlier draft of this preamble organised the batch on the cubic screen as
"the necessary condition for everything else".  That was wrong and is corrected
in `docs/batch13_corrections.md` §1.  The cubic screen detects permanent-specific
information and makes the padded side computable by the cheap reducible route; it
is not a prerequisite for a determinant-side search, and there is no
cubic-screen-first ordering rule in this batch.

`docs/stocktake_batch12.md` is the context; `docs/batch13_board.md` is the board.

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
