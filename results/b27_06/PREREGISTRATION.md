# B27-06 — proposed determinant-rank measurement

**HAND — status and approval unit.** This is registered outcome 2: a priced proposal, not permission to execute. The present slot has performed no target build or rank measurement. A future approval should name either Cell A alone or Cells A and B sequentially, with the limits below. Cell A is the recommended first purchase of machine time. No alternative cell, degree sweep, padding experiment or automatic extension belongs to this proposal.

**READ — frozen targets and premises.** The following dimensions come from commit `7c36a52ddf338eb390a9bcd491cb9c50cf9e2a19` (C), `results/s60_census.json` and `results/occurrence_screen.csv`; their raw bytes are bound in INPUT_BINDINGS.json. The ordinary-coefficient and raising conventions are those of `C:docs/stabiliser_reduction.md` and `C:docs/sparse_det_route.md`. The five parts are distinct, so n_chi=N_S.

| Target | Degree | a | n_chi=N_S | Target room m_det; not measured mult_det |
|---|---:|---:|---:|---:|
| A: (12,8,6,4,2) | 8 | 109 | 813,314 | 27,257 |
| B: (14,10,6,4,2) | 9 | 437 | 2,085,864 | 104,544 |

**READ — record check.** No determinant rank at these exact targets was found in the saved all-local-ref committed-record search; refs were unchanged at the continuation preflight. SEARCH_AUDIT.md states the coverage and exceptions. If a valid prior measurement is located during future preflight, stop before constructing either target and report it.

## Method, budget and expected range

**HAND — selected method.** Use the exact modular blocked triangular-cover/Schur hybrid from Session 71 with the corrections in Session 79. Prepare a determinant-only adaptation of `C:analysis/wk12_s79_cell6.py`, keeping the blocked source engine in `analysis/wk11_s71_hybrid.py` and its verified arithmetic. Remove the other evaluation families and their allocations. Preserve the corrected `nullspace(G)` orientation. The stock driver runs more families and does not export these large kernel bases, so it is not the proposed finished driver.

**READ — calibration basis.** Session 71 gives 72 banked calibration cells and 151 additional closing cells; Session 79 reaches n_chi=732,815. The exact extracted timing rows and fits are in TIMING_DATA.json. The selected method has already been compared with Session 60's different rank algorithm on smaller cells (`C:docs/s71_report.md` §2.3). These are READ historical checks, not fresh target evidence.

**COMPUTED — central scenario prices.** With z=nnz(E)=10n, residual U=a+ceil(f*n), and f=0.10%..0.48%, the published fit plus explicit residual and replay allowances gives:

| Target | Two primes + one independent rebuild/replay | Estimated peak | Earlier worst f=1.30%, same z=10n |
|---|---:|---:|---:|
| A | 0.54–2.24 hours | 4.4–5.6 GB | 6.34 hours; 13.4 GB |
| B | 4.07–15.56 hours | 19.8–28.1 GB | 47.59 hours; 80.1 GB |

**HAND — uncertainty.** These are scenarios, not confidence intervals. Neither target's z nor U has been measured. A crude structural bound is z<=4kn; replacing 10n by 32n/36n can materially increase cost. At f=0.48%, that sensitivity gives **COMPUTED** 7.03/53.36 audit hours and 7.4/33.5 GB; at f=1.30%, 19.08/147.22 hours and 15.2/85.5 GB. An additional host-rate multiplier of 0.5..2 is a planning sensitivity until a provisioned-host calibration replaces it. No completion guarantee is made at the caps.

**HAND — proposed hard reservations.** Use a 64-bit Linux host with one numerical process, one BLAS thread and sequential primes; no GPU or multicore speedup is assumed. The historical CPU model is unspecified. Required libraries/compiler are checked before execution; the pricing slot installs nothing.

| Budget item | Target A | Target B |
|---|---:|---:|
| Provisioned RAM | 32 GB or larger | 128 GB or larger |
| Aggregate job-memory cap | 24,000,000,000 bytes | 96,000,000,000 bytes |
| Total target wall cap, including rebuild/replay and any failed attempt | 24 hours | 72 hours |
| Proposed free local SSD reservation | 64 GB | 128 GB |
| Artifact-size stop | 50 GB | 100 GB |

**HAND — preparation allowance.** Separately allow 1–2 working days of implementation and reviewer effort for the determinant-only driver, independent verifier, deterministic fixtures and resource wrapper. This is an engineering estimate, not measured machine time. Provisioned-host control/calibration runs have a separate aggregate cap of two hours and 8 GB. There is no dollar quote without a selected provider. If preparation or calibration does not fit, report the obstruction before a target launch; do not silently consume target time or change the method.

## Frozen execution protocol after a future approval

1. **HAND — preflight and controls.** Verify frozen input hashes; record CPU, OS, compiler, library versions, BLAS thread settings and free resources. Freeze and hash the adapted producer and verifier before any target build. The verifier must regenerate the source/evaluation matrices from mathematical inputs rather than accept stored ranks. Replay a known small live determinant source and a deliberate corrupted-source/point control. Never assert that the research cell itself must have positive determinant rank.

2. **HAND — calibrate on recorded smaller cells only.** Use `(24,6,5,3,2)_10` from the s71 record to check a distinct-part five-row carrier, and `(13,9,9,3,1,1)_9` from s79 to check the large-carrier blocked path. Run one prime sequentially, determinant only; compare the exact published source dimensions and determinant full rank. Record separate build, cover, Schur, lifting/checking, evaluation, and verifier times. Stop on disagreement or control-budget exhaustion. Use observed rates, including a slower verifier if applicable, to replace the planning coefficients. No extrapolation based on another family's evaluation speed is permitted without stating it.

3. **HAND — build-and-cover gate.** For each approved target, build only the monomial carrier and full sparse integer E; assert its column count equals the frozen n_chi. Save actual row count, z, dtypes, CSR byte count, memory high-water mark and phase times. Select and save a deterministic cover, with actual pivots S and residual U. Reprice the remainder before allocating the dense Schur residual. If the predicted total remaining producer and verifier work exceeds the unused wall budget, or the conservative memory estimate exceeds 75% of the job-memory cap, stop and deliver the sizing receipt. The full job cap remains an OS-enforced backstop. No target rank is inferred from this sizing result.

4. **HAND — modular source gate.** Use primes 2,147,483,647 and 2,147,483,629 sequentially, as in the committed engine. Pin the projection recipe and seed (base seed 20260908), including its per-prime offset, and save the actual projection recipe/hash. Use one projection attempt per prime. Freeze cover ordering and its tie-breaking before launch. Set the X-block budget to 250 MB, account for the engine's minimum 32-column block, and reduce the block size in the adaptation if the proved memory bound requires it. A failed source-rank/nullity gate is an inconclusive run, not evidence of an equation; stop rather than search more seeds.

5. **HAND — exact source verification.** Certify nonzero triangular pivots and the projected residual rank nU-a. Lift a linearly independent a-column basis K and verify E K=0 on every row of the original E. Both rank inequalities must hold: merely obtaining a vectors killed by E is insufficient. Verify every integer/limb arithmetic bound before arithmetic is performed. In particular the recorded exact float64 limb products require inner dimension <2^21, or a further exact block reduction. No numerical rank tolerance is allowed.

6. **HAND — determinant evaluation.** Use a+8 integer five-matrix pencils per prime, bound 40 and seed 11, as in the recorded determinant generator; serialize the actual integer pencils so replay never depends only on PRNG behavior. Use the same fixed pencils across the two primes. Evaluate ordinary determinant coefficients and monomials in batches of at most eight points, contract with K, and compute exact modular rank. Save a nonzero a-square minor if full. Stop the point set at the registered size; a deficiency does not authorize an adaptive random search.

7. **HAND — independent replay.** Before claiming a characteristic-zero conclusion, a verifier separate from the producer driver and C Schur helper must rebuild the relevant E rows, cover, projected residual and determinant evaluations, then check the source-rank gate, all K vectors and the claimed evaluation minor. The verifier may share a declared low-level finite-field library. Freeze its code and successful small-cell comparisons first. The price includes one such whole numerical pass with an independent rebuild; if its calibrated rate differs, use that rate at the build-and-cover gate. Saved producer matrices alone are insufficient geometric provenance.

**HAND — gate formula.** Using n, measured z and U, the baseline phase model in seconds is

`B=2.1e-6*n*k; S=5e-7*z; H=8e-8*z*U; V=2.7e-8*(a+8)*n*k; R=1e-9*(a+8)*n*a; D=5e-10*U^3`.

**HAND — total and memory.** The central two-prime-plus-rebuild/replay total is `2*(B+S)+3*(H+V+R+D)`, adjusted phasewise using host calibration. D is a conservative additional residual allowance, not an independently fitted theorem. The updated memory envelope is `16*n*a + 100*z + 400*n + 5*max(250000000,128*n) + 80*U^2 + 500000000` bytes. It explicitly counts a temporary uint32 kernel copy. Actual allocation accounting and OS limits take priority over this heuristic envelope. FINAL_PRICE_AUDIT.json verifies these formulae exactly.

## Certificate and decision rules

**HAND — full rank.** A certified `rank_Fp E=n-a`, a verified full kernel K, and a nonzero a-minor of the actual determinant evaluation VK give `mult_det=a` over Q. Equivalently, [E;V] has full column rank modulo p. One prime suffices mathematically. The second and the independent replay are implementation controls; disagreement must be investigated and reported, not averaged away.

**HAND — modular deficiency.** If evaluation rank r<a, label it only a modular finite-sample deficiency. With the verified source-lifting gate it supplies the lower bound `mult_det>=r`. Save the modular candidate combinations from `nullspace(VK)` and verify their full E equations and saved point evaluations. Agreement of primes or extra numerical zeros would still not give a characteristic-zero upper bound. Do not write `mult_det=r` as an exact characteristic-zero claim.

**HAND — characteristic-zero drop.** A separate exact certificate must exhibit q != 0 over Q, prove its weight/degree and E q=0, and prove

`q(coefficients of det(s1*A1+...+s5*A5)) identically equals 0`

in all 80 independent pencil entries. Complete exact coefficient cancellation, a proved interpolation bound with exhaustive exact checks, or a correctly identified faithful Theta/positive-semidefinite rational Gram kernel is acceptable. Rational reconstruction without these checks is not. One such q proves a drop; d independent q plus a certified rank floor a-d proves exact multiplicity a-d.

**HAND — drop-proof budget boundary.** The target-scale global identity calculation has no established affordable implementation/timing in the retrieved record. It is **not** included as a promised completion within 24/72 hours. A deficiency exits this approved measurement proposal with saved candidates and a separately priced identity-verification request. This is an explicit limit of the preregistration, not promotion of a modular result into a theorem.

**HAND — all exits are reportable.** Deliver one of: certified full rank; modular deficiency with stated lower bound and unproved candidate; source/control failure; resource stop; or discovered existing measurement. No projection retries, other primes, extra point batches, fallback Wiedemann jobs or global identity run are automatically authorized. If only A was approved, B remains unrun regardless of A's outcome.

**HAND — evidence delivery.** Save exact source conventions and indexing, frozen commit and code hashes, all resource receipts (including failures), cover and projection data, both modular bases in binary uint32 form, actual integer pencils, evaluated minor entries and pivot data, and independent replay results. Use chunked binary data rather than JSON dumps of dense kernels. Bind every payload by raw SHA-256 and bytes; retain a standalone verifier and commands. No shared ledger or publication is part of the measurement proposal.

**READ — prior, not a probabilistic model.** Session 60 reports 419/419 measured cells with full determinant multiplicity. Later hybrid work also supplies full-rank observations. This record is calibration context, not a probability estimate for the unmeasured balanced corner.

**HAND — achievement boundary.** Full rank adds a no-equation cell. A certified drop establishes existence of an equation only; it does not show padding separation or a positive multiplicity gap. **READ:** “No five-row determinant equation is known to be nonzero on padding.”
