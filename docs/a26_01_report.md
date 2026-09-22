# A26-01 — symmetric padding has an exact determinant lift

**Registered outcome (2): PROVED scoped containment/no-go, PRODUCER ONLY / UNCOMMITTED.** Every quartic obtained by multiplying the permanent of a symmetric 3-by-3 matrix of linear forms by another linear form is an actual 4-by-4 linear determinant. For rational input, the explicit pencil has coefficients in Q(sqrt(2)). This covers every fixed variable change of A25-04's old witness and strengthens its five-center completion to equality of the full quartic. **General actual-padding containment in the closed five-center determinant image remains OPEN.**

No separating equation, positive multiplicity gap or asymptotic lower bound is produced. The degree-eight coefficient space below is exactly specified, but its determinant kernel is not computed. The complete certificate closes the selected padding family for every coefficient polynomial, in every degree.

## 1. Exact family and complete certificate

Work over C, with ordinary coefficients. Set D=closure{det(sum_(i=1..5) x_i B_i)} and let P be the closure of actual substitutions of z per_3. The selected family consists of

    F=l per [a d e; d b f; e f c],

where l,a,b,c,d,e,f are **arbitrary linear forms in five variables**. Its actual-padding map has rows (l,a,d,e,d,b,f,e,f,c), so this is a specified restriction of the general 10-by-5 substitution. No equality with the full product locus is assumed.

The decisive universal identity, with u an indeterminate, is

    M_u = [a   d             e
           -d  b          (u-1)f
           -e -(u+1)f        c],

    det diag(l,M_u)-l per[a d e; d b f; e f c]
        = (u^2-2) l a f^2.                              (C)

**PROVED by hand:** expanding six determinant terms gives abc+be^2+cd^2+(u^2-1)af^2+2def. The six permanent terms give abc+af^2+be^2+cd^2+2def. Set u=sqrt(2), and (C) is the desired exact equality. No research code or symbolic micro-test was used.

Let S be the closure of this specified family's image. The explicit matrix proves literal family membership in the determinant image, hence S subset D. Consequently every determinant equation, including every equation in the five-center ring, vanishes on S. This is a complete all-degree certificate **for S**, not a whole-P theorem. [PROOF.md](../results/a26_01/PROOF.md) states the maps, coordinate-ring composition and closure argument in full.

There are no parameter-dependent denominators. The fixed quadratic extension has relation u^2-2; either conjugate supplies the same quartic, and scalar-extension injectivity handles rational coefficient equations. No ordered binary roots, chart specialization, elimination cutoff or automatic closedness of projection is used.

## 2. Named H and the retained-information check

Let E={alpha in N^5: |alpha|=4 and max alpha>=2}; these are the 65 retained five-center coefficients. Choose

    H=(Q[c_alpha:alpha in E])_(coefficient degree 8,
                              substitution weight (24,2,2,2,2)).

An exact monomial basis is all products product c_alpha^(m_alpha) with sum m_alpha=8 and sum m_alpha alpha=(24,2,2,2,2), in lexicographic exponent-array order. This is a finite coefficient-weight space, not an asserted highest-weight or tableau space. It includes c_(4,0,0,0,0)^6 c_(0,2,2,0,0) c_(0,0,0,2,2), beyond the first-center jet. No basis enumeration is needed for the map-factorization certificate, which covers the whole ring.

The five omitted squarefree quartics remain omitted. To test genuinely changed retained information, consider the actual substitution

    l=x1, a=x1+x5, b=x1-x5, c=x1,
    d=x2+s x1, e=x3, f=x4.

The old signed determinant differs from its padding by 2x1x2x3x4+2s x1^2 x3x4. The second summand is retained, so for s!=0 the old signed matrix stops being a completion. This is a concrete algebraic visibility change, not recovery of the fixed projection kernel.

The complete obstruction is that (C) gives a different determinant presentation of the **entire** sheared form. An explicit visibility control h_star in H has value -64 at s=1; that same form is an algebraic determinant, so h_star is rejected as a determinant equation. It uses first-center coefficients and is only a visibility control, not a revived positive candidate. Thus repairing the old visible discrepancy within this symmetric family cannot supply separation.

## 3. Exclusions and achieved level

[EXCLUSIONS.md](../results/a26_01/EXCLUSIONS.md) checks the actual committed statements: B22-02 **L1-L6**, B22 review caveats, corrected GKZ threshold scope, A25-02 Application 3, B25-04's component theorem and erratum, A25-04's ten-minor algebra, and the old T completion. Their scopes do not collectively prove a whole-ring no-go for H. No large-minor extraction, invariant/cubic-covariant lift, rank threshold, tableau spanning assertion or graph argument is assumed. The numerical onset floor retains its adopted status; degree and tail 8 do not by themselves imply viability.

The new exact lift closes the selected symmetric-family route directly. It needs none of C_PER, C_DUBE, the historical rank computations or the unreviewed general B17-01 claim. The global programme baseline remains **no construction ready**. C45's accepted unpadded n=3, degree-12 status is preserved and is unrelated to this result.

Achieved level: **scoped geometric containment/no-go**. A nonzero coefficient function and actual-padding visibility were exhibited, but no determinant equation nonzero on padding, positive multiplicity gap or asymptotic lower bound was established.

## 4. Global price, limits and exact reopening boundary

[VERIFICATION_COST.md](../results/a26_01/VERIFICATION_COST.md) prices the **complete** universal certificate: at most 17 raw monomial terms, a conservative 256 coefficient-operation bound, at most 16 KiB of explicitly represented mathematical data and fewer than 10^6 elementary bit operations under the stated naive representation. These are hand-derived upper bounds, not measured process resources. The map factorization proves all-degree inclusion without enumerating H or an elimination basis. Cheap single-point evaluation is not substituted for global verification.

No scientific lemma remains missing for this scoped theorem. Byte-preserving committed delivery and an independent hand audit are separate outstanding steps. For the general question, the missing certificate remains either I(Y5) subset ker(q_P) for the full actual-padding parametrization, or one explicit global determinant equation with a certified nonzero value at a new actual T'. The current identity cannot be generalized to arbitrary independent off-diagonal forms by assertion. A future proposal must first avoid this certified family and supply its own complete price. No follow-up is launched. [LIMITATIONS.md](../results/a26_01/LIMITATIONS.md) makes every scope boundary explicit.

## 5. Provenance, time and delivery

First actual clock / conservative substantive start: **2026-09-22 20:16:38 UTC**. Early checkpoint: **20:20:57 UTC**. Mathematical stop: **20:25:46 UTC**. Conservative substantive interval: **9m08s**, including interleaved reading and administration; no interruptions or time deductions. Packet administration follows the stop and is timestamped separately. [CHECKPOINT.md](../results/a26_01/CHECKPOINT.md) preserves the incremental decision, and [RESOURCE_RECEIPT.md](../results/a26_01/RESOURCE_RECEIPT.md) records the clock sequence.

**Zero mathematical programs, zero pilots and zero mathematical computational seconds.** No lease, other session/subagent, task message, installation, Git mutation, paper/shared-ledger edit, publication or automatic continuation occurred.

The fresh byte audit matched **107 dispatch bindings**, resolved **110 distinct committed objects**, and verified **95 manifest payload declarations**, with zero mismatches. It did not replay mathematics or recursively verify every historical premise. [INPUT_BINDINGS.json](../results/a26_01/INPUT_BINDINGS.json) records the bindings; [SOURCE_METHOD_LEDGER.md](../results/a26_01/SOURCE_METHOD_LEDGER.md) distinguishes READ, hand derivation, SECONDARY and UNREAD. No external PRIMARY reading is claimed.

Assigned repository: C:/Users/swami/Projects/gct-gpt/work/batch15; branch **batch15-launch**; HEAD **d00da15c830cd2bc9bec8c3e8b4260506c9e1f2f**. Unrelated untracked work is preserved. All output paths remain **UNCOMMITTED / PRODUCER ONLY**. [MANIFEST.json](../results/a26_01/MANIFEST.json) binds raw payload bytes and excludes itself; [PROPOSED_DELIVERY_PATHS.txt](../results/a26_01/PROPOSED_DELIVERY_PATHS.txt) lists the exact later delivery footprint. There is no producer delivery commit and no independent acceptance yet.
