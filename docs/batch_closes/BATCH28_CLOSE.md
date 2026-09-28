# Batch 28 — closed

**Written 2026-09-28 by the integrator from committed records.** The coordinator's seal goes in
its Batch 28 ledger, and is committed in the first Batch 29 delivery pass. This file summarizes
the batch; it does not replace the seal. The integrator verified every manifest below by hashing
each payload on the host.

## Headline

Batch 28 made the first new determinant-rank measurement in the programme's hardest regime, and
certified it.

- **Cell A is closed.** `λ = (12,8,6,4,2)` at `k = 8`, with `a = 109` and `n_χ = 813,314`, has
  `mult_det = 109 = a`, so it contains **no determinant equation**.
  - This was the largest unmeasured degree-8 cell, and the most plausible place for a degree-8
    equation.
  - It was priced out until B27-06. It ran in about 16 minutes of compute on the author's laptop.
- **The transfer lemma is accepted in every form degree.**
- **Paper 3's named open question is updated.** Its smooth-cubic form is answered by C1, and it is
  now restated for the singular case, which is B27-01's class (iii).
- **No construction was produced.** A25-10's decision stands: **no construction ready.**
- **Binding constraint, unchanged:** No five-row determinant equation is known to be nonzero on
  padding.

## Results

**1 — Cell A certified negative (COMPUTED, cross-lineage).**
- **Result:** `mult_det = 109 = a` at `(12,8,6,4,2)`, `k = 8`. There is **no determinant equation
  in this cell.** None of the four achievements moves; this is a certified negative in one cell.
- **Machinery** (B28-01a → c → d; Claude, laptop under WSL2):
  - B28-01a `a1c3c3a6`, manifest `420eb69a` (186 payloads).
  - B28-01c `5a3174cd`, manifest `93bb78e2` (211 payloads).
  - B28-01d `0f7af8b1`, manifest `2129631d` (63 payloads).
- **Reviews** (Astra):
  - R28-01 `8a86fec1` (`5ffcc018`): YES after repairs P1–P5.
  - R28-01b `93db0679` (`5068e6cd`): P1–P4 ACCEPT, P5 REPAIR.
  - R28-01c `ff62d929` (`66eb68fc`): YES.
- **Measurement:** B28-01b (Claude), tip `467e8402`, manifest `9beba33c` (25 payloads).
- **Cross-lineage replay:** R28-01d (Astra) `1b9c2295`, manifest `76f41c38` (22 payloads), ACCEPT.

**2 — The any-degree transfer lemma (HAND, cross-lineage).** Level: transfer lemma.
- B28-03 (Astra) `e0a8041b`, manifest `ab09c3fd`, **ACCEPTS** R27-K4's lemma for every `d ≥ 1`,
  `1 ≤ r ≤ N`, `δ ≥ 0` and `ℓ(λ) ≤ r`.
- It covers every `eq:lengthred` use in Paper 2, including the cap-proof clause for `n ≥ 3`.
- It clears only the transfer step: the LMR copy and the other cap inputs rest on their own
  evidence.

**3 — Literature READ.** Level: none; no record change.
- B28-02 (Astra) `fd001ddb`, manifest `eedb5373`. Verdicts: **2a = B, 2b = B.**
- **2a:** no known method computes image multiplicities for the degree-4-generated subalgebra.
- **2b:** Hüttenhain (2017) gives explicit size-4 first-order boundary components, which is a lead
  for class (iii). No source decides class (iii).

**4 — B27-04b, six editorial items (author-approved in full).** Editorial only.
- Paper 2: `11e99b25`, manifest `4036bea4`. Paper 3: `181214bc`, manifest `b653306a`.
- Items: the "35" gloss; the cap clause cited through the accepted any-degree lemma; Paper 3's
  Question 6.5; the n=3 cap inputs; PAPER2_GAPS; the stale labels.
- **All 12 edits plus the append applied verbatim.** The integrator compiled both after-states
  clean: 16 and 24 pages, with 0 undefined references or citations.

**Paper 3's Question 6.5, as the author approved.** The smooth form ("a boundary point `ℓ·C*`
with `C*` smooth?") is **answered negatively by C1**. The open question is now a boundary point
`ℓ·C` with `C` singular, `C ∉ D₃₅`, and `C` containing no plane. Whether the cap minors vanish
there is not known.

## What the review chain caught (B28-01)

The arithmetic was never in question: every replay matched byte for byte. Four review rounds
tightened the guard rails:

| round | what it caught |
|---|---|
| **R28-01** | **P1:** failure paths continued. **P2:** the verifier accepted a certificate with its minor missing or with a false recipe (demonstrated). **P3/P4:** the gate underpriced verifier time and memory. **P5:** the wall-clock cap |
| **R28-01b** | The supervisor could leave a child alive after a stop, and could miss a size crossing at step exit (both demonstrated) |
| **R28-01d** | The host sleep setting was still 900 s at first check. The session stopped until the author set it to Never |

These are the reasons the certificate can be trusted, and the frozen machinery is now reusable
unchanged.

## Measured performance (Cell A, B28-01b)

| item | value |
|---|---|
| Sizes | `z = 10,062,442` (about 12.4 n); residual `U = 3,658` (about 0.44 %) |
| Compute | 977 s monotonic across two primes and the independent replay |
| Peak memory | 4.09 GB (scope) |
| Wall time | about 34 min, including a 17.5 min host sleep during the verifier step |

The sleep affected only timings. R28-01d replayed the verifier with sleep off and got the same
bytes.

## What did not happen

- No coefficient equation nonzero on padding.
- No separation.
- No positive multiplicity gap.
- No asymptotic statement.
- No modular deficiency anywhere.

## Integrator errors this batch

The count now stands at 23.

- **22:** proposed a numerical near-membership probe for class (iii) without checking the record.
  That method had already failed its positive control (Grenet at n=7: residual 1.9×10⁻²). The
  author supplied the correction: any such probe must first reproduce member/non-member
  discrimination.
- **23:** B28-01b's brief relied on the author's verbal confirmation that sleep was off, instead
  of a machine check. The Windows AC sleep timeout was 900 s. R28-01d's brief added a `powercfg`
  check that stops the run.
- **Correction accepted from the author:** the claim that the record has "nothing to learn from"
  was wrong. Continuous quantities (`sk − a`, `mult_red`, `i_det`) vary across hundreds of cells.
- **Estimates, not counted:** Cell A came in at the fast end of its priced range.
- Integrator research suggestions are **0 for 5**.

## Errata recorded (no commit needed)

- R27-K4 §3: "necessarily dependent including `r ≥ 10`" should read `r < 10`. Found by B28-03;
  not used in any proof.
- Paper 3 L918 and L924 still write `C^*` after Question 6.5 now uses `C`. This is notation only;
  it goes to Batch 29 (M1).

## Process record

- **Sessions:**
  - 7 producers: B28-01a, 01c, 01d, 01b, 02, 03 and 04.
  - 4 reviews: R28-01, 01b, 01c, 01d.
  - 1 setup pass: PART 27.
- **Stops, all correct:**
  - R28-01 and R28-01b returned NO or YES-after-repairs.
  - R28-01d stopped on the sleep setting.
  - B28-01c's first control run stopped on an over-broad output check.
- **New standing lessons:**
  - Keep timings out of certificate files.
  - Check host power settings by machine, not by word.
  - Freeze and review machinery once, then reuse it.
- **Host:** the author's laptop under WSL2 Ubuntu 24.04.5, 28 GB cap, 20 cores. Installs happened
  inside WSL only, with versions recorded.

## Carried into Batch 29

| # | item | note |
|---|---|---|
| M1 | Paper 3 `C^*` → `C` at L918, L924 | Author ruling 2026-09-28: take it up in Batch 29. One approved find/replace pair |
| M2 | **Degree-8 census** | Measure every unmeasured degree-8 cell with the frozen B28-01d machinery, unchanged. One review per batch of cells. The host preflight must include the `powercfg` sleep check. Price it from Cell A's measured rates |
| M3 | **Cell B**, `(14,10,6,4,2)` at k=9 (`a = 437`, `n = 2,085,864`) | Reprice from Cell A's rates before approval |
| M4 | **Class-(iii) numerical probe** | Controls preregistered first. It must reproduce the recorded discrimination (known member about 10⁻¹⁶, non-member about 0.41) before any target. Positive controls: `p₄` or class-(i) points. Negative controls: `T*`, `T′`. Starting points: Hüttenhain's size-4 components. A lead generator only |
| M5 | **Multiplicity regression with saliency** (Davies mode) | Targets `sk − a`, `mult_red`, `i_det`, not `mult_det`, which equals `a` everywhere measured. Its outputs are conjectures |
| M6 | Candidate-generation loop | Last in priority, and only with exact membership built in |
| M7 | Image-bound contraction of the s56 Foulkes map | Parked. B28-02 found no known method |
| M8 | G-A1: singular and reducible cubic factors | Now the same object as Paper 3's restated Question 6.5 and B27-01's class (iii) |
| M9 | A26-01 literature priority; Application 3's floor (CERTIFIED-modular); A26-03's padding value; `n > 4`; signed combinations | Unchanged |
| M10 | Commit the coordinator's sealed Batch 28 ledger | In the first Batch 29 delivery pass |

## Delivery

PART 28 (`HOUSEKEEPING_B28_PART28_CLOSE.md`) makes one close pass:
- it merges `b28-02`, `b28-03`, `b28-01` and `b28-01r` into `batch15-launch`;
- it fast-forwards `b24-06-paper2` and `b23-04-paper3` to B28-04's tips;
- it commits the sealed Batch 27 ledger (`45a0a0ec`), this file, and the Batch 28 briefs,
  including the approved wording draft.
