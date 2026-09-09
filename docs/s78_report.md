# Session 78 — r = 5 by bounded elimination

Branch `s78-elimination`, base `main = afb8c3319d3d1f3afc3d2578c8cb322f2b8a3b92`.
Pre-registration: `results/PREREG_s78.md` (committed before any elimination).
Author: Swami Sethuraman / swsethuraman@beneficus.ai / Beneficus AI.

Every row is labelled **PROVED** (exact, certified), **MEASURED** (exact at
sampled points / a certified one-sided bound), or **RECORDED** (adopted from a
prior session, not re-derived here). The house rule that no probabilistic bound
is promoted is observed throughout: the sufficient bound is `dim(D₅∩W) ≤ 34`
affine (`≤ 33` projective / in the chart), and nothing below promotes s72's
interior `31` or any sampled value.

---

## 0. One-paragraph outcome

The two mandatory controls pass (Singular/msolve smoke test; S2's verifier; the
rank-3 arc reproduced independently). The unconditional Job A (S2's two 149-variable
chart eliminations) **does not finish** in a bounded pilot, and neither does a
Gröbner dimension of the source locus, in the 2-core/7 GB container — the
pre-registered F3 outcome, with the exact residual preserved. The session's new
content is (a) a **certified reduction** of Job A from 149 variables to 98, with
the `f₀`-saturation removed, together with the clean equivalence
`W ⊆ D₅ ⇔ a 64-variable char-coefficient map is dominant`; (b) an **exact**
image dimension for the ker/coker component (28 projective, all contact orders),
which independently reproduces and sharpens S2's Theorem 5.1; and (c) a
definitive check that **no tested singular family exhibits the reversal**
`W ⊆ D₅`. Global noncontainment remains **OPEN**: proving it needs the generic
char-coefficient rank `≤ 33` (an exact image equation), which is the same wall
as Job A and as S2/s72 already reported.

---

## 1. Controls (must-pass)

| item | status | evidence |
|---|---|---|
| `Singular` 4.3.2 + `msolve` resolve and run; 10-min smoke test | PROVED | `x²+y²−1, x−y` → `2y²−1` in 0.01 s |
| S2's own verifier on S2's certificates | PROVED (reproduced) | `results/astra/S2/verify_s2.py` → ranks 9/0/3/9, tangent quotient 0, arc leading form `v·w·(y+v)(z+v)`, 24 point checks |
| **Rank-3 arc reproduced independently** | PROVED | `analysis/wk12_s78_arc_control.py`, `results/s78_arc_control.json` |

The arc control is independent of S2's code: from the base pencil in
`intermediate_rank3_arc.json` it rebuilds `M(t) = [[B, t b],[t cᵀ, t² w]]`,
confirms `det M(t)` has vanishing `t⁰,t¹` coefficients and leading form
`t²·s₅ s₄ (s₂+s₅)(s₃+s₅)` (= the block identity `t²(w det B − cᵀ adj(B) b)`),
that the base span is 5, and that the reduced map
`L_b(c') = c'ᵀ adj(B') b' mod (det B')·S₁` has rank exactly 3 (image span
`wy²z, wyz², w²yz`). Exact over `ℚ` and confirmed mod both house primes. A
pipeline that could not see this intermediate rank would not be entitled to a
global claim; ours reproduces it.

---

## 2. The certified reduction of Job A (PROVED)

`analysis/wk12_s78_structure.py`, `analysis/wk12_s78_reduction_check.py`,
`results/s78_reduced_polys.json`.

`f₀ = det(A₅)` depends only on the 16 entries of `A₅`, and the good-coordinate
ratios `F_α/f₀` are invariant under `A_k ↦ P A_k Q` because
`det(P A_k Q) = det P · det Q · det(A_k)`. On the target chart `y₀ ≠ 0` the source
point has `det A₅ ≠ 0` (the `s₅⁴` coefficient is `det A₅`), so `A₅` may be
normalized to the identity. Writing `B_k = A₅⁻¹ A_k` (k ≤ 4):

- `f₀ ≡ 1` — **the f₀-saturation disappears entirely**;
- `det(s₅ I + Σ_{k≤4} s_k B_k) = s₅⁴ + s₅³P₁ + s₅²P₂ + s₅P₃ + P₄`, where `P_j`
  is homogeneous of degree `j` in `s' = (s₁..s₄)` (`P₁` = traces, 4 coeffs;
  `P₂`, 10; `P₃`, 20; `P₄ = det(Σ_{k≤4} s_k B_k)`, 35);
- the **34 good coordinates** are the coefficients of `P₁,P₂,P₃`;
- the **W condition** `y_bad = 0` is exactly `P₄ ≡ 0`, i.e. the 4-pencil
  `(B₁,…,B₄)` spans a **space of singular matrices** `S`.

This reduces S2's 149-variable job (`u`, 79 `x`, 69 `y`) to **98 variables**
(64 `B` + 34 `y_good`), with no saturation. Verified against the direct ratio
definition at random points over `ℚ` and both primes (all good and bad
coordinates match), and the `P`-decomposition verified to reproduce the
determinant coefficient-by-coefficient.

**Equivalence (PROVED).** `W` is irreducible and `y₀` is not identically zero on
it, so `{y₀ ≠ 0}` is dense in `W`. A generic point of `W`, if it lies in `D₅`,
is an actual image point of a source point with `A₅` invertible (from `y₀ ≠ 0`)
whose first four matrices span a singular space (from membership in `W`) — i.e.
of a point of the reduced source `S`. Hence

> `W ⊆ D₅  ⇔  the char-coefficient map G: S → 𝔸³⁴ is dominant (generic rank 34)`,
> equivalently `dim(D₅∩W) = 34` affine; and `W ⊄ D₅ ⇔ generic rank ≤ 33`.

This settles the S2 §7 boundary worry **for the dimension/noncontainment
question**: because `W` is irreducible, `dim(D₅∩W)` is exactly the dimension of
the naive image of `G` on `S`; the closure/saturation subtlety only affects the
image-ideal-as-a-set computation, not the decision. (The reduction is a valid
setup simplification for the elimination; it does not by itself finish it.)

---

## 3. Bounded pilots — Job A does not finish (MEASURED, pre-registered F3)

`results/logs/pilot_chart0_outcome.md`, `results/logs/run_pilot_chart0.sh`,
`results/logs/pilot_chart0.pid`.

- S2's exact `chart_0_Q.sing` (149 vars, lex `u > x > y`) under `timeout 600` +
  `ulimit -v 6200000`. Ended at the wall-clock bound; **no output** — the first
  `std(raw)` did not complete. Peak ~4.4 GB (< the 6.2 GB cap): a **time** wall.
- The `A₅=I` reduced source-locus dimension `dim S` (64 vars, `dp`, 35 quartic
  generators) under `timeout 420` + the same memory cap: **hit the memory cap**;
  no dimension returned. Even the reduced Gröbner is out of reach in-container.

**Exact preserved residual.** No Gröbner step completed, so the residual is the
input ideal itself — `raw = (1 − u·f₀, f_α − y_α·f₀ : α=1..69)` — reproducible
in `chart_0_Q.sing` (all 15,000 determinant terms). A timeout is **not** a
reversal certificate, and none is claimed.

---

## 4. Exact per-component image dimensions (fallback, §C strata)

`analysis/wk12_s78_ker_dim.py`, `analysis/wk12_s78_compression_dim.py`,
`analysis/wk12_s78_dominance.py`; `results/s78_ker_dim.json`,
`results/s78_compression_dim.json`, `results/s78_dominance.json`.

| component of `S` | naive image dim (chart) | status | how |
|---|---:|---|---|
| **ker / coker** (common kernel / cokernel of `B₁..B₄`) | **28** | PROVED (all contact orders) | matching bounds, below |
| C21 (`B_k(U₂)⊆W₁`), fixed flag | 17 | MEASURED (certified `≥`, stable) | Jacobian rank mod both primes, 8 points |
| C32 (`B_k(U₃)⊆W₂`), fixed flag | 17 (family) / 19 (at a C32 point of `S`) | MEASURED | as above; `19 = rank dΨ − rank d·bad` at a generic C32 point |
| S2 §5 order-two image on integral-cubic ker/coker | ≤ 29 | PROVED (reproduced) | `analysis/wk12_s78_s5bound.py` |

**ker/coker = 28, exactly, all orders (PROVED).** On the common-kernel component,
after `A₅ = I`, in a frame with the kernel vector first `B_k = [[0, r_kᵀ],[0, C_k]]`
and the determinant factors **globally** as
`det(s₅I₄ + Σ s_k B_k) = s₅ · det(s₅I₃ + Σ_{k≤4} s_k C_k)` — the off-diagonal
`r_k` do not enter, and there is no contact-order/arc approximation. So the
component image is the char-variety of a 3×3 four-tuple `M₃⁴ → 𝔸³⁴`. Its
dimension is pinned by matching exact bounds:
- **upper 28**: the map is invariant under `C_k ↦ g C_k g⁻¹`; the centralizer of
  a 3×3 tuple always contains the scalar line, and is observed to equal it
  (dim 1) at an integer point, so the generic `PGL₃`-orbit has dim 8 and is
  contained in the generic fibre ⇒ image `≤ 36 − 8 = 28`;
- **lower 28**: the 34×36 Jacobian has rank 28 at an integer point mod both
  house primes (`rank_p ≤ rank_{generic}`).

This is 28 projective = **29 affine**, matching s72's *recorded* ker/coker affine
value 29, and it **sharpens S2 Theorem 5.1** (which bounded only order-two
leading forms, `≤ 29`) to the whole component at every contact order, exactly.
By transposition coker = 28.

**S2 §5 bound reproduced exactly (PROVED).** The determinant-preserving group
`GL₃×GL₃` (`det P·det Q = 1`, dim 17) acts on the 45-dim space of 3×3 linear-form
matrices with generic Lie-algebra stabilizer of dimension exactly 1 (verified at
random `L`; the scalar line is always present and 1 is attained), so orbits are
16-dim and the 3×3-linear-determinant image has dim `≤ 45 − 16 = 29`.

**On the C21/C32 numbers.** The values 17/19 are *naive image* dimensions of the
actual family (a genuine subvariety of `D₅∩W`), each `< 34`. They are a **different
object** from s72's recorded exceptional-image value 31 for those labels (a
Rees / normal-cone construction); the two are not expected to coincide and
neither is promoted. The flag-preserving conjugation parabolic (dim 11,
stabilizer at the scalar floor) gives a rigorous but loose upper bound 30 for
these families; the true naive image sits at 17–19.

---

## 5. The reversal is ruled out at every tested family (MEASURED)

`W ⊆ D₅` would require some family to fill the 34-dim chart. Computing
`image-dim = rank(dΨ) − rank(d·bad)` at generic points of ker, coker and C32
gives 28, 28, 19 — **none reaches 34**. So the reversal `W ⊆ D₅` does not occur
at any tested point: had any single point given rank 34, that would have *proved*
`W ⊆ D₅` and triggered the verification protocol; none did. This is a certified
lower bound `dim(D₅∩W) ≥ 28` and evidence for noncontainment. It is **not** a
proof of `W ⊄ D₅`: that needs the generic rank `≤ 33` (all 34×34 Jacobian minors
vanishing on `S`, i.e. an exact image equation).

---

## 6. What is proved, what is open

**PROVED this session.** The controls; the 149→98 reduction and its
`f₀`-saturation removal; the `W ⊆ D₅ ⇔ G dominant` equivalence; the ker/coker
component image = 28 exactly at all orders; the exact reproduction of S2's §5
`≤ 29`. **MEASURED.** Job A and the reduced `dim S` Gröbner both wall
in-container (F3); C21/C32 naive images 17–19; no reversal at tested families;
`dim(D₅∩W) ≥ 28`. **RECORDED (not re-derived).** s72's interior 31 and the
exceptional-image values (probabilistic, unpromoted); S2's rank dichotomy and
vertex correction (independently reviewed, not recomputed beyond §5 and the arc).

**OPEN — the wall.** A certified `dim(D₅∩W) ≤ 34` (equivalently the generic
char-coefficient rank `≤ 33`, an exact image equation / nonzero `I_h`). This is
the same object as S2's Job A and s72's global bound. Via the reduction it is now
cleanly stated as: *the map `G` from the variety `S` of 4-dimensional singular
`4×4` matrix spaces to `𝔸³⁴` is not dominant.* Its completeness half — that the
named families exhaust `S` (S2 §C6) — is precisely the **classification of
`4`-dimensional singular matrix spaces in `M₄`** (Dieudonné / Eisenbud–Harris
type), which no computation in this batch funds. The exhaustive elimination and
the structural classification are the two routes; both remain the wall, exactly
as S2 and s72 reported. The session narrows the object and removes the
saturation, and closes the ker/coker component exactly, but does not decide
`R₅ ⊆ D₅`.

---

## 7. Deliverables

- `results/PREREG_s78.md` — pre-registration (before any elimination).
- `analysis/wk12_s78_arc_control.py`, `results/s78_arc_control.json` — arc control.
- `analysis/wk12_s78_structure.py`, `analysis/wk12_s78_build_reduced.py`,
  `analysis/wk12_s78_reduction_check.py`, `analysis/wk12_s78_verify_reduced_polys.py`,
  `results/s78_reduced_polys.json` — the certified reduction.
- `analysis/wk12_s78_s5bound.py` — S2 §5 reproduced.
- `analysis/wk12_s78_ker_dim.py`, `results/s78_ker_dim.json` — ker/coker = 28 exact.
- `analysis/wk12_s78_compression_dim.py`, `results/s78_compression_dim.json` — C21/C32.
- `analysis/wk12_s78_dominance.py`, `results/s78_dominance.json` — reversal test.
- `results/logs/` — bounded-pilot launchers, pids, outputs, and outcome note.
- `s78_elimination.bundle` (+ `.md5`) — delivered against `main`.
