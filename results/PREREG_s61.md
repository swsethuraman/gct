# PRE-REGISTRATION — session 61, the full polar profile of `per_3`

Committed **before** any computation of this session. Branch `s61-polar`, off
`main` at `0960bd548eae4a9767276f9a1f20d686538c3374` (the tip of `work/main`
as staged at session start; `work/` had been fast-forwarded from `0f8c08a` to
`0960bd5` by a pull of `gct_housekeeping.bundle` about twenty minutes before the
session opened — the sync baseline for rule 10 is therefore `0960bd5`).

Nothing below has been measured at the time of this commit. The only arithmetic
done while drafting is stated in §0 as hand derivation and is re-derived by
script before it is used anywhere.

## 0. Prior information carried into the session

### 0a. The object and the convention (fixed here, used verbatim in the report)

For a hypersurface `X = {F = 0} ⊂ P^N` of degree `d`, the conormal variety
`C(X) ⊂ P^N × P^N*` is the closure of `{(x, [∇F(x)]) : x ∈ X_smooth}`; it has
dimension `N − 1`. Its **polar profile** is

    δ_k(X) = ∫ [C(X)] · h^{N−1−k} · ȟ^{k},      k = 0, …, N−1,

`h`, `ȟ` the hyperplane classes of the two factors. Equivalently, `δ_k` is the
number of points `x ∈ X_smooth` with `x ∈ Λ` and `∇F(x) ∈ Λ̌`, for a generic
linear `Λ ⊂ P^N` of dimension `k+1` and a generic linear `Λ̌ ⊂ P^N*` of
codimension `k`; equivalently the class (degree of the dual) of a generic
`(k+1)`-dimensional linear section of `X`. Standard consequences, used as
checks: `δ_0 = d`; `δ_k = 0` for `k > dim X*` and `δ_{dim X*} = deg X*`;
`δ_k = d(d−1)^k` whenever `codim_{P^N} Sing X ≥ k + 2`; `δ_k ≤ (d−1) δ_{k−1}`
(the polar variety `P_k` sits inside `P_{k−1}` cut by one more form of degree
`d−1`); read backwards the profile is the profile of `X*`.

This is the convention under which the brief's determinant profile reads
`(δ_0, …, δ_6) = (4, 12, 36, 68, 84, 60, 20)`, `δ_7 = 0`: `δ_0 = deg det_4`,
`δ_6 = deg(P^3 × P^3) = C(6,3) = 20`, `δ_7 = 0 ⟺ dim X*_det = 6`.

### 0b. Two elementary lemmas the comparison rests on (proved in the report)

**Cone/union lemma.** If `Y ⊂ P^n` is a hypersurface and `X ⊂ P^{n+1}` is the
cone over `Y`, then `(δ_0, …, δ_n)(X) = (δ_0, …, δ_{n−1}(Y), 0)`; and the
profile of a reducible hypersurface is the sum of the profiles of its
components. Hence the padded permanent `{x_0 · per_3 = 0} ⊂ P^15` (a cone with
`P^5` vertex over the reducible `P^9` hypersurface `{x_0 = 0} ∪ cone(per_3)`)
has profile

    (1 + δ_0(per_3), δ_1(per_3), …, δ_7(per_3), 0, …, 0) = (4, δ_1, …, δ_7, 0, …),

which is why the brief's componentwise comparison of `(δ_0, …, δ_7)(per_3)`
against `(4, 12, 36, 68, 84, 60, 20, 0)` is the right comparison, with the one
book-keeping shift that slot 0 of the padded quartic is `3 + 1 = 4`, equal to
the determinant's.

**Specialisation inequality.** If `F_t → F_0` is a one-parameter degeneration
of hypersurfaces of `P^N` (for us: a curve `g(t)·det_4` in the orbit tending to
the padded permanent), then `δ_k(X_0) ≤ δ_k(X_t)` for every `k`: the flat limit
of the conormal cycles is an effective cycle of the same multidegrees, and it
contains `C(X_0)` as a union of components (over every smooth point `x` of `X_0`
the pairs `(x_t, [∇F_t(x_t)])` with `x_t ∈ X_t`, `x_t → x`, converge to
`(x, [∇F_0(x)])`). This is the whole "conormal specialisation" input the session
needs, and it does **not** depend on the preprints of §0e. Consequently
`P ∈ closure(GL_16 · det_4)` forces `δ_k(P) ≤ δ_k(det_4)` for all `k`, and a
slot with `δ_k(P) > δ_k(det_4)` is an obstruction.

### 0c. What is already known about the two profiles

- `δ_7(det_4) = 0`, `δ_7(per_3) > 0`: `dim X*_det = 6` (`rank Hess det_4 = 8`
  on the rank-3 sheet, s55 M2) while `rank Hess(x_0·per_3) = 9` on the
  permanent sheet (s50, Katz; identity `det H_P = −(3/2) x_0^8 per_3 det H_{per_3}`
  in the integrator notes), so `dim X* = 7` for the pad. This slot separates and
  is the LMR dual-defect condition again (`docs/external_reviews_round3.md` §3).
- An external review reports `δ_7(per_3) = 6` from four prime/patch/coefficient
  choices, labelled a computational measurement. **Goal to reproduce or refute,
  not an input.**
- Hand derivation while drafting (to be re-derived by script, §2 M1): for the
  smooth Segre `P^3 × P^3 ⊂ P^15`, the polar degrees of a smooth `m`-fold,
  `μ_k = Σ_{i=0}^{k} (−1)^i C(m−i+1, k−i) ∫ c_i(T) h^{m−i}`, give
  `μ_0 = 20`, `μ_1 = 7·20 − 80 = 60`, `μ_2 = 21·20 − 6·80 + 144 = 84`, i.e. the
  brief's vector read backwards, as it must be (profile of `X*` = reversed
  profile of `X`). The remaining four entries were not computed by hand.
- Hand derivation while drafting: the two lowest non-smooth slots of `det_4`
  are explained by its singularities — the generic `P^4`-section has exactly
  `deg(rank ≤ 2 locus) = 20` ordinary nodes, each costing 2 (Teissier), so
  `δ_3 = 4·27 − 40 = 68`; and the generic `P^5`-section has a smooth curve of
  transversal `A_1` points of degree 20, for which Piene's polar formula with
  Aluffi's Milnor class and `Eu = 2` gives `δ_4 = 4·81 + 20·(2·5 − 2 − 5·4) = 84`.
  Both agree with the brief's vector; both are re-derived in the report.

### 0d. The singular locus of `per_3` — what we expect, stated before computing

The partials of `per_3` are the nine `2×2` sub-permanents. Expected (from the
structure of the permanental ideal `P_2` of a `3×3` matrix, Laubenbacher–Swanson
2000, *recalled, not re-read*): `Sing(per_3) ⊂ P^8` has **15 components of
projective dimension 2**: three planes `{two rows = 0}`, three planes
`{two columns = 0}`, and nine smooth quadric surfaces `{row i = 0, column j = 0,
complementary 2×2 permanent = 0}`; total degree `3 + 3 + 9·2 = 24`;
codimension **6** in `P^8`. At a general point of every component the
hypersurface has a **transversal `A_1`** singularity (the local equation is
exactly a rank-6 quadratic form in the six normal directions), so
`rank Hess(per_3) = 6` there. The components meet pairwise along 18 lines
(`{two rows = 0, one column = 0}` and transposes), each on exactly three
components, where the transversal type degenerates (Hessian rank 4).

### 0e. The citation that must not be built on

The proposing session cites arXiv:2606.13628 and arXiv:2606.15970 (Sheshadri,
June 2026) for a conormal specialisation theorem. The integrator failed to
locate either in six attempts. This session will make one more attempt (§2 M8)
and record the outcome verbatim. Nothing in §0b or in any conclusion depends on
them; the inequality actually needed is the elementary one stated above.

### 0f. House pre-checks

- `docs/brief_wording.md` **§5** (degeneracy direction) and **§7**
  (functoriality). Both are answered in §2 M7 before any statistic is developed
  further, and again in the report.

## 1. What this session will and will not do

It will compute eight numbers for `per_3`, eight for `det_4`, compare them, and
give a verdict. It will not develop characteristic-cycle or vanishing-cycle
machinery, will not attempt an algebraisation, and will not open a broader
microlocal programme. If a slot `k ≤ 6` violates, the report will *estimate*
the degree at which the corresponding closed condition could be algebraised,
with the basis of the estimate stated; it will not construct the equations.

## 2. The measurements, fixed now

**Method.** Saturated polar ideals: on a generic linear `Λ ≅ P^{k+1}` (random
integer basis, seeded), the ideal `(F|_Λ, m_1(∇F|_Λ), …, m_k(∇F|_Λ))` with
`m_i` random linear combinations of the partials of `F`, saturated with respect
to the ideal of all partials of `F` restricted to `Λ` (the excess locus is
exactly `Sing(X) ∩ Λ`; legitimate points have `∇F ≠ 0`). The count is the
degree of the saturated zero-dimensional projective scheme, read two ways:
the projective degree (Hilbert polynomial), and `vdim` on a random affine chart
`ℓ_0 = 1` ("patch"). Reducedness is checked by comparing with the degree of the
radical. Engines: **Singular 4.3.2** as primary; **Macaulay2 1.22** as an
independent second implementation of the same method on every non-trivial slot
(different code base, different Gröbner engine); a third, methodologically
different route where feasible — the multidegree of the conormal ideal itself
(elimination in the bigraded ring), which produces the whole profile at once.
Exact arithmetic throughout: `Z/p` at **both house primes `2147483647` and
`2147483629`**, and over `Q` wherever the computation finishes inside the time
bound. Every run bounded by `timeout` and `ulimit -v`, process id recorded to
`results/logs/s61_<run>.pid`, ended only by that id. Seeds: 61, 62, 63 for
coefficient choices; two affine charts per seed. `python-flint` for the exact
linear algebra of the smooth-Segre formula and the Hessian ranks.

### M1 — the determinant profile from the smooth Segre side (calibration, theory)

Compute `μ_k(P^3 × P^3)` for `k = 0..6` exactly from
`c(T) = (1+a)^4 (1+b)^4`, `h = a + b`, `∫ a^3 b^3 = 1`.

- **Prediction (prior 0.9):** `(μ_0, …, μ_6) = (20, 60, 84, 68, 36, 12, 4)`,
  i.e. the brief's `(4, 12, 36, 68, 84, 60, 20)` reversed.
- **Falsifier:** any other vector. Then either the brief's profile or the
  convention of §0a is wrong, and the session stops to find out which before
  touching the permanent.

### M2 — the determinant profile by the saturation method (calibration, computation)

`F = det_4` in 16 variables, `k = 0..7`, both primes, seeds 61–63, two charts.

- **Prediction (prior 0.9):** `(4, 12, 36, 68, 84, 60, 20, 0)` at every prime,
  seed and chart, every saturated scheme reduced.
- **Falsifier:** any slot off at any setting. A method that cannot reproduce a
  profile known in closed form is not applied to the permanent; the session
  stops and repairs the method first.
- Also recorded: `k = 3` — the `P^4` section has exactly 20 singular points,
  all with Hessian rank 4 in the section (nodes); `k = 4` — the singular curve
  of the `P^5` section has degree 20.

### M3 — the singular locus of `per_3`

Minimal primes of the ideal of the nine `2×2` sub-permanents over `Q` and
modulo both primes; dimension and degree of each; `rank Hess(per_3)` at a
random point of each component; the pairwise intersections.

- **Prediction (prior 0.8 on the exact list, 0.9 on codimension 6):** as in
  §0d — 15 components of dimension 2, degrees `1^6 2^9`, total 24, Hessian
  rank 6 at general points of all fifteen, rank 4 on the 18 intersection lines.
- **Falsifier:** a component of dimension `≥ 3` (then the smooth range shrinks
  and M4 changes), or a component with Hessian rank `≠ 6` generically (then M5's
  Teissier count changes).

### M4 — `δ_0, …, δ_4` of `per_3`

By the saturation method, both primes, seeds, charts; and by Bézout, since
`codim Sing = 6 ≥ k + 2` for `k ≤ 4` leaves no excess.

- **Prediction (prior 0.95 given M3):** `(3, 6, 12, 24, 48)`. Each is below the
  determinant's `(4, 12, 36, 68, 84)`; **no violation is possible in slots
  0–4.**

### M5 — `δ_5` of `per_3`

Saturation method as above; and independently `3·2^5 − 2·24 = 48` by Teissier's
formula for a hypersurface with isolated `A_1` points (the generic `P^6` section
meets the 2-dimensional `Sing` in `deg Sing = 24` points, each an ordinary node
since the section misses the 1-dimensional special strata). Recorded alongside:
the 24 singular points of one explicit section and their Hessian ranks.

- **Prediction (prior 0.75):** `δ_5(per_3) = 48`, below the determinant's 60.
  **No violation at slot 5.**
- **Falsifier:** any other value — then either M3 is wrong or the saturation
  method mishandles isolated excess, and the two routes disagreeing is itself
  the finding.

### M6 — `δ_6` and `δ_7` of `per_3` — the decisive slots

Saturation method at both primes, seeds 61–63, two charts each, Singular and
Macaulay2; radical check; conormal-multidegree route if it finishes; for `δ_7`
additionally the degree of the dual hypersurface by implicitisation of
`A ↦ ∇per_3(A)` on `{per_3 = 0}` (independent of the polar count).

Constraints the results must satisfy (checked, not assumed):
`δ_6 ≤ 2 δ_5`, `δ_7 ≤ 2 δ_6`, `δ_6 ≤ δ_7(δ_7 − 1)`, `δ_5 ≤ (δ_7 − 1) δ_6`
(the last two are the same inequality read from the dual side).

- **`δ_7`:** the external value 6 is the goal. **Prediction (prior 0.5):**
  `δ_7(per_3) = 6` is reproduced at every prime, seed, chart and engine. The
  complementary 0.5 is a different value — most likely the external run's
  saturation or its characteristic. Either way `δ_7 > 0 = δ_7(det_4)`, the
  known dual-defect separation (prior 0.99).
- **`δ_6`:** the only slot `k ≤ 6` where a violation is still possible after
  M4–M5. Bracket, fixed now: `0 ≤ δ_6 ≤ min(96, δ_7(δ_7 − 1))`; if `δ_7 = 6`,
  `δ_6 ≤ 30`. **Prediction (prior 0.6): `δ_6(per_3) ≤ 20`, no violation.**
  Basis, stated honestly as weak: (i) for the pure case of a smooth singular
  curve of transversal `A_1` points, the Piene–Aluffi formula of §0c gives
  `192 + 24·(2·7 − 2 − 7·3) = −24 < 0`, so `δ_6` is small and owes its very
  non-negativity to the 18 special points of the section, each of which would
  have to contribute more than `44/18` for a violation; (ii) if `δ_7 = 6` the
  dual is a sextic hypersurface whose generic plane section is a plane sextic,
  class `30` minus `2` per node and `3` per cusp, and the dual is expected to
  be singular (it contains six planes of hyperplanes tangent along `P^5`'s).
  **Falsifier and the best outcome:** `δ_6(per_3) > 20`. Then there is a
  conormal inequality independent of dual defect, and the report estimates the
  algebraisation degree of `{F : δ_6(F) ≤ 20}` (a closed, `GL_16`-invariant
  condition containing `D_16` by §0b).

### M7 — the two house pre-checks, run on the statistic itself

Degeneracy direction (§5): the full profile at (1) a `det_4` pencil in 16 and
in 10 variables (a generic linear section truncates the profile), (2) a
reducible `ℓ·c` with `c` a generic cubic in 10 variables, (3) the full
ten-variable `x_0·per_3` — the last two computed directly by the saturation
method as well as by the cone/union lemma, so the lemma is itself tested at the
padded point.

- **Prediction:** (2) gives `(4, 6, 12, 24, 48, 96, 192, 384, 768)` (hyperplane
  plus smooth cubic 8-fold), exceeding the determinant from slot 5 on — the
  reducible generic quartic in `r ≥ 7` variables is not a border determinant,
  consistent with `dim R_r > dim D_r` there; (3) gives `(4, δ_1, …, δ_7(per_3), 0)`.
  The padded permanent is **less** degenerate than the determinant in this
  statistic (its profile is not componentwise `≤`), so the statistic points the
  right way; prior 0.95.

Functoriality (§7): passes by §0b ("specialises in a controlled direction under
degeneration"); the proof is written out in the report. Prior 0.99 that it
survives an adversarial reading.

### M8 — the citation

One attempt each: arXiv listing/abs pages for 2606.13628 and 2606.15970, an
author/title search. Record verbatim what comes back. **Prediction (prior
0.8):** neither identifier resolves to a paper on conormal specialisation. If
one does, record identifier and a quoted theorem statement; the session's
conclusions are unchanged either way.

### M9 — the verifier

This session produces no `gct-cert/1` certificate: its claims are polar counts,
not highest-weight-vector, matrix-rank or full-rank claims, and no cell reports
`D > 0`. `tools/verify/verify.py` is run on the 50 committed certificates as a
regression on this branch (prediction: 50/50 pass, prior 0.95), and the report
states explicitly that no new certificate was produced and why. The session's
own reproducibility artefacts are the seeded scripts, the logs, and
`results/s61_profiles.json`.

## 3. Standing predictions about the session's own conclusion

1. **Slots 0–5 of `per_3` are clean** (below the determinant): prior 0.9.
2. **The branch retires** — every slot `k ≤ 6` satisfies the determinant bound
   and only `δ_7` differs, so the whole microlocal signal at `(3,4)` is the
   dual-defect condition already algebraised by LMR at degree 24: prior 0.6.
3. **The alternative** — `δ_6(per_3) > 20`, a second conormal signal: prior 0.4.
   It would be the best outcome and would be reported as such, with the
   algebraisation-degree estimate.
4. The external `δ_7 = 6` is reproduced: prior 0.5.
5. The determinant calibration reproduces the brief's vector at the first
   attempt: prior 0.85 (the residual is method bugs, not mathematics).
6. Macaulay2 and Singular agree on every slot they both finish: prior 0.95.

A refutation of any of these is a result and will be recorded as one.
