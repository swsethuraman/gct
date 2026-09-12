**B14-03 continuation: complete and independently verify the degree-13 interpolation certificate**

Continue your completed B14-03 work. The integrator replayed your delivery: all 97 controls passed, the mathematical lemma checked out, and the bundle passed the delivery gate. Now implement the degree-13 profile and deliver a portable certificate accepted by the repository's normal verifier.

The target completion is already known. Your task is to certify it end to end, including the polynomial meanings of its entries. Treat the expected numbers below as falsifiable checks, not acceptance criteria that override contrary evidence. Work autonomously through implementation, bounded computation, verification and packaging. This is a degree-13 completion assignment; degree 14 is a later task.

**The result to verify**

Use the existing positive coefficient-weight convention, n=4, r=9, delta=13, lambda=(21,17,2,2,2,2,2,2,2). Let M13 be the complete quartic highest-weight source and let phi(F)(ell,c)=F(ell*c). Its target is

    N13 = HW_lambda(Sym^13 V tensor Sym^13(Sym^3 V)),
    dim M13 = 39, dim N13 = 73.

B14-01 supplied 72 mixed target members on 96 primary P13 points. The integrator found that the extra member

    G73(ell,c) = F15_native(ell*c)

completes the target. Here **15 is the zero-based source index: the sixteenth entry of results/s74/source.json**. It is native degree 13 and needs no transport. This polynomial is a genuine target member by equivariance, bidegree and highest weight. A target member need not be one individual mixed bracket. Its membership does not depend on any candidate kernel relation, so using it is not circular.

The saved completed 73-minors have residues 1832982837 at p=2147483647 and 1811606566 at p=2147483629, with the specific row/column order recorded in the joint certificate. Different valid minor choices can have different determinants; preserve and verify their indices explicitly.

B14-02 supplied an exact integer source matrix A of shape 39-by-96, rank 36, and a 39-by-3 matrix K with rank 3 and A^T K=0. Complete interpolation should therefore certify i_red(13)=3. Transporting these three equations to degree 24 should give i_pad(24)>=3 and, with the banked padded floor and determinant result, D_LMR in [-4,-2]. Do not conclude D=-4: the other two sampled relations remain open.

**Read these inputs first**

All paths below are on the shared local machine. Use other sessions' directories as read-only inputs, and record the hashes of the exact files you consume.

- Your integrator review: `C:/Users/swami/Projects/gct-gpt/Batch14_Results/B14-03_review/REVIEW.md`.
- Combined proof, qualification of the previous replay, and source search diagnosis: `C:/Users/swami/Projects/gct-gpt/Batch14_Results/B14-02_review/REVIEW.md`.
- In that B14-02_review directory: `joint_certificate.json`, `completed_target_matrices.json`, `exact_relations.json`, `joint_verify.py`, `source_basis_replay.json`, `completing_member_fresh_entry.json`.
- Earlier review helper and dimension receipt: `C:/Users/swami/Projects/gct-gpt/Batch14_Results/B14-01_review/review_checks.py` and `dimension_replay.json`.

The joint review scripts establish useful arithmetic checks but do **not** freshly regenerate every delivered evaluation. They are integration aids, not a substitute for your independent acceptance path. Their `joint_complete_interpolation_review` record is not already a registered repository certificate kind.

Pinned repositories and primary inputs:

| Input | Local checkout and identity | Files to inspect |
|---|---|---|
| Your completed B14-03 | `C:/Users/swami/Projects/gct-gpt/work/batch14/B14-03`, head `d1ef799ddd96ef119584844c6a6d5188117eac0c` | `tools/verify/complete_interpolation.py`, `tools/verify/verify.py`, `docs/b14_03_complete_interpolation.md`, existing controls |
| B14-01 | `C:/Users/swami/Projects/gct-gpt/work/reviews/b14-01`, head `cf68004cf2bd31831117c77cea6ac6621f4b8c22` | `results/b14_01/certificate_d13.json`, its member definitions, mixed evaluator and controls |
| B14-02 | `C:/Users/swami/Projects/gct-gpt/work/reviews/b14-02`, head `f0e626263ef48e60e39e162daf418616162c3e2e` | `results/b14_02/A13_primary.json`, `kernel_primary.json`, all seven primary residue blocks, source evaluator, independent exact evaluator, controls |
| B14-04 dimension proof | `C:/Users/swami/Projects/gct-gpt/work/batch14/B14-04`, head beginning `27be12c0` | `analysis/b14_04/verify.py`, `results/b14_04/hpad13.json`, `hpad13_power.json.gz` |
| B14-05 membership/transport proof | `C:/Users/swami/Projects/gct-gpt/work/batch14/B14-05`, head beginning `54584452` | `docs/b14_05_transport.md` |

Resolve the abbreviated B14-04/05 heads to full commit identities and record them. Shared frozen inputs are `results/s74/source.json` and `results/b14_prep/points/P13.json`; base is `9898e56941a7665f231873481dae956f08509995`. Source and point definitions must agree across deliveries. Snapshot selected dependencies into the continuation's deliverable with provenance; a receiver must not need the integrator's absolute-path layout.

Create a named continuation branch and a separate worktree from your completed B14-03 head, preserving the original completed delivery. A suitable location is `C:/Users/swami/Projects/gct-gpt/work/batch14/B14-03-ci73`. Commit the continuation and produce a named-ref bundle. This assignment authorizes local implementation and packaging, not integration merges or remote publication.

**Implementation and proof obligations**

1. **Add a separately registered profile.** Retain your small profile. The larger profile must represent mixed-bracket members and verified quartic-source pullbacks, with explicit normalization, source identities, transport, points and matrix orientation. Reject unknown profiles and missing proof inputs. Avoid expanding the completing member into 4^13 slot choices or expanding the full large carrier. Use a justified contraction/DP representation.

2. **Verify the target dimension independently of evaluation ranks.** Replay B14-04's exact power-sum/character calculation, including complete Pieri predecessor enumeration and all 15 channel multiplicities. Verify the power expansion rather than trusting a stored total or a PASS receipt. Recover 73 without invoking sampled source rank. Bring the required verification logic into a reusable verifier component; the acceptance path must not import a producer from analysis/ or a local integrator helper by absolute path.

3. **Verify source membership and independence.** Check all 39 highest-weight definitions and their common rational/integer convention. Two rows are native degree 12 and 37 are native degree 13. Construct degree-13 rows from `native`, using u^(13-native_degree), where u=24*[x1^4]f. The source file's `literal` field describes degree 24 and is wrong for this computation. Recheck a valid source-independence witness against the specified polynomials, and include a checked ambient dimension-39 dependency before asserting the exact ideal multiplicity. A banked rank table or generic full rank by itself does not establish every convention or source-membership premise.

4. **Verify points and target completeness.** P13 contains 116 points: use the 96 labelled primary points for the delivered matrix, retaining the 20 holdouts as controls. Reconstruct ell*c, ordinary coefficients, factorial symbols, point IDs and their order. Check membership of every selected target member. Recompute the polynomial values needed for a full 73-minor, including the completing pullback, and verify its nonzero determinant. One valid prime minor proves a characteristic-zero rank floor in the stated integral model; agreement at a second prime is useful corroboration. Do not turn a sampled deficiency into a rational upper bound.

5. **Verify exact source arithmetic and relations.** The delivered seven primes are 2147483647, 2147483629, 2147483587, 2147483579, 2147483563, 2147483549 and 2147483543. Check primality, distinctness, denominator compatibility, actual residue evaluations and signed reconstruction. Re-derive H=(9!)^2*2^15*1176^13 from the actual climbed fillings and point bounds; verify each filling really has the stated column counts. The modulus must exceed 2H. Verify rank(A)=36 using a valid minor plus the exact rank-three kernel, and verify A^T K=0 over Q. Describe K as integer representatives of a rational kernel basis; do not claim a saturated Z-lattice basis without proving it.

6. **Minimize work without weakening the proof.** You may select a common 73-point subset supporting a full target minor, and verify the exact source relations on that subset: complete interpolation on those points suffices. Check source rank and every required polynomial value for that chosen witness. There is no need to regenerate unused columns or compute enormous exact target determinants when a modular nonzero minor suffices. State exactly which witnesses the full acceptance path verifies. Either replay all residues needed for signed CRT, evaluate the required entries exactly, or provide an equivalently complete checked arithmetic witness. Checksums, residue consistency with a stored matrix, and random spot checks alone cannot certify that the stored entries are polynomial evaluations.

7. **Conclude and export the equations.** When all premises pass, export Q_j=sum_i K[i,j] F_i^up13 for j=1,2,3, with every coefficient and source definition. Verify the relation between these definitions and their degree-24 transport u^11 Q_j. In the literal degree-24 S74 basis, the coefficients are K on the first 39 rows and zero on the remaining 235. Cite the checked inherited a24=274, determinant rank 273 and padded rank>=269 dependencies separately from the new degree-13 computation. The derived claim is 3<=i_pad(24)<=5 and -4<=D<=-2, not exact i_pad(24)=5.

**Verification quality and controls**

Preserve all original 97 controls and the normal-dispatcher tests. Add degree-13 controls that can actually fail:

- Replace the completing member with a duplicate and require the full-target-rank gate to fail.
- Change a source identifier or polynomial while retaining incompatible stored evaluations; detect the mismatch. A consistent change to a different valid member is not inherently an error.
- Alter a point or reorder a point list without updating its matrix, and reject it.
- Use degree-24 `literal` data, a wrong transport exponent, or a wrong factorial scale in the degree-13 contract, and reject it.
- Alter one integer entry, residue, kernel coefficient, or rank witness; reject the affected mathematical claim.
- Supply an insufficient CRT modulus, an unsupported dimension proof, or a missing dependency; do not return PASS.
- Test a consistent invertible source rescaling and obtain the same ideal dimension with correctly transformed kernel coordinates.

The independent evaluator should have a justified algorithm and comparisons against literal small cases or the separate exact evaluator. Do not create apparent independence by calling the same producer through a renamed wrapper. Distinguish fresh polynomial evaluation, verified certificate dependencies, and arithmetic replay in the report. A faster cached-arithmetic mode may be useful, but must not present itself as full polynomial verification.

Address the review's dispatcher detail while integrating: the legacy loader currently parses CI files before the bounded CI loader. Apply appropriate compressed/expanded-size and duplicate-key checks before unbounded parsing, with limits suitable for the new profile or bounded referenced artifacts. Avoid claiming legacy regression coverage that was not actually run.

**Execution and completion**

Check the available compiler/runtime and free memory before choosing an evaluator. On the reviewed Windows runtime Python/NumPy were available, but flint and gcc were not; do not assume Linux binaries are usable here. You may implement or build a suitable local backend, retaining small exact reference controls and clear build instructions. Use at most two evaluation workers and an aggregate 4 GiB memory budget unless the existing launch constraints are stricter. Measure a representative batch, then set explicit time/memory limits and resumable chunk sizes; record toolchain, PIDs, resource use and process exits. Adjust algorithms if pricing is poor rather than starting a large uncontrolled expansion.

Completion means that a clean receiver can build any required backend and run the repository's standard verifier to obtain a properly scoped PASS for the degree-13 certificate, including all proof dependencies needed for the exact equation claim. Deliver the explicit three equations, the transport proof and the accurately qualified LMR consequence. A general schema, a rank-only replay, or another partial target search is not completion.

If a premise or value disagrees, produce the smallest reproducible discrepancy and correct the result; never force the expected answer. If a computation hits its declared limit, retain all valid intermediate work, identify the exact unresolved gate, and label it incomplete instead of certifying it. Do not divert into degree 14 before this certificate is complete.

Deliver a concise report, standalone replay instructions, producer/independent-verifier code, portable input and certificate manifests, positive and rejection results, resource logs, and a verified named-ref Git bundle with checksum sidecars. Run the delivery gate against the captured base. Append only discharged statements to the continuation's PROVED ledger, explicitly superseding the frozen historical interval with the newly verified scoped result and citing its dependencies. Stop after packaging the completed degree-13 result for integrator review.
