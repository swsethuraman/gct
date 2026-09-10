# B13-08 — generated figures (analysis/wk13_b08_reportnums.py)

- reached: **48 of 95** (Σa = 236 of 367), every one `mult = a` at both house primes
- contiguous prefix in the recorded cost order: **42** weights, through **rank 338**
- on the unchanged engine: 46; on the lean driver (the `n_chi >= 2^21` weights of addendum B): 2 — ranks 319, 361
- drops: **0**; prime disagreements: **0**
- N_S over the weights reached: 1,706,497 to 4,606,382; a from 1 to 15; n_chi to 2,422,004
- cost: 10,902 CPU-seconds over the weights reached, longest 877 s, peak RSS 3.84 GB
- not reached: 47 (Σa = 131), of which 15 are addendum-B weights not yet run
- measured throughput: median **7.1 s per 10^6 of N_S·delta** over the 48 reached; the 47 unreached carry Σ N_S·delta = 2,692·10^6, so **≈ 5.3 CPU-hours**, about 3.1 h of wall clock on a two-lane box of this size
- degree-10 length-6 census: 402 weights, session 79 banked 296, this session 48 → **344 empty, 58 open** (47 of them below N_S = 10^7, 11 deferred to batch 14 at or above it)
