# Pre-registration — session 44 (the six-row cap: bracketing `I(D_6^{det_4})` from above)

Branch `s44-sixrowcap` off `0c229c1`.  Written **before any rank is
computed**.  The only computation performed before this file was committed is
Hilbert-series arithmetic (binomial sums; no matrix, no rank) — it is
reproduced in §2 so that the prediction can be judged against the same
numbers I had.

Labels used later: **proved** / **measured** / **adopted-from-literature** /
**expectation**.

## 1. The question

`D_6^{det_4} = closure{ det_4(Σ_{i=1}^{6} s_i A_i) } ⊆ Sym^4 C^6`.  Sessions 36
and 41 measured 90 six-row cells through `δ = 8` with `mult_det = a` at every
one, so `I(D_6^{det_4})` is empty on everything reachable; the cells where it
would plausibly switch on are two to three orders of magnitude out of reach.
This session tries to bound the onset **from above**, by the mechanism that
gave `cap(n)` at five rows (`docs/onset_conjecture.md` Theorem 1): a rank drop
of the degree-`d` Macaulay matrix `M_d` of the partials on the determinantal
locus makes the size-`ρ_d` minors — polynomials of degree `ρ_d = rank M_d`
(generic) on `Sym^4 C^6` — nonzero elements of `I(D_6^{det_4})_{ρ_d}`.

**The five-row proof does not transfer.**  At `r = 5` the generic determinantal
member has isolated singularities (`ν(n)` nodes) and Dimca's theorem converts a
defect of the node set into Milnor-algebra dimension.  At `r = 6` the singular
locus is the rank-`≤ 2` locus of the pencil, of codimension 4 in `P(M_4)`,
hence a **curve** in `P^5`.  Dimca's isolated-singularity theorem is
unavailable; this session must decide the degree of the first drop by
computation, with the Gulliksen–Négård ceiling of §2 as the only a priori grip.

## 2. The a priori ladder (arithmetic only; no ranks)

`S = C[s_1..s_6]`, `F` a quartic, `J_F` its Jacobian ideal (6 cubics),
`M_d` the Macaulay matrix with rows `(i, m)`, `m ∈ monomials of degree d−3`.
`rank M_d(F) = dim (J_F)_d`, `corank = dim (S/J_F)_d`.

Smooth `F`: partials are a regular sequence, `dim (S/J_F)_d = h_d :=
[t^d] (1+t+t^2)^6`, so the generic rank is `ρ_d = dim S_d − h_d`.

`J(M)` = ideal of the sixteen `3×3` minors of `M(s)`.  Jacobi's formula
`∂_kF = tr(adj M(s)·A_k)` puts every partial in `J(M)`, so **`J_F ⊆ J(M)` and
`rank M_d ≤ dim J(M)_d` at every determinantal point**.  For a generic pencil
the rank-`≤ 2` locus is cut in codimension 4 (Kleiman), so `grade J(M) = 4`
and the Gulliksen–Négård resolution

    0 → S(−8) → S(−5)^16 → S(−4)^30 → S(−3)^16 → S → S/J(M) → 0

is exact, giving `H_{S/J(M)}(d)` exactly.  Hence the ceiling column below.

| `d` | rows | cols `dim S_d` | `h_d` | generic rank `ρ_d` | `H_{S/J(M)}(d)` | ceiling `dim J(M)_d` | slack |
|---|---|---|---|---|---|---|---|
| 3 | 6 | 56 | 50 | 6 | 40 | 16 | +10 |
| 4 | 36 | 126 | 90 | **36** | 60 | 66 | +30 |
| 5 | 126 | 252 | 126 | **126** | 80 | 172 | +46 |
| 6 | 336 | 462 | 141 | **321** | 100 | 362 | +41 |
| 7 | 756 | 792 | 126 | **666** | 120 | 672 | **+6** |
| 8 | 1512 | 1287 | 90 | **1197** | 140 | 1147 | **−50** |
| 9 | 2772 | 2002 | 50 | 1952 | 160 | 1842 | −110 |

**Consequence, proved before any computation.**  At `d = 8` the ceiling `1147`
is below the generic rank `1197`.  So every determinantal quartic in six
variables has `rank M_8 ≤ 1147 < 1197`, the size-`1197` minors of `M_8` are
degree-`1197` forms on `Sym^4 C^6` that are not identically zero (a smooth
quartic attains `1197`) and vanish on `D_6^{det_4}`.  **`onset I(D_6^{det_4}) ≤
1197` unconditionally**, modulo Kleiman transversality and the GN resolution,
both adopted and named.  Every computation this session can do is to lower
this.

`H_{S/J(M)}(d) = 20d − 20` for `d ≥ 5`: the singular curve has degree 20 (the
Harris–Tu number `ν(4) = 20`) and arithmetic genus 21 — recorded here as a
prediction for Phase 4.3.

## 3. Predictions (binding)

**P1 — the smallest `d` with a strict drop on `D_6^{det_4}`: `d = 7`.**
Cap `= ρ_7 = 666`.  Predicted corank `127 = h_7 + 1` (drop of exactly one),
predicted rank `665`.  Reasoning: at the five-row anchor `n = 4, r = 5` the GN
ceiling forces a drop only at `d = 8` (ceiling 475 < generic 480) yet the true
first drop is at `d = 7` (measured corank `31 = 30 + 1`, cap 300) — the drop
begins one degree *before* the ceiling forces it, and is tight at the forced
degree.  Here the forced degree is 8, so the predicted first drop is 7; and at
`d = 7` the ceiling leaves only six dimensions of headroom over `ρ_7`, so a
single non-Koszul syzygy in degree 7 suffices.  Independently, both five-row
anchors put the first drop at `3(n−1) − 2` in the generator degree `n−1`
(`d = 4` at `n = 3`, `d = 7` at `n = 4`); if that degree is a function of the
generator degree rather than of `r`, it is again 7.

Alternatives, with the priors I am willing to be scored on:
`d = 7` (cap 666) ≈ 0.45; `d = 8` (cap 1197, the forced degree, i.e. the
ceiling is tight from the start) ≈ 0.35; `d = 6` (cap 321) ≈ 0.17;
`d ≤ 5` (cap 126 or 36, i.e. a linear syzygy among the partials) ≈ 0.03.
A drop at `d = 4` or `5` would require the six partials to satisfy a linear
syzygy `Σ L_k ∂_kF = 0`; the syzygies of that shape are `X M(s) + M(s) Y ∈ L`
with `tr X + tr Y = 0`, which is 60 conditions on a 31-dimensional space and
has only the trivial solution `(λI, −λI)` for a generic 6-dimensional `L`.  I
therefore expect no drop at `d = 4, 5`, and will treat one as a bug until it
survives an exact integer rank.

**P2 — Phase 4.1, the padded permanent: not a separator.**  A padded point
`ℓ(s)·per_3(A(s))` is a **reducible** quartic, singular along the codimension-2
locus `{ℓ = 0} ∩ {per_3 = 0}` — a threefold in `P^5`, far larger than the
determinantal curve.  Its Milnor algebra is therefore much larger and its
Macaulay rank much smaller, so the minors will vanish at padded points too.
Prediction: the minors vanish on padded permanents (probability ≈ 0.97), the
cap is a bound on the determinant ideal and **not** a separating equation.  If
they do not vanish, I stop and apply the `docs/s41_prompt.md` verification
protocol before claiming anything.

**P3 — Phase 4.3.**  The rank-`≤ 2` locus of a generic six-parameter `4×4`
pencil is a curve in `P^5` of degree 20 and arithmetic genus 21, with
`H_{S/J(M)}(d) = 20d − 20` for `d ≥ 5`.

**P4 — Phase 4.4.**  If the first drop is at the GN-forced degree in general,
the rule is: the smallest `d` with `dim S_d − H_{S/J(M)}(d) < dim S_d − h_d`,
i.e. `h_d < H_{S/J(M)}(d)`.  At `(n,r) = (3,5)` this gives `d = 4`, cap 65 ✓;
at `(4,5)` it gives `d = 8`, cap 480 ✗ (truth 300, i.e. the rule is an upper
bound only).  I predict the rule is a **cap on the cap**, correct at `(3,5)`
and loose at `(4,5)`, and will report it as such rather than as a formula.

## 4. Method, fixed in advance

- Ranks by `python-flint` `nmod_mat`, at both house primes
  `P1 = 2147483647`, `P2 = 2147483629`.
- Determinantal points: `det_4(Σ_{i=1}^{6} s_i A_i)` with independent uniform
  integer `A_i` in `±BOX`, `BOX = 10^6`; at least three fresh pencils per `d`,
  fresh seeds, both primes.
- Smooth controls: uniform random integer quartics, at least three per `d`,
  both primes; the control is *passed* only if the corank equals `h_d`
  exactly, which is simultaneously the check of the `h_d` formula.
- Direction of every inference: a rank measured at a point is `≤` the generic
  rank, so a **measured drop is a proof** that the generic determinantal rank
  drops (the locus is irreducible and the minors are polynomials), while a
  measured *equality* only bounds the generic rank below and does **not** prove
  the absence of a drop.  Absence of a drop is therefore reported as measured,
  never as proved.
- Anchors first: `(n,r,d) = (3,5,4)` must give generic 65 / determinantal 64,
  and `(4,5,7)` generic 300 / determinantal 299, before the six-row ladder is
  believed.

## 5. Stopping rules

1. A drop that appears at one seed or one prime and not another is a bug or an
   unlucky prime: chase it with a third prime and an exact `fmpz_mat` rank on
   the same matrix.  Never average, never report a majority vote.
2. A drop at `d ≤ 5` is not reported until confirmed by an exact integer rank.
3. If the anchors fail to reproduce, the session stops and reports the failure;
   no six-row number is published on a broken harness.
4. Phase 4.2 (weights of the minor module) is attempted only if the cap `ρ` is
   below 200; at `ρ = 321` or more the module is out of reach and I will say so
   rather than produce a partial decomposition.
5. Every run is bounded by `timeout` and `ulimit -v`, its pid recorded in
   `results/logs/<run>.pid`, and ended only by that recorded pid.
6. Budget: if the ladder is not settled after the anchors plus three seeds per
   `d`, I report the ladder as far as it goes and the a priori bound 1197, and
   do not start Phase 4.

## 6. What would falsify the session's claim

The cap claim is falsified by a demonstration that the size-`ρ` minors of `M_d`
are identically zero on `Sym^4 C^6` (they are not: a smooth quartic attains
`ρ_d`), or that some determinantal point attains rank `ρ_d` at the reported `d`
(a single such point kills the drop at that `d`).  Both are cheap to check and
both are run.
