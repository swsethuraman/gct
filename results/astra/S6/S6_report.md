# Batch 12 S6 — Sol adversarial audit

## Executive verdict

**Batch 12 does not determine the LMR rank gap.**  At the frozen cell

`lambda=(65,17,2^7), delta=24, r=9, a=274`, with
`D=rank(T_pad)-rank(T_det)`, the audit promotes only

* `rank(T_det) >= 2` from S1, while the LMR upper bound remains `rank(T_det) <= 273`;
* `rank(T_pad) >= 12` from S4, with no matching upper-rank certificate below 274;
* the S3 degree-12 compact-operator control and its later common-source evaluation bridge;
* exact bounded r=5 lemmas and counterexamples from S2, not a global r=5 theorem; and
* the corrected stable weight-13 census: **57** partitions, **10** zero ambient blocks, **47** positive blocks, and **five** open `a_infinity=4` candidates.

The exact ranks `273` and `274`, and therefore the sign or value of `D`, remain **OPEN**.  No report supplied a deterministic 274-dimensional rational source basis evaluated on both target families in the same ordering.

All completed S1–S4 frozen manifests pass after rechecking.  The current durable checkout is clean at `afb8c3319d3d1f3afc3d2578c8cb322f2b8a3b92`, equals the locally cached `origin/main`, and has `c984e2c...` as an ancestor.  Network access was restricted, so this is not a fresh remote verification.

The requested external result directory was outside the writable roots available to this run.  This bounded fallback delivery is therefore under
`C:\Users\swami\Projects\gct-gpt\Batch12_Results\S6`; canonical sources, the shared checkout, and the frozen session reports were left unchanged.  One S1 replay helper unexpectedly rewrote JSON formatting; the affected file was immediately restored byte-for-byte from `S1_artifacts.zip`, its expected SHA256 was rechecked, and the complete S1 manifest now passes.

## Inputs and precedence

The full S6 brief, Batch 12 launch packet, reconciled final proposal, both Batch 11 stocktakes, and the comprehensive session source were read.  The finalized proposal/launch assignments were used wherever older board names conflicted.  Exact paths and hashes are frozen in `input_manifest.json`.

The rank protocol was applied literally:

* vectors are columns and evaluation points are columns of the transposed evaluation convention recorded by each session;
* the true padded family is `ell * per_3`, distinct from an unpadded permanent pencil;
* the reducible family is `ell * c`;
* a nonzero modular minor of an explicitly integral/rationally normalized matrix supplies a rational lower bound at a good prime;
* a modular kernel alone does not lift to a rational kernel;
* sampled deficiency is not an upper-rank certificate; and
* cross-field promotion requires both house primes `2147483647` and `2147483629`, reproducible points/source semantics, normalization, and independent arithmetic.

## Independent checks

| Check | Result | Adversarial qualification |
|---|---:|---|
| Frozen S1 manifest | PASS, 60/60 | The audit-induced formatting rewrite was restored from the frozen archive before the final check. |
| Frozen S2 manifest | PASS, 218/218 | S2's exact standard-library verifier was copied and rerun in an isolated S6 directory; its source hash matches the frozen script. |
| Frozen S3 manifest | PASS, 37/37 | The original write-producing rebuild was not rerun in place. |
| S3 continuation manifest | PASS, 59/59 | Its dedicated read-only verifier separately reported 680 hashes/entries checked, the frozen parent archive unchanged, and the two-prime scalar bridge valid. |
| Frozen S4 manifest | PASS, 68/68 | Its read-only arithmetic/tiny-literal verifier reported 18/18 PASS. |
| S1 transported determinant minors | PASS at both house primes | Two-by-two determinants recomputed independently; proves only `rank(T_det)>=2`. |
| S3 control rank/kernel | PASS at both house primes | Independent 29-minors recomputed and `R*U=0` checked for the stored `239 x 31` controls. |
| S3 common-source bridge | PASS at both house primes | All saved `2 x 2` basis-change, generic, and determinant minors recomputed. |
| S4 padded minors | PASS at both house primes | The selected `12 x 12` target minors were recomputed from the stored `34 x 12` matrices. |
| Stable weight-13 census | PASS at both house primes | All 57 `a_infinity` values and all five raw frontier dimensions agree modulo both mandated house primes. |
| Current repository self-test | BLOCKED BEFORE TESTS | `ModuleNotFoundError: No module named 'flint'`; zero general-verifier tests ran. |
| s67/s71 comparison | 40/40 agree | Only five selected cells times eight orders; none of the five was full-rank certified. This is equivalence evidence, not a corpus-wide PASS. |
| Point-family/seed semantics | PASS | Current order is `det_pencil, padded_permanent, reducible, generic, permanent_pencil`; the unpadded family is appended, preserving older seed offsets. |

The machine-readable details, including recomputed residues and determinants, are in `independent_check_log.json`.

## Session-by-session disposition

### S1 — source construction and straightening

**Completed bounded fallback.**  Promote the exact birth-quotient theorem
`ker(restriction)=u M_(d-1)` over Q and the saved two-source determinant lower bound.  Eight fresh degree-13 birth vectors plus two seeds give ten independent stored source vectors, but only the two seed-derived target columns yield a promoted determinant rank bound.  The unrestricted expansion exceeded the session cap, the full 274-source assembly was not produced, and the reported 113-rank benchmark is a measured implementation datum rather than a target theorem.

Verdict: exact theorem **ACCEPT**; `rank(T_det)>=2` **ACCEPT**; any full-source or rank-273 claim **REJECT/OPEN**.

### S2 — r=5 completeness geometry

**Completed bounded fallback.**  The isolated replay reproduced rational ranks `9,0,3,9`, the `dPhi` rank-16/kernel-64 tangent control, two tangent ranks `57,57` spanning 64, eight exact jet cases, and the explicit reducible rank-3 arc with 24 determinant checks.  The irreducible restricted-cubic rank dichotomy and the reducible counterexample are useful exact structure.

The two projective-source chart ideals are generated inputs only: Singular/msolve eliminations were not run.  The historical interior value 31 is governed by sampling/Schwartz–Zippel reasoning, not a deterministic global upper theorem.  Exceptional reducible and singular strata remain material.

Verdict: finite exact statements **ACCEPT**; chart recipes **CONDITIONAL**; global r=5 completeness/noncontainment **OPEN**.

### S3 — compact operator and bridge

**Completed control fallback plus a completed continuation.**  The original report establishes the compact control operator and a residual rank `29`/nullity `2` at both house primes.  Its original evaluation bridge was open; the later continuation closes that degree-12 control bridge with one rationally defined common source, explicit basis changes, and nonzero generic/determinant minors at both house primes.

The degree-13 follow-up directory has no completed report or manifest and contains only a partial one-prime selection.  It is not part of the promoted S3 result.  No usable degree-24 274-vector basis or target rank was delivered.

Verdict: operator identity/control/bridge **ACCEPT**; degree-13 partial run **NOT CHECKED**; LMR target ranks **OPEN**.

### S4 — true padded-permanent injectivity

**Completed 12-column prefix.**  The normalized padded-permanent factorization and fixed-factor kernel lemma are exact.  Both independent `12 x 12` target minors are nonzero, so the stored rationally normalized construction proves `rank(T_pad)>=12`.  Only 12 of 34 saved candidate columns were evaluated and independently certified; the residual source dimension is 262, not a small cleanup problem.  The 48 target blocks and a 274-dimensional source assembly remain uncomputed.

Verdict: fixed-factor lemma and `rank(T_pad)>=12` **ACCEPT**; `rank(T_pad)=274` **OPEN**.

### S5 — scaling law and cost model

**Incomplete.**  The isolated work directory contains ambient, precursor, boundary, width-sample, cost-ledger, and stable-frontier artifacts, but no S5 report or artifact manifest.  The records suggest `a_40=176451` against a stable precursor of 176452 and leave five boundary multiplicities unresolved; width samples are heuristic and exact `C_total/C_peak` economics are absent.  These items are leads, not frozen conclusions.

Verdict: stable census cross-check only **ACCEPT**; finite scaling law and peak-memory claims **NOT CHECKED**.

### Implementation sessions s74–s79

No correctly assigned, completed report/manifests were available for finalized s74, s75, s76, s77, s78, or s79.  An available file named `s78_report.md` studies bounded r=5 elimination—the finalized **s77** mission—not stable M6.  It conditionally reduces part of the r=5 problem (149 to 98 variables, with a remaining 64-variable dominance question), but cannot be counted as the finalized s78 deliverable.

Verdict: the bounded r=5 reduction is **CONDITIONAL s77 evidence**; finalized s78 stable restriction ranks and all other missing implementation deliverables are **NOT CHECKED**.

## Promotion ledger

| Status | Claim | Scope/why |
|---|---|---|
| ACCEPT | S1 birth-quotient theorem | Exact Q statement; no full target basis implied. |
| ACCEPT | `rank(T_det)>=2` | Both house-prime saved minors independently recomputed. |
| ACCEPT | S2 finite ranks, tangent/jet controls, reducible rank-3 arc | Exact bounded statements only. |
| CONDITIONAL | S2 r=5 chart ideals | Generated, but eliminations/completeness not executed. |
| ACCEPT | S3 control rank 29/nullity 2 and common-source bridge | Degree-12 control only. |
| ACCEPT | `rank(T_pad)>=12` | True padded family; explicit saved prefix at both house primes. |
| ACCEPT | 57/10/47 stable census and five `a_infinity=4` candidates | Ambient dimensions, not determinant restriction ranks. |
| ACCEPT | Current family-name and seed-offset semantics | Padded and unpadded permanent families are distinct. |
| CONDITIONAL | s67/s71 semantic equivalence | Forty selected comparisons; not a full-rank certification. |
| REJECT | “46 positive stable blocks” | Exhaustive recount gives 47; `(5,3,3,2)` must remain. |
| REJECT | `rank(T_det)=273`, `rank(T_pad)=274`, or `D=1` | No delivered exact certificate. |
| REJECT | Modular kernel or sampled deficiency as Q upper bound | Invalid without an exact rational lift/common-source argument. |
| REJECT | s78-labelled r=5 report as finalized s78 completion | Assignment mismatch; no stable M6 ranks. |
| NOT CHECKED | Correctly assigned s74–s79 deliverables | Missing completed reports/manifests. |
| NOT CHECKED | S5 finite scaling and peak economics | Incomplete, unfrozen work. |

The complete structured ledger is `promotion_ledger.json`.

## Stable-regime correction and next frontier

The older count 46 is superseded.  Independent enumeration gives:

* 57 partitions of 13 into at most five parts;
* 10 with `a_infinity=0`;
* 47 with `a_infinity>0`;
* 11 positive blocks with `a_infinity<=3`, already closed by the earlier stable determinant work; and
* five blocks with `a_infinity=4`, none yet evaluated on the determinant restriction map.

The four `a_infinity=1` tails are `(5,3,3,1,1)`, `(5,3,3,2)`, `(5,5,1,1,1)`, and `(7,2,2,1,1)`.  The length-four tail `(5,3,3,2)` was the omission highlighted by the review and remains explicitly retained.

The five open blocks, in raw-space cost order, are:

| Tail | `a_infinity` | Raw weight space |
|---|---:|---:|
| `(6,3,3,1)` | 4 | 1,668 |
| `(4,4,3,2)` | 4 | 3,716 |
| `(6,2,2,2,1)` | 4 | 4,636 |
| `(5,3,2,2,1)` | 4 | 6,922 |
| `(5,2,2,2,2)` | 4 | 9,166 |

These are excellent bounded targets.  A negative prefix is not a theorem about the remaining suffix; the run must stop at the first equation, duplicate it, and study its mechanism.

## Conditional Batch 13 board

The board is conditional on exact outcomes rather than optimism.  Every slot has an input, target, success condition, kill condition, bounded fallback, and verification route; the full structured form is `batch13_conditional_board.json`.

| Priority/branch | Input and target | Success | Kill/fallback | Verification |
|---|---|---|---|---|
| 1. LMR rank resolution | Assemble one deterministic 274-source rational basis from the S1/S3/S4 checkpoints and evaluate det/pad on identical ordered columns. | A 273 det minor closes det rank by LMR; a 274 pad minor closes pad rank; compute exact `D`. | Kill source/order/semantics drift or sampled-upper claims; fallback banks maximal exact common-source minors and residual blocks. | Both house primes, independent evaluator, fresh reproducible points, normalization/orientation, hashes. |
| 2. `D>0` | Duplicate the positive gap and find its kernel mechanism; test only successors satisfying `2n+1<=m^2+1`. | Exact duplicate plus an invariant mechanism and admissible growing-m successor. | Kill single-cell extrapolation and fixed `m=3,n=5`; fallback publishes the finite result/mechanism ledger. | Same cross-field protocol and independent source reconstruction. |
| 3. `D=0` | Compare the two exact kernel subspaces on the common source. | Explicit coincidence, containment, or difference witnesses. | Kill equal-nullity-as-equal-subspace reasoning; fallback exact intersection bounds. | Rational/subspace certificates and both-prime reductions. |
| 4. `D<0` | Freeze the negative cell and move to precommitted scaling/stable successors. | Negative certificate plus one fully costed admissible successor. | Kill relabelling a controlled negative as evaluator failure; fallback funds only the cheapest checkpoint. | Controls, common-source ranks, and frozen artifacts. |
| 5. r=5 geometry | S2 exact charts plus the conditional 98/64-variable reduction. | Exact global bound or complete exceptional-component classification. | Stop CAS at fixed resources; fallback preserves residual ideals/components and a smaller next job. | Independent substitutions and rational certificate checking; modular scouting is not a Q proof. |
| 6. stable M6 | Evaluate the five `a_infinity=4` blocks in the cost order above. | First duplicated stable equation, or all five exact full-rank certificates. | Stop at first equation; fallback banks each exact prefix and resumes at the next untouched block. | Both house primes, independent restriction evaluator, hashes. |
| 7. scaling economics | Finish S5's finite counts/boundaries and expose `C_total/C_peak` for a growing-m family. | Two exact count paths and a checkpointable measured cost law. | Kill width-only inference, unresolved boundaries, and row-budget violations; fallback exact component bounds only. | Independent counts, exhaustive boundary audit, measured peak memory, versioned source. |

## Bottom line

Batch 12 materially improves the evidence base but does not close its headline cell.  The strongest safe status is:

`2 <= rank(T_det) <= 273`, `12 <= rank(T_pad) <= 274`, and `D` **OPEN**.

The next rational investment is a common 274-source LMR assembly, with the five-block stable M6 frontier as the cheapest precommitted parallel/fallback direction and the exact r=5 component problem as a separate geometry track.  No Batch 13 slot should begin by inheriting the stale count 46, conflating padded and unpadded permanent families, or treating the mislabelled s78 report as stable-M6 evidence.

