# B17-04 authorized continuation, 14 September 2026

The user explicitly conveyed integrator authorization for **one corrected
bounded invocation** of the saved verifier, in this same session/worktree,
at most60 seconds/512MiB, one process and one BLAS thread through the
inspected `analysis/b15_bound.py`. This resolves the earlier authorization
blocker. No heavy lease, agents, new worktree, commit, push or publication.
A failure or cap hit will be reported and will not trigger another run.

Before invocation, all49 previously pinned input/artifact/runtime records
were checked against current SHA256 hashes; every record matched. The
complete corrected verifier, wrapper, report, preflight, status, failure
transcript, resource receipt, PID receipt, delivery README and manifest
were inspected. The corrected verifier retains its saved bytes; the only
code change relative to the first source is the explicit rational adapter
already saved in the initial delivery. Historical successful receivers
are not rerun. The imported Hessian source supplies functions for the new
comparison and new twelve-point test; its main replay is not invoked.

The original estimate remains30 seconds/256MiB, with hard60s/512MiB limits.
It is an estimate for unreached stages, not a measured successful pilot.

The unique receipt prefix is `b17_04_retry_20260914_01`; existing files
with that prefix are checked before invocation. Command:

```powershell
.\.venv\python.exe -B analysis/b15_bound.py --seconds 60 --memory-mb 512 --name b17_04_retry_20260914_01 --slot 04 analysis/b17_04_verify_next.py
```

Current inputs, including the corrected source, are pinned before running.
The original input manifest, report, status and delivery envelope are
archived in owned b17_04 paths before current status updates. The first
failed source and all its log receipts remain unchanged.
