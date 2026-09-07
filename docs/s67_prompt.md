# Session 67 (C6) — certification, degeneration, and two engineering defects

Batch 10, wave 1.  Ungated, and deliberately early: its Part A defines the
certificate kind that sessions 63 and 65 will need, and back-filling
certificates after the batch's most load-bearing claims are produced is the
outcome this session exists to prevent.  Base commit `226b4ef1`.
**Read `docs/batch10_worker_preamble.md` first**, then `docs/batch10_plan.md`
§4 (C6), `docs/artifacts.md`, `tools/verify/FORMAT.md`, `tools/verify/verify.py`,
`docs/sparse_det_route.md`, and `docs/s60_report.md` §7.

## Why this session

Session 60 reports `mult_det = a` at 419 cells.  **264 of them carry no
checkable certificate** — their proof is algorithmic, by the sparse Wiedemann
route, and nobody has proposed a format for it.  That is the largest body of
unwitnessed claims in the programme, and the next batch is about to scale two
new engines on top of it.

## Part A — certificates

1. Design and document a **`gct-cert/1`** kind for the sparse-route
   nonsingularity certificate.  It must record at minimum: the seeds, the
   levels, the pinned evaluation rows, and the checked kernel candidates —
   enough that a reader with `tools/verify/verify.py` and no access to the
   original run can re-derive the conclusion.  Write it into `docs/artifacts.md`
   and `tools/verify/FORMAT.md` in the style already used there.
2. Implement the checker in `tools/verify/verify.py`, with a case in
   `tools/verify/selftest.py`.
3. **Back-fill session 60's 264 uncertified cells.**  If the original run data is
   insufficient for some, say which and why rather than regenerating silently.
4. **Separate finite-field full-rank certificates from characteristic-zero
   kernel certificates in the format itself.**  This is not cosmetic:
   `rank_p ≤ rank_Q`, so a mod-`p` full rank certifies characteristic zero,
   while a mod-`p` *kernel* certifies nothing — and session 62's Gram route
   (`rank(Θ*Θ) = rank Θ`) is valid only in characteristic zero.  The format must
   make it impossible to lose that distinction downstream.  Add the declared
   field and require it.
5. Ensure every new `Θ⁺`, Gram and padded output from this batch has a
   machine-reproducible record.  Coordinate with the shapes sessions 62, 63 and
   64 are producing; read their reports if they have landed.

## Part B — degeneration as a full-rank certifier, one direction only

`rank(in Θ) ≤ rank Θ` for an initial-term degeneration under any term order.
**Therefore full rank of the initial map certifies full rank of the original**,
and that is the only inference permitted.

1. Choose a term order on the Plücker algebra and implement the initial map.
2. Test it on known negative blocks — session 56's forty cells, and a sample
   from session 60's 419 — and measure how often it certifies full rank and how
   much cheaper it is when it does.
3. **A rank drop in the degeneration is never evidence of an obstruction.**  The
   inequality runs the wrong way.  If you observe one, record it as
   uninformative and move on.  This is the reason the associated
   Rogers–Ramanujan framing was set aside during planning: it aimed the
   machinery at obstruction discovery, which it cannot do.
4. Report the fraction of the closure queue this would accelerate, so a future
   session can price reserve E2.

## Part C — two engineering defects

1. **`tools/verify/verify.py`**: large `nonvanishing_minor` determinants fail the
   `content` line on Python's integer-to-string conversion limit, *after* the
   rank checks have already passed.  Session 56 flagged it.  One
   `sys.set_int_max_str_digits` call, plus a regression case in the selftest
   that would have caught it.
2. **The int64 monomial encoding** of the session-45 build confines tail closure
   to `δ_close ≤ 18`, which blocks **183 of 1 075** closing cells.  Widen it.
   The census (`results/s60_tail_census.md`) records that 892 closing cells are
   buildable today; report the new figure after widening, and confirm that
   existing results are bit-identical across the change on a sample of cells
   that were already reachable.

## Success

Unified verifier coverage for the batch; the 264 cells certified or their
shortfall named; at least one class of negative blocks certified more cheaply by
degeneration; both defects fixed with regression tests.

## Stopping rules

- Do not change the meaning of any existing certificate kind.  `gct-cert/1` is
  additive; the format is append-only in the same sense the repository
  configuration is.
- If back-filling reveals that a session-60 claim cannot be certified from the
  data retained, **report it as an uncertified claim rather than re-running the
  cell to manufacture one.**  The scope of what is unwitnessed is itself the
  finding.
- Widening the monomial code must not alter any banked value.  If it does, that
  is a defect in one of the two versions and finding out which is more important
  than shipping the widening.

## Deliverables

`results/PREREG_s67.md`; `docs/s67_report.md`; the format additions in
`docs/artifacts.md` and `tools/verify/FORMAT.md`; the 264 back-filled
certificates; the degeneration measurement as `results/s67_degeneration.md`;
selftest cases for both defects; code under `analysis/wk10_s67_*.py` and
`tools/verify/`; bundle `s67_certification.bundle` + `.md5`.
