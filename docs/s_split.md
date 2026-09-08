# The reducible-normalisation split `S`, written out — and why it is source-dependent

Session 70 (C3), branch `s70-tworanks` off `226b4ef1`. The object the batch-11
brief and session 64 §7 name `S_{λ,δ}`, written down for the first time: its
definition, the identity `rank S = mult_red`, its exact implementation
(`analysis/wk11_s70_split.py`, calibrated at three `n=4` cells), and the
determination the brief asks for in Part A — **does `rank S_{λ,24}` need the
explicit source?** Labels: **proved** / **measured** / **adopted**.

## 1. The map

`V = C^r`, `W = Sym⁴V^*`, `R_r = {ℓ·c : ℓ ∈ V^*, c ∈ Sym³V^*} ⊆ W` the reducible
locus. Its coordinate-ring map is the pullback of the multiplication
`μ : V^* × Sym³V^* → W`, `(ℓ,c) ↦ ℓ·c`:

    μ* : C[W] → C[V^*] ⊗ C[Sym³V^*],   degree δ ↦ Sym^δ V ⊗ Sym^δ(Sym³V) =: D_δ,

with `im(μ*_δ) = C[R_r]_δ` and `ker(μ*_δ) = I(R_r)_δ`. On the coefficient
generators `c_α` (`|α| = 4`), reading off the coefficient of `x^α` in `ℓ·c`,

> **`μ*(c_α) = Σ_{i : α_i ≥ 1} y_i ⊗ d_{α − e_i}`**,   `y_i` the linear
> coordinates (a basis of `V`), `d_β` the cubic coordinates (`|β| = 3`),

extended as a ring homomorphism: for a degree-`δ` monomial `∏_{j=1}^{δ} c_{α^j}`,

    μ*(∏_j c_{α^j}) = ∏_j (Σ_{i} y_i ⊗ d_{α^j − e_i})
                    = Σ_{(i_1,…,i_δ)}  y^γ ⊗ ∏_j d_{α^j − e_{i_j}} ,   γ = Σ_j e_{i_j}.

This is exactly the **symbolic** form of the programme's own reducible evaluation
`red_coeffs` (`wk9_s60_cell`: `out[α] += ℓ_i · c_{α−e_i}`) — the split with the
point `(ℓ,c)` kept indeterminate instead of numeric.

**`S = S_{λ,δ}`** is `μ*_δ` restricted to the `λ`-highest-weight space:

    S : M⁴_λ := HWV_λ(Sym^δ Sym⁴V) ⟶ HWV_λ(D_δ) = ⊕_μ M³_μ ,

`dim M⁴_λ = a` (the quartic plethysm), `dim ⊕_μ M³_μ = h_pad` (§2). At LMR
`a = 274`, `h_pad = 521`: the `274 × 521` split.

## 2. The target is `⊕_μ M³_μ` — the Pieri shapes, source-free *(proved)*

`D_δ = Sym^δ V ⊗ Sym^δ(Sym³V)`. By Pieri (`Sym^δ V = S_{(δ)}V`),

    HWV_λ(D_δ) = ⊕_{μ : λ/μ a horizontal δ-strip}  M³_μ ,
    M³_μ := HWV_μ(Sym^δ Sym³V),   dim M³_μ = a₃(μ,δ),

so `dim = Σ_μ a₃(μ,δ) = h_pad(λ,δ)` — the **session-42 normalisation identity**
(`wk9_s42_hpad.py`, `docs/reducible_engine.md` §B; Kempf collapsing:
`H⁰(Z,O_Z) = ⊕_δ Sym^δV ⊗ Sym^δSym³V` is the Segre-product ring, the
normalisation of `C[R_r]`). The shapes `μ` and the cubic multiplicities `a₃(μ,δ)`
are combinatorial functions of `λ, δ` — **no quartic monomial ever enters the
target.** At LMR the work list is the **48** Pieri strips of `(65,17,2⁷)` at
`δ = 24` (`wk9_s42_hpad.pieri_strips`), each an `Sym³` block strictly smaller than
the `Sym⁴` source.

## 3. `rank S = mult_red` *(proved)*

`μ*_δ` is `GL(V)`-equivariant, so it carries the `λ`-isotypic component of `C[W]_δ`
to that of `D_δ`, and by Schur's lemma the induced map on multiplicity spaces
`S : C^a → C^{h_pad}` has

    rank S = mult_λ(im μ*_δ) = mult_λ C[R_r]_δ = mult_red ,
    ker S = mult_λ I(R_r)_δ,   i_red = a − rank S.   ∎

Concretely: the `a` vectors `μ*(v_1),…,μ*(v_a)` (`{v_j}` an HWV basis of `M⁴_λ`)
are highest-weight vectors of weight `λ` in `D_δ`; their span's dimension, read in
any basis of `D_δ`, is `mult_red`. The implementation ranks them in the
monomial basis `{y^γ ⊗ ∏ d_β}` of `D_δ`.

This is the `S` stage of session 64 §7's factorization
`M⁴_λ →^S ⊕_μ M³_μ →^{⊕Θ} ⊕_μ M³_μ/ker Θ^{per₃}`, whose composite has
`rank[(⊕Θ)∘S] = mult_pad`. `rank S = mult_red` is the universal
reducible-normalisation stage; `mult_pad ≤ mult_red` always, with equality at
`r ≤ 5` (`P_r = R_r`, washout Thm 2 / s64).

## 4. The implementation *(measured, calibrated)*

`analysis/wk11_s70_split.py`:

1. **Domain HWVs** `{v_j}` = kernel of the raising operators `E` on the
   `χ_λ`-isotypic carrier (`wk9_s45_build.build_cell`, `wk9_s60_cell.kernel_dense`;
   `nullity = a` asserted `= a_weyl`, every vector verified `E·v = 0` on the full
   sparse `E`). Expanded to monomial coordinates by `coeff(m) = kern[col_of[m]]·sgn[m]`.
2. **`μ*`** by the exact formula of §1, vectorised (`explode`): the full
   product-of-sums over the `δ` factors of every weight-`λ` monomial, ~30–36 M
   terms in ~13 s. The linear multidegree `γ` is packed exactly (base `δ+1`); the
   cubic multiset is an additive 63-bit multiset hash, run at **two independent
   seeds** (a collision can only merge codomain columns, i.e. only *lower* rank).
3. **Rank** of the `a × (#codomain monomials)` matrix `W·T` (`W` the HWV
   coefficients, `T` the `μ*` incidence) over each house prime, by `python-flint`.

Cross-checks, all required to agree and to equal the banked `mult_red`: both
primes; both hash seeds; the `(★)/E_red` route `rank kern[:,¬red]`
(`docs/reducible_ideal.md` Thm 1) on the **same** HWVs — an independent route to
`mult_red`; and `a_weyl = nullity(E)`.

**Result** (`results/s70_ranks.md`, `.jsonl`; `results/certs/s70/`):

| λ, δ | a | h_pad | rank S | i_red | banked | (★) | role |
|---|---|---|---|---|---|---|---|
| (10,6,4,2,2), 6 | 6 | 24 | **6** | 0 | 6 | 6 | full-rank control |
| (8,4,4,4,4), 6 | 2 | 1 | **1** | 1 | 1 | 1 | bite |
| (12,9,9,1,1), 8 | 7 | 6 | **5** | 2 | 5 | 5 | bite |

Two-sided: full rank where `mult_red = a`, the correct drop at each bite; every
number matches across primes, seeds, the `(★)` route and the banked record.

## 5. Part A — the determination: `rank S` is **source-dependent** *(proved)*

**Question.** `det A₂₄` needs the explicit source. Does `rank S_{λ,24}`? The
brief's conditional: *if `S`'s rows are the Pieri shapes and its columns the
ambient multiplicity **abstractly** (not explicit source vectors), then `S` is
computable from `λ,δ` alone and the LMR half is ungated.*

**Answer: the antecedent fails; `rank S` is source-dependent, exactly as
`det A₂₄` is.** The rows/target (§2) and the map `μ*` (§1) are source-free, but
the **columns are a basis of `M⁴_λ = HWV_λ(Sym^δ Sym⁴V)`, the `a`-dimensional
quartic source, and there is no basis of that space that is not explicit source
vectors.** Three independent grounds:

1. **No abstract column basis carries `μ*`.** To fill column `j` you must apply
   `μ*` to the `j`-th source vector, and `μ*` (§1) acts on the *realisation* of
   that vector as a polynomial in the `c_α` (equivalently, on its `χ_λ`-carrier
   coordinates). The "ambient multiplicity" `M⁴_λ` is an `a`-dimensional space
   with **no canonical basis** and no combinatorial model on which `μ*` has a
   known rule; any handle on a specific vector of it *is* an explicit quartic
   HWV. (Contrast the target: `⊕_μ M³_μ` has the canonical Pieri/cubic basis.)

2. **A source-free matrix would make `mult_red` a closed form — false.** If the
   *matrix* `S` were writable from `λ,δ` alone, then `rank S = mult_red` would be
   a function of `λ,δ`. It is not: s42 §B **proves** `h_pad − mult_red =
   mult_λ(D_δ/C[R_r]_δ)` is the multiplicity of the normalisation quotient,
   supported on the non-normal locus `{ℓℓ'q} ∪ {ℓ²q}`, and "computing it is
   exactly the original problem — the image of `A` in `D`"; and s60 **measured**
   eight `r=5` cells with `mult_red < min(a,h_pad)` by amounts (`1,1,1,1,2,2,4,…`)
   with no combinatorial law. A source-free `S`-matrix cannot exist without
   contradicting both.

   The one thing that *is* free is the embedding `M⁴_λ ↪ Sym^δ(V⊗Sym³V)` (via
   `Sym^δ` of the split), whose `λ`-isotypic image sits inside the source-free
   Cauchy space `⊕_{π⊢δ} S_πV ⊗ S_π(Sym³V)`; but pinning that image *is* locating
   the quartic plethysm inside the Cauchy expansion — the source realisation
   again, no cheaper.

3. **s64 §7 says so, from the other side.** The factorized route's `ev_pad` fast
   branch "is gated on the **same wall** (building/evaluating the common source at
   `r=9, δ=24`)"; its 48-block advantage is on the **target**, not the source.

**Consequence.** At LMR, `M⁴_λ` is precisely the object session 63 measured
walled on all three realisations: native HWV build `N_S = 1.56·10¹¹` (14.4 TB),
Foulkes column `1.2·10⁹³`, Gram/Schur `|S| ≥ 6·10⁶` (the `χ_λ`-carrier,
`n_χ ~ 3.1·10⁷`, `u`-free slice `~1.4·10⁶`; `docs/lmr_cell.md` §6). So the LMR
`274 × 521` rank is **gated on the same source as `det A₂₄`**, no source lands
(carrier build forbidden, s63 wall), and the batch's ungated half is the `n=4`
calibration of §4. The construction is exact and reusable: when a streaming
orbit-rep source engine reaches `r=9, δ=24` (s63's reserve-class opening),
`S` computes `mult_red = rank S` at LMR with the PREREG §0 semantics attached.

## 6. What `S` is not

`S` is **not** the LMR carrier-space engine (the `E_red`/`ev_red` nullity on the
`χ_λ`-carrier) that s63 measured dead on all three realisations — that computes
`i_red` on the same source. `S` computes `rank = mult_red` on the *image* side,
into the normalisation `D_δ`; the two share only the domain HWVs, and their
agreement at §4's three cells is a genuine check of the split identity
`rank S = mult_red` (which s64 §7 flagged "unchecked and unbanked" for the
composite `(⊕Θ)∘S`). Both are gated at LMR by the same quartic source.
