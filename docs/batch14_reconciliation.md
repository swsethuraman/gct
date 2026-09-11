# Batch 14 — reconciling three boards

**Revision 2.** §1's blocking question is resolved: a second Claude session wrote
the strategy memo, and Astra could not tell two Claude sessions apart. Not a
provenance failure — a coordination gap. §1 is kept as the record of what was
checked; §§8–10 are the assessment that matters.

Integrator assessment. Everything below was checked against the tree.

## 1. Blocking: v0.2 is built on a memo I did not write

v0.2 reallocates **eight of twelve slots** around what it calls "Claude's
strategy memo" — the mixed linear/cubic bracket construction, the
complete-interpolation argument, and a ladder calculation. **I did not produce
any of it.**

`docs/batch14_board.md` at `325bf521` contains zero occurrences of: *mixed
bracket*, *mixed linear*, *separating set*, *complete interpolation*, *N13*,
*N14*, *P13*, *P14*, *CRT*, *390*, *532*, *533*, *159*.

Worse, four numbers the proposal attributes to me have **no provenance in the
repository at all**:

| number | in the tree? |
|---|---|
| 391, 392, 529, 531 | **yes** — B13-06, `results/b13_06/rank_questions.json` |
| **390, 532, 533, 159** | **nowhere** |
| target cell `(63,19,2⁷)` at degree 24 | **nowhere** |

B14-08 is tasked to "check the reported `dim N14 = 159`" and B14-12's entire
mechanism rests on "Claude's ladder calculation, treated as pending recount"
for a cell that does not exist in the tree. Both are recounting numbers whose
author cannot be asked.

This is not a formality. v0.2 §1's own table already marks several of the memo's
claims **"Too strong"**, **"Not established"** and **"Invalid as an exclusion"** —
Astra is correctly reviewing a document nobody can question. v0.1 §9 names two
other models in this pipeline (Gemini, Kimi). **Before v0.3, we need to know
which of them wrote it**, because the answer decides whether 08 and 12 are
verifying a colleague's arithmetic or auditing an unattributable claim.

## 2. The route itself is sound, and its source side checks out here

Setting attribution aside, the mathematics in v0.2 §2 is valid and rather good.
If `dim N_d = h` is proved and `h` explicit members of `N_d` have a nonzero
`h`-minor on a point set `P`, they are a basis, evaluation on `P` is injective on
`N_d`, and the exact source matrix on `P` therefore has the true restriction
kernel — with no need to express source images in the target basis first. That
genuinely avoids the Pieri coupling, which is what blocked B13-01/02/03.

**Verified here:** `results/s74/source.json` has `complete: true`, 274 entries,
and a birth profile giving exactly **39 rows through degree 13** and **93 through
degree 14** (2 + 37, then + 54). Astra's source arithmetic is right, and the
`H_d = (9!)²·2¹⁵·1176^d` bound with six/seven CRT primes is checkable from the
Leibniz definition it cites.

**But note what the route can and cannot deliver**, which v0.2 states correctly
and which should drive the allocation: `i_red(13) = 0` leaves LMR open. The
route's best outcome is `i_red(14) = 5`, giving `D_LMR = −4` exactly — a
**negative** decision. Eight of twelve slots on a chain whose success kills the
programme's main candidate and whose failure proves nothing is a large bet in one
direction.

## 3. B14-01's premise is already answered in the tree, and that is my fault

v0.1/v0.2 give a slot to auditing exclusions that relied on the blanket
"`a = 1` closed by BIP" convention, because Theorem 1.5 assumes `n ≥ m^25`. The
reasoning is right. The house already has a **stronger** answer, twice:

- `docs/dip_transfer.md` §3 (s37) relabelled the convention *"excluded by
  convention, not by theorem."*
- `docs/bip_transfer.md` (s52) asked whether the **mechanism** reaches `n = 4`
  even though the theorem does not, and answered no for a sharper reason than the
  hypothesis: its reach is measured in weight **length**, which at `n = 4` is
  `ℓ(λ) ≤ 4`, while permanent-sensitivity begins at `ℓ(λ) = 6`. Every
  determinant-side point it supplies at `n = 4` is a product of four linear forms
  with span `≤ 3`, and a weight vector of weight `λ` vanishes at every point of
  span `< ℓ(λ)`. Verified in-house at three six-row cells.

**Neither was cited in `PROVED.md`.** That is the gap in the index I built, and
its consequence is a planning document proposing to spend a session re-deriving a
weaker form of a proved, measured result. Batch 13 lost three sessions to exactly
this shape. Now indexed as `bip_blind_at_n4`.

Also checked: `results/integrate/inherited_exclusions.json` carries **no**
occurrence, BIP or `a == 1` predicate — its predicates are length and
containment. The machine ledger never depended on the convention, so the exposure
was always in prose. B14-01 shrinks accordingly: confirm the s37/s52 relabelling
was applied everywhere in prose, then build the quartic shortlist. That is a
fraction of a slot, not a slot.

## 4. Two things v0.2 parks that should not go

**The 58 six-row degree-10 cells.** v0.2 §9 parks "broad cubic sweeps". These are
not a sweep — they are 58 named cells, 344 of 402 already closed, the nearest
completable frontier theorem in the programme, and one of the four success
criteria batch 13's own stocktake names. A1 also established that some of them
will need `matmul_mod_wide` and that none of their `n_χ` has ever been measured.
Dropping them leaves a finite, 86%-complete theorem unfinished.

**The compact certificate kind.** v0.2 §9 parks "generic large-hybrid certificate
development" and B14-08 becomes a dimension recount. But 837 of s79's 2,066
listed certificates are absent, every result above `N_S·a = 3×10⁶` is
producer-attested only, and `certificate_ceiling` says the existing formats
cannot express these results at all. This is also a named success criterion. If
it is parked, the verification backlog keeps growing faster than the mathematics.

## 5. Baseline

Both versions use `7e69506a`, three commits stale. They miss A1 revision 2 (the
deficient-control gap, D1 at `ℓ = 7`, A2 re-scoped, A2b), the two `PROVED.md`
corrections (Theorem F's missing hypothesis, Theorem E's withdrawn dismissal),
and the board itself. Current base is **`736e5cf0`**.

Credit where due: v0.1 §3 independently carries the corrected length bound
`6 ≤ ℓ ≤ min(r,δ)`, the ladder-product qualification *"only with nonzero
coordinate-ring factors, including positive ambient multiplicity"* — which is
exactly the Theorem F hypothesis — and *"apply stabilizer conclusions only in
their proved scope"*. Astra's register had all three before the corrections
reached it.

Astra also works from `C:/Users/swami/Projects/gct-gpt/work/batch13_rewritten`,
a different clone from `C:/Users/swami/Projects/gct/work`. Both should be pinned
to the same base hash before dispatch.

## 6. Recommended shape for v0.3

Keep the interpolation chain, at five slots rather than eight; restore the two
parked items; shrink the BIP audit.

| # | job | from |
|---|---|---|
| 1 | Exact degree-13 source matrix at `P13` (39 × 96, signed CRT) | Astra 02 |
| 2 | Mixed-letter evaluator and the degree-13 target basis | Astra 04 |
| 3 | Complete-interpolation certificate spec and independent checker | Astra 03 |
| 4 | Independent recount of `dim N13`, by a method unlike Weyl alternation | Astra 08, **less** the unprovenanced 159 |
| 5 | Exact degree-14 source matrix at `P14` (93 × 192) — bounded stretch | Astra 07 |
| 6 | The 58 six-row degree-10 cells | my B14-01 |
| 7 | `(12,4,4,4,4,4)₈`, the last Q1 cell | both boards |
| 8 | The compact `hybrid_kernel` certificate kind | my B14-10 |
| 9 | The product image at 392 and 531, ranks 2 and 3 | both boards |
| 10 | Evidence base: 874 files + 837 certificates | both boards |
| 11 | Exclusion audit (shrunk) + quartic shortlist at `δ ≤ 8` | Astra 01 |
| 12 | **Open** — pending the memo's provenance | — |

Slot 12 is deliberately unfilled. If the memo turns out to be a colleague's with
a checkable derivation, the degree-24 neighbour job earns it back. If nobody can
produce the derivation of 390, 532, 533 and 159, the slot should go to the
degree-9 portion or the five-variable elimination instead — not to recounting
numbers with no author.

## 7. One thing to keep from the exchange regardless

v0.1 §5: *"A test must actually reach its assertions and must fail on a
deliberately wrong input."* Astra wrote that independently, and it is the same
lesson A1's first pass learned the hard way — eleven cells that all returned
rank `= a` and could not have detected a rank computation that had stopped
computing. Two boards converging on that rule from different directions is
worth more than either statement alone. It belongs in the preamble verbatim.


---

## 8. Resolved, and the numbers are right

I reproduced the three unprovenanced ladder values on the house census, with
three banked values calibrating the instrument:

| cell | δ | a | memo | banked |
|---|---|---|---|---|
| `(63,19,2⁷)` | 24 | **390** | 390 | — |
| `(67,19,2⁷)` | 25 | **391** | 391 | — |
| `(71,19,2⁷)` | 26 | 392 | 392 | 392 ✓ |
| `(69,21,2⁷)` | 26 | 531 | 531 | 531 ✓ |
| `(73,21,2⁷)` | 27 | **532** | 532 | — |
| `(65,17,2⁷)` LMR | 24 | 274 | 274 | 274 ✓ |

**Said precisely, because the distinction is the whole point here: this is a
reproduction, not method diversity.** The memo computed 390, 391 and 532 with the
same house `a_weyl` I just used. Agreement rules out a scratch or transcription
error. It does not rule out a systematic error in `a_weyl`.

**And the single-method exposure is wider than the memo's own §5 admits.** It
flags `dim N₁₃ = 73` as confirmed only by Weyl alternation. But `a_∞ = 392` and
`533` come from that session's own stable-slice code, and `h_pad = 159` from
B13-01's counter with the degree generalised — each one implementation, one
method. **159 decides rung 14, which is where `D = −4` would be settled.** The
recount slot must cover 73, 159, 533 and `a_∞`, not 73 alone.

## 9. The memo's strategic argument beats mine, and changes my board

Lemma T is the best contribution on the table. Multiplication by a highest-weight
vector is injective on each ideal, so **every genuine padded relation at LMR
survives to both B13-06 targets** — not three of five. Two consequences my board
did not have:

- **B14-05's thresholds are moot unless `i_pad(24) ≤ 1` (target A) or `≤ 2`
  (target B).** If `i_pad(24) = 5`, a positive gap at target A needs *four*
  determinant equations at `(63,19,2⁷)₂₄`, where no known module lives. So the
  product-image job is dominated by a number nobody has certified.
- **The capability gap is smaller than I assumed.** My Tier C built two slots on
  the 521-coordinate conversion and the Pieri strip coupling. The memo replaces
  both: mixed linear/cubic brackets need no Pieri coefficients, and a spanning
  certificate replaces the conversion. My C1 and C2 were over-built.

So the top priority is certifying `i_red(13)` and then `i_red(14)`, and I adopt
that. I also concede most of the memo's case against my slot 1: a
permanent-specific cubic equation *raises* `i_pad` and therefore *lowers* `D`, so
the degree-10 frontier does not advance either objective. My "nearest completable
frontier" justification was weaker than I presented it. I would keep it, demoted:
the expected outcome — all 58 empty, given 344 of 402 already are — extends
`degree8_global` to degree 10, which is a real theorem and the *good* direction
for `D`.

**Where Astra is right against the memo.** Its v0.2 §1 makes two corrections I
endorse. The memo's board has **five slots waiting on other slots** (07 after
01+02, 08 after 03+01, 09 after 01/02/05, 10 after 06 or 08); Astra caught it and
rebuilt every job with an independent core, which is the standing rule. And the
memo abandons `(12,4,4,4,4,4)₈` because "no known family lives there" — Astra's
table marks that form of reasoning **"invalid as an exclusion; it can justify a
funding preference only."** That is the same error class as the Theorem E
dismissal withdrawn this morning: an absence of known mechanism treated as a
bound. Deprioritise it if you like; do not retire it on that argument.

## 10. Recommended v0.3 — twelve slots, no in-batch dependencies

Six needing `gcc` + `python-flint`, six not, which matches the established host
split exactly.

| # | job | host | from |
|---|---|---|---|
| 1 | Mixed-letter evaluator; controls; a nonzero 73-minor at `P13` | flint | memo 01 |
| 2 | Exact degree-13 source matrix at `P13`, signed CRT, exact nullspace | flint | memo 02 / Astra 02 |
| 3 | `complete_interpolation` certificate kind and an independent verifier | any | memo 05 / Astra 03 |
| 4 | Second-method recounts: **73, 159, 533, `a_∞`** — widened | stdlib | Astra 08, widened |
| 5 | Lemma T and Lemma CI write-up; bracket-adjunction proof and validation | stdlib | memo 03 |
| 6 | Stable bracket evaluator; reproduce 274 / 273 / 269 at the LMR tail | flint | memo 06 |
| 7 | Exact degree-14 source matrix at `P14` — **source half needs nothing from 1** | flint | memo 07, dependency removed |
| 8 | Transport census, combinatorial half, all 239 components | stdlib | memo 08, dependency removed |
| 9 | The 58 six-row degree-10 cells — demoted, not dropped | flint | my B14-01 |
| 10 | Evidence base: 874 files + 837 absent certificates | any | all three boards |
| 11 | Exclusion audit (shrunk — `bip_blind_at_n4` is now indexed) + quartic shortlist | any | Astra 01 |
| 12 | `(12,4,4,4,4,4)₈`, the last Q1 cell | flint | Astra 05 / my B14-07 |

Two structural fixes carried in: slots 7 and 8 keep the memo's targets but take
the core work that starts from frozen inputs, so nothing waits; and there is no
integrator slot, because integration is continuous and not a twelfth of the
batch's research capacity.

**The pre-flight items stay mine**: the full-stabiliser probe at `ℓ = 9`, and now
also confirming that the s37/s52 BIP relabelling was applied everywhere in prose.
