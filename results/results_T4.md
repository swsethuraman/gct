# Session 14: the rigidity determination (T4 + cross-scheme runs)

Date 2026-08-28. Engine dp2g evalopts (checkpointed), exact int64; every
value below landed AFTER its outcome map was committed (pre-registration
commits 8e9f51e and 7af9d09).

## Engine record (all final states 1)

| run      | point | scheme | sigma | VALUE        | role |
|----------|-------|--------|-------|--------------|------|
| f1T4_00  | T4    | 1      | 00    | +108,712,800 | ratio_id = 1 |
| f1T4_35  | T4    | 1      | 35    | +108,712,800 | GATE = 00 (pre-rho AND post-omega partner): PASSED |
| f1T4_05  | T4    | 1      | 05    | −476,884,800 | ratio_(02) = 1: uniformity |
| f2C_00   | C     | 2      | 00    |  +78,850,800 | kappa_2 = 1043/1438 |
| f3C_00   | C     | 3      | 00    |  +17,388,000 | kappa_3 = 115/719 |
| f2T4_00  | T4    | 2      | 00    |  +78,850,800 | LS1 prediction HIT exactly |
| f3T4_00  | T4    | 3      | 00    |  +17,388,000 | LS1 prediction HIT exactly |

T4 = {x3+=x0, x4+=x1, x7+=x1, x8+=x2}, pencil (diag(1,1,0), diag(0,1,1)) —
a third pencil class (contains invertible elements; not H-conjugate to C's
cyclic or R's diagonal-units class). Point symmetry pi = (0 2)(3 8)(4 7)(5 6)
sign +1, rho = (0 2); extended orbits (with the scheme automorphisms):
8 orbits, sizes (2,8,8,2,4,4,4,4). SAT screen: live at point and all run
sigmas. Input integrity: f1T4 verified distinct from f1R at file level and
canonically identical to an independent regeneration.

## VERDICT

1. **Scheme-1 line measured: Psi ∝ 2v − D** (v = u1 − 2u2, D the pencil
   discriminant; normalization Psi(C-pencil) = 1). Selected by the
   pre-registered O3 map at rho = 1; uniform across both tested W-classes.
2. **Strong rigidity (rank 1) across the ambient multiplicity space:**
   schemes 2 and 3 evaluate through the SAME line — cross-point ratios
   V^h(T4)/V^h(C) = 1 = Psi(T4)/Psi(C), both exact. Every functional
   V^h_sigma(N) = W^h(sigma) · Psi(N) on balanced pencils.
3. **Integrality theorem: the three ambient HWVs are pairwise-independent
   functionals** (kappa_2·W((0 2)) = −248695423200/719 ∉ Z, and 719 ∤
   115·476884800 — sigma-table proportionality is impossible). The amb = 3
   basis is honest; the compression to one covariant is a property of the
   balanced-pencil restriction, not of a degenerate basis.
4. Everything banked is explained by Psi = 2v − D: Psi(C) = Psi(R) =
   Psi(T4) = 1 (universality of totals and tables across three pencil
   classes), Psi ≡ 0 on rank-1 pencils (P's exact zeros — doubly derived),
   and TOTAL_G = Psi(G)·TC = 1,152,144,000 (standing implied prediction,
   still deliberately un-run).
5. Standing falsifiers (cheap, any time): coefficient-2 pencil must scale
   all values by 4; any new balanced point N must give
   TOTAL(N) = (2v−D)(N) · 1,152,144,000.

Prediction ledger: gate 00=35 HIT; T4-05 = −476,884,800 HIT; f2T4_00 =
+78,850,800 HIT; f3T4_00 = +17,388,000 HIT — every pre-registered
prediction of the session landed exactly; the one open map entry (rho)
selected O3 = 1 from within the pre-written inversion formula.

The theorem left to prove (math, no engine): the composite
Sym⁴W → (3-dim ambient)* has rank 1 on the balanced cone with image
span{2v − D} — all measured structure is now an exact target.
