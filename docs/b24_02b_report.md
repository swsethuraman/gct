# B24-02b — C45 closed: LMR Theorem 2.3.1 read, and recorded PRIMARY at the point of use

**Slot:** B24-02b, a half-slot. **Worktree:** `work/batch15_workers/B15-01`, branch
`b15-01-ci159`. **Starting HEAD:** `cc14e88cca7860b4a666ecf2bc18701ac8a05584`, confirmed by
`git rev-parse HEAD`; unchanged at close. `git status --porcelain --untracked-files=no` is
**empty** at start and at close — **read-only git, nothing committed, nothing staged**. B24-02's
untracked packet (`docs/b24_02_report.md`, sha256
`cf09c536cf1fb4ab65fb97ae538371e151b7e50bfaf5464c97a4120e3b125256`, matching the brief, and
`results/b24_02/`) was **left untouched**; this slot writes only `docs/b24_02b_report.md` and
`results/b24_02b/`.

**No pilot, no computation, no `.pid`.** The one-job rule was not engaged. I checked it anyway:
`..\B15-02\results\logs\b24_04_*.pid` now shows **three** receipts (`p1_patterns`, `p2_saturate`,
`p3_close`), so B24-04 has since spent the batch's numerical job. Nothing in this slot needed one.

---

## Outcome, up front

**Outcome 1: it checks out.** And it checks out **more strongly than the record claims**. LMR
does not merely imply `i_det >= 1` at this cell — **the paper prints the cell, its ambient
multiplicity, and its ideal multiplicity, explicitly**, in §3.2:

> **For example, when `n = 3`, the module with highest weight `12 ω_1 + 5 ω_2 + 2 ω_7` occurs
> with multiplicity six in `S^{12}(S^3 C^9)`, but only one copy of it is in the ideal.**

That single sentence carries all three of the record's claims at once: the weight
`12ω_1 + 5ω_2 + 2ω_7` is the partition `(19,7,2⁵)`; the degree is `12`; the ambient multiplicity
is **six**, which is `lmr_cell.md`'s `a = 6`, "LMR's own value"; and "only one copy of it is in
the ideal" is `i_det = 1` — **stronger than the `i_det >= 1` the record takes from LMR.**

**C45 closes.** The floor is PRIMARY-sourced, from bytes verified identical to the record's own
recorded hash.

**Three things the close carries with it, none of which undoes it:**

1. **Cite Theorem 2.3.1 (with §3.1 and §3.2), never Theorem 1.0.2.** Thm 1.0.2's printed `ω_1`
   coefficient and its printed degree are **both halved** and are mutually inconsistent. The
   record's `equation_census.md` §2.1 spotted this and resolved it correctly; I confirm it and
   sharpen it (§2.5).
2. **The transfer from LMR's `C⁹` to the record's `C⁷` is the programme's own (★), not LMR's.**
   LMR's sentence is about `S^{12}(S^3 C^9)` and `closure(GL_9·[det_3])`. The record's cell is
   `Sym^{12}(Sym^3 C^7)` and `D_7`. The bridge is s73 §1's (★) reduction, valid for `ℓ(λ) <= 7`,
   and here `ℓ(λ) = 7` **exactly at its boundary** (§2.4). This is a record-internal premise that
   was already on the record; naming it is the honest form of the close.
3. **The record leans only on the *proved* half of LMR's sentence, which is the right half.**
   `i_det >= 1` follows from Thm 2.3.1 plus Thm 3.1.1/§3.2's ideal statement, which are proved.
   "Only one copy" (`i_det <= 1`) is **asserted without a printed proof**, and the record does not
   use it — it measures the ceiling instead. That split turns out to be exactly correct (§3.3).

A bonus cross-check fell out. LMR prints multiplicity **six** at `N = 9`; s73 computed `a = 6` at
`N = 7` by three independent engines. The two agree across different variable counts, which is an
independent confirmation of the multiplicity-stability step that `lmr_cell.md` §2 invokes and that
nothing on the record had checked against an external source (§2.4).

---

## 0. What one reading can and cannot establish

**What it can.** It can settle a *read-status*: whether the statement a record sentence leans on
says what the record says it says, in the source, at bytes anyone can re-fetch and re-hash. That
is the whole content of G14/G14′, and it is what was missing.

**What it cannot.** It cannot verify LMR's proof. I read the statements of Thm 2.3.1, Thm 3.1.1
and §3.2 and the construction in §2.3 that produces the weight; I did **not** audit the proofs in
§§2.2–2.3 or §3.3 line by line. PRIMARY means *read at the source*, not *re-derived*. Where LMR
asserts without proof, I say so (§3.3) rather than inheriting the assertion silently.

**It cannot repair the record's own premises.** The `C⁹ → C⁷` transfer (★) is the record's, and a
reading of LMR cannot certify it. §2.4 states it as a named condition rather than absorbing it.

**It cannot make C45's computational half any better.** The `a`-ladder at `δ = 8..40`, the
nullity certificates at `δ = 12..16` and Proposition S are untouched here. Their status is what
B24-02 §2.2(d) left.

---

## 1. The fetch, with bytes verified

| what | URL | sha256 | bytes |
|---|---|---|---|
| **LMR PDF, v1** | `https://arxiv.org/pdf/1004.4802v1` | `cfc28275a8c6b27f0ad6946d495ed4f889f7617df479be943d8d35718dbf2d79` | 180 675 |
| ar5iv rendering | `https://ar5iv.labs.arxiv.org/html/1004.4802` | `fb5844ada6bec339638b584bcf385686935e96e03aa8f0ab9e2561bb0b316e05` | 382 135 |
| tag-stripped text | (derived, `sed`/`tr`) | `b772b08cf3afb69d9122dcfc89956018ae8018d053742513b3bf7a0f5c5d8bcb` | 63 344 |
| arXiv abstract page | `https://arxiv.org/abs/1004.4802` | `dc097e58fa7eeed4adc1f7869a5a737e1b8b0de6ccfb6f0f315fe0042ca473d6` | 39 416 |

**The bytes match the record.** B23-06 recorded `cfc28275a8c6b27f…` for this PDF; the full hash
is in `results/b23_06/MANIFEST.json` @ `feed104e` as
`"https://arxiv.org/pdf/1004.4802v1 (LMR)": "cfc28275a8c6b27f0ad6946d495ed4f889f7617df479be943d8d35718dbf2d79"`.
**My download hashes to exactly that, all 64 hex digits.** The paper is 11 pages, PDF 1.4.

**Note on the record's own citation hygiene.** B23-06's *report* prints only the truncated
`cfc28275a8c6b27f…` (16 hex digits, 64 bits). The full hash survives only in its `MANIFEST.json`.
A truncated hash in prose is fine when the manifest carries the full one, as here — but a reader
of the report alone cannot verify bytes. Noted, not filed as a defect.

**How the text was read, and why not the PDF directly.** PDF page rendering is unavailable on this
host (`pdftoppm` / poppler not installed), so the PDF was hashed but not rendered; the text was
read from the ar5iv HTML, which is the route B23-06 used. **There is no version ambiguity:** the
arXiv abstract page shows a single submission, **`[v1] Tue, 27 Apr 2010`, and no later version**,
so the ar5iv rendering and the hashed PDF are the same and only version. Text extraction used
`sed` and `tr`; hashing used `sha256sum`. **No interpreter was launched in this slot at all.**

The passages relied on are quoted verbatim in `results/b24_02b/lmr_quotes.md` (Q1–Q7), so every
claim below can be checked without re-fetching.

---

## 2. Theorem 2.3.1 as printed, and the three confirmations

### 2.1 The statement (Q1)

> Define `Dual_{k,d,N} ⊂ P(S^d W*)` as the Zariski closure of the set of irreducible hypersurfaces
> of degree `d` in `PW ≃ P^{N−1}`, whose dual variety has dimension at most `k`.
>
> **Theorem 2.3.1.** The variety `Dual_{k,d,N}` has equations given by a copy of the `SL_N`-module
> with highest weight
> `Ω(k,d) = (d−1)(d−2)(k+2) ω_1 + ( d(k+2) − 2k − 5 ) ω_2 + 2 ω_{k+3}`.
> These equations have degree `(k+2)(d−1)`.

**This is verbatim what `equation_census.md` §2.1 says it is**, including the degree
`(k+2)(d−1)`. (The displayed line writes `P(S^n(C^N)*)` where the definition above it uses degree
`d`; an evident typo, not material.)

### 2.2 Confirmation 1 — the module is non-vacuous exactly when `N >= k+3` ✓

The census reads non-vacuity as `N >= ℓ(λ) = k+3`. **Confirmed in the text, and the reason is
printed.** §2.3's construction (Q3) says: *"Recall that `F ⊂ W` is a subspace of dimension
`k+3`"*, and the equation attached to the flag `D ⊂ L ⊂ F` *"must therefore be a highest weight
vector in some module … and its highest weight must be of the form `a ω_1 + b ω_2 + c ω_{k+3}`."*

So `ω_{k+3}` is a fundamental weight of `SL_N` only when `k+3 <= N`, and the subspace `F` exists
only when `k+3 <= N`. At `n = 3` the relevant `k` is `4` (§2.3 below), so the condition is
**`N >= 7`** — and the record's `r = 7` sits **exactly at the pinch**, as `lmr_cell.md` §1 says.
The census's reading is correct.

### 2.3 Confirmation 2 — `D_7` lies in the dual-degenerate locus, at `k = 4` ✓

This was flagged in the brief as the step most likely to hide an unrecorded hypothesis. **It does
not, and in fact LMR states the conclusion directly, so the containment need not be constructed.**

§3.1 (Q4) prints the dual and its dimension: *"The hypersurface in `PW` defined by the determinant
is dual to the variety of rank one matrices, the Segre product `P^{n−1} × P^{n−1} ⊂ P^{N−1}`."*
That has dimension `2n−2`, so at `n = 3` it is **4** — and `k = 2n−2 = 4` is exactly the index
the record uses. `det_3` is irreducible of degree `3`, so `[det_3] ∈ Dual_{4,3,9}` by the
definition in Q1; `Dual` is closed and `GL`-stable, so `closure(GL_9·[det_3]) ⊆ Dual_{4,3,9}` and
therefore `I(Dual_{4,3,9}) ⊆ I(closure(GL_9·[det_3]))`.

**LMR does not leave this to the reader.** §3.2 (Q6) opens with the global statement:

> A copy of the module with highest weight `n(n−1)(n−2) ω_1 + (2n²−4n−1) ω_2 + 2 ω_{2n+1}` in
> `S^{2n(n−1)}(S^n C^{n²})` **is in the ideal of** `closure(GL(W)·[det_n])`.

and §3.1 (Q5), after Thm 3.1.1: *"the `SL(W)`-module of highest weight `Ω(2n−2, n)` … gives local
equations at `[det_n]` of `closure(GL_{n²}·[det_n])`, of degree `2n(n−1)`."*

**So the ideal membership is asserted by the paper for the determinant orbit closure itself, at
`k = 2n−2`.** "Local equations at `[det_n]`" in §3.1 is about Thm 3.1.1's smoothness claim; §3.2's
sentence is global and is the one the record needs. No unrecorded hypothesis appears.

### 2.4 Confirmation 3 — the printed worked instance, `a = 6`, and `i_det = 1` ✓✓

§3.2 (Q6), verbatim:

> **For example, when `n = 3`, the module with highest weight `12 ω_1 + 5 ω_2 + 2 ω_7` occurs with
> multiplicity six in `S^{12}(S^3 C^9)`, but only one copy of it is in the ideal.**

Converting `12ω_1 + 5ω_2 + 2ω_7` to a partition (`λ_j = Σ_{i>=j} c_i`):
`λ_1 = 12+5+2 = 19`, `λ_2 = 5+2 = 7`, `λ_3..λ_7 = 2` — **`λ = (19,7,2⁵)`**, with `|λ| = 36 = 12·3`
matching the printed `S^{12}` ✓. So:

| record claim | source | verdict |
|---|---|---|
| `λ(4,3) = (19,7,2⁵)` at `δ = 12` is "the partition printed in the paper" (`equation_census.md` §2.1) | §3.2 example | **CONFIRMED.** Printed as `12ω_1+5ω_2+2ω_7` in `S^{12}(S^3 C^9)` |
| `a = 6` is "LMR's own value" (`lmr_cell.md` §3b) | §3.2 example | **CONFIRMED.** "occurs with multiplicity six" |
| `i_det(12) >= 1` is "LMR's theorem at this cell" (s73 §2(c)) | §3.2 example + Thm 2.3.1 + Thm 3.1.1 | **CONFIRMED, and exceeded** — LMR prints "only one copy of it is in the ideal", i.e. `i_det = 1` |

**The one thing the record must carry: LMR's sentence is at `N = 9`, the record's cell is at
`N = 7`.** LMR states multiplicity six and one ideal copy in `S^{12}(S^3 C^9)`, for
`closure(GL_9·[det_3])`. The record's cell is `Sym^{12}(Sym^3 C^7)` and `D_7`, the 7-pencil
slice. The transfer is **s73 §1's (★) reduction** — *"by the programme's (★) reduction the
`λ`-isotypic part of `C[GL_9·f]` is that of `C[X_7]` for `ℓ(λ) <= 7`"* — together with
multiplicity stability in the variable count for the ambient `a` (`lmr_cell.md` §2: *"the value
is independent of `N` once `N >= ℓ(λ)`"*). Here `ℓ(λ) = 7`, so both apply **exactly at the
boundary of their stated range**. This is a record-internal premise already on the record; it is
not a new condition, and it is not LMR's. It should be named whenever the LMR citation is used,
and §3.2 does so.

**A cross-check the record did not have.** s73 computed `a = 6` for `S_λ(C^7)` in
`Sym^{12}(Sym^3 C^7)` by three independent engines. LMR prints multiplicity **six** in
`S^{12}(S^3 C^9)`. Different variable counts, independent computations, same number — which
independently corroborates the stability step (`N = 7` vs `N = 9`, both `>= ℓ(λ) = 7`) that
`lmr_cell.md` §2 asserts. Small, but it is a free external check on a step that previously had
none.

### 2.5 The factor of two — `equation_census.md` §2.1 vindicated, and sharpened

The census wrote that *"LMR's printed Theorem 1.0.2 says `n(n−1)`, which would be 12 at `n = 4`
and is inconsistent with the highest weight printed in the same theorem"*, and settled the
pre-registered question as **24, not 12**. **Confirmed.** Working it out at `k = 2n−2, d = n`:

| source | `ω_1` coefficient | degree | internally consistent? |
|---|---|---|---|
| Thm 2.3.1 at `k = 2n−2` (Q1) | `2n(n−1)(n−2)` | `2n(n−1)` | **yes** |
| Thm 3.1.1's following sentence (Q5) | `Ω(2n−2,n)`, i.e. `2n(n−1)(n−2)` | `2n(n−1)` | **yes** |
| §3.2 example at `n = 3` (Q6) | `12 = 2·3·2·1` | `12 = 2·3·2` | **yes** |
| **Thm 1.0.2** (Q7) | `n(n−1)(n−2)` ✗ | `n(n−1)` ✗ | **no** |
| **§3.2 opening sentence** (Q6) | `n(n−1)(n−2)` ✗ | `2n(n−1)` ✓ | **no** |

The arithmetic: a weight `A ω_1 + (2n²−4n−1) ω_2 + 2 ω_{2n+1}` has
`|λ| = A + 2(2n²−4n−1) + 2(2n+1) = A + 4n(n−1)`, and `|λ| = δn` forces `δ = (A + 4n(n−1))/n`.
With `A = 2n(n−1)(n−2)` this gives `δ = 2n(n−1)` ✓. With the printed `A = n(n−1)(n−2)` it gives
`δ = (n−1)(n+2)` — which equals **neither** printed degree (at `n = 3`: `10`, against Thm 1.0.2's
`6` and §3.2's `12`; at `n = 4`: `18`, against `12` and `24`).

**So the `ω_1` coefficient `n(n−1)(n−2)` is the typo** — it should be `2n(n−1)(n−2)` — and
Thm 1.0.2's degree `n(n−1)` is a **second, separate** halving. The same `ω_1` typo recurs in
§3.2's opening sentence, which otherwise has the correct degree `2n(n−1)`. The census reached the
right answer by the right route (deriving `δ` from the weight rather than trusting the printed
degree), and its conclusion `24, not 12` at `n = 4` is correct. I add only that the *weight* is
the corrupted side in Thm 1.0.2, and that the corruption is not confined to Thm 1.0.2.

**Consequence for citation, and it is not cosmetic.** A future reader who cites **Thm 1.0.2** for
this cell gets `6ω_1 + 5ω_2 + 2ω_7` — the partition `(13,7,2⁵)` at degree 6 — which is **not the
record's cell** and is not internally consistent. The correct citation is **Thm 2.3.1**, with
**§3.1's sentence after Thm 3.1.1** for the determinant specialization and **§3.2's example** for
the `n = 3` numbers. `equation_census.md` already cites Thm 2.3.1; `lmr_cell.md` and s73 cite
"LMR" without a theorem number, and §3.2 below fixes that at the point of use.

---

## 3. Outcome, and the label recorded at the point of use

### 3.1 The label

> **LMR = J. M. Landsberg, L. Manivel, N. Ressayre, *Hypersurfaces with degenerate duals and the
> Geometric Complexity Theory Program*, arXiv:1004.4802v1 (27 Apr 2010; v1 is the only version).**
> **Read-status: PRIMARY (G14/G14′).**
> **File:** `https://arxiv.org/pdf/1004.4802v1`, sha256
> `cfc28275a8c6b27f0ad6946d495ed4f889f7617df479be943d8d35718dbf2d79`, 180 675 bytes — the same
> bytes B23-06 recorded.
> **Sections read:** §2.3 (the construction, the definition of `Dual_{k,d,N}`, **Theorem 2.3.1**
> and the scope paragraph following it); §3.1 (the determinant's dual, **Theorem 3.1.1** and the
> sentence after it); §3.2 (the global ideal statement and **the printed `n = 3` example**); §1
> (Theorem 1.0.2, for the factor-of-two record). Text read via the ar5iv rendering, sha256
> `fb5844ada6bec339638b584bcf385686935e96e03aa8f0ab9e2561bb0b316e05`; passages quoted verbatim in
> `results/b24_02b/lmr_quotes.md`.
> **Proofs: not audited** — PRIMARY at the level of the statements read (§0).

### 3.2 The exact record sentences this now attaches to

These are the sentences that were carrying an unlabelled dependency. Each now carries the label
above. **No sealed file is edited by this slot (G13); this table is the record of where the label
attaches.**

| # | file (sha256) | sentence, as written | label now carried |
|---|---|---|---|
| 1 | `equation_census.md` (`ba7b20f9…`) §2.1 | "LMR Theorem 2.3.1 gives the equations of `Dual_{k,d,N}` as a copy of the `SL_N`-module of highest weight `Omega(k,d) = …`" | **PRIMARY**, §2.3 (Q1). Verbatim correct |
| 2 | `equation_census.md` §2.1 | "LMR's own worked instance reproduces exactly — `lambda(4,3) = (19,7,2^5)` at `delta = 12`, `n = 3`, which is the partition printed in the paper." | **PRIMARY**, §3.2 (Q6). Confirmed — printed as `12ω_1+5ω_2+2ω_7` in `S^{12}(S^3 C^9)` |
| 3 | `equation_census.md` census table, row 1 | "LMR dual-degeneracy module, `k = 6` \| LMR Thm 2.3.1 \| **24**" | **PRIMARY**, §2.3 + §3.1 (Q1, Q5). Degree `(k+2)(d−1) = 24` at `n = 4` confirmed |
| 4 | `equation_census.md` §2.1 | "LMR's **printed Theorem 1.0.2 says `n(n-1)`** … inconsistent with the highest weight printed in the same theorem … **24, not 12.**" | **PRIMARY**, §1 (Q7). Confirmed and sharpened (§2.5) |
| 5 | `lmr_cell.md` (`0ab35e4e…`) §3b | "`a = 6` (LMR's own value, reproduced here at inner degree 3)" | **PRIMARY**, §3.2 (Q6): "occurs with multiplicity six". **Carry (★):** LMR's six is at `N = 9` |
| 6 | `lmr_cell.md` §3b | "The LMR module is non-vacuous there, so `i_det ≥ 1`" | **PRIMARY**, Thm 2.3.1 + §3.2 (Q1, Q6). **Carry (★)** |
| 7 | `s73_report.md` (`f40783ba…`) §2(c) | "`i_det(12) ≥ 1` is LMR's theorem at this cell (adopted)" | **PRIMARY**. The theorem is **Thm 2.3.1**, specialized by §3.1 and instanced in §3.2. **Carry (★)** |
| 8 | `s73_report.md` §3, instrument table | "the rigorous `v ∈ I(D_7)` at `δ = 12` is LMR" | **PRIMARY**, §3.2's "is in the ideal" (Q6). **Carry (★)** |
| 9 | `s73_report.md` §8 | "`D = +1` for every `δ ≥ 12` therefore rests on: LMR (literature), …" | **PRIMARY**. The literature dependency is now sourced |
| 10 | `CLAIMS.md` (`2b7ba688…`) C45 | "base `i_det(12) >= 1` from LMR (**read-status for this use not on record, G-15**)" | The parenthesis is **discharged**. Replacement wording in §3.4 |

### 3.3 Which half of LMR's sentence the record uses — and why that matters

§3.2's example makes two claims: *"occurs with multiplicity six"* (`a = 6`) and *"only one copy of
it is in the ideal"* (`i_det = 1`). **Neither is accompanied by a printed proof** in the paper;
they are stated as an example illustrating that the isotypic component is not contained in the
ideal.

What *is* proved is the general statement — Thm 2.3.1 (constructed in §2.3) and Thm 3.1.1, giving
`a copy of the module is in the ideal`, hence **`i_det >= 1`**. And `i_det >= 1` is exactly what
the record takes from LMR: s73 §2(c) takes the **floor** from LMR and the **ceiling**
`i_det <= 1` from its own measured nullity.

**So the record leans only on the proved half, and derives the other half itself.** That is the
correct division, and it was already the record's. It also means the close does **not** depend on
LMR's unproved "only one copy": if that assertion were wrong, `i_det` could only be larger, and
`D = i_det − i_per >= 1 > 0` would still hold. **The positive result is robust to the weakest link
in the citation.** I therefore do **not** recommend rewriting the record to take `i_det = 1` from
LMR; the measured ceiling should stay.

### 3.4 Replacement wording for C45's status cell (for the author; not applied here)

Current: *"base `i_det(12) >= 1` from LMR (read-status for this use not on record, G-15)"*.
Suggested:

> base `i_det(12) >= 1` from **LMR Thm 2.3.1**, specialized at `k = 2n−2` by §3.1 and instanced at
> `n = 3` in §3.2 (multiplicity six, one ideal copy, in `S^{12}(S^3 C^9)`); **PRIMARY**, arXiv
> 1004.4802v1, sha256 `cfc28275a8c6b27f…`, read B24-02b. Transfer to `D_7` is the programme's (★)
> at `ℓ(λ) = 7`. **Do not cite Thm 1.0.2: its printed `ω_1` coefficient and degree are both
> halved.**

**G-15 is closed.** C45's label becomes **PROVED**, with the citation and (★) carried — outcome 1
of the brief's three, with the small qualification of outcome 2 attached, which is (★), a premise
the record already held.

---

## 4. Scope and residue

**Scope of this close.**
- It closes **G-15 / C45's read-status** only. The computational half of C45 (the `a`-ladder at
  `δ = 8..40`, the `δ = 12..16` nullity certificates, Proposition S) is untouched.
- It is PRIMARY **at the level of the statements read**. LMR's proofs in §§2.2–2.3 and §3.3 were
  not audited (§0). Anyone needing the *proof* of Thm 2.3.1 has a further reading to do.
- It certifies nothing about the record's (★) reduction, which is internal and sits exactly at
  `ℓ(λ) = 7`, the boundary of its stated range.

**Scope limits printed in LMR that should travel with any *other* use of these equations** (Q2,
Q5) — none of them threatens `i_det >= 1`, which is ideal membership and is unaffected by how
large the zero set is:
- *"Set theoretically, these equations suffice to define `Dual_{k,d,N}` locally, at least on the
  open subset parametrizing irreducible hypersurfaces."* — local, set-theoretic, and only on the
  irreducible locus.
- *"if `P` is not reduced, then these equations can vanish even if the dual of `P_red` is
  non-degenerate."*
- *"the zero set of the equations is strictly larger than `closure(GL_{n²}·[det_n])`"*, and
  `Dual_{2n−2,n,n²}` **is not irreducible** — it contains the subspace variety of cones, of larger
  dimension than the orbit. LMR: *"We have not yet been able to find equations that separate the
  orbit of `[det_n]` from the other components."*
- *"we did not suppose that `L` was contained in `F`. This indicates that the module generated by
  these equations should in fact be larger than the single module with highest weight `Ω(k,d)`."*
  — this makes the module **larger**, so non-vacuity is preserved a fortiori.

**Residue, OPEN.**
- **(★) at the boundary.** `ℓ(λ) = 7 = r` is the extreme case of "valid for `ℓ(λ) <= 7`". Nothing
  here suggests it fails; it is simply the one step in the chain with no external corroboration.
  The `a = 6` agreement across `N = 7` and `N = 9` (§2.4) is partial corroboration of the
  stability half, not of (★) itself.
- **LMR's "only one copy" is unproved in the paper.** Not used by the record, so not load-bearing
  (§3.3), but it should not be cited as if proved.
- **A truncated hash in B23-06's prose** (§1). Cosmetic; the manifest carries the full one.

**Dimension convention (G24).** Every dimension in this report is the dimension of a **projective**
variety where LMR states it that way (`Dual_{k,d,N} ⊂ P(S^d W*)`; the dual variety of dimension
`2n−2 = 4`; the Segre `P^{n−1} × P^{n−1}`), because those are LMR's own conventions and I am
reporting what the source prints. The multiplicities `a`, `i_det`, `i_per`, `mult_X` are
**affine** dimensions of spaces of highest-weight vectors, as in s73 §1. The two never mix in this
report.

---

## 5. Labelled ledger

Producer-only (G18). Every row is this slot's own work.

| # | statement | label | lineage | where |
|---|---|---|---|---|
| B24-02b.1 | The fetched PDF of arXiv 1004.4802v1 hashes to `cfc28275a8c6b27f0ad6946d…`, identical to the hash `results/b23_06/MANIFEST.json` records; v1 is the only version | **VERIFIED** (bytes) | this slot | §1 |
| B24-02b.2 | LMR Thm 2.3.1 states what `equation_census.md` §2.1 says it states, verbatim, including the degree `(k+2)(d−1)` | **PRIMARY READ** | this slot | §2.1, Q1 |
| B24-02b.3 | Non-vacuity requires `N >= k+3`, because `F ⊂ W` has dimension `k+3` and the weight involves `ω_{k+3}`; at `k = 4` this is `N >= 7`, the pinch | **PRIMARY READ** | this slot | §2.2, Q3 |
| B24-02b.4 | `det_n`'s dual is the Segre, of dimension `2n−2`; at `n = 3`, `k = 4`. LMR states the module is in the ideal of `closure(GL(W)·[det_n])` directly | **PRIMARY READ** | this slot | §2.3, Q4–Q6 |
| B24-02b.5 | `λ = (19,7,2⁵)` at `δ = 12` **is** printed in LMR (§3.2, as `12ω_1+5ω_2+2ω_7` in `S^{12}(S^3 C^9)`) | **PRIMARY READ**; confirms `equation_census.md` §2.1 | this slot | §2.4, Q6 |
| B24-02b.6 | `a = 6` is printed ("multiplicity six"); confirms `lmr_cell.md` §3b's "LMR's own value" | **PRIMARY READ** | this slot | §2.4, Q6 |
| B24-02b.7 | LMR prints `i_det = 1` ("only one copy of it is in the ideal") — stronger than the `>= 1` the record takes | **PRIMARY READ** | this slot | §2.4, Q6 |
| B24-02b.8 | LMR's numbers are at `N = 9`; transfer to the record's `D_7` at `N = 7` is the programme's own (★), at `ℓ(λ) = 7`, the boundary of its range | **FINDING** (a named condition, not a new one) | this slot, against s73 §1 and `lmr_cell.md` §2 | §2.4 |
| B24-02b.9 | s73's `a = 6` at `N = 7` (three engines) agrees with LMR's printed six at `N = 9` — an external cross-check of the stability step | **CORROBORATION** | this slot | §2.4 |
| B24-02b.10 | Thm 1.0.2's printed `ω_1` coefficient **and** degree are both halved and mutually inconsistent; the `ω_1` typo recurs in §3.2's opening sentence; Thm 2.3.1, Thm 3.1.1 and the `n = 3` example are consistent | **PROVED** (arithmetic on the printed weights) + **PRIMARY READ** | this slot; confirms and sharpens `equation_census.md` §2.1 | §2.5, Q1/Q5/Q6/Q7 |
| B24-02b.11 | Citing Thm 1.0.2 for this cell yields `(13,7,2⁵)` at degree 6 — not the record's cell. Cite Thm 2.3.1 + §3.1 + §3.2 | **RULING** | this slot | §2.5, §3.4 |
| B24-02b.12 | LMR's "multiplicity six" and "only one copy" are asserted without printed proof; the record uses only the proved floor, so the close is robust to the weaker assertion | **FINDING** | this slot | §3.3 |
| B24-02b.13 | LMR at the C45 point of use is **PRIMARY** (file, hash, sections named); G-15 discharged; C45 becomes PROVED with citation and (★) carried | **RULING** | this slot | §3.1–3.4 |

**G14/G14′ at the point of use, for this slot.** LMR arXiv:1004.4802v1 — **PRIMARY**, hashed, §§1,
2.3, 3.1, 3.2 read, proofs not audited. No other external source was consulted. The elementary
facts used (converting fundamental weights to partitions; `|λ| = δ·d` for `S^δ(S^d C^N)`; closure
and `GL`-stability of `Dual_{k,d,N}`) are **UNREAD-CLASSICAL**.

---

## 6. Resources and manifest

**Numerical runs: none. Wrapped launches: 0. Interpreter launches: 0.** No `.pid` was produced,
so **negation missing for `b24_02b_`** is reported as a statement about `.gitignore` coverage
rather than an actual ignored receipt: this slot created no receipt to be ignored, and
`results/logs/` was not written to at all. Tools used: `curl`, `sha256sum`, `sed`, `tr`, `grep`,
`wc`, `file`, `git show`, `git rev-parse`, `git status`, `ls`, `find`, `mkdir`, `cat`. **No
Python, no interpreter of any kind** — so G19 is not engaged and there is nothing to disclose
under it.

**One tool call that returned an error and produced nothing**, disclosed rather than left silent:
an attempt to render the PDF for direct reading failed with *"pdftoppm is not installed"*. No
text was extracted from it and no fallback inference was drawn from the failure; the ar5iv route
was used instead (§1).

**Files written by this slot:**

| path | what |
|---|---|
| `docs/b24_02b_report.md` | this report |
| `analysis/b24_02b_seal.sh` | seal step (hashing and listing only; no interpreter) |
| `results/b24_02b/lmr_quotes.md` | the passages read, quoted verbatim (Q1–Q7) |
| `results/b24_02b/MANIFEST.json` | manifest (not self-bound) |
| `results/b24_02b/SEAL_LOG.txt` | seal log (not self-bound) |

The manifest was checked for well-formedness **without an interpreter** (brace and bracket
balance 18/18 and 4/4, no trailing commas, full text inspected), to keep the zero-launch count
above literally true rather than nearly true. `jq` is not installed on this host.

**External sources** are hashed in the manifest but **kept in the scratchpad literature cache, not
the delivery tree** (the convention the Astra packet states and B23-10 followed): the PDF, the
ar5iv HTML, the tag-stripped text and the abstract page, with the sha256 values in §1.

**Nothing else was touched.** B24-02's packet is byte-unchanged (`docs/b24_02_report.md` still
`cf09c536cf1fb4ab65fb97ae538371e151b7e50bfaf5464c97a4120e3b125256`). No `b23_*` or earlier results
directory was written to. No sealed packet was edited; §3.2 and §3.4 record where the label
attaches and what the wording should become, for the author to apply (G13).

**Pinned inputs** bound in `results/b24_02b/MANIFEST.json`: `equation_census.md`, `lmr_cell.md`,
`s73_report.md` (all at `82633a60`), `CLAIMS.md` and `GAPS.md` (at `ce43cdb7`), `b23_06_report.md`
and `results/b23_06/MANIFEST.json` (at `feed104e`, the source of the recorded LMR hash), and
`b23_10_review.md` (at `239dd6e8`).

**G9/G10:** no pin or receipt overwritten. **G16, G21–G23** observed: no cell nominated, no gap
claimed, no sealed packet edited. **G9′: tool memory is not an input** — every fact here is either
quoted from the hashed source or derived in full in the text. (Session memory did hold a note that
local PDF text extraction is unavailable; that note was **re-verified against the host**, which
returned the `pdftoppm` error above, rather than relied on.)
