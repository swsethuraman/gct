# Paper 1: change ledger

Two passes are recorded here. **Part I** is B24-01, which cleared four of the
five submission blockers and prepared the fifth. **Part II** is the earlier
B23-05 finishing pass, kept unedited except where B23-10 §6.2 corrected it;
those corrections are recorded in Part I §4 and not applied in place.

---

# PART I — B24-01: clearing the five blockers

Worktree `C:\Users\swami\Projects\gct-gpt\work\batch15_workers\B23-05`, branch
`b23-05-paper1`.

- **HEAD at start:** `bbd1d12e80ae162feb368f75c9c270ccf79747f8`. This matches
  the packet. Unchanged at end.
- **`git status --porcelain` at start:** empty. At end: `M README.md`,
  `M paper/det3-conductor.tex`, `?? ATTRIBUTION_PATCH.md`.
- **Git use:** read-only. Nothing was committed, staged or stashed.
- **Pre-edit sha256:** `paper/det3-conductor.tex` =
  `11e34759afd29b532d9420c5fdab6275d607f4c609a668b9ac0501377fb54c2b`,
  `README.md` =
  `60b07db6da34c17f743be398fb97316c7b558278becd7e8ec7bd535940da7ac4`.
- **Post-edit sha256:** `paper/det3-conductor.tex` =
  `b911a15184ebf819301deddfc178d76a5d9a6d01b881d5fc64b32a8982457445`,
  `README.md` =
  `5ba2586a7f312be99fb6f6e231e95461a17acdc2c1c3e0fccdfc4c8427eeb617`.
- **Hunk count:** `git diff HEAD -U0 -- paper/det3-conductor.tex` has
  **12 hunks**, and `README.md` has **4**. Every one is a row below.
- **Blocker 1 was not applied.** It is prepared as `ATTRIBUTION_PATCH.md`.
  `paper/det3-conductor.tex` contains none of it; the patch's own diff is
  verified by `git apply --check` against the post-edit file.

## 1. Sources read in this pass (G14/G14′)

All four are labelled **PRIMARY** from this pass. No LaTeX toolchain and no
PDF-to-image tool is installed here; the three arXiv items were read as the
ar5iv HTML rendering, and the thesis as `pdftotext` output of the DNB copy.
The files live in this session's scratchpad, which does not survive the
session; the URL and hash below are what lets anyone refetch and re-verify.

| source | fetched from | sha256 of the bytes fetched |
|---|---|---|
| Ikenmeyer–Kandasamy, STOC 2020, arXiv:1911.03990 | `ar5iv.labs.arxiv.org/html/1911.03990` | `a34b735c3b5c9a101300aac5a750367e91ed6ae463c866d05db7a4c617896d18` |
| Landsberg–Manivel–Ressayre, CMH 88 (2013), arXiv:1004.4802 | `ar5iv.labs.arxiv.org/html/1004.4802` | `fb5844ada6bec339638b584bcf385686935e96e03aa8f0ab9e2561bb0b316e05` |
| Kumar, Compositio 151 (2015), arXiv:1109.5996 | `ar5iv.labs.arxiv.org/html/1109.5996` | `7eeacd13f1578c3cf3d676c655013c09f00864e27f7b1f5faf416b2dc5521029` |
| Hüttenhain, TU Berlin thesis 2017, doi:10.14279/depositonce-6032 | `d-nb.info/1156010608/34` (PDF) | `ccf1a13e6b8c0d9ee25f0a85616eb47232bf90bdad0b03bb9169ee91e7609edd` |

Bürgisser–Ikenmeyer (arXiv:1511.02927) was **not** re-read here; it was read in
full by B23-10, whose hashes are in `docs/b23_10_review.md` §4.1 at
`239dd6e8`. Nothing in this pass rests on a fresh reading of it.

## 2. Paper edits (`paper/det3-conductor.tex`), one row per hunk

| # | Blocker | Where | What changed | Authorising record line |
|---|---|---|---|---|
| Q1 | 5 (Kumar) | §1, after "…not to suffice \cite{BIP}" | Adds three sentences: what is known on the closure side is mostly occurrence and conditional — for **even** `n`, and assuming Alon–Tarsi in its column-Latin-square form, Kumar shows `V(nλ)` occurs in `ℂ[Ω̄(det_n)]` for every `λ` of length ≤ `n` — and that this paper differs on all three counts, `n = 3` being odd, the case that argument excludes. | `GAPS.md` §C, "Not cited; candidates", Kumar row: "Read it. It probably deserves a sentence in §1 distinguishing occurrence results from the exact multiplicities and deficits computed here." Source: Kumar Cor. 6.2, with Thm 6.1's "Assume, as above, that `m` is even. Assume further that the column Latin `(m,m)`-square conjecture 4.3 is true", and "From now on, `m` is an even positive integer" after Cor. 2.4. |
| Q2 | 5 (IK) | §1, the `\cite[Lem.~5.2]{IK}` sentence | "at an explicit uniform bound" becomes "at an explicit bound depending only on the degree and not on the weight"; the regime is named as `m ≥ D` with the power sum written out; and the **odd-`D` side condition `C(2(D−1), D−1) ≥ 2(m−1)`** is stated, which the paper had omitted. | `READINESS.md` blocker 5 and `GAPS.md` §C ("IK Lem 5.2 is cited for a specific statement, so a primary read is needed before submission"); B23-10 §10.2 item 1, "the reading of IK Lem. 5.2". Source: IK §5, Lemma 5.2, and §3's "For `m ≥ D` let `p := x_1^D + … + x_m^D` … Let `G := GL_m`". The lemma's `e` depends on `d, m, D` and not on `λ ⊢_m dD`, which is what "uniform" was doing; the proof's tightness remark is about `e_ϱ`, not about minimality of the shift, so "makes no optimality claim" stands. |
| Q3 | **2** | After the proof of Theorem 4.5 `thm:census` | "The gauge law of Section 5, which is verified and not proved, and the covariance hypotheses refuted there, enter nowhere in this section" becomes "The totals law of Section 5 --- a theorem, but one whose proof consumes the two inputs of Lemma 5.6 as given --- and the covariance hypotheses refuted there, enter nowhere in this section." **The paper was wrong, not Theorem 5.5.** | `PROJECT_NOTES.md` L422, "SESSION 22: **the totals law TOTAL(N) = Psi(N) x 1,152,144,000 is a THEOREM.**" (and L1093–1094, session 22's own entry). The replacement clause is the paper's own phrase from the paragraph after `thm:totals`, "the two inputs the proof consumes", which Lemma 5.6 `lem:inputs` states. Wording as proposed in `GAPS.md` G-S1. |
| Q4 | 5 (LMR, Hüttenhain) | "Boundary geometry", after the `P_1`/`P_2` sentence | Adds that neither component is special to `n = 3` nor new with \cite{HL}: for odd `n`, LMR exhibit `P_Λ(M) = det_n(A,…,A,S) = Σ s_ij Pf_i(A) Pf_j(A)` and prove its orbit closure is an irreducible codimension-one boundary component not in `End·det_n`, which at `n = 3` is exactly `P_2`; and the traceless `d×d` determinant gives a component for every `d ≥ 3`. What \cite{HL} establish at `n = 3` is that there are no others. | `GAPS.md` §C, Hüttenhain-thesis row ("It is the most likely place for a det₃ orbit-closure computation the paper should distinguish") and LMR row ("Read it"). Sources, both read here: LMR Prop. 3.5.1 verbatim, and Hüttenhain Cor. 8.3.2 with §8.3's "A computation as in Lemma 8.1.2 shows that for `d ∈ {3,4,5}` … We will show in this section that it is true for all `d ≥ 3`". The identification `P_Λ = P_2` at `n = 3` is the thesis's own: §8.1 gives `b♯ = uᵗu` with `u = (x₃,x₂,x₁)` and `tr(b♯a) = u a uᵗ = 2Q₂`, which expands to the universal quadric the paper writes; and the thesis states the link explicitly — "the limit of the determinant on the space of skew-symmetric matrices always leads to a component of the boundary … when `d ≥ 3` is odd, as shown by Landsberg, Manivel, and Ressayre [LMR13, Prop. 3.5.1]". |
| Q5 | **3** | The paragraph after Proposition 4.8 `prop:divisor` | "deriving it directly from the explicit degeneration to `P₂` that Hüttenhain and Lairez supply … is the obvious next step and **we have not carried it out**" is replaced by what was actually done: the degeneration is written out, it **was** run (session 10), and it is consistent — `det L(t) = −64t⁶`, the Jacobi limit reproduces the `P₂` representative, tangency rather than crossing. **But** the family determines only the product `m₂c = 18`, and the observed `c = 2` is also what that product forces from `m₂ = 9`, so the two determinations lock each other. It is therefore a consistency check and not a derivation, **and the label "computed, not proved" stands. The paper was wrong, not the record.** | `docs/boundary_deficit.html` §W3 session 10, "m₂ = 9, now on two legs … Hüttenhain–Lairez's paper (fetched) supplies the explicit degeneration onto P₂ … Running our machinery over it: the 9×9 substitution matrix has det L(t) = −64t⁶ exactly … the Jacobi limit reproduces our P₂ representative on the nose, and — the sharp check — … the curve kisses P₂ with contact 2 rather than crossing it. The two independent determinations now lock each other: m₂ · contact = 6d − 18 = 18 from the family, m₂ = 9 from torus integrality, hence contact = 2" (`350825ae`). `docs/conductor.html` §5.4, "m₂ = 9 forced by torus integrality and confirmed against Hüttenhain–Lairez's explicit degeneration (contact 2, Jacobi limit)". The label is **not** upgraded, per G26 and `GAPS.md` G-S3; the Jacobi formula and the skew/symmetric split are cited to \cite[§8.1]{Hue}, read here, where `tr(b♯a) = 2Q₂` appears verbatim. |
| Q6 | 5 (LMR) | After Corollary 4.13 `cor:perm` | "of course classical and easy by other means" is replaced by the actual other means: LMR prove the **border** determinantal complexity of `per_m` is at least `m²/2`, which at `m = 3` gives 5; theirs is the first quadratic bound for the border measure, and the earlier Mignon–Ressayre bound is for `dc`, not `dc̄`, so it does not by itself exclude `per₃ ∈ Ω̄`. | `GAPS.md` §C, LMR row: "The abstract states a quadratic lower bound on the determinantal *border* complexity … The paper calls this 'classical and easy by other means' and cites nothing. Read it, then cite it as the 'other means' in the sentence after Corollary 4.13." Source: LMR Thm 1.0.1, `dc̄(perm_m) ≥ m²/2`, with §1's "The best known lower bound is `dc(perm_m) ≥ m²/2`, which was proved in [3]" (Mignon–Ressayre) and "The best known lower bound on this function [`dc̄`] had been linear." This is the `dc`/`dc̄` distinction of ruling **B23-10.23**. |
| Q7 | **4** | Remark 5.11 `rem:fails`, opening | "**Three** hypotheses about the functional were pre-registered and then refuted by their own tests … each was killed by a single number" becomes "**Two** … (a) and (b) below, each killed by a single number. A third route, (c), was not pre-registered and was closed instead by a degree count and an explicit counterexample." | `PROJECT_NOTES.md` session-16 header, "the rigidity theorem is RETRACTED — **two** receiving-space hypotheses falsified by their own pre-registered tests", with items (2) and (4) being (a) and (b). For (c): `PROJECT_NOTES.md` session 18 (2) and `docs/psi_identification.md` "The plane-cubic hypothesis is DEAD (two independent proofs) — (a) Degree count … (b) Explicit counterexample, projective class", neither of which is a pre-registered test. The record nowhere says (c) was pre-registered; `GAPS.md` G-S2 flagged exactly this hole, and the resolution is to say which of the three was and which was not. |
| Q8 | — (K10) | Remark 5.11 `rem:fails`, the retraction sentence | "which rested on the fits refuted in **(b)**" becomes "…in **(a)**". | Corrigendum **K10** of `docs/b23_10_review.md` §12.1 at `239dd6e8`, and §6.2: `PROJECT_NOTES.md` L755 logs `TOTAL_G` in session 13, L775 carries it through session 14, L829 withdraws it; session 13/14 is the det²-slot hypothesis, which is (a). B23-10 §10.2 lists this under "(f-1) Paper 1 blockers". |
| Q9 | **4** | §7 `sec:method`, "Pre-registration" | "**Two** of the hypotheses so registered were refuted (Remark 5.11)" becomes "**Five** …", enumerated: the two of Remark 5.11(a), (b); the arithmetic claim corrected in Remark 5.10; and, for Theorem 3.1, that attainment holds wherever `m(λ) > 0` (refuted at `(17,17,2)`) and that non-attainment occurs exactly on empty support (refuted by the parity family). §7's scope is every pre-registration behind the paper's results, not only Remark 5.11's. | Two: `PROJECT_NOTES.md` session-16 header, as in Q7. One: `results/PREREG_Xm3.md`, "Predictions, logged now … 4. Every value is `151,200 x` an integer (the programme's arithmetic signature)", refuted in `PROJECT_NOTES.md` session 23 (4) "**REFUTATION — THE ARITHMETIC SIGNATURE IS 75,600, NOT 151,200**", with the session-23 ledger "six pre-registered, five hit, one refuted". Two: `docs/session_23.md` §4, rows P3 ("attainment holds whenever `m(λ) > 0` — **REFUTED** — `(17,17,2)`, falsifier F3 fired") and P5 ("non-attainment happens exactly on empty support — **REFUTED** — the parity family is mostly `m > 0`"), with the line below the table, "Two pre-registered hypotheses refuted (P3, P5), both kept." `2 + 1 + 2 = 5`. |
| Q10 | 5 (Hüttenhain) | Bibliography, `\bibitem{Hue}` | Adds `doi:10.14279/depositonce-6032`, so that the two new section-level citations to the thesis are locatable. | The citation is now used at Q4 and Q5, which G14 requires to be findable. DOI read off the TU Berlin DepositOnce record for the thesis. |
| Q11 | 5 (Kumar) | Bibliography | New `\bibitem{KumarComp}`: Kumar, *A study of the representations supported by the orbit closure of the determinant*, Compositio Math. **151** (2015), 292–312; arXiv:1109.5996. | Required by Q1. Volume, year and pages confirmed against Ikenmeyer–Kandasamy's bibliography entry `[Kum15]`, read here. |
| Q12 | 5 (LMR) | Bibliography | New `\bibitem{LMR}`: Landsberg, Manivel, Ressayre, *Hypersurfaces with degenerate duals and the geometric complexity theory program*, Comment. Math. Helv. **88** (2013), no. 2, 469–484; arXiv:1004.4802. | Required by Q4 and Q6. arXiv carries no journal reference, so volume, issue and pages are taken from Hüttenhain's bibliography entry `[LMR13]`, read here. |

## 3. README edits (`README.md`, the public README)

| # | What changed | Authorising line |
|---|---|---|
| R7 | The refutation list (l. 78 ff.) said "**Three** pre-registered hypotheses were **refuted**, each by a single number". It now says two were pre-registered and refuted, each by a single number, and that the third route was closed without a pre-registered test; each bullet is tagged *(pre-registered)* or *(not pre-registered: killed by a degree count and an explicit counterexample)*. | The same lines as Q7. Blocker 4 requires paper §7, paper Remark 5.11 and `README.md` to agree; this is the Remark 5.11 side. |
| R8 | "On the commit history" (l. 187) said "**Two** of the pre-registered hypotheses were refuted". It now says **five**, enumerated as in Q9, with a pointer to the *Arithmetic signature* section for the `151,200` one. | The same lines as Q9. This is the §7 side of the same count. |

## 4. B23-10 §6.2's three findings against the B23-05 ledger in Part II

Recorded here rather than edited into Part II, which is left as it was written.

- **P4 and P5 — incomplete authority (not a wrong claim).** Both cite
  `docs/boundary_deficit.html` session 9 and omit that **session 10 of the same
  file** upgraded `m₂ = 9` "from derived to confirmed". B23-10: "the CHANGES
  entries should cite session 10 too." They now do, through Q5, which reads
  session 10 in full, keeps the conservative label, and gives the reason the
  session-10 check does not upgrade it.
- **P7 — unsupported letter.** Corrected in the paper by **Q8**.
- The three corrections B23-05 made to the integrator's brief (remark numbers
  4.7 and 5.10; no `README_public.md` ever existed; no paper version mentions
  "rigidity" or "TOTAL_G") were all verified by B23-10 and stand. The theorem
  counter was re-walked in this pass and is unchanged: 52 environments,
  `prop:census` = 4.1, `cor:lower` = 4.2, `thm:census` = 4.5, `rem:norm` = 4.7,
  `prop:divisor` = 4.8, `cor:perm` = 4.13, `rem:BI` = 4.14, `thm:totals` = 5.5,
  `lem:inputs` = 5.6, `rem:arith` = 5.10, `rem:fails` = 5.11.

## 5. Checks run on the edited source

No LaTeX toolchain is installed in this worktree, so the source was not
compiled. Instead, by script, before and after:

- brace balance (1388 / 1388) and `$` parity (even) — both hold;
- every `\ref` and `\eqref` resolves to a `\label`; **0** undefined;
- every `\cite` key resolves to a `\bibitem`, and **every `\bibitem` is cited**,
  including the two new ones; **0** undefined, **0** orphaned;
- the theorem counter walked end to end and compared against `HEAD`:
  **identical**, 52 environments, so no cross-reference in the record moves.

## 6. Things deliberately not changed

- **Blocker 1, the attribution.** Prepared as `ATTRIBUTION_PATCH.md` and not
  applied, by the user's decision of 2026-09-19. The paper contains none of it.
- The items the paper states as open in its own voice — the three Remark 3.3
  items, the finite verification behind attainment, the computed `m₂ = 9`,
  primitivity — stay open. Nothing here closes one by argument.
- New findings from this pass that are framing rather than correction are in
  `GAPS.md` (G-P3, G-P4, G-P5) with proposed wording, unapplied.

---

# PART II — B23-05: the earlier finishing pass

Worktree `C:\Users\swami\Projects\gct-gpt\work\batch15_workers\b23-05`, branch
`b23-05-paper1`.

- **HEAD at start:** `82633a60893236fab4fbc317df416e1b8a349005`. This matches
  the packet.
- **`git status --porcelain` at start:** empty.
- **Git use:** read-only. Nothing was committed.
- **Pre-edit blobs:** `paper/det3-conductor.tex` = `7ac14b6c5a`,
  `README.md` = `f0ef47df05`.
- **Authorising record blobs at HEAD:**

  | File | Blob |
  |---|---|
  | `PROJECT_NOTES.md` | `b506647fbc` |
  | `docs/ambient_audit.md` | `c5d77e927e` |
  | `docs/transport_formula.md` | `c4e6d847f5` |
  | `docs/session_23.md` | `84ace6b452` |
  | `docs/primitivity.md` | `0ef3fd41b3` |
  | `docs/boundary_deficit.html` | `86c4513348` |
  | `docs/rigidity_theorem.md` | `55be84df44` |

## Three corrections to the packet's own references

These are recorded before the edits so that every row below is unambiguous.

1. **The primitivity remark is Remark 4.7, not 4.8.** In the source at HEAD the
   primitivity remark `rem:norm` is **4.7**, and 4.8 is `prop:divisor`. The
   remark `rem:arith` is **5.10**, not 5.11; 5.11 is `rem:fails`. Both numbers
   were computed by walking the shared theorem counter; no LaTeX toolchain is
   installed here. Remark 3.3 = `rem:Bcaveat` is correct. The packet's numbers
   look like an older build with one environment fewer in each place. The edits
   below target the remarks by content, not by number.
2. **`README_public.md` does not exist.** No file of that name exists in the
   worktree, in git history (`git log --all -- '*README_public*'`), or under
   `C:\Users\swami\Projects\gct-gpt`. The public README is `README.md`: it was
   created as "public README" in `2cd41b5a` ("Paper: arXiv source; public
   README; dual license…"). That is the file corrected here.
3. **The paper never mentioned the rigidity theorem or TOTAL_G.** Item 7
   presumes the paper "keeps saying" these are retracted. Every one of the 20
   commits that touch `paper/det3-conductor.tex` was checked, from `2cd41b5a`
   to `7309c4e2`: none contains "rigidity" or "TOTAL_G". Only the V^h_σ
   refutation was ever present (`rem:fails` (a)). So no retraction was removed.
   The two missing retractions are added (row P7).

## Paper edits (`paper/det3-conductor.tex`)

| # | Where | What changed | Why | Authorising record line |
|---|---|---|---|---|
| P1 | Remark 3.2 `rem:orphan`, list of four orphans | "are *finitely many* — exactly four, at every degree" becomes "are, on the exhaustive sweep of Remark 3.3(iii), exactly four". Adds "That there are no others is open." "Finiteness holds because …" becomes "The reason we expect finiteness, which we give as a sketch and not as a proof, is …". | Item 1 (iii). The remark asserted as proved what Remark 3.3 says is not. The label is narrowed, not upgraded. | `docs/transport_formula.md` §5 "The honest boundary", "Not proved" bullet 3 ("Finiteness of the orphan locus has the character estimate of §4 as a proof sketch; the explicit constant … was not computed. The sweep to `p, q ≤ 150` is the actual evidence"), introduced `72b52ab5`. `docs/session_23.md` §5 (iii), `fe116f95`. |
| P2 | Remark 3.3 `rem:Bcaveat` | Each of (i), (ii) and (iii) now ends with an explicit statement that it is open. (ii) now says the codimension statement is quoted, not verified, and has no reference. Adds one sentence: the attainment half rests on a finite verification that was checked exhaustively but is not written out as inequalities. | Item 1. None of the three is resolved anywhere in the record, so each is stated as open in the paper's voice. The added sentence is the record's own qualification of Theorem 3.1. | Same two lines as P1: `transport_formula.md` §5, all three "Not proved" bullets and the "Proved modulo an explicit finite verification" paragraph (`72b52ab5`); `session_23.md` §5 ("Proved modulo an explicit finite verification: Theorem 2 (attainment) … Not proved: (i) … (ii) … (iii) …", `fe116f95`). `docs/isotypic_rank.md` and `docs/session_26.md` remove the dualisation only for the det₃ rank lemma, not for World B, so they do not close (i). |
| P3 | Remark 4.7 `rem:norm` | "We have not determined whether 𝒩 is primitive, but the question is now bounded" becomes "Whether 𝒩 is primitive is open", with the reason no evaluation can prove primitivity. Two closing sentences name what would settle it. | Item 2. The record leaves primitivity open, so the plain sentence replaces the hedge. No new bound or value is added. | `PROJECT_NOTES.md` status header "OPEN AND NEWLY SHARP: NEITHER Phi_18 NOR Phi_24 is known to be primitive" (introduced `7c86da91`). `PROJECT_NOTES.md` session-23 item (5) "PRIMITIVITY (Job 4)": "g(F) … only an upper bound, so no finite set of evaluations can PROVE primitivity" and "Settle it by exhibiting an integral invariant F with V = 46,448,640 . F …, or by getting coefficients OUTSIDE U (… br2.c handles only the six permutation monomials)" (`7c86da91`). `docs/primitivity.md` "RESULT (session 23)" (`008a03c4`). |
| P4 | Proposition 4.8 `prop:divisor`, statement | Adds: "The coefficient 6 is proved. The coefficient 9 is computed, not proved; its source is given below." | Item 3. A computed value inside a Proposition must carry its label in the statement, not only in the paragraph after it. | `PROJECT_NOTES.md` line 483–484: "div(Φ₁₈) = 6P₁ + 9P₂ (session 9: Ω̄ smooth along generic P₁, ramification 6; P₂ wild/non-normal, m₂ = 9 by torus integrality)". `docs/boundary_deficit.html` §W3 session 9: P₁ "theorem + verified 3 ways"; m₂ "Tagged as derived, not proved" (`350825ae`). |
| P5 | Paragraph after `prop:divisor` | States the assumption the m₂ computation makes (unit-factor vanishing at a generic point of P₂, as proved along P₁), the forcing step 18/m₂ = 2, and the source: session 9 of `docs/boundary_deficit.html`. The existing "computed value rather than a proved one" is kept. | Item 3 ("with its source"). The assumption is part of the source's own statement, so leaving it out would overstate the label. | `docs/boundary_deficit.html` §W3 session 9: "assuming the generic-point unit-factor behavior (which held rigorously at P₁), the normal weight vector is proportional to the trace character, and torus integrality plus SL-invariance of the normal weight force 18/m₂ = 2: m₂ = 9 … Tagged as derived, not proved" (`350825ae`). |
| P6 | After the proof of Proposition 4.15 `prop:def222` | Adds the ambient-audit framing. The deficit is ambient arithmetic, because Sym²(Sym³) contains no S_(2,2,2). The *base point* of the ray says nothing about the boundary of 𝒪. The conductor is the stabilisation index along the Φ₁₈-ray, and it stands. | Item 4. The sentence goes where the paper introduces def((2,2,2),2) = 1. c((2,2,2),2) = 1 is explicitly not retracted. | `docs/ambient_audit.md` §7, final paragraph: "This does not retract `c((2,2,2),2) = 1`. The conductor is the stabilisation index along the `Phi_18`-ray … What it retracts is the *framing*: the base point of the ray is not evidence about the determinant's boundary, and the paper should say so where it introduces the datum" (introduced `a363f967`). |
| P7 | Remark 5.11 `rem:fails`, after (c) | Adds that (a) and (b) also retract two working-record claims that never appeared in the paper. The first is the rigidity theorem. The second is the predicted total at a further point (G), which rested on the refuted fits; G has never been evaluated and its total is open. The retraction notices remain in the repository. | Item 7. The packet requires the paper to keep saying these are retracted. It never had (see correction 3). G is described rather than named, because the paper never defines it. | `PROJECT_NOTES.md` status header "RETRACTED 2026-08-29 …: the rigidity theorem; V^h_sigma as a det^2-covariant; V^h_sigma as a simultaneous-conjugation invariant; TOTAL_G = 1,152,144,000 (G never run, value OPEN)" (`3041a3ad`). `PROJECT_NOTES.md` session 16 items (1)–(6), including "(6) WITHDRAWN: TOTAL_G … rested on the refuted fits. G has never been run" (`3c5d50f4`). `docs/rigidity_theorem.md` line 3 "RETRACTED" (`3c5d50f4`). |

Retractions check (item 7), all confirmed present after the edits:

- **V^h_σ covariance refutation:** `rem:fails` (a), unchanged.
- **Conjugation-invariance refutation:** `rem:fails` (b), unchanged.
- **Rigidity theorem and TOTAL_G:** added in P7.
- **151,200 correction:** `rem:arith`, unchanged.

No existing retraction was removed or softened.

## README edits (`README.md`, the public README)

| # | What changed | Why | Authorising line |
|---|---|---|---|
| R1 | The ternary-cubics row had the uncorrected floor `c = ⌊μ_max/|w_N|⌋`, "equality on all 254 weights, δ ≤ 10". It now reads `c = ⌊(λ₁−2λ₃)/6⌋ − π(λ)` with π defined, the status "≤ proved; equality rests on a finite verification and on the three open items of Remark 3.3", and the first failure at (17,17,2). | Item 5, "the uncorrected World B floor". | Paper Theorem 3.1 `thm:B` and Remark 3.3 (as edited in P2). `docs/session_23.md` §1 (`fe116f95`). |
| R2 | The Φ₁₈(det₃) row's status "exact" gains "in the normalisation 𝒩; whether 𝒩 is primitive is open (Remark 4.7)". | The paper says the factorisation "may be mostly normalisation". The README had quoted it bare. | Paper Remark 4.7 `rem:norm`. `PROJECT_NOTES.md` "OPEN AND NEWLY SHARP" (`7c86da91`). |
| R3 | The row "`V(Φ₁₈) ∩ Ω̄ = ∂Ω̄`; `div = 6P₁ + 9P₂` — proved" is split in two: "V(Φ₁₈) ∩ Ω̄ = ∂Ω̄ — proved", and "div — 6 proved; 9 computed, not proved". | Item 5, "fix the file to match the paper". The README called the P₂ multiplicity proved; the paper does not. | Paper Proposition 4.8, as labelled in P4/P5. `boundary_deficit.html` session 9 (`350825ae`). |
| R4 | The totals row changes from "tested at Ψ = 1, 4, 0 only — **not proved**" to "theorem (Thm 5.5); its out-of-sample prediction at X₋₃ (Ψ = −3) measured and exact". | Item 5, "the totals law as stated there". | Paper Theorem 5.5 `thm:totals`, and the X₋₃ paragraph after it. `PROJECT_NOTES.md` status "SESSION 22: … the totals law … is a THEOREM" and "SESSION 23 … TOTAL(X_-3) = -3,456,432,000 … CONFIRMED". |
| R5 | The section "What is *not* proved" is replaced. It had said the totals law is empirical, that X₋₃ has not been measured, and that there is "one gap χ ↔ det²". There are now two sections. "The totals law" states the theorem and the X₋₃ confirmation. "What is *not* proved" lists the three Remark 3.3 items, the computed m₂ = 9, and open primitivity. | Item 5. Every statement in the old section was superseded by the paper. The new list is exactly what the paper labels open or computed, and nothing else. | Paper Theorem 5.5, Lemmas 5.7 and 5.8, Remark 3.3, Proposition 4.8, Remark 4.7. The same `PROJECT_NOTES.md` session-22 and session-23 lines as R4. |
| R6 | After the three refutations, adds that the rigidity theorem is retracted and `TOTAL_G = 1,152,144,000` is withdrawn, with G never run and its value open. | Item 7, applied to the public README as well. | The same lines as P7. |
| — | **Signature 151,200 (no change needed).** The "Arithmetic signature" section already says 75,600. It keeps 151,200 only for the ten enumerated values, and says in bold that the earlier claim was wrong. That matches paper Remark 5.10 `rem:arith` word for word in substance. | Item 5, first bullet. It was already fixed at `5e13cbc8` ("Correct the arithmetic signature to 75,600 in README, paper and notes"). Rewriting it would be an edit without a reason. | `5e13cbc8`. `PROJECT_NOTES.md` session-23 "REFUTED … 75,600 … NOT 151,200". |

## Things deliberately not changed

These are stale or unattributed text that falls outside items 1–7. Each goes to
`GAPS.md` with proposed wording, per G26:

- **G-P1:** the attribution of the bracket census to Bürgisser–Ikenmeyer
  Cor. 7.2.
- **G-S1:** "verified and not proved" at paper line 617.
- **G-S2:** "Two/Three" pre-registered refutations (paper §7 against
  Remark 5.11; README l.79 against l.183).
- **G-S3:** the paper's statement that the Hüttenhain–Lairez check was "not
  carried out", against the record's session 10.
