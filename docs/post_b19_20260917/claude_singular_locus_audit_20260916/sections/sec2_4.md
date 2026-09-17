
## 2. Definitions used below (kept distinct)

Throughout, `V = W = C^4`, `Mat4 = Hom(V, W)`, `G = SL4 x SL4` acting by `B -> P B Q`, and a
"tuple" is `T = (B_1, ..., B_5)`, viewed also as the tensor `sum_k e_k (x) B_k` in
`C^5 (x) C^4 (x) C^4` with `GL5` acting on the index `k`. `X = span(B_1, ..., B_5)` in `Mat4`.
`Z = {T : det(sum_k x_k B_k) == 0 identically}`, i.e. `X` is a *singular* (rank `<= 3`) subspace.

- **Rank, nondegenerate, compression space, projection, primitive, primitive part**:
  EH's definitions, quoted in section 1.1. "Compression space of rank `k`" requires *equality*
  `codim V' + dim W' = k`; a space merely contained in a compression space of rank `<= 3` is
  called here *sub-compression*.
- **Imprimitive**: EH's negation of primitive (some `(V', W') != (V, W)` with
  `rank pi^{-1} pi(M) = rank M`). HL/Atkinson-Lloyd's "imprimitive" (one hyperplane restriction
  of `phi` or `phi^t` drops the bounded rank by one) implies EH-imprimitive; the converse is
  not used and not claimed.
- **Shrunk subspace**: `V'` in `V` with `dim X.V' < dim V'`, where `X.V' = span{A v : A in X,
  v in V'}`. In adapted bases this is a `p x q` zero block common to all of `X`, with
  `p = 4 - dim X.V'` rows and `q = dim V'` columns, `p + q > 4`.
- **`G`-semistable tuple**: `T` outside the null cone of `G`; equivalently some
  positive-degree `G`-invariant is nonzero at `T`. The `G`-invariants of `(Mat4)^5` are
  spanned by the blow-up determinants `det(sum_k M_k (x) B_k)`, `M_k in Mat_m` (Domokos-Zubkov,
  Derksen-Weyman, Schofield-Van den Bergh; adopted exactly as in the B15-12 note), so one
  nonzero blow-up determinant certifies `G`-semistability. Semistability is transpose-
  invariant (swap the two `SL4` factors).
- **Five-row source functions**: for `l(lambda) = 5` the full-`H` source `M_lambda` sits inside
  the `S_lambda`-isotypic component of `C[(Mat4)^5]^G`. That component is `GL5`-stable and is
  spanned by multihomogeneous functions whose multidegree `nu` (degree `nu_k` in the entries
  of `B_k`) is a weight of `S_lambda(C^5)`, hence satisfies `nu_5 >= lambda_5 >= 1` (each of
  the `lambda_5` columns of height 5 of a semistandard tableau contains a 5). This is the
  B15-12 note's Claim 4.2.2, which stays PROVED and is used again in section 4.

## 3. Compression, shrunk subspaces and instability (elementary, self-contained)

**Lemma 3.1 (shrunk implies `G`-unstable).** If `X` has a shrunk subspace, every
positive-degree `G`-invariant vanishes at every tuple whose span is contained in `X`.

*Proof.* Choose bases with `V' = <e_1..e_d>` and `X.V'` inside `<f_1..f_{d-c}>`, `c >= 1`.
Then every `A in X` vanishes on the block `R x C` with `R = {d-c+1..4}` (`|R| = 4-d+c`) and
`C = {1..d}`. Take the one-parameter subgroup `P(t) = diag(t^{p_i})`, `Q(t) = diag(t^{q_j})`
with `p_i = -(d-c)` for `i in R`, `p_i = 4-d+c` for `i not in R`, `q_j = -(4-d)` for `j in C`,
`q_j = d` for `j not in C`. Both exponent vectors sum to zero, so `(P(t), Q(t))` lies in `G`.
Entry `(i, j)` of `P A Q` is multiplied by `t^{p_i + q_j}`, which is `t^{c}` on `R x C^c`,
`t^{c}` on `R^c x C`, and `t^{4+c}` on `R^c x C^c`; the block `R x C` is zero. All nonzero
entries carry a positive weight, so `(P(t), Q(t)).T -> 0` as `t -> 0`; a homogeneous
invariant of positive degree is constant on the orbit and continuous, hence equals its
value at `0`. QED

**Lemma 3.2.** (a) A subspace of a compression space of rank `<= 3` has a shrunk subspace.
(b) A degenerate space (common kernel vector, or all images in a hyperplane) has a shrunk
subspace. (c) Every `4 x 4` space of rank `<= 2` has a shrunk subspace.

*Proof.* (a) `A(V')` inside `W'` for all `A in X` with `codim V' + dim W' <= 3` gives
`dim X.V' <= dim W' <= 3 - codim V' = dim V' - 1`. (b) Common kernel `v`: `V' = <v>`,
`X.V' = 0`. Images in a hyperplane `H`: `V' = V`, `X.V` inside `H`. (c) If degenerate, use
(b). If nondegenerate, EH Corollary 1.4 with `k = 2`, `s = 4 >= 4` (or `k = 1`; rank 0 is
trivial) makes it a compression space; use (a). QED

Hence the only tuples in `Z` that can carry a nonzero `G`-invariant are those whose span
`X` is nondegenerate of generic rank exactly 3 and is not sub-compression. This handles
generic ranks `<= 2` and both transposes without any classification of rank-2 spaces
beyond Corollary 1.4.

**Lemma 3.3 (classification input; EH Theorems 1.1, 1.2, Corollary 1.3).** Let `X` in `Mat4`
be a `G`-semistable singular subspace. Then, after a change of bases of `V` and `W` and
possibly a transpose, either

- (P) `dim X = 4` and `X` is one of the primitive `4 x 4` spaces (12), (13) of Theorem 1.2; or
- (S) `X` is a subspace of `Mt := { [[S, u], [0, t]] : S in skew_3, u in C^3, t in C }`,
  `dim Mt = 7`.

*Proof.* By Lemmas 3.1-3.2, `X` is nondegenerate of rank exactly 3 and not a compression
space, so Corollary 1.3 leaves two cases. If `X` is primitive, Theorem 1.2 applies; among the
listed spaces only (12), (13) and their transposes are `4 x 4` (equivalence preserves
`dim V` and `dim W`), and each is the full 4-parameter family, so `dim X = 4`: case (P).
Otherwise `X` has a primitive part `M' = pi_{V',W'}(X)` equal, up to equivalence, to the
`3 x 3` skew space (rank `k' = 2`) with `rank pi^{-1}(M') = rank X = 3`, so the rank formula
of p. 139 gives `codim V' + dim W' = 1`. Case `codim V' = 1, W' = 0`: `M'` in `Hom(V', W)` is a
rank-2 primitive space of `4 x 3` matrices; its nondegenerate core (quotient by the common
kernel `K` in `V'`, restriction to the span `W''` of the images) is primitive of rank 2, hence
by Theorem 1.1 the `3 x 3` skew space, which forces `K = 0`, `dim W'' = 3`. In adapted bases
`M' = {[[S],[0]] : S skew}` and `X` lies in `pi^{-1}(M') = {A : A|_{V'} in M'} = Mt`. Case
`V' = V, dim W' = 1` is the transpose. QED

`Mt` has generic rank 3 (`det [[S,u],[0,t]] = t . det S = 0`) and **no shrunk subspace**: for
`v = (x, y)` with `y != 0`, `Mt.<v>` contains `(Sx + yu, ty)` for all `S, u, t`, which spans
`C^4`; for `V'` inside `C^3 x 0`, `Mt.V' = sum_{x in V'} x^perp` has dimension `2, 3, 3` for
`dim V' = 1, 2, 3`. Therefore `Mt` (dimension 7) and, for instance, its 5-dimensional subspace

    X_0 = skew_3 + <E_14> + <E_44>,   B_1 = E_12 - E_21, B_2 = E_13 - E_31,
                                      B_3 = E_23 - E_32, B_4 = E_14, B_5 = E_44,

are `G`-semistable singular spaces of dimension `>= 5`. For `X_0` this is certified in
section 6 (check 1: blow-up determinant `-1044 != 0`), and also follows from the
shrunk-subspace criterion by a short case check (`X_0.<(x,y)>` contains `x^perp + <e_1, e_4>`
when `y != 0` and equals `x^perp` when `y = 0`; `X_0.V'` contains `C^3` whenever `V'` meets
`C^3 x 0` in a plane).

**Consequence for the note's hypothesis.** H-EH ("every singular subspace of `Mat4` of
dimension `>= 5` is a compression space") is **false**; `Mt` and `X_0` are explicit
counterexamples, and they are even `G`-semistable. The prior sessions' caution (ledger E22,
CONDITIONAL) was justified. The note's Claim 4.2.3 in the non-surjective-kernel case is not
merely unproved but wrong as a dimension bound: on `Mt` the kernel map is linear,
`kappa(S, u, t) = (axis(S), 0)` with 3-dimensional image `C^3 x 0` (check 1 records the
generic kernel `(c/a, -b/a, 1, 0)`), while `dim Mt = 7`. On `Mt^T` the kernel map is not
linear (`ker [[S,0],[u^T,t]] = <(axis S, -<u, axis S>/t)>`), so the "kernel degree `>= 2`"
case the note flagged is realised, not vacuous. By Lemma 3.3 these are the only two shapes
that occur.

## 4. The closure theorem: `Z` is invisible to every five-row cell

**Theorem 4.1.** Let `lambda |- 4d` with `l(lambda) = 5`. Every element of the
`S_lambda`-isotypic component of `C[(Mat4)^5]^G` (in particular every element of the full-`H`
source `M_lambda`) vanishes identically on `Z`. Hence `rho_Z = 0` in every five-row cell, and
the restriction bound of the B15-12 note (its Theorem 3.1, corrected form E18) reads
`m_det <= min(a, s)` on `L = Z`: the singular-pencil locus contributes nothing.

*Proof.* Let `T = (B_1..B_5)` in `Z`, `X = span(B_i)`, and `f` in the isotypic component.
Case 1: the `B_i` are dependent. Then `f(T) = 0` by the note's Claim 4.2.2 (section 2).
Case 2: the `B_i` are independent but `T` is `G`-unstable. Then `f(T) = 0` because `f` is a
positive-degree `G`-invariant.
Case 3: independent and `G`-semistable, `dim X = 5`. Lemma 3.3 applies; (P) is impossible
(`dim = 4`), so up to bases and transpose `X` lies in `Mt`. The linear map `Mt -> skew_3 + C`,
`[[S,u],[0,t]] -> (S, t)`, has 4-dimensional target, so its restriction to the 5-dimensional
`X` has a nonzero kernel: `X` contains a nonzero matrix `B_5' = [[0, u_0],[0, 0]]`
("column-only"). Since the isotypic component is `GL5`-stable, it suffices to prove
vanishing at one tuple spanning `X`; choose the tuple with fifth entry `B_5'` and any
completion `B_1'..B_4'` to a basis of `X`, and it suffices to treat weight vectors `f` of
multidegree `nu`, which have `nu_5 >= 1` (section 2). Consider the one-parameter subgroup
of `GL5 x G`

    g(tau) = ( diag(1, 1, 1, 1, tau^{-4+eps}),  P(tau) = diag(tau, tau, tau, tau^{-3}),
               Q(tau) = diag(tau^{-1}, tau^{-1}, tau^{-1}, tau^{3}) ),   0 < eps < 4.

`(P, Q)` lies in `G` and scales entry `(i, j)` by `tau^{p_i + q_j}`: the `S` block
(`i, j <= 3`) by `tau^0`, the `u` column (`i <= 3, j = 4`) by `tau^4`, the `t` entry by
`tau^0`, and the bottom-left row (`i = 4, j <= 3`), which is zero on all of `Mt`, by
`tau^{-4}`. The `GL5` factor multiplies `B_5'` by `tau^{-4+eps}`. So every nonzero entry of
`g(tau).T` carries exponent `0` or `4` (in `B_1'..B_4'`) or `eps` (in `B_5'`), all `>= 0`:
the limit `T_0 = lim_{tau -> 0} g(tau).T` exists. On the other hand `f` is `G`-invariant and
of degree `nu_5` in `B_5'`, so `f(g(tau).T) = tau^{-(4-eps) nu_5} f(T)`. As `tau -> 0` the
left side tends to `f(T_0)`, which is finite, while the right side is unbounded unless
`f(T) = 0`. Hence `f(T) = 0`. For the transposed shape use
`P(tau) = diag(tau^{-1}, tau^{-1}, tau^{-1}, tau^{3})`, `Q(tau) = diag(tau, tau, tau, tau^{-3})`
and the row-only element of `X`. QED

**Remarks.** (i) For rectangular `lambda = (m^5)` the source consists of `SL5 x G`-invariants,
and the proof shows more: the tensor `T` is `SL5 x G`-unstable for every 5-dimensional `X`
in `Mt` (perturb to `a = ((4-eps)/4, ..., (4-eps)/4, -(4-eps))`; all exponents stay
positive). This is why check 2 (section 6) *had* to return zeros for the certified `(4^5)`
vectors on `X_0`: those zeros are now a theorem, not sampled evidence. (ii) The same
argument with `m` matrices and `l(lambda) = m >= 5` gives `rho_Z = 0` in every cell with at
least five rows in any `m`-variable model: a `G`-semistable `m`-dimensional singular span is
again of shape (S) (case (P) has dimension 4), the projection to `(S, t)` has an
`(m-4)`-dimensional kernel on `X`, and `nu_m >= lambda_m >= 1`. (iii) Nothing here concerns
cells with at most four rows: the primitive spaces (12), (13) are `G`-semistable singular
4-dimensional spaces (the "semistable singular spaces of dimension four" of the earlier
work; the note's `X_Lambda` is one of them), and a four-row function need not vanish there.
That is outside the five-row programme and is not pursued.
