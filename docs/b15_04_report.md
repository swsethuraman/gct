# B15-04 complementary multiplicity panel

Model: gpt-6-astra for reasoning, implementation, verification, and delivery; xhigh requested by dispatch. Existing B13/B14 code and mathematics retain their original attribution. Base commit: f365568d80d5f66fea2dd9342ff1998e1d866915; base tree: aff6ca0921ec964cc8b7fcbd64bd5e5e9de9fbbd. The existing assigned worktree and branch were retained.

Both assigned degree-eight cells have determinant rank at least three and padded upper bound three, hence D<=0. Three explicit integral highest-weight polynomials per cell and three integer determinant pencils certify the rank floors. Fresh compact replay independently checks every simple raising identity over the integers and regenerates determinant coefficients and evaluation minors. Proposed exclusions await integrator review; no shared theorem or exclusion file was changed.

## Exact findings

Both cells have n=4, polynomial degree 8, ambient dimension 16, and seven-row highest weights. The seven-variable evaluation restrictions use the ordinary coefficient convention inherited from wk8_s30_core: E_(i,i+1)c_alpha=(alpha_i+1)c_(alpha+e_i-e_(i+1)). No factorial rescaling, u multiplication, or basis conversion is applied. Independently padded points come from z per_3 with ten essential variables; a seven-dimensional restriction does not change that definition.

| Label | Ambient a | Pullback h_pad | Raw weight count | Signed carrier n_chi | U_pad |
|---|---:|---:|---:|---:|---:|
| (11,11,5,2,1,1,1) | 4 | 3 | 1,577,460 | 70,438 | 3 |
| (12,11,4,2,1,1,1) | 3 | 3 | 986,119 | 85,325 | 3 |

Status: EXACT combinatorial computation. Fresh character/plethysm and Pieri/cubic counts agree with the launch values. Signed Burnside counts were independently checked against direct small orbit enumeration, including an odd-character mutation. The naive raw-count/stabilizer quotients are 131,455 and 986,119/6, neither the correct signed carrier size. The first cell has the larger raw construction but the smaller reduced carrier.

The scoped typed exclusion ledger, accepted-state corrections, transport overlay, and shortlist removals were applied. Neither assigned cell matched an exclusion or overlay entry. With L_pad=0, U_pad=min(a,h_pad,a-L_pad)=3 for both cells. Determinant rank at least three excludes D>0. The first cell needs two global determinant equations plus padded rank three for D>=1; the second needs one equation plus padded rank three. Sample deficiencies do not establish global equations.

## Research measurements and certificates

| Measurement | (11,11,5,2,1,1,1) | (12,11,4,2,1,1,1) |
|---|---:|---:|
| Raw monomial construction, seconds | 2.070 | 1.478 |
| Signed orbit construction, seconds | 8.255 | 2.653 |
| Raising-row construction, seconds | 22.846 | 13.590 |
| Complete construction, seconds | 33.172 | 17.721 |
| Raising rows / nonzeros | 384,995 / 1,445,964 | 332,513 / 1,032,133 |
| Best triangular cover | 70,418 | 85,304 |
| Residual columns | 20 | 21 |
| Cover selection, seconds | 0.198 | 0.162 |
| Full projected reduction, seconds | 0.871 | 0.952 |
| Dense residual nullspace, seconds | 0.0029 | 0.0003 |
| Determinant points used | 3 | 3 |
| Checked determinant rank floor | 3 | 3 |
| Integral evaluation minor mod 2,147,483,647 | 2,044,407,607 | 1,601,498,597 |
| Integral source union monomials | 296,730 | 145,230 |
| Compressed integral source bytes | 1,533,693 | 693,686 |

The first cell costs more in raw construction; the second has the larger signed carrier. Neither initial dense carrier estimate predicts the actual reduction cost well: the reversed triangular order leaves only 20 and 21 columns. The projected uint32 matrices need 6,720 and 7,140 bytes. The one-block residual benchmark measured 16 columns before extension; the full rank follows from the complete controlled reduction and direct source verification, not from that benchmark.

For the first cell, the final result is m_det>=3, i_det<=1 and D<=0. For the second, a=3 gives m_det=3 and i_det=0, with D<=0. We stopped determinant evaluations at rank three. No padded rank was measured and no exact D value is claimed. The sufficient missing witness for D=0 at the second cell is padded rank three. Determining the first cell's exact D additionally needs its padded multiplicity and either the fourth determinant direction or a valid global determinant upper bound three. Positive D is excluded in both cells under the stated ambient/pullback conventions.

The final sources have integer coefficients of absolute value at most 4,608. Exact coefficient-by-coefficient Leibniz raising checks use the exported polynomial terms and an independently assembled combinadic, rather than the constructed raising matrix. Their monomial weights and degree are checked in the compact replay. A fresh determinant expansion by permutations regenerates the ordinary coefficients from the explicit pencils; a nonzero 3 by 3 minor at one prime proves the rational rank floor. No uniqueness claim or rational reconstruction assumption enters this final proof: reconstruction is followed by exact integer source verification.

The largest local construction caches are 9,963,925 and 6,337,199 bytes. They are preserved untracked and excluded from delivery. All complete integral polynomial terms, the letter indexing, and explicit points are delivered in the compact source/certificate files. The cover and modular kernel are retained as optional construction provenance. The native carriers can be rebuilt from the frozen input construction, but the concise certificate replay does not need them.

## Resource decisions and stopped attempt

The integrator granted the first pilot, reviewed its measurements, then authorized first-cell rank and second-cell construction sequentially. After the second measurements, it authorized the short rank and integral verification runs. No concurrent numerical jobs were launched by this worker. No 90-minute production extension was needed. The lease was explicitly released with process identities, recorded start times, and completed resource receipts in results/b15_04/lease_release.json. One PID was reused by Windows between completed runs; no archived PID was used to end a process.

| Run | Return code | Wall seconds | Aggregate peak MiB |
|---|---:|---:|---:|
| First-cell construction pilot | 0 | 36.052 | 339.58 |
| First-cell rank | 0 | 2.293 | 157.30 |
| Second-cell construction pilot | 0 | 20.266 | 294.49 |
| Second-cell rank | 0 | 2.418 | 156.89 |
| Initial integral verification gate | 1 | 0.718 | 143.82 |
| First-cell optimized integral verification | 0 | 2.207 | 309.20 |
| Second-cell integral verification | 0 | 1.310 | 196.04 |
| Final compact replay, both cells | 0 | 2.512 | 260.17 |

The initial integral attempt reconstructed and checked integer source coordinates on E, then stopped at the script's 150,000-term expanded-verification gate when the first union contained 296,730 terms. This was a cost-gate stop, not a mathematical failure or a breached operating-system memory limit. The revised implementation replaces per-term Python list lookups with a 210-letter replacement table and permits up to 400,000 terms. Both runs then passed under unchanged 60-second/512-MiB limits. The failed log and return code are retained. Construction pilots used 900 seconds/1536 MiB; rank follow-ups used the tighter 120 seconds/512 MiB; every verification used 60 seconds/512 MiB. All numerical runs used one process and one BLAS thread.

## Controls and smallest exported witness

The integral degree-two source is F=3 c_(3,1)^2-8 c_(2,2)c_(4,0), weight (6,2). It is annihilated by the raising operator and has exact value -1597 on the explicit two-matrix determinant pencil in results/b15_04/controls.json. It vanishes on a fourth power. This establishes liveness independently of both research cells.

The lean and older constructors agree entrywise on two small cells, including a nontrivial odd stabilizer character. The uncompressed raising implementation checks the complete exported source. Defect controls alter a source sign, a point coefficient, and coefficient factorial normalization. The independently padded evaluator is checked by a direct permanent sum using ten-column frames. A separate verifier imports no producer code: it reconstructs the binary quartic by exact Vandermonde interpolation from FLINT integer determinants, verifies the full raising identity, and reproduces -1597. It also verifies 17 frozen input hashes and the signed Burnside arithmetic in the receipt.

The native portable reduction uses signed integer triangular solves, narrow residual blocks, and a seeded sparse projection, with an explicit memory estimate before dense elimination. Its triangular solves agree with FLINT at both house primes. A synthetic residual system exercises projection and lifting, rejects a corrupted kernel, and agrees with exact nullity; the actual source control remains nonzero through this reduction.

| Run | Return code | Wall seconds | Aggregate peak MiB |
|---|---:|---:|---:|
| b15_04_controls | 0 | 1.905 | 72.89 |
| b15_04_sizing | 0 | 1.074 | 82.69 |
| b15_04_controls_reduction | 0 | 2.897 | 66.12 |
| b15_04_independent | 0 | 0.448 | 48.39 |
| b15_04_projection_control | 0 | 0.561 | 68.64 |

All runs used the exact assigned Python executable, Windows Job Object limits of 60 seconds and 512 MiB, one numerical process, and one BLAS thread. Recorded PIDs belong to completed runs and are not used for subsequent process operations. Pre-existing native and preflight runtime logs are preserved separately and excluded from research commits.

## Evidence boundaries and replay

The rational lifting lemma in docs/b15_04_proved.md requires rank_Fp(E)=rank_Q(E)=n_chi-a. A triangular cover plus projected residual rank and a verified complete kernel can establish the finite-field equality. A p-unit maximal minor then makes the source kernel commute with reduction over Z_(p), so a modular evaluation minor is a valid rational rank floor. Checking only E K=0 on some vectors is insufficient. The general representation/source interpretation and Pad-to-linear-times-cubic pullback inclusion are inherited premises; the numerical counts and small witness are freshly checked.

From the assigned worktree, use the executable C:/Users/swami/Projects/gct-gpt/work/batch15_workers/B15-04/.venv/python.exe. The commands following that executable are:

```text
analysis/b15_bound.py --slot 04 --name b15_04_replay_controls --seconds 60 --memory-mb 512 analysis/b15_04_panel.py controls
analysis/b15_bound.py --slot 04 --name b15_04_replay_sizing --seconds 60 --memory-mb 512 analysis/b15_04_panel.py sizing
analysis/b15_bound.py --slot 04 --name b15_04_replay_independent --seconds 60 --memory-mb 512 analysis/b15_04_verify.py
analysis/b15_bound.py --slot 04 --name b15_04_replay_projection --seconds 60 --memory-mb 512 analysis/b15_04_reduce.py control
```

Input hashes, explicit control source and points, phase receipts, return codes, and aggregate memory measurements are in results/b15_04 and results/logs/b15_04_* respectively. The first preregistration commit is 8eb873192fe2121c8a4c6c4286bfede359cf6fce. A pre-run follow-up corrected its coefficient-convention sentence after input inspection; the correction is explicit in the preregistration.

The shortest complete research-certificate replay, from the assigned worktree and using the exact executable above, is:

```text
analysis/b15_bound.py --slot 04 --name b15_04_receiver --seconds 60 --memory-mb 512 analysis/b15_04_replay.py
```

It checks both full integral polynomial sources and freshly rebuilds all six determinant point evaluations. Source NPZ arrays contain monomials (rows of eight letter indices), coefficients (three integral polynomial columns), and letters (the 210 exponent vectors). The two JSON certificates contain the explicit points, expected 3 by 3 matrices, prime, nonzero minors, and exact source hashes. The standalone helper does not read the local native caches. This delivery contains two proposed exclusions, docs/b15_04_proved.md, and the complete bounded receipts. Packaging checks do not certify the mathematics.
