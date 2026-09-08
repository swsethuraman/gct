# Batch 12 — the plan

Sessions **s74–s79** (Claude) and **S1–S6** (Sol).  Base: the tip of `main`
after the push of §0.  This plan is written against
`docs/stocktake_batch11.md`, which is the record it follows from.

---

## 0. Before anything: the push

`origin/main` is at `226b4ef1` and local `main` is **65 commits ahead**.  Every
session of batch 11 cloned the pre-batch commit; two of them rebuilt machinery
that was already banked, and one of those two rebuilds has never been compared
against the original.

**Batch 12 does not go out until `git ls-remote origin refs/heads/main` returns
the commit that contains this file.**  That is not a process preference; three of
the six Claude sessions of batch 11 recorded the consequences in their reports.

The check itself is being fixed, not just repeated — see §6.

---

## 1. What this batch is for

Batch 11 broke the wall.  The bottleneck that defined batches 9, 10 and 11 —
*`dim M_λ = 274` and every realisation needs `≥ 10⁷` coordinates* — is gone, in
two independent ways:

    bracket circuit (s69)      evaluate a highest-weight vector at LMR:  0.13 s
    block-swap recursion (S5)  precursor at LMR:  B_24 = 2 168 dimensions

**So the bottleneck has moved, and batch 12 is organised around where it moved
to.**  It is now *basis enumeration*: `mult_X` at LMR is a rank on the same
`274 × K` evaluation matrix for every variety `X`, and every one of those ranks
is cheap **once 274 spanning vectors exist**.  s69 prices that at 12–15
CPU-hours by sampling; S5's recursion may give it by construction; and a
straightening basis would give it in closed form.

The design principle is unchanged and it is the one that just worked:

> **Fund the bottleneck redundantly; do not make the batch wait for it.**

Batch 11 funded the old bottleneck three ways and one of the three broke it.
Batch 12 funds the new one three ways — sampling (C1), recursion (C2), and a
combinatorial basis (S1) — and keeps the other nine sessions productive if all
three stall.

**The prize is specific.**  If any of the three lands, `D` at the LMR cell is
decided; and by s73's flat-ladder argument together with s57's measurement that
the LMR cell is the first stable cell of its ladder, **`D(24)` decides `D(δ)` for
every `δ ≥ 24` at once**.  The `n = 4` question is one cell, not a ladder.

---

## 2. The board

### Claude — sessions 74 to 79

| | mission | gate | success | stopping rules |
|---|---|---|---|---|
| **C1 / s74 — LMR basis by sampling, then the decision** | **Resume** s69's checkpointed run (`results/s69_lmr_state.json`, `results/s69_ladder_n4.json`, `analysis/wk11_s69_*`) — do not restart it. Climb the ladder, sampling only for the `a_δ − a_{δ−1}` new directions per rung. Then, on whatever span is reached, evaluate at **four** families on the *same* vectors: `det_4` pencils, reducible `ℓ·c`, padded `ℓ·per_3`, and unpadded `per_4`. | none | 274 spanning fillings, generic rank 274 at both primes, then `i_det`, `i_red`, `i_pad`, `i_{per₄}`, `U_D`, `U_P`, `dim(U_D ∩ U_P)` and **`D`** at LMR | span stalls: report the rank curve, the per-rung tail, and the four columns **on the span reached** — a rank on a proper subspace is a lower bound on `mult`, which is the useful direction |
| **C2 / s75 — LMR basis by recursion, then the same decision** | Build `M_λ` as `ker(τ − I)` on the `B₂₄ = 2 168`-dimensional precursor (`docs/s1_s6_batch11_review.md` §3, `results/wk11_int_b24.json`). **Two-part control at `δ = 12` first**: recover `dim M₁₂ = 2` from the 31-dimensional precursor **and evaluate the two vectors it returns** against determinant points, reproducing s69's banked `i_det(12) = 0`. Then climb. Same four columns as C1. | none | the two-part control, then a basis and the same decision table | the control's *second* part fails — the recursion produces the right dimension but not evaluable vectors. That is the route's real risk and it is a full result |
| **C3 / s76 — the `ℓ = 6` padded frontier** | The washout theorem says nothing at length `≤ 5` bears on the permanent and length 6 is the first that can. s71's hybrid (10 s where the Wiedemann route took 3 094 s) and s69's circuit both reach cells that were priced out. Push the `ℓ = 6` frontier: the first cell with `i_det ≥ 1`, or with `mult_pad < mult_red`. | none | a new `ℓ = 6` cell with either inequality strict | the frontier is bounded by the build, not the rank — report where and at what `N_S·δ` |
| **C4 / s77 — the re-priced frontier** | The cost model changed by four to six orders of magnitude on the source side and two to three below the build wall. **Re-price the census under both new models** — the circuit (`a_δ` fillings × `2^{n₂}2^h` determinants, or the DP's pathwidth cost) and the hybrid (bounded by `N_S·δ`, not `n_χ²`) — and emit a new work queue. | none | a re-priced census and a ranked queue that says what batch 13 can reach | — |
| **C5 / s78 — consolidation, and the certification debt** | Reconcile the **two verifier extensions** (`permanent` vs `permanent_pencil` — a one-word rename across s73's 46 certificates) and the **two certifier implementations** (s67's and s71's, never compared). Back-fill certificates for s63/s64/s66 where the artefacts allow. Define a certificate kind for a split rank and for a hybrid kernel. Adopt one validated hybrid as the house instrument. | none | one verifier, one certifier, the corpus re-verified, the debt of `docs/housekeeping_batch10.md` §4 either paid or re-recorded as unpayable with the reason | — |
| **C6 / s79 — is LMR's the only equation at `ℓ = 9`?** | Sol S1 closed literature retrieval and named the only sensible follow-up: *a direct finite minimality search*, which was out of reach when evaluation cost 415 days a vector and is not now. Search `ℓ = 6, 7, 8` at `δ < 24`, and `ℓ = 9` at tails other than `(17,2⁷)`, for a second `i_det ≥ 1`. | none | a determinant equation in a cheaper cell — which would replace LMR as the programme's laboratory | a characterised negative over a stated, priced region is a full deliverable |

### Sol

| | mission | why now |
|---|---|---|
| **S1 — the straightening basis of fillings** | s69 identified it and did not build it: a combinatorial basis of `M_λ` indexed by fillings (a straightening / plethysm rule), rather than a spanning set found by sampling. **This is the highest-leverage session on the board**: it collapses C1's 12–15 CPU-hours to minutes and removes the coupon-collector tail that is now the programme's only cost. |
| **S2 — the `r = 5` completeness theorem** | s72 proved `dim(D₅ ∩ W) = 31 < 35` on the *enumerated* normal cone and said plainly that completeness of the enumeration is not its to prove. That statement — that `Proj gr_J R` has no component outside the list — is the only thing between s72's number and `R₅ ⊄ D₅` as a theorem. |
| **S3 — `τ` in compact coordinates, and whether the recursion evaluates** | S5's two named residues, and C2's two blockers. Can the block swap be applied without forming `W_δ` explicitly? And — the one that decides the route — does the recursion carry an evaluation map, or does it produce vectors that cannot be paired with determinant points? |
| **S4 — stable `a_∞ = 4` at weight 13** | `a_∞ ≤ 3` is now closed on eleven blocks (S4 batch 11, completed here with `(5,3,3,2)`). The first possible weight-13 stable determinant equation needs `a_∞ ≥ 4`. In cost order, stopping at the first nonzero stable ideal; if all die, raise the threshold rather than run a census. |
| **S5 — the successor, written before the answer** | `D(24) ≤ 0` is a real possibility and the programme should not meet it unprepared. Rank and **price** the candidates: the `n = 5` family member (`δ = 40`, `λ = (151,31,2⁹)`, now priceable with the circuit); other `ℓ = 9` tails; the stable route; a padded model other than `ℓ·per₃`. Written now, so it is not written in disappointment later. |
| **S6 — adversarial audit, and the batch-13 board** | Read code and docs, ignoring session conclusions until the implementation is checked. Batch 11's version of this found four things. Then draft batch 13. |

---

## 3. Gate structure

    ungated (12):  C1 C2 C3 C4 C5 C6   S1 S2 S3 S4 S5 S6
    gated  (0)

**No session in this batch waits on another.**  C1 and C2 approach the same object
by different routes and **both carry the decision table**, so whichever gets a
span first produces `D`; neither is the other's consumer.  Both have the same
ungated fallback if the span stalls: the four columns on the span reached, plus
the `n = 4` `D`-ladder upward from `δ = 12`, where s69 banked `M₁₂` explicitly
(`results/s69_n4_seed.json`) — the `n = 4` analogue of what s73 did at `n = 3`,
and the first padded measurement ever made on the LMR ladder.

This is the first batch since the programme began with no gate at all.  That is
a consequence of the wall falling, not a relaxation of the rule.

---

## 4. Three results that would change the batch mid-flight

Stated now so nobody has to decide at 3 a.m.

1. **S1 delivers a straightening basis.**  Then C1 and C2 both stop sampling and
   use it, and `D` at LMR is a same-night result.  Relay immediately.
2. **C2's two-part control fails on its second half** — the recursion returns
   `dim M₁₂ = 2` but the vectors do not evaluate.  Then the recursion is a
   dimension count, not a source, and S3's evaluation question becomes the whole
   route.  Say so; do not work around it.
3. **`D(24) > 0`.**  The verification protocol takes over before it is reported
   anywhere, including in conversation.  Two primes, two independent evaluation
   families, characteristic zero by rational reconstruction, an independent
   source, and the degeneracy pre-check.  s73 ran the full protocol at `n = 3`
   and its §6 is the template.

---

## 5. Priority

Expected value per unit effort, not execution order:

    S1  >  C1 ≈ C2  >  S2  >  C3  >  S3  >  C6  >  C4  >  S4  >  C5  >  S5  >  S6

S1 is first because it is the only session that can make the other two
unnecessary.  C5 is low on expected *scientific* value and is on the board
anyway, because the debt it clears is the reason two sessions of batch 11 spent
part of a night rebuilding banked machinery.

---

## 6. Process rules

Carried from batch 11, with two changes marked **new**.

1. **new — the tree check keys on the tree, not on the worker.**  Batch 11's
   preamble said "stop if the plan is not in your clone"; it did not fire,
   because the sessions had the brief pasted and could reconstruct what they
   needed.  Batch 12's preamble instead requires, as the first recorded action:

       git rev-parse main
       git cat-file -e main:docs/batch12_plan.md   # must succeed
       git log --oneline -1 -- docs/stocktake_batch11.md   # must be non-empty

   and a report that does not open with those three outputs is incomplete.
2. **new — the integrator verifies the push before the briefs go out**, by
   `git ls-remote`, and records the hash in the batch plan.  The rule that failed
   twice was mine to execute, not the workers'.
3. Read the code before believing a document; cite the file, not the memo.
4. Pre-registration before computation.  `python-flint` for exact linear algebra.
   Both house primes.  Any `D > 0` cell goes through the verification protocol.
5. Bound every run with `timeout` and `ulimit -v`, check `free -g` first, record
   the pid, and end runs **only by recorded id**.
6. Delivery by git bundle only; the proxy's refusal of pushes is an access
   control.  No file over 5 MB.  Commit messages carry
   `Co-Authored-By: Claude Opus 5 <noreply@anthropic.com>` and nothing else.
7. `docs/brief_wording.md` §2 and §4 are binding.  §5 and §7 apply to any new
   statistic or transport.
8. **new, from batch 11's corrections ledger:** any brief that introduces a new
   evaluation column states, in one line of arithmetic, that both varieties are
   proper in the ambient space at the length where the column is used.  Two of
   my briefs have now specified vacuous comparisons for want of that line.

---

## 7. If `D(24) ≤ 0`

The batch still has S2's theorem, S4's frontier, C3's `ℓ = 6` cells, C6's
minimality search and S5's priced successor list — none of which depends on the
LMR answer.  And the record gains what it has never had: **an exact `D` at the
cell the programme was built around**, which converts the central question from
open to answered and points the successor at a different cell rather than a
different method.

The one thing that must not happen is the batch reading a `D ≤ 0` as a failure
of the instruments.  Batch 11 established the instruments: the `n = 3` control
is exact at `D = +1` and holds at every rung as a theorem, `per₄` is a passed
positive control at 223 cells, and `rank S` is two-sided against banked truth at
three.  If `D(24) ≤ 0` it is because the cell is silent, and that is a result.
