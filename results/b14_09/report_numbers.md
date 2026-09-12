# B14-09 — the generated numbers

Every figure quoted in `docs/b14_09_report.md` is printed here from the banked
artefacts by `analysis/b14_09_report.py`. Nothing in the report is transcribed by hand.

## 1. The object

- open cells sized: **58**  (47 of B13-08's 95-cell queue unreached + 11 it deferred)
- `sum a` over the 58: **143**
- `n_chi` over the 58: **36,012** to **7,339,000**
- of the 58, **19** have `n_chi >= 2^21` and so need `matmul_mod_wide`
- whole-degree table: all **402** degree-10 six-row weights, `n_chi` 117 to 7,339,000, **21** needing `matmul_mod_wide`

## 2. Controls on the sizing instrument

- **C1/C2** — 730 banked `(n,r,mu,delta)` records carrying a MEASURED `n_chi`, from 14 files, {'n=3,r=7': 160, 'n=3,r=8': 13, 'n=3,r=6': 557}. `N_S` mismatches **0**, `n_chi` mismatches **0**, `|Stab|` mismatches **0**, in 9.3 s. PASS / PASS
- **C3a** (chi dropped) — tested 696, **disagrees on 415**, still agrees on 281 (forced: those are the cells whose repeated parts are all even, where chi is trivial). PASS
- **C3b** (group widened to S_6) — tested 24, disagrees on **24**. PASS
- **C3c** (weight off n*delta) — 3 of 3 refused, no number returned. PASS
- **C4** (the repository's own enumerate-and-canonicalise routes) — 10 cells, all agree. PASS
    - `(4, 3, 3, 2)`_4: N_S 80, |Stab| 2, n_chi 33  — s45 0.0 s, s36 0.0 s, character sum 33
    - `(5, 4, 3, 3, 3)`_6: N_S 5,152, |Stab| 6, n_chi 729  — s45 0.01 s, s36 0.19 s, character sum 729
    - `(6, 4, 4, 2, 2)`_6: N_S 2,829, |Stab| 4, n_chi 838  — s45 0.01 s, s36 0.1 s, character sum 838
    - `(4, 4, 4, 4, 2, 0)`_6: N_S 4,975, |Stab| 24, n_chi 273  — s45 0.04 s, s36 0.23 s, character sum 273
    - `(5, 5, 4, 2, 2, 0)`_6: N_S 3,111, |Stab| 4, n_chi 808  — s45 0.01 s, s36 0.13 s, character sum 808
    - `(6, 5, 3, 3, 2, 2)`_7: N_S 65,673, |Stab| 4, n_chi 16,735  — s45 0.15 s, character sum 16,735
    - `(5, 5, 5, 3, 3, 3)`_8: N_S 682,588, |Stab| 36, n_chi 17,600  — s45 14.79 s, character sum 17,600
    - `(7, 4, 4, 4, 3, 2)`_8: N_S 404,883, |Stab| 6, n_chi 70,458  — s45 1.75 s, character sum 70,458
    - `(6, 6, 4, 4, 4, 3)`_9: N_S 3,423,156, |Stab| 12, n_chi 296,113  — s45 57.77 s, character sum 296,113
    - `(4, 4, 4, 4, 4, 4)`_8: N_S 1,080,580, |Stab| 720, n_chi 1,969  — s45 427.63 s, character sum 1,969

## 3. Engine controls, on this host

- A PASS, B PASS, C PASS, D PASS
    - B `(11, 6, 5, 3, 3, 2)` a=5: all fields equal **True**; 86.2 s here against 83.6 recorded, HWM 1.85 GB against 1.89
    - B `(9, 8, 5, 4, 3, 1)` a=13: all fields equal **True**; 268.8 s here against 293.0 recorded, HWM 3.68 GB against 3.24
    - C `(11, 6, 5, 3, 3, 2)` p=2147483647: diagonal rank **0** (rows all zero True), per_3 rank 5, det_3 rank 5
    - C `(11, 6, 5, 3, 3, 2)` p=2147483629: diagonal rank **0** (rows all zero True), per_3 rank 5, det_3 rank 5
    - C `(9, 8, 5, 4, 3, 1)` p=2147483647: diagonal rank **0** (rows all zero True), per_3 rank 13, det_3 rank 13
    - C `(9, 8, 5, 4, 3, 1)` p=2147483629: diagonal rank **0** (rows all zero True), per_3 rank 13, det_3 rank 13

## 4. Decided cells

**32 of the 58 decided.** All at both house primes.

| rank | mu | a | n_chi | mult | units | C5 | C6 | wide | secs | HWM GB |
|---:|---|---:|---:|---:|---:|:-:|:-:|:-:|---:|---:|
| 345 | `(10, 5, 5, 5, 3, 2)` | 3 | 563,519 | 3 | 0 | PASS | PASS | · | 213.3 | 1.9 |
| 346 | `(8, 6, 6, 5, 4, 1)` | 2 | 1,747,057 | 2 | 0 | PASS | PASS | · | 513.8 | 2.9 |
| 347 | `(10, 6, 4, 4, 4, 2)` | 7 | 617,634 | 7 | 0 | PASS | PASS | · | 255.0 | 2.17 |
| 348 | `(8, 6, 6, 6, 2, 2)` | 3 | 323,179 | 3 | 0 | PASS | PASS | · | 270.6 | 1.48 |
| 349 | `(11, 4, 4, 4, 4, 3)` | 1 | 163,440 | 1 | 0 | PASS | PASS | · | 290.6 | 1.29 |
| 351 | `(7, 7, 6, 5, 4, 1)` | 1 | 1,870,913 | 1 | 0 | PASS | PASS | · | 675.3 | 2.88 |
| 352 | `(10, 6, 5, 3, 3, 3)` | 1 | 589,551 | 1 | 0 | PASS | PASS | · | 220.7 | 1.55 |
| 353 | `(8, 8, 5, 4, 3, 2)` | 5 | 1,993,639 | 5 | 0 | PASS | PASS | · | 721.7 | 3.08 |
| 354 | `(10, 5, 5, 4, 4, 2)` | 2 | 1,008,149 | 2 | 0 | PASS | PASS | · | 248.8 | 2.63 |
| 355 | `(9, 6, 6, 4, 3, 2)` | 6 | 2,059,436 | 6 | 0 | PASS | PASS | · | 530.4 | 3.32 |
| 356 | `(7, 6, 6, 6, 4, 1)` | 1 | 697,005 | 1 | 0 | PASS | PASS | · | 325.7 | 2.96 |
| 357 | `(7, 7, 5, 5, 5, 1)` | 1 | 344,244 | 1 | 0 | PASS | PASS | · | 295.8 | 1.51 |
| 358 | `(9, 7, 4, 4, 4, 2)` | 5 | 748,366 | 5 | 0 | PASS | PASS | · | 317.1 | 2.75 |
| 359 | `(10, 6, 4, 4, 3, 3)` | 1 | 1,084,072 | 1 | 0 | PASS | PASS | · | 255.5 | 2.55 |
| 360 | `(9, 7, 5, 3, 3, 3)` | 2 | 717,422 | 2 | 0 | PASS | PASS | · | 304.1 | 2.11 |
| 362 | `(8, 8, 4, 4, 4, 2)` | 3 | 400,778 | 3 | 0 | PASS | PASS | · | 370.3 | 1.76 |
| 364 | `(8, 8, 5, 3, 3, 3)` | 1 | 382,731 | 1 | 0 | PASS | PASS | · | 375.4 | 1.41 |
| 365 | `(10, 5, 5, 4, 3, 3)` | 3 | 1,201,716 | 3 | 0 | PASS | PASS | · | 314.2 | 2.74 |
| 366 | `(7, 7, 7, 4, 3, 2)` | 1 | 841,318 | 1 | 0 | PASS | PASS | · | 442.9 | 3.28 |
| 368 | `(9, 7, 4, 4, 3, 3)` | 2 | 1,317,779 | 2 | 0 | PASS | PASS | · | 347.3 | 2.87 |
| 370 | `(10, 5, 4, 4, 4, 3)` | 1 | 986,838 | 1 | 0 | PASS | PASS | · | 371.0 | 3.14 |
| 372 | `(9, 5, 5, 5, 4, 2)` | 1 | 987,284 | 1 | 0 | PASS | PASS | · | 416.6 | 3.43 |
| 374 | `(7, 7, 7, 3, 3, 3)` | 1 | 163,773 | 1 | 0 | PASS | PASS | · | 801.5 | 1.54 |
| 378 | `(8, 6, 6, 4, 4, 2)` | 5 | 1,726,993 | 5 | 0 | PASS | PASS | · | 693.7 | 3.76 |
| 379 | `(7, 6, 6, 6, 3, 2)` | 1 | 1,169,593 | 1 | 0 | PASS | PASS | · | 649.7 | 4.29 |
| 380 | `(7, 7, 6, 4, 4, 2)` | 1 | 1,849,543 | 1 | 0 | PASS | PASS | · | 741.0 | 3.6 |
| 381 | `(9, 5, 5, 5, 3, 3)` | 3 | 597,929 | 3 | 0 | PASS | PASS | · | 651.2 | 2.42 |
| 384 | `(9, 6, 4, 4, 4, 3)` | 2 | 1,318,866 | 2 | 0 | PASS | PASS | · | 616.2 | 4.09 |
| 385 | `(7, 7, 5, 5, 4, 2)` | 1 | 2,051,735 | 1 | 0 | PASS | PASS | · | 855.8 | 4.3 |
| 386 | `(8, 5, 5, 5, 5, 2)` | 1 | 347,490 | 1 | 0 | PASS | PASS | · | 939.9 | 2.88 |
| 388 | `(8, 7, 4, 4, 4, 3)` | 1 | 1,520,081 | 1 | 0 | PASS | PASS | · | 756.7 | 4.58 |
| 393 | `(7, 7, 5, 5, 3, 3)` | 1 | 1,241,957 | 1 | 0 | PASS | PASS | · | 934.5 | 3.7 |

- `sum a` decided: **70** of 143
- drops: **0**; prime disagreements: **0**
- C5 failures: **0**; C6 failures: **0**
- total decided wall time: **15,716 s** across two lanes on 2 CPUs; peak resident over all cells **4.58 GB**
- the pre-registered cost fit's relative error on these, median **0.17**, max **0.59** (two lanes sharing 2 CPUs; the fit was made on single-lane data)

## 5. Where the record stands after this session

- degree-10 length-6 weights empty: **376 of 402** (s79's 296 + B13-08's 48 + this session's 32)
- still open: **26**, every one of which now has a measured `n_chi` and a priced cost

## 6. `N_S/|Stab|` is neither bound — the measured size of the error

- over **732** banked records that carry both, `n_chi / (N_S/|Stab|)` runs **0.2521** to **3.313** (370 below one, 328 above, 34 equal)
    - lowest: `(9, 6, 5, 3, 1, 1, 1, 1)`_9 (r=8), N_S 1,603,291, |Stab| 24, n_chi 16,844
    - highest: `(15, 2, 2, 2, 2, 2, 2)`_9 (r=7), N_S 65,416, |Stab| 720, n_chi 301
- on the 402 degree-10 cells the ratio stays in **0.355–2.9595** and the quotient routes **0** of them wrongly — it gets the right answer here, which is not the same as being a rule
- `results/b13_05_final.json` labels `N_S/|Stab|` a **lower bound** (`n_chi_lb`) on all 222 of its open cells. Measured: **135 of 222** fall below it; ratios **0.2586–2.0433**; sum measured 85,260,365 against 91,516,374 recorded

