# B27-04 — editorial pass on Papers 1–3

**Slot:** B27-04 (Claude producer). **Date:** 2026-09-23 UTC. **Authority:** the author accepted
all edits on 2026-09-23 (`B27-04.md`); the user authorised the slot at launch. **Method:** apply the
committed diffs with `git apply --check` then `git apply`, plus the enumerated own-wording edits.
Static source checks only: no TeX is installed, so nothing was compiled. The integrator compiles.
No compute runs (the static check is an administrative text scan).

**Registered outcome: 14 of the brief's 15 items APPLIED, 1 STOPPED** (Paper 3 item 4, the "35" gloss; §4). Paper 1: 3/3. Paper 2: 6/6 (rename, two appends, flag, smooth-cubic, BLOCKERS). Paper 3: 5/6 (items 1, 2, 3, 5, and the CLAIMS/GAPS update; item 4 stopped).

## 0. Preflight

| item | value |
|---|---|
| `B27_COMMON.md` raw sha256 | `891e3ca872bc795b6f943ac89f55112573803f006e0208940dd6cad1f750d6ee` (matches board) |
| `B27-04.md` raw sha256 | `165f3a62706f406258cc3fac00084126deb59f046830b93dee963738268d20ea` (matches board) |
| `BATCH27_BOARD.md` raw sha256 | `b0bc2501aba62d49b91862d821232ac1b9904480057a8dcdb4cbc03fbd86efec` |
| `b27-04-p1` HEAD | `f3b1d3297f44ac0819042847b8064bad5e38d159` = PART 25 setup commit (parent `af8468f3`); worktree clean; `ls-remote` equal |
| `b27-04-p2` HEAD | `e3823bd519cf7ec3dc531c924bf561cd38aa7593` = PART 25 setup commit (parent `721d54a2`); worktree clean; `ls-remote` equal |
| `b27-04-p3` HEAD | `64424450850bd7b6e1da1759e1586719e033599e` = PART 25 setup commit (parent `0a8029bb`); worktree clean; `ls-remote` equal |
| output paths | `docs/b27_04_report.md`, `results/b27_04/`, `analysis/b27_04_static_check.py`: absent before this pass |

The brief and receipts are dated 2026-09-23. That is the UTC date; the machine's local date was
still 2026-09-22 (EDT), so this is not a mismatch.

## 1. Inputs (which bytes each hash names)

| input | commit:path | raw sha256 | check |
|---|---|---|---|
| Kumar citation diff | `af8468f3:results/b26_03/b26_03_gp4_kumar_citation.diff` | `955ab126…` | = B26-03 MANIFEST |
| IK Lem. 5.2 narrow diff | `af8468f3:results/b26_03/b26_03_ik_lem52_narrow.diff` | `b574d1b5…` | = B26-03 MANIFEST |
| IK arXiv locator diff | `af8468f3:results/b26_03/b26_03_ik_arxiv_locator_OPTIONAL.diff` | `0a6e6da3…` | = B26-03 MANIFEST |
| rename diff (CRLF) | `721d54a2:results/b26_05/proposed/paper2_length_restriction_rename.CRLF.diff` | `f4afd947…` | = B26-05 MANIFEST (`has_cr: true`) |
| CLAIMS append diff | `721d54a2:results/b26_05/proposed/PAPER2_CLAIMS.append.diff` | `d1883dd2…` | = B26-05 MANIFEST |
| READINESS append diff | `721d54a2:results/b26_05/proposed/PAPER2_READINESS.append.diff` | `120b5a49…` | = B26-05 MANIFEST |
| B26-04 report (§7 wording) | `65736d9f:docs/b26_04_report.md` | `9d61f5e2…` | READ §6–§7 |
| B26-10A review (acceptance of §7 wording) | `21816b3c:docs/b26_10a_review.md` | — | READ §3.3–§3.4 (line 110: "Its proposed replacement is accurate for `D₉`") |
| B26-05 report (overlap map) | `721d54a2:docs/b26_05_report.md` | `26717997…` | = B26-05 MANIFEST; READ §1, §4 |
| Paper 2 before-state | `e3823bd5:paper/det4-onset.tex` | `065f8799…` | = the bytes B26-05's diffs target |

Blobs read to label citations: Paper 2 Thm. 3.1 (Washout, L288) and Lemma 3.3 (Finite generic
stabiliser, L322), and Paper 1 Prop. 4.23 (The Jacobian cap, L1231) are READ. Their numbers were
derived from the `\newtheorem{…}[section]` shared counter (HAND), since nothing was compiled. The smooth-cubic
result is taken as accepted from `B27_COMMON.md` "Accepted, cross-lineage" (READ). Its proof
(B17-01) was not re-read here.

## 2. Edit list (before line → after line)

Line numbers: "before" is the setup commit's blob, "after" is this pass's commit.

### Paper 1 — branch `b27-04-p1`, `paper/det3-conductor.tex` (LF blob; worktree CRLF via autocrlf)

| # | edit | before | after | status |
|---|---|---|---|---|
| P1-1 | Kumar citation: "Kumar's `\cite{KumarCMH,KL}`" → "due to Kumar and to Kumar and Landsberg `\cite{KumarComp,KL}`" | L985 | L985–986 | **APPLIED** (`git apply` clean) |
| P1-2 | IK Lem. 5.2 regime: `$m\ge D$` → `$m\ge D\ge3$` | L156 | L156 | **APPLIED** (clean) |
| P1-3 | IK bibitem: add `arXiv:1911.03990` | L2072 | L2073–2074 | **APPLIED** (clean, offset +1 after P1-1) |

`KumarCMH` is still cited at L121 and L782, so no bibitem became orphaned.

### Paper 2 — branch `b27-04-p2`, `paper/det4-onset.tex` (CRLF blob, `-text`)

| # | edit | before | after | status |
|---|---|---|---|---|
| P2-1a | rename: `$(\star)$ below` → "the length-restriction lemma below" | L1003 | L1010 | **APPLIED** (CRLF diff, clean) |
| P2-1b | rename: "call it `$(\star)$`" → "this is the programme's length-restriction lemma" | L1019–1020 | L1026–1027 | **APPLIED** |
| P2-1c | rename: "analogue of the premise `$(\star)$` of the" → "analogue of the length-restriction lemma used in the" | L1061–1062 | superseded by P2-3 | **APPLIED**, then replaced by P2-3 |
| — | `thm:star` (Thm. 5.1, the reducible criterion; L172, L429, L449, L474) | — | — | untouched, as required |
| P2-2a | `PAPER2_CLAIMS.md` §N append (B26-05) | after L215 | L216–238 | **APPLIED** (clean) |
| P2-2b | `PAPER2_READINESS.md` amendment append (B26-05) | after L62 | L63–98 | **APPLIED** (clean) |
| P2-3 | r = 9 transfer flag removed: "That transfer is the $n=4$ analogue … so this transfer is flagged, not established." → B26-04 §7's proposed sentence, "Here $\Ddet_9$ is exactly the closure … rests only on \cite{LMR}." | L1061–1063 | L1068–1073 | **APPLIED** |
| P2-4a | closure statement: the one-witness ADOPTED wording ("carried in this paper as \emph{adopted} … exhibits a padded smooth cubic threefold $s_5\cdot C^{\ast}$ outside $\Ddet_5$") → the general result `$\ell\cdot C\notin\Ddet_5$` for every smooth cubic $C$ and every nonzero linear form $\ell$, cited `\cite{Companion2}` as a result of this programme; scope stated as geometric non-containment; singular or reducible $C$ explicitly not covered | L536–542 | L536–547 | **APPLIED** |
| P2-4b | G-A1 gap, Rem. 6.3's closing sentence: "used in this paper only as the adopted statement" → rests on the smooth-cubic result, which excludes every $\ell\cdot C$ with $C$ smooth; boundary points with $C$ singular or reducible remain unclassified | L632–634 | L637–641 | **APPLIED** |
| P2-5 | `PAPER2_BLOCKERS.md` new §5 (B5, G-P2-19, B10/G-P2-18, G-A1, B14 dispositions) | after L435 | L436–453 | **APPLIED** |

Notes on P2-3. B26-04 §7 quotes the pre-rename sentence. After P2-1c the lead-in ("…carries the
copy from sixteen variables to $\Ddet_9$.") is byte-identical, and only the flagged sentence
differs, so the replacement maps one-to-one. §7's text is Markdown, so its code spans
`` `\Ddet_9` `` and `` `\overline{\GL_{16}\cdot\det_4}` `` are rendered as TeX math, `$…$`, as the
surrounding TeX requires. No word was changed. `\GL` and `\Ddet` are defined (L18, L37). Every
other use of `eq:lengthred` is unchanged, pending R27-K4.

Notes on P2-4. No slot label was added to the TeX. The binding constraint is echoed as "no
equation of $\Ddet_5$ is known to be nonzero on $\Rr_5$". The sentence "Given it, together with
the dimension gap $39<50$ …" follows unchanged.

### Paper 3 — branch `b27-04-p3`, `papers/det4-blindness/det4-blindness.tex` (LF, `-text`)

| # | edit | before | after | status |
|---|---|---|---|---|
| P3-1a | abstract: "$D=+1$ at every rung $\delta\ge12$, PROVED, with the record's length-restriction lemma …" → "…: PROVED at $\delta=12$, with the record's length-restriction lemma carrying it from nine variables to seven; higher rungs rest on the \texttt{s73} certificates." | L128–129 | L128–129 | **APPLIED** |
| P3-1b | §1: "$D=+1$ at every rung, PROVED via the record's length-restriction lemma, where the comparison has content." → "…at every rung where the comparison has content: PROVED at $\delta=12$ via the record's length-restriction lemma; higher rungs rest on the \texttt{s73} certificates." | L215–216 | L215–216 | **APPLIED** |
| P3-1c | §8: "produces $D=+1$ at every rung, PROVED, as soon as …" → "…at every rung as soon as the comparison has content: PROVED at $\delta=12$; higher rungs rest on the \texttt{s73} certificates." | L1036 | L1036–1037 | **APPLIED** |
| P3-2 | C32 provenance: "Residues still OPEN: Theorem~6's exactness (…; the replay gives a floor only) and C33" → "Theorem~6's exactness, $\dim D_6^{\per_3}=50$, is PROVED: the replay's floor $50$ meets the ceiling $9r-4=50$ at $r=6$ of \cite[Lem.~3.3]{Paper2}. Residue still OPEN: C33" | L810 | L810 | **APPLIED** |
| P3-3a | C02 statement: "$\Pf=R_{135}$ (ADOPTED)" → "(proved: \cite[Thm.~3.1]{Paper2}; Record~\ref{rec:washout})" | L250 | L250 | **APPLIED** |
| P3-3b | C02 provenance label: "$\Pf=R_{135}$: ADOPTED" → "PROVED, \cite[Thm.~3.1]{Paper2} and the $r=5$ case of C32" | L256 | L256 | **APPLIED** |
| P3-3c | C32 provenance label: "PROVED" → "PROVED; also proved in \cite[Thm.~3.1]{Paper2}" | L810 | L810 | **APPLIED** |
| P3-3d | new `\bibitem{Paper2}`, which the citations above need (title from Paper 2's `\title`, in the style of the `Paper1` item) | — | L1209–1211 | **APPLIED** |
| P3-4 | disambiguate the two uses of "35" | — | — | **STOPPED** (§4) |
| P3-5 | C34 provenance: "(Theorem~\ref{thm:cap}, PROVED modulo Kleiman, Dimca and Gulliksen--Neg\aa rd, all three ADOPTED inputs)" → "(Theorem~\ref{thm:cap}), which is PROVED modulo Kleiman and Dimca, both ADOPTED inputs: the Gulliksen--Neg\aa rd assumption is not needed at $n=3$ \cite[Prop.~4.23]{Paper1}" | L840 | L840 | **APPLIED** |
| P3-6 | `CLAIMS.md`: dated header paragraph; rows C02, C32 (two cells), C34, C45; cross-check trap for C11/C34 | L42, 111, 141, 143, 154, 190 | L43–50, 119, 149, 151, 162, 198–203 | **APPLIED** |
| P3-7 | `GAPS.md`: new B27-04 section (G-34 half closed; G-12 at C34; C02/C32; C45; the "35" stop; observation on G-33) | after L162 | L163–182 | **APPLIED** |

## 3. Static checks (receipt `results/b27_04/static_check.txt`)

Script `analysis/b27_04_static_check.py`: `python analysis/b27_04_static_check.py ..` from
`work/batch27/b27-04-p2`. Script sha256 `a64e5da4…`. It was run twice, 0.71 s wall time each.
Run 1 (output `2cd454ed…`, superseded) hashed Paper 1's CRLF worktree rendering. Run 2 (output
`83e08a54…`, the committed receipt) ran after Paper 1's worktree bytes were written as LF (§6).
The check results are identical. Inputs are the three setup-commit blobs and the three worktree after-states, whose
hashes are printed in the receipt. This is a text scan, not a compile.

| check | P1 | P2 | P3 |
|---|---|---|---|
| brace balance | 0 → 0 | 0 → 0 | 0 → 0 |
| `$` parity | even → even | even (1852) → even (1878) | even (2208) → even (2226) |
| `\ref`/`\eqref` undefined | none | none | none |
| `\cite`/`\lit` key without bibitem | none | none | none |
| bibitem never cited | none | none | none (the new `Paper2` is cited) |
| "Claude" outside the acknowledgement | none (1 inside) | none (1 inside) | none |
| slot labels outside the acknowledgement | 0 → 0 | 0 → 0 | 366 → 366 |

Paper 3's 366 slot-label tokens are its established provenance style: every `\prov` line names
its packet. The count is unchanged, and this pass added none to any TeX.

## 4. The STOPPED item: Paper 3 item 4 ("35")

The brief asks to disambiguate "the two uses of '35', with a one-clause gloss at each", from
B26-05. B26-05 §4.2 places the two uses in **different papers**:
- Paper 2's `31 < 35 = dim W`, with the factor fixed;
- Paper 3's `dim T_2 = 35`, affine, with ℓ varying.

Paper 3 contains only the second use: the abstract at L122 and C35 at L856. It never writes
`35 = dim W`. B26-05's own advice is a half-sentence in **Paper 2 Rem. 6.3(iv)**, which is not
among Paper 2's enumerated edits. A gloss "at each" cannot be applied within Paper 3 alone, and
adding one to Paper 2 would go beyond its listed edits. **Stopped on this item. It needs a ruling
on where the gloss goes.** No bytes were changed for it.

## 5. Observations, not acted on

1. **Paper 3 still treats smooth-cubic boundary points as open.** The abstract (L124–127),
   Question 6.5 (its provenance at L918) and `GAPS.md` G-33 say that nothing excludes a boundary point
   `ℓ·C*` with `C*` smooth. The accepted smooth-cubic exclusion, which Paper 2 now cites (P2-4),
   does exclude it. Paper 3 needs a matching edit, which this brief did not authorise.
2. **Gulliksen–Negård at `n = 3` elsewhere in Paper 3.** Abstract (iv) (L118–119) and L896–898
   still carry the three-input label in the `n = 3` cubic-factor context. The brief scoped P3-5 to
   C34.
3. **`PAPER2_GAPS.md`** G-P2-18 and G-P2-19 still describe the before-state. The brief named only
   `PAPER2_BLOCKERS.md`, whose new §5 records the change.
4. **The appended B26-05 texts** in `PAPER2_CLAIMS.md` §N and `PAPER2_READINESS.md` still call
   themselves "PROPOSED, UNCOMMITTED". They were applied verbatim, as instructed. Their row
   J3–J5, and item (1) "stays flagged", are superseded by P2-3 and recorded in BLOCKERS §5.
5. **The `Companion2` locator.** It must actually contain the general smooth-cubic statement. That
   is an [AUTHOR] item, carried in BLOCKERS §5.

## 6. Delivery

**Paper 1 line endings.** The blob is LF (`-text` is not set; `core.autocrlf=true` gives a CRLF
worktree). The worktree bytes were rewritten CRLF → LF before staging, so that
`git hash-object == git hash-object --no-filters`. The blob is the same either way: `e2b1f445…`
(filtered CRLF, filtered LF and unfiltered LF all agree). The manifest's raw sha256 is that of
the LF bytes, which equal the blob.

One commit per branch, pushed to `b27-04-p1`, `b27-04-p2` and `b27-04-p3` only. Each branch
carries `results/b27_04/MANIFEST.json`, which binds its payloads' raw sha256 and bytes and excludes
itself. The commit SHAs are in the final message to the integrator, not in this file. This file
is part of the `b27-04-p2` commit.

## Appendix A. Exact TeX diffs (before = setup commit, after = this commit; `git diff -U0`; CR bytes of Paper 2 not shown)

### b27-04-p1 `paper/det3-conductor.tex`

```diff
diff --git a/paper/det3-conductor.tex b/paper/det3-conductor.tex
--- a/paper/det3-conductor.tex
+++ b/paper/det3-conductor.tex
@@ -156 +156 @@ not on the weight, is a theorem of Ikenmeyer and Kandasamy
-(number of variables) $m\ge D$ (degree): unconditionally for $D$ even, and for
+(number of variables) $m\ge D\ge3$ (degree): unconditionally for $D$ even, and for
@@ -985 +985,2 @@ verified at $n=2$ and, by computer, at $n=4$; the analogous statement for the
-product of variables is Kumar's \cite{KumarCMH,KL}.  For \emph{odd} $n$ the
+product of variables is due to Kumar and to Kumar and Landsberg
+\cite{KumarComp,KL}.  For \emph{odd} $n$ the
@@ -2072 +2073,2 @@ closures via symmetries},
-Proc. 52nd ACM Symposium on Theory of Computing (STOC 2020), 713--726.
+Proc. 52nd ACM Symposium on Theory of Computing (STOC 2020), 713--726;
+arXiv:1911.03990.
```

### b27-04-p2 `paper/det4-onset.tex`

```diff
diff --git a/paper/det4-onset.tex b/paper/det4-onset.tex
--- a/paper/det4-onset.tex
+++ b/paper/det4-onset.tex
@@ -536,7 +536,12 @@ $\Ddet_5\cap W$ may be a limit of determinants that is not itself a
-determinant, and no classification of such boundary points is available here
-(Remark~\ref{rem:noncontain-status}).  The closure statement
-$\Rr_5\not\subseteq\Ddet_5$ is carried in this paper as \emph{adopted}: it is a
-separate, unpublished result of this programme, carried as ADOPTED on the programme's
-record, that exhibits a padded smooth cubic threefold
-$s_5\cdot C^{\ast}$ outside $\Ddet_5$ \cite{Companion2}; it is not a
-consequence of Theorem~\ref{thm:noncontain}.  Given it, together with the
+determinant, and no classification of such boundary points with a singular or
+reducible cubic factor is available here (Remark~\ref{rem:noncontain-status}).
+The closure statement rests instead on a separate result of this programme
+\cite{Companion2}: for every smooth cubic $C\in\Sym^{3}\bC^{5}$ and every
+nonzero linear form $\ell$,
+\[
+  \ell\cdot C\notin\Ddet_5 ;
+\]
+in particular $\Rr_5\not\subseteq\Ddet_5$.  It is not a consequence of
+Theorem~\ref{thm:noncontain}.  Its scope is geometric non-containment only: no
+equation of $\Ddet_5$ is known to be nonzero on $\Rr_5$, and nothing is claimed
+for $\ell\cdot C$ with $C$ singular or reducible.  Given it, together with the
@@ -632,3 +637,5 @@ dimension at least $50+39-70=19$; nothing here excludes one \cite{Companion3}.
-$\dim(\Ddet_5\cap W)$ is established for the determinant part only, and the
-closure statement $\Rr_5\not\subseteq\Ddet_5$ is used in this paper only as
-the adopted statement recorded after Theorem~\ref{thm:noncontain}.
+$\dim(\Ddet_5\cap W)$ is established for the determinant part only.  The
+closure statement $\Rr_5\not\subseteq\Ddet_5$ rests on the smooth-cubic result
+recorded after Theorem~\ref{thm:noncontain} \cite{Companion2}, which excludes
+every point $\ell\cdot C$ with $C$ smooth from $\Ddet_5$; the boundary points
+$\ell\cdot C$ with $C$ singular or reducible remain unclassified.
@@ -1003 +1010 @@ ambient space.  We find
-proved; its one premise beyond the measurements, $(\star)$ below, is itself proved.  The halves are rigorous for
+proved; its one premise beyond the measurements, the length-restriction lemma below, is itself proved.  The halves are rigorous for
@@ -1019,2 +1026,2 @@ programme's isotypic restriction from nine variables to seven, valid for
-$\ell(\lambda)\le7$ and used here at its boundary $\ell(\lambda)=7$; call it
-$(\star)$.  It is not a statement of \cite{LMR}; it is proved in this programme, so the conclusion
+$\ell(\lambda)\le7$ and used here at its boundary $\ell(\lambda)=7$; this is the
+programme's length-restriction lemma.  It is not a statement of \cite{LMR}; it is proved in this programme, so the conclusion
@@ -1061,3 +1068,6 @@ length reduction \eqref{eq:lengthred} carries the copy from sixteen variables to
-$\Ddet_9$.  That transfer is the $n=4$ analogue of the premise $(\star)$ of the
-$n=3$ control above: the $n=3$ case is proved; the $n=4$ case is not yet checked, so
-this transfer is flagged, not established.  (We do not
+$\Ddet_9$.  Here $\Ddet_9$ is exactly the closure of the restrictions of
+$\overline{\GL_{16}\cdot\det_4}$ to a $9$-plane, and the length-restriction lemma holds at
+$(d,N,r)=(4,16,9)$ with the same proof as at $n=3$: weights of coefficient functionals are
+non-negative, the raising operators $E_{i,i+1}$ with $i\ge9$ kill every restricted coefficient,
+independent $9$-tuples are dense in $M_4^{9}$, and complete reducibility holds in characteristic zero.
+So the transfer is proved, and $i_{\det}\ge1$ on $\Ddet_9$ rests only on \cite{LMR}.  (We do not
```

### b27-04-p3 `papers/det4-blindness/det4-blindness.tex`

```diff
diff --git a/papers/det4-blindness/det4-blindness.tex b/papers/det4-blindness/det4-blindness.tex
--- a/papers/det4-blindness/det4-blindness.tex
+++ b/papers/det4-blindness/det4-blindness.tex
@@ -128,2 +128,2 @@ that the instruments work where there is something to see: the unpadded $n=3$ co
-$D=+1$ at every rung $\delta\ge12$, PROVED, with the record's length-restriction lemma carrying it from nine
-variables to seven. We also include one worked example of the method: the
+$D=+1$ at every rung $\delta\ge12$: PROVED at $\delta=12$, with the record's length-restriction lemma carrying it from nine
+variables to seven; higher rungs rest on the \texttt{s73} certificates. We also include one worked example of the method: the
@@ -215,2 +215,2 @@ The instruments are not broken: the positive control of \S\ref{sec:control} show
-$D=+1$ at every rung, PROVED via the record's length-restriction lemma, where the comparison has
-content. The blindness is a property
+$D=+1$ at every rung where the comparison has content: PROVED at $\delta=12$ via the record's
+length-restriction lemma; higher rungs rest on the \texttt{s73} certificates. The blindness is a property
@@ -250 +250 @@ dimension $39$ (affine).
-At five rows the padded permanent restricts to $\Pf=R_{135}$ (ADOPTED). Above five variables
+At five rows the padded permanent restricts to $\Pf=R_{135}$ (proved: \cite[Thm.~3.1]{Paper2}; Record~\ref{rec:washout}). Above five variables
@@ -256 +256 @@ equality holds only at $L=5$. So an evaluation at an arbitrary product above fiv
-\prov{$\Pf=R_{135}$: ADOPTED; $L\ge6$ statement: MEASURED and PROVED}{B22-02 \S0 notation (citing B18-10 \S9) @ \cm{e22a41b1}; B19-12 ledger F7 @ \cm{f008ac39}}{two lineages (B18 slot~10 and integrator); the dimension convention of $10L-5$ is not stated at the source (GAPS G-24)}
+\prov{$\Pf=R_{135}$: PROVED, \cite[Thm.~3.1]{Paper2} and the $r=5$ case of \cid{C32}; $L\ge6$ statement: MEASURED and PROVED}{B22-02 \S0 notation (citing B18-10 \S9) @ \cm{e22a41b1}; B19-12 ledger F7 @ \cm{f008ac39}}{two lineages (B18 slot~10 and integrator); the dimension convention of $10L-5$ is not stated at the source (GAPS G-24)}
@@ -810 +810 @@ $k\le5$. So every $D\ne0$ cell at length $\le5$, in either sign, is a statement
-\prov{PROVED}{\texttt{docs/washout\_lemma.md} \S0, Thm.~2 @ \cm{82633a60}; \texttt{docs/PROVED.md} entries \texttt{washout\_thm2}, \texttt{restriction\_lemma} @ \cm{82633a60}; B23-10 \S7 rank~3, ruling B23-10.18 @ \cm{239dd6e8}}{producer (session 37); re-derived from its generator by B13-07 (per \texttt{PROVED.md}); reviewer B23-10 (INDEPENDENT EVALUATOR, pilot~2, its own code on a fresh seed and two primes: Jacobian ranks $4,10,20,35$ at $r=2..5$ and floor $50$ at $r=6$, matching the recorded table; the restriction lemma, Lemma~1 and Theorems~2--3 re-derived by READ). \textbf{Second lineage closed 2026-09-19.} Residues still OPEN: Theorem~6's exactness ($\dim D_6^{\per_3}=50$; the replay gives a floor only) and \cid{C33}}
+\prov{PROVED; also proved in \cite[Thm.~3.1]{Paper2}}{\texttt{docs/washout\_lemma.md} \S0, Thm.~2 @ \cm{82633a60}; \texttt{docs/PROVED.md} entries \texttt{washout\_thm2}, \texttt{restriction\_lemma} @ \cm{82633a60}; B23-10 \S7 rank~3, ruling B23-10.18 @ \cm{239dd6e8}}{producer (session 37); re-derived from its generator by B13-07 (per \texttt{PROVED.md}); reviewer B23-10 (INDEPENDENT EVALUATOR, pilot~2, its own code on a fresh seed and two primes: Jacobian ranks $4,10,20,35$ at $r=2..5$ and floor $50$ at $r=6$, matching the recorded table; the restriction lemma, Lemma~1 and Theorems~2--3 re-derived by READ). \textbf{Second lineage closed 2026-09-19.} Theorem~6's exactness, $\dim D_6^{\per_3}=50$, is PROVED: the replay's floor $50$ meets the ceiling $9r-4=50$ at $r=6$ of \cite[Lem.~3.3]{Paper2}. Residue still OPEN: \cid{C33}}
@@ -840 +840 @@ nonzero there. Since the cap minors also vanish on every cubic through a plane
-\prov{containment and restriction PROVED. The right-way clause is CONDITIONAL on the cap theorem at $n=3$ (Theorem~\ref{thm:cap}, PROVED modulo Kleiman, Dimca and Gulliksen--Neg\aa rd, all three ADOPTED inputs). The bound $\delta_0\ge8$ is ADOPTED record-internal and holds given the batch-13 measured identity; unconditionally the record has $\delta_0\ge6$ (Record~\ref{rec:delta0}). The resulting degree bound on a separating $f$ is recorded ``because it is proved, not because it is informative''. It is far below the onset conjecture's $>300$, which is an expectation}{B22-02 Lemma~1.6 (L6) @ \cm{e22a41b1}; B22-10 S18 @ \cm{2efb7aaf}}{producer B22-02; reviewer B22-10 (READ + INDEPENDENT hand: the rank-$64$ instance on a generic $D_{35}$ point re-derived from Dimca Thm.~3.1 \lit{Dimca13}{PRIMARY, statement level} and general position; MEASURED rank $64$ on $D_{35}$ and $65$ generic, at single random points. The companion figure ``$64$ on a cubic through a plane'' was one exact rank at one point --- a floor --- and is SUPERSEDED by Proposition~\ref{prop:capplane}, which proves the ceiling for every member; corrigendum K3). The strengthening to $D_{35}\cup\Sigma_\Pi$ is B23-03 \S2.5 @ \cm{3bcad666}, anticipated by B22-10 S18}
+\prov{containment and restriction PROVED. The right-way clause is CONDITIONAL on the cap theorem at $n=3$ (Theorem~\ref{thm:cap}), which is PROVED modulo Kleiman and Dimca, both ADOPTED inputs: the Gulliksen--Neg\aa rd assumption is not needed at $n=3$ \cite[Prop.~4.23]{Paper1}. The bound $\delta_0\ge8$ is ADOPTED record-internal and holds given the batch-13 measured identity; unconditionally the record has $\delta_0\ge6$ (Record~\ref{rec:delta0}). The resulting degree bound on a separating $f$ is recorded ``because it is proved, not because it is informative''. It is far below the onset conjecture's $>300$, which is an expectation}{B22-02 Lemma~1.6 (L6) @ \cm{e22a41b1}; B22-10 S18 @ \cm{2efb7aaf}}{producer B22-02; reviewer B22-10 (READ + INDEPENDENT hand: the rank-$64$ instance on a generic $D_{35}$ point re-derived from Dimca Thm.~3.1 \lit{Dimca13}{PRIMARY, statement level} and general position; MEASURED rank $64$ on $D_{35}$ and $65$ generic, at single random points. The companion figure ``$64$ on a cubic through a plane'' was one exact rank at one point --- a floor --- and is SUPERSEDED by Proposition~\ref{prop:capplane}, which proves the ceiling for every member; corrigendum K3). The strengthening to $D_{35}\cup\Sigma_\Pi$ is B23-03 \S2.5 @ \cm{3bcad666}, anticipated by B22-10 S18}
@@ -1036 +1036,2 @@ section. The same evaluation, transport and certification machinery that is blin
-produces $D=+1$ at every rung, PROVED, as soon as the comparison has content. It
+produces $D=+1$ at every rung as soon as the comparison has content: PROVED at $\delta=12$;
+higher rungs rest on the \texttt{s73} certificates. It
@@ -1207,0 +1209,3 @@ $\delta_0$ bracket's source as ``paper~1'', UNREAD (B22-12 \S3).]
+\bibitem{Paper2} S.~Sethuraman, \emph{The onset of the determinant's five-row ideal, and the
+padded permanent at $n=4$} (paper~2 of this programme).
+
```
