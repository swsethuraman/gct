# The Pieri transport step, with explicit maps on multiplicity spaces

Session 49 (brief §2.4).  This re-proves Proposition 8 of
`docs/transfer_lemma.md` — the statement that the permanent can lower a
reducible-locus multiplicity only through a Pieri predecessor lying in the
ideal of `D_r^{per_3}` — with the maps written out on the multiplicity spaces
themselves rather than by a dimension count.  The statement is unchanged; the
write-up is new because an external audit read the old one as needing a
surjectivity that is neither true in general nor used.  **The direction the
programme uses is the easy one: an injection, giving an upper bound on the
erasure.  No surjectivity is claimed anywhere, and none is needed.**

## 1. Setting

`V = C^r`, `W = Sym^4 V^*` (quartics in `s_1..s_r`), `G = GL(V)` acting on
`V^*`, `Sym^3 V^*`, `W` by substitution and on functions by
`(g·h)(F) = h(g^{-1}·F)`.  Multiplication

    μ : V^* × Sym^3 V^*  →  W,      μ(l, c) = l·c

is bilinear and `G`-equivariant.  `R_r = μ(V^* × Sym^3 V^*) = {l·c}` is closed
(image of a proper map on the projectivisations, plus `0`), and
`P_r = closure μ(V^* × D_r^{per_3})` with `D_r^{per_3} = closure{per_3(A(s))}
⊆ Sym^3 V^*`.  So `P_r ⊆ R_r`, with equality iff `D_r^{per_3} = Sym^3 V^*`
(washout, `r ≤ 5`).

Coordinate rings are `C[X] = Sym(X^*)`; degree `δ` parts are written
`C[X]_δ`.  For a `G`-module `M` (polynomial, locally finite) and a weight `λ`,
the **multiplicity space** is the highest-weight space

    M^{hw}_λ  =  { v ∈ M_λ : E_{i,i+1} v = 0 for i = 1..r−1 },      dim M^{hw}_λ = mult_λ(M),

and a `G`-equivariant linear map `φ : M → N` sends `M^{hw}_λ` into `N^{hw}_λ`
(it preserves weights and commutes with the `E_{i,i+1}`).  The programme's
quantities at a cell `(λ, δ)` are

    a = mult_λ C[W]_δ,   i_X = dim (I(X)_δ)^{hw}_λ,   mult_X = a − i_X,

for `X = R_r, P_r, D_r^{det_4}`; write `U_R = (I(R_r)_δ)^{hw}_λ` and
`U_P = (I(P_r)_δ)^{hw}_λ`.  Since `P_r ⊆ R_r`, `I(R_r) ⊆ I(P_r)` and
`U_R ⊆ U_P ⊆ (C[W]_δ)^{hw}_λ`, whence

    mult_red − mult_pad  =  i_pad − i_red  =  dim (U_P / U_R).                                (1)

## 2. The pullback, written out

Because `μ` is bilinear, `μ^* : C[W] → C[V^* × Sym^3 V^*] = C[V^*] ⊗ C[Sym^3 V^*]`
sends `C[W]_δ` into the bidegree-`(δ, δ)` part

    C[V^*]_δ ⊗ C[Sym^3 V^*]_δ  =  Sym^δ V ⊗ Sym^δ (Sym^3 V) .

In coordinates: with `c_α(F) = [s^α]F` on `W`, `l_i = [s_i] l` on `V^*` and
`c_β(c) = [s^β] c` on `Sym^3 V^*`,

    μ^* c_α  =  Σ_{i : α_i ≥ 1}  l_i · c_{α − e_i} ,                                            (2)

and `μ^*` of a monomial `c_{α^1} ⋯ c_{α^δ}` is the product of the `δ` bilinear
forms (2) — explicit, of bidegree `(δ, δ)`, and computable term by term (this is
what the verifier's `star_support` check is a shadow of).  `μ^*` is
`G`-equivariant, so it restricts to a map of multiplicity spaces

    μ^*_λ : (C[W]_δ)^{hw}_λ  →  (Sym^δ V ⊗ Sym^δ Sym^3 V)^{hw}_λ .

## 3. The two kernels

**Lemma 1.**  `ker(μ^* on C[W]_δ) = I(R_r)_δ`.

*Proof.*  `h ∘ μ = 0` iff `h` vanishes on the image `μ(V^* × Sym^3 V^*) = R_r`.  ∎

**Lemma 2.**  For `h ∈ C[W]_δ`: `h ∈ I(P_r)` iff `μ^* h ∈ C[V^*]_δ ⊗ I(D_r^{per_3})_δ`.

*Proof.*  `h` vanishes on `P_r` iff it vanishes on the dense subset
`μ(V^* × D_r^{per_3})`, iff `μ^* h` vanishes on `V^* × D_r^{per_3}`.  The ideal
of a product with an affine space is `I(V^* × Y) = C[V^*] ⊗ I(Y)`: expand
`μ^* h = Σ_k m_k ⊗ g_k` with the `m_k ∈ C[V^*]_δ` linearly independent; vanishing
at `(l, c)` for every `l` forces every `g_k(c) = 0`, i.e. `g_k ∈ I(Y)`, and the
converse is clear.  With `Y = D_r^{per_3}` and bidegree `(δ, δ)` this is the
claim.  ∎

## 4. The theorem, as maps

**Theorem 3 (Pieri transport).**  `μ^*_λ` restricted to `U_P` has kernel
exactly `U_R` and lands in `(Sym^δ V ⊗ I(D_r^{per_3})_δ)^{hw}_λ`; hence it
induces an **injection** of multiplicity spaces

    ῡ : U_P / U_R  ↪  ( Sym^δ V ⊗ I(D_r^{per_3})_δ )^{hw}_λ ,                                    (3)

and therefore

    mult_red(λ, δ) − mult_pad(λ, δ)  =  dim(U_P/U_R)
                                     ≤  mult_λ( Sym^δ V ⊗ I(D_r^{per_3})_δ )
                                     =  Σ_{μ ⊢ 3δ, λ/μ a horizontal δ-strip}  mult_μ( I(D_r^{per_3})_δ ) .   (4)

*Proof.*  Lemma 2 gives the target; Lemma 1 gives the kernel, since
`U_P ∩ ker μ^* = U_P ∩ (I(R_r)_δ)^{hw}_λ = U_R`; equivariance keeps the map
inside highest-weight spaces of weight `λ`, so (3) is an injection of
multiplicity spaces and the dimension inequality in (4) follows.  The last
equality is Pieri's rule: `Sym^δ V ⊗ S_μ V ≅ ⊕_λ S_λ V` over the `λ ⊇ μ` with
`λ/μ` a horizontal strip of `δ` boxes, applied to the decomposition
`I(D_r^{per_3})_δ ≅ ⊕_μ S_μ^{⊕ mult_μ}`.  ∎

**Corollary 4.**
1. If `I(D_r^{per_3})_δ = 0` then `U_P = U_R` and `mult_pad = mult_red` at every
   weight `λ` of degree `δ`.
2. If `mult_pad(λ, δ) < mult_red(λ, δ)` then some `μ` with `λ/μ` a horizontal
   `δ`-strip has `S_μ ⊆ I(D_r^{per_3})_δ`; and the erasure at `(λ, δ)` is at most
   the sum in (4).
3. Explicitly: a vector `v ∈ U_P ∖ U_R` is a highest-weight vector of
   `I(P_r)_δ` not in `I(R_r)_δ`, and `μ^* v ≠ 0` is an explicit highest-weight
   vector of weight `λ` in `Sym^δ V ⊗ I(D_r^{per_3})_δ`, computable from (2).
   Conversely nothing is asserted about which elements of the target arise
   this way.

## 5. Direction of use, stated plainly

The programme uses (4) in one direction only: **from the pad side to the
reducible side**, to bound the erasure `mult_red − mult_pad` from above and,
when the right side is zero, to *transfer* `mult_red` to `mult_pad` exactly
(Corollary 4(1); this is what makes `mult_pad = mult_red` a theorem at every
weight of degree `8` for `r = 6`, `I(D_6^{per_3})_8 = 0` having been measured in
session 47).  That needs the injection (3) and nothing more.

The external audit read the step as requiring `ῡ` (or `μ^*_λ`) to be
**surjective** onto the λ-isotypic part of the target.  It does not.  A
surjectivity statement would be needed only for the converse of Corollary
4(2) — to conclude from `S_μ ⊆ I(D_r^{per_3})_δ` that the permanent *does*
erase at some `λ ⊇ μ` — and the programme never draws that conclusion: an
erasure is only ever established by evaluating at true padded-permanent
points (the pipeline evaluates at `x_0(s)·per_3(X(s))`, never at `l·(random
cubic)`; `docs/transfer_lemma.md` §3).  Equally, `μ^*` on all of `C[W]_δ` is
not surjective onto `Sym^δ V ⊗ Sym^δ Sym^3 V` — its image is the coordinate ring
`C[R_r]_δ` of the non-normal `R_r` inside its normalisation, which is
exactly the gap `h_pad − mult_red` of Corollary B2 in `docs/reducible_engine.md`
— and that is no obstacle either, for the same reason.

## 6. What is proved here, and what was already on record

Everything above is proved; nothing is measured.  Theorem 3 is Proposition 8
of `docs/transfer_lemma.md` restated with the maps explicit; Corollary 4(1),(2)
are its two items; Corollary 4(3) and §5 are the additions.  The paper-2
statement `prop:pieri` (`I(P_6)_δ = I(R_6)_δ` for `δ ≤ 5`, measured at `6`) is
Corollary 4(1) together with the free fact that `I(D_6^{per_3})_δ = 0` for
`δ ≤ 5` (every constituent of `Sym^δ(Sym^3 C^6)` has at most `δ` rows, and the
ideal lives at length exactly 6) — again an injection, not a surjection.
