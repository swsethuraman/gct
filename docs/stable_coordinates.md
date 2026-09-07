# A change of coordinates that shrinks the LMR problem by a factor of twenty

Integrator note, written on instruction to stop validating the determinant
evaluator and look only for coordinates or algorithms that avoid the `n_χ` and
Foulkes-support walls.  Two walls stand (`docs/s63_integrator_note2.md` §4):

    n_χ wall            n_χ = 3.10 × 10⁷ at the goal cell; the raising-operator
                        build extrapolates to ~7 × 10⁹ nonzeros, ~570 GB
    support wall        |S| ≈ 10⁵ ⟹ 273·|S|² ≈ 10¹³

**Both are walls of the `δ`-graded picture.  Neither is intrinsic.**

## 1. The move

Work in the **stable picture** of Proposition S (session 57).  Dehomogenising at
`s_1` replaces

    Sym^δ(Sym^4 C^ℓ)  at  λ = (4δ − t, ρ)      by      Sym(Sym² ⊕ Sym³ ⊕ Sym⁴)(C^{ℓ−1})  at  ρ

and identifies stable `i_det` with the multiplicity of `S_ρ` in the ideal of
`M_ℓ`, the variety of characteristic polynomials of traceless `(ℓ−1)`-pencils of
`4×4` matrices.  For LMR: `ℓ = 9`, `ρ = (17, 2⁷)`, `|ρ| = 31`, eight variables,
generators the coefficients `e_2, e_3, e_4` of the pencil's characteristic
polynomial.

## 2. Why it settles the goal cell

The ladder theorem gives `i_det` **non-decreasing** in `δ` and constant for
`δ ≥ t`.  With `t = |ρ| = 31 > 24`:

    i_det(δ = 24)  ≤  i_det(δ = 31)  =  i_det(∞)  =  I(ρ)

and LMR supplies `i_det(24) ≥ 1`.  Therefore

> **`I(ρ) = 1`  ⟹  `i_det(24) = 1`.**

No rank at `δ = 24` is ever computed.  If `I(ρ) ≥ 2` the result is a range
rather than a value — still informative, and a stable obstruction in its own
right, which is S1's target.

**The same argument runs on the padded side, and gives the whole answer.**
`i_pad` is non-decreasing too, so `I_pad(ρ) = 0 ⟹ i_pad(24) = 0`, and with
`i_det(24) = 1` that is `D_LMR = 1`.  One caveat: session 57 proved the ladder
for `C[D_r]` and `C[R_r]` via `det(s_1 I_4) = s_1⁴`.  For `C[P_r]` the same
one-line argument goes through — `per_3(diag(s_1,s_1,s_1)) = s_1³`, so
`s_1⁴ = s_1·per_3(…) ∈ P_r` and `u` does not vanish on it — but it is **not in
the record** and should be written down before it is used.

## 3. The saving, measured

`analysis/wk10_int_stable_weight.py`, exact multiset counts:

| | `δ`-graded weight space | stable weight space | factor |
|---|---|---|---|
| **n = 3 LMR** `(19,7,2⁵)`, `δ=12` | `N_S = 1 155 302` | `W = 69 766` | **16.6×** |
| **n = 4 LMR** `(65,17,2⁷)`, `δ=24` | `N_S = 156 438 903 314` | `W = 7 212 907 703` | **21.7×** |

The stabiliser is the same on both sides of each row (`S_7` on the seven 2s at
`n = 4`, `S_5` at `n = 3`), so the factor carries to the column count:

    n_χ  :  3.10 × 10⁷   ⟶   ≈ 1.43 × 10⁶        (n = 4)
    n_χ  :  9 628        ⟶   ≈ 581               (n = 3)

The source is the same 274-dimensional space either way; only the ambient it
sits in shrinks.

## 4. What that does to the walls

**`n_χ` wall.**  Extrapolating session 60's measured build (`n_χ = 92 031` →
20.7 M nonzeros, 1.69 GB) linearly: `1.43 × 10⁶` gives ≈ 315 M nonzeros and
≈ 26 GB, against 570 GB.  **Still ~15× beyond session 60's practical ceiling of
`n_χ ~ 10⁵` — this does not make the goal cell easy.**  It moves it from 300×
out of reach to 15× out of reach, which is the difference between needing a new
idea and needing a bigger machine plus the sparse route.

**Support wall.**  Whatever `|S|` scaling session 63 measures, it is measured
against `n_χ`; a 20× smaller ambient moves the same curve back by 20×, and the
Gram cost is quadratic, so ~400× on that term.

## 5. The validation is free

The `n = 3` LMR cell in the stable picture is **581 columns**.  The answer is
already known — session 62/63 measured `i_det = 1` there this morning.  So the
whole stable route can be built and validated end to end, against a known
answer, at a size that is trivial: build the stable weight space at
`ρ = (7,2⁵)` in `Sym(Sym² ⊕ Sym³)(C⁶)`, the 6 raising operators, the HWV
kernel (should return `a_∞ = 6`), evaluate at characteristic polynomials of
traceless 6-parameter pencils of `3×3` matrices, and check the rank is 5.

**Do this before anything at `n = 4`.**  It costs an afternoon and it tests
every part of the construction at once: the dehomogenisation, the `M_ℓ` point
family, and Proposition S's identification.

## 6. A second ladder — real, and it runs the wrong way for this purpose

Recording it because it is new and it is useful elsewhere.

`det(A_1) = e_4(A_1)` has weight `(4,0,…,0)` in the tail variables, and it **is
a highest-weight vector**: the raising operators `E_{i,i+1}` act as derivations
sending `A_{i+1} ↦ A_i`, and `det(A_1)` contains no `A_j` for `j ≥ 2`, so every
one annihilates it.  Multiplication by it is injective on the ambient polynomial
ring, hence on `I(M_ℓ)`, and injective on `C[M_ℓ]` because `M_ℓ` is irreducible
so `C[M_ℓ]` is a domain and `det(A_1)` is not identically zero on it.

So there is a **second ladder, in the tail's first part**, in steps of 4:

    I(5, 2⁷)  ≤  I(9, 2⁷)  ≤  I(13, 2⁷)  ≤  I(17, 2⁷)

**This does not help C2**, because it bounds `I(17)` from *below* and the goal
needs an upper bound.  It **does** help S1: its deliverable is to push the
stable dead region farther, and `I(k) = 0` at the largest feasible `k` proves
`I = 0` at every smaller one.  The weight spaces along it, for reference:

    k :   2         3         4         5         6        8        10        12       14       17
    W : 7.36e6   2.06e7   4.85e7   1.00e8   1.88e8   5.25e8   1.17e9   2.25e9   3.82e9   7.21e9

## 7. What this does not solve, stated plainly

- `1.43 × 10⁶` is an estimate `W/|Stab|`; compute `n_χ` directly before relying
  on it.
- It is still beyond anything the programme has built.  The gain is a factor of
  twenty, not a change of regime.
- A new point family is needed — characteristic polynomials of traceless
  `(ℓ−1)`-pencils — and it must be calibrated like any other evaluator.  §5 is
  where that happens.
- Proposition S's identification of stable `i_det` with the `M_ℓ` ideal
  multiplicity is session 57's and was reproduced here only for `a_∞`
  (155/155 at length-5 tails), **not** for the `i_det` half.  §5 is also the
  first test of that half.

## 8. The next question worth asking

The `δ`-ladder is generated by `u = e_1⁴`, weight `(4,0,…,0)` in the *full*
variable set; the second ladder by `det(A_1)`, weight `(4,0,…,0)` in the *tail*
variables.  Both are highest-weight multipliers that are nonzero on the variety.
**Is there a complete list?**  Every such multiplier gives a monotonicity, and
the useful ones are those that run toward small weight spaces from above — that
is, elements whose *removal* is what one wants.  A systematic search over
highest-weight elements of `C[M_ℓ]` that are nonzerodivisors is a well-posed
question, it is small, and it is the natural continuation of Proposition S.
