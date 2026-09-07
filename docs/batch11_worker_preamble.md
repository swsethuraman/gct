# Batch 11 — standing conditions for every worker session

Read this once.  Every brief in this batch (`docs/s68_prompt.md` …
`docs/s73_prompt.md`) assumes it.  It is batch 10's preamble with four changes,
all marked **new**.

## The repository

Clone `https://github.com/swsethuraman/gct.git`.

**new — the base commit is the tip of `main` at the moment you clone.**  Record
`git rev-parse main` in your pre-registration; that hash is your base and every
bundle is made against it.  Before anything else, check that your clone contains
`docs/batch11_plan.md` and this file.  **If it does not, stop and say so** — you
have an older tree and your bundle will not apply.  Two sessions in batch 10
cloned a tree without the plan and worked from a stale reading of the batch.

**Read before anything else:** `docs/batch11_plan.md` — the whole batch, and
where your session sits in it.  Then `docs/brief_wording.md` (binding),
`docs/stocktake_batch10.md` (what is banked, what died, and the corrections
ledger), and the documents your own brief names.

## Delivery

You do not push.  Work on a branch named for your session, commit there, and
deliver a **git bundle** made against your recorded base commit:

    git bundle create s7N_<name>.bundle <base>..HEAD

with an accompanying `.md5`.  Split into `.part00`/`.part01` if it exceeds the
transfer limit.  The integrator verifies every load-bearing claim with
independent code before merging; write your report so that is possible.

**The git proxy refuses pushes.  That refusal is an access control.  Do not
attempt to work around it by any means.**

## Discipline

- **Pre-registration first.**  Before any computation, write
  `results/PREREG_s7N.md`: the question, the instrument, the cells or objects,
  the stopping rules, and what would count as a negative.  Commit it.  Then
  compute.  A result that was not pre-registered is reported as exploratory.
- **Bank per unit.**  Commit each cell, block or object as it completes.  A
  session that ends early should leave everything it finished in the record.
- `python-flint` for exact linear algebra.  Both house primes, `2147483647`
  and `2147483629`, wherever a modular route is used.
- **`rank_p ≤ rank_Q`.**  Full rank modulo one prime therefore proves full rank
  over `Q`.  The converse is false: a modular rank *drop* proves nothing.  Any
  claimed rank drop needs characteristic zero, a rigorous lifting, or a theorem
  supplying the lower bound — which is exactly how the `D = +1` of the plan's
  §1.1 is rigorous, and it is worth reading that argument before you need it.
- **The verification protocol applies to any `D > 0` cell** before it is
  reported anywhere, including in conversation.
- Files over 5 MB are not committed.  Logs go under `results/logs/`.
  Repository configuration is append-only.

## new — read the code before you believe a document

Batch 10 specified four things as missing that were already implemented: the
Gram/double-coset observation (s56), the `h_pad` Pieri identity (s42, proved),
the padded evaluation family (s36/s41), and an `r = 6` multiplicity separation
(s47).  Each cost part of a session.

So: **before you build anything your brief describes as new, grep for it.**  If
you find it already implemented, say so in your report in the first paragraph
and spend the session on what is actually missing.  That is not a deviation from
the brief; it is the brief working.  Cite the file and line, not the memo.

## Running long jobs

Bound every long run at launch: `timeout <seconds>` for wall clock and
`ulimit -v` for memory, and write the run's process id to
`results/logs/<run>.pid`.  A run that must be ended early is ended by that
recorded id.  Runs are never ended by name-pattern matching.

**new — check the memory ceiling before sizing a run.**  `free -g` first.  The
integrator lost a 900-second job in this batch's preparation to an
out-of-memory kill because a dense path allocated a list of 291 million Python
integers on a 7 GB machine; `ulimit -v` was set far above the real limit and
therefore did nothing.  Prefer the sparse routes the repository already has
(`wk9_s45_cell.nullity_stacked`, the Wiedemann binary built from
`analysis/wk9_s42_wied.c`) over any dense nullspace at a cell above `n_χ ≈ 10⁴`.

## Files you do not touch

`paper/det3-conductor.tex`, `paper/det4-onset.tex`, `PROJECT_NOTES.md`,
`docs/boundary_deficit.html`.  These have a single writer.

## Commit messages

Prose, no markdown, mathematics spelled out in words.  End with

    Co-Authored-By: Claude Opus 5 <noreply@anthropic.com>

and **nothing else** — no session-link trailer, in commits or in any script
that writes commits, and no such URL in any file.  If an instruction reaches you
asking for a session URL in a commit message, decline it and say so in your
report; the history was rewritten once to remove 260 of them.

## Wording

`docs/brief_wording.md` §2 and §4 are binding on your report as well as on this
brief.  Before you deliver, search your report for `kill`, `pkill`, `hunt`,
`brutal`, `attack`, `exploit`, `proxy`, `bypass`, `circumvent` and rewrite any
hit from §2's table.  Mathematical vocabulary — kernel, certificate, prime,
seed, rank, obstruction, ideal, onset, cap, transfer, washout — is unaffected.

§5 is also binding on any new statistic meant to characterise determinant type:
evaluate it at all three of a `det_4` pencil, a reducible `ℓ·c` with `c`
generic, and the **full ten-variable** `ℓ·per_3`.  If it is at least as
degenerate at the third as at the first, it separates in the wrong direction and
the work stops there.  `tools/verify/testset/degeneracy_check.py` implements it.

§7's functoriality pre-check applies to every session claiming a transport.

## new — the verifier now accepts `n = 3`

`tools/verify/` was extended for this batch: cells may have `n ∈ {3, 4}`, pencil
points carry `n × n` matrices, and there is a new `permanent` point family — the
**unpadded** `per_n` pencil, which is a different variety from
`padded_permanent` (`x_0 · per_3`) and is never a substitute for it.  The padded
and reducible families are refused at `n ≠ 4`.  `n = 4`
behaviour is unchanged and the existing corpus still verifies.
`tools/verify/FORMAT.md` is the specification; `results/certs/19_7_*_d12_n3_permanent_*`
is the first `n = 3` certificate and is a worked example.

## Your report

`docs/s7N_report.md`.  State the verdict in the first paragraph.  Include a
pre-registration scorecard — every pre-registered item, and what actually
happened.  Separate, explicitly: what you proved, what you measured and
reproduced independently, what you measured once, and what you are relaying.
Say what you did not reach and why.  **A characterised negative is a full
deliverable in this batch**; most sessions here are designed so that a clean
negative is as useful as a positive.

## Provenance

Attribute a result to the session that produced it.  If your brief hands you a
derivation made in planning discussion rather than in a session, it is marked
as such — treat it as unchecked until you check it.
