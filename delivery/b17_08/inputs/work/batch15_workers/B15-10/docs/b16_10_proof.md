# B16-10: exact padding arc coefficients and the finite-cell stop

13 September 2026. New proof and implementation: gpt-6-astra, xhigh.
Characteristic zero; ordinary coefficient convention in Sym^d(Sym^4 C^16).
All source membership and finite polynomiality statements for the Hessian
remainders below are inherited from the accepted Hessian11_1631 report and
its integrator review. Their exact input snapshots and hashes are retained.
This task supplies fresh geometric coefficients and a reusable receiver.

## Scope and rigorous stop

There is no surviving cell among the four assigned by slot02. Its final
finite-hook proof and independent receiver give the actual finite ambient
counts below. The accepted Dream_Upper288 product-map proof supplies the
padding coordinate ceilings U. In particular U is not an image rank.

| Degree | Weight | Finite a | U | Full i_det upper | D upper |
|---:|---|---:|---:|---:|---:|
| 23 | (61,15,2^8) | 189 | 158 | 11 | -20 |
| 25 | (67,17,2^8) | 294 | 218 | 11 | -65 |
| 26 | (71,17,2^8) | 294 | 218 | 11 | -65 |
| 27 | (73,19,2^8) | 429 | 288 | 11 | -130 |

Here is a direct finite polynomial transport proof of the full ideal upper,
avoiding an unproved assertion that a source count is an image dimension.
For the binary restriction write G=c t^4+a1 t^3 x+a2 t^2 x^2+... . Set

    h = 8 c a2 - 3 a1^2.

The simple raising operator satisfies E(c)=0, E(a1)=4c, E(a2)=3a1.
Thus E(h)=24ca1-24ca1=0. Other simple raising operators act as zero.
The nonzero polynomial h has coefficient degree 2 and weight (6,2).
The leading coefficient c is highest weight (4), degree 1. The following
multipliers send each specified ideal highest-weight space into the fixed
degree-35, weight-(105,19,2^8) determinant ideal space:

| Input degree | Multiplier | Degree after multiplication |
|---:|---|---:|
| 23 | h^2 c^8 | 35 |
| 25 | h c^8 | 35 |
| 26 | h c^7 | 35 |
| 27 | c^8 | 35 |

All multipliers are nonzero in the ambient polynomial domain. Multiplication
is therefore injective on these vector spaces and preserves the determinant
ideal. No nonvanishing-on-determinant premise is needed for this ideal map.
The accepted stable ambient429 and determinant rank floor418 give full
ideal dimension at most11 at the target. Hence all four finite ideals have
dimension at most11. This argument only uses the accepted upper bound; the
eleven-space equality is unnecessary to the exclusions.

Finally i_pad=a-m_pad>=a-U, so

    D=m_pad-m_det=i_det-i_pad <= 11+U-a.

This proves the table under the named inherited finite counts, stable
rank floor, and padding source bounds. It is not the invalid inference
that failure of a sufficient q+r>a inequality excludes a gap. Even using
q=11, the required padding ranks would be179,284,284,419, all above U.
There is no compatible positive witness in these four cells.

Slot02's finite lemma is inspected: for tau of size n, every finite
character correction contains a hook whose first row is at least2d-n+2.
When this exceeds tau_1, Littlewood-Richardson containment kills the
correction. The four lower bounds are17,19,21,21 versus15,17,17,19.
Its separate connected-border-strip receiver reports PASS for189,294,429,
all four finite arithmetic rows, and five corruption rejections. We retain
that receipt and proof; we do not rerun its count production.
The later independent integrator review also accepted these counts and
exclusions after a fresh0.5511-second receiver run; its hashed snapshot is
included in the supplementary input manifest.

## A true ten-variable arc

Let y=(z,X11,X12,X13,X21,X22,X23,X31,X32,X33). The source is exactly

    P(y)=z sum_(sigma in S3) product_i X_(i,sigma(i)).

Each of its ten formal first partials is nonzero. Their monomial supports
are pairwise disjoint, so they are linearly independent. This proves ten
essential variables, separately from any Hessian or multiplicity rank.

Order the target variables as (t,x1,...,x9). Put

    a=(1,1,0,0,0,1,0,0,0,1),
    b=(2,1,2,1,3,1,2,2,1,4),
    L(u)=[a+u e2, b, e2,e3,...,e9],

with zero-based source indices. The base L(0) is the attributed Dream
full-support control. The new arc changes only its (X12,t) entry. The
upper-left block [[1,2],[1,1]] and the remaining identity columns prove
det L(u)=-1 for every u, exactly. Extending by an identity on six unused
variables gives an invertible GL16 substitution. Thus every point on this
arc is in the genuine padded orbit, not merely a degenerate closure point.

The coefficient of t^4 is per(I3+u E12)=1, so c(u)=1 identically. At
(t,x1,x2,...,x9)=(t,1,0,...,0),

    z=t+2,
    X=[[t+1, u*t+2, 1], [3,t+1,2], [2,1,t+4]].

We differentiate the full ten-variable source before evaluating this line.
The line is only an evaluation path: its two-variable Hessian is never
substituted for the full ten-by-ten Hessian.

## Exact arithmetic and finite source definitions

Let G_u=P composed L(u). Normalize by its leading coefficient and depress
the t^3 term by the full shear t -> t-a1(x)/(4c). Let p(t) be its restriction
at x=e1 and let D(t) be the determinant of the full normalized/depressed
ten-variable Hessian on that line. Set

    S_j=[t^j](D mod p^2),  s2=[t^2]p, s3=[t]p, s4=[1]p.

The inherited polynomial highest-weight sources used here are

    degree23: c^23 S7;
    degree25: c^25 (S5, s2 S7);
    degree27: c^27 (S3, s2 S5, s3 S6, s4 S7, s2^2 S7).

Their weights are those in the stop table. Inheritance includes the
global determinant vanishing proof, denominator induction c^(30-j) S_j,
highest-weight membership, and ambient16 extension. Fresh coefficients do
not by themselves prove these source-membership statements. Multiplying
the degree25 pair by c gives the specified degree26 weight and preserves
our coefficient rows since c(u)=1.

The new code performs exact arithmetic in Q[t,u]/(u^3). It recomputes the
six source monomials, their Hessians, the normalization, monic division by
p^2, and the depression shift. Every denominator has nonzero constant
term; here c=1 and the only rational constants arise from depression.
There is no finite-difference approximation, modular lifting, or numerical
rank plateau. Coefficients are Hasse derivatives, including the factor1/k!
implicit in [u^k].

For cubic C=per3 with g=grad C and H_C=Hess C,

    Hess(zC)=[[0,g^T],[g,zH_C]],
    det Hess(zC)=-(3/2) z^8 C det H_C.

The proof is the polynomial bordered determinant formula, H_C x=2g,
and Euler's identity. Our receiver independently constructs the full
ten-by-ten Hessian from the six quartic monomials and checks equality
with the factored nine-by-nine computation in the truncated polynomial
ring. Congruence then multiplies by det(L)^2. The depression shear has
determinant1; normalization scales the Hessian determinant by c^-10.

Subset determinant expansion stores a used-column mask after each row,
with sign (-1)^(number of previous columns greater than the new column).
This is exactly the ordinary signed permutation determinant grouped by
subsets. A separate three-by-three Leibniz expansion checks this recurrence.
Monic polynomial division commutes with reduction modulo u^3. Inversion of
a unit and substitution by a series do as well. Thus discarding higher
u-orders cannot alter the saved coefficients of orders0,1,2.

## Saved coefficient minors

Rows are [u^0], [u^1], [u^2], in that order. For degree23 the column is

    (8918784, -4999680, -155213568)^T.

The first entry freshly regenerates the attributed control value. For
degree25, columns (c^25 S5, c^25 s2 S7) give

    [  58028544,     62431488 ]
    [ -324600192,      677376 ]
    [  -88058448,  -1136594592 ].

The first two rows have determinant20304580134666240, nonzero over Q.
For degree27 the five columns in the order above give

    [  286868736,   406199808,    317689344,          0,   437020416 ]
    [ -6968562048, -2040087168,  -4533536448, -140470848,   254467584 ]
    [ 12765678912, -2110656240,   6464531808,  247644432, -8164158912 ].

The first three columns have determinant1208423772021694132374994944.
The complete rows and all intermediate polynomial coefficients are in
jet_certificate.json. Exact signed permutation determinants verify both
small minors. The saved shared-padding identity

    S3-s2*S5-s3*S6-(s4-s2^2)*S7=0

holds through all retained arc orders and follows globally from p|D for
split cubics. Its arc verification is a control, not a global identity
inference from three coefficients.

If a linear combination of these source restrictions were zero on the
padded orbit closure, its pullback to this invertible arc would be zero.
Every coefficient functional would vanish. An invertible coefficient
minor contradicts this for any nonzero coefficient vector. Therefore the
fresh named-source restriction floors are1 at23,2 at25,2 at26,3 at27.
These are multiplicity-space restriction bounds, not tangent dimensions.
No claim of an upper bound follows from stopping at order2. At degree27,
slot02's finite/stable identification transports the inherited stronger
padding floor243; our tiny rank3 is an instrument certificate, not an
improvement over that accepted full-space floor.

## Reuse and limits

For any future finite highest-weight sources F_i with proved polynomiality,
form their actual pullbacks along explicitly invertible padding arcs and
retain exact coefficient functionals. Any nonzero k-minor proves a
restriction rank floor k. The source degree is4d in the100 entries of a
ten-by-ten matrix, and one affine line supplies at most4d+1 coefficient
rows. A line with a known base row can add at most4d new rows. These are
support bounds, not promises of independence.

The present single-parameter order2 computation prices only three rows
on eight inherited expressions. It uses at most63 (t,u) coefficient slots
per Hessian polynomial, subset layers at most252, and a hard50000-monomial
guard. Actual maximum support57 and actual largest determinant layer220
are saved. We did not allocate a full degree92/100/104/108 pullback, a
complete ambient source basis, or a rank419 production job.

A future positive witness requires a different finite cell with certified
ambient a, global determinant ideal floor q, and an actual padding
coefficient/evaluation minor of rank r satisfying q+r>a. No witness meeting
that condition exists in these four cells under the accepted premises.
An earlier finite rung outside slot02's onset needs a fresh count and
comparison; none is excluded by this report. No further search is claimed.
