# Degree-13 conversion completed

The same 39 recursive rational-source vectors now have certified circuit conversions and explicit generic evaluations at both house primes. The same 39 original circuit fillings work in the same order at both primes. Separate determinant evaluations also have certified rank 39. No degree-24 conversion was launched.

All work is in this continuation directory. The frozen S3 artifacts and the preceding control bridge were preserved; their 680 manifest entries and original archive passed the final read-only verifier.

## Certificates

Rows of evaluation matrices index basis vectors; columns index the 39 retained points. Every determinant below is for the full 39-by-39 matrix in that order.

| Exact residue | 2147483647 | 2147483629 |
|---|---:|---:|
| Native pairing determinant, det A | 1722913369 | 563415 |
| Common-source conversion determinant, det C | 1917932034 | 129088222 |
| Generic circuit evaluation determinant | 673873375 | 852494311 |
| Generic common-recursive evaluation determinant | 1359760426 | 613074802 |
| Determinant circuit evaluation determinant | 153445580 | 611475568 |
| Determinant common-recursive evaluation determinant | 1487192307 | 1920504081 |

The complete matrices, evaluations, row/point indices and conventions are in [conversion_certificate.json](C:/Users/swami/Projects/gct-gpt/Batch12_Results/S3/degree13_conversion_20260908/artifacts/conversion_certificate.json) and [evaluation_certificate.json](C:/Users/swami/Projects/gct-gpt/Batch12_Results/S3/degree13_conversion_20260908/artifacts/evaluation_certificate.json). The 6,084 individual evaluations remain in four streamed JSONL files. Exact integer generic coefficients and determinant pencils are retained in `artifacts/points_generic.json` and `artifacts/points_det.json`; each determinant point is det of a 4-by-4 pencil in nine independent directions.

## Source and common rational convention

Both source constructions finish with 1,362 DAG nodes and 349,974 inclusion entries. Each prime adds 440 certified nodes to the frozen degree-12 source. The root residual is 2,383-by-315, has rank 276, and its kernel has dimension 39. The independently recomputed 276-minors are 852981679 and 2127592554. Each new node retains its residual hash, pivot rows/columns, nonzero minor, kernel and free-row identity certificate. The complete root residual and local records are retained. First-prime reconstruction agrees exactly with the preceding pilot.

At every node, lift the first-prime inclusion entries to integers in [0,p1), combine recursively common child vectors, then apply the rational H_d average. This defines actual rational vectors; all averaging denominators are invertible at both primes. At the second prime compute the exact transport L from this common source into the native modular source. All 1,362 transports are nonsingular; det L at the root is 895536430. Matching dimensions or pivot patterns alone are never used to identify rational vectors. This is a specified rational-source convention, not rational reconstruction from two residues.

The invariant Gram forms are nonsingular throughout. At the root, the actual spherical average (I+12T)/13 equals the Gram orthogonal projector, is idempotent, and has trace 39. The transport and these checks are retained in [common_source_transport.json](C:/Users/swami/Projects/gct-gpt/Batch12_Results/S3/degree13_conversion_20260908/artifacts/common_source_transport.json), `gram_spherical.json`, and `independent_source_audit.json`.

## Pairings, conversion and normalization

The coefficient routine acts on the single column-superstandard tableau vector, using a shape-resolved matrix product representation, then contracts its Gram-weighted amplitudes with the saved inclusion DAG. It never expands the full ambient Specht module. Exact modular rank factorizations retain and verify every factor entry. Original fillings and explicit signed representatives pi_new = h pi_original c are saved for every candidate.

All 78 accepted pairing columns were computed twice: by backward corner-removal contraction and independently organized forward one-box propagation with four-box inclusion contractions. They agree entry by entry. These organizations share the local permutation-gate implementation, whose direction and transpose were validated in the preceding control diagnostics; they are not represented as wholly unrelated implementations.

Vectors are columns, A[alpha,i] = <v_alpha,rho(pi_i)e_tc>, C = G_M^(-1) A, and E_recursive = C^(-t) E_circuit. For the common basis, A_common = L^t A_native, G_common = L^t G_native L, C_common = L^(-1) C_native. Independent scalar arithmetic verifies these equations, inverse identities, every full pairing/conversion minor, and every full evaluation minor. Raw evaluation records are reconciled against the final matrices.

The map sends e_tc to the unnormalized column-wedge tensor. The house factor is (4!)^13 = 876488338465357824, with symbols m_alpha = alpha! c_alpha = 4! polarized(f)_alpha. H is averaged; horizontal-strip embeddings are all-one sums. There is no added strip, column or H factorial. The exact g_tc and column-wedge norm are recorded separately in the evaluation certificate.

## Bounded search and measured costs

The pilot justified 180 seconds / 256 MiB for source stages, 20 seconds / 256 MiB for each pairing, and 900 seconds / 256 MiB for each evaluation family/prime. Detailed preregistrations and checkpoints remain beside this report. Timing below means elapsed worker or function time, not CPU counters.

| Pairing strategy at p1 | Queries | Rank after stage | Worker seconds |
|---|---:|---:|---:|
| Stratified fillings | 200 | 37 | 396.853 |
| Single-column multiplicity patterns | 120 | 37 | 247.528 |
| Alternate permutation representatives | 12 | 37 | 23.389 |
| Control lifts and archived candidates | 18 | 37 | 31.469 |
| Source-guided path witnesses | 2 | 39 | 3.578 |

Nine queries stopped at their memory reservations; their precise gate prefixes, unfinished states and bottlenecks remain in `artifacts/pair_*_checkpoint.pkl` and [resource_summary.json](C:/Users/swami/Projects/gct-gpt/Batch12_Results/S3/degree13_conversion_20260908/artifacts/resource_summary.json). Twelve alternate representatives completed but supplied no new columns. The structured stage's coordinator recorded 2,065.766 seconds against its 420-second bound, detected between queries. Its 31.469 worker seconds do not explain the remaining wall interval. This bound overrun is retained explicitly; no further structured queries were launched after detection.

The successful fallback retained only independent coefficient-row path witnesses at each source node: 3,148 paths in 0.812 seconds. The first two resulting circuit candidates supplied the missing pairing ranks 38 and 39. The coefficient-row witness determinant itself was not used as circuit independence evidence. The same 39 circuits then took 98.889 worker seconds at p2 and all remained independent. Across the 78 selected queries: 196.623 seconds, peak resident 180,391,936 bytes, peak pagefile 202,915,840 bytes, maximum live MPS tensors 116,212,472 bytes, maximum per-shape bond rank 737, maximum summed bond dimensions 6,798. Forward contraction peaked at 20,932 entries; backward memoization at 6,296.

Source construction took 42.797 and 42.203 seconds, with peak resident memory below 135 MB. The evaluator restricts exterior-DP subsets to their exact used cardinalities. Selected evaluation widths are 4–6; maximum simultaneous DP arrays occupy 16,257,024 bytes. It matches all 16 frozen control values and four fresh degree-13 values evaluated with the frozen implementation. Generic evaluation took 350.380 and 350.536 seconds per prime; determinant evaluation took 356.964 and 353.091 seconds. Each completed all 1,521 values, with process peak resident memory below 201 MB. Values are flushed individually, and point-by-point rank growth is retained.

## What this enables next

The method works beyond the two-dimensional control with a previously known evaluable counterpart: it discovered and certified an entire new degree-13 circuit basis. The source-guided selector is a useful diagnostic, not a general guarantee that its witness fillings span after averaging or that future contraction widths stay bounded.

[S76_COMPATIBILITY.md](C:/Users/swami/Projects/gct-gpt/Batch12_Results/S3/degree13_conversion_20260908/S76_COMPATIBILITY.md) identifies an actual seminormal gauge and strip-normalization mismatch, with 12 exact small-strip checks, and the missing predecessor-level files in s76's bundle. It gives interface and storage requirements without attempting the degree-24 conversion.

The degree-24 usable 274-dimensional target basis remains unfinished. B24 = 2168 alone does not complete the source or its evaluation. Determinant rank 273, true-padded rank 274, and D = 1 remain open. See the [claim ledger](C:/Users/swami/Projects/gct-gpt/Batch12_Results/S3/degree13_conversion_20260908/CLAIM_LEDGER.md) and [replay instructions](C:/Users/swami/Projects/gct-gpt/Batch12_Results/S3/degree13_conversion_20260908/REPLAY.md).
