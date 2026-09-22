# A25-03 — two-frame second-jet data are dense

**Outcome (3): a proved scoped no-go. LOCAL COMPLETE, UNCOMMITTED / NOT RELEASED; producer-only.** For every fixed pair of frames with distinct center lines in C^5, the joint projection of five-variable 4-by-4 determinant pencils onto their second transverse coefficient jets is dense in the actual joint-data space. Each frame contributes 15 linear coefficient functionals; their intersection has dimension one, so the joint space has dimension **29**, not 30. There is no nonzero determinant coefficient equation in this joint ring, in any polynomial degree.

This result closes the assessed two-frame family. It produces no padding separator, multiplicity gap or asymptotic bound. **Zero mathematical pilots; zero mathematical computational seconds.**

## Exact family and frame scope

Use V=C^5, W=Sym^4(V*), X=(Mat4)^5 and phi(B)=det(sum_i x_i B_i). A frame is an ordered basis (v,u1,...,u4). Retain the coefficients of t^4, t^3 yi and t^2 yi yj in F(tv+sum yi ui). Their functional span in W* is v^2 Sym^2 V, independent of the complementary basis. For nonproportional v,w the intersection is C v^2 w^2. These facts, their ordinary-coefficient conventions and the induced GL5 action are proved in [FRAMES.md](../results/a25_03/FRAMES.md).

The one frozen representative uses the identity frame and the rational permutation g swapping e1,e2. With z_a=x_(a+2), an independent joint basis is:

- the five binary quartic coefficients in x1,x2;
- the twelve coefficients x1^(3-k) x2^k z_a, k=0,...,3 and a=1,2,3;
- the twelve coefficients x1^2 z_a z_b and x2^2 z_a z_b, a<=b.

The duplicated coordinate in the two original 15-arrays is x1^2 x2^2. Equality of its two names is the only universal linear relation, and generates every universal polynomial relation in that redundant presentation. A determinant-specific equation must survive this quotient.

The representative covers **every fixed distinct-center pair**, not just a generic pair: GL5 transports the two independent center vectors, while changes of their transverse complements induce invertible changes of retained coordinates. On pencils F(x)->F(Ax) is the invertible mixing B'_j=sum_i A_ij B_i. Both sides of this transport are proved, rather than inferred from a classification of full frame pairs. Frames are fixed data; no hidden or coefficient-dependent frame variables are admitted. Proportional centers reduce to the single-frame result independently verified below.

## Proof certificate and global implication

The base pencil is

    B1=I4, B2=diag(1,2,3,4),
    B3=E12+E13, B4=E14+E23, B5=E24+E34.

[PROOF.md](../results/a25_03/PROOF.md) specifies an affine 29-parameter family through it, with exact source-entry and target-coefficient bases. Its differential has a 5-by-5 binary block of determinant 12, three 4-by-4 first-transverse blocks each of determinant 12, and six 2-by-2 second-transverse blocks. The latter use complementary eigenvalue products (12,8), (6,4), (3,2), repeated three, two and one times respectively. Their determinants are -4,-2,-1. Therefore the complete differential has determinant

    12^4 (-4)^3 (-2)^2 (-1) = 5,308,416 != 0.

[JACOBIAN_CERTIFICATE.json](../results/a25_03/JACOBIAN_CERTIFICATE.json) records the exact integer base, 29 row exponent vectors, 29 source directions and blocks. This certificate is **PROVED by hand from the determinant permutation expansion**, not a computed or modular rank claim.

The global implication is also proved directly: a hypothetical nonzero relation, translated at the target base point, has a lowest nonzero homogeneous part. Substitution through a map with invertible linear term preserves that nonzero lowest part, contradicting an identically zero pullback. Hence the affine family is dense in the target, so no relation can vanish on every determinant pencil. A successful full-rank certificate on this slice proves global independence; an unsuccessful slice would not have proved nondominance.

Equivalently, if R_(2,g) is the polynomial subring on the 29 independent joint coefficients, then ker(phi*) intersect R_(2,g)=0 in every degree. In the redundant 30-name ring the kernel is exactly the universal overlap ideal. No ambient high-degree basis or elimination matrix was expanded.

## Prior inputs, exclusions, and actual padding

The A25-01/02 packets were read as explicitly provisional, uncommitted research input. All 15 and 14 manifest payload hashes respectively matched their current bytes. The single-frame rational section and closure of padding-blind ideals under GL5 translates are independently re-derived in [INDEPENDENT_LEMMAS.md](../results/a25_03/INDEPENDENT_LEMMAS.md). There is no conditional A25-01/02 premise in the new theorem, and no promotion of those packets to independent acceptance.

[EXCLUSION_PADDING.md](../results/a25_03/EXCLUSION_PADDING.md) checks all six inherited exclusions against their actual hypotheses. The source-Jacobian rank here is not a form-space rank-threshold separator; the fixed-frame ring is not an SL5 invariant/covariant construction; the old five-block support theorem leaves allowed-jet relations outside its scope. The new proof settles this particular family directly. The pure-power check and tail theorem are necessary checks in their own regimes, not substitutes for the differential proof. Mixing previously padding-blind generators remains blind, but that observation alone would not settle mixed jets.

Actual padding is P_T=(z per3) composed with T, T:C^5->C^10. **No nonzero h from this family vanishes globally on determinants, so none can separate at any actual P_T.** This conclusion needs neither the ADOPTED equality with all products lC nor an inferred explicit T. The formal overlap relation is zero on all quartics. No nonzero padding evaluation is claimed; the status is impossibility within this family, not an untested promising equation.

C45 remains the unpadded n=3 control, PROVED modulo (star), and the cap retains its named adopted inputs and historical read-status qualifiers. No existing scientific label is upgraded.

## Timing, evidence and delivery

Assessment start 2026-09-21T03:27:10Z; mechanism frozen at 03:28:13Z; outcome settled by 03:30:32Z. The selection and proof assessment were inside the 45-minute/half-session gate. Remaining time was packet writing, audit and verification. [RESOURCES_NEXT.md](../results/a25_03/RESOURCES_NEXT.md) gives exact object sizes, bit bounds, zero-pilot receipts and limitations.

**One next certificate:** independent hand audit of J29, its overlap/transport argument and its global polynomial implication, estimated 20-40 minutes. There is no missing scientific lemma in this producer proof; independent review and committed delivery remain open. No third-frame, higher-jet or full-elimination follow-on is proposed or launched.

Evidence method: READ of the bound inputs plus independent hand derivation; no computational REPLAY or INDEPENDENT EVALUATOR. [SOURCE_READS.md](../results/a25_03/SOURCE_READS.md) records PRIMARY/SECONDARY/UNREAD at each use; [SOURCE_BINDINGS.json](../results/a25_03/SOURCE_BINDINGS.json) distinguishes verified committed blobs from provisional and administrative UNCOMMITTED bytes. No external theorem is load-bearing in the new proof. No tool memory was created or consumed.

Starting and ending baseline: batch15-launch at 82633a60893236fab4fbc317df416e1b8a349005, subject to the final read-only check in ADMIN_VERIFICATION.json. All writes are confined to this slot's paths. No Git mutation, paper edit, extra task/agent, installation or publication occurred. Concurrent files were preserved.

[MANIFEST.json](../results/a25_03/MANIFEST.json) binds every actual payload file except itself. [DELIVERY_NOTE.md](../results/a25_03/DELIVERY_NOTE.md) and [ADD_LIST.txt](../results/a25_03/ADD_LIST.txt) give the complete explicit proposed footprint. Every new hash identifies UNCOMMITTED bytes. G29, byte-preserving delivery and independent acceptance remain pending; no delivery commit exists.

The three generated metadata JSON files have raw-versus-Git-filtered byte differences, recorded for the later delivery pass. No normalization or attribute change was made.
