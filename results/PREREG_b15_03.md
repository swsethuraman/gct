# B15-03 preregistration

Model for preparation, proof, implementation and verification: gpt-6-astra,
xhigh reasoning. Banked implementations retain their original attribution;
the B14-12 driver and B13-10 lean machinery are inherited Claude work.

## Readiness and scope

The existing B15-03 worktree is on b15-03-two-dimensional. The launch commit
f365568d80d5f66fea2dd9342ff1998e1d866915, tree
aff6ca0921ec964cc8b7fcbd64bd5e5e9de9fbbd, and annotated tag object
80209c13e9ae33bad8933cb47413bf7710c96cb1 were checked before work.
The native READINESS.md receipt and lease record were read. No heavy lease is
held. Setup logs remain untracked and are not research outputs.

The main cell is n=4, degree=8, lambda=(13,11,3,2,1,1,1), length=7, in
Sym^8(Sym^4 C^16), using the polynomial representation convention dual to
quartic forms. The seven-variable restriction computes its highest-weight
multiplicity; it does not replace the sixteen-variable orbit closure or the
ten-essential-variable independent padded permanent by a different variety.
The input claims a=2, h_pad=2, N_S=519879, n_chi=43364.
The secondary cell (11,8,8,2,1,1,1) has claimed a=4, h_pad=2,
N_S=2806818, n_chi=128559. Its construction requires a separately priced run.

## Question and decisions

Compute U_pad=min(a,h_pad,a-L_pad,other valid upper bounds), with only proved
premises included. Reapply the typed scoped ledger and accepted-state overlay.
The desired negative certificate is r_det_lb>=U_pad, hence D_ub<=0.
A positive certificate needs global i_det_lb=q and padded r_pad_lb with
q+r_pad_lb>a. For the main cell q=1 and r_pad_lb=2 suffice; for the secondary
cell q=3 and r_pad_lb=2 suffice. Stable deficient sample ranks supply no global
equations. A rank-one observation will retain its source and missing direction
as CANDIDATE, together with the exact global verification still required.

## Counts, source and evaluation

Independently recount ambient multiplicity by Weyl alternation with exact
integer generating-function weight counts, cross-checked against the banked
rational power-sum character formula. Enumerate all horizontal eight-strips and
sum exact cubic multiplicities for h_pad. Recompute signed Burnside dimensions;
do not use N_S divided by stabilizer order as n_chi.

First price the inherited lean sparse raising construction and its initial-term
cover. Preserve monomial ordering from wk8_s30_core.exps, the equal-row
stabilizer character, and ordinary coefficient convention
E_ij c_alpha=(alpha_i+1)c_(alpha+e_i-e_j). No dense n_chi square is allowed.
Use a bounded sparse triangular/Schur method only after measuring the uncovered
dimension. A local NumPy/Numba adapter may replace the Linux C backend after
separate exact controls; it must verify every resulting vector on the full
integer raising operator. Never edit shared implementations for this adapter.

A modular kernel needs a rational source justification: exact ambient nullity
equal to modular nullity proves good reduction of the saturated integer kernel,
provided the assembled integer operator and stabilizer coordinates are proved
complete over Q and localized away from the prime. Alternatively construct
integral highest-weight polynomials directly by Young column alternation and
quartic/block symmetrization, retaining the normalization explicitly. If the
sparse construction exceeds the pilot gate, record a precise memory/backend
obstruction and a compact direct-HWV plan with actual contraction sizes.

Use p=2147483647 and 2147483629, one prime first. Retain explicit integer points:
generic quartic coefficient dictionaries; det_4(sum x_i A_i) for integral
4-by-4 matrices A_i; independent padding z*per_3 under a seven-frame in C^10
with a separate z coordinate; reducible l*c; and diagonal determinant pencils
equal to a product of four linear forms. A restriction frame can extend to an
invertible ambient change of basis, or lies in its polynomial closure.
Evaluate native coefficients afresh, not only stored evaluation matrices.
Record coefficient factorials, source orientation, prime, seeds and all inputs.
No multiplication by the climbing symbol u is used in this fixed degree.

## Controls and resource gates

Run the native b15_bound.py resource smoke under 30 seconds and 512 MiB before
research controls, using exactly the worker-local .venv/python.exe. Confirm
NumPy, SciPy, python-flint and Numba as required. Small counts and control cells
use at most 60 seconds and 512 MiB per bounded run; raise that only with measured
justification and an explicit resource record. Known positive liveness uses a
separate small source, e.g. quartic degree two lambda=(6,2). Check source
annihilation, independence, evaluator agreement with direct ordinary polynomial
evaluation, and detection of altered source, normalization, sign and point data.
The main cell may have determinant rank zero without failing a liveness gate.
On length>4, a diagonal determinant pencil is a forced zero control.

Request a heavy lease before the main source pilot. Default leased pilot:
900 seconds, 1536 MiB aggregate Job Object cap, one process and one BLAS thread.
Construction, reduction and evaluation are timed separately. After measurement,
a production extension can use at most 5400 seconds under the same memory cap.
Stop before allocations whose conservative envelope exceeds the cap; do not
repeat unchanged failed runs. Read the integrator-owned lease record before
each heavy run. Do not self-assign or transfer leases.

## Delivery

Report every attempt and stop in docs/b15_03_report.md. Put proof records in
docs/b15_03_proved.md, code in analysis/b15_03_*, native sources/points and
records in results/b15_03/, and research logs under results/logs/b15_03_*.
Use EXACT, REPLAYED_RANK_FLOOR, RECORDED, CANDIDATE or RESOURCE_STOP with
inherited dependencies explicit. Proposed exclusions are per-slot JSON only.
Commit intended artifacts only, each below 5000000 bytes, with model trailers.
Run the specified delivery checker and fresh-directory bundle packager after
the last commit; return head, tree, report, checks and next sufficient witness.

## Input hashes

The following SHA-256 values are for exact local file bytes (including native
line endings), not the launch manifest's normalized-text convention.
- docs/batch15/WORKER_PREAMBLE.md: 9946cbeba95c3b53e0da6322b92b874c3e69ab8c5314d98c27d70a7285778703
- docs/batch15/ACCEPTED_STATE.md: 9805ecc550bae5dbdfe845e280f42a0c2b03e0b6989e819e5a3d93e62f59148c
- docs/batch15/briefs/B15-03.md: d5127f3e8512861e81f2c3617cddbd014fa8add97aad30d5a86f1f3351448c81
- docs/brief_wording.md: 0f3c6dbb15920aa25d52676cb638004d7bc989c22f9d88fe584ff36a5317cf5a
- results/b15_prep/small_panel_sizing.json: 6a441a32bf891a53cd0fa56cb32912c862d2a862edb61bf5779a031c5b53c903
- results/b15_prep/transport_overlay.json: b594dcdae7b4b448039d705d6f15f319e245a0d2cf3636f8b08b15cbfc42b4df
- results/integrate/inherited_exclusions.json: b71469d2d3db97e4d16f6b9b4be6f77ac1cfc00ea286b2e9cedefcec43b1458b
- analysis/b14_11_work.py: b6e0621c8ffeb02a7f16a4c28b78c8bb2fa57c463278a6997cd42462ce7dba1b
- analysis/b14_12_cell.py: 87270f2417fd40cabab9e64ff6e272b3a44ca21c333d49a23122affb1f9c783f
- analysis/b14_12_families.py: fa2a8c229ea61440ad57d0a451546c26b0483dce220dec70f8518317770cd1c4
- analysis/b14_11_sizes.py: 072501b587e7514d7167289b34a0bd52312f815eb3a04d953404c0de4b7830a2
- analysis/wk8_s30_core.py: 9b40e885fd5d7c501fd3c4db2ce36b6bd944a101e41d92d7bd31669066423d8d
- analysis/wk8_s30_pleth.py: 2edd98529b228e91842d70ef1516381d54c81315928ea4202729cfe4d01bd166
- analysis/wk9_s57_lib.py: 17b2a5fb91d71b0edca50fb9a630505be6782bb3444c991bd0e1d536b2a2fcea
- analysis/wk13_b10_lean.py: 7b7cca6d95f9454e94a771137cd4fe4d4917d29a589e87e7c67c6ac4764bf46f
- analysis/b15_bound.py: ca001081f49e0048812b871a31e3be85435b210b3a538170a9f006408a41f854
