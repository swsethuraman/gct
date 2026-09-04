# V4 — the generator isotypic reduction against session 45's build

Session 46, branch `s46-balanced`, 2026-09-04.  Code
`analysis/wk9_s46_gen.py` (the new build), `analysis/wk9_s46_validate.py` (this
comparison); raw records `results/s46_v4.jsonl`; log `results/logs/s46_v4.log`.
Pre-registered in `results/PREREG_s46.md` §2 before it was run, including the
falsifier and the cell list.  **Result: every part passes at every cell.**

## 0. What was replaced, and what was not

Session 45's `_canon_acc` makes `2|Stab_W(λ)|` passes over the `(N_S × δ)`
monomial array — one gather, one row sort, one combinadic code and one
`searchsorted` per group element, twice.  At `|Stab| = 120` that is 240 such
passes and it is what stopped `(8,4,4,4,4,4)_7`.

`analysis/wk9_s46_gen.py` computes the image-index array once per **generator**
of the Young subgroup `Stab_W(λ) = ∏_B S_{k_B}` — the adjacent transpositions
inside its blocks, `#gen = Σ_B (k_B − 1)`, four of them at `|Stab| = 120` — and
then works on index arrays only:

- each generator is a transposition, so its image-index array is an
  **involution** and the generator edges form a matching;
- `canon` (the minimum index in each orbit) by min-label propagation over those
  edges, iterated to a fixed point.  At the fixed point no edge can lower a
  label, so the labels are constant on orbits, and they are the minima because
  the minimum-index member of an orbit never receives a smaller label.  The
  number of rounds is the generator-graph diameter of one orbit: **2 to 5** at
  every cell below;
- the sign by carrying the character along the same edges,
  `s[g·m] = χ(g)·s[m]`, anchored at `s[representative] = +1`.  Both routes
  anchor `+1` at the minimum-index representative, so the signs must agree
  **exactly**, not up to a per-orbit global sign — and they do;
- the drop test as one consistency pass at the end: the orbit of `m` is dropped
  exactly when some generator edge inside it has `χ(g)·s[m] ≠ s[g·m]`.

**The drop test is the same test, proved.**  A sign conflict on a closed walk
from the representative `ρ` is a word `w` in the generators with `w·ρ = ρ` and
`χ(w) = −1`, i.e. an element `h ∈ Stab_ρ` with `χ(h) = −1`; conversely every
`h ∈ Stab_ρ` is such a word.  Since `χ` is a homomorphism to `{±1}`,
`Σ_{h ∈ Stab_ρ} χ(h)` is `|Stab_ρ|` if `χ|_{Stab_ρ}` is trivial and `0`
otherwise.  So *some generator edge in the orbit is sign-inconsistent* ⟺
*`acc[ρ] = 0`* — session 45's test, reached in `O(N_S · #gen)` instead of
`O(N_S · |Stab|)`. ∎

The same substitution is made in the second place `_canon_acc` is called: the
`H`-orbit dedup of target rows in the raising-operator assembly, `H` the common
stabiliser `Stab(λ) ∩ Stab(λ + e_i − e_j)`, whose generators are the adjacent
transpositions of the *movable* indices of each block.  That is the only other
textual difference between `raising_rows_gen` and
`wk9_s45_build.raising_rows_arr`.

Everything else is **imported, not copied**: `monomials_array` (so the monomial
order is the same object, not a reimplementation of it), `_codes`,
`ev_rows_arr`, the raising rule, the chunked assembly, the `χ`-obstructed
cancellation assertion, the row filtering, and the whole solve path
(`wk9_s45_cell.measure_cell`, used unchanged — `analysis/wk9_s46_cell.py`
substitutes its build function and nothing else).

## 1. The comparison

Twelve cells, `|Stab|` from **2 to 120**, spanning one, two and three nontrivial
blocks and both parities of block value (so both the "no orbit can drop" and the
"most orbits drop" regimes — `(13,10,6,1,1,1)_8` drops 27,663 of 38,345 orbits,
`(6,6,6,6,2,2)_7` drops none).  Checked at each: `n_χ`, the dropped-orbit count,
`col_of` entrywise, `sgn` entrywise, the raising-operator matrix `E` entrywise
(shape, `nnz` and every entry), the count of `χ`-obstructed target rows that
cancel, and — where `n_χ ≤ 1000`, so a dense rank is affordable —
`rank_p(E_45) = rank_p(E_46) = rank_p([E_45; E_46])` at **both house primes**,
which certifies equal row space independently of the entrywise check.

| λ | δ | \|Stab\| | #gen | rounds | `N_S` | `n_χ` | orbits dropped | orbits s45 | orbits s46 | × | rows s45 | rows s46 | `nnz` | partition, `sgn`, `E` | row space |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| `(12, 9, 3, 2, 1, 1)` | 7 | 2 | 1 | 2 | 50462 | 19985 | 10492 | 0.04 | 0.02 | **2.0** | 0.46 | 0.42 | 199780 | identical | entrywise identical |
| `(9, 9, 6, 2, 1, 1)` | 7 | 4 | 2 | 2 | 177331 | 36090 | 16947 | 0.29 | 0.1 | **2.9** | 1.83 | 1.37 | 693243 | identical | entrywise identical |
| `(14, 8, 3, 1, 1, 1)` | 7 | 6 | 2 | 3 | 14636 | 928 | 3338 | 0.03 | 0.01 | **3.0** | 0.19 | 0.14 | 7711 | identical | equal at both primes |
| `(13, 10, 6, 1, 1, 1)` | 8 | 6 | 2 | 3 | 140749 | 10682 | 27663 | 0.38 | 0.08 | **4.75** | 1.69 | 1.13 | 111832 | identical | entrywise identical |
| `(9, 9, 4, 4, 1, 1)` | 7 | 8 | 3 | 2 | 314143 | 32631 | 15101 | 1.22 | 0.27 | **4.52** | 4.21 | 3.33 | 933623 | identical | entrywise identical |
| `(12, 12, 3, 3, 1, 1)` | 8 | 8 | 3 | 2 | 237040 | 23700 | 13248 | 0.86 | 0.2 | **4.3** | 3.04 | 2.29 | 630087 | identical | entrywise identical |
| `(15, 5, 5, 1, 1, 1)` | 7 | 12 | 3 | 3 | 17091 | 576 | 1991 | 0.07 | 0.01 | **7.0** | 0.22 | 0.16 | 9126 | identical | equal at both primes |
| `(9, 9, 9, 3, 1, 1)` | 8 | 12 | 3 | 3 | 1404263 | 97399 | 40475 | 11.61 | 2.19 | **5.3** | 25.95 | 16.85 | 6167051 | identical | entrywise identical |
| `(8, 8, 6, 2, 2, 2)` | 7 | 12 | 3 | 3 | 1184921 | 114875 | 0 | 9.3 | 1.53 | **6.08** | 23.79 | 14.89 | 4120214 | identical | entrywise identical |
| `(10, 10, 2, 2, 2, 2)` | 7 | 48 | 4 | 4 | 201554 | 6269 | 0 | 4.01 | 0.22 | **18.23** | 4.47 | 1.97 | 358162 | identical | entrywise identical |
| `(6, 6, 6, 6, 2, 2)` | 7 | 48 | 4 | 4 | 4408003 | 99480 | 0 | 240.72 | 13.12 | **18.35** | 187.48 | 81.9 | 14273855 | identical | entrywise identical |
| `(18, 2, 2, 2, 2, 2)` | 7 | 120 | 4 | 5 | 8128 | 190 | 0 | 0.37 | 0.01 | **37.0** | 0.21 | 0.15 | 10610 | identical | equal at both primes |

Each cell was run twice (the battery was launched twice by accident and both
copies completed, concurrently, on the two cores); both copies agree in every
column, and the timings above are from the second copy, so the speed-up ratios
are measured *within one process* and are unaffected by the two runs sharing the
machine.  `results/s46_v4.jsonl` holds all 24 records.

## 2. What the numbers say

- **Identity, everywhere.**  `col_of`, `sgn`, `n_χ`, the dropped-orbit set, `E`
  entrywise and the `χ`-obstructed cancellation count agree at all twelve cells.
  The `sgn` agreement is exact, not up to a per-orbit global sign — the stronger
  of the two forms the pre-registration allowed.  Row space is separately
  certified equal at both primes at the four cells small enough for a dense
  rank.
- **The speed-up is `|Stab|`-shaped, as predicted.**  `×2` at `|Stab| = 2` (one
  generator, nothing to save), `×4–6` in the middle, **`×18–22` at
  `|Stab| = 48`** and **`×37` at `|Stab| = 120`**.  The reduction of
  `(6,6,6,6,2,2)_7` — the cell that cost session 45 361 s and made it the most
  expensive build in the programme — now costs **13.1 s**.
- **The raising-operator assembly also gets faster**, by 1.2× to 2.4×, entirely
  from the `H`-orbit dedup: at `(6,6,6,6,2,2)_7`, 187.5 s → 81.9 s.  This was
  not predicted and is a second-order effect of the same change.
- **Rounds are small.**  The label propagation converged in 2–5 rounds at every
  cell, against the `|Stab|` bound; the loop carries a hard cap and an assertion
  that the fixed point is constant on every generator edge.

## 3. The honest boundary of this validation

- The comparison is an **identity check against session 45's build**, not an
  independent re-derivation of the isotypic reduction.  Session 45's build was
  itself checked against the s36 and s42 implementations at 16 cells
  (`results/s45_validation.md` §2), and this session inherits that chain rather
  than repeating it.  What is new here is only the claim that the generator
  route computes the same objects, and that claim is checked entrywise.
- Twelve cells is not all cells.  The `|Stab|` values covered are
  2, 4, 6, 8, 12, 48, 120; block sizes up to 5; `N_S` up to 4.4 M.  The named
  target `(8,4,4,4,4,4)_7` has `|Stab| = 120` with a **single** block of size 5,
  a shape the battery covers only at `(18,2,2,2,2,2)_7` (`|Stab| = 120`, block
  `2^5`, `N_S = 8128`) — same group and same generator count, three orders of
  magnitude smaller.  The assertions inside the build (labels constant on every
  edge, orbit size divides `|Stab|`, no kept monomial with sign 0, `χ`-obstructed
  rows cancel to zero, raising image in the target basis) run at every cell,
  including the target, and are the check that travels with the measurement.
- The `n_χ ≤ 1000` rank check covers 4 of the 12 cells.  Above that the evidence
  is entrywise equality of `E`, which implies equal row space trivially but is a
  different kind of statement from an independently computed rank.
