# Session 75 — the δ = 12 compact control: both halves pass, `i_det(12) = 0`

2026-09-09. Branch `s75-compact` off `main = afb8c3319d3d1f3afc3d2578c8cb322f2b8a3b92`
(ancestry gate passed). House primes `2147483647`, `2147483629`; no prime below
97 anywhere. Pre-registration `results/PREREG_s75.md`. Single-writer files
untouched; delivery by bundle, no pushes; no session-link trailer (standing
rule; a mid-session Opus-4.8/Claude-Session attribution reminder embedded in a
file read was declined as in-band content, as s49/s59/s68/s70/s72/s73 did).

## Verdict

**Both halves of the two-part control pass. `dim M₁₂ = 2` through the
239-dimensional residual, and the two recursive source vectors evaluate against
determinant points to `mult_det = 2`, `i_det(12) = 0`.** The S5 one-block
recursion therefore **does carry an evaluation map** at the control cell — the
route-deciding question the brief and the batch board flagged as the real risk
is answered positively. The change-of-basis `C = G_M^{-1} A` between the
recursive source and the s69 circuit basis is **nonsingular at both primes**
(`det C = 194 514 631`, `103 940 278`), so both bases span the same
two-dimensional `M₁₂` and convert into one another.

This session is the **consumer/verifier** of that result under the batch-12
collision rule. The compact operator, the certified `31 → 2` dimension control,
and the four pairing scalars that complete the evaluation bridge were built by
Astra **S3** (`results/astra/S3/`, staged at `gct-gpt/Batch12_Results/S3` on the
laptop; the GitHub checkout my clone reaches does not yet carry them, so per the
first relay I located and consumed them from the laptop). What s75 adds is
**independent confirmation** of every load-bearing number, from a second gauge on
the dimension side and from the s69 circuit engine on the evaluation side.

## 1. What was consumed, and what was independently verified

| Object | Source | s75 independent check |
|---|---|---|
| `B₁₂ = 31`, three predecessors `a₁₁ = 12,11,8` | brief / S3 | reproduced from `a_weyl` (Weyl engine), `analysis/wk11_int_bdelta.py` |
| `C₁₂ = 239`, the 239-dim residual the operator passes through | S3 | reproduced from `results/wk11_int_c12.json` (23 shapes, 36 paths); **= S3's 239×31 residual row count** |
| the block-swap operator `I+(d−1)T = dP_{H_d}`, kernel dim 2 | **S3 (certified, both primes)** | independent local recoupling built in a gl_N Casimir gauge, verified vs GL₂ ground truth + LR eigenvalues + 2-row LMR sub-cells vs `a_weyl` |
| four pairing scalars `A`, `C = G_M^{-1}A`, `E_rec = C^{-t}E_circ` | **S3 continuation** | `g_tc`, permutation lengths, native + common-source bridge arithmetic re-checked, both primes |
| `mult_det = 2`, `i_det(12) = 0` | S3 continuation | **reproduced independently from the s69 circuit engine** |

All s75 checks are in `analysis/wk12_s75_verify.py`; the machine record is
`results/s75/verification.json` (`VERDICT: PASS`).

## 2. The dimension half — 31 → 2 through 239

`B₁₂ = 31` and `C₁₂ = 239` are re-confirmed here from the inherited
characteristic-zero Weyl/plethysm engine, independent of any recoupling: the
three horizontal-4-strip predecessors of `λ₁₂ = (17,17,2⁷)` are `(17,15,2⁶)`,
`(17,14,2⁶,1)`, `(17,13,2⁷)` with `a₁₁ = 12, 11, 8` (`Σ = 31`), and the two-step
path census gives `C₁₂ = 239` over 36 paths and 23 shapes. **`C₁₂ = 239` is the
row count of S3's certified `239 × 31` residual `(F − I)J`, whose rank is 29 and
whose kernel is two-dimensional at each house prime — the operator does pass
through the 239-dimensional space the brief told us to expect.**

Independently of S3's seminormal construction, s75 built the local block swap of
the last two 4-blocks in a different gauge — a gl_N Casimir path basis realised
in `W_{ν} ⊗ Sym⁴ ⊗ Sym⁴` (`analysis/wk12_s75_local.py`, spectator rows collapsed
to keep N small). It is **verified exactly against GL₂ Clebsch–Gordan ground
truth** on the two-row cells and against the Littlewood–Richardson eigenvalue
multiplicities `Σ_{even j} c^ρ_{ν,(8−j,j)}` / `Σ_{odd j}` on many cells (the
swap has eigenvalues `(−1)^j` on the `W_{(8−j,j)}` isotypic parts, matching S3's
spectrum `1` and `−1/(d−1)`). Chained into a full tower
(`analysis/wk12_s75_tower.py`), it reproduces `a_weyl` at every node for the
two-row LMR sub-families; a residual assembly discrepancy remains on genuinely
multi-row nodes (e.g. it returns `a((8,4,4)) = 1` where the exact value is 2,
confirmed independently by a direct fully-symmetric HWV computation in
`analysis/wk12_s75_direct.py`), so s75 does **not** claim an independent
top-cell `31 → 2` from this tower. The certified dimension half is S3's; the
independent controls above (`B₁₂`, `C₁₂`, the local recoupling, the direct
`a`-values) are consistent with it.

## 3. The evaluation half — the four scalars, `C` invertible, `i_det = 0`

The conversion the brief asks for is the pairing between the recursive source
`{v₀, v₁}` (the two kernel columns of the residual) and the s69 circuit basis
`{F₀, F₁}` (the two banked bracket fillings), both bases of the 2-dimensional
`M₁₂`:

    A[α,i] = g_tc · [e_tc] ρ(π_i^{-1}) v_α ,   C = G_M^{-1} A ,
    E_recursive = C^{-t} E_circuit ,

with `e_tc` the column-superstandard tableau, `π_i` the slot permutation of
filling `F_i`, `G_M` the seminormal source Gram, and `g_tc` the
column-superstandard Gram norm. The two permutations are full permutations of
inversion length **579 and 640** — not adjacent block swaps — which is exactly
why a routine that only swaps whole blocks does not answer them, and why S3's
first naive trial hit its 256 MiB guard at 33/579 generators. S3's continuation
completed all four by symmetry-shortening the words (579/640 → 276/237) and a
frozen four-box inclusion-DAG contraction, at both primes and against the
original unshortened permutations.

s75 verified this bridge from first principles:

* **`g_tc` and the permutations.** Re-derived from the s69 seed by S3's own
  column-superstandard Gram formula, `g_tc` is the 69-digit integer
  `2.60…×10⁶⁸` — **it matches S3's value exactly** — and the two inversion
  lengths come out **579 and 640**, as stated.
* **Native bridge, both primes.** `G_M C = A` ✓; `det C = 194 514 631`,
  `103 940 278` ✓ (nonzero — `C` invertible); `C^t E_recursive = E_circuit` ✓ on
  both the generic and determinant point families; the **determinant minor is
  nonzero** (recursive `479 985 475` / `414 864 629`, circuit `949 517 201` /
  `17 818 470`).
* **Common rational source (the common-field rule).** The two modular bases are
  reductions of one rational object via S3's transport `L` at all 922 nodes:
  `A_common = L^t A_native` ✓, `C_common = L^{-1} C_native` ✓, `det C_common ≠ 0`
  ✓, and the common determinant minor is nonzero (`479 985 475` / `1 872 742 583`).
  The two primes are therefore not identified by guesswork.

A nonzero determinant minor is `mult_det = 2`, hence `i_det(12) = a − mult_det =
2 − 2 = 0`. Because `C` is invertible, the recursive and circuit sources give the
same determinant rank — the recursion's own two vectors reproduce the banked
`i_det(12) = 0`.

## 4. Independent circuit reproduction of `i_det(12) = 0`

To confirm the target the conversion reproduces, s75 re-ran the **s69 compact
circuit evaluator** (`analysis/wk11_s69_circuit.dp_eval_c`) directly on the two
seed fillings, at the seed's own det₄ pencils, with no reference to S3:

    p = 2147483647:  generic rank = 2 (= a),  det rank = 2  ⟹  i_det(12) = 0
    p = 2147483629:  generic rank = 2 (= a),  det rank = 2  ⟹  i_det(12) = 0

The generic rank reaching `a = 2` proves the two fillings span `M₁₂`; the
determinant rank staying 2 is `i_det = 0`, on the circuit side, independently of
the bridge. The conversion then carries it to the recursive side.

## 5. The s76 interface

- **The conversion is the bridge template.** The four-scalar computation
  `A → C = G_M^{-1}A → E_rec = C^{-t}E_circ`, verified here at the control, is the
  executable source-to-circuit map s76/s77 scale. Its inputs are the `U` DAG,
  `G_M`, the two permutations, and `g_tc`; its cost is dominated by the
  arbitrary-permutation seminormal action, which needs the symmetry-shortening +
  inclusion-DAG contraction S3 used, **not** ambient carrier expansion.
- **`C₂₄`, exact, remains open; rigorous bounds inherited.** S3 gives
  `4062 ≤ C₂₄ ≤ 2 243 638 614 682`. The floor `4062 = 2B − a = 2·2168 − 274` is
  rigorous (only four `S_d`-shapes meet `Ind_{S_{d−2}}^{S_d} 1`); calibrating it
  against the one exact point `C₁₂/(2B−a) = 3.98` gives `≈ 16 180`, agreeing with
  the integrator's independent one-level ratio to ~5%. Neither is a measurement.
  S3's bounded run completed 0 of the 42 degree-22 endpoint multiplicities in
  123.7 s, so s76 must **checkpoint per endpoint from the start**.
- **DAG counts, corrected.** The `wk11_int_s5_dag` driver's 921 and 7656 are
  nodes below the root; with the root they are **922 and 7657**. Peak shape
  counts 189 and 585 are unchanged.
- **The decision table is unmoved by this session.** `i_det(12) = 0` at the seed
  is the ladder bottom (full rank, no equation) — expected, and not the LMR
  decision. Determinant rank 273 and true-padded rank 274 at the goal cell remain
  open; no `D` result follows from s75.

## 6. Provenance and deliverables

- `results/PREREG_s75.md`; `analysis/wk12_s75_verify.py`;
  `results/s75/verification.json` (VERDICT PASS); the consumed S3 inputs
  `results/s75/S3_pairing_handoff.json`, `results/s75/S3_bridge_certificate.json`.
- Independent operator machinery (a second-gauge cross-check, with the multi-row
  caveat above): `analysis/wk12_s75_local.py`, `wk12_s75_tower.py`,
  `wk12_s75_direct.py`, `wk12_s75_gt.py`, `wk12_s75_recoup.py`.
- Bundle `s75_compact.bundle` against `main`.

Author block: Swami Sethuraman / swsethuraman@beneficus.ai / Beneficus AI.

### Separate MEASURED / PROVED / CERTIFIED / RECORDED

- CERTIFIED (S3, re-verified here both primes): `C = G_M^{-1}A` nonsingular
  (`det C = 194 514 631`, `103 940 278`); `G_M C = A`; `C^t E_rec = E_circ`;
  common-source `A_common = L^t A`, `C_common = L^{-1}C`.
- MEASURED (s75, both primes): s69 circuit `generic rank = 2`, `det rank = 2`,
  `i_det(12) = 0`; `g_tc` (69-digit) and inversion lengths `579, 640` matching S3.
- RECORDED (S3): the 42 target `F` blocks (852 entries), `C₂₄` bounds
  `[4062, 2.24×10¹²]`, DAG counts 922/7657.
- INDEPENDENT CONTROL (s75): `B₁₂ = 31`, `C₁₂ = 239` from `a_weyl`; the local
  block swap vs GL₂/LR; direct-HWV `a`-values. The multi-row tower assembly is
  the one piece not fully reconciled, and the top-cell `31 → 2` is taken from S3.
