---
board_numbering: batch13
session_id: B13-06
model: gpt-6-astra
reasoning_effort: xhigh
base: 00495110c62acfbbbc951e82cc218ed091563b3f
branch: b13-06
---

# B13-06: positive gap beyond the LMR cell

**RECORDED — Delivery:** one bundle part, numbered `part00`, accompanies the
whole bundle, with whole-file and per-part MD5 and SHA-256 checksums. This report
delivers the complete finite product-domain census, guaranteed image components,
two exact transport limitations, and the precise unresolved comparison maps.
No positive multiplicity gap is claimed. The actual model is `gpt-6-astra`
(`xhigh`, confirmed by the executing automation configuration).

## Result and scope

**PROVED — Finite reduction.** Multiplying the one-copy LMR module
E=S_(65,17,2^7)V in coefficient degree 24 by linear or quadratic coefficient
polynomials has the following tensor-domain support. The image of multiplication
is a quotient of this domain; the table does not assert that every component
survives.

| Coefficient degree | Distinct constituents | Length 9 | Length 10 | Length 11 | Sum of tensor multiplicities | Largest tensor multiplicity |
|---|---:|---:|---:|---:|---:|---:|
| 25 | 31 | 15 | 16 | 0 | 31 | 1 |
| 26 | 305 | 89 | 119 | 97 | 799 | 10 |

**PROVED — Closed portions.** All 97 eleven-row components have mult_pad=0,
so D<=0. The two highest-coefficient components (69,17,2^7)_25 and
(73,17,2^7)_26 preserve exactly the LMR gap, including its unresolved sign.
This leaves 30 degree-25 and 207 degree-26 components where this session does
not decide improvement: 237 candidates in the full problem, or 102 after
restricting to nine variables. These are a complete finite list, not a ranked
claim that all 237 occur in the product image.

**PROVED — Guaranteed new equations.** Write u=c_(4,0,...,0),
c_j=c_(4-j,j,0,...,0), and let f be any nonzero highest-weight generator of
the exact LMR equation line. In addition to uf and u^2 f, the two products

    f (8 c_0 c_2 - 3 c_1^2),             weight (71,19,2^7), degree 26,
    f (12 c_0 c_4 - 3 c_1 c_3 + c_2^2), weight (69,21,2^7), degree 26,

are nonzero determinant equations. Their product-image multiplicities j lie
respectively in [1,2] and [1,3]. Polynomial multiplication in a domain proves
nonzeroness; the raising rule below proves highest weight; the ideal property
proves membership. These are identities expressed in the adopted exact LMR
generator, not a reconstructed rational coordinate vector for that generator.
The products give a mechanism for i_det>0 outside the LMR ladder. They do not
prove that the reducible or padded ideal multiplicity is smaller.

**CERTIFIED — Completed ambient counts and concrete next questions.** A new
integer Weyl/DP computation, with overflow detection at every addition, gives:

| Degree | Weight | Ambient a | Product image j | Sufficient padded rank if maximal j is proved |
|---|---|---:|---|---:|
| 24 control | (65,17,2^7) | 274 | 1, adopted LMR | 274 |
| 25 | (69,17,2^7) | 274 | 1 | 274; same gap as control |
| 26 | (73,17,2^7) | 274 | 1 | 274; same gap as control |
| 26 | (71,19,2^7) | 392 | 1 through 2 | 391 |
| 26 | (69,21,2^7) | 531 | 1 through 3 | 529 |

The latter two ambient counts took 47.7 and 52.4 seconds. If only the
guaranteed one-copy product is proved, the sufficient padded ranks are instead
392 and 531. No such padded rank, or maximal product-image rank, was measured.

**RECORDED — Complete list and data.** Every partition, channel multiplicity,
image-rank interval, dimension price, and decision question is in
`results/b13_06/components.json` and the human-readable `components.md`.
`lr_audit.json` includes zero channels, so completeness was checked even for
constituents removed by cancellation. The ambient files and controls file give
the additional completed computations; `run_summary.json` summarizes their
actual outcomes and resource costs.

## Objects, conventions and input audit

**RECORDED.** A=Q[c_alpha: |alpha|=4]=Sym(Sym^4 V), with coefficient degree
grading. The action is the repository convention

    c_alpha(F)=[s^alpha]F,
    E_ij c_alpha=(alpha_i+1)c_(alpha+e_i-e_j), when alpha_j>0.

Take V of dimension 16 for det_4 and full l*per_3, and specialize the polynomial
functors to r=9 or r=10 when appropriate. All constituent lengths are <=11;
dimension 16 is therefore in the stable range for this tensor decomposition.
P_r is the closure of l(s)*per_3(M(s)), R_r the image of (l,c)->lc, and D_r
the closure of det_4 pencils. All are irreducible: each is the closure of a
polynomial image of an irreducible affine parameter space. P_r is contained in
R_r. Multiplicities are stable once the ambient variable count is at least the
weight length, by the restriction/inheritance convention used in the repository.

**ADOPTED — Exact LMR inputs.** The 274 integral bracket fillings in
`results/s74/source.json` form the ambient highest-weight basis; determinant
rank is exactly 273 and padded rank is at least 269. Hence

    D=mult_pad-mult_det=i_det-i_pad=1-i_pad(24),   -4<=D<=1.

**MEASURED — Not adopted as identities.** Reducible/padded sampled ranks 269,
the same five-dimensional sampled kernels, and D=-4 are measurements. Neither
the rational reducible nullity nor i_pad(24)=i_pad(23) is inferred from them.
There is no dependence on the batch-13 sessions assigned those questions.

**RECORDED — Replay boundary.** The exact row polynomials use the letter
normalization m_alpha=alpha! c_alpha. Native values at rung d become degree-24
values after multiplication by msym_u^(24-d), msym_u=24u. The new arithmetic
checker validates literal fillings and this scaling, recomputes u from integer
points, and checks modular LMR residues. These are arithmetic checks of the
stored evaluations, not fresh evaluations of every circuit or a fresh rank
certification. Original integer points and u-values accompany those checks in
`input_arithmetic_<family>_<prime>.json`; transformations are recorded next to
the numbers. Both house primes are used, never a small substitute.

**ADOPTED with a precise implication.** The exact LMR line is nonzero on P and
R, as certified in s74. This can be justified without rational reconstruction:
the adopted nonzero determinant 273-minor and a modular annihilating vector
give a one-dimensional sampled determinant kernel. A primitive integral
coordinate vector for the rational LMR line reduces nontrivially into that
kernel. Its tested nonzero padded/reducible residue therefore precludes rational
membership in either ideal. This use of a nonzero minor is different from
lifting a modular *containment* of a higher-dimensional kernel, which is the
unresolved degree-23/24 issue. The present session does not claim to recompute
the 273-minor itself.

**RECORDED — Inputs and board defects.** The required five documents were read
before coding. B13-06 names conceptual inputs but not exact paths or ambient
variable count. This report resolves them using `lmr_cell.md`,
`s74_final_review.md`, `compact_circuit.md`, the s74 source/columns/certificates,
`s63_aladder.json`, and sections 2 and 5 of the batch-10/11 stocktakes on failed
transport methods. The stable-range proof uses s57 Lemma L/Proposition S.
These tier-3 additions resolve those board omissions. The user-supplied frozen
checkout controls over the preamble's fresh-clone/main instructions: main is
absent, the starting HEAD equals the required base, and no shared checkout or
global Git configuration was changed.

## Decomposition and actual images

**PROVED.** A_1=S_4 V. Its product with E is multiplicity-free, indexed by
horizontal four-strips nu/lambda. A_2=S_8 V + S_(6,2)V + S_(4,4)V. Thus

    t_(1,nu)=c_(lambda,(4))^nu,
    t_(2,nu)=c_(lambda,(8))^nu+c_(lambda,(6,2))^nu+c_(lambda,(4,4))^nu.

The channel multiplicity sums in degree 26 are 109, 501 and 189. Use
s_(a,b)=h_a h_b-h_(a+1)h_(b-1) and Pieri to enumerate. Independently enumerate
semistandard LR tableaux in every skew shape obtained by adding four/eight
boxes. The latter checks row/column inequalities and the lattice reading word;
it does not call the Pieri implementation.

**CERTIFIED — Exact finite combinatorics.** All 2,196 channel coefficients
agree. Eight Weyl-dimension sums agree with dim(E)*dim(A_k), at r=9,10,11,16.
Direct monomial characters verify Sym^2(Sym^4)=S_8+S_62+S_44 in dimensions
2,3,4 (15,120,630 monomials). All arithmetic in these checks is over Z or Q.
The complete computation took about 0.11 s and 20.3 MB peak process memory.

**PROVED — Small image control.** For Sym^4(C^2) tensor Sym^4(C^2), the
five tensor components have weights (8),(7,1),(6,2),(5,3),(4,4). Explicit
highest-weight tensors multiply nontrivially in the three even channels and
to zero in the two odd channels. Their dimensions give image dimension 15
and kernel dimension 10. The delivered checker verifies the tensors and their
products over Z. Thus a positive LR coefficient alone is demonstrably
insufficient to assert a product equation in a given isotypic component.

**PROVED — Three quadratic highest weights.** The polynomials u^2,
8c_0c_2-3c_1^2, and 12c_0c_4-3c_1c_3+c_2^2 have highest weights (8),(6,2),
(4,4), since E_12 c_j=(5-j)c_(j-1) makes their derivatives zero, and all other
simple raising operators vanish. Multiplication by f gives the guaranteed
Cartan components stated above. The coefficient factors are nonzero on P and R;
together with the adopted nonvanishing of f and the domain property of their
coordinate rings, each product also restricts nontrivially to P and R.
That says one determinant equation does not vanish there; it does not compare
the total ideal multiplicities.

**RECORDED — Pre-checks.** Coordinate-ring restriction is functorial in the
needed direction: P subset D implies Q[D] surjects onto Q[P], hence D<=0.
The coefficient-factor controls use a fixed det_4 pencil, a committed reducible
point, and a full ten-variable padded permanent. The latter is obtained by
completing the committed 10-by-9 linear-form matrix to an invertible 10-by-10
integer substitution, whose exact determinant is stored. It retains all ten
essential variables. These controls concern the factors, not a newly proposed
degeneracy statistic. No D>0 or nonzero cubic-permanent ideal is reported, so
no positive-candidate verification protocol is asserted to have been completed.

## Why the two ladder products cannot improve the gap

**PROVED, using the adopted/recounted ambient dimensions.** Multiplication by
u induces injections on ambient highest-weight spaces, on I(X), and on Q[X]
for X=D,P,R: u is nonzero on each irreducible variety. If ambient dimensions
are equal at adjacent rungs, the ambient injection is an isomorphism. Moreover
uf belongs to I(X) iff f belongs to I(X), since Q[X] is a domain. Therefore
both ideal and coordinate-ring multiplicities are equal at those rungs.

The adopted saturation a_24=a_infinity=274 forces a_d=274 for every d>=24;
the bounded ambient computation additionally recounts the adjacent cells.
Consequently, for every k>=0 along this particular ladder,

    i_X((65+4k,17,2^7),24+k)=i_X((65,17,2^7),24),
    mult_det=273, mult_pad>=269, D=1-i_pad(24).

This is a limitation on all Cartan powers of the highest coefficient, not a
proof that D<=0. It uses no degree-23 padded equality. The two other quadratic
Cartan products change the second row and are not covered by this argument.

**PROVED — Length exclusion.** The full padded form has ten essential
variables. Its orbit closure lies in the ten-variable subspace variety, whose
coordinate ring has no constituent of length greater than ten. Equivalently
any column antisymmetrization of height eleven evaluates to zero on a form
supported in a ten-dimensional space. Hence mult_pad=0 for all 97 eleven-row
entries, while mult_det>=0, giving D<=0 without any sampled deficiency.

## The exact questions that decide the remaining components

**PROVED — Image and comparison formulas.** For a listed nu in degree d=24+k,
let M_nu be the ambient highest-weight space, a_nu=dim M_nu, and choose an exact
basis of its t_nu-dimensional tensor-product highest-weight space. Polynomial
multiplication defines

    B_nu: Q^(t_nu) -> M_nu,     j_nu=rank_Q B_nu,
    S_nu: M_nu -> (Sym^d V tensor Sym^d(Sym^3 V))_nu^hw,
    T_X,nu: M_nu -> Q[X]_d,nu^hw.

Here S is the multiplication pullback c_alpha -> sum_(alpha_i>0)
l_i c_(alpha-e_i). The domain and normalization of S are explicit. Then

    J_d,nu=im B_nu subset I(D)_d,nu,
    i_det>=j_nu,  i_red=a_nu-rank S_nu,
    D=rank T_pad,nu-rank T_det,nu,
    dim(J_d,nu intersect I(X))=j_nu-rank(T_X,nu B_nu).

The last identity prevents confusing nonvanishing of product equations with
the total comparison: it measures only the intersection of the product image
with the other ideal. Extra determinant equations outside J may also exist.

**PROVED — Sufficient certification threshold.** Exact membership and
independence of j_nu product equations give rank T_det<=a_nu-j_nu. A padded
minor of size a_nu-j_nu+1 therefore proves D>0 (subject to the board's full
verification protocol). For the necessary reducible gate, j_nu>i_red is a
sufficient way to establish i_det>i_red; it is not sufficient for D>0 because
i_pad may exceed i_red. Conversely j_nu<=i_red only defeats this lower bound
strategy, not all possible determinant equations. Each census entry includes
these precise questions with its own t_nu and image interval.

**RECORDED — What is still needed.** No non-Cartan B_nu, S_nu, or full padded
rank has been constructed at degree 25 or 26. The explicit rational LMR
generator in the 274-filling coordinates is also not reconstructed here.
The family-level membership proof uses its certified existence. The numerical
gap at the original LMR cell remains [-4,+1], with -4 measured. Thus this is
the board's finite justified reduction with completed mathematics, not a
positive obstruction or a global impossibility theorem for products.

## Bounded continuation and reproducibility

**RECORDED — First continuation.** Use the two guaranteed non-ladder weights
(71,19,2^7) and (69,21,2^7). Their B matrices have respectively two and three
columns. `run_summary.json` supplies the completed ambient row counts. Recover
an exact LMR equation (for example from the original flag/Hessian construction),
construct the two/three highest-weight product columns, and test their rational
independence. If all survive, the required padded minor sizes are respectively
a-1 and a-2; if only the guaranteed Cartan copy survives, each requires full
padded rank a. A sampled reducible/padded deficiency does not answer that task.

**RECORDED — Costs, not promises.** The naive whole-module tensor domain has
dim(E)*binomial(binomial(r+3,4)+k-1,k) coordinates; exact values are in the
census dimension checks. Even the nine-variable source module has quadrillions
of coordinates, so this domain must not be materialized. Multiplicity maps
have at most ten columns, but constructing their polynomial entries remains
the unresolved symbolic cost. The naive ambient tail-DP arrays across the
census range up to 212,576,400 bytes for one int64 array, before temporaries
and Weyl shifts; this is a memory price, not a measured rank-build time.
The existing LMR weight-space construction already has 156,438,903,314
monomials. Small multiplicity-space dimensions do not remove that expansion
cost. A continuation should launch one 1,200 s / 768 MiB pilot per selected
B column, bank an exact prefix and measured entry costs, and stop before any
full weight-space allocation. No unmeasured wall-time estimate is presented
as a completed benchmark.

**RECORDED — Local execution.** All computations ran in the isolated checkout,
one numerical worker and one BLAS thread. Windows Job Objects enforce 768 MiB
per process, with wall watchdogs at 300 or 1,200 s. PIDs and actual memory/time
are in `results/logs/b13_06_*.resources.json` and `.pid` files. Initial physical
memory was 33.75 GB total / 7.43 GB free; each launch records a fresh reading.
numpy and Python 3.12.14 were available. flint, sympy, scipy and psutil were
not; Singular/msolve were not found. Local dependency installation failed on
network socket access (WinError 10013), and no runtime was modified. The
registered exact decomposition and coefficient calculations require none of
those missing packages. Fresh python-flint rank replays remain unperformed.

**RECORDED — Replay.** With the bundled Python executable (or compatible
Python 3.12 plus numpy), run each script through `analysis/b13_06_bound.py`:
`b13_06_decompose.py`, `b13_06_ambient.py --degree D --weight COMMA_LIST`, and
`b13_06_controls.py`. The manifest lists input SHA-256 hashes, output hashes,
all five ambient cells, the commits, and exact resource logs. On non-Windows
hosts provide equivalent wall/memory bounds instead of this native wrapper.
Do not run the historical s63 driver: it writes to the old session's paths.

**ADOPTED — Literature provenance.** LMR's Theorem 2.3.1 gives the weight and
degree (k+2)(d-1); section 3.1 specializes it to determinant equations, giving
degree 24 at k=6,d=4. The introductory statement in the old arXiv v1 has a
different degree; this report uses the detailed theorem and the frozen
repository's corrected degree, not that introductory line.
[Landsberg–Manivel–Ressayre](https://arxiv.org/html/1004.4802#S2.SS3).
The Schur calculations are fully replayed locally; standard symmetric-function
operations are documented in [Sage's Schur reference](https://doc.sagemath.org/html/en/reference/combinat/sage/combinat/sf/schur.html).

**RECORDED.** No branch history was rewritten. Commits were banked by unit;
there were no pushes, external publications, global Git changes, or new
follow-up schedules. No Adams, wreath, or block-diagonal operation is used as
a transport to larger determinants. All claims concern the same det_4 and
l*per_3 comparison in coefficient degrees 25 and 26.
