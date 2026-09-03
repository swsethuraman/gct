# Session 43 — closing the six-row region that is already in reach

You are session 43 of the gct programme, working for the integrator.  Date your
work 2026-09-03 onward.  This session finishes what session 41 left inside its
own frontier: 49 eligible six-row cells it could have measured but ran out of
time for, and the handful of permanent-side weights that stand between us and a
clean theorem at degree 7.  If the repository already shows a session 43, do not
renumber; flag it and carry on.

## Rules (standing)

- Fresh clone of `github.com/swsethuraman/gct`, branch `s43-sixrow-close`,
  container only.  **Clone check**: `docs/s41_review.md`,
  `analysis/wk9_s41_kernel.py`, `results/s41_ledger.md`,
  `results/sixrow_census.md`, `results/s41_per6.md` and
  `docs/brief_wording.md` must all exist (absence ⇒ stale clone; stop and
  report).
- Single-writer files — never edit: `paper/det3-conductor.tex`,
  `paper/det4-onset.tex`, `PROJECT_NOTES.md`, `docs/boundary_deficit.html`.
- Delivery is by git bundle (`git bundle create sixrowclose.bundle
  s43-sixrow-close`, single ref).  Do not push.  Write a checkpoint bundle
  every few hours.
- **Commit messages carry `Co-Authored-By` only.**  Do not add a session-link
  trailer, and do not hard-code one in any script that commits (the s36 and s41
  sweep scripts do; do not copy that pattern).  No `claude.ai/...` URL in any
  file you write.
- No file over 5 MB committed; logs under `results/logs/`; never rewrite
  repository-wide config (append only).
- **Bounding long runs.**  Launch each with `timeout <seconds>` for wall clock
  and `ulimit -v` for memory, and write its process id to
  `results/logs/<run>.pid`.  A run that must be ended early is ended by that
  recorded id; never by name-pattern matching.  One heavy cell at a time above
  `n_χ ≈ 8000` — the container is a strict one-cell machine there
  (`docs/sixrow_frontier.md`, engineering notes).
- `results/PREREG_s43.md` first: predictions, falsifiers, stopping rules, the
  verification protocol copied verbatim.  Bank per cell with a commit;
  `python-flint` only.

## Required reading

`docs/sixrow_frontier.md` and `docs/s41_review.md` (what was measured and what
the numbers mean), `results/s41_coverage.md` (the exact gaps this session
fills), `results/s41_ledger.md` (row format and conventions),
`docs/stabiliser_reduction.md` (the reduction), `docs/transfer_lemma.md`
(Prop. 8 — why Phase B below is a theorem, not a measurement),
`docs/reducible_ideal.md` ((★) and the point-free `mult_red`),
`docs/brief_wording.md` (house vocabulary).

## Conventions (inherited, all proved)

`D = mult_pad − mult_det`; an obstruction is one cell with `D > 0`.  A cell is
eligible at `n = 4`, `ℓ(λ) = 6` when `a(λ,δ) ≥ 1` and `λ_1 ≥ δ`.  `D > 0`
requires `mult_det < a`, since `mult_pad ≤ a` always — so every cell with
`mult_det = a` is blind, whatever the pad side does.  **Pad points must be true
padded-permanent restrictions** `l(s)·per_3(A(s))`, never `l·(random cubic)`.

## Phase A — the 49 unmeasured cells inside the frontier

`results/s41_coverage.md` records, per degree, the eligible cells that fit at
`n_χ ≤ 20,000` and which of them are measured: `δ = 7`, 58 reachable of which
52 measured; `δ = 8`, 65 reachable of which 22 measured.  Rebuild that list
yourself from `results/sixrow_census.md` (do not trust the counts — re-derive
them, and report any disagreement as a finding), publish it as
`results/s43_todo.md` ordered by `n_χ`, then measure ascending in `n_χ`.

Per cell, exactly as `results/s41_ledger.md`: `a` by kernel dimension **and** by
plethysm, asserted equal; `rank(R) = n_χ − a` asserted; `mult_det` and
`mult_pad` at `a + 8` points; two primes; the point-free `mult_red` by (★).  Any
cell with `mult < a` on either side gets the independent re-check (`3a + 24`
fresh points, a fresh seed, both primes) before it is banked.

Two outcomes, both worth having:

- **`mult_det < a`** — the six-row onset, the number the programme wants.
  Record the degree, the weight, and the determinant-side kernel; exhibit it and
  re-check it independently.  Then measure the pad side at that cell with care.
- **`D > 0`** — halt the sweep; the verification protocol takes over: `a` both
  routes; `mult_det` and `mult_pad` re-derived at 3× points and a second prime;
  the kernel vector exhibited and shown nonzero at 20 independently built true
  padded-permanent points and zero at 20 determinant pencils; `m_det`
  re-derived by a second, independently written implementation (calibrated on
  the anchors 3, 11, 43); everything into `docs/OBSTRUCTION_CANDIDATE.md`, and
  end the session there.  The integrator re-derives before the word is used.

## Phase B — close `I(D_6^{per_3})_7 = 0` completely

`results/s41_per6.md` measured 20 of the 27 length-6 weights `μ ⊢ 21` with
`a(μ,7) ≥ 1`, all with `mult = a`, stopping at `n_χ ≤ 6000`.  The seven left
are `(9,4,3,2,2,1)`, `(8,5,3,2,2,1)`, `(7,6,3,2,2,1)`, `(7,5,4,3,1,1)`,
`(7,5,4,2,2,1)`, `(6,6,4,2,2,1)`, `(6,5,4,3,2,1)`, each with `a = 1` (verify
this yourself).  Measure them (points `per_3(Σ s_i A_i)`, `n = 3`, `r = 6`, both
primes).  If all are empty then `I(D_6^{per_3})_7 = 0` outright, and by
Prop. 8(1) of `docs/transfer_lemma.md` **`mult_pad = mult_red` in every weight
of degree 7** — a theorem with no points in it, and it removes the one
"not forced" cell of `results/s41_coverage.md`.  If one is *not* empty, that is
the first permanent equation the programme has ever seen: stop, certify it
(exhibit the vector, re-check at a fresh seed and both primes), and report — it
is a bigger result than anything in Phase A.

Then, as budget allows, continue the same scan at `δ = 8` above `n_χ = 6000`
(63 weights remain), ascending in `n_χ`.

## Phase C — the first rung at `δ = 9`

Cells with `ℓ = 6`, `λ ⊢ 36`, `λ_1 ≥ 9`, `a ≥ 1`, ordered by `n_χ`; measure the
cheapest that fit.  Each degree the determinant ideal is empty extends the
bracket by a rung; note that `I(R_6)` has gained an element in a new weight at
each of `δ = 6, 7, 8`, so the pad side may well bite here too — a `D = −1` at
`δ = 9` is expected and is not an obstruction.

## Pre-registration (minimum)

P1: validation reproduces three banked s41 rows including `(13,10,6,1,1,1)`
`δ = 8` (`a = 9`, `mult_det = 9`, `mult_pad = mult_red = 8`) — a cell where a
route that cannot see the drop would return 9.  P2: your prediction for whether
any of the 49 shows `mult_det < a`, with reasoning and the regime it lives in.
P3: your prediction for Phase B, with reasoning.  Stopping rules: validation
failure → stop; `D > 0` → the protocol; memory → the todo list bounds honesty.

## Deliverables

`results/PREREG_s43.md`, `results/s43_todo.md`, `results/s43_ledger.md`,
`results/s43_per6.md`, `docs/sixrow_close.md` (house style: what is now
measured, the coverage arithmetic redone, the Phase-B verdict and what it makes
a theorem, the honest boundary), code `analysis/wk9_s43_*.py`.  End with the
frontier as you leave it and the bundle head hash.
