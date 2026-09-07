# Session 67 — certification, degeneration, and two engineering defects

Batch 10, wave 1 (C6).  Branch `s67-certification` off `main` at `226b4ef1`
(ancestry gate passes).  Pre-registration `results/PREREG_s67.md` (committed
before any measurement).  Ungated and deliberately early: Part A defines the
certificate kind that sessions 63 and 65 will need, so the format lands before
the batch's most load-bearing claims are produced.  Labels: **proved** /
**measured** / **adopted** / **expectation**.  Single-writer files untouched;
`Co-Authored-By` trailer only, no session-link trailer (standing rule, as
sessions 49, 56, 59).

## 0. Verdict

> **The largest body of unwitnessed claims in the programme now has a machine
> checkable, reproducible home, and the format enforces the distinction that
> keeps a mod-`p` computation from being read as a characteristic-zero fact.**
>
> * **Part A.**  A `gct-cert/1` kind `sparse_nullity` for the sparse (Wiedemann)
>   route, with an independent checker that rebuilds `E` and `ev` from scratch and
>   re-derives the nullity itself.  **All 264 of session 60's uncertified
>   determinant claims are back-filled; shortfall: none.**  21 were independently
>   re-derived this session (6 at full soundness), every one confirming
>   `mult_det = a`.  A **declared field** is added and required for the new kinds:
>   a finite-field full column rank certifies characteristic zero, a finite-field
>   kernel does not, and a Gram-route rank is accepted only over `Q` — so the
>   `rank(Θ*Θ) = rank Θ` trap that session 62's route would otherwise fall into
>   is closed in the format itself.  The addition is append-only: all 370
>   pre-existing certificates verify unchanged.
> * **Part B.**  A degeneration full-rank certifier, sound and one-directional
>   (`rank(in Θ) ≤ rank Θ`).  It **certifies a genuine class more cheaply** — 27
>   of 32 nontrivial-reducible session-56 cells, at `O(nnz)`, thousands of times
>   cheaper than the rank it replaces — with **0 false certifications**.  Where it
>   falls short it covers 99.4–99.9% of the columns but no more, an intrinsic
>   limit, so a pure-degeneration closure engine (reserve E2) is not worth pricing
>   highly; a hybrid is the only version worth a successor's time.
> * **Part C.**  Both engineering defects fixed with regressions: the
>   integer-to-string limit in `verify.py`, and the int64 monomial code, widened
>   so buildable closing cells rise from 892 to all 1 075 — bit-identically on
>   every already-reachable cell.

## 1. Part A — the sparse-route certificate (`docs/artifacts.md`, `tools/verify/FORMAT.md`)

### 1.1 The kind and the checker

The sparse route proves `mult_X(λ, δ) = a` by `nullity_p([E; ev_X]) = 0` at one
prime, which by `rank_p ≤ rank_Q ≤ a` (`docs/sparse_det_route.md`, Lemmas 1–2)
gives `mult_X = a` over `Q`; the nullity is decided by the session-42 Wiedemann
certificate (Lemma 4).  The new kind `sparse_nullity` records the cell, the
finite field, the variety, the claimed nullity, the evaluation points **as
substitution data** (so they are rebuilt and checked to lie on the variety), the
reproducible recipe (seeds, levels), and the Wiedemann provenance.

The checker (`tools/verify/layer3.py`, `chi_build.py`, `wied_check.c`) does not
trust the recorded verdict.  It **rebuilds `E` and `ev` on the full weight space**
— importing nothing from `analysis/` and **not** using the stabiliser reduction
the original run used, so it independently checks that reduction too — confirms
`nullity_p(E) = a` (E's kernel is the highest-weight space; exact where the cell
densifies, else a two-sided Wiedemann test), and decides `nullity_p([E; ev])`
itself by an exact flint rank (small cells) or its own preconditioned Wiedemann
(large).  It reports **`PASS`** only for a claim it re-derived, **`RECORDED`** for
a well-formed reproducible certificate it did not re-derive this run (distinct
from `PASS`), and it recomputes the true `N_S` from the cell rather than trusting
any size the certificate declares.

### 1.2 The field distinction (Part A4)

`rank_p ≤ rank_Q`.  A mod-`p` **full column rank** certifies characteristic zero
(`mult = a`, `i = 0`); a mod-`p` **kernel** certifies only `mult ≥ a − k`
(`i ≤ k`) — a bound, never a characteristic-zero ideal.  Session 62's Gram
identity `rank(Θ*Θ) = rank Θ` holds only over characteristic zero.  So every
certificate declares a `field`, **required** for `sparse_nullity` (a finite field)
and for Gram matrices (`matrix_role: "gram"`, which must be `"Q"`), **optional and
consistency-checked** on the older kinds.  A Gram matrix over a finite field, and
a `sparse_nullity` over `Q`, are both rejected as `UNPARSEABLE`.  The distinction
is enforced by self-test, not only prose.

### 1.3 The back-fill (`results/s67_verify_sparse.md`)

All **264** sparse-route determinant claims were certifiable from the retained
`results/s60_cells.jsonl` — the seed, `K`, bound, levels, and a `NONSINGULAR`
(nullity 0) verdict at both house primes — so all 264 `sparse_nullity`
certificates were written (`results/certs/s60/*_det_sparse_p2147483647.json.gz`,
821 KB total).  **Shortfall: none.**  All 264 structurally validate (schema,
field, points on the variety, and recorded `N_S` matching the true dimension).
**21 were independently re-derived** — 6 at full soundness spanning `|Stab| ∈
{1,2,6}` and `δ ∈ {6,8,11,14}` (both the int64 and the object monomial-code
paths), 15 more confirming `nullity_p([E; ev]) = 0` — all `mult_det = a`, none
contradicting the banked value.  Re-deriving a cell costs one build plus one
Wiedemann sequence (the cost of the original measurement): the certificate is
checkable on demand, not cheaply checkable — inherent to an algorithmic proof,
and the motivation for Part B.

### 1.4 Coordination with sessions 62–64 (Part A5)

Those sessions have not landed in this clone (expected — C6 is wave 1), so the
deliverable is the **format they must target**: session 63's `Θ⁺`/Gram ranks as
`matrix` certificates with `matrix_role: "gram"`, `field: "Q"`; session 64's
padded-side proofs as `full_rank`/`sparse_nullity` with
`variety: "padded_permanent"`.  Documented and enforced ahead of them.

## 2. Part B — degeneration as a full-rank certifier (`results/s67_degeneration.md`)

For a term order on the columns of `F = [E; ev]` (the coordinates of the
Plücker/coordinate ring), the initial map keeps each row's leading column, and
`rank(in F) = #distinct leading columns ≤ rank F` for **every** term order.  So
`#distinct leading columns = n_χ` certifies full column rank, hence `mult = a`; a
shortfall certifies nothing and is **never** evidence of a rank drop or an
obstruction — the inequality runs one way only.  (This is exactly why the
Rogers–Ramanujan framing, which aimed such machinery at obstruction discovery,
was set aside.)  Cost: one `O(nnz)` pass per term order, against `O(n_χ · nnz)`
for a Wiedemann sequence.

Measured on session 56's 40 cells and a session 60 sample (`analysis/wk10_s67_degeneration.py`):

* **Sound.**  Across all 51 cells (all `mult = a`), 0 false certifications; the 27
  certified reducible-side cells were re-ranked exactly by flint.
* **Certifies a class more cheaply.**  On the point-free reducible side it fully
  certifies `mult_red = a` for **27 of 32** nontrivial session-56 cells — the
  skewed weights — at `O(nnz)`, thousands of times cheaper than the rank it
  replaces.
* **Where it fails, the failure is intrinsic.**  On the larger cells and all the
  length-5 cells it covers 99.4–99.9% of the columns but falls a small bounded
  gap short: `#distinct realizable leads ≤ rank`, and the two genuinely differ
  near the near-rectangular corner — exactly where a determinant equation would
  first appear.  The determinant side is weaker still: the `a+8` **dense**
  evaluation rows all lead the single top column, so degeneration is suited to
  the point-free `(★)` side (and session 63's combinatorial Gram target), not to
  the point-based side.
* **For pricing reserve E2.**  The closure queue is walked by determinant-side
  full-rank checks, where the certifier is weakest, so a pure-degeneration
  closure engine accelerates only a small (small-`n`) fraction.  **Reserve E2 is
  not worth pricing highly as a pure certifier;** the 99%+ near-cover points at a
  *hybrid* (combinatorial cover plus a small exact residual on the ~0.1–0.4%
  uncovered columns), which shaves the constant but keeps the complexity class.

## 3. Part C — two engineering defects

### 3.1 `verify.py` integer-to-string limit (`tools/verify/`)

A large `nonvanishing_minor` determinant (any full-rank minor of order ≳ 300 with
this programme's entries exceeds 4300 digits) was rendered into the report line
**after** the rank checks passed, hitting Python's int→str cap and reporting a
valid certificate as `UNPARSEABLE` (session 56's defect).  Fixed by one
`sys.set_int_max_str_digits` call; self-test case 7 (a 4515-digit determinant)
fails before the fix and passes after.

### 3.2 The int64 monomial code, widened (`results/s67_monomial_widening.md`)

The multiset combinadic `code(m) = Σ_k C(m_k + k, k+1)` (`wk9_s42_orbits._codes`,
used by the s45 build) overflows int64 at `δ = 20` (`r = 5`, `L = 70`), capping
tail closure.  Widened: the int64 path is kept **byte-for-byte** where it did not
overflow, an exact Python-integer path takes over above it.  Buildable closing
cells rise from **892** (session 60's conservative `CODE_SAFE_DELTA = 18` flag;
the true int64 reach was `δ ≤ 19` = 1 048) to **all 1 075** — the smallest
`δ_close = 20` cell `(57,17,2,2,2)` now builds (`N_S = 169 331`, `n_χ = 36 488`,
15 s).  `analysis/wk10_s67_bitident.py` is the regression: seven already-reachable
cells build **bit-identically** (`N_S`, `|Stab|`, `n_χ`, `col_of`, `sgn`, the full
`E`) under the int64 and the object path, at cells up to `n_χ = 70 027`, plus the
`δ = 20` unblock.  The stopping rule held: no banked value changed.

## 4. Pre-registration scorecard

| id | prediction | outcome |
|---|---|---|
| A1 | all 264 have the seeds/levels to write a certificate | **confirmed** |
| A2 | all 264 have det-side `NONSINGULAR` (nullity 0) at both primes | **confirmed** |
| A3 | the verifier re-derives every sparse cell it can afford; none contradicts | **confirmed** (21 re-derived, 0 contradictions) |
| A4c | some recipe field needs the seed + convention (points by seed) | **confirmed** (points reconstructed from the seed, recorded as substitution data) |
| D1 | 0 false certifications | **confirmed** (0/51; 27 re-ranked exactly) |
| D2 | degeneration certifies a nonzero fraction of s56's cells | **confirmed** (27/32 reducible side) |
| D3 | ditto for a s60 sample | **refuted** for full certification (0/11; 99.5%+ coverage) — the near-cover finding |
| D4 | where it certifies, strictly cheaper | **confirmed** (`O(nnz)` vs `O(n·nnz)`) |
| D5 | a rank drop observed and recorded as uninformative | **confirmed** (the gap columns; recorded uninformative, never an obstruction) |
| C1p | oversized-minor self-test passes, all others still pass | **confirmed** (10/10) |
| C2p | buildable count rises toward 1 075 | **confirmed** (892 → 1 075) |
| C2b | bit-identical on reachable cells | **confirmed** (7 cells) |

Unregistered: the adversarial audit's finding that `RECORDED` must be distinct
from `PASS` and the true `N_S` never trusted from the certificate — both fixed;
the forged-size exploit now `FAIL`s and the tool reports `PASS` only for a claim
it re-derived.

## 5. Honest boundary

* **Proved / enforced:** the field distinction and the append-only property (all
  370 pre-existing certificates verify unchanged; 10/10 self-test); the
  degeneration inequality (one direction); the bit-identity of the widened code.
* **Independently re-derived:** 21 of the 264 sparse cells (`mult_det = a`); the
  27 reducible cells the degeneration certifies (exact flint).
* **Recorded, not re-derived this run:** the other 243 sparse certificates —
  reproducible on demand, reported `RECORDED`, never `PASS`.  The cost of
  re-deriving a large cell is the cost of the original measurement.
* **Not this session's:** sessions 62–64 have not landed; Part A5 is a format and
  enforcement deliverable, not a back-fill of their cells.
* **The one intrinsic negative:** the pure degeneration certifier cannot close
  the gap on the balanced/large cells (`#realizable-leads < rank` near the
  rectangular corner); that is a property of the map, not of the search.

## 6. Deliverables

`results/PREREG_s67.md`; this report; the format additions in `docs/artifacts.md`
and `tools/verify/FORMAT.md`; the checker (`tools/verify/verify.py`,
`layer3.py`, `chi_build.py`, `wied_check.c`) and self-test (`selftest.py`, 10
cases); the 264 back-filled certificates under `results/certs/s60/` with the
coverage record `results/s67_verify_sparse.md` and the structural report
`results/s67_verify_sparse_parse.md`; the degeneration measurement
`results/s67_degeneration.md` (+ `.json`); the widened code with
`results/s67_monomial_widening.md` and the regression `analysis/wk10_s67_bitident.py`;
code under `analysis/wk10_s67_*.py`.  Delivered as the single-ref bundle
`s67_certification.bundle` (+ `.md5`), prerequisite `226b4ef1`.
