# Batch 28 — PART 27: batch-start setup (branches, worktrees, one attribute rule)

**STATUS: READY.** Run this in a Claude Code session in **default permission mode**. It is the
only housekeeping pass before the batch starts. It assesses no mathematics and edits no packet,
paper, ledger or seal.

Read `batch28_launch/B28_COMMON.md` for conventions. **In this pass only**, the Git prohibitions
are lifted for exactly: branch creation, `git worktree add`, the attribute commit on each new
branch, and `push -u` of each new branch.

## §0 — Author decisions (given 2026-09-24)

Create the branches, add the worktrees, make the attribute commit, and push: **YES.**

The coordinator's Batch 27 ledger is **not** in this pass. It goes in the Batch 28 close pass.

## Branches to create

For each row below:

1. Confirm the base tip with `git ls-remote`.
2. If the actual tip is a descendant of the expected tip, use the actual tip and record it. If
   the base has diverged in any other way, stop that row.
3. Run `git branch <new> <base-tip>`.
4. Run `git worktree add <path> <new>`.

| new branch | base | expected base tip | worktree path |
|---|---|---|---|
| `b28-01` | `batch15-launch` | `96a8074d240033161302233672aed5980d84eccb` | `work/batch28/b28-01` |
| `b28-01r` | `batch15-launch` | same | `work/batch28/b28-01r` |
| `b28-02` | `batch15-launch` | same | `work/batch28/b28-02` |
| `b28-03` | `batch15-launch` | same | `work/batch28/b28-03` |
| `b28-04-p2` | `b24-06-paper2` | `f8326974a1454ac83a925860635e29bbfaf5d5c7` | `work/batch28/b28-04-p2` |
| `b28-04-p3` | `b23-04-paper3` | `4c5a54501bb046b236239fdbcff19556a317655c` | `work/batch28/b28-04-p3` |

## One attribute commit per new branch

Append these three lines to `.gitattributes`, matching the line endings the file already uses:

```
docs/b28_* -text whitespace=cr-at-eol
results/b28_*/** -text whitespace=cr-at-eol
analysis/b28_* -text whitespace=cr-at-eol
```

- Before appending, confirm that no line mentioning `b28` exists yet, and that no tracked path
  matches the new patterns.
- Commit message: `Batch 28 setup: byte-preserving attributes for b28 outputs`.
- Record each setup commit's SHA; slots use it as their expected HEAD.
- Make no other change. When a permission prompt appears for `.gitattributes`, the user approves
  it once per branch.

## Push

For each new branch, run `git push -u origin <new>` and confirm it with `ls-remote`. **Never push
to any base branch.**

## Deliverables

Write these to `Claude_Handover_B15_B18\post_b19_housekeeping_20260917\`:

- `B28_PART27_SETUP_RECEIPTS.json`, with, for each row: base tip, setup commit SHA, worktree
  path, and push confirmation.
- `B28_PART27_SETUP_REPORT.md`, at most 50 lines.

Then stop. **No slot is launched by this pass.**
