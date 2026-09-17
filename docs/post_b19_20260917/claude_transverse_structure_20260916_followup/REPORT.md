# Follow-up: repaired rank formulas, the injectivity/intersection question, and one dense-evaluator experiment

Claude session, 17 September 2026. Fresh directory `work/claude_transverse_structure_20260916_followup/`
(did not exist at session start). The sealed transverse-structure packet
(`work/claude_transverse_structure_20260916/`, `REPORT.md` SHA-256 `5342a929…`, `MANIFEST.json`
`2c42caa8…`) is preserved byte-for-byte; corrections are in `CORRIGENDUM.md` here (items K1–K9).
Historical files and other sessions' directories are read-only. Written incrementally: §0–§2
were written before the pilot ran; the status line is replaced at the end.

Status: **COMPLETE — outcome 2: fourth-order compatibility certified independent of `C2` on the
known source subspace; arc independence open; injectivity and the intersection condition
unresolved structurally, reduced to a finite map.**

## 0. Session state and scope

`tasklist` at start: no `python` process; only editor/agent shells. The addendum session
`work/descent_followup_claude_20260916_addendum/` is **finished and sealed** (its `MANIFEST.json`
and `FEASIBILITY.md` were last written 04:37 on 17 September; its decision is "feasibility
unresolved", its Stage B never ran, and no continuation was launched). Nothing here duplicates it:
this follow-up uses the sealed *dense* runner at four new transverse points, which that session
explicitly did not do.

Notation (fixed for this document): `M = M_(4^5)` (dim `s = 5`); `E ⊆ M` the determinant
coordinate subspace (dim `m_det = 1`, generator `H5 ∘ phi`); `j : M -> J` the source jet map
through order four, `J = C ⊕ Sym^2(N^*)^{Stab} ⊕ Sym^4(N^*)^{Stab}`, `dim J = 7`; `V = j(M)`;
`L = j(E)` (a line: `H5(u^2) = 322560 != 0`); `L_max` = the target-compatible plane obtained by
leaving the Hessian parameter unspecified, `L_max = span{(1, beta_0, A'), (0, 0, N∘h_4)}`,
`L ⊆ L_max`, `L ⊆ V`. `Ann(X) ⊆ J^*` is the annihilator of `X ⊆ J`; for a family `F ⊆ J^*`,
"rank on `M`" means the rank of `{phi ∘ j : phi ∈ F}` as functionals on `M`.

Limits obeyed: two numerical pilots under `b15_bound.py` (60 s / 512 MiB, one process, one BLAS
thread), 15.6 s of the 120 s total; no carrier search; no arc experiment; no new evaluator; no
historical file modified. This cell has `a = m_det = 1` and cannot yield a positive gap.

## 1. Part A — the repaired linear algebra (summary; exact replacements in `CORRIGENDUM.md`)

- Rank on `M` of all conditions annihilating `L_max`: `dim V − dim(V ∩ L_max)`.
- Rank on `M` of all conditions annihilating `L`: `dim V − dim L` (because `L ⊆ V`).
- The sealed Theorem 6.1(c) substituted `dim L_max` for `dim(V ∩ L_max)` (K1). "At most
  `dim J − 2`" is a dimension in `J^*`, not a rank on `M` (K2). Finite direction families need
  not span the annihilators (§3.3). The Taylor expansion is audited in §3.6 (K5).

## 2. Part C — the experiment: plan and price (written before running)

**Question.** On `span(q_3, q_7)` (the two certified vectors of the sealed packet), are the
order-four rows `C4_{S1,S2}` and `C4_{S1,S4}` independent of the order-two row `C2`?
Not a test of arc independence (`C` is injective on this subspace, sealed E6).

**Inputs.** `p6_basis.json` (slot lists, index 3 and 7, pairings `((0,1),(2,3))` and
`((0,2),(1,3))`), `p7_arc_S0.json` (preserved values at `K5, K5+S1, K5+2S1`; `C2` row), the
sealed `paired_runner.py` (imported unmodified; `evaluate_P` + hand orders `(0,1,2,3)` for `q_3`,
`(0,2,1,3)` for `q_7`, both orientations, recomputed with `hand_plan` and asserted equal to the
stored plans), `b18_02_carrier.py` (SHA-256 `8670040e…`, asserted equal to the pins in both
sealed JSONs), and Check 2's JSON (H5 values, integer `C4` coefficients).

**Point conventions.** Exactly the sealed P7 `K5_tuple`: `Y[i]` is the coefficient matrix of
`x_{i+1}`; `x1` at `(0,1)/(1,0)` and `(2,3)/(3,2)`; `S1 = x1 I` adds `t I` to `Y[0]`;
`S2 = x2 I` adds `t I` to `Y[1]`; `S4 = x1 diag(1,1,0,0)` adds `t diag(1,1,0,0)` to `Y[0]`.
Reused: `K5, K5+S1, K5+2S1` for both vectors. New: `K5+S2, K5+2S2, K5+S4, K5+2S4` for both.

**Price (label-only `hand_plan`, then the sealed measurements).** Max intermediate `4^10 =
1,048,576` int64 entries (8 MiB) per orientation; column tensor `16^5` entries (8 MiB);
`3.4·10^8` flop units per orientation; overflow guard: entries `< 2^19`, at most `4^12` summed
products per einsum, `4^12·P^2 < 2^63`; sealed wall `0.55 s` per symmetrised evaluation and
`219 MB` peak job memory (P7). Planned evaluations: 4 reproduction + 2 corrupted inputs + 1
evenness + 2 degree control + 8 new = **17**, ESTIMATE about 11 s, `< 250 MB`. Pass/fail: any
reproduction mismatch or an unrejected corruption stops the pilot.

**Controls.** (a) Reproduce the preserved `K5` and `K5+S1` values for **each** vector; (b) a
degenerate pencil (repeated `x1` entry zeroed) must fail reproduction — in fact every `z ∈ M`
vanishes there (§5.2), so the expected value is exactly `0`; (c) `Y_2 -> 2 Y_2` must give exactly
`16×` the stored value (degree `4` in `Y_2`); (d) a corrupted `C4` coefficient vector must fail the
exact-zero test on the H5 generator while the true one passes; (e) `q(K5 − S2) = q(K5 + S2)`
(evenness on an actual source vector); (f) `q(K5 + 3S2)` predicted from `t = 0, 1, 2` by an even
quartic (degree `<= 4` on an actual source vector, rank-one update).

**Decision rule.** A nonzero modular `2×2` minor of `[C2; C4_*]` on columns `(q_3, q_7)` certifies
independence of the two functionals over `Q` (integer coefficients, integer evaluations reduced
mod `524287`). Zero modular minors are inconclusive. Either way nothing follows for all of `M`
or for `ker C`.

## 3. Part A in full

### 3.1 The two rank formulas (PROVED)

**Lemma 3.1.** For a subspace `X ⊆ J`: `{phi|_V : phi ∈ Ann(X)} = Ann_V(V ∩ X)`.
*Proof.* `⊆` is clear. Conversely, `psi ∈ V^*` vanishing on `V ∩ X` extends to `V + X` by zero on
`X` (well defined on the intersection) and then to `J`. ∎

**Proposition 3.2.** `j : M -> V` is surjective, so the rank on `M` of `{phi ∘ j : phi ∈ Ann(X)}`
is `dim V − dim(V ∩ X)`. In particular: rank of the E-free family `F_free := Ann(L_max) ∘ j` is
`dim V − dim(V ∩ L_max)`; rank of the E-using family `F_E := Ann(L) ∘ j` is `dim V − dim L`
(since `L ⊆ V`). As `L ⊆ V ∩ L_max`: `rank F_free ≤ rank F_E`, with equality iff
`V ∩ L_max = L`. ∎

At `(5,(4^5))`: `dim L = 1`. If `dim V = 5` (jet injectivity), `rank F_E = 4`; `rank F_free = 4` iff
`V ∩ L_max = L`, and `= 3` iff `L_max ⊆ V` (the only other possibility, `dim L_max = 2`).

### 3.2 What the sealed "missing lemma" concerns (K4)

The sealed Lemma of §9.3 is henceforth statement (i): `ker j = 0`, equivalently `dim V = 5`.
Consequences: `ker F_E = j^{-1}(L) = E + ker j`, so `ker F_E = E` iff `ker j ⊆ E` iff (as
`E ∩ ker j = 0`) `ker j = 0`. `ker F_free = j^{-1}(V ∩ L_max)`, so `ker F_free = E` iff `ker j = 0`
**and** `V ∩ L_max = L`. Injectivity alone does not discharge the intersection condition.

### 3.3 Criterion for a tested family (PROVED)

**Proposition 3.3.** Let `T = {phi_1 ∘ j, …, phi_m ∘ j}` with `phi_i ∈ Ann(L)`. Then
`ker T = j^{-1}(∩_i ker phi_i ∩ V) ⊇ E + ker j`, and

    ker T = E   ⟺   ker j = 0   and   span{phi_i|_V} = Ann_V(L)  (i.e. ∩_i ker phi_i ∩ V = L).

If all `phi_i ∈ Ann(L_max)`, the second condition forces `V ∩ L_max = L` in addition. Equivalently:
`ker T = E` iff `rank T = 4` on `M` (because `dim M = 5` and `E ⊆ ker T`); a certified rank `4` of
`T` on `M` therefore proves `ker j = 0`, the spanning, and (for E-free `T`) `V ∩ L_max = L` all
at once, whereas `ker j = 0` by itself proves none of the spanning. ∎

The finite direction families actually constructed are: order-two functionals in rank-one
directions (all proportional, Theorem 6.2 of the sealed report), and order-four functionals
in rank-one directions `S = ell ⊗ M`, whose `Phi_4`-components are the evaluations
`Phi -> Phi(S_N)`; the set `{S_N : S rank-one}` is a cone of dimension `≤ 14` in the
35-dimensional `N_5`, so **these evaluations need not span the five-dimensional
`(Sym^4 N_5^*)^{Sp_4, *}`** — spanning is an OPEN finite question, not a consequence of anything
proved. Only general symmetric directions (degree up to `20` in `t`, eleven even nodes) can
supply the rest.

### 3.4 The narrowed families (K2)

`F_free = Ann(L_max) ∘ j`: the conditions obtained by eliminating both target parameters
`(F(u^2), kappa~)`; `C2` and every `C4_{S,S'}` belong to it. `F_E = Ann(L) ∘ j`: uses the Hessian
ratio of the ambient generator (`[t^4]/[t^0]` on `H5 ∘ phi`: `13/21` for `S1`, `2/7` for `S2`, `0`
for `S4`, from Check 2), an **ambient-image datum adopted from the evaluation of `H5`**; these
conditions are not independent of ambient-image information and are labelled so wherever used
(§5.5).

### 3.5 Wording (K3)

Every "`C4` vanishes on the ambient line" of the sealed report is to be read as "`C4` evaluates
to zero exactly on the ambient generator `H5 ∘ phi`, hence on `E`"; no statement about the full
kernel of a single condition is made or proved.

### 3.6 Audit of the formal-slice expansion (K5; PROVED)

Write `c(t)^{4d} = 1 + g_1 t + g_2 t^2 + g_3 t^3 + g_4 t^4 + …`, `n(t) = n_1 t + n_2 t^2 + n_3 t^3 + …`
(`n_1 = S_N`), `f_z = z(K) + Phi_2 + Phi_3 + Phi_4 + …` (`Phi_m` the degree-`m` part, a symmetric
`m`-linear form). Multiplying out `c(t)^{4d} f_z(n(t))`:

    [t^2] = g_2 z(K) + Phi_2(n_1,n_1)
    [t^3] = g_3 z(K) + g_1 Phi_2(n_1,n_1) + 2 Phi_2(n_1,n_2) + Phi_3(n_1^3)
    [t^4] = g_4 z(K) + g_2 Phi_2(n_1,n_1) + 2 g_1 Phi_2(n_1,n_2) + Phi_2(n_2,n_2) + 2 Phi_2(n_1,n_3)
            + g_1 Phi_3(n_1^3) + 3 Phi_3(n_1,n_1,n_2) + Phi_4(n_1^4).

**Gauge lemma.** Choose a `tau'`-stable complement `Q` of `Lie(Stab_K)` in `Lie(Gamma)` (`tau'`
normalises `Gamma` — conjugation by transpose sends `(A,B)` to `(B^T, A^T)` — and has finite
order, so a stable complement exists by averaging). The map `Psi(xi, c, n) = c·exp(xi)·(K + n)`,
`xi ∈ Q`, has invertible differential at `(0,1,0)`, so every formal curve through `K` has a
**unique** formal lift. For symmetric `S`, `tau'(K + tS) = K − tS`, and
`tau' Psi(xi, c, n) = Psi(Ad(tau') xi, c, −n)`; uniqueness gives `c(−t) = c(t)`, `n(−t) = −n(t)`.
Hence `g_1 = g_3 = 0`, `n_2 = 0`; with `Phi_odd = 0` (`tau'`-invariance of `f_z`):

    [t^2] = g_2 z(K) + Phi_2(n_1,n_1),      [t^4] = g_4 z(K) + g_2 Phi_2(n_1,n_1) + 2 Phi_2(n_1,n_3) + Phi_4(n_1^4).

The factorization-through-jets conclusion (every Taylor coefficient is a universal linear
function of `(z(K), Phi_2(z), Phi_4(z), …)`) holds with or without the gauge; only the displayed
coefficient in the sealed Theorem 4.4 was wrong. In five variables `Phi_2 = beta_z B`, so
`[t^4] = g_4 z(K) + beta_z (g_2 B(n_1,n_1) + 2 B(n_1,n_3)) + Phi_4(z)(n_1^4)`: the order-four
coefficient mixes in the order-two datum, as the sealed §6.5 item 3 said.

### 3.7 Full-stabilizer check (K6; PROVED, one classical fact ADOPTED)

`Stab_Gamma(K) = {(A, cA^T, g_A) : A ∈ G_r, c^2 det A = 1}` is a connected double cover of the
connected group `G_r` (`GL_4` or `GSp_4`), hence connected: there are no further components
inside `Gamma`. `N` is the unique isotypic component of its type in `T`, hence stable under the
whole stabilizer. The extra symmetry `tau'` acts on all symmetric directions by `−1`, so it
preserves `N ⊆ V_sym` and acts trivially on `Sym^{even}(N^*)`. The image of the stabilizer in
`GL(T)` is `PGL_4` resp. `PSp_4`, and the centre of `SL_4` resp. `Sp_4` acts trivially on `T`, so
the character counts `j_m(r)` computed for `SL_4`/`Sp_4` are the counts for the full symmetry
group of `z` fixing `K`. The `r = 6` commutant statement is ADOPTED as classical; the `r = 5` one
was MEASURED in the sealed Check 1.

### 3.8 The six-row consequence retained (K7)

`dim V ≤ 3`, `dim L = 1` ⇒ `rank F_E ≤ 2`, `rank F_free ≤ 1` on `M_(4^6)`. At most two of the nine
false directions are removable by linear tests factoring through order-`<= 4` jets at `K6`; no
surjectivity of `j` is needed. Whether the second (E-using) condition adds rank is
`dim V = 3` versus `2`, OPEN.

## 4. Part B — injectivity and the intersection condition, structurally

### 4.1 What a flat invariant would have to do (PROVED)

Let `z ∈ ker j` (`z(K5) = 0`, `Phi_2(z) = 0`, `Phi_4(z) = 0`; `Phi_odd = 0`). Then `f_z ∈ m^6`, so
`z(K5 + tS) = O(t^6)` for **every** direction `S` (Theorem 4.4). For a rank-one tuple update
`S = ell ⊗ M` the Plücker vector of `span(Y_i + t ell_i M)` is `p_0 + t p_1` (terms with two
factors `M` vanish), so `z(K5 + tS)`, a quartic in Plücker coordinates, has degree `≤ 4` in `t`
and must vanish identically. Rank-one updates are exactly the points on lines of `Gr(5, 16)`
through `[Pi]`, `Pi = span(Y_i)`; so `z` vanishes on the cone of lines `C_1(Pi) = {Pi' :
dim(Pi ∩ Pi') ≥ 4}` (dimension 15), and by `Gamma`-invariance on `C_1(g Pi)` for every orbit
point, and to order `≥ 6` along the whole orbit `O = H^0·[Pi]` (dimension 20). **Caveat (as
required):** for a general perturbation the Plücker coordinates have degree up to `5` in `t` and
`z` up to `20`; the degree-four bound holds only for rank-one updates, and the sealed
three-point extraction is valid only there.

Conversely `z|_{C_1(Pi)} = 0` gives `z(Pi) = 0`, `beta_z = 0` (the `t^2` coefficient on each
line), and `Phi_4(z)(S_N) = 0` for all rank-one `S`; it does **not** give `Phi_4(z) = 0`, because
the rank-one normal components form a cone of dimension `≤ 14` in `N_5` (§3.3). So "vanishing on
all lines through `Pi`" is weaker than `ker j`.

### 4.2 The rank-one order-four coefficient is a value at a neighbouring point (PROVED; new)

`z` has degree exactly `4` in each matrix slot (`GL_5`-weight `(4^5)`). Hence for `S = x_i ⊗ M`
(adding `tM` to `Y_i`), by multi-homogeneity,

    [t^4] z(K5 + t x_i ⊗ M) = z(Y_1, …, M (slot i), …, Y_5),

the **value** of `z` at the tuple with `Y_i` replaced by `M`; and `[t^2]` is the mixed part of
bidegree `(2, 2)` in `(Y_i, M)`. So:

- the E-using order-four condition for `S1` is the **two-point test**
  `z(I, Y_2, Y_3, Y_4, Y_5) − (13/21) z(K5) = 0`, i.e. the Astra-type finite descent test at the
  pencil `P_1 = x_1 I + x_2 Y_2 + … + x_5 Y_5` (`det P_1 = x_1^4 + x_1^2 (x_2^2+x_3^2+x_4^2+x_5^2) +
  (x_3 x_4 − x_2 x_5)^2`), with ratio `H5(det P_1)/H5(det K5) = 199680/322560 = 13/21`;
- for `S4 = x_1 ⊗ diag(1,1,0,0)` the neighbouring tuple `(diag(1,1,0,0), Y_2, …, Y_5)` is
  torus-unstable: `A = diag(s, s, 1/s, 1/s)`, `(A, A) ∈ H^0`, scales slot 1 by `s^2` and fixes the
  others, so `z = s^8 z` there and **`[t^4] z(K5 + t S4) = 0` for every `z ∈ M`** — the E-using
  `S4` row is identically zero on `M` (observed on `q_3, q_7` and on `H5 ∘ phi`, §5.5);
- the same torus argument at the degenerate pencil (`x_1` entry `(3,4)` removed, `A` as above,
  slot 1 scaled by `s^2`) proves `z = 0` there for every `z ∈ M`, which is why control (b) has
  exact expected value `0`;
- the E-free `C4_{S,S'}` is therefore a combination of two two-point tests and the two
  order-two (genuinely jet) data; its content beyond `C2` lies in `Phi_4`, and §5.4 shows that
  content is nonzero on the source.

This reframes the six-row `J_1, J_2` as values at `(I, Y_2, …, Y_6)` and `(I, Y_2, …, Y_5, I)`,
i.e. the fourth-order transverse condition there is an elimination between two two-point
descent tests and the (automatic) order-two data.

### 4.3 Outcome of the structural attempt

- **Proof of jet injectivity:** not obtained. The line argument gives vanishing on
  `C_1(O)` (dimension `≤ 35` in the 55-dimensional Grassmannian) and order-six vanishing along
  `O`; neither contradicts the existence of a degree-four `H`-invariant section, and the
  Kronecker description `M = (S_(4^5) W)^H`, `dim = 5`, offers no product structure
  (`M_(e^5) = 0` for `e < 4` since `5e` must be divisible by `4`).
- **Explicit flat invariant:** none exhibited; the two certified vectors are not flat
  (`q_3(K5), q_7(K5) ≠ 0`).
- **Reduction to a finite map (precise; cost stated).** Let `b_1..b_5` be a certified basis of
  `M` and `S^(1..D)` rank-one symmetric directions. Form the `5 × (1 + 2D)` matrix
  `F = [ z_b(K5) ; [t^2]_i z_b ; [t^4]_i z_b ]` (three points per direction, exact integers).
  (i) `rank F = 5` ⇒ `ker j = 0` (`F` factors through `j`), and then the used functionals span
  `V^*`, so the E-using tested family has `ker = E` (Prop. 3.3). (ii) With `dim V = 5`, the rank
  of the E-free block (`C2` and the `D − 1` rows `C4_{S^(1),S^(i)}`) is `4` iff `V ∩ L_max = L`,
  and `3` iff `L_max ⊆ V`. (iii) `rank F < 5` is inconclusive for injectivity unless the
  rank-one evaluations are shown to span `(Sym^4 N_5^*)^{Sp_4,*}` (the OPEN spanning question of
  §3.3); a negative would then need general symmetric directions (eleven nodes each).
  Cost: the basis (three more certified vectors — the open carrier problem of the sealed and
  addendum sessions) plus `5 × 2D` dense evaluations, `D = 5`: about `28 s` at the measured
  `0.55 s`, one wrapped pilot. **Not run** (no carrier search authorised).
- **What this follow-up certifies toward it (§5):** `rank F_free ≥ 2` on `M`, hence
  `dim V − dim(V ∩ L_max) ≥ 2` and `dim V ≥ 3`.

## 5. Part C — results

### 5.1 Pilot F1 (stopped by its own control; receipt `results/logs/f1_c4_vs_c2_resources.json`)

Wall `3.9 s`, exit `1`, peak job memory `118 MB`. Pricing and plan orders as in §2 (asserted equal
to the stored P7 plans). Reproduction passed for **each** vector: `q_3, q_7` at `K5` =
`(94237, 491460)` and at `K5+S1` = `(458787, 393135)`, equal to the preserved P7 values. The
corrupted-input control then **failed to reject**: the chosen "corruption" (sign flip at the
repeated `x1` position `(3,4)`) produced the same values. Reason, found and proved: that pencil
is `A K5 A^T` with `A = diag(1,1,1,−1)` and the relabelling `x_3, x_5 -> −x_3, −x_5`
(`g = diag(1,1,−1,1,−1) ∈ SL_5`), a symmetry of every `z ∈ M`; equal values were forced. The
pilot stopped as designed; no value from it is used except as an additional (unplanned)
invariance check.

### 5.2 Pilot F2 (second and last pilot; receipt `results/logs/f2_c4_vs_c2_resources.json`)

Wall `11.7 s`, exit `0`, peak job memory `142 MB`, max intermediate `1,048,576` entries;
17 symmetrised evaluations. All controls passed:

| control | expected | observed | passed |
|---|---|---|---|
| reproduce `K5`, `K5+S1` for `q_3` and for `q_7` | P7 values | equal | yes (each vector) |
| degenerate pencil (`x_1` entry `(3,4)` removed) | exactly `0` for every `z ∈ M` (§4.2 torus) | `(0, 0)` | yes (rejected, and predicted) |
| `Y_2 -> 2 Y_2` | `16 ×` stored: `(459218, 523342)` | `(459218, 523342)` | yes |
| `C4` coefficient corruption (`−27 -> −26`, `−2211 -> −2210`) on the H5 generator | true rows give `0`, corrupted give `322560 ≠ 0` | as expected | yes |
| `C2` row recomputed from preserved values | `(456851, 3402)` | equal | yes |
| evenness `q(K5 − S2) = q(K5 + S2)` | equal | `(372809, 122730)` both | yes |
| degree `≤ 4`: `q(K5 + 3 S2)` from even quartic through `t = 0,1,2` | `(291847, 251770)` | `(291847, 251770)` | yes |

New values (mod `524287`), columns `(q_3, q_7)`: `K5+S2 = (372809, 122730)`, `K5+2S2 =
(299315, 228736)`, `K5+S4 = (196638, 458687)`, `K5+2S4 = (503841, 360368)`.

### 5.3 Rows on the same columns and the minors

| row (integer coefficients on `(z(K5), z(K5+S), z(K5+2S), z(K5+S'), z(K5+2S'))`) | `q_3` | `q_7` |
|---|---|---|
| `C2 = (−177, 112, −7)` on `(K5, K5+S1, K5+2S1)` (preserved) | `456851` | `3402` |
| `C4_{S1,S2} = (−27, −60, 15, 368, −92)` | `30271` | `137059` |
| `C4_{S1,S4} = (−2211, −252, 63, 2576, −644)` | `120670` | `19278` |

`2×2` minors mod `P`: `det[C2; C4_{S1,S2}] = 247396`, `det[C2; C4_{S1,S4}] = 197933`,
`det[C4_{S1,S2}; C4_{S1,S4}] = 281079`; rank of the `3×2` matrix `= 2`.

### 5.4 What is certified, and what is not

- **Certified (characteristic zero).** `C2` and `C4_{S1,S2}` are linearly independent functionals
  on `M` (a nonzero minor of integer evaluations reduced modulo a prime is a nonzero integer
  minor); likewise `C2` and `C4_{S1,S4}`. Hence `rank F_free ≥ 2` on `M`, so
  `dim V − dim(V ∩ L_max) ≥ 2` and `dim V ≥ 3`. A posteriori, the `Phi_4`-component of
  `C4_{S1,S2}` on `J` is nonzero (a `C4` with zero `Phi_4`-component is a combination of
  `z(K5)` and `beta_z` vanishing on `L_max`, hence a multiple of `C2`), which settles the sealed
  T9' positively.
- **Not certified.** Whether `C4_{S1,S2}` and `C4_{S1,S4}` are independent of each other on `M`
  beyond this subspace (`281079 ≠ 0` shows they are independent on `span(q_3, q_7)`, hence on
  `M`; but the rank of `{C2, C4_{S1,S2}, C4_{S1,S4}}` on `M` is only known to be `≥ 2`, the
  subspace having dimension two); the rank of `F_free` on all of `M`; `ker j = 0`;
  `V ∩ L_max = L`; and, above all, whether any transverse row is nonzero on `ker C` — `C` is
  injective on `span(q_3, q_7)`, so nothing about `ker C` is tested here.
- Exact dependence on the two vectors, had it occurred, would have proved nothing about `M`.

### 5.5 Derived rows from stored values only (`pilots/f3_derived_rows.py`, arithmetic, no evaluations)

Using the ambient ratios from Check 2 (`[t^4]/[t^0]` on `H5 ∘ phi`: `13/21`, `2/7`, `0`;
`[t^2]/[t^0]`: `6/7`, `8/7`, `3/7`) — **adopted ambient-image data**, so these rows are E-using:

| E-using row on `(q_3, q_7)` | values | minor with `C2` |
|---|---|---|
| `J_{S1} − (13/21) z(K5)` | `(201275, 262169)` | `165485` |
| `J_{S2} − (2/7) z(K5)` | `(84553, 385022)` | `418521` |
| `J_{S4} − 0·z(K5)` | `(0, 0)` | `0` (identically zero on `M`, §4.2) |

Order-two rows in directions `S2`, `S4` are proportional to `C2` on `(q_3, q_7)` (minors `0`,
consistent with the sealed Theorem 6.2, which predicts exact proportionality on all of `M`); the
`S1` order-two row equals `C2/84` exactly. The vanishing of the `S4` order-four row on both
certified vectors and on `H5` is the torus identity of §4.2, observed exactly.

## 6. Decision

**Outcome 2.** Fourth-order compatibility (`C4_{S1,S2}`, and separately `C4_{S1,S4}`) is
certified independent of the order-two condition `C2` over characteristic zero on the known
source subspace `span(q_3, q_7)`; arc independence remains open (`C` is injective there);
jet injectivity and `V ∩ L_max = L` are not settled structurally (§4) and are reduced to the
finite map of §4.3.

**Smallest further certificate that could decide whether an additional condition detects an
old-arc survivor (not executed; separate assignment required).** An exact vector `n ∈ ker C`
and the three numbers `C2(n), C4_{S1,S2}(n), C4_{S1,S4}(n)`. Exactness of `n` needs the sealed
§C step 4 (all forbidden coefficient polynomials of `n` verified zero), which in practice needs a
certified complete carrier (three more independent vectors) and the interpolation theorem, or a
rank-four forbidden minor (then `ker C = E` and every transverse condition is redundant with the
arc, closing the question negatively). Given the carrier, the transverse side costs
`5 × 4 = 20` further dense evaluations at the four new points (about `11 s`) plus the arc rows
already planned by the sealed packet. A nonzero `T·n` would prove an increment of the transverse
family over the arc in this cell; it would not produce a determinant equation, a bound below
`a = 1`, or a gap.

## 7. Claim ledger (this follow-up)

| # | claim | label | evidence |
|---|---|---|---|
| F1 | rank formulas `dim V − dim(V ∩ L_max)` and `dim V − dim L`; E-free `≤` E-using with equality iff `V ∩ L_max = L` | PROVED | §3.1, K1 |
| F2 | tested-family criterion (`ker T = E` iff `ker j = 0` and spanning; rank `4` on `M` suffices) | PROVED | §3.3, K4 |
| F3 | rank-one evaluations may fail to span `(Sym^4 N_5^*)^{inv,*}` | OPEN (dimension count `≤ 14 < 35` only) | §3.3 |
| F4 | audited Taylor expansion and parity gauge | PROVED | §3.6, K5 |
| F5 | stabilizer connected; `N` stable; counts apply to the full symmetry group | PROVED (one classical fact ADOPTED) | §3.7, K6 |
| F6 | six-row: at most two of nine directions removable through order-four jets at `K6` | PROVED (no surjectivity needed) | §3.8, K7 |
| F7 | `ker j` vectors vanish on `C_1(O)` and to order six along `O`; converse fails | PROVED | §4.1 |
| F8 | `[t^4]` in rank-one direction `x_i ⊗ M` = value at the tuple with `M` in slot `i`; E-using order-four rows are two-point descent tests; `S4` row and the degenerate pencil are torus-forced zeros | PROVED | §4.2 |
| F9 | jet injectivity; `V ∩ L_max = L` | OPEN; reduced to the finite map of §4.3 | §4.3 |
| F10 | reproduction of preserved values for each vector; six further controls | MEASURED, all passed (F2) | §5.2 |
| F11 | F1 corruption control ineffective because the flipped pencil is a stabilizer conjugate | PROVED; F1 stopped as designed | §5.1 |
| F12 | `C2` and `C4_{S1,S2}` (and `C2`, `C4_{S1,S4}`) independent over `Q` on `M`; `rank F_free ≥ 2`; `dim V ≥ 3`; T9' positive | CERTIFIED (nonzero modular minors of integer evaluations) | §5.3–5.4 |
| F13 | anything about `ker C`, about `rank F_free` on all of `M`, or about a gap | NOT REACHED / impossible in this cell | §5.4, §6 |

## 8. Files and receipts

- `CORRIGENDUM.md` — items K1–K9 with sealed line numbers.
- `pilots/f1_c4_vs_c2.py/.json` — first pilot (stopped at its control; `status = reproduction_done`),
  receipt `results/logs/f1_c4_vs_c2_resources.json` (wall `3.88 s`, exit `1`, peak job memory
  `118,149,120` bytes).
- `pilots/f2_c4_vs_c2.py/.json` — second pilot (complete), receipt
  `results/logs/f2_c4_vs_c2_resources.json` (wall `11.72 s`, exit `0`, peak job memory
  `141,914,112` bytes).
- `pilots/f3_derived_rows.py/.json` — arithmetic on stored values only (no evaluations, no
  wrapper).
- Total pilot wall time `15.6 s` of `120 s`; the sealed runner and all historical files unmodified;
  the sealed transverse-structure packet unmodified (hashes re-listed in `MANIFEST.json`).
- `MANIFEST.json` — SHA-256 of inputs and of every file here; finalised after this document.
