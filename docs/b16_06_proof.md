# B16-06: exact LMR polynomial multiplication images

New work: gpt-6-astra, xhigh. Characteristic zero throughout. This proof concerns
the original flag module E24=S_(65,17,2^7) in degree24, with comparison in ten
variables and ordinary coefficient conventions. Inheritance extends the
statements to sixteen variables. The B13-06 tensor census, Claude Opus5 B14
bracket conventions, and the Astra Hessian11 reconstruction retain their
original attribution. No new padding experiment is used.

## 1. A complete source circuit and its exact flag projection

Let G be an arbitrary quartic in ten variables. Use vectors a,b and a covector
n. The determinant twist det(V)^2 is understood when identifying a hyperplane
cofactor with n. Set c=G(a), x=ta+b, p=G(x), H=Hess G(x), D=det H, and

    F(a,b,n)=c^16 [t^-1] n^T adj(H) n / p.

The brackets denote the Laurent coefficient at infinity. This is a polynomial:
adj(H) has t-degree18, so the coefficient uses at most the fifteenth coefficient
of 1/(c+c1/t+...+c4/t^4); c^16 clears every denominator. Its coefficient degree
is9+15=24, and its parameter degrees (a,b,n) are (63,15,2). Translation of t
proves (a.d_b)F=0. On n(a)=n(b)=0 its value is the degree24 LMR flag equation,
up to the common determinant/basis normalization. In particular its incidence
class is nonzero by the inherited LMR source theorem. All coefficients of F
are global determinant equations, by the ordinary 9-minor remainder theorem.
That theorem uses rank Hess(det4)<=8 on the singular locus, division on the
squarefree chart, and density; it is not a conclusion from sampled zeros.

Write u=n(a), v=n(b), C=b.d_a, Da=d_a.d_n, Db=d_b.d_n. The following is an
explicit operator on polynomials of parameter degree (63,15,2), killed by
a.d_b. Each differential word acts on F to its right:

    Fh = F - v DbF/24 + u C DbF/1752 - u DaF/73
       + v^2 Db^2F/1104 - u v C Db^2F/40296 + u v DaDbF/1752
       + u^2 C^2 Db^2F/5802624 - u^2 C DaDbF/126144
       + u^2 Da^2F/10512.

The receiver regenerates these rational coefficients by imposing DaFh=DbFh=0.
For completeness, on a term u^i v^j C^k Da^l Db^m F, set A=63,B=15,N=10.
Da gives the following three terms (any negative exponent or l+m>2 is zero):

    u^i v^j C^k Da^(l+1)Db^m F,
    i(N+i+j-1+A-l-k+2-l-m) u^(i-1)v^j C^k Da^lDb^m F,
    j u^i v^(j-1) C^(k+1)Da^lDb^m F.

Db gives five terms, with coefficients respectively

    1, k, j(N+i+j-1+B-m+k+2-l-m), -il,
    ik(A-B-l+m-k+1),

and index tuples (i,j,k,l,m+1), (i,j,k-1,l+1,m),
(i,j-1,k,l,m), (i-1,j,k,l-1,m+1), (i-1,j,k-1,l,m).
These follow directly from the product rule. They give a rank9 system in ten
coefficients, normalized by the coefficient of F being1. Commuting a.d_b
through the displayed expression also gives zero. Corrections are in (u,v),
so the incidence class is preserved. A separate ordinary-polynomial control
in dimension3 checks both derivatives, the raising equation, incidence
restriction and rejection of a changed coefficient.

Here is why the projected coefficients belong to the specified E24, rather
than merely to the larger remainder module. The parameter module before
projection is S_(63,15)V tensor Sym^2(V*) tensor det(V)^2. Dual Pieri gives
the six rational weights before the determinant twist:

    (63,15,0^7,-2), (62,15,0^7,-1), (63,14,0^7,-1),
    (61,15,0^8), (62,14,0^8), (63,13,0^8).

Each occurs once. For K=uDa+vDb, the Casimir identity gives eigenvalues
0,73,24,144,96,46 respectively. The receiver checks these integers and the
six Weyl dimensions against the full tensor dimension. Thus the joint trace
kernel, which is contained in ker K, has only the first constituent. Its
determinant twist is exactly (65,17,2^7,0). Since Fh has the same nonzero
incidence class as F, it gives the full E24 source circuit. Parameter
differentiation and linear combinations preserve coefficient ideal membership.

## 2. Three actual multiplication maps

For a symmetric tensor M define <M,Fh>=sum M_ij d_ni d_nj Fh. This operation
multiplies coefficient polynomials and contracts parameter indices; it is
GL-equivariant. Define ordinary binary coefficients cj(a,z)=[t^(4-j)]G(ta+z).
The three multiplier tensors are

    M4 = Hess G(a)/12 = G(a,a,-,-),
    M62 = Hess_z(8 c0 c2 - 3 c1^2)/2,
    M44 = Hess_z(12 c0 c4 - 3 c1 c3 + c2^2)|_(z=b)/2.

M4 is linear in coefficients, M62 and M44 quadratic. The latter two come from
the genuine S_(6,2) and S_(4,4) coefficient modules. Their contractions with
Fh give P25, P26_62 and P26_44. They are coefficient degrees25,26,26 and
highest weights (67,17,2^8), (71,17,2^8), (69,19,2^8). This follows either by
parameter degrees and a.d_b=0, or by the displayed equivariant maps. For M44,
a.d_b M44=0 follows from invariance of q44(a,z) under z->z+sa. The two quadratic
tensors annihilate a. There is no addition of tensor multiplicities here.

## 3. Exact reduction to the inherited Hessian coordinates

On the monic depressed chart, take a=e0,b=e1 and the inherited notation

    G(t,x)=t^4+f2(x)t^2+f3(x)t+f4(x),
    p=t^4+s2 t^2+s3 t+s4,
    H=[[12t^2+2s2,(4t u2+3u3)^T],[4t u2+3u3,B(t)]],
    B(t)=2t^2 N2+6t N3+12N4.

Put A_Rj=[t^j](det B mod p), Td_Rj=[t^j](tr(adjH diag(0,Nd)) mod p),
Q22_R3=[t^3]((0,u2)^T adjH (0,u2) mod p), and
Sj=[t^j](det H mod p^2). The results are

    P25 = (2/73) A_R3 + (227/657) T2_R3
        + (2/5037) S5 + (191/45333) s2 S7,

    P26_62 = 16 T2_R3 + (16/69) s2 S7,

    P26_44 = 144 T4_R3 + 8 Q22_R3 + 4 s2 T2_R3
           + (48/23) s4 S7 + (4/23) s2^2 S7.

These equalities are algebraic identities. The following intermediate trace
arithmetic makes their derivation checkable. Let Kj=[t^-1]t^j D/p^2,
Lj=[t^-1]t^j adjH/p, h=16, g=grad G(a), and c1=grad G(a).b. The divergence
of the adjugate of a Hessian is zero (terms cancel in pairs by symmetry of
third derivatives). Also Hx=3 grad G(x), so adjH grad G(x)=Dx/3. Product rules
then give, writing X=DaF, Y=DbF, U=Da^2F, V=DaDbF, W=Db^2F:

    X = 32 c^15 n^T L0 g - (2/3)c^16(u K2+v K1),
    Y = -(2/3)c^16(u K1+v K0),
    W = -(44/3)c^16 K0,
    V = -(2/3)c^15(86c K1+16c1 K0),
    U = 480c^14 g^T L0 g +32c^15 tr(L0 HessG(a))
        -100c^16 K2 -(64/3)c^15 c1 K1.

C acts by Cc=c1, Cc1=2c2, C Kj=(14+j)K_(j+1), C Lj=(16+j)L_(j+1),
Ca=b, Cb=0. The latter residue formulas follow from homogeneity and
[t^-1](t^(j+2)R')=-(j+2)[t^-1]t^(j+1)R. Consequently on the depressed chart:

    K0=S7, K1=S6, K2=S5-2s2 S7,
    X(n=a)=128 A_R3-(2/3)K2,
    (CY)(n=a)=-10K2,
    Y(n=(0,u2))=-(2/3)s2 S7,
    U=8064 A_R3+64 T2_R3-100 S5+200s2 S7,
    CV=-860S5+(5096/3)s2 S7,
    C^2W=-3080S5+(17072/3)s2 S7.

Contraction with M4 sends F to 2A_R3+T2_R3/3, uX to2X(n=a), uCY to
2(CY)(n=a), vY to Y(n=(0,u2))/3, u^2U to2U, u^2CV to2CV,
u^2C^2W to2C^2W, uv times anything to0, and v^2W to(s2/3)W.
The ten columns and their rational sum are saved in projector.json and the
image certificate. They give P25 exactly.

For M62, its chart matrix is diag(0,8N2). Only F, vY, v^2W survive; their
values are 16T2_R3, -(32/3)s2S7, -(704/3)s2S7. Their projector coefficients
are 1,-1/24,1/1104, yielding P26_62. For M44 the chart matrix is
diag(0,72N4+4u2u2^T+2s2N2). The three surviving values are

    144T4_R3+8Q22_R3+4s2T2_R3,
    -96s4S7-8s2^2S7,
    -2112s4S7-176s2^2S7.

The same coefficients yield P26_44. This also checks the factorial convention
in the binary Hessian multipliers. Dense-chart injectivity promotes the
identities to the actual finite coefficient polynomials. Polynomiality here
comes from the parameter circuit, not an unproved minimum pole bound.

## 4. Images, intersections and finite conclusions

The receiver regenerates the fourteen inherited source expansions and their
363 Euler relations, using N_d e=u_d and e^T u_d=s_d. It forms the three displayed
product vectors in that exact quotient. It also computes fourteen fresh generic
integer Hessian evaluations, with complete interpolation of the t-polynomials,
and saves nonzero rational minors. A separate complete bivariate bordered-
determinant interpolation agrees with the source expansions. Thus source
relations supply upper bounds and fresh evaluation minors supply matching
lower bounds; sampled nullities never supply equations.

To compare tail17 in the common tail19 source, multiply every vector by s2.
This is injective in the ambient polynomial ring and changes neither rank nor
intersection dimension. At degree25 the P25 image has rank1, disjoint from
the two-space (S5,s2S7). At26 the images (c P25,P26_62) have rank2, also
disjoint from that two-space multiplied by c. Fresh LR counts are1 and2;
therefore these are the FULL images of E24*A1 and E24*A2 at the respective
tail17 weights. Their unions give determinant ideal floors3 and4 at25/26.

At degree26, P26_44 is a nonzero selected product at weight(69,19,2^8).
Its line is disjoint from the five squared expressions in the stable source.
Those five have only an inherited sufficient lift degree27 in this comparison,
so the rank6 union is NOT asserted to lie in degree26. At degree27 both
c P26_44 and q62 P25 are polynomial. Their two-space is disjoint from the
five degree27 squared expressions, giving a seven-space and i_det>=7 at
(27,(73,19,2^8)). On the normalized chart q62 P25=8s2P25; the harmless factor8
is omitted in the rank matrices. This is a selected image, not all E24*A3.

All these product spaces lie in the certified stable eleven-space. Thus their
intersection with that eleven-space is their entire image (ranks1,2,1,2);
the stable quotient by them has dimensions10,9,10,9 respectively. No claim
places the full eleven-space at degree25,26 or27.

## 5. Precisely which ideal and what remains

Let Jflag=(E24). In the two tail17 cells, the two squared equations have
independent nonzero classes modulo Jflag, because the FULL Jflag images just
computed are disjoint from them. Let J24 denote an ideal generated by the
FULL degree24 ordinary remainder module, allowing planes outside the Hessian
hyperplane. That generator space may be larger than E24. Nothing here proves
these classes survive modulo J24. At degree27 the selected two-space is not
the full Jflag image either, so its quotient is only a quotient by that
specified subspace. The inherited degree23 S7 polynomial is outside any ideal
generated in degree24 simply by grading. None of these statements proves
nonmembership in every LMR construction or a discriminant saturation.

The ordinary remainder construction and the flag/full-module distinction are
in LMR §§2.2–2.3, Theorem2.3.1 of the inspected arXiv v1,
https://arxiv.org/pdf/1004.4802. The checked version is explicitly v1; no full
version-by-version novelty audit is claimed.

For multiplicity comparison, still require finite ambient a and an ACTUAL
padding coordinate floor r in the same cell, with q+r>a. Current derived
floors are q=3,4,7 at25,26,27. Source ceilings are not ranks. No new padding
substitution was made and no nine-variable replacement for independent
ten-variable z*per3 is used. The accepted stable exclusion remains unchanged.

Next sufficient image witnesses: finish all five E24*A2 channels at
(26,(69,19,2^8)), then the full E24*A3 image at degree27, using this source
circuit and bounded parameter derivatives. To decide novelty modulo J24,
first decompose all degree24 nonflag remainder modules and compute their
actual finite multiplication maps and overlaps. No full carrier is priced
or authorized by this report.
