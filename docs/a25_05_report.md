# A25-05 — multi-center second jets: a structural reduction

**Outcome (3), with containment unresolved. LOCAL COMPLETE / UNCOMMITTED / NOT RELEASED. Producer-only, pending independent review.** For three, four and five fixed independent centers, the actual retained targets have dimensions **42, 54 and 65**. Determinant relations necessarily exist at four and five centers, but this session does not prove that any is nonzero on actual padding. On a generic ordered-root chart, the five-center comparison for the full product locus reduces to containment of four explicit **affine 22-planes** in the closed image of a **33-parameter polynomial map to 48 coordinates**; its equivalence for actual padding is **conditional on C_PER**, specified below. A finite global certificate directly using actual padding is also specified, with a prohibitive general price; none was computed.

**No five-row determinant equation is known to be nonzero on padding.** No separator, positive multiplicity gap, or asymptotic lower bound is claimed. There were **zero mathematical pilots**, zero mathematical subprocess seconds, and no compute lease. There is a timing-control exception: the observed wall interval greatly exceeds 90 minutes, and substantive theory time was not instrumented, so compliance with the authorized 90-minute theory ceiling is **not verified**. Research stopped when the long interval was observed; only packet completion and administrative checks followed. See section 6.

## 1. Exact structural map

Use W=Sym^4((C^5)*), phi(B)=det(sum x_i B_i), D=closure(im phi), and P=closure{(z per3) composed with T}. All closures and dimensions are affine. For independent centers extend v_1,...,v_m to a basis. Their functional space is sum_i v_i^2 Sym^2(C^5), independent of transverse complements. In that basis retain ordinary monomials with exponent at least two in one of x1,...,xm. Pairwise overlaps are the distinct monomials xi^2 xj^2; no triple overlap occurs. This proves dim J_m=15m-binom(m,2), rather than counting 15m coordinate names.

Both determinant pencils and actual padding are stable under invertible changes of variables. Thus the canonical calculations transport to **every fixed independent center tuple**, with an invertible change in the retained target. No conclusion is made for dependent configurations or coefficient-dependent centers. [STRUCTURAL_MAP.md](../results/a25_05/STRUCTURAL_MAP.md) gives the proof and omitted bases.

Write Y_m=closure(pi_m(D)) and R=closure{l C : C an arbitrary quinary cubic}.

| m | dim J_m | dim omitted space | proved determinant-image bounds | padding comparison |
|---|---:|---:|---|---|
| 3 | 42 | 28 | 29 <= dim Y_3 <= 42; dominance OPEN | dim closure(pi_3(P)) <=35; all-P containment OPEN |
| 4 | 54 | 16 | 29 <= dim Y_4 <=50; codimension >=4 | dim closure(pi_4(P)) <=38; all-P containment OPEN |
| 5 | 65 | 5 | 29 <= dim Y_5 <=50; codimension >=15 | dim closure(pi_5(P)) <=39; decisive comparison OPEN |

The product-locus dimensions are exactly **35,38,39**, proved here. They become equalities for P **modulo C_PER**, the separate committed B13-07 rank-35 cubic-permanent certificate, which was read and byte-bound but not replayed. This optional dependency is not silently promoted to a fresh certification. The unconditional actual-padding upper bounds and explicit actual-padding control below need no product-equality premise.

The determinant upper bound is a bound on the actual image, proved using a dense explicit normal form:

    a det(x1 I4+x2 diag(lambda1,...,lambda4)+x3 C+x4 E+x5 G),
    C12=C13=C14=1.

There are fifty parameters. Density is proved by normalizing an invertible B1, diagonalizing a generic B1^-1 B2 with distinct eigenvalues, then using diagonal conjugation to fix three nonzero first-row entries of B1^-1 B3. Conversely every displayed form is an actual determinant. This is not an assumption that a symmetry count equals differential rank. The lower bound 29 follows from an independent hand check of the earlier two-center blocks, recorded in [PRIOR_CHECKS.md](../results/a25_05/PRIOR_CHECKS.md).

## 2. New padding-fiber information

For l=sum a_i xi, put r=#{i<=m:a_i!=0}. **PROVED:** the kernel of C -> pi_m(l C) has dimension

    [t^3](1+t)^(m-r)/(1-t)^(5-m).

Its cubics are independent of selected variables with ai!=0, multiaffine in selected variables with ai=0, and unrestricted in unselected variables. This follows from degree_i(l C)=degree_i(l)+degree_i(C) in a polynomial domain.

For a factor nonzero at all selected centers, the invisible cubic spaces have dimensions **4,1,0**. At five centers, injectivity already holds when l is nonzero at at least three centers. Thus a completion preserving such an l must be the original quartic. In particular a block-diagonal construction det diag(l,M3) cannot use omitted coefficients to change a generic cubic factor. This excludes that construction, not arbitrary determinant completions or projected limits.

There is also a generic full-fiber description. The binary quartic and its three first-transverse binary cubics, seventeen retained coordinates, determine at most four possible linear factors. For each possible factor the remaining cubic equations are linear. On the stated open set, the literal product-completion fiber is a union of at most four affine spaces of dimensions 4,1,0 for m=3,4,5. In particular five-center data have at most four literal product completions there. [PADDING_FIBERS.md](../results/a25_05/PADDING_FIBERS.md) and [FIVE_CENTER_REDUCTION.md](../results/a25_05/FIVE_CENTER_REDUCTION.md) give all formulas and hypotheses.

**Exact actual-padding control.** For arbitrary linear a,b,c and z=x1,d=x2,e=x3,f=x4,

    z per [a d e; d b f; e f c]
      - det diag(z,[a d e; -d b f; -e -f c])
      =2x1x2x3x4.

The right side is omitted even at five centers. Therefore this specified actual-padding family has exact determinant completions in every ring considered. In particular the integer T from A25-04, with a=x1+x5,b=x1-x5,c=x1, **cannot** witness separation in the maximal five-center ring, in any degree. This is a direct six-term hand identity, not a sampled padding inference. It is a proper family; it does not establish all-P containment.

## 3. The decisive five-center reduction

At five centers K_5 is exactly the span of the five squarefree quartics q_i=product_{j!=i}x_j. Every sum b_i q_i is itself an actual 4-by-4 determinant, by the diagonal-plus-rank-one construction in the proof. Consequently the projective projection center meets D in its entirety; closedness of the projected image cannot be inferred from a base-point-free proper map.

The correct closed set is

    pi_5^-1(Y_5)=closure(D+K_5).

A failure to represent F_T+sum b_i q_i by a literal matrix therefore does not suffice. Even membership of a literal completion in D, as opposed to im phi, would not automatically exhaust all points of the closed projection. The earlier determinant-part boundary caveat remains relevant and unresolved.

On the generic chart write t=x1,u=x2,z=(x3,x4,x5), binary quartic a product L_i with L_i=t+lambda_i u, and first-transverse cubics ell_s. Their seventeen coordinates determine every diagonal entry of the normalized pencil by

    (C_s)_ii=ell_s(-lambda_i,1)/(a product_{j!=i}(lambda_j-lambda_i)).

After the three conjugation normalizations, **33 off-diagonal parameters** remain. The remaining five-center data are **48** explicitly indexed coefficients, polynomial of degree at most four in those parameters over the seventeen-parameter function field.

Choosing which binary root belongs to the padding factor determines that entire factor and the binary and first-transverse parts of its cubic. Exactly **22 free cubic coefficients** remain. Their retained data form an affine 22-plane. The four root choices give the four planes. Full formulas, the dense-chart proof, the closure qualification, and a correct root-symmetric descent procedure are in the reduction file. In particular blindly taking a norm/product can lose padding nonvanishing; the proof instead uses all symmetric coefficients of the conjugate factors.

The **single missing scientific lemma** is whether the elimination ideal of the specified 33-parameter map vanishes identically on the specified 22-plane, or admits a certified nonzero restriction. A dimension comparison does not decide it. The exact actual-padding version is the global ideal/pullback comparison in NEXT_CERTIFICATE.md and does not require C_PER.

## 4. Where the earlier extension fails

The binary-diagonal upper-triangular Jacobian used for two centers cannot simply be enlarged to three-center dominance. At x1=x2=0 its adjugate has only the three-edge path cofactor, so the pure-transverse quartic differential lies in

    span(x3,x4,x5) * u12 u23 u34,

of dimension at most three. Three-center data require six independent pure-transverse quartics. The entire class of such base pencils therefore has differential rank at most **39<42** for that projection. This is a proved obstruction to that proof construction, not a proof that Y_3 is nondominant. No numerical pilot was spent rediscovering it.

## 5. Certificate and evidence boundary

[NEXT_CERTIFICATE.md](../results/a25_05/NEXT_CERTIFICATE.md) specifies the global fifty-parameter determinant map and fifty-parameter **actual-padding** map, their exact coefficient matrices, sparsity and bit bounds, and the kernel-inclusion test. An optional universal finite degree cap follows **modulo C_DUBE**, Dubé's Corollary 8.3, read in the primary article at statement level; the full external proof was not independently audited. The resulting general certificate is prohibitively large and is not a proposed pilot. No affordable sparse separator, global sampled-rank ceiling, or closure-aware elimination basis was identified.

This is outcome (3) because it supplies exact spaces, an actual-image upper bound, a new padding-fiber classification, a concrete actual-padding completion, a proved obstruction to the inherited Jacobian extension, and a finite missing comparison. It is **not** a claim that separation or containment has been decided. Outcome (1) and whole-P outcome (2) were not obtained. No further session or follow-on allocation is requested.

[SOURCE_READS.md](../results/a25_05/SOURCE_READS.md) records READ / hand derivation and PRIMARY / SECONDARY / UNREAD boundaries. [SOURCE_BINDINGS.json](../results/a25_05/SOURCE_BINDINGS.json) binds all 57 prior A25 manifest payloads, their four manifests, the required administrative inputs, and the committed sources actually used. Hash verification is provenance, not mathematical acceptance. No computational REPLAY or INDEPENDENT EVALUATOR was run. No tool memory was created or used as evidence.

C45 remains the unpadded n=3 control, degree 12, lambda=(19,7,2^5), D=+1, **PROVED modulo (star)**. The cap remains **PROVED modulo Kleiman (SECONDARY), Dimca (PRIMARY, statement level), and Gulliksen-Negard (SECONDARY), all named ADOPTED inputs**. Their historical literature access labels are not claimed as new primary readings here. No inherited result, paper, or gate was edited.

## 6. Resources, timing exception, and delivery

First recorded intake was 2026-09-21T04:15:25Z; the five-center mechanism was written before the 04:17:54Z checkpoint. Clock readings remained near that range through **04:26:41Z**. The next clock checkpoint returned **11:52:37Z**, a 7h25m56s interval without substantive-time instrumentation. A second clock reading and PowerShell UTC time agreed around 11:52:59Z. The interval cannot honestly be relabelled as either active theory or idle time from the available receipts. The observed intake-to-stop wall span is **7h37m12s**, exceeding the nominal ceiling if counted as theory. Thus **90-minute substantive-budget compliance is unverified, a timing-control defect**. Research stopped at that observation; subsequent work was report/source/manifest completion. No retrospective claim of an early stop within the ceiling is made.

Mathematical pilots/processes: **0**. Mathematical computational wall time: **0 seconds**. Mathematical peak memory: **not applicable**, not a measured zero. No lease was acquired or modified. Administrative PowerShell/Git/hash calls and web reading are separately disclosed. No agents, additional tasks, installation, Git staging/commit/branch change, prior-packet edit, shared-ledger edit, paper edit, message to another session, or publication occurred.

The existing repository remains on batch15-launch at **82633a60893236fab4fbc317df416e1b8a349005**, subject to the final recorded administrative check. All writes are confined to docs/a25_05_report.md, results/a25_05/, and analysis/a25_05_*. [ADD_LIST.txt](../results/a25_05/ADD_LIST.txt) lists the complete delivery footprint; [MANIFEST.json](../results/a25_05/MANIFEST.json) hashes every payload except itself, and the separate receipt hashes that manifest. All new bytes are **UNCOMMITTED / NOT RELEASED**. Byte-preserving committed delivery and independent acceptance remain separate, open steps.
