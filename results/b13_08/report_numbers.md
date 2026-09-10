# B13-08 — generated figures (analysis/wk13_b08_reportnums.py)

- reached: **38 of 95** (Σa = 210 of 367), every one `mult = a` at both house primes
- contiguous prefix in the recorded cost order: **22** weights, through **rank 318**
- on the unchanged engine: 38; on the lean driver (the `n_chi >= 2^21` weights of addendum B): 0
- drops: **0**; prime disagreements: **0**
- N_S over the weights reached: 1,706,497 to 3,041,630; a from 1 to 15; n_chi to 1,713,081
- cost: 7,338 CPU-seconds over the weights reached, longest 548 s, peak RSS 3.84 GB
- not reached: 57 (Σa = 157), of which 17 are addendum-B weights not yet run
- measured throughput: median **7.1 s per 10^6 of N_S·delta** over the 38 reached; the 57 unreached carry Σ N_S·delta = 3,011·10^6, so **≈ 6.0 CPU-hours**, about 3.5 h of wall clock on a two-lane box of this size
- degree-10 length-6 census: 402 weights, session 79 banked 296, this session 38 → **334 empty, 68 open** (57 of them below N_S = 10^7, 11 deferred to batch 14 at or above it)
