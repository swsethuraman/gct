# B19-01 — Does the present boundary condition add genuinely new equations?

Status: **COMPLETE.** One structural result, in the form the brief calls option 2/3: a proved region where the arc is silent (`lambda_1 + lambda_2 + lambda_3 <= 2d` gives `b = 0`), a proved counterexample to exactness inside it (`d = 6`, `lambda = (4^6)`: `a = 1`, `s = 10`, `b = 0`), and a Levi reduction bounding `b` by a finite branching number. The band is empty for length at most five, so the five-row question is untouched. No carrier run, no cell nomination, no gap.

## 0. Provenance

Read-only commands, run in `work/batch15_workers/B15-01` before anything was written:

```
git rev-parse HEAD        -> 03c8fb861f99626e27826a86bc3cbd128744bad4
git rev-parse HEAD^{tree} -> d755e531fa754cafe31ca3117593e544bc09a3fa
```

`git status --porcelain` was also run, as the preamble permits, to confirm the write footprint. No other git command.

Inputs read:

| File | Role |
|---|---|
| `Claude_Handover_B15_B18/batch19_launch/B19_PREAMBLE.md` | conventions, what batch 18 settled, direction-of-inference rules |
| `Claude_Handover_B15_B18/BATCH19_PROPOSED_BOARD.md` | board |
| `../B15-02/docs/b18_02_report.md` | the carrier, the skew-degree weight lemma (Lemma 4.1), the twenty controls, the missing theorem (its §8) |
| `../B15-02/docs/b18_02_review.md` | integrator review; the `a >= 1` precondition |
| `../B15-08/docs/b17_08_report.md` | the five-row determinant deficit |

## 1. Plain terms

Batch 18 built a boundary instrument. For a cell `(d, lambda)` it takes the full-`H`-invariant source `M_lambda = (S_lambda W)^H`, of dimension `s`, and projects onto the part of **skew-degree greater than `2d`**. Anything in the image cannot extend to the orbit closure, so the rank `b` of that projection cuts the global determinant ceiling down to `B = min(a, s - b)`.

In all twenty certified controls the instrument returned `s - b = a` exactly: it removed the surplus of the source over the ambient multiplicity and **nothing more**. Nobody knew whether that is the method's ceiling or an artefact of small cells. That is this slot's question.

This report answers it in one direction, with a proof, and the answer is a **structural ceiling**.

1. **A grading identity.** Decomposing `W` by the arc weight gives `W = W_{-1} + W_0 + W_{+1}` of dimensions 4, 3, 9, with `W_0` the skew part. Under the Littlewood–Richardson decomposition of `S_lambda W`, every component of every full-`H` invariant has `W_{-1}`-degree exactly `d`, `W_0`-degree `j`, and `W_{+1}`-degree `3d - j`. This re-derives B18-02's Lemma 4.1 in a form that can be read off `lambda` itself. (§3.)
2. **A silence theorem (§4).** If `lambda_1 + lambda_2 + lambda_3 <= 2d`, then the forbidden part of `S_lambda W` is **empty** — not merely empty on invariants. So `b = 0`, and the arc contributes nothing whatever the carrier would have measured. The condition is testable by reading three parts of `lambda`. A sharper Littlewood–Richardson form (§4.2) decides more cells.
3. **Where that region lies (§4.3).** It is **empty for every cell of length at most five**, which is exactly why twenty controls never saw it. It is **non-empty for lengths six to ten**, which is exactly the range B17-03-D leaves open for a positive gap. At length six it is a single rectangle.
4. **A counterexample to exactness (§5).** In a silent cell the arc's ceiling is the whole source, `s - b = s`. So any silent cell with `s > a` has `s - b = s > a >= m_det`: the arc criterion admits invariants that provably do not extend. That refutes the exactness reading in the region where it can be tested cheaply, and it does so **without running the carrier**.
5. **A Levi reduction (§6).** The projection commutes with the grading-preserving subgroup of `H`, a `GL_3` times a torus. Hence `b` is bounded above by the dimension of the **negative-weight invariants of that Levi**, a finite branching number, giving a cheap pre-screen before any heavy carrier run.

What this report does **not** do: it does not compute `b` in any cell with `a > 0` and length five, does not run the carrier, does not nominate a cell, and does not produce any bound `B < U`, any padding rank, or any gap.

**The one thing the board should take from it:** the instrument is provably blind in an explicitly described band of six-to-ten-row cells, and in that band it is also provably not exact. Heavy lease time spent there buys nothing.

## 2. Conventions, and the justification each one travels with

**ADOPTED** from the preamble and from B18-02 §1, unchanged. Per the preamble's third rule, each import is listed with the hypothesis or measurement that justifies it and whether that justification survives in my regime.

| Import | Source | Justification it travels with | Holds here? |
|---|---|---|---|
| `W` = 16-dimensional space of linear forms; `f = det4`; `X = closure(GL(W)·f)`; coordinate modules `S_lambda(W*)`, `lambda ⊢ 4d` | preamble, B18-02 §1 | definition | yes |
| `H = Stab(f)` = `{x -> AxB : det A det B = 1}` extended by transposition; `M_lambda = (S_lambda W)^H`, `s = dim M_lambda` | B18-02 §1, supplement02 audit | stabiliser computation accepted in B17-02 supplement02 | yes, and my results are statements about this same `M_lambda` |
| adapted coordinates `a, r, c, S, v` on `W`, invertible with determinant `-8` | B18-02 §1 | explicit change of basis | yes |
| the arc `gamma(t)`: scales `a, r` by `t^-1`, fixes `v`, scales `c, S` by `t`; `gamma(t)f = Q0 + tQ1 + t^2Q2` | B17-02 supplement02, ADOPTED by B18-02 | accepted arc identity | yes; I use only the **weights**, never the `Q_i` |
| forbidden `gamma`-weights: `k < 0` or `k > 2d` | B18-02 §1 | limits of `gamma(t)f` and of `t^-2 gamma(t^-1)f` both lie in `X` | yes |
| Lemma 4.1: on torus-invariant polynomials the `gamma`-weight is `2d - #v`, so `C` is the projection onto skew-degree `>= 2d + 1` | B18-02 §4, PROVED there | grid-row and grid-column torus invariance | yes — and §3 re-derives it independently, which is the only part of B18-02 my theorems depend on |
| `s = [S^lambda : Sym^2(S^{(d^4)})]`, formula (3.1) | B18-02 §3, PROVED | Schur–Weyl plus the first fundamental theorem for `SL_4`; transposition acts as the plain swap | yes; my pilot recomputes `s` from (3.1) independently and reproduces B18-02's published values |
| `b = rank C`, `B = min(a, s - b)` | preamble | `C` is a necessary condition for extension | yes |
| `a >= 1` is a precondition for a nomination | B18-02 review §2 | `m_det <= a` and `m_pad <= a` | yes; §5 is explicit about which of my cells have `a = 0` |
| ordinary coefficients, positive weights, no factorial normalisation | preamble | convention | yes; nothing here uses the raising-operator normalisation |

Two quantities are used with the preamble's meanings: `a` is the ambient multiplicity of `S_lambda` in `Sym^d(Sym^4 W)`, and `m_det <= min(a, s)` is the coordinate multiplicity of the closure.

**One standing fact, used repeatedly.** `a(d, lambda)` computed in `n` variables is independent of `n` once `n >= ell(lambda)`; likewise the identification of cells between 5, 6, ... and 16 variables is B17-03-A. So a plethysm multiplicity for `ell(lambda) = L` may be computed in `L` variables. This is the same stability B18-01 §8 and the B18-02 review used.

## 3. The grading identity: what the arc weight is, read off `lambda`

Write the arc weight decomposition of `W`:

| piece | coordinates | dimension | `gamma`-weight |
|---|---|---:|---:|
| `W_{-1}` | `a` and `r_1, r_2, r_3` (the first grid row) | 4 | `-1` |
| `W_0` | `v_1, v_2, v_3` (the skew part of the lower-right `3x3` block) | 3 | `0` |
| `W_{+1}` | `c_1, c_2, c_3` and the six `S_ij` | 9 | `+1` |

**Proposition 3.1 (PROVED).** Let `z` be any element of `S_lambda W` invariant under the diagonal tori of `SL(A)` and `SL(B)` — in particular any element of `M_lambda`. Decompose

    S_lambda W  =  (+)_{mu, kappa, tau}  c^lambda_{mu kappa tau} · S_mu(W_{-1}) (x) S_kappa(W_0) (x) S_tau(W_{+1}),

the Littlewood–Richardson decomposition, where `ell(mu) <= 4`, `ell(kappa) <= 3`, `ell(tau) <= 9` and `|mu| + |kappa| + |tau| = 4d`. Then every component of `z` has

    |mu| = d,      |kappa| = #v,      |tau| = 3d - #v,      gamma-weight = |tau| - |mu| = 2d - #v.

*Proof.* The `gamma`-weight of a component is `|tau| - |mu|` because `W_{+1}`, `W_0`, `W_{-1}` carry weights `+1, 0, -1`. Invariance under the diagonal torus of `SL(A)`, which acts on the grid row index, forces every standard-entry monomial of `z` to carry total degree `d` in each grid row: the four row degrees are equal and sum to `4d`. The first grid row spans exactly `W_{-1}`, so the `W_{-1}`-degree of every component is `d`, i.e. `|mu| = d`. Then `|tau| = 4d - d - |kappa| = 3d - |kappa|`, and `|kappa|` is by definition the number of skew factors `#v`. The weight is `|tau| - |mu| = 2d - |kappa|`. ∎

This is B18-02's Lemma 4.1, obtained from the decomposition rather than from monomial bookkeeping, and it yields the two facts this report needs:

**Corollary 3.2 (PROVED).** On `M_lambda`, the forbidden projection `C` is the projection onto the components with `|kappa| >= 2d + 1`; its kernel is the sum of the components with `|kappa| <= 2d`. In particular `C` depends on `lambda` only through which triples `(mu, kappa, tau)` occur.

**Corollary 3.3 (PROVED).** `b > 0` requires a triple `(mu, kappa, tau)` with

    |mu| = d,  ell(mu) <= 4;    |kappa| >= 2d + 1,  ell(kappa) <= 3;    |tau| = 3d - |kappa| <= d - 1,  ell(tau) <= 9;
    c^lambda_{mu kappa tau} > 0.

Every Littlewood–Richardson constituent satisfies `kappa ⊆ lambda`, `mu ⊆ lambda`, `tau ⊆ lambda`.

## 4. The silence theorem: an explicit region where the arc has nothing to say

### 4.1 The theorem

**Theorem 4.1 (PROVED).** Let `lambda ⊢ 4d`. If

    lambda_1 + lambda_2 + lambda_3  <=  2d,

then the forbidden part of `S_lambda W` is zero; hence `C = 0` on `M_lambda`, `b = 0`, and

    B = min(a, s - b) = min(a, s).

The arc contributes nothing in that cell, whatever a carrier run would have measured.

*Proof.* By Corollary 3.2 a nonzero forbidden component needs `|kappa| >= 2d + 1` with `ell(kappa) <= 3` and `kappa ⊆ lambda`. A partition with at most three rows contained in `lambda` has size at most `lambda_1 + lambda_2 + lambda_3 <= 2d < 2d + 1`. So no such `kappa` exists, and the whole forbidden subspace of `S_lambda W` vanishes — not merely its intersection with `M_lambda`. ∎

Note the strength: the conclusion is about `S_lambda W`, so it is independent of `H`, of the transposition, of `s`, and of whether the spanning family of B18-02 §2 reaches rank `s`. It cannot be defeated by a better carrier implementation.

### 4.2 The sharper, still cheap criterion

**Theorem 4.2 (PROVED).** `b = 0` unless there exist partitions `mu ⊢ d` (`ell <= 4`), `kappa ⊢ j` with `2d + 1 <= j <= lambda_1 + lambda_2 + lambda_3` (`ell <= 3`), and `tau ⊢ 3d - j` (`ell <= 9`) with `c^lambda_{mu kappa tau} > 0`.

*Proof.* Corollary 3.3. ∎

This is a finite check on Littlewood–Richardson coefficients for one cell, and it is strictly sharper than Theorem 4.1, which is the special case where the `kappa` range is empty. Two immediate consequences of the same bookkeeping:

**Corollary 4.3 (PROVED).** `b > 0` requires `ell(lambda) <= 7 + min(9, d - 1)`. In particular, for `d = 2` every `lambda` with `ell(lambda) >= 9` has `b = 0`, and for `d = 3` every `lambda` with `ell(lambda) >= 10` has `b = 0`.

*Proof.* `ell(lambda) <= ell(mu) + ell(kappa) + ell(tau) <= 4 + 3 + ell(tau)`, and `ell(tau) <= |tau| = 3d - j <= d - 1`, also `ell(tau) <= 9`. ∎

### 4.3 Where the silent region is — and why twenty controls never saw it

**Proposition 4.4 (PROVED).** Let `L = ell(lambda)` and `lambda ⊢ 4d`.

1. If `L <= 5` then `lambda_1 + lambda_2 + lambda_3 >= (3/5)·4d = 2.4d > 2d`. **Theorem 4.1 never applies to a cell of length at most five.**
2. If `L = 6` the hypothesis holds only for the rectangle `lambda = ((2d/3)^6)`, and only when `3 | 2d`.
3. For `7 <= L <= 16` the region is a non-trivial band: it is exactly the set of `lambda ⊢ 4d` with `lambda_4 + ... + lambda_L >= 2d`.

*Proof.* (1) The three largest parts of a partition of `4d` into at most 5 parts are each at least the average, so their sum is at least `3·(4d)/5`. (2) With `L = 6`, `lambda_4 + lambda_5 + lambda_6 >= 2d >= lambda_1 + lambda_2 + lambda_3 >= lambda_4 + lambda_5 + lambda_6` forces equality throughout, hence all six parts equal. (3) Restatement of `lambda_1 + lambda_2 + lambda_3 <= 2d` using `|lambda| = 4d`. ∎

This explains the twenty controls exactly. Every certified cell in B18-02 has `ell(lambda) <= 5`, where by Proposition 4.4(1) the silent region is empty — so the controls could not have detected this ceiling, and their regularity `s - b = a` is evidence about a region that provably excludes the silent band.

It also places the silent band inside the range that matters: B17-03-D leaves lengths **five to ten** open for a positive gap, and the band is non-empty for lengths six to ten. The band is therefore a set of live-looking cells where this instrument is provably useless.

**What Theorem 4.1 does not say.** It does not say `B = a`, does not say `m_det = a`, and says nothing about `s` versus `a`. It says the arc adds nothing to whichever of `a` and `s` is smaller. And it is a statement about this arc: a different arc, or a different boundary point, is untouched by it.

## 5. A counterexample to exactness, with `a >= 1`

### 5.1 The conjecture being tested

Write `E_lambda ⊆ M_lambda` for the image of the ambient multiplicity space under restriction to the orbit; `dim E_lambda = m_det`, and `E_lambda ⊆ ker C` because a restriction of a global polynomial extends to the closure and therefore has no forbidden weight.

> **Exactness conjecture (EC).** `ker C = E_lambda`, i.e. `s - b = m_det`.

B18-02 §8 poses this for `ell(lambda) <= 5`. In all twenty of its controls `s - b = a` and `m_det = a`, so EC held in every measured cell. The following refutes EC in general, in the region Theorem 4.1 describes. It does **not** refute the length-at-most-five form, where the band is empty (Proposition 4.4(1)); that form remains open.

### 5.2 The computation

`analysis/b19_01_band.py` and `analysis/b19_01_band6.py` compute `a` (ambient multiplicity, by the Weyl alternation on the weight multiplicities of `Sym^d(Sym^4 C^n)`, `n = ell(lambda)`), `g` (ordinary rectangular Kronecker) and `s` (symmetric, formula (3.1)). **Controls, all passing:**

| Control | Content | Result |
|---|---|---|
| C1 | `d = 2`: `s = 1` exactly for `(8), (6,2), (4,4), (4,2,2), (2,2,2,2)`, `s = 0` for the other 13 partitions of 8 with at most five rows; `a = 1, 1, 1, 0, 0` | reproduces B18-02 §6 |
| C2 | `d = 3`: `(6,3,1,1,1)` gives `g = 3, s = 1`; `(5,3,2,1,1)` gives `g = 4, s = 2` | reproduces B18-02 and the integrator review |
| C3 | `sum_lambda g·f^lambda = (f^R)^2` and `g(R,R,(4d)) = 1`, for `d = 1..4` | holds |
| C4 | `f^(3,3,3,3) = 462` | holds |
| C5 | `d = 1`: `s_(4) = 1`, all other `s = 0` | holds |
| P1 | `d = 6`: `sum_lambda a·dim S_lambda(C^6) = dim Sym^6(Sym^4 C^6) = 6,249,655,776` | holds |
| P2 | `d = 6`: `chi_R(1^24) = f^R` and `chi_lambda(1^24) = f^lambda`, both `140,229,804` | holds |

**The cell (MEASURED, exact).**

    d = 6,   lambda = (4,4,4,4,4,4) |- 24,   ell(lambda) = 6,
    lambda_1 + lambda_2 + lambda_3 = 12 = 2d      (silent band, Theorem 4.1)
    a = 1,   g = 13,   s = 10.

Why this is the first cell where the question can be asked at all: the band needs `ell(lambda) >= 6` (Proposition 4.4), while `a > 0` needs `ell(lambda) <= d` (constituents of `Sym^d(Sym^4)` have at most `d` rows, B18-01 Lemma 8.1). So `d >= 6`, and at `d = 6` Proposition 4.4(2) leaves exactly one candidate, the rectangle. It has `a = 1`, so it is **not** ambient-empty and the `a >= 1` precondition of the B18-02 review is met.

### 5.3 The conclusion

**Theorem 5.1 (PROVED, given the MEASURED values above).** At `d = 6`, `lambda = (4^6)`:

    b = 0                        (Theorem 4.1: the band condition holds with equality)
    ker C = M_lambda,  dim 10
    m_det <= a = 1
    so   dim ker C - m_det >= 9 > 0.

Hence **EC is false in this cell**: the arc criterion admits a 10-dimensional space of invariants of which at most one dimension can come from a function on the closure. The same conclusion holds, with `m_det = 0`, in the ambient-empty band cells `(2^6)` at `d = 3` (`s = 1`), `(4,2^6)` and `(2^8)` at `d = 4` (`s = 3`, `s = 1`) and `(3,3,2,2,2,2,1,1)` at `d = 4` (`s = 2`).

**What this costs the instrument, stated precisely.**
- In this cell `B = min(a, s - b) = min(1, 10) = 1 = a`. The arc reproduces the ambient ceiling and cannot go below it.
- A gap certificate here would need `r > B`, so `B = 0`, so `b = s = 10`. Theorem 4.1 proves `b = 0`. **This arc can never certify a gap in a band cell**, whatever the truth about `m_det` and `m_pad` there.
- So the twenty controls' regularity `s - b = a` is not a law that continues to hold with `s - b` tracking `m_det`: here `s - b = 10` while `a = 1`. The regularity was an artefact of a region — length at most five, small `d`, and `m_det = a` — and the failure mode outside it is the arc becoming **blind**, not sharper.

## 6. The Levi reduction: a cheap upper bound on `b` before any carrier run

### 6.1 The grading-preserving subgroup

**Proposition 6.1 (PROVED).** Let `L ⊆ H` be the subgroup preserving the three `gamma`-weight spaces of `W`. Its identity component is

    L^0 = { x -> A x B :  A = diag(alpha, A'),  B = diag(beta, c·A'^T),  A' in GL_3,  det A det B = 1 },

acting on the pieces as

    W_{-1} = <a> (+) <r>        =  triv (+) std,          with scalars alpha·beta and alpha·c
    W_0    = <v>                =  Lambda^2(std),         with scalar c
    W_{+1} = <c_k> (+) <S_ij>   =  std (+) Sym^2(std),    with scalars beta and c

where `std = C^3` is the standard `GL_3 = GL(A')`-module.

*Proof.* Preserving `W_{-1}`, the first grid row `a_1 (x) B`, forces `A a_1 ∈ <a_1>`; preserving `A' (x) b_1 ⊆ W_{+1}` forces the first row of `B` to be `(beta, 0, 0, 0)`. On the lower-right block, `E -> A' E B'`, and the symmetric and skew parts are preserved for all `E` exactly when `B' = c·A'^T`, since then `E -> c A' E A'^T`. The displayed module structure is read off: `r -> alpha c (A' r^T)^T`, `c_k -> beta (A' c)`, `E -> c A' E A'^T` with `Sym^2` and `Lambda^2` as stated. The transposition is **not** in `L`: it exchanges `r` and `c`, which have `gamma`-weights `-1` and `+1`. ∎

### 6.2 The bound

**Theorem 6.2 (PROVED).** `C` is `L`-equivariant, and `M_lambda ⊆ (S_lambda W)^L`. Hence

    b  =  rank( C|_{M_lambda} )  <=  dim ( (S_lambda W)_{<0} )^L
       =  sum over (mu, kappa, tau) with |mu| = d, |kappa| >= 2d+1, |tau| = 3d - |kappa|
          of  c^lambda_{mu kappa tau} · dim [ S_mu(triv + std) (x) S_kappa(Lambda^2 std) (x) S_tau(std + Sym^2 std) ]^L.

*Proof.* `L` preserves each `gamma`-weight space, so it preserves the decomposition and commutes with the projection onto the negative part; `L ⊆ H` gives `M_lambda ⊆ (S_lambda W)^L`; so `C(M_lambda) ⊆ ((S_lambda W)_{<0})^L`. The displayed expansion is Proposition 3.1 plus Proposition 6.1. ∎

Theorem 4.1 is the case where the sum is empty. The bound is a **pre-screen**: it is computed from `lambda` alone, before any carrier evaluation, and whenever it returns a value `<= s - a` the cell cannot yield `B < a` and the heavy run is pointless.

### 6.3 The named finite problem, and its size

For one cell `(d, lambda)` the quantity above is:

1. **Littlewood–Richardson.** Enumerate `mu ⊢ d` with `ell <= 4`, `kappa ⊢ j` with `ell <= 3` and `2d+1 <= j <= lambda_1+lambda_2+lambda_3`, `tau ⊢ 3d-j` with `ell <= 9`; compute `c^lambda_{mu kappa tau}` (a three-factor LR coefficient, i.e. a sum of products of ordinary LR coefficients over intermediate shapes).
2. **A `GL_3` invariant count.** For each surviving triple, the dimension of the `L`-invariants of `S_mu(triv + std) (x) S_kappa(Lambda^2 std) (x) S_tau(std + Sym^2 std)`, which expands by Cauchy and the classical `GL_3` plethysms of `Sym^2` and `Lambda^2`, with the three scalar characters `alpha, beta, c` imposing three linear conditions on the multidegrees.

**Size, for the cells this programme cares about.** The triple count is `p_4(d) · sum_j p_3(j) · p_9(3d - j)`, where `p_k(n)` counts partitions of `n` into at most `k` parts. For a cell at `d = 7` (`j` from 15 to 21, `|tau| <= 6`): `p_4(7) = 11` and `sum_j p_3(j)·p_9(21-j) = 955`, so at most 10,505 triples, each an LR coefficient on shapes of size at most 28 plus a `GL_3` count. That is seconds to minutes of symmetric-function arithmetic, against the hours-to-days of the carrier run B18-02 prices for the same cell. For the ten-row LMR-type cell at `d = 26` the crude triple count is about `4.2·10^8`, so the screen is itself a real computation there, though still far below the 8.8 TB column tensors B18-02 records for that cell; the `kappa ⊆ lambda` and `tau ⊆ lambda` restrictions cut the count substantially and were not exploited in this estimate.

**Not done here.** I did not implement step 2. What is proved is the inequality and the reduction; the screen's value in a specific five-row cell is **NOT REACHED**.

## 7. What still lacks a proof

Stated plainly, because these are the places a reader could over-read this report.

1. **The length-at-most-five question is untouched.** Proposition 4.4(1) says the silent band is empty there, so Theorem 4.1 proves nothing about the cells the gap hunt actually wants. **Whether `b > s - a` is possible for `ell(lambda) <= 5` is open.** My results do not make it more or less likely; they only explain why twenty controls could not decide it.
2. **No cell with `m_det < a` was analysed.** The instrument's decisive case remains the one B18-02 identified: a cell where `m_det < a`, where exactness would give `B = m_det` and blindness would give `B = a`. The only such certified cells are the excluded ten-row ones. My counterexample works in the opposite direction — it shows blindness where `m_det <= a` is small and `s` is large — and says nothing about whether the arc is sharp when it is not blind.
3. **`m_det` at `(4^6)`, `d = 6`, is not computed.** Theorem 5.1 needs only `m_det <= a = 1`. Whether `m_det` is 0 or 1 there is unknown, and with it whether that cell has `D > 0` at all. It cannot be settled by this arc (§5.3).
4. **Theorem 6.2's screen is unevaluated.** The `GL_3` invariant count of step 2 is standard but was not implemented, so no numerical upper bound on `b` exists for any five-row cell.
5. **Nothing here bounds `m_pad`, produces a padding rank, or nominates a cell.** No `U`, no `r`, no gap. The `a >= 1` precondition is checked only for `(4^6)`.
6. **The arc is one arc.** Every statement is about the specific `gamma` of B17-02/B18-02. A different one-parameter degeneration, or the full boundary, is untouched: Theorem 4.1 is not a statement that the boundary carries no information in the band, only that this arc does not.

## 8. Claims, negatives, resources, and the next test

### 8.1 Ledger

| # | Claim | Label |
|---|---|---|
| 3.1 | every component of a full-`H` invariant has `|mu| = d`, `|kappa| = #v`, `|tau| = 3d - #v`, `gamma`-weight `2d - #v` | **PROVED** (independent re-derivation of B18-02 Lemma 4.1) |
| 3.2, 3.3 | `C` is the projection onto `|kappa| >= 2d+1`; necessary conditions on the triple | **PROVED** |
| 4.1 | `lambda_1 + lambda_2 + lambda_3 <= 2d` implies the forbidden subspace of `S_lambda W` is zero, so `b = 0` and `B = min(a, s)` | **PROVED** |
| 4.2 | sharper Littlewood–Richardson silence criterion | **PROVED** |
| 4.3 | `b > 0` requires `ell(lambda) <= 7 + min(9, d-1)` | **PROVED** |
| 4.4 | the band is empty for `ell <= 5`; at `ell = 6` it is the rectangle `((2d/3)^6)`; for `7 <= ell <= 16` it is `lambda_4 + ... + lambda_L >= 2d` | **PROVED** |
| 5.2 | `d = 6`, `lambda = (4^6)`: `a = 1`, `g = 13`, `s = 10`; band cells at `d = 3, 4` with `a = 0` and `s = 1, 3, 2, 1` | **MEASURED** (exact; seven controls pass, including reproduction of B18-02's `s` values) |
| 5.1 | in that cell `b = 0`, `ker C = M_lambda` has dimension 10, `m_det <= 1`: **EC is false**, defect at least 9; and no gap certificate is possible in any band cell | **PROVED**, given the MEASURED `a` and `s` |
| 6.1, 6.2 | the grading-preserving Levi `L`, its module structure, and `b <= dim((S_lambda W)_{<0})^L` | **PROVED** |
| 6.3 | the screen as a named finite problem, with triple counts 10,505 at `d = 7` and about `4.2·10^8` at `d = 26` | **PROVED counts**, screen **NOT REACHED** |
| — | anything about `ell(lambda) <= 5`; any cell with `m_det < a`; any `B < U`; any padding rank; any gap | **NOT REACHED** |

### 8.2 Honest negatives

1. **The headline is a negative.** The instrument is blind in the band, not sharper. This closes a spending question, not the mathematical one.
2. **The counterexample is at length six**, where B18-02 did not claim exactness. It refutes the general reading of EC, not their length-five form.
3. **`a = 1` at `(4^6)` is thin.** The cell meets the `a >= 1` precondition, but a one-dimensional ambient multiplicity is the weakest non-degenerate case available; the three other band cells I certify have `a = 0`.
4. **No five-row cell was advanced in any way.**
5. **The Levi screen is a proof, not a number.** Until step 2 is implemented it cannot retire a specific five-row cell.
6. **Budget, not mathematics, set `MAXROWS = 8` and `d <= 4`** in the sweep of §5.2; band cells with more rows at `d >= 5` were not enumerated.

### 8.3 Resources

| Run | Command | Wall | Peak | Exit |
|---|---|---|---|---|
| band sweep, `d = 1..4`, controls C1–C5 | `timeout 60 python analysis/b19_01_band.py` | 7.84 s | well under the 512 MiB cap | 0 |
| the `d = 6` cell, controls P1–P2 | `timeout 60 python analysis/b19_01_band6.py` | 2.31 s | well under the cap | 0 |

Both: one process, `OMP_NUM_THREADS=1`, `OPENBLAS_NUM_THREADS=1`, under `timeout 60` and `ulimit -v 524288` (the shell accepts `ulimit -v`; enforcement against a native Windows `python.exe` is not verified). No lease requested or used; no background process remains. **No carrier run, no large computation, no new cell handed to slots 05 or 10 for numerical work.**

| Artifact | SHA-256 |
|---|---|
| `analysis/b19_01_band.py` | `3b15bbd25f55b5a783e2c61354e23dd7055f48f1ccd320a6e568efeb0e8dd919` |
| `analysis/b19_01_band6.py` | `908cc1ee4f331ff89e57c3bda93c3e5c6db6d8e2481ba56ebbd15e14b662868d` |
| `results/b19_01/band_cells.json` | `346630587aa7c2d7aca075216593a1abf88a975c03305c24fac3a50ec7b4863e` |
| `results/b19_01/band_cell_d6.json` | `3bd1695d1eb84868891a9af6e0ca8a8f73bf213c6b86c6ca6deadfc36fc2cdf2` |

One implementation error is recorded because it changes how the numbers should be read: a first version of `b19_01_band6.py` skipped conjugacy classes with `chi_R(eta) = 0`, which drops the `chi_R(eta^2)` term of formula (3.1) and made `s` non-integral. The assertion caught it. The published `s` values come from the corrected code, which reproduces B18-02's independently published `s` in seven cells.

### 8.4 One next sufficient test, and its price

**Test.** Implement step 2 of §6.3 and evaluate the Levi screen `dim((S_lambda W)_{<0})^L` on the five-row cells slot 06 is considering, **before** any carrier run. For each cell report the screen value `b_max` next to `s`, `a` and `U`.

- If `b_max <= s - a`, the cell provably cannot give `B < a` by this arc: **do not spend the lease**.
- If `b_max > s - a`, the cell is one where the arc could in principle beat the ambient ceiling, and the carrier run B18-02 prices is justified.
- The screen never certifies a gap by itself: it is an upper bound on `b`, and `b` is what a gap certificate needs to be **large**.

**Price.** One process, symmetric-function arithmetic only. At `d <= 7`: at most about 10,505 triples per cell, each an LR coefficient on shapes of size `<= 4d` plus a `GL_3` invariant count; estimated seconds to a few minutes per cell, inside the default 60 s / 512 MiB pilot for a single cell, and a small explicit lease for a sweep of many cells. **Estimated, not measured.** The `d = 26` ten-row cell is out of scope at about `4.2·10^8` triples before the `⊆ lambda` restrictions.

**What the integrator most needs to know.** The twenty-control regularity `s - b = a` does not extend: at `d = 6`, `lambda = (4^6)`, `b = 0` is proved while `s = 10` and `a = 1`. In that whole band the arc cannot certify anything, so any plan that budgets carrier time on six-to-ten-row cells should first check three parts of `lambda` against `2d`.
