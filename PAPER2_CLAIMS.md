# PAPER2_CLAIMS — every numbered result of `paper/det4-onset.tex`, against the record

Slot B24-06, 2026-09-19/20. **Assessment only; the `.tex` is unchanged.**

**Provenance, recorded before any write.**

```
worktree   C:\Users\swami\Projects\gct-gpt\work\batch15_workers\B24-06
branch     b24-06-paper2
HEAD       82633a60893236fab4fbc317df416e1b8a349005
HEAD^{tree} e82fd3291d1a2adc8a577647314c251366ff5142
git status --porcelain   (empty)
paper      paper/det4-onset.tex, 957 lines,
           sha256 7c2bc7365c3aacc75e5d79906a4aaa3364ff015e5bbc91e2f585b1ca45678b7b
           last touched a1bf7c00, 2026-09-09
```

Read-only git; no commit, no computation, no pilot.

**How old the draft is.** `a1bf7c00` is **434 commits** behind `82633a60`, and the next commit
after it is `3d978222` ("Batch 13 consolidated"). So the paper predates the **dispatch of
Batch 13**, not Batch 14: eleven batches of record have landed since, not nine. (The 2026-09-17
stocktake's "since Batch 14" is one batch generous. First brief item checked.)

## Reading the columns

- **paper's label** — what the draft claims for itself (theorem / proof sketch / measured / conjecture).
- **record label** — the label the governing packet carries. Labels are quoted, never upgraded (G26).
- **source @ commit** — the packet and the commit at which the statement is there.
- **lineage** — who produced it and who re-derived it.
- **stale?** — whether the record has moved under the paper since `a1bf7c00`.

**Reachability of sources.** Everything cited as `@ 82633a60` is in this worktree's tree. Three
classes of source are **not**:

| source | where | status |
|---|---|---|
| `docs/b23_03_report.md` | branch `b23-03-intersection` @ `3bcad666`, sha256 `0101f224…` | committed, but **not an ancestor of HEAD** (`git merge-base --is-ancestor` fails) |
| `papers/det4-blindness/*` (Paper 3) | branch `b23-04-paper3` @ `ce43cdb7` | committed, not an ancestor of HEAD |
| `docs/b23_06_report.md`, `docs/b23_10_review.md`, `docs/b23_12_ledger.md`, `docs/b15_01_report.md` | worktrees B15-02, B15-10, B15-12, B15-01 | **uncommitted**. sha256 of the B23-10 review is `8bbc8d9eaee69620…`, which is the hash the B23-12 ledger §2.0b binds |
| the 2026-09-17 stocktake itself | — | **not found.** No file under `work/` or in the tree contains the phrase "second author"; the description of Paper 2 that this slot was sent to check is not on disk anywhere I can reach (GAPS G-P2-16) |

---

## A. The abstract

| # | claim | paper's label | record label | source @ commit | lineage | stale? |
|---|---|---|---|---|---|---|
| A1 | (i) washout: `per_3` restricts to a generic reducible form at every `r <= 5`; permanent's structure first at length six, degree seven | "we prove" | PROVED | `docs/washout_lemma.md` §0, Thm 2 + Thm 3(1); `docs/PROVED.md` `washout_thm2`, `restriction_lemma` @ `82633a60` | s26 → re-verified s37 → **re-derived from its generator by B13-07** | no |
| A2 | (ii) transfer lemma: the reducible locus is a complete screen | "we prove" | PROVED | `docs/transfer_lemma.md` §0, Lemmas 1–2 @ `82633a60` | s37 | no |
| A3 | (iii) combinatorial criterion for `I({l·c})`, recovering Kadish–Landsberg as its degenerate case | "we prove" | PROVED (every `n, r, δ, k`) | `docs/reducible_ideal.md` §0 Thm 1 @ `82633a60` | s36 (post hoc, 91 cells) → written as a theorem s40 | no |
| A4 | (iv) cap theorem, `cap(n) = 5n(n−1)²(7n−8)/12` | "we prove" | **"proved modulo Kleiman, Dimca and Gulliksen–Negård, all adopted and named"** | `docs/onset_conjecture.md` §0 Thm 1 @ `82633a60` | s35 (cap at `n=4`) → s40 (every `n`) | no — but the modulus is dropped from the abstract's "we prove". Paper 3 labels the same theorem **ADOPTED modulo** those three (`papers/det4-blindness/det4-blindness.tex` C11 @ `ce43cdb7`) |
| A5 | "the cap is exact at `n = 2`" | proved | PROVED | `docs/onset_conjecture.md` §2.6 @ `82633a60` | s40 | no |
| A6 | "improves the second author's earlier bound `80` at `n = 3` to `65`" | — | the bracket is Paper 1's `δ_0`; record value **`6 <= δ_0 <= 65` unconditionally, `8 <= δ_0 <= 65` given the batch-13 total-deficit identity** | Paper 3 C12 @ `ce43cdb7`, quoting the GKZ scope corrigendum | B22-12 ledger §3 | **yes** — and "second author" is wrong on a single-author paper (blocker B15) |
| A7 | "Across the entire computed range we find no multiplicity obstruction" | measured | MEASURED / CERTIFIED per cell | `docs/det_onset.md` §0, `docs/PROVED.md` `b14_11_quartic_census` @ `82633a60` | s38, B14-11 | **partly** — the computed range has grown: B14-11's census is the whole `n=4`, `δ <= 8`, `5 <= ℓ <= δ`, `λ_1 >= δ` region, **4,198 labels, 2,734 with `a > 0`, of which 2,571 remain open** |

---

## B. §2 — the two varieties

| # | result | paper's label | record label | source @ commit | lineage | stale? |
|---|---|---|---|---|---|---|
| B1 | **Prop. 2.1** (Dimensions): `dim D^det_5 = 50`, `codim 20` in `W_5` (70); `dim D^det_6 = 66`; `dim P_r = r + dim Sym³C^r − 1` for `r <= 5`; `dim P_6 = 55`, `dim R_6 = 61`; `dim R_r = r + C(r+2,3) − 1` | proposition, "unconditional given §3" | PROVED (the `n=4` table); the general formula `dim D_5^{det_n} = 3n² + 2` is **ADOPTED beyond `n = 4`** | `docs/washout_lemma.md` §4–§5; `docs/onset_conjecture.md` §1 and §6 "Honest boundary" @ `82633a60` | s26, s30, s33 tables → made unconditional by s37's stabiliser count | no — **but the statement contains a garbled formula** (blocker B9) |
| B2 | "The generic member of `D^det_5` is a quartic threefold with exactly 20 ordinary double points and defect one; it is non-`Q`-factorial" | proposition text, proved | PROVED: `ν(4) = 20`, `def_{2n−5} = 1` exactly (measured, both primes); non-factoriality is the defect | `docs/onset_conjecture.md` §0, §2.2, §4 @ `82633a60` | s40 | no |

---

## C. §3 — the washout theorem

| # | result | paper's label | record label | source @ commit | lineage | stale? |
|---|---|---|---|---|---|---|
| C1 | **Thm 3.1** (Washout): `P_r = R_r` for `r <= 5`; no covariant of length `<= 5` distinguishes the padded permanent from `l·(any cubic)` | theorem + proof | PROVED | `docs/washout_lemma.md` §0 Thm 2, Thm 3(1); `docs/PROVED.md` `washout_thm2` @ `82633a60` | s26 (rank 35, both primes) → s37 → **B13-07 re-derived it from its generator** | no. Paper 3 states the same as C32, PROVED |
| C2 | **Cor 3.2**: onset of the separation is a length-six phenomenon; `dim P_6 = 6 + 50 − 1 = 55` vs `dim R_6 = 6 + 56 − 1 = 61` | corollary | PROVED | `docs/washout_lemma.md` §0 Thm 6; `docs/transfer_lemma.md` Lemma 1 @ `82633a60` | s37 | no |
| C3 | **Lemma 3.3** (Finite generic stabiliser), with `dim D^det_r = min(dim W_r, n²r − dim Stab(det_n))` for `r >= 3` and `dim Stab(per_3) = 4` | lemma + **proof sketch** | PROVED at `n = 4` and for `per_3`; the count beyond `n = 4` is **ADOPTED** | `docs/washout_lemma.md` §4; `docs/onset_conjecture.md` §6 ("**adopted**: the finite-stabiliser dimension count `dim D_5^{det_n} = 3n²+2` beyond `n = 4`") @ `82633a60` | s37 wrote it once for `per_3` and once for `det_4` | **scope widened** — the paper quantifies over all `n`; the record proves `n = 4` and adopts the rest (G26). The proof sketch also ends in a garbled clause (blocker B9) |
| C4 | **Prop. 3.4** (Pieri delay): `I(P_6)_δ = I(R_6)_δ` for `δ <= 5`; permanent's own structure first visible at `δ >= 7` | proposition | PROVED (`δ <= 5` by Pieri; `δ = 6` measured) | `docs/transfer_lemma.md` §0 and Prop. 8; `docs/PROVED.md` `length6_record` @ `82633a60` | s37, s41, s43 | no. The **surrounding §1 prose** is understated: the record is `I(D_r^{per₃})_δ = 0` for **every `r`** and every `δ <= 8` (`degree8_global`, PROVED), not "every length at most six" |

---

## D. §4 — the transfer lemma

| # | result | paper's label | record label | source @ commit | lineage | stale? |
|---|---|---|---|---|---|---|
| D1 | **Thm 4.1** (Transfer), items (1)–(3) | theorem + proof | PROVED | `docs/transfer_lemma.md` §0, §1 Lemmas 1–2 @ `82633a60` | s37, formalising the `docs/s35_review.md` §1 caveat | no. The record adds one clause the paper drops: `P_r = R_r` **iff** `r <= 5` |

---

## E. §5 — the reducible ideal

| # | result | paper's label | record label | source @ commit | lineage | stale? |
|---|---|---|---|---|---|---|
| E1 | **Thm 5.1** (the reducible criterion (★)), with the multiplicity-`k` version | theorem + **proof sketch** | PROVED, for every `n, r, δ, k` | `docs/reducible_ideal.md` §0 Thm 1 @ `82633a60` | s36 derived it post hoc and used it at 91 cells; s40 wrote it with the Bruhat proof in full | no |
| E2 | **Cor 5.2** (point-free multiplicity) | corollary | PROVED (Corollary A) | `docs/reducible_ideal.md` §0 @ `82633a60` | s40 | no |
| E3 | **Cor 5.3** (padding bound): "`mult_λ C[R_r] = a(λ,δ)` and `I(R_r)` has no length-`ℓ(λ)` part at `λ`" | corollary | PROVED as **`mult_λ C[Y]_δ = 0`** | `docs/reducible_ideal.md` §0 Corollary B; `docs/PROVED.md` `quartic_length_and_eligibility` ("`mult_pad > 0` implies `λ_1 >= δ`") @ `82633a60` | s40; Kadish–Landsberg Thm 1.3 is the prior statement | **WRONG DIRECTION — blocker B1.** The paper's own Cor 5.2 gives `0`. The final sentence ("no obstruction at `λ_1 < δ`") survives |
| E4 | "`I(R_r)` begins in degree five for every `r >= 5`"; the degree-5 quinary invariant is an `a = 1` cell | proved + measured | PROVED + MEASURED; `onset I(R_r) = 5` for `r >= 5`, and `I(R_r)_5` is exactly the `(4^5, 0^{r−5})` isotypic component | `docs/reducible_ideal.md` §4 Proposition, items 1–3 @ `82633a60` | s35, s36 | no. Two items the paper omits: at `r = 3, 4` the onset is **6**; and `I_5, I_6` do **not** generate — three further minimal generators at degree 7 |
| E5 | "the technique is theirs, the exact criterion of Thm 5.1 we have not found stated" | attribution | the record's wording: "**as far as one pass shows**, not on record … we claim them as not-found-in-the-literature, **not as new**" | `docs/reducible_ideal.md` §0 and §5 @ `82633a60` | s40, one literature pass | **under-labelled** — the paper does not name the five sources the one pass checked (blocker B6(d)) |

---

## F. §6 — containment at `r <= 4`, non-containment at `r = 5`

| # | result | paper's label | record label | source @ commit | lineage | stale? |
|---|---|---|---|---|---|---|
| F1 | **Prop. 6.1** (Containment, `r <= 4`) | proposition + proof sketch | **ADOPTED** ("a containment exclusion, not an empty-ideal assertion") | `docs/PROVED.md` `n4_gate_containment`; `docs/n4_gate.md` §1 Theorem (proved there) @ `82633a60` | s27; the board never cited it, which `docs/PROVED.md`'s own preamble calls out | no — but the paper writes `R_r ⊆ D^det_4` where `D^det_r` is meant (blocker B8) |
| F2 | **Thm 6.2** (Non-containment at `r = 5`), "unconditional", max rank `31 < 35` | theorem, unconditional | PROVED, unconditionally, **after** session 32 classified the 4-dimensional singular subspaces of `M_4(C)` completely: four compression branches at ranks `29, 31, 31, 29`, plus **two exceptional strata at 27 and 25** | `docs/singular_spaces.md` §0, §1; `docs/l5_containment.md` §3 + the session-32 update @ `82633a60` | integrator (branch ranks) → s32 (classification + independent reimplementation) | no on the mathematics; **the statement misdescribes its own input**: "five-dimensional" should be four-dimensional (the paper's very next sentence says four), "not all compression spaces" is the obstacle s32 had to *overcome*, and the appeal to "highest-weight vectors" is a non-sequitur (blocker B8) |
| F3 | **Rem. 6.3** (i) the contact-order lemma | "now proved" | on the record | s66 chain; `docs/s66_report.md` @ `82633a60` | s62/s63/s66 | no |
| F4 | **Rem. 6.3** (ii) eight components once `SP` is included; a further 49-dimensional semi-primitive component absent from every earlier stratum list; `P ∩ ker` is rank-`<= 2` | "now proved" | on the record | `docs/s66_report.md` §§; `docs/stocktake_batch10.md` L194; `docs/housekeeping_batch10.md` L67 @ `82633a60` | s66 | **yes, and it is now the wrong worry** — see F6 |
| F5 | **Rem. 6.3** (iii) base scheme non-reduced along every pairwise incidence: `dim Q_2 = 12 < 16`, `41 < 69`, `25 < 49`, `59 < 144` | "now proved" | on the record, all four | `docs/s66_report.md` L75–76; `docs/s62_s63_s66_review.md` L117–118; `docs/batch11_plan.md` L464–465 @ `82633a60` | s66, reviewed | no |
| F6 | **Rem. 6.3** (iv) the four residues are numbers; `dim W_int = 31`; "`dim(D^det ∩ W) = 31 < 35` on the enumerated cone"; "**what is still not proved is that the enumeration is complete**" | measured + one "evidence rather than proof" | **superseded on the interior.** B23-03 **Theorem 2.1 (PROVED)**: `closure(D45° ∩ P5) = T1 ∪ T2`, with `T1` **33 aff / 32 proj**, `T2` **35 aff / 34 proj**, `Sigma_Pi` **31 aff / 30 proj**, `T3` **29 aff / 28 proj**. At a fixed `l` that is exactly the paper's 31 (the `Sigma_Pi` branch) against 29 (the `D35` branch) | `B23-03/docs/b23_03_report.md` §2.4 @ `3bcad666` (**not an ancestor of HEAD**), sha256 `0101f224…`; reviewer-reproduced in `B15-10/docs/b23_10_review.md` (uncommitted, sha256 `8bbc8d9e…`) | B22-10 → B23-03 → B23-10 reproduced all 8 determinant floors, 8 padding ceilings, 3 Newton certificates | **yes.** The interior enumeration is now a theorem; what remains is B23-03's **G-A1**, the boundary `(D45 \ D45°) ∩ P5`, ruled "**genuinely open**" by B23-10, with any component of affine dimension `>= 19`. The paper's eight-component worry (F4) is about the base scheme of `Φ`, a different object, and the remark does not say so |

---

## G. §7 — the cap theorem

| # | result | paper's label | record label | source @ commit | lineage | stale? |
|---|---|---|---|---|---|---|
| G1 | **Thm 7.1** (the cap), values `5, 65, 300, 900, 2125, 4305` | theorem + four-step proof | **"proved modulo Kleiman, Dimca and Gulliksen–Negård, all adopted and named"** | `docs/onset_conjecture.md` §0 Thm 1, §2.1–§2.5 @ `82633a60` | s35 (`n = 4`) → s40 (every `n`); Paper 3 carries it as C11 **ADOPTED modulo** the same three, with read-statuses attached | no — but the modulus is not attached to the theorem (blocker B6(c)). Arithmetic re-derived here: `cap(n)` closed form, `5C(2n,4) − 10C(n+1,4)`, `μ_{3n−5}(n)` and `ν(n)` all check at `n = 2..7` |
| G2 | Step 2: Kleiman's transversality gives `ν(n) = n²(n²−1)/12` ordinary double points | proved modulo Kleiman | ADOPTED (Kleiman, characteristic 0), rest PROVED | `docs/onset_conjecture.md` §2.2 @ `82633a60` | s40 | no. **Kleiman is SECONDARY (not read)** on the record — `papers/det4-blindness/BIB.md` @ `ce43cdb7`, route B20-10 R15 |
| G3 | Step 3: the nodes fail degree `2n−5` forms by one, via Gulliksen–Negård | proved | PROVED, three routes; (c) modulo the adopted GN resolution | `docs/onset_conjecture.md` §2.3 @ `82633a60` | s40 | no. **GN is SECONDARY (not read)**, same source |
| G4 | Step 4: Dimca, `\cite[Thm.~3.1]{Dimca13}` | adopted | ADOPTED; theorem number **confirmed** as Thm 3.1, statement re-read | `docs/onset_conjecture.md` §2.4 @ `82633a60`; **PRIMARY** read-status with PDF hash in `papers/det4-blindness/BIB.md` @ `ce43cdb7` | s37 pinned it; s40 re-read | no. The one load-bearing citation with a clean read-status |
| G5 | "Measured, both primes, fresh pencils": coranks `6, 31, 102, 256, 541` at `n = 3..7` against smooth `5, 30, 101, 255, 540` | measured | MEASURED, both primes | `docs/onset_conjecture.md` §0 and §6 @ `82633a60` | s40 | no. All ten values re-derived arithmetically here from `μ_{3n−5}(n)`; they agree |
| G6 | **Conj. 7.2** (the onset is the cap) | conjecture | **Expectation**, labelled | `docs/onset_conjecture.md` §0 Conjecture 2, §3 @ `82633a60` | s40 | no |
| G7 | Evidence for 7.2 at `n = 3`: empty through degree seven; empty on all **121** length-five cells at degrees eight and nine; the degree-10 `SL_5` invariant does not vanish, so no invariant below degree fifteen is an equation | measured | MEASURED | `docs/onset_conjecture.md` §0 Deliverable-4 runs @ `82633a60` | s40; `results/n3_ledger.md` | no. **121 = 72 (at `δ = 8`, `n_χ <= 6659`) + 49 (at `δ = 9`, `n_χ <= 2500`)** — these are the affordable cells, not all cells, and the paper's "measured" is the right word |
| G8 | Evidence at `n = 4`: empty through degree seven, and on every measured cell at degree eight | measured | MEASURED, **on the measured corner only** — "δ=8 is excluded only on the measured corner (27 of 435 cells), so the onset could still be 8 on an unreached cell" | `docs/det_onset.md` §0.2 @ `82633a60` | s38 | no |
| G9 | **§7.1 the `n = 5` anomaly**: `ν(5) = 50` but `codim = 49`; `D^det_5` a superabundant component of the 50-nodal locus, dimension 76 against the expected 75 | proved + measured | PROVED + MEASURED, **with a condition the paper drops**: `D_5^{det_n}` is a component of the `ν(n)`-nodal locus "at every `n` **where the minor ideal is saturated in degree `n`** (measured at `n = 3..7`)" | `docs/onset_conjecture.md` §0, §4 @ `82633a60` | s40 | **condition dropped — G26.** The identity `codim = ν(n) − C(n−1,4)` re-derived here and correct at `n = 3..6` |
| G10 | **Thm 7.3** (the `n = 3` twin) | theorem + proof sketch | PROVED, with two exact certificates | `docs/onset_conjecture.md` §0 and §5 Theorem 3 @ `82633a60` | s40; answers Paper 1's Question 8.5, first sub-question | no. Two omissions: the "irreducible component of the six-nodal locus" half is proved in the record by §4(iii)'s tangent-space argument (`def_3(N) = 0`), which the sketch does not carry; and the record flags the classical neighbourhood (the `P^4` of cubics through a fixed frame contains the Segre cubic) that the paper does not — see blocker B6(a) |

---

## H. §8 — the stabiliser-isotypic reduction

| # | result | paper's label | record label | source @ commit | lineage | stale? |
|---|---|---|---|---|---|---|
| H1 | **Thm 8.1** (Reduction): `P_w v = χ_λ(w) v`, `χ_λ(w) = Π_B sgn(w_B)^{m_B}` | theorem + proof sketch | PROVED, and validated by tests the wrong sign rule fails | `docs/stabiliser_reduction.md` §1 Lemma @ `82633a60` | s36; validation `results/stabred_validation.md` | no |
| H2 | "of dimension `n_χ ≈ N_S/|Stab_W(λ)|`", "cutting the working dimension by **up to** `|Stab_W(λ)|`" | stated as fact | **contradicted.** "`n_χ` is **not** `N_S/|Stab|` — that quotient is neither an upper nor a lower bound for it" | `docs/PROVED.md` `nchi_2_21_guard`, `nchi_lb_field_is_false` (B14-09: 135 of 222 cells have `n_χ` strictly **below** it), `nchi_est_is_the_forbidden_quotient` (B14-12: true `n_χ` **higher** at both cells where it is known — 1,606,104 vs 1,528,114) @ `82633a60` | B14-09, B14-12 | **yes — blocker B12** |
| H3 | "brings weights of `N_S` up to `1.5×10⁶` within reach (e.g. the senary sextic invariant, `N_S = 1,532,489` → `n_χ = 2804`)" | measured | the cell is right; the **name** is wrong and the **reach** is stale | cell: `docs/stabiliser_reduction.md` §4.3 — "the unique degree-6 invariant `I_6` of senary **quartics**, weight `(4^6)`" @ `82633a60`. Reach: `docs/PROVED.md` `build_no_longer_binding` (ceiling `N_S·δ ≈ 2.8–5.4×10⁸`), `proved_but_uncertifiable` (`(12,4,4,4,4,4)_8` closed at `N_S·a = 1.08×10⁸`) | s36; B13-10; B14-12 | **yes — blocker B12** |
| H4 | "the one-operator shortcut … relies on 2-transitivity of the alternating group and does not generalise" | remark in the sketch | on the record | `docs/stabiliser_reduction.md` L109 @ `82633a60` | s36 | no |

---

## I. §9 — negative results

| # | result | paper's label | record label | source @ commit | lineage | stale? |
|---|---|---|---|---|---|---|
| I1 | **Thm 9.1** (Blindness on the short slab): "`mult_λ C[D^det_4] = a(λ,δ)` for **every** `ℓ(λ) <= 4` and **every** degree" | theorem + proof | **PROVED only below the `r = 4` onset.** Record Theorem A: `Δ <= 0` at `ℓ <= 4` for all `δ`; `det_units = 0` for `ℓ <= 3` at all `δ`, and for `ℓ = 4` **only at `δ <= e − 1`**, where `e >= 10` is certified (s33) and `e = 320112` is **adopted** (LLV) | `docs/blindness_slab.md` §0 Theorem A, §1 @ `82633a60`; `e` also in `docs/e4_hunt.md`, `docs/det_onset.md` L62, `docs/equation_census.md` row 13 | s37; `e` from LLV via s33 | **over-claimed — blocker B2.** `dim D^det_4 = 34` in `dim W_4 = 35`, so `I(D^det_4)` is principal and nonzero. The paper's own proof already hedges ("degree ≫ δ for the degrees in question") while the statement says "every degree". The **conclusion** `Δ <= 0` survives via Prop. 6.1 |
| I2 | "strict inequality exhibited at explicit cells" | asserted | the cells are on the record and unnamed in the paper: `D((8,8,8), 6) = −1` and `D((12,8,8), 7) = −1`, both proved + measured | `docs/blindness_slab.md` §0 @ `82633a60` | s37 | no, but incomplete |
| I3 | **Thm 9.2** (No arithmetic obstruction): no length-five cell occurrence-forced through degree ten, exhaustive check of **2585** cells | theorem, measured | MEASURED, exhaustive, and stated by the record in the same words | `docs/det_onset.md` §0.1 and L91, L165 @ `82633a60` | s38; corroborated `docs/external_reviews_round3.md`, `docs/s38_review.md` | no — 2585 confirmed. It is a **measurement**, not a theorem; the paper's environment says `theorem` |
| I4 | **Rem. 9.3** (the gate): BIP "requires `n >= m^25` and is silent at `(m,n) = (3,4)`"; the correct gate is `a >= 1` | remark | CONFIRMED and **sharper on the record**: BIP Thm 1.4's hypothesis is `n >= m^25` (PRIMARY, arXiv 1604.06431v3) and the theorem is about **occurrence, not multiplicity**, so it says nothing about multiplicity obstructions at **any** `n`; and the reach that actually fails at `n = 4` is measured in weight **length** | `B15-02/docs/b23_06_report.md` §1 (uncommitted, sha256 `a56d2394…`); `docs/PROVED.md` `bip_blind_at_n4`; `docs/n4_gate.md` §2 @ `82633a60` | B13-11/B14-11 → B23-06 read BIP at source | **partly** — the paper's reason is the constant; the record's is the mechanism |
| I5 | "the correct gate at small parameters is `a >= 1`" | remark | the current gate is **`a > 0` and `ℓ >= 5`** | `docs/PROVED.md` `quartic_length_and_eligibility`; `docs/n4_gate.md` §2 @ `82633a60` | B14-11 | no on `a`; the length half is missing, and §9's "length `>= 6`" contradicts it (blocker B3) |
| I6 | "The honest frame …: a map of where the certificate can live — **length `>= 6`**, degree `>= 8`, first row `>= degree`" | asserted | **`ℓ >= 5`**, not `>= 6`. At `r = 5` the paper's own Thm 3.1 gives `P_5 = R_5`, so `Δ = Δ_R` exactly and a positive `Δ_R` at `ℓ = 5` **is** an obstruction. The open region is `ℓ >= 5`: **2,571 of B14-11's 2,734 positive labels are still open**, concentrated there | `docs/n4_gate.md` §2; `docs/PROVED.md` `quartic_length_and_eligibility`, `b14_11_quartic_census`; `docs/batch14_close.md` L67, L153 @ `82633a60` | s27 → B14-11 → batch-14 close | **wrong — blocker B3.** "degree `>= 8`" and "first row `>= degree`" are supported (`I(D^det_5)` empty through 7, measured; `λ_1 >= δ` proved) |

---

## J. §9's two unnumbered subsections

| # | result | paper's label | record label | source @ commit | lineage | stale? |
|---|---|---|---|---|---|---|
| J1 | **The `n = 3` positive control**: `λ = (19,7,2^5)`, `δ = 12`, `r = 7`, `a = 6`, `dim D^det_7 = 47`, `dim P_7 = 59`, `mult_det = 5`, `mult_per = 6`, **`Δ = +1`** | measured, both primes | **RECORDED** (the certificate kind the record uses for this pair) | `docs/artifacts.md` L92 ("the permanent half of the `D = +1` at `(19,7,2⁵)₁₂`, both `RECORDED`"); `a = 6` and `N_S = 17,047` in `docs/b13_11_review.md` L88 and `docs/b13_10_report.md` D1 @ `82633a60` | batch-11 verifier extension; B13-10/B13-11 | no. Paper 3 carries the same as **C45** (`ce43cdb7`) — see the overlap note in `PAPER2_BLOCKERS.md` |
| J2 | "the padded `n = 3` cell can never carry an obstruction … forces `Δ <= 0` there identically" | proved in prose | PROVED, by a different route: `l·per₂ = z(ad+bc)` has **exactly five essential variables**, so `mult_pad = 0` at a seven-row weight, `i_pad = a`, padded gap **−5** | `docs/PROVED.md` `n3_padded_seven_row` @ `82633a60` | B13-11, promoted from assumption | no. The record's own caution is the paper's: "**The unpadded `+1` example at `(19,7,2⁵)` supplies no padded test**" |
| J3 | **The length-nine cell**: `a = 274`, `rank Θ^det = 273`, `i_det = 1`, padded floor 269 | measured + adopted | **CERTIFIED / ADOPTED** (`lmr_ranks`) | `docs/PROVED.md` `lmr_ranks`; `docs/lmr_cell.md` @ `82633a60` | s74 → replayed by B13-07 and B13-11 at both primes → 274/273/269 reproduced independently by B14-06 | no on the three numbers |
| J4 | "`Δ ∈ [−4, +1]`" | stated as the justified interval | **`D_LMR ∈ [−4, −2]`**; `i_pad(24) >= 3`, so `D <= −2`, and `D = +1, 0, −1` are **excluded at this cell**. CERTIFIED, conditional on the ADOPTED `dim N₁₃ = 73` | `docs/PROVED.md` `lmr_D_upper`; `docs/b14_01_02_joint_review.md`; `docs/batch15/ACCEPTED_STATE.md` @ `82633a60` | **B14-01 + B14-02 combined — a deduction neither report made**, each link checked by the integrator | **yes — blocker B4.** An uncommitted batch-15 result narrows to `[−4, −3]` (`B15-01/docs/b15_01_report.md`); that is a gaps entry, not prose |
| J5 | "the one-dimensional kernel is therefore \[LMR\]'s own equation"; "the determinant side is bounded below by \[LMR\] at this cell"; "the rigorous lower bound … remains \[LMR\]'s" | asserted, three times | the weight **is** LMR's `Ω(k,d)` at `n = 4`, `k = 6` — record-internal. But **LMR is UNREAD-SPECIALIST** on the record except for Thm 1.0.1 | `docs/lmr_cell.md` §1 @ `82633a60`; read-status in `papers/det4-blindness/BIB.md` @ `ce43cdb7` (UNREAD-SPECIALIST, B22-02 §5) and `B15-02/docs/b23_06_report.md` §1 (Thm 1.0.1 **PRIMARY**, arXiv 1004.4802v1, PDF sha256 `cfc28275a8c6b27f…`) | s55/s74 → B23-06 read Thm 1.0.1 | **blocker B5** — the module/equation statements the paper attributes to LMR are not verified at source anywhere on the record |
| J6 | "its residues are nonzero at every one of **282** integer padded points at both primes, so it does not vanish on the padded permanent"; "the observed nullity of five … is not a theorem" | measured, with the caveat stated | MEASURED, and the record states the same caveat in the same direction: "a five-dimensional sampled kernel at 282 points bounds `i_pad <= 5` and proves **nothing** downward" | `docs/PROVED.md` `lmr_D_measured`, `rank_floor`, `evaluation_cannot_certify_i_ge_1`; `docs/b13_07_report.md` L135 @ `82633a60` | s74 → B13-07 checked all 282 values at each prime | no — this is the paper at its most careful |
| J7 | "the padded and reducible kernels coincide, so `mult_pad = mult_red` and the whole question is one about `R_9`" | measured | MEASURED, both primes, independent evaluator | `docs/rung13_reducible.md` @ `82633a60` | integrator's own points, own evaluator, 43 reducible points, generic control 39/39 | no |

---

## K. §10 — open problems

| # | question | paper's framing | record | stale? |
|---|---|---|---|---|
| K1 | **Q 10.1** Is Conj. 7.2 true at `n = 3`? | balanced length-five cells at `δ = 8, 9` now within reach | matches `docs/onset_conjecture.md` §3 and `results/n3_census.md`'s named unmeasured cells @ `82633a60` | no |
| K2 | **Q 10.2** A `Δ > 0` between `P_6` and `D^det_6` at length six? "the **682** six-row cells we have measured through degree twelve … carry no determinant equation, no permanent-specific equation and no `per_4` equation, and **63** tails are closed at every degree" | measured | 682 cells at `δ <= 12`, tail weights 13–23, confirmed: `docs/s79_part2_review.md` L79, `docs/s79_review.md` L65/L78, `docs/b13_07_report.md` L186 ("all 682 determinant-full records agree"), `docs/b13_11_report.md` L67 ("682 cells remain **MEASURED**"); 63 tails with 69 cells: `docs/b13_07_report.md` L43, `docs/batch13_plan.md` L162 @ `82633a60` | **partly** — since then `docs/PROVED.md` `q1_queue_complete` closes **all 123** six-row cells of session 79's frozen Q1 queue with `i_det = 0`, the last by B14-12 at `N_S·a = 1.08×10⁸`; and `peaked_quartic_ladders` closes 10 more of the quartic census |
| K3 | **Q 10.3** A closed form for the extra Jacobian syzygy | open | matches: "**Not done**: no attempt to exhibit the extra syzygy in closed form (s35's adjugate candidate)" — `docs/onset_conjecture.md` §6 @ `82633a60` | no |
| K4 | **Q 10.4** Does the reducible-locus screen ever certify blindness over an unbounded degree range? | open | not contradicted on the record | no |
| K5 | **Q 10.5** Is `I(D_r^{per₃})_δ` ever nonzero? "It is empty in every degree we have computed" | open | `degree8_global` is **PROVED** for every `r` at every `δ <= 8`, and `length6_record` gives `δ <= 9` at `r = 6`; the constituent-length window is `6 <= ℓ(μ) <= min(r, δ)` (`length_bound`, PROVED, **with the historical `, 9` clamp WITHDRAWN**) | **understated** — the same defect as C4; and the withdrawn clamp is the kind of thing a question of this shape should name |

---

## L. What this table does **not** cover

- No claim here is upgraded, no condition dropped, no scope widened (G26). Where the paper is
  broader than its source, the row says so and the source's own words are quoted.
- Numerical re-derivations done in this slot are arithmetic only (`cap(n)`, `μ_{3n−5}(n)`,
  `ν(n)`, `codim = ν(n) − C(n−1,4)`, the corank columns, `9r − 16` and `9r − 4`). **No
  computation, no pilot, no `.pid`.** They agree with the paper and with the record at every
  value checked.
- Mechanical check of the source (script in the session scratchpad, not in the tree): 33 labels,
  22 references, **0 undefined references**, 11 unused labels, braces and `$` balanced, all 16
  bibliography keys cited and every cited key present. Theorem numbering re-derived and matches
  what the stocktake assumed for Prop. 2.1, Thm 6.2 and Rem. 6.3. **No LaTeX toolchain is
  installed here, so the source has not been compiled** — the same limitation B23-05 recorded
  for Paper 1.

---

## M. B25-02 changes to claim labels (2026-09-22, UNCOMMITTED, producer-only)

Rows A–K above are the unchanged B24-06 table. Label changes in the repaired after-state:

| row | after B25-02 |
|---|---|
| A4 / G1 | cap theorem printed as PROVED modulo Kleiman (SECONDARY), Dimca (PRIMARY, statement level), GN (SECONDARY), all ADOPTED — abstract and Thm 7.1 |
| A6 | "second author" removed; δ0 bracket 6 ≤ δ0 ≤ 65 (unconditional), 8 ≤ δ0 ≤ 65 given measured totals |
| B1 / C3 | Prop. 2.1 and Lemma 3.3 give an upper bound with equality at r = 3..6; count beyond n = 4 ADOPTED |
| E3 | Cor. 5.3 = KL Thm 1.3 (PRIMARY), `mult = 0` |
| F1 | Prop. 6.1 inequality direction corrected (≤), `D^det_r` |
| F2 | Thm 6.2 = determinant part (PROVED); closure `R5 ⊄ D^det_5` ADOPTED (B17-01), G-A1 OPEN |
| G9 / G10 | saturation condition restored; component half of Thm 7.3 now proved in sketch |
| H2 / H3 | n_χ by signed Burnside count; quotient neither bound; `I_6` of senary quartics |
| I1 | Thm 9.1 four items per Theorem A (see BLOCKERS §4) |
| I5 / I6 | gate ℓ ≥ 5; degree ≥ 8 labelled measured |
| J1 | Δ = +1 PROVED modulo (★) |
| J4 | Δ ∈ [−4, −2] CERTIFIED conditional on ADOPTED dim N13 = 73 |
| J5 | LMR uses cite Thm 1.0.1 / 2.3.1 / 3.1.1 / §3.2, PRIMARY; Thm 1.0.2 not used |
| C4 / K5 | `degree8_global` stated for every r, δ ≤ 8 (single reconciliation lineage) |
