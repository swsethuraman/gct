# B18-12 review — the evidence ledger

Ledger: `work/batch15_workers/B15-12/docs/b18_12_ledger.md`, 441 lines, 14 sections.
Started from `761e0e7e`, tree `67f8d126`. No computation, no lease, no git beyond the
two `rev-parse` calls. Current as of 17:07.

## Verdict

**ACCEPT.** The ledger does the job it exists to do, and its §4a arithmetic is exact —
I checked every row. Two sections are now stale through no fault of the slot, and this
review is written so it can be transcribed directly as the update.

## 1. §4a verified completely

Every row of the exact-cells table, checked independently:

| check | result |
|---|---|
| each `lambda` sums to `4d` | **10/10** |
| each has exactly ten rows | **10/10** |
| `D upper = U − (a − i_det)` | **10/10** exact |
| first part `= 4d − t − 16` with `t = 17` or `19` (and `15` for the first B16 row) | **10/10** |
| `d = 27` row: `D lower = 243 − (a − i_det) = −175` | exact |

And it agrees with a slot that never saw it. B18-06 independently reported "the padding
ceiling is only 0.67–0.84 of `a`" and "every assigned cell has `q + U − a <= −30`".
From this table I get `U/a` ranging **0.671 to 0.836** and a maximum `D upper` of
**exactly −30**. Two slots, two documents, no contact, the same statistics.

The writing-out of the first parts — "so nobody has to re-derive them" — is exactly the
right instinct. That family has been described by formula in three batches and printed
in none.

## 2. The best line in the delivery

> "Update §2a from the review's own §5 ledger when it lands, and **never before**."

Slot 10's review is partial and its rulings on the aggregate claim, the ceilings and
the release gates are unwritten. The ledger records what 10 has accepted, marks it
partial, and **refuses to act on it** — noting that every accepted line concerns
existence or dimension and that "none names a cell, `s`, `b`, `r`, or a gap."

That is the difference between a ledger and a summary. A summary would have reported
"slot 10 accepts the dimension and degree claims" and let the batch read that as
progress. This one says the accepted lines change no operational plan. Keep doing that.

The framing "the three reports on disk are unfinished sessions, not finished proofs" is
the single most useful sentence anyone has written this batch.

## 3. What is now stale, and why it is not the slot's fault

The ledger timestamps itself honestly and says it stays open. But it was written at
17:07, and:

- **§7 says "05, 06 have written nothing."** Slot 06 delivered at 17:39 and slot 05 at
  17:43. Both are complete, both reviewed and accepted.
- **§10's decision tree is keyed on slot 06's shortlist**, which has since resolved.
  The branch the next board hangs on is closed.

So the ledger's forward-looking section rests on a fork that shut thirty minutes after
it was written. Nothing to correct in method; it simply needs the update below.

## 4. Updates to transcribe

**§7 completion states.**

| slot | state |
|---|---|
| 01 | COMPLETE. Report 527 lines, sha256 `2ba3fc9c…2256`. Reviewed, ACCEPTED. |
| 02 | COMPLETE. Reviewed, ACCEPTED, one condition. |
| 05 | COMPLETE. Reviewed, ACCEPTED, one repair requested (degenerate generic-quartic control). |
| 06 | COMPLETE. **Empty shortlist, accepted as the right answer.** Reviewed. |
| 10 | PARTIAL, stalled at §§1–2, resume issued. |
| 12 | OPEN. |
| 03, 04, 07, 08, 09 | NOT_TRIGGERED. 06 recommends no cell for 02, 03, 04. |
| 11 | COMPLETE. |

**§6 costs — two entries close.**

- "Slot 01's revision has delivered a new certificate, **unreplayed here**" — it has now
  been replayed twice independently: by the integrator (Leibniz cofactor expansion and
  exact `Fraction` elimination) and by slot 10 (two primes, over `Q`, at the two
  recorded points **and one fresh random point**, stabiliser nullity 1). `dim D45 = 50`
  has three lineages and five points behind it.
- Measured and feasible, contrary to "nothing measured feasible": B18-06's P1 closed six
  five-row cells at **at most 5.2 s and 289 MiB each**, and B18-02 certified twenty
  cells inside `55 s / 447 MiB`. The determinant evaluation is the first measured-cheap
  decision procedure the batch has.

**§3 hypotheses — H7 now has evidence, and it leans the wrong way.**

H7 ("a usable `b` exists somewhere") carries slots 03, 04 and 09 entirely, and the
ledger records it as having no evidence. It now has some: **B18-02 measured
`s − b = a` in all twenty certified cells** — the arc reproduced the ambient ceiling
exactly and never once exceeded it. Reaching a usable `b` needs `b = s`, which has not
been observed in a single cell. That is not a disproof, but H7 should no longer be
listed as evidence-free, and the entry should say which direction the evidence points.

**§4b cells nominated in batch 18.** Still none, and now for a stronger reason. Of the
23 degree-five five-row cells — **all with `a = 1`**, recomputed independently — four
are settled: `(4,4,4,4,4)` excluded by null cone, `(12,2,2,2,2)` by B18-06's covariant
family, `(9,7,2,1,1)` and `(7,7,4,1,1)` at the first determinant point. **Nineteen
remain untested**, and a sweep is issued. Record them as *untested*, not as candidates
and not as excluded.

**§9 recommendations.** 05: the bounded attempt is spent and delivered; the only
outstanding item is the control repair. 08: stop, unchanged. 07: hold, unchanged and
now better supported, since revision 2 supplies no construction either.

## 5. One thing to add to §4

A precondition the table does not currently carry, which B18-02 and the integrator
established between them: **`a >= 1` is a precondition of any five-row gate, not a
refinement of it.** A cell selected by `s`, `b` and `U` alone can be empty in the
ambient — both of B18-02's illustrative cells have `a = 0`, and no five-row
`lambda ⊢ 12` has `a > 0` at all. Any future nomination records `a` first.

## 6. What enters the index

| id | statement | status |
|---|---|---|
| `ten_excluded_cells_exact` | The ten excluded ten-row cells `(4d − t − 16, t, 2^8)`, `t ∈ {15,17,19}`, `d ∈ [23,27]`, with `a`, `i_det`, `U` and `D upper = U − (a − i_det) ∈ [−130, −30]`. Padding ceiling `U/a ∈ [0.671, 0.836]`. Exclusion is by exact determinant floors against a reviewed padding ceiling; it does not depend on `s` or `b` | MEASURED, exact; every row recomputed here |
| `partial_is_not_proved` | A session's partial output on disk is an unfinished session, not a finished proof. Accepted lines from a partial review are transcribed only from that review's own closing ledger, never from its intermediate sections | RECORDED rule |

## 7. Carry-forward

1. §2a still waits for slot 10's own §5 ledger. The resume is issued. Do not transcribe
   from §§1–2.
2. §7 and §10 need the updates in §4 above before the next board is read by anyone.
3. Add `a >= 1` as a precondition to §4's conventions block.
