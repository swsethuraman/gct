# B27-05 resource receipt

This was a record-check closure under B27-05 rung 0, registered outcome 4.

- Exact-arithmetic / symbolic / certificate-replay runs: **0 of 10**.
- Mathematical scripts: none. No random search, sampled nullspace, installed package, or new rank calculation.
- The installed-symbolic-tool probe was not needed because the record stop rule fired before a mathematical run was proposed.
- Read-only source operations used installed Git and PowerShell. Git's ownership check was handled by `git -c safe.directory=C:/Users/swami/Projects/gct-gpt/work/batch27/b27-03 -C ...`; no configuration file was written.
- File hashes, byte comparisons, JSON/CSV record selection, text authoring and manifest verification are administrative operations, not mathematical experiments. They make no new arithmetic theorem or rank claim.
- No subagents, other sessions, messages to tasks, publication or automatic continuation.
- Every new filesystem output is confined to `batch27_launch/b27_05_out/`. Existing untracked files were left alone. No Git write, paper, ledger, seal, attributes or ignore edit was made.

## Run log

The mathematical run log is empty. There are no commands, mathematical input/output hashes or measured mathematical wall times to report. Historical timings in REPORT.md are labelled READ and refer to their original committed reports, not to runs in this slot.

## Source and search log

All committed reads used commit `7c36a52ddf338eb390a9bcd491cb9c50cf9e2a19` and worktree `C:/Users/swami/Projects/gct-gpt/work/batch27/b27-03`.

The operative command forms were:

```text
git -c safe.directory=<worktree> -C <worktree> show <commit>:<path>
git -c safe.directory=<worktree> -C <worktree> ls-tree -r --name-only <commit> -- docs analysis results
git -c safe.directory=<worktree> -C <worktree> grep -n/-l -i -E <record topic> <commit> -- <selected paths>
git -c safe.directory=<worktree> -C <worktree> log --all --format=<hash and subject> -- docs/s38_review.md results/occurrence_screen.md
git -c safe.directory=<worktree> -C <worktree> hash-object --no-filters <brief-named file>
git -c safe.directory=<worktree> -C <worktree> cat-file -e <raw-file blob OID>
```

Search topics included stabiliser reduction, first-row reduction, subalgebra, semi-invariants, Foulkes, balanced degree 8/9, and the exact tuples `(12,8,6,4,2)` and `(14,10,6,4,2)`. The scope was the selected committed tree and its relevant history, not a claim to have audited every archived branch or external paper.

The raw-file blob OIDs `f7404197feb3ea9de9dab70e5e3d1376860b31cf` and `77d3aa6cccbf490947b6c82e65b5abca51fd6cbd` were not present in the accessed object store (`cat-file -e` exit 1). The expected SHA-256 files were found and their CRLF-to-LF equality to the committed versions was verified; the brief expressly permits this fallback.

Initial broad file search output was excessive and was replaced with bounded committed-tree searches. Guessed paths `docs/s54_review.md`, `docs/CORRIGENDUM.md` and `CORRIGENDUM.md` did not exist at C; none was a required brief input and none supplies a claim here. Large census output was subsequently narrowed to the exact records saved in `RECORD_EXCERPTS.json`. These lookup issues caused no mathematical run and no write outside the output folder.

## Time and checkpoint

The first clock receipt was `2026-09-23 05:03:54 UTC`, immediately after the initial brief reads. The record check reached the stop rule and the packet was finished before the 45-minute checkpoint. `SESSION_CLOSE.json` records the final clock receipt and the rung dispositions. The 90-minute ceiling was not approached. No later wakeup is scheduled.

## Verification

Input snapshots were obtained through Git's binary stdout stream, preserving their bytes. `INPUT_BINDINGS.json` binds committed blob-content SHA-256 and length, and `FILE_FALLBACK_BINDINGS.json` separately binds the two raw files. Control files are bound in `PREFLIGHT.json` and retained byte-for-byte. Final administrative verification checks each binding, the unchanged control hashes, every payload's manifest hash and byte count, exclusion of MANIFEST.json from itself, and that there are no unlisted payloads.
