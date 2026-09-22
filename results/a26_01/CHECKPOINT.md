# A26-01 checkpoint

UNCOMMITTED / PRODUCER ONLY. Actual clock observation: **2026-09-22 20:20:57 UTC**, 4m19s after the conservative substantive start at 20:16:38 UTC. No interruption has occurred. This early checkpoint records a decisive scoped containment, so no further mechanism search is selected.

## 1. The exact coefficient space

Work over Q and then C. Let E={alpha in N^5: |alpha|=4, max(alpha)>=2}; these are the 65 retained ordinary quartic coefficients. Set A5=Q[c_alpha: alpha in E]. Give c_alpha coefficient degree 1 and substitution weight alpha. The producer-selected space is

    H = (A5)_{degree 8, weight (24,2,2,2,2)}.

Its exact monomial basis is {product_(alpha in E) c_alpha^(m_alpha): m_alpha in N, sum m_alpha=8, sum m_alpha alpha=(24,2,2,2,2)}, ordered lexicographically by m after ordering E in descending lexicographic order. This finite set is a basis because A5 is a polynomial ring. It is a weight space, not an asserted highest-weight space or a tableau span. No basis enumeration or mathematical program was used.

H genuinely permits coefficients beyond the first-center jet: c_(4,0,0,0,0)^6 c_(0,2,2,0,0) c_(0,0,0,2,2) is a basis monomial. This is not a claim that H contains a determinant equation or a separator.

## 2. Exclusions

The applicable committed B22-02 L1-L6 statements and B22 review caveats, corrected GKZ scope, A25-02 Application 3, B25-04 component theorem/erratum, A25-04 and A25-05 completion were read. Their precise applicability is recorded in EXCLUSIONS.md. H has no stipulated large-minor, invariant/cubic-covariant, rank-threshold or single-tableau factorization. Its tail is 8, equal to its coefficient degree, so the inherited adopted degree-eight floor does not itself close H. None of these scope observations is positive feasibility evidence. A25-04's ten-minor subalgebra remains closed, and its old T is forbidden as a separator witness.

## 3. Retained information and the decisive obstruction

The trial actual-padding family is l per[a d e; d b f; e f c], with all seven entries l,a,b,c,d,e,f arbitrary linear forms in five variables. In the particular shear l=x1, a=x1+x5, b=x1-x5, c=x1, d=x2+s x1, e=x3, f=x4, the old signed completion differs by 2x1x2x3x4+2s x1^2 x3x4. Only the first summand is discarded. Thus c_(2,0,1,1,0) does see this discrepancy: it equals 2s on padding and 0 on that old signed determinant. The five squarefree-quartic directions remain discarded, unchanged.

But a different constant lift defeats the entire trial family. With u^2=2,

    M_u=[a d e; -d b (u-1)f; -e -(u+1)f c]

satisfies det M_u=per[a d e; d b f; e f c]. Therefore det diag(l,M_u) equals the actual padded quartic itself. This is the complete obstruction for this family, not failure of a particular projected equation. Arbitrary changes of the seven linear forms and their limits are covered. General nonsymmetric actual padding is not decided.

## 4. Complete verification and outcome

The universal certificate is the six-term polynomial identity

    det diag(l,M_u)-l per[a d e; d b f; e f c]
        = (u^2-2) l a f^2

in Z[u,l,a,b,c,d,e,f]. Reducing modulo u^2-2 proves the parameter-map factorization globally. It implies I(Y5) maps to zero on this family's entire parameter ring, in every degree, without computing a pullback matrix for H. Closure follows because D is closed and every literal family member is already an actual determinant. Constant field extension creates no parameter denominator or eigenvalue descent issue. VERIFICATION_COST.md gives a deliberately conservative constant-size arithmetic/storage bound for this complete certificate, not a cost for one sampled evaluation.

**Registered outcome (2), scoped no-go/containment.** The positive mechanism is closed on the selected symmetric family, including the proposed shear. No separator, multiplicity gap, asymptotic bound, whole-P containment, or computation request results. No missing scientific lemma remains for this scoped identity; independent review and byte-preserving delivery remain pending. The general five-center comparison stays OPEN.
