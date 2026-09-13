# B15-08: three-column bracket evaluator

Model: gpt-6-astra, xhigh reasoning as dispatched, for all new proof, code, controls and delivery. B14-06's two-column formula and jet controls retain their original Claude Opus 5 attribution. No extra agents were used.

## Result and current execution status

The evaluator now supports tails with conjugate (h,h,2,1^k), including the requested (t,3,2^6) at h=8. It expands the short column into two signed terms and evaluates each by finite differences of a bordered determinant. It uses actual symmetric tensors, including the third derivatives needed by a letter meeting all three columns. It does not build a weight-space carrier.

The algebraic proof and small controls are complete. A compact exact ambient witness is derived for the full-height tail (4,3,2^6): two sources at two explicit integral points have evaluation matrix diag(5040,720), determinant 3,628,800. The freshly computed exact ambient dimension is 2. Thus the proof establishes ambient completeness for this cell without a spanning assumption. The evaluator has reproduced the general witness at heights two and three. The full-height evaluator invocation is pending the integrator's resource ruling; the derived height-eight values are not described as a numerical replay.

No heavy job has run. Slot08's initial lease request was received and queued behind 04,05,06; the current holders remain 01 and 03. A smaller control request was prepared, but automatic approval review rejected sending it to the integrator task. Explicit authorization for that message was requested in this task. The existing lease queue is unaffected. No shared lease or theorem record was edited.

## Checked evidence

| Check | Fresh result | Evidence status |
|---|---|---|
| Formula versus direct epsilon contractions | 193 exact integer equalities, 120 nonzero values, heights 2 and 3 | EXACT |
| Sign and coefficient factors | Reversing the short column negates live values; omitted sign and repeated-matrix factorial defects detected | EXACT |
| Liveness independent of research cells | Quadratic two-column control equals 3!*det(T2), nonzero | EXACT |
| Repeated letters and vectors | Invalid overfilled letter rejected; repeated-vector source exactly zero | EXACT |
| Highest-weight convention | Upper unitriangular invariance and torus weight (5,3,2) checked | EXACT |
| Polynomial jets | 90 derivative identities through order three; Euler relations included | EXACT |
| Native DET/PAD points | Fresh full polynomials agree with regenerated B14-06 two-jets at both primes | EXACT |
| Independent padding | Full ten-variable z*per3 construction checked with invertible integer 10 by 10 L; nine-variable restriction is identified explicitly | EXACT |
| Polynomial normalization | Direct native and depressed polynomial values agree for DET, PAD and RED; zero-c inputs rejected; altered depressed coefficient detected | EXACT |
| Small ambient dimensions | Nine shapes reach their exact counted dimensions at both primes | REPLAYED_RANK_FLOOR plus exact upper bounds |
| Full-height analytic witness | Rank 2 from the proved two-point formula and exact character count; evaluator execution pending | EXACT algebraic proof |

The two primes are 2147483647 and 2147483629. The nine small generic ranks, in shape order, are (3,3):0; (4,3):2; (5,3):2; (6,3):6; (3,3,2):0; (4,3,2):2; (5,3,2):4; (6,3,2):10; (7,3,2):15. Both primes agree with the exact characteristic-zero ambient counts.

The short-column brute implementation directly enumerates all h!^2*2 assignments and does not use the determinant formula. The analytic witness specializes at h=2 to the identity matrix and at h=3 to diag(2,1); these were checked over the integers, by direct contraction, and at both primes.

## Exact sizing and mathematical scope

For h=8 the stable algebra is C[Z]=Sym(Sym^2 C^8 + Sym^3 C^8 + Sym^4 C^8), in the positive highest-weight convention. Weighted degree W=t+15 is distinct from quartic coordinate degree delta. The inherited Proposition S identification is used only for n=4, ell=9, delta>=W, lambda=(4*delta-W,t,3,2^6). The full determinant ambient can have 16 variables; the length-nine restriction used here does not change the representation convention. No earlier finite stabilization is asserted.

| t | W | Exact a_inf | Explicit source rows | Determinant calls per point, upper bound | Largest determinant order |
|---|---|---|---|---|---|
| 3 | 18 | 0 | 2 | 72 | 9 |
| 4 | 19 | 2 | 6 | 256 | 9 |
| 5 | 20 | 4 | 21 | 894 | 10 |
| 6 | 21 | 12 | 49 | 2212 | 10 |
| 7 | 22 | 21 | 113 | 5194 | 10 |
| 8 | 23 | 41 | 219 | 10454 | 10 |
| 9 | 24 | 66 | 414 | 20052 | 11 |

The counts are exact rational power-sum inner products using the banked B14-04 recurrence and Murnaghan-Nakayama routine. Small character orthogonality and known multiplicities were freshly checked. Source-row counts are not dimensions, and no stabilizer quotient replaces a signed count. The first prototype t=3 has zero ambient multiplicity and cannot be used as a nonzero liveness goal.

A direct full-height contraction has 8!^2*2=3,251,404,800 terms per source. The derived evaluator avoids that width. Its construction lists only explicit signatures and matrices of order at most the tabled size. Point construction, source evaluation and matrix reduction are separately timed by the prepared production runner. It has not run, so no production timing estimate is reported as a measurement. The smaller analytic replay is prepared independently.

All three scalar/gradient/Hessian data and the third-order slices come from full polynomial tensors. Ordinary coefficient alpha equals d!/product(alpha_i!) times the tensor entry. Native generic points are integral. Geometric points come from integer matrices and forms, with rational normalization by nonzero c and small factorial denominators; those denominators are invertible at the selected primes. This supplies rational lifting of modular rank floors.

The typed scoped exclusion ledger and accepted-state transport overlay were applied to every sized representative. The h=8 representatives have no matching exclusion in those inputs. The known small-length containment gate applies to the short controls but does not assert an empty determinant ideal. No padded/reducible equality above degree eight is assumed. No geometric rank was obtained for these new tails: point-family controls establish validity, not multiplicities. Hence no new exclusion is proposed. For a future gap test the conservative valid padded bound is U_pad=a; a determinant floor a would exclude positive D. A positive gap would require a global determinant upper bound and a strictly larger padded floor. Deficient samples alone would not supply that upper bound.

## Outcomes and resources

All runs used the assigned local Python executable, the Windows Job Object wrapper, one process and one BLAS thread. No worktree, trust, ownership or sandbox settings changed. Available physical memory was checked by the wrapper before each numerical run. The two original runtime provenance files remain untracked and were not staged with preregistration.

| Run | Return code | Wall seconds | Aggregate peak MiB | Cap |
|---|---|---|---|---|
| b15_08_sizing | 0 | 0.295 | 23.87 | 60 s / 512 MiB |
| b15_08_controls | 1 | 0.125 | 23.75 | 60 s / 512 MiB |
| b15_08_controls_v2 | 0 | 0.217 | 24.09 | 60 s / 512 MiB |
| b15_08_point_controls | 1 | 0.247 | 26.24 | 60 s / 512 MiB |
| b15_08_point_controls_v2 | 0 | 1.854 | 25.99 | 60 s / 512 MiB |
| b15_08_point_controls_v3 | 0 | 0.284 | 26.07 | 60 s / 512 MiB |
| b15_08_small_ranks | 0 | 0.473 | 19.89 | 60 s / 512 MiB |
| b15_08_analytic_small | 0 | 0.042 | 16.24 | 30 s / 128 MiB |

Return codes above are the wrapper's recorded Python return codes. The first control run used fewer sources than its own minimum sample threshold and stopped; the sample was expanded without changing the identity check. The first point-control run encountered a c=0 random point and stopped correctly, but its harness did not yet collect and resample chart rejections. The corrected harness records them explicitly. The third point-control version added a changed-normalization control. All original failure logs and resource receipts are preserved. No wall or memory limit was reached. Clock timestamps reflect the host; wall durations are the wrapper's monotonic measurements.

## Replay and delivery

All shell commands run from the existing assigned worktree. In PowerShell set:

    $b15Python = 'C:\Users\swami\Projects\gct-gpt\work\batch15_workers\B15-08\.venv\python.exe'

Small verified replays:

    & $b15Python analysis/b15_bound.py --slot 08 --name b15_08_receiver_controls --seconds 60 --memory-mb 512 analysis/b15_08_run.py controls
    & $b15Python analysis/b15_bound.py --slot 08 --name b15_08_receiver_points --seconds 60 --memory-mb 512 analysis/b15_08_run.py point_controls
    & $b15Python analysis/b15_bound.py --slot 08 --name b15_08_receiver_small --seconds 60 --memory-mb 512 analysis/b15_08_run.py small_ranks
    & $b15Python analysis/b15_bound.py --slot 08 --name b15_08_receiver_analytic_small --seconds 30 --memory-mb 128 analysis/b15_08_witness.py small

The sufficient remaining operational witness is the full-height evaluation of the proved 2 by 2 matrix, after the integrator's resource ruling:

    & $b15Python analysis/b15_bound.py --slot 08 --name b15_08_fullheight --seconds 30 --memory-mb 128 analysis/b15_08_witness.py full
    & $b15Python analysis/b15_bound.py --slot 08 --name b15_08_fresh_replay --seconds 30 --memory-mb 128 analysis/b15_08_witness.py replay

The prepared larger `production` and `replay` modes remain gated by the shared lease record and were not executed. They cover three full-height tails with exact counts, explicit native parameters, full regenerated polynomial values and nonzero minors. They are optional follow-on work after the smaller completion check, not evidence for this report.

Input SHA-256 hashes are in the preregistration and machine receipts. Full small inputs, sources and values are retained in results/b15_08; the analytic full-height recipe is in analytic_witness.json. The proof fragment names inherited premises separately. Final committed head/tree and delivery-check results will be recorded by the external packaging manifest after the final commit. A packaging PASS does not verify the mathematical claims.
