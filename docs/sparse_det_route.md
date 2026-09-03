# The determinant side at `O(nnz)` memory: a sparse certificate, and the balanced six-row corner

Session 45 (2026-09-03), branch `s45-sparsedet`, clone tip `0c229c1` (clone
check passes: `analysis/wk9_s36_stabred.py`, `analysis/wk8_s30_calib.py`,
`results/s36_ledger.md`, `results/s41_ledger.md`, `docs/sixrow_frontier.md` all
present; no session 45 in the repository).  Pre-registration
`results/PREREG_s45.md` (commit `bbd7d06`, **before any measurement**).
Validation `results/s45_validation.md`; ledger `results/s45_ledger.md`; raw
records `results/s45_cells.jsonl`, `results/s45_buildcurve.jsonl`,
`results/s45_v{2,3,4,5}.*`; logs `results/logs/`; code
`analysis/wk9_s45_*.py` and the session-42 C helper `analysis/wk9_s42_wied.c`
used unchanged.  Labels: **proved** / **measured** / **adopted-from-literature**
/ **expectation**.

## 0. Verdict

> **The determinant-side memory wall is gone, and the balanced six-row corner is
> open.**  Session 41's frontier `n_χ = 19,985` was set by `8 n_χ²` bytes of
> dense `rref`; the quantity actually wanted is the nullity of a sparse matrix,
> which needs `O(nnz + n)`.  Session 42 built that route on the reducible side.
> This session carries it to the determinant side at scale — the evaluation rows
> at `n_χ ~ 10^5`, and a streaming build that removes the Python objects the old
> pipeline needed — and sweeps with it.
>
> **The frontier moves from `n_χ = 19,985` to `n_χ = 114,875`**, and the
> binding constraint moves from `n_χ` (memory) to `N_S` (build time): the
> largest cell measured has `N_S = 4,408,003` monomials, `n_χ = 99,480`,
> and peaks at 1.03 GB — against the `106` GB the dense
> route would need at the largest `n_χ` reached.  Session 41's own frontier cell `(12,9,3,2,1,1)_7` cost it
> **2500 s and 4.68 GB**; here it costs **62 s** and its build 0.4 s.
>
> **9 determinant-side cells measured, 9 of them with `mult_det = a` proved by a single-prime nonsingularity certificate — no bite, no onset.**  They run from `n_χ = 23700` to `n_χ = 114875` and from balance 11 down to balance **4**; the pre-registered prediction (§5 of the pre-registration: no cell shows `mult_det < a`, confidence 85–90 %) held at every one.
>
> **The certificate is one-sided and that is the point.**  `rank_p ≤ rank_Q`, so
> `nullity_p([E; ev]) = 0` at a *single* prime **proves** `mult_det = a` over
> `Q`; no randomness enters that implication (§1, Lemma 2).  A positive nullity
> is only a measurement until its kernel is exhibited and verified — which is
> why the validation battery is dominated by cells where the answer is *not*
> full rank: all six pad-side bites the programme has, each returned with an
> exhibited rational vector verified over `Z` and against Theorem (★), plus 200
> synthetic matrices with planted nullities 0–6 and the `l^3 m` witness.  A
> route that answered "full column rank" unconditionally would pass every
> determinant-side test in the repository.
>
> **The obstruction question is untouched and the six-row onset is pushed
> further out.**  With these cells the six-row record is 99 cells / 223 ambient units, `mult_det = a`
> at every one; `mult_pad ≤ a = mult_det` still makes `D > 0` arithmetically
> impossible wherever the determinant ideal is empty, and it is empty
> everywhere reached.

## 1. The construction and its two lemmas

Fix a cell `(λ, δ)` with `n = 4` and `r = ℓ(λ)`.  Let `V_χ` be the
`χ_λ`-isotypic reduction of the `λ`-weight space of `C[Sym^4 C^r]_δ`
(`docs/stabiliser_reduction.md`), `dim V_χ = n_χ`, and let `E` be the stack of
simple raising operators restricted to `V_χ`, so `HWV_λ = ker E` and
`dim ker_Q E = a`, the plethysm value.  For points `P_1, …, P_K` let `ev_j` be
the row that evaluates a weight vector at `P_j`, contracted to
`χ`-coordinates.

**Lemma 1 (the pairing; proved, elementary).**  For `K ≥ a` points in general
position on the orbit closure,

    mult_det(λ, δ)  =  a − dim ker [ E ; ev_1 ; … ; ev_K ].

*Proof.*  `mult_det(λ, δ)` is the rank of the evaluation pairing
`HWV_λ × {P_j} → C`, i.e. `a − dim(HWV_λ ∩ ann(P_1, …, P_K))`.  A vector of
`V_χ` lies in `HWV_λ` iff it is killed by every simple raising operator, i.e.
iff it is in `ker E`; it annihilates every point iff it is in `ker[ev_j]`.  So
`HWV_λ ∩ ann(points) = ker[E; ev]`. ∎  (The house choice `K = a + 8` is
inherited from `wk8_s30_core.measure`; `a` points suffice for the rank and the
eight extra are the standing margin against a degenerate draw.)

**Lemma 2 (the one-sided certificate; proved).**  For any integer matrix `F`
and any prime `p`, `rank_p F ≤ rank_Q F`, hence
`nullity_p F ≥ nullity_Q F`, hence with `F = [E; ev]`

    a − nullity_p([E; ev])   ≤   mult_det(λ, δ)   ≤   a .

In particular **`nullity_p([E; ev]) = 0` at one prime proves `mult_det = a`
over `Q`.**  *Proof.*  Reduction mod `p` of a matrix over `Z` cannot raise the
rank (a nonvanishing `k × k` minor over `F_p` lifts to a nonzero minor over
`Z`).  The right inequality is `mult_det ≤ dim HWV_λ = a`.  ∎  The direction
that is *not* free is the other one: `nullity_p = k > 0` gives only
`mult_det ≥ a − k` proved and `mult_det = a − k` measured, and is promoted to
proved only by exhibiting `k` independent rational kernel vectors and verifying
them exactly.  The same statement holds verbatim on the pad side with true
padded-permanent points, and point-free for `mult_red` by (★).

### 1.1 Deciding the nullity without dense linear algebra

The two Wiedemann lemmas are session 42's (`docs/reducible_engine.md` §A3),
restated because this session's matrix is `[E; ev]`, not `E_red`.  Let `F` be
`m × n` over `F_p`, `D_1, D_2` diagonal with entries uniform in `F_p^*`, and
`M = D_2 F^T D_1 F D_2`, never formed — only its action
`x ↦ D_2(F^T(D_1(F(D_2 x))))`.

**Lemma 3 (preconditioner; proved).**  `rank(F^T D F) = rank F` with
probability `≥ 1 − n/p`.  *Proof.*  Let `ρ = rank F` and let `S` be `ρ`
independent columns.  Cauchy–Binet gives
`det((F^T D F)_{S,S}) = Σ_{|T| = ρ} det(F_{T,S})² ∏_{i∈T} d_i`, a polynomial of
degree `ρ` in the `d_i` whose monomials are distinct across `T` and which is
nonzero because some `det(F_{T,S}) ≠ 0`; Schwartz–Zippel bounds the vanishing
probability by `ρ/p ≤ n/p`. ∎

**Lemma 4 (the certificate; proved).**  Take `u, b ∈ F_p^n`, form
`s_i = u^T M^i b` for `0 ≤ i < 2n`, and let `f` be the minimal polynomial of
that sequence (Berlekamp–Massey).  If `deg f = n` and `f(0) ≠ 0` then `M` is
nonsingular and `F` has full column rank.  *Proof.*  The minimal polynomial of
the sequence divides the minimal polynomial of `b` under `M`, which divides the
minimal polynomial of `M`, which divides its characteristic polynomial, of
degree `n`.  `deg f = n` forces all four equal, so `f` is the characteristic
polynomial and `f(0) = ±det M ≠ 0`.  If `F x = 0` then `M(D_2^{-1}x) = 0`, so
`x = 0`. ∎  **No randomness enters this implication**: `D_1, D_2, u, b` decide
only whether a run is *conclusive*, never whether a conclusive verdict is
correct.

**Kernel direction.**  If `f = x^s g` with `g(0) ≠ 0`, then
`y = D_2 M^{s−1} g(M) b` is a *candidate* kernel vector; it is verified by the
sparse product `F y = 0` — in C, and again in Python against the full
`[E; ev]` — before it is reported.  `k` verified independent vectors prove
`nullity_p ≥ k`; a Lemma-4 certificate for `[F; R]` with `R` a random `k × n`
dense block proves `nullity_p ≤ k`.  So a reported nullity is certified in both
directions by objects a reader can re-check with sparse products, plus one
Berlekamp–Massey computation whose output is additionally checked inside the C
helper to annihilate the whole sequence.

**Row compression, and the one change this session makes to it.**  Sampling and
`±1`-grouping the rows of `E` can only lose rank, so a nonsingularity
certificate for the compressed matrix still proves `[E; ev]` injective; a kernel
vector that fails on the full matrix escalates to the next level.  The change:
**the `K` evaluation rows are pinned** — only the rows of `E` are sampled, and
the `ev` rows are stacked on afterwards.  They are dense (one entry per column)
and there are only `K` of them, so they cost `K·n_χ` of the `nnz`; sampling them
away would manufacture spurious kernel vectors and force needless escalation
without changing any verdict.  Three levels are used, `(3,2) → (12,2) →
uncompressed`, and the ledger records which one carried each verdict.

**Cost.**  `O(n·nnz)` field operations per sequence and `O(nnz + n)` memory,
against `O(n³)` time and `8n²` bytes dense.  Measured constants in §3.

## 2. The build, which is now the binding constraint

For balanced `λ` the stabiliser is trivial or small, so `n_χ ≈ N_S` and the
build is the whole cost.  Session 42's build is vectorised but stores `|Stab|`
index arrays of length `N_S`, the Python `basis` list of `N_S` tuples and
(optionally) the `vecs` list of `N_S` dicts, and recovers the raising
operators' target set by an `np.unique` over an `N_S·δ` concatenation.  At
`N_S ~ 10^6` that is already gigabytes.  `analysis/wk9_s45_build.py` changes
*how*, never *what* — every step is checked against the s36/s42
implementations at 16 cells (`results/s45_validation.md` §2):

**(a) Monomials by an exact feasibility DP.**  The weight-`λ` monomials are
produced as an `(N_S × δ)` `int32` array, level by level, never as a Python
list.  The naive prune (`residual ≥ 0`, `residual ≤ n·(factors left)`) overshoots
badly — at `(7,7,6,6,1,1)_7` it holds 5,537,426 length-6 prefixes for a cell with
`N_S = 832,523`.  Instead a DP over the *small* state space (distinct residual
weight, minimum allowed index) decides feasibility exactly:
`G[k][t][i] = 1` iff `A[i] ≤ REM_k[t]` and `REM_k[t] − A[i]` is a sum of
`δ−k−1` exponent vectors with indices `≥ i`, computed by a backward suffix-OR
over `D_k × L` states with `D_k` in the thousands and `L = |exps(4,r)| = 84` at
`r = 6`.  **No dead prefix is ever stored**, so the live set never exceeds `N_S`
at any level.  Breadth-first expansion in index order reproduces the depth-first
lexicographic order of `wk8_s30_core.monomials` exactly (asserted).  Measured:
`N_S = 10,060,304` in 11.3 s at 1.10 GB, against 2.7 s for `monomials()` at
`N_S = 75,689` — a 25× speed-up at the small end and the difference between
possible and impossible at the large one.

**(b) The isotypic reduction in two group passes.**  `canon[j] = min_g index(g·m_j)`
and `acc[j] = Σ_g χ(g)[g·rep_j = j]` are computed in two passes over
`Stab_W(λ)`, each pass recomputing the image index rather than storing `|Stab|`
arrays of length `N_S` (which at `N_S = 10^7`, `|Stab| = 120` would be 9.6 TB).
The s42 assertions are kept and vectorised: `|acc| = |Stab|/|orbit|` on every
kept orbit, and — a theorem, now checked — the twisted sum vanishes on **every**
member of a dropped orbit, not only on its representative.

**(c) Raising operators against a directly enumerated target basis.**  For each
`E_{i,i+1}` the target set is the weight-`λ + e_i − e_j` monomial basis,
enumerated by (a) and ranked by the same multiset combinadic, so the operator is
assembled by `searchsorted` in chunks with periodic consolidation into CSR — no
`np.unique` over an `N_S·δ` concatenation, no dense object anywhere.  The
`H`-orbit dedup of target rows and the assertion that `χ`-obstructed `H`-fixed
rows cancel exactly are unchanged.

**(d) Evaluation rows by numpy.**  `wk9_s36_stabred.point_rows` is a Python loop
over `N_S × δ`, needing `basis` and `vecs`.  Here the monomial values are a
running modular product over the `δ` columns of `M` and the orbit sums are one
`add.reduceat` over the monomials pre-grouped by `χ`-column.  Identical output,
entrywise, on the same random stream (asserted, det and pad).

## 3. The measured cost curve

Two curves, because the two costs scale with different quantities: the **build**
with `N_S` (and `|Stab|`), the **solve** with `n_χ · nnz`.

### 3a. Build — time and peak resident as a function of `N_S` *(measured)*

One process per cell, `VmHWM`.  `mono` is the monomial array, `orbits` the
isotypic reduction (`2|Stab|` numpy passes), `rows` the raising operators.

| λ | δ | `N_S` | \|Stab\| | `n_χ` | rows | `nnz` | `nnz/N_S` | mono s | orbits s | rows s | build s | HWM GB |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| `(9, 9, 6, 2, 1, 1)` | 7 | 177331 | 4 | 36090 | 177881 | 693243 | 3.91 | 0.2 | 0.3 | 1.7 | 2.2 | 0.14 |
| `(12, 12, 3, 3, 1, 1)` | 8 | 237040 | 8 | 23700 | 171279 | 630087 | 2.66 | 0.6 | 0.8 | 3.0 | 4.4 | 0.16 |
| `(9, 9, 4, 4, 1, 1)` | 7 | 314143 | 8 | 32631 | 243459 | 933623 | 2.97 | 0.3 | 1.2 | 3.8 | 5.4 | 0.19 |
| `(8, 8, 7, 3, 1, 1)` | 7 | 387460 | 4 | 79865 | 404493 | 1619899 | 4.18 | 0.7 | 0.8 | 4.2 | 5.8 | 0.19 |
| `(8, 8, 5, 5, 1, 1)` | 7 | 603787 | 8 | 62613 | 494685 | 1957617 | 3.24 | 0.6 | 2.9 | 9.2 | 12.6 | 0.22 |
| `(7, 7, 6, 6, 1, 1)` | 7 | 832523 | 8 | 87045 | 720637 | 2882165 | 3.46 | 0.8 | 5.0 | 14.6 | 20.4 | 0.27 |
| `(8, 8, 6, 2, 2, 2)` | 7 | 1184921 | 12 | 114875 | 1418175 | 4120214 | 3.48 | 1.1 | 11.0 | 27.6 | 39.7 | 0.32 |
| `(9, 9, 9, 3, 1, 1)` | 8 | 1404263 | 12 | 97399 | 1333285 | 6167051 | 4.39 | 2.4 | 14.2 | 29.0 | 45.5 | 0.41 |
| `(6, 6, 6, 6, 2, 2)` | 7 | 4408003 | 48 | 99480 | 3628307 | 14273855 | 3.24 | 8.0 | 361.4 | 293.9 | 663.4 | 1.0 |

**The law.**  Peak resident is linear in `N_S` with slope about
`159` bytes per monomial plus a fixed ~0.15 GB of interpreter and
libraries; build time is linear in `N_S` with the group passes as the only
superlinear-looking term (`orbits` scales as `N_S·|Stab|`).  The extremes
measured: `N_S = 177331` in 2.2 s, and
`N_S = 4408003` (`|Stab| = 48`) in 663.4 s at 1.0 GB.
`nnz(E) ≈ 3.50·N_S` across the whole range
(2.66–4.39), independently of `|Stab|` — the single most useful
number for planning a successor sweep.  **Compare the dense route**: `8 n_χ²`
bytes, i.e. 106 GB at the largest `n_χ` reached here
(`n_χ = 114875`) and 79 GB at the largest `N_S` cell, against the
1.0 GB this route actually used anywhere.

### 3b. Solve — the sequence cost *(measured)*

`nnz_c` is the `nnz` of the compressed stack that carried the verdict (the
level in the ledger); one sequence is `2 n_χ` matvecs at `2 nnz_c` field
operations each, and the two house primes run concurrently on the two cores,
so the wall time of a cell is one sequence plus the build plus
Berlekamp–Massey.

| λ | δ | `n_χ` | level | `nnz_c` | `nnz_c/n_χ` | seq s | wall s | ns per element-op |
|---|---|---|---|---|---|---|---|---|
| `(12, 12, 3, 3, 1, 1)` | 8 | 23700 | (3,2) | 593658 | 25.0 | 94 | 1605.9 | 1.66 |
| `(9, 9, 4, 4, 1, 1)` | 7 | 32631 | (3,2) | 766648 | 23.5 | 175 | 2331.7 | 1.75 |
| `(9, 9, 6, 2, 1, 1)` | 7 | 36090 | (3,2) | 855590 | 23.7 | 212 | 1402.5 | 1.71 |
| `(8, 8, 5, 5, 1, 1)` | 7 | 62613 | (3,2) | 1432234 | 22.9 | 685 | 721.9 | 1.91 |
| `(8, 8, 7, 3, 1, 1)` | 7 | 79865 | (3,2) | 1838105 | 23.0 | 1237 | 1271.8 | 2.11 |
| `(7, 7, 6, 6, 1, 1)` | 7 | 87045 | (3,2) | 1828426 | 21.0 | 1503 | 1554.1 | 2.36 |
| `(9, 9, 9, 3, 1, 1)` | 8 | 97399 | (12,2) | 6477407 | 66.5 | 8317 | 8527.0 | 3.30 |
| `(6, 6, 6, 6, 2, 2)` | 7 | 99480 | (12,2) | 5591733 | 56.2 | 11889 | 12745.0 | 5.34 |
| `(8, 8, 6, 2, 2, 2)` | 7 | 114875 | (12,2) | 5269103 | 45.9 | 9232 | 13479.5 | 3.81 |

One sequence costs `4 · n_χ · nnz_c` element-operations at
**1.7–5.3 ns** each on this container's single core (the spread is cache:
the random access `xs[col[t]]` leaves L2 as `n_χ` grows past a few times `10^4`).
So a cell costs about `10.6·10^-9 · n_χ · nnz_c` seconds of wall clock,
against `O(n_χ³)` time and `8 n_χ²` bytes for the dense route.

### 3c. Which compression level to start at *(measured; a finding for successors)*

The cheap level `(3,2)` samples `3 n_χ` of the `n_rows` rows of `E` and groups
them in pairs.  It carried the verdict at every cell with
`n_rows / n_χ ≲ 8` and cost a third of what the `(12,2)` level costs.  At
`(8,8,6,2,2,2)_7`, where `n_rows / n_χ = 12.3`, it failed — and failed
*informatively*: the compressed matrix came out with Berlekamp–Massey degree
`114,818` against `n_χ = 114,875`, i.e. exactly `57` short of full column rank,
**at both primes with independent randomness**.  That is sampling loss, not a
kernel of `[E; ev]`: the candidate vector failed the check against the full
matrix and the run escalated, correctly, to `(12,2)`, which certified
nonsingularity.  The escalation is sound but it is not free — that cell cost
3 h 45 m instead of 2 h 30 m.  So the rule this session leaves behind is
**start at `(12,2)` whenever `n_rows / n_χ ≳ 10`**, and the two cells run after
the finding (`(9,9,9,3,1,1)_8` at `13.7` and `(6,6,6,6,2,2)_7` at `36.5`) were
run that way and were certified at the first level they tried.

The episode is also the clearest live demonstration in the session that the
one-sided certificate does what it claims: a compressed matrix that is genuinely
rank-deficient produces a kernel candidate, the candidate is checked against the
full `[E; ev]`, it fails, and no wrong verdict is emitted anywhere.

## 4. The sweep

The order was published in `results/PREREG_s45.md` §4 before any of it was
measured; the ledger is `results/s45_ledger.md`.  Summary:

| δ | λ | balance | `a` | `n_χ` | `nnz` | nullity `[E; ev_det]` | verdict | wall s | HWM GB |
|---|---|---|---|---|---|---|---|---|---|
| 8 | `(12, 12, 3, 3, 1, 1)` | 11 | 6 | 23700 | 630087 | 0 | **`mult_det = a = 6`** (proved) | 1605.9 | 0.89 |
| 7 | `(9, 9, 4, 4, 1, 1)` | 8 | 4 | 32631 | 933623 | 0 | **`mult_det = a = 4`** (proved) | 2331.7 | 0.37 |
| 7 | `(9, 9, 6, 2, 1, 1)` | 8 | 4 | 36090 | 693243 | 0 | **`mult_det = a = 4`** (proved) | 1402.5 | 0.34 |
| 7 | `(8, 8, 5, 5, 1, 1)` | 7 | 3 | 62613 | 1957617 | 0 | **`mult_det = a = 3`** (proved) | 721.9 | 0.4 |
| 7 | `(8, 8, 7, 3, 1, 1)` | 7 | 3 | 79865 | 1619899 | 0 | **`mult_det = a = 3`** (proved) | 1271.8 | 0.36 |
| 7 | `(7, 7, 6, 6, 1, 1)` | 6 | 1 | 87045 | 2882165 | 0 | **`mult_det = a = 1`** (proved) | 1554.1 | 0.45 |
| 8 | `(9, 9, 9, 3, 1, 1)` | 8 | 3 | 97399 | 6167051 | 0 | **`mult_det = a = 3`** (proved) | 8527.0 | 1.08 |
| 7 | `(6, 6, 6, 6, 2, 2)` | 4 | 1 | 99480 | 14273855 | 0 | **`mult_det = a = 1`** (proved) | 12745.0 | 1.03 |
| 7 | `(8, 8, 6, 2, 2, 2)` | 6 | 3 | 114875 | 4120214 | 0 | **`mult_det = a = 3`** (proved) | 13479.5 | 0.49 |

`a` is the plethysm value at every cell and is additionally asserted equal to
the full-`E` nullity at the 3 cells where that second
certificate was affordable.  Both house primes agree at every cell.  No
determinant-side nullity was positive, so the pre-registered stopping rules 3
and 4 (exhibited vectors, exact verification, fresh preconditioner and prime,
20 fresh pencils, then the pad side, then `docs/OBSTRUCTION_CANDIDATE.md`) were
never triggered.

## 5. The balanced corner as this session leaves it

The reason the balanced cells were out of reach is structural, not incidental:
the stabiliser reduction divides the weight space by `|Stab_W(λ)|`, which is `1`
when the parts of `λ` are distinct and small when they are nearly distinct.  So
the cells with `λ_1 − λ_ℓ` small — exactly where a determinant equation is most
plausible, because the `SL_4 × SL_4 ⋊ Z/2` stabiliser of `det_4` leaves most room
in the near-rectangular weights — get the least reduction, and their `n_χ` is
the largest in the region.  That is why session 41's `n_χ ≤ 20,000` frontier saw
nothing below balance 8, and why every cell it measured at balance 8 or 9 had
`n_χ` under 5,000 (`(9,9,7,1,1,1)_7`, `n_χ = 3086`) or sat at the edge.

This session measured 9 cells with balances 4, 6, 7, 8, 11, the best being
**balance 4** at `(6, 6, 6, 6, 2, 2)`, `δ = 7`, `n_χ = 99480` — the most
balanced six-row cell the programme has ever measured on the determinant side,
(it is `λ_1 < δ`, so it cannot itself carry an obstruction — but it can carry the
determinant ideal, and it does not), and `mult_det = a` there too.  Extrapolating the cost law of §3 across the
census (`analysis/wk9_s45_reach.py`; an **expectation**, not a measurement — it
assumes the fitted `nnz_c/n_χ` and the fitted ns-per-op hold at cells nobody has
built):

```
fitted nnz/N_S = 3.50 from 9 measured cells; nnz_c/n_chi = 60.0, 2.3 ns per element-op
  delta=7 eligible (lam_1>=delta): 258 cells -> <=1h 108, <=8h 163, <=48h 203, beyond 55
      balance 4: 3 cells, 1 within 48 h (smallest n_chi 83836)
      balance 5: 8 cells, 1 within 48 h (smallest n_chi 460010)
      balance 6: 18 cells, 6 within 48 h (smallest n_chi 87045)
      balance 7: 33 cells, 16 within 48 h (smallest n_chi 62613)
      balance 8: 40 cells, 27 within 48 h (smallest n_chi 3086)
  delta=7 onset-only (lam_1<delta): 3 cells -> <=1h 0, <=8h 1, <=48h 2, beyond 1
      balance 4: 2 cells, 1 within 48 h (smallest n_chi 99480)
  delta=8 eligible (lam_1>=delta): 591 cells -> <=1h 112, <=8h 181, <=48h 261, beyond 330
      balance 4: 3 cells, 0 within 48 h (smallest n_chi 1693303)
      balance 5: 11 cells, 0 within 48 h (smallest n_chi 3132073)
      balance 6: 27 cells, 0 within 48 h (smallest n_chi 1363750)
      balance 7: 49 cells, 3 within 48 h (smallest n_chi 207927)
      balance 8: 66 cells, 7 within 48 h (smallest n_chi 97399)
  delta=8 onset-only (lam_1<delta): 14 cells -> <=1h 0, <=8h 0, <=48h 0, beyond 14
      balance 4: 5 cells, 0 within 48 h (smallest n_chi 782875)
      balance 5: 5 cells, 0 within 48 h (smallest n_chi 578194)
      balance 6: 2 cells, 0 within 48 h (smallest n_chi 4854423)
```

So the balance-6 and balance-7 corner at `δ = 7` is now *routine* — six and
sixteen cells respectively inside a 48-hour budget — where before this session
none of it was reachable at all; the `δ = 8` balanced corner and the
`λ_1 < δ` onset-only cells above `n_χ ~ 3·10^5` remain out of reach, and the
`δ = 8` rectangles (`(7,7,7,7,2,2)`, `n_χ ≈ 5.8·10^5`) are two orders of
magnitude of work away.

## 6. Honest boundary

**The certificates are one-sided by construction.**  `nullity_p([E; ev]) = 0`
proves `mult_det = a` over `Q` at a single prime, with no probabilistic step in
the implication (Lemma 2, Lemma 4).  A *positive* nullity would prove only
`mult_det ≥ a − k`; the reverse needs exhibited rational vectors, exact
verification and fresh randomness, and that branch was pre-registered
(`results/PREREG_s45.md` §6) but never taken on the determinant side this
session — every swept cell came out full rank.  The branch is not untested: V2
exercises it end to end at six cells where the answer is a drop.

**Randomness enters only through conclusiveness, never through correctness.**
`D_1, D_2, u, b`, the row sampling and the seeds decide whether a run reaches a
verdict; they cannot make a wrong verdict.  A kernel candidate is reported only
after `F y = 0` is checked against the **full** `[E; ev]`; a nonsingularity
certificate is emitted only after Berlekamp–Massey's output is checked to
annihilate the whole sequence.  Berlekamp–Massey is the one hand-written exact
routine in the chain, and V4 is its validation (300 matrices, planted nullities
0–6, against `python-flint`).

**What a `mult_det = a` row does and does not say.**  It says the determinant
ideal `I(D_6^{det_4})` is empty in that cell, so no obstruction can live there:
`mult_pad ≤ a = mult_det` forces `D ≤ 0`.  It says nothing about neighbouring
cells, and nothing about degrees above 8.  The six-row onset is bracketed from
below only; this session pushes that bracket outward in the balanced direction
without closing it.

**The `a + 8` points are a convention, not a theorem.**  `K = a` points suffice
for the rank of the evaluation pairing at a generic draw, and the eight extra
are the house margin (`wk8_s30_core.measure`).  A degenerate draw would *lower*
the measured rank, i.e. report `mult_det < a` — so it can only produce a false
*bite*, never a false `mult_det = a`, and the pre-registered sceptical branch
(fresh points, fresh seeds, a second prime, 20 fresh pencils) exists precisely
to catch that.  No such branch was needed.

**The build's ceiling is now `N_S`, and it is a soft one.**  Nothing in the
route needs `O(N_S)` memory in principle — the monomial array could be
streamed to disk and the group passes done blockwise — so the cells beyond this
session's reach are beyond its *time*, not its method.  The one place the
current implementation genuinely stops is `|Stab|` large *and* `N_S` large
together: `(8,4,4,4,4,4)_7` (`N_S = 10,060,304`, `|Stab| = 120`, balance 4, the
most balanced obstruction-eligible `δ = 7` cell of all) enumerates its monomials
in 11 s but needs 240 group passes over that array, and it did not finish inside
this session's build budget.  It is the natural first target for a successor.

**Two conventions inherited without re-derivation** (adopted-from-literature
within the programme): the corrected raising rule
`E_ij c_α = (α_i + 1) c_{α + e_i − e_j}` (`wk8_s30_core`, calibrated by the
`l^3 m` witness in V1), and the stabiliser-reduction lemma
`HWV_λ ⊆ V_χ` (`docs/stabiliser_reduction.md`).  Both are load-bearing here and
neither is re-proved in this document.


## 7. The frontier as this session leaves it

**Determinant side, `n = 4`, `ℓ(λ) = 6`.**  Reached and proved:
`n_χ = 114875` (`(8, 8, 6, 2, 2, 2)` at
`δ = 7`), against session 41's `19,985` — a
5.7× move.  Largest cell built:
`N_S = 4,408,003` (`(6, 6, 6, 6, 2, 2)` at `δ = 7`,
`|Stab| = 48`) in 663.4 s at 1.0 GB.  Best balance measured:
**4**.  Peak resident anywhere in the sweep:
1.08 GB.

**The binding constraint is now `N_S`, through the `2|Stab|` group passes of the
isotypic reduction, not `n_χ` through memory.**  The named next targets, in
order: `(8,4,4,4,4,4)_7` (`N_S = 10,060,304`, `|Stab| = 120`, balance 4,
`n_χ ≈ 83,836`, the most balanced *obstruction-eligible* `δ = 7` cell of all) —
blocked only by the group passes, which are embarrassingly parallel and could be
blocked over `N_S` on more than two cores; then the `δ = 7` balance-5 and
balance-6 cells listed in §5; then `(7,7,7,7,2,2)_8`.

**Six-row record after this session:** 99 cells / 223 ambient
units across `δ = 6, 7, 8`, `mult_det = a` at **every one**.  The six-row onset
of `I(D_6^{det_4})` is still not observed; the bracket `≥ 9` in every component
reached is unchanged in degree and pushed outward in balance, from 8 to
4.  `D > 0` remains arithmetically impossible everywhere reached.
