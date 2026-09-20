# B23-10 pilot 3 — pre-registration (written before launch; its sha256 is a required argument of the pilot)

Session 2 of slot B23-10, 2026-09-19. Pilots 1 and 2 of this slot ran at 01:53Z and 01:57Z (receipts
under `results/logs/b23_10_p{1,2}_*`). This is the third and last permitted launch.

**A. B23-03 Theorem 3.2, determinant side, `k = 6..8` (`N = 8`: `k = 6, 7`).** At a fresh random
integer point of `D_N` (the determinant of a `4 x 4` matrix of integer linear forms in `N` variables,
computed exactly over `Z`), `rank M_k` modulo `p = 2^31 - 1`. A modular rank at an integer point is a
floor on the generic rank of `D_N`. Code written here; B23-03's scripts were not read.
Prediction: equal to B23-03's shipped floors (N = 6: 321 / 660 / 1146; N = 7: 567 / 1279 / 2435;
N = 8: 932 / 2248). A value above a shipped floor would only improve it; a value below would mean my
point is special or the shipped value is wrong, and would be reported as a discrepancy, not a refutation.
The margins are then my floors minus the padding ceilings replayed in pilot 1
(N = 6: 287 / 532 / 918; N = 7: 518 / 1050 / 1968; N = 8: 876 / 1926). Predicted margins:
+34 / +128 / +228; +49 / +229 / +467; +56 / +322.

**B. B23-03 Proposition 2.5, floor.** Exact rank over `Q` (fmpz) of `M_4` at a fresh random integer cubic
`x_1 q_1 + x_2 q_2` through the plane `x_1 = x_2 = 0`: predicted **64**. At a fresh random integer cubic:
predicted **65**. (Pilot 1 found 58 at B23-03's witness, which is a special member; B23-03 does not
claim 64 there.)

Stop rule: the pilot skips any stage not started by 45 s elapsed and records the skip.
