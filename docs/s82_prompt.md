# s82 — the cubic side at `r = 7` and `r = 8`

`board_numbering: batch13`.  Read `docs/batch13_worker_preamble.md` first.

## Mission

`I(D_r^{per₃})_δ` at two lengths nobody has looked at.  One scan per `(r, δ)`
covers every weight of that length and degree through Prop. 8(1), so this is the
cheapest information per second available to the batch.

## Task

`analysis/wk12_s79_per6.py` made length-general (`r = len(μ)`), on the unchanged
engine, at `r = 7` then `r = 8`, by degree from the bottom, both primes, in `N_S`
order, until the build wall.  Session 41's family `per₃(Σ_{i≤r} s_i A_i)`, seed
41, bound 40, `a + 8` points, a drop re-checked at `3a + 24` fresh points.

**Include every length ≤ `r`, not only length exactly `r`.**  That is the
quantifier session 79's degree-9 scan missed and it is the falsifier here: a
`μ` shorter than `λ` pairs with `λ` under Prop. 8(2) because `μ` interlaces it.
Enumerate the census yourself and report it.

Report the boundary you reach as a degree with its `N_S·δ`, and price the first
unreached degree.  If s80's builder has landed and passed, use it and say so; if
not, use the existing one and report the ceiling you hit.

## Calibration

Before the queue, at each length: reproduce a banked cell of the record at that
length if one exists, and in any case run the `per_form(3)`-versus-hand-permanent
control and the `per₃`-versus-`det₃`-restriction control that s79 added
(`results/s79_per6_control.json`) — they are what distinguish the family from a
generic cubic.

## Predictions and falsifiers

- **P1 (0.6):** empty through `δ = 8` at both lengths.
- **P2:** a nonzero weight → the protocol, and stop.
- **F1:** the controls fail → stop, report; nothing is a result.

## Deliverables

`results/PREREG_s82.md`; `results/s82_per7.jsonl`, `results/s82_per8.jsonl`; the
censuses; the priced boundary; `docs/s82_report.md`; bundle + `.md5`.
