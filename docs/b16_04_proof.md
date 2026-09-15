# B16-04: exact finite filtration of the global Hessian eleven-space

13 September 2026. New derivation and code: gpt-6-astra/xhigh. The inherited
Hessian construction/evaluator is the gpt-6-astra Hessian11_1631 packet;
its underlying bracket normalization retains Claude Opus 5 attribution.
All arithmetic is rational, in characteristic zero.

**Result.** For the eleven-dimensional global determinant equation space of
stable tail `(19,2^8)`, its finite dimensions in degrees 23,24,25,26,27 are
**4,7,9,10,11**. They are zero through degree22 and eleven thereafter.
For the corresponding complete stable spaces in tails `(17,2^8)` and
`(15,2^8)`, the dimensions are respectively **2,3,4,4,4** and **1,1,1,1,1**
in degrees23 through27; both are zero through22.

The assertion about filtration of the displayed spaces uses only their
global identities and independence, freshly replayed here. Identifying
these with the **entire determinant ideal multiplicity spaces** additionally
uses the accepted B15 stable tail19 equality `429-418=11` and the S57
highest-weight/ideal filtration. Those are inherited, not recounted here.

| Declared cell | Exact determinant ideal dimension, under those premises |
|---|---:|
| d23, `(61,15,2^8)` | 1 |
| d25, `(67,17,2^8)` | 4 |
| d26, `(71,17,2^8)` | 4 |
| d27, `(73,19,2^8)` | 11 |

No ambient finite multiplicity or padding image rank is inferred from these
numbers. They are dimensions of actual independent equations, not a sum of
scalar/product or tensor channels.

## 1. The inherited space and notation

Write a monic depressed quartic as
`F(t,x)=t^4+f2(x)t^2+f3(x)t+f4(x)`, with nine x variables and `e=e1`.
Let `Nd=Hess(fd)(e)/(d(d-1))`, `ud=Nd e`, and `sd=e^T Nd e`.
The three symmetric nine-by-nine matrices Nd can be arbitrary: their entries
are the freely specifiable second jets at e of homogeneous forms fd.
Set

```
p=t^4+s2*t^2+s3*t+s4
B=2*t^2*N2+6*t*N3+12*N4
v=4*t*u2+3*u3; h=12*t^2+2*s2
H=[[h,v^T],[v,B]]
A=det B; D=det H
Jd=-ud^T adj(B) v
Q22=(0,u2)^T adj(H) (0,u2)
Td=tr(adj(H) diag(0,Nd))
Rj(P)=[t^j](P mod p); Sj=[t^j](D mod p^2).
```

The ordered basis `E` used in every exported vector is the inherited
indices `[0,1,2,3,4,5,6,7,8,10,11]`:

```
(R1(A), s2*R3(A), R2(J2), R3(J3), R3(Q22),
 S3, s2*S5, s3*S6, s4*S7, R1(T2), s2*R3(T2)).
```

The lower-tail bases are `L=(R3(A),R3(T2),S5,s2*S7)` at tail17 and `S7`
at tail15. The inherited source receiver regenerates all 363 Euler
relations, the exact fourteen-to-eleven dependencies, and a nonzero integer
eleven-by-eleven ambient minor. In particular the omitted `s2^2*S7` is
already a linear combination, not a twelfth direction. The lower-tail
four- and one-dimensional independence minors are also freshly replayed.

For det4, the Hessian at every singular matrix has rank at most eight.
Thus ordinary adjugate remainders vanish, and `p^2` divides the ten-by-ten
Hessian determinant on the squarefree-pencil open set. Monic division
and density establish the inherited global equations, including arbitrary
linear pencils and orbit closure. Sampled zeros are not used as that proof.

## 2. Exact polynomiality is a c-adic problem

Write an unnormalized quartic as

`G=c*t^4+4*L(x)*t^3+a2(x)*t^2+a3(x)*t+a4(x)`.

Normalize and depress by `t -> t-L(x)/c`. If
`Md=Hess(ad)(e)/(d(d-1))`, define `Kd=c^d Nd` for the resulting depressed
jets. Weighted homogeneity gives, for tail `(tau,2^8)` of weight `W=tau+16`,

`c^W E(pi(G/c)) = E(K2,K3,K4) = P_E(c)`.

This is a polynomial in the original coefficients. Therefore the unique
rational lift `c^d E(pi(G/c))` is polynomial exactly when `P_E` is divisible
by `c^(W-d)` in that coefficient ring. There are no other denominators
apart from fixed rational constants. The coefficient degree of the lift is d.

It is enough to prove each coefficient identity when `L=x1`. To see this,
on the dense open set `a=L(e) != 0`, choose an invertible g with
`g e=e/a` and `L g=x1`. Bracket equivariance under the parabolic stabilizing
the line e multiplies a tail-tau expression by
`det(g)^2*(1/a)^(W-18)`, a nonzero factor independent of c. A coefficient
identity for arbitrary raw jets on the aligned chart therefore holds on
that dense open set, and hence identically. This is not specialization to
diagonal determinant pencils. A fresh exact control with nontrivial L and
g checks this transformation separately.

For `L=x1`, split each raw matrix as
`Md=[[sd,bd^T],[bd,Cd]]`, with an eight-dimensional transverse block.
The transformed jets are

```
K2 = c*M2 - 6*e*e^T
K3 = c^2*M3 -(2*c/3)*(M2+e*u2^T+u2*e^T) +8*e*e^T
K4 = c^3*M4 -(c^2/4)*(2*M3+e*u3^T+u3*e^T)
     +(c/6)*(M2+2*e*u2^T+2*u2*e^T+s2*e*e^T)-3*e*e^T.
```

Here `ud=Md e` and the scalars on the right are raw, not depressed.
Every transverse row of every Kd and of every Kd e is divisible by c.
Each inherited bordered-determinant source expression has eight such
rows, so **every source numerator is divisible by c^8**. This proves the
universal safe lift degree `W-8=tau+8`: all eleven directions lift by27,
all four lower directions by25, and S7 by23. The source expansion, not
an observed sampled vanishing order, proves this bound.

To obtain all degrees23..27 it remains to know at most four coefficients
of `P_E/c^8`: its c-orders0,1,2,3. All higher orders are irrelevant to these
filtration tests. They were not expanded.

## 3. A complete universal calculation with small support

Put `u=t-1`. After removing the eight transverse row factors c, the Hessian
has a transverse matrix

`C0=alpha*C2+c*beta*C3+c^2*gamma*C4`,
where `alpha=2*u^2`, `beta=6*u`, `gamma=12`.

Its two transverse off-block coefficient rows, in the ordered vectors
`(b2,b3,b4)`, are

```
vbar=(4*u, 3*c, 0)
wbar=(2*u*(u-2), 3*c*(2*u-1), 12*c^2).
```

The scalar transformed jets are

```
s2k=-6+c*s2
s3k=8-2*c*s2+c^2*s3
s4k=-3+c*s2-c^2*s3+c^3*s4.
```

Work provisionally on the dense open set `det C2 != 0`, and set
`X=C2^(-1) C3`, `Y=C2^(-1) C4`. The exact expansion through c^3 is

```
det(C0)/det(C2) = alpha^8
 + c*beta*alpha^7*tr(X)
 + c^2*(gamma*alpha^7*tr(Y)
        + beta^2*alpha^6*(tr(X)^2-tr(X^2))/2)
 + c^3*(beta*gamma*alpha^6*(tr(X)*tr(Y)-tr(XY))
        + beta^3*alpha^5*(tr(X)^3-3*tr(X)*tr(X^2)+2*tr(X^3))/6).
```

In each Schur complement the inverse is multiplied by an additional c,
so only inverse orders0..2 are needed:

```
C0^(-1) = C2^(-1)/alpha
 - c*beta*X*C2^(-1)/alpha^2
 + c^2*(beta^2*X^2*C2^(-1)/alpha^3
        -gamma*Y*C2^(-1)/alpha^2) + O(c^3).
```

For each pair of border vectors bi,bj, introduce formal Gram symbols for
the four bilinear expressions using `C2^(-1)`, `X*C2^(-1)`,
`Y*C2^(-1)`, `X^2*C2^(-1)`. These and the five trace symbols are treated
as **independent formal variables**. No assertion of their independence
on actual matrices is required: a polynomial identity in the free formal
ring remains an identity after matrix substitution.

For any small scalar block Z and off-block rows V,W the exact identity is

`det [[Z,c*V],[W^T,C0]] = det(C0)*det(Z-c*V*C0^(-1)*W^T)`.

`b16_04_universal.py` applies this with scalar block sizes1,2,3 to A,
J2,J3,D,Q22. It obtains Td by differentiating
`det(H+z*diag(0,Kd))` at z=0, including the scalar, border, and transverse
matrix derivatives. Terms of z-degree2 or higher cannot affect this
derivative. It then performs exact monic t-division by p or p^2 over the
truncated coefficient ring. Truncation in c commutes with monic division.
All temporary alpha denominators cancel before substituting alpha.

The exported universal coefficient lists contain the **entire** required
c-orders0..3 in the free trace/Gram ring, after division by `det C2`.
Vanishing there proves the original coefficient vanishes on `det C2 !=0`,
then polynomial density removes that condition. The earlier c^8 proof
covers every omitted negative/lower order. The peak intermediate sparse
support was764 terms, against an enforced100000-term assertion.

## 4. Necessary constraints, sufficient identities, and exact dimensions

Four explicitly saved arbitrary raw-jet points (seeds91604..91607) give
necessary conditions on any polynomial lift. Each coefficient is obtained
by complete interpolation of `P_E(c)` at36 integers. The safe degree
bound is35; the actual source bounds are at most26. One held-out c=37
evaluation also agrees. Each Hessian polynomial is itself reconstructed
from21 t-values, its proven maximum t-degree being20. The raw matrices
are integral with M2 scaled by6 and M3 by4 only to clear fixed constants.

At degree d, stack every coefficient row with exponent `k<W-d` from all
four points. A nonzero rational rank minor of this matrix gives a rigorous
upper bound on the dimension of possible lifts. The receiver saves the
actual row/column selections, rational matrices, and nonzero determinants.
It does not mistake a sampled zero for a universal identity.

For every vector in the nullspace of this necessary matrix, the universal
calculation in section3 verifies every required c coefficient is exactly
zero. Thus the necessary kernel is contained in the true polynomiality
kernel. The reverse inclusion follows from specialization. This proves
**equality of the two kernels**, and therefore complete filtration
constraints relative to each declared stable space. It does not assume
the formal trace/Gram symbols have no intrinsic relations.

`universal_pole_certificate.json` stores every kernel basis in the fixed
orders E and L. Their dimensions are

| Tail tau | d<=22 | d23 | d24 | d25 | d26 | d27 and later |
|---|---:|---:|---:|---:|---:|---:|
| 19 | 0 | 4 | 7 | 9 | 10 | 11 |
| 17 | 0 | 2 | 3 | 4 | 4 | 4 |
| 15 | 0 | 1 | 1 | 1 | 1 | 1 |

The full necessary rank at22 excludes all earlier degrees by nesting.
For example the tail17 degree23 basis, in order L, is

`(-15/4,3/8,1,0)` and `(33/2,3/4,0,1)`.

For tail19 a degree23 basis, in order E, is

```
(2/3,5/9,26/9,-3/2,1,0,0,0,0,0,0)
(16/3,560/33,592/99,1094/33,0,-52/99,2/99,1,0,0,0)
(20/3,-46/3,-44/9,-97/3,0,-1/9,-1/9,0,1,0,0)
(32,112/11,92/33,67/11,0,16/33,40/33,0,0,2,1).
```

For each displayed vector f the actual equation is `c^23 f(pi(G/c))`.
The other degrees use their corresponding exported kernel vectors.
Independence follows by restricting to `c=1,a1=0`, where these vectors
are independent linear combinations of the already certified basis.
Polynomiality extends determinant vanishing from `c!=0` to every pencil
and its closure. Highest weights are `(4d-tau-16,tau,2^8)` by the
inherited highest-weight chart construction. In particular the new
tail19 degree23 weight is `(57,19,2^8)`, distinct from the declared
tail15 degree23 cell. These dimensions are never combined across cells.

The degree23 equations lie outside the homogeneous ideal generated by
degree24 equations for the elementary degree reason. This makes no claim
about all LMR constructions, saturation, or literature novelty. No
multiplication-image dimension is inferred from these bases.

## 5. Completeness of the lower-tail stable spaces

This step uses the accepted fact that the entire stable tail19 determinant
ideal is E. Multiplication by the nonzero polynomial s2 injects the stable
tail17 determinant ideal into E. Its image lies among elements of E
divisible by s2. At12 fresh ambient points with `s2=0`, the E evaluations
have exact rank7, with a retained nonzero rational minor. Thus at most4
elements can be divisible by s2. The four known products

`s2*L = (E_index1, E_index11, E_index6, E_index9)`

are independent and belong to E; the last has its inherited exact
eleven-basis coordinates, not an additional direction. Therefore the
entire stable tail17 ideal is precisely L. Applying the same argument
to L at `s2=0` gives rank3, so its divisible subspace has dimension1,
attained by `s2*S7`. Hence the entire stable tail15 ideal is spanned by S7.
The saved points are genuine ambient homogeneous jets; s2 is an independent
coordinate in their polynomial ring. These are necessary divisibility
constraints matched by actual products, not sampled ideal-membership claims.

With S57's identification of the finite ideal as the intersection of the
stable ideal and the finite ambient filtration, section4 now supplies exact
finite determinant ideal multiplicities, including the four declared cells.

## 6. Verification, inherited boundaries, and what remains

The final receiver regenerates all four c-interpolation pilots and compares
their exact saved coefficients. A separately implemented Schur/trace/Gram
calculation agrees with256 direct Hessian coefficients. It verifies every
universal kernel vector, all necessary pole minors, the stable descent
minors, the inherited eleven-space independence and Euler identities, and
the nontrivial parabolic coordinate control. A changed-value control is
rejected. Hashes of all recorded mathematical inputs are checked on replay.

Fresh: pole transformation, universal c^8 bound, full required universal
coefficient expansion, exact necessary minors, matched finite kernels,
lower-tail stable descent bounds, and executable receiver. Fresh replay
of inherited code is identified as replay, not an independent replacement
proof of the B15 Hessian global-vanishing argument.

Inherited: stable ambient429, determinant rank418, S57's chart and ideal
filtration, the original global Hessian identities, and standard
characteristic-zero highest-weight inheritance to16 ambient variables.
The B15 input files are preserved. The frozen per-worktree head is taken
from the launch manifest; no new Git verification, commit, merge, or common
base is asserted.

The declared-cell exact determinant ideals are q=(1,4,4,11). A positive
witness would need an actual independent ten-variable `z*per3` rank at
least `a-q+1` in that same cell. Source sizes158,218,218,288 are only
padding upper bounds. During closeout the integrator delivered accepted
Slot02 finite ambient counts `(189,294,294,429)` in the frozen snapshot
`Batch16/reviews/02/integrator_review.json`, now a hashed inherited input.
Combining those counts with the exact ideals gives

| d | a | i_det | m_det=a-i_det | m_pad upper | D upper |
|---|---:|---:|---:|---:|---:|
| 23, tail15 | 189 | 1 | 188 | 158 | -30 |
| 25, tail17 | 294 | 4 | 290 | 218 | -72 |
| 26, tail17 | 294 | 4 | 290 | 218 | -72 |
| 27, tail19 | 429 | 11 | 418 | 288 | -130 |

These are rigorous exclusions using full determinant ideal upper bounds,
not merely a failed sufficient positivity inequality. The sufficient
padding witness sizes `(189,291,291,419)` exceed their certified source
ceilings; consequently no such witness exists in these cells and no rank
search is proposed. No new padding rank production was performed. The
inherited receiver's tiny independent-padding control remains only a floor.
The next useful receiver action is independent review of the present
complete filtration and its exact bases, or using them in the assigned
multiplication-image comparison; a new positive target would require a
different finite cell and independently certified premises.

Every computation used the inspected Windows Job Object wrapper, one
process/BLAS thread, a60-second wall cap and512MiB cap. No heavy lease was
requested or held. Resource summaries retain implementation/debug failures
as well as final successful runs. These failures were API/serialization
issues, not suppressed mathematical counterexamples. See the resource and
process-exit receipts for measured totals and final status.
