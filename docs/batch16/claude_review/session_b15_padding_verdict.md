# B15 — the ℓ = 10 stable cell (105, 19, 2⁸) at δ = 35: is m_pad ≥ 419?

*Independent session, new harness. Instrument: the banked B14-06 bracket evaluator
(`b14_06_bracket.py`, `b14_06_points.py`) with the B15-06 dimension adapter
(`b15_06_geometry.py`), `col = 9`, `W = 35`, 1019 brackets, 14 (a,b) patterns.
Nothing below reuses the batch-15 point seeds or its `[-12,12]` integer grid.*

---

## Verdict

**419 is not attainable in this cell, and the cell does not need the padded column
to die — it dies one stage earlier, at the reducible relaxation.** In a fixed
429-bracket basis, at **four** independent primes, with substitutions drawn
**uniformly mod p** rather than from `[-12,12]`, the evaluation ranks are
`GEN 429`, `DET 418`, `RED 410`, `PAD 243`. Every point of the padded orbit is a
linear form times a cubic, so `I(R₁₀) ⊆ I(D₁₀^pad)` — verified here as an exact
subspace inclusion, not assumed — hence `m_pad ≤ m_red`. With
`i_red = 19 > i_det = 11` that already gives `D ≤ D_R = m_red − m_det = −8 < 0`;
the direct padded column gives `D = −175`. This is session 70's *strongest cheap
outcome* configuration: **settled against `D > 0` by the reducible rank alone**,
so no permanent-specific or `det A`-style work on this cell is needed. The 243 is
**not** a sampling defect, but the batch-15 evidence for it was genuinely
uncertifiable: the bracket values have degree 140 in the substitution entries
against a 25-value grid, so Schwartz–Zippel said nothing at `[-12,12]` no matter
how many points were drawn. Uniform mod-`p` sampling reproduces 243 exactly and
there SZ gives `≤ 2.7 × 10⁻⁵` per run. The 186 padded kernel directions are real:
19 of them are the reducibility ideal and the remaining **167 are a
permanent-specific ideal** — the first one this cell's tail has shown.

---

## 1. What was measured

Ranks of the 1019 × 480 bracket-evaluation matrix (rows = brackets, columns =
points), `r = 10`, `col = 9`, `W = 35`, 480 points requested per run.

| family | source | p₁ 2147483647 | p₂ 2147483629 | p₃ 2147482951 | p₄ 2147482949 |
|---|---|---|---|---|---|
| GEN | free symmetric `N₂,N₃,N₄` (Euler-closed) | **429** | **429** | **429** | **429** |
| DET | traceless 4×4 pencil, entries uniform mod p | **418** | **418** | **418** | **418** |
| RED | `ℓ · C`, `ℓ ∈ C¹⁰*`, `C ∈ Sym³C¹⁰*` uniform mod p | **410** | **410** | **410** | **410** |
| PAD | `z·per₃ ∘ L`, `L ∈ C^{10×10}` uniform mod p | **243** | **243** | **243** | **243** |

`PAD` with the original `[-12,12]` grid also reads 243 (455 of 480 points valid);
with uniform mod-`p` entries all 480 survive the chart. `GEN 429 = a_∞` is the
spanning control — the 1019 brackets span the whole highest-weight space.

Derived, in the 429-dimensional highest-weight space:

| | i (= 429 − rank) | m |
|---|---|---|
| det | **11** | 418 |
| reducible | **19** | 410 |
| padded | **186** | 243 |

`D = m_pad − m_det = −175`.  `D_R = m_red − m_det = −8`.

Exact subspace relations (computed, all four primes agree):

* `I_red ⊂ I_pad` — **exactly**, dim(I_pad + I_red) = dim I_pad = 186. (Required
  by `X_pad ⊆ R₁₀`; it is a control that it holds numerically.)
* `dim(I_det ∩ I_red) = 0` — no determinant equation is a reducibility equation.
* `dim(I_det ∩ I_pad) = 2` — only two of the eleven determinant equations also
  kill the padded family.

---

## 2. The derivation

### 2.1 The 10 × 10 substitution family is complete — a proof, not a heuristic

`λ = (105,19,2⁸)` has **exactly ten positive parts**. A highest-weight vector
`f_λ ∈ C[Sym⁴C¹⁶]₃₅` is a polynomial in the coefficients `c_α` of the quartic;
weight `λ` forces every monomial of `f_λ` to be built from `c_α` whose `α` is
supported on the first ten variables (the torus weight of `c_α` is `α`, and
`λ_j = 0` for `j > 10`). Hence for every quartic `F`

  `f_λ(F) = f_λ( F|_{x₁₁ = … = x₁₆ = 0} )`.

Apply this to `F = P ∘ M`, `M ∈ GL₁₆`, `P = z·per₃` using ten of the sixteen
variables. Writing `π : C¹⁶ ↠ C¹⁰` for the projection onto the ten variables `P`
uses and `ι : C¹⁰ ↪ C¹⁶`, we get `(P∘M)|_{C¹⁰} = P ∘ (π M ι)`, and as `M` ranges
over `GL₁₆` the composite `πMι` ranges over **all** of `End(C¹⁰)`. Therefore

> a weight-`λ` HWV vanishes on `GL₁₆·(z·per₃)` **iff** it vanishes on
> `{ P ∘ L : L ∈ GL₁₀ }`.

So: **no omitted degrees of freedom.** The six unused variables contribute
nothing, and neither does any part of the 16×16 substitution group beyond its
10×10 corner. The chart `c = F(e₀) ≠ 0` and the normalise/depress step restrict to
a dense open subset of the same family, and a HWV vanishing on a dense subset of
an irreducible family vanishes on it, so they lose nothing either. This answers
question 1 structurally rather than by a dimension count, and it is why more
random points was never going to be the issue.

### 2.2 `D` needs no ambient count

`m_fam = a_λ − i_fam`, and `i_fam = a_λ − rank_fam` when the brackets span, so
`m_fam = rank_fam` **directly**. Hence

  `D = m_pad − m_det = rank_PAD − rank_DET`,

computed in one basis on one instrument. `a_λ = 429` enters only as the spanning
control (`GEN` must read `a_∞`), never as a term in `D`. This also makes the
finite-cell screening in §5 well-posed without a finite ambient count.

### 2.3 The Schwartz–Zippel certificate — and the exact defect in the old grid

For **every** bracket in this cell, `Σ_d d·n_d = 35`. The depressed data satisfies
`c^d·G_d = (polynomial of degree d in F)`, so for a bracket of multidegree
`(n₂,n₃,n₄)`

  `c(F)³⁵ · bracket(reduced F) = N(F)`, a polynomial of degree exactly **35** in
  the coefficients of `F`, with the **same** exponent 35 for every bracket.

Scaling column `i` by `c(L⁽ⁱ⁾)³⁵ ≠ 0` is therefore rank-preserving, and turns the
entries into `N(P∘L⁽ⁱ⁾)`, polynomials of degree `≤ 4·35 = 140` in the 100 entries
of `L⁽ⁱ⁾`.

If the generic rank were `ρ ≥ 419`, some `419×419` minor is a **nonzero**
polynomial of degree `≤ 140·419 = 58,660` in the 48,000 sampled entries.

* over the `[-12,12]` grid (25 values): SZ bound `58,660/25 ≫ 1` — **vacuous**.
  *This, not the point count, is why 462 points at `[-12,12]` could not certify
  anything;* the note "already 462 points were available" was answering the wrong
  objection.
* over uniform `F_p`, `p ≈ 2.147×10⁹`: SZ bound `≤ 2.7×10⁻⁵` **per run**. Six
  independent uniform runs across four primes all read 243.

For `RED` the parameters are `(ℓ, C) ∈ C¹⁰ × C²²⁰` and `N(ℓ·C)` has bidegree
`(35,35)`, total degree 70, so the per-run bound is `≤ 70·419/p ≈ 1.4×10⁻⁵`.

### 2.4 The reducible bound — the strongest single item

`z·per₃(X)` composed with any substitution is `(z∘M)·per₃(X∘M)`: a linear form
times a cubic. So `X_pad ⊆ R₁₀ = {ℓ·C}` **with no sampling**, hence
`I(R₁₀) ⊆ I(X_pad)` and

  `m_pad ≤ m_red`.

Measured `m_red = 410 < 418 = m_det`, so `D ≤ D_R = −8`. The cell is closed
against `D > 0` by the reducible column alone; the padded column's further drop to
243 is extra information, not load-bearing for the verdict.

---

## 3. Routes that were asked for and are dead

### 3.1 The stabilizer bound is vacuous here — by six orders of magnitude

`Stab_{GL₁₀}(z·per₃)°` is the **5-dimensional** torus
`{ z ↦ (∏d_r ∏d_c)⁻¹ z, X ↦ D_r X D_c }`, with component group `(S₃×S₃)⋊Z₂` of
order 72 (row/column permutations and transpose). No unipotent part survives: a
`z ↦ αz + ℓ(X)` or `X ↦ TX + zC` mixing is killed by the `z`-degree.

`m_pad ≤ dim (S_λ C¹⁰)^H`. For the torus, an invariant weight has `μ_z = 35` and
the 3×3 array of the other nine parts has **all row and column sums 35**, so the
bound is `Σ_m K_{λ,μ(m)}` over 3×3 magic squares `m` of line sum 35. For this `λ`
the Kostka number is elementary: columns 1 and 2 of any SSYT are forced to be
`(1,…,10)`, and putting `z` first in the alphabet makes the two-row ballot
condition vacuous, leaving

  `K_{λ,μ} = #{ b : 0 ≤ b_ij ≤ m_ij − 2, Σ b_ij = 17 }`.

(Validated against brute-force SSYT enumeration on 4,660 small cases, zero
mismatches, and its symmetry in `μ` checked.) Summing:

> **`dim (S_λ C¹⁰)^{T_H} = 44,104,382,352`**, and even divided by the order-72
> component group that is `6.1 × 10⁸` against `a_λ = 429`.

**Retire this route for the padded column.** The reason is structural, not
specific to this cell: the padded permanent has a 5-dimensional stabilizer, so
`C[GL₁₀/H]` is enormous and the binding constraint on `m_pad` is always the
ambient `a_λ`. Ordinary stabilizer bounds will never see a padded obstruction.

### 3.2 The Pieri / reducible-parametrization bound — not worth paying for

`R₁₀` is the image of `C¹⁰* × Sym³C¹⁰*`, so
`m_red ≤ Σ_β c^λ_{(35),β} · mult_β Sym³⁵(Sym³C¹⁰)` with `λ/β` a horizontal
35-strip, i.e. `β = (β₁, β₂, 2⁷, β₁₀)`, `β₁+β₂+β₁₀ = 91`, `β₂ ∈ [2,19]`,
`β₁₀ ∈ [0,2]` — **54 terms**, each a full cubic-plethysm multiplicity. The sum is
`≥ m_red = 410` by construction and is a sum of 54 such numbers, so it will not
land below 418. Two further obstacles if it is ever wanted: the `β₁₀ = 1` tails
have conjugate shape `(9,8,1^k)`, which the present evaluator (written for
`(col,col,1^k)`) cannot express; and the cubic-side stability threshold at
`β₁ ≥ 70` is unproved.

---

## 4. Four things worth banking regardless of the verdict

1. **`i_det = 11 > 0`** on this stable ten-row cell — against `i_det = 0`
   everywhere in the six-row record. The tail is doing what it was chosen to do.
2. **`i_red = 19 > i_det = 11`.** The reducibility bite is *larger* than the
   determinant ideal here. Since `i_pad ≥ i_red` always, **`i_red < i_det` is a
   necessary condition for an obstruction at any cell**, and it is much cheaper
   to test than the padded column. This cell fails it by 8.
3. **`mult_pad = 243 ≪ mult_red = 410`: a 167-dimensional permanent-specific
   ideal.** The six-row record (s41/s43/s47/s79) has `mult_pad = mult_red` at
   every measured cell, and s79 states the first cell where they can differ has
   `δ ≥ 10`. At `ℓ = 10`, `δ = 35` they differ enormously. If the programme wants
   permanent-specific equations as objects, **this cell is where they live.**
4. **The `Q`-multidegree grading is useless for certificate search.** Splitting
   the 1019 brackets by `(n₂,n₃,n₄)` (30 blocks, `2n₂+3n₃+4n₄ = 35`): every block
   has the **same** rank on GEN, DET, PAD and RED, and the 30 block ranks sum to
   exactly 429 for all four families. So `I_det`, `I_red`, `I_pad` each meet every
   graded piece in **0** — every equation strictly mixes multidegrees. Any
   certificate search that proceeds block-by-block will find nothing, by
   construction.

| `(n₂,n₃,n₄)` | #br | GEN | DET | PAD | RED |
|---|---|---|---|---|---|
| (0,1,8) | 1 | 1 | 1 | 1 | 1 |
| (3,7,2) | 55 | 24 | 24 | 24 | 24 |
| (7,3,3) | 96 | 39 | 39 | 39 | 39 |
| (16,1,0) | 5 | 2 | 2 | 2 | 2 |
| *(all 30 blocks)* | 1019 | **429** | **429** | **429** | **429** |

---

## 5. The two tests

Sizes below are **hypotheses until measured**; both are single-process.

### Test 1 (rank 1) — deterministic closure from eleven *reducible* equations

**Why this one.** It removes every probabilistic step from the verdict, and the
target is small: `i_red ≥ 11` alone gives `m_red ≤ 418`, hence
`m_pad ≤ m_red ≤ 418 < 419`. Eleven equations on the **reducible** variety —
a classical GL-stable object — not 186 permanent-specific ones.

**Source, already produced here.** In the fixed 429-bracket basis (the pivot rows
of the GEN matrix, recorded), `I_red` is 19-dimensional and `I_det` is
11-dimensional. Both lift from the four primes (124-bit modulus) by CRT +
rational reconstruction to **exact rational vectors** whose numerators and denominators are bounded by
`2.7×10⁸` and `2.5×10⁹` respectively — about `2³²` against a `2⁶¹`
reconstruction bound, so the lift is genuine, not an artefact of the modulus.
Cleared to primitive integer rows the largest entries are `3.08×10¹²` (`I_red`)
and `5.67×10¹¹` (`I_det`). The exact integer rows are
in `exact_ideals.json` (`basis_bracket_indices`, `I_red` 19×429, `I_det` 11×429,
plus the bracket list).

**The control that makes the method credible:** `I_det` is the family whose eleven
equations are *already proved global*. They lift, with small height, by exactly
this procedure. The nineteen reducible vectors come out of the same pipe.

**What to do.** Certify that eleven independent rows of `I_red` annihilate
`F = ℓ·C` identically. Degree: bidegree `(35,35)` in `(ℓ, C) ∈ C¹⁰ × C²²⁰` after
clearing `c³⁵`. The natural exact route is the depressed-jet picture — the bracket
value depends on `(ℓ,C)` only through the 2-jet at `e₁` of the depressed
`(G₂,G₃,G₄)` — so the identity to verify lives in ≈120 jet parameters, not 230.

**Bounded preflight (fits 60 s / 512 MiB) — this session already ran it:**
re-evaluate the lifted **integer** vectors on fresh RED/DET/PAD/GEN points at a
**fifth, unused prime**. Required: `I_red` kills RED and PAD and not GEN or DET;
`I_det` kills DET and not GEN or RED. Results in §7.

**Interpretation.** Symbolic vanishing of eleven `I_red` rows ⟹ `D < 0` here is a
theorem, with no sampling anywhere. A single lifted row that fails to vanish at a
fresh exact point ⟹ either the lift or the 410 is wrong and the whole reducible
reading must be re-opened.

### Test 2 (rank 2) — screen the finite cells by the *reducible* column only

**Which cell.** `δ = 27`, `(73, 19, 2⁸)`, determinant floor `i_det = 5`. It has the
largest floor of the three, and — decisive for interpretation — it carries the
**same tail `(19,2⁸)`** as the stable cell measured here, so the stable numbers
`i_det^∞ = 11`, `i_red^∞ = 19` are directly comparable priors. The `δ = 23` and
`δ = 25` cells (floors 1 and 2) need `i_red = 0` and `i_red ≤ 1`, which is
strictly harder; test them only if `δ = 27` survives.

**What to compute.** On the finite-cell instrument, in one bracket basis:
`rank_DET` and `rank_RED` only. **Do not build the padded column first.** By §2.2
the comparison needs no finite ambient count: an obstruction requires
`rank_RED > rank_DET`, i.e. `i_red < i_det = 5`.

**Falsifiable prediction (mine, stated before the run):** `i_red ≥ 5` at
`δ = 27` and the cell dies the same way. Reasoning: at the same tail in the
stable regime `i_red/i_det = 19/11 ≈ 1.7`; the finite cell's det floor is 5, so a
proportional `i_red` is `≈ 9`. I would be surprised by `i_red ≤ 4` and astonished
by `i_red = 0`.

**Interpretation.** `i_red ≥ 5` ⟹ cell dead, stop, do not price the padded
column. `i_red ≤ 4` ⟹ this is the only configuration in the stated list that can
still produce `D > 0`, and *then* the padded column is worth its cost — and the
167-dimensional permanent-specific ideal found here says to expect
`i_pad ≫ i_red` there too.

---

## 6. Unproved steps, explicitly

1. **Modular vs characteristic zero.** All ranks are `F_p` ranks. Bad reduction
   can only *lower* rank, so `m_pad^C ≥ 243` is safe, but the upper direction
   assumes none of the four primes is bad. Four primes near `2³¹` agreeing is
   strong, not a proof. Test 1 removes this for the reducible column.
2. **Schwartz–Zippel is a probability, not a theorem.** `≤ 2.7×10⁻⁵` per padded
   run, `≤ 1.4×10⁻⁵` per reducible run, six runs. Test 1 removes this.
3. **Inherited from the instrument**, not re-derived here: Proposition S and the
   stable ambient theorem; `a_∞ = 429`; that the 1019 brackets span `HWV_λ`
   (used only via the `GEN = 429` control); the derived `det BigM` evaluation
   formula and its sign/factorial conventions (their control C2).
4. **`I_red ⊆ I_pad`** is proved structurally (`X_pad ⊆ R₁₀`); its numerical
   confirmation here is a control, not the proof.
5. **The exact lift** is certain to `~2⁻⁶⁰` heuristically (height `2³²` recovered
   against a `2⁶¹` bound) but is not itself certified; §7's fifth-prime check is
   an independent test of it, not a proof.
6. **Nothing here says anything about the asymptotic conjecture.** This is one
   fixed weight at `n = 16`, `m = 3`. A negative at `(105,19,2⁸)₃₅` closes this
   cell and nothing else.

---

## 7. Preflight for Test 1 — run here, PASS

`lift2.py`: the four-prime CRT lift, then the exact **integer** rows applied to
**fresh** points at a **fifth prime, `2147482943`, not used in the lift**.

That prime independently reproduces the whole table:
`GEN 429, DET 418, RED 410, PAD 243`.

| exact rows | on RED | on DET | on PAD | on GEN |
|---|---|---|---|---|
| `I_red` (19×429, max entry 3.08×10¹²) | **0** | ≠ 0 | **0** | ≠ 0 |
| `I_det` (11×429, max entry 5.67×10¹¹) | ≠ 0 | **0** | ≠ 0 | ≠ 0 |

Every cell is as it must be. `I_red` vanishing on PAD at a prime it was never
fitted at is the inclusion `X_pad ⊆ R₁₀` seen from the exact side; `I_det`
nonvanishing on PAD is `dim(I_det ∩ I_pad) = 2 < 11`; both nonvanish on GEN, so
neither is a trivial relation among the 1019 brackets.

**The 19 exact reducible equations are therefore in hand, in integers, in a
recorded basis.** What remains for Test 1 is only the symbolic step: show that
eleven of them vanish identically on `ℓ·C`, which turns `D < 0` at this cell from
a four-prime measurement into a theorem.

**Artefacts.** `exact_ideals.json` — `basis_bracket_indices` (the 429 pivot
bracket indices), `brackets` (all 1019 as `(a,b,c,z)`), `I_red` (19×429 integers),
`I_det` (11×429 integers). Harness: `harness.py`, `red.py`, `kernels.py`,
`lift2.py`, `stab3.py`, `kostka_check.py`.
