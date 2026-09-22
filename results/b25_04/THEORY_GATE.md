# B25-04 theory gate — written before any code or pilot

Written by 2026-09-21T03:43:24Z (first recorded UTC in session 03:38:39Z; gate budget 45 min). UNCOMMITTED.

Project variables throughout: form degree `n`, equation degree `d`, variable count `r`.
BDI's `Sym^{n_B} Sym^{d_B} C^m` is our `Sym^d(Sym^n C^r)`: `n_B = d`, `d_B = n`, `m = r`.
A tableau `T̂` has shape `λ ⊢ nd`, `ℓ(λ) ≤ r`, content `d × n` (entries `1..d`, each `n` times);
`G_T̂` has vertex set `{1..d}`, edge `{a,b}` iff `a,b` share a column (BDI §7, read at source).
Tail `t = |λ̄| = nd − λ_1`.

## The paragraph

**Candidate no-go class.** Let `F_{<k}` be the set of single-tableau functions `f_T̂` whose graph
`G_T̂` has every connected component on fewer than `k` vertices. This is the natural way to build
"large tail, small treewidth": concatenate the columns of many small tableaux on disjoint entry
sets; `τ(G_T̂) ≤ k − 2`, while the tail is additive and unbounded. **Proof idea.** From BDI eq.
(5.2), for `p = Σ_{i≤R} ℓ_i^{n}` one has `f_T̂(p) = Σ_{φ:[d]→[R]} Π_c det_c(φ)`, where each column
factor depends only on `φ` restricted to that column's entries; a column is a clique, so it lies in
one component; hence the sum factorises, `f_T̂ = Π_C f_{T̂_C}` over the components `C`, where
`T̂_C` is the column-tableau of the columns with entries in `C` (itself a BDI tableau of degree
`|C|` after sorting columns). An isolated vertex contributes `Σ_i (ℓ_i)_1^n = c_{ne_1}`, so this is
Theorem 1's factor seen at the level of fillings. Every `p` has a finite Waring decomposition, so
the identity is an identity of polynomials. Then: `I(D_r^{det_n})` prime and `f_T̂ ∈ I` give some
`f_{T̂_C} ∈ I`; `f_T̂|_{P_r} ≠ 0` gives a point of `P_r` where **every** factor is nonzero (no
irreducibility of `P_r` needed). So `f_{T̂_C}` is separating of degree `|C|`, hence `|C| ≥ D*`, and
by Theorem 1 applied to `f_{T̂_C}` its own tail is `≥ D*`. **Conclusion: no member of `F_{<D*}` is
separating; unconditionally (floor `D* ≥ 8`), no member of `F_{≤7}` is.** **Objections
discharged.** *Nonzero:* `F_{<k}` has nonzero members of every tail — the one semistandard tableau
of shape `(2n−2, 2)`, content `2 × n` (any `n ≥ 2`; row 2 is forced to be `2 2`) spans
`HWV_{(2n−2,2)}(Sym^2 Sym^n)` by BDI (5.6), which is 1-dimensional by the classical
`Sym^2 Sym^n = ⊕_{j even} S_{(2n−j, j)}`, so it is nonzero; and powers/products of nonzero polynomials are nonzero (domain).
*Correct graph:* vertices are entries, edges from the filling (BDI §7 quoted). *Legal weights:*
`λ` a partition of `nd` with `≤ r` rows; column concatenation of disjoint-entry tableaux, columns
sorted by length, is a partition shape. *Small width:* `τ ≤ k − 2`; `w ≤ W(n,r) := max_k
min(C(k+r−1,k), C(n−k+r−1,n−k))` by BDI Prop. 6.8, constant at fixed `(n,r)`. *Independent
functions:* the no-go is about **single** tableau functions; it does **not** pass to linear
combinations (a sum of products can lie in a prime ideal with no factor in it), so the span question
survives and is priced, not closed. *Tail theorem:* consistent — `f_{T̂_C}` has tail `t_C ≥ D*`
and `t ≥ t_C`; nothing here claims large tail forces large treewidth, and connected components of
bounded treewidth (paths, cycles, trees of cliques) are **not** excluded.

**Outcome targeted: (2)**, no-go for the precisely defined family `F_{<D*}`, with the surviving
corner (connected small-treewidth tableaux; spans) priced as the reopening condition.

**Pilot plan.** One optional wrapped control (not a proof): exact-integer evaluation of (5.2) at
random Waring points for (a) one disconnected tableau vs the product of its components, (b) the
isolated-vertex factor vs `c_{ne_1}`, (c) nonvanishing of the `(8,2)`, `n = 5` tableau function.
Priced < 5 s, < 100 MiB. Preregistered separately before writing it.
