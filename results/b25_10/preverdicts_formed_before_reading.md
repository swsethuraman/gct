# B25-10 — risks and pre-verdicts formed before opening any Batch 25 producer packet

Written 2026-09-22T14:35Z (UTC), before any `b25_0*` report, paper after-state, or diff was opened.
UNCOMMITTED. Not edited after writing; later blocks are appended with their own timestamps.

## 0. Exposure disclosure (read this first)

I am **not** a clean-room reader. Before writing this file I had been exposed to producer
conclusions through three channels, and I do not backdate anything:

1. **The launch prompt `B25_REVIEW_LAUNCH_20260922.md`** (integrator) states: B25-05 "claims to
   prove (★)" via "§A.3"; B25-02 repaired Theorem 9.1 with "the reversed Prop. 6.1 inequality it
   depends on" and "the new B17-01 dependency in Theorem 6.2"; B25-01 has a "Corollary 4.5
   placement" and a "C11 label"; Paper 2 needed a one-line integrator byte edit at line 653 to
   build; Paper 1's `.tex` is unchanged at `241da4db`.
2. **Tool memory index (`MEMORY.md`) loaded into this session's context** contains one-line
   summaries written by other sessions: "B25-05 … s73 (★)=isotypic_rank Prop 5, PROVED;
   equivariance (c)"; "B25-01 … five edits applied … D2′=C51 Cor 4.5 … after-state uncompiled";
   "B25-02 … Thm 9.1 repaired; Thm 6.2 closure now ADOPTED (B17-01)"; "B25-04 … disconnected
   fillings factor and never separate below D*; spans/connected open; membership cert ~1e161";
   "B25-06 … order-one limits exclude smooth-cubic padding; residue val≥2 skew-bordered/W-skew;
   G-A1 OPEN". **These are producer tool memory. I quarantine them from every mathematical
   premise** and use them only as a list of claims to check. I created no tool memory before this
   file.
3. **B24-10 (my own prior slot, committed at `ab2f8a40`)** — the governing baseline, not a
   producer conclusion.

## 1. Risks derived from the assignment and the old baseline

### (★) — the label-changing result (highest risk)

- R1. **Which (★)?** SOURCE_INDEX warns two different (★) exist: s73's N=9→7 isotypic restriction
  and stabiliser_reduction.md's Bruhat/monomial criterion. A proof of the wrong one is worthless.
- R2. **What does the floor actually need?** B24-10 §3.2(ii): the ambient multiplicity `a=6`
  agreeing at N=9 and N=7 is not the claim. The floor needs that the **ideal-copy count**
  `i_det ≥ 1` established by LMR for `closure(GL_9·det_3)` in `S^12(S^3 C^9)` survives to
  `D_7 ⊂ S^3 C^7`. My pre-verdict on the mathematics: the natural proof is that restriction of
  polynomial functions along a *linear* inclusion `C^7 ↪ C^9` (or the projection) maps the
  `λ`-isotypic component of `C[S^3 C^9]_12` to that of `C[S^3 C^7]_12` for `ℓ(λ) ≤ 7`
  isomorphically on highest-weight vectors (inheritance / multiplicity stability: HWVs of weight
  λ with ℓ(λ) ≤ 7 only involve the first 7 variables), and that the ideal of the orbit closure is
  compatible because `D_7 = D_9 ∩ S^3 C^7` **or** `D_7` = image of `D_9` under projection.
  **Which of the two** is exactly where proofs go wrong: for ideals, the correct statement uses
  the projection `π: C^9 → C^7` (closure of GL_7-orbit of the padded det lies in the image), and
  the standard inheritance lemma (e.g. Bürgisser–Ikenmeyer / Kadish–Landsberg "padding",
  Landsberg's book) says `I(D_N)` HWVs of weight λ with ℓ(λ) ≤ M correspond to those of `I(D_M)`
  when both N, M ≥ the "stability" bound (for det_3 padded: need N, M ≥ 9? or ≥ ℓ(λ)?). **Risk:
  the proof needs M ≥ 9 (the number of variables of det_3 itself = n² = 9) and N=7 < 9 is below
  that.** For N < n², `D_N` is *not* the orbit closure of det_3 in the usual sense — det_3 needs 9
  variables; at N=7 one uses the padded/restricted object. This is my central pre-registered
  question: **is the object at N=7 actually defined as a restriction/projection of the N=9 one,
  and does the HWV correspondence hold for ideals (not only for coordinate rings) at N=7 < 9?**
- R3. Pre-verdict: the equality `mult_λ(I(D_9)) = mult_λ(I(D_7))` for ℓ(λ) ≤ 7 is plausible and
  is a standard inheritance result **if** `D_7 := D_9 ∩ S^3 C^7` equals `π(D_9)` (both hold for
  GL-stable closed cones via `π∘ι = id` and GL_9-stability: `ι(π(p)) ∈ closure(GL_9 p)`).
  The key lemma: for a GL_N-stable closed cone `X ⊂ S^d C^N`, `X ∩ S^d C^M = π(X)` (π the
  coordinate projection, as a limit of diagonal matrices), and then HWVs of weight λ, ℓ(λ) ≤ M,
  in `C[X]` restrict injectively. I will accept a proof that establishes: (a) the N=7 object is
  defined as `D_9 ∩ S^3C^7` or equivalently; (b) the lowest-/highest-weight-vector correspondence
  for ideals, with the direction that gives `i_det(7) ≥ i_det(9)` (the floor direction). Only the
  **≥** direction is needed. **Failure modes:** proof of multiplicity equality in the coordinate
  ring only; use of a weight convention (highest vs lowest, U vs U⁻) that silently flips which
  variables are retained; a statement at ℓ(λ) ≤ 7 that is actually proved only for ℓ(λ) < 7.
- R4. The integrator's memory calls it "isotypic_rank Prop 5". If the proof is **a citation to a
  record-internal computation** (a rank measured at N=7), it is CERTIFIED-modular at best and
  does not make (★) PROVED. Must be a proof.

### Paper 3 (B25-01)

- R5. Five edits: G-30 (C48/row-1, N=5..8 elementary), G-31 (C45 PROVED mod (★), Thm 2.3.1),
  G-32 (C11 → PROVED modulo three ADOPTED inputs), G-36 (D2′ own claim ID, witness named,
  "closed" in hypothesis, kind≠mechanism), and a fifth. Risks: "three negative controls" leaking;
  D(k) range quoted unrestricted (must be k ≥ 3, positive for k ≥ 10); §E's "same kind" wording
  surviving; C45 losing "(★)" or gaining "PROVED" before this review; cap label flat anywhere.
- R6. Corollary numbering: if D2′ is placed as "Cor 4.5" the shared counter must make it 4.5 in
  the built paper; check source order.
- R7. G-A1 must remain OPEN; B25-06 may try to move it; B25-06 gates no paper.
- R8. Onset inequality `deg f ≥ onset I(D35 ∪ Σ_Π)` must remain cubic-side (Σ_Π not T2).

### Paper 2 (B25-02)

- R9. B2: the repair must be the three-clause statement. Pre-verdict: `Δ ≤ 0` for ℓ ≤ 4 at
  every degree is degree-free **only if** it follows from a containment; any sentence claiming
  `mult_det = a` at all degrees for ℓ = 4 is false (principal ideal of the degree-e hypersurface).
  The launch prompt says the repair depends on a "reversed Prop. 6.1 inequality". **Risk:** if
  Prop 6.1 was reversed, B24-10 §5.1/5.2's "Δ ≤ 0 from Prop 6.1 containment" argument may have
  been reading the old (wrong-direction?) inequality. Must re-derive direction from first
  principles: `D^perm ⊆ D^det` (padded permanent lies in the det orbit closure at n where the
  permanent has a determinantal formula) ⇒ `C[D^det] ↠ C[D^perm]` ⇒ `mult_λ C[D^perm] ≤
  mult_λ C[D^det]` ⇒ Δ := mult_perm − mult_det ≤ 0 (with the record's sign convention to be
  confirmed). The containment direction must be checked for n=4: is `D^perm_4 ⊆ D^det_4` actually
  known? perm_4 has determinantal complexity ≥ 7 > 4, so at *equal* matrix size it is **not**
  contained. The containment must be into a larger det orbit closure (D^det_m with padding).
  This is a real risk: which m, which padding.
- R10. B3: gate ℓ ≥ 5. B4: `[−4,−2]` conditional on ADOPTED `dim N13 = 73`. B1: Kadish–Landsberg
  direction checked at PRIMARY source, not from the record.
- R11. Cap label in abstract and Thm 7.1 must be "PROVED modulo …". Beauville read PRIMARY with
  exact statement used.
- R12. "Thm 6.2 closure ADOPTED (B17-01)": a new dependency introduced during repair must be
  labelled and B17-01's status checked; must not be silently PROVED.
- R13. Build: integrator's one-line edit at line 653 is a byte change by a non-producer; the
  reviewed after-state is `39d15aea` (raw) — I review that, and the edit itself.

### Paper 1 (B25-03)

- R14. Six paths bound; "LMR Prop 3.5.1 constructs P2" confirmed or withdrawn from PRIMARY source;
  attribution patch unapplied (`\cite[Cor.~7.2]{BI}` count 0); author credit unchanged;
  "one signature" checked against full blocker list. Paper `.tex` unchanged at `f52f8d16` (LF blob).

### Research

- R15. B25-04: cheap evaluation ≠ separation; "never separate below D*" is a restatement of B24-04
  Thm 1 unless a new object; cost ~1e161 must be a certification cost, not a claim.
- R16. B25-06: "exclude smooth-cubic padding from the boundary" is a global exclusion; needs proof
  not sampling; order-one limits only ⇒ scope is order-one limits, not the whole boundary; G-A1
  stays OPEN unless the full boundary is covered.

## 2. Pre-verdicts (to be confirmed or overturned in the review)

- PV1. (★): accept as PROVED only if the proof establishes the ideal-level inequality
  `i_det(N=7) ≥ i_det(N=9)` (or equality) for λ=(19,7,2^5) from a lemma of the form
  `X ∩ S^d C^M = π_M(X)` plus HWV restriction, with the N<n² subtlety handled. Expected outcome
  if the proof is only multiplicity-in-coordinate-ring: REPAIR.
- PV2. Paper 3: PROCEED to build/author check, conditional on no C45 upgrade applied pre-review.
- PV3. Paper 2: REPAIR likely remains (16 blockers); B2 repair acceptable only if three-clause.
- PV4. Paper 1: PROCEED for readiness only if the LMR Prop 3.5.1 finding is decided from PRIMARY.

---

## Block 2 — appended 2026-09-22T14:50Z, after reading B25-05 only

(★) ruling formed after reading `2688efd1:docs/b25_05_report.md` and the record anchors
(`82633a60:docs/s73_report.md` §1, `82633a60:docs/isotypic_rank.md` Lemmas 3–4/Prop. 5,
`5a97317e:results/b24_02b/lmr_quotes.md` Q1, Q5, Q6). My pre-registered R2 worry (N = 7 < n² = 9)
**does not bite**: `D_7` is *defined* (s73 §1) as the pencil closure `closure Φ_f((M_3)^7)`, which is
the closure of the restriction image `ρ(GL_9·f)`; R4–R5 use vanishing only, so no orbit structure at
N = 7 is needed. PV1's criteria (ideal-level, floor direction, ℓ(λ)=7 closed) are met.
Independently re-derived: E_ij sign convention from `(g·F)(v) = F(g^{-1}v)`; `ρ^* c_α = c_{(α,0)}`;
R2 for i ≥ r; A_i = columns of g^{-1}; R5. LMR Ω(4,3) = 12ω1+5ω2+2ω7, degree (k+2)(d−1) = 12 ⇒
λ = (19,7,2^5). Noted independently: LMR §3.2's *general* printed formula also carries the halved
ω_1 coefficient n(n−1)(n−2) (=6 at n=3, size 30 ≠ 36); the correct coefficient is 2n(n−1)(n−2),
which Thm 2.3.1's Ω(2n−2, n) gives. B25-05 uses the example and Thm 2.3.1, not the §3.2 general
formula — correct, but the §3.2 general formula must not be cited either.
Pre-verdict before opening any paper after-state: **(★) PROVED; C45 → PROVED with LMR Thm 2.3.1
+ §3.1 as its one external input (PRIMARY, statement level).**

---

## Block 3 — correction, appended 2026-09-22T14:45Z

Block 2's heading says "appended 2026-09-22T14:50Z". **That time is wrong**: I wrote an estimate
rather than reading the clock. `date -u` read 2026-09-22T14:41:03Z at my first download after
Block 2 was written, so Block 2 was appended **before 14:41:03Z**. Block 2's text is left as
written; this correction governs its time. Order is unaffected: Block 2 was written after reading
B25-05 and before opening any paper after-state.
