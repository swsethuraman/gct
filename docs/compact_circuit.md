# The compact circuit — highest-weight vectors as contractions (session 69)

This is the specification the brief asks for: the representation, its evaluation
semantics, its raising-operator action, and its conversion to the batch's
χ-coordinates — all stated before anything was computed (`results/PREREG_s69.md`
carries the same definitions in shorter form). Proofs are given where the
statement is proved; everything measured is in `docs/s69_report.md`.

## 1. Conventions (house)

`W = Sym^n C^r`, a form `f(s) = Σ_α f_α s^α` in `s_1..s_r`. `C[W]_δ =
Sym^δ(Sym^n C^r)` is the space of degree-`δ` polynomials in the coefficient
functionals `c_α`, `c_α(f) = f_α`. `GL_r` acts by substitution, `F ↦ F(f∘g)`;
its infinitesimal form on the `c_α` is the house rule

    E_{ij} c_α = (α_i + 1) c_{α + e_i − e_j},       torus weight of c_α = α,

which is the derivative along `s_i ↦ s_i + t s_j` (`wk8_s30_core`, session
30). A **highest-weight vector of weight `λ`** is `F ∈ C[W]_δ` with torus
weight `λ` and `E_{i,i+1} F = 0` for all `i`; equivalently `F(f∘u) = F(f)` for
every upper unitriangular `u`. `M_λ := HWV_λ(C[W]_δ)`, `dim M_λ = a(λ, δ)`.

**χ-coordinates** (`docs/stabiliser_reduction.md`, `wk9_s45_build.orbit_setup_arr`).
The weight-`λ` monomials `Π_k c_{A[m_k]}` (`m` a sorted `δ`-tuple of indices
into `A = exps(n, r)`) are permuted by `Stab_W(λ) = Π S_{k_b}`; every
highest-weight vector satisfies `P_w v = χ_λ(w) v`, so it lies in the span of
the χ-twisted orbit sums `Σ_{m∈O} sgn_m Π c`. A χ-vector `v ∈ Z^{n_χ}` is the
polynomial `Σ_j v_j Σ_{m∈O_j} sgn_m Π_k c_{A[m_k]}`; equivalently the
coefficient of the monomial `m` in it is `v_{col_of[m]} · sgn[m]`, zero on
dropped orbits.

## 2. The representation: bracket monomials

**Polarisation.** `f̃` is the symmetric `n`-linear form with `f̃(v,…,v) = f(v)`;
on basis vectors `f̃(e_{i_1},…,e_{i_n}) = (α!/n!) f_α`, `α` the multiplicity
vector of `(i_1..i_n)`. The **letter symbol** is `m_α := α! · c_α` (the
polarised coefficient times `n!`; the constant `n!^{−δ}` is dropped throughout).

**Fillings.** Let `λ ⊢ nδ` with conjugate `λ' = (h_1, …, h_{λ_1})`. A *filling*
`T` assigns to every cell of the diagram of `λ` one of `δ` letters so that each
letter is used exactly `n` times and no letter is used twice in a column. (Two
letters with the same set of cells are the same letter; letters are unlabelled
— `F_T` below is symmetric in them because every letter is the same `f`.)

**Definition.** For a filling `T`,

    F_T(f)  :=  Σ_{σ_1,…,σ_{λ_1}}  Π_{j=1}^{λ_1} sgn(σ_j)  ·  Π_{letters ℓ}  m_{α_ℓ(σ)}(f),

the sum over one bijection `σ_j : {rows of column j} → {1,…,h_j}` per column,
`sgn(σ_j)` the sign of `σ_j` as a permutation of the row order, and
`α_ℓ(σ) ∈ N^r` the multiplicity vector of the `n` indices `σ_{col(c)}(row(c))`
at the cells `c` of `ℓ`. In tensor language: one node `ε_{h_j} = e_1∧…∧e_{h_j}`
per column, one node `f̃` per letter, the cells as edges; `F_T = ⟨⊗_j ε_{h_j},
f̃^{⊗δ}⟩` with the slots matched by `T`.

**The LMR shapes.** `λ = (65, 17, 2^7)` has `λ' = (9, 9, 2^{15}, 1^{48})`; the
`n = 3` control `(19, 7, 2^5)` has `λ' = (7, 7, 2^5, 1^{12})`; the ladder
`λ_δ = (4δ − 31, 17, 2^7)` adds one `1`-column per degree. Every shape in this
session is `λ' = (h, h, 2^{n_2}, 1^{n_1})`: two *tall columns* `C_1, C_2`, `n_2`
*two-columns*, `n_1` *one-columns*, with `2h + 2n_2 + n_1 = nδ`. The `(2^9) +
(63,15)` of the brief is exactly this: the tall columns are the two `9×9`
brackets, the two long rows are the `2×2` brackets and the `e_1`-factors. In
this family a filling is the data

    C_1, C_2 : the h letters of each tall column in row order;
    two      : n_2 ordered pairs (letter in row 1, letter in row 2);
    one      : the n_1 letters of the one-columns,

with every letter used `n` times and no letter twice in `C_1`, in `C_2` or in
one pair (`wk11_s69_circuit.Filling`). Two rows of a tall column swapped is a
sign; the order of the two-columns and of the one-columns is irrelevant; the
`k := |C_1 ∩ C_2|` letters shared by the tall columns are the coupling between
the two `h×h` brackets.

## 3. The three identities

**Identity 1 (highest weight; proved).** `F_T ∈ M_λ` for every filling `T`.
*Proof.* For `g` upper unitriangular in the basis `e_i` (the action
`(f∘g)~(v_1..v_n) = f̃(gv_1, …, gv_n)`, `g e_k = e_k + Σ_{i<k} g_{ik} e_i`),
`g e_1 ∧ … ∧ g e_h = e_1 ∧ … ∧ e_h` because each `g e_k` differs from `e_k` by
vectors already in the wedge; so every column node is fixed and
`F_T(f∘g) = F_T(f)`. The torus acts on `f̃(e_{i_1},…)` by `Π t_{i_k}`, so the
weight of `F_T` is `Σ_j (1^{h_j}) = λ`. ∎

**Raising-operator action.** `E_{ij}` acts on a bracket monomial through the
same substitution rule as on the coordinates, and on the column nodes by
`E_{ij}(e_1∧…∧e_h) = Σ_k e_1∧…∧E_{ij}e_k∧…∧e_h = 0` for `i < j` (the only term
is `k = j`, which puts a second `e_i` into the wedge when `i ≤ h`, and vanishes
when `j > h`). So **every raising operator annihilates every bracket monomial;
this is the circuit's raising-operator action.** It is not assumed in the code:
the exact expansion of every filling used at `n = 3` is multiplied by the
programme's raising matrix `E` from `build_cell` and must give zero over `Z`
(`docs/s69_report.md`). The general (non-highest-weight) weight vectors of the
letterplace model — columns filled with arbitrary index sets `e_{i_1}∧…∧e_{i_h}`
— carry the nontrivial action `E_{ij}: e_j ↦ e_i` in each column; the
highest-weight vectors are the ones with the canonical column filling
`(1, …, h_j)`, and only those are used here.

**Identity 2 (spanning; classical).** The `F_T` span `M_λ`. *Proof sketch.*
In `V^{⊗nδ}` (`V = C^r`) the highest-weight vectors of weight `λ` are spanned
by the tensors `⊗_j (e_1∧…∧e_{h_j})` placed along the columns of a tableau of
shape `λ` (Schur–Weyl: they are the images of the column antisymmetrisers,
one per tableau, on `e_1^{⊗λ_1} ⊗ e_2^{⊗λ_2} ⊗ …`). `Sym^δ(Sym^n V)` is the image
of the symmetriser `Sym = Sym_δ ∘ Sym_n^{⊗δ}`, which is equivariant, so
`HWV_λ(Sym^δ Sym^n V) = Sym(HWV_λ(V^{⊗nδ}))`; and `⟨Sym(t), f^{⊗δ}⟩ = ⟨t,
Sym(f^{⊗δ})⟩ = ⟨t, f^{⊗δ}⟩` because the symmetriser is self-adjoint for the
pairing and fixes `f^{⊗δ}`. The pairing of the tableau tensor with `f^{⊗δ}`,
the tensor slots assigned to cells, is `F_T` for the filling `T` that records
which copy of `f` sits in each cell (up to the constant `n!^{δ}`). ∎ No
combinatorial *basis* is claimed; that would be a plethysm rule. Spanning is
verified numerically at every cell used: sampled fillings are evaluated at
generic points and the rank must reach `a(λ, δ)` from `a_weyl`.

**Identity 3 (evaluation; proved).** Fix an assignment `s ∈ {0,1}^{n_2}` of
indices to the two-columns (`s_e = 0`: row-1 letter gets index 1, row-2 letter
index 2; `s_e = 1`: swapped; sign `(−1)^{|s|}`), and index 1 to every
one-column. For a *row-unit* `k = 1..h` of `C_1` let `M_k` be the `h×h` matrix

    M_k(i, j) = m_{α}(ℓ_k with C_1-index i, C_2-index j, other legs by s)      if ℓ_k ∈ C_2 (shared),
    M_k(i, j) = m(ℓ_k; C_1-index i, …) · m(ℓ'_k; C_2-index j, …)               if ℓ_k ∉ C_2,

where the `C_1`-only letters are paired bijectively with the `C_2`-only letters
(`ℓ_k ↦ ℓ'_k`, any bijection; the code takes the one with the most two-columns
inside pairs), and let `N(s)` be the product of the symbols of the letters in
neither tall column. Let `π ∈ S_h` send the `C_1` row `k` to the `C_2` row of
its partner (`ℓ_k` itself if shared, `ℓ'_k` otherwise). Then

    F_T  =  sgn(π) · Σ_s (−1)^{|s|} N(s) · Σ_{S ⊆ [h]} (−1)^{h − |S|} det( Σ_{k∈S} M_k(s) ).

*Proof.* With `τ(k) := σ_2(π(k))`, `Π_ℓ m_{α_ℓ} = N(s) Π_k M_k(σ_1(k), τ(k))`
and `sgn(σ_2) = sgn(τ) sgn(π)`. The coefficient of `x_1⋯x_h` in
`det(Σ_k x_k M_k)` is `Σ_{σ,τ} sgn(σ) sgn(τ) Π_k M_k(σ(k), τ(k))` (expand the
determinant by the Leibniz rule, choose which `k` supplies each row, and
re-index by `k`), and for any polynomial of degree `≤ h` that coefficient is
`Σ_{S ⊆ [h]} (−1)^{h−|S|} P(1_S)`, since `Σ_{S ⊇ supp β} (−1)^{h−|S|} = [supp β
= [h]]`. ∎ This replaces `(h!)^2` permutation pairs by `2^h` determinants —
`128` at `n = 3`, `512` at `n = 4` — per two-column pattern, and every
determinant is taken exactly modulo the house primes. The three evaluators
(`brute_force_eval`, the literal definition; `fast_eval_py`; `fast_eval_c`) are
compared on random fillings of nineteen small shapes at both primes in regime
R0 (`results/s69_r0.json`).

## 4. Semantics, stated as procedures

**Evaluation at a point.** Input: a form `f` by its coefficients `f_α` (a
generic point: uniform residues mod `p`; a determinant point: `restrict` of
`det_n(Σ s_i A_i)` with integer `A_i`), a filling `T`, a prime `p`. Output:
`F_T(f) mod p` by Identity 3. Cost `2^{n_2} · 2^h · (h^3/3)` multiplications:
`4096` determinants of size 7 at the `n = 3` cells (about 3 ms in C), `2^{15}·512
= 1.7×10^7` determinants of size 9 at the `n = 4` ladder bottom (measured in the
report).

**Rank, kernel, ideal.** A set of fillings `T_1..T_t` and points `P_1..P_K`
give the `t × K` matrix `(F_{T_i}(P_j))`. Its rank over `F_p` at generic points
is a lower bound on the rank of `{F_{T_i}}` in `M_λ` over `Q` (so rank `= t`
proves independence over `Q`); reaching `a(λ, δ)` proves spanning. At
determinant points the rank is a lower bound on `mult_det`, and the left kernel
is the space of combinations vanishing at those points: `i_det = a − rank`
measured, with the same Schwartz–Zippel status as every evaluation-route
measurement in the programme (`docs/randomised_protocol.md`). The kernel vector
`x` gives `U_D = Σ x_i F_{T_i}` **as a circuit**: `t` fillings and `t`
coefficients.

**Conversion to χ-coordinates (the expansion).** `F_T = Σ_σ Π_j sgn(σ_j) Π_ℓ
α_ℓ(σ)! · Π_ℓ c_{α_ℓ(σ)}` is a sum over `Π_j h_j!` index assignments, each
contributing one weight-`λ` monomial with integer coefficient `± Π_ℓ α_ℓ!`;
collecting terms gives the monomial expansion, and `v_{col_of[m]} = coef[m] ·
sgn[m]` (asserted constant on every kept orbit and zero on every dropped
orbit) gives the χ-vector. `analysis/wk11_s69_expand.c` does this literally,
in 128-bit integers, looking each monomial up by the house combinadic code:
`(7!)^2 · 2^5 = 8.13×10^8` terms per filling at the `n = 3` cells (constant
along the ladder — added one-columns are fixed indices), measured at about a
minute per filling. At `n = 4` the same count is `(9!)^2 · 2^{15} = 4.3×10^{15}`
per filling; the literal expansion is not available there, and §6 says what is.

## 5. Why this is the same object, and the pre-checks

`brief_wording` §7 asks whether a proposed invariant is functorial under
closed immersion. Nothing new is proposed: `F_T` is an element of `M_λ ⊂
C[W]_δ`, the coordinate ring's degree-`δ` piece, written as a contraction. The
statistic is still `mult_λ C[D]_δ = rank(M_λ → C^{D-points})`, still
functorial by `P ⊆ D ⟹ I(D) ⊆ I(P) ⟹ C[D] ↠ C[P]`, and the circuit changes
only how a vector of `M_λ` is *stored and evaluated*. The one way it could be
a different vector of the same weight is a convention error — the `α!`
weights, a sign, the identification of `c_α` — and that is what the exact
`n = 3` control, the χ-isotypy assertion, the `E v = 0` check and the
evaluator-versus-expander comparison are for. §5 of `brief_wording` (the
degeneracy direction) does not apply: no new statistic is introduced.

## 6. What the circuit does not do cheaply (stated precisely)

* **Coordinates at `n = 4`.** The literal expansion is `(9!)^2 2^{15}` terms per
  filling. The alternatives are (a) a Grassmann/exterior-algebra expansion with
  polynomial coefficients — its intermediate states are partial products over
  subsets of letters whose monomial supports are not bounded by the final `n_χ`;
  (b) a per-monomial coefficient oracle (`⟨F_T, m⟩` as a signed count of index
  assignments), which is a streaming build of exactly the kind session 63 named
  as the only opening, and whose per-monomial cost is not yet priced. Neither is
  built here. A vector of `M_λ` at `n = 4` is therefore handed over as fillings
  + coefficients + committed evaluation values at named points, with this
  conversion documented, not as an `n_χ`-vector.
* **A basis.** The circuit gives spanning sets and verifies independence by
  evaluation; it does not give a combinatorial basis (no plethysm rule is
  claimed). The number of sampled fillings needed to reach rank `a` is a
  measured quantity (`results/s69_sizes.md`).
* **Cheap evaluation for every filling.** The evaluation cost is `2^{n_2}`
  two-column patterns times `2^h` determinants; the `2^{n_2}` factor is the
  price of the coupling between the two long rows and the tall columns. At the
  ladder bottom every filling has `k ≥ 6` shared letters and `n_2 = 15`; up the
  ladder `n_2` stays `15` while `n_1` grows, so the per-evaluation cost is
  constant in `δ` and the number of fillings grows like `a_δ` (`2 → 274`).
