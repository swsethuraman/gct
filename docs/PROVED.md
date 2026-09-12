# PROVED — the index of established results

**Read this before writing a brief and before starting work.** Every entry is a
result that exists; citing it is cheaper than re-deriving it. Batch 13 paid for
this file three times over: B13-02, B13-03 and B13-04 each independently
re-derived S4's fixed-factor lemma, and B13-11 nearly reported nineteen false
open candidates because the board never cited `docs/n4_gate.md`.

Machine-applicable exclusions — those with a predicate over `(n, r, δ)` — also
live in `results/integrate/inherited_exclusions.json`, which
`tools/integrate/reconcile_cells.py` joins against the cell catalog. **A result
that excludes a family belongs in both.** Keeping them apart is what let batch 13
close the same cells twice.

Status: **PROVED** (theorem with a proof in the tree) / **CERTIFIED** (exact
statement over ℚ carried by a replayable artefact) / **ADOPTED** (taken from the
record or the literature, cited).

---

## A. Structure of the cubic ideal

| id | statement | status | source |
|---|---|---|---|
| `washout_thm2` | `D_k^{per₃} = Sym³Cᵏ` for `k ≤ 5`, so `I(D_k^{per₃})_δ = 0` at **every** degree | PROVED | `docs/washout_lemma.md` Thm 2 + Thm 3(1); exact full-Jacobian rank 35 at both primes; **re-derived from its generator by B13-07** |
| `restriction_lemma` | a HWV of weight `μ`, `ℓ(μ) = k < r`, sees only `F\|_{Cᵏ}`; hence `mult_μ C[D_r]_δ = mult_μ C[D_k]_δ`. **A shorter weight's `units` is its length-`k` value at every degree.** | PROVED | `docs/washout_lemma.md` §1; proved from source by B13-07 |
| `length6_record` | `I(D_6^{per₃})_δ = 0` for `δ ≤ 9` | PROVED | δ≤6 Pieri+s37; δ=7 s41+s43 (27); δ=8 +s47 (91); δ=9 s79 (210). Counts reproduced by B13-05, B13-07, B13-09, B13-11 |
| **`degree8_global`** | **`I(D_r^{per₃})_δ = 0` for every `r` and every `δ ≤ 8`; hence `mult_pad = mult_red` at every weight of every length in every degree ≤ 8** | PROVED | **RECONCILIATION RESULT — stated by no single session.** ℓ≤5 `washout_thm2`; ℓ=6 `length6_record`; ℓ=7 at δ=8 B13-09 (all 42); ℓ=8 at δ=8 B13-05 top cells (all 6); `length_bound` closes the list |
| `length_bound` | constituents of `I(D_r^{per₃})_δ` satisfy `6 ≤ ℓ(μ) ≤ min(r, δ)` | PROVED | B13-05 Theorem A. **The `, 9` clamp recorded here until now is WITHDRAWN.** The justification given for it — above 9 nothing new appears, the family pulls back along `Cʳ → C⁹` — yields that no *new* constituent of length ≤ 9 appears above `r = 9`. That is not the statement that no constituent of length > 9 exists; the equations of "supported on ≤ 9 variables" are the obvious candidate at `r, δ ≥ 10`. Nothing depended on it: all 1,846 catalogued cells have `ℓ ≤ 9`, so the clamp never bound. Caught by Astra, batch-13 reconciliation |
| `bip_blind_at_n4` | the BIP mechanism does **not** reach `n = 4`, and not because its constants are small: its reach is measured in weight **length**, which at `n = 4` is `ℓ(λ) ≤ 4`, while permanent-sensitivity begins at `ℓ(λ) = 6`. Every determinant-side point the argument supplies at `n = 4` is a product of four linear forms with span `≤ 3`, and a weight vector of weight `λ` vanishes at every point of span `< ℓ(λ)`. So its whole supply of evaluation points is identically blind to every weight of the census | PROVED + MEASURED | `docs/bip_transfer.md` (s52), verified in-house at three six-row cells — the HWV vanishes at all eight points and is nonzero at a determinant pencil in the same run. **Therefore `a = 1` cells are "excluded by convention, not by theorem"** (`docs/dip_transfer.md` §3, s37). `inherited_exclusions.json` carries no occurrence predicate, so the machine ledger never depended on it. The one piece that does transfer is Kadish–Landsberg `\|λ̄\| ≤ md`, which at `(n,m) = (4,3)` reads `λ₁ ≥ δ` — numerically identical to the programme's own eligibility gate |
| `top_cells_catalecticant` | cells with `ℓ(μ) = δ` are indexed by strict partitions, have `a = 1`, and their HWV space is spanned by a `δ×δ` **maximal minor of the second catalecticant**. So `i(μ,δ) = 0` iff one exact integer determinant is nonzero. | PROVED | B13-05 Theorem C, via Littlewood `e_δ[h₂] = Σ_{ν strict} s_{(ν\|ν−1)}`. **Replaces an `N_S`-sized rank with a 0.01 s determinant.** |
| `ideal_ladder` | `i(μ,δ) ≥ 1 ⟹ i(μ+ν, δ+δ′) ≥ 1`; contrapositively `i(μ+ν, δ+δ′) = 0 ⟹ i(μ,δ) = 0` | PROVED | B13-05 Theorem D. **Ordering tool, not a pruning tool** at these degrees |
| `ladder_converse` | **`a(κ,p) ≥ 1` and `a(ν,q) ≥ 1`** and `i(κ,p) = i(ν,q) = 0` `⟹ mult(κ+ν, p+q) ≥ 1`; with `a = 1` this closes the cell | PROVED | B13-05 Theorem F. **The two `a ≥ 1` hypotheses were missing here until now** — the proof takes highest-weight vectors `h_κ`, `h_ν` and multiplies them, which presupposes they exist; when `a(κ,p) = 0` the hypothesis `i(κ,p) = 0` holds *vacuously* and there is no `h_κ` to take. Caught by Astra. **All 18 derived closures stand**: all 92 witness factors were checked here on the house census and every one has `a ≥ 1`; **16 of the 18** use `κ = (3)` at `δ = 1` where `a = 1`; the other two — `(10,7,5,2,1,1,1)₉` and `(10,8,3,3,1,1,1)₉` — use `(4,2)` at `δ = 2`. I wrote "every" and it is 16 of 18; caught by Astra. No closure reopens: all 92 factor occurrences were checked and every one has `a ≥ 1` |
| `orbit_stabiliser_silent` | the bound `mult ≤ dim S_μ(C⁹)^{H′}` is silent at **all 4,517** weights, `δ ≤ 9`, every length, by margins 4–691, and **`H′` is already the whole stabiliser**, so there is no larger group to try | MEASURED + ADOPTED | B13-05 Theorem E and §6.3. **The stated argument was wrong and the conclusion is right, for a different reason.** B13-05 justified "not rescued by the full stabiliser" by *the remaining factors are finite, so `b` can fall by at most a bounded factor* — false: invariants under a larger group are an intersection of eigenspaces, and a `Z₂` acting by `−1` on a line takes `d = 1` to `0`. Astra caught that. But `docs/washout_lemma.md` Prop. 5 records the permanent's stabiliser as `(T_eff ⋊ (S₃ × S₃)) ⋊ Z₂`, **adopted from Marcus–May / Botta**, which is exactly the `H′ = T ⋊ F`, `\|F\| = 72`, that `analysis/wk13_b13_05_bound.py` uses — and F's containment is re-verified exactly on per₃'s monomial dictionary at every run. So the extension does not exist. **Conditional on an ADOPTED theorem**: if Marcus–May were wrong the question would reopen. **Do not fund again at any length** |

## B. Transfer between the cubic and quartic sides

| id | statement | status | source |
|---|---|---|---|
| `transfer_exact` | `I(P)_δ / I(R)_δ ≅ W_δ ∩ (Sym^δV ⊗ J_δ)`; the gap `mult_R − mult_P` **is** the dimension of that intersection | PROVED | B13-04 Theorem A; identified with Prop. 8 and with **S4's factorization** `rank T_pad = rank S − dim(S(M_λ) ∩ K)` |
| **`fixed_factor`** | `ρ(h)(c) := h(x₁·c)`; `h ∈ I(R) ⟺ ρ(h) = 0`, `h ∈ I(P) ⟺ ρ(h) ∈ J_δ`, `rank ρ = mult_R`. Monomially, `ρ` deletes every monomial containing a letter with `β₁ = 0`. **So a reducible-ideal HWV is exactly one with no `x₁`-pure monomial — a support test, no pullback to expand.** | PROVED | S4 (batch 12) for the kernel half; extended by B13-04 Lemma B. **Re-derived independently by B13-02, B13-03 and B13-04 for want of this citation** |
| `channels` | `ρ(H_λ) ⊆ B^λ = ⊕_ν B^λ_ν` with `dim B^λ_ν = a⁽³⁾(ν,δ)`; the gap is `dim(ρ(H_λ) ∩ J^λ)` | PROVED | B13-04 Proposition C |
| `transfer_bounds` | `max(0, Σi⁽³⁾ + mult_R − Σa⁽³⁾) ≤ gap ≤ min(mult_R, Σi⁽³⁾)` | PROVED | B13-04 Corollary D. A screen on both sides, not a substitute for the criterion |
| `pieri_not_sufficient` | the converse of Prop. 8(2) is **false**: a Pieri-compatible cubic constituent need not contribute | PROVED | B13-04 Theorem E, `r = 2`, `f = x³`, `δ = 2`. Measured rate: **13 of 646 channel lines, 2.4 % of compatible pairs** |
| `swap_identity` | `F(ℓ·q) = ℓ₁^δ F(u_ℓ⁻¹(x₁·q))` for `F ∈ ρ(H_λ)` — a two-evaluation exact **rejection** test | PROVED | B13-04 Lemma F. Detected 152 of 152 non-descents |
| `swap_not_sufficient` | the swap identity, **and the full two-factor consistency condition**, are necessary but not sufficient. No condition read off the affine slice `ℓ₁ ≠ 0` characterises descent. | PROVED | B13-04 Theorem H; 78-term witness at `r = 3`, `δ = 7`, `λ = (16,6,6)`, two symbolic identities over ℤ |
| `swap_one_sided` | sampling only *under*-constrains a kernel, so a computed `dim T^λ = mult_R` **certifies** `T^λ = ρ(H_λ)`; `>` is only a ceiling | PROVED | B13-04 §12.1. 432 of 433 cells certified this way |
| `length_quantifier` | a predecessor of length `k` enters only through its **length-`k`** value of `i⁽³⁾`, and may be ignored exactly when that is already known zero (`k ≤ 5` always). At `λ₁₃`, `k = 8 > 5`: nothing is inherited. | PROVED | B13-04 §7; demonstrated at `λ = (7,7,1,1)` where the only contributing channel is a *shorter* predecessor |

## C. The LMR cell and its neighbourhood

| id | statement | status | source |
|---|---|---|---|
| `lmr_ranks` | `a = 274`, `mult_det = 273` exactly, `mult_pad ≥ 269`; so `i_det = 1` and **`D = 1 − i_pad(24) ∈ [−4, +1]`** | CERTIFIED / ADOPTED | s74; replayed by B13-07 and B13-11 at both primes |
| `lmr_D_measured` | the sampled value `D = −4` | **MEASURED, never promoted** | a five-dimensional sampled kernel at 282 points bounds `i_pad ≤ 5` and proves **nothing** downward |
| `eps_pad_inference_dead` | the two-prime inference `ker mod p ⊆ uM₂₃ ⟹ ker_ℚ ⊆ uM₂₃` is **false**: `q = 2147483647·2147483629`, matrix `[q,1]` has modular kernel in the old subspace at both primes and rational kernel `(1,−q)` outside it | PROVED | B13-07. `ε_pad ∈ {0,1}` stands; three routes remain, named there |
| `cartan_ladder_invariance` | `i_X((65+4k,17,2⁷), 24+k) = i_X((65,17,2⁷),24)` for every `k ≥ 0`, `X ∈ {D,P,R}` | PROVED | B13-06. **Preserves an unresolved `D`; does not bound it.** Later rungs are not independent opportunities |
| `eleven_row_padded_zero` | `ℓ·per₃` has ten essential variables ⟹ `mult_pad = 0` at every eleven-row weight ⟹ `D ≤ 0` there, with no sampling | PROVED | B13-06. 97 degree-26 components settled |
| `offladder_targets` | two guaranteed **new** determinant equations at `(71,19,2⁷)` and `(69,21,2⁷)`, degree 26, ambient `a = 392` and `531` | PROVED | B13-06; both ambient counts independently confirmed on `wk9_s42_census.a_weyl`. Sufficient padded minors **392 and 531**, falling to 391 and 529 **only if** product-image ranks 2 and 3 are first proved |
| `n3_padded_seven_row` | `ℓ·per₂ = z(ad+bc)` has **exactly** five essential variables ⟹ `mult_pad = 0` at a seven-row weight, `i_pad = a`, padded gap **−5** | PROVED | B13-11. Promoted from assumption. **The unpadded `+1` example at `(19,7,2⁵)` supplies no padded test** |
| `weight13_census_closed` | of 57 weight-13 tails with ≤5 parts, 10 have `a_inf = 0`, 28 of the 47 positive are closed, and the remaining 19 have quartic length ≤ 4 — excluded by `n4_gate_containment`. **No block of that census remains open for `D > 0`** | CERTIFIED + ADOPTED | B13-11 |
| `n4_gate_containment` | generic four-variable cubics have a 3×3 determinantal representation, so `ℓ·c = det diag(ℓ,M)` puts the reducible — hence padded — locus in the determinant closure: no positive padded gap at quartic length ≤ 4 | ADOPTED | `docs/n4_gate.md` §1. **A containment exclusion, not an empty-ideal assertion.** The board never cited this |

## D. Five-variable geometry

| id | statement | status | source |
|---|---|---|---|
| `rank_one_universal` | a **nonzero** projective rank-one support already has the whole determinant image closure as its graph image | PROVED | B13-12 §4; arc with `det = t⁸·det(vI + ΣsᵢCᵢ)`, constant projective target. Exponent matrix and identity independently verified |
| `exceptional_image_warning` | the exceptional image of a parameter-space blowup **must not** be identified with the target's closure-minus-actual-image boundary | PROVED | B13-12 §4. **Retires the wording in `docs/critic_rees_response.md`** |
| `dominance_not_equivalent` | `closure(G(S)) ⊆ Z ∩ {y_bad = 0}`; equality is an **extra** statement. Dominance gives containment; failure of dominance gives nothing | PROVED | B13-12 §2, correcting s78's claimed equivalence. Controls: `(a,b) ↦ (a,ab)` and `(x(x−z)):x^∞` |
| `saturate_then_restrict` | saturate the graph **first**, impose `y_bad = 0` or `z = 0` afterwards — the reverse order loses points | PROVED | B13-12 §2, §3 |
| `triangular_family_dim` | the simultaneously-triangularizable family image is closed with fixed-factor chart dimension exactly **12**, by a finite-map argument | PROVED | B13-12 §5. **Does not bound the graph over a triangular support** — `Y` in `rank_one_universal` is itself strictly triangular |
| `W_in_D5_decidable` | `W ⊆ D5 ⟺ J_W = (0)`; no radical computation needed. Certificate shortcut: one `F(y)` with `F(p(B)) = 0` identically and `F(y_good,0) ≠ 0` suffices without a Gröbner basis | PROVED | B13-12 §3. 133 variables, 69 generators |

## E. Instrument facts that are load-bearing

| id | statement | source |
|---|---|---|
| `rank_floor` | `rank_p ≤ rank_ℚ`. **A sampled deficient rank is a floor on the rank and a ceiling on `i`.** It never establishes `i ≥ 1`. | standing; violated in prose four times before batch 13 and once inside it (`results/s63_n3control.json`, corrected) |
| `evaluation_cannot_certify_i_ge_1` | `i_red ≥ 1` is an **upper** bound on a rank; an evaluation's nullity is a ceiling. **No evaluation-based instrument can certify it.** A brief asking for `i ≥ 1` must designate a carrier or a coupled target | B13-01 |
| `nchi_2_21_guard` | `wk11_s71_hybrid.matmul_mod` asserts inner dimension `< 2²¹` — a **correctness** guard (16-bit limbs in float64, `K·2³² < 2⁵³`), not a memory limit. Bound is on `n_χ = N_S/\|Stab\|`, **not** `N_S`, so it spares high-stabiliser weights | B13-08 §5; fix `matmul_mod_wide` validated three ways |
| `certificate_ceiling` | `full_rank` certificates are gated at `N_S·a ≤ 3×10⁶`; above it this tree can **prove** what it cannot **certify**. `sparse_nullity` is keyed to Wiedemann and the hybrid produces no such record | B13-08 §6 |
| `cost_model` | `build_secs ≈ 3.06×10⁻⁶·N_S·δ + 1.07×10⁻⁶·\|Stab\|·N_S`. The `\|Stab\|` term comes from `_canon_acc`'s **two passes over the group** — a deliberate memory-for-time trade, right at `\|Stab\| ≤ 120`, fatal at 5040 | B13-09 §4. **The old `N_S·δ`-only model is up to 21.7× low. Do not quote it** |
| `build_no_longer_binding` | the raising-row build is not the wall: the pilot at `N_S·δ = 1.47×10⁸` builds at **1.96 GB**; the rows are 664 MB and the old "4 GB" was transients. Ceiling now `N_S·δ ≈ 2.8–5.4×10⁸`; **the consumer binds first** | B13-10 |
| `negative_control_forced` | diagonal pencils make `per₃` a product of three linear forms, whose coordinate ring carries no constituent of more than three rows — so any length-6 weight **must** read rank 0. Forced by representation theory, works at weights with no banked history | B13-08 Control C. **Required on every evaluation-rank sweep** |
| `check_must_be_able_to_fail` | a check that cannot fail is not a check. Six instances in batch 13 alone: a lookup that skipped missing targets; a function below a `__main__` guard; a support condition with no teeth; a comparator matching an all-`None` record; a join comparing padded to unpadded keys; and two **direction-of-inference** errors | mine, B13-03, B13-04, B13-08, B13-10, B13-11, B13-12 |
