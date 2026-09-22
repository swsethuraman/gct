# A25-02 — Checkable survivor specification

UNCOMMITTED / NOT RELEASED. This is an acceptance interface for a future proposal, not a construction or existence proof. PASS means the supplied data support their labelled claim; ELIGIBLE means the object is fully specified and its missing certificates are precise and priced; UNDERSPECIFIED means those data are absent; EXCLUDED means a proved applicable result rules out the proposed separation. Being outside an exclusion is never PASS.

## Logically necessary for the claimed achievement

**An exact object and map.** Supply d>=1 and h in A_d=C[Sym^4((C^5)*)]_d in ordinary coefficients, represented by a finite coefficient list or a division-free arithmetic circuit with an unambiguous translation to coefficients. More generally a finite-dimensional H with an exact basis and a kernel vector suffices. If the construction starts with source functions, give M, its polynomial basis, the map q|H, and the bridge producing h; no source necessary condition may be renamed K. State the left/right character, transposition, variable action, weight conventions and all divisions and domains if any.

**Global determinant membership.** Supply a proof h(phi(B))=0 as a polynomial identity in all 80 entries. Valid alternatives include a checked symbolic identity, a proved finite-dimensional presentation, or an injective-evaluation certificate/global rank ceiling with a matching rank floor as in IMPLICATIONS Theorem A. Membership then extends to the closure by B19-02 Lemma 3.1. Sampled zeros, a modular nullspace, a rank floor alone or an orbit-only property is insufficient. A rational recipe must be shown to define the specified polynomial globally, with cancellation justified before using values at a denominator-zero point.

**A separate actual-padding nonvanishing certificate.** Prefer T in Mat_(10x5)(Q), with row order z,y11,y12,y13,y21,y22,y23,y31,y32,y33, and an exact nonzero value h((z per_3) composed with T). For algebraic entries specify minimal polynomials and exact field representations. A proved nonzero restriction on P5 is logically sufficient for separation, but the programme requests an explicit evaluation certificate for portability. If using P5=closure{lC}, mark that equality ADOPTED and separate the dominance/closure inference from an explicit-image claim. Above five variables that equality is unavailable. A generic product is not automatically an explicit T.

**Claim strength.** These certificates prove an equation and separation at the named parameters only. To assert a positive multiplicity gap, provide the relevant representation multiplicities and comparison; one nonzero separating vector is insufficient. To assert an asymptotic lower bound, specify an asymptotic family and prove its parameter relation and uniform conclusion. A candidate need not claim either stronger result.

## Hypothesis audit required for eligibility

| filter | checkable submission |
|---|---|
| S1 | Identify any extraction matrix/minor sizes. Prove the construction is not forced into a known padding-vanishing minor ideal, or acknowledge exclusion. Rational extraction requires its separate global polynomial certificate. |
| S2 | State invariant/covariant target and determinant-twist convention. If it is in the positive-degree SL5-invariant or specified cubic-lift class, reject separation. Outside those hypotheses, explain exactly which is absent; that explanation is not a nonvanishing proof. |
| S3 | Show the alleged necessary locus contains pure powers, or directly verify h(x_1^4)=0. For membership via q this is automatic; record it as a consistency check. Passing it is not evidence of survival at other padding points. |
| S4 | When weights are used, give (n,r,d,lambda), weight versus highest-weight distinction, t and the proved/conditional status of any D* bound. For t<d, name the factored lower-degree object. Do not assert multiplicity equality or import n=5's conjectural900 into n=4. |
| S5 | State the actual statistic, semicontinuity, determinant bound, and padding comparison. Match N,j,k and all remaining premises to the scope submatrix. Non-rank relations must exhibit their own identity. |
| S6 | Give the decomposition and source symmetry proof. If tests are block-scalar interval/exact-support tests, acknowledge N=L C_arc and no improvement to the ceiling. A proposed allowed-jet/fibre relation must be explicit and its independence/effectiveness proved, not just named. |

These are conditional audits for the mechanisms actually used. It is not logically necessary to escape every theorem's hypotheses: a separator can pass a necessary condition (e.g. the pure-power test) while lying in that theorem's ambient category. What is necessary is to avoid the theorem's proved nonseparating conclusion. Explanations of failed hypotheses are required only where that exclusion was proposed as applicable.

## Finite certificate and price: programme feasibility

Before any pilot, submit one identity proof plan, dimensions, sparsity, coefficient heights, working-memory peak including copies, expected wall time and a hard stop. This is a programme feasibility requirement, not a theorem that expensive separators cannot exist.

For a matrix plan let a=dim H and b=dim M. Supply exact bases and polynomial expansion identities for the b-by-a Q, evaluation matrix R if used, the padding row p, and v with Qv=0, pv nonzero (or the proved exact-kernel substitute). A full unstructured choice has a=binom(d+69,69), b=binom(4d+79,79); no dense computation at those sizes is authorized. Dense elimination has arithmetic cost bounded by O(ab min(a,b)) and stores O(ab) field elements, in addition to constructing Q; rational bit growth must also be priced. A tailored M can reduce b only after its containment and basis are proved. Sampling/injective evaluation requires pricing the number of functions and evaluations, not just one cheap filling.

For a sparse direct certificate, clear h's denominators and suppose it has S terms and integer coefficients of at most H bits. Each phi_alpha has at most 576 signed raw determinant-expansion terms: 24 permutations times at most 24 assignments of four variable choices for a fixed alpha. A degree-d monomial in the c_alpha expands into at most 576^d raw products. Thus a deliberately conservative expansion cap is S*576^d raw terms, with at most binom(4d+79,79) distinct entry monomials; a source coefficient has at most H+ceil(log2 S)+ceil(d log2 576)+2 bits under this raw bound. Encode each exponent vector (80 entries, exponents <=4d), coefficients and indexing overhead when computing memory. This is an algebraic upper-bound formula derived by hand, not a runtime forecast or an executed enumeration. Circuit identities can be much cheaper but require a stated verification proof. An exact padding evaluation of a given sparse h can be priced by computing 70 quartic coefficients and at most S products of d factors, with bit lengths from the submitted T and h. No numerical price in seconds is defensible before those inputs are fixed.

Any mathematical pilot would additionally need the shared COMPUTE_PROTOCOL, a coordinated exclusive reservation, first-output preregistration hash, identity-based controls, one process/BLAS thread, enforced <=60 seconds and <=512 MiB per pilot, at most three launches and <=180 seconds total, and untouched original failure receipts. No pilot is proposed by this packet.

## Current decision and one next certificate

The abstract coefficient-kernel route has an exact mathematical interface but no submitted feasible H/h/T instance. Row 3 lacks its matrix/minor-family/identity triple. The large-minor polynomial control fails the interface because its output is padding-blind.

**One next certificate to request, not launch:** a single explicit rational pair (h,T), with d, a finite coefficient/circuit representation of h, a global proof of h(phi(B))=0 and exact h((z per_3) composed with T) nonzero, accompanied by its size/bit/memory price. Theorem A supplies an alternative finite linear-algebra form of this same certificate. Until one is specified, there is no justified numerical job or reserve session.

Existence of an affordable specified proposal meeting this interface remains OPEN here; so does exhaustive coverage by the six exclusions. This does not withdraw the record's abstract/existential claims under their adopted premises: B19-02 records a particular padding point outside D45 as ADOPTED from B17-01-C, and a point outside a closed affine variety necessarily has some separating polynomial. That input is not re-certified or used as a new witness in A25-02. No known explicit padding-nonzero five-row determinant equation is supplied by this assessment.
