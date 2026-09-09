# Session 77 — integrator review

Branch `s77-bridge`, base `afb8c33`, merged at `5784094`.  Bundle md5 matches;
pre-registration is the first commit; **no single-writer file touched**; **no
banked artefact modified** (all additions — the s75 trap did not recur here);
self-test still twelve cases.

## 1. The bridge is an identification, not a construction

This is the result and it is better than what the brief asked for.  The brief
asked for a *map* from S5 Pieri states to s69 bracket fillings.  s77's answer is
that there is nothing to construct: **a bracket filling *is* an unlabelled Pieri
chain.**  A column-strict filling of `λ` with content `(nᵟ)` is exactly a chain
`λ = ν⁽ᵟ⁾ ⊃ … ⊃ ν⁽¹⁾` of removable horizontal `n`-strips, the tableau tensor is
the iterated Pieri image of the seed, and because letters are unlabelled the
filling polynomial is already the `S_δ`-invariant projection — the same thing the
recursion computes as `ker(τ − I)`.

**Verified here on seven independent shapes.**  I wrote both enumerators from
scratch — SSYT with content `(nᵟ)` on one side, chains of removable horizontal
`n`-strips on the other — and the explicit map (*label each cell by the step at
which it appears*) is a bijection onto the SSYT set every time, with equal counts:

    (4,2) n2 d3: 3=3   (4,4) n2 d4: 3=3   (6,3) n3 d3: 4=4   (4,2,2) n2 d4: 6=6
    (3,3,3) n3 d3: 1=1   (5,2,2,1) n2 d5: 20=20   (6,6,2) n2 d7: 225=225

The consequence is the one that matters: **the map is evaluable by construction.**
No `x = y A^{-1}`, no coordinate expansion — the circuit pairs these vectors with
determinant points directly.  So on the filling side the recursion route's named
risk, *vectors that cannot be paired with determinant points*, does not bind.

## 2. Both controls, from a deterministic stream

`n = 3` LMR: generic rank 6, determinant rank 5, `i_det = 1` — the programme's
positive control, reproduced from canonical enumeration rather than sampling —
**and the banked determinant ideal line matched entry for entry** over 17,047
χ-coordinates, equal up to sign over `Z`.  `n = 4, δ = 12`: rank 2, `i_det = 0`.

Two factual claims I checked: `dim S^λ((17,17,2⁷)) = 6 741 370 483 828 179 366 024`
reproduces exactly by hook length; and S3's `u₀` really is
`results/s69_n4_seed.json` `basis[0]`, `C1 = [11,7,10,4,1,2,9,8,6]`.

## 3. The reconciliation the batch needs — s77 and s75 ran with different information

s77 reports the recursion→circuit change of basis `C` as **OPEN**, with its naive
route **priced out**: `ρ(π_i^{-1})` acts on the full Specht module, and that
module has dimension `6.74 × 10²¹` at the control, so even one coefficient's
covector lives there.  That pricing is correct and I verified the number.

s75 reports that **S3's continuation completed all four coefficients** by
symmetry-shortening the words (579/640 → 276/237) plus a frozen four-box
inclusion-DAG contraction — and I verified `C` there: nonsingular at both primes,
13/13 bridge identities each.

**Both are right about what they knew.**  s77 ran without S3's continuation and
correctly priced the route it could see; s75 consumed the continuation.  The
batch-level status is therefore:

> **The four coefficients are closed.**  s77's contribution is not a failure to
> close them — it is the *price of the naive route*, which is exactly the argument
> for why a compact routine was necessary rather than a convenience.

And the position is stronger than either session alone.  At the control cell the
programme now has **two independent evaluable sources**: S3's compact recursion
via the four coefficients (verified by s75), and s77's SSYT/filling basis
(evaluable by construction, needing no coefficients at all).  They agree on the
observable — `dim M₁₂ = 2`, `i_det(12) = 0`.

One reading trap worth marking: s77's own deterministic basis has directions at
`k = 9, 8`, while the **banked** seed fillings have `k = 7, 8` (checked).
Different bases of the same 2-dimensional space; no contradiction, but the report
puts both numbers close together.

## 4. The negative result, reported rather than buried

The measured ladder comparison, same points, same filter, same budget, source the
only variable:

| rung | `b_δ` | deterministic | random |
|---|---:|---:|---:|
| `δ = 14` | 54 | 7 | **24** |
| `δ = 13` | 37 | 8 | **18** |

**Random sampling beats canonical enumeration for discovery**, because the
deterministic births cluster in a low-rank subspace.  That is the opposite of what
a deterministic-basis session hopes to find, and s77 reports it plainly and draws
the right conclusion: it agrees with the batch's own finding that discovery is not
the binding constraint, and the deterministic basis earns its place through
**reproducible assembly and certification**, which §2's controls demonstrate.

The generator engineering banked with it is worth keeping: one-columns are the
forced sorted tail so they complete without backtracking (400 SSYT in ≤0.1 s at
`δ = 22`); of three canonical orders, small-values-first buries births under the
`u`-tower at high `δ`, and the maximal-overlap class alone under-spans — so a
spanning stream must mix `k`.

## 5. Process

- It flagged the same tree defect I found: **S3 is not in the reachable tree**,
  `origin/main` still `afb8c33` with only `results/astra/{S1,S2}`, so it had to
  reach S3 through the device bridge.  Two sessions have now paid for that.
- `python-flint` was absent from its container and it installed it — an
  environment gap, correctly not reported as a result.
- It declined an in-band attribution reminder embedded in a file it read — the
  eighth session to do so.
- It ran an **adversarial subagent** that wrote its own SSYT generator and points,
  reproduced rank 6 / determinant rank 5, and added a check neither the brief nor
  I asked for: upper-unitriangular invariance, 18/18 invariant and 18/18 *not*
  lower-triangular-invariant — a proper highest-weight witness independent of
  s69's Identity 1.  It also built a second, 5/6-disjoint rank-6 basis to show the
  span is not an artefact of one enumeration order.  That is better verification
  practice than the brief required.

## 6. Ledger

| claim | status |
|---|---|
| bracket filling = unlabelled Pieri chain (SSYT); the polynomial is the `S_δ`-invariant projection | PROVED; **bijection re-derived here on 7 shapes** |
| the map is evaluable by construction — no `S^λ` ever formed | PROVED |
| `n = 3`: rank 6, `mult_det = 5`, `i_det = 1`, banked ideal line entry-for-entry over `Z` | MEASURED + CERTIFIED |
| `n = 4, δ = 12`: rank 2, `i_det = 0`; `k = 9` class alone rank 1 | MEASURED |
| `dim S^λ = 6.74 × 10²¹`; naive route to the four coefficients priced out | PROVED; **re-derived here by hook length** |
| the four coefficients themselves | **CLOSED by S3's continuation, verified by s75** — s77's OPEN is superseded, not wrong |
| deterministic vs random for discovery at `δ = 13, 14` | MEASURED; random wins, reported plainly |
| goal-cell ranks, `D` | untouched — the session produces no `D` and no padded evaluation |
