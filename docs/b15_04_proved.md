# B15-04 proof fragment

Model: gpt-6-astra. Banked input mathematics and implementations retain original attribution. This is a per-slot record; it does not amend the shared theorem index.

## Exact dimensions and sufficient inequalities

Claim: for n=4, delta=8, ambient dimension 16 and labels (11,11,5,2,1,1,1) and (12,11,4,2,1,1,1), the ambient multiplicities are respectively 4 and 3. The linear-times-cubic pullback dimensions are both 3. The signed stabilizer carriers have dimensions 70,438 and 85,325, with raw weight counts 1,577,460 and 986,119.

Status: EXACT combinatorial computation, freshly checked in results/b15_04/sizing.json. Verifier: analysis/b15_04_panel.py sizing. Dependencies: the banked Murnaghan-Nakayama and power-sum plethysm implementation, Pieri interlacing for the pullback, and character-twisted Burnside counting. Direct orbit enumeration on small examples checks the signed Burnside implementation; ambient and pullback recounts agree with the supplied inventory.

Hypotheses for the geometric bound: Pad is the closure of the GL(16) orbit of the quartic z per_3 on ten independent essential variables, and Det is the corresponding determinant orbit closure. Pullback along multiplication of a linear form and a cubic gives m_pad <= h_pad. Thus U_pad=min(a,h_pad,a-L_pad)=3 with the trivial valid L_pad=0. No scoped exclusion or transport-overlay entry matches either assigned label. Rank_det >=3 suffices for D=m_pad-m_det<=0. For D>0, the first cell needs global i_det>=2 and rank_pad>=3; the second needs global i_det>=1 and rank_pad>=3. This fragment does not assert any such research rank or global determinant equation.

## Ordinary coefficient convention

Claim: the inherited raising/evaluation pipeline uses ordinary coefficient functionals c_alpha with E_(i,i+1)c_alpha=(alpha_i+1)c_(alpha+e_i-e_(i+1)). Each orbit column is an integral signed sum of products of these c_alpha. Factorial-scaled coordinates require conjugating the raising matrix and are not substituted into this evaluator.

Status: EXACT on the exported control and directly checked against the input implementation. The two-term integral source of weight (6,2), degree 2, is 3 c_(3,1)^2 - 8 c_(2,2)c_(4,0). Applying the raising operator gives 24 c_(3,1)c_(4,0)-24 c_(3,1)c_(4,0)=0. The explicit determinant pencil in results/b15_04/controls.json gives value -1597. The source vanishes on every fourth power: its two terms evaluate as 3(4a^3b)^2-8(6a^2b^2)(a^4)=0. The source is integral, so either nonzero house-prime residue also proves a rational rank floor one for this control cell.

Verifier: analysis/b15_04_panel.py controls. Independent checks use the uncompressed raising implementation and FLINT integer determinants on five separating binary-quartic points (1,t), t=0,...,4. Separate mutations alter a point coefficient, a source sign, and the factorial normalization. Ten-column padded frames are also checked against a direct permanent sum. These are liveness and defect controls, not rank claims for either degree-eight cell.

## Rational lifting gate

Claim: let E be an integer m by n matrix with dim_Q ker E=a. If rank_Fp E=n-a, then every vector in ker_Fp E lifts to an element of ker_(Z_(p)) E. A nonzero evaluation minor on such vectors at integer points is therefore a valid rational rank floor.

Proof: rank_Fp E=n-a exhibits an (n-a)-square minor whose determinant is a unit in Z_(p). Reorder its rows and columns to the leading block A. Write those rows as (A B). Given any free coordinate vector y over Z_(p), set x=-A^(-1)By. All other equations vanish because the full rational rank is n-a. Reducing this parametrization modulo p gives the full finite-field kernel and any prescribed vector in it. Polynomial evaluation is Z_(p)-linear in source coordinates and reduces compatibly, so an evaluation minor nonzero modulo p is nonzero over Q.

Status: EXACT deduction. To apply it to a computed kernel, certify both sides of the rank equality. A triangular cover of size nS and a projected Schur matrix of rank nU-a supply rank_Fp E>=n-a; a verified full kernel of dimension a supplies the converse. Merely checking E K=0 on a columns does not supply the necessary lower bound. Dependencies for the geometric application additionally include the exact source construction and characteristic-zero multiplicity a. No research-cell modular kernel is certified by this lemma alone.
