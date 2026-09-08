# S1 checks actually run
Frozen at 2026-09-08 21:00:02 UTC.

## Fresh control minors

Rows are source fillings and columns are explicit points. Indices are zero-based and retained in the JSON files. Residues are exact integers.

| Control | p=2147483647: rank / minor | p=2147483629: rank / minor |
|---|---:|---:|
| n=3, generic | 6 / 1620360193 | 6 / 123484146 |
| n=3, det | 5 / 1651298045 | 5 / 231228918 |
| n=3, permanent | 6 / 1716478146 | 6 / 1416905587 |
| n=3, birth | 1 / 1310708144 | 1 / 2073428185 |
| n=4, generic | 2 / 863359049 | 2 / 441683901 |
| n=4, det | 2 / 1203347414 | 2 / 1424748952 |

The n=3 determinant ideal combination `[66,-972,12,-37,4,320]` evaluates to zero on all seven fresh determinant points at each prime. This finite check is consistent with the banked ideal identity, and is not its global proof.

All entries of the eight n=3 minors (generic, determinant, unpadded permanent, birth; both primes) were recomputed by the independent Python determinant-polarization path. All eight entries of the n=4 determinant 2x2 minors were recomputed by C# determinant polarization. The same minors were also checked arithmetically by integer Bareiss elimination. The two evaluators share the audited symbol packer; 16 tiny literal-sum checks separately test this normalization and signs, including four nontrivial Plucker checks.

## Exact archived comparison

The six archived chi arrays are independent at both primes. Their ideal combination has gcd 29,859,840; after division it is the negative of the banked primitive vector. All 17,047 coordinates match, with support 3,900 and maximum absolute coefficient 544. This is new exact arithmetic on archived expansions; neither literal expansion nor the large E-matrix was rebuilt.

The saved 113x300 target generic matrix has rank 113 under fresh elimination; its leading 113x113 determinant is 487364101 modulo 2147483647. Its evaluator/point semantics were not freshly replayed. It is not promoted into a new target certificate.

## Degree-13 birth-prefix replay

The first eight saved degree-13 birth fillings give rank eight on ten fresh u=0 points at each prime. The matrices are 8x10. This verifies eight classes, not all 32 archived classes or the full 37-dimensional birth quotient.

| Prime | Rank | Retained 8-minor |
|---:|---:|---:|
| 2147483647 | 8 | 1038086563 |
| 2147483629 | 8 | 1199155609 |

Together with the two seed vectors, these supply the ten independent target source vectors in `partial_source_10.json` by proved u-transport. This is a small certified partial source; it is not a ten-row target determinant/padded rank measurement.

The independent seed determinant minor also transports, because both leading coefficients at its points are nonzero. `transported_det_lower_bound_2.json` gives a reconstructible target determinant lower bound two using normalized u^12 seed circuits. No target determinant rank beyond two and no new true-padded lower bound is claimed.

## Paired bounded sampling benchmark

The 64-candidate stream uses n=3, degree 12, seed 120112 and P1. The same candidates are tested against a fresh certified five-dimensional transported old span, and separately at one u=0 point. This isolates the final one-dimensional source birth.

- Ordinary seven-point residual test: 22/64 candidates have a nonzero class.
- Birth test: 22/64 nonzero; the entire acceptance pattern agrees. The first success is candidate 6 (zero-based).
- Pure-u removal rejects 27 candidates exactly, without evaluating them.
- Point evaluations: 448 versus 37, a 12.11-fold reduction.
- Summed evaluator time for these policies: 0.720755 s versus 0.046267 s, a 15.58-fold reduction in this run.

These very short timings exclude startup, packing, and elimination and are not a stable machine-performance calibration. The ordinary policy evaluates seven points for every candidate; an optimized sequential baseline would be cheaper. The comparison demonstrates removed work, not a higher mathematical hit rate or a target completion-time prediction. After one birth is retained, the quotient is full; all 64 were inspected solely for this bounded benchmark.

## Rewrite and circuit timing checks

Every one of 113 saved target fillings exceeded the reducer cap of 64 pending/normal-form terms (and a separate maximum of 512 rewrites). That particular full-expansion route was stopped. It does not establish that better cancellation-aware or tall-column straightening is impossible.

Pure-u stripping of the archived target fillings gives this exact active-degree histogram: `{'23': 20, '22': 39, '21': 31, '24': 5, '20': 16, '19': 2}`. An active degree is a visible transport origin, not a proof of the vector's minimal birth degree.

| Evaluator/control family | Calls | Sum seconds | Median seconds |
|---|---:|---:|---:|
| exterior, 3_generic | 84 | 0.2139 | 0.001976 |
| exterior, 3_det | 84 | 0.1560 | 0.001856 |
| exterior, 3_permanent | 84 | 0.1537 | 0.001901 |
| exterior, 3_birth | 84 | 0.0681 | 0.000760 |
| exterior, 4_generic | 12 | 4.7229 | 0.386118 |
| exterior, 4_det | 12 | 5.1150 | 0.426512 |
| independent mixed determinant, n=4 | 8 | 359.9978 | 44.991680 |
| exterior, n=4 saved birth prefix | 160 | 50.8571 | 0.262024 |

The historical 12–15 CPU-hour LMR completion estimate was not run as a baseline and cannot be replaced by multiplying these small-control timings.

## Preflight result

Local HEAD and cached origin/main matched c984e2c6d59ba0bbc6ac2fdd113edf920a8aebd9. A live remote fetch was unavailable from the shell. Repository selftest stopped on the missing flint import. No selftest cases, full s67/s71 calibration, second-engine B24 calculation, or weighted-DAG calculation are marked PASS. The source manifest was checked again before this freeze. Canonical inputs and shared checkout were unchanged. The requested Documents destination was denied; this permitted workspace directory is the delivered fallback.

## Rank outcome

Target source: ten independently constructed Q vectors are supplied by the proved two-block transport argument. Target determinant: a transported lower bound two, with the inherited LMR upper bound 273. Target padded: no new lower bound computed. Determinant rank 273, padded rank 274, and D remain OPEN.
