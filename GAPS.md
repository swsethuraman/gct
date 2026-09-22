# Paper 1: gaps list

Everything here is something the paper wants and the record does not supply,
or a defect found during a pass that fell outside its named items. Where a fix
is obvious, proposed wording is given for the author to accept or reject.

**Updated by B24-01, 2026-09-19.** Entries now carry a status line. Four of the
five submission blockers are **CLOSED in the paper**: G-S1, G-S2, G-S3, and the
prior-art reads of section C. G-P1, the attribution, is **PREPARED AND
UNAPPLIED** in `ATTRIBUTION_PATCH.md` and is the only blocker left; it waits on
the author's signature. The open-mathematics entries G-A1 to G-A6 are untouched
— B24-01 proved nothing and closed nothing by argument, per G26. Three new
entries, G-P3 to G-P5, came out of the prior-art reads; none is a blocker.

> **B25-03 update, 2026-09-21 UTC (UNCOMMITTED; the B24-01 text is kept).**
> (i) "G-P1 … is the only blocker left" is **withdrawn**. The enumerated
> pre-posting list is in `READINESS.md` and `docs/b25_03_report.md` §4.
> (ii) The LMR Prop. 3.5.1 row of the blocker-5 table below is now
> **PRIMARY, read by B25-03**. It uses arXiv:1004.4802v1, PDF SHA-256
> `cfc28275a8c6b27f0ad6946d495ed4f889f7617df479be943d8d35718dbf2d79`, with the
> text read from the ar5iv rendering `fb5844ad…`. The quotes are in
> `results/b25_03/lmr_prop351_quotes.md`. The finding is **confirmed and
> narrowed**: LMR construct `P_Λ` and prove the component statement for odd
> `n`. The equality of its orbit closure with `P₂` at `n = 3` is B25-03's
> hand check, not a statement printed in LMR. The thesis sentence quoted
> below was not re-read. (iii) The IK, Kumar-Compositio and Hüttenhain rows
> are still B24-01 readings with no packet (B24-10 §4.1). B25-03 did not
> re-read them. (iv) G-P1: `ATTRIBUTION_PATCH.md` is re-bound to
> `bc7e62b7`, with one wording flag in its §6.

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

- **Needs:** a proof of the P₂ multiplicity. **B24-01 narrows what would
  count.** The Hüttenhain–Lairez degeneration on its own does *not* suffice
  and is no longer the open route it looked like: it has been run (session 10),
  and what it yields is the product `m₂ · c = 18` with `c` the contact order.
  Closing G-A6 by that route therefore needs an **independent determination of
  the contact order** — one that does not read `c = 2` back off `m₂ = 9`.
  Failing that, it needs either a proof of the unit-factor vanishing at a
  generic point of P₂, which is the assumption the torus-integrality
  computation makes, or a direct multiplicity computation on the non-normal
  component.
- **Related:** G-S3, now closed; the mathematics it exposed is this entry.

## B. Defects found outside items 1–7 (not edited; wording proposed)

**G-P1 — The bracket census is in Bürgisser–Ikenmeyer (PRIMARY; read by
B23-05, and read in full independently by B23-10).** This is the most serious
finding.

> **STATUS (B24-01): PREPARED, NOT APPLIED. The only blocker left.**
> B23-10 ruled on this at `239dd6e8` (§4.3, ruling **B23-10.13**) and the
> ruling is **narrower** than the allegation below. Prop. 4.1 is **not
> equivalent** to Cor. 7.2 with Prop. 7.3; it is the **pigeonhole case** of
> Cor. 7.2 and exactly the counting step of Prop. 3.24(3). Cor. 7.2 is
> strictly stronger, because it also imposes regularity, and **Prop. 7.3 is
> neither needed nor proved in BI**. Corrigendum **K9** replaces the proposed
> wording below with B23-10 §4.4's. The whole edit — the credit sentence, the
> change to Corollary 4.2, and the change to the introduction — is written out
> as exact current text, exact proposed text and an applying diff in
> **`ATTRIBUTION_PATCH.md`**. It was deliberately **not applied**: by the
> user's decision of 2026-09-19 this is the author's credit line and the
> author signs it off. The wording proposed at the end of this entry is
> **superseded by K9** and is kept only so the correction is visible.

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
paragraph).** It read: "The gauge law of Section 5, which is verified and not
proved, and the covariance hypotheses refuted there, enter nowhere in this
section."

> **STATUS (B24-01): CLOSED.** Fixed in the paper as edit **Q3** of
> `CHANGES.md` Part I, in the wording proposed below. The paper was the wrong
> one of the two, not Theorem 5.5: the totals law became a theorem in session
> 22 (`PROJECT_NOTES.md` L422), and the sentence predates that. The sentence
> is now at line 627 of the edited source; line 617 is its position at
> `82633a60`.

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
disagreed within each file:

> **STATUS (B24-01): CLOSED, and the count was settled from the record rather
> than by dropping the numeral.** Fixed as edits **Q7** (Remark 5.11), **Q9**
> (§7) and **R7**, **R8** (`README.md`). The two numerals were measuring two
> different things, which is why they could not be reconciled as they stood:
>
> - **Remark 5.11's scope is the functional.** There the answer is **two**,
>   not three. `PROJECT_NOTES.md`'s session-16 header says "**two**
>   receiving-space hypotheses falsified by their own pre-registered tests",
>   and those are (a) and (b). Item (c) was never pre-registered: the record
>   for it is session 18 and `docs/psi_identification.md`, "The plane-cubic
>   hypothesis is DEAD (two independent proofs) — (a) Degree count … (b)
>   Explicit counterexample", which is not a test against a logged prediction
>   and is not "a single number". The paper now says which of the three was
>   pre-registered and which was not.
> - **§7's scope is every pre-registration behind the paper.** There the
>   answer is **five**, not two: the two above, plus the `151,200` arithmetic
>   signature (`results/PREREG_Xm3.md` prediction 4, refuted in session 23),
>   plus P3 and P5 of `docs/session_23.md` §4, whose own line reads "Two
>   pre-registered hypotheses refuted (P3, P5), both kept."
>
> So the open question this entry raised — whether (c) was pre-registered —
> **is answered: the record does not record it as one, and the paper now says
> so explicitly rather than counting it.** That is a statement about the
> record, not a claim that no such pre-registration was ever made off the
> record.

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

**G-S3 — The P₂ derivation from Hüttenhain–Lairez.** The paper said deriving
m₂ = 9 from HL's degeneration via Jacobi's formula "is the obvious next step
and we have not carried it out".

> **STATUS (B24-01): CLOSED. The paper was wrong, not the record.** Session 10
> of `docs/boundary_deficit.html` ran the degeneration, and says so in detail
> — `det L(t) = −64t⁶`, the Jacobi limit reproducing the P₂ representative,
> contact 2. So the paper's "we have not carried it out" was false, and it is
> the loser. Fixed as edit **Q5**, which writes out what session 10 did and
> then says why it does not upgrade the label: the family determines only the
> product `m₂ · c = 18`, and the observed contact `c = 2` is also what that
> product forces from `m₂ = 9`, so the two determinations lock each other
> instead of being independent. **`m₂ = 9` therefore stays "computed, not
> proved"** — the label was not upgraded, per G26. The underlying mathematical
> gap is unchanged and stays open as **G-A6**.

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

**G-P3 — The thesis's saturation theorem is the occurrence-level analogue of
the deficit, and the paper does not mention it (found by B24-01).** Hüttenhain
Thm 4.1.2: for `d > 2`, the saturation of the weight semigroup `Λ⁺(D_d)` of the
determinant orbit closure contains every `λ` with `ℓ(λ) ≤ d` and `|λ| ∈ dZ`;
"hence occurrence obstructions must be **gaps** of `Λ⁺(D_d)`". Kumar's
conditional Thm 4.1.3 is the other half, with a "stretching factor" of `d`.

- **Why it may matter:** gaps of the weight semigroup are the occurrence-level
  shadow of the paper's multiplicity deficit, and "stretching factor" is the
  dilation analogue of the conductor's ray index. The two operations are
  genuinely different — `λ ↦ kλ` against `λ ↦ λ + 6k·1₉` — so this is a
  comparison, not a collision.
- **Proposed** (not applied): one sentence in §1 or in Remark 4.14 noting that
  the occurrence side has a saturation statement with a stretching factor,
  while the conductor measures depth along the semiinvariant ray, and that the
  two indices are not the same number.
- **Blocker:** no. It is framing, like G-P2, and the author decides.
- **Source:** Hüttenhain thesis Thm 4.1.2 and §4.1.1, read by B24-01
  (sha256 `ccf1a13e…`). The published form is Bürgisser–Hüttenhain–Ikenmeyer,
  PAMS 145 (2017), still **UNREAD-SPECIALIST**.

**G-P4 — Remark 4.14's citation for the product of variables may be the wrong
Kumar paper (found by B24-01).** The remark says "the analogous statement for
the product of variables is Kumar's `\cite{KumarCMH,KL}`". Ikenmeyer and
Kandasamy attribute that statement — `mult_{(m)*} ℂ[G(x₁⋯x_m)‾] ≥ 1`, and the
same at `(m×m)`, under the Alon–Tarsi condition — to `[Kum15]`, which their
bibliography gives as **Compositio 151 (2015)**, the paper newly cited here as
`KumarComp`, not as CMH 2013.

- **What is not settled:** the Compositio paper's own text never mentions
  `x₁⋯x_m`; its variety `𝒳` is the determinant's orbit closure throughout. So
  either IK are compressing a consequence, or the statement lives in one of
  the other two Kumar papers. **Not resolved here, and not edited**, because
  resolving it needs a read of Kumar CMH 2013 and of Kumar–Landsberg 2015,
  neither of which this pass did.
- **Blocker:** no, but it is a citation for a specific statement, so it should
  be settled before submission.
- **Source:** IK §5, "Kumar proved [Kum15] that …", with IK's bibliography
  entry `[Kum15]`; both read by B24-01 (sha256 `a34b735c…`).

**G-P5 — Two unread citations are still cited for specific statements.** After
this pass the `UNREAD-SPECIALIST` list is MS 2001, BIP 2019, DM 2017, KL 2015,
Landsberg 2017 and LR 2016, and the `UNREAD-CLASSICAL` list is unchanged. Every
one of them supports a framing sentence rather than a step in a proof, with one
exception now flagged: **`KL` via G-P4**. `MM` (Marcus–Minc) is load-bearing in
the proof of Corollary 4.13 and is `UNREAD-CLASSICAL`.

- **Needs:** either a primary read of Marcus–Minc 1961, or an explicit note
  that it is being taken as a standard reference. It is a 1961 result in the
  literature for sixty-five years and is not in doubt; the point is only that
  G14′ asks for the label to be honest.
- **Blocker:** the author's call. It is listed in `READINESS.md` as a decision,
  not as an unresolved defect.

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
| IK 2020 (`IK`) | **PRIMARY**, read by B24-01 | See the blocker-5 table below. | Kept, with its hypothesis corrected (edit Q2). |
| Hüttenhain thesis 2017 (`Hue`) | **PRIMARY**, read by B24-01 | See the blocker-5 table below. | Kept and promoted from "see also" to two cited statements (edits Q4, Q5). |
| MS 2001; BIP 2019; DM 2017; KL 2015; Landsberg 2017; LR 2016 | **UNREAD-SPECIALIST** as far as the record documents | Cited as motivation or context only. Each supports a framing sentence, not a step in a proof. | Still unread. None of them is cited for a specific statement the paper relies on, so none is a blocker; they are marked unread here, which is what G14′ requires of an unread citation. If any is to be cited for a statement rather than for context, it must be read first. |

### Not cited; candidates

| Item | Label | Why it may matter | Recommendation |
|---|---|---|---|
| Landsberg–Manivel–Ressayre, *Hypersurfaces with degenerate duals and the GCT program*, CMH 88 (2013), no. 2, 469–484; arXiv:1004.4802 | **PRIMARY**, read by B24-01 | As anticipated, and more. | **Now cited**, in two places: edits Q4 and Q6. See the blocker-5 table. |
| Kumar, *A study of the representations supported by the orbit closure of the determinant*, Compositio 151 (2015), 292–312; arXiv:1109.5996 | **PRIMARY**, read by B24-01 | As anticipated. | **Now cited** in §1: edit Q1. See the blocker-5 table. |
| Bürgisser–Hüttenhain–Ikenmeyer, *Permanent versus determinant: not via saturations*, PAMS 145 (2017) | **UNREAD-SPECIALIST** | It is BI's ref. [4], and it bears on the multiplicity programme. | Low priority. |
| Dörfler–Ikenmeyer–Panova, multiplicity against occurrence obstructions (2019/20) | **UNREAD-SPECIALIST** (from memory; not searched) | This is the closure-multiplicity side of GCT that the deficits contribute to. | Check it before submission. |

Nothing found contradicts a result of the paper. The one attribution defect is
G-P1.

### Blocker 5, settled: the four papers, read and decided (B24-01)

Labels are per point of use, with the sha256 of the bytes read; the full fetch
table is `CHANGES.md` Part I §1. All four were read in this pass and all four
are **PRIMARY**. No citation had to be dropped.

| paper | point of use | decision |
|---|---|---|
| **Ikenmeyer–Kandasamy**, STOC 2020, arXiv:1911.03990. sha256 `a34b735c…` | §1, `\cite[Lem.~5.2]{IK}`, for the existence of a uniform conductor bound for power sums | **KEEP, corrected.** Lemma 5.2 does say what the paper says: at the shifted weight `λ + (m×eD)` the closure multiplicity equals the orbit multiplicity, with `e` given explicitly in terms of `d`, `m`, `D` and **not** of `λ` — which is what "uniform" was doing, and it is right. The regime is right too: IK set `p := x_1^D + … + x_m^D` "for `m ≥ D`". Two corrections, both made (edit Q2): the paper omitted the **odd-`D` side condition `C(2(D−1), D−1) ≥ 2(m−1)`**, which bounds `m` above and so is a real restriction; and "uniform bound" is clearer said as "depending only on the degree and not on the weight". "Makes no optimality claim" stands — the tightness remark inside IK's proof is about the combinatorial quantity `e_ϱ`, not about minimality of the shift. |
| **Hüttenhain**, TU Berlin thesis 2017, doi:10.14279/depositonce-6032. sha256 `ccf1a13e…` | was a bare "see also" beside `\cite{HL}` | **KEEP, and now used.** The fear behind this item does not materialise: **the thesis contains no computation of invariants of the det₃ orbit closure at all** — no fundamental invariant, no invariant degree, no `SL₉`-invariant ring. Its det₃ chapter (Ch. 8) opens "These results have been previously published in [HL16]", so on the boundary it is the CRAS paper plus two extras: §8.3, the stabiliser of the traceless determinant and the corollary that its orbit closure is a boundary component for **all** `d ≥ 3`; and §8.4, the 4×4 boundary. Both extras are now cited (edits Q4, Q5), and the DOI was added so they are locatable (Q10). |
| **Landsberg–Manivel–Ressayre**, CMH 88 (2013). sha256 `fb5844ad…` | was uncited | **CITE, in two places.** (i) Theorem 1.0.1 **is** the `m²/2` bound and it is for the **border** measure: `dc̄(perm_m) ≥ m²/2`, hence `dc̄(per₃) ≥ 5 > 3`. That is exactly the "other means" the paper waved at after Corollary 4.13, and the paper's "classical" was wrong — LMR say in their own §1 that before them "the best known lower bound on this function had been linear", the `m²/2` bound of Mignon–Ressayre being for `dc`, not `dc̄`. This is the `dc`/`dc̄` distinction of ruling B23-10.23, and edit Q6 makes it. (ii) **A second and larger find:** LMR Prop. 3.5.1 already constructs the paper's boundary component `P₂`, for every odd `n`, as `P_Λ(M) = det_n(A,…,A,S) = Σ s_ij Pf_i(A) Pf_j(A)`, and proves its orbit closure is an irreducible codimension-one component of the boundary not contained in `End·det_n`. At `n = 3` this is the universal quadric verbatim. The thesis says so itself, in the line after its own construction of `Q₂`. Edit Q4 credits it. |
| **Kumar**, Compositio 151 (2015). sha256 `7eeacd13…` | was uncited | **CITE, one distinguishing sentence in §1** (edit Q1), as anticipated. Its principal result, Cor. 6.2, is an **occurrence** statement: `V_E(mλ)` occurs in `ℂ[𝒳]` with nonzero multiplicity for every `λ` of length ≤ `m`. It carries two hypotheses the paper does not: **`m` is even** ("From now on, `m` is an even positive integer", after Cor. 2.4), and **the column Latin `(m,m)`-square conjecture**, i.e. Alon–Tarsi. Both matter here: `n = 3` is odd, which is exactly the case Kumar's argument excludes, and nothing in this paper is conditional. Its Prop. 2.3, quoted from Howe, is the same vanishing the paper already cites through BI Thm 3.14/3.15 — `[S^ℓ(S^m E)]^{SL(E)} = 0` for `0 < j < ℓ`, and `0` at `j = ℓ` when `m` is odd — so there is no conflict with the census, only a second route to the same classical fact. |
