# Session 60 — the balanced length-5 cells, by the sparse route; and the ladders that close them

Branch `s60-balanced5` off `main` at `0960bd5` (the tip of the public clone and
of the laptop's `work/` at session start).  Pre-registration
`results/PREREG_s60.md` (commit `c308f30`, before any multiplicity was
computed).  Code `analysis/wk9_s60_{census,cell,sweep,tails,report}.py`; census
`results/s60_census.{json,md}`, `results/s60_census_d10.{json,md}`,
`results/s60_tail_census.{json,md}`; calibration `results/s60_calibration.md`
(+ `.jsonl`, `s60_scan_{dense,sparse}.jsonl`, `s60_recheck.jsonl`); raw
records `results/s60_cells.jsonl`; ledger `results/s60_ledger.md`;
certificates `results/certs/s60/` with the verifier report
`results/s60_verify.md`; logs `results/logs/s60_*`.  Labels: **proved** /
**measured** / **adopted** (from the integrator's notes of this session, proof
re-derived here) / **expectation**.

## 0. Verdict

> **No length-5 cell has `mult_red > mult_det`.  `R_5 ⊆ D_5^{det_4}` survives
> the balanced complement — the necessary condition holds on everything reached,
> and the "we only looked at skewed weights" objection is closed at `δ = 6`
> outright and reduced to a named, sized frontier at `δ = 7, 8, 9`.**
>
> * **δ = 6 is complete.**  All 88 balanced cells s54 skipped are measured, both
>   sides, both primes.  With s54's 17 skewed cells the entire length-5 record at
>   `δ = 6` — 105 cells, every balance from 0 to 14 — reads `mult_red ≤ mult_det`.
> * **δ = 7 / 8 / 9: 85 / 95 / 94 of the 220 / 414 / 684 informative balanced
>   cells measured directly**, cheapest first (up to `n_χ ≈ 20 000`), plus
>   **99 whole tails closed** by one determinant-side rank each at their
>   stable rung (§4), which settles every rung of those tails in every degree —
>   including 99 of the 1 056 informative `δ = 10` cells, a degree never
>   measured at length 5 before, and closing cells at `δ = 11 … 17`, the first
>   length-5 measurements above `δ = 10` in the programme.  In all, **465 of the
>   2 506 census cells (δ = 6…10) are settled** beside the 362 measured directly
>   (419 cells measured in total, counting the 57 closing cells).
> * **`mult_det = a` at every one of the 419 measured cells** (both
>   primes; nullity-zero certificates above `n_χ = 4000`, exact kernels below).
>   The determinant ideal of `D_5^{det_4}` is still empty everywhere it has been
>   looked for, now including the balanced weights and the stable rungs of
>   99 ladders.
> * **The reducible side bites, and always in the direction containment
>   predicts.**  Eleven measured cells have `mult_red < a` — eight of them below the
>   normalisation bound `h_pad` as well — every one with `mult_det = a`, so
>   `0 = i_det < i_red` there.  `R_5 ⊆ D_5` implies `i_det ≤ i_red` at every cell;
>   all 419 measured cells satisfy it and eleven satisfy it strictly.  The multiplicity record
>   leans **toward** containment; session 54's geometry (and s59's, which this
>   session has not seen) leans **away**.  There is no contradiction — the
>   separating equation, if it exists, sits at a cell outside the measured region,
>   and §4 explains why the balanced region can never be more than a sample of it.
> * **The ladder theorem (adopted from the integrator, proof re-derived in §4,
>   239 consecutive measured pairs with 0 monotonicity violations)** changes what
>   a measurement means: a balanced cell closes only itself and the rungs below
>   it, while one rank at a tail's first stable rung closes the tail forever.  The
>   cost wall for the balanced complement is therefore stated twice (§6): as the
>   cheapest unmeasured balanced cell per degree, and as the cheapest unclosed
>   tail — the second is the one a successor should walk.

## 1. The question and the instrument

At `r = 5`, `P_5 = R_5` (washout Thm 2) so `mult_pad = mult_red` (Thm 3(1)),
and `R_5 ⊆ D_5^{det_4}` forces `mult_red ≤ mult_det` at every length-5 cell
(functoriality, `docs/brief_wording.md` §7); one cell with `mult_red > mult_det`
refutes containment and is the programme's first `D > 0` with no transfer gap
(T1/T2 of `results/PREREG_s54.md`).  Session 54 measured 56 such cells — all
`mult_det = mult_red = a` — but only at skewed weights (`nb ≤ 2500`), and left
88 / 224 / 423 / 696 balanced cells unmeasured at `δ = 6 / 7 / 8 / 9`.

**Determinant side.**  `mult_det = a − nullity_Q [E; ev_det]`, `E` the stacked
simple raising operators on the `χ_λ`-isotypic reduction `V_χ`
(`analysis/wk9_s45_build.py`, unchanged, at `r = 5`), `ev_det` the evaluation
rows at `K = a + 8` random `det_4` pencils.  `nullity_p = 0` at one prime
**proves** `mult_det = a` over `Q` (`docs/sparse_det_route.md` Lemmas 1–2).
Both house primes at every cell, concurrently.

**Reducible side, two instruments.**  (i) Point-free, by Theorem (★)
(`docs/reducible_ideal.md`): `HWV_λ ∩ I(R_5) = ker E ∩ span M_red`, so
`mult_red = a − nullity(E_red)` with `E_red` the columns of `E` whose monomials
have, for every variable, a factor free of it.  (ii) The brief's instrument:
evaluation at `K` random reducible points `ℓ(s)·c(s)`.  Both were run at every
dense-route cell and at every sparse-route cell with `n_χ ≤ 12 000`
(20 000 during the `δ = 6` phase); above that (★) alone.  **Where both ran they
agreed at every cell.**  On the sparse route the (★) nullity is run with the
theorem's floor `k_extra = a − h_pad` random rows from the first attempt
(`mult_red ≤ h_pad`, Corollary B2), so an exact normalisation bound is settled by
a single nonsingularity certificate; cells with `h_pad = 0` (`mult_red = 0` by
theorem, 'dead' in the census) were not measured — none can refute containment
and all are large.

**Routes by `n_χ`** (`results/s60_calibration.md`).  `n_χ ≤ 4000`: the dense
route — exact `python-flint` kernel at both primes, `a` asserted equal to the
Weyl alternation, every kernel vector checked against the full sparse `E`, both
sides as ranks of small matrices, `gct-cert/1` certificates.  Above: the
session-45 Wiedemann certificates with the evaluation rows pinned, levels
`(3,2) → (12,2) → full`, every kernel candidate checked against the full matrix
before it counts.  Calibration before the sweep: the twelve s54 cells with the
smallest, median and largest `nb` per degree reproduce s54's values exactly; the
cost law is `≈ 10^-8 · n_χ² · (14.5 + a)` seconds per determinant sequence at
2–2.5 ns per element operation; the s52 small-cell pathology does **not**
reproduce at `r = 5` (the sparse route did an `n_χ = 66` cell in under 3 s at
0.1 GB; the 4.6 GB s52 saw is consistent with the Frobenius plethysm `amb()`
that this pipeline no longer calls, which costs 25 s and 0.4 GB at `δ = 8` alone).

`N_S` is the full weight-space dimension; `n_χ = dim V_χ` is the stabiliser
reduction of it (`docs/stabiliser_reduction.md`), the column count of every
matrix in this report, and equals `N_S` only when the parts of `λ` are distinct.
Every `n_χ` attached to a measured cell is exact.

## 2. The census (`results/s60_census.md`, `results/s60_census_d10.md`)

| δ | length-5 cells `a > 0` | measured by s54 | complement | informative (`h_pad ≥ 1`) | dead (`h_pad = 0`) | `n_χ ≤ 3000` / `≤ 20k` / `≤ 100k` / above | largest `n_χ` |
|---|---|---|---|---|---|---|---|
| 6 | 105 | 17 | 88 | 88 | 0 | 23 / 52 / 13 / 0 | 70 027 `(7,6,5,4,2)` |
| 7 | 239 | 15 | 224 | 220 | 4 | 26 / 62 / 87 / 49 | 576 214 `(8,7,6,4,3)` |
| 8 | 435 | 12 | 423 | 414 | 9 | 25 / 77 / 96 / 225 | 4 822 376 `(9,8,6,5,4)` |
| 9 | 708 | 12 | 696 | 684 | 12 | 23 / 79 / 104 / 490 | 39 069 764 `(10,8,7,6,5)` |
| 10 | 1075 | 0 | 1075 | 1056 | 19 | 36 / 81 / 116 / 842 | 3.0·10⁸ `(10,9,8,7,6)` |

The complement counts are s54's own skipped counts (prediction C1).  `a` by the
Weyl alternation agrees with s54's Frobenius plethysm at all 1487 cells (C5).
Dead cells are 0 / 4 / 9 / 12 / 19 — far below the 25 % of C2 — and are all
large (`n_χ ≥ 48 156`).  Once the stabiliser reduction is applied the cheapest
unmeasured cell at every degree sits between `n_χ = 524` and `629`, inside the
dense range (C3): s54's `nb ≤ 2500` cap was a cap on `N_S`, not on the matrix it
would have had to rank.  The isotypic reduction, not the sparse route, is what
made the first 130 cells of the complement cheap.

## 3. Coverage and results

| δ | complement | informative | dead | measured (inf.) | implied (inf.) | settled by a closed tail (inf. / dead) | open (inf.) | measured (dead) | D>0 | D=0 | D<0 | mult_det<a | mult_red<a | mult_red<min(a,h_pad) | dense/sparse | cheapest open informative (n_chi) | largest measured n_chi | wall h |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 6 | 88 | 88 | 0 | 88 | 0 | 42 / 0 | 0 | 0 | 0 | 87 | 1 | 0 | 1 | 0 | 27/61 | none — degree complete | 70027 | 2.44 |
| 7 | 224 | 220 | 4 | 85 | 0 | 65 / 0 | 135 | 0 | 0 | 82 | 3 | 0 | 3 | 1 | 36/49 | `(11, 7, 7, 2, 1)` (19316, a=8) | 20177 | 0.87 |
| 8 | 423 | 414 | 9 | 95 | 0 | 78 / 0 | 318 | 0 | 0 | 91 | 4 | 0 | 4 | 4 | 36/59 | `(11, 10, 9, 1, 1)` (21108, a=5) | 19608 | 1.0 |
| 9 | 696 | 684 | 12 | 94 | 0 | 83 / 0 | 587 | 0 | 0 | 91 | 3 | 0 | 3 | 3 | 35/59 | `(16, 9, 9, 1, 1)` (16217, a=23) | 20099 | 1.47 |
| 10 | 1075 | 1056 | 19 | 0 | 0 | 99 / 0 | 957 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0/0 | `(17, 17, 2, 2, 2)` (7601, a=2) | 0 | 0.0 |

Column meanings: *measured* = both sides at that cell; *settled by a closed tail*
= the cell's tail has a full-rank determinant result at its stable rung (§4), so
`D ≤ 0` there by theorem; *open* = informative cells neither measured nor on a
closed tail.  `D = mult_red − mult_det`.  Wall = hours of the measured cells of
that degree.

**Determinant side.**  `mult_det = a` at all 362 census cells and all 57
closing cells.  Zero refutations, zero self-check failures, zero prime
disagreements.  Largest census cell `(7,6,5,4,2)_6`, `n_χ = 70 027`, 21 min at
0.15 GB; the sparse route never exceeded 0.17 GB.

**Reducible side — the named finding: `h_pad` is not tight, and `I(R_5)` bites
where the determinant ideal does not.**  Eleven measured cells have
`mult_red < a`, all with `mult_det = a`:

| δ | λ | a | h_pad | mult_red | i_red | tail ρ, t | against the bound |
|---|---|---|---|---|---|---|---|
| 6 | (8,4,4,4,4) | 2 | 1 | 1 | 1 | (4,4,4,4), 16 | `= h_pad` (bound exact) |
| 7 | (9,9,8,1,1) | 2 | 1 | 1 | 1 | (9,8,1,1), 19 | `= h_pad` |
| 7 | (8,8,8,2,2) | 3 | 2 | 2 | 1 | (8,8,2,2), 20 | `= h_pad` |
| 7 | (12,4,4,4,4) | 4 | 4 | 3 | 1 | (4,4,4,4), 16 | **`< h_pad = a`** |
| 8 | (11,11,8,1,1) | 8 | 8 | 7 | 1 | (11,8,1,1), 21 | **`< h_pad = a`** |
| 8 | (12,9,9,1,1) | 7 | 6 | 5 | 2 | (9,9,1,1), 20 | **`< h_pad < a`** |
| 8 | (16,4,4,4,4) | 7 | 10 | 6 | 1 | (4,4,4,4), 16 | **`< a < h_pad`** |
| 8 | (13,9,8,1,1) | 15 | 21 | 13 | 2 | (9,8,1,1), 19 | **`< a < h_pad`** |
| 9 | (15,15,4,1,1) | 9 | 12 | 8 | 1 | (15,4,1,1), 21 | **`< a < h_pad`** |
| 9 | (20,4,4,4,4) | 9 | 13 | 8 | 1 | (4,4,4,4), 16 | **`< a < h_pad`** |
| 9 | (13,13,8,1,1) | 19 | 17 | 15 | 4 | (13,8,1,1), 23 | **`< h_pad < a`** (pre-sweep scan; re-checked) |
| 10 | (24,4,4,4,4) — closing cell | 10 | 14 | 9 | 1 | (4,4,4,4), 16 | stable rung: `i_red(∞) = 1` |

Three of the eleven sit exactly at the normalisation bound; eight are strictly
below it (and six have `h_pad ≥ a`, so the bound would have allowed `mult_red =
a`).  Read along ladders the values are consistent to the digit with the
theorem of §4: on `(4,4,4,4)` `i_red = 1` at `δ = 6, 7, 8, 9` and at the stable
rung `δ = 10`, i.e. `i_red ≡ 1` on the whole ladder from `δ = 6`; on `(9,8,1,1)`
`i_red = 1` at `δ = 7` and `2` at `δ = 8`.

Each value is exact at both primes: (★) and the `ℓ·c` points agree wherever
both ran, and all eight cells strictly below the bound were re-derived with fresh seeds
(fresh points, fresh preconditioners: `results/s60_recheck.jsonl`; the dense
kernel for `(15,15,4,1,1)_9`, fresh sparse seeds for the others) with identical
values.
Their ideal vectors are exhibited as `hwv` certificates where the dense route
ran — `(9,9,8,1,1)_7` in the sweep and `(15,15,4,1,1)_9` in its re-check
(`results/certs/s60/*_red_ideal_*`): (★)-supported, vanishing at the
recorded and at fresh reducible and padded-permanent points, nonzero at the
determinant pencils.  **Orientation.**  `R_5 ⊆ D_5 ⟹ I(D_5) ⊆ I(R_5) ⟹
i_det ≤ i_red` cell by cell; every measured cell satisfies it, these eleven
strictly.  Read with the ladder theorem, each of these `i_red` values persists at
every higher rung of its tail: `i_red ≥ 1` on `(15,4,1,1)` from `δ = 9` on,
`i_red ≥ 2` on `(9,9,1,1)` from `δ = 8` on, `i_red ≥ 4` on `(13,8,1,1)` from
`δ = 9` on, and `i_red(∞) = 1` exactly on
`(4,4,4,4)` (measured at its stable rung).  The exactness conjecture s47 refuted
at length 6 fails at length 5 in the same way (prediction M3 refuted, M4
confirmed).

## 4. The ladder theorem, and what it did to the sweep

**Statement (adopted from the integrator's notes 1–3; proof checked here).**
Fix a tail `ρ = (λ_2, λ_3, λ_4, λ_5)`, `t = |ρ|`, and the ladder
`λ_δ = (4δ − t, ρ)`.  Let `u = c_{(4,0,0,0,0)}` (the `s_1^4` coefficient
functional, a highest-weight vector of weight `(4,0,0,0,0)` in degree 1).
Multiplication by `u` maps `HWV_{λ_δ}(δ)` into `HWV_{λ_{δ+1}}(δ+1)` (the
raising operators are derivations and annihilate `u`), injectively (`Sym(Sym^4 V)` is
a domain), and descends injectively to `C[D_5]` and `C[R_5]` (both prime
ideals, and `u ∉ I(D_5)`, `u ∉ I(R_5)`: `det(s_1 I_4) = s_1^4` and
`s_1 · s_1^3` have `u`-value 1).  Hence `a`, `mult_det`, `mult_red`,
`i_det = a − mult_det`, `i_red` are **non-decreasing in `δ`** along a ladder.
For `δ ≥ t` every weight-`λ_{δ+1}` monomial has a factor `u` (its `δ+1 > t`
factors other than `u` each carry tail weight `≥ 1`), and `u·E(w) = 0 ⟹ E(w) = 0`
in a domain, so `u·` is onto: everything is **constant for `δ ≥ t`**, and
`a_∞(ρ) := a_t(ρ)` is a proved value.  If `a_δ = a_∞` at some `δ` then every
step from `δ` on is an isomorphism between equal-dimensional spaces, ideal parts
included (`u·w ∈ I ⟺ w ∈ I` by primality), so everything is constant from `δ`
on; the first such `δ` is `δ_close(ρ)`.  **A determinant-side full-rank result
at `(λ_close, δ_close)` gives `i_det = 0` at every rung of the ladder — downward
by monotonicity, upward by stability — hence `D = i_det − i_red ≤ 0` at every
degree: the tail is dead for `D > 0` permanently.**  Caution (integrator note
3, respected in `analysis/wk9_s60_tails.py`): `a_∞` is always the proved `a_t`,
never an observed plateau — `a_δ` can plateau and rise again (`ρ = (4)`:
`1, 1, 2, 2`).

**Checked on live data.**  239 consecutive measured pairs along ladders
(census cells and closing cells): `a, mult_det, mult_red, i_det, i_red`
non-decreasing at every one, 0 violations — 239 independent confirmations of
the theorem at length 5, and of the implementation, since a bug on either side
would show as a violation.  `a_δ` sequences computed here agree with the
integrator's file on all 1 075 tails of the census (`a_∞`, `δ_close` identical).

**What it says about balance.**  Closure at the theorem-guaranteed rung `δ ≥ t`
is `λ_1 ≥ 3δ`; no balanced weight is ever there (`λ_1 ≈ 4δ/5` gives
`t ≈ 3.2δ`), and at length 5 the criterion never even fires at a tail's cheapest
closing cell: every one of the 1 075 census tails stabilises strictly before
`δ = t`, so `a_δ = a_∞` is the criterion that does all the work and `δ ≥ t` is a
fallback that is always more expensive.  Balanced also means bottom-of-ladder
(`λ_1 ≈ λ_2` is `δ ≈ δ_min`), so a balanced cell closes nothing below it and
nothing above it — exactly what the queue `groupby` found: no measured cell of
the complement was implied by another.  **The balanced complement cannot be
closed by sweeping it; it can only be sampled.  The justification for sampling it
stands — `P_5 = R_5`, and a single `mult_red > mult_det` settles everything at
once — but the report has to say what each row reaches, and the ledger now does
(`ρ`, `t`, `reach`).**  Where downward closure does buy something is on
moderately skewed tails: `(5,4,3,1)` has `n_χ = 16 315 / 17 133 / 17 375` at
`δ = 8 / 9 / 10` and `δ_close = 8`, so one cell closes three rungs and the tail.

**The closing sweep.**  `analysis/wk9_s60_tails.py` computes, for each of the
1 075 tails, `δ_min`, the sequence `a_δ` up to `t`, `a_∞ = a_t`, `δ_close`, the
closing cell and its size (`results/s60_tail_census.md`); 892 closing cells are
buildable with the session-45 code (`δ_close ≤ 18`, the int64 multiset code),
183 are not.  The last hours of the budget went to the closing cells, cheapest
first (`results/s60_ledger.md`, second table): 57 closing cells run, every one
full rank on the determinant side, at `δ_close` from 5 to 17 and `a_∞` up to 56;
another 42 tails turn out to have been closed by census cells that already sat
at or above their tail's `δ_close` (the ledger's `reach` column names them).
**99 tails are closed in all** — **the first permanently closed length-5 tails in the
programme**, and the first length-5 measurements at `δ = 11 … 17`.  Their
reducible sides at the stable rung classify the closed tails:

| type at the stable rung | tails | meaning |
|---|---|---|
| `i_det(∞) = 0`, `i_red(∞) = 0` ("empty") | 98 | neither variety has a stable ideal copy at that weight; `D = 0` on the whole ladder |
| `i_det(∞) = 0`, `i_red(∞) > 0` ("reducible-first") | 1 | `(4,4,4,4)`: `i_red(∞) = 1`; `D ≤ 0` on the whole ladder, `< 0` from the rung where `i_red` turns on |
| `i_det(∞) > 0` | 0 | the unseen type; the only one that could host `D > 0` somewhere on the ladder |

Small `a_∞` carries no signal for a determinant equation, exactly as small `a`
did not (s52): 99 closed tails with `a_∞` from 1 to 56, all full rank at the
stable rung.

## 5. What the clean sweep means

The objection to the length-5 record — "only skewed weights were measured" —
is **removed at `δ = 6`**: the record there is complete at every balance.  At
`δ = 7, 8, 9` it is reduced to a frontier stated in §6, with the balanced
region sampled to `n_χ ≈ 20 000` and 99 tails closed outright.  The
necessary condition `mult_red ≤ mult_det` for `R_5 ⊆ D_5` holds on all of it,
with the reducible side biting in the direction containment predicts.  Since
(§4) the balanced region can never be more than sampled by multiplicities, and
no determinant equation has appeared anywhere at length 5 through `δ = 17`, the
geometric route — s54's higher-order exceptional image, s59 — is the only
remaining route to the closure question; the multiplicity route can still
refute it, cheaply and forever per tail, by walking the closing cells.

## 6. The cost wall, stated twice

**As balanced cells.**  Cheapest open informative cell per degree (both
routes, exact `n_χ`): `δ = 7`: `(11,7,7,2,1)`, `n_χ = 19 316`, `a = 8`; `δ = 8`:
`(11,10,9,1,1)`, `n_χ = 21 108`, `a = 5`; `δ = 9`: `(16,9,9,1,1)`, `n_χ = 16 217`,
`a = 23`; `δ = 10`: `(17,17,2,2,2)`, `n_χ = 7 601`, `a = 2`.  Largest cell measured: `n_χ = 70 027`
(`δ = 6`, 21 min); largest at `δ ≥ 7`: `n_χ ≈ 20 000` (3–10 min each).  The
cost law makes a `10^5` cell an hour and a `10^6` cell four days per sequence;
the balanced `δ = 8, 9` cells (`n_χ` up to `3.9·10^7`) are out of reach of this
instrument by orders of magnitude.

**As tails.**  Cheapest unclosed tails (closing cell, `δ_close`, `a_∞`, `n_χ`;
`results/s60_tail_census.md` in `close_key` order): `(13,4,1,1)` →
`(37,13,4,1,1)_14`, `a_∞ = 71`, `n_χ = 13 252` — the cell in flight when the
closing sweep was ended by its recorded process id at rank 58 of 892; then
`(6,6,2,1)` → `(25,6,6,2,1)_10`, `a_∞ = 23`, `n_χ = 18 738`; `(9,3,2,1)` →
`(29,9,3,2,1)_11`, `a_∞ = 37`, `n_χ = 18 207`; `(7,4,2,1)` → `(26,7,4,2,1)_10`,
`a_∞ = 37`, `n_χ = 18 348`.  Each closes three to five census rungs and the tail.  Closing cells with
`n_χ ≤ 30 000` exist for 127 tails (settling 517 census rungs), with
`n_χ ≤ 100 000` for 199 tails (775 rungs); 183 tails have `δ_close > 18` and
need a monomial code wider than int64 before the session-45 build can touch
them.  A successor that walks `results/s60_tail_census.md` by `n_χ` closes
tails at a few minutes each; the queue's cheap end is dense in repeated-part
tails, whose `n_χ` is well below their `N_S`.

**Dead cells** (`h_pad = 0`, 44 across `δ = 7…10`) were not measured; the
cheapest are `(6,6,6,6,4)_7` at `n_χ = 48 156` and `(7,7,7,5,2)_7` at 72 949 —
determinant-side-only measurements, 10 and 25 minutes.

## 7. Certificates and what the verifier covered

362 `gct-cert/1` certificates under `results/certs/s60/`, all through
`tools/verify/verify.py` (`results/s60_verify.md`): **PASS 362, FAIL 0, UNPARSEABLE 0, ERROR 0** (the run was split in two
halves of 181 files to use both cores; `results/logs/s60_verify_{a,b}.log`).
`full_rank` for `det_pencil` and for `reducible` at every dense-route cell
(both primes when `N_S ≤ 3000`; `P1` with the mod-`p` basis recorded when
`N_S > 3000`), and `hwv` certificates of the (★)-supported ideal vectors at the
dense-route reducible bites.  The sparse-route cells (`n_χ > 4000`: 264 of the 419
measured cells; 155 ran the dense route) rest on the algorithmic single-prime nonsingularity certificate
(Lemma 4 of `docs/sparse_det_route.md`), reproducible from the seeds and levels
in `results/s60_cells.jsonl`; `gct-cert/1` has no kind for it — the gap
registered in the pre-registration §7, not discovered afterwards.

## 8. Pre-registration scorecard

| id | prediction | prior | outcome |
|---|---|---|---|
| C1 | complement 88/224/423/696 | 0.95 | **confirmed** |
| C2 | dead cells < 25 % at every degree | 0.60 | **confirmed** (0 / 1.8 / 2.1 / 1.7 %) |
| C3 | cheapest unmeasured informative cell `n_χ ≤ 5000` at every degree | 0.85 | **confirmed** (524–629) |
| C4 | largest `n_χ ~ 10^5` at δ=6, `≥ 10^6` at δ=9 | 0.70 | **confirmed** (70 027; 3.9·10⁷) |
| C5 | Weyl `a` = s54 plethysm at all 1487 cells | 0.97 | **confirmed** |
| M1 | no `mult_red > mult_det` | 0.85 | **confirmed**, 362 census cells + 57 closing cells |
| M2 | `mult_det = a` everywhere | 0.80 | **confirmed** |
| M3 | `mult_red = a` at every informative cell with `h_pad ≥ a` | 0.60 | **refuted** at six cells — `(12,4,4,4,4)_7`, `(11,11,8,1,1)_8`, `(16,4,4,4,4)_8`, `(13,9,8,1,1)_8`, `(15,15,4,1,1)_9`, `(20,4,4,4,4)_9` |
| M4 | some informative cell has `h_pad < a` | 0.55 | **confirmed** (291 in the census; 5 measured, all with `mult_red ≤ h_pad` as the theorem requires) |
| M5 | (★) = points wherever both computed | 0.95 | **confirmed** (345 cells) |
| M6 | both primes agree everywhere | 0.97 | **confirmed** |
| B1 | ≥ 60 % of the δ=6 complement measured | 0.70 | **confirmed** (100 %) |
| B2 | ≥ 25 % of the δ=7 complement measured | 0.50 | **confirmed** (85/220 = 38.6 % measured) |
| B3 | < 10 % of the δ=9 complement measured | 0.75 | **refuted** (94/684 = 13.7 % measured) |
| B4 | ≥ 5 δ=10 cells measured | 0.50 | **confirmed** in the ladder sense: 7 closing cells run at `δ = 10` and 99 `δ = 10` census cells settled by closed tails |
| B5 | s52 small-cell pathology absent at r=5 | 0.50 | **confirmed** |

Unregistered: the ladder theorem and the closing sweep (integrator notes,
mid-session); the three-type classification of closed tails; the exactness
failures below `h_pad`.

## 9. Honest boundary and corrections flagged

* **Proved:** the theorem inputs (washout `P_5 = R_5`, (★), Corollary B2,
  Lemmas 1–4 of the sparse route) and the ladder theorem (§4).
* **Measured, exact, both primes:** everything in the ledger; every
  `mult = a` is a proof (nullity-zero or exact kernel), every `mult < a` is
  exhibited at both primes and re-derived with fresh seeds.
* **Not measured:** 135 / 318 / 587 informative cells at δ = 7 / 8 / 9 (and 957 at
  δ = 10) remain open (neither measured nor on a closed tail), all 44 dead cells, and the 183
  tails whose closing cell needs `δ > 18`.
* **Certificates:** independent verification covers the dense-route cells only
  (§7); the sparse route's proofs are algorithmic.
* **Not this session's:** s59's geometric result, referred to only as the
  brief describes it.
* **Correction flagged (single-writer files untouched):** none of the four
  protected files was found wrong.  `docs/reducible_engine.md` §B's phrase
  "exact where it fires" for `h_pad` (already withdrawn at length 6 by s47)
  is now also false at length 5 at seven measured cells.
* **Engineering:** the s45 build's multiset code is int64 and overflows at
  `δ ≥ 19` (`C(70+δ−1, δ) > 2^63`); a hashed or two-word code is the one change
  needed to reach the 183 unbuildable closing cells.  The `(3,2)` compression
  level loses rank on `E_red` more often than on `E` (three escalations in the
  δ = 6 phase, all caught and certified at `(12,2)`); starting `E_red` at
  `(12,2)` would save a few minutes per large cell.
