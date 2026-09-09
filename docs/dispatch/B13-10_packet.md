# B13-10 — session packet

**You are B13-10.**  `board_numbering: batch13`.  Model: Claude Fable 5.1 — record
the model that actually ran this session in your commit trailer, not the one the
preamble asks for; truthful attribution wins.

## Before anything else

1. Clone `https://github.com/swsethuraman/gct.git` and record
   `git rev-parse main` in your pre-registration.  **Check that the clone
   contains `docs/batch13_board.md`, `docs/batch13_corrections.md`,
   `docs/stocktake_batch12.md` and `docs/batch13_worker_preamble.md`.  If any is
   missing, stop and say so** — you have a tree from before the batch-13 freeze.
   (`docs/batch13_plan.md` is a superseded draft; its presence proves nothing.)
2. Read, in full, before writing any code:
   `docs/batch13_worker_preamble.md`, `docs/batch13_board.md` (the whole
   objectives section, not only your entry), `docs/batch13_corrections.md`,
   `docs/stocktake_batch12.md`, `docs/brief_wording.md`.
   `batch13_launch_packet.zip` carries all of them if the clone is behind.
3. Write `results/PREREG_b13_10.md` — question, instrument, objects, stopping
   rules, what counts as a negative — **commit it, then compute.**  Anything not
   pre-registered is reported as exploratory.  Dated addenda are fine and are
   committed before the measurements they govern.
4. Check your toolchain rather than assuming it:
   `python3 -c "import flint, sympy, numpy, scipy; print('ok')" || pip install python-flint sympy numpy scipy`,
   and record what you installed in the preflight table.

## The two objectives, so you know which one you serve

    1.  a positive multiplicity obstruction      D = mult_pad - mult_det > 0
    2.  permanent-specific equations             mult_pad < mult_red

**The second is not necessary for the first.**  `P` inside `D` forces
`mult_pad <= mult_det` at every weight, so `mult_pad > mult_det` refutes
containment whether or not the equation is permanent-specific.  There is no
cubic-screen-first ordering rule.  `docs/batch13_corrections.md` §1 says why an
earlier draft had this backwards.

## Your assignment, verbatim from the board

### B13-10 — Fable — leaner raising-row construction

**Inputs** the current builder; s79's measured memory failures; banked
cubic and quartic controls.

Reduce peak memory in the raising-row construction, preserving mathematical
semantics, and expose the real memory/work tradeoff.

*The wall, measured.*  s79 abandoned `(10,6,6,6,2,2)₈` at `N_S·δ = 1.47·10⁸`
with the rows exceeding 4 GB, killed at `E_45`, while its kernels were never the
constraint — the largest hybrid phase in 682 cells was 202 s at
`n_χ = 732 815`.

**Acceptance.**  Matching `mult_det` is **not** sufficient — two incorrect
operators can give the same sampled rank.  On a pre-registered representative
suite spanning both polynomial degrees and both problem sizes (at least fifteen
banked cells, `n_χ` from `10³` to `10⁶`, `n = 3` and `n = 4`, lengths 5, 6 and 9
where banked cells exist), require:

1. **exact operator agreement** under declared row and column conventions, or an
   explicitly verified equivalent row space;
2. **kernel vectors returned by the new builder verified against the original
   uncompressed operators**;
3. evaluation ranks — `mult_det` at both primes — as *additional* checks, not as
   the acceptance test;

then a measured difficult-cell pilot.

**Success** a validated construction ceiling and a reproducible memory curve.
**Fallback** a working improvement on a bounded range with the remaining
allocation bottleneck identified.

**No other daytime session depends on this.**  Its production consumers are
batch 14's.
## The rules that cost batch 12 a session each

- **A nonzero minor is a rank FLOOR.**  It proves `i <= a - k`.  A sampled
  deficient rank bounds `i` from above and **never** establishes `i >= 1`.
  Nothing proves `i >= 1` except a membership statement.  Do not enter a negative
  decision-table branch on a sampled kernel; session 74 did once and withdrew it.
- **Two `exps` orderings exist and they are opposite.**  `wk8_s30_core.exps` runs
  the first exponent up from 0; other modules run it down from `n`.  Resolve a
  letter by `E.index(...)` in the ordering of the module you are calling, never
  by a literal.  This has cost three sessions, most recently in a check that
  skipped the targets it could not place and reported PASS on nothing.  **A check
  that can silently drop its own terms is not a check.**
- **Stored value matrices carry a `values_are` field** naming any transform,
  beside the numbers and not only in a sibling string.
- **A transported certificate ships its points and its `u`-values**, and records
  `u(P_j) != 0` at each.  One `u`-zero voids every transported row in its column,
  silently.
- Both house primes, `2147483647` and `2147483629`.  `rank_p <= rank_Q`.
- Runs bounded at launch with `timeout` and `ulimit -v`, pid to
  `results/logs/<run>.pid`, ended only by that recorded id.
- Files over 5 MB are not committed.  Logs under `results/logs/`.  Repository
  configuration is append-only.

## Delivery

**You do not push.  The git proxy refuses pushes; that refusal is an access
control.  Do not attempt to work around it by any means.**

Branch named for this session; deliver a git bundle against your recorded base:

    git bundle create b13_10_<name>.bundle <base>..HEAD

with a `.md5`.  **Parts are numbered from `part00`, contiguously; your report
states the total part count in its first paragraph; the `.md5` names bare
filenames and carries a digest for the whole file and one per part.**  Batch 12
delivered a two-part bundle that was really three, and a digest naming a
container path.  Both cost a round trip.

## Report

`docs/b13_10_report.md`.  Label every statement **PROVED** / **CERTIFIED** /
**MEASURED** / **ADOPTED** / **RECORDED**.  Say what you did not do, and price
what you did not reach so the next batch can plan against it.  A negative
characterised over a stated, priced region is a deliverable; an unstated gap is
not.  **Report defects in this assignment — the integrator wants them**; batch
12's best catches came from sessions correcting their briefs.

## Checkpoints

An early input-and-control checkpoint; a substantive update around 18:00; a
usable report or a resumable handoff by about 20:30 America/New_York.

**Declare your actual host resources.**  Twelve sessions do not imply twelve
independent memory budgets.

No external announcement or publication is part of this assignment.
