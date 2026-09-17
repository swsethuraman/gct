# Single five-row test

Test d=3, lambda=(4,2,2,2,2). The full stabilizer carrier has dimension 2 (fresh character computation); the ambient multiplicity is zero by length(lambda)>d. No ambient basis is needed.

Pairs are five-variable block diagonal 2+2 pencils and the partial transpose of the first block. Their determinants agree identically. A difference row is globally necessary for polynomial descent.

Build at most two independent exact epsilon-contraction carrier polynomials, using modular evaluation to certify their independence. Up to 48 proposed contractions, at two generic points. Store only distinct column tensors (heights 5 and 1). Reject a contraction plan above 2^24 intermediate entries or 10^8 contraction operations. Then use nine nodes for the skew degree, whose maximum is 8 in this cell, at two generic points. Nonzero minors prove characteristic-zero rank floors. A sampled kernel is NOT certified as a characteristic-zero kernel.

Stop if the arc already has rank 2: then no necessary fiber test adds information in this cell, regardless of its own rank. A rank-deficient sampled arc is an unresolved candidate, not a positive result. One process, 60-second/512-MiB wrapper; no larger carrier or sweep.
