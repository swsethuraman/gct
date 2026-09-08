# Batch 11, Claude side — review of sessions 68, 69, 70, 72, 73

Five of six delivered; **session 71 (C4, the `r = 5` closure falsifier) has not
arrived** and this review is written without it.  All five bundles verify
against their `.md5` and apply cleanly onto `226b4ef1`.  Labels: **confirmed**
(reproduced here), **corrected**, **relayed** (not checkable here), **new**
(found here).

---

## 0. Verdict

> **Sessions 68 and 69 contradict each other about the same object, and both are
> right.**  s68 measured the ladder seed `M₁₂` at `(17,17,2⁷)` and found it
> walled twice over — 2.47 TB to build, 90–310 years per prime to solve.  s69
> *produced* it: generic rank 2 at both primes, determinant rank 2, `i_det = 0`.
> The difference is entirely the representation.  **The wall the programme has
> been measuring since batch 9 is a property of the coordinates, not of the
> object**, and the batch's redundancy design is what made that visible in one
> night rather than three.
>
> **s69 also passed the exact control.**  Its bracket circuit reproduces the
> banked `n = 3` ideal vector entry for entry — 0 mismatches across all 17 047
> coordinates, equal up to sign over `Z` — and evaluates a highest-weight vector
> at the LMR cell in **0.13 s**, against 14.4 TB and 415 days for one vector in
> coordinates.  Its honest residue is *basis enumeration*, not evaluation.
>
> **s73 turned the `D = +1` into a theorem.**  The `n = 3` `a`-ladder is flat
> from `δ = 12` (verified here independently at `δ = 12…18, 20`), so Lemma L
> forces `i_det = 1` and `i_per = 0` at **every** rung: `D(δ) = +1` for all
> `δ ≥ 12`.  It measured five rungs anyway and they agree with the theorem at
> every point.  46 certificates, 46 PASS.
>
> **s72 delivered the other half of the `r = 5` bound.**  `dim(D₅ ∩ W) = 31 < 35`
> on the enumerated normal cone, with all four of session 66's named residues
> closed to numbers — including `P ∩ c21` at order 2 = 19, the one number s66
> left open and the brief flagged as residue 1.
>
> **s70 did the ungated fallback exactly as briefed** and wrote down `S` for the
> first time, with a two-sided calibration.  Its Part A determination is sound.
> One of its two premises has since been overtaken — see §5.

---

## 1. The process failure that framed the batch

**Every session cloned `226b4ef1`.**  s73 records it in its second paragraph:
the batch-11 plan, the worker preamble, `docs/s65_prompt.md`,
`docs/stocktake_batch10.md`, `analysis/wk11_int_p0a.py`, the P0-A certificates
and the `n ∈ {3,4}` verifier "exist neither at `226b4ef1`, nor in any branch of
the public repository, nor in the integrator tree on the laptop".  s72 says the
same of the preamble and §6 of the plan.

So the push never landed, exactly as I flagged when the sessions were fired.
The consequences are visible and were paid for:

- **s73 rebuilt the verifier extension from scratch** — `n ∈ {3,4}`, an
  `n × n` `det_pencil`, and a permanent point family — because the one I had
  already written and banked was not in its tree.  It flags the collision
  itself: it named the family `permanent_pencil` where mine is `permanent`.
  **That is a one-word rename in its 46 certificates and nothing else**, and it
  is the whole cost of the duplication, which is a good outcome for a bad
  cause.
- s73 also could not read the P0-A result and so **re-derived `i_per(12) = 0`
  independently**, on fresh evaluation families with seeds chosen to be disjoint
  from the banked ones.  That converts an accident into the strongest possible
  confirmation: two integrator runs and one worker session, three independent
  evaluation families, all giving `mult_per = 6`.
- The briefs themselves reached the sessions (they were pasted), which is why
  the work is on target despite the tree being a batch behind.

**For the record:** the rule that failed here is batch 11's own process rule 2,
and the preamble's "stop if the plan is not in your clone" check did not fire
because the sessions had the brief text and could reconstruct what they needed.
That is the check working badly — it should key on the tree, not on whether the
worker feels blocked.

---

## 2. Confirmed here

**s68's seed sizing, exactly.**  `N_S(λ₁₂, 12) = 51 446 325 457` — digit for
digit the value my own unbounded-knapsack count produced independently
(`analysis/wk11_int_ladder_size.py`); `|Stab| = 2!·7! = 10 080`;
`n_χ ≈ 5.10×10⁶`.  Two different methods, same integer.

**s69's whole `n = 4` ladder size table.**  Its seven `N_S` values at
`δ = 12, 14, 18, 21, 22, 23, 24` agree with my independent count at every digit
(`51,446,325,457`; `106,429,467,326`; `151,601,110,197`; `156,124,593,451`;
`156,346,649,229`; `156,419,279,221`; `156,438,903,314`).  Two independent
enumerations of a `1.5×10¹¹`-element set agreeing exactly is about as good as
cross-validation gets.

**s70's three ranks against banked truth.**  `rank S = 6, 1, 5` at
`(10,6,4,2,2)₆`, `(8,4,4,4,4)₆`, `(12,9,9,1,1)₈` — and session 60's table gives
`mult_red = 6, 1, 5` at those cells.  Both calibration cells are strictly below
`a` (`1 < 2`, `5 < 7`), which is the LMR regime, and the control returns
`rank S = a`, so the instrument is two-sided.  A construction returning `a` at
either bite would have been wrong.

**s73's `n = 3` `a`-ladder, the premise of its theorem.**  Recomputed here with
the house Kostant alternation:

    δ :  8   9  10  11  12  13  14  15  16  17  18  20
    a :  0   2   4   5   6   6   6   6   6   6   6   6

Flat from `δ = 12`, and flat through the stable threshold `t = 17`, so
Proposition S closes the tail.  s73's `D(δ) = +1` for all `δ ≥ 12` follows from
this plus Lemma L, and the premise is now checked on two engines plus mine.

---

## 3. Corrected

**`docs/lmr_cell.md` §6 has carried a wrong birth profile since it was
written, and session 69 quoted it back.**  It read

    11, 37, 54, 52, 43, 31, 22, 14, 9, 5, 3, 1, 1

The first entry is `a₁₂`, and `a₁₂ = 2` — banked in `results/s63_aladder.json`
and recomputed independently here.  The old sequence sums to **283**; `a₂₄ = 274`.
The corrected one sums to 274 exactly.  Fixed in place with a note.

Only the first entry changes, so nothing that used the tail is affected —
s69's concentration diagnosis (which turns on the thin `…5, 3, 1, 1` end) and
the plan's §2.3 both stand unaltered.  But three sessions have now read that
line, and this is the fourth inherited-number error the programme has found in
two batches.

**A near-miss worth naming so nobody trips on it.**  s73's third route to its
`a`-ladder is the `n = 3` stable value `a_∞((7,2⁵)) = 6`, the multiplicity in
`Sym(Sym² ⊕ Sym³)(C⁶)` — **two** summands.  The programme's banked `a_inf`
routine (`analysis/wk9_s57_stable.py`) computes the `n = 4` quantity, over
`Sym² ⊕ Sym³ ⊕ Sym⁴`, and returns **12** for the same tail.  Both are right;
they are different objects.  Anyone comparing them will think one session is
wrong.

---

## 4. The seed — the batch's central finding

| | s68 (coordinates) | s69 (circuit) |
|---|---|---|
| the object | `M₁₂` at `(17,17,2⁷)`, `a = 2` | the same |
| build | monomial array **2.47 TB**, peak 8.18 TB | no coordinates built |
| matrix | `nnz ≈ 0.5–1.8×10¹¹`, 0.6–2.2 TB | — |
| solve | **90–310 years per prime** | sampled fillings, generic rank 2 both primes |
| result | **walled, twice, each by ≥ 100×** | `mult_det = 2`, **`i_det = 0`**, both primes |

Both are correct and they are not in tension: s68 measured the cost of the
*coordinate realisation* and s69 never formed one.  The brief anticipated this
pair exactly — "if one side produces it and the other does not, say so plainly;
that is the batch's best possible outcome for this pair" — and s69 says so.

**So the record must not carry "the seed is unreachable".**  What s68 proved is
that the seed is unreachable *in coordinates*, and that streaming orbit
representatives (session 63's named opening) does not change that, because the
reduced matrix already has `nnz ≈ N_S`.  Both are real results and the second is
new.  What is now false is the inference the programme has been drawing from
them since batch 9.

s69's `i_det(12) = 0` is also the first measurement ever made on the `n = 4` LMR
ladder, and it is consistent with everything: Lemma L makes `i_det`
non-decreasing and `i_det(24) = 1`, so a zero at the bottom is exactly what a
correct instrument returns.

---

## 5. Where the sessions did not see each other — and what composes

**s70's gating premise is half overtaken.**  Its Part A has two parts: *(a)* the
`S`-construction provably needs the quartic source, since the columns of `S` are
a basis of `M⁴_λ` and that space has no basis which is not explicit
highest-weight vectors; *(b)* that source is walled, so `rank S` at LMR cannot
be run.  Part (a) is proved and stands.  **Part (b) was true of the coordinate
source and is what s69 changed.**

And the two compose more directly than either could see:

- `mult_red = rank S`, and `rank S` is the rank of the `a` source vectors in the
  normalisation `D_δ`.  Equivalently — and this is the cheaper reading —
  `mult_red` is the rank of the source evaluated at random **reducible** points
  `ℓ·c`.  Those are ordinary points of `Sym⁴C⁹`.
- s69's circuit evaluates a highest-weight vector at *any* point in ~0.13 s.
- Therefore `mult_red`, `mult_det`, `mult_pad` and `i_{per₄}` at LMR are all
  rank computations on the **same** `274 × K` evaluation matrix, and every one
  of them is cheap **once 274 spanning fillings exist**.

That last clause is s69's own stated residue: basis enumeration, which it prices
at **12–15 CPU-hours in a 2-core container** with the ladder climb implemented
and validated at `n = 3`.  So the honest bottom line of the batch is not "LMR is
walled" but:

> **every LMR number the programme wants is one 12–15 CPU-hour basis enumeration
> away, on hardware already in use.**

I have not verified this composition — it is a proposal, and the thing to check
first is whether `μ*` pushes through a bracket monomial cheaply (it should: with
`f = ℓ·c` the polarisation gives `f̃ = (1/n)Σᵢ ℓ(vᵢ)·c̃(…v̂ᵢ…)`, so `μ*` turns
each `f̃` node into a sum of `n` nodes with one leg split off, and the result is
again a contraction network).  If that holds, the evaluation route does not even
need `μ*`.

**s73 adds the structural remark that makes this decisive rather than
incremental.**  By the same flat-ladder argument it proved at `n = 3`, and s57's
measurement that the LMR cell is the first stable cell of its ladder at `n = 4`,
**once `D(24)` is known it is known at every `δ ≥ 24`.**  The `n = 4` question is
one cell, not a ladder.

---

## 6. Session by session

**s68 (C1) — the seed wall, and the algorithm validated.**  Did exactly what the
brief separated: reported Part A as a *seed* failure and not a failure of the
ladder algorithm, then validated the algorithm elsewhere.  The three-part rung
certificate holds at both primes on two reachable `n = 4` ladders, with a
genuine chained climb that carries the assembled predecessor forward rather than
a recomputed oracle.  Its Part C is a clean negative that kills one of my own
plan assumptions: **the highest-weight space is dense** (support 0.91–1.00, not
the 0.20–0.26 the plan projected from `δ = 4`), and the u-free part carries
births only as a *quotient* — `ker(E|_{u-free}) = 0` at every rung — so column
restriction yields no saving and the deflation needs the full carrier. The exact
sequence `0 → J(M_{δ−1}) → M_δ → π(M_δ) → 0` is the right statement and is new.
It also folded in an adversarial audit that caught its own over-claims.

**s69 (C2) — the batch's result.**  Exact control passed; LMR evaluation at
0.13 s; the `k`-vanishing regularity recorded so a successor does not rediscover
it; the ladder climb implemented and validated at `n = 3`.  Its limitation is
stated precisely and it is the right one.  One correction propagated (§3).

**s70 (C3) — the fallback, done properly.**  `S` written down for the first
time, `rank S = mult_red` proved by Schur, calibrated two-sided against banked
truth, four-way cross-checked, and reproduced by an adversarial from-scratch
reimplementation.  The Part A labelling is careful in exactly the way the record
needs: proved core, hardness judgment separated, gating conclusion resting only
on the proved half.

**s72 (C5) — the upper bound, on the enumerated cone.**  `dim(D₅ ∩ W) = 31 < 35`.
All four residues closed: `P ∩ c21` order 2 = **19**; the `ker ∩ coker` rank
strata are 0 and 9 only, both image 29; order `≥ 4` obstructed on the linear
route (evidence, not proof, and labelled so); the deeper rank-`≤2` strata drop.
The interior/boundary split with an exact Jacobian bound of 31 is new and closes
the image-versus-closure gap that s54/s59 raised and that Sol's S6 independently
re-raised this batch.  **It is honest about the one thing it does not prove** —
that the enumeration is complete — and correctly assigns that to S3.

**s73 (C6) — the theorem.**  `D = +1` at every rung, proved rather than
measured, plus five rungs measured to check the instrument against a predicted
answer.  The transport work is the best part: the same integer vector arrives by
direct Wiedemann measurement at each new rung and by transport from the previous
one, and session 62's independently exhibited vector transports into session
73's — two sessions, two drivers, two evaluation families, one line.

---

## 7. What I would do with this

1. **Push the tree**, before anything else.  It has now cost one duplicated
   verifier extension and would have cost more.
2. **The composition of §5 is the highest-value next unit of work** — s69's
   circuit as the source, s70's `S` (or direct reducible-point evaluation) as
   the consumer, and 12–15 CPU-hours of basis enumeration between them.  It is
   the first time in this programme that every LMR number has had a single
   named, priced obstacle.
3. **Reconcile the two verifier extensions** — one-word rename, and s73's
   `sparse_nullity` documentation should be merged with the banked one.
4. **s71 is missing** and C4's falsifier sweep is the one ungated result the
   batch does not have.
