# S4 replay and artifact map

The archive is self-contained for the performed checks. Use the bundled Python with NumPy and PowerShell with Add-Type. No Linux library or shared-checkout write is needed. The copied S1 helper has one recorded adaptation: its source root points to the local frozen snapshot.

```powershell
$S4Root = 'C:\Users\swami\Projects\gct-gpt\Batch12_Results\S4'
$S4Python = 'C:\Users\swami\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe'
& $S4Python "$S4Root\src\s4.py" prepare 36
& "$S4Root\src\run.ps1" -Limit 12
& $S4Python "$S4Root\src\s4.py" summarize
& $S4Python "$S4Root\src\calibrate.py"
& $S4Python "$S4Root\src\verify.py" tiny
& "$S4Root\src\run.ps1" -Limit 1 -InputPrefix tiny -OutputPrefix tiny_values
& $S4Python "$S4Root\src\verify.py"
```

Twelve is the completed prefix. The original invocation allowed 36 but stopped at the 25-minute soft wall-time gate after column 11; the reason and outlier are in the report. Regeneration creates temporary JSON packs in scratch. They are omitted from the frozen deliverable because all inputs and packing code are retained. The small retained evaluation logs preserve actual timings and the cross-evaluator checks. A replay changes timing fields and requires a new freeze if published.

Main artifacts:

* `artifacts/padded_certificate.json`: full 34 by 12 native/target matrices at both primes, minor indices and determinants.
* `artifacts/points.json`: all 36 generated integer point arrays and coefficients; only 0 through 11 evaluated.
* `artifacts/source.json`, `source_coordinate_transforms.json`: 34 candidate vectors, native degrees, exact transport factors, literal target extensions and tensor permutations; first 12 certified by the displayed minor.
* `artifacts/48_block_ledger.json` and `.md`: 48 independently enumerated indices with inherited dimensions and uncomputed block-rank status.
* `artifacts/s64_control.json`: entire 561-coordinate control basis, raising rows and 559-minor, integer source vectors, exact fixed-factor kernel, points and rank minors.
* `artifacts/s64_r5_exact_kernel.json.gz`: primitive integer polynomial, archived-coordinate scalar, exact identity checks, fresh point checks.
* `artifacts/r6_parametrization.json`: both parameter Jacobians, actual parameters, and nonzero 55/61 minors.
* `artifacts/n3_control.json`: fresh determinant/unpadded-per3 matrices with exact native sources and points.
* `artifacts/independent_checks.json`, `tiny_literal.json`: separate minor arithmetic and literal contraction checks.
* `input_manifest.json`, `artifact_manifest.json`, `preflight.json`: immutable input base, hashes, local/remote qualifications, and delivery restriction.

These are session-specific research certificates, not purported PASS records from the general repository verifier. The latter's split_rank/hybrid_kernel records are not re-derived here. No proof of target upper rank or Q-kernel is inferred from a finite deficient matrix.
