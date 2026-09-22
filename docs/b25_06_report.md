# B25-06 — G-A1, the boundary: order-one limits excluded, higher orders reduced to two primitive families

21 September 2026 (UTC). Slot B25-06, Batch 25. Worktree `work/batch15_workers/B23-03`, branch
`b23-03-intersection`. Author: Claude (Opus 5, 1M context). Producer only, unreviewed (G18).
Theory only: **zero pilots, no lease taken, no mathematical program run.** **UNCOMMITTED.**

## Result first

**No smooth-cubic boundary example was found.** Nothing in this report kills the right-way
corner.

**G-A1 itself remains OPEN.** Registered outcome **(3): a partial result with every premise
named.** The pieces:

- **Theorem 1 (PROVED modulo B23-03 Thm 2.1).** Let `A_0` and `A_1` be `4 x 4` matrices of
  linear forms in five variables with `det A_0 ≡ 0`. Then `F = tr(adj(A_0) A_1)`, the
  **order-one limit** `lim_{s→0} det(A_0 + s A_1)/s`, is never of the form `l·C*` with `C*`
  smooth. So every point of `D45 ∩ P5` that is reached by a curve along which the determinant
  vanishes to order exactly one has a singular cubic factor.
- **Theorem 2 (CONDITIONAL on the rank-≤2 classification; its rank-3 part is PROVED by
  hand).** If some `l·C*` with `C*` smooth lies in `D45`, then it is the leading coefficient of
  `det M(s)` for a polynomial curve `M(s)` with `val_s det M >= 2` whose reduction `M(0)` is a
  non-compression singular space of one of two explicit primitive types: the **skew-bordered**
  type or the **W-skew** type (rows are skew forms on a 4-dimensional quotient), or a transpose
  of one of them.
- **Proposition 3 (PROVED modulo one classical finiteness theorem).** Any irreducible component of
  `D45 ∩ P5` that contains a smooth-cubic point has affine dimension `>= 25`
  (projective `>= 24`). The recorded bound, valid for every component, is 19.

**Exact obstruction.** The case where the determinant vanishes to order `k >= 2` and the
reduction is primitive (skew-bordered or W-skew). There the leading coefficient mixes `M_1`,
`M_2`, … and `adj(M_0)` no longer controls it. **Next certificate:** see §6.

Paper 3's determinant-part statements (C36, C37, Question 6.5) are unaffected. Nothing here
edits them.

## 0. Preflight, inputs and conventions

Preflight at 2026-09-21T03:39:40Z: branch `b23-03-intersection`, HEAD
`3bcad66601a586936ce5c76fdf72d9551700dab3` (= baseline), `git status --short` empty. Git was
used read-only (`rev-parse`, `status`, `show`, `cat-file`, `diff --stat`). The route gate was
passed at 2026-09-21T03:55:34Z, with about 16 minutes of substantive assessment, inside the
45-minute limit. Inputs:

| input | locator | SHA-256 (raw bytes read) | status |
|---|---|---|---|
| B25-06 prompt | launch pack `v1_20260921T003934Z/B25-06.md` | `bb5c8f9d…cbb445e` | UNCOMMITTED admin |
| CLAUDE_COMMON.md | same pack | `ef258214…63986dd` | UNCOMMITTED admin |
| COMPUTE_PROTOCOL.md | same pack | `9746d7ce…f8d932c` | UNCOMMITTED admin |
| SOURCE_INDEX.md | same pack | `959733b9…0c54e44` | UNCOMMITTED admin |
| v2 board | `BATCH25_PROPOSED_BOARD_v2.md` | `85777105…613e826` | UNCOMMITTED admin |
| live ledger (B25-06 outcomes) | `B15-12/docs/b25_12_ledger.md` | `b49f2b5b…5a36494` | UNCOMMITTED, live |
| B23-03 report | `3bcad666:docs/b23_03_report.md`, blob `4e60a293…` | `0101f224…7e0a91` | committed; raw = blob content |
| B24-10 review §§6, 9.3, 11.6 | `ab2f8a40:docs/b24_10_review.md`, blob `46edbcb0…` | `da1528ba…a11c2bf3` | committed; raw = blob content |
| Paper 3 §6 and Question 6.5 | `f95742ae:papers/det4-blindness/det4-blindness.tex`, blob `50b1918c…` | blob content `ab69ccbe…678455b` | committed; see note |

Full digests are in `results/b25_06/MANIFEST.json`. For the B23-03 and B24-10 rows, the raw
file and the committed blob content hash identically. **Note on Paper 3:** the
B23-04 working copy is modified (not by me; B25-01 is editing it). I read passages from the
working copy, then checked Question 6.5 against the committed blob: its text is identical. The
modified-copy diff touches none of Thm 6.3, Prop 6.4 or Question 6.5's statement, only
cap-label wording nearby.

**Conventions (the packet's, not extended).** `V = C^5`. A *linear matrix* is an element of
`Mat_4 ⊗ V*`. `D45°` is the set of actual determinants `det A`. `D45` is its closure: 50 aff /
49 proj in `Sym^4 V* = C^70`. `P5` is the closure of all products `l·C`: 39 aff / 38 proj.
`T1, T2, D35, Σ_Π` are as in B23-03 and the packet. `O = C[[s]]`. `val` is the `s`-adic
valuation. For `M(s) ∈ Mat_4(O) ⊗ V*` with `det M ≠ 0`, `lead det M` is the lowest-order
coefficient `F` in `det M = s^k (F + O(s))`. "Smooth `C*`" means that the projective cubic
threefold `{C* = 0} ⊂ P^4` is smooth.

## 1. Route selected, and why (route gate, written before any claim below)

**Route 1 plus route 3**, over the valuation description of `D45`: this is a direct analysis of
the closure of the actual image. Normal forms of divergent pencils are obtained by lattice
(`s`-power) moves, and each reduction is classified from the degrees of `adj(A_0)`'s rank-one
factors. That classification is self-contained. It uses **no Eisenbud–Harris or Ballico
input** in rank 3. The rank-≤2 step uses one classical classification, labelled CONDITIONAL.

Route 2 (a fixed-`l` identity `{C : lC ∈ D45} = D35 ∪ Σ_Π`) was considered and not taken. It
would need exactly the higher-order control that §6 names as the open core.

Two other ideas were assessed and rejected as routes:

- *A sheaf limit:* the flat limit of `coker A_s` on `P^4`. The Hilbert-polynomial and
  global-generation constraints on its parts on `H` and `C*` are satisfiable, so this gives no
  contradiction.
- *Clemens–Griffiths by degeneration:* `J(C*)` inside the limit of the intermediate Jacobians
  `J(Γ_s)`, with `Γ_s` of genus 11. This needs semistable reduction of a singular total space
  and control of restriction maps. Its stable-rationality variant needs the stable
  irrationality of cubic threefolds, which is open. Both would be at best CONDITIONAL on heavy
  UNREAD inputs.

## 2. The valuation description (PROVED, except the one step marked)

**2.1.** *(⇐, PROVED.)* If `M(s) ∈ Mat_4(C[s]) ⊗ V*` has `det M = s^k(F + O(s))` with `F ≠ 0`,
then `F ∈ D45`.
*Proof.* `D45°` is closed under `C^*`-scaling, since `det(cA) = c^4 det A`. So
`s^{-k} det M(s) ∈ D45°` for `s ≠ 0`, and it tends to `F`. ∎

*(⇒, UNREAD-CLASSICAL: curve selection for constructible sets.)* Every `F ∈ D45 \ {0}` arises
this way, for some formal curve. Truncating it at order `k` keeps `F`. This direction is used
only in Theorem 2.

**2.2. Moves that keep `F`.** Constant `(g, h) ∈ GL_4 x GL_4` multiply `F` by `det g det h`.
Diagonal moves `M ↦ D_1 M D_2`, with `D_i` diagonal in powers of `s` and the result still
polynomial, multiply `det M` by an exact power of `s` and leave `F` unchanged.

**Lemma 2.3 (descent, PROVED).** Suppose `M(0)` has, after a constant `(g, h)`, a zero block on
rows `R` and columns `Q` with `|R| + |Q| = p + q >= 5`. Then
`M' = diag(s^{-1} on R, 1) · M · diag(1, s on Q^c)` is polynomial, `lead det M' = lead det M`,
and `val det M' = val det M − (p + q − 4)`.
*Proof.* Entry `(i, j)` is multiplied by `s^{α_i + β_j}` with `α = −1` on `R` and `β = 1` off
`Q`. On `R x Q` the exponent is −1, and `M_{RQ} = O(s)`. Elsewhere the exponent is `>= 0`.
The determinant is multiplied by `s^{−p + (4 − q)}`. ∎

A common kernel vector is a `4 x 1` block. The `(2,1)`-compression has a `3 x 2` block and the
`(1,1)`-compression a `3 x 3` block. **Every compression space descends.**

**2.4. Order one.** `det(A_0 + sA_1) = det A_0 + s·tr(adj(A_0) A_1) + O(s^2)`, by Jacobi's
formula (UNREAD-CLASSICAL, as in B23-03). Write
`B1 := {tr(adj A_0 · A_1) ≠ 0 : det A_0 ≡ 0}`. **`B1 ⊆ D45`** by 2.1, and `F` depends only on
`M_0` and `M_1` whenever `val = 1`.

## 3. Theorem 1 — order-one limits never give a smooth cubic

**Theorem 1 (PROVED modulo B23-03 Thm 2.1).** If `F ∈ B1` and `F = l·C`, then `C` is singular.

**Premises:**
- B23-03 Theorem 2.1 with its fixed-`l` corollary (B23-03 §2.5): every `F = lC ∈ D45°` has
  `C ∈ D35 ∪ Σ_Π`. This is record-PROVED by its producer; B23-10 affirmed it on READ and did not
  replay it.
- UNREAD-CLASSICAL: Jacobi's formula; Gauss's lemma over the UFD `C[x]`; the Koszul syzygies of
  a regular pair; the dimension theorem (two conics in `P^2` meet; a 5-dimensional linear
  subspace meets the 5-dimensional rank-≤1 cone in `C^9` nontrivially).

**Singular reference sets (PROVED):**
- Every `C ∈ D35 ∪ Σ_Π` is singular. For `det_3 M`, a nonzero `x` with `rank M(x) <= 1` exists
  by the dimension count, and every `2 x 2` minor, hence `∇ det`, vanishes there. The
  discriminant is closed, so this holds on all of `D35`. For `C = m_1q_1 + m_2q_2`, `C` is
  singular where `q_1 = q_2 = 0` on the plane `{m_1 = m_2 = 0}`, which is nonempty.
- A reducible cubic `σ q` is singular on `{σ = q = 0} ≠ ∅`. A smooth `C` is irreducible.

**Proof.** If `rank A_0 <= 2` generically, then `adj A_0 ≡ 0` and `F = 0`. So assume generic
rank 3. Then `adj A_0 = σ k κ^T` with `k, κ` primitive and
`deg σ + deg k + deg κ = 3`, so `F = σ κ^T A_1 k`. Assume `C` smooth, and derive a
contradiction in each case. Two definitions:
- `K`, the constant `4 x 5` matrix with `k = Kx` when `deg k = 1`; `a = rank K ∈ {2, 3, 4}`
  (`a = 1` would make `k` non-primitive); `N = ker K`, so `V(k) = P(N)`.
- `K'`, `b` and `N'`, defined the same way for `κ`.

Transposing `(A_0, A_1)` fixes `F`, so each case has a transposed twin.

**(i) `k` or `κ` constant** (this includes `deg σ = 3`). Make column 4 of `A_0` zero. By
multilinearity, `F = Σ_j det(A_0 with column j replaced by column j of A_1)`, and only the
`j = 4` term survives. So `F ∈ D45°`, hence `C ∈ D35 ∪ Σ_Π` (premise), which is singular.

**(ii) `deg k, deg κ >= 1`, so `deg σ <= 1`.** If `σ` is linear and not proportional to `l`,
then `σ | C`, which is impossible. So either:
- **(ii-a)** `σ ∝ l`, `deg k = deg κ = 1`, and `C = κ^T A_1 k ∈ I_k·I_κ`; or
- **(ii-b)** `σ` constant, `(deg k, deg κ) = (1, 2)` (or the transpose), and `lC = κ^T A_1 k`.

**Structure lemma for `deg k = 1` (PROVED).** `A_0 k = 0` makes each row's bilinear form
`β_i(x, y) = r_i(x)·Ky` alternating. Hence `A_0(n) K = 0` for every `n ∈ N`. Then:
- **`a = 4`:** `A_0(n) = 0`, so `A_0` depends only on `y = x mod n`, and each row is
  `y^T Φ_i` with `Φ_i` skew. This is the **W-skew** type, which contains T3. By Gauss's lemma
  over `C[y] ⊂ C[x]`, `k`, `κ` and `σ` also depend only on `y`, so `K'n = 0`.
- **`a = 3`:** `β_i ∈ Λ^2 (C^5/N)* ≅ C^3`. In the basis `C^4 = im K ⊕ ⟨e⟩`, with `u = Kx`,
  `A_0 = [P·S(u) | c(x)]` for a constant `4 x 3` matrix `P`; `S(u)` is the cross-product
  matrix. Its sub-cases:
  - `rank P <= 1` gives `rank A_0 <= 2`, which is excluded.
  - `rank P = 2`: after row operations, rows 3–4 vanish on columns 1–3. That is a
    **`2 x 3` compression block**, with `κ = (0, 0, c_4, −c_3)` linear with `b = 2`, or `κ`
    constant.
  - `rank P = 3`: after row operations `A_0 = [[S(u), c'],[0, c_4]]`, the **skew-bordered**
    type (B23-03 §2.2). Here `κ ∝ (c_4 u, −u·c')`. It is linear iff `c_4 | u·c'`, and then
    `κ = (u, −m)` with `N' = {u = m = 0} ⊆ N`.
- **`a = 2`:** Koszul gives `A_0 = [[y_2, −y_1, d_1, d_2],[0, 0, D]]`, the
  **`(2,1)`-compression**, with a `3 x 2` zero block.

**(ii-a)**, with `C ∈ I_k I_κ`, singular at every point of `P(N) ∩ P(N')`:
- `a = 2`: at `x ∈ P(N)` (a plane), `C(x) = 0` and `∇C(x) = Σ_j g_j(x) ∇k_j`, where
  `g = κ^T A_1` is a vector of quadrics. Only two of the `∇k_j` are independent, so two
  quadrics on `P^2` must vanish, and they have a common zero. **Singular.** The case `b = 2` is
  symmetric.
- `a = 4`: `N ⊆ N'`. **Singular at `P(N)`.**
- `a = 3`: `rank P = 2` gives `b = 2`, done above. `rank P = 3` with `κ` linear gives
  `N' ⊆ N`, singular at `P(N') ≠ ∅`.

**(ii-b)**, with `lC = κ^T A_1 k` and `κ` quadratic:
- **`a = 4`.** `k` generates `m_p` (with `N = ⟨p⟩`), and `κ` consists of quadrics in `y`, so
  `F ∈ m_p^3`. Then `mult_p C >= 3 − mult_p l >= 2`. **Singular at `p`.**
- **`a = 2`.** `A_0` is the `(2,1)`-compression. By Lemma 2.3 with `(p, q) = (3, 2)`,
  `F = det M'(0)` for a linear `M'(0) = [[y_2, −y_1, 0, 0],[Γ, D]]`, where `Γ` is the
  corresponding block of `A_1`. So `F ∈ D45°`, and **singular** by the premise.
- **`a = 3`.** `rank P = 2` forces `deg κ <= 1`, a contradiction. So `A_0` is skew-bordered with
  `c_4 ∤ u·c'` and `F = c_4·(u^T B u) − (u·c')(r·u)`. Here `B` is the top-left `3 x 3` block
  of `A_1` and `r` the first three entries of its row 4. Both terms lie in `I_L^2`, where
  `L = P({u = 0})` is a line.
  - If `l` does not vanish on `L`, then at `x ∈ L` with `l(x) ≠ 0`,
    `mult_x C = mult_x F >= 2`. **Singular.**
  - Otherwise take `l = u_1` (the skew-bordered form is stable under `GL_3` on `u`). Then
    `C ∈ I_L`. Write `C_1` for its part linear in `u`; `C` is singular at `v ∈ L` iff the
    three binary quadrics that make up `C_1(·; v)` vanish at `v`. Two cases:
    - **`c_4 ∈ span(u)`.** The `u`-degree-2 part of `F` is `−(u·c'^v)(u·r^v)`, where
      `c'^v` and `r^v` are the parts of `c'` and `r` in the coordinates along `L`, and it is
      divisible by `u_1`. So `c'^v` or `r^v` is `(f, 0, 0)`, and
      `C_1 = −f(v)·(u·r^v)` or `−f(v)·(u·c'^v)`. **Singular at the zero of `f` on `L`.**
    - **`c_4 ∉ span(u)`.** `c_4 mod u_1` is prime and divides `(u·c')(r·u) mod u_1`, so it
      divides one factor. If it divides the first, `u·c' = c_4 α + u_1 c̃` with
      `α ∈ span(u_2, u_3)`. Then `u_1 | c_4 (u^T B u − α (r·u))` forces
      `u^T B u − α(r·u) = u_1 T`, so `C = c_4 T − c̃ (r·u) ∈ (c_4, c̃)`. So `C` contains the
      plane `{c_4 = c̃ = 0}`, or is divisible by `c_4`. **Singular.** The other factor is the
      same with `c'` and `r` exchanged.

Every case is singular. ∎

**Scope, exactly.** Theorem 1 speaks about the set `B1 ∩ P5`. The singular-factor locus
`{lC : C singular}` is closed: it is the image of `P^4 x disc` under the finite multiplication
map. Therefore `closure(B1 ∩ P5)` is covered too. **`closure(B1) ∩ P5` is NOT covered**: that
is the same intersection-versus-closure trap the packet warns about.

The proof also does not show `B1 ∩ P5 ⊆ T1 ∪ T2`. Cases (ii-a, `a = 4`) and (ii-b, `a = 4`)
give singular `C` that I did not place in `D35 ∪ Σ_Π`. Whether they add singular-cubic
boundary points outside `T1 ∪ T2` is not decided here, and G-A1 does not ask it.

## 4. Theorem 2 — reduction of the whole boundary to two primitive types

**Theorem 2.** Its premises:
- curve selection (UNREAD-CLASSICAL);
- **the classification of spaces of `4 x 4` matrices of rank `<= 2`**: every such space is a
  compression space or lies in a zero-padded `3 x 3` skew space. This is Atkinson–Lloyd and
  Eisenbud–Harris Thm 1.1, **UNREAD**, and it is used only for rank `<= 2`, **so this step is
  CONDITIONAL**;
- Theorem 1.

**Statement.** If `lC* ∈ D45` with `C*` smooth, then there is a polynomial `M(s)` with
`lead det M = lC*`, `val det M >= 2`, and `M(0)` singular, not constant-equivalent to any
matrix with a `p x q` zero block with `p + q >= 5`, and of **skew-bordered** or **W-skew**
type, or a transpose of one of them.

*Proof.* Take `M` by curve selection and apply Lemma 2.3 as long as a block exists. The
valuation drops each time, so the process stops. At the end one of four things holds:
- `val = 0`: then `lC* ∈ D45°`, which Theorem 2.1 of B23-03 excludes;
- `val = 1`: Theorem 1 excludes it;
- `rank M(0) <= 2`: every compression space and every padded skew space has a block with
  `p + q >= 5`, contradicting termination (this is where the CONDITIONAL premise enters);
- `rank M(0) = 3`: the structure lemma of §3 (PROVED, and it uses no EH) leaves only the
  primitive types (a constant kernel, the `(2,1)`-compression and `rank P = 2` all have
  blocks). ∎

The rank-3 half of this reduction is **PROVED** and self-contained. The packet's warning holds:
the reduction says nothing about whether residual degenerations exist or what they give.

## 5. Proposition 3 — dimension of a smooth-cubic boundary component

**Proposition 3 (PROVED modulo Matsumura–Monsky finiteness of `Aut` of smooth hypersurfaces of
degree `>= 3`, UNREAD-CLASSICAL).** Let `Z` be an irreducible component of `D45 ∩ P5`
containing `lC*` with `C*` smooth. Then `dim Z >= 25` aff (`>= 24` proj).

*Proof.*
- `GL_5` is connected and preserves `D45` and `P5`, so it preserves each component; hence
  `Z ⊇ GL_5 · lC*`.
- Let `g` fix `lC*`. By unique factorisation, `g` fixes `[l]` and `[C*]`, so its image in
  `PGL_5` lies in the finite group `Aut(C*)`. The scalars in the stabiliser satisfy
  `λ^4 = 1`. So the stabiliser is finite and the orbit has dimension 25. ∎

This sharpens the record's `>= 19`, which holds for every component, but only for components
that carry smooth-cubic points. Those points form an open subset of `Z`, because the
singular-factor locus is closed.

## 6. What is not excluded, and the next certificate

**OPEN.** Points `lC*`, with `C*` smooth, reached only by curves `M(s)` with
`val det M = k >= 2` and a primitive reduction `M_0`. Their `s^k`-coefficient is a sum of mixed
determinants of `M_0, …, M_k` subject to `tr(adj(M_0) M_1) ≡ 0`, and higher vanishing
conditions. The `adj(M_0) = σkκ^T` structure no longer confines `F` to `I_k I_κ`. Only terms
with three columns from `M_0` see it.

**Single next certificate (theory, paragraph-first, no pilot):** an **order-two analysis over
the two primitive reductions**. For skew-bordered and W-skew `M_0`, either
- find a non-diagonal lattice move (a unipotent `g(s), h(s) ∈ GL_4(C[s, s^{-1}])`) that lowers
  `val` whenever `tr(adj(M_0) M_1) ≡ 0`, which would give `D45 = D45° ∪ B1` up to these types
  and close G-A1 negatively by Theorem 1; or
- exhibit `M_0, M_1, M_2` with `val = 2` and `lead det = lC*`. Then certify `C*` smooth exactly
  (for example, rank `M_6(C*) = 210` modulo one prime, which is a rational certificate because
  210 is the maximum), and certify boundary status by B23-03 Thm 2.1. **That would be the
  corner-killing example, and would be reported first.**

A secondary certificate would remove the CONDITIONAL in Theorem 2: an elementary proof, or a
PRIMARY reading, of the rank-≤2 classification.

**Not claimed:** that G-A1 is closed; that `(D45\D45°) ∩ P5 ⊆ T1 ∪ T2`; anything about
`closure(B1) ∩ P5`; any equation, padding separation, positive gap or lift; anything at `n > 5`
variables or for other padding conventions.

## 7. Labelled ledger (producer only, G18)

| id | claim | label | verification |
|---|---|---|---|
| L1 | valuation description, ⇐ direction (2.1) | PROVED | hand |
| L2 | ⇒ direction | UNREAD-CLASSICAL (curve selection) | — |
| L3 | descent Lemma 2.3; every compression space descends | PROVED | hand |
| L4 | structure lemma for `deg k = 1` (types by `a` and `rank P`) | PROVED, self-contained, no EH | hand |
| L5 | **Theorem 1**: `B1 ∩ P5` has only singular cubic factors; also `closure(B1 ∩ P5)` | PROVED modulo B23-03 Thm 2.1 (record-PROVED, READ-affirmed, not replayed) | hand; **no machine check** |
| L6 | **Theorem 2**: reduction to `val >= 2` with a skew-bordered or W-skew reduction | CONDITIONAL (rank-≤2 classification UNREAD; curve selection) — rank-3 part PROVED | hand |
| L7 | **Proposition 3**: smooth-cubic component `>= 25` aff / `>= 24` proj | PROVED modulo Matsumura–Monsky (UNREAD-CLASSICAL) | hand |
| L8 | G-A1 | **OPEN**; obstruction and next certificate in §6 | — |
| L9 | smooth-cubic boundary example | **none found**; none claimed | — |

**Sources.** READ, PRIMARY for use: B23-03 report (§§2.1–2.6, 4) at `3bcad666`; B24-10 §§6.2,
9.3 fifth item and 11.6 at `ab2f8a40`; Paper 3 Thm 6.3, Prop 6.4, §6.2 and Question 6.5 with
its provenance line at `f95742ae`; v2 board B25-06 lines; ledger B25-06 outcomes.

UNREAD, used only as labelled: Atkinson–Lloyd and Eisenbud–Harris (the rank-≤2 classification,
L6 only); Matsumura–Monsky (L7); curve selection (L2, L6). **Ballico is not used.** Landsberg
`P_{Λ,m}` is not used beyond Paper 3's own remark.

**Verification method:** all by hand. No REPLAY, no independent evaluator, no symbolic check. A
reviewer should re-derive the skew-bordered case (ii-b, `a = 3`) independently. It is the
longest case analysis.

## 8. Resources, files, state

- **Pilots: 0.** Mathematical compute: 0 s. **Lease not acquired, not touched**, and no
  mathematical program ran, wrapped or unwrapped. Non-mathematical shell actions: `date`,
  `sha256sum`, read-only `git`, `ls`, `grep`, `sed`, `cat`.
- **Files created (all UNCOMMITTED, untracked):** `docs/b25_06_report.md`,
  `results/b25_06/STATUS.md`, `results/b25_06/MANIFEST.json`. No `analysis/b25_06_*` script
  exists, because there was no computation. No existing file was edited; Paper 3 and the B23-03
  evidence were not touched.
- **Tool memory:** one note was created in the Claude Code auto-memory
  (`b25-06-boundary-outcome.md`). It is a pointer to this report, and it is quarantined from
  every mathematical premise here (G9′). No other session's memory is a premise.
- Baseline commit: `3bcad66601a586936ce5c76fdf72d9551700dab3`. After-state hashes are in
  `results/b25_06/MANIFEST.json`, which hashes this report and STATUS.md, not itself. **The
  after-state is UNCOMMITTED**, and delivery needs a separately authorised explicit-path pass.
