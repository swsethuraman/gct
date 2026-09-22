# B25-01 — Paper 3: the five edits unblocked by B24-10

**Status: UNCOMMITTED local packet.** Slot B25-01, Batch 25, Claude producer. Worktree
`work/batch15_workers/B23-04`, branch `b23-04-paper3`, baseline HEAD
`f95742aed4dd22d3f04ac1313ce3d78e6e0bc87c` (= the launch pin), `git status --porcelain` empty at
2026-09-21T03:35:28Z. Git read-only throughout. No commit, stage, stash, fetch or branch change. No
computation, no research pilot, no `.pid`, nothing installed. This is a writing slot and **no new
mathematics was done**. Under G29's edits-only exception this report carries before/after bindings
(`results/b25_01/bindings.md`) instead of a full manifest.

## Outcome

**Registered outcome (1): all five edits applied from committed sources, internally consistent,
and statically verified.** No edit was deferred. No source conflict needing a proof was found. One
residue that the edits expose, the label of the record's reduction (★), is recorded as **G-37**. It
is not a blocked edit: the review's ruling says to carry C45 as PROVED modulo (★) until an accepted
update arrives, and that is what the paper now does.

## The five items

Authority for all five: B24-10 @ `ab2f8a40`, closing ledger 11.9.7 ("FIRST: the four Paper 3
edits … plus a fifth edit … C11 → PROVED modulo"), with 11.6.9–11.6.12 and 11.5.10. Line numbers
refer to the after-state of `det4-blindness.tex`. The full table is in `DIFF_NOTES.md` §7.

| # | item | source (commit, section) | claim: old → new status | edited locations |
|---|---|---|---|---|
| 1 | **G-30** row 1 / Astra | B24-02 @ `f8273c3b` §3, §4.2–4.4, ledger B24-02.1–.4; B24-10 §3.4, 11.3.11–.15, 11.6.9 | **C48**: PROVED-kill with K5's Kleiman premise at `N = 5`, `k >= 7` → **PROVED-kill on elementary premises across `N = 5..8`** (K5 discharged). **C24**: PROVED, one lineage → **PROVED, second lineage by INDEPENDENT hand re-derivation, not a code replay, no evaluator**; G-23 closed only to that extent. C18's own label unchanged. "Three negative controls" → **one control at three points**; `D(k) > 0` scoped to `k >= 3`, used for integer `k >= 10` | tex: abstract (ii) L103–105; C18 prov L484; **C48 L515–530**; C23 L567–569, L583; **C24 prov L600**; Table 1 row 1 L698, L719. CLAIMS: C18, C23, C24, C30, C48. GAPS: G-23, G-30 disposition (and *sic* note in the old entry) |
| 2 | **G-31** C45 / LMR | B24-02b @ `5a97317e` §§1–4, `lmr_quotes.md` Q1, Q5–Q7; B24-02 §2.2–2.4; s73 §1 @ `82633a60`; B24-10 §§3.1–3.3, 11.3.1–.10, 11.6.10 | **C45**: PROVED with an unlabelled LMR condition ("CONDITIONAL until read-status settled") → **PROVED modulo (★)**. Floor from LMR **Thm. 2.3.1 with §§3.1–3.2**, PRIMARY; ceiling from the record's own nullity (different evidence); never Thm. 1.0.2; `N = 9 → 7` transport and closed `ℓ(λ) <= 7` range carried. **G-15 CLOSED** as read-status; residue **G-37** (open). B25-05 neither awaited nor assumed | tex: abstract L127–129; §1.3 L214–216; **C45 prov L1025**; §8 closing L1036; §8 scope paragraph L1051–1066; §9 item 4 L1095–1099; bibliography LMR (iii) L1184–1197. CLAIMS: C45. GAPS: G-15, G-37, G-31 disposition. BIB: LMR |
| 3 | **G-32** cap statement sync | onset §0 @ `82633a60` ("proved modulo Kleiman, Dimca and Gulliksen–Negård, all adopted and named"); B24-10 §5.3, 11.5.10, 11.6.11 | every use of the cap theorem now reads **PROVED modulo Kleiman (SECONDARY), Dimca (PRIMARY, statement level), Gulliksen–Negård (SECONDARY), all three ADOPTED inputs**. **G-32 CLOSED**. G-12 stays open (the SECONDARY reads are unchanged) | tex: abstract (iv) L118–119; C34 prov L840; §6.1 L896–898 (and C11, item 5). CLAIMS: C11, C34, cross-check list. GAPS: G-12, G-32 disposition. BIB: Dimca, GN, Kleiman |
| 4 | **G-36** D2′ | B24-05 @ `5c5ba86e` §1.2 (D1, D2, D2′, Remark), §4, M4–M6; B24-10 §§2.1–2.4, 11.2.1–.10, 11.6.12 | new **C51, Corollary 4.5** (was: held in GAPS): PROVED, from D2 **alone**; witness `x^n` named in the statement (`x_1^4 ∈ D45` in the image; `x_{11}^n ∈ Det_n`); "closed" in the hypothesis; D1 only as premise of the `b_F` application; **witness exclusion, not mechanism exclusion**, with the escape route for properties holding at the pure power stated. "Same kind and scope" **withdrawn** | tex: new `\subsection` L422; **C51 L429–442**; paragraphs L444–462. CLAIMS: new row C51, cross-check. GAPS: G-36 disposition, WITHDRAWN note in the old entry |
| 5 | **C11** label | as item 3 | **C11: ADOPTED modulo … → PROVED modulo Kleiman, Dimca, Gulliksen–Negård**, all named ADOPTED inputs with their read-statuses | tex: **C11 prov L353**. CLAIMS: C11, "how to read a row" note. (Completes item 3; not double-counted) |

Numbering: C51 is Corollary 4.5, so sixteen results after it in §4 move by one (C17 → Fact 4.6 …
C49 → Prop. 4.21). CLAIMS.md's draft column was recomputed mechanically. Question 6.5 (G-A1) is
unchanged.

**Preserved, as required:** the determinant-part scoping at all five right-way-corner occurrences
(L123–124, L208, L710, L901, L1076) and Question 6.5 as the principal open question; the cubic-side
`Σ_Π` in `deg f >= onset I(D35 ∪ Σ_Π)` (diff checked: no changed line touches it); "no five-row
determinant equation is **known** to be nonzero on padding" (L96); the author line.

## Occurrence searches

- **Cap label.** Every "ADOPTED" in the tex was checked. The four cap-theorem uses now read PROVED
  modulo (L118, L353, L840, L897). The only remaining "ADOPTED modulo" string is inside C11's
  provenance, describing the superseded label. The other ADOPTED labels (C02, C12, `δ_0`) are
  different claims and are unchanged.
- **LMR Thm. 1.0.2.** Two occurrences, L1055 and L1196, both warnings not to cite it. Thm. 2.3.1
  is cited at C45's provenance, §8 and the bibliography.
- **Stale "uncommitted / pending commit / not cited here".** No remaining occurrence in the tex.
  In CLAIMS/GAPS/BIB/DIFF_NOTES the ones that remain are inside historical passages, each followed by
  a dated disposition.
- **"three negative controls" / "same kind and scope".** Neither phrase is in the tex or in
  CLAIMS as a claim. In GAPS each survives only inside its historical entry, annotated *sic* or
  WITHDRAWN.

## Verification

- **Method: READ.** Each edit was checked against the committed bytes of its packet and against
  B24-10's closing ledger. Nothing was replayed, and no independent evaluation was done.
- **Static source check** (administrative text scan, not a compile and not a mathematical
  computation), in `results/b25_01/static_check.txt`: 51 IDs C01–C51 (50 on a heading, C30 on a
  caption), 0 duplicate, 59 labels with 0 duplicated, 43 refs with 0 undefined, every `\lit` key
  is a `\bibitem` and every `\bibitem` is cited, environments balanced, braces balanced, 61
  provenance lines (58 before), even `$` parity.
- **Compile: NOT done.** No TeX toolchain is installed (pdflatex, latexmk, lualatex, xelatex,
  tectonic and MiKTeX are all absent), and nothing was installed. The historical "not compiled"
  note was checked, not carried: the **baseline** bytes `ab69ccbe…` were compiled by the
  integrator to 22 pages, clean (B24 ledger @ `f55ed57f`; PDF digest `1958bade…` names an
  uncommitted artefact). The after-state has not been compiled.

## Source and read status (this slot's own access)

| source | status for this slot | limits |
|---|---|---|
| B24-10, B24-02, B24-02b (+ `lmr_quotes.md`), B24-05, `onset_conjecture.md`, `s73_report.md` §1, B24 ledger | READ, committed blobs at the pins | s73 read for the (★) sentence only; (★)'s proof status was **not** assessed |
| LMR arXiv:1004.4802v1 | **not read by this slot**; consumed B24-02b's committed PRIMARY reading and verbatim quotations | no local copy of the PDF was found; nothing was fetched |
| Kleiman, Dimca, Gulliksen–Negård | not read; read-statuses carried from the record | — |
| B24-06 Paper 2 files | not read | G-32 closes on B24-10's ruling |

**Tool memory.** One entry was created after the work was finished (`b25-01-paper3-edits-outcome.md` in the auto-memory directory). It records this outcome for later sessions, and no premise here rests on it. The shared auto-memory index gained, during this session, an entry
from another session naming a B25-05 outcome for (★). It is not a committed packet and was
**quarantined**: not used as a premise, and G-37 stays open.

## Resources

Zero research pilots and zero mathematical computation. Two administrative Python text scans
(numbering derivation and the static check; scripts copied into `results/b25_01/`), each under a
second. The compute lease was not taken, because none is needed for a text scan.

## Files

Modified (UNCOMMITTED): `papers/det4-blindness/{det4-blindness.tex, CLAIMS.md, GAPS.md, BIB.md,
DIFF_NOTES.md}`. Created (UNCOMMITTED): `docs/b25_01_report.md`, `results/b25_01/{STATUS.md,
bindings.md, static_check.txt, static_check.py, num.py, FILES.sha256}`. Nothing else was written;
no prior packet and no other paper was touched. None of the new paths is gitignored.

## Completion table

| # | item | applied? | where (primary location) | status change |
|---|---|---|---|---|
| 1 | G-30: row 1 elementary at N=5..8; Astra hand lineage; control count; D(k) range | **APPLIED** | Ruling C48 (L515–530); C24 prov (L600) | C48 → PROVED on elementary premises; C24 second lineage (hand, not replay); G-23 closed to that extent |
| 2 | G-31: C45 PROVED modulo (★), Thm. 2.3.1 §§3.1–3.2 | **APPLIED** | C45 prov (L1025); §8 (L1051–1066) | C45 → PROVED modulo (★); G-15 closed; G-37 opened |
| 3 | G-32: cap statement, abstract/discussion, provenance synced | **APPLIED** | abstract (iv) L118; C34 L840; §6.1 L897 | G-32 closed |
| 4 | G-36: D2′ as its own claim ID, witness named, "closed", D2 alone | **APPLIED** | C51, Cor. 4.5 (L429–462) | new PROVED claim; "same kind" withdrawn |
| 5 | C11: ADOPTED modulo → PROVED modulo | **APPLIED** | C11 prov (L353) | C11 → PROVED modulo three named ADOPTED inputs |

## Remaining readiness blockers (Paper 3)

1. **Delivery.** These after-state bytes are UNCOMMITTED. They need a separately authorised
   explicit-path commit with blob verification against `results/b25_01/bindings.md`, then B25-10's
   review of the delivered packet. Until then nothing here counts as accepted.
2. **Compile.** The after-state has not been typeset. The next session with an installed TeX
   toolchain should compile it and fix typesetting only. The risk is small, since the static
   check is clean and the pass changed only prose, one corollary and one subsection.
3. **G-37, the label of (★).** C45, the only positive result, stays PROVED modulo (★) until an
   accepted, committed B25-05 update, with review, settles it. Then it needs a one-row label edit.
4. **Standing labelled dependencies**, not blockers to correctness, since each is labelled at its
   point of use: G-12 (Kleiman and Gulliksen–Negård read only secondarily); G-4 (Ballico unread,
   C28 CONDITIONAL); G-9 (T2, C20 CONDITIONAL); G-11 (Fulton, C06 CONDITIONAL); G-25 (incomplete
   bibliographic data, to be filled from sources); G-33/G-A1 (the paper's named open question,
   which gates nothing, B24-10 11.6.6).
5. **Circulation** is a separate user decision. The draft's `\date` still says "Not for
   circulation".

**Single next required certificate:** a verified delivery commit of the twelve explicit paths
above, whose committed blobs match the predicted blob ids in `results/b25_01/bindings.md`.
