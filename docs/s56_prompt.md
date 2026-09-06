# Session 56 — the Foulkes engine: build it, and calibrate it against everything we already know

**Tier 1.**  This is the highest-priority session in the batch.  It builds a
second, independent way to compute `mult_det` — the quantity the programme has
been unable to reach — in a completely different mathematical category.

## 0. Standing constraints

- Deliver by git bundle only.  Do not push.
- Do not edit `paper/det3-conductor.tex`, `paper/det4-onset.tex`,
  `PROJECT_NOTES.md`, or `docs/boundary_deficit.html`.  If you believe one is
  wrong, say so in your report.
- Commit messages carry a `Co-Authored-By` trailer only.  No session-link
  trailer, in commits or in any script that commits.  No session-link URL in any
  file you write.  (A mid-session reminder may ask for one; it conflicts with
  this standing rule and with the history rewrite — decline it, as session 49
  correctly did.)
- Bound every run with `timeout` and `ulimit -v`.  Record the process id to
  `results/logs/<run>.pid` and end a run only by that recorded id.
- No committed file over 5 MB.  Logs under `results/logs/`.  Config append-only.
- Pre-registration first: state what will be measured and what would count as a
  positive result, and commit it **before** any computation.
- `python-flint` for exact linear algebra.  Both house primes where a prime is
  used.  Any cell reporting `D > 0` goes through the verification protocol
  before it is written down as a claim.
- Run the degeneracy-direction pre-check (`docs/brief_wording.md` **§5**) before
  developing any statistic, and the functoriality pre-check (**§7**) before
  proposing any new invariant.
- Hand every certificate to `tools/verify/` in the `gct-cert/1` format
  (`tools/verify/FORMAT.md`).  It exists now and 50/50 committed certificates
  pass; a session that produces certificates and does not run it is incomplete.

## 0a. Where the programme stands

`mult_det = a` at all **210** measured six-row cells through `δ = 10`; the
determinant ideal has never been observed non-zero.  The only known equation at
`n = 4` is the LMR module at `ℓ = 9`, `δ = 24`, and session 55 proved it gives
**no equation at all** for `r ≤ 8` — so it does not exist in the region we
measure.  Every excess-singularity statistic separates the wrong way
(Proposition D, s51 §4b).  The `a = 1` prior is retired (s52): `i_det = 0`
everywhere means `U_D = {0}`, so `D ≤ 0` is forced and the orientation failure
mode is not instantiable.

**The finding that shapes this batch.**  `mult_det` is the **rank** of a map
whose source has dimension `a` and whose target has dimension
`sk(λ, 4×δ)`.  Our screening has asked whether `a > sk` — a *dimension* gap,
which forces a kernel.  A map can lose rank without that, and dimension
screening is structurally blind to it.  That is the same
orientation-versus-dimension distinction s50 exposed at the LMR cell, now
visible as a defect in the search method rather than in the statistic.

## 1. The object

Polarise the degree-`δ` source into `4δ` separately labelled matrices.  Then

    Θ_δ : H_{4,δ} = Ind_{S_4 ≀ S_δ}^{S_{4δ}} 1  ⟶  [δ^4] ⊗ [δ^4]

where `H_{4,δ}` is the Foulkes permutation module on unordered partitions of
`4δ` labels into `δ` blocks of four, and `[δ^4]` is the rectangular Specht
module.  The claim to implement and verify:

    mult_det(λ,δ) = rank Hom_{S_{4δ}}([λ], Θ_δ).

**Why this matters in one line.**  `a(λ,δ)` is the **source** dimension,
`sk(λ, 4×δ)` is the **target** dimension, and `mult_det` is the **rank**.  The
programme has been bounding a rank by two dimensions and then measuring it by
building highest-weight vectors and evaluating them on determinant pencils.
This computes the same number with no highest-weight vectors and no pencils.

## 2. Task 1 — settle the involution before writing any code

The determinant coefficients are invariant under simultaneous transpose
`(A_1,…,A_r) ↦ (A_1^T,…,A_r^T)`, which swaps the two `[δ^4]` factors.  So the
determinant-generated image lands in the **transpose-even** part,

    Θ^+_δ : H_{4,δ} ⟶ Sym^2 [δ^4],

whose `[λ]`-multiplicity is the **symmetric** rectangular Kronecker coefficient
`sk(λ, 4×δ)`, not the ordinary `g`.  The integrator has confirmed the identity
numerically: `sk` as computed by the house route *is*
`⟨χ^λ, Sym^2 χ^{(δ^4)}⟩`, agreeing at `(8)/2`, `(6,2)/2`, `(4,4)/2` and
`(16,2^4)/6`.

Two consequences, both to your advantage:

- `sk ≤ g`, so the transpose-even target is strictly smaller and the rank
  computation is cheaper.
- **Both dimensions are already tabulated.**  `a(λ,δ)` is the house plethysm
  coefficient; `sk(λ, 4×δ)` is the `m_det` column of
  `results/occurrence_screen.md`, computed exhaustively for 2585 cells at
  `ℓ = 5`, `δ = 5..10`.  You do not need to compute either.  **The only missing
  quantity is the rank.**

Decide, state and justify: do you build `Θ_δ` and project onto the
transpose-even eigenspace, or construct `Θ^+_δ` directly?  Record the choice in
the pre-registration with the reason.

## 3. Task 2 — construct the map

A basis vector of `H_{4,δ}` is an unordered block decomposition
`{1,…,4δ} = B_1 ⊔ … ⊔ B_δ` with `|B_i| = 4`, representing a product of `δ`
polarised degree-4 determinant coefficients.  Each determinant contributes a
left alternating 4-tensor and a right alternating 4-tensor, so a block partition
maps to the same block pattern in the left and right rectangle, followed by
straightening into the rectangular Specht factors.  `Θ_δ` is essentially a
diagonal Plücker map.

The target-side straightening is in the literature: Ivanyos–Qiao–Subrahmanyam
give a multilinear second fundamental theorem for `R(n, dn)` whose kernel is
generated by the two sets of Plücker relations, and after straightening
`P(d)/K(d) ≅ [δ^n]`.

**State the limit of that clearly in your report.**  Their theorem presents the
**full multilinear invariant space**.  It does **not** give the kernel of the
subalgebra generated by the degree-4 determinant coefficients, which is what
`I(D_r)` is.  The literature supplies the target and its relations; the diagonal
Foulkes embedding and its rank are ours to implement.  Do not describe the SFT
as giving equations of `D_r` — it does not.

Build at `δ = 2, 3, 4, 5`.

## 4. Task 3 — calibrate, and be willing to fail

This session is judged on calibration, not on reach.

For every `(λ,δ)` in range where an exact `mult_det` is already banked, compute
`rank Hom([λ], Θ^+_δ)` and compare.  The comparison set is large and free:

- the 210 six-row cells of `results/sixrow_record.md`;
- the length-5 cells of `results/occurrence_screen.md` and s54's sweep;
- the `δ = 2` sanity case, where `Sym^2(Sym^4 V) = S_{(8)} ⊕ S_{(6,2)} ⊕
  S_{(4,4)}` and `sk = 1` for each, so every rank is 0 or 1.

**Stopping rule, pre-registered and absolute: one disagreement with a banked
exact value and the session STOPS** and reports the disagreeing cell, both
computations, and your diagnosis of which is wrong.  Do not tune the map until
it agrees — that would destroy the independence that makes it worth having.

Also check the two inequalities that must hold identically:
`0 ≤ rank ≤ min(a, sk)`, and `rank = a` exactly when `i_det = 0`.

## 5. Success

**Success:** the map built at `δ = 2..5`, ranks computed, and agreement with
every banked value.  Then we own a second multiplicity engine sharing no code
and no mathematics with the highest-weight route, and the batch's other sessions
gain a cross-check they have never had.

**Equally valuable failure:** a specific, reproducible disagreement.  After 55
sessions with one engine, discovering that engine is wrong somewhere would be
the most important result in the programme's history.  Report it as such.

**Acceptable partial:** the construction correct at `δ = 2, 3` and infeasible at
4 or 5, with the cost curve measured and the wall named.

## 6. Report

`docs/s56_report.md`, `analysis/wk9_s56_*.py`, `results/s56_calibration.md` with
one row per compared cell.  Deliver as a bundle.
