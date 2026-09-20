# Paper 1: submission readiness

`paper/det3-conductor.tex` is **not ready for arXiv**, and what stands between
it and arXiv is now **one signature**.

B23-05 stated five blockers. B24-01 cleared four of them in the paper and
prepared the fifth as an unapplied patch. What follows is the state after that
pass, at HEAD `bbd1d12e80ae162feb368f75c9c270ccf79747f8` with the working tree
carrying the B24-01 edits and nothing committed.

---

## The one thing that remains

**The attribution of Proposition 4.1 to Bürgisser–Ikenmeyer, signed off by the
author.** The edit is written and verified; it is deliberately not applied,
because it is the author's credit line. It is in **`ATTRIBUTION_PATCH.md`**:
exact current text, exact proposed text, the ruling it implements with its
commit, an applying diff, and a paragraph on what signing it concedes.

In short: the bracket census is not the paper's. It is the pigeonhole case of
BI Cor. 7.2 and the counting step of BI Prop. 3.24(3), and `e(det₃) ≥ 18`
follows from BI plus their period theorem alone. It is **not** equivalent to
Cor. 7.2 with Prop. 7.3, as B23-05 alleged — Cor. 7.2 is strictly stronger and
Prop. 7.3 is neither needed nor proved in BI (ruling **B23-10.13**, corrigendum
**K9**, `docs/b23_10_review.md` §4.3–§4.4 at `239dd6e8`). Nothing is retracted:
`e(det₃) = 18` exactly, the one-dimensionality, the value, the divisor, the
semigroup, the conductor, the degree-24 generator and the length theorem are
all untouched. The cost is one paragraph of credit across three passages.

**Say yes and it can be applied in minutes. Say no and what is needed is a
different wording, not a different fact — the ruling is not in doubt.**

---

## The four that are cleared

1. **Self-contradiction at line 617 (G-S1) — fixed.** The sentence calling the
   totals law "verified and not proved" contradicted Theorem 5.5. The *paper*
   was the wrong one of the two: the law became a theorem in session 22
   (`PROJECT_NOTES.md` L422). It now reads as a theorem whose proof consumes
   the two inputs of Lemma 5.6 as given. Edit **Q3**.
2. **Paper against record on m₂ = 9 (G-S3) — fixed.** The paper said the
   Hüttenhain–Lairez derivation "is the obvious next step and we have not
   carried it out". Session 10 of `docs/boundary_deficit.html` says it was run.
   The *paper* was wrong. It now reports what was run and why that does not
   upgrade the label: the degeneration pins only the product `m₂ · c = 18`,
   and the observed contact `c = 2` is also what that product forces from
   `m₂ = 9`, so the two determinations lock each other. **`m₂ = 9` remains
   "computed, not proved".** Edit **Q5**.
3. **The refutation count (G-S2) — fixed by counting, not by hedging.** The two
   numerals were measuring different things, which is why they could not be
   reconciled as they stood. Remark 5.11's scope is the functional, and there
   the answer is **two** pre-registered refutations, (a) and (b); item (c) was
   never pre-registered and was closed by a degree count and a counterexample,
   which the paper now says. §7's scope is every pre-registration behind the
   paper, and there the answer is **five**: those two, the `151,200` arithmetic
   signature, and P3 and P5 of the ternary-cubic ledger. `README.md` now
   matches both. Edits **Q7**, **Q9**, **R7**, **R8**.
4. **The four unread papers — all four read, all four decided, none dropped.**
   Labels, points of use and hashes are in `GAPS.md` §C and `CHANGES.md` §1.
   - **Ikenmeyer–Kandasamy Lem. 5.2:** right in substance, and missing a
     hypothesis. The odd-`D` side condition `C(2(D−1), D−1) ≥ 2(m−1)` is now
     stated. Edit **Q2**.
   - **The Hüttenhain thesis:** the feared collision is not there. It contains
     **no** invariant computation for the det₃ orbit closure at all. Its det₃
     chapter is the CRAS paper plus the traceless-determinant stabiliser and
     the 4×4 boundary, and those two extras are now cited rather than gestured
     at. Edits **Q4**, **Q5**, **Q10**.
   - **Landsberg–Manivel–Ressayre:** cited twice, and the second reason is the
     bigger one. Their Thm 1.0.1 is the `m²/2` bound **for the border
     measure**, so it is the "other means" after Corollary 4.13 and the word
     "classical" was wrong there. And their Prop. 3.5.1 already constructs the
     paper's boundary component `P₂`, for every odd `n`. Edits **Q4**, **Q6**.
   - **Kumar, Compositio 2015:** cited in §1, distinguishing occurrence from
     exact multiplicity. Its results assume `n` **even** and the Alon–Tarsi
     conjecture; here `n = 3` is odd and nothing is conditional. Edit **Q1**.

One item outside the five was cleared too, because B23-10 ranked it with them:
**K10**, the letter in Remark 5.11's retraction sentence, now reads "(a)". Edit
**Q8**.

---

## What the author still decides, none of it a defect

- **The one signature above.** That is the blocker.
- **Two citation questions the reading raised,** both in `GAPS.md`:
  - **G-P4.** Remark 4.14 credits the product-of-variables statement to
    `\cite{KumarCMH,KL}`; Ikenmeyer and Kandasamy credit it to the Compositio
    paper. Settling it needs a read of Kumar CMH 2013 or Kumar–Landsberg 2015,
    which this pass did not do. It is a citation for a specific statement, so
    it should be settled.
  - **G-P5.** Marcus–Minc is load-bearing in the proof of Corollary 4.13 and is
    `UNREAD-CLASSICAL`. Either read it, or accept it explicitly as a standard
    reference. The other unread citations all support framing sentences.
- **Two framing additions, offered and not applied:** G-P2 (the paper's results
  answer BI's Problem 3.23 at `(D, m) = (3, 9)`) and the new **G-P3** (the
  occurrence side has a saturation theorem with a stretching factor, which is
  the dilation analogue of the conductor — a comparison, not a collision).
- **Housekeeping in the source header,** unchanged and pre-existing: the MSC
  codes and the arXiv categories.

## Still open, and staying open

The paper states these in its own voice, and B24-01 closed none of them by
argument (G26):

- the three Remark 3.3 items (G-A1 to G-A3);
- the finite verification behind attainment (G-A4);
- the computed multiplicity 9 along P₂ (G-A6) — and B24-01 **narrows what would
  close it**: the Hüttenhain–Lairez route is spent, so what is needed is an
  independent determination of the contact order, or a proof of the
  unit-factor vanishing at a generic point of P₂;
- the primitivity of 𝒩 (G-A5).

A reader should be warned about primitivity in particular: until it is settled,
the headline factorisation −2¹⁶3⁷5³7² carries the Remark 4.7 caveat.

## How the source was checked

No LaTeX toolchain is installed in this worktree, so it was **not compiled**.
By script, before and after the edits: brace balance (1388/1388) and `$` parity
hold; every `\ref` and `\eqref` resolves; every `\cite` key resolves and every
`\bibitem` is cited, including the two new ones; and the theorem counter,
walked end to end, is **identical to HEAD** — 52 environments, with
`prop:census` = 4.1, `cor:lower` = 4.2, `thm:census` = 4.5, `rem:norm` = 4.7,
`prop:divisor` = 4.8, `cor:perm` = 4.13, `rem:BI` = 4.14, `thm:totals` = 5.5,
`lem:inputs` = 5.6, `rem:arith` = 5.10, `rem:fails` = 5.11. **A real
`pdflatex` run is still owed before posting,** and it is the one check nothing
here substitutes for.
