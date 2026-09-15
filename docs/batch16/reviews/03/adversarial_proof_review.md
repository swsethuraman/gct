# B16-12 independent receipt of slots03 and07

Both delivered mathematical claims pass adversarial proof review and bounded execution of the inspected worker receivers. These replays use the workers' verification implementations; slot12's independent contribution is the proof review, provenance checks and preserved replay. They are not new separately implemented geometric algorithms.

Original files were hash-verified before copying. Immutable intakes are `results/b16_12/intake/03` and `/07`, with source-to-snapshot bindings and full upstream input hashes in `intake_03.json` and `intake_07.json`. The intake contains23/15 delivered files respectively, with86/23 upstream hash records verified. The replay checked both sets again afterward. No original worker or intake bytes were changed. Slot03 writes only in the separate owned `results/b16_12/replay/03`; slot07 writes `results/b16_12/receiver07.json`. Snapshot and replay scripts reside in `analysis/b16_12_snapshot.py` and `analysis/b16_12_replay.py`.

## 03: global degree23 equation and actual padding nonzero

The reviewed division-free circuit is

    P=sum_(k=7..20) D_k c^(20-k) T_k,
    T7=1, T8=-2a1, T9=3a1^2-2c a2,
    T_k=-sum_(i=1..8;k-i>=7) B_i T_(k-i),
    B_i=c^i [t^(8-i)](g/c)^2.

For i1, B1=2a1; for i>=2, its formula c^(i-2) sum_(u+v=i) a_u a_v has no negative c exponent. The companion recurrence gives T_k=c^(k-7)[t7](t^k mod(g/c)^2). Thus P=c^13[t7](D_G mod(g/c)^2) on c!=0 and extends polynomially to c0. Each summand has coefficient degree10+(20-k)+(k-7)=23. Full depression has determinant one; the top coefficient of a remainder of degree at most7 is translation invariant. The normalized Hessian contributes c^-10, so this is precisely c^23 S7, with no omitted factorial or sign.

The universal torus law of D_G is alpha^2 beta^22 product(gamma_j^2) D_G(alpha t/beta). The top remainder law is alpha^9 beta^15 product(gamma_j^2), and c^13 adds alpha^52, giving (61,15,2^8). Upper root substitutions either fix the evaluation line or translate it. They preserve the top remainder and c, proving highest-weight invariance for the full polynomial, including c0 by polynomial equality. Six-zero extension supplies the16-variable highest weight. The assigned ten-variable independent padding is maintained throughout.

Global vanishing is valid: the determinant matrix-entry Hessian has rank<=8 on det4=0 by the rank-three normal form and closure. Any ten-direction pencil pullback has corank>=2 at each simple root, so its Hessian determinant is divisible by the squared line polynomial on the nonempty squarefree chart. The division-free circuit then vanishes identically in arbitrary pencil entries by density, and hence on the orbit closure. Numerical determinant zeros are controls only.

The fresh replay matches every saved certificate field, including full sparse quartic coefficients,21-node determinant interpolation, an independently differentiated source Hessian at a different complete set of21 nodes, full depression, covariance and c0 controls. It recovers

    det(L)=-248434, c=2,
    P(z per3 composed with L)=-26743148924112014067635076791795712.

This proves a nonzero equation and one nonzero padding restriction. The two Hessian arithmetic routes are independently coded inside the delivered receiver, while common exact matrix determinants use python-flint. No saved B15 raw Hessian coefficient is used. Opposite-shear and changed-D7 controls reject incorrect data. An invertible10x10 map extends by I6 to GL16.

The supplied pole bound is sufficient, not minimal; no complete finite ideal dimension follows from this one equation. It is outside an ideal generated in degree24 by grading, but the proof makes no stronger claim about every LMR mechanism or saturation. Slot02's accepted a23=189 and the full ideal upper11 imply D23<=-20 with the reviewed padding ceiling158. Equation separation therefore coexists with a negative multiplicity gap in this cell.

Resources: `b16_12_replay03_resources.json` records exit0,0.7784152 s, peak working set47,628,288 bytes and peak Job memory35,512,320 bytes. It used B15-12's Python, the unchanged inspected wrapper, one process/BLAS thread and enforced60s/512MiB. PID44408 was confirmed absent. Hashing of actual imported flint modules is saved in `replay_03_integrity.json`.

## 07: necessary degree conditions exclude both low rungs

This argument uses a special ambient family to prove necessary conditions. That use of specialization is sound: every degree-d coefficient polynomial restricts to u-degree<=d when all nonleading coefficients are linear in u and c=1. No claim that the family is dense is needed for this direction.

Highest-weight restriction to c1 and then depression is injective by homogeneity, shear invariance and the dense c!=0 chart. The essential inherited premise is that the complete stable determinant ideal at tail(21,2^7) has basis Phi=(s4 R3,s2^2 R3,s3 R2,s2 R1). Its completeness depends on the accepted stable ambient533, determinant floor529 and exact global four-space certificate; it is not proved merely by knowing four equations. Given completeness, the restriction of any finite determinant equation is a constant linear combination alpha.Phi. The coefficients alpha may be complex; the rational matrix below is invertible over C as well as Q.

The receiver independently differentiates the actual nine-variable quartic G_u, whose displayed first2x2 Hessian block and seven scalar blocks agree with direct derivatives. Exact monic division and full shear t->t-u x1 reproduce the depressed scalars and Phi functions, including all coefficients. The u-degree rows28,26,25,24 give primitive matrix

    [-1,12,-8,-6]
    [-906993,10740556,-7202184,-5397158]
    [28769891,-330695844,224156760,167800306]
    [-343406787,3755985188,-2586728520,-1934494122]

with determinant -5639493386240000. Since all these degrees exceed14 and15, any degree14/15 finite equation must have M alpha=0, hence alpha=0 and the equation is zero. The distinction is material: a special-family rank upper bound would be unsafe, but an invertible matrix of necessary vanishing constraints gives the asserted upper bound. No finite ambient533 substitution occurs.

Consequently i_det(14,(21,21,2^7))=i_det(15,(25,21,2^7))=0 under the stated complete-space premise. Nonnegativity of i_pad gives D14<=0. The further D15<=-3 uses inherited CI73's three independent degree13 reducible equations, multiplied by nonzero q44=12c0c4-3c1c3+c2^2 of degree2 and weight(4,4). The receiver verifies its raising operator vanishes and a nonzero value. Multiplication in the ambient polynomial domain preserves independence. Independent z per3 belongs to the reducible family; no nine-variable clamp on padding or equality of reducible and padding images is used.

The replay matches the whole polynomial data, raw and primitive minors, four changed-coefficient rejections and q44 controls. Resources: exit0,3.0620319 s including hashing imported SymPy modules, peak working set77,615,104 bytes and peak Job memory63,934,464 bytes;60s/512MiB, one process/BLAS thread. PID25932 was confirmed absent. SymPy1.14.0 and actual imported module hashes are in `replay_07_integrity.json`. The historical complete ideal and CI73 large computations were not rerun.

No mathematical defect or unstated new premise was found. Claims remain confined to the assigned cells; this receipt does not promote a broader onset from the same necessary test. Slots04/05/06/08 still await exact delivery.
