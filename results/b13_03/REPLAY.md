# B13-03 replay

board_numbering: batch13
session_id: B13-03

Run from either the B13-03 checkout or the user delivery directory, which retains
the same analysis/results paths. The two S4 control inputs are supplied with the
delivery. CPython 3.12+ suffices for production; NumPy is used only by the separate
verifier. No flint, compiler, network, or other Batch 13 session is needed.

On this Windows host:

```powershell
$B13Python = 'C:\Users\swami\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe'
& $B13Python -u analysis/b13_03_bound.py --name b13_03_replay_complete --seconds 600 --memory-mb 768 analysis/b13_03_exact.py --cell '4:3:6:8,8,8' --full --output results/b13_03/replay_complete.json
& $B13Python -u analysis/b13_03_bound.py --name b13_03_replay_mixed --seconds 600 --memory-mb 768 analysis/b13_03_exact.py --input results/b13_03/mixed_source.json --full --output results/b13_03/replay_mixed.json
& $B13Python -u analysis/b13_03_bound.py --name b13_03_replay_independent --seconds 600 --memory-mb 768 analysis/b13_03_verify.py
```

Expected: source dimension 2, restriction rank 1, kernel `(1,0)` in the complete
source; kernel `(1,-1)` in the mixed source; independent verifier PASS. The mixed
CLI input represents an explicit source; completeness comes from the separately
certified primary control. Every value is stored with its coefficient convention.

To reproduce all preregistered calculations, invoke `analysis/b13_03_controls.py`
through the same bounded runner with final argument `tiny`, `primary`, or `r5`.
This regenerates the named artifacts and their timing fields. Preserve the frozen
delivery separately before replay if its checksums must remain unchanged.

`analysis/b13_03_exact.py` is portable; `analysis/b13_03_bound.py` is Windows
specific. On another platform, launch the portable computation under that
platform's memory/time limits. No claim is made about large cells beyond the
explicit builder and term caps. The code intentionally errors on a missing
coordinate, inconsistent weight, non-rational coefficient or non-HW shortcut
input. A finite sampled deficiency is never an accepted membership certificate.

Bundle application after checksum verification, in a repository containing the
frozen base:

```powershell
git bundle verify b13_03_exact_reducible_membership.bundle
git fetch b13_03_exact_reducible_membership.bundle b13-03:review-b13-03
```

There is one byte-identical part, `.bundle.part00`. The `.bundle.md5` and
`.bundle.sha256` files contain bare filenames for both the complete bundle and
the part. The delivery manifest records the final branch commit, base, part count,
all file hashes, and bundle verification. No push or merge is part of replay.
