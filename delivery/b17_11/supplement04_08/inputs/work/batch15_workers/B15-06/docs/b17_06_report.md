# B17-06: cancellation-controlled permanent coefficients

13 September 2026, America/New_York. **COMPLETE as a bounded theory and control contribution.**
No positive multiplicity gap or new candidate cell is claimed. Author: gpt-6-astra,
xhigh. No agents, tasks, worktrees, commits, publication, trust changes, or heavy
lease were used.

The result is a sufficient independence criterion on a family retaining all nine
permanent entries. Its coefficient support has exactly

\[
 K_d=\binom{d+5}{5}-\binom{d+2}{5}
     =\frac{d^4+6d^3+15d^2+18d+8}{8}                         \tag{1}
\]

possible slots (the second binomial is zero for d<3). An explicit normal form
combines every collision with its actual sign. Four entry parameters suffice;
one arc invertible at its base point preserves all the resulting independence.
These are capacities of the specified family, not actual padding multiplicities.

The first fresh check is the known degree-five cell `(d,lambda)=(5,(16,4))`.
Two explicit highest-weight polynomials give a minor **-184926** on a full-entry
unit arc. A second, encoded arc gives **32286015**. This control has
`a=m_det=m_pad=2`; it is not a separation probe. An adversarial control proves
that a natural older base has rank only one on its entire entry-scaling family,
despite the global rank two.

## 1. Scope, normalization, and evidence

Work over Q for certificates and extend to C for representation theory. Set
`V=C^16`, `W=Sym^4(V*)`, `A_d=C[W]_d=Sym^d(Sym^4 V)`, with
`(g.f)(x)=f(g^-1 x)`. The coefficient of a monomial is its ordinary coefficient,
without divided-power or binomial rescaling. Coefficient rows in an arc are
Hasse coefficients `[u^k]`, not ordinary derivatives. All functions used for a
multiplicity floor must be polynomial highest-weight vectors of the **same**
`S_lambda V` type in the **same finite degree d**.

For `X_f=closure(GL16.f)`, write `m_f` for the coordinate multiplicity in that
cell, `a` for the ambient multiplicity, and `i_f=a-m_f`. Thus

\[
 D=m_{pad}-m_{det}=i_{det}-i_{pad}.
\]

A reviewed global upper `m_det<=B` and an actual padding minor of rank `r>B`
are sufficient. A padding-source ceiling `m_pad<=U` supplies only a necessary
headroom gate `B<U`. Coordinate functions on the closure are restrictions of
ambient polynomials; orbit invariant dimensions are upper bounds and do not
settle boundary extension. See [BLMW, §§4.1 and 5.2, Proposition 5.2.1](https://arxiv.org/pdf/0907.2850v2).
The padding source/normalization distinction is also explicit in
[Kadish–Landsberg, Theorem 1.7 and Proposition 1.8](https://arxiv.org/pdf/1204.4693).

The required board, screen report, common context, stocktake, and `Batch16/INTAKE.json`
were read. The current board/screen supersede the planning report's obsolete
description of six nearby cells as uncomputed: **all six are now excluded**.
The degree-seven short-body symmetry screen has no survivor; this does not
exclude boundary losses or every degree-seven cell.

Provenance followed `Batch16/INTAKE.json`, entry 10, to the original
`B15-10/docs/b16_10_proof.md`, its original coefficient certificate and accepted
delivery manifest, then to the original Hessian11_1631 report/review named in
its input manifest. The bounded check verifies that the original arc proof and
certificate match the Batch16 review copies and the accepted package hashes.
It also verifies the original Hessian report/review hashes against B16-10's
recorded inputs. **No historical Hessian computation was rerun.** The inherited
arc floors 1/2/2/3 and the stronger old padding floor 243 are not fresh results
here. They are unnecessary to the new theorem or degree-five proof.

Nineteen exact-byte input snapshots and hashes, including the inspected wrapper,
are in [INPUTS.json](../delivery/b17_06/INPUTS.json). The interpreter is separately
hash-pinned. [MANIFEST.json](../delivery/b17_06/MANIFEST.json) binds outputs,
resources, source provenance, and access limitations. No common Git base or
new Git commit is asserted.

## 2. First control: a known multiplicity-two cell with every entry retained

For the binary restriction of a quartic write

\[
 f(t,x)=ct^4+a_1t^3x+a_2t^2x^2+a_3tx^3+a_4x^4,
\quad h=8ca_2-3a_1^2,\quad I=a_2^2-3a_1a_3+12ca_4.
\]

Take `F1=c^3 I` and `F2=c h^2`. In the ordinary coefficient convention the
simple raising derivation is `E(c)=0`, `E(a_i)=(5-i)a_(i-1)`. Directly
`E(h)=E(I)=0`. Both F's have coefficient degree five and weight `(16,4)`.
The other simple raising operators of GL16 kill these functions: they depend
only on coefficients supported on the first two coordinates. This gives
ambient GL16 highest-weight vectors, not just functions on a binary space.

The multiplicity of `(16,4)` is two. Indeed the binary weight spaces of tails
four and three in `Sym^5(Sym^4 C^2)` have dimensions five and three: they count
partitions of four and three into at most five parts of size at most four.
The GL2 highest-weight multiplicity is their difference, two. The identical
coefficient monomials and raising equations give the same highest-weight
space in GL16. Every binary quartic splits over C into four linear factors
and hence is a specialization of det4. Consequently these two binary
highest-weight functions have independent restrictions to the determinant
closure. The actual padding minor below supplies the matching padding floor.
Thus `a=m_det=m_pad=2`, consistently with the prior planning control.

Order source coordinates as
`(z,X11,X12,X13,X21,X22,X23,X31,X32,X33)` and target coordinates as
`(t,x1,...,x9)`. Put

```
a = (1,1,0,0,0,1,0,0,0,1)
b = (2,1,2,1,3,1,2,2,1,5)
L0 = [a,b,e2,e3,...,e9]       # zero-based source indices
```

The first two rows/columns give `[[1,2],[1,1]]`; the remaining columns give
an identity block, so `det L0=-1`. Every one of the nine entry forms and z is
nonzero, and all ten are linearly independent. Extend with an identity on six
unused coordinates to get a GL16 matrix. Scale the **whole X12 form** by
`s=1+u`. Then `det L(u)=-(1+u)`, a unit in Q[[u]]. Every specialization except
`u=-1` is invertible. No entry is identically zero.

On the binary line `x1=1`, the source substitution is

\[
 z=t+2,\qquad
 X=\begin{pmatrix}t+1&2s&1\\3&t+1&2\\2&1&t+5\end{pmatrix}.
\]

This line computes ordinary binary coefficients of the full quartic; the
full substitution L(u) above is what establishes genuine padding membership.
Expansion of all six permanent terms gives

\[
 \operatorname{per}X=t^3+7t^2+(15+6s)t+(12+38s),
\]

so `(c,a1,a2,a3,a4)=(1,9,29+6s,42+50s,24+76s)`. Hence

\[
 F_1=-59-18u+36u^2,\qquad
 F_2=1369+3552u+2304u^2,
\]

and the coefficient minor with rows `[u^0],[u^1]` is

\[
 \det\begin{pmatrix}-59&1369\\-18&3552\end{pmatrix}=-184926\ne0. \tag{2}
\]

These are the first mathematical checks in the one fresh computation, before
the normal-form tests. They prove a genuine rank-two control using all nine
permanent entries. Binary splitting above is used only to identify the known
determinant control; a zero-entry padding family is never used for the minor.

## 3. The exact cancellation criterion

Fix ten independent rational linear forms `b,L11,...,L33` on V. Write

\[
 q_\sigma=b\prod_{i=1}^3L_{i,\sigma(i)},\qquad
 p_s=b\operatorname{per}(s_{ij}L_{ij})
     =\sum_{\sigma\in S_3}s^{P_\sigma}q_\sigma,               \tag{3}
\]

where `P_sigma` is the permutation matrix. For all nine nonzero scalars
`s_ij`, the ten forms in (3) remain independent. Therefore p_s is an actual
GL16 transform of **independent z*per3**, and the polynomial parameter family
also lands in its closure at exceptional parameter values. It is not per4,
nor padding of a generic cubic in ten variables.

For any supplied polynomial `F_j in A_d` define the homogeneous polynomial

\[
 H_j(y)=F_j\left(\sum_{\sigma\in S_3}y_\sigma q_\sigma\right)
       =\sum_{|\alpha|=d} h_{j,\alpha}y^\alpha.              \tag{4}
\]

The `h_(j,alpha)` are the **actual** coefficients after all source/tableau
signs and repeated terms are combined. Formula (4) uses six fixed quartics;
its independent y's are an auxiliary coefficient calculation, not permission
to treat every such quartic combination as padding.

Let `E={123,231,312}` and `O={132,213,321}`. In the six-variable ring set

\[
 R=\prod_{\sigma\in E}y_\sigma-\prod_{\sigma\in O}y_\sigma,
 \qquad v_\sigma=\begin{cases}1&\sigma\in E,\\-1&\sigma\in O.\end{cases}
\]

For an exponent alpha define

\[
 k(\alpha)=\min_{\sigma\in E}\alpha_\sigma,\qquad
 N(\alpha)=\alpha-k(\alpha)v.                              \tag{5}
\]

Thus N has nonnegative coordinates, the same total degree, and at least one
zero even coordinate. Replace every `y^alpha` by `y^N(alpha)` and add its signed
coefficient. Denote the resulting normal form by `NF(H_j)`.

**Theorem 1 (sufficient independence, with complete collision control).**
The kernel of `y_sigma -> s^P_sigma` is the principal ideal `(R)`. For each
canonical exponent beta, the normal-form coefficient is exactly

\[
 C_{\beta j}=\sum_{k=0}^{\min_{\sigma\in O}\beta_\sigma}
                       h_{j,\beta+kv}.                   \tag{6}
\]

The matrix C has precisely the restriction rank of the F_j on the fixed
family (3). In particular, if the F_j are highest-weight polynomials of the
same finite `(d,lambda)` and C has an r-by-r nonzero minor, then
`m_pad(lambda,d)>=r`. Pairwise distinct nonzero leading monomials of the
normal forms, in any fixed monomial order, are a sufficient triangular
certificate. A signed sum in (6), not the existence of a single contribution,
is what must be nonzero.

**Proof.** Write `M alpha=sum_sigma alpha_sigma P_sigma`. Every entry (i,j)
belongs to exactly one even and one odd permutation. Each even/odd pair
shares exactly one entry. Thus if `M z=0`, all nine equations are
`z_even+z_odd=0`: every even coordinate equals one scalar a and every odd
coordinate equals -a. Over the integers, `ker M=Z v`.

Consequently `M alpha=M gamma` exactly when alpha and gamma differ by an
integer multiple of v. Subtracting the minimum even coordinate as in (5)
gives their unique common canonical representative. The entire nonnegative
fiber through beta is `beta+kv`, with the bounds in (6). This proves the
coefficient formula and its cancellation completeness. Reduction (5) is also
division by the monic binomial R with its even product as leading term; for
example lex order with y123 first gives that leading term. Distinct canonical
monomials have distinct images, so their images are independent monomials in
s. Every polynomial reduces to zero precisely when its image is zero. The
kernel is therefore `(R)`.

If a linear combination of F_j vanishes on X_pad, it vanishes on every p_s
for nonzero s. Its pullback polynomial is zero on a dense torus and hence
identically zero. Its coefficient vector lies in the kernel of C. A nonzero
r-minor rules out a dependence among those r restrictions. In characteristic
zero, the highest-weight space of type lambda in the coordinate ring has
dimension m_pad, giving the stated lower bound. Finally distinct leading
monomials imply independence by inspecting the largest leading monomial in
any proposed nontrivial linear combination. This is a triangular minor after
ordering. QED.

The principal Birkhoff-binomial fact itself is established literature, not a
novelty claim: see [Ohsugi–Hibi, *Toric rings and ideals of nested configurations*,
Example 3.1](https://arxiv.org/abs/0907.3253), also available as
[author-uploaded primary text](https://www.researchgate.net/publication/45862999_Toric_rings_and_ideals_of_nested_configurations).
Our elementary proof above fixes the signs and conventions needed here.
The application to actual padding coefficients and the following arc/cost
formulas are deductions supplied in this contribution.

**Adversarial cancellation check.** In degree three the two monomials in R
each have a contribution and both map to `prod_(i,j) s_ij`. They cancel
exactly. Replacing their difference by a sum gives coefficient two, not zero.
This invalidates a certificate that records unsigned matching existence.
The executable checks both cases, independently using nine-entry exponents
and normal-form reduction.

## 4. Four entry parameters and an invertible arc without coefficient loss

All monomials `s^T` in a degree-d pullback have nonnegative integer 3-by-3
exponent matrices T with every row sum and column sum d. The four entries
`(T22,T23,T32,T33)` determine the rest:

```
T21 = d-T22-T23       T31 = d-T32-T33
T12 = d-T22-T32       T13 = d-T23-T33
T11 = T22+T23+T32+T33-d.
```

Therefore setting the five scalars in the first row or first column of s to
**one** leaves distinct exponent monomials distinct in degree d. It loses no
restriction rank within that degree. This fixes entry **scalars**, not
permanent entries to zero. All nine forms remain present.

For `d>=1`, let `b_d=d+1` (this integer is distinct from the linear form b)
and set

\[
 s_{22}=(1+u),\quad s_{23}=(1+u)^{b_d},\quad
 s_{32}=(1+u)^{b_d^2},\quad s_{33}=(1+u)^{b_d^3},             \tag{7}
\]

with the other five scalars equal to one. The exponent map is

\[
 e(T)=T_{22}+b_d T_{23}+b_d^2T_{32}+b_d^3T_{33}.             \tag{8}
\]

Every digit lies between zero and d, so (8) is injective. Thus the arc
pullback is `sum_T C_(T,j) (1+u)^e(T)`, and the polynomials `(1+u)^e(T)` are
linearly independent for distinct e(T). This preserves the entire rank of
the nine-parameter family in the fixed degree d.

The underlying 16-by-16 substitution determinant is

\[
 \det G(u)=\det G_0(1+u)^{1+b_d+b_d^2+b_d^3}.
\]

It is a unit at u=0. Equivalently (7) is a family of invertible substitutions
over `v=1+u in G_m`. It is **not** claimed invertible at the exceptional
affine value u=-1. That point is not used for a certificate. The arc is full
support throughout its formal neighborhood of zero.

**Theorem 2 (finite jet suffices).** If K distinct entry-exponent monomials
occur in the union of supports of the chosen restrictions, the Hasse rows
`[u^0],...,[u^(K-1)]` of (7) have the same column rank as C. In particular
K<=K_d suffices. Selected r rows proving a nonzero r-minor are enough; it is
not necessary to construct all K rows.

**Proof.** With distinct exponents `e1<...<eK`, the change of coefficient
functionals is the square matrix `J_(k,l)=binom(e_l,k)`, `0<=k<K`. Since the
polynomial `binom(z,k)` has leading coefficient `1/k!`,

\[
 \det J=\frac{\prod_{i<j}(e_j-e_i)}{\prod_{k=0}^{K-1}k!}\ne0. \tag{9}
\]

Multiplying C by this invertible matrix preserves rank. This is exact over
Q; a modular implementation must avoid bad primes and clear denominators
before interpreting a nonzero minor in characteristic zero. QED.

The degree of the arc polynomials is bounded by

\[
 \max e(T)\le d\bigl(1+(d+1)^3\bigr).                     \tag{10}
\]

Indeed each perfect matching contributes one of
`1+b_d^3, b_d+b_d^2, b_d^3, b_d, b_d^2, 1`; the largest is `1+b_d^3`.
No expansion to every univariate coefficient through (10) is required.
Sparse exponents followed by (9) are usually much cheaper. None of this
promises that the **first r** rows work for arbitrary r functions.

For the degree-five control, weights are `(1,6,36,216)`. Only twelve exponent
slots occur, with maximum 1085. Rows zero and one are already

\[
 \begin{pmatrix}-59&1369\\-67494&1018869\end{pmatrix},
 \qquad\det=32286015.                                    \tag{11}
\]

The receipt retains all twelve support exponents and Hasse rows. A separate
4-by-4 binomial determinant control gives `57153083855`, agreeing with (9).
These are tests of the general proofs, not numerical substitutes for them.

## 5. Support cost, and what the bound does not pay for

There are `binom(d+5,5)` degree-d monomials in the six y variables. Noncanonical
ones are exactly those divisible by the product of the three even variables;
there are `binom(d+2,5)` of them. This proves (1), including its polynomial
form, in every degree. Equivalently the Hilbert series is
`(1-t^3)/(1-t)^6`. Each canonical slot represents a distinct actual entry
monomial. Its signed fiber (6) has at most `floor(d/3)+1` summands.

| Degree | Six-variable slots before merging | Exact slots after merging |
|---:|---:|---:|
| 0 | 1 | 1 |
| 1 | 6 | 6 |
| 2 | 21 | 21 |
| 3 | 56 | 55 |
| 4 | 126 | 120 |
| 5 | 252 | 231 |

The one control checks all 462 raw monomials across these degrees: exponent
fibers, normal forms, four-parameter injectivity, and integer arc encoding
all agree. No higher-degree enumeration was performed.

For r supplied polynomials the coefficient table requires at most `r K_d`
scalar slots. This is a storage/support bound for one fixed base family,
not a computation lease or a guarantee of r independent columns. If the
F_j are supplied as homogeneous division-free circuits, substitute each
quartic coefficient by its six-term linear form from (4), and perform circuit
operations modulo R. An intermediate homogeneous degree e has at most K_e
slots. A naive product of degrees e and f takes at most `K_e K_f` scalar
pair accumulations plus constant-size exponent normalization. A raw degree-d
expansion followed by reduction instead processes at most `binom(d+5,5)`
terms per polynomial. Source cancellation must be included in either method.

These counts do **not** cover constructing highest-weight source circuits,
their coefficient bit lengths, preparing all needed coefficients of the
q_sigma, or selecting a good base G0. For a q_sigma the immediate product
expansion cost is at most `support(b) prod_i support(L_i,sigma(i))` ordered
terms; this should be priced for the actual forms. Computing even one desired
coefficient of a large circuit may be expensive. There is no generic claim
that the fibers in (6) can be extracted cheaply.

If the sparse exponent table has K columns and one wants all K Hasse rows,
the binomial transform alone has K^2 entries. Its integers can be large.
Use direct normal-form leading monomials/minors when available; price the
actual needed rows and bit lengths before allocating an arc expansion.
The `O(d^4)` support identity is not a complexity lower bound, a fast
algorithm for arbitrary highest-weight sources, or improved determinant-size
growth. In particular it does not improve the LMR benchmark.

## 6. A proved failure mode: the old base torus misses a real direction

Replace the last entry 5 of the control vector b by 4. This is precisely the
base matrix of the accepted B16-10 arc (the old arc varied a different
matrix coefficient). Its determinant remains -1 and all ten forms remain
independent. Scale all nine permanent entries by arbitrary scalars s.

In its binary restriction only the diagonal matching has t-degree three,
and the diagonal factors are `(t+1),(t+1),(t+4)`. If
`c=s11*s22*s33`, the quartic has `a1=8c` and has the fixed root -2 from
z=t+2. On c!=0, normalize by c and depress by `t -> t-2`. The depressed
constant term s4 is zero. For a depressed normalized quartic,

\[
 h=8c^2s_2,\qquad I=c^2(s_2^2+12s_4).
\]

Therefore **F2=64 F1 on this entire nine-parameter torus**. Polynomiality and
density extend the identity over its parameter closure. At the identity
scales, F1=49, so the restriction rank there is exactly one. The new base
with final entry 5 has the nonzero minor (2), so this relation is not a
global equation on X_pad. The executable separately verifies the old
normal-form identity and its failure at the new base.

This proves a specific limitation of the proposed method: a deficient
normal-form matrix certifies only a deficient chosen family. It is not a
padding multiplicity upper bound. Trying another base is a new, separately
priced test; ranks from several bases cannot simply be added. A single
combined matrix on the same source columns is needed.

The inherited sparse-probe lemma remains a stricter rejection rule: setting
one permanent entry **identically** to zero makes the padded family a det4
specialization (after moving the zero to (3,3), negate entries (1,1),(2,2)).
No union of such families can beat a valid global determinant upper. Our
families retain every entry; that necessary condition alone does not ensure
independence or separation.

## 7. Fresh/inherited status, resources, and the next sufficient test

Fresh deductions: the coefficient application with complete fiber sums,
the exact support cost, four-parameter reduction, injective unit-arc encoding,
finite Hasse-jet bound, explicit degree-five highest-weight control, and the
old-base rank-one identity. The Birkhoff relation is a cited standard fact,
also reproved here. The contribution has not yet received an independent
Batch17 mathematical review; same-author checks do not replace that review.

Fresh computation: exactly one standard-library process using the existing
`.venv/python.exe -B` and inspected, unchanged `analysis/b15_bound.py`.
Preflight: [PREFLIGHT.json](../results/b17_06/PREFLIGHT.json).
Executable: [b17_06_verify.py](../analysis/b17_06_verify.py).
Exact receipt: [control_01.json](../results/b17_06/control_01.json).
Resources: [wrapper receipt](../results/logs/b17_06_control_01_resources.json).

| Measure | Result |
|---|---:|
| Wrapper wall time | 0.0740545 seconds |
| Peak Job Object committed bytes | 13,541,376 |
| Peak working-set bytes | 21,078,016 |
| Process / configured BLAS threads | 1 / 1 |
| Wall / aggregate Job Object caps | 60 seconds / 512 MiB |
| Exit code | 0 |
| Polynomial products / term pairs | 42 / 186 |
| Largest stored polynomial support | 12 |

The wrapper's legacy B15 session label does not change the B17 ownership of
this receipt. Its timer thread only enforces the deadline. No subprocess,
background computation, or second research run occurred. The logged
13-bit maximum is for sparse source-polynomial coefficients only; the Hasse
rows contain larger integers. No cap was hit. A cap hit would be uncomputed.
After the user's capacity-resume message, the saved report, executable hash,
and successful receipt were inspected. Finalization used those completed
results; no calculation was repeated and no scope or lease was expanded.

Inherited, not rerun: Batch16 counts, complete ideal dimensions, padding
ceilings/floors, original Hessian source membership, and historical arc
arithmetic. Their status does not imply a new positive cell. The fresh
degree-five argument establishes its own highest-weight membership and
ambient count without importing those computations.

**One next sufficient test, addressed to the integrator.** Supply and review
one new finite `(d,lambda)` with a globally valid `m_det<=B`, correct
nine-variable-core padding ceiling `U>B`, and exactly `r=B+1` explicit
polynomial highest-weight source circuits. If a beyond-occurrence claim is
intended, also supply actual determinant occurrence, not merely `B>=1`.
For one specified invertible base G0, price its q_sigma input coefficients,
the circuit operations modulo R, coefficient bit lengths, and one proposed
r-by-r minor. Review this report's lemma first, then test that single minor
or a triangular normal-form certificate. A nonzero minor proves
`D>=r-B>0`. A zero minor is only a failed test. A proven full rank at most B
for that family still does not exclude the cell globally.

No reviewed `B<U` cell or such sources were supplied here, and no large
candidate matrix was built. **No larger lease is requested for this completed
contribution.** If the integrator supplies that input and its priced test
exceeds the small-run cap, the report requests explicit integrator resource
review before any execution; slot 06 must not self-issue a lease. No idle
dependency polling or indefinite search remains active.

## 8. Reproduction and access record

The single executed command was:

```powershell
& .venv/python.exe -B analysis/b15_bound.py --slot 06 --name b17_06_control_01 --seconds 60 --memory-mb 512 analysis/b17_06_verify.py --output results/b17_06/control_01.json
```

For a separately authorized receiver, use a fresh `b17_06` log and output
name; the program refuses to overwrite its receipt and imports no original
worker arithmetic. All mathematical input snapshots are local to this
delivery. The original wrapper and existing Windows Python environment are
needed for the stated resource enforcement. The script was not changed
after the successful run.

Routine read access found no applicable AGENTS.md in the checked worktree
ancestors or authorized output directories. The initial conventional
`.venv/Scripts/python.exe` lookup was absent; the existing `.venv/python.exe`
was used. Read-only Git status warned that the global ignore file was
inaccessible; no trust or permission setting was changed. No requested
research action was rejected by automatic approval review.

Two literature fetch limitations are retained in the manifest: the Kyoto
Haase–Paffenholz PDF URL was refused by the web tool as unsafe/non-retryable,
and the arXiv Ohsugi–Hibi PDF returned a cache miss. Neither was retried or
bypassed. The latter paper's author-uploaded primary text, Example 3.1, was
available in the independent literature search. The theorem above has a
self-contained proof, so neither failed fetch is a mathematical dependency.
