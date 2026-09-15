# B16-09: determinant completion of the B15-08 two-source space

Author: GPT-6 Astra, xhigh, assigned slot09. The sources and their alternating-column evaluator are B15-08 work. B15-08 attributes the underlying two-column bordered determinant to B14-06 / Claude Opus 5. The rational character recurrence and character engine are inherited B14-04 and S30 inputs. Their original bytes, reports, intake review, and attribution are preserved in `delivery/b16_09/inputs`.

## Exact scope and result

Over characteristic zero, take quartic coordinate degree delta=19 and

    lambda=(57,4,3,2,2,2,2,2,2), with trailing zeros to length16.

In this cell a=m_det=2, i_det=0, m_pad<=2, and D=m_pad-m_det<=0. The same statement holds in the inherited conservative stable range delta>=19 at lambda=(4*delta-19,4,3,2^6). No earlier finite stabilization or value of m_pad is asserted. The weighted tail degree19 is not the source's ordinary degree: the two slice sources have respectively9 and8 letters.

## Sources, polynomial lift, and upper bound

Let h=8 and let Q,R,S be the actual symmetric tensors of degrees2,3,4 on the depressed monic quartic chart. Use B15-08's unnormalized alternating sums with two height-eight columns A,B and one height-two column C. In the supplied order define

    B=[(2,AB)^7,(2,C),(3,ABC)],
    H=[(2,AB)^6,(3,ABC),(4,ABC)].

Here an unused letter slot receives e0 and C receives e0 wedge e1. Both sources have weight tau=(4,3,2^6), total tail weight19. The wedge proof in the preserved B15-08 proof gives their highest-weight property; source count alone is not used as a dimension.

For an arbitrary quartic f=c*s0^4+b1*s0^3+b2*s0^2+b3*s0+b4, set gj=bj/c on c!=0 and depress s0 by -g1/4. Its remaining forms are

    G2=g2-3*g1^2/8,
    G3=g3-g1*g2/2+g1^3/8,
    G4=g4-g1*g3/4+g1^2*g2/16-3*g1^4/256.

Each Gd has denominator dividing c^d. Consequently c^19*B(G2,G3,G4) and c^19*H(G2,G3,G4) are global coefficient polynomials. They are homogeneous of coefficient degree19: every fraction gj has coefficient degree0, and multiplying by c^19 supplies degree19. Depression removes the first-row shears; the construction is GL8-equivariant and the wedge proof supplies the remaining upper-unitriangular invariance. Tail weight19 and total weight76 force first weight57. This also directly explains why the conservative degree19 lift is valid. Multiplication by c^(delta-19) gives the stated higher-degree lifts.

The inherited S57 Proposition S identifies the full highest-weight space at delta>=19 with weight tau in Sym(Sym^2 C^8 + Sym^3 C^8 + Sym^4 C^8), and gives an injective restriction to this slice. The B14-04 exact rational power-sum recurrence was rerun at weighted degree19. For every partition rho, the certificate saves [p_rho]F19 as numerator/denominator and chi_tau(rho). The289 terms sum exactly to2. This is fresh arithmetic using the inherited character algorithm; no new independent character implementation or finite plethysm count is claimed.

## Actual determinant points and normalization

For each of two stored lists A0,...,A7 of integral traceless4x4 matrices, construct

    f(s0,x)=det(s0*I + sum_i x_i*A_i).

Every matrix entry is saved in `results/b16_09/certificate.json`; seeds160900 and160901 are provenance, not substitutes for the saved inputs. Each polynomial is independently expanded over the24 determinant permutations using integer ordinary coefficients. The s0^4 coefficient is1 and every s0^3*x_i coefficient is0. Thus its degree2,3,4 forms already lie in the depressed chart and come from the same determinant.

The nine directions I,A0,...,A7 are linearly independent. Greedy completion by stored matrix units gives full16x16 integer frames of determinants -120 and -9366. These define actual GL16 determinant orbit points. Their restrictions to the first nine variables are the polynomials evaluated here. The nine-variable highest-weight functions depend only on this restriction. No dimension of a restricted parameter family is used as geometric rank.

For ordinary coefficient p_alpha, the tensor entry is p_alpha/(d!/product alpha_i!). All denominators divide24. The integer path evaluates the scaled tensors Q'=24Q,R'=24R,S'=24S. B scales by24^9 and H by24^8. This scaling is removed exactly using rational arithmetic; it is not a source-dimension argument.

## Independent evaluation identity

The primary path reuses the inspected B15-08 signed finite-difference determinant formula. A second path uses the following identity on invertible Q'. Write

    C_k=(R'(ei,ej,ek))_ij,
    E_k=(S'(ei,ej,ek,e0))_ij,
    u_k=Q'(e0,ek), k=0,1,
    L(X)=tr(Q'^(-1)*X),
    M(X,Y)=L(X)*L(Y)-tr(Q'^(-1)*X*Q'^(-1)*Y).

Then

    B=7!*det(Q')*(u0*L(C1)-u1*L(C0)),
    H=6!*det(Q')*(M(C0,E1)-M(C1,E0)).

To derive these, expand C as (e0,e1)-(e1,e0). In B, the labelled coefficient of seven copies of Q' and one copy of Ck is7!*det(Q')*L(Ck). In H, the corresponding coefficient of six copies of Q', Ck and El is6!*det(Q')*M(Ck,El). These are the first and mixed second derivative formulas for a determinant. This is a rational matrix calculation with exact cancellation to integers on the two points, independently checking the finite-difference evaluation, signs, and factorials. The inverse is only an evaluation device on these points, not a premise for global polynomiality.

## Saved arithmetic and rank conclusion

The actual unscaled source evaluation matrix, with rows(B,H) and columns(point0,point1), is

    [ -805005139365/8       -39873415834035/4 ]
    [ 1042617902945/16       -211528414305/32 ].

Its determinant is

    166461230261179373415548625 / 256 != 0.

The independently computed integer matrix on24-scaled tensors is

    [ -265833580886691120414720   -26334472651210174192680960 ]
    [ 7172905827012071915520      -727626770680436490240 ].

Its determinant is189088119961154504262176953411728814041464832000, equal to24^17 times the rational determinant above. Fresh reconstruction using the original B15-08 polynomial implementation gives

| Prime | Unscaled matrix | Minor |
|---|---|---|
| 2147483647 | [[1111395356,802001777],[873327252,1912562777]] | 227593281 |
| 2147483629 | [[574523596,1875660031],[68021430,167732257]] | 2131745150 |

Both modular ranks are2. Full polynomial coefficients, tensors, source rows, frames, and all289 character summands are retained. Direct4x4 determinant evaluation also checks each integer polynomial at three prescribed arguments. The receiver reconstructs these objects instead of trusting stored evaluations and rejects altered evaluation and native-point entries.

Because these two highest-weight polynomials are independent on the determinant orbit, m_det>=2. The exact ambient upper bound is2, so m_det=a=2 and i_det=0. For genuine independent ten-variable padding z*per3, the coordinate multiplicity always satisfies m_pad<=a. Therefore D<=0 without making or needing any claim that nine variables parametrize the padding family. No padding point is modified, substituted, or evaluated in this work.

## Limits and next sufficient witness

The assigned geometric completion is finished. No global determinant equation candidate remains in this two-dimensional space. The conclusion is conditional only on the named characteristic-zero highest-weight and stable-space identification conventions, with their source proof preserved. The exact matrix evaluation itself is unconditional rational arithmetic on saved determinant pencils.

No value of m_pad or exact D is obtained. An exact gap would additionally require a certified padding image rank (for example a genuine z*per3 rank2 witness would give D=0 here). No further witness is needed for this cell's exclusion of positive D. Other tails, degrees below19, shared theorem files, and B15 evidence were not changed.
