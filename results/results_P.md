# Point P = (x3+=x0, x6+=x0): exact vanishing (session 12, 2026-08-25)

Factored scheme-1 evaluation of the k=1 HWV (lambda' = (8,8,8,6^6), delta=20)
at the rank-1 double-transvection point P. Grind stopped after 4 runs — all
exactly zero. Engine: dp2g (evalopts, checkpointed), regression-validated
same day including a complete f1C_00 reproduction (+108,712,800).

## Completed runs

| sub | assignment (s6,s7) | orbit | VALUE | final states | runtime |
|-----|--------------------|-------|-------|--------------|---------|
| 00  | (id, id)           | 0     | 0     | 0            | 103 min |
| 07  | ((0 2 1),(0 2 1))  | 0     | 0     | 0            | 101 min |
| 01  | (id, (0 2 1))      | 1     | 0     | 0            |  96 min |
| 02  | (id, (1 0 2))      | 2     | 0     | 0            | 101 min |

Pair gate 00 = 07: MATCH (at zero) — pre-rho relation empirically validated
at P. Orbits 0, 1, 2 = 16 of 36 subproblems dead.

## The signature: exact terminal cancellation, not structural absence

Every run dies the same way (sub 07 shown):

    level 18: states 124     emitted 5702  sum|w| 2624166720
    level 19: states 0       emitted 56    sum|w| 0
    level 20: states 0       emitted 0     sum|w| 0

L18 still carries billions-scale weights across 100+ states; the closure of
short column 7 (copy 19 = (3,5,7)) cancels every accumulated state weight to
exactly 0 (the engine drops zero-weight states, hence "final states 0").
The SAT screen (analysis/wk3_s12_satfeas.py; validated: C assignments
SAT-live and engine-nonzero) shows completing paths EXIST at every checked
P-assignment — the zero is algebraic cancellation, not combinatorial
infeasibility. The content-DFS feasibility (wk3_s8_feas) is therefore
doubly insufficient: it misses wedge structure, and no path-existence
screen can see cancellation.

## Mechanism conjecture (open)

P is RANK-1: u = I + (e_30 + e_60), both transvections sourcing x0.
Content forces every completing path to use exactly 4 substituted legs, so
h1(u_t . det3) = t^4 * TOTAL_P — a pure 4th directional derivative of h1
along a rank-1 direction. Conjecture: this vanishes identically for all
three rank-1 (column-uniform) points of the balanced sweep — (x3+=x0,x6+=x0),
(x4+=x1,x7+=x1), (x5+=x2,x8+=x2) — and rank >= 2 is necessary for a
nonvanishing certificate point. No (pi, theta)-symmetry can force these
zeros (their value-relation signs are point-independent, and the same
scheme's values at C are nonzero); the mechanism is new. Candidate proof
route: a sign-reversing pairing on the choices of which 4 columns receive
the substituted x0-legs.

## Status

Remaining P-orbits unrun (03/04 checkpoints preserved in gct-run/p1,p2).
Certificate grind relaunched at the rank-2 point Q = (x4+=x0, x6+=x1) —
see PROJECT_NOTES session-12 and results_Q.md when it lands.
