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

### Five process failures, and what caught each

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

**(d) `pgrep -f` matched my own shell — twice.**  Infrastructure rule 4 warns
about this and session 29 was bitten by it; I walked into it again.  A chained
launcher whose body waited on `pgrep -f "run62c.py asc"` never exited its loop,
because the shell that *created* the script had the heredoc text — including
that very string — in its own command line, so the pattern always matched
something.  Eleven minutes lost.  Trying to clean up with
`kill $(pgrep -f "...")` then killed the shell issuing the command, for exactly
the same reason, and took the patch with it.  The rule that works: **kill by
explicit PID, obtained and read back first**; never let a match pattern be
constructed from text that appears in the killing command line.

**(e) The memory gate sat in front of the claim check.**  The first version of
the guard asked "does this cell fit?" before asking "has someone already done
it?", so a worker spent twenty minutes waiting on memory for a cell that was
already banked.  Caught immediately in the log.  Fixed with a cheap
existence pre-check; the atomic `O_EXCL` claim remains the authority.

None of the five touched a reported number.  They were all process failures,
never measurement failures, and two are worth carrying forward: **(b)** a
cleanup routine that does not know what is still running is more dangerous
than no cleanup at all; and **(d)** the `pgrep`/`pkill` self-match is not a
once-off — it has now cost two sessions, and the only reliable defence is to
kill by explicit PID.

## 4. Coverage — the honest fraction

<!--GEN:S30COV-->
**25 of the 62 cells measured — 40%.**  Weighted by ambient multiplicity (the quantity actually at stake) that is **83 of 189 units, 44%**.

| axis | reached | across the 62 |
|---|---|---|
| `N_S` | 2800 – 9224 | 2800 – 97713 |
| `a` | 2 – 7 | 2 – 7 |
| balance | 7 – 12 | 4 – 12 |
<!--/GEN:S30COV-->

The binding constraint is **memory**, not time: peak RSS goes as `~7.5e-8 . N_S^2`
GB against a usable budget near 6.5 GB, which caps the reachable weight-space
dimension around `N_S ~ 11500` for a single worker.  The 62 run to
`N_S = 97713`.  The pre-registration anticipated partial coverage and committed
to reporting it as a fraction; `docs/sweep62.md` §6 gives the per-axis breakdown
and lists, by name and by the memory each would need, the six `balance <= 6`
cells that were out of reach — the one genuinely untested corner.

I want to be plain about what that corner does and does not cost.  The sweep
reached balance 7 and no lower.  The reason to expect `balance <= 6` to agree
is structural (§4 of `docs/sweep62.md`: at `delta = 6` neither ideal has begun,
for reasons independent of the weight's shape), and structural reasons are the
kind this programme has been wrong about before.  So: expectation, not
measurement, and labelled as such.

## 5. What I would tell the next session

**The question has moved.**  "Is `D = 0` a law over the weights at `delta = 6`?"
is now the wrong question, because the codimension table answers it in the
negative for free: `dim D_5^pad = 39` and `dim D_5^det = 50` are different, so
the ideals differ, so some `(lam, delta)` separates them.  What the sweep
establishes is that `delta = 6` is *before the onset* at `r = 5`.  The next
gate is the degree.

**The cheapest next measurement is not another cell of the 62.**  It is `e`,
the degree of the principal ideal of the `r = 4` determinantal hypersurface
(codim exactly 1 — established here, §4 of `docs/sweep62.md`).  `e` is one
number, it is far cheaper than any remaining `delta = 6` cell, and it calibrates
where to start looking at `r = 5`.  Session 29's task B was aimed at it.

**Two warnings about the machinery.**

1. The raising rule in `docs/isotypic_rank.md` §1 is **still wrong on `main`**
   as of `13fb170` — session 29 has not landed.  Anyone starting from the
   repository rather than from a brief will re-derive the same error.  The
   correct rule and a two-line witness that discriminates are at the top of
   `docs/sweep62.md` §1; that witness costs seconds and should be the first
   thing any new session runs.
2. `mult = a` calibrations cannot detect a wrong raising rule, because the two
   rules differ by a diagonal rescaling that preserves kernel dimension.  A
   calibration battery is only worth running if some part of it **fails** under
   the hypothesis being guarded against; ours had 41 such cells out of 48, and
   that ratio is the number to look at, not "48/48 passed".

## 6. Honest boundary of this session

- Coverage of the 62 is **partial**, and the untested corner is the balanced
  end below balance 7.  Nothing here should be quoted as "the 62 agree".
- `D = 0` on every cell measured is a statement about `delta = 6` at `r = 5`.
  It is **not** evidence that `per_3^pad` sits inside `det_4` — it is the
  absence of evidence against it, in a degree where §4 predicts no evidence
  either way could appear.
- The codimension table is the durable result of this session.  It was computed
  by generic Jacobian rank at random points: that is a lower bound on dimension
  which is sharp with probability 1, confirmed at three points over two primes,
  but it is a probabilistic certificate and not a proof.
- Nothing in `paper/`, `PROJECT_NOTES.md`, or `docs/boundary_deficit.html` was
  touched.  All files added are new.
