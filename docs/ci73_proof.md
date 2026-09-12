# Degree-13 complete interpolation: definitions and proof

The certificate concerns Q, n=4, r=9, degree 13, and
lambda=(21,17,2,2,2,2,2,2,2). Its acceptance path is
`tools/verify/verify.py` → `tools/verify/ci73.py`. All mathematical inputs are
relative references below `results/ci73`, with checked canonical JSON digests.
No producer, integrator helper, sampled-rank dimension oracle, or stored DP
output is imported by that path.

## 1. Actual polynomials and highest weight

Use the positive coefficient weight convention. For a homogeneous form f,
c_alpha(f) is its ordinary coefficient and m_alpha(f)=alpha! c_alpha(f), where
alpha! is the product of the coordinate factorials. A valence-n letter with
assigned row multiset alpha contributes m_alpha. This is n! times the normalized
polar tensor entry, hence an equivariant linear evaluation of that letter.
Equal letters of a type are evaluated on the same form; there is no additional
degree factorial, orbit averaging, or division by column factorials.

For each listed ordered column (t_0,...,t_(h-1)), sum over all permutations pi of
0,...,h-1 with coefficient sign(pi), assigning row pi(j) to letter t_j. Multiply
these column signs and the letter contributions, and sum. A singleton assigns
row 0. This finite Leibniz formula defines every source and mixed bracket,
including fillings whose resulting polynomial might be zero.

Each initial-column bracket is a highest-weight vector: upper unipotent row
operations leave its determinant invariant, and its torus weight is
epsilon_1+...+epsilon_h. Products remain highest weight; the equivariant letter
evaluation preserves this property. Thus two height-nine columns, fifteen
height-two columns, and four singletons give weight (21,17,2^7).

The first 39 S74 entries are checked individually. Two have native degree 12
and weight (17,17,2^7); 37 have native degree 13. Define

    u(f) = m_(4,0^8)(f) = 24 c_(4,0^8)(f),
    F_i^up13 = u^(13-d_i) F_i^native.

The verifier constructs this product by appending four singleton occurrences
of each new valence-four letter. Every degree-13 filling has thirteen
valence-four letters and exactly the column shape just stated. It checks the
source key, native degree and weight, and the separate literal degree-24
transport. It does not evaluate degree-24 literal data as a degree-13 source.

Mixed members have thirteen valence-one letters evaluated on ell and thirteen
valence-three letters evaluated on c. They are highest weight of bidegree
(13,13), hence lie in

    N13 = HW_lambda(Sym^13 V tensor Sym^13(Sym^3 V)).

The remaining member is the pullback F_15^native(ell*c), with zero-based index
15, native degree 13. Multiplication (ell,c) → ell*c is equivariant and its
pullback has bidegree (13,13), so this member also belongs to N13. Its membership
uses its source definition, not any kernel equation. The schema also permits
other verified source pullbacks; any proposed replacement must pass fresh value
and full target minor checks.
For such a reference, `basis: native_unscaled` selects the validated native
representation with its registered transport to degree 13 and without the
optional rational source-row scale. Source 15 needs no transport.

## 2. Dimensions independent of point ranks

The verifier implements exact Newton recurrence in the power-sum basis:

    d h_d[h_n] = sum_(r=1)^d p_r[h_n] h_(d-r)[h_n],
    p_r[h_n] = sum_(sigma partition of n) p_(r sigma) / z_sigma.

Murnaghan–Nakayama characters are computed recursively by legal connected
outer-rim removals, with sign (-1)^(number of occupied rows minus 1). Small
character tables satisfy hook dimensions and full character orthogonality for
sizes 1 through 7. The source calculation pairs the full h13[h4] expansion
with chi_(21,17,2^7), giving 39. Every one of the 31,573 saved power classes is
compared with the freshly generated rational expansion.

Pieri's rule gives the target dimension by summing coefficients of s_mu in
h13[h3] over every mu for which lambda/mu is a horizontal 13-strip. Independent
bounded-composition recursion enumerates all interlacing mu of size 39; exactly
15 occur. Every coefficient of the 5,586-class h13[h3] expansion is freshly
computed over Q and by modular Newton recurrence at both house primes. All 15
character sums are recomputed; their sum is 73. Stored status fields and prior
dimension expectations do not discharge these checks.

## 3. Polynomial evaluation algorithm

`ci73_backend.cs` is a new implementation of the defining Leibniz sum. Processing
one letter at a time, its state records the row subsets already used in each
tall column and the row assignment at the first endpoint of each open
two-column. A transition chooses an unused row for each tall-column occurrence
and each newly opened two-column bit. At a closing endpoint, the row is forced
to the complementary bit. The letter's factorial symbol multiplies the state.

Tall-column inversions are counted as each row is appended in processing order;
the final permutation from processing order to the listed column order supplies
the remaining sign. A two-column pays its sign at opening, using its first
listed endpoint's row bit. Closed columns disappear from the frontier. By
induction, each state sums exactly all partial Leibniz assignments with that
boundary data; the final single state is the polynomial value.

The Python planner uses a full subset optimization for 13 letters and a
deterministic beam for 26. Ordering affects cost only. The backend does not
reuse either producer's evaluator or their state representation. Literal
Cartesian-product reference controls compare 192 values/residues on mixed
small shapes spanning three independent directions, in addition to eight
quartic controls and the delivered independent exact source15 sample.

Modular arithmetic uses signed 64-bit temporaries; p<=2^31-1 makes products
and each reduced accumulation safe. Exact source evaluation uses eight uint32
limbs in Z/(2^256), with signed multiply-add implemented explicitly. Tensor
coefficients have absolute value below 2^30, so all limb temporaries fit int64.
The final signed reconstruction is exact by the independently checked bound
below; intermediate overflow in this ring is intentional and harmless.

No value cache on disk can grant acceptance. Adversarial tests may retain only
values freshly computed in their own live process, keyed by the complete
filling, coefficient/exponent data and modulus. Changed definitions force new
evaluation. Standalone verifier invocations always begin with an empty cache.

## 4. Points, integer reconstruction and witness scope

P13 contains 96 primary and 20 holdout points, with explicit IDs, roles, linear
coefficients and all 165 cubic ordinary coefficients. The verifier reconstructs

    c_alpha(ell*c) = sum_(i: alpha_i>0) ell_i c_(alpha-e_i)(c)

in all 495 quartic coordinates, applies alpha!, and checks the stored u and
maximum-symbol tags. All integer input coefficients have absolute value <=7.
Enumerating the quartic exponent vectors establishes

    alpha! * |support(alpha)| * 7^2 <= 24*49 = 1176.

Each source summand is a product of thirteen such symbols. Its two tall
columns and fifteen two-columns have at most (9!)^2 2^15 terms. Consequently

    H = (9!)^2 2^15 1176^13
      = 35503501195553840281013485855286379513864748625244979200.

H<2^255 proves uniqueness of the signed exact result from the 256-bit ring.
The seven listed primes are checked by trial division, and their product is

    210624540280123215664455028101579518916489513913592524753702238459 > 2H.

Every one of the 39×73 source values on primary indices 0,...,72 is freshly
evaluated exactly, compared with the certificate and original integer matrix,
reduced against all seven actual residue blocks, and recovered by signed CRT.
All 72×73 mixed values are freshly evaluated at both house primes; the 73rd
target row uses the already freshly evaluated source row. The full 73×73
target minors use explicitly recorded row/column order. A nonzero modular
minor in this integral model proves nonzero determinant over Q.

The remaining 23 primary columns are checked only for stored integer/residue
consistency, not freshly evaluated and not needed by CI. All 39 sources are
freshly evaluated on all 20 holdouts, and all 60 relation identities checked
there as additional controls. No holdout is used in the target minor.

Source independence is checked on 39 explicit generic quartic points, with
ordinary coefficient integer lifts from the frozen p=2147483647 bank. Every
one of the 1,521 source values is freshly evaluated from its polynomial. Their
nonzero 39-minor and ambient dimension 39 prove the source is a full Q-basis.

## 5. Exact equations and the CI inference

The source matrix has source rows and point columns. Its exact integer
36-minor is recomputed by fraction-free Bareiss elimination with checked exact
divisions. K has 39 rows, three columns, rational rank three, and satisfies
A^T K=0 exactly at all 73 selected points. Therefore rank_Q A=36. The full
target minor and independently proved target dimension 73 make evaluation
injective on N13. Consequently the sampled kernel equals the polynomial
pullback kernel, of dimension 39-36=3.

`results/ci73/equations.json` and `docs/ci73_equations.md` specify every native
source filling, every degree-13 transport, and every coefficient in

    Q_j = sum_(i=0)^38 K[i,j] F_i^up13,  j=1,2,3.

These are integer representatives of a Q-kernel basis. No saturated integral
lattice basis is claimed. An invertible rational rescaling F'_i=s_i F_i changes
coordinates to K'[i,j]=K[i,j]/s_i; the checker uses effective coefficients
s_i K'[i,j], and verifies prime compatibility of scalars explicitly.

The closure of the image of (ell,c) → ell*c is the reducible locus R. The
identities Q_j(ell*c)=0 therefore give three independent elements of I(R) in
this component, and the full source/dimension argument proves i_red(13)=3.

## 6. Transport and qualified LMR consequence

The ambient coefficient ring is a domain. Multiplication by nonzero u^11 is
injective on its ideal subspaces, adds degree 11 and first-row weight 44, and
preserves highest weight. Since the padded permanent locus P is contained in
R, the three polynomials u^11 Q_j lie independently in I(P) at degree 24 and
weight (65,17,2^7). Source definitions are checked to satisfy

    u^11 F_i^up13 = F_i^literal24.

Thus the transported coordinate matrix consists of the same first 39
effective coefficients and 235 zero rows. This establishes i_pad(24)>=3
without assuming that the other two sampled padded relations are equations.

Separately inherited from frozen S74 are ambient a24=274, the determinant
rank floor 273 together with the adopted LMR upper bound 273, and the padded
rank floor 269. The continuation identifies their precise source and minor
records and separately replays the banked minor arithmetic. It does not label
the degree-24 native polynomial values or the literature upper bound as new
fresh degree-13 evaluations. The banked a24 is an inherited dimension result;
the newly proved a13=39 has its own full character replay.

These inherited facts give i_det(24)=1 and i_pad(24)<=274-269=5. With the new
lower bound, 3<=i_pad(24)<=5 and

    D_LMR = mult_pad - mult_det = 1 - i_pad(24) lies in [-4,-2].

D=-4 remains open. This argument does not assert equality of the full padded
and reducible ideals, and makes no new degree-14 claim.
