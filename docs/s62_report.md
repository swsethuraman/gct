# Session 62 — the last-born scalar, the two positive controls, and what the Gram route costs

Branch `s62-gram` off `main` at `226b4ef1` (ancestry gate
`git merge-base --is-ancestor 226b4ef1 HEAD` passed on a fresh clone). Container
only, no pushes. Pre-registration `results/PREREG_s62.md` committed before any
measurement. Delivery by single-ref bundle `s62_gram.bundle` + `.md5`.

**Missing inputs, recorded up front.** The brief names
`docs/batch10_worker_preamble.md` and `docs/batch10_plan.md`. Neither exists at
`226b4ef1`, in any branch of the public repository, or in any of the three
clones on the laptop (`work/`, `gct-rewrite/`, `work-preRewrite/`). This session
worked from the brief's own statement of C1 and from the two integrator notes
delivered mid-session.

## Verdict

The room-one scalar `s` is real, it is a within-degree Schur complement (not a
ratio of two Gram determinants — integrator note 1), and **it vanishes at the
`n = 3` LMR cell and only there.** Three things are banked:

1. **The full `n = 4` `δ = 2,3,4` calibration, reproduced through the block
   Gram** — 40 constituents, `rank_Q G_λ = a`, `i_det = 0` at every one, no
   room-one scalar zero. The centralizer bookkeeping the brief states is
   confirmed exactly, and `β_4` is shown **noncentral**.
2. **Two positive controls, both showing a rank drop.** The `n = 2` cell
   `(2^δ)` is a *proved* drop (the discriminant of a rank-`≤4` matrix): the
   Foulkes Gram returns full rank at `δ = 3,4` and rank `0` at `δ = 5,6`,
   matching the theorem at the boundary — the explicit Gram/Schur machinery
   exhibited end to end. The `n = 3` LMR cell `(19,7,2^5)_{12}` is the
   mandatory control: `mult_det = 5 < a = 6`, `i_det = 1`, at both house primes,
   with the first exhibited element of `I(D)^{HWV}` the programme has ever
   produced.
3. **The cost curve, measured, with `|S|` — the reduced-route support — as the
   number that decides session 63.** The enumeration route dies at `δ = 5`
   (stopping rule 2), and the reduced-route support `|S| ~ n_λ ~ 10¹¹` at the LMR
   cell puts that route out of reach too. Session 63 must run the direct
   `λ`-block (evaluation) route, exactly as the `n = 3` control is done here.

## 0. Provenance — what was banked before this session

The orbital observation is **session 56's**: `analysis/wk9_s56_hecke.py` already
states and verifies that `π ↦ ε_π` is not equivariant, that with the increasing
coset representative `K(π,π') = σ(h,π_0) K(π_0, hπ_0)` so one row gives the whole
signed Gram matrix, that `β = K∘K` is `S_N`-invariant and depends only on the
double coset, and is the Gram matrix of `Θ⁺(π) = ε_π ⊗ ε_π`; and s56 computed the
isotypic ranks at every `δ ≤ 4` constituent. **This session did not rediscover
that.** It (i) lifted the orbital Gram to the `a × a` block on the highest-weight
vectors and the room-one Schur complement; (ii) built two positive controls the
record never had; (iii) measured the cost in the units that decide session 63.
The `n = 4` orbital counts and `Σ_λ a_λ² = #orbitals = 3, 9, 43` are s56's and
stand (verified again here).

## 1. The objects (as implemented)

For a weight `λ ⊢ nδ`, `r = ℓ(λ)`, `H = H_{n,δ}` the Foulkes module. Highest-weight
vectors live in the weight space `H^{S_λ}` (orbit-sum basis `m_O`, one per
weight-`λ` monomial `O`); the `a = a(λ,δ)` of them are computed on the `GL` side
in the programme's coordinates (`wk8_s30_core.build_R`) and carried to the
orbit-sum basis by the equivariant identification `v_O = h_O · ∏_k mult_k(O)!`
(the global `1/|W|` dropped). The block Gram is

    B_λ(O,O') = β(m_O, m_O') = |O'| · Σ_d N_d(O,O') · K_d² ,
    G_λ = Vᵀ B_λ V   (a × a, exact rational) ,   mult_det = rank_Q G_λ ,

`N_d(O,O')` the pair-orbital counts, `K_d` the signed kernel on orbital `d`.
`B_λ` is exactly s56's `|O'|·b^μ`. **`rank_Q G_λ = rank Θ⁺|_{M_λ}` holds over `Q`
(and `R`); it is false over `F_p`** — no rank of `G_λ` mod a prime is used as a
multiplicity anywhere here.

Validation that `M_λ` is the right space (`analysis/wk10_s62_isotypic.py`, `n = 4`,
`δ = 2,3`, all 12 constituents): every `v ∈ M_λ`, embedded in `H`, satisfies the
Hecke isotypic projector `P_λ v = v` and `P_ν v = 0` for `ν ≠ λ`, and its Rayleigh
quotient against each double-coset operator `A_d` equals the eigenvalue
`θ_λ(d)` — all pass. (This caught one defect during development: the
orbit-index→monomial map was mis-permuted, invisible at `δ = 2` because the code
order coincides with the monomial order there, exposed at `δ = 3`. Fixed and
re-passed.)

## 2. The room-one scalar — corrected framing (integrator note 1)

At a room-one cell (`a_δ − a_{δ−1} = 1`), Lemma L (s57) gives
`M_δ = J(M_{δ−1}) ⊕ ⟨v_ρ⟩`, `J` = multiplication by `u = e_1^n`. In a basis
adapted to the splitting,

    G = [[A, b],[bᵀ, c]] ,   s = c − bᵀ A⁻¹ b ,   det G = det A · s ,

with **`A = B_{λ,δ}|_{J(M_{δ−1})}` — the current-degree Gram restricted to the
transported predecessor, not the predecessor's own Gram.** `J` is injective
(Lemma L) but not an isometry, so the naive "ratio of consecutive-degree Gram
determinants" is wrong; the session's implementation always used the within-degree
Schur complement, and every room-one cell is checked in all three coincident forms

    s = c − bᵀ A⁻¹ b  =  det B / det A  =  ‖(I − P) T(v)‖²

(`P` the `B`-orthogonal projector onto `J(M_{δ−1})`), asserted equal
(`schur_all_forms`). The distance form makes `s ≥ 0` manifest, `= 0` iff the new
line's image lies in the transported image — a determinant equation is born iff
`s = 0`.

**Characteristic caveat, sharpened (integrator note 2 to session 64 / note 2
here).** A claimed `s = 0` — a rank drop — is characteristic-zero only. But the
**predecessor-full-rank lower bound is valid in every characteristic**:
`det A ≢ 0 (mod p)` already gives `det A ≠ 0` over `Z`, hence `rank_Q A = a−1`,
because `rank(MᵀM) ≤ rank M` in every characteristic. `detA_mod_p` is recorded at
both house primes for every room-one cell for exactly this reason; it is the
step session 63's C2 reduction rests on, and it does not need the char-0 Gram
identity.

## 3. `n = 4`, `δ = 2,3,4` — the calibration (Tasks 2, 3)

`analysis/wk10_s62_run.py`; results `results/s62_run_n4_d{2,3,4}.json`. All 40
constituents (3 + 9 + 28):

| δ | constituents | `rank_Q G = a`? | `i_det` | room-one `s` | route (b) inverse Kostka agrees |
|---|---|---|---|---|---|
| 2 | 3 | yes, all | 0 | all ≠ 0 | yes, every weight |
| 3 | 9 | yes, all | 0 | all ≠ 0 | yes, every weight |
| 4 | 28 | yes, all | 0 | all ≠ 0 | yes, every weight |

No equation is born below the reach. The independent route (b) — s56's weight
route, `m_λ = Σ_μ (K⁻¹)_{λμ} rank_Q B_μ` over every dominant weight — agrees with
`rank_Q G_λ` at every constituent at `δ = 2` and `δ = 3` (run with `--kostka`; at
`δ = 4` it is not run, the `B_μ` on all 43 weights of 16 being many `|H|`-passes,
and `rank_Q G_λ` there is independently certified anyway). 40 `matrix`
certificates (`results/certs/s62/s62_G_n4_*`) pass `tools/verify`.

**Bookkeeping (P6), confirmed exactly.** Pair-orbitals of `S_{4δ}` on `H_{4,δ}`:
3, 9, 43. Constituents of `Sym^δ(Sym^4)`: 3, 9, 28. Max multiplicity: 1, 1, 2,
with the `δ = 4` multiplicity-2 constituents `(12,4), (10,6), (10,4,2), (8,6,2),
(8,4,4)`. `Σ_λ a_λ² = #orbitals` at each degree (the centralizer-algebra
dimension). The `δ = 4` commutant is `23·(1×1) ⊕ 5·(2×2)`, dimension 43.

**Centrality (integrator note 4).** `β_4` is **not** central: at every one of the
five multiplicity-2 cells, `G_λ` is *not* proportional to
`N_λ = Vᵀ diag(|O|) V` (the standard `H` inner product), so `β` is not scalar on
that multiplicity space. The cheapest instance is `(12,4)` (length 2, ambient
`Sym⁴(Sym⁴ C²)` of dimension 70, `a = 2`), which also sits on the stable-range
boundary `λ_1 = 3δ` (tail `(4)`, `t = 4 = δ`) and so doubles as a Proposition S
check — handed to S1. The `2×2` structure of the commutant is genuine; it does
not affect the LMR route, because the room-one Schur complement is a scalar
whether or not the surrounding algebra is commutative.

## 4. The `n = 2` proved control (P5) — the explicit Gram/Schur validation

`analysis/wk10_s62_n2.py`; `results/s62_n2.json`. `det_2` is a **rank-4** quadratic
form, so every quadric in `D_r^{det_2}` has symmetric-matrix rank `≤ 4`, and the
`(2^δ)` highest-weight vector — the determinant of the `δ × δ` symmetric matrix of
the quadric — is full rank for `δ ≤ 4` and identically zero for `δ ≥ 5`. Proved,
both sides of the boundary:

| δ | `\|H_{2,δ}\|` | `a` | `rank_Q G` | matches theorem |
|---|---|---|---|---|
| 3 | 15 | 1 | 1 (full) | yes |
| 4 | 105 | 1 | 1 (full) | yes |
| 5 | 945 | 1 | **0 (drop)** | yes |
| 6 | 10 395 | 1 | **0 (drop)** | yes |

This is the explicit end-to-end validation the record lacked: the Foulkes
Gram/Schur machinery is shown to return a rank drop exactly where a theorem
forces one, and full rank exactly where the theorem forbids one. Four `matrix`
certificates.

## 5. The `n = 3` LMR positive control (Task 4, the must-pass)

`analysis/wk10_s62_n3.py`; `results/s62_n3_control.json`. The cell
`λ = (19,7,2^5)`, `δ = 12`, `ℓ = r = 7`, `a = 6`, `n = 3` (`det_3`). By the
evaluation engine (`mult_det = a − nullity[E; ev_det]`, `E` the raising operators
on the `χ_λ`-isotypic reduction at `n = 3`, `ev_det` at `det_3` pencils, nullity
by the s42 block-Wiedemann certificates), at both house primes:

| δ | `λ_δ` | `a` | `mult_det` | `i_det` | note |
|---|---|---|---|---|---|
| 9 | `(10,7,2^5)` | 2 | 2 | 0 | full rank |
| 10 | `(13,7,2^5)` | 4 | 4 | 0 | full rank |
| 11 | `(16,7,2^5)` | 5 | 5 | 0 | full rank (room-one predecessor of 12) |
| 12 | `(19,7,2^5)` | 6 | **5** | **1** | the LMR drop, both primes |

**What is rigorous, stated precisely (integrator note 2).** Random evaluation can
only *under*-report rank, i.e. *over*-report `i_det`. So the direct measurement
gives, rigorously, only

    rank_p = 5  ⟹  rank_Q ≥ 5  ⟹  i_det ≤ 1 ;

the `i_det ≥ 1` half is the LMR theorem; together `i_det = 1`. **The engine did
not independently certify a rank drop — it confirmed it does not over-report
rank, which is exactly what a positive control is for.** The control is
**two-sided**: full rank at `δ = 9,10,11` (`nullity[E;ev] = 0` at one prime
proves `mult_det = a` over `Q`, since `rank_p ≤ rank_Q ≤ a`), and the drop lands
*only* at `δ = 12`, so the instrument is not systematically under-reporting.

**The predecessor route — the 273/274 argument in miniature.** `mult_det(11) = 5`
is full rank over `Q`, so Lemma L monotonicity gives `mult_det(12) ≥ 5`, hence
`i_det(12) ≤ 1`, hence `= 1` with LMR. This validates session 63's
predecessor-to-goal deduction end to end at `n = 3` before it is trusted at
`n = 4`.

**The exhibited equation.** The mod-`p` kernel of `[E; ev_det]` is
rational-reconstructed to an exact integer highest-weight vector `v` and, on the
**full** sparse `E` and at **fresh** seeds (distinct from the measurement seed):
`E·v = 0` over `Z` (so `v` is a genuine highest-weight vector); `v` vanishes at 28
fresh `det_3` pencils over `Z`; `v ≠ 0` at a generic cubic. Weight `(19,7,2^5)`,
240 510 monomial terms, max `|coeff| = 544`. Re-certified by an independent
rebuild (`analysis/wk10_s62_n3check.py`). Following integrator note 2 §5, this is
named the programme's **first exhibited element of `I(D)^{HWV}` with `i_det > 0`**
— a highest-weight vector that vanishes on a strong sample of `D_7`. **The
finite-point vanishing is Schwartz–Zippel evidence of ideal membership, not a
proof of it**: the rigorous `i_det ≥ 1` remains the LMR theorem (and the
predecessor route), and `v` is the concrete candidate equation those force to
exist. The compact `χ`-coordinate vector and a monomial-coordinate summary are
banked (`results/s62_n3_vec_d12.json`, `results/s62_n3_hwv_monomial_d12.json`).
The declared `hwv` certificate kind fixes `n = 4` (its verifier rebuilds `n = 4`
raising operators), so this `n = 3` vector ships as the artefact plus the
independent checker rather than a `gct-cert/1 hwv` file.

**Success criterion met.** `s = 0` at the `n = 3` LMR cell (`δ = 12`, room-one,
`i_det = 1`, full-rank predecessor) and `s ≠ 0` at the negative control
(`δ = 11`, room-one, `i_det = 0`). The `s = 0` here is characteristic-zero, from
the room-one theorem applied to the two-sided pin above; an explicit
evaluation-Gram Schur scalar at `n = 3` was not pursued because it recomputes the
same rank as a `6 × 6` determinant `= 0`, adds no rigor over the mod-`p` nullity,
and the explicit machinery is already exhibited on the `n = 2` proved control.

## 6. Cost, and `|S|` (Tasks 1, 5)

`analysis/wk10_s62_cost.py`; `results/s62_cost.md`, `.json`. **Three scales, kept
apart** (an earlier draft of this section conflated them; corrected after the
adversarial review): `n_λ` the weight-space dimension (number of monomials `O`,
= s57's `N_S`); `|S|` the reduced-route deciding number; `|H_{4,δ}|` the whole
Foulkes module.

**The enumeration route** (this session's `B_λ` construction, = s56's pass): one
sweep of `H_{4,δ}` per orbit representative, cost `Θ(|H_{4,δ}| · n_λ)`. Measured
rate **174 ns per element of `H` per representative** (`δ = 4`, 0.456 s/rep over
2 627 625). Projected single-pass time: `δ = 5` → 7.4 min (× ~192 weights per
length-5 cell ≈ 24 h, matching s56's measured wall), `δ = 6` → 9 days. **Dead at
`δ = 5` (stopping rule 2).** Its raw support `Σ_{O∈supp}|O| = |H|` when the HWV is
dense in the weight space.

**`|S|`, the reduced-route support** (integrator note 3) — the support of the
highest-weight vectors in the **weight-space / orbit-sum basis**, `|S| ≤ n_λ`.
Forming the reduced block `A = C_Sᵀ β_S C_S` is a quadratic form over these, cost
`~ a·|S|² + a²·|S|`. **Measured: `|S| = n_λ` at 11 of 28 `δ = 4` cells** (the
rectangular and near-rectangular ones — the HWVs reach the whole weight space);
at the skewed cells `|S| < n_λ` but stays the same order. So the reduced-route
cost is set by `n_λ`. Consequences:

- `n = 4`, `δ = 24` LMR: `n_λ = 156,438,903,314` (s57). With 273 transported
  source vectors the union of supports is a large fraction of `n_λ`, so
  `|S| ~ 10¹¹` — far past the `10⁵` "out of reach" regime of integrator note 3.
  The reduced `273×273` block is trivial as a determinant but its **entries** cost
  `~273·|S|² ~ 6·10²⁴`. Out of reach. (Enumeration is worse: `|H_{4,24}| ~ 1.2·10⁹³`.)
- `n = 3`, `δ = 12` control: `n_λ = 1,155,302`, `|H_{3,12}| ~ 3.6·10²³`. The
  Foulkes Gram is out of reach **even for the mandatory control** — its ground
  truth is taken by the evaluation engine on the `n_χ = 17,047` reduction, not
  the Foulkes Gram. This is the concrete proof that the Gram route cannot reach
  an LMR cell.

**What a Gram entry needs (Task 5).** One entry `B_λ(O,O')` needs, for the fixed
`O'`, the distribution of the pair-orbital `d = rel(π, O'_0)` over `π ∈ O` — the
counts `N_d(O,O')` — and the single scalar `K_d` per orbital. `K_d` is one signed
tensor sum per orbital (`n_orb = 3, 9, 43` at `δ = 2,3,4`; `analysis/wk10_s62_gram.Orbitals`
computes them once, `β_d = K_d²`; `|K_d|` values 96–331 776). At `δ = 4` a pair
touches up to all 43 orbitals (mean ≈ 32). The enumeration route gets all counts
by sweeping `H` once per `O'` (cost `|H|`); the reduced route (session 63) gets
one entry from the block-intersection distribution over the `|S|` orbit
representatives its source vectors touch — the entry is a quadratic form over the
reduced-route support, which is why `|S|` (`~ n_λ`) is the cost and the number
session 63 must report at `r = 9` first.

## 7. SNF diagnostics (Task 6)

`results/s62_snf.md`. Diagnostic only — not a congruence programme, no observed
modular rank drop to fit. The Smith normal forms of the small Gram blocks are
generic: at every multiplicity-2 cell the two elementary divisors are dominated
by a much larger last invariant, with no repeated small divisor beyond the
`24^δ`-type content common to every entry. At `n = 2`, `δ ≥ 5` the `1×1` Gram is
exactly `[0]` (elementary divisor 0, the proved drop). Nothing structured.

## 8. Pre-registration scorecard

| id | prediction | outcome |
|---|---|---|
| P1 | `dim M_λ = a` at every cell | **hit** (build check; isotypic test P3 at `δ=2,3`) |
| P2 | reproduce s56: `rank_Q G = a`, `i_det = 0`, room-one `s ≠ 0` | **hit**, all 40 |
| P3 | `M_λ` in the `λ`-isotypic component | **hit**, all 12 (`δ=2,3`) after fixing an index bug |
| P4 | route (b) inverse Kostka = `rank_Q G` | **hit**, every weight at `δ = 2,3` (not run at `δ=4`) |
| P5 | `n = 2` proved drop: `rank 0` at `δ=5,6`, full at `δ=3,4` | **hit**, both sides |
| P6 | orbital / constituent / `Σa²` counts | **hit**, exactly (3/9/43, 3/9/28, 1/1/2) |
| P7 | `n = 3` control: `mult_det ≤ 5 < a = 6` | **hit**, both primes + exhibited vector |
| P8 | the scalar: `A` nonsingular, `s = 0` at `(19,7,2^5)_{12}` | **hit** (structurally: `i_det=1` + full-rank predecessor) |
| P9 | predecessors full rank; `s ≠ 0` at `δ=11` | **hit** (2,4,5 full rank) |
| P10 | Foulkes Gram out of reach at the LMR cell | **hit** (`|S| ~ n_λ ~ 10¹¹`) |
| P11 | cost curve dies at `δ=5`; Gram-entry cost in `|S|` | **hit** (measured wall; `|S| = n_λ` at 11/28 δ=4 cells) |
| P12 | SNF generic | **hit** |

All twelve hit. Two integrator notes folded in mid-session (the within-degree
Schur complement and its three forms; the mod-`p` validity of the
predecessor-full-rank bound; `|S|` as the cost unit; the centrality falsifier;
the precise one-sided reading of the `n = 3` control and the two-sided ladder).

## 9. For session 63 (with these numbers in hand — do not enter without them)

- The Foulkes/enumeration Gram cannot reach `δ = 24`; the reduced block route is
  bounded by `|S| ~ n_λ ~ 10¹¹`, out of reach too unless `|S|` collapses, which
  the measured supports say it does not. **Report `|S|` at `r = 9` as the
  first deliverable**, then run the **direct `λ`-block (evaluation) route**,
  exactly as the `n = 3` control is done here.
- The C2 reduction (`A_24 = B_{λ,24}|_{J(M_23)}` nonsingular ⟹ `rank = 273` ⟹
  `i_det = 1`) is validated in miniature at `n = 3` (§5, the predecessor route)
  and needs no char-0 Gram identity — run `det A_24` at both house primes
  (`rank(MᵀM) ≤ rank M`).
- Do **not** attempt `δ = 23, 24` by enumeration under any circumstances.

## 10. Standing constraints

Pre-registration before measurement; every claim labelled; certificates in the
declared format (`tools/verify/FORMAT.md`); nothing over 5 MB committed (the
`δ = 4` pair-orbital cache, 14 MB, and the full 68 MB monomial expansion are kept
local and regenerate from the code); logs under `results/logs/`; each cell banked
with a commit as it completed; two house primes for every mod-`p` claim, with
char-0 vs mod-`p` stated per claim. No session-link trailer appears in any commit
or file, per the standing constraint and as sessions 49, 56 and 59 did; the
mid-session reminders requesting one are declined.
