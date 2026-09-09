# PREREG s75 — the δ = 12 compact control (evaluation half)

Base commit `main = afb8c3319d3d1f3afc3d2578c8cb322f2b8a3b92`. Branch `s75-compact`.
House primes `2147483647`, `2147483629`. No prime below 97 anywhere (|λ₁₂| = 48;
both house primes exceed |λ₂₄| = 96, so `F_p[S_96]` is semisimple by Maschke and
every char-0 statement about `S^λ`, its invariants and the projectors holds mod p).

## Honest ordering note

Discipline asks for pre-registration before measurement. This file is committed
mid-session, after two integrator relays arrived and redirected the task. The
sequence was: (i) the brief was executed as written — I independently rebuilt
the one-block operator and the controls `B₁₂ = 31`, `C₁₂ = 239`; (ii) relay 1
said S3 had done the dimension half and to put the budget on evaluation; (iii)
relay 2 supplied S3's report in the tree and named the concrete task (four
pairing scalars); (iv) the S3 artifacts were located on the laptop
(`gct-gpt/Batch12_Results/S3`) and its **continuation** already carried the
completed bridge. The registered instrument below reflects the task as it
actually stood after the relays: **verify**, not re-derive.

## Question (from the brief, unchanged)

Does S5's one-block recursion produce an invariant source that can be
**evaluated**, at the smallest cell where the answer is known? `λ₁₂ = (17,17,2⁷)`,
`B₁₂ = 31`, `a₁₂ = 2`. Two parts: (1) recover `dim M₁₂ = 2` from the 31-dim
precursor; (2) evaluate the two recovered vectors against determinant points,
reproducing s69's banked `i_det(12) = 0`. Part (2) decides the route.

## Pre-registered controls (from the brief)

- `B₁₂ = 31` (precursor `W₁₂ = (S^{λ₁₂})^{K₁₂}`), three horizontal-4-strip
  predecessors with `a₁₁ = 12, 11, 8`.
- `C₁₂ = 239` — the operator passes through a 239-dimensional space
  `(S^{λ₁₂})^{K'}`, `K' = H₁₀ × S₄ × S₄`; 36 two-strip paths over 23 shapes.
- `a₁₂ = 2`, `i_det(12) = 0`.

## Instrument (as it stands after the relays)

- **Dimension half — independent controls, and consume S3's certified operator.**
  Re-confirm `B₁₂ = 31` and `C₁₂ = 239` from the inherited Weyl engine
  (`a_weyl`, `analysis/wk11_int_bdelta.py`, `results/wk11_int_c12.json`),
  independent of S3. Independently construct the local block-swap recoupling in a
  gl_N Casimir gauge and verify it against GL₂ ground truth and against the
  Littlewood–Richardson eigenvalue multiplicities. Take S3's 239×31 residual
  (rank 29, kernel 2, both primes) as the certified dimension half.
- **Evaluation half — the s75 consumer per the collision rule.** S3's
  continuation computed the four pairing scalars
  `A[α,i] = g_tc · [e_tc] ρ(π_i^{-1}) v_α`, `C = G_M^{-1} A`, and the recursive
  evaluations `E_recursive = C^{-t} E_circuit`. Verify: re-derive `g_tc` and the
  two permutation inversion lengths (expected 579, 640) from the s69 seed; check
  `G_M C = A`, `det C ≠ 0`, `C^t E_recursive = E_circuit`, and the determinant
  minor, at both primes, native and common-source (`A_common = L^t A_native`,
  `C_common = L^{-1} C_native`).
- **Independent circuit reproduction.** Re-evaluate the two s69 seed fillings at
  the seed's own det₄ pencils with the s69 DP evaluator; `i_det = a − rank`.

## Success

Both halves pass: `dim M₁₂ = 2` through the 239-dimensional residual, **and**
`C` nonsingular with the converted vectors reproducing `mult_det = 2`,
`i_det(12) = 0`, without ambient Specht/HWV carrier expansion.

## Stopping rules (neutral wording)

- If a coefficient routine intrinsically requires ambient Specht/HWV carrier
  expansion, name the obstruction and stop (bound: 30 min / 256 MiB for a first
  trial; record the exact unfinished coefficient and its contraction width).
- If the operator returns `dim = 2` but the vectors do not evaluate, that is the
  route's real risk and a complete deliverable — report it plainly.

## What counts as a negative

`C` singular, or a determinant minor zero on the converted vectors while the
circuit minor is nonzero (a genuine failure of the conversion), would be a
negative and would be reported as such.

## Common-field rule

Two modular DAGs select bases independently; common pivots do not prove common
rational entries. Verify the common-source only through S3's explicit `L`
transport (`A_common = L^t A_native`, etc.), not by guessing rational lifts.
