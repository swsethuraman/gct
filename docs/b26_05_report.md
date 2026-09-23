# B26-05 — Paper readiness records and the Paper 2/3 overlap

**UNCOMMITTED / PRODUCER ONLY.** Claude Code, default permission mode. Editorial and readiness
work only. No paper or metadata file was edited; every proposed change is under
`results/b26_05/proposed/`. **No paper is declared ready.**

Achievement level: **none of the four** (source condition, coefficient equation, separation on
padding, positive multiplicity gap). This slot produces records and advice, not mathematics.

---

## 0. Preflight and bindings

| item | value |
|---|---|
| UTC start | 2026-09-22T23:43:46Z |
| `B26_COMMON.md` raw sha256 | `a22c91034244d48aae2be5c9f5ecb4337cff609cda1aaf08e593e497656a51fd` (equals the adoption table in `LAUNCH_PROTOCOL_B26.md`) |
| `B26-05.md` raw sha256 | `4cd1b28fa883af5029a9c9e7a17c4ff480cde19f85bcb38d2f542926b49e6bfc` (equals the adoption table) |
| `BATCH26_LIVE_LEDGER.md` raw sha256 | `9d24c37c5953c66583f199af3e8fc226e4feb9f7c70d412f2d4424594b47d2c8` (read for its hash only) |
| worktree / branch | `work/batch15_workers/B24-06` / `b24-06-paper2` |
| HEAD | `79b68dcf7597e3b0efa63984327ad9f34e5bf74d`, which is the expected value. It equals `origin/b24-06-paper2` in the local ref store; no fetch was run. |
| `git status --porcelain` at start | empty |
| output paths at start | `docs/b26_05_report.md` and `results/b26_05/` absent, so no collision |
| `AGENTS.md` / `CLAUDE.md` | none in the worktree or in the project root |
| other input pins | `0a8029bb` = `b23-04-paper3` tip; `848e22b4` = `b23-05-paper1` tip; both equal their `origin/` refs |
| build evidence | `build_evidence_20260922_close/SHA256SUMS.txt` raw sha256 `c4c56d0d3c09122c4be1d347933a1b77678f55cae7823a9a6eb37665eed2680b` (the brief's value). `sha256sum -c` passes for all 12 entries. **Nothing was recompiled.** |

Everything matched the brief. Nothing had to be stopped.

### 0.1 Input bytes (which bytes each hash names)

| input | commit:path | git blob | raw sha256 of the blob | byte form |
|---|---|---|---|---|
| Paper 3 source | `0a8029bb:papers/det4-blindness/det4-blindness.tex` | `8ff59649…` | `d7d92249…` | LF (raw = blob) |
| Paper 3 claims | `0a8029bb:papers/det4-blindness/CLAIMS.md` | `55a57ea3…` | `23744c6a…` | LF |
| Paper 3 gaps | `0a8029bb:papers/det4-blindness/GAPS.md` | `bc63e29a…` | `23104bfd…` | LF |
| Paper 2 source | `79b68dcf:paper/det4-onset.tex` | `60bc18a4…` | `065f8799…` | **CRLF with `-text`**, so the blob bytes are the raw CRLF bytes; LF rendering `c265937d…` |
| Paper 2 claims | `79b68dcf:PAPER2_CLAIMS.md` | `d33b1a45…` | `6a2b5252…` | LF (`-text`) |
| Paper 2 readiness | `79b68dcf:PAPER2_READINESS.md` | `db878a30…` | `9de8d41f…` | LF (`-text`) |
| Paper 2 blockers | `79b68dcf:PAPER2_BLOCKERS.md` | `b42215a1…` | `ee34b373…` | LF |
| Paper 2 gaps | `79b68dcf:PAPER2_GAPS.md` | `8d59ced0…` | `9fa78279…` | LF |
| Paper 1 source | `848e22b4:paper/det3-conductor.tex` | `7988a8a2…` | `4e1ccf70…` | **LF blob**; CRLF working copy `fada5f7c…` (per the build note; not re-hashed from B23-05's working tree) |
| Paper 1 readiness | `848e22b4:READINESS.md` | `ff74494e…` | `9d82b251…` | LF blob (attribute `text` unspecified, `core.autocrlf=true`, so the working copy is CRLF) |
| Paper 1 gaps | `848e22b4:GAPS.md` | `d4369976…` | `b1b8d4c7…` | LF blob |
| Governing ruling | `42e7f4ba:docs/b25_10_review.md` | `e29797e6…` | `0488ce1e…` | LF |
| PART 17 records | `79b68dcf:results/b25_02/EDITS_SUPPLEMENT_20260922.md`; `848e22b4:results/b25_03/SIGNATURE_SUPPLEMENT_20260922.md` | — | — | read only |

All inputs were read from committed blobs with `git show`. Full sha256 values are in
`results/b26_05/source_ledger.json`.

---

## 1. Readiness table (paper × item × current state × evidence × owner)

States are as of the three after-states. "Owner" is who acts next; "author" includes the user's
circulation decisions.

### Paper 1 — `det3-conductor.tex` @ `848e22b4`

| item | current state | evidence (label) | owner |
|---|---|---|---|
| Attribution signature (G-P1) | **APPLIED**: Form A at Cor. 4.2; the §6 intro wording; no admissible-family phrase | commit `848e22b4`; `SIGNATURE_SUPPLEMENT_20260922.md` (READ). Blob grep: `Cor.~7.2]{BI}` ×3, "no family of" ×2, "no admissible family" ×0 (READ) | done |
| B16 acknowledgement | **REPLACED**; byline `\author{Swami Sethuraman}` unchanged (L40) | source L2002–2006 (READ) | done |
| Compile of the signed bytes | **DONE by the integrator**: 0 errors, 0 undefined refs/cites, 27 pp | `BUILD_NOTE.md`; `SHA256SUMS.txt` verified (READ; PDF and log uncommitted) | done |
| G-P4 (Kumar citation, Rem. 4.14) | **OPEN** | `GAPS.md` G-P4 (READ) | **B26-03** (not anticipated) |
| Read-status of IK / Kumar-Compositio / Hüttenhain | **OPEN**: B24-01 readings, not packeted | `GAPS.md` header (iii); B25-10 §5 (READ) | **B26-03** |
| `READINESS.md` headline, "not applied", "pdflatex still owed", "not compiled" | **STALE** | `READINESS.md` L39–68, L156–167 (READ) | delivery pass; amendment proposed (§2.3) |
| G-P5, G-P2/G-P3 framing, MSC and arXiv categories, LMR journal metadata | author decisions, unchanged | `READINESS.md` (READ) | author |
| G-A1–G-A6 (open mathematics the paper states as open) | unchanged | `GAPS.md` §A (READ) | — |
| Submission placeholders in its own source | **none** (no `XXXX`, no "to be inserted") | grep (READ) | — |

### Paper 2 — `det4-onset.tex` @ `79b68dcf`

| item | current state | evidence (label) | owner |
|---|---|---|---|
| `n = 3` control, `(19,7,2^5)`, `δ = 12`, `Δ = +1` | **PROVED in the TeX** (L1003, L1020–1021); the metadata still says "PROVED modulo (★)" | B25-10 §2.4, §10 (READ); PART 17b item (ii) (READ) | delivery pass; amendments proposed (§2.1, §2.2) |
| Terminology `(⋆)` → "the length-restriction lemma" | **3 occurrences remain** (L1003, L1020, L1061) | source (READ); §3 | author and edits pass; diff proposed |
| `n = 4` sixteen-to-nine transfer | **FLAGGED**, and it stays flagged | L1058–1063 (READ); G-P2-19; B25-10 §2.4 last bullet | **B26-04**, then independent review; flag kept |
| Scope of that flag against §2's eq. (2.1) | **observation**: (2.1) is asserted for `det_4` and `x_0 per_3` without a flag and used throughout (§5) | L254–259, L705–706, L860–861 (READ) | author, and B26-04's reviewer |
| Closure `R_5 ⊄ D^det_5` | ADOPTED, worded as B25-10 §4.3 asks, one-witness reading only | L533–545 (READ) | author: `Companion2` must contain the `s_5·C*` witness |
| Cap theorem label | PROVED modulo Kleiman (SECONDARY), Dimca (PRIMARY, statement level), GN (SECONDARY), all adopted; **agrees with Paper 3** | L68–71, L180–181, L653–655 (READ) | — |
| Compile | **DONE by the integrator**: 0 errors, 15 pp | build evidence (READ) | done |
| G-P2-SUB placeholders | **3 open** (§3.3) | L1197–1207 (READ) | author, at submission |
| Paper 2/3 overlap | advice given (§4); **no contradiction found** | §4 | author |
| Metadata staleness | `PAPER2_CLAIMS.md` §M J1, §L; `PAPER2_READINESS.md` B25-02 paragraph; also `PAPER2_BLOCKERS.md` §4's last line "uncompiled" (outside this brief's list, not amended) | READ | delivery pass; amendments proposed for the two named files |
| B25-02 outcome-(2) items (`b25_02_report.md` §6) | not re-assessed | — | — |

### Paper 3 — `det4-blindness.tex` @ `0a8029bb` (the reference usage; reported, nothing proposed for its files)

| item | current state | evidence (label) | owner |
|---|---|---|---|
| C45 label | PROVED; the provenance splits `δ = 12` (B25-10) from the rungs above (s73 lineage) correctly | L1025 provenance; `CLAIMS.md` C45 (READ) | — |
| C45 summary sentences | the abstract (L127–129), §1 (L214–216) and §8 (L1035–1036) say "`D = +1` at every rung … PROVED" **without the lineage split** | READ | author (wording; §4 row 8) |
| Compile | **DONE by the integrator**: 0 errors, 24 pp. Stale: the header comment L16–18, `GAPS.md` P-1 and `CLAIMS.md` cross-check 1 still say the B25-01 bytes are uncompiled | build note (READ) | editing pass |
| `\date` | reads "Not for circulation" (L76–80) | READ | user (circulation) |
| `Paper1` bibitem / C12 | no locator; C12 marks Paper 1 "UNREAD per the ledger", though Paper 1 is committed with the bracket at L1277–1299 | READ | author / record |
| G-A1 (Question 6.5) | OPEN | READ | — |

---

## 2. Task 1 — stale records: proposed current-state amendments

All three are **appends**. The historical text is preserved byte for byte. Each was checked with
`git apply --check` against the committed blob (`core.autocrlf=false`). All three blobs are LF.

| file | append text | diff | blob before (raw sha256) | after (raw sha256, if applied) |
|---|---|---|---|---|
| `PAPER2_CLAIMS.md` @ `79b68dcf` | `proposed/PAPER2_CLAIMS.append.md` (new §N) | `proposed/PAPER2_CLAIMS.append.diff` | `6a2b5252…` | `fcf67074…` |
| `PAPER2_READINESS.md` @ `79b68dcf` | `proposed/PAPER2_READINESS.append.md` (new paragraph) | `proposed/PAPER2_READINESS.append.diff` | `9de8d41f…` | `bc2f4883…` |
| Paper 1 `READINESS.md` @ `848e22b4` | `proposed/PAPER1_READINESS.append.md` (new section) | `proposed/PAPER1_READINESS.append.diff` | `9d82b251…` | `e9809f41…` |

### 2.1 and 2.2 — Paper 2's claims and readiness files

What the amendments record:

- **C45 `δ = 12` ruling, recorded on its own.** The unpadded `n = 3` cell `(19,7,2^5)`,
  `δ = 12`, `D = +1` is **PROVED** (B25-10 §2.4 @ `42e7f4ba`, READ). §M's "PROVED modulo (★)" is
  superseded. The TeX already reflects this.
- **Higher rungs, recorded separately.** Any rung `δ > 12` keeps its **s73 lineage** (Prop. S,
  Lemma L). Paper 2 claims no rung above 12. Paper 3 does, and that is where the distinction has
  to be carried.
- **The `n = 4` transfer flag is kept.** B26-04 has not been independently accepted, and the
  amendments neither anticipate nor cite it. No B26-03 or Astra result is used.
- **Two objects named "(★)".** In `PAPER2_CLAIMS.md`, row E1's (★) is the **reducible
  criterion** (Thm 5.1, TeX label `thm:star`). §M row J1's (★) is the **length-restriction
  lemma**. Only the latter is renamed.
- **Compile and headers.** The "not compiled" statements are superseded by the integrator's
  build. The provenance headers are marked historical.
- **Readiness.** The readiness paragraph lists what still stands, and says **not ready**.

### 2.3 Paper 1's readiness file

Of B25-03's four items, two are now done: the signature (APPLIED at `848e22b4`) and the compile of
the signed bytes (integrator build). The other two are **OPEN and owned by B26-03**: G-P4, and
the IK / Kumar / Hüttenhain read-statuses. The amendment lists the three stale lines it leaves in
place and restates the unchanged author decisions. It says **not ready**.

---

## 3. Tasks 2 and 3 — terminology and placeholders

### 3.1 Every `(⋆)` in Paper 2 that should become "the length-restriction lemma"

A search of the LF rendering finds exactly **three** occurrences of `\star`, and no `★`,
`\bigstar` or `(*)`. All three denote the `N = 9 → 7` isotypic restriction, which is Paper 3's
"length-restriction lemma".

| line (LF rendering) | current text | proposed text |
|---|---|---|
| L1003 | "proved; its one premise beyond the measurements, `$(\star)$` below, is itself proved." | "…, the length-restriction lemma below, is itself proved." |
| L1019–1020 | "…used here at its boundary `$\ell(\lambda)=7$`; call it `$(\star)$`.  It is not a statement of \cite{LMR};" | "…at its boundary `$\ell(\lambda)=7$`; this is the programme's length-restriction lemma.  It is not a statement of \cite{LMR};" |
| L1061–1062 | "That transfer is the `$n=4$` analogue of the premise `$(\star)$` of the `$n=3$` control above: the `$n=3$` case is proved; the `$n=4$` case is not yet checked, so this transfer is flagged, not established." | "That transfer is the `$n=4$` analogue of the length-restriction lemma used in the `$n=3$` control above: …" **The flag clause is unchanged, word for word.** |

The diffs are `proposed/paper2_length_restriction_rename.CRLF.diff`, which is the form to apply to
the `-text` CRLF blob and passes `git apply --check` against `065f8799…`, and
`paper2_length_restriction_rename.LF.diff`, a readable LF rendering. If applied, the result would
be raw CRLF `c5a64f3f…` (1,247 lines, all CRLF) and LF rendering `b0431395…`, with no `\star`
left.

**Not renamed:** the key `thm:star` at L172, L429 and L449. It is Theorem 5.1, the reducible
criterion, a different object, and it prints as "5.1". The key itself never renders. Renaming it
(for example to `thm:reducible`) would be cosmetic, and that is the author's call.

The wording follows Paper 3, which says "the record's length-restriction lemma" (L128), "the
programme's own length-restriction lemma" (L1057) and "The length-restriction lemma" (L1025).

### 3.2 A consequence of the rename, reported rather than proposed

After the rename, Paper 2 would name the premise without saying where it lives. Paper 3 cites
`isotypic_rank.md` Prop. 5 with B25-05 Lemma R. Paper 2 cites nothing for it and says only
"proved in this programme". Whether to add a locator, such as `Companion2`/`Companion3` or a
Paper 3 citation, is an author decision (§6). Adding one would be a content change, not a rename.

### 3.3 G-P2-SUB placeholders, as they stand (report only)

| where (LF line) | bibitem | placeholder | cited |
|---|---|---|---|
| L1197–1199 | `Companion` = Paper 1, *Conductors of orbit closures, and the fundamental invariant of the 3×3 determinant* | "arXiv preprint, 2026, arXiv:XXXX.XXXXX [identifier to be inserted at submission]" | 9× |
| L1201–1203 | `Companion2`, *Singular matrix spaces and the length-five non-containment*, technical report | "PDF at [repository URL to be inserted at submission]" | 2× (L530, L541) |
| L1205–1207 | `Companion3`, *`D_{45}∩P_5` classified up to its boundary, and the rank thresholds at `N=6,7,8`*, technical report | "PDF at [repository URL to be inserted at submission]" | 3× (L622, L631, L720) |

Context for the author, as facts only:
- Paper 2's own Data availability (L1175–1177) already prints `https://github.com/swsethuraman/gct`,
  as does Paper 1 (L1997).
- Paper 1's source has no placeholders.
- Paper 3's `Paper1` bibitem (L1204–1206) has no locator. It will need the same arXiv identifier
  when Paper 3 is submitted.

---

## 4. Task 4 — the overlap map (advice only)

The map was built from the current source bytes of all three papers, read in full for Papers 2
and 3 and at the shared passages of Paper 1.

**Contradictions: none found.** No shared statement is asserted with incompatible content in two
papers. What exists is duplication, **label discrepancies**, one **scope compression**, one
**numeral that reads as a contradiction but is not one**, and **no cross-reference between Paper 2
and Paper 3 in either direction**. Paper 2 cites Paper 1, `Companion2` and `Companion3`. Paper 3
cites Paper 1. Neither cites the other.

### 4.1 Label and scope discrepancies (listed first, as the nearest things to a contradiction)

1. **The dimension of `D_6^{per_3}` (50), and so `dim P_6 = 55`.**
   - Paper 2 proves exactness: Lemma 3.3 gives the upper bound `9r − 4`, and a Jacobian rank of
     50 at an explicit point gives the lower bound. This is used in Prop. 2.1 and Cor. 3.2
     (L270–271, L310–333).
   - Paper 3 C32's provenance lists "Theorem 6's exactness (`dim D_6^{per_3} = 50`; the replay
     gives a floor only)" among the **"Residues still OPEN"** (L810). Its C02 carries
     `dim P_L = 10L − 5` for `L ≥ 6` as "MEASURED and PROVED".
   - Paper 3's residue is a **review-lineage** residue: the reviewer's replay is a floor. It is
     not a claim that the value differs. Still, a reader sees "OPEN" in one paper against a
     printed proof in the other.
   - *Advice:* have Paper 3's C32 say what is open (independent review of the upper bound) and
     point to Paper 2 Lemma 3.3. Paper 2 unchanged. (Hand check only: `9·6 − 4 = 50`, and
     `6 + 50 − 1 = 55` equals `10·6 − 5`.)
2. **`P_5 = R_5` (the washout at `r = 5`).**
   - Paper 2 Thm 3.1: **proved**, with proof (L288–308).
   - Paper 3 C32 (Record 5.3): PROVED, the same fact for `r ≤ 5`.
   - Paper 3 C02 (Record 2.2): "`P5 = R135` … (**ADOPTED**)", sourced to B22-02 §0.
   - So one paper carries the same fact with two labels, and a third label sits in Paper 2.
     ADOPTED is weaker, so nothing is false.
   - *Advice:* point Paper 3's C02 at C32 and at Paper 2 Thm 3.1. Whether the label itself moves
     is a record decision under G26 (§6).
3. **Paper 3's ladder summaries.**
   - The abstract (L127–129), §1 (L214–216) and §8 (L1035–1036) say "`D = +1` at every rung
     `δ ≥ 12`, PROVED".
   - B25-10 §2.4 scopes the upgrade to `δ = 12`. The rungs above keep their s73 lineage
     (Prop. S, Lemma L; producer only), and Paper 3's own C45 provenance says so (L1025).
   - The summaries compress that split.
   - Paper 2 claims only `δ = 12`, so the two papers do **not** contradict each other.
   - *Advice:* add "(base rung reviewed; higher rungs on the s73 lineage)" or similar to the
     three summaries. I did not read s73, and the s73 label of the higher rungs is taken from
     Paper 3's `CLAIMS.md`, not verified.
4. **The cap theorem at `n = 3`.**
   - Paper 3 C34 conditions the right-way cubic clause on "the cap theorem at `n = 3`, PROVED
     modulo Kleiman, Dimca and Gulliksen–Negård".
   - Paper 1 Prop. 4.23 proves the `n = 3` case using Kleiman and Dimca only (L1250–1269): Step 3
     is "six points impose at most five conditions on linear forms". Paper 2 says the same at
     L693–695.
   - Paper 3's condition is therefore **more conservative** than it needs to be. It is not wrong.
   - *Advice:* optional narrowing, with a citation of Paper 1 Prop. 4.23. Author and record
     decision.
5. **`δ_0`.**
   - All three papers agree on `6 ≤ δ_0 ≤ 65` unconditionally and `8 ≤ δ_0 ≤ 65` given the
     measured totals: Paper 1 at L1296–1298, Paper 2 at L197–200, Paper 3 C12.
   - Paper 3 C12 still labels its source "paper 1 … UNREAD per the ledger", while Paper 1 is
     committed and states the bracket with its argument.
   - *Advice:* Paper 3 cites Paper 1 §4 directly after a reading pass. The label is not changed
     here.

### 4.2 A numeral that reads as a contradiction but is not one

**"35".**
- Paper 2 Thm 6.2 and Rem. 6.3: "`dim ≤ 31 < 35 = dim W`". Here `W = s_5·Sym^3 C^5` has the
  factor **fixed**.
- Paper 3 C35: "`dim T_2 = 35` affine". Here `T_2 = {ℓ·C : C ∈ Σ_Π}` has `ℓ` **varying**.
- Both are right. By hand: with `ℓ` varying, `dim = dim(cubic family) + 5 − 1`, which gives
  `29 → 33` and `31 → 35`.
- *Advice:* a half-sentence in Paper 2 Rem. 6.3(iv) ("for a fixed factor; with the factor
  varying these are 33 and 35, as in Paper 3") prevents a referee from reading "35 < 35".

### 4.3 The map

"Proves" means the paper prints a proof or proof sketch. "States" means a statement with a
citation or provenance only.

| # | shared statement | proves | repeats | relation | where a cross-reference would do |
|---|---|---|---|---|---|
| 1 | Washout: `P_r = R_r` for `r ≤ 5`; `per_3` first visible at length 6 | **Paper 2** Thm 3.1, Cor. 3.2 | Paper 3 C32 (statement, PROVED); C02 (ADOPTED, at `r = 5`) | duplication + label discrepancy (§4.1 item 2) | Paper 3 C02/C32 → Paper 2 Thm 3.1 |
| 2 | `dim D^det_5 = 50`, `dim R_5 = 39` (affine); `dim D35 = 29` | Paper 2 Prop. 2.1 + Lemma 3.3 (the stabiliser bound) | Paper 3 C01, C03 (from the record, with affine/projective stated) | duplication; consistent. Paper 2 never writes "affine" | Paper 2 could add "affine"; either may cite the other |
| 3 | `dim D_6^{per_3} = 50`, `dim P_6 = 55` | Paper 2 (Lemma 3.3 + Jacobian rank) | Paper 3 C02 (`10L − 5`), C32 residue "OPEN" | label discrepancy (§4.1 item 1) | Paper 3 C32 → Paper 2 Lemma 3.3 |
| 4 | Degree-eight silence: `I(D_r^{per_3})_δ = 0` for all `r`, `δ ≤ 8` | neither (the record's reconciliation) | Paper 2 §1 (L151–158), Q 10.5; Paper 3 C33 | agreement | either |
| 5 | Cap theorem `cap(n) = 5n(n−1)²(7n−8)/12` | **Paper 2** Thm 7.1, four-step proof; `n = 3` case also **Paper 1** Prop. 4.23 | Paper 3 C11 (statement, same label) | agreement on the label (B25-10 §6); §4.1 item 4 at `n = 3` | Paper 3 C11 → Paper 2 Thm 7.1 (and Paper 1 Prop. 4.23 for `n = 3`) |
| 6 | Cap minors vanish on every cubic through a plane; generic rank 64 | Paper 2 §7 paragraph (sketch, cites `Companion3`); Paper 3 C37 (proof in provenance) | — | duplication with two sketches; consistent (31 > 29) | one of them cites the other |
| 7 | Determinant part of `D45 ∩ P5`: for a fixed factor the cubic is `3×3` determinantal (29) or contains a plane (31) | **Paper 2** Thm 6.2 (via the singular-subspace classification, `Companion2`); **Paper 3** Thm 6.3/C36 (B23-03's case analysis, a different proof, and more: irreducibility, `T_1 ⊄ T_2`, `T_3 ⊆ T_2`) | Paper 2 Rem. 6.3(iv) restates via `Companion3` | **two proofs of overlapping statements**; consistent; the "35" note (§4.2) | Paper 2 Thm 6.2 → Paper 3 Thm 6.3 for the full classification |
| 8 | Boundary / closure (G-A1) | neither | Paper 2: closure non-containment ADOPTED via one smooth witness (L538–542); Paper 3 Q 6.5: OPEN; "B17-01-C excludes one specific `F*`, not a family" | agreement on the narrow reading (B25-10 §6). B17-01's general form is used by neither | Paper 2 L631 → Paper 3 Q 6.5 |
| 9 | `n = 3` positive control, `(19,7,2^5)`, `δ = 12`, `Δ = +1` | **both**: Paper 2 §9 (~45 lines: LMR floor, measured ceiling, length-restriction transport); Paper 3 Thm 8.1/C45 and the scope paragraph | — | **duplication of the argument**. Labels agree at `δ = 12`; terminology differs (§3.1); Paper 3 also states the ladder (§4.1 item 3) | one paper carries it and the other cites it (§4.4) |
| 10 | The padded `n = 3` cell is degenerate | Paper 2 (L1037–1042: `per_2 ~ det_2`, block split, `Δ ≤ 0`); Paper 3 C46 (`ℓ·per_2` has five essential variables, gap `−5`) | — | two different arguments; compatible (`−5 ≤ 0`) | either |
| 11 | `n = 3` twin: `D^det_5 = closure of cubics singular at a frame`; a component of the six-nodal locus | **Paper 2** Thm 7.3 (sketch) | **Paper 1** Q 8.5 (the same argument sketched; Paper 2 L766–767 already says so) | duplication, already cross-referenced | none needed |
| 12 | Length reduction: multiplicities of the orbit closure = those of the pencil closure at `ℓ(λ) = r` | **Paper 1** Prop. 4.19 (`det_3`); Paper 3's length-restriction lemma (C45, `N = 9 → 7`, `det_3`) | Paper 2 eq. (2.1): "applies verbatim to `det_4` and `x_0 per_3`", citing Paper 1 | Paper 2 extends it to `n = 4` without a flag in §2 and flags it at L1061 (§5) | — |
| 13 | `δ_0` bracket | **Paper 1** §4 (L1277–1299), Q 8.5 | Paper 2 §1; Paper 3 C12 (Paper 1 "UNREAD") | agreement; §4.1 item 5 | Paper 3 C12 → Paper 1 §4 |
| 14 | Five-row determinant ideal empty in low degree (`n = 4`) | Paper 3 C08: `I(D45)_d = 0`, `d ≤ 5`, PROVED | Paper 2: "measured empty through degree seven" (L977–978, L742) | different strength (proved ≤ 5, measured ≤ 7); compatible | Paper 2 could cite the proved half |

### 4.4 The minimal editorial arrangement (advice; the decision is the author's)

Minimal means the fewest edits that remove every friction above **without moving a proof**:

1. **Add mutual citations.** A bibitem for Paper 3 in Paper 2 and one for Paper 2 in Paper 3,
   with a one-clause cross-reference at rows 1, 3, 5, 7, 8 and 9. Everything else stays where it
   is.
2. **Harmonise the terminology** (§3.1, the proposed diff).
3. **Harmonise Paper 3's labels and wording** at C02 and C32 (§4.1 items 1 and 2) and in its
   three ladder summaries (item 3). These are small wording or record changes in Paper 3 only.
4. **Add the "fixed factor" half-sentence** in Paper 2 Rem. 6.3(iv) (§4.2).

Larger arrangements, for the author only (no recommendation made):
- keep the `n = 3` control argument in one paper and reduce the other to a statement plus a
  citation;
- keep the full determinant-part classification only in Paper 3 and restate Paper 2 Thm 6.2 as a
  corollary of it;
- present the cap theorem's proof only in Paper 2 (Paper 3 already only states it).

Proof placement, restructuring and publication are the author's decisions.

---

## 5. An observation on the scope of Paper 2's `n = 4` flag (reported, not resolved)

- **§2** asserts eq. (2.1), `mult_λ C[O]_δ = mult_{S_λ(C^r)} C[O|_{C^r}]_δ`, for
  `O = closure(GL_16·det_4)` with `O|_{C^r} = D^det_r`, and for the padded permanent. The
  justification is that Paper 1's proof "applies verbatim" (L254–262). **No flag is attached.**
- Paper 2 then uses (2.1) at `n = 4`:
  - the cap theorem's last step (L705–706);
  - §9's "By (2.1) both multiplicities are those of the orbit closures in `Sym^4 C^16`"
    (L860–861);
  - the length-nine paragraph (L1060).
- **§9, L1061–1063**, flags the `r = 9` instance ("not yet checked").
- Since the ambient multiplicity `a(λ, δ)` is the same on both sides for `ℓ(λ) ≤ r`, equality of
  multiplicities is equivalent to equality of ideal-copy counts. So the flagged transfer appears
  to be the `r = 9` instance of (2.1) (hand derivation, at the level of definitions only).
- B25-10 §2.4 notes that its re-derivation "used no step specific to degree 3", and it
  explicitly did not rule on `n = 4`.

**Consequence:** the flag is currently narrower than the paper's own unflagged uses. I do not
resolve this and I do not anticipate B26-04. After B26-04 is independently accepted or rejected,
the author should either lift the flag or extend it to §2's statement of (2.1) at `n = 4` and to
the places that use it (§6).

---

## 6. Author decisions (the list)

1. Apply the `(⋆)` → "the length-restriction lemma" rename (§3.1). Optionally rename the key
   `thm:star`.
2. Whether Paper 2 gives a locator for the length-restriction lemma (§3.2).
3. The Paper 2/3 arrangement: the minimal option (§4.4, items 1–4) or a larger one. This covers
   proof placement for rows 7 and 9.
4. Paper 3: align C02's label with C32 and Paper 2 Thm 3.1. This is a record/G26 decision.
5. Paper 3: reword C32's "residue OPEN" for `dim D_6^{per_3} = 50` against Paper 2's proof.
6. Paper 3: carry the `δ = 12` / higher-rung lineage split in the abstract, §1 and §8.
7. Paper 3: optionally narrow C34's `n = 3` condition to Kleiman and Dimca, citing Paper 1
   Prop. 4.23.
8. Paper 3: cite Paper 1 §4 for `δ_0`, after a reading pass that changes C12's read-status.
9. Paper 2: the scope of the `n = 4` flag against eq. (2.1) (§5), after B26-04's independent
   review.
10. Paper 2: confirm that `Companion2` contains the `s_5·C*` witness (B25-10 §4.3).
11. G-P2-SUB at submission: Paper 1's arXiv identifier; the repository URL for `Companion2` and
    `Companion3`, and whether it is the URL already printed in Data availability. The same
    identifier will be needed for Paper 3's `Paper1` bibitem.
12. Paper 1 (unchanged): G-P5, G-P2/G-P3 framing, MSC and arXiv categories, LMR journal metadata.
13. Whether a housekeeping pass delivers this packet and applies the three metadata appends
    (`results/b26_05/PROPOSED_DELIVERY_PATHS.txt`).
14. Circulation and publication of all three papers (user).

---

## 7. Source and method ledger

| claim at point of use | label | bytes |
|---|---|---|
| C45 PROVED at `δ = 12`; higher rungs keep s73 lineage; rename endorsed; `n = 4` not ruled | **READ** (B25-10 §2.4, §4.3, §4.4, §6, §10) | `42e7f4ba:docs/b25_10_review.md`, LF, raw `0488ce1e…` |
| Paper 2 TeX content, line numbers, the three `\star` | **READ** | LF rendering `c265937d…` of the CRLF blob `065f8799…` |
| Paper 3 TeX content | **READ** | LF blob `d7d92249…` |
| Paper 1 Prop. 4.19, 4.23, the `δ_0` bracket, Q 8.5, acknowledgement, byline, grep counts | **READ** | LF blob `4e1ccf70…` |
| Paper 2/1/3 metadata content | **READ** | blobs listed in §0.1 |
| PART 17b/17c edits and signature | **READ** | `EDITS_SUPPLEMENT_20260922.md` @ `79b68dcf`; `SIGNATURE_SUPPLEMENT_20260922.md` @ `848e22b4` |
| Build results (errors, pages) | **READ** (integrator's note); hashes verified by `sha256sum -c` | `build_evidence_20260922_close/` |
| Locators Paper 1 Prop. 4.19 / 4.23 / Q 8.5 resolve | **READ** (text extracted from the integrator's PDF with `pdftotext`; administrative) | `paper1_det3-conductor_848e22b4.pdf` (`2608e3d3…`) |
| s73's own label for the rungs above 12 | **UNREAD** by me; taken from Paper 3 `CLAIMS.md` C45 and B25-10 §2.4 | — |
| `9·6 − 4 = 50`; `29+5−1 = 33`, `31+5−1 = 35`; (2.1) at `r = 9` ⇔ the flagged transfer | **hand derivation** (arithmetic and definitions only) | — |
| B17-01, B26-01, B26-03, B26-04, A26-01 results | **not used**; not anticipated | — |
| Tool memory, conversation summaries | not used as evidence | — |

---

## 8. Limitations

- **Advice, not review.** The overlap map is advice, not a mathematical review. I re-derived no
  proof, and "agreement" means that the statements and labels are compatible as printed.
- **Paper 1 read in part.** Paper 1 was read at the shared passages (L1130–1310, L1940–2010,
  plus grep), not in full.
- **s73 not read.** The higher-rung label is carried from Paper 3 and B25-10.
- **Line numbers.** Paper 2 line numbers are of the LF rendering. They equal the CRLF blob's line
  numbers, since there are 1,247 lines in both.
- **Proposed after-state hashes.** The hashes for the proposed after-states come from scratch
  copies. Nothing was applied to the tree.
- **The §5 observation** is an equivalence at the level of definitions, not a ruling on the
  `n = 4` transfer.

## 9. Resource receipt

**Zero pilots, zero mathematical programs.**
- **Administrative operations used:** `git show`/`ls-tree`/`log`/`rev-parse`/`check-attr`, sha256
  hashing, `sha256sum -c` of the build evidence, `pdftotext` on the integrator's PDFs to verify
  locators, and text substitution plus `diff -u` and `git apply --check` on scratch copies to
  produce the proposed diffs.
- **Nothing else:** no compile, no fetch, no staging, no commit, no subagent.
- **Clock:** UTC start 2026-09-22T23:43:46Z; no 45-minute checkpoint (the slot has none); no
  interruptions. The stop time is in `results/b26_05/resource_receipt.json`.

## 10. Outcome

The deliverable is complete:
- the readiness table (§1);
- three metadata amendments and one TeX diff, proposed (§2, §3);
- placeholders reported (§3.3);
- the overlap map with a minimal arrangement (§4);
- one flag-scope observation (§5);
- the author-decision list (§6).

**No contradiction was found between the papers.** No paper is declared ready. Achievement level:
none of the four (editorial slot). The `n = 4` transfer flag is kept.
