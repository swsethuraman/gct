# `delta = 7` at `ell >= 5` — the census, then the sweep: still before the onset

Session 34, branch `s34-d7`.  Clone tip `29bea5f`; ancestry verified.
Pre-registration: `results/PREREG_s34.md`, committed before any measurement.
Census: `results/d7_census.md`, committed before any sweep.
Per-cell record: `results/d7_ledger.md`.  Calibration: `results/s34_calibration.md`.

**Verdict in one line.**  *(measured)*  Every cell measured at `delta = 7`
returns `mult_det = mult_pad = a` — both ideals are still **empty** in every
isotypic component this container can reach — so the onset degree of both
ideals at `r = 5` is now dated **above 7** on the reachable range, one degree
deeper than session 30 left it; the census (a deliverable in itself) shows the
gate exploding from 71 cells at `delta = 6` to **433 cells / 2708 ambient
units**, of which this container could measure the `ell = 5` cheap-to-middle
tier.  Pre-registered P2 (uniform `D = 0`) confirmed on every measured cell;
P3 (pad bites first) remains untested — nothing bit.

---

## 1. What was asked, and what the answer turned on

Session 30 closed `delta = 6` by argument: both ideals empty in every measured
component, and the dimension table (`50` vs `39` inside `dim Sym^4 C^5 = 70`)
forcing *some* degree to separate the two varieties.  Its verdict — "the axis
is the degree, not the weight" — made `delta = 7` the next gate, and this
session is the first probe of it.  The pre-registered interpretation rule
(PREREG §0, verbatim from the brief): `D := mult_pad − mult_det`; an
obstruction is `D > 0` **only**; `D < 0` is the *expected* direction (the pad
variety is smaller, 39 < 50, so its ideal should switch on earlier) and is
not an obstruction but an onset date.  Neither direction materialised: at
`delta = 7`, on everything measured, both ideals are still switched off.

## 2. Entry calibration — all green before anything new was trusted

*(measured, and pre-committed in order)*  The witness (binary quartics,
`closure{l^3 m}`, `lam = (4,4)`, `delta = 2`) gives `mult = 0` with kernel
exactly `(12, −3, 1)`; `analysis/wk8_s30_calib.py` run as-is passes all five
parts, with the World A battery quoted as its discriminating ratio — **41 of
48** cells where `mult < a`, the parts a wrong rule could have failed; and the
three s30 cells picked by the pre-registered hash rule (ledger rows 13, 24, 1:
`(13,4,4,2,1)`, `(9,8,5,1,1)`, `(13,5,4,1,1)`) re-certify **EXACT** on every
field, on s30's own code path.  P1 confirmed; kill criterion 3 never fired.
Details and logs: `results/s34_calibration.md`.

## 3. The census — the deliverable the degree axis now needs

*(measured — enumeration, two independent routes per number)*  At
`(n, delta) = (4, 7)`, `|lam| = 28`, the two-condition gate (`ell >= 5`,
`a >= 2`) passes **433 cells carrying 2708 units of ambient multiplicity** —
against 71 cells / 189 units at `delta = 6`.  The strata: `ell = 5/6/7` =
210/194/29 cells.  `a` was computed by two independent plethysm
implementations (`wk8_s30_pleth.amb` and `scripts/ambient_screen.stratify`),
agreeing on all 433; `N_S` by an exact DP cross-checked against the sweep's
own basis enumeration on all 87 cells with `N_S <= 30000`; no weight of
`ell >= 8` carries ambient room (asserted, as `Sym^7(Sym^4)` forces).

The feasibility line (census §1, at `5.6e-8 · N_S^2` GB against this
container's 7.2 GB): **46 cells / 258 units fit — 10.6% of cells, 9.5% of
units** — and everything feasible has `ell = 5`.  The `ell = 6` stratum
starts at ~24 GB (`(16,5,2,2,2,1)`, `N_S = 20850`); the most balanced cells
(balance 4) sit at ~10^6 GB; the largest-`a` cell anywhere (`a = 26`,
`(12,8,5,2,1)`) needs ~38 GB.  The reachable frontier of each axis inside the
budget: `a` up to 15, balance down to 10, `N_S` to 11269.

## 4. Discipline actually applied at every cell

- `a` by two independent routes (raising-operator kernel dimension vs
  plethysm), asserted equal at every cell; `rank(R) = N_S − a` asserted on
  both primes; `N_S` asserted equal to the census DP value.
- Ranks over the two word-size primes (2147483647, 2147483629) via
  `python-flint 0.9.0` `nmod_mat.rank()`; no hand-rolled elimination.
- Measurement path: `wk8_s30_fast.cell` — `R` built once per cell and shared
  by both forms, all rows used — with s30's seeds (det 11 / pad 29), `bound
  40`, `npts = a + 8`; identical point streams to the banked s30 path.
- A rank attaining `a` is a certificate.  The sceptical branch (3× points,
  fresh seed, kernel exhibited) **was never entered: no cell came in below
  `a` on either side.**
- Every row banked with fsync as it completed and committed within minutes;
  claims via the s30 claim-queue (`O_CREAT|O_EXCL`, PID-owned, reconciled
  before restarts); memory guard waits, never skips; kills only by explicit
  PID after read-back.

## 5. The sweep

*(tables generated from the ledger by `analysis/wk9_s34_report.py`, not typed)*

The pre-registered order was kept: ascending `N_S` interleaved 3:1 with
probes of the largest-`a` / most-balanced cells, realised across workers by
the claim queue.  The regime falsifier was genuinely exposed, early: the
**`a = 15`** cell `(15,6,4,2,1)` — the largest ambient multiplicity reachable
at this degree — was the 4th slot of the master order, and the `a = 14`,
`a = 13`, `a = 11` probes and the most balanced feasible cell
(`(11,11,4,1,1)`, balance 10) were all measured, not merely scheduled.

<!--GEN:TABLE-->
<!--/GEN:TABLE-->

## 6. Coverage, and the boundary of what was reachable

<!--GEN:COVERAGE-->
<!--/GEN:COVERAGE-->

**The memory story, told plainly.**  The census frontier was drawn at s30's
measured constant `5.6e-8 · N_S^2` GB.  The fast measurement path peaks lower
— the largest completed cells fit `~3.2–3.4e-8` (e.g. 4.22 GB at
`N_S = 11158`) — so the in-sweep guard (census constant, 0.85 headroom
against `MemAvailable`, which tops at ~7.2 GB in this container) honestly
**deferred** the five predicted-`>= 6.1` GB cells; each defer is banked as a
`DEFER-MEM` row, never quoted as a measurement.  After the rest of the
feasible set was exhausted, those cells were re-admitted under the observed
constant (`3.5e-8`, PREREG §4's post-exhaustion rule) in fresh single-cell
processes, and their completed rows follow their defer rows in the ledger.
A `DEFER-MEM` row followed by a measured row is that sequence, in the open.

**What was not reached, stated plainly.**  Everything outside the 46: the
whole `ell = 6, 7` strata (223 cells), every cell with balance `<= 9`, and
every `a > 15` cell — including the census's `a = 26` summit.  The strongest
honest statement about that region is that it is **untested** — not that it
agrees.  The reason to *expect* agreement there is structural (the same
degree-counting that dates both onsets above `delta = 7` has nothing to do
with the weight's shape), but that is an **expectation** and is recorded as
one, exactly as s30's balance-`<= 6` caveat was.

## 7. What this does to the picture

- *(measured)*  Both ideals at `r = 5` are empty in every measured isotypic
  component at `delta = 7`.  With s30, the onset bracket at `r = 5` is now
  `delta_onset >= 8` **on the measured range** — lopsided-to-mid `ell = 5`
  weights, `a <= 15`, balance `>= 10` — for both `D_5^det4` and `D_5^pad`.
- *(measured)*  P2 confirmed at every cell; P3 untested (no bite anywhere);
  the pad ideal's onset date, which a first `D < 0` would have provided, is
  still open.
- *(proved elsewhere, unchanged here)*  The dimension sandwich (50 vs 39)
  still forces some degree to separate the varieties; s32's Theorem 5 forces
  set-level difference in the obstruction-relevant direction.  Nothing in
  this session strengthens or weakens either; no measurement here contradicts
  anything on the record.
- *(expectation, labelled as such)*  The s30-P4 degree-count extended to
  `delta = 7` says the pad side has no dimension pressure until much later
  (the crude forcing degree is 13; PREREG §2), and the `n = 3` analogue at
  `r = 5` (codim 6) is invisible through `delta = 7` with `delta_0 >= 8`.  On
  that reasoning the expectation is more empty degrees before the pad ideal
  switches on, with the det ideal later still — but every degree probed is a
  fresh chance to be wrong, which is why P2's confidence was set at moderate
  and why the falsifiers were named.

## 8. Recommendation

1. **Do not sweep more weights at `delta = 7` in this container class.**  The
   reachable tier is measured; the next marginal cell tests the same
   structural statement again.
2. **`delta = 8` at `ell = 5` is affordable and scoped** *(post-hoc scoping,
   not pre-registered — enumeration only, `results/d8_scope.json`)*: the gate
   there is 1569 cells / 24964 units, of which ~46 cells (317 units) fit this
   container class, starting at `N_S = 1527` (`(22,5,2,2,1)`) — the cheap end
   of `delta = 8` costs no more than the cheap end of `delta = 7` did.  The
   degree axis can be walked at least one more step by exactly this session's
   playbook.
3. **The `r = 4` onset number `e` is still the cheap calibrator** (s30 review
   §4b, literature-first: the Lüroth-hypersurface analogy) — one number that
   bounds where the `r = 5` det onset can start, and it shapes whether
   walking `delta = 8, 9, ...` is the right spend at all.
4. **A ~40 GB box changes the game more than another degree.**  At 38 GB the
   `delta = 7` census admits the `a = 26` summit `(12,8,5,2,1)` and the
   `delta = 8` gate admits 79 cells / 847 units; the balanced `delta = 6`
   corner s30 flagged (`(8,8,4,2,2)`, ~38 GB) fits the same box.  One memory
   upgrade retires the honest-boundary caveats of three sessions at once.

---

*Engineering note for the record: the claim-queue + PID-read-back discipline
inherited from s30 ran three worker generations and two finish passes with
zero claim races and zero pattern-kills; the one scheduling intervention
(retiring an idle worker whose 0.70-headroom gate could never admit the
giants) was done by explicit PID after verifying it held no claim.  Full
worker logs are in `results/s34_worker_*.log` and `results/s34_finish*.log`.*
