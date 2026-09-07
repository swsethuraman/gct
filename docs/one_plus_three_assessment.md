# Integrator assessment — the `ℓ·det_3` route, and where its gate really is

On the external three-prong memo (D1 `1+3` degeneration, D2 direct
274-dimensional source, D3 bracket compression).  **D1 is right, and it is a
better idea than the stable-coordinates note I committed an hour earlier
(`docs/stable_coordinates.md`).**  Three of its claims are confirmed below
without any computation beyond arithmetic, one structural correction follows,
and the corrected ordering matters: **D1 is gated on D2, not parallel to it.**

## 1. Confirmed — the containment, and it needs no degeneration argument

A block-diagonal pencil `M(s) = diag(ℓ(s), A_3(s))` is an ordinary `4×4` pencil,
so `X_{1+3} = closure{ℓ·det_3(A)}` is not a *limit* of the determinant family —
it is a **subfamily of it**, and `X_{1+3} ⊆ D_9` holds on the nose.  Hence
`I(D_9) ⊆ I(X)`, `C[D_9] ↠ C[X]`, and

    mult_X(λ, 24) ≤ mult_det(λ, 24)          (brief_wording.md §7 functoriality)

so `mult_X ≥ 273` forces `mult_det ≥ 273`, and LMR's `≤ 273` closes it:
`i_det = 1`.  **The generic `det_4` block need never be constructed.**  This is
the cleanest formulation of the goal anyone has produced.

Dimensions, for the record (`dim D_r = 16r − 30`, which reproduces the banked
`dim D_5 = 50` exactly):

    dim X_{1+3} at r = 9  =  9 + (9·9 − 16) − 1  =  73
    dim D_9               =  16·9 − 30           =  114        73 ⊂ 114  ✓
    dim R_9               =  9 + C(11,3) − 1     =  173

## 2. Confirmed — the concision argument, and `1+3` is minimal

A form depending on at most `k` essential linear forms has every `S_λ` with
`ℓ(λ) > k` in its ideal, so the whole module is annihilated and `mult = 0`.
Counting the linear forms each block split can use:

| split | forms | at `ℓ(λ) = 9` |
|---|---|---|
| `x_1x_2x_3x_4` | 4 | blind |
| `det_2 · det_2` | 8 | blind |
| **`ℓ · det_3`** | **1 + 9 = 10** | **can see it** |

So `1+3` is exactly the first block split rich enough to see the LMR weight.
That is a real structural point and it is correct.

## 3. Confirmed — the shape twist

`(65,17,2⁷) − (2⁹) = (63,15)`, so

    S_{(65,17,2⁷)}(C⁹)  ≅  (det)² ⊗ S_{(63,15)}(C⁹)

by the standard `S_{λ+(k^n)}(C^n) = (det)^k ⊗ S_λ(C^n)`.  The LMR weight is a
**two-row shape twisted by `det²`**.  Correct, and it is the strongest argument
for D3 being worth scoping.

## 4. The correction — D1 is gated on D2

The memo presents three parallel prongs and recommends starting with D1.  **D1
cannot start.**

The `274 → 521` split `S_{λ,24}` is a map *out of* `M^{(4)}_λ`, and `M^{(4)}_λ`
is precisely the 274-dimensional space nobody can construct — it is the `n_χ`
wall by another name.  Writing the matrix of `S` requires a basis of its source.
So the order is:

    D2  (build M_λ at dimension 274, by branching)
      ⟶  D1  (the 274 × 521 split, then the 48 det_3 blocks)

D2 is not one of three options; **it is the enabling step for the other two**,
and the memo's own closing sentence — that the object is 274-dimensional and the
algorithm should know it — is the argument for putting it first.

## 5. Where D1's gate actually sits, and the cheap test that answers it

The memo's D1 asks whether rank 273 is "representation-theoretically plausible
before coding anything".  Here is the precise form of that question.

`X_{1+3} ⊆ R_9`, so `I(R_9) ⊆ I(X)` and **`i_red ≤ i_X`**.  The route needs
`i_X ≤ 1`.  Therefore:

> **Route D1 requires `i_red ≤ 1` at the LMR cell.**  If the *reducible* ideal
> carries two or more equations there, `i_X ≥ 2` and D1 is dead whatever the
> `det_3` blocks do.

And `mult_red` is computable by the **first stage alone**: the normalisation of
`C[R_r]` is `⊕_δ Sym^δ V ⊗ Sym^δ(Sym³V)`, the split `S_{λ,δ}` *is* the map into
it, and `C[R] ⊆` its normalisation, so

    mult_red(λ, 24)  =  rank S_{λ,24}          a 274 × 521 matrix

**No `det_3` blocks, no second stage.**  So the gate for the whole route is one
rank of a 274 × 521 matrix, and it is the first thing to compute once D2 lands:

    rank S ≤ 272   ⟹  i_red ≥ 2  ⟹  i_X ≥ 2  ⟹  **D1 is dead**
    rank S ≥ 273   ⟹  D1 is alive; the 48 det_3 blocks decide

It also produces `mult_red` at the LMR cell, which the record does not hold and
which is worth having on its own.

**One thing the length-5 record cannot tell us.**  `dim R_9 = 173 > 114 =
dim D_9`, so **`R_9 ⊄ D_9`** — the reducible variety is not inside the
determinant one at length 9, and `i_det` and `i_red` are therefore *not*
comparable there.  The length-5 intuition (`i_det ≤ i_red`, from cells where
containment holds) does not transfer, and `i_red` at LMR could be anything.
That is exactly why §5's rank is a gate and not a formality.

## 6. On my own note from an hour ago

`docs/stable_coordinates.md` proposes working in the Proposition S stable
picture, which shrinks the ambient from `3.10 × 10⁷` to `≈ 1.43 × 10⁶` — a
measured factor of 21.7.  **If D2 works, that note is subsumed**: D2 removes the
ambient entirely rather than shrinking it by twenty, and a construction that
scales with `a_λ = 274` does not care what carrier it would have sat in.

Keep two things from it regardless of D2's fate.  The **monotonicity argument**
(`i_det(24) ≤ i_det(∞)`, so a stable value of 1 settles the goal cell without
any rank at `δ = 24`) is independent of how `M_λ` is built and composes with any
of D1–D3.  And the **second ladder** — `det(A_1)` is a highest-weight vector of
weight `(4,0,…,0)` in the tail variables and a nonzerodivisor on `C[M_ℓ]`, so
`i_det` is monotone in the tail's first part — is banked structure that S1 can
use to widen the stable dead region.

## 7. Recommended order

1. **D2 first.**  Pre-register exactly as the memo says: build through
   `δ = 12, 14, 16, 18` on the wreath chain `S_4 ≀ S_1 ⊂ … ⊂ S_4 ≀ S_24` and
   record the **maximum live branching-state count**.  That number, not `n_χ`,
   is the one that decides everything downstream.  Hundreds or thousands:
   continue.  `10⁶` despite a multiplicity of 274: stop, and say so.
2. **Then D1's gate**: `rank S_{λ,24}` as a `274 × 521` matrix.  One number,
   and it either retires the route or opens it.
3. **D3 in parallel with either**, with the memo's own stopping rule — reproduce
   the `n = 3` one-dimensional kernel banked this morning at `(19,7,2⁵)`, or
   retire it. That control is now real and it costs nothing to demand.
