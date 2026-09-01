# Session 34 — `δ = 7` at `ℓ ≥ 5` (`n = 4`): the census, then the sweep

You are **session 34** of the gct programme, working for the integrator.  Date
your work 2026-09-01 onward.  If the repository already shows a session
claiming number 34, do not renumber yourself — flag the collision and carry on.

## Rules (standing)

- Fresh clone of the public repository `github.com/swsethuraman/gct`.  Branch
  `s34-d7`, container only.
- **Ancestry check before anything else**: `git merge-base --is-ancestor
  29bea5f HEAD` must succeed (ancestry, not equality).  If it fails, stop and
  report.
- Single-writer files — never touch: `paper/det3-conductor.tex`,
  `PROJECT_NOTES.md`, `docs/boundary_deficit.html`.
- Delivery is a git bundle (`git bundle create d7.bundle s34-d7`, single ref).
  No pushes; the proxy refuses them by design.
- Pre-registration first (`results/PREREG_s34.md`, committed before any
  measurement), with named falsifiers, kill criteria, and a **regime
  statement** for every prediction.
- Bank per cell, commit as completed; the container resets.

## Context (read first)

`docs/sweep62.md` (all of it) and `docs/s30_review.md`.  Session 30
established that `δ = 6` is below the onset of *both* ideals at `r = 5`:
every measured cell returned `mult_det = mult_pad = a`.  The dimension table
(15/34/50 vs 12/23/39) says the two varieties differ, so some degree
separates them — the axis is the degree, and you are the first probe at
`δ = 7`.

**Convention, stated so it cannot drift**: `D := mult_pad − mult_det`.  An
obstruction is `D > 0` — the padded permanent strictly exceeding the
determinant at a weight.  `D < 0` (the pad side biting first) is the
*expected* direction — pad's variety is smaller (39 < 50), so its ideal
should switch on earlier — and it is **not** an obstruction.  Pre-register
this interpretation rule verbatim, so a `D < 0` cannot be upgraded into a
claim it is not.  A first pad-side bite is still informative (it dates the
pad ideal's onset) and goes in the ledger as the byproduct it is.

## Entry calibration (all before anything new is trusted)

1. **The witness**: binary quartics, `closure{l^3 m}`, `λ = (4,4)`, `δ = 2` —
   `mult = 0`, kernel `∝ (12, −3, 1)` (wrong rule gives `(1, −4, 3)`).  The
   rule on `main` is correct as of `7d93449`; the witness guards against a
   stale clone and costs seconds.
2. Run `analysis/wk8_s30_calib.py` as-is — all five parts must pass.  Quote
   the **discriminating ratio** (41 of 48), never the bare pass count.
3. Re-certify **three** of session 30's banked cells, chosen by a
   deterministic rule you state in the prereg (e.g. hash of the date mod the
   ledger length) — results must reproduce `results/sweep62_ledger.md`
   exactly.

## Phase 1 — the census (a deliverable in itself)

Enumerate every cell at `n = 4`, `δ = 7` (`|λ| = 28`), `ℓ(λ) ≥ 5`, `a ≥ 2` —
the two-condition gate; reuse `scripts/ambient_screen.py`'s `must_have_room`
adapted to `(n, δ) = (4, 7)`.  For each cell: `a` (by plethysm), `N_S`,
balance (`λ_1 − λ_ℓ`), and predicted memory at `5.6e-8 · N_S^2` GB against
the ~6.5 GB usable budget (this is s30's *measured* constant; their
conservative 7.5e-8 fit overdrew the frontier by one cell).  Publish
`results/d7_census.md` **before any sweep begins**, with the feasibility
line: which cells fit, which do not, totals by `a` and by balance.  If
nothing fits, the census and feasibility map **is** the session — deliver it
honestly and stop.

## Phase 2 — the sweep

- **Pre-register the exact order**: ascending `N_S` interleaved 3:1 with
  deliberate probes of the largest-`a` and lowest-balance cells the budget
  reaches — the representativeness falsifier must be genuinely exposed, not
  nominally (s30's P4 discipline).
- Per cell, the full discipline: `a` by two independent routes (kernel
  dimension and plethysm — must agree); ranks over two word-size primes via
  `python-flint` `nmod_mat` (no hand-rolled elimination — two sessions'
  self-tests have failed at it); `rank(R) = N_S − a` asserted; **both**
  `mult_det` and `mult_pad`; the row banked to `results/d7_ledger.md` and
  committed before the next cell starts.
- **Sceptical branch** (either side below `a`): re-run at 3× evaluation
  points, second prime, fresh seed; exhibit the kernel vector.  Only then
  does the bite enter the ledger.
- **`D > 0` is STOP-EVERYTHING.**  No further cells.  The obstruction
  protocol, in full: (i) both `a`-routes agree at the cell; (ii) both
  multiplicities re-derived at 3× points on a second prime; (iii) the
  det-side kernel vector exhibited and **evaluated nonzero at three explicit
  padded pencils** (substitutions of `x_0`-padded `per_3`) — a vector claimed
  to separate must be shown to separate; (iv) everything into
  `docs/OBSTRUCTION_CANDIDATE.md`, prereg cross-referenced, and the session
  ends there.  The integrator re-derives independently before anyone uses
  the word obstruction.

## Engineering (inherit, do not rediscover)

Multi-worker only via the claim-queue design of `analysis/wk8_s30_run62c.py`
and `wk8_s30_reconcile.py`: `O_CREAT|O_EXCL` claim files, PID-owned, a claim
released only when its owner is dead.  A memory guard **waits**, it does not
skip.  Kill by explicit PID, read back first — `pgrep -f`/`pkill -f`
self-matching has now cost two sessions.  Existence pre-check before the
memory gate.

## Pre-registration contents (minimum)

- **P1**: the three re-certified cells reproduce the s30 ledger exactly.
- **P2**: your committed prediction for the modal outcome at `δ = 7`
  (uniform `D = 0` again, or first bites — say which, with reasoning and its
  regime).
- **P3**: if any side bites, the pad side bites first.
- Kill criteria: witness failure → stop; `D > 0` → the protocol above;
  memory → the census already bounds honesty; any deviation of the three
  re-certs → stop everything, the pipeline is not the one s30 ran.

## Deliverables

`results/PREREG_s34.md`, `results/d7_census.md`, `results/d7_ledger.md`,
`docs/d7_sweep.md` (house style: proved / measured / expectation, each
labelled; honest boundary; coverage as a fraction of cells *and* of ambient
units), code as `analysis/wk9_s34_*.py`.  Reuse s30's machinery wherever it
fits.  End your report with the bundle head hash.
