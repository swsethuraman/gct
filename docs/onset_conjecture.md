# The onset of `I(D_5^{det_n})`: the cap theorem at every `n`, the onset conjecture, and the `n = 5` anomaly

Session 40 (2026-09-02), branch `s40-onset` off `e9cb8dd`.  Pre-registration
`results/PREREG_s40.md` (commit `d8a50f2`, before any computation).  Exact
checks: `analysis/wk9_s40_cap.py` (`results/logs/s40_cap.log`),
`analysis/wk9_s40_jacobian.py` (`results/logs/s40_jacobian_n34.log`,
`s40_jacobian_n56.log`), `analysis/wk9_s40_frame.py` (`results/logs/s40_frame.log`);
the `n = 3` det-side runs of Deliverable 4 in `results/n3_ledger.md`.
Labels: **proved** / **measured** / **adopted-from-literature** / **expectation**.

## 0. Verdict

> **Theorem 1 (the cap at every `n`; proved modulo Kleiman, Dimca and
> Gulliksen–Negård, all adopted and named).**  For every `n ≥ 2` the
> size-`cap(n)` minors of the degree-`(3n−5)` Macaulay matrix of the five
> partials lie in `I(D_5^{det_n})`, where
>
>     cap(n) = dim Sym^{3n−5} C^5 − μ_{3n−5}(n) = 5·C(2n,4) − 10·C(n+1,4) = 5n(n−1)²(7n−8)/12
>            = 5, 65, 300, 900, 2125, 4305, ...   (n = 2, 3, 4, 5, 6, 7, ...).
>
> Hence `onset I(D_5^{det_n}) ≤ cap(n)`.  At `n = 2` the bound is the
> discriminant and is exact (proved).  At `n = 3` this moves paper 1's bracket
> from `8 ≤ δ_0 ≤ 80` to **`8 ≤ δ_0 ≤ 65`**; at `n = 4` the window is
> `[8, 300]` (s37's cap, now with its defect step proved rather than
> measured).  The mechanism is one formula at every `n`: the generic member is
> a threefold with `ν(n) = n²(n²−1)/12` ordinary double points which fail to
> impose independent conditions on forms of degree `2n−5` by exactly one, and
> Dimca's theorem turns that one into one extra dimension of the Milnor
> algebra in degree `3n−5`.
>
> **Conjecture 2 (expectation).**  `onset I(D_5^{det_n}) = cap(n)`: the
> Jacobian minors are the first equations.  Proved at `n = 2`; open at `n ≥ 3`;
> killed by any length-5 bite below 65 at `n = 3` or below 300 at `n = 4`.
>
> **The `n = 5` anomaly (proved + measured).**  `ν(5) = 50` but
> `codim D_5^{det_5} = 49` because the fifty nodes fail to impose independent
> conditions on *quintics* by one — the same defect that makes the threefold
> non-factorial, since `2n − 5 = n` exactly at `n = 5`.  In general
> `codim D_5^{det_n} = ν(n) − C(n−1, 4)`, `D_5^{det_n}` is an irreducible
> component of the `ν(n)`-nodal locus at every `n` where the minor ideal is
> saturated in degree `n` (measured at `n = 3..6`), superabundant by
> `C(n−1,4)` for `n ≥ 5`, and the cap theorem is untouched: it needs only
> `def_{2n−5} ≥ 1`, and more defect can only lower the cap.
>
> **Measured this session, both primes, fresh pencils:** corank of
> `M_{3n−5}` on `D_5^{det_n}` is `6, 31, 102, 256` at `n = 3, 4, 5, 6` against
> the smooth `5, 30, 101, 255`; the minor-ideal Hilbert functions equal the
> Gulliksen–Negård prediction in every degree; `def_{2n−5} = 1` exactly and
> `def_n = 0, 0, 1, 5 = C(n−1,4)` at `n = 3, 4, 5, 6`.
>
> **The `n = 3` twin, sharpened (proved; §5).**  `D_5^{det_3}` is the closure
> of the cubic threefolds singular at six points in linearly general
> position: the generic six-nodal cubic threefold with nodes in general
> position is determinantal — the affirmative answer to the first
> sub-question of paper 1's Question 8.5.
>
> **Deliverable-4 runs (measured).**  At `n = 3`, `δ = 8`, all 60 length-5
> cells with `n_χ ≤ 5000` (120 of the 227 ambient units of the slab) have
> `mult_det = a`: the ideal is empty there.  The unique degree-10
> `SL_5`-invariant of cubic threefolds (`(6^5)`, `a = 1`) is the single most
> consequential cheap test; its status, and the `δ = 9` cells run, are in
> `results/n3_ledger.md` and `results/n3_length5_plan.md`.

## 1. Objects and the numbers

`D_5^{det_n} = closure{ det M(s) : M(s) = s_1 A_1 + ... + s_5 A_5, A_i ∈ M_n }
⊆ Sym^n C^5`, the quinary `n`-ics with an `n×n` linear determinantal
representation; `dim D_5^{det_n} = 5n² − (2n² − 2) = 3n² + 2` for `n ≥ 3`
(generic finite stabiliser: paper 1 at `n = 3`, `docs/washout_lemma.md` §4
at `n = 4`; the same count at every `n ≥ 3` — the stabiliser of `det_n` has
dimension `2(n²−1)` and a generic 5-tuple has finite stabiliser inside it —
is **adopted from the record** for `n = 3, 4` and **expectation** for
`n ≥ 5`, where it enters only the anomaly discussion of §4, not Theorem 1).

`S = C[s_1..s_5]`, `S_k = Sym^k C^5`.  For `F ∈ Sym^n C^5`, `J_F = (∂_1F, ..,
∂_5F)`, `M(F) = S/J_F` its Milnor algebra, and `M_k(F)` the degree-`k`
**Macaulay matrix**: rows indexed by pairs `(i, m)`, `m` a monomial of degree
`k − n + 1`, columns by monomials of degree `k`, entry the coefficient of the
column monomial in `m·∂_iF`.  Its entries are linear in `F`, its row space is
`(J_F)_k`, so `corank M_k(F) = dim M(F)_k`.  For smooth `F` the partials form
a regular sequence and

    μ_k(n) := dim M(F)_k = [t^k] ((1 − t^{n−1})/(1 − t))^5,      μ_{3n−5}(n) = 0, 5, 30, 101, 255, 540 at n = 2..7.

`Z(M) = {s ∈ P^4 : rank M(s) ≤ n−2}`, the pencil's intersection with the
rank-`≤ n−2` locus; `J = J(M)` the ideal of the `n²` submaximal
`(n−1)×(n−1)` minors of `M(s)`, generated in degree `n−1`; `I_Z` the
saturated ideal of `Z`.  `ν(n) = deg{rank ≤ n−2} ⊂ P(M_n)`, by the
Harris–Tu/Giambelli product formula for `n×n` matrices of rank `≤ n−2`
(`∏_{i=0}^{1} (n+i)! i! / ((n−2+i)! (2+i)!)`):

    ν(n) = C(n,2) · n(n+1)/6 = n²(n²−1)/12 = 1, 6, 20, 50, 105, 196, 336 at n = 2..8.

For a finite reduced set `N ⊂ P^4` and `k ≥ 0`,
`def_k(N) = |N| − H_{S/I_N}(k) = h^0(I_N(k)) − (h^0(O(k)) − |N|)` is the
failure of `N` to impose independent conditions on forms of degree `k`
(`H_{S/I_N}` the Hilbert function of `N`).

All numbers of this section are in `results/logs/s40_cap.log`, with the
closed forms verified symbolically as polynomial identities in `n`.

## 2. Theorem 1 — the cap

**Theorem 1.**  Let `n ≥ 2`.  Every size-`cap(n)` minor of `M_{3n−5}(F)` is a
nonzero polynomial of degree `cap(n)` in the coefficients of `F` and vanishes
identically on `D_5^{det_n}`.  The span of these minors is a nonzero
`GL_5`-submodule of `I(D_5^{det_n})_{cap(n)}`; hence `onset I(D_5^{det_n}) ≤
cap(n)`.

The case `n = 2` is §2.6; assume `n ≥ 3`.  The proof is four steps; the
labels are per step.

### 2.1 Step 1 — every member is singular along `Z(M)` *(proved)*

Jacobi's formula gives `∂_kF = tr(adj M(s) · A_k)`.  At `s ∈ Z(M)` every
`(n−1)`-minor of `M(s)` vanishes, so `adj M(s) = 0` and every partial of
`F = det M` vanishes: `Z(M) ⊆ Sing(F)`.  (This is paper 1's Theorem
`thm:sharp` argument at `n = 3` and `docs/theory_directions.md` §C(ii)(a) at
`n = 4`, verbatim at every `n`.)

### 2.2 Step 2 — for the generic pencil, `Sing(F) = Z(M)` consists of `ν(n)` ordinary double points *(Kleiman adopted; the rest proved)*

Let `Σ_k = {rank = k} ⊂ P(M_n) = P^{n²−1}`, a smooth locally closed
subvariety (one `GL_n × GL_n`-orbit) of codimension `(n−k)²`; its closure is
the rank-`≤ k` locus, and the determinant hypersurface `{det = 0} =
closure(Σ_{n−1})` is smooth exactly along `Σ_{n−1}`.  For linearly
independent `A_1..A_5` (a generic condition) the pencil is a `P^4 = P(L)`,
`L = span(A_i)`.

*Adopted (Kleiman's transversality theorem, characteristic 0, for the
transitive action of `PGL(M_n)` on `P(M_n)`).*  For a generic 5-dimensional
`L`, `P(L) ∩ Σ_k` is empty or smooth of dimension `4 − (n−k)²`, and the
intersection is transverse, for every `k`.  Consequently: `P(L)` misses
`Σ_k` for `k ≤ n−3` (`4 − 9 < 0`); `P(L) ∩ Σ_{n−2}` is a finite transverse
intersection, hence `Z(M) = P(L) ∩ closure(Σ_{n−2})` is a reduced
0-dimensional scheme whose length is the degree `ν(n)` of the rank-`≤ n−2`
locus (the definition of degree through a generic linear section); and
`P(L) ∩ Σ_{n−1} = {F = 0} \ Z(M)` is smooth of dimension 3, i.e. the
threefold `X = {F = 0}` is smooth away from `Z(M)`.  With Step 1,
`Sing(F) = Z(M)`, exactly `ν(n)` points, each of rank exactly `n−2`.

*Proved (each point is an ordinary double point).*  Fix `s_0 ∈ Z(M)`, choose
bases with `M(s_0) = diag(I_{n−2}, 0_2)`, and write `M(s) = [[P, Q], [R, S]]`
with `P` of size `n−2` and `S` of size `2×2`, so `P(s_0) = I`, `Q(s_0) = 0`,
`R(s_0) = 0`, `S(s_0) = 0`.  In affine coordinates `y ∈ C^4` on `P^4` centred
at `s_0`, `det M = det P · det(S − R P^{−1} Q)`.  The tangent space of the
rank-`≤ n−2` locus at `M(s_0)` is `{B : B_{22} = 0}` (`B` must map
`ker M(s_0)` into `im M(s_0)`), so its normal space is the lower-right `2×2`
block, and transversality says the four entries of `S(y)` are linearly
independent linear forms in `y`.  Since `R` and `Q` vanish at `s_0`,
`R P^{−1} Q = O(|y|²)` and `det(S − R P^{−1}Q) = det S(y) + O(|y|³)`, while
`det S(y) = S_{11}S_{22} − S_{12}S_{21}` is a quadratic form of rank 4 in the
four independent linear forms.  With `det P(s_0) = 1`, `F` has a
non-degenerate quadratic leading term at `s_0`: an `A_1` point.  ∎

### 2.3 Step 3 — the nodes fail forms of degree `2n−5` by at least one *(proved; three routes)*

Let `N = Z(M)` for a generic pencil, `|N| = ν(n)`.  Since every
`(n−1)`-minor vanishes on the rank-`≤ n−2` locus, `J ⊆ I_N`, hence
`H_{S/I_N}(k) ≤ H_{S/J}(k)` for every `k`, i.e.

    def_k(N)  ≥  ν(n) − H_{S/J}(k).                                          (3.1)

*(a) `n = 3` — counting (proved outright).*  `2n − 5 = 1`: six points impose
at most `h^0(O(1)) = 5` conditions on linear forms, so `def_1(N) ≥ 1`.  No
geometry is needed; the defect is `≥ 1` on the entire six-nodal locus.

*(b) `n = 4` — the sixteen cubics (proved, with one exact certificate).*
`2n − 5 = 3 = n − 1`: the sixteen `3×3` minors are cubics through the twenty
nodes.  They are linearly independent for the generic pencil — independence
is an open condition on `(M_4)^5`, and it holds at explicit integer pencils
(rank 16 of the `16 × 35` coefficient matrix at both primes; s35 T2sat, and
`dim J_3 = 16` at two fresh pencils in `s40_jacobian_n34.log`; a rank at a
point is a lower bound on the generic rank, so the direction of the
promotion is the right one).  Twenty points impose at most `35 − 16 = 19 <
20` conditions on cubics: `def_3(N) ≥ 1`.  This is s35's measured defect,
now a proof.

*(c) every `n ≥ 3` — Gulliksen–Negård (adopted) plus one identity (proved).*
Adopted: the ideal of submaximal minors of the generic `n×n` matrix has the
Gulliksen–Negård resolution

    0 → S(−2n) → S(−n−1)^{n²} → S(−n)^{2n²−2} → S(−n+1)^{n²} → S → S/J → 0

(Gulliksen–Negård 1972; Bruns–Vetter, *Determinantal rings*, and Weyman,
*Cohomology of vector bundles and syzygies*, for the statement in this
form), and it specialises to a resolution for any square matrix `M` over a
Noetherian ring whose submaximal-minor ideal has the generic grade 4
(generic perfection, Hochster–Eagon / Buchsbaum–Eisenbud; Bruns–Vetter §3).
For the generic pencil `V(J) ⊂ C^5` is the affine cone over the finite set
`N`, of dimension 1, so `grade J = height J = 4` and the resolution
applies.  Therefore

    H_{S/J}(k) = [t^k] (1 − n² t^{n−1} + (2n²−2) t^n − n² t^{n+1} + t^{2n}) / (1−t)^5,

and at `k = 2n − 5 < 2n`,

    H_{S/J}(2n−5) = C(2n−1,4) − n² C(n,4) + (2n²−2) C(n−1,4) − n² C(n−2,4) = ν(n) − 1

— a polynomial identity in `n`, verified symbolically (`wk9_s40_cap.py`;
the binomials are the polynomials `m(m−1)(m−2)(m−3)/24`, which vanish
exactly where the true binomials do for the small `n`).  By (3.1),
`def_{2n−5}(N) ≥ 1` for every `n ≥ 3`.  ∎

The three routes agree where they overlap: (c) at `n = 3` reads
`H_{S/J}(1) = 5`, at `n = 4` `H_{S/J}(3) = 19`.  A conceptual remark, worth
recording because it is what the numbers are saying: the `2n² − 2` linear
syzygies of the minors in the GN complex are the infinitesimal stabiliser of
the determinant — for `(X, Y) ∈ gl_n ⊕ gl_n` with `tr X + tr Y = 0`,
`tr(adj M · (XM + MY)) = det M · (tr X + tr Y) = 0` is a linear relation
among the entries of `adj M`, and these `2n² − 1` relations, modulo the
one-dimensional kernel `(λI, −λI)` of `(X,Y) ↦ XM + MY` at a generic pencil,
are `2n² − 2` of them.  This is also why `dim J_n = 5n² − (2n²−2) = 3n² + 2 =
dim D_5^{det_n}` (§4).

*Measured (both primes, fresh pencils, `s40_jacobian_*.log`).*  `H_{S/J}(k)`
equals the GN value in every degree `min(n−1, 2n−5) ≤ k ≤ 2n` at `n = 3, 4,
5, 6`, stabilising at `ν = 6, 20, 50, 105` (the node counts, measured
independently of Giambelli); the saturated values `h^0(I_N(2n−5))`, computed
as `(J_{2n−5+e} : m^e)_{2n−5}` with `e` chosen so that `J` and `I_N` agree in
degree `2n − 5 + e`, are `0, 16, 77, 226`, i.e. **`def_{2n−5}(N) = 1`
exactly** at `n = 3, 4, 5, 6`.  Direction: `h^0(I_N(k))` is upper
semicontinuous in the pencil, so a measured defect of 1 bounds the generic
defect *above* by 1, and (c) bounds it below: equality is proved at these
`n`.

### 2.4 Step 4 — Dimca's theorem converts the defect into Milnor-algebra dimension *(adopted, pinned by s37)*

*Adopted 1 (Dimca, Bull. Math. Soc. Sci. Math. Roumanie 56 (2013), Thm 3.1;
arXiv:1210.1795, re-read this session to the statement quoted).*  For `D : f
= 0` of degree `d` in `P^m` with only isolated singularities, `K^*(f)` the
Koszul complex of `f_0..f_m` graded by `|x_j| = |dx_j| = 1`,

    dim H^m(K^*(f))_{md − m − 1 − k} = def_k Σ_f       for 0 ≤ k ≤ md − 2m − 1,

where `Σ_f` is the singular subscheme and `def_k Σ_f = τ(D) − dim S_k/(Ĵ_f)_k`
is its failure to impose independent conditions on degree-`k` forms; for
nodes `Σ_f = N` reduced and `τ = |N|`.

*Bookkeeping (proved; `docs/blindness_slab.md` §5, restated).*  With `m =
4`: for isolated singularities the partials have a one-dimensional common
zero set in `C^5`, so `grade J_f = 4`, the Koszul cohomology `H^j(K^*(f))`
vanishes for `j < 4`, and the Euler characteristic of each graded piece of
the complex (which depends on `(m, d)` only) gives

    dim M(f)_k = dim M(f_s)_k + dim H^4(K^*(f))_{k + 5 − d}       (f_s smooth of the same degree).

At `d = n`, `k = 3n − 5`: the correction is `dim H^4(K^*(f))_{2n}`, and
Dimca's index `4n − 5 − k' = 2n` gives `k' = 2n − 5`, inside the range
`[0, 4n − 9]` for every `n ≥ 3` (at `n = 2` the range is empty, which is why
`n = 2` is treated directly).  Hence, for a nodal quinary `n`-ic with node
set `N`,

    dim M(F)_{3n−5} = μ_{3n−5}(n) + def_{2n−5}(N).                                (4.1)

### 2.5 Conclusion *(proved from the steps)*

For the generic pencil, `F = det M` is a hypersurface with exactly `ν(n)`
nodes (Step 2), whose node set has `def_{2n−5} ≥ 1` (Step 3), so by (4.1)
`corank M_{3n−5}(F) = dim M(F)_{3n−5} ≥ μ_{3n−5}(n) + 1`, i.e. `rank
M_{3n−5}(F) ≤ cap(n) − 1` and every size-`cap(n)` minor vanishes at `F`.
The set of such `F` is the image of a dense open subset of `(M_n)^5`, hence
dense in `D_5^{det_n}`; the minors are polynomials, so they vanish on the
closure.  For smooth `F` the corank is exactly `μ_{3n−5}(n)` (regular
sequence), so `rank M_{3n−5} = cap(n)` generically and some size-`cap(n)`
minor is a nonzero polynomial; each entry of `M_{3n−5}(F)` is linear in the
coefficients of `F`, so the minors have degree exactly `cap(n)`.  The span
of the size-`cap(n)` minors is the `μ`-th Fitting ideal of the cokernel of
the `GL_5`-equivariant map `F ↦ (S_{2n−4}^5 → S_{3n−5})` in degree `cap(n)`,
hence `GL_5`-stable.  ∎

The rank formula: `cap(n) = 5·C(2n,4) − 10·C(n+1,4)` counts rows
(`5 · dim S_{2n−4}`) minus the Koszul syzygies `∂_iF·∂_jF − ∂_jF·∂_iF` in
that degree (`C(5,2) · dim S_{n−3}`); the second Koszul term does not reach
degree `3n − 5`.  The closed form `5n(n−1)²(7n−8)/12` follows.

### 2.6 The case `n = 2` *(proved, exact)*

`M_1(F)` is twice the symmetric `5×5` matrix `Q` of the quadric, `cap(2) =
5`, and the unique size-5 minor is `32 det Q`, the discriminant.  `D_5^{det_2}`
is the locus of quadrics of rank `≤ 4` (a `2×2` determinant of linear forms
lies in the span of four linear forms; conversely every quadric of rank `≤ 4`
is `x_1x_2 − x_3x_4` or a degeneration of it, which is `det [[x_1, x_3],[x_4,
x_2]]`), the irreducible hypersurface `{det Q = 0}`, whose ideal in the UFD
`C[Sym^2 C^5]` is principal, generated by the irreducible `det Q` of degree
5.  So `onset I(D_5^{det_2}) = 5 = cap(2)`: the conjecture holds at `n = 2`.

### 2.7 The record at `n = 3`: the corank drop re-verified *(measured)*

`analysis/wk9_s40_jacobian.py`, seed `20260902`, box `±10^6`, three fresh
pencils, both primes: `corank M_4(det M(s)) = 6` at every pencil, against
`5` for a random cubic, `5` for a cubic with five nodes at general points,
and `6` for a cubic with six nodes at general points — at `n = 3` the drop is
"six nodes", not "determinantal", exactly as route (a) says.  The
integrator's three-pencil measurement is reproduced.  `H_{S/J}(1) = 5`
(the six nodes span `P^4`, so `def_1 = 1` exactly), `H_{S/J}(k) = 6` for `k
≥ 2`.

Fresh at this session: `n = 5`, corank `M_{10} = 102 = 101 + 1` (two
pencils); `n = 6`, corank `M_{13} = 256 = 255 + 1` (one pencil, 9 s per
prime); both against the smooth values at random forms.  These are the cap
mechanism operating at two values of `n` where nothing had been measured,
and they agree with (4.1) with `def_{2n−5} = 1` on the nose.

| `n` | `3n−5` | `dim S_{3n−5}` | `μ` | `cap(n)` | `ν(n)` | `codim D_5` | corank on `D_5` (measured) | `def_{2n−5}` (meas.) | `def_n` (meas.) | `C(n−1,4)` | `deg disc` |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 2 | 1 | 5 | 0 | **5** | 1 | 1 | 1 (= `5 − rank Q`) | — | — | 0 | 5 |
| 3 | 4 | 70 | 5 | **65** | 6 | 6 | 6 | 1 | 0 | 0 | 80 |
| 4 | 7 | 330 | 30 | **300** | 20 | 20 | 31 | 1 | 0 | 0 | 405 |
| 5 | 10 | 1001 | 101 | **900** | 50 | 49 | 102 | 1 | 1 | 1 | 1280 |
| 6 | 13 | 2380 | 255 | **2125** | 105 | 100 | 256 | 1 | 5 | 5 | 3125 |
| 7 | 16 | 4845 | 540 | **4305** | 196 | 181 | (≥ 541, thm) | ≥ 1 (thm) | ≥ 15 (thm) | 15 | 6480 |
| 8 | 19 | 8855 | 1015 | **7840** | 336 | 301 | (≥ 1016, thm) | ≥ 1 | ≥ 35 | 35 | 12005 |

`cap(n) < 5(n−1)^4` for every `n ≥ 3`: the Jacobian family always beats the
discriminant, by 19% at `n = 3` and by a factor approaching `12·5/35 ≈ 1.7`.

## 3. Conjecture 2 — the Jacobian minors are the first equations

**Conjecture 2 (expectation).**  For every `n ≥ 2`, `onset I(D_5^{det_n}) =
cap(n)`.  Equivalently: no `GL_5`-covariant of degree below `cap(n)` vanishes
on the quinary `n`-ics with an `n×n` linear determinantal representation.

**Status.**

- `n = 2`: **proved** (§2.6).
- `n = 3`: the record is `I(D_5)_δ = 0` for `δ ≤ 7` (paper 1: certified
  through 5, forced by the measured deficit totals at 6 and 7), so the
  bracket is `[8, 65]`.  This session (Deliverable 4, `results/n3_ledger.md`)
  measured every length-5 cell at `δ = 8` with `n_χ ≤ 5000` — 60 of the 107
  cells, 120 of 227 units — through the validated reduction, det side, both
  primes: **every one has `mult_det = a`**.  `δ = 8` is therefore empty on
  the measured corner; the 47 balanced cells above `n_χ = 5000` (36 of them
  below the frontier) are named in `results/n3_census.md`, not estimated.
- `n = 4`: `[8, 300]` (s34/s36/s38: `δ ≤ 7` empty on every measured cell, `δ
  = 8` empty on 29 peaked cells; s37's cap with Step 3 now proved).

**What kills it.**  A single length-5 cell `(λ, δ)` with `mult_det < a` at
`δ < cap(n)`: at `n = 3` any bite at `δ ≤ 64`, at `n = 4` any at `δ ≤ 299`.
At `n = 3` the cheapest decisive test is the rectangular cell `((6^5), 10)`:
`a = 1`, so there is a unique degree-10 `SL_5`-invariant of cubic threefolds,
and it either vanishes on `D_5` (then `δ_0 = 10` and the conjecture is dead)
or it does not (then no invariant can vanish before degree 15).  Its status
is in `results/n3_ledger.md`.

**What supports it.**

1. Exactness at `n = 2`, where the mechanism and the ideal coincide.
2. Silence through `δ = 7` at both `n`, and at `δ = 8` on every measured
   cell (this session at `n = 3`; s38 at `n = 4`), with the onset known to be
   a *multiplicity* phenomenon at `n = 4`: s38's occurrence screen found
   `a ≤ m_det` at every length-5 cell through `δ = 10` with a widening gap,
   so nothing arithmetic forces an early equation there.
3. s35's Fitting-degree observation, which is a theorem about this family:
   the equations produced by an `F`-linear matrix cost their rank.  Within
   the Jacobian family `t = 3n − 5` is the cheapest degree — at `n = 3` the
   coranks `dim M(F)_t` on `D_5` are `10, 6, 6, 6` at `t = 3, 4, 5, 6`
   (by (4.1)'s general form `dim M(F)_t = μ_t + def_{5n−10−t}(N)` together
   with Dimca's `τ`-stabilisation for `t ≥ 3n − 3`; measured `10, 6, 6, 6`
   at fresh pencils, `s40_jacobian_n3t.log`) against the smooth `10, 5, 1,
   0`, so the vanishing minors have sizes `65, 121, 205` at `t = 4, 5, 6`.
   In general the drop first appears at `t = 3n − 5`: the correction at
   degree `t` is `def_{5n−10−t}(N)`, and `def_{2n−4}(N) = 0` by one more GN
   identity, `H_{S/J}(2n−4) = ν(n)` (verified symbolically); the matrix
   sizes only grow after that.
4. The discriminant route is more expensive at every `n`: `disc` vanishes to
   order `ν(n)` along `D_5^{det_n}`, so its derivatives of order `ν − 1` are
   covariants of degree `5(n−1)^4 − ν(n) + 1` in the ideal — `75` at `n = 3`,
   `386` at `n = 4` — above the cap.
5. Paper 1's dimension count (Question 8.5): at `n = 3` the
   `SL_3 × SL_3`-semi-invariant ring of `(M_3)^5` stays larger than
   `Sym^δ Sym^3 C^5` past degree 100, so no equation is *forced* by counting
   anywhere below the cap.

**What the support is not.**  None of 1–5 is evidence *for* an equation-free
range up to 64; they are the absence of the mechanisms we know.  The
conjecture extrapolates from one hypersurface case and from silence through
degree 8; `D_5^{det_3}` has codimension 6 and its ideal will have generators
in several degrees, of which the cap family is one.  The pre-registered
prior (`PREREG_s40.md` P1.4) was low-to-moderate at `n = 3`, and the
Deliverable-4 plan is the honest way to move it.

## 4. The `n = 5` anomaly, and what "nodes = codimension" was saying

At `n = 3, 4` the codimension of `D_5^{det_n}` equals the number of nodes:
`6 = 6`, `20 = 20`.  At `n = 5`, `ν(5) = 50` but `codim D_5^{det_5} = C(9,4)
− 77 = 49`.  Three statements, each labelled.

**(i) The tangent space of `D_5^{det_n}` is the degree-`n` part of the minor
ideal (proved).**  Differentiating the parametrisation, `d/dε det(M + εB) =
tr(adj M · B)`; as `B(s)` ranges over all `n×n` matrices of linear forms
this is `Σ_{ij} adj_{ji}(s) · (linear forms) = J_{n−1} · S_1 = J_n`.  By
generic smoothness (char 0) the differential is onto `T_F D_5^{det_n}` at a
generic `F`, so `dim J_n = dim D_5^{det_n}`; with GN, `dim J_n = 5n² −
(2n²−2) = 3n² + 2`, which is the stabiliser count of §1 seen from the
syzygies (measured: `dim J_n = 29, 50, 77, 110` at `n = 3..6`).  Hence

    codim D_5^{det_n} = H_{S/J}(n),        ν(n) − codim D_5^{det_n} = ν(n) − H_{S/J}(n) = C(n−1, 4)

(the last a polynomial identity, proved symbolically): `0, 0, 1, 5, 15, 35`
at `n = 3..8`.

**(ii) The nodes fail forms of degree `n` by `C(n−1,4)` (proved `≥`; measured
`=` at `n ≤ 6`).**  By (3.1) with `k = n`, `def_n(N) ≥ ν(n) − H_{S/J}(n) =
C(n−1,4)`, with equality iff `J` is saturated in degree `n` (`J_n = (I_N)_n`).
Measured: `def_n = 0, 0, 1, 5` at `n = 3, 4, 5, 6`, i.e. saturated at each.
So at `n = 3, 4` the nodes impose independent conditions on forms of the
hypersurface's own degree — that is the "coincidence" — while from `n = 5`
on they do not, and the amount they fail by is exactly the excess of the
node count over the codimension.  At `n = 5` the two defects coincide,
`def_5 = def_{2n−5} = 1`, because `2n − 5 = n`; for `n ≥ 6` the nodes fail
degree `n` by more than they fail degree `2n − 5` (`def_k` is non-increasing
in `k`).

**(iii) `D_5^{det_n}` is an irreducible component of the `ν(n)`-nodal locus,
superabundant by `C(n−1,4)` (proved given saturation in degree `n`; hence
proved at `n = 3..6`, expectation beyond).**  Let `I_ν = {(F, p_1..p_ν) :
∇F(p_i) = 0}` be the incidence variety over `P(Sym^n C^5) × (P^4)^ν`.  At a
point `(F, N)` with `F` a generic determinantal form and `N` its nodes, the
differential of the `5ν` defining equations sends `(G, q_1..q_ν)` to
`(∇G(p_i) + Hess_F(p_i) q_i)_i`; each Hessian has rank 4 with image
`p_i^⊥`, and `∇G(p_i) mod p_i^⊥ = n·G(p_i)` by Euler, so the image has
dimension `4ν + (ν − def_n(N))` and the Zariski tangent space of `I_ν` at
`(F, N)` has dimension

    (C(n+4,4) − 1) + 4ν − 5ν + def_n(N) = C(n+4,4) − 1 − H_{S/I_N}(n)  ≥  C(n+4,4) − 1 − H_{S/J}(n) = dim P(D_5^{det_n}),

with equality iff `J` is saturated in degree `n`.  The lift of
`P(D_5^{det_n})` to `I_ν` (through its nodes) is irreducible of dimension
`3n² + 1`; under equality it is the unique component of `I_ν` through
`(F, N)`, and `I_ν` is smooth there.  Any irreducible component `W` of the
closure of the `(≥ ν)`-nodal locus containing `D_5^{det_n}` has generic
member with exactly `ν` nodes (each `A_1` point of `F` absorbs at most one
singular point of a nearby member, by semicontinuity of the Milnor number),
so `W` lifts to `I_ν` through `(F, N)` and lies in the lift of `D_5^{det_n}`:
`W = D_5^{det_n}`.  Its dimension exceeds the expected `C(n+4,4) − 1 − ν(n)`
by exactly `C(n−1,4)`, which is `0` at `n = 3, 4` (the components have the
expected dimension, and this is the content of the two coincidences) and
`1` at `n = 5`: **`D_5^{det_5}` is a superabundant component of the
50-nodal locus of quintic threefolds, of dimension 76 against the expected
75, the excess being the one condition the fifty nodes fail to impose on
quintics.**  The corresponding tangent-space statement at `n = 5` is the
equality `H^0(I_N(5)) = J_5 = T_F D_5^{det_5}`, both of dimension 77.

**Does any of this threaten Theorem 1?**  No.  Theorem 1 uses only
`def_{2n−5}(N) ≥ 1`, which is proved at every `n ≥ 3` by route (c) with no
saturation hypothesis.  A larger defect in degree `2n − 5` would only raise
the corank in (4.1) and make *smaller* minors vanish — a stronger cap, never
a weaker one.  At `n = 3..6` the measured coranks `6, 31, 102, 256` are
exactly `μ + 1`, so `def_{2n−5} = 1` there and `cap(n)` is the exact rank of
`M_{3n−5}` on `D_5^{det_n}`: the size-`(cap(n)−1)` minors do *not* all
vanish, and the family enters the ideal precisely at degree `cap(n)`.

## 5. The `n = 3` twin, sharpened: `D_5` is the six-nodes-in-general-position locus *(proved, with two exact certificates)*

Paper 1's Question 8.5 asks whether the generic six-nodal cubic threefold is
determinantal.  For nodes in linearly general position the answer is yes.

**Theorem 3.**  Let `W ⊂ P(Sym^3 C^5)` be the closure of the set of cubic
threefolds singular at six points in linearly general position (every five
of them spanning `P^4`).  Then `W = P(D_5^{det_3})`.  In particular the
generic member of `W` is determinantal, every cubic singular at six points
in linearly general position is a limit of determinantal cubics, and
`D_5^{det_3}` is an irreducible component of the closure of the six-nodal
locus.

*Proof.*  Six points of `P^4` in linearly general position form a projective
frame, unique up to `PGL_5`; so `W = closure(PGL_5 · P(V))` with `V` the
space of cubics singular at the standard frame `e_1, .., e_5, e_1 + ... +
e_5`.  The thirty conditions `∇F(p_i) = 0` are linearly independent on the
35 coefficients (rank 30, exact over `Z`, `s40_frame.log`), so `P(V) = P^4`
and `W`, the closure of the image of the irreducible `PGL_5 × P^4`, is
irreducible of dimension `≤ 24 + 4 = 28 = dim P(D_5^{det_3})`.  It remains to
show `P(D_5^{det_3}) ⊆ W`, i.e. that the six nodes of the generic
determinantal cubic form a frame; both sides being irreducible and closed
of dimension 28, equality follows.  On the open subset of the Grassmannian
`Gr(5, M_3)` where `P(L)` meets the Segre in six reduced points, the frame
condition fails on a closed subset (the image, under the proper incidence
correspondence, of "five of the points lie in a hyperplane"), so the frame
condition holds on a dense open subset of the irreducible `Gr(5, M_3)` as
soon as it holds at one `L` — and one exact witness suffices.  Take `L`
spanned by five random integer rank-one matrices `u_i v_i^T`, so that five
of the six Segre points of `P(L)` are its coordinate points; the sixth is
the remaining solution of the nine `2×2` minors, found by a lex Gröbner
basis over `Q` and verified exactly to have rank one:
`(−5160/37469, 3612/57731, 129/148, −129/226, 1)`.  The Hilbert function
of the minor ideal on this `L` is `5, 6, 6, 6, 6` in degrees `1..5` (exact
over `Z`), so `P(L) ∩ Segre` is a zero-dimensional scheme of length six,
exhausted by the six points found, and reduced; and all five coordinates of
the sixth point are nonzero, so every five of the six nodes span `P^4`
(`s40_frame.log`).  Finally, `D_5^{det_3}` is
a component of the six-nodal closure by §4(iii) at `n = 3` (`def_3(N) = 0`:
the incidence variety is smooth at the determinantal point with tangent
space of dimension 28).  ∎

What this gives paper 1: the first sub-question of Question 8.5 is answered
(for nodes in general position), and the hunt for `δ_0` becomes the hunt
for the first covariant vanishing on cubic threefolds singular at a
projective frame — a classical object (the `P^4` of cubics through a fixed
frame contains the Segre cubic, the unique ten-nodal cubic threefold).
Whether the closure of the six-nodal locus has *other* components, with
nodes in special position, is not decided here and is not needed.

## 6. Honest boundary

- **Proved:** Steps 1, 2 (the ODP computation), 3 (routes (a), (b), (c) —
  (c) modulo the adopted GN resolution and its specialisation), the
  bookkeeping of Step 4, the conclusion of Theorem 1, the `n = 2` case, the
  rank formula and closed form for `cap(n)`, the identities of §1 and §4(i),
  §4(ii)'s inequality, §4(iii)'s tangent-space argument, Theorem 3 (with two
  exact certificates whose promotion to the generic case goes in the
  right direction — openness).
- **Adopted from literature:** Kleiman's transversality theorem
  (characteristic 0; the one geometric step, as the brief asked);
  Dimca 2013 Thm 3.1 (statement re-read this session; grading and range as
  quoted); the Gulliksen–Negård resolution and generic perfection; the
  finite-stabiliser dimension count `dim D_5^{det_n} = 3n² + 2` beyond `n =
  4` (used only in §4, where it is also what the measured `dim J_n`
  reports).
- **Measured, both primes, seeds and boxes in the logs:** the coranks
  `6/31/102/256`; the minor-ideal Hilbert functions (equal to GN in every
  degree tested); `def_{2n−5} = 1` and `def_n = C(n−1,4)` at `n = 3..6`
  (upper bounds on the generic values, matched by the proved lower bounds);
  the `n = 3` controls; the `δ = 8` det-side cells of `results/n3_ledger.md`.
- **Expectation, labelled:** Conjecture 2 at `n ≥ 3`; saturation of `J` in
  degree `n` (and hence §4(iii)) for `n ≥ 7`; `def_{2n−5} = 1` exactly for
  `n ≥ 7`.
- **Not done:** no attempt to exhibit the extra syzygy in closed form
  (s35's adjugate candidate); no `n = 4` cells were run (out of scope);
  the `n = 3` census cells above `n_χ = 5000` at `δ = 8` and all of
  `δ ≥ 9` beyond what the ledger lists are named in `results/n3_census.md`,
  not estimated.
- **Regime:** everything here is det-side and permanent-independent; at
  length 5 the padded permanent is washed out (`docs/s35_review.md` §1), so
  nothing in this document bears on the obstruction question in either
  direction.  A bite below the cap would date the *determinant's* first
  five-row equation; it would not be an obstruction.

## 7. One sentence to carry forward

The determinant's first five-row equation at every `n` is capped by one
formula, `cap(n) = 5n(n−1)²(7n−8)/12 = 5, 65, 300, 900, ...`, proved from
`ν(n) = n²(n²−1)/12` nodes that fail forms of degree `2n − 5` by exactly one
(Gulliksen–Negård + Dimca, Kleiman the one adopted step) and now measured
at `n = 3..6`; the conjecture that the cap is the onset is proved at `n = 2`,
survives `δ = 8` at `n = 3`, and dies the day any length-5 cell below 65 (`n
= 3`) or 300 (`n = 4`) bites.
