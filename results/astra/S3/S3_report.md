# Batch 12 S3 — compact spherical operator, certified dimension control, and the remaining evaluation pairing

**Frozen research report, 8 September 2026.** This session derived and implemented the compact operator. It recovered the 31-to-2 control with reconstructible certificates at both house primes. It did **not** complete the evaluation bridge for those recursive vectors or construct the 274-dimensional target basis. The deliverable is a proved operator, executable recurrence, successful dimension control, and a precise bounded fallback—not a launch plan or a completed LMR rank decision.

## 1. Outcome and falsifiable hypothesis

The preregistered hypothesis was that last-eight-slot recoupling, together with stored predecessor inclusions, gives manageable exact matrix elements **and an evaluation-compatible source**. Acceptance required both the 31-to-2 construction and determinant rank two on the **same recovered vectors**, with another point family and independent checking.

The first half is established. The second half remains **OPEN**. In particular, fresh evaluations of the banked circuit seed are not silently relabelled evaluations of the new recursive basis.

The main results are:

* **PROVED:** on the K-invariant precursor, the spherical operator satisfies the stronger identity
  \[
  \boxed{I+(d-1)T=dP_{H_d}|_{W_d}}.
  \]
  This proves the desired fixed-space equivalence and supplies a specific good-reduction argument. A finite-field norm argument is unnecessary.
* **PROVED / implemented:** all recoupling is an eight-box seminormal calculation. The exact residual is `(F-I)J`, where J uses only stored predecessor basis matrices. No unknown global LR coefficient is needed for source construction.
* **CERTIFIED dimension control:** a 239 by 31 residual has rank 29 and a displayed two-column kernel at each house prime. The actual 31 by 31 spherical matrices, Gram matrices, and projectors are also supplied and checked.
* **Independently reproduced:** all 23 degree-10 multiplicities underlying C12 agree with the inherited Weyl-engine table; C12=239. The new engine is representation recursion, not a rearrangement of that Weyl alternation.
* **Exact target local data:** all 42 rational swap blocks for the target are supplied, comprising 852 scalar matrix entries. The largest local tableau space at that top level is 1,120. This is not a 274-vector target source.
* **Bounded fallback:** four explicitly specified pairing coefficients connect the recursive two-dimensional control to the banked circuit basis. Their permutations, normalization, and coordinate transforms are supplied. Computing those coefficients compactly remains the next task.

**BANK** the operator and dimension-control artifacts. **KILL** raw `tau|W` and unrestricted ambient expansion as implementations. **PARK** target source construction until evaluation of the control basis is resolved. Failure of a conversion budget is not a mathematical impossibility.

## 2. Inputs, authority, and checks that were unavailable

All four canonical files were read, including the actual DOCX text: the final reconciled proposal, both Batch 11 stock-takes, and the complete comprehensive source. The standalone S3 brief and complete launch packet were read. The final proposal §§1.3 and 3.3 S3 and this brief control assignments over the older repository board.

The shared checkout was observed at `afb8c3319d3d1f3afc3d2578c8cb322f2b8a3b92`, with no tracked working-tree changes reported. Git verified that the supplied readiness commit `c984e2c6d59ba0bbc6ac2fdd113edf920a8aebd9` is an ancestor. To avoid moving inputs, computation uses an isolated `git archive` of **c984e2c6d59ba0bbc6ac2fdd113edf920a8aebd9**. The live-remote query failed to connect to GitHub. The user's earlier successful remote verification remains source-reported evidence; this run claims no fresh remote PASS.

| Input or check | Actual status |
|---|---|
| `wk11_int_bdelta.py`, `wk11_int_b24.py`, `wk11_int_cdelta.py`, `wk11_int_s5_dag.py` | Present in the frozen accepted base; inspected |
| Multiplicity drivers | The B/C drivers use pruned Weyl alternation and `N_S_tail_n`; the separate power-sum/Murnaghan–Nakayama implementation is `wk8_s30_pleth.py` |
| B24 predecessor table | Present; its twelve terms were **not** independently rerun in this session |
| C12 table | Present; all 23 terms compared with the new compact recursion |
| s69 target state, ladder, n4 seed, n3 control, s63 ladder | Present and frozen; no target sampler restarted |
| Repository self-test | Attempted in the isolated snapshot; import failed on missing `flint`; no self-test cases ran |
| s67/s71 reconciliation / full calibration corpus | Not replayed; no blanket preflight PASS |
| Circuit calibration runtime | Frozen S1 Python packer and C# evaluator inspected and reused; Linux `.so` files not loaded |
| Completed Batch 12 reports | Workspace S1 and S2 reports read; the requested Documents results directory was absent |

S1 supplies the exact birth-quotient theorem and a separate circuit calibration, but explicitly leaves its Pieri conversion unresolved. S2 supplies a rank-three special-stratum counterexample to an unqualified r=5 rank dichotomy and retains the global geometry theorem as open. This session neither re-audits that geometry nor assumes it is complete. These are actual available reports, not reports this session waited for.

The requested Documents destination is outside this execution's writable roots. Results therefore live in the permitted isolated directory **C:\Users\swami\Projects\gct-gpt\Batch12_Results\S3**. No canonical source, shared checkout, schedule, or other task was changed. Input and artifact manifests record full paths, sizes, hashes, and the immutable code base. Outputs are frozen for independent integrator review; no scientific promotion or external relay was sent.

## 3. Groups, exact fixed-space identity, and good reduction

Write `d` for coefficient degree and use consecutive four-slot blocks in `{1,...,4d}`. Let

\[
N_d=S_4^d,\quad H_d=N_d\rtimes S_d,\quad
K_d=N_d\rtimes S_{d-1}=H_{d-1}\times S_4.
\]

Here `S_(d-1)` fixes block d. Let tau exchange blocks d-1 and d, preserving each within-block position. Then

\[
L_d=K_d\cap\tau K_d\tau^{-1}
   =H_{d-2}\times S_4\times S_4.
\]

For any H-module V in characteristic zero, set `W=V^K`, `Z=V^L`, and let P denote **averages**, with factors `1/|K|` and `1/|H|`. The group `<K,tau>` is H. Thus the literal map

\[
R:W\longrightarrow Z,\qquad v\longmapsto(\tau-1)v
\]

has kernel `V^H`. It is a rectangular map; no assertion that tau preserves W is made.

For the endomorphism `T=P_K tau P_K|W`, the double cosets K and `K tau K` partition H. Equivalently, average the images of the distinguished block. For v in W,

\[
P_K\tau v={1\over d-1}\sum_{i=1}^{d-1}(i\ d)v,
\qquad
P_Hv={1\over d}\left(v+\sum_{i=1}^{d-1}(i\ d)v\right),
\]

where `(i d)` exchanges whole blocks. This proves the boxed identity in §1. Consequently

\[
\ker(T-I)=V^H,\qquad (T-I)((d-1)T+I)=0.
\]

The only eigenvalues in characteristic zero are 1 and `-1/(d-1)`. With `B=dim W` and `a=dim V^H`, their multiplicities are a and B-a. In particular, the control has trace `-7/11`; the expected target spectrum, **conditional on the inherited dimensions**, is 1 with multiplicity 274 and `-1/23` with multiplicity 1894. This spectral statement does not compute a target basis or a determinant evaluation rank.

For comparison, the usual characteristic-zero norm proof takes an invariant positive definite inner product: `P_K tau v=v` and equality of projected and original norms imply `tau v=v`. That proof is valid over Q after extension to R. It is **not** the modular proof used here.

### Specific integral model and specialization theorem

Fix a prime p greater than `N=4d` and work over the local PID `A=Z_(p)`. The rational seminormal model below has a free A-lattice, all adjacent-generator denominators being nonzero content differences of absolute value at most N-1. It is stable under the entire symmetric group. Alternatively use the integral Specht lattice and its localization. Both have the characteristic-zero representation `S^lambda`.

The orders `|H_d|=24^d d!`, `|K_d|=24^d(d-1)!`, and `|L_d|=24^d(d-2)!` are units in A. Their averaging operators are **idempotents over A**. Images and kernels of each idempotent are direct summands of a finite free A-module and hence are free. Tensoring the direct-sum decomposition with Q or F_p preserves it. Therefore invariants commute with these base changes and have equal dimensions. This is the needed rank-stability statement, not a generic invocation of Maschke for an arbitrary matrix.

Moreover, `d` and `d-1` are units. The double-coset identity holds over A and F_p and gives

\[
T-I={d\over d-1}(P_H-I)|W
\]

there too. Thus the compact fixed space has the correct dimension after reduction, provided the stored columns really are a basis of the K-invariant lattice modulo p. The recursive construction below proves precisely that condition inductively.

RREF normalization adds inverses of selected modular pivots, each explicitly nonzero modulo its chosen prime. These are legitimate p-local basis changes; they are **not** declarations that the residue entries themselves solve the original rational equations. A reconstructible rational lift of a saved modular basis is: lift each U entry to `{0,...,p-1}`, assemble its predecessor vector using already lifted children, then apply the rational H-average. Its reduction is the saved invariant vector. The lifted vectors are independent over Q and form a p-local basis, by their independent reductions and the invariant-dimension theorem. Keep the average as a symbolic node; enumerating its enormous sum is not an implementation instruction.

The two runs select bases separately over the two primes. Common pivot/free indices do not prove their entries are reductions of the same naively lifted rational matrix. For a common rational evaluation certificate, choose one projection-lifted basis and reduce that same basis at the other prime, or provide an exact basis transform. This obligation is included in the handoff.

For a target run, the analogous exact group-theoretic argument plus a reconstructible `(B24-274)=1894` residual minor and a complete 274-column modular kernel would certify its characteristic-zero invariant dimension. **That target certificate was not constructed here.** The inherited value a=274 remains the target dimension input.

## 4. Basis order, intertwiners, and the eight-box formula

Shapes are partitions with trailing zeroes removed, ordered in **descending lexicographic order**. `lambda/mu` is a horizontal four-strip exactly when `lambda_i >= mu_i >= lambda_(i+1)` and its size is four. No conjugation or vertical-strip convention is used.

Number a box `(r,c)` from zero in formulas and assign content `c-r`. A standard tableau is stored as the sequence of rows occupied by labels 1,2,...,N, in increasing lexicographic order. Positions within a row follow from the preceding shape. Columns of matrices are vectors; multiplying a generator on the left acts on a column. In the rational seminormal basis,

\[
s_i e_t={1\over q_i(t)}e_t+
\left(1+{1\over q_i(t)}\right)e_{s_it},
\quad q_i(t)=c_t(i+1)-c_t(i).
\]

The second term is omitted if the swapped tableau is nonstandard. In particular, same-row adjacent entries give +1, same-column entries -1. This is the convention actually implemented. It is a rational gauge of Young's seminormal representation; the defining relations were checked independently on all basis columns for shape `(4,2,2)`. The representation and multiplicity-free chain branching are the standard seminormal construction; see the primary [Okounkov–Vershik paper](https://www.esi.ac.at/preprints/esi333.pdf), especially its seminormal construction. The formulas, scaling, and specialization argument needed here are stated explicitly rather than delegated to that reference.

For a horizontal strip `lambda/mu`, the normalized Pieri embedding is

\[
i_{\lambda\mu}(e_t)=
\sum_{u\in\operatorname{SYT}(\lambda/\mu)}e_{t\sqcup u}.
\]

**There is no factorial divisor in this sum.** Its coefficient at every standard extension is one. In each two-tableau generator block, a constant coefficient vector is +1 invariant under the above convention; the same-row case also fixes it. Horizontal-strip Pieri gives precisely this one-dimensional S4-invariant extension and none for other shapes. Distinct predecessor shapes lie in distinct restriction summands.

If `M_(d-1,mu)` has ordered basis `v_(mu,alpha)`, the precursor basis is

\[
w_{\mu\alpha}=i_{\lambda\mu}(v_{\mu\alpha}),\qquad
B_\lambda=\sum_{\lambda/\mu\in HS_4}a_{d-1}(\mu).
\]

Write `U_mu[(nu,beta),alpha]` for the stored basis of `M_(d-1,mu)` inside its own precursor. At d=1 only shape `(4)` has invariant dimension one, with basis coefficient one; other partitions of four have dimension zero.

For each two-step endpoint nu, let

\[
\mathcal P_{\lambda\nu}=\{\mu:\lambda/\mu,\mu/\nu\in HS_4\},\quad c_{\lambda\nu}=|\mathcal P_{\lambda\nu}|.
\]

In the **eight-box** skew space with standard tableaux of `lambda/nu`, put

\[
b_\mu=\sum_{t:\,\mathrm{shape}(t_{1..4})=\mu/\nu}e_t.
\]

The local block F is determined by `tau b_mu = sum_eta F_(eta,mu) b_eta`. To compute it, apply the adjacent generators in the zero-based word

```text
3,2,1,0, 4,3,2,1, 5,4,3,2, 6,5,4,3
```

to each b column in sequence. It exchanges the first four and last four labels; its reverse is the same involution and is used by the independent rational checker. Read the output coefficient at the lexicographically first tableau of each eta path. Verify that coefficients are constant on that path and zero outside the allowed paths. This extracts F without solving an LR system. The local tables have at most `8!=40320` states, regardless of total N, and F has only `c_(lambda,nu)` rows and columns.

The full L-invariant coordinates are `(nu,beta,mu)`, ordered by nu descending, mu descending, then beta increasing. The precursor inclusion J is explicit:

\[
J_{(\nu,\beta,\eta),(\mu,\alpha)}
=\mathbf1_{\eta=\mu}\,U_\mu[(\nu,\beta),\alpha].
\]

Let `F_big = direct_sum_nu (F_(lambda,nu) tensor I_(a_nu))` in that order. Then

\[
\boxed{R_\lambda=(F_{big}-I)J},\qquad
U_\lambda=\operatorname{Nullspace}(R_\lambda).
\]

This is the implementable recurrence. The only nontrivial recoupling coefficients are the explicit local F entries. Multiplicity drivers are the predecessor dimensions and stored U matrices, not a claim that all horizontal-strip channels have multiplicity one after taking wreath invariants.

For example, at d=12, nu=`(17,11,2,2,2,2,2,2)` and paths
`(17,15,2^6)`, `(17,14,2^6,1)`, `(17,13,2^7)` in that order, the exact block is

\[
F=\begin{pmatrix}
1/35&-64/133&138/95\\
-17/140&125/133&69/380\\
68/105&128/399&3/95
\end{pmatrix},\qquad F^2=I.
\]

It is not Euclidean-orthogonal in this rational gauge. Its Gram pairing is essential if an orthogonal projection is used. All 65 top-level rational blocks for d=12 and d=24, including zero-multiplicity endpoints at the control, are in `exact_local_blocks.json`.

## 5. Gram and spherical normalization sheet

Give the row-superstandard seminormal tableau norm one. For any t, its squared norm is the product, over pairs of boxes whose row-reading order is reversed in t, of `(q-1)/(q+1)`, where q is the content of the lower-row box minus the content of the upper-row box. Such an inverted pair is incomparable and q is at most -2. This positive rational diagonal Gram satisfies self-adjointness of every adjacent transposition: for a valid swap, `g_(s_i t)/g_t=(q_i-1)/(q_i+1)`. The product formula makes the normalization independent of the chosen swap path.

For an embedding `i_(lambda,mu)`, define

\[
s_{\lambda\mu}=
\left[\prod_{\substack{x\in\lambda/\mu,\ y\in\mu\\\mathrm{row}(x)<\mathrm{row}(y)}}
{c(y)-c(x)-1\over c(y)-c(x)+1}\right]
\sum_{u\in\mathrm{SYT}(\lambda/\mu)}g^{local}_u.
\]

The product accounts for inversions between new and old boxes; `g^local` accounts for inversions among the four new boxes. Then

\[
G_W=\bigoplus_\mu s_{\lambda\mu}G_{M_\mu},\qquad
G_{M_\lambda}=U_\lambda^tG_WU_\lambda.
\]

In the L basis, the block `(nu,mu)` has Gram `s_(lambda,mu)s_(mu,nu)G_(M_nu)`. Calling this G_Z gives the actual spherical matrix

\[
\boxed{T=G_W^{-1}J^tG_ZF_{big}J}.
\]

No square roots, hidden orthonormalization, or unrecorded rescaling are used. The residual route needs none of these Gram inverses. The spherical implementation checked that this T agrees with the independent expression

\[
T={d\,U(U^tG_WU)^{-1}U^tG_W-I\over d-1}.
\]

All seminormal Gram factors are products/quotients of integers of magnitude at most N; they are units at p>N. The group average is self-adjoint, so its invariant summand is orthogonal to its complementary summand. The nondegenerate lattice pairing therefore restricts nondegenerately to each invariant summand. This justifies Gram inversion in the selected p-local bases, in addition to the direct checks of nonzero pivots. It does **not** assert that an arbitrary Gram matrix or arbitrary modular basis elsewhere in the repository has this property.

As a small universal example, in the permutation module of S3 with precursor basis `e3, e1+e2`,

\[
T=\begin{pmatrix}0&1\\1/2&1/2\end{pmatrix},\quad
P_H=\begin{pmatrix}1/3&2/3\\1/3&2/3\end{pmatrix},
\quad G_W=\operatorname{diag}(1,2).
\]

This illustrates both the double-coset formula and why an unweighted symmetric-matrix convention would be wrong.

## 6. Executed control and independent evidence

The new recursion constructed all 922 nodes including the degree-12 root. It returned precursor channels 12, 11, and 8 in descending shape order, hence B12=31. All 23 endpoint multiplicities matched the separate inherited Weyl computation, including its two zeros; their path-weighted sum is C12=239.

| Exact modular check | 2147483647 | 2147483629 |
|---|---:|---:|
| R dimensions | 239 by 31 | 239 by 31 |
| R rank / kernel dimension | 29 / 2 | 29 / 2 |
| Retained 29-minor | 1235010539 | 142343174 |
| Free precursor columns, zero-based | 25, 26 | 25, 26 |
| R U | zero | zero |
| H-projector trace | 2 | 2 |
| Full recursion wall time | 17.353 s | 16.643 s |

The row/column indices of the nonzero minors, full residuals, two-column U matrices, predecessor basis matrices at every node, and each local block needed to reconstruct the residual are retained. The free rows of U are the 2 by 2 identity. Python-integer elimination independently checked each retained minor and the complete R U product. The rational group/lattice proof in §3 is what turns this semantically checked dimension computation into the corresponding characteristic-zero invariant dimension; agreement of two modular kernels alone would not suffice.

The independent local checker uses backward corner-removal tableaux, Fraction arithmetic, sparse scalar updates, and the reversed reduced word. It checked all 23 control and 42 target blocks, F squared equals I, and pathwise constancy. The control blocks agree with the builder at both primes. It also checked 1,568 individual Coxeter column relations on the 56-tableau shape `(4,2,2)`. These checks test conventions; the general seminormal theorem, not finite test coverage, proves the recurrence for every partition.

The separate Gram implementation checked nondegeneracy at every constructed node, self-adjointness of T, T U=U, the double-coset/projector identity, idempotence, and trace. Its two expressions for T agree. Thus the successful dimension two is supported by matrix semantics and independent checks, not accepted because it is the desired small number.

### Fresh circuit calibration, explicitly a different source basis

The two banked s69 n4 seed fillings were evaluated on two new generic coefficient points and two new determinant pencils, with the same integer points at both primes. Coordinates are ordinary coefficients in recursive exponent order with the first exponent increasing. Generic seeds are 12030000 and 12030001 with coefficients in `[-31,31]`; determinant seeds are 12030100 and 12030101 with pencil entries in `[-7,7]`. Determinant expansion was checked by direct numerical substitution, and the nine matrix directions are independent at both primes. The complete integer matrices, exponent lists, and fillings are retained.

House symbols are `m_alpha=alpha! c_alpha=4! polarized(f)(e_i1,...,e_i4)`. Column antisymmetrizers are unnormalized sums, and the polynomial for a filling is the signed contraction product of these symbols. Each letter occurs four times, and the column-height weight is the stated lambda. These are valid highest-weight source vectors by the column-wedge construction.

| Fresh seed calibration | P1 minor | P2 minor |
|---|---:|---:|
| Generic 2 by 2 | 1332552299 | 305414543 |
| Determinant 2 by 2 | 949517201 | 17818470 |

All four matrices have rank two; the exterior evaluation took 6.46 seconds total for 16 entries. The separate determinant-polarization evaluator checks the eight determinant entries at both primes; its final check status and timing are in `calibration_independent.json`. It has no exterior-state recurrence. The paths share the already audited symbol packing conventions, so their independence is algorithmic rather than absolute. Fresh point construction and integer minor arithmetic are also retained.

These calibration minors are nonzero evaluations of explicit rational/integer source polynomials and therefore give characteristic-zero lower bounds. Together with dimension two, they prove that determinant restriction is injective on the entire control space, hence on any basis of it, including the recursive basis. They do **not** provide coordinates of those circuit vectors in the new recursive basis or the requested explicit evaluations of that basis. The n3 six-dimensional source, determinant rank five, unpadded per3 rank six, and its banked ideal line were read in the available S1 report and original inputs; they were not replayed in S3. The n3 comparison is never padded per2.

## 7. Exact unresolved evaluation map: four scalars at the control

Here is a fully specified conversion problem, with no unspecified basis or factorial.

Let t_c be the **column-superstandard** tableau of lambda. Let q_lambda be the tensor product, in column order, of unnormalized wedges `e1 wedge ... wedge e_(height)`. Both are fixed by the same column-subgroup sign character. Its multiplicity in S^lambda is one. There is a unique S_N-intertwiner Phi from the seminormal S^lambda to the lambda-highest-weight tensor space normalized by

\[
\Phi(e_{t_c})=q_\lambda.
\]

For a filling F_i, concatenate its two tall columns, its ordered short columns, and its singletons. Map the k-th occurrence of letter l to fixed tensor slot `4l+k`, with zero-based k. This defines the explicit permutation pi_i, stored in `pairing_handoff.json`. The two control permutations have adjacent-swap lengths **579 and 640**. The house polynomial of a recursive source vector v is

\[
F_v(f)=(4!)^{12}\langle\Phi(v),\widetilde f^{\otimes12}\rangle.
\]

Thus the banked circuits correspond exactly to `u_i=P_H rho(pi_i)e_(t_c)` in this model. For recursive basis vectors `v_0,v_1`, define the four entries

\[
A_{\alpha i}=\langle v_\alpha,\rho(\pi_i)e_{t_c}\rangle_G
=g_{t_c}\,[e_{t_c}]\,\rho(\pi_i^{-1})v_\alpha.
\]

The explicit global norm here is

```text
g_tc = 260219038130785936600032618419240717460731768774188862903040000000000
```

Let `C=G_M^{-1}A`. Then `u_i=sum_alpha C_(alpha,i)v_alpha`, and column evaluation vectors satisfy

\[
\mathrm{ev}_{circuit}=C^t\mathrm{ev}_{recursive},\qquad
\mathrm{ev}_{recursive}=(C^t)^{-1}\mathrm{ev}_{circuit}.
\]

Both bases span the two-dimensional source, so C must be invertible once the pairings are correctly constructed. The coefficient formula is exact and its input permutations and Gram are supplied. The missing implementation is **computing these four arbitrary-permutation matrix coefficients from the compact DAG without expanding the ambient Specht basis**. Last-eight-slot recoupling solves adjacent whole-block swaps; it does not automatically implement arbitrary pi_i on the compressed source.

Applying each adjacent transposition to an expanded vector can double support, with crude bounds `2^579` and `2^640`. Those are algorithmic upper bounds, not measured supports or complexity lower bounds. No such expansion was attempted. A general natural/seminormal transition formula also does not by itself provide the required compact cost; see the primary [Armon–Halverson transition-matrix paper](https://arxiv.org/abs/2012.03828). This session does not promote its existence into an evaluation bridge.

The alternative missing primitive is an evaluator for `i_(lambda,mu)(v_(mu,alpha))` on form tensors with a controlled contraction width. Merely solving for a basis transform from sampled values assumes that evaluator already exists and is circular here. Four pairing entries at the control are the smaller concrete interface.

## 8. Census, arithmetic, storage, and scaling cost

The independently enumerated topology is:

| d | One-strip predecessors | Two-strip paths | Endpoints nu | Maximum paths per endpoint |
|---:|---:|---:|---:|---:|
|12|3|36|23|3|
|13|12|136|35|10|
|14|12|160|42|10|
|24|12|160|42|10|

The saturation assertion concerns this two-step shape pattern. The actual recoupling coefficients still depend on box contents and are not copied unchanged from d=14 to d=24.

The repository's DAG driver reports nodes **below** the root. Its 921 and 7656 therefore mean **922 and 7657 including the root**. The peak shape counts remain 189 and 585. This is an indexing convention correction, not a disagreement in the enumerated graph.

For the completed control DAG, the weighted layer totals from d=1 through 12 are

```text
1, 3, 8, 24, 61, 115, 170, 203, 195, 137, 31, 2
```

Hence `C_total=950`, `C_peak=203`, including the root; excluding the root, total is 948. Neither is the two-step carrier C12=239. Storing all inclusion matrices uses **40,427 field entries**, a further cost not captured by a count of multiplicity coordinates alone. The largest node has B=128; maximum C is 820; maximum actual C*B is 104,960. These are control measurements, not target predictions.

There were 3,916 local blocks computed in the control DAG; its largest local skew tableau space had 2,520 states. At the **top** control and target levels the rational-block totals are respectively:

| Quantity | d=12 top | d=24 top |
|---|---:|---:|
| Local F entries, sum c_nu squared | 68 | 852 |
| Total local skew tableaux across endpoints | 3430 | 10688 |
| Largest local tableau space | 560 | 1120 |

Thus neither a dense C by C action nor the global Specht carrier is necessary. The compact action is block diagonal, repeated on multiplicity indices. Forming C explicitly is optional: process one endpoint block at a time, or stream its residual rows into elimination.

For a general node v=(d,lambda), define `t_(lambda,nu)=#SYT(lambda/nu)` for its eight-box skew shape. In field operations, the explicit implementation has bounds

\[
\begin{aligned}
\text{local coefficients}&:\ O\left(16\sum_\nu t_{\lambda\nu}c_{\lambda\nu}\right),\\
\text{residual assembly}&:\ O\left(B_v\sum_\nu a_\nu c_{\lambda\nu}^2\right),\\
\text{dense elimination}&:\ O\left(C_vB_v\min(C_v,B_v)\right),\\
\text{stored recursive inclusions}&:\ \sum_v B_v a_v\text{ entries}.
\end{aligned}
\]

Full residual storage is O(C_v B_v); streamed elimination reduces the working elimination array to O(B_v squared), plus the largest endpoint and predecessor data. The supplied implementation retains full small residuals to make checking simple. It caches local tableaux, so its Python-object overhead is not a target peak-RAM estimate. A production version should release local tableaux after saving F and record measured peak bytes.

At inherited B24=2168, a dense square workspace has 4,700,224 entries, or **37,601,792 bytes** in int64. A 2168 by 274 inclusion has 594,032 entries, or **4,752,256 bytes**. The 852 top local F residues use 6,816 bytes before metadata. These exact storage counts exclude all predecessor matrices and evaluator state.

At the two house primes, residues are reduced after every multiply-add. A product is below 2^62; the local update adds at most two such products, below 2^63. Long dot products are not left to unchecked int64 `matmul`; they are accumulated with reduction at every step. Scalar inverse and determinant checking uses Python integers. Rational local verification uses `Fraction`. No floating-point rank arithmetic is used.

### C24 measurement and rigorous bounds

A separate **dimension-only** fallback had a 120-second soft budget and B cap 768. It stopped after 123.699 seconds at a recursion boundary, with 2237 completed nodes, maximum completed B=278 and C=2167, and 9146 measured multiplicity coordinates on that partial node set. It completed **zero of the 42 requested degree-22 endpoint multiplicities**. It did not construct W24. Counts from this partial run are a cost observation, not a completed target certificate; no second-prime replay or claim of a complete weighted DAG is attached to them.

For a rigorous fallback bound, put `Q=(S^lambda)^(S4^d)` as an S_d-module. Only shapes `(d)`, `(d-1,1)`, `(d-2,2)`, and `(d-2,1,1)` contribute to its S_(d-2)-invariants. If their multiplicities are a,b,c,e, then

\[
B=a+b,\qquad C=a+2b+c+e\ge2B-a.
\]

With inherited a24=274 and B24=2168 this gives **C24 >= 4062**, conditional on those inherited count inputs. This lower bound is not inferred from a sampled residual.

For the upper bound, every highest-weight multiplicity `a22(nu)` is at most its ordinary weight-space dimension in `Sym^22(Sym^4)`. An exact tail-multiset DP computed all 42 such weight dimensions and their path-weighted sum:

\[
\boxed{4062\ \le C_{24}\ \le 2243638614682}.
\]

The upper bound is deliberately loose and does not validate the historical estimate 1.7 times 10^4. Its integer computation checked every addition for overflow; the largest intermediate was 156346649229, and the largest DP array used 7,243,344 bytes. All 42 terms and the recurrence are supplied. Exact C24 remains **OPEN**. The next measurement should continue with checkpointed compact inclusions or a separately verified multiplicity engine, not extrapolate a one-level ratio.

Conversion/evaluation has a separate unresolved cost: four coefficient queries at d=12, then a controlled general evaluator or circuit conversion. A short block-swap recurrence does not bound arbitrary-permutation width or prove a usable target evaluation runtime. No polynomial-in-growing-n claim, n5 cost extrapolation, or claim that these measurements settle Valiant asymptotics is made.

## 9. Executable handoff and exact stopping point

The executable scripts and replay commands accompany this report. The recurrence is:

```text
build(lambda):
  if |lambda|=4: return the trivial (4) basis or zero
  build every horizontal-four-strip predecessor mu
  order W columns (mu, alpha)
  for each two-step endpoint nu:
      compute F(lambda,nu) on eight-box tableaux
      insert predecessor U_mu slices into J_nu
      append rows of (F(lambda,nu) tensor I - I) J_nu
  take deterministic RREF kernel with free columns in increasing order
  retain original residual rows/columns, pivot minor, U and normalization
```

The next bounded implementation task for s75, through the integrator, is the four pairing entries in §7. Inputs are the saved U DAG, Gram_M, the two explicit permutations, and g_tc. Use a compact matrix-coefficient or tensor-contraction algorithm. Precommit to at most 30 minutes for the first control implementation trial and a measured 256 MiB workspace cap for any new coefficient routine; checkpoint the exact unfinished coefficient and its width if the cap is reached. Those are proposed **next-task bounds**, not durations this session claims to have run. Do not expand the target ambient carrier.

Once A is obtained, compute C, verify it is invertible, and use `(C^t)^-1` to evaluate the **same recursive vectors** at the retained generic and determinant points. Verify one rational common-source convention or explicitly transport across the two modular bases. Independently check the converted two-minors and the normalization against direct circuit evaluation. Only then pass the complete control and scale source construction.

At the target, retain all twelve B24 terms, all 42 C24 terms if using that carrier, the weighted DAG/edge totals, the 1894-minor, the complete 274-column kernel, and independent evaluation evidence. An exact dimension result alone still does not supply padded rank 274 or determinant rank 273.

## 10. Claim ledger and frozen rank status

| Claim | Status | Evidence or remaining obligation |
|---|---|---|
| Double-coset identity and fixed-space equivalence | PROVED | Explicit subgroup averages and generation |
| Good reduction for the specified model at p>4d | PROVED | Stable free p-local lattice, idempotent direct summands, unit denominators |
| Exact compact residual and Gram/spherical formula | PROVED / implemented | Explicit eight-box seminormal recurrence and predecessor inclusions |
| 31-to-2 invariant control | CERTIFIED | Both primes; 29-minors, full kernels, group-model transfer, independent scalar checks |
| C12=239 and its 23 terms | CERTIFIED count reproduction | New recursion agrees term by term with inherited Weyl table |
| Target 42 rational local swap blocks | Exact verified artifacts | No target fixed basis or evaluation follows merely from these blocks |
| Fresh n4 banked circuit ranks | Certified lower bounds, separately normalized source | Explicit points and nonzero minors; independent determinant entries checked in attached log |
| Abstract determinant injectivity on the control space | PROVED from dimension and fresh minor | Basis-independent consequence; does not supply recursive evaluation entries |
| Explicit evaluation of the newly recursive n4 basis | OPEN | Four compact pairing coefficients not computed |
| B24=2168, a24=274 | Inherited BANK | No completed second-engine target reproduction here |
| Exact C24 / full target weighted cost | OPEN | Bounded count run incomplete; rigorous bounds supplied |
| Complete usable 274-vector target basis | OPEN / PARK pending control evaluation | Compact construction exists as an algorithm; target run not delivered |
| Target determinant rank 273 / padded rank 274 | OPEN / OPEN | No qualifying target evaluation minors supplied |

The frozen target remains `lambda=(65,17,2^7)`, `delta=24`, `r=9`, `a=274`. In common source coordinates, `i_X=274-rank(T_X)` and `D=rank(T_pad)-rank(T_det)`. LMR supplies **determinant rank at most 273**, not equality. S3 adds no target determinant or padded evaluation lower bound. The earlier S1 transported determinant lower bound two remains separately reported evidence, not a new S3 target computation.

True padding is **ell times per3**; the reducible comparison is ell times a general cubic. Neither was evaluated at the target here. A certified determinant lower bound 273 would close its half without a full 274-vector source. A valid true-padded 274-minor would also certify independence of its source vectors. Stalled finite evaluation ranks imply only lower bounds, never a rational kernel or D<=0. If future exact ranks are both 273, retain and compare kernel orientation in common coordinates. No D conclusion is promoted by this session. The r=5 theorem still requires global completeness and valid exceptional-image bounds.
