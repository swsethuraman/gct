# PREREG — B14-09, the 58 six-row degree-10 cells

`board_numbering: batch14`.  Slot 9 of `docs/batch14_board.md` v0.4.
Branch `b14_09_sixrow_d10`.  Base: the annotated tag `batch14-base`, which peels
to commit `9898e56941a7665f231873481dae956f08509995`, tree
`cb688cd3fe454d638f3202e759e2eaa0c629739f` (`git log -1 --format=%H` /
`--format=%T`; `git rev-parse` returns the tag object `4bda8a12…` and is not
used).  **Committed before any measurement.**  Anything not below is reported as
exploratory.  Dated addenda are committed before the measurements they govern.

Model actually running this session: **Claude Opus 5** (`claude-opus-5`), one
model throughout.  If that changes the report says so per phase.

## 0. Host, declared

One shared cloud container, not twelve: **2 CPUs (Intel Xeon @ 2.80 GHz),
8 023 MB RAM, no swap, ~30 GB free disk.**  Every memory figure below is against
that single 8 GB budget with at most two concurrent lanes.

Toolchain checked, not assumed:

| item | at clone | action |
|---|---|---|
| `python3` | 3.11.15 | — |
| `numpy` / `scipy` | 2.4.4 / 1.17.1 | — |
| `python-flint` | **missing** | `pip install --break-system-packages python-flint` → 0.9.0 |
| `sympy` | **missing** | same → 1.14.0 (+ mpmath 1.3.0) |
| `gcc` | 13.3.0 | present; `analysis/wk11_s71_schur.c` compiled by the engine |

`python3 -c "import flint, sympy, numpy, scipy; print('ok')"` → `ok` after the
two installs.

## 1. Question

Fixed `n = 3`, `r = 6`, `δ = 10`.  The frozen object is session 79's
`results/s79_per6_queue.json['10']`: the **402** length-6 weights `μ ⊢ 30` with
`a(μ,10) ≥ 1`, in `N_S`-ascending order.  296 were banked by s79 and 48 more by
B13-08 (`results/b13_08/per6_d10.jsonl`), leaving **58 open** — the 47 of
B13-08's 95-cell queue it did not reach (ranks 339, 345–360, 362–391) and the 11
it deferred at `N_S ≥ 10⁷` (ranks 392–402).  This is derived, not asserted; §6
Q0 checks the derivation.

**Q1 (sizing).**  For each of the 58: what is `n_χ` — the dimension of the
`χ_μ`-isotypic reduced space that the multiplication's inner dimension actually
is?  No `n_χ` has ever been recorded for any of these 58.

**Q2 (decision).**  For as many of the 58 as the host allows, cheapest first:
is `mult_per3(μ,10) = a(μ,10)`, i.e. is `S_μ ∉ I(D_6^{per₃})_{10}` over `ℚ`?

**What Q2 is and is not for.**  `PROVED.md: degree8_global` is "every `r`, every
`δ ≤ 8`"; **this slot does not extend it.**  Completing all 402 would give
`I(D_6^{per₃})_{10} = 0` — the *six-variable* record through degree 10 — together
with `washout_thm2` and `restriction_lemma` for `ℓ ≤ 5`.  Lengths 7+ at `δ = 9`
and `δ = 10` stay open.  A hit here would be a **permanent-specific** equation,
which *raises* `i_pad` and therefore *lowers* `D`: it advances neither batch
objective.  The slot is demoted and this pre-registration does not pretend
otherwise.

## 2. Instruments

### I1 — `n_χ` by an exact character sum (new; the sizing instrument)

`n_χ` as the engine computes it (`analysis/wk9_s45_build.orbit_setup_arr`) is
the number of `G`-orbits on the weight-`μ` monomial set `X` whose point
stabiliser is contained in `ker χ_μ`, where `G = Stab_W(μ)` is the Young subgroup
of `S_6` fixing `μ` and `χ_μ(σ) = Π_{blocks B} sgn(σ|_B)^{[μ_B odd]}`
(`analysis/wk9_s36_stabred.stab_group`).  `χ_μ` is one-dimensional, so
`ℂ[X] = ⊕_O Ind_{G_m}^G 1` gives

>   **`n_χ = ⟨χ_μ, ℂ[X]⟩ = (1/|G|) · Σ_{g ∈ G} χ_μ(g) · |Fix_X(g)|`.**

`|Fix_X(g)|` is computed **without enumerating `X`**: a multiset is `g`-fixed iff
its multiplicity function is constant on the `⟨g⟩`-orbits of `A = exps(3,6)`
(`|A| = 56`), so

>   `|Fix_X(g)| = #{ c ∈ ℤ_{≥0}^{orbits} : Σ_O c_O · w(O) = μ }`,  `w(O) = Σ_{α∈O} α`,

an exact knapsack DP over residual weight vectors (`≤ Π(μ_i+1) ≤ 46 656` states).
Degree is implied by weight, so no second constraint is needed.  The `g = 1` term
is `N_S`.

**This is an exact value, not a bound.**  It is what the board asks for in place
of `N_S/|Stab|`, which `PROVED.md: nchi_2_21_guard` records as neither an upper
nor a lower bound.

### I2 — the decision, by the house engine (unchanged)

`analysis/wk12_s79_per6.measure_weight`, i.e. `wk9_s45_build.build_cell` →
`wk11_s71_hybrid.hybrid_kernel` → `ev_rows_from_coeffs` on `a + 8` `per₃`
pencils (seed 41, bound 40), **both house primes** `2147483647`, `2147483629`;
`rank_p ≤ rank_ℚ`, so `units = a − mult = 0` at **one** prime already proves
`S_μ ∉ I(D_6^{per₃})_{10}` over `ℚ`.  `matmul_mod_wide` where the **actual inner
dimension of the multiplication** reaches `2²¹`, per `nchi_2_21_guard`; the
guard is applied to that dimension and to nothing else.  No engine change is
planned; any that proves necessary is a dated addendum committed before it runs.

## 3. Controls — each stated with the input that must make it fail

| id | control | must fail when |
|---|---|---|
| **C1** | the `g = 1` term of I1 reproduces the banked `N_S` at all 58 open cells **and** at all 48 B13-08 cells and all 296 s79 cells | any error in the monomial-count DP or the weight convention |
| **C2** | I1's `n_χ` equals the **measured** `n_chi` banked by B13-08 (48 cells) and by s79 (`results/s79_per6.jsonl`, all degrees present), field by field | any error in `χ_μ`, in the orbit decomposition, or in the fixed-point count |
| **C3a** | *negative, deliberately wrong input*: re-run I1 with `χ ≡ 1` (the plain orbit count, sign twist dropped).  It **must disagree** with the banked `n_chi` on at least one banked cell | if it agrees everywhere, I1 is insensitive to `χ` and C2 has no teeth |
| **C3b** | *negative*: re-run I1 with `G` replaced by the full `S_6`.  Must disagree with the banked `n_chi` | if it agrees, I1 is insensitive to the group |
| **C3c** | *negative*: perturb one `μ` by one box (weight no longer `3δ`).  I1 must return 0 / raise, not a number | a silent wrong-weight answer |
| **C4** | I1 agrees with the repository's own independent implementation `wk9_s45_build.orbit_setup_arr` (enumerate → canonicalise → twist) on every cell small enough to run it, and with `wk9_s36_stabred.orbit_setup` on the smallest | two implementations sharing no code disagreeing |
| **C5** | **the registered prediction**: for every cell of the 58 that I2 actually builds, I1's `n_χ` is written to `results/b14_09/sizing.json` **before the build starts**, and the builder's measured `n_chi` must equal it | I1 wrong at exactly the cells that matter |
| **C6** | `negative_control_forced` (`PROVED.md`), required on every evaluation-rank sweep: a diagonal `per₃` pencil makes `per₃` a product of three linear forms, whose coordinate ring carries no constituent of more than three rows, so **every length-6 weight must read rank 0** | a rank computation that has stopped computing, or evaluation rows that are not the ones claimed |
| **C7** | B13-08's two banked degree-10 records are reproduced on this container before any new cell is decided: `(11,6,5,3,3,2)` and `(9,8,5,4,3,1)`, field by field on `a`, `N_S`, `|Stab|`, `n_chi`, `mult` at both primes | an engine that behaves differently here than it did there |

C1, C2, C4 are run on data that already exists, so they can fail on arrival.
C3a/b/c are run and their **disagreement is recorded as the PASS condition**.
C6 is run inside every decided cell.

## 4. Decision table

| observation | reading | action |
|---|---|---|
| C1–C7 all pass | instruments sound | proceed |
| **any** control fails | the instrument is wrong | the affected table is **withdrawn**, not patched; report the failure |
| I1 `n_χ` ≠ builder `n_chi` at a built cell (C5) | I1 wrong | withdraw the whole sizing table; report as a failed instrument |
| `units = 0` at either prime | `mult = a`; `S_μ ∉ I(D_6^{per₃})_{10}` over `ℚ` | **PROVED** for that cell; bank and continue |
| `units ≥ 1` at both primes | a candidate **permanent-specific** cubic equation | re-check at `3a + 24` fresh points (seed 907), exhibit the kernel vector, verify `E·v = 0`, **halt the sweep; the verification protocol takes over**.  Report as MEASURED, not promoted |
| primes disagree | arithmetic fault | halt that cell, bank both, report; no characteristic-zero claim |
| build or kernel exceeds the bound | not reached | record `n_χ`, the stage that bound, and the measured cost; **NOT REACHED** |

**`rank_floor` is in force**: a deficient sampled rank is a **ceiling on `i`** and
never establishes `i ≥ 1`.  `complete_interpolation` is not available here (no
proved `dim N = h` for these cells), so no `i ≥ 1` claim is derivable from this
slot by any route, and none will be made.

## 5. Stopping rules

- Every run bounded at launch by `timeout <seconds>` and `ulimit -v`; the pid is
  written to `results/logs/<run>.pid`; a run that must be ended early is ended by
  that recorded id.  No name-pattern matching.
- Memory bound per lane: `ulimit -v 6500000` (6.5 GB) with at most one heavy lane,
  `ulimit -v 3200000` with two.  A cell that trips it is NOT REACHED at that
  bound, and the bound is reported with it.
- Wall-clock bound per cell: 2 400 s for the build-and-decide path; a cell that
  trips it is NOT REACHED and its measured partial cost is reported.
- A control failure stops the sweep at once.
- A `units ≥ 1` reading stops the sweep at once (decision table above).
- The sizing table (Q1) is delivered even if Q2 reaches zero cells.  That is the
  board's stated fallback and it is the floor of this slot, not its goal.

## 6. Labelled expectations, registered before computing

| id | expectation | confidence |
|---|---|---|
| **Q0** | the open set is exactly 58 = 47 (ranks 339, 345–360, 362–391) + 11 (392–402) | 95 % — derived here, checked against B13-08 §0 |
| **E1** | I1 returns all 58 exact `n_χ` in under 15 minutes wall clock total | 85 % |
| **E2** | at every cell with `|Stab| = 1`, `n_χ = N_S` exactly (forced: trivial group) | 99 % |
| **E3** | `n_χ < N_S/|Stab|` at **some** of the 58 with `|Stab| > 1`, and `n_χ > N_S/|Stab|` at **some** other cell of the banked set — i.e. the quotient is neither bound, as `nchi_2_21_guard` says | 80 % on the first clause, 55 % on the second |
| **E4** | B13-08's "17 of 95 exceed `2²¹`" was computed on `N_S/|Stab|`, so the count of the 58 needing `matmul_mod_wide` on **measured** `n_χ` differs from the count the quotient predicts | 70 % |
| **E5** | of the cells I2 reaches, **every one** reads `mult = a` (no drop) | 90 % |
| **E6** | I2 reaches at least 6 of the 58 within the session window | 55 % |
| **E7** | the binding stage on this host is the kernel, not the build (`build_no_longer_binding`) | 70 % |

E5 is the one that matters and it is the one this slot is least able to move: a
drop would be the programme's first permanent-specific equation, and it would
still not be an obstruction.

## 7. What is banked, and where

- `results/b14_09/sizing.json` + `.md` — the 58-cell sizing table (Q1), written
  **before** any build.
- `results/b14_09/controls.json` — C1–C7 with their inputs, outputs and the
  deliberately wrong inputs that made C3a/b/c fail.
- `results/b14_09/per6_d10.jsonl` — one record per decided cell (Q2).
- `results/logs/` — every run log and pid.
- `docs/b14_09_report.md` — the report, every statement labelled.
- Code under `analysis/b14_09_*.py`.  Nothing writes outside `results/`,
  `docs/b14_09_report.md` and `analysis/b14_09_*`.
- The four single-writer files are not touched.

Co-Authored-By: Claude Opus 5 <noreply@anthropic.com>
