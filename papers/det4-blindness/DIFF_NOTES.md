# DIFF_NOTES — what slot B24-03 changed in `papers/det4-blindness/`, and on whose authority

**Slot B24-03, 2026-09-20.** A writing slot: no new mathematics, no computation, no pilot, no
`.pid`. Worktree `work/batch15_workers/B23-04`, branch `b23-04-paper3`.

**Session state, recorded before the first write.**

```
git rev-parse HEAD           ce43cdb79d8170a6f96f569bfe5f5be6036b5d4a
git rev-parse --abbrev-ref HEAD   b23-04-paper3
git status --porcelain       (empty)
```

Git was used read-only throughout (`rev-parse`, `status`, `log`, `show`, `cat-file`, `branch -a`,
`worktree list`). Nothing was committed, staged or stashed, and no sealed packet was edited.

**Files changed:** `det4-blindness.tex`, `CLAIMS.md`, `GAPS.md`, `BIB.md`. **New:** this file.
Nothing outside `papers/det4-blindness/` was written.

---

## 0. The one decision a reader should check first

**Four Batch-24 items had reported when this pass ran. None of them is committed on any ref.**

| item | where it lives | tracked? |
|---|---|---|
| B24-02 (`docs/b24_02_report.md`, `results/b24_02/`) | worktree `B15-01`, branch `b15-01-ci159` | **untracked** |
| B24-02b (`docs/b24_02b_report.md`, `results/b24_02b/`) | worktree `B15-01`, same branch | **untracked** |
| B24-05 (`docs/b24_05_report.md`, `results/b24_05/`) | worktree `B24-05`, branch `b24-05-dmodule` | **untracked** |
| B24-06 (`PAPER2_*.md`, four files) | worktree `B24-06`, branch `b24-06-paper2` | **untracked** |

Checked with `git log --all --name-only` over every local branch and remote, and against each
worktree's `git status --porcelain`.

**Consequence, under G26** — *every claim carries the record's label, the packet and commit* —
**no row of `CLAIMS.md` and no sentence of the draft cites any of them.** What each would change
is in `GAPS.md` Section E (G-30, G-31, G-32, G-36), naming the claim and the label it would move
it to, so that each becomes a one-edit update the moment its packet is committed.

**This cuts against the paper in two places, and it is applied anyway.**

1. **Row 1 of the kill table.** The launch prompt instructs: *"write the strong sentence: row 1 is
   a PROVED-kill on elementary premises across the whole window `N = 5..8`"*, on the authority of
   B24-02's pilot. The draft instead writes what the **committed** record carries, which is
   B23-10's corrigendum **K5** — a reviewer corrigendum, and those govern:

   > PROVED-kill at `N = 6, 7, 8` (no adopted input); at `N = 5` PROVED as GKZ Theorem B, modulo
   > Kleiman (ADOPTED, SECONDARY) at `k >= 7`.

   The corrected integrator ledger at `7d9839e7` says the same in its own words ("at `N = 5` it
   still leans on Kleiman for `k >= 7` — one cheap pilot would remove that"). **The window claim
   itself is not weakened:** row 1 *is* a PROVED-kill for every `k` across `N = 5..8` on committed
   bytes, and the draft says so in Ruling C48. What is held back is only the sentence "on
   elementary premises **across the whole window**", because the elementary premise at `N = 5`
   rests on an uncommitted packet. When B24-02 is committed, **one sentence in C48 and one clause
   in C18's provenance line** discharge the qualifier.

2. **Corollary D2′.** The prompt is explicit that this "belongs in the body of the blindness
   chapter, not in a table of dead candidates", and that judgement is right — it is a general
   exclusion of the same kind and scope as Lemmas 1.3 and 1.4 (C15, C16), excluding a class that
   goes through neither. The prompt is equally explicit about the rule when the packet is not
   committed, and B24-05 is not. **It is therefore at `GAPS.md` G-36, with its commit pending,
   and it is the omission this pass most regrets.** G-36 states the corollary and both its
   self-contained premises in full, so committing B24-05 turns it into an insertion, not a
   reconstruction.

The one thing the prompt asks *not* be changed — this paper's label on the cap theorem, which a
companion paper ships flat — is not changed. C11 keeps `ADOPTED modulo Kleiman, Dimca,
Gulliksen–Negård`, and the divergence is recorded at G-32.

---

## 1. Was it five stale rows?

The prompt says to identify the stale rows from `CLAIMS.md` against the committed packets, not to
take the count on faith, and to say so if it is not five.

**It is five.** Checked row by row against `68866e6d` (B23-02) and `3bcad666` (B23-03), which
agrees with B23-10 §6.1:

| row | was | now | authorising commit |
|---|---|---|---|
| C23 | rows 1–2 ASSESSED at `N = 6..8` | row 1 PROVED-kill at 6–8; row 2 splits (zero ideal CONDITIONAL for `j >= N−3`, OPEN for `2 <= j <= N−4`) | `3bcad666`, `239dd6e8` |
| C30 | kill-table rows 1, 10, 13 | rows 1, 2, 10, 13 all move | `68866e6d`, `3bcad666` |
| C35 | plane family "dim `>= 35`" | exactly 35 aff / 34 proj; `T1` 33/32; `Σ_Π` 31/30 | `3bcad666`, `239dd6e8` |
| C36 | classification OPEN | `closure(D45° ∩ P5) = T1 ∪ T2` PROVED; boundary OPEN | `3bcad666` |
| C37 | cap minors on the plane family OPEN | PROVED for every member of `Σ_Π` | `3bcad666`, `239dd6e8` |

**Two further rows carry a clause that is superseded rather than stale**, which is why they are
marked but not counted: `C34`'s MEASURED "64 on a cubic through a plane" (corrigendum K3) and the
"in flight" lineage notes on `C42`/`C43`/`C36`. B23-10 lists these as informational, and this pass
agrees with that classification.

---

## 2. Changes to `det4-blindness.tex`

One row per change. "Authority" is the commit whose bytes support the new text.

| # | where | was | is | authority |
|---|---|---|---|---|
| T1 | header comment, `\date` | slot B23-04 only | records the B24-03 pass, its scope, and that no uncommitted packet is cited | — (procedural) |
| T2 | abstract, clause (ii) | `d_1` rank-threshold kill stated at `N = 5` | adds `N = 6,7,8`, "there on elementary premises alone" | `3bcad666`, `239dd6e8` |
| T3 | abstract, clause (iii) | "At `N = 6,7,8` the rank-threshold kills are *assessed, not proved*" | proved for `d_1`, open for `2 <= j <= N−4`; adds that blindness worsens with `n` and not along the ladder, and that the second fundamental form's blind zone reproduces the LMR frontier | `3bcad666`, `feed104e`, `239dd6e8` |
| T4 | abstract, clause (iv) | "`D45 ∩ P5` is strictly larger than `{l·C : C ∈ D35}`" | the determinant part classified, with both exact dimensions; cap minors vanish on every cubic through a plane; right-way corner survives **on that part**; the boundary named as the paper's open question | `3bcad666`, `239dd6e8` |
| T5 | §1.3 thesis (b) | "At `N = 6,7,8` it is a heuristic" | proved for the first Koszul differential; heuristic for the higher ones in `2 <= j <= N−4` | `3bcad666`, `239dd6e8` |
| T6 | §1.3 thesis (c) | two vacuous statistics | adds that neither escape route — raising `n`, or climbing the ladder — helps | `feed104e` |
| T7 | §1.3 thesis (d) | "what is missing is a lift" | adds that the right-way corner is proved to survive on the determinant part and is **not known** to survive on the boundary | `3bcad666`, `239dd6e8` |
| T8 | §1.4 | "IDs `C01`–`C46`" | "`C01`–`C50`", with `C30` on the table caption | — (bookkeeping) |
| T9 | C09/C10, after the degree-five records | — | **new scope paragraph:** of the 23 closed degree-five cells only `(4^5)` has two lineages; the other 22 rest on producer plus integrator acceptance and their census values were not re-extracted. Prose now matches the gaps entry | `f008ac39`, `6915ae6f` (G-19) |
| T10 | C11 lineage | — | one-line pointer to G-32 (companion paper's divergent label). **Label unchanged**, as instructed | `82633a60` (the divergence itself is at G-32, uncommitted) |
| T11 | C18 provenance | "Kleiman for `k >= 7`" | quotes the corrigendum's "Kleiman remains the only adopted input for `k >= 7`" and points at the pending discharge (G-30) | `82633a60` (GKZ corrigendum C2) |
| T12 | §4, after C19 | — | **new Theorem C47:** `r_k(P_N) <= r_k(D_N)` for `N = 6,7,8`, every `k`, with the ceiling/floor structure, the monomial point `F_0`, all margins and the Newton certificate | `3bcad666` (Thm. 3.2), `239dd6e8` (replay) |
| T13 | §4, after C47 | — | **new Ruling C48:** row 1 across the window, with the two ends' premises kept apart. Transcribes K5 verbatim | `239dd6e8`, `7d9839e7` |
| T14 | C23 ruling | ASSESSED at `N = 6,7,8` | rewritten: `d_1` proved at 5–8 and 16; `d_j` split at 6–8 into CONDITIONAL zero ideal (`j >= N−3`) and OPEN (`2 <= j <= N−4`) | `3bcad666`, `239dd6e8` |
| T15 | §4, before the kill table | — | **new Proposition C49** (row 10 restated as `ker φ*`), plus the escape-paragraph analysis and the `2.1 × 10^10`-coefficient price — about 300× the per-vector cap at the degree floor of 8 | `68866e6d` |
| T16 | Table 1 row 1 | PROVED at `N = 5,16`; ASSESSED at 6,7,8 | PROVED at `N = 5,6,7,8` and 16, with the `N = 5`, `k >= 7` premise named | `3bcad666`, `239dd6e8` |
| T17 | Table 1 row 2 | ASSESSED at 6,7,8 | zero ideal for `j >= N−3` (CONDITIONAL); OPEN for `2 <= j <= N−4` | `3bcad666` |
| T18 | Table 1 row 10 | ASSESSED-kill; "holds on padding iff the closure has members in a hyperplane" | PROVED-merge into row 11 (10a/b/d); PROVED-kill at `N = 5` (10c) | `68866e6d` |
| T19 | Table 1 row 13 | "needs `D45 ∩ P5`" | target known on the determinant part, unknown on the boundary | `3bcad666` |
| T20 | paragraph after Table 1 | "row 10 is an ASSESSED-kill; the question is in flight" | rewritten: the question did not need an answer; what stays undecided is the boundary of the Bordiga family, and its own producer declines to fund it | `68866e6d` |
| T21 | after C31 | "the rank-threshold kills are only ASSESSED [at 6,7,8]" | first differential settled; higher ones open in the stated range | `3bcad666` |
| T22 | §5 | — | **new Lemma C50:** second fundamental form of `X_det_n` has rank `2(n−1)`; blind iff `N <= 2n`; visible rows iff `n <= m²/2`; ladder range `2m+3 .. m²+1`. Plus the LMR-frontier identification **with the reviewer's boundary precision** (LMR's inequality is not strict at `n = m²/2`, `m` even) and the catalecticant-is-reversed paragraph with `rank Cat_{k,n−k} = C(n,k)²` | `feed104e`, `239dd6e8` |
| T23 | C34 statement | `d >= onset I(D35)`; matrix "`75 × 70`" | strengthened to `d >= onset I(D35 ∪ Σ_Π)`; matrix corrected to **`70 × 75`** (the draft had it transposed — a defect in the draft's own prose, not in a packet, so fixed rather than logged) | `3bcad666` (§2.5); shape from B23-03's conventions |
| T24 | C34 provenance | "MEASURED ranks 64/64/65 at single points" | the "64 on a cubic through a plane" figure marked **SUPERSEDED** by C37 (K3); the other two kept | `239dd6e8`, `3bcad666` |
| T25 | C35 | "dim `>= 35` (affine) against exactly 33" | `T1`/`T2` named; exact 33/32 and 35/34; `Σ_Π` 31/30; neither inside the other. Provenance records the **convention ruling**: both of B22-10's figures were affine floors, "projective `>= 35`" was never in a packet, and B22-10's "off by one" is superseded (K4) | `3bcad666`, `239dd6e8` |
| T26 | C36 | Record: "classification OPEN" | **Theorem:** `closure(D45° ∩ P5) = T1 ∪ T2`, with `T3` and the skew-bordered type inside `T2`, and the reviewer's honest negative (read, not replayed) in the lineage | `3bcad666`, `239dd6e8` |
| T27 | C37 | Remark: vanishing OPEN | **Proposition:** `rank M_4(C) <= 64` on all of `Σ_Π`, generic exactly 64, with the syzygy argument; three method-disjoint lineages for the generic value; plus the carried caution that the witness has rank **58** | `3bcad666`, `239dd6e8` |
| T28 | §6, new subsection | — | "The right-way corner, and exactly how far it reaches", assembling the three results and scoping the corner to the determinant part — a scope requirement the reviewer imposed | `3bcad666`, `239dd6e8` |
| T29 | §6, new `question` environment | — | **Question 6.5 (G-A1):** the boundary. With the two invariants that fail to exclude it, the `>= 19` dimension floor, the Landsberg `dc̄ < dc` phenomenon, and the three closing routes — none of which is a pilot | `3bcad666`, `239dd6e8` |
| T30 | C42 statement | "would require `P` to divide every minor" | keeps that wording (it was always correct) and adds the corrected biconditional and the second prime `P₂ = 524269`, with "evidence, not proof; the label does not move" | `cc14e88c`, `239dd6e8` |
| T31 | C42 provenance | — | states **gate G27** and both corrigenda K1 (B22-10 S11) and K2 (B23-01's own sentence (b)); lineage updated, "in flight" removed | `239dd6e8` |
| T32 | C43 provenance | — | records that the second-prime test could have refuted the `Q` form and did not, which moves nothing | `cc14e88c`, `239dd6e8` |
| T33 | C44 | "conditional on its height-2000 search" | the scoped sentence quoted in full (common-denominator reading true, per-coefficient false, candidate height 2842); marked SUPERSEDED, not struck (K7) | `239dd6e8` |
| T34 | C04 lineage | "producer only; no reviewer row located" | **second lineage closed** by B23-10's re-derivation, with the residue named (Lemma 1 and (SUR) only) | `239dd6e8` |
| T35 | C32 lineage | producer + B13-07 | **second lineage closed** by B23-10 pilot 2 (fresh seed, two primes, ranks 4/10/20/35, floor 50), with residues named (Thm. 6 exactness; C33) | `239dd6e8` |
| T36 | C45 provenance | "read-status for this use not located" | states plainly that the rung `D = +1` is **CONDITIONAL on LMR at this use**, and that the two labels on record are for a different theorem and a different use | `239dd6e8` (B23-10.20), `82633a60` (s73 §2(c)) |
| T37 | §8, after the closing paragraph | — | **new scope paragraph, placed where the control is offered as the paper's evidence that the instruments work:** `i_det` is a nullity and a modular nullity is a ceiling, `i_per = 0` is proved over `Q`, so the certificates alone give only `0 <= D <= 1`; the floor, and with it the sign, comes from LMR and nowhere else; the record-internal alternative is Schwartz–Zippel evidence, not a membership proof | `82633a60` (s73 §2(c), §3, §8), `239dd6e8` |
| T38 | §9 open list | four items, with row 10 and the classification among them | reordered and rewritten: **the boundary is now item 1 and the paper's principal open question**; row 10 removed (closed) with the three-kinds summary in its place, marked ASSESSED; higher differentials at `2 <= j <= N−4` with the theory prerequisite named; LMR's read-status added | `3bcad666`, `68866e6d`, `239dd6e8` |
| T39 | bibliography | — | `Landsberg13` added under PRIMARY; the LMR entry rewritten to separate its three uses and three read-statuses | `feed104e`, `239dd6e8` |
| T40 | §§4–6 numbering | — | inserting C47, C48, C49, C50 and Question 6.5 shifted the draft's internal numbering in §§4–6. `CLAIMS.md`'s "draft" column was recomputed to match (12 rows renumbered). The `\cid` IDs and `\label`s are the stable keys | — (bookkeeping) |

**Static re-check after the pass** (there is still no TeX toolchain, GAPS P-1): 0 undefined
`\ref`, 0 duplicated `\label`, 50 claim IDs `C01`–`C50` with no gaps or duplicates, every `\lit`
key present as a `\bibitem` and every `\bibitem` cited, environments balanced, braces balanced,
59 provenance lines.

---

## 3. Changes to `CLAIMS.md`

| # | change | authority |
|---|---|---|
| M1 | Header records the B24-03 pass, its session state, the review's `46/46` result, the confirmed count of five stale rows, and the rule that uncommitted packets are not cited | `239dd6e8` |
| M2 | Packet-path table gains B23-01 `cc14e88c`, B23-02 `68866e6d`, B23-03 `3bcad666`, B23-06 `feed104e`, B23-10 `239dd6e8`, B23-12 `7d9839e7` | — |
| M3 | Rows C23, C30, C35, C36, C37 rewritten (the five stale rows), each marked `⟳ 2026-09-20` and numbered "stale row *n* of 5" | as in §1 above |
| M4 | Rows C04, C32 gain their second lineage; C09, C11, C24, C34, C42, C43, C44, C45 marked and amended as described in §2 | `239dd6e8`, and per row |
| M5 | Four rows added: C47, C48, C49, C50 | `3bcad666`, `239dd6e8`, `68866e6d`, `feed104e` |
| M6 | Draft-column numbers recomputed for the 12 rows whose numbering shifted | — |
| M7 | Cross-check list updated: 50 IDs; the static checks actually run; a G27 check; a check that every `D45 ∩ P5` claim says whether it concerns the determinant part; a check that no row cites an uncommitted path | — |

## 4. Changes to `GAPS.md`

| # | change | authority |
|---|---|---|
| N1 | Section A relabelled: the three slots have reported and been reviewed. G-1 answered (no refutation, no label moves), **G-2 CLOSED**, **G-3 CLOSED up to the boundary** | `cc14e88c`, `68866e6d`, `3bcad666`, `239dd6e8` |
| N2 | **G-2b** added: what B23-02 left undecided, and its producer's reasoned refusal to fund it | `68866e6d` |
| N3 | **G-6 partly closed:** `d_1` done at 6–8; `2 <= j <= N−4` open, with the theory prerequisite named and B23-03's pilot prices carried | `3bcad666`, `239dd6e8` |
| N4 | **G-14 CLOSED** (deficit lemma), with the residue: Lemma 1 and (SUR) only | `239dd6e8` |
| N5 | **G-15 sharpened and kept OPEN:** the reviewer's ruling that the rung is CONDITIONAL, the one-sidedness of the nullity, and why no computation can close it | `239dd6e8`, `82633a60` |
| N6 | **G-17 CLOSED**, and **this entry's own error corrected (K8)**: B22-10's rank was computed **exactly over `Q`**, not modulo a prime as the entry said. The correction is to the gaps entry, not to the packet | `239dd6e8`, `3bcad666` |
| N7 | **G-18** upheld, generalised into **gate G27**, and extended to B23-01's own transcription sentence (K1, K2) | `239dd6e8` |
| N8 | **G-23** kept OPEN with the reviewer's ranking and price | `239dd6e8` |
| N9 | **G-33** (the boundary, G-A1), **G-34** (washout residues), **G-35** (`T3 ⊆ T1`, recorded so the MEASURED profile is not mistaken for a claim) added | `3bcad666`, `239dd6e8` |
| N10 | **Section E added** — G-30 (B24-02), G-31 (B24-02b), G-32 (B24-06), G-36 (B24-05): reported, not committed, not citable, each with the claim it would move | the four uncommitted worktrees |
| N11 | **P-1** updated with the checks actually run and a note to the first slot with TeX about the shifted numbering; **P-3** amended; **P-5** added for this pass's session state | — |

## 5. Changes to `BIB.md`

| # | change | authority |
|---|---|---|
| B1 | Header explains why one item now carries three read-statuses, and warns against carrying one point of use's status to another | — |
| B2 | `Landsberg13` added under PRIMARY, load-bearing in two places | `feed104e`, `239dd6e8` |
| B3 | `LMR` rewritten: three uses, three statuses, with (iii) identified as carrying the *sign* of C45 and the pending B24-02b close described including the `C⁹ → C⁷` condition it would bring with it | `feed104e`, `239dd6e8`, and G-31 |
| B4 | `Kleiman` "used in" narrowed: its load in row 1 has shrunk to the single point `N = 5`, `k >= 7` | `3bcad666`, `82633a60` |
| B5 | Hilbert–Burch / Eagon–Northcott and the classical inputs of the `D45 ∩ P5` classification added under UNREAD-CLASSICAL, with the note that the two Hilbert-function facts are used only for `T1 ⊄ T2` | `68866e6d`, `3bcad666` |

---

## 6. What this pass did **not** do

- **No label was upgraded**, no condition dropped, no scope widened. `CERTIFIED-modular` is still
  `CERTIFIED-modular` (C42), the cap theorem is still `ADOPTED` (C11), and every CONDITIONAL row
  carries its condition in the same sentence.
- **No error in a committed packet was fixed in prose.** The three found in this pass — B22-10's
  "do vanish" (K3), B22-10's "off by one" (K4), and this file's predecessor's own misdescription
  of B22-10's method (K8) — are recorded in `GAPS.md` and left in the sealed packets.
- **Nothing was proved.** The one correction made directly in the draft's prose is the transposed
  matrix shape `75 × 70` → `70 × 75` (T23), which is the draft's own typo against B23-03's stated
  convention and changes no rank and no claim.
- **No uncommitted packet is cited**, and the four that reported are in Section E.
- **Paper 2's label was not matched**, as instructed (G-32).

---

## 7. Slot B25-01, 2026-09-21: the five edits unblocked by B24-10

A writing slot: no new mathematics, no computation, no pilot, no `.pid`, nothing installed.
Worktree `work/batch15_workers/B23-04`, branch `b23-04-paper3`.

```
git rev-parse HEAD                f95742aed4dd22d3f04ac1313ce3d78e6e0bc87c   (= launch pin)
git rev-parse --abbrev-ref HEAD   b23-04-paper3
git status --porcelain            (empty)            recorded 2026-09-21T03:35:28Z
```

Git read-only (`rev-parse`, `status`, `show`, `cat-file`, `config --get`, `diff`). Nothing was
committed, staged or stashed; no sealed packet was edited. **All after-state bytes are
UNCOMMITTED** until a separately authorised delivery pass binds them. Bindings:
`results/b25_01/bindings.md`; report: `docs/b25_01_report.md`.

**Authority.** B24-10 @ `ab2f8a40` is the governing review (§11 decides). The four Batch-24 items
that §§0–6 above held out as uncommitted are now committed at the pins the review verified:
B24-02 @ `f8273c3b`, B24-02b @ `5a97317e`, B24-05 @ `5c5ba86e`; the G-32 ruling is the review's
own. The review's closing ledger 11.9.7 orders the five edits first, with three corrections of
wording (11.6.9, 11.6.10, 11.6.12) and the C11 ruling (11.5.10, 11.6.11). §0 above is kept as
history: its two regretted omissions (the row-1 sentence, Corollary D2′) are now applied, and its
statement that C11 keeps `ADOPTED modulo` is superseded by the reviewer's ruling.

### 7.1 Changes to `det4-blindness.tex` (line numbers are in the after-state)

| # | item | where | was | is | authority |
|---|---|---|---|---|---|
| U1 | — | header comment L1–L18, `\date` L74–L78 | B24-03 pass; "Not compiled" | records B25-01; C01..C51; compile status split: B24-03 bytes compiled at 22 pp (integrator), B25-01 bytes not compiled | B24 ledger @ `f55ed57f` |
| U2 | G-30 | abstract (ii), L103–L105 | "the same holds at `N = 6,7,8` — there on elementary premises alone" | adds "across the whole window `N = 5..8` this is now proved on elementary premises alone" | `f8273c3b` §4.4 |
| U3 | G-32 / C11 | abstract (iv), L118–L119 | "the cap theorem (ADOPTED)" | "PROVED modulo Kleiman, Dimca and Gulliksen–Negård, all three ADOPTED inputs" | `ab2f8a40` 11.5.10 |
| U4 | G-31 | abstract L127–L129; §1.3 closing L214–L216; §8 closing L1036 | "`D = +1` at every rung", "a theorem at every rung" | each adds "PROVED modulo (★)" | `ab2f8a40` 11.3.7 |
| U5 | — | §1.4 L220–L227 | IDs C01–C50, 49 headings; label list | C01–C51, 50 headings; "PROVED modulo named premises" defined | bookkeeping |
| U6 | **C11** | provenance L353 | `ADOPTED modulo …`; "deliberately not resolved here" | **`PROVED modulo Kleiman (SECONDARY), Dimca (PRIMARY, statement level) and Gulliksen–Negård (SECONDARY), all three named ADOPTED inputs`**, with the source wording, the review's reason, and G-12 kept open | `82633a60` onset §0; `ab2f8a40` §5.3, 11.5.10, 11.6.11 |
| U7 | **G-36 / C51** | new `\subsection` L422, Cor. C51 L429–L442, two paragraphs L444–L462 | — (held at G-36) | **Corollary 4.5 (C51, D2′)**, witness named in the statement (`x_1^4 ∈ D45` in the image; `x_{11}^n ∈ Det_n`), "closed" in the hypothesis, D2 the only premise; the six disposals with D1 as premise of the first only; the witness-vs-mechanism paragraph with the escape route | `5c5ba86e` §1.2, §4; `ab2f8a40` §§2.1–2.4, 11.2.1–.10, 11.6.12 |
| U8 | G-30 | C18 provenance L484 | "a Batch-24 discharge … reported but not committed (G-30)" | row 1's use bypassed by B24-02's elementary proof; Theorem B not reproved, its label unchanged | `f8273c3b` §5 |
| U9 | **G-30 / C48** | Ruling C48 L515–L530 | K5's two-premise ruling, Kleiman at `N = 5`, `k >= 7` | PROVED-kill on elementary premises across `N = 5..8`; the `N = 5` ceiling/floor/tail statement; **"one control checked at three points"**; `D(k) > 0` scoped to `k >= 3`, used for integer `k >= 10` | `f8273c3b` §4, B24-02.1–.2; `ab2f8a40` §3.4, 11.3.11–.15 |
| U10 | G-30 | C23 first bullet L567–L569, provenance L583 | "with Ruling row1's distinction of premises" | "on elementary premises throughout"; Kleiman at `j >= N−3`, `N = 6,7` noted as a different, untouched use | `f8273c3b` |
| U11 | **G-30 / C24** | C24 provenance L600 | "No reviewer re-derivation on record" | second lineage: B24-02 INDEPENDENT hand re-derivation, **not a code replay**, no evaluator; implicit vertex hypothesis carried | `f8273c3b` §3; `ab2f8a40` 11.6.9 |
| U12 | G-30 | Table 1 row 1 L698, table provenance L719 | "at `N = 5`, `k >= 7` through Kleiman" | "on elementary premises (Ruling C48)" | `f8273c3b`; `ab2f8a40` 11.6.9 |
| U13 | G-32 | C34 provenance L840; §6.1 L896–L898 | "ADOPTED modulo …"; "the cap theorem's own ADOPTED label" | "PROVED modulo …, all three ADOPTED inputs". **The cubic-side `Σ_Π` in `d >= onset I(D35 ∪ Σ_Π)` is untouched** (B24-10 11.7.3) | `ab2f8a40` |
| U14 | **G-31 / C45** | C45 provenance L1025 | bare PROVED; "base value rests on LMR … read-status not on the record … CONDITIONAL" | **PROVED modulo (★)**; floor from LMR Thm. 2.3.1 + §3.1 + §3.2, PRIMARY; never Thm. 1.0.2; ceiling the record's own nullity, not LMR's "only one copy"; (★) = s73 §1, closed range `ℓ(λ) <= 7`, cell at endpoint; `N = 9 → 7` transport named as the load-bearing step; `a = 6` corroborates the ambient count only; lineages B24-02, B24-02b, B24-10 | `82633a60` s73 §1; `f8273c3b` §2; `5a97317e`; `ab2f8a40` §3, 11.3.1–.10, 11.6.10 |
| U15 | G-31 | §8 scope paragraph L1051–L1066 | "PROVED modulo LMR at this cell … reported done but not yet committed" | the reading is done; what remains is (★), with the double pinch; label PROVED modulo (★); G-37 | as U14 |
| U16 | G-31 | §9 item 4 L1095–L1099 | "the read-status of LMR … costs one reading" | "the status of (★) … a reading of the record, not a pilot (G-37)" | `ab2f8a40` 11.3.8, 11.9.10 |
| U17 | G-31 | bibliography LMR L1184–L1197 | (iii) "no read-status on the committed record … not committed (G-31)" | (iii) PRIMARY via B24-02b, file and hash, sections, proofs not audited; never Thm. 1.0.2; (★) is the record's | `5a97317e` |

Numbering: inserting C51 as Corollary 4.5 shifts the sixteen numbered results after it in §4 by
one (C17 → Fact 4.6, …, C49 → Prop. 4.21); §§5–8 are unchanged and Question 6.5 is still 6.5.
Derived mechanically from the shared `theorem` counter (`results/b25_01/static_check.txt`); the
`\cid` IDs and `\label`s remain the stable keys.

### 7.2 Changes to `CLAIMS.md`

| # | change | authority |
|---|---|---|
| V1 | Header paragraph for B25-01; the "uncommitted packets" paragraph marked historical; `C01`–`C51` | — |
| V2 | Packet table: B24-02 `f8273c3b`, B24-02b `5a97317e`, B24-05 `5c5ba86e`, B24-10 `ab2f8a40` | — |
| V3 | "How to read a row" note: the one label moved away from ADOPTED is C11, on B24-10's ruling | `ab2f8a40` 11.5.10 |
| V4 | Rows **C11** (label), **C18** (note), **C23** (clause), **C24** (lineage), **C30** (row-1 label), **C34** (cap label), **C45** (label + lineage), **C48** (statement + label + lineage), each marked `⟳ 2026-09-21` | per row |
| V5 | New row **C51** (D2′) | `5c5ba86e`, `ab2f8a40` |
| V6 | Draft column renumbered for C17–C29, C47, C48, C49 | — |
| V7 | Cross-checks: 51 IDs; cap label check rewritten; C45 and C51 checks added; row-1 check updated; "no uncommitted path" updated | — |

### 7.3 Changes to `GAPS.md`

| # | change | authority |
|---|---|---|
| W1 | Header note for B25-01: Section E committed; "uncommitted" entries are history with dispositions | — |
| W2 | **G-12**: label correction recorded; gap (primary reads) stays OPEN | `ab2f8a40` |
| W3 | **G-15 CLOSED** as read-status; residue → G-37 | `5a97317e`, `ab2f8a40` |
| W4 | **G-23 CLOSED to the extent of a hand re-derivation**; no evaluator | `f8273c3b`, `ab2f8a40` |
| W5 | **G-29** lineage note updated | — |
| W6 | **P-1**: the historical "not compiled" checked — B24-03 bytes compiled at 22 pp (integrator); B25-01 bytes not compiled, no toolchain | `f55ed57f` |
| W7 | **P-6**: this pass's session state | — |
| W8 | **G-37** new: (★)'s label open; B25-05 neither awaited nor assumed | `ab2f8a40` 11.3.3–.8 |
| W9 | Section E: disposition table (G-30/31/36 APPLIED, G-32 CLOSED); "three negative controls" annotated *sic* with the correction; "same kind and scope" annotated WITHDRAWN. The original entries are otherwise kept byte-for-byte | `ab2f8a40` 11.3.13, 11.2.9, 11.6.9–.12 |

### 7.4 Changes to `BIB.md`

| # | change | authority |
|---|---|---|
| X1 | 2026-09-21 change note | — |
| X2 | Dimca, Gulliksen–Negård, Kleiman: "cap theorem (ADOPTED)" → ADOPTED inputs of a theorem PROVED modulo them; Kleiman no longer in row 1 | `ab2f8a40`, `f8273c3b` |
| X3 | LMR use (iii): PRIMARY via B24-02b, full hash, sections, proofs not audited, never Thm. 1.0.2, (★) carried; this slot did not re-read the PDF | `5a97317e` |

### 7.5 What this pass did not do

- **No new mathematics, nothing proved.** Every new sentence is a committed packet's or the
  review's, cited at its commit. No source conflict needing a proof was found.
- **No label beyond the review's rulings.** C45 is PROVED modulo (★), not PROVED; C11 is PROVED
  modulo named ADOPTED inputs, not PROVED; C24's label is unchanged; C18's label is unchanged.
- **(★) was not audited** and B25-05 was not awaited: G-37 records it open.
- **LMR was not re-read by this slot**; its PRIMARY status is B24-02b's committed reading.
- **The draft was not compiled.** No TeX toolchain is installed; a static source check is not a
  compile.
- **The scope of the determinant-part restriction and of G-A1 is unchanged**: at the five
  right-way-corner occurrences (abstract, thesis (d), Table 1 row 13, §6.1, §9 item 1) the
  determinant-part scoping clauses are untouched — two of those paragraphs (abstract (iv), §6.1)
  had only their cap-theorem label changed — and Question 6.5 is not edited. "No five-row
  determinant equation is known to be nonzero on padding" is unchanged. Author credits are
  unchanged.
- **Tool memory.** This slot wrote one post-hoc outcome note to auto-memory, which is not a premise. A later-written entry in the shared auto-memory index names a B25-05 outcome
  for (★). It is another session's tool memory, not a committed packet: it was **not** used, and
  G-37 stays open.
