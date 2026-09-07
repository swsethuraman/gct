# Integrator note 3 to session 63 — I overreached; continue, and here is the sharper reason why

Note 2 told you to stop measuring and report two walls.  **Withdraw that
instruction.**  The external memo is right that three points cannot carry the
extrapolation, and one of my two walls was not a wall at all.  Continue the
measurement programme, with the amendments below.

## 1. Where I overreached

My "wall 1" was an extrapolation over four orders of magnitude from three
points whose exponent is **visibly still moving**:

    n_χ ×7.9  →  |S| ×5.0   ⟹  α = 0.784
    n_χ ×4.7  →  |S| ×2.5   ⟹  α = 0.600

and the conclusion is not robust to where it settles:

| α settles at | `|S|` at `n_χ = 3.1×10⁷` | `273·|S|²` | |
|---|---|---|---|
| 0.60 | 205 895 | 1.2 × 10¹³ | red |
| 0.50 | 85 824 | 2.0 × 10¹² | amber |
| 0.40 | 35 774 | 3.5 × 10¹¹ | amber |
| 0.30 | 14 912 | 6.1 × 10¹⁰ | **yellow** |
| 0.25 | 9 628 | 2.5 × 10¹⁰ | **yellow** |

I fitted a constant exponent to a sequence that does not have one, and then
reported the result as a measurement.  That is the same error I have been
correcting in other people's memos this week, and the correction is the same:
**an extrapolation is not a wall.**  Get the `n_χ ~ 10⁴–10⁵` points.

## 2. The proposed second compression — right instinct, wrong statistic

The memo proposes measuring `T_S = #{type(P,Q) : P,Q ∈ S}` and treating
`T_S ≪ |S|²` as evidence that the Gram route survives.  **`T_S` does not
control the cost.**  Writing `A = Σ_k κ_k · (Cᵀ A_k C)`, partitioning the pairs
by orbital type does not reduce the number of pairs — you still classify every
one of the `|S|²` of them, and classification (form the block-intersection
matrix, canonicalise it) is the expensive per-pair step.  Few distinct values is
necessary for a compression and nowhere near sufficient.

**The statistic that does control it is the number of distinct rows of `β_S`.**
For `P ∈ S` let its profile be `(type(P,Q))_{Q ∈ S}`.  If there are `T` distinct
profiles then `β_S` has `T` distinct rows and

    cost  =  |S|²  (classification, unavoidable)  +  273·T·|S|  (the products)

instead of `|S|² + 273·|S|²`.  **That removes the factor of 273**, which is what
actually kills the route.  At `|S| = 10⁵` with small `T` the total is `~10¹⁰`,
which is feasible; the `273` multiplier is what turns it into `10¹³`.

So measure distinct profiles, or the rank of `β_S`, not the number of realised
types.  Record `T_S` too — it is cheap and it may reveal structure — but do not
put it in the decision tree.

## 3. The reason `|S|` matters more than either of us said

Both of us have treated `|S|` as a *cost parameter* of the Gram assembly, with
the source vectors `C` assumed already in hand.  They are not: obtaining `C`
means solving the highest-weight condition at `δ = 24`, and that is my note 2's
"wall 2" — the `~570 GB` raising-operator build.  **So on the naive reading,
`|S|` is downstream of something already out of reach, and no value of it would
help.**

That reading is wrong, and here is the way through.

**Support-restricted solving is exact.**  If `v` is supported on a monomial set
`S`, then `E·v = 0` holds if and only if `E[R(S), S] · v|_S = 0`, where `R(S)`
is the set of rows of `E` having a nonzero entry in some column of `S`.  Rows
untouched by `S` are satisfied automatically.  This is an identity, not an
approximation: **every solution of the restricted system is a genuine
highest-weight vector of the full space.**

The only risk is incompleteness — vectors not supported in `S` are missed — and
that is *detected, not guessed*: compare the solution dimension against the
known `a_δ` from the plethysm.  If it equals `a_δ`, then `S` carries a full
basis and the construction is exact and self-certifying.

**And the ladder makes `S` grow rather than be guessed.**  Note 2 §3: `u` is the
single coordinate `c_{(4,0,…,0)}`, so transport preserves support exactly.  So:

    δ = 12 :  solve on a small candidate S,  verify dim = a_12 = 2
    δ → δ+1:  transport (supports unchanged, free), extend S by candidates for
              the b_{δ+1} newly born vectors, solve, verify dim = a_{δ+1}
    …
    δ = 23 :  transport once more, form A_24 = Cᵀ β_S C

The generic `n_χ = 3.1×10⁷` space is never formed.  **`|S|` stops being a
parameter of the computation and becomes its size** — which is exactly why the
measurement is worth the session's remaining time, and why the memo's instinct
to keep measuring is better than my instruction to stop.

**The open question this exposes**, and it is sharper than "measure `|S|` at a
bigger cell": the transported vectors are free, but the `b_δ` newly born ones at
each rung need a candidate monomial set.  If that set has to be all of `n_χ`,
nothing is gained.  So — **can the newly born vectors' supports be predicted, or
grown incrementally from the transported ones?**  The birth counts are
`2, 37, 54, 52, 43, 31, 22, 14, 9, 5, 3, 1, 1`, so the largest single rung is 54
vectors at `δ = 14`, not 273 at `δ = 24`.  If the answer is yes, C2 is
reachable by a route neither of us had costed.

## 4. Revised measurement list

Per buildable LMR-family cell, spanning `n_χ ~ 10⁴` through `10⁵` and beyond:

1. `n_χ`, mean support, `|S|`, `|S|/n_χ` — as the memo asks.
2. **Overlap statistics between the source supports.**  The memo is right that
   this matters: 273 individually moderate vectors with a manageable union is
   precisely the favourable case, and the union is what the cost sees.
3. **`|R(S)|`, the number of equation rows touched by `S`, and `|R(S)|/|S|`.**
   Nobody has named this; it is the other half of the restricted-solve cost
   in §3 and it decides whether that route is cheap.
4. **Distinct row-profiles of `β_S`** (§2), not `T_S`.
5. **Does the newly born vector at each rung have support inside the union of
   the transported ones, or does it need new monomials — and how many?**  This
   is the §3 question in measurable form, and it is the single most valuable
   number you could return.

The memo's zones are sensible and I endorse them — green below `3×10³`, yellow
to `2×10⁴`, retire direct assembly above `10⁵` — with one amendment: under §3
those zones now govern the **whole** computation, build included, not just the
Gram assembly.

## 5. Correction to note 2

Note 2 §4 reported "both walls measured" and told you to stop.  Wall 1 was an
over-extrapolation (§1).  Wall 2 — the `570 GB` build — is real for a *generic*
build over the whole weight space, and **is not a wall for the support-restricted
build of §3**, which never forms that space.  Note 2's §1, §2 and §3 stand: the
`n_χ` confirmation, the correction to `docs/lmr_cell.md` §3a that the predecessor
is not cheaper, and the transport lemma with its non-saving.  Its §4 conclusion
does not, and its §5 recommendation — deliver the `n = 3` positive control —
stands on its own merits rather than as a consolation.
