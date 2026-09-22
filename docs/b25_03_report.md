# B25-03: Paper 1 packet repair for B24-01, and attribution-patch rebind

**Status: UNCOMMITTED.** This report and `results/b25_03/` are local prepared
work. A separately authorised delivery pass must commit their explicit paths
before G29 intake. No commit, stage, stash or other Git mutation was made.

- Producer: Claude, slot B25-03.
- Worktree: `C:/Users/swami/Projects/gct-gpt/work/batch15_workers/B23-05`,
  branch `b23-05-paper1`.
- Session: 2026-09-21, 03:37 to about 03:50 UTC.

## Outcome

Two of the preregistered outcomes apply: **(2) one relay claim withdrawn and
the other confirmed but narrowed**, and **(3) additional pre-posting items
found and recorded**.

1. **"Paper 1 awaits one signature": WITHDRAWN.**
   - What is established: the attribution patch is committed and unapplied,
     so a signature is pending. This is CERTIFIED from bytes; B24-10 §4.2
     found the same and B25-03 re-checked it in §4.
   - What fails: the word "one". A check at `bc7e62b7` leaves **four
     pre-posting items**, listed in §4.
   - `READINESS.md` already contradicted its own headline. Its last section
     says a real `pdflatex` run "is still owed before posting".
2. **"LMR Prop. 3.5.1 constructs `P₂`": CONFIRMED, NARROWED. PRIMARY.**
   - LMR construct `P_Λ` for odd `n`. They prove its orbit closure is an
     irreducible codimension-one boundary component of the `det_n` orbit
     closure, not contained in `End(W)·[det_n]`.
   - LMR do not mention `n = 3` or `P₂`. That at `n = 3` the orbit closure
     equals the paper's `P₂` is B25-03's own hand check (§3.3): an explicit
     linear change of coordinates. It is PROVED, but elementary.
   - The paper's sentence stating this (§"Boundary geometry") is accurate as
     written.
3. **Attribution patch: RE-BOUND, still NOT APPLIED.**
   - The digest `b911a151…` that B24-10 could not resolve is the CRLF
     working-copy rendering of the committed blob
     `bc7e62b7:paper/det3-conductor.tex` (content `f52f8d16…`).
   - The patch applies to that blob with zero offset.
   - **One wording flag is raised for the author** (§5.3). The
     introduction hunk uses the "no admissible family" phrase that B23-10
     §4.3/K9 rejected.
4. **The paper's surviving results** on the governing record are unchanged:
   `e(det₃) = 18` exactly and the one-dimensionality. B25-03 edited no
   mathematical text and no author or credit line.

---

## 1. Inputs read, and their status

| input | locator | used for | read-status |
|---|---|---|---|
| Slot prompt, `CLAUDE_COMMON.md`, `COMPUTE_PROTOCOL.md`, `SOURCE_INDEX.md` | `…/batch25_launch/v1_20260921T003934Z/` (UNCOMMITTED admin) | instructions | READ |
| Live ledger, B25-03 row and outcome space | `B15-12/docs/b25_12_ledger.md` (live working copy) | outcomes | READ |
| B24-10 §4 and §11.4 | `ab2f8a40:docs/b24_10_review.md` | the governing rulings on B24-01 | READ |
| B23-10 §4.1–4.5 and §12.1 (K9) | `239dd6e8:docs/b23_10_review.md` | attribution ruling and wording | READ |
| B24-02b §0, §1, §3, `lmr_quotes.md` | `5a97317e:docs/b24_02b_report.md`, `5a97317e:results/b24_02b/lmr_quotes.md` | the reading standard, and LMR's recorded bytes | READ |
| The six Paper 1 paths | `bc7e62b7` blobs and working copy | §2 | READ, from the bytes |
| LMR arXiv:1004.4802v1 | fetched fresh; §3.1 | Prop. 3.5.1, Thm. 1.0.1, §1 | **PRIMARY** (statements and construction; stabiliser proof step not audited) |

- **Not read by B25-03**, and so not relied on:
  - BI arXiv:1511.02927. B23-10 read it, and the rulings are carried from
    B23-10 §4.
  - The Hüttenhain thesis.
  - IK arXiv:1911.03990.
  - Kumar arXiv:1109.5996.
  - Marcus–Minc.
- **Tool memory.** One auto-memory index was loaded at session start. It
  holds prior-session notes, and one relevant note says no PDF text tool is
  on this host. That note was re-checked, and it is not a mathematical
  premise here. No tool memory was created by this session.
- **Git access.** No Git query was blocked. Committed inputs were read with
  `git show <commit>:<path>` from `work/batch15`, which shares the object
  database, and `git cat-file` here.

## 2. Bindings of the six paths

- **Baseline:** HEAD `bc7e62b714632c20d2405e54030224a2549c242d`, branch
  `b23-05-paper1`. `git status --porcelain --ignored` was empty at start
  (03:37:49 UTC), so the baseline matched the prompt.
- **No B24-01 packet exists at baseline.** There is no `docs/b24_01_report.md`
  and no `results/b24_01/`. B25-03 does not reconstruct one.
- `core.autocrlf=true`, and none of the six paths has a `.gitattributes`
  rule. All six blobs are LF.
- **Line endings, and a correction to my own method.** In this Git Bash,
  `grep -c $'\r$'` returned the line count for LF files too, so it is not a
  CR test. Every EOL statement below comes from raw byte counts
  (`tr -cd '\r' | wc -c`).

### 2.1 Before (baseline)

The "commit" column gives the blob id at `bc7e62b7`. The `SHA-256 (blob)`
column is the SHA-256 of that blob's content, i.e. the committed object.

| path | blob id | SHA-256 (blob) | blob bytes | working-copy SHA-256 (before) | wc bytes | wc CR count |
|---|---|---|---|---|---|---|
| `paper/det3-conductor.tex` | `975b59e931ff5ac4a1a1b49d08dbe0ce246c5c6e` | `f52f8d16a8d11d23a9f7ccd7ebc99dfb6d6fcf00b10ee3b128bb871034b4f866` | 114 279 | `b911a15184ebf819301deddfc178d76a5d9a6d01b881d5fc64b32a8982457445` | 116 406 | 2 127 (all lines CRLF) |
| `CHANGES.md` | `440e8592f02ce17232098e33ff9c01001453fe29` | `374160edf31347345235dcd8c08ed38d5ad96248842a88823b783e1bbe5a354d` | 29 075 | = blob | 29 075 | 0 |
| `GAPS.md` | `a783a19e3487c991b8a120e0db1b6da8050ccdc3` | `054706573b9dc042a358d39f129e817568c6096a514042fd4292bcbfe31f4ec0` | 26 297 | = blob | 26 297 | 0 |
| `READINESS.md` | `ff426dc7ef0d516516c3ee1d04403f121799d1f7` | `6f440fe78b1c1556938b160d83401af241dadd82f46071d635843f174b2f6e37` | 7 477 | = blob | 7 477 | 0 |
| `README.md` | `c52011622d461d39823528ac853313055f509629` | `de13076a194c9e4f23142bdb6102b35f63cf1518f0c83502aa0b24fd94687cd8` | 9 667 | `5ba2586a7f312be99fb6f6e231e95461a17acdc2c1c3e0fccdfc4c8427eeb617` | 9 892 | 225 (all lines CRLF) |
| `ATTRIBUTION_PATCH.md` | `f4f12c83eaad5495294a9e2933444a284c0dddfb` | `a8c261823985d9f907d6c8210bf1169d9c27c802a2cc5b38d5fd0ca7179b2357` | 10 517 | = blob | 10 517 | 0 |

- **The committed paper SHA-256 given in the prompt is verified.** It is
  `f52f8d16…`, all 64 hex digits.
- **The tex and README hash differences are line endings only.** Stripping
  CR from each working copy reproduces the blob digest. Inserting CR before
  each LF of the blob reproduces the working-copy digest.
- **Nothing was normalised.**

### 2.2 After (UNCOMMITTED)

| path | after SHA-256 (working copy, UNCOMMITTED) | bytes | change |
|---|---|---|---|
| `paper/det3-conductor.tex` | `b911a15184ebf819301deddfc178d76a5d9a6d01b881d5fc64b32a8982457445` | 116 406 | **unchanged** (byte-identical to before) |
| `CHANGES.md` | `13572d1564c40612f32c78b1091f87c494faa05ae81a36936102ddb8a0f1bb58` | 30 662 | +31 lines, 0 deleted (Part 0), LF kept |
| `GAPS.md` | `b1b8d4c773a614d85610b63999959164291e05d42ca5fa3f96f6f7ce809a298d` | 27 371 | +16, 0 deleted (status note), LF kept |
| `READINESS.md` | `9d82b251ead30b3e6b5634237b97b879365383a796c1db514447db87b5ee8470` | 9 662 | +36, 0 deleted (superseding note), LF kept |
| `README.md` | `5ba2586a7f312be99fb6f6e231e95461a17acdc2c1c3e0fccdfc4c8427eeb617` | 9 892 | **unchanged**; it makes no readiness, LMR or census-credit claim needing repair |
| `ATTRIBUTION_PATCH.md` | `4882be4b31000877a35636e61df195789002ef2cf91d59dfebab40650a678497` | 14 528 | +72, 0 deleted (binding note and §6), LF kept; §§1–5 and the diff block byte-identical |

- The diff block extracted from the after-state patch hashes to the same
  `ea80adeb…` as `results/b25_03/attribution_patch_extracted.diff`.
- `git diff --numstat` shows 0 deletions in every file.
- Git warns that these four LF files would become CRLF "the next time Git
  touches it". That warning describes a future checkout, not the current
  bytes. The committed blobs are LF, so a commit would keep them LF.

### 2.3 The historical digests, resolved

These digests appear in `CHANGES.md` Part I and `ATTRIBUTION_PATCH.md`. Each
is the CRLF rendering of a committed blob.

| digest | stated as | is the CRLF checkout of |
|---|---|---|
| `11e34759…` | pre-edit paper | `bbd1d12e:paper/det3-conductor.tex` (content `2cc15d3f…`) |
| `60b07db6…` | pre-edit README | `bbd1d12e:README.md` (content `c47e7396…`) |
| `b911a151…` | post-edit paper; the patch's target | `bc7e62b7:paper/det3-conductor.tex` (content `f52f8d16…`) |
| `5ba2586a…` | post-edit README | `bc7e62b7:README.md` (content `de13076a…`) |

So B24-01's post-edit working state is exactly what `bc7e62b7` committed.
This refines B24-10 §4.3 and ruling 4.7 ("resolves to NOTHING"). B24-10
hashed blob content, which is LF, over the branch history, and never tried
the CRLF rendering. Its conclusion that the binding was unverifiable was
correct for what it had. The binding itself was recoverable. B24-10's other
statements are unaffected.

## 3. LMR Prop. 3.5.1, read to B24-02b's standard

### 3.1 Version and hash

| object | SHA-256 | match |
|---|---|---|
| PDF `https://arxiv.org/pdf/1004.4802v1`, 180 675 bytes, `%PDF-1.4` | `cfc28275a8c6b27f0ad6946d495ed4f889f7617df479be943d8d35718dbf2d79` | equals SOURCE_INDEX's prior verified hash, B24-02b and B23-06 |
| ar5iv HTML (the text read) | `fb5844ada6bec339638b584bcf385686935e96e03aa8f0ab9e2561bb0b316e05` | equals B24-02b and B24-01's `CHANGES.md` |
| abstract page | `dc097e58fa7eeed4adc1f7869a5a737e1b8b0de6ccfb6f0f315fe0042ca473d6` | equals B24-02b; shows `[v1]` only |

- The files were fetched fresh with `curl` at 03:39 UTC.
- The PDF was hashed but not rendered, because no poppler is installed. The
  text was read from ar5iv, which is the same and only version.
- The verbatim quotes are in `results/b25_03/lmr_prop351_quotes.md`
  (L1–L5).

### 3.2 Locator, hypotheses, statement

- **Locator:** LMR §3.5, "On the boundary of the orbit of the determinant",
  Proposition 3.5.1, with the construction just before it (quotes L2, L3).
  The §1 pointer is quote L1.
- **Hypotheses:** `n` odd. LMR say "`P_Λ` … is easily seen to be zero for
  `n` even so we suppose `n` to be odd". `W = M_n(C)`, with `GL(W)` acting.
- **Statement:** `P_Λ ∈ closure(GL(W)·[det_n])`, and
  `closure(GL(W)·P_Λ)` is an irreducible codimension-one component of the
  boundary, not contained in `End(W)·[det_n]`.
- **Construction:** `P_Λ(M) = det_n(A,…,A,S) = Σ_{i,j} s_ij Pf_i(A) Pf_j(A)`,
  where `A` and `S` are the skew and symmetric parts of `M`, and `Pf_i` is
  the Pfaffian with row and column `i` deleted.
- **Proof status:** the degeneration `det_n(A+tS)` is given. The stabiliser
  computation is partly asserted ("one can check"), and **B25-03 did not
  audit it**. So the label is PRIMARY at the level of statement and
  construction.

### 3.3 Notation map to the paper, and the supported inference (INDEPENDENT hand check)

The paper defines `P₂` as the orbit closure of the universal quadric
`x₄x₁² + x₅x₂² + x₆x₃² + x₇x₁x₂ + x₈x₂x₃ + x₉x₁x₃` (paper §"Boundary geometry",
source lines 727–731 at `bc7e62b7`).

At `n = 3`, deleting row and column `i` from the skew matrix `A` leaves the
`2×2` skew block on the other two indices. So `Pf₁ = a₂₃`, `Pf₂ = a₁₃` and
`Pf₃ = a₁₂`, and

  `P_Λ = s₁₁a₂₃² + s₂₂a₁₃² + s₃₃a₁₂² + 2s₁₂a₂₃a₁₃ + 2s₂₃a₁₃a₁₂ + 2s₁₃a₂₃a₁₂`.

Now set `x₁ = a₂₃`, `x₂ = a₁₃`, `x₃ = a₁₂`, `x₄ = s₁₁`, `x₅ = s₂₂`,
`x₆ = s₃₃`, `x₇ = 2s₁₂`, `x₈ = 2s₂₃` and `x₉ = 2s₁₃`. This is an invertible
linear change of coordinates on `M₃(C) ≅ C⁹`, because `M ↦ (A, S)` is an
isomorphism onto the 3 + 6 skew and symmetric coordinates. Under it, `P_Λ`
becomes the universal quadric term by term.

Two variants give the same answer:

- LMR's first formula, `det₃(A,A,S)`, equals `tr(adj(A)S)` up to a nonzero
  scalar.
- The signed variant, with `adj(A) = wwᵀ` and `w = (a₂₃, −a₁₃, a₁₂)`,
  differs from the formula above only by `a₁₃ ↦ −a₁₃`.

Neither a scalar nor that sign changes the `GL₉`-orbit.

**Inference (PROVED, elementary):** `closure(GL₉·P_Λ) = P₂` at `n = 3`. With
LMR Prop. 3.5.1 (PRIMARY, statement level), `P₂` is LMR's component, and it
predates HL: LMR v1 is dated 27 Apr 2010 on the abstract page. The paper's
sentence says exactly this: "prove that … is an irreducible codimension-one
component of the boundary not contained in End·det_n \cite[Prop.~3.5.1]{LMR};
at `n=3` this is exactly `P_2`". It is **confirmed as written**.

- **Narrowing 1: who made the identification.** B24-01's `GAPS.md` row
  attributes the `n = 3` identification to the Hüttenhain thesis, and
  B25-03 did not read the thesis. The identification is carried here by
  the hand check above, not by the thesis.
- **Narrowing 2: what LMR state.** LMR state no `n = 3` instance.

**Not affected:** the paper's own results. LMR construct and classify the
component. They say nothing about `Φ₁₈`, its divisor, or `m₂ = 9`, and the
`m₂ = 9` label stays "computed, not proved" (G-A6).

### 3.4 The paper's other LMR uses (the same bytes)

| paper use | LMR text | verdict |
|---|---|---|
| after Cor. 4.13: `dc̄(per_m) ≥ m²/2` \cite[Thm.~1.0.1]{LMR}, "at `m = 3` already gives 5" | Thm. 1.0.1 `dc̄(perm_m) ≥ m²/2` (L5) | PRIMARY; confirmed (`⌈9/2⌉ = 5`) |
| "the earlier quadratic bound of Mignon and Ressayre, which they cite, is for determinantal complexity proper" | "The best known lower bound is `dc(perm_m) ≥ m²/2`, which was proved in [3]"; [3] = Mignon–Ressayre, IMRN 2004 | PRIMARY; confirmed |
| "the best previous bound for the border measure having been linear" \cite[§1]{LMR} | "The best known lower bound on this function had been linear", where "this function" is `dc̄(perm_m)` (text lines 65–71) | PRIMARY; confirmed |
| `\bibitem{LMR}`: CMH 88 (2013), no. 2, 469–484 | the arXiv abstract page has no journal-ref | **not verified here**; B24-01 took it from a secondary bibliography |

## 4. Readiness: what was checked, and what remains

### 4.1 What was checked

All checks ran on `bc7e62b7`, on the working copy with CR stripped.

| check | result | method |
|---|---|---|
| duplicate `\label` | none | grep/sort over comment-stripped source |
| `\ref`/`\eqref` → `\label` | 52 ref keys, **0 undefined** (64 labels, 12 unreferenced, which is harmless) | same |
| `\cite` → `\bibitem` | 23 keys, **0 undefined, 0 uncited** | same |
| brace balance (unescaped) | 1 418 / 1 418 | `tr` count |
| `$` parity (unescaped) | 3 014, even | `tr` count |
| theorem counter | 52 environments; `prop:census` 4.1, `cor:lower` 4.2, `thm:census` 4.5, `rem:norm` 4.7, `prop:divisor` 4.8, `cor:perm` 4.13, `rem:BI` 4.14, `thm:totals` 5.5, `lem:inputs` 5.6, `rem:arith` 5.10, `rem:fails` 5.11 (same as B24-01's statement) | token walk with shared counter per `\newtheorem` lines 12–20 |
| attribution applied? | **no**: line 176 "turns out to need no computation", line 560 "with no computation."; `Cor.~7.2]{BI}` 0 occurrences | grep |
| author line | line 40 `\author{Swami Sethuraman}`, untouched | read |
| header housekeeping | MSC `\subjclass[2020]{Primary 14L24; …}` present; line 3–4 comment asks for a glance at MSC and arXiv categories | read |
| LaTeX toolchain | `pdflatex`, `latexmk`, `tectonic`, `xelatex`, `lualatex`, `bibtex` and `kpsewhich` all absent; no MiKTeX or TeX Live directory | `command -v`, `ls` |
| build evidence on record | none; `READINESS.md` and `CHANGES.md` both say "not compiled" | read |
| G-P1 to G-P5 statuses in `GAPS.md` | read in full | read |

### 4.2 The four pre-posting items

"One signature" is not established. These four remain before posting:

1. **Author signature on `ATTRIBUTION_PATCH.md`.** It includes the choice of
   Cor. 4.2 form and a decision on the §5.3 wording flag. This is the
   ruled submission blocker (B23-10.13).
2. **A real LaTeX compile.** No build evidence exists, and this host cannot
   produce any. B24-01's own `READINESS.md` names it as "owed before
   posting". The script checks in §4.1 do not substitute for it: they
   cannot see macro errors, package errors or bibliography typesetting.
3. **G-P4.** Remark 4.14 credits the product-of-variables statement to
   `\cite{KumarCMH,KL}`, while IK credit it to Kumar's Compositio paper.
   `GAPS.md` says it "should be settled before submission". It is
   unresolved, and both of those sources are UNREAD by the record.
4. **Read-status of the B24-01 readings now at points of use in the paper.**
   These are IK Lem. 5.2 (edit Q2), Kumar Compositio Cor. 6.2 with its
   hypotheses (Q1), and Hüttenhain §8.1 and Cor. 8.3.2 (Q4, Q5). B24-01
   recorded hashes for its fetches (`CHANGES.md` Part I §1) but committed no
   quotes and no packet. Under B24-10 §4.1, "nothing from B24-01 is citable
   as a finding". **B25-03 did not re-read these**, by scope. For each
   one, either a quoted, hashed reading or explicit author acceptance is
   needed.

### 4.3 Author's discretion, not defects

- G-P5, the Marcus–Minc `UNREAD-CLASSICAL` label.
- G-P2 and G-P3, framing sentences.
- The optional one-sentence remark in patch §4.
- MSC codes and arXiv categories.
- LMR journal metadata, which could be confirmed at the publisher.

### 4.4 Open in the paper's own voice, and not blockers

G-A1 to G-A6, including primitivity and `m₂ = 9`.

## 5. Attribution patch: rebind and validation (patch NOT APPLIED)

### 5.1 Target

`bc7e62b7:paper/det3-conductor.tex`, blob `975b59e9…`, content SHA-256
`f52f8d16…`. The working copy `b911a151…` is its CRLF checkout (§2.3).

### 5.2 Applicability

- The diff block is extracted, byte for byte, as
  `results/b25_03/attribution_patch_extracted.diff` (42 lines, SHA-256
  `ea80adeb…`).
- `git apply --check` passes against a disposable LF copy of the blob,
  placed under `results/b25_03/validation_DISPOSABLE/`, and against the
  CRLF working copy (`--check` writes nothing).
- GNU `patch -p1` on the disposable copy applies all three hunks at their
  stated line numbers, with no offset or fuzz.
- The §2 prose locators are exact: 175–179, 498–501 and 559–561.
- **The patched disposable copy was checked as follows:**
  - SHA-256 `a289c9de57455dcf4e3666801f7f1af12f5306e5212b8eeb3b48806ff85a598c`.
    This is an UNCOMMITTED validation state and not the paper.
  - 0 undefined refs or cites, and 0 uncited items.
  - Braces balance at 1 423/1 423, and the `$` count is 3 024 (even).
  - The counter is identical (52 environments).
  - `\cite[Cor.~7.2]{BI}` occurs 3 times, and `Prop.~7.3` 0 times.
- The disposable directory was then deleted, and the paper was never
  touched.

### 5.3 Wording flag (new, READ)

This flag is raised for the author and is not applied.

- The patch's §2.1 sentence says "no family of `δ` distinct `D`-subsets of
  `[k]` exists at all". That is B23-10 §4.4 verbatim, and it is correct.
- The §2.3 introduction text says "the case of their plethysm bound
  \cite[Cor.~7.2]{BI} in which **no admissible family exists** at all".
- B23-10 §4.3 ruled against "the case of Cor. 7.2 … in which no admissible
  set exists": it is not Prop. 4.1, because that case includes the
  regularity failures. Corrigendum K9 (§12.1) replaced that phrase.
- The §2.3 wording therefore reintroduces the rejected distinction in the
  introduction. B24-10 §4.3's comparison checked only that the introduction
  credits BI, which §4.4 requires, so it did not test this point.
- **The wording in patch §§1–5 is preserved.** §6 of the patch offers the
  minimal consistent alternative ("in which no family of `δ` distinct
  `D`-subsets exists at all") for the author to take or leave at signing.

### 5.4 Adjudicated distinctions, preserved

- Prop. 4.1 is **RELATED**, as the pigeonhole special case, to BI Cor. 7.2.
  It is not equivalent to it.
- At `δ = 2m, k = 2D` it is the counting step of BI Prop. 3.24(3).
- Prop. 7.3 is not cited.
- The optional remark is one sentence with no novelty claim.
- These are carried from B23-10 §4.3–4.5 (READ). BI was not re-read by
  B25-03.

## 6. Computation

- **Zero mathematical pilots.** The compute lease was not requested and no
  mathematical program was run.
- No interpreter was launched. The only tools used were `curl`,
  `sha256sum`, `sed`/`tr`/`grep`/`awk` and `git apply --check`/`patch` on a
  disposable copy. These are administrative checks under
  COMPUTE_PROTOCOL.md.

## 7. Files

**Modified (UNCOMMITTED):**

- `ATTRIBUTION_PATCH.md`
- `CHANGES.md`
- `GAPS.md`
- `READINESS.md`

**Created (UNCOMMITTED):**

- `docs/b25_03_report.md`
- `results/b25_03/MANIFEST.json`
- `results/b25_03/lmr_prop351_quotes.md`
- `results/b25_03/attribution_patch_extracted.diff`

**Unchanged:**

- `paper/det3-conductor.tex`
- `README.md`

**Created and deleted within the session:**
`results/b25_03/validation_DISPOSABLE/` (a disposable validation copy).

Scratchpad files outside the repository hold the fetched LMR bytes and the
derived text. They are identified by hash in §3.1 and are not packet
files.

## 8. Remaining decision, and the next required certificate

**The remaining decision is the author's.** Sign `ATTRIBUTION_PATCH.md`, with
a choice on the Cor. 4.2 form and on the §5.3 wording flag. B25-03 did not
apply it.

**The next required certificate is a real LaTeX compile** of the signed
paper: a log with 0 undefined references and citations. Alongside it, the
read-status packet for the IK, Kumar-Compositio and Hüttenhain points of use
is needed, and G-P4 must be settled. Only then is a readiness count of zero
supportable.
