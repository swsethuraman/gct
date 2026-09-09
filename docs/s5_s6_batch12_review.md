# Batch-12 S5 and S6 — integrator review

Both staged at `results/astra/S5/`, `results/astra/S6/`.  With these, all six
theory sessions have reported.  Three Claude sessions — s74, s76, s79 — have not.

---

## 1. S5's most important result is a limit, and it reframes the ladder

Buried in §9 is the sharpest statement anyone has made about what this programme
can deliver.  The LMR family has `r = 2n + 1` rows; a padded `per_m` model has
`m² + 1` variables; so the family is only admissible when

    2N + 1 ≤ m² + 1,   with m ≤ N     ⟺     N ≤ m²/2.

I checked it across the ladder:

| `n` | rows `r = 2n+1` | is `ℓ·per₃` admissible (10 vars)? | minimal `m` |
|---|---:|---|---:|
| 3 | 7 | yes | 3 |
| **4** | **9** | **yes — and this is the last one** | 3 |
| 5 | 11 | **no** | 4 |
| 6 | 13 | no | 4 |

**The `n = 4` LMR cell is not an arbitrary choice of laboratory — it is the
largest determinant size the `per₃` model can express at all.**  `m = 3` admits
`N ≤ 4`.  That is why the programme is at `n = 4`, and why S5's `n = 5` successor
must switch to `z·per₄` (degree 5, 17 variables), which S5 states.

And the scope consequence, which is the part to carry into any write-up:

> This family probes a **quadratic** determinant-size scale.  `N ≤ m²/2` means it
> cannot express `N = m^c` for any `c > 2`.  A finite obstruction here would be a
> genuine multiplicity obstruction and the first of its kind, and it would support
> a quadratic lower-bound programme — **it would not establish a Valiant-level
> superpolynomial separation.**

Nobody had said this.  It does not diminish the target; it fixes what the target
means, and it should be stated in any paper before someone else states it.

## 2. S5's other content

**Certified, by a better method than the house standard.**  `a₄₀ = 17,107` by
**five-prime CRT with a modulus exceeding an explicit integer upper bound** —
`4.57×10⁴⁶` against a bound of `2.67×10³⁷` — so this is a genuine certification,
not two-prime agreement.  `B₄₀ = 176,451`: the stable precursor is `176,452` and
the sole finite correction is identified exactly as
`[S^{(2⁹)}] Sym⁹(Sym²) = 1`.  Hence the last ladder birth is exactly **one**,
mirroring `b₂₄ = 1` at `n = 4`.

**An outstanding pre-batch item closed as a side effect.**  S5's independent
multiplicity engine "recovers `a₂₄ = 274` and stable `B_∞ = 2169`; the known single
boundary correction returns `B₂₄ = 2168`."  That is **the independent second-engine
re-derivation of `B₂₄`** that the reconciled proposal's §0.3 asked for and that no
session had done.  It arrives as a control rather than as a deliverable, which is
the best way for it to arrive.

**Topology, exact**: 15 channels, 250 two-step paths, 54 endpoints, 42,533 nodes,
671,954 edges, peak 1,661 shapes.  Note the shape: nodes rise 5.6× and edges 7.6×
from `n = 4`, but `a` rises **62×** and `B` **81×** — *topology understates the
weighted cost*, which is exactly the correction S3 made to my DAG-node framing and
it now has a second instance.

**The honest verdict, and it is a stop.**  The current dense/streamed recursion
needs 441 GiB (full residual) or 232 GiB (streamed `B²`) against a 7 GiB cap, from
the *proved lower bound* alone.  **KILL for this implementation**, correctly
labelled as an implementation verdict rather than a mathematical impossibility.
A future S5 route must be genuinely sparse, endpoint-blocked, black-box or
quotient-first.

**Bounds, with the slack admitted**: `335,795 ≤ C_residual ≤ 7.5×10³⁷`.  The upper
bound is deliberately coarse and S5 says so.  It also notes that the two planning
anchors — my `C₂₄/B₂₄` ratio projected forward, and top-multiplicity × path count
— give 1.38M and 4.28M, differing threefold, and concludes that neither is a
bound and a direct measurement is needed.  That is the right treatment of my own
estimate and I accept it.

---

## 3. S6 is a genuine audit, and its independent checks are the batch's best

It re-verified every frozen manifest (S1 60/60, S2 218/218, S3 37/37 plus
continuation 59/59, S4 68/68) and **independently recomputed at both house
primes**: S1's transported minors, S3's 29-minors and `R·U = 0`, S3's
common-source bridge, S4's `12×12` padded minors, and all 57 weight-13 `a_∞`
values.  Several of those I had also recomputed here; we agree everywhere.

It also caught itself — an S1 replay helper rewrote a JSON's formatting, and the
file was restored byte-for-byte from the frozen archive and re-hashed before the
final check.  That is the right way to report a self-inflicted perturbation.

**Its stable census confirms mine independently**: 57 partitions, 10 zero, 47
positive, 11 closed at `a_∞ ≤ 3`, five open at `a_∞ = 4` — and the five tails are
**the same set** as my census returns.  It goes further than I did and gives the
cost order, which is directly useful:

    (6,3,3,1) 1,668 · (4,4,3,2) 3,716 · (6,2,2,2,1) 4,636 · (5,3,2,2,1) 6,922 · (5,2,2,2,2) 9,166

Its bottom line is the right one: `2 ≤ rank T_det ≤ 273`, `12 ≤ rank T_pad ≤ 274`,
`D` **OPEN**.

## 4. Where S6's audit is wrong about the Claude sessions — and the cause is mine

S6 writes:

> "No correctly assigned, completed report/manifests were available for finalized
> s74 … s79.  An available file named `s78_report.md` studies bounded r=5
> elimination — the finalized **s77** mission — not stable M6."
> **REJECT** — "s78-labelled r=5 report as finalized s78 completion; assignment
> mismatch."

**That rejection is incorrect, and the confusion is my fault.**  Our board
renumbered: I split the reconciled proposal's s75 into two sessions and merged its
s78 and s79 into one, so **our s78 *is* the r = 5 session by design**, adjudicated
by the principal and documented with a mapping table on page one of every brief
and in `docs/batch12_worker_preamble.md`.  S6 audited from the launch packet's
numbering and never saw that table.

So: the r = 5 report is a correctly assigned, completed **s78** deliverable in
this board's numbering.  It is merged at `5a7bc55` and reviewed in
`docs/s78_review.md`.

Two further corrections of fact, both from S6 running before or without the
bundles:

- **s75 and s77 have completed reports and bundles**, both merged here (`b6fc844`,
  `5784094`) with reviews.  s75's headline — both halves of the `δ = 12` control
  pass — is exactly the thing S6 lists as missing ("no report supplied a
  deterministic … source evaluated on both target families").  It is half right:
  no session supplied a *274-dimensional* source; two supplied evaluable sources
  at the control.
- **S6's S5 disposition is stale**, not wrong-headed: it saw S5's artefacts before
  the report existed, and read the precursor numbers as `a₄₀` (`a₄₀ = 17,107`;
  `176,451` is `B₄₀`).

**The lesson is mine to record.**  I renumbered the board for reasons I still
think were right, and I mitigated with a mapping table.  It was not enough: an
auditor working from the other numbering mis-filed a completed session as missing
and rejected it for an assignment mismatch that does not exist.  **A mapping table
protects the workers who receive briefs; it does not protect a reviewer who never
receives one.**  Any future renumbering must push the mapping into the artefacts
themselves — a `board_numbering` field in every report and manifest — not only
into the briefs.

## 5. What S6 gets right that is uncomfortable and should stand

- "No report supplied a deterministic 274-dimensional rational source basis
  evaluated on both target families in the same ordering."  True, and it is the
  batch's headline gap.
- The 46-vs-47 stable count: **REJECT 46**, and `(5,3,3,2)` stays.  Settled twice
  independently now.
- Modular kernel ≠ rational kernel; sampled deficiency is not an upper-rank
  certificate.  Repeated because it keeps needing repeating.
- Its conditional batch-13 board is branch-structured on the exact outcome rather
  than on optimism, with kill conditions and verification routes per slot.  I
  would adopt its shape.

## 6. Ledger

| claim | status |
|---|---|
| `N ≤ m²/2`: the family probes a quadratic scale only; `n = 4` is the last `per₃`-admissible rung | **PROVED (S5); re-derived here across the ladder** |
| `a₄₀ = 17,107` | CERTIFIED (five-prime CRT above an explicit bound) |
| `B₄₀ = 176,451`; last birth exactly 1 | PROVED (S5) |
| independent second-engine `B₂₄ = 2168`, `a₂₄ = 274` | **CLOSED as an S5 control** — an outstanding pre-batch item |
| S5 exact topology (42,533 nodes, 671,954 edges, peak 1,661) | EXACT |
| current dense/streamed `n = 5` recursion | **KILL for this implementation** (441 / 232 GiB vs 7 GiB), not a mathematical bar |
| exact `C_residual`, `C_total`, `C_peak`, S5 ranks | OPEN |
| all four frozen manifests; both-prime recomputation of S1/S3/S4 minors | PASS (S6), agreeing with my own checks |
| 57 / 10 / 47 and five `a_∞ = 4` tails, with cost order | CONFIRMED — same set as my census |
| "no correctly assigned s74–s79 deliverables" | **INCORRECT** — s75, s77, s78 are complete, merged and reviewed; the numbering collision is mine |
| `2 ≤ rank T_det ≤ 273`, `12 ≤ rank T_pad ≤ 274`, `D` | OPEN — the batch's honest status |
