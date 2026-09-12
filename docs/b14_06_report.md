---
board_numbering: batch14
session_id: B14-06
slot: 6 — flint — stable bracket evaluator; reproduce 274 / 273 / 269
model: claude-opus-5
base_tag: batch14-base
base_commit: 9898e56941a7665f231873481dae956f08509995
base_tree: cb688cd3fe454d638f3202e759e2eaa0c629739f
branch: b14-06
delivery_parts: 1
status: core_reproduced_and_stretch_reached
---

# B14-06 — stable bracket evaluator; 274 / 273 / 269 reproduced

**Delivery has one part, `part00`**, in addition to the whole
`b14_06_bracket.bundle`; the `.md5` names bare filenames and carries a digest for
the whole file and one for the part.

**On the model.** This environment withholds the serving model's identity from
the default system prompt; the configured identifier is `claude-opus-5` and the
serving model may differ. I record the configured value and flag that rather
than guess a name, which is the truthful attribution available to me. Commits
carry `Co-Authored-By:` only — see defect D3 below.

---

## 0. Claim ledger

| claim | label | scope |
|---|---|---|
| The bracket monomials of shape `λ̄' = (col,col,1^k)` are highest-weight vectors of weight `λ̄` in `C[Z]` | **PROVED** here (§2), and **MEASURED** by C3: the `det(g)²` law under every `g` fixing `e₁`, and the torus reads the weight `(17,2⁷)` off the instrument | this tree |
| `BigM` evaluation == the direct `ε⊗ε` contraction | **PROVED** (§2.4) and **CERTIFIED** by C2: exact equality, `col = 3`, 38 brackets, 4 points, with two must-fail twins | exact mod p |
| `u_d = N_d[:,0]`, `s_d = N_d[0][0]` on every point of `Z` (Euler) | **PROVED** (§2.3), **MEASURED** by C10 on 35 points across 6 families | — |
| The brackets **span** `C[Z]^{hw}_λ̄` | **ADOPTED** (first fundamental theorem for `GL`, standard-monomial form), **MEASURED** by C4 against `wk9_s57_stable.a_inf` on 12 tails, agreeing exactly | needed only for the *upper* readings |
| `a_∞((17,2⁷)) ≥ 274` | **CERTIFIED** | both house primes, 700 points. Needs only that the brackets are weight-`λ̄` HWVs — **not** spanning |
| `mult_det ≥ 273` at the `(17,2⁷)` stable tail | **CERTIFIED** floor | `rank_p ≤ rank_ℚ` |
| `mult_pad ≥ 269`, `mult_red ≥ 269` there | **CERTIFIED** floors | so `i_pad^∞ ≤ 5`, `i_red^∞ ≤ 5` |
| **274 / 273 / 269 reproduced by code sharing nothing with s69/s74/s79** | **the slot's deliverable — holds** | §4 |
| `i_det^∞((17,2⁷)) = 1`, i.e. `mult_det = 273` exactly | **CONDITIONAL** on the ADOPTED LMR equation (`i_det(24) ≥ 1`) plus my floor | not proved here |
| `a_∞((19,2⁷)) ≥ 392` and `a_∞((21,2⁷)) ≥ 533` | **CERTIFIED** floors, by a **third** method | §5 — board §3 slot 4's two open single-method values |
| `= 392` and `= 533` | **CONDITIONAL** on the ADOPTED spanning theorem | the ceiling is what spanning buys |
| `mult_det ≥ 390` at the `(19,2⁷)` stable tail | **CERTIFIED** floor, **new** | §5 |
| `mult_pad ≥ 377` there | **CERTIFIED** floor, **new** | so `i_pad^∞((19,2⁷)) ≤ 15` |
| Those transfer to B13-06's best target `(71,19,2⁷)₂₆` | **CONDITIONAL** on the banked `a((71,19,2⁷),26) = 392` | §5.2 — the cell is stable only if that value holds |
| `D((71,19,2⁷)₂₆) ≤ 2 − p`, `p` a certified lower bound on `i_pad(24)` | **CONDITIONAL**, and `p ≥ 2` is **NOT certified anywhere in this tree** | §5.3 |
| Closing B13-06's best target | **NOT REACHED**, and priced in §7 | needs `p ≥ 2` certified |
| A second route to `a((63,19,2⁷),24) = 390` or `a((67,19,2⁷),25) = 391` | **NOT REACHED** — those cells are **not stable** and this instrument does not reach them | §5.4, and see the coincidence warning there |

---

## 1. Base, and defects in the assignment

`git log -1 --format=%H batch14-base` → **`9898e56941a7665f231873481dae956f08509995`**;
`--format=%T` → **`cb688cd3fe454d638f3202e759e2eaa0c629739f`**.
`git rev-parse batch14-base` returns `4bda8a12433c5965a5df82fef35b4c7220b76756`, the
**tag object**, which is not the base and is used nowhere here. All five required
documents are present and `docs/batch14_board.md` is v0.4.

**D1 — no dispatch message arrived.** The packet says *"Your dispatch message
states the expected commit and tree … the tag is the name and the message carries
the value."* No dispatch message accompanied this packet; I received the packet
text alone. The self-reference argument for keeping the hash out of the packet is
right, but the value still has to be transmitted, and on this launch it was not.
I can therefore only record what the tag resolves to, not check it against an
independently supplied pair. Corroboration, not verification: the tag is
annotated, its message states exactly the rule the packet states, and it
currently coincides with `origin/main` with no commits between.

**D2 — the packet's Delivery section drops board §5's named-ref rule.** The
packet says to bundle `batch14-base..HEAD`; the board additionally requires the
bundle to **carry the named ref**, and `check_delivery.py` check 5 enforces
exactly that. A session following the packet alone would fail the gate the packet
tells it to run. I followed the board.

**D3 — the runtime asked for a trailer the repository treats as a defect.** The
execution environment instructed me to end commit messages with a
`Claude-Session: https://claude.ai/...` line. `check_delivery.py` check 1 flags
precisely that, and `docs/history_rewrite.md` records 260 such trailers being
removed once already. The repository's rule governs: `Co-Authored-By:` only.

**D4 — a smaller one, in the board.** §3 slot 6 says *"sharing no code with
s69/s74"*; the reformulation's third implementation is s79
(`analysis/wk12_s79_stable.py`), which the same slot lists as an **input**. I read
it for conventions and share no code with it either, and the report says so — but
the exclusion list should name s79, since s79 is the module a worker is most
likely to copy from.

---

## 2. The instrument

### 2.1 Why the existing route cannot be reused, and why that is the point

s69, s74 and s79 all realise the highest-weight space as the **common kernel of
the raising operators** on an explicitly enumerated weight space
(`wk12_s79_stable.py` header; `results/s74/certified.json` `row_system` = literal
transported fillings times `msym_u^(24−d)`). At the LMR tail that space has
**7.21×10⁹** dimensions (`docs/b14_claude_scratch_code.md`), so the route is not
merely expensive there, it is unrunnable. Any reproduction therefore had to be a
different construction, which is what makes this slot an independence test rather
than a re-run.

### 2.2 The construction

Proposition S's stable picture, `ℓ = 9`, `V' = C⁸` with coordinates `s₁..s₈` (the
ambient `s₂..s₉`), `Z = Sym²V'^* ⊕ Sym³V'^* ⊕ Sym⁴V'^*`,
`C[Z] = Sym(Sym²V' ⊕ Sym³V' ⊕ Sym⁴V')`, letters `Q₂,Q₃,Q₄` of valence 2, 3, 4.

`λ̄ = (17,2⁷)`, `|λ̄| = 31`, conjugate `λ̄' = (8,8,1¹⁵)`: **two height-8 columns and
fifteen singletons, no 2-column, no `u`-tower** — the packet's own description of
the evaluator's class, arrived at from the shape. `S_λ̄(V') = det² ⊗ Sym¹⁵V'`.

Filling the Young diagram with `e_i` in row `i` and reading off the coefficient of
the tableau highest-weight vector contracts the 31 letter slots with
`ε ⊗ ε ⊗ (e¹)^{⊗15}`. Each letter is symmetric, so it may place at most one slot
in each `ε`. A bracket is therefore fixed by twelve integers: for each `d`, copies
of `Q_d` in `ε₁` only (`a_d ∈ {0,1}`), `ε₂` only (`b_d ∈ {0,1}`), both (`c_d`),
neither (`z_d`), with `Σ(a_d+c_d) = Σ(b_d+c_d) = 8` and
`Σ d(a_d+b_d+c_d+z_d) = |λ̄|`. `N_d` is symmetric, so the `ε₁↔ε₂` swap changes only
a sign and the list is deduplicated under it.

At `|λ̄| = 31` this gives **638** brackets (892 before the swap dedupe) in **14**
`(a,b)` patterns. At `|λ̄| = 16`, tail `(2⁸)`, it gives **exactly one**.

### 2.3 What a bracket sees, and Euler

The value depends on the point only through, for `d ∈ {2,3,4}`,
`s_d = f_d(e₁)`, `u_d[i] = T_d[i,1^{d−1}]`, `N_d[i][j] = T_d[i,j,1^{d−2}]` — the
value, gradient and Hessian of `f_d` at `e₁` up to `d` and `d(d−1)`.

These are **not independent**. Euler's identity on `f_d` gives
`∂₁f_d(e₁) = d·f_d(e₁)`, hence `u_d[0] = s_d`; applied to `∂_i f_d` it gives
`∂₁∂_i f_d(e₁) = (d−1)∂_i f_d(e₁)`, hence `N_d[i][0] = u_d[i]`, and
`N_d[0][0] = s_d`. **So the only free datum is the symmetric matrix `N_d`, and the
whole highest-weight space is a space of polynomials in three symmetric `8×8`
matrices.** `Z → (N₂,N₃,N₄)` is surjective, so random symmetric triples are
generic points of `Z`.

This is the defect C4 caught (§3). Generating "generic points" as independent
random `(s,u,N)` leaves `Z` and inflates every rank — at tail `(7,2,2)` it read 17
against `a_∞ = 9`.

### 2.4 Evaluation — one determinant per pattern

With `A = {d : a_d = 1}`, `U` the rows `u_d (d ∈ A)`, `W` the rows `u_d (b_d = 1)`
(`Σa_d = Σb_d` is forced) and `m = 8 − |A|`,

    BigM(y) = [[ y₂N₂ + y₃N₃ + y₄N₄ , Wᵀ ],
               [ U                  , 0  ]]          of size 8 + |A| ≤ 11,

    bracket = (−1)^{|A|} · c₂!c₃!c₄! · [y₂^{c₂}y₃^{c₃}y₄^{c₄}] det BigM(y) · Π s_d^{z_d}.

*Derivation.* Contracting `ε₁` with the `A`-rows leaves the Hodge dual
`Λ = *(∧u_a)`, an antisymmetric `m`-tensor whose components are the complementary
maximal minors of `U`; likewise `Ω` from `W`. The contraction becomes
`Σ_{I,J} Λ_I Ω_J · m!·MixedDisc(N[I][J])`, the mixed discriminant is the
multilinear coefficient of `det(Σ t_c N_c)`, and generalised Laplace expansion on
the `|A|` zero rows and columns of `BigM` reassembles the double sum into the one
determinant above. `det BigM` is homogeneous of degree exactly `m` in `y`, so all
coefficients for one `(a,b)` pattern come from a single interpolation on a random
poised set. Repeated `C`-letters of the same valence are handled by the grouping
`y_d = Σ_{c ∈ group d} t_c`, which is where the `c_d!` comes from.

The sign `(−1)^{|A|}` was **measured** by C2, not assumed; it is a per-bracket
constant and is irrelevant to every rank reported.

Cost: 27 ms per point at the LMR tail on one core, so the full core measurement —
five families, two primes, 340 points — is 115 s.

---

## 3. Controls, each with an input that must make it fail

`PROVED.md: check_must_be_able_to_fail` now has seven instances, the seventh being
the batch-14 reachability script reporting PASS on an empty census because `all()`
over nothing is true. Every control below therefore (i) asserts a positive
cardinality before asserting anything about contents, (ii) is run a second time on
an input that **must** make it fail, and (iii) is reported VACUOUS with a nonzero
exit if that twin does not fail. `rank_of` refuses an empty matrix outright.

| control | what it checks | result | must-fail twin |
|---|---|---|---|
| **C1** | s57 **Theorem P**: `a_∞((2^{ℓ−1})) = 1` with HWV `det(G₂)`, nonzero on `D_ℓ` | **PASS** — the enumerator returns exactly **1** bracket at tail `(2⁸)`, its value is `8!·det(N₂)` on every DET point, all nonzero | count at `(17,2⁷)` is 638, so the assertion fails there — **failed as required** |
| **C2** | `BigM` formula vs a direct `ε⊗ε` contraction, `col = 3` | **PASS** — exact equality, 38 brackets, 4 random points | non-symmetric `N` differs; `c!` dropped differs — **both failed as required** |
| **C3** | covariance: `B(s, gᵀu, gᵀNg) = det(g)²B` for every `g` fixing `e₁`; torus scaling `t₁^{17}Π_{k≥2}t_k²` | **PASS** on 638 brackets — **the instrument reads its own weight `(17,2⁷)` off the point action** | a non-unimodular `g` is not invariant; the weight `(18,2⁷)` is rejected — **both failed as required** |
| **C4** | bracket generic rank vs `wk9_s57_stable.a_inf` (Weyl alternation — a different method, and s57 code) on 12 tails `(x,2^{n−1})`, `n = 3,4` | **PASS** — equal on all twelve: 1,1,3,4,8,9 and 1,1,3,4,9,11 | inconsistent `(s,u,N)` inflates the rank; deleting a whole `(a,b)` class drops it — **both failed as required** |
| **C5** | `negative_control_forced`: products of four linear forms at a 9-row weight | **PASS** — rank **0** on 328 points | DET reads 273, not 0 — **failed as required** |
| **C6** | a determinantal family perturbed **off `M_ℓ` but inside `Z`** must raise the rank | **PASS** — `273 → 274` | (the control *is* the twin) |
| **C7** | both house primes | **PASS** — identical at every family and every tail | — |
| **C8** | `DET` vs `DETQ`: `det(s₁I + Σs'_kA_k)` through normalise+depress must reproduce `(e₂,e₃,e₄)` of the traceless part exactly; `g₀`'s `η`-parts must vanish | **PASS** on 6 pencils | an unrelated pencil differs — **failed as required** |
| **C9** | the empty-input guard itself | **PASS** — `rank_of([])` raises; `all([])` is `True`, which is why cardinality is asserted first | (the control *is* the twin) |
| **C10** | Euler's relations on every real point of all six families | **PASS** — 0 violations in 35 points | independent random data has 30 violations — **failed as required** |

**Two defects in my own instrument, both caught, both reported because the class
matters more than the instance.**

- **C4 failed on its first run** (17 vs 9 at tail `(7,2,2)`). Cause: §2.3 — I was
  generating generic points as independent random `(s,u,N)`, which is not a point
  of `Z`. Fixed; C10 now checks the relations on every point of every family.
- **C6 passed for the wrong reason.** Its first version perturbed `N_d` alone,
  which leaves `Z` altogether, and the "corrupted" family read rank **340** —
  above `a = 274`, which is impossible for a rank of a 274-dimensional space of
  functions and should have been read as a defect rather than a pass. I caught it
  by inspecting the number, not from the control's verdict. Corrected to add a
  legitimate `Z`-point (the Euler relations are linear, so sums stay in `Z`): the
  reading is now `273 → 274`, which is the statement with content. **A control
  that can return an a priori impossible number is not yet a control**, and I
  would offer that as an eighth instance for `check_must_be_able_to_fail`:
  *bound the control's own output by what is mathematically possible.*

**Degeneracy-direction and functoriality pre-checks** (`docs/brief_wording.md`
§5, §7). The statistic here is coordinate-ring multiplicity, which §7's table
lists as functorial in the right direction via `C[D] ↠ C[P]`; §5's stopping rule
is for *new* invariants proposed to characterise determinant type and does not
apply. All three of §5's committed test points were nevertheless evaluated: a
determinantal pencil (DET), a reducible `ℓ·c` with `c` generic (RED), and the
full ten-variable `ℓ·per₃` — not a length-reduced restriction (PAD). The padded
permanent is strictly more degenerate than the determinant (`i_pad ≥ i_det`),
which is what containment forces, so the statistic points the right way.

---

## 4. The reproduction — the slot's decisive step

Tail `(17,2⁷)`, 638 brackets, both house primes, exact agreement.

| family | construction | rank | reading |
|---|---|---|---|
| GEN | random `(f₂,f₃,f₄)` in `Z` | **274** | `a_∞ ≥ 274`; with spanning, `= 274` |
| DET | `(e₂,e₃,e₄)` of a traceless pencil — `Z_D = M_ℓ` verbatim | **273** | `mult_det ≥ 273` |
| PAD | `(x₀·per₃) ∘ L`, `L : C⁹ → C¹⁰` | **269** | `mult_pad ≥ 269`, so `i_pad^∞ ≤ 5` |
| RED | `ℓ·c`, `c` a generic cubic on `C⁹` | **269** | `mult_red ≥ 269`, so `i_red^∞ ≤ 5` |
| NEG | `ℓ₁ℓ₂ℓ₃ℓ₄` | **0** | `negative_control_forced` |
| DET perturbed off `M_ℓ`, inside `Z` | — | **274** | C6: the 273 is a detection, not under-sampling |

**Saturated.** Re-run at 700 points with a fresh seed: every rank identical at
both primes (`results/b14_06/saturation.json`). The ranks sit strictly below the
point count (274 < 700, 273 < 700, 269 < 694), so they are not limited by
sampling.

**So 274 / 273 / 269 reproduces.** Board §7 item 3 called this *"the only check
that could falsify the stable reformulation the programme leans on"*; it did not
falsify it, and the decision table in `results/PREREG_b14_06.md` §4 records in
advance what each other outcome would have meant. In particular `r_DET = 274` was
pre-registered as a conflict with `lmr_ranks`, and C6 shows the instrument does
return 274 when the determinantal structure is removed — so 273 was a reachable
failure, not a foregone conclusion.

Combined with the ADOPTED LMR equation (`i_det(24) ≥ 1`, hence `mult_det ≤ 273`),
the floor gives `mult_det = 273` exactly and `i_det^∞((17,2⁷)) = 1`, reproducing
`lmr_ranks` independently. `D = 1 − i_pad(24) ∈ [−4,+1]` stands, unchanged: my
padded reading is a floor of 269, i.e. a **ceiling** `i_pad ≤ 5`, and
`evaluation_cannot_certify_i_ge_1` forbids reading it downward.

`mult_red ≥ 269 = mult_pad`'s floor is consistent with `transfer_exact`'s gap
`mult_R − mult_P` being 0 here, and proves nothing about it: two floors that
coincide are two floors.

---

## 5. The stretch — reached, and it went further than the packet asked

### 5.1 `a_∞` at `(19,2⁷)` and `(21,2⁷)`: the batch's two open single-method values

Board §3 slot 4: *"`a_∞(19,2⁷) = 392` and `a_∞(21,2⁷) = 533` … **single method —
your priority**"*, and `docs/batch14_reconciliation.md` §8 says the same, noting
that the integrator's own reproduction on the house `a_weyl` is replay, not
method diversity. The bracket route is a **third** method: neither the Weyl
alternation nor the stable-slice counter, and it imports nothing from either.

| tail | brackets | points | generic rank, both primes | banked |
|---|---|---|---|---|
| `(19,2⁷)` | 950 | 460, re-run at 700 | **392** | 392 |
| `(21,2⁷)` | 1337 | 610 | **533** | 533 |

`a_∞ ≥ 392` and `a_∞ ≥ 533` are **CERTIFIED** and need only that the brackets are
weight-`λ̄` highest-weight vectors (C3), not that they span. Equality is
**CONDITIONAL** on the ADOPTED first fundamental theorem, which C4 validates on
twelve tails. Ranks sit strictly below the point counts, so neither is
sampling-limited.

This discharges slot 4's *lower* half for both values by a genuinely different
route, at a cost of about 90 seconds. It does not discharge 533's upper half
beyond what spanning gives.

### 5.2 The determinant and padded ranks at `(19,2⁷)` — new

| family | rank, both primes | reading at the stable tail |
|---|---|---|
| GEN | 392 | `a_∞ ≥ 392` |
| DET | **390** | `mult_det ≥ 390`, so `i_det^∞ ≤ 2` |
| PAD | **377** | `mult_pad ≥ 377`, so `i_pad^∞ ≤ 15` |
| DET perturbed off `M_ℓ` | 392 | C6 again: the 390 is a detection |

`a = a_∞` at a cell forces `i_X = i_X^∞` there for every `X` — the filtration in
Proposition S's proof has saturated, so the whole of `C[Z]^{hw}_λ̄` is already
present and so is every subspace of it. The banked `a((71,19,2⁷),26) = 392`
therefore makes B13-06's best target a stable cell, and these values are its
values. **That transfer is CONDITIONAL on the banked 392 at that cell**, which is
a different statement from my `a_∞ ≥ 392` and is not established here.

Conditional on it: at `(71,19,2⁷)₂₆`, `mult_det ≥ 390` and `mult_pad ≥ 377`.
`offladder_targets` PROVES a new determinant equation there, so `mult_det ≤ 391`
and `mult_det ∈ {390, 391}`.

**The padded reading was run as a falsification test, not a confirmation.**
Containment `P ⊆ D` forces `mult_pad ≤ mult_det ≤ 391`, so a padded floor of 392
at that cell would have refuted containment. It read 377.

### 5.3 What the determinant floor buys, exactly

The packet: *"a floor of `392 − p` closes B13-06's best target, `p` being the
certified lower bound on `i_pad(24)`."* The floor is **390 = 392 − 2**.

By Lemma T every genuine padded relation at LMR survives to the target, so
`i_pad(target) ≥ i_pad(24) ≥ p` and `mult_pad(target) ≤ 392 − p`. With
`mult_det(target) ≥ 390`,

    D((71,19,2⁷)₂₆) = mult_pad − mult_det ≤ (392 − p) − 390 = 2 − p.

**So `p ≥ 2` closes the target, and the requirement is now exactly 2.**

**`p ≥ 2` is not certified anywhere in this tree, and neither is `p ≥ 1`.**
`lmr_D_measured` is MEASURED and explicitly never promoted; a five-dimensional
sampled kernel at 282 points bounds `i_pad ≤ 5` and proves nothing downward;
`results/s74/certified.json` `padded_candidates` says in terms *"no
characteristic-zero membership claimed"*; and `evaluation_cannot_certify_i_ge_1`
is the standing rule that a sampled nullity is a ceiling. My own PAD floor of 269
at LMR is likewise a ceiling `i_pad ≤ 5` and cannot supply `p`. **The target is
therefore NOT closed by this session**, and I said so in the pre-registration
before measuring rather than after.

The hand-off is exact: **certify `i_pad(24) ≥ 2` — by `complete_interpolation`
(slots 1, 2, 3, 7) or otherwise — and B13-06's best target closes on this floor
alone.**

### 5.4 A coincidence that will otherwise be misread

My determinant floor at the `(19,2⁷)` **stable** tail is **390**, and `390` is
also the banked ambient `a((63,19,2⁷),24)` from the scratch code. **These are
different numbers about different cells and their agreement is a coincidence.**
This instrument computes stable values; `(63,19,2⁷)₂₄` and `(67,19,2⁷)₂₅` are
non-stable cells of that ladder (`a = 390, 391 < 392`) and it does not reach them.
**390 and 391 remain single-route**, and nothing here changes that.

---

## 6. Independence, stated precisely

No code, data structure, or mechanism is shared with s69, s74 or s79. There is no
raising operator, no weight-space enumeration, no `u`-tower, no transport
exponent and no CRT reconstruction anywhere in `analysis/b14_06_*`. What is
imported: the two house primes; `analysis/wk9_s57_stable.a_inf` **as a comparison
in C4 only** (s57 code, the Weyl alternation, never in an evaluation path); and
the target values 274/273/269, 392, 533, which a reproduction must compare
against. `docs/s57_report.md` Proposition S supplied the picture and the point
maps; `analysis/wk12_s79_stable.py` and `docs/b13_07_report.md` were read for
conventions only; `results/s74/certified.json` supplied the values being
reproduced and its `row_system` string, which is what established that s74's
presentation is the transported non-stable one and therefore that nothing in it
could be reused.

`docs/b14_claude_scratch_code.md`'s caveat 5 — *"the stable counter has no
circuit … the stable bracket evaluator slot 6 asks for is not here and not
started"* — is accurate: nothing from it was used, and it is now written.

---

## 7. What I did not do, priced

- **`i_pad(24) ≥ 2` is not certified**, so B13-06's best target is **NOT
  closed**. That is slots 1/2/3/7's `complete_interpolation` chain, not mine.
- **`mult_det` at `(19,2⁷)` is a floor, not an exact value.** `i_det^∞ ∈ {1,2}`
  there. Deciding between them needs either `complete_interpolation` at that tail
  or an exhibited second determinant equation. Cost on this instrument: the
  evaluation side is already done; what is missing is the *upper* half, which
  evaluation cannot supply — `evaluation_cannot_certify_i_ge_1`.
- **`a((71,19,2⁷),26) = 392` is inherited, not checked here.** The stable-tail
  values transfer to that cell only through it. Checking it needs a non-stable
  ambient count; ~220 s on the house `a_weyl` per
  `docs/b14_claude_scratch_code.md`, and it would still be the same route.
- **`(21,2⁷)`: only `a_∞`.** DET and PAD there were not run. They would be
  ~18 s/family/prime on this instrument, but `(69,21,2⁷)₂₆` has `a = 531 < 533`,
  so that cell is **not stable** and the stable values would not transfer to it.
  Reaching it needs the non-stable picture, which this instrument does not have.
- **No exact rational arithmetic.** Everything is mod two house primes, which is
  what floors require (`rank_p ≤ rank_ℚ`) and all that is claimed. An exact
  `ℚ`-rank would need signed CRT over a re-derived height bound, as in slots 2
  and 7; not attempted, and not needed for a floor.
- **Tails of other shapes.** The enumerator assumes `λ̄' = (col,col,1^k)`, i.e.
  `λ̄ = (x,2^{col−1})`. General tails need columns of other heights — the same
  construction, more bookkeeping in `enumerate_brackets` and a `BigM` with more
  than two blocks. Not attempted. It is the natural next extension of this
  instrument and I would price it at a fraction of a session.
- **Nothing was announced or published**, no history was rewritten, no push was
  made, and the four single-writer files were not touched.

## 8. Host resources, declared

An isolated cloud container: **2 cores, 8.0 GB RAM, ~30 GB free disk**, not shared
with the other eleven sessions. `gcc` 13.3.0, numpy 2.4.4, scipy 1.17.1 present;
**`python-flint` 0.9.0 and `sympy` 1.14.0 installed by me**. Every run was
launched under `timeout` and `ulimit -v 6291456`, with its pid written to
`results/logs/<run>.pid`; no run needed ending, and none was ended by anything
other than its recorded id. Total compute for everything in this report: under
nine minutes. The instrument is cheap enough that the next session should treat
re-running it as free.

## 9. Files

| path | what |
|---|---|
| `results/PREREG_b14_06.md` | pre-registration, committed before any measurement |
| `analysis/b14_06_bracket.py` | the bracket index set, the `BigM` evaluator, the brute-force control, Euler relations, jets |
| `analysis/b14_06_points.py` | the six point families and the normalise+depress map |
| `analysis/b14_06_run.py` | controls with their must-fail twins, and the measurements |
| `results/b14_06/selftest.json` | controls only |
| `results/b14_06/lmr.json` | the `(17,2⁷)` reproduction |
| `results/b14_06/stretch.json` | `(19,2⁷)` and `(21,2⁷)` |
| `results/b14_06/saturation.json` | 700-point re-run, fresh seed |
| `results/logs/b14_06_*.log`, `*.pid` | run logs and recorded pids |

Replay, from the repository root, about nine minutes total on two cores:

```
python3 analysis/b14_06_run.py --selftest
python3 analysis/b14_06_run.py --measure --tail 17,2,2,2,2,2,2,2 --npts 340
python3 analysis/b14_06_run.py --stretch
```

Each exits nonzero if any control fails **or if any must-fail twin does not
fail**.
