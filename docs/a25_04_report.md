# A25-04 — a scoped no-go for bordered Jacobian minors

**Outcome (3): PROVED scoped no-go, producer-only. LOCAL COMPLETE / UNCOMMITTED / NOT RELEASED.** Ten specified bordered 2-by-2 minors of the five-variable degree-three Jacobian matrix take arbitrary values on 4-by-4 determinant pencils. Consequently no nonzero polynomial in those ten minors is a global determinant equation. This closes the chosen trace-pairing mechanism; it does not close row 3 in general.

The exact candidate h0=det(m_ij) is nonzero on actual padding, with value -4096 at an explicit integer substitution, but also nonzero on an explicit determinant pencil, with value 256. It therefore **fails determinant membership**. The stronger polynomial-section theorem rules out repairing it by another polynomial in the same ten minors. There is no separating equation, positive multiplicity gap, or asymptotic bound. **Zero pilots; zero mathematical computational seconds.**

## Exact selected object and result

Over C use ordinary quartic coefficients and phi(B)=det(sum_(l=1..5) x_l B_l). Set N=5, j=1, k=3. The matrix M=d_1^(3): C^5 -> S_3 has 35 monomial rows and 5 derivative columns, with entry M_(beta,l)=(beta_l+1)c_(beta+e_l). Signs, order, domain and codomain are fixed in [CONSTRUCTION_AND_PROOF.md](../results/a25_04/CONSTRUCTION_AND_PROOF.md), section 1.

Writing the first three x1-layers as a x1^4+x1^3 sum p_i y_i+x1^2 sum_(i<=j) q_ij y_i y_j, with y_i=x_(i+1), select rows (x1^3,x1^2 y_i) and columns (1,j+1), for 1<=i<=j<=4. These ten minors are

    m_ii=8a q_ii-3p_i^2,    m_ij=4a q_ij-3p_i p_j (i<j).

Set m_ji=m_ij and h0=det(m). This is one explicitly specified polynomial R in the selected smaller minors, of coefficient degree 8.

The determinant-specific factorization is globally

    m_ij(phi(B))=-4 tr(W_i W_j),
    W_i=adj(B1)B_(i+1)-(tr(adj(B1)B_(i+1))/4)I4.

It follows first by expanding the determinant to transverse degree two on det B1!=0, and then everywhere because both sides are polynomials in all 80 pencil entries. Thus the formula is not an auxiliary-coordinate relation mistakenly assumed to descend; its coefficient translation is explicitly proved. It supplies no rank restriction on the Gram matrix of four traceless 4-by-4 matrices.

To prove that rigorously, take u=(E12,E13,E14,E23), v_i=u_i^T. Direct multiplication gives tr(u_i u_j)=tr(v_i v_j)=0 and tr(u_i v_j)=delta_ij. For an arbitrary symmetric 4-by-4 t, set

    B1=I4,    B_(i+1)=u_i-(1/8)sum_j t_ij v_j.

Then m_ij(phi(B(t)))=t_ij. This is a **polynomial section**, with only constant denominators, and proves

    I(D45) intersect C[m_11,m_12,...,m_44] = {0}.

Every step is re-derived in the proof file. The overlapping A25-01 two-jet result was read as provisional context; no unreviewed lemma is required as a premise. This is a direct row-3 specialization of that elementary idea, not a claimed new general classification.

## Three rejection tests and achievement distinctions

| Check | Exact disposition |
|---|---|
| Ambient nonzero | h0 is nonzero, witnessed already by the determinant control below. The ten minors are algebraically independent on ambient quartics. |
| Global determinant identity | **REJECTED for h0:** choose B1=I4 and B_(i+1)=u_i+v_i/2. Then m=-4I4 and h0=256. More strongly, no nonzero R in the same ten generators can vanish on all pencils. |
| Actual padding | **PROVED nonzero for h0:** z=x1 and permanent matrix [[x1+x5,x2,x3],[x2,x1-x5,x4],[x3,x4,x1]] give m=diag(8,8,8,-8), h0=-4096. The full 10-by-5 T and six-term expansion are in proof section 4. This nonvanishing is not separation because the preceding condition fails. |
| Universality | The bordered-minor formula h0=(4a)^3 det L holds for every such block L, so subtracting its two sides yields the zero coefficient polynomial. It is not a determinant-specific obstruction. |
| Actual rank scope | Both explicit controls have rank M=5, the column maximum. Hence r_D=r_P=r_ambient=5 for this matrix. Size 2 is smaller than the determinant maximum. No M7 rank bound was transferred here. |

[EXCLUSION_AUDIT.md](../results/a25_04/EXCLUSION_AUDIT.md) checks all six inherited exclusions with their hypotheses. In particular h0 belongs to the 5-minor ideal by the universal bordered-minor formula, but the strict padding-rank deficit required by Lemma 1.3 is absent at the displayed padding point. The separate M7 control keeps its actual N=5,j=1,k=7 scope, uniform padding ceiling 245 and historical CERTIFIED-modular determinant floor 299; its entire 299-minor ideal remains padding-blind.

No invariant/cubic covariant or old five-block source tests are used. The pure-power consistency check passes. The candidate's weight is (24,2,2,2,2), with tail equal to coefficient degree 8; this is a weight calculation, not a highest-weight or multiplicity claim. No cell is nominated.

## Boundaries, evidence and next certificate

The theorem concerns polynomials in the ten selected minors in one fixed frame. It applies to any single fixed change of frame, but not a mixture of frames, other row selections, arbitrary coefficient multipliers, higher gradings, all adjugate identities, or row 3 as a whole. No rational cancellation/saturation construction is proposed. The mechanism is closed; no second route or follow-on allocation is requested.

Evidence: **READ of pinned committed reports/reviews and provisional A25 packets; self-contained hand derivation of the stated theorem and controls.** No REPLAY or computational INDEPENDENT EVALUATOR was run, and this producer work is not independent downstream acceptance. [SOURCE_READS.md](../results/a25_04/SOURCE_READS.md) records use-specific PRIMARY/SECONDARY/UNREAD statuses and exact sections. [SOURCE_BINDINGS.json](../results/a25_04/SOURCE_BINDINGS.json) freshly binds 16 committed blobs, both provisional manifests and all 29 A25-01/02 manifest payloads, plus the administrative launch inputs. Hashes are integrity evidence, not theorem acceptance.

C45 remains the unpadded n=3 control, PROVED modulo (star). The cap retains its named ADOPTED-input qualifications. No external source status is promoted by this packet. No tool memory was created or consumed as evidence; no unfinished A25-03 or new Claude output was read.

**One next certificate:** independent hand review of the ten section identities, the global polynomial extension and the two exact controls. This is a bounded 20–40 minute review of four 4-by-4 matrices and a six-term permanent, with no dense pullback or numerical experiment; the price and checks are in [RESOURCE_RECEIPTS.md](../results/a25_04/RESOURCE_RECEIPTS.md). No missing scientific lemma remains in this producer proof. Delivery and independent acceptance remain open.

## Local delivery

The repository remained on batch15-launch at 82633a60893236fab4fbc317df416e1b8a349005. Selection started at 2026-09-21T03:27:11Z and the mechanism was frozen by 03:29:36Z, within the 45-minute/half-session gate; the proof outcome was fixed by 03:33:27Z. Only this slot's paths were written. No shared lease was acquired, no mathematical pilot ran, and no Git mutation, paper edit, agent, extra task or publication occurred.

[MANIFEST.json](../results/a25_04/MANIFEST.json) lists all actual packet files and their **UNCOMMITTED** raw-byte hashes, excluding itself. [ADD_LIST.txt](../results/a25_04/ADD_LIST.txt) gives the exact proposed delivery paths; [DELIVERY_NOTE.md](../results/a25_04/DELIVERY_NOTE.md) records the downstream boundary and byte-filter checks. There is no delivery commit. A separately authorized pass must bind reviewed bytes to committed objects before downstream acceptance; no historical seal or other producer's file was changed.
