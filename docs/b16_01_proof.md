# B16-01: finite cubic sources and transport

13 September 2026. Characteristic zero; positive coefficient-weight convention.
This is new Slot01 proof and arithmetic, not a new computation of padding image
ranks or the ambient quartic census. The finite counts below equal the accepted
chart ceilings numerically. The new statement is equality for the finite SOURCE.

## 1. The finite branching identity

Let W have dimension r, let beta be a partition with at most r parts, put
w=|beta| and b=beta_1 (b=0 if beta is empty), and suppose (3d-w,beta) is a
partition. Write a3_d(3d-w,beta) for its multiplicity in Sym^d(Sym^3(C+W)).
All symmetric functions below are in W, graded by ordinary W-weight.

Branch Sym^3(C+W)=C+W+Sym^2 W+Sym^3 W, keeping the first-variable degree.
After putting the first variable equal to one, the degree-d character is

    T_d = sum_{k1+k2+k3 <= d} h_k1 h_k2[h2] h_k3[h3].

The omitted k0=d-k1-k2-k3 counts factors from C. The missing first-variable
weight of a summand is k1+2k2+3k3. It is therefore sufficient to retain W-weight
w, without expanding a character of total weight 3d.

The GL(r+1) Weyl denominator factors as

    product_i(1-y_i) * product_{i<j}(1-y_j/y_i).

The Weyl coefficient formula for a dominant highest weight, followed by the
GL(r) Weyl coefficient formula, gives the exact finite identity

    a3_d(3d-w,beta) = [s_beta] ( E(-1) T_d )_w,
    E(-1) = sum_{j=0}^r (-1)^j e_j.                         (1)

Here [s_beta] means Schur coefficient. This is a finite character identity,
not a dense-chart lifting assumption. Universal symmetric functions can be
used: specializing to r variables only removes types with more than r rows.

## 2. A sufficient finite stability threshold

Assume d >= floor(w/2), as will follow from the final threshold. Fix k2,k3,
put k=k2+k3, v=2k2+3k3, s=w-v and D=d-k. Only v<=w matters and k<=floor(w/2),
so D>=0. Its contribution in (1) contains

    B_(D,s) = sum_{i=0}^{min(D,s)} (-1)^(s-i) h_i e_(s-i).

Since H(t)E(-t)=1, B_(D,0)=1 and B_(D,s)=0 for 1<=s<=D.
For s>D, the horizontal/vertical Pieri identities telescope to

    B_(D,s) = (-1)^(s-D) s_(D+1,1^(s-D-1)).                (2)

This remains true after specialization to r variables; a hook longer than r
vanishes. Thus (1) is the chart coefficient

    h(beta)=[s_beta] Sym(Sym^2 W + Sym^3 W)

plus the signed contributions (2), each multiplied by h_k2[h2]h_k3[h3].
This latter factor is Schur-positive. A nonzero Littlewood--Richardson
coefficient into beta requires its hook factor to be contained in beta;
in particular D+1<=b. Together with s>D, a correction therefore requires

    k >= d+1-b,
    k2+2k3 <= w-d-1.

Since k<=k2+2k3, it requires

    2d <= w+b-2.                                         (3)

Consequently, whenever (3d-w,beta) is dominant,

    d >= floor((w+b)/2)  ==>  a3_d(3d-w,beta)=h(beta).      (4)

The threshold in (4) also implies d>=floor(w/2). It is sufficient, not an
assertion of the least stabilization degree. In particular, for
beta=(b,2^7), w=b+14 and d>=b+7 suffices. No chart denominators or unproved
polynomial extensions enter this equality proof.

The receiver independently enumerates the possible correction hooks at every
assigned channel and checks that none is contained in beta. Its direct
full-plethysm controls include nonstable cases, so it also checks that finite
counts are not indiscriminately replaced by chart counts.

## 3. The product source and its finite counts

Let V have dimension 16 and use the positive coefficient convention. Let
Y=Sub_9(Sym^3 V*) and Z be the closure of products ell*C with ell in V* and
C in Y. Every arbitrary linear substitution in the independent ten-variable
z*per3 belongs to Z. Thus X_pad is contained in Z. Multiplication gives

    A_d=Sym^d(Sym^4 V) --phi--> N_d=Sym^d V tensor C[Y]_d.

The image is C[Z]_d, because pullback into functions on the source is
injective for the coordinate ring of the image closure. Coefficient degree d
pulls back to source bidegree(d,d). Restriction C[Z]_d -> C[X_pad]_d is
surjective. Characteristic-zero complete reducibility therefore gives

    m_pad(d,lambda) <= rank(phi_lambda) <= dim(N_d)_lambda. (5)

The subspace variety removes precisely the cubic Schur types of length >9.
One elementary way to see this is to restrict coefficient polynomials to every
nine-dimensional subspace: functorial restriction retains each multiplicity
space of a Schur type of length <=9, whereas longer types vanish. Thus the
multiplicity of a length <=9 type in C[Y]_d is its ordinary nine-variable
cubic plethysm multiplicity.

Pieri gives

    dim(N_d)_lambda = sum_{lambda/mu horizontal d-strip, len(mu)<=9} a3_d(mu).

For lambda=(4d-t-16,t,2^8), interlacing forces mu_10=0,
mu_3=...=mu_9=2, 2<=mu_2=b<=t and

    mu_b=(3d-14-b,b,2^7).                                 (6)

All remaining inequalities hold at the four assigned cells. The receiver
enumerates all strips directly, then compares to (6). By (4), all their finite
cubic counts equal the following freshly recomputed character sums:

| b | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |
|---|---|---|---|---|---|---|---|---|---|
| a3 | 1 | 1 | 2 | 3 | 5 | 6 | 9 | 11 | 14 |

| b | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 |
|---|---|---|---|---|---|---|---|---|---|
| a3 | 16 | 19 | 21 | 24 | 26 | 29 | 31 | 34 | 36 |

| Degree | Quartic weight | Channels | Largest sufficient degree | Exact source dimension | Padding ceiling |
|---|---|---|---|---|---|
| 23 | (61,15,2^8) | b=2..15 | 22 | 158 | 158 |
| 25 | (67,17,2^8) | b=2..17 | 24 | 218 | 218 |
| 26 | (71,17,2^8) | b=2..17 | 24 | 218 | 218 |
| 27 | (73,19,2^8) | b=2..19 | 26 | 288 | 288 |

The same channel argument at the inherited stable cell d35 gives source 288.
That is a source count, not a rank computation. It supplies no improvement
to the accepted 243<=m_pad<=288 interval there.

The source channels are counted as summands of N_d. Equation (5) does not say
their images are independent or that phi is surjective. The actual product
image can be smaller; restriction to the genuine permanent can decrease it
further. In particular this result does not prove m_pad equals 158,218 or288.

## 4. Precise map and transport bounds

For any finite cell with ambient multiplicity a and this source dimension U,

    m_pad <= min(a,U),  i_pad >= max(0,a-U).                 (7)

Writing i_det in [q,J], the bound on the multiplicity gap is

    D=m_pad-m_det=i_det-i_pad <= min(a,U)-a+min(a,J).

In particular, a>=U+J is a sufficient exclusion. Conversely, to prove
positivity using a certified ideal floor q, an actual padding coordinate
floor r must satisfy r>=a-q+1. Since r<=U, a<=U+q-1 is necessary for success
using that particular q. Failure of this necessary condition is not alone
an exclusion of a gap with a larger determinant ideal floor.

Here the inherited exact ideal dimension in the d35, tail19 cell is 11.
The following explicit coefficient multipliers give J=11 for every assigned
cell, without presuming a complete finite equation filtration. On the first
two variables write a quartic as

    c*s^4 + A*s^3*y + B*s^2*y^2 + ... .

Let u=c and v=8cB-3A^2. Their coefficient degrees and positive weights are
(1,(4,0,...)) and (2,(6,2,0,...)). Under s -> s+h*y,

    c'=c, A'=A+4ch, B'=B+3Ah+6ch^2,

so v'=v by direct expansion. Both are highest-weight polynomials: the first
two-variable shear is the only potentially nontrivial raising action, and
all higher-variable raising actions vanish on their coefficients. They are
nonzero polynomials in the ambient coefficient ring, which is a domain.
Multiplication by their powers preserves any GL-stable ideal and is injective
on its highest-weight space.

Set k=(19-t)/2 and j=35-d-2k. The multipliers below all have j,k>=0 and send
the assigned degree/weight exactly to d35,(105,19,2^8):

| Starting cell | k | j | Injective ideal multiplier |
|---|---|---|---|
| d23,t15 | 2 | 8 | u^8 v^2 |
| d25,t17 | 1 | 8 | u^8 v |
| d26,t17 | 1 | 7 | u^7 v |
| d27,t19 | 0 | 8 | u^8 |

The degree increment is j+2k and weight increment is (4j+6k,2k,0,...).
Thus i_det(d,lambda)<=11 using the inherited d35 ideal dimension. This is
an ideal injection; no assertion of nonzero quotient multiplication is
needed for this upper bound. Along a fixed tail, multiplication by u also
injects coordinate spaces on det or padding, since each coordinate ring is
an irreducible orbit-closure domain and u is nonzero there. For example,
m_pad(25,(67,17,2^8)) <= m_pad(26,(71,17,2^8)) <=218. This direction does not
transport a stable padding floor backwards.

With the inherited q=1,2,2,5 respectively, the numerical receiver thresholds
for the separate ambient census are:

| Cell | q | U | Required padding floor | Necessary a using q | Exclusion if a is at least (J=11) |
|---|---|---|---|---|---|
| d23,t15 | 1 | 158 | a | 158 | 169 |
| d25,t17 | 2 | 218 | a-1 | 219 | 229 |
| d26,t17 | 2 | 218 | a-1 | 219 | 229 |
| d27,t19 | 5 | 288 | a-4 | 292 | 299 |

No ambient value at these cells is asserted here. The interval between the
last two thresholds requires stronger information on i_det or actual ranks.

## 5. Arithmetic and provenance

The weight-graded series is

    F(z)=exp(sum_{j=2,3} sum_{r>=1} sum_{rho |- j}
             p_(r*rho) z^(jr)/(r*z_rho)).

Writing its logarithmic derivative as sum_m L_m z^m gives
n F_n=sum_{m=1}^n L_m F_(n-m), with exact rational coefficients. The saved
arithmetic records every power-sum partition, numerator, denominator and
character in all 18 sums. Characters use both outer-rim removal and a
separate beta-number implementation. Controls compare the series through
weight12 with the direct outer-partition definition, test complete character
orthogonality through S6, and compare (1) to full h_d[h3] in 235 dominant
small cells with d<=6 and tail weight<=8. The full small expansion has total
weight at most18. No high-degree dense carrier was built.

Fresh: formulas (1)--(4), exact finite interpretation at the four cells,
complete strip checks, regenerated character arithmetic, 235 finite controls,
and the explicit u/v transport proof. The executable receiver recomputes the
whole certificate and rejects changed source totals, characters, missing
channels, and treating a source count as an image rank. Both implementations
are by this same task; this is not an external independent mathematical review.

Inherited: Dream_Upper288's source-map framing and accepted stable
a=429,m_det=418,m_pad>=243; existing determinant equation floors1,2,2,5.
The accepted B15-01 full replay and its nine-row conclusions were read and
preserved, not rerun and not recast as a cubic or ten-row count. The original
worker reports credit native S74/B14-07 work, including Claude Opus 5. This
task preserves that attribution and makes no new claim from those numerical
entries. Inspected B15-01 dimension code and retained Session30 helpers
provided algorithmic context; the delivered code imports neither producer.

The standard product-map/subspace background is also described in
[Kadish--Landsberg, Theorem 1.7 and Proposition 1.12](https://arxiv.org/pdf/1204.4693v1).
The finite correction argument above is given in full and makes no literature
priority claim. Exact working-byte hashes of every local source read are in
results/b16_01/input_hashes.json; runtime wrapper/script hashes are in receipts
and the delivery inventory. Hashes bind bytes, not mathematical truth.

Limits and next sufficient witness: no actual image rank, new padding minor,
new ambient count, complete determinant filtration, optimal stabilization
degree, or positive multiplicity gap was computed. If the ambient census
leaves a viable cell, the next positive witness is a global determinant ideal
floor q plus an actual independent ten-variable z*per3 restriction minor of
rank r with q+r>a. To improve U below the exact finite source dimension,
one must bound the product image or its further genuine-permanent restriction;
additional finite cubic source counting at these cells cannot lower U.
