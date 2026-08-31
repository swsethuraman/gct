# Session 25 — the ambient cap, applied backwards and forwards

Branch `s25-race`.  2026-08-31.  Cloud container, fresh clone of the public
repo.  Nothing read from or written to `Projects\gct` (rule 9).  Nothing
appended to `PROJECT_NOTES.md` or `docs/boundary_deficit.html`.  All files
added are new.

Deliverables: `results/PREREG_s25.md` (commit `6ca9481`, before any
computation), `docs/ambient_audit.md`, `docs/race.md`, this record.

## 0. Clone state

`origin/main` at clone time: **`3dfd524`** — one commit *ahead* of the
`a3df8ba` the brief expects.  `a3df8ba` is an ancestor and the intervening
commit is "Correct the expected tip in both briefs, and point them at the
screen", so this is a benign fast-forward, **not** a rollback alarm.
`c9240f3` and `ad9502f` are both present, and sessions 24 and 24b are merged
(`61e748e`) — which closes the sync alarm raised in `docs/session_24b.md` §0.

## 1. Results in one line each

* **The 742 are 97.0% forced** — but only 25.2% by `a = 0`.  24.5% are the
  `{Ac, D}` hypersurface-blind pair, 47.3% saturate the ceiling
  `mult_A = mult_B = a`, and 3.0% (22 cells) are genuine.  80.9% of all 742 are
  cancellations between two hypersurfaces, where `D = 0` is an identity between
  plethysm coefficients.  **Retire the saturation law.**
* **All 22 survivors have `mult_A = mult_B = a - 1`**, across four pair-types;
  14 of them are still hypersurface pairs.
* **The paper's base point is ambient arithmetic.**  `def_det((2,2,2),2) = 1`
  is forced by `a((2,2,2),2) = 0`.  Forced fractions of the determinant's total
  deficit: **100%, 83.3%, 80.6%** at `delta = 2, 3, 4`.
* **`m_det >= a` at all 664 ambient-support weights computed** (`n=3` to
  `delta=8`, `n=4` to `delta=5`, `n=5` to `delta=4`), worst margin exactly 0.
  The ratio **rises** in `delta` and in `n`; the tie fraction falls in `n`.
* **But the pointwise inequality provably fails eventually.**
  `Sigma_a ~ delta^{A-1}` against `Sigma_m ~ delta^{d-1}` with `A-1 = 164`
  against `d-1 = 64` at `n = 3`.  The no-go is **bounded-range**, and must be
  written as one.
* **The padded problem at `(4,3)` is dead below `delta = 4`**; the row bound
  `ell <= m^2+1` is not binding, and `m_det >= a` throughout.
* **A correction to `docs/easy_counts.md`**: all 36 weights at `(5,2)` with
  `m_det = 0` have `a = 0`, so `def_per = m_per` there is ambient arithmetic,
  not BIP.

## 2. Prediction ledger

| | prediction | outcome |
|---|---|---|
| S1 | forced fraction of the 742 = 55%, range 40–70% | **REFUTED** — 25.2%, below my range (the integrator's 40–75% is refuted the same way) |
| S2 | `forced + empty >= 90%`, `substantive < 5%` | **REFUTED, and badly** — `empty` is exactly 0 and the naive `substantive` bucket is 74.8%.  My reasoning ("nothing was present at either weight") was wrong: things *were* present, and equal.  The 97% figure comes from two mechanisms I had not thought of when I registered |
| S3 | `m_det / a` **falls** with `n` | **REFUTED** — it rises, at every `delta` I reach.  The integrator's prior is refuted with mine |
| S4 | no `m_det < a` at `n = 4, 5` in reach; but it must exist eventually, first at a weight with `a >= 2` and `m_det = 1` | **first clause CONFIRMED** (zero half-free weights anywhere); **second clause upheld and upgraded to a proof** via the dimension count; **third clause UNTESTED** — no such weight was reached |
| S5 | `delta = 2` is `m_det = a = 1`, a tie, for every `n` | **CONFIRMED** at `n = 3, 4, 5` |
| S6 | paper audit 100% forced at `delta = 2`, above 80% at all three | **CONFIRMED** — 100.0, 83.3, 80.6 |
| S7 | most of the 34 `(5,2)` weights have `a = 0`, so BIP is not doing the work | **CONFIRMED, unanimously** — 36 of 36 |

Three refutations (S1, S2, S3), all kept.  S2 is the instructive one: I
predicted the zeros were vacuous because nothing was there, and the data says
the opposite — the closures usually *both* carried the full ambient
multiplicity.  Saturation at the ceiling is a real mechanism and it is the
largest single bucket; neither the brief nor I anticipated it.

## 3. Verification

Every routine written fresh before the screen was consulted.

| quantity | route 1 | route 2 | external |
|---|---|---|---|
| `chi^lam(rho)` | rim-hook removal on the diagram (mine) | full column orthogonality `S_1..S_8` | 0 disagreements with `ambient_screen.chi` over all `(lam,rho)` through `S_8` |
| `a(lam,delta)` | power-sum plethysm + character pairing | `sum_lam a dim S_lam = dim Sym^delta(Sym^d C^N)` at 8 different `(delta,d,N)` | brief's `n=3` stratification at `delta = 2..6`; `(9,4,2)` unique at `delta = 5` |
| World A `a` | plethysm | Gaussian-binomial difference (box DP) | 0 disagreements over all 221 weights; `27 / 60 / 134` split reproduced |
| `m_det` | symmetric rectangular Kronecker | — | sums `3, 11, 43` and supports `3, 10, 34`; the `delta = 2` row; `g((9,4,2),5^3,5^3) = 3` |
| World A closure tables | rederived from scratch | committed `wk5_s24_worldA.py` | **0 disagreements in 1568 cells**; and `1292` / `742` reproduced exactly |

Structural gates, all passing: `def >= 0` and **`mult <= a`** at every World A
cell (the cap itself, asserted rather than assumed).

Two bugs of mine, both caught by calibration before any result formed: a
trailing-zero mismatch in the ambient lookup (which manufactured a false
disagreement with the brief's `27 of 221`), and a compositions-for-partitions
DP.  Recorded in `docs/ambient_audit.md` §1.

## 4. Consequences the programme should absorb

1. **Strike the saturation law from the open problems.**  `docs/ambient_audit.md`
   §6 gives the honest ground: 80.9% of the zeros are hypersurface-vs-
   hypersurface, where the multiplicity function is determined by the ambient
   and one (degree, weight) pair.
2. **Reframe, do not retract, `c((2,2,2),2) = 1`.**  The conductor is a
   stabilisation index along the `Phi_18`-ray; what the audit removes is the
   claim that its base point is evidence about the determinant's boundary.  The
   paper should say where it introduces the datum that `a((2,2,2),2) = 0`.
3. **Correct `docs/easy_counts.md`** on the BIP attribution (§8 of the audit).
4. **State the no-go with its range.**  `docs/race.md` §4.  An unqualified
   no-go would repeat exactly the error the audit is correcting.
5. **The screen should record `a >= 2` as the live gate and `mult = a` as a
   second forced case.**  `must_have_room` currently rejects `a = 0`; the
   ceiling mechanism (47.3% of the 742) is invisible to it.

## 5. Files added

    results/PREREG_s25.md            pre-registration, committed first
    docs/ambient_audit.md            question A: forced vs genuine, paper audit
    docs/race.md                     question B: m_det vs a, and question C
    docs/session_25.md               this record
    analysis/wk6_s25_core.py         fresh MN / Kronecker / m_det / plethysm
    analysis/wk6_s25_calib.py        the brief's calibration battery
    analysis/wk6_s25_worldA.py       World A tables, rederived
    analysis/wk6_s25_audit.py        the 742, classified
    analysis/wk6_s25_paper.py        paper + easy_counts audits
    analysis/wk6_s25_race.py         the race
    analysis/wk6_s25_crossover.py    the dimension count
    analysis/wk6_s25_padlive.py      the padded live locus

Pure Python, exact integers and `Fraction`.  No engine, no checkpoints, no
closure geometry.  Whole session well under an hour of compute.

## 6. What a successor should do first

1. **Push the race in `delta`, not in `n`.**  `n` makes it worse.  At `n = 3`
   the ambient support is still only 371 weights at `delta = 8`; `delta = 9, 10`
   are reachable and are the only direction in which the half-free profile can
   appear.
2. **Bound `Sigma_m` rigorously** so the crossover degree becomes a computed
   number rather than an existence proof.  A usable upper bound on
   `sum_lam m_det dim S_lam` would convert `docs/race.md` §3 from "it must
   happen" into "it must happen by `delta = X`".
3. **Re-audit World B** the same way.  The ternary-cubic corpus has never been
   screened against its ambient `Sym^delta(Sym^3 C^3)`, and the 254
   deficit-positive weights are the obvious next target.
4. **Check the `mult = a - 1` pattern.**  All 22 survivors sit at it.  If that
   is a theorem about Gaussian-binomial differences, the residue closes
   completely and the audit becomes exhaustive rather than 97%.
