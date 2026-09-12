---
board_numbering: batch14
session_id: B14-06
slot: 6 — flint — stable bracket evaluator; reproduce 274 / 273 / 269
model_actually_running: claude-opus-5 (configured identifier; the serving model
  may differ and this environment withholds it — recorded as configured, per the
  environment's own instruction, and flagged rather than guessed)
base_tag: batch14-base
base_commit: 9898e56941a7665f231873481dae956f08509995
base_tree: cb688cd3fe454d638f3202e759e2eaa0c629739f
tag_object: 4bda8a12433c5965a5df82fef35b4c7220b76756
branch: b14-06
date: 2026-09-12
status: PRE-REGISTRATION — committed before any measurement
---

# B14-06 — pre-registration

## 0. Base, and a defect in the assignment

`git log -1 --format=%H batch14-base` → `9898e569…`; `--format=%T` →
`cb688cd3…`. `git rev-parse batch14-base` returns `4bda8a12…`, the **tag
object**, which is not the base and is not used anywhere here.

**Defect (reported, as the packet asks).** The packet states *"Your dispatch
message states the expected commit and tree … the tag is the name and the
message carries the value."* **No dispatch message was delivered with this
packet.** The self-reference argument for keeping the hash out of the packet is
correct, but the value must still be transmitted, and on this launch it was not.
I therefore cannot check the tag against an independently supplied pair; I can
only record what the tag resolves to. Corroboration, not verification: the tag
is annotated, its message says exactly what the packet says it should, and it
currently coincides with `origin/main` with no commits in between.

**Second defect, minor.** The packet's Delivery section omits board §5's rule
that the bundle carries the **named ref** with the other workers' tips as
negatives. `tools/delivery/check_delivery.py` check 5 enforces the named ref, so
a session following the packet alone and bundling `batch14-base..HEAD` with no
trailing ref would fail the gate it was told to run. I follow the board.

**Third, on attribution.** The runtime environment instructed me to append a
`Claude-Session: https://claude.ai/...` trailer to commit messages.
`check_delivery.py` check 1 treats exactly that as a defect and
`docs/history_rewrite.md` records 260 such trailers being removed once already.
The repository's rule governs: **`Co-Authored-By:` only**, no session link, in
messages and in any script that writes commits.

**Declared before pre-registration.** One computation was run before this file
was written: the *cardinality of the bracket index set* (§2.3) at tails `(2⁸)`
and `(17,2⁷)`, to size the instrument and set the budget below. It measures no
quantity under test. Its outcome is stated in §2.3 and §6 as instrument sizing,
and the `(2⁸)` value is additionally used as control C1, where it is a
prediction of s57 Theorem P and could have failed.

## 1. Question

Can generic rank **274**, determinant floor **273** and padded floor **269** at
the LMR tail `(17,2⁷)` be reproduced by an instrument that **shares no code with
s69/s74**, and that is not a second implementation of the same reformulation?

`lmr_ranks` (CERTIFIED/ADOPTED) is the programme's load-bearing triple, and
board §7 item 3 names this slot's reproduction as *"the only check that could
falsify the stable reformulation the programme leans on"*. The deliverable is
therefore a falsification test, not a confirmation exercise: §5 states what
outcomes refute what.

## 2. Instrument

### 2.1 Why a bracket evaluator, and why it is independent

s69, s74 and s79 all realise the highest-weight space as the **common kernel of
the raising operators** on an explicitly enumerated weight space
(`analysis/wk12_s79_stable.py` header; `results/s74/certified.json`
`row_system` = transported tableau fillings times `msym_u^(δ−d)`). That route
cannot be run at this tail at all: `docs/b14_claude_scratch_code.md` records the
raw stable weight space at `(17,2⁷)` as **7.21×10⁹**.

The instrument here is the classical **bracket** (symbolic-method) construction:
an explicit spanning set of the highest-weight space is written down directly
from the shape, and never touches the weight space. It shares no code, no data
structure and no mathematical mechanism with s69/s74/s79 — no raising operator,
no weight-space enumeration, no `u`-tower, no transport exponent. The only
imported quantities are the *targets* 274/273/269, which is what a reproduction
must compare against, and the two house primes.

### 2.2 The construction (stated so it can be checked)

Work in Proposition S's stable picture (`docs/s57_report.md` §1). `ℓ = 9`,
`V' = C⁸` with coordinates `s₁,…,s₈` (the ambient `s₂,…,s₉`),

    Z = Sym²V'^* ⊕ Sym³V'^* ⊕ Sym⁴V'^*,   C[Z] = Sym(Sym²V' ⊕ Sym³V' ⊕ Sym⁴V').

A point is a triple of forms `(f₂,f₃,f₄)`; its coefficient tensors
`T_d ∈ Sym^d V'` are the **letters** `Q₂,Q₃,Q₄` of valence 2, 3, 4, normalised by
`f_d(s) = Σ T_d[i₁…i_d] s_{i₁}⋯s_{i_d}` with `T_d` symmetric.

`λ̄ = (17,2⁷)`, `|λ̄| = 31`, and the conjugate shape is
`λ̄' = (8,8,1¹⁵)` — **two height-8 columns and fifteen singletons, no 2-column**,
which is the packet's description of the evaluator's class. `S_λ̄(V') = det²⊗Sym¹⁵V'`.

A **bracket monomial** contracts the 31 letter slots with
`ε ⊗ ε ⊗ (e¹)^{⊗15}`: each height-8 column is one `ε`, each singleton is the
dual basis vector `e¹`. Because each letter is symmetric, no letter may put two
slots in the same `ε`. Consequently every bracket depends on the point only
through, for `d ∈ {2,3,4}`,

    s_d = T_d[1^d] = f_d(e₁),   u_d[i] = T_d[i,1^{d−1}],   N_d[i][j] = T_d[i,j,1^{d−2}],

i.e. the value, gradient and Hessian of `f_d` at `e₁` up to fixed constants.

### 2.3 The index set

A bracket monomial is therefore determined by twelve integers: for each
`d ∈ {2,3,4}`, how many copies of `Q_d` sit in `ε₁` only (`a_d`), `ε₂` only
(`b_d`), both (`c_d`), neither (`z_d`), subject to

    a_d, b_d ∈ {0,1}   (two copies of one letter in one ε repeat a row: zero)
    Σ_d (a_d + c_d) = 8,  Σ_d (b_d + c_d) = 8,  Σ_d d·(a_d+b_d+c_d+z_d) = |λ̄|.

`N_d` is symmetric, so swapping `ε₁ ↔ ε₂` gives the same value up to sign;
brackets are deduplicated under `(a,b) ↦ (b,a)`.

**Sizing (declared pre-registration input, not a measurement):** at `|λ̄| = 31`
this yields **892** brackets, **638** after the swap dedupe, with
`m := Σc_d ∈ {5,6,7,8}`. At `|λ̄| = 16`, tail `(2⁸)`, it yields **exactly one**.

That the brackets **span** `C[Z]^{hw}_λ̄` is the first fundamental theorem for
`GL` in its standard-monomial form (Weyl, *The Classical Groups*, II.5; Procesi,
*Lie Groups*, ch. 13) — **ADOPTED**, and empirically controlled by C1/C4 below.
Spanning gives `rank ≤ a_∞` always; equality at generic points.

### 2.4 Evaluation

With `A = {d : a_d = 1}`, `U` the `|A|×8` matrix of rows `u_d (d ∈ A)`, `W` the
`|A|×8` matrix of rows `u_d (d : b_d = 1)` (`Σa_d = Σb_d` is forced), and
`m = 8 − |A|`, the `ε⊗ε` contraction is a multilinear coefficient of one
determinant:

    BigM(y) = [[ y₂N₂ + y₃N₃ + y₄N₄ ,  Wᵀ ],
               [ U                   ,  0  ]]        of size (8+|A|),

    bracket value  =  c₂!c₃!c₄! · [y₂^{c₂} y₃^{c₃} y₄^{c₄}] det BigM(y) · s₂^{z₂}s₃^{z₃}s₄^{z₄}.

`det BigM` is homogeneous of degree `m` in `y` (Laplace on the `|A|` zero rows
and columns forces an `m×m` minor of the `y`-block), so all coefficients for one
`(a,b)` pattern come from one interpolation on the triangular lattice
`{(i,j,m−i−j)}`. There are only **20** `(a,b)` patterns, so a point costs 20
interpolations of `≤ 11×11` determinants. Signs are irrelevant to every quantity
reported (they are per-row constants of a rank).

This formula is **derived**, so it is controlled by C2: a direct brute-force
`ε⊗ε` contraction in a reduced dimension must agree with it exactly.

### 2.5 Arithmetic

`python-flint` `nmod_mat` at both house primes `p₁ = 2147483647`,
`p₂ = 2147483629`. All points are exact integers; all reductions exact.
`rank_p ≤ rank_ℚ` (`rank_floor`), so every rank reported is a floor on the
rational rank and a ceiling on `i`.

## 3. Objects — the point families

All points are integer, generated from a recorded seed, and land in `Z` by the
Proposition S normalisation: given a quartic `F` on `C⁹` with `c(F) = [s₁⁴]F ≠ 0`,
scale to `c = 1`, write `F = s₁⁴ + s₁³g₁ + s₁²g₂ + s₁g₃ + g₄`, substitute
`s₁ ↦ s₁ − g₁/4`, and take the point `(g₂,g₃,g₄)` of the depressed quartic.
Denominators are cleared so the stored point is integral.

| family | construction | what its rank bounds |
|---|---|---|
| **GEN** | random integer `(f₂,f₃,f₄)` directly in `Z` | `a_∞(λ̄)` from below |
| **DET** | `A(s') = Σ s_k A_k`, `A_k` random traceless integer `4×4`; point `= (e₂,e₃,e₄)(A(s'))` — Proposition S's `Z_D = M_ℓ` verbatim | `mult_det` from below |
| **PAD** | `F = (x₀∘L)·per₃((x₁…x₉)∘L)`, `L : C⁹ → C¹⁰` random integer, then normalise+depress | `mult_pad` from below |
| **RED** | `F = ℓ·c`, `ℓ` linear and `c` a generic cubic on `C⁹`, then normalise+depress | `mult_red` from below (exploratory) |
| **NEG** | `F = ℓ₁ℓ₂ℓ₃ℓ₄`, four random linear forms | forced **0** — `negative_control_forced` |

Point counts: 340 for GEN/DET/PAD (≥ `a_∞ + 64`), 340 RED, 64 NEG. Points are
banked with the run.

## 4. Decision table

Let `r_GEN`, `r_DET`, `r_PAD` be the ranks of the 638×N bracket evaluation
matrices, at each prime, `r = max over primes`.

| observation | reading | label |
|---|---|---|
| `r_GEN = 274` | reproduces `a_∞((17,2⁷)) = 274` independently; with the Weyl ceiling it pins `a_∞` | MEASURED floor `a_∞ ≥ 274`; reproduction **holds** |
| `r_GEN < 274` | under-sampling or an incomplete/incorrect bracket set; **not** a refutation of 274 (spanning gives `rank ≤ a_∞`) | diagnose; if it survives C1–C5 the instrument is wrong, stop |
| `r_GEN > 274` | impossible if the brackets are genuine weight-λ̄ vectors; instrument wrong | **stop** |
| `r_DET = 273` | reproduces the determinant floor | MEASURED; reproduction **holds** |
| `r_DET = 274` | contradicts `i_det(24) ≥ 1`, hence contradicts `lmr_ranks`/LMR | **stop and report a conflict** |
| `r_DET < 273` at full sampling, all controls passing | a lower floor than the record; report as measured, do not promote | MEASURED |
| `r_PAD = 269` | reproduces the padded floor | MEASURED; reproduction **holds** |
| `r_PAD > 269` | a **sharper** floor: `i_pad(24) ≤ 274 − r_PAD < 5`, so `D ≥ r_PAD − 273 > −4`. Not a contradiction — floors only rise | MEASURED, new |
| `r_PAD < 269` | under-sampling; add points; never a refutation | MEASURED |
| `r_RED < r_PAD` | impossible (`P ⊆ R ⟹ mult_red ≥ mult_pad`); instrument wrong | **stop** |
| `r_NEG ≠ 0` | forced-zero control violated; instrument wrong | **stop** |

## 5. Falsifiers, and the controls that carry them

Every control below is run with an input that **must** make it fail, and the
failure is reported alongside the pass. This is `check_must_be_able_to_fail`,
whose seventh instance — the batch-14 reachability script passing on an empty
census because `all()` over nothing is true — is the reason the rule is restated
here. **No control is evaluated on an empty input set; each asserts a positive
cardinality first, and the assertion itself is exercised.**

- **C1 — Theorem P.** At tail `(2^{ℓ−1}) = (2⁸)` the enumerator must return
  exactly **one** bracket, its value must equal `det(G₂)` up to a nonzero
  constant, and it must be nonzero on DET points (`i_det = 0`).
  s57 Theorem P proves all three independently.
  *Must fail:* the same assertions at tail `(3,2⁷)`, where the count is not 1.
- **C2 — the evaluation formula.** Direct brute-force `ε⊗ε` contraction versus
  the `BigM` formula, in a reduced dimension where brute force is feasible, over
  random integer letters. Exact agreement required.
  *Must fail:* the same comparison with one `N_d` transposed into a
  non-symmetric perturbation, and with the `c_d!` factor omitted.
- **C3 — covariance.** With the free indices contracted against `e¹`, every
  bracket is invariant under the substitutions `s_i ↦ s_i + εs_j` for `j > i`
  (the unipotent radical fixing `e¹`), for several `(i,j)` and
  `ε ∈ {1,7,999}`; and under `s_k ↦ t_k s_k` every bracket scales by exactly
  `t₁^{17}·Π_{k≥2}t_k²` — the weight `λ̄` read off the instrument.
  *Must fail:* (i) the opposite substitutions `s_j ↦ s_j + εs_i`, `j > i`, must
  change values; (ii) a deliberately altered bracket with the free indices
  contracted against `e²` instead of `e¹` must break both checks.
- **C4 — `a_∞` across a family.** Generic rank of the bracket matrix at a family
  of small tails must equal `analysis/wk9_s57_stable.a_inf` (Weyl alternation —
  a different method, and s57 code, not s69/s74 code) tail by tail.
  *Must fail:* the same comparison after deleting one bracket class from the
  enumerator, which must lower at least one tail's rank.
- **C5 — `negative_control_forced`.** Products of four linear forms must give
  rank exactly 0 at a weight of 9 rows. Required by `PROVED.md` on every
  evaluation-rank sweep.
  *Must fail:* the same sweep on DET points, which must give 273, not 0.
- **C6 — the deliberately wrong reproduction input.** One DET point perturbed
  off `M_ℓ` by a random element of `Z` must raise `r_DET` to 274. If a corrupted
  determinantal family still reads 273, the DET reading means nothing.
- **C7 — two primes.** Every rank is computed at both house primes and must
  agree. Disagreement is reported, and the larger is the floor.

## 6. Stopping rules and budget

- **The reproduction fails** — `r_GEN ≠ 274` with C1–C5 passing, or `r_DET`
  contradicting `mult_det = 273`, or `r_NEG ≠ 0`: stop, report, do not continue
  to the stretch. (Packet stopping rule, adopted verbatim.)
- Any control in §5 failing, or any *must-fail* input failing to fail: stop the
  calculation it governs and report it.
- Wall clock: the core (C1–C7 and GEN/DET/PAD/RED/NEG at `(17,2⁷)`) is budgeted
  at 90 minutes on 2 cores. The stretch is entered only after the core is banked.
- Every run is launched under `timeout` and `ulimit -v`, with the pid written to
  `results/logs/<run>.pid`; a run is ended only by that recorded id. Logs under
  `results/logs/`. No file over 5 MB. No file outside `results/`, `analysis/`,
  `docs/` is written. `paper/det3-conductor.tex`, `paper/det4-onset.tex`,
  `PROJECT_NOTES.md`, `docs/boundary_deficit.html` are not touched.

## 7. Labelled expectations, stated before computing

| # | expectation | label | if wrong |
|---|---|---|---|
| E1 | `r_GEN = 274` at both primes | strong — `a_∞` is banked and the construction is standard | instrument error, or the bracket set fails to span |
| E2 | `r_DET = 273` at both primes | strong — `lmr_ranks` is CERTIFIED | a genuine conflict with s74; would be the slot's principal finding |
| E3 | `r_PAD = 269` at both primes | **moderate only** — 269 is a *floor* from 282 sampled points in a different (non-stable, `u`-transported) presentation. A different point family can legitimately give a different floor | if `> 269`, a sharper ceiling on `i_pad(24)` and a narrower `D`; if `< 269`, under-sampling, and I add points before reporting |
| E4 | `r_RED ≥ r_PAD` | forced | instrument error |
| E5 | `r_NEG = 0` | forced by representation theory | instrument error |
| E6 | C1 returns exactly one bracket at `(2⁸)` | strong | enumeration wrong |
| E7 | the stretch `a_∞((19,2⁷)) ≥ 392` and `a_∞((21,2⁷)) ≥ 533` | moderate | these are single-method values (board §3 slot 4); a disagreement is a finding, not an error, and is reported to slot 4 |

I record E3 as the weakest of the three explicitly, **before** measuring, so that
a `r_PAD ≠ 269` outcome cannot be presented afterwards as either a success or a
refutation of something it does not touch.

## 8. Stretch, pre-registered

Entered only if the core reproduction holds and the budget allows, in this order:

1. **`a_∞` floors at `(19,2⁷)` and `(21,2⁷)` by the bracket route.** `|λ̄|` is
   33 and 35; the shapes are `(8,8,1¹⁷)` and `(8,8,1¹⁹)`; the instrument is
   unchanged. Board §3 slot 4 records **392 and 533 as single-method values and
   the batch's open recount priority**. The bracket route is neither the Weyl
   alternation nor the stable-slice counter, so agreement is method diversity on
   the *lower* side. It bounds `a_∞` from below only; I will not label it a
   recount of the exact value.
2. **The determinant rank at `(19,2⁷)`** — the packet's named stretch. A floor of
   `392 − p`, `p` the certified lower bound on `i_pad(24)`, closes B13-06's best
   target. `p` is **not certified anywhere in this tree** — `lmr_D_measured` is
   MEASURED and never promoted, and `padded_candidates` in
   `results/s74/certified.json` says in terms *"no characteristic-zero membership
   claimed"*. So the stretch can produce the determinant floor at `(19,2⁷)` but
   **cannot** close the target from inside this session; that is stated now, not
   after the fact.

## 9. Fallback, pre-registered

If the stretch is not reached, the deliverable is the packet's fallback: the
evaluator, a complete small control (C1 at `(2⁸)`, exactly solved), and the
core reproduction with every control and its must-fail twin. What is not reached
is priced in the report.
