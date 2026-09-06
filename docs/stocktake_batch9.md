# Programme stock-take at the end of batch 9

> **Correction (applied at merge of s56 and s57, same day).**  §1 below is wrong
> on its central claim and §4's gating changes with it.  **Both sessions ran.**
> Their bundles existed and had simply never been handed to the integrator, so
> they were absent from the repository when this was written; they are merged
> now.  §6 states what actually changed.  Everything in §2 and §3 stands, and
> §2 gains two rows.  The ladder theorem's attribution also changes: **s57 proved
> it first**, on 5–6 September; the audits and my notes to s58–s60 rederived it.

Written at the checkpoint after s58, s59, s60, s61, the Rees audit and the
slot-6 audit.  Three parts: what the repository actually holds (§1), what died
(§2), and what the next ten should be (§4) — which differs from the sketch on
the table in three places, one of them because the sketch contains a number that
is zero.

## 1. Inventory — and the gap the list on the table hides

**In the repository, with pre-registration, artefacts and a merge commit:**
s21–s52 (as before), s54, s55, **s58, s59, s60, s61**.  413 certificate files;
159 documents.

**Not in the repository at all:**

| session | status |
|---|---|
| s53 | retired by decision (its motivation was removed by s55) |
| **s56 — the `Θ⁺` engine** | **never run.  No pre-registration, no code, no results.** |
| **s57 — the ladder/selector session** | run outside the repository; **results exist only as a relayed summary** |

This matters more than any other line in the stock-take.  The list of things "we
have" includes "s57 ladder theorem" and "Foulkes proof audit", which is true of
the *theory* and false of the *instrument*:

- The **ladder theorem is banked** — proved, checked here step by step, checked
  again on 2 107 length-5 tails and on 239 of s60's own measured pairs, and used
  to close 99 tails.  Its proof came through the audits, not through s57.
- The **Foulkes identification `mult_det = rank Θ⁺` is banked as theory** and
  nothing else: there is no implementation, anywhere, of `Θ⁺`.
- s57's other content — the 34 closed six-row ladders, the peaked theorem for
  `ℓ ≤ 16`, the nominee table — is **relayed, not verified, not committed**.  The
  one piece of it I did reproduce independently is the LMR `a`-sequence
  (`2, 39, …, 273, 274`, and `a_∞ = 274` proved by carrying the ladder to
  `δ = 31`).

**So: of the two things every party ranks first, one has zero lines of code and
the other is blocked on it.**  This batch built excellent instrumentation and
produced twelve clean negatives, and did not start the one experiment that could
produce a positive.  That is the finding the next batch has to answer.

## 2. What died — twelve routes, and why that is the batch's real output

| # | route | killed by |
|---|---|---|
| 1 | LMR family as a source of equations at `r ≤ 8` | s55 census (`k ≥ min(6,r−2)` vs `k ≤ r−3`) |
| 2 | `a = 1` as a selection principle | s52 |
| 3 | small `a` as a rank-drop mechanism | s52 |
| 4 | small `a_∞` as a rank-drop mechanism | s60: 99 closed tails, `a_∞` 1…56, all full rank |
| 5 | final ambient jump `= 1` as a selector | integrator: 42 % of live length-5 tails have it |
| 6 | "lateness" of the final birth as a selector | integrator: LMR's two instances straddle the mean (0.632, 0.444) |
| 7 | `sk/a` balance as a rank-loss mechanism | s57 (relayed) + the Foulkes audit: `a`, `sk` are dimensions, rank is the question |
| 8 | balance as a search axis at length 5 | s60 §4 + `λ_1 ≥ 3δ`: a balanced weight is never in its ladder's stable range |
| 9 | generic higher contact order `q ≤ 4` at `r = 5` | s59 (`29,29,28,28,24` invariant in `q`) |
| 10 | **compression incidences as a source of exotic first-order directions** | **integrator: `ker dΦ = T C_{21} + T C_{32}` exactly; transverse quotient 0 at three incidences** |
| 11 | slot-6 algebraisation below degree 24 | slot-6 audit: the `21×21` Fitting route computes the unsaturated length |
| 12 | `h_pad` exactness on the reducible side | s47 (`ℓ = 6`), s60 (`ℓ = 5`, eleven cells) |

Twelve dead routes is a good batch.  Note the pattern in 2–8: **seven of the
twelve are selectors read off ambient plethysm data, and every one of them
carries no signal.**  That is now a result in its own right and it is the
strongest argument for nominating from the equation side instead.

## 3. What is banked, and how firmly

**Proved.**  The ladder theorem (all five quantities monotone, constant for
`δ ≥ t`, `a_∞ = a_t`, a closing-cell full-rank result kills a tail forever).
The `s61` specialisation inequality (`P ∈ closure(GL·det_4) ⟹ δ_k(P) ≤ δ_k(det_4)`).
`per_3^∨ = {4·per(B∘B) − 2·per(B)² − det(B)² = 0}`, irreducible, with
`codim Sing = 3`, hence `δ_6(per_3) = 30` as a theorem.  `dim(D_5 ∩ W) ≥ 31`
certified over `Q`.

**Measured and independently reproduced here.**  Both polar profiles and the
padded quartic in 16 variables; `a = 274`, `a_23 = 273`, `a_∞ = 274`;
`g = 92 000` by a third route; twelve boundary-family `sk` values and the `n = 3`
LMR cell; the length-5 census sizes; all 1 075 tails' `t`, `a_∞`, `δ_close`;
`dim D_5 = 50` and the exact-locus `29/29/31/31`.

**Measured, single source.**  `sk = 48 825` (the `A = 5 650` half rests on s58's
reduction and the Manivel route, not on anything of mine).  s60's
`mult_det = a` at 419 cells — of which **264 carry no checkable certificate**,
their proof being algorithmic.  s59's contact-order invariance at `q = 2, 3, 4`.

**Relayed only.**  All of s57 beyond the LMR sequence.

## 4. The ten — with gating, and three changes to the sketch

The sketch on the table is *3–4 `Θ⁺`/LMR, 2 padded-side, 2 `r = 5` normal cone,
1 length-5 selector, 1 audit*.  Three changes.

**(a) `Θ⁺` is a gate, not a quota.**  Sessions 2–4 below cannot start until
session 1 exists and passes.  Running them in parallel would mean three sessions
briefed against an unvalidated engine.

**(b) The `r = 5` normal cone is not four-dimensional; it is zero-dimensional.**
`docs/rees_boundary_audit.md`: at `C_{21} ∩ C_{32}`, at `C_{21}` alone and at
`ker ∩ coker`, `ker dΦ` is exactly the span of the base components' tangent
spaces.  Two sessions briefed on "the four-dimensional transverse problem" would
be briefed on nothing.  One session, re-pointed at the **primitive family**.

**(c) A "length-5 tail selector" session is the wrong instrument.**  §2 rows
2–8 say selectors do not work; s60 says closure by cost does.  Make it a
throughput session.

### Gate

1. **Build `Θ⁺` and validate it against a known rank drop.**  Mandatory
   calibration, in this order: the nine exact `δ = 3` blocks including the three
   with `a = 1, sk = 2` (rank-one `C → C²`); at least one banked `δ ≥ 6` six-row
   cell against the existing HWV engine; and — the one that matters — the
   **`n = 3` LMR cell `((19,7,2⁵), 12)`, `a = 6`, `sk = 10`, which must return
   rank ≤ 5**.  Every other cell the programme has measured is full rank; this is
   the first rank drop the engine would ever be shown, and it costs a `6 × 10`
   matrix.  If it returns 6, stop the batch and fix the engine.

### Gated on 1

2. **The LMR predecessor** `((61,17,2⁷), 23)`, `C²⁷³ → C⁴⁸ ⁸²⁵`.  Full rank there
   forces `i_det = 1` at the LMR cell exactly.  Cheaper than the LMR cell and
   strictly more informative.  Note `δ = 23` is below Manivel's threshold, so its
   target dimension rests on s58's reduction alone.
3. **The LMR cell itself** `C²⁷⁴ → C⁴⁸ ⁸²⁵`, if 2 does not settle it.
4. **The padded side at the LMR cell.**  `i_det = 1` is not `D > 0`;
   `D = i_det − i_pad` needs `i_pad` at the same cell.  This is the session that
   would produce the programme's first `D > 0`, and it is the reason 2 and 3 are
   worth running at all.

### Ungated — these can start now

5. **The `r = 5` special fibre, at the primitive family.**  s59 named the
   deliverable (`dim F(J_C)`, or an upper bound on `dim(D_5 ∩ W)`) and said it
   needed a CAS; Singular, msolve and Macaulay2 are now available and s61
   demonstrated the discipline.  This is the **only route in the programme to a
   theorem rather than a measurement**, and the primitive family is the one base
   type where no transverse direction has been ruled out.
6. **The length-5 closure walk.**  Walk `results/s60_tail_census.md` by `n_χ`:
   199 tails close below `n_χ = 100 000`, settling 775 census rungs.  Include the
   named engineering deliverable — widen the int64 multiset code — which unblocks
   the 183 tails with `δ_close > 18`.  High certainty, low variance.
7. **The certificate gap.**  Add a `gct-cert/1` kind for the sparse-route
   Wiedemann nonsingularity certificate (seeds, levels, pinned evaluation rows,
   checked kernel candidates) and back-fill s60's 264 uncertified cells.  Nobody
   has proposed this and it protects the largest single body of claims in the
   programme.
8. **Commit s57, or re-run it.**  Its results are load-bearing for the nominee
   discussion and exist only as prose.  Either its artefacts enter the repository
   with a pre-registration, or the claims are marked relayed everywhere they are
   used.  Cheapest version: re-derive the six-row ladder census with the tail
   engine that already exists (`wk9_s60_tails.py` generalises), which also gives
   the 34-closed-ladder count a proved `a_∞` rather than an observed plateau.

### Judgement

9. **A `dc̄` reach audit.**  Every obstruction the programme holds certifies
   `dc̄(per_3) ≥ 5`, which is LMR's bound.  One session should ask, adversarially,
   what would have to be true for *any* instrument now in hand to reach 6 — and
   say plainly if the answer is "none of them can".  That is worth knowing before
   another ten sessions are spent.
10. **Independent adversarial synthesis**, as proposed — with one instruction:
    it should read `docs/` rather than the reports, because five of this batch's
    corrections were to statements that were right in a report and wrong in the
    summary of it.

### Split

1, 2, 3, 4, 6, 7 are implementation and belong with the side that has the
repository, the engines and the certificate format.  5, 8, 9, 10 are theory,
audit and reconstruction and split naturally the other way.  That is 6/4 rather
than 5/5, and the imbalance is the point: this batch was 5/5 and produced no
implementation of the one instrument everything else is waiting on.

## 5. Housekeeping, due now

The history rewrite (`tools/rewrite/run_rewrite.sh`, prepared and tested at
`0960bd5`) has been pending across the whole batch.  A batch boundary is when to
do it.  **Order matters: take the private `gct-archive` from the pre-rewrite
state first, then force-push the rewritten history.**  Two further corrections
are queued for the same pass: `results/occurrence_screen.md`'s claim that
`δ = 11, 12` exceed budget (false since s58), and `results/longweight_screen.md`'s
silence about the s39 engine's `N ≤ 64` and bead-width limits.

## 6. Correction, after s56 and s57 were merged

### What was wrong

| §1 said | actually |
|---|---|
| "s56 — the `Θ⁺` engine — never run.  No pre-registration, no code, no results." | **ran**; pre-registration `5d63e7c`, three commits, eight certificates, 40 cells |
| "s57 — results exist only as a relayed summary" | **ran**; pre-registration `905c1a2`, the brief committed beside it, full artefacts |
| "the ladder theorem … came through the audits, not through s57" | **s57 proved it** (Lemma L, Proposition S), and proved a sharper version |

### What survives, in a different form

The stock-take's headline was *"of the two things every party ranks first, one
has zero lines of code and the other is blocked on it."*  The letter is wrong.
The substance is not, and s56 is why:

> `Θ⁺` **is** built and **does** calibrate — 40/40 at `δ = 2, 3, 4` — and the
> session measured that it **cannot reach any cell where a rank drop could
> live**.  `|H_{4,5}| = 2 546 168 625` and the engine is quadratic in that
> module, so the six-row cells, every length-5 cell at `δ ≥ 5`, the `n = 3`
> positive control at `δ = 12` and the LMR cell at `δ = 24` are all beyond it.

So the gate is still shut.  What changed is that it is now **characterised
rather than unopened**, which is a much better position: we know the
construction is right, we know exactly what makes it infeasible, and we know
what a successful continuation must avoid.

### The revised item 1

Not "build `Θ⁺` and validate it" — that is done.  Instead:

> **Does the rank admit a tail reduction?**  s58 showed the *target dimension*
> `sk(λ, 4×δ)` reduces to class sums over `S_{|λ̄|}`, with `N` absent from the
> cost — the LMR cell in 0.2 s against `p(96) = 1.2 × 10⁸`.  s56 shows the
> *rank* as currently computed is quadratic in `H_{4,δ}`.  The session is: push
> the Gram kernel `K(π,π')` and its Hadamard square through s58's reduction, or
> establish that it cannot be done.

That is well-posed, has a worked precedent inside the programme, and either
outcome is worth the slot.  Items 2, 3 and 4 remain gated — on *that* engine,
not on s56.

### Other consequences

- **Item 8 is void.**  s57 is in the repository.
- **`(30,2⁵)_{10}` is dead** — s57's Theorem P: the peaked family has `a_∞ = 1`
  with the bordered discriminant as its unique highest-weight vector, nonzero at
  a generic pencil, at every `ℓ ≤ 16`.  I had named that cell as the single best
  next test; it needs no measurement and never did.
- **§2 gains two rows.**  `sk/a` is now refuted four ways, the fourth being
  s56's sharp `δ = 4` cells (`a = 1` against `sk = 11` and `sk = 10`, rank 1 at
  both), and s57's `1 033 030`-weight sample puts the LMR cell in the 0.4 % most
  skewed of its slice.
- **A new object worth a session on its own.**  Proposition S identifies the
  stable `i_det` as the multiplicity of `S_λ̄` in the ideal of `M_ℓ`, the variety
  of characteristic polynomials of traceless `(ℓ−1)`-pencils of `4×4` matrices.
  That turns "a rank drop somewhere up this ladder" into "an equation of one
  explicit affine variety" — and `M_ℓ` is small enough for the CAS that is now
  available.  It did not exist as a target when §4 was written.
- **`tools/verify/verify.py`** has a real defect (s56): large `nonvanishing_minor`
  determinants fail the `content` line on Python's integer-to-string limit after
  the rank checks pass.  One line to fix, in the same pass as the rest.
