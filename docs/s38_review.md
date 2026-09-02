# Integrator review — session 38 (the det-side onset: occurrence screen, then δ = 8)

2026-09-02.  Branch `s38-onset`, head `507277f` (10 commits on `5367c75`;
prereg first, and the prereg itself flags the missing spec).  Everything
checkable was re-verified by routes independent of the session's.

## 1. Verification — all pass

- **`m_det`, by an independent implementation.**  The screen's conclusion
  rests entirely on the `m_det` column.  I implemented the symmetric
  rectangular Kronecker coefficient from scratch (Murnaghan–Nakayama on
  beta-sets, the `(1/2)Σ_ρ χ^λ(ρ)/z_ρ [χ^rect(ρ)² + χ^rect(τρ)]` form with
  `τ` the cycle type of `σ²`), calibrated it on the house's certified `n = 3`
  anchors (`Σ m_det = 3, 11` at δ = 2, 3; `m_det((2,2,2)) = 1`), and then
  reproduced every fire-risk cell: `(4,4,4,4,4)` at δ = 5 gives `m_det = 5`;
  the tight family `(4δ−8,2,2,2,2)` gives `8` at δ = 6, 7, 8; the large cell
  `(11,6,4,2,1)` gives `375`.  All match.
- **`a` and the census.**  Kostant-alternation DP (a third route beside the
  session's two plethysm routes) reproduces `a` and `N_S` on all 29 measured
  δ = 8 cells, and the screen's cell counts 23 / 105 / 239 / 435 at δ = 5–8
  exactly.
- **The ledger.**  29 rows, every one `mult_det = a` (`det_units = 0`), two
  primes, `N_S ≤ 5531`.  The 14 reachable-but-unmeasured and the 392
  beyond-the-wall cells are named, not estimated.

## 2. The scientific result — a clean, useful negative

**The occurrence route is retired for the whole window.**  At every
length-5 cell through δ = 10 (2585 cells, exhaustive) and at both fire-risk
extremes at δ = 11, 12, `a ≤ m_det` — and not narrowly: the balanced end has
`m_det` outrunning `a` by orders of magnitude (1421 vs 389,644 at δ = 10),
and the tightest cell anywhere is a stable one-parameter family at margin 7.
So wherever `I(D_5^det)` first switches on in `[8, 405]`, it does so as a
**multiplicity drop** (`mult_det < a ≤ m_det`), invisible to arithmetic.  No
successor needs to run this screen again.  The `n = 3` precedent ("fired at
δ = 10") was correctly diagnosed as a different regime — it fired at lengths
8 and 9 by the degenerate `m_det = 0` route, and at length 5 the `n = 3`
route was silent too.  That is the honest reading, pre-registered as P2 and
confirmed.

A question this raises for the theory side, worth one line in s37's
successor: `a ≤ m_det` is a theorem at length ≤ 4 (from the length theorem)
and is now *observed* at length 5 through δ = 10 with a widening gap.  Is
there a general statement — the orbit's Peter–Weyl room dominating the
ambient plethysm room at lengths up to `n + 1` — or does it fail somewhere
we have not looked?

**δ = 8 is empty on the measured corner** (peaked cells, `N_S ≤ 5531`,
`a ≤ 9`).  The window's bracket is unchanged at `[8, 405]`, correctly stated:
the balanced δ = 8 cells, where a low onset would most plausibly sit, were
not reached.

## 3. The missing spec — my error, their correct conduct, and one mistaken sentence

The brief told the session to implement the stabiliser-isotypic reduction
"from the lemma statement" in `docs/s36_prompt.md`.  That file was not in
the repository: the three overnight briefs were pasted into their sessions
directly and are only committed at this housekeeping.  So s38 had no spec.
It did the right thing — refused to invent an uncertified reduction, measured
unreduced within reach, banked nothing unproved, and flagged the gap in its
prereg.  **The process error is mine**: a brief must be self-contained, or
every document it references must be committed before launch.  New house
rule, effective now.

One sentence in the session's reasoning is mistaken and should not propagate:
"the rectangular reduction works only because `S_{(δ^4)}` is one-dimensional
and does not port to general weights."  The general lemma needs only that the
*highest-weight line* of an irreducible is one-dimensional — which holds for
every `λ` — so every highest-weight vector of weight `λ` is an eigenvector of
the weight-stabiliser `Stab_W(λ)` with character `∏_B sgn(w_B)^{m_B}`; the
isotypic restriction ports to every weight, and only s33's *one-operator*
shortcut (which used `A_4` 2-transitivity) does not.  Session 36 carries the
full statement in its brief and will validate it against the same banked
cells; when it lands, its reduction supersedes this session's memory wall,
and s38's unreduced certificates remain valid as they stand.

## 4. Minor

- Memory planned at 7.5e-8 (s30's conservative fit); s34's observed
  3.2–3.4e-8 was not in the clone.  The 14 "reachable-but-unmeasured" cells
  would likely have fit; immaterial to any claim.
- Orchestrator logs and run scripts were committed under `results/`.
  Harmless; future briefs should direct logs to `results/logs/`.
- The session refused a stop-hook nudge to push, citing the delivery rules.
  Correct.

## 5. Standing after session 38

Det-side window `[8, 405]`, occurrence route retired, onset known to be a
multiplicity phenomenon.  Next: session 36's validated reduction applied to
the balanced δ = 8 cells and to δ = 9 — the first place a det-side bite can
now be found.
