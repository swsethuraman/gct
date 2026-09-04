# The washout threshold as a function of `m`

Session 48, branch `s48-theorems`, 2026-09-04, off `9aa6a9c`.
Pre-registration `results/PREREG_s48.md` (commit `902cccd`, **before any
Jacobian was computed**).  Code `analysis/wk9_s48_washout.py`,
`analysis/wk9_s48_washout_hi.py`; raw output `results/logs/s48_washout.log`,
`results/logs/s48_washout_hi.log`; table `results/s48_washout.md`.
Labels: **proved** / **measured** / **adopted-from-literature** /
**expectation**, as pre-registered.

## 0. Verdict

> **Theorem C (the washout threshold; both directions).**  Let
> `Phi_{m,r} : (M_m)^r -> Sym^m C^r`, `(A_1..A_r) |-> per_m(sum_i s_i A_i)`,
> and let `D_r^{per_m} = closure(im Phi_{m,r})`.  Put
>
>     orbit(m)  =  2m − 2   (m >= 3),        orbit(2) = 6 .
>
> **(i) Failure direction (proved, no computation).**  For every `m` and every
> `r >= 3`,
>
>     dim D_r^{per_m}  <=  m^2 r − orbit(m) ,
>
> so `Phi_{m,r}` is **not** dominant, and `P_r != R_r`, whenever
> `m^2 r − orbit(m) < C(r+m−1, m)`.
>
> **(ii) Density direction (proved at each `(m, r)` in the verified range).**
> Write `r*(m)` for the largest `r` with `m^2 r − orbit(m) >= C(r+m−1, m)`.
> Then for **every** `(m, r)` with `2 <= m <= 16` and `2 <= r <= r*(m)` the
> Jacobian of `Phi_{m,r}` has full rank `C(r+m−1, m)` at an explicit integer
> point modulo both house primes — which **proves** density (Lemma 1 of
> `docs/washout_lemma.md`; a rank at a point is a *lower* bound on the generic
> rank, the direction that closes).  Hence `D_r^{per_m} = Sym^m C^r` and
> `P_r = R_r` there.  In every case tested the bound of (i) is **attained**:
>
>     dim D_r^{per_m}  =  min( C(r+m−1, m),  m^2 r − orbit(m) )      (measured)
>
> — the counting threshold is sharp, not merely necessary.
>
> **(iii) The threshold.**
>
>     r*(m)  =  4   for  m = 2  and  5 <= m <= 16 ,
>     r*(m)  =  5   for  m = 3, 4 ,
>     r*(m)  =  3   for  m >= 17   (proved for all m >= 17, §3).
>
> **Two corrections to the integrator's table.**  The `m = 2` row read
> `r* = 7`; the truth is `r* = 4`, because `per_2` is a *nondegenerate quadratic
> form in four variables* and every `per_2(A(s))` therefore has rank `<= 4` as a
> quadratic form — a proof, not a count (§2).  And the `deficit` column of that
> table is the naive `C(r+m−1,m) − m^2 r`, which understates the true
> codimension at every `m` because it omits `orbit(m)`: at the programme's own
> case `m = 3`, `r = 6` the naive deficit is 2 and the truth is **6**
> (`dim D_6^{per_3} = 50 < 56`, session 26/37, Theorem 6 of
> `docs/washout_lemma.md`).
>
> **What it means (§5).**  Any length-reduced model must work at length
> `> r*(m)` to see `per_m` at all, and the deficit at `r*(m)+1` measures how
> faintly it first shows.  For the programme's `m = 3` this is length `>= 6`,
> which is where the hunt already is.  This is a limitation on the
> **length-reduced model** — on what a covariant of bounded length can resolve —
> and it is **not** a barrier theorem about GCT, and in particular **not** a
> natural-proofs barrier (§5).

## 1. The two ingredients

`P_r = R_r` requires `{per_m(A(s))}` to be dense in `Sym^m C^r`
(`docs/washout_lemma.md` §3): once `Phi_{m,r}` is dominant, unique
factorisation gives `P_r = closure{l · c : c in Phi_{m,r}((M_m)^r)} = R_r`, and
the permanent has disappeared from the problem.

**Lemma 4 restated (proved; `docs/washout_lemma.md` §4).**  If a group `G` acts
on the source of a polynomial map and leaves it invariant, the generic fibre
contains a `G`-orbit, so `dim im <= dim source − dim(generic orbit)`.

**Proposition 5-general (proved here; the `m = 3` case is s37's Proposition 5,
whose argument is `m`-general verbatim).**  Let
`T = {(D_1, D_2) : D_i diagonal m x m, det D_1 det D_2 = 1}` act on `(M_m)^r`
by `A_i |-> D_1 A_i D_2`.  Since `per(D_1 A D_2) = det D_1 det D_2 per A` for
diagonal `D_i`, `Phi_{m,r}` is `T`-invariant.  `dim T = 2m − 1`; the subgroup
`{(u I, u^{-1} I)}` acts trivially on tuples; and for **every** `r >= 1` the
stabiliser in `T_eff` of a generic tuple is trivial — if `D_1 A_1 D_2 = A_1`
with every entry of `A_1` nonzero then `d_j e_k = 1` for all `j, k`, forcing
`D_1 = d I`, `D_2 = d^{-1} I`.  Hence the generic orbit has dimension
`2m − 2` and

    dim D_r^{per_m}  <=  min( C(r+m−1, m),  m^2 r − (2m − 2) )        (m >= 3).

(Using the full stabiliser of `per_m` instead of its torus part cannot improve
this: for `m >= 3` the linear preservers of the permanent are
`X |-> D P X Q E` and its transpose — Marcus–May, Botta,
**adopted-from-literature** — and the extra factors are finite.)  ∎

Note the sharpness check that was already on file: at `m = 3`, `r = 6` this
reads `54 − 4 = 50`, and the measured Jacobian rank is exactly **50**.

**Lemma 1 restated (proved; `docs/washout_lemma.md` §2).**  A single point with
`rank dPhi = C(r+m−1, m)` proves `Phi_{m,r}` dominant.  A rank modulo `p` at an
integer point is at most the rank over `Q`, so a full rank read modulo `p` is a
proof, not a probability.

**How the Jacobian is computed** (`analysis/wk9_s48_washout.py`).  Since
`per` is linear in each entry,

    d per_m(A(s)) / d (A_k)_{ij}  =  s_k · per_{m−1}( A(s)^{(i,j)} ) ,

so the row space of `dPhi` is `S_1 · span{ q_ij }` with `q_ij = per A^{(i,j)}`
of degree `m − 1`, and

    rank dPhi_{m,r}  =  dim ( S_1 · span{q_ij} )_m  .

The `m^2` sub-permanents are computed by a subset DP over columns (one DP per
deleted row yields all `m` of its minors at once), with homogeneous pieces held
as numpy coefficient vectors modulo `p`.  This shares no code with
`analysis/wk9_s37_jacobian.py`, and it reproduces that script's `m = 3` column
(`4, 10, 20, 35, 50` at `r = 2..6`) exactly.

## 2. `m = 2` is exceptional, and the integrator's first row is wrong *(proved)*

`per_2(A) = a_11 a_22 + a_12 a_21` is a **nondegenerate quadratic form `Q` on
`C^4`** (it is `det_2` after `a_21 |-> −a_21`).  A tuple `(A_1..A_r)` is a
linear map `phi : C^r -> C^4`, and `per_2(A(s)) = phi^*Q`.  A pullback of a
rank-4 quadric has rank `<= 4`.  Hence

    D_r^{per_2}  =  { quadratic forms of rank <= 4 }  ⊊  Sym^2 C^r   for r >= 5,

of dimension `4r − 6` (the rank-`<=k` locus in `Sym^2 C^r` has dimension
`kr − C(k,2)`), and `r*(2) = 4`, **not** 7.  The naive count `4r >= C(r+1,2)`
gives `r <= 7` only because it ignores the stabiliser, which here is `O(Q)` of
dimension **6** — much larger than the `2m − 2 = 2` torus, because `per_2`, alone
among the permanents, is a smooth quadric.  Measured (§4): rank `dPhi_{2,r}` is
`3, 6, 10, 14` at `r = 2, 3, 4, 5`, i.e. exactly `min(C(r+1,2), 4r−6)` for
`r >= 3`.  The `r = 2` entry is 3, not `4·2−6 = 2`: at `r = 2` the map `phi` is
not surjective and its `O(4)`-stabiliser is positive-dimensional — the same
`r = 2` exception that `docs/washout_lemma.md` records for `det_4`.

This was pre-registered as prediction **C3** at prior 0.90 and is confirmed.

## 3. The threshold, and why it stops at 3 *(proved)*

`r*(m) = max{ r : m^2 r − orbit(m) >= C(r+m−1, m) }`.

| `m` | `orbit(m)` | `r*` (sharp) | `r*` (naive count) | first visible at | `dim Sym^m C^{r*+1}` | sharp bound there | **deficit** |
|---|---|---|---|---|---|---|---|
| 2 | 6 | **4** | 7 | 5 | 15 | 14 | **1** |
| 3 | 4 | **5** | 5 | 6 | 56 | 50 | **6** |
| 4 | 6 | **5** | 5 | 6 | 126 | 90 | **36** |
| 5 | 8 | **4** | 4 | 5 | 126 | 117 | **9** |
| 6 | 10 | **4** | 4 | 5 | 210 | 170 | **40** |
| 7 | 12 | **4** | 4 | 5 | 330 | 233 | **97** |
| 8 | 14 | **4** | 4 | 5 | 495 | 306 | **189** |
| 9 | 16 | **4** | 4 | 5 | 715 | 389 | **326** |
| 10 | 18 | **4** | 4 | 5 | 1001 | 482 | **519** |
| 11 | 20 | **4** | 4 | 5 | 1365 | 585 | **780** |
| 12 | 22 | **4** | 4 | 5 | 1820 | 698 | **1122** |
| 13 | 24 | **4** | 4 | 5 | 2380 | 821 | **1559** |
| 14 | 26 | **4** | 4 | 5 | 3060 | 954 | **2106** |
| 15 | 28 | **4** | 4 | 5 | 3876 | 1097 | **2779** |
| 16 | 30 | **4** | 4 | 5 | 4845 | 1250 | **3595** |
| 17 | 32 | **3** | 4 | 4 | 1140 | 1124 | **16** |
| 18 | 34 | **3** | 3 | 4 | 1330 | 1262 | **68** |

The integrator's table is the `r*` column with `orbit = 0`; it agrees for
`3 <= m <= 16` and differs at `m = 2` (§2) and at `m = 17`, where
`17^2 · 4 = 1156 >= 1140 = C(20,17)` but `1156 − 32 = 1124 < 1140`.  Its
deficit column differs everywhere, being `C − m^2 r` rather than
`C − (m^2 r − orbit)`.

**`r*(m) = 3` for every `m >= 17` (proved).**  At `r = 4`,
`m^2·4 − (2m−2) − C(m+3,3) = 4m^2 − 2m + 2 − (m+1)(m+2)(m+3)/6`, which is
`+25` at `m = 16`, `−16` at `m = 17`, and strictly decreasing thereafter (its
difference is `8m + 2 − (m+2)(m+3)/2 < 0` for `m >= 14`), so `r = 4` fails for
every `m >= 17`.  At `r = 3`, `9m^2 − 2m + 2 >= (m+1)(m+2)/2` for every
`m >= 1`, so `r*(m) >= 3` always.  ∎

**`r = 2` is dense for every `m` (proved, no computation).**  Take
`A(s,t) = diag(a_1 s + b_1 t, ..., a_m s + b_m t)`; then
`per_m(A(s,t)) = prod_i (a_i s + b_i t)`, and every binary form of degree `m`
is such a product.  So `D_2^{per_m} = Sym^m C^2` for all `m`.  ∎

## 4. The Jacobian checks *(measured; `results/s48_washout.md`)*

Every `(m, r)` with `2 <= m <= 16` and `r <= r*(m)`, at a random integer point
(box `10^6`), modulo both house primes, with the first failing `r` also read so
the threshold is bracketed on both sides.  In **every** row the measured rank
equals `min(C(r+m−1,m), m^2 r − orbit(m))` at both primes — the two sides of
the sandwich meet, so each is the exact dimension, not a bound:

| `m` | `r` | `m^2 r − orbit` | `dim Sym^m C^r` | rank `dPhi` (both `p`) | dense |
|---|---|---|---|---|---|
| 2 | 4 | 10 | 10 | **10** | yes |
| 2 | 5 | 14 | 15 | **14** | no (codim 1) |
| 3 | 5 | 41 | 35 | **35** | yes |
| 3 | 6 | 50 | 56 | **50** | no (codim 6) |
| 4 | 5 | 74 | 70 | **70** | yes |
| 4 | 6 | 90 | 126 | **90** | no (codim 36) |
| 5 | 4 | 92 | 56 | **56** | yes |
| 5 | 5 | 117 | 126 | **117** | no (codim 9) |
| 8 | 4 | 242 | 165 | **165** | yes |
| 8 | 5 | 306 | 495 | **306** | no (codim 189) |
| 11 | 4 | 464 | 364 | **364** | yes |
| 11 | 5 | 585 | 1365 | **585** | no (codim 780) |
| 12 | 4 | 554 | 455 | **455** | yes |
| 16 | 3 | 738 | 153 | **153** | yes |

(the full 40-row table, including every `m` and every `r` from 2, is
`results/s48_washout.md`.)

Pre-registered prediction **C4** — full rank at every `(m, r)` with
`r <= r*(m)` — is confirmed over the whole verified range, at prior 0.70.
Prediction **C2**, the `orbit(m) = 2m − 2` correction, is confirmed at prior
0.85 and is moreover *sharp*: the bound is attained at every measured `(m,r)`.

**What is not proved.**  Density for `m >= 17` at `r = 3` (and for `m > 16` at
`r <= r*`) is **not** verified: the sub-permanent DP costs `m^2 2^m` and was
out of budget past `m = 16`.  The failure direction of Theorem C is
unconditional in `m`; the density direction is a theorem at each `(m, r)`
actually run, and an **expectation** beyond.  `r = 2` is proved for all `m`
(§3).

## 5. What it means, and what it is not

**The statement.**  Fix `m`.  A covariant of length `k = ell(lam) <= r*(m)`
cannot distinguish the padded permanent `x_0 · per_m` from `l · c` for *any*
cubic-analogue `c`: on such cells `mult_pad = mult_{R_k}`, and `per_m` has been
washed out.  So **any length-reduced model must work at length `> r*(m)` to see
the permanent at all**, and the deficit at `r*(m)+1` — `dim Sym^m C^{r*+1}`
minus `dim D_{r*+1}^{per_m}` — measures how faintly it first shows.  At `m = 3`
that is length `>= 6` with deficit 6; at `m = 4`, length `>= 6` with deficit 36;
for `5 <= m <= 16`, length `>= 5`; for `m >= 17`, length `>= 4`.  The threshold
*falls* with `m`: bigger permanents become visible sooner, because
`dim Sym^m C^r` outruns `m^2 r` faster.

**This is a limitation on the length-reduced model, and nothing stronger.**  It
says what a bounded-length covariant can resolve.  It does not say that no
obstruction exists, it does not bound `mult_pad − mult_det` at lengths above
the threshold, and it is a statement about *this* family of test functions, not
about GCT.  It is **not** a natural-proofs barrier: natural proofs is
constructivity plus largeness, neither of which appears anywhere above.  The
known GCT barriers are Bürgisser–Ikenmeyer–Panova on occurrence obstructions
(no occurrence obstructions for `det` vs padded `per`), which is a different
statement again — about *occurrence*, where this is about a dimension count
that makes the permanent literally absent from the equations.  Pre-registered
as **C5**.

## 6. Literature verdict *(per claim)*

| claim | verdict |
|---|---|
| `per(D_1 A D_2) = det D_1 det D_2 per A` for diagonal `D_i` | classical; **known** |
| linear preservers of `per_m` (`m >= 3`) are `X \|-> D P X Q E` and its transpose | Marcus–May (1962), Botta; **adopted-from-literature** (used only for the remark that the extra factors are finite; the torus part is proved here) |
| the orbit bound `dim D_r^{per_m} <= m^2 r − (2m−2)` | **not found** in the literature in this form; it is s37's Prop. 5 made `m`-general |
| the threshold `r*(m)` and the table of §3 | **not found**.  Searches for permanental analogues of Dixon/Beauville determinantal representations, and for the dimension of `D_r^{per_m}`, return determinantal results only |
| `per_2` is a nondegenerate quadric, so `D_r^{per_2}` is the rank-`<=4` locus | elementary and surely folklore, but **not found stated** as a washout threshold |
| "permanental varieties" of arXiv:2402.17839 (Laubenbacher–Swanson lineage, improving von zur Gathen 1987) | a **different object** — the locus where permanental *minors* vanish, not `closure{per_m(A(s))}`.  No overlap with the threshold above |
| Bürgisser–Ikenmeyer–Panova, no occurrence obstructions | **known**; cited above only to say what this result is *not* |

Pre-registered **C5** put `P(unknown) = 0.6`; the verdict is unknown for the
threshold itself and known for the two classical inputs it uses.
