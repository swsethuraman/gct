# Session 34 — entry calibration, banked before the sweep

Order and pass criteria pre-registered (`results/PREREG_s34.md` §1).  All run
in this container after the census was committed and before any `delta = 7`
cell was measured.

## 1. The witness (kill criterion) — PASS

Binary quartics, `closure{l^3 m}`, `lam = (4,4)`, `delta = 2`:
`mult = 0` and kernel `(12, −3, 1)` on `(c40 c04, c31 c13, c22^2)` — exactly
the corrected-rule kernel (the wrong rule gives `mult = 1`, kernel
`(1, −4, 3)`).  Guards against a stale clone; the rule on `main` is correct as
of `7d93449` and this clone's tip is `29bea5f`.

## 2. `analysis/wk8_s30_calib.py`, run as-is — all five parts PASS

    PASS witness {l^3 m} lam=(4,4) delta=2 : mult = 0
    PASS witness kernel == (12,-3,1)
    PASS discriminating battery: 48 World A cells, 41 with mult < a
    PASS session 26's five cells
    PASS mult_det = a at all 20 weights, n=3, delta<=4

The battery is quoted as its **discriminating ratio: 41 of 48** — the 41 cells
where `mult < a`, i.e. the parts the wrong rule could have failed — never the
bare pass count (a battery is evidence only through the parts that could have
failed; s30 review §1).

## 3. Three of s30's banked cells, re-certified — all EXACT (P1 confirmed)

Deterministic rule (pre-registered §1.3): `SHA-256("s34-recert-2026-09-01")
mod 34`, step 11 → ledger rows **13, 24, 1**.  Code path: `wk8_s30_core.measure`,
`a_expect` from the plethysm, det seed 11 / pad seed 29, `npts = a+8` — the
exact `wk8_s30_run62c.py` call pattern, at `delta = 6`.

| ledger row | lam | ell | a | N_S | mult_det | mult_pad | D | verdict | secs |
|---|---|---|---|---|---|---|---|---|---|
| 13 | (13, 4, 4, 2, 1) | 5 | 2 | 3199 | 2 | 2 | +0 | EXACT | 198 |
| 24 | (9, 8, 5, 1, 1)  | 5 | 2 | 5159 | 2 | 2 | +0 | EXACT | 725 |
| 1  | (13, 5, 4, 1, 1) | 5 | 2 | 1824 | 2 | 2 | +0 | EXACT | 39 |

Every field of every row reproduces `results/sweep62_ledger.md` exactly.
Kill criterion 3 does not fire; the pipeline is the one s30 ran.
Raw log: `results/s34_recert.log`.

**Environment note:** `python-flint` 0.9.0 (s30's version), primes
2147483647 / 2147483629, 2 cores, MemAvailable 7.6 GB at start.
