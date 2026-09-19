# B23-03 pre-registration snapshot (written before any computation)

Written 2026-09-18, after `git rev-parse HEAD` = `82633a60893236fab4fbc317df416e1b8a349005`
(tree `e82fd3291d1a2adc8a577647314c251366ff5142`) and `git status --porcelain` = empty were
recorded at 2026-09-18T20:47:28Z. No pilot has run when this file is hashed. Its sha256 is
computed and printed by pilot 1 itself (G25); nothing in this file is edited afterwards.

Conventions (G24). Every dimension is marked **aff** (affine cone in the coefficient space) or
**proj** (its projectivisation, one less). `x = (x1..x5)`; on the hyperplane `H = {l = 0}` we use
coordinates with `l = t = x5`, `y = (x1..x4)`. `D45` = closure of `{det A(x)}` for `A` a `4 x 4`
matrix of linear forms in five variables, 50 aff / 49 proj. `P5 = {l C}`, 39 aff / 38 proj.
`D35` = closure of `{det_3 M(x)}`, 29 aff / 28 proj (B22-10 S24). `D45°` = the set of actual
determinants (no closure). `Sigma_Pi` = cubics containing a plane. `M_k(C)` = the degree-`k`
Macaulay matrix of the five partials of a cubic `C` (`dim S_k` rows, `5 dim S_{k-2}` columns).

## 0. What this slot can and cannot establish

A classification of `D45 ∩ P5` is a statement about a set: it names families, their dimensions,
and what is not excluded. It is **not** an equation, not a separation, not a gap, not a cell. The
cap-minor test (Question A.3) says whether one *mechanism* (rank thresholds of the cubic's
Macaulay matrices) can supply a lift target; it constructs nothing. Question B settles, at named
`(N, k)`, whether the rank-threshold kill of B22-02 rows 1–2 is PROVED or only ASSESSED.
Anything sampled is MEASURED and labelled so; single random points give floors on generic ranks
and on dimensions, never ceilings.

## 1. Theory written before computation

### 1.1 The direct points of `D45 ∩ P5` (hand classification; to be written in full in the report)

Let `F = det A(x) = l C != 0`. Put `l = t`, `A = A_0(y) + t B`, so `det A_0 ≡ 0` (a singular
space of `4 x 4` matrices in four variables). Let `r` be the generic rank of `A_0`.

- `r <= 2`: all `3 x 3` minors of `A_0` vanish, so `t^2 | F`, `C = t Q` contains a hyperplane,
  hence planes: `C ∈ Sigma_Pi`.
- `r = 3`: `adj A_0 = s k kappa^T` with `k`, `kappa` primitive polynomial vectors and
  `deg s + deg k + deg kappa = 3`; `A_0 k = 0`, `kappa^T A_0 = 0`; Jacobi gives
  `C|_{t=0} = tr(adj(A_0) B) = s kappa^T B k`.
  - `deg k = 0` or `deg kappa = 0`: constant kernel, a zero column (row) after constant
    changes of basis, the column of `A` is `t b`, and `F = t det_3 M`: **`C ∈ D35`** (family T1).
  - `deg k = deg kappa = 1`, `s` linear: `C|_{t=0}` is divisible by `s`, so `C` contains the
    plane `{t = s = 0}`: `C ∈ Sigma_Pi`.
  - `(deg k, deg kappa) = (1, 2)` (and `(2, 1)` by transposition): `k = K y`.
    - `rank K = 2`: the first two columns of `A_0` are `c (y2, -y1)`; a `(2,1)` compression
      space; B22-10's template; `C ∈ I(Pi)`, `C ∈ Sigma_Pi`.
    - `rank K = 3`: `A_0 = [[S(u), c(y)], [0, a(y)]]` with `S(u)` the `3 x 3` cross-product
      matrix of three coordinates `u` (the skew-bordered type). Claim: `C` contains a plane,
      namely the cone over `{(u, t) : u x z + t B_11 z = 0}` for a root `z = (z1, z2, 0)` of
      `z^T B_11 z = 0` (after normalising the bottom row to `t e3^T`). So `C ∈ Sigma_Pi`.
    - `rank K = 4`: WLOG `k = y`; every row of `A_0` is `y^T Phi_r` with `Phi_r` skew. This is
      the primitive family **T3** := closure of `GL_5 . { det([y^T Phi_r]_r + t B) }` over all
      `Phi in (Lambda^2)^4`, `B in Mat_4`. The generic `Phi` is equivalent to the normal form
      `A_0(y) v = y' (x) v'' - v' (x) y''` (`y = (y', y'')`, two skew lines).

**Claimed theorem (hand, pre-computation).** `closure(D45° ∩ P5) = T1 ∪ T2 ∪ T3` with
`T1 = {l C : C ∈ D35}`, `T2 = {l C : C ∈ Sigma_Pi}`, `T3` as above; each is irreducible.

**Dimensions claimed before computation.** `T1`: 33 aff / 32 proj (B22-10, replayed here).
`T2`: exactly 35 aff / 34 proj, from `dim Sigma_Pi <= 6 + 25 = 31` aff (hence `T2 <= 35` aff)
and B22-10's Jacobian floor 35 (replayed). `T3`: **at most 29 aff / 28 proj**, because a 13-dim
group (4 shears `y -> y + t c`, `GL_2 x GL_2` on `(y', y'')`, `t -> s t`) acts on the 41-dim
parameter space `GL_5 x Mat_4` freely, and the determinant is constant up to a scalar character
on its orbits (fibres of the affine map `>= 12`).

### 1.2 Predictions and decision rules (Question A)

| # | quantity (pilot 1) | prediction | what each outcome means |
|---|---|---|---|
| A1 | Jacobian rank of the T3 normal-form map (41 params) | **29** | = 29: `dim T3 = 29` aff exactly; < 29: floor only |
| A2 | Jacobian rank of the T3 map with 4 random skew `Phi_r` (65 params) | **29** | > 29 falsifies my normal-form reduction; report it |
| A3 | `rank M_6(C)` for a T3 cubic `C` (mod `2^31-1`) | **210 (smooth)**, uncertain | 210: `C` smooth, so T3 ⊄ T1 ∪ T2 (both lie in the discriminant), PROVED. Else fall back on `rank M_4` |
| A4 | exact `rank M_4`: T1, T2, T3 (two), random cubic | 64, 64, **65**, 65, 65 | T3 at 65: the cap minors are **not** zero on T3's cubics, PROVED from one exact rank |
| A5 | T2 template Jacobian (55 params); `(l, M) -> l det_3 M` Jacobian; orbit rank | 35, 33, 17 | replay of B22-10 |
| A6 | `T1 ⊄ T2` certificate: an S_3-symmetric `D35` cubic with six rank-one points, linearly general, `dim (S/J)_k = 6` at `k = 6, 7` | 6, 6 | Gotzmann persistence gives exactly six reduced singular points, none four coplanar, so no plane: PROVED `D35 ⊄ Sigma_Pi` |
| A7 | the syzygy `sum_{j>=3} g_j d_j C = 0` for `C = x1 q1 + x2 q2`, `g` = the `2 x 2` minors of `(d_j q1, d_j q2)_{j=3,4,5}` | identity holds | sanity check of the hand proof that `rank M_4 <= 64` on all of `Sigma_Pi` |
| A8 | skew-bordered type: `C` vanishes on the claimed plane | identically 0 | sanity check of the hand proof |

**Q3 prediction.** For T1 the cap minors vanish (record's cap theorem, CONDITIONAL as labelled);
for T2 they vanish (PROVED by hand via one extra quadratic syzygy); for T3 they do **not**
(prediction A4). If A3/A4 come out as predicted, the right-way corner of B22-02 Lemma 1.6 does
not survive on `D45 ∩ P5` as a whole.

**Not excluded, stated now.** Points of `D45 ∩ P5` that are limits of determinants without
being determinants themselves (the boundary `D45 \ D45°`). The classification above covers
`closure(D45° ∩ P5)` only.

### 1.3 Question B plan (pilot 2) and decision rule

Padding at `N` is `(z per_3) ∘ T`, so every padding point is a product `l · P` with `P` a cubic.
Hence `J_F ⊆ (l, P)` and, for every padding point,
`rank M_k(F) <= dim S_k - h_N(k)`, `h_N(k) = C(k+N-2, N-2) - C(k+N-5, N-2)` (PROVED; the
B20-02/GKZ Theorem B argument). The global ceilings `N`, `N^2`, `N dim S_2`,
`N dim S_3 - C(N,2)` hold at `k = 3, 4, 5, 6` for every quartic. On the determinant side,
floors come from exact or modular ranks at explicit integer points of `D_N` (lower
semicontinuity), including the monomial-Jacobian points `x1x2x3x4 - x5x6x7x8` (`N = 8`),
`x1x2x3x4 - x5^2 x6 x7` (`N = 7`), `x1x2x3x4 - x5^2 x6^2` (`N = 6`), whose Hilbert functions
are combinatorial for **all** `k`.

**Rule.** The kill is PROVED at `(N, k)` iff (det floor) `>=` min(padding ceiling, global
ceiling). For `k >= k_1(N)` it is proved by the monomial point plus a Newton forward-difference
certificate. Any `(N, k)` left open is reported with its MEASURED values and a price.
**Prediction:** row 1 (`d_1`) closes at `N = 8` for all `k`; at `N = 6, 7` the gradings
`k = 6..8` are the ones at risk. Row 2 (`d_j`, `j >= 2`) is not closed cheaply; it is priced.

### 1.4 Prices

Pilot 1 (Question A): about 5 s, under 100 MB, all matrices at most `330 x 630`.
Pilot 2 (Question B): 20–45 s, under 400 MB. The largest matrices are `3003 x 3234` (`N = 7`,
`k = 8`) and `3432 x 2640` (`N = 8`, `k = 7`), both python-flint `nmod_mat`. Determinant floors
run first and padding measurements only if time remains. Results are written after every
matrix, so a deadline hit keeps what was done. Pilot 3 is held in reserve. Limits are 60 s and
512 MiB each; 3 pilots and 180 s in total.
