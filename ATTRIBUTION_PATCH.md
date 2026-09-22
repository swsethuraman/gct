# ATTRIBUTION PATCH — Proposition 4.1 (Bracket census) and Bürgisser–Ikenmeyer

**Status: PREPARED, NOT APPLIED.** `paper/det3-conductor.tex` is unchanged by
this file. It is the author's credit line, and the author signs it off.

> **Binding corrected by B25-03 (2026-09-21 UTC; UNCOMMITTED).** The header
> bullets below are kept as B24-01 wrote them. The target they name is now
> resolved. It is `bc7e62b714632c20d2405e54030224a2549c242d:paper/det3-conductor.tex`,
> blob `975b59e931ff5ac4a1a1b49d08dbe0ce246c5c6e`, content SHA-256
> `f52f8d16a8d11d23a9f7ccd7ebc99dfb6d6fcf00b10ee3b128bb871034b4f866` (LF,
> 114 279 bytes). The digest `b911a151…` below is the CRLF working-copy
> rendering of exactly that blob (`core.autocrlf=true`), so it is not a lost
> state. Applicability to the committed blob, and one wording flag for the
> author, are in §6. Nothing in §§1–5 has been reworded.

- **Worktree:** `C:\Users\swami\Projects\gct-gpt\work\batch15_workers\B23-05`,
  branch `b23-05-paper1`, HEAD `bbd1d12e80ae162feb368f75c9c270ccf79747f8`.
- **Applies to:** `paper/det3-conductor.tex` as it stands *after* the B24-01
  edits recorded in `CHANGES.md`, sha256
  `b911a15184ebf819301deddfc178d76a5d9a6d01b881d5fc64b32a8982457445`.
  (None of those edits touch any of the three passages below, so the patch also
  applies cleanly to the file at HEAD, modulo line offsets.)
- **Authority:** ruling **B23-10.13** and corrigendum **K9**, in
  `docs/b23_10_review.md` §4.3 and §4.4, at commit
  `239dd6e84417ab04914a8d84cca02ddf754bf1fb`.

---

## 1. The ruling, and why it is narrower than B23-05 alleged

B23-05 (`GAPS.md`, G-P1) alleged that Proposition 4.1 is **equivalent** to
Bürgisser–Ikenmeyer Cor. 7.2 *with* Prop. 7.3. B23-10 read BI in full and ruled
otherwise (§4.3, ruling B23-10.13):

- **RELATED — a special case, not an equivalent.** Prop. 4.1 is the
  **pigeonhole case** of BI Cor. 7.2: put `d = δ`; if `δ > C(k, D)` then no
  family of `δ` distinct `D`-subsets of `[k]` exists at all, so BI's count is
  `0`. At `δ = 2m`, `k = 2D` it is **exactly** the counting step of BI
  Prop. 3.24(3), word for word.
- **Cor. 7.2 is strictly stronger.** It counts, and it imposes regularity (each
  element in exactly `m` subsets), so it can vanish where `δ ≤ C(k, D)`.
  Prop. 4.1's statement uses only the "no distinct family at all" case.
  B23-05's proposed phrase "the case of Cor. 7.2 in which no admissible set
  exists" is *also* wrong, because that case includes the regularity failures.
- **Prop. 7.3 is not needed** for the implication, and **BI state it without
  proof** ("We state without proof …"). Citing it would import an unproved
  statement for nothing. It is dropped from the credit.
- **What B23-05 got right, and what remains a blocker.** The substance: the
  census is not the paper's. BI prove it (Cor. 7.2) and use it (Prop. 3.24(3)),
  and Corollary 4.2 (`e(det₃) ≥ 18`) follows from BI Cor. 7.2 plus their period
  theorem alone — at `m = 9`, `D = 3` the pigeonhole excludes
  `δ = 3, 6, 9, 12, 15` (`C(k,3) = 0, 0, 1, 4, 10 < δ`). So the paper's "turns
  out to need no computation … already excludes every smaller degree" is BI's
  argument and needs their name.
- **Not a retraction.** B23-10 §4.5 and ruling B23-10.14: the two proofs are
  the same antisymmetry of odd-degree letters (BI via the transposed-plethysm
  weight space, the paper via the first fundamental theorem and the sign
  `(−1)^D = −1`). That is worth **one remark sentence** and **no claim of a new
  result**. The novelty claims that survive untouched are `e(det₃) = 18`
  exactly, the one-dimensionality, the value, and everything after.

---

## 2. The three passages: exact current text, exact proposed text

### 2.1 The paragraph introducing Proposition 4.1 (currently at lines 498–501)

**Current, verbatim:**

```latex
A second, entirely elementary constraint removes the rest of the range.  It is
a parity count on bracket monomials, and it extends the argument by which Howe
disposes of $\delta=m$ when $D$ is odd; we state it in general because the
statement costs nothing extra and because it is what does the work here.
```

**Proposed, verbatim** (the added sentences are B23-10 §4.4's wording):

```latex
A second, entirely elementary constraint removes the rest of the range.  It is
a parity count on bracket monomials, and it extends the argument by which Howe
disposes of $\delta=m$ when $D$ is odd; we state it in general because the
statement costs nothing extra and because it is what does the work here.
Proposition \ref{prop:census} is the case of B\"urgisser and Ikenmeyer's
plethysm bound \cite[Cor.~7.2]{BI} in which no family of $\delta$ distinct
$D$-subsets of $[k]$ exists at all, and for $\delta=2m$, $k=2D$ it is the
counting step of \cite[Prop.~3.24(3)]{BI}.  We include the bracket-monomial
proof because it is short and self-contained.
```

### 2.2 Corollary 4.2 (currently at lines 559–561)

**Current, verbatim:**

```latex
\begin{corollary}\label{cor:lower}
$e(\det_3)\ge 18$, with no computation.
\end{corollary}
```

**Proposed, verbatim** (B23-10 §4.4 offers two forms; this is the one that
keeps "with no computation" and adds the citation):

```latex
\begin{corollary}\label{cor:lower}
$e(\det_3)\ge 18$, by \cite[Cor.~7.2]{BI} and the period theorem, with no
computation.
\end{corollary}
```

*Alternative, also authorised by §4.4:* drop "with no computation" and let the
statement read `$e(\det_3)\ge 18$, by \cite[Cor.~7.2]{BI} and the period
theorem.`

### 2.3 The introduction (currently at lines 175–179)

**Current, verbatim:**

```latex
Section \ref{sec:det} contains the main results.  The lower bound
$e(\det_3)\ge18$ turns out to need no computation: an elementary parity count
on bracket monomials (Proposition \ref{prop:census}), which recovers Howe's
vanishing theorems and reproduces the classical first-invariant degrees for
ternary cubics and cubic surfaces, already excludes every smaller degree.
```

**Proposed, verbatim:**

```latex
Section \ref{sec:det} contains the main results.  The lower bound
$e(\det_3)\ge18$ needs no computation, and it is B\"urgisser and Ikenmeyer's:
an elementary parity count on bracket monomials (Proposition
\ref{prop:census}), which is the case of their plethysm bound
\cite[Cor.~7.2]{BI} in which no admissible family exists at all and which
recovers Howe's vanishing theorems and reproduces the classical
first-invariant degrees for ternary cubics and cubic surfaces, already
excludes every smaller degree.
```

---

## 3. The diff

Unified diff against `paper/det3-conductor.tex` at sha256 `b911a151…`. Apply
with `git apply` or `patch -p1` from the worktree root.

```diff
--- a/paper/det3-conductor.tex
+++ b/paper/det3-conductor.tex
@@ -173,10 +173,13 @@
 boundary weight.
 
 Section \ref{sec:det} contains the main results.  The lower bound
-$e(\det_3)\ge18$ turns out to need no computation: an elementary parity count
-on bracket monomials (Proposition \ref{prop:census}), which recovers Howe's
-vanishing theorems and reproduces the classical first-invariant degrees for
-ternary cubics and cubic surfaces, already excludes every smaller degree.
+$e(\det_3)\ge18$ needs no computation, and it is B\"urgisser and Ikenmeyer's:
+an elementary parity count on bracket monomials (Proposition
+\ref{prop:census}), which is the case of their plethysm bound
+\cite[Cor.~7.2]{BI} in which no admissible family exists at all and which
+recovers Howe's vanishing theorems and reproduces the classical
+first-invariant degrees for ternary cubics and cubic surfaces, already
+excludes every smaller degree.
 B\"urgisser and Ikenmeyer prove $e(\det_n)\ge n^{2}$ for every $n$, strictly
 when $n$ is odd, and their degree-period theorem confines $e(\det_3)$ to the
 multiples of $6$ that are at least $12$; equality $e(\det_n)=n^{2}$ is known
@@ -499,6 +502,11 @@
 a parity count on bracket monomials, and it extends the argument by which Howe
 disposes of $\delta=m$ when $D$ is odd; we state it in general because the
 statement costs nothing extra and because it is what does the work here.
+Proposition \ref{prop:census} is the case of B\"urgisser and Ikenmeyer's
+plethysm bound \cite[Cor.~7.2]{BI} in which no family of $\delta$ distinct
+$D$-subsets of $[k]$ exists at all, and for $\delta=2m$, $k=2D$ it is the
+counting step of \cite[Prop.~3.24(3)]{BI}.  We include the bracket-monomial
+proof because it is short and self-contained.
 
 \begin{proposition}[Bracket census]\label{prop:census}
 Let $D$ be odd and let $\delta,m$ satisfy $m\mid \delta D$.  Put $k=\delta D/m$.
@@ -557,7 +565,8 @@
 \]
 
 \begin{corollary}\label{cor:lower}
-$e(\det_3)\ge 18$, with no computation.
+$e(\det_3)\ge 18$, by \cite[Cor.~7.2]{BI} and the period theorem, with no
+computation.
 \end{corollary}
 
 At $\delta=18$ the census is silent, and one exact count settles what it leaves
```

**Checked on the patched copy, not on the paper:** braces balanced, `$` count
even, no undefined `\ref` or `\cite`, and the theorem numbering is byte-for-byte
identical to the unpatched file (52 environments, `prop:census` = 4.1,
`cor:lower` = 4.2 both before and after). No LaTeX toolchain is installed here,
so the source was not compiled.

---

## 4. Optional addendum (not part of the ruling's required wording)

B23-10 §4.5 observes that the paper's proof and BI's are the same antisymmetry
reached two ways, and that this is worth one sentence *if the author wants it*.
It is an addition, not a correction, and the patch above is complete without
it. If wanted, append to §2.1's proposed text:

```latex
The route differs: BI pass through the transposed-plethysm weight space,
where the exterior power forbids repeated $D$-subsets, while the proof below
uses the first fundamental theorem and the transposition sign $(-1)^{D}=-1$.
```

---

## 5. What the author is agreeing to

Signing this off means conceding that the bracket census is not the paper's
result: Bürgisser and Ikenmeyer proved the bound (Cor. 7.2), used the same
counting step (Prop. 3.24(3)), and their bound is strictly stronger than
Proposition 4.1, so the lower bound `e(det₃) ≥ 18` follows from their work plus
their period theorem without any of this paper's machinery. Three passages
therefore stop presenting that bound as the paper's own and name BI instead. It
is not a retraction and nothing is withdrawn: the bracket-monomial proof stays,
because it is short, self-contained and takes a different route to the same
antisymmetry; and the results that make the paper — `e(det₃) = 18` exactly, the
one-dimensionality of the ambient and restricted spaces, the value
`Φ₁₈(det₃) = −2¹⁶3⁷5³7²`, the divisor, the semigroup, the conductor, the
degree-24 generator and the length theorem — are untouched and uncontested. The
cost is one paragraph of credit and the loss of the word "elementary" as a claim
of priority; the gain is that a referee who knows BI Appendix 7 will find the
citation already there rather than discovering it themselves. B23-10 rates this
a **submission blocker** (ruling B23-10.13), so arXiv should wait on this
signature.

---

## 6. Binding addendum (B25-03, 2026-09-21 UTC; UNCOMMITTED, patch still NOT APPLIED)

**Target.** Commit `bc7e62b714632c20d2405e54030224a2549c242d`, path
`paper/det3-conductor.tex`, blob `975b59e931ff5ac4a1a1b49d08dbe0ce246c5c6e`,
content SHA-256 `f52f8d16a8d11d23a9f7ccd7ebc99dfb6d6fcf00b10ee3b128bb871034b4f866`,
114 279 bytes, 2 127 LF lines.

**The historical digest.** The working copy is 116 406 bytes with CRLF on all
2 127 lines, SHA-256
`b911a15184ebf819301deddfc178d76a5d9a6d01b881d5fc64b32a8982457445`. Two
checks show it is the committed blob:

- inserting `\r` before every `\n` of the blob hashes to `b911a151…`;
- stripping `\r` from the working copy hashes to `f52f8d16…`.

So the header's `b911a151…` is the CRLF checkout of the file B24-01 then
committed, with its content unchanged. B24-10 §4.3 hashed blob contents
(LF), which is why it did not find the digest. The header's HEAD
`bbd1d12e…` was HEAD while the edits were in progress; the edited file is
committed at `bc7e62b7`. By the same test, `CHANGES.md` Part I's pre-edit
digests `11e34759…` (paper) and `60b07db6…` (README) are the CRLF
renderings of the `bbd1d12e` blobs `2cc15d3f…` and `c47e7396…`.

**Applicability, checked without touching the paper:**

- The §3 diff is extracted as `results/b25_03/attribution_patch_extracted.diff`
  (SHA-256 `ea80adeb9b85cc3906bf03086cbc404e6e99cdf49086376290f13c14229734f5`,
  UNCOMMITTED). `git apply --check` passes against a disposable LF copy of
  the blob, and also against the CRLF working copy. `git apply --check`
  writes nothing.
- GNU `patch -p1` on the disposable copy applies all three hunks at their
  stated lines, with no offset or fuzz.
- §2's line locators are exact at `bc7e62b7`: 175–179, 498–501 and
  559–561.
- After the patch, the disposable copy's SHA-256 is
  `a289c9de57455dcf4e3666801f7f1af12f5306e5212b8eeb3b48806ff85a598c` (LF).
  This is an UNCOMMITTED validation state, not the paper, and the copy has
  been deleted. On that copy:
  - 0 undefined `\ref`/`\eqref`, 0 undefined `\cite` and 0 uncited
    `\bibitem`;
  - braces balance at 1 423/1 423, and the `$` count is even;
  - the theorem counter matches the unpatched file exactly (52
    environments; `prop:census` = 4.1, `cor:lower` = 4.2);
  - `\cite[Cor.~7.2]{BI}` occurs 3 times and `Prop.~7.3` 0 times.
- Not compiled, because no LaTeX toolchain is installed.

**One wording flag for the author (not applied, wording above unchanged).**
§2.1's sentence correctly says "no family of $\delta$ distinct $D$-subsets
of $[k]$ exists at all". §2.3's introduction text says "the case of their
plethysm bound \cite[Cor.~7.2]{BI} in which no admissible family exists at
all". B23-10 §4.3 (at `239dd6e8`) rejected that phrase: "the case of
Cor. 7.2 … in which no admissible set exists" is not Prop. 4.1, because
that case includes the regularity failures. Corrigendum K9 replaced it. The
§2.3 text therefore conflicts with the ruling it implements. B24-10 §4.3
checked only that the introduction credits BI, so it did not test this
point. If the author wants the §2.3 text to match §2.1 and K9, the minimal
change is "in which no family of $\delta$ distinct $D$-subsets exists at
all". Either way, this is part of the same signature decision. **The
author/credit line and the paper are untouched.**
