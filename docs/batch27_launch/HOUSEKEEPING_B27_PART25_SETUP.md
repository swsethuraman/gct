# Batch 27 — PART 25: batch-start setup (branches, worktrees, one attribute rule)

**STATUS: READY.** Run this in a Claude Code session in **default permission mode**. It is the
only housekeeping pass before the batch starts. It creates the slot branches and worktrees so
that producers can commit their own work. It assesses no mathematics and edits no packet or
paper.

Read `batch27_launch/B27_COMMON.md` for conventions. **In this pass only**, the Git prohibitions
are lifted for exactly: branch creation, `git worktree add`, the attribute commit on each new
branch, and `push -u` of each new branch.

## §0 — Author decisions (given 2026-09-23)

Create the branches, add the worktrees, make the attribute commit, and push: **YES.**

## Branches to create

For each row below:

1. Confirm the base tip with `git ls-remote`.
2. If the actual tip is a descendant of the expected tip, use the actual tip and record it. If
   the base has diverged in any other way, stop that row.
3. Run `git branch <new> <base-tip>`.
4. Run `git worktree add <path> <new>`.

| new branch | base | expected base tip | worktree path |
|---|---|---|---|
| `b27-01` | `batch15-launch` | `f7967d17935d6256e7744f6457b45a3787b6940f` | `work/batch27/b27-01` |
| `b27-02` | `batch15-launch` | same | `work/batch27/b27-02` |
| `b27-03` | `batch15-launch` | same | `work/batch27/b27-03` |
| `b27-01r` | `batch15-launch` | same | `work/batch27/b27-01r` |
| `b27-02r` | `batch15-launch` | same | `work/batch27/b27-02r` |
| `b27-03r` | `batch15-launch` | same | `work/batch27/b27-03r` |
| `b27-k4r` | `batch15-launch` | same | `work/batch27/b27-k4r` |
| `b27-04-p1` | `b23-05-paper1` | `af8468f34fb67b1c647b448e4a0c82085ddaba13` | `work/batch27/b27-04-p1` |
| `b27-04-p2` | `b24-06-paper2` | `721d54a2afc1e0a89eacd3e1e9bf5a78cea12dce` | `work/batch27/b27-04-p2` |
| `b27-04-p3` | `b23-04-paper3` | `0a8029bbb13fae7995f0406c6b5a5a3f2daf8a6e` | `work/batch27/b27-04-p3` |

## One attribute commit per new branch

Append these three lines to `.gitattributes`, matching the line endings the file already uses:

```
docs/b27_* -text whitespace=cr-at-eol
results/b27_*/** -text whitespace=cr-at-eol
analysis/b27_* -text whitespace=cr-at-eol
```

- Commit message: `Batch 27 setup: byte-preserving attributes for b27 outputs`.
- Record each setup commit's SHA; slots use it as their expected HEAD.
- Make no other change. When a permission prompt appears for `.gitattributes`, the user approves
  it once per branch.

## Push

For each new branch, run `git push -u origin <new>` and confirm it with `ls-remote`. **Never push
to any base branch.**

## Deliverables

Write these to `Claude_Handover_B15_B18\post_b19_housekeeping_20260917\`:

- `B27_PART25_SETUP_RECEIPTS.json`, with, for each row: base tip, setup commit SHA, worktree
  path, and push confirmation.
- `B27_PART25_SETUP_REPORT.md`, at most 50 lines.

Then stop. **No slot is launched by this pass.**
