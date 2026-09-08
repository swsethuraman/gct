# Thoughts on the batch-11 stock-take and the batch-12 roadmap

Integrator note, written after reading both documents against my own board
(`docs/batch12_plan.md`) and after computing one number that neither board has.

---

## 0. Verdict

The stock-take is accurate and its one correction of me is right.  The roadmap
is better than mine on the mathematics and worse on the process, and the split
is clean enough that a merged board is easy to state.  Three things:

1. **One correction lands on me and it is a good one.**  `i_det(24) = 1` is not
   banked.  Following it through gives a real economy that neither of us had
   drawn out — and it puts the whole remaining difficulty of the padded side
   onto a single vector.
2. **The `τ` correction is right, and the characteristic-`p` question it raises
   has a one-line answer nobody has written down.**  It is favourable.  It
   should be banked as a lemma anyway, because it licenses a great deal that
   the programme has been doing without justification, and because it names a
   constraint on prime choice that would otherwise be easy to violate.
3. **There is a number the roadmap needs and does not have.**  The size of the
   linear algebra the block swap actually does is not `B_δ`.  I computed it:
   `C₁₂ = 239` exactly, and `C₂₄ ≈ 1.7 × 10⁴`.  This turns C74's binary
   stopping rule into a measurement, and the answer is that the route is
   operational.

---

## 1. The `i_det(24)` correction, and what falls out of it

The stock-take is right.  What LMR gives is `i_det(24) ≥ 1`, equivalently
`mult_det ≤ 273`.  Equality is not banked, and my batch-11 C3 line —
"`rank S < 274` implies `i_pad ≥ 1`, which with `i_det = 1` gives `D ≤ 0`" —
leans on the equality.  That line is wrong as written and I am carrying the
correction forward.

The consequence the stock-take draws is the valuable part, and it is worth
stating precisely because it is easy to state slightly wrong:

> If a session exhibits a **273-dimensional subspace** of the source on which
> the determinant evaluation has rank 273, then `rank T_det ≥ 273`, so
> `i_det ≤ 274 − 273 = 1`; with LMR's `i_det ≥ 1` this gives `i_det = 1`
> exactly.  The determinant side never needs the 274th basis vector.

Now put that against s69's birth profile.  The new directions per rung from
`δ = 12` to `24` are

    2, 37, 54, 52, 43, 31, 22, 14, 9, 5, 3, 1, 1

and the sampling tail is a coupon-collector tail precisely because random
circuit fillings over-sample early-born directions.  The single vector the
determinant side may skip is the last-born one at `δ = 24` — the last coupon,
the most expensive one in the entire run.

The padded side has no such luxury.  `i_pad = 0` means `rank T_pad = 274`, and
that needs every direction including the last-born.  So:

**The asymmetry is real, and the whole residual difficulty of the LMR decision
now sits on one explicitly identifiable vector** — the direction born at the
top rung of the ladder.  A session that produces *that vector alone*, by
straightening rather than by sampling, finishes the padded side modulo a rank
computation on a space that already exists.

This changes what T3 ("prove `i_pad = 0` structurally") should try first.  Not
a blockwise rank bound summing to 274 — a description of the last-born
direction.  It also gives C76/s74 a much better stopping rule than "the span
stalls": if the span reaches 273 and stalls, the determinant column is
*finished*, and only the padded column is short.  That is a good night's work,
not a stall, and the brief should say so.

---

## 2. The `τ` correction, and the characteristic-`p` line nobody wrote

The roadmap's T1 is right that the raw adjacent block transposition does not
preserve `W_δ = (S^{λ_δ})^{K_δ}`: `τ v` is invariant under `τ K_δ τ^{-1}`, not
under `K_δ`.  The proposed repair, the projected operator `P_K τ P_K`, is the
standard one, and the standard argument that its `+1` eigenspace is exactly
`(S^{λ_δ})^{H_δ}` runs through averaging and semisimplicity.

I flagged this as a possible silent failure, because the programme computes
mod `p` and the usual argument is written for characteristic zero.  It is not
a failure.  The reason is one line and it is worth banking:

> `|λ_δ| = 4δ`, so `λ₂₄ ⊢ 96`.  Both house primes — `2147483647` and
> `2147483629` — exceed 96, so `F_p[S_96]` is semisimple by Maschke, and every
> characteristic-zero statement about `S^λ`, its `H_δ`- and `K_δ`-invariants,
> and the projectors onto them holds verbatim mod `p`.

Two reasons to write it down rather than leave it implicit.

First, it retroactively licenses something the programme does constantly and
has never justified: `a_δ`, `B_δ`, `C_δ` and the DAG counts are all computed by
characteristic-zero plethysm and Weyl alternation, and then used to size and
check computations carried out mod `p`.  That is legitimate exactly when
`p > |λ|`, and only then.

Second, it names a constraint that is otherwise invisible and tempting to
violate.  `|H_δ|` and `|S_96|` have all their prime factors below 97; a session
looking to make the recursion faster might reach for a 16-bit or 32-bit prime
below 97 for the small controls at `δ = 12` (`|λ₁₂| = 48`).  Below `p = 97`
the projector may not exist and the eigenspace argument fails.  **Pre-register:
no prime below 97, at any `δ`, anywhere in the S5 route.**

---

## 3. The number the roadmap needs: `C_δ`

### 3.1 What it is

`τ` does not preserve `W_δ`, so the equation `τ v = v` cannot be written inside
the 2168-dimensional precursor.  Both `v` and `τ v` are invariant under

    K' = K_δ ∩ τ K_δ τ^{-1} = H_{δ−2} × S₄ × S₄

and that is where the residual `τ v − v` lives.  Writing `C_δ = dim
(S^{λ_δ})^{K'}`, one-block Pieri gives

    C_δ  =  Σ over two-step horizontal-4-strip paths λ → μ → ν  of  a_{δ−2}(ν)
         =  Σ_{μ a one-strip predecessor of λ_δ}  B_{δ−1}(μ),

i.e. exactly one more level of the same recursion that produced `B_δ`.

**`C_δ`, not `B_δ`, is the dimension of the space the block swap works in.**
`B_δ` is the size of the answer; `C_δ` is the size of the equation.

### 3.2 The numbers

Path structure — computed exactly (`analysis/wk11_int_cdelta.py`):

| `δ` | one-strip preds | two-strip paths | distinct shapes `ν` | max `c_ν` |
|---|---|---|---|---|
| 12 | 3 | 36 | 23 | 3 |
| 13 | 12 | 136 | 35 | 10 |
| ≥ 14 | 12 | **160** | **42** | **10** |

The structure saturates at `δ = 14` and is then constant to `δ = 24`.  So the
recoupling at the top of the ladder is combinatorially identical to the
recoupling at `δ = 14` — only the multiplicities `a_{δ−2}(ν)` grow.

The exact value at the control cell (`results/wk11_int_c12.json`):

    C₁₂ = 239        against  B₁₂ = 31,  a₁₂ = 2
    21 of 23 shapes nonzero;  largest single channel 18  (7.5% of the total)

Note how flat that is.  `B₂₄`'s twelve channels are dominated by one of 273 out
of 2168 (12.6%); `C₁₂`'s channels are flatter still.  There is no channel to
concentrate on — the recoupling cost is spread.

For `δ = 24` I have not run the exact evaluation (42 shapes at `δ − 2 = 22`, of
the same cost class as the `B₂₄` run, so roughly 90 chunked evaluations).  Two
independent calibrations agree:

    C₁₂ / B₁₂ = 7.71        (exact, measured here)
    B₂₄ / a₂₄ = 7.91        (exact, banked)

Both are "one more level of the same recursion" ratios.  So

    C₂₄ ≈ 8 × 2168 ≈ 1.7 × 10⁴        (estimate, not a measurement)

### 3.3 What this does to C74

The roadmap's C74 has a binary stopping rule: stop if the block swap
"intrinsically requires expansion into the 5.1-million-coordinate carrier".
But the quantity is not binary — it is a number between `B₂₄ = 2168` and
`n_χ = 5.1 × 10⁶`, and it is now known to about a factor of two.  `1.7 × 10⁴`
is 8× the precursor and 300× below the carrier.  **The route is operational.**
C74 should be told to measure `C₂₄`, not to test whether it is finite.

More usefully, `C₁₂ = 239` is a far sharper implementation control than the
one C74 currently carries.  "Recover `dim M₁₂ = 2`" can be hit by accident —
2 is a small number and several wrong operators return it.  But a correct
`P_K τ P_K` at `δ = 12` maps a 31-dimensional space through a 239-dimensional
one.  A session whose implementation never forms a 239-dimensional object is
either doing something cleverer than I know, or wrong, and it must say which.

So: pre-register `C₁₂ = 239`, the 42/160/10 saturated structure, and the
`C₂₄ ≈ 1.7 × 10⁴` estimate.  Require `C₂₄` exactly as a deliverable of the
scaling session, since it is the honest cost model for the whole route and
nobody has it.

---

## 4. Where the roadmap is better than mine

Said plainly, because I want these adopted.

- **C75 / T2, the Pieri-to-circuit bridge.**  The best idea in either document.
  My S1 asked for a straightening basis on the S5 side and stopped there; the
  roadmap's version asks for the map that makes that basis *evaluable through
  the s69 oracle*.  That is the difference between a deterministic basis and a
  deterministic basis you can use.  It connects the two things batch 11 actually
  produced instead of proposing a third.  Highest expected value on the merged
  board.

- **T3, proving `i_pad = 0` structurally.**  I have nothing like it.  It goes
  at the padded side, which §1 above shows is the side that genuinely needs
  everything.  Keep it, and point it at the last-born direction first.

- **The four-outcome LMR decision table (§6), pre-registered.**  Better than my
  "three results that would change the batch".  Fixing the interpretation of
  every possible rank pair before the computation is the discipline this
  programme runs on and I should have written it.  Adopt as is.

- **The "do not fund" list (§7).**  Sharper than anything on my board, and the
  closing rule — *any exotic idea must produce an operator, recurrence, rank
  implication, or complexity reduction* — is the right test.  Adopt as is.
  (I would apply it to the roadmap's own T5, below.)

- **Independent `B₂₄` re-derivation (§0.3).**  Correct and I missed it.  `2168`
  now sizes the whole route and has exactly one implementation behind it — mine.
  It needs a second engine before anything is built on it.

- **Splitting the `δ = 12` control off as its own session (C74).**  I had it as
  the first half of the scaling session.  Making it standalone and must-pass is
  right: it is where the route lives or dies, and it should not share a night
  with the thing that depends on it.

- **Consolidation in pre-batch rather than a session.**  Correct, and mostly
  done — see §6.

---

## 5. Where my board holds

- **The push is a hard blocker and the roadmap does not treat it as one.**
  §0.1 says "integrate the tree, record one immutable base commit".  The tree
  *is* integrated — here, in my clone, at `2a9da4b`.  What has not happened is
  `origin/main` moving; it is still at `226b4ef1`, **65 commits behind**.
  Batch 11 paid for this three times: s73 rebuilt the verifier extension from
  scratch, s71 re-implemented s67's certifier from a report without ever seeing
  the code, s72 ran without the plan.  Batch 12 is larger and depends more on
  banked artefacts.

  The test is not "did the integrator merge" but:

      git ls-remote origin refs/heads/main

  returning the commit that contains `docs/batch12_plan.md`.  Until it does,
  no brief goes out.  This is the single highest-value item in either document
  and it costs nothing.

- **A plan for `D(24) ≤ 0`.**  The roadmap's §8 gives the best outcome and the
  second-best and stops.  `D ≤ 0` is a live possibility and the programme
  should not meet it unprepared, with no successor cell priced and no laboratory
  other than LMR.  My S5 exists for exactly this and it should be written before
  the answer, not after.

- **A second cell.**  The roadmap has nothing outside LMR and `r = 5`.  Its
  "do not fund" list retires more length-5 census, which I agree with — but
  `ℓ = 6` is not length-5 census.  The washout theorem says nothing at length
  ≤ 5 bears on the permanent, so `ℓ = 6` is the *first* length that can, and it
  was priced out until batch 11 changed the source-side cost by four to six
  orders of magnitude.  Related: S1 closed literature retrieval and named a
  direct finite minimality search as the only sensible follow-up — is LMR's the
  only determinant equation at `ℓ = 9`?  If the answer is no, the programme
  gets a cheaper laboratory; if yes, that is a characterised negative over a
  priced region, which is a full result.

- **Re-pricing the census.**  Not on the roadmap at all.  The queue that ranked
  batches 9 through 11 was priced under a cost model that is now wrong by
  orders of magnitude on both the source side (the circuit) and the rank side
  (the hybrid, bounded by `N_S · δ` rather than `n_χ²`).  Anything selected
  from that queue is selected wrongly.  One session, and it sets up batch 13.

- **Zero gates.**  The roadmap gates C77 on C74 or C75.  I would not.  With
  `C₁₂ = 239` banked and `C₂₄ ≈ 1.7 × 10⁴` sized, the scaling session has a
  target it can build against independently, and its fallback — the *exact*
  `C₂₄`, which nobody has — is a full deliverable on its own.  Batch 11 ran
  with one partial gate and batch 12 can run with none; that is a consequence
  of the wall falling, not a relaxation of the rule.

---

## 6. Housekeeping: what is actually done

Against the roadmap's §0, so nothing is assumed:

| §0 item | state |
|---|---|
| merge s68–s73 bundles | **done** (`2a9da4b`; six branches) |
| reconcile the verifier family-name difference | **done** — s73's appended `permanent_pencil` adopted; my inserted `permanent` was a latent defect (it shifted fresh-point seed offsets) and s73 caught it |
| verifier extensions in the base commit | **done** — 1,082 certificates, six kinds, all schema-valid, self-test passing |
| plan, stock-take, P0-A artefacts in the base commit | **done** |
| reconcile the duplicated s67 / s71 certifier code | **not done** — two `sparse_nullity` dialects are *accepted*, not *unified*; the two certifier implementations have never been compared line for line; `split_rank` and `hybrid_kernel` report RECORDED, not re-derived |
| mark `i_det(24) = 1` OPEN pending rank 273 | **doing now** (§1) |
| birth-profile first entry `a₁₂ = 2` | **done in batch 11** (`docs/lmr_cell.md` §6; old sequence summed to 283 against `a₂₄ = 274`) |
| stable missing tail `(5,3,3,2)` | to record |
| weight-13 nonzero-block total flagged for recount | to record |
| independent `B₂₄` re-derivation | **not done** — needs a second engine |
| weighted DAG economics | **superseded** — `C_δ` (§3) is the sharper form of the same question, and `C₁₂` is exact |
| freeze the three-outcome table | adopt the roadmap's four-outcome §6 as is |
| **push `origin/main`** | **not done, and it blocks the batch** |

The certifier debt is the one item I would not leave in pre-batch — but the
reason two sessions rebuilt banked machinery was the unpushed tree, not the
debt.  Fix the cause, and the debt is an afternoon of mine rather than a
session of someone's.

---

## 7. The merged board

Twelve sessions, no gates.

### Claude — s74 to s79

| | mission | provenance |
|---|---|---|
| **s74 — resume s69 and decide LMR** | Resume the checkpointed run; do not restart.  Climb the ladder sampling only the `a_δ − a_{δ−1}` new directions per rung.  Evaluate at four families on the same vectors — `det₄` pencils, reducible `ℓ·c`, padded `ℓ·per₃`, unpadded `per₄` — then `i_det`, `i_pad`, `U_D ∩ U_P`, `D`. **New stopping rule (§1): a span of 273 with determinant rank 273 finishes the determinant column outright.** | mine C1 = roadmap C76 |
| **s75 — the `δ = 12` golden control** | The compact one-block recursion at `λ₁₂`.  Recover `dim M₁₂ = 2` **and evaluate the two vectors against determinant points**, reproducing `i_det(12) = 0`.  **Pre-registered: `C₁₂ = 239`** — the operator passes through a 239-dimensional space, and an implementation that never forms one must say why.  No prime below 97. | roadmap C74, sharpened |
| **s76 — the Pieri-to-circuit bridge** | An explicit map from S5 Pieri states to s69 bracket fillings, controlled at `n = 3` and at `n = 4, δ = 12`.  Fallback: a birth-channel-informed sampling distribution and the expected reduction in the coupon-collector tail. | roadmap C75 (= my S1, improved) |
| **s77 — scale the recursion to `B₂₄ = 2168`** | Build `M_λ` as `ker(τ − 1)` on the 2168-dimensional precursor via `P_K τ P_K`.  **Deliverable either way: `C₂₄` exactly.**  Same four columns as s74. | mine C2 = roadmap C77, ungated |
| **s78 — `r = 5` Rees / special-fibre completeness** | Close the enumeration gap under s72's `dim(D₅ ∩ W) = 31 < 35`, quantified over `Proj gr_J R`. | roadmap C78 |
| **s79 — the `ℓ = 6` frontier, minimality, and the re-price** | First `ℓ = 6` cell with `i_det ≥ 1` or `mult_pad < mult_red`; is LMR's the only equation at `ℓ = 9`; and a census re-priced under the circuit and hybrid cost models, with a ranked queue for batch 13. | mine C3 + C6 + C4 |

### Sol / theory — T1 to T6

| | mission | provenance |
|---|---|---|
| **T1 — the compact block-swap operator** | Exact matrix elements for `P_K τ P_K` in predecessor coordinates, with a complexity bound.  Inputs it now has: `C₁₂ = 239`, the saturated 42/160/10 structure, and the semisimplicity lemma of §2. | roadmap T1 |
| **T2 — Pieri basis vs bracket basis** | The theory half of s76: constructive at `n = 3`, then `n = 4, δ = 12`, then the inductive rule, and the tall-column `k`-vanishing in representation-theoretic language. | roadmap T2 |
| **T3 — `i_pad = 0` structurally** | **Start with the last-born direction at `δ = 24`** (§1), not a blockwise rank bound.  The padded side's entire residual difficulty is one vector. | roadmap T3, redirected |
| **T4 — the `r = 5` completeness theorem** | The statement that `Proj gr_J R` has no component outside s72's list. | mine S2 = roadmap T4 |
| **T5 — the successor, written before the answer** | Rank and price what follows LMR, in both directions: if `D ≤ 0`, which cell next (`n = 5` at `δ = 40`, `λ = (151,31,2⁹)`, now priceable with the circuit; other `ℓ = 9` tails; the stable route; a padded model other than `ℓ·per₃`).  If `D > 0`, how a finite cell becomes a growing-`n` family. | mine S5 + roadmap T6 |
| **T6 — adversarial audit and the batch-13 board** | Read code and docs, ignoring session conclusions until the implementation is checked.  Batch 11's version found four things, one of them a latent defect of mine. | mine S6 |

**One contention I am not resolving unilaterally.**  The stable `a_∞ = 4`
frontier at weight 13 (my S4, the roadmap's C79) and the adversarial audit
compete for the last theory slot.  My call is the audit — the stable frontier
is not on the critical path to either of §8's two theorems and can wait one
batch, whereas the audit has a measured return.  If you want both, the
candidate to cut is the roadmap's T5 (Ramanujan / transfer-matrix), by the
roadmap's own §7 test: it does not yet name an operator, recurrence, rank
implication or complexity reduction on any stated path.

### Priority

Expected value per unit effort, not execution order:

    s76 ≈ T2  >  s74  >  s75  >  T1  >  T3  >  s77  >  s78 ≈ T4  >  s79  >  T5  >  T6

`s76`/`T2` first because they are the only pair that can make the sampling tail
— now the programme's entire remaining cost — go away.  `s74` next because it
may settle LMR with machinery that already works, and §1 has just made its
stopping rule much better.

---

## 8. What I am doing next, in order

1. **Push.**  Nothing below happens first.
2. Bank `C₁₂ = 239`, `analysis/wk11_int_cdelta.py`, and the §2 lemma.
3. Record the `i_det(24)` correction in `PROJECT_NOTES.md` and correct the
   batch-11 C3 line in the stock-take.
4. Clear the certifier debt: unify the two `sparse_nullity` dialects, compare
   s67's and s71's certifiers line for line, decide whether `split_rank` and
   `hybrid_kernel` can be made re-derivable.
5. Write the twelve briefs against the merged board, with the four-outcome
   decision table and the "do not fund" list attached to all of them.
