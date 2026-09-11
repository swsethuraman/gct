# Batch 14 — reconciling Astra's v0.1 / v0.2 with the board at `325bf521`

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
