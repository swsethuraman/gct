# Batch 10 — standing conditions for every worker session

Read this once.  Every brief in this batch (`docs/s62_prompt.md` …
`docs/s67_prompt.md`) assumes it.

## The repository

Clone `https://github.com/swsethuraman/gct.git`.  **Base commit for this batch
is `226b4ef1`** — every pre-registration names it.  Older base hashes
(`0960bd5` and its generation) were removed by a history rewrite at the batch
boundary and resolve only in a private archive; do not cite them.

**Read before anything else:** `docs/batch10_plan.md` (the whole batch, and
where your session sits in it), `docs/brief_wording.md` (binding), and the
documents your own brief names.

## Delivery

You do not push.  Work on a branch named for your session, commit there, and
deliver a **git bundle** made against the base commit:

    git bundle create s6N_<name>.bundle 226b4ef1..HEAD

with an accompanying `.md5`.  Split into `.part00`/`.part01` if it exceeds the
transfer limit.  The integrator verifies every load-bearing claim with
independent code before merging; write your report so that is possible.

## Discipline

- **Pre-registration first.**  Before any computation, write
  `results/PREREG_s6N.md`: the question, the instrument, the cells or objects,
  the stopping rules, and what would count as a negative.  Commit it.  Then
  compute.  A result that was not pre-registered is reported as exploratory.
- **Bank per unit.**  Commit each cell, block or object as it completes.  A
  session that ends early should leave everything it finished in the record.
- `python-flint` for exact linear algebra.  Both house primes, `2147483647`
  and `2147483629`, wherever a modular route is used.
- **`rank_p ≤ rank_Q`.**  Full rank modulo one prime therefore proves full rank
  over `Q`.  The converse is false: a modular rank *drop* proves nothing.  Any
  claimed rank drop needs characteristic zero or a rigorous lifting.
- **The verification protocol applies to any `D > 0` cell** before it is
  reported anywhere, including in conversation.
- Files over 5 MB are not committed.  Logs go under `results/logs/`.
  Repository configuration is append-only.

## Running long jobs

Bound every long run at launch: `timeout <seconds>` for wall clock and
`ulimit -v` for memory, and write the run's process id to
`results/logs/<run>.pid`.  A run that must be ended early is ended by that
recorded id.  Runs are never ended by name-pattern matching.

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

## Your report

`docs/s6N_report.md`.  State the verdict in the first paragraph.  Include a
pre-registration scorecard — every pre-registered item, and what actually
happened.  Separate, explicitly: what you proved, what you measured and
reproduced independently, what you measured once, and what you are relaying.
Say what you did not reach and why.  **A characterised negative is a full
deliverable in this batch**; several sessions here are designed so that a clean
negative is as useful as a positive.

## Provenance

Attribute a result to the session that produced it.  If your brief hands you a
derivation made in planning discussion rather than in a session, it is marked
as such — treat it as unchecked until you check it.
