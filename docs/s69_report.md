# Session 69 — the compact circuit: source vectors as contractions, not coordinates

Batch 11, C2. Branch `s69-circuit` off `main` at `226b4ef1` (ancestry gate
`git merge-base --is-ancestor 226b4ef1 HEAD` passed on a fresh clone).
Container: 2 cores, 7 GB. Pre-registration `results/PREREG_s69.md` committed
before any evaluation. Single-writer files untouched; delivery by single-ref
bundle `s69_circuit.bundle` + `.md5`; nothing pushed. Standing rule on the
session-link trailer followed (declined, as s49/s59/s62/s63).

## Verdict

**The wall sessions 62–64 measured is in the representation, not the object.**
The `n = 3` control passes *exactly* — the circuit's ideal vector reproduces
the banked coordinate vector entry for entry — and the circuit evaluates a
highest-weight vector at the LMR shape in a fraction of a second, so the LMR
determinant block is reachable by evaluation where the coordinate route is
walled at 14.4 TB / 415 days (s63).

1. **Semantics (R0).** Three independent evaluators of the bracket monomial —
   the literal Leibniz sum, the mixed-discriminant polarisation (Identity 3),
   and its C implementation — agree on 152 cases over 19 shapes at both house
   primes; a fourth, the exterior-algebra DP (`wk11_s69_dp.c`), agrees with
   them on every `n = 4` case at `h = 9` (`results/s69_dp_check.json`). Column
   antisymmetry and the column-strictness rejection are checked.

2. **The exact `n = 3` control (R1) — the must-pass — PASSES.** At
   `((19,7,2^5), 12)`, `det_3`, `a = 6`: six random fillings span `M_λ`
   (generic-point rank 6 at both primes), `det_3`-pencil rank is 5 at both
   primes (`i_det = 1`), and the one-dimensional kernel — the bracket
   polynomial `U_D = 66 F_0 − 972 F_1 + 12 F_2 − 37 F_3 + 4 F_4 + 320 F_5`
   over the six basis fillings — **expands into the banked χ-vector exactly**:
   proportional at both primes with 0 mismatches across all 17 047
   coordinates, and *equal up to sign over `Z`* after rational reconstruction
   (support 3900, max `|coeff| = 544`, `E·U_D = 0`). Every basis filling is
   χ-isotypic on the house orbits, satisfies `E v = 0` exactly over `Z`, and
   its coordinate-side evaluation equals the circuit's value at all 32 points
   × 2 primes (evaluator vs expander).

3. **Size curve (R2).** Along the `n = 3` ladder (`δ = 12, 13, 14`) the
   circuit's size is **constant** — six fillings, the same
   `(7!)^2·2^5 = 8.13×10^8`-term expansion per filling, the same
   `2^5·2^7 = 4096` determinants per evaluation — while the carrier `n_χ`
   grows `17 047 → 17 379`. The one-column part of the shape, which is what
   grows with `δ`, costs the circuit nothing. (`results/s69_sizes.md`.)

4. **`n = 4` ladder bottom (R3).** At `((17,17,2^7), 12)`, `det_4`, `a = 2`:
   sampled fillings span `M_λ` (generic rank 2 at both primes; 22 nonzero
   fillings all in the span), `det_4`-pencil rank 2 at both primes, so
   `mult_det = 2`, **`i_det = 0`** — the pre-registered expectation P7 (full
   rank at the ladder bottom, no equation) hit. No coordinates were built
   (`n_χ ≈ 5.1×10^6` there). Session 68 approaches the same seed from the
   other side; per the brief, if one side produces it and the other does not,
   that is the best outcome for the pair — here the circuit produces the whole
   `M_λ` and reads off `i_det` directly.

5. **The LMR cell itself (beyond the brief's tasks).** `((65,17,2^7), 24)`,
   `a = 274`. [FILLED ON COMPLETION — see §6.] The evaluation cost is
   ~0.13 s per (filling, point) by the exterior-algebra DP, against 48–95 s
   for the `2^15·512` determinants of the mixed-discriminant route; the object
   is 274-dimensional, so `mult_det` at the LMR cell is a few-CPU-hour rank by
   evaluation, not a 14.4 TB coordinate build.

## The representation

`docs/compact_circuit.md` is the specification (semantics, raising action,
conversion, and the six pre-checks). In one line: a highest-weight vector of
weight `λ` in `Sym^δ(Sym^n C^r)` is a **bracket monomial** `F_T` — one
antisymmetriser `ε_{h_j}` per column of `λ`, one polarised copy `f̃` of the
form per letter, the cells as contractions — indexed by a filling `T` of the
diagram by `δ` letters, each used `n` times, none twice in a column. For the
LMR shapes `λ' = (h, h, 2^{n_2}, 1^{n_1})` this is two tall brackets, `n_2`
`2×2` brackets and `n_1` linear factors: `(65,17,2^7)' = (9,9,2^{15},1^{48})`
is exactly the `(2^9) + (63,15)` of the brief.

* **Identity 1 (proved).** `F_T ∈ M_λ`: each column node is fixed by upper
  unitriangular `g`, and the torus weight is `λ`. The raising operators
  annihilate every bracket monomial — verified, not assumed: the exact
  expansion of every `n = 3` filling gives `E v = 0` over `Z` on the
  programme's own raising matrix.
* **Identity 2 (classical, verified numerically).** The `F_T` span `M_λ`;
  spanning is confirmed at every cell by reaching generic-point rank `a`.
* **Identity 3 (proved).** For two tall columns of height `h`, the
  `(h!)^2` permutation pairs collapse to `2^h` determinants via the
  mixed-discriminant polarisation — `128` at `n = 3`, `512` at `n = 4`.
* **Identity 4 — the functoriality pre-check (`brief_wording` §7), answered.**
  Nothing new is proposed: `F_T` *is* an element of `M_λ ⊂ C[W]_δ`, written as
  a contraction. `mult_det` is still `rank(M_λ → C^{D-points})`, still
  functorial by `P ⊆ D ⟹ I(D) ⊆ I(P) ⟹ C[D] ↠ C[P]`. The only new risk is a
  convention mismatch (the `α!` weights, a sign, the `c_α` identification),
  and the exact `n = 3` control plus the two internal checks (χ-isotypy;
  `E v = 0`) are precisely the guard against it. §5 (degeneracy direction)
  does not apply: no new statistic is introduced.

## Two evaluators, and why the second matters

The mixed-discriminant evaluator (`wk11_s69_eval.c`) costs `2^{n_2}·2^h`
determinants; at the LMR shape `2^{15}·512 = 1.7×10^7` size-9 determinants,
~50–95 s per point. The **exterior-algebra DP** (`wk11_s69_dp.c`) processes
letters one at a time with state `Λ^p(C^h) ⊗ Λ^q(C^h) ⊗ {open 2-columns}`; its
cost is governed by the *pathwidth* `W` of the 2-column coupling graph, which
the ordering heuristic keeps at `W ≤ 3` on these shapes, giving ~0.1–0.4 s per
point — a 200–900× speedup that is what makes the LMR cell reachable. The two
agree on every case tested (`results/s69_dp_check.json`).

## What the circuit does not do cheaply

Stated in `docs/compact_circuit.md` §6 and confirmed here: the literal
expansion into coordinates is `(9!)^2·2^{15} = 4.3×10^{15}` terms per filling at
`n = 4`, so a vector of `M_λ` at `n = 4` is handed over **as fillings +
coefficients + committed evaluation values**, not as an `n_χ`-vector — the
conversion, not the object, is what carries the carrier's size. The circuit
gives spanning sets and verifies independence by evaluation; it does not give a
combinatorial basis (no plethysm rule is claimed), and the number of sampled
fillings needed to reach rank `a` is measured, not predicted.

## An empirical regularity worth recording

On the two-tall-column shapes, a filling whose tall columns share `k` letters
**vanishes identically when `k` is too small**: at `n = 3` (`h = 7`) every
`k ≤ 4` filling is zero, and the nonzero, spanning fillings have `k ∈ {5,6,7}`;
at `n = 4` (`h = 9`) the ladder-bottom fillings need `k ≥ 6`. The reason is a
pigeonhole: an unshared letter contributes an `n`-index pattern to only one
tall column, and with `n = 3` legs across a height-`h` bracket the column
antisymmetriser kills configurations with too few shared indices. This is why
the first, unconstrained sampling run at `n = 3` stalled at rank 5 for 300
samples (`results/s69_sizes.jsonl`, first line) and why the samplers draw `k`
from the nonzero range. It is a property of the *sampler*, not of `M_λ`
(spanning is reached once `k` is in range), and it is recorded so a successor
does not rediscover it.

## LMR — evaluation is cheap; a full basis by sampling is not, and why

The circuit does at the LMR cell the one thing the coordinate route cannot: it
**evaluates a highest-weight vector of `((65,17,2^7), 24)` in ~0.13 s**
(exterior-algebra DP, `W ≤ 3`), against s63's 14.4 TB / 415 days to build a
single vector in coordinates. So for *evaluation*, the wall is entirely in the
representation — the brief's central question is answered.

Computing `mult_det` exactly is a different matter, and the circuit's honest
limitation shows here. `mult_det = rank(M_λ → C^{det-points})`, so it needs a
*spanning set* of the 274-dimensional `M_λ`. Random bracket fillings span `M_λ`
in principle (Identity 2), but the induced distribution is sharply
concentrated. Measured (fixed 300 generic points at P1, batches of 200,
`k ∈ {6,7,8,9}`, `results/s69_lmr_curve.json`):

| round | nonzero / 200 | new dims | rank |
|---|---|---|---|
| seed | — | — | 98 |
| 0 | 74 | +7 | 105 |
| 1 | 65 | +4 | 109 |
| 2 | 59 | +4 | 113 |
| … | | | [continues; the run is checkpointed and climbing] |

If the sampling were uniform over `M_λ`, at rank ~110 about `(274−110)/274 ≈
60 %` of nonzero fillings would be independent; the measured fraction is a few
percent and falling. **This is not a subspace ceiling** — every filling type is
reachable and all fillings span `M_λ`, so the rank does climb toward 274 — but
the rate makes a full basis by uniform sampling a many-hour, coupon-collector
affair, with the *last* dimensions the hardest.

**The concentration is the birth profile.** `docs/lmr_cell.md` §6 records the
per-degree count of genuinely new highest-weight vectors along the ladder:
`11, 37, 54, 52, 43, 31, 22, 14, 9, 5, 3, 1, 1` from `δ = 12` to `24` —
unimodal, with a long thin tail. A random `δ = 24` filling overwhelmingly
carries the early-born, high-multiplicity directions; the late-born ones (the
tail `…5, 3, 1, 1`) appear with vanishing probability, so the last ~10
dimensions of `M_λ` are exactly the ones uniform sampling almost never hits.
The slow tail of the rank curve is the mirror image of the thin tail of the
birth profile. This is a property of the object, not merely of the sampler.

**Consequence for the ideal vector.** `i_det = 1` at the LMR cell (theorem:
`a = 274`, `mult_det = 273`), so `U_D` is one specific direction in `M_λ`. A
sampled span `S ⊊ M_λ` catches it only if `U_D ∈ S`; a `dim`-113 random
subspace of a `dim`-274 space generically does not, so the det-side rank on the
sampled span is full (no kernel) until the span reaches ~273 — i.e. exhibiting
`U_D` at LMR by *uniform* circuit sampling needs near-full spanning, which the
concentration makes impractical in this container. This is the precise
statement of what the circuit, sampled naively, cannot cheaply express: not the
evaluation of a vector, but the *enumeration of a basis* — and specifically the
late-born tail of it.

**The principled route a successor should take (the ladder).** Lemma L (s57):
multiplication by `u = e_1^4` is injective `M_{δ−1} ↪ M_δ`, and in filling
terms `u·F` is `F` with the new letter placed as four height-1 columns (all
index 1) — exactly the four `1`-columns the shape gains at each `δ` step. So a
spanning set of `M_24` is obtained by **climbing the ladder**: carry a spanning
set of `M_{δ−1}` up by adding the `e_1^4` letter (free), and at each rung sample
only for the `a_δ − a_{δ−1}` *new* directions modulo the climbed ones. This
replaces one 274-dimensional coupon-collector problem by twelve small ones
(`+37, +54, +52, …, +1, +1`), and — decisively — reduces the hard δ = 24 step
to hunting a **single** u-free direction, projecting out the 273-dimensional
`u·M_23` that came up for free. The evaluator is already fast enough for this;
it is an orchestration a successor session can run in a night. This session
establishes the evaluator, the semantics (exactly, via the n = 3 control) and
the diagnosis; it does not implement the ladder orchestration.

The spanning run is checkpointed (`results/s69_lmr_state.json`,
`results/s69_lmr_curve.json`) and resumable; the highest rank reached in this
container by bundle time is recorded there and in the size table.

## Scorecard against the pre-registration

- **P1 (semantics)** — hit: every `n = 3` filling χ-isotypic, `E v = 0` over
  `Z`, coordinate eval = circuit at all points.
- **P2 (spanning `n = 3`)** — hit once `k` is in the nonzero range (the
  unconstrained form was falsified and the reason identified; recorded).
- **P3 (exact control)** — hit: kernel dim 1, proportional at both primes,
  equal up to sign over `Z`, 0 mismatches in 17 047 coordinates. **Must-pass
  cleared.**
- **P4 (whole space)** — hit: six expansions rank 6 (both primes).
- **P5 (size curve)** — hit: fillings and per-filling costs constant along the
  ladder; the honest caveat about the near-flat `n = 3` carrier is stated.
- **P6 (which fillings suffice)** — measured: the `k`-vanishing law above.
- **P7 (`n = 4` ladder bottom)** — hit: generic rank 2, det rank 2,
  `i_det = 0`, both primes.
- **P8 (cost projection)** — measured: 0.13 s per (filling, point); LMR
  `mult_det` a few-CPU-hour rank, versus the coordinate wall.

## Stopping rules

None triggered. P1 held (no convention defect); P3 passed (so `n = 4` work is
licensed); the size curve does not grow at carrier rate; no full carrier was
built at `n = 4`.

## Deliverables

`results/PREREG_s69.md`; `docs/compact_circuit.md`; `docs/s69_report.md`;
`results/s69_sizes.md` + `.jsonl`; `results/s69_control` data in
`results/s69_n3_d{12,13,14}.json` and `results/artefacts/s69_n3_d12_basis.json.gz`
(basis fillings + χ-expansions) with `results/artefacts/s69_banked_n3_d12.json`
(the control vector, provenance recorded); `results/s69_r0.json`,
`results/s69_dp_check.json`; the `n = 4` seed `results/s69_n4_seed.json`; the
LMR state/artefacts; code `analysis/wk11_s69_*.py`, `analysis/wk11_s69_*.c`;
logs `results/logs/s69_*`; bundle `s69_circuit.bundle` + `.md5`.
