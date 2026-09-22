# PAPER2_BLOCKERS — `paper/det4-onset.tex`, assessed against the record

Slot B24-06, 2026-09-19/20. **Assessment only. Nothing in `paper/det4-onset.tex` was changed.**
Repair is Batch 25, from this list.

```
worktree   C:\Users\swami\Projects\gct-gpt\work\batch15_workers\B24-06
branch     b24-06-paper2
HEAD       82633a60893236fab4fbc317df416e1b8a349005
HEAD^{tree} e82fd3291d1a2adc8a577647314c251366ff5142
git status --porcelain   (empty, at start and at end)
paper      sha256 7c2bc7365c3aacc75e5d79906a4aaa3364ff015e5bbc91e2f585b1ca45678b7b
           last touched a1bf7c00, 2026-09-09, 434 commits behind HEAD
```

Claims table: `PAPER2_CLAIMS.md`. Gaps and record defects: `PAPER2_GAPS.md`. Readiness
paragraph: `PAPER2_READINESS.md`. Every label below is the record's own; nothing is upgraded,
no condition is dropped, no scope is widened (G26).

---

## 0. First: the stocktake's six candidates, verified

The 2026-09-17 stocktake is the only description of Paper 2 on the record, and it is
integrator-written and unverified. **The document itself could not be found** — no file under
`work/` or in the tree contains the phrase "second author" (GAPS G-P2-16). The six items were
checked against the source instead.

| stocktake said | verdict |
|---|---|
| a garbled formula in **Prop. 2.1** | **REAL**, and the number is right. `\dim\Ddet_r=5r^{2}\cdot0+\ \dim\GL-\emph{orbit count}` (L237) is not a formula. **A second garbled clause the stocktake missed**: Lemma 3.3's proof ends "and is `2n-\dim` in the relevant range" (L303). → **B9** |
| an empty `\cite` | **REAL but misdescribed.** There is no `\cite{}`. There is `\cite[\S]{Companion2}` (L440), whose optional argument is a section sign with no number; it typesets as "[§]". All 16 bibliography keys are cited and every cited key is present. → **B14** |
| the abstract refers to a "second author" | **REAL, wrong location.** The abstract does not. §1 does, L183: "improves the second author's earlier bound `80` at `n = 3` to `65`". → **B15** |
| **Thm 6.2**'s "unconditional" against **Rem. 6.3**'s unproved completeness | **REAL, and both numbers are right** (numbering re-derived: `prop:dims` = 2.1, `thm:noncontain` = 6.2, `rem:noncontain-status` = 6.3). The tension is genuine, and the record has moved under both halves. → **B8**, **B10** |
| §9's LMR range needs `[−4, −2]`, conditional | **REAL.** The paper says `[−4, +1]`; `docs/PROVED.md` `lmr_D_upper` gives `D_LMR ∈ [−4, −2]`, CERTIFIED conditional on the ADOPTED `dim N₁₃ = 73`. → **B4** |
| absorb the `n = 3` positive control (`D = +1`) and the length-theorem cross-reference | **ALREADY DONE, and half-done.** The `D = +1` control at `(19,7,2^5)_{12}` is in the paper, as the §9 subsection "The method exhibited on a separation of its own size", with the record's own caveat that it is unpadded and calibration only. The **length theorem** is present only as content (`ℓ <= δ` inside Prop. 3.4; `λ_1 >= δ` as Cor. 5.3) and is never cited as a theorem — and the record's `length_bound` has since **withdrawn its `, 9` clamp**. → not a blocker; **B13** and GAPS |

**Four of six real, one already fixed, one misdescribed. None was invented** — unlike the Paper 1
brief, where three of the items were wrong (B23-10 §6.2 confirms B23-05's three corrections: the
remark numbers 4.7 and 5.10, the `README_public` file that never existed, and "rigidity"/"TOTAL_G"
absent from all twenty paper versions).

---

## 1. Blockers, ordered

Ordered by what a reader would be misled by first. **[AUTHOR]** marks an item that is a decision,
not a correction.

### B1 — Corollary 5.3 states the Kadish–Landsberg bound backwards

**What.** §5, `cor:kl` (L409–417): "If `λ_1 < δ` then every monomial of every weight-`λ`
highest-weight vector omits some variable automatically, so **`mult_λ C[R_r] = a(λ,δ)`** and
`I(R_r)` has no length-`ℓ(λ)` part at `λ`."

**Why it is wrong.** Vanishing on `R_r` is membership *in* `I(R_r)`. If every weight-`λ`
highest-weight vector vanishes, then all `a(λ,δ)` of them lie in the ideal and
`mult_λ C[R_r]_δ = 0` — which is what the paper's **own Corollary 5.2** computes
(`mult = a − dim{v satisfying (★)}`). The record says it in one line: "`mult_λ C[Y]_δ = 0` for
every `G`-stable closed `Y ⊆ X^{(k)}`" (`docs/reducible_ideal.md` §0 Corollary B @ `82633a60`);
independently `docs/PROVED.md` `quartic_length_and_eligibility`, "`mult_pad > 0` implies
`λ_1 >= δ`" (PROVED, B14-11).

**What clearing it takes.** Two substitutions in one sentence: `= a(λ,δ)` → `= 0`, and "`I(R_r)`
has no length-`ℓ(λ)` part at `λ`" → "`I(R_r)_λ` is the whole isotypic component". The
corollary's final sentence — no obstruction at `λ_1 < δ` — is correct and unaffected, and the
attribution paragraph that follows is correct. Nothing else in the paper depends on the wrong
form.

### B2 — Theorem 9.1 is false as stated; it holds only below the `r = 4` onset

**What.** §9, `thm:slab`: "For every weight with `ℓ(λ) <= 4` and **every degree**,
`mult_λ C[D^det_4] = a(λ,δ)`."

**Why it is wrong.** `dim D^det_4 = 34` in `dim W_4 = 35` — the paper's own Prop. 2.1 table — so
`I(D^det_4)` is principal and **nonzero**, and `mult_det < a` at and above its generator's
degree. The paper's proof already knows this: it says "whose ideal begins in degree `≫ δ` **for
the degrees in question**", which is not the quantifier in the statement.

**The record splits it correctly.** `docs/blindness_slab.md` §0 Theorem A @ `82633a60`:
`Δ <= 0` for `ℓ(λ) <= 4` at every `δ`; `det_units = 0` for `ℓ <= 3` at every `δ`; and for
`ℓ = 4` **only at `δ <= e − 1`**, where `e = onset I(D_4^{det_4})`, with `e >= 10` **certified**
(s33) and `e = 320112` **adopted** (LLV). The value is also carried by `docs/e4_hunt.md`,
`docs/det_onset.md` L62 and `docs/equation_census.md` row 13.

**What clearing it takes.** Restate Theorem 9.1 as the record's three-clause Theorem A, and cite
`e`. The headline conclusion (`Δ <= 0` on the whole length-`<= 4` slab, at every degree) is
**not lost** — it follows from the paper's own Prop. 6.1 / `docs/PROVED.md`
`n4_gate_containment`, which is a containment and therefore degree-free. Note also that the two
named strict cells are on the record and unnamed in the paper: `D((8,8,8), 6) = −1` and
`D((12,8,8), 7) = −1`.

### B3 — "length `>= 6`" is the wrong gate, and contradicts the record

**What.** §9, "The honest frame" paragraph: "a map of where the certificate can live — **length
`>= 6`**, degree `>= 8`, first row `>= degree` — and a proof that large parts of that map are
empty."

**Why it is wrong.** At `r = 5` the paper's own Theorem 3.1 gives `P_5 = R_5` exactly, so
`Δ = Δ_R` there; a positive `Δ_R` at `ℓ = 5` **is** a multiplicity obstruction for the padded
permanent. The washout's true content is about *interpretation* — such a certificate would
certify reducibility against the determinant rather than the permanent — not about existence.
The record's gate is `ℓ >= 5`:

- `docs/n4_gate.md` §2 @ `82633a60`: "The current ambient gate is `a > 0` … after the containment
  exclusion of section 1 the length gate is `ell >= 5`."
- `docs/PROVED.md` `quartic_length_and_eligibility`: "the historical `a >= 2` and `ℓ >= 4` gates
  are replaced by `a > 0` and `ℓ >= 5`".
- And that is where the open region is: `b14_11_quartic_census` counts 4,198 labels in the
  `n = 4`, `δ <= 8`, `5 <= ℓ <= δ`, `λ_1 >= δ` region, 2,734 with `a > 0`, of which
  **2,571 are still open** (`docs/batch14_close.md` L67, L153).

**What clearing it takes.** "length `>= 5`" in that sentence, and a separate sentence for the
washout reading. The other two coordinates of the map are supported: "degree `>= 8`" by
`I(D_5^{det_4})` being empty through degree seven (measured, `docs/det_onset.md`), and "first row
`>= degree`" by `quartic_length_and_eligibility` (proved). Note the same paragraph's "a proof
that large parts of that map are empty" should say which parts are proved and which measured.

### B4 — §9's LMR interval is stale

**What.** §9, "What the length-nine cell reduces to": "`Δ ∈ [−4, +1]`".

**The record.** `docs/PROVED.md` `lmr_D_upper` @ `82633a60`: "`i_pad(24) >= 3`, hence `D <= −2`;
with the banked ceiling, **`D_LMR ∈ [−4, −2]`** and `D = +1, 0, −1` are excluded at this cell" —
**CERTIFIED, conditional on the ADOPTED `dim N₁₃ = 73`**. It is a deduction neither producing
report made: B14-01 + B14-02 combined, each link checked by the integrator
(`docs/b14_01_02_joint_review.md`), and it is what `docs/batch15/ACCEPTED_STATE.md` carries.

**What clearing it takes.** Replace the interval; carry the condition (`dim N₁₃ = 73`, ADOPTED,
two lineages) rather than dropping it; and say that the positive case is closed at this cell,
which is the substantive change — the paper currently leaves `Δ = +1` on the table at the one
cell where the programme has excluded it.

**[AUTHOR]** An uncommitted batch-15 result narrows further to `D_LMR ∈ [−4, −3]`
(`B15-01/docs/b15_01_report.md`, worktree B15-01, uncommitted). Whether an unpublished,
uncommitted result may be cited in a paper is the author's call; the committed record stops at
`[−4, −2]`.

### B5 — Landsberg–Manivel–Ressayre is load-bearing four times over and is unread

**What.** §1 and §9 rest on LMR at four points: the set-theoretic non-containment
`x_0 per_3 ∉ closure(GL_16 · det_4)`; "the determinant side is **bounded below by** \[LMR\] at
this cell, which is what makes the measurement a control"; "the one-dimensional kernel is
therefore \[LMR\]'s **own equation**"; "the rigorous lower bound on the determinant side
**remains** \[LMR\]'s".

**The record's read-status.** `papers/det4-blindness/BIB.md` @ `ce43cdb7` files LMR under
**UNREAD-SPECIALIST** (B22-02 §5). B23-06 later read it at source — but only
**Theorem 1.0.1**, `dcbar(perm_m) >= m²/2` (PRIMARY, arXiv 1004.4802v1, PDF sha256
`cfc28275a8c6b27f…`; `B15-02/docs/b23_06_report.md` §1, uncommitted, sha256 `a56d2394…`).
Theorem 1.0.1 supports the **first** of the four uses and nothing else. The module `Ω(k,d)`, the
multiplicity lower bound at `λ = (65,17,2^7)` and the identification of the kernel direction as
LMR's equation are record-internal (`docs/lmr_cell.md` §1 @ `82633a60`) and **verified at source
nowhere on the record**. Under G14′ every claim resting on an unread load-bearing citation is
CONDITIONAL.

**What clearing it takes.** Read LMR (Comment. Math. Helv. 88 (2013), 469–484) and confirm,
re-attribute, or label the three unsupported uses CONDITIONAL. This is the **same source** that
B23-05 made blocker 5 for Paper 1 ("must also read Landsberg–Manivel–Ressayre (2013) … and
decide whether to cite them"); one read clears it for both papers.

### B6 — Prior art is not labelled at the point of use, and one source is the Paper-1 failure mode

Gate G14/G14′ requires every external theorem a proof step uses to carry PRIMARY / SECONDARY /
UNREAD-CLASSICAL / UNREAD-SPECIALIST at the point of use. Paper 2 carries none. Four specific
items:

**(a) Beauville — the one to worry about. [AUTHOR decides only after reading]**
`\cite{Beau}` (Beauville, *Determinantal hypersurfaces*, Michigan Math. J. 48 (2000)) appears
**once**, in Prop. 6.1's sketch, for a negative fact that the record measures anyway (5-ary
cubics are not all `3×3`-determinantal; Jacobian rank 29 of 35, `docs/l5_containment.md` §3).
It has **no read-status anywhere on the record** — it is absent from Paper 3's BIB entirely.
That paper is the standard reference for exactly three things Paper 2 claims in its own voice:
the dimension of the variety of determinantal hypersurfaces (Prop. 2.1), the singular locus of
the generic determinantal member (Theorem 7.1 Step 2, the `ν(n)` nodes), and the quinary cubic
case (Theorem 7.3). **This is the Paper 1 failure mode**: B23-10 §4.3 found an attribution
defect in Paper 1 that only a full read of the source turned up, and B23-05 made it blocker 1
(Prop. 4.1 is the pigeonhole case of Bürgisser–Ikenmeyer Cor. 7.2). Until Beauville is read in
full, Prop. 2.1, Thm 7.1 Step 2 and Thm 7.3 **cannot be claimed as the paper's own**.

**(b) LLV is PRIMARY on the record and uncited in the paper.** arXiv:2303.09028v3, PDF sha256
`67b1701f761d4336…`, read in the primary text by B20-10 §4.3: "Theorem 2. The family of
determinantal quartic surfaces consists of 5 prime divisors `F1, …, F5`" with
`deg(F1) = 320112` (`D44 = F1`), and **Corollary 3.1** on the dimension of linear determinantal
surfaces. That is the number Theorem 9.1 needs (B2) and a published statement of the `r = 4`
dimension the paper proves for itself. Paper 2 cites neither. *(Record defect alongside it:
`docs/equation_census.md` L372 calls the family "an irreducible divisor"; LLV says five prime
divisors — see `PAPER2_GAPS.md` G-P2-06.)*

**(c) Kleiman and Gulliksen–Negård are SECONDARY, not read.** `papers/det4-blindness/BIB.md` @
`ce43cdb7`, route B20-10 R15: both "ADOPTED exactly as in `onset_conjecture.md` §2 (not
re-fetched)". The record's own wording for the cap is "**proved modulo** Kleiman, Dimca and
Gulliksen–Negård, all adopted and named" (`docs/onset_conjecture.md` §0). Paper 2's Theorem 7.1
is stated flatly; the modulus appears only in a general paragraph in §1, and the abstract says
"we prove". Paper 3 labels the identical theorem **ADOPTED modulo** those three (C11). Dimca is
the one clean citation: **PRIMARY**, hashed, theorem number (Thm 3.1) confirmed.

**(d) Theorem 5.1's novelty claim does not name what was searched.** The paper says "the exact
criterion of Theorem 5.1 we have not found stated". The record's one pass names five sources —
Kadish–Landsberg 2014 (Thm 1.3, Prop. 1.12, read), Chipalkatti, Abdesselam–Chipalkatti,
CGGHMNS 2019, Landsberg Ch. 8–9 — and phrases the verdict as "**as far as one pass shows**, not
on record … we claim them as not-found-in-the-literature, **not as new**"
(`docs/reducible_ideal.md` §5 @ `82633a60`). The paper should carry the list and the record's
weaker phrasing.

### B7 — `\cite{MM}` is the wrong reference for the permanent's stabiliser

**What.** Lemma 3.3's proof: "The determinant and permanent stabilisers are explicit
(`2(n²−1)`-dimensional and `4`-dimensional respectively \cite{BI,MM})", with `MM` = Marcus–Minc,
*On the relation between the determinant and the permanent*, Illinois J. Math. 5 (1961).

**Why.** The linear-preserver theorem for `per_m`, `m >= 3`, is **Marcus–May (1962)** and
**Botta**, and that is what the record cites, four times: `docs/washout_threshold.md` L103 and
L289 ("Marcus–May (1962), Botta; **adopted-from-literature**"), `docs/batch14_board.md` L56,
`docs/washout_lemma.md` L176. The record also notes that **only the torus part is used and is
proved in-tree** — so the citation is both wrong and heavier than it needs to be.

### B8 — Theorem 6.2's statement contradicts its own next sentence, and is mistyped

Three defects in four lines of §6:

1. "the singular **five**-dimensional subspaces of `M_4`" — the object is the **four**-dimensional
   `span(A_2, …, A_5)` (`docs/l5_containment.md` §2; `docs/singular_spaces.md` §1 Lemma 1:
   "`s_1 | F` iff `S_0 := span(A_2,...,A_5)` consists of singular matrices"). The paper's **very
   next sentence** says "a classification of the 4-dimensional singular matrix spaces".
2. "are not all compression spaces" is offered as the *reason* for the conclusion. It is the
   **obstacle**: `docs/singular_spaces.md` §0 records that the compression-only assumption is
   false (the padded `3×3` skew space is the counterexample), that s32 classified the two
   exceptional strata, and that they measure **27** and **25**, both below the compression
   maximum **31**. That is what makes the theorem unconditional.
3. "the corresponding highest-weight vectors separate the two varieties as sets" is a
   non-sequitur — the separation is the dimension count `31 < 35`; no highest-weight vector
   enters.

**Typing, same section.** Prop. 6.1 writes `R_r ⊆ D^det_4` and Thm 6.2 writes
`R_5 ⊄ D^det_4`. In the paper's own notation `D^det_r ⊂ Sym^4 C^r`, so both sides of Thm 6.2
live in different ambient spaces; `D^det_5` and `D^det_r` are meant.

### B9 — Two garbled formulas

- **Prop. 2.1**, L237: `\dim\Ddet_r=5r^{2}\cdot0+\ \dim\GL-\emph{orbit count}`. The intended
  content is Lemma 3.3's own formula, `min(dim W_r, n²r − dim Stab(det_n))`, equivalently
  `dim D_5^{det_n} = 3n² + 2` (`docs/onset_conjecture.md` §1 @ `82633a60`). The numbers that
  follow in the same sentence are all correct.
- **Lemma 3.3**, L303: the sketch ends "… only when the pencil is special, and is `2n-\dim` in
  the relevant range." Incomplete clause.

### B10 — Remark 6.3 is stale in the half that matters, and still fights Theorem 6.2 [AUTHOR]

**Stale.** The remark's closing move is "what is still not proved is that the enumeration is
complete". On the **interior** that is now a theorem. B23-03 **Theorem 2.1 (PROVED)**:
`closure(D45° ∩ P5) = T1 ∪ T2`, with exact dimensions `T1` **33 aff / 32 proj**, `T2`
**35 aff / 34 proj**, `Sigma_Pi` **31 aff / 30 proj**, `T3` **29 aff / 28 proj**
(`B23-03/docs/b23_03_report.md` §2.4 @ `3bcad666`, sha256 `0101f224…`). At a fixed `l` those are
the paper's own numbers: the `Sigma_Pi` branch gives 31, the `D35` branch 29 — the remark's
`dim W_int = 31` exactly. B23-10 reproduced the certificates with its own code.

**What survives.** B23-03's **G-A1**: the boundary `(D45 \ D45°) ∩ P5` is untouched, and B23-10
rules it "**genuinely open**". Any component it forms has affine dimension `>= 19`. So the
remark's caveat is right in its bottom line and wrong in its object.

**Still unresolved in the paper.** Theorem 6.2 says "unconditional" (correct: session 32) while
Remark 6.3(ii) says the stratum list "is longer than the classification used above" (correct:
session 66, eight components plus a 49-dimensional semi-primitive one). These are enumerations
of **two different objects** — the 4-dimensional singular subspaces, and the components of
`Proj gr_J R` — and the paper never says so, which is what makes the two read as contradictory.

**[AUTHOR] decision.** B23-03 is on branch `b23-03-intersection` and is **not an ancestor of
HEAD**. Whether Paper 2 may cite a sibling branch, or must wait for it to land, is not this
slot's call.

### B11 — The cap minors vanish off `D^det_5`, and §7 does not say so [AUTHOR]

**What.** §7 presents the size-`cap(n)` minors purely as equations of `D^det_5`, and
Conjecture 7.2 as "the Jacobian minors are the first equations".

**The record.** B23-03 **Proposition 2.5 (PROVED, by hand)**: at `n = 3`,
`rank M_4(C) <= 64` — i.e. the size-65 minors vanish — for **every** `C ∈ Sigma_Pi`, the cubics
containing a plane, with generic value exactly 64. `Sigma_Pi` is 31 aff / 30 proj and
`T1 ⊄ T2`, so this is a family strictly larger than, and not contained in, `D35` (29 aff). This
supersedes B22-10's single measured rank of 64, which B23-03 §2.4 item 4 corrects explicitly:
"That was one MEASURED rank, and a single point cannot bound the generic rank from above. It is
**now PROVED for every member**." B23-10 confirms: "B23-03's Prop. 2.5 now proves it".

**Why it matters to the paper.** The zero locus of the cap minors is strictly larger than
`D^det_5`. That does not touch Theorem 7.1 or Conjecture 7.2 as stated, but it does bear on how
they are read — and on any use of the minors as a separating equation, which is the use Paper 3
puts them to. One sentence, plus a decision about whether Conjecture 7.2's phrasing should note
it. **[AUTHOR]**, and again gated on B23-03's branch status.

### B12 — §8's quantitative claims are contradicted by the record

Three, in two sentences:

1. "confin\[es\] the highest-weight vectors … to a single character-isotypic component, of
   dimension `n_χ ≈ N_S/|Stab_W(λ)|`" and "cutting the working dimension by **up to**
   `|Stab_W(λ)|`". `docs/PROVED.md` `nchi_2_21_guard`: "**`n_χ` is not `N_S/|Stab|`** — that
   quotient is neither an upper nor a lower bound for it." Measured both ways:
   `nchi_lb_field_is_false` (B14-09) has 135 of 222 cells with `n_χ` strictly **below** the
   quotient — a *larger* reduction than "up to `|Stab|`" allows; `nchi_est_is_the_forbidden_quotient`
   (B14-12) has the true `n_χ` **higher** at both cells where it is now known, 1,606,104 against
   1,528,114 at `(10,6,6,6,2,2)_8`.
2. "brings weights of `N_S` up to `1.5×10⁶` … within reach" is stale by more than an order of
   magnitude: `build_no_longer_binding` (B13-10) puts the ceiling at `N_S·δ ≈ 2.8–5.4×10⁸`, and
   `proved_but_uncertifiable` records `(12,4,4,4,4,4)_8` closed at `N_S·a = 1.08×10⁸`.
3. "the **senary sextic** invariant" is misnamed. The record's cell is `I_6`, **the unique
   degree-6 invariant of senary quartics**, weight `(4^6)`, `N_S = 1,532,489`, `n_χ = 2804`
   (`docs/stabiliser_reduction.md` §4.3 @ `82633a60`). The two numbers are right.

The lemma itself (Theorem 8.1) is PROVED and matches the record exactly, including the
2-transitivity remark.

### B13 — §1 and Question 10.5 understate the cubic-side silence

**What.** §1: "that ideal is empty in every degree we have been able to compute — through degree
eight **for every length at most six** \[Companion\], and in degree nine at `r = 6`".
Question 10.5 repeats the framing.

**The record.** `docs/PROVED.md` `degree8_global`, **PROVED**: `I(D_r^{per₃})_δ = 0` for
**every `r`** and every `δ <= 8`; hence `mult_pad = mult_red` at every weight of every length in
every degree `<= 8`. It is flagged there as "a **RECONCILIATION RESULT** — stated by no single
session", assembled from `washout_thm2` (`ℓ <= 5`), `length6_record` (`ℓ = 6`), B13-09 (`ℓ = 7`
at `δ = 8`, all 42), B13-05 (`ℓ = 8` at `δ = 8`, all 6) and `length_bound`. Paper 3 states it as
**C33, PROVED**.

Related, and worth a sentence in Question 10.5: `length_bound`'s window is
`6 <= ℓ(μ) <= min(r, δ)`, and its historical `, 9` clamp has been **WITHDRAWN** — "the equations
of 'supported on `<= 9` variables' are the obvious candidate at `r, δ >= 10`".

### B14 — Two self-citations a reader cannot follow, and one malformed locator [AUTHOR]

`\cite[\S]{Companion2}` (L440) prints "[§]" with no number. More substantially, `Companion`
("in preparation") and `Companion2` ("technical report, this programme") are the paper's two
most-used references — 11 and 1 citations — and neither is locatable by a reader. `Companion2`'s
content is `docs/singular_spaces.md` (session 32) and `docs/l5_containment.md`. How to cite
unpublished companion material at submission is the author's call; the locator is a typo either
way.

### B15 — "the second author" on a single-author paper

§1, L183: "improves the second author's earlier bound `80` at `n = 3` to `65` \[Companion\]".
The paper has one author. While there: the record's current bracket for that quantity is
`6 <= δ_0 <= 65` unconditionally and `8 <= δ_0 <= 65` given the batch-13 total-deficit identity
(Paper 3 **C12** @ `ce43cdb7`), and `δ_0` is defined there as `onset I(D_35)`, the onset for
quinary **cubics** — a scope note the paper does not carry.

### B16 — Acknowledgements against the paper's voice [AUTHOR]

"The work reported here was carried out jointly with Claude (Anthropic). Responsibility for the
correctness of every statement in this paper rests with the named author." — against a
single-author byline and a "we" throughout. This is the same question B23-05 left open for
Paper 1, and the B24-12 ledger §9 lists "Paper 1's attribution wording … **Your credit line**"
as a decision open for the user. Paper 2 should be resolved the same way, whichever way that is.

---

## 2. Overlap with Paper 3 — reported, not resolved

Paper 3 is `papers/det4-blindness/det4-blindness.tex` on branch `b23-04-paper3` @ `ce43cdb7`
(B23-04), with `CLAIMS.md` (46 rows), `GAPS.md` and `BIB.md`. It is **not** an ancestor of HEAD.
The two papers are companions and now say several of the same things in two different voices —
and, more awkwardly, with **two different labels**.

| the statement | Paper 2 | Paper 3 | the friction |
|---|---|---|---|
| the cap theorem, `cap(n) = 5n(n−1)²(7n−8)/12` | **Thm 7.1**, stated flatly with a four-step proof, listed in the abstract under "we prove" | **C11**, `\prov{ADOPTED modulo Kleiman \lit{Kleiman}{SECONDARY}, Dimca \lit{Dimca13}{PRIMARY, statement level} and Gulliksen–Negård \lit{GN}{SECONDARY}}` | the **same theorem with two different labels**, one of them in a paper that prints read-statuses at every point of use. Two papers from one programme cannot ship like this |
| the washout | **Thm 3.1 + Cor. 3.2**, with the proof | **C32**, a `record` environment, PROVED, pointing at `washout_lemma.md` | duplication; decide which paper carries the proof |
| degree-eight silence on the cubic side | §1 prose, understated (**B13**) | **C33**, stated correctly for every `r` | Paper 3 is right and Paper 2 is behind |
| `D45 ∩ P5` | **Thm 6.2 + Rem. 6.3**, long, measured, hedged | **C35 + C36**: "the intersection is larger than expected" (plane family `>= 35` affine against 33), classification **OPEN**, "this paper says nothing more about it" | **both are now stale** against B23-03 Thm 2.1. B23-10 §6.1 already lists C35 and C36 as two of the five rows Paper 3 must update |
| whether the cap minors vanish on the plane family | not mentioned | **C37**, OPEN with a single-point measured rank | **both stale**: B23-03 Prop. 2.5 PROVES it (**B11**). B23-10 lists C37 among the five |
| the `n = 3` positive control, `Δ = +1` at `(19,7,2^5)_{12}` | a §9 subsection, ~40 lines, presented as "the first `Δ > 0` this programme has produced end to end" | **C45**, "the `n = 3` ladder", the positive control | the same control as the emotional centre of two papers |
| the padded `n = 3` control is degenerate | a paragraph inside the same subsection | **C46**, its own record row | duplication |
| dimensions of `D^det_r`, `D35` | **Prop. 2.1** | **C01, C03** | duplication |
| `δ_0` | §1, "80 → 65" | **C12**, with the scope note ("never denotes an onset of `I(D_ff)`") and the current bracket | Paper 2 is behind |

**One structural difference to weigh, not a defect.** Paper 3 carries a per-claim provenance
macro (`\prov{label}{source @ commit}{lineage}`) and a bibliography grouped by read-status.
Paper 2 carries neither. If the two ship together, the asymmetry will be the first thing a
reader notices.

**Not resolved here, by instruction.** No recommendation is made about which paper keeps which
result.

---

## 3. Not blockers

Recorded so nothing looks overlooked.

- **Numbering, references, bibliography** are clean: 33 labels, 22 references, 0 undefined
  references, braces and `$` balanced, all 16 bibliography keys cited, every cited key present.
  11 labels are unused (`prop:dims`, `prop:contain`, `thm:frame`, `rem:gate`,
  `rem:noncontain-status`, `cor:pointfree` and six section labels) — harmless.
- **`\subjclass`, `\keywords`, arXiv categories** unchecked, exactly as B23-05 left them for
  Paper 1.
- **The source has not been compiled**: no LaTeX toolchain is installed in this environment. The
  checks above are mechanical, by script, from the scratchpad; nothing was written to the tree.
- **Thm 7.3's second half** ("`D^det_5` is an irreducible component of the closure of the
  six-nodal locus") has no proof in its sketch; the record supplies one
  (`docs/onset_conjecture.md` §4(iii), `def_3(N) = 0`, tangent space of dimension 28).
- **§7.1** drops the record's condition on the component claim ("at every `n` **where the minor
  ideal is saturated in degree `n`** (measured at `n = 3..7`)") — a G26 scope widening, but a
  narrow one; it is logged in `PAPER2_GAPS.md` as G-P2-09.
- **Rem. 9.3's** reading of BIP is narrower than `bip_blind_at_n4`'s, which locates the failure
  in weight length rather than in the size of the constant; and B23-06 §1 adds that BIP Thm 1.4
  is about **occurrence**, so it constrains multiplicity obstructions at **no** `n`.
- **Thm 9.2** is in a `theorem` environment and is a measurement (2585 cells, exhaustive,
  `docs/det_onset.md`). Environment choice, not a defect in the number — 2585 is confirmed.

---

## 4. B25-02 repair status (2026-09-22, UNCOMMITTED, producer-only)

Appended by B25-02; sections 0–3 above are the unchanged B24-06 assessment. Full dispositions,
evidence and edited locations: `docs/b25_02_report.md` §5.

| blocker | B25-02 disposition |
|---|---|
| B1 | REPAIRED — checked at Kadish–Landsberg Thm 1.3 (PRIMARY, arXiv:1204.4693v1); `mult = 0`, whole isotypic component in the ideal |
| B2 | REPAIRED — Thm 9.1 is Theorem A's clauses: Δ ≤ 0 (ℓ ≤ 4, every δ, containment); `i_det = 0` (ℓ ≤ 3, every δ); ℓ = 4 only for δ ≤ e − 1, e ≥ 10 CERTIFIED, e = 320112 ADOPTED (LLV Thm 2, now PRIMARY-read) |
| B3 | REPAIRED — gate ℓ ≥ 5; open five-row region preserved; washout = interpretation, not impossibility |
| B4 | REPAIRED — Δ ∈ [−4, −2], CERTIFIED conditional on ADOPTED dim N13 = 73; [−4, −3] not used |
| B5 | REPAIRED, qualified — LMR read PRIMARY (Thm 1.0.1, 2.3.1, 3.1.1, §3.2); C45 carries (★) |
| B6 | REPAIRED — Beauville read PRIMARY (v2): it contains none of Prop. 2.1 / Thm 7.1 Step 2 / Thm 7.3; used at Prop. 6.1 only; LLV cited; cap label in abstract and Thm 7.1 |
| B7 | REPAIRED — MM removed; only in-lemma tori used |
| B8, B9 | REPAIRED |
| B10 | QUALIFIED — and Thm 6.2 downgraded to the determinant part; closure statement carried as ADOPTED (B17-01), G-A1 OPEN |
| B11, B12, B13, B15 | REPAIRED |
| B14 | PARTLY — locators fixed (Paper 1 Prop. 4.19 / 4.23 / Q 8.5); companion locatability [AUTHOR] |
| B16 | untouched [AUTHOR] |

New findings recorded by B25-02: N1 Prop. 6.1's inequality was reversed; N2 "maximal minors" in
the abstract; N3 Thm 6.2 "unconditional" not supported for the closure; N4 Lemma 3.3 scope beyond
n = 4; N5 "Prop. C" locator nonexistent; N6 Thm 7.3 already sketched in Paper 1 Q 8.5 remarks.
**Not ready**: uncompiled (no toolchain), plus report §6.
