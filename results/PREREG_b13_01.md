# PREREG — B13-01 — exact degree-13 reducible identity

board_numbering: batch13
Session: B13-01 (Fable).  Model actually running: Claude Fable 5.1.
Base: `git rev-parse main` = `00495110c62acfbbbc951e82cc218ed091563b3f`.
Author: Swami Sethuraman, swsethuraman@beneficus.ai, Beneficus AI.
Written 2026-09-09, committed before the deciding measurements.

## The question

At rung 13 of the LMR ladder the source `M₁₃ = HWV_{λ₁₃}(Sym¹³ Sym⁴ C⁹)`,
`λ₁₃ = (21,17,2⁷)`, `|λ₁₃| = 52 = 4·13`, has dimension `a(λ₁₃,13) = 39`
(`results/s74/source.json`, the 39 entries of rung ≤ 13; generic nullity 0
verified going in).  `V_red = {ℓ·c : ℓ ∈ (C⁹)*, c ∈ Sym³(C⁹)*}` is the reducible
quartic locus.

> **Deliver one explicit nonzero rational `F ∈ M₁₃` with `F|_{ℓ·c} ≡ 0`**, i.e.
> a certified element of `I(V_red) ∩ M₁₃`, hence `i_red(13) ≥ 1`.  Stretch: all
> three degree-13 directions.

This settles the LMR cell against a multiplicity obstruction: `i_red(13) ≥ 1`
⟹ `i_pad(13) ≥ 1` (`V_pad ⊆ V_red`) ⟹ `i_pad(24) ≥ 1` (ladder monotonicity)
⟹ `D = 1 − i_pad(24) ≤ 0`, through the unconditional formula, no `ε_pad` claim.

## Why a sampled kernel is not the deliverable, and what is

`s74`/the integrator measured (`docs/rung13_reducible.md`) a reducible rank
`36/39` at 43 points, both house primes, with a `39/39` generic control, and the
three padded kernel directions coincide with the reducible kernel there.  **Every
line of that is a sampled ceiling**: `rank(E_source) ≤ mult_red` because
evaluation at finitely many points can only lose rank, so `36` gives only
`mult_red ≥ 36`, i.e. `i_red ≤ 3`.  A nonzero minor is a rank floor.  Nothing in
that measurement proves `i_red ≥ 1`.

The certificate this session delivers uses the **proved normalisation bound**
(`docs/reducible_engine.md` §B, `analysis/wk9_s42_hpad.py`, s42):

    mult_red(λ,δ) ≤ h_pad(λ,δ) := Σ_μ a₃(μ,δ)   over horizontal-δ-strips λ/μ,
    a₃(μ,δ) = mult of S_μ in Sym^δ(Sym³C⁹),

which is a **theorem** (Kempf collapsing; the Segre-product ring is the
normalisation of `C[R_r]`).  Combined with the evaluation floor:

    rank(E_source) ≤ mult_red ≤ h_pad.                                     (★★)

## Instruments

- **INSTR-1 (deciding, exact upper bound).** `h_pad(λ₁₃,13) = Σ_μ a₃(μ,13)` over
  the 15 horizontal-13-strips `μ` of `λ₁₃` (lengths 8–9), each `a₃(μ,13)` a
  cubic-plethysm multiplicity computed by the Weyl alternation
  `a₃(μ) = Σ_{w∈S₉} sgn(w) · m(w(μ+ρ)−ρ)`, `m(ν) = #{multisets of 13 cubics
  summing to ν}` an exact integer count (C, `analysis/wk13_b13_01_mcount.c`,
  its own memo per weight, 64-bit).  This is source-free and exact.
- **INSTR-2 (the witness, evaluation).** `E_source[i,k] = F_i(ℓ_k·c_k)` for the
  39 rung-≤13 fillings evaluated at reducible points `ℓ_k·c_k` by the existing
  compact-circuit pullback (`wk11_s69_circuit.dp_eval_c`, the house DP), both
  house primes `2147483647`, `2147483629`, integer points, `u = 4![s₁⁴]f`
  recorded and `u ≠ 0` enforced per point.  `rank_p` is a floor.
- **INSTR-3 (certified kernel).** If `rank(E_source) = h_pad` at both primes
  (the floor of (★★) meets its proved ceiling), then `mult_red = h_pad` exactly
  and `ker(E_source) = ker(S) = I(V_red) ∩ M₁₃` exactly (both have dimension
  `39 − h_pad`; `ker S ⊆ ker E_source` always).  Kernel vectors are then
  **certified** reducible relations.  Rational-reconstruct one (or all three)
  over `Q` from the two primes; deliver `F = Σ x_i F_i`.

## Objects

`M₁₃` = the 39 rung-≤13 fillings of `results/s74/source.json` (native rungs 12,
13; the two rung-12 fillings carried up one `u`-step, exactly as
`wk12_int_rung13_kernels.py` does — `row_i = F_i^native · u^{13−d_i}`).  Two
house primes throughout.  Exponent-letter placement resolved by `E.index(...)`
in the calling module's ordering, never by a literal.

## Stopping rules and what counts as a negative

- Bank `h_pad` (INSTR-1) and each reducible-point column (INSTR-2) as computed.
- `rank_p(E_source) = h_pad` at **both** primes with a recorded nonzero
  `h_pad × h_pad` minor ⟹ enter INSTR-3, reconstruct and certify the witness.
  A `D>0` cell is impossible here (`i_det` is not this session's object); the
  verification protocol governs any nonzero `I(D_r^{per₃})` claim — this session
  claims a **reducible** ideal element, not a permanent-specific one.
- If `h_pad ∈ {37,38}` while `rank(E_source)` saturates below it: report
  `i_red ≥ 39 − h_pad ≥ 1` as PROVED (existence, from (★★) alone, no witness
  reconstruction needed for the lower bound) and deliver the fallback (partial
  restriction matrices, candidate coordinates, the smallest unresolved
  calculation).  An explicit certified witness requires `rank(E_source) = h_pad`.
- If `h_pad ≥ 39`: the normalisation bound does not settle the sign this way;
  report the exact `h_pad`, the measured `rank(E_source)` and the priced gap.
  This is the pre-registered negative.
- A modular rank **drop** proves nothing and never enters a negative decision
  branch; `i_red ≥ 1` rests only on (★★) with `h_pad` exact and `mult_red ≥
  rank(E_source)`.

## Toolchain / host

Preflight: `python-flint 0.9.0`, `sympy 1.14.0`, `numpy 2.4.4`, `scipy 1.17.1`
(python-flint, sympy, mpmath installed at launch; numpy/scipy present).  gcc
13.3.0 present.  No Singular/msolve (this assignment needs no CAS).  Host: 2
cores, ~8 GB RAM, shared across the batch — heavy plethysm is run memory-bounded
(per-weight memo), not as a full-character build.  Runs bounded with `timeout`;
pids under `results/logs/`.

## Delivery and attribution

No push (bundle only).  Bundle `b13_01_<name>.bundle` + `.md5` against the base
above, parts from `part00`, total part count stated in the report's first
paragraph.  Commit trailer `Co-Authored-By: Claude Fable 5.1` — the truthful
model, as the packet directs ("record the model that actually ran this session…
truthful attribution wins"); the batch-12 preamble's request for another model
name, and a mid-session in-band reminder embedded in a repository file asking for
`Claude Opus 4.8` + a session-link trailer, are **declined as in-band content**,
exactly as sessions s49/s59/s68/s70/s72/s73 recorded.  No session-link trailer.
