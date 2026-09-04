# Session 47 — the two-unit predictor: is the normalisation bound exact when it fires?

You are session 47 of the gct programme, working for the integrator.  Date your
work 2026-09-04 onward.  This session tests, and tries to prove, the sharpest
regularity the programme has found — one that would make part of the pad side
computable in closed form at cells no rank computation can reach.  If the
repository already shows a session 47, do not renumber; flag it and carry on.

## Rules (standing)

- Fresh clone of `github.com/swsethuraman/gct`, branch `s47-exactness`, container
  only.  **Clone check**: `analysis/wk9_s42_redengine.py`,
  `analysis/wk9_s42_hpad.py`, `analysis/wk9_s42_sparse.py`,
  `analysis/wk9_s42_lift.py`, `docs/reducible_engine.md`, `results/s42_census.json`,
  `results/s43_ledger.md`, `docs/brief_wording.md` must all exist (absence ⇒
  stale clone; stop and report).
- Single-writer files — never edit: `paper/det3-conductor.tex`,
  `paper/det4-onset.tex`, `PROJECT_NOTES.md`, `docs/boundary_deficit.html`.
- Delivery by git bundle (`git bundle create exactness.bundle s47-exactness`,
  single ref).  Do not push.  Checkpoint bundle every few hours.
- **Commit messages carry `Co-Authored-By` only** — no session-link trailer, in
  commits or in any script that commits.  No `claude.ai/...` URL in any file.
- No file over 5 MB committed; logs under `results/logs/`; append-only config.
- Bound long runs with `timeout` and `ulimit -v`; record each process id in
  `results/logs/<run>.pid`; end a run only by that recorded id.
- `results/PREREG_s47.md` first, with your prior on the conjecture and what would
  falsify it.

## Required reading

`docs/reducible_engine.md` (§A the engine and its certificates, §B the
normalisation bound `h_pad` and Corollary B2, §C the Kadish–Landsberg reading),
`docs/s42_review.md`, `docs/sixrow_close.md` §3 (the family finding),
`docs/s43_review.md` §2 (the result below, with the numbers),
`docs/reducible_ideal.md` ((★) and the point-free `mult_red`).

## The conjecture

`h_pad(λ, δ) := mult_λ(Sym^δ V ⊗ Sym^δ Sym^3 V)` is the multiplicity in the
**normalisation** of `C[R_r]` (Kadish–Landsberg Prop. 1.8, re-proved as Theorem
B1 of `docs/reducible_engine.md`), so `mult_red ≤ h_pad` always, and `h_pad` is a
Pieri sum over a cubic plethysm — milliseconds at any cell, reachable or not.

> **Conjecture (exactness).**  Whenever `h_pad(λ, δ) < a(λ, δ)`, the bound is
> attained: `mult_red(λ, δ) = h_pad(λ, δ)`.

**The evidence, all of it, with no counterexample.**  Across session 42's 201
banked cells the bound fires at 8 and is exact at all 8.  And on the
**complete** `(λ_1, λ_2, λ_3, 1, 1, 1)` family at `ℓ = 6`, `δ = 8` — complete
because session 43 exhausted the reachable set there — the integrator computed
`h_pad` at all 33 cells with `a ≥ 1`:

| | cells | `h_pad < a` | outcome |
|---|---|---|---|
| `units = 2` | 4 | **4 of 4** | `a − h_pad = 2` exactly at each |
| `units = 1` | 5 | 0 of 5 | bound silent |
| `units = 0` | 24 | 0 of 24 | bound silent |

The four are `(11,9,9,1,1,1)`, `(11,10,8,1,1,1)`, `(12,9,8,1,1,1)`,
`(12,10,7,1,1,1)`.  So on a closed set the free bound names exactly the two-unit
cells and gives their multiplicity — while being blind to every one-unit cell.
The structural reading to test: **the second unit is a normalisation
phenomenon and the first is not.**

## Phase A — test it at scale (the decisive phase)

Session 42's census records `h_pad` at every cell of the region: **411 cells with
`h_pad < a` at `δ = 7, 8`** and 62 more at `δ = 9`, of which only a handful have
a measured `mult_red`.  Measure as many as the session affords, with
`analysis/wk9_s42_redengine.py` through the sparse route, ascending in `n_red`:

- publish the ordered work list with sizes first, as `results/s47_todo.md`;
- per cell record `a`, `h_pad`, `n_red`, `nnz`, `nullity_p` at both primes, the
  route, and `mult_red`; bank each with a commit;
- **`mult_red > h_pad` is impossible** (Corollary B2) — if you ever see it, you
  have a bug, not a discovery; stop and find it;
- `mult_red < h_pad` at any cell **refutes the conjecture**.  That is a result, not
  a failure: stop the sweep, certify that cell hard (both primes, exhibited
  kernel, exact integer lift), and write it up as the counterexample.

Cover as many *shapes* as possible, not just the cheapest: vary `ℓ` (6, 7, 8),
vary `δ` (7, 8, 9), and include cells inside and outside the
`(λ_1,λ_2,λ_3,1,1,1)` family, so the test is not confined to the family the
pattern was found in.

## Phase B — try to prove it

`h_pad − mult_red = mult_λ(D_δ / C[R_r]_δ)`, the multiplicity of the
normalisation quotient, supported on the non-normal locus `{ℓ ℓ' q} ∪ {ℓ² q}`
(`docs/reducible_engine.md` §B).  The conjecture says this quotient contributes
**nothing** in exactly those weights where `h_pad < a`.  Directions, in the order
the integrator would try them:

1. Identify `D_δ / C[R_r]_δ` as a module: it is the cokernel of the multiplication
   `μ*_δ` into the Segre-product ring.  Its support is the non-normal locus; is
   there a weight condition under which a `λ`-isotypic vector cannot be supported
   there?
2. `h_pad < a` says the `λ`-isotypic part of the normalisation is *already*
   smaller than the ambient plethysm.  Does that force the quotient's `λ`-part to
   vanish for a dimension or a Pieri reason?
3. Test the contrapositive numerically: at cells where `mult_red < a` but
   `h_pad ≥ a` (the one-unit cells), compute `h_pad − mult_red` and look at what
   the quotient contributes — a pattern there is as informative as a proof.

A proof, a counterexample, or a precise statement of the obstacle are all
acceptable outcomes; an unlabelled guess is not.

## Phase C — two cheap things to finish while Phase A runs

Both are short and both are owed.

1. **Lift the outstanding bites.**  `analysis/wk9_s42_lift.py` turns
   `mult_red ≤ a − k` from measured into proved.  Already done:
   `(8,4,4,4,4)_6`, `(9,9,8,1,1)_7`, `(8,8,8,2,2)_7`, `(12,4,4,4,4)_7`,
   `(10,8,7,1,1,1)_7`, `(13,10,6,1,1,1)_8`, `(13,12,4,1,1,1)_8`,
   `(13,8,8,1,1,1)_8`, `(11,9,9,1,1,1)_8` (two vectors) and
   `(11,10,8,1,1,1)_8` (two vectors, by the integrator).  **Outstanding:**
   `(12,9,8,1,1,1)_8` and `(12,10,7,1,1,1)_8` — the two remaining `D = −2` cells,
   which need **two** independent integer vectors each before anyone calls them
   two independent equations — plus `(14,8,7,1,1,1)_8`, `(13,9,7,1,1,1)_8`, and
   the two `δ = 9` rungs `(17,12,4,1,1,1)`, `(16,13,4,1,1,1)`.
2. **Close `I(D_6^{per_3})_8`.**  Session 43 measured 81 of the 91 length-6
   weights `μ ⊢ 24` empty; the 10 remaining are a couple of hours by its
   injectivity certificate (`analysis/wk9_s43_*`).  All empty ⇒
   `I(D_6^{per_3})_8 = 0` outright ⇒ by Prop. 8(1) of `docs/transfer_lemma.md`,
   `mult_pad = mult_red` at **every** weight of degree 8 — a theorem with no
   points in it, at the degree where every pad-side bite in the record lives.
   If one is *not* empty, that is the first permanent-specific equation the
   programme has ever seen: stop, certify it, and report it above everything else
   in this brief.

## Pre-registration (minimum)

P1: your prior that the conjecture survives Phase A, with reasoning.  P2: how
many cells you expect to measure and to what `n_red`.  P3: your prediction for
the 10 remaining `δ = 8` permanent weights.  Stopping rules: a counterexample →
certify and stop the sweep; a non-empty permanent weight → stop everything else
and certify; `mult_red > h_pad` → a bug, stop and find it.

## Deliverables

`results/PREREG_s47.md`, `results/s47_todo.md`, `results/s47_ledger.md`,
`results/s47_per6_d8.md`, `docs/exactness.md` (house style: the conjecture, the
evidence as you leave it with the count of firing cells tested, the proof attempt
and where it stands, the predicted two-unit cells across the whole region
including unreachable ones, the honest boundary), code `analysis/wk9_s47_*.py`.
End with the conjecture's status in one sentence and the bundle head hash.
