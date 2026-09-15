B17-04 bounded preflight, 13 September 2026.

The single proposed computation checks exact candidate-to-Hessian coefficient
identities and evaluates twelve fixed rational transforms of independent
`z*per3`. This is equation-structure work in the accepted eleven-space.
It does not reopen a multiplicity-excluded cell or form a 429-column
geometric evaluation matrix.

Inspected executable inputs: this worktree's `analysis/b15_bound.py`,
`analysis/b17_04_verify.py`, and the accepted Hessian11 `verify_small.py`.
Claude's harness was read as data; none of its producers is imported or run.

Price: at most 2,500 sparse universal Euler relations on the fixed 1,019
brackets (at most six initial terms each); 25 source vectors, each supported
on at most 1,019 brackets; an 11-by-11 rational change of basis; twelve
points, each with 21 univariate determinant-interpolation nodes and matrix
order at most 11. No determinant expansion in generic matrix entries.
The prior Hessian11 receiver measured 0.5493 seconds for its smaller-height
fourteen-point control. Larger integer heights and generalized straightening
are priced conservatively at 30 seconds and 256 MiB. These are estimates,
not measured guarantees. The hard cap is 60 seconds / 512 MiB.

There is one Python invocation through the existing Job Object wrapper,
one process, one BLAS thread; the wrapper's deadline-monitor thread is not
a computation worker. No heavy lease is requested. A cap hit or a failed
stage means that stage is uncomputed; saved earlier exact certificates
remain available. No repeat or enlargement is authorized by this file.

Command, from the assigned worktree:

```powershell
.\.venv\python.exe -B analysis/b15_bound.py --seconds 60 --memory-mb 512 --name b17_04_verify --slot 04 analysis/b17_04_verify.py
```

An upper bound will use only global identities, never the kernel dimension
of these twelve samples. The inherited shared E3 gives restriction rank
at most ten. A rank-nine minor would initially prove only 9 <= rank <= 10.

Read-only Git observations at entry: branch `b15-04-small-panel`, HEAD
`3d3f9f8b427f257a0d5db678b1645212033652ff`; pre-existing untracked Batch16
and older result files were present. `git status --short` also reported
`warning: unable to access 'C:\Users\swami/.config/git/ignore': Permission denied`.
No trust, ownership, configuration or permission change was attempted.
The Git query still returned its status listing. This warning does not
block independent mathematics. No automatic approval rejection occurred.
