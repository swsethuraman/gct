# Subdivided expander tableaux survive on actual padding

Date: 2026-09-21. Producer: Astra integrator, current task.
Status: HAND PROOF / PRODUCER ONLY / PENDING INDEPENDENT REVIEW.

Follow-up: [DETERMINANT_REJECTION.md](DETERMINANT_REJECTION.md) now gives an
explicit determinant pencil with exactly the same positive evaluation. Thus
padding survival stands, but every individual function in this family is
rejected as a determinant equation, subject to independent review.

Outcome: affirmative, for every member of the subdivided family, at n=4 and
n=5. The same argument works for the singleton-completed family at every n>=4.
This is a padding-nonvanishing certificate, NOT a determinant equation or an
obstruction. No mathematical programs or pilots were run; no compute lease,
Git mutation, paper change, or new research task was needed.

## 1. Binding and statement

The tableau is precisely the subdivided construction in sections 5--6 of
CONSTRUCTION_AND_LIMITATIONS.md in this directory. That input's SHA-256 before
adding the follow-up pointer was:

    67d3d1ccfee0c6b1a3e3f1c3f909de2b37f0bdd988e850f506a5d34f5508a1d1

Let H be the simple 5-regular seed graph with 2k vertices and 5k edges. The
subdivision has 10k half-edge labels. Duplicate every incident-label column,
then add n-4 singleton columns per label. Let f_(H,n) denote its BDI tableau
function, with equation degree d=10k and weight

    ((10n-26)k,14k,4k,4k,4k).

Define

    z=x1+i*x2,  w=x1-i*x2,
    A=x1^2+x2^2=z*w,
    B=x3^2+x4^2+x5^2,  Q=A+B,
    p_n=z^(n-3)*w*Q.

The point p_n is an ACTUAL linear restriction of padded per_3, not merely a
point of a larger product locus. We prove

    f_(H,n)(p_n)
       = (12800/6561)^k * alpha_n^(4k) * beta_n^(6k) * Z_H,

where

    alpha_n=12/[n(n-1)],
    beta_n=24/[n(n-1)(n-2)],
    Z_H=sum_F 2^(number of cycles of F) / 40^(number of edges of F).

The sum includes every subgraph F of H that is a disjoint union of
vertex-disjoint simple cycles, including the empty subgraph, whose term is 1.
In particular Z_H>=1. Every quantity on the right is positive for n>=4.
This is an exact finite combinatorial formula and a strict lower bound; no
enumeration of cycles is needed to establish nonvanishing.

The formula applies even when H is not bipartite or expanding. Those
properties are not needed for the certificate.

## 2. An explicit padded-permanent substitution

All substitutions below are over Q(i). Write column vectors

    a=(x1+i*x2, x3+i*x4, x5)^T,
    c=(x1-i*x2, x3-i*x4, x5)^T,
    M=J_3-I_3,
    b=(-I_3+J_3/2)c.

Here J_3 is the all-ones matrix. Direct multiplication gives
M^(-1)=-I_3+J_3/2, and hence a^T M b=a^T c=Q.
Use the 3x3 matrix of linear forms

    Y = [ a1 a2 a3
          b1 b2 b3
           w  w  w ].

Its permanent is

    per_3(Y)=w*sum_(i!=j) a_i b_j=w*a^T M b=w*Q.

Set the independent padding coordinate equal to z. Then

    (padding coordinate)^(n-3) * per_3(Y)=p_n.

This specifies all nine matrix entries and the padding coordinate. It uses
only five input variables and lies in the actual parameterized image, so no
orbit-closure or cubic-universality premise is required. At n=4 the resulting
point p_4=A(A+B) even has rational real coefficients. The representation over
Q(i) is legitimate for the project's characteristic-zero complex loci.

## 3. Tensor convention and the quartic contraction

Use the symmetric tensor corresponding to a polynomial under normalized
symmetrization: an x1^2*x2^2 coefficient c corresponds to tensor entries
q_1122=c/6. Equivalently q(x)=sum q_ijkl*x_i*x_j*x_k*x_l.

The source of the tableau evaluation convention is BDI, arXiv:2002.11594v2,
section 5, equation (5.2). Normalized symmetric products and the derivative
factor are stated in section 5 and Lemma 6.5. These passages were checked
directly in the primary PDF in this task:
https://arxiv.org/pdf/2002.11594
The tensor contraction below is the multilinear version of that evaluation;
it agrees on sums of pure powers and therefore on all symmetric tensors.

First consider the real quartic

    q=alpha*A^2+beta*A*B,  alpha,beta>0.

At every half-edge label, two tensor legs go to the paired height-five
columns at an old vertex, and two go to the paired height-two columns at the
subdivision vertex. Let i,j in {1,...,5} index the first pair and a,b in {1,2}
the second. The local tensor is q_ijab.

Use this orthonormal basis of real symmetric 2x2 matrices:

    E0=I_2/sqrt(2),
    E1=diag(1,-1)/sqrt(2),
    E2=[[0,1],[1,0]]/sqrt(2).

Set M_r(i,j)=sum_(a,b) q_ijab E_r(a,b). Since q is symmetric in a,b,
q_ijab=sum_r M_r(i,j)E_r(a,b).

Writing U=span(e1,e2), V=span(e3,e4,e5), direct coefficient extraction gives

    M0=diag(a0*I_2,c0*I_3),
    M1=diag(b0*diag(1,-1),0_3),
    M2=diag(b0*[[0,1],[1,0]],0_3),

where

    a0=4*alpha/(3*sqrt(2)),
    b0=2*alpha/(3*sqrt(2)),
    c0=beta/(3*sqrt(2)).

For example q_1111=q_2222=alpha, q_1122=alpha/3, and
q_jj11=q_jj22=beta/6 for j=3,4,5; terms with an odd number of V indices vanish.

## 4. Edge signs and vertex weights

The two height-two columns at a subdivision vertex contract the endpoint
matrices with epsilon_ac epsilon_bd. In the E0,E1,E2 basis their bilinear
form is diagonal:

    K_rs=sum_(a,b,c,d) E_r(a,b) E_s(c,d) epsilon_ac epsilon_bd
         =diag(1,-1,-1)_rs.

Thus each original edge of H must have the same colour r at both ends and
contributes sigma_0=1 or sigma_1=sigma_2=-1. No factors of two are omitted:
E2 has BOTH off-diagonal entries 1/sqrt(2), and the sums use ordered indices.

At an old vertex with five incident colours r1,...,r5 the paired height-five
columns give the symmetric tensor

    R(r1,...,r5)=sum_(i1,...,i5,j1,...,j5)
                  epsilon_(i1...i5) epsilon_(j1...j5)
                  product_(h=1)^5 M_(rh)(ih,jh).

Its generating polynomial is

    sum_(r1,...,r5) R(r1,...,r5) y_(r1)...y_(r5)
       =5! det(y0*M0+y1*M1+y2*M2)
       =120*c0^3*y0^3*[a0^2*y0^2-b0^2*(y1^2+y2^2)].

Consequently there are only three kinds of nonzero vertex assignments:

* All five edges have colour 0: R0=120*a0^2*c0^3.
* Exactly two edges have colour 1, the rest 0: R1=-12*b0^2*c0^3.
* Exactly two edges have colour 2, the rest 0: the same R1.

The factor 12 is 120/binomial(5,2). In particular

    R0=160*alpha^2*beta^3/(81*sqrt(2)),
    R1/R0=-1/40.

Both paired columns use the same ordering, so changing that ordering creates
two cancelling determinant signs. This prevents an orientation-dependent
overall sign in the formula.

## 5. The positive cycle sum

A surviving assignment of colours to edges therefore consists of a
vertex-disjoint union F of cycles of nonzero colours. Each cycle is uniformly
colour 1 or uniformly colour 2, giving two choices per cycle.

Every active vertex contributes R1/R0=-1/40. Every active edge contributes -1.
Since |V(F)|=|E(F)|, these signs cancel:

    (-1/40)^|V(F)| * (-1)^|E(F)|=40^(-|E(F)|).

This argument works for odd cycles as well as even cycles. Bipartiteness,
though available in our expander seeds, is unnecessary here.

Summing the network contraction gives exactly

    f_(H,4)(alpha*A^2+beta*A*B)=R0^(2k)*Z_H
       =(12800/6561)^k * alpha^(4k)*beta^(6k)*Z_H.

The empty cycle configuration has positive weight R0^(2k); all other
surviving configurations also have positive weight. Hence there is no
cancellation, and the evaluation is strictly positive. Taking alpha=beta=1
proves survival on the actual quartic padding p_4 from section 2.

## 6. Quintics and the general singleton completion

Each singleton column fixes its tensor leg to coordinate 1. For n>=4 let
m=n-4. Contracting these m legs at every label replaces p_n by the quartic

    q_n= [4!/n!] * (partial/partial x1)^m p_n,
    f_(H,n)(p_n)=f_(H,4)(q_n).

There is no extra global constant: 4!/n! is precisely the normalized tensor
contraction factor, and is applied inside q_n at every label.

Since z=x1+i*x2 and w=x1-i*x2, partial_x1=partial_z+partial_w and

    p_n=z^(m+2)*w^2+z^(m+1)*w*B.

Under z->t*z, w->t^(-1)*w, with V fixed, the terms of q_n have weights
0,2,4, all nonnegative. The weight-zero part, obtained by taking every
derivative in z, is

    q_n,0=alpha_n*A^2+beta_n*A*B,
    alpha_n=12/[n(n-1)],
    beta_n=24/[n(n-1)(n-2)].

The displayed substitution is an SL2 change of the first two coordinates.
Every column of the quartic tableau has height 2 or 5, so its determinant
is unchanged by this change of coordinates. Therefore f_(H,4) is invariant
under it. Taking the polynomial limit t->0 gives

    f_(H,4)(q_n)=f_(H,4)(q_n,0).

Section 5 proves the claimed formula and positivity for every n>=4.

Explicitly at n=5,

    q_5=(1/5)*partial_x1[p_5]
       =(3/5)*A^2+(2/5)*A*B+(1/5)*z^2*(2*A+B),

and the last term has positive weight 2 and disappears in this limit. Thus

    f_(H,5)(p_5)
       =(3/5)^(4k)*(2/5)^(6k)*f_(H,4)(p_4)>0.

## 7. Certificate, limits, and next question

For the first seed H=K_(5,5), k=5 and equation degree d=50. We have the exact
strict lower bounds

    f_(H,4)(p_4) >= (12800/6561)^5 > 0,
    f_(H,5)(p_5) >= (12800/6561)^5*(3/5)^20*(2/5)^30 > 0.

No floating-point evaluation, sampled rank, or uncomputed equality is being
used as evidence. These inequalities follow from the exact contraction and
the empty term of a finite sum with positive terms. We have not enumerated
Z_H or claimed a numerical value for the full evaluation.

This upgrades the subdivided family's padding restriction from open to a
producer-proved NONZERO result. It establishes actual padding survival,
not merely survival on arbitrary linear-times-cubic forms. It neither proves
nor assumes determinant-ideal membership. A nonzero value on padding is
necessary for separation, not sufficient.

Expansion is absent from the proof. The certificate would work on any simple
5-regular seed graph with 2k vertices. It therefore does not establish that
expanders are better separators than nonexpanders. It also does not make the
full degree-50 cells cheap to compute.

Independent review should check the six-term permanent substitution, the
normalized tensor entries, the signed edge metric, the factor 120/10 at a
vertex, and the SL2/derivative reduction. Those are the load-bearing steps.
This task has no independent reviewer; no accepted batch status is changed.

The next mathematical certificate is determinant-side: either an exact
determinant pencil where this function is nonzero (rejecting it as an equation),
or a symbolic identity proving it vanishes on all determinant pencils.
No determinant search or empirical comparison was run as part of this task.
