**B14-03 integrator review — September 12, 2026**

**Assessment: successful delivery of the scoped proof and verification instrument.** I found no mathematical defect in its complete-interpolation argument or its implemented small-cell acceptance checks. I imported the delivered bundle into a separate review worktree, read the proof, producer, checker and dispatcher changes, and reran the full bounded replay. The five stages passed, including all 97 control cases. This is a useful foundation for certifying the combined B14-01/02 result; the delivered checker does not yet implement that larger case.

The original worker checkout, integration branch and delivered files were left unchanged. Review execution used `work/reviews/b14-03`, detached at `d1ef799ddd96ef119584844c6a6d5188117eac0c`.

**What it contributes in plain terms**

Ordinarily, an expression being zero at all tested points leaves a possibility that it becomes nonzero somewhere else. Complete interpolation removes that possibility by first proving that these points detect every possible expression in a specified finite-dimensional space. Once that coverage is established, an exact zero in the evaluation matrix is a genuine equation everywhere on the parameterized variety.

B14-03 spells out the proof obligations and implements a checker that reconstructs the relevant mathematical objects. It checks source polynomials and their completeness, target membership and dimension, point definitions, actual evaluations, sufficient integer-reconstruction bounds, and the correct source relations. It rejects unsupported inputs instead of accepting a bare matrix as a proof about polynomials.

Its demonstrated target has dimension **1**, in the separate ternary quartic degree-6 control of weight `(8,8,8)`. That number does not refer to the previously missing direction in our 73-dimensional degree-13 target.

| Deliverable | Review assessment |
|---|---|
| General complete-interpolation lemma | Correct, including the dimension-upper-bound formulation |
| Independent checker integrated with the ordinary repository command | Working for the registered small profile |
| Complete source and target certificates on the small control | Recomputed successfully |
| Wrong-input and corruption rejection suite | 97/97 cases pass: 2 accepted, 95 rejected |
| Separate full coefficient identity | All 1,720 retained coefficients agree |
| Degree-13/14 production checker | Not implemented; larger profiles explicitly rejected |
| New LMR equation or value of D from this session alone | None claimed or established |

The small control's equation was already known from B13-03. The contribution is the independent certification route and its integration, rather than discovery of that equation.

**Why the proof is sound**

Let the complete source be M, let phi be the specified polynomial restriction map, and prove phi(M) is contained in N. Suppose dim N is at most h. If h genuine members of N have a nonzero h-by-h evaluation minor, they are independent, so dim N is exactly h and evaluation is injective on N. Consequently the kernel of evaluated restriction equals the kernel of polynomial restriction.

With source vectors as rows, the evaluation matrix A has a rows and m point columns. A source relation is a column of K, and the required identity is **A^T K = 0**. B14-03 checks that identity over Q and verifies both the rank of K and its completeness as the kernel. Its corruption suite deliberately supplies an actual relation between point columns and confirms that this cannot pass as a source relation.

The implementation uses a valid characteristic-zero dimension sandwich. For the source it constructs all 561 weight monomials and the 1,056-row raising matrix. Modular rank 559 proves nullity at most 2; two independent exact highest-weight polynomials prove nullity at least 2. For the target, Pieri gives exactly one cubic predecessor, `(8,8,2)`. Its 54-by-38 raising matrix has modular rank 37, giving target dimension at most 1. The nonzero mixed bracket proves the reverse bound. No modular rank deficiency is promoted into an exact equation by itself.

The ordinary coefficient substitution is correctly stated as

    c_alpha(ell*c) = sum_i ell_i d_(alpha-e_i).

There is no alpha_i multiplier in these ordinary coordinates. The factorial-symbol convention used elsewhere gives a different-looking formula, with alpha_i, after changing coordinates. These statements are compatible. The checker explicitly handles the factorial weights in the mixed bracket map and separately verifies all raising residuals.

Rational rescaling is also handled correctly: it clears row denominators, checks their compatibility with the primes, derives a value-height bound from the actual polynomials and points, and requires a CRT modulus greater than twice that bound. Kernel coordinates are interpreted in the rational source basis, rather than silently in the cleared integer basis.

**Fresh verification evidence**

The bounded replay took **22.14 seconds**, with a maximum recorded working set of **44.39 MiB**. All stages enforced the delivered 768 MiB process cap and one-worker limit.

- Producer: regenerated the control successfully.
- Controls: 97/97, including 71 separate required-key deletions. Duplicate-JSON-key rejection also passed.
- Independent checker: source dimension 2, target dimension 1, exact restriction rank 1, exact reducible ideal multiplicity 1.
- Repository dispatcher: integer, rational and compressed positive certificates all passed.
- Dispatcher negatives: the altered integer entry failed; missing points, duplicate keys and a nonexistent file were unparseable. The process returned the required nonzero exit.
- The separate universal-pullback oracle confirmed the zero source image and the identity `G = 288 phi(F1)` on all 1,720 coefficients.
- The delivery gate is CLEAN for 56 changed files. All delivery checksum entries and all 75 manifest file records match; whole bundle and part00 are byte-identical. The delivered standalone checker matches the bundled checker.

The integer control evaluates to

    A = [[729, 3969], [729, 3969]],
    K = [[1], [-1]],
    T = [[209952, 1143072]].

The nonzero target entry 209952 certifies complete interpolation in the one-dimensional target. Both source rows are nonzero, so the test exercises cancellation between sources. The rational control changes the sources to `(F0+F1)/2, F1/3` and correctly returns relation coefficients `(2,-3)`.

**Limits and integration findings**

The implemented profile is deliberately specialized: three variables, quartic degree 6, two source vectors, one target member and at most 16 points. It expands the small mixed bracket polynomial explicitly. Changing a dimension field or profile name cannot turn this into a degree-13 verifier. This matches the session's preregistered scope and fallback, but matters when assessing readiness for LMR.

The legacy numerical imports were moved into the branches that need them. I inspected those routing changes; the old numerical backends themselves were not changed. I have not replayed the full legacy certificate corpus, because this runtime lacks its flint/scipy dependencies. The fresh PASS results apply to the new interpolation path and its dispatcher controls.

A small implementation follow-up: the normal dispatcher first parses a file with its legacy loader, then reloads CI certificates through the bounded CI loader. Thus the CI loader's five-megabyte limit is not an early parsing limit at the dispatcher entrance. The standalone checker applies its limit before parsing, and the delivered replay has an external process-memory cap. This does not affect the mathematical verdicts. A production integration should avoid the initial unbounded/double parse if it promises that limit at every entry point.

The original report's LMR interval `[-4,+1]` records its frozen-base knowledge. It must not overwrite the later joint B14-01/02 deduction when updating the current research ledger.

**How it applies to our combined degree-13 result**

Our preceding review completed B14-01's 72 mixed target members with the genuine target polynomial

    G_73(ell,c) = F_15(ell*c),

where 15 is the zero-based native degree-13 source index. The completed target has nonzero 73-minors at both house primes. Membership of this extra function follows from equivariant restriction, independently of whether any candidate equation is a kernel vector. It therefore satisfies B14-03's general theorem: a target member need not be a single mixed bracket.

Combined with the independently recounted target dimension 73, the exact 39-by-96 source matrix of rank 36, and its three independent exact kernel columns, this yields **i_red(13)=3**. Multiplication by the specified highest-weight polynomial transports those three equations injectively to the degree-24 LMR cell. With the banked padded rank floor and exact determinant multiplicity, the current combined conclusion is

    3 <= i_pad(24) <= 5,
    D_LMR = 1 - i_pad(24) in [-4,-2].

This excludes a positive multiplicity obstruction at that cell. The exact value `D=-4` remains open. B14-03 corroborates the mathematical mechanism; it has not itself replayed or registered this larger certificate. The preceding joint review documents which evaluation values were freshly regenerated and which were checked using delivered residues, inspected evaluators and banked certificates.

**Concrete continuation**

Extend the checker with a separately registered degree-13 profile and the following obligations:

1. Accept both mixed-bracket target definitions and a pullback of a verified quartic source vector. This accommodates the completing member without expanding its 4^13 slot choices.
2. Independently check the dimension-73 certificate, all 39 source definitions and source independence, and the complete point/coordinate contract. Explicitly transport the two native degree-12 rows to degree 13.
3. Verify the completed 73-minor, the exact source matrix and its seven-prime uniqueness bounds, rank 36, and all identities in A^T K=0. Retain bounded independent evaluation checks; stored matrices alone are insufficient.
4. Add degree-13-specific rejection cases: duplicate completing member, wrong source index, altered point, wrong transport exponent or factorial scale, insufficient CRT modulus and an altered kernel coefficient.
5. Register the three equations and their degree-24 transport in the current ledger only with accurate replay provenance. Keep the two additional sampled relations open.

For degree 14, the independently counted target dimension is 159. Its own complete interpolation and source-kernel certificates are still needed to turn all five sampled relations into exact equations and settle `D=-4`. The degree-13 adapter should provide reusable components for that work.

**Local evidence:** `review_checks.json`, `control_results.json`, `verification.json`, `replay_results.json`, `dispatcher_report.md`, `dispatcher_rejections.md`, and `delivery_check.txt` in this review directory. `collect_review.py` checks delivery identities and collects the fresh replay outputs; the mathematical replay itself is the delivered `analysis/b14_03_replay.py` in the detached review checkout. The preceding combined deduction is recorded in `../B14-02_review/REVIEW.md`.
