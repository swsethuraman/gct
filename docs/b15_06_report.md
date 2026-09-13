# B15-06: fresh stable families

Model for all new work: gpt-6-astra, xhigh. Banked B14-06 code and mathematics retain Claude Opus 5 attribution.

The exact census covers all 40 requested families. A fresh recomputation using the same character methods agrees on all 80 ambient/normalization counts. The dimension-explicit evaluator passes both-prime controls at r=7,8,9,10, including full ten-variable independent padding. No positive multiplicity gap is claimed.

## Exact census

Each entry below is a_inf for tail (t,2^(r-2)). Use n=4, comparison ambient dimension16, stable coefficient degree delta=t+2(r-2), and lambda=(3delta,t,2^(r-2)). S57 Proposition S is inherited; the rational character arithmetic is newly computed.

| t | r=7 | r=8 | r=9 | r=10 |
|---|---:|---:|---:|---:|
| 3 | 1 | 1 | 1 | 1 |
| 5 | 4 | 4 | 4 | 4 |
| 7 | 12 | 12 | 12 | 12 |
| 9 | 28 | 29 | 29 | 29 |
| 11 | 55 | 58 | 60 | 61 |
| 13 | 94 | 103 | 109 | 112 |
| 15 | 146 | 166 | 180 | 189 |
| 17 | 211 | 246 | 274 | 294 |
| 19 | 288 | 344 | 392 | 429 |
| 21 | 378 | 460 | 533 | 594 |

The accepted overlay excludes nine-row t=17 from degree 13 and t=19 from degree 15, with D<=-2 and D<=-1. These are inherited exclusions and were skipped. Nine-row t=21 remains reserved to B15-05. Ten-row t=21 has a_inf=594 and exceeds the 533 cap. Thus 36 families remain within this slot's eligible census before pilot outcomes.

For each stable family the census records i_pad_lb and m_pad_ub=min(a_inf,h_pad_ub,a_inf-i_pad_lb). The exact h_pad_ub is the multiplicity in Sym(V'+Sym^2 V'+Sym^3 V'), derived from the reducible parametrization in proof C2. All 40 values exceed a_inf; this bound adds no ideal floor. Only the accepted nine-row t=17/19/21 transport supplies L_pad=3. Unknown additional ideal floors are not inferred from sampled ranks.

The historical record audit found no previously full stable determinant witness among the other requested families. It retains finite-rung nine-row t=17 observations separately; the stable-ambient upper bound is never substituted for a finite ambient dimension. B13-06 tensor components are inventoried in census.json, with tensor multiplicities distinguished from image ranks.

## Selected pilots

selection.json was written before geometry: (r,t)=(10,19),(8,21),(7,21), with ambient multiplicities 429,460,378. The ten-row family has an inherited LMR structural motivation (k=7, degree 27); the seven/eight-row comparison at t=21 probes lengths where that mechanism is absent. Other open rows are ranked by source size as a resource order, without assigning a probability of positive D.

| r | t | a_inf | GEN rank_lb | DET rank_lb | PAD rank_lb | Interpretation |
|---|---|---:|---:|---:|---:|---|
| 10 | 19 | 429 | pending | pending | pending | Heavy lease requested |
| 8 | 21 | 460 | pending | pending | pending | Heavy lease requested |
| 7 | 21 | 378 | pending | pending | pending | Heavy lease requested |

All ranks, when present, agree at 2147483647 and 2147483629 and are backed by explicit nonzero square minors. The replay reconstructs jets from integer pencils or independent padded linear forms, reevaluates the selected source brackets, and checks every entry of the minor before recomputing its determinant. This is a fresh geometric replay, not stored-matrix elimination. Generic source matrices attaining a_inf also certify source completeness without a separate spanning premise.

A deficient DET rank is a floor, and bounds the ideal from above. A deficient PAD sample cannot produce an ideal lower bound. For a remaining candidate, the next sufficient positive witness is a global determinant ideal floor q and a padded minor r_pad satisfying q+r_pad>a at one fixed cell. A sufficient negative witness is a padded ideal floor at least a_inf-r_det, combined with the stable ideal filtration. No finite degree 27 ambient value is asserted from the stable ten-row count 429.

## Validation and resource decisions

The frozen commit f365568d80d5f66fea2dd9342ff1998e1d866915, tree aff6ca0921ec964cc8b7fcbd64bd5e5e9de9fbbd and annotated tag object 80209c13e9ae33bad8933cb47413bf7710c96cb1 matched before work. Preregistration commit: 5cded1760b25641074ddbf2795554c1dd14b6672. Original setup runtime logs were preserved and excluded from research staging.

The original B14-06 point module fixes NV=8 and AMB=9, and the evaluator factorial table ends at 8!. The per-slot extension makes all point dimensions explicit, validates array shapes, and extends factorials through col!. Reused Jet/contraction/normalization helpers retain their banked attribution. Small controls compare direct epsilon contractions, shifted DET/DETQ, covariance and torus weights, and known peaked liveness. Altered point, Euler, sign, factorial, dimension and source serialization checks detect defects. Full ten-variable padding has exact derivative rank 10 and a nonsingular integer ten-by-ten substitution. NumPy 2.4.6 and python-flint 0.9.0 ran successfully.

| Run | Exit | Wall seconds | Peak aggregate MiB | Cap seconds / MiB |
|---|---:|---:|---:|---|
| b15_06_census_small_resources | 0 | 14.465 | 118.70 | 60 / 512 |
| b15_06_count_replay_small_resources | 0 | 12.078 | 109.14 | 60 / 512 |
| b15_06_extension_small_resources | 0 | 1.179 | 25.23 | 60 / 512 |
| b15_06_timing_small_resources | 0 | 0.882 | 26.95 | 60 / 512 |

Completed pilot/replay pairs: 0/3. No heavy lease is held; the request is recorded in lease_request.json. Independent census and extension work is complete.

One process and one BLAS thread were used under the native Windows Job Object wrapper. Four-point timing controls price construction, point generation and evaluation separately; extrapolations are labeled estimates and exclude matrix reduction/replay. No weight carrier or stabilizer quotient was allocated. Every tracked artifact is checked below 5,000,000 bytes; large delivery bundles are split by the supplied helper.

## Replay and delivery

All commands run from C:/Users/swami/Projects/gct-gpt/work/batch15_workers/B15-06. A concise exact-count replay is:

```powershell
& 'C:/Users/swami/Projects/gct-gpt/work/batch15_workers/B15-06/.venv/python.exe' analysis/b15_bound.py --slot 06 --name b15_06_receiver_counts --seconds 60 --memory-mb 512 analysis/b15_06_verify.py counts
```

Use the same executable and wrapper for the following entry points, with unique run names:

- analysis/b15_06_census.py: regenerate the 40-row census (60 seconds,512 MiB).
- analysis/b15_06_verify.py counts: independently recompute and compare 80 certificates (60 seconds,512 MiB).
- analysis/b15_06_geometry.py controls: dimension and liveness controls (60 seconds,512 MiB).
- analysis/b15_06_heavy.py: selected production and native geometric replay, requiring an integrator lease (900 seconds,1536 MiB).
- analysis/b15_06_verify.py geometry --r R --t T: replay saved native minors under a lease.

Input hashes are in preregistration and input_hashes.json. Source constructions, integer points, primes, interpolation seed, bracket-by-point orientation, minors, and resource logs are retained. The chart uses ordinary c=[s0^4]F, with c=1 for DET; it does not silently substitute the historical factorial symbol u=24c.

Final packaging, after the last commit: tools/delivery/check_batch15.py --branch b15-06-fresh-tails --base f365568d80d5f66fea2dd9342ff1998e1d866915 --slot 06, then tools/delivery/package_batch15.py --branch b15-06-fresh-tails --slot 06 --model gpt-6-astra --output delivery/b15_06_final. The external manifest carries head/tree and bundle checksums without self-reference. A packaging PASS is not mathematical verification.
