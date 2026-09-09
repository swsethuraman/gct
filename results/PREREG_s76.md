# Pre-registration — session 76: scale the recursion to `δ = 24`, measure `C₂₄`

Committed before any measurement.  Brief: `docs/s76_prompt.md` (the reconciled
proposal's s75, second half).  Preamble: `docs/batch12_worker_preamble.md`.

- Base commit: `main` = `afb8c3319d3d1f3afc3d2578c8cb322f2b8a3b92`
  (`docs/batch12_s1_s2_consolidated.md` present; `tools/verify/selftest.py`
  12 cases PASSED; `python-flint` had to be installed — an environment gap,
  recorded, not a result).
- Branch: `s76-scale24`.  Delivery by bundle against the base.
- Gate run: `two_strip_paths(24)` = 160 paths over 42 shapes, identical to
  `δ = 14` (160 / 42) and against 36 / 23 at `δ = 12` — the saturation the brief
  states, reproduced.
- s75 has not reported; nothing of its interface is in the tree.  Everything
  below is built against the specification in the brief, and the assumptions
  about the Pieri embeddings and the evaluation map are recorded in §4 so that a
  later session can tell which results depend on them.
- Primes: `2147483647` (house prime 1) for every modular step; `2147483629`
  (house prime 2) as a second run where time allows.  No prime below 97
  anywhere (`|λ₂₄| = 96`).

## 1. Question A — `C₂₄` exactly (the deliverable that lands either way)

`C_δ = dim (S^{λ_δ})^{K'}`, `K' = H_{δ−2} × S₄ × S₄`,
`C_δ = Σ_{two-strip paths λ→μ→ν} a_{δ−2}(ν) = Σ_{μ} B_{δ−1}(μ)`.

Instrument: `analysis/wk11_int_cdelta.py`'s functions (`weyl_terms`, the pruned
Weyl alternation with terms collapsed by sorted key; `wk9_s42_census.N_S_tail_n`,
the tail DP) driven by `analysis/wk12_s76_c24.py`, which adds a per-50-key /
30-second checkpoint, two workers over the 42 shapes, and a per-shape bank in
`results/s76_c24/shape_NN.json`.  The instrument is the one that produced
`B₂₄` and `C₁₂`; only the checkpoint granularity and the worker split are new.

Prior (labelled EXPECTATION, from the brief): `C₂₄ ≈ 1.7 × 10⁴`, from the
one-level ratios `C₁₂/B₁₂ = 7.71` and `B₂₄/a₂₄ = 7.91`; `2168 × 7.7 ≈ 16 700`.
The measurement replaces it.

Internal checks the run must pass (each a stopping rule if it fails):

- **A1** every channel `a₂₂(ν) ≥ 0` (it is a multiplicity).
- **A2** the shape `(57,17,2⁷)` is `λ₂₂` on the LMR ladder and must return the
  banked `a₂₂ = 272` (s57/s63 ladder `2,39,93,145,188,219,241,255,264,269,272,
  273,274,274` at `δ = 12..25`).  This is the analogue of `B₂₄`'s `273`
  self-check.
- **A3** `C₂₄ ≥ B₂₄ = 2168` (`W_δ ⊂ (S^λ)^{K'}` forces it).
- **A4** `C₂₄ = Σ_{μ} B₂₃(μ)` with `B₂₃(μ) = Σ_{ν ⊂ μ} a₂₂(ν)` (a bookkeeping
  identity inside the engine; recorded per predecessor).

What counts as the result: the integer `C₂₄`, the 42 channels `a₂₂(ν)` with
their path multiplicities, the 12 values `B₂₃(μ)`, and the engine time.  A
partial run is reported as the banked shapes plus the remaining ones' term
counts — an interrupted run loses at most 50 keys.

## 2. Question B — the recursion at `δ = 24`: precursor, operator, source

The S5 one-block recursion (`docs/sol/sol_batch11_report.md` §5.4, restated
correctly in `docs/s75_prompt.md`): `W_δ(ν) = (S^ν)^{K_δ} = ⊕_{ν/ξ horiz.
4-strip} M_{δ−1}(ξ) ⊗ (S^{ν/ξ})^{S₄}`, and `M_δ(ν) = W_δ(ν) ∩ Fix(τ)` where the
block swap `τ` is a genuine involution on `(S^ν)^{K'}` (`τ` normalises `K'`)
but does not preserve `W_δ`.

The implementation, stated so its assumptions are visible:

- **Model.**  `S^ν` in Young's seminormal form (rational matrices; every
  denominator is an axial distance, `< 97`, hence invertible at both house
  primes — this is exactly what "no prime below 97" buys).  The chain is
  `S₄ ⊂ S₈ ⊂ … ⊂ S_{4δ}` by blocks.
- **Strip invariants.**  For a horizontal 4-strip `ξ/η` (a disjoint union of
  row segments, so `S^{ξ/η} ≅ M^{(k₁,k₂,…)}` as an `S₄`-module) the trivial
  vector `c^{ξ/η}` in the seminormal basis of standard fillings is computed as
  `⋂_i ker(s_i − I)` and normalised by a rule that depends only on the skew
  diagram (coefficient 1 on the lexicographically first standard filling).
  Every use of the embedding `M_{δ−1}(ξ) ⊗ c^{ξ/η}` uses this same vector.
- **Recoupling.**  For each two-strip skew diagram `D = ν/η` the involution
  `τ = (1 5)(2 6)(3 7)(4 8)` (block swap of `S₈`) is computed on the seminormal
  module `S^{D}`, restricted to the `(S₄×S₄)`-invariants in the basis
  `u_ξ = c^{ξ/η} ⊗ c^{ν/ξ}` indexed by the intermediate shapes `ξ`; the
  `m(η) × m(η)` matrix `R^{D}` is exact over `Q`, checked to satisfy
  `R² = I`, and reduced mod `p`.  `m ≤ 10` at every node; the set of skew
  diagrams is the same at every `δ ≥ 14` (saturation).
- **The operator.**  At node `(ν, d)` a vector of `W_d(ν)` is a coefficient
  vector `c ∈ F_p^{B_d(ν)}` over the bases of the `M_{d−1}(ξ)`; its
  coordinates in `(S^ν)^{K'} = ⊕_{(ξ,η)} M_{d−2}(η)` are read off the stored
  matrices `E_{d−1}(ξ)`; `τ − I` acts block-diagonally over `η` as
  `(R^{ν/η} − I) ⊗ I_{a_{d−2}(η)}` on the `ξ`-index.  `M_d(ν)` is the kernel
  of that `C_d(ν) × B_d(ν)` system; its reduced-row-echelon basis is
  `E_d(ν)`, an `a_d(ν) × B_d(ν)` matrix.  This is deterministic given the
  prime and the coordinate order.
- **Memoisation.**  Bottom-up over the 7 658-node DAG of shapes reachable from
  `λ₂₄` (recounted here: 1 + 5 + 22 + … + 12 + 1, peak 585 per level at
  `δ = 12..16`; the integrator's 7 656 counts `δ = 1..23`).  Only one level of
  `E` matrices is held at a time.

Pre-registered predictions (each is a check of the operator, and each failure
is a stopping rule):

- **B0** base cases: at `δ = 2` the recoupling on the one-dimensional channel
  spaces is `+1` for `ν ∈ {(8),(6,2),(4,4)}` and `−1` for `(7,1),(5,3)`
  (`h₂[h₄] = s₈ + s₆₂ + s₄₄`), so `a₂(ν)` comes out `1,0,1,0,1`.
- **B1** at every node the kernel dimension equals the plethysm coefficient
  `a_d(ν)`; checked against an independent Weyl-alternation value at every
  node of the `λ₁₂` sub-DAG (921 nodes; the 23 shapes at `δ = 10` are banked in
  `results/wk11_int_c12.json`) and at every node of levels `δ ≤ 8` of the full
  DAG, at the LMR ladder rungs (banked s63 values), at the 12 predecessors at
  `δ = 23` (banked `results/wk11_int_b24.json`) and at the 42 shapes at
  `δ = 22` (Question A).
- **B2** the `δ = 12` control: `B₁₂ = 31`, `C₁₂ = 239`, `dim M₁₂ = 2` (s75's
  control, reached here as a by-product; the *evaluation* half of s75 is not
  claimed).
- **B3** the independent re-derivation the brief asks for: the twelve kernel
  dimensions at `δ = 23` sum to `B₂₄ = 2168`, with the ladder predecessor
  `(61,17,2⁷)` returning `273`; the goal-cell kernel has dimension `274`; and
  the operator's intermediate space at the goal cell has dimension equal to
  Question A's `C₂₄` (a second, independent route to `C₂₄`: kernel dimensions
  at `δ = 22` instead of Weyl alternation).
- **B4** `Fix(τ)` on `(S^λ)^{K'}` has dimension `Σ_η a₂₂(η)·f(η)`,
  `f(η) = dim Fix(R^{λ/η})`; `M₂₄ = W₂₄ ∩ Fix(τ)` must have dimension exactly
  274 — not `dim Fix(τ)` and not `B₂₄`.

Stopping rules for B:

- a kernel dimension that disagrees with a checked `a_d(ν)`: stop the climb,
  report the node, the two numbers and the recoupling diagram involved;
- memory or time on the DAG: report the **peak weighted state count** — per
  level `Σ_ν a_d(ν)·B_d(ν)` entries stored and the largest `C_d(ν) × B_d(ν)`
  system solved — and the level reached, with the banked levels below it.

## 3. Question C — the four evaluation columns

EXPECTATION (labelled, `P ≈ 0.9`): the compact source cannot be evaluated
without an unfolding of carrier scale.  The step is the conversion of a
compact coordinate vector (coefficients over the recursion's bases) into any
representation on which `det₄`, `ℓ·c`, `ℓ·per₃` or `per₄` points can be paired —
bracket monomials / fillings (s69's circuit) or monomials of the native
carrier.  The quantities: the `(S₄)^{24}`-invariant Gelfand–Tsetlin state
count `K_{λ₂₄,(4²⁴)} = 70 233 345 083 979 459 756 ≈ 7.0 × 10¹⁹` (the number of
4-strip tableaux of `λ₂₄`, computed here by the strip DP; `7.9 × 10⁷` at
`δ = 12`), and the monomial carrier `N_S = 1.56 × 10¹¹`.  If that expectation
holds the four columns are **not reached**, the step and the quantity are
named, `C₂₄` is delivered, and the session stops on the brief's first stopping
rule.  If a compact evaluation route appears, it is reported as exploratory
(not pre-registered) and any `D > 0` hands over to the verification protocol
before it is reported anywhere.

## 4. Assumptions recorded for the absent s75 interface

1. Pieri embeddings are realised in Young's seminormal form of `S^ν` with the
   strip invariant `c^{ξ/η}` normalised as in §2; a different normalisation
   rescales coordinates channel by channel and conjugates the recoupling
   matrices by the corresponding diagonal — every dimension in §2 is
   independent of it, the *coefficients* of `E_d(ν)` are not.
2. The evaluation map is **not** supplied; §3 states what it would need.
3. The bases `E_d(ν)` are the reduced-row-echelon kernel bases at the house
   prime — deterministic, but not evaluable and not the s74/S1 circuit
   coordinates; a bridge between the two is s77's object.

## 5. Claim labels used in the report

PROVED (a derivation on the page), MEASURED (a number this session computed,
with instrument and prime), RECORDED (a number taken from a banked file),
EXPECTATION (a prior).  Ranks: full rank at one prime proves full rank over
`Q`; a modular drop proves nothing.  `D = mult_pad − mult_det`; only `D > 0`
is an obstruction.

## 6. What counts as a negative

- Question A: none — it is a measurement; an incomplete run is reported with
  the banked shapes.
- Question B: a stalled climb with the peak weighted state count and the level
  reached is a full result; a dimension mismatch at a checked node is a full
  result (it falsifies the operator as implemented, not the recursion).
- Question C: the expected outcome is the negative; it is reported with the
  step and the quantity.
