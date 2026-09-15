# B16-07 exact low-rung exclusion certificate

Work over Q (and hence C) in the positive coefficient-weight convention
`C[Sym^4 V*]=Sym(Sym^4 V)`. For `d=14,15`, put
`lambda_d=(4d-35,21,2,2,2,2,2,2,2)`. Its size is `4d`, and it is a
dominant nine-row partition, including at d=14 where the first two parts
are equal. Ideals and coordinate rings refer to orbit closures.

**Finite restriction.** Write a general nine-variable quartic as

`G(t,x)=c t^4+a1(x)t^3+a2(x)t^2+a3(x)t+a4(x)`.

A homogeneous coefficient polynomial F of degree d is determined by its
restriction to c=1, because `F(G)=c^d F(G/c)` on the dense open set c!=0.
Its restriction to c=1 has ordinary coefficient degree at most d.
For a highest-weight F, the first-row unipotent root groups make that
restriction invariant under `t -> t+ell(x)`. The unique depressed
representative is obtained by `t -> t-a1(x)/4`. Denote the depression
map at c=1 by pi. Thus there is a unique slice polynomial psi with

`F|_(c=1)=psi o pi`.

Restriction is injective, including at d=14; no stable-range equality
of ambient multiplicities is required. If F vanishes on determinant
substitutions, psi vanishes on the traceless-pencil slice, since a
determinantal quartic with invertible leading matrix normalizes and
depresses to `det(t I4+A(x))` for a traceless pencil A.

The nine-variable convention does not weaken the 16-variable statement.
In characteristic zero, a highest-weight coefficient polynomial with
nine-row weight restricts injectively to the first nine variables (Schur
functor inheritance). A generic 16 by 9 linear map extends to an invertible
16 by 16 map; arbitrary maps follow by closure. Thus determinant ideal
membership restricts to the same nine-variable substitution locus.

**The accepted complete stable space.** On the depressed slice set

`F_slice(t,x)=t^4+f2(x)t^2+f3(x)t+f4(x)`,
`s_j=f_j(e1)`, `p(t)=t^4+s2 t^2+s3 t+s4`.

Let `R0+R1 t+R2 t^2+R3 t^3` be the monic remainder of the determinant
of the full nine-variable Hessian of F_slice, evaluated at `(t,e1)`,
divided by p. In the order used throughout the certificate, set

`Phi=(s4 R3, s2^2 R3, s3 R2, s2 R1)`.

The Slot05 Hessian review proves global vanishing and the exact
identification of this four-space with the stable determinant ideal at
tail `(21,2^7)`. Its completeness uses the accepted stable ambient 533
and determinant image floor 529. The membership mechanism is the
rank-at-most-eight Hessian of det4 at every singular matrix: at a
rank-three normal form the quadratic part is `a tr(E)-r c`, with Hessian
rank eight; congruence and density extend the bound. Pullback to nine
pencil directions preserves the bound. Hence the Hessian determinant
vanishes at every simple characteristic root; monic remainder
polynomiality and density extend this identity to all traceless pencils.
The review's rational source identities certify the exact Phi convention.

We inherit this complete-space statement. Therefore every finite F in
either target determinant ideal has

`F|_(c=1)=sum_j alpha_j Phi_j o pi`, with alpha_j in Q,

and its right side has coefficient degree at most d. It is enough to
give four independent necessary conditions on the constants alpha_j.

**An authentic ambient test family.** Put x=(x1,...,x8), and for
`i=0,...,6` put `(A_i,B_i,C_i)=(i+1,2i+1,3i+2)`. Define

```
a2 = 2*x1^2 + sum_(i=0)^6 A_i*x_(i+2)^2
a3 = 3*x1^3 + 3*sum_(i=0)^6 B_i*x1*x_(i+2)^2
a4 = 5*x1^4 + 6*sum_(i=0)^6 C_i*x1^2*x_(i+2)^2
G_u = t^4 + u*(4*x1*t^3 + a2*t^2 + a3*t + a4).
```

All nonleading coefficients of G_u depend linearly on u. Consequently
evaluation of any coefficient polynomial of degree <=d at G_u has
u-degree <=d. This holds even though the family is special; a necessary
degree condition on a special family is sufficient for an upper bound.

At x=e1 the full ordinary Hessian is block diagonal, with first block

```
[12*t^2+24*u*t+4*u,       12*u*t^2+8*u*t+9*u]
[12*u*t^2+8*u*t+9*u,       4*u*t^2+18*u*t+60*u]
```

and seven one-by-one blocks

`u*(2*A_i*t^2+6*B_i*t+12*C_i)`.

Thus its determinant D(t,u) is the 2 by 2 determinant times the seven
displayed entries. The producer saves the complete exact bivariate
polynomial. The receiver instead constructs G_u, differentiates it in
all nine variables, substitutes x=e1, and computes the determinant
symbolically. Those two constructions agree coefficient by coefficient.

Divide D(t,u) monically in t by

`p_u=t^4+4*u*t^3+2*u*t^2+3*u*t+5*u`.

Write its remainder as `S0+S1*t+S2*t^2+S3*t^3`. Exact quotient and
remainder are saved. The depression shear is `t -> t-u*x1`, whose
determinant is one. Hessians transform by congruence under this fixed
linear substitution, so their determinants and their monic remainders
transform by the same substitution. At e1 this gives

```
R3 = S3
R2 = S2-3*u*S3
R1 = S1-2*u*S2+3*u^2*S3
s2 = 2*u-6*u^2
s3 = 3*u-4*u^2+8*u^3
s4 = 5*u-3*u^2+2*u^3-3*u^4.
```

In particular these are exactly the Phi functions in the accepted basis,
evaluated on pi(G_u), with no tensor normalization or scalar ambiguity.
The receiver independently depresses the whole quartic as a check.

**Saved arithmetic.** In the order Phi above, the coefficient rows at
u-powers `(28,26,25,24)`, after division of each row by its positive gcd,
form the integer matrix

```
M = [         -1,          12,          -8,          -6 ]
    [    -906993,    10740556,    -7202184,    -5397158 ]
    [   28769891,  -330695844,   224156760,   167800306 ]
    [ -343406787,  3755985188, -2586728520, -1934494122 ].
```

The positive row divisors, in the same order, are

```
299243084615516160, 22265110462464, 2783138807808, 695784701952.
```

Exact determinants are

```
det(M) = -5639493386240000
det(raw coefficient matrix) =
-72761025516595267466940416959830900717923971797102514649360341401600000.
```

Both are nonzero. The independent receiver checks the entire polynomial
data and this minor over Z, not only modulo a prime or at finitely many
values of u. Four deliberate coefficient changes are rejected. The
producer's three integer 9 by 9 Hessian evaluations are additional
instrument controls; they do not supply polynomial completeness.

**Conclusion for the two assigned degrees.** Each of 28,26,25,24 is
greater than 14 and 15. Hence any finite determinant equation F in
either target cell must satisfy `M alpha=0`. Invertibility gives
alpha=0, and finite restriction injectivity gives F=0. Thus

`i_det(14,(21,21,2^7))=i_det(15,(25,21,2^7))=0`.

No finite ambient count is substituted for 533. The equality `m_det=a`
is a consequence of the proved ideal zero in each finite cell.

**Padding and sign.** Nonnegativity of i_pad alone gives D14<=0.
For degree 15 use the accepted CI73 independent degree-13 equations
`Q1,Q2,Q3` at weight `(21,17,2^7)`, vanishing on all products of a
linear form and a cubic. In ordinary binary quartic coefficients put

`q44=12*c0*c4-3*c1*c3+c2^2`.

This is a nonzero degree-two highest-weight polynomial of weight (4,4).
The raising operator satisfies `E(c_j)=(5-j)c_(j-1)`; direct
differentiation gives E(q44)=0. Other raising operators act trivially
because only the first two variables occur. The receiver checks this
identity, a nonzero value, and rejection of an altered coefficient.
Multiplication by q44 in the ambient polynomial domain is injective,
so `q44 Q1,q44 Q2,q44 Q3` are three independent degree-15 equations
of weight `(25,21,2^7)`. Every independently padded form z*per3 is
reducible, including arbitrary linear substitutions and closures.
Therefore `i_pad15>=3`, retaining all ten independent source variables.

Finally, characteristic-zero semisimplicity gives `m_X=a-i_X` in
each fixed finite cell. Thus `D=i_det-i_pad`, and

`D14=-i_pad14<=0`, `D15=-i_pad15<=-3`.

The old exact CI computation is inherited; it is not repeated here.
No source dimension is identified with an image rank, no padded and
reducible image equality is used, and no positive multiplicity gap is
asserted. This proof makes claims only for the two assigned low cells.

