# Pre-registration — session 39: the long-weight occurrence screen (`ℓ = 6..10`) and one-bit obstruction tests

Session 39, 2026-09-02.  Branch `s39-longweights` off clone tip `e9cb8dd`
(the s36 merge).  Ancestry gate `git merge-base --is-ancestor 48bbdc3 HEAD`:
**pass**; `docs/s36_review.md` present.  No session-39 collision: the
repository carries only the brief `docs/s39_prompt.md`, no session-39 code,
results or record.  Brief: `docs/s39_prompt.md`, plus the integrator's
addendum received at the start of the session (§0 below).  This file is
committed before any screen row is computed and before any evaluation.

Convention (stated so it cannot drift): `D := mult_pad − mult_det`; only
`D > 0` is an obstruction; `D < 0` is the expected direction and is not one.
An **occurrence obstruction** is a cell with `mult_det = 0 < mult_pad`.

## 0. The integrator's addendum — a proved constraint, banked

> Restrict the screen and the one-bit tests to `6 ≤ ℓ(λ) ≤ 10`.  The padded
> permanent is concise in 10 variables, so its orbit closure lies in the
> subspace variety `Sub_10`, whose coordinate ring supports only weights with
> at most 10 rows; hence `mult_pad = 0` for every weight with `ℓ ≥ 11` and no
> obstruction can live there.

*Proof (one paragraph, house notation).*  Every pad point of the pipeline is
`l(s)·per_3(A(s))`, a linear pullback of `x_0·per_3(x_1..x_9) ∈ Sym^4 C^{10}`
along `C^r → C^{10}`; so `P_r ⊆ Sub_10 := GL_r · Sym^4(C^{10}) ⊆ Sym^4 C^r`,
the quartics expressible in ≤ 10 linear forms (closed: a collapsing image).
Let `v` be a highest-weight vector of weight `λ` with `ℓ(λ) ≥ 11` and
`F = g·F_0 ∈ Sub_10` with `F_0 ∈ Sym^4(C^{10})` (only `x_1..x_{10}`).  Then
`v(F) = (g^{-1}·v)(F_0)`, and `g^{-1}·v ∈ V_λ` is a sum of weight vectors of
weights `μ` of `V_λ`; a weight vector of weight `μ` is a combination of
monomials `∏ c_{α_j}` with `Σ α_j = μ`, and only monomials with every `α_j`
supported on `{1..10}` survive at `F_0`, forcing `μ_{11} = … = μ_r = 0`.  But
every weight `μ` of `V_λ` has `sort(μ) ⊴ λ`, so `μ_1+…+μ_{10} = |λ| ≤
λ_1+…+λ_{10}` forces `λ_{11} = 0`, contradicting `ℓ(λ) ≥ 11`.  Hence `V_λ`
vanishes on `Sym^4(C^{10})`, so on `Sub_10`, so on `P_r`: `mult_pad(λ,δ) = 0`.
∎  (Same argument with 16 in place of 10 gives the brief's `ℓ ≤ 16` for the
determinant side, and with `k = ℓ(λ)` it is the standing restriction lemma.)

**Consequence for this session.**  The obstruction-eligible region is now
`a ≥ 1`, `λ_1 ≥ δ` (Kadish–Landsberg via (★)), `6 ≤ ℓ(λ) ≤ min(δ, 10)`
(`ℓ ≤ 5` cannot see the permanent, `docs/washout_lemma.md`; `ℓ ≤ δ` because
every constituent of `Sym^δ(Sym^4)` has at most `δ` rows; `ℓ ≤ 10` by the
addendum).  Rows `11..16` are excluded by theorem, not by budget, and are
not screened.

## 1. What is fixed before the first row

### 1.1 Code and its validation (done before this file; disclosed)

The pure-python house character routines (`scripts/ambient_screen.py`) cost
~70 ms per weight at `δ = 8` and were projected at days for this region
(`results/logs/s39_size_screen.log`).  So the screen runs on a C
Murnaghan–Nakayama engine written for this session from the rule,
**independently of the house routine**: `analysis/wk9_s39_chars.c` (exact
`__int128` characters, memo on beta-sets × suffix ids) with the python
driver `analysis/wk9_s39_chars.py` (`a` and `m_det` as modular weighted sums
over two 61-bit primes, CRT-reconstructed against the bounds `a ≤ f^λ`,
`|T| ≤ g ≤ f^{rect} < 2^70`; the anti-symmetric part `(g − T)/2` asserted a
non-negative integer on every cell).  `python3 analysis/wk9_s39_chars.py
--selftest` (`results/logs/s39_chars_selftest.log`, all pass):

- full character tables `N ≤ 14` (rows ≤ 10) and sampled characters at
  `N = 24, 32, 40` equal the house `chi`;
- the `n = 3` anchors: `Σ m_det = 3, 11, 43` (supports 3, 10, 34) at
  `δ = 2, 3, 4`;
- the `n = 3`, `δ = 10` precedent of `docs/d5_ideal.md` §0: the three
  weights `(13,3,2^7)`, `(12,5,2^6,1)`, `(9,9,2^6)` return `(a, m_det) =
  (1, 0)`; `a((9,4,2),5) = 2`;
- `a(λ, δ)` equals the house `a` at **every** weight with ≤ 10 rows at
  `δ = 5, 6` (530 and 1204 weights);
- **s38's length-5 table** (`results/occurrence_screen.csv`): every row at
  `δ = 5, 6, 7, 8` (23 + 105 + 239 + 435) and at `δ = 9` (708 rows,
  `results/logs/s39_engine_timing.log`) reproduced in `(a, m_det)`;
- `m_det` equals the house `m_det` at 30 random weights (≤ 10 rows),
  `n = 4`, `δ = 6`.

This is the "validate against s38's length-5 table before extending"
requirement of the brief, and it is also the second independently written
`m_det` implementation the obstruction protocol asks for in step (ii),
calibrated exactly as that step prescribes.  It exists *before* any candidate.

**Pilot values, disclosed.**  The timing run (`results/logs/s39_engine_timing.log`)
evaluated four weights per `δ` at `δ = 10, 11, 12` to size the budget:
`(N−8, 1^8)`: `a = 0`; `(N−18, 2^9)`: `a = 1, m_det = 18`; and two balanced
10-row weights (`a = 0` at `δ = 10, 11`; `(12, 4^9)`: `a = 4, m_det = 2254`).
They are not results; every one is recomputed inside the screen.  P2 below
was written with them in view and says so.

### 1.2 Phase 0 — the screen (exact arithmetic)

For `δ = 8, 9, 10, 11, 12` and every `λ ⊢ 4δ` with `6 ≤ ℓ(λ) ≤ min(δ, 10)`
and `λ_1 ≥ δ` (candidate counts 2228 / 5526 / 12464 / 21925 / 37112):
`a(λ, δ)` by the C engine; for `a ≥ 1`, `m_det(λ)` by the C engine.  Per
`δ`, a random sample of 40 cells is cross-checked against the house routes
(`ambient_screen.a`, `wk8_s30_pleth.a_of`, `ambient_screen.m_det`) where the
house `m_det` is affordable (`δ ≤ 9`; above, `a` only — the house `m_det`
at `N ≥ 40` is beyond its own memory wall, s38).  Sanity: the `ℓ > δ`
candidates at `δ = 8, 9` are confirmed `a = 0`.

Banked lists: **one-bit** (`a = 1, m_det = 0`), **forced** (`a > m_det ≥ 1`),
**silent** (everything else).  Rows banked per `(δ, ℓ)` chunk to
`results/s39_screen/*.csv` as computed (claim queue, two workers, explicit
PIDs), merged into `results/longweight_screen.csv`;
`results/longweight_screen.md` published **before any evaluation**.

**Budget statement.**  From the timing (≤ 0.6 s per `a`, ≤ 1.5 s per
`m_det` at `δ = 12`, memo shared) the whole region through `δ = 12` is
planned exhaustive on two cores in roughly a day.  If the budget stops
earlier the table states exactly which `(δ, ℓ)` chunks were completed; an
incomplete `δ` is reported as "partial", never as "clean".

### 1.3 Phase 1 — tests, ascending in cost

For every one-bit cell, in ascending `n_χ`: the unique HWV by the validated
reduction (`wk9_s36_stabred.py`, both primes), exact reconstruction over `Z`
(`wk9_s36_exact.py` logic: CRT + rational reconstruction), every simple
raising operator applied over `Z` (must vanish); then

1. 20 `det_4` pencils in `ℓ` variables, two primes — **must vanish** (audits
   `m_det = 0`; a nonzero value is a kill: stop everything, that is the
   finding);
2. 20 independently constructed true padded-permanent points
   `l(s)·per_3(A(s))` (the `wk9_s36_bite.family('truepad')` construction,
   which shares no code with `restrict()`), two primes — nonzero at any one
   means `mult_pad = 1 > 0 = mult_det`: an occurrence-obstruction candidate.

For every forced cell: pad-side rank at `3(a + 8)` true padded-permanent
points, two primes; rank `≥ m_det + 1` is a candidate.

Cells beyond the reduction's frontier (`n_χ > 15,500`, `docs/stabiliser_reduction.md`
§6) are named as unreached, not estimated.

## 2. Predictions, falsifiers, regimes

**P1 — the reduction validation reproduces three s36 ledger cells and the
witness.**  Cells chosen by rule before running: the `D = −1` cell
`(8,4,4,4,4)` at `δ = 6` (the most discriminating row), the cheapest
`ℓ = 5` row `(11,4,4,4,1)` at `δ = 6`, and the cheapest `ℓ = 6` row
`(13,8,4,1,1,1)` at `δ = 7`.  Prediction: `(a, N_S, |Stab|, n_χ, mult_det,
mult_pad)` reproduce `results/s36_ledger.md` exactly at both primes, and the
`l^3 m` witness (`(4,4)`, `δ = 2`) gives kernel `∝ (12, −3, 1)`, `mult = 0`.
Falsifier: any deviation → stop; the pipeline is not the one s36 ran.
Regime: same code, same container class; no transfer.

**P2 — whether one-bit or forced cells exist at `6 ≤ ℓ ≤ 10` by `δ = 12`.**
Prediction: **both lists are empty** — the occurrence route is silent at
every length `6..10` through `δ = 12` (confidence ~0.85).  Falsifier: any
row with `a > m_det`.  Basis and regime, stated honestly:

- *Same `(n, m) = (4, 3)`, same objects, extrapolated in `ℓ` from 5 to
  6..10.*  s38's length-5 record (`a ≤ m_det` at 2585 cells, gap widening
  with `δ`, tightest family `(4δ−8, 2^4)` at `a = 1`, `m_det = 8`) plus the
  disclosed pilot cells (`(N−18, 2^9)`: `a = 1`, `m_det = 18` at
  `δ = 10, 11, 12`; `(12, 4^9)`: `4` vs `2254`) suggest the margin grows,
  not shrinks, with the number of rows in this range.
- *The `n = 3` precedent is a different regime and is not transferred.*
  Its one-bit cells sat at `ℓ = 8, 9` of the Kronecker bound `ℓ ≤ n² = 9`
  — the edge where `g(λ, δ^n, δ^n)` is sparse.  Here the corresponding edge
  is `ℓ ≈ 14..16 = n²`, excluded by the addendum; `ℓ ≤ 10` is well inside.
  The house has been burned by regime transfer three times; this prediction
  is the *opposite* of a naive transfer, and if the lists are non-empty the
  regime argument is what failed.
- What would make P2 wrong: a genuinely new vanishing of the two-rectangle
  Kronecker coefficient at a 6–10-row weight with plethysm room — exactly
  the object BIP's positivity theorems cover only for `n ≥ m^25`.  Nobody
  knows; that is why the screen is run.

**P3 — if a one-bit cell exists, does its vector vanish at the padded
permanent?**  The brief reads BIP's asymptotic phenomenon as "yes".  My
prior, with its basis: BIP's non-existence of occurrence obstructions at
`n ≥ m^25` is achieved by *positivity of the Kronecker side* (`m_det > 0`
wherever `a > 0` in the relevant range), i.e. by one-bit cells not existing
at all — it says nothing about the pad side of a one-bit cell that does
exist.  Conditional on existence at `ℓ = 6..10`, `λ_1 ≥ δ`, the only known
mechanism for a low-degree HWV to vanish on `P_r` is the reducible-locus
criterion (★), and the house record at `a = 1`, `λ_1 ≥ δ` (s36's 32 `a = 1`
cells at `ℓ = 5, 6`, `δ = 6, 7`: `mult_pad = 1` in every one) says (★)
rarely holds there.  So conditional on a one-bit cell existing I put
**P(vector vanishes at pad) ≈ 0.3** — i.e. a one-bit cell is more likely a
candidate than not, which is why the protocol below is proportionate.
Falsifier of the prior: the vector vanishes at all 20 points at both primes
and (★) is checked to explain it.  Regime: house data at `ℓ ≤ 6`, `δ ≤ 7`
extrapolated; BIP's regime is not this one.

**P4 — coverage honesty.**  The table states, by `δ` and by `ℓ`, exactly
what was computed; every `m_det` is exact (two primes, CRT, bound checks);
no cell is inferred from a neighbour.

## 3. Kill criteria

- Any det-side non-vanishing at a one-bit cell → **stop everything**; the
  finding is that `a`, `m_det`, or the pipeline is wrong, and the session
  reports which.
- P1 deviation → stop.
- Character budget → the honest table of what was reached (§1.2); nothing
  extrapolated.
- Memory: the reduction frontier `n_χ ≈ 15,500`; cells above it are named.
- `D > 0` anywhere → the obstruction protocol below, then the session ends.

## 4. Obstruction protocol (from the brief, verbatim)

> **Obstruction protocol — STOP-EVERYTHING on any candidate.**  No further
> cells.  Then, in order: (i) `a` by both plethysm routes; (ii) `m_det`
> re-derived by a **second, independently written** implementation
> (Murnaghan–Nakayama on beta-sets, calibrated on the `n = 3` self-test
> values 3, 11 and on s38's length-5 cells) — the whole claim rests on this
> number; (iii) the vector re-reconstructed from a third prime; (iv) the pad
> points rebuilt from scratch by a different random construction, and the
> det vanishing re-checked at 50 pencils; (v) everything into
> `docs/OBSTRUCTION_CANDIDATE.md` with every input file named; (vi) the
> session ends there.  The integrator re-derives independently before anyone
> uses the word.  A false obstruction would be the worst outcome this
> programme could produce; the protocol is proportionate.

Implementation note for (ii): the C engine of §1.1 is one of the two
implementations; the other is the house `scripts/ambient_screen.m_det`
(python, MN on beta-sets), which is affordable at any single cell.  Both are
calibrated on the `n = 3` values and on s38's cells as required.

## 5. Standing rules acknowledged

Single-writer files untouched; delivery by single-ref bundle
`longweights.bundle`, insurance bundles every few hours; no file over 5 MB
committed (certificate vectors to `results/s39_cells/` only under that size,
otherwise a hash and a reproduction command); logs under `results/logs/`;
no repository-wide configuration changed; `python-flint` for every rank;
claim queue with `O_EXCL` claims and explicit-PID kills, read back first;
`pkill -f` never.
