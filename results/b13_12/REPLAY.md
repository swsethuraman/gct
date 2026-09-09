# B13-12 replay

The report is `docs/b13_12_report.md`. All numerical outputs use ordinary
coefficients; no floating-point ranks, transported matrices or multiplicity
computations occur. The frozen base is
`00495110c62acfbbbc951e82cc218ed091563b3f`.

Use a separate checkout when regenerating timestamped or resource records.
From its root on Windows, with Python 3.12 or later:

```powershell
& $python 'analysis/b13_12_bounded.py' b13_12_coefficients 120 'analysis/b13_12_exact.py' coefficients
& $python 'analysis/b13_12_bounded.py' b13_12_boundary 120 'analysis/b13_12_exact.py' boundary
& $python 'analysis/b13_12_bounded.py' b13_12_s2 300 'analysis/b13_12_exact.py' s2
& $python 'analysis/b13_12_bounded.py' b13_12_triangular 120 'analysis/b13_12_exact.py' triangular
```

Set `$python` to your Python executable. On this host it is
`C:\Users\swami\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe`.
No third-party package is required for these commands. The launcher enforces a
1 GiB process-memory cap before calculation, sets one BLAS thread, records the
child PID and bounds elapsed time. If less than 2 GiB physical memory is free,
it refuses to launch. Non-Windows hosts should use their own equivalent
resource guard and run the exact script's four units sequentially.

Expected checks:

* 69/69 inherited nonanchor polynomials agree exactly; all 70 exponents present.
* 12 direct integer determinant comparisons in two point families, also checked
  at both house primes.
* Generic 64-parameter boundary identity, all coefficient monomials; source
  entry exponents 0 through 4, determinant exponent exactly 8.
* S2 rational rank cases 9,0,3,9; tangent quotient zero; eight jet cases and
  24 checks of its rank-three arc. Source matrices, minors and kernels replay.
* 70/70 triangular identities, 625 terms, 125 terms with one diagonal form zero.

The algebraic proofs of proper-image universality and the finite-map dimension
must also be reviewed; replaying identities alone is not a proof of every
geometric statement in the report.

The Singular jobs under `cas/` have not been run. `full_monic_Q.sing` is the
global decision job. Run it from the repository root, with a separately
enforced wall and memory bound. Its 133-variable contraction must finish
**before** the bad target coordinates are set to zero. Preserve and verify a
polynomial-substitution or standard-basis membership certificate over Q before
promoting any output. A unit fixed-factor ideal contradicts the known point
`v^4`. The infinity and nilpotent-support files are auxiliary specifications;
the latter is not a replacement for the saturated graph.

Bundle verification:

```powershell
git bundle verify 'b13_12_five_variable_closure.bundle'
git bundle list-heads 'b13_12_five_variable_closure.bundle'
Get-FileHash -Algorithm SHA256 -LiteralPath 'b13_12_five_variable_closure.bundle','b13_12_five_variable_closure.part00'
Get-FileHash -Algorithm MD5 -LiteralPath 'b13_12_five_variable_closure.bundle','b13_12_five_variable_closure.part00'
```

The prerequisite commit must exist for `git bundle verify`. There is exactly
one part, part00, identical to the whole bundle. Digest files use bare
filenames. The delivery also contains a Git archive of the changed files at
the exact delivered head, and user-facing report/manifest copies.
