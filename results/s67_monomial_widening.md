# The widened monomial code (session 67, Part C2)

The session-45 build ranks weight-`λ` monomials by the multiset combinadic
`code(m) = Σ_k C(m_k + k, k+1)` (`analysis/wk9_s42_orbits._codes`), an injection
used only through `argsort`/`searchsorted` to recover each monomial's basis
index.  It was computed in `int64`, with the assertion `C(L+δ−1, δ) < 2^63`.

## What bound actually binds

At `r = 5`, `L = |exps(4,5)| = 70`.  The largest code, `C(70+δ−1, δ) − 1`, fits
a signed `int64` through **`δ = 19`** (`C(88,19) = 8.91·10^18 < 9.22·10^18`) and
overflows at **`δ = 20`** (`C(89,20) = 3.97·10^19`).  Session 60's tail census
used a conservative flag `CODE_SAFE_DELTA = 18` and so reported **892** buildable
closing cells; the true `int64` reach was `δ_close ≤ 19` (**1 048** cells), and
only the **27** cells at `δ_close = 20` genuinely overflowed.

## The widening

`_codes` now selects its dtype by an exact size test (`_codes_fit_int64`):

* `int64` wherever the old code did not overflow — **byte-for-byte the same
  values, dtype and cost**, so every already-reachable build is unchanged;
* exact Python-integer (`object`) only where `int64` would overflow.

Because object integers equal the `int64` values wherever the latter did not
overflow, the two paths give identical `argsort`/`searchsorted` and hence
identical basis indices on every reachable cell — the downstream `n_χ`,
`col_of`, `sgn` and raising matrix `E` are bit-identical (the stopping rule).

## New buildable figure

| | closing cells |
|---|---|
| session 60's flag (`δ_close ≤ 18`) | 892 |
| true `int64` reach (`δ_close ≤ 19`) | 1 048 |
| **after widening (all `δ_close`, up to 20 in the census)** | **1 075** |

The encoding no longer bounds tail closure at length 5; the remaining limit is
`N_S` (build time and memory), the same soft wall as everywhere else — 541 of
the 1 075 closing cells have `N_S ≤ 5·10^6`.

## Evidence

`analysis/wk10_s67_bitident.py` (the C2 regression) builds seven reachable cells
twice — forcing the `int64` path and forcing the object path — and asserts
`N_S`, `|Stab|`, `n_χ`, `col_of`, `sgn`, and the full `E` (shape, `indptr`,
`indices`, `data`, `nfixed`) are identical, at cells up to `n_χ = 70 027` /
`N_S = 205 616`; it confirms the `int64` boundary (fits `δ ≤ 19`, overflows
`δ ≥ 20`); and it builds the smallest `δ_close = 20` cell `(57,17,2,2,2)`
(`N_S = 169 331`, `n_χ = 36 488`, every column reached) — over the old wall,
impossible before this change.  Full build wall: 15 s at 0.16 GB.
