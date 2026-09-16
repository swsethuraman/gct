# B18-06 review — the empty shortlist

Report: `work/batch15_workers/B15-06/docs/b18_06_report.md`. Started from `8f7ab3bb`,
tree `f0428d81`. Pilot `analysis/b18_06_pilot.py`, certificates `results/b18_06/`.

## Verdict

**ACCEPT, and the empty shortlist is the right answer.** A nomination the evidence
does not support would have cost the batch more than this. The slot says so and
delivers the negative cleanly.

This is also the most consequential delivery of the batch, because it reached B18-01's
degree-five family **independently** and then closed part of it.

## 1. The dependency it flagged, discharged

The report records: "The results rely on the census values of `a`, taken from the tree
rather than recomputed." I recomputed every one, from the plethysm `h_d[h_4]` by
dynamic programming and the Weyl alternant — my own lineage, not the tree's:

| cell | `d` | `a` (mine) | 06's census |
|---|---:|---:|---|
| `(9,7,2,1,1)` | 5 | 1 | 1 |
| `(7,7,4,1,1)` | 5 | 1 | 1 |
| `(12,2,2,2,2)` | 5 | 1 | 1 (control) |
| `(15,3,2,2,2)` | 6 | 1 | 1 |
| `(11,9,2,1,1)` | 6 | 1 | 1 |
| `(14,4,2,2,2)` | 6 | **2** | 2 |
| `(16,2,2,2,2)` | 6 | 1 | family |
| `(20,2,2,2,2)` | 7 | 1 | family |

**8/8 exact**, including the `a = 2` cell, which is the one where a census error would
have changed the conclusion. The `(4d−8, 2^4)` family has `a = 1` at `d = 5, 6, 7`
exactly as claimed. I also computed `s = 8` for `(12,2,2,2,2)` earlier in this batch,
matching "the five-row family with the smallest `s` (8)".

That closes the report's own stated weakness. The pilot no longer rests on the tree.

## 2. The convergence, which is why 06 was left alone

06 ran without sight of B18-01 §8. It arrived at the same family — five rows, small
`s`, `a = 1` at low degree — and then did what 01 proposed and did not run. Two slots,
no contact, same target. That is worth more than either result alone, and it is the
return on not briefing 06 mid-flight.

## 3. The operational result, which I think is the batch's most useful output

> `D > 0` forces `i_det >= a − U + 1 >= 1`. So one full-rank determinant evaluation
> closes a cell outright.

The inference is correct. With `U = a`, `D > 0` requires `i_det >= 1`, hence
`m_det = a − i_det <= a − 1`; at `a = 1` that is `m_det = 0`. One exact nonzero
`h_lambda(phi(B))` gives `m_det >= 1` and the cell dies. A **nonzero** used in the one
direction it permits, and it costs seconds.

Six cells tried, six closed at the **first** determinant point, plus all nine in
B15-02. That is the cheap decision procedure the batch was looking for. It points the
opposite way from what we hoped, but it is the thing we asked for.

## 4. What this does, and does not, do to B18-01's family

Of B18-01's 23 degree-five cells, all with `a = 1`:

- `(4,4,4,4,4)` — excluded by 01's null-cone argument (Prop. 8.4);
- `(12,2,2,2,2)` — closed here by the Hessian covariant, as the `d = 5` member of a
  family closed at `d = 5, 6, 7`;
- `(9,7,2,1,1)`, `(7,7,4,1,1)` — closed here at the first determinant point.

**Four of 23 closed. Nineteen untested.**

So the family is **not retired**, and I want that stated precisely because the batch
will be tempted to treat it as retired. Six-for-six at the first point moves the prior
hard, but a determinant nonzero is a retirement tool: it can only ever subtract. No
number of closed cells says anything about an untested one.

What *would* retire the family is the remaining nineteen going the same way. At seconds
per cell, that is minutes of work, and it is the natural close-out — not another
carrier build.

This also settles the exchange with Astra: `(12,2,2,2,2)` was nominated as the
feasibility probe, and it is now closed. The probe is moot, but the method Astra was
reaching for — a cheap targeted test rather than a 6-to-57-hour run — is exactly what
06 executed.

## 5. The recorded failure is handled correctly

> "The first compressed kernel computation lost rank in all six cells; the declared
> retry at twice the size gave the correct dimension."

A compressed computation *losing* rank is the dangerous direction: a lost rank reads as
a smaller rank, and a smaller `m` reads as a larger `i`, which is the direction that
manufactures false gaps. It was caught because the retry was **declared in the report
before the run**. Pre-registration did its job. Recorded as a defect, not smoothed over.

## 6. Where I would keep the door open

06's negative is about affordability, and it is well argued: five-to-eight rows have no
determinant equation of their own type and no mechanism produces one; ten rows have
equations but padding is too thin (`q + U − a <= −30` in every assigned cell). I accept
both.

The one thing it does not establish — and does not claim to — is that no five-row cell
has `m_det = 0`. Its evidence is that every cell *tried* has `m_det = 1`. The Kronecker
route (`s = 0` certifies `m_det = 0`) remains the only route that can come back
positive, and it has still not been run on the nineteen. If all nineteen close at a
determinant point, that route becomes irrelevant. If one survives, it becomes the whole
game.

So: run the nineteen. It is minutes, it uses the machinery 06 has already built and
priced, and it either closes the family honestly or finds the one cell worth the
expensive work.

## 7. What enters the index

| id | statement | status |
|---|---|---|
| `one_evaluation_closes_a_cell` | `D > 0` forces `i_det >= a − U + 1 >= 1`. When `U = a`, one exact nonzero determinant evaluation gives `m_det >= 1` and closes the cell outright, in seconds | PROVED |
| `small_s_five_row_family_closed` | The five-row family `(4d−8, 2^4)`, the smallest `s` (= 8) five-row family, is closed by a Hessian covariant nonzero on both closures: `D = 0` wherever `a = 1`, certified at `d = 5, 6, 7` | PROVED; `a = 1` at all three degrees recomputed here |
| `six_cells_closed_at_first_point` | Six five-row cells across `d = 5, 6` — including one with `a = 2` — closed with `D = 0` at the first determinant point, at most 5.2 s and 289 MiB each; plus all nine in B15-02 | MEASURED; all census `a` values recomputed here |
| `no_affordable_cell` | No cell in five-to-eight rows has a determinant equation of its own type, and neither the certified det4 ideal nor any Hessian-minor construction produces a type with `<= 8` rows. Ten-row cells beyond the ten excluded have padding ceiling `0.67–0.84` of `a` and `q + U − a <= −30`. The shortlist is empty | PROVED / MEASURED per §7.2; affordability, not impossibility |
| `compressed_kernel_loses_rank` | A compressed kernel computation lost rank in all six pilot cells; the pre-declared retry at twice the size recovered the correct dimension. Rank loss reads as a smaller `m` and so a larger `i` — the direction that manufactures false gaps. Declare the retry before the run | RECORDED defect |

## 8. On the instruction to slots 02, 03 and 04

Agreed. No cell to take. And the standing order 06 proposes — one determinant full-rank
evaluation before building any carrier — should be in every future five-row brief. It
costs seconds and it closed every cell tried in this batch.
