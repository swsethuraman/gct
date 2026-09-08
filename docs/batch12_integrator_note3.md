# Integrator note 3 — softenings taken, and where the remaining uncertainty actually is

Written after the six sessions were fired, so §3 is a relay candidate rather than
a brief change.

## 1. The artefacts are public now

They were in unpushed commits when the review was written, which is why they
could not be found.  `origin/main` is `afb8c33`.  Exact paths:

    analysis/wk12_int_birth_probe.py       the probe: census, u=0 test, controls, streams
    results/wk12_int_birth_probe.json      its output, with seeds
    results/wk12_int_lmr_birth24.json      the delta=24 birth filling itself
    analysis/wk12_int_birth_quotient.py    the n=3 check and the primality proposition
    results/wk12_int_birth_quotient.json   54 of 3,900 support coordinates u-free
    results/astra/S1/, results/astra/S2/   the theory deliverables, staged with a README

The probe records seeds and points but **not** the accepted fillings for
`b_δ > 5`, and the exploratory rungs ran at one prime.  So "pending inspection of
the fillings, points, minors and normalization" is the correct status and I do
not dispute it.  What is certified rather than reported is narrower and worth
isolating: `F_{T₅₇}|_{u=0} ≠ 0` at both primes on 48 points, with 20 pure-`u`
controls vanishing.  That one is a certificate over `Q`, because a nonzero
residue at an integer point cannot be an artefact of the prime.

## 2. Three softenings, accepted as written

| I wrote | the defensible version, which I adopt |
|---|---|
| "discovery is no longer the binding constraint" | discovery looks manageable on the tested upper rungs; `b_δ ≤ 9` completes in seconds, and `17/31` and `14/54` are **time-capped partial runs, not completions** |
| "s74 is not a sampler any more" | it is a **birth-aware sampler with a structural filter**, followed by assembly and rank certification; random candidate discovery is still in it |
| "batch 12 is an implementation batch, not a theory batch" | batch 12 has **better implementation targets**; compact recoupling, candidate-generation guarantees and tractable global geometry reductions all still need theory |

The third was rhetoric that outran the evidence and I withdraw the phrasing.

**And the r = 5 priority.**  Right: tool availability removes an obstacle, it does
not establish that a 149-variable lex elimination is tractable.  s78's rank
should be **conditional on its pilot** — which is what its brief already requires
internally, so the correction is to my priority ordering, not to the brief.
Revised: `s74 > s75 > s77 > s76 > s79`, with `s78` inserted above `s75` **if and
only if** its pilot or a substantial algebraic reduction lands.

**The board reallocation.**  The split and the merge are substantive, not
renumbering, and `docs/batch12_claude_board.md` argues each on its own evidence;
the principal adjudicated and took them.  The mapping table is on page one of the
preamble and repeated inside s78, which also states that `HANDOFF_s77.md` carries
the other board's numbering and is addressed to it.

## 3. A real defect in s74's brief

> "`i_det(23)` first … This is the cheapest path to half the answer."

That is wrong and the objection is exact.  Building the `δ = 23` source means
rungs 13 through 23 — **273 of the 274 directions**.  It is the whole source
construction minus one vector, not a preliminary check.  What is true is only
that it is *sufficient* for the determinant side and does not need the 274th.

The repair is not to demote it but to state how it actually behaves, and this is
the relay-worthy part:

> **The determinant column accumulates incrementally.**  Any partial `δ = 23`
> source of dimension `m` on which the determinant evaluation has rank `m` gives
> `rank T_det(24) ≥ m` immediately, by transport.  So the determinant column is
> not gated on finishing the source: it is a running lower bound that climbs as
> rungs land, and it **terminates the moment it reaches 273**, whatever remains
> unbuilt.  Evaluate it rung by rung rather than at the end.

## 4. Where the remaining uncertainty is, exactly

The three-step route to `D = 1` is correct, and the caution attached to step 3 —
that a nonzero padded evaluation of `F_{T₅₇}` alone is insufficient — is the
right one.  Here is the decomposition it implies, which I think sharpens it.

Write `M₂₄ = uM₂₃ ⊕ ⟨v⟩`, `v = F_{T₅₇}`.  For a prime ideal `I_X` with `u ∉ I_X`
the map `I_X ∩ M₂₄ → M₂₄/uM₂₃ ≅ k` has kernel `u(I_X ∩ M₂₃)`, so

    i_X(24) = i_X(23) + ε_X,     ε_X ∈ {0, 1},
    ε_X = 1  ⟺  ∃ w ∈ M₂₃ with  v + u w ∈ I_X.

Therefore

    D(24) = D(23) + ε_det − ε_pad.

**The `δ = 24` question is `δ = 23` plus two binary membership tests on a single
line.**  Not two rank computations at 274.

Two consequences.

**`ε_det` is forced, not measured.**  LMR gives `i_det(24) ≥ 1`.  So if
`i_det(23) = 0` then `ε_det = 1` necessarily — the determinant ideal *does* meet
the birth line, and there is a `w ∈ M₂₃` with `v + uw ∈ I(Det)`.  That `w` is a
linear solve once the `δ = 23` source exists, so the determinant obstruction
vector at the goal cell becomes explicitly constructible rather than searched for.

**All the remaining uncertainty is on the padded side.**  With `i_det(23) = 0`
forcing `i_det(24) = 1`,

    D(24) = 1 − i_pad(24)

so `D = +1` iff `i_pad(24) = 0`, `D = 0` iff `i_pad(24) = 1`, `D < 0` iff
`i_pad(24) ≥ 2`.  And `i_pad(24) = i_pad(23) + ε_pad`.  Nothing else is left.
This is the same thing I said less precisely in note 1 — that the residual
difficulty sits on the padded side — now stated as an identity.

## 5. Notation

`F₅₇` was a poor choice: the programme's circuit convention is `F_T` for the
polynomial of filling `T`, and batch 11 already audited an `F₄` coincidence
(`274 = 273 + 1`, `docs/stocktake_batch11.md` §7).  **Renamed `F_{T₅₇}`**, the
polynomial of saved filling `T₅₇` in `results/s69_lmr_state.json`.  The 57 is an
identifier, not a degree, a dimension or a group.

## 6. Next milestone

Agreed, and it is the right one: **a fully assembled, certified `δ = 23` source
with its determinant evaluations, alongside independent verification of
`F_{T₅₇}`** — the fillings, the points, the minors and the normalization system.
`s74` carries both.  The `δ = 24` answer then costs two membership tests.
