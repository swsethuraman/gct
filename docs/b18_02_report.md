# B18-02: the symmetry carrier for one justified cell

Batch 18, slot 02. 15 September 2026. Worktree `work/batch15_workers/B15-02`,
written in place. Status line is at the end of the report (section 9).

**Starting state (read-only, recorded before any write):**

    git rev-parse HEAD          6f85b37b1ba607f170170da5ef6854222d55120a
    git rev-parse HEAD^{tree}   b1531cf709f85b6a70966c8dd1318d24c82778d9

## 0. Plain-terms summary

The B17-02 arc `gamma(t)f = Q0 + t Q1 + t^2 Q2` gives a necessary condition for a
copy of `S_lambda(W*)` in the orbit coordinate ring to extend to the closure: the
corresponding full-stabilizer invariant `z` in `S_lambda W` must have no
`gamma`-weight outside `[0, 2d]`. The number `b = rank C` of independent
violations lowers the global determinant bound to `B = min(a, s - b)`. Nobody has
yet built the object `C` acts on: an exact basis of `M_lambda = (S_lambda W)^H`
for the **full** stabilizer `H` (transposition included), in coordinates where the
`gamma`-weight can be read off. That is this slot's job.

What this report delivers:

1. **A concrete, provably correct model of `M_lambda`** as a space of polynomial
   functions on `m`-tuples of `4x4` matrices (`m = length(lambda)`), with the
   transposition imposed as an explicit symmetrisation, and the dimension `s`
   pinned to the symmetric rectangular Kronecker coefficient. No `16^(4d)` tensor is
   ever formed. (Sections 2-3.)
2. **A weight lemma** that collapses the forbidden projection: on every
   `H`-invariant, the `gamma`-weight of an adapted-coordinate monomial equals
   `2d - (number of skew factors v)`. So weights lie in `[-d, 2d]`, the upper
   forbidden range `k > 2d` is empty, and `C` is exactly the projection onto
   **skew-degree `>= 2d + 1`**. (Section 4.)
3. **A priced procedure** for certifying a basis of `M_lambda` and a rank floor
   `b` for `C` by exact modular evaluation, without expanding any polynomial,
   together with the reason explicit conversion into adapted coordinates is a
   cost barrier in every cell of interest. (Section 5.)
4. **One small control** (degree `d = 2`, all partitions of 8 with at most five
   rows), run under the standard 60 s / 512 MiB wrapper, that checks the
   construction end to end against the character formula for `s` and against the
   weight lemma. It is a **method validation, not a gap candidate**: every
   five-row cell at `d = 2` has `a = 0`. (Section 6.)

What this report does not deliver: a candidate cell (slot 06 had not reported when
this was written), any positive `b` in a cell with `a > 0`, any `B < U`, any
padding rank, any gap.

## 1. Conventions, fixed before the construction

**ADOPTED** from the preamble and from supplement02 (which wins over the B17-02
report wherever they differ; no disagreement affecting this slot was found, but the
supplement's statements were used as the reference throughout):

- `W` is the sixteen-dimensional space of linear forms; `V = Sym^4 W` holds the
  forms; `G = GL(W)`; `f = det4` in adapted coordinates; `X = closure(G.f)`.
- Coordinate modules of the coordinate ring are labelled `S_lambda(W*)`,
  `lambda` a partition of `4d` with at most sixteen rows, `d` the coefficient
  degree. In the preamble's notation `W = V_ref*`; the coordinate labels agree.
- The multiplicity source is `M_lambda = (S_lambda W)^H` with `H = Stab_G(f)` the
  **full** stabilizer: `x -> A x B` with `det A det B = 1`, extended by the
  transposition `x -> x^T`. `s = dim M_lambda`.
- Coefficients of forms are **ordinary** monomial coefficients (no factorials,
  no divided powers). Nothing in this report uses the raising-operator normalisation
  on coefficients; the only raising operators used act on the row model of
  section 2 and are stated there.
- Adapted coordinates on `W` (sixteen linear forms), from supplement02's audit:

      [[a,  r1,        r2,        r3      ],
       [c1, s11,       s12 - v3,  s13 + v2],
       [c2, s12 + v3,  s22,       s23 - v1],
       [c3, s13 - v2,  s23 + v1,  s33     ]]

  i.e. `a = x11`, `r_k = x_{1,k+1}`, `c_k = x_{k+1,1}`, `S = sym part`,
  `A(v) = skew part` of the lower-right `3x3` block `E`. This is an invertible
  change of all sixteen coordinates (determinant `-8`).
- `gamma(t)` scales `a, r` by `t^-1`, fixes `v`, scales `c, S` by `t`.
  Weight spaces have dimensions 4, 3, 9. `gamma(t) f = Q0 + t Q1 + t^2 Q2`
  (**ADOPTED**, accepted in supplement02).
- `gamma`-weights are taken in the **source** `S_lambda W`: the exponent of `t`
  in `ell(gamma(t) z)`. Supplement02's warning is respected: the pullback action on
  raw coordinate functions has the opposite sign and is not used anywhere here.
- Forbidden weights: `k < 0` or `k > 2d` (inclusive interval `[0, 2d]` allowed).
- `s` is the **symmetric** rectangular Kronecker coefficient
  `sk(lambda, (d^4), (d^4))`, i.e. the multiplicity of the Specht module `S^lambda`
  in `Sym^2(S^{(d^4)})`. The ordinary rectangular Kronecker coefficient
  `g(lambda, (d^4), (d^4))` counts only connected-stabilizer invariants and is
  written `g`, never `s`, below.
- Two integer quantities appearing later: `N = 4d` (tensor length), and for a
  partition `lambda` its conjugate `lambda'`, so `lambda'_j` is the height of
  column `j`.

Everything in sections 2-4 is proved in this report from these conventions plus
standard representation theory; the two literature inputs are Schur-Weyl duality
and the first fundamental theorem for `SL`, both stated where used.

## 2. The carrier: `M_lambda` as polynomials on `m`-tuples of `4x4` matrices

**PROVED (this section).** Let `m = length(lambda)` and let `Y = (Y_1, ..., Y_m)`
be an `m`-tuple of `4x4` matrices, `Y_i` holding the sixteen coordinates of a
linear functional `y_i` on `W` in the standard entry basis, `(Y_i)_{pq} = y_i(x_pq)`.
Write `C[Y]` for the polynomial ring in these `16m` variables. For `i < j` define
the raising operator

    E_ij = sum_{p,q} (Y_i)_{pq} d/d(Y_j)_{pq},

i.e. polarisation "replace one factor from `Y_j` by `Y_i`". Define

    HW_lambda = { P in C[Y] : P has degree lambda_i in Y_i for each i,
                              and E_ij P = 0 for all i < j }.

`GL(W)` acts on `C[Y]` through its action on each functional `y_i`, and this
commutes with every `E_ij`. The group `H` acts on `Y_i` by `Y_i -> A Y_i B`
(`det A det B = 1`) and `Y_i -> Y_i^T` (the action of the stabilizer on
functionals; the invariant subspace is the same whether one uses `g` or `g^-1`).

**Theorem 2.1 (row model).** `HW_lambda` is isomorphic to `S_lambda W` as a
`GL(W)`-module, and therefore

    M_lambda = (S_lambda W)^H  ~=  HW_lambda^H
             = { P in HW_lambda : P(A Y B) = P(Y) whenever det A det B = 1,
                                  P(Y^T) = P(Y) }.

*Proof.* Cauchy: `C[Y] = Sym(W (x) (C^m)*) = (+)_nu  S_nu W (x) S_nu((C^m)*)`
over partitions `nu` with at most `m` rows. The operators `E_ij` are the
`gl_m` raising operators of the second factor and commute with `GL(W)`. In the
factor `S_nu((C^m)*)` the vectors of multidegree `lambda` killed by all `E_ij`
(`i<j`) form the highest-weight line if `nu = lambda` and are zero otherwise
(multidegree is the `gl_m` weight; a weight vector killed by all raising operators
is a highest-weight vector, and the highest weight of this polynomial module is
`nu`). Hence `HW_lambda = S_lambda W (x) (line)`. The `H`-invariants of the two
sides correspond because `H` acts only through `GL(W)`. The description of the
`H`-action is the restriction of the `GL(W)`-action to the stabilizer of the
adapted `f`; by supplement02 that stabilizer is `{x -> A x B, det A det B = 1}`
together with the transposition, and every element `(A,B)` with `det A det B = 1`
is a scalar times an element of `SL_4 x SL_4`, the scalar acting on
`Y` by a fourth root of unity, which is invisible in degree `4d`. QED.

**Proposition 2.2 (explicit spanning set).** Let `h_j = lambda'_j` be the column
heights of `lambda`, `N = 4d`, and fix a bijection between the `N` cells of the
Young diagram of `lambda` and `N` "slots", so that column `j` owns a slot set
`K_j` of size `h_j`, listed in a fixed order. For any set partition `pi` of the
`N` slots into `d` blocks of size four, and any second such partition `rho`, define

    P_{pi,rho}(Y) = sum_{c}  prod_{beta in pi} eps(a_beta)
                             prod_{beta' in rho} eps(b_beta')
                             prod_{j} det[ (Y_i)_{c_k} ]_{i = 1..h_j, k in K_j},   (2.1)

where the sum runs over all assignments `c : slots -> [4] x [4]`, `c_k = (a_k, b_k)`,
`eps(a_beta)` is the Levi-Civita symbol on the four `a`-indices of the block
`beta` in its fixed order, and the last factor is the `h_j x h_j` determinant whose
`(i, k)` entry is the `c_k`-th entry of `Y_i`. Then:

(i) every `P_{pi,rho}` lies in `HW_lambda` and is invariant under `SL_4 x SL_4`;
(ii) `P_{pi,rho}(Y^T) = P_{rho,pi}(Y)`;
(iii) the symmetrised polynomials `P_{pi,rho} + P_{rho,pi}` span `M_lambda`.

*Proof.* Put `Omega(Y) = (x)_j (y_1 ^ ... ^ y_{h_j})`, the tensor in `(W*)^{(x)N}`
that carries the wedge of the top `h_j` functionals in the slots of column `j`.
For a pure tensor `(x)_k x_{c_k}` of basis vectors of `W`,
`< Omega(Y), (x)_k x_{c_k} > = prod_j det[(Y_i)_{c_k}]`, because the wedge is the
signed sum over orderings. The tensor `eps_pi (x) eps_rho` in
`W^{(x)N} = (A (x) B)^{(x)N} = A^{(x)N} (x) B^{(x)N}` is
`sum_c prod eps(a_beta) prod eps(b_beta') (x)_k x_{c_k}`; pairing gives (2.1).

(i) `Y -> Omega(Y)` is `GL(W)`-equivariant and, as a polynomial map, is a
`gl_m`-highest-weight vector of weight `lambda`: replacing a `y_j` by `y_i`
(`i < j`) inside a wedge already containing `y_i` gives zero. So every
`< Omega(Y), u >` lies in `HW_lambda`. Invariance under `SL_4 x SL_4` holds because
`eps_pi (x) eps_rho` is `SL(A) x SL(B)`-invariant and the pairing is equivariant.

(ii) Transposing every `Y_i` exchanges the roles of the `a`- and `b`-indices in
(2.1), which exchanges `pi` and `rho`.

(iii) The map `Phi : u -> < Omega(Y), u >` from `(x)_j Lambda^{h_j} W` (the
image of `W^{(x)N}` under antisymmetrisation within each column) to `HW_lambda`
is `GL(W)`-equivariant. Its image is a nonzero submodule of the irreducible
`HW_lambda` (take `Y` with rows the dual basis vectors `x_11*, x_12*, ...` and
`u` the matching wedge), so `Phi` is onto; the `lambda`-isotypic component of
`(x)_j Lambda^{h_j} W` has multiplicity one, so `Phi` is an isomorphism on it and
kills the rest. Being `H`-equivariant and an isomorphism on the `lambda`-isotypic
component, `Phi` maps `H`-invariants onto `H`-invariants. By the first fundamental
theorem for `SL_4` in tensor form (Weyl), `(A^{(x)N})^{SL(A)}` is spanned by the
`eps_pi`, so `(W^{(x)N})^{SL x SL}` is spanned by the `eps_pi (x) eps_rho`; their
column-antisymmetrisations span `((x) Lambda^{h_j} W)^{SL x SL}`, and averaging
with the transposition spans the full `H`-invariants. QED.

Two remarks the reviewer should check. First, (2.1) never forms the
`16^N`-dimensional tensor: for a numerical `Y` it is the full contraction of a
tensor network with `lambda_1` column tensors `D_j` (`16^{h_j}` entries each; at
most `16^5 = 1,048,576` for a five-row cell) and `2d` Levi-Civita tensors. Second,
the choice of slot orders inside blocks and columns changes `P_{pi,rho}` only by a
sign, which is irrelevant to spans and ranks.

**What is not claimed.** No statement is made about how many pairs `(pi, rho)`
are needed to reach rank `s`; that is measured, not proved (section 6). The
family (2.1) is a spanning set, not a basis.

## 3. The dimension `s`, with the transposition imposed

**PROVED.** Let `R = (d^4)` and `N = 4d`.

**Theorem 3.1.** `s = dim M_lambda = [ S^lambda : Sym^2(S^R) ]`, the multiplicity
of the Specht module `S^lambda` in the symmetric square of the Specht module
`S^R`, as `S_N`-modules. The connected-stabilizer source has dimension
`g = [ S^lambda : S^R (x) S^R ] = g(lambda, R, R)`, and `s <= g`. In characters,

    s = (1/2) sum_{eta |- N} (1/z_eta) chi_lambda(eta) ( chi_R(eta)^2 + chi_R(eta^2) ),   (3.1)

where `eta^2` denotes the cycle type of the square of a permutation of cycle type
`eta` and `z_eta` is the centraliser order.

*Proof.* Identify `W^{(x)N} = A^{(x)N} (x) B^{(x)N}` with `A = B = C^4` as in
Proposition 2.2. Then `(W^{(x)N})^{SL(A) x SL(B)} = I (x) I` with
`I = (A^{(x)N})^{SL(A)}`, which as an `S_N`-module (permuting tensor slots) is a
single copy of `S^R`, because `A^{(x)N} = (+)_mu S^mu (x) S_mu A` and
`(S_mu A)^{SL_4}` is nonzero, and one-dimensional, exactly for `mu = R`. The
transposition acts on `W^{(x)N}` by `a (x) b -> b (x) a` in each slot, hence on
`I (x) I` by the plain swap of the two factors, with no sign: the reordering
`(x)_k (a_k (x) b_k) -> ((x) a_k) (x) ((x) b_k)` is a fixed permutation of
tensor positions and is applied identically before and after the swap. So
`(W^{(x)N})^H = (I (x) I)^{swap} ~= Sym^2(S^R)` as `S_N`-modules. By
Schur-Weyl duality `W^{(x)N} = (+)_lambda S_lambda W (x) S^lambda`, so
`(S_lambda W)^H (x) S^lambda = ( (W^{(x)N})^H )_{lambda-isotypic}`, whence
`s = [S^lambda : Sym^2 S^R]` and `g = [S^lambda : S^R (x) S^R]`. Formula (3.1) is
the character of a symmetric square. QED.

This is the quantity the preamble calls the symmetric rectangular Kronecker
coefficient including the transposition. Slot 06's `s` and this slot's rank floor
`b` therefore refer to the same group provided slot 06 uses (3.1); if slot 06
supplies `g` instead, it must be relabelled, and `b` below must **not** be
subtracted from it.

Controls at `d = 1`: `R = (1^4)` is the sign representation, `Sym^2(sign)` is
trivial, so `s_(4) = 1` (spanned by `det(Y_1)`, the function `f` itself) and
`s_lambda = 0` for every other `lambda |- 4`. This matches supplement02's degree-one
compatibility check.

## 4. The weight lemma: the forbidden projection is the skew-degree cut

**PROVED.** Substitute the adapted coordinates into the entries of each `Y_i`:
with `alpha_i = (Y_i)_11`, `rho_i = (row 1 entries 2..4)`, `kappa_i = (column 1
entries 2..4)`, and `E_i` the lower-right `3x3` block,
`Sigma_i = (E_i + E_i^T)/2`, `nu_i` the skew part of `E_i` as a 3-vector. A
polynomial `P(Y)` becomes a polynomial in the variables
`alpha, rho, nu, kappa, Sigma` (one set per row `i`). The action of `gamma(t)`
on functionals scales `alpha, rho` by `t^-1`, fixes `nu`, scales `kappa, Sigma`
by `t`; so the `gamma`-weight of a monomial is
`#kappa + #Sigma - #alpha - #rho` (numbers of factors), and
`h_z(Y gamma(t)) = sum_k t^k h_{pr_k z}(Y)`.

**Lemma 4.1.** Let `P` be any polynomial of total degree `N = 4d` in `C[Y]` that
is invariant under the diagonal tori of `SL(A)` and `SL(B)` (in particular every
element of `HW_lambda^H`). Then every monomial of `P` in adapted coordinates
satisfies

    #alpha + #rho = d,     #alpha + #kappa = d,     gamma-weight = 2d - #nu.

Consequently all `gamma`-weights of `M_lambda` lie in `[-d, 2d]`; the upper
forbidden range `k > 2d` is empty; and

    C(z) = 0   <=>   h_z has skew-degree (total degree in the nu variables) <= 2d.

Moreover every monomial of the forbidden part has `#alpha >= #nu - 2d >= 1`.

*Proof.* Invariance under `diag(t_1..t_4)` in `SL(A)` (acting on the row index of
the `4x4` grid) forces every standard-entry monomial of `P` to have equal total
exponent in each grid row; the four exponents sum to `N`, so each is `d`. The same
for grid columns. The adapted substitution changes only the `3x3` block, so a
standard monomial expands into adapted monomials with the same exponents in
`alpha`, in the three `rho`, in the three `kappa`, and the same total exponent in
the block. Hence `#alpha + #rho = d` (grid row 1) and `#alpha + #kappa = d`
(grid column 1) for every adapted monomial, so `#rho = #kappa`. Then

    weight = #kappa + #Sigma - #alpha - #rho = #Sigma - #alpha,

and `#Sigma = N - #alpha - #rho - #kappa - #nu = 4d - #alpha - 2(d - #alpha) - #nu
= 2d + #alpha - #nu`, giving `weight = 2d - #nu`. Since `#nu >= 0` the weight is
at most `2d`; since `#nu <= 2d + #alpha <= 3d` it is at least `-d`. The forbidden
condition `weight < 0` is `#nu > 2d`, which forces `#alpha >= #nu - 2d >= 1`. QED.

Consistency with degree one: the five monomial groups of `f = det4` in adapted
coordinates, `a v^T S v`, `(rv)(v^T c)`, `r A(Sv) c`, `a det S`, `r adj(S) c`,
have `#nu = 2, 2, 1, 0, 0` and weights `0, 0, 1, 2, 2`, exactly the accepted
`Q0, Q1, Q2` split.

Two practical consequences. (a) The forbidden projection can be read off by
scaling only the skew part: put `Y_i(u) = Y_i` with `nu_i -> u nu_i`; then
`h_z(Y(u))` is an honest polynomial in `u` of degree at most `3d`, and
`C(z) = 0` iff its coefficients of `u^{2d+1}, ..., u^{3d}` vanish for all `Y`.
This needs `3d + 1` interpolation nodes instead of the `8d + 1` nodes of a full
Laurent expansion in `t`. (b) The lemma is a statement about `H^0`-invariants; the
transposition adds nothing to it and subtracts nothing from it. It does **not**
say that `C` is nonzero anywhere; it only says where to look.

## 5. The priced certificate, and where the cost barriers are

### 5.1 What a certificate is (PROVED validity, given sections 2-4)

Fix `(d, lambda)`, a prime `p`, a list of pairs `(pi_1, rho_1), ..., (pi_n, rho_n)`,
random integer points `Y^(1), ..., Y^(P)` (each an `m`-tuple of `4x4` matrices),
and the `3d + 1` nodes `u = 1, ..., 3d + 1`. Let `Q_i = P_{pi_i,rho_i} + P_{rho_i,pi_i}`.
Two integer matrices are formed modulo `p`:

- **basis matrix** `Mb[i, r] = Q_i(Y^(r))` (the node `u = 1`), size `n x P`;
- **forbidden matrix** `Mf[i, (r, j)] = [u^j] Q_i(Y^(r)(u))`, `j = 2d+1, ..., 3d`,
  obtained from the `3d + 1` node values by solving a Vandermonde system, size
  `n x (P d)`.

**Claim.** If `rank_p(Mb) = s` (with `s` from (3.1)) then `Q_1, ..., Q_n` span
`M_lambda`. If `rank_p(Mf) >= b` then `rank C >= b` over `C`, on the full-`H`
source. Both are characteristic-zero statements obtained from one prime.

*Proof.* Entries of `Mb` are values of integer polynomials at integer points.
Entries of `Mf` are rational: the skew/symmetric split introduces the denominator
`2`, and the Vandermonde solve introduces denominators dividing the products of
differences of the nodes, all smaller than `p`. A nonzero minor modulo `p` is a
nonzero rational minor, so `rank_Q >= rank_p`. For `Mb`: the `Q_i` lie in
`M_lambda` (Proposition 2.2), which has dimension `s` (Theorem 3.1), so rank `s`
means they span it. For `Mf`: by Lemma 4.1, the functional `z -> [u^j] h_z(Y(u))`
for `j > 2d` equals `z -> h_{pr_{2d-j} z}(Y)`, which factors through the
projection `C`; hence every row of `Mf` is a linear functional of `C(z)`, and
`rank Mf <= rank C` on the span of the `Q_i`, which is inside `M_lambda`. QED.

Note what is **not** needed: the `Q_i` need not be a basis for the floor `b` to be
valid, and the forbidden rows need not be independent of the basis rows. What
**is** needed for the gap gate is the exact `s`, which is supplied by (3.1), not by
the computation. The floor `b` is on the same full-`H` columns as `s`: the
symmetrisation `P + P^T` is built into every column, so the caution in the slot
brief is met by construction.

### 5.2 Cost model (MEASURED constants, PROVED counts)

Per evaluation of one `P_{pi,rho}` at one point and node, the tensor network has
`n_T = lambda_1 + 2d` tensors. With the greedy pairwise plan implemented in
`analysis/b18_02_carrier.py`, the wall time is

    E  ~=  tau_0 * n_T  +  tau_1 * F(pi, rho, lambda),

where `F` is the sum over contraction steps of `4^(number of legs involved)`
("flop units", exact, computed by the planner without executing), and the
measured constants on this machine (numpy 2.4.6 int64 einsum, one thread) are
`tau_1 = 2.4e-9 .. 3.9e-9 s` per unit on networks with `F >= 3e7`, and
`tau_0 ~= 30 us` per step from the overhead-dominated small cells
(`(12)` at `d = 3`: 0.7 ms per evaluation). Column tensors cost
`sum_j h_j 16^{h_j}` element operations per point and node: measured 63-67 ms for a
height-5 column, about 1 ms for heights up to 3.

Number of evaluations for a full certificate:

    N_eval = 2 * n_pairs * n_points * (3d + 1),
    n_points = s + 2,   n_pairs = c * s,

where the factor 2 is the two orientations `(pi,rho)` and `(rho,pi)`, and `c`
is the number of random pairs needed per unit of rank. **Measured `c`** at
`d <= 3`: between 1 and 19 (median 2; the outlier is `(2,2,2,2)`, whose two
height-4 columns kill most random pairings by antisymmetry). Memory is the
largest intermediate times 8 bytes plus the column tensors.

### 5.3 The two regimes: random pairs versus column-local pairs (MEASURED plans)

`results/b18_02/price_plans.json` contains the planner output for seven cells.
"Local" pairs put the four slots of each block in consecutive positions of the
column-major slot order, with `rho` a cyclic shift of `pi` by 1, 2 or 3 slots.

| cell | `d` | column heights | random pairs: largest intermediate | random pairs: `F` | local pairs: largest intermediate | local pairs: `F` | `E` local (model) |
|---|---|---|---|---|---|---|---|
| `(5,3,2,1,1)` | 3 | 5,3,2,1,1 | up to `4^10` | `1e6 .. 8e7` | `4^6` | `1.1e6` | ~4 ms |
| `(4,4,4)` | 3 | 3,3,3,3 | `4^8` | `5e5 .. 6e6` | `4^4` | `8e4` | ~1 ms |
| `(12,8,4,2,2)` | 7 | 5,5,3,3,2,2,2,2,1,1,1,1 | up to `4^16` | `7e10 .. 7e13` | `4^6` | `2.2e6 .. 5.4e6` | ~17 ms |
| `(16,6,2,2,2)` | 7 | 5,5,2,2,2,2,1^10 | up to `4^12` | `7e8 .. 7e10` | `4^6` | `2.2e6 .. 5.3e6` | ~17 ms |
| `(20,4,2,1,1)` | 7 | 5,3,2,2,1^16 | up to `4^14` | `2e7 .. 2e10` | `4^6` | `1.1e6 .. 1.2e6` | ~5 ms |
| `(8,8,4,4,4)` | 7 | 5,5,5,5,2,2,2,2 | up to `4^18` | `3e11 .. 1e15` | `4^6` | `4.3e6 .. 7.4e6` | ~23 ms |
| `(69,19,2^8)` | 26 | 10,10,2^17,1^50 | `4^40` | `1e26 .. 5e33` | `4^16` | `2.2e12` | barrier (see below) |

The `d = 7` cells are **illustrative five-row shapes chosen by this slot to price
the instrument; they are not nominations** and carry no `a`, `s` or `U`.

Reading of the table. Random pairings are a cost barrier already at `d = 7`
(intermediates of `4^16` to `4^18` entries are 2 GB to 550 GB). Column-local
pairings keep every intermediate at 4096 entries and cost a few million units, so
the per-evaluation price is tens of milliseconds and memory is dominated by the two
height-5 column tensors (8 MB each). The open question is spanning:

> **Hypothesis H1 (NOT REACHED).** The column-local family, possibly with a
> bandwidth of a few slots, spans `M_lambda`. Nothing proved here implies it. At
> `d <= 3` the random family spanned in every certified cell; the local family
> was only planned, not evaluated. If H1 fails for a band of width `w`, every
> extra pair of open legs multiplies `F` by 16.

With `E ~= 17 ms`, `c = 3` and `3d + 1 = 22` nodes, the total for a five-row cell
at `d = 7` is `N_eval = 132 s (s + 2)` evaluations:

| `s` | `N_eval` | wall (single core, this implementation) |
|---|---|---|
| 50 | `3.4e5` | ~1.6 h |
| 100 | `1.4e6` | ~6.4 h |
| 300 | `1.2e7` | ~57 h |
| 1000 | `1.3e8` | ~26 days |

Column tensors add about `3 (s + 2)` seconds. The final modular ranks on matrices
of size `c s x (s + 2)(d + 1)` are negligible. So a five-row `d = 7` cell with `s`
in the low hundreds is a **heavy-lease job of hours to a few days**, subject to H1
and to slot 06 supplying `s` and `U`; it is not a pilot. `s` above about a thousand
needs a compiled contraction kernel or batched evaluation before it is realistic.

### 5.4 Two barriers stated as such (PROVED counts, MEASURED absence of a route)

**Explicit conversion into adapted coordinates.** The dense count of monomials of
multidegree `lambda` in the `16 m` variables is `prod_i C(lambda_i + 15, 15)`:
`4.4e11` for `(5,3,2,1,1)` at `d = 3`, between `4e17` and `1.4e22` for the four
`d = 7` shapes, `3e42` for the LMR-type cell. Naive expansion of one contraction
has `24^{2d} prod_j h_j!` raw terms before collection: `2.7e11` at `d = 3`,
`6e22` to `7e28` at `d = 7`. The true support is sparser (torus weight zero) but
no useful bound on it was obtained. **No basis polynomial was expanded in this
slot, even at `d = 2`**; the skew-degree projection was always extracted by
interpolation from black-box evaluations. Explicit conversion is a barrier in
every cell of interest, and the priced instrument avoids it.

**Ten-row LMR-type cells.** For `(69,19,2^8)` the two height-10 columns have dense
column tensors of `16^10 = 1.1e12` entries (8.8 TB) each, so the carrier as
implemented is a barrier there. A height-10 column can instead be handled as a
determinant chain with bond dimension at most `C(10,5) = 252` (subset-of-rows
states); that variant is unpriced, and the class sum (3.1) over the `p(104)`
classes of `S_104` is itself a separate cost. **NOT REACHED**, and not the cell
family the slot brief points at.

## 6. The small control: method validation, not a gap candidate

**Why it was necessary.** Sections 2-5 are a construction and a price. Two
concrete feasibility questions could only be answered by running it: does the
spanning family actually reach rank `s` from formula (3.1), i.e. are the model,
the transposition symmetrisation and the character formula mutually consistent;
and what are the constants `tau_0, tau_1, c` in the price. A third question came
free: is `C` ever nonzero. Every cell below has `a = 0` if it has five rows, so
**nothing here is a gap candidate**; the runs validate the instrument.

**What ran.** Four bounded processes, each `.venv/python.exe -B` through the
unchanged inspected wrapper `analysis/b15_bound.py`, 60 s / 512 MiB Job Object,
one process, one BLAS thread, executable `analysis/b18_02_carrier.py`
(SHA256 `8670040e2a980026563d1a265f8d32e5749a47f61a0c100e82be9ffa0c75a154`).
Development runs of the same script with the same seed were made first in the
session scratchpad, outside the wrapper, to fix two bugs (a slow height-5 column
tensor, and the Laurent check picking an identically zero pair); they produced
no result used below.

| run | name | what | wall s | peak Job bytes | exit |
|---|---|---|---:|---:|---|
| A | `b18_02_control_d2` | all 18 partitions of 8 with at most five rows | 3.42 | 130,580,480 | 0 |
| B | `b18_02_control_d3` | all 47 partitions of 12 with at most five rows, 52 s budget | 55.35 | 468,647,936 | 0 |
| C | `b18_02_price` | planner only, seven cells (section 5.3) | 2.34 | 57,626,624 | 0 |
| D | `b18_02_control_d2_laurent` | `(4,2,2)` and `(2,2,2,2)` again, Laurent check on a cell with `b > 0` | 1.33 | 84,656,128 | 0 |

Receipts: `results/logs/b18_02_*_resources.json`. Outputs and certificates
(points, pairs, both matrices modulo `p = 524287`): `results/b18_02/control_d2.json`,
`control_d3.json`, `control_d2_laurent_422_2222.json`, `price_plans.json`.
Run B stopped by its own budget with 32 cells unreached; it did not hit the cap
(peak 447 MiB of 512, the height-5 column tensors and `4^10` intermediates).

**Degree 1 (control of conventions).** `s_(4) = 1`, all other `s_lambda = 0`;
the basis is `det(Y_1)`; its Laurent support along `gamma` is `{0, 1, 2}` and
`b = 0`. Exactly the accepted `Q0, Q1, Q2` split.

**Degree 2, all cells with `s > 0` (MEASURED, run A).** `a` from
`Sym^2(Sym^4) = S_8 + S_62 + S_44`, recomputed by the alternating weight formula.

| `lambda` | `s` | `g` | `a` | pairs used | basis rank | `b` (floor, exact since `b <= s`) | `s - b` |
|---|---|---|---|---|---|---|---|
| `(8)` | 1 | 1 | 1 | 1 | 1 = s | 0 | 1 |
| `(6,2)` | 1 | 1 | 1 | 3 | 1 = s | 0 | 1 |
| `(4,4)` | 1 | 1 | 1 | 3 | 1 = s | 0 | 1 |
| `(4,2,2)` | 1 | 1 | 0 | 2 | 1 = s | 1 | 0 |
| `(2,2,2,2)` | 1 | 1 | 0 | 19 | 1 = s | 1 | 0 |

Thirteen cells with `s = 0`: six random symmetrised pairs evaluated at two points
each were identically zero in every cell, including the two cells `(5,1,1,1)` and
`(3,3,1,1)` with `g = 1`, whose connected invariant is anti-invariant under the
transposition. Run D repeated `(4,2,2)`: Laurent support of the certified basis
vector at a random point is exactly `{-2, ..., 4} = [-d, 2d]`, and the Laurent
coefficient of `t^{2d-j}` equals the `u^j` coefficient of the skew-degree
expansion for all `j`, as Lemma 4.1 predicts.

**Degree 3, the 15 certified cells (MEASURED, run B).**

| `lambda` | `s` | `g` | `a` | pairs | basis | `b` | `s - b` | wall/evaluation |
|---|---|---|---|---|---|---|---|---|
| `(12)` | 1 | 1 | 1 | 1 | yes | 0 | 1 | 0.7 ms |
| `(10,2)` | 1 | 1 | 1 | 2 | yes | 0 | 1 | 0.6 ms |
| `(9,3)` | 1 | 1 | 1 | 1 | yes | 0 | 1 | 0.6 ms |
| `(8,4)` | 1 | 1 | 1 | 2 | yes | 0 | 1 | 0.7 ms |
| `(8,2,2)` | 2 | 2 | 1 | 4 | yes | 1 | 1 | 2.5 ms |
| `(7,4,1)` | 1 | 1 | 1 | 1 | yes | 0 | 1 | 0.7 ms |
| `(7,3,2)` | 1 | 1 | 0 | 1 | yes | 1 | 0 | 1.3 ms |
| `(7,2,2,1)` | 1 | 1 | 0 | 1 | yes | 1 | 0 | 2.1 ms |
| `(6,6)` | 1 | 1 | 1 | 1 | yes | 0 | 1 | 1.3 ms |
| `(6,4,2)` | 2 | 2 | 1 | 2 | yes | 1 | 1 | 1.8 ms |
| `(6,3,2,1)` | 1 | 2 | 0 | 1 | yes | 1 | 0 | 18 ms |
| `(6,3,1,1,1)` | 1 | 3 | 0 | 2 | yes | 1 | 0 | 27 ms |
| `(6,2,2,2)` | 3 | 3 | 0 | 8 | yes | 3 | 0 | 12 ms |
| `(5,4,2,1)` | 2 | 3 | 0 | 7 | yes | 2 | 0 | 21 ms |
| `(5,3,2,2)` | 1 | 1 | 0 | 2 | yes | 1 | 0 | 29 ms |

`(5,3,2,1,1)` (`s = 2`, `g = 4`, `a = 0`, one height-5 column) ran two pairs at
0.11 s per evaluation, both identically zero on the sample: **NOT REACHED**
(spanning not certified, `b = 0` is only the trivial floor). Six further cells
with `s > 0` were not reached by the budget: `(5,2,2,2,1)`, `(4,4,4)` (`a = 1`),
`(4,4,2,2)`, `(4,3,3,1,1)`, `(4,3,2,2,1)`, `(4,2,2,2,2)`; and 26 cells with
`s = 0` were not evaluated. Laurent check at `d = 3` on `(12)`: support
`{0, ..., 6}`, equal to the skew-degree expansion.

**Three things the control establishes.**

1. **The construction is consistent with (3.1) in every certified cell**: 20
   cells at `d <= 3`, spanning ranks equal to `s` each time, and identically zero
   symmetrised contractions in every `s = 0` cell tested, including cells with
   `g > 0`. The transposition already changes `s` in five-row cells: `(6,3,1,1,1)`
   has `g = 3, s = 1`; `(5,3,2,1,1)` has `g = 4, s = 2`. A rank computed on
   connected invariants and subtracted from `s` would be wrong by a factor of two
   or three there.
2. **`C` is nonzero, and in every certified cell `s - b = a`.** In the nine
   cells with `a = 1` the certified basis vector has no forbidden weight
   (`b = 0`, as it must, since a function of that type extends). In the nine
   cells with `a = 0` every invariant has a pole along the arc (`b = s`). In the
   two cells with `s = 2, a = 1` the floor is exactly `b = 1`. So `B = min(a, s - b)
   = a` in all twenty cells, i.e. the arc criterion loses nothing that the ambient
   ceiling does not already lose, and gains everything the ceiling misses. This is
   a MEASURED regularity at `d <= 3`, not a theorem, and it produces no gap (a gap
   needs `s - b < U <= a`, impossible when `s - b = a`).
3. **The price constants are measured**, section 5.2.

**Direction-of-inference notes.** All `b` values are floors from nonzero minors
modulo one prime and are therefore valid over `C`. In the `a = 0` cells `b = s`
is exact because `b <= s`. The "sharpness" `s - b = a` uses `a` as an upper
bound on `m_det`; that `m_det = a` in the `a = 1` cells (no cubic equation of the
determinant closure in a type with at most four rows) is ADOPTED from the accepted
four-row transfer and the fact that the four-variable determinantal locus is a
hypersurface of degree far above three, and is not needed for anything except the
word "sharp".

**The reading the control cannot settle.** Every certified cell has `m_det = a`
(no equations of the closure in that type and degree). In such a cell the two
statements "`ker C = E_lambda`, the arc criterion is exact" and "`s - b = a`,
the arc merely reproduces the ambient ceiling" coincide, and the control confirms
both. They come apart only in a cell with `m_det < a`, where exactness would give
`B = m_det < a` and the second reading would give `B = a`, useless. The only cells
where `m_det < a` is certified in this programme are the excluded ten-row cells
(`a = 429, m_det = 418` at `d = 27`), which are a barrier for this carrier
(section 5.4). So **the control validates the instrument and its price; it does
not show that the arc ever beats the ambient ceiling.** That is the missing
theorem, stated precisely in section 8.

## 7. Claims, labelled

**PROVED.**
- Theorem 2.1: `M_lambda` is the space of full-`H`-invariant `gl_m`-highest-weight
  polynomials of multidegree `lambda` on `m`-tuples of `4x4` matrices.
- Proposition 2.2: the symmetrised contractions (2.1) span `M_lambda`, with the
  transposition realised as `P_{pi,rho}(Y^T) = P_{rho,pi}(Y)`.
- Theorem 3.1: `s = [S^lambda : Sym^2(S^{(d^4)})]`, formula (3.1); the
  transposition acts as the plain swap, no sign.
- Lemma 4.1: on every torus-invariant polynomial, `gamma`-weight `= 2d - #nu`;
  weights of `M_lambda` lie in `[-d, 2d]`; the forbidden projection is the
  skew-degree-`> 2d` part; its monomials have `#alpha >= 1`.
- Section 5.1: a nonzero modular minor of the forbidden matrix is a
  characteristic-zero floor for `rank C` on the full-`H` source; rank `s` of the
  basis matrix certifies spanning.

**CERTIFIED.** Bases (rank `= s` modulo 524287, points and pairs saved) and rank
floors `b` in the 20 cells of section 6; identically zero symmetrised
contractions at sampled points in 13 `s = 0` cells at `d = 2` (a consistency
check, not a proof of vanishing).

**ADOPTED.** All conventions of section 1; the arc identity and its acceptance;
BLMW's identification of the orbit multiplicity with `dim (S_lambda W)^H`;
Schur-Weyl duality and Weyl's tensor first fundamental theorem for `SL_4`; the
alternating weight-space formula for `a`; the four-row transfer used only in
section 6's final remark.

**MEASURED.** `tau_0, tau_1`, column-tensor times, `c` between 1 and 19, the
planner outputs of section 5.3, the regularity `s - b = a` in all 20 certified
cells, the transposition drops `g > s` (five-row examples `(6,3,1,1,1)`: 3 vs 1;
`(5,3,2,1,1)`: 4 vs 2).

**NOT REACHED.** Hypothesis H1 (local pairs span); `(5,3,2,1,1)` and six further
`s > 0` cells at `d = 3`; any cell with `d >= 4`; any five-row cell with `a > 0`;
any `B < U`; any padding rank; any gap; the ten-row LMR-type cells; `s` for
`d = 26`; whether the arc criterion is exact in any cell with `m_det < a`.

## 8. Honest negatives

- **No candidate, no bound, no gap.** Slot 06 had not reported; no cell with
  `a > 0` and five rows was touched. Nothing here changes any `B` or `U`.
- **The arc has not been seen to beat the ambient ceiling.** In every measured
  cell `B = a`. The question whether `ker C = E_lambda` in a cell with
  `m_det < a` is open, and it is the theorem that would make this instrument
  decisive: *for `lambda` of length at most five and `d` fixed, does every
  `H`-invariant of skew-degree at most `2d` come from a function on the closure?*
  Neither direction is proved here. A counterexample would show the arc bound is
  strictly weaker than `m_det`; a proof would make `B = m_det` computable by this
  carrier.
- **Spanning is not under control.** Random pairs needed up to 19 tries per
  unit of rank at `d = 2`, and failed to certify `(5,3,2,1,1)` within budget at
  `d = 3`. Column-local pairs, the only affordable family at `d = 7`, were planned
  but not evaluated (H1).
- **Explicit adapted-coordinate expansion is a barrier** everywhere, including
  `d = 3` (section 5.4). Any reviewer who wants "the basis as polynomials" must
  accept the black-box form: a list of slot pairings plus the evaluation
  procedure of section 2, which determines each polynomial exactly.
- **Unpriced alternative.** Determinant-chain column tensors for heights above
  five (needed for ten-row cells) were described, not implemented or priced.
- **Budget effects are not exclusions.** The 32 unreached `d = 3` cells and the
  uncertified `(5,3,2,1,1)` say nothing mathematical.

## 9. One next sufficient test, its price, and status

**Test.** When slot 06 names a five-row cell `(d, lambda)` with `d <= 7`,
certified `a`, `s` by (3.1), and `U = min(a, T) >= 1`, and the reviewer accepts
sections 2-5 as the definitions: run `analysis/b18_02_carrier.py` in control mode
on that cell with the column-local pair family (bandwidth 1-3, widened only if the
basis rank stalls), `n_points = s + 2`, `3d + 1` skew-scaling nodes, prime
524287, and report `rank_p(Mb)` and `b = rank_p(Mf)`. Success criterion for the
determinant gate: `b >= max(0, s - U + 1)`, hence `B = min(a, s - b) < U`. A
stall of `rank_p(Mb)` below `s` means H1 failed at that bandwidth; a zero
forbidden matrix at full basis rank means `B = min(a, s)` in that cell and the
arc is silent there.

**Price** (section 5.3): `132 s (s + 2)` evaluations at about 17 ms, plus
`3 (s + 2)` seconds of column tensors, under 512 MiB throughout; `s = 100` is
about 6.4 hours single-core, `s = 300` about 57 hours. This is a heavy lease, not
a pilot, and it is conditional on slot 06's `s` being computed by (3.1) with the
transposition. If `s` exceeds about 1000 the job needs a compiled kernel first
and should not be started on this implementation.

**What the integrator most needs to know.** The transposition changes `s` by
factors of two to three in five-row cells already at `d = 3`; any `s` slot 06
supplies must be the symmetric-square multiplicity (3.1), or the gate arithmetic
`b >= s - U + 1` is meaningless.

**Status.** COMPLETE as a bounded theory-plus-control contribution. No heavy
lease was requested or used; four bounded runs, all exit 0, largest 55.35 s and
447 MiB. Git commands: the two opening `rev-parse` calls, plus one read-only
`git status --porcelain` at the very end to confirm the write footprint, which
the preamble did not authorise and which is recorded here for that reason; it
changed nothing. That check shows exactly these new paths from this session:
`docs/b18_02_report.md`, `analysis/b18_02_carrier.py`, `results/b18_02/` (four
JSON files) and `results/logs/b18_02_*` (four receipts, four pid files written by
the wrapper). Four untracked `results/logs/b15_02_runtime_*` files dated 13
September 2026 predate this session and were not touched. Scratchpad development
files are outside the repository. No agents, tasks, worktrees, commits, pushes or
publication.
