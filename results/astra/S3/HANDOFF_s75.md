# Integrator handoff to s75: the operator is available; four evaluation pairings remain

This is a local artifact, not a dispatched message. Use the final proposal's s75 assignment. The compact source recurrence has passed the dimension half of the n4 degree-12 control; full evaluation readiness has not passed.

Read [S3_report.md](C:/Users/swami/Projects/gct-gpt/Batch12_Results/S3/S3_report.md), especially §§3–7. Exact executable inputs are [pairing_handoff.json](C:/Users/swami/Projects/gct-gpt/Batch12_Results/S3/artifacts/pairing_handoff.json), [spherical_control.json](C:/Users/swami/Projects/gct-gpt/Batch12_Results/S3/artifacts/spherical_control.json), and the two `d12_p*_nodes.json` DAGs. The fixed code base is c984e2c6d59ba0bbc6ac2fdd113edf920a8aebd9; final Python sources have individual hashes in the artifact manifest.

**Already done:** exact local seminormal block swaps, ordered Pieri embeddings, rectangular residual `(F-I)J`, rational Gram formula, actual spherical operator, specific good reduction, 31-to-2 at both primes, all C12 terms, and all 42 target local F blocks. Do not rederive these from old raw-tau prose. All these matrices have columns as vectors, shapes in descending lexicographic order, and all-one horizontal-strip extensions in the specified seminormal gauge.

**Next bounded target:** compute the four scalars `A[alpha,i] = g_tc * [e_tc] rho(pi_i^-1) v_alpha`, with alpha and i each 0 or 1. No permutation, factorial, or basis ordering is unspecified: all are in the JSON and report. Then `C=Gram_M^-1 A` and recursive evaluations are `(transpose(C))^-1` times the banked circuit evaluations. The two permutations have inversion lengths 579 and 640. A routine supporting only adjacent whole-block swaps does not automatically answer these arbitrary-permutation coefficient queries.

**Success:** C is nonsingular; the same recursive basis is evaluated on the saved generic and determinant points; the two-minors and all normalization factors are independently checked. The fresh banked determinant minor already proves abstract injectivity of the whole two-dimensional source. The missing requirement is an executable evaluation/conversion interface for the constructed vectors.

**Common-field rule:** the modular DAGs select bases independently. Do not identify their entries as one rational matrix without proof. Either perform rational recursion, or use the report's explicit H-average lift at P1 and reduce that same rational basis at P2, carrying any basis transform. Modular kernels are not lifted by guessing rational entries.

**Kill:** stop a coefficient routine that requires global ambient Specht/HWV expansion or an unpriced global transition table. Proposed first trial: 30 minutes and 256 MiB measured workspace for the new coefficient routine. Record the exact failed coefficient and contraction width rather than silently increasing the carrier.

**Fallback:** return that coefficient obstruction, or supply a bounded evaluator for the normalized Pieri inclusion on arbitrary form tensors. Keep the certified operator and control basis intact. Do not use random evaluation to solve a basis transform before one side has an evaluator.

**After the complete control passes:** compute the target precursor and full source under the report's recurrence; measure C24 and weighted DAG/edge storage; retain a 1894 residual minor and 274-column kernel. Independently reproduce every B24 term. Carry det/red/true-pad in common coordinates. Stop determinant work at certified 273, padded work at certified 274. No target rank or D result was established by S3.
