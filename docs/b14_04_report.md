# B14-04 — Independent dimension recounts

All four assigned dimensions are confirmed by exact character calculations: **dim N13 = 73**, **dim N14 = 159**, **a_inf(19,2^7) = 392**, and **a_inf(21,2^7) = 533**. The stable LMR control is **274**. The stable recounts now have a method independent of the scratch Weyl counter, together with a separate exact verifier. Delivery comprises one unsplit named-branch Git bundle; total numbered split-part count: **0**. The dimensions alone leave **D_LMR in [-4,+1]**.

## Status, provenance, and the fixed input

**RECORDED.** board_numbering: batch14. Actual model: **gpt-6-astra (Codex)** throughout; the launch requested xhigh reasoning. No other model or subagent was used. The actual reasoning-effort setting is not independently introspectable from the runtime. Session date: 2026-09-12 UTC (evening September 11 in America/New_York).

- Prepared branch: `b14-04-astra`.
- Frozen base commit: `9898e56941a7665f231873481dae956f08509995`.
- Frozen base tree: `cb688cd3fe454d638f3202e759e2eaa0c629739f`.
- Both required `git log -1 --format=%H batch14-base` and `git log -1 --format=%T batch14-base` matched; initial HEAD was the base and the working tree was clean.
- Preregistration commit: `d74f053f`, containing `results/PREREG_b14_04.md` and the frozen input manifest, before new mathematical measurements.
- Authoritative input identities: `results/b14_04/input_manifest.json`, with Git blob IDs and working-file SHA256 hashes. The verifier checks actual content against each frozen blob, permits line-ending differences, and verifies that the explicitly appended proof index preserves its complete frozen prefix. External launch-file hashes are in `launch_inputs.json`.
- Final head/tree and bundle prerequisites are recorded in the external delivery manifest. This avoids a self-referential commit hash in a tracked report.

**RECORDED versus new work.** The 73/159 values were already observed character-method pilots. This session formalises, controls and independently verifies them; they are not blind predictions. The 392/533 expectations were known from the scratch stable-slice implementation. Their character recounts and all independent verification here are new. No scratch counter, `a_weyl`, or `amb` is imported or executed by either new calculation program.

## Exact results and their scope

**CERTIFIED — complete finite rational calculations, with a local replayable certificate and separate verifier.** This is a session-specific symmetric-function certificate, not a new accepted kind in the repository's general rank-certificate verifier.

| Object | Exact dimension | Complete evidence |
|---|---:|---|
| N13 at (21,17,2^7) | 73 | All 15 interlacing channels; 5,586 power-sum classes |
| N14 at (25,17,2^7) | 159 | All 27 interlacing channels; 8,667 power-sum classes |
| Stable tail (17,2^7), control | 274 | All 3,522 nonzero classes in weighted degree 31 |
| Stable tail (19,2^7) | 392 | All 5,126 nonzero classes in weighted degree 33 |
| Stable tail (21,2^7) | 533 | All 7,365 nonzero classes in weighted degree 35 |

Every channel at degrees 13 and 14 matches both the original pilot and its integrator replay by its partition key. All 15 degree-13 channels also match B13-01's Weyl output. Complete channel tables are in `hpad13.json` and `hpad14.json`; their associated gzip files contain the exact power-sum expansions. Stable certificates `stable31.json.gz`, `stable33.json.gz`, and `stable35.json.gz` contain every nonzero coefficient, its integer character, and exact signed subtotals by largest cycle. There are no omitted nonzero classes or unresolved partial sums.

**PROVED — normalization interpretation.** Let V have dimension at least nine, with the coordinate-function convention in s57, and define

    N_d = HWV_lambda(Sym^d V tensor Sym^d(Sym^3 V)).

Decompose `h_d[h_3]` into Schur functions and apply Pieri to its product with `h_d`. A channel mu occurs precisely when `lambda_i >= mu_i >= lambda_(i+1)` and `|mu|=3d`; each such Pieri coefficient is one. Therefore

    dim N_d = sum_mu <h_d[h_3], s_mu>.

The fresh interlacing enumeration exhausts these conditions. The independent verifier instead enumerates the bounded compositions recursively. These are dimensions of the full normalization target; neither is a padded orbit coordinate-ring multiplicity, a reducible-image dimension, nor an evaluation rank. The pullback-to-target convention uses `PROVED.md: fixed_factor` and `channels`; proving a target dimension does not prove that the source image fills it.

**PROVED — stable-count interpretation, using s57 Proposition S.** The stable module is

    Sym(Sym^2 V' direct_sum Sym^3 V' direct_sum Sym^4 V'), dim V' = 8.

Its weighted-degree-N Frobenius characteristic is F_N in

    F(t) = exp(L(t)),
    L(t) = sum_(j=2,3,4) sum_(r>=1) t^(jr) p_r[h_j]/r.

This follows by applying the symmetric-power identity to each homogeneous summand; at fixed degree N all sums are finite. Consequently the desired multiplicity is `<F_N,s_tail>`. Proposition S's localization proof identifies this multiplicity with `a_inf`; the present calculation independently checks the combinatorial coefficients, not the geometry of that localization. In particular the stable value 533 does not by itself certify the finite rung-28 ambient value or an exact first stabilization degree.

## Arithmetic conventions and proof of the instrument

**PROVED.** Partitions and cycle types use nonincreasing positive parts, with trailing zeros removed. In the Hall scalar product,

    h_j = sum_(sigma partition j) p_sigma/z_sigma,
    z_sigma = product_i i^(m_i) m_i!,
    <p_rho,s_lambda> = chi_lambda(rho).

Thus `p_r[h_3] = p_r^3/6 + p_r p_(2r)/2 + p_(3r)/3`. The producer obtains the hpad expansions from the banked `wk8_s30_pleth.pleth_p` and uses its beta-number Murnaghan–Nakayama routine. For the stable expansion it differentiates `F=exp(L)`:

    F_0=1; n F_n = sum_(m=1..n) (m L_m) F_(n-m).

Since `m=jr`, the coefficient in `m L_m` is `j/z_sigma`, not `1/(r z_sigma)`. This recurrence determines every F_n uniquely over Q. All arithmetic uses Python arbitrary-precision integers and reduced `Fraction`s. It neither counts monomial weight spaces nor alternates over a Weyl group.

The independent verifier reconstructs F by multiplying the individual factors `exp(c p_sigma t^m)`, expanding each as `sum_k c^k p_sigma^k t^(mk)/k!`. It reconstructs hpad power expansions using a separate Newton recurrence, rather than the producer's enumeration of outer partitions. It reconstructs every character using contiguous segments of the Young diagram's outer rim, retaining only removals leaving a partition and assigning sign `(-1)^(number of occupied rows-1)`. These are exactly removable border strips. This second character routine contains no beta numbers and imports no producer arithmetic. Every saved coefficient and character agrees exactly.

**PROVED — common integral model and denominators.** Each F_N is the Frobenius characteristic of the permutation representation on set partitions of N labelled positions into blocks of sizes 2, 3 and 4. The cubic plethysm is the analogous representation with d unordered blocks of size 3. Accordingly `z_rho [p_rho] F_N` is an integer character value, and every reduced coefficient denominator divides N!. This is also checked explicitly for every stored row, including N=39 and 42 on the cubic side. The natural integral polynomial/symmetric-power model precedes the rational change to power-sum coordinates.

Both house primes, 2147483647 and 2147483629, exceed 42. Every stored denominator is verified to be a unit at each prime before comparison. Independently implemented modular Newton recurrences agree with every rational coefficient at both primes. These modular checks support an already exact rational calculation; they are not used to infer an equality from two residues.

**RECORDED — interface.** Stable rows carry `values_are` beside the values and mean `[rho, numerator, denominator, unscaled character]`. The coefficient is `[p_rho]F_N`; it is not multiplied by z_rho. The scalar product is the sum of coefficient times character, with no additional z-factor. Hpad rows mean unscaled integer cubic Schur multiplicities. No evaluation matrix is produced, so matrix orientation and tensor-entry normalization are not applicable here. A downstream source matrix would have source vectors as rows and points as columns, with relation columns K satisfying `A^T K=0`.

## Validation, including tests that fail

**CERTIFIED.** `analysis/b14_04/verify.py` is the replay entrypoint and imports only the Python standard library. `verification.json` records the exact comparisons and all mutation rejections. A run starts with status RUNNING and changes to FAIL on an exception; a missing required file cannot inherit an earlier PASS.

- The producer and diagram verifier each check full character orthogonality and hook-length dimensions for all partitions through degree 7. The producer also checks sign, trivial and conjugate characters.
- The producer checks the full Schur decompositions `h_2[h_2]=s_4+s_(2,2)` and `h_2[h_3]=s_6+s_(4,2)`, and rejects the intentionally wrong coefficient of `p_2 p_1` in the cubic normalization.
- Through weighted degree 10 the stable recurrence agrees coefficient by coefficient with an explicit finite sum of products of banked plethysms. The two degree-13 stable controls `(6,3,3,1)` and `(5,2,2,2,2)` both give 4.
- Every identity-cycle character agrees with an independent labelled-set-partition recurrence. At N=31,33,35 these dimensions are respectively 113215155877486062400000, 13867871310296842558720000, and 1844517852226181623941450000.
- Deliberately empty, missing, duplicated and altered channel lists fail. Wrong normalization and wrong character controls fail.
- The final verifier rejects 19 deliberately invalid inputs: eleven stable mutations, one missing required file, and seven hpad mutations. These include altered coefficients, characters, totals, subtotals, weights, generators, completion flags and normalization fields. The authentic complete artifacts pass first.
- Resource controls also fail as intended: requesting 128 MiB under a 64 MiB process limit raises MemoryError; a three-second wait is ended after approximately 0.42 s under a 0.4 s wall limit. These are intentional failed controls, not incomplete research calculations.

## Measured resources, checkpoints, and remaining work

**MEASURED.** Windows 11 build 26200; Python 3.12.14; 20 logical CPUs; physical RAM 33,752,997,888 bytes; available at preflight 12,873,416,704 bytes. CIM inventory was denied; the Win32 memory query succeeded. NumPy 2.3.5 is installed but is not used by the new arithmetic. No dependency was installed.

Every research calculation ran as one worker under a Windows Job Object with a 1,024 MiB process commit limit installed before work began. Numerical-library thread counts were one. The supervisor recorded the process ID and wall budget, logged measured peak commit bytes, and enforced bounded subprocess lifetime. Peak commit memory is a Windows commitment metric, not a sampled RSS claim.

| Calculation | Wall limit | Measured supervisor wall time | Peak committed memory |
|---|---:|---:|---:|
| Initial controls | 120 s | 0.11 s | 13.5 MiB |
| N13 recount | 180 s | 7.13 s | 99.2 MiB |
| N14 recount | 180 s | 23.38 s | 133.6 MiB |
| Stable expansion + all three tails | 600 s | 1.52 s | 62.2 MiB |
| First separate exact verification | 600 s | 11.94 s | 146.8 MiB |

Final verifier runs include strengthened mutation and portability checks; their precise times and peaks are in the associated `results/logs/b14_04_*.resources.json` records. All mathematical calculations completed within their budgets. A delivery-stage input check initially rejected the deliberately appended PROVED.md index, correctly writing FAIL. Its check was refined to require the entire frozen prefix plus the named session appendix; the failed log is retained and the final verifier rerun passes. No arithmetic discrepancy was involved. The stable producer's arithmetic time was 1.375 s, including writing its certificates. A conservative partition-count estimate allowed 714,919 recurrence multiply-adds through degree 35 and estimated 79.3 MiB of sparse storage; this was an estimate, while the Job Object supplied the actual memory limit.

Input-and-control checkpoint: committed preregistration plus passing controls. Substantive checkpoint: complete 73/159 and 274/392/533 artifacts, followed by exact independent agreement. Final checkpoint: this report, replay scripts, validated certificates and named-branch bundle. The progression files now indicate completion and retain complete channel rows where useful.

**NOT REACHED / OPEN — scope, not a computational bottleneck.** No assigned dimension remains unresolved. No determinant or padded evaluation rank, equation, rational source kernel, target minor, or source-to-target interpolation certificate was computed. Thus `PROVED.md: lmr_ranks` remains `a24=274`, determinant rank 273, padded rank at least 269, and `D in [-4,+1]`. A sampled five-dimensional padded kernel still does not certify five equations. Applying `complete_interpolation` still requires genuine target members, a full 73- or 159-minor on the agreed points, and exact source arithmetic. The present work supplies only the justified target dimensions. Costs for the remaining rank/interpolation work were not measured here.

**Negative results with a domain.** There are zero coefficient, character or channel discrepancies over all five complete artifacts, and no accepted mutation in the 19-case final invalid-input suite. This is not a negative obstruction decision. Finite ladder values 390/391/532, rung28, tensor evaluations and new geometry were outside scope; no time or rank estimate for them is inferred from these character timings.

## Assignment corrections and reusable interfaces

**RECORDED.** The launch correctly supersedes the packet's moving/fetch/checkout examples: the prepared branch and fixed peeled tag were used without switching the integration checkout. Its named-branch bundle instruction supersedes the packet's HEAD-only shorthand. Windows required a Job Object supervisor because Linux `timeout`/`ulimit` syntax is not portable. No new dependency was necessary.

The stable route's previously unmeasured runtime was resolved by sparse exponential recurrence. Expanding a whole ambient Schur decomposition is unnecessary; through weighted degree 35 this calculation is inexpensive. The historical memo's statement that five sampled relations are reducible relations remains conditional under the frozen evidence rules; this recount supplies no missing ideal-membership proof. Older scratch-file claims that 73/159 still have one lineage are superseded by the banked pilot and the final board.

Reusable interfaces are `exp_series` and `scalar` in the producer, `exponential_product`, `character` and `check_stable` in the separate verifier, and the saved exact cycle-class certificates. The latter can be recombined or inspected without running a Weyl counter. All relevant files are under `analysis/b14_04`, `results/b14_04`, `results/logs/b14_04_*`, and this report; the shared proof index receives only the two appropriately scoped entries. All four protected single-writer files and repository configuration are unchanged.

**Next step.** Integration can accept 73 and 159 as independently checked normalization dimensions, and 392 and 533 as independently checked stable ambient multiplicities. It must assess the separate membership, minor and exact-source evidence before drawing an ideal-dimension or D conclusion. Nothing was pushed or merged into integration, and no other session was awaited.
