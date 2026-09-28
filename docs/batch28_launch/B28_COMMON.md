# Batch 28 — common rules (all slots)

**Status: in force for Batch 28.** Written by the integrator on 2026-09-24. A slot is authorized
when the user pastes its one-line launch (see `BATCH28_BOARD.md`). Where a slot brief and this
file differ, the slot brief governs. Astra sessions ignore the "Claude Code" line below and
otherwise follow this file.

## Session and workspace

- **Session:** Claude Code or Astra, in **default permission mode**. The project root is
  `C:\Users\swami\Projects\gct-gpt`, which is not a Git repository. Run Git as
  `git -C <your worktree>`.
- **Your own branch.** Each slot has its own branch and worktree, prepared by PART 27 (see the
  board). Only you write to it. All worktrees share one object store, so read any committed input
  with `git show <commit>:<path>`. The Batch 27 records are on `batch15-launch` at `96a8074d`.
- **Preflight:**
  - Record the raw SHA-256 of this file, of your brief and of `BATCH28_BOARD.md`.
  - Confirm your branch, and that its HEAD is PART 27's setup commit for your slot.
  - Leave untracked files alone.
  - Confirm your output paths do not exist.
  - If anything is wrong, stop and report.

## Inputs and labels

- **Mathematical premises come only from committed blobs, or from PRIMARY sources.** State which
  bytes each hash names.
- **Tool memory and paraphrases are not evidence.**
- **Label every claim at its point of use** with one of:
  - **READ**: you read the committed text;
  - **PRIMARY**: an external source you read, with version, locator and SHA-256. Third-party
    files are bound by hash and **never committed**;
  - **HAND**: your own derivation;
  - **COMPUTED**: see below;
  - **UNREAD**.

## Compute allowance (unchanged from Batch 27, except B28-01)

- Exact arithmetic and symbolic algebra only.
- At most **10 runs per session**, each at most **60 s and 512 MB**, run sequentially.
- **No installs**, except in B28-01, whose brief sets its own resources.
- **Not allowed:** random searches, sampled nullspaces, and any result that is a guess rather
  than a certificate.
- Every script goes in `analysis/b28_<slot>_*`. Log each run in the resource receipt with its
  command, input hash, output hash and wall time.
- **New in Batch 28:**
  - Keep wall-clock times and other nondeterministic fields **out of certificate and output
    files**. Put them in the receipt only. That way a replay reproduces the output bytes exactly
    (R27-03's lesson).
- Results obtained this way are labelled **COMPUTED**, never PROVED. Reviewers re-run them.

## Standing conventions (updated from Batch 27)

- **Four achievements stay distinct:** source condition, coefficient equation, separation on
  padding, positive multiplicity gap. Geometric noncontainment, existence of an equation in a
  cell, and asymptotic bounds are further labels.
- **Binding constraint, exact wording:** "No five-row determinant equation is known to be nonzero
  on padding."
- **Programme decision:** "no construction ready."
- **Accepted in Batch 27, cross-lineage** (see `docs/batch_closes/BATCH27_CLOSE.md` at
  `96a8074d`):
  - The padding map: certified inside 45–49, certified outside 50, unresolved 49.
  - `T*` and `T′` are certified outside `D₄,₅`, via smooth cubic factors and C1.
  - `p₄` lies in `D₄,₅`, so it is **retired** as a test point.
  - B27-02's candidate is rejected.
  - B27-03's zero kernels: `k ≤ 4`, two degree-8 weights, two rays.
  - B26-10A §2.3, the general degree-4 statement and the `P_r` identification.
- **Padding test points:** any point offered as a separation witness must carry its own proof
  that it is not in `D₄,₅`. Use `T*` or `T′`, or certify a new one.
- **Application 3:** the ceiling is proved; the floor is CERTIFIED-modular.
- **Integrator suggestions are 0 for 4.** Briefs pose questions; the producer owns the method.

## Ladders

Each slot has ordered sub-questions. When one resolves early, with a proof, a certified negative
or an exact obstruction, **move on to the next rung** instead of stopping. Stop at the ceiling, or
when a rung's stop rule fires.

## Commit and push (your branch only)

At the end:
1. Write `MANIFEST.json`, binding every payload's raw SHA-256 and bytes and excluding itself.
2. Stage your output paths **by explicit path**. Confirm
   `git hash-object <p> == git hash-object --no-filters <p>` for each one.
3. Make one commit, then `git push origin <your branch>`.
4. Confirm the push with `ls-remote`.

**Never:**
- touch another branch;
- merge, rebase, amend, reset, clean, check out, or use `-f` or `-A`;
- edit `.gitattributes` or `.gitignore`;
- edit papers, except in slot B28-04;
- edit ledgers or seals.

In your final message, give the commit SHA and the manifest hash, and state your outcome on each
rung and the achievement level.

## Prohibitions

No subagents or other sessions. No messages to other tasks. No publication. No automatic
continuation.
