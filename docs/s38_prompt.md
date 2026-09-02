# Session 38 — where do the determinant's five-row equations begin? (the occurrence screen, then δ = 8)

You are **session 38** of the gct programme, working for the integrator.  Date
your work 2026-09-02 onward.  This is a long compute session with a
permanent-independent target: the onset degree of `I(D_5^det)` — the first
degree at which five-row determinantal quartic threefolds acquire an
equation.  The window is `[8, 405]` (empty through 7 on every measured cell;
capped by the discriminant).  If the repository already shows a session 38,
do not renumber; flag it and carry on.

## Rules (standing)

- Fresh clone of `github.com/swsethuraman/gct`, branch `s38-onset`,
  container only.  **Ancestry gate**: `git merge-base --is-ancestor c02cee8
  HEAD` must pass, **and** `docs/s35_review.md` must exist.
- Single-writer files — never touch: `paper/det3-conductor.tex`,
  `PROJECT_NOTES.md`, `docs/boundary_deficit.html`.
- Delivery by git bundle (`git bundle create onset.bundle s38-onset`, single
  ref).  No pushes.  Insurance bundle every few hours.
- `results/PREREG_s38.md` first; bank per cell; `python-flint` only; claim
  queue and PID discipline as in `analysis/wk8_s30_run62c.py`.

## Why this target, and what it is not

At `ell = 5` the padded permanent is washed out (`docs/s35_review.md` §1):
nothing at this length is about the permanent, so this session does **not**
hunt `D > 0` and measures the **det side only**.  What it measures is real
and permanent-independent: the degree at which `D_5^det` — a codimension-20
variety whose generic member is a 20-nodal non-factorial quartic threefold
(`docs/theory_directions.md` §C) — first has an equation.  Codimension-20
loci usually have low-degree equations; this one has none through degree 7.
Pinning the onset dates the whole window and is a headline number for the
second paper.  If a pad-side number is cheap at a cell you are measuring
anyway, bank it for the record, labelled "reducibility, not permanent."

## Required reading

`docs/s35_review.md`, `docs/s33_review.md` §4, `docs/theory_directions.md`
§C and §D (Direction 4), `docs/d5_ideal.md` (s28's `n = 3` occurrence
mechanism, the one that fired at `delta = 10`), `docs/sweep62.md`,
`docs/e4_hunt.md` §4, and `docs/s36_prompt.md` for the stabiliser
reduction lemma, which you will also implement — **independently**.

## Phase 0 — the occurrence screen (exact arithmetic, no memory wall)

For every weight with `ell(lam) = 5`, `|lam| = 4·delta`, `a(lam, delta) >= 1`,
at `delta = 8, 9, 10, 11, 12` (as far as the character computations allow
in budget): compute `a` (plethysm — reuse `analysis/wk8_s30_pleth.py`) and
the Peter–Weyl bound `m_det(lam)` (the multiplicity in the coordinate ring of
the orbit; via the symmetric rectangular Kronecker formula of the
programme's easy-count work, with `(delta^4)` the rectangle — validate your
implementation against the `n = 3` values in `scripts/ambient_screen.py
--selftest` and against any banked `n = 4` `m_det`).  Since
`mult_det <= min(a, m_det)`, **every cell with `a > m_det` has
`det_units >= a − m_det > 0` with no rank computation at all** — this is how
the `n = 3` ideal was first pinned (s28, `delta = 10`).  The first `delta`
with such a cell is an unconditional upper bound on the onset; if none
appears through `delta = 12`, that is banked as "the occurrence route is
silent through 12," itself a result (it says the onset, when found, will be
a genuine multiplicity phenomenon).  Pre-register which way you expect it.

## Phase 1 — rank measurements at `delta = 8` (and `9` if the budget allows)

Implement the stabiliser-isotypic reduction of `docs/s36_prompt.md`
**from the lemma statement, not from session 36's code** (two independent
implementations are the house's check on a shared spec).  Validate exactly
as that brief prescribes — including the odd-block sign tests and the
ledger reproductions — before any new cell.  Then: the `delta = 8`, `ell = 5`
census with reduced sizes (`n_chi`), published before sweeping; det-side
measurements ascending in `n_chi`, with any `a > m_det` cells from Phase 0
pulled to the front (they are certain to bite; measure them to exhibit the
kernel).  Per cell: `a` two routes, `rank(R) = n_chi − a` asserted, two
primes, banked with a commit.

**The first det-side bite is the onset**, and it gets the full sceptical
protocol: 3× points, second seed and prime, the kernel vector exhibited and
shown to vanish at 10 fresh det pencils and *not* at a generic quartic; then
its weight, degree and length recorded as the programme's first equation of
`D_5^det`.  If `delta = 8` is empty on every reachable cell, the floor moves
to 9 for the measured corner and you say exactly which cells were not
reached.

## Pre-registration (minimum)

P1: validation battery passes, odd-block tests included.  P2: whether the
occurrence screen fires by `delta = 12`, with reasoning and its regime
(the `n = 3` mirror fired at 10; state why that may or may not transfer —
the house has been burned by regime transfer three times).  P3: whether
`delta = 8` bites on any reachable cell.  Kill criteria: validation failure
→ stop; a Phase-0 `a > m_det` cell whose rank measurement *fails* to bite →
stop everything, one of `a`, `m_det`, or the pipeline is wrong, and that is
the finding.

## Deliverables

`results/PREREG_s38.md`, `results/occurrence_screen.md` (the full `a` vs
`m_det` table by degree), `results/onset_ledger.md`, `docs/det_onset.md`
(findings in the house style; if the onset is found, its full certificate;
if not, the honest bracket), code as `analysis/wk9_s38_*.py`.  End with the
window as you leave it — `[floor, 405]` or the pinned onset — and the bundle
head hash.
