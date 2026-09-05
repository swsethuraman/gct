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
