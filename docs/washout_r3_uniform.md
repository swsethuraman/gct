# Density of `per_m` pencils at length 3, uniformly in `m`

Session 49 (brief §2.5, Theorem C).  Session 48 proved the *counting* threshold
`r*(m) = 3` for `m ≥ 17` (`docs/washout_threshold.md` §3: `r = 4` fails the
parameter count `m²r − orbit(m) ≥ C(r+m−1,m)` for every `m ≥ 17`, a uniform
inequality) but established the **density** direction — that `Φ_{m,3}` is
actually dominant, so washout holds up to `r = 3` — only by a Jacobian rank at
each `m` on a finite range (`m ≤ 17`).  Finitely many evaluations do not prove
an infinite family.  This note supplies the uniform argument the brief asked
for: **`Φ_{m,3}` is dominant for every `m`**, hence washout holds at `r = 3` for
all `m`, and `r*(m) = 3` for `m ≥ 17` is a threshold about a *proved* density,
not a measured one.

Notation: `Φ_{m,r} : (M_m)^r → Sym^m C^r`, `(A_1,…,A_r) ↦ per_m(Σ s_i A_i)`.
A single point of full Jacobian rank proves dominance (Lemma 1 of
`docs/washout_lemma.md`; a rank at a point is a lower bound on the generic rank,
the direction that closes).

## 1. The structured point

Fix `m` and a primitive `m`-th root of unity `ω` (over `C`; over `F_p` take
`p ≡ 1 (mod m)`, as the checks do).  Take

    A_1 = I,   A_2 = diag(1, ω, ω², …, ω^{m−1}),   A_3 = P,

`P` the cyclic shift `P e_i = e_{i−1}` (so `P_{i,i+1} = 1`, indices mod `m`).
Then

    A(s) = s_1 A_1 + s_2 A_2 + s_3 A_3

is the **cyclic bidiagonal** matrix with diagonal `x_i(s) = s_1 + ω^i s_2` and
cyclic superdiagonal `s_3`.

**Cyclic symmetry (proved).**  Let `S` be the permutation matrix `S e_i = e_{i+1}`
and `τ` the substitution `(s_1, s_2, s_3) ↦ (s_1, ω s_2, s_3)`.  Then

    S A(s) S^{-1} = A(τ s),                                                      (1)

because conjugating by `S` shifts the diagonal `x_i ↦ x_{i+1}` and `x_i(τs) =
s_1 + ω^i·ω s_2 = x_{i+1}(s)`, while the cyclic superdiagonal is fixed.  Writing
`σ_{ij}(s) = per(A(s)^{(i,j)})` for the `(i,j)` cofactor-permanent (delete row
`i`, column `j`), (1) gives

    σ_{i+1,j+1}(s) = τ( σ_{ij}(s) ) .                                            (2)

(Verified coefficientwise, `analysis/wk9_s49_checks.py D`,
`results/logs/s49_checks_D2.log`.)

## 2. The sub-permanents are `s_3`-homogeneous

**Lemma A.**  For the cyclic distance `w = (j − i) mod m`,

    σ_{i,i+w}(s) = s_3^{\,m−w} · f_i^{(w)}(s_1, s_2),   1 ≤ w ≤ m−1,

with `f_i^{(w)}` a binary form of degree `w − 1`; and `σ_{i,i}(s) =
∏_{r ≠ i} x_r(s)`, a binary form of degree `m − 1` (the `w = 0` case, `s_3`-free).

*Proof.*  A nonzero term of `σ_{i,j}` is a bijection `f` from rows `∖{i}` to
columns `∖{j}` with `f(r) ∈ {r, r+1}` (diagonal weight `x_r`, shift weight
`s_3`).  The number of shift edges is `Σ_r [f(r) = r+1]`; reducing the identity
`Σ_{r≠i} f(r) = Σ_{c≠j} c` modulo `m` gives `#shift ≡ (Σ_{c≠j}c) − (Σ_{r≠i}r) ≡
i − j ≡ m − w (mod m)`, and since `#shift ∈ {0,…,m−1}` it equals `m − w` for
`1 ≤ w ≤ m−1` — the **same** for every term, so every monomial of `σ_{i,i+w}`
carries `s_3^{m−w}` and the remaining `w − 1` factors are diagonal entries `x_r`,
a binary form of degree `w − 1`.  For `w = 0` no shift edge can occur (column
`i` is deleted, forcing all `f(r) = r`), giving `∏_{r≠i} x_r`.  ∎

(The `s_3`-power `m − w` and total degree `m − 1` are verified coefficientwise for
`2 ≤ m ≤ 14` in `results/logs/s49_checks_D2.log`; the exact diagonal window in
`f_i^{(w)}` depends on `i` and is immaterial below — only (2) is used.)

## 3. The window lemma, proved uniformly

**Lemma B (window lemma).**  Let `x_r = s_1 + ω^r s_2`.  For `1 ≤ j ≤ m − 1` the
`m` cyclic window products `W_a = ∏_{t=0}^{j−1} x_{a+t}` (`a = 0,…,m−1`, indices
mod `m`) span `Sym^j C^2`.

*Proof.*  `τ` (from §1) fixes `s_1` and scales `s_2` by `ω`, so it acts on
`Sym^j C^2` diagonally, with eigenvalue `ω^k` on the monomial `s_1^{j−k} s_2^k`,
`k = 0,…,j`.  These `j + 1` eigenvalues are **distinct** because `0 ≤ k ≤ j ≤
m − 1 < m`.  Since `τ x_r = x_{r+1}`, we have `W_a = τ^a W_0`, so
`span{W_a} = span{τ^a W_0 : a}` is the sum of the `τ`-eigenlines on which `W_0`
has a nonzero component.  The `s_1^{j−k}s_2^k`-coefficient of
`W_0 = ∏_{t=0}^{j−1}(s_1 + ω^t s_2)` is the elementary symmetric function

    e_k(1, ω, …, ω^{j−1}) = ω^{k(k−1)/2} · \binom{j}{k}_ω ,

the `q`-binomial at `q = ω`.  For `0 ≤ k ≤ j ≤ m − 1`,
`\binom{j}{k}_ω = ∏_{t=1}^{k} (1 − ω^{j−t+1})/(1 − ω^t)` has every factor
nonzero (each exponent `j−t+1` and `t` lies in `{1,…,m−1}`, so `ω^{\cdot} ≠ 1`),
hence `e_k ≠ 0` for **every** `k`.  So `W_0` has a nonzero component on every
eigenline and `span{W_a} = Sym^j C^2`.  ∎

(Verified as a rank over `F_p` for `2 ≤ m ≤ 40` and every `1 ≤ j ≤ m−1`,
`analysis/wk9_s49_checks.py C`, `results/logs/s49_checks_C.log`; the
`q`-binomial identity and non-vanishing independently at `m ≤ 24`.)

## 4. Assembly: full rank for every `m`

The differential of `Φ_{m,3}` at the structured point sends a matrix direction
in slot `k` at entry `(i,j)` to `s_k · σ_{ij}(s)`, so its image is

    Im dΦ = span{ s_k · σ_{ij}(s) : k ∈ {1,2,3}, 0 ≤ i, j ≤ m−1 } ⊆ Sym^m C^3 .

Grade `Sym^m C^3 = ⊕_{t=0}^{m} s_3^{t}·Sym^{m−t} C^2`.  We hit each summand:

- **`t = 0`** (`s_3`-free, `Sym^m C^2`): the `w = 0` sub-permanents
  `σ_{ii} = ∏_{r≠i} x_r` are, by (2), the `τ`-orbit of `∏_{r≠0} x_r`; by the
  argument of Lemma B (all `q`-binomial coefficients nonzero at `j = m−1`) they
  span `Sym^{m−1} C^2`, and `s_1·Sym^{m−1} + s_2·Sym^{m−1} = Sym^m C^2`.
- **`1 ≤ t ≤ m−1`**: take `w = m − t` (`1 ≤ w ≤ m−1`).  By Lemma A the
  sub-permanents `σ_{i,i+w} = s_3^{t}·f_i^{(w)}` with `deg f_i^{(w)} = w−1 =
  m−t−1`; by (2) the `f_i^{(w)}` are the `τ`-orbit of `f_0^{(w)}`, which spans
  `Sym^{m−t−1} C^2` (Lemma B).  Then `s_1·f + s_2·f` fills
  `s_3^{t}·Sym^{m−t} C^2`.
- **`t = m`** (`s_3^m`): `w = 1` gives `σ_{i,i+1} = s_3^{m−1}`, and `s_3·s_3^{m−1}
  = s_3^{m}`.

So `Im dΦ = Sym^m C^3`, `rank dΦ_{m,3} = C(m+2, 2)`, and `Φ_{m,3}` is dominant.
Every step holds for every `m`.  ∎

**Corollary (Theorem C, density at `r = 3`, uniform).**  `D_3^{per_m} =
Sym^m C^3` and `P_3 = R_3` for every `m`.  Combined with the uniform failure of
the count at `r = 4` for `m ≥ 17` (`docs/washout_threshold.md` §3), the washout
threshold satisfies `r*(m) = 3` for all `m ≥ 17` **with the density direction
now proved, not merely measured**.  (`r = 2` is elementary for every `m`: every
binary `m`-form is a product of linear forms, `washout_threshold` §3.)

## 5. What this does and does not close

- **Closed:** `r = 3` density for all `m` — the finite-evaluation gap in
  Theorem C(ii) at `r = 3`.  The measured range (`m ≤ 20` here,
  `results/logs/s49_checks_B20.log`, extending s48's `m ≤ 17`) now corroborates
  a theorem rather than standing in for one.
- **Still measured, not proved:** density at the *top* row `r = r*(m)` for
  `4 ≤ m ≤ 16` (there `r*(m) ∈ {4,5}`).  That is Theorem C(ii) at `r = 4, 5`,
  verified per `m` on the range s48 ran; the structured point above is a `r = 3`
  construction and says nothing about `r = 4, 5`.  Those rows remain
  "proved on the checked range," and Theorem C should keep that label for them.
