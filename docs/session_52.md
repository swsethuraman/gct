# Session 52 — the `a = 1` census: the BIP gate resolved, and the prior's benefit shown void

2026-09-05.  Branch `s52-aone` off `eb8cecb` (`work/`'s `main`, which no bundle in
`Projects\gct` contained — the three newest bundles `s47-exactness 4b8047d`,
`s48-theorems ec2d3c9`, `s46-balanced bb47bbf` are all ancestors of it).
Delivered as **`aone.bundle`**, single ref `refs/heads/s52-aone`, prerequisite
`eb8cecb`, verified and confirmed to fast-forward `main`.  Pre-registration
`results/PREREG_s52.md` at `45137c0`, before any computation.  Nothing pushed.

**The laptop dropped off the bridge before write-back**, so the bundle was
delivered into the conversation rather than copied into `Projects\gct`.  The
ancestor test was re-run mid-session and passed (`work/`'s `main` still
`eb8cecb`, no other writer).  It must be re-run before the bundle is applied.

## Verdict

> **Task 0 resolved: the BIP mechanism does not transfer to `n = 4`, and the
> failure is a gap in the *length* of weight the argument can see, not a gap in
> constants.**  Deliverable `docs/bip_transfer.md`, the companion to
> `docs/dip_transfer.md`.
>
> **The census is complete over `δ = 7, 8, 9, 10`, and the integrator's counts
> reproduce exactly.**  `results/s52_census.md`.
>
> **17 `a = 1` cells measured, `i_det = 0` at every one**, including the
> programme's **first `δ = 10` cells**.  With the 193-cell reconciled record the
> six-row determinant ideal is now empty at **208 measured cells** across
> `δ = 6..10`.  `results/s52_ledger.md`.
>
> **The `a = 1` prior's stated benefit is void on the current record** — §3.
> This is the finding that should change what a later session does.

## 1. Task 0 — BIP at `n = 4`

Theorem 1.4 (arXiv v3) = 1.5 (v1) needs `n ≥ m^25`; `3^25 = 847,288,609,443`
against `n = 4`, so the theorem is silent.  Reading confirmed against the paper.

The mechanism, taken apart (every hypothesis quoted; `analysis/wk9_s52_bipreach.py`
only evaluates them at small `n`, which the paper never does):

* **Thm 2.5**, the entire supply of determinant-side points, is the padded power
  sums `X^{n−s}(φ_1^s+···+φ_k^s)` with `n ≥ sk`.  At `n = 4` there are exactly
  **eight**, every one a **product of four linear forms** over `C`, every one of
  **linear span ≤ 3**.
* **Lemma B (proved, one line):** a weight vector of weight `λ` vanishes at every
  point of linear span `< ℓ(λ)`.  So at `n = 4` the whole supply is *identically*
  blind to every weight of the census, which is at `ℓ(λ) = 6`.
* Prop. 2.3 + semigroup reaches `ℓ(λ) ≤ 3`; Prop. 2.4/5.1 needs `md² ≤ n`, vacuous
  for `δ ≥ 3`; Prop. 5.2 reaches `ℓ(λ) ≤ 4`, hooks only; Prop. 5.5 needs
  `n ≥ 24m^6 = 1536`.  Best reach at `n = 4`: **`ℓ(λ) ≤ 4`**.
* Least `n` reaching a six-row weight: **9**, hooks only — and **not one of the
  150 `a = 1` eligible cells is a hook** (`λ_2` runs 2..12), so even that case
  covers nothing here; the real requirement is `n ≥ 9λ_2² ∈ [36, 1296]`.
* **Measured** at three banked six-row cells, both primes: the HWV is zero at all
  eight BIP points and at a generic product of four linear forms, non-zero at a
  `det_4` pencil, at `ℓ·c` and at the true padded permanent, in one run.
* **One piece transfers and is already ours:** Kadish–Landsberg's `|λ̄| ≤ mδ` is,
  at `(4,3)`, exactly `λ_1 ≥ δ` — our obstruction-eligibility gate, confirmed
  from outside the programme.
* Flagged, not claimed: [KL]'s `ℓ(λ) ≤ m² = 9` is sharper than
  `docs/sixrow_frontier.md`'s `ℓ ≤ 10`; if it transfers to the length-reduced
  model the permanent-visible window closes one row earlier.

## 2. The census (`results/s52_census.md`)

| `δ` | eligible | units | `a = 1` | share | `h_pad = 0` (dead) | informative |
|---|---|---|---|---|---|---|
| 7 | 258 | 954 | 64 | 24.8% | 9 | 55 |
| 8 | 591 | 10,054 | 45 | 7.6% | 10 | 35 |
| 9 | 1,079 | 86,363 | 24 | 2.2% | 2 | 22 |
| 10 | 1,793 | 653,974 | 17 | 0.95% | 0 | 17 |
| **all** | **3,721** | **751,345** | **150** | **4.0%** | **21** | **129** |

`δ = 7, 8` reproduce the integrator exactly; `δ = 9` reproduces s43's 1,079 /
86,363 exactly.  The definitional risk was real — `a = 1` among *all* `ℓ = 6`
cells is 67 / 57, not 64 / 45.

**Lemma A** (proved before the census ran): at `a = 1`, `h_pad < a ⟺ h_pad = 0`,
and `h_pad = 0 ⟹ mult_red = 0 ⟹ mult_pad = 0 ⟹ D ≤ 0` with no measurement.  So
the informative cells are exactly `h_pad ≥ 1`.

**Enumeration.**  `amb(10,4,6)` does not fit the container (3.9 GB, then ended by
the kernel, empty log; the cost is the Murnaghan–Nakayama memo over the ~37,000
partitions of 40).  The Weyl alternation restricted to the eligible cells does
the same census in **202 s inside 3 GB** — the brief's "better enumeration, not a
longer bound".  `δ = 10` therefore covers eligible cells only.

## 3. The finding that should change the next session

`D = i_det − i_pad`, and `results/sixrow_record.md` has `mult_det = a` at **all
193** cells, i.e. `i_det = 0`, i.e. `U_D = {0}` everywhere measured.  A zero
subspace has no orientation, so the failure mode the `a = 1` prior protects
against — `dim U_D = dim U_P` with `U_D ≠ U_P` — **is not instantiable anywhere
in the record**.  The protection is void; the cost (giving up the strictly
stronger of the two obstruction notions, per Dörfler–Ikenmeyer–Panova) is paid
immediately.

**Recommendation.**  Retire `a = 1` as a selection principle until a cell with
`i_det ≥ 1` exists.  The successor test is the direct containment `U_D ⊆ U_P`,
which refutes `P_6 ⊆ D_6^{det_4}` whenever it fails, is strictly stronger than
`D > 0`, works at every `a`, and costs nothing beyond what a measured cell
already produces.

A second cost, specific to `δ ≤ 8`: s43 and s47 proved `I(D_6^{per_3})_7 = 0` and
`I(D_6^{per_3})_8 = 0`, so `mult_pad = mult_red` there and any `D > 0` would be
permanent-**insensitive**.  The 22 `δ = 9` and 17 `δ = 10` `a = 1` cells are the
first in this census where that is not excluded by a theorem.

## 4. The measurements (`results/s52_ledger.md`)

17 cells: 3 at `δ = 7`, 1 at `δ = 9`, 13 at `δ = 10`; `n_χ` from 200 to 65,778;
`mult_det = mult_pad = 1 = a`, `D = 0`, at every one.  No `D > 0`, so the
verification protocol was never entered.  Every determinant verdict is a *proof*:
exact kernel at both primes (dense route) or a single-prime non-singularity
certificate (sparse route, one-sided by `rank_p ≤ rank_Q`).

**Re-measurement gate** passed: the smallest, median and largest by `n_χ` of the
six banked `δ = 7` `a = 1` rows of `results/s36_aone.md` re-measured from
scratch, every field identical.  The work list was re-derived by re-parsing the
six banked ledgers, and the same parser reproduces the reconciled record exactly
(193 cells, 16/70/67/40).

**Two engineering findings worth keeping.**

1. **The cheap `a = 1` cells at `δ ≤ 9` are gone.**  Entering the session, every
   unmeasured informative `a = 1` cell at `δ ≤ 9` already had an `n_χ` estimate
   above 15,000; the four measured here (estimates 15,594 to 64,614) exhaust the
   affordable remainder, and **the cheapest still unmeasured sits at 92,217**.
   The cheap ones are at `δ = 10`, which the programme had never touched: 13 of
   its 17 sit below `n_χ = 17,000`, the smallest at 200.
2. **Session 45's sparse route is worse than the dense route on small cells, not
   merely unnecessary.**  At `(30,2,2,2,2,2)_10`, `n_χ = 200`, it reached 4.6 GB
   and was ended by the kernel after 317 s (build 1 s at 0.07 GB, so the cost is
   in the evaluation/compression stage); the dense exact route did the same cell
   in **3.3 s at 0.09 GB**.  Crossover used here: `n_χ ≈ 20,000`.

## 5. Pre-registration scorecard

P1 (BIP does not transfer, 0.85) **confirmed**, more sharply than logged.
P2, P3 (258/64, 591/45, 0.80 each) **confirmed exactly**.
P4 (`δ = 9` inside 30 min, 0.85) **confirmed**, 273 s.
P5 (`δ = 10` completes, 0.55) **confirmed, but not by the assumed route**.
P6 (`a = 1` share < 5% at `δ = 9`, 0.70) **confirmed**, 2.2% then 0.95%.
P7 (≥ half the `a = 1` cells dead, 0.45) **refuted** — 9/64, 10/45, 2/24, 0/17.
P8, P9, P10 **confirmed**.

## 6. Honest boundary

61 of the 129 informative `a = 1` cells remain, none cheap at `δ ≤ 9`; four
`δ = 10` cells remain (estimates 115k, 131k, 737k, 2.7M).  `δ ≥ 11` was launched
and ended by its recorded process id after 100 of 2,902 cells — the enumeration
runs ascending in `λ_1` and the `a = 1` cells are at the far end, so a partial run
carries no rate; affordable in a session that starts with it.  At `δ = 10` there
is one cross-check fewer (`a` by the Weyl route only).  `mult_red` on the sparse
rows is forced by `mult_pad ≤ mult_red ≤ a = 1`, not measured, and is marked `1*`.

## 7. Corrections

* `docs/s52_prompt.md` §0 points at `brief_wording.md` **§6** for the
  degeneracy-direction pre-check; it is **§5** (§6 is the citation corrections,
  §7 the functoriality check).  Both checks are answered in the pre-registration.
* `n_χ = ⌈N_S/|Stab|⌉` is an estimate, not a bound (s46).  Measured against it
  this session: `(14,5,3,2,2,2)_7` estimate 24,971, measured 30,037.
* `PROJECT_NOTES.md` was not edited (single writer).  Its "Sync state" still names
  session 19 as owner and its roadmap R1–R7 predates the whole `n = 4` programme.
