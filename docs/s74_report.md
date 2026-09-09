# Session 74 — the LMR source by births, then the decision

Branch `s74-births` off `main` at `afb8c3319d3d1f3afc3d2578c8cb322f2b8a3b92`;
pre-registration `results/PREREG_s74.md` (commit `3edd772`, dated addenda
`5caa2af`) written before any birth was drawn.  Bundle `s74_births.bundle` +
`.md5`.  Labels throughout: **PROVED** / **CERTIFIED** (a nonzero minor over
`Z`, sound over `Q`) / **MEASURED** (a mod-`p` value, or a rank that is only a
floor) / **ADOPTED** / **RECORDED**.

## 0. Verdict

**Decision-table branch: `pad < det`, `D < 0` — no multiplicity obstruction
at the LMR cell.**  On the complete, certified 274-vector source

    rank T_det = 273   CERTIFIED as a floor (nonzero 273×273 minor at both primes),
                       = 273 exactly with LMR's rank T_det ≤ 273 (ADOPTED)
                       ⟹ i_det(24) = 1, and i_det(23) = 0 (the transported
                       δ = 23 source has determinant rank 273 on its own)
    rank T_pad = 269   CERTIFIED as a floor (nonzero 269×269 minor at both primes);
                       269 exactly is MEASURED (nullity 5 at P1 and P2, K = 282
                       true padded points, and again at fresh box-1000 points)
    D = rank T_pad − rank T_det = −4   MEASURED; certified only as D ≤ +1 … see §6

with `dim(U_D ∩ U_P) = 0`, `U_D ⊄ U_P` and `U_P ⊄ U_D` (mod both primes).  The
determinant half of the brief's success criterion is met in full: the
determinant column is finished at 273.  The padded half is the negative: the
padded permanent's ideal meets this weight in five directions where the
determinant's meets it in one.  By note 3 §8's asymmetry the rank floors are
cheap certificates and the shortfall `274 − 269 = 5` is not a theorem; it is
reported as what it is — the same value at two primes, at two point families,
with the kernel exhibited mod `p`.

What this does and does not mean.  `D < 0` is the direction containment
permits (`P ⊆ D ⟹ mult_pad ≤ mult_det`), so the cell gives no obstruction;
the separation `ℓ·per₃ ∉ \overline{GL·det₄}` is known (LMR), and the
multiplicity statistic in weight `(65,17,2⁷)` does not see it.  The known LMR
equation is there (`i_det = 1`), the padded side has more equations (`i_pad = 5`
measured), and the LMR line is not among them (`U_D ∩ U_P = 0`).

The source itself is a deliverable: 274 bracket fillings with every rung's
birth quotient certified at both primes, assembled under one declared row
system, with generic rank 274.

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
