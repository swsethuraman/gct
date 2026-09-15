# B17-06 delivery

Status: COMPLETE for the assigned bounded contribution; independent review pending.

Read [the report](../../docs/b17_06_report.md) for the cancellation criterion,
proofs, support cost, exact control, and next sufficient test. [MANIFEST.json](MANIFEST.json)
records exact-byte hashes, provenance, resources, and unresolved inputs.

The sole research run passed: degree-five full-entry arc minors -184926 and
32286015, 0.0740545 seconds, 13,541,376 peak Job Object committed bytes.
No positive multiplicity gap or new candidate matrix was produced. A reviewed
new finite cell with global determinant upper B and padding ceiling U>B is
needed before proposing a B+1 minor.

The [standard-library verifier](../../analysis/b17_06_verify.py) and
[exact receipt](../../results/b17_06/control_01.json) are preserved unchanged.
Input snapshots are in `inputs/`; all nineteen were hash-verified in the run.
The existing interpreter and inspected original wrapper are hash-pinned in
the manifest. No historical Hessian arithmetic was rerun.

A separately authorized receiver can run from the assigned worktree, using
a fresh output and log name:

```powershell
& .venv/python.exe -B analysis/b15_bound.py --slot 06 --name b17_06_receiver_fresh --seconds 60 --memory-mb 512 analysis/b17_06_verify.py --output results/b17_06/receiver_fresh.json
```

That replay command is documentation, not an additional run or a new lease.
The original session used its one computation and finalized after inspecting
the saved results on resume. No agent, task, new worktree, commit, push,
publication, or ownership/trust/sandbox change occurred.
