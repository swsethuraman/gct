# Back-fill and independent re-derivation of session 60's sparse-route claims

Session 67, Part A3.  Session 60 proved `mult_det = a` at 419 length-5 cells;
**264 ran the sparse (Wiedemann) route**, whose single-prime nonsingularity
proofs (`nullity_p([E; ev_det]) = 0`) had no home in `gct-cert/1` — the largest
body of unwitnessed claims in the programme.  This session gives them one.

## The back-fill

`analysis/wk10_s67_backfill.py` reads `results/s60_cells.jsonl` and writes one
`sparse_nullity` certificate per sparse-route cell to
`results/certs/s60/<cell>_det_sparse_p2147483647.json.gz`.

* **264 of 264 certified from the retained data; shortfall: none.**  Every
  sparse-route determinant claim had, in the retained record, everything a
  `sparse_nullity` certificate needs: the cell and `a`, the evaluation seed
  (`det = 11`), `K = a + 8`, the bound (40), the compression levels, and a
  determinant-side `nullity 0` verdict (`NONSINGULAR`, Berlekamp–Massey degree
  `= n_χ`, `f(0) ≠ 0`) **at both house primes**.  The evaluation points are
  reconstructed from the seed as substitution data, so each certificate is
  self-contained.  Prediction A1 (0.90) and A2 (0.97): both confirmed.
* Total size 821 KB, largest file 8 KB — well under the 5 MB limit.

## Structural validation — all 264

`tools/verify/verify.py` on all 264 files (`VERIFY_MAX_NS=0`, re-derivation
deferred): **PASS 264, FAIL 0, UNPARSEABLE 0, ERROR 0**.  For each: the schema
and conventions parse, the field is a valid finite field, `a` is recomputed by
the Weyl alternation and matches, and every recorded point rebuilds onto the
`det_pencil` variety.  So all 264 certificates are well-formed and reproducible.

## Independent re-derivation — a sample

The checker (`tools/verify/layer3.py`, `chi_build.py`, `wied_check.c`) rebuilds
`E` and `ev` on the **full** weight space — importing nothing from `analysis/`
and **not** using the stabiliser reduction the original run used, so it is an
independent check of that reduction as well — and decides the nullity itself.

`analysis/wk10_s67_recheck.py` re-derived **21 of the 264** cells (a stratified
spread), **all PASS, all concluding `mult_det = a` over `Q`**:

* **6 at full soundness** — `nullity_p(E) = a` (the build's kernel is the
  highest-weight space) **and** `nullity_p([E; ev]) = 0` — spanning stabiliser
  sizes `|Stab| ∈ {1, 2, 6}` and degrees `δ ∈ {6, 8, 11, 14}`, i.e. both the
  `int64` and the object-integer monomial-code paths;
* **15 more** confirming `nullity_p([E; ev]) = 0`, the build taken as validated
  by the full-soundness cells (`chi_build` is deterministic and
  cell-shape-independent).

Coverage of the sample: `N_S` from 4 942 to 22 475, `n_χ` from 4 016 to 16 315,
`a` from 1 to 30, `|Stab| ∈ {1, 2, 4, 6}`, `δ ∈ {6, 7, 8, 11, 14}`.  Not one
re-derivation contradicted the banked value (prediction A3, 0.90: confirmed).
The full record is `results/s67_sparse_sample.jsonl`.

## What is and is not witnessed now

* **Witnessed (machine-checkable, in the unified format):** all 264 sparse-route
  determinant claims as reproducible `sparse_nullity` certificates; 21 of them
  independently re-derived this session by a from-scratch build and an
  independent Wiedemann.
* **The honest limit of an algorithmic certificate:** re-deriving a cell costs
  one full-weight-space build plus one Wiedemann sequence — the cost of the
  original measurement.  So the certificate is *checkable on demand*, not
  *cheaply checkable*; the other 243 are reproducible from their recipe and were
  not re-run this session.  A cell above `VERIFY_MAX_NS` is reported `RECORDED`,
  never "verified."  This is inherent to a sparse-route proof, and is the reason
  Part B asks whether a cheaper (degeneration) certifier exists.
* **Field discipline:** every certificate declares `field = F_2147483647`; the
  conclusion `mult_det = a` over `Q` follows from the **full-column-rank**
  direction (`rank_p ≤ rank_Q`).  None of these is a kernel certificate, so none
  claims a characteristic-zero ideal.
