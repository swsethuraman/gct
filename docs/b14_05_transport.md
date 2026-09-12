# B14-05: transport, complete interpolation, and the adjunction qualification

**PROVED / CERTIFIED / CONDITIONAL, distinguished below.** Lemmas T and CI are
valid with the hypotheses stated here. Raw letter adjunction for an arbitrary
horizontal strip is **false as a map on source polynomials**. Section 5 gives an
exact counterexample in dimensions two to two, a corrected binary operator, and
the valid first-row operator in arbitrary dimension. None of these results
decides the LMR padded ideal dimension.

## 1. Common model and scope

Work over Q and extend scalars to C for varieties and representation theory.
Let V=Q^r, W=Sym^n(V*) and A=Q[W]=Sym(Sym^n V), graded by coefficient degree.
For a form f, c_alpha(f)=[s^alpha]f is an **ordinary coefficient**. The action is
fixed by

    wt(c_alpha)=alpha,
    E_ij c_alpha=(alpha_i+1)c_(alpha+e_i-e_j), if alpha_j>0, and 0 otherwise.

E acts as a derivation on A. Write M_(lambda,d)=(A_d)^hw_lambda, a=dim M;
for a homogeneous GL(V)-stable ideal I, put i_I=dim(I_d intersect M).
In characteristic zero finite-dimensional rational GL(V)-modules are semisimple;
the fixed highest-weight functor is therefore exact, and
mult_lambda(A_d/I_d)=a-i_I. This standard representation-theory fact is the
same premise used in s57 Lemma L and the indexed `fixed_factor` / `channels`.

For n=4 the relevant varieties are D_r, the closure of det_4 pencils; P_r, the
closure of l per_3 pencils; and R_r, the closure of all l c with c cubic.
They are irreducible: they are closures of polynomial images of affine parameter
spaces. P_r is contained in R_r. Their ideals are homogeneous and GL-stable.
These geometric facts, not sampled vanishing, justify the ring hypotheses below.

**Normalization.** A valence n symmetric letter is evaluated as
m_alpha=alpha! c_alpha, where alpha! is the product of factorials of its entries.
Its normalized polar tensor entry is m_alpha/n!. Column brackets are alternating
sums, with no division by a column factorial. All equal letters of one type are
evaluated on the same form. The resulting product already accounts for the
equal-letter symmetry; do not multiply by d! again. In particular
u=c_(n,0,...,0) and msym_u=n!u are distinct conventions.

## 2. Lemma T and the birth bound B

**Lemma T (PROVED).** Let 0 != w in M_(mu,k). Multiplication by w gives
injections

    M_(lambda,d) -> M_(lambda+mu,d+k),
    (I_d)^hw_lambda -> (I_(d+k))^hw_(lambda+mu)

for every homogeneous GL-stable ideal I of A. No irreducibility or nonvanishing
of w modulo I is needed for these two injections. Thus
i_I(lambda+mu,d+k)>=i_I(lambda,d).

If in addition multiplication by the residue of w is injective on A/I (for
example, I is prime and w is not in I), there is also an injection on quotient
highest-weight spaces, and

    mult_I(lambda+mu,d+k) >= mult_I(lambda,d),
    0 <= i_I(lambda+mu,d+k)-i_I(lambda,d)
       <= a(lambda+mu,d+k)-a(lambda,d).

The exact weakest quotient hypothesis for this particular statement is
injectivity on the specified quotient highest-weight space; regularity on A/I
is a convenient sufficient hypothesis. Nonzero residue alone is insufficient
in a quotient with zero divisors: multiplication by x in Q[x,y]/(xy) kills y.

*Proof.* The product of two U-fixed vectors is U-fixed, and torus weights and
degrees add. A is a domain, so multiplication by nonzero w is injective. The
ideal property preserves I. The additional quotient hypothesis supplies its
injection. Subtract the quotient dimensions from the corresponding ambient
dimensions to get the upper inequality. This proves all assertions. In
particular multiplying an actual ideal subspace of dimension p carries all p
directions injectively, not just a selected number of them. The theorem says
nothing about the ideal membership of a sampled evaluation kernel. QED.

**Lemma B (PROVED, first-row specialization).** Take w=u, mu=(n). If X is a
nonzero irreducible GL-stable cone in W, u is not identically zero on X: for a
nonzero form f there is v with f(v)!=0; a change of variables makes v the first
basis vector. Consequently

    i_X(lambda+(n),d+1) <= i_X(lambda,d)
                               + a(lambda+(n),d+1)-a(lambda,d).

Iterating gives the same inequality with the total ambient increment between
any two rungs. Equality of ambient dimensions forces equality of the ideal and
quotient dimensions at those rungs. The empty/nonzero qualification excludes
X={0}; the ideal injection in T remains valid even there. No assertion about
the generic stabilizer dimension in s57 Proposition S is needed for T or B.

**Application (PROVED, conditional only on the source equations).** In ordinary
binary quartic coefficients c_j=[s1^(4-j)s2^j]f,

    q62=8c0 c2-3c1^2,          q44=12c0 c4-3c1 c3+c2^2

are nonzero HWVs of weights (6,2) and (4,4). Direct differentiation by
E12 c_j=(5-j)c_(j-1) proves this; the other raising operators vanish after
embedding into r variables. Their Cartan products with every LMR ideal vector
are independent at (71,19,2^7)_26 and (69,21,2^7)_26 respectively. Therefore
both destination padded ideal multiplicities are at least i_pad(24). This does
not assert i_pad(24)=5 or a product-image rank of two or three. Slot 08 owns the
remaining transport census; this note does not rebuild it.

## 3. Lemma CI, including arithmetic hypotheses

**Lemma CI (PROVED).** Let M be an a-dimensional Q-vector space with a proved
basis F_1,...,F_a, and let phi:M -> N be Q-linear, where N is a finite-dimensional
space of Q-valued functions on a set Y. Require:

1. dim_Q N=h is justified (even a proved upper bound h suffices below).
2. g_1,...,g_h are genuinely in N, with exact definitions in the same rational
   model as phi and the evaluations.
3. P=(P_1,...,P_s) is an explicit list in Y and B_ij=g_i(P_j) has a nonzero
   h-by-h minor over Q.
4. Every phi(F_i) is proved to belong to N. The source matrix A_ij=phi(F_i)(P_j)
   is exact in the stated rational model; its rational rank r is proved.

Then evaluation ev_P is injective on N, ker(ev_P phi)=ker phi, and
dim ker phi=a-r. With source vectors as **rows** and points as **columns**, a
basis of relation vectors is an a-by-(a-r) matrix K of column rank a-r satisfying

    A^T K=0.

An exact r-minor of A plus this annihilation identity and the full column rank
of K proves the claimed source rank without requiring a large determinant.

*Proof.* The nonzero B minor makes the h target members independent. The
dimension bound makes them a basis. If g=sum_i t_i g_i vanishes on P, the same
minor forces t=0. Thus ev_P is injective, and composing with it preserves the
kernel of phi. The remaining assertions are rank-nullity and the displayed
matrix orientation. The case h=0 requires a proof N=0 and forces phi=0; an
empty certificate with missing dimension or membership evidence is never this
case. QED.

**Modular minor (PROVED qualification).** A nonzero B minor modulo a prime p
proves a nonzero rational minor only when all evaluated entries and transformations
come from a common Z localized away from p, with their denominators verified
prime to p. Recorded rational row or column scalings must be applied consistently;
ones claimed invertible modulo p must also have unit numerators. Multiplying by
a documented common denominator gives an alternative integral model. Each house
prime, 2147483647 and 2147483629, is checked in this session. This is a rank floor
over Q. Rank deficiency modulo either or both primes is not a rational rank
ceiling. An integer reconstruction of residues is exact only with a proved
absolute entry bound H, signed CRT modulus M>2H, and the required source
arithmetic checks; agreement at two primes by itself is not such a proof.

**Reducible pullback (PROVED, consistent with `fixed_factor`).** For n=4 let
Y=V* x Sym^3(V*) and mu(l,c)=lc. Then

    N_d=(Sym^d V tensor Sym^d(Sym^3 V))^hw_(lambda_d),
    phi(F)=F(lc),     phi(c_alpha)=sum_(i:alpha_i>0) l_i c_(alpha-e_i).

The map is equivariant, of bidegree (d,d), and its kernel on M is
I(R_r) intersect M because R_r is the closure of the image of mu. Over Q this
is a polynomial identity assertion, equivalent after extension to C. Thus CI
gives **i_red=a-rank_Q A**, if its premises are supplied. It does not give i_pad
unless a separate equality of the two ideals in that component is established.

If only an a'-dimensional source subspace has been justified, CI gives its
intersection dimension, not the full ideal multiplicity. A deficient source
matrix without a complete target gives only an upper bound on ideal nullity.
This note supplies neither the 73/159 target minors nor the 39/93-row exact
LMR source matrices. The abstract fixture in controls.json has N=Q[t]_(<=1),
phi(y0,y1,y2)=(1,t,2t), rank two and relation y2-2y1; it exercises the theorem
and rejects invalid inputs, but is not an LMR certificate.

## 4. Mixed brackets at both degrees

**Definition (PROVED membership convention).** For lambda partitioning 4d,
take its columns with heights lambda'. Fill the boxes with distinct formal
letters L_1,...,L_d of valence one and C_1,...,C_d of valence three. Each L occurs
once; each C occurs three times. For each column independently permute the
indices 1,...,height, multiply its permutation sign, then multiply the letter
values

    L_i(index j)=l_j,
    C_i(indices with multiplicities beta)=beta! c_beta.

Sum over all column permutations. Row order fixes the signs. A column containing
two occurrences of one symmetric letter gives zero, so it may be discarded.
After all L copies become the same l, two distinct L letters in one column
also give zero. These discarded zero fillings add no spanning directions.

Every such polynomial has bidegree (d,d), weight lambda, and all raising
operators zero. Indeed each initial wedge e1 wedge ... wedge eh is U-fixed
and has torus weight (1^h); their weights sum to lambda. Pairing with the letter
tensors preserves that statement. A polynomial may be zero; membership does
not assert nonzeroness or independence.

**Spanning (PROVED using characteristic-zero Schur-Weyl duality).** The
permutations of the tensor product of the initial column wedges span the
highest-weight weight-lambda subspace of V^(tensor 4d). Project equivariantly
onto Sym^d V tensor Sym^d(Sym^3 V) by separately symmetrizing the d linear slots,
the three slots of each cubic block, and the d cubic blocks. The two letter
types are never exchanged. The normalized symmetrizer has denominator
(d!)^2(3!)^d. Exactness of the highest-weight functor makes the projected
spanning set span all of N_d. Pairing on repeated l,c tensors makes the group
averages implicit and gives exactly the mixed polynomials above, up to the
common nonzero factor (3!)^d from the cubic m convention. Thus **all** these
fillings span. This is not a claim that an arbitrary sampled or partially
enumerated subset spans, nor that row/column conditions supply a plethysm basis.
One can instead use the standard semistandard spanning family in the formal
letter model (fixed content 1^d,3^d and a fixed total order) before coalescing
equal types; a bounded partial pass still has to exhibit a full rank minor.

The exact parameter spaces are:

| d | r | row shape lambda_d | column heights | source a, recorded | dim N_d, recorded |
|---|---|---|---|---:|---:|
| 13 | >=9 | (21,17,2^7) | (9,9,2^15,1^4) | 39 | 73 |
| 14 | >=9 | (25,17,2^7) | (9,9,2^15,1^8) | 93 | 159 |

There are d linear and d cubic letters, hence 4d boxes at each degree. The
dimension formula, as a characteristic-zero representation identity, is

    dim N_d = sum_(eta partitioning 3d, lambda_d/eta horizontal d-strip)
                         [s_eta] h_d[h_3],

where eta is padded with zeros to r entries and the strip condition is
lambda_i>=eta_i>=lambda_(i+1). These numerical dimensions are **RECORDED / ADOPTED
inputs** here. The frozen board records two counting routes agreeing; slot 04
owns their formalized independent recount. This session proves the target
identification and spanning theorem, not a fresh 73/159 recount. To apply CI
at r=9, justify the dimension and exhibit 73 or 159 independent members at the
matching points. An N13 minor cannot certify N14.

**Exact source-to-target normalization (PROVED).** On one quartic tensor,

    mu*(m4_alpha)=alpha! sum_i l_i c_(alpha-e_i)
                 =sum_i alpha_i l_i m3_(alpha-e_i).

The last sum is the sum over the four individual tensor slots: designate one
slot linear and the other three cubic. Therefore the pullback of a degree-d
quartic bracket is the sum over **4^d slot choices** of mixed brackets, with
no extra factor 1/4^d in the m convention. Coincident terms retain their
multiplicities. This gives source inclusion constructively and fixes the
relative normalization without Pieri coefficients. At d=2 the checker compares
all 16 choices to ordinary coefficient substitution and rejects division by 16.
The formula is for proof and conversion semantics; it is not an instruction
to expand 4^13 or 4^14 terms on the shared host.

**Source ladder values.** The banked native row born at t becomes a degree-d
row as F_native*(24u)^(d-t), with u(lc)=l1*c_(3,0,...,0). State beside a stored
matrix whether these are literal values or ones divided by 24^(d-t), and
recompute u from the stored l and cubic exponent ordering. A transported
evaluation certificate must carry its points and u-values, all nonzero at
columns used for transport. Changing row scalings changes kernel coefficients.
Mixed target rows have their own (3!)^d convention; matching scalar choices
between different basis rows is unnecessary for CI provided their definitions,
memberships and actual evaluations are consistent in the same rational model.

## 5. Adjunction: counterexample, correction, and precise limit

**Counterexample (PROVED, exact certificate).** For binary quartics put
H=8c0c2-3c1^2. Use source lambda=(12,4), d=4. Write a two-column as its ordered
letter pair and a singleton as its letter. Let the pair columns in both T,U be

    (0,1), (0,1), (2,3), (2,3).

Their eight singleton columns, respectively, are

    T: 0,0,1,1,2,2,3,3;
    U: 0,2,0,1,1,2,3,3.

Each letter has valence four. Singleton order is irrelevant to the original
polynomial, so F_T=F_U=576 H^2, a nonzero source polynomial. Adjoin new letter 4
in the fixed horizontal strip nu/lambda for nu=(14,6): extend columns 5 and 6
downward and add new singleton columns 13 and 14. At f=s1^4+s1*s2^3, namely
(c0,c1,c2,c3,c4)=(1,0,0,1,0), literal alternating expansion gives

    F_(T')=0,       F_(U')=497664.

This value can also be checked without a polynomial engine. At this f a letter
is nonzero only with zero or three index-2 legs, contributing 24 or 6 respectively.
In T', letters 1 and 4 have at most two index-2 legs, so both must have none;
their four edges force letter 0 to have four, giving zero. In U', letters 1,3,4
must have none, forcing letters 0 and 2 to have three each. There is exactly
one surviving column assignment, with positive sign, and value 6^2*24^3=497664.

The complete seven-term difference polynomial and both fillings are in
results/b14_05/controls.json. Since equal source vectors have unequal images,
**there exists no linear operator Phi_nu on source polynomials satisfying the
raw formula for all fillings**. Both images separately remain highest-weight
members of the target; highest-weight membership cannot test this defect.

This is a multidimensional case: binary quartic weight multiplicity at (4d-b,b)
is the number of multisets of d indices in {0,...,4} summing to b, minus the
number summing to b-1. This follows by subtracting the consecutive weight
spaces in the sl2 decomposition. At (d,b)=(4,4) and (5,6) the differences are
5-3=2 and 8-6=2. The exact code enumerates these tiny spaces. A second source
diagram, four copies of pair (0,1) followed by four singleton 2's and four
singleton 3's, equals 55296 c0^2(12c0c4-3c1c3+c2^2); together with F_T it has
coefficient rank two. Thus neither a dimension-one caveat nor a scalar
normalization alone resolves the counterexample.

**Corrected binary adjunction (PROVED).** Let n be the inner degree, F a binary
HWV of weight (a,b), m=a-b, and 0<=k<=min(n,m). The horizontal n-strip with k
new boxes in the second row has nu=(a+n-k,b+k). Put D=E21 and

    Psi_k(F)=sum_(i=0)^k (-1)^i (n-k+1)^(rising i)
                      / (i! m^(falling i)) * (D^i F) c_(k-i).

Empty products equal one. This fixes the coefficient of F tensor c_k in the
Pieri highest-weight tensor to one. It is a linear, representative-independent
operator into the target HWV space, possibly with kernel; it preserves every
GL-stable ideal. It is polynomial multiplication **after** the normalized
Pieri tensor construction, rather than multiplication by one coefficient.

*Proof.* sl2 gives E12 D^i F=i(m-i+1)D^(i-1)F. In the tensor product the raising
equations for successive coefficients a_i are

    a_(i+1)(i+1)(m-i)+a_i(n-k+1+i)=0,   a_0=1.

The displayed coefficients solve them. Weights add to nu. Multiplication
commutes with the action. If F lies in a GL-stable ideal then every D^i F does
as well, so each product lies in it. This also proves representative independence.

For a binary source filling there are m singleton slots. Average the literal
extensions over all binomial(m,k) choices of singleton slots to extend. In the
expansion choose i of these slots to swap. Each i-subset occurs in
binomial(m-i,k-i) chosen k-subsets. D kills each two-column wedge and acts only
on singleton e1 slots; hence the sum of the source tensors with i distinct
singleton slots changed to e2 is D^i F/i!. The new letter contributes
(n-k+i)!(k-i)! c_(k-i). Combining these factors gives

    average_raw_extensions(F)=(n-k)! k! Psi_k(F).

Thus the average descends even though each raw extension need not. QED.

**Validation (CERTIFIED).** At n=4,m=8,k=2 the operator is

    Psi_2(F)=F c2-(3/8)(DF)c1+(3/28)(D^2 F)c0.

The average of all 28 literal extensions equals 4 Psi_2(F), checked coefficient
by coefficient for both source basis vectors. Both images have rank two over Q
and at both house primes. The basis change [[1,2],[3,5]], determinant -1, is
applied before the operator and independently to its images; the complete
polynomials agree. An unchanged target basis and a missing factor four are
both rejected. All denominators are explicitly checked before modular ranks.

**Arbitrary r, first-row case (PROVED and CERTIFIED on banked coordinates).**
When the strip adds n singleton columns in row one, the new letter always has
index 1, so

    F_(T')=n!u F_T.

This gives the genuine linear operator in the literal m convention; division
by n! gives multiplication by u. At n=3 the six integral s69 source coordinate
rows at (19,7,2^5)_12 and the six independently selected target rows at
(22,7,2^5)_13 give the exact matrix identity J(S)=C T, J=6u, with

    C = [  1/21,  1,    8/21,     0,    5,   0  ]
        [  1/42,  0,    1/42,     0,    0,   0  ]
        [ -1/126,-1/6, -17/84,    7/2,  0,   0  ]
        [  0,     0,   10,        0,    0,   0  ]
        [  1/42,  1/2,-11/28,   -21/2,  0,   1/2]
        [  0,     0,    7/6,      0,   -1,   0  ],
    det C=5/12.

All 103836 target coordinates were compared over Q. Exact minors certify rank
six for both supplied coordinate matrices; their reductions also have rank six
at both primes. The independent target basis exercises mixing between many
directions. The integer identity

    66 S0-972 S1+12 S2-37 S3+4 S4+320 S5=-29859840 v_s62

is rechecked at all 17047 source coordinates, and u*v_s62 equals the banked s73
degree-13 integer vector exactly. Coordinate orbit representatives and signs,
including the resolved exponent tuple for u, are used instead of assuming
equal coordinate indices between degrees. Multiplication by u commutes with
the tail stabilizer; adding its fixed monomial preserves the lexicographically
least orbit representative and the character. This justifies the coordinate
map used in the replay.

**Evidence boundary.** s69's expensive filling-to-coordinate expansions and
s73's ambient upper counts of six are adopted. This session replays exact
identities of those integer matrices, not their original expansions or the
large raising matrices. The rank minors alone prove at least six independent
supplied coordinate directions. The polynomial first-row theorem is proved
independently of this data. Ideal membership of the n=3 line continues to rely
on the LMR theorem and the inherited exact rank argument, not newly sampled
vanishing. This first-row validation does not validate any other strip.

**General non-Cartan replacement (defined, implementation OPEN).** Fix the
irreducible module S_lambda with a normalized highest vector v_lambda. Choose
the nonzero highest-weight vector h_nu in the multiplicity-one Pieri component
of S_lambda tensor Sym^n V, and state its scalar normalization. For each
F in M_lambda there is a unique GL-intertwiner i_F:S_lambda -> A_d carrying
v_lambda to F. Define

    Phi_nu(F)=multiply((i_F tensor id)(h_nu)).

This is well-defined, linear, and ideal-preserving. It can be zero; a Pieri
constituent in the tensor domain need not survive multiplication. Implementing
it requires the actual coupled tensor (equivalently, an appropriate sum of
lowering operators or straightened averaged fillings), with compatible
normalization. A horizontal strip alone specifies neither that normalization
nor a raw-filling-independent map. The exact unresolved higher-rank task is
to construct and validate these coupled operators for the non-Cartan n=4
strips, including height-three and unequal tall columns. Raw extension cannot
serve as their implementation. This is the substantive fallback to the false
unqualified adjunction request, not a resource-based absence of evidence.

## 6. Implications for the frozen LMR boundary

**ADOPTED:** a24=274, determinant rank 273, padded rank at least 269, so
D=1-i_pad(24) lies in [-4,+1]. **CONDITIONAL:** a completed CI certificate with
i_red(13)>=1 gives i_pad(24)>=1 by ideal containment and multiplication by u^11,
hence D<=0. A completed certificate with i_red(14)=5 gives i_pad(24)>=5 by u^10;
the adopted padded rank floor gives i_pad(24)<=5, hence D=-4 exactly.

Neither antecedent is supplied here. Lemma T applies to genuine equations,
and corrected adjunction preserves genuine ideals; neither turns the five
sampled kernel vectors into equations. The adjunction counterexample leaves
the separate mixed-target interpolation approach intact: that approach uses
membership plus spanning, not a non-Cartan product operator.
