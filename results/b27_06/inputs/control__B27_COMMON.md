# Batch 27 — common rules (all slots)

**Status: in force for Batch 27.** Written by the integrator, 2026-09-23. The operating changes
were approved by the user on 2026-09-23. A slot is authorized when the user pastes its one-line
launch (see `BATCH27_BOARD.md`). Where a slot brief and this file differ, the slot brief governs.
Astra sessions ignore the "Claude Code" line below and otherwise follow this file.

## Session and workspace

- **Session:** Claude Code or Astra, in **default permission mode**. The project root is
  `C:\Users\swami\Projects\gct-gpt`, which is not a Git repository. Run Git as
  `git -C <your worktree>`.
- **Your own branch.** Each slot has its own branch and worktree, prepared by PART 25 (see the
  board). Only you write to it. All worktrees share one object store, so read any committed input
  with `git show <commit>:<path>`.
- **Preflight:**
  - Record the raw SHA-256 of this file, of your brief and of `BATCH27_BOARD.md`.
  - Confirm your branch, and that its HEAD is PART 25's setup commit for your slot.
  - Leave untracked files alone.
  - Confirm your output paths do not exist.
  - If anything is wrong, stop and report.

## Inputs and labels

- **Mathematical premises come only from committed blobs.** State which bytes each hash names.
- **Tool memory and paraphrases are not evidence.**
- **Label every claim at its point of use** with one of:
  - **READ**: you read the committed text;
  - **PRIMARY**: an external source you read, with version, locator and hash;
  - **HAND**: your own derivation;
  - **COMPUTED**: see below;
  - **UNREAD**.

## Compute allowance (new in Batch 27)

**What is allowed:**
- Exact arithmetic and symbolic algebra: rational or finite-field arithmetic, polynomial
  identities, small exact linear algebra.
- Use only tools already installed. Check with `python -c "import sympy"`, or Sage if present.
  **No installs.** If nothing is available, work by hand and say so.
- At most **10 runs per session**, each at most **60 s and 512 MB**, run sequentially.
- **Verification first.** Allowed: checking a claimed identity or value, replaying a certificate,
  and exhaustive checks up to a stated bound.
- **Not allowed:** random searches, sampled nullspaces, and any result that is a guess rather
  than a certificate.

**How to record it:**
- Every script goes in `analysis/b27_<slot>_*.py`. Log each run in the resource receipt with its
  command, input hash, output hash and wall time.
- A result obtained this way is labelled **COMPUTED**, never PROVED. It can support a hand proof
  or serve as a finite certificate. Reviewers re-run it.
- Anything larger needs a priced preregistration and the user's approval.

## Standing conventions (updated from Batch 26)

- **Four achievements stay distinct:** source condition, coefficient equation, separation on
  padding, positive multiplicity gap. Geometric noncontainment and asymptotic bounds are further
  labels.
- **Binding constraint, exact wording:** "No five-row determinant equation is known to be
  nonzero on padding."
- **Accepted, cross-lineage (Batch 26):**
  - A26-01, symmetric padding is a determinant (`7464a2bd`).
  - The smooth-cubic exclusion `lC ∉ D₄,₅` (B17-01; C1 closed by the user's ruling; G-A1 closed
    for smooth cubic factors only).
  - B26-02: the expander family is rejected member by member (`cdf6839c`).
  - A26-03 plus the corrected statement: at n=4, every single fully paired, distinct-label tableau
    is nonzero on `Q² = det K_Q` (`f7967d17`, `a7b7c19f`).
  - B26-04: the r=9 quartic transfer (`65736d9f`, `21816b3c`).
- **Reopening condition for tableau separators.** A separator needs a column with no identical
  partner, or a mixed-sign combination. This is necessary, not sufficient. Any actual-padding
  witness must break symmetry.
- **Application 3:** the ceiling is proved; the floor is CERTIFIED-modular.
- **C45:** PROVED at δ=12 only.
- **A25-10's decision stands:** no construction ready.
- **Integrator suggestions are 0 for 3.** Briefs pose questions; the producer owns the method.

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
- edit papers, except in slot B27-04;
- edit ledgers or seals.

In your final message, give the commit SHA and the manifest hash, and state your outcome on each
rung and the achievement level.

## Prohibitions

No subagents or other sessions. No messages to other tasks. No publication. No automatic
continuation.
