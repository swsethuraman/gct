# Pre-registration — B13-05 — finite-range padded/reducible equality

```
board_numbering: batch13
session:         B13-05
model:           Claude Fable 5.1 (claude-fable-5-1) — the model that actually ran this session
base (main):     00495110c62acfbbbc951e82cc218ed091563b3f
branch:          b13_05_fable
written:         2026-09-09 15:10 UTC (11:10 America/New_York), before any computation
```

Freeze check passed: `docs/batch13_board.md`, `docs/batch13_corrections.md`,
`docs/stocktake_batch12.md`, `docs/batch13_worker_preamble.md` all present in the
clone at the base above.

## 0. Preflight

| item | state |
|---|---|
| `python3 -c "import flint, sympy, numpy, scipy"` | **failed** (`flint` missing) |
| installed here | `python-flint 0.9.0`, `sympy 1.14.0` (+ `mpmath 1.3.0`) via `pip --break-system-packages` |
| already present | `numpy 2.4.4`, `scipy 1.17.1`, Python 3.11.15, gcc |
| absent, not needed | Singular, msolve |
| host | 2 vCPU (Xeon 2.1 GHz), 7 GB RAM, **no swap**, ~30 GB writable disk |

Host resources are small and are declared: nothing here is a heavy job, and
every run is bounded at launch (`timeout`, `ulimit -v 5000000`, pid to
`results/logs/<run>.pid`).

## 1. Question

Objective 2 of the board (`mult_pad < mult_red` — permanent-specific equations),
on the cubic side.  By Prop. 8 of `docs/transfer_lemma.md`,
`mult_pad(λ,δ) < mult_red(λ,δ)` at length `r` requires `I(D_r^{per₃})_δ ≠ 0`,
and `I(D_r^{per₃})_δ = 0` gives `mult_pad = mult_red` at every weight of that
length and degree.  Write

    a(μ,δ)     = mult of S_μ in Sym^δ(Sym³ Cʳ)        (plethysm; r ≥ ℓ(μ))
    i(μ,δ)     = mult of S_μ in I(D_r^{per₃})_δ        (the ideal's share)
    mult(μ,δ)  = a − i                                  (the coordinate ring's share)

For **r ∈ {7, 8} and δ ≤ 9**: which constituents `S_μ` of `Sym^δ(Sym³Cʳ)` can
lie in `I(D_r^{per₃})_δ`?  Specifically:

- **Q1 (inheritance).**  Separate the constituents excluded automatically —
  `ℓ(μ) ≤ 5` by `docs/washout_lemma.md` Theorem 2 + the restriction lemma;
  `ℓ(μ) = 6` by the certified length-6 record `I(D₆^{per₃})_δ = 0`, `δ ≤ 9`
  (s37 `δ ≤ 6`, s43 `δ = 7`, s41/s43/s47 `δ = 8`, s79 `δ = 9`) — from the
  **genuinely new** ones: `ℓ(μ) = 7` (shared by `r = 7` and `r = 8`) and
  `ℓ(μ) = 8` (`r = 8` only).  Produce the exact census of the genuinely new
  constituents with `a`, `N_S`, `|Stab_W(μ)|`, `n_χ ≥ N_S/|Stab|`.
- **Q2 (structure).**  Prove and state, for the report and for B13-09's queue:
  (i) the restriction/inheritance theorem in the form "the cubic problem is the
  ideal of the orbit closure of `per₃` in `Sym³C⁹`, organised by length: lengths
  `≤ 5` empty, lengths `≥ 10` automatic, lengths 6–9 the content";
  (ii) the degree floor `I(D_r^{per₃})_δ = 0` for `δ ≤ 6`, every `r`;
  (iii) the **cubic ladder**: multiplication by a highest-weight vector of weight
  `ν` and degree `δ'` injects `I_δ[μ] → I_{δ+δ'}[μ+ν]`, so `i(μ+ν, δ+δ') ≥ i(μ,δ)`
  and a certified full-rank cell closes all its predecessors — in particular the
  degree-9 census at lengths 7 and 8 implies the degree-7 and degree-8 censuses;
  (iv) the **orbit-stabiliser bound**: `mult(μ,δ) ≤ b(μ,δ) := dim S_μ(C⁹)^{H'}`
  with `H' = T ⋊ ((S₃×S₃)⋊Z₂)` the proved subgroup of `Stab_{GL₉}(per₃)`
  (row/column scaling with `det D₁ det D₂ = 1`, row/column permutations,
  transpose).  Where `b(μ,δ) < a(μ,δ)` this is a **membership statement**:
  `i(μ,δ) ≥ a − b ≥ 1`, proved, no sampling.
- **Q3 (the residual set).**  The rigorously specified set of constituents that
  must still be computed = the genuinely new cells with `b ≥ a`, ordered by
  price, with the ladder structure that says which of them are logically
  implied by which.

Not sought: global equality at six variables (`dim P₆ = 55 < 61 = dim R₆`);
any quartic/padded cell; B13-09's numerical queue.

## 2. Instruments

- **I1 — plethysm.**  `a(μ,δ)` by `analysis/wk8_s30_pleth.amb` (symmetric-function
  route) **and** by `analysis/wk9_s42_census.a_weyl` (Weyl alternation over the
  tail DP) at every census weight.  Disagreement anywhere halts the census.
- **I2 — price.**  `N_S` by the tail DP `N_S_tail_n(μ, δ, 3)` with `r = ℓ(μ)`;
  `|Stab_W(μ)|` by `stab_order`; `n_χ` reported as the lower bound `N_S/|Stab|`
  (exact `n_χ` needs the orbit enumeration and is B13-09's).
- **I3 — the orbit-stabiliser bound.**  `b(μ,δ) = (1/72) Σ_{f∈F} tr(f | S_μ(C⁹)^T)`,
  `tr(f | S_μ[ν]) = ⟨ s_μ , Π_{cycles c of f} p_{ℓ_c}[h_{ν_c}] ⟩` summed over the
  magic squares `ν` (3×3, line sums `δ`) fixed by `f` (Cauchy identity; proof in
  the report).  Characters `χ^μ(τ)` by Murnaghan–Nakayama (`wk8_s30_pleth.chi`).
  The torus-only bound `b_T(μ,δ) = Σ_{ν} K_{μν}` by an independent Kostka DP.
  **Checks, all mandatory before I3 is used:**
  1. the `f = id` term agrees between the Kostka DP and the character route at
     every `μ`;
  2. the global sum rule `Σ_μ b(μ,δ)·dim S_μ(C⁹) = (1/72) Σ_f #{monomials of
     `Sym^{3δ}(C⁹⊗C⁹)` with magic right-content, fixed by `f`}` (Burnside on the
     monomial basis, an independent count) at every `δ ≤ 9`;
  3. brute force at `δ = 2` and `δ = 3`: `b(μ,δ)` as the kernel dimension of the
     left raising operators plus `F`-invariance on the multigraded monomial space,
     exact, for every `μ ⊢ 3δ`;
  4. consistency with the record: `b(μ,δ) ≥ a(μ,δ)` wherever `i = 0` is proved
     or certified — every `μ` at `δ ≤ 6`, every `ℓ(μ) ≤ 6` at `δ = 7, 8, 9`.
     A single violation is an instrument defect and I3 is withdrawn.
- **I4 — validation only, not a census.**  `analysis/wk8_s30_core.measure`
  (`n = 3`, points `per₃(Σ sᵢAᵢ)`, both house primes `2147483647`, `2147483629`,
  `a + 8` points, seed 11, box ±40) at **at most three pre-named cells**, chosen
  as the cheapest by `N_S` among `a ≥ 1` cells with `N_S ≤ 60 000`:
  (ℓ = 6, δ = 7) computed at `r = 7` — must reproduce the `r = 6` record
  (`mult = a`), the inheritance check; the cheapest (ℓ = 7, δ = 7) at `r = 7`;
  the cheapest (ℓ = 8, δ = 8) at `r = 8`.  Plus, if I3 gives `b < a` at a cell
  with `N_S ≤ 60 000`: the sampled `mult` there must be `≤ b` (a violation is a
  defect in I3), and `mult = b` pins `i = a − b` exactly.

## 3. Objects

All partitions `μ ⊢ 3δ` with `ℓ(μ) ≤ 9` and `a(μ,δ) ≥ 1`, `δ = 1..9`, tabulated
by `(δ, ℓ(μ))`.  The assignment's objects are `ℓ(μ) ∈ {7, 8}`, `δ ∈ {7, 8, 9}`
(Pieri: `ℓ(μ) ≤ δ`, so length 8 starts at `δ = 8`).  `ℓ ≤ 6` are the inherited
controls for check I3.4.  `ℓ = 9` at `δ ≤ 9` is **outside the assignment** and is
reported as exploratory only (it is the `r = 9` problem).

## 4. Stopping rules

- Every script: `timeout`, `ulimit -v 5000000`, pid in `results/logs/<run>.pid`.
- Character/plethysm work: at most 3600 s per degree; if degree 9 does not
  finish, the census is delivered through degree 8 and the boundary is named.
- Brute-force checks only at `δ ≤ 3`; validation cells only with `N_S ≤ 60 000`,
  1800 s each; at most three plus the `b < a` cells.
- The 18:00 ET update and the 20:30 ET report are hard stops; whatever is
  unfinished is priced and handed off.
- No cell is banked below both primes; a modular rank drop is a ceiling on `i`,
  never a floor; a claimed `i ≥ 1` comes only from the bound `b < a` (a
  membership statement) and goes through the verification protocol
  (`docs/batch13_worker_preamble.md`) before it is reported anywhere.

## 5. What counts as a negative

- **N1.**  `b(μ,δ) ≥ a(μ,δ)` at every genuinely new cell in range: the
  orbit-stabiliser bound is silent at lengths 7 and 8 through degree 9.
  Reported as a priced negative with the margin `b − a` per cell; the residual
  set is then the whole genuinely new census, and Q3 is its ladder-reduced form.
- **N2.**  A validation cell with `mult = a` at both primes: certifies
  `i = 0` at that one cell over `Q`; it says nothing about any other cell.
- **N3.**  A failed check (I1 disagreement, I3.1–I3.4): an instrument defect;
  nothing is claimed from the failing instrument, and the defect is reported.

What counts as **positive**: `b(μ,δ) < a(μ,δ)` at some cell with `ℓ(μ) ∈ {7,8}`,
`δ ≤ 9` — **PROVED** `i(μ,δ) ≥ a − b ≥ 1`, i.e. `S_μ ⊂ I(D_r^{per₃})_δ` for
`r = ℓ(μ)`, a permanent-specific cubic equation at that weight.  This is an
objective-2 statement; it does not produce, and is not claimed to produce, a
`D > 0` cell.

## 6. Labels

**PROVED** (a proof in the report) / **CERTIFIED** (a full rank mod a house
prime, valid over `Q`) / **MEASURED** (sampled) / **ADOPTED** (an input taken
from the record or the literature: Theorem 2, the restriction lemma, Prop. 8,
the length-6 record s37/s41/s43/s47/s79, the Marcus–May stabiliser — the latter
is **not** load-bearing, only the proved subgroup `H'` is used) / **RECORDED**.

## 7. Deliverables

`results/b13_05_census.json`, `results/b13_05_census.md`,
`results/b13_05_bound.json`, `analysis/wk13_b13_05_*.py`, logs under
`results/logs/b13_05_*`, `docs/b13_05_report.md`; bundle `b13_05_fable.bundle`
+ `.md5` against the base above.  Dated addenda to this file are committed
before the measurements they govern.

Author of record for the session: B13-05 (Claude Fable 5.1).  Programme author:
Swami Sethuraman, swsethuraman@beneficus.ai, Beneficus AI.
board_numbering: batch13

---

## Addendum A (2026-09-09 15:35 UTC / 11:35 ET) — committed before the computations it governs

**What is already known at this point (banked in `305ae5a`):** the census
through degree 9 (two `a`-routes agree at all 1444 rows) and the
orbit-stabiliser bound through degree 7: checks I3.1, I3.2, I3.4 pass, and
the bound is **silent** at every cell with `a ≥ 1` (minimum margin `b − a = 117`
at `(9,2⁶)₇`).  Degrees 8 and 9 of the bound will be run for the record; the
expectation is N1.

**A1 — a new structural instrument, I5: the top cells are catalecticant minors.**
For `ℓ(μ) = δ` write `λ = μ − (1^δ)`.  Claim to be proved in the report: the
`GL(V)`-map `ψ : Λ^δ(Sym²V) ⊗ Λ^δV → Sym^δ(Sym³V)`,
`(q₁∧…∧q_δ) ⊗ (v₁∧…∧v_δ) ↦ Σ_σ sgn(σ) Π_i (q_i · v_{σ(i)})`, sends the
highest-weight vector `m₁∧…∧m_δ` (the quadratic monomials of the shifted diagram
of the strict partition `λ`) ⊗ `e₁∧…∧e_δ` to the weight-`μ` highest-weight vector

    h_μ(c) = det [ ⟨c, m_i e_j⟩ ]_{i,j=1..δ}  =  a δ×δ maximal minor of the catalecticant Cat_{1,2}(c): V → Sym²V*,

and, since `a(μ,δ) = 1` at every top cell in range (census), `h_μ` spans the
weight-`μ` highest-weight space whenever it is a nonzero polynomial.  Then
`i(μ,δ) = 0` **iff** `h_μ(c) ≠ 0` at one point `c = per₃(Σ sᵢAᵢ)` — a single
`δ×δ` determinant of third derivatives (polarised permanents), no `N_S`-sized
linear algebra.  Validation of I5 before use: (a) at `δ = 3, 4, 5` express `h_μ`
in the house monomial basis and check exactly that it is killed by the house
raising operators (`wk8_s30_core.build_R`) and is nonzero; (b) at every top
cell `δ ≤ 9` check the weight and nonvanishing at a random rational cubic;
(c) at `δ ≤ 6` the value at a `per₃` pencil must be nonzero (the record has
`I = 0` there).  Then evaluate at the 19 top cells of `δ = 7, 8, 9`
(`5 + 6 + 8`), both house primes, `a + 8 = 9` pencils each (seed 11, box ±40,
the house family), and report: a nonzero determinant at one pencil at one prime
is a **CERTIFIED** `i = 0`; a zero at all pencils at both primes is a
**candidate** `i = 1` and goes to the verification protocol, not to the report
as a result.  The `ℓ = 9`, `δ = 9` top cells are outside the assignment and are
reported as exploratory.

**A2 — I3.3 cap.**  The brute-force check is run at `δ = 2` for every `μ ⊢ 6`
and at `δ = 3` for every `μ ⊢ 9` whose monomial space (9×9 contingency tables
with row sums `μ` and magic column sums) has at most `2·10⁵` elements; the
weights above the cap are named in the report as unchecked by I3.3.  Method:
`F`-orbit sums first, then the left raising operators on the orbit-sum basis,
exact rank over `Q` (flint `fmpq_mat`) and at both primes.

**A3 — dimension witnesses.**  Jacobian rank of `Φ_r : M₃ʳ → Sym³Cʳ` at one
random integer point (box ±10⁶, seed 20260909), both primes, for `r = 7, 8, 9`;
a rank equal to `9r − 4` proves `dim D_r^{per₃} = 9r − 4` (Lemma 1 + Prop. 5 of
`docs/washout_lemma.md`, the sandwich), extending Corollary 7's table.

**A4 — the I4 cells, named.**  (ℓ=6, δ=7) at `r = 7`: `(11,2,2,2,2,2,0)`,
`N_S = 4603`, the cheapest length-6 weight of degree 7 (s41 line 1), run with
`wk8_s30_core.measure(per₃, 9, 3, 7, 7, ·)`; expected `a = 1`, `mult = 1` at
both primes.  The (ℓ=7, δ=7) and (ℓ=8, δ=8) I4 cells are **replaced by I5**
(their `N_S` are 48 122+ and 1 259 739+, above the dense route's reach on this
host); this replacement is recorded here as a change of instrument, not of
question.

board_numbering: batch13
