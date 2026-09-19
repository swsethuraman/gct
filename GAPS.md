# B23-05 — Paper 1: gaps list

Everything here is something the paper wants and the record does not supply,
or a defect found during the pass that falls outside the seven named items. Per
G26, none of these was fixed in the paper. Where a fix is obvious, proposed
wording is given for the author to accept or reject.

## A. Open mathematics (the paper now says "open")

**G-A1 — Remark 3.3 (i): the `V ↔ V*` orientation in World B.** The τ-grading
dictionary was pinned by consistency, using the block-order bound and the
2361-weight regression. It was not pinned by tracking the dualisation through
Peter–Weyl.

- **Record:** `docs/transport_formula.md` §5; `docs/session_23.md` §5 (i).
- **Not closed by:** the dualisation-free rank lemma of `docs/isotypic_rank.md`
  and `docs/session_26.md`. That lemma is for det₃ and does not reach the World
  B torus criterion.
- **Needs:** the bookkeeping itself, which no session has done.

**G-A2 — Remark 3.3 (ii): normality of the Aronhold quartic.** The singular
locus of `{S = 0}` (= σ₂(v₃(P²))) has codimension 3. This is quoted, not
verified, and the paper gives no reference.

- **Needs:** a primary-source citation for the singular locus of the secant
  variety, read under G14. Or verification by the record. Serre's criterion
  then gives normality.

**G-A3 — Remark 3.3 (iii) and Remark 3.2: finiteness of the orphan locus.** The
character estimate is a sketch, and the explicit constant was never computed.
Completeness of the four-element list rests on the sweep `p, q ≤ 150`.

- **Minor record inconsistency:** `docs/session_23.md` §1 describes this range
  as "every λ with λ₁ − λ₃ ≤ 300". `docs/transport_formula.md` §3 says "p, q ≤
  150 (45593 classes, i.e. every λ with λ₁ − λ₃ ≤ 300, by Lemma F)". The two
  regions are not equal, since `p, q ≤ 150` is strictly smaller than
  `p + q ≤ 300`. The paper uses `p, q ≤ 150`, which is the one the sweep
  code's class count supports.

**G-A4 — Theorem 3.1, attainment half.** It is proved modulo an exhaustive
finite verification of 80 exceptional classes, not written as inequalities
(`transport_formula.md` §5). Remark 3.3 now says so. A referee-proof version
needs the chain of inequalities written out.

**G-A5 — Primitivity of 𝒩 (Remark 4.7; the packet's "Remark 4.8").** Open. The
content divides 46,448,640 = 2¹⁴3⁴·5·7, so 18,900 ≤ |Φ₁₈^prim(det₃)| ≤
877,879,296,000. The degree-24 analogue is also open (content | 39,674,880).

- **Consequence:** the headline factorisation −2¹⁶3⁷5³7² in the abstract,
  Theorem 4.6 and Remark 5.10 may be mostly normalisation. So may the 75,600
  signature, which rescales with the content.
- **To settle it:** coefficients of Φ₁₈ off the six-parameter family, which
  needs a general-support evaluator (br2.c handles only the six permutation
  monomials). Or, at the extreme of the bound, an explicit integral F with
  𝒩 = 46,448,640·F.
- **Record:** `PROJECT_NOTES.md` session 23 (5); `docs/primitivity.md`.

**G-A6 — m₂ = 9 along P₂ (Proposition 4.8).** Computed under the assumption of
unit-factor vanishing at a generic point of P₂, which is not proved there. The
paper now labels it computed.

- **Needs:** a proof of the P₂ multiplicity, for example from the
  Hüttenhain–Lairez degeneration via Jacobi's formula.
- **Related:** G-S3.

## B. Defects found outside items 1–7 (not edited; wording proposed)

**G-P1 — The bracket census is in Bürgisser–Ikenmeyer (PRIMARY; read this
pass).** This is the most serious finding.

- **What BI prove:** BI, arXiv:1511.02927, Appendix 7 (§7.1 "Plethysms").
  - Prop. 7.1 and Cor. 7.2: for D odd and m | dD, the dimension of the SL_m
    invariants in O(Sym^D C^m)_d is at most the number of cardinality-d *sets*
    of D-subsets of {1,…,dD/m} in which each number occurs in exactly m
    subsets.
  - Prop. 7.3 strengthens this to exclude two numbers occurring in the same
    columns.
  - Prop. 3.24(3) applies it, as "there are only C(2D,D) cardinality-D subsets".
- **Why it matters:** if d > C(dD/m, D), no such set exists. That is exactly
  paper Proposition 4.1 (Bracket census), under the same odd-D hypothesis.
  Corollary 4.2 (e(det₃) ≥ 18) then follows from BI Cor. 7.2 directly.
- **What the paper claims:** it presents the census as its own ("A second,
  entirely elementary constraint … it extends the argument by which Howe
  disposes of δ = m"), with a proof from the first fundamental theorem. BI's
  own proof goes through the transposed-plethysm weight space, a different
  route to the same bound.
- **Proposed wording** (for the author; not applied): after "we state it in
  general because the statement costs nothing extra", add:

  > "The bound is equivalent to the case of Bürgisser and Ikenmeyer's plethysm
  > estimate \cite[Cor.~7.2 and Prop.~7.3]{BI} in which no admissible set
  > exists, and is the mechanism of \cite[Prop.~3.24(3)]{BI}; we include the
  > bracket-monomial proof because it is short and self-contained."

  Also soften "Corollary 4.2 … with no computation" and the intro's "an
  elementary parity count … already excludes every smaller degree" to credit
  BI.
- **Status:** the novelty claims that survive are e(det₃) = 18 exactly, the
  one-dimensionality, the value, and everything after. Those are untouched.
- **Blocker:** yes.

**G-P2 — BI Problem 3.23 (PRIMARY; read this pass).** BI ask: "In which degree
does the generic fundamental invariant appear for odd D and arbitrary m?"

- **What the paper's results imply:** for (D, m) = (3, 9), no invariant below
  degree 18 (census), a one-dimensional ambient space at 18 (Theorem 4.3), and
  Φ₁₈(det₃) ≠ 0. Together these give e(3, 9) = 18.
- **Record basis:** `docs/conductor.html` §5, "det₃ achieves the generic
  minimum"; `docs/boundary_deficit.html` session 11, "18 is provably the first
  degree any cubic in nine variables admits".
- **What the paper does not do:** it never states this or connects it to
  Problem 3.23.
- **Proposed:** one sentence in Remark 4.14 `rem:BI`. The author decides. This
  is a new *framing* of existing results, not new mathematics.
- **Blocker:** no.

**G-S1 — Stale sentence, paper line 617 (`thm:census` dependencies
paragraph).** It reads: "The gauge law of Section 5, which is verified and not
proved, and the covariance hypotheses refuted there, enter nowhere in this
section."

- **Why it is stale:** since `d9606d93` (the totals law becomes a theorem) this
  contradicts Theorem 5.5. `git log -S` shows the sentence dates from
  `d9bb2723`, which is earlier.
- **Proposed:**

  > "The totals law of Section 5 --- a theorem, but one whose proof consumes
  > the inputs of Lemma 5.6 as given --- and the covariance hypotheses refuted
  > there, enter nowhere in this section."

- **Authorised by:** `PROJECT_NOTES.md` status "SESSION 22 … is a THEOREM",
  and session 22's "the two consumed inputs … were used as given, not
  re-derived".
- **Blocker:** yes, because it is a self-contradiction a referee will find.

**G-S2 — "Two" against "Three" pre-registered refutations.** The same count
disagrees within each file:

- **Paper:** §7 says "Two of the hypotheses so registered were refuted
  (Remark 5.11)". Remark 5.11 says "Three hypotheses … were pre-registered and
  then refuted".
- **README:** l.79 says "Three". l.183 says "Two".
- **More refutations:** the record has further pre-registered refutations. One
  is `rem:arith`'s 151,200 (pre-registered prediction 4 in
  `results/PREREG_Xm3.md`). Others are P3 and P5 of session 23
  (`docs/session_23.md` §4).
- **What is missing:** the record does not say whether (c) was pre-registered.
  So the right number cannot be set from the record.
- **Proposed:** the author states the count from the pre-registration commits,
  or drops the numeral ("the hypotheses so registered that were refuted
  (Remarks 5.10, 5.11) …").

**G-S3 — The P₂ derivation from Hüttenhain–Lairez.** The paper says deriving
m₂ = 9 from HL's degeneration via Jacobi's formula "is the obvious next step
and we have not carried it out".

- **What the record says:** `docs/boundary_deficit.html` §W3 session 10 ("m₂ =
  9, now on two legs", `350825ae`) reports running the machinery over that
  degeneration. It found det L(t) = −64t⁶, a Jacobi limit reproducing P₂, and
  contact 2. It records "upgraded from derived to confirmed". `conductor.html`
  §5.4 says "confirmed against Hüttenhain–Lairez's explicit degeneration".
- **Why the paper's label was kept:** that session's two determinations "lock
  each other" through m₂·contact = 18. As written, contact = 2 is partly
  inferred from m₂ = 9. G26 forbids upgrading a label, so the more
  conservative label stays.
- **What the author must decide:** either the sentence "we have not carried it
  out" is corrected to describe the session-10 consistency check (which stays a
  consistency check, not a proof), or the session-10 claim is withdrawn in the
  record.
- **Blocker:** yes, since the paper and the record disagree on a fact.

**G-S4 — Record file still asserts 151,200.** `docs/primitivity.md` lines
203–210 ("151,200 … divides every measured det₃ evaluation") is stale against
the session-23 correction. It is not a paper file, so it is out of scope for
this slot. Noted for whoever next touches the record.

## C. Prior-art pass (item 6)

Labels follow G14/G14′:

- **PRIMARY:** the primary source was read, in this pass or in a record line
  that says so.
- **SECONDARY:** known only via an abstract, search snippet or secondary
  account.
- **UNREAD-CLASSICAL / UNREAD-SPECIALIST:** not read.

An unread item is cited as unread or not cited. The search was run on the web
on 2026-09-18. Several searches for a published value of e(det₃), or a degree-18
invariant on the det₃ orbit closure, found none. The only hit is this project's
own public repository. MathSciNet was not available, so that is still unchecked,
as it was in the record's August pass (`docs/conductor.html` §7).

### Already cited in the paper

| Ref | Label | Basis | Finding |
|---|---|---|---|
| BI, *Fundamental invariants of orbit closures* (J. Algebra 477, 2017; arXiv:1511.02927) | **PRIMARY** | Full text read this pass. | These cited statements check out: Thm 2.5 (period 2 for n ≡ 2, 3 mod 4), Cor 2.9, Thm 3.4, Prop 3.9, Thm 3.14 (Howe), Thm 3.15 (strict for D odd), Prop 3.28, and the n = 4 computer verification. Two new items are G-P1 (Cor 7.2 is the bracket census) and G-P2 (Problem 3.23). One small point: BI settle n = 2 via the quadratic form (Remark 3.27, Thm 3.18), not via the admissible-table count. The paper's Remark 4.14 says the criterion is "verified at n = 2", which is harmless but loose. |
| Hüttenhain–Lairez, CRAS 2016 | **PRIMARY** | Per record: "fetched" (`boundary_deficit.html` session 10); "Primary background checked online" (`post_b19…/extension_descent_20260916/REPORT.md` l.250). | None. |
| Kumar, CMH 2013 (non-normality) | **PRIMARY** | Per record: the same REPORT.md l.250. | None. |
| Dimca 2013 Thm 3.1; Kleiman 1974 | **PRIMARY** | Per record: "both clauses read in the primary source" (`claude_gkz_incidence_20260917/REPORT.md` §8). | None. |
| Bremner–Hu–Oeding 2014 | **SECONDARY** | The record uses the 1152-monomial count (`docs/i6_identification.md`); a full read is not documented. | None. |
| Beauville 2000; AFPRW 2019; Nurmiev 2000; Kraft 1984; Weyl 1939; Marcus–Minc 1961; GKZ 1994 | **UNREAD-CLASSICAL** as far as the record documents | Cited for standard facts. | They are cited for classical statements. The paper should either confirm them against the sources or keep them as standard references. |
| MS 2001; BIP 2019; IK 2020; DM 2017; KL 2015; Landsberg 2017; LR 2016; Hüttenhain thesis 2017 | **UNREAD-SPECIALIST** as far as the record documents | Cited as motivation or context, except IK Lem 5.2, which is cited for a specific statement. | IK Lem 5.2 is cited for a specific statement, so a primary read is needed before submission. The thesis `Hue` is cited "see also" and not read. It is the most likely place for a det₃ orbit-closure computation the paper should distinguish. |

### Not cited; candidates

| Item | Label | Why it may matter | Recommendation |
|---|---|---|---|
| Landsberg–Manivel–Ressayre, *Hypersurfaces with degenerate duals and the GCT program*, CMH 88 (2013); arXiv:1004.4802 | **SECONDARY** (abstract only) | The abstract states a quadratic lower bound on the determinantal *border* complexity of the permanent. If it is the m²/2 bound, then per₃ ∉ 𝒪 follows immediately. The paper calls this "classical and easy by other means" and cites nothing. | Read it, then cite it as the "other means" in the sentence after Corollary 4.13. Until read, do not cite, per G14. |
| Kumar, *A study of the representations supported by the orbit closure of the determinant*, Compositio 151 (2015); arXiv:1109.5996 | **SECONDARY** (abstract only) | It concerns which irreducibles occur in ℂ[𝒪(det_n)], the closure side the paper's deficits measure. It is conditional on Alon–Tarsi. | Read it. It probably deserves a sentence in §1 distinguishing occurrence results from the exact multiplicities and deficits computed here. |
| Bürgisser–Hüttenhain–Ikenmeyer, *Permanent versus determinant: not via saturations*, PAMS 145 (2017) | **UNREAD-SPECIALIST** | It is BI's ref. [4], and it bears on the multiplicity programme. | Low priority. |
| Dörfler–Ikenmeyer–Panova, multiplicity against occurrence obstructions (2019/20) | **UNREAD-SPECIALIST** (from memory; not searched) | This is the closure-multiplicity side of GCT that the deficits contribute to. | Check it before submission. |

Nothing found contradicts a result of the paper. The one attribution defect is
G-P1.
