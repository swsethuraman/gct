# PREREG — B25-04 pilot 1 (`b25_04_p1_factor`)

Written before the pilot script exists. UNCOMMITTED. Governs the only pilot this slot plans.

## Purpose

A control on the **reading** of BDI eq. (5.2) that the theory gate (`THEORY_GATE.md`) uses, and an
exact witness of nonvanishing. It is **not** the proof of the Component Lemma, which is by hand.

## Object

`f_T̂(p)` computed literally from BDI eq. (5.2), generalised to a weighted Waring decomposition
`p = Σ_i c_i ℓ_i^n` (`c_i` integers, `ℓ_i ∈ Z^r`):
`f_T̂(p) = Σ_{φ:[d]→[R]} Π_{a∈[d]} c_{φ(a)} · Π_{columns c} det(top ν_c × ν_c block of [ℓ_{φ(a)}]_{a ∈ c})`.
Exact Python integers only. Project variables: form degree `n = 5`, `r = 3`, `d ≤ 5`, `R ≤ 4`.

## Claims tested (fixed now; nothing added after results)

- **K1 (nonvanishing, proof direction).** `g := f_{T̂_g}`, `T̂_g` the unique semistandard tableau of
  shape `(8,2)`, content `2 × 5` (row 1 `1 1 1 1 1 2 2 2`, row 2 `2 2`), has a nonzero value at a
  seeded integer point. A nonzero exact value **proves** `g ≠ 0` (given the implementation).
- **K2 (Component Lemma consistency).** For `T̂` with columns
  `(1,2,3),(1,2),(4,5),(4,5)` plus 16 singleton columns so that each entry occurs 5 times
  (`d = 5`, column lengths `3,2,2,2,1^16`, so `λ = (20,4,1)`; asserted in code),
  `f_T̂(p) = f_{T̂_{123}}(p)·f_{T̂_{45}}(p)` at 5 seeded points. Also the isolated-vertex case:
  `T̂_g` plus entry 3 in five singleton columns (`d = 3`, `λ = (13,2)`) equals
  `g(p) · c_{5e_1}(p)`, `c_{5e_1}(p) = Σ_i c_i (ℓ_i)_1^5`, at 5 points.
- **K3 (HWV reading).** `g(L·p) = g(p)` for 3 seeded lower-unitriangular integer `L` acting on the
  `ℓ_i` (top-minor invariance), and `g(diag(α)·p) = α_1^8 α_2^2 g(p)` for one seeded torus element.
  This checks that "top square submatrix" is read with the right orientation.

## Controls

- **C1** Lemma 5.5: a tableau with a repeated entry in one column evaluates to 0 at all points.
- **C2** pure power `p = x_1^5` (`R = 1`, `ℓ = e_1`): `g(p) = 0`.
- **C3** well-definedness: `p = 2ℓ_1^5 + ℓ_2^5 + ℓ_3^5` evaluated with weights `(2,1,1)` and as
  `(1,1,1,1)` with `ℓ_1` repeated gives the same value, for `g` and for K2's `T̂`.

Seeds: `random.Random(2509210401)`; entries of `ℓ_i` in `[-3,3]`.

## Price, limits, stop rule

At most `R^d = 4^5 = 1024` placements × ≤ 20 small determinants per evaluation, ≈ 60 evaluations:
**< 5 s, < 100 MiB** (Python startup dominates). Wrapped by `analysis/b15_bound.py`
(`ca001081…`), `--seconds 60 --memory-mb 512`, one process, one thread, under the shared exclusive
lease. Any failed assertion stops the run and is reported as a failure, not rerun silently; a
rerun would count as pilot 2. Outputs: `results/b25_04/p1_factor.json` and stdout; the script
prints and asserts this file's SHA-256 before any mathematical work.
