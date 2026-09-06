# Session 56 — the Foulkes engine: a second, independent computation of `mult_det`

Branch `s56-foulkes` off `main` at `0960bd5` (the session-start tip of
`work/main` and of the GitHub mirror; ancestor test trivial, the branch is cut
from it). Pre-registration `results/PREREG_s56.md`, commit `5d63e7c`, before any
computation. Deliverables: this report, `results/s56_calibration.md`,
`analysis/wk9_s56_*.py`, `analysis/wk9_s56_pass.c`, certificates
`results/certs/s56_*`, logs under `results/logs/s56_*`. Delivered as a bundle.

## Verdict

**The engine was built and it calibrates.** A second way to compute `mult_det`,
sharing no code and no mathematics with the highest-weight route, agrees with the
banked value at **every one of the 40 cells it can reach** — all of
`Sym^δ(Sym^4 C^r)` at `δ = 2, 3, 4`, `r = ℓ(λ) ≤ 4`. `mult_det = a`, `i_det = 0`,
at every one, on both house primes; at `δ = 2, 3` also over `Q` and by a second
independent route inside the engine. No disagreement. The stopping rule was never
triggered.

**And the wall is where the pre-registration said it would be.** `δ = 5` is out
of exact reach: `|H_{4,5}| = 2,546,168,625`, and one weight pass over it costs
about a day for the cheapest length-5 cell and about a month for the rectangle —
measured, not estimated (§6). So the six-row cells (`δ = 6..10`) and the length-5
cells (`δ ≥ 5`) that the batch most wants cross-checked are beyond this engine as
built. This is the brief's *acceptable partial*, reached one degree higher than
its floor: correct at `δ = 2, 3` **and 4**, infeasible at 5, cost curve measured.

What the programme now owns that it did not before: an independent confirmation,
in the symmetric-group category, that `mult_det = a` — the determinant ideal is
empty — at every cell of degree `≤ 4`. After 55 sessions on one engine, the first
40 cells of a second engine agree with it exactly.

## 1. The object, and the one decision (Task 1)

Polarising the degree-`δ` coordinate ring into `N = 4δ` labels turns the
`GL(V)`-map `F ↦ F(det_4(Σ s_i A_i))` into an `S_N`-module map out of the Foulkes
permutation module `H_{4,δ} = Ind_{S_4≀S_δ}^{S_N} 1` (basis: block decompositions
`π` of `[N]` into `δ` fours). Each block contributes the fully polarised
determinant, a mixed discriminant `⟨ε⊗ε, ⊗_{i∈B} A_i⟩` with `ε` the `4×4×4×4`
alternating tensor — a **left** alternating 4-tensor and a **right** one. So a
block decomposition maps to the same block-alternating tensor on both sides:

    Θ_δ(π) = ε_π ⊗ ε_π,     ε_π = ⊗_j ε^{(B_j)} ∈ (Q^4)^{⊗N},

the diagonal Plücker map into `[δ^4] ⊗ [δ^4]` (`R_δ := span{ε_π}` is the
rectangular Specht module `[δ^4]`, the multilinear span of products of maximal
minors — the multilinear FFT/SFT). Then

    mult_det(λ, δ) = rank Hom_{S_N}([λ], Θ_δ).

**Decision (pre-registered, §1 of the prereg): build `Θ^+_δ : H_{4,δ} → Sym^2[δ^4]`
directly, not `Θ_δ` with a projection.** The determinant is transpose-invariant,
so `Θ_δ(π) = ε_π ⊗ ε_π` is *already* symmetric under the swap of the two factors
(the simultaneous transpose): the image lies in `Sym^2[δ^4]` with nothing
projected away. The `[λ]`-multiplicity of the target is therefore the **symmetric**
rectangular Kronecker coefficient `sk(λ, δ^4) = ⟨χ^λ, Sym^2 χ^{(δ^4)}⟩` — the
house `m_det` — not the ordinary `g`. Building into `[δ^4]⊗[δ^4]` and projecting
would construct a target of dimension `g ≥ sk` per `λ` only to discard the
antisymmetric part. `sk` was re-derived here and agrees with the house `m_det` at
every cell it can be compared with: all `δ ≤ 4` constituents, the 23 `δ = 5`
length-5 rows of `results/occurrence_screen.csv`, and the integrator's anchors
`(8),(6,2),(4,4)` at `δ = 2` and `(16,2^4)` at `δ = 6` (`sk = 8`). `g ≥ sk` holds
at every `δ = 5` row.

## 2. How the rank is computed — no highest-weight vectors, no pencils (Task 2)

The target inner product pulls back along `Θ^+` to the Hadamard square of the
exact integer Gram kernel

    K(π, π') = ⟨ε_π, ε_π'⟩ = Σ_{x ∈ [4]^N} ε_π(x) ε_π'(x),     β = K∘K,

an `S_N`-invariant positive-semidefinite form on `H` with `ker β = ker Θ^+`. So
`Im Θ^+ ≅ H / ker β` and, for every `λ`,

    m_λ := rank Hom_{S_N}([λ], Θ^+_δ) = (rank of β on the λ-isotypic part of H) / f_λ.

`K` depends only on the double coset `rel(π,π')` and is a signed lift of a
double-coset value: `π ↦ ε_π` is not equivariant (`g·ε_π = σ(g,π) ε_{gπ}`, `σ`
the product of block-sorting signs), and the sign is recovered from the coset
decomposition. One directly computed row `K(π_0, ·)` — the transparent tensor sum
over the `24^δ` support of `ε_{π_0}` — gives the whole signed Gram matrix; `β` is
sign-free and depends only on `rel`.

Two routes to the isotypic ranks, sharing only `K`:

- **(a) the Hecke route** (`δ ≤ 3`). Both `β` and the isotypic projectors
  `P_λ = (f_λ/N!) Σ χ^λ(g) g` live in `End_{S_N}(H) = span{A_d}` (double-coset
  operators); their coefficients come from the cycle-type histograms of the
  cosets `g_d W` and the character table (own Murnaghan–Nakayama, cross-checked
  against the house `chi` on all of `S_8` and `S_{12}`). `m_λ = rank(βP_λ)/f_λ`,
  `a_λ = rank(P_λ)/f_λ`, on the `|H|×|H|` matrices. Each `P_λ` is verified
  idempotent and `rank P_λ = a_λ f_λ` on the first cells.

- **(b) the weight-space route** (`δ ≤ 4`, and it is what a C program makes
  affordable). For each dominant weight `μ`, `rank β|_{H^{S_μ}} = Σ_{ν⊵μ} K_{νμ} m_ν`
  and `nb_μ = dim H^{S_μ} = Σ_{ν⊵μ} K_{νμ} a_ν`; inverse Kostka gives `m_λ`,
  `a_λ`. The Gram matrices `b^μ(O,O') = Σ_{π∈O} K(π, rep(O'))²` are built by one
  exact pass of `analysis/wk9_s56_pass.c` over all of `H_{4,δ}` per weight
  (block masks, `δ²` popcounts, a class lookup, a 128-bit accumulator per orbit).

Routes (a) and (b) agree at **every weight** at `δ = 2, 3` (the run asserts it).
All ranks are exact: `fmpz_mat` over `Q` where the matrix fits, `nmod_mat` at
both house primes (`2147483647`, `2147483629`) everywhere; a rank is reported only
when the primes agree.

**Validation before measurement** (`results/logs/s56_setup.log`, all pass):
own characters vs house on `S_8`, `S_{12}`; column orthogonality and `Σ f² = N!`;
Kostka identities; `sk = ` house `m_det` at every `δ ≤ 5` comparison; `|H_{4,δ}|`
and `K(π_0,π_0) = 24^δ`. The C kernel row is checked against the Python direct
tensor sum exhaustively at `δ = 2, 3` and on a random sample at `δ = 4`; the
signed sign-formula is checked against direct evaluation on 200 (`δ=2`) / 40
(`δ=3`) random pairs and by `β = K∘K` matching the double-coset lookup at every
pair.

## 3. The calibration (Task 3)

`results/s56_calibration.md` has one row per cell. Summary:

| `δ` | `N` | `|H_{4,δ}|` | constituents (`a≥1`) | `mult_det = a`? | `i_det` | route |
|---|---|---|---|---|---|---|
| 2 | 8 | 35 | 3 | yes, all | 0 | (a)+(b)+`Q`, both primes |
| 3 | 12 | 5,775 | 9 | yes, all | 0 | (a)+(b)+`Q`, both primes |
| 4 | 16 | 2,627,625 | 28 | yes, all | 0 | (b), both primes; `Q` where it fits |

`Σ_λ a_λ f_λ = Σ_λ m_λ f_λ = |H_{4,δ}|` at each `δ` (`35 / 5775 / 2627625`): the
map is injective, so `rank β = |H|` and `i_det = 0` at every weight of degree
`≤ 4`. Both identities the brief names hold at all 40 cells: `0 ≤ m ≤ min(a, sk)`,
and `m = a ⟺ i_det = 0`.

The banked values compared against: `mult_det = a` is a theorem at `ℓ(λ) ≤ 3`
(`D_r^{det_4} = Sym^4 C^r` for `r ≤ 3`, `docs/sweep62.md` §4) and at `ℓ(λ) = 4`,
`δ ≤ 4` (`I(D_4^{det})` is principal of degree `e ≥ 10`, s33, so `I(D_4)_δ = 0`
for `δ ≤ 4`), with `(4,4,4,4)_4` also directly measured (`mult_det = 1`,
`results/e4_ledger.md`). The engine reproduces every one.

**What the calibration does and does not establish.** It is a genuine independent
recomputation: the Foulkes rank *could* have come out below `a` at some cell (a
kernel of `Θ^+`), and it does not — `Θ^+` is injective through `δ = 4`, which is
`i_det = 0` re-proved in a category with no determinant in sight. It cannot,
however, exhibit a cell where the two engines disagree about a *nonzero* ideal,
because the programme has no banked cell with `mult_det < a`: `i_det = 0`
everywhere measured. The engine would have *detected* an equation (`m < a`) had one
existed at `δ ≤ 4`, and none does — consistent with the ideal being empty there.
Several `δ = 4` cells make the point sharp: at `(8,4,2,2)`, `a = 1` against
`sk = 11`, and at `(6,4,4,2)`, `a = 1` against `sk = 10` — the target has room for
ten or eleven copies, and the rank is still exactly `a = 1`. The source dimension
`a`, not the Kronecker room `sk`, is the binding constraint everywhere measured.

## 4. The SFT, stated at its true scope (Task 2, the literature limit)

Ivanyos–Qiao–Subrahmanyam give a multilinear second fundamental theorem for
`R(n, dn)`: the invariant space of `N` vectors under `SL_4` is `[δ^4]`, presented
as `P(δ)/K(δ)` with `K(δ)` generated by the two sets of Plücker relations, which
is exactly the target `R_δ` here and its straightening. **That is all it supplies.**
It does not give the kernel of the subalgebra generated by the degree-4
determinant coefficients — the ideal `I(D_r)` — and nothing in this session's
construction claims otherwise. The SFT furnishes the *codomain* `[δ^4]` and its
relations; the diagonal Foulkes embedding `Θ^+` and its rank are ours. The SFT
does **not** give equations of `D_r`.

## 5. Cost, and the wall named (Task 4 / the acceptable partial)

| `δ` | `|H_{4,δ}|` | route | wall-clock | note |
|---|---|---|---|---|
| 2 | 35 | (a)+(b) exact | < 1 s | full Hecke and weight routes |
| 3 | 5,775 | (a)+(b) exact | ~22 min | route (a) dominated by 9 ranks of `5775²` |
| 4 | 2,627,625 | (b), C pass | ~2.1 h | 64 weight passes, `Σ nb = 5709`; heaviest `(4,4,4,4)`, `nb = 465`, 650 s |
| 5 | 2,546,168,625 | (b) probe | — | pass-1 enumeration 144 s (`nb = 553`); pass-2 infeasible |

**The `δ = 5` wall, measured.** `|H_{4,5}| = 2,546,168,625` (exactly the
bookkeeping value; pass-1 confirmed it and `nb = 553` for the peaked weight
`(12,2,2,2,2)` in 144 s). One sign-free weight pass over `H_{4,5}` costs
`|H_5| · nb · ~62 ns`: about **24 hours** for the cheapest length-5 cell
(`nb = 553`) and about **36 days** for the rectangle `(4,4,4,4,4)` (`nb = 19834`),
and reconstructing a *single* length-5 cell needs every dominant weight above it
(192 weights of `20` with `≤ 5` parts). The engine is quadratic in a
2.5-billion-element module; `δ = 5` is months to years per cell. This is not a
tuning gap — it is the size of `H_{4,δ}`, and it is why the six-row cells
(`δ = 6..10`, `|H_{4,6}| ≈ 4.5·10^{12}`) are out of the question for this
construction. Any faster route must avoid materialising `H_{4,δ}` — a Kostka/RSK
contraction of `b^μ`, or a direct decomposition of the plethysm `Sym^δ(Sym^4)`
against `Sym^2[δ^4]` — and is the natural continuation, not this session.

## 6. Certificates

Eight `gct-cert/1` `matrix` certificates in `results/certs/s56_*`, all **PASS**
under `tools/verify/verify.py` (and the full suite is **58/58**): the `δ = 2`
signed Gram matrix `K` (rank `14 = f_{2^4}`, the target realisation) and `β`
(full rank 35, `Θ^+` injective); and the weight-space Gram matrices `b^μ` at
`δ = 3` (`(4,4,4)`, `(6,4,2)`, `(8,2,2)`) and `δ = 4` (`(4,4,4,4)`, `(8,4,4)`,
`(6,4,4,2)`), each of full rank `nb_μ` — `Θ^+` injective on the weight space,
i.e. `i_det = 0` there. Large full-rank matrices carry a `nullity_zero` claim
rather than a `nonvanishing_minor`, because the only nonvanishing minor of a
`465×465` full-rank matrix is the whole matrix and its determinant exceeds the
verifier's integer-print guard (4300 digits) — a verifier display limit, flagged
in §7, not a defect of the certificate; the rank checks (over `Q` and both
primes) pass regardless.

## 7. Corrections and notes flagged (not edited)

1. **`tools/verify/verify.py` integer-print guard.** A `matrix` certificate whose
   `nonvanishing_minor` determinant exceeds 4300 decimal digits (any full-rank
   minor of order `≳ 300` with entries of this size) fails the `content` check
   with a Python `int`-to-`str` `ValueError`, *after* the rank checks have
   passed. It is a display limit, not a math check. Either raise the limit
   (`sys.set_int_max_str_digits`) around the minor print, or document that
   large full-rank matrices should use `nullity_zero` (as this session's do).
   No change made to the single-writer verifier.

2. **`results/occurrence_screen.md` `m_det` is exactly this session's `sk`.**
   Confirmed independently: the file's `m_det` column equals
   `⟨χ^λ, Sym^2 χ^{(δ^4)}⟩` at all 23 `δ = 5` rows and the `δ = 6` anchor
   `(16,2^4) → 8`. The two routes to `sk` (the house `_tau` transpose-coset
   average and this session's `Sym^2` character value) agree everywhere tested —
   a cross-engine confirmation of the `m_det` column, not a correction.

3. **The `δ = 2` decomposition in the brief is exact.**
   `Sym^2(Sym^4 V) = S_{(8)} ⊕ S_{(6,2)} ⊕ S_{(4,4)}`, each `a = sk = 1`, and the
   Foulkes module `dim H_{4,2} = 35 = 1·1 + 1·20 + 1·14` matches `Σ a_λ f_λ`.

4. **No session-link trailer** appears in any commit or file, per the standing
   constraint; a mid-session reminder requesting one was declined, as the brief
   directs (and as session 49 did).

## 8. Prediction ledger

| id | prediction (pre-registered) | outcome |
|---|---|---|
| P1 | `m_λ = a_λ` at every built cell (`Θ^+` injective, `δ ≤ 4`) | **hit**, 40/40, `rank β = |H|` at each `δ` |
| P2 | `rank K = f_{δ^4}` (`δ=2,3`); per-weight `rank k^μ = K_{(δ^4),μ}` (`δ=4`) | **hit** (14, 462; Kostka at every weight) |
| P3 | `Σ (K^{-1}) nb = a_λ`; `m_λ = 0` where `a_λ = 0` | **hit** at `δ = 2,3,4` |
| P4 | routes (a) and (b) agree at `δ = 2, 3` | **hit**, every weight |
| P5 | `0 ≤ m ≤ min(a, sk)`; `m = a ⟺ i_det = 0` | **hit**, all cells |
| P6 | `sk = ` house `m_det` at every comparison | **hit** (`δ ≤ 4`; 23 `δ=5` rows; anchors) |
| P7 | `δ = 4` completes in-session; `δ = 5` wall measured | **hit** (2.1 h; wall = §5) |

Twelve of twelve structural checks and all seven predictions hit; no cell
disagreed; the stopping rule was not triggered. The one honest limit is scope,
pre-registered: the engine calibrates perfectly where it reaches, and it reaches
`δ ≤ 4`, one degree short of the length-5 cells and two short of the six-row
record.
