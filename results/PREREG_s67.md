# Pre-registration — session 67: certification, degeneration, and two engineering defects

Branch `s67-certification` off `main` at `226b4ef1` (the stock-take-correction
tip after sessions 56 and 57 were merged; ancestry gate
`git merge-base --is-ancestor 226b4ef1 HEAD` passes).  Written and committed
**before any measurement** — before the degeneration certification rate is
measured, before the back-fill counts are known, and before the widened
monomial code is run on any cell.  The only computation that precedes this file
is a re-reading of the repository (the verifier, `docs/sparse_det_route.md`,
`docs/s60_report.md`, `results/s60_cells.jsonl`, the s45 build, the s56 report).

Standing constraints of the programme are in force: delivery by a single-ref
git bundle, no push; single-writer files never touched
(`paper/det3-conductor.tex`, `paper/det4-onset.tex`, `PROJECT_NOTES.md`,
`docs/boundary_deficit.html`, `docs/conductor.html`); `Co-Authored-By` trailer
only, **no session-link trailer** (declined per the standing rule, as sessions
49, 56 and 59 did); every long run bounded by `timeout` and `ulimit -v` with its
process id in `results/logs/` and ended only by that id; logs under
`results/logs/`; no committed file over 5 MB; `python-flint` for every exact
rank; both house primes `2147483647, 2147483629` wherever a prime is used.

This is batch 10, wave 1 (C6), ungated and deliberately early: Part A defines
the certificate kind that sessions 63 and 65 will need, so the format additions
land before the batch's most load-bearing claims are produced.  Labels in the
report: **proved** / **measured** / **adopted** / **expectation**.

## 0. What this session is, and the one hard invariant

Three deliverables, none of which is a multiplicity measurement:

* **A.** A `gct-cert/1` certificate kind for the sparse (Wiedemann) route, its
  checker, its self-test, and the back-fill of session 60's 264 uncertified
  cells — or the named shortfall where the retained run data is insufficient.
* **B.** A degeneration full-rank certifier, one direction only
  (`rank(in Θ) ≤ rank Θ`), measured on known-negative blocks.
* **C.** Two engineering defects fixed with regression tests.

**The hard invariant, registered now so it cannot be quietly broken later:**
the format is **append-only** and **no existing certificate kind changes
meaning**.  A file that verified before this session verifies after it, byte
for byte, to the same verdict.  Every check below is stated as additive.

## 1. Part A — the sparse-route certificate kind (design registered before code)

The sparse route proves `mult_X(λ,δ) = a` by
`nullity_p([E; ev_X]) = 0` at a single prime, which by `rank_p ≤ rank_Q ≤ a`
(`docs/sparse_det_route.md`, Lemmas 1–2) proves `mult_X = a` over `Q`.  The
nullity itself is decided by the session-42 Wiedemann certificate (Lemma 4): a
Berlekamp–Massey minimal polynomial of degree exactly `n_χ` with `f(0) ≠ 0`
proves the preconditioned `M = D_2 F^T D_1 F D_2` nonsingular, hence
`F = [E; ev]` of full column rank.  **No randomness enters that implication**;
`D_1, D_2, u, b`, the row compression and the seeds decide only whether a run
is conclusive.

I register the following design commitments for the new kind
(name `sparse_nullity`), to be documented in `docs/artifacts.md` and
`tools/verify/FORMAT.md` and implemented in `tools/verify/`:

1. **It records the recipe, not the matrix.**  The cell `(n, r, λ, δ, a)`, the
   conventions, the declared field (see §2), the variety, the pinned evaluation
   points **as substitution data** (so the verifier rebuilds them and checks
   they lie on the variety, exactly as `full_rank` does — never a bare list of
   numbers), the compression levels and seeds used, the Wiedemann seed(s) of the
   conclusive run, and the claimed nullity `k`.  For `k > 0` it additionally
   records the checked kernel candidates (χ-coordinate vectors, or their
   expansion to the monomial basis) and the complementary nonsingularity data.

2. **The verifier re-derives, it does not trust.**  Given the recipe it rebuilds
   `V_χ`, the stacked simple raising operators `E`, and the evaluation rows —
   in its own code, importing nothing from `analysis/` — and then decides the
   nullity itself.  For `k = 0` it runs its own Berlekamp–Massey/Wiedemann on
   the rebuilt `[E; ev]` (with its own randomness; the recorded seeds are
   provenance, not trust, since a conclusive NONSINGULAR verdict is
   seed-independent) and confirms degree `= n_χ`, `f(0) ≠ 0`.  For `k > 0` it
   checks each recorded kernel vector by the sparse product `[E; ev] y = 0`,
   checks their independence exactly, and confirms `nullity ≤ k` by a Wiedemann
   certificate on `[E; ev; R]` with `k` fresh dense rows.

3. **The soundness statement the checker prints** is exactly Lemma 2's:
   `nullity_p([E; ev_X]) = 0 ⟹ mult_X(λ,δ) = a` over `Q`, provided the points
   lie on `X` (which rebuilding from substitution data checks).

Registered prediction (A-scope): the verifier will re-derive the full
conclusion, at both house primes, for **every dense-route cost class it can
afford within the session's compute budget**, and I register now that the
largest sparse cells (`n_χ` up to 70 027) cost a full χ-build plus a Wiedemann
sequence each and cannot all be re-run in one session — the report will state,
cell by cell, which the verifier re-derived and which rest on the recorded
Wiedemann certificate plus the reproducible recipe.  That split is the honest
content of "coverage," not a shortfall discovered afterward.

## 2. Part A4 — the field distinction, registered as a soundness rule

`rank_p ≤ rank_Q`.  Therefore:

* a mod-`p` **full column rank** (`nullity_p = 0`) certifies characteristic
  zero: `mult = a`, `i = 0`.  **Sound.**
* a mod-`p` **kernel** of dimension `k` certifies only `nullity_p = k`, hence
  `mult ≥ a − k`, i.e. `i ≤ k` — an **upper bound on the ideal codimension**,
  and **no** characteristic-zero ideal membership.  To prove `i ≥ 1` (a genuine
  bite) one must exhibit a **characteristic-zero** kernel vector and verify it
  exactly (the existing `hwv` kind with `modulus: null`).

The trap this is registered to prevent: session 62's Gram route uses
`rank(Θ*Θ) = rank Θ`, which holds **only in characteristic zero** (a nonzero
vector can be isotropic mod `p`).  A mod-`p` Gram rank therefore certifies
**nothing** about `rank Θ`.

Design commitment: introduce a **declared field** into the format.

* For the new kinds (`sparse_nullity`, and the Gram/`Θ⁺` shapes of §4) the
  `field` key is **required**; its value is `"Q"` (an exact characteristic-zero
  computation, or a multimodular lift certified over `Z`) or `"F_<p>"` (a single
  finite field).
* A Gram-route rank claim (`rank(Gram) = rank(Θ)`, the char-0 identity) is
  accepted **only** with `field: "Q"`; a Gram certificate declaring a finite
  field is rejected as **UNPARSEABLE** with the reason.
* A `sparse_nullity` or `full_rank` certificate over `F_p` may conclude `mult = a`
  over `Q` **only** through the full-rank (`nullity = 0`) direction; a `k > 0`
  claim over `F_p` is reported as a mod-`p` bound and never as a char-0 ideal.
* For the existing kinds (`hwv`, `matrix`, `full_rank`) `field` is **optional and
  additive**: absent, the verifier infers the field from `modulus`/`prime`
  exactly as today (so all 370 committed certificates keep verifying unchanged);
  present, it is checked for consistency with `modulus`/`prime`.

Registered invariant: the self-test will contain a case that **must be rejected**
— a Gram-style rank claim carrying a finite field — so the distinction is
enforced by a test, not only by prose.

## 3. Part A3 — the back-fill, and what "insufficient data" means

`results/s60_cells.jsonl` retains, for each of the 419 measured cells: `lam`,
`delta`, `a`, `K`, the evaluation seeds (`det`/`red`/`wied`), the compression
levels, the primes, and per-prime per-side Wiedemann diagnostics (status,
Berlekamp–Massey degree, `f0`, rows, nnz).  264 of the 419 ran the sparse route.

Registered predictions:

| id | prediction | prior |
|---|---|---|
| A1 | all 264 sparse cells have, in the retained record, the seeds and levels needed to write a reproducible `sparse_nullity` certificate for `mult_det = a` | 0.90 |
| A2 | the determinant-side verdict of every one of the 264 is `NONSINGULAR` (nullity 0) at both primes in the retained diagnostics | 0.97 |
| A3 | the independent verifier re-derives `mult_det = a` for every sparse cell it can afford (a spread by `n_χ` across the session budget); no re-derivation contradicts the banked value | 0.90 |
| A4c | at least one field of the recipe is missing for some cells (e.g. the fresh points are recorded by seed, not as substitution data, so a pinned-point rebuild needs the seed + the drawing convention) and is named as a recipe caveat rather than silently reconstructed | 0.55 |

If the retained data is insufficient to certify a cell, it is **reported as an
uncertified claim with the reason**, never re-run to manufacture a certificate
(stopping rule, brief): the scope of what is unwitnessed is itself the finding.

## 4. Part A5 — the shapes sessions 62/63/64 are producing

Sessions 62, 63, 64 (and 65) have **not landed** in this clone at session start
(no `docs/s6{2,3,4,5}_*`, no `results/PREREG_s6{2,3,4,5}.md`, no
`results/certs/s6{2,3,4}*`).  This is expected — C6 is wave 1, ahead of them.
The coordination this session can do is therefore to **define the certificate
shapes their outputs must target**, from the mathematics already banked (the
s56 Foulkes engine, `docs/s56_report.md`):

* **`Θ⁺` rank / Gram** (s56's engine, s63's route): `mult_det = rank Θ⁺` on the
  λ-isotypic part `= (rank of β on that part)/f_λ`, `β = K∘K` the Hadamard
  square of the exact integer bracket Gram.  This is a `matrix` certificate with
  a rank claim (s56 already committed eight), now **required to declare
  `field: "Q"`** because `rank β = rank Θ⁺` is the char-0 Gram identity.
* **padded outputs** (s64's route): `full_rank`/`sparse_nullity` with
  `variety: padded_permanent`, under the same field discipline.

Design commitment: document these usages in `FORMAT.md`/`artifacts.md`, and make
the verifier enforce the field rule on them, so that when 62–64 land their
outputs have a machine-reproducible home that already exists.  Registered
expectation: no code from 62–64 is available to run, so A5 is a **format and
enforcement** deliverable, verified by self-test, not a back-fill of their
cells.

## 5. Part B — degeneration as a full-rank certifier (measurement, registered before running)

`rank(in Θ) ≤ rank Θ` for an initial-term degeneration under any term order, so
**full column rank of the initial map certifies full column rank of the
original**, hence `mult = a`; that is the only inference permitted.

The concrete instrument I will implement and its one-directional soundness,
registered now:

> **The leading-position (term-order) certifier.**  Fix a term order.  Take the
> matrix `F = [E; ev]` (columns = the `n_χ` χ-basis monomials; full column rank
> `⟺ mult = a`).  Assign each nonzero position a key from the term order; each
> column's *initial position* is its top-key nonzero entry.  If the `n_χ` columns
> have **distinct** initial positions with nonzero entries, the columns are
> linearly independent (the standard leading-term argument), so `F` has full
> column rank and `mult = a`.  This is `rank(in F) ≤ rank F` with `in F` the
> initial-position pattern; a **failure to find distinct initial positions is
> uninformative** — never evidence of a rank drop, because the inequality runs
> one way only.

For the evaluation rows the key includes the point-coordinate monomial (the
points are lifted to a generic 1-parameter family / a degenerate limit point,
so the ev entries carry a term order); for the constant raising-operator rows
the key is the row order.  The initial map is thus evaluation at a
term-order-degenerate configuration together with the raising skeleton, and its
full column rank certifies the original.

Registered predictions:

| id | prediction | prior |
|---|---|---|
| D1 | the certifier is **sound**: on every block it certifies, `python-flint`/Wiedemann confirms full rank (0 false certifications) | 0.97 |
| D2 | it certifies full rank on a **nonzero fraction** of session 56's 40 blocks | 0.70 |
| D3 | it certifies full rank on a nonzero fraction of a sampled set of session 60's cells | 0.60 |
| D4 | where it certifies, it is **strictly cheaper** than the Wiedemann/dense rank it replaces (near-linear in `nnz` vs `O(n_χ·nnz)`) | 0.85 |
| D5 | a rank drop in the degeneration is observed on some block and is recorded as **uninformative**, not as an obstruction | 0.60 |

Stopping rule (registered): a rank drop in the degeneration is **never** written
as evidence of an obstruction.  If one is observed it is logged as uninformative
and the session moves on.  This is why the Rogers–Ramanujan framing was set
aside in planning — it aimed the machinery at obstruction discovery, which the
one-directional inequality forbids.

Deliverable: `results/s67_degeneration.md` with the certification fraction, the
measured speedup where it certifies, and the fraction of the closure queue
(`results/s60_tail_census.md`) whose closing cells it would accelerate — so a
future session can price reserve E2.

## 6. Part C — two engineering defects (registered with the regression each needs)

* **C1.**  `tools/verify/verify.py`: a large `nonvanishing_minor` determinant
  fails the `content` line on Python's integer-to-string conversion limit
  (`ValueError: Exceeds the limit (4300 digits)`), **after** the rank checks have
  already passed (flagged by s56).  Fix: one `sys.set_int_max_str_digits` call.
  Regression: a self-test `matrix` certificate whose `nonvanishing_minor`
  determinant exceeds 4300 digits — which fails today and must pass after.

* **C2.**  The int64 multiset-combinadic monomial code
  (`analysis/wk9_s42_orbits._codes`, used unchanged by `analysis/wk9_s45_build`)
  asserts `comb(L + δ − 1, δ) < 2^63` and so confines the session-45 build to
  `δ_close ≤ 18` at `r = 5` (`L = 70`), which blocks 183 of the 1 075 closing
  cells (`results/s60_tail_census.md`: 892 buildable today).  Fix: widen the
  code so the assertion no longer binds, **without changing any banked value**.

Registered predictions:

| id | prediction | prior |
|---|---|---|
| C1p | after the fix, the oversized-minor self-test passes and every existing self-test still passes | 0.95 |
| C2p | after widening, the number of buildable closing cells rises from 892 toward 1 075; I register the new figure will be reported exactly | 0.9 |
| C2b | on a sample of already-reachable cells (`δ_close ≤ 18`), the widened code produces **bit-identical** `n_χ`, `col_of`, `sgn` (up to the existing per-orbit sign convention) and raising-operator matrices to the int64 code | 0.9 |

Stopping rule (registered, brief): widening the monomial code must not alter any
banked value.  If it does, that is a defect in one of the two versions, and
**finding out which is more important than shipping the widening** — the session
reports the discrepancy and does not ship until it is understood.

## 7. Deliverables

`results/PREREG_s67.md` (this file); the format additions in
`docs/artifacts.md` and `tools/verify/FORMAT.md`; the checker in
`tools/verify/verify.py` (+ `tools/verify/layer3.py` for the sparse re-derivation)
and self-test cases for the new kind and both defects in
`tools/verify/selftest.py`; the 264 back-filled certificates under
`results/certs/s60/` (or the named shortfall); the degeneration measurement
`results/s67_degeneration.md`; the widened monomial code with its bit-identity
report; `docs/s67_report.md`; code under `analysis/wk10_s67_*.py` and
`tools/verify/`; verifier reports under `results/`.  Delivered as the single-ref
bundle `s67_certification.bundle` (+ `.md5`), prerequisite `226b4ef1`.
