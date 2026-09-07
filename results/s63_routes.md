# Session 63 — the three projections at r = 9, costed

The C2 question — is `i_det = 1` at the LMR cell `λ = (65,17,2⁷)`, `δ = 24`? —
reduces (both integrator notes, `docs/lmr_cell.md` §3a) to **one rank lower
bound**: `rank Θ⁺₂₃ = 273` (full) at the predecessor `(61,17,2⁷)`, or
`rank Θ⁺₂₄ ≥ 273` directly, with the ladder + LMR then pinning `i_det = 1`. Only
a lower bound of 273 is ever needed, and `rank(PA) ≤ rank(A)` makes any
projection safe in that direction.

This file costs the three ways to realise the projection `P` at `r = 9`, per
Task 2. **`docs/s62_report.md` and `results/s62_cost.md` were absent at session
start and at the halfway mark**, so `|S|` — the number session 62 task 1 was to
measure and the number both notes make session 63's first deliverable — is
measured here from the family scaling rather than read from s62.

Container: **2 cores, 7 GB RAM**. Every cost below is against that.

## The measured scaling inputs

`N_S` (weight-`λ` monomial count) and `n_χ = N_S/|Stab_W(λ)|`, `|Stab| = S₇ = 5040`,
reproduced here exactly by the independent `K` engine (`wk10_s63_averify.K_exact`),
matching `docs/lmr_cell.md` §6:

| `δ` | `N_S` | `n_χ ≈` |
|---|---|---|
| 12 | 51,446,325,457 | 1.02 × 10⁷ |
| 23 | **156,419,279,221** | **3.10 × 10⁷** |
| 24 | **156,438,903,314** | **3.10 × 10⁷** |

HWV **support density** `|S_cell|/n_χ`, measured by building the χ-reduction and
taking the kernel of the raising operators at LMR-type family cells
(`wk10_s63_support.py`, `results/s63_support.jsonl`):

| cell `λ(k,m)` | `r` | `δ` | `a` | `n_χ` | `|S|` | `|S|/n_χ` |
|---|---|---|---|---|---|---|
| (16,4,2²) | 4 | 6 | 3 | 131 | 84 | 0.641 |
| (21,5,2³) | 5 | 8 | 4 | 1 040 | 424 | 0.408 |
| (23,5,2⁴) | 6 | 9 | 4 | 4 954 | 1 080 | 0.218 |
| (26,6,2⁴) | 6 | 10 | 9 | 8 486 | 2 206 | 0.260 |

The density falls from 0.64 and **plateaus at ≈ 0.20–0.26**; it does not continue
to zero (the single ideal vector `U_D` at the `n=3` LMR cell independently sits at
3 900/17 047 = 0.229). The union support grows with `a`, so at `a = 274` it can
only be larger. A conservative model `|S|_LMR ≈ 0.20–0.26 · n_χ` gives

    |S|_LMR  ≈  6.2 × 10⁶  to  8.1 × 10⁶      (a floor; larger as a grows)

**This is the number that decides the session, and it is ≥ 6 × 10⁶ — two orders
of magnitude past S2's `10⁵` "out of reach" line.**

## Route 1 — evaluation at random `det₄` pencils (the native HWV instrument)

`mult_det = a − nullity_Q[E; ev_det]`; the projection is evaluation at
`K = a + 8` pencils, so the 48 825-dim target never appears. The wall is the
**build**: the `s45` construction enumerates the `N_S` weight-`λ` monomials as an
`(N_S × δ)` int32 array before any reduction.

Extrapolated from the **measured** `n = 3` control build (`N_S = 1 155 302`,
265 s, 0.36 GB peak; §`wk10_s63_n3control`), linear in `N_S`:

| | measured (n=3 ctrl) | LMR `δ = 23` | factor |
|---|---|---|---|
| `N_S` | 1.16 × 10⁶ | 1.564 × 10¹¹ | 1.35 × 10⁵ |
| monomial array | 55 MB | **14.4 TB** | — |
| build wall-clock | 265 s | ≈ **415 days** | — |
| peak RSS | 0.36 GB | ≈ **49 TB** | — |

**Walled by ~2 000× in memory and ~4 000× in time.** Even the reduced
`n_χ ≈ 3.1 × 10⁷` sparse operator cannot be assembled without first enumerating
all `N_S` monomials in the existing engine. A streaming orbit-representative
build (enumerate the `3.1 × 10⁷` orbit reps directly, never the `1.56 × 10¹¹`
monomials) is the only conceivable opening and is a new engine, not this session.

## Route 2 — random functionals on `Θ⁺`, one `λ`-block column at a time (Foulkes)

s56's engine is quadratic in `|H_{4,δ}| = (4δ)!/(24^δ δ!)`:

| `δ` | `|H_{4,δ}|` |
|---|---|
| 5 | 2.55 × 10⁹ (s56: already infeasible, ~month/cell) |
| 23 | 8.66 × 10⁸⁷ |
| 24 | **1.20 × 10⁹³** |

A single `λ`-block column still pulls back through the Gram kernel `K(π,π′)` over
`|H|²` pairs (`~10¹⁸⁶`). **Infeasible by ~80 orders of magnitude**; taking one
column rather than the whole module changes nothing. Closed.

## Route 3 — the Gram/Schur C2 reduction (S2, sharpened by both notes)

Form `A₂₄ = B_{λ,24}|_{J(M₂₃)}`, a `273 × 273` Gram block on the transported
predecessor; `det A₂₄ ≠ 0 ⟹ rank Θ⁺₂₄ ≥ 273 ⟹ i_det = 1`. Two properties make
this the *architecturally* preferred route:

- **Characteristic-free** (note 1 to 62/63 §2): the step uses only
  `rank(MᵀM) ≤ rank(M)`, true in every characteristic, so `det A₂₄ ≢ 0 (mod p)`
  already gives `det A₂₄ ≠ 0` over `Z`. Entries may be computed mod `p` from the
  start, at both house primes — **no char-0 Gram identity needed** (the char-0
  restriction is only on a claimed *drop* `s = 0`, not on this nonsingularity).
- It removes the 48 825 target **and** the separate `δ = 23` measurement.

But the cost relocates into the entries: `A = C_Sᵀ β_S C_S`, `S` the union of the
273 transported source supports, cost `≈ 273|S|² + 273²|S|`:

| `|S|` | cost | verdict (S2) |
|---|---|---|
| 10³ | 3 × 10⁸ | comfortable |
| 10⁴ | 3 × 10¹⁰ | heavy but possible |
| 10⁵ | 3 × 10¹² | out of reach |
| **6.2 × 10⁶ (measured floor)** | **1.0 × 10¹⁶** | far out of reach |

and the Gram matrix `β_S` alone is `|S|² ≈ 4 × 10¹³` entries. **Out of reach by
≥ 2 orders past the threshold**, and gated on the same build wall as route 1
(the transported source vectors are HWVs in the `n_χ ≈ 3.1 × 10⁷` space).

## Verdict

| route | deciding quantity at `r = 9` | feasible in 7 GB / 2 core? |
|---|---|---|
| 1 native HWV | `N_S = 1.56 × 10¹¹` (build) → 14.4 TB / 415 d | **no** (~2 000×) |
| 2 Foulkes column | `|H_{4,24}| = 1.2 × 10⁹³`, quadratic | **no** (~10⁸⁰×) |
| 3 Gram/Schur C2 | `|S| ≥ 6 × 10⁶` | **no** (~100×), + build-gated |

All three are walled at `δ = 23/24` in this container, by three to eighty-plus
orders of magnitude. The reduction chain is exact and the rank is genuinely
required (`h_pad(LMR) = 521 > 274 = a`, integrator note 1 to s64: every cheap
screen is vacuous), but the single rank it needs is **not affordable here**. The
pre-registered time-box (P3: build does not close) is met, and the stopping rule
— report the measured wall, do not extend — applies. The method itself is
validated at the `n = 3` positive control (below), where the same instrument
returns the first rank drop the programme has ever exhibited.
