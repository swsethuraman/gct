# B23-05 — Paper 1 finishing pass: change ledger

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
