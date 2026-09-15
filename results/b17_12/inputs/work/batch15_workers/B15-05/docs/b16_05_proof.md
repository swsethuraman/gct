# B16-05: shared split-cubic identities and an exact small restriction image

All statements below are in characteristic zero. The finite ambient space uses
sixteen variables, with ten independent source coordinates `(z,x1,...,x9)` for
`z*per3`. A split cubic means `z*C(x1,...,x9)` for an arbitrary homogeneous cubic
`C`, followed by linear substitution. It does not mean a product of three linear
forms. Let Z denote the closure of this larger family.

## 1. Universal Hessian factorization

Write `g=grad C`, `H_C=Hess C`. Euler's identities give

`H_C x=2g`, `x^T g=3C`.

The essential ten-variable Hessian is

`H_(zC) = [[0,g^T],[g,z H_C]]`.

The bordered determinant and polynomial adjugate identity imply

`det H_(zC) = -z^8 g^T adj(H_C)g`

`g^T adj(H_C)g = (1/4)x^T H_C adj(H_C)H_C x`

`= (1/4)det(H_C)x^T H_C x = (3/2)C det(H_C)`.

Consequently

`det H_(zC) = -(3/2) z^8 C det(H_C)`.

No inverse of `H_C` was used, so the identity also holds on its singular locus.
For a ten-by-ten linear substitution L, Hessian congruence multiplies the
determinant by `det(L)^2`. Thus `zC` divides the essential Hessian determinant,
and every corresponding line polynomial divides the Hessian determinant on
that line. Independent L is dense in the parameter space; polynomiality
extends the divisibility remainder identities to dependent L and the closure.
The same substitution argument covers ten-direction restrictions of the
sixteen-variable orbit. It retains z as an independent source variable.

At `z=0`, the Hessian has rank at most two. At `C=0`, the vector `(-2z,x)`
is in its kernel. The order-eight factor at z and the simple factor C are
structural constraints of all of Z, not properties special to the permanent.

## 2. Four exact shared remainder relations

On the nonzero-leading-coefficient chart normalize and depress the quartic:

`F(t,x)=t^4+f2(x)t^2+f3(x)t+f4(x)`;

`sd=fd(e1)`, `ud=grad(fd)(e1)/d`, `Nd=Hess(fd)(e1)/(d(d-1))`.

Set

`p=t^4+s2*t^2+s3*t+s4`,

`H=[[12*t^2+2*s2, (4*t*u2+3*u3)^T],`
`   [4*t*u2+3*u3, 2*t^2*N2+6*t*N3+12*N4]]`,

`D=det H`, `S=D mod p^2=sum_(j=0)^7 Sj*t^j`.

On Z, `p|D` by section 1, hence `S mod p=0`. Direct monic division yields

```
E0 = S0 - s4*S4 + s2*s4*S6 + s3*s4*S7
E1 = S1 - s3*S4 - s4*S5 + s2*s3*S6 + (s2*s4+s3^2)*S7
E2 = S2 - s2*S4 - s3*S5 + (s2^2-s4)*S6 + 2*s2*s3*S7
E3 = S3 - s2*S5 - s3*S6 - (s4-s2^2)*S7
```

All four vanish globally on Z and therefore on padded permanent. The
coefficient reduction is regenerated over `Z[s2,s3,s4]` by
`analysis/b16_05_proof.py`; `proof_arithmetic.json` stores every term.
Over `Q(s2,s3,s4)` these four linear constraints on the eight formal S
coefficients have rank four, since their S0..S3 block is the identity. This
is a formal coefficient rank, not four independent equations in one weight.
Their slice weights are respectively 38,37,36,35. E3 has tail `(19,2^8)`.

The inherited global determinant argument gives `p^2|D`: at each simple root
of a determinantal p, the ten-variable Hessian has rank at most eight, so D
has a double zero. Monic remainder polynomiality and density extend this
to all determinant pencils. Thus E3 is shared by determinant and padding.
This determinant premise is the accepted Hessian11 result, not a new
determinant vanishing proof inferred from numerical zeros.

## 3. E3 is a nonzero finite equation, not a universal ambient identity

The accepted Hessian11 pole bound is `c^(30-j)*Sj` polynomial, and `c^d*sd`
is polynomial. Therefore `c^27*E3` is polynomial: the sufficient powers
for its five summands are `27`, `2+25`, `3+24`, `4+23`, and `4+23`.
It has coefficient degree 27 and highest weight `(73,19,2^8)`, using the
inherited highest-weight convention and ambient inheritance. This proves a
finite shared equation at that cell, not a minimum lift degree.

A fresh integer ambient nonzero is

`E3 = 348671260102848768` at `c=1`.

Its three complete symmetric nine-by-nine matrices N2,N3,N4, all 21
integer Hessian determinants, the interpolated D coefficients and all S
coefficients are in `proof_arithmetic.json`. This is a genuine ambient
quartic jet: choose a symmetric degree-d tensor with
`T[i,j,0,...,0]=Nd[i,j]`, and all unspecified entries zero. Symmetry and
Euler ties are consistent for every symmetric Nd. The quartic is the
displayed monic depressed F. Entries of H have t-degree at most two, so
21 nodes determine D exactly (degree at most20). No generic/nonzero
statement is based on a truncated interpolation.

## 4. Exact restriction rank four in the five-dimensional S space

Let

`W=span(S3, s2*S5, s3*S6, s4*S7, s2^2*S7)`.

W is the five-dimensional ambient squared-remainder space from the
accepted Hessian11 source/independence certificate. The nonzero element
E3 belongs to its restriction kernel on both Z and padded permanent,
so both restriction ranks are at most four.

The new four-point minors, modulo prime 2147483647, are:

| Family | Columns in displayed order (zero based) | Slice minor | Degree27 minor after c^27 scaling |
|---|---|---:|---:|
| Z (arbitrary cubic) | 0,1,2,3 | 803082805 | 509205790 |
| independent z*per3 | 0,1,2,3 | 24032485 | 92514376 |

All are nonzero. Both families use the same four invertible integer L,
whose determinants are `9160047173,-7142132844,63297144,-17994845570`.
Every leading coefficient is nonzero modulo the prime. The selected
points therefore lift to rational characteristic-zero evaluations, and
each modular nonzero proves the corresponding rational minor nonzero.
The complete integer coefficient matrices of all ten native first
derivatives have rank10 for every saved cubic, including the permanent;
essential-variable rank is therefore10 before and after invertible L.

It follows that **both restrictions W->C[Z] and W->C[X_pad] have exact
rank4 and kernel exactly span(E3)**. This holds also for the specified
degree27 lifts and for the degree35 lifts obtained by multiplying by c^8.
It is an exact image statement about this five-space, not the entire
eleven-space or the full429-dimensional multiplicity space.

The lower certificates are fresh. Their proof imports the accepted
five-space dimension/highest-weight/pole-clearing conventions. To bind
the geometry, the receiver regenerates the cubic jets, normalizes and
depresses them, and independently differentiates the native z*C monomials.
It compares all100 Hessian entries at21 nodes at each of the eight saved
points (16800 entry checks). It checks native factorization before
congruence, the line polynomial, and all four remainder relations.
An S3 coefficient mutation is rejected. The final proof run repeats
these geometric checks and extracts the actual4-by-4 minors.

## 5. The full429-space comparison and its limit

Use B15-06's retained generic rank429 pivot rows to fix an ambient basis.
The retained padding minor selects243 points and243 basis coordinates.
Write its basis evaluation matrix in blocks `[A;B]`, with A invertible.
For a new value column `[u;v]`, its residual is

`v-B*A^(-1)*u` in186 coordinates.

The stored A determinant is freshly recomputed as2061185452 modulo the
prime. The old basis/minor values themselves are inherited; this run
does not reconstruct the old243 points. The residual map has rank186
on the inherited generic witness, which is a positive control for the
receiver rather than fresh ambient geometry.

Four independently chosen cubics (165 possible monomials each) and four
genuine permanent substitutions all have zero residual. The receiver
stores their429 coordinates,186 residuals, source L, cubic coefficients,
and full projection matrix. Changed bracket interpolation nodes reproduce
all3432 new ambient entries. A changed residual coordinate is rejected.

These eight zeros do not prove a global186-dimensional kernel, an exact
full padding rank243, or an exact split-cubic image rank243. The certified
interval remains `243<=m_pad<=288`; the source ceiling288 is inherited
and is not an image rank. With `m_det=418`, the stable gap remains
`-175<=D<=-130`. The new shared E3 is not added to the141-dimensional
ideal floor from the source bound; its overlap with that floor has not
been separated.

To settle the plateau, a sufficient next witness is either an exact
split-image upper bound243 (global kernel proof plus an image minor),
or a genuine permanent minor244. A split-cubic minor244 would only refute
the enlarged-family rank243 hypothesis. To prove positivity elsewhere
requires a finite cell with globally certified q and actual padding r
satisfying `q+r>a`; this stable cell cannot supply it.
