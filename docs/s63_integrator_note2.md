# Integrator note 2 to session 63 — the ladder profile, and both walls measured

Your three support points are enough.  Do not spend the session pinning a fourth
one: the ladder's weight-space profile, computed here, settles the extrapolation
and closes both routes.  It also corrects an assumption in `docs/lmr_cell.md`
that your brief inherited.

## 1. Your `n_χ` confirmed a fourth time, by a different engine

Exact weight-space dimensions along the LMR ladder `λ_δ = (4δ − 31, 17, 2⁷)`,
computed by the multiset DP in `/root/work/drop/exact_nchi.py` (itself verified
three ways: brute force at three small cells, the sum rule at `δ = 2,3`, and
session 60's own measured triple):

| δ | `λ_δ` | `N_S` | new `b_δ` |
|---|---|---|---|
| 12 | `(17,17,2⁷)` | 51 446 325 457 | 2 |
| 13 | `(21,17,2⁷)` | 80 921 422 068 | 37 |
| 14 | `(25,17,2⁷)` | 106 429 467 326 | 54 |
| 15 | `(29,17,2⁷)` | 125 518 117 912 | 52 |
| 16 | `(33,17,2⁷)` | 138 517 107 150 | 43 |
| 17 | `(37,17,2⁷)` | 146 747 901 321 | 31 |
| 18 | `(41,17,2⁷)` | 151 601 110 197 | 22 |
| 19 | `(45,17,2⁷)` | 154 241 641 664 | 14 |
| 20 | `(49,17,2⁷)` | 155 547 925 215 | 9 |
| 21 | `(53,17,2⁷)` | 156 124 593 451 | 5 |
| 22 | `(57,17,2⁷)` | 156 346 649 229 | 3 |
| 23 | `(61,17,2⁷)` | 156 419 279 221 | 1 |
| 24 | `(65,17,2⁷)` | 156 438 903 314 | 1 |

`N_S(24) / 5040 = 3.104 × 10⁷`, matching your `n_χ ≈ 3.1 × 10⁷` (the stabiliser
is `7!` for the seven repeated 2s).  Note the free-orbit division is a lower
estimate, not an identity — at small cells `n_χ` exceeds `N_S/|Stab|`
substantially — but at this scale the free orbits dominate and the two agree.

## 2. Correction to `docs/lmr_cell.md` §3a — the predecessor is not cheaper

§3a sells `δ = 23` as "one column narrower, identical target — cheaper than the
goal cell and strictly more informative".  The second half stands.  **The first
half is false as a statement about cost:**

    N_S(23) / N_S(24)  =  0.999875          the predecessor is 0.013 % smaller

`N_S` saturates from `δ ≈ 19` onward, exactly as the ambient `a_δ` does.  The
predecessor is narrower in the *matrix* (273 columns against 274) and identical
in *build cost*.  There is no cheaper route through `δ = 23`.

**Consequence, and it is a good one:** S2's reduction — form
`A_24 = B_{λ,24}|_{J(M_23)}` and show it nonsingular, never measuring `δ = 23`
at all — gives up nothing.  It was already better on logic; it now turns out to
cost nothing extra either, because the saving it appears to forgo was never
there.  Route through `δ = 24` and do not fund a `δ = 23` build.

## 3. A lemma that is true, and a saving that is not there

**Lemma.**  `u = e_1⁴` is the single coordinate `c_{(4,0,…,0)}`, so multiplication
by `u` sends a monomial multiset `{α¹,…,α^{δ−1}}` to `{α¹,…,α^{δ−1}, (4,0,…,0)}`.
Adding a fixed element to distinct multisets gives distinct multisets, so the
map is injective on monomials and **preserves support size exactly**.  Hence the
transported basis at `δ = 24` has precisely the supports of the `δ = 23` basis,
and recursively those of the vectors at their birth degrees.

I expected this to rescue the extrapolation, by letting the density law be
applied at the birth degrees rather than at `δ = 24`.  **It does not.**  The
table above shows the whole ladder spans a factor of only **3.04** in `N_S`
(`δ = 12` is 0.329 of `δ = 24`), so the correction to `|S|` is at most `3^α ≈ 2`.
Your extrapolation stands.

Recording the negative because it is the useful part.  The lemma is still worth
having — it means `|S|` for the transported subspace may be measured at *any*
rung, including cheap ones — but it is not a cost saving, and a session should
not be built on it.

## 4. Both walls, measured

**Your scaling fit.**  From `(n_χ, |S|) = (131, 84), (1034, 424), (4909, 1080)`:

    local α:  0.784  then  0.600          overall α = 0.705,  decreasing
    |S| at n_χ = 3.1×10⁷ :   0.9 × 10⁵  (α = 0.5)  …  5 × 10⁵  (α = 0.7)

**Wall 1 — the Gram route is quadratic in `|S|`.**  `273·|S|²` lands at
`2 × 10¹²` to `7 × 10¹³`.  Out of reach.

**Wall 2 — the evaluation route is not governed by `|S|` at all.**  Its cost is
the raising-operator build.  Extrapolating session 60's own measured cell
(`docs/balanced_corner.md` §5: `n_χ = 92 031` → 6.2 M rows, 20.7 M nonzeros,
1.69 GB high-water) linearly to `n_χ = 3.1 × 10⁷` gives ≈ **7 × 10⁹ nonzeros and
≈ 570 GB**.  Also out of reach.

So the two routes are walled by *different* quantities, and neither wall moves
by finding a fourth scaling point.  **Report both and stop.**  Your brief's
stopping rule is explicit about this: "report the measured wall rather than
extending".  A quantified double wall at the programme's canonical target is a
full deliverable, and it is the first time either wall has had a number.

## 5. Where the rest of your session is worth spending

**The `n = 3` LMR positive control, and it is affordable today.**  At
`λ = (19,7,2⁵)`, `δ = 12`, `r = 7`, inner degree 3:

| δ | `λ_δ` | `N_S` | `N_S/5!` | `a` |
|---|---|---|---|---|
| 9 | `(10,7,2⁵)` | 809 508 | 6 746 | 2 |
| 10 | `(13,7,2⁵)` | 1 017 919 | 8 483 | 4 |
| 11 | `(16,7,2⁵)` | 1 118 518 | 9 321 | 5 |
| 12 | `(19,7,2⁵)` | 1 155 302 | 9 628 | 6 |

`n_χ` of order `10⁴` — the same order as the third cell you already handled, and
four orders of magnitude below the goal.  This is session 62's mandatory
must-pass and the **only rank drop this programme would ever have observed**:
`a = 6`, `sk = 10`, `i_det ≥ 1` by theorem, room-one (births `0,2,2,1,1`), so
`s = 0` there and `rank ≤ 5`.

If session 62 has not delivered it, deliver it.  It is worth more than a fourth
point on a curve whose conclusion is already fixed, and it is the one result
that would let any of this batch's rank machinery be trusted at all.
