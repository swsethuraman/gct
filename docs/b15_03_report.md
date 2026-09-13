# B15-03: exact equality in the first two-dimensional comparison

For degree eight, n=4, lambda=(13,11,3,2,1,1,1), the result is **EXACT**:
ambient multiplicity a=2, determinant and independently padded permanent
coordinate multiplicities both two, ideal multiplicities both zero, and D=0.
Two explicit integral highest-weight polynomials and nonzero integer minors
certify both ranks. The primary assignment is complete.

Model throughout preparation, proof, coding, checking and delivery:
gpt-6-astra, xhigh. Inherited B13-10/B14-12 implementations retain their Claude
attribution. No additional research task or agent was created.

## Evidence and scope

The ambient space has 16 variables. The independent padded form is z*per_3,
with ten essential variables. Evaluations use seven-variable restrictions
through explicitly saved frames; the comparison remains about the ambient
orbit closures. Ordinary coefficients, the corrected raising rule and source
orientation are fixed in docs/b15_03_proved.md and integral_source.json.
No climbing symbol u or change of degree is used.

The integer source and fresh geometric replay give these minors:

| Family | Integer 2-by-2 minor | Rank floor |
|---|---:|---:|
| det_4 | -11513882102246656749727216917727852673280 | 2 |
| independent z*per_3 | -8764935843899184496923422711808 | 2 |
| diagonal determinant pencils | 0, all four values zero | 0 |

Every source monomial has the stated weight and degree. Every simple raising
operator vanishes over Z in an independent full monomial calculation. This
removes the modular lifting premise from the final certificate. Rational
reconstruction was a discovery step, followed by exact verification; it is
not itself treated as a proof.

The count file independently recounts a=2 and h_pad=2 by integer Weyl
alternation and a rational character cross-check. There are 24 Pieri channels,
with exactly two nonzero cubic multiplicities, each one. The signed Burnside
count is N_S=519879 and n_chi=43364. The scoped ledger and accepted-state
overlay return no closure. Here U_pad=min(a,h_pad,a-i_pad_lb)=2 even before
the padded rank floor is supplied.

The comparison is stronger than an exclusion alone: a=2 bounds both ranks
from above, and the two integral minors bound both from below. Thus D has
the exact interval [0,0]. No sampled deficiency was interpreted as a global
equation. The accepted degree-eight padded/reducible transfer is unnecessary
for this direct padded certificate.

## Construction and resource decisions

The existing assigned worktree and branch were retained. Frozen commit
f365568d80d5f66fea2dd9342ff1998e1d866915, tree
aff6ca0921ec964cc8b7fcbd64bd5e5e9de9fbbd and tag object
80209c13e9ae33bad8933cb47413bf7710c96cb1 matched before work.
Preregistration was the first commit:
fb4432aa7189f7ac4bfb37abe60cfb87b61693c0.

Only proof, code, exact counts and small controls ran before the integrator
granted the primary pilot lease. The native Job Object wrapper set one process
and one BLAS thread. It checked available RAM before each run. The discovery
construction used the inherited lean builder with memory blocks and a
20000-row chunk, avoiding its caller-scratch cleanup path. The shared code
was not edited.

The source build took 8.643 seconds and produced a 169570-by-43364 sparse
raising operator with 496826 nonzeros, occupying 3659240 CSR bytes. A dense
43364-square int64 array alone would require 15043491968 bytes, or
14346.59 MiB. No such array was allocated.

The cover took 0.090 seconds, certifying 43359 independent rows and leaving
only five uncovered columns. The local NumPy/Numba adapter priced its live
reduction arrays at 8880820 bytes excluding interpreter baseline before
allocation. It used a 37-by-5 projected Schur matrix, exact flint nullspace,
and full raising verification. The first-prime reduction took 2.665 seconds
including JIT compilation; the second took 0.194 seconds. Fresh geometric
evaluations took 0.376 and 0.362 seconds. Both primes gave rank two on generic,
determinant and padded points, and zero on diagonal pencils.

| Bounded run | Wall seconds | Aggregate peak MiB | Cap seconds / MiB | Exit |
|---|---:|---:|---|---:|
| Native resource smoke | 0.066 | 18.41 | 30 / 512 | 0 |
| Count controls | 0.089 | 20.95 | 60 / 512 | 0 |
| Primary exact counts | 0.739 | 36.05 | 60 / 512 | 0 |
| Secondary exact counts | 0.726 | 34.72 | 60 / 512 | 0 |
| Engine controls | 5.216 | 92.26 | 60 / 512 | 0 |
| Authorized primary pilot | 17.397 | 248.73 | 900 / 1536 | 0 |
| Authorized exact follow-up, including saved-source replay | 1.688 | 118.77 | 60 / 512 | 0 |

All resource records include PID, UTC start, return code, measured wall time,
memory before/after and aggregate Job Object peak. The 60-second follow-up
was separately approved after the measured pilot. The integral sources have
denominator-clearing factors 48 and 192 and 6105 nonzero carrier-coordinate
rows; their combined expanded support has 36630 monomials.

The lease was explicitly released at 2026-09-13T13:56:38.4781960Z after all
seven recorded research PIDs were freshly found absent. Last job:
b15_03_exact_followup, PID 19960, start 2026-09-13T13:55:58Z, exit zero.
The release record is results/b15_03/lease_release.json. There was no resource
stop, production extension or secondary numerical construction.

## Controls and corrections to the inherited route

Known positive source liveness was separate from the research cell. The binary
quartic control checked the integral HWV 8*c40*c22-3*c31^2, its raising equation,
and direct coefficient evaluation. A separate six-row degree-six control had
determinant rank one and diagonal rank zero. Changed source and point data,
incorrect normalization, and the signed Burnside character were detected.
Near-prime products and a nontrivial triangular system checked modular
arithmetic without int64 overflow. NumPy 2.4.6, SciPy 1.18.1, python-flint
0.9.0 and Numba 0.66.0 were actually used.

The inherited B14-12 driver asserts that the research cell's determinant rank
is positive as part of a liveness gate. That would mishandle a valid zero-rank
result. The local adapter uses a separate known cell and permits determinant
rank zero in the primary computation. Its final exact certificate uses only
Python and NumPy and does not require the inherited Linux C backend, Numba,
flint, or sparse construction to replay the saved integer source.

The brief's counts and decision thresholds were correct. The direct-HWV
fallback was unnecessary because the sparse source pilot succeeded. The
secondary cell was independently counted, as preregistered, at a=4,h_pad=2,
N_S=2806818,n_chi=128559. It was not evaluated and no conclusion about its D
is proposed.

## Replay and delivery

Use the assigned worktree as the shell working directory. This is the short
saved-source geometric replay command (choose a fresh log name):

```powershell
& 'C:\Users\swami\Projects\gct-gpt\work\batch15_workers\B15-03\.venv\python.exe' 'C:\Users\swami\Projects\gct-gpt\work\batch15_workers\B15-03\analysis\b15_bound.py' --slot 03 --name b15_03_receiver_replay --seconds 60 --memory-mb 512 'C:\Users\swami\Projects\gct-gpt\work\batch15_workers\B15-03\analysis\b15_03_exact.py' replay
```

The checked saved-source pass took 0.735 seconds of verifier time, within the
1.688-second follow-up process. It loads the committed integer polynomials,
rechecks all integer raising identities, and rebuilds determinant and padded
coefficients and values. This is a native geometric replay, not a rank check
on stored matrices. Recount with analysis/b15_03_counts.py primary under the
same bounded runner; that pass took 0.739 seconds including wrapper overhead.

The compact discovery construction is analysis/b15_03_run.py, which requires
an explicit live lease for any future pilot. Final verification is
analysis/b15_03_exact.py. Exact-byte SHA-256 input hashes appear in the
preregistration, pilot and exact certificate. They describe the local bytes at
run time, including the recorded line-ending convention; binary carrier hashes
are independent of checkout text conversion. The proof fragment names all
inherited mathematical conventions separately from fresh evidence.

The intended final delivery directory is delivery/b15_03_final, created after
the last commit by the required packager. Its external manifest records the
exact final head/tree and single base prerequisite. Packaging PASS checks the
delivery structure and hashes, not the mathematics. The mathematical evidence
is the exact certificate and saved-source replay.

The primary cell needs no further witness. For the unevaluated secondary cell,
two determinant directions suffice for exclusion. Positive D with padded rank
two would require three globally proved independent determinant equations.

All new artifacts are below 5000000 bytes. Setup runtime/smoke provenance was
preserved and excluded from research staging. Protected papers, shared theorem
records, shared lease/intake files and Git trust configuration were unchanged.
No push or publication was performed.
