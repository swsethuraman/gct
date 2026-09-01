# Session 30 — the 62 at `delta = 6`, `ell >= 5`

Branch `s30-sweep62`.  Clone tip `13fb170`; ancestry verified (`13fb170` is an
ancestor of the tip, checked by ancestry and not by equality).
Findings: `docs/sweep62.md`.  Pre-registration: `results/PREREG_s30.md`.
Per-cell record: `results/sweep62_ledger.md`.

## 1. What was asked and what came back

Sweep the 62 open cells at `n = 4`, `delta = 6`, `a >= 2`, `ell >= 5` (the 71
minus session 27's nine) under the **corrected** raising rule, after a
mandatory discriminating calibration and a re-certification of the nine.

- **Calibration: passed, all five parts**, including two checks the *wrong*
  rule fails outright (the `l^3 m` witness, and its kernel `(12, -3, 1)`), and
  a 48-cell battery of which **41 discriminate** between the rules.
- **The nine: all nine unchanged** under the corrected rule.  Session 27's
  record stands.  This was pre-registered prediction **P1** and it held.
- **The 62: partial coverage, uniform result.**  Every cell measured returns
  `mult_det = mult_pad = a` and `D = 0`.  No cell came in below the ambient
  cap, so the sceptical re-run branch (3× points, second seed) was never
  needed.  No `D > 0`; the STOP-EVERYTHING criterion was never triggered.
- **A dimension count settles the interpretation** independently of the sweep:
  `dim D_5^pad = 39 < dim D_5^det = 50` inside `Sym^4 C^5` of dimension 70, so
  the two ideals differ and `D = 0` *cannot* hold at every degree.  The sweep's
  uniformity dates the phenomenon rather than establishing a law.

## 2. Prediction ledger

| | prediction | outcome |
|---|---|---|
| **P1** | none of session 27's nine change under the corrected rule | **held** — 9/9 unchanged |
| **P2** | all 62 give `D = 0` with `mult = a` both sides | **held on every cell measured**; coverage partial (§4) |
| **P3** | no cell has `mult < a`; if any, the **pad** side first | **held** — no cell below `a` on either side |
| **P4** | if the nine were unrepresentative it shows first at the **balanced, large-`a`** end | **not triggered** — that end was probed on purpose and agrees |

P4 is the one I cared about getting right, and the pre-registration committed
in advance to a sweep order that could falsify it: *not* pure ascending `N_S`,
but interleaved with a deliberate pass over the largest-`a` and most balanced
cells the budget could reach.  That commitment was kept — **both `a = 7` cells
of the 62, the largest ambient multiplicity present, were measured**, and the
most balanced cell within the compute budget as well.

## 3. Engineering record

`python-flint` 0.9.0; `nmod_mat.rank()` and `.nullspace()` over two word-size
primes.  **No hand-rolled elimination was written** — sessions 28 and 29 both
tried and both failed their own self-tests, and I was session 29.

Files added (all new; nothing existing was touched):

| file | what |
|---|---|
| `analysis/wk8_s30_core.py` | corrected-rule raising operators, restriction, evaluation, `measure` |
| `analysis/wk8_s30_pleth.py` | `a(lam, delta)` by plethysm — the independent route |
| `analysis/wk8_s30_calib.py` | the five-part discriminating calibration |
| `analysis/wk8_s30_sweep.py` | the 62, and the interleaved order |
| `analysis/wk8_s30_run62c.py` | the coordinated worker, shared claim queue, memory guard |
| `analysis/wk8_s30_reconcile.py` | PID-aware claim release |
| `analysis/wk8_s30_report.py` | ledger → coverage fractions and tables |
| `analysis/wk8_s30_dims.py` | short-weight variety dimensions, exact derivatives |
| `results/PREREG_s30.md` | pre-registration, committed before any computation |
| `results/sweep62_ledger.md` | per-cell record, banked as each cell completed |

### Three mistakes, and what caught each

**(a) Two drivers recomputing the same cells.**  I launched an interleaved
driver and an ascending driver in parallel.  Their cheap ends coincide, so
they duplicated four cells before I noticed it in the logs — a straight waste
of budget, caught by reading output rather than by any check.  Fixed by
replacing both with a shared work queue: a cell is claimed by creating
`results/claims/<lam>.claim` with `O_CREAT|O_EXCL`, which is atomic, so
exactly one worker gets each cell.

**(b) The first reconcile released a live worker's claim.**  Cleaning up after
a killed worker, I released *every* unbanked claim — including the cell a
still-running worker was in the middle of computing.  Two workers would then
have raced on it.  Caught within a minute by checking which claims existed
against which workers were alive, and the claim was restored by hand before
any damage.  Fixed properly: claim files record their owning PID and a claim
is released only when its owner is gone.  The next reconcile confirmed the fix
by leaving two live claims alone and releasing only the dead worker's.

**(c) An OOM kill.**  Peak RSS is quadratic in `N_S` (measured: 2.4 GB at
`N_S = 6789`, giving `~5.2e-8 . N_S^2` GB).  I set a second worker's cap at
`N_S <= 13000` on an estimate rather than a measurement, and it was killed at
`N_S = 9224` with 4.76 GB anon-rss while the first worker held memory.  The
cell was lost, not corrupted — the ledger is append-only and the claim was
released by the reconcile — but it cost about 40 minutes.  Fixed by a memory
guard in the driver that predicts a cell's requirement and **waits** rather
than skipping, so coverage is never silently reduced by a memory dip.

None of the three touched a reported number.  All three were process failures,
and (b) is the one worth remembering: a cleanup routine that does not know
what is still running is more dangerous than no cleanup at all.

