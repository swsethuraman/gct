# The six Claude sessions — where I differ from the reconciled proposal

Integrator response to *Batch 12: Review of Claude's Proposal and Final
Reconciled Roadmap* (8 September 2026).  **The Sol/Astra board S1–S6 is adopted
as written** and is not discussed below except where a Claude session feeds it.
This document covers only s74–s79.

---

## 0. The call, in one table

| | reconciled proposal | mine | why |
|---|---|---|---|
| s74 | direct circuit sampling to the decision | **same** | no change |
| s75 | S5 recursion: 31 → 2 control **and then** 2168 → 274 | **the control only** | the two halves are different-shaped problems and the merge is a gate inside a session |
| s76 | deterministic circuit basis / straightening | **the scale to δ = 24, with exact `C₂₄`** | freed by the split; carries a deliverable that lands whether or not the control passes |
| s77 | r = 5 Rees / special-fibre completeness | **the Pieri-to-circuit bridge, then straightening** | the bridge is on neither final board and was on the earlier one; without it the two batch-11 breakthroughs do not compose |
| s78 | stable `M₆` frontier at `a_∞ = 4` | **r = 5 Rees / special-fibre completeness** | shifted down one, unchanged in content |
| s79 | first non-washout padded frontier at `ℓ = 6` | **`ℓ = 6` frontier *and* the `a_∞ = 4` test** | `a_∞ = 4` is five blocks, measured — it is an afternoon, not a night |

Three changes: one split, one restoration, one merge.  Each rests on a number
that was not available when the proposal was written.

---

## 1. What I accept without argument

Stated first and briefly, so the disagreements are legible as the small part.

- **Every cut of mine.**  C4 (re-price the census) and C5 (certification debt)
  out of the research slots and into pre-batch: correct.  C6 (broad minimality
  search) narrowed sharply: correct, and see §2.
- **The determinant stopping rule at rank 273**, and the block-swap semantics
  correction — that a brief must not write `ker(τ − I | W_δ)` as though the
  endomorphism existed.  Both are right and both are already carried in
  `PROJECT_NOTES.md`.
- **The pre-registered outcome table (§6).**  Better than anything I wrote.
  Adopt as is, with one row added in §5 below.
- **The no-fund list (§7)**, including the new final item.
- **The relay rules (§4)** and the no-gate architecture.
- **`s77` → r = 5 completeness computationally, paired with S2 in theory.**  Two
  slots on one theorem is right when it is the second-likeliest theorem to land.

## 2. The concession

§1.4 is correct and I withdraw the language it flags.  s69's circuit is fast on
the LMR family because its contraction network has a favourable pathwidth on
**two-tall-column shapes**; nothing establishes that an arbitrary partition
inherits either the representation or the cost.  My C4/C6 wording treated the
breakthrough as a general repricing and it is not one.  Any repricing outside
the demonstrated shape class must first exhibit the contraction representation
and a pathwidth bound for that class.  This is the second time a session or a
review has caught me specifying a comparison without checking that both sides
of it are actually defined; I am carrying it forward as a standing check.

## 3. Four pre-batch items this proposal asks for that are already done

The proposal reviewed `docs/batch12_plan.md`, which predates
`docs/batch12_integrator_note1.md`.  Against §3.1:

| §3.1 | state |
|---|---|
| 1. push and verify the integrated tree | **done** — `origin/main` = `c984e2c`, verified by `ls-remote` from both machines |
| 2. reconcile the s67 / s71 certifier implementations | **compared, line for line and empirically** — the two compute the same bound under `pos = (nc−1) − key`; 40 comparisons over five cells agreeing on *every individual order*. What remains is unifying the two `sparse_nullity` dialects |
| 3. record the missing stable tail; recount the weight-13 blocks | **done, and the recount changes the board** — see §4.3 |
| 3. mark `i_det(24) = 1` OPEN; correct the birth profile | **done** |
| 4. independently reproduce `B₂₄ = 2168` | **open**, and harder than it looks: `tools/verify/pleth.py` is a genuinely independent engine but its boxed weight-multiplicity array exceeds its own ceiling at `r = 9`, so it cannot serve at `δ = 23`. A second engine at the goal cell is session-sized |
| 5. weighted S5 DAG economics `C_total`, `C_peak` | **superseded by a sharper quantity** — see §4.1 |
| 6. freeze the outcome table | adopt §6 as written, plus the row in §5 |
| 7. census repricing as bookkeeping only | accepted |

---

## 4. The three differences

### 4.1 Split `s75`.  The control and the scale are different problems, and the number says so

The proposal merges my C2 into one session that recovers `dim M₁₂ = 2`, and
*then*, "if the two-part control passes", scales to `δ = 24`.  That is a gate
inside a session — the worst of the three placements, because a session that
spends its night on the first half produces nothing for the second and the batch
cannot tell in advance.  The earlier roadmap split them (C74 and C77) and was
right to.

What has changed since either document is that the size of the second half is
now known.  τ does not preserve `W_δ`, so the residual `τv − v` lives in the
invariants of `K' = H_{δ−2} × S₄ × S₄`, of dimension

    C_δ = Σ over two-step horizontal-4-strip paths λ → μ → ν of a_{δ−2}(ν)
        = Σ_{μ a one-strip predecessor of λ_δ} B_{δ−1}(μ).

Measured exactly: **`C₁₂ = 239`** (against `B₁₂ = 31`, `a₁₂ = 2`), 36 paths over
23 shapes.  The path structure **saturates at `δ = 14`** and is constant to 24:
12 predecessors, 160 paths, 42 distinct shapes, maximum multiplicity 10.  Two
independent one-level ratios — `C₁₂/B₁₂ = 7.71` and `B₂₄/a₂₄ = 7.91` — put
**`C₂₄ ≈ 1.7 × 10⁴`**.

So the two halves are:

- **the control** — an *operator-correctness* problem in a 239-dimensional
  recoupling space, where the question is whether `P_K τ P_K` has been built
  correctly and whether its output vectors evaluate;
- **the scale** — a *build-and-memoise* problem in a 2168-dimensional precursor
  with a ~1.7 × 10⁴-dimensional recoupling space and a saturated 42/160/10
  path structure that is identical at `δ = 14` and `δ = 24`.

Different failure modes, different instruments, one night each.

And the split costs nothing, because the scaling session has a deliverable that
does not depend on the control: **`C₂₄` exactly**.  Nobody has it; it is roughly
90 chunked evaluations of the same class that produced `B₂₄`; and it is the
honest cost model for the entire S5 route.  A scaling session whose control
turned out to have failed still returns that.

`C₁₂ = 239` is also a far sharper control than "recover `dim M₁₂ = 2`".  Two is
a small number and several wrong operators return it.  A correct `P_K τ P_K` at
`δ = 12` maps a 31-dimensional space through a 239-dimensional one; a session
whose implementation never forms a 239-dimensional object is either doing
something cleverer than I know or is wrong, and must say which.

### 4.2 Restore the Pieri-to-circuit bridge.  It is on neither final board, and it was on the earlier one

The earlier roadmap had it twice — C75 on the implementation side and T2 on the
theory side — and I called it the best idea in either document.  In the
reconciled proposal it is gone.  `s76` is now a circuit-side-only line of work
("structured fillings, tall-column overlap, ladder birth channels, pivoting and
straightening"), S1 is a circuit-side straightening rule, and S3 is the
block-swap operator.  **No session on either board now asks for the map between
the two coordinate systems.**

That leaves the batch with two deterministic constructions that do not compose.
The recursion route's real risk — the one I have flagged since the batch-11
review and which the proposal's own hard stopping rule for `s75` names — is not
that it returns the wrong dimension but that it returns vectors that cannot be
paired with determinant points.  The bridge is precisely the repair for that
failure, and it is also what would let s69's 0.13-second oracle evaluate a
deterministic basis instead of a sampled one.  Dropping it removes the batch's
answer to its own stated risk.

So my `s77` is the bridge first, straightening second, in that order and stated
as an order: an explicit map from S5 Pieri states to s69 bracket fillings,
controlled at `n = 3` (the six-dimensional source and the exact banked ideal
line) and at `n = 4, δ = 12` (the two-dimensional source), with the fallback the
proposal already specifies — a birth-channel-informed sampling distribution and
a measured expected cost for the last dimensions.

### 4.3 Merge `a_∞ = 4` into the length-6 session.  It is five blocks

The proposal gives the stable frontier a full session and asks that the
weight-13 nonzero-block total be recounted before publication.  Recounting it
answers the first question:

    57 partitions of 13 into at most 5 parts
    10 with a_∞ = 0   (not 11 — the record's 47 stands, the review's 46 was off by one)
    47 with a nonempty stable block

    a_∞ ≤ 3 :  11 blocks   all closed
    a_∞ = 4 :   5 blocks   ← the entire open frontier this session was to cover
    a_∞ ≥ 4 :  36 blocks

The review's substantive correction is confirmed and untouched: four `a_∞ = 1`
tails, not three, with `(5,3,3,2)` the one no session had tested.

**Five blocks on a validated instrument is an afternoon.**  The batch-10 stable
pullback ran `(5,3,3,2)` in 26.5 seconds; the `a_∞ = 4` shapes are larger but
they are five.  A whole night on it buys nothing the second half of a night does
not, and the freed slot pays for §4.1.

So `s79` runs the five-block test **first** — bounded work, a certain result,
and the stronger theorem banked either way — and then spends the rest of the
night on the `ℓ = 6` padded frontier, which is open-ended.  Bounded before
unbounded, so the session cannot return empty.

The one risk I am taking on, stated plainly: these are two instruments, not one,
and a session that switches instruments mid-night does each less well than a
dedicated session would.  I accept that for the stable half because its scope is
now known exactly and small.  If the `a_∞ = 4` raw spaces turn out an order of
magnitude larger than the `a_∞ = 1` ones, the right response is to give it back
its own slot in batch 13, not to let it eat the `ℓ = 6` night.

---

## 5. Two additions to the pre-registered material

**A row for the outcome table.**  §6's last row — *partial source only → only
rank lower bounds → do not infer nullity from sampling failure* — is right in
general and too weak in one case:

| observed | consequence | action |
|---|---|---|
| span < 274 but `rank T_det = 273` on the span reached | `i_det ≤ 1`, and with LMR's `i_det ≥ 1`, **`i_det = 1` exactly** | the determinant column is finished. Only the padded column is short; report it as a completed half, not a stall |

This is the rank-273 rule applied to a partial span, and it matters because the
birth profile says the direction a partial span is most likely to be missing is
the last-born one at `δ = 24` — the last coupon, the most expensive in the run,
and precisely the one the determinant side is allowed to skip.  The padded side
is not allowed to skip it, which is why the whole residual difficulty of the LMR
decision sits on that single vector, and why S4's padded-injectivity work
should start by describing it rather than by summing blockwise rank bounds.

**A constraint on prime choice.**  Neither board states it and it is invisible
until it breaks something.  The projected operator `P_K τ P_K` and the argument
that its `+1` space is the full invariant source both run through averaging and
semisimplicity.  That transfers to characteristic `p` here — `λ₂₄ ⊢ 96`, both
house primes exceed 96, so `F_p[S_96]` is semisimple by Maschke and every
characteristic-zero statement about `S^λ`, its invariants and the projectors
holds verbatim mod `p`.  It also licenses what the programme does everywhere:
sizing mod-`p` computations with `a_δ`, `B_δ`, `C_δ` and the DAG counts, all
computed by characteristic-zero plethysm.  It is legitimate exactly when
`p > |λ|`.

    Pre-register: no prime below 97 anywhere in the S5 route, at any δ,
    however tempting for speed at the δ = 12 control (where |λ₁₂| = 48).

---

## 6. The six, and the priority

| | mission |
|---|---|
| **s74 — sampling to the LMR decision** | As written in §3.2. Resume s69's checkpointed ladder; sample only the new birth directions per rung; evaluate every accepted vector on the same generic / determinant / reducible / padded / `per₄` families. Stop determinant work at rank 273, padded at 274. On a stall, the rank curve, the missing birth directions, and the completed-half rule of §5. |
| **s75 — the `δ = 12` compact control** | Build the 31-dimensional precursor; construct `P_K τ P_K` (not raw `τ`); recover `dim M₁₂ = 2` **and evaluate the two vectors** against determinant points, reproducing `i_det(12) = 0`. Pre-registered: the operator passes through a **239-dimensional** space, and an implementation that never forms one must say why. No prime below 97. |
| **s76 — scale the recursion to `δ = 24`** | The `B₂₄ = 2168` precursor and the saturated 42/160/10 recoupling; recover a deterministic 274-dimensional source; carry the same decision table. **Deliverable either way: `C₂₄` exactly.** Hard stopping rule as written — if exact recoupling or evaluation needs ambient carrier expansion, name the obstruction and stop. |
| **s77 — the bridge, then straightening** | An explicit map from S5 Pieri states to s69 bracket fillings, controlled at `n = 3` and at `n = 4, δ = 12`; then straightening / structured fillings / tall-column overlap against the coupon-collector residue. Fallback as written. |
| **s78 — r = 5 Rees / special-fibre completeness** | Exactly §3.2's s77: certify that every exceptional component lies over the supports S3/s72 enumerated, quantified over `Proj gr_J R`. With `31 < 35` this gives `R₅ ⊄ D₅`. Fallback: the exact unclassified associated prime, not another arc table. |
| **s79 — the two independent frontiers** | The five `a_∞ = 4` weight-13 blocks in raw-space cost order, stopping at the first nonzero stable ideal — bounded, first. Then the `ℓ = 6` padded frontier: `i_det ≥ 1` or `mult_pad < mult_red` in the cheapest tractable cells, **without extrapolating s69's cost model** to a shape class whose contraction representation and pathwidth have not been exhibited. |

**Priority**, expected value per unit effort, Claude side only:

    s75 ≈ s74  >  s77  >  s76  >  s78  >  s79

`s75` and `s74` first for the reasons the proposal gives.  `s77` above `s76`
because the bridge can remove the sampling tail entirely — it is the only
session that can make two others cheap — whereas `s76` has a guaranteed
deliverable and can therefore afford to be later.

Interleaved with the theory board, and taking §5's ranking as given for S1–S6:

    s75 ≈ s74  >  S3  >  S1 ≈ s77  >  s76  >  S4  >  s78  >  S2  >  s79  >  S5  >  S6

`S1` and `s77` are paired because they are the same question from the two sides,
and if either lands the other should stop and consume it.
