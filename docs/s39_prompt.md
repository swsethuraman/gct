# Session 39 — the long-weight occurrence screen, and one-bit obstruction tests

You are **session 39** of the gct programme, working for the integrator.  Date
your work 2026-09-02 onward.  This is the programme's first direct hunt for an
obstruction in the one region no session has examined: weights with **seven
to sixteen rows**.  If the repository already shows a session 39, do not
renumber; flag it and carry on.

## Rules (standing, plus two new ones)

- Fresh clone of `github.com/swsethuraman/gct`, branch `s39-longweights`,
  container only.  **Ancestry gate**: `git merge-base --is-ancestor 48bbdc3
  HEAD` must pass, **and** `docs/s36_review.md` must exist in your clone (it
  lands after `48bbdc3`; absence means a stale clone — stop and report).
- Single-writer files — never touch: `paper/det3-conductor.tex`,
  `PROJECT_NOTES.md`, `docs/boundary_deficit.html`.
- Delivery by git bundle (`git bundle create longweights.bundle
  s39-longweights`, single ref).  No pushes.  Insurance bundle every few
  hours.  **New rule: never commit a file over 5 MB** (certificate vectors go
  in `results/s39_cells/` only if under that; otherwise bank a hash and a
  reproduction command).  **New rule: logs under `results/logs/`;** never
  rewrite repository-wide configuration.
- `results/PREREG_s39.md` first: predictions with falsifiers and the regime
  each lives in; kill criteria; the obstruction protocol below copied
  verbatim.  Bank per cell; `python-flint` only; claim queue and explicit-PID
  kills as in `analysis/wk8_s30_run62c.py` — `pkill -f` is banned outright.

## Required reading

`docs/s36_review.md`, `docs/stabiliser_reduction.md`, `docs/s38_review.md`
and `results/occurrence_screen.md` (the length-5 screen you are extending),
`docs/transfer_lemma.md` and `docs/washout_lemma.md` (s37), `docs/d5_ideal.md`
§1 (session 28's δ = 10 finding at `n = 3` — the precedent), and
`docs/s34_prompt.md` for conventions.

## Why this region, and why now

At `n = 3` the determinant's ideal was first pinned at δ = 10 not at length 5
but at **lengths 8 and 9**, by the degenerate mechanism `m_det = 0`: the
orbit has no functions of that weight at all, so the closure cannot either,
while the ambient has `a = 1`.  Every `n = 4` session has worked at lengths 5
and 6 — and we have since proved five rows cannot carry the permanent and
measured that six rows do not through degree 7.  Lengths 7–16 have never
been screened at `n = 4`.

An occurrence obstruction is a weight with `mult_det = 0 < mult_pad`.
Bürgisser–Ikenmeyer–Panova prove none exist for `n ≥ m^25`; at `(3, 4)` their
theorem is silent and their constructions do not exist.  Nobody knows.  A hit
would be the first representation-theoretic separation of a padded permanent
from a determinant at any size (the known separation, Landsberg–Manivel–
Ressayre, is geometric); a clean miss through δ = 12 at every length extends
their phenomenon downward, honestly pre-registered.  Both are results.

Constraints you inherit, all proved: obstruction cells need `λ_1 ≥ δ`
(Kadish–Landsberg, via (★) in `docs/stabiliser_reduction.md`); `a ≥ 1` is
the correct gate (`docs/s37_review.md` §2b); and pad points must be **true
padded-permanent restrictions** `l(s)·per_3(A(s))` with `A` a `3×3` matrix of
random linear forms in the `ℓ` variables — never `l·(random cubic)`
(`docs/transfer_lemma.md`).

## Phase 0 — the screen (exact arithmetic, no memory wall)

For `δ = 8, 9, 10, 11, 12` (as far as the character budget allows — state
where it stopped), every `λ ⊢ 4δ` with `ℓ(λ)` from **6 to min(δ, 16)** (a
degree-δ equation has at most δ rows), `a(λ, δ) ≥ 1`, and `λ_1 ≥ δ`: compute
`a` (plethysm; reuse `analysis/wk8_s30_pleth.py` / `scripts/ambient_screen.py`)
and `m_det(λ)` (the symmetric rectangular Kronecker coefficient; reuse
`analysis/wk9_s38_screen.py`, and **validate it against s38's length-5 table
before extending it**).  Bank three lists:

- **one-bit cells**: `a = 1, m_det = 0` — the determinant side is zero for
  free, and the permanent side is a single evaluation;
- **forced cells**: `a > m_det ≥ 1` — the determinant loses `a − m_det`
  units for free, and an obstruction is certified by a pad-side rank
  `≥ m_det + 1` (since `mult_det ≤ m_det < mult_pad`), with **no det-side
  computation at all**;
- everything else (silent).

Publish `results/longweight_screen.md` before any evaluation.  If both lists
are empty through your reachable δ, that is the session's result: "the
occurrence route is silent at every length through δ = k," banked with the
table.  Pre-register (P2) whether you expect the lists to be non-empty, and
say which regime the expectation comes from — the `n = 3` precedent is a
different `n` and a different length; the house has been burned by regime
transfer three times.

## Phase 1 — one-bit tests, ascending in cost

For each one-bit cell: build the unique highest-weight vector with the
validated reduction (`analysis/wk9_s36_stabred.py`; these peaked long weights
have large stabilisers on their repeated small parts, so they are cheap),
reconstruct it exactly over ℤ (`analysis/wk9_s36_exact.py`) and verify the
raising operators kill it.  Then two evaluations, both primes:

1. at 20 `det_4` pencils in `ℓ` variables — it **must vanish** (this audits
   `m_det = 0`; a nonzero value here means `a`, `m_det`, or the pipeline is
   wrong — stop everything, that is the finding);
2. at 20 independently constructed true padded-permanent points — **nonzero
   at any one of them means `mult_pad = 1 > 0 = mult_det`: an occurrence
   obstruction candidate.**

For each forced cell: pad-side rank at `3(a+8)` true padded-permanent points,
two primes; rank `≥ m_det + 1` is an obstruction candidate.

**Obstruction protocol — STOP-EVERYTHING on any candidate.**  No further
cells.  Then, in order: (i) `a` by both plethysm routes; (ii) `m_det`
re-derived by a **second, independently written** implementation
(Murnaghan–Nakayama on beta-sets, calibrated on the `n = 3` self-test values
3, 11 and on s38's length-5 cells) — the whole claim rests on this number;
(iii) the vector re-reconstructed from a third prime; (iv) the pad points
rebuilt from scratch by a different random construction, and the det
vanishing re-checked at 50 pencils; (v) everything into
`docs/OBSTRUCTION_CANDIDATE.md` with every input file named; (vi) the session
ends there.  The integrator re-derives independently before anyone uses the
word.  A false obstruction would be the worst outcome this programme could
produce; the protocol is proportionate.

## Pre-registration (minimum)

P1: the reduction validation reproduces three s36 ledger cells and the
witness.  P2: whether one-bit or forced cells exist by δ = 12 (with regime).
P3: if they exist, whether the one-bit vector vanishes at the padded
permanent (BIP's asymptotic phenomenon says yes; state your prior and its
basis).  Kill criteria: any det-side non-vanishing at a one-bit cell → stop;
character budget → honest table of what was reached.

## Deliverables

`results/PREREG_s39.md`, `results/longweight_screen.md` (+ csv),
`results/onebit_ledger.md`, `docs/longweight_hunt.md` (house style: proved /
measured / expectation; the window as left; coverage by δ and by length),
code as `analysis/wk9_s39_*.py`.  End with the bundle head hash.
