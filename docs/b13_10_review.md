# B13-10 review — a leaner raising-row construction

board_numbering: batch13
session_id: B13-10
models recorded by the session: **`Claude Fable 5.1`** through `e5c29c5`, then
**`Claude Opus 5`** — 2 and 4 commit trailers
bundle: `b13_10_lean_rows.bundle` (one part)
base: `00495110c62acfbbbc951e82cc218ed091563b3f`
head: `4a2d4698eb399f5407681e009994832f5473ac42`
status claimed: **the construction is bit-identical and materially leaner, and
the wall is gone**
integrator verdict: **accept and merge. The board aimed this session at a
bottleneck three other sessions measured as the wrong one — and it broke the
specific wall the board named anyway, and closed a cell. Two small delivery
defects; the mathematics and the engineering both stand.**

---

## 1. Zero-cost checks

| check | result |
|---|---|
| md5 | `1ae634afca4287bf50f0b2415b2849b1` — matches |
| `git bundle verify` | "is okay" |
| **bundle refs** | **`HEAD` only — the named branch `b13-10-lean-rows` is NOT carried**, so `git fetch <bundle> b13-10-lean-rows:…` fails with *"couldn't find remote ref"*. Fetching via `HEAD:` works. See §7. |
| declared base | `0049511` — equals `origin/main` and my tip |
| applies | clean; 78 files, 3,583 insertions, **0 deletions**; 6 commits |
| single-writer files | **none touched** |
| **frozen engine** | **`wk9_s45_build`, `wk11_s71_hybrid`, `wk12_s79*` all unmodified** — exactly as pre-registered, and it is what makes every banked number a genuine reproduction rather than a re-run of changed code |
| 5 MB rule | none close |
| `Claude-Session:` | **present on all 6 commits** |
| pre-registration | `77ad539` before any measurement; addendum A at `e5c29c5` before the cells it governs |

Every load-bearing figure reproduces:

| stated | recomputed |
|---|---|
| `E.data` int16 justified by an entry bound of 480 | `\|Stab\|·δ·(n+1) = 12·8·5 = 480 < 2¹⁵` ✓ |
| pilot rate 1.30 GB per `10⁸` | `1.904 / 1.467 = 1.30` ✓ |
| ceilings `≈2.8×10⁸` and `≈5.4×10⁸` at 7 GB | `7.0/2.48 = 2.82`, `7.0/1.30 = 5.38` ✓ |
| whole cell 24.0 minutes | `812.1 + 40.4 + 307.8 + 280.8 = 1441.1 s` ✓ |
| operator 664 MB compact | `110,695,059 × 6 B = 664 MB` ✓ |
| `(12,4,4,4,4,4)₈` above the pilot by 1.47× | `2.16/1.467 = 1.47` ✓ |

---

## 2. The result: the wall my board named is gone

**The pilot is the cell `docs/batch13_board.md:322` names as the wall** —
`(10,6,6,6,2,2)₈`, `N_S·δ = 1.47×10⁸`, where s79 was ended by the box inside
`E_45` with the rows over 4 GB.

**It builds in 812 s at a peak of 1.963 GB**, and on each of the four blocks s79
did finish, the lean build's row and nonzero counts agree with s79's log exactly
— twelve integers from different code on a different day. Then the kernel runs at
both primes inside the same box, every vector verified on `E`, and

    mult_det((10,6,6,6,2,2), 8) = a = 10 at both primes,  so  i_det = 0   (PROVED over Q)

**s79's Q1 queue now has no cell left below its cap.** Whole cell — build,
kernel, evaluation — 4.53 GB and 24.0 minutes.

The scope is stated correctly and not inflated: only the determinant family was
evaluated; `mult_pad`, `mult_red` and `mult_per4` are priced, not done; and
`i_det = 0` is a statement about that weight alone.

**The suite is the real evidence.** 20 of 20 cells return the **identical
operator** — same shape, `indptr`, `indices` and integer `data`, plus the same
`M`, `col_of`, `sgn`, `n_χ` — not an equivalent row space. The row-multiset
fallback was never needed. And the session says exactly why that matters: *"Two
incorrect operators can share a sampled rank; they cannot share every one of the
23,818,432 entries of `C6`."* Every kernel was verified against the **old,
uncompressed int64** operator, and every banked evaluation rank reproduced at
both primes, **including all four deficient ones**.

**And it is faster as well as smaller** — 1.77× to 2.64× less memory at
**0.40–0.90× the wall time** on the large cells. The pre-registration expected a
memory-for-time trade; there isn't one in the default setting, because the old
builder's second pass over the target codes and its int64 temporaries cost time
as well as bytes.

---

## 3. The finding neither B13-09 nor B13-10 made

B13-09's central defect was that `wk9_s45_build._canon_acc` makes **two passes
over the stabiliser group**, so orbit setup is `O(|Stab| · N_S)` — invisible at
length 6, fatal at `|Stab| = 5040`. Its requested fix was *"a single pass over
the group that accumulates `canon` and `acc` together"*.

B13-10's lean builder does exactly that — "one pass over the target codes,
chunked canonicalisation". **And the suite's own time column confirms it worked,
though neither report says so.** Sorting the twenty cells by stabiliser size:

| `\|Stab\|` | cells | median lean/old **time** |
|---|---|---|
| ≥ 120 | B1, C1, C4, D1, X1, X2 | **0.53×** |
| ≤ 6, non-trivial work | A4, B4, B6, C3, C5, C6 … | 0.63× |

The two `|Stab| = 120` cells with real work are **the two fastest in the whole
suite** — `C4` at 0.40× and `D1` at 0.42×, i.e. 2.4–2.5× faster — and the two
`|Stab| = 240` cells follow at 0.50× and 0.56×. **The biggest time wins land
exactly on the highest-stabiliser cells, which is precisely B13-09's wall.**

Two caveats, so this is not over-read: the suite tops out at `|Stab| = 240`
against B13-09's 5040, and **the lean builder was deliberately not wired into any
production driver** (§8.4), so B13-09's `(10,2⁷)_8` would still fail today. The
fix exists, is measured in the right direction, and is not connected to the
queue that needs it. **That connection is the single most valuable thing to do
with this delivery.**

---

## 4. Where the three "wrong bottleneck" reports now stand

I passed on three independent reports that B13-10's brief named the wrong wall.
All three were right about their own queues, and B13-10 succeeded anyway. Both
are true, and the resolution is worth stating precisely:

| session | its wall | does B13-10 address it? |
|---|---|---|
| **B13-05** | the kernel/decision on the cubic degree-9 queue, 20× the build | **No.** Unchanged. |
| **B13-08** | kernel check + evaluation rows, and the `n_χ ≥ 2²¹` exactness bound | **No** — and B13-10 confirms it from the other side: *"the constraint has moved to the consumer"*, 1.96 GB build against a 4.53 GB whole cell. |
| **B13-09** | orbit-setup **time**, `O(\|Stab\|·N_S)` | **Yes**, by §3 — measured, but not wired in. |
| **the board's brief** | peak memory in the raising-row build | **Yes, and it was real** — but for a reason the brief got wrong: see §6. |

So the brief was not wrong about *whether* there was something to fix. It was
wrong about *what the object was*, and three sessions correctly reported that its
stated bottleneck was not theirs. **B13-10 fixed the builder and the consumer is
now the wall — which is what B13-05 and B13-08 were telling me all along.**

---

## 5. Two inherited defects, both verified in the tree

1. **`wk11_s71_hybrid.hybrid_kernel` raises on a complete cover.** Confirmed:
   line 266 sets `ublock = nU`, and line 279 is `for b0 in range(0, nU, ublock)`.
   With `nU = 0` that is `range(0, 0, 0)`, which raises `ValueError: range() arg
   3 must not be zero` — I reproduced it. It is reachable exactly when the
   initial-term cover reaches every column, i.e. when the operator has **certified
   full column rank** and `a = 0`. No sweep has ever hit it because no sweep
   queues `a = 0` weights; **any census that enumerates them will.** The lean
   wrapper returns the empty kernel with a certificate; `wk11_s71_hybrid.py` was
   correctly left unedited, and a one-line guard upstream is mine to apply.
2. **`E.data` narrower than int64 breaks the hybrid under NumPy 2.** Confirmed on
   this box: `int16_array % 2147483647` raises `OverflowError: Python integer
   2147483647 out of bounds for int16` under NumPy 2.4.4. `hybrid_kernel_lean`
   upcasts in chunks at exactly those two points. **Any future consumer of a
   compact `E` meets the same wall**, so this belongs in the preamble.

---

## 6. Defects in my board — one of them the sharpest of the batch

**"The rows exceeding 4 GB" mis-describes the object, and the mis-description
points at the wrong remedy.** The rows at that cell are 110.7 M nonzeros —
664 MB compact, which I verified. *"The 4 GB was the transients, not the
operator. That distinction is what made the cell reachable, and a brief that says
'the rows exceed 4 GB' invites the wrong fix (a bigger box) rather than the right
one."*

That is the most useful defect report in the batch. My brief described a symptom
as if it were the object, and a session following it literally would have asked
for more memory instead of narrower dtypes and one fewer pass.

**"Lengths 5, 6 and 9 where banked cells exist" has no length-9 instance.** A
scan of every `results/**/*.json*` finds **no cell of length ≥ 8 the raising-row
builder has ever built**, and all sixteen length-9 candidates priced here have
`a = 0`. The suite substitutes the banked length-7 control `D1` and two `a = 0`
length-9 operator checks, and says so. `D1` earns its place: it is the only
suite cell where the record's determinant rank is **deficient** (5 against
`a = 6`), so it tests the instrument's ability to see a drop, not only to confirm
fullness.

**"Its production consumers are batch 14's" is true of the builder but not of the
pilot**, which necessarily produced a new mathematical result in s79's frozen
queue. It sits in `results/b13_10/pilot.json` and is **not** merged into
`results/s79_cells.jsonl`, whose schema carries four families and not one.
Deciding where it goes is mine.

---

## 7. Conduct — including the fifth appearance of one error class

**The rank comparator would have reported PASS on an empty comparison.**
`banked()` took the first record matching `D1` in `results/s69_sizes.jsonl`,
which is that session's `SPANNING_FAILED` first pass with every rank `None`; the
comparison came back `{}` and the cell passed on the operator and kernel tests
alone. The session names it correctly: *"That is the batch-12 failure mode the
preamble names — a check that silently drops its own targets."* Found and fixed
mid-session; the record is now chosen by carrying measurements, a cell whose
banked multiplicities cannot all be placed **fails**, and **every cell was re-run
under the fixed comparator**.

**That is the fifth occurrence in batch 13** — my `E·v = 0`, B13-04's
`__main__`-guarded function, B13-03's hypothesis guard, B13-08's Control C, and
now this. Five of nine sessions independently hit or guarded against the same
class. It is not a stray mistake; it is the characteristic failure of this
programme's instruments, and it belongs at the top of the preamble.

Other conduct, all self-reported: one unbounded process before the
pre-registration existed (recorded twice rather than buried); a five-hour
container suspension; twelve suite records discarded after a builder change with
every cell re-run under one code version, and the discarded file retained as
audit rather than as record. The stopping-rule deviation is in the session's
favour — the re-run loop used a **tighter** `ulimit` than pre-registered.

**Delivery defects, both small:**

- **The bundle carries `HEAD` only, not the named branch.** `git bundle
  list-heads` shows one line and no `refs/heads/b13-10-lean-rows`, so the
  by-name fetch fails. **This is the third appearance of this exact issue**:
  B13-08 caught it in itself by replaying into a fresh clone before delivering,
  B13-09 documented it in its `.md5` header, and B13-10 shipped it. It costs
  nothing here — `HEAD:` works — but it is now unambiguous that the preamble
  needs the incantation.
- A small internal inconsistency: §2.4's `×mem` column gives `B5` 2.19× and `C4`
  2.64×, while §7's scorecard quotes 2.24× and 2.71× for the same cells (`B6`
  and `B7` agree). Probably raw peak versus peak-above-baseline; the table is the
  one to trust.

**Attribution.** Six commits, 2 Fable + 4 Opus 5, and **all six carry the
session-link trailer**. That makes four of five Fable→Opus 5 sessions complying
(B13-04, B13-05, B13-09, B13-10) against one declining (B13-08). Same mechanical
fix.

---

## 8. Discipline worth recording

Three things this session refused to overclaim, all unprompted:

- **On `D1`**: *"a modular rank of 5 proves `mult_det ≥ 5`, hence `i_det ≤ 1`,
  and nothing whatever about `i_det ≥ 1`. The record's own `i_det = 1` there is
  s69's inherited value and is not re-established here."* That is the corrected
  discipline exactly.
- **On the phase attribution**: the pre-registration's reading of *where* the old
  builder's peak sits was never measured, because the old builder was never
  phase-instrumented. *"What is measured is the outcome … not the attribution."*
  The reading is offered as design rationale and labelled as a reading.
- **On `fo='inplace'`**: its equivalence is banked on three cells at both primes;
  its **saving is measured nowhere**, and the ~0.7 GB figure is *"arithmetic from
  the size of the `F_o` copy, not a measurement, and is labelled as such."*
- **On the fifteen degree-13 predecessors**: *"Nothing in this session should be
  read as putting `I(D₉^{per₃})₁₃` in reach."* The cheapest few come within 1.4×
  of the pilot; the dearest is `1.05×10¹⁰` and stays out of reach. Given how
  easily this result could have been oversold against B13-01's route, that
  sentence is worth a lot.

And P4′ is **recorded as not fired** with the reason — `triples='recompute'`
moves the raising-phase peak by ±4 %, because after the dtype and target-table
changes the stored triples are no longer the largest live allocation. The knob
that pays is `blocks='disk'`, at 0.64–0.83× the lean peak for 1.02–1.14× the
time. A prediction that fails for a reason the design explains is more useful
than one that hits.

---

## 9. Actions

1. **Wire the lean builder into the production drivers** — this is the highest-
   value item in the batch. `wk12_s79_per6`, `wk12_s79_cell6` and the rest still
   call `wk9_s45_build.build_cell`. Doing so gives B13-09's `(10,2⁷)_8` at
   `|Stab| = 5040` a chance it does not have today, and unblocks B13-08's 47
   remaining degree-10 weights and B13-05's degree-8 completion.
2. **Apply the `a = 0` guard** to `wk11_s71_hybrid.py:266–279` — one line,
   verified reachable, and any census enumerating `a = 0` weights will hit it.
3. **Re-price the open regions with the measured build rate.** The eleven
   degree-10 cubic weights blocking `I(D₆^{per₃})₁₀` are `N_S·δ = 1.0–2.7×10⁸`,
   the cheapest **below** the pilot; `(12,4,4,4,4,4)₈` at `2.16×10⁸` is ≈ 2.8 GB
   and ≈ 20 minutes and is *cheaper downstream* than the pilot because
   `|Stab| = 120` compresses its `n_χ` sevenfold. Correct
   `docs/batch13_board.md:322` and `docs/stocktake_batch12.md` §7 — the latter for
   the fourth time this batch.
4. **Decide where the pilot's `i_det = 0` is banked.** It belongs in the
   determinant record; `results/s79_cells.jsonl`'s four-family schema does not fit
   a one-family row. Either extend the schema or open a companion file.
5. **Measure `fo='inplace'`** before the next production sweep — the consumer is
   now the binding side.
6. **Preamble**: the `git bundle create` incantation that carries the named
   branch ref (three sessions, three encounters); the NumPy-2 narrow-dtype wall;
   and "a check that cannot fail is not a check" at the top, with five worked
   instances.
7. Price and run the three remaining families at the pilot cell — under an hour
   by this session's own rates — if the record wants a four-family row.
8. On the deferred verification pass: rebuild one suite cell with the lean
   builder and confirm the identical operator independently, and re-derive the
   int16 entry bound at the pilot.
