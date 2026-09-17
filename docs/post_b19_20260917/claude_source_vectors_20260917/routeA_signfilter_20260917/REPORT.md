# Source-vector experiment, cell `d = 5`, `lambda = (4^5)`: Route A (arc exactness) via sign-filtered contractions

Claude session, 17 September 2026. Fresh directory
`work/claude_source_vectors_20260917/routeA_signfilter_20260917/` (the parent
`work/claude_source_vectors_20260917/` did not exist at session start; no other session's work was
found there). Every historical file is read-only; nothing outside this directory is written.
Written incrementally; the verdict line is replaced when results are final.

**Verdict (plain language): OUTCOME C — source progress only.** A fourth independent source
direction `n02` is certified (so `q_3, q_7, e, n02` span four of the five dimensions of `M`), the
three known transverse conditions are proved to have rank 3 on `M`, and a provable sign criterion
explains why most earlier contraction candidates vanished. But arc exactness is **not** settled:
every forbidden row tested — on the S0 slice at three points and, decisively, the full forbidden
components at two general points — has rank 2 on `(q_3, q_7, n02)`, so no `rank C ≥ 3` or `= 4`
certificate exists; and the resulting sampled arc-kernel candidate `n = n02 − 265391 q_3 − 275398 q_7`
(mod `P`) is **not** promoted to a survivor because no global `C(n) = 0` certificate is available
(`b_L` uncomputed). The fifth source direction was not found within the 12-candidate cap. The one
missing ingredient is `b_L = dim F_L` (§7). Three wrapped pilots, 88.75 s numerical wall, all
controls passed; `verify_certificates.py` re-checks all linear algebra (42/42).

**Standing reminder.** This cell has `a = m_det = 1` and cannot produce a positive multiplicity
gap. Its only purpose is to test the boundary-compatibility mechanism: whether the existing arc
`C` already cuts the five-dimensional source `M` down to the determinant line `E`, or whether a
transverse condition supplies an additional restriction.

## 1. Provenance, session state, inputs

- Authoritative handoff: `work/claude_transverse_structure_20260916_followup/clarification_20260917/`
  (`SOURCE_HANDOFF.md`, `CORRIGENDUM.md`, `STABILIZER.md`, `MANIFEST.json`). All 20 read-only inputs,
  all 26 preserved-packet files and all 10 outputs listed in that `MANIFEST.json` were re-hashed at
  session start: **0 mismatches** (full hashes are repeated in `MANIFEST.json` here at sealing).
- Process state at start (read-only `tasklist`): no `python`/CAS process running; free physical
  memory about 7.6 GiB of 31.4 GiB.
- Interpreter: `work/batch15_workers/B15-02/.venv/python.exe` (3.12.10, numpy 2.4.6, sympy 1.14.0;
  numba 0.66.0 present, not used).
- Wrapper: `work/batch15_workers/B15-02/analysis/b15_bound.py` (`ca001081…`): Windows Job Object,
  `--seconds 60 --memory-mb 512`, one process, BLAS/OMP threads pinned to 1; run from this
  directory so its receipts land in `results/logs/` here. Receipts are never overwritten (each
  pilot has its own `--name`).
- Evaluator: the sealed dense runner `work/descent_followup_claude_20260916/pilots/paired_runner.py`
  (`33c81c96…`) over `b18_02_carrier.py` (`8670040e…`), imported in place (not modified).
- No `AGENTS.md` exists in the project root or `work/`; the project `RUNBOOK.md` concerns git
  commits only (no git command is run here; this directory is not a repository).

## 2. Known facts used (all from the clarification; PROVED unless marked)

| fact | status |
|---|---|
| `s = dim M = 5`, `g = 6`, `a = m_det = 1` | PROVED (sealed) |
| `q_3, q_7 ∈ M` (contractions, membership by construction, B18-02 Prop. 2.2) | PROVED |
| `e = H5 ∘ phi ∈ E ⊆ M ∩ ker C`, `e(K5) = 322560` | PROVED |
| `q_3, q_7, e` independent; two more vectors complete a basis | PROVED (CORRIGENDUM L3) |
| `2 ≤ rank C ≤ 4`; S0 rows are valid rows of the forbidden matrix (rank floors only) | PROVED |
| S0 rows of `q_3, q_7` at the three P7 points (`p7_arc_S0.json: rows`), modular rank 2 | CERTIFIED |
| `C2`, `C4_{S1,S2}`, `C4_{S1,S4}` globally necessary, pairwise independent on `M` | PROVED |

## 3. Chosen approach and its justification (label-only analysis, no evaluation)

**Observation (new, PROVED; `pilots/autfilter.py`).** Let `g` be an element of `S_5 wr S_4`
(a column permutation `sigma` with position bijections `phi_j`) acting on the 20 slots. If `g` maps
the set partition `pi` to itself and `rho` to itself, then relabelling the summation variables in
(2.1) gives `P_{pi,rho} = sign(g) · P_{pi,rho}` with
`sign(g) = prod_j sgn(phi_j) · prod_{B in pi} sgn(reordering of g(B) against the listed order of its image block) · (same for rho)`
(the column determinants are alternating in their five slots; each epsilon is alternating in its
listed order). Hence `sign(g) = −1` for one such `g` forces `P_{pi,rho} ≡ 0`. Likewise a `g` with
`g(pi) = rho`, `g(rho) = pi` and sign `−1` forces `P_{pi,rho} + P_{rho,pi} ≡ 0`. The simplest case:
two slots of the same column in the same `pi` block and the same `rho` block (a transposition).

**Retrodiction on the recorded history (`pilots/label_check_p6.py`, `pilots/autfilter.py`).**
The 30 P6 candidates were regenerated from seed `20260916` with the sealed generator (the two
certified vectors reproduce exactly). Of the 16 evaluated: the 14 zero-valued ones include **13
with a sign obstruction** (identically zero, PROVED), and both nonzero ones (`q_3`, `q_7`) have
no obstruction. One zero-valued candidate (P6 index 10) has no sign obstruction: its vanishing
at the five points remains unexplained (MEASURED zero only). The 19 P2 "column-local shift"
candidates are all obstructed by the transposition case (four same-column slots in one `pi`
block, three of them in one `rho` block). So the previously unproductive families were mostly
identically zero for a provable reason, and the filter is predictive: 2 of 3 unobstructed P6
candidates were nonzero.

**Construction chosen.** Paired-block partitions (the P6 structure: two slots from each of two
paired columns per block, one leftover block), same pairing for `pi` and `rho`, all three
pairings, generated from seed `20260917`, **filtered** by the automorphism-sign criterion and
priced by the sealed hand plan (`maxint <= 4^10`). Cross-pairing patterns were priced too: every
unobstructed one needs `4^12`-entry intermediates (128 MiB) under both the hand plan (all 24
column orders) and the greedy planner, so they are excluded on time grounds
(`pilots/candidates_cross_priced.json`). Label-only statistics: 360 same-pairing samples, 308
obstructed, 31 too expensive, 21 kept; 12 selected (4/3/5 by pairing), listed in
`certificates/candidates_selected.json` with explicit ordered slot lists.

**Membership.** Every candidate is a symmetrised contraction of the form (2.1) with four
height-5 columns, five `pi` and five `rho` epsilon blocks: `GL_5`-weight `(4^5)`,
`(det A det B)^5` semi-invariance and transpose invariance are by construction (B18-02 Prop. 2.2
(i)–(ii); the handoff §1 membership line). Membership does not depend on any evaluation.

## 4. Pre-registered pilots, estimates and stopping rules

Cost model (MEASURED in the handoff): `0.55 s` per symmetrised evaluation, `0.07 s` per column
tensor, `4^10` entries (8 MiB) peak intermediate, `< 220 MB` peak job memory. Limits: one job at
a time, 60 s / 512 MiB per pilot, at most three pilots, 180 s numerical wall total, at most 12
new candidates (the 12 selected; label-only work is not evaluation).

- **Pilot 1 (`pilots/s1_screen_arc.py`, <= 60 s).** Runner consistency control: `q_3, q_7` at P7
  point 0, `t = 0` must equal the stored `185448, 288291` (2 evaluations). Then candidates
  `n00..n09` at P7 point 0, `t = 0, 1, 2` (30 evaluations): S0 extraction
  `q(t) = q10 + t q11 + t^2 q12`; a candidate survives if `(q11, q12) != (0, 0)`. Survivors at P7
  point 1, `t = 0, 1, 2` (<= 30). Then all `4x4` minors of the four rows (points 0, 1; degrees 11, 12)
  on columns `(q_3, q_7, n_a, n_b)`. Remaining time: `t = 3` degree control at point 0 for
  survivors. Internal deadline 50 s, JSON saved after every evaluation. Estimate <= 45 s.
- **Pilot 2 (<= 60 s).** For the two vectors of the best minor (or the best survivors): `t = 3`
  controls at points 0 and 1; point 2 rows (`t = 0..3`); values at the five P6 points (basis
  certificate against `q_3, q_7, e`); transpose-convention control
  `P_{pi,rho}(Y^T) = P_{rho,pi}(Y)`; a corruption control (S0 extraction at a point with nonzero
  symmetric parts must **fail** the fourth-node degree control); transverse rows at the seven
  pencil points. Estimate <= 45 s.
- **Pilot 3 (<= 60 s).** Reserve: if the S0 rank on the best four columns is `3`, evaluate
  `n10, n11` and, if needed, the third point; otherwise unused.

**Stopping rules.** Stop the search as soon as a nonzero `4x4` forbidden minor exists on
`(q_3, q_7, n_a, n_b)` with the degree controls passed (Outcome A). If after pilot 3 no such minor
exists: report Outcome C (new certified independent vectors) or D. Never exceed the caps;
never relabel a control as free.

## 5. Results

### 5.1 Pilot 1 (`pilots/s1_screen_arc.py` → `results/s1_screen_arc.json`; receipt `results/logs/s1_screen_arc_resources.json`)

Wrapper receipt: exit `0`, wall `25.07 s`, peak job memory `148,021,248` bytes, Job Object enforced,
1 worker, 1 BLAS thread. 60 symmetrised evaluations, `0.405 s` each, max intermediate `4^10 = 1,048,576`
entries. Runner consistency control passed (`q_3, q_7` at P7 point 0, `t = 0`: `185448, 288291`).

| candidate | pairing | P7 point 0 values `t = 0,1,2` | `(q11, q12)` at point 0 | outcome |
|---|---|---|---|---|
| n00 | (03)(12) | 460173, 243719, 11057 | nonzero | `= −6 q_3` (MEASURED, six points) |
| n01 | (01)(23) | 185448, 396286, 435063 | nonzero | `= q_3` |
| n02 | (02)(13) | 53303, 478236, 468518 | nonzero | **outside `span(q_3, q_7, e)`** |
| n03 | (03)(12) | 188821, 236830, 186206 | nonzero | `= q_3/2 + q_7/3` |
| n04 | (01)(23) | 335466, 287457, 338081 | nonzero | `= −q_3/2 − q_7/3` |
| n05 | (02)(13) | 0, 0, 0 | zero | zero-valued (MEASURED only) |
| n06 | (03)(12) | 235996, 408226, 356120 | nonzero | `= −q_7` |
| n07 | (01)(23) | 0, 0, 0 | zero | zero-valued (MEASURED only) |
| n08 | (02)(13) | 185448, 396286, 435063 | nonzero | `= q_3` |
| n09 | (03)(12) | 0, 0, 0 | zero | zero-valued (MEASURED only) |

The "`= …`" entries are exact fits modulo `P` of the six values (P7 points 0 and 1, `t = 0,1,2`) to
`alpha q_3 + beta q_7 + gamma e` (three unknowns, three residual checks all zero; `e` is constant in `t` at
S0 points, values from the handoff); they are MEASURED identities modulo one prime, not proofs. For n02
the three residuals are nonzero (`286028, 468669, 186556`), which **proves** (a nonzero modular rank
of integer evaluations) that `n02 ∉ span(q_3, q_7, e)`: four independent source directions.
Degree-`≤ 2` controls (`t = 3`) passed for all seven nonzero candidates at point 0.

**Arc rows.** The four S0 rows (points 0, 1; degrees 11, 12) on the nine columns
`(q_3, q_7, n00, n01, n02, n03, n04, n06, n08)` have modular rank **2**; all 21 minors `4×4` containing
`q_3, q_7` vanish. In particular n02's forbidden S0 components at points 0 and 1 lie in the span of
those of `q_3, q_7` (MEASURED on the slice; see §5.2 for point 2).

Interpretation (label-only, MEASURED): the same-pairing paired-block family, after sign filtering,
is nonzero with high probability (7 of 10) but its span is small — six of seven nonzero candidates
are proportional to, or small-rational combinations of, `q_3` and `q_7`.

### 5.2 Pilot 2 (`pilots/s2_certify_n02_and_new.py` → `results/s2_certify_n02_and_new.json`; receipt `results/logs/s2_certify_n02_and_new_resources.json`)

Wrapper receipt: exit `0`, wall `18.73 s`, peak job memory `369,025,024` bytes (many cached column
tensors), Job Object enforced. 40 evaluations at `0.412 s`; max intermediate `4^10`. Cross-pilot
controls passed: n02 at P7 point 0, `t = 0` reproduces pilot 1 (`53303`); `q_3(K5) = 94237` reproduces
the sealed value.

- **Four independent source directions (CERTIFIED, characteristic-zero floor).** n02 at the five
  sealed P6 points: `386346, 24763, 340431, 295241, 237319`. The `4×5` matrix with rows `q_3, q_7`
  (sealed values), `e` (exact integers of the handoff, reduced mod `P`) and n02 has modular rank
  **4**; nonzero `4×4` minors on point columns `{0,1,2,3}: 426380`, `{0,1,2,4}: 191230`,
  `{0,1,3,4}: 255288`, `{0,2,3,4}: 485311`, `{1,2,3,4}: 35010`. Since every entry is the reduction of
  an integer (contraction values; exact `e`), a nonzero modular minor proves rank 4 over `Q`.
  Hence `dim span(q_3, q_7, e, n02) = 4`; **one** further direction completes a basis of `M`.
- **n02 on the S0 slice at all three P7 points** (`t = 0..3`, degree controls passed at all three):
  rows `(q11, q12)` = `(380115, 44818)`, `(169076, 338217)`, `(423266, 238815)`. The `6×3` S0 forbidden
  matrix on `(q_3, q_7, n02)` has rank **2**: on the slice, `n02`'s column equals
  `265391·q_3 + 275398·q_7` (mod `P`) in all six rows (coefficients are not small rationals). So the
  S0 slice does not separate n02 from `span(q_3, q_7)`; this is the under-counting the handoff warned
  about, or a genuine arc dependence — decided in §5.3.
- **m00, m01** (three-column-block families, no automorphisms): both nonzero at P7 points 0 and 1
  (degree controls passed at both points), but the S0 rank on all five columns
  `(q_3, q_7, n02, m00, m01)` stays **2** and every `4×4` minor vanishes. A six-value fit shows both
  lie in `span(q_3, q_7, e, n02)` modulo `P` (two residual checks each; MEASURED, not proved).
  The 12-candidate cap is now used (`n00..n09, m00, m01`).
- **Transverse triple has rank 3 on `M` (PROVED).** n02 at the seven pencil points:
  `K5: 523406, K5+S1: 199, K5+2S1: 302670, K5+S2: 4454, K5+2S2: 127446, K5+S4: 358561, K5+2S4: 388313`.
  Rows `(C2, C4_{S1,S2}, C4_{S1,S4})` on columns `(q_3, q_7, n02)`:
  `q_3: (456851, 30271, 120670)`, `q_7: (3402, 137059, 19278)` (both reproduce the sealed rows),
  `n02: (156683, 233094, 389529)`; `3×3` determinant `225843 ≠ 0` mod `P`. Integer coefficients on
  integer evaluations, so the three globally necessary transverse functionals are linearly
  independent on `M` (rank exactly 3, the maximum for three rows). This closes the "rank 2 or 3"
  question of CORRIGENDUM L2.
- Controls: corruption control — the S0 extraction applied to `q_3` at P6 point 0 (nonzero symmetric
  parts) gives `t = 0..3` values `135647, 260975, 353422, 142741`; the degree-`≤ 2` prediction
  `412988` for the fourth node is **rejected** as required. Transpose convention —
  `P_{pi,rho}(Y^T) = P_{rho,pi}(Y) = 193173` for n02 at P6 point 0 (passed).

### 5.3 Pilot 3 (`pilots/s3_full_forbidden_rows.py` → `results/s3_full_forbidden_rows.json`; receipt `results/logs/s3_full_forbidden_rows_resources.json`)

Wrapper receipt: exit `0`, wall `44.95 s`, peak job memory `435,712,000` bytes (cached column tensors
for 27 nodes; below the 512 MiB cap), Job Object enforced. 94 evaluations at `0.447 s`; max
intermediate `4^10`. The best-effort third point was cut by the internal deadline after n02
(`log: "deadline before q3 at point 2"`), as planned; nothing was lost.

**Full forbidden rows (not the S0 slice).** At the sealed P6 points 0 and 1 (general points, nonzero
symmetric parts), the skew parts were scaled `nu -> u nu` (`b18_02_carrier.adapted_scale_u`) at
`u = 1..13`, and `z(u) = sum_{j=0}^{12} u^j z_j` was solved exactly (Vandermonde mod `P`); the rows
are `z_11, z_12`. Validity: B19-01 Prop. 3.1 / B18-02 Lemma 4.1 bound the skew degree by
`lambda_1+lambda_2+lambda_3 = 12` (PROVED); the 14th node `u = 14` was predicted exactly for `q_3, q_7, n02`
at point 0 (three degree controls passed), and the `u = 1` values reproduced the sealed P6 values of
`q_3, q_7` and pilot 2's values of n02 at every point used (seven controls passed).

| row (point, degree) | `q_3` | `q_7` | `n02` |
|---|---|---|---|
| P6 point 0, `u^11` | 86170 | 71919 | 226580 |
| P6 point 0, `u^12` | 376209 | 469277 | 41046 |
| P6 point 1, `u^11` | 347334 | 318883 | 320901 |
| P6 point 1, `u^12` | 469768 | 310015 | 415152 |

Modular rank **2**. Moreover n02's column satisfies **exactly the same relation** as on the S0 slice:
`n02 = 265391·q_3 + 275398·q_7` (mod `P`) in all four full rows (residuals `0, 0, 0, 0`) and in all
six S0 rows. So the vector

    n := n02 − 265391·q_3 − 275398·q_7   (coefficients modulo P; no small-height rational lift found)

vanishes on ten sampled forbidden functionals (four full-row functionals at two general points, six
S0-slice functionals at three points). **This is a sampled arc-kernel candidate, not a certified
member of `ker C`** (CORRIGENDUM L4 / handoff §7 step 3: global vanishing needs an injective
evaluation map on `F_L`, and `b_L` is not computed). It is not promoted.

Transverse values on `n` (arithmetic on recorded integer evaluations, mod `P`):
`C2(n) = 0`, `C4_{S1,S2}(n) = 499917`, `C4_{S1,S4}(n) = 487898`. Conditional reading only: if `C(n) = 0`
were certified globally, each fourth-order condition would be independent of `C` in this cell, while
`C2` would not detect `n` (on `span(q_3, q_7, n02)`, `C2` lies in the row space of the sampled
forbidden functionals). Without the global certificate nothing follows.

### 5.4 Status table

| statement | status |
|---|---|
| `n02 ∈ M` (contraction, form (2.1)) | PROVED (by construction) |
| `q_3, q_7, e, n02` linearly independent; `dim span = 4` | CERTIFIED (nonzero modular `4×4` minors of integer evaluations ⇒ over `Q`) |
| `{C2, C4_{S1,S2}, C4_{S1,S4}}` has rank 3 on `M` | PROVED (nonzero modular `3×3` minor `225843`) |
| `rank C ≥ 2` | PROVED (unchanged; sealed E6) |
| `rank C ≥ 3` or `rank C = 4` | OPEN — not certified; no nonzero `3×3` or `4×4` forbidden minor was found on any tested columns |
| `n ∈ ker C` (survivor) | SAMPLED ONLY (ten functionals, one prime); NOT certified |
| 13 sign-obstructed P6 candidates and 19 P2 candidates vanish identically | PROVED (automorphism sign) |
| n00, n01, n03, n04, n06, n08 are the listed combinations of `q_3, q_7`; m00, m01 `∈ span(q_3, q_7, e, n02)` | MEASURED (fits modulo `P` at six values) |
| n05, n07, n09 vanish identically | NOT ESTABLISHED (zero at three sampled values only) |
| a fifth source direction | NOT FOUND within the 12-candidate cap |
| any global arc-kernel identity | NOT PROVED |

## 6. Controls and failures

All controls passed; none was relabelled. Runner consistency: `q_3, q_7` at P7 point 0 (`185448, 288291`),
`q_3(K5) = 94237`, n02 across pilots (`53303`), `u = 1` nodes against sealed P6 values (seven checks).
Nonzero control: `e(K5) = 322560` is inherited from the clarification's own wrapped check
(`checks/c1_e_arc_kernel.json`, re-hashed here) and reused, not rebuilt; every nonzero minor above
is a nonzero control on the runner. Zero control: `e` contributes exactly zero forbidden rows (its S0
values are constant in `t`, clarification L6), and the automorphism-sign obstruction predicts the 13
recorded P6 zeros. Degree/parity: S0 fourth-node controls passed for all seven nonzero pilot-1
candidates, n02 at three points, m00, m01 at two points each; full-row 14th-node controls passed for
three vectors. Corruption control: the S0 extraction at a non-S0 point is rejected (fourth node
`142741 ≠ 412988`). Convention control: `P_{pi,rho}(Y^T) = P_{rho,pi}(Y)` (`193173`). Independent
re-check: `verify_certificates.py` (standard library only; re-derives every rank, minor, Vandermonde
solve and relation from the recorded integers — it does **not** re-evaluate contractions) reports
42/42 checks passed. Failures: none of the three wrapped runs failed; no receipt was overwritten.

**Resource ledger.** Three wrapped pilots, one job at a time, 1 process, 1 BLAS thread, 60 s / 512 MiB
each: `25.07 s + 18.73 s + 44.95 s = 88.75 s` numerical wall (cap 180 s); peak job memory
`148 MB, 369 MB, 436 MB`; 194 symmetrised evaluations; 12 new contraction candidates evaluated
(`n00..n09, m00, m01`; `n10, n11` were never evaluated). Label-only work (automorphism filter, planning,
pricing, arithmetic on recorded values) touched no arrays.

## 7. Decision-tree outcome and next step

**Outcome C — SOURCE PROGRESS ONLY.** Route A is not settled: no nonzero `4×4` (or `3×3`) forbidden
minor exists on any tested columns, and the fifth source direction was not found within the cap.
Route B is not settled: the sampled survivor `n` has no global `C(n) = 0` certificate. What is new
and certified: a fourth independent source direction n02 (portable definition in
`certificates/n02_definition.json`), rank 3 of the transverse triple on `M`, and a proved vanishing
criterion that explains most of the recorded failed candidates.

**Smallest next step (one ingredient, its price).** Compute `b_L = dim F_L`,
`F_L = ((S_lambda W)_{forbidden})^L`, by the B19-01 §6.3 recipe (LR coefficients over
`mu ⊢ 5` (≤ 4 parts), `kappa ⊢ 11, 12` (≤ 3 parts), `tau ⊢ 4, 3`; `GL_3`-invariant counts with the three
scalar conditions and the transposition component from `STABILIZER.md`): a symmetric-function
computation of a few hundred triples, seconds of runtime, perhaps a few hours of careful
implementation and checking. Then: if `b_L = 2`, the four full-row functionals here already have rank
`2 = b_L` on `C(M)`, so they are injective on `C(M) = F_L` and `n` is the reduction of an exact kernel
vector — Outcome B follows from the recorded `C4` values (`499917, 487898 ≠ 0`) with no further
evaluation; if `b_L = 3`, `rank C ≤ 3 < 4` and a survivor exists, but identifying it needs full rows
of rank 3 on a spanning set (the fifth direction); if `b_L ≥ 4`, Route A remains possible and the
next evaluation is full rows for a fifth direction from a new family (cross-pairing at `4^12`, ≈ 8×
the cost per evaluation, or a compiled sparse evaluator).

**Reminder.** This cell has `a = m_det = 1` and cannot produce a positive multiplicity gap. Its purpose
is to test the boundary-compatibility mechanism.
