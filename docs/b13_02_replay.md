---
board_numbering: batch13
session_id: B13-02
---

# Replay and bounded resumption

Run from the isolated checkout. Python integers suffice for the coefficient
maps; NumPy is additionally required for the fresh dimension calculation.
The launcher enforces a 768 MiB Windows Job Object limit, sets all BLAS thread
counts to one, records its child PID, checks absolute wall deadlines in parent
and child, and returns nonzero on a deadline status. Replays rewrite their own
derived result files, including timings; retain the delivered hashes separately.

```powershell
$B13Python = 'C:\Users\swami\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe'
& $B13Python analysis/b13_02_run.py b13_02_audit_replay audit --seconds 120
& $B13Python analysis/b13_02_run.py b13_02_controls_replay controls --seconds 120
& $B13Python analysis/b13_02_run.py b13_02_taller_replay taller_controls --seconds 120
& $B13Python analysis/b13_02_run.py b13_02_dimensions_replay dimensions --seconds 600
& $B13Python analysis/b13_02_run.py b13_02_verify_replay verify --seconds 60
```

The first missing coefficient is column 2, row 29. This resumes at most eight
new coefficient attempts and retains all 31 completed entries, without treating
the interrupted entry as zero:

```powershell
& $B13Python analysis/b13_02_run.py b13_02_resume02 pilot --arg '2:resume:8' --seconds 60
```

Do not equate completion of this column with completion of S: all five columns
are only a coordinate projection. A rational ideal certificate requires the
entire symbolic restriction to vanish in characteristic zero.

The source restriction artifact refers to s74's unmodified source order. Its
house-symbol transport is `(24*d_(3,0^8))^(24-native_degree)`. The partial matrix
uses ordinary cubic coefficient monomials, with `null` explicitly uncomputed.

Verify the delivered bundle with `git bundle verify` in a repository containing
the frozen base. The part00 file is the sole part and is byte-identical to the
whole bundle. The `.md5` and `.sha256` list bare filenames for both. All JSON
manifests carry board_numbering and session_id; the delivery manifest records
the final commit and the whole-file and part checksums.
