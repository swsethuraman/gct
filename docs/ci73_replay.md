# Replay the degree-13 certificate

Use a repository containing the bundle prerequisite
`9898e56941a7665f231873481dae956f08509995` (tree
`cb688cd3fe454d638f3202e759e2eaa0c629739f`). The delivery has a named ref
`refs/heads/b14-03-ci73`; it preserves the original B14-03 branch and delivery.
Verify both checksum sidecars and the bundle before importing. From an existing
repository with that base, for example:

```powershell
git bundle verify C:/path/to/b14_03_ci73.bundle
git fetch C:/path/to/b14_03_ci73.bundle b14-03-ci73:b14-03-ci73
git worktree add C:/path/to/ci73-replay b14-03-ci73
Set-Location C:/path/to/ci73-replay
```

All commands below run at that checkout root. No integrator or other worker
directory is needed by the verifier. Paths in provenance records identify
historical inputs only and are not runtime dependencies.

## Build requirements and the minimal full check

The supported bounded replay uses 64-bit Windows, Python 3.12 or newer, and a
C#5-compatible .NET Framework compiler. It requires only Python's standard
library and the Windows Framework assemblies `System.Numerics` and
`System.Web.Extensions`. NumPy, flint, gcc and a native Unix library are not
needed. On the reviewed host, Python 3.12.14 and Framework64 v4.0.30319 `csc.exe`
were used. The compiler defaults to
`C:/Windows/Microsoft.NET/Framework64/v4.0.30319/csc.exe`; set `CI73_CSC` to an
alternative compatible compiler if necessary. Compilation is automatic, with
the executable named by the backend source hash under `results/ci73/cache`.

```powershell
python analysis/ci73_bound.py --seconds 1800 --memory-mb 768 --name ci73_receiver tools/verify/verify.py results/ci73/certificate.json --report results/ci73/receiver_report.md --json-report results/ci73/verification.json
```

Expected: standard verifier **PASS**, exit 0, dimension 39/73, exact source
rank 36, three polynomial kernel equations. Any missing dependency, disagreement,
compiler error or resource failure gives no acceptance. The run starts empty
and freshly evaluates all required source, target and generic witness entries.
It never accepts the stored backend output as an evaluation oracle.
The optional JSON report starts in RUNNING state and records the digest of the
certificate actually consumed; the equation exporter requires that binding.

The checker also works as the direct standard command
`python tools/verify/verify.py results/ci73/certificate.json`; the bounded wrapper
is recommended because it enforces the declared aggregate memory and wall
limits. The backend is compiled from the included source, not supplied as an
opaque binary. The wrapper uses one numerical worker/thread, batches of at most
16 points, an aggregate 768 MiB Windows Job Object and a 120 s child deadline.
It prevents automatic idle sleep while running and releases that request on
exit. Manual suspension cannot turn an elapsed-limit violation into PASS.

The first 73 primary columns form the CI witness; the other 23 primary columns
are only a stored-arithmetic cross-check. Every one of the 20 holdouts is freshly
checked for all 39 source members and all three equations. Read the final
report for measured runtime, actual peak memory and interrupted-run evidence.

## Complete replay and controls

`python analysis/ci73_replay.py` runs the following serially, with expected
exit codes enforced and stdout/stderr retained in `results/logs`:

1. Original B14-03 producer, all 97 original controls, independent small-profile
   verification, and normal-dispatcher positive and negative tests.
2. Literal mixed tests (192 comparisons spanning three independent directions),
   the source15 benchmark, and the forced Chow rank-zero control.
3. The standard degree-13 verifier CLI path on the authentic certificate,
   including a complete fresh polynomial replay and JSON report. The same
   process then runs the new adversarial tests and positive rational-rescaling
   and alternate-completing-source controls. It memoizes only polynomial values
   freshly computed during that process's authentic verification.
4. Separate inherited S74 minor arithmetic replay, and explicit equation export.

The new control script records each rejected mathematical gate. It updates
dependency digests when deliberately changing definitions, so rejection is not
merely a checksum failure. The duplicate completing member also receives a
consistent duplicate value row and must fail specifically at the full-rank
minor. Correct source rescaling and a different valid completing source pass.
Malformed JSON, duplicate keys and size-limit probes use the same dispatcher
entrance as real certificates.

`results/ci73/inputs` includes the original source matrix, seven residue blocks,
mixed definitions and selected primary inputs with provenance. The certificate
contains the common 73-column witness. `analysis/ci73_prepare.py` rebuilds that
certificate from pinned definitions; it produces candidate data, not a PASS.
`analysis/ci73_dimension_run.py` regenerates the ambient power expansion.
`analysis/ci73_provenance.py` is a historical local-input audit and intentionally
uses the original machine layout; a receiver does not run it. Its complete
results and hashes are included. The acceptance path instead checks actual
bounded referenced contents directly.

## Equations and scope

`docs/ci73_equations.md` lists all 117 coefficients and all 39 native definitions.
`results/ci73/equations.json` additionally contains each degree-13 and literal
degree-24 definition and the full 274-by-3 transported coordinate matrix.
The normalization is ordinary coefficients with alpha! symbols and
u=24 c_(4,0^8); indices are zero-based, so completing source 15 is the sixteenth
entry. K consists of integer representatives of a rational kernel basis, without
an integral saturation claim.

The new proof establishes i_red(13)=3 and, by u^11 transport, i_pad(24)>=3.
The separately inherited S74 a24=274, determinant rank 273 (using the adopted
LMR upper bound) and padded rank floor 269 give i_pad(24) in [3,5] and D_LMR in
[-4,-2]. The inherited replay recomputes minor arithmetic and point u values;
it does not freshly regenerate their degree-24 native polynomials. D=-4 and
the remaining two degree-14 candidate equations remain open.
