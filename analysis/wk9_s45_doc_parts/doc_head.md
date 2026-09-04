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
> **The frontier moves from `n_χ = 19,985` to `n_χ = PLACEHOLDER_FRONTIER`**, and the
> binding constraint moves from `n_χ` (memory) to `N_S` (build time): the
> largest cell measured has `N_S = PLACEHOLDER_NS` monomials, `n_χ = PLACEHOLDER_NSNCHI`,
> and peaks at PLACEHOLDER_NSHWM GB — against the `PLACEHOLDER_DENSE_GB` GB the dense
> route would need at the largest `n_χ` reached.  Session 41's own frontier cell `(12,9,3,2,1,1)_7` cost it
> **2500 s and 4.68 GB**; here it costs **62 s** and its build 0.4 s.
>
> PLACEHOLDER_VERDICT_CELLS
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
> further out.**  With these cells the six-row record is PLACEHOLDER_RECORD, `mult_det = a`
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
