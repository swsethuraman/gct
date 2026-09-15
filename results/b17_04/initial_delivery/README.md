B17-04 delivery: see `docs/b17_04_report.md` for exact conventions, proofs,
fresh/inherited distinctions, failure and limitations. `MANIFEST.json` binds
the input and output files and records the sole capped invocation.

The original failed source `analysis/b17_04_verify.py` is preserved.
`analysis/b17_04_verify_next.py` changes only the rational matrix boundary:
each Python rational becomes `flint.fmpq(numerator,denominator)` before
construction. It is unexecuted. No claim is made that all remaining stages
pass or that its runtime estimate has been measured.

The user allowed at most one computation for this contribution. An integrator
must authorize another before the following command is run. This file does
not issue that authorization or a heavy lease.

```powershell
.\.venv\python.exe -B analysis/b15_bound.py --seconds 60 --memory-mb 512 --name b17_04_verify_next --slot 04 analysis/b17_04_verify_next.py
```

Run from the existing assigned B15-04 worktree. The report's next sufficient
test requires exact candidate identities and a nonzero rank-nine minor;
sampled kernel vectors remain unproved until their global identities are
established. No full429-space rank production or external harness is run.
