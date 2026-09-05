# The BIP mechanism, tested against our pair at `n = 4`

Session 52, Task 0.  Companion to `docs/dip_transfer.md`, which did the same
job for Dörfler–Ikenmeyer–Panova and left this question open: session 37 flagged
that the house convention "`a = 1` cells are closed by BIP" is *"an extrapolation
outside the theorem's regime"* and should be re-labelled **"excluded by
convention, not by theorem"** (`docs/dip_transfer.md` §3), but it did not ask
whether the **mechanism** reaches `n = 4` even though the theorem does not.
This document answers that.

Literature read this session, all **adopted-from-literature**, quoted to the
arXiv versions named:

* Bürgisser, Ikenmeyer, Panova, *No occurrence obstructions in geometric
  complexity theory*, arXiv:1604.06431; FOCS 2016; **J. Amer. Math. Soc. 32
  (2019), 163–193** [BIP].  arXiv has three versions (v1 2016-04-21,
  v2 2017-03-14, v3 2018-09-17) and the numbering differs: the main theorem is
  **Theorem 1.4 in v3** and **Theorem 1.5 in v1**; the three positive
  propositions are **2.4, and §6** in v3 and **5.1, 5.2, 5.5** in v1 and in the
  authors' copy.  Both numberings are given below.
* Kadish, Landsberg, *Padded polynomials, their cousins, and geometric
  complexity theory*, **Comm. Algebra 42 (2014), no. 5, 2171–2180** [KL].
* Ikenmeyer, Panova, *Rectangular Kronecker coefficients and plethysms in
  geometric complexity theory*, **Adv. Math. 319 (2017), 40–66**;
  arXiv:1512.03798 [IP].
* Dörfler, Ikenmeyer, Panova, *On geometric complexity theory: multiplicity
  obstructions are stronger than occurrence obstructions*, ICALP 2019,
  LIPIcs 132, art. 51; **SIAM J. Appl. Algebra Geom. 4 (2020), no. 2, 354–376**;
  arXiv:1901.04576 [DIP].

---

## 0. Verdict

> **The mechanism does not transfer to `n = 4`, and the reason is not that the
> constants are too small.  It is that the machinery's reach is measured in the
> *length* of the weight, and at `n = 4` that reach is `ℓ(λ) ≤ 4`, while
> permanent-sensitivity at `n = 4` begins at `ℓ(λ) = 6`.**
>
> Sharply: every determinant-side point BIP's argument supplies at `n = 4` is a
> padded power sum with `s·k ≤ 4`, of which there are exactly **eight**; every
> one of them is a **product of four linear forms** and has **linear span at
> most 3**; and a weight vector of weight `λ` vanishes identically at every
> point whose span has dimension `< ℓ(λ)` (Lemma B, one line).  So the
> mechanism's entire supply of evaluation points is **blind, identically, to
> every weight of the census**.  Verified in-house at three six-row cells: the
> highest weight vector vanishes at all eight, and is non-zero at a determinant
> pencil in the same run.
>
> **One piece does transfer, and it is already in the house under another
> name.**  BIP's only input about the padded permanent is Kadish–Landsberg's
> necessary condition `|λ̄| ≤ md`, which at `(n,m) = (4,3)` reads `λ_1 ≥ δ` —
> numerically identical to the programme's own obstruction-eligibility gate.
>
> **The negative the brief hoped for is not available.**  A transfer would have
> been worth more than the census; it is not there, so the census proceeds.

---

## 1. T0a — the hypothesis, confirmed

**Theorem 1.4 [v3] = Theorem 1.5 [v1] (quoted):**

> *Let `n, d, m` be positive integers with `n ≥ m^25` and `λ ⊢ nd`. If `λ`
> occurs in `C[Z_{n,m}]`, then `λ` also occurs in `C[Ω_n]`.*

with `Ω_n := closure(GL_{n²}·det_n)` and `Z_{n,m} := closure(GL_{n²}·X_{11}^{n−m}per_m)`
(v3 eq. (1.2)).  At `(n,m) = (4,3)`:

    m^25 = 3^25 = 847,288,609,443     vs     n = 4.

The hypothesis fails by eleven orders of magnitude.  The brief's reading is
correct and the theorem is silent at our pair.  The paper's only remark on the
bound is *"One can likely improve the bound on `n` by a more careful analysis"*;
there is no claim that the result holds, or is expected to hold, at small `n`.

---

## 2. The mechanism, in four pieces

The proof has one negative input and three positive engines.

**(a) The necessary condition** — the *only* thing BIP use about the padded
permanent.  **Theorem 2.1 [v3] = Prop. 4.1 [v1]**, attributed in the text to
*"an insight due to Kadish and Landsberg"*:

> *If `λ ⊢ nd` occurs in `C[Z_{n,m}]_d`, then `ℓ(λ) ≤ m²` and `|λ̄| ≤ md`.*

(`λ̄` is `λ` with its first row deleted.)

**(b) The supply of determinant-side points.**  **Theorem 2.5 [v3] = Theorem 2.8
[v1]:**

> *Let `X, φ_1, …, φ_k` be linear forms on `C^{n×n}` and assume `n ≥ sk`. Then
> the power sum `X^{n−s}(φ_1^s + · · · + φ_k^s)` of `k` terms of degree `s`,
> padded to degree `n`, is contained in `Ω_n`.*

and **Proposition 2.3 [v3]:** *"Let `n ≥ kℓ` and `ℓ` be even. Then
`(k × ℓ)^{♯nk}` occurs in `C[Ω_n]_k`."*  (The weight is a body of `k` rows of
length `ℓ` under one long first row, so `ℓ(λ) = k+1`.)

**(c) The semigroup property** (Lemma 2.2): occurrences add.

**(d) The three evaluation engines.**  Every one is a statement that a highest
weight vector of weight `λ` fails to vanish on `Ω_n`:

| | statement | hypotheses |
|---|---|---|
| **Prop. 2.4 [v3] = 5.1 [v1]**, *small degrees* | every HWV of weight `λ` in `Sym^d Sym^n V` is non-vanishing on `Ω_n` | `∃m: |λ̄| ≤ md` and **`md² ≤ n`** |
| **Prop. 5.2 [v1]**, *extremely long first rows* | same | `ℓ(λ) ≤ m²`, `λ_2 ≤ s`, **`m²s² ≤ n`**, `m²s ≤ d` |
| **Prop. 5.5 [v1]**, *splitting* | `λ` occurs in `C[Ω_n]_d` | `ℓ(λ) ≤ m²`, `m^10 ≤ |λ̄| ≤ md`, **`n ≥ 24m^6`**, `d > 4m^6` |

`m` in (d) is a **free auxiliary parameter**, not the permanent size; the main
theorem ties it to `m` only at the end.  Everything below optimises over it,
which is the generous reading.

The case split is quoted verbatim in v3 §2(a): *"We distinguish two cases. If
the degree `d` is large (say `d ≥ 24m^6`) we proceed as in [IP] … If the degree
`d` is small, we rely on the following result."*  `n ≥ m^25` is not consumed by
one lemma; it is the single bound that clears all three cases at once.

---

## 3. Each piece at `n = 4`

Machine-checked by `analysis/wk9_s52_bipreach.py` (which only evaluates the
hypotheses above; it re-derives nothing).

### (a) transfers — and is our eligibility gate

At `(n,m,d) = (4,3,δ)` we have `|λ| = 4δ`, so

    |λ̄| ≤ mδ   ⟺   4δ − λ_1 ≤ 3δ   ⟺   **λ_1 ≥ δ**,

which is exactly the programme's obstruction-eligibility condition (Corollary B
of `docs/reducible_ideal.md`, derived in-house from the reducible model).  The
two statements are about different objects — [KL] bound `Z_{n,m}` in `Sym^4 C^16`,
Corollary B bounds `mult_pad` in the length-reduced model at `r` variables — and
they arrive at the same inequality.  **This is an independent confirmation of
the eligibility gate from outside the programme.**

*A note for the `ℓ ≥ 7` sessions, flagged not claimed.*  [KL]'s companion bound
is `ℓ(λ) ≤ m² = 9`, whereas `docs/sixrow_frontier.md` §1 records the
permanent-visible window as `6 ≤ ℓ(λ) ≤ 10`.  The `10` is the support count
`1 + m²` of `x_0·per_3(x_1..x_9)`; [KL]'s `9` is sharper.  If [KL]'s bound
transfers to the length-reduced model, `ℓ = 10` is empty and the window closes
one row earlier.  This session does not settle it — it does not arise at
`ℓ = 6` — but it is worth one paragraph of a later session.

### (b) the supply of points collapses

`n ≥ sk` at `n = 4` admits exactly eight `(s,k)`:

| `(s,k)` | point | linear span |
|---|---|---|
| (1,1) (1,2) (1,3) (1,4) | `X³·(φ_1+···+φ_k)` — the sum is one linear form | **2** |
| (2,1) | `X²φ²` | 2 |
| (2,2) | `X²(φ_1²+φ_2²)` | **3** |
| (3,1) | `X·φ³` | 2 |
| (4,1) | `φ⁴` | 1 |

**Maximum linear span 3.**  And over `C` every one of the eight is a *product of
four linear forms* — `φ_1²+φ_2² = (φ_1+iφ_2)(φ_1−iφ_2)` — so the whole supply
lies inside the Chow variety `Ch^4`, which sits in a 3-dimensional subspace:
dimension at most `4·3 − 3 = 9`, against `dim D_6^{det_4} = 66`.

Proposition 2.3 collapses the same way: `n ≥ kℓ` with `ℓ` even forces `k ≤ 2`,
so `ℓ(λ) = k+1 ≤ 3`, and the two surviving generators are `(2,2)` at degree 1
and `(4,2,2)` at degree 2.  Sums of partitions of length `≤ 3` have length
`≤ 3`, so the semigroup route (c) never leaves `ℓ(λ) ≤ 3` either.

### (c) the evaluation engines

* **Prop. 2.4 / 5.1** needs `md² ≤ n = 4` with `m ≥ 1`: admissible only for
  `d ≤ 2`.  **Vacuous at every degree of this programme** (`δ ≥ 6`), and it
  fails by a factor `md²/n ≥ δ²/4`, which is 12 at `δ = 7` and 20 at `δ = 9`.
* **Prop. 5.2** needs `m²s² ≤ 4`.  The only choices are `(m,s) = (1,1), (1,2),
  (2,1)`, and the best length reach is `m² = 4`: **`ℓ(λ) ≤ 4`**, and only for
  `λ_2 ≤ s = 1`, i.e. hooks, at degree `d ≥ 4`.
* **Prop. 5.5** needs `n ≥ 24m^6 ≥ 24·2^6 = 1536`.  **Vacuous.**

### The reach, as a function of `n`

The least `n` at which some engine reaches a weight of length `ℓ` with
`λ_2 = L` (`analysis/wk9_s52_bipreach.py`; the Prop. 2.3 column is optimistic —
it is a length reach only, and only for bodies that are sums of even rectangles,
which is why the general statement needs Prop. 5.5):

| `ℓ(λ)` | `λ_2` | Prop. 5.2 | Prop. 2.3 | Prop. 5.5 | best |
|---|---|---|---|---|---|
| 3 | any | `9λ_2²` | 4 | 1536 | **4** |
| 4 | 1 | 4 | 6 | 1536 | **4** |
| 4 | ≥2 | `16λ_2²` | 6 | 1536 | **6** |
| 5 | 1 | 9 | 8 | 17496 | **8** |
| 6 | 1 | **9** | 10 | 17496 | **9** |
| 6 | ≥2 | `9λ_2²` | 10 | 17496 | **10** |

**The least `n` at which the machinery says anything at all about a six-row
weight is `n = 9`** (Prop. 5.2, hooks `λ = (λ_1,1,1,1,1,1)` only, degree `≥ 9`).
For a six-row weight with `λ_2 = L` the requirement is `n ≥ 9L²`.

And that hook case covers **no cell of this session's census**: over the 150
`a = 1` obstruction-eligible cells at `δ = 7, 8, 9, 10`, `λ_2` runs from **2 to
12** and **not one is a hook** (measured, `results/s52_census.md`).  So the
requirement for the cells we actually measure is `n ≥ 9λ_2² ∈ [36, 1296]`.  We
are at `n = 4`.

---

## 4. Lemma B, which makes the collapse decisive rather than merely tight

**Lemma B (proved).**  Let `f` be a weight vector of weight `λ` in
`C[Sym^n V]_δ` and let `p ∈ Sym^n V` have linear span of dimension `u < ℓ(λ)`.
Then `f(p) = 0`.

*Proof.*  Choose coordinates so the span is `⟨e_1,…,e_u⟩` and take the torus
element `t = diag(1,…,1,c,…,c)` with `c` in positions `u+1,…`.  Then `t·p = p`,
while `f(t·q) = t^λ f(q)` with `t^λ = c^{λ_{u+1}+···+λ_N}`.  Since `ℓ(λ) > u`,
`λ_{u+1} ≥ 1`, so the exponent is positive; choosing `c ≠ 1` forces
`f(p) = 0`. ∎

Combined with §3(b): **at `n = 4`, every highest weight vector of weight `λ`
with `ℓ(λ) ≥ 4` vanishes at every point BIP's Theorem 2.5 supplies.**  This is
not a statement about constants that a sharper analysis could improve — the
evaluation the mechanism performs is identically zero on the region the
programme measures.

### Verified in-house (measured)

`analysis/wk9_s52_bippoints.py`, three banked six-row `a = 1` cells at `δ = 7`,
both house primes, one exhibited highest weight vector each:

| `λ` (`δ = 7`) | `N_S` | `n_χ` | eight BIP points | `chow3` | `chow6` | `ℓ·c` | `det_4` pencil | true pad |
|---|---|---|---|---|---|---|---|---|
| `(18,2,2,2,2,2)` | 8128 | 190 | **0** | 0 | 0 | ≠0 | **≠0** | ≠0 |
| `(15,5,5,1,1,1)` | 17091 | 576 | **0** | 0 | 0 | ≠0 | **≠0** | ≠0 |
| `(14,8,3,1,1,1)` | 14636 | 928 | **0** | 0 | 0 | ≠0 | **≠0** | ≠0 |

`N_S` and `n_χ` reproduce `results/s36_aone.md` exactly at all three, and the
`det`/`pad` columns reproduce its `mult_det = mult_pad = 1` verdicts.

Two readings, both worth recording.  The eight zeros are Lemma B, as predicted.
The `chow6` zero is *not* Lemma B — that point has full support 6 — and says
that at these three cells the highest weight vector vanishes on the whole Chow
variety of products of four linear forms, so BIP's supply at `n = 4` fails for a
second, independent reason.  The `ℓ·c` column being non-zero while `chow6`
vanishes is the expected ordering `Ch^4 ⊂ R_6` (so `I(R_6) ⊆ I(Ch^4)`) and is
the `docs/brief_wording.md` §5 degeneracy-direction control: the statistic is
*less* degenerate at the reducible point than at the Chow point, in the
direction the containment demands.

---

## 5. Why the failure is essential, not technical

Three ways of saying the same thing.

1. **The padding exponent is 1.**  BIP's object is `X_{11}^{n−m}per_m`; at
   `(4,3)` the padding is a single variable.  The entire method is "peel the
   long first row off `λ`, reduce to the body, evaluate the body at a power sum
   under a large padding exponent".  At `n − m = 1` there is nothing to peel and
   nothing to pad with.
2. **The body is three quarters of the partition.**  [KL] allows
   `|λ̄|/|λ| ≤ m/n`.  BIP work at `n ≥ m^25`, where that ratio is at most
   `m^{−24} ≤ 3^{−24} ≈ 1.2·10^{−12}`: `λ` is one very long row with a
   negligible body.  At `(4,3)` the ratio is `3/4`.  The regime the argument
   describes is absent.
3. **`n < m²`.**  [KL] permit `ℓ(λ) ≤ m² = 9`, and every engine needs the
   determinant to be *bigger* than the length it must see — `n ≥ kℓ`,
   `n ≥ m²s²`, `n ≥ 24m^6`.  At `(4,3)` the permitted length already exceeds
   `n`, so no engine can cover even the shortest permitted weight.

---

## 6. What a transfer would have had to look like, and what our own data says

A transferred mechanism would be an argument, valid at `n = 4`, concluding
`i_det = 0` — that the weight-`λ` highest weight vector cannot vanish on all
`det_4` pencils — from the mere fact that `λ` is eligible.  BIP have no such
argument: their entire positive half runs through points of one special shape,
and §3–§4 show that shape is degenerate here.

Two honest observations on the other side, neither of which rescues the
mechanism.

* **Our own record is consistent with the conclusion even though the method
  fails.**  `results/sixrow_record.md`: `mult_det = a` at all 193 measured
  six-row cells, i.e. `i_det = 0` at every one, across `δ = 6, 7, 8, 9`.  So the
  *statement* an `n = 4` analogue would make has 193 confirmations and no
  counterexample.  That is evidence about the world, not about the proof, and it
  is exactly why the census is worth running rather than assumed.
* **But no unrestricted analogue can hold.**  `onset I(D_6^{det_4}) ≤ 1197` is a
  theorem (s44 Theorem A; the s49 brief corrects the constant to 1148, which
  changes nothing here), so `I(D_6^{det_4})` is non-zero at some degree, hence
  some weight has `i_det ≥ 1`, hence "every six-row highest weight vector is
  non-vanishing on `D_6^{det_4}`" is **false**.  What remains open — and is not
  decided by anything in this session — is whether the first such weight is
  obstruction-eligible (`λ_1 ≥ δ`) or onset-only.

---

## 7. The cost of the `a = 1` prior (T0c)

At `a = 1` the highest weight space is a line, so `mult_det ∈ {0,1}` and a
multiplicity obstruction (`mult_pad > mult_det`) forces `mult_det = 0`: it **is**
an occurrence obstruction.  The `a = 1` restriction therefore gives up the whole
strength gap between the two notions.

[DIP] is the paper that establishes that gap is real, and it should be cited for
exactly what it proves and no more:

* the setting is the **Chow variety** `Ch^n_m` (products of homogeneous linear
  forms) against **bounded border Waring rank** `Pow^n_{m,k}` — *not* determinant
  against padded permanent;
* Theorem 2.3: for `m ≥ 3, n ≥ 2, k = d = n+1, λ = (n²−2, n, 2)`,
  `mult_λ C[Ch^n_m]_d < mult_λ C[Pow^n_{m,k}]_d`; and in the two finite settings
  `(k,n,m,d) = (4,6,3,7)`, `λ = (34,6,2)`, `7 < 8`, and `(4,7,4,8)`,
  `λ = (47,7,2)`, `< 11`, the separation **cannot** be achieved by occurrence
  obstructions for any `k`;
* [DIP] **do not state** the multiplicity-1 observation above.  It is a
  one-line consequence of their definitions and is claimed here as ours, not
  attributed to them.

So the price is stated plainly, as the brief asks: **the `a = 1` census buys
losslessness against the orientation problem by restricting to the strictly
weaker of the two obstruction notions.**  Nothing in this session raises the
probability that a cell fires; it raises what a firing cell would be worth.

---

## 8. Labels

* **adopted-from-literature:** every quoted statement of [BIP], [KL], [IP],
  [DIP] in §§1–2 and §7.
* **proved:** Lemma B; the eight-point enumeration and the length reaches of
  §3, which are evaluations of quoted hypotheses at `n = 4`; the identity
  `|λ̄| ≤ mδ ⟺ λ_1 ≥ δ` at `(n,m) = (4,3)`.
* **measured:** the table in §4.
* **flagged, not claimed:** the `ℓ(λ) ≤ m² = 9` versus `ℓ ≤ 10` question in §3(a).
