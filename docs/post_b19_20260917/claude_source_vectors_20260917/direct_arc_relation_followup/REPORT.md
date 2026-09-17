# Direct test of the forbidden-component dependence on `U = span(q_3, q_7, n02)`

Claude session, 17 September 2026. Fresh directory
`work/claude_source_vectors_20260917/direct_arc_relation_followup/`. The two sealed sibling packets
(`routeA_signfilter_20260917/`, `arc_target_dimension_followup/`) and all inherited inputs were
re-hashed at session start and at sealing (31 + 13 outputs, 46 inherited inputs: 0 mismatches, no
unlisted files) and are not modified.

## Verdict

**Outcome C — `rank_Q(C|_U)` is NOT resolved: neither 2 nor 3 is proved.** Everything recorded remains
consistent with `rank C|_U = 2` (the sampled relation and, newly, an exact rank-1 structure of the
degree-12 rows), but the mechanism this session pre-registered to prove it — proportional top parts of
the two-column covariants — is **refuted by exact computation**, and no nonzero `3×3` minor was sought
or found (no new full-row evaluations were made). Transverse independence from the full arc is
therefore not proved; no explicit rational survivor is supplied; the residues `265391, 275398` remain
modular. What is new and proved: (i) every same-pairing paired contraction factors as a symmetric
pairing `B(X_H, X_{H'})` of two-column covariants, and this factorization reproduces the sealed values of
`q_3, q_7, n02` exactly; (ii) the skew-degree-12 parts of these covariants are their restrictions to an
explicit locus `S*`, and linear relations among such restrictions can be certified exactly on a
transversal 50-point slice (a reusable method, validated by controls); (iii) the covariants carrying
`q_3, q_7, n02` are, exactly at the general point, three vectors `Φ_1, Φ_2, Φ_3` with
`q_3 = 2B(Φ_1,Φ_2)`, `q_7 = 2B(Φ_3,Φ_2)`, `n02 = 2B(Φ_1,Φ_1)`, whose top parts are exactly linearly
independent on `S*` (rank 3). The remaining lemma is stated precisely in §C.4.

Resources: three wrapped pilots (0.42 s, 5.6 s, 35.0 s; exit 0, peak memory 14 MB, 193 MB, 462 MB),
plus disclosed unwrapped micro-computations (≈ 8 s), total ≈ 49 s of the 180 s cap; no source-vector
search; no runner evaluation of any source vector.

**Standing reminder.** `a = m_det = 1`: no positive multiplicity gap is possible in this cell. The
question is only whether the transverse mechanism detects a failure the arc misses.

## Part A — the exact statement (unchanged from the pre-registration)

`W = Mat_4 = A ⊗ B`; adapted coordinates per matrix `a, r_k, c_k, Σ, v` (B18-02 §1;
`A(v)_{ij} = −ε_{ijk} v_k`); `z ∈ M` graded by the skew degree `#v`, `z = Σ_{n≤12} z^{[n]}`;
`C(z) := (z^{[12]}, z^{[11]})` (B18-02 Lemma 4.1, B19-01 Prop. 3.1). The identity to decide:

    (∗)  z^{[12]}(n02) − α z^{[12]}(q_3) − β z^{[12]}(q_7) = 0  and  z^{[11]}(n02) − α z^{[11]}(q_3) − β z^{[11]}(q_7) = 0,  α, β ∈ Q,

as polynomials in the 80 variables. `(∗)` for some `(α,β)` ⟺ `rank_Q(C|_U) = 2` (`C` is injective on
`span(q_3,q_7)`, sealed E6). Discovery, certification and global proof are kept apart (§A.2 of the
pre-registration). A nonzero `2×2` evaluation minor on `(Cq_3, Cq_7)` (`104967` at P7 point 0, `171205` at
P6 point 0) fixes `(α, β)` uniquely **if** a global relation exists; it does not prove existence.

## Part B — routes priced; the selected structural route

Route 2 (certified finite identity test in `F^L`, dimension 74) needs an explicit 74-vector basis and
about 2 900 runner evaluations (≈ 22 min): not affordable (pre-registration §B.1). Route 1 was selected.

### B.1 Factorization (PROVED; verified exactly)

Let the pairing be `((X,Y),(Z,W))` and write the leftover blocks `π_5 = (x_5, y_5, z_5, w_5)`,
`ρ_5 = (x_5', y_5', z_5', w_5')`. Summing (2.1) first over all indices of the slots in columns `X, Y` except
the `a`-legs of `x_5, y_5` and the `b`-legs of `x_5', y_5'` gives a tensor `X_{H_1} ∈ A⊗A⊗B⊗B`; similarly
`X_{H_2}` for `(Z, W)`; then `P_{π,ρ} = B(X_{H_1}, X_{H_2})` with
`B(X, X') = Σ ε_A[a_1..a_4] ε_B[b_1..b_4] X[a_1,a_2,b_1,b_2] X'[a_3,a_4,b_3,b_4]`, and
`q = P_{π,ρ} + P_{ρ,π} = B(X_{H_1}, X_{H_2}) + B(X_{H_1^τ}, X_{H_2^τ})` (`τ` = roles of `π, ρ` swapped).
Each `X_H` is a quadratic `GL(A)×GL(B)`-covariant of the 5-wedge `D` (an element of
`Cov = Hom(Sym²Λ⁵(A⊗B), Λ²A⊗Λ²B⊗det_A²det_B²)`; only the `Λ²⊗Λ²` part survives `B`).
**Verification (pilot 3, mod `P`):** the twelve half-tensors of `q_3, q_7, n02`, recombined through `B`,
reproduce the sealed values at P6 point 0 exactly: `260975, 301718, 386346`.

### B.2 Tops live on a locus (PROVED)

Each column determinant has skew degree `≤ 3`, so `X_H` has skew degree `≤ 6` and the degree-12 part of
`B(H, H')` is `B(X_H^{(6)}, X_{H'}^{(6)})`. Expanding `D = Y_1∧…∧Y_5` with `Y_m = Y'_m + Σ_k v^{(m)}_k ν_k`
(`ν_k` the three basis skew matrices): `D^{(3)} = ν_1∧ν_2∧ν_3 ∧ Z_1 ∧ Z_2` with `Z_1, Z_2 ∈ W'`
polynomial in `Y` (the dual Plücker coordinates of the `3×5` matrix `(v^{(m)}_k)` applied to the
`Y'_m`). Hence `X_H^{(6)}(Y) = X_H(ν_1, ν_2, ν_3, Z_1, Z_2)`: **the top part is the covariant restricted to
`S* := {(ν_1,ν_2,ν_3,Z_1,Z_2)}`**, and `S*` is the cone of decomposable bivectors `Z_1∧Z_2 ∈ Λ²W'` (dim 23).

### B.3 The counts (pilot 1, PROVED; `results/p1_covariant_counts.json`)

`m = dim Cov = 4` (plethysm/LR route and weight-pair route agree; constituents: `Λ²(S_{32}A⊗S_{221}B)`,
`Λ²(S_{311}⊗S_{311})`, `Λ²(S_{221}⊗S_{32})`, `(S_{32}⊗S_{221})⊗(S_{221}⊗S_{32})`, one each).
`N_top = dim Hom_L(Sym²(Λ²W'⊗Λ³W_0), Λ²A⊗Λ²B⊗det²) = 26` (two extraction procedures agree), and `18`
through `S_{(2,2)}(W')` (Plücker-reduced). Controls: dimension sums 4368, 3081, 36; small plethysms.
So the pre-registered hypothesis (`m = 2`, `N_top = 1`) fails at the character level.

### B.4 Isotypic vanishing on `S*` (pilot 2, PROVED negative; `results/p2_isotypic_top_vanishing.json`)

With the exact `gl(A)`-Casimir on `Λ⁵(A⊗B)` (4368-dim; eigenvalues 30, 24, 20, 16, 10; minimal
polynomial and trace `87360` verified), **no** isotypic component of `ν_1∧ν_2∧ν_3∧Z_1∧Z_2` vanishes for all
`Z_1, Z_2 ∈ W'` (all 78 basis pairs give nonzero projections in all five pieces). No covariant is forced
to have vanishing top by this argument.

### B.5 Transversal slice certification (method PROVED; `results/slice_choice.json`)

The group `G' = L̃ ⋉ U_-` (`L̃ = GL_3×(C*)³` acting as in the Levi table; `U_-` = left multiplication by
`I + E_{k0}` and right multiplication by `I + E_{0n}`, which fix every `ν_k` pointwise and preserve `W_0`)
acts on `W' = W/W_0` and on `S*`; every covariant restricted to `S*` is `G'`-equivariant (`X_H(g·Y*)`
equals the output action times a character times `X_H(Y*)`, and adding `W_0`-components to `Z_i` does not
change `ν_1∧ν_2∧ν_3∧Z_1∧Z_2`), so its zero set is `G'`-stable. Orbits have dimension 18 at generic points.
For the 5-dimensional slice `V = span(A_1..A_5)` of `results/slice_choice.json`, the tangent directions
of `G'` and of `cone(V)` at the recorded point span the full 23-dimensional tangent space of `S*`
(exact rank 23), so `G'·cone(V)` is dense in `S*` and **a linear combination of restricted covariants
vanishing on `cone(V)` vanishes on `S*`**. Functions on `cone(V)` of the relevant type are quadratic forms
in the ten Plücker coordinates modulo the Plücker relations, i.e. the 50-dimensional `S_{22}(C⁵)^*`; the
50 recorded points `(s,t) ∈ {−1,0,1}^5×{−1,0,1}^5` are poised (evaluation matrix of rank 50), so
vanishing at them is vanishing on `cone(V)`. Controls: a 3-dimensional sub-slice is not transversal
(rank 16), and a deliberately corrupted coefficient is rejected (§Controls).

## Part C — execution and result (pilot 3; `results/p3_covariant_relation.json`)

### C.1 Exact values at the general point (P6 point 0)

Eighteen two-column patterns (the twelve halves `q_k_h1, h1t, h2, h2t` and six random paired
patterns), evaluated modulo three primes (`524287, 599999, 599993`) and reconstructed exactly by CRT
(a-priori bound `331776·(120·3⁵)² = 2.8·10¹⁴ < modulus/2`). Exact rank of the 18 vectors: **3**. Basis
`Φ_1 := X_{q_3\_h1}`, `Φ_2 := X_{q_3\_h2}`, `Φ_3 := X_{q_7\_h1}`; exact coordinates:

| pattern | coordinates in `(Φ_1, Φ_2, Φ_3)` |
|---|---|
| `q_3_h1`, `q_3_h1t` | `(1, 0, 0)` |
| `q_3_h2`, `q_3_h2t`, `q_7_h2`, `q_7_h2t` | `(0, 1, 0)` |
| `q_7_h1`, `q_7_h1t` | `(0, 0, 1)` |
| `n02_h1`, `n02_h1t`, `n02_h2`, `n02_h2t` | `(−1, 0, 0)` |
| random `x0, x1, x2, x3, x5` | `0` (vanish at the point) |
| random `x4` | `(0, −1, 0)` |

Hence, exactly at this point, `q_3 = 2B(Φ_1,Φ_2)`, `q_7 = 2B(Φ_3,Φ_2)`, `n02 = 2B(Φ_1,Φ_1)`
(MEASURED-EXACT at one point; as identities of functions they hold if evaluation at the point is injective
on the span of the patterns, which is not certified: the rank 3 is a floor for that span's dimension).
The vanishing of five of six random patterns at a generic point matches the parent's sign-obstruction
phenomenon at the two-column level.

### C.2 Tops on the slice

`Φ_1, Φ_2, Φ_3` evaluated at all 50 poised points of `cone(V) ⊂ S*` modulo two primes (`524287, 599999`),
CRT-exact (bound `331776·(120·2·2)² = 7.6·10¹⁰ < modulus/2`), balanced-residue float64 BLAS products
verified exact (`4⁸·(p/2)² < 2⁵³`) and cross-checked against the sealed int64 path. **Exact rank of the
three restricted covariants: 3.** Since restriction to the dense-orbit slice is injective on this span
(§B.5), `dim span(Φ_1^{(6)}, Φ_2^{(6)}, Φ_3^{(6)}) = 3` as functions: **the tops are linearly independent;
the proportional-tops mechanism is false.** At slice point 0 the twelve halves' tops are consistent with
the coordinates above (`n02` halves `= −Φ_1` exactly; `q_7_h1` not proportional to `Φ_1`).

### C.3 What this does and does not say about `rank C|_U`

Write `t_i := Φ_i^{(6)}` (top) and `s_i := Φ_i^{(5)}`. Then, exactly in terms of the factorization,
`z^{[12]}(q_3) = 2B(t_1,t_2)`, `z^{[12]}(q_7) = 2B(t_3,t_2)`, `z^{[12]}(n02) = 2B(t_1,t_1)`, and
`z^{[11]}(q_3) = 2[B(t_1,s_2)+B(s_1,t_2)]`, `z^{[11]}(q_7) = 2[B(t_3,s_2)+B(s_3,t_2)]`, `z^{[11]}(n02) = 4B(t_1,s_1)`.
The recorded degree-12 rows are proportional at all five sampled points (exact rank 1 modulo `P`,
constant ratios `101007`, `295818`): with independent tops, this says the pairing `B` restricted to the
top space has (sampled) rank 1 — a genuine structural fact about `B`, not about the tops. The degree-11
rows have sampled rank 2. `rank C|_U = 2` is therefore equivalent to a relation involving the mixed pairings
`B(t_i, s_j)`, which this session could not certify: the `(−1)` functions live in `F^L_{−1}` (dimension 70)
and no injective evaluation scheme for them was affordable. Nothing here excludes `rank C|_U = 3`
either: no new full-row functional was evaluated, so no `3×3` minor beyond the recorded (zero) ones exists.

### C.4 The missing lemma, precisely

Either of the following would finish the question:
1. (**relation route**) An exact certificate of the single identity
   `4B(t_1,s_1) = α·2[B(t_1,s_2)+B(s_1,t_2)] + β·2[B(t_3,s_2)+B(s_3,t_2)]` for the `(α,β)` fixed by the
   degree-12 rows — e.g. by extending the `S*`-locus trick to the skew-degree-5 parts (`D^{(2)} =
   Σ_{k<l} ν_k∧ν_l∧(three `W'`-vectors)`, so `s_i` is a sum of three restricted covariants on the loci
   `S**_{kl}`) and finding a group with dense orbits on the joint locus of `(t, s)`-arguments; or by an
   explicit basis of `F^L_{−1}` (70 vectors) with an injective evaluation set (≈ 70 general points × 13 nodes
   × 3 vectors ≈ 2 700 runner evaluations, ≈ 20 min).
2. (**independence route**) One nonzero `3×3` minor of full forbidden rows on `(q_3,q_7,n02)`: each new
   general point costs 39 runner evaluations (≈ 18 s) and two rows; given the exact rank-1 structure of the
   degree-12 rows, only degree-11 rows can contribute, so the minor must use at least two degree-11 rows.
   This is cheap per point but cannot prove `rank 2`.
Smallest next step: one wrapped pilot evaluating three new general points (117 evaluations, ≈ 55 s); if
all `3×3` minors remain zero the evidence is strengthened only, and route 1 is required.

## Controls

- Nonzero known forbidden minor: the recorded `2×2` minors `104967` (S0, P7 point 0) and `171205` (full,
  P6 point 0) on `(q_3, q_7)`; the `4×4` P6 independence minor `426380` (parent) — replayed, not recomputed.
- Justified zero for the full arc: `e ∈ E ⊆ ker C` (B19-01 §5; S0 constancy checked in the clarification
  packet) — inherited, not re-evaluated.
- Factorization control (new, exact mod `P`): halves recombine to the sealed values of `q_3, q_7, n02`.
- Evaluator lineage: the float64 path agrees with the sealed `contract_pair` int64 path on three halves
  (smoke test); the exact int64 column tensor is a re-implementation of the carrier's Laplace routine
  without modulus; CRT bounds are a-priori (`24⁴` epsilon terms × entry bounds).
- Symbolic-method rejection control: with the corrupted coefficient `λ+1` the relation
  `t(Φ_2) − (λ+1)t(Φ_1)` is nonzero on the slice (and, as it turned out, so is the true-`λ` relation, since
  the tops are independent); the 3-dimensional sub-slice fails transversality (rank 16 < 23).
- Character-level controls (pilot 1): dimension sums 4368 (`Λ⁵`), 3081, 36; `Sym²Λ²C⁴ = S_{22}+S_{1111}`;
  `Λ²Λ²C⁴ = S_{211}`; Casimir minimal polynomial and trace (pilot 2).
- Corrupted-relation control on recorded rows: any `(α', β') ≠ (265391, 275398)` fails the recorded
  relation (the `2×2` system is nonsingular mod `P`), replayed in `verify_records.py`.
- `verify_records.py` (standard library; recomputes the slice geometry with a fresh implementation and
  replays the recorded ranks and bounds; it does not re-evaluate any contraction).

## Resource ledger

| run | wrapped | exit | wall | peak job memory | purpose |
|---|---|---|---|---|---|
| `p1_covariant_counts` | yes | 0 | 0.42 s | 13.9 MB | `m = 4`, `N_top = 26` |
| `p2_isotypic_top_vanishing` | yes | 0 | 5.6 s | 193 MB | no isotypic vanishing on `S*` |
| `p3_covariant_relation` | yes | 0 | 35.0 s | 462 MB | factorization, exact structure, `r_top = 3` |
| unwrapped micro-computations | no | — | ≈ 8 s | — | `N_22 = 18` (0.02 s), slice geometry searches (≈ 2 s), two smoke tests of pilot 3 (≈ 5 s), disclosed |

Total ≈ 49 s of 180 s; three of three wrapped pilots used; no failed receipts; no source-vector search;
no evaluation of any source vector by the runner.

## Proof dependencies of the verdict

B18-02 (2.1), Lemma 4.1; B19-01 Prop. 3.1; the sealed values of `q_3, q_7, n02` at P6 point 0 and the
recorded forbidden rows (parent packets); exact integer arithmetic of pilots 1–3 with the a-priori CRT
bounds stated above; the `G'`-equivariance and density argument of §B.5. No modular zero is used as a
characteristic-zero statement anywhere; the only characteristic-zero rank statements are floors
(`r_top ≥ 3` from an exact nonzero rank on the slice, promoted to equality by the density argument on
the span of the three covariants).
