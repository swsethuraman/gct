# Corrigendum (clarification addendum) to the follow-up packet

Claude session, 17 September 2026, subdirectory `clarification_20260917/`. The follow-up packet
(`work/claude_transverse_structure_20260916_followup/`, `REPORT.md` SHA-256 `1c9bd9e5…`,
`CORRIGENDUM.md` `e4254c6a…`, `MANIFEST.json` `95f41e50…`) and the sealed packet
(`work/claude_transverse_structure_20260916/`, `REPORT.md` `5342a929…`) are preserved
byte-for-byte. Every item cites the file and section it corrects and gives the replacement.

Standing distinction, unchanged: the nonzero minors `247396` and `197933` (follow-up §5.3)
prove that fourth-order compatibility supplies functionals independent of `C2` on `M = M_(4^5)`;
independence from the old arc `C` remains unresolved (`C` is injective on `span(q_3, q_7)`).

## L1. Stabilizer proof — follow-up `REPORT.md` §3.7 and `CORRIGENDUM.md` K6; sealed Lemma 4.1

**Defect.** "A connected double cover of a connected group is connected" is not a valid inference.
Also, for `A in GSp_4`, `det A = mu(A)^2`, so the `H^0` condition `det A det B = 1` with `B = cA^T`
reads `(c mu)^4 = 1`: four branches before further constraints, not one.

**Replacement.** `STABILIZER.md` here. Summary: the parameter group of the `epsilon = 1` part of the
full stabilizer (in `GL_5 x GL_4 x GL_4`, with the character `chi = det(g)^4 det(A)^5 det(B)^5`)
is `GSp_4 x C^*` (connected), with kernel `{(aI, c)}` and effective image `PSp_4`; the `SL_5`
condition on the induced row action `g` (`det g = (c mu)^{-5}`) selects the single branch
`c mu = 1` inside `SL_5 x H^0`; `chi ≡ 1` on the whole stabilizer (computed, not assumed); the
transpose contributes exactly one further component `tau' : Y -> -Y^T`, acting by `-1` on `N`.
Hence `C[N]^{S_eff} = ⊕_{m even} Sym^m(N^*)^{Sp_4}`, and **all invariant counts and jet-space
dimensions of the sealed Check 1 remain valid** (`j_2(5) = 1`, `j_4(5) = 5`, `dim J_{<=4} = 7`;
six variables `j_2(6) = 0`, `j_4(6) = 2`, `dim J_{<=4} = 3`). Six variables are treated separately
in `STABILIZER.md` §5 (effective `PGL_4 ⋊ <tau'>`; inside `SL_6 x H^0` both branches
`c = ±(det A)^{-1/2}` survive and act identically). Nothing downstream changes.

## L2. Pairwise independence — follow-up `REPORT.md` §5.4, second bullet

**Defect.** The text says the rank of `{C2, C4_{S1,S2}, C4_{S1,S4}}` on `M` "is only known to be
`≥ 2`", then adds that `281079 ≠ 0` shows the two `C4` rows independent "on `span(q_3, q_7)`,
hence on `M`; but …", which reads as if pairwise independence were in doubt.

**Replacement.** *The nonzero modular minor `281079` of integer evaluations proves that
`C4_{S1,S2}` and `C4_{S1,S4}` are linearly independent functionals on `span(q_3, q_7)`, hence on
all of `M`. Likewise each of them is independent of `C2` on `M` (minors `247396`, `197933`). What
two source columns cannot decide is whether the **three** rows `{C2, C4_{S1,S2}, C4_{S1,S4}}` have
total rank `2` or `3` on `M`; on the two known columns their rank is `2` (the maximum possible
there), which is compatible with either.* Consequently `rank F_free ≥ 2` and `dim V ≥ 3` (unchanged).

## L3. Three source directions are already known — follow-up `REPORT.md` §4.3, §6; sealed §9.3

**Defect.** The carrier count "three more independent vectors" (follow-up §4.3, §6, and the sealed
§D.2 wording inherited from the consolidated packet) ignores the known ambient vector.

**Replacement.** Let `e := H5 ∘ phi`, `e(Y) = H5(det(sum_i x_i Y_i))`. Premises, each verified:
(i) `e ∈ E ⊆ M`: `H5` is the unique (up to scale) element of `A_{5,(4^5)}` (`a = 1`, Weyl alternant,
sealed P1 and B19-02 `rect_4_4_4_4_4.json`), and `E = phi^*(A_{5,(4^5)}) ⊆ M` by the row-model
identification (`extension_descent` conventions); (ii) `e ≠ 0`: `e(K5) = 322560` (sealed P3,
Check 2, and `checks/c1_e_arc_kernel.json` here); (iii) `e ∈ ker C`: `E ⊆ ker C` (B19-01 §5); in
the implemented S0 convention this was checked exactly here: at each of the three sealed P7
symmetric-part-zero points, `e(a -> t a)` is **constant** for `t = 0..3` (exact integers,
`c1_e_arc_kernel.json`), i.e. its S0-restricted forbidden components vanish; (iv) `C` is
injective on `span(q_3, q_7)` (sealed E6: nonzero modular `2×2` minor of actual forbidden rows).
*Proof of independence.* If `a q_3 + b q_7 + c e = 0`, apply `C`: `a C q_3 + b C q_7 = 0`, so
`a = b = 0` by (iv), then `c = 0` by (ii). ∎ Numerical confirmation: the rows `(q_3, q_7, e)` at the
five sealed P6 points have modular rank `3` (minor `475171` on columns `0,1,2`,
`checks/c2_three_rows_rank.json`). **Corrected carrier count: `dim span(q_3, q_7, e) = 3`; a
complete five-dimensional carrier needs TWO further independent source vectors, not three.**
`e` is not rebuilt as a contraction; its evaluable formula, normalisation, script and certificate
are documented in `SOURCE_HANDOFF.md` §2.

## L4. Sharpened completion routes — follow-up `REPORT.md` §6 ("smallest further certificate")

**Replacement.** See `SOURCE_HANDOFF.md` §7. In brief:
- **Route A (exactness).** Two further source directions `q_a, q_b` whose old-arc images extend the
  known rank-two image to rank four: a nonzero `4×4` minor of actual forbidden coefficient rows on
  columns `(q_3, q_7, q_a, q_b)` proves `rank C = 4` (with the known bound `rank C ≤ 4` from
  `E ⊆ ker C`, `dim E = 1`), hence `ker C = E` and every transverse condition is redundant with the
  arc. No complete basis is needed; S0 rows suffice for this floor.
- **Route B (survivor).** Construct `n ∈ ker C` and certify `C(n) = 0` **globally**, then show
  `T(n) ≠ 0`. Sampled zeros do not certify `n ∈ ker C`, for two separate reasons stated in the
  handoff: (a) S0 rows see only the `#Sigma = 0` part of the forbidden components (B18-02 Lemma
  4.1: forbidden monomials have `#Sigma = 10 + #alpha − #nu`, which can be positive), so general
  points with the full skew-scaling (13 nodes) are required; (b) even then, finitely many
  evaluations certify `C(n) = 0` only through an injectivity argument on the finite-dimensional
  space `F_L := ((S_lambda W)_{forbidden})^L ⊇ C(M)` (B19-01 Thm 6.2), of dimension `b_L`
  (computable by branching, not yet computed): either an explicit basis of `F_L` with an invertible
  sample matrix, or the observation that a sampled forbidden matrix of rank `b_L` on any set of
  source vectors makes the sample functionals injective on `C(M) = F_L`. A complete source basis by
  itself supplies neither.

## L5. Ledger corrections — follow-up `REPORT.md` §7

| entry | correction |
|---|---|
| F5 | proof replaced by `STABILIZER.md`; statement unchanged |
| F12 | add: `C4_{S1,S2}` and `C4_{S1,S4}` independent of each other on `M` (minor `281079`); the triple's rank on `M` is `2` or `3`, undecided |
| new F14 | `q_3, q_7, e` linearly independent (PROVED, and modular rank `3` at the P6 points); two further vectors complete the carrier |
| new F15 | S0-sampled forbidden rows are restrictions to `#Sigma = 0`; valid for rank floors, insufficient for kernel certification (PROVED from B18-02 Lemma 4.1) |

## L6. Checks run in this addendum (arithmetic only; no contraction of any source vector)

- `checks/c1_e_arc_kernel.py` → `c1_e_arc_kernel.json`, under the Job Object wrapper
  (`results/logs/c1_e_arc_kernel_resources.json`: wall `19.4 s`, exit `0`): `e` at the three P7 S0
  points for `t = 0..3` (constant, three points), `e` at the five P6 points, `e(K5) = 322560`,
  `e` at the sign-flip conjugate (`322560`), at the degenerate pencil (`0`), at `Y_2 -> 2Y_2`
  (`16 × 322560 = 5160960`).
- `checks/c2_three_rows_rank.py` → `c2_three_rows_rank.json` (plain arithmetic, no wrapper): rank
  `3`, minor `475171` mod `524287`.
No carrier search, no new engine, no historical file touched.
