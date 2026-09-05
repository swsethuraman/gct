# Session 52 — the `a = 1` census: where the statistic is lossless, and what that costs

Branch `s52-aone` off `eb8cecb` (`main`).  Pre-registration `results/PREREG_s52.md`,
committed at `45137c0` **before any computation of the session**.  Deliverables:
`docs/bip_transfer.md` (Task 0), `results/s52_census.md`, `results/s52_ledger.md`,
`analysis/wk9_s52_*.py`, logs under `results/logs/s52_*`.  Labels **proved** /
**measured** / **adopted-from-literature** / **expectation** throughout.
Delivered as a bundle; nothing pushed.

---

## 0. Verdict

> **Task 0 is resolved: the BIP mechanism does not transfer to `n = 4`, and the
> reason is structural rather than numerical.**  Its entire supply of
> determinant-side evaluation points at `n = 4` is eight padded power sums, every
> one a product of four linear forms with linear span at most 3; a weight vector
> of weight `λ` vanishes identically at every point of span `< ℓ(λ)`; the census
> is at `ℓ(λ) = 6`.  The machinery's length reach at `n = 4` is `ℓ(λ) ≤ 4`, and
> the least `n` at which it reaches a six-row weight is `n = 9` — for hooks only.
> The census therefore proceeds, as the brief directs.
>
> **The census is complete over `δ = 7, 8, 9, 10` and the integrator's counts
> reproduce exactly.**  `δ = 7`: 258 eligible, 64 with `a = 1`.  `δ = 8`: 591,
> 45.  New: `δ = 9`, 1079 eligible / 86,363 units, 24 with `a = 1`; `δ = 10`,
> 1793 eligible / 653,974 units, 17 with `a = 1`.  The `a = 1` share of the
> eligible cells falls 24.8 → 7.6 → 2.2 → 0.95 per cent.
>
> **Every cell measured this session has `i_det = 0`, `D ≤ 0`.**  The record
> gains the programme's first `δ = 10` cells.
>
> **The honest finding the brief asked for, and it cuts against the brief's own
> premise.**  The `a = 1` restriction is sold as protection against the
> orientation problem — `D = 0` hiding `U_D ≠ U_P`.  **That failure mode cannot
> occur anywhere in the current record**: `i_det = 0` at all 193 cells of
> `results/sixrow_record.md` means `U_D = {0}` at every one, so `U_D ⊆ U_P`
> holds trivially and there is no orientation to discard.  The protection is
> void until the determinant ideal is first observed non-empty at a measured
> cell; the cost — giving up the strictly stronger of the two obstruction
> notions — is paid immediately.  On the current record the `a = 1` prior is a
> net loss, and it becomes a net gain exactly when `i_det ≥ 1` first appears.

---

## 1. Task 0 — the BIP determination

Full argument, with every quoted hypothesis and its version numbering, in
**`docs/bip_transfer.md`**.  In brief:

**(a) The reading is confirmed.**  Theorem 1.4 (arXiv v3) = Theorem 1.5 (v1):
*"Let `n, d, m` be positive integers with `n ≥ m^25` and `λ ⊢ nd`. If `λ` occurs
in `C[Z_{n,m}]`, then `λ` also occurs in `C[Ω_n]`."*  At `(n,m) = (4,3)`,
`3^25 = 847,288,609,443` against `n = 4`.  Silent, by eleven orders of
magnitude.  The paper's only remark on the bound is *"One can likely improve the
bound on `n` by a more careful analysis"*; it says nothing about small `n`.

**(b) The mechanism does not transfer.**  BIP's positive half is three
propositions, each of which certifies non-vanishing of a highest weight vector
on `Ω_n` by evaluating it at a point supplied by their Theorem 2.5, the padded
power sums `X^{n−s}(φ_1^s + ··· + φ_k^s)` with `n ≥ sk`.  At `n = 4`:

| BIP tool | hypothesis | at `n = 4` |
|---|---|---|
| Thm 2.5 (the point supply) | `n ≥ sk` | 8 shapes, **linear span ≤ 3**, all products of four linear forms |
| Prop. 2.3 + semigroup | `n ≥ kℓ`, `ℓ` even | `ℓ(λ) ≤ 3` |
| Prop. 2.4 / 5.1 | `md² ≤ n` | **vacuous for `δ ≥ 3`** |
| Prop. 5.2 | `m²s² ≤ n` | `ℓ(λ) ≤ 4`, hooks only |
| Prop. 5.5 | `n ≥ 24m^6 ≥ 1536` | **vacuous** |

**Lemma B (proved, one line).**  A weight vector of weight `λ` vanishes at every
point whose linear span has dimension `< ℓ(λ)`.  *(Torus element trivial on the
span; the weight character is a positive power of the scaling.)*

So at `n = 4` every highest weight vector of weight `λ` with `ℓ(λ) ≥ 4` vanishes
at **every** point BIP's Theorem 2.5 supplies.  **Measured** at three banked
six-row `a = 1` cells, both primes (`analysis/wk9_s52_bippoints.py`): the
exhibited highest weight vector is zero at all eight BIP points and at a generic
product of four linear forms, and non-zero at a `det_4` pencil, at `ℓ·c` and at
the true padded permanent, in the same run.  `N_S` and `n_χ` reproduce
`results/s36_aone.md` exactly at all three.

**(c) Why this is essential and not technical.**  The padding exponent `n − m`
is 1 at `(4,3)`.  Kadish–Landsberg allow a body of relative size `m/n = 3/4`;
BIP work where it is `≤ m^{−24} ≈ 10^{−12}`.  And `n = 4 < 9 = m²`, so the
permitted length already exceeds the determinant's own size, while every engine
needs `n` to *exceed* the length it must see.

**(d) One piece does transfer, and it is already ours.**  BIP's only input about
the padded permanent is Kadish–Landsberg's `|λ̄| ≤ md`, which at `(n,m) = (4,3)`
reads `λ_1 ≥ δ` — numerically identical to the programme's own
obstruction-eligibility gate (Corollary B of `docs/reducible_ideal.md`), derived
in-house from the reducible model.  An independent confirmation of the gate from
outside the programme.

**(e) The cost, stated plainly (brief §2.2).**  At `a = 1` a multiplicity
obstruction *is* an occurrence obstruction, so the restriction gives up exactly
the strength gap Dörfler–Ikenmeyer–Panova established.  Their setting is the
Chow variety against bounded border Waring rank, not determinant against padded
permanent, and **they do not state the multiplicity-one observation** — it is
one line from their definitions and is claimed here as ours, not attributed to
them.

---

## 2. What the `a = 1` prior buys, and what it costs

### 2.1 Lemma A, proved before the census ran

At `a = 1`:  `h_pad < a ⟺ h_pad = 0`, and `h_pad = 0 ⟹ mult_red = 0 ⟹
mult_pad = 0 ⟹ i_pad = 1 ⟹ D ≤ 0`, with no measurement.  So the **informative**
`a = 1` cells are exactly those with `h_pad ≥ 1`, and `D > 0` at an `a = 1` cell
requires the pad ideal *empty* (`mult_pad = 1`) and the determinant ideal *full*
(`mult_det = 0`) at the same weight.  This is the brief's instruction to mark and
exclude `h_pad = 0` cells, in the form it takes at `a = 1`; it also means the
exactness question session 47 refuted cannot arise here, since
`mult_red ≤ h_pad = 0` forces equality with no computation.

### 2.2 The stated benefit is void on the current record

The brief's argument for `a = 1` is that a multiplicity obstruction can fail for
a reason unrelated to closeness: `dim U_D = dim U_P` with `U_D ≠ U_P` gives
`D = 0` although the ideals differ.  True in general.  But `D = i_det − i_pad`,
and `results/sixrow_record.md` reports `mult_det = a` at **all 193** measured
six-row cells, i.e. `i_det = 0` at every one, i.e. `U_D = {0}` at every one.  A
zero subspace has no orientation: `U_D ⊆ U_P` holds trivially, `D = −i_pad ≤ 0`
by construction, and the failure mode the `a = 1` prior protects against is not
instantiable anywhere the programme has measured.  It becomes instantiable
exactly when `i_det ≥ 1` is first observed — which is the six-row onset, and is
what sessions 41–48 have been bracketing.

**Recommendation to the integrator:** the `a = 1` restriction should not be used
as a selection principle again until a cell with `i_det ≥ 1` exists.  When one
does, the right test is not `a = 1` but the direct subspace containment
`U_D ⊆ U_P`, which refutes `P_6 ⊆ D_6^{det_4}` whenever it fails and is
strictly stronger than `D > 0` at every `a`.  That test costs nothing beyond
what a measured cell already produces — both kernels are exhibited — and it does
not require `a = 1`.

### 2.3 A second cost, at `δ ≤ 8` specifically

Session 43 proved `I(D_6^{per_3})_7 = 0` and session 47 proved
`I(D_6^{per_3})_8 = 0`, so by Prop. 8(1) of `docs/transfer_lemma.md`,
`mult_pad = mult_red` at **every** weight of degree 7 and 8.  Hence at every
`δ = 7, 8` cell of this census a positive `D` would equal `mult_red − mult_det`
and would be an obstruction for the pair `(R_6, D_6^{det_4})` — permanent-
insensitive in the sense of `docs/dip_transfer.md` Theorem 2.  **The `δ = 9` and
`δ = 10` `a = 1` cells are the first in this census where a permanent-specific
`D > 0` is not excluded by a theorem**; there are 22 and 17 of them.

---

## 3. The census

Full tables in `results/s52_census.md`.  Region fixed in the pre-registration
before any run: `n = 4`, `r = 6`, `ℓ(λ) = 6` exactly, obstruction-eligible iff
`λ_1 ≥ δ`.  `a` by two independent routes asserted equal at every `a = 1` cell
and a sample of the rest; `h_pad` by two routes on a sample of the `a = 1` cells;
`N_S` by the generating-function DP.

| `δ` | eligible cells | ambient units | `a = 1` eligible | share | `h_pad = 0` (dead, Lemma A) | **informative** |
|---|---|---|---|---|---|---|
| 7 | 258 | 954 | 64 | 24.8% | 9 | **55** |
| 8 | 591 | 10,054 | 45 | 7.6% | 10 | **35** |
| 9 | 1,079 | 86,363 | 24 | 2.2% | 2 | **22** |
| 10 | 1,793 | 653,974 | 17 | 0.95% | 0 | **17** |
| **all** | **3,721** | **751,345** | **150** | **4.0%** | **21** | **129** |

**Reproduction gate (P2, P3): both hit exactly.**  258 / 64 at `δ = 7` and
591 / 45 at `δ = 8` — the integrator's counts, independently obtained, and the
`δ = 7, 8` eligible counts and unit totals also match `results/sixrow_census.md`.
The definitional risk the priors were hedging against was real: `a = 1` among
*all* `ℓ = 6` cells is 67 and 57, not 64 and 45, so the counts refer to `a = 1`
among the **eligible** cells.  The `δ = 9` census reproduces session 43's
independently obtained 1,079 cells / 86,363 units exactly.

**`δ = 9` (P4) and `δ = 10` (P5) both completed, but not by the same route.**
The Frobenius-plethysm route `amb(δ,4,6)` does `δ = 9` in 273 s; at `δ = 10` it
was launched under `ulimit -v 6.3 GB`, reached 3.9 GB resident and was ended by
the kernel with no traceback (`results/logs/s52_census10.log` is empty), the cost
being the unbounded Murnaghan–Nakayama memo over the ~37,000 partitions of 40.
The brief asked for a better enumeration rather than a longer bound: restricting
to the obstruction-eligible cells up front (1,874 partitions rather than every
`ℓ = 6` partition of 40) and scoring each by the Weyl alternation with
non-negativity pruning over a per-cell tail DP finishes the same census in
**202 s inside 3 GB**.  The `δ = 10` row therefore covers the eligible cells
only; its `λ_1 < 10` onset-only cells were not enumerated and are not counted.

**P6 confirmed and sharper than logged.**  The `a = 1` share falls monotonically
`24.8 → 7.6 → 2.2 → 0.95` per cent, so the `a = 1` route thins out fast in the
degree axis.  **P7 refuted:** the `h_pad = 0` dead fraction is 9/64, 10/45, 2/24,
0/17 — the informative fraction is high and rising, not low.

---

## 4. The measurements

Full rows in `results/s52_ledger.md`.

**Re-measurement gate** (pre-registration §5, fixed before any new cell): the
smallest, median and largest by `n_χ` of the six banked `δ = 7` `a = 1` rows of
`results/s36_aone.md` — `(18,2,2,2,2,2)` `n_χ = 190`, `(14,8,3,1,1,1)`
`n_χ = 928`, `(17,4,2,2,2,1)` `n_χ = 2614` — re-measured from scratch by the
exact route: **every field identical**, `a`, `N_S`, `n_χ`, `|Stab|`, `mult_det`,
`mult_pad`, `mult_red`.  Session 45's sparse route separately reproduced
`(14,8,3,1,1,1)` before it was used anywhere.

**The work list, re-derived rather than inherited.**  `analysis/wk9_s52_todo.py`
subtracts the already-measured cells by re-parsing the six banked ledgers
themselves; the same parser reproduces the reconciled six-row record exactly —
**193 `ℓ = 6` cells split 16 / 70 / 67 / 40 over `δ = 6, 7, 8, 9`**, which is
`results/sixrow_record.md`'s table on the nose.  Of the 129 informative `a = 1`
cells, 51 already have a `mult_det`; 78 do not.

**The cost finding that reshaped the session.**  The brief's premise — "these
are also our cheapest cells" — is true of the `a = 1` region as a whole and
false of what is *left* in it at `δ = 7, 8, 9`: every unmeasured informative
`a = 1` cell at those degrees has `n_χ ≳ 15,000`, and all but one `≳ 24,000`,
i.e. at or beyond session 41's dense frontier.  Sessions 36, 41, 43, 45 and 46
took the cheap ones already.  **The cheap `a = 1` cells are at `δ = 10`**, which
the programme has never touched: 13 of its 17 have `n_χ < 16,000`, the smallest
`n_χ = 200`.

**Routes.**  Below `n_χ ≈ 20,000` the dense route (`analysis/wk9_s41_cell.py`,
exact kernel, both primes, `mult_red` by (★)); above it session 45's sparse
Wiedemann certificate, where `nullity_p = 0` at one prime *proves* `mult = a`
over `ℚ` — at `a = 1` exactly the brief's cheap direction.  An engineering note
worth banking: **the sparse route is not merely unnecessary on small cells, it is
worse.**  At `(30,2,2,2,2,2)`, `δ = 10`, `n_χ = 200`, it reached 4.6 GB and was
ended by the kernel after 317 s (`rc = −9`, build itself 1 s at 0.07 GB), while
the dense exact route finished the same cell in **3.3 s at 0.09 GB**.  The
crossover is a property of the evaluation/compression stage, not the build.

<!--MEASUREMENTS-->

---

## 5. Pre-registration scorecard

<!--SCORECARD-->

---

## 6. Honest boundary

<!--BOUNDARY-->

---

## 7. Corrections and notes for the integrator

1. **The brief's pointer is off by one section.**  `docs/s52_prompt.md` §0 says
   "the degeneracy-direction pre-check in `docs/brief_wording.md` §6"; in the
   committed file that check is **§5**, §6 is the two citation corrections and
   §7 is the functoriality pre-check.  Recorded in the pre-registration §0; both
   §5 and §7 are answered in pre-registration §6 and in §4 above.
2. **`ℓ(λ) ≤ m² = 9` versus the `ℓ ≤ 10` window.**  `docs/sixrow_frontier.md` §1
   records the permanent-visible window as `6 ≤ ℓ(λ) ≤ 10`, the 10 being the
   support count `1 + m²` of `x_0·per_3(x_1..x_9)`.  Kadish–Landsberg's
   companion bound is `ℓ(λ) ≤ m² = 9`, which is sharper.  The two are stated for
   different objects and this session does not settle whether [KL] transfers to
   the length-reduced model; if it does, `ℓ = 10` is empty and the window closes
   one row earlier.  Flagged, not claimed — it does not arise at `ℓ = 6`.
3. **`n_χ = ⌈N_S/|Stab|⌉` is an estimate, not a bound** (session 46's
   correction).  This session's census tables label that column `n_χ ~` and the
   ledger carries the measured `n_χ`; the two differ by up to 21% in either
   direction, and the ordering of the work list is by the estimate, so a cell's
   true cost can be above or below its place in the queue.
4. **The `a = 1` prior should be retired as a selection principle** until a cell
   with `i_det ≥ 1` exists — §2.2 above.  The successor test is `U_D ⊆ U_P`,
   which is available at every `a` and is strictly stronger than `D > 0`.
5. `results/PROJECT_NOTES.md` and the two single-writer papers were not edited.
   `PROJECT_NOTES.md`'s "Sync state" section still names session 19 as the owner
   and its roadmap R1–R7 predates the whole `n = 4` programme; that is an
   integrator matter, not a correction this session is entitled to make.
