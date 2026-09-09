---
board_numbering: batch13
session_id: B13-12
model: GPT-6 Astra (gpt-6-astra; no serving build identifier exposed)
base: 00495110c62acfbbbc951e82cc218ed091563b3f
---

# Five-variable closure repair preregistration

Registered 2026-09-09, before new mathematical computations. Branch b13-12,
prepared isolated checkout as authorized. `main` is absent locally; the supplied
frozen base and HEAD coincide. No clone or change to shared repository needed.

Question: retain all limits in the monic chart of the five-variable 4 by 4
determinant coefficient image, and correct s78's actual-image-to-closure step.
Work over Q with ordinary coefficients, and over C for geometric statements.
No multiplicity experiment is planned. D=mult_pad-mult_det; inherited LMR
determinant rank 273, padded floor 269, D=1-i_pad(24) in [-4,1].

Inputs read: the five mandatory batch documents, S2 report/replay/graph generator
and exact controls, s78 report/review/reduced polynomial generator/arc control,
batch11_plan section 6, rees_boundary_audit, critic_rees_response. Hash the exact
computational inputs used. The board names input collections, not file paths;
resolve them by repository search and record this interpretation in the report.

Preregistered objects and instruments:

1. Rebuild all coefficients of det(v I4 + sum_(i=1)^4 s_i B_i) by an independent
   sparse permutation expansion. Compare all 69 nonanchor polynomials exactly
   with results/s78_reduced_polys.json, verify the 4/10/20/35 degree counts and
   direct integer determinants at two deterministic point families, plus both
   house primes 2147483647 and 2147483629. Seed families 1312001 and 1312002.
2. Replay the available S2 exact rank/arc controls into new B13-12 output paths,
   never overwriting inherited files. Missing artifacts are recorded explicitly.
3. Prove the corrected reduction: eliminate the FULL monic coefficient graph
   before restricting its target to the 34 good coordinates. Give a complete
   133-variable rational elimination job (64 source, 69 target), and a proper
   projective-source formulation retaining infinity. Determine its exact
   necessary support equations at infinity. No unsupported bounded-rank
   classification will be adopted.
4. Test a possible universal boundary support in the normalized compactification:
   g(t)=diag(t^-1,1,1,t), z=t^2, N_i=t^2 g(t) C_i g(t)^-1. Check the full generic
   polynomial identity P_j(N)=t^(2j) P_j(C), the rank-one square-zero limit,
   and whether properness forces its closed boundary image to equal the full
   monic image closure. This is a structural control, not contact sampling.
5. Complete exact small elimination controls for ordering of closure and target
   intersection. If useful, prove the monic triangular-family image is closed
   and give its fixed-factor dimension; explicitly distinguish graph of that
   family from the full graph restricted over triangular support.

Stopping rules: one sequential computational worker, one BLAS/OpenMP thread;
Windows job-object process-memory cap 1 GiB and per-launch wall cap 120 seconds
(S2 replay may use 300 seconds). Record PID, elapsed time, outcome and memory.
First memory measurement: 33,752,997,888 total physical bytes, 7,569,129,472
available. Recheck before launches; no allocations approaching that free memory.
No 133/149-variable Groebner production run in this budget. Generate exact
residual inputs; count their terms/degrees/variables and state the first
uncompleted contraction. Bounded small exact algebra is enough for controls.

Bundled Python 3.12 is available. numpy is installed; flint/sympy/scipy/psutil
are absent, Singular/msolve absent from PATH. A pip installation was attempted
and failed at the host's network socket restriction (WinError 10013), before
any package download. Use existing standard-library exact arithmetic for the
finite controls; do not claim a CAS run or interpret missing imports as math.
Check local installed package locations before abandoning optional CAS controls.

Success: valid global reduction plus a completed nontrivial exact control or
component. Bounded fallback: explicit residual ideals and next elimination job.
A failure of an actual-image implication is not a counterexample to containment.
Sampled deficiencies are never rational ideal membership; no global image bound
will be asserted from samples. Report which elimination steps were not run.

Bank preregistration, then each completed object; deliver a one-part bundle
(part00 is the whole-file copy) against the frozen base, whole/part MD5 and
SHA256 checksums, report and manifests under Batch13_Results/B13-12. No push,
publication, delegation, additional schedule, or shared-source edits.
