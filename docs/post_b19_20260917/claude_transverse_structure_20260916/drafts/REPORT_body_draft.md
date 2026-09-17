
## 4. Source side: what the stabilizer of `K` forces on every full-`H` invariant

### 4.1 Base points and stabilizers

`K6` is the generic skew pencil of `extension_descent §3` (six variables, `det K6 = u_6^2`,
`u_6 = x1 x6 - x2 x5 + x3 x4`, the Pfaffian); `K5` is the assignment's five-variable pencil
(`det K5 = u_5^2`, `u_5 = x1^2 - x2 x5 + x3 x4`). In both cases the tuple `K = (Y_1..Y_r)` consists of
skew matrices, `span(Y_i)` is all of `Lambda^2 C^4` (`r = 6`) or the hyperplane `omega^perp`
for the nondegenerate form `omega = E12 - E21 - E34 + E43` (`r = 5`; the pencil repeats `x1` at
positions `(1,2)` and `(3,4)`), and `u = Pf|_span`, nondegenerate in both cases
(`det Q_0 = 1/16` for `r = 5`, MEASURED in Check 2).

Let `Gamma := SL_r x H^0`. Every `z in M_(4k)^r` is `Gamma`-invariant (its `GL_r`-weight is
`det^{4k}`), homogeneous of matrix-entry degree `4d = 4rk`, and satisfies `z(-Y^T) = z(Y)`.

**Lemma 4.1 (stabilizer; PROVED, dimensions MEASURED).** `Stab_Gamma(K)^0 = {(A, cA^T, g_A) :
A in G_r, c^2 det A = 1}` with `G_6 = GL_4`, `G_5 = GSp_4(omega)`, and `g_A in SL_r` the inverse
of the action induced on `span(Y_i)`. Its image in `GL(T_K)` is `SL_4/mu_2 = SO_6` (`r = 6`) resp.
`Sp_4/mu_2 = SO_5` (`r = 5`), acting on `C^r = span(Y_i)` through `Lambda^2` and preserving `u`
up to the scalar `det A`.
*Proof.* `A Y B` is skew for every `Y` in the span iff `Y D = D^T Y` for all such `Y`, where
`D = B A^{-T}`; the solution space is `C.I` (for `r = 5` MEASURED in Check 1,
`A_K5_commutant_dimension = 1`; for `r = 6` it is the classical statement for all of
`Lambda^2`). So `B = cA^T`, and `Y -> cAYA^T` acts on `Lambda^2` by `c Lambda^2 A`, which
preserves `omega^perp` iff `A` preserves the line `[omega]`, i.e. `A in GSp_4(omega)`. The
`SL_r` component is forced. Dimensions `16` and `11` give orbit dimensions `66 - 16 = 50` and
`55 - 11 = 44`, which Check 1 confirms directly. `Lambda^2 : SL_4 -> SO(Pf)` is the standard
isogeny; restricted to `Sp_4` it lands in `SO(omega^perp)`. ∎

The element `tau' : Y -> -Y^T` fixes `K` (`K^T = -K`), preserves every `z`, acts on symmetric
tangent directions by `-1` and on skew ones by `+1`.

**Lemma 4.2 (tangent decomposition; MEASURED exactly, Check 1 Part A).**
`T_K W^r = T_orb (+) C.K (+) N`, where `T_orb = Lie(Gamma).K` has dimension `50` (`r = 6`) resp.
`44` (`r = 5`), the radial line `C.K` is not in `T_orb`, **every skew direction lies in
`T_orb + C.K`**, and `N` is the unique `Stab^0`-stable complement, contained in the symmetric
directions `V_sym = Sym^2 C^4 (x) C^r`:

| `r` | `dim T` | `dim T_orb` | `dim(T_orb + C.K)` | `dim V_sym` | `dim(V_sym ∩ (T_orb + C.K))` | `dim N` | `N` as `Stab^0`-module |
|---|---|---|---|---|---|---|---|
| 6 | 96 | 50 | 51 | 60 | 15 | **45** | `S_(3,1) C^4` (`V_sym = 45 + 15`, LR multiplicities `1, 1`; not self-dual: `S_(3,1)^* = S_(3,3,2)`) |
| 5 | 80 | 44 | 45 | 50 | 15 | **35** | `V(2 omega_1 + omega_2)` of `Sp_4` (`V_sym = 35 + 10 + 5`, multiplicities `1, 1, 1`; orthogonal) |

The identification of `N` uses only that `V_sym` is multiplicity-free with a unique
15-dimensional submodule (`15 = S_(2,1,1)`, resp. `10 + 5`). `tau'` acts on `N` by `-1`.

**Lemma 4.3 (formal slice; PROVED).** For every `S in T` there are formal curves
`gamma(t) in Gamma`, `c(t) in 1 + t C[[t]]`, `n(t) in t N[[t]]` with
`K + tS = c(t) . gamma(t) . (K + n(t))`, and `n(t) = t S_N + O(t^2)` with `S_N` the
`N`-component of `S`. *Proof.* The map `(gamma, c, n) -> c gamma (K + n)` has differential
`Lie(Gamma) (+) C (+) N -> T_orb + C.K + N = T` at `(e, 1, 0)`, surjective by Lemma 4.2; apply
the formal inverse function theorem to lift the curve `K + tS`. ∎

**Theorem 4.4 (automatic jets; PROVED).** For `z in M_(4k)^r` let `f_z(n) := z(K + n)`, a
`Stab(K)`-invariant polynomial on `N`. Write `f_z = z(K) + Phi_2(z) + Phi_3(z) + ...` with
`Phi_m(z) in Sym^m(N^*)^{Stab^0}`. Then `Phi_odd(z) = 0` (by `tau'`), and for every `S in T`

    z(K + tS) = c(t)^{4d} . f_z(n(t)).

Consequently every Taylor coefficient of `z(K + tS)`, in every direction, is a linear function
of the **transverse jet data** `(z(K), Phi_2(z), Phi_4(z), ...)` with coefficients that depend
only on `S`, `r`, `k` (through `c(t)`, `n(t)`), not on `z`. In particular:

- `[t^2] z(K + tS) = z(K) alpha_2(S) + Phi_2(z)(S_N, S_N)`;
- `[t^4] z(K + tS) = z(K) alpha_4(S) + (terms linear in Phi_2(z)) + Phi_4(z)(S_N^4)`;
- jets in skew (orbit) directions and mixed jets carry nothing beyond the same data.

*Proof.* `z` is `Gamma`-invariant and homogeneous, so `z(c gamma Y) = c^{4d} z(Y)`; insert Lemma
4.3. `f_z` is `Stab`-invariant because `Stab` preserves `K + N`. `tau'` acts on `N` by `-1` and
fixes `z`, so the odd parts vanish. ∎

**Corollary 4.5 (the counts; MEASURED, Check 1 Part B, all controls passing).**
`j_m(r) := dim Sym^m(N_r)^{Stab^0}`:

| `r` | `j_2` | `j_4` | `j_6` | `j_8` | reason for `j_2` |
|---|---|---|---|---|---|
| 6 | **0** | **2** | 6 | not computed | `N_6` irreducible and not self-dual: no invariant bilinear form at all (`Lambda^2` invariants also `0`) |
| 5 | **1** | **5** | 24 | 127 | `N_5` irreducible and orthogonal (`Sym^2` invariant `1`, `Lambda^2` invariant `0`) |

Controls: `Sym^2(sl_4)^{SL_4} = 1`, `Sym^2(C^4)^{SL_4} = 0`, `Sym^2(C^4)^{Sp_4} = 0`,
`Sym^2(5)^{Sp_4} = 1`, `Sym^2(10)^{Sp_4} = 1`, `dim H_4(C^6) = 105 = S_(4,4)C^4`,
`dim H_4(C^5) = 55`, `Sym^2(H_4)^{inv} = 1` in both cases. The finite parts of `Stab` (`tau'`,
the centre `mu_4`, the sign `c = -1`) act trivially on `Sym^{even}(N^*)`, so these are the
counts for the full stabilizer.

**Corollary 4.6 (what is forced on every source invariant).** For `z in M_(4k)^r` and
symmetric `S`:

1. `z(K + tS)` is even in `t` (all `r`); for `S = ell(x) M` (a rank-one tuple update) it has
   degree `<= 4k` because `z` has degree `4k` in the Plücker coordinates of `span(Y_i)` and
   the wedge changes linearly in `t` (`M ∧ M = 0`).
2. `r = 6`: `[t^2] z(K + tS) = z(K) alpha_2(S)` for **every** `z` and every symmetric `S`
   (`j_2(6) = 0`). This is the attachment's "order two is silent", now proved from Lemma 4.2:
   there is no order-two transverse datum at all in six variables.
3. `r = 5`: `[t^2] z(K + tS) = z(K) alpha_2(S) + beta_z B(S_N, S_N)` where `B` is the unique
   (up to scale) `Sp_4`-invariant quadratic form on `N_5` and `beta_z` is **one** scalar per
   `z`. So the order-two jets in all symmetric directions together span at most a
   two-dimensional space of functionals on `M_(4k)^5`, namely `span(z -> z(K5), z -> beta_z)`.
4. Order four: `Phi_4(z)` lives in a space of dimension `2` (`r = 6`) resp. `5` (`r = 5`).
   The full order-`<= 4` jet data at `K` of a source vector lie in `J_{<=4} := C (+)
   Sym^2(N^*)^{inv} (+) Sym^4(N^*)^{inv}` of dimension **3** (`r = 6`) resp. **7** (`r = 5`).

None of this uses the ambient space, `a`, `m_det`, or any carrier.

## 5. Target side: what a genuine quartic-coefficient function must additionally satisfy

### 5.1 Derivatives at the quartic `u^2`

Let `F in A_{d,lambda}`, `lambda = (4k)^r`, so `F(q o A) = det(A)^{4k} F(q)` for `A in GL_r`. The
point `u^2 in Sym^4 C^r` is fixed by `SO(u)` and scaled by the conformal group. Hence
`d^j F_{u^2}` is an `SO_r`-invariant `j`-linear form on `Sym^4 C^r = H_4 (+) u H_2 (+) C u^2`
(harmonic decomposition; the three summands are pairwise non-isomorphic, irreducible and
self-dual, dimensions `105, 20, 1` for `r = 6` and `55, 14, 1` for `r = 5`).

- **Order one (jet order two).** `dF_{u^2}` is `SO_r`-invariant, so it factors through the
  `u^2`-component: `dF_{u^2}(q) = d . c(q) . F(u^2)`, `c(q) = Delta^2 q / Delta^2(u^2)`, with
  `Delta` the `Q_0^{-1}`-Laplacian (`Delta^2(u^2) = 2r(4r + 8) = 384, 280`). **No free
  parameter.** (VERIFIED; this is the sealed §C.2 and attachment 515d31fd §1.)
- **Order two (jet order four).** `d^2 F_{u^2} in Sym^2(Sym^4 C^r)^{*, SO_r}` is
  three-dimensional (`Sym^2(H_4)^{inv} = Sym^2(H_2)^{inv} = 1`, `Sym^2(u^2)`, no cross terms;
  MEASURED controls in Check 1). Covariance along the quadratic-square family fixes two of the
  three: for a quadratic `a` with matrix `Q_a` and `M := Q_0^{-1} Q_a`, expanding
  `F((u + eps a)^2) = F(u^2) det(I + eps M)^{2k}` gives

      dF_{u^2}(u a) = k tr(M) F(u^2),
      dF_{u^2}(a^2) + 2 d^2F_{u^2}(u a, u a) = k [2k tr(M)^2 - tr(M^2)] F(u^2),

  which by polarisation determines `d^2F_{u^2}` on `(u . Sym^2) x (u . Sym^2)`, i.e. on the
  `u H_2` and `u^2` summands and their cross term. The only free parameter is
  `kappa_F` with `d^2F_{u^2}(h, h') = 2 kappa_F N(h, h')` for `h, h' in H_4`, `N(h, h') :=
  h(Q_0^{-1} d) h'` the invariant pairing. **One free parameter through order four.** (PROVED;
  the six-variable specialisation is attachment 515d31fd §1, VERIFIED below.)

### 5.2 The universal quartic and the order-four jet on `E`

For a symmetric tuple `S`, `det(K + tS) = u^2 + t^2 v(S) + t^4 w(S)` (even in `t` by transposition;
`t`-support `{0, 2, 4}` MEASURED for all seven directions used). Decompose
`v = h_4 + u h_2 + c_v u^2` and put `a := h_2 + c_v u`, `M_a := Q_0^{-1} Q_a`. Then for
`z = F o phi`:

    [t^2] z(K + tS) = d . c_v(S) . z(K),
    [t^4] z(K + tS) = z(K) . A_{r,k}(S) + kappa_F . N(h_4(S), h_4(S)),
    A_{r,k}(S) = d c(w) + (1/4) [ k (2k tr(M_a)^2 - tr(M_a^2)) - d c(a^2) ],      d = rk.

(PROVED from §5.1 by the chain rule; `dF(w)` and `(1/2) d^2F(v, v)` split by Schur into the
`H_4` term and the `u`-multiple terms.) Both `A_{r,k}` and `N o h_4` are **universal**: they
depend on `(r, k, S)` only.

**Check 2 (MEASURED, 3.4 s, receipt `results/logs/c2_fivevar_order4_resources.json`).**

Six variables, `k = 1`, control against attachment 515d31fd and the sealed `p9`:

| direction | `c_v` | `A_{6,1}` | `N(h_4)` | `[t^4]/[t^0]` on `E` (sealed p9) | `kappa` |
|---|---|---|---|---|---|
| `S1 = x1 I` | `1/6` | `3/20` | `96/5` | `3/14` | `3/896` |
| `S2 = (x1+x6) I` | `1/3` | `11/5` | `10368/5` | `64/7` | `3/896` |

`N(S2)/N(S1) = 108`, `A(S2) - 108 A(S1) = -14`, a **single** `kappa = 3/896` fits both sealed
values (the sealed E11 records the same `3/896`). The attachment's table is reproduced exactly
by an independent route (trace formulas instead of its `J(h_2)` bookkeeping). **VERIFIED.**

Five variables, `k = 1` (`d = 5`), five directions, with `H5` (the unique `(4^5)` invariant,
integral convention `T_alpha = alpha! c_alpha`) recomputed at `K5 + tS`, `t = 0..4`:

| direction | `c_v` | `A_{5,1}` | `N(h_4)` | `H5` polynomial support | `[t^2]/[t^0]` (= `5 c_v`?) | `[t^4]/[t^0]` | `kappa~` |
|---|---|---|---|---|---|---|---|
| `S1 = x1 I` | `6/35` | `89/441` | `5888/63` | `{0,2,4}` | `6/7` ✓ | `13/21` | `1/224` |
| `S2 = x2 I` | `8/35` | `32/147` | `320/21` | `{0,2,4}` | `8/7` ✓ | `2/7` | `1/224` |
| `S3 = (x1+x2) I` | `2/5` | `43/63` | `832/9` | `{0,2,4}` | `2` ✓ | `23/21` | `1/224` |
| `S4 = x1 diag(1,1,0,0)` | `3/35` | `-2/49` | `64/7` | `{0,2}` | `3/7` ✓ | `0` | `1/224` |
| `S5 = (x1+x3) I` | `2/5` | `43/63` | `832/9` | `{0,2,4}` | `2` ✓ | `23/21` | `1/224` |

`H5(K5) = 322560` (agrees with the sealed P3). All five `H5` restrictions are even quartics; the
three-point extraction of `[t^2]` and `[t^4]` agrees with the five-point interpolation; the
order-two ratio equals `5 c_v` in every direction (the target-side order-two statement is
direction-independent, as §5.1 says); and one `kappa~ = 1/224` fits all five directions —
**four independent consistency checks of `A_{5,1}` and `N`**, including a non-scalar
symmetric direction. **VERIFIED.**

### 5.3 The explicit E-free order-four five-row condition (`k = 1`)

Eliminating `kappa~` between two directions `S, S'` (with `J_S(z) := [t^4] z(K5 + tS)
= (z(K5+2S) - 4 z(K5+S) + 3 z(K5))/12` for `k = 1`):

    C4_{S,S'}(z) := N(h_4(S')) [J_S(z) - z(K5) A(S)] - N(h_4(S)) [J_{S'}(z) - z(K5) A(S')].

In integer form on the value vector `(z(K5), z(K5+S), z(K5+2S), z(K5+S'), z(K5+2S'))`:

| pair | integer coefficients | value on the `H5` line |
|---|---|---|
| `(S1, S2)` | `(-27, -60, 15, 368, -92)` | `0` |
| `(S1, S3)` | `(3711, -2548, 637, 2576, -644)` | `0` |
| `(S1, S4)` | `(-2211, -252, 63, 2576, -644)` | `0` |
| `(S1, S5)` | identical to `(S1, S3)` (`x2 <-> x3` is a stabilizer symmetry of `K5`) | `0` |

Each `C4_{S,S'}` is **globally necessary** on `M_(4^5)` (it vanishes on `E` by construction, and
the vanishing on the ambient line is checked exactly). Whether any of them is nonzero on the
source is **not established here**: no full-`H` source vector was evaluated (the certified
`q_3, q_7` values exist only at `K5, K5+S1, K5+2S1`, sealed `p7_arc_S0.json`).

### 5.4 Dependence on `k` (requirement 5)

For `lambda = (4k)^5`, `d = 5k`: the source-side structure of §4 (`N_5`, `j_m(5)`, Theorem 4.4)
is **independent of `k`**; the target-side constants are not:

- `[t^2] z(K5 + tS) = 5k c_v(S) z(K5)` on `E`; for `S = x1 I`, `c_v = 6/35`, so the order-two
  condition is `C2^{(k)}(z) = [t^2] z(K5 + t x1 I) - (6k/7) z(K5)` (the sealed `112, -7, -177`
  form is the `k = 1` three-node evaluation of this).
- `z(K5 + tS)` is even of degree `<= 4k` for rank-one updates `S = ell(x) M`, so `[t^2]` and
  `[t^4]` need `2k + 1` even nodes (`t = 0, 1, ..., 2k`), not three.
- `A_{5,k}` changes through `d = 5k` and the covariance exponent `2k` (formula in §5.2);
  `N o h_4` does not.
- The stopping rule "a nonzero `4 x 4` forbidden minor proves exactness" is specific to
  `s = 5`, `m_det = 1` at `k = 1`.

Only `k = 1` is checked (Check 2). The `k >= 2` formulas are PROVED from §5.1–5.2 but have no
numerical control here.

## 6. Comparison map, its position, and the selection rule

### 6.1 The two jet maps

Let `J_{<=4} := C (+) Sym^2(N^*)^{Stab} (+) Sym^4(N^*)^{Stab}` (dimension `3` for `r = 6`, `7` for
`r = 5`). The **source jet map** is `j : M_lambda -> J_{<=4}`, `z -> (z(K), Phi_2(z), Phi_4(z))`.
The **ambient jet map** is `j_A : A_{d,lambda} -> J_{<=4}`, `F -> j(F o phi)`; its image is

    L := { ( f,  f . beta_0,  f . A' + kappa . (N o h_4) ) : (f, kappa) = (F(u^2), kappa_F) },

a subspace of the two-dimensional space `L_max` spanned by `(1, beta_0, A')` and
`(0, 0, N o h_4)`. Here `A'` and `beta_0` are the universal elements of `Sym^4(N^*)^{Stab}` and
`Sym^2(N^*)^{Stab}` obtained by rewriting §5.2 in the normal coordinates of §4 (for `r = 6`,
`beta_0 = 0` since `j_2 = 0`). `j(E) = j_A(A_{d,lambda}) = L`, and `E subset M_lambda`, so
`L subset j(M_lambda)`.

**What determines the position of `L` inside `J_{<=4}`** (requirement 2): (i) the universal
constants of the group geometry, `c(t)` and `n(t)` of Lemma 4.3, equivalently `alpha_2, alpha_4`
and the `Phi_2`-coefficients in Theorem 4.4 — these are functions of `S` only; (ii) the
`Stab`-equivariant quadratic map `h_4 : N -> H_4(C^r)` (the `H_4`-component of `v(S)`) and the
invariant pairing `N` on `H_4`; (iii) the universal quartic `A_{r,k}` and the scalar
`d c_v`, i.e. the covariance exponent `2k` and the degree `d`; (iv) the ambient data
`(F(u^2), kappa_F)` for `F in A_{d,lambda}`, in particular the ratio `kappa_H / H(u^2)` when
`a = 1` (`3/896` for `(6,(4^6))`, `1/224` for `(5,(4^5))` in the normalisations of Check 2).
Items (i)–(iii) are computable from `(r, k, S)` alone; only (iv) needs the ambient space, and
the **E-free** conditions do not need it at all.

### 6.2 The selection rule (Theorem)

**Theorem 6.1 (PROVED).** Let `lambda = (4k)^r`, `r in {5, 6}`, `K` as above.

(a) Every globally necessary linear condition on `M_lambda` that is built from Taylor
coefficients of order `<= 4` of `z(K + tS)` at `K`, in any finite set of directions `S`
(symmetric or not) and without using knowledge of `A_{d,lambda}` beyond its covariance,
factors through `j` and vanishes on `L_max`. The space of such **E-free** conditions has
dimension at most `dim J_{<=4} - 2`, i.e. **`1` for `r = 6` and `5` for `r = 5`**.

(b) Conditions that also use the actual ambient image (a known `E`) are the annihilator of
`j(E) = L`: at most `dim J_{<=4} - dim L`, i.e. `2` for `r = 6` and `6` for `r = 5` when
`a = m_det = 1`.

(c) The **rank actually realised** on `M_lambda` by all order-`<= 4` conditions at `K` is
`dim j(M_lambda) - dim L` (with `L` replaced by `L_max` for E-free conditions), hence at most
`min(dim J_{<=4}, s) - m_det` in case (b). A condition of order `2m` can exist only if
`Sym^{2m}(N^*)^{Stab} != 0`.

*Proof.* (a), (b): Theorem 4.4 says every such Taylor coefficient is a fixed linear functional
on `J_{<=4}` composed with `j`; §5.2 says the image of `E` lies in `L subset L_max`; necessity
means vanishing on `E`. (c): rank of a family of functionals on `M_lambda` vanishing on a
subspace equals `dim j(M) - dim(j(M) ∩ L)` and `L subset j(M)`. ∎

### 6.3 Consequences, cell by cell

**Six variables, `(6k, (4k)^6)`.**

- Order two: **no condition exists** for any `z`, any direction (Cor. 4.6.2). The attachment's
  silence claim is a theorem. (PROVED)
- Order four: `dim J_{<=4} = 3`, so there is **exactly one E-free condition** (up to scale),
  and it is the verified `C_2 = J_2 - 108 J_1 + 14 z(K)` (nonzero on `Q^2`, sealed E11,
  reproduced in Check 2). **No second pair of directions, no non-scalar symmetric direction,
  and no mixed jet can add an E-free condition of order `<= 4` at `K6`.** (PROVED + VERIFIED)
- With `E` known (`a = 1`, `kappa_H6 = 3/896`): at most **two** conditions, the second being
  e.g. `J_1(z) - (3/14) z(K)` (value `1/4 - 3/14 = 1/28 != 0` on `Q^2`); whether it is
  independent of `C_2` on `M_(4^6)` is the question whether `j(M_(4^6)) = J_{<=4}` (rank 3),
  which needs a third source vector with jet outside `span(j(H6 o phi), j(Q^2))`. (OPEN)
- Hence **at least `9 - 2 = 7` of the nine false survivors of `(6,(4^6))` are invisible to every
  jet condition of order `<= 4` at `K6`**, whatever carrier is built. Detecting them needs order
  `>= 6` (`j_6(6) = 6`; the target-side count at order six is not derived here) or other base
  points (the two-pencil test `q(K) - 1120 q(L)` is a 0-jet at the second point `L`, whose
  stabilizer is much smaller and where far less is forced — its counting is OPEN).

**Five variables, `(5k, (4k)^5)`.**

- Order two: `dim J_{<=2} = 2`, `dim L_{<=2} = 1`, so there is **exactly one E-free order-two
  condition**, and it is `C2` (nonzero on the source at `k = 1`: sealed E6). **Theorem 6.2
  (redundancy of all other order-two directions; PROVED).** For every symmetric tuple `S'`,

      [t^2] z(K5 + tS') - d c_v(S') z(K5)  =  ( B(S'_N, S'_N) / B(S_N, S_N) ) . C2^{S}(z)

  identically on `M_(4k)^5`, where `S = x1 I` and `B` is the invariant form on `N_5`; the ratio
  is computable from `S'` alone, and it is `0` exactly when `S'_N` is `B`-isotropic. (Cor. 4.6.3
  plus §5.1; `B(S_N, S_N) != 0` because `C2^{S} != 0` on the source.) So the active session's
  `C2` is *the* order-two transverse test at `K5`, in every direction and for every `k`.
- Order four: `dim J_{<=4} = 7`, `dim L_max = 2`: **up to five E-free conditions in total**, one
  of them `C2`, hence **up to four genuinely new order-four conditions** (`C4_{S,S'}` of §5.3
  are explicit members; five independent 4-jet directions are needed to realise all four, and
  the scalar-matrix family `ell(x) I` alone may not suffice — its 4-jet evaluations span an
  unknown part of `(Sym^4 N_5^*)^{inv, *}`; non-scalar directions such as `S4` should be
  included).
- Realised rank: at most `s - m_det = 4` at `k = 1`. Whether the order-`<= 4` transverse
  conditions at `K5` reach rank 4 on `M_(4^5)` is exactly the **missing lemma** of §9.

**Non-rectangular cells.** The proof of Theorem 6.1 uses `SL_r`-invariance of `z`. For general
`lambda` the source is only `U_r`-invariant and the stabilizer of `K` in the relevant group is
not reductive, so the counting must be replaced by a branching problem: source-side jets of
order `m` live in `Hom_{Stab^0}(V_lambda^*|_{Stab^0}, Sym^m(N^*))`, target-side in the
corresponding branching of `Sym^d(Sym^4)`-covariants restricted to `SO_r`. This is stated, not
proved (OPEN). All five-row cells with `d <= 5` are excluded anyway (`D <= 0`), so the first
non-rectangular candidates are at `d = 6`.

### 6.4 Can the mismatch predict constraints before a carrier is built? (requirement 3)

Yes for **upper bounds and for where to look**; no for **lower bounds**:

- The rule decides, from `(r, m)` alone, whether order `2m` has *room*: none at order two for
  six variables, one at order two for five variables, `j_4 - 1` E-free at order four. This is
  what makes five variables cheaper than six (§7).
- It bounds the total number of order-`<= 4` conditions at `K` (`1` E-free / `2` total for
  `r = 6`; `5` E-free / `6` total for `r = 5`), hence bounds what any carrier can deliver from
  this base point and jet order, e.g. the "at least seven invisible survivors" statement.
- It cannot certify that a predicted condition is nonzero on the source: `j` may fail to be
  surjective. One explicit source vector with a nonzero value settles that (as `Q^2` did in six
  variables and `q_3, q_7` did for `C2`). That is a one-vector certificate, far cheaper than a
  complete carrier, and it is the discriminating test proposed in §9.

## 7. What transfers from six variables to five (requirement 4)

| item | six variables | five variables | transfers? |
|---|---|---|---|
| base point | generic skew pencil, `det = u^2`, `u` nondegenerate in 6 vars | hyperplane skew pencil `K5`, `det = u^2`, `u` nondegenerate in 5 vars | yes (both are "skew pencil with quadratic-square determinant") |
| `Stab^0` image | `SO_6 = SL_4/mu_2` | `SO_5 = Sp_4/mu_2` | yes, as "the conformal orthogonal group of `u`" |
| normal space `N` | `45 = S_(3,1)C^4`, not self-dual | `35 = V(2w_1+w_2)`, orthogonal | the *mechanism* transfers; the *module* changes, and with it the lowest nontrivial order |
| lowest order with room | 4 (`j_2 = 0`) | 2 (`j_2 = 1`) | **no**: five variables admit an order-two test, six do not |
| E-free conditions through order 4 | exactly 1 | up to 5 | no |
| target-side free parameters through order 4 | `F(u^2), kappa_F` | `F(u^2), kappa_F` | yes (harmonic decomposition has the same shape) |
| universal constants | `A_{6,1}`, `N`, `108`, `-14` | `A_{5,1}`, `N`, tables in §5.2–5.3 | **no**: every constant must be recomputed; Check 2 does this for `k = 1` |
| evenness and degree `<= 4k` in `t` | yes (Plücker argument) | yes | yes |
| three-point extraction | `k = 1` only | `k = 1` only | yes at `k = 1`; `2k+1` nodes otherwise |
| arc `C` | `C = 0` (silent band) | `2 <= rank C <= 4` | no: independence from `C` is automatic in six variables and open in five |
| the restriction-only (quadratic-square family) obstruction | one scalar survives | one scalar survives | yes: only the value `z(K)` is seen; jets are indispensable in both |

## 8. Independence from the old arc, and the three distinctions

### 8.1 Route to nonzero action on `ker C` (requirement 6)

- `(6,(4^6))`: `C = 0` on the source (B19-01 Thm 4.1), so every nonzero necessary functional acts
  nonzero on `ker C = M`. Independence is automatic; `C_2` is one certified additional
  constraint (sealed). **PROVED.**
- `(5,(4^5))`: `E subset ker C`, `dim E = 1`, so `rank C <= 4`, and `E` lies in the kernel of every
  transverse condition too, so `rank [C; transverse] <= 4`. Therefore

      increment := rank [C; T] - rank C  in {0, 1, 2}  with  rank C in {2, 3, 4},

  and the increment is positive **iff** `rank C < 4` and some transverse condition does not
  vanish on `ker C`. Three routes, in order of cost:
  1. **Rank-four arc certificate** (a nonzero `4 x 4` minor of actual forbidden coefficients on
     four certified independent vectors): then `ker C = E`, and *every* necessary condition —
     `C2`, all `C4`, anything else — is redundant. A theorem of redundancy, not a witness.
  2. **Transverse-first**: if the order-`<= 4` transverse family reaches rank `4` on `M_(4^5)`
     (the missing lemma), then `ker T = E` and the increment equals `4 - rank C`; independence
     from `C` is then equivalent to non-exactness of the arc, and a single exact arc-kernel
     vector `n` with `T n != 0` follows automatically from `rank C < 4`. This route needs the
     complete carrier once (five vectors, `1 + 2 x (number of directions)` points each) and no
     exact forbidden-coefficient verification beyond what route 1 already needs.
  3. **Witness**: an exact `n in ker C` (all forbidden coefficient polynomials verified zero,
     sealed §C step 4) with `C2(n) != 0` or `C4(n) != 0`. Cheapest if the carrier and the exact
     kernel are already in hand; this is the active session's target.
  A **redundancy theorem** without computation is not available: `C` is equivariant for the
  Levi `L` of B19-01 Prop. 6.1 and `T` for `Stab(K5)`, and these groups have no common
  reductive subgroup acting on `M_(4^5)` that could force `T subset rowspace(C)` by Schur's
  lemma. Redundancy can only be established as in route 1, or by `T` vanishing on a certified
  spanning set of `ker C` (corrigendum D).

### 8.2 The three distinctions (requirement 7)

- **Improved source bound** = `rank [C; T] > rank C`: the surviving source `s - rank` shrinks.
  Possible in `(4^5)` (unknown) and already realised in `(4^6)` (by one).
- **Bound below `a`** = `s - rank [C; T] < a`. Since `E` lies in every kernel,
  `rank <= s - m_det`, so `B >= m_det`, and `B < a` requires `m_det < a`, i.e. a determinant
  equation in the cell. In every cell touched here `m_det = a = 1`; **no transverse condition
  can lower the clipped bound below `a` there**, and none can anywhere unless an equation
  exists.
- **`D > 0`** additionally needs a certified actual-padding rank floor `r > B`. Nothing here
  produces a padding floor; the transverse programme is a determinant-side tool only.

## 9. Final deliverables

### 9.1 The representation-based selection rule (one sentence)

At a skew pencil `K` with `det K = u^2` and rectangular `lambda = (4k)^r`, the globally
necessary transverse conditions of order `<= 2m` number at most
`1 + sum_{j <= m} dim Sym^{2j}(N_r^*)^{Stab(K)} - (target parameters through order 2m)`, with
`N_6 = S_(3,1)C^4` (no order-two room, one E-free order-four condition, exactly the known one)
and `N_5 = V(2w_1 + w_2)` of `Sp_4` (one order-two condition, `C2`, unique up to scale in all
directions and all `k`; up to four further E-free conditions at order four).

### 9.2 The smallest meaningful ambient-nonempty test

`(5, (4^5))`, `a = s_det = 1`, `s = 5`: evaluate the two certified vectors `q_3, q_7` at
`K5 + S2, K5 + 2 S2` (`S2 = x2 I`) and `K5 + S4, K5 + 2 S4` (`S4 = x1 diag(1,1,0,0)`), and compute
`rank [C2; C4_{S1,S2}; C4_{S1,S4}]` on `span(q_3, q_7)` modulo the working prime, using the
sealed values at `K5, K5 + S1, K5 + 2 S1`. Outcomes: rank `2` proves that the order-four
transverse family is not a multiple of `C2` on the source (the order-four room predicted by
`j_4(5) = 5` is realised, at least partly, by actual full-`H` vectors); rank `1` is
inconclusive (two vectors only). Either way no gap and no arc statement follows.

### 9.3 The exact missing lemma

**Lemma (jet injectivity at `K5`, OPEN).** *For `z in M_(4^5)`: if `z(K5) = 0`, `Phi_2(z) = 0`
and `Phi_4(z) = 0`, then `z = 0`.* Equivalently, the source jet map
`j : M_(4^5) -> J_{<=4} = C^7` is injective, i.e. the order-`<= 4` transverse conditions at `K5`
have rank exactly `4` on the source and their common kernel is `E`.

If true, the transverse family alone certifies the determinant coordinate subspace in this
cell, the arc is redundant with it, and "independence from `C`" reduces to `rank C < 4`. If
false, there is a nonzero full-`H` invariant flat to order four at `K5` in every normal
direction, and order six (`j_6(5) = 24`) or a second base point is required. The six-variable
analogue (`j : M_(4^6) -> C^3` surjective?) decides whether the second, `E`-using order-four
condition adds rank there.

A complete carrier of `M_(4^5)` is needed to decide the lemma; five independent 4-jet
directions (including non-scalar symmetric tuples) give `5 x (1 + 2 x 5) = 55` evaluations at
`k = 1`.

### 9.4 One proposed experiment (priced, NOT run)

The test of §9.2. Inputs: `pilots/p6_basis.json` (slot lists of `q_3, q_7`), the sealed dense
runner `pilots/paired_runner.py` (measured `0.55 s` per symmetrised evaluation, `4^10`-entry
intermediates, peak job memory `219 MB` in the sealed P7), the integer coefficient vectors of
§5.3. Cost: `2 vectors x 4 new points = 8` evaluations, about `5 s` and `< 250 MiB` in one
wrapped process, plus a `3 x 2` modular rank. Falsification: rank `1` on the two vectors leaves
the order-four family undistinguished from `C2` on the certified subspace.
**Not run here**: it evaluates the same certified vectors at `K5`-type points that the active
sparse-evaluator session (`…_addendum/FEASIBILITY.md` Stage B) uses for its verification, so it
overlaps that session's work and would duplicate its point family; it should be attached to that
session's continuation, with the two new directions added to its point list.

## 10. Claim ledger

| # | claim | label | evidence |
|---|---|---|---|
| T1 | `Stab_Gamma(K)^0` as in Lemma 4.1; image `SO_6` / `SO_5` | PROVED (commutant MEASURED for `K5`) | §4.1, `c1…json: A_K5_commutant_dimension = 1` |
| T2 | `T_K = T_orb (+) C.K (+) N`, dims `50/51/45` and `44/45/35`; all skew directions in `T_orb + C.K` | MEASURED (exact rank) | `c1…json: A_tangent_K6/K5` |
| T3 | `N_6 = S_(3,1)C^4` (not self-dual), `N_5 = V(2w_1+w_2)` (orthogonal) | PROVED given T2 + MEASURED LR multiplicities | `c1…json: B_characters` |
| T4 | formal slice and automatic-jets theorem (4.3, 4.4) | PROVED | §4 |
| T5 | `j_2(6)=0, j_4(6)=2, j_6(6)=6; j_2(5)=1, j_4(5)=5, j_6(5)=24, j_8(5)=127` | MEASURED, eight controls passing | `c1…json` |
| T6 | target-side: no free parameter at order two, one (`kappa_F`) at order four; covariance formulas | PROVED | §5.1 |
| T7 | `A_{r,k}`, `N o h_4`, the `[t^4]` formula on `E` | PROVED; VERIFIED at `(r,k) = (6,1)` against p9 (`108, -14, 3/896`) and at `(5,1)` on five directions (`kappa~ = 1/224`) | `c2…json` |
| T8 | explicit `C4_{S,S'}` integer conditions, globally necessary on `M_(4^5)` | PROVED (necessity) + VERIFIED (exact zero on `H5` line) | `c2…json: five_variables.C4` |
| T9 | `C4` nonzero on the source | NOT REACHED (no source vector evaluated) | — |
| T10 | six-row: no order-two condition; exactly one E-free order-`<=4` condition; `>= 7` survivors invisible at `K6` through order four | PROVED (given T5) | §6.3 |
| T11 | five-row order-two redundancy theorem (all directions ∝ `C2`) | PROVED (given T5) | §6.3, Thm 6.2 |
| T12 | five-row: `<= 5` E-free conditions through order four, realised rank `<= 4` | PROVED | §6.3 |
| T13 | `k`-dependence formulas for `(4k)^5` | PROVED, checked only at `k = 1` | §5.4 |
| T14 | non-rectangular counting as a branching problem | OPEN (stated only) | §6.3 |
| T15 | jet-injectivity lemma at `K5` | OPEN | §9.3 |
| T16 | `rank[C;T] <= 4` at `(4^5)`; increment iff `rank C < 4` and `T` nonzero on `ker C`; no Schur-type redundancy theorem available | PROVED | §8.1 |
| T17 | no transverse condition lowers `B` below `a` where `m_det = a`; no padding content | PROVED | §8.2 |
| T18 | sealed inputs used: `C2` necessity and nonzeroness (E3, E6), `-12` witness (E11), `3/896` | ADOPTED from the sealed packet, VERIFIED where recomputed (T7) | §1 |

## 11. Honest negatives and limits

1. No source vector was evaluated; every "realised rank" statement about the five-row
   order-four family is open. The numbers `j_m` are room, not rank.
2. The target-side count beyond order four (how many of the `j_6` source parameters are matched
   by `d^3 F_{u^2}` invariants) was not derived; "order six" statements are about room only.
3. Non-rectangular cells are not covered by the theorem.
4. The `k >= 2` formulas have no numerical control.
5. The six-row question whether the second (`E`-using) order-four condition adds rank is open.
6. Nothing here produces a padding floor, an equation, or a gap; every cell touched is a known
   no-gap cell.
7. Check 1's Sym-power characters were truncated at order six (`r = 6`) and eight (`r = 5`) for
   cost; higher orders are not tabulated.

## 12. Files and receipts

- `checks/c1_normal_space_counts.py/.json` — Check 1 (wall `1.01 s`, exit `0`, Job Object
  receipt `results/logs/c1_normal_space_counts_resources.json`, peak job memory in the receipt).
- `checks/c2_fivevar_order4.py/.json` — Check 2 (wall `3.44 s`, exit `0`, receipt
  `results/logs/c2_fivevar_order4_resources.json`).
- Total numerical wall time: about `4.5 s` of the two allowed checks; no failures, no retries.
- `MANIFEST.json` — SHA-256 of every input listed in §1 and of every file written here; the
  report was finalised before hashing.
