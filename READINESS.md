# B23-05 — Paper 1: submission readiness

The author's judgement is stated as a list of blockers. `det3-conductor.tex` is
**not ready for arXiv**. It becomes ready when these five blockers are cleared:

1. **Attribution (G-P1).** The bracket census, Proposition 4.1, must be
   credited to Bürgisser–Ikenmeyer, Appendix Cor. 7.2 and Prop. 7.3 (as used
   in their Prop. 3.24(3)). The "no computation" framing of Corollary 4.2 and
   of the introduction must then be adjusted to match.
2. **Self-contradiction (G-S1).** Line 617 calls the totals law "verified and
   not proved", against Theorem 5.5.
3. **Paper against record (G-S3).** The paper says the Hüttenhain–Lairez
   derivation of m₂ = 9 was not carried out, while the record's session 10 says
   it was run as a check. One of the two must be corrected.
4. **Refutation count (G-S2).** The count of pre-registered refutations
   disagrees between §7 and Remark 5.11, and within `README.md`.
5. **Unread references.** Before citing them, the author must read Ikenmeyer–
   Kandasamy Lem. 5.2 (which is cited for a specific statement), and must
   either read or drop the "see also" citation to the Hüttenhain thesis. The
   author must also read Landsberg–Manivel–Ressayre (2013) and Kumar
   (Compositio 2015) and decide whether to cite them.

Items that are **not** blockers, because the paper now states them as open in
its own voice (G-A1 to G-A6):

- the three Remark 3.3 items;
- the finite verification behind attainment;
- the computed multiplicity 9 along P₂;
- the primitivity of 𝒩.

A reader should be warned about primitivity in particular: until it is settled,
the headline factorisation −2¹⁶3⁷5³7² carries the Remark 4.7 caveat.

Also left to the author are the pre-existing housekeeping items in the source
header: the MSC codes and the arXiv categories. The source has not been compiled
in this slot, because no LaTeX toolchain is installed. Instead, brace and `$`
balance, label and reference resolution, and theorem numbering were checked by
script, and all are unchanged from HEAD.
