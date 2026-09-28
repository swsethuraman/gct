# B28-04 — the approved B27-04b edits applied to Papers 2 and 3

Producer: Claude Code (Opus 5.5), 2026-09-28. This is an editorial pass only: **no achievement
level moves**. There was no TeX toolchain, so nothing was compiled. The integrator compiles both
after-states. The binding constraint stands: "No five-row determinant equation is known to be
nonzero on padding."

## 1. Preflight

| check | value | result |
|---|---|---|
| `B28_COMMON.md` raw sha256 | `06799a9e404fc45a0944f7fcae88d8dd5511f7721f704ebe69872dd3061c87b9` | = board |
| `B28-04.md` raw sha256 | `8f2213af031198efa547aa889ab9c0af4a7964001999be64c4e690be8e6d637f` | = board |
| `BATCH28_BOARD.md` raw sha256 | `ba404fd0a2c9686e76701e9f3e84681b7806bca8d198d23127a8c46d77f149b6` | recorded |
| `B27_04B_WORDING_DRAFT.md` raw sha256 | `5d8f40124402c298321450c7ab31c192276655e5767665ec50a29f6f09d38663` | = brief and board |
| `b28-04-p2` HEAD | `65060deaf1c8ceb23026571b2fd23d187bc3e6f2` (= origin) | = brief, worktree clean |
| `b28-04-p3` HEAD | `ff1d4772de09f6c497b2d5c485a5052cef8db820` (= origin) | = brief, worktree clean |
| output paths | `docs/b28_04_report.md`, `results/b28_04/`, `analysis/b28_04_*` | absent before this pass |
| attributes | every target and output path is `-text` (`PAPER2_*.md`, `paper/det4-onset.tex`, `papers/det4-blindness/**`, `docs/b28_*`, `results/b28_*/**`, `analysis/b28_*`) | stored as written, byte for byte |
| line endings before | `paper/det4-onset.tex`: CRLF (1257/1257). `PAPER2_GAPS/CLAIMS/READINESS.md`, `det4-blindness.tex` and P3 `GAPS.md`: LF only | preserved (§3) |

The approval is the author's approval of all six items unchanged, on 2026-09-28, as stated in the
brief and in the board's hash table. I did not see it independently: it is **READ** from the
brief and the board.

## 2. The edits

Method (`analysis/b28_04_apply_edits.py`): the script reads the 25 fenced blocks (12 FIND/REPLACE
pairs and 1 APPEND) **directly from the draft bytes**, after checking its hash. So no FIND or
REPLACE text was retyped. For a CRLF target, each `\n` in the FIND and REPLACE becomes `\r\n`. For an LF
target, the text is used as is. Each FIND is counted in the file's current state, in the
draft's order, and replaced only when the count is exactly 1. Per-step FIND and REPLACE hashes,
counts and byte offsets are in `results/b28_04/apply_record.json`.

Line numbers are at the setup commit (before) and in the after-state (after). A FIND that begins
or ends mid-line (3a, 3c, 3d, 4) replaces only the matched span. The rest of that line is untouched.

| # | item | file | occurrences | before lines | after lines | status |
|---|---|---|---|---|---|---|
| 1 | 1 ("35" gloss, Rem. 6.3(iv)) | P2 `paper/det4-onset.tex` (CRLF) | 1 | L627 | L627–630 | **APPLIED** |
| 2 | 2 (cap-proof clause) | P2 `paper/det4-onset.tex` (CRLF) | 1 | L712–713 | L715–721 | **APPLIED** |
| 3 | 3a (abstract) | P3 `det4-blindness.tex` | 1 | L124–126 | L124–127 | **APPLIED** |
| 4 | 3b (Question 6.5 + paragraph) | P3 `det4-blindness.tex` | 1 | L904–910 | L906–916 | **APPLIED** |
| 5 | 3c (`\prov{OPEN. …}` of Q 6.5) | P3 `det4-blindness.tex` | 1 | L918 (tail of arg. 1) | L924 | **APPLIED** |
| 6 | 3d (G-33, first FIND) | P3 `papers/det4-blindness/GAPS.md` | 1 | L126 | L126 | **APPLIED** |
| 7 | 3d (G-33, second FIND, same row) | P3 `papers/det4-blindness/GAPS.md` | 1 | L126 | L126 | **APPLIED** |
| 8 | 4 (abstract (iv)) | P3 `det4-blindness.tex` | 1 | L118–119 | L118–119 | **APPLIED** |
| 9 | 4 (§6) | P3 `det4-blindness.tex` | 1 | L897–898 | L898–900 | **APPLIED** |
| — | 5 (APPEND Part V) | P2 `PAPER2_GAPS.md` (LF, ends in newline) | n/a | after L259 | L260–265 | **APPLIED** |
| 10 | 6 (§N heading) | P2 `PAPER2_CLAIMS.md` | 1 | L219 | L219 | **APPLIED** |
| 11 | 6 (amendment header) | P2 `PAPER2_READINESS.md` | 1 | L64 | L64 | **APPLIED** |
| 12 | 6 ("stays flagged" line) | P2 `PAPER2_READINESS.md` | 1 | L83 | L83–84 | **APPLIED** |

The APPEND block begins with an empty line, so `PAPER2_GAPS.md` now has one blank line between the
old last line and `## Part V — …`, followed by the block and a final newline.

The draft's approximate locators were "L123–126" for 3a and "L896–898" for Item 4 §6. They differ
by about one line from the lines where the FIND matched. The unique FIND match governs, and the
text matched is the text the draft quotes.

### Registered outcome

| item | outcome |
|---|---|
| 1 | **APPLIED** |
| 2 | **APPLIED** |
| 3a | **APPLIED** |
| 3b | **APPLIED** |
| 3c | **APPLIED** |
| 3d | **APPLIED** (both FIND/REPLACE pairs) |
| 4 | **APPLIED** (both FIND/REPLACE pairs) |
| 5 | **APPLIED** |
| 6 | **APPLIED** (all three FIND/REPLACE pairs) |

No item was STOPPED. Nothing was reworded, reflowed or added beyond the draft's text.

### Observation for the integrator (not acted on)

After 3b, Question 6.5 uses `C` throughout. The unchanged sentences that follow in the same
paragraph ("the $20$ nodes of a generic $\det A$ may converge onto the surface
$\{\ell=0\}\cap C^*$"), and route (a) in the `\prov` block ("$\det A(t)\to\ell\cdot C^*$"),
still say `C^*`. These lines lie outside every FIND, so the approved wording did not cover them
and I did not change them. Whether to harmonise them is the author's call.

## 3. Static checks (receipt `results/b28_04/static_check.txt`)

Script `analysis/b28_04_static_check.py`, adapted from `analysis/b27_04_static_check.py`. It is a
text scan, not a compile. Before is the setup-commit blob and after is the worktree.

| check | P2 before → after | P3 before → after |
|---|---|---|
| brace balance | 0 → 0 | 0 → 0 |
| `$` count (parity) | 1878 → 1894 (even) | 2226 → 2258 (even) |
| duplicated labels | none → none | none → none |
| undefined `\ref`/`\eqref` | none → none | none → none |
| undefined `\cite`/`\lit` keys | none → none | none → none (new `\cite{Paper2}` ×2 and `\cite[Prop.~4.23]{Paper1}` ×2 resolve to existing bibitems) |
| uncited bibitems | none → none | none → none |
| "Claude" outside the acknowledgement | 0 → 0 (1 inside it, unchanged) | 0 → 0 |
| slot labels outside the acknowledgement | 0 → 0; **no new slot labels** | 366 → 370; new kinds exactly `A26-02R`, `B26-01`, `B27-01`, `R27-01`, all inside the Item 3c `\prov` block, as the brief permits |
| `\cm`, `\prov` defined (used by 3c) | n/a | yes, yes |

No bibitems were added.

## 4. Git storage

Every changed and new path is under `-text`. For each staged path, `git hash-object <p>` equals
`git hash-object --no-filters <p>` (recorded at commit time in the final message). Paper 2's TeX
after-state is still 100% CRLF (1265 CRLF / 1265 LF), and every other edited file is still 100% LF.
No LF-to-CRLF rewrite was needed.

## 5. Payload

- Branch `b28-04-p2`: `paper/det4-onset.tex`, `PAPER2_GAPS.md`, `PAPER2_CLAIMS.md`,
  `PAPER2_READINESS.md`, `analysis/b28_04_apply_edits.py`, `analysis/b28_04_static_check.py`,
  `results/b28_04/{apply_record.json, static_check.txt, RESOURCE_RECEIPT.md, paper2.diff,
  paper3.diff, MANIFEST.json}`, `docs/b28_04_report.md`.
- Branch `b28-04-p3`: `papers/det4-blindness/det4-blindness.tex`, `papers/det4-blindness/GAPS.md`,
  `results/b28_04/{paper3.diff, MANIFEST.json}`.

`paper2.diff` and `paper3.diff` are the byte-exact `git diff --no-color` output of each
worktree against its setup commit. `paper2.diff` carries the TeX's CRLF bytes. The appendix below
is the same two diffs with the CR characters removed, for reading.

## Appendix A — exact diff, Paper 2 (`b28-04-p2` vs `65060dea`; CR removed for display)

```diff
diff --git a/PAPER2_CLAIMS.md b/PAPER2_CLAIMS.md
index 4966bcd0..79951413 100644
--- a/PAPER2_CLAIMS.md
+++ b/PAPER2_CLAIMS.md
@@ -216,7 +216,7 @@ Rows A–K above are the unchanged B24-06 table. Label changes in the repaired a
 
 ---
 
-## N. B26-05 current-state amendment (2026-09-22, PROPOSED, UNCOMMITTED, producer-only)
+## N. B26-05 current-state amendment (2026-09-22; proposed by B26-05, applied verbatim by B27-04 @ `f8326974`)
 
 Rows A–M above are kept as written. Sections A–L are B24-06's table at `82633a60`; §M is
 B25-02's. This section records the state of the after-state `paper/det4-onset.tex` at
diff --git a/PAPER2_GAPS.md b/PAPER2_GAPS.md
index 8d59ced0..b1cc9ecb 100644
--- a/PAPER2_GAPS.md
+++ b/PAPER2_GAPS.md
@@ -257,3 +257,9 @@ Parts I–II above are unchanged. Status of the gaps after the B25-02 repair pas
 - **G-P2-02 / G-P2-07** — the `n = 3` control is now PROVED: (★) is proved (B25-10 §2.4). The paper keeps the symbol `(★)` for that premise.
 - **G-P2-19** — **stays flagged.** The `n = 4` sentence now says the `n = 3` case is proved and the `n = 4` case is not yet checked, so the transfer is flagged, not established. B25-10 §2.4's one-paragraph check was **not** attempted.
 - G-P2-17 — still open: no compile on this host either; mechanical checks pass (`results/b25_02/EDITS_SUPPLEMENT_20260922.md`). The integrator compiles the after-state.
+
+## Part V — B27-04 and B28-04 (2026-09-23/24)
+
+- **G-P2-18 — CLOSED.** The smooth-cubic result is stated in general in the TeX (B27-04 @ `f8326974`): `ℓ·C ∉ D₄,₅` for every smooth cubic `C` and every `ℓ ≠ 0`, cited through `Companion2`, scope geometric non-containment only. C1 was closed by the author's ruling of 2026-09-23 on B17-01 @ `01c49022`, B26-01 @ `901b0fe6` and A26-02R @ `b0d2d2e8`. Singular and reducible cubic factors stay open (G-A1).
+- **G-P2-19 — CLOSED.** The `r = 9` flag was removed by B27-04. The quartic `16 → 9` transfer was accepted cross-lineage (B26-04 @ `65736d9f`, B26-10A @ `21816b3c`); the general degree-4 statement by R27-K4 @ `53206b43`; and the any-degree form by B28-03 @ `e0a8041b`. The cap-proof clause now uses the any-degree form (B28-04 item 2). This clears the transfer step only: the LMR copy and the other cap-theorem inputs rest on their own evidence.
+- **Remark 6.3(iv)** gains the fixed/varying-factor gloss on "35" (B26-05 §4.2; B28-04 item 1).
diff --git a/PAPER2_READINESS.md b/PAPER2_READINESS.md
index 06413651..0bed2971 100644
--- a/PAPER2_READINESS.md
+++ b/PAPER2_READINESS.md
@@ -61,7 +61,7 @@ remains PROVED modulo (★); several results are cited only through unlocatable
 material; and the author decisions B14/B16 and the Paper 3 overlap are unresolved. Details:
 `docs/b25_02_report.md`.
 
-**B26-05 current-state amendment (2026-09-22, PROPOSED, UNCOMMITTED, producer-only; the B24-06
+**B26-05 current-state amendment (2026-09-22; proposed by B26-05, applied verbatim by B27-04 @ `f8326974`; the B24-06
 paragraph and the B25-02 update above are kept as written).** The subject is the after-state
 `paper/det4-onset.tex` at `79b68dcf` (raw CRLF sha256 `065f8799…`). **It is still not ready.** No
 readiness is declared here. Five statements in the B25-02 update are now stale:
@@ -80,7 +80,8 @@ in `Companion2` and `Companion3`.
 (e) "the author decisions B14/B16 … are unresolved". B14 and B16 were decided and applied on
 2026-09-22 (PART 17b).
 **What still stands:**
-(1) The `n = 4` sixteen-to-nine transfer **stays flagged** (G-P2-19). B26-04 is checking it, and
+(1) [⟳ 2026-09-24: superseded. The flag was removed by B27-04 and the transfer is accepted; see
+PAPER2_GAPS Part V.] The `n = 4` sixteen-to-nine transfer **stays flagged** (G-P2-19). B26-04 is checking it, and
 nothing from it has been independently accepted. Note also that §2 asserts the length reduction
 (2.1) for `det_4` and `x_0 per_3` without a flag, and the paper uses it at several points. So the
 flag at the length-nine cell is narrower than the paper's own unflagged uses of the same
diff --git a/paper/det4-onset.tex b/paper/det4-onset.tex
index a5ff9ef6..5ab2be7e 100644
--- a/paper/det4-onset.tex
+++ b/paper/det4-onset.tex
@@ -624,7 +624,10 @@ bound, not an arc lower bound.  It is
 This interior count is the content of Theorem~\ref{thm:noncontain}: for the
 fixed factor, the cubics $C$ with $s_5C$ an actual determinant are the
 $3\times3$ determinantal cubics ($29$) and the cubics containing a plane
-($31$) \cite{Companion3}.  With every enumerated exceptional component at most $31$ as well,
+($31$) \cite{Companion3}.  (These are fixed-factor dimensions; letting the linear factor vary
+adds $5-1=4$, giving families $\{\ell\cdot C\}$ of affine dimensions $33$ and $35$, and the
+latter $35$ is not the $35=\dim W$ used here.)  With every enumerated exceptional component at
+most $31$ as well,
 $\dim(\Ddet_5\cap W)\le31<35=\dim W$ holds on the enumerated cone.
 
 \emph{What is not proved} is that the enumeration is complete --- that
@@ -709,8 +712,13 @@ With Step 3, $\dim(\bC[s]/J_F)_{3n-5}\ge\mu_{3n-5}(n)+1$, i.e.\
 $\rank M_{3n-5}(F)\le\mathrm{cap}(n)-1$ on the dense determinantal locus, hence
 on $\Ddet_5$; the minors vanish there.  For smooth $F$ the rank is exactly
 $\mathrm{cap}(n)$, so some minor is a nonzero polynomial; equivariance of the
-Fitting construction makes the span $\GL_5$-stable, and \eqref{eq:lengthred}
-carries it into $I(\cO)$.
+Fitting construction makes the span $\GL_5$-stable, and the length-restriction
+lemma carries it into the ideal of $\overline{\GL_{n^{2}}\cdot\det_n}$: its proof
+(coefficient weights are non-negative, the raising operators beyond the first
+five coordinates kill every restricted coefficient, injective substitutions are
+dense, and complete reducibility holds in characteristic zero) uses nothing about
+the form degree, so it applies verbatim with $(d,N,r)=(n,n^{2},5)$ for every
+$n\ge3$, each highest-weight vector pulling back to a nonzero one.
 \end{proof}
 
 \emph{Measured, both primes, fresh pencils.} The corank of $M_{3n-5}$ on
```

## Appendix B — exact diff, Paper 3 (`b28-04-p3` vs `ff1d4772`)

```diff
diff --git a/papers/det4-blindness/GAPS.md b/papers/det4-blindness/GAPS.md
index 728775a4..4534af0a 100644
--- a/papers/det4-blindness/GAPS.md
+++ b/papers/det4-blindness/GAPS.md
@@ -123,7 +123,7 @@ discrepancy here for a reviewer or producer slot.
 
 | id | gap | draft touches | effect today | who could close it |
 |---|---|---|---|---|
-| **G-33** | **G-A1, the boundary of `D45 ∩ P5`. This is the paper's principal open question.** Theorem 2.1 classifies `closure(D45° ∩ P5)`, the closure of the **actual** determinants in `P5`. A point of `(D45 \ D45°) ∩ P5` is a limit of determinants that is not itself one. **Nothing on the record excludes such a point of the form `l·C*` with `C*` smooth**, and if one exists the right-way corner is gone: a smooth cubic would lie in the lift's projection and no Macaulay-rank threshold could separate. Any component such points form has affine dimension `>= 50 + 39 − 70 = 19`. Two natural invariants fail to exclude it: rank thresholds of `F` run the wrong way on padding (C18, C47), and the 20 nodes of a generic `det A` may converge onto `{l = 0} ∩ C*`, so semicontinuity of the singular locus says nothing. `D45°` is not to be expected closed by default — Landsberg exhibits `P_{Λ,m}` with `dc̄ = m < dc`, limits of determinantal expressions that are not determinantal, which shows the phenomenon is real without placing an instance here. | C36, C37, C34, §6 (Question 6.5), thesis clause (d), §9 item 1 | **The draft states the right-way corner as PROVED on the determinant part only**, and names this as its open question. This is a scope requirement the reviewer imposed, not an option. B17-01-C excludes one specific `F*`, not a family. | Three routes, in increasing strength. **(a)** A boundary description: put every one-parameter degeneration `det A(t) → l·C*` with `A(t)` divergent into normal form (curve selection plus a normal form for linear `4×4` pencils in five variables through the singular-pencil locus `Z`) and show it lands in `T1 ∪ T2`. One theory slot, paragraph-first; it inherits the Eisenbud–Harris C1/C3 conditional status (G-4). **No pilot can close it** — sampled degenerations are only MEASURED. **(b)** A direct proof that `{C : l·C ∈ D45} = D35 ∪ Σ_Π` for fixed `l`. **(c)** A proof that `D45°` is closed; not expected. Source: B23-03 §2.6, L13 @ `3bcad666`; B23-10 §3.3, B23-10.11 @ `239dd6e8`. |
+| **G-33** | **G-A1, the boundary of `D45 ∩ P5`. This is the paper's principal open question.** Theorem 2.1 classifies `closure(D45° ∩ P5)`, the closure of the **actual** determinants in `P5`. A point of `(D45 \ D45°) ∩ P5` is a limit of determinants that is not itself one. **⟳ 2026-09-24: the smooth case is CLOSED.** `l·C ∉ D45` for every smooth cubic `C` and every `l ≠ 0` (B17-01 @ `01c49022`; B26-01 @ `901b0fe6`; A26-02R @ `b0d2d2e8`; author's ruling 2026-09-23), so no boundary point has a smooth cubic factor and the right-way corner cannot be lost there. **What stays open is a boundary point `l·C` with `C` singular, `C ∉ D35`, `C` containing no plane** (reducible `C` lies in `Σ_Π`). B27-01 @ `01f78eb2` (R27-01 @ `51f9d17e`) shows this class is 49-dimensional in the padding parameters and excluded from literal determinants; its closure membership is undecided. (Historical wording: nothing on the record excluded such a point with `C*` smooth.) Any component such points form has affine dimension `>= 50 + 39 − 70 = 19`. Two natural invariants fail to exclude it: rank thresholds of `F` run the wrong way on padding (C18, C47), and the 20 nodes of a generic `det A` may converge onto `{l = 0} ∩ C*`, so semicontinuity of the singular locus says nothing. `D45°` is not to be expected closed by default — Landsberg exhibits `P_{Λ,m}` with `dc̄ = m < dc`, limits of determinantal expressions that are not determinantal, which shows the phenomenon is real without placing an instance here. | C36, C37, C34, §6 (Question 6.5), thesis clause (d), §9 item 1 | **The draft states the right-way corner as PROVED on the determinant part only**, and names this as its open question. This is a scope requirement the reviewer imposed, not an option. B17-01-C excluded one specific `F*`; the general smooth-cubic exclusion is now accepted (above). | Three routes, in increasing strength. **(a)** A boundary description: put every one-parameter degeneration `det A(t) → l·C*` with `A(t)` divergent into normal form (curve selection plus a normal form for linear `4×4` pencils in five variables through the singular-pencil locus `Z`) and show it lands in `T1 ∪ T2`. One theory slot, paragraph-first; it inherits the Eisenbud–Harris C1/C3 conditional status (G-4). **No pilot can close it** — sampled degenerations are only MEASURED. **(b)** A direct proof that `{C : l·C ∈ D45} = D35 ∪ Σ_Π` for fixed `l`. **(c)** A proof that `D45°` is closed; not expected. Source: B23-03 §2.6, L13 @ `3bcad666`; B23-10 §3.3, B23-10.11 @ `239dd6e8`. |
 | **G-34** | **Washout residues.** B23-10 closed C32's second lineage by replay but named two residues it did not close: **Theorem 6's exactness** (`dim D_6^{per_3} = 50`; the replay gives a **floor** only, and a floor is not an exactness statement) and **C33** (`degree8_global`), which is a separate integrator reconciliation of several batch-13 producers and was not reviewed. | C32, C33 | C32 has two lineages; **C33 still has one**, and it is the integrator's reconciliation. The draft labels it as such. | A reviewer slot, or an exact rank at `r = 6`. |
 | **G-37** | **CLOSED 2026-09-22** (B25-05 Lemma R @ `2688efd1`, reviewed B25-10 §2.4 @ `42e7f4ba`): (★), renamed **the length-restriction lemma**, is **PROVED**. It is `isotypic_rank.md` Prop. 5, with its two implicit steps supplied by Lemma R; method READ plus INDEPENDENT hand re-derivation of R1–R6. `D_7` is the pencil closure `X_7` by definition, and only vanishing is used. **C45 is PROVED**; the ladder above `δ = 12` keeps its s73 lineage. *The entry as written on 2026-09-21 follows.* **New 2026-09-21. The label of (★), the record's `N = 9 → 7` isotypic reduction, at `ℓ(λ) = 7`.** s73 §1: "by the programme's (★) reduction the `λ`-isotypic part of `C[GL_9·f]` is that of `C[X_7]` for `ℓ(λ) <= 7`". C45's floor comes from LMR at `N = 9` and reaches the record's `D_7` only through (★). Reviewer B24-10 rules the use at the included endpoint of a **closed** range sound (11.3.3), names the load-bearing step as the transport of the **ideal-copy count** (11.3.5), notes the double pinch (`ℓ = 7`, and `N >= k+3 = 7`; 11.3.4), and **could not settle whether (★) is PROVED or ADOPTED** because s73 was outside its pins (11.3.8). The `a = 6` agreement at `N = 9` and `N = 7` corroborates the ambient multiplicity, not the ideal count (11.3.6). Not the unrelated (★) Bruhat criterion of `stabiliser_reduction.md`. | C45, §8 scope paragraph, §9 item 4 | C45 is **PROVED modulo (★)** in its row, its provenance line, the abstract, the introduction and §8. **This writing slot proves nothing about (★)** and does not wait for or assume B25-05's result. If (★) is PROVED, the qualifier becomes bookkeeping; if ADOPTED, the programme's only positive result rests on an adopted internal reduction as well as an external theorem, and the label must say so. | B25-05 (reading part), then a label update by a writing slot citing its committed packet and review. |
 | **G-35** | **`T3 ⊆ T1`?** B23-03 measures a length-10 singular profile (the Segre-cubic profile, exact `rank M_4 = 60`) at four `T3` points and observes that the Segre cubic is itself determinantal, so `T3` is probably also inside `T1`. **It does not claim this and nothing depends on it.** | C36 (the `T3` clause) | Not stated in the draft beyond `T3 ⊆ T2`, which is PROVED and is all the classification needs. | Nobody need close it. Recorded so that a reader does not mistake the MEASURED profile for a claim. Source: B23-03 §2.3, L5 @ `3bcad666`. |
diff --git a/papers/det4-blindness/det4-blindness.tex b/papers/det4-blindness/det4-blindness.tex
index 9d965016..365f2a74 100644
--- a/papers/det4-blindness/det4-blindness.tex
+++ b/papers/det4-blindness/det4-blindness.tex
@@ -115,15 +115,16 @@ ladder $(m,m+1)$ does not, and the blind zone of the second fundamental form rep
 the frontier of Landsberg--Manivel--Ressayre. At $N=6,7,8$ the kill is now proved for the first
 Koszul differential; for the higher ones it stays open in the range $2\le j\le N-4$. (iv)
 Restricted to padding, the separation problem runs the right way on the cubic factor,
-conditional on the cap theorem (PROVED modulo Kleiman, Dimca and Gulliksen--Neg\aa rd, all
-three ADOPTED inputs). What is missing is a lift to quartics. The
+conditional on the cap theorem, which at $n=3$ is PROVED modulo Kleiman and Dimca, both ADOPTED
+inputs (Gulliksen--Neg\aa rd is not needed at $n=3$ \cite[Prop.~4.23]{Paper1}). What is missing is a lift to quartics. The
 \emph{determinant part} of $\Dff\cap\Pf$ is now classified: it is the union of two irreducible
 families, $\{\ell\cdot C: C\in D_{35}\}$ of affine dimension $33$ and
 $\{\ell\cdot C: C\ \text{contains a plane}\}$ of affine dimension $35$, neither inside the
 other. The cap minors vanish on every cubic through a plane, so the right-way corner survives on
-that part. Whether it survives on the boundary --- a point of $\Dff\cap\Pf$ that is a limit of
-determinants without being one, with smooth cubic factor --- is this paper's named open
-question. We include the evidence
+that part. A boundary point with smooth cubic factor would have destroyed it, and there is none:
+$\ell\cdot C\notin\Dff$ for every smooth cubic $C$ and every $\ell\ne0$ \cite{Paper2}. Whether
+it survives on the remaining boundary --- limits of determinants $\ell\cdot C$ with $C$ singular,
+not determinantal and containing no plane --- is this paper's named open question. We include the evidence
 that the instruments work where there is something to see: the unpadded $n=3$ control, with
 $D=+1$ at every rung $\delta\ge12$: PROVED at $\delta=12$, with the record's length-restriction lemma carrying it from nine
 variables to seven; higher rungs rest on the \texttt{s73} certificates. We also include one worked example of the method: the
@@ -894,8 +895,9 @@ Put the three results together. For a fixed $\ell$, the cubics $C$ with
 $\ell\cdot C\in T_1\cup T_2$ are exactly $D_{35}\cup\Sigma_\Pi$: another factorisation
 $\ell C=\ell'C'$ with $\ell'\ne\ell$ would force $\ell'\mid C$, and then $C$ contains a
 hyperplane. The cap minors lie in $I(D_{35}\cup\Sigma_\Pi)$ --- the $\Sigma_\Pi$ half PROVED
-(Proposition~\ref{prop:capplane}), the $D_{35}$ half carrying the cap theorem's own label,
-PROVED modulo three named ADOPTED inputs (Theorem~\ref{thm:cap}) --- and they are nonzero at
+(Proposition~\ref{prop:capplane}), the $D_{35}$ half carrying the cap theorem's label at $n=3$,
+PROVED modulo Kleiman and Dimca, both ADOPTED (Theorem~\ref{thm:cap}; Gulliksen--Neg\aa rd is
+not needed at $n=3$ \cite[Prop.~4.23]{Paper1}) --- and they are nonzero at
 every smooth cubic. So a Nullstellensatz lift
 has a rank-threshold target, and the right-way corner survives the enlargement of the
 intersection. \emph{On the determinant part of it.}
@@ -903,11 +905,15 @@ intersection. \emph{On the determinant part of it.}
 \begin{question}[G-A1; the boundary]\label{q:boundary}
 Theorem~\ref{thm:classify} classifies $\overline{\Dff^\circ\cap\Pf}$. Is there a point of
 $\Dff\cap\Pf$ outside $T_1\cup T_2$ --- necessarily a limit of determinants that is not itself a
-determinant --- of the form $\ell\cdot C^*$ with $C^*$ smooth?
+determinant --- of the form $\ell\cdot C$ with $C$ singular, $C\notin D_{35}$ and $C$ containing
+no plane?
 \end{question}
-\noindent If there is, the right-way corner is gone: a smooth cubic would lie in the lift's
-projection, and no Macaulay-rank threshold could separate. Nothing on the record excludes such a
-point. Two natural invariants fail to exclude it. Rank thresholds of $F$ run the wrong way on
+\noindent As first posed, with $C$ smooth, the question is answered: there is no such point,
+since $\ell\cdot C\notin\Dff$ for every smooth cubic $C$ and every $\ell\ne0$ \cite{Paper2}. So
+the right-way corner cannot be lost at a smooth cubic factor. A reducible $C$ contains a
+hyperplane and lies in $\Sigma_\Pi$, so the singular irreducible case above is what remains.
+Nothing on the record excludes such a point, and whether the cap minors vanish at one is not
+known. Two natural invariants fail to exclude it. Rank thresholds of $F$ run the wrong way on
 padding (Theorem~\ref{thm:gkzB}); and the $20$ nodes of a generic $\det A$ may converge onto the
 surface $\{\ell=0\}\cap C^*$, so semicontinuity of the singular locus says nothing either. Any
 component such points form has affine dimension at least $50+39-70=19$. Nor is ``$\Dff^\circ$ is
@@ -915,7 +921,7 @@ closed'' to be expected by default: Landsberg exhibits polynomials $P_{\Lambda,m
 $\overline{dc}(P_{\Lambda,m})=m<dc(P_{\Lambda,m})$, limits of determinantal expressions that are
 not themselves determinantal. That shows the phenomenon is real; it does not place an instance in
 $\Dff\cap\Pf$. This is the paper's named open question.
-\prov{OPEN. Three routes would close it, in increasing strength: (a) a normal-form analysis of every one-parameter degeneration $\det A(t)\to\ell\cdot C^*$ with $A(t)$ divergent --- one theory slot, paragraph-first, and \emph{no pilot can close it}, since sampled degenerations are only MEASURED; (b) a direct proof that $\{C:\ell\cdot C\in\Dff\}=D_{35}\cup\Sigma_\Pi$ for fixed $\ell$; (c) a proof that $\Dff^\circ$ is closed, which is not expected. Route (a) inherits the conditional status of the Eisenbud--Harris and Ballico inputs (Theorem~\ref{thm:rhoZ}). B17-01-C excludes one specific $F^*$, not a family}{B23-03 \S2.6 (G-A1), L13 @ \cm{3bcad666}; B23-10 \S3.3, ruling B23-10.11 @ \cm{239dd6e8}; Landsberg \lit{Landsberg13}{PRIMARY, via ar5iv} \S2, as read by B23-10}{producer B23-03 named it; reviewer B23-10 (READ + INDEPENDENT hand) affirmed it as genuinely open, supplied the two failed invariants and the three routes, and required that the ``right-way corner survives'' sentence be scoped to the determinant part}
+\prov{OPEN. Three routes would close it, in increasing strength: (a) a normal-form analysis of every one-parameter degeneration $\det A(t)\to\ell\cdot C^*$ with $A(t)$ divergent --- one theory slot, paragraph-first, and \emph{no pilot can close it}, since sampled degenerations are only MEASURED; (b) a direct proof that $\{C:\ell\cdot C\in\Dff\}=D_{35}\cup\Sigma_\Pi$ for fixed $\ell$; (c) a proof that $\Dff^\circ$ is closed, which is not expected. Route (a) inherits the conditional status of the Eisenbud--Harris and Ballico inputs (Theorem~\ref{thm:rhoZ}). The smooth form of the question is CLOSED: B17-01's general smooth-cubic exclusion @ \cm{01c49022}, reviewed by B26-01 @ \cm{901b0fe6} and cross-lineage by A26-02R @ \cm{b0d2d2e8}, closed by the author's ruling of 2026-09-23. The singular form stated above stays OPEN; B27-01 @ \cm{01f78eb2}, reviewed by R27-01 @ \cm{51f9d17e}, shows that in the padding parameters it is a $49$-dimensional class excluded from literal determinants, with closure membership undecided}{B23-03 \S2.6 (G-A1), L13 @ \cm{3bcad666}; B23-10 \S3.3, ruling B23-10.11 @ \cm{239dd6e8}; Landsberg \lit{Landsberg13}{PRIMARY, via ar5iv} \S2, as read by B23-10}{producer B23-03 named it; reviewer B23-10 (READ + INDEPENDENT hand) affirmed it as genuinely open, supplied the two failed invariants and the three routes, and required that the ``right-way corner survives'' sentence be scoped to the determinant part}
 
 The lift that exists is the Nullstellensatz one, and it is not constructive. The covariant lifts
 are dead by Lemma~\ref{lem:nullcone}(c). This is the precise sense of clause (d) of the thesis.
```
