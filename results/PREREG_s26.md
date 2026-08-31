# PRE-REGISTRATION — the `a = 2` lemma and the first live cells (session 26)

Committed **before any computation is run in this session**. Branch
`s26-tworank`, cloned fresh from public `origin/main`.

**Tip at clone time: `3dfd524`.** This is *not* the `a3df8ba` the brief names,
but it is **not a rollback alarm**: `3dfd524` is one commit *above* `a3df8ba`
("Correct the expected tip in both briefs, and point them at the screen",
by swsethuraman, 2026-08-31 13:24), and `a3df8ba`, `c9240f3`, `ad9502f` are all
present in its ancestry in the stated order. The brief in the repo
(`docs/s26_tworank.md`) already carries the corrected text. Branched from
`3dfd524`.

Date: 2026-08-31.

---

## 1. What was derived by hand before this commit

No routine has been written and nothing has been evaluated. The following is a
pencil argument, and it is logged here as the reason for the predictions
below — not as a result.

### 1.1 The rank lemma (the brief's generalisation), and a form of it with no
### dualisation in it

Let `M_lam` be the `lam`-isotypic component of `C[W]_delta`, `W = Sym^3 C^9`,
`M_lam = S_lam (x) C^a`. The ideal `I` of `closure(G.x)` is a `G`-submodule, so
`I ∩ M_lam = S_lam (x) U`. Let `h_1..h_a` be a basis of the space of
**highest-weight vectors of weight `lam`** in `C[W]_delta`; under
`M_lam = S_lam (x) C^a` these are `v_hw (x) e_k`. Then for `u in C^a`,

    S_lam (x) u  ⊆ I   <=>   v_hw (x) u = sum_k u_k h_k  vanishes on the orbit,

because `v_hw (x) u` generates `S_lam (x) u` as a `G`-module and `I` is
`G`-stable. Hence

    mult_lam C[closure]_delta  =  a  −  dim { u : sum_k u_k h_k vanishes on G.x }.

This is the brief's lemma, stated so that **no `S_lam` versus `S_lam^*`
question arises anywhere**: the `h_k` are explicit polynomials in the
coefficient coordinates of `W`, their torus weight is read off directly, and
they are evaluated at explicit points of the orbit. The dual form
`mult = dim span{phi_k}` is the same statement transposed; the practical
matrix `[h_k(g_j.x)]` computes a lower bound for every finite set of `g_j`,
with equality for generic `g_j`.

### 1.2 The short-weight reduction — this is what makes the cells computable

`C[W]_delta` is spanned by monomials in the coefficient functionals `c_alpha`
(`alpha` a degree-3 exponent vector on the 9 matrix coordinates), and the
weight of such a monomial is the sum of its `alpha`s, which has **non-negative
entries**. So a weight vector of weight `(lam_1,...,lam_r,0,...,0)` can only
involve `c_alpha` with `alpha` supported on the first `r` coordinates.
Therefore

    h(F)  depends only on  F restricted to  L = span(e_1,...,e_r),

and for `F = g.det_3` that restriction is

    F|_L (s_1,...,s_r)  =  det( s_1 A_1 + ... + s_r A_r ),   A_i = g^{-1} e_i,

with `A_1..A_r` an arbitrary linearly independent `r`-tuple of `3x3` matrices.
**So the whole question, for a weight of length `r`, is whether a nonzero
polynomial on `Sym^3 C^r` can vanish on the set of `r`-ary cubics of the form
`det(sum s_i A_i)`** — i.e. whether the determinantal `r`-ary cubics are
Zariski-dense.

### 1.3 Dimension count for density

`(A_1..A_r) -> det(sum s_i A_i)` has source `9r` and is invariant under
`(P,Q) . A_i = P A_i Q` with `det P det Q = 1`; that group has dimension 17 and
its scalar subgroup `(mu I, mu^{-1} I)` acts trivially, so the **effective**
group has dimension **16**. Generic stabilisers are trivial (a `P` commuting
with three generic matrices is scalar), so the image has dimension at most
`9r − 16`, against a target `Sym^3 C^r` of dimension `C(r+2,3)`:

| r | source `9r` | `9r − 16` | target | dense possible? |
|---|---|---|---|---|
| 2 | 18 | 2 (but target is 4 — see below) | 4 | yes, by an exact argument |
| 3 | 27 | 11 | 10 | yes |
| 4 | 36 | 20 | 20 | yes, exactly |
| 5 | 45 | 29 | 35 | **no** |

(At `r = 2` the effective group cannot act with 16-dimensional orbits on an
18-dimensional source with 4-dimensional image; the bound `9r−16` is not the
binding one there and the exact argument below settles it.)

- **`r = 2`: exact, not a count.** Every binary cubic over `C` splits into
  three linear forms, `prod_i (alpha_i s + beta_i t) = det(s D_alpha + t D_beta)`
  with `D` diagonal. So the determinantal binary cubics are **all** of them.
- **`r = 3`: classical.** Every plane cubic curve has a `3x3` linear
  determinantal representation (Dickson; for smooth cubics a 1-parameter
  family, which is exactly the `27 − 10 = 17 > 16` slack above).
- **`r = 4`: classical.** Every smooth cubic surface is determinantal — 72
  inequivalent representations, a finite fibre, matching `36 − 16 = 20`
  exactly.
- **`r = 5`: the count forbids it.** `29 < 35`.

### 1.4 The consequence

> **Predicted theorem.** For every `lam` with `ell(lam) <= 4` and every
> `delta`, no nonzero highest-weight vector of weight `lam` in `C[W]_delta`
> lies in `I(closure(GL_9 . det_3))`; hence
>
>     mult_lam C[closure(det_3)]_delta  =  a(lam, delta),
>     def_det(lam, delta)               =  m_det(lam) − a(lam, delta).
>
> The argument stops at `ell = 5`, so `ell(lam) = 5` is the first length at
> which the ideal can bite.

---

## 2. Predictions, with falsifiers

**Q1 — `mult_det` at the two two-row cells.**
**`mult_det((12,6), 6) = 2` and `mult_det((15,6), 7) = 2`.** Both fill the
room. Reasoning: §1.2 + §1.3 `r = 2`, which is exact — the evaluation map is
*onto* binary cubics, so no nonzero polynomial in the binary coefficients can
vanish on the orbit, whatever the weight.
*Falsifier F1: rank `< 2` at either cell, on any set of evaluation points.*

**Q2 — `def_det` at those cells.**
`m_det = 2` at both (the brief's table; to be independently recomputed), so
**`def_det = 0` at both. I do NOT expect a nonzero deficit here.** The two-row
cells cannot produce the "first genuine full deficit" of kill criterion 3.
*Falsifier F2: `m_det != 2` at either cell on my own recomputation, or
`def_det != 0`.*

**Q3 — how many random points the rank needs.**
`a` points suffice generically, so **2** at the two-row cells and 2–3 at the
three-row cells. I will use at least 8 and report the rank as a function of the
number of points.
*What would show the bound is not tight: the rank still rising when the
`(k+1)`-st point is added for some `k >= a`. I predict it does not — the rank
is `a` already at `k = a` for random integer points.*

**Q4 — the whole table.** With `a` and `m_det` as in the brief:

| lam | delta | a | m_det | predicted mult_det | predicted def_det |
|---|---|---|---|---|---|
| (12,6) | 6 | 2 | 2 | **2** | **0** |
| (15,6) | 7 | 2 | 2 | **2** | **0** |
| (9,4,2) | 5 | 2 | 3 | **2** | **1** |
| (12,4,2) | 6 | 2 | 3 | **2** | **1** |
| (13,6,2) | 7 | 3 | 4 | **3** | **1** |

*Falsifier F4: any cell where `mult_det < a`.*

**Q5 — the sharpest falsifier of the predicted theorem, and it is cheap.**
`mult <= min(m_det, a)` always. If `mult = a` whenever `ell(lam) <= 4`, then

    a(lam, delta)  <=  m_det(lam)   for every lam with ell(lam) <= 4.

That is a statement about a plethysm and a symmetric Kronecker coefficient with
no geometry in it, and it can be swept over thousands of weights.
*Falsifier F5: a single `lam` with `ell(lam) <= 4` and `a(lam,delta) >
m_det(lam)`. That would refute §1.4 outright, and I would stop and report it.*
I note in advance that the brief's own table has `a = m_det = 2` at both
two-row cells — the bound is **tight** there, which is a nontrivial prior check
that already passes.

**Q6 — the permanent, as calibration only.**
For `ell(lam) <= 2` the same exactness holds (`per` and `det` agree on diagonal
matrices, and every binary cubic splits), so **`mult_per = a` at both two-row
cells**. For `ell(lam) = 3` I predict the permanental map
`(A,B,C) -> per(sA+tB+uC)` is also dominant (Jacobian rank 10), hence
`mult_per = a` at the three-row cells too. I will test the Jacobian rank rather
than assume it.
*Falsifier F6: Jacobian rank `< 10` for the permanental map at a random point.*
**As the brief instructs: unpadded `per_3` is outside `closure(det_3)` for
dimension reasons (77 > 65), so nothing here is a GCT measurement.**

**Q7 — the global consistency check (predicted, to be run).**
If `mult = min(m_det, a)` at every weight, the published determinant
total-deficit sequence must satisfy

    total_def(delta)  =  sum_lam ( m_det(lam) − min(m_det(lam), a(lam,delta)) ).

At `delta = 2,3,4` the brief's own numbers already force this: `3−2 = 1`,
`11−5 = 6`, `43−12 = 31`, matching `1, 6, 31`. **I predict it continues to
match `141, 618, 2488` at `delta = 5,6,7`.**
*Falsifier F7: a mismatch. A mismatch would be a real finding, not a bug — it
would locate a weight where the ideal bites, necessarily of length `>= 5`, and
would be the first such weight known.*

**Q8 — where the argument stops.** `ell(lam) = 5` is the first length at which
the ideal can contain a highest-weight vector, by the `29 < 35` count.
*Falsifier F8: Jacobian rank of the `r = 5` determinantal map equal to 35 at a
random point (which would extend the theorem), or rank `< 20` at `r = 4`
(which would shrink it to `ell <= 3`).*

---

## 3. Method, fixed in advance

- **Independent rederivation first.** My own partition/character/plethysm and
  symmetric-Kronecker routines, written before `scripts/ambient_screen.py` is
  called, then cross-checked against it. A disagreement is reported before
  anything else proceeds.
- **Every number twice.** `a` by two routes (symmetric-function plethysm; and
  the dimension of the explicitly constructed highest-weight-vector space).
  `m_det` by two routes (symmetric Kronecker with the transpose correction; and
  the screen). Ranks over `Q` with exact integers *and* over a large prime.
- **Exact arithmetic only.** No floating point anywhere.
- The calibration required by kill criterion 2: at every `delta <= 4` weight
  the ideal is known to be zero (the paper's `1, 6, 31` row), so the rank must
  equal `a` at all of them. That is run before any new cell is measured.

## 4. What is NOT claimed here

Nothing about `n = 4`, nothing about padding, nothing about the World-A or
World-B conductor work. No paper edit is contemplated unless Q1–Q5 all resolve
as predicted, and any such edit will be flagged for the integrator.
