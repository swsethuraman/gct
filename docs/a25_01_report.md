# A25-01 — no relations among the first two transverse coefficient jets

**Outcome (3): a scoped no-go theorem. LOCAL COMPLETE, UNCOMMITTED / NOT RELEASED, producer-only.** Over C, the projection of the five-variable 4x4 determinant parametrization onto the 15 ordinary quartic coefficients of transverse degree at most two has a rational section on the open set where the coefficient of x1^4 is nonzero. Those coefficients are therefore algebraically independent. No nonzero polynomial in this one framed set of jet coefficients can lie in ker(phi*), in any degree.

This closes the selected allowed-jet family. It does not close row 12, all allowed jets, fibre compatibility or combinations of different frames. No coefficient equation, actual-padding separation, positive multiplicity gap or asymptotic lower bound is produced. **0 pilots, 0 mathematical computational seconds.**

## 1. Launch, object and evidence

The live B25-12 administrative ledger registered the four permitted outcomes before launch. The launch addendum supersedes the draft's absent-ledger/manual-dispatch state only. INTAKE.md records branch, HEAD, initial status, the ownership-read failure and its safe resolution, and source provenance. The first recorded substantive checkpoint is 2026-09-21T00:45:06Z; the sole construction was frozen at 2026-09-21T00:46:10Z. The bounded assessment is complete at the checkpoint in STATUS.md, within the 45-minute gate. No second construction was pursued.

Use V=C^5, W5=Sym^4(V*), A=Sym(Sym^4 V), X=(Mat4)^5 and phi(B)=det(sum x_k B_k). Ordinary coefficients c_alpha are used throughout. Let y_i=x_(i+1). Retain a=[x1^4]F, p_i=[x1^3 y_i]F and q_ij=[x1^2 y_i y_j]F for i<=j. These give the subring R2=C[a,p_i,q_ij], with 15 generators. The frozen finite test is U_d=(R2)_d for 1<=d<=8; the theorem proves the stronger all-degree result. Every generator and the finite source space M_d, including left/right determinant character and transposition, are defined in CONSTRUCTION.md. E_d=im(phi*_d) is source-side; K_d=ker(phi*_d) is coefficient-side.

**Evidence method:** READ of pinned reports and their governing corrections; independent hand derivation of the new theorem in PROOFS.md. No REPLAY or computational INDEPENDENT EVALUATOR was run. SOURCE_BINDINGS.json records exact committed object IDs, bytes and SHA-256 for the used report/manifest blobs, with original repository bindings and current local path-history checks. Hash checks are provenance, not acceptance. No new external literature claim is made. No tool memory was created or used.

## 2. The explicit section

Choose u=(E12,E13,E14,E23) and v_i=u_i^T. Then tr(u_i u_j)=tr(v_i v_j)=0 and tr(u_i v_j)=delta_ij. For arbitrary symmetric G, D_i=u_i+(1/2)sum_j G_ij v_j satisfies tr(D_i)=0 and tr(D_i D_j)=G_ij.

Given a!=0 and arbitrary p,q, set r_i=p_i/a and

    G_ii=3r_i^2/4-2q_ii/a,
    G_ij=3r_i r_j/4-q_ij/a (i<j),
    C_i=(r_i/4)I4+D_i,
    B1=diag(a,1,1,1)=P_a,   B_(i+1)=P_a C_i.

The elementary quadratic determinant identity gives exactly the requested a,p,q. In particular the mixed coefficient is tr(C_i)tr(C_j)-tr(C_i C_j), whereas a square coefficient has the additional factor 1/2. All denominators are powers of a and rational constants. The ring composite R2 -> A -> C[X] -> R2[a^-1] is ordinary localization and is injective. Hence **K intersect R2=0 (PROVED, producer-only)**. No extension of the section to a=0, normality theorem or fibre-descent assertion is needed. The full proof includes the commutative diagram and boundary argument.

## 3. Why this is a bounded row-12 assessment

The source family is B1=P_a, B_(i+1)=P_a C_i, with 65 affine parameters. Scaling the transverse variables by t makes the selected coefficients its allowed t^0,t^1,t^2 jets. This is a relation question among allowed jets, which the old five-block forbidden-support theorem explicitly does not decide. The new section theorem kills the chosen class directly.

The six exclusions and their precise hypotheses are checked in EXCLUSION_CHECK.md. Lemmas 1.3 and 1.4, direction reversal and the five-block support theorem are outside this mechanism's stated scope. The pure-power witness check and tail theorem provide necessary checks but do not decide the full selected family. No exclusion has been silently generalized. In particular a single transformed copy of R2 is excluded, but the span/ring combining multiple frames is not.

## 4. Row 10 remains a merge, with its qualifiers

**READ context, not a premise of the new proof:** B23-02 Proposition 1.1 assumes a 3x4 matrix B of linear forms with height I3(B)=2. Hilbert–Burch gives cubic maximal-minor generators and linear syzygies, so its quartic ideal component is sum_j m_j Delta_j(B)=det[B;m] by Laplace expansion. Thus scheme-theoretic containment of a genuine member forces a determinant representation, and the closure of this family is D45. R1 has ideal exactly K. R2 (closed boundary incidence) and R3 (its fibre-dimension threshold) can yield only subideals of K and require additional boundary/elimination input. Their landing in K is not an algorithm to find an equation. This carries the source's Hilbert–Burch/grade=height **UNREAD-CLASSICAL/ADOPTED** qualification; no PRIMARY literature reading was performed here.

B23-10's correction is essential: scheme-theoretic and set-theoretic containment differ. A genuine nonreduced triple plane can lie set-theoretically in the padding hyperplane, so the set-theoretic condition holds throughout padding and is directly killed. The scheme-theoretic route instead merges into the coefficient-kernel problem. Neither reading justifies a new separator. Unrestricted degree-8 coefficient space has binom(77,8)=21,042,084,900 entries as priced in B23-02; none was constructed.

## 5. Price, achievements and next certificate

The finite space U_d has binom(d+14,14) monomials (319,770 at d=8), specified combinatorially and never expanded. The section proof uses only 15 target parameters, four 4x4 C_i matrices and a diagonal P_a, at most 40 nonzero entry positions in the five B matrices. There is no evaluation matrix, highest-weight basis or elimination job. The proof handles the entire chosen class without materializing its monomial basis.

| achievement | result |
|---|---|
| Source necessity / allowed-jet structure | Explicit allowed-jet map and section PROVED; no nonzero relation among these jets |
| Nonzero global determinant coefficient equation | **None; impossible within R2 by the theorem** |
| Nonzero evaluation on actual padding | **None; there is no nonzero h from the class** |
| Positive multiplicity gap | **Not claimed**; no representation-multiplicity calculation |
| Asymptotic lower bound | **Not claimed**; no asymptotic inference |

PADDING_STATUS.md keeps the actual-padding definition and adopted five-variable product identification separate. This proof needs neither that identification nor C45. The record's unpadded C45 remains PROVED modulo (star), with the internal reduction OPEN in B24-10; it is not a padded-det4 breakthrough.

**One next certificate:** independent verification of the 15 universal section identities. NEXT_CERTIFICATE.md prices a hand review at 20–40 minutes, or a single future wrapped exact symbolic check capped at 60 s/512 MiB with three corruption controls. No missing scientific hypothesis remains in the producer proof; this certificate is for independent review. No such check was launched. Reopening research requires a precisely specified class outside R2, such as higher jets or mixed frames; this packet does not choose or launch it.

## 6. Delivery boundary

The packet is local and uncommitted. MANIFEST.json binds report, proof, intake, scope/padding/resource records, source audit and delivery proposal; it does not hash itself. DELIVERY_NOTE.md and PROPOSED_ADD_LIST.txt name exact paths for a separately authorized delivery pass. G29 remains open until that pass supplies a delivery commit, verifies committed blobs against these reviewed bytes and records the manifest digest separately. No stage, commit, push, publication, trust/ownership change, agent or additional task was performed.
