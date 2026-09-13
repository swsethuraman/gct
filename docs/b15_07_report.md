# B15-07: a defined non-Cartan polynomial product map

EXACT: the assignment's operator gates pass. For ternary quartics, the
canonical map P_(6,4,2) composed with multiplication sends
S_(6,2,0) tensor S_(4,0,0) onto S_(6,4,2). Its representation image has
dimension 27 and highest-weight image multiplicity one. Equivariance,
presentation independence, normalization and preservation of homogeneous
GL-stable ideals are proved in `docs/b15_07_proved.md` and checked on
complete small coefficient matrices. No positive multiplicity gap is claimed.

Actual model for preregistration, proof, implementation, verification and
delivery: gpt-6-astra, xhigh, as configured by the native dispatch. There
was no live Claude phase and no extra agent/task. Historical inputs retain
their existing authorship; B13/B14 reports are not rewritten.

## Checked findings

| Check | Fresh exact result |
|---|---|
| Full polynomial operator | Multiplication followed by a normalized spectral polynomial in C=sum E_ij E_ji |
| First source | n=4, coefficient degree 2, three ambient variables, 15 coefficient variables, weight (6,2,0), module dimension 60 |
| First output | Degree 3, weight (6,4,2), ambient multiplicity a=1, module and image dimension 27 |
| Complete degree-three carrier | 680 monomials; largest weight block 23; 2,580 root intertwining columns |
| Exact nonzero value | P(q62*c_022)=G/50; value 1733/25 at c=(1,...,15) |
| Normalized Pieri tensor | One HW tensor in a 22-dimensional tensor-weight space; image 4G/9 |
| Equivalent fillings | Equal polynomial presentations have equal nonzero projected images |
| Exact source relation | Nonzero Plucker terms satisfy the relation before and after projection |
| Repeated ambient component | Degree 4, weight (10,4,2), a=2; both copies and their basis mixtures retained |
| Repeated tensor channel | S_(6,2) tensor S_(6,2): three HW tensors, product rank two, kernel dimension one |
| Stable ideal control | Exact pullback to fourth powers vanishes for all 60 source vectors and 680 projected monomials |
| Hypothesis counterexample | The nonstable ideal (c_400) is not preserved; degree-two rational counterexample retained |
| Spectral qualification | (8,2,2) and (6,6) collide at Casimir eigenvalue 84; single-component selection rejected |
| Independent verifier | Rebuilt polynomial arithmetic in a different monomial representation; all checks pass and all four altered-artifact controls reject |

The producer also rejects six intentional coefficient, relation-sign,
normalization, point and spectral defects. Its separate source/evaluator
liveness control does not depend on the research image rank. The banked
B14-05 binary control is freshly regenerated, including its exact raw
adjunction failure. The historical large n3 coordinate transport remains
RECORDED; no new large filling expansion is claimed.

The small coefficient matrices are not determinant/padded evaluation
matrices. We compute no geometric i, m or h_pad. In particular, dimension
27 above is not ambient multiplicity 27. Images of known equations remain
subspaces of the relevant ideal; they are not identified with its entirety.

## Next sufficient witness and cost

The selected B13-06 channel is nu=(68,17,3,2^6), degree 25, from
lambda=(65,17,2^7), degree 24, times S_4. The scoped ledger gives no
exclusion and the accepted transport overlay marks it OPEN. The four
already closed named products and the original LMR cell are not reopened.

For a rational source HW polynomial F, the normalized formula is

    T(F)=F*c_301 -(E32 F)*c_310/15 -(E31 F)*c_400/16
                                      +(E21 E32 F)*c_400/240.

Its raising identities are proved symbolically. With a complete source
circuit, five simultaneous derivative values per node suffice: at most
11 multiplications and 6 additions per circuit multiplication node, plus
5 additions per circuit addition node. Reduction concerns one HW column.
Evaluation at s points repeats that bounded circuit s times. Bit costs
depend on rational source and point heights; no measured production time
is available. Exact full-carrier and module counts are retained solely to
reject allocating those carriers, not to substitute for signed Burnside
counts. No carrier of the degree-25 problem was built.

The next sufficient missing witness is a complete rational LMR source
circuit with its global determinant-equation provenance, plus an exact
nonzero value of T(F). That would give one product equation. A positive
gap would additionally need padded rank a (or stronger separated bounds),
using true independent padding z*per3. No claim follows from testing only
three known padded equations. The original LMR D interval [-4,-2] and
the accepted degree-13 completeness statement remain inherited premises.

## Resources, provenance and replay

The assigned existing branch/worktree was retained. The frozen commit,
tree and annotated tag object matched the dispatch. Preregistration was
the first commit, ebd6e6d8, containing only results/PREREG_b15_07.md.
No heavy lease was held, requested or needed; the lease record assigned
slots 01 and 02. All jobs here are small controls with one process, one
BLAS thread and the tested aggregate Windows Job Object bound. No sandbox,
ownership, trust configuration or shared record was changed.

| Final run | Wall seconds | Aggregate peak committed bytes | Return code |
|---|---:|---:|---:|
| exact_controls_final | 0.331 | 28,004,352 | 0 |
| independent_verify_final | 0.304 | 21,848,064 | 0 |
| next_sizing_v1 | 0.738 | 71,061,504 | 0 |

The first two caps were 60 seconds/512 MiB; sizing used 30 seconds/512 MiB.
All earlier bounded iterations also passed. v1 covered the first operator;
v2 added the explicit stable-ideal and normalized-tensor controls; v3 added
the repeated LR channel; the final run added a nonzero projected relation
and direct equivalent-filling image check. Their individual logs, PID and
aggregate resource records are preserved. No resource stop or production
extension occurred. `results/b15_07/run_summary.json` inventories every run.

The exact local Python is
`C:/Users/swami/Projects/gct-gpt/work/batch15_workers/B15-07/.venv/python.exe`.
Use that executable in the assigned checkout for each replay:

```powershell
& 'C:/Users/swami/Projects/gct-gpt/work/batch15_workers/B15-07/.venv/python.exe' analysis/b15_bound.py --slot 07 --name b15_07_receiver_controls --seconds 60 --memory-mb 512 analysis/b15_07_projected.py
& 'C:/Users/swami/Projects/gct-gpt/work/batch15_workers/B15-07/.venv/python.exe' analysis/b15_bound.py --slot 07 --name b15_07_receiver_verify --seconds 60 --memory-mb 512 analysis/b15_07_verify.py
& 'C:/Users/swami/Projects/gct-gpt/work/batch15_workers/B15-07/.venv/python.exe' analysis/b15_bound.py --slot 07 --name b15_07_receiver_sizing --seconds 30 --memory-mb 512 analysis/b15_07_next.py
```

The programs use Python, NumPy, python-flint and SymPy already confirmed
in the worker runtime; versions and exact/normalized input SHA-256 hashes
are in input_manifest.json. Ordinary coefficient conventions, explicit
points, source lowering words and complete small matrices are retained.
Every new artifact is below 5,000,000 bytes. The preregistered .venv
executable is used throughout; no PATH Python is assumed.

The pre-existing native runtime/smoke logs are preserved as setup
provenance and excluded from research commits. `proposed_exclusions.json`
is empty. Delivery goes to `delivery/b15_07_final`; the external manifest
records final head/tree, the single frozen prerequisite and checksums
after the last commit. Packaging PASS concerns the delivery contract;
the mathematical evidence is the proof and exact verifiers above.
