# B18-12 note — Can the determinant coefficient algebra give a sharper cell bound than the stabilizer space?

Slot 12, theory-first note, 2026-09-16. Worktree `work/batch15_workers/B15-12`
(starting commit recorded in `docs/b18_12_ledger.md`: `761e0e7e…`, tree `67f8d126…`).
Written incrementally. One bounded exact check was run (§8); its receipt is at the end.

## 0. Verdict in plain terms

**No, not as a cheaper computation; yes, as one new arc-free constraint whose worth in
five-row cells is untested.** Precisely:

1. The determinant coefficient algebra `A` *is* the coordinate ring of the determinant
   closure, so `dim A_{d,lambda}` is `m_det` itself. Any bound `B < a` on it is the same
   thing as `a - B` independent determinant equations in the cell. There is no algebraic
   reformulation that makes that free. (§2)
2. What the algebra viewpoint does give is an exact description of the *target*:
   `A` consists of the functions on the invariant-theory quotient `Y` that are constant
   on the fibres of `Y -> D45`. Every cheap upper bound on `m_det` is a subspace of the
   stabilizer space provably containing `A`, and this is the largest such subspace that
   uses only "A is pulled back from `D45`". (§3)
3. The part of that constraint living over `F = 0` (semistable tuples with identically
   singular pencil, the locus `Z`) is **nonempty** (certified, §4 and §8) but contributes
   **nothing in any cell with five or more rows**: five-row functions vanish on tuples
   whose five matrices are dependent, and the only primitive singular spaces of `4x4`
   matrices with a linear kernel map have dimension at most four (proved, §4); the
   degree `>= 2` case rests on a literature classification that must be verified (flagged).
4. The part living over interior points is real and explicit: **block-triangular
   fibres**. Every tuple `[[M1, N],[0, M2]]` has the same pencil determinant as
   `[[M1, 0],[0, M2]]`, so every element of `A` is independent of `N`, while a general
   stabilizer-invariant is not (certified at degree 8, §8). This yields a provable
   inequality `m_det <= min(a, s - rank Delta_p)` with `Delta_p` an explicit linear map
   on the same `s`-dimensional full-stabilizer source the boundary method uses, tested
   at explicit integer points, with no arc and no limit. (§5, §6)
5. It is **not cheaper** than the boundary method: it needs evaluations of the
   full-`H` invariant source at points, which is exactly slot 02's priced barrier. It is a
   different criterion on the same source, so it can only be stacked with `b` after a
   joint rank check. Whether it ever beats `a` in a five-row cell is unknown; §9 names
   the smallest structural test and the check that kills it.

Nothing here produces an equation, a `B < a`, an `r`, or a gap.

## 1. Setup and conventions (ADOPTED unless marked)

- `V5 = C^5`, forms in `Sym^4(V5*)`, coordinate ring `Sym(Sym^4 V5)`, ordinary
  coefficients `c_alpha = [x^alpha] F`, weights `alpha >= 0`. Raising
  `E_ij c_alpha = (alpha_i + 1) c_(alpha + e_i - e_j)`; no factorial-normalised symbol
  is used anywhere in this note.
- `G = SL4 x SL4` acts on `(Mat4)^5` by `B_k -> P B_k Q`. `R = C[(Mat4)^5]^G`, graded by
  total entry degree; the coefficients `c_alpha(B) = [x^alpha] det(sum_k x_k B_k)` have
  entry degree 4, which is **normalised degree 1**. `R_{4d}` is the normalised-degree-`d`
  part. `GL5` acts on the index `k`, so each `R_{4d}` is a `GL5`-module.
- `phi : (Mat4)^5 -> W5 = Sym^4(V5*)`, `phi(B) = det(sum_k x_k B_k)`; `D45` is the Zariski
  closure of its image (dimension 50, accepted in batch 18, ledger §2a).
- `A = C[c_alpha] subset R` is the coefficient algebra; `A_d = phi^*(Sym^d(Sym^4 V5))`.
- `tau` is transposition `B_k -> B_k^T`; `det` is `tau`-invariant, so `A subset R^tau`.
- `Y = Spec R = (Mat4)^5 // G` and `pi : Y -> D45` the map induced by `phi`
  (`A = pi^* C[D45]`). Points of `Y` are closed `G`-orbits (polystable tuples).
- For `lambda |- 4d` with at most five rows: `a(d,lambda)`, `m_det(d,lambda)` as in the
  preamble. `g = g((d^4),(d^4),lambda)` is the **ordinary** rectangular Kronecker
  coefficient; `s` is the **symmetric** one (transposition included); `s <= g`.
- **Five-variable identification (ADOPTED, B17-03 Lemmas 1–2, accepted):** for
  `ell(lambda) <= 5`, `m_det(d,lambda)` computed on `X_det` in sixteen variables equals
  the `S_lambda(C^5)`-multiplicity of `C[D45]_d`.

**Claim 1.1 (PROVED, standard).** `A_d = C[D45]_d`, hence
`dim A_{d,lambda} = m_det(d,lambda)` for `ell(lambda) <= 5`, where `A_{d,lambda}` is
the highest-weight space of weight `lambda` in `A_d`.
*Proof.* `phi^*` is a surjection of `GL5`-modules `Sym^d(Sym^4 V5) -> A_d` with kernel
`I(D45)_d`, so `A_d = C[D45]_d`; multiplicities of highest-weight spaces agree with
multiplicities of isotypic components in characteristic zero.

**Claim 1.2 (PROVED, standard; = B17-02's `s` and v1's Claim 6.1 re-derived as closure
statements).** The `S_lambda(C^5)`-multiplicity of `R_{4d}` is `g`, and that of
`R^tau_{4d}` is `s`. Hence `m_det <= s <= g`, with no orbit-versus-closure caveat.
*Proof.* `C[(Mat4)^5]_{4d} = Sym^{4d}(C^4 (x) C^4 (x) C^5)^*`; by Cauchy and the
Kronecker decomposition its `G`-invariants are `⊕_lambda g((d^4),(d^4),lambda)
S_lambda(C^5)`, because `S_mu(C^4)^{SL4}` is nonzero only for the rectangle
`mu = (d^4)`. Transposition swaps the two `C^4` factors and acts on the
`g`-dimensional multiplicity space as the involution whose fixed subspace has
dimension `s` (the multiplicity of `S^lambda` in `Sym^2 S^{(d^4)}`).

## 2. Why "bound `dim A_{d,lambda}`" is not a cheaper problem (PROVED, elementary)

By Claim 1.1, an upper bound `B < a` on `dim A_{d,lambda}` is *literally* the statement
`dim I(D45)_{d,lambda} >= a - B`: the existence of `a - B` independent determinant
equations in the cell. Every such bound is therefore one of two kinds:

- **kernel side**: exhibit or count equations. The only structural handle the algebra
  adds here is that `A` is generated in degree 1, which gives the recursion
  `m_det(d,lambda) <= sum_{mu} m_det(d-1,mu)` over `mu` with `lambda/mu` a horizontal
  `4`-strip (Pieri, from the surjection `Sym^4 (x) A_{d-1} -> A_d`). Unwinding it,
  this is exactly `i_det(d,lambda) >= sum_mu i_det(d-1,mu) - sigma(d,lambda)` with
  `sigma = sum_mu a(d-1,mu) - a(d,lambda) >= 0` the Koszul slack: the count of
  equations obtained by multiplying lower-degree equations by the seventy coefficient
  variables, with worst-case overlap. **That is the programme's existing lift counting**
  (B16: "the eleven tail-19 equations lift by degree 27"), not a new bound. It also
  reproduces the accepted fact that lower-row types cannot arise by multiplication from
  higher-row generators (`ell(mu) <= ell(lambda)` along a strip).
- **target side**: exhibit a subspace of `R^tau_{4d,lambda}` (dimension `s`) provably
  containing `A_{d,lambda}`, and bound its dimension. The stabilizer bound `s` and the
  boundary method (`s - b`) are both of this kind. Everything new in this note is of
  this kind.

There is no third kind. So the honest answer to the assignment's first question is:
the cleanest finite map with image `A_{d,lambda}` is `phi^*` itself on the ambient
highest-weight space (the expensive pullback), and any cheaper description must be a
target-side containment. §3 gives the largest target-side containment that uses only
`A = pi^* C[D45]`.

## 3. The exact target: fibre-constancy (the one construction)

**Theorem 3.1 (PROVED).** Let `L subset (Mat4)^5` be closed, `G`-stable and
`GL5`-stable, and let `pi(L) subset D45` be the closure of `phi(L)`. Write
`S = R^tau_{4d,lambda}^{hw}` for the highest-weight space (dimension `s`), and let

- `rho_L` be the rank of the restriction map `S -> C[L]`, `f -> f|_L`;
- `u_L` be the `S_lambda(C^5)`-multiplicity of `C[pi(L)]_d`, the degree-`d` coordinate
  ring of `pi(L)` as a quotient of `Sym^d(Sym^4 V5)`.

Then

    m_det(d,lambda) <= min( a,  s - rho_L + u_L ).

Any certified **lower** bound on `rho_L` (a nonzero minor of `[f_j(B_i)]` at explicit
points `B_i` of `L`, exact or at one prime) and any certified **upper** bound on `u_L`
give a valid inequality. Both are the cheap directions.

*Proof.* `A_{d,lambda} subset S` (Claim 1.2). For `f in A_d`, `f = q ∘ phi` with
`q in Sym^d(Sym^4 V5)`, so `f|_L = (q|_{pi(L)}) ∘ phi`: the restriction of `A_d` to `L`
is `phi^* C[pi(L)]_d`, whose `lambda`-highest-weight space has dimension `u_L` (the
restriction map is `GL5`-equivariant, so highest-weight spaces map to highest-weight
spaces). Hence `dim (A_{d,lambda}|_L) <= u_L`, while
`dim (A_{d,lambda} ∩ ker(rho)) <= dim ker(rho) = s - rho_L`. Add. The clip by `a` is
`m_det <= a`. ∎

**What this is.** Functions in `A` are constant on the fibres of `pi : Y -> D45`.
Theorem 3.1 is the cell-wise, highest-weight form of that single fact, localised to a
locus `L`. Two special cases:

- `L = (Mat4)^5`: `rho_L = s`, `u_L = a`; the bound is `min(a, a) = a`. Trivial.
- `L = Z`, the semistable tuples with identically singular pencil (`pi(Z) = {0}`,
  `u_Z = 0` for `d >= 1`): `m_det <= s - rho_Z`. See §4.2.

**Answer to the assignment's third question (what proves a direction is outside `A`
and independent modulo `A`).** If `f_1, ..., f_p in S` have restrictions to `L` whose
images in `C[L] / phi^* C[pi(L)]` are linearly independent, then they are independent
modulo `A_{d,lambda}`: a relation `sum c_j f_j in A` would restrict to an element of
`phi^* C[pi(L)]`. Concretely: a `p x p` minor of `[f_j(B_i)]` that stays nonzero after
projecting away the `u_L`-dimensional subspace of values attainable by `phi^* C[pi(L)]`
certifies `p` directions outside `A` and independent modulo it. Being a higher-degree
generator of `R` proves nothing; only the restriction test does.

**Relation to the boundary method.** The boundary bound `s - b` is also target-side on
the same `S`, but its criterion is analytic (no pole along one arc to a boundary point of
`X_det`). Theorem 3.1's criterion is algebraic and interior (values at explicit
polystable tuples). Neither implies the other, so the two losses may **not** be added:
a combined bound requires the rank of the stacked conditions on the same columns, as
supplement04_08 already demands for any two forbidden projections.

## 4. Which loci carry content

### 4.1 Block-triangular fibres: vacuous (PROVED, and MEASURED as a control)

Tuples `[[M1, N],[0, M2]]` and `[[M1, 0],[0, M2]]` (block sizes `p + q = 4`) have the
same pencil determinant, so every element of `A` is independent of `N`. But so is every
element of `R`: the one-parameter subgroup `(diag(t I_p, I_q), diag(t^{-1} I_p, I_q))`
of `G` scales `N -> t N` and fixes the diagonal blocks, so the block-diagonal tuple lies
in the orbit closure of the block-triangular one and invariants cannot separate them.
The two tuples are the **same point of `Y`**. The bounded check (§8) confirms this at
degree 8 for `p = 1, 2`: the `tau`-symmetrised semi-invariant takes equal values. This
locus gives `rho_L` nothing beyond what block-diagonal tuples give. Recorded so that
nobody re-derives it as a mechanism.

### 4.2 The contracted locus `Z`: nonempty, but blind to five or more rows

**Claim 4.2.1 (CERTIFIED, §8).** `Z` is nonempty. Take a generic linear
`Lambda : Wedge^2 C^4 -> C^4` and `X_Lambda = { Lambda(x, ·) : x in C^4 } subset Mat4`.
Each `Lambda(x, ·)` kills `x`, so every element of `X_Lambda` is singular and
`det(sum_k x_k B_k) ≡ 0` for any tuple in `X_Lambda` (checked symbolically). A random
integer `Lambda` and the tuple `(Lambda(e_1,·), ..., Lambda(e_4,·), Lambda(e_1+...+e_4,·))`
has the degree-8 semi-invariant `det(sum_k M_k (x) B_k) = 184691212016 != 0` for random
integer `2 x 2` matrices `M_k` (and `tau`-symmetrised value `303165134600`). By King's
criterion a nonzero semi-invariant certifies semistability, so this tuple represents a
point of `Z`. (The quiver-semi-invariant spanning theorem — Derksen–Weyman,
Schofield–Van den Bergh, Domokos–Zubkov — is used only to know that these determinants
are invariants; nonvanishing of one of them is what is certified.)

**Claim 4.2.2 (PROVED).** Let `ell(lambda) = 5`. Every `f` in the `S_lambda`-isotypic
component of `C[(Mat4)^5]` vanishes on every tuple whose five matrices are linearly
dependent. *Proof.* Every weight `nu` of `S_lambda(C^5)` has `nu_5 >= lambda_5 >= 1`
(a semistandard tableau of shape `lambda` with entries `<= 5` has `lambda_5` columns of
height 5, each containing a 5). So every weight vector has positive degree in `B_5` and
vanishes on `{B_5 = 0}`; the isotypic component is `GL5`-stable and the dependent locus is
`GL5 · {B_5 = 0}`. ∎

Hence `rho_Z` for a five-row `lambda` sees only points of `Z` whose five matrices span a
**five-dimensional singular subspace of `Mat4` with no compression subspace**.

**Claim 4.2.3 (PROVED).** If a singular subspace `X subset Mat4` of generic rank 3 has
kernel map of degree one (`x -> ker B_x` linear on `P(X)`, after removing common
factors), then `dim X <= 4`. *Proof.* Write `kappa : X -> C^4` linear with
`B_x kappa(x) = 0`. If `kappa` has a kernel `x_0 != 0`, then for `x = x' + t x_0`,
`B_{x'} kappa(x') + t B_{x_0} kappa(x') = 0` for all `x', t` forces `B_{x_0} kappa(x') = 0`
for all `x'`; if `kappa` is surjective this gives `B_{x_0} = 0`, contradicting
injectivity of `x -> B_x`; so `kappa` is injective and `dim X <= 4`. If `kappa` is not
surjective (image `K` of dimension `<= 3`), the same argument only gives
`B_x|_K = 0` for `x in ker kappa`, which is **not** by itself a compression statement;
that sub-case is left to the classification (H-EH below). ∎ (partial: surjective
`kappa` only)

**Hypothesis H-EH (NOT verified here; literature pointer).** Every singular subspace of
`Mat4` of dimension `>= 5` is a compression space (equivalently: primitive spaces of
`4 x 4` matrices of rank `<= 3` have dimension `<= 4`). Eisenbud–Harris, *Vector spaces
of matrices of low rank*, Adv. Math. 70 (1988), Theorem 1.1, classifies spaces of rank
`<= 3`; the claim should be read off from the primary source, with the exact statement
and the rank-`<= 2` case (3x3 skew) checked. The kernel-degree `>= 2` cases are what
Claim 4.2.3 leaves open.

**Consequence (PROVED conditional on H-EH).** `rho_Z = 0` for every `lambda` with
`ell(lambda) >= 5`, in five variables and, by the same weight argument with `m`
matrices, in every `m`-variable model. **The contracted locus contributes nothing in any
cell the programme can use.** The same dependent-tuple argument shows that the
degree-8 semistable cone tuple `(E_11, E_22, E_33, E_44, E_12)` of §8, although
independent and semistable, is the same point of `Y` as `(E_11, ..., E_44, 0)` (torus
limit), so cone fibres of that type are also blind to five rows.

### 4.3 The reducible block-diagonal loci: live

Let `L_(1,3)` be the closure of the `G x GL5`-saturation of block-diagonal tuples
`(a_k ⊕ M_k)` with `a_k in C` and `M_k in Mat3`, and `L_(2,2)` likewise with
`2 + 2` blocks. Then:

- `pi(L_(1,3)) = { l · C : C a 3x3-determinantal cubic }` and
  `pi(L_(2,2)) = { q_1 q_2 : q_i quadrics of rank <= 4 }`. Both lie inside the reducible
  locus, and **`u_{L_(1,3)} <= U(d,lambda)`**, the accepted clipped five-variable
  product-map ceiling, because `{l · C_det} subset {l · C}` and `U` bounds the
  `S_lambda`-multiplicity of `C[{l·C}]_d` (B17-08, accepted; v1 Claim 6.2, accepted by
  slot 10 as far as written). In fact `u_{L_(1,3)}` is the multiplicity in the coordinate
  ring of a **33-dimensional** subvariety of the 39-dimensional `{l·C}`, so it can be
  strictly smaller than `U` in high degree.
- The points are polystable and independent for generic blocks, so five-row functions
  are not forced to vanish (Claim 4.2.2 does not apply). `rho_L` is a genuine unknown.
- For `(1,3)` blocks the partial transpose is `tau` itself; for `(2,2)` blocks the
  tuples `M_1 ⊕ M_2` and `M_1 ⊕ M_2^T` are `G`-inequivalent, `tau`-inequivalent, and
  have the same pencil determinant: an explicit interior pair of distinct points of `Y`
  with the same image, on which `A` must agree and `R^tau` need not.

**Dimension bookkeeping (MEASURED by counting, not a theorem about ranks).**
`dim L_(1,3) // G = 50 - 17 = 33 = dim pi(L_(1,3))` (`G`-orbits of generic block tuples
are 17-dimensional; `3x3` determinantal cubic threefolds form a 29-dimensional affine
family, i.e. the six-nodal cubics). So `L_(1,3)//G -> pi(L_(1,3))` is generically finite,
and `rho_L - u_L` in a cell measures **non-normality of the reducible determinantal
locus plus the degree of that map** — precisely the part of the deficit `s - m_det` that
lives over the reducible locus. Whether it is positive in any cell is what the pilot
asks.

## 5. Route from the construction to a determinant multiplicity upper bound

In one cell `(d, lambda)`, `ell(lambda) = 5`, in the conventions of §1:

1. Take the full-`H` (transposition included) highest-weight source of weight `lambda`,
   dimension `s`, as a list of evaluable functions on `5`-tuples of `4 x 4` matrices.
   This is slot 02's object; its construction is slot 02's priced barrier and is **not**
   made cheaper here.
2. Choose `L = L_(1,3)` (or `L_(2,2)`), and `N` random integer block-diagonal tuples
   `B_1, ..., B_N`. Compute `rank_p [f_j(B_i)]` at one prime. That is a certified lower
   bound `rho_0 <= rho_L` (`rank_p <= rank_Q <= rho_L`; the safe direction).
3. Take `u_0 = U(d,lambda) = min(a, T)` from the accepted symmetric-function
   computation, or the sharper `u_0 = mult_lambda C[{l·C_det}]_d` if certified.
4. Then **`m_det(d,lambda) <= B_L := min(a, s - rho_0 + u_0)`** is PROVED for that cell.

`B_L < a` iff `rho_0 - u_0 > s - a`. When `s = a` (the small-control regime) this needs
only `rho_0 > u_0`: the source must have more independent functions on the reducible
determinantal locus than the image of that locus can carry.

## 6. What a positive gap would additionally need

`r > B_L` with `r` an exact actual-padding rank floor in the same cell (five-variable
product map `(l, C) -> lC`, accepted dominance, exact minor; slot 04's remit). Since
`r <= U` and `u_0 <= U`, the inequality `r > s - rho_0 + u_0` can hold only if

    r - u_0 > s - rho_0,

i.e. **actual padding must realise strictly more independent `lambda`-coefficient
functions than the determinantal reducible locus `{l·C_det}` realises, by a margin
exceeding the source's blindness `s - rho_0` on that locus.** This is a coherent
same-cell statement: both sides are ranks of coefficient functions on reducible quartics
`l · C`, one with `C` general (padding, dense in cubics by B17-01), one with `C`
six-nodal determinantal. It is exactly where B17-01's separation lives, now as a
multiplicity comparison rather than a membership statement. Nothing in this note
supplies `r`.

## 7. Pilot: what was run, what is priced, the test cell, and the kill

### 7.1 Run here (MEASURED; one process, no BLAS, `timeout 60`; receipts in §8)

- `b18_12_fibre_check.py` (2.4 s): §4.1 vacuity confirmed at degree 8; §4.2.1 `Z != ∅`
  certified; the independent semistable cone tuple has degree-8 semi-invariant
  `-3724 != 0`.
- `b18_12_ambient_table.py` (under 60 s): `a(d,lambda)` for all five-row `lambda`, `d = 5, 6`,
  with the control `sum_lambda a · dim S_lambda = binom(69+d, d)` passing at both
  degrees. `d = 5`: exactly the 23 five-row cells, each `a = 1` — matching the
  assignment's count. `d = 6`: 105 five-row cells, total `a = 240`; the smallest `a >= 2`
  cells include `(8,4,4,4,4)` with `a = 2`, and the largest are `(10,7,4,2,1)`,
  `(11,6,4,2,1)` with `a = 7`.

### 7.2 The one bounded test (priced, not run)

**Test cell, chosen on structural grounds: `d = 6`, `lambda = (4^6)`, six rows.** It is
the only cell where the total deficit is known (`s = 10`, `a = 1`, `m_det <= 1`, so
`s - m_det >= 9`) **and** the boundary criterion is provably blind (`b = 0` by the
silence criterion `lambda_1 + lambda_2 + lambda_3 = 12 <= 2d = 12`). It therefore
discriminates between "the fibre criterion sees the deficit the arc cannot" and "the
deficit is unibranch non-normality that no target-side test sees". It is a diagnostic,
not a candidate: padding vanishes there.

Procedure (six-variable model, `m = 6` matrices, everything else as in §3):
take B19-01's ten source functions and its ambient vector `q`; evaluate the ten at
`N = 40` random integer block-diagonal `(1,3)` six-tuples and `40` `(2,2)` six-tuples;
`rho_0 = rank_p` at `p = 2^31 - 1`; `u_0 = 1` (the safe clip; `u_0 = 0` may **not** be
inferred from sampled zeros of `q` on `l · C_det`). Readout: `m_det <= 11 - rho_0`.

- `rho_0 >= 9`: the fibre criterion explains essentially the whole deficit in the cell
  where the arc saw nothing; that justifies pricing it in a five-row `a >= 2` cell.
- `rho_0 = 0` on both block types: the criterion is dead as an explanation here; stop.
- In between: report the number; do not extrapolate.

Price: given the B19-01 basis, `80` evaluations of ten degree-24 functions and one
`80 x 10` modular rank — seconds to minutes. Without a deliverable basis, the price is
slot 02's barrier and the test stops with that number. Stop condition: one prime, one
run, no re-sampling.

### 7.3 The first five-row candidate cell and its kill

If 7.2 reads `rho_0 >= 9`, the smallest five-row cell with room is **`d = 6`,
`lambda = (8,4,4,4,4)`, `a = 2`** (smallest `a >= 2` in the table, and the Pieri
extension of the excluded rectangle `(4^5)`, so one of its two ambient directions is
the product `c_{(4,0,0,0,0)} · (the (4^5) invariant)`, structurally the most "determinantal"
of the 105 cells). Required before anything else, in this order:

1. **Kill switch (cheap, standard):** the two ambient highest-weight vectors of
   `Sym^6(Sym^4 C^5)` of weight `(8,4,4,4,4)`, evaluated at a handful of random integer
   pencils `det(sum x_k B_k)`, rank 2 at one prime ⇒ `m_det = a = 2` ⇒ no upper bound
   below `a` exists by any method, and the cell is dead for a gap. This is one
   `b15_bound.py`-sized run.
2. `U(6,(8,4,4,4,4))`: if `0`, no padding rank can exist and the cell is dead
   regardless of `m_det`.
3. Only then `s`, the source, `rho_0`, and `B_L`.

I nominate this cell only as the next *structural* place to measure, not as a
candidate: no number in this note says it has `D > 0`.

## 8. Receipts

Both runs: one process, the worktree's own `.venv` Python 3.12.10 with sympy 1.14.0,
no BLAS, `timeout 60`, `ulimit -v 524288` requested (the shell may ignore it on this
platform; both runs used a few MB). No lease requested. No git command beyond
`git status --porcelain` (permitted by the preamble) and the two `rev-parse` calls
recorded in the ledger.

| File | SHA256 |
|---|---|
| `analysis/b18_12_fibre_check.py` | `5ac1a31f31184e063f1029f87abbc6336fb21a30f314b11da5d21ec92dafea6a` |
| `results/b18_12/fibre_check.out` | `d2d992d9eb25bf256b4a76da02f7579dfccc34a1c98a014323f9b3de0cbef279` |
| `analysis/b18_12_ambient_table.py` | `76e709ba9387d62c55f80a35e82ed31c239dbb689ecb5be69b57bd2cfda1a55b` |
| `results/b18_12/ambient_table.out` | `bec224ec65094a4f8b08966a96893574bcb6dfaa4117f35f2604faf9af163d4e` |

`fibre_check.out` (2.4 s wall):

```
X_Lambda_pencil_det_is_zero = True
X_Lambda_each_singular = True
X_Lambda_semi_invariant_deg8 = 184691212016
X_Lambda_tau_semi_invariant_deg8 = 303165134600
cone_tuple_pencil_det = x1*x2*x3*x4
cone_tuple_semi_invariant_deg8 = -3724
block_triangular p=1: A control equal = True; R^tau deg-8 value equal on and off the fibre (Delta = 0)
block_triangular p=2: A control equal = True; R^tau deg-8 value equal on and off the fibre (Delta = 0)
```

`ambient_table.out` (2.9 s wall): control sums `16108764 = binom(74,5)` and
`201359550 = binom(75,6)` both match; 23 five-row cells at `d = 5`, all `a = 1`;
105 five-row cells at `d = 6`, total `a = 240`. Random seed `20260916` for the
integer points; sympy exact integer determinants; nothing modular.

## 9. Labels, negatives, and the direct answers

**PROVED here:** Claims 1.1, 1.2 (standard); §2 (kernel/target dichotomy and the Pieri
recursion as lift counting); Theorem 3.1; §4.1 (block-triangular vacuity); Claim 4.2.2
(five-row functions vanish on dependent tuples); Claim 4.2.3 in the surjective-kernel
case. **CERTIFIED:** `Z != ∅` (§4.2.1), semistability of the cone tuple, and the
degree-8 vacuity, all by exact integer evaluation. **MEASURED:** the `a(d,lambda)` table
with its passing control. **ADOPTED:** conventions, B17-03 identification, B17-08's `U`,
the quiver semi-invariant description of `R`. **HYPOTHESIS:** H-EH (classification of
rank-`<= 3` spaces), needed only for "Z is blind to `>= 5` rows" beyond the linear-kernel
case. **NOT REACHED:** any `rho_L`, any `u_L` sharper than `U`, any `B_L`, any `r`, any
`s` at `d = 6`, any gap.

**Honest negatives.**

1. The coefficient algebra gives no cheaper computation of `m_det`: `dim A_{d,lambda}`
   *is* `m_det`, and every bound below `a` is a count of equations (§2).
2. The one genuinely new target-side constraint (Theorem 3.1) costs the same as the
   boundary method: evaluations of the full-`H` source. It changes the *criterion*, not
   the *price*.
3. The two loci one would try first are worthless for the programme's cells: block-
   triangular fibres are invisible to invariants (§4.1), and the contracted locus `Z`,
   though nonempty, is blind to every cell with five or more rows (§4.2, conditional on
   H-EH beyond the linear-kernel case).
4. What survives — the reducible block-diagonal loci — has an unknown rank `rho_L`. A
   dimension count (§4.3) says the quantity it measures is non-normality of `{l·C_det}`
   plus a finite degree; it does not say that number is positive in any cell.
5. The `(4^6)` diagnostic can end either way; the note does not predict it.

**Direct answers to the assignment.**

- *Cleanest finite map with image `A_{d,lambda}`:* `phi^*` on the ambient highest-weight
  space — the expensive pullback. Ordinary `g` counts `S_lambda` in `R_{4d}`;
  symmetric `s` counts it in `R^tau_{4d}`; `A subset R^tau`, so `s` is the right ceiling
  and `g` must never be used as `s`.
- *Filtration / multiplication / straightening / syzygy / quotient giving `B < a` without
  the pullback:* multiplication gives only lift counting (§2). The one quotient that
  works is restriction to a locus with a known image (Theorem 3.1): it trades the
  pullback for source evaluations plus a padding-type ceiling on the image.
- *What proves directions are outside `A` and independent modulo it:* a minor of source
  values on `L` that survives projection away from the `u_L`-dimensional image space
  (§3). Degree of a generator proves nothing.
- *Total deficit versus this test's rank:* `s - m_det >= rho_L - u_L` is the only
  relation; `rho_L - u_L` is not `b`, and the two may not be added without a joint rank.
- *Is this only a reformulation?* For the algebra itself, yes. For Theorem 3.1, no: it
  is a different necessary condition on the same source, arc-free, with the padding
  ceiling appearing on the determinant side for the first time. Its worth is one
  measurement away (§7.2).

**One next sufficient test and its price:** §7.2, the `(4^6)` fibre-rank diagnostic;
seconds to minutes given B19-01's basis, otherwise slot 02's barrier, and it stops there.
