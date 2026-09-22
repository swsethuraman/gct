# Complete verification price and stopping rule

UNCOMMITTED / PRODUCER ONLY. These are hand-derived bounds for checking the finite certificate in PROOF.md. They are not measured runtime or a request to run a program. Zero mathematical programs are authorized or executed in this slot.

## What must be checked globally

1. Read the six signed determinant terms and six permanent terms in PROOF.md, section 2. Establish (C) in Z[u,l,a,b,c,d,e,f].
2. Reduce (C) modulo u^2-2. Substitution of seven arbitrary linear forms gives the map factorization (F), for all 35 parameters at once.
3. Check that the displayed matrix entries are linear forms and hence are a legitimate 4-by-4 determinant pencil. Verify coordinate-ring composition (I), scalar-extension injectivity and passage to closures.
4. For the optional visibility control only, inspect four displayed coefficients of F_s and multiply their values to get -4s^2(1+s^2)^4. This control is not used as evidence of universal vanishing.

Steps 1-3 constitute a complete all-degree family-inclusion certificate. They do not infer an ideal basis from evaluations or enumerate all elements of H. The reason a finite check proves an infinite statement is the explicit factorization of the parameter maps, not a finite degree cutoff.

## Arithmetic and storage bound for the universal certificate

There are eight abstract indeterminates. Of the six determinant terms, three are single monomials, two have one factor (u+/-1), and one has both factors. Before collection this gives at most 3+2+2+4=11 monomials. The six permanent terms give six more: at most 17 raw terms to compare. Multiplication by l changes only one exponent. All exponents are at most 2. After u^2 is replaced by 2, collecting these terms produces coefficients of absolute value at most 32, a deliberately loose signed eight-bit bound.

A completely naive verifier can multiply the at-most-four factors in each of the twelve displayed permutation products and collect by a quadratic scan. At most 256 coefficient additions/multiplications and 256 exponent-vector additions suffice: for the determinant, 6 products * 3 multiplication stages * at most 4 term pairs bounds expansion by 72 updates; for the permanent the corresponding bound is 18; fewer than 40 additional updates collect/subtract/reduce, all well below 256. Even allocating 64 term records of 128 bytes, plus duplicate working storage, stays within **16 KiB of explicitly represented mathematical data**. No rational-function field, large integer, unbounded expression DAG, or elimination matrix is hidden in this representation.

Using eight-bit schoolbook integer arithmetic and direct comparison of eight two-bit exponents, the preceding expansion, reduction and at most 64^2 record comparisons fit a conservative **10^6 elementary bit-operation bound**. This is an abstract upper bound for this fixed certificate, not a benchmark, process-memory prediction, or a guarantee about a particular interpreter. Proof text and ordinary reader/software overhead are distinct from the mathematical data bound. A human can check the six displayed terms directly; no algorithmic implementation is required for this packet.

The field relation u^2-2 is fixed and monic. Denominators are absent. This bound therefore prices the full global identity and its exact field arithmetic, not a single evaluation that would leave membership unproved.

## Optional instantiated-pencil representation

For rational input forms with numerators/denominators of at most B bits each, each of the 80 pencil entries is represented in the basis (1,u). The only new coefficients are 0, signed copies of input coefficients, and the pairs produced by (u-1)f and -(u+1)f. Thus 160 rational coefficient slots suffice; their heights do not grow beyond B up to a constant sign/zero convention. Formation takes O(160 B) bit-copy/sign work and storage O(320 B) bits for numerator/denominator data, plus fixed indexing overhead. The cost of expanding a specialized quartic is unnecessary for the proof and is not silently included as zero.

## Scope of affordability

This constant certificate is affordable for the entire symmetric family S and all coefficient degrees. It does **not** price the general H pullback kernel or the all-P inclusion. Those larger tasks remain unattempted; the prior dense global/relative-chart prices are not claimed as lower bounds for all possible methods. No pilot preregistration is justified by this result.

## Exact reopening boundary

No missing scientific lemma remains for the scoped theorem. Separate delivery must bind these bytes to committed objects; a separate reviewer must audit (C), (F), the closure implication and the scope. Neither step is launched here.

A future positive five-center proposal must give a specified actual-padding T' whose form is not already ruled out by this symmetric-family lift (merely writing a nonsymmetric matrix is not proof that its form lies outside S), together with an explicit h in a named finite space, universal h(phi(B))=0, h(pi(P_T'))!=0, and a complete total price. Alternatively it must give a closure-aware complete inclusion certificate for a precisely larger family. This is a reopening condition, not a recommendation, permission, scheduled continuation or generic search request.
