# B14-07 — session packet

**You are B14-07.** `board_numbering: batch14`. Intended model: **Claude**.
Record the model that *actually* ran this session in your commit trailer and your
report, not the one this preamble names — truthful attribution wins.

Host class: **flint**. You need `gcc`, `python-flint` and SciPy together. Six of the twelve do; allocate on that line.

## Your base — one commit, and it does not move

    git fetch origin --tags
    git rev-parse batch14-base

**`batch14-base` is an annotated tag, not a branch.** Check out that exact
commit, run the delivery check against it, and cut your bundle against it. Do not
substitute `origin/main`: it can advance while you are running, and a base that
moves under a session is how a worker delivers against a tree it never read. Two
earlier versions of this rule were wrong — a stamped hash that named the commit
before the board, then a moving ref — and the tag is the third and last answer.

Record `git rev-parse batch14-base` and `git show -s --format=%T batch14-base` in
your pre-registration. If the tag is absent, your clone predates the freeze:
stop and say so rather than guessing a base.

## Before anything else

1. Confirm the tree carries `docs/batch14_board.md` (v0.4 or later),
   `docs/PROVED.md`, `docs/brief_wording.md`, `docs/b14_claude_scratch_code.md`
   and `docs/batch14_reconciliation.md`. **If any is missing, stop and say so.**
2. Read, in full, before writing any code: `docs/batch14_board.md` — the whole
   of §1 and §2, not only your own entry — then `docs/PROVED.md`,
   `docs/brief_wording.md`, and `docs/batch14_reconciliation.md`.
3. Write `results/PREREG_b14_07.md` — question, instrument, objects, decision
   table, falsifiers, stopping rules, labelled expectations — **commit it, then
   compute.** Anything not pre-registered is reported as exploratory. Dated
   addenda are fine and are committed before the measurements they govern.
4. Check your toolchain rather than assuming it, and record what you installed:
   `python3 -c "import flint, sympy, numpy, scipy; print('ok')"`.

## The two objectives, so you know which one you serve

    1.  a positive multiplicity obstruction      D = mult_pad - mult_det > 0
    2.  permanent-specific equations             mult_pad < mult_red

**The second is not necessary for the first.** `P` inside `D` forces
`mult_pad <= mult_det` at every weight, so `mult_pad > mult_det` refutes
containment whether or not the equation is permanent-specific.

At LMR, `a = 274`, `m_det = 273` exactly and `m_pad >= 269`, so `D` lies in
`[-4, +1]`. The batch's centre of mass is spent on closing our own main
candidate, because closing it cheaply is worth more than sampling around it, and
because Lemma T makes the alternatives conditional on the same number.

## Your assignment, verbatim from the board

### 7 — flint — exact degree-14 source matrix at `P14`

**Inputs** as slot 2; `P14.json` by blob; `results/s74/ladder_ranks.json`.

The `93 × 192` integer matrix from rows born by degree 14, transport exponent
`14 − native_degree`, seven-prime signed CRT on a bound you re-derive.

**Left kernel, as in slot 2**: `K14` of size `93 × k`, verify `A14ᵀ·K14 = 0`,
`rank(K14) = k`, `rank(A14) = 93 − k` over `ℚ`. It becomes an ideal kernel only
after the degree-14 target certificate, the recount and the interpolation check
all pass.

**This does not wait on slots 1 or 2.** The source half is independent of the
target half; begin with one exact block and measure it. The memo's indicative
seven hours across seven primes is *not* a validated timing and the rung-13 rate
is not a rung-14 rate. **Success** the exact matrix and rational kernel, or a
certified prefix with a reproducible completion plan. **Stopping rule** a bound violation
or a source-control inconsistency stops the arithmetic. A partial matrix's
nullity remains a **ceiling**.

## The rules that have each cost this programme a session

- **A nonzero minor is a rank FLOOR.** It proves `i <= a - k`. A sampled deficient
  rank bounds `i` from above and **never** establishes `i >= 1` on its own. The
  single exception is `complete_interpolation`, and it needs all four conditions:
  `dim N = h` proved, `h` members exhibited, a nonzero `h x h` minor at `P`, and
  exact source arithmetic. `PROVED.md: evaluation_cannot_certify_i_ge_1` carries
  the corrected statement; an earlier wording denied the exception outright.
- **A check that cannot fail is not a check.** `PROVED.md:
  check_must_be_able_to_fail` lists six instances in batch 13. There is now a
  seventh, and it is the integrator's: the batch-14 reachability script reported
  both controls PASS on an **empty** census, because `all()` and `not any()` over
  nothing are vacuously true, and the integrator replayed it and certified the
  controls without testing that either could fail. **Feed every control an input
  that must make it fail, and report that you did.**
- **Two `exps` orderings exist and they are opposite.** `wk8_s30_core.exps` runs
  the first exponent up from 0; other modules run it down from `n`. Resolve a
  letter by `E.index(...)` in the ordering of the module you are calling, never by
  a literal. Three sessions have paid for this.
- **A transported certificate ships its points and its `u`-values**, and records
  `u(P_j) != 0` at each. One `u`-zero voids every transported row in its column,
  silently.
- **Stored value matrices carry a `values_are` field** naming any transform,
  beside the numbers and not only in a sibling string.
- **`n_chi` is not `N_S/|Stab|`.** That quotient is neither an upper nor a lower
  bound. `FORMAT.md` records `N_S = 211636`, `|Stab| = 2`, `n_chi = 82004`. The
  invariant is `n_chi <= N_S`; measure `n_chi` rather than deriving it.
- Both house primes, `2147483647` and `2147483629`. `rank_p <= rank_Q`.
- `python-flint` for exact linear algebra. Pre-registration before computation.
- Runs bounded at launch with `timeout` and `ulimit -v`, pid written to
  `results/logs/<run>.pid`, ended only by that recorded id.
- Files over 5 MB are not committed. Logs under `results/logs/`. Repository
  configuration is append-only.
- Never touch `paper/det3-conductor.tex`, `paper/det4-onset.tex`,
  `PROJECT_NOTES.md`, `docs/boundary_deficit.html` — the integrator is the only
  writer of those four.

## Delivery

**Deliver by bundle; do not push.**

Branch named for this session; bundle against the tag:

    git bundle create b14_07_<name>.bundle batch14-base..HEAD

with a `.md5`. Parts are numbered from `part00`, contiguously; your report states
the total part count in its first paragraph; the `.md5` names bare filenames and
carries a digest for the whole file and one per part.

Run `python3 tools/delivery/check_delivery.py --branch <your branch> --base
$(git rev-parse batch14-base)` before creating the bundle, then rerun it **with**
`--bundle <file>` once the file exists.

## Report

`docs/b14_07_report.md`. Label every statement **PROVED** / **CERTIFIED** /
**ADOPTED** / **MEASURED** / **CONDITIONAL** / **NOT REACHED**. Say what you did
not do, and price what you did not reach so the next batch can plan against it. A
negative characterised over a stated, priced region is a deliverable; an unstated
gap is not.

**Report defects in this assignment — the integrator wants them.** Every round of
this batch's planning, the sharpest corrections came from a session or a reviewer
correcting its own brief. The integrator has been wrong about the delivery base
three times, about a control that could not fail, and about four entries in the
index you are being told to read.

## Checkpoints

An early input-and-control checkpoint; a substantive update partway; a usable
report or a resumable handoff by the end of your window.

**Declare your actual host resources.** Twelve sessions do not imply twelve
independent memory budgets.

No external announcement or publication is part of this assignment.
