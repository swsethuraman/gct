# Singular-pencil locus audit: was Z legitimately excluded as a source of five-row determinant constraints?

Claude session, 16 September 2026. Fresh directory `work/claude_singular_locus_audit_20260916/`
(created by this session; nothing pre-existed). Historical files read-only; no agents,
no commits, no dependency changes. Written incrementally; the status line is replaced at the end.

Status: **COMPLETE** — closure theorem delivered (section 4); H-EH refuted (section 3); the exclusion of `Z` is upheld by a different proof. The provisional verdict of section 0 is confirmed in the sense stated in section 7.

## 0. Question and provisional verdict (written before the sources were read)

Question. For tuples `B = (B_1..B_5)` of `4x4` matrices, `phi(B) = det(sum x_i B_i)`,
`Z = phi^{-1}(0)` (identically singular pencils). Five-row full-`H` functions vanish on
tuples whose five matrices are linearly dependent (proved: B15-12 note Claim 4.2.2). The
proposed dismissal of `Z` as a source of five-row constraints rested on the unverified
hypothesis H-EH: "every singular subspace of `Mat4` of dimension `>= 5` is a compression
space". Was that dismissal legitimate?

Provisional verdict (to be confirmed or overturned in §5): the exclusion was NOT proved
by the linear-kernel argument alone; whether the primary classification closes it is
exactly what this audit decides.

## 1. Sources actually read (primary text, not paraphrase)

**Eisenbud–Harris, *Vector spaces of matrices of low rank*, Adv. Math. 70 (1988) 135–155.**
Fetched from `https://eisenbud.github.io/papers/pdfs/1988-004.pdf`; SHA-256
`6b10d8fea80396a7c833391847decd0da346f3b08a4e45e2e858f5a6f2f10657` (1,067,244 bytes; same
prefix as recorded by the descent follow-up session, which could not read it). The file is a
scan with no text layer (330 CCITT G4 strips, 18 per page). This session reassembled the
strips into 21 page images (script `checks/render_eh_pages.py`, ImageMagick 7.1.2 for the
G4 decode; images kept in the session scratchpad, outside the delivery tree, per the
literature rule) and read pages 135–141 directly. Everything quoted below was transcribed
from those images; page numbers are the journal's.

**Huang–Landsberg, *On linear spaces of matrices of bounded rank*, arXiv:2306.14428 (v1, 26
June 2023; no journal reference on the abstract page).** Read through the arXiv HTML
rendering `https://arxiv.org/html/2306.14428v1`, §1 (Examples 1.1–1.3), §4.1 (Atkinson–Lloyd,
Atkinson), §4.2 (Eisenbud–Harris), §2 Theorem 2.1. Used only as corroboration of the
rank-three classification and for the *other* meaning of "primitive"; no result of this
paper is load-bearing below.

**Atkinson, *Primitive spaces of matrices of bounded rank II*, J. Austral. Math. Soc. 34
(1983) 306–315.** Not fetched. Cited by EH (p. 135, p. 136) as an independent, prior proof of
the rank `<= 3` classification, and restated by HL §4.1 as "for `r = 3` the only primitive
examples are Example 1.3 and its projections". It is not needed: the closure below uses EH's
own statements.

### 1.1 Verbatim statements (EH, pp. 135–141)

- p. 135: "The basic objects to be considered here are vector spaces of linear
  transformations, that is, a pair of vector spaces `V` and `W` and a linear subspace
  `M ⊂ Hom(V, W)`, over an algebraically closed field. We will say that `M` has *rank `k`* if
  the maximum of the ranks of the matrices in `M` is `k`."
- p. 137: "we will henceforward assume that `M` is *nondegenerate*, in the sense that the
  kernels of elements of `M` intersect in 0 and the images of the elements of `M` generate
  `W`."
- p. 137: "Suppose that for some subspaces `V' ⊂ V` and `W' ⊂ W` of codimension `k_1` and
  dimension `k_2`, respectively, every map in `M` maps `V'` into `W'`. It is easy to see that
  the rank of `M` is at most `codim V' + dim W'`. If equality holds, we will call `M` a
  *compression space*". "In general, a compression space of rank `k` is one which is
  equivalent to a space of `(dim V) x (dim W)` matrices having a common `v_1 x w_1` block of
  zeros with `(dim V − v_1) + (dim W − w_1) = k`, the largest possible value."
- p. 138: display (4) is the `3 x 3` skew-symmetric space (rank 2); display (5) is the
  `4 x 6` space `e -> e ∧ ·` on `Λ^2` of a 4-space (rank 3); "the transpose of the space (4)
  is equivalent to (4) itself, but this is obviously no longer true for the space (5)";
  display (6) is `(0 a b *; −a 0 c *; −b −c 0 *; 0 0 0 0)`, "the rank 3 spaces of matrices"
  obtained from (4) "by adding some rows or columns of arbitrary entries".
- p. 139: "if `V' ⊂ V` and `W' ⊂ W` are subspaces, and `M' ⊂ Hom(V', W/W')` is any space of
  maps of rank `k'`, then the space `M ⊂ Hom(V, W)` of maps that induce maps in `M'` has rank
  `k = k' + codim V' + dim W'`." "we write `π = π_{V'W'}` for the *projection* map from
  `Hom(V, W)` to `Hom(V', W/W')`". "We say that a space `M ⊂ Hom(V, W)` is *primitive* if
  there are no subspaces `V' ⊂ V` and `W' ⊂ W` with `(V', W') ≠ (V, W)` such that
  `rank(π^{-1}(π(M))) = rank(M)` with `π = π_{V',W'}`. (7)" "If `M` is not primitive, there
  will exist `V'` and `W'` satisfying (7) such that `M' = π_{V',W'}(M)` is primitive; we call
  `M'` a *primitive part* of `M`." "a compression space (such as (1), (2), or (3)) is exactly
  a space whose primitive part is zero; in particular, there are no primitive spaces of rank
  1. The space (4) of skew-symmetric `3 x 3` matrices is primitive, as indeed are all the
  spaces which like (4) and (5) are of the form `M ⊂ Hom(M, Λ^2 M)`, and a primitive part of
  the space (6) is given by the first three rows."
- p. 140: "One warning: the primitive part of a space of maps is not in general unique."
  "**Theorem 1.1.** *A space of matrices of rank `<= 2` is either a compression space or is
  primitive, in which case it is the space (4) of `3 x 3` skew-symmetric matrices.*"
  "In rank 3 there are two complications: projections of the space (5) appear, and there are
  imprimitive spaces which are not compression spaces, obtained by adding a row or column to
  example (4), as in (6)." "**Theorem 1.2.** *A primitive rank 3 space of matrices is
  equivalent either to (5) or its transpose or to one of the following four projections of
  (5) and their transposes, which are themselves primitive and pairwise inequivalent:*"
  (10) and (11) are `4 x 5`, (12) and (13) are `4 x 4`; all four are parametrised linearly by
  `a, b, c, d` (dimension 4).
- p. 141: "We postpone the proofs until Section 3." "**Corollary 1.3.** *A nondegenerate space
  of matrices of rank 3 is either a compression space, or primitive, or has rank 3 and
  primitive part the space of `3 x 3` skew-symmetric matrices, so that it is of the form
  given by (6) or its transpose.*" "**Corollary 1.4.** *Let `M ⊂ Hom(V, W)` be a nondegenerate
  space of rank `k`, and set `s = min(dim V, dim W)`. If `k = 1` or `k = 2` and `s >= 4` or
  `k = 3` and `s >= 5` then `M` is a compression space.*"

Two remarks on scope that matter here. (i) The proofs of Theorems 1.1–1.2 are in EH §3 and
rest on the sheaf theorem of §2; Atkinson [2] is cited as an independent earlier proof. This
audit takes the theorems as published and does not re-verify their proofs. (ii) In
Corollary 1.4 the letter `s` is the **matrix size** `min(dim V, dim W)`, not the dimension
of `M`. For `4 x 4` matrices `s = 4`: rank `<= 2` spaces are covered (`s >= 4`), rank 3 spaces
are **not** (`s >= 5` fails). That is exactly the borderline the note's hypothesis H-EH
ignored.

### 1.2 The prior session's B.6 outcome, re-examined

The descent follow-up report (§B.6 outcome, ledger E22) could not read the PDF and recorded
HL's restatement of Atkinson only. Its caution was correct: HL's "primitive" (§4.1: "A bounded
rank `r` space is imprimitive if there exists `H ⊂ B^*` such that `φ|_H` is of bounded rank
`r − 1` or if there exists `H ⊂ C^*` such that `φ^t|_H` is of bounded rank `r − 1`. Otherwise
it is primitive") is the one-row/one-column reduction, while EH's primitivity (7) allows a
simultaneous row-and-column projection and demands that the *full preimage* keep the rank.
The two notions are not interchangeable and the audit below uses EH's throughout.

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

## 5. Answers to the seven required items

1. **Primary statements read.** EH Theorems 1.1, 1.2, Corollaries 1.3, 1.4 and the
   definitions, transcribed verbatim from the scanned primary text (section 1.1, pages
   135-141, PDF SHA-256 `6b10d8fe...`). HL arXiv:2306.14428v1 sections 1, 4.1, 4.2 read for
   the Atkinson restatement and the competing definition of "primitive". Atkinson 1983 and
   Ballico's addendum (Beitraege Algebra Geom. 36 (1995) 119-122, "...and vector bundles on
   projective spaces") were **not** read: the EUDML record carries no abstract and zbMATH
   refused the fetch. Ballico's title points at the bundle-theoretic part (EH sections 2
   and 4); no correction to the rank `<= 3` statements of EH section 1 is known to this
   session, and Atkinson's independent proof (cited by EH p. 136 and restated by HL) covers
   the same statements. This residual dependence is recorded in the ledger (C3).
2. **Definitions** kept distinct in section 2: EH-primitive (projection form (7)) versus
   HL/Atkinson-Lloyd-primitive (hyperplane form); compression (equality) versus
   sub-compression; shrunk subspace; `G`-semistability; `GL5 x G` weight vanishing.
3. **Generic ranks.** Rank `<= 2` (either side): Lemma 3.2(c) via Corollary 1.4, unstable.
   Rank 3 degenerate: Lemma 3.2(b), unstable. Rank 3 compression: Lemma 3.2(a), unstable.
   Rank 3 primitive: dimension 4 (Theorem 1.2), so a five-tuple in it is dependent.
   Rank 3 with skew primitive part: shape (S) or its transpose (Lemma 3.3), semistable
   possible, and handled by Theorem 4.1. Transposes appear in Lemma 3.3 and in the last
   line of the proof of Theorem 4.1.
4. **The linear-kernel argument.** Surjective `kappa`: the note's proof stands
   (`dim X <= 4`). Non-surjective `kappa`: the conclusion `dim X <= 4` is **false** (`Mt`,
   `dim 7`, `kappa` linear with 3-dimensional image). Non-linear kernel map: realised by
   `Mt^T`. So Claim 4.2.3 cannot be completed as a dimension bound; the route is closed
   instead by Theorem 4.1, whose mechanism is a `GL5 x G` one-parameter subgroup, not a
   dimension count.
5. **Semistable independent five-tuple in `Z` under `G = SL4 x SL4`: YES.**
   `X_0 = skew_3 + <E_14> + <E_44>` with the basis of section 3 is independent, identically
   singular, and `G`-semistable (check 1: degree-8 blow-up determinant `-1044`). But under
   the group that matters for five-row functions the answer is **no**: for every
   5-dimensional singular `G`-semistable `X` the tensor is `SL5 x G`-unstable (Remark 4.1(i)),
   and every five-row isotypic component vanishes on it (Theorem 4.1). The earlier "no
   compression subspace" paraphrase conflated the two questions.
6. **Not applicable as an inference; recorded as a negative.** Because such spaces exist,
   the certification protocol was executed rather than assumed: check 2 evaluated the two
   certified full-`H` vectors `q_3, q_7` of `M_(4^5)` (descent follow-up session, ledger E5)
   at four `GL5`-mixes of `X_0` after two controls that can fail (the stored `K5` values are
   reproduced; a dependent tuple gives zero). All eight values are zero, exactly as
   Theorem 4.1 predicts; they are **not** used as evidence, the theorem is. Had a nonzero
   residue appeared, it would have refuted Theorem 4.1 (a nonzero residue mod `P` is a
   nonzero integer).
7. **Complete deduction that `Z` is invisible to all five-row functions:** Theorem 4.1 with
   Lemmas 3.1-3.3, citing EH Theorem 1.1 (p. 140), Theorem 1.2 (p. 140), Corollary 1.3
   (p. 141), Corollary 1.4 (p. 141), the rank formula (p. 139) and the nondegeneracy
   convention (p. 137).

## 6. Bounded checks (two, both through the inspected Job Object wrapper)

Wrapper: `work/batch15_workers/B15-02/analysis/b15_bound.py` (60 s, 512 MiB, one worker,
one BLAS thread, `job_object_enforced: true` in both receipts under `checks/results/logs/`).
Both checks were prepriced from the descent follow-up receipts (0.34 s per column tensor,
0.55 s per vector evaluation).

| check | script / certificate | content | wall | outcome |
|---|---|---|---|---|
| 1 | `checks/check1_counterexample.py` -> `.json` | `det(sum x_i B_i)` for `X_0` expands to `0` (sympy, exact); the five matrices are independent (rank 5); 2x2 blow-up with fixed integer `M_k` (seed 20260917) has determinant `-1044`; generic rank 3; generic kernel `(c/a, -b/a, 1, 0)` | 1.16 s | PASSED: `X_0` in `Z`, independent, `G`-semistable |
| 2 | `checks/check2_restriction_to_Z.py` -> `.json` | `q_3, q_7` (p6_basis.json plans, p7 hand orders, `P = 524287`) at four `GL5(Z)`-mixes of `X_0` (mix determinants `-246, 57, -54, 150`) | 5.97 s | all values `0`; controls passed (`K5` values `94237, 491460` reproduced; dependent tuple `0, 0`) - INCONCLUSIVE as evidence, CONSISTENT with Theorem 4.1 |

Two aborted starts of check 2 (0.75 s and 0.31 s, no computation reached) were caused by
this session's own script errors (list-versus-tuple plan labels; a wrong assertion about
which basis file p7 used - it used `p6_basis.json`). They are not retries of a failed
bounded computation. Total measured wall time including them: about 8.2 s.

## 7. Claim ledger, negatives, and the next lemma

| id | claim | status | where |
|---|---|---|---|
| C1 | EH Thms 1.1, 1.2, Cors 1.3, 1.4 as transcribed | READ FROM PRIMARY SCAN (proofs not re-verified) | section 1.1 |
| C2 | HL's "primitive" differs from EH's | VERIFIED from both texts | sections 1.2, 2 |
| C3 | No later correction alters EH section 1 | NOT VERIFIED (Ballico addendum not read; title indicates bundle scope; Atkinson independent proof) | section 5.1 |
| C4 | Shrunk implies `G`-unstable; compression/degenerate/rank `<= 2` are shrunk | PROVED (Lemmas 3.1, 3.2; 3.2(c) uses Cor 1.4) | section 3 |
| C5 | `G`-semistable singular `X` is (P) dim 4 or (S) inside `Mt` | PROVED from C1 | Lemma 3.3 |
| C6 | H-EH is false; `Mt`, `X_0` are `G`-semistable singular of dim 7, 5 | PROVED and CERTIFIED (check 1) | section 3, check 1 |
| C7 | Note's Claim 4.2.3, non-surjective case | REFUTED as a dimension bound | section 3 |
| C8 | Every five-row isotypic component vanishes on `Z` (`rho_Z = 0`) | PROVED (Theorem 4.1), conditional only on C1 | section 4 |
| C9 | Same for `>= 5` rows in any `m`-variable model | PROVED (Remark 4.1(ii)) | section 4 |
| C10 | `q_3, q_7` vanish at four points of `X_0` | MEASURED (mod `P`), explained by C8 | check 2 |
| C11 | Four-row cells can see `Z` | NOT CLAIMED either way; outside scope | Remark 4.1(iii) |

**Honest negatives.** (a) The proofs in EH section 3 were not replayed; the closure rests on
the published statements. (b) The Ballico addendum was not read. (c) No `rho_Z`, no
`m_det`, no `m_pad`, no `r`, no gap: the outcome is purely a closure. (d) Check 2's zeros
are consistent with, not evidence for, Theorem 4.1.

**Decision.** *Rigorous closure theorem for this route.* The identically singular locus
`Z` was excluded for the **wrong reason** in the B15-12 note (H-EH is false, and the
linear-kernel argument cannot be completed), but the **exclusion itself is correct**:
Theorem 4.1 shows every five-row full-`H` function vanishes on `Z`, so `Z` can never
supply a five-row determinant constraint, in five or more variables. Nothing on `Z` can be
"certified nonzero in a named full-`H` cell" with five rows; the route is closed, not
reopened.

**Exact next missing lemma (the only residual).** *Independence from later literature:*
confirm that Ballico (1995) and any addendum to Atkinson (1983) leave EH Theorems 1.1-1.2
and Corollaries 1.3-1.4 unchanged for `4 x 4` matrices. Inputs: those two texts. Expected
output: one sentence each, with page references. Falsification: a corrected list of
rank-3 primitive or imprimitive `4 x 4` spaces containing a `G`-semistable 5-dimensional
member with no column-only (or row-only) element, which would break Case 3 of
Theorem 4.1. Independently of the literature, a self-contained proof of Lemma 3.3 for
`4 x 4` matrices (rank-3 spaces with no shrunk subspace are contained in `Mt` or `Mt^T`)
would remove C1 and C3 from the dependency list entirely; it is a finite linear-algebra
statement and is the natural target if the closure is to be made literature-free.

Status: **COMPLETE - closure theorem delivered; H-EH refuted; exclusion of `Z` upheld by a
different proof; one residual literature dependence recorded.**
