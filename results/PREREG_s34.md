# Pre-registration — session 34: `delta = 7` at `ell >= 5` (`n = 4`), the census and the first probe

Written **before** any computation.  Branch `s34-d7`, 2026-09-01.

**Clone state.**  Fresh clone; `origin/main` at **`29bea5f`** (the integrator's
s30 review).  `git merge-base --is-ancestor 29bea5f HEAD` passes (ancestry, not
equality — here HEAD *is* `29bea5f`).  No session claiming number 34 exists
anywhere in the repository (no `*_s34_*` files, no s34 branch or commit) — no
collision to flag.  Sessions 30, 31, 32 and the s21/s32 merges are in; there is
no session 33 on `main`.

**Environment.**  `python-flint` 0.9.0 freshly installed; `nmod_mat.rank()`
verified on a toy matrix.  2 cores.  `MemAvailable` at prereg time: **7.6 GB**
(MemTotal 8.2 GB, cgroup limit effectively unbounded).  **Usable budget for
this session's feasibility line: 7.2 GB** (measured MemAvailable minus 0.4 GB
for interpreter and OS overhead outside the matrices).  s30's 6.5 GB reference
budget is *also* tabulated in the census so the two frontiers can be compared.

**Single-writer files, untouched by this session:** `paper/det3-conductor.tex`,
`PROJECT_NOTES.md`, `docs/boundary_deficit.html`.  Delivery is a git bundle of
the single ref `s34-d7`; no pushes.

---

## 0. Conventions, restated verbatim so they cannot drift

The corrected raising rule throughout (s30's, witness-guarded):

    E_ij . c_alpha  =  (alpha_i + 1) . c_{alpha + e_i - e_j}

**The interpretation rule, pre-registered verbatim:**

> Convention, stated so it cannot drift: `D := mult_pad − mult_det`.  An
> obstruction is `D > 0` — the padded permanent strictly exceeding the
> determinant at a weight.  `D < 0` (the pad side biting first) is the expected
> direction — pad's variety is smaller (39 < 50), so its ideal should switch on
> earlier — and it is **not** an obstruction.  A `D < 0` cannot be upgraded
> into a claim it is not.  A first pad-side bite is still informative (it dates
> the pad ideal's onset) and goes in the ledger as the byproduct it is.

**The gate** (two conditions, `scripts/ambient_screen.py::must_have_room`
semantics adapted to `(n, delta) = (4, 7)`): `|lam| = 28`, `ell(lam) >= 5`,
`a(lam, 7) >= 2`.  Structural note to be verified in the census: every weight
of `Sym^7(Sym^4)` has `ell(lam) <= 7` (a product of seven one-row shapes), so
the census range is `ell in {5, 6, 7}`; the enumeration nevertheless runs to
`maxrows = 16` (s30's setting) and the emptiness of `ell >= 8` is asserted,
not assumed.

**Forms.**  `det_4` (16 variables) vs `x_0`-padded `per_3` (10 variables),
exactly `wk8_s30_core.det_form(4)` and `per_padded(3, 4)`.

---

## 1. Entry calibration, pre-committed order (all before anything new is trusted)

1. **The witness** (kill criterion): binary quartics, `closure{l^3 m}`,
   `lam = (4,4)`, `delta = 2` — `mult = 0`, kernel `∝ (12, −3, 1)`.  The wrong
   rule gives `mult = 1` and kernel `(1, −4, 3)`.  Any deviation → **stop, and
   nothing is measured**.
2. **`analysis/wk8_s30_calib.py`, run as-is.**  All five parts must pass.  The
   World A battery is quoted as its **discriminating ratio — expected 41 of
   48** — never the bare pass count (a battery is evidence only through the
   parts that could have failed).  Any failure → stop.
3. **Re-certification of three of s30's banked cells**, chosen by this
   deterministic rule, fixed here before any of them is run:

   - Take the 34 banked rows of `results/sweep62_ledger.md` in file order
     (9 re-certified + 25 measured), 0-indexed.
   - `H := SHA-256("s34-recert-2026-09-01")` as an integer; `L = 34`;
     `step = floor(L/3) = 11`.
   - Indices `(H + k·step) mod L` for `k = 0, 1, 2` → **13, 24, 1**.

   The three cells this rule picks, with the ledger rows they must reproduce
   **exactly** (every field: `ell`, `a`, `N_S`, `mult_det`, `mult_pad`, `D`):

   | idx | lam | ell | a | N_S | mult_det | mult_pad | D |
   |---|---|---|---|---|---|---|---|
   | 13 | (13, 4, 4, 2, 1) | 5 | 2 | 3199 | 2 | 2 | +0 |
   | 24 | (9, 8, 5, 1, 1)  | 5 | 2 | 5159 | 2 | 2 | +0 |
   | 1  | (13, 5, 4, 1, 1) | 5 | 2 | 1824 | 2 | 2 | +0 |

   Code path for the re-certs: `wk8_s30_core.measure` with `a_expect` from the
   plethysm, det seed 11, pad seed 29, `bound = 40`, default `npts = a + 8` —
   the exact call pattern of `wk8_s30_run62c.py`, at `delta = 6`.

---

## 2. Pre-registered predictions

**P1 — the three re-certs reproduce the s30 ledger exactly.**  Confidence:
high.  *Regime:* these three cells, this container, s30's exact code path.
*Falsifier:* any field of any of the three differing.  *Kill:* any deviation →
**stop everything** — the pipeline is not the one s30 ran, and nothing this
session could measure would be interpretable.

**P2 — the modal outcome at `delta = 7` is uniform `D = 0` again: every
measured cell returns `mult_det = mult_pad = a`, both ideals still empty in
every gated component reached.**  Committed choice between the brief's two
alternatives: **uniform `D = 0`, not first bites.**  Reasoning:

- *The pad side has no dimension pressure at `delta = 7`.*  The s30-P4 count
  extended one degree: restriction of ambient degree-`delta` forms to the
  parameter space `C^5 × C^35` of `D_5^pad = closure{l · c}` lands in the
  bidegree-`(delta, delta)` polynomials.  At `delta = 7`:
  `C(76,7) ≈ 2.19e9` ambient against `C(11,7)·C(41,7) ≈ 7.42e9` — no forced
  kernel, by a factor ~3.4.  The crude count first forces a kernel at
  **`delta = 13`** (`4.46e14 > 3.35e14`).  Forcing is sufficient, not
  necessary, so the onset may be earlier — but nothing *pushes* it below 13.
- *The `n = 3` analogue at `r = 5` bites late relative to its codimension.*
  `D_5` for cubics has codimension 6, and its ideal is invisible at every
  measured length-5 weight through `delta = 7`, with `delta_0 >= 8` given the
  published deficit sequence (`docs/d5_ideal.md` §4–5).  The `n = 4` codims at
  `r = 5` are larger (20 and 31), which argues for an earlier onset than the
  `n = 3` case *in codimension units* — but `delta = 7` is only one degree past
  a sweep (s30's) that found not a single near-miss in 34 cells: every rank
  attained `a` with no instability on either prime.
- *s30's verdict mechanism.*  The uniform emptiness at `delta = 6` was read as
  "below the onset of both ideals at `r = 5`"; one degree is the smallest
  possible step, and the cells this budget reaches are the same lopsided,
  small-`a` end where emptiness has been most robust.

Confidence: **moderate** — deliberately not high: the onset must exist
(39 < 50), every degree probed is a fresh chance to hit it, and this programme
has died three times by carrying a pattern out of its regime.
*Regime:* the cells within this container's budget at `delta = 7` — by the
census forecast these are the small-`N_S` (lopsided to moderately balanced)
cells, expected `ell` mostly 5 — and **nothing beyond**: not the balanced or
`ell = 6, 7` deep cells outside the budget, not `delta >= 8`.
*Falsifier:* any measured cell with `mult < a` on either side that survives
the sceptical branch (§5).

**P3 — if any side bites at any measured cell, the pad side bites first**:
at the first cell in sweep order showing either side `< a`, it is `mult_pad <
a` with `mult_det = a` (i.e. `D < 0`).  Reasoning: codimension 31 vs 20 at
`r = 5`; the crude forcing degree is 13 for pad and nowhere in range for det
(the det parametrisation through `(C^16)^5` has DOF that dwarf the ambient at
every degree in reach); and the det ideal at `r = 4` is already known to start
at `e >= 6` with the Lüroth analogy suggesting much later — the det side is
the *slow* side on every count.  Confidence: moderate-high, conditional.
*Regime:* conditional on a bite among the cells this session measures; says
nothing about which side bites first in the unreachable region or at higher
degree.  *Falsifier:* first bite on the det side, or both sides biting at the
same first cell.

Note the deliberate asymmetry: a pad-side bite **falsifies P2 while confirming
P3** — the two predictions cannot absorb each other's outcomes, and a `D < 0`
row is banked as the onset-dating byproduct the interpretation rule (§0) says
it is, nothing more.

---

## 3. Phase 1 — census commitments (a deliverable in itself, before any sweep)

- Enumerate all cells at `(n, delta) = (4, 7)`, `|lam| = 28`, via the plethysm
  route (`wk8_s30_pleth.amb(7, 4, 16)`), gate `ell >= 5` and `a >= 2`
  (`must_have_room` semantics, `need = 2`); assert no weight with `ell >= 8`
  carries `a > 0`.
- Per cell: `a` (plethysm), `N_S = len(monomials(4, ell, 7, lam))`, balance
  `lam_1 − lam_ell`, predicted memory **`5.6e-8 · N_S^2` GB** — s30's measured
  constant from its largest completed cell (their conservative `7.5e-8` fit
  overdrew the frontier by one cell; the review's flag (a) endorses `5.6e-8`).
- Feasibility line: which cells fit within **7.2 GB** (this container), with
  the **6.5 GB** (s30 reference) frontier alongside; totals by `a` and by
  balance.  Published as `results/d7_census.md` and committed **before any
  cell is measured**.
- If nothing fits, the census and feasibility map **is** the session; deliver
  honestly and stop.

## 4. Phase 2 — the sweep order, exact and deterministic

Let `F` be the feasible set from the census (predicted GB ≤ 7.2).

- `ASC` = `F` ascending by `N_S`, ties by descending lexicographic `lam`.
- `PROBE` = `F` sorted by (`a` descending, balance ascending, `N_S` ascending,
  ties by descending lexicographic `lam`) — s30's probe key: the largest-`a`,
  most-balanced cells first.
- The order is s30's interleave, verbatim: repeatedly take the next **3**
  unvisited cells from `ASC`, then **1** unvisited from `PROBE`, until `F` is
  exhausted.
- Two workers may run concurrently through the claim queue (§6); the union of
  their streams realises the same commitment — ascending for coverage plus a
  deliberate early pass over the largest-`a` / most-balanced cells the budget
  reaches — so the representativeness falsifier is genuinely exposed, not
  nominally (s30's P4 discipline).  Above `N_S ≈ 6000`, one worker at a time.
- **Representativeness commitment:** the largest-`a` cell(s) of `F` and the
  minimum-balance cell(s) of `F` *will be measured*, not merely scheduled —
  subject only to the memory guard's honest defer, which if it fires is banked
  and reported as "attempted, deferred (memory)", never as a measurement.
- If wall-clock runs out before `F` is exhausted, coverage is reported as a
  fraction of cells and of ambient units, s30-style, with the interleave
  guaranteeing both ends of the axis are represented early.

**Code path, fixed in advance:** the sweep runs `wk8_s30_fast.cell` (s30's
fast path: `R` built once per cell, shared by both forms, sparse matrix
construction, *all* rows used — subsampling stays rejected), with `a_expect`
from the plethysm, seeds det 11 / pad 29, `bound = 40`, `npts = a + 8`,
primes 2147483647 and 2147483629.  `fast.cell` draws evaluation points with
the same `random.Random(seed)` stream as `core.measure`, so its outputs are
definitionally identical to the banked s30 path; the re-certs (§1.3) still use
`core.measure` itself so the comparison to s30's ledger is path-exact.
If the observed peak-RSS constant on the first ≥ 5 completed cells fits below
`5.6e-8`, cells beyond the pre-registered frontier may be attempted **after
`F` is exhausted**, banked in the same ledger flagged `EXT`, and reported as
an extension beyond the pre-registered frontier — never silently mixed in.

## 5. Per-cell discipline (s30's, unchanged)

- `a` by two independent routes — raising-operator kernel dimension and
  plethysm — must agree (`a_expect` asserted in the measuring code).
- `rank(R) = N_S − a` asserted at every cell, both primes.
- Ranks over the two word-size primes via `python-flint` `nmod_mat.rank()`;
  **no hand-rolled elimination** (two sessions' self-tests have failed at it).
- Both `mult_det` and `mult_pad` per cell; a rank attaining `a` is a
  certificate (`rank_p <= rank_Q <= a`).
- **Sceptical branch** (either side below `a`): re-run at 3× evaluation points
  (`npts = 3a + 24`), both primes, fresh seed (907), and the kernel vector
  exhibited (`want_U`).  Only then does the bite enter the ledger.
- Every row banked to `results/d7_ledger.md` (append + fsync at completion)
  and committed by the driver at each poll cycle — exposure to a container
  reset is at most one poll interval, and no number is used anywhere before it
  is committed.

## 6. `D > 0` is STOP-EVERYTHING (the obstruction protocol, in full)

No further cells.  Then, in order: (i) both `a`-routes agree at the cell;
(ii) both multiplicities re-derived at 3× points on a second prime, fresh
seed; (iii) the det-side kernel vector exhibited and evaluated **nonzero at
three explicit padded pencils** — substitutions of `x_0`-padded `per_3` — a
vector claimed to separate must be shown to separate; (iv) everything into
`docs/OBSTRUCTION_CANDIDATE.md`, cross-referenced to this prereg, and the
session ends there.  The integrator re-derives independently before anyone
uses the word obstruction.

## 7. Kill criteria, complete list

1. Witness failure → stop; nothing is measured.
2. Any calibration part failing → stop.
3. Any deviation in the three re-certs → **stop everything**: the pipeline is
   not the one s30 ran.
4. `D > 0` → the §6 protocol, then the session ends.
5. Memory: the census already bounds honesty.  The in-sweep guard **waits, it
   does not skip**; a census-feasible cell that still cannot start after the
   guard's patience with the container quiet is banked "attempted, deferred
   (memory)" — a "would not start" is never quoted as a measurement.
6. Prime disagreement on any rank, `a`-route disagreement, or
   `rank(R) ≠ N_S − a` → the cell is not banked; investigate; unresolved →
   stop and report.

## 8. Engineering commitments (inherited, not rediscovered)

- Multi-worker **only** via s30's claim-queue design (`wk8_s30_run62c.py`,
  `wk8_s30_reconcile.py`): claims in `results/claims_d7/` via
  `O_CREAT|O_EXCL`, PID-owned, a claim released only when its owner is dead;
  existence pre-check **before** the memory gate; reconcile before any worker
  restart.
- Memory guard: predicted `5.6e-8 · N_S^2` GB against `MemAvailable`, headroom
  0.85 single-worker / 0.70 two-worker; the guard blocks and re-polls (waits);
  patience 40 × 30 s, then honest defer (§7.5).
- Kill only by explicit PID, read back from the claim or worker log first —
  never `pgrep -f`/`pkill -f` (self-matching has now cost two sessions).
- New code lands as `analysis/wk9_s34_*.py`; nothing in `analysis/wk8_*` is
  edited.

## 9. Deliverables

`results/PREREG_s34.md` (this file, committed first), `results/d7_census.md`,
`results/d7_ledger.md`, `results/s34_calibration.md` (witness + battery +
re-certs, banked), `docs/d7_sweep.md` (house style: proved / measured /
expectation, each labelled; honest boundary; coverage as a fraction of cells
and of ambient units), code as `analysis/wk9_s34_*.py`, and the bundle
`d7.bundle` (single ref `s34-d7`).
