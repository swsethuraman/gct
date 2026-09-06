# Pre-registration — session 60: the balanced length-5 cells, by the sparse route

Branch `s60-balanced5` off `main` at `0960bd5` (the tip of both the public clone
and the laptop's `work/` at session start; `origin/main` on the laptop points at
the same commit).  Written and committed **before any multiplicity is computed**.
The only computation that precedes this file is a re-reading of the repository;
the census (§2) runs after this commit and its predicted shape is registered
below so that it can be scored.  Labels in the report: **proved** / **measured**
/ **adopted-from-literature** / **expectation**, per `docs/brief_wording.md`.

Standing constraints of the brief are in force: delivery by git bundle, no
push; single-writer files untouched; `Co-Authored-By` trailer only; every long
run bounded by `timeout` and `ulimit -v` with its process id in
`results/logs/<run>.pid` and ended only by that id; logs under `results/logs/`;
no committed file over 5 MB; `python-flint` for every dense rank; both house
primes `2147483647, 2147483629` wherever a prime is used; every `D > 0` cell
through the verification protocol before it is written as a claim; certificates
in `gct-cert/1` through `tools/verify/`.

## 0. The question, and why length 5 is the clean case (proved inputs)

`D_5 := D_5^{det_4} = closure{det_4(Σ s_i A_i)} ⊆ Sym^4 C^5` (dim 50),
`R_5 = {ℓ·c}` (dim 39) — washout Cor. 7.  At `r = 5`, `P_5 = R_5`
(washout Thm 2) so `mult_pad = mult_red` (washout Thm 3(1)) and any `D > 0`
here is a genuine `D = mult_red − mult_det > 0` with **no transfer gap**.
By functoriality (`docs/brief_wording.md` §7, row 1),

    R_5 ⊆ D_5  ⟹  I(D_5) ⊆ I(R_5)  ⟹  C[D_5] ↠ C[R_5]  ⟹  mult_red ≤ mult_det

at every cell, so **one length-5 cell with `mult_red > mult_det` refutes
`R_5 ⊆ D_5`** (T1 of `results/PREREG_s54.md`), and only length exactly 5 can
(T2).  Session 54 found `mult_det = mult_red = a` at every reachable cell
through `δ = 9`, but reached only the skewed weights (`nb ≤ 2500`); 88, 224,
423 and 696 balanced cells were skipped at `δ = 6, 7, 8, 9`.  This session
measures that complement, both sides, as far as the budget allows.

## 1. The instruments (all inherited and validated; nothing new is proved here)

Fix a cell `(λ, δ)`, `ℓ(λ) = 5`, `n = 4`.  `V_χ` is the `χ_λ`-isotypic
reduction of the `λ`-weight space (`docs/stabiliser_reduction.md`;
`HWV_λ ⊆ V_χ` proved), `dim V_χ = n_χ`, and `E` the stacked simple raising
operators on `V_χ` (`analysis/wk9_s45_build.py`, unchanged, at `r = 5`;
`dim ker_Q E = a`, the plethysm value).

**Determinant side.**  `mult_det = a − dim ker_Q[E; ev_1; …; ev_K]` with `ev_j`
the evaluation at a random `det_4` pencil in χ-coordinates, `K = a + 8`
(`docs/sparse_det_route.md` Lemma 1).  Since `rank_p ≤ rank_Q`,
**`nullity_p([E; ev]) = 0` at one prime proves `mult_det = a` over `Q`**
(Lemma 2); a positive nullity is a measurement until its kernel is exhibited and
verified.  The nullity is decided by the session-42 Wiedemann certificate
(`analysis/wk9_s42_wied.c`, unchanged) with the evaluation rows pinned
(session 45), levels `(3,2) → (12,2) → full`, both primes concurrently.

**Reducible side, two instruments, both recorded at every cell where both are
affordable.**

- **(★), point-free (proved, `docs/reducible_ideal.md` Thm 1).**
  `HWV_λ ∩ I(R_5) = ker E ∩ span M_red`, `M_red` the weight-`λ` monomials with,
  for every `i ∈ [5]`, a factor `c_α` with `α_i = 0`; `M_red` is `Stab`-stable
  so a χ-column is entirely red or entirely non-red.  Hence
  `mult_red = a − nullity_Q(E_red)`, `E_red = E` restricted to the red columns,
  and **`nullity_p(E_red) = 0` at one prime proves `mult_red = a`** by the same
  Lemma 2.  No points enter.
- **Points (the brief's instrument).**  `mult_red = a − dim ker_Q[E; ev'_1; …; ev'_K]`
  with `ev'_j` the evaluation at a random reducible point `ℓ(s)·c(s)`, `ℓ` a
  random linear form and `c` a random quinary cubic, drawn as in
  `analysis/wk9_s54_measure.py`.

At `r = 5` the two must agree exactly whenever the points are generic (KC2
below); the (★) value is the one written in the `mult_red` column when only one
is affordable, and the ledger says which instrument produced each entry.

**Routes by `n_χ`, not by habit (brief §3, s52's crossover finding).**
Below a dense cap `D_CAP` the cell is done by the dense route
(`analysis/wk9_s41_kernel.py` semantics: the exact HWV kernel by `python-flint`
at both primes, `rank(R) = n_χ − a` asserted, `mult_det` and `mult_red` from the
explicit basis by points and by (★)); above it by the sparse certificates.
`D_CAP` is set by a calibration run on s54's own cells and on the smallest
unmeasured ones **before the sweep starts**, and is recorded in
`results/s60_calibration.md` together with the s52 small-cell pathology
(whether the sparse route's memory blow-up at tiny cells reproduces at `r = 5`,
and if so where it comes from).  Expectation: `D_CAP` between 3,000 and 8,000.

**Order.**  Cells are measured in ascending order of the cost key
`n_χ² · (a + 30)` (one Wiedemann sequence costs `≈ 4·n_χ·nnz_c` element
operations with `nnz_c ≈ (11 + K)·n_χ` on the determinant side), informative
cells (§2) before dead ones, and within a session budget of about eight hours
of wall clock for the sweep.

## 2. The census (runs after this commit; predictions registered now)

`analysis/wk9_s60_census.py` scores every length-5 cell with `a > 0` at
`δ = 6..9` that s54 did not measure, plus every length-5 cell at `δ = 10`,
with `a` (s54's plethysm value re-derived by the Weyl alternation and asserted
equal), `h_pad` (`mult_red ≤ h_pad`, proved), `N_S = nb`, `|Stab|`, `n_χ`
(exact where cheap, else `⌈N_S/|Stab|⌉` flagged), and the classification

- **informative**: `h_pad ≥ 1` — a refutation is not excluded by a theorem;
- **dead**: `h_pad = 0` — `mult_red = 0` is forced (Corollary B for
  `λ_1 < δ`, Corollary B2 in general), the cell cannot refute `R_5 ⊆ D_5`, and
  only its determinant side is a measurement (it still bears on the onset of
  `I(D_5^{det_4})`).

| id | prediction about the census | prior |
|---|---|---|
| C1 | the complement counts are exactly 88 / 224 / 423 / 696 at `δ = 6/7/8/9` (s54's own skipped counts) | 0.95 |
| C2 | at every degree fewer than 25 % of the unmeasured cells are dead (`h_pad = 0`) | 0.60 |
| C3 | the cheapest unmeasured informative cell at every degree has `n_χ ≤ 5000` | 0.85 |
| C4 | the largest `n_χ` in the complement is `~10^5` at `δ = 6` and `≥ 10^6` at `δ = 9` | 0.70 |
| C5 | `a` by the Weyl alternation agrees with s54's census at every one of the 1487 cells | 0.97 |

## 3. Predictions about the measurements

| id | prediction | prior |
|---|---|---|
| M1 | **no measured cell has `mult_red > mult_det`** (the necessary condition for `R_5 ⊆ D_5` holds on everything reached) | 0.85 |
| M2 | `mult_det = a` at every measured cell — the determinant ideal of `D_5^{det_4}` stays empty at every balanced length-5 cell reached (the onset expectation, `docs/onset_conjecture.md`) | 0.80 |
| M3 | at every informative measured cell with `h_pad ≥ a`, `mult_red = a` | 0.60 |
| M4 | at least one informative measured cell has `h_pad < a` (so `mult_red < a` by theorem there, `D < 0` if M2 holds) | 0.55 |
| M5 | (★) and the `ℓ·c` points agree at every cell where both are computed | 0.95 |
| M6 | both primes agree at every cell | 0.97 |
| B1 | at least 60 % of the `δ = 6` complement is measured, both sides | 0.70 |
| B2 | at least 25 % of the `δ = 7` complement is measured, both sides | 0.50 |
| B3 | fewer than 10 % of the `δ = 9` complement is measured | 0.75 |
| B4 | at least five `δ = 10` length-5 cells are measured, both sides | 0.50 |
| B5 | the s52 small-cell pathology of the sparse route does **not** reproduce at `r = 5` below `n_χ = 3000` in this pipeline | 0.50 |

If M1 fails the session is about that one cell (§5) and B1–B4 are void.

## 4. Stopping rules and re-check discipline

- **Halt on `mult_red > mult_det`** at any cell (both primes): the sweep stops;
  the verification protocol takes over (§5).  Nothing else in the batch matters
  more than getting that cell right.
- **`mult_det < a` at a cell** (determinant nullity `k ≥ 1` at both primes): the
  first non-empty determinant ideal the programme would have seen at `r = 5`.
  Independent re-check before it is banked: the `k` kernel vectors exhibited,
  checked against the **full** `[E; ev]` at both primes, re-derived at a fresh
  seed, fresh preconditioner and fresh points (`3a + 24` pencils), and shown to
  vanish at 20 fresh determinant pencils built independently.  Then the reducible
  side at that cell by both instruments.  If `mult_red ≤ mult_det` the sweep
  continues; if `mult_red > mult_det` the halt rule applies.
- **`mult_red < min(a, h_pad)` at a cell** (a reducible bite beyond the
  normalisation bound): the independent re-check (fresh seeds, both primes) and
  the (★)/points cross-check before banking; no halt (this is consistent with
  containment).
- **KC1 (calibration).**  The instrument reproduces s54's measured values
  (`mult_det = mult_red = a`, both primes) on a sample of its cells at each
  degree, by both routes where both apply.  A mismatch stops the session until
  it is understood.
- **KC2 (self-consistency).**  Dense route: `rank(R) = n_χ − a` at both primes
  and (★) `=` points.  Sparse route: the two primes agree; any kernel candidate
  is checked against the full matrix before it counts.  A disagreement between
  (★) and points at a cell is itself a finding (degenerate points or a bug) and
  is resolved before the cell is banked.
- **Budget.**  A cell whose run exceeds its `timeout` is banked as DEFER with
  its sizes and named as the frontier; the sweep proceeds to the next cell.

## 5. Verification protocol for a `mult_red > mult_det` cell (copied, s41/s43)

`a` by both routes (plethysm and kernel); `mult_det` and `mult_red` re-derived at
`3a + 24` points and a second prime; the determinant-side kernel vector(s)
exhibited (χ-coordinates expanded to the monomial basis), lifted to integer
vectors where affordable, shown zero at 20 independently built `det_4` pencils
and nonzero at 20 independently built reducible points `ℓ·c` **and** at 20
true padded-permanent points `x_0·per_3` restricted to five variables (the
committed three-point set of `docs/brief_wording.md` §5, with (2) and (3) both
required to be nonzero for a refutation); `mult_det` re-derived by a second,
independently written implementation (the dense flint route where `n_χ` allows,
else the s41 compressed route); everything into `docs/OBSTRUCTION_CANDIDATE.md`
with this file cross-referenced; certificates (`hwv` kind with `vanishes_at`
determinant points and `nonvanishing_at` reducible points, and `full_rank`
where applicable) through `tools/verify/`; the session ends there.  The
integrator re-derives before the word is used.

## 6. The two pre-checks of `docs/brief_wording.md`

**§5 (degeneracy direction).**  No new statistic is introduced: the instrument
is the coordinate-ring multiplicity.  Any candidate separating covariant
(a determinant-side kernel vector) is evaluated at the committed three-point
set — a `det_4` pencil, a generic `ℓ·c`, the ten-variable `x_0·per_3` — and is
a refutation only if it vanishes at (1) and at neither (2) nor (3); a vector
vanishing at (3) but not (2) would be the "(2) and (3) disagree" case and is
reported as such, not as a refutation.

**§7 (functoriality).**  Coordinate-ring multiplicities are functorial in the
right direction under closed immersion (row 1 of the table): `R_5 ⊆ D_5` forces
`mult_red ≤ mult_det` cell by cell, so `mult_red > mult_det` refutes containment.
The (★) instrument is the same multiplicity computed point-free (Thm 1 of
`docs/reducible_ideal.md`), not a different invariant.

## 7. Certificates and what the verifier can and cannot check

`gct-cert/1` has the kind `full_rank` for `mult_X(λ, δ) = a`: the verifier
recomputes the highest-weight space when `N_S ≤ 3000` and otherwise needs a
recorded basis.  So: every dense-route cell gets `full_rank` certificates for
`det_pencil` and for `reducible` (both primes when `N_S ≤ 3000`; one prime with
the mod-`p` basis recorded when `N_S > 3000` and the file stays well under the
5 MB limit), all run through `tools/verify/verify.py` with a report committed.
The sparse route never computes the kernel, so its `mult = a` proofs are the
algorithmic single-prime nonsingularity certificates (Lemma 4 of
`docs/sparse_det_route.md`), reproducible from the seeds in the ledger but
**not representable in `gct-cert/1`**; the report states, cell by cell, which
proofs the independent verifier covered and which rest on the Wiedemann
certificate alone.  This is registered as a known gap, not discovered after
the fact.

## 8. Deliverables

`results/s60_census.{json,md}`, `results/s60_calibration.md`,
`results/s60_cells.jsonl` (raw, one record per cell per side, appended as
banked), `results/s60_ledger.md` (one row per cell, both sides, instrument and
proof status named), certificates under `results/certs/s60/` with the verifier
report `results/s60_verify.md`, `docs/s60_report.md` with the skipped/measured
counts stated per degree and the cheapest unmeasured cell named with its
`n_χ`, logs under `results/logs/s60_*`.  Delivered as the single-ref bundle
`s60_balanced5.bundle` (prerequisite `0960bd5`).  Note for the integrator: the
history rewrite of `docs/history_rewrite.md` has been prepared but not run; if
it runs before this bundle is applied, the prerequisite hash changes and the
branch must be replayed (`git format-patch`/`am` or `rebase --onto`) rather
than fetched from the bundle.
