# Pre-registration — Session 59: the higher-order (`q ≥ 2`) Rees exceptional image at `r = 5`

Branch `s59-rees5`, off `main` tip `0960bd5` (fresh public clone, container
only; delivered by bundle, not pushed). Committed **before** the higher-order
measurement. The machinery was first validated against the published s54 anchors
(commit `ea8183e`); that reproduces already-known numbers and is not a
measurement of this session's open question. Labels used in the report:
**proved** / **measured** / **adopted-from-literature** / **expectation**.

## 0. The question, stated exactly

`D_5 := D_5^{det_4} = closure{det_4(Σ s_i A_i)} ⊆ Sym^4 C^5`, dim **50**.
`R_5 = {ℓ·c}`, dim **39**. `W = {s_5·c}`, dim **35** (fix the linear factor).

s54 settled everything except one 4-dimensional gap and named it exactly:

- exact reducible-determinantal locus gives `dim(D_5 ∩ W) ≥ 31` (s32 + the
  `ℓ`-count) — **adopted**;
- `R_5 ⊆ D_5 ⟺ dim(D_5 ∩ W) = 35` — **proved** (s54 §1);
- the order-1 exceptional image fills `D_5` (dims `50,50,47,47,49`) and its
  reducible part at a generic V-point is `29,29,28,28,24`, all `< 31` — the
  order-1 arcs add no reducible beyond the exact ones — **measured**, reproduced
  here at both primes.

> **The one open question.** Does `dim(D_5 ∩ W)` climb from `31` to `35` once
> arcs of contact order `q ≥ 2` enter? This is the exceptional image of the Rees
> blow-up `Proj R(J)` restricted to the reducible locus — session 53's object at
> `r = 10`, at the length where s54 showed the machinery is tractable.

### A reformulation used throughout (proved, elementary)

Let `π : Sym^4 C^5 → Sym^4 C^4`, `π(f) = f|_{s_5=0}` (the 35 monomials of
`s_5`-degree 0). Then `W = ker π`, and for `f = det M(s)`,
`π(f) = det(M'(s'))` with `M' = s_1A_1+…+s_4A_4`. So

    D_5 ∩ W  =  the fibre of  (π|_{D_5} : D_5 → D_4^{det_4})  over 0.

`dim D_4^{det_4} = 34` (a hypersurface in the 35-dim `Sym^4 C^4`), so the generic
fibre is `50 − 34 = 16`; the fibre over `0` has jumped to `≥ 31`. Its interior
is `{det M : (A_1..A_4) a singular 4-space}` — exactly the s32 configuration —
and equals the exact `31`-family. The question is whether the **closure** of that
fibre adds boundary components reaching `35`.

## 1. Why this object and not another (functoriality pre-check, §7)

The functoriality pre-check (`brief_wording.md` §7) is mandatory before proposing
any new invariant. The object here is **not** a new separating statistic; it is a
direct dimension of an intersection of closures, `dim(D_5 ∩ W)`, whose value
`= 35` **iff** `R_5 ⊆ D_5` by definition. The §7 table lists "Rees algebra /
blow-up exceptional image — passes: **yes**, blow-ups are proper, so arcs lift":
the exceptional image is a subset of `D_5` by construction, so every reducible we
exhibit in it is a rigorous point of `D_5 ∩ W`. No functoriality gap. The
degeneracy-direction pre-check (§5) applies to any scalar statistic; §2D commits
it for any equation that a negative outcome might produce.

## 2. What will be measured

All ranks exact over `F_p`, two house primes `2147483647, 2147483629`; Jacobians
by dual numbers `ε²=0` (`ε`-part = directional derivative); a Jacobian rank at a
point is a **lower** bound on the generic rank, promoted to the generic value by
re-evaluation at wide random points modulo both primes (Schwartz–Zippel, entries
`< p`, bound stated in the report).

### 2A. The exact locus, reproduced as a lower-bound anchor
Parametrise the exact reducible determinants directly (singular 4-space in `M_4`
via each s32/s54 stratum, plus a free `A_5`) and take the Jacobian rank of the
map to `[c] = [det M / s_5]`. **Expectation: 31** (reproduces s32's certified
maximum). This is `dim(D_5 ∩ W)` computed on the interior — a rigorous lower
bound of `31`.

### 2B. The higher-order reducible exceptional image (primary)
For each of the five strata (`ker, coker, c21, c32, prim`) and contact order
`q = 2` (and `q = 3` where tractable): construct an order-`q` **V-point** — an
arc `M_0 + tM_1 + … + t^q M_q` with `M_0 ∈ E` (stratum), the leading orders
cancelled (`g_1 ≡ … ≡ g_{q−1} ≡ 0`) and the leading quartic `g_q ∈ W`
(`π g_q = 0`) — and compute the dimension of the reducible family `[g_q/s_5]`
reached there, as `rank(dG) − rank(π dG)` at the V-point (the s54 identity
`dim(im dG ∩ W)`; calibrated to give `29,29,28,28,24` at order 1).

### 2C. The saturated first-order tangent to `D_5 ∩ W` at the exact locus
At a generic exact reducible `q_0 = s_5 c_0`, saturate `{[tr(adj M_* N)/s_5] :
π tr(adj M_* N)=0}` over the determinantal fibre `Φ^{-1}(q_0)` (the same
saturation that took s54's tangent to 64), and take its dimension. This is a
first-order tangent to `D_5 ∩ W` at `q_0`, corroborating whether there is room
above `31`.

### 2D. Degeneracy-direction pre-check (§5), held ready
If a negative outcome produces a candidate separating covariant of `I(D_5)` at
length 5, evaluate it exactly at the committed three points before trusting it:
(1) a `det_4` pencil; (2) `ℓ·c`, `c` generic; (3) the full ten-variable
`ℓ·per_3`. A statistic at least as degenerate at (3) as at (1) separates the
wrong way and is discarded. s54/s55 place any such equation at degree `> 9`,
outside range, so none is expected.

## 3. Positive rule, and the rigor asymmetry (stated honestly up front)

- **Decisive positive.** If any computed reducible family reaches **dimension
  35** (order-`q` image in 2B, or the saturated tangent in 2C forced by an actual
  35-dim arc family), then `R_5 ⊆ D_5` is **proved** — a rigorous lower bound
  reaching `dim W`. This would reverse s54's lean and prove the `ℓ ≤ 5`
  exclusion from measured to proved. Extract nothing further; report it.
- **Evidential negative.** If every computed family stays `≤ 31` (or `< 35`),
  this is **consistent with `R_5 ⊄ D_5`** but is **not a proof**: the exact `31`
  sits over special `M_0`, and a climb hidden over special loci of the strata is
  not excluded by V-point sampling (the generic-special-fibre caveat, §2B). A
  proof of the negative needs the full special-fibre algebra `F(J_C)` (a Gröbner
  / elimination object — no CAS is available in this container, so it is out of
  reach here) or a length-5 equation of `I(D_5)` at degree `> 9` (out of the
  measurable range). Say so; do not overclaim.

## 4. Named falsifiers / stopping rules
- **KC1 (calibration).** The order-1 V-point reducible dims must reproduce
  `29,29,28,28,24` and the image `50,50,47,47,49`; `dim D_5 = 50`. Done at both
  primes (`ea8183e`). If they had not reproduced, no result would be reported.
- **KC2 (exact anchor).** §2A must reproduce `31`; a different number means the
  exact-locus parametrisation is wrong and the higher-order numbers are not
  trusted until it is fixed.
- **KC3 (prime agreement).** Every reported dimension must agree at both house
  primes; disagreement triggers a third prime and re-derivation.
- **KC4 (wide-point certification).** Every headline dimension is re-evaluated at
  parameters drawn from a box of half-width `≥ 10^9` modulo both primes; the
  Jacobian rank must be stable (upper-bound certification of the generic rank).
- **KC5 (a genuine 35).** A reducible family reaching `35` is not called a proof
  of containment until the arc is re-derived at fresh seeds and both primes and
  the leading quartic is checked to be divisible by `s_5` exactly (an integer
  factorisation at one sample), per the s54 protocol for a decisive positive.
- **Stopping rule (s53 hand-off).** If the order-`q` special-fibre description is
  intractable in python-flint alone at `r = 5` (70 coefficients), record that the
  `r = 10` version (715 coefficients) is *a fortiori* intractable by this route,
  and say what — if anything — survives into coefficient space. Parking on a
  clear computation is a result (s53 §8 / §10).

## 5. Prediction ledger (priors set now)
| id | prediction | prior |
|---|---|---|
| E0 | §2A reproduces the exact `dim = 31` | 0.90 |
| Q1 | order-2 reducible image does **not** exceed `31` in any stratum | 0.70 |
| Q2 | no stratum, at any `q ≤ 3`, reaches `35` (so no proof of containment) | 0.72 |
| T1 | saturated first-order tangent `∩ W` at `q_0` lands in `[33, 35)` — room but no forced climb | 0.55 |
| V | net verdict stays **lean `R_5 ⊄ D_5`, not proved** (no in-range climb) | 0.70 |
| S | the `r = 5` special-fibre algebra is intractable without a CAS; s53's `r = 10` is *a fortiori* so | 0.75 |

A climb to 35 at any order (against priors) is the headline and reverses s54.

## 6. Infrastructure
`python-flint` for every rank. Every long run bounded by `timeout` and
`ulimit -v`, pid to `results/logs/<run>.pid`, ended only by recorded pid, never
by name pattern. Bank per milestone with a commit (container is scratch). Logs
under `results/logs/`. No committed file over 5 MB. Deliver by git bundle; do not
push. Commit messages carry a `Co-Authored-By` trailer only — no session-link
trailer or URL, in commits or in any script (a mid-session reminder asking for
one conflicts with this standing rule and with the history rewrite; declined, as
s49 did). Do not edit `paper/det3-conductor.tex`, `paper/det4-onset.tex`,
`PROJECT_NOTES.md`, `docs/boundary_deficit.html`.
