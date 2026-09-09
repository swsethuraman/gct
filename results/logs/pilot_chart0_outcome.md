# Bounded pilot — S2 chart_0 job (session 78)

- Job: `results/astra/S2/cas/chart_0_Q.sing`, S2's exact Job-A recipe, verbatim.
- Ring: 149 variables (`u`, `x1..x79`, `y1..y69`), lex `u > x > y`.
- Bounds: `timeout --signal=TERM 600` (10 min wall), `ulimit -v 6200000` (~6.2 GB).
- Launcher: `results/logs/run_pilot_chart0.sh`; pid recorded in `results/logs/pilot_chart0.pid`.
- Ended: by the wall-clock bound (`timeout` sent TERM at 600s; Singular printed `halt 1`).
- Output: **none**. The first `std(raw)` of the 149-variable ideal did not
  complete inside the bound, so no `chart_0_graph.txt`, `_image_full.txt`, or
  `_image_Q.txt` was written. Peak resident memory during the run reached ~4.4 GB
  (under the 6.2 GB cap), so this is a **time** wall, not a memory wall, at 600s.

## Exact preserved residual

No Gröbner step completed, so there is no partial standard basis to preserve.
The exact residual ideal is therefore the **input ideal itself**, committed and
reproducible in the tree:

    raw = ( 1 - u*f0,  f_alpha - y_alpha*f0 : alpha = 1..69 )   in Q[u, x1..x79, y1..y69]

with the 70 generators `f0..f69` written out in `chart_0_Q.sing` (all 15,000
determinant monomials). This is the reference specification; the session did not
obtain a partial elimination basis from it within the bound.

## Consequence

Per the pre-registration (F3), the unconditional 149-variable Job A does not
finish in-container. The session proceeds on (a) the certified **A5=I
reduction** of Job A (149 -> 98 variables, no f0 saturation) and its bounded
runs, and (b) the S2 section-C strata where exact structural certificates are
attainable. A timeout is explicitly **not** a reversal certificate (`I_h = 0`
must be certified exactly), and none is claimed.
