# Exact determinant witness rejects the subdivided family

Date: 2026-09-21. Producer: Astra integrator, current task.
Status: HAND PROOF / PRODUCER ONLY / PENDING INDEPENDENT REVIEW.

Outcome: every individual function f_(H,n) of the subdivided family is NONZERO
on an explicit size-n determinant pencil, for n=4, n=5, and indeed all n>=4.
It therefore is not a determinant equation and cannot be a separator.

The determinant witness has exactly the same evaluation as the actual padding
witness from PADDING_SURVIVAL.md. This is a structural blindness certificate,
not a failed numerical search. No mathematical programs, pilots, compute lease,
Git mutations, or changes to accepted batch records were used.

## 1. Inputs and conventions

The family is defined in CONSTRUCTION_AND_LIMITATIONS.md, section 5, with
equation degree d=10k for a simple 5-regular seed graph H on 2k vertices.
Each half-edge label has two occurrences in height-five columns, two in
height-two columns, and n-4 occurrences in singleton columns.

The source of its exact positive padding evaluation is PADDING_SURVIVAL.md,
whose SHA-256 before adding the follow-up pointer in this task was

    6bfebc9b913377664919bde1eaa9f652748745659016b31749b988dff5ec4ca4

Its proof is producer-only, not an independently accepted premise. The
normalization, contraction and positivity arguments are used as stated there.

Write

    z=x1+i*x2,  w=x1-i*x2,
    u=x3+i*x4,  v=x3-i*x4,  t=x5,
    A=zw=x1^2+x2^2,
    B=uv+t^2=x3^2+x4^2+x5^2.

The actual padding witness was

    p_n=z^(n-4)*A*(A+B).

Its explicit padded-permanent parameterization is retained in section 2 of
PADDING_SURVIVAL.md. No larger product locus is substituted for actual padding.

## 2. Explicit determinant pencils

Consider the skew-symmetric matrix of linear forms over Q(i):

    K = [    0     z    u/2   t/2
            -z     0     t    -v
          -u/2    -t     0     w
          -t/2     v    -w     0 ].

For a 4x4 skew-symmetric matrix with upper-triangular entries a,b,c,d,e,f in
positions 12,13,14,23,24,34, direct determinant expansion gives

    det K=(af-be+cd)^2.

For this K the expression inside the square is

    zw-(u/2)*(-v)+(t/2)*t=A+B/2.

Thus, without approximation,

    D_4=det K=(A+B/2)^2=A^2+A*B+B^2/4.

For n>=4 take

    M_n=diag(K,z*I_(n-4)),
    D_n=det M_n=z^(n-4)*(A+B/2)^2.

At n=4 the extra block is empty; at n=5 it is the single entry z. All entries
are homogeneous linear forms in the same five variables. Therefore D_n lies
in the actual determinant-pencil image, not just its closure.

The coefficient matrix of x1 is diag(J,J,I_(n-4)), where
J=[[0,1],[-1,0]]. It is invertible with determinant 1. Multiplying M_n on the
left by its inverse produces a normalized pencil x1*I+sum_(j=2)^5 xj*A_j
without changing its determinant. The witness therefore also belongs to the
project's normalized determinant chart.

The difference from the padding witness is exactly

    D_n-p_n=(1/4)*z^(n-4)*B^2.

## 3. The invisible direction

First consider quartics. In every tableau label, two legs are contracted by
the height-two columns. Those columns use only coordinates 1 and 2. Hence the
function depends on a quartic q only through tensor entries

    q_ijab,  i,j in {1,...,5}, a,b in {1,2}.

A quartic h involving only x3,x4,x5 has h_ijab=0 for every such entry. In the
multilinear contraction, replacing any copy of q by h gives zero. Expanding
the contraction on (q+h) at all labels therefore proves the exact identity

    f_(H,4)(q+h)=f_(H,4)(q)

for EVERY quartic q and every h in Sym^4(span(x3,x4,x5)). This is not a
linearization or first-order statement.

Apply this with q=p_4 and h=B^2/4. It gives

    f_(H,4)(D_4)=f_(H,4)(p_4).

For n>=4 set m=n-4. The singleton columns contract m legs at each label to
coordinate 1, leaving the normalized quartic tensor

    C_n(q)=(4!/n!)*partial_x1^m(q),
    f_(H,n)(q)=f_(H,4)(C_n(q)).

Since partial_x1(z)=1 and B is independent of x1,

    C_n(D_n-p_n)= [4!*m!/(4*n!)]*B^2
                = B^2/[4*binomial(n,4)].

This again lies in the invisible quartic subspace. Consequently

    f_(H,n)(D_n)=f_(H,n)(p_n)  for every n>=4.

One can also see the vanishing directly: the difference z^m B^2 has only m
legs in the first two coordinates. A nonzero contraction would need all m
singleton legs PLUS the two height-two legs in those coordinates. There are
not enough. The derivative argument above fixes the precise normalization.

## 4. Exact nonzero determinant evaluation

For reference, the established contraction in PADDING_SURVIVAL.md yields

    f_(H,n)(p_n)
      = (12800/6561)^k * alpha_n^(4k) * beta_n^(6k) * Z_H,

where

    alpha_n=12/[n(n-1)],
    beta_n=24/[n(n-1)(n-2)],
    Z_H=sum_F 2^(number of cycles of F)/40^(number of edges of F).

Here F ranges over unions of vertex-disjoint simple cycles of H, including
the empty configuration. The empty term is 1 and every term is positive.

The essential local checks behind that formula are: the height-two edge
metric is diag(1,-1,-1); the height-five vertex permits either all-zero
edge colours with weight R0, or two equal nonzero colours with weight
-R0/40; and every nonzero-colour edge has weight -1. The signs cancel on
each cycle. For q=alpha*A^2+beta*A*B,
R0=160*alpha^2*beta^3/(81*sqrt(2)). The normalized singleton derivative and
an SL2 limit give the alpha_n and beta_n above.

Combining this positive formula with section 3 gives the determinant-side
certificate

    f_(H,n)(det M_n)
      = (12800/6561)^k * alpha_n^(4k) * beta_n^(6k) * Z_H > 0.

For each individual f_(H,n), this is an exact nonmembership witness for the
ideal of the size-n determinant-pencil closure.

## 5. A fully specified scalar for the degree-50 base candidate

For H=K_(5,5), k=5, d=50. Its cycle sum has only the following possibilities:
one cycle of length 4,6,8,10; two cycles of lengths 4+4 or 4+6; or none.

The number of unoriented simple cycles of length 2r in K_(5,5) is

    binomial(5,r)^2 * r!*(r-1)!/2.

Choose its r vertices on each side, then order the alternating cycle, dividing
by rotations and reversal. This gives respectively 100,600,1800,1440 cycles.
The number of disjoint pairs of 4-cycles is 100*9/2=450. The number of
disjoint 4-cycle/6-cycle pairs is 100*6=600. These counts exhaust all cases,
because every cycle uses at least two vertices from each side.

Including the two colour choices per cycle,

    Z_0=1+200/40^4+1200/40^6+5400/40^8+5280/40^10.

Thus the two base-candidate evaluations are the explicit positive rational
numbers

    f_(K55,4)(det K)=(12800/6561)^5*Z_0,

    f_(K55,5)(det diag(K,z))
       =(12800/6561)^5*(3/5)^20*(2/5)^30*Z_0.

These exact rational expressions were derived by hand; no floating-point
value, numerical evaluation, or machine verification is claimed.

## 6. Scope of the rejection and research consequence

Rejected: every INDIVIDUAL member of this subdivided paired-column family as
a determinant equation, at n=4 and n=5 and its n>=4 singleton completions.
This holds regardless of expansion, using one common determinant witness at
each n. The preceding padding nonvanishing result remains valid.

Not rejected: arbitrary expander-based tableaux, constructions with different
column arrangements, or linear combinations of the current functions. A
linear combination could cancel on this particular determinant witness; its
membership must be tested separately. All such combinations remain equally
blind to the invisible direction in section 3, so this padding point would
not witness their separation if they vanished on its matching determinant.

The concrete lesson is that many contractions on a large connected graph can
still depend on a restricted portion of the coefficient tensor. Here adding
the unseen quartic B^2/4 completes the padding witness to an exact determinant.
Expansion does not repair that loss of information.

No further search is recommended for the individual members of this family.
A redesigned family would need to detect directions currently invisible to
the height-two contractions, or establish useful cancellation in a span.
Neither possibility is proved or launched here.

Independent review should verify the explicit matrix determinant, the
normalized-chart inclusion, the invisible-direction identity, and the positive
cycle-sum normalization inherited from PADDING_SURVIVAL.md. This remains a
producer proof; no independently accepted programme status is changed.
