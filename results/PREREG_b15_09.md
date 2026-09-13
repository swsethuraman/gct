# B15-09 preregistration: a complete determinant pullback instrument

Date: 2026-09-13. Assigned branch: `b15-09-global-det` in the existing B15-09
worktree. Model for proof, implementation and review: gpt-6-astra; requested
reasoning xhigh, as supplied by the native dispatch. No secondary agent or live
Claude session is used. B14-06 retains its Claude Opus 5 attribution.

## Readiness and immutable inputs

The tag resolves to commit `f365568d80d5f66fea2dd9342ff1998e1d866915`, tree
`aff6ca0921ec964cc8b7fcbd64bd5e5e9de9fbbd`, annotated tag object
`80209c13e9ae33bad8933cb47413bf7710c96cb1`. The assigned branch and HEAD match.
The native READINESS receipt was read. Its runtime and smoke logs are setup
provenance and will remain untracked. No applicable AGENTS.md was found in the
worktree or its ancestor directories. No worktree operation is needed.

SHA-256 below uses the exact local file bytes (including existing line endings).
The verifier will additionally record LF-normalized text digests for replay
across Git line-ending settings.

| Input | SHA-256 |
|---|---|
| docs/batch15/WORKER_PREAMBLE.md | 9946cbeba95c3b53e0da6322b92b874c3e69ab8c5314d98c27d70a7285778703 |
| docs/batch15/ACCEPTED_STATE.md | 9805ecc550bae5dbdfe845e280f42a0c2b03e0b6989e819e5a3d93e62f59148c |
| docs/batch15/briefs/B15-09.md | e30ba60a71d8278b21214834af6e69b48f2155b4a5d111cc46703f7a34a3b685 |
| docs/brief_wording.md | 0f3c6dbb15920aa25d52676cb638004d7bc989c22f9d88fe584ff36a5317cf5a |
| docs/s57_report.md | 21e0a591844fde1375426306cb331d13f273cbe6d42ea7945158b11338551e46 |
| analysis/b14_06_bracket.py | d67a78c39694b1d4229970fd1bec46213913935030afcfae5165d2697d68b493 |
| analysis/ci73_replay.py | 2d2a27be1224b60333d5f9df8542f284607366025a09d3b5cefdebb0070df4bb |
| docs/ci73_proof.md | 644acd3aaf603e1200e77c5be9b0ccb73b8b312d4f63cff7ed6205fc25475b81 |
| results/ci73/certificate.json | 8f4d168ecfb922213b5baee66ac6250dd99dcf2ace669eebc2426c782e9b231d |
| results/b15_prep/candidate_preflight.json | 6535761f3a1413239cbb5009707b4de65116e8061f3154f02b9d8c974146b5b4 |
| results/b15_prep/transport_overlay.json | b594dcdae7b4b448039d705d6f15f319e245a0d2cf3636f8b08b15cbfc42b4df |
| results/b15_prep/shortlist_overlay.json | e60ebf6dcc2c4c19b0fc317fa5f7907b1525e23dcdec37e6179c5bb5322192b0 |
| results/integrate/inherited_exclusions.json | b71469d2d3db97e4d16f6b9b4be6f77ac1cfc00ea286b2e9cedefcec43b1458b |
| tools/integrate/exclusion_predicates.py | 432ff7e06f90cffbf056a52ea25233527b1e3648b48f6a43888a1555a2fd2d3f |

CI73 supplies the proof architecture, not its reducible dimension 73 for a
determinant computation. S57 supplies the chart idea, whose density and
denominators will be proved explicitly. B14-06 supplies the normalized polar
tensor convention; no modular vector is promoted to a rational polynomial.

## Questions and definitions

1. Certify the complete pullback of the multidegree (2,2,2,2) coefficient
   weight space of a quadratic form q in four variables under
   q(y)=det(sum y_i A_i), A_i=[[a_i,b_i],[c_i,-a_i]]. Count its independent
   monomial source before allocating it. Determine its kernel over Q by two
   exact routes: coefficient expansion and complete interpolation.
2. Prove that the discriminant relation homogenizes to an independent global
   ideal vector for D_{2,5}, the closure of all five-variable 2x2 determinant
   pencils. The finite cell is n=2, polynomial degree delta=5, ambient variable
   count N=5, partition (2,2,2,2,2). Expected ambient multiplicity a=1,
   determinant coordinate multiplicity m_det=0, ideal multiplicity i_det=1.
   This deliberately redundant-variable control is not a new quartic equation
   or a positive padded multiplicity gap.
3. Cost the same procedure for the frozen open proposal n=4, delta=8, N=7,
   lambda=(13,11,3,2,1,1,1), recorded a=2 and h_pad=2. Reapply the scoped ledger
   and accepted overlay. Derive a valid full polynomial space on the traceless
   chart and count it exactly. Do not infer its dimension from the number of
   geometric parameters or from reducible interpolation.

All coefficient weights are positive, as in CI73. Ordinary coefficients,
normalized polar tensors, and factorial symbols will be related explicitly.
The small integral chart uses M=2Q, where q(y)=y^T Q y. The compact source is
monomials in symmetric entries M_ij; the expected kernel is det M. The finite
source will be expressed by the symmetric coefficient matrix of a general
five-variable quadric, with denominator clearing stated. For quartics,
u=24c_(4,0,...) remains unchanged. No cross-model basis identification is made.

## Algorithm and controls

Use a sparse integer polynomial engine to substitute the exact chart in all
source monomials and form the full coefficient matrix. Independently evaluate
all sources on the Cartesian product of the six nodes e1,e2,e3,e1+e2,e1+e3,
e2+e3 in each of four three-parameter blocks. Degree two in each block gives
the complete containing space of dimension 6^4=1296; certify its evaluation
minor by the tensor product of the six-dimensional quadratic Vandermonde.
Compute both kernels over Q, with source rows and point/monomial columns
recorded. Equality of kernels is checked, but completeness rests on the proven
degree bounds and invertible full containing-space minor.

Liveness: symbolic 2x2 Cayley-Hamilton, a nonzero three-direction trace-Gram
minor, and a generic ambient quadric where the discriminant is nonzero.
Defect controls: change the determinant sign or off-diagonal normalization;
alter a nonzero kernel coefficient; duplicate an interpolation node. Each
affected check must reject. The determinant research kernel may be nonzero;
the liveness checks are separate. A quartic normalization control will check
the trace formulas and the shift on explicit integral matrices.

The discriminant is a closed rank condition, hence vanishing passes to the
orbit closure. Its multiplicity interpretation will be proved separately from
weight-space nullity. No new containment statistic is proposed. True quartic
padding is the GL orbit closure of z*per3 with ten independent variables;
the degree-eight m_pad=m_red premise, if used for sizing, is inherited only.

## Resource envelope and decisions

The lease record was read: holders 01 and 02, B15-09 has no heavy lease.
Perform only exact sizing and small controls now. Each numerical control uses
the exact local `.venv/python.exe` through `analysis/b15_bound.py`, one BLAS
thread, at most 60 seconds and 512 MiB aggregate. The native 30-second runtime
control already tested the runner; research controls will record their own
logs. No dependency installation is expected; verify actual imports.

Before a larger run, request an integrator lease in this task, reread the lease
record, and wait for a grant. A granted pilot would use 900 seconds/1536 MiB;
production up to 5400 seconds requires measured justification. Stop the dense
route before allocation if even a single eight-byte row of the complete
containing space exceeds 1536 MiB, or if the required source polynomials are
not explicit rational constructions. This is a stop for that representation,
not a proof that the actual image is large or all algorithms are infeasible.

Accept global vanishing only after exact polynomial cancellation or exact
complete interpolation, chart density, source independence and denominator
clearing. Sampled rank deficiency alone is CANDIDATE. For the quartic proposal,
U_pad=min(a,h_pad,a-L_pad,other valid bounds); positive D needs a certified
U_det<r_pad, equivalently i_det_lb+r_pad>a. Do not claim either quartic bound
without its witness. If the quartic computation fails sizing, deliver the
functioning small instance, precise cost analysis and the next sufficient
witness. No heavy request is needed for an already rejected dense allocation.

## Delivery

Write only slot-owned analysis, results, proof and report files and intended
research logs. Preserve setup provenance. Commit this preregistration alone
first, then implementation and checked results with actual model trailers.
Return a delta bundle from the prescribed checker/packager after the final
commit, without pushing. The integrator alone writes shared theorem/exclusion
records and lease/intake files; proposed exclusions remain slot-local.
