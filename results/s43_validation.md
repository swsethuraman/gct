# Session 43 — validation (P1 of `results/PREREG_s43.md`), before any new cell

All four parts run on branch `s43-sixrow-close` before the first Phase-A or
Phase-B measurement.  Pipeline as pre-registered; `python-flint` only.

## Part A — three banked session-41 rows, re-measured from scratch

`analysis/wk9_s41_cell.py` (the validated driver, unchanged), in-place kernel
route, both primes, `a + 8` points, `mult_red` point-free by (★).

| δ | λ | a | m_det | N_S | Stab | n_χ | rows | mult_det | mult_pad | mult_red | D | s41 row | verdict |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 7 | `(12, 10, 3, 1, 1, 1)` | 1 | 227 | 19488 | 6 | 1282 | 4357 | 1 | 1 | 1 | +0 | identical | **reproduces** |
| 8 | `(16, 10, 3, 1, 1, 1)` | 2 | 536 | 28410 | 6 | 1850 | 6173 | 2 | 2 | 2 | +0 | identical | **reproduces** |
| 8 | `(13, 10, 6, 1, 1, 1)` | 9 | 2229 | 140749 | 6 | 10682 | 31515 | 9 | **8** | **8** | **−1** | identical | **reproduces** |

Every field of every row — `a`, `N_S`, `Stab`, `n_χ`, `rows`, both multiplicities,
`mult_red`, `D` — matches `results/s41_ledger.md` exactly, at both primes
(`2147483647`, `2147483629`); `rank(R) = n_χ − a` and `a` (kernel dimension) `=`
`a` (plethysm) asserted inside each cell process, and every kernel vector was
verified against the uncompressed raising-operator rows.

The third row is the discriminating one, as pre-registered: a route that has
lost the true padded-permanent points, or the (★) reducibility criterion, returns
`mult_pad = 9 = a` and `D = 0` there.  It returned `mult_pad = mult_red = 8`.
Peak resident set 1.46 GB, 495 s — also identical to the s41 row.

## Part B — the `m_det` anchors at `n = 3`

`scripts/ambient_screen.py --selftest`:

```
  [ok] m_det n=3 delta=2 (sum, support)               got (3, 3)
  [ok] m_det n=3 delta=3 (sum, support)               got (11, 10)
  [ok] m_det n=3 delta=4 (sum, support)               got (43, 34)
ALL CHECKS PASSED
```

`Σ m_det = 3, 11, 43` at `δ = 2, 3, 4`.  **PASS.**

## Part C — Phase B's driver against banked `results/s41_per6.md` rows

Two rows of `results/s41_per6.md` re-measured by this session's Phase-B path
(`analysis/wk9_s43_per6.py --one`, which calls `wk9_s41_per6.measure_per6`
unchanged), both primes:

| δ | μ | a | N_S | Stab | n_χ | rows | mult | s41_per6 row | verdict |
|---|---|---|---|---|---|---|---|---|---|
| 7 | `(8, 5, 4, 2, 1, 1)` | 1 | 9649 | 2 | 3751 | 11921 | 1 | identical | **reproduces** |
| 7 | `(8, 4, 4, 2, 2, 1)` | 1 | 18067 | 4 | 5029 | 35318 | 1 | identical | **reproduces** |

**PASS.**

## Part D — the `a = 1` injectivity route (the gate of P3)

Pre-registered gate: the sparse injectivity certificate must reproduce the dense
route's verdict at three already-measured `a = 1` weights of the same family
before it is used at `(6,5,4,3,2,1)`.

| δ | μ | n_χ | rows of `[M;Ev]` | nnz | `mult` (injectivity) | `mult` (dense, s41) | secs | HWM |
|---|---|---|---|---|---|---|---|---|
| 7 | `(8, 4, 4, 2, 2, 1)` | 5029 | 35327 | 150395 | 1 | 1 | 12 | 0.10 |
| 7 | `(7, 6, 4, 2, 1, 1)` | 4383 | 14179 | 82028 | 1 | 1 | 6 | 0.10 |
| 7 | `(6, 5, 5, 3, 1, 1)` | 4187 | 23562 | 116119 | 1 | 1 | 8 | 0.10 |

Both primes, `NONSINGULAR` with a Berlekamp–Massey minimal polynomial of degree
exactly `n_χ` and `f(0) ≠ 0` in every case.  **3 of 3 agree: PASS.**  Peak
resident set 0.10 GB against the dense route's 0.5–0.9 GB at the same weights,
and 6–12 s against 25–56 s: the certificate is `O(nnz)`, not `O(n_χ²)`.

## Verdict

**P1 passes in every part.**  The session proceeds to Phase A and Phase B.
