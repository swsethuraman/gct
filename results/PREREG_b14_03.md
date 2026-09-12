---
board_numbering: batch14
session_id: B14-03
model: gpt-6-astra
reasoning_effort: xhigh
base: 9898e56941a7665f231873481dae956f08509995
base_tree: cb688cd3fe454d638f3202e759e2eaa0c629739f
branch: b14-03-astra
---

# Preregistration: complete interpolation verifier

Recorded 2026-09-12 UTC, before new mathematical measurements. Actual model
and effort confirmed from this task's local turn_context, not inferred from
the launch title. HEAD, peeled batch14-base commit, and both tree readings
match the identities above. No applicable AGENTS.md was found in the workspace
or its ancestors. The launch brief overrides the packet's checkout and bundle
shorthand; work remains on the prepared branch.

Question: can a fail-closed, independently implemented complete_interpolation
checker certify the exact ternary quartic control (8,8,8), degree 6, and reject
all specified corruptions? Historical observations (not blind predictions):
B13-03 reports ambient multiplicity 2, normalization multiplicity 1, restriction
rank 1, F1(l*c)=729 at its supplied point, and mixed-source relation (1,-1).
No new mathematical pilot has run in this session.

Instrument: a session-specific producer, independent checker importing no
analysis code, exact Python integer/Fraction arithmetic, and separately reduced
modular arithmetic at 2147483647 and 2147483629. Reuse the banked ordinary
source polynomials and producer utilities only after checking exponent tuples,
raising rules and normalization. Reconstruct every target entry from explicit
mixed bracket columns. Prove bracket membership by equivariance and verify a
nonzero example. Independently derive dim N using Pieri and full small cubic
raising matrices; independently certify source completeness by full raising
rank floors and exact independent highest-weight vectors.

Objects and conventions: source rows, point columns; A has a rows, and K has
a rows with A^T K=0. Ordinary coefficients c_alpha; house bracket contraction
uses m_alpha=alpha! c_alpha separately for cubic and linear letters. Products
of brackets have initial column coordinates. Pullback is
c_alpha -> sum_(i:alpha_i>0) l_i d_(alpha-e_i), with NO alpha_i multiplier.
Use a common rational model with explicit cleared row denominators, verify
prime invertibility, and label each stored matrix with values_are.

Decision table: PASS only if dimension, membership, full target minor, complete
source, exact evaluations, rational rank and left-kernel identities all pass.
Missing required data is UNPARSEABLE, never PASS. Invalid mathematical data is
FAIL; unsupported cells/proofs are NOT VERIFIED. Resource exits are explicitly
resource-limited, not mathematical negatives. Sampled deficiency without the
complete target remains only a nullity ceiling.

Required falsifiers: changed points; wrong source scaling; invalid target
membership (including wrong valences/column shape); rank-deficient target;
insufficient CRT modulus; one changed integer entry; every missing required
input. Additional controls: empty points/target/source, wrong dimension proof,
right instead of left kernel, corrupted residues, forbidden denominator prime,
wrong values_are, and consistent nonsingular source rescaling accepted. Retain
all results, including failed development runs, in session logs.

Bounded search: first use one six-cubic-letter cycle with two cubic triples and
six distinct linear letters (each linear letter appears once). If it vanishes,
try at most 64 deterministic degree-compatible bracket layouts; at most 120 s
per search. Literal full expansion has at most 6^8=1,679,616 assignments per
layout; evaluate at the sparse l=x1 point first (at most 2^6*6^2=2304). No large
LMR expansion or other-session dependency. Cap live symbolic terms at 250,000,
weight enumeration at 3,000 and dense matrices at 5 million entries. Individual
validation runs: at most 600 s, 768 MiB process memory via Windows Job Object,
one process and one numerical-library thread. Record PID, time and memory.

Toolchain preflight: CPython 3.12.14, numpy 2.3.5 available; python-flint,
sympy and psutil absent. Use exact stdlib alternatives allowed by the launch
brief; install nothing. Host has 20 logical CPUs and 33,752,997,888 physical
bytes, with 12,970,004,480 available at preflight (shared, not reserved).
WMI resource query was denied; native GlobalMemoryStatusEx succeeds.

Fallback: a proved general format and working complete h=1 control checker,
with unsupported larger profiles explicitly rejected. Degree-13/14 integration,
hybrid_kernel upgrades and any new LMR conclusion are outside this run. Frozen
LMR evidence remains a24=274, determinant rank 273, padded rank >=269,
D in [-4,+1]. A sampled five-dimensional kernel is not five certified equations.

Deliver exact certificates, independent rejection suite, proof/specification,
replay, resource logs and report; append only justified instrument facts to
PROVED. Run delivery checker before and after named-branch bundle creation.
Input byte SHA256 and portable Git blob identities are in
results/b14_03/input_manifest.json, committed with this preregistration.
