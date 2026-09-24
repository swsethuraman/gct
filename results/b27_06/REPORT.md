# B27-06 — priced determinant-rank preregistration

**READ — continuation history.** The first segment stopped after detecting a wall-clock ceiling overrun. The user explicitly authorized continuation; the resumed segment began at 2026-09-23 10:51:42 UTC with a new 45-minute checkpoint and 90-minute ceiling, while retaining the original ten-run arithmetic allowance. All 112 previously sealed payloads, the control hashes and committed inputs verified; Git refs were unchanged. The original stop report, pricing draft, receipt and manifest are preserved byte-for-byte in `interrupted_delivery/`. The suspected connection drop is unverified. This completed report supersedes the stopped draft; it still does not authorize a target measurement.

**HAND — registered outcome 2.** The cheapest credible recorded method is the blocked triangular-cover/Schur-complement hybrid of Session 71, with Session 79's memory and kernel-extraction fixes. Propose the degree-8 cell first on a 32 GB machine with a 24-hour limit, then the degree-9 cell on a 128 GB machine with a 72-hour limit. These are proposed ceilings, not authorizations or promises of completion. [PREREGISTRATION.md](PREREGISTRATION.md) gives the standalone approval unit, conditional prices, certificate requirements and resource stops.

**READ — rung 0.** No rank measurement at either exact cell was found in the locally available committed record, including Session 60's closing sweeps, post-62 work, and later branch histories. Counts, source dimensions, a queue's ordinal `rank`, and skipped jobs are not rank measurements. Search evidence is in [RECORD_SEARCH_SUMMARY.json](RECORD_SEARCH_SUMMARY.json), [RECORD_SEARCH_MATCHES.json](RECORD_SEARCH_MATCHES.json), [BINARY_REVIEW.json](BINARY_REVIEW.json), and [ARCHIVE_EXCEPTIONS.json](ARCHIVE_EXCEPTIONS.json). The damaged archive's explicit cell is (15,7,4,1,1), degree 7, unrelated to either target; only its available prefix was searchable.

**READ + HAND — rung 1.** The audited method and certificate inventory below includes the required methods, later hybrid implementations, and the limits of specialized alternatives. Modular full rank certifies characteristic-zero full rank. A modular deficiency does **not** certify a characteristic-zero drop. A drop needs an exact rational highest-weight vector whose determinant pullback vanishes identically, or an equivalent exact faithful-map/Gram certificate.

**COMPUTED + HAND — rung 2.** Conditional prices are supplied for both cells, with recorded timing fits, memory models, uncertainty and stop rules. No target matrix was constructed, and no target or smaller-cell rank run was made. The allowance use was exact arithmetic on recorded sizes and timing formulae: one failed parsing attempt, one successful pricing run, and one bounded verification/correction run. The latter passed 32 exact formula checks and recorded a 20.5 MB peak working set. Source timings remain READ, not freshly replayed timings. FINAL_PRICE_AUDIT.json supersedes the two explicitly corrected hybrid fields of PRICE_CALCULATIONS.json; original run outputs remain unchanged.

**READ — standing constraint.** “No five-row determinant equation is known to be nonzero on padding.”

## Provenance and dimensions

**READ — citation convention.** `C` means commit `7c36a52ddf338eb390a9bcd491cb9c50cf9e2a19` in the read-only repository `work/batch15`. Every cited `C:path` has a raw-byte snapshot and a full commit/path/blob-ID/SHA-256/byte binding in [INPUT_BINDINGS.json](INPUT_BINDINGS.json). Those SHA-256 values hash raw `git show` content, without newline conversion. The final manifest separately hashes the delivered files. Later inputs are explicitly identified by commit below. Control files are administrative instructions, not mathematical premises.

**READ — preflight.** The output folder was absent before creation. This is the fresh B27-06 session in default permission mode. The slot's no-Git-write, output-folder, preflight and manifest-delivery overrides govern. The three control hashes were checked again unchanged; all 39 payloads of B27-05's manifest `325c1c817bce32e0f11fbd587bee16ea14ae3111c2ee56129fa7028571558a5c` verified. Its report served as a locator only. See [PREFLIGHT.json](PREFLIGHT.json) and [B27_05_VERIFICATION.json](B27_05_VERIFICATION.json). No commit or push was made.

**READ — target data:** `C:results/occurrence_screen.csv`, `C:docs/session_38.md`, and exact rows in `C:results/s60_census.json`.

| Cell | Degree k | Ambient HWV dimension a | Recorded target multiplicity m_det | N_S = n_chi |
|---|---:|---:|---:|---:|
| (12,8,6,4,2) | 8 | 109 | 27,257 | 813,314 |
| (14,10,6,4,2) | 9 | 437 | 104,544 | 2,085,864 |

**HAND — interpretation.** Here the brief's `m_det` is target representation room, not the unknown coordinate-ring multiplicity `mult_det`. Having room greater than a proves no rank. Both partitions have distinct parts, so the Weyl stabilizer is trivial: the signed stabilizer reduction gives no column reduction at these cells. The full weight count really is the raising-matrix column count. This follows from the construction in `C:docs/stabiliser_reduction.md`; it is also explicitly recorded in the census.

## Rung 0: what the target records actually say

**READ — direct evidence.** `C:results/s54_cells_d8.jsonl:292` and `s54_cells_d9.jsonl:431` say `skipped: over_maxnb`. Session 60's census supplies dimensions; its actual census and closing rank files contain neither target. Session 58's calibration rows 820 and 1504 compute symmetric Kronecker room, not determinant-map rank. Session 76's ambient reference gives a=109, not a Gram-rank measurement. Session 79 queue substring matches are different, longer partitions.

**READ — subsequent inventories.** `C:results/b13_11/candidate_inventory.part00.jsonl` rows 2984 and 5226 leave the cells open, with empty closures/resources; the corresponding ledger rows 2489 and 3373 have empty sides, prime data and ranks. The reconciliation records `cells.part03.jsonl:48` and `cells.part04.jsonl:468` likewise only import the skipped Session 54 rows. `C:results/b14_11/inventory.json` at `$/1110` and `cost_queue.json` at `$/1594` mark degree 8 `NOT_FOUND`, with no recorded full determinant rank. At commit `c40546038506fc6c7c4585dc32244a63376a91dc`, `results/b15_11/frontier.part03.jsonl:95` still calls it `UNRESOLVED CANDIDATE`, with empty recorded/replayed evidence and bounds 0..109.

**READ — closing sweeps are not a shortcut here.** The tail census places (8,6,4,2) at closing cell (36,8,6,4,2), degree 14, n_chi=2,207,134; tail (10,6,4,2) closes at (42,10,6,4,2), degree 16, n_chi=5,015,415. Session 71's frozen queue puts them at positions 397 and 497, beyond its measured prefix 1..151. Neither is in Session 60's measured closing file. Their old `pred_mem_bytes` entries price an unblocked X array, not the later blocked implementation. See `C:results/s60_tail_census.json`, `results/s71_queue.json`, and `docs/s71_report.md` §§4,6. Extracted records are in [TARGET_RECORD_EXCERPTS.json](TARGET_RECORD_EXCERPTS.json).

**READ — negative-search boundary.** The saved inventory covers all 14,130 unique blobs reachable from all local refs: 709,592,918 raw bytes, including 3,777,345,506 bytes of searched text after archive expansion. It is not a claim about uncommitted work, unreachable objects or absent remote-only commits. Numerical sidecars were inventoried, not interpreted as unlabeled new rank claims. No mathematical premise was taken from an external web source.

## Rung 1: methods and certificates

**READ — common representation model.** In ordinary coefficient coordinates, E is the integer matrix of all simple raising operators on the integral weight/stabilizer carrier. Its characteristic-zero kernel is the a-dimensional HWV space. At integer determinant pencils, V is the evaluation matrix and F=[E;V]. This is the model of `C:docs/stabiliser_reduction.md`, `C:docs/sparse_det_route.md` Lemmas 1–4, and `C:analysis/wk9_s60_cell.py`.

**HAND — full-rank implication.** A nonzero n_chi-square minor of F modulo a prime is a nonzero integer minor; hence ker_Q F=0 and `mult_det=a`. Finite samples suffice in this direction because an injective restriction to finitely many actual determinant points makes the full restriction map injective. No probability assumption is needed after the certificate verifies.

**HAND — source-lifting gate for kernel-based floors.** A matrix K with E K=0 alone is insufficient. Certify `rank_Fp E=n_chi-a` as well as an independent a-column kernel. Since `rank_Q E=n_chi-a`, a maximal minor is a p-unit; solving against it over Z_(p) makes the rational source kernel commute with reduction. Therefore `rank_Fp(VK)=r` gives `mult_det>=r`. This argument is also written explicitly in `3d3f9f8b427f257a0d5db678b1645212033652ff:docs/b15_04_proved.md`, “Rational lifting gate”.

| Recorded method | READ: what it computes | HAND: certificate of full rank | HAND: certificate of a characteristic-zero drop |
|---|---|---|---|
| s36/s38 reduced dense nullspace | Twisted orbit carrier, compressed raising rows, dense modular nullspace K, evaluation rank VK | Verified full E-kernel/rank gate and a nonzero a-minor of VK; equivalently a full-rank certificate for [E;V] | Reconstruct a nonzero rational source vector, check all raising equations exactly, then prove its determinant pullback is identically zero |
| s60 dense | Same source/evaluation map, faster sparse builder and row generation, dense source nullspace | Same; dense `full_rank` artifacts have an independent format verifier in the record | Same exact identity step; fresh points or matching primes are not substitutes |
| s60 sparse/Wiedemann | Compressed E plus pinned evaluation rows; nonsingularity of a preconditioned normal product | Replay the saved sequence and full-degree nonzero-constant polynomial condition of sparse-route Lemma 4, with matrix/point provenance; successful compression certifies the full stack | Recovered finite-field kernel vectors are candidates only; lift and verify a global characteristic-zero identity |
| s71/s79 blocked hybrid | Triangular cover, exact projected Schur nullspace, lifted and fully verified E-kernel, then VK | Cover pivots + residual rank certify rank E; independent a-kernel and a-minor of VK certify full stack rank | Same exact rational identity requirement; use `nullspace(G)`, not `nullspace(G.T)`, for source combinations |
| s56 diagonal Foulkes map / s62 orbital Gram | Exact faithful determinant restriction Theta, or G=V_source^T B V_source with rational positive semidefinite B from Theta | Nonzero a-minor over Q or modulo an admissible prime after clearing denominators | Exact rational singularity of the correctly assembled faithful Gram, with a nonzero rational kernel vector and source identification; equivalently exact Theta(v)=0 |

**READ — source locators for the table.** s36/s38: `docs/stabiliser_reduction.md`, `docs/s36_review.md`, `docs/session_38.md`, `analysis/wk9_s36_stabred.py`; s60: `docs/s60_report.md` §§1,7, `analysis/wk9_s60_cell.py`, `analysis/wk9_s45_cell.py`, `analysis/wk9_s42_sparse.py`, `analysis/wk9_s42_wied.c`; hybrid: `docs/s71_report.md` §2, `docs/s79_report.md` §4, `analysis/wk11_s71_hybrid.py`, `analysis/wk11_s71_schur.c`, `analysis/wk12_s79_cell6.py`; Gram: `docs/s56_report.md` §§1–2, `docs/s62_report.md` §§1,6, `analysis/wk10_s62_gram.py`, all at C.

**HAND — the sparse certificate is one-sided.** For the actual compressed stack F, let M=D2 F^T D1 F D2. The recorded successful scalar-Wiedemann condition is degree n_chi and nonzero constant term for the minimal recurrence from the 2n_chi-term sequence. Recomputing that condition from the actual matrix proves M nonsingular, hence F full column rank. A singular M or a lower-degree scalar recurrence can instead be caused by projection/preconditioning; it is not an equation certificate. Pinned evaluation rows must remain uncompressed. The recurrence log alone is not an independently replayed certificate.

**READ — hybrid correctness and limitations.** If T=R1[:,S] is the invertible triangular cover and U its complementary columns, the residual is `F_o[:,U]-F_o[:,S] T^-1 R1[:,U]`. The sparse projection to |U|+64 rows can only increase nullity. A lifted independent basis verified on every row of E, with size equal to projected nullity a, therefore certifies the exact modular kernel. Session 71 agrees with 72 banked cells and two independent Wiedemann re-derivations. Its recipe-style hybrid certificates are **not** accepted by the old `tools/verify` format. Session 79 fixes transposed drop extraction, sets X blocks by `S71_MEM_X`, and evaluates eight points at a time. The proposed delivery must include a real independent replay, not just the old recipe.

**READ — later refinements corroborate the same method.** B15-03 at `fde81352a5868a1d152a73716f47ecd4b285adbe:docs/b15_03_report.md` uses a native hybrid on n_chi=43,364 with residual 5. B15-04 at `3d3f9f8b427f257a0d5db678b1645212033652ff:docs/b15_04_report.md` uses n_chi=70,438/85,325 with residual 20/21 and obtains compact integral source certificates. Their ambient dimensions are only 2–4. These are useful implementation/certificate precedents, not measured timing fits for a=109/437. They do not supply a different target rank or a faster established general asymptotic law.

**HAND — exactly what a drop needs.** Exhibit a nonzero rational coefficient vector q of the stated weight/degree, prove E q=0, and verify coefficientwise or by a complete exact identity certificate that

`q(coefficients of det(s1 A1 + ... + s5 A5)) = 0`

in the 80 independent entries of the five 4-by-4 matrices. The pullback has total degree 4k (32 or 36). A complete exact faithful-Theta calculation or exact rational Gram-kernel calculation can replace direct polynomial expansion. Rational reconstruction must be followed by exact checks; further primes and fresh random points never suffice alone. To certify exact `mult_det=a-d`, provide d independent global equations and a valid rank floor a-d. For existence of a drop, one nonzero global equation suffices.

**HAND — Gram specialization.** Over Q, positivity of the faithful pullback Gram gives `ker G=ker Theta`. Over a finite field, isotropy or reduction can create extra Gram nullvectors. Thus modular nonsingularity is useful, but modular Gram singularity is not a characteristic-zero upper bound either.

## Rung 2: prices and uncertainty

**HAND — hardware and units.** Prices assume one numerical process at a time on a 64-bit Linux CPU host with NumPy/SciPy/python-flint and the recorded compiled helper; one BLAS thread and sequential primes. The historical CPU model and clock are not recorded sufficiently to promise an absolute rate. Session 71 describes a roughly 2-core/7 GB container. No speedup is credited for extra cores. GB/TB in the estimates are decimal; host reservations may use the slightly larger GiB sizes. Wall times are sequential, not CPU-core-hour totals. Rational arithmetic bit growth is not represented by a one-word memory estimate.

### Dense routes and sparse Wiedemann

**READ — timing anchors.** Session 36 records a roughly 15,500-column dense frontier and a `2.4e-8*n_chi^2` GB three-array peak; Session 38's old conservative envelope is `7.5e-8*N_S^2` GB. The ledger supplies two-prime whole-cell times. Session 60's raw dense records provide per-prime kernel times. The sparse route gives `1e-8*n_chi^2*(a+14.5)` seconds per determinant sequence (`docs/s60_report.md` §1), consistent with `docs/sparse_det_route.md` §3b's 1.7–5.3 ns per element operation.

**COMPUTED — fitted rates.** [TIMING_DATA.json](TIMING_DATA.json) preserves every selected raw timing. Among 32 s36 ledger rows with n_chi>=8,000, `total_seconds/(2*n_chi^3)` has median 1.86e-10 and range 1.74e-10..2.70e-10. Six s60 per-prime dense records with n_chi>=3,000 have median 3.72e-10 and range 2.72e-10..4.12e-10. Rounded historical times are treated as their exact displayed decimals. These are descriptive ratios, not statistically independent samples or confidence intervals.

**HAND — extrapolation envelope.** Use 1..5e-10 seconds/n^3/prime for s36 and 3..12e-10 for s60 dense, deliberately widening the observed bands. This cannot model a multi-terabyte NUMA machine reliably; it establishes that the recorded dense algorithms are unattractive. For sparse F, pinned a+8 dense evaluation rows dominate: approximate `nnz(F)=(a+14.5)n`. C CSR/CSC alone is about 16 bytes/nonzero; retained Python/SciPy copies, EV, conversion and serialization motivate a 60..100 bytes/nonzero pipeline allowance. Code: `wk9_s45_cell.py`, `wk9_s42_sparse.py`, `wk9_s42_wied.c`.

**COMPUTED — conditional extrapolations from those formulae:**

| Method and scope | Degree 8 wall | Degree 9 wall | Degree 8 peak estimate | Degree 9 peak estimate |
|---|---:|---:|---:|---:|
| s36/s38 dense, two sequential primes | 1,245–6,227 days | 21,007–105,037 days | 15.9–49.6 TB | 104–326 TB |
| s60 dense, one prime | 1,868–7,472 days | 31,511–126,045 days | 15.9–49.6 TB | 104–326 TB |
| s60 sparse, one successful sequence | nominal 9.46 days; 6.43–20.05 | nominal 227 days; 155–482 | 6.0–10.0 GB | 56.5–94.2 GB |
| s60 sparse, two primes + one sequence replay | nominal 28.4 days; 19.3–60.1 | nominal 682 days; 464–1,446 | same, sequential | same, sequential |

**HAND — sparse qualifications.** Those sparse intervals are the recorded operation-rate range, before cache/memory-bandwidth degradation, compressed-row escalation or another seed. Rebuilding F adds comparatively little but is not zero. The C-only lower arrays are 1.61/15.07 GB, and EV alone 0.76/7.43 GB; the historical 0.17 GB peak does not transfer to these large-a targets. A 16 GB / 128 GB host would be a starting reservation for this route, subject to actual allocation accounting. Even its optimistic wall prices are dominated by the hybrid below.

### The blocked hybrid: the realistic choice

**READ — anchors beyond the original brief.** Session 71 reaches n_chi=193,330 and a=640 across its sweep, with residual excess median 0.10%, p90 0.25%, maximum 0.48%; its earlier calibration used worst f=1.3%. Session 79 reaches n_chi=732,815 at `(13,9,9,3,1,1)_9`, a=70, nnz=18,374,635, residual U=1,277: hybrid 202.1/190.1 seconds per prime, build 99.9 seconds, total 1,347.3 seconds across its families, peak 4.35 GB. A distinct-part five-row anchor `(24,6,5,3,2)_10` has n_chi=188,872, a=47, nnz=1,951,800 and U=374. Sources: `C:results/s71_calibration.jsonl`, `results/s71_sweep.jsonl`, `results/s79_cells.jsonl`, `docs/s79_report.md` §4.

**COMPUTED — descriptive cross-check.** Pooling the 1,208 eligible per-prime hybrid records with n_chi>=20,000 from those three files gives median `t_hybrid/(nnz*U)=1.88e-8`, p90 4.68e-8, max 9.61e-8. The pool mixes shapes/lengths and may include repeated calibrations; it is not a probability model. Zero minima arise from historical 0.1-second rounding. Retain the published conservative `c_h=8e-8`, rather than projecting the best observed rate.

**READ — published fit.** `C:results/s71_cost_refit.json` gives build `2.1e-6*N_S*k`, five-order sieve `5e-7*nnz`, hybrid `8e-8*nnz*U`, evaluation `2.7e-8*(a+8)*N_S*k` per family per prime, and contraction `1e-9*(a+8)*n_chi*a`. Its original three-family factor is removed here because the proposed research measures determinant only.

**HAND — explicit added allowances.** Write n=n_chi=N_S, z=nnz(E), K=a+8, U=a+ceil(f*n). Take z=10n as the published central model, not as a measured target fact. Add `5e-10*U^3` seconds per pass for dense residual work; this conservative allowance may overlap the small-cell hybrid fit but exposes a growing cubic residual cost. Two-prime time is B+S+2(H+Ev+R+Residual). The audited price is `2*(B+S)+3*(H+Ev+R+Residual)`, including one independent rebuild and numerical replay. Its measured host rate must replace the assumed one-pass replay price if different. Independent implementation preparation is separate.

**HAND — memory model.** The working envelope in bytes is

`16*n*a + 100*z + 400*n + 5*max(250000000,128*n) + 80*U^2 + 500000000`.

**HAND — explanation of the envelope.** The first term covers uint32 K, an int64 copy and a temporary uint32 `K % p` copy during conversion; the next two cover sparse/live builder and verification copies, the fourth X-block and solve temporaries, the fifth Python-list/flint residual copies, and the last interpreter allowance. The recorded minimum 32-column block can exceed `S71_MEM_X=250 MB`: 4*n*32 is 267 MB at degree 9. These are conservative allocation estimates, not measured peaks or proven upper bounds. K alone is 0.355/3.646 GB; K plus int64 copy is 1.064/10.938 GB before that extra temporary. Avoid whole dense evaluation families and simultaneous primes.

**COMPUTED — conditional one-family prices, z=10n:**

| Residual scenario | U, degree 8 | Two primes | + one replay | Peak envelope | U, degree 9 | Two primes | + one replay | Peak envelope |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| f=0.10%, s71 median | 923 | 0.36 h | 0.54 h | 4.4 GB | 2,523 | 2.71 h | 4.07 h | 19.8 GB |
| f=0.25%, s71 p90 | 2,143 | 0.80 h | 1.20 h | 4.7 GB | 5,652 | 5.65 h | 8.49 h | 21.9 GB |
| f=0.48%, s71 maximum | 4,013 | 1.49 h | 2.24 h | 5.6 GB | 10,450 | 10.37 h | 15.56 h | 28.1 GB |
| f=1.30%, earlier worst calibration | 10,683 | 4.22 h | 6.34 h | 13.4 GB | 27,554 | 31.72 h | 47.59 h | 80.1 GB |

**HAND — uncertainty that matters.** Neither target's z nor U has been measured. Without stabilizer reduction, the four simple raising operators give the crude structural bound z<=4kn (32n/36n), so the z-dependent terms may be 3.2/3.6 times their central price. A host-rate factor can compound this. Residual fraction beyond the scenarios makes both U^3 time and U^2 memory grow sharply. Ordinary scenario prices of about 0.54–2.24 / 4.07–15.56 hours including a replay are therefore conditional, not guaranteed intervals. Use a separate 0.5–2 host-rate sensitivity factor until replay calibration on the provisioned host supplies rates. Do not multiply every phase by z indiscriminately. **COMPUTED:** at the structural z bound and f=1.30%, the model gives 19.08/147.22 audit hours, so degree 9 would stop for repricing under the proposed 72-hour cap.

**HAND — realistic reservation.** Reserve up to one machine-day at 32 GB for degree 8 and up to three at 128 GB for degree 9, with aggregate job-memory stops at 24/96 GB. Authorize them as separate sequential cells, degree 8 first. Build and cover precede any Schur allocation; insert measured z and U into the formula and reprice if the remaining approved time or memory budget is exceeded. These caps intentionally permit an honest “resource stop”; they do not guarantee closure of a difficult residual. Allow 1–2 working days of implementation/reviewer time to produce and test a determinant-only driver and independent verifier; that is a HAND planning allowance, not a benchmark or a promised elapsed delivery date.

**READ + HAND — exact arithmetic implementation constraint.** The recorded `matmul_mod` uses float64 only for provably exact small-limb dot products, with an inner-dimension assertion below 2^21; it does not use numerical rank tolerances. Both n values meet that bound, degree 9 by only 11,288. The adaptation must preserve/check this bound or block the inner dimension further, and audit every integer overflow bound and dtype conversion. Merely calling floating matrix multiplication without those bounds would not implement the proposed exact modular method.

### Diagonal Foulkes and orbital Gram

**READ — entry assembly dominates.** Session 62's implemented orbital assembly sweeps all `H=(4k)!/(24^k*k!)` labeled block decompositions per weight-orbit representative, at about 174 ns/H/representative measured at k=4. Its raw cost coefficient is 173.6766634725818 ns; this report rounds it upward to 173.7 ns. Session 56's earlier weight pass quotes about 62 ns. Source: `C:docs/s62_report.md` §6, `results/s62_cost.json`, `docs/s56_report.md` §5. A small final a-by-a matrix does not remove its entry-construction cost.

**COMPUTED — literal enumeration prices:**

| Quantity | Degree 8 | Degree 9 |
|---|---:|---:|
| H | 59,287,247,761,257,140,625 | 388,035,036,597,427,985,390,625 |
| s62 single H pass | 1.19e8 days | 7.80e11 days |
| s62 n weight-representative passes | 9.69e13 days | 1.63e18 days |
| s56 one weight pass, 62 ns*H*n | 3.46e13 days | 5.81e17 days |
| Current s62 label array alone, 4k*H bytes | 1.90e21 bytes | 1.40e25 bytes |
| One 8-byte n-by-n B array alone | 5.29 TB | 34.81 TB |
| Current 4-byte pair-count tensor, per orbital | 2.65 TB | 17.40 TB |

**HAND — interpretation.** These are orders of magnitude from the recorded enumeration laws, not precise future runtimes. A tenfold rate change cannot make this implementation realistic. s56 multiplicity recovery also needs the dominant-weight calculation, so its one-weight price is not a whole-cell upper bound. Exact rational entry storage only increases the one-word lower bounds; a finite realistic peak estimate is unavailable because the required label array is already impossible.

**READ + HAND — unmodified code cannot scale numerically either.** `C:analysis/wk10_s62_gram.py` materializes H labels and a weight-pair/orbital count tensor; its base-5 orbital encoding uses int64 and its pair counts int32. The encoding range at k=8/9 exceeds int64, and sufficiently large counts exceed int32. Widening or replacing them is necessary but does not solve the enumeration wall. No target Gram was built here.

**READ — the reduced-support formulation is a separate obstruction.** Session 62 prices contraction as `a*|S|^2+a^2*|S|`, with |S| the HWV union support in the weight-orbit basis; |S|=n at 11/28 tested degree-4 cells. It does not supply target |S|, target orbital counts, or a timed target-scale way to produce all required entries without enumeration. If |S|=n, the contraction alone is **COMPUTED** at 7.21e13 / 1.90e15 scalar operations, with multi-terabyte dense storage if materialized. Assigning wall seconds from a^3 or from m_det*a would omit the main work. The recorded enumerating Gram is priced out; a new compressed orbital assembler is method-specific **UNREAD/unpriced**, not a reason to declare the already priced hybrid impossible.

**READ — scope-specific alternatives.** Session 69's compact tableau circuit (`docs/s69_report.md`), the s73/s79 stable-slice constructions, and B15-05's double-epsilon bracket family (`5a019b2fb24fecf208118e628772b373235a6d61:docs/b15_05_report.md`) have demonstrated shape-specific bases/evaluators. No complete target basis, circuit-width bound and target timing law was found for these two weights. **HAND:** both targets' transpose column heights start 5,5,4,4,3,3, with further height-2/1 columns, so the cited two-tall-column construction cannot be transferred without new work. Initial-term covering alone leaves at least a-1 columns undecided after the dense evaluation rows; its useful general role is the hybrid. Source/target counting algorithms in s58/s76 are not rank instruments.

## Delivery and achievement level

**READ — resource boundary.** [RESOURCE_RECEIPT.json](RESOURCE_RECEIPT.json) records all three allowance attempts, input/output hashes, wall times and the resumed segment's timing. Raw source scanning, decompression, hashing and report writing were administrative retrieval, not rank experiments. No installation, Git mutation, subagent, other task, publication, target sampling or automatic continuation occurred. The first segment's ceiling mismatch remains documented; the explicitly authorized continuation completed before its new 45-minute checkpoint. The original failed parser source was overwritten before the first stop and only its hash survives; it produced no mathematical result. Both successful script versions and their exact inputs/outputs are retained.

**HAND — remaining uncertainty and decision.** This is a priced proposal for a modular measurement with a rigorous characteristic-zero full-rank exit. The characteristic-zero **drop proof** is specified exactly but is not assigned a fictitious completion budget: if a deficiency survives controls, record candidate status and separately price the global identity computation. No established target-scale formal identity algorithm in this record warrants promising that step within the rank-run cap.

**HAND — achievement level.** READ inventory + HAND certificate analysis + COMPUTED pricing arithmetic + a completed priced preregistration (outcome 2). No new source condition, coefficient equation, padding separation, positive multiplicity gap, geometric noncontainment or asymptotic result is claimed. A future certified drop here would establish existence of an equation only. “No five-row determinant equation is known to be nonzero on padding.”
