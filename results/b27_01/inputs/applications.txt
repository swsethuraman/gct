# A25-02 — Three frozen applications

UNCOMMITTED / NOT RELEASED. READ of the pinned record plus the hand proofs in IMPLICATIONS.md. No unfinished A25-01 material is an input. Assessment words ELIGIBLE IN PRINCIPLE, UNDERSPECIFIED and EXCLUDED below are defined locally; none means a candidate has been built unless its data are actually supplied.

## 1. Row 12 / coefficient-kernel bridge

**Recorded object.** B19-02 sections 2–3 gives the graph equations c_alpha-phi_alpha(B) in the ring C[c,B], with 70 coefficient and 80 parameter variables. Eliminating B gives I(D45)=ker phi*. Equivalently, in degree d, choose an exact subspace H of A_d and construct q|H. This object is coefficient-side, whereas B22-02 row 12 names possible relations among allowed source jets, compatibility across a limit fibre and special-locus cancellations in a finite M on the parameter side. No equality between their kernels is implicit.

**Bridge required.** A row-12 proposal must name M and E_H, prove that each source function belongs to M, and supply either a globally correct coefficient expression h or an explicit q presentation plus an exact kernel/evaluation certificate as in Theorem A. A relation among source tests can improve a ceiling only if it gives a new, universally valid constraint on E_H. Descending a source function into E_H, even if proved, constructs a coefficient function modulo K; it does not by itself construct a nonzero element of K. Conversely Nq=0 for a necessary test supplies no coefficient equation at all (Theorem B).

**Applicability.**

| exclusion | disposition for the abstract instruction “find h in K” |
|---|---|
| S1 | No r-minor factorization has been specified; NOT APPLICABLE to the abstract kernel. A resulting h may still lie in the excluded minor ideal. |
| S2 | No invariant/covariant regime has been specified. If h is a positive-degree SL5 invariant it is excluded; a non-rectangular weight alone is not a separation proof. |
| S3 | Tautologically passed once global membership is proved: h(x_1^4)=0. This says nothing about nonvanishing at a different actual padding point. |
| S4 | Applies only after d and a weight/cell are specified. Any separating weight must obey its scoped tail bound; no numeric det4 onset is invented. |
| S5 | No statistic or threshold matrix is specified; NOT APPLICABLE. Global coefficient membership must still be proved by another means. |
| S6 | Applies to source tests only after M/actions are fixed. The old block-scalar tests provide no new ceiling. Relations among allowed jets remain outside its scope, with construction and effectiveness OPEN. |

**Row 10 is not another equation source.** Under scheme-theoretic containment and ht I_3(B)=2, B23-02 Proposition 1.1 expresses a containing quartic as det[B;m]. Closure of the genuine incidence image is D45, so R1 is precisely the same kernel/elimination problem. This implication is PROVED modulo its named Hilbert–Burch and grade=height classical inputs, read via row10=68866e6d and review23=239dd6e8 section 5.4. Boundary incidence enlargements require their own presentation; that boundary is not declared equal to D45. Under set-theoretic containment the reviewed triple-plane example instead makes that version padding-blind. This is part of the same recorded bridge application, not a new construction proposal.

**Verdict: ELIGIBLE IN PRINCIPLE as an exact membership framework, UNDERSPECIFIED as a feasible construction.** “Find h in K” covers every equation by definition but provides no d, H basis, nonzero v, injective evaluation certificate, actual-padding witness or affordable verification price. No separator is accepted here. This assessment does not prove that row 12 is impossible or that all equations must be found by literal elimination.

## 2. Non-rank smaller-minor relations (row 3)

B22-02 row 3 and B20-02 section 8 describe minors of d_j^(k) of size at most the determinant maximum, potentially vanishing for reasons other than rank. That description does not specify a triple consisting of a matrix, minor family and proposed identity. The reviewed statements and B22-10 section 6 retain the lack-of-mechanism assessment; no later committed construction is supplied by the authoritative inputs read here.

**Verdict: UNDERSPECIFIED; stop.** Missing data are:

1. Exact N, j, internal k, bases/signs for M=d_j^(k), and a stated size s with specified row/column index family.
2. A polynomial relation R in those minors, including coefficients, such that h(F)=R(minors(M(F))) is a specified polynomial, with proof it is not identically zero.
3. A global identity h(phi(B))=0 on all pencils (or an equivalent globally valid ideal-membership certificate), not a sample rank drop or “being a minor.”
4. An explicit T:C^5->C^10 and exact h((z per_3) composed with T) nonzero, separately verified; or a carefully labelled closure argument followed by a witness plan.
5. A finite verification plan and cost under SURVIVOR_SPEC.md.

S5's rank-threshold results do not automatically exclude such a relation. S1 excludes it only if the finished polynomial factors through an applicable padding-vanishing extraction. S2–S4 and S6 need their own respective data before a decision. No matrix triple is invented here; no random sampling, minor enumeration or reserved session is proposed. The >300 claim in the old row is CONJECTURAL, as corrected by B22-10, and is not used as a proved filter.

## 3. Closed control: polynomial extraction from large minors of M_7

Fix N=5, M_7=d_1^(7): C^5 tensor S_4 -> S_7, given by (a_i)->sum a_i partial_i F. With monomial bases this is a 330-by-350 matrix, linear in the 70 ordinary quartic coefficients. Define r=max_D45 rank M_7. By B24-02 section 4, a certified modular determinant-point floor gives r>=299; the elementary padding ceiling is rank M_7(P)<=245 for all P in P5. Hence rank M_7(P)<r globally on P5.

Consider the specified construction family

    h(F)=sum_(I,J) a_(I,J)(F) det M_7(F)[I,J],  |I|=|J|=r,

with finitely many coefficient-polynomial multipliers a_(I,J). S1 and Proposition C prove h|P5=0. If a separate identity also proves h in I(D45), it is still a nonseparator. No assertion that these r-minors themselves vanish on D45 is made. As a completely fixed-size version, the same conclusion holds for the entire ideal of 299-minors, since 245<299; this version does not require knowing the exact maximum r. In particular it covers polynomial expressions with zero constant term in those 299-minors. A determinant floor299 also shows at least one 299-minor is not a determinant equation, so membership cannot be inferred from its size.

**Verdict: EXCLUDED as a polynomial separator construction, globally on P5.** The floor is a historical CERTIFIED-modular input used only in the safe direction, not a fresh computation. The uniform ceiling is proved, not a padding sample. The older exact sampled padding rank244 is not substituted for the universal ceiling245. This control is nonvacuous and requires no assumption about the exact r=299 cap calculation. Rational cancellation is outside the stated family and receives no verdict of viability.
