# B15-02 preregistration

Model for reasoning, implementation, verification and reporting: gpt-6-astra;
dispatch requests xhigh. No live Claude phase; inherited implementations retain
their original session attribution. Date: 2026-09-13.

## Readiness and scope

Use the existing B15-02 worktree and branch b15-02-a1-probes only. Fresh Git
reads matched commit f365568d80d5f66fea2dd9342ff1998e1d866915, tree
aff6ca0921ec964cc8b7fcbd64bd5e5e9de9fbbd, and annotated tag object
80209c13e9ae33bad8933cb47413bf7710c96cb1. Native READINESS.md records
the bounded runtime control PASS. Setup logs stay untracked and preserved.
No applicable AGENTS.md was found in the worktree or its checked ancestors.
Read the preamble, accepted state, brief, wording guide, original shortlist,
candidate preflight, sizing code, predicates, overlay and source/evaluator code.

Question: for n=4, degree 7, ambient V of dimension 16, does the determinant
coordinate multiplicity m_det reach U_pad=1 in each of the nine supplied cells?
The working source is Sym^7(Sym^4 C^7), stabilized to C^16 by the usual
Schur functor restriction convention. Coefficient functions c_alpha are ordinary
polynomial coefficients; E_ij c_alpha=(alpha_i+1)c_(alpha+e_i-e_j).
No factorial rescaling or u multiplication is performed. Partitions descend.
All nine have ambient multiplicity a=1. Pullback h is an upper bound, not a
coordinate multiplicity. Use D=m_pad-m_det=i_det-i_pad.

Order (degree 7 throughout), with signed Burnside dimension n_chi:

| Partition | n_chi | h_pad upper bound |
|---|---:|---:|
| (11,8,5,1,1,1,1) | 1576 | 1 |
| (13,5,5,2,1,1,1) | 10923 | 5 |
| (15,4,2,2,2,2,1) | 11682 | 5 |
| (13,6,3,3,1,1,1) | 11856 | 4 |
| (12,8,3,2,1,1,1) | 17367 | 2 |
| (13,7,2,2,2,1,1) | 17725 | 4 |
| (11,9,3,2,1,1,1) | 20079 | 1 |
| (12,7,4,2,1,1,1) | 26609 | 4 |
| (14,5,3,2,2,1,1) | 53827 | 6 |

Reapply the frozen typed ledger and accepted-state transport overlay before
evaluation; record each conclusion and skip any closed cell. The old
(16,2,2,2,2,2,2) cell is a screening control. Do not use an every-degree
length-four fullness claim or a nine-variable independent-padding clamp.

## Algorithm and certification

1. Recompute exact signed Burnside counts before carrier allocation and compare
   with the original shortlist. Recompute a by exact character/Weyl arithmetic
   where feasible; inherited a=1 must be identified if used.
2. Build integer signed orbit sums and all simple raising equations with the
   preserved S45 builder. Equal-part block permutations use sign(g)^part.
   Use the S71 initial-term cover, then exact residual elimination over a prime.
   A local NumPy/SciPy triangular/Schur implementation may replace the Unix C
   backend, after a direct dense control. Never allocate a full n_chi square
   for the larger cells. Primary prime 65521; reserve 65519 if a bad reduction
   is detected. These primes exceed 4*7 and do not divide orbit group orders.
3. Verify every source on the full raising matrix. Certify its full modular
   nullity, using a projected residual rank and an independently checked lifted
   kernel. Projection may increase nullity and is never trusted without checks.
   Save source chi coordinates and deterministic carrier construction, explicit
   row/column conventions, cover/projection recipe and input hashes.
4. Lifting: the rational HW space has dimension a=1 and lies in the signed
   carrier. If integer E has rank n_chi-1 both over Q and modulo p, a nonzero
   modular maximal minor is a unit over Z_(p). Solving those pivot equations
   with one free coordinate gives a rational HWV regular at p whose reduction
   is the verified normalized modular vector. Hence a nonzero modular
   evaluation proves a nonzero rational determinant HWV. Modular HW membership
   without this rank/dimension argument is insufficient.
5. Generate explicit integer 4x4 pencils with seven variables, seed 11 and
   entries in [-4,4]. Evaluate det(sum s_i A_i) in ordinary coefficients.
   Stop a cell at its first nonzero; save that point and residue and perform
   a fresh polynomial replay. At most eight determinant points per stalled
   cell, with sources retained. If all zero, test up to four true independent
   padded frames (seed 37, seven rows by ten columns, entries [-4,4]), defining
   l*per3 with the pad separate from the nine entries. Seek an exact global
   determinant argument within the remaining budget; samples alone give none.
6. A certified determinant rank floor 1 with U_pad=min(a,h_pad,a-0)=1 proves
   D<=0. A positive requires r_pad>U_det with U_det global; no zero-sample
   inference. Export stalled cells as CANDIDATE or RESOURCE_STOP.

## Controls and resources

Before research, use the bounded native runner for dependency imports and
algorithm controls. A separate known positive (6,2) in degree 2 has explicit
HWV 8*c40*c22-3*c31^2 and a nonzero determinant example. Compare the reduced
raising operator with direct expanded differentiation. Deliberately change a
source coefficient, orbit sign or factorial normalization and require the
relevant equality check to fail. Check determinant coefficients independently
by permutation expansion/direct integer determinant evaluation. Include a
synthetic zero evaluation that is accepted as CANDIDATE, independently of the
positive liveness control. Compare local residual elimination with dense flint
on small matrices and check overflow bounds before integer matrix products.

Slot 02 holds an initial heavy lease per the read launch LEASES.json. Read it
again before each heavy launch. At most one numerical job for this slot, one
process and one BLAS thread, 1536 MiB aggregate memory. Use exact executable
C:/Users/swami/Projects/gct-gpt/work/batch15_workers/B15-02/.venv/python.exe.
Controls: up to 120 seconds, 768 MiB. Pilot: 900 seconds, 1536 MiB, one cell.
Production only after measured costs justify it, at most 5400 seconds and the
same memory cap. Cap residual storage conservatively, keep construction,
reduction and evaluation times separate, checkpoint per cell. No unchanged
repeated failed attempts. Resource exhaustion is an outcome, never a theorem.

Deliver per-slot report, proof fragment, proposed exclusions, sources, explicit
points and replay; no shared theorem or ledger edits. Each tracked file is
below 5,000,000 bytes. Commit attribution trailers, run delivery checks and
package a one-ref delta bundle with only the frozen base prerequisite. No push.

## Input SHA-256

Text hashes normalize CRLF to LF, leaving other bytes unchanged.

| Input | SHA-256 |
|---|---|
| docs/batch15/WORKER_PREAMBLE.md | b41ab684785ad4be1fa91ec491c25c10fa463c0bdf2d5bb69b3e59e2abf6797d |
| docs/batch15/ACCEPTED_STATE.md | 97b07d5f50c21fc6a3a6bba267339ba385dcda0b6bad7a067c5905b1351352df |
| docs/batch15/briefs/B15-02.md | e76e674ce98bc6fe34c998b548f65d5ee70f66ee21f19feee7c0819da899517e |
| results/b15_prep/candidate_preflight.json | 1bbb7009392b2bba9192b0e62f5a5ac31f5ac27ad062f0a00f550cdee642060e |
| results/b14_11/shortlist.json | 2d4ec31171f2387c8368c3a93da94824f77721dd597ec8bf288cb292a460412a |
| analysis/b14_11_sizes.py | adc9e3bc5a5fac3e618eaf7f9f50c5f142176b207307d8b068225bbbbf4ba887 |
| tools/integrate/exclusion_predicates.py | e5addf6e749ce129db4bb8308d72aadb0984852e64d12957a92f131b0b76776f |
| results/integrate/inherited_exclusions.json | bfdf6bf971e192723bb48c9c9be4cf00f32ecb0f05647f4df790858145edb338 |
| results/b15_prep/transport_overlay.json | e8f2d129c60eaf36e0ec6644b5e9f706a6c540cc85a8329f17bcdc0c8ba6c007 |
| analysis/wk9_s45_build.py | 7a6b2e280d2e214430ad35f5f0edc596d04a856561b5a70a4413674a4f3ad1d3 |
| analysis/wk11_s71_hybrid.py | 26a69eaa177ccd276f87af364aa624baae083c2573969da796458e956ce26073 |
| analysis/wk12_s79_cell6.py | 0e29bd408efe78ab7bf3f3c55cfff7aa83f1aefb4f9f53634ea1d5c1a2a158b1 |
| analysis/wk8_s30_core.py | 4cca6f67127d7435fe24c6413d1f39c139184905fbcc25bcfd9323cdb058f304 |
| analysis/wk10_s64_pad.py | 73490ef336e6e875daa7877b10b86f873622f0930b648150e6b29c32144e6323 |
| analysis/wk9_s42_census.py | 2aab179653a5e6f64bf00b7e4902a16d29ff5bafd14e2c804ede3543303e7210 |
