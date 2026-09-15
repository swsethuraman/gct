# Batch17 prerequisite screens

13 September 2026. Both requested production screens completed under a 60-second / 512-MiB Windows Job Object cap, one process and one BLAS thread. No orbit evaluation matrices, Git changes, or worker dispatches were needed.

## Six nearby finite cells

Weights are (4d-t-16,t,2^8). All numbers are in the same finite cell. Complete determinant ideal dimensions and padding ceilings are inherited from accepted Batch16; ambient corrections are fresh.

| d | t | Stable ambient | Finite correction | Finite ambient a | Exact determinant ideal q | Determinant coordinate multiplicity a-q | Padding ceiling U | Gap upper q+U-a |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|
|23|17|294|-2|292|2|290|218|-72|
|24|17|294|-1|293|3|290|218|-72|
|23|19|429|-10|419|4|415|288|-127|
|24|19|429|-5|424|7|417|288|-129|
|25|19|429|-2|427|9|418|288|-130|
|26|19|429|-1|428|10|418|288|-130|

All six cells are excluded for positive multiplicity gaps. This is not a conclusion inferred from tableau-count monotonicity. The finite corrections were explicitly computed.

Method: use the exact GL1 branching identity in B16-02. For tail tau of size w, let G_(b,m) be the character with b generators and weight m in Sym(Sym2+Sym3+Sym4). For L=w-m and D=d-b, the truncated first-row Weyl sum is zero if 0<L<=D, is one for L=0, and is (-1)^(L-D) s_(D+1,1^(L-D-1)) if L>D>=0. All six d satisfy d>=floor(w/2), so no b>d case occurs. Add these finite terms to the accepted stable count. Pair G_(b,m) with the skew Schur function tau/hook; hooks not contained in tau contribute zero.

The producer evaluates skew Schur functions by exact Jacobi-Trudi determinant expansion and rational power sums. It passes 85 small comparisons against direct quartic plethysm, including outside-stability cells. The second route evaluates the same pairings using skew Murnaghan-Nakayama with geometrically enumerated border strips. All 57 retained correction carriers match. The second route shares the branching identity and G expansion; this is not a wholly independent theorem proof.

Production runtime: 3.684 seconds; peak Job Object committed memory 19,562,496 bytes. Machine-readable records: finite_screen.json.

## Degree-seven symmetry slice

Scope: det4 versus independent z*per3; lambda=(28-|nu|,nu), |nu|<=10, 2<=length(nu)<=6, and ambient multiplicity at least two.

114 shapes considered; 31 have ambient multiplicity at least two. Compute finite ambient a, support-corrected cubic source U, connected rectangular coefficient g, transpose trace t, and symmetric coefficient s=(g+t)/2. Set B=min(a,s). No shape satisfies 1<=B<U.

This retires this particular symmetry-only proposal. It does NOT prove absence of actual multiplicity gaps in the slice, because determinant boundary losses may make its true coordinate multiplicity smaller than B. It does not screen the rest of degree seven.

Production runtime: 12.000 seconds; peak Job Object committed memory 43,958,272 bytes. Machine-readable records: degree7_screen.json. Character controls include S6 orthogonality and a signed transpose example. The second geometric-border-strip route passed all 31 eligible rows, recomputing ambient, connected, transpose and padding-source values; see verification.json. It also passed all 57 finite correction carriers. Combined verification runtime was 12.997 seconds under the same 60-second / 512-MiB cap.

## Consequence for planning

No padding rank hunt is justified by either screen. Do not expand the short-body character search automatically. Retain the existing global determinant equations as structural inputs, but seek a new closure-sensitive bound or a new representation family before allocating heavy evaluation work. Batches15/16 stay closed. Batch17 is a staged research board, not launched.
