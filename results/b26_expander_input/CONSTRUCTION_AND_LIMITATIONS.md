# Expander tableaux in five-row quartic and quintic cells

Date: 2026-09-21. Producer: Astra integrator, current task.
Status: HAND PROOF / PRODUCER ONLY / NOT INDEPENDENTLY REVIEWED.

Follow-up: [PADDING_SURVIVAL.md](PADDING_SURVIVAL.md) now supplies an explicit
actual-padding witness and a positive cycle-sum proof for the subdivided
family. Its formerly open padding status below is preserved as the original
construction-stage record; the follow-up supersedes that item, subject to
independent review. Determinant-ideal membership remains open.

Later follow-up: [DETERMINANT_REJECTION.md](DETERMINANT_REJECTION.md) settles
that remaining membership question negatively for every individual member:
an explicit determinant has the same positive evaluation as the padding
witness. This supersedes the open membership statements below, subject to
independent review; it does not rule out arbitrary linear combinations.

No mathematical programs, numerical experiments, compute lease, Git mutation,
paper changes, or research-task launches. This is a new research note, not an
accepted numbered batch certificate. No claim of literature novelty.

## 1. Answer and scope

Yes: there is an algorithmically specified infinite family of admissible,
nonzero, five-row tableau functions at form degrees n=4 and n=5 whose tableau
graphs are bounded-degree expanders. A fixed rational form is an exact
nonvanishing witness for every member. The construction uses doubled columns,
an idea already present in BDI's graph-colouring reduction, adapted here to
incidence graphs and the project's small form degrees.

The first, unsubdivided construction is identically zero on padding. A modified
construction passes the elementary padding-capacity condition, but its
nonvanishing on actual padding and its determinant-ideal membership are BOTH
unresolved. It is not an obstruction.

Expansion supplies a separator/treewidth statement. Nonvanishing follows from
column pairing and an explicit colouring, without using expansion. No theorem
connecting expansion itself to determinant separation is established here.

## 2. Conventions and sources

Work over C, using real rational points for positivity certificates. Form
degree is n, equation degree is d, and r=5 variables are used. A filling T has
content d x n: labels 1,...,d occur n times each. Its columns, ordered by
nonincreasing height, define a partition lambda of nd. Its graph has labels as
vertices; distinct labels sharing a column are adjacent. Multiple columns do
not create multiple graph edges.

For p=sum_j ell_j^n, use the BDI normalization

    f_T(p) = sum_phi product_columns c det(top |c| coordinates
                                        of ell_{phi(a)}, a in c).

This defines a polynomial in p. For any such filling it is a highest-weight
function of shape lambda if nonzero: an upper-unitriangular change in the
representation acts by a lower-unitriangular change on the evaluation vectors,
preserving each top-coordinate determinant; a diagonal change gives weight
lambda. Semistandardness is NOT required for this construction. Straightening
may express it as a sum of semistandard functions, without preserving its graph.

External inputs, statements adopted rather than proofs audited in full:

* BDI, arXiv:2002.11594v2, Definition 5.1, equation (5.2), Lemma 5.4,
  Theorem 7.2; also the proof of Theorem 8.1 for prior use of doubled columns.
  Relevant PDF passages read directly in this task:
  https://arxiv.org/pdf/2002.11594
* Marcus--Spielman--Srivastava, Interlacing Families I: the existence of a
  Ramanujan-preserving 2-lift for every regular bipartite Ramanujan graph.
  https://arxiv.org/abs/1304.4132
  https://www.cs.yale.edu/homes/spielman/PAPERS/lifts.pdf
* Gima et al., spectral bound tw(G)>=N lambda_2/(Delta+lambda_2)-1.
  https://arxiv.org/abs/2404.08520

Local contextual input: work/batch15_workers/B15-02/docs/b25_04_report.md,
especially definitions, component factorization, and the surviving connected
and linear-combination cases. None of its degree floors is needed below.

## 3. A precise expander sequence

Let H_0=K_{5,5}, with bipartition L_i,R_j for i,j in Z/5Z and edge colour
c(L_i R_j)=i+j modulo 5. It is simple, connected, 5-regular, bipartite, and
Ramanujan; its nontrivial adjacency eigenvalues are zero.

Inductively order the edges of H_s lexicographically. Enumerate signings in a
fixed lexicographic order and choose the first signing whose signed adjacency
matrix A_sign satisfies

    -4 I <= A_sign <= 4 I.

These inequalities can be decided exactly, for example by the principal-minor
criterion for positive semidefiniteness of 4I +/- A_sign. Form its 2-lift:
a positive edge joins equal sheets and a negative edge joins opposite sheets.
The MSS theorem guarantees a qualifying signing. The spectrum of the lift is
the union of the old and signed spectra, by the equal-sheet/opposite-sheet
decomposition. Thus every H_s is again bipartite Ramanujan. It is connected
because no new eigenvalue 5 is introduced. Simplicity is preserved.

Retain each edge's colour on its two lifted edges. Each vertex still has one
edge of each of the five colours. Write

    k = 5*2^s,  |L(H_s)|=|R(H_s)|=k,  |E(H_s)|=5k.

The combinatorial Laplacian gap of H_s is at least 1, since its second largest
adjacency eigenvalue is at most 4.

Explicitness limitation: this is a terminating deterministic specification,
not a claim of an efficient or strongly explicit expander construction. The
exhaustive signing search has not been executed. The base instance needs no
search. An efficient explicit expander of suitable bounded degree could replace
this sequence if the Ramanujan property were not required of the seed graphs.

## 4. The direct construction: nonzero, but washed out by padding

Label the 5k edges of H_s. For every vertex of H_s, take the column consisting
of its five incident edge labels, in a fixed order, and put that column in
twice. Every label has four occurrences. For n>=4 add n-4 singleton columns
for each label.

This gives d=5k and

    lambda_direct=((5n-16)k, 4k, 4k, 4k, 4k).

In particular n=4 gives (4k)^5, and n=5 gives (9k,4k,4k,4k,4k).
The graph is the line graph of H_s. Section 6's squared-determinant argument,
using the inherited edge colouring, proves this function nonzero.

However, for ANY tableau of degree d and shape lambda,

    lambda_1 < (n-3)d  ==>  f_T(l^(n-3) C)=0

for every linear form l and cubic C. To prove this, expand the symmetric tensor
l^(n-3) C multilinearly in each of the d copies. Each term places (n-3)d
copies of the same vector l into the boxes. A nonzero alternating column can
contain at most one such copy. There are lambda_1 columns. The stated
inequality forces a zero determinant in every term. The assertion holds for
all l, not only a coordinate vector, and extends to the closure of the padded
locus. Cubics can be expanded into products of vectors, so the argument does
not require a chosen Waring decomposition of C.

Here (n-3)d=(5n-15)k exceeds lambda_1 by k. Thus every direct-family function
vanishes on all padded cubics, including actual padded-permanent restrictions.
Neither these functions nor linear combinations of them can separate padding
from determinants in the required direction. Nonzero polynomial and useful
padding test are genuinely different conditions.

## 5. The subdivided construction in the relevant form degrees

Subdivide every edge uv of H_s once, introducing a vertex m_uv. Call the
result J_s. Its vertices have degrees 5 (old vertices) or 2 (new vertices).
Its 10k edges, or half-edges of H_s, are the tableau labels. Thus d=10k.

For each vertex of J_s, put its incident-label column in twice, keeping the
same within-column order in both copies. Add n-4 singleton columns per label.
Order columns by height. There are:

    4k columns of height 5;
    10k columns of height 2;
    (n-4)*10k columns of height 1.

Each label belongs to the stars of its two endpoints, hence appears four times
before singleton completion and exactly n times afterward. No column repeats
a label. The resulting shape is

    lambda=((10n-26)k, 14k, 4k, 4k, 4k),  d=10k.

The first row is at least the second for every n>=4. The boxes total 10nk=nd.
For our two cases:

| form degree n | equation degree d | shape lambda | tail |
|---|---|---|---|
| 4 | 10k | (14k,14k,4k,4k,4k) | 26k |
| 5 | 10k | (24k,14k,4k,4k,4k) | 26k |

The smallest instance has k=5 and d=50: quartic shape (70,70,20,20,20),
quintic shape (120,70,20,20,20), and tail 130. These are admissible five-row
cells in the project's ambient modules, not certified separating cells, and
not a claim that full cell computations are affordable.

Here lambda_1-(n-3)d=4k>0. Thus the capacity no-go of section 4 does not apply.
This is only a necessary-condition check; it does NOT prove padding survival.

For a completely specified base tableau, labels are a_ij=(L_i,m_ij) and
b_ij=(m_ij,R_j), i,j=0,...,4. Duplicate each of these columns:

    (a_i0,a_i1,a_i2,a_i3,a_i4), for every i;
    (b_0j,b_1j,b_2j,b_3j,b_4j), for every j;
    (a_ij,b_ij), for every i,j.

At n=5 additionally put each of the 50 labels into a singleton column.
This finite formula lists all columns without any search or unspecified choice.

## 6. Exact nonvanishing certificate, and the algebraic property obtained

For j=0,...,4 let

    ell_j = x_1+j x_2+j^2 x_3+j^3 x_4+j^4 x_5,
    p_n = sum_(j=0)^4 ell_j^n.

All these vectors have first coordinate 1. Every square top-coordinate minor
on distinct ell_j's is a nonzero Vandermonde determinant. For a map phi from
labels (edges of J_s) to colours {0,...,4}, BDI's formula becomes

    f_T(p_n) = sum_phi product_(v in V(J_s))
                         det(top deg(v) coordinates
                             of ell_{phi(e)}, e incident to v)^2.

Singleton factors are 1. Every summand is a nonnegative integer. A summand is
positive exactly when phi is a proper edge-colouring of J_s with five colours.
This is an exact weighted edge-colouring partition function, not a random test.

Here is a specific proper colouring. If uv is an edge of H_s, with u in L,
v in R and inherited colour c, assign colour c to (u,m_uv), and c+1 modulo 5
to (m_uv,v). At each old vertex all five colours occur. At each new vertex
the two colours differ. This proves a positive summand and therefore f_T!=0.

More explicitly, the five-colour Vandermonde determinant is

    product_(0<=a<b<=4)(b-a)=288.

There are 2k old vertices, giving 288^(4k) after squaring. Each inherited
colour occurs on k edges of H_s. At new vertices the squared two-colour
difference is 1 for c=0,1,2,3 and 16 for c=4. The selected summand is exactly

    288^(4k) * 16^k,

so f_T(p_n) >= 288^(4k)*16^k > 0, for both n=4 and n=5 (indeed every n>=4).
For the direct family the selected summand is 288^(4k), also positive.
These are lower bounds on the full evaluation, not claims to have summed it.

This argument proves nonzero highest-weight spaces in the displayed cells.
It does not show that distinct graph choices give independent polynomials.
At points of Waring rank <=4 every height-five determinant vanishes; hence
these functions vanish there and, by closedness, on border Waring rank <=4.
That low-rank vanishing comes from column height, not from expansion.

The witness p_n is an ambient rational form. No membership of p_n in actual
padding or in the determinant locus is asserted. A positive evaluation here
cannot substitute for either of the two separator certificates.

## 7. Expansion of the actual tableau graph, with a quantitative proof

The tableau graph G_s is the line graph of J_s. Equivalently, replace every
vertex v of H_s by a five-vertex clique of its incident half-edges, then join
the two half-edges of each original edge by a matching edge. Consequently
G_s has N=10k=d vertices and is simple and 5-regular. Duplicating columns and
adding singleton columns do not change G_s. We do NOT claim G_s is Ramanujan;
the seed H_s is Ramanujan and G_s is an expander.

For completeness here is a direct spectral-gap proof, avoiding an unproved
claim that graph operations preserve expansion. Give the vertices of G_s
real values x with sum zero. In the clique over v write a_v for the mean and
b_(v,e)=x_(v,e)-a_v. Let E_c and E_m be the sums of squared differences over
clique edges and matching edges, respectively, and E=E_c+E_m. Then

    E_c=5 sum b_(v,e)^2;   sum_v a_v=0.

For each original edge uv,

    a_u-a_v = -b_(u,uv) + (x_(u,uv)-x_(v,uv)) + b_(v,uv).

Using (A+B+C)^2<=3(A^2+B^2+C^2) and summing gives

    sum_(uv in E(H_s)) (a_u-a_v)^2
       <=3(E_m+sum b^2) <=3E.

The gap of H_s is at least 1, so sum_v a_v^2<=3E. Therefore

    sum x^2 = sum b^2+5 sum a_v^2
             <= E/5+15E = (76/5)E.

Thus the combinatorial Laplacian gap of G_s is at least 5/76. In particular,
for S of at most N/2 vertices the indicator-vector Rayleigh quotient gives

    |edges(S,S^c)| >= (5/152)|S|.

This is expansion beyond mere connectivity, with constants independent of s.
The cited spectral treewidth inequality yields

    tw(G_s) >= N/77 - 1.

The particular BDI treewidth evaluation bound therefore has an exponent
linear in d for these presented fillings. This is NOT a lower bound on every
algorithm for these functions, nor on alternative presentations of them.

## 8. What the result does and does not change

Established by the above hand arguments, conditional only on the named
external construction/formalism inputs:

1. An algorithmically specified infinite expander sequence, and completely
   specified base tableaux, in five-row quartic and quintic cells.
2. Exact content and shape, highest-weight character, and nonzero evaluation.
3. A weighted-colouring interpretation and a concrete positive summand.
4. A uniform spectral gap and a linear treewidth lower bound for the actual
   tableau graphs.
5. A padding no-go for the direct construction, and failure of that particular
   no-go to settle the subdivided construction.

Not established:

* Nonzero restriction of the subdivided functions to actual padding.
* A determinant identity for any member, or any separating linear combination.
* Algebraic irreducibility from graph connectivity, or independence from
  graph nonisomorphism.
* A correlation between spectral expansion and separating power.
* Semistandard expander presentations, strongly explicit/efficient Ramanujan
  generation, or efficient general evaluation.
* An accepted or independently checked new theorem for the programme.

The actual algebraic properties proved here do not require expansion: the
same pairing/colouring argument works for nonexpanding seed graphs. Thus this
answers the realization question affirmatively while leaving the proposed
expansion-to-separation link open.

## 9. Next certificate, before any empirical comparison

First independently review the content/normalization, padding-capacity proof,
explicit colouring and spectral-gap proof. The proof does not require pilots.

Then determine whether the subdivided family restricts nontrivially to actual
padding. A positive certificate must give an actual padded-permanent
substitution and an exact nonzero evaluation, or a symbolic nonvanishing
proof; a generic ambient point is insufficient. A uniform vanishing proof
would close this family just as section 4 closes the direct one.

Only if padding survival holds should determinant-ideal membership be pursued.
Neither a few zero determinant evaluations nor the graph's spectral gap is a
membership certificate. No computational search or comparison is launched by
this note.
