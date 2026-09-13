# B15-01: four reducible equations from partial degree-14 interpolation

**EXACT: 4 <= i_red,14 <= 5.** A fresh rank-158 normalization minor,
independently recomputed normalization dimension 159, a fresh complete source
basis of dimension 93, and fresh exact identities for a five-dimensional
sampled source kernel establish this bound. With the accepted degree-24
premises and injective multiplication by u^10, **D_LMR is in [-4,-3]**.
The requested full rank 159 and exact value D_LMR=-4 remain open.

Model: gpt-6-astra for planning, code, arithmetic, verification and reporting;
xhigh requested by dispatch. No other live model or agent participated.
Native S74 and banked B14-07 inputs retain their original attribution,
including Claude Opus 5 work. This is a per-slot proof and delivery record.

## Cell, conventions and inherited premises

Work over Q with n=4, degree 14, nine row coordinates and
lambda=(25,17,2,2,2,2,2,2,2). The ambient highest-weight source is
HW_lambda(Sym^14(Sym^4 V)), of dimension a14=93. The normalization space is
N14=HW_lambda(Sym^14 V tensor Sym^14(Sym^3 V)), of dimension h14=159.
The pullback sends F to the polynomial (ell,c) -> F(ell*c). There are 495 quartic ordinary
coefficients and 174 parameter coefficients (9 linear and 165 cubic).

Every symbol is alpha!*c_alpha; u=24*c_(4,0^8). All 93 native source indices,
including the first 39, are retained, with F_i^native*u^(14-rung_i).
Sources index rows, points index columns, and A^T*K=0. No rational change of
source normalization was introduced. The effective CI73 relation columns
equal respectively 3, -2 and 6 times the first three K14 columns on the first
39 coordinates, with 54 trailing zero coordinates. Their degree-14 transport
is multiplication by u.

The independently padded permanent is z*per3 with ten essential variables.
The argument uses containment of its orbit closure P in the reducible
closure R and functorial extension of equations from the first nine row
coordinates. It does not assume m_pad=m_red in degree 14. The degree-24
values a24=274, m_det24=273 and m_pad24>=269 are inherited from the accepted
CI73/S74 receipts and `docs/batch15/ACCEPTED_STATE.md`; those large degree-24
polynomial evaluations were not repeated. Positive D was already excluded
in this cell before this work.

Frozen base: f365568d80d5f66fea2dd9342ff1998e1d866915; tree:
aff6ca0921ec964cc8b7fcbd64bd5e5e9de9fbbd; annotated tag object:
80209c13e9ae33bad8933cb47413bf7710c96cb1. The first commit is preregistration
25984fec83a8d06f1379d89934413655ae30b805. Work stayed in the supplied B15-01
checkout on branch b15-01-ci159.

## Checked result and proof

The independent shared-verifier replay returned PASS with the strict
`quartic_lmr_degree14_ci158` partial-interpolation profile. It imports the
accepted evaluator, backend and dimension routines, and imports no producer.
The checked premises are:

| Premise | Fresh evidence |
|---|---|
| 158 genuine normalization members | Full integral definitions; 24,964 newly evaluated modular entries; nonzero 158-by-158 minor modulo 2147483647, determinant 823506578 |
| Complete normalization dimension 159 | Exact Newton power-sum expansion of h14[h3], 8,667 classes, all 27 Pieri channels and outer-rim character calculations |
| Complete ambient dimension 93 | Exact h14[h4] expansion, 52,157 classes, independently computed character multiplicity |
| 93 independent native source polynomials | 8,649 newly evaluated generic modular entries; 93-by-93 determinant 702376822 modulo 2147483647 |
| Rational sampled source rank 88 and kernel rank 5 | 14,694 newly evaluated signed integer source entries at the same 158 points; all 790 entries of A^T*K vanish exactly |
| Integral signed reconstruction | H=(9!)^2*2^15*1176^14; both the seven-prime product and 2^256 exceed 2H; explicit signed margins |
| Degree-24 transport | All first 93 literal degree-24 definitions match native degree-14 definitions times u^10; the coefficient extension has 181 zero rows |

Let S be the complete 93-dimensional source, phi:S->N14 the pullback and
E:N14->Q^158 evaluation at the retained points. The fresh 158-minor implies
dim ker(E)<=1. The five-dimensional rational subspace W specified by K14
is contained in ker(E*phi). Thus dim phi(W)<=1 and
dim(W intersect ker(phi))>=4. The fresh sampled source rank 88 also gives
dim ker(phi)<=93-88=5. This proves the stated interval over Q, rather than
inferring polynomial vanishing from modular zeros.

This is an existence and dimension certificate for at least four equations
inside the supplied five-dimensional space. It does not extract a fourth
explicit globally vanishing coefficient vector or certify either remaining
K14 column individually. The first three global equations are inherited
from accepted CI73.

Multiplication by the nonzero coefficient polynomial u^10 is injective and
sends this source weight to (65,17,2,2,2,2,2,2,2) in degree 24. Hence
i_pad24>=4. Together with inherited i_pad24<=5 and
D_LMR=m_pad24-m_det24=1-i_pad24, this gives D_LMR in [-4,-3].

The proof fragment `docs/b15_01_proved.md` records the equivariant integral
membership construction and the partial-interpolation argument. The full
rank-159 code path remains unexercised by a successful complete certificate;
the delivered certificate claims only the partial result actually checked.

## Construction and bounded outcomes

Begin with the 88 genuine source-pullback members. Multiply the 72 degree-13
mixed members by the integral factor ell_0*m_(3,0^8)(c)=u(ell*c)/4, then
exchange occurrences of added linear or cubic singleton letters while
preserving every valence and column height. All retained rows have complete
definitions in `pilot.json` and the canonical certificate member snapshot.
The final 158 rows consist of the 88 source pullbacks and 70 mixed members.

| Construction stage | Evaluated candidates | Rank change | Bounded wall seconds | Seconds per added direction |
|---|---:|---:|---:|---:|
| Initial pilot: lifts and single cubic exchanges | 143 | 88 to 155 | 825.903 | 12.327 |
| Linear and double exchanges | 75 | 155 to 156 | 405.381 | 405.381 |
| One linear and up to two cubic exchanges | 290 | 156 to 158 | 814.958 | 407.479 |
| Quartic-on-ell*c hybrids and four-term polar splits | 55 | 158 to 158 | 522.000 | no gain |
| Explicit Hessian/transvectant control | 1 | 158 to 158 | 0.164 | no gain |
| Fixed Hessian/transvectant family | 36 | 158 to 158 | 0.772 | no gain |

The 72 original lifts reached rank 125; the initial cubic exchanges reached
155. The focused stage added its two directions at candidate indices 254
and 263. The hybrid route incorporated the degree-13 completing source 15
through explicit valence-four letters and exact polar splits. It added no
direction. The fixed Hessian family also added none. These are bounded
construction results, with no spanning or exhaustive-search assertion.
Unused hybrid and Hessian rows are not premises of the rank-158 theorem.

Construction, planning, evaluation and reduction measurements are retained
per stage in `pilot.json`. For example, the initial pilot spent 13.378
seconds planning, 801.939 evaluating and 0.093 reducing, excluding its small
remaining setup and serialization costs. Complete tested-candidate records,
rank gains, explicit points and intermediate basis snapshots are preserved.
The first four construction stages used about 2,568.2 bounded wall seconds.

## Controls and independent replay

The audit passed 46 literal-Leibniz comparisons with the independent C#
backend over integers and both house primes. It includes known nonzero
mixed and quartic controls, column-sign reversal, factorial alteration,
point scaling and an altered kernel coefficient. Independently recomputed
dimension data and the stored 93-by-212 source arithmetic are labeled
separately from fresh polynomial evaluations. The audit also freshly checked
12 source entries from indices 0, 15, 39 and 92 at three specified points.

A further 68-entry control verified native-degree evaluation followed by
exact multiplication by u, with integer and modular values and old/new
contraction-order comparisons. The new full-subset order calculation for
14 quartic letters changes evaluation order only. The backend, integral
symbols and Leibniz sum remain the accepted CI73 implementation.
The final exporter expands the S74 sparse generic-point representation by
inserting explicit zero coefficients. All 93 forms were checked unchanged.
A separate 192-entry integer/modular control checked batches up to 48 points
under the unchanged 380,000,000-byte backend array budget.

Nine altered-input controls were rejected: wrong claim, wrong degree,
wrong coefficient convention, an unknown field, changed canonical digest,
a reference outside the certificate directory, presenting rank 158 as
complete rank 159, presenting rank 157 as sufficient for four equations,
and an altered stored member value with a newly computed digest. The last
case failed on a fresh polynomial evaluation, demonstrating that a matching
input digest alone cannot authorize stored values as geometric evidence.

The shared implementation patch adds explicit dispatch for the two degree-14
profiles in `tools/verify/verify.py` and routes them to
`tools/verify/b15_01_ci159.py`. Existing degree-13 schema validation remains
accepted. Only the partial profile has a successful full replay here.
The authentic receipt is `results/b15_01/shared_verifier_report.md` and the
machine-readable result is `results/b15_01/verification.json`.

## Resource record

Slot 01 held the numerical lease. Numerical jobs used the exact worker
Python, one BLAS thread and the aggregate Windows Job Object cap. Heavy jobs
were sequential; resource changes and measured decisions are retained
in `resource_decisions.json` and `verification_v3_decision.json`.
The final replay cap was 5,400 seconds and
1,536 MiB. It completed in 2295.076 seconds, exit 0,
with aggregate peak commitment 949.92 MiB.
The backend evaluated 48,307 entries in this replay;
recorded contraction time was 2239.681 seconds.

| Run | Recorded PID | Wall seconds | Aggregate peak MiB | Exit |
|---|---:|---:|---:|---|
| b15_01_resource_control | 43912 | 0.070 | 17.93 | 0 |
| b15_01_audit | 25944 | 0.202 | 25.44 | 1 |
| b15_01_audit_v2 | 42100 | 18.516 | 273.89 | 0 |
| b15_01_pilot | 28196 | 825.903 | 394.16 | 0 |
| b15_01_extension | 33188 | 405.381 | 331.93 | 0 |
| b15_01_focus | 40864 | 814.958 | 287.68 | 0 |
| b15_01_hybrid | 42708 | 522.000 | 305.82 | 0 |
| b15_01_hessian_control | 42976 | 0.164 | 19.88 | 0 |
| b15_01_verification | 39520 | 244.680 | unavailable | 1 (manual stop) |
| b15_01_native_control | 3564 | 6.343 | 195.26 | 0 |
| b15_01_verification_v2 | 40464 | 1268.570 | 259.10 | 1 |
| b15_01_hessian_family | 38388 | 0.772 | 24.04 | 0 |
| b15_01_export_control | 15180 | 14.506 | 662.76 | 0 |
| b15_01_verification_v3 | 42420 | 2295.076 | 949.92 | 0 |
| b15_01_shared_controls | 8416 | 18.838 | 313.12 | 0 |

The initial audit failed because an unnecessary degree-13 sidecar path was
absent; the accepted certificate already contained the needed coefficients.
The failure and corrected audit are both retained. The first verifier used
a 2,700-second cap. After measured fresh-definition costs raised concern
about the remaining budget, it was ended at the verified recorded PID
39520 and restarted from fresh values with the documented 5,400-second cap.
Its exact worker executable and UTC start time were checked. A timestamp
conversion guard initially declined the stop, then corrected DateTime
handling matched the start within 0.537 seconds. Aggregate peak commitment
for that interrupted run is unavailable and is recorded as null. Its own
process peak is not substituted for the aggregate value. No values from
the interrupted replay granted acceptance in the final run.

The second replay freshly passed the rank-158 minor (determinant 823506578)
and dimensions 93/159, then exited 1 at the generic-input shape check after
1,268.570 seconds. S74 records omit zero coefficients, so some generic points
have 493 or 494 stored terms. The corrected exporter supplies all 495
coefficients without changing the forms, and the verifier now checks this
input shape before costly evaluation. Its old certificate bytes, sparse
generic snapshot, successful minor, report and resource log are preserved.
The final replay starts fresh again; no earlier value receipt grants its
acceptance. Larger point batches reduce call overhead within the same array
and aggregate memory limits.

## Reproduction and delivery

From the supplied B15-01 worktree, use the exact environment interpreter:

```powershell
& 'C:/Users/swami/Projects/gct-gpt/work/batch15_workers/B15-01/.venv/python.exe' analysis/b15_bound.py --slot 01 --name b15_01_receiver_replay --seconds 5400 --memory-mb 1536 tools/verify/verify.py results/b15_01/certificate.json --report results/b15_01/receiver_report.md --quiet
```

This command requires a numerical lease. Receiver outputs use their own
bounded-run name; per-call receipts include the current process ID. It
recomputes the values from the exported definitions and explicit points.
The certificate references canonical, compressed input snapshots under
`results/b15_01/ci159_inputs/`; each dependency carries a canonical SHA256.
The original working-byte hashes are separately in `input_hashes.json`.
Producer runs and audit modes are in the `analysis/b15_01_*.py` scripts;
their successful output files already form part of this delivery.

`backend_receipts.json.gz` preserves per-call arithmetic and resource
receipts. `run_resources.json`, bounded logs, `delivery_inventory.json`
and `stage_paths.txt` record provenance and the intended file set.
Reproducible tensor/executable caches and pre-existing setup logs are
excluded from the research commit. The final external bundle manifest
records the committed head/tree, one branch ref and only the frozen base
prerequisite. Packaging PASS is distinct from mathematical verification.

No new exclusion is proposed; `proposed_exclusions.json` is empty.
The next sufficient witness is one genuine N14 member independent of the
retained 158 at compatible points, followed by a full rank-159 replay, or
an exact global symbolic proof for both remaining independent sampled
relations. If new points are needed, their source values must also be
freshly evaluated. The current result does not determine which value of
D_LMR in [-4,-3] occurs.
