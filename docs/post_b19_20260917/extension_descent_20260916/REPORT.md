# An explicit false survivor, and a finite route to five-row equations

16 September 2026. Characteristic zero. This is a new, bounded investigation; historical batch files were read but not edited. No claim of literature priority is made.

**Verdict.** Yes: an additional global polynomial-descent condition detects an explicit vector in the requested cell `(d,lambda)=(6,(4^6))` that the present boundary arc admits. The new condition is a single scalar linear functional on the same ten-dimensional full-stabilizer multiplicity space. Its rank is exactly one, while the old map has rank zero. This removes a false survivor but leaves the clipped determinant bound equal to one. It produces neither a determinant equation nor a multiplicity gap.

For the independent five-row assignment, the selected route is **certified interpolation of the coefficient pullback in a complete full-stabilizer carrier**. Its certification step does not use the boundary arc or require an orbit-bound dimension deficit. It can turn a sampled candidate into a global polynomial identity. Its cheap pilot at degree six, type `(12,8,2,1,1)`, is negative: an exact determinant nonzero proves that this cell contains no determinant equation. The larger carrier was therefore not built. No explicit five-row determinant equation is claimed.

**Conventions and inherited inputs.** Let `W=Mat_4` be the sixteen-dimensional space of determinant variables, `G=GL(W)`, `f=det_4`, `X=closure(G f)`, and `H=Stab(f)`, including transposition. Write `M_lambda=(S_lambda W)^H`; coordinate modules on `X` have the dual label `S_lambda(W*)`. When working directly with forms on `C^r`, use ordinary coefficient functions `c_alpha(F)=[x^alpha]F`, with positive weights. Highest-weight coefficient polynomials have label `S_lambda(C^r)` in this convention. These are the usual dual presentations of the same finite multiplicity calculation.

The row model realizes `M_lambda` as polynomials `q(Y_1,...,Y_r)` in `r` matrices, of row-label highest weight `lambda`, invariant under determinant-preserving simultaneous left/right operations and under simultaneous transposition. In this model the actual determinant coordinate subspace is

`E_lambda = phi_r^*(A_{d,lambda}) subset M_lambda`,

where `A_{d,lambda}` is the ambient coefficient highest-weight space and `phi_r(Y)=det(sum x_i Y_i)`. This follows from equivariance of coefficient pullback and the row-model/Peter-Weyl identification; it identifies positions of subspaces, not just their dimensions.

Adopted from the reviewed B19-01 calculation: at `(6,(4^6))`, `a=1`, `s=10`, and `C=0`. At `(3,(2^6))`, `a=0`, `s=1`, and `C=0`. We prove the first cell's `m_det=1` afresh below by an exact ambient nonzero. The latest B19-02 report/review closes the degree-five rectangle and records `I(D45)_d=0` for all `d<=5`. That latest review, rather than the older '22 determined, one bounded' statement, is the input used here. This investigation does not replay the entire degree-five certificate.

## 1. What the current arc actually checks

In the adapted coordinates of B17-02,

`gamma(t) f = Q0 + t Q1 + t^2 Q2`,

where `Q0=a v^T S v-(r v)(v^T c)`, `Q1=r A(Sv)c`, and `Q2=a det S-r adj(S)c`. The weights on `(a,r),v,(c,S)` are `-1,0,+1`.

For `z in M_lambda`, the matrix coefficients on the orbit are `h_{ell,z}(g f)=ell(g z)`. If they extend to homogeneous coefficient-degree `d` functions on `X`, then

`ell(gamma(t)z)=P_ell(Q0+tQ1+t^2Q2)`

has powers only in `[0,2d]`. Thus

`C(z)=(pr_k z)_{k<0 or k>2d}`.

The lower bound is regularity at `t=0`. The upper bound is the homogeneous degree constraint, equivalently regularity at the opposite end after multiplying the pullback by `t^(2d)` and replacing `t` by `t^-1`. Together these say that every pullback is a section of `O_{P1}(2d)` on this parametrized projective curve. They do not require that these sections arise from a common coefficient polynomial on `X`.

On the stabilizer-invariant source, row-torus invariance gives first-grid-row degree `d`, hence gamma weight `2d-j` for skew degree `j`. For `lambda=(4^6)`, the three-dimensional skew space can have degree at most `lambda_1+lambda_2+lambda_3=12`. Consequently no source vector has a forbidden exponent at `d=6`.

Precision correction to the older report: this proves `C=0` on the invariant source. The whole Schur module can still have negative gamma weights, since its first-grid-row degree need not equal `d`. No claim that the entire negative-weight carrier is empty is needed.

Passing one such curve cannot establish extension. It omits other geometric directions and, even more basically, polynomial descent to the original coefficient ring. A valuation-only approach through normalization needs a separate descent argument if the original closure is nonnormal. Our new condition below uses the original coefficient ring directly, so neither normalization nor boundary coverage is assumed.

## 2. The one additional condition: finite polynomial-descent compatibility

Choose an exact basis `h_1,...,h_a` of `A_{d,lambda}` and finitely many matrix tuples `Y^(1),...,Y^(N)`. Form

`A_T = ( h_i(phi_r(Y^(j))) )_{j,i}`.

Define the linear map

`C2_T : M_lambda -> Q^N / im(A_T)`,

`q -> [(q(Y^(1)),...,q(Y^(N)))]`.

Extend scalars to `C` if desired. This is an explicitly finite regularity test: do the values of the orbit function satisfy the linear compatibility required of a homogeneous polynomial in quartic coefficients? It does not define the unknown target using `E_lambda`, an unknown ideal, or an unknown boundary classification. Its inputs are ambient coefficient polynomials and actual pencils.

**Necessity proof.** If `q` comes from a determinant coordinate function in this cell, then `q=phi_r^*(sum_i u_i h_i)` for some constants `u_i`. Substitution at every tuple gives `ev_T(q)=A_T u`, so `C2_T(q)=0`. This is an identity on all matrix tuples. It is valid on singular tuples, on arbitrary frames, and on every function of the original affine closure. It needs no normality, no exhaustive chart cover, and no geometric conjecture. The identification with an ambient homogeneous representative is valid because the closure coordinate ring is a graded quotient of the ambient polynomial ring. QED.

This method pays for knowledge of the ambient highest-weight space. It is a polynomial-descent test, not a new boundary divisor or a new valuation theorem.

**When finite evaluations suffice.** Suppose `q_1,...,q_s` are a certified basis of `M_lambda` and the `N x s` matrix `S_T=(q_i(Y^(j)))` has column rank `s`. Then evaluation is injective on the whole carrier. Since both `q` and `phi_r^*h` belong to this carrier, equality of their values implies equality as polynomials. Therefore

`ker C2_T = E_lambda`.

Independent polynomials admit an injective evaluation map at `s` suitable points: inductively choose a point not annihilating a nonzero polynomial in the remaining kernel. Integer tuples suffice over `Q` by Zariski density. This proves existence of such points, not that an arbitrary fixed sample or a bounded search finds them.

## 3. An explicit invariant missed by the arc

Use slots `0,...,11` and six matrices `Y_1,...,Y_6`. For a slot assignment `c_k=(a_k,b_k)` in `{1,2,3,4}^2`, set

`Delta(c_0,...,c_5)=det[(Y_i)_{a_k b_k}]_{i=1,...,6; k=0,...,5}`,

and similarly for slots `6,...,11`. Epsilon has convention `epsilon(1,2,3,4)=1`; the following slot lists are ordered and zero-based:

```
pi  = ((0,1,6,7), (2,3,8,9), (4,5,10,11))
rho = ((3,1,10,9), (5,2,11,6), (4,0,8,7))
```

Define the finite polynomial

`P_{pi,rho}(Y) = sum_c [prod_{B in pi} epsilon(a_B)] [prod_{B in rho} epsilon(b_B)] Delta(c_0,...,c_5) Delta(c_6,...,c_11)`,

and put `Q=P_{pi,rho}+P_{rho,pi}`.

**Representation and stabilizer proof.** Each six-slot determinant transforms by `det(g)` under mixing the six matrices by `g in GL_6`; hence `Q` has row-label character `det(g)^2`. Three row-index epsilon tensors and three column-index epsilon tensors transform by `(det A det B)^3`, so they are invariant when `det A det B=1`. Simultaneous transpose interchanges `pi` and `rho`; `Q` is therefore fixed by the full stabilizer. Thus `Q in M_(2^6)`, with total matrix-entry degree 12 and coefficient degree 3. Its square

`z_* := Q^2 in M_(4^6)`

has total matrix-entry degree 24 and coefficient degree 6. The nonzero evaluations below also prove these are nonzero polynomials. By the silence calculation, `C(z_*)=0`.

Define two explicit pencils:

```
K(x) = [[ 0,  x1,  x2,  x3],
        [-x1,  0,  x4,  x5],
        [-x2,-x4,   0,  x6],
        [-x3,-x5, -x6,   0]]

L(x) = [[x1,x5, 0, 0],
        [ 0,x2,x5, 0],
        [ 0, 0,x3,x6],
        [x6, 0, 0,x4]]
```

Their quartics are

`F_K=(x1*x6-x2*x5+x3*x4)^2`,

`F_L=x1*x2*x3*x4-x5^2*x6^2`.

Let `T_ijkl=alpha! c_alpha`, where `alpha=e_i+e_j+e_k+e_l`, and define

`H6(F)=sum_{sigma,tau,upsilon in S6} sign(sigma)sign(tau)sign(upsilon) prod_{i=1}^6 T_{i,sigma(i),tau(i),upsilon(i)}`.

Its full four-epsilon contraction is `6! H6`. This proves its weight `(4^6)` and raising annihilation by the alternating-tensor identity. It is a coefficient-degree-six ambient polynomial. Since the accepted ambient multiplicity is one and `H6(F_L)!=0`, it spans `A_{6,(4^6)}` and proves `m_det=1`.

Exact values, computed in the stated integral normalization:

| Pencil | `Q` | `Q^2` | `H6(det pencil)` |
|---|---:|---:|---:|
| `K` | -86,400 | 7,464,960,000 | 1,290,240 |
| `L` | -720 | 518,400 | 1,152 |

Thus `H6(F_K)=1120 H6(F_L)`. Specialize the single additional condition to

`C2 : M_(4^6) -> Q`,

`C2(q)=q(K)-1120 q(L)`.

Every determinant coordinate vector in this cell is a scalar multiple of `H6 o phi_6`, so necessity follows both from Section 2 and directly from the displayed values. But

`C2(z_*) = 6,884,352,000 != 0`.

Equivalently the evaluation minor with columns `(H6 o phi_6, Q^2)` and rows `(K,L)` is `-7,930,773,504,000`.

This is the requested false survivor in the preferred cell, with no hypothetical geometric input. Its construction is independent of knowing a complete ten-vector source basis. The new scalar map has rank one, and the combined map has rank one because `C=0`. The surviving source has dimension nine; the clipped bound is still `min(1,9)=1`. We have detected one of the nine missing dimensions, not certified that this one functional detects all nine.

The smaller control is `(3,(2^6))`: `Q` is an explicit nonzero vector in `ker C`, while the ambient space is zero. Here `C2_T=ev_L : M_(2^6)->Q`, and `Q(L)=-720` proves rank one. This is a smaller known silent-band control; no exhaustive minimality claim over all possible cells/tests is made.

## 4. Redundancy and combined ranks

For the old all-matrix-coefficients test:

* A fixed left translate `h gamma(t)f` gives exactly the same condition, because `ell` ranges over the whole dual and `ell h` does too.
* Simultaneously transporting the representative and subgroup, `(f,gamma,z)` to `(hf,h gamma h^-1,hz)`, gives the same map up to invertible source/target identifications.
* A stabilizer change of basepoint is redundant since it fixes every `z in M_lambda`.
* Replacing `t` by `c t^m`, `c!=0`, multiplies all exponents and the permitted degree bound by `m`, and cannot change the kernel. More generally a surjective finite reparametrization of the projective parameter curve preserves pole orders after accounting for ramification and the pulled-back line bundle. An arbitrary local reparametrization alone does not replace the upper-degree check at infinity.

Conjugating only the subgroup while holding the old `f` fixed is a different question: the resulting family need not be polynomial. If it is polynomial, its independence must be checked on the same source. A coordinate-looking formula is not an independence proof.

Our `C2` is not any of the redundant changes, since it is nonzero on a vector in `ker C`. That is a direct common-source independence certificate.

For general cells, if columns of `N_C` are a basis of `ker C`, then

`rank [C;C2] = rank C + rank(C2 N_C)`.

One can instead certify a nonzero minor of the stacked matrix. Never add the individual ranks without checking the restriction to the first kernel. Modular minors of correctly defined rational/integral matrices certify characteristic-zero rank floors. Modular sampled zeros do not certify a rational identity or a rational kernel vector.

**Bounded diagnostic and failure criteria.** The executed test needs the formulas `pi,rho,H6`, the two fixed pencils, and the inherited `a=1` and arc-silence proof. It uses a `2 x 2` evaluation matrix, defining a `10 -> 1` map. At the skew pencil each alternating column has only `6! 2^6=46,080` assignments. The first evaluator aggregates by six two-element subsets of a four-element set, at most `6^6=46,656` keys; the actual nonzero aggregates had 1,140 entries. At the cycle pencil there are 2,880 assignments. No dense `16^24` tensor is created.

The initial search tried four fixed-seed pairs of slot partitions, including three zeros; all are retained in `skew_witness.json`. The two-pencil calculation took 0.25 seconds. An independent direct-epsilon evaluation, without signed aggregation, verified the same values in 1.625 seconds, using 213,696 compatible term pairs for the skew point and 2,784 for the cycle point. A separate direct permutation recursion verified `H6` against the producer's subset dynamic program. These are independent arithmetic paths within this investigation, not an external peer review.

Failure criteria were a zero minor, failure of full-H/type membership, nonzero old `C`, disagreement of the arithmetic paths, or exceeding the declared finite support/time cap. A zero minor would rule out only this pair and this witness. All mathematical criteria passed. See `sixrow_witness.json` and `verification.json`.

To find all nine missing directions by the same condition, supply a complete ten-vector full-H basis and an injective ten-point evaluation matrix; quotient by the single ambient column. The resulting map has rank nine exactly. Generic existence is proved above; that carrier/basis computation was not performed here.

## 5. One independent route to an explicit five-row equation

The construction is **certified interpolation of phi^***, carried out one highest-weight cell at a time. This is not a dimension-count argument in the semi-invariant ring.

There are 70 ordinary quartic coefficient variables `c_alpha` and 80 matrix-entry parameters `b_ij^(k)`. The 70 substitution polynomials are

`phi_alpha(B)=[x^alpha] det(sum_{k=1}^5 x_k B_k)`.

They have matrix-entry degree four. In a fixed cell, the exact linear map is

`T_lambda : A_{d,lambda} -> M_lambda`,

`h -> h(phi_alpha(B))`.

Its input degree is `d`, output degree `4d`, and variable-label weight is `lambda`. A nonzero kernel vector, written in an ambient highest-weight basis, is the desired explicit equation of type `S_lambda(C^5)` (and the corresponding five-row type in the sixteen-variable comparison). No factorization witnesses `M,N` are used.

**Closure-correct proof.** A certified `T_lambda(h)=0` is a polynomial identity in all 80 parameters. Hence `h` vanishes on every actual determinant representation. Its zero set is closed, so it vanishes on `D45=closure(im phi)`, including boundary quartics without finite matrix representatives. Conversely every equation of `D45` has this zero pullback. No closedness of an auxiliary projection is asserted or needed.

**The finite problem replacing a huge coefficient expansion.** Obtain a complete full-H carrier basis `q_1,...,q_s` using ordered epsilon contractions as in Section 3, now with Young-column heights `lambda'_j`, `d` four-slot row epsilons and `d` column epsilons, averaged with transpose. The tensor first fundamental theorem and the Young column construction give a spanning family; completeness is certified by reaching the known character dimension `s`.

Choose `s` integer tuples and form

`S=(q_i(B^(j)))_{j,i}` and `A=(h_i(phi(B^(j))))_{j,i}`.

Require `det S != 0`. A nonzero reduction modulo a suitable prime suffices to certify this rational nonzero. Then `T_lambda` has matrix `S^-1 A`, and

`ker T_lambda = ker A` **over Q**.

Proof: all substituted highest-weight polynomials belong to `M_lambda`, and evaluation is injective there. Therefore an exact rational relation among the evaluated columns is a relation of polynomials, not just an observation about a sample. Rationally reconstruct any modular candidate and check `A v=0` exactly. Merely observing `A v=0 mod p`, or testing extra random determinant points, is insufficient.

This addresses the missing certification step even when `a<s`: one need not have `rank A=min(a,s)`, and a rank-deficient `A` can genuinely certify equations once the separate carrier evaluation is injective. Constructing that injective carrier evaluation is the exact bottleneck. Replacing the carrier by a smaller unproved subspace invalidates the theorem.

**Five rows and padding.** Work only in partitions of `4d` with exactly five nonzero parts. Test an extracted equation on

`c_alpha(l C)=sum_{i:alpha_i>0} l_i C_(alpha-e_i)`.

The padding pullback has bidegree `(d,d)` in five linear coefficients and 35 cubic coefficients. By the accepted five-variable equality of the actual padding restriction closure with `R135`, a nonzero value on any `lC` is a legitimate padding separation certificate here. It is not an extrapolation to unrestricted cubic products in more variables. If a particular highest-weight equation is a separator only after a GL5 translate, search/evaluate its module translates or an appropriate transformed product point; one accidentally vanishing product point does not exclude separation.

For `a=1`, a nonzero determinant equation gives `m_det=0`; a padding nonzero gives `m_pad=1`, hence `D=1`. For `a>1`, an equation outside the padding ideal shows only that the two kernels have different positions. A positive gap additionally requires `rank(T_pad)>rank(T_det)` in that same full ambient multiplicity space, or a certified determinant upper bound below an actual padding rank floor. Padding-source dimensions cannot replace that lower rank evidence.

## 6. The minimal five-row pilot, and its stop

We chose the single cell

`d=6, lambda=(12,8,2,1,1), a=1, s=24`.

The dimensions `a,s` are inherited from the saved exact character table, not re-screened over degree six. This is a tractable test of the construction, not evidence that this cell should contain an equation. The accepted no-equation-through-degree-five result is why the pilot starts at six.

**Cheap falsification first.** Construct the unique ambient highest-weight polynomial `h`, verify its four raising residues over the integers, and evaluate it on one actual determinant. If nonzero, the entire cell is equation-free and the carrier construction stops. This check needs neither `s` nor `C` for its conclusion.

Measured source weight dimension: **1,121**. The four raising maps have target dimensions **927, 493, 556, 730**, with **3,954, 1,776, 1,121, 1,121** nonzeros, respectively. The reconstructed primitive integer polynomial has **230 terms**, maximum absolute coefficient **64**. Every raising residue is zero over `Z`; deliberately corrupting one coefficient gives a nonzero residue.

At the saved integer determinant pencil, its exact value is

`h(det(sum x_k B_k)) = -222,071,593,284,381,720 != 0`.

A separate verifier reads the stored 230 terms, recomputes raising derivatives directly as coefficient-polynomial dictionaries, and independently expands the determinant pencil. It reproduces the zero raising residues and the displayed nonzero without importing the constructor; see `verify_five_row.py` and `five_row_verification.json`.

Therefore `m_det=1=a` and `I(D45)_{6,(12,8,2,1,1)}=0`. The expensive stage was stopped. The JSON certificate stores the actual 230-term polynomial and all 80 matrix entries, not only its seed. The run used the historical highest-weight constructor read-only, with its SHA-256 pinned; membership was checked by exact raising operators after reconstruction. It ran under a 60-second/512-MiB Job Object cap: 4.80 seconds wrapper wall time, 28,733,440 bytes peak commitment, 39,772,160 bytes peak working set.

**Price had the cheap test survived.** The exact carrier-evaluation problem would have been `24 x 24`, with a `24 x 1` substituted ambient column; 576 retained carrier values and 24 ambient evaluations. Column heights are `(5,3,2,2,2,2,2,2,1,1,1,1)`. At one tuple the distinct alternating-column data have only

`binom(16,5)+binom(16,3)+binom(16,2)+16 = 5,064`

independent minor entries (40,512 bytes as 64-bit residues). The uncompressed distinct column tensors contain 1,052,944 entries, about 8.04 MiB. Repeated heights reuse the same data. This prices stored input tensors, not contraction intermediates: each contraction path must be priced separately before execution. A complete basis may need more candidates than 24.

A bounded continuation would permit at most 96 proposed carrier columns at 24 points (2,304 contractions), rejecting paths with more than `2^24` intermediate scalar entries or `5*10^7` multiply-adds, with an aggregate `10^9`-operation ceiling and a 60-second/512-MiB wall/memory cap. Failure to obtain rank 24 within those caps means **carrier not certified**, not a geometric negative. These are explicit stop limits, not a promise that the full calculation fits them. This stage was not launched after the exact nonzero.

The cheap negative rules out **only this degree-six representation cell**. It does not rule out the interpolation construction, other five-row cells, degree-six equations elsewhere, or the accepted noncontainment `R135 not subset D45`.

## 7. Evidence, extrapolation, and the unproved claim

The new six-row mechanism is proved and numerically instantiated: `C2(Q^2)!=0` with `C(Q^2)=0`. It distinguishes regular coefficient functions from extra orbit functions. The two pencil points are sufficient for this claim; no normalization model or boundary chart is assumed.

For five rows, the same finite-descent theorem applies, and certified carrier interpolation would compute the true determinant kernel. That is a valid mechanism, not evidence of a small equation. In every already-certified cell with `ker C=E_lambda`, any globally necessary `C2` must vanish on `ker C`; it cannot add constraints there. The absence of the six-row silence band at five rows supplies no contrary evidence. Our single five-row pilot is an additional negative of explicitly limited scope.

**The strongest desired claim not proved:** a named computationally manageable five-row cell has a nonzero determinant pullback kernel containing a polynomial nonzero on `R135`. We have neither such a kernel vector nor a positive multiplicity gap, and no proof that an analogous two-point test is independent of `C` in any five-row cell. The six-row success does not predict a degree, a partition, or `D>0` for five rows.

**Files and source trail.** Fresh formulas and exact data: `skew_witness.py/json`, `sixrow_witness.py/json`, `verify_witness.py`, `verification.json`, `five_row_pilot.py/json`, and `results/logs/five_row_pilot_resources.json`, all alongside this report. `MANIFEST.json` binds these files and the consulted mathematical inputs. No historical result is presented as a fresh replay.

Local mathematical inputs: B15-02 `docs/b17_02_report.md` and `docs/b18_02_report.md` for the arc and row carrier; B15-01 `docs/b19_01_report.md` and its review for the diagnostic dimensions; B15-10 `docs/b15_10_proved.md` for the integral H6 convention; B15-02 `docs/b19_02_report.md` and its review for the latest degree-five status; the saved `Batch17_Planning/symmetry_dream/astra/toy_character_screen_d5_d6.json` for the one pilot's inherited dimensions; B15-06 `analysis/b18_06_sweep.py` for the highest-weight constructor.

Primary background checked online: Kumar, [Geometry of orbits of permanents and determinants](https://arxiv.org/abs/1007.1695), for nonnormality of determinant orbit closures; Huettenhain--Lairez, [The boundary of the orbit of the 3 by 3 determinant polynomial](https://arxiv.org/abs/1512.02437), for the scope of the cubic boundary precursor. The new descent proof and arithmetic above do not depend on a boundary classification. The five-variable degree-five premise is adopted from the latest local review; no claim that the online abstracts independently certify that calculation is made.
