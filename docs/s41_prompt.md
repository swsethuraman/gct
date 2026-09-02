# Session 41 — the six-row frontier: the onset of the six-row determinant ideal, and the obstruction there

You are session 41 of the gct programme, working for the integrator.  Date
your work 2026-09-02 onward.  This is the programme's live obstruction hunt at
the first length that can carry the permanent.  If the repository already
shows a session 41, do not renumber; flag it and carry on.

## Rules (standing)

- Fresh clone of `github.com/swsethuraman/gct`, branch `s41-sixrow`, container
  only.  Ancestry gate: `git merge-base --is-ancestor 5aa564b HEAD` must pass,
  and both `docs/s40_review.md` and `analysis/wk9_s36_stabred.py` must exist in
  your clone (absence ⇒ stale clone; stop and report).
- Single-writer files — never touch: `paper/det3-conductor.tex`,
  `paper/det4-onset.tex`, `PROJECT_NOTES.md`, `docs/boundary_deficit.html`.
- Delivery by git bundle (`git bundle create sixrow.bundle s41-sixrow`, single
  ref).  No pushes.  Insurance bundle every few hours.  No file over 5 MB
  committed; logs under `results/logs/`; never rewrite repository-wide config;
  kill by explicit PID, never `pkill -f`.
- `results/PREREG_s41.md` first: predictions, falsifiers, the regime each lives
  in, kill criteria, the obstruction protocol copied verbatim.  Bank per cell;
  `python-flint` only; claim queue as in `analysis/wk8_s30_run62c.py`.

## Required reading

`docs/s36_review.md` and `docs/stabiliser_reduction.md` (the reduction you
will use), `docs/s37_review.md`, `docs/washout_lemma.md`,
`docs/transfer_lemma.md` (why ℓ=6 and δ≥7), `docs/reducible_ideal.md` (the
(★) criterion and point-free `mult_red`), `results/s36_ledger.md` (the 34 ℓ=6
cells already done), `docs/s34_prompt.md` (conventions and the protocol).

## The target, stated precisely

Convention: `D = mult_pad − mult_det`; an obstruction is a single cell with
`D > 0`.  Two facts frame the hunt:

1. The permanent is visible only at ℓ ≥ 6 and δ ≥ 7 (washout + the Pieri delay
   of `docs/s37_review.md`).  So ℓ=6 is the first permanent-sensitive length,
   and δ=7 the first permanent-sensitive degree.
2. `D > 0` requires `mult_det < a` — the determinant's six-row ideal must be
   nonzero at the cell, since `mult_pad ≤ a` always.  Session 36 found the
   six-row ideal empty (`mult_det = a`) at every reachable cell of δ=6,7.  So
   the obstruction cannot appear until the six-row determinant ideal switches
   on, and that onset degree is unknown.  Pinning it is this session's first
   job, and the obstruction hunt rides on top of it.

Also inherited, all proved: obstruction cells need `λ_1 ≥ δ` (Kadish–Landsberg
via (★)); `6 ≤ ℓ(λ) ≤ 10` (permanent-visible, and `mult_pad = 0` for ℓ ≥ 11
since the padded permanent lives in 10 variables); `a ≥ 1` is the correct
gate (BIP is silent at (3,4)).  Pad points must be true padded-permanent
restrictions `l(s)·per_3(A(s))`, never `l·(random cubic)` — at r=6 the two
differ and the wrong one manufactures false obstructions.

## Phase 0 — the reduced census and the arithmetic map

Enumerate every `λ ⊢ 28` (n=4, δ=7) and `λ ⊢ 32` (δ=8) with `ℓ(λ) = 6`,
`a(λ,δ) ≥ 1`, `λ_1 ≥ δ`.  For each: `a` (two independent routes), `m_det(λ)`
(the symmetric rectangular Kronecker bound — reuse `analysis/wk9_s38_screen.py`,
validated against the n=3 self-test values 3, 11 before use), the reduced size
`n_χ = N_S/|Stab_W(λ)|`, and predicted memory (`~1.7e-8·n_χ²` GB, s36's
measured constant).  Publish `results/sixrow_census.md` before any
measurement, with the feasibility line and, per cell, whether `a > m_det` (an
arithmetic-forced candidate — measure these first) or `a ≤ m_det` (the onset
there will be a pure rank drop).

## Phase 1 — validate, then sweep ascending degree

Validate the reduction exactly as `docs/s36_review.md` §1 prescribes: the
`l^3 m` witness (kernel `(12,−3,1)`), `analysis/wk8_s30_calib.py` as-is, and
reproduce three of s36's banked ℓ=6 cells (`results/s36_ledger.md`) at both
primes.  Only then measure.

Sweep the reachable ℓ=6 cells ascending in degree (δ=7 first, then δ=8),
within each degree ascending in `n_χ`, interleaved 3:1 with the largest-`a`
and most-balanced reachable cells.  Per cell measure both `mult_det` and
`mult_pad` (true pad points), `a` by kernel dimension = plethysm,
`rank(R) = n_χ − a` asserted, two primes, banked with a commit.  Also record
the point-free `mult_red` (via (★), `analysis/wk9_s36_red.py`): at ℓ=6 it is
an upper bound on `mult_pad`, and where `mult_red = mult_pad` you learn the
permanent adds nothing at that cell.

Two outcomes to watch, both valuable:

- The six-row onset: the first cell with `mult_det < a`.  Record its degree,
  weight, and the det-side kernel (exhibited, sceptical branch: 3× points,
  second prime, fresh seed).  This is the six-row analogue of the five-row
  onset the cap theorem bounds — a headline number for paper 2, obstruction
  or not.
- `D > 0`: STOP-EVERYTHING.  Full protocol: (i) `a` both routes; (ii)
  `mult_det` and `mult_pad` re-derived at 3× points, second prime; (iii) the
  det-side kernel vector exhibited and shown nonzero at 20 independently built
  true padded-permanent points and vanishing at 20 det pencils; (iv) `m_det`
  re-derived by a second, independently written implementation
  (Murnaghan–Nakayama, calibrated on 3, 11); (v) everything into
  `docs/OBSTRUCTION_CANDIDATE.md`, prereg cross-referenced; (vi) end the
  session there.  The integrator re-derives before the word is used.

## Pre-registration (minimum)

P1: validation reproduces three s36 cells and the witness.  P2: your
prediction for whether the six-row ideal switches on by δ=8 in reach, with the
reasoning and its regime (note: nothing forces it low; the five-row onset was
≥ 8).  P3: if `mult_det < a` appears, whether `mult_pad` beats it (your prior
on `D > 0`, and its basis — BIP's asymptotic blindness says no).  Kill
criteria: validation failure → stop; `D > 0` → the protocol; memory → the
census bounds honesty.

## Deliverables

`results/PREREG_s41.md`, `results/sixrow_census.md`, `results/s41_ledger.md`
(both multiplicities and `mult_red` per cell), `docs/sixrow_frontier.md`
(house style: the six-row onset as found or bracketed; coverage by degree and
`a`; the obstruction verdict; honest boundary), code `analysis/wk9_s41_*.py`.
End with the frontier as you leave it and the bundle head hash.
