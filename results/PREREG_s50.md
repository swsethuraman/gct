# Pre-registration — Session 50 (LMR equation: derive, then evaluate)

Committed **before any remainder is computed**. Branch `s50-lmr` off `eb8cecb`.
Labels used later: **proved / measured / adopted-from-literature / expectation**.

## 0. What is fixed before measurement

### 0.1 The weight, derived independently (Task 1) — already settled, recorded here for the record

From arXiv:1004.4802 / Comment. Math. Helv. 88 (2013), Landsberg–Manivel–Ressayre,
*Hypersurfaces with degenerate duals and the GCT program*:

- `Dual_{k,d,N}` = degree-`d` forms in `N` variables whose hypersurface has dual
  variety of dimension `≤ k`. The determinant `det_n` sits in `N = n²`, `d = n`,
  `k = 2n − 2` (dual of `det_n` = rank-1 matrices, dimension `2n−2`).
- Construction (Katz/Segre): `dim Z(P)* = rank(H_{P,w}) − 2` at a general point
  `w` of the cone. Dual degenerate to `≤ k` ⟺ `rank H_P ≤ k+2` on `Z(P)` ⟺
  **`P` divides `det_{k+3}(H_P|_F)` for every `(k+3)`-plane `F`**, where
  `det_{k+3}(H_P|_F)` is a form of degree `(k+3)(d−2)` in the `N` variables.

**Independent degree derivation** (from the divisibility, not from the paper's
weight). On a general line, `p = P|_ℓ` (degree `d`) must divide
`g = det_{k+3}(H_P|_F)|_ℓ` (degree `e = (k+3)(d−2)`). `p | g` is `d` linear
conditions on `coeffs(g)`; each left-kernel functional of the `(e+1)×(e−d+1)`
multiplication matrix has degree `(e−d+1)` in `coeffs(p)`, and `coeffs(g)` have
degree `(k+3)` in `coeffs(P)`. Hence each equation has coefficient-degree

    D = (e − d + 1) + (k + 3) = (k+3)(d−2) + k − d + 4 = (d−1)(k+2).

With `d = n`, `k = 2n−2`:  **`D = 2n(n−1)`**.  Since `|λ| = n·D` and the two
lower coefficients are fixed (`ω₂`-coeff `= 2n²−4n−1`, `ω_{2n+1}`-coeff `= 2`),

    a := coeff of ω₁ = n·D − 4n(n−1) = 2n²(n−1) − 4n(n−1) = 2n(n−1)(n−2).

- **n = 3 check (their stated example):** `a = 12, b = 5, c = 2`,
  `λ = 12ω₁+5ω₂+2ω₇ = (19,7,2⁵)`, `δ = 12`, `|λ| = 36 = 3·12`.  The paper §3.2
  states verbatim "for `n=3`, the module with highest weight `12ω₁+5ω₂+2ω₇`
  occurs with multiplicity six in `S₁₂(S³C⁹)`."  **Reproduced exactly.**
- **n = 4 (our cell):** `a = 48, b = 15, c = 2`,
  `λ = 48ω₁+15ω₂+2ω₉ = (65,17,2⁷)`, **`δ = 24`**, `|λ| = 96 = 4·24`,
  `ℓ(λ) = 9 ≤ 10`.  Matches Theorem 1.1.2 (`ω₁`-coeff `2n(n−1)(n−2) = 48`).

**Factor-of-two resolution (pre-registered): `δ = 24`, NOT `δ = 12`.**  The
`δ = 12` alternative would require `a = n(n−1)(n−2) = 24` (half), which is
inconsistent with (i) the divisibility-derived `D = (d−1)(k+2)`, (ii) Theorem
1.1.2's stated `ω₁`-coefficient, and (iii) the paper's own `n=3` example, which
is at `δ = 12 = 2·3·2` and would be `δ = 6` under the halved reading.  All three
agree on `δ = 2n(n−1)`.

### 0.2 The object evaluated (Task 3)

Ambient `V = C^{16}`, coordinates `x_0,…,x_15`.  `det_4 =` determinant of
`[[x_0..x_3],[x_4..x_7],[x_8..x_11],[x_12..x_15]]`.  Padded permanent
`P_pad = x_0 · per_3(X)`, `X = [[x_1,x_2,x_3],[x_4,x_5,x_6],[x_7,x_8,x_9]]`
(active variables `x_0..x_9`, the "full ten-variable" form).

For a quartic `P` and a random `16×9` integer matrix `B` (the `(k+3)=9`-plane
`F`, `x = B y`, `y = (y_1..y_9)`):

    H_P(x)      = 16×16 Hessian, entries ∂²P/∂x_i∂x_j (quadratic in x)
    M(y)        = Bᵀ · H_P(B y) · B                  (9×9, quadratic entries)
    G(y)        = det_9 M(y)                          (form of degree 18 in y)
    p_pad(y)    = P(B y)                              (quartic in y)
    remainder r = G  mod  p(B y)      (multivariate division; {p} is its own
                                       Gröbner basis, so r = 0 ⟺ p | G)

Computed **exactly over F_p** by specialising `y_2..y_9` to random field
elements and reducing univariate in `y_1` (see §2).  `r ≡ 0` ⟺ the LMR
divisibility holds at `P` ⟺ the degree-24 equation vanishes at `P`.

## 1. The four controls and the positive-result criteria

All four are run.  "remainder 0" is one-sided-hard (needs `r ≡ 0` at many random
`y_2..y_9` over ≥2 primes); "remainder ≠ 0" is one-sided-easy (a single nonzero
`r` at one prime is a rigorous certificate that `p ∤ G` over `Q`, hence the
equation does not vanish).

| # | point | prediction | prior | what it establishes |
|---|---|---|---|---|
| 1 | `det_4` (16 vars) | **r = 0** | 0.90 | **calibration** — LMR's theorem; a nonzero `r` here means the implementation is wrong and nothing downstream counts |
| 2 | generic quartic (10 vars) | **r ≠ 0** | 0.95 | the expression is not identically zero |
| 3 | `ℓ·c`, `c` generic cubic (10 vars) | **r ≠ 0** | 0.85 | transfer control; `P_r ⊆ R_r`, so a nonzero here is weaker than at a true padded permanent |
| 4 | `x_0·per_3` (full 10 vars) | **r ≠ 0** ⇒ **separation** | 0.75 | the sharp test — a degree-24 equation vanishing on `D_r` and not on `P_r` |

Auxiliary, pre-registered:

- **P5 (degeneracy pre-check, brief_wording §6).** Is `G ≡ 0` *identically* for
  `x_0·per_3` (i.e. is the generic rank of `H_{P_pad}` below 9 so the whole
  expression collapses)?  Prediction: **no** — generic `rank H_{P_pad} ≥ 9`, so
  `G ≢ 0` and control 4 is a real divisibility test.  Prior 0.70.  The §6 check
  itself is: control 1 (`det_4` pencil), control 3 (`ℓ·c`), control 4
  (full `x_0·per_3`).  If control 4 is *at least as degenerate* (r = 0) as
  control 1 (r = 0), the equation does not separate at the padded permanent.
- **P6 (controls 3 vs 4).** Prediction: they **agree** (both `r ≠ 0`).  If they
  disagree — control 3 `r ≠ 0` but control 4 `r = 0` — that is the most
  informative outcome and is reported as the headline (per §6, "where (2) and
  (3) disagree, that disagreement is the result").  Prior on agreement 0.75.

**Headline positive result:** control 1 `r = 0` **and** control 4 `r ≠ 0`.
This is a concrete degree-24 separation of `det_4` from the padded `per_3` at the
LMR weight — consistent with LMR's own bound `dc̄(per_3) ≥ 3²/2 > 4`.

**A real failure worth reporting (brief §7):** control 1 or 2 failing.  If the
construction does not vanish on `det_4` (`r ≠ 0` at control 1) or vanishes on
everything (`r = 0` at control 2, the expression identically zero), stop and
report; do not adjust the construction and re-present it.

## 2. Method, exactly

Work over `F_p`, `p` a fixed prime (headline claims repeated over a second
prime).  Fix `B ∈ Z^{16×9}` (recorded).  To test `p_pad | G` without ever
forming the degree-18 `G` in 9 variables:

1. Draw random `a = (a_2,…,a_9) ∈ F_p^8` (recorded seed).
2. `x(t) = B · (t, a_2,…,a_9)ᵀ ∈ F_p[t]^16` (affine-linear in `t = y_1`).
3. `p_a(t) = P(x(t))` — degree ≤ 4 in `t`; get its coefficients by evaluation +
   interpolation at 5 nodes.
4. `g_a(t) = det_9( Bᵀ H_P(x(t)) B )` — degree ≤ 18 in `t`; evaluate the numeric
   `9×9` determinant at 19 nodes and interpolate.
5. `r_a(t) = g_a(t) mod p_a(t)` (univariate over `F_p`).
6. `p ∤ G` (equation nonzero) as soon as one `a` gives `r_a ≠ 0`.  `p | G`
   (equation zero) certified by `r_a = 0` at many random `a` over ≥2 primes;
   `r_a(t)` has `t`-degree ≤ 3 with coefficients of `y`-degree ≤ 18 in 8
   variables, so a modest sample bounds the Schwartz–Zippel error.

Every reported remainder is an exact `F_p` object (a univariate polynomial or
the certified-zero symbol) with `B`, `p`, the seed, and the number of `a`-samples
recorded, and handed to the verifier (§3).

The generic rank of `H_P` and of `M(y)` (for P5) is measured the same way: rank
of `M(a')` at a random `a' ∈ F_p^9` off `{p=0}`.

## 3. Verification

The session-49 verifier (`tools/verify/`) **does not exist in the tree at
`eb8cecb`** — session 49 has not been run; only its brief is committed.  This is
recorded as a finding.  In its place:

- an **independent re-implementation** of the divisibility test (`_v2`, a
  different route: form `G` by a second method — Bareiss/interpolation vs
  cofactor — and reduce) cross-checks every headline remainder;
- **two primes** for every `r = 0` claim, plus an **exact-rational**
  reconstruction of the control-1 quotient `G/det_4` on a random line as a
  positive check that the division is exact over `Q`;
- a **rank/Hessian audit**: the Hessians are checked by finite symbolic identity
  on `det_2`/`per_2` analogues where the answer is known.

## 4. Sizing (Task 2), pre-registered as an expectation

`a(λ,δ)`, `n_χ` (by the session-46 generator walk, never `N_S/|Stab|`), `N_S`,
`h_pad`, and the shape of the `i_det` linear system are reported **with numbers**
for `λ = (65,17,2⁷)`, `δ = 24`, `N = 16`.  Prediction: **out of reach by many
orders of magnitude** (the point of the session is that evaluation via
divisibility sidesteps exactly this).  No engine run is attempted on it.

## 5. Constraints honoured

Deliver by bundle; do not push.  `Co-Authored-By` trailer only; no session-link
trailer or URL anywhere.  Every long run bounded by `timeout` + `ulimit -v` with
its pid in `results/logs/`; ended only by recorded pid.  No committed file
> 5 MB.  `python-flint` for exact linear algebra.  Single-writer files
(`paper/*.tex`, `PROJECT_NOTES.md`, `docs/boundary_deficit.html`) untouched.
