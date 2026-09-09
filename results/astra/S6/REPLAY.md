# Replaying the S6 audit

The audit builder is read-only with respect to the durable checkout and frozen
S1–S4 deliveries.  It writes only generated JSON files in this S6 directory.
The isolated S2 replay has already been materialized under `replays/s2`.

```powershell
$python = 'C:\Users\swami\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe'
$env:PYTHONDONTWRITEBYTECODE = '1'
& $python 'C:\Users\swami\Projects\gct-gpt\Batch12_Results\S6\src\s6_audit.py'
```

Expected top-level result: `PASS_WITH_OPEN_TARGETS`.  All S1–S4 frozen manifests,
S1/S3/S4 direct certificate checks, and the stable recount should pass.  The
general repository self-test is expected to remain `BLOCKED_BEFORE_TESTS` until
`python-flint` is available; this is calibration debt, not a session-specific
certificate failure.

Do not rerun `S1/verify_n3_minors.py` in the frozen directory: despite its name,
it rewrites `n3_independent_minors.json`.  The audit records the one such incident
and its byte-for-byte restoration from `S1_artifacts.zip`.
