# Session 74 — the LMR source by births, then the decision

Branch `s74-births` off `main` at `afb8c3319d3d1f3afc3d2578c8cb322f2b8a3b92`;
pre-registration `results/PREREG_s74.md` (commit `3edd772`, dated addenda
`5caa2af`) written before any birth was drawn.  Bundle `s74_births.bundle` +
`.md5`.  Labels throughout: **PROVED** / **CERTIFIED** (a nonzero minor over
`Z`, sound over `Q`) / **MEASURED** (a mod-`p` value, or a rank that is only a
floor) / **ADOPTED** / **RECORDED**.

## 0. Verdict

On the complete, certified 274-vector source, at both house primes:

    rank T_det = 273        CERTIFIED: a nonzero 273×273 minor on the transported δ=23
                            rows (rank_Q ≥ 273) against LMR's rank T_det ≤ 273 (ADOPTED)
                            ⟹ i_det(23) = 0, ε_det = 1, i_det(24) = 1
    rank T_pad ≥ 269        CERTIFIED: a nonzero 269×269 minor at true padded points
    D = rank T_pad − 273 ∈ [−4, +1]      CERTIFIED (the two lines above)
    rank T_pad = 269, i_pad = 5, D = −4  MEASURED: the same value at two primes, at two
                            point families (boxes 30 and 1000) and by two evaluation paths;
                            the five padded kernel vectors are retained as candidate
                            relations, not promoted
    y ∈ I(Det) ∖ I(Pad)     CERTIFIED: the LMR equation y — the unique element of M₂₄
                            vanishing on determinant pencils, exact by LMR + the floor —
                            is nonzero at 282/282 integer padded points at both primes

with `dim(U_D ∩ U_P) = 0`, `U_D ⊄ U_P`, `U_P ⊄ U_D` (mod both primes).  Per
the integrator's instruction (03:05 UTC) and note 3 §8, the negative
decision-table branch is **not entered**: `D = −4` is the observed shortfall,
`D ∈ [−4, +1]` is what is certified, and certifying any `D ≤ 0` would need a
characteristic-zero membership proof for at least one of the five padded
candidates.  What is finished is the determinant column, exactly at 273, and
the source: 274 bracket fillings, every rung's birth quotient certified at
both primes, assembled under one declared row system, generic rank 274.

What the measured value would mean if it stood: `D < 0` is the direction
containment permits, so the multiplicity statistic in weight `(65,17,2⁷)`
would not see the known separation `ℓ·per₃ ∉ \overline{GL·det₄}` — the LMR
equation is there (`i_det = 1`) and the padded side would have more equations
(five), none of them the LMR line.  What stands regardless of the five
candidates: the LMR equation itself separates the padded permanent, with an
evaluation certificate rather than LMR's dual-variety argument.

## 1. Objects and conventions

`n = 4`, `r = 9`, the goal cell `λ = (65, 17, 2⁷)`, `δ = 24`, `a = 274`; the
ladder `λ_δ = (4δ − 31, 17, 2⁷)`, `δ = 12 … 24`, shapes `λ'_δ = (9, 9, 2¹⁵,
1^{4δ−48})`.  `u = c_{(4,0,…,0)}`, resolved as `exps(4,9).index(...)` = 494 in
the `wk8_s30_core` ordering.  `M_δ = HWV_{λ_δ}(Sym^δ Sym⁴ C⁹)`.  Fillings and
their bracket monomials `F_T` are s69's (`docs/compact_circuit.md`); the
`a`-ladder `2, 39, 93, 145, 188, 219, 241, 255, 264, 269, 272, 273, 274` and
the birth profile `b_δ = 2, 37, 54, 52, 43, 31, 22, 14, 9, 5, 3, 1, 1` are
ADOPTED (s57/s63).  Point families, all integer substitution data in the
verifier's four kinds: `det_pencil`, `padded_permanent` (`restrict(PAD34)` =
`x₀(s)·per₃(X(s))` on a generic 9-plane — the true padded permanent, not
`ℓ·c`), `reducible`, `permanent_pencil`, plus a generic integer quartic for the
assembly check; `K = a + 8 = 282` per family, entries in `[−30, 30]`, seeds
`20260974 / 20261974 / 20262974 / 20263974 / 20264974 + j`.  Every record was
rebuilt by `tools/verify/forms.py` (which imports nothing from `analysis/`) and
agreed with my coefficient vectors.  Both house primes throughout.

**The declared row system** (PREREG §3b).  The source is the list of 274
*literal transported fillings* `T_i^↑` (native `T_i` of birth rung `d_i`, plus
`24 − d_i` letters each on four one-columns).  For every column and both primes

    row_i(f) = F_{T_i^↑}(f) = F_{T_i}(f) · msym_u(f)^{24−d_i},   msym_u = 4!·[s₁⁴]f.

Checked from the other side: for 24 rows spanning all rungs, 3 points of each
of 3 families, both primes — 432 direct DP evaluations of the climbed fillings
equal the scaled native values, 432/432 (`results/s74/row_system_check.json`).
S1's "`u`-normalised" convention is `literal / 24^{24−d_i}` per row and is
recorded in `source.json` for conversion; kernel vectors below are on the
literal rows.

## 2. What was pre-registered, and the two dated addenda

PREREG §1–8 as committed.  Addenda (§9), each committed before the
measurements it governs: (i) the stall bandit and the first-point short-circuit
in the birth streams (23:15 UTC), after rung 13 showed the house sampler's
`k = 5` draws vanish identically and its last directions are rare; (ii) the
integrator's sequencing relay (note 3, 23:30 UTC): the determinant column is
evaluated rung by rung as a running lower bound and stops at 273; the padded
column is prioritised.  A second relay (S4, 01:00 UTC) arrived after the full
padded column was already running and is addressed in §5.

## 3. The births — every rung of the ladder filled at both primes

Instrument `analysis/wk12_s74_births.py`.  At rung `d`: draw column-strict
fillings of `λ'_d`; reject syntactically any with a pure-`u` letter (four legs
on one-columns: `F_T = 4!·u·F_deleted`, an identity); evaluate survivors at
`K_d = b_d + 8` generic points with `u = 0` mod `P1`; keep a filling iff it
raises the rank; stop at `b_d`.  **Certificate per rung**: the kept `b_d × K_d`
matrix has rank `b_d` at `P1` (a nonzero `b_d × b_d` minor is recorded, column
set and determinant), and the same fillings at `K_d` fresh `u = 0` points mod
`P2` again have rank `b_d` (second minor recorded).  Because the restricted
polynomials have integer coefficients and the points are integer points, rank
`b_d` at one prime proves the `b_d` classes `Q`-independent in `ρ_d(M_d)`, and
S1's theorem (`M_d/uM_{d−1} ≅ ρ_d(M_d)`, dimension `b_d`, PROVED) makes them a
basis of the birth quotient.  Files `results/s74/births_d13..23.json`
(fillings, both point seeds, both matrices, both minors, the draw record).

| rung | `b_d` | draws | past filter | zero rows | draws to last keep | stalled at | bandit draws / hits | wall (s) | `P1` minor det | `P2` rank |
|---|---|---|---|---|---|---|---|---|---|---|
| 13 | 37 | 1500 | 1500 | 317 | 1499 | draw 276 at 34/37 | 1223 / 3 | 3999 | 422436750 | 37 |
| 14 | 54 | 246 | 246 | 76 | 243 | — | — | 618 | 812286308 | 54 |
| 15 | 52 | 172 | 168 | 57 | 167 | — | — | 795 | 1417421658 | 52 |
| 16 | 43 | 194 | 186 | 80 | 193 | draw 168 at 42/43 | 23 / 1 | 532 | 949079092 | 43 |
| 17 | 31 | 109 | 90 | 48 | 107 | — | — | 383 | 529725090 | 31 |
| 18 | 22 | 96 | 84 | 43 | 90 | — | — | 215 | 1352898995 | 22 |
| 19 | 14 | 70 | 48 | 31 | 68 | — | — | 11 | 56982487 | 14 |
| 20 | 9 | 51 | 30 | — | 41 | — | — | 31 | 2068777070 | 9 |
| 21 | 5 | 133 | 48 | — | 131 | — | — | 30 | 953552015 | 5 |
| 22 | 3 | 142 | 42 | — | 142 | — | — | 18 | 1990675105 | 3 |
| 23 | 1 | 37 | 12 | — | 33 | — | — | 4 | 1080273749 | 1 |

(`draws` includes the batch overshoot past the last keep; "draws to last keep"
is the sequential count.  Rung 13's first 1 500 s ran the s69 evaluator; the
wall times of 14–23 are on the compact one, §7.  Rungs 20–23 were run under the
probe's exact seeds and reproduce the integrator's streams — 33/142/131/41
draws, 10/42/47/26 survivors, identical fillings where the probe saved them.)

Rung 12 is the s69 seed pair (generic rank 2 and `u = 0` rank 2 at both
primes); rung 24 is `F_{T₅₇}` (`u = 0` rank 1, nonzero at 9/9 points at both
primes, on my own points).  S1's ten vectors replayed: its two seeds are s69's,
its eight `δ = 13` classes have `u = 0` rank 8 at both primes, and they were
admitted as the first eight rung-13 candidates through the same test.

**What the streams taught.**  (a) `k = 5` fillings (five letters shared by the
two tall columns) vanish identically at rung 13 — 0 hits in 27 draws, 4/4 zero
at generic points — extending S1's proved `k < 5` vanishing by one; about half
the `k = 6` draws vanish too.  (b) Rung 13 has a real tail: 34/37 after 270
draws, 35 at 354, 36 at 701, 37 at 1499, and the last two directions were found
by the house sampler at `k = 8, 9` while the ones-first and mutation samplers
found none (the bandit's 1 223 draws: 3 hits).  s69's "+1 per 150–200 samples"
was optimistic for the last one.  (c) Rungs 14–19 filled without a tail
(hit rate 20–30% of draws throughout), and rung 16's single stall resolved in
23 bandit draws.  The pure-`u` filter removes 0–35% of draws at the middle
rungs and 70% at the top; identically-zero survivors (the first-point
short-circuit) are another 25–45%.  Total discovery wall: 1.9 h, of which 1.1 h
is rung 13.

## 4. The source, assembled

`results/s74/source.json`: 274 entries in rung order — seeds (2), rungs 13–23
(37+54+52+43+31+22+14+9+5+3+1 = 271), `F_{T₅₇}` (1) — each with its native
filling, its literal transported filling, the exponent `24 − d_i`, the
`(4!)^{24−d_i}` conversion scalar, and the birth file it came from.  By S1's
theorem and injectivity of `u·` the transported births are a basis of `M₂₄`
(PROVED given the per-rung certificates); the generic column confirms it on
the assembled rows (§5).

## 5. The evaluation columns and the decision quantities

Instrument `analysis/wk12_s74_columns.py` (native values, per-row checkpoints)
and `wk12_s74_decide.py` (assembly under the row system, python-flint ranks
and left kernels).  `K = 282` points per family; both primes; the same 274
rows for every column.  Two padded points (`j = 243, 263`) were skipped because
their `s₁⁴` coefficient vanishes (recorded); no other family skipped a point.

| column | `P1` rank / nullity | `P2` rank / nullity | on the δ=23 rows (273) | status |
|---|---|---|---|---|
| generic (assembly check) | 274 / 0 | 274 / 0 | 273 / 0 | CERTIFIED: the 274 transported births are a basis of `M₂₄` |
| `det₄` pencils | 273 / 1 | 273 / 1 | 273 / 0 | CERTIFIED floor 273 (minor); = 273 with LMR; `i_det(23) = 0`, `i_det(24) = 1` |
| true padded `ℓ·per₃` | 269 / 5 | 269 / 5 | 268 / 5 | CERTIFIED floor 269 (minor); 269 MEASURED at two primes and at fresh box-1000 points |
| reducible `ℓ·c` | 269 / 5 | 269 / 5 | 268 / 5 | floor 269 (a mod-`p` rank is a floor over `Q`); 269 MEASURED at two primes; `U_R = U_P` at both primes (the five padded relations are reducible-locus relations) |
| unpadded `per₄` | 274 / 0 | 274 / 0 | 273 / 0 | CERTIFIED `i_per4 = 0`: no equation of the unpadded `per₄` 9-pencil variety in this weight |

Kernels (mod `p`, on the literal rows): `U_D` one-dimensional at both primes,
with nonzero coefficient on `F_{T₅₇}` as `ε_det = 1` forces; `U_P`
five-dimensional at both primes; `dim(U_D ∩ U_P) = 0`, `U_D ⊄ U_P`, `U_P ⊄ U_D`
(`results/s74/decision_<p>.json`, `results/certs/s74_kernel_*.json`).
`U_R ⊆ U_P` with `dim U_R = dim U_P = 5`, so `U_R = U_P` at both primes:
`mult_pad = mult_red = 269` — the padded permanent inherits no equation in
this weight beyond those of the reducible locus `ℓ·c` (the `r ≤ 5` identity
`mult_pad = mult_red` of s64 recurs at `r = 9`, mod both primes).  `U_R ⊄ U_D`.
The five padded/reducible kernel vectors (echelon form) are supported exactly
on the rows of rungs `≤ 13` (three of them) and `≤ 14` (two), at both primes:
they lie in `u¹¹·M₁₃` and `u¹⁰·M₁₄` respectively, so the candidates are (mod
`p`) transported from the 39- and 93-dimensional cells `(21,17,2⁷)_{13}` and
`(25,17,2⁷)_{14}`, where an exact membership proof would live, not at 274.

**Fresh points, literal path.**  `analysis/wk12_s74_verify.py` re-evaluates the
*literal* climbed fillings directly (no native value, no transport scalar) at
`K = 294` fresh points with entries in `[−1000, 1000]` (seeds `+100000`):
padded rank `269/274`, `268/273` on the δ=23 rows at `P1` — AGREE;
determinant rank `273/274`, `273/273` on the δ=23 rows at `P1` — AGREE; padded rank `269/274`, `268/273` on the δ=23 rows at `P2` — AGREE (`results/s74/verify_<p>.json`).

**The D-ladder** (`results/s74/ladder_ranks.json`, both primes identical).
Restricting the banked columns to the rows of rung `≤ d` reads `mult_X(d)`
(multiplication by `u^{24−d}` is injective on functions of an irreducible
variety with `u ∉ I_X`):

    δ        12  13  14  15  16  17  18  19  20  21  22  23  24
    a         2  39  93 145 188 219 241 255 264 269 272 273 274
    i_det     0   0   0   0   0   0   0   0   0   0   0   0   1
    i_pad     0   3   5   5   5   5   5   5   5   5   5   5   5
    i_red     0   3   5   5   5   5   5   5   5   5   5   5   5
    i_per4    0   0   0   0   0   0   0   0   0   0   0   0   0
    D         0  −3  −5  −5  −5  −5  −5  −5  −5  −5  −5  −5  −4     (MEASURED, mod P1 and P2;
                                                                     every sub-source has generic nullity 0)

The LMR equation is born exactly at `δ = 24`; the padded ideal — which
coincides with the reducible ideal at every rung — enters the ladder at
`δ = 13` (three directions in a 39-dimensional space) and `δ = 14` (two more)
and is pure transport from there on; the unpadded `per₄` pencils have no
equation anywhere on the ladder — consistent with the
inequality `i_X(d) − i_X(d−1) ≤ b_d` for prime ideals not containing `u`.
`i_pad(23) = 5`, `ε_pad = 0`: `F_{T₅₇}`'s padded evaluation escapes the old
padded image (rank 268 → 269).

**S4's relay.**  The full padded column was already running when the relay
arrived, so the pivot-block route was not needed.  S4's certificate was
cross-checked on the compact evaluator: all 144 entries of each 12-minor and
both determinants (`1086325324` at `P1`, `2097075880` at `P2`) reproduce
(`results/s74/s4_crosscheck.json`) — a third evaluator agreeing with S4's own
and the integrator's s69-DP re-derivation.  `269 ≥ 12`, as it must be.

## 6. What is certified, what is measured, and the decision-table reading

Per the integrator's instruction (03:05 UTC) and note 3 §8's asymmetry:

- **CERTIFIED** (`results/s74/certified.json`, both primes): a nonzero
  `273×273` minor of the transported δ=23 rows at determinant points (`P1`
  det `895171876`, `P2` det `394515299`) — `rank_Q T_det ≥ 273`; with LMR's
  `rank T_det ≤ 273` (ADOPTED), `rank T_det = 273`, `i_det(24) = 1`,
  `i_det(23) = 0`, `ε_det = 1`.  A nonzero `269×269` padded minor (`P1`
  `1236200953`, `P2` `1999071517`) — `rank_Q T_pad ≥ 269`.  Hence
  **`D ∈ [−4, +1]`**.  The generic rank 274 — the source is a basis.
- **MEASURED** (not a theorem; the negative branch is *not* entered):
  `rank T_pad = 269` at two primes and two point families, `i_pad = 5`,
  `D = −4`; the five padded kernel vectors are retained mod both primes as
  candidate relations for exact identity verification, each nonzero at all
  282 determinant points.  Certifying `D = −4` would need `i_pad(24) ≥ 5`
  over `Q`, a membership proof for those five candidates; certifying even
  `D ≤ 0` needs one of them.
- **The LMR line separates true padding — CERTIFIED.**  Since `rank_Q T_det =
  273` exactly, `ker T_det` over `Q` is one line `⟨y⟩` and `y` is the LMR
  equation of this weight restricted to the 9-pencil variety (it is the only
  element of `M₂₄` vanishing on the determinant pencils).  The mod-`p`
  point-evaluation matrix has nullity exactly 1 and `y mod p` lies in its
  kernel, so `k_p = c_p·y (mod p)` with `c_p ≠ 0`; therefore for every integer
  point `f`, `y(f) ≡ c_p · (k_p · row(f)) (mod p)`, and a nonzero residue
  certifies `y(f) ≠ 0` over `Q`.  The residues are nonzero at **282/282 true
  padded points at both primes**: `y ∈ I(Det) ∖ I(Pad)`.  Exact determinant
  membership of `y` comes from LMR's theorem and the floor, not from
  evaluation; no rational reconstruction is involved.  The same residues are nonzero at 282/282 reducible, 282/282 unpadded-`per₄`
and 282/282 generic points at both primes: `y ∉ I(Red)`, `y ∉ I(Per₄)`.
- **Why the kernel line is not reconstructed over `Q`.**  Its coordinates on
  the random-filling basis are ratios of `273×273` minors of a matrix whose
  entries are integers near `10^170` (degree-24 evaluations at integer
  points); rational reconstruction from the two primes (62 bits) fails on 94
  of 274 coordinates and returns numerators at the bound on the rest, and the
  Hadamard bound puts the true height around `10^{47000}` — thousands of
  primes, each a full column.  The exact statements above do not need it,
  and the mod-`p` reductions of the line are exhibited at both primes.

Reading of the table: the determinant column is finished (row "det 273");
the padded column is a certified floor with a stable measured value below
274, so the cell is reported as *rank floors plus the observed shortfall*
(note 3 §8), with `D ≤ +1` certified and `D = −4` measured.  Nothing here is
a `D > 0` claim, so the `D > 0` protocol was not invoked.

## 7. The instruments, and one engineering result

`wk12_s74_births.py` (streams: pure-`u` filter, first-point short-circuit,
`u = 0` rank test, stall bandit, exact resume), `wk12_s74_sampler.py`
(ones-first and mutation samplers), `wk12_s74_columns.py` (points, native
values, checkpoints, the row-system identity), `wk12_s74_decide.py`,
`wk12_s74_certify.py`, `wk12_s74_certs.py`, `wk12_s74_verify.py`,
`wk12_s74_driver.py` (the rung-by-rung determinant accumulation of note 3,
pausing the streams by their recorded process group), and

**`wk12_s74_dpc.c` — the s69 Grassmann DP with compact state.**  The original
keeps its state over all `(mask₁, mask₂, open)`, `2⁹·2⁹·2^W` entries (16 MB at
`W = 3`), and clears it at every letter, although after `t` letters only masks
of the current popcounts are populated (`≤ 126·126·8` entries, 1 MB).  Measured
on this box: `0.128 s` per evaluation alone and `0.244 s` each for two
concurrent evaluations — memory-bandwidth bound, no gain from the second core,
and the reason the first column pass ran at 39 s per row.  Ranking masks
within their popcount class and storing only the populated block gives
`0.051 s` (rung-13 filling) / `0.016 s` (rung-24 filling) per evaluation,
unchanged with two workers: 2.5–8× per evaluation and a clean 2× from the
cores.  Validated entry for entry against `dp_eval_c` on 50 random (filling,
point) pairs across rungs 12–24 at both primes, `u = 0` points included
(`wk12_s74_dp.py validate`); the verifier keeps the original evaluator behind
`S74_VERIFY_S69_DP=1`, and `--spot` checks the s69 DP against the
mixed-discriminant evaluator (Identity 3, `wk11_s69_eval.c`) on literal δ=24 fillings at fresh determinant
points: 8/8 agreements at both primes, `0.05–0.16 s` against `47 s` per
evaluation (`results/s74/spot_evaluators.json`).  A full `274 × 282` column costs
20–45 min instead of hours; the whole session's evaluation budget was roughly
20 CPU-hours.

## 8. Certificates and the verifier

`results/certs/s74_65_17_2x7_d24_{det_pencil,padded_permanent}_{P1,P2}.json`,
`sparse_nullity` in the session-67 spelling (`field`, top-level `nullity`,
`recipe`, `provenance`, `basis: null`), points as substitution data, the
nonzero minor in `recipe.nonzero_minor`, and the mod-`p` kernels exhibited in
companion files through `kernel_certificates` (the χ-expansion of a kernel
vector at this cell is out of range, `N_S = 1.56·10¹¹`; the companions carry
the coefficient vectors on the circuit source instead).  All pass
`tools/verify`'s strict schema check.  **They are RECORDED-class by
construction**: the verifier re-derives a `sparse_nullity` by enumerating the
weight space and rebuilding `[E; ev]`, which at `N_S = 156 438 903 314` is not
reachable (and its enumeration runs before the `VERIFY_MAX_NS` guard, so the
integrator should not point it at these files without a size guard).  The
independent re-derivation is `analysis/wk12_s74_verify.py`: fresh points,
literal fillings, a recount of `N_S` by an exact multiset DP (`results/s74/ns_count.json`):
`N_S(λ₂₃) = 156 419 279 221` and `N_S(λ₂₄) = 156 438 903 314`, both equal to
`lmr_cell.md` §6 — an independent confirmation of the sizes the certificates
carry.  The verifier's `forms.py` was
used to confirm every point record.  Eight certificates in all: the four varieties at both primes (`reducible`
269 / nullity 5 with its kernel companion, `permanent_pencil` 274 / nullity 0 —
the latter a sound `i_per4 = 0` over `Q` in the format's own semantics, if the
verifier could reach the cell).

## 9. Honest boundary

- `rank T_det ≤ 273` is LMR's theorem (`docs/lmr_cell.md`), ADOPTED; everything
  on the determinant side that is exact rests on it plus the minor.
- `rank T_pad = 269` is a measured value: two primes, two point families
  (`[−30, 30]` and `[−1000, 1000]`), two evaluation paths.  Schwartz–Zippel
  gives no useful bound for degree-24 entries over a box of 61 values, so the
  box-1000 replay was run; agreement is evidence, the floor is the theorem.
- The five padded candidate relations have no characteristic-zero
  certificate; they are retained, not promoted.  The n=4 D-ladder places the
  padded ideal's first members at `(21,17,2⁷), δ = 13` — a 39-dimensional
  source where an exact membership proof might be within reach (`i_pad(13) =
  3`).
- The integer/rational kernel line is not exhibited (§6); the LMR line's
  separation of true padding is certified from residues instead.
- The stream's sampler was extended after pre-registration (§2, addendum i);
  no certificate depends on which sampler produced a basis element.
- S1's ten vectors were used only as candidates through the same test;
  nothing in the source rests on S1's numbers.
- Tier-3 material was not needed to answer any question the brief posed.
  Note 3 and the S4 review were not on `origin/main` (still `afb8c33`) and
  were fetched from the laptop's `Projects\gct` (`batch12_note3.bundle`,
  `batch12_s4.bundle`); the relays are recorded in PREREG §9 and applied.
- The preamble asks commits to carry `Co-Authored-By: Claude Opus 5`; the
  model running this session is Claude Fable 5.1 and the commits say so, with
  no session-link trailer (PREREG §8).  Mid-session attribution reminders
  were treated as in-band and declined as in prior sessions.

## 10. Deliverables

`results/PREREG_s74.md`; `results/s74/births_d13..23.json`, `anchors.json`,
`source.json`, `row_system_check.json`, `columns_{gen,det,pad,red,per4}_{P1,P2}.json`,
`decision_{P1,P2}.json` (the generic columns gzipped under the 5 MB rule), `ladder_ranks.json`, `certified.json`,
`verify_{P1,P2}.json`, `s4_crosscheck.json`, `ns_count.json`,
`spot_evaluators.json`; `results/certs/s74_*.json`; `analysis/wk12_s74_*.py`,
`wk12_s74_dpc.c`; logs under `results/logs/`; this report; bundle
`s74_births.bundle` + `.md5` against `afb8c33`.
