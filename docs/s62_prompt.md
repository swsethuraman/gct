# Session 62 (C1) — the last-born scalar, and what the Gram route actually costs

Batch 10, wave 1.  Ungated.  Base commit `226b4ef1`.
**Read `docs/batch10_worker_preamble.md` first**, then `docs/batch10_plan.md`
§0, §1, §4 (C1) and §5, `docs/lmr_cell.md` §3b, and `docs/s56_report.md`.

## The question

At a room-one closing cell whose predecessor is full rank, does one rational
scalar decide whether a determinant equation is born — and what does computing
it cost?

## The mechanism

The ladder theorem (session 57, Lemma L) says multiplication by `u = e_1^4`
carries highest-weight vectors injectively up a ladder, on the ambient ring, on
the ideal and on `C[D_r]`.  So at a cell where `a_δ − a_{δ−1} = 1` — a *room-one*
cell — the source splits as

    M_δ  =  u·M_{δ−1}  ⊕  ⟨v_ρ⟩

with one new line.  If the predecessor is determinant-full-rank, then
`i_det,δ ∈ {0,1}` and the equation is born exactly when the image of the new
line falls into the transported image.  Writing `G = Θ*Θ` in that splitting,

        ⎡ A   b ⎤
    G = ⎢       ⎥ ,   det G = det A · s ,   s = c − bᵀ A⁻¹ b ,
        ⎣ bᵀ  c ⎦

with `A` nonsingular precisely because the predecessor is full rank.  Then

> **a new determinant kernel is born  ⟺  `s = 0`.**

## Your head start — this is further along than the plan suggests

**`analysis/wk9_s56_hecke.py` already implements the Gram matrix and already
states its double-coset invariance.**  Its docstring records that `π ↦ ε_π` is
not equivariant but that with the increasing coset representative
`K(π,π') = σ(h,π_0) K(π_0, h π_0)`, so one computed row gives the whole signed
Gram matrix, and that **`β = K ∘ K` is `S_N`-invariant and depends only on the
double coset** — `β` being the Gram matrix of `Θ⁺(π) = ε_π ⊗ ε_π`.

So the structural observation is banked, in the repository, from session 56.
**Your session is not to rediscover it.**  It is to (i) measure what it costs,
(ii) lift it to the `λ`-block Schur complement, and (iii) run the positive
control.  Say so in your report — the provenance matters.

Two further facts, measured by the integrator during batch-10 planning and
**unchecked by any session** (verify them; they are cheap):

    pair-orbitals of S_{4δ} on H_{4,δ}    δ=2: 3     δ=3: 9     δ=4: 43
    Sym^δ(Sym^4) constituents             δ=2: 3     δ=3: 9     δ=4: 28
    max multiplicity                      δ=2: 1     δ=3: 1     δ=4: 2
    Σ_λ a_λ²                              δ=2: 3     δ=3: 9     δ=4: 43

with multiplicity 2 at `(12,4)`, `(10,6)`, `(10,4,2)`, `(8,6,2)`, `(8,4,4)`.
`Σ a_λ² = #orbitals` at every degree checked, which is the consistency identity
between the two computations.

**Consequence, and it is binding on how you write this up.**  The `δ = 4`
commutant is `23·(1×1) ⊕ 5·(2×2)`, dimension 43, and it is **not commutative**.
Use coherent-configuration or centralizer language.  Do **not** claim a global
Bose–Mesner diagonalisation, a spectral theorem, or a product formula resting on
commutativity.  What survives is: orbital constancy of the entries; closure
under the Hadamard product, so the squaring that makes this the determinant
problem rather than the Foulkes problem is structurally free; the `a_λ × a_λ`
block; and — decisively — **the room-one Schur complement is a scalar whether or
not the commutant is commutative.**

## Tasks, in order

1. **Support sizing, and it comes first.**  Measure, in your implementation, the
   source / highest-weight-vector / last-born support sizes at `δ = 2, 3, 4`.
   Session 56 avoids highest-weight vectors and so does not record this; what it
   does give is tensor-row support `24^δ` (13 824 at `δ=3`, 331 776 at `δ=4`),
   the `δ=4` weight route at 64 passes with `Σ n_b = 5 709` and `max n_b = 465`,
   example `δ=3` Gram sizes 8, 15, 23, an example `δ=4` certified `51×51` block
   at `(8,4,4)`, and ≈ 2.1 h for the full `δ=4` calibration.  **Produce a cost
   curve, not an estimate.**  This number decides whether the route reaches
   `δ = 23, 24` and it is the single most valuable thing this session can
   deliver.
2. Build the exact **rational** `G = Θ*Θ` on tiny controls, reusing
   `wk9_s56_hecke.py` where you can.
3. Reproduce every `δ = 2` and `δ = 3` full-rank calibration from session 56 —
   40 cells, `mult_det = a`, `i_det = 0` — through the Schur-complement route
   wherever the cell is room-one, and through the plain block rank otherwise.
4. **The positive control, and the session's must-pass.**  The `n = 3` LMR cell
   `λ = (19,7,2⁵)`, `δ = 12`, `ℓ = 7`, `a = 6`, `sk = 10`.  Its `a`-sequence is
   `0,2,4,5,6,6` from `δ = 8` (inner degree 3), so `δ_close = 12` and **it is
   room-one**, and the LMR module is non-vacuous there, so `i_det ≥ 1` by
   theorem.  Therefore:

       ground truth :  rank ≤ 5, not 6
       Gram route   :  s = 0

   Get the ground truth first, by whatever route reaches it — the natural
   candidate is the programme's own evaluation engine, `mult_det = a −
   nullity_Q [E; ev_det]` as in `analysis/wk9_s60_cell.py`, at `r = 7` with
   `det_3` pencils.  Then validate the Gram machinery against it.  **This is the
   first rank drop any engine in this programme would ever have been shown**;
   every one of the 419 measured cells is full rank.  If the ground truth itself
   is out of reach, that is the session's headline finding and it must be stated
   plainly, because it would mean the mandatory positive control is unreachable
   and the Gram programme is unvalidated.
5. Record exactly which pair-orbital / block-intersection data suffices to
   compute a Gram entry, and how the cost of one entry scales.
6. Smith normal forms and determinantal divisors on the small blocks, as **cheap
   diagnostics only**.  Report whether the elementary divisors look generic or
   structured.  This is not a congruence programme and must not become one:
   there is no observed modular rank drop anywhere in the record to fit.

## Binding caveat — characteristic zero

`rank(Θ*Θ) = rank Θ` is **false over `F_p`**.  The Gram route is exact
characteristic zero; at `a × a` with `a` in the hundreds that is free, and the
cost is in the entries, not the rank.  Ordinary mod-`p` full rank of the
*original* map remains a valid characteristic-zero lower bound and is
unaffected.  Say which of the two you used, per claim.

## Success

`s = 0` at the `n = 3` cell and `s ≠ 0` at every known negative control; a
measured cost curve; a written statement of what a Gram entry needs.

## Stopping rules

- Any mismatch with a banked rank stops the implementation, not the theorem —
  find the defect before proceeding.
- If Gram-entry construction explodes by `δ = 4`, **stop the Gram route there**,
  keep the Schur-complement result, and record the cost curve.  Session 63 will
  proceed by the direct `λ`-block route; your cost curve is what tells it to.
- Do not attempt `δ = 23` or `δ = 24` in this session under any circumstances.
  That is session 63's, and it must be entered with your numbers in hand.

## Deliverables

`results/PREREG_s62.md`; `docs/s62_report.md`; the cost table as
`results/s62_cost.md` and `.json`; certificates for every reproduced
calibration in the declared format (`tools/verify/FORMAT.md`); the `n = 3`
positive control as its own artefact with both routes shown side by side; code
under `analysis/wk10_s62_*.py`; bundle `s62_gram.bundle` + `.md5`.
