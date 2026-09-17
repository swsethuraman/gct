# Corrigendum notes (direct arc-relation follow-up, 17 September 2026)

Both parent packets (`routeA_signfilter_20260917/`, `arc_target_dimension_followup/`) are preserved
byte-for-byte (re-hashed at session start and at sealing, 0 mismatches). No statement of either parent
is found false. Two clarifications and one self-correction are recorded.

## C1. Parent (arc_target) §6.4 and §7.3 — price and status of the "smallest next step"

The parent priced `dim F''` as the decisive next computation. This session shows a cheaper and more
structural route exists for the specific subspace `U = span(q_3, q_7, n02)`: every same-pairing paired
contraction factors through two-column covariants (REPORT.md §B.2, PROVED and verified exactly against
the sealed values), which reduces the forbidden components of `U` to pairings of restricted covariants.
The parent's price estimate is not wrong; it is no longer the only route. Proposition 7.1 of the parent
(conditional on `rank C|_U = 2`) is unchanged and still the bridge to the existence result.

## C2. Parent (routeA) §5.3 — the sampled candidate

Unchanged: the residues `265391, 275398` remain modular; no rational lift is supplied here either.
New, exact, and consistent with the parent: the skew-degree-12 rows of `q_3, q_7, n02` are proportional
at all five recorded points with constant ratios (`q_7 : q_3 = 101007`, `n02 : q_3 = 295818` mod `P`),
i.e. the degree-12 part of the sampled forbidden matrix has rank 1, not 2; the recorded rank 2 comes
entirely from the degree-11 rows.

## C3. Self-correction — this session's pre-registered mechanism (REPORT.md §B.2, written before pilots 2–3)

The plan proposed `m = dim Cov = 2` and `N_top = 1` as the route to "proportional top parts". Pilot 1 gives
`m = 4`, `N_top = 26` (and `18` through `S_{22}`); pilot 2 shows no isotypic component of
`ν_1∧ν_2∧ν_3∧Z_1∧Z_2` vanishes; pilot 3 shows the tops of the three covariants that actually carry
`q_3, q_7, n02` have exact rank 3 on the transversal slice. **The proportional-tops mechanism is refuted.**
The factorization itself, the reduction of tops to the locus `S*`, the transversal-slice certification
method and the exact structure `q_3 = 2B(Φ_1,Φ_2)`, `q_7 = 2B(Φ_3,Φ_2)`, `n02 = 2B(Φ_1,Φ_1)` (exact at
the general point) stand and are the new starting point.
