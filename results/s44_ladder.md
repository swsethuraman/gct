# `results/s44_ladder.md` — the six-row Macaulay ladder, every rank

Session 44, branch `s44-sixrowcap`, 2026-09-03.  Pre-registration
`results/PREREG_s44.md` (commit `2e06e3f`, before any rank).  Code
`analysis/wk9_s44_poly.py` (toolkit), `wk9_s44_anchor.py`, `wk9_s44_ladder.py`,
`wk9_s44_sweep.py`, `wk9_s44_syzygy.py`, `wk9_s44_locus.py`,
`wk9_s44_certify.py`.  Logs `results/logs/s44_*.log`.
House primes `P1 = 2147483647`, `P2 = 2147483629`; box `±10^6` unless stated;
seed `20260903`.  Every rank below agreed at both primes at every seed — no
row in this file is a majority vote or an average.

Notation: `M_d(F)` is the Macaulay matrix of the `r` partials of `F` in degree
`d` (rows `(i, m)`, `m` a monomial of degree `d − n + 1`; columns monomials of
degree `d`); `rank M_d = dim (J_F)_d`, `corank = dim (S/J_F)_d`;
`h_d = [t^d] ((1 − t^{n−1})/(1 − t))^r` is the smooth (regular-sequence) corank
and `ρ_d = dim Sym^d C^r − h_d` the generic rank; `ceiling` is
`dim J(M)_d = dim S_d − H_GN(d)` with `J(M)` the ideal of the sixteen `3×3`
minors of the pencil and `H_GN` its Gulliksen–Négård Hilbert function.

## 1. Phase 1 — the two anchors (`results/logs/s44_anchor.log`)

`ρ_d = dim Sym^d − h_d` verified by direct rank at random forms at twelve
`(n, r, d)` away from the anchors — `(3,4,3) (3,4,4) (3,5,3) (3,5,5) (4,4,5)
(4,4,6) (4,5,5) (4,5,6) (4,6,4) (4,6,5) (5,4,8) (3,6,3)` — all agree at both
primes.  Then:

| anchor | `n` | `r` | `d` | rows | cols | `h_d` | `ρ_d` | smooth rank (3 forms) | determinantal rank (3 pencils) | corank |
|---|---|---|---|---|---|---|---|---|---|---|
| A | 3 | 5 | 4 | 75 | 70 | 5 | **65** | 65, 65, 65 | **64, 64, 64** | 6 = μ + 1 |
| B | 4 | 5 | 7 | 350 | 330 | 30 | **300** | 300, 300, 300 | **299, 299, 299** | 31 = μ + 1 |

65 is paper 1's `δ_0 ≤ 65`; 300 is `cap(4)` of the five-row cap theorem.  Both
reproduce exactly, with the drop of one predicted by
`docs/onset_conjecture.md` Theorem 1.  The harness is the cap theorem.

## 2. Phase 2 — the six-row ladder, `n = 4`, `r = 6`

Three random quartics, three `det_4(Σ_{i=1}^{6} s_i A_i)`, three padded
permanents `ℓ(s)·per_3(A(s))` at each `d`, fresh seeds, both primes.  Every
trial of a kind gave the same rank; the single number is that common value.
(`results/logs/s44_ladder_d4to7.log`, `s44_ladder_d8.log`,
`s44_ladder_d9d10.log`.)

| `d` | rows | cols | `h_d` | `ρ_d` | ceiling | smooth | **determinantal** | drop | corank | padded permanent | drop |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 4 | 36 | 126 | 90 | **36** | 66 | 36 | 36 | 0 | 90 | 36 | 0 |
| 5 | 126 | 252 | 126 | **126** | 172 | 126 | 126 | 0 | 126 | **116** | 10 |
| 6 | 336 | 462 | 141 | **321** | 362 | 321 | 321 | 0 | 141 | **271** | 50 |
| 7 | 756 | 792 | 126 | **666** | 672 | 666 | **660** | **6** | **132** | **526** | 140 |
| 8 | 1512 | 1287 | 90 | **1197** | 1147 | 1197 | **1146** | 51 | 141 | **917** | 280 |

**The smallest `d` with a strict drop on `D_6^{det_4}` is `d = 7`, the corank
is `132 = h_7 + 6`, and the cap is `ρ_7 = 666`.**  The pre-registered
prediction P1 (`d = 7`, cap 666) is correct; the pre-registered corank
prediction (`127`, drop of one by analogy with five rows) is **wrong** — the
drop is six, not one.

The `d ≤ 6` rows are not merely "no drop observed".  A rank measured at a
point is a lower bound on the generic rank, and the generic rank is at most
`ρ_d`; a determinantal point attaining `ρ_d` therefore **proves** that the
generic determinantal rank at that `d` is exactly `ρ_d`.  So there is no drop
at `d = 4, 5, 6`, and 666 is the smallest cap this mechanism can produce at six
rows.

## 3. Phase 4.1 — the padded permanent (`pad` columns above)

`ℓ(s)·per_3(A(s))` is reducible, hence singular along the codimension-2 locus
`{ℓ = 0} ∩ {per_3 = 0}` — a threefold in `P^5`, against the determinantal
curve.  Its ranks drop earlier and much further: already at `d = 5` (drop 10)
where the determinant does not drop at all.  In particular **at `d = 7` the
size-666 minors vanish at padded permanents as well as at determinantal
points**: they are equations of `D_6^{det_4}` but not separators.
Pre-registered prediction P2 confirmed.

The `d = 5` row runs the other way — the size-126 minors of `M_5` vanish on
padded permanents and not on determinantal quartics — which is the useless
direction for an obstruction (`mult_pad ≤ a` needs `mult_det < a`), and is
recorded only so the asymmetry is on the file.

## 4. Phase 4.3 — the singular curve and the module `J(M)/J_F`
(`results/logs/s44_locus.log`)

`H_{S/J(M)}(d)` measured from the sixteen `3×3` minors at a fresh pencil, both
primes, against the Gulliksen–Négård prediction; `H_Q(d) = dim J(M)_d −
rank M_d` is the Hilbert function of `Q = J(M)/J_F`, the cokernel of the six
partials inside the sixteen minors.

| `d` | `dim S_d` | `H_GN(d)` | measured `P1` | measured `P2` | `dim J(M)_d` | `rank M_d` | `ρ_d` | `H_Q(d)` |
|---|---|---|---|---|---|---|---|---|
| 3 | 56 | 40 | 40 | 40 | 16 | 6 | 6 | 10 |
| 4 | 126 | 60 | 60 | 60 | 66 | 36 | 36 | 30 |
| 5 | 252 | 80 | 80 | 80 | 172 | 126 | 126 | 46 |
| 6 | 462 | 100 | 100 | 100 | 362 | 321 | 321 | 41 |
| 7 | 792 | 120 | 120 | 120 | 672 | 660 | 666 | 12 |
| 8 | 1287 | 140 | 140 | 140 | 1147 | 1146 | 1197 | 1 |

`H_GN(d) = 20d − 20` for `d ≥ 5` (checked symbolically for `d = 5..11`): the
singular locus is a curve of **degree 20** — the Harris–Tu number
`ν(4) = n²(n²−1)/12` — and **arithmetic genus 21**.  Pre-registered
prediction P3 confirmed, and the measurement agrees with GN in every degree at
both primes, so the grade-4 specialisation of the resolution is doing what it
should at these pencils.

`H_Q` is `10, 30, 46, 41, 12, 1`: the six partials fall short of the sixteen
minors by twelve dimensions in degree 7 and by one in degree 8.

## 5. Phase 3 — the syzygies behind the drop (`results/logs/s44_syzygy.log`)

`rank M_d = r·dim S_{d−n+1} − dim Syz_d`, and the smooth value is attained
exactly when `Syz_d` is the Koszul span.  At `(n, r, d) = (4, 6, 7)`, at both
primes and two independent pencils:

    rows 756, rank 660, nullity 96 = Koszul 90 + extra 6.

The 90 is `C(6,2)·dim S_1 = 15·6`, the Koszul syzygies `(∂_lF)e_k − (∂_kF)e_l`
times a linear form; the Koszul span has rank exactly 90 and together with the
kernel spans it (checked).  So **the drop of six is exactly
`dim H_1(K(∂F; S))_7 = 6`**, six non-Koszul syzygies.  Two structural probes:

- the coefficient forms `G_k ∈ S_4` of the extra syzygies are **not** in
  `J(M)_4` (dim 66 of 126) — the extra syzygies are not minor-generated;
- writing `W(s) = Σ_k G_k A_k ∈ M_4 ⊗ S_4`, every extra syzygy has
  `W ∈ span{ (XM + MY)·S_3 : tr X + tr Y = 0 }` (dim 1344 = `dim Syz_7` of the
  sixteen minors), as the Gulliksen–Négård generation of the syzygies of the
  minors requires.  This is a consistency check on the whole picture and it
  passes.

## 6. Phase 4.4 — the first drop across `(n, r)` (`results/logs/s44_sweep.log`)

Two determinantal pencils per `(n, r, d)`, both primes, with a random-form
control at every `d` that must return `ρ_d` before the determinantal ranks are
looked at.  `d*` is the smallest `d` with a strict drop.

| `n` | `r` | `d*` | `3n−5` | `ρ_{d*}` | rank | drop | corank | `h_{d*}` | GN-forced `d` | `ρ` there |
|---|---|---|---|---|---|---|---|---|---|---|
| 3 | 5 | 4 | 4 | 65 | 64 | 1 | 6 | 5 | 4 | 65 |
| 3 | 6 | 4 | 4 | 111 | 102 | 9 | 24 | 15 | 4 | 111 |
| 3 | 7 | 3 | 4 | 49 | 47 | 2 | 37 | 35 | 3 | 49 |
| 3 | 8 | 3 | 4 | 64 | 56 | 8 | 64 | 56 | 3 | 64 |
| 4 | 5 | 7 | 7 | 300 | 299 | 1 | 31 | 30 | 8 | 480 |
| 4 | 6 | **7** | 7 | **666** | **660** | **6** | 132 | 126 | 8 | 1197 |
| 4 | 7 | 7 | 7 | 1323 | 1279 | 44 | 437 | 393 | 7 | 1323 |
| 4 | 8 | 7 | 7 | 2416 | 2248 | 168 | 1184 | 1016 | 7 | 2416 |
| 5 | 5 | 10 | 10 | 900 | 899 | 1 | 102 | 101 | 12 | 1785 |
| 5 | 6 | 10 | 10 | 2457 | 2451 | **6** | 552 | 546 | 12 | 5852 |
| 5 | 7 | — | 11 | — | — | — | — | — | 11 | 10248 |
| 5 | 8 | — | 11 | — | — | — | — | — | 11 | 24096 |

(`5,7` and `5,8` exceeded the 3500-column budget of the run and were not
measured.)  Two readings, both worth recording:

1. **The first drop sits at `d = 3n − 5` whenever `r ≤ 6`** — `d = 4` at
   `n = 3`, `d = 7` at `n = 4`, `d = 10` at `n = 5`, at `r = 5` and at
   `r = 6` alike.  This is the degree of the five-row cap theorem, and it does
   **not** move when the fifth row becomes a sixth.  At `r = 7, 8` and `n = 3`
   the drop moves down to `d = 3 = n`, where linear syzygies among the partials
   become available because `L` is large inside `M_3` (`dim M_3 = 9`).
2. **At `d = 3n − 5` the size of the drop depends on `r` and not on `n`**:
   it is `1` at `r = 5` for `n = 3, 4, 5`, and `6` at `r = 6` for
   `n = 4, 5`.  (`n = 3, r = 6` reads 9 rather than 6, but there the GN
   ceiling is already binding at `d = 4` — the measured rank 102 *is* the
   ceiling — so that row is ceiling-limited, not mechanism-limited.)
   `1 = C(5,5)` and `6 = C(6,5)` is the obvious guess; `r = 7` cannot test it
   because every `r = 7` case in reach is ceiling-limited too, and the one
   clean test, `(n, r) = (5, 7)`, is out of the column budget.  Recorded as a
   **guess**, not a claim.

## 7. The multimodular certificate (`results/logs/s44_certify_d7.log`)

See `docs/sixrow_cap.md` §4 for why the mod-`p` ranks above do not by
themselves prove anything about the generic point, and what the certificate
adds.
