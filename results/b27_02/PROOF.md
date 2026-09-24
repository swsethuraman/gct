# One mixed-sign contraction passes the two squares and fails a third determinant

All mathematical definitions and deductions in this file are **HAND** unless a
paragraph explicitly says **READ** or **COMPUTED**. This heading applies locally
to the displayed formulas within each HAND paragraph; computations are also
identified individually. No external theorem or uncommitted mathematical text
is a premise. Work over C, with rational coefficients in the function f.

## 1. The one candidate (rung 2a)

**READ.** A26-03 `f7967d17:results/a26_03/PROOF.md` fixes the tensor convention;
B26-10C `a7b7c19f:docs/b26_10c_review.md`, section 2.4, gives the corrected
mixed-sign reopening rule. Full commit, blob ID, byte count and raw blob SHA-256
are in INPUT_BINDINGS.json. These are committed payload bytes, not worktree text.

**HAND.** For a quartic q, write

    q(x) = sum_{i,j,k,l=1}^5 q_ijkl x_i x_j x_k x_l.

Thus q_1122 is one sixth of the coefficient of x1^2 x2^2. A height-h column is
the alternating tensor on coordinates 1,...,h with epsilon_(1,...,h)=1.
Contract one copy of q at each label. Divide by no column, label, or row
factorials. Repeated columns below have the same displayed order.

**HAND.** There are ten labels, each of content four. Define two fillings:

| tableau | height-five columns | singleton columns |
|---|---|---|
| T1 | four copies of (1,2,3,4,5) | four copies of (j) for each j=6,...,10 |
| T2 | two copies of (1,2,3,4,5), two of (6,7,8,9,10) | two copies of (j) for every j=1,...,10 |

**HAND.** Both have four height-five and twenty height-one columns. Their common
shape is lambda=(24,4,4,4,4), size 40; n=4 and coefficient degree d=10.
Every column has distinct labels. No semistandardness is required or claimed.
The candidate, including its normalization and exact coefficients, is

    f = f_T1 - 567 f_T2.                                      (1)

Both tableaux are fully paired in the same orientation; the effective
coefficients +1 and -567 have mixed sign. This satisfies the reopening gate.
There is only one candidate in this packet.

**HAND.** For compact evaluation set

    a(q) = q_1111,       C(q)_ij = q_11ij,
    H(q) = 5! det C(q),
    F(q) = contraction of five labels with four columns (1,2,3,4,5).

The tensor at each of the five labels in H has two singleton legs, leaving C
on the other two legs. The double-epsilon formula is 5! det C, with no hidden
normalization. Disjoint label sets multiply. Therefore

    f_T1(q) = a(q)^5 F(q),  f_T2(q) = H(q)^2,
    f(q) = a(q)^5 F(q) - 567 H(q)^2.                          (2)

**HAND.** Top-coordinate minors are fixed by lower-unitriangular changes of
evaluation vectors. A diagonal change multiplies either tableau function by
t1^24 t2^4 t3^4 t4^4 t5^4. Equation (1) is therefore a highest-weight function
in this tensor convention as soon as it is nonzero; section 4 proves it is.
This is a direct argument, not a source-condition theorem about determinants.

## 2. A short exact evaluation of F(Q^2)

**HAND.** Put A=x1^2+x2^2, B=x3^2+x4^2+x5^2 and Q=A+B. At Q^2 the quartic
tensor is

    q_ijkl = (delta_ij delta_kl + delta_ik delta_jl
              + delta_il delta_jk)/3.

In the four-column epsilon expansion of F, simultaneous permutation of the
five coordinate values preserves the tensor and multiplies four epsilons by
the fourth power of its sign. Fix the first column to the identity and multiply
by 5!. Call the second column sigma. If sigma(i) != i, the remaining indices
must be (i,sigma(i)) or (sigma(i),i), each with scaled tensor entry 1. On each
nontrivial cycle of sigma the third column must choose consistently one of the
two options; otherwise it repeats a coordinate. The fourth column takes the
complementary option. If sigma fixes k labels, the third column permutes those
labels by some tau and the fourth column equals tau there. An entry with all
four indices equal has scaled weight 3; the other permitted entries have
weight 1. The product of the four column signs is +1 in every permitted case.

**HAND.** Set a_k=sum_{tau in S_k} 3^{fix(tau)}. Marking any chosen subset of
fixed points in (1+2)^{fix(tau)} gives

    a_k = k! sum_{j=0}^k 2^j/j!.

The integer sum after fixing the first column is consequently the following
finite calculation. The final column includes both the multiplicity of sigma
and the contribution from its nontrivial cycles and fixed points.

| cycle type of sigma | number | contribution |
|---|---:|---:|
| 1^5 | 1 | a5 = 872 |
| 2,1^3 | 10 | 10 * 2 * a3 = 760 |
| 2^2,1 | 15 | 15 * 4 * a1 = 180 |
| 3,1^2 | 20 | 20 * 2 * a2 = 400 |
| 3,2 | 20 | 20 * 4 * a0 = 80 |
| 4,1 | 30 | 30 * 2 * a1 = 180 |
| 5 | 24 | 24 * 2 * a0 = 48 |
| total | 120 | 2520 |

**HAND.** Reinstating the first column and tensor denominators gives

    F(Q^2) = 120 * 2520 / 3^5 = 11200/9.                    (3)

This derivation does not assume a Gaussian integral, an invariant-theory
dimension formula, or a computationally guessed constant.

## 3. The two known determinants (rung 2c)

**READ.** The committed A26-03 proof, section 3, supplies K_Q; B26-02 at
`cdf6839c:docs/b26_02_review.md`, item 5, supplies D4. For completeness the
identities are replayed here by hand rather than merely inherited.

**HAND.** Set z=x1+i*x2, w=x1-i*x2, u=x3+i*x4, v=x3-i*x4 and t=x5. Then
zw=A and uv+t^2=B. A skew 4-by-4 matrix with upper entries
(k12,k13,k14,k23,k24,k34) has determinant
(k12*k34-k13*k24+k14*k23)^2, as direct expansion shows. The respective choices

    (z,u,t,t,-v,w),       (z,u/2,t/2,t,-v,w)

give Q^2 and D4=(A+B/2)^2. In both pencils the x1 coefficient is diag(J,J),
J=[[0,1],[-1,0]], of determinant one. Left multiplication by its inverse puts
the pencil into the x1 I4 chart without changing the determinant.

**HAND.** For q=alpha A^2+beta AB+gamma B^2,

    a=alpha,     C=diag(alpha,alpha/3,beta/6,beta/6,beta/6).

Consequently H(Q^2)=40/27, while H(D4)=H(p4)=5/27 for p4=A(A+B).
The diagonal substitution g=diag(1,1,1/sqrt(2),1/sqrt(2),1/sqrt(2)) sends
Q^2 to D4. Since F has four full columns, F(q(gx))=det(g)^4 F(q), and hence

    F(D4)=F(Q^2)/64=175/9.

**HAND.** The coefficient 567 in (1) was chosen exactly as

    F(Q^2)/H(Q^2)^2 = (11200/9)/(1600/729) = 567.

Both prescribed evaluations therefore vanish:

    f(Q^2) = 11200/9 - 567*(40/27)^2 = 0,
    f(D4)  =   175/9 - 567*(5/27)^2 = 0.                    (4)

**HAND.** These are not independent vanishing tests for any fixed-weight
candidate: if g has weight lambda, then
g(D4)=2^{-(lambda3+lambda4+lambda5)/2} g(Q^2).
For the present shape this factor is 1/64. This observation does not say that
passing either test proves a determinant identity.

## 4. Visibility and actual padding (rungs 2b and 2d)

**READ.** B26-02, item 3, identifies the literal actual-padding point p4.
The following explicit substitution replays that membership. At entry to rung
2d the b27-01 ref was still the setup commit with no b27_01 payload, so the
brief's fallback is p4; no uncommitted B27-01 work is used.

**HAND.** With the linear forms above, let r=(z,u,t)^T, s=(w,v,t)^T,
M=J3-I3, where J3 is the all-ones matrix, and b=(-I3+J3/2)s. Since J3^2=3J3,
M(-I3+J3/2)=I3. Let Y have rows r^T, b^T and (w,w,w). Summing its six
permanent terms gives

    per_3(Y)=w sum_{i != j} r_i b_j = w r^T M b
            = w(zw+uv+t^2)=wQ.

Taking padding coordinate z gives z per_3(Y)=zwQ=p4. All ten input coordinates
are linear forms, so this is actual padding, not merely the product locus.
The matrix Y is nonsymmetric. The witness's cubic wQ is reducible; no smooth-
cubic exclusion or symmetric-permanent premise is invoked.

**HAND.** F vanishes on any quartic with a linear factor. Indeed, if q=lC,
its symmetric tensor is a sum of terms placing l in one of its four legs.
In every term of the expansion at five labels, five copies of the same l
must enter four alternating columns. Some column contains l twice and is
zero. In particular F(p4)=0. A second check specific to p4 is that it has at
most two indices from {3,4,5} per nonzero tensor entry, while F requires twelve
such indices across five labels, exceeding ten.

**HAND.** Equations (2) and (4) now give

    f(p4) = -567*(5/27)^2 = -175/9 != 0.                    (5)

For the ambient visibility certificate take q=p4 and direction B^2 in
Sym^4(span(x3,x4,x5)). The exact two endpoints are

    f(q+0*B^2)=-175/9,       f(q+(1/4)*B^2)=f(D4)=0.

Thus t -> f(q+t B^2) is nonconstant. Rung 2b does not rely on a numerical
approximation or on a mere indication from the columns. Rung 2d was performed
only after the hand calculation (4) passed rung 2c. Rung 2b uses these same
endpoints solely as an ambient calculation; its membership interpretation is
the additional conclusion in rung 2d.

## 5. The determinant-side question is answered negatively

**HAND.** A universal identity would have to prove

    a(det(sum x_i M_i))^5 F(det(sum x_i M_i))
       - 567 H(det(sum x_i M_i))^2 = 0                     (6)

as a polynomial in all 80 matrix entries M_i, or equivalently establish its
vanishing on every literal 4-by-4 linear pencil and hence its closure.
Checking the two squares is insufficient. Equation (6) is false even in
the normalized chart, at the completely specified pencil

             [ x1   0    0     x3   ]
    L_E(x) = [  0  x1    0     x4   ].
             [  0   0   x1     x5   ]
             [ x3  x4   x5   x1+x2  ]

**HAND.** Expansion along the last row, or the adjugate of x1 I3 as a polynomial
identity, gives

    E=det L_E=x1^4+x1^3*x2-x1^2 B=x1^2(x1^2+x1*x2-B).

The x1 coefficient matrix is I4. F(E)=0 by its linear factor, while

    C(E) = [[1,1/4],[1/4,0]] direct_sum diag(-1/6,-1/6,-1/6),
    det C(E)=(-1/16)*(-1/216)=1/3456,
    H(E)=5/144,
    f(E)=-567*(5/144)^2=-175/256 != 0.                      (7)

Thus the sole candidate is rejected as a determinant equation. This is a
literal exact counterexample, not an unproved suspicion about (6).

**HAND.** More strongly, this entire two-dimensional span contains no nonzero
determinant equation. Put u=a^5F, v=H^2. Their evaluations at Q^2 and E form

    [[11200/9, 1600/729],
     [      0, 25/20736]],

whose determinant is 4375/2916 != 0. Any c*u+d*v vanishing on all determinants
must have c=d=0. This is a scoped obstruction for this explicit span, not for
all mixed-sign contractions or all functions of this highest weight.

## 6. Exact replay and scope

**COMPUTED.** The two sequential runs in run01_output.json and run02_output.json
verify every value in the table below using installed Python integers and
Fraction. No floating-point arithmetic enters a mathematical value.

| quartic | F | H | f |
|---|---:|---:|---:|
| Q^2 | 11200/9 | 40/27 | 0 |
| D4 | 175/9 | 5/27 | 0 |
| p4 | 0 | 5/27 | -175/9 |
| E | 0 | 5/144 | -175/256 |

**COMPUTED.** Run 1 enumerates the epsilon contraction after quotienting the
first-column choices by S2 x S3 (10 representatives, at most 144000 triples
per even quartic). Run 2 enumerates all 120 first-column permutations, at most
1728000 triples per even quartic, without that symmetry reduction. For even
quartics the fourth index at every label is forced by the first three, and
non-permutations are discarded exactly. Each run expands the extra pencil's
24 determinant terms, checks F(E)=0 by the explicit support-capacity
certificate, evaluates the 5-by-5 determinant C by all 120 permutations, and
checks the nonzero determinant of the two-function evaluation matrix. This is
a finite certificate replay, not a random or sampled search. The two replays
share code and are not independent reviews.

**HAND.** The mathematical conclusions also have the separate derivations in
sections 1-5. The replay outputs are labelled COMPUTED, never promoted to a
universal proof on the strength of evaluations. The negative universal result
uses the exact counterexample (7).

**HAND — achievement level.** A legal, nonzero highest-weight coefficient
function; mixed-sign escape; visibility; zero on two specified determinant
points; nonzero on literal actual padding; rejection on a third determinant;
and a two-dimensional-span obstruction. No new source condition is asserted.
No determinant coefficient equation, separation on padding, positive
multiplicity gap, geometric noncontainment, or asymptotic lower bound is
established. In particular, f(p4)!=f(D4) is not separation from the determinant
variety. No conclusion about other candidates or higher form degrees follows.

**READ — standing convention:** No five-row determinant equation is known to be
nonzero on padding. The programme decision remains "no construction ready."
