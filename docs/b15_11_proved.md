# B15-11 proof and evidence fragment

This slot supplies a decision contract and a bounded historical audit. It adds
no new positive multiplicity gap and proposes no new canonical exclusion.
Actual model for this phase: gpt-6-astra; requested reasoning xhigh.

**Claim B15-11.1 — interval decisions are sound under their listed premises.**
Status: EXACT deduction. Fix a characteristic-zero polynomial Schur cell in
one ambient coordinate ring, and closed varieties D and P in that ambient.
Write a for ambient multiplicity, m_X for coordinate multiplicity and i_X for
ideal multiplicity. Exactness of the coordinate-ring quotient in each
isotypic component gives m_X+i_X=a. Thus a valid m_X lower bound gives an i_X
upper bound, and a global i_X lower bound gives an m_X upper bound. If a
pullback carrier has dimension at most h, its image has dimension at most h.
Intersecting these inequalities gives

    U_pad = min(a, h_pad, a-i_pad_lb, other proved upper bounds).
    D_ub = U_pad-m_det_lb.
    D_lb = m_pad_lb-(a-i_det_lb).

Positive D is excluded when D_ub<=0 and established only when D_lb>0. A
sampled nullity alone never enters i_det_lb. Overlapping ideal product images
are intersected as lower bounds using max, never added without independence.
Contradictory intervals reject the entire query instead of yielding an
exclusion. Verifier: analysis/b15_11_memory.py close_intervals; strict-positive,
equality and inconsistency fixtures in analysis/b15_11_controls.py. Dependencies:
the cell's separately authorized premises. This is a proof of an implication,
not authority for arbitrary user-supplied interval inputs.

**Claim B15-11.2 — coordinate multiplication needs nonvanishing on X.**
Status: EXACT deduction. For an irreducible closed variety X over an
algebraically closed field, its coordinate ring is a domain. If the image of f
is nonzero there, multiplication by f is injective. This preserves the linear
independence of source images in the corresponding product cell. Nonzero in
the ambient polynomial ring alone does not suffice: f may belong to I(X).
GL orbit closures are irreducible, since GL is irreducible and images and
closures preserve irreducibility. The executable control evaluates
u=n!c_(n,0,...) from an integral first-variable matrix: a determinant for D,
a permanent for per3, and the independent linear factor times that permanent
for P. It rejects zero, the wrong variety, and a claimed native evaluation with
no point. The identity 4x4 matrix gives u=24 on D. This is a small nonvanishing
control in the closure; it supplies no research-cell source rank. Dependency:
an already verified source-image rank and compatible product-cell weights.
The public consumer does not accept transport flags as evidence.

**Claim B15-11.3 — four banked integral witnesses freshly replay.**
Status: REPLAYED_RANK_FLOOR. n=3, delta=8, ambient variable count9,
partition lengths8, unpadded per3 orbit closure. The partitions are
(7,5,5,2,2,1,1,1), (7,6,3,3,2,1,1,1), (8,5,3,2,2,2,1,1), and
(9,4,2,2,2,2,2,1). Each source is the integral shifted-diagram catalecticant
HWV from results/b14_10/recovered. Its matrix entries are alpha! times plain
cubic coefficients. Its rows are shifted quadratic monomials and columns are
linear variables. The explicit integral pencil reconstructs the permanent,
the matrix and its determinant. The verifier expands the HWV over Z, checks
every weight and raising derivative, and compares Bareiss and Leibniz
determinants and both house-prime residues. Each nonzero value gives
m_per3_lb=1 over Q without a modular-lifting assumption. The ambient a=1
statement remains the inherited top-cell theorem. No original missing gzip
bytes are recreated, and these cells were already closed. Verifier:
analysis/b14_10/recover.py, hash-pinned by B15-11; the new control driver calls
it and separately tests semantic mutations. This reuses B14-10's verifier and
does not claim a newly independent implementation of its algebra.

**Claim B15-11.4 — current exact deductions retain their evidence boundary.**
Status: EXACT deductions with inherited premises. The accepted LMR facts
a=274, m_det=273, m_pad>=269, i_pad>=3 give -4<=D<=-2. The reviewed tail19
bounds i_pad>=3 and i_det<=2 give D<=-1. At the tail21 degree26 cell,
a=531 and i_pad>=3 give U_pad<=528, so a valid determinant rank floor528
would suffice. For the stable family, a_inf=533 needs floor530. Those two
missing rank witnesses are not supplied here. Dependencies:
docs/batch15/ACCEPTED_STATE.md and results/b15_prep/transport_overlay.json.
The inherited CI73 completeness proof and S74 degree24 geometry are not
rerun by this slot.

**Claim B15-11.5 — audit identities.**
Status: EXACT file/count checks. The 29 compressed-MD5 discrepancies are
exactly the present paths whose s79 manifest says shipped=false. All 1,005
absent paths are uniquely enumerated and remain absent. Among the original
223 key-incomplete files, 10 S74 files receive checked source bindings and
three more receive explicit same-object key locations; 210 remain unresolved.
The 274 S74 source entries have matching native and literal cell data,
exponents and 24-power factorial scalars; their native row keys match all
eight named column files. This is structural binding, not a new polynomial
evaluation or rank replay. The operational queue is 1715-3-2=1710: three
scoped peaked exclusions and two historical record deferrals. The latter two
remain RECORDED in the portable-witness consumer. Verifier:
analysis/b15_11_audit.py. Dependencies: per-file hashes in consumed_inputs.json
and the separately pinned inputs in trusted_inputs.json.
