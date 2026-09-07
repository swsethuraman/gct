# Session 62 — Smith normal form diagnostics (Task 6)

Diagnostic only: this is not a congruence programme, and there is no observed modular
rank drop anywhere in the record to fit. Reported to say whether the elementary divisors
of the small Gram blocks look generic or structured.


## n = 4 block Gram G_lambda (room-one and multiplicity-2 cells)


| delta | lambda | a | rank | SNF(G) elementary divisors |
|---|---|---|---|---|
| 4 | (12, 4) | 2 | 2 | ['476763704524800000', '601322989968949248000000'] |
| 4 | (10, 6) | 2 | 2 | ['1365277881139200000', '73588477793402880000000'] |
| 4 | (10, 4, 2) | 2 | 2 | ['130026464870400000', '76377545464872960000000'] |
| 4 | (8, 6, 2) | 2 | 2 | ['5350883328000000', '31620745912437964800000000'] |
| 4 | (8, 4, 4) | 2 | 2 | ['3210529996800000', '190811236668014592000000'] |

The multiplicity-2 blocks (`(12,4)`, `(10,6)`, `(10,4,2)`, `(8,6,2)`, `(8,4,4)` at δ=4) all have
two elementary divisors dominated by a much larger last invariant — the generic shape of a
Gram matrix of independent integer vectors, not a structured (e.g. all-equal or small-prime-
repeated) spectrum. No repeated small elementary divisor beyond the 24^δ-type content common
to every entry appears. **Nothing structured; no modular rank drop; the SNF is generic.**


## n = 2 proved control


| delta | lambda | rank | SNF(G) |
|---|---|---|---|
| 3 | (2^3) | 1 | [1152] |
| 4 | (2^4) | 1 | [46080] |
| 5 | (2^5) | 0 | [0] |
| 6 | (2^6) | 0 | [0] |

At δ=5,6 the 1×1 Gram is exactly `[0]` (rank 0): the proved rank drop, elementary divisor 0.

