# Degeneration as a full-rank certifier -- measurement (session 67, Part B)

## The certifier and the one direction it runs

For a term order on the columns of a matrix `F` (the weight-`lambda` monomials -- the
coordinates of the Plucker/coordinate ring), the *initial map* `in(F)` keeps each row's
leading (largest-order nonzero) column.  Its rank is the number of distinct leading
columns, and

        rank(in F)  =  #distinct leading columns  <=  rank(F),

for every term order (pick one row per distinct lead: distinct leads => independent).
So **`#distinct leading columns = n` certifies full column rank**, hence `mult = a`.
A shortfall certifies nothing -- the rank may be full through colliding leads -- so it is
**uninformative and never evidence of a rank drop or an obstruction**.  (This is exactly
why the Rogers-Ramanujan framing, aimed at obstruction discovery, was set aside: the
inequality forbids that use.)  Cost: one `O(nnz)` pass per term order, against
`O(n * nnz)` for a Wiedemann sequence.

The certifier is run on two maps: the **point-free reducible side** `E_red` (Theorem
(star): no dense evaluation rows -- its natural home) and the **determinant side**
`[E; ev_det]` at `K = a+8` generic points.

## Soundness

Across all 51 cells tested (all known `mult = a`), **every** cell the
certifier certified was independently full rank -- 0 false certifications (prediction
D1).  This was checked exactly: all **27** certified reducible-side cells were
re-ranked with `python-flint` (`nullity(E_red) = 0` at every one,
`analysis/wk10_s67_degeneration.py` cross-check).  The determinant side is
`mult_det = a` at every one; the reducible side matches the banked `mult_red`
wherever both were computed.

## Coverage and certification rate

| side | block set | cells (nontrivial) | fully certified | mean column coverage (best d / n) |
|---|---|---|---|---|
| reducible `E_red` | session 56 | 32 | 27 (84%) | 99.53% |
| reducible `E_red` | session 60 sample | 11 | 0 (0%) | 99.74% |
| determinant `[E;ev]` | session 56 | 40 | 3 (8%) | 85.60% |
| determinant `[E;ev]` | session 60 sample | 11 | 0 (0%) | 99.72% |

**The class it certifies.**  On the **point-free reducible side**, the initial map fully
certifies `mult_red = a` for **27 of 32** session-56 cells with a nontrivial
reducible part -- the skewed weights -- at `O(nnz)`, thousands of times cheaper than the
rank it replaces (below).  That is a genuine class of negative blocks certified more
cheaply by degeneration.

**Where it falls short, and why it is intrinsic.**  On the larger cells (and on all the
length-5 session-60 cells) the initial map covers 99.4-99.9% of the columns but falls a
small bounded gap short of `n`.  The gap is not a term-order-search failure:
`#distinct realizable leads <= rank`, and the two genuinely differ near the near-
rectangular corner (`(8,4,4)`, `(6,6,4)`, `(4,4,4,4)`, ...), exactly where a determinant
equation would first appear.  The **determinant side** is weaker still -- the `a+8`
**dense** evaluation rows all lead the single top column, so they add almost no lead
diversity -- confirming degeneration is suited to the point-free `(star)` side (and, by
the same token, to session 63's Foulkes Gram, whose target is combinatorial) and not to
the point-based side.

## Fraction of the closure queue this would accelerate (for pricing reserve E2)

The closure queue (`results/s60_tail_census.md`) is walked by full-column-rank checks
on the determinant side, where the certifier is weakest (dense points).  On the
point-free reducible side it fully certifies only the smallest cells.  So a
pure-degeneration closure engine would accelerate a **small** fraction of the queue --
the small-`n` tail -- and cannot replace the Wiedemann route on the balanced/large
cells that dominate it.  **Recommendation: reserve E2 (a degeneration-accelerated
closure engine) is not worth pricing highly as a pure certifier;** the near-cover
(99%+) points instead at a *hybrid* -- combinatorial cover plus a small exact residual
on the ~0.1-0.4% uncovered columns -- which would shave the constant but keeps the
complexity class, and is the only version worth a successor's time.

## Per-cell (session 60 sample)

| lambda | delta | n_chi | n_red | RED cover | RED cert | DET cover | DET cert |
|---|---|---|---|---|---|---|---|
| `(9, 7, 2, 1, 1)` | 5 | 621 | 409 | 99.760% | no | 99.840% | no |
| `(12, 5, 5, 1, 1)` | 6 | 2795 | 1958 | 99.740% | no | 99.750% | no |
| `(13, 5, 2, 2, 2)` | 6 | 3672 | 2182 | 99.910% | no | 99.810% | no |
| `(11, 7, 4, 1, 1)` | 6 | 3209 | 2448 | 99.670% | no | 99.630% | no |
| `(15, 6, 5, 1, 1)` | 7 | 5368 | 3772 | 99.790% | no | 99.760% | no |
| `(13, 13, 2, 2, 2)` | 8 | 29372 | 25241 | 99.710% | no | 99.660% | no |
| `(17, 10, 2, 2, 1)` | 8 | 7572 | 5669 | 99.740% | no | 99.710% | no |
| `(24, 5, 3, 2, 2)` | 9 | 10918 | 6167 | 99.850% | no | 99.840% | no |
| `(14, 8, 3, 2, 1)` | 7 | 8987 | 6792 | 99.680% | no | 99.610% | no |
| `(8, 6, 6, 3, 1)` | 6 | 23592 | 22088 | 99.450% | no | 99.470% | no |
| `(19, 4, 4, 3, 2)` | 8 | 29093 | 18474 | 99.860% | no | 99.840% | no |

## Session 56's cells (delta 2-4, ell<=4; all mult_det = a)

| lambda | delta | n_chi | n_red | RED cover | RED cert | DET cover | DET cert |
|---|---|---|---|---|---|---|---|
| `(8,)` | 2 | 1 | 0 | 100.000% | yes | 100.000% | yes |
| `(6, 2)` | 2 | 2 | 0 | 100.000% | yes | 50.000% | no |
| `(4, 4)` | 2 | 3 | 1 | 100.000% | yes | 66.670% | no |
| `(12,)` | 3 | 1 | 0 | 100.000% | yes | 100.000% | yes |
| `(10, 2)` | 3 | 2 | 0 | 100.000% | yes | 50.000% | no |
| `(9, 3)` | 3 | 3 | 0 | 100.000% | yes | 66.670% | no |
| `(8, 4)` | 3 | 4 | 1 | 100.000% | yes | 75.000% | no |
| `(8, 2, 2)` | 3 | 8 | 1 | 100.000% | yes | 87.500% | no |
| `(7, 4, 1)` | 3 | 8 | 2 | 100.000% | yes | 87.500% | no |
| `(6, 6)` | 3 | 5 | 1 | 100.000% | yes | 80.000% | no |
| `(6, 4, 2)` | 3 | 15 | 5 | 100.000% | yes | 86.670% | no |
| `(4, 4, 4)` | 3 | 23 | 10 | 100.000% | yes | 95.650% | no |
| `(16,)` | 4 | 1 | 0 | 100.000% | yes | 100.000% | yes |
| `(14, 2)` | 4 | 2 | 0 | 100.000% | yes | 50.000% | no |
| `(13, 3)` | 4 | 3 | 0 | 100.000% | yes | 66.670% | no |
| `(12, 4)` | 4 | 5 | 1 | 100.000% | yes | 60.000% | no |
| `(12, 2, 2)` | 4 | 9 | 1 | 100.000% | yes | 88.890% | no |
| `(11, 4, 1)` | 4 | 10 | 2 | 100.000% | yes | 90.000% | no |
| `(11, 3, 2)` | 4 | 14 | 2 | 100.000% | yes | 92.860% | no |
| `(10, 6)` | 4 | 7 | 2 | 100.000% | yes | 71.430% | no |
| `(10, 5, 1)` | 4 | 13 | 4 | 100.000% | yes | 92.310% | no |
| `(10, 4, 2)` | 4 | 22 | 6 | 100.000% | yes | 86.360% | no |
| `(10, 2, 2, 2)` | 4 | 55 | 12 | 100.000% | yes | 98.180% | no |
| `(9, 6, 1)` | 4 | 16 | 6 | 100.000% | yes | 87.500% | no |
| `(9, 5, 2)` | 4 | 27 | 10 | 100.000% | yes | 88.890% | no |
| `(9, 4, 3)` | 4 | 35 | 13 | 100.000% | yes | 91.430% | no |
| `(9, 4, 2, 1)` | 4 | 63 | 23 | 100.000% | yes | 98.410% | no |
| `(8, 8)` | 4 | 8 | 3 | 100.000% | yes | 75.000% | no |
| `(8, 6, 2)` | 4 | 33 | 15 | 100.000% | yes | 84.850% | no |
| `(8, 5, 2, 1)` | 4 | 80 | 38 | 100.000% | yes | 97.500% | no |
| `(8, 4, 4)` | 4 | 51 | 24 | 95.830% | no | 90.200% | no |
| `(8, 4, 2, 2)` | 4 | 136 | 64 | 100.000% | yes | 97.790% | no |
| `(7, 7, 1, 1)` | 4 | 47 | 23 | 100.000% | yes | 97.870% | no |
| `(7, 6, 3)` | 4 | 49 | 25 | 100.000% | yes | 89.800% | no |
| `(7, 5, 3, 1)` | 4 | 127 | 74 | 100.000% | yes | 97.640% | no |
| `(7, 4, 4, 1)` | 4 | 145 | 85 | 98.820% | no | 97.240% | no |
| `(6, 6, 4)` | 4 | 66 | 38 | 92.110% | no | 90.910% | no |
| `(6, 6, 2, 2)` | 4 | 180 | 111 | 100.000% | yes | 98.330% | no |
| `(6, 4, 4, 2)` | 4 | 288 | 199 | 98.490% | no | 98.610% | no |
| `(4, 4, 4, 4)` | 4 | 465 | 380 | 99.740% | no | 99.780% | no |
