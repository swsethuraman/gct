# Final bounded arc diagnostic: one new-point pilot seeking a nonzero 3×3 full-forbidden minor on `(q_3, q_7, n02)`

Claude session, 17 September 2026. Fresh directory
`work/claude_source_vectors_20260917/final_arc_diagnostic/`. Inherited sealed packets re-hashed at start
and at sealing (routeA 31 outputs, arc_target 13, direct_arc 23, inherited inputs 46, Astra outputs: 0
mismatches, no unlisted files); nothing outside this directory is written. Written incrementally.

## Verdict

**Outcome B — no nonzero `3×3` minor found; `rank(C|_U) ∈ {2, 3}` remains unresolved.** One wrapped
pilot (68 runner evaluations, 35.0 s wall, exit 0, peak 233 MB) produced four new full forbidden rows at
the sealed general points P6 point 2 and P6 point 3 (skew degrees 11 and 12). All four satisfy the
recorded relation `n02 ≡ 265391 q_3 + 275398 q_7 (mod 524287)` exactly (residuals 0); the combined
14-row matrix has rank 2 and all 364 `3×3` minors vanish modulo `P`; the seven degree-12 rows have rank
1 with the constant ratios `101007, 295818`. These are additional sampled zeros and prove nothing about a
ceiling; they are not promoted. Transverse independence from the full arc is not proved; no explicit
rational survivor exists; `rank C ∈ {2, 3, 4}` as before. The diagnostic is paused after this attempt;
the consolidated handoff is `CURRENT_DIAGNOSTIC_STATE.md`.

**Standing reminder.** `a = m_det = 1`: no positive multiplicity gap is possible in this cell.

## 1. Theorem target (unchanged from the pre-registration)

`U = span_Q(q_3, q_7, n02)`, `dim U = 3` (certified). `C(z) = (z^{[12]}, z^{[11]})` (skew degrees 12, 11;
B18-02 Lemma 4.1, B19-01 Prop. 3.1). A row is the functional `z ↦ z^{[n]}(Y)` at a point `Y`; entries on
`(q_3, q_7, n02)` are integers reduced mod `P = 524287`. A nonzero `3×3` minor would prove
`rank_Q(C|_U) = 3` and `rank C ≥ 3` (Outcome A); zero minors prove no ceiling (Outcome B). Ten inherited
rows have rank 2 with the constant relation above (degree-12 rows rank 1); any new row violating the
relation would give a nonzero minor with two inherited rows.

## 2. Astra's exclusion, incorporated

`work/astra_gkz_degenerations_20260917/REPORT.md` (Outcome C, theorem proved globally; manifest and output
hashes verified): in the fixed adapted decomposition `(a, r, c, S, v)`, every universal forbidden-weight
test from block-scalar scalings, and every exact-exponent-support test, factors through the existing
`C`; for any stack `N` of such tests `rank(C,T,N) = rank(C,T)`; the nine normal-fan classes classify
initial forms of this restricted family only. Accordingly no five-block weights were enumerated, no
face degeneration sought, no alternative endpoint assumed independent. General-point evaluations of the
existing `C` (this pilot) are a rank certificate attempt for `C` itself and are unaffected by the
theorem, which settles neither `rank(C|_U)`, nor the mixed-pairing identity, nor transverse
independence.

## 3. Points, extraction, conventions (as executed)

- Evaluator: sealed `paired_runner.py` (`33c81c96…`) over `b18_02_carrier.py` (`8670040e…`), hand-plan
  orders `(0,1,2,3)` for `q_3` and `(0,2,1,3)` for `q_7`, `n02` (both orientations), values mod `P`;
  wrapper `b15_bound.py`, 60 s / 512 MiB, one process, one BLAS thread; receipt
  `results/logs/f1_new_point_minor_resources.json`.
- Extraction: skew part `ν → uν` (`adapted_scale_u`), nodes `u = 1..13`, Vandermonde for
  `z(u) = Σ_{j≤12} u^j z_j` (degree bound `#v ≤ 12`, PROVED), rows `z_11, z_12`; node `u = 14` as degree
  control; no degree-11-only shortcut.
- Points: sealed P6 points 2 and 3 (`p6_basis.json: points_entries`, integer entries in `[−3, 3]`,
  nonzero symmetric parts, off the S0 slice). Heuristic motivation only: they are generic seeded points
  with certified `u = 1` values for all three vectors. At point 2 the `n02` row was reused from the
  sealed parent (`s3_full_forbidden_rows.json: n02_pt2_coeffs_u0_to_u12`, `z_11 = 240230`, `z_12 = 285304`)
  and only `q_3, q_7` were evaluated. P6 point 4 was skipped by the pre-registered rule (17.4 s left < 21 s).
- Column order of every row: `(q_3, q_7, n02)`; all 13 node values per vector/point are recorded in
  `results/f1_new_point_minor.json: values`.

## 4. Price versus measurement

Planned ≈ 34 s (68 evaluations at 0.447 s, 27 tensors, startup); measured 34.6 s inside the script
(`0.48 s` per evaluation), 35.0 s wrapper wall, peak job memory 233 MB.

## 5. Results

New rows (mod `P`):

| row | `q_3` | `q_7` | `n02` | relation residual |
|---|---|---|---|---|
| full P6 point 2, degree 11 | 40035 | 209168 | 240230 (sealed parent) | 0 |
| full P6 point 2, degree 12 | 501035 | 190996 | 285304 (sealed parent) | 0 |
| full P6 point 3, degree 11 | 93310 | 521790 | 182077 | 0 |
| full P6 point 3, degree 12 | 100242 | 113150 | 239523 | 0 |

Combined with the ten inherited rows (six S0 rows at P7 points 0–2, four full rows at P6 points 0–1):
rank 2; all `3×3` minors zero; degree-12 rows (seven) rank 1 with ratios `q_7 : q_3 = 101007`,
`n02 : q_3 = 295818` at every point. **No Outcome-A certificate.** The sampled relation now holds on
14 functionals at 5 general and 3 S0 points, all modulo one prime. This remains evidence only.

## 6. Controls (all passed; replayed by `verify_minors.py`, 36/36)

Preserved nonzero evaluations: `u = 1` nodes equal the sealed values for `q_3, q_7` at point 2
(`336756, 275526`) and for all three at point 3 (`260012, 317892, 295241`). Inherited nonzero `2×2`
minors recomputed: `104967`, `171205`. Degree assumption: `u = 14` predicted exactly for `q_3, q_7, n02`
at point 3 (`417014, 97357, 177928`). Corrupted extraction: perturbing node `u = 3` by `+1` breaks the
`u = 14` prediction for each vector. Corrupted relation: `(α+1, β)` fails on the rows. `e ∈ ker C` is the
inherited global proof (B19-01 §5, restriction of a global polynomial), not a sampled zero.

## 7. Outcome and closure

Outcome B. Proved intervals unchanged: `rank(C|_U) ∈ {2, 3}`, `rank C ∈ {2, 3, 4}`, `rank T = 3` on `M`
and on `U`. No further sampling round is scheduled; no source search, no `F''`, no symbolic
mixed-pairing implementation, no five-block tests were run. Consolidated handoff:
`CURRENT_DIAGNOSTIC_STATE.md`. Resources: one wrapped pilot (35.0 s of the 60 s cap), no unwrapped
computation.
