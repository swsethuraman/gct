# Equal-quartic compatibility without an ambient highest-weight basis

16 September 2026. Characteristic zero. This investigation uses one family: partial transposition of a block diagonal 2+2 determinant pencil. Historical files were read, not changed. No claim of literature priority is made.

**Verdict.** Equal-quartic pencils give globally necessary scalar constraints without constructing any ambient highest-weight polynomial. This investigation constructs an explicit nonzero constraint in the five-row cell `(d,lambda)=(3,(4,2,2,2,2))`, with exact values at a simple pair of pencils. However, it proves that this constraint adds **zero** information to the present arc in that cell: the arc already has full rank two. It also proves that this entire family is blind on every five-row rectangle `(4k)^5`. No positive five-row increment over the arc is claimed.

**Source, target, and construction.** Retain the established row model, with `W=Mat_4`, `H=Stab(det_4)` including whole-matrix transpose, and

`M_lambda=(S_lambda W)^H`, `|lambda|=4d`.

Its vectors are highest-weight polynomials `q(Y_1,...,Y_r)` in matrix tuples, invariant under determinant-preserving simultaneous left/right operations and simultaneous transpose. Write

`phi_r(Y)=det(sum_i x_i Y_i)`,

`E_lambda=phi_r^*(A_{d,lambda}) subset M_lambda`

for the actual determinant coordinate subspace. Positive partition labels refer to the coefficient/row convention; the corresponding coordinate modules on the sixteen-variable orbit closure carry the dual label.

Take arbitrary `r`-variable 2x2 pencils `A(x),D(x)`, and set

`B(x)=diag(A(x),D(x))`, `B'(x)=diag(A(x)^T,D(x))`.

Then `det B=det A det D=det B'`, as an identity, including all singular specializations. For a fixed rational pair define

`C2_{B,B'}: M_lambda -> Q`, `q -> q(B_1,...,B_r)-q(B'_1,...,B'_r)`.

This is the proposed additional condition. One can also package all such pairs in the single restriction map

`D_lambda: M_lambda -> Q[A_i,D_i]_(2d,2d)`,

`(D_lambda q)(A,D)=q(diag(A_i,D_i)_i)-q(diag(A_i^T,D_i)_i)`.

For `r=5` there are 40 block-entry variables, 20 of each kind. The bidegree follows by applying the determinant-preserving left operation `diag(t I_2,t^-1 I_2)` and using total degree `4d`. Evaluating this polynomial at a fixed pair produces the scalar map above; its full monomial target never needs to be constructed. For example at `d=3`, the unrestricted bidegree target has `binom(25,6)^2=31,364,410,000` monomials, whereas our executed map is just a `1 x 2` row.

**Why every determinant coordinate function satisfies it.** If `q=h o phi_r`, then

`C2(q)=h(det B)-h(det B')=0`.

Every homogeneous coordinate function on the determinant closure has an ambient homogeneous representative, since its coordinate ring is a graded quotient of the ambient polynomial ring. Therefore this identity applies to all determinant coordinate vectors in the stated common source. The definition does not require computing that representative or a basis of its ambient space.

There is no appeal to normalization, boundary coverage, closedness of an auxiliary projection, or an unproved geometric hypothesis. The pair consists of actual representations. There are no matrix-factorization witnesses of the form `MN=F I`.

This is a necessary descent condition, not a sufficiency theorem. Even equality on every set-theoretic fiber can fail to imply polynomial descent: `t -> (t^2,t^3)` has singleton fibers but the polynomial `t` is not in `Q[t^2,t^3]`. A few such pairs impose still less. Accordingly, a survivor of all tests used here is not thereby proved to extend.

**Removing the immediate redundancies.** If two tuples differ by determinant-preserving left/right operations or whole-matrix transpose, then every `q in M_lambda` already takes equal values on them. Those pairs give zero maps. Partial transpose is not such an operation in general. The explicit nonzero below proves that our two tuples are not related by the full stabilizer. This distinguishes a genuinely nonzero fiber test from a stabilizer identity; it does not prove independence from `C`.

The old all-matrix-coefficients arc test is also unchanged by a fixed left group translate or a simultaneous transport of source and arc. Replacing the parameter by `c t^m` preserves its kernel when the allowed homogeneous degree interval is scaled accordingly. Our test has a different definition, but the only decisive independence criterion remains its restriction to the old kernel.

**An exact five-row example.** Use

```text
A(x) = [[x1,x2], [x3,x4]],
D(x) = [[x1,x2], [x3,x5]].
```

The two block diagonal pencils are representations of the same genuine five-variable quartic

`F=(x1*x4-x2*x3)*(x1*x5-x2*x3)`.

The five coefficient matrices are linearly independent. Work in `d=3, lambda=(4,2,2,2,2)`. A fresh exact character calculation gives connected and full-stabilizer multiplicities `g=s=2`. The ambient multiplicity is `a=0`: a constituent of `Sym^3(Sym^4 C^5)` has at most three rows. This is a mechanism diagnostic, not an equation or padding-separation cell.

Here are fully specified integral carrier polynomials. Use slots `0,...,11`; a slot coordinate is `c_k=(a_k,b_k)` in `{0,1,2,3}^2`. Put

`Delta(c_0,...,c_4)=det[(Y_i)_(a_k,b_k)]_(i=1,...,5; k=0,...,4)`

and similarly for slots 5 through 9. With `epsilon(0,1,2,3)=1`, define

`P_(pi,rho)=sum_c (prod_(T in pi) epsilon(a_T)) (prod_(T in rho) epsilon(b_T)) Delta(c_0,...,c_4) Delta(c_5,...,c_9) (Y_1)_(c_10) (Y_1)_(c_11)`,

`q_(pi,rho)=P_(pi,rho)+P_(rho,pi)`.

All slot lists below are ordered:

```text
q1:
pi  = ((8,6,1,4), (7,5,3,0), (11,9,10,2))
rho = ((1,10,3,6), (0,7,8,9), (4,2,11,5))

q2:
pi  = ((3,9,0,5), (8,1,6,11), (10,7,4,2))
rho = ((1,10,11,2), (9,6,4,3), (7,5,8,0))
```

Two full five-label wedges and two copies of label 1 give highest weight `(4,2,2,2,2)`. The three row epsilons and three column epsilons give the factor `(det L det R)^3` under simultaneous `Y_i -> L Y_i R`, hence invariance whenever `det L det R=1`. Transpose interchanges the ordered partitions, so the sum is invariant under the full stabilizer. Thus membership is proved directly, without ambient polynomials. A two-point evaluation determinant `418914 mod 524287` proves independence. Together with `s=2`, this certifies a complete source basis for this small cell.

The sparse integer calculation gives:

| Vector | At B | At B' | C2 |
|---|---:|---:|---:|
| q1 | -496 | 224 | -720 |
| q2 | 816 | -624 | 1440 |

Thus `C2=(-720,1440)` is a nonzero globally necessary map in an exactly five-row cell. Already the single explicit `q1` proves this assertion; a complete source basis is needed here only to conclude the rank comparison below. The quartic identity is proved by block determinants, independently of the carrier arithmetic.

**Comparison with the present arc.** In the established adapted coordinates, gamma weight equals `2d-j` on the invariant source, where `j` is degree in the three-dimensional skew coordinate space. At this partition, `j<=lambda_1+lambda_2+lambda_3=8`. Therefore the forbidden degrees are `j=7,8`. Nine nodes `u=0,...,8` recover every coefficient of each specialized polynomial in `u`.

The stored two generic tuples and interpolation samples give these four rows of the arc test modulo `p=524287`:

```text
278271  517626
225875  379213
359281  191966
 30731  122924
```

The first two rows have determinant `61631 mod p`, nonzero. They are evaluations of actual forbidden coefficient polynomials, so this proves a characteristic-zero rank floor two. The source dimension is two; consequently

`rank_Q C=2`, `ker C=0`,

`rank_Q C2=1`, `rank_Q [C;C2]=2`.

The rank increment is **zero**. This is stronger than merely failing to find a witness: no globally necessary additional test can remove an arc survivor in this cell, because there are none. The nonzero fiber functional cannot be advertised as five-row progress beyond the arc.

**A structural obstruction for this pair family.** Before building a large carrier, apply the following representation filter. The restriction to `diag(A,D)` is invariant under an independent `SL_2 x SL_2` acting on each block. On `Mat_2`, this connected group has image `SO_4` for the determinant quadratic form, and transpose is an orthogonal reflection. An `SO_4` invariant in the reflection-odd sector has label `alpha` with exactly four odd positive parts. This parity input is the orthogonal sign-isotypic statement of Lemma 6.6 in [Howard--Millson--Snowden--Vakil, The ideal of relations for the ring of invariants of n points on the line, printed p. 33](https://ems.press/content/serial-article-files/31806).

Here is its application to our map. Let `R(q)` denote block restriction, and let `tau_A,tau_D` transpose the two blocks. Whole-transpose invariance says `tau_A tau_D R(q)=R(q)`. Therefore

`D_lambda q=(1-tau_A)R(q)`

is odd under **each** of `tau_A,tau_D`. It belongs to the tensor product of the two odd sectors. Since its block degrees are `2d,2d`, a necessary condition for a nonzero map on type `lambda` is

`c^lambda_(alpha,beta)>0`

for partitions `alpha,beta` of `2d`, both with exactly four odd positive parts. This is a finite Littlewood--Richardson support check, with no ambient highest-weight basis. Passing it is only a necessary filter; the restriction map itself may still be zero.

For the five-row rectangle `lambda=(m^5)`, with even `m`, this support is empty. Indeed, if `det^m` occurs in `S_alpha(C^5) tensor S_beta(C^5)`, Schur's lemma forces

`beta=(m-alpha_5,m-alpha_4,m-alpha_3,m-alpha_2,m-alpha_1)`.

If this is not a polynomial dominant weight there is no occurrence. Otherwise `alpha` has exactly four rows, so `alpha_5=0` and `beta_1=m`, an even positive part. That contradicts the odd-sector condition on `beta`. This proves

`D_(4k)^5 = 0` on the entire full-stabilizer source, for every `k>=1`.

The same complement argument proves blindness on even rectangles with more than four rows, in particular the earlier `(d,lambda)=(6,(4^6))` diagnostic. Thus partial transpose of 2+2 blocks cannot replace the previous two-point test there. That previous test used two different quartics and knowledge of the one-dimensional ambient space; it is not contradicted by this obstruction. Other equal-quartic families are not ruled out.

**The bounded test and its cost.** The executed pilot used one process with a 60-second, 512-MiB Job Object cap. Inputs were the stated partition, the exact character formula, full-H epsilon contractions, and the existing adapted arc. It allowed at most 48 proposed contractions at two fixed-seed generic points and retained two independent columns after 11 attempts. Every contraction plan was priced before use and rejected above `2^24` intermediate entries or `10^8` contraction operations. Distinct column tensors have heights 5 and 1; the larger contains `16^5=1,048,576` residues, 8 MiB. No tensor with `16^12` entries was formed.

The retained linear algebra consists of a `2 x 2` source evaluation, a `4 x 2` sampled arc matrix, and a `1 x 2` compatibility row. The arc needs 2 tuples times 9 nodes times 2 vector evaluations. At the simple equal-quartic pair the height-five column has just `5! * 2^3=960` nonzero assignments; exact sparse contraction avoids a dense tensor altogether.

The wrapped pilot finished in 17.90 seconds, using 224,456,704 bytes peak commitment and 239,177,728 bytes peak working set. The exact pair was then evaluated separately. An independent modular tensor contraction agrees with its integer values, and a separate Lagrange interpolation implementation reproduces the arc rows obtained by the producer's Vandermonde solve. Whole-transpose controls also pass. These are independent arithmetic paths, not an external peer review.

The predeclared stop was full arc rank: after reaching rank two there is no reason to enlarge the pair sample in this cell. A rank-deficient sampled arc would instead have been inconclusive. The other failure conditions were insufficient carrier rank within the caps, a zero compatibility row, or disagreement in verification. None can be converted into a geometric conclusion beyond the inputs actually certified.

One additional small check tested an attempted pole-canceling shortcut: the ambient quinary degree-five rectangular invariant `H5` was nonzero at two arc endpoints, with residues `420343,25268 mod p`. Thus it does not vanish identically there and cannot provide a universal boundary-vanishing multiplier for this construction. This check rules out only that proposed multiplier, not products or cancellations in general.

**What a positive next test must certify.** For any future five-row cell passing the odd-sector support filter, the minimal useful input is one explicitly represented `q in M_lambda` with an exact proof `Cq=0`. Evaluate the same block-pair difference on `q`; one nonzero exact value then proves an added constraint. Neither a complete ambient basis nor a complete source basis is required for this one-vector certificate. Constructing or certifying the arc-kernel vector, rather than evaluating the equal-fiber row, is now the bottleneck.

If a certified kernel matrix `N_C` is available instead, compute `C2 N_C`. Precisely,

`rank [C;C2]=rank C+rank(C2 N_C)`.

An exact witness proves a positive increment; a nonzero modular minor of correctly defined rational matrices certifies a rank floor. Modular sampled zeros do not establish that a lifted vector belongs to the exact arc kernel. Likewise a lower bound on the stacked rank does not prove an increment over an old rank that is known only from below.

**Scope of the result.** The explicit pair proves that cheap equal-fiber compatibility can detect non-descent in five-row source spaces. The completed rank computation supplies no evidence that it detects false *arc survivors* in five rows. The rectangular obstruction gives an all-degree negative for this particular family. What remains unproved is a named nonrectangular five-row cell and an explicit `q in ker C` with `D_lambda q !=0`, preferably with positive ambient multiplicity. This report provides no determinant equation, no padding separator, and no multiplicity gap. Even a positive source-rank increment would not imply any of those without the relevant ambient/padding rank evidence.

**Reproduction and evidence.** `pilot.py/json` contain the exact contraction descriptions, fixed sample tuples, modular values, and arc rows. `exact_pair.py/json` contain the sparse integer evaluator and both pencils. `verify.py` and `verification.json` record the independent checks. `rectangular_factor_check.py/json` record the separately scoped multiplier falsification. The original preflight and wrapper resource record are retained. Run the scripts using the existing B15-02 Python environment; only `pilot.py` imports the historical carrier implementation, whose SHA-256 is pinned in `pilot.json`. `MANIFEST.json` binds this report, new evidence, and the historical mathematical/code inputs.
