# B23-03 — `D45 ∩ P5` classified up to its boundary, and the rank thresholds at `N = 6, 7, 8`

18 September 2026 (UTC). Slot 03, Batch 23. Worktree `work/batch15_workers/B23-03` (on disk
`b23-03`; Windows paths are case-insensitive), branch `b23-03-intersection`. Author: Claude
(Opus 5, 1M context), default permission mode. Theory first. Producer only, unreviewed (G18).

**Provenance, recorded before any write (2026-09-18T20:47:28Z):**

```
git rev-parse HEAD          82633a60893236fab4fbc317df416e1b8a349005   (= the brief's archive commit)
git rev-parse HEAD^{tree}   e82fd3291d1a2adc8a577647314c251366ff5142
git status --porcelain      (empty)
```

Git was used read-only throughout (`rev-parse`, `status`, `show`, `log`, `grep`, `check-ignore`):
no commit, push, stash or checkout.

**Conventions (G13, G23, G24).** Every dimension is marked **aff** (the affine cone in the
coefficient space `Sym^4 C^5 = C^70` or `Sym^3 C^5 = C^35`) or **proj** (its projectivisation,
one less). The ambient is always one of those two spaces, and it is named where it is not
obvious. `D45` = closure of `{det A(x)}`, where `A` is a `4 x 4` matrix of linear forms in
`x = (x_1..x_5)`: 50 aff / 49 proj. `D45°` = the set of actual determinants, with no closure
taken. `P5 = {l C}`: 39 aff / 38 proj. `D35` = closure of `{det_3 M(x)}` in `Sym^3 C^5`:
29 aff / 28 proj. `Sigma_Pi` = cubics containing a plane. `M_k(C)` = the degree-`k` Macaulay
matrix of the five partials of a cubic (`dim S_k` rows, `5 dim S_{k-2}` columns). The cap minors
are the `65 x 65` minors of `M_4` (`70 x 75`). `delta_0` is not used anywhere (G13).

## Plain terms, up front

**Question A.** Every point of `D45 ∩ P5` that is an actual determinant lies in one of **two**
irreducible families, and both are needed:

- **T1** = `{l C : C ∈ D35}`, **33 aff / 32 proj**;
- **T2** = `{l C : C contains a plane}`, **35 aff / 34 proj** (exact, not just `>= 35`).

Neither contains the other. The certificate that `D35` is not inside the plane family is new
here (§2.4). The classification is by hand, self-contained, and uses no Eisenbud–Harris or
Atkinson. It also finds the primitive space B22-10 asked about: a third family **T3**
(29 aff / 28 proj) coming from a genuinely non-compression space of `4 x 4` matrices. **T3 lies
inside T2** (§2.3). My pre-registered prediction was that T3's cubic is smooth; that was
**falsified** by pilot 1 (its cubics are singular with a length-10 singular profile). The
theorem `T3 ⊆ T2` was found after that and proved by hand.

**The consequence (A.3): the right-way corner survives.** The cap minors vanish on *every*
cubic through a plane, PROVED by hand from one extra quadratic syzygy (§2.5). Before this slot
that rested on one random rank. On `D35` they vanish under the record's cap theorem (CONDITIONAL
as labelled there). They are nonzero at every smooth cubic. So on the closure of the determinant
points of `D45 ∩ P5`, the Nullstellensatz lift of B22-02 row 13 has a rank-threshold target,
`I(D35 ∪ Sigma_Pi)`. **What is not excluded:** points of `D45 ∩ P5` that are limits of
determinants without being determinants (§2.6). If one of those is a smooth `l C*`, the corner is
gone again. Nothing here rules that out.

**Question B.** Row 1 of B22-02 (rank thresholds of `d_1`) is now a **PROVED-kill at
`N = 6, 7, 8` for every `k`**. Padding's `rank M_k` is `<=` the determinant's with proved
margins of 0 at `k <= 5` and of `+34 .. +467` at `k = 6..8`, and `>= +11, +119, +69` for all
larger `k`. Row 2 (`d_j`, `j >= 2`) is **not** closed. For `j >= N - 3` the rank-threshold ideal
is zero, CONDITIONAL as in B20-02. For `2 <= j <= N - 4` it is open and priced (§3.3).

Two wrapped pilots were used of three (16.0 s of 180 s). Nothing here is a gap, a cell or an
equation.

## 0. What this slot can and cannot establish

A classification of `D45 ∩ P5` is a statement about a **set**. It names families, gives exact
dimensions and names what is not excluded. It is not an equation of `D45`, not a separation,
not a gap and not a cell. The cap-minor test asks whether one mechanism (rank thresholds of the
cubic factor's Macaulay matrices) can supply a lift target. It constructs no lift. Question B
settles, at named `(N, k)`, whether the kill of B22-02 rows 1–2 is PROVED or only ASSESSED. It
produces no equation. Every sampled number is labelled MEASURED. A rank at one random point is
a floor for the generic rank and never a ceiling; every ceiling below is proved.

## 1. Pre-registration

The snapshot `results/b23_03/preregistration_snapshot.md` (sha256
`3cb7b7c9c80e5dd9ef739b0d3a53d23c4e20a9123a06de0059c85555851b08df`) was written and hashed
before any computation. **Its hash is printed by pilot 1 itself** (the first line of its
stdout and the field `prereg_sha256` of `p1_classification.json`), and the wrapper's
`started_utc` of 20:51:29Z orders it (G25). It holds §0 above, the hand classification of §2.1
up to the rank-`K = 4` case, the dimension ceilings, and predictions A1–A8 and the Question B
rule with prices.

An addendum, `results/b23_03/addendum_before_p2.md` (sha256
`b184f4bfcadef6fffc59c5ec23c68e7921e9bcd44587dadc17b72f278f1b30b3`, printed by pilot 2),
records what pilot 1 falsified and the theorem `T3 ⊆ T2` found afterwards. Both files are
unedited.

**Predictions against outcomes (each copied from the pilot outputs):**

| # | predicted | outcome | verdict |
|---|---|---|---|
| A1 | T3 normal-form Jacobian rank 29 | 29 (41 params) | confirmed |
| A2 | T3 random-`Phi` Jacobian rank 29 | 29 (65 params) | confirmed |
| A3 | a T3 cubic is smooth (`rank M_6 = 210`) | corank 10 at every `k = 2..7`, at 4 of 4 points | **falsified** |
| A4 | exact `rank M_4`: 64, 64, 65, 65, 65 (T1, T2, T3, T3, random) | 64, 64, **60, 60**, 65 | **falsified for T3** |
| A5 | 35, 33, 17 (replays) | 35 (template), 35 (via `Sigma_Pi`), 33, 17 | confirmed |
| A6 | `T1 ⊄ T2` certificate with coranks 6, 6 | pilot 1: **not obtained** (S_3-symmetric points are singular along curves: coranks 17, 21, 25, 29). Pilot 2, new construction: coranks 6, 6, 6, 6 at `k = 4..7` | obtained in pilot 2 |
| A7 | the `Sigma_Pi` syzygy identity | holds (random point and witness) | confirmed |
| A8 | the skew-bordered cubic vanishes on the claimed plane | holds (2 of 2) | confirmed |
| B | row 1 closes at `N = 8`; `N = 6, 7` at risk at `k = 6..8` | closes at all three `N`, every `k` | better than predicted |

**Deviations, disclosed.** (1) Pilot 2 was pre-registered for Question B only. It also carried
the corrected A6 certificate and a check of `T3 ⊆ T2`, recorded in the addendum before it ran.
(2) Two interpreter invocations ran outside the wrapper during inspection, one executing
`print('x')` and one with an empty program. Neither computed anything on the objects under
study, so neither is a numerical run under G19's definition (B21-10 R22). Both are listed in §6
anyway.

## 2. Question A — `D45 ∩ P5`

### 2.1 The direct points: a complete case analysis (PROVED, by hand)

Let `F = det A(x) = l C != 0` be an actual determinant in `P5`. Choose coordinates with
`l = t = x_5` and `y = (x_1..x_4)` on `H = {t = 0}`, and write `A = A_0(y) + t B` with `B`
constant. Then `det A_0 ≡ 0`: `A_0` is a linear space of singular `4 x 4` matrices in four
variables. Let `r` be its generic rank. **Jacobi's formula gives
`C|_{t=0} = tr(adj(A_0) B)`**, the key identity used throughout.

**(a) `r <= 2`.** All `3 x 3` minors of `A_0` vanish, so `t^2 | F`. Then `C = t Q` contains a
hyperplane, hence planes, and **`C ∈ Sigma_Pi`**.

**(b) `r = 3`.** `adj(A_0)` is a nonzero polynomial matrix of rank 1. Over the UFD `C[y]` it
factors as `adj(A_0) = s k kappa^T`, where `k` and `kappa` are primitive vectors and `s` is a
polynomial, and by homogeneity `deg s + deg k + deg kappa = 3`. `A_0 adj(A_0) = 0` gives
`A_0 k = 0` and `kappa^T A_0 = 0`, and `C|_{t=0} = s kappa^T B k`.

- **`deg k = 0` (or `deg kappa = 0`).** A constant kernel vector: after constant column
  operations the fourth column of `A_0` is zero, so the fourth column of `A` is `t b`. `b != 0`,
  since otherwise `F = 0`. Row operations make it `t e_4`, and `F = t det_3 M` with `M` the
  remaining `3 x 3` block (linear in all five variables). **`C ∈ D35°`.** (Transpose for
  `deg kappa = 0`.) This is B22-02's block-diagonal family.
- **`deg k = deg kappa = 1`, `s` linear.** `s | C|_{t=0}`, so `C` vanishes on the plane
  `{t = s = 0}`: **`C ∈ Sigma_Pi`**.
- **`(deg k, deg kappa) = (1, 2)`**, `s` constant. The case `(2, 1)` is its transpose, and
  transposition preserves `det`. Write `k = K y` with `K` a constant `4 x 4`. `K` has rank at
  least 2, because a rank-1 `K` makes `k` non-primitive.
  - **`rank K = 2`.** In adapted coordinates `k = (y_1, y_2, 0, 0)`, so
    `y_1 a_1(y) + y_2 a_2(y) = 0` for the first two columns. By the Koszul relation of
    `(y_1, y_2)` those columns are `c (y_2, -y_1)` with `c` constant, and row operations make
    `c = e_1`. `A_0` then has a `3 x 2` zero block: the **`(2,1)`-compression space**. Normalising
    `A`'s block `t R` (`R` a constant `3 x 2`) gives three sub-cases.
    - `rank R = 2`: B22-10's template
      `[[a11..a14], [t, 0, D11, D12], [0, t, D21, D22], [0, 0, D31, D32]]`, with
      `C = D32 Q1 - D31 Q2` in the ideal `(D31, D32)`. `C` contains the plane
      `{D31 = D32 = 0}`, or a hyperplane if those forms are dependent.
    - `rank R = 1`: `C` = (linear form)·(`2 x 2` determinant) contains a hyperplane.
    - `R = 0`: `F = 0`.

    In every case **`C ∈ Sigma_Pi`**.
  - **`rank K = 3`.** In adapted coordinates `k = (u, 0)` with `u = (y_1, y_2, y_3)` and
    `w = y_4`. Each row of the first three columns satisfies `row(y)·u = 0` identically, which
    forces `row = (s_r x u)^T`, independent of `w`. If the `s_r` span at most 2 dimensions, row
    operations give a `2 x 3` zero block. That is a `(1,2)`-compression, the transpose of the
    previous case, and **`C ∈ Sigma_Pi`**. If they span 3, then
    `A_0 = [[S(u), c(y)], [0, a(y)]]` with `S(u)` the cross-product matrix. This is the
    **skew-bordered type**, **proved in §2.2 to lie in `Sigma_Pi`**.
  - **`rank K = 4`.** Taking `k = y`, each row is `y^T Phi_r` with `Phi_r` skew. This is the
    primitive family **T3**, which **§2.3 proves lies in T2**.

**Theorem 2.1 (PROVED, by hand).** `closure(D45° ∩ P5) = T1 ∪ T2`, where
`T1 = {l C : C ∈ D35}` and `T2 = {l C : C ∈ Sigma_Pi}`.

*Proof.* The case analysis puts every point of `D45° ∩ P5` into T1 or T2; §§2.2–2.3 supply the
two sub-cases deferred there. Conversely, `T1 ⊆ D45` by `l det_3 M = det_4 diag(l, M)`. For
T2, the template family is contained in T2 and its closure is irreducible of dimension
`>= 35` aff (§2.4). T2 is irreducible of dimension `<= 35` aff (§2.4). So the two are equal,
and `T2 ⊆ D45`. ∎

(The cases fit B22-10's reading. The `(1,3)/(3,1)` compressions, which are the zero-row and
zero-column cases, give `D35`, and the `(2,1)/(1,2)` compressions give the plane family. B22-10
did not settle whether primitive rank-3 spaces contribute. They do: the skew-bordered type and
T3 both give direct points, and both lie in T2.)

### 2.2 The skew-bordered type lies in `Sigma_Pi` (PROVED, by hand; sanity-checked in pilot 1)

`A = [[S(u) + t B_11, c(x)], [t b^T, a(x)]]`. If `b = 0`, then `C = a · det(S(u) + tB_11)/t`
contains a hyperplane. Otherwise conjugating by `(g, g^T)` on the `3 x 3` block preserves the
form, since `g S(u) g^T = S(det(g) g^{-T} u)`, and makes `b = e_3`. Let `N(u,t)` be the `4 x 3`
first-three-columns matrix. Each of its maximal minors is divisible by `t`, and
`F = det[N | (c; a)]` gives `C = sum_r ± (c; a)_r Q_r(u, t)` with `Q_r = minor_r(N)/t`.

Pick `z = (z_1, z_2, 0) != 0` with `z^T B_11 z = 0`. That is a binary quadratic, so it always
has a root. The linear map `(u, t) -> u x z + t B_11 z` has image in `z^perp`, which is
2-dimensional, and already has rank 2 on `u`. So its kernel `L_z` is 2-dimensional and not
contained in `{t = 0}`. On `L_z`, `N z = 0`, so `t Q_r = 0` and hence `Q_r = 0`. Therefore `C`
vanishes on the plane `{(u, t, w) : (u, t) ∈ L_z}`. ∎ Pilot 1 E5 checked the identity at two
integer points with `z = e_1` (`C_on_plane_identically_zero: true`, twice).

### 2.3 T3: the primitive family (dimension 29 aff / 28 proj; T3 ⊆ T2)

**Normal form.** Write `C^4 = U' ⊕ U''` with `y = (y', y'')`, and define
`A_0(y) v = y' ⊗ v'' - v' ⊗ y''` in `U' ⊗ U''`. This is the space of lines meeting two skew
lines. Its kernel is `y`, its left kernel is the quadratic `y' ⊗ y''`, and
`det A_0 ≡ 0`. It is **not** a compression space: a direct check rules out each of the types
`(0,3), (1,2), (2,1), (3,0)`. Pilot 1 E1 confirmed `A_0 y = 0`, `det A_0 = 0`, and that the
columns of `adj A_0` are proportional to `y`.

**T3 is the whole rank-`K = 4` case.** Take four skew `Phi_r`, the rows of `A_0`, and let
`R = span(Phi_r)`. For generic `Phi`, `R^perp` (under the wedge pairing) is a pencil that meets
the Klein quadric in two decomposable forms `a_1 ∧ b_1` and `a_2 ∧ b_2`, since a generic line
meets a quadric twice. These four covectors are a basis, so a change of basis makes the pencil
`<e_12, e_34>` and `R = <e_13, e_14, e_23, e_24>`, which is the normal form. Non-generic
`Phi` are limits. So T3 := `closure(GL_5 . {det(A_0^{std}(y) + t B)})` is irreducible and
contains every rank-`K = 4` direct point.

**Dimension: exactly 29 aff / 28 proj.**
- *Ceiling (PROVED).* A 13-dimensional subgroup of `GL_5` acts freely on the 41-dimensional
  parameter space `GL_5 x Mat_4`. It consists of the shears `y -> y + t c` (4), `GL_2 x GL_2`
  on `(y', y'')` (8), and `t -> s t` (1). The identities are
  - `F_{B + A_0(c)} = F_B ∘ σ_c`;
  - `F_B(g y, t) = χ(g) F_{B'}(y, t)` with `B' = (g' ⊗ g'')^{-1} B g`, because
    `A_0(g y) = (g' ⊗ g'') A_0(y) g^{-1}`;
  - `F_B(y, s t) = F_{s B}(y, t)`.

  Hence fibres of the projectivised map are `>= 13`-dimensional, the projective dimension is at
  most 28, and the affine dimension at most 29.
- *Floor (CERTIFIED).* The Jacobian has exact rank **29** over `Q` at an integer point. Pilot 1
  E2 gave 29 for the normal form (41 params) and 29 with four random skew `Phi` (65 params).

**Theorem 2.3 (PROVED, by hand, found after pilot 1). T3 ⊆ T2.** Take `phi = alpha ⊗ beta` in
`(U' ⊗ U'')^*`. The row functional is
`phi(A(x) v) = alpha(y') beta(v'') - alpha(v') beta(y'') + t phi(B v)`, so its `v'`-part is
`-beta(y'') alpha + t (B^T phi)'` and its `v''`-part is `alpha(y') beta + t (B^T phi)''`.
Suppose `(B^T phi)' = c_1 alpha` and `(B^T phi)'' = c_2 beta`. Then both parts vanish on the
3-dimensional subspace `P_phi = {beta(y'') = c_1 t, alpha(y') = -c_2 t}`, which is not inside
`{t = 0}`. So `phi` is a constant left kernel of `A` on `P_phi`, `det A = 0` there, and `C`
contains the plane `P(P_phi)`.

The two conditions on `(alpha, beta)` in `P^1 x P^1` have bidegrees `(2, 1)` and `(1, 2)`, with
intersection number `2·2 + 1·1 = 5 > 0`. So a solution exists for **every** `B`: generically
five, and a whole curve or the whole space if the forms share a component or vanish. So every
normal-form cubic is in `Sigma_Pi`. Because the normal forms are dense in T3 and T2 is closed,
T3 ⊆ T2. ∎ Pilot 2 F2 checked the identity at two integer `B` whose row 0 is `(c_1, 0, c_2, 0)`
(`C_vanishes_on_plane: true`, twice).

**What T3's cubics look like (MEASURED, not used).** At four T3 points,
`dim (S/J_C)_k = 10` for every `k = 2..7` (mod `2^31 - 1`) and the exact `rank M_4 = 60`. That
is the Hilbert function of a length-10 singular scheme, the Segre-cubic profile. The Segre
cubic is itself determinantal, so T3 is probably also inside T1. That is not claimed, and
nothing depends on it.

### 2.4 The two components: dimensions, irreducibility, and `T1 ⊄ T2`

| family | construction | dimension | irreducible | how the dimension is known |
|---|---|---|---|---|
| `D35` | closure of `{det_3 M(x)}` | **29 aff / 28 proj** | yes | B22-10 S24; orbit rank 17 replayed (pilot 1 E2) |
| **T1** | `{l C : C ∈ D35}`, i.e. `det_4 diag(l, M)` | **33 aff / 32 proj** | yes (image of `C^5 x D35`) | Jacobian rank 33 (floor) and `50 - 17 = 33` (ceiling), both replayed exactly |
| `Sigma_Pi` | cubics containing a plane; closed, the image of a rank-25 bundle over `Gr(3,5)` | **31 aff / 30 proj** | yes | ceiling `6 + 25 = 31`; exactness follows from T2's floor |
| **T2** | `{l C : C ∈ Sigma_Pi}`, the closure of B22-10's `(2,1)`-compression template | **35 aff / 34 proj** | yes | ceiling `5 + 31 - 1 = 35`; floor: template Jacobian rank 35 (exact, pilot 1 E2); independently `(l, m_1, m_2, q_1, q_2) -> l(m_1 q_1 + m_2 q_2)` has rank 35 |
| T3 | §2.3, primitive | **29 aff / 28 proj** | yes | §2.3; **contained in T2** |
| skew-bordered | §2.2 | not computed (not needed) | yes | **contained in T2** |

**`T2 ⊄ T1`** follows from the dimensions (35 > 33, both aff).

**`T1 ⊄ T2` (PROVED; certificate in pilot 2 F1).** Take two rank-one decompositions
`X = sum_{i<=3} u_i v_i^T = sum_{j<=3} w_j z_j^T` of one invertible integer `3 x 3` matrix,
using unimodular `U` and `W`. The six rank-one matrices `u_i v_i^T` and `-w_j z_j^T` sum to
zero. Set `M(x) = sum_{i<5} x_i R_i` and `C = det M ∈ D35`. The six rank-one points are
`e_0, ..., e_4` and `-(1, ..., 1)`. They are in linearly general position: no coordinate of the
sixth point vanishes, and `LGP_all_5_subsets_det_nonzero: true`. Each is a node (Hessian ranks
4, 4, 4, 4, 4, 4). Pilot 2 gave `dim (S/J_C)_k = 6, 6, 6, 6` at `k = 4..7` mod `P`; a modular
corank is `>=` the rational one, and six distinct singular points force `>= 6`, so the rational
value at `k = 7` is exactly 6.

Suppose `C` contained a plane `Pi = {m_1 = m_2 = 0}`. Then `C = m_1 q_1 + m_2 q_2` and
`J_C ⊆ I_Z` with `Z = V(m_1, m_2, q_1, q_2) ⊂ Pi`, while also `J_C ⊆ I_{pts}`.
- If `Z` is infinite, or contains a point outside the six, or a non-reduced point, then the
  scheme `Z ∪ pts` has a curve component or length `>= 7`. That gives
  `dim (S/J_C)_7 >= 7`, a contradiction. (A zero-dimensional scheme of length `L` imposes `L`
  conditions in degree `>= L - 1`; a curve imposes at least 8 in degree 7. Both are
  UNREAD-CLASSICAL.)
- So `Z` is a length-4 subscheme of six reduced points: four of them, and they are coplanar.
  That contradicts linear general position.

Hence `C ∉ Sigma_Pi`. `D35` is irreducible and `Sigma_Pi` closed, so `D35 ⊄ Sigma_Pi`. Unique
factorisation then gives `T1 ⊄ T2`: `C` is irreducible, because a reducible cubic is singular
along a curve. ∎

(Pilot 1's first attempt used S_3-symmetric configurations. They are singular along curves
(coranks 17, 21, 25, 29; Hessian rank 3) and certify nothing. They are disclosed, not used.)

**Record lines corrected (G24).** The record's own dimension line disagrees with this slot in
the places below. Each is stated explicitly.

1. **The brief's line** "that family has **projective** dimension `>= 35` against exactly 33 for
   the `D35` family" mislabels both numbers. B22-10's 35 and 33 are Jacobian ranks of affine
   maps, so both are **affine**. Corrected: **35 aff / 34 proj (exact)** against **33 aff /
   32 proj (exact)**.
2. **B22-10 §1 vs §7.** §1 says the record's 32 is "off by one"; §7 says "wording only". The
   second is right: B22-02's 32 is the correct **projective** value (33 aff). The defect was
   quoting it beside `dim D45 = 50` (aff), not an arithmetic error.
3. **B22-10 §7 / S23**, "family dimension `>= 35`" → **exactly 35 aff / 34 proj**.
   "Cubics through a plane form a 31-dimensional affine family" (stated there as an expected
   count) → **PROVED: 31 aff / 30 proj**.
4. **B22-10 §7**, "the cap minors do vanish on the plane family too (rank 64 there, pilot 2)".
   That was one MEASURED rank, and a single point cannot bound the generic rank from above.
   It is **now PROVED for every member (§2.5)**.
5. **B22-02 row 13**, "`D45 ∩ P5` … contains `{l C : C ∈ D35}` of dimension 32; whether it is
   larger is open". It is larger (B22-10), and its determinant part is now determined: T1 ∪ T2.

### 2.5 The cap-minor test, family by family (A.3)

The cap minors vanish at `C` iff `rank M_4(C) <= 64`. At every smooth cubic
`rank M_4 = 70 - 5 = 65`: the partials form a regular sequence, whose Hilbert function is
`(1 + t)^5`, so this holds at **every** smooth cubic (PROVED).

**Proposition 2.5 (PROVED, by hand). `rank M_4(C) <= 64` for every `C ∈ Sigma_Pi`, with generic
value exactly 64.** Write `C = x_1 q_1 + x_2 q_2`. For `j = 3, 4, 5`,
`d_j C = x_1 d_j q_1 + x_2 d_j q_2`. Let `g = (M_45, -M_35, M_34)`, where `M_jk` are the
`2 x 2` minors of the `2 x 3` matrix `(d_j q_1, d_j q_2)_{j = 3,4,5}`. Then
`sum_{j>=3} g_j d_j C = 0`, a syzygy with quadric coefficients.

Assume the partials are independent. Then the 10 Koszul syzygies are independent, and any
combination of them with `g_1 = g_2 = 0` has all its components in `(x_1, x_2)`. So `g` is
**not** Koszul whenever `M_45` has a monomial free of `x_1, x_2`. That gives
`dim ker M_4 >= 11` and `rank <= 64`.

Both conditions are open and hold at the witness `q_1 = x_3^2 + x_4^2`, `q_2 = x_5^2 + x_3 x_4`
(disjoint monomial supports, so the partials are independent, and `M_45 = 4 x_4 x_5`). They
therefore hold on a dense subset of `(x_1, x_2)_3`. The closed condition `rank <= 64` extends to
all of it, and by `GL_5` to all of `Sigma_Pi`. ∎

Pilot 1 E4 checked the identity at a random point and at the witness, and confirmed the witness
conditions (partials rank 5; `g0_has_monomial_free_of_x0_x1: true`). A random plane cubic has
exact rank 64, so generic rank `>= 64` (pilot 1 E6), and with the ceiling it is exactly 64.

| family | cap minors vanish on it? | label |
|---|---|---|
| T1 (`D35`) | yes | CONDITIONAL on the record's cap theorem at `n = 3` (`onset_conjecture.md` Theorem 1, "modulo Kleiman, Dimca, Gulliksen–Negård, all adopted"; B22-10 S18's Dimca instance). MEASURED 64 at a random point (pilot 1 E6) and at the pilot 2 F1 cubic (corank 6 at `k = 4`) |
| T2 (`Sigma_Pi`) | **yes, every member** | **PROVED** (Prop. 2.5) |
| T3 | yes | PROVED (T3 ⊆ T2); MEASURED exact rank 60 |
| skew-bordered | yes | PROVED (⊆ T2); MEASURED 63 and 59 at two points |

**So the right-way corner survives** on `closure(D45° ∩ P5)`. For any fixed `l`, the cubics
`{C : l C ∈ T1 ∪ T2}` are exactly `D35 ∪ Sigma_Pi`: another factorisation `l C = l' C'` with
`l' ≠ l` makes `l' | C`, and then `C` contains a hyperplane. The cap minors lie in
`I(D35 ∪ Sigma_Pi)` (the `D35` half is CONDITIONAL as labelled) and are nonzero at every smooth
cubic. A Nullstellensatz lift therefore has a rank-threshold target on the determinant part.
This strengthens B22-02 Lemma 1.6 as B22-10 anticipated:
`deg f >= onset I(D35 ∪ Sigma_Pi)`. It constructs no lift, and Lemma 1.4's kill of covariant
lifts is untouched.

### 2.6 What is not excluded (named gaps)

- **G-A1 — the boundary.** Theorem 2.1 is about `closure(D45° ∩ P5)`. A point of `D45 ∩ P5`
  outside T1 ∪ T2 would have to lie in `(D45 \ D45°) ∩ P5`: a limit of determinants that is
  itself no determinant. Nothing here excludes such points. By the affine dimension inequality
  in `C^70`, any component they form has dimension `>= 50 + 39 - 70 = 19` aff. **This is the gap
  that decides A.3 in full:** a boundary point `l C*` with `C*` smooth would put a smooth cubic
  in the lift's projection, and no Macaulay-rank threshold would then separate. *Reopening
  condition:* a proof that `D45°` is closed (every limit of `4 x 4` linear determinants in five
  variables is one), or a description of the boundary meeting `P5`. No such statement is on the
  record, and I have not attempted one.
- **G-A2.** The T1 clause of §2.5 rests on the record's cap theorem, as labelled there.
- **G-A3.** Whether `T3 ⊆ T1` (the MEASURED Segre profile suggests yes). It is irrelevant to
  the classification.

## 3. Question B — the rank thresholds at `N = 6, 7, 8`

### 3.1 The argument (all ceilings PROVED)

**Padding ceiling.** Every padding point `(z per_3) ∘ T` is a product `l P` with `P` a cubic.
Then `d_i(l P) ∈ (l, P)`, so `rank M_k(F) <= dim S_k - h_N(k)` with
`h_N(k) = C(k+N-2, N-2) - C(k+N-5, N-2)`, the Hilbert function of `S/(l, P)` when `l ∤ P`. If
`l | P` the quotient is larger and the bound only improves. This is the B20-02 / GKZ Theorem B
argument, and it holds on the larger set of **all** products `l C` in `N` variables, so the
distinction between `(z per_3) ∘ T` and `l C` does not matter for it.

Universal ceilings hold for every quartic: `N`, `N^2` and `N dim S_2` at `k = 3, 4, 5` (the
column count), and `N dim S_3 - C(N,2)` at `k = 6` (the Koszul relations are independent when
the partials are; otherwise the rank is `<= (N - 1) dim S_3`, which is smaller). Padding
ceiling = the minimum of the two.

**Determinant floors.**
- *`k = 3..8` (`N = 8`: `3..7`).* Modular rank of `M_k` at a random integer point of `D_N`
  (lower semicontinuity).
- *All larger `k`.* The monomial-Jacobian points
  `F_0 = x1x2x3x4 - x5x6x7x8` (`N = 8`), `x1x2x3x4 - x5^2 x6 x7` (`N = 7`) and
  `x1x2x3x4 - x5^2 x6^2` (`N = 6`). Each is the determinant of
  `[[x1,0,0,o1],[o2,x2,0,0],[0,o3,x3,0],[0,0,o4,x4]]`, so each lies in `D_N`. Its Jacobian ideal
  is monomial, so its Hilbert function is exact for every `k`:
  `H(k) = sum_a A(a) B_N(k - a)`, with `A(0) = 1` and `A(a) = 6a - 2`. Pilot 2 checked this
  against brute-force enumeration for `k = 0..7` and against `rank M_k(F_0)` for `k = 3..6`.
- *Certificate.* `D(k) = h_N(k) - H(k)` is a polynomial of degree `<= 5` on `k >= k_1`. That
  holds because `h_N` is polynomial for `k >= 0`, and a convolution of eventually-polynomial
  sequences is polynomial once past the exceptional initial terms (`k >= 4` here). The Newton
  expansion `D(k) = sum_i e_i C(k - k_1, i)` with every `e_i >= 0` then gives
  `D(k) >= e_0 > 0` for all `k >= k_1`.

### 3.2 Results (copied from `p2_certificates_and_thresholds.json`)

| `N` | `k` | padding ceiling (proved) | det floor (mod `P`) | proved margin | padding (MEASURED, random point) |
|---|---|---|---|---|---|
| 6 | 3 / 4 / 5 | 6 / 36 / 126 | 6 / 36 / 126 | 0 / 0 / 0 | 6 / 36 / 116 |
| 6 | 6 / 7 / 8 | 287 / 532 / 918 | 321 / 660 / 1146 | **+34 / +128 / +228** | 271 / 526 / 917 |
| 6 | `>= 9` | `dim S_k - h_6(k)` | `F_0`: `dim S_k - H(k)` | `>= 11` (Newton at `k_1 = 9`: `e = 11, 50, 21, 3, 0, …`) | — |
| 7 | 3 / 4 / 5 | 7 / 49 / 196 | 7 / 49 / 196 | 0 / 0 / 0 | 7 / 49 / 181 |
| 7 | 6 / 7 / 8 | 518 / 1050 / 1968 | 567 / 1279 / 2435 | **+49 / +229 / +467** | 477 / 1023 / 1944 |
| 7 | `>= 9` | `dim S_k - h_7(k)` | `F_0` | `>= 119` (`k_1 = 9`: `e = 119, 216, 117, 30, 3, 0, …`) | — |
| 8 | 3 / 4 / 5 | 8 / 64 / 288 | 8 / 64 / 288 | 0 / 0 / 0 | 8 / 64 / 267 |
| 8 | 6 / 7 | 876 / 1926 | 932 / 2248 | **+56 / +322** | 774 / 1803 |
| 8 | `>= 8` | `dim S_k - h_8(k)` | `F_0` | `>= 69` (`k_1 = 8`: `e = 69, 420, 371, 163, 36, 3, 0, …`) | — |

At `k <= 2`, `M_k` has no columns. At `k = 3..6` the determinant floor equals the universal
ceiling, so the determinant's rank is exactly the global maximum there. The margins at
`k = 3..5` are ties: padding cannot exceed the determinant, and no equation can separate.

**Theorem 3.2 (PROVED).** For `N = 6, 7, 8` and every `k >= 0`, `r_k(P_N) <= r_k(D_N)`. Hence
every `(r_det(k) + 1)`-minor of `M_k` vanishes on padding. **B22-02 row 1 is a PROVED-kill in
the whole window `N = 5..8`**: at `N = 5` by GKZ Theorem B (record), and at `N = 6, 7, 8` here.
It no longer carries B22-10's ASSESSED label.

The only premises are the elementary padding ceiling, the certified modular floors at explicit
integer points, the combinatorial Hilbert functions of the `F_0` (with the brute-force
cross-check), and the Newton certificate. No Kleiman, Dimca, Gulliksen–Negård or depth
sensitivity is used. The MEASURED padding ranks lie below the ceilings, so the true margins are
larger. For example, at `(N, k) = (7, 8)` the measured padding rank is 1944 against the
determinant's 2435.

### 3.3 Row 2 (`d_j`, `j >= 2`): not closed, and what it would cost

- **`j >= N - 3` (`j >= 3, 4, 5` at `N = 6, 7, 8`).** If `grade J_det = 4`, depth sensitivity
  kills Koszul homology in positions `> N - 4`. Descending recursion then makes `rank d_j`
  generic for `j >= N - 3`, so the rank-threshold ideal on `D_N` is **zero** and there is
  nothing to kill. Labels:
  - `grade = height = 4` at `N = 8` is PROVED here: the monomial ideal `J_{F_0}` has height 4,
    height is upper semicontinuous, and the rank-`<= 2` locus caps it at 4.
  - At `N = 6, 7` the `F_0` above have height 3, so grade 4 there is ADOPTED (Kleiman,
    generic).
  - Depth sensitivity is **CONDITIONAL**, exactly as in B20-02 (Bruns–Herzog Thm 1.6.17,
    UNREAD; B20-02's O2).
- **`2 <= j <= N - 4` (`j = 2` at `N = 6`; `2, 3` at `N = 7`; `2, 3, 4` at `N = 8`): OPEN,
  ASSESSED.** B20-02's C5 identity constrains only `rank d_2 + dim H_1`. No padding-side ceiling
  for `rank d_j` exists on the record, and a determinant floor alone decides nothing. **Price:**
  1. one theory slot, paragraph-first, for a padding ceiling on `rank d_j^{(k)}` (for example,
     a lower bound on the Koszul homology of `J_{lP} ⊆ (l, P)`, which has grade 2);
  2. one default pilot for the `N = 6` determinant floors of `d_2^{(k)}` at `k <= 10`. The
     largest matrix is `4752 x 1890`, about 72 MB as an `nmod_mat`;
  3. a heavy lease for `N = 7, 8` at `k >= 9`. For example, `d_2^{(9)}` at `N = 8` is
     `13728 x 3360` (46 M entries, about 0.37 GB before the LU copy), over the default
     512 MiB cap.

  Without item 1, items 2–3 can only give MEASURED comparisons.

## 4. Exact scope and reopening conditions

**Established.**
- **PROVED:**
  - Theorem 2.1 (`closure(D45° ∩ P5) = T1 ∪ T2`).
  - The dimensions of §2.4: T1 33/32, T2 35/34, `Sigma_Pi` 31/30, T3 29/28, all aff/proj.
    The floors are exact ranks at integer points, the ceilings are proved.
  - `T1 ⊄ T2` and `T2 ⊄ T1`.
  - `T3 ⊆ T2`, and the skew-bordered type `⊆ T2`.
  - Proposition 2.5 (the cap minors vanish on all of `Sigma_Pi`).
  - Theorem 3.2 (row 1 at `N = 6, 7, 8`, every `k`).
- **CONDITIONAL:** the cap minors on `D35` (record's cap theorem); the zero ideal of `d_j`,
  `j >= N - 3`, at `N = 6, 7, 8` (depth sensitivity; plus Kleiman at `N = 6, 7`).

**Not established.**
- The boundary part of `D45 ∩ P5` (G-A1), and hence A.3 beyond the determinant part.
- Whether `T3 ⊆ T1`.
- Row 2 for `2 <= j <= N - 4`.
- Anything at `N >= 9`.
- No equation, gap, cell or separation.

**Reopening conditions.**
- *A.3 fails in full* iff some `l C*` with `C*` smooth lies in `D45`. By Theorem 2.1 such a
  point would have to be a boundary point. B17-01-C's `F* ∉ D45` (ADOPTED) excludes one
  specific `C*` only.
- *Classification complete* once `D45°` is shown to be closed, or its boundary points in `P5`
  are shown to lie in T1 ∪ T2.
- *Row 2* reopens with a padding-side ceiling on `rank d_j` (§3.3, item 1).
- *B23-02*, which asks about members of the Bordiga-type closure inside a hyperplane, is a
  different question and is not touched. If it needs `D45 ∩ P5`, Theorem 2.1 and G-A1 are the
  statements to use.

## 5. Labelled ledger (all rows producer only, G18)

| id | claim | label | method |
|---|---|---|---|
| L1 | Case analysis of the direct points by the degrees of `adj A_0 = s k kappa^T` (§2.1) | PROVED | hand |
| L2 | Skew-bordered type ⊆ `Sigma_Pi` (§2.2) | PROVED | hand; identity checked (pilot 1 E5) |
| L3 | T3: normal-form reduction; not a compression space; dimension 29 aff / 28 proj | PROVED (ceiling by hand; floor = exact Jacobian rank 29, twice) | hand + pilot 1 E1–E2 |
| L4 | **T3 ⊆ T2** (constant left kernel `alpha ⊗ beta` on a 3-space; intersection number 5) | PROVED | hand (post-pilot-1, addendum); identity checked (pilot 2 F2) |
| L5 | T3's cubics have a length-10 singular profile (`rank M_4 = 60`) | MEASURED | pilot 1 E1, E6 |
| L6 | Prediction A3 (T3 smooth) and A4's T3 entry | FALSIFIED | pilot 1 |
| L7 | **Theorem 2.1**: `closure(D45° ∩ P5) = T1 ∪ T2` | PROVED | L1–L4 + L8 |
| L8 | Dimensions: `D35` 29/28, T1 33/32, `Sigma_Pi` 31/30, **T2 exactly 35/34** (aff/proj) | PROVED (exact ranks as floors; ceilings by hand) | pilot 1 E2 + hand |
| L9 | **`T1 ⊄ T2`**: a `D35` cubic with exactly six nodes, in linearly general position | PROVED (the corank-at-`k = 7` step uses two UNREAD-CLASSICAL facts on the Hilbert functions of zero-dimensional schemes and curves) | pilot 2 F1 + hand |
| L10 | **Prop. 2.5**: `rank M_4 <= 64` on all of `Sigma_Pi`; generic exactly 64 | PROVED | hand + pilot 1 E4, E6 |
| L11 | Cap minors vanish on T1 | CONDITIONAL (record's cap theorem, as labelled there) | record |
| L12 | Record corrections 1–5 of §2.4 (the brief's "projective ≥ 35"; B22-10 §1 vs §7; exactness; one-point rank; B22-02 row 13) | corrections | this slot |
| L13 | G-A1: boundary points of `D45 ∩ P5` not excluded; any such component `>= 19` aff | OPEN | hand |
| L14 | **Theorem 3.2**: row 1 PROVED-kill at `N = 6, 7, 8`, every `k`; margins as in §3.2 | PROVED | pilot 2 + hand |
| L15 | Row 2, `j >= N - 3`: zero ideal | CONDITIONAL (depth sensitivity; Kleiman at `N = 6, 7`; `N = 8` height PROVED) | hand |
| L16 | Row 2, `2 <= j <= N - 4` | OPEN, ASSESSED; priced §3.3 | — |
| L17 | MEASURED padding ranks of §3.2 | MEASURED | pilot 2 |

**Literature at the point of use (G14, G14′).**
- UNREAD-CLASSICAL, each at its point of use:
  - Jacobi's formula;
  - Gauss's lemma (rank-one factorisation over a UFD);
  - Koszul relations of a regular pair;
  - intersection numbers on `P^1 x P^1`;
  - "a generic line meets a quadric in two points";
  - lower semicontinuity of rank and upper semicontinuity of fibre dimension;
  - closedness of images of projective morphisms;
  - Bézout for two plane conics;
  - Hilbert functions of zero-dimensional schemes (length `L` imposes `L` conditions in degree
    `>= L - 1`) and of curves;
  - the affine dimension inequality for intersections.
- UNREAD, as B20-02 labelled it: Bruns–Herzog Thm 1.6.17 (depth sensitivity), used only in L15.
- ADOPTED, as labelled on the record: Kleiman (L15 at `N = 6, 7`) and the cap theorem at
  `n = 3` (L11).
- **Not used:** Eisenbud–Harris and Atkinson, since §2.1 is self-contained; Dimca; Gotzmann
  (considered, not needed); the uniqueness of the Segre cubic (mentioned only as the reading of
  L5).

No specialist text is load-bearing for any PROVED row.

## 6. Resources, receipts, manifest

Interpreter `..\B15-02\.venv\python.exe` (Python 3.12.10, python-flint 0.9.0). Wrapper
`..\B15-02\analysis\b15_bound.py --seconds 60 --memory-mb 512` (`job_object_enforced: true`).
The wrapper prefixes `B15-` to `--slot`, so the receipts read `session_id: B15-23-03`.
`PYTHONDONTWRITEBYTECODE=1`. Before each launch I checked
`..\B15-01\results\logs\b23_01_*.pid` and `..\B15-02\results\logs\b23_02_*.pid` and ran
`Get-Process python*`. Only `b23_01_p1_secondprime.pid` (pid 48188) existed; its receipt shows
exit 0 at 45.45 s, and no python process was live (0 both times).

| run | started (UTC) | exit | wall | peak job memory | receipt |
|---|---|---|---|---|---|
| `b23_03_p1_classification` | 20:51:29Z | 0 | 0.277 s | 22,769,664 B | `results/logs/b23_03_p1_classification_resources.json`, `.pid` |
| `b23_03_p2_certificates_and_thresholds` | 20:59:07Z | 0 | 15.738 s | 209,850,368 B | `results/logs/b23_03_p2_certificates_and_thresholds_resources.json`, `.pid` |

**Budget:** 2 wrapped launches of 3; 16.0 s of 180 s. No cap was hit, there was no crash, and
no retry was needed. Pilot 3 was not used.

**Unwrapped actions.** These were non-numerical under G19 as ruled in B21-10 R22: read-only
git, `sha256sum`, `ls`, `grep`, `sed`, `Get-Process`, reading the python-flint type stubs, and
the bash seal step. **Two further unwrapped interpreter invocations** occurred during
inspection, one executing `print('x')` and one with an empty program. Neither performed
computation on the objects under study, and neither produced a result used anywhere. They are
listed for completeness.

**Receipts.** `results/logs/*.pid` is ignored at `.gitignore:51`, and
`git check-ignore -v` confirms both `b23_03_*.pid`. Housekeeping item:
**negation missing for `b23_03_`**. The `_resources.json` receipts and everything under
`results/b23_03/` are not ignored.

**Write footprint (all new):**
- `docs/b23_03_report.md`;
- `analysis/b23_03_p1_classification.py` and `analysis/b23_03_p2_certificates_and_thresholds.py`;
- under `results/b23_03/`: `preregistration_snapshot.md`, `addendum_before_p2.md`,
  `p1_classification.json`, `p2_certificates_and_thresholds.json`, `MANIFEST.json`,
  `SEAL_LOG.txt`;
- the four `results/logs/b23_03_*` receipts.

No existing file was edited. `results/b23_03/MANIFEST.json` is written by a bash seal step that
prints every count into `SEAL_LOG.txt`. It binds this report, the two scripts, the two pilot
outputs, the pre-registration and the addendum, the four receipts, and the pinned inputs:

| input | pin | sha256 |
|---|---|---|
| `docs/b22_10_review.md` | `2efb7aaf` | `86d8caf98a1c088a890bab5d3676ac40c5f9bfdd591c1af95d7a4981073ec092` |
| `analysis/b22_10_p2_D45_cap_P5.py` | `2efb7aaf` | `4086abfb04491048196b7836aacfa3886ba438a7c3e2ab54a5220072417a3862` |
| `results/b22_10/p2_D45_cap_P5.json` | `2efb7aaf` | `1259070a47f84479a2ae64ed106a0358beb49c79b652f47c4eadb4167fa6dce3` |
| `docs/b22_02_report.md` | `e22a41b1` | `b41e4265809a018750286d6eda416d62c4f4044b3fdb7cbac2cc51caf50593e4` (= B22-10's pin) |
| `docs/b20_02_report.md` | `7de65d7c` | `15ef389b5eb84074e77f2bd88c2dd5e98b14399a394d150b05f2b1b3f2baeda2` (= B22-02's pin) |
| `docs/b20_02b_report.md` | `7de65d7c` | `60ff4be461ad1f3b4733fdec36372bf0f0af3612a31f8a48af6260c49b5902ea` (= B22-02's pin) |
| `docs/onset_conjecture.md` | `82633a60` | `e43237da22f4f1f9260a01e5d5fd4bd41828c29aa6cdf0f8b6ac7c282214f49f` (= B22-02's pin) |
| `docs/det_onset.md` | `82633a60` | `da9f8f73f80128d8c9811b821abc6defd024ee7d2329db933692106eff4097a3` (= B22-02's pin) |
| `docs/post_b19_20260917/claude_gkz_incidence_20260917/REPORT.md` (Theorems A/B) | `82633a60` | `3cacb625f9c99344c2722abab21515e6fa5e697fdb8f7fd7be7396e765860b43` (= B20-02's prefix) |

No tool memory, chat value or scratchpad value is a premise of any row (G9, G9′). The report
does not name its own hash.
