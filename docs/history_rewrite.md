# The one-pass history rewrite

Prepared before the run; this page is the record of what it changes and why.

## What it fixes, in a single `git-filter-repo` pass

| # | defect | where | count |
|---|---|---|---|
| 1 | UTF-8 byte-order mark leading the commit message | the s47 and s48 merge commits | 2 |
| 2 | `h_pad >= 19` should read `h_pad >= 9` | the s47 merge message | 1 |
| 3 | `Claude-Session:` trailer lines and bare `claude.ai` URLs | throughout | 260 commits |
| 4 | blobs over the 5 MB repository limit | see below | 4 |

**On (1).**  Windows PowerShell's `Set-Content -Encoding utf8` writes UTF-8
*with* a BOM, and `git commit -F` kept it in the message.  Use
`[IO.File]::WriteAllText($path, $text)` instead, or PowerShell 7's
`-Encoding utf8NoBOM`.

**On (2).**  19 is the *first* counterexample's `h_pad`; the minimum over the
five is 9, which is what `results/sixrow_record.md` states.  The record was
always right; only the merge message was wrong.

**On (4).**  Three of the four are the session-36 padded-side records at
`(8,8,8,2,2)`, `δ = 7`.  These were **gzipped in an ordinary commit before the
rewrite** (about seventeen-fold, all under 0.75 MB — see
`results/s36_cells/README.md`), so the data is preserved in the tree and only
the uncompressed history blobs are stripped.  The fourth, `lev6.dat` (6.0 MB),
was deleted from the tree long ago and survives only in the pack.

## Why one pass and not four

Every one of these needs history rewritten, which changes every commit hash
from the earliest affected commit forward.  Doing them separately would mean
several force-pushes to a public repository, each breaking every existing
clone.  The blob compression was done first as an ordinary commit precisely so
that it did *not* need the rewrite; everything that genuinely does need it goes
in one pass.

## How to run it

On a **fresh clone**, never on a working repository:

    git clone --no-local https://github.com/swsethuraman/gct.git gct-rewrite
    cd gct-rewrite
    bash tools/rewrite/run_rewrite.sh

The script prints its own post-conditions: zero BOMs, zero `h_pad >= 19`, zero
session links, zero blobs over 5 MB, and the commit count unchanged.  Inspect
those, spot-check a few messages, and only then force-push.

Note that `filter-repo` removes the `origin` remote by design, so the push is
explicit:

    git remote add origin <url>
    git push --force origin main

Every existing clone must then be re-cloned; a `git pull` will not recover.

## What it deliberately does not do

- No content of any tracked file is altered.  Only commit messages, and the
  removal of four oversized blobs.
- Author, committer, dates and `Co-Authored-By` trailers are untouched.
- The commit graph is unchanged in shape — same count, same merges.


---

## The second pass: batch 13

Run on `b31a0de`, the batch-13 integration merge over `0049511`.  Same script,
same callback.  The outcome contradicted three of this page's closing claims, so
they are corrected below rather than left quietly standing.

| | before | after |
|---|---|---|
| `main` | `0049511` | `ea2ad30` |
| `integration/batch13` | `b31a0de` | `743d640`, then `a4ba320` with the map |
| commits | 1548 | 1524 |
| commit-map | — | 1549 lines, `results/integrate/batch13_commit_map.txt` |

**What it removed.**  206 session links: 195 new in batch 13 and **11 already
published on `main`** (s71 x3, s72 x8; earliest `28550ce`).  So this pass was
never confined to the integration branch, and `main` had to be force-pushed too.
The defect was message-only: no file on `main` emits a session link, and the
twelve that mention `claude.ai` do so as prose about the rule.

**Two of the four fixes were dead.**  Zero byte-order marks and zero
`h_pad >= 19` remained anywhere in history; the first pass had cleared both.  The
`h_pad` substitution is now retired from the callback -- a one-off content
correction, complete.  The BOM strip stays: PowerShell can reintroduce one at any
time.

### Correction 1 -- the commit count is not preserved

1548 to 1524.  **Nothing is dropped**: every entry in the map points at a real
commit.  24 *pairs* collapse into 24 single commits, because the repository held
two parallel chains of s74/s79 commits identical in tree, author, timestamp and
message, differing only in whether they carried an SSH signature.  Strip the
signature and each pair becomes the same object.  That duplication was
pre-existing and invisible; the rewrite is what surfaced it.

### Correction 2 -- the graph shape is not preserved

Follows from the above.  "Same count, same merges" held for the first pass and
should not have been written as a property of the procedure.

### Correction 3 -- signatures do not survive

`filter-repo` cannot re-sign, and a signature covers the message, so every
rewritten commit loses its SSH signature: **780 of 1548 commits were rewritten
and 647 of those were signed**.  The 768 commits below the earliest contaminated
commit keep both their hashes and their signatures.  This is unavoidable, not a
flag that was forgotten.

### What was verified rather than assumed

Both branch trees are bit-identical before and after: `git diff --stat 0049511
origin/main` is empty, and the batch-13 tip differs from `b31a0de` by exactly the
map file added afterwards.  The rewrite is deterministic -- three independent
runs, two in the integrator's container and one on the author's machine, produced
the same two hashes, which is what let the runner script gate on them.

One object in history exceeded 5 MB, `results/s74/columns_gen_2147483647.json` at
5,886,081 B, already absent from both current trees.  `--strip-blobs-bigger-than
5M` removed it.

### Why a rewrite is re-run at the destination and never shipped

A bundle of the rewritten refs with the old tips as prerequisites selects 8578
objects and 133 MB *even though every tree is shared*: git's uninteresting-marking
does not propagate across two structurally parallel histories, and bundles are
never thin (`--objects-edge-aggressive` only gets to 4462).  Re-running a
three-second rewrite at the destination beats any delivery of it.

## Running it on Windows

`bash tools/rewrite/run_rewrite.sh` does not work from PowerShell.  The batch-13
attempt failed four times before it ran; `tools/rewrite/run_batch13_rewrite.ps1`
is the script that finally did it, kept as the record.  Copy it and change the
four expected-value constants for the next pass.  The traps, in the order they
were hit:

1. **A stale `gct-rewrite` from the previous pass.**  `git clone` refuses a
   non-empty destination -- but the *following* commands ran anyway and committed
   that pass's `.git/filter-repo/commit-map`, 769 lines, from a rewrite two
   batches earlier.  Delete the directory; never reuse it.  A commit-map whose
   line count you have not checked against this run is not evidence of anything.
2. **`bash` is not a PowerShell command**, and Git Bash's own `bash.exe` cannot
   see `git filter-repo` when filter-repo is a user-site pip install, because
   pip's Scripts directory is not on Git Bash's PATH.  Drive it from Python:
   `python -m git_filter_repo` finds the module directly, and Python passes the
   multi-line `--commit-callback` body as one argv element without PowerShell
   mangling its quotes.
3. **`2>&1` on a native command.**  PowerShell turns redirected native stderr
   into error records; with `$ErrorActionPreference = "Stop"` the script dies on
   git's own success chatter ("Already on 'integration/batch13'").  Never
   redirect a native command; check `$LASTEXITCODE` instead.
4. **Deleting the directory you are standing in.**  `Remove-Item` fails with "in
   use" when the shell's working directory is inside it.

Every one of those was survivable except the first, and the first did damage only
because step *n* failing did not stop step *n+1*.  The rule that follows: a
rewrite procedure aborts on the first failed check, and verifies the result
against independently computed expected values before anything is committed or
pushed.
