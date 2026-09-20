# B24-02 pilot 1 — pre-registration snapshot

Written and hashed **before** `analysis/b24_02_p1_n5_kleiman.py` was run. Its sha256 is printed
into `results/b24_02/p1_n5_kleiman.json` as the file's first field (G25).

## Question

Row 1 of B22-02 (rank thresholds of `d_1`) is a PROVED-kill at `N = 6, 7, 8` for every `k` on
elementary premises (B23-03 Thm 3.2, replayed by B23-10 §3.2). At `N = 5` it rests on GKZ
Theorem B, which for `k >= 7` adopts Kleiman (GKZ corrigendum C2: "Kleiman remains the only
adopted input for `k >= 7`").

**Can B23-03's own method — elementary padding ceiling + certified determinant floor at explicit
integer points + a Newton certificate for the tail — discharge Kleiman at `N = 5`?**

All dimensions below are **affine** dimensions of graded pieces of `S = C[x_1..x_5]` (G24); no
projective dimension is used anywhere in this pilot.

## Pre-registered quantities

`S_k` = degree-`k` forms in `N = 5` variables, `dim S_k = C(k+4, 4)`.
`M_k(F)` = the Macaulay matrix of the Jacobian ideal `J_F = (dF/dx_1, ..., dF/dx_5)` in degree
`k`: rows indexed by degree-`k` monomials, columns by (partial `i`, degree-`(k-3)` monomial).
`rank M_k(F) = dim (J_F)_k`.

1. **Padding ceiling (elementary, exact).** Every padding point is a product `l P` (`l` linear,
   `P` cubic), so `J_{lP} ⊆ (l, P)` and
   `rank M_k(lP) <= dim S_k − h_5(k)`, `h_5(k) = C(k+3,3) − C(k,3) = (3k² + 3k + 2)/2`.
   Universal ceilings for every quartic: `5·dim S_{k−3}` at `k = 3, 4, 5` (the generator count)
   and `5·dim S_3 − C(5,2) = 165` at `k = 6` (Koszul relations). Ceiling = the minimum.
2. **Determinant floor at a random integer point, `k = 3..9`.** `F = det` of a random `4 × 4`
   matrix of integer linear forms in five variables, computed exactly over `Z`; then
   `rank M_k(F) mod P`, `P = 2^31 − 1`. A modular rank at an integer point is a **floor** on the
   generic rank over `D45` (lower semicontinuity, twice).
3. **The tail point.** `F_0 = x_1x_2x_3x_4 − x_5^4`, asserted to be the determinant of
   `[[x1,0,0,x5],[x5,x2,0,0],[0,x5,x3,0],[0,0,x5,x4]]` (verified symbolically in the pilot), so
   `F_0 ∈ D45`. Its Jacobian ideal `(x2x3x4, x1x3x4, x1x2x4, x1x2x3, x5^3)` is monomial, so its
   Hilbert function is **exact** for every `k`: `H(k) = Σ_a A(a)·B(k−a)` with `A(0) = 1`,
   `A(a) = 6a − 2` for `a >= 1`, and `B(j) = 1` for `j = 0,1,2`, else `0`. Hence
   `H(k) = 18k − 24` for `k >= 3`.
4. **Newton certificate.** `D(k) = h_5(k) − H(k) = (3k² − 33k + 50)/2` for `k >= 3`. Expanded as
   `D(k) = Σ_i e_i·C(k − k_1, i)` at `k_1 = 10`; every `e_i >= 0` with `e_0 > 0` proves
   `D(k) >= e_0 > 0` for every `k >= k_1`.

## Pre-registered predictions (recorded before the run)

- `h_5(k)` at `k = 3..9`: `19, 31, 46, 64, 85, 109, 136`.
- Padding ceilings at `k = 3..9`: `5, 25, 75, 146, 245, 386, 579`.
- `A(a) = 6a − 2` for `a >= 1` reproduced by brute-force enumeration for `a = 0..12`.
- `H(k) = 18k − 24` for `k = 3..12` reproduced by brute-force enumeration.
- `D(k) < 0` at `k = 7, 8, 9` (`−17, −11, −2`): **the `F_0` point does not separate there**, which
  is exactly why the random-point floors at `k = 7, 8, 9` are needed.
- Newton coefficients at `k_1 = 10`: `e = 10, 15, 3, 0, 0, ...`.
- `k = 3, 4, 5`: determinant floor **equals** the universal ceiling (margin `0`, a tie; padding
  cannot exceed the determinant and no equation separates).
- `k = 6, 7, 8, 9`: determinant floor **strictly exceeds** the padding ceiling.

## Decision rule, fixed in advance

**PASS** (row 1 unconditional at `N = 5`, Kleiman discharged) iff all three hold:
- (a) margins at `k = 3, 4, 5` are `>= 0`;
- (b) margins at `k = 6, 7, 8, 9` are `> 0`;
- (c) the Newton certificate at `k_1 = 10` has all `e_i >= 0` and `e_0 > 0`.

**FAIL** otherwise. On FAIL the slot stops and prices the gap; it does not spend a second pilot
(the brief's instruction).

## Seed and modulus

`SEED = 20260919`, `P = 2147483647`. Entries of the random linear forms drawn uniformly from
`[−5, 5]`. One prime only: a floor is all that is claimed, and a second prime cannot raise it.

## What a PASS would and would not establish

It would remove Kleiman from row 1 at `N = 5`, making row 1 a PROVED-kill on elementary premises
across the whole window `N = 5..8`. It would say nothing about row 2 (`d_j`, `j >= 2`), nothing
about `D45 ∩ P5`, and nothing about any other adopted use of Kleiman elsewhere in the record.
