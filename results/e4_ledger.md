# e4 ledger — session 33: the ambient ladder and the rung record

Branch `s33-e4`.  Pre-registration: `results/PREREG_s33.md` (committed at
`f31a3f4`, before any number below existed).  Phase 1 code:
`analysis/wk9_s33_ladder.py` (numpy DP over weight multiplicities;
`a` by the signed 24-term Weyl sum).

**Self-checks, all passed before the table was written** (P5): brute-force
enumeration agrees at `delta <= 4` (`N_S`, `a`, `n_chi`); s29's anchors
`a((delta^4), delta) = 0,0,0,1,0,1,1,3` for `delta = 1..8` reproduce; s29's
recorded `N_S(6) = 12652`, `N_S(7) = 57232` reproduce; `a(10) = 5 >= 1`
(catalecticant); the plethysm route (`analysis/wk8_s30_pleth.py`, reused
verbatim) agrees at every `delta <= 9`; the `r = 2` witness arithmetic gives
`mult s_(4,4) in Sym^2(Sym^4 C^2) = 1`.

## Phase 1 — the ladder, `delta = 1..24` (exact, three independent routes on the overlap)

`a(delta) = <h_delta[h_4], s_(delta^4)>` = dim of degree-`delta`
`SL_4`-invariants of quartic surfaces.  `N_S` = weight-`(delta^4)` space
dimension (unreduced pipeline size); `n_chi` = its `sign^delta`-isotypic part
(reduced pipeline size, per the registered rectangular-weight reduction);
`N'` = the `E_12` target weight space `(delta+1, delta-1, delta, delta)`.

| delta | a | N_S | GB unreduced (5.6e-8 N_S^2) | n_chi | N' | GB reduced matrix (8 N' n_chi) | status |
|---|---|---|---|---|---|---|---|
| 1 | 0 | 1 | ~0 | 0 | 1 | ~0 | excluded free (a = 0) |
| 2 | 0 | 10 | ~0 | 3 | 8 | ~0 | excluded free (a = 0) |
| 3 | 0 | 70 | ~0 | 3 | 62 | ~0 | excluded free (a = 0) |
| 4 | 1 | 465 | 0.012 | 43 | 404 | 0.0001 | live — validation anchor (s29: mult = 1) |
| 5 | 0 | 2505 | 0.35 | 95 | 2293 | 0.002 | excluded free (a = 0) |
| 6 | 1 | 12652 | **9.0 — over budget unreduced** | 661 | 11624 | 0.06 | live — **the deciding rung** (integrator e = 6 vs s29 e >= 7) |
| 7 | 1 | 57232 | 183 | 2310 | 53506 | 0.99 | live |
| 8 | 3 | 240481 | 3240 | 10738 | 226348 | 19.4 dense → blocked echelon (<= n_chi^2 = 0.92 GB resident) | live — attempt per prereg §4 |
| 9 | 0 | 936785 | — | 38499 | 889332 | — | excluded free (a = 0) |
| 10 | 5 | 3428138 | — | 146206 | 3270668 | 3800 | beyond budget (echelon alone ~170 GB) |
| 11 | 2 | 11817866 | — | 489514 | 11335671 | — | beyond budget |
| 12 | 11 | 38676949 | — | 1625621 | 37238136 | — | beyond budget |
| 13 | 4 | 120577553 | — | 5010838 | 116511802 | — | beyond budget |
| 14 | 19 | 359800464 | — | 15044485 | 348660633 | — | beyond budget |
| 15 | 12 | 1030830032 | — | 42898390 | 1001541696 | — | beyond budget |
| 16 | 43 | 2845200663 | — | 118731621 | 2770427524 | — | beyond budget |
| 17 | 26 | 7584911479 | — | 315848122 | 7400351958 | — | beyond budget |
| 18 | 86 | 19580001382 | — | 816409799 | 19136550490 | — | beyond budget |
| 19 | 73 | 49046743566 | — | 2042992716 | 48011079287 | — | beyond budget |
| 20 | 190 | 119457712491 | — | 4979112445 | 117097136160 | — | beyond budget |
| 21 | 172 | 283383330899 | — | 11805753509 | 278133237929 | — | beyond budget |
| 22 | 406 | 655832583316 | — | 27331117859 | 644408586110 | — | beyond budget |
| 23 | 430 | 1482829086428 | — | 61779198234 | 1458500964329 | — | beyond budget |
| 24 | 901 | 3279794012205 | — | 136670650003 | 3228995236485 | — | beyond budget |

**What the ladder alone already says.**  `e ∈ {4, 6, 7, 8} ∪ {10, 11, ...}`:
degrees 1, 2, 3, 5 and — new this session — **9** carry no `SL_4`-invariant at
all, so no equation can live there; `e = 4` is excluded by s29's measured
`mult((4^4), 4) = 1 = a` (re-certified below).  The reachable rungs are
exactly 6, 7, 8; rung 9 is excluded free; rung 10 is one-to-two orders of
magnitude beyond this container either way (K3 territory).  So this session's
strongest possible measured outcomes are: `e ∈ {6, 7, 8}` exhibited with the
sceptical protocol, or the bracket `e >= 10`.

Incidental to the hunt but worth banking: the ladder is the Poincaré series of
the invariant ring of quartic surfaces through degree 24 —
`1, 0, 0, 0, 1, 0, 1, 1, 3, 0, 5, 2, 11, 4, 19, 12, 43, 26, 86, 73, 190, 172,
406, 430, 901` (degrees 0..24) — with the degree-9 gap and the `a(8) = 3 =
{I4^2} + two new` structure visible.

## Phase 2 — the rung record (banked as completed)

**Gate and validation battery (K1, V1–V5), all passed before any rung:**

| check | result |
|---|---|
| K1 witness: binary quartics, `closure{l^3 m}`, `lam=(4,4)`, `delta=2`, unreduced s30 pipeline | `a=1, mult=0`, kernel `= (12,-3,1)` at both primes; wrong-rule signature `(1,-4,3)` asserted absent ✓ |
| V2: rung 4 by *both* pipelines | reduced == unreduced: `a=1, mult=1`, **same kernel vector** at both primes ✓ (re-certifies s29's `e != 4` under the corrected rule) |
| V3: enumeration vs DP | `N_S`, `n_chi`, `N'` agree at every rung touched ✓ (asserted in-run) |
| V4: rung 5 (odd/sign branch) | reduced kernel dimension `0 = a(5)`; odd-swap-fixed rows cancel identically (exact assert) ✓ |
| V5: rung 6 at both primes | below ✓ |

Per-rung discipline as pre-registered: `a` by reduced-kernel dimension must
equal the plethysm (asserted); `rank = n_chi − a` asserted; evaluation at
`npts = a + 8` random integer 4-tuples (entries `[−40, 40]`, s30
`restrict`/`eval_row` verbatim); flint `nmod_mat` for every rank/nullspace;
both house primes.  A rank attaining `a` is a certificate
(`rank_p <= rank_Q <= a`).

| rung `delta` | a | mult | verdict | cost |
|---|---|---|---|---|
| 4 | 1 | **1** | `e != 4` re-certified (both pipelines, both primes) | <1 s |
| 5 | 0 | — | excluded free (`a = 0`), sign-branch check non-vacuous | <1 s |
| 6 | 1 | **1** | **`e != 6` — the deciding rung: the integrator's standing `e = 6` is refuted; s29's `e >= 7` confirmed.**  The unique degree-6 invariant does not vanish on `D_4`.  Both primes, 5930 dedup rows × 661 cols, rank 660 = `n_chi − a` | 7 s |

*(rungs 7 and 8 appended as they complete)*
