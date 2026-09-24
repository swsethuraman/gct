# Batch 27 — closed

**Written 2026-09-23 by the integrator from committed records.** The coordinator's seal is separate:
it goes in the coordinator's Batch 27 ledger, and it is committed in the first Batch 28 delivery
pass. This file summarizes the batch; it does not replace the seal. The integrator verified every
manifest below by staging each payload and hashing it.

## Headline

Batch 27 ran on the new operating model: slot branches, a bounded compute allowance, ladders, and
review folded into each wave.

- **Every producer result is cross-lineage reviewed.** There were three research slots, one
  editorial slot, one review of B26 work, and two no-Git scoping slots.
- The batch mapped where a separating witness can live. It produced a second certified-outside
  padding witness. It retired a bad test point, and it found the exact cost of the next honest
  measurement.
- **No construction was produced.** A25-10's decision stands: **no construction ready.**
- **Binding constraint, unchanged:** No five-row determinant equation is known to be nonzero on
  padding.

## Results (research and review)

**1 — B27-01 (Astra), the padding map.** Level: geometric noncontainment at an explicit point.
- Producer tip `01f78eb2`, manifest `580aa717…`. Reviewed by R27-01 (Claude), `51f9d17e`,
  manifest `5e1b039f…`.
- **Verdict: ACCEPT on all three rungs.** One wording erratum: "B27 acceptance of C1" should read
  "Batch 26".
- **1a, the map.** The 50-parameter family splits three ways:
  - certified inside `D₄,₅`: dimension 45 to 49;
  - certified outside, via C1 on a smooth cubic factor: dimension 50;
  - unresolved: dimension 49. Here `C` is singular, not in `D₃,₅` and contains no plane. Such
    points are excluded as *literal* determinants, but closure membership is open.
- **1b, `T*`.** `T*` is the B17-01 witness. It is re-certified smooth, and R27-01 independently
  validated the witness itself for the first time. `x₀C* ∉ D₄,₅`.
- **1c, degree window at `T*`.** It is `6 ≤ d(T*) ≤ 4⁴⁹`, where the upper bound assumes refined
  Bézout. It narrows to `[8, 4⁴⁹]` under the batch-13 premise. The figures 65, 245, 299 and 300 are
  not upper bounds.

**2 — B27-02 (Astra), the mixed-sign tableau candidate.** Level: rejection of one candidate.
- Producer tip `35eeff49`, manifest `bb55a4e5…`. Reviewed by R27-02 (Claude), `459c32fa`, manifest
  `a57995e5…`.
- **Verdict: ACCEPT outcome 3.** One clerical repair: the report table prints a truncated hash;
  the bindings file is correct.
- The candidate is `f = f_T1 − 567 f_T2`. It meets the reopening condition, sees `B²`, and vanishes
  on `Q²` and `D₄` by construction.
- **It is rejected by a new determinant `E`**, with `f(E) = −175/256`. The two-dimensional span
  contains no determinant equation.

**3 — `p₄` is a determinant.** Level: record fact (test-point retirement).
- **Closure:** B27-01 (Astra) shows `p₄ ∈ D₄,₅` by a Laurent-pencil limit, and R27-01 (Claude)
  ACCEPTS it. That makes the closure statement cross-lineage.
- **Literal:** R27-02 (Claude) shows `p₄ = det diag(w, M)` with `det M = zQ`, and the integrator
  checked this by hand. It is not separately reviewed, but it is consistent with the closure
  statement and immediate to check.
- **Consequence:** every determinant equation vanishes on `p₄`, and on `p_n = z^(n−4)p₄`.

**4 — B27-03 (Claude), the reopening condition at a nonsymmetric witness.** Level: scoped
exclusions and zero-kernel certificates.
- Producer tip `7c36a52d`, manifest `463d9dfc…`. Reviewed by R27-03 (Astra), `8f011f01`, manifest
  `62759639…`.
- **3a, witness: ACCEPT.** `T′ = (x₁+…+x₅)·per₃(A′)` with `A′` nonsymmetric. All 65 retained
  coefficients were recomputed independently. `C′` is smooth by an independent certificate (a
  210-minor, 3123 mod 32003), so `l·C′ ∉ D₄,₅` by C1.
- **3b: ACCEPT.** No reducible literal completion exists. Membership of `π(F′)` in the projected
  closure is open.
- **3c: ACCEPT.** Zero kernel for every `k ≤ 4` in both rings, at the degree-8 weights
  `(24,2,2,2,2)` and `(23,3,2,2,2)`, and along two full rays. The balanced-weight lemma is accepted
  through an independent root-string proof. The first degree with a nonzero kernel is **DEFERRED**.
- **3d: REPAIR.** "None observed" becomes "none found in the spaces tested". Degree-300 equations
  are recorded (C10), and they vanish on padding. The memory estimate `8N(N+16)` prices one array,
  not peak use. "Cannot yield outcome 1" becomes "expected zero kernel, unproved".
- **Reproducibility wording: REPAIR.** Outputs embed wall times, so "deterministic" applies only
  to the mathematical payload.

**5 — R27-K4 (Claude) reviewing B26-10A §2.3 (Astra).** Level: transfer lemma.
- Review `53206b43`, manifest `d63c535f…`.
- **Verdict:** ACCEPT the general degree-4 statement and the `P_r` identification. REPAIR the flag
  inventory: add a scope note at Paper 2 L705–706, n=4. **That note is not yet applied** (L1).
- R27-K4's own any-degree lemma is new Claude work and unreviewed (L2).

## Editorial

**B27-04 (Claude), the accepted edits to Papers 1–3.** 14 of 15 items applied, 1 stopped. Nothing
moves any achievement.

| paper | tip | manifest | items |
|---|---|---|---|
| Paper 1 | `d59ce77a` | `bcd6b425…` | 3 of 3 |
| Paper 2 | `f8326974` | `5130c98f…` | 6 of 6 |
| Paper 3 | `4c5a5450` | `2fc8a591…` | 5 of 6 |

- The item that stopped is Paper 3's "35" gloss. The producer was right: the gloss belongs in
  Paper 2 Rem. 6.3(iv), which was outside the list.
- **The integrator compiled all three after-states clean:** 27, 16 and 24 pages, with 0 undefined
  references or citations. There was one font-substitution warning in Paper 3.
- B27-04 found four stale statements outside its list. The user ruled on 2026-09-23 that these,
  the "35" gloss and the L705–706 note all go to Batch 28 as B27-04b (L1).

## Scoping slots (no Git; outputs committed at close)

**B27-05 (Astra), bound the determinant-substitution image.** Outcome 4, READ-level feasibility.
Folder manifest `325c1c81…`.
- The record already has the exact object: session 56's Foulkes map, whose rank equals
  `mult_det`. Its cost is also recorded: enumeration is priced out from degree 5 on.
- Session 60 measured `mult_det = a` at all 419 of its cells.
- The open problem is a *rank-preserving contraction* of that map, not a new object.

**B27-06 (Astra), price the largest-`a` cells.** Outcome 2, a priced preregistration. Folder
manifest `b713ca8b…`.
- The cells are `(12,8,6,4,2)` at k=8 (`a=109`, `n=813,314`) and `(14,10,6,4,2)` at k=9
  (`a=437`).
- Neither has ever been measured.
- The cheapest method is the s71/s79 blocked hybrid:
  - Cell A: about 0.5–2.2 h with replay, 4–6 GB. The structural worst case is 19 h.
  - Cell B: about 4–16 h, 20–28 GB.
  - A 32 GB machine and 1–2 days to build a determinant-only driver plus an independent verifier.
- A modular deficiency would be a candidate only. **Not approved; decision pending** (L4).

## Rulings and standing items

**The user's Batch 28 direction (2026-09-23):**
- The `SL₄×SL₄` pullback bound is sound. But session 38's symmetric count already shows it never
  drops below `dim H` for `k ≤ 10`, so no slot goes to that scan.
- The target is instead a bound on the substitution image itself.
- The Mulmuley slides are a pointer only.
- B27-04b goes in Batch 28.

**Proposed standing rule** (integrator, from R27-02, for adoption at seal):
- Any padding point offered as a separation witness must carry its own proof that it is not in
  `D₄,₅`.
- The certified witnesses are `T*` (R27-01) and `T′` (R27-03). `p₄` is retired.

**Binding constraint and programme decision:** unchanged.

## What did not happen

- No coefficient equation nonzero on padding.
- No separation.
- No positive multiplicity gap.
- No asymptotic statement.
- No determinant rank measured at any new cell.

## Integrator errors this batch

The count now stands at 21.

- **20:** proposed a Kostka–Kronecker scan without checking the record. Session 38 had already run
  the stronger symmetric count, and session 56 had the exact image object. B27-05 confirmed both.
- **21:** B27-02's brief offered `p₄` as the fallback padding point, but `p₄` is a determinant, so
  rung 2d could never separate anything.
- **Estimates, noted and not counted:**
  - I expected B27-05 to take real effort; the record answered it at rung 0.
  - I expected B27-06's cell to be priced out; it prices at hours.
- Integrator research suggestions are **0 for 4**.

## Process record

- **Sessions:**
  - 5 producers: B27-01 to B27-04, and R27-K4 as the review of B26 work.
  - 3 cross-lineage reviews: R27-01, R27-02, R27-03.
  - 2 no-Git scoping slots: B27-05 and B27-06.
  - 1 setup pass: PART 25.
- **Slot branches worked.** There were no per-slot delivery passes and every packet was clean at
  first check: 0 mismatches across all manifests.
- **Stops, all correct:**
  - B27-04's "35" item.
  - B27-06's ceiling overrun, continued with the user's authorization. The interrupted delivery is
    preserved.
- **Lessons:**
  - Keep wall times out of certificate files (R27-03).
  - Every padding test point needs a non-membership proof (R27-02).
  - Paper 1's CRLF working copy needs an LF rewrite before `hash-object` parity holds (B27-04).
- **Compute:** every run stayed within 10 runs of ≤60 s and ≤512 MB each. The largest was R27-03's
  191 MB peak.

## Carried into Batch 28

| # | item | note |
|---|---|---|
| L1 | **B27-04b editorial follow-up** (user ruling) | Items: the "35" gloss in Paper 2 Rem. 6.3(iv); R27-K4's L705–706 scope note; Paper 3's smooth-cubic statements (abstract, Q6.5, G-33) now contradicted by C1; Paper 3's n=3 cap-input wording (abstract iv, L896–898); PAPER2_GAPS G-P2-18/19; the "PROPOSED, UNCOMMITTED" labels on the B26-05 appends. The integrator drafts the wording and the author approves it. |
| L2 | R27-K4's any-degree lemma | New Claude work; needs an Astra check before anything cites it. |
| L3 | Class (iii) boundary | Closure membership of the 49-dimensional class. Typed question: is some class-(iii) `lC` a first-order limit `tr(adj M₀·M₁)` with `det M₀ ≡ 0`? Needs a literature check first. |
| L4 | **B27-06 Cell A** | User decision: approve degree 8 alone (32 GB, ≤24 h, 1–2 days build) or decline. Cell B stays unrun. |
| L5 | Image-bound problem | A rank-preserving contraction of the s56 Foulkes map. Pointer only; the producer must name an intermediate object and its price. |
| L6 | B27-03 follow-ups | First nonzero kernel degree (DEFERRED); `π(F′)` in the projected closure (open). |
| L7 | READ-slot candidate | Is there a known algorithm for multiplicities in the subalgebra generated by the degree-4 left-right semi-invariants of `M₄(ℂ)⁵`, faster than the Foulkes carrier? |
| L8 | G-A1, singular and reducible cubic factors | Open (was K5). |
| L9 | A26-01 literature priority | DEFER (was K6). |
| L10 | Application 3 floor | CERTIFIED-modular, one prime (was K11). |
| L11 | A26-03 padding value; `n>4`; signed combinations | Low priority (was K12). |
| L12 | Commit the coordinator's sealed Batch 27 ledger | In the first Batch 28 delivery pass. |

## Delivery

PART 26 (`HOUSEKEEPING_B27_PART26_CLOSE.md`) makes one close pass:
- merges the seven research and review branches into `batch15-launch`;
- fast-forwards the three paper branches to B27-04's tips;
- commits `BATCH26_CLOSE.md`, the sealed Batch 26 ledger (`66b4869d…`), this file, the Batch 27
  launch briefs, and the B27-05 and B27-06 folders.

Receipts are recorded in that pass's report.
