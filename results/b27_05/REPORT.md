# B27-05 — record check and feasibility closure

**Registered outcome 4. Rung 0's stop rule fires.** The committed record already identifies, implements and tests the determinant-generated image, strictly smaller than the symmetric rectangular Kronecker target in named cells. It also prices out the existing Foulkes enumeration implementation before the requested degree-8 cells. This packet is a **READ-level feasibility result**, not a new mathematical result or a replay of those certificates.

**READ (file, instruction):** B27-05 says: “If the record already answers rung 1, or already prices it out, stop here and report.” Accordingly, no new construction, mathematical run or experiment was launched. The obstruction is the cost of assembling the recorded image map, not a missing definition of that map. This does **not** prove that every possible compressed upper bound is unavailable.

## Provenance and preflight

**READ (file):** The output directory was absent before creation. There is no branch or HEAD requirement for this slot; its explicit overrides forbid Git writes and put delivery in this folder. All Git commands in this session were read-only. The sandbox account required a per-command `safe.directory` setting to read the existing worktree; no persistent Git configuration was changed. No ancestor `AGENTS.md` was found on the path to the output directory.

**READ (file), raw SHA-256:**

| Control file | SHA-256 of the raw file bytes |
|---|---|
| `B27_COMMON.md` | `891e3ca872bc795b6f943ac89f55112573803f006e0208940dd6cad1f750d6ee` |
| `B27-05.md` | `1c2a37885816f19852436ded553fd44e18820458ab2fa91fe21a2a3d712f749e` |
| `BATCH27_BOARD.md` | `b0bc2501aba62d49b91862d821232ac1b9904480057a8dcdb4cbc03fbd86efec` |

**READ:** Every committed citation below is at **`7c36a52ddf338eb390a9bcd491cb9c50cf9e2a19`**, abbreviated **C**. `INPUT_BINDINGS.json` binds the exact raw bytes obtained from `git show C:path`, their byte lengths, and their unmodified local snapshots. Hashes are SHA-256 of blob content, not Git object IDs, decoded strings or normalized files. Reading is scoped to the cited sections/records; retained session-summary snapshots marked UNREAD are not premises.

**READ (file), permitted fallback:** The two files specified by the brief have the expected raw hashes, but their exact raw Git blob objects were not found in the accessed shared object store. The brief explicitly permits file citations in this case. Both files differ from the corresponding committed blobs only by CRLF versus LF line endings; equality after that one conversion was checked. They are not falsely cited as byte-identical committed blobs. Mathematical premises below use the separately bound committed LF blobs.

| Brief source | Raw file SHA-256 / bytes | Committed blob SHA-256 / bytes at C |
|---|---|---|
| `work/batch15/docs/s38_review.md` | `370ba28982137b0c5febb7b0f59c303783a39bb00189cf764004615c8bd26a10` / 5,333 | `6f4662489829e50fef5fb866f5992ed323571586809b55df48f9e3b5b91d78f0` / 5,241 |
| `work/batch27/b27-03/results/occurrence_screen.md` | `a447e99a02e2ee39e819c13238b141acd42048cfa4268d496fac48925a4dbcb0` / 5,624 | `669a89988c23a7679f4c8607525084d4eff718abbd3783d59c48040dcc65865d` / 5,531 |

The exact file paths, hashes and comparison results are in `FILE_FALLBACK_BINDINGS.json`. The raw control files are also retained under `inputs/control__*`.

## Rung 0: what the record already says

### Session 36: a source reduction, not a new determinant-image ceiling

**READ — C:`docs/stabiliser_reduction.md` §§1–3; C:`docs/s36_review.md` §§1–2.** For blocks B of equal parts of lambda, every highest-weight vector lies in the weight-stabiliser character

`chi_lambda(w) = product_B sign(w|B)^(common part on B)`.

The implementation restricts the coefficient weight space to twisted orbit sums, then applies all simple raising operators. It does not replace the determinant restriction map by a Kronecker dimension count. The general isotypic reduction is valid; the old one-operator shortcut does not transfer to arbitrary weights. Session 36's review reports 91 ledger rows with `mult_det = a`. The historical dense frontier was roughly 15,500 reduced columns, with three quadratic arrays inside the nullspace computation. That is a recorded implementation limit, not a universal limit.

### Session 58: the first-row reduction computes the target dimension

**READ — C:`docs/s58_report.md` §§0–1,6; C:`docs/s58_review.md` §§2–3.** Jacobi–Trudi along lambda's first row and Frobenius reciprocity reduce the symmetric rectangular Kronecker count to sums over the tail. The rectangle remains through the exact box condition `beta_1 <= k`. This computes `m_det = sk`, not `mult_det` or the entries of determinant substitution. The report's `274 -> 48,825` LMR example is explicitly a source/target dimension statement with rank still to be determined in that historical report.

**READ — C:`results/occurrence_screen.md`, session-58 correction; C:`docs/s56_review.md` §4.** The old assertion that length-five degree-11/12 character counts are beyond budget is superseded. That correction does not reduce the rank problem. Session 56's review explicitly identifies the unresolved continuation as reducing the rank/Gram kernel, rather than merely its target dimension.

### Balanced degree-8 and degree-9 measurements: Session 60 matters

**READ — C:`docs/s38_review.md` §§1–2.** Session 38 measured 29 degree-8 cells, all with `mult_det = a`, in a peaked corner with `N_S <= 5,531`; it did not measure the large balanced corner. The older producer report contains stale 27/29 counts; the integrator review's 29 is the value used here.

**READ — C:`docs/s54_report.md` §3.** Session 54's degree-8 and degree-9 measurements were also restricted: 12 cells at each degree, with unreduced weight-space size at most 2,500. Its broader prose about degrees beyond nine must not be read as a full-slice exclusion.

**READ — C:`docs/s60_report.md` §§0,2–3,6–7.** A later session did measure the balanced complement: **95 degree-8 and 94 degree-9 informative complement cells** in its reported census sweep. It reports `mult_det = a` at all 419 measured cells across its census and closing sweeps. Thus “balanced degree 8/9 has never been measured” is incorrect. Coverage is partial. Its quoted larger-cell times are minutes to days, not a claim that the whole balanced slice fits this slot's 60-second runs. Its certificate coverage also distinguishes dense certificates from sparse algorithmic nonsingularity records; none was replayed here.

**READ — C:`results/s60_census.json`, degree keys 8 and 9; C:`results/s60_cells.jsonl`; C:`results/occurrence_screen.csv`; C:`results/b14_11/inventory.json`, degree 8, lambda `(12,8,6,4,2)`.** The two largest-`a` cells named by Session 38's occurrence table remain distinct from the measured complement:

| Cell | Recorded a | Recorded m_det | Recorded N_S = n_chi | Recorded rank status in sources checked |
|---|---:|---:|---:|---|
| `(12,8,6,4,2)`, k=8 | 109 | 27,257 | 813,314 | No row in Session 60's raw rank file; later B14-11 inventory has empty `recorded_evidence`, `recorded_full_det=false`, `CANDIDATE` |
| `(14,10,6,4,2)`, k=9 | 437 | 104,544 | 2,085,864 | No row in Session 60's raw rank file; no measured rank found in the cited reports |

These are scoped record findings, not proofs that no other archived artifact can contain a measurement. “Largest balanced cell in the Session-38 table” is taken to mean its largest-`a` representative `(12,8,6,4,2)`, not the different balanced weight `(7,7,6,6,6)`. `RECORD_EXCERPTS.json` retains the selected committed census/inventory rows and concrete measured examples. Its data selection is READ, not a fresh rank calculation.

### Relations, generation and the actual image object

**READ — C:`docs/s56_report.md` §§1–2,4; C:`docs/s56_review.md` §§1–4.** The determinant-generated image is already identified explicitly. With `N=4k`, the recorded map is

`Theta_k^+ : H_(4,k) = Ind_(S_4 wreath S_k)^(S_N) 1 -> Sym^2([k^4])`,

`Theta_k^+(pi) = epsilon_pi tensor epsilon_pi`.

Its image is the polarised degree-k determinant-coefficient algebra. In the **multiplicity currency**, denote the already recorded object by

`W_record_(k,lambda) = Hom_(S_N)([lambda], image Theta_k^+)`.

The recorded identification is

`dim W_record_(k,lambda) = mult_det(lambda,k) <= min(a(lambda,k), m_det(lambda,k))`.

Session 56 supplies an exact Gram realization: `beta = K Hadamard-square K`, with `ker beta = ker Theta_k^+` over characteristic zero. This is a finite computation of the image, not just the name of an unknown quotient. It was implemented and calibrated at all 40 constituents through k=4.

**READ — C:`docs/s56_review.md` §§1–2.** Strictness below `m_det` was already tested: at k=4, `(8,4,2,2)` has image multiplicity 1 and target multiplicity 11; `(6,4,4,2)` has 1 versus 10.

**READ — C:`docs/stabiliser_reduction.md` §4.3; C:`results/occurrence_screen.csv`, k=5, lambda `(4,4,4,4,4)`.** There is also a five-row strict example already in the record: `mult_det = a = 1`, whereas `m_det = 5`. At k=8 the requested tight cell `(24,2,2,2,2)` likewise has recorded `mult_det = a = 1 < 8 = m_det` (C:`results/s54_cells_d8.jsonl`, that cell; occurrence CSV). These drops from target dimension do **not** give equations, because the image still has the full source multiplicity a.

**READ — C:`docs/s62_report.md` §§1–2,6.** The smaller multiplicity Gram was already formulated as `G_lambda = V^T B_lambda V`, an `a x a` rational matrix with `rank_Q G_lambda = mult_det`. The size of this final matrix does not price the computation: its entries require the orbital/support contraction. A deficient modular Gram rank is not a characteristic-zero upper bound; that characteristic caveat is explicit in the source.

**READ — C:`docs/s56_report.md` §4.** The cited multilinear SFT provides the rectangular target and Plücker relations. It does not provide the kernel of the determinant-coefficient subalgebra. Re-labelling target straightening as a presentation of the image would duplicate precisely the error that the record warns against.

**READ — C:`docs/quiver_route.md` §§1,3,6.** The kernel/cokernel distinction is already explicit in the earlier quiver analysis. Its degree-one generation failure and degree-two extra generator are for **3 x 3 matrices and cubics**. They cannot be imported as numerical generation results for the present 4 x 4/quartic problem. No such transfer is made here; the cited external SFT and quiver literature were not independently read in this slot (UNREAD externally).

**READ — C:`docs/s57_report.md` §0 and §1, Proposition S.** The record also gives a localized description through characteristic-polynomial coefficients of traceless pencils, and stability along fixed tails. This changes coordinates for the same image; it is not a proof that the coefficient-generated algebra equals the whole invariant ring.

**READ — C:`docs/b27_03_report.md` §3.** B27-03 reports injectivity in every coefficient degree at most 4, on degree-8 retained weights `(24,2,2,2,2)` and `(23,3,2,2,2)` of dimensions 480 and 1,018, and along its two specified retained weight rays in every degree. The first degree-8 weight also has full rank 619 in the 70-coordinate ring. These are **weight-space** dimensions, not multiplicities 480 or 1,018. B27-03 is producer-level pending its review at C; its certificates were not replayed here. Its §4 says the positive exact upper-bound method is unpriced there. Session 56 shows the abstract exact map already existed; what B27-03 lacked was an affordable realization for this purpose.

## Why the stop rule fires, and what remains open

**READ — C:`docs/s56_report.md` §5; C:`docs/s56_review.md` §3.** The existing enumeration implementation is priced out already at k=5: `|H_(4,5)| = 2,546,168,625`; the producer estimates roughly 24 hours for the cheapest length-five weight pass and roughly 36 days for the rectangle, before the complete inversion over dominant weights. Its k=4 calibration cost roughly 2.1 hours. These are historical method-specific measurements/estimates, not measurements on this host and not a lower bound for all algorithms.

**READ — C:`docs/s62_report.md` §6.** Passing to an `a x a` matrix was already tried as a formulation. The remaining bottleneck is support/orbital assembly, not elimination on that small matrix. **READ — C:`docs/s56_review.md` §4.** The record's open continuation is a rank-preserving contraction that avoids the full Foulkes carrier. Neither Session 36's source symmetry nor Session 58's character count supplies that contraction.

**READ-level decision:** Rung 1's literal requirement—an explicit computable image object bounded above by `m_det`, with strictness somewhere—is already answered by the committed construction and strict examples above. The available implementation is also already costed outside this allowance at the relevant degrees. Rebuilding it or re-running its small no-drop controls would duplicate recorded work. A genuinely new, inexpensive over-space whose dimension can fall **below a** remains a research problem; this record check has not solved or ruled out that problem.

| Rung | Disposition | Achievement level |
|---|---|---|
| 0 — record check | Complete; mandated early stop | READ, feasibility / registered outcome 4 |
| 1 — new W and HAND proof | Not launched; recorded image object and its proof located | No new HAND theorem |
| 2 — new prices for the three requested targets | Not launched after rung-0 stop; historical carrier sizes and method-specific prices reported above | No new price or runtime guarantee |
| 3 — one bounded exact test | Not launched | No COMPUTED result; zero mathematical runs |

No new source condition, coefficient equation, separation on actual padding, or positive multiplicity gap is claimed. No new geometric noncontainment or asymptotic bound is claimed. **The binding constraint stands: “No five-row determinant equation is known to be nonzero on padding.”**

Delivery consists of this report, provenance bindings, selected record excerpts, the resource receipt, unmodified input snapshots and `MANIFEST.json`. There is **no new commit or push**, as B27-05 requires. The integrator owns the eventual commit of this folder.
