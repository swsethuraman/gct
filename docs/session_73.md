# Session 73 — the decision table, and the `D`-ladder at `n = 3` (batch 11, C6)

2026-09-08.  Branch `s73-dladder` off `main` at `226b4ef1`; pre-registration
`results/PREREG_s73.md` (`bc7a3b0`) before any build; report
`docs/s73_report.md`; bundle `s73_decision.bundle` + `.md5`.  Mode B (the
default); the Mode A gate at 04:30 UTC found no LMR source (§ Mode A of the
report).  House wording; no session-link trailer (standing rule).

## What was asked

Three rungs of the `n = 3` `D`-ladder `λ_δ = (3δ − 17, 7, 2^5)` (the unpadded
`det_3` vs `per_3` comparison on 7-pencils), with `U_D = ker T_det`,
`U_P = ker T_per` in the same `χ`-coordinates, `dim(U_D ∩ U_P)`, the
three-outcome table, `sparse_nullity` certificates for every full-rank claim,
exhibited kernel vectors for every positive nullity, and an answer to whether
the programme's first `D = +1` (at `δ = 12`) survives transport up the ladder.

## What was found

1. **The answer is a theorem.**  The `a`-ladder is `0, 2, 4, 5` at
   `δ = 8..11` and **flat at 6 for every `δ ≥ 12`** (two independent
   plethysm engines to `δ = 20`, the house engine to 40, and the stable value
   `a_∞((7,2^5)) = 6` by a from-scratch DP; Proposition S gives equality with
   `a_∞` from `δ = 17`).  Lemma L (s57; the proof is degree-generic and holds
   verbatim at `n = 3` with `c = c_{(3,0,…,0)}`) makes `a`, `mult_X`, `i_X`
   non-decreasing with `a = mult_X + i_X`, so a flat `a` freezes both:
   `i_det(δ) = 1`, `i_per(δ) = 0`, **`D(δ) = +1` for all `δ ≥ 12`**, and
   `D = 0` at `9, 10, 11`.  The brief's first case (`1, 1, 1, …`, a persistent
   obstruction family) holds, with exactly one ideal highest-weight vector on
   the determinant side at every rung — the LMR vector, born at 12 and
   transported — and none on the permanent side, ever.  The prediction was
   pre-registered before the rungs were measured.
2. **The rungs agree with it at every point.**  `δ = 12, 13, 14, 15, 16`
   directly: `nullity[E; ev_det] = 1`, `nullity[E; ev_per] = 0` at both house
   primes on fresh pre-registered evaluation families; `δ = 9, 10, 11` both
   sides full rank at both primes.  `dim(U_D ∩ U_P) = 0` everywhere;
   orientation `U_D ⊄ U_P`, `U_P = 0`.
3. **One line, on every engine.**  The `δ = 12` integer kernel vector
   (support 3900 of `n_χ = 17 047`, largest coefficient 544) equals session
   62's exhibited vector up to sign; the full-`E` solve gives the explicit
   basis `M_12` (nullity `6 = a`), whose rank on the 729 `u`-free columns is
   `1 = a(12) − a(11)` (so `dim J(M_11) = 5`, birth space of dimension 1) and
   the LMR vector has a nonzero `u`-free part — born at 12, not transported.
   Above 12: `J(M_12) = M_13`, and `J(v_12) = ±v_13`, `J(v_13) = ±v_14`, …
   **exactly over `Z`** — the direct Wiedemann measurement on an independently
   built cell and the transport of the previous rung's vector coincide.
4. **Certificates (46, all PASS).**  For every rung: `sparse_nullity` records for both sides
   at both primes (the closing Berlekamp–Massey nonsingularity record with the
   pencils as substitution data) and, at the positive rungs, the LMR line as
   an **integer `hwv` certificate** (240 510 terms, 1.45 MB) — annihilated by
   the raising operators over `Z`, vanishing at recorded and fresh `det_3`
   pencils, **nonvanishing at recorded and fresh `per_3` pencils** and generic
   cubics — verified from scratch by `tools/verify`.  All pass.
5. **`i_pad`** on the same source is `a` at every rung (the padded `n = 3`
   model is concise in 5 variables, `ℓ(λ) = 7`: washout, proved), as the
   stock-take's §6 says the padded `n = 3` cell must be.

## Corrections and flags for the integrator

- The batch-11 inputs named in the brief (preamble, plan, `s65_prompt`,
  `stocktake_batch10`, P0-A code/results, s63's `n3control`, the P0-A
  permanent certificates, the `n ∈ {3,4}` verifier) exist neither on GitHub
  `main` nor in the laptop's `work/`, and the s63 bundle is not in
  `Projects/gct`; the session ran from the brief with the s62/s64/s66
  bundles.  `tools/verify` was extended here (`n ∈ {3,4}`, `permanent_pencil`
  family, `sparse_nullity` kind, `FORMAT.md`) and needs reconciling with the
  integrator's version — at most a family rename.
- The brief's framing "nobody knows which" of the three ladder outcomes holds:
  the flatness of the `a`-ladder from the LMR degree decides it, and this is
  exactly the s57 regularity (the LMR cell is the first stable cell of its
  ladder).  At `n = 4` the same argument makes the LMR ladder's `D` equal to
  `D(24)` at every `δ ≥ 24`: the `n = 4` question is one cell, not a ladder.
- The laptop link dropped mid-session; the bundle was delivered to the
  conversation, and the laptop copy is pending.
