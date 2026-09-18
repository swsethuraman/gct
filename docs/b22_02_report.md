# B22-02 — One construction of a determinant equation of length 5–8 nonzero on padding: the gate, and the negative

18 September 2026 (UTC). Slot 02, batch 22, worktree `work/batch15_workers/B15-02`, branch
`b15-02-a1-probes`. Author: Claude (Opus 5). Theory only: the gate of §1 was not passed, so no
pilot was priced or run.

**Provenance, recorded before any write (2026-09-18T02:21:12Z):**

```
git rev-parse HEAD           7de65d7c4e08ec0142d863415daa4903a2f9c8ac   (= the starting HEAD in the launch prompt)
git rev-parse HEAD^{tree}    97263cd02ab680426f159b08683da93441034cbb
git log 7de65d7c..HEAD       empty (PART 9 adds nothing on this branch; confirmed)
git status --porcelain       only the four untracked B15 runtime receipts of 2026-09-13 under results/logs/
```

Read-only git throughout (`git show`, `git rev-parse`, `git log`, `git status`). No commit, no
push, no stash.

**Notation (G13).** The launch prompt writes `L` for the number of variables. This report writes
**`N`** for it (B20-02's convention) and does not use the letter `L` at all, so that no reader
can confuse it with the jet line or the Levi factor. `delta_0` is not used; where the det3 cubic
onset is needed (Lemma 1.6) it is written out as `onset I(D35)` and refers only to cubics.
`D45` = closure of `{det(sum_i x_i A_i)}` in `Sym^4 C^5` (dim 50); `D35` = the same for `3 x 3`
matrices in `Sym^3 C^5` (`D_5^{det_3}` of the record); `P5 = R135 = closure{l·C}` (B18-10 §9,
ADOPTED); `C*` a smooth cubic threefold, `F* = l·C*` (B17-01-C, ADOPTED: `F* ∉ D45`).

## 0. What this slot can and cannot establish

**What a positive would have been.** A polynomial `f` in the 70 coefficients of a quinary
quartic (or in those of an `N`-ary quartic, `N <= 8`), **PROVED** to vanish on `D45` (or on the
`N`-variable determinant locus), with an exhibited actual-padding point where it is nonzero.
That is a **separation**: the third of the programme's four achievements, not the fourth. It
would not be a gap. It would not select a cell. It would not bound any multiplicity. A sampled
vanishing on `D45` would have been MEASURED, never PROVED.

**What this slot delivers.** The gate was not passed. I considered thirteen candidates (§1.3).
None has an escape paragraph that survives my own reading, so the deliverable is the
**negative**: each candidate, with the sentence that kills it. The kills rest on six short
lemmas (§1.2). They are PROVED and elementary, and each is a statement about a whole class
of constructions, not about a single one:

- **Lemma 1.3 (kernel covariants).** Suppose you pull the determinant's extra structure (its
  defect syzygy, its twenty nodes, its non-Cartier divisor) out of a derivative matrix by
  linear algebra. Everything you can build polynomially from that structure vanishes on
  padding. The reason is that padding's rank is already lower than the size of the minors
  you used.
- **Lemma 1.4 (nullcone).** `l·C` is `SL_5`-unstable. So every `SL_5`-invariant vanishes on
  `P5`. And every covariant `Psi : Sym^4 -> Sym^t` of degree `e` sends `l·C` to a multiple of
  `l^{ceil((t+e)/5)}`. In particular every cubic-valued covariant sends padding **into `D35`**.
- **Lemma 1.5 (the window is exactly `N <= 8`).** The two local statistics that do bite on
  linear sections of `det_4` are vacuous exactly for `N <= 8`. They are the rank-6 bound on the
  second fundamental form, which gives the Landsberg–Manivel–Ressayre dual-defect equation
  from `N = 9`, and the rank-36 bound on the middle catalecticant.
- **Lemma 1.6 (restriction to the cubic factor).** Any separating `f` restricts, along each
  `l`, to a nonzero equation of `D35`. So `deg f >= onset I(D35)`, which is `>= 8` on the
  record. On the cubic side, though, the separation exists and runs the **right way**: the
  degree-65 cap minors of the cubic's Macaulay matrix vanish on `D35` and are nonzero at every
  smooth cubic. The reversal is a property of the quartic-side *mechanisms*, not of the
  separation problem restricted to `P5`. What is missing is a lift. Lemma 1.4 kills the
  covariant lifts, and the Nullstellensatz lift is not constructive.

**What it does not establish.** It is not a theorem that no construction exists. It gives no
equation, no degree beyond Lemma 1.6, no gap, no cell, and nothing at sixteen variables. The
kills are only as strong as their labels in §5: some are PROVED statements that a named
polynomial vanishes on padding, and some are ASSESSED statements that no recipe exists.

## 1. The gate

### 1.1 What an escape has to be, stated as a definition rather than a slogan

Let `q` be an integer-valued function of the quartic `F` (a rank, a dimension, a degree). A
closed condition on `F` extracted from `q` is always a threshold in the direction in which `q`
is semicontinuous:

- if `q` is **upper** semicontinuous (it jumps *up* on closed sets: `dim Sing X_F`, `dim H_j(F)_k`,
  the corank of any matrix built from `F`, Milnor numbers), the closed conditions are
  `{q >= c}`. They separate `D45` from a padding point `P` iff `q(P) < c <= q(generic D45)`;
- if `q` is **lower** semicontinuous (it jumps *down*: ranks, `dim X_F^vee`, the class,
  orbit dimension), the closed conditions are `{q <= c}`. They separate iff
  `q(generic D45) <= c < q(P)`.

Padding is more singular than the determinant. So every singularity-driven `q` has
`q(P) >= q(D45)` when it is u.s.c. (it fails the first test) and `q(P) <= q(D45)` when it is
l.s.c. (it fails the second). That is the direction reversal, stated as a two-line fact. The
launch prompt's first escape clause, "a quantity that *increases* with the singularity",
works only for a quantity that is **lower** semicontinuous and still larger on the more
singular form. The one example on record is `dim X_F^vee` at `N = 16`, which is LMR and
vacuous at `N = 5` (B20-02 §4). Every candidate below was read against this definition,
against the second clause (not a rank statistic of a derivative matrix) and against the third
(it uses the structure of `P5`).

### 1.2 Six lemmas the kills rest on (all PROVED, elementary, producer only)

**Lemma 1.2 (a separating polynomial is generically nonzero).** If `f(P) != 0` at one point
`P`, then `f` is nonzero on a dense open subset of `Sym^4 C^5`. In particular it is nonzero at
quartics with finite singular locus. So no polynomial can be "supported on" the
positive-dimensional part of padding's singular locus.

*Proof.* `{f != 0}` is open and nonempty in an irreducible space. ∎

**Lemma 1.3 (kernel covariants inherit the reversal).** Let `M(F)` be a matrix whose entries
are polynomials in `F`. Let `r := max_{F in D45} rank M(F)`, and let `P` be a point with
`rank M(P) < r`. Then every polynomial without constant term in the `r x r` minors of `M(F)`
vanishes at `P`. The Plücker coordinates of `ker M(F)` and of `im M(F)` at generic points of
`D45`, and every covariant built polynomially from them, are such polynomials.

*Proof.* All `r x r` minors vanish at `P`. On the open set where the rank equals `r`, Cramer's
rule and the Plücker embedding express the kernel and image through `r x r` minors. ∎

*Instance.* `M = M_7 = d_1^{(7)}`. At the two `P5` points of B20-02 `rank = 244`, and at the
P2 pencil `rank = 299`; both are exact over `Q` (B20-02 §7.3). The determinant's one extra
syzygy class at `k = 7` (its defect: `dim H_1 = 1`) is extracted by `299`-minors. So every
construction that uses that syzygy vanishes on padding. The same holds at `k >= 8` for the
ideal of the twenty nodes, which is the row space of `M_k` and is extracted by minors of size
`dim S_k - 20`. Padding's rank is lower at every `k = 5..10` computed.

**Lemma 1.4 (padding is in the `SL_5`-nullcone; covariants of padding are `l`-heavy).** Let
`lambda(s) = diag(s^{-4}, s, s, s, s) in SL_5` act by `x_i -> lambda_i x_i`. A monomial `x^beta`
of degree `t` gets weight `t - 5 beta_1` (the exponent of `s`).

(a) Every quartic `x_1 C` has only monomials with `beta_1 >= 1`, hence of weight `<= -1`. So
`lambda(s) · x_1 C -> 0` as `s -> infinity`, and `x_1 C` lies in the nullcone. `SL_5` is
transitive on nonzero linear forms up to scalars, and `P5` is the closure of the products. So
**every `SL_5`-invariant of positive degree vanishes on `P5`**, including every equation of
`D45` in a rectangular cell `((4d/5)^5)`.

(b) Let `Psi : Sym^4 C^5 -> Sym^t C^5` be an `SL_5`-equivariant polynomial map, homogeneous of
degree `e` in `F`. Then `Psi(l·C)` is divisible by `l^{a}` with `a >= ceil((t+e)/5)`.

(c) A `GL_5`-covariant `Psi : Sym^4 -> Sym^3` of degree `e` has `4e = 3 + 5k` with `k >= 1`.
Its constituent `S_{(3+k, k^4)}` has five rows, so `e >= 5`, and `e ≡ 2 mod 5` gives `e >= 7`.
Hence `Psi(l·C) = l^2 · m` with `m` linear (or `0`). That is a product of three linear forms,
equal to `det diag(l, l, m)`, and lies in `D35`.

*Proof of (b).* Equivariance gives `Psi(lambda(s)·F) = lambda(s)·Psi(F)`. Take `F = x_1 C`.
Every coefficient of `Psi` is a degree-`e` polynomial in coefficients of weight `<= -1`, so the
left side has only `s`-exponents `<= -e`. On the right, the coefficient of `x^beta` carries
`s^{t - 5 beta_1}`. Hence it vanishes unless `t - 5 beta_1 <= -e`. For a general `l`, conjugate
by `SL_5`. ∎ *(Part (c) uses only that `Sym^e(Sym^4)` has constituents with at most `e` rows.)*

The record already has the instance "padding ceiling `U = 0` in `(4^5)`" (B19-02 §8.1). Part (a)
is its uniform form for every rectangle.

**Lemma 1.5 (why the window is `N = 5..8`).** Let `F = det_4 ∘ Lambda` with
`Lambda : C^N -> Mat_4` linear. Then:

(i) at every point `x` of `X_F` with `rank Lambda(x) = 3`, the second fundamental form of `X_F`
is the pull-back of that of `X_det`. The latter has rank `6`: at `A = diag(1,1,1,0)` the
tangent hyperplane is `b_44 = 0` and the form is `-sum_{i<=3} b_{i4} b_{4i}`. So `rank II_F <= 6`
on the space `T_x X_F / <x>`, which has dimension `N - 2`;

(ii) the middle catalecticant `Cat_{2,2}(F) = (Sym^2 Lambda)^T Cat_{2,2}(det_4) (Sym^2 Lambda)`
has rank `<= 36`. That is the number of `2 x 2` minors of a `4 x 4` matrix; they have disjoint
monomial supports, so they are independent. The source space has `dim Sym^2 C^N = N(N+1)/2`.

Both bounds are **vacuous exactly for `N <= 8`** (`N - 2 <= 6` and `N(N+1)/2 <= 36`). Both bite
from `N = 9`. Bound (i) is the right-way LMR statistic, and padding's second fundamental form is
nondegenerate. Bound (ii) is reversed: for `z per_3` the span of second partials is smaller
than 36. ∎ So in the window, neither the classical right-way local statistic nor the classical
flattening sees anything. The window is not an accident of the record.

**Lemma 1.6 (restriction to the cubic factor).** Let `f in I(D45)_d` with `f(l·C*) != 0` for one
`l` and one smooth `C*`. Then for that `l` the polynomial `C -> f(l·C)` is a nonzero element of
`I(D35)_d`. Hence `d >= onset I(D35)`. Moreover the restricted problem separates in the right
direction: the size-65 minors of `M_4(C)` (the degree-4 Macaulay matrix of the five partials of
a quinary cubic, `75 x 70`) vanish on `D35`, and some of them are nonzero at every smooth cubic.

*Proof.* For `C = det_3(M(x))` we have `l·C = det_4 diag(l, M(x))`, which lies in `D45`. This
identity is on record (`sweep62.md` l.175). So `f(l·C)` vanishes on the image, hence on its
closure `D35`. It is nonzero at `C*` and homogeneous of degree `d` in `C`. The vanishing of the
65-minors on `D35` is the record's cap theorem at `n = 3`
(`onset_conjecture.md` Theorem 1, `cap(3) = 65`). The record labels it "proved modulo Kleiman,
Dimca and Gulliksen–Negård, all adopted". At a smooth cubic the five partials form a regular
sequence and `dim (S/J_C)_4 = [t^4]((1-t^2)/(1-t))^5 = 5`, so `rank M_4(C) = 70 - 5 = 65`. ∎

The value of `onset I(D35)` is not recomputed here. The record's bracket is `8 <= onset I(D35) <= 65`
(`onset_conjecture.md` §0, ADOPTED record-internal, UNREAD at its source "paper 1"). The
resulting `deg f >= 8` is weaker than the onset conjecture's `> 300` for five-row equations
nonzero on padding. It is recorded because it is proved, not because it is informative.

**Fact 1.7 (the hyperplane-section discriminant vanishes on padding).** Let
`Delta_F(xi) := Disc(F|_{xi = 0})`, the covariant of degree `108` in `F` and in `xi`. Then
`Delta_{l·C} ≡ 0`. If `H != {l = 0}`, the section `(l·C)|_H` is singular along the curve
`{l = C = 0} ∩ H`. If `H = {l = 0}`, the section is identically zero. For generic `F in D45`,
`Delta_F != 0` by Bertini: a general hyperplane misses the finitely many nodes. ∎

### 1.3 The candidates, and the sentence that kills each

Labels: **PROVED-kill** means a lemma shows that the natural polynomial of the candidate
vanishes on padding, or that the candidate is contained in an exclusion. **ASSESSED-kill** means
no recipe that outputs a polynomial in the coefficients exists on record or here, or its
separation is undecided and unpriced. No row is "unassessed".

| # | candidate | killing sentence | label |
|---|---|---|---|
| 1 | Rank thresholds of `d_1` (Macaulay/Jacobian minors), every `k`, `N = 5, 16`, including the cap minors | Theorems A/B put every rank-threshold ideal of `d_1` in `I(D45) ∩ I(P5)`: padding's `rank M_k` is `<=` the determinant's at every `k`. | PROVED-kill (record) |
| 2 | Rank thresholds of `d_j`, `j >= 2` | In five variables their ideals on `D45` are zero (B20-02 Thm 6.4), and at `N = 16`, `k = 8` no reversal (`13490 < 15660`, B20-02b). | PROVED-kill (record) |
| 3 | Minors of `d_j^{(k)}` of size `<= rho_j(k)` (or of `d_1` of size `<= r_det(k)`) vanishing on `D45` for non-rank reasons (B20-02 §8) | "Being a minor" supplies neither the vanishing on `D45` nor the nonvanishing on padding. The candidate is the unrestricted search of `I(D45)` inside the `GL_5`-span of minors, with no mechanism named. By the onset conjecture any padding-nonzero member has size `> 300`. | ASSESSED-kill (no mechanism) |
| 4 | Class of `X_F^vee` (its degree) | The class is l.s.c. and *drops* on padding (68 generic nodal against 24 for `l·C`, B20-02 §4). The closed condition `class <= 68` holds on padding: §1.1 in the wrong direction. | PROVED-kill (given the two classes; Teissier SECONDARY, not load-bearing) |
| 5 | `dim X_F^vee` | Both are hypersurfaces at `N = 5` (B20-02 §4). It is vacuous in the whole window by Lemma 1.5(i): the right-way statistic first bites at `N = 9`. | PROVED-kill |
| 6 | Hyperplane-section discriminant `Delta_F` and anything built polynomially from it (e.g. "`Delta_F` has twenty squared linear factors") | `Delta_{l·C} ≡ 0` (Fact 1.7), so every polynomial in its coefficients without constant term vanishes on `P5`. | PROVED-kill |
| 7 | Higher tangency loci (hyperplanes whose section has a worse singularity, bitangent hyperplanes) | Every hyperplane section of `l·C` is singular along a curve, hence of infinite Milnor number, so every hyperplane lies in every closed tangency locus cut out by a Milnor-number threshold. Closed conditions "the locus has dimension `>= e`" hold on padding with `e = 4`. For type-specific loci the needed adjacency is not established and no recipe is priced. | PROVED-kill for Milnor-number loci; ASSESSED-kill for type-specific ones |
| 8 | Chow form of `Sing X_F` | The 0-cycle Chow form of the twenty nodes is extracted from `J_F` by minors of size `dim S_k - 20` (Lemma 1.3), or as the trailing coefficient of a generalised characteristic polynomial at the determinant's excess order. Both vanish on padding, whose excess is larger. A Chow form of the *surface* part is excluded by Lemma 1.2: a polynomial nonzero on padding is nonzero where `Sing` is finite. | PROVED-kill (via 1.2, 1.3) |
| 9 | `GL_5`-isotypic structure of `H_1(F)` | For fixed `F`, `H_1(F)` is not a `GL_5`-module. Its equivariant versions are Fitting-ideal conditions `dim H_1(F)_k >= c` (u.s.c.; padding is larger: 6, 24, 56, 98 against 0, 0, 1, 5 at `k = 5..8`, exact, B20-02 §7.3), or covariants of the syzygy class, which are `299`-minors and vanish on padding (Lemma 1.3). | PROVED-kill |
| 10 | The determinantal sheaf itself: a rank-one ACM/Ulrich sheaf, a non-Cartier Weil divisor (the Bordiga-type surfaces cut by `3 x 4` submatrices), the rational parametrisation `P^3 -> X_F` by the `4 x 4` minors of a `4 x 5` linear matrix | On a hypersurface with isolated singularities the extra divisor class is detected by the defect, which Dimca turns into the degree-`3n-5` Milnor jump (record mechanism, `onset_conjecture.md` §0), a rank threshold: row 1. Padding is reducible and so has a non-Cartier Weil divisor automatically. The containment forms ("`X_F` contains a member of family `Sigma`") hold on padding whenever the closure of `Sigma` has members inside a hyperplane, which is undecided and unpriced; and they are eliminations with no degree on record. | ASSESSED-kill |
| 11 | Invariant theory through `ker phi^*` (the only membership mechanism that is not a derivative matrix): SL_5-invariants, the counting criterion, Theorem 7.1 certification | `SL_5`-invariants vanish on `P5` (Lemma 1.4(a)). The counting criterion is provably silent below 320112 at `N = 4` and measured moving away from firing at `N = 5` (B19-02 §§5–6). Certification needs a cell with `a > s` or the Missing Lemma (B19-02 §7.3), neither known. | PROVED-kill (invariants); ASSESSED-kill (the rest, record) |
| 12 | Astra's verbatim exclusions (equations among allowed jets; descent between parameter points of a limit fibre; special-locus cancellations) | These name what Astra 8.1–8.3 do not reach on the *source* side (the space `M` of semi-invariant functions on pencils). They are not recipes. A coefficient-side polynomial comes out of them only through `ker phi^*` (B19-02 Lemma 3.1), which is row 11. No degree, cell or construction is attached to any of them on record, and I cannot supply one. | ASSESSED-kill |
| 13 | Restriction to the cubic factor (uses the structure of `P5`): lift a right-way equation of `D35` (the n = 3 cap minors, Lemma 1.6) to an equation of `D45` | This is the one candidate with an escape on its restricted problem: smooth `C*` is *less* singular than a det3 cubic. It has no lift. A covariant lift `f = e ∘ Psi`, `Psi : Sym^4 -> Sym^3`, sends padding into `D35` (Lemma 1.4(c)) and so vanishes there, *before* one asks for `Psi(D45) ⊆ D35`, for which no `Psi` is known. The lift that exists (Nullstellensatz: `e^m` lies in `I(D45)` restricted to `P5` once `e` vanishes on `D45 ∩ P5`) is not constructive, and it needs `D45 ∩ P5`, which is not determined (it contains `{l·C : C in D35}` of dimension 32; whether it is larger is open). | PROVED-kill (covariant lifts); ASSESSED-kill (the rest) |

Two further non-candidates, recorded so nobody re-proposes them. Rationality of `X_F` and the
intermediate Jacobian (Clemens–Griffiths) separate `D45` from `l·C*` in fact: determinantal
quartic threefolds are rational through the kernel map, and smooth cubic threefolds are not.
But neither is a polynomial condition on the coefficients, and specialisation results for
rationality do not address reducible fibres. The Hessian determinant and the polar map are
l.s.c. degree statistics that drop, or tie, on padding (§1.1).

### 1.4 Non-coverage, for the record

The prompt asks why Theorems A, B, Astra 8.1–8.3, B20-02 Thm 6.4 and the onset cap do not
already cover the construction. That question applies only to a surviving candidate, and none
survived. The table above states, row by row, which of those results or which lemma does the
killing. Rows 3, 7 (type-specific), 10, 12 and 13 (Nullstellensatz part) are not covered by any
of the five. They are killed as *constructions*, for lack of a recipe, not excluded as
*mechanisms*. That is the exact residue a future slot could reopen (§4).

### 1.5 Price

No candidate passed the gate, so no construction is priced and no pilot is run. The launch
prompt's rule applies: an empty slot beats a survey.

## 2–3. The pursuit

None. No computation was run in this slot.

## 4. Exact scope

**Established (PROVED, elementary):**
- Lemma 1.2 (a separating polynomial is generically nonzero).
- Lemma 1.3 (kernel covariants inherit the reversal), with the `M_7` instance resting on
  B20-02's exact ranks.
- Lemma 1.4: `P5` is in the `SL_5`-nullcone; covariants of `l·C` are divisible by
  `l^{ceil((t+e)/5)}`; cubic-valued covariants send `P5` into `D35`.
- Lemma 1.5: vacuity of the rank-6 second-fundamental-form bound and of the rank-36 middle
  catalecticant bound exactly for `N <= 8`.
- Lemma 1.6: restriction to the cubic factor, `deg f >= onset I(D35)`. It is conditional on the
  record's cap theorem at `n = 3` only for the "right way" clause.
- Fact 1.7: `Delta_{l·C} ≡ 0`.

**Assessed, not proved.** Thirteen candidates each have a killing sentence (§1.3). The
ASSESSED-kills say that no recipe exists on record or here. They do not say that the
mechanism is impossible.

**Not established.** No equation of `D45` nonzero on padding. No statement that none of length
5–8 exists (B18 F2 says one does, conditional on refined Bézout). No degree bound beyond Lemma
1.6. No determination of `D45 ∩ P5`. Nothing at `N = 16` or for `N = 6, 7, 8` beyond Lemma 1.5.
No gap, no cell, no carrier.

**Reopening conditions.** A named polynomial construction for one of rows 3, 7, 10, 12 or 13 with:
(i) a membership proof for `I(D45)` that does not pass through `r_det`-minors of a derivative
matrix (Lemma 1.3), through an `SL_5`-covariant into a determinantal locus (Lemma 1.4), or
through `Delta_F` (Fact 1.7); and (ii) a stated reason the value at `l·C*` is nonzero. For
row 13 the smallest concrete question is the determination of `D45 ∩ P5` as a set: is it
exactly `{l·C : C in D35}`?

## 5. Labelled ledger (all rows producer only, G18)

| # | claim | status |
|---|---|---|
| L1 | §1.1: separation by a semicontinuous statistic needs an l.s.c. quantity larger on padding or a u.s.c. quantity smaller on padding | PROVED (definitions) |
| L2 | Lemma 1.2 | PROVED |
| L3 | Lemma 1.3; instance at `M_7` using `rank 244` (padding) and `299` (P2 pencil) | PROVED; instance rests on B20-02 §7.3 CERTIFIED exact ranks |
| L4 | Lemma 1.4(a)–(c): nullcone; `l`-divisibility of covariants; cubic covariants send `P5` into `D35` | PROVED (Hilbert–Mumford weight count; the plethysm row bound is UNREAD-CLASSICAL) |
| L5 | Lemma 1.5: the rank-6 II bound and rank-36 catalecticant bound are vacuous exactly for `N <= 8` | PROVED |
| L6 | Lemma 1.6: restriction lands in `I(D35)`; `deg f >= onset I(D35)` | PROVED; the right-way clause is CONDITIONAL on the record's cap theorem at `n = 3` (ADOPTED, record labels: modulo Kleiman, Dimca, Gulliksen–Negård); `onset I(D35) >= 8` ADOPTED record-internal |
| L7 | Fact 1.7: `Delta_{l·C} ≡ 0`, `Delta_F != 0` generically on `D45` | PROVED (Bertini for the second clause, UNREAD-CLASSICAL) |
| L8 | Rows 1, 2, 5, 6, 8, 9 of §1.3 | PROVED-kill (record theorems or L2–L7) |
| L9 | Row 4 | PROVED-kill given the two class values (B20-02 §4; Teissier SECONDARY/UNREAD, illustrative) |
| L10 | Rows 3, 10, 12; the type-specific part of 7; the non-invariant part of 11; the Nullstellensatz part of 13 | ASSESSED-kill (no recipe; not an impossibility) |
| L11 | No equation of length 5–8 nonzero on padding produced; gate not passed | — |

Literature at the point of use (G14/G14′). Landsberg–Manivel–Ressayre (the dual-defect
statistic) is UNREAD-SPECIALIST and not load-bearing: Lemma 1.5(i) is proved self-contained.
Clemens–Griffiths is UNREAD-SPECIALIST and not load-bearing (a non-candidate). Teissier's class
formula is SECONDARY/UNREAD and illustrative only. Hilbert–Mumford, Bertini, Cramer/Plücker and
the Pieri/plethysm row bound are UNREAD-CLASSICAL. No specialist text was needed for any PROVED
row except through the record's own ADOPTED labels in L6.

## 6. Resources, receipts, manifest

**Numerical runs: none.** Wrapped launches 0 of 3; wall 0 s of 180 s; no unwrapped computation
(G19). Before deciding not to run, I checked the batch's one-job rule:
`..\B15-01\results\logs\b22_01_*.pid` did not exist, and `Get-Process python*` returned 0
processes (2026-09-18T02:21Z). The session ran only reading, text search, hashing and
read-only git. G19 says these need no wrapper.

| action | kind | receipt |
|---|---|---|
| `git show` / `git rev-parse` / `git log` / `git status` | read-only git | this section |
| `sha256sum` of the inputs below; of this report | hashing | `results/b22_02/MANIFEST.json` |

**Inputs read, hashed from the git object store (sha256):**

| input | pin | sha256 |
|---|---|---|
| `docs/b20_02_report.md` | `7de65d7c` | `15ef389b5eb84074e77f2bd88c2dd5e98b14399a394d150b05f2b1b3f2baeda2` (matches B20-02b's quoted prefix) |
| `docs/b20_02b_report.md` | `7de65d7c` | `60ff4be461ad1f3b4733fdec36372bf0f0af3612a31f8a48af6260c49b5902ea` |
| `docs/b19_02_report.md` | `7de65d7c` | `52a9e47409acef8294cf79c2795d50ff97432d0a84758abb016ccc5e2dddb62e` |
| `docs/b21_10_review.md` (§7–§9) | `f7727cb7` | `ce2814c74be173b8569e7c5aec5670a34e2bc2911c90d1fe6426e65a03de28e5` |
| `docs/b20_10_review.md` (§9 gates) | `6915ae6f` | `021be68f748e8f05e0c8efcd7c50bd58bede1a34b420c2632f3006612fb3a5fa` (matches B20-02's pin) |
| `docs/onset_conjecture.md` (§0–§2.1) | `82633a60` | `e43237da22f4f1f9260a01e5d5fd4bd41828c29aa6cdf0f8b6ac7c282214f49f` |
| `docs/det_onset.md` (§0–§1) | `82633a60` | `da9f8f73f80128d8c9811b821abc6defd024ee7d2329db933692106eff4097a3` |
| `docs/post_b19_20260917/astra_gkz_degenerations_20260917/REPORT.md` (§8) | `82633a60` | `c79145e0077beeb05527a970529d9822e5c331043dd977827b7ef38459563c5c` (matches B20-02's pin) |

`sweep62.md` l.175 was located by text search in sibling worktrees and is cited only for the
block-diagonal identity, which Lemma 1.6's proof re-derives in one line. The corrigendum was
not re-read. Its C1–C12 are used only as B20-02 §2 states them.

**New files:** `docs/b22_02_report.md` and `results/b22_02/MANIFEST.json`. Nothing under
`results/b20_02*/` was touched. The four 2026-09-13 receipts are pre-existing. Git read-only;
no commit.
