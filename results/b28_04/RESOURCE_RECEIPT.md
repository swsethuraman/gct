# B28-04 resource receipt

Producer: Claude Code (Opus 5.5), default permission mode, 2026-09-28. Host: Windows 11, Python 3.12.10.
There was no TeX toolchain and no installs. All runs were sequential, and each was far below 60 s and 512 MB.
Wall times appear here only and appear in no output file.

These runs are administrative text operations: string replacement and a static source scan. None
is a mathematical computation, so none produces a COMPUTED claim. They are logged because
`B28_COMMON.md` requires every script run to be logged. Runs used: 5 of 10.

| run | command (from `work/batch28`) | inputs (raw sha256) | output (raw sha256) | wall |
|---|---|---|---|---|
| 1 | `python b28-04-p2/analysis/b28_04_apply_edits.py <draft> b28-04-p2 b28-04-p3` (dry run, stdout to a temp file) | script `98e737e9…85f3`; draft `5d8f4012…8663`; the six setup-commit files (before hashes in `apply_record.json`) | temp `bafb982b…71d5` (not kept). It is identical in content to run 2's record except for `"applied_to_disk": false`, and it has CRLF line endings because stdout is in text mode on Windows | 0.68 s |
| 2 | same, with `--apply --out b28-04-p2/results/b28_04/apply_record.json` | same | `apply_record.json` `cebcf921a0fb343992afe595205d4aa4b19ff24f05b90d5b6bb51d942358f2f7` (written as binary, LF) | 0.63 s |
| 3 | `python b28-04-p2/analysis/b28_04_static_check.py . > …/static_check.txt` | a first adaptation of `analysis/b27_04_static_check.py` | none: Python `SyntaxError` (a mangled backslash escape in the added macro check). Those script bytes were overwritten and not kept | 0.64 s |
| 4 | same | second adaptation | none: `SyntaxError` again, from the same line | 0.63 s |
| 5 | same | script `7c2c907ad17587ac07d90651a9d548d30ba702bd358cee69000afc3309dc0a6b`; setup blobs `65060dea:paper/det4-onset.tex`, `ff1d4772:papers/det4-blindness/det4-blindness.tex`; worktree after-states (hashes in `apply_record.json`) | `static_check.txt` `0cd9a356b1e7c661c7b41b8c780eeb342a2568eec3acbb6e14466f486586fd83` (stdout, so CRLF on Windows) | 0.69 s |

Replay: run 2 reproduces `apply_record.json` byte for byte from the setup-commit files. It must be
run against clean setup-commit checkouts, because on already-edited files every FIND is absent and
each step reports STOPPED. Run 5 reproduces `static_check.txt` on Windows. Elsewhere, stdout gives
LF, so the content matches and only the line endings differ.

Other operations were Git plumbing and not script runs: `git diff --no-color` to `paper2.diff`
and `paper3.diff`, `git hash-object`, `sha256sum`, commit and push.
