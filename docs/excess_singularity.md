# Excess singularity cannot separate: a closure result for `n = 4`

Session 48, branch `s48-theorems`, 2026-09-04.  Target D of the session brief.
Pre-registered as **D1** in `results/PREREG_s48.md` at prior 0.5.
Labels: **proved** / **measured** / **adopted**.
Inputs used: the Hilbert function of `Q = J(M)/J_F` measured in session 44
(`docs/sixrow_cap.md` §3), and the Gulliksen–Négård Hilbert function (adopted).

## 0. Statement

> **Proved-vs-measured note (session 49, brief §2.5).**  In the inequality
> `dim (S/J_{pad})_d > dim (S/J_{det})_d` the **pad side is a proved lower
> bound** (`J_F ⊆ (l,c)`, a regular sequence — §1), while the **determinantal
> side is a measured upper bound**: at `d = 6, 7, 8` it is the determinantal
> corank read modulo `p` at random pencils (a mod-`p` corank is an *upper* bound
> on the true corank, the safe direction here), and at `d ≥ 9` it is the
> Gulliksen–Négård value `20d − 20` together with `dim Q_d = 0`, which was
> **measured** in s44 (the six partials generating the full minor ideal from
> degree 9), not proved.  So Proposition D is a theorem **given the s44
> measurements of the determinantal Milnor corank**, and it is a statement about
> the **Macaulay-minor mechanism specifically** — it renames accordingly:

> **Proposition D (the Macaulay-minor mechanism does not separate at `n = 4`;
> proved given the measured determinantal coranks).**
> Fix `4 <= r <= 6`.  Let `F_det = det_4(M(s))` for a generic pencil
> `M(s) = sum_{i=1}^r s_i A_i` of `4x4` matrices, and let `F_pad = l(s)·c(s)` be
> any reducible quartic in `r` variables with `l` linear and `c` cubic, `l ∤ c`
> — in particular the padded permanent `l · per_3(A(s))`.  Then for every
> `d >= 6`
>
>     dim (S/J_{F_pad})_d  >  dim (S/J_{F_det})_d ,
>     equivalently   rank M_d(F_pad)  <  rank M_d(F_det) .
>
> Consequently, for every `d >= 6` and every `k`, a size-`k` minor of the
> Macaulay matrix `M_d` that vanishes identically on `D_r^{det_4}` **also
> vanishes on `R_r` and hence on the padded permanent**.  No such minor is a
> separating equation, in any cell, at any degree.  The threshold `d >= 6` is
> explicit and is the same for `r = 4, 5, 6`.
>
> At `d = 5` the same conclusion holds by measurement (s44: pad corank 136
> against determinantal 126 at `r = 6`); at `d = 4` the two coranks are equal
> (90) and the mechanism produces nothing at all.  So the conclusion is
> **unconditional over the whole range in which the mechanism produces any
> equation**.

## 1. Why: codimension 2 against codimension 4

The mechanism is `docs/sixrow_cap.md` §1: `rank M_d(F) = dim (J_F)_d`, every
`k x k` minor is a degree-`k` form on `Sym^4 C^r`, and a minor vanishes at `F`
exactly when `rank M_d(F) < k`.  Equations for a variety `X` therefore come
from the rank being **small** on `X` — from the Milnor algebra `S/J_F` being
**large**.  So the construction reads excess singularity, and the proposition
says the pad always has more of it than the determinant.

**Pad side (proved).**  Write `F = l·c`.  Then
`d_iF = (d_i l)·c + l·(d_i c) ∈ (l, c)` for every `i`, so `J_F ⊆ (l, c)` and

    dim (S/J_F)_d  >=  dim (S/(l,c))_d  =  C(d+r−2, r−2) − C(d+r−5, r−2) ,

`(l, c)` being a regular sequence (linear, cubic) with Hilbert series
`(1−t^3)/(1−t)^{r−1}`.  Geometrically `Sing(l·c) ⊇ {l = c = 0}`, of
**codimension 2**, so the bound grows like `3 d^{r−3}/(r−3)!`.

**Determinantal side (adopted + measured).**  `Sing(det M) = {rank M(s) <= 2}`
has codimension 4 for a generic pencil, so it is a variety of dimension `r − 5`
and `dim (S/J_{F_det})_d` grows like `d^{r−5}` — two degrees slower.  Exactly:
`dim (S/J_{F_det})_d = H_{S/J(M)}(d) + dim Q_d`, `Q = J(M)/J_F` of finite
length, with `H_{S/J(M)}` the Gulliksen–Négård value and `Q` measured by s44 to
have Hilbert function `10, 30, 46, 41, 12, 1, 0` in degrees `3..9` at `r = 6`.

## 2. The threshold, degree by degree *(proved)*

`padLB(d, r) = C(d+r−2, r−2) − C(d+r−5, r−2)` against the determinantal corank:

| `d` | `r = 6` padLB | `r = 6` det | `r = 5` padLB | `r = 5` det | `r = 4` padLB | `r = 4` det |
|---|---|---|---|---|---|---|
| 4 | 65 | 90 | 31 | 45 | 12 | 19 |
| 5 | 111 | 126 | 46 | 51 | 15 | 16 |
| **6** | **175** | 141 | **64** | 45 | **18** | 10 |
| 7 | 260 | 132 | 85 | 31 | 21 | 4 |
| 8 | 369 | 141 | 109 | 16 | 24 | 1 |
| 9 | 505 | 160 | 136 | 20 | 27 | 0 |
| 10 | 671 | 180 | 166 | 20 | 30 | 0 |

**Monotonicity (proved given the measured `Q_d = 0`), `r = 6`.**  For `d >= 9`
the determinantal corank is exactly `20d − 20` — the Gulliksen–Négård value
`H_{S/J(M)}(d) = 20d − 20` (`d >= 5`, adopted) plus `dim Q_d = 0`, the latter
**measured** in s44 (the six partials generate the full minor ideal from `d = 9`;
this is the measured input the proposition rests on) — so its increment is 20,
while
`padLB(d+1,6) − padLB(d,6) = C(d+4,3) − C(d+1,3) = 146` at `d = 9` and strictly
increasing.  The gap is therefore increasing for `d >= 9`, and `d = 6, 7, 8` are
in the table.  ∎  `r = 5` (determinantal corank constant at 20 for `d >> 0`,
the 20 nodes) and `r = 4` (determinantal corank `h_d`, zero from `d = 9`, the
generic determinantal surface in `P^3` being smooth) are the same argument with
an easier right-hand side.

**Below the threshold.**  At `d = 5, r = 6` the bound gives 111 < 126 and is
simply too weak — the *measured* pad corank is `252 − 116 = 136 > 126` (s44
§5), so the conclusion holds there too, by measurement rather than by the
bound.  At `d = 4` both coranks are 90: the determinantal rank is `rho_4 = 36`
and so is the pad's, no minor vanishes on either, and there is nothing to
separate.

## 3. What this closes

`D(lam, delta) = mult_pad − mult_det > 0` requires an equation vanishing on
`D_r^{det_4}` but **not** on the padded permanent.  Proposition D says every
equation this mechanism produces vanishes on both.  Therefore:

- **No Macaulay-minor construction at `n = 4` can witness `D > 0`**, at any
  Macaulay degree `d`, any minor size `k`, any length `r <= 6`, and any cell —
  not because the minors are weak, but because they read a quantity
  (`dim` of the Milnor algebra) on which the pad is *uniformly larger*.  The
  useful direction is closed off by the sign of a codimension.
- The same argument closes every variant that produces equations from "the
  singular locus is bigger than expected": Jacobian-ideal Hilbert-function
  conditions, Milnor-number conditions.  Any functional that is monotone in
  `dim (S/J_F)_d` inherits the inequality.
  **Correction (s55, applied at merge).**  This clause previously also named
  **Hessian-rank conditions**, and that is refuted.  The LMR / Mignon–Ressayre
  Hessian condition runs the *opposite* way: `rank Hess` on the hypersurface is
  **8** for `det_4` and **9** for `x_0·per_3`, so the determinant is the more
  degenerate one and the condition separates in the useful direction — which is
  exactly why s50's degree-24 evaluation works.  Hessian rank is not monotone in
  `dim (S/J_F)_d`.  There are two families of statistic at `n = 4` and they run
  in opposite directions; this proposition governs only the first.
- s44's asymmetric `d = 5` row is explained rather than merely recorded: the
  minors of `M_5` vanish on pads and not on determinants precisely because the
  inequality already runs the pad's way there, and it always will.
- **It does not** close constructions that read something other than excess
  singularity — anything sensitive to the *structure* of the singular locus
  rather than its size (which component, which multiplicity structure, the
  `GL_r`-module of the equations of `Sing`), nor anything at `n >= 5`, where
  the codimension arithmetic must be redone.

This is a limitation on a family of constructions, not a barrier theorem; the
framing rules of `docs/washout_threshold.md` §5 apply verbatim.

Pre-registered **D1**: written this session, with the degree bound explicit
(`d >= 6`) rather than asymptotic, as the 0.8 sub-prediction anticipated.
