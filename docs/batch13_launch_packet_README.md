# Batch 13 — launch packet

**Reference documents.**  Computational inputs come from the frozen repository
and from named supplemental archives — not from this packet.  These are the
documents a session reads, at commit `main` as of the batch-13 freeze; the
repository copies are authoritative.

The computational inputs live at:

    results/s74/                          the 274-row source and its columns
    results/s79_cells.jsonl, s79_per6.jsonl   the six-row and cubic scans
    results/astra/S3/degree13_conversion/ S3's degree-13 delivery -- read its
                                          README first; three files totalling
                                          19.5 MB are over the repository limit
                                          and are supplied separately
    results/s74/source.json               the integral degree-13 fillings that
                                          are B13-01's primary source

## Give every session

    batch13_worker_preamble.md    tier 1 -- read in full first
    batch13_board.md              the controlling document; find your B13-xx entry
    batch13_corrections.md        what the first draft got wrong and why
    stocktake_batch12.md          the context in one document
    brief_wording.md              binding on the report

## Cited as inputs by particular assignments

    transfer_lemma.md             Prop. 8 -- B13-04, B13-05, B13-07, B13-09
    washout_lemma.md              Thm 2 and Thm 3(1), the length-<=5 exclusion --
                                  B13-05, B13-07, B13-09.  Load-bearing: it is
                                  what makes s79's 210 checks a full statement.
    s74_final_review.md           the goal cell's verified state -- B13-01, B13-02
    rung13_reducible.md           the degree-13 measurement -- B13-01, B13-04
    s79_review.md                 Part 1, verified 60/60 -- B13-07
    s79_part2_review.md           what the degree-9 scan covers -- B13-07, B13-09
    wk12_int_pred13_audit.log     the fifteen predecessors, audited -- B13-04
    batch11_plan.md               C3, the rank S screen -- B13-02
    lmr_cell.md                   the goal cell
    compact_circuit.md            the filling/circuit conventions
    sparse_det_route.md           Lemma 2, rank_p <= rank_Q

## Not in the packet

Everything else is tier 3 and lives in the repository.  A session that finds
itself reconstructing context from tier 3 to answer a question its assignment
should have answered must say so in its report.

## Repository

`https://github.com/swsethuraman/gct.git`.  Record `git rev-parse main` in the
pre-registration.  If the clone lacks `docs/batch13_board.md`, it is an older
tree and the bundle will not apply.
