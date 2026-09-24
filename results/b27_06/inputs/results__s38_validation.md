# s38 validation battery (P1) — result: PASS

All run on this container, 2026-09-02, before any new cell was banked. Kill
criterion "validation failure → stop" did **not** fire.

## Core pipeline / corrected raising rule

- **K1 witness gate** (`wk9_s33_rungs.py gate`): binary quartics, closure`{l^3 m}`,
  `lam=(4,4)`, `delta=2` ⇒ `a=1`, `mult=0`, kernel `(12,−3,1)` at both primes
  (P1: `(12, 2147483644, 1)`, P2: `(12, 2147483626, 1)` — i.e. `(12,−3,1)`).
  The wrong (uncorrected) rule would give `(1,−4,3)`; it does not. ✓

## Rectangular ladder — `D_4^det`, `lam = (delta^4)` (independent reduction, s33)

Reproduced from the plethysm `a` and the sign^δ-isotypic S_4 reduction; every
row asserts `rank(R) = n_chi − a`, two primes, and (odd δ) exact cancellation of
the swap-fixed target rows — the **odd-block sign test**.

| rung δ | a (plethysm) | n_chi | mult_det | odd-block test |
|---|---|---|---|---|
| 4 | 1 | 43    | 1 | — (reduced == unreduced, same kernel vector, V2) |
| 5 | 0 | 95    | — | **cancels exactly (V4)** |
| 6 | 1 | 661   | 1 | — (decides e ≠ 6) |
| 7 | 1 | 2310  | 1 | **cancels exactly** |
| 8 | 3 | 10738 | 3 | — (compressed route; matches banked) |

All match `docs/n4_gate.md` §5 and `results/e4_ledger.md`. ✓

## Length-5 unreduced pipeline — the target regime (`validate6`)

The nine banked `delta=6`, `ell=5` cells of `docs/n4_gate.md` §6, by the
unreduced `measure(det_4, 16, 4, 5, 6, lam)` used for all Phase-1 δ=8 work.
Every one returns `mult_det = a`, `a` matches the plethysm, and `N_S` matches
the banked value:

| lam | a | mult_det | N_S |
|---|---|---|---|
| (14,5,2,2,1) | 2 | 2 | 1337 |
| (13,5,4,1,1) | 2 | 2 | 1824 |
| (12,7,3,1,1) | 3 | 3 | 1884 |
| (13,6,2,2,1) | 3 | 3 | 1910 |
| (11,8,3,1,1) | 2 | 2 | 2224 |
| (14,4,2,2,2) | 2 | 2 | 2337 |
| (12,7,2,2,1) | 3 | 3 | 2467 |
| (12,6,4,1,1) | 2 | 2 | 2553 |
| (12,5,5,1,1) | 2 | 2 | 2795 |

VALIDATE6 PASS. ✓

## Independent cross-checks on the Phase-0 counts

- `a(lam,δ,d=4,nv=5) == a(lam,δ,d=4,nv=16)` (variable-count independence) and
  `a == dim ker(R)` (the definition) asserted on the reachable δ=8 cells
  (`--checkdef`).
- Batched `m_det` == `ambient_screen.m_det` on ≥6 cells per δ (`mdet-xcheck`).
- `scripts/ambient_screen.py --selftest` passes (n=3 record: plethysm strata,
  `m_det` sums/supports 3/11/43 and 3/10/34, the δ=5 live weight `(9,4,2)`).
- Capped `N_S` counter == `len(monomials(...))` on 87 cells, and reproduces the
  `n4_gate` §6 sizes (1337, 2224, 2795).
