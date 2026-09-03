# Pre-registration — session 45: the determinant side at `O(nnz)` memory

Branch `s45-sparsedet`, clone tip `0c229c1`.  Written and committed **before any
measurement of this session**.  Labels used throughout: **proved** / **measured**
/ **adopted-from-literature** / **expectation**.

Clone check (all present, so the clone is current): `analysis/wk9_s36_stabred.py`,
`analysis/wk8_s30_calib.py`, `results/s36_ledger.md`, `results/s41_ledger.md`,
`docs/sixrow_frontier.md`.  Session 42's machinery is also present and will be
used unchanged where it applies: `analysis/wk9_s42_sparse.py`,
`analysis/wk9_s42_wied.c`, `analysis/wk9_s42_redengine.py`,
`analysis/wk9_s42_orbits.py`, `analysis/wk9_s42_detcert.py`.  No session 45
exists in the repository.

---

## 0. What this session claims to add

Session 41's determinant-side frontier `n_χ = 19,985` was set by memory:
the dense in-place `rref` costs `8 n_χ²` bytes.  The quantity actually wanted is
`nullity_p` of a sparse matrix, which needs `O(nnz + n)` memory.  Session 42
built and validated that route on the **reducible** side.  This session carries
it to the **determinant** side at scale, which needs three things session 42 did
not need:

1. the `K = a + 8` evaluation rows at `n_χ ~ 10^5` without the Python
   `basis`/`vecs` objects (`point_rows` of `wk9_s36_stabred` is `O(N_S·δ)`
   Python operations per point and needs the orbit dicts in memory);
2. a **streaming build**: the weight-`λ` monomials as an `int32` array produced
   without a Python list of `N_S` tuples, the isotypic reduction in `O(N_S)`
   memory with `|Stab|` numpy passes instead of `|Stab|` stored index arrays,
   and the raising operators assembled chunkwise into CSR against a directly
   enumerated target basis (no `np.unique` over an `N_S·δ` concatenation);
3. the balanced corner, where `|Stab_W(λ)| = 1` or small, so `n_χ ≈ N_S` and the
   build is the entire cost.

## 1. The construction being pre-registered

Fix `(λ, δ)`, `n = 4`, `r = ℓ(λ) = 6`.  `V_χ` = the `χ_λ`-isotypic reduction of
the `λ`-weight space of `C[Sym^4 C^r]_δ` (`docs/stabiliser_reduction.md`),
`dim V_χ = n_χ`; `E` = the stacked simple raising operators on `V_χ`, so
`HWV_λ = ker E` and `dim ker_Q E = a` (the plethysm value — **asserted**, never
read off a kernel).  `ev_j` = the row evaluating a weight vector at the point
`P_j`, contracted to `χ`-coordinates.  Then

    mult_det(λ, δ) = a − dim ker [ E ; ev_1 ; … ; ev_K ],    K = a + 8 det points,

and since `rank_p ≤ rank_Q`, at any prime `p`

    a − nullity_p([E; ev])  ≤  mult_det  ≤  a.                         (†)

**`nullity_p([E; ev]) = 0` at one prime is a proof that `mult_det = a`.**  A
positive nullity is only a measurement: it is promoted by exhibiting `k`
independent kernel vectors, verifying them exactly, and re-running under fresh
randomness at a second prime.  Same statement on the pad side with true
padded-permanent points (`per_padded(3,4)` through `restrict()`), and
point-free for `mult_red` by (★).

Nullity is decided by the session-42 Wiedemann certificates (Lemmas A3, A4 of
`docs/reducible_engine.md`): `M = D_2 F^T D_1 F D_2` applied only as an operator,
`s_i = u^T M^i b` for `i < 2n`, Berlekamp–Massey; `deg f = n` and `f(0) ≠ 0`
proves `F` injective, with no randomness in the implication.  Row sampling and
`±1`-grouping can only lose rank, so a nonsingularity certificate for a
compressed matrix still proves `F` injective; a kernel vector that fails on the
full `E` escalates.

## 2. Validation battery — required, both house primes (`2147483647`, `2147483629`)

Nothing downstream counts if any of these fails.  The battery is deliberately
dominated by cells whose answer is **not** full rank, because a route that
always answered "full column rank" would pass every `mult_det = a` test in the
repository.

| # | test | pre-registered expected outcome |
|---|---|---|
| V1 | the `l^3 m` witness: `a = 1`, kernel `∝ (12, −3, 1)`, `mult = 0`; `analysis/wk8_s30_calib.py` as-is (48-cell battery, 41 discriminating) | `CALIBRATION PASSED`, kernel `(12,−3,1)`, `mult = 0` |
| V2 | every pad-side bite in the programme, through the new sparse det/pad driver: `(8,4,4,4,4)_6` (`a=2`, `mult_pad=1`), `(9,9,8,1,1)_7` (`a=2`, `1`), `(8,8,8,2,2)_7` (`a=3`, `2`), `(12,4,4,4,4)_7` (`a=4`, `3`), `(10,8,7,1,1,1)_7` (`a=3`, `2`), `(13,10,6,1,1,1)_8` (`a=9`, `mult_pad=8`) | the drop returned at both primes; every exhibited kernel vector satisfies `E v = 0` and (★) |
| V3 | ≥ 8 `D = 0` rows of `results/s41_ledger.md` reproduced on the **det** side by the sparse route, spanning `n_χ` from small to the s41 frontier | `nullity_p([E; ev]) = 0` at every one, i.e. `mult_det = a`, agreeing with the banked dense answer |
| V4 | Berlekamp–Massey / the whole sparse route on 200 synthetic sparse matrices with planted nullities 0–6, against `python-flint` | 200/200 exact agreement |
| V5 *(added, not in the brief)* | the memory-lean build against `wk9_s42_orbits` / `wk9_s36_stabred` on a spread of cells: identical `n_χ`, identical orbit partition, identical row count and `nnz`, identical row space where a dense rank can check it; and the vectorised `ev` rows identical to `wk9_s36_stabred.point_rows` entrywise | identical at every cell |

`a` is the plethysm value at every cell and is asserted against the full-`E`
nullity wherever that is affordable.

## 3. Predicted frontier and cost curve *(expectation)*

Container: 2 cores, ~7 GB.  One heavy cell at a time; the two primes may run
concurrently (one core each).

**Build.**  Predicted peak resident for the streaming build
`≈ 0.35 GB + (4δ + 28)·N_S + 12·nnz(E)` bytes, i.e. linear in `N_S` with slope
`≈ 56–60` bytes per monomial at `δ = 7–8` plus the operator storage.  Predicted:
`< 0.8 GB` at `N_S = 10^6`, `< 2.5 GB` at `N_S = 5·10^6`.  Predicted build time
`≈ (2|Stab| + 3δ)` numpy passes over `N_S·δ` `int32`, i.e. roughly
`1.5·10^{-7}·N_S·(2|Stab| + 3δ)` seconds — minutes at `N_S ~ 10^6, |Stab| ≤ 12`,
tens of minutes at `N_S ~ 5·10^6, |Stab| = 48`.

**Solve.**  One Wiedemann sequence is `2n` matvecs at `2·nnz` field operations
each.  Session 42 measured `3.2 ns` per `nnz`-element on this container's C
inner loop (`n = 4289, nnz = 4.0·10^5`: 22 s).  With `nnz(E) ≈ 90–100·n_χ`
observed at `ℓ = 6`, one sequence costs `≈ 4·3.2·10^{-9}·n_χ·nnz` seconds
`≈ 1.2·10^{-6}·n_χ²` s.  Predicted: `≈ 20 min` at `n_χ = 4·10^4`, `≈ 2 h` at
`n_χ = 1.3·10^5`… i.e. **`3–4 h` per sequence at `n_χ = 10^5`**, with the two
primes concurrent, plus `O(n²)` Berlekamp–Massey (predicted `< 10 min` at
`n_χ = 10^5`).  Row sampling below `12n` rows is expected to cut this by up to a
third and is pre-registered as an *escalating* first level, never as the final
authority.

**Predicted frontier reached this session:** `n_χ ≈ 10^5` on the determinant
side (a five-fold increase over session 41's `19,985`), with the memory ceiling
moved from `n_χ` to `N_S` and predicted to sit near `N_S ≈ 5·10^6`.  Stretch
target `(6,6,6,6,2,2)` at `δ = 7` (`N_S = 4,408,003`, `n_χ ≈ 91,834`, balance
`4`) — the smallest genuinely balanced six-row cell in the region — is predicted
**reachable in memory** and marginal in time.

## 4. The sweep, published before it starts

Six-row cells, `n = 4`, `ℓ(λ) = 6`, `a ≥ 1`, `λ_1 ≥ δ`, determinant side,
ascending in `n_χ` from 20,000, `δ = 7` then `δ = 8`, most balanced cell
available at each size (`balance := λ_1 − λ_6`; `n_χ` and `N_S` from
`results/sixrow_census.md`, `~` = the census bound `N_S/|Stab|`).  Predicted
cost from §3.

| # | δ | λ | balance | a | N_S | \|Stab\| | n_χ | predicted h/sequence |
|---|---|---|---|---|---|---|---|---|
| 1 | 7 | `(9, 9, 4, 4, 1, 1)` | 8 | 4 | 314,143 | 8 | 32,631 | 0.4 |
| 2 | 7 | `(9, 9, 6, 2, 1, 1)` | 8 | 4 | 177,331 | 4 | ~44,333 | 0.7 |
| 3 | 8 | `(12, 12, 3, 3, 1, 1)` | 11 | 6 | 237,040 | 8 | 23,700 | 0.2 |
| 4 | 7 | `(8, 8, 5, 5, 1, 1)` | **7** | 3 | 603,787 | 8 | ~75,474 | 1.9 |
| 5 | 7 | `(8, 8, 7, 3, 1, 1)` | **7** | 3 | 387,460 | 4 | ~96,865 | 3.1 |
| 6 | 7 | `(7, 7, 6, 6, 1, 1)` | **6** | 1 | 832,523 | 8 | ~104,066 | 3.6 |
| 7 | 7 | `(8, 8, 6, 2, 2, 2)` | **6** | 3 | 1,184,921 | 12 | ~98,744 | 3.3 |
| 8 | 8 | `(9, 9, 9, 3, 1, 1)` | **8** | 3 | 1,404,263 | 12 | ~117,022 | 4.6 |
| S | 7 | `(6, 6, 6, 6, 2, 2)` | **4** | 1 | 4,408,003 | 48 | ~91,834 | 2.8 (+ long build) |

`(8,4,4,4,4,4)_7` (balance 4, `a = 2`, `n_χ ≈ 83,836`) is the most balanced
*obstruction-eligible* `δ = 7` cell of all, but `N_S = 10,060,304` and
`|Stab| = 120`: it is listed as a second stretch target, taken only if the
measured build curve says it fits.  Cells are banked with a commit as they
complete; **breadth is never traded for the first balanced cell** — if time
allows only one of rows 4–8 plus S, S is preferred.

## 5. Predictions on the answer *(expectation, recorded before measuring)*

**Prediction: no cell measured this session shows `mult_det < a`.  I expect
`mult_det = a` at every cell in §4, proved by `nullity_p = 0`.**  Confidence
`≈ 85–90 %`.

Reasoning.  (i) 90 six-row cells through `δ = 8` all have `mult_det = a`, and
`I(D_6^{det_4})_δ` is empty at every cell any session has reached; session 41
bracketed the six-row onset `≥ 9` in every component reached.  (ii) The
five-row analogue switched on only at `δ ≥ 8` and the six-row locus is *larger*
(`dim D_6^{det_4}` grows), so its ideal should switch on *later*, not earlier.
(iii) The arithmetic screen is silent: `a ≤ m_det` at all 849 census cells, with
the tightest margin `m_det − a = 12`; nothing forces an equation.  (iv) The
regime where I would expect an onset first is exactly the balanced corner —
`λ_1 − λ_6` small, `a` small relative to `n_χ` — because the determinant's
`SL_4 × SL_4 ⋊ Z/2` stabiliser leaves most room in the near-rectangular weights;
that is why the sweep is ordered by balance and not by `a`.  If the prediction
fails anywhere, I expect it at rows 6–8 or S (balance ≤ 6), not at rows 1–3.

Secondary predictions: `nnz(E)/n_χ` between 60 and 140 at every swept cell; the
sparse route agrees with every banked dense answer (V3) with no exception; no
prime disagreement anywhere.

## 6. Stopping rules

1. **Any validation failure (V1–V5) stops the session.**  The failure is
   reported, nothing downstream is published, no sweep row is banked.
2. A cell whose build exceeds 5.5 GB resident or 90 minutes, or whose solve
   exceeds 8 hours per sequence, is abandoned and recorded as *not reached*,
   with its measured build curve point kept.
3. `nullity_p > 0` on the det side at any swept cell **halts the ascending
   sweep**.  The cell then gets: `k` exhibited kernel vectors, exact
   verification (`E v = 0` over `Z` by CRT + rational reconstruction, or exact
   evaluation at the points), a re-run at a fresh preconditioner, a fresh seed
   and the second prime, and a check that the vectors are nonzero at 20 fresh
   determinant pencils' worth of independent evaluations.  Only then is
   `mult_det = a − k` recorded as measured.
4. If that survives, the **pad side** is measured at the same cell
   (`mult_pad` at true padded-permanent points, and `mult_red` point-free by
   (★)).  If `D = mult_pad − mult_det > 0`, the sweep halts permanently, the
   verification protocol of `docs/s41_prompt.md` takes over, and the session
   ends with `docs/OBSTRUCTION_CANDIDATE.md` in place of a sweep table.
5. Primes disagreeing on a nullity is a bug or an unlucky prime, never a
   result: a third prime is run and the discrepancy reported either way.
6. `nullity_p(E)` on the full column set exceeding `a` is impossible over `Q`
   and stops the cell with an error.

## 7. Housekeeping

Container only, no push; delivery by `git bundle create sparsedet.bundle
s45-sparsedet` (single ref), checkpointed every few hours.  Commit messages
carry `Co-Authored-By` only — no session-link trailer, in commits or in any
script that commits, and no `claude.ai/...` URL in any file.  Single-writer
files never edited: `paper/det3-conductor.tex`, `paper/det4-onset.tex`,
`PROJECT_NOTES.md`, `docs/boundary_deficit.html`.  No file over 5 MB committed;
logs under `results/logs/`; long runs bounded with `timeout` and `ulimit -v`,
each run's process id recorded in `results/logs/<run>.pid` and ended only by
that recorded id.
