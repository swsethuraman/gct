# Symmetry-guided multiplicity search: shared context

Exploratory planning, 13 September 2026. Batch 17 has not been launched. Treat this context as reported project results, not independently reproduced mathematics. Distinguish your proven deductions, literature results, plausible conjectures, and untested computational proposals.

## Question

Can determinant symmetry or shared geometric rigidity predict representation cells where determinant coordinate multiplicity drops more than padded-permanent coordinate multiplicity? The informal idea is “group resonance.” Turn it into a falsifiable mathematical criterion, or explain why it fails. We want actual multiplicity obstructions, not just more equations or occurrence obstructions.

## Definitions and target

Use G=GL_16, det_4 and p=z*per_3 with independent z, embedded in 16 variables. For degree d and partition lambda of 4d, fix a consistent representation/dual convention. Write a for ambient multiplicity, m_det and m_pad for coordinate-ring multiplicities of the two G-orbit closures, and i_det=a-m_det, i_pad=a-m_pad. Desired gap is D=m_pad-m_det=i_det-i_pad>0.

A certified determinant ideal floor q and actual padding coordinate floor r prove a gap if q+r>a. A padding source ceiling U cannot replace r. If q is the complete determinant ideal dimension, q+U<=a excludes that cell. If q is only a floor it excludes only the proposed certificate based on those q equations.

Cells are representations of the same ambient G. Subgroup restriction is an auxiliary tool, not permission to compare unrelated groups. For an actual stabilizer H_det, the correctly oriented H_det-fixed multiplicity in the orbit coordinate ring bounds the closure multiplicity above. Determine the exact character, transpose component and dual convention; an identity-component calculation may give a looser upper bound. Large stabilizer dimension alone gives no ordering of invariant dimensions across representations. Dividing a vector-space dimension by a finite group order is not a general invariant-dimension lower bound. A proposed permanent lower bound needs actual independent regular coordinate functions, not merely stabilizer-compatible vectors on its orbit.

## Accepted project results

We have global Hessian-divisibility determinant equations with exact nonzero evaluations on invertible transforms of z*per_3. Thus p is outside the det_4 orbit closure. No positive multiplicity obstruction has been found. Noncontainment can hold when all tested multiplicity gaps are negative: distinct restriction kernels need not have unequal dimensions in the required direction.

Stable ten-row tail (19,2^8): a=429, m_det=418, i_det=11, and 243<=m_pad<=288. Therefore -175<=D<=-130; seeking rank 419 here is impossible. The upper bound uses the source of products l*C with C a cubic in at most nine essential variables. Generic l*C in ten cubic variables is a different, larger comparison family.

For weights lambda=(4d-t-16,t,2^8), the complete determinant ideal filtration is:
- t=15: dimension 1 for d>=23, zero through 22.
- t=17: dimensions 2,3,4,4,4 at d=23,24,25,26,27, zero through 22.
- t=19: dimensions 4,7,9,10,11 at those degrees, zero through 22; all 11 thereafter.

Declared cells already excluded: (d,t)=(23,15),(25,17),(26,17),(27,19), with (a,i_det,U) respectively (189,1,158),(294,4,218),(294,4,218),(429,11,288). Their D upper bounds are -30,-72,-72,-130.

Six nearby cells have not yet had their finite ambient/source counts computed in the roadmap: (23,17),(24,17),(23,19),(24,19),(25,19),(26,19). Their known i_det values are 2,3,4,7,9,10; coarse U values 218,218,288,288,288,288. These are screening candidates, not positive signals or permission for brute-force computation.

A certified five-dimensional determinant equation subspace restricts with exact rank 4 to both nine-variable split cubics and actual padding, leaving one shared equation. This establishes separation but not a positive multiplicity gap. An external sampled claim that the full eleven-space restricts with rank 9 remains unproved.

The Hessian mechanism uses rank<=8 at singular det_4 points, forcing squared divisibility of a ten-variable Hessian determinant along a pencil. A division-free global degree-23 certificate exists. This is not a new determinant-size growth lower bound. LMR's quadratic border-complexity benchmark n>=m^2/2 already covers m=3,n=4.

A tiny shared-jet control det(diag(0,I_3)+sum_{i=1}^3 x_i B_i), with 34 nonconstant coefficient functions, has no ordinary coefficient-degree<=2 relation. This does not rule out richer jets or higher coefficient degree. Matrix blocks shared across derivative orders are a possible new mechanism, not an established obstruction.

## Desired signal

Seek cells where a rigorous determinant upper bound is small, the padding source ceiling leaves headroom, and an actual padding lower-bound construction can plausibly exceed that upper bound. Compare determinant, generic quartics, split cubics with nine-variable support, and actual padding to distinguish determinant-specific loss from loss already forced by padding.

For generalization use G=GL_(n^2), p=z^(n-m)*per_m. A small explicit example, a multiplicity obstruction family, a bound beyond n~m^2/2, and a superpolynomial lower bound are different achievements.

## Literature starting points to verify

- Landsberg–Manivel–Ressayre, https://arxiv.org/abs/1004.4802
- Kadish–Landsberg, https://arxiv.org/abs/1204.4693
- Bürgisser–Ikenmeyer–Panova, No occurrence obstructions in geometric complexity theory, https://arxiv.org/abs/1604.06431
- https://arxiv.org/abs/1901.04576 on multiplicity versus occurrence obstructions; do not transfer results from other variety comparisons to permanent versus determinant without proof.

Verify exact theorem regimes from primary sources. Do not claim the occurrence barrier rules out all multiplicity obstructions.
