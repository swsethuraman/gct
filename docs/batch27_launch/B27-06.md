# B27-06 — price a measurement of `mult_det` at the largest-`a` degree-8 cell (Astra producer, overnight pricing slot)

Read `B27_COMMON.md` first. **This brief overrides it in the same four places as B27-05:**

1. **No Git writes at all.** Read-only `git show` is allowed.
2. **Output folder.** Write every output, including scripts named `b27_06_*.py`, only to
   `C:/Users/swami/Projects/gct-gpt/Claude_Handover_B15_B18/post_b19_housekeeping_20260917/batch27_launch/b27_06_out/`.
   Stop if that folder already exists.
3. **Preflight.** Record the raw SHA-256 of `B27_COMMON.md`, of this file and of
   `BATCH27_BOARD.md`.
4. **Delivery.** Finish with `MANIFEST.json` in the folder, binding every payload's raw SHA-256
   and bytes and excluding itself.

| item | value |
|---|---|
| Session | a **fresh Astra session**, not the B27-05 session, in default permission mode |
| Ceiling | 90 min, with a checkpoint at 45 |
| Compute | the B27 allowance: exact only, ≤10 runs, each ≤60 s and ≤512 MB, no installs |

## Why this slot exists

B27-05 is a READ-level feasibility result: its folder is verified and its manifest hash is
`325c1c81…`. It found that session 60 measured `mult_det = a` at all 419 of its cells, including
95 at degree 8 and 94 at degree 9 in the balanced complement. It also found two cells with **no
recorded rank measurement** in the sources it checked:

| cell | a | m_det | N_S |
|---|---|---|---|
| `(12,8,6,4,2)` at k=8 | 109 | 27,257 | 813,314 |
| `(14,10,6,4,2)` at k=9 | 437 | 104,544 | 2,085,864 |

These are the largest-`a` cells in session 38's table, so they are the most plausible places for a
first `mult_det < a` at degree 8 or 9.

Measuring them is **not** possible inside the B27 allowance. For comparison, session 36's recorded
dense frontier was about 15,500 reduced columns. This slot therefore produces the **priced
preregistration** that `B27_COMMON.md` requires before any larger computation. **Do not attempt
the measurement.**

All citations are at commit `7c36a52d` unless you find a later one. B27-05's `REPORT.md`, in the
folder above, lists the relevant sections of sessions 36, 54, 56, 58, 60 and 62 and of B14-11. It
is a producer-level READ, so re-read the committed sources and do not rely on its summary.

## Ladder

**0 — Record check (READ).** Search the whole committed record for any rank measurement at either
cell. That includes session 60's closing sweeps and anything after session 62. If you find a
measurement, stop and report it.

**1 — Method and certificate inventory (READ, then HAND).** For each recorded method that could
measure `mult_det` at these cells, state:
- what it computes;
- what certifies **full rank** (`mult_det = a`, so no equation in that cell);
- what would certify a **drop** (`mult_det < a`, so an equation exists) over characteristic zero.

The methods are at least: the reduced nullspace of sessions 36 and 38; session 60's sparse or
dense route; and session 62's `a × a` Gram matrix with orbital assembly.

State plainly the asymmetry. Modular full rank certifies full rank. A modular deficiency is
**not** a characteristic-zero certificate of a drop. Say exactly what extra step a drop would need.

**2 — Price (checkpoint at 45 min).** For each method, estimate wall time and peak memory at both
cells:
- Base the estimate on recorded timings. You may also use up to 10 allowance runs that **replay
  already recorded smaller cells**, to fit a scaling law. These are verification runs; state which
  cells and why.
- Give the fit, its uncertainty, and the hardware assumption.
- Name the cheapest method that is realistic, and what it would need: machine size, days, and
  whether it is exact or modular.

## Registered outcomes

1. A measurement already exists in the record (cite it).
2. A priced preregistration: named method, certificate type in each direction, cost with
   uncertainty, for the user to approve or decline.
3. Priced out for every recorded method, with the bottleneck named.
4. Obstruction: the inventory or scaling cannot be established from the record, stated precisely.

**Prior, for calibration only.** 419 of 419 measured cells have `mult_det = a`. A measurement at
these cells is more likely to add a no-equation cell than to find a drop. A drop would be
existence of an equation only, never separation on padding.

The binding constraint stands: "No five-row determinant equation is known to be nonzero on
padding." Integrator method suggestions are 0 for 4, so the producer owns the method.
