# B13-08 — generated figures (analysis/wk13_b08_reportnums.py)

- reached: **47 of 95** (Σa = 232 of 367), every one `mult = a` at both house primes
- contiguous prefix in the recorded cost order: **42** weights, through **rank 338**
- on the unchanged engine: 45; on the lean driver (the `n_chi >= 2^21` weights of addendum B): 2 — ranks 319, 361
- drops: **0**; prime disagreements: **0**
- N_S over the weights reached: 1,706,497 to 4,606,382; a from 1 to 15; n_chi to 2,422,004
- cost: 10,341 CPU-seconds over the weights reached, longest 877 s, peak RSS 3.84 GB
- not reached: 48 (Σa = 135), of which 15 are addendum-B weights not yet run
- measured throughput: median **6.9 s per 10^6 of N_S·delta** over the 47 reached; the 48 unreached carry Σ N_S·delta = 2,725·10^6, so **≈ 5.2 CPU-hours**, about 3.1 h of wall clock on a two-lane box of this size
- degree-10 length-6 census: 402 weights, session 79 banked 296, this session 47 → **343 empty, 59 open** (48 of them below N_S = 10^7, 11 deferred to batch 14 at or above it)
