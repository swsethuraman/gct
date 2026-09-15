# B17-02: a shared-block boundary arc and a finite extension bound

**COMPLETE: bounded theory contribution with one exact pilot.**
13 September 2026, America/New_York. Original work in the assigned B15-02
worktree; no agents, tasks, worktrees, commits, publication or heavy lease.

The result is an explicit polynomial arc in the det4 orbit closure with a
proved boundary endpoint, and a representation-specific necessary condition
for regular extension from the orbit. In a finite cell it gives

    m_det(d,lambda) <= B := min(a_(d,lambda), s_lambda - rank C_(d,lambda)).       (1)

Here s_lambda is the full stabilizer bound, including transposition, and C
is the explicit forbidden-weight projection defined below. A certified
rank floor b may replace rank C. This is a proved refinement formula;
**no positive rank b in a new cell, strict numerical improvement, equation
module, or multiplicity gap is claimed.** The uncomputed input is an exact
stabilizer-invariant basis in one integrator-selected finite representation.
The boundary identity and the validity of (1) do not depend on that input.

The sole pilot passed in 0.0698843 seconds, with 13,692,928 bytes peak Job
Object commitment, under the inspected 60-second/512-MiB wrapper. It
verified polynomial identities, not a representation rank. Executable:
[analysis/b17_02_verify.py](../analysis/b17_02_verify.py). Input hashes,
resource receipts and delivery inventory are bound by
[delivery/b17_02/MANIFEST.json](../delivery/b17_02/MANIFEST.json).

## 1. Accepted scope and conventions

Work over C. Let W be the sixteen-dimensional space of linear forms,
V=Sym^4 W, G=GL(W), and X=closure(G.det4) in V. Coordinate modules are
labelled **S_lambda(W*)**, with lambda a partition of 4d, length at most
16, in coefficient degree d. Thus

    a_(d,lambda) = mult(S_lambda(W*), Sym^d(Sym^4(W*))).

For a chosen determinant representative f, write H=Stab_G(f) and
M_lambda=(S_lambda W)^H. Algebraic Peter-Weyl identifies the orbit
multiplicity with s_lambda=dim M_lambda; the dual on the coordinate
module is essential. H is the full determinant stabilizer, conjugate to
the determinant-preserving left/right group with transposition adjoined.
Equivalently s_lambda is the symmetric rectangular Kronecker coefficient
with rectangles (d,d,d,d). Taking only connected invariants gives a
possibly larger source and must be labelled accordingly. These facts are
the literature input for the representation interpretation; the arc and
bound are proved here. [Bürgisser–Landsberg–Manivel–Weyman, §4.1 and
§5.2](https://arxiv.org/pdf/0907.2850).

The requested evidence chain was followed:

1. Batch16/INTAKE.json, accepted scoped slot08 and reviewer12;
2. Batch16/reviews/12_milestone/intake_08.json and its proof supplement;
3. sibling B15-08/docs/b16_08_proof.md, report, executable excerpts and
   ARTIFACT_HASHES.json;
4. its INPUT_HASHES.json back through the Batch15 intake to
   Batch15_Launch/native_20260913/reviews_filesystem/Hessian11_1631/REPORT.md,
   especially the shared formulas at lines 135–146.

All eleven declared B16-08 artifact hashes matched. The original report
hash matched 54b0b4ddd5e7e98879e7f74219d081b4ee58dce124fecfd03675ed08c81b6f68.
This is a fresh provenance check, **not** a replay of the accepted
630-column/165-block negative computation. Its inherited conclusion is
only absence of ordinary coefficient-degree <=2 relations among the 34
three-direction Taylor coordinates. No broader degree or variable
exclusion is inferred. The old quadratic control was not rerun.

Batch17's screen supersedes the stale pending-cell language in common
context: all six nearby cells are excluded, and the specified degree-seven
symmetry screen has no survivor. Neither screen excludes boundary losses.
The independent padding model remains z*per3 with all nine permanent
variables and a separate z; it is neither per4 nor arbitrary cubic
padding in ten cubic variables. No padding computation is made here.

## 2. The common blocks produce a genuine polynomial boundary arc

Use sixteen independent coordinates

    a; r=(r1,r2,r3); c=(c1,c2,c3)^T; v=(v1,v2,v3)^T;
    S=[[s11,s12,s13],[s12,s22,s23],[s13,s23,s33]].

Set

    A(v)=[[0,-v3,v2],[v3,0,-v1],[-v2,v1,0]],
    f=det([[a,r],[c,A(v)+S]]).

The change from the nine entries of E to its skew and symmetric parts is
invertible in characteristic zero, so f is in the det4 orbit. Its three
off-diagonal coordinate pairs have nonzero determinants of magnitude two.
There is no restriction to symmetric determinant pencils.

Define the one-parameter subgroup gamma(t) of G by its action on W:

    a,r -> t^(-1)(a,r),     v -> v,     c,S -> t(c,S).

Its weight spaces have dimensions 4,3,9 for weights -1,0,+1; its determinant
as a sixteen-dimensional linear map is t^5. For t != 0,

    f_t=gamma(t)f=det([[a/t,r/t],[t*c,A(v)+t*S]]).

**Polynomial identity.** In the full polynomial ring in all sixteen
coordinates,

    f_t=Q0+t Q1+t^2 Q2,                                                   (2)
    Q0=a v^T S v-(r v)(v^T c),
    Q1=r A(Sv)c,
    Q2=a det(S)-r adj(S)c.

The same a,r,c,v,S are used in every expression; they are not independent
data at different orders. To prove (2), cofactor expansion gives the
division-free block formula det([[a,r],[c,E]])=a det(E)-r adj(E)c. Direct
three-by-three cofactors give

    det(A(v)+tS)=t v^T S v+t^3 det(S),
    adj(A(v)+tS)=v v^T-t A(Sv)+t^2 adj(S).                                (3)

Substitution in the block formula cancels the apparent t^(-1) pole and
proves (2). Formulas (2)–(3) are identities with integral coefficients,
valid for singular S as well. In particular t=0 is defined without any
localization. This cancellation is why the skew block is useful.

The analogous cubic leading term v^T S v is the classical skew-block
boundary construction for det3. Here we retain the common off-diagonal
r,c terms and the complete quartic arc. No literature novelty or det4
boundary classification is asserted. [Hüttenhain–Lairez, Lemma 5](https://arxiv.org/pdf/1512.02437).

**Compatibility across all derivative orders.** Let J be the point with
S=I and a=r=c=v=0. For ordinary Taylor coefficients in u (no factorials),
write e2(S)=sum_(i<j)(Sii Sjj-Sij^2). The same block identity gives

    f_t(J+uX)
      = u t^2 a
        +u^2 t^2(a tr(S)-rc)
        +u^3{a(v^T v)+t r A(v)c
               +t^2[a e2(S)-r((tr S)I-S)c]}
        +u^4{Q0+t Q1+t^2 Q2}.                                           (4)

At t=1 this specializes exactly to the inherited shared F1,F2,F3,F4
formulas with E=A+S: tr(A)=0, e2(A+S)=v^T v+e2(S). Equation (4) controls
the moving determinant family at a fixed point in the variable space W*;
it does not fix an untransported normalized matrix basepoint and then
silently discard normalization poles.

**Boundary endpoint.** Equation (2) defines a morphism A^1 -> X because
its punctured image lies in G.f and X is closed. Moreover Q0 is outside
G.f. Indeed (4) at t=0 says Q0 has multiplicity exactly three at the
nonzero point J, with lowest Taylor term a(v1^2+v2^2+v3^2). This cubic is
nonzero and reducible. For an actual det4, a matrix of rank r has
multiplicity 4-r: after constant invertible row/column changes the lowest
Taylor term is det of the missing (4-r)-square block. Consequently every
triple point on an invertible transform of det4 has an irreducible det3
cubic as its lowest term, even with the remaining variables adjoined.
Invertible coordinate changes preserve both multiplicity and reducibility
of that term. This contradicts the displayed cubic for Q0. Thus

    Q0 belongs to X \ (G.f).

This proves one boundary point, not that its orbit closure is an
irreducible boundary component. Nor does it prove that Q0 is outside the
image of every singular linear substitution of det4.

## 3. The representation-labelled extension criterion

Fix d>=0 and lambda partitioning 4d. In the finite representation
S_lambda W, let pr_k be projection onto gamma-weight k and define

    C_(d,lambda): M_lambda -> direct_sum_(k<0 or k>2d) (S_lambda W)_k,
    C_(d,lambda)(z)=(pr_k z)_(k<0 or k>2d).                               (5)

This is an explicit linear map once an exact H-invariant basis is given.
It acts on the **multiplicity source**, rather than on an arbitrarily
chosen ambient equation kernel. All weights lie in [-4d,4d]. A more
detailed label uses W=W_- + W_0 + W_+, with dimensions 4,3,9: the Levi
constituent S_alpha W_- tensor S_beta W_0 tensor S_delta W_+ has gamma
weight |delta|-|alpha| and iterated Littlewood–Richardson multiplicity
c^lambda_(alpha,beta,delta). The prohibited constituents have that integer
outside [0,2d]. This branching description is a definition of the carrier;
no character enumeration is performed.

**Theorem.** Every copy of S_lambda(W*) in C[X]_d corresponds, under the
orbit restriction/Peter-Weyl identification, to a vector in ker C. Hence
(1) holds. More generally an exact rank floor b for (5) proves

    m_det(d,lambda) <= min(a_(d,lambda), s_lambda-b).                       (6)

**Proof.** For z in M_lambda and ell in (S_lambda W)* the orbit function

    h_(ell,z)(g f)=ell(g z)

is well-defined, since z is H-fixed. Let E_lambda be the subspace of
M_lambda whose entire matrix-coefficient copy extends to C[X]. It has
dimension m_det(d,lambda). The size condition |lambda|=4d gives coefficient
degree d: a scalar q I acts by q^(4d) on S_lambda W and by q^4 on f.

If z is in E_lambda, choose the corresponding homogeneous ambient
polynomial P_ell of coefficient degree d. Such a representative exists
because C[X] is the graded quotient of C[V]. Evaluate it on (2):

    ell(gamma(t)z)=P_ell(Q0+tQ1+t^2Q2).

The right side is a polynomial in t with exponents between 0 and 2d.
The left side is sum_k t^k ell(pr_k z). Equality on C* and uniqueness of
Laurent coefficients imply ell(pr_k z)=0 for all forbidden k. Since ell
is arbitrary, pr_k z=0. Thus E_lambda is contained in ker C. Taking
dimensions and also using the ambient ceiling gives (1); replacing the
exact rank with a certified floor gives (6). This proves the statement
for every finite d,lambda in the specified convention. It is not a
claim extrapolated from a small-degree test. QED.

**Why this is a global polynomial bound.** The proof starts with a
polynomial representative of an actual function on the entire affine
closure and pulls it back along a polynomial morphism A^1 -> X. It needs
neither a smooth-root chart nor normality of X, and it never divides a
coefficient polynomial by an unverified denominator. Equations (2)–(4)
remain true after arbitrary linear substitutions of their sixteen
coordinates. End(W) preserves X by density of GL(W), so these
substitutions also stay inside the closed determinant family.

Conversely, C(z)=0 only proves this copy has no forbidden powers on this
particular arc. It is **not a sufficient condition for global extension**.
Other arcs and descent through a nonnormal boundary may impose further
conditions. General boundary-valuation approaches already distinguish
necessary extension conditions from equality under a normality
hypothesis. [Bürgisser–Landsberg–Manivel–Weyman, §7.3](https://arxiv.org/pdf/0907.2850).
Fundamental-invariant extension also exhibits the orbit/closure
distinction; it does not make a single-arc test complete.
[Bürgisser–Ikenmeyer, §3](https://arxiv.org/pdf/1511.02927).

The improvement threshold matters. Let B0=min(a,s). A rank floor b gives
a **strict** refinement of B0 only if

    b >= s-B0+1.                                                         (7)

A nonzero forbidden projection is not enough when s is much larger than
a. No b satisfying (7) has been found or presumed here. In degree one,
lambda=(4), the invariant vector is f itself, with gamma weights 0,1,2,
so C(f)=0 as it must. This is a compatibility control, not a new cell.

## 4. A proved negative control for simpler block rescalings

There is a reason not to replace the skew cancellation by only scaling
the original sixteen matrix entries. Suppose gamma_w(t) sends x_ij to
t^(w_ij)x_ij, and gamma_w(t)det4 is a polynomial in t of degree L. Because
the 24 determinant monomials are distinct, every permutation weight
sum_i w_(i,sigma(i)) lies in [0,L].

Embed S_lambda W in W^(tensor 4d). Each tensor word in an H-invariant
vector has occurrence matrix N=(n_ij) with every row sum and every column
sum equal to d. This follows from the two determinant-preserving diagonal
tori; total word length is 4d. The integer matrix N decomposes into d
permutation matrices. To see this, view N as a d-regular bipartite
multigraph: d|R| edges from any row subset require at least |R| neighboring
columns, so Hall's theorem gives a perfect matching; remove it and repeat.
The word's gamma_w weight is therefore a sum of d permutation weights,
and lies in [0,dL]. This holds for every H-invariant vector in every
polynomial label of size 4d.

Thus the analogous forbidden-weight projection is identically zero for
**every such original-entry diagonal arc**. Neither its pole check nor
its upper-degree check sharpens the stabilizer bound. This is a proved
scoped negative result, independent of the inherited 34-coordinate test.
Our gamma is diagonal in skew/symmetric coordinates, not the original
matrix entries, so this argument does not make (5) zero. It also does not
prove that (5) is nonzero in a useful representation.

## 5. Priced pilot, evidence and limitations

[docs/b17_02_preflight.md](b17_02_preflight.md) was saved and read before
the only mathematical run. The direct determinant expansions were priced
at 192 raw terms for (2) and 384 for (4). The predicted reduced arc
supports 15,18,23 matched exactly. The verifier used only standard-library
integer sparse dictionaries and an independent 24-permutation route
against (2)–(4). It checked every adjugate entry, all Taylor coefficients,
the gamma weights and two deliberately wrong formulas.

| Measured item | Result |
|---|---:|
| Mathematical computations in this session | 1 |
| Wall seconds in inspected wrapper | 0.06988429999910295 |
| Peak Job Object committed bytes | 13,692,928 |
| Peak working-set bytes | 21,024,768 |
| Largest dictionary / full Taylor support | 90 monomials |
| Monomial-pair products | 939 |
| Exit code | 0 |

All 22 pinned input hashes were verified by the pilot before arithmetic.
The process exited; no timeout, memory cap hit or heavy lease occurred.
The wrapper's legacy B15-02 label is retained and mapped to B17-02 in the
manifest. No representation matrix was built and no second computation
was used to repeat the verifier. The program remains executable for a
separately authorized receiver. The proof of (1) and the tangent-cone
argument were reasoned here, not independently reviewed by another agent.

Fresh results are (2)–(6), the boundary-endpoint proof, the entrywise-arc
negative lemma, support pricing and exact verification. The general
extension principle and the cubic skew precursor are literature inputs;
the underlying shared F1..F4 formulas and the narrow quadratic negative
scope are inherited accepted project evidence. This combination is not
claimed new to the literature.

This report does not furnish an eliminant in quartic coefficients or
membership/nonmembership modulo J24, Jflag or a saturation. Its output
is the allowed alternative: a representation-labelled extension criterion
with a proof that it bounds the polynomial closure coordinate ring.
It yields no numeric B, actual-padding rank, positive gap, improved LMR
determinant-size growth, or asymptotic separation. Distinct kernels and
shared equations are not dimension comparisons. Failure of this arc in
any future cell would exclude only that arc's certificate in that cell.

For an actual obstruction, keep one finite cell and obtain B from (6)
and an actual independent-padding coordinate floor r>B. Then
D=m_pad-m_det=i_det-i_pad>0. A padding-source ceiling U only permits the
necessary pre-screen B<U; it never substitutes for r. Existing excluded
cells remain excluded, regardless of their equations.

## 6. One next sufficient test and integrator request

Supply **one** new finite cell (d,lambda), certified a,s,U, and a sparse
exact full-H invariant basis z1,...,zs in the adapted coordinates above.
Require a support price before any Schur expansion: number of stored
terms, forbidden rows, rational bit sizes, and the number of columns
needed for the intended minor. Do not build the naive 16^(4d) tensor
carrier. No cell is nominated by an unperformed character census here.

The single sufficient test is an exact nonzero b-by-b minor of
(C(z1),...,C(zs)), with

    b >= s-B0+1,     B=min(a,s-b) < U.

The invariant-basis certificate must include the transposition component;
a minor over a verified integral lattice modulo a prime suffices for a
characteristic-zero rank floor. Its successful output is a new global
determinant upper bound B, not a gap. Only then is a B+1-column actual
z*per3 independence witness a justified next task.

**Integrator action requested through this report:** review this theorem
and supply that one representation/basis package if continuing. The
measured pilot establishes the price of the identity instrument only.
It does not price the representation calculation or authorize a larger
lease. This session's one computation is exhausted. Any follow-up run
requires new task authorization, and any larger lease requires integrator
resource review; none is self-issued here. The bounded contribution is
complete without waiting for that optional follow-up input.
