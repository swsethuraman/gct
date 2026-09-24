# Session 60 — calibration of the length-5 instrument, before the sweep

Everything here was run before the sweep started (PREREG_s60.md §1 asks for the
dense cap to be fixed by calibration first).  Raw records:
`results/s60_calibration.jsonl` (KC1), `results/s60_scan_dense.jsonl` and
`results/s60_scan_sparse.jsonl` (the timing scan).  Machine: the session
container, 2 cores, 7 GB; both primes run concurrently, so a cell's wall time is
one prime's work plus the shared build.

## 1. KC1 — the instrument reproduces session 54

The twelve s54 cells with the smallest, median and largest `nb` at each degree,
re-measured by the dense route (exact flint kernel, both primes; `mult_det` at
`a + 8` determinant pencils, `mult_red` by (★) and by `a + 8` reducible
`ℓ·c` points):

| δ | λ | `a` | `nb = N_S` | `n_χ` | s54 `mult_det / mult_red` | here `mult_det / mult_red(★) / mult_red(pts)` | s54 s | here s |
|---|---|---|---|---|---|---|---|---|
| 6 | (16,2,2,2,2) | 1 | 608 | 66 | 1 / 1 | 1 / 1 / 1 | 1.6 | 2.8 |
| 6 | (13,6,3,1,1) | 1 | 1463 | 742 | 1 / 1 | 1 / 1 / 1 | 18.8 | 2.7 |
| 6 | (12,7,2,2,1) | 3 | 2467 | 1238 | 3 / 3 | 3 / 3 / 3 | 64.5 | 7.4 |
| 7 | (20,2,2,2,2) | 1 | 618 | 66 | 1 / 1 | 1 / 1 / 1 | 2.9 | 8.0 |
| 7 | (17,6,3,1,1) | 1 | 1733 | 875 | 1 / 1 | 1 / 1 / 1 | 28.0 | 8.5 |
| 7 | (16,7,3,1,1) | 4 | 2414 | 1214 | 4 / 4 | 4 / 4 / 4 | 59.3 | 9.2 |
| 8 | (24,2,2,2,2) | 1 | 619 | 66 | 1 / 1 | 1 / 1 / 1 | 2.1 | 25.5 |
| 8 | (20,8,2,1,1) | 1 | 1623 | 816 | 1 / 1 | 1 / 1 / 1 | 28.9 | 25.6 |
| 8 | (21,6,2,2,1) | 4 | 2403 | 1210 | 4 / 4 | 4 / 4 / 4 | 55.9 | 30.4 |
| 9 | (28,2,2,2,2) | 1 | 619 | 66 | 1 / 1 | 1 / 1 / 1 | 2.4 | 66.7 |
| 9 | (24,8,2,1,1) | 1 | 1709 | 859 | 1 / 1 | 1 / 1 / 1 | 33.4 | 4.6 |
| 9 | (25,6,2,2,1) | 4 | 2448 | 1231 | 4 / 4 | 4 / 4 / 4 | 57.6 | 4.4 |

Every value reproduced, `D = 0` at all twelve, `rank(E) = n_χ − a` and (★) =
points at both primes everywhere.  (The δ = 8, 9 wall times of this run were
dominated by `wk8_s30_pleth.amb`, the Frobenius plethysm used for `a`, which
costs 25 s and 0.4 GB at δ = 8 and more at δ = 9; the instrument now takes `a`
from the Weyl alternation, asserted equal to the census value, and the δ = 9
cells at the bottom of the table already show the corrected cost.)

## 2. The timing scan and the dense cap

Ten informative census cells spanning `n_χ` from 999 to 70 027, each by the
sparse route and (up to 6029) by the dense route, both sides, both primes:

| δ | λ | `a` | `h_pad` | `N_S` | `n_χ` | dense s (HWM GB) | sparse s (HWM GB) | result |
|---|---|---|---|---|---|---|---|---|
| 9 | (24,7,3,1,1) | 4 | 14 | 2804 | 999 | 1.4 (0.12) | 0.7 (0.06) | `4 / 4 / 4` |
| 7 | (15,6,5,1,1) | 4 | 15 | 5368 | 1988 | 7.7 (0.32) | 2.4 (0.06) | `4 / 4 / 4` |
| 8 | (13,13,2,2,2) | 1 | 8 | 29372 | 3009 | 9.4 (0.29) | 14.2 (0.07) | `1 / 1 / 1` |
| 9 | (18,13,3,1,1) | 12 | 29 | 10766 | 3978 | 32.7 (0.43) | 13.4 (0.07) | `12 / 12 / 12` |
| 9 | (24,5,3,2,2) | 4 | 23 | 10918 | 6029 | 95.1 (0.91) | 23.3 (0.07) | `4 / 4 / 4` |
| 9 | (17,13,4,1,1) | 27 | 55 | 21268 | 8001 | — | 67.5 (0.07) | `27 / 27 / 27` |
| 6 | (8,6,6,3,1) | 1 | 4 | 23592 | 11955 | — | 79.1 (0.07) | `1 / 1 / 1` |
| 9 | (13,13,8,1,1) | 19 | 17 | 101838 | 20099 | — | 459.2 (0.11) | `19 / 15 / —` |

(`mult_det / mult_red(★) / mult_red(pts)`; the last cell ran with (★) only, and
its reducible nullity 4 needed four kernel extractions plus a nonsingularity
certificate at `k = 4`, which is where its time went — see §4.)

**Cost law (sparse route).**  One Wiedemann sequence costs about
`10^-8 · n_χ² · (14.5 + a)` seconds on this container for the determinant
side (`nnz_c ≈ (6.5 + K)·n_χ` at level (3,2) with `K = a + 8` pinned rows) and
`≈ 10^-8 · n_χ² · 6.5` for the (★) side, at 2–2.5 ns per element operation;
measured: 101 s for the `n_χ = 20099`, `a = 19` determinant sequence against
135 s predicted, 36.7 s for its (★) sequence against 26 s predicted.  Peak
resident never exceeded 0.11 GB on the sparse route.

**The dense cap is `n_χ = 4000`.**  Below it the dense route costs at most
~35 s per cell (both primes), and it is the route that yields an explicit
highest-weight kernel — hence `gct-cert/1` certificates the independent
verifier can check, the point-free (★) value with no extraction, and the
`ℓ·c` points value from the same kernel.  Above it the sparse route is faster
by a growing factor (4× at 6029) and needs no `O(n_χ²)` memory.  The pure-speed
crossover is lower (`n_χ ≈ 1000–3000`), so the cap trades about 15 s per cell
in the 1000–4000 band for verifiable certificates.

**The s52 small-cell pathology does not reproduce here (prediction B5).**
The sparse route on the smallest cells — `n_χ = 546` in 3.0 s at 0.11 GB,
`n_χ = 66` cells in under 3 s — shows none of the 4.6 GB blow-up session 52
saw at `(30,2,2,2,2,2)_10`, `n_χ = 200`.  The likely cause there was not the
sparse solve but the same `amb()` plethysm call noted above (`δ = 10`, six
rows, the Murnaghan–Nakayama memo), which this pipeline no longer makes.
This is an inference from the profile, not a re-run of the s52 cell.

## 3. Reducible-side protocol: the theorem floor

On the sparse route the reducible nullity has the free lower bound
`a − h_pad` (Corollary B2), so the C helper is run with `k_extra = max(a − h_pad,
#exhibited)` random rows from the first attempt.  A NONSINGULAR verdict then
proves `nullity ≤ a − h_pad`, which with the theorem gives equality: `mult_red =
h_pad` from one sequence.  Checked at `(9,9,8,1,1)_7` (`a = 2`, `h_pad = 1`):
one sequence per side, `mult_red = 1` by (★) and by points, 6.5 s; the dense
route (explicit kernel) gives the same `1`, and the `hwv` certificate of the
single (★)-supported ideal vector passes the verifier (vanishes at the recorded
and fresh reducible and padded-permanent points, nonzero at the determinant
pencils).

## 4. A finding from the scan, ahead of the sweep

`(13,13,8,1,1)`, `δ = 9`: `a = 19`, `h_pad = 17`, and the (★) nullity is **4**
at both primes (four independent kernel vectors, each checked against the full
`E_red`, and `[E_red; R_4]` certified nonsingular), so **`mult_red = 15 < h_pad
= 17`**: the normalisation bound is not exact at this length-5 cell, the same
phenomenon session 47 found at length 6.  `mult_det = 19 = a`, `D = −4`.  The
cell is re-measured inside the sweep (it is in the census) so that its ledger
row comes from the same pipeline as every other.

## 5. Certificates

Dense-route cells write `full_rank` certificates for `det_pencil` and
`reducible` when the side has `mult = a`, and `hwv` certificates of the ideal
vectors when it does not (reducible side: the (★)-supported combinations,
claims `star_support`, `vanishes_at` the reducible points, `nonvanishing_at`
the determinant pencils when `mult_det = a`, fresh reducible and
padded-permanent points vanishing, fresh determinant and generic points not).
Both primes when `N_S ≤ 3000`; `P1` only with the mod-`p` basis recorded when
`N_S > 3000`, and none when `N_S · a > 400 000` terms (noted in the record).
The four calibration certificates of `(14,4,2,2,2)_6` and the four of
`(9,9,8,1,1)_7` pass `tools/verify/verify.py` (8/8).
