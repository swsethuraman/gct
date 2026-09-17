# SOURCE_HANDOFF — minimal handoff for a new source-vector session, cell `d = 5`, `lambda = (4^5)`

Claude session, 17 September 2026. All paths relative to `C:/Users/swami/Projects/gct-gpt/`.
SHA-256 values are full in `MANIFEST.json` of this subdirectory; prefixes here. Everything listed
is read-only for the new session; write only in a fresh directory.

Cell facts (all certified in the sealed packets): `s = 5`, `g = 6`, `a = 1`, `m_det = 1`,
`2 ≤ rank C ≤ 4`, no positive gap possible (`a = m_det`). Goal of a new session: **two** further
independent source vectors (§7), not three (§2.3).

## 1. Conventions (row model, `P = 524287`)

- A source point is a tuple `Y = (Y_1, …, Y_5)` of integer `4×4` matrices, `Y_i` the coefficient
  matrix of `x_i`; stored as nested lists `[5][4][4]`, `Y[i][r][c]`.
- Slots `(j, k)`, column `j ∈ {0,1,2,3}`, position `k ∈ {0,…,4}`; position value `c = 4a + b`
  (row `a`, column `b` of the matrix). Column tensor `D_j[c_0..c_4] = det[(Y_i)_{c_k}]_{i=1..5, k=0..4}`,
  shape `(16,)^5`, computed mod `P` by `b18_02_carrier.column_tensor` (Laplace expansion).
- An epsilon block is an **ordered** list of four slots; `pi` blocks contract the row indices
  `a` of their slots, `rho` blocks the column indices `b`, with `epsilon(0,1,2,3) = 1`
  (`b18_02_carrier.EPS4`). `P_{pi,rho}(Y) = sum_c prod_{B∈pi} eps(a_B) prod_{B∈rho} eps(b_B) prod_j D_j[c(j,·)]`,
  and the symmetrised vector is `q = P_{pi,rho} + P_{rho,pi}` (`paired_runner.qval`; the transposed
  term uses the `rho` blocks on rows and the `pi` blocks on columns). Values are integers reduced
  mod `P` (int64 einsum; overflow guard `4^12 · P^2 < 2^63`, `MAX_SUM_LEGS = 12`).
- Membership `q ∈ M`: four full five-wedges give `GL_5`-weight `(4^5)`; five `pi` and five `rho`
  epsilons give `(det A det B)^5`; symmetrisation gives transpose invariance (sealed §3 item 3).
- The pencil `K5`: `Y_1 = E_01 − E_10 + E_23 − E_32`, `Y_2 = E_02 − E_20`, `Y_3 = E_03 − E_30`,
  `Y_4 = E_12 − E_21`, `Y_5 = E_13 − E_31` (0-based indices); `det K5 = u^2`, `u = x1^2 − x2 x5 + x3 x4`.
  Directions: `S1 = x1 I` (add `t I` to `Y_1`), `S2 = x2 I` (add `t I` to `Y_2`),
  `S4 = x1 diag(1,1,0,0)` (add `t diag(1,1,0,0)` to `Y_1`).

## 2. The three known source vectors

### 2.1 `q_3` and `q_7` (full-`H` epsilon contractions; PROVED members of `M`)

File `work/descent_followup_claude_20260916/pilots/p6_basis.json` (`aaee6ec0…`), field `basis`;
generator `pilots/p6_basis.py` (`4365d765…`), seed `20260916`, pairings
`((0,1),(2,3))` for index 3 and `((0,2),(1,3))` for index 7. Ordered slot lists `[column, position]`:

```
q3  pi  = [[0,1],[0,4],[1,3],[1,0]] [[0,0],[0,3],[1,2],[1,1]] [[2,3],[2,4],[3,3],[3,1]] [[2,2],[2,1],[3,0],[3,2]] [[0,2],[1,4],[2,0],[3,4]]
q3  rho = [[0,4],[0,2],[1,0],[1,4]] [[0,3],[0,1],[1,3],[1,2]] [[2,1],[2,4],[3,2],[3,1]] [[2,0],[2,3],[3,4],[3,0]] [[0,0],[1,1],[2,2],[3,3]]
q7  pi  = [[0,1],[0,3],[2,3],[2,0]] [[0,4],[0,0],[2,4],[2,2]] [[1,1],[1,4],[3,4],[3,2]] [[1,2],[1,0],[3,0],[3,1]] [[0,2],[2,1],[1,3],[3,3]]
q7  rho = [[0,4],[0,1],[2,2],[2,0]] [[0,3],[0,0],[2,3],[2,4]] [[1,3],[1,0],[3,3],[3,2]] [[1,2],[1,4],[3,0],[3,4]] [[0,2],[2,1],[1,1],[3,1]]
```

Hand-ordered plans (`paired_runner.hand_plan`, asserted equal in P7 and F2): `q_3` order
`(0,1,2,3)` for both orientations; `q_7` order `(0,2,1,3)` for both. Max intermediate `4^10`
entries. Independence: modular rank `2` of their values at the five P6 points (sealed E5).

### 2.2 `e = H5 ∘ phi` (the ambient generator; PROVED member of `E ⊆ M ∩ ker C`)

- Formula: `e(Y) = H5(det(sum_i x_i Y_i))`, `H5(F) = sum_{sigma,tau,upsilon ∈ S_5} sgn(sigma)sgn(tau)sgn(upsilon)
  prod_{i=1}^5 T_{i,sigma(i),tau(i),upsilon(i)}`, with `T_alpha = alpha! · c_alpha` for the ordinary
  coefficients `c_alpha = [x^alpha] F` (integral convention; the producer's `T' = T/24` convention
  rescales by `24^{-5}`, and the full four-epsilon contraction is `5! · H5`). Exact integers.
- Evaluators: `work/descent_followup_claude_20260916/pilots/p3_c2_derivation.py` (`6cc62417…`,
  function `H5`, sympy determinant of the pencil); the same function in
  `work/claude_transverse_structure_20260916/checks/c2_fivevar_order4.py` (`8f07184b…`) and in
  `clarification_20260917/checks/c1_e_arc_kernel.py` here (`e_of`). Cost: about `1.5 s` per point
  (determinant expansion dominates).
- Certificates: `a = 1` by the Weyl alternant (sealed P1); the B19-02 rectangle certificate
  `work/batch15_workers/B15-02/results/b19_02/rect_4_4_4_4_4.json` (`16aa1626…`, script
  `analysis/b19_02_rect.py` `26f66bc4…`): a highest-weight vector of weight `(4^5)` in the
  19834-dimensional weight space, exact raising residues zero for `E_12, E_23, E_34, E_45`
  (operator nonzero counts `51723`), nonzero at determinant points; by `a = 1` it is proportional
  to the alternant `H5`. Nonzeroness of `e`: `e(K5) = 322560` (sealed P3; recomputed here).
  `E ⊆ ker C`: B19-01 §5; checked here in the S0 convention (§4).
- Values of `e` at every preserved point are in §3 (from `c2_fivevar_order4.json` and
  `checks/c1_e_arc_kernel.json`).

### 2.3 Independence and the carrier count (PROVED; CORRIGENDUM L3)

`C` is injective on `span(q_3, q_7)` and `C e = 0`, `e ≠ 0` ⇒ `q_3, q_7, e` are linearly independent.
Modular confirmation: rows `(q_3, q_7, e)` at the P6 points have rank `3`, minor `475171`
(`checks/c2_three_rows_rank.json`). **Two** further independent vectors complete a basis of `M`.
A candidate `q_a` is independent of the known three iff the `4×5` matrix of `(q_3, q_7, e, q_a)` at
the P6 points has modular rank `4` (a floor, valid over `Q`); with `q_b`, a nonzero `5×5` modular
minor certifies a basis (`s = 5`). Only the P6 points are needed for this step, and the `e` row
there is already computed (§3).

## 3. Preserved point evaluations (mod `P` unless stated)

| point set | source | `q_3` | `q_7` | `e` (exact integer) |
|---|---|---|---|---|
| P6 points 0..4 (`p6_basis.json: points_entries`) | `basis_matrix_pair_by_point` | `260975, 509003, 336756, 260012, 342025` | `301718, 423302, 275526, 317892, 384` | `1133111758001692800, −204681391250300160, −123041748408339456, −7214659371047040, 437311725353472` |
| `K5`, `K5+S1`, `K5+2S1` | `p7_arc_S0.json: C2_values_at_K5_K5S_K52S` | `94237, 458787, 323691` | `491460, 393135, 229099` | `322560, 798720, 4623360` (also `t=3,4`: `18984960, 55864320`) |
| `K5+S2`, `K5+2S2`, `K5−S2`, `K5+3S2` | follow-up `pilots/f2_c4_vs_c2.json` | `372809, 299315, 372809, 291847` | `122730, 228736, 122730, 251770` | `783360, 3271680, 783360, 11105280` |
| `K5+S4`, `K5+2S4` | same | `196638, 503841` | `458687, 360368` | `460800, 875520` |
| P7 S0 points 0,1,2 at `t = 0..3` (`p7_arc_S0.json: points[*].values_t0_t1_t2_t3`) | same | see file (`q10, q11, q12` extracted) | see file | constant in `t`: `−103092282930268800`, `−205527152486400`, `12248442247766400` |
| degenerate pencil (`x1` entry `(2,3)` removed) | F2 control | `0` | `0` | `0` (forced: torus `diag(s,s,1/s,1/s)`) |
| `K5` with `Y_2 -> 2Y_2` | F2 control | `459218 = 16·94237` | `523342 = 16·491460` | `5160960 = 16·322560` |

Hashes: `p7_arc_S0.json` `b84168a2…`, `f2_c4_vs_c2.json` `065ee1d1…`, `c2_fivevar_order4.json`
`aa97511c…`, `c1_e_arc_kernel.json` (this subdirectory, see manifest).

## 4. Old-arc forbidden rows and the S0 extraction (PROVED, with a scope caveat)

- Adapted coordinates per matrix (B18-02 §4): `a = Y[0][0]`, `r = Y[0][1:]`, `c = Y[1:][0]`, lower-right
  `3×3` block `E = Sigma + nu` (symmetric + skew). Arc weights `−1, 0, +1` on `(a, r) / nu / (c, Sigma)`.
  B18-02 Lemma 4.1 (re-derived as B19-01 Prop. 3.1): every monomial of `z ∈ M` has
  `#alpha + #rho = d`, `#alpha + #kappa = d`, weight `2d − #nu`, and `#Sigma = 2d + #alpha − #nu`.
  Forbidden = skew degree `#nu ∈ {11, 12}` (`2d + 1 = 11`, `lambda_1+lambda_2+lambda_3 = 12`).
- **S0 extraction** (`p7_arc_S0.py` `31564d75…`, `S0_point`, `scale_a`): at a point with all
  `Sigma = 0`, only monomials with `#Sigma = 0` survive, so `#nu = 10 + #alpha`; scaling `a -> t a`
  gives `z(t) = z_10 + t z_11 + t^2 z_12` where `z_11, z_12` are the forbidden components
  **restricted to the slice `Sigma = 0`**. Three nodes suffice; the fourth node is a degree control
  (passed at all three P7 points). Rows: `p7_arc_S0.json: rows` (six rows, columns `(q_3, q_7)`),
  modular rank `2` ⇒ `rank C ≥ 2` over `Q` (sealed E6, PROVED floor).
- **Caveat (new, CORRIGENDUM L4).** Forbidden monomials with `#Sigma = #alpha − (#nu − 10) > 0`
  are invisible on the S0 slice. S0 rows are therefore valid for **rank floors** but a vector with
  vanishing S0-sampled forbidden rows is **not** thereby in `ker C`. The complete forbidden
  components at a general point `Y` are obtained by scaling the skew parts `nu -> u nu` and
  interpolating `z(u) = sum_{j=0}^{12} u^j z_j(Y)` from 13 nodes (sealed test plan §3 step 4);
  `z_11(Y), z_12(Y)` are then the full forbidden values at `Y` (13 evaluations per point per vector).
- `e` at the S0 points is constant in `t` (checked exactly here), as `E ⊆ ker C` requires.

## 5. Transverse formulas (PROVED globally necessary; integer coefficients)

- Order two (sealed C2): `C2(z) = 112 z(K5+S1) − 7 z(K5+2S1) − 177 z(K5)`; equals
  `84 · ([t^2] z(K5 + t S1) − (6/7) z(K5))`. Unique order-two condition up to scale in every
  direction (sealed Thm 6.2). Row on `(q_3, q_7)`: `(456851, 3402)`.
- Order four, E-free (`kappa~` eliminated), on `(z(K5), z(K5+S), z(K5+2S), z(K5+S'), z(K5+2S'))`:
  `C4_{S1,S2} = (−27, −60, 15, 368, −92)`, `C4_{S1,S4} = (−2211, −252, 63, 2576, −644)`
  (`c2_fivevar_order4.json: five_variables.C4`; each evaluates to `0` exactly on `e`). Rows on
  `(q_3, q_7)`: `(30271, 137059)`, `(120670, 19278)`; minors with `C2`: `247396`, `197933`; mutual
  `281079` — all nonzero mod `P` ⇒ pairwise independent over `Q` on `M`; the triple's rank on `M`
  is `2` or `3` (undecided).
- Order four, E-using (adopt `[t^4]/[t^0]` on `e`: `13/21` for `S1`, `2/7` for `S2`, `0` for `S4`):
  `J_S(z) − ratio · z(K5)` with `J_S = (z(K5+2S) − 4 z(K5+S) + 3 z(K5))/12`; the `S1` row is the
  two-point test `z(I, Y_2, …, Y_5) = (13/21) z(K5)`; the `S4` row is identically zero on `M`.
- Three-point extraction is valid only for rank-one tuple updates `ell ⊗ M` at `k = 1`.

## 6. Working dense runner and costs (MEASURED)

`work/descent_followup_claude_20260916/pilots/paired_runner.py` (`33c81c96…`) over
`work/batch15_workers/B15-02/analysis/b18_02_carrier.py` (`8670040e…`); wrapper
`work/batch15_workers/B15-02/analysis/b15_bound.py` (`ca001081…`, 60 s / 512 MiB, one process,
one BLAS thread); interpreter `work/batch15_workers/B15-02/.venv/python.exe` (3.12.10).
Per symmetrised evaluation of `q_3` or `q_7` at one point: `0.55 s`, max intermediate `4^10`
entries (8 MiB), `3.4·10^8` flop units per orientation; column tensor `0.07 s`; peak job memory
`142 MB` (F2, 17 evaluations) to `219 MB` (P7). Budget rule of thumb: about 90 evaluations per
60 s pilot including imports. The runner is mod one prime; exact rational reconstruction would need
several primes (the carrier's `P` is a module constant — do not modify the sealed files; copy).

## 7. The two completion routes, sharpened

**Route A — exactness (`rank C = 4`).** Find `q_a, q_b ∈ M` (contractions, membership by
construction) such that the S0 forbidden rows on columns `(q_3, q_7, q_a, q_b)` contain a nonzero
`4×4` modular minor. Since `rank C ≤ 4` (`E ⊆ ker C`, `dim E = 1`), this proves `rank C = 4`,
`ker C = E`, and **every** globally necessary condition (`C2`, `C4`, anything) is redundant with
the arc in this cell. No complete basis and no general points are needed; S0 rows suffice
(floors are valid on the slice). Cost after finding the vectors: `4 × 3 × 4 = 48` evaluations
(about 26 s) plus the P6 independence rows. Note `e` contributes zero rows, so the two new vectors
must carry the missing arc rank themselves; if the S0 rank on four vectors stays `3`, try general
points with 13 nodes before concluding anything (S0 may under-count).

**Route B — a survivor (`n ∈ ker C`, `T(n) ≠ 0`).** Requires all of:
1. a certified basis `(q_3, q_7, e, q_a, q_b)` (nonzero `5×5` P6 minor);
2. **full** forbidden values (13-node skew scaling at general points, §4) for the four
   non-`e` vectors, giving a sampled forbidden matrix `R` on `M`;
3. a global-vanishing certificate: `C(M) ⊆ F_L := ((S_lambda W)_{forbidden})^L` (B19-01 Thm 6.2;
   `L` the grading-preserving Levi of Prop. 6.1), `b_L := dim F_L` computable by branching (recipe in
   B19-01 §6; **not yet computed**). Then either (a) `rank_P R = b_L` — this forces
   `rank C = b_L`, `C(M) = F_L`, and the sample functionals are injective on `C(M)`, so a mod-`P`
   kernel vector of `R` is the reduction of an exact kernel vector of `C` (equal ranks over `Q` and
   mod `P`); or (b) an explicit basis of `F_L` with an invertible `b_L × b_L` sample matrix. A complete
   source basis alone gives neither. Sampled zeros without (a) or (b) certify nothing;
4. `T(n) ≠ 0` for `T ∈ {C2, C4_{S1,S2}, C4_{S1,S4}}` at the seven transverse points (`n` mod `P`
   suffices once step 3 makes it the reduction of an exact kernel vector; a nonzero residue is then a
   characteristic-zero certificate).
If `b_L ≤ 3` turns out true, `rank C ≤ 3 < 4` follows at once and a survivor exists; if `b_L = 4`,
Route A and Route B are the two exhaustive outcomes.

## 8. Failed contraction families and sparse pricing (SAMPLED; no exhaustion claim)

Counts per the addendum corrigendum A (`work/descent_followup_claude_20260916_addendum/CORRIGENDUM.md`
`d0463d99…`), which supersedes the sealed "33 of 35":

| pilot | family | generated / accepted | attempted | points | zero-valued at all sampled points (mod `P`) | nonzero |
|---|---|---|---|---|---|---|
| P2 (`p2_carrier_arc.json` `82c8037e…`) | column-local cyclic shifts | 19 (+400 random, 0 accepted by cost guard) | 19 | 7 | 19 | 0 |
| P4 (`p4_paired_basis.json` `e12e304d…`) | paired blocks, over-strict filter | 0 of 60 | 0 | — | 0 | 0 |
| P6 (`p6_basis.json`) | same-pairing paired blocks | 30 generated, 16 reached | 16 | 5 | 14 | 2 (`q_3, q_7`) |
| P8 (`p8_basis_v2.json` `95a55b0b…`) | priced random and pair-block | 4000 tried, 65 accepted, 19 reached | 19 | 5 (P6 points) | 19 | 0 |
| total | | | **54** | | **52** | **2** |

Distinctness among the 14 P6 zero candidates and the 19 P8 candidates was **not** verified. A zero
value at finitely many points modulo one prime is **not** a global identity, and no bound on the
span of any family was proved: **none of these families is shown exhausted.** The `4^14`-entry
(2 GiB) intermediate that stopped the first P7 attempt was the cost of particular greedy/hand
plans, not a lower bound over evaluators. Sparse pricing (addendum `pilots/q1_price.json`
`5a760d83…`, `FEASIBILITY.md` `05602f27…`): exact support sizes (7680 ordered entries at `K5`,
15360 at `K5+S`), transition bounds `2.9·10^7` (`q_3` at `K5`), `6.4·10^7` (`q_3` at `K5+S`),
`1.5·10^9`–`1.4·10^10` (`q_7`), `7·10^7`–`1.6·10^8` (a cross-pairing pattern); the pre-registered
pass criterion (`< 5·10^6` transitions) failed for every pattern, so the sparse Stage B was not
run; the sparse method is **not shown to exceed the cap**, only unpriceable below it with those
bounds; a compiled inner loop (`numba` present in the environment) was suggested, not tried.

## 9. Proved versus sampled (summary)

| statement | status |
|---|---|
| `q_3, q_7 ∈ M`; `e ∈ E ⊆ M ∩ ker C`; `q_3, q_7, e` independent | PROVED (membership by construction / certificates; independence by the arc argument), plus modular rank 3 |
| `rank C ≥ 2`, `rank C ≤ 4` | PROVED (modular floor of actual forbidden rows; `E ⊆ ker C`) |
| `C2`, `C4_{S1,S2}`, `C4_{S1,S4}` globally necessary | PROVED (vanish exactly on the generator `e`, hence on `E`) |
| `C2`, `C4_{S1,S2}`, `C4_{S1,S4}` pairwise independent on `M` | PROVED (nonzero modular minors of integer evaluations) |
| rank of the triple on `M`; `rank F_free`; `dim V`; `ker j`; `V ∩ L_max` | OPEN |
| any transverse row nonzero on `ker C` | OPEN (no vector of `ker C` other than `e` is known) |
| zero-valued contraction candidates are identically zero; a family is exhausted | NOT ESTABLISHED (sampled only) |
| S0 rows certify `ker C` membership | FALSE in general (slice restriction, §4) |
| `b_L = dim F_L` | NOT COMPUTED (recipe B19-01 §6) |

## 10. Hash table (SHA-256 prefixes; full values in `MANIFEST.json`)

| file | prefix |
|---|---|
| `work/descent_followup_claude_20260916/pilots/p6_basis.json` | `aaee6ec0` |
| `…/pilots/p6_basis.py` | `4365d765` |
| `…/pilots/p7_arc_S0.json` | `b84168a2` |
| `…/pilots/p7_arc_S0.py` | `31564d75` |
| `…/pilots/paired_runner.py` | `33c81c96` |
| `…/pilots/p3_c2_derivation.py` / `.json` | `6cc62417` / `604b3967` |
| `…/pilots/p2_carrier_arc.json`, `p4_paired_basis.json`, `p8_basis_v2.json` | `82c8037e`, `e12e304d`, `95a55b0b` |
| `work/descent_followup_claude_20260916_addendum/CORRIGENDUM.md`, `FEASIBILITY.md`, `pilots/q1_price.json` | `d0463d99`, `05602f27`, `5a760d83` |
| `work/batch15_workers/B15-02/analysis/b18_02_carrier.py`, `b15_bound.py` | `8670040e`, `ca001081` |
| `work/batch15_workers/B15-02/results/b19_02/rect_4_4_4_4_4.json`, `analysis/b19_02_rect.py` | `16aa1626`, `26f66bc4` |
| `work/batch15_workers/B15-01/docs/b19_01_report.md`, `B15-02/docs/b18_02_report.md`, `b19_02_report.md` | `aa136106`, `dca6de94`, `52a9e474` |
| `work/claude_transverse_structure_20260916/REPORT.md`, `checks/c2_fivevar_order4.py` / `.json` | `5342a929`, `8f07184b` / `aa97511c` |
| `work/claude_transverse_structure_20260916_followup/REPORT.md`, `CORRIGENDUM.md`, `MANIFEST.json`, `pilots/f2_c4_vs_c2.py` / `.json`, `pilots/f3_derived_rows.json` | `1c9bd9e5`, `e4254c6a`, `95f41e50`, `428253d2` / `065ee1d1`, `ac072933` |
