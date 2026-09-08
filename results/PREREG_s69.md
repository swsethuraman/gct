# PRE-REGISTRATION — session 69 (batch 11, C2): the compact circuit — source vectors as contractions, not coordinates

Committed **before** any evaluation, rank, kernel or expansion of this session
is computed. Branch `s69-circuit`, off `main` at `226b4ef1` (the public tip at
session start; ancestry gate `git merge-base --is-ancestor 226b4ef1 HEAD`
passed on the fresh clone). Container: 2 cores, 7 GB. Container only, no
pushes; delivery by single-ref bundle `s69_circuit.bundle` + `.md5`.

**Missing inputs, recorded.** The brief names `docs/batch11_worker_preamble.md`,
`docs/batch11_plan.md` (§2.1, §4, §9), `docs/stocktake_batch10.md` §4,
`analysis/wk10_s63_n3control.py` and `results/artefacts/s63_n3_ideal_vectors.npz`
as required reading / the control artefact. None of these exists at
`226b4ef1`, in any branch of the public repository, or in the integrator tree
`Projects\gct\work` on the laptop (listed at session start); the s63 bundle
(`s63_lmr_det.bundle`, head `30358ff`) is not among the bundles kept there
either. What *is* available and is used instead:

* `docs/lmr_cell.md`, `docs/brief_wording.md` §7 (present at `226b4ef1`);
* the session-62 bundle (`s62_gram.bundle`, head `79a07d8`, on the laptop),
  which banks **the same object** the brief names: the ideal highest-weight
  vector at `((19,7,2^5), 12)`, `n = 3`, in the χ-coordinates of
  `wk9_s45_build.build_cell` — `results/s62_n3_vec_d12.json` (exact integer
  form, support 3900 of 17047, max |coeff| 544) and
  `results/s62_n3_kern_d12.json` (the same vector mod `2147483647`). The s63
  record (project note `claude/session_63.md`) describes its artefact with the
  identical parameters (shape `(1, 17047)`, prime `2147483647`, 3900 nonzero
  χ-coordinates), and both sessions ran the same engine on the same cell. This
  session therefore takes the s62 vector as *the banked control vector*, says
  so wherever the brief's `.npz` would be cited, and rebuilds the cell itself
  so that the coordinate system is the one the rest of the batch uses
  (`n_χ = 17047` must be reproduced by the rebuild before any comparison).

What was computed before this commit, and decides nothing: the ambient
multiplicities `a = 6, 6, 6` at `λ_δ = (3δ−17, 7, 2^5)`, `δ = 12, 13, 14`,
`n = 3`, and `a = 2` at `((17,17,2^7), 12)`, `n = 4` (house `a_weyl`,
reproducing `lmr_cell` §7 and §6); the raw weight-space sizes
`N_S = 1 155 302, 1 165 249, 1 167 156` at the three `n = 3` cells (house
`monomials_array`). Sizes of the problem, quoted so the regimes can be stated.

## 0. The question, restated in the terms this session will answer it

Sessions 62–64 measured the wall in coordinates: `n_χ ≈ 3.1×10^7` at the LMR
cell, against `dim M_λ = a = 274`. The brief asks whether the wall is in the
object or in the representation, i.e. whether the 274 vectors have a short
description that never mentions the coordinates. The candidate description is
the classical one: **highest-weight vectors of weight `λ` in `Sym^δ(Sym^n C^r)`
are spanned by bracket monomials** — contractions of `δ` polarised copies of
the form with one antisymmetriser per column of `λ` — and the LMR shape
`(65,17,2^7)`, with conjugate `(9, 9, 2^15, 1^48)`, is two full `9×9` brackets,
fifteen `2×2` brackets and forty-eight linear factors. That is the
"`(2^9) + (63,15)`" of the brief: the two columns of height 9 are the
determinantal part, the two long rows are the `2×2` brackets and the
`e_1`-factors.

This session (1) states that representation and its semantics exactly
(`docs/compact_circuit.md`), (2) proves — by exact expansion into the batch's
χ-coordinates — that it is the same object as the coordinate one at the
`n = 3` control cell, (3) measures its size against the carrier along the
`n = 3` ladder, and (4) applies it at the `n = 4` ladder bottom, where the
coordinate route is walled.

## 1. Objects and the identities everything rests on

**Coordinates (house convention, `wk8_s30_core`).** `W = Sym^n C^r`, forms
`f(s) = Σ_α f_α s^α` in `s_1..s_r`; `c_α` the coefficient functional
`c_α(f) = f_α`; `C[W]_δ = Sym^δ(Sym^n C^r)` with torus weight `α` on `c_α` and
raising rule `E_{ij} c_α = (α_i + 1) c_{α + e_i − e_j}` (`i < j`). This is the
infinitesimal form of the substitution action `f ↦ f∘g`, `(gs)_i = s_i + t s_j`:
`(E_{ij}F)(f) = d/dt F(f∘g_t)|_0`. A highest-weight vector of weight `λ` is a
polynomial `F` of degree `δ` in the `f_α`, of weight `λ` under `f ↦ f(ts)`, and
invariant under `f ↦ f∘u` for every upper unitriangular `u`.
`M_λ := HWV_λ(C[W]_δ)`, `dim M_λ = a(λ,δ)`. The χ-coordinates are those of
`wk9_s45_build.orbit_setup_arr`: one coordinate per `Stab_W(λ)`-orbit of
weight-`λ` monomials whose `χ_λ`-twisted orbit sum is nonzero; a χ-vector `v`
is the polynomial `Σ_j v_j Σ_{m∈O_j} sgn_m Π_{k} c_{A[m_k]}`, and every
highest-weight vector lies in this subspace (`docs/stabiliser_reduction.md`).

**Bracket monomials (the circuit).** Let `f̃` be the polarisation of `f`, the
symmetric `n`-linear form with `f̃(e_{i_1},…,e_{i_n}) = (α!/n!) f_α`, `α` the
multiplicity vector of `(i_1..i_n)`. A *filling* `T` of the diagram of `λ`
(`|λ| = nδ`) by `δ` letters, each used exactly `n` times, no letter twice in a
column, defines

    F_T(f)  :=  Σ_{σ_1,…,σ_{λ_1}}  Π_j sgn(σ_j)  Π_{letters ℓ}  n!·f̃(e_{σ(c)} : c ∈ ℓ)
             =  Σ_{σ}  Π_j sgn(σ_j)  Π_ℓ  α_ℓ(σ)! · c_{α_ℓ(σ)}(f),

the sum over one bijection `σ_j : rows of column j → {1..h_j}` per column
(`h_j = λ'_j`), `sgn(σ_j)` taken with respect to the row order, `σ(c)` the
index assigned to cell `c`, and `α_ℓ(σ)` the multiplicity vector of the `n`
indices assigned to the cells of letter `ℓ`. Equivalently `F_T` is the tensor
network with one node `ε_{h_j} = e_1∧…∧e_{h_j}` per column and one node `f̃`
per letter, edges the cells. The factor `n!` per letter is a global constant
and is dropped in all code (`m_α := α!·c_α` is the letter symbol).

**Identity 1 (proved, classical; restated in `docs/compact_circuit.md` with the
one-line proof).** `F_T ∈ M_λ` for every filling `T`: `ε_h` is fixed by upper
unitriangular `g` (`g e_k = e_k + Σ_{i<k} g_{ik} e_i`), so `F_T(f∘g) = F_T(f)`,
and the torus weight is `Σ_j (1^{h_j}) = λ`. The raising operators act on the
circuit by the same rule as on the coordinates and **vanish identically on
every bracket monomial**; this is the circuit's raising-operator action, and
it is checked on the coordinate side (§3, P1) rather than assumed.

**Identity 2 (proved, classical).** The `F_T` span `M_λ`: the highest-weight
vectors of weight `λ` in `(C^r)^{⊗nδ}` are spanned by the column-wedge
products indexed by fillings, and `Sym^δ Sym^n` is the image under the
symmetriser, which is self-adjoint for the pairing with `f^{⊗δ}`. No
combinatorial *basis* is claimed (that would be a plethysm rule); spanning is
verified numerically by rank against `a` from `a_weyl` at every cell used.

**Identity 3 (evaluation; proved in `docs/compact_circuit.md` §3).** For a
shape with two tall columns `C_1, C_2` of height `h`, `2`-columns and
`1`-columns, and a fixed assignment `I` of indices to the `2`-columns,

    Σ_{σ,τ∈S_h} sgn σ · sgn τ · Π_{k=1}^{h} M_k(σ(k), τ(k))  =  Σ_{S⊆[h]} (−1)^{h−|S|} det( Σ_{k∈S} M_k ),

the polarisation identity for the mixed discriminant (coefficient of
`x_1⋯x_h` in `det Σ x_k M_k`), with `M_k` the `h×h` symbol matrix of the
letter in row `k` of `C_1` (a rank-one product `v w^T` when that letter is
not in `C_2`, paired with a `C_2`-only letter; a sign `sgn π` from the
relative row order of `C_2`). This turns `(h!)^2` permutations into `2^h`
determinants: `128` at `n = 3`, `512` at `n = 4`, per `2`-column pattern.

**Identity 4 (the functoriality pre-check, `brief_wording` §7, answered).** The
circuit computes **the same functional** on `Sym^δ(Sym^n C^r)` as the
coordinate representation — `F_T` *is* an element of `M_λ ⊂ C[W]_δ`, written
as a contraction instead of as a coefficient list; its value at any `f`, and
therefore the rank of `M_λ → C^{points}` at determinant pencils, is a property
of the vector, not of the encoding. Nothing in the containment argument
`P ⊆ D ⟹ I(D) ⊆ I(P) ⟹ mult_λ C[P] ≤ mult_λ C[D]` is touched: `mult_det` is
still the rank of evaluation on `M_λ`, and `i_det = a − mult_det` still counts
ideal elements. The only new risk is a **convention mismatch** (the `α!`
weights, the sign conventions, the identification of `c_α` with the
coefficient functional), which would make the circuit a different vector of
the same weight; the exact `n = 3` control exists to catch exactly that, and
the two internal checks of P1 (χ-isotypy of the expansion; `E v = 0` on the
programme's own `E`) catch it before the control is even reached.

## 2. Regimes

| regime | `n` | cell(s) | what is computed | purpose |
|---|---|---|---|---|
| R0 | 2, 3 | tiny shapes (`δ ≤ 4`, `r ≤ 4`) | brute-force Leibniz sum vs the determinant evaluator, random fillings, both primes | semantics + sign conventions of the evaluator |
| R1 | 3 | `((19,7,2^5), 12)` | sampled fillings; generic-point rank to `a = 6`; det-pencil rank; kernel `U_D`; exact C expansion of every basis filling into χ-coordinates; `E v = 0`; comparison with the banked vector | **the control** (Tasks 2, 3) |
| R2 | 3 | `((22,7,2^5), 13)`, `((25,7,2^5), 14)` | same as R1 without the banked comparison; `n_χ` by rebuild; expansion term count, evaluation cost, tableaux needed; the `k = 0` (disjoint tall columns) spanning test at `δ = 14` | the size curve (Task 4) |
| R3 | 4 | `((17,17,2^7), 12)`, `a = 2` | sampled fillings (every filling here has `≥ 6` letters shared by the two 9-columns); generic and det-pencil ranks at both primes; per-evaluation cost | the ladder bottom (Task 5) |
| R4 | 4 | LMR shape, one filling, one point | timing only | cost projection; **no carrier is built** |

Points: generic points are uniform random coefficient vectors mod `p`;
determinant points are `f = det_n(Σ s_i A_i)` with integer `A_i` drawn from
`random.Random(seed)`, reduced mod `p`, exactly as `wk9_s45_build.ev_rows_arr`
draws them. Ranks by `python-flint nmod_mat` at both house primes
`P1 = 2147483647`, `P2 = 2147483629`. A generic-point rank equal to the number
of fillings is a rigorous independence statement over `Q` (a mod-`p` rank is a
lower bound for the rank over `Q`); a det-point rank is a rigorous *lower*
bound on `mult_det` and, by the same logic as every session since 30, the
measured value up to the Schwartz–Zippel failure probability `≤ δ/p` per
vanishing.

## 3. Predictions with named falsifiers

**P1 (semantics).** For every filling used at R1/R2, the exact expansion
(Python-integer coefficients, C enumeration of the `(7!)^2·2^5 = 8.13×10^8`
terms) (a) has a coefficient that is constant times `sgn_m` on every kept
`Stab`-orbit and zero on every dropped orbit — i.e. lies in `V_χ` — and (b)
satisfies `E v = 0` exactly over `Z` on the programme's raising matrix from
`build_cell`. *Falsifier:* any orbit inconsistency or any nonzero entry of
`E v`. A failure here is a convention error and stops everything until it is
understood; a "fix" that is not a stated convention change is not a fix.

**P2 (spanning at `n = 3`).** Random column-strict fillings reach
generic-point rank `a = 6` at `((19,7,2^5),12)` within 30 samples.
*Falsifier:* rank `< 6` after 300 samples (would contradict Identity 2 and
mean a bug in the generator or evaluator).

**P3 (the exact control — the must-pass).** Restricted to six independent
fillings, the det-pencil evaluation has rank `5` at both primes, the kernel is
one-dimensional, and the χ-expansion of the kernel vector is **proportional
to the banked vector, entry by entry, all 17 047 entries**, mod `P1` and — after
rational reconstruction of the kernel coefficients — over `Z`. *Falsifier:*
kernel dimension `≠ 1`, or any entry outside proportionality. **Failure stops
the session at `n = 3`** (brief's first stopping rule); the report then says
what the circuit produced and how it differs.

**P4 (the whole space).** The six expansions are linearly independent as
χ-vectors (rank 6 of the `6 × 17047` matrix, both primes) and span the
coordinate-side `ker E` (dimension 6): every kernel vector of `E` computed on
the coordinate side is in their span. *Falsifier:* rank `< 6`, or a kernel
vector of `E` outside the span.

**P5 (size curve).** At `δ = 12, 13, 14`: fillings needed `= 6, 6, 6`; the
Leibniz term count per filling is constant at `8.13×10^8` (only `1`-columns
are added along the ladder); the evaluation cost per (filling, point) is
constant at `2^5·2^7 = 4096` determinants of size 7; `n_χ` grows from `17 047`
(by rebuild; `N_S` grows `1 155 302 → 1 165 249 → 1 167 156`, so the growth is
slow here — the `n = 3` ladder is already near saturation, and this is said in
the report rather than dressed up). `i_det = 1` at all three (ladder theorem:
`i_det` non-decreasing, `a` constant). *Falsifier:* fillings needed growing
with `δ`, or an expansion/evaluation cost that grows with `n_χ`. A
representation whose size grows like the carrier has not solved anything and
the report will say so with the numbers.

**P6 (which fillings suffice — no prediction, measured).** At `δ = 14`,
whether fillings with the two 7-columns on *disjoint* letter sets (`k = 0`)
already span `M_λ`. This is the structural datum that decides the LMR cost
projection (R4): with `k = 0` the double-column part is a single product of
two determinants per `2`-column pattern.

**P7 (`n = 4` ladder bottom).** Sampled fillings at `((17,17,2^7),12)` reach
generic rank `a = 2`; det-pencil rank `∈ {1, 2}` at both primes, the two
primes agreeing. *Expectation:* rank `2`, `i_det = 0` at the ladder bottom, by
analogy with the `n = 3` ladder (full rank at `δ = 9,10,11`, drop only at the
closing degree). A rank of `1` would be a highest-weight vector of weight
`(17,17,2^7)` in `I(D_9^{det_4})_{12}` — reported as **measured** with the
kernel vector, its fresh-point checks, and the standing caution that the
measurement alone gives `i_det ≤ 1`; it is not a `D > 0` event (the padded
side is not measured here) and does not invoke the `D > 0` protocol.
*Falsifier of the method:* generic rank `< 2` after 200 samples.

**P8 (cost projection, measured then extrapolated).** The measured
per-(filling, point) cost at R3 and R4, and from it the cost of the LMR block
by the circuit route: `≥ 274` fillings × `≥ 2·(274+8)` points × 2 primes. The
report states whether that is hours, days or out of reach in this container,
and what would change it (the answer to P6).

## 4. Stopping rules

1. P1 fails → stop; report the convention defect.
2. P3 fails → stop at `n = 3`; no `n = 4` work on a representation that does
   not reproduce a banked vector (brief).
3. Circuit size growing at carrier rate in `δ` (P5) → negative result; report
   the growth law and stop.
4. No full carrier is built at `n = 4` (brief); R4 is one filling at one point.
5. Every long run is bounded at launch (`timeout`, `ulimit -v`), pid under
   `results/logs/`; nothing over 5 MB is committed; single-writer files
   untouched; delivery by bundle.

## 5. Deliverables

`docs/compact_circuit.md` (the specification), `docs/s69_report.md`,
`results/s69_sizes.md` + `.jsonl`, `results/s69_control.json` (the comparison),
`results/artefacts/s69_*` (basis fillings and their χ-expansions at `n = 3`
compressed; the `n = 4` seed as fillings + coefficients + committed evaluation
values, with the conversion documented), code `analysis/wk11_s69_*.py` and
`analysis/wk11_s69_*.c`, logs `results/logs/s69_*`, bundle
`s69_circuit.bundle` + `.md5`.
