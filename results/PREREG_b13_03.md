---
board_numbering: batch13
session_id: B13-03
model: gpt-6-astra (Astra; runtime identifier to be audited before delivery)
base: 00495110c62acfbbbc951e82cc218ed091563b3f
branch: b13-03
registered_local_date: 2026-09-09
---

# Exact reducible membership method: preregistration

Question: compute the rational kernel of multiplication pullback on a specified
highest-weight space, and demonstrate an accepted nonzero ideal element and a
rejected non-element. This is B13-03, independent of other Batch 13 sessions.

The required five documents have been read. Inputs resolving the board's broad
names are `docs/reducible_ideal.md` (Theorem star),
`docs/s64_integrator_note1.md` (batch-10 factorization),
`results/astra/S4/S4_report.md`, its `src/calibrate.py`,
`artifacts/s64_control.json`, and `artifacts/s64_r5_exact_kernel.json.gz`.
`analysis/wk8_s30_core.py` supplies the audited coefficient convention.
These paths and input hashes will be recorded in the manifest. The board did not
name the small-control filenames; their resolution from S4 is recorded here.

The user-provided isolated checkout is verified clean at the frozen base on
branch b13-03. No local main ref exists (`git rev-parse main` failed); record the
verified HEAD instead. No clone, shared checkout edit, or remote push is needed.

## Objects and instruments

1. Primary complete control: n=4, r=3, delta=6, lambda=(8,8,8).
   Independently enumerate its weight monomials and simple raising equations;
   compute the exact rational highest-weight space or certify the archived two
   integer vectors by exact raising identities plus two-prime rank upper bounds.
   Verify coefficient ordering by exponent tuples, never literal letter indices.
   Compute the full symbolic pullback under c_alpha -> sum y_i d_(alpha-e_i)
   and the fixed-factor restriction c_alpha -> d_(alpha-e_1) if alpha_1>0,
   zero otherwise. Compare kernels over Q, and compare all-coordinate star test.
   Report complete map dimensions, sparse supports, coefficient sizes and costs.
   Check the first source vector as candidate accepted element and the second as
   candidate rejected non-element; their status remains conditional on replay.
   Use a source mixing (F0+F1,F1) as a cancellation control so membership is
   computed by a kernel, not merely by testing basis vectors separately.
2. Basic controls: c_(4,0,0)^delta, delta=1 and 2, must be rejected, and its
   full pullback must match the multinomial expansion. Enumerate additional
   tiny complete spaces (n,r,delta,lambda)=(4,2,2,(4,4)) and (4,3,2,(4,4,0)).
3. Hypothesis guard: a polynomial vanishing on every coordinate-factor subspace
   but not highest weight must not be certified by the star shortcut; explicitly
   use c_(4,0,0)c_(0,4,0)c_(0,0,4), which is nonzero at
   (x1+x2+x3)(x1^3+x2^3+x3^3). Malformed, missing, duplicated or mismatched
   coefficient/exponent data must fail, never silently omit terms.
4. Extension after the primary control is banked: audit the existing r=5,
   delta=6, lambda=(8,4,4,4,4) integer polynomial by every exact simple raising
   equation and fixed-factor/star supports. This is a membership check of one
   vector, not a complete computation of that highest-weight space.

Full pullback output is a sparse ordinary-coefficient matrix, columns source
vectors, rows pairs of linear-variable exponent and cubic coefficient monomial.
No rational kernel is inferred from a finite sampled deficiency. House primes
2147483647 and 2147483629 are cross-checks; the load-bearing identities use Z/Q.
No Q permanent stage is constructed. No new D>0 or cubic permanent ideal claim
is attempted. D=mult_pad-mult_det, LMR det rank 273 exactly and padded floor 269
remain ADOPTED from the frozen board. LMR i_red, i_pad and D are not recomputed.

## Bounded launch and negative outcome

One numerical process, one BLAS thread. Native GlobalMemoryStatusEx reported
33,752,997,888 bytes physical and 7,445,872,640 bytes available in preflight.
Use the Windows Job Object runner in `analysis/b13_03_bound.py`: 768 MiB hard
process memory cap, PID saved under results/logs, 600-second wall cap per control
unit. A watchdog exits only its own process. Recheck available memory at launch;
refuse if below twice the cap. No target-scale allocations. Each sparse expansion
has a 250,000-live-term guard; full matrices at most 1,500 columns and 2,500 rows
for exact source construction, with at most 5,000,000 dense entries. Stop and save
the precise stage and counts if a cap is reached. Commit each completed unit.

Dependency preflight: bundled CPython 3.12.14 and NumPy available; python-flint,
SymPy, SciPy, psutil, Singular and msolve not available through detected runtime or
PATH. Attempted local `pip install --target .b13_03_deps --only-binary=:all:
--timeout 20 --retries 1 python-flint sympy scipy`; blocked by WinError 10013
network access control. No package installed. Existing cache/project search found
no usable flint runtime. Use Python integers and Fraction for exact algebra, with
explicit proof certificates, rather than change the question to sampled rank.
This is a documented toolchain deviation from the preamble's flint preference.

Success: reusable exact algorithm plus complete primary control in both
directions. A computation stopped by a resource cap is not a mathematical
negative. Fallback: fixed-factor highest-weight method with a completed exact
example, precise unresolved dimensions, and measured continuation cost. Any
unregistered measurements receive a dated committed addendum first or an
exploratory label. No history rewriting, schedules, publication or push.
