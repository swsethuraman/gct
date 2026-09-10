# B13-04 review — sharpen the cubic-to-quartic transfer

board_numbering: batch13
session_id: B13-04
models recorded by the session: **`Claude Fable 5.1`** through commit `2b89394`,
then **`Claude Opus 5`** from `b4c6a93` (a model-availability limit mid-session)
bundle: `b13_04_fable.bundle` (one part)
base: `00495110c62acfbbbc951e82cc218ed091563b3f`
head: `16f8f55e546066ffa4a0303890f38935a6148aab` (`refs/heads/b13_04`)
status claimed: success — the exact criterion, the converse refuted, the audit
reconciled, the quantifier stated, and a second counterexample in an addendum
integrator verdict: **accept the mathematics; the delivery needs one mechanical
fix before merge — all eight commits carry a session-link trailer**

Stock-take. Arithmetic below is closed-form or pencil-and-paper only.

---

## 1. Zero-cost checks

| check | result |
|---|---|
| md5 | `5d0e65b631e02ef2f112f71bb3fcb983` — matches, for whole and `part00` |
| `git bundle verify` | "is okay"; one ref `refs/heads/b13_04` |
| declared base | `0049511` — equals `origin/main` and my tip |
| applies | clean; 68 files, 484,690 insertions, **0 deletions** |
| single-writer files | **none touched** |
| 5 MB rule | no file in the delivery exceeds it |
| `claude.ai` URL in any delivered **file** | **none** |
| `Claude-Session:` trailer in commit messages | **present in all eight — see §7** |
| pre-registration | `35148d8` before any computation; addendum `b4c6a93` before the measurements it governs |

**Theorem E checked by hand, no machine.** `r = 2`, `f = x₁³`, `δ = 2`:

- `h = 8q₄₀q₂₂ − 3q₃₁²`. By `E_ij q_β = (β_i+1)q_{β+e_i−e_j}`:
  `E₁₂(q₄₀q₂₂) = 3q₄₀q₃₁`, `E₁₂(q₃₁²) = 8q₃₁q₄₀`, so `E₁₂h = 24 − 24 = 0`. ✓
- Lemma B(4) deletes letters with `β₁ = 0` and relabels `β ↦ β−e₁`:
  `ρ(h) = 8c₃₀c₁₂ − 3c₂₁²`. ✓
- `g = 3c₃₀c₁₂ − c₂₁²`: `E₁₂g = 6c₃₀c₂₁ − 6c₂₁c₃₀ = 0` ✓, and on `m³`
  (`c₃₀,c₂₁,c₁₂ = a³,3a²b,3ab²`) `g = 9a⁴b² − 9a⁴b² = 0` ✓.
- `8/3 ≠ 3/1`, so `ρ(h) ∉ C·g`: **the Pieri-compatible constituent contributes
  nothing.** Directly, `h(x₂·x₁³) = −3` (only `q₃₁ = 1`). ✓
- Contrast at `(4,4)`: `ρ(12q₄₀q₀₄ − 3q₃₁q₁₃ + q₂₂²) = c₁₂² − 3c₂₁c₀₃`, and
  `E₂₁²g = 6c₂₁c₀₃ − 2c₁₂² = −2(c₁₂² − 3c₂₁c₀₃)`. So `ρ(h)` **is** the branching
  vector, to a factor of `−½`, exactly as claimed. ✓

**The counterexample to the converse of Prop. 8(2) is correct and needs no
computer to check.** That is the ideal form for a load-bearing negative.

Internal consistency, all reproduced: the §12.4 census columns sum to 199
cells / 646 lines / 13 contributing / 85 cells with gap / 117 total gap / 22
above Corollary D's floor; the §12.2 sweep rows sum to 433 and 432; the fifteen
`N_S` values total `3.0835×10⁹` against the stated `3.08×10⁹`; the partition
counts of 39 into 6–9 parts are `[1729, 2400, 2857, 3060]`, total 10,046,
exactly as stated; `888 − 887 = 1`, the single excess dimension of the
exception.

---

## 2. Two cross-confirmations that no single session could give

**With B13-01, on the fifteen predecessors.** B13-01 computed
`h_pad(21,17,2⁷;13) = Σ_μ a₃(μ,13)` by Weyl alternation over `S₉` with an exact
cubic-multiset counter in C. B13-04 computed `Σ_ν a⁽³⁾(ν,13)` by Kostant
alternation with `W`-sorted weight caching. The two multisets of fifteen values
are **identical** —
`{1,2,2,3,3,4,4,5,5,5,6,7,8,9,9}`, sum **73** — and B13-04's `N_S` column
carries B13-01's two `(★)`-bad sub-carriers to the digit: `809,527,307` at
`(17,8,2⁷)` and `117,718,904` at `(21,4,2⁷)`. Different formulas, different data
structures, different sessions, different models.

And the two readings of that 73 are complementary, not redundant:

- **B13-01:** `73 > 39 = a`, so the normalisation bound `mult_red ≤ h_pad` is
  vacuous — no carrier-free route to `i_red ≥ 1` at rung 13.
- **B13-04:** the 36-dimensional reducible image sits inside a 73-dimensional
  channel space `B^{λ₁₃}`, so **no dimension count forces a transfer**; a forced
  gap would need at least 38 of the 73 channel dimensions inside the cubic
  ideal.

Same number, same cell, two independent derivations, two different things
learned. B13-04 also notes the shape repeats: 39 against 73 at `δ = 13` is
274 against 521 at `δ = 24`.

**With B13-03, on the `(8,8,8)₆` control.** B13-04's
`results/b13_04/control_888_d6.json` records `N_S = 561`, `a = 2`,
`rank ρ over Q = 1`, `i_R` certified `= 1`, kernel `κ = (1,0)`, **377 terms**,
`pure_monomials = 0`, `support_test = true`, `symbolic_identity_zero = true`,
0.8 s. B13-03 reported the identical cell independently: source dim 2,
restriction rank 1, `i_red = 1`, `F0` accepted with **377** nonzero integer
terms, kernel `(1,0)`, target weight-monomial count **561**.

Two sessions, two models, unrelated code, the same 377-term vector. And
B13-04 adds what B13-03 did not have: by Lemma B(4) a reducible-ideal
highest-weight vector is exactly one **no monomial of which is `x₁`-pure**, so
membership is certified by a support inspection with no pullback to expand.
B13-04 offers this to B13-03 explicitly. **It is the cheaper certificate shape,
and it should be adopted.**

---

## 3. The mathematics

**Theorem A (PROVED).** `I(P)_δ / I(R)_δ ≅ W_δ ∩ (Sym^δV ⊗ J_δ)`, so
`mult_R − mult_P` is the dimension of that intersection's `λ`-highest-weight
space. Identified with Prop. 8 and with S4's factorization
`rank T_pad = rank S − dim(S(M_λ) ∩ K)`, and claimed as new only in that
identification.

**Lemma B (PROVED; kernel half is S4's).** `ρ(h)(c) := h(x₁·c)`;
`h ∈ I(R) ⟺ ρ(h) = 0`, `h ∈ I(P) ⟺ ρ(h) ∈ J_δ`, `rank ρ = mult_R`, and the
monomial form: `ρ` deletes every monomial containing a letter with `β₁ = 0` and
relabels the rest injectively. Hence the support characterisation, and
`mult_R = 0` whenever `λ₁ < δ`.

**Proposition C, Corollary D (PROVED).** The channel decomposition
`ρ(H_λ) ⊆ B^λ = ⊕_ν B^λ_ν` with `dim B^λ_ν = a⁽³⁾(ν,δ)`, and the two-sided bound
`max(0, Σ i⁽³⁾ + mult_R − Σ a⁽³⁾) ≤ gap ≤ min(mult_R, Σ i⁽³⁾)`. The upper bound
is Prop. 8(2) made quantitative.

**Theorem E (PROVED).** The converse of Prop. 8(2) is false for a general
`GL_r`-stable cone — §1 above.

**Theorem H (PROVED, addendum).** The swap identity, and even the full
two-factor consistency condition, are necessary but **not sufficient** for
descent: an explicit 78-term integer polynomial at `r = 3`, `δ = 7`,
`λ = (16,6,6)` satisfies both **as polynomial identities over `Z`** (233/233 and
3152/3152 monomials cancelling) yet is provably not `ρ(h)` for any quartic
highest-weight vector. So no condition read off the affine slice `ℓ₁ ≠ 0`
characterises descent — the obstruction lives at the boundary `ℓ₁ = 0`.

Two things make this addendum better than it had to be. First, the
**one-sidedness lemma**: sampling can only under-constrain a kernel, so a
computed `dim T^λ = mult_R` *certifies* equality with no saturation caveat,
while `>` is only a ceiling. That converts a 433-cell sweep from measurement
into certification — 432 cells certified, one exception, and the exception is
then proved symbolically rather than sampled. Second, the swap conditions
involve only `(r, δ, λ)` and **not the cubic `f`**, so descent is a statement
about the reducible locus alone and sweeps model-free.

**The `(POLE)` reading is labelled MEASURED and should stay that way.** At
fifteen specialisations the witness shows no boundary pole, which *suggests* it
lies in the seminormalisation of `R` and not in `R` — i.e. that `R₃ ⊆ Sym⁴C³`
is not seminormal in that graded piece. Specialisation is one-sided the wrong
way, and the session says so. Worth noting for the board: that object is
exactly what **B13-02's seminormal recursion** works with, so B13-04's single
most valuable open item and B13-02's method meet on the same ground.

**The quantitative headline.** Across 199 exactly computed cells on five
cubics, two lengths and five degrees: **13 of 646 channel lines, over 541
Pieri-compatible constituent/cell pairs — 2.4 % — contribute on their own.**
Pieri compatibility is very far from sufficient. Twenty-two gaps exceed
Corollary D's dimension floor, all at `δ ≥ 5`, so the exact criterion does work
no count can do. The swap identity detected all 152 non-descents in the first
census.

**Scope limit, stated by the session and worth repeating.** No `per₃` example
of the transfer mechanism exists to compute on — every measured
`I(D_r^{per₃})_δ` in the tree is zero. The models use `x³`, `x³+y³` and `xyz`.
The theorems are general; **the 2.4 % is a fact about those cubics, not about
`per₃`.** The cheapest place a first `per₃` instance could appear is the
degree-10 length-6 remainder (B13-08).

---

## 4. The length quantifier, and why it is not a formality

§7 states it once, quotably, and §12.5 demonstrates it: at `r = 4`, `δ = 4`,
`λ = (7,7,1,1)` the length-4 predecessors carry `Σ a⁽³⁾ = 0` and the **only**
channel is the length-3 predecessor `(7,4,1,0)`, which has `i⁽³⁾ = 1` and
contributes. The additional padded equation at a full-length weight comes
entirely from a shorter predecessor. Twenty-three (cell, shorter-predecessor)
pairs at full-length `λ` in that census, forty-seven over all cells; shorter
predecessors behave exactly like full-length ones — live, and mostly
non-descending.

The rule: a predecessor of length `k` may be ignored exactly when its
length-`k` value of `i⁽³⁾` is already known zero — for `k ≤ 5` by Theorem 2 of
`washout_lemma.md`, and for `(k,δ)` pairs closed by an earlier full-rank scan.
At `λ₁₃`, `k = 8 > 5`: **nothing is inherited**, and the five length-8
predecessors are as live as the ten length-9 ones.

---

## 5. Self-caught defects — the good kind

**An independent adversarial audit agent** re-derived Theorem E by hand and by
its own code, re-verified Theorem H on its own highest-weight kernel and its own
polynomial arithmetic, and checked the convention traps. It found six defects.
All six were fixed; no mathematical claim changed. **This is the first session
in the programme to run an adversarial audit on itself, and it should become
the convention.**

Two of the six are worth naming:

1. **`symbolic_fibre_zero` sat below the `__main__` guard and was never called**,
   so Theorem H item 2 was asserted with no artefact behind it. The function was
   moved, called, and the run repeated. **This is precisely the error class I
   made with the `E·v = 0` check** — a check that can silently not run, and
   therefore passes. Third occurrence in this programme. It belongs in the
   preamble as a named trap.
2. **One stored witness of 118 is vacuous**: the kernel of `[RH | J]ᵀ` at a cell
   with `i_R ≥ 1` also contains the linear relations among the `ρ(h)`, which
   give `ρ(h) = 0` and pass the ideal test trivially. Stated rather than
   repaired, with the two fields that identify it
   (`rho_h_terms = 0`, `nonzero_on_reducible = false`), and no reported number
   depends on it — `criterion_gap` is computed independently.

Stating a defect you chose not to repair, with the fields that expose it, is
better practice than a silent fix.

---

## 6. Defects against my board — all six accepted

1. **The B13-04 entry does not cite S4**, whose factorization identity *is* the
   intersection the entry asks for. This one has a measurable cost: B13-02 and
   B13-03 **both** re-derived the fixed-factor lemma independently, and B13-04
   re-derived the identity. Three sessions spent effort on a PROVED batch-12
   result because the board did not point at it. Fix the entry to cite
   `results/astra/S4/S4_report.md` §"The factorization" and
   `docs/s4_batch12_review.md` §1.
2. **"A counterexample to a proposed converse"** — no converse is proposed
   anywhere in the tree. B13-04 states the one it refutes; the brief should
   state it.
3. **"Existing small exact controls"** are named as inputs, but none with a
   nonzero cubic ideal exists for `per₃`. The brief should say a model cubic is
   expected.
4. **`docs/stocktake_batch12.md:173` still carries the truncated `N_S` range**
   (`1.6·10⁷` to `3.7·10⁸`). Confirmed against the tree. I corrected the board
   and not the stocktake; the true maximum is `8.10·10⁸` at `(17,8,2⁷)`. **Mine,
   still live, third document to be caught by it.**
5. **`wk8_s30_pleth.amb` is unusable at `δ = 13, r = 9` on a 3 GB budget**;
   the Kostant tail alternation is, and is faster with `W`-sorted caching. Worth
   a line in the preamble's tool list.
6. §7's length-quantifier paragraph should replace the four scattered sentences
   in the board's B13-04 entry.

---

## 7. The one thing that must be fixed before merge

**All eight commits carry `Claude-Session: https://claude.ai/code/session_011d…`.**

This violates the standing rule: commit messages carry
`Co-Authored-By: <model>` only, no session-link trailer, in commits or in any
script that commits. It is the first hard house-rule breach in batch 13.
B13-01, on the same model family, explicitly declined the same trailer; B13-04
did not, and the report does not mention it. Both the Fable commits and the
Opus commits carry it, so it is not the model swap.

**No delivered file contains a `claude.ai` URL** — checked across all 68 changed
files. The breach is confined to commit messages, which is the repairable case:
`tools/rewrite/message_callback.py` already strips lines beginning
`Claude-Session:`, and `docs/history_rewrite.md` records it doing so across 260
commits. Run it over the eight before merging; nothing else about the delivery
changes.

Minor and separate: the report's closing line names one model
("Author of record for this session: B13-04 (Claude Fable 5.1)") where the
header correctly names two. The header governs; the footer should match it.

Otherwise the model handling is the best in the batch — the swap is recorded in
the pre-registration addendum, committed *before* the measurements it governs,
in the report header, and per-commit, with no result attributed to the model
that did not produce it.

---

## 8. Actions

1. **Strip the `Claude-Session:` trailers from the eight commits** with
   `tools/rewrite/message_callback.py` before merging. Do not merge as-is.
2. **Fix `docs/stocktake_batch12.md:173`** — the `3.7·10⁸` range. Mine, and now
   caught by a third session.
3. **Cite S4 in the board's B13-04 entry.** Three sessions have re-derived a
   PROVED batch-12 result for want of a pointer.
4. **Adopt the support test** (`pure_monomials = 0`) as the reducible-membership
   certificate shape, and tell B13-03 — it is cheaper than expanding a pullback.
5. **Add "a check that cannot fail is not a check" to the preamble** as a named
   trap, with the `__main__`-guard instance and the `E·v = 0` instance as the
   two examples.
6. **Adopt the adversarial self-audit** as a delivery convention for batch 14.
7. Add the Kostant tail alternation to the preamble's tool list, and replace the
   board's scattered length-quantifier sentences with §7's paragraph.
8. On the deferred verification pass: re-derive Theorem H's two symbolic
   identities independently (233 and 3152 monomials — cheap), and re-run the
   `(8,8,8)₆` support test against B13-03's `F0` to confirm the two 377-term
   vectors are the same vector and not merely the same count.
