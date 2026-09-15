# B17-02 support price recorded before the only pilot

2026-09-13. Worktree B15-02, research slot B17-02. This is a price for one
small identity verification, not a heavy lease or a representation census.

Use sixteen independent linear coordinates a, r1..r3, c1..c3, v1..v3,
s11,s22,s33,s12,s13,s23. Let A(v) be the three-by-three cross-product
skew matrix and S the generic symmetric matrix. Verify the identity

    det([[a/t,r/t],[t*c,A(v)+t*S]]) = Q0 + t*Q1 + t^2*Q2,
    Q0 = a*v^T*S*v - (r*v)*(v^T*c),
    Q1 = r*A(S*v)*c,
    Q2 = a*det(S) - r*adj(S)*c.

The same run verifies the Taylor expansion at J=(S=I, all other
coordinates zero), retaining the same a,r,c,v,S in all four orders.
No 34-coordinate chart map, relation search, orbit rank matrix, character
calculation, or old worker evaluator will be run.

Pricing is by explicit support, before execution:

- A direct 4x4 permutation expansion has 24 summands. Each has at most
  three two-term entries, hence at most 192 raw terms for the arc.
- Adding J and the Taylor variable u gives at most four two-term entries,
  hence at most 384 raw terms for that direct expansion.
- Expected reduced arc supports are 15,18,23 in t-degrees 0,1,2.
  These are predictions, not measured results: 6+9, 6*3, and 5+9*2.
- Adjugates use nine 2x2 minors; the determinant of S has six permutation
  summands. All polynomial degrees in the sixteen coordinates are <=4.
- The implementation additionally stops above 10,000 monomials in any
  dictionary or 1,000,000 monomial-pair products. These are conservative
  algorithmic guards, not authorization to consume a larger job.
- Estimated wall time below 5 seconds and process commitment below
  128 MiB. Hard limits: 60 seconds, 512 MiB, one Python process and one
  BLAS thread, through the existing inspected analysis/b15_bound.py.
  Its timer thread is a deadline guard; the research code uses no threads.

The exact command, after input hashes are pinned, is:

    .\.venv\python.exe -B analysis/b15_bound.py --seconds 60 --memory-mb 512 --name b17_02_boundary_pilot --slot 02 analysis/b17_02_verify.py

At most this one mathematical computation is authorized for this task.
A failure or cap hit is recorded as uncomputed; no retry or larger job
will be launched in this session. The program is also the future
executable verification; a reviewer must obtain its own run authorization.

The next representation calculation is deliberately not priced as cheap:
for a supplied lambda of size 4d it needs an exact basis of
(S_lambda W)^H and its forbidden gamma-weight projections. A naive
tensor carrier has dimension 16^(4d) and is prohibited. A sparse proposal
must report the actual number of invariant columns, stored tensor terms,
forbidden rows and rational bit sizes, then receive integrator review.
No such basis or calculation is assumed available here.
