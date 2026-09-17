# Current diagnostic state — the `d = 5`, `λ = (4^5)` source-vector sequence (consolidated handoff)

Claude, 17 September 2026. Covers the sealed packets `routeA_signfilter_20260917/`,
`arc_target_dimension_followup/`, `direct_arc_relation_followup/`, `final_arc_diagnostic/` (this), the
clarification handoff `clarification_20260917/SOURCE_HANDOFF.md`, and Astra's
`astra_gkz_degenerations_20260917/`. Labels: PROVED (characteristic-zero argument or exact integer
computation), CERTIFIED (nonzero modular minor of integer evaluations ⇒ characteristic-zero floor),
SAMPLED (finitely many evaluations modulo one prime; no ceiling), OPEN.

**The cell has `a = m_det = 1`. Nothing here is or can become a positive multiplicity obstruction.** The
diagnostic tests only whether the boundary-compatibility (transverse) mechanism detects a failure that
the existing arc `C` misses.

## 1. Certified source directions and portable definitions

`M = M_{(4^5)}`, `dim M = 5` (PROVED, sealed). Four independent directions (CERTIFIED: `4×5` matrix at
the sealed P6 points, minors `426380, 191230, 255288, 485311, 35010`):

| vector | definition | location |
|---|---|---|
| `q_3` | symmetrised paired contraction, pairing (01)(23), P6 index 3 | `descent_followup_claude_20260916/pilots/p6_basis.json` |
| `q_7` | same, pairing (02)(13), P6 index 7 | same |
| `n02` | same, pairing (02)(13), seed 20260917 | `routeA_signfilter_20260917/certificates/n02_definition.json` (ordered slot lists, plan orders, values) |
| `e` | `H5 ∘ φ`, `e(K5) = 322560` | `SOURCE_HANDOFF.md` §2.2 (formula, evaluators, certificates) |

Conventions: `SOURCE_HANDOFF.md` §1 (slots, ordered epsilon blocks, column tensors, `P = 524287`).
Membership of `q_3, q_7, n02` is by construction (B18-02 Prop. 2.2); `e ∈ E ⊆ ker C` by the global
restriction argument (B19-01 §5). The fifth direction is NOT found. `U := span_Q(q_3, q_7, n02)`.

## 2. Exact rank floors and ceilings

| map | floor | ceiling | status |
|---|---|---|---|
| `C` on `M` | 2 (CERTIFIED, sealed E6) | 4 (PROVED: `E ⊆ ker C`) | `rank C ∈ {2,3,4}` OPEN |
| `C` on `U` | 2 (CERTIFIED) | 3 (dim) | `rank(C|_U) ∈ {2,3}` OPEN |
| `T = (C2, C4_{S1,S2}, C4_{S1,S4})` on `M` and on `U` | 3 (CERTIFIED, minor `225843`) | 3 | `rank T = 3`, `T|_U` injective, PROVED |
| Levi target `F^L` | — | `b_L = 74` (PROVED, two formulations) | uninformative (§7) |

## 3. Global identities that are proved

- `C2`, `C4_{S1,S2}`, `C4_{S1,S4}` vanish on `E` (globally necessary); pairwise and jointly independent on `M`.
- The automorphism-sign theorem (§5) and the covariant factorization (§6), with their stated scopes.
- Skew degree of every element of `M` is `≤ 12` (B19-01 Prop. 3.1); the 13-node extraction is exact.
- Astra: block-scalar and exact-exponent-support tests factor through `C` (§8).

## 4. Relations that remain sampled or modular

- `n02 ≡ 265391 q_3 + 275398 q_7` on the forbidden components at **14 sampled functionals** (six S0 rows at
  P7 points 0–2; eight full rows at P6 points 0–3), modulo `P` only. The coefficients are residues; no
  small-height rational lift exists (bound 2000). Not a global identity.
- Degree-12 rows: rank 1 at all seven recorded points with constant ratios `101007, 295818` (SAMPLED).
- Zero-valued contraction candidates (n05, n07, n09; P8 family) are zero at sampled points only.
- Coordinates `q_3 = 2B(Φ_1,Φ_2)`, `q_7 = 2B(Φ_3,Φ_2)`, `n02 = 2B(Φ_1,Φ_1)` hold exactly at one general
  point (exact integers); as identities of functions they need injectivity of evaluation on the pattern
  span, which is not certified (values have rank 3 there, `dim Cov = 4`).

## 5. The sign-filter theorem (PROVED; `routeA_signfilter_20260917/pilots/autfilter.py`)

If `g ∈ S_5 ≀ S_4` (column permutation with position bijections) maps the set partition `π` to itself and
`ρ` to itself, then `P_{π,ρ} = sign(g)·P_{π,ρ}`, `sign(g) = ∏_j sgn(φ_j) · ∏_{blocks} sgn(reordering)`; a sign
`−1` forces `P_{π,ρ} ≡ 0`; a `g` swapping `π ↔ ρ` with sign `−1` forces `P_{π,ρ} + P_{ρ,π} ≡ 0`. Scope: an
identity of polynomials, valid for any pattern; it explains 13 of 14 recorded P6 zeros and all 19 P2
zeros; it is not a completeness statement (one recorded zero, P6 index 10, is unexplained).

## 6. Covariant factorization (PROVED; verified exactly against sealed values)

Every same-pairing paired contraction factors as `P_{π,ρ} = B(X_{H_1}, X_{H_2})`, `X_H ∈ A⊗A⊗B⊗B` the
partial contraction of one column pair (free legs: `a`-legs of the two `π`-leftover slots, `b`-legs of the
two `ρ`-leftover slots), `B` the symmetric `ε_A ε_B` pairing on `Λ²A⊗Λ²B`; `q = B(X_{H_1},X_{H_2}) +
B(X_{H_1^τ},X_{H_2^τ})`. Each `X_H` is a quadratic `GL(A)×GL(B)`-covariant of the 5-wedge; `dim Cov = 4`
(PROVED by two character routes). The skew-degree-12 part of `X_H` at `Y` equals `X_H` at the point
`(ν_1,ν_2,ν_3,Z_1,Z_2)` of the locus `S*` (cone of decomposable bivectors of `W'`), and linear relations
among restricted covariants are certified exactly on a transversal 5-dimensional slice with 50 poised
points (density: tangent rank 23 under the 18-dimensional group `L̃ ⋉ U_-`). Results: the tops of the
three covariants carrying `q_3, q_7, n02` are exactly independent (rank 3); no isotypic component of
`ν_1∧ν_2∧ν_3∧Z_1∧Z_2` vanishes; hence the "proportional tops" mechanism for `rank(C|_U) = 2` is refuted.

## 7. The Levi bound 74

`F^L`, the `L`-invariant forbidden target (`L` the grading-preserving Levi, connected, no transposition
component), has dimension 74 (70 from skew degree 11, 4 from 12). It is a valid ceiling for `rank C` but
weaker than the trivial ceiling 4 because `L` (dim 11) sees none of the unipotent constraints of `H^0`
(dim 31); the refined target `F''` (pure equations from all of `gl_4 ⊕ gl_4` plus transposition invariance)
is proved to contain `C(M)` but its dimension was never computed.

## 8. Astra's five-block redundancy theorem (PROVED globally, `astra_gkz_degenerations_20260917`)

In the fixed adapted decomposition `(a, r, c, S, v)` every universal forbidden-weight test from
block-scalar scaling, and every exact-exponent-support test, factors through the existing `C`:
`rank(C,T,N) = rank(C,T)` for any stack `N` of such tests. The nine normal-fan classes classify initial
forms of this restricted family, not all arcs or all determinant degenerations. It does not settle
`rank(C|_U)`, the mixed-pairing identity, or transverse independence. Consequence: no more five-block
weights, no stronger test from face degeneration in that family.

## 9. The exact unresolved mixed-pairing statement

Let `Φ_1, Φ_2, Φ_3` be the two-column covariants with (at the general point) `q_3 = 2B(Φ_1,Φ_2)`,
`q_7 = 2B(Φ_3,Φ_2)`, `n02 = 2B(Φ_1,Φ_1)`; write `t_i := Φ_i^{(6)}` (skew-degree-6 part, a function on `S*`)
and `s_i := Φ_i^{(5)}` (skew-degree-5 part; `D^{(2)} = Σ_{k<l} ν_k∧ν_l∧(three W'-vectors)`, so `s_i` is a sum
of three restricted covariants on the loci `S**_{kl}`). Then, exactly,

    z^{[12]}(q_3) = 2B(t_1,t_2),  z^{[12]}(q_7) = 2B(t_3,t_2),  z^{[12]}(n02) = 2B(t_1,t_1),
    z^{[11]}(q_3) = 2[B(t_1,s_2)+B(s_1,t_2)],  z^{[11]}(q_7) = 2[B(t_3,s_2)+B(s_3,t_2)],  z^{[11]}(n02) = 4B(t_1,s_1)

(as identities of functions, conditional on the pattern-span injectivity of §4; unconditionally at the
general point). `rank(C|_U) = 2` ⟺ there are `α, β ∈ Q` with
`4B(t_1,s_1) = 2α[B(t_1,s_2)+B(s_1,t_2)] + 2β[B(t_3,s_2)+B(s_3,t_2)]` and `2B(t_1,t_1) = 2αB(t_1,t_2) + 2βB(t_3,t_2)`
as polynomials in `Y`. The degree-12 equation is sampled-true (rank-1 rows); the degree-11 equation is
the open "mixed-pairing identity". `rank(C|_U) = 3` ⟺ some full-row `3×3` minor is nonzero (none found
on 14 functionals).

## 10. What would suffice

- **This survivor (`rank(C|_U) = 2`, existence + lift):** an exact certificate of the mixed-pairing identity
  (§9) — e.g. an injective evaluation scheme on `F^L_{−1}` (explicit 70-vector basis, ≈ 2 700 runner
  evaluations), or a locus/density argument for the `(t, s)` pairings analogous to §6 — then Proposition
  7.1 of `arc_target_dimension_followup` gives the existence of `n ∈ ker C` with `C4(n) ≠ 0` and the lift
  of the modular candidate. Or, for the negation: one nonzero `3×3` full-row minor (≈ 18 s per new point).
- **Full arc exactness (`rank C = 4`):** two source directions beyond `span(q_3, q_7, e, n02)`... precisely,
  the fifth direction plus full rows giving a nonzero `4×4` forbidden minor; the paired families tried so far
  live in `span(q_3, q_7, e, n02)`.
- **Independence of `T` from `C`:** `rank C ≤ 2` proved (then `dim ker C = 3 > 2 = dim ker T`), or an explicit
  `n ∈ ker C` with `T(n) ≠ 0` (the survivor above), or `dim F'' ≤ 2`.
- **Whether `C` and `T` together isolate `E`:** `rank(C,T) = 4` on `M`; needs the fifth direction and the
  joint rows; currently `rank(C,T) ≥ 3` (from `T` alone) and `≤ 4`.

## 11. Diagnostic progress versus obstruction

Everything above is progress on the *mechanism*: which conditions are redundant with the arc, which are
not, and how the source space is organised (sign filter, covariant factorization, loci). None of it is,
or can be turned into, a multiplicity obstruction in this cell (`a = m_det = 1`); a positive gap would
require a cell with `a > m_det`, which this cell is not.

## Future options (not launched)

1. **Independence hunt, priced:** one wrapped pilot per two new general points (≈ 70 evaluations, ≈ 35 s);
   each adds two full rows; stops at the first nonzero `3×3` minor. Cheap, but cannot prove rank 2, and
   after 14 concordant functionals the prior for rank 3 is low.
2. **Mixed-pairing identity, unpriced in detail:** extend the `S*`-locus method to the skew-degree-5 parts
   (loci `S**_{kl}` with the same group `L̃ ⋉ U_-`), find a transversal slice for the joint `(t, s)`
   arguments, and certify the degree-11 identity of §9 exactly; requires new theory (a density argument on
   a product locus) and roughly 2–4 wrapped pilots of two-column contractions.

Reopening this diagnostic is justified only by (a) a theorem giving an injective evaluation scheme or a
dense-orbit slice for the mixed pairings, or (b) a construction of the fifth source direction outside
`span(q_3, q_7, e, n02)`, or (c) a cell with `a > m_det` where the same mechanism could matter.
