# Session 51 — the `Λ⁵` structure derived from the resolution, and the rank
# condition it produces separates the wrong way

Branch `s51-lambda5`, off `eb8cecb`.  Pre-registration `results/PREREG_s51.md`
(commit `f60c463`, before any result below).  Code
`analysis/wk9_s51_resolution.py`, `analysis/wk9_s51_module.py`,
`analysis/wk9_s51_precheck.py`, verifier `tools/verify_s51.py`; logs under
`results/logs/s51_*`; the exact syzygy in `results/s51_r5_syzygy.json`.
Labels: **proved / measured / certified / adopted-from-literature / expectation**.

Convention: `F = det_n` on a generic `r`-pencil `M(s) = Σ sᵢ Aᵢ`, `d = 3n−5`.
`ρ_d = dim Sym^d ℂ^r − h_d`, `h_d = [t^d]((1−t^{n−1})/(1−t))^r`.
`drop = ρ_d − rank M_d(F)` = non-Koszul syzygies of the `r` partials in degree `d`.

## 0. Verdict

> **The `C(r,5)` drop is derived from the Gulliksen–Négård resolution, not read
> off a rank, and the module is identified: it is `Λ⁵` of the pencil space,
> `dim = C(r,5)`, with the "5" equal to `codim(Σ_{n−2}) + 1 = 4 + 1` (independent
> of `n`).**  This settles what session 48 left open (its A2/A3): the equivariant
> type is `Λ⁵`, proved — not by transporting one pencil, but by the
> dimension-polynomial argument, and directly at `r = 5` where the syzygy line is
> `SL₅`-invariant of centre-weight `−5 = det^{−1}`.
>
> **The `r = 5` syzygy is exhibited exactly and verified over ℤ** (independent
> checker `tools/verify_s51.py`, clean).  A short **closed form** in the pencil is
> **not** obtained: one-adjugate words, two-adjugate `(adj·linear)` words, the
> `tr(adj·A·M·A)` family, and the Hessian image `H·q` were each tested and each
> captures **zero** of the one non-Koszul dimension — consistent with s48's
> exhaustion of the one-adjugate ansatz.  The syzygy is genuinely not a simple
> word.
>
> **`(5,7)` consistency holds:** `dim Λ⁵ℂ⁷ = C(7,5) = 21`, the s48-measured value,
> reproduced here at both primes.
>
> **§4b — the step the brief called the one that matters most — is settled in the
> negative, and this is the session's most consequential output.**  The mandated
> degeneracy-direction pre-check was run first, as the gate.  At the committed
> ten-variable test set (`d = 7`, both house primes):
>
> | quartic (r = 10) | Macaulay drop at d = 7 |
> |---|---|
> | generic (control) | 0 |
> | **det₄ pencil** | **980** |
> | reducible `ℓ·c` | 1536 |
> | **full 10-var `ℓ·per₃`** | **2141** |
>
> The padded permanent is **strictly more degenerate** than the determinant
> (`2141 > 980`); even a reducible quartic (`1536`) is.  A `rank Ψ_f ≤ R` condition
> is closed and passes to the border, but here it separates in the **wrong
> direction**: any upper bound on rank that `det₄` satisfies, the more-degenerate
> `ℓ·per₃` satisfies too.  **Per the pre-registered stop rule, §4b halts.**  The
> `Λ⁵`-syzygy route — the brief's best hope for a determinant equation below
> degree 24 — is therefore **not a candidate obstruction**.  It is the same
> phenomenon as Proposition D (s48): determinant type is *less* singular than the
> padded permanent, and every excess-singularity statistic points the wrong way.

## 1. The drop from the restricted Gulliksen–Négård resolution *(proved / measured)*

`F = det_n` on a generic pencil.  The `r` partials `∂ᵢF = tr(adj(M) Aᵢ)` (Jacobi)
are `r` generic linear combinations of the 16 restricted cofactors
`c_{ab} = ι#(3×3 minor)`, which generate `I₃(M)·S` — the ideal of the submaximal
minors, cut down to the pencil.  Write `U = ⟨c_{ab}⟩ ≅ ℂ¹⁶`, `P = ⟨∂ᵢF⟩ ≅ ℂ^r`
(a generic `r`-subspace of `U`).  A syzygy of the partials at internal degree `d`
is exactly `ker(Ψ)_d ∩ (P ⊗ S_{d−3})`, where `Ψ` presents the 16 cofactors, and
`ker(Ψ)` is the first-syzygy module of `I₃·S`.

**Tor vanishing (proved, and verified).**  `Σ_{n−2} = {rank ≤ n−2}` has
codimension 4; for a generic pencil `V` meets it in the expected dimension, so the
`16−r` linear forms cutting out `V` are a regular sequence on the
Cohen–Macaulay ring `R/I₃`.  Hence `Tor^R_{>0}(R/I₃, S) = 0` and the **restricted
Gulliksen–Négård complex resolves `S/I₃·S`**:

```
0 → S(−8) → S(−5)¹⁶ → S(−4)³⁰ → S(−3)¹⁶ → S → S/I₃·S → 0,
```

giving `γ_d := dim(S/I₃·S)_d = Σ_j (−1)^j β_j·dim S_{d−shift_j}`, Betti–shift
`1(0), −16(3), 30(4), −16(5), 1(8)`.  This was checked against the measured
minor-ideal corank at **ten** `(r,d)` pairs — `(4,7),(5,7),(6,7)`,
`(5,5),(5,6),(5,8),(6,5),(6,6),(6,8),(7,7)` — **all agree** (e.g. `r=5` gives
`γ=20` constant in `d`, the 20 nodes; `r=6` gives `80,100,120,140` at `d=5..8`).
`analysis/wk9_s51_resolution.py`, `results/logs/s51_closedform_probe.log`.

**The drop, from the resolution.**  With `P ⊂ U` generic,

```
drop_d = (γ_d − h_d) + e_d,   e_d = dim coker( ker(Ψ)_d → (U/P) ⊗ S_{d−3} ),
```

every term a resolution quantity.  At `n = 4`, `d = 7`:

| r | γ₇ (restricted GN) | h₇ | γ₇−h₇ | e₇ | drop | C(r,5) |
|---|---|---|---|---|---|---|
| 4 | 0 | 4 | −4 | 4 | 0 | 0 |
| 5 | 20 | 30 | −10 | 11 | 1 | 1 |
| 6 | 120 | 126 | −6 | 12 | 6 | 6 |

and at `(n,r,d) = (5,10,7... )` the `(5,7)` case gives drop `21`.  The drop equals
`C(r,5)` throughout the **non-ceiling regime** (`ρ_d < dim S_d − H_{GN}(d)`).

**The regime, and the negative control.**  `C(r,5)` is the drop only where the
Gulliksen–Négård ceiling does not bind.  At `n = 3` (also `codim Σ_{n−2} = 4`,
`d = 4`) the drop is `1, 9, 26` at `r = 5, 6, 7` — equal to `C(r,5)=1` only at
`r=5`; at `r=6,7` the ceiling binds and the drop exceeds `C(r,5)`.  So the clean
statement is exactly "in the non-ceiling range," matching s48's remark that the
`(5,7)` slack `+293` is what made that test clean.

**`5 = codim + 1`.**  The "5" is not `n+1` (it is the same 5 at `n = 3` and
`n = 4`); it is `codim(Σ_{n−2}) + 1 = 4 + 1`, the hallmark of the top of a
length-4 (codimension-4) resolution — the Gulliksen–Négård tail `S(−8)` — met by a
generic linear space.  This is why `Λ⁵`, and why it is `n`-independent.

## 2. The module is `Λ⁵` *(proved)*

The non-Koszul syzygy space `E(V)` is a polynomial `GL(V)`-functor of the
`r`-dimensional space `E` of linear forms (choosing a pencil basis is choosing an
isomorphism `E ≅ ℂ^r`; `E` transforms accordingly).  It sits inside
`E ⊗ Sym⁴ E` — a polynomial functor of **degree exactly 5** — so `dim E(ℂ^r)` is a
polynomial in `r` of degree **≤ 5**, hence determined by **six** values.  Measured
(all in the non-ceiling regime, `analysis/wk9_s51_module.py`):

```
r    = 2  3  4  5  6  7
drop = 0  0  0  1  6  21   =   C(r,5)   exactly.
```

Six points pin `dim E(ℂ^r) = C(r,5)` as polynomials.  Among Schur functors the
dimension polynomials `{dim 𝕊_λ(ℂ^r) : |λ| ≤ 5}` are linearly independent, and the
only non-negative integer combination equal to `C(r,5)` is `𝕊_{1⁵} = Λ⁵`.  **So
`E ≅ Λ⁵E`** (character `e₅`, the 5th elementary symmetric polynomial), up to the
determinantal twist fixed by the internal grading.  (No `r = 8` point is needed:
the ambient degree bound makes six points sufficient; `r=8` was attempted for
over-determination and is not required.)

**Direct confirmation at `r = 5`.**  There `E` is one-dimensional, so `SL₅` acts
trivially and the centre `t·I` acts by the ambient weight `t^{−5}` on
`E ⊗ Sym⁴E`; a one-dimensional `GL₅`-representation with centre-weight `−5` is
exactly `det^{−1} = Λ⁵E`.  This is the "equivariant type identified" that s48
recorded as needing a construction — obtained here without one, from the weight
alone.

**`(5,7)` consistency test (required, brief §4).**  The module predicts
`dim Λ⁵ℂ⁷ = C(7,5) = 21`.  Re-measured this session at `(n,r,d) = (5,7,10)`,
both house primes: **drop = 21**.  Consistent; the module is not falsified.

## 3. The `r = 5` syzygy: exact, ℤ-verified; closed form open *(measured / proved)*

At `(n,r,d) = (4,5,7)` the non-Koszul syzygy is unique up to scale
(`dim Syz₇ = 51 = 50` Koszul `+ 1`).  It is extracted exactly over ℚ (fmpq rref
nullspace, reduced modulo the Koszul lattice) and cleared to a primitive integer
tuple `(g₀,…,g₄)`, `gᵢ ∈ S₄`; `results/s51_r5_syzygy.json`.

**ℤ-verification (proved).**  `Σ gᵢ ∂ᵢF = 0` as an exact identity over ℤ — every
coefficient, not mod p.  Re-checked by the independent verifier
`tools/verify_s51.py` (shares no code with the worker toolkit): it recomputes the
pencil's determinant from scratch and confirms the recorded pencil really is
`det₄`; that each `gᵢ` is homogeneous of degree 4; the exact-ℤ annihilation; a
Schwartz–Zippel ℤ evaluation at six random integer points; and that the syzygy is
outside an independently rebuilt Koszul span at both primes.  All pass
(`results/logs/s51_verify.log`).

**Closed form — not obtained (brief §3, P4).**  For a generic pencil the exact
coefficients have large height (no small representative exists), so a closed form
must be a *formula* in the pencil, not numbers.  Four natural ansätze were tested
and each captures **zero** of the one non-Koszul dimension:
`ℓ(s)·Aₐ adj(M) A_b` (one adjugate); `gₐ = (adj entry)·(linear)` (two adjugates,
word shape); `T_{ab} = tr(adj(M) Aₐ M A_b)`; and the Hessian image `{H·q}`.  This
is consistent with s48 having ruled out the whole one-adjugate word ansatz: the
syzygy is not a simple matrix word.  The resolution does give its provenance — it
is an `S`-combination of the 30 Gulliksen–Négård first-syzygies (the relations
`M·adj(M) = adj(M)·M = F·I`) supported on the pencil — but not a short formula.
**Recorded open.**

## 4. §4b — the Fitting condition separates the wrong way *(the decisive result)*

The brief asked, as "the step that matters most," to convert the module into a
closed condition `rank Ψ_f ≤ R` on the coefficients of `f`, with `Ψ_f` built from
`f` alone, and to report its Fitting degree — after running the
degeneracy-direction pre-check (requirement 3) **first**.

**The pre-check is the gate, and it fails.**  The statistic `Ψ_f` refines is the
degree-`d` Macaulay rank-drop of the Jacobian ideal of the quartic `f`.  Evaluated
at the committed ten-variable test set (`r = 10`, `d = 7`, seeds `5100/5107/5108/
5109`, both primes; `analysis/wk9_s51_precheck.py`):

| f (quartic in r = 10 vars) | drop at d = 7 |
|---|---|
| generic (control) | 0 |
| det₄ pencil | 980 |
| reducible `ℓ·c` | 1536 |
| full ten-variable `ℓ·per₃` | 2141 |

Both primes agree exactly, so these are the generic ranks.  `drop(ℓ·per₃) = 2141`
is far larger than `drop(det₄) = 980`: **the padded permanent is strictly more
degenerate than the determinant under this statistic**, and so is a mere reducible
quartic.  A rank condition `rank Ψ_f ≤ R` is closed and passes to the border (as
required, and unlike a graded-Betti / semicontinuity argument, which the brief
warned against and which we did not use) — but a closed *upper* bound on rank that
`det₄` satisfies is satisfied *a fortiori* by the more-degenerate `ℓ·per₃`.  The
condition cannot vanish on `D_r` without vanishing on `P_r`.  **Per the
pre-registered stop rule, §4b halts here.**

**What this means for the programme.**  The `Λ⁵`-syzygy route was the brief's best
candidate for a determinant equation below degree 24.  It is not one: it separates
in the wrong direction, for the same structural reason as Proposition D (s48) —
determinant type is *less* singular than the padded permanent, so every
excess-singularity / Milnor-corank statistic ranks the permanent as "more special."
The honest Fitting degree of the only condition actually available (the Macaulay
minors, `Ψ_f = M_d(f)`) is the cap size `ρ_d − drop + 1` — at `r = 6`, `d = 7`,
the certified `661` (s49's correction of the repository's `666`); it is
`built from f alone` and closed, but by the pre-check it does not separate, so it
does not make `cap ≤ 661` a *lower*-bound obstruction theorem.  A genuinely smaller
`Ψ_f` would require the closed-form `Λ⁵` map (§3, open) — but the pre-check shows
that even if found, the resulting rank condition would separate the wrong way.
**This route is closed.**

## 5. Pre-registration scorecard

| id | prediction | prior | outcome |
|---|---|---|---|
| P1 | drop `= C(r,5)`, regime stated | 0.90 | **confirmed** (`0,0,0,1,6,21`; `n=3` ceiling control) |
| P2 | derived from restricted GN, not a rank | 0.80 | **confirmed** (Tor-vanishing at 10 `(r,d)`; `5 = codim+1`) |
| P3 | `r=5` syzygy exact + ℤ-verified | 0.90 | **confirmed** (independent verifier clean) |
| P4 | closed **form** for the `r=5` syzygy | 0.25 | **not achieved** (four ansätze excluded; recorded open) |
| P5 | module is `Λ⁵` (equivariant type) | 0.70 | **confirmed** (dimension polynomial + centre-weight at `r=5`) |
| P6 | `(5,7)` consistency `= 21` | 0.90 | **confirmed** |
| P7 | Fitting degree + pre-check gate | 0.95 run / 0.15 small | **pre-check RUN, GATE FAILED**: `ℓ·per₃` (2141) ≫ `det₄` (980); route separates the wrong way, §4b halts |

## 6. For the integrator

- s48's A2/A3 (the `Λ⁵` equivariant type) can be marked **resolved**: the module
  is `Λ⁵` of the pencil space, proved by the dimension-polynomial argument, and
  directly at `r=5` by the centre-weight.  The drop `C(r,5)` is now **derived**
  from the Gulliksen–Négård resolution in the non-ceiling regime, not measured.
- **The `Λ⁵`-syzygy → rank-condition route is not a candidate obstruction** (§4,
  pre-check).  It should be recorded alongside Proposition D as another instance of
  the general fact that excess-singularity statistics separate the wrong way at
  `n = 4`.  It does **not** promote `cap ≤ 661` to an obstruction theorem.
- The session-49 verifier does not yet exist in the tree (`tools/verify/` absent,
  no `docs/s49_report.md`, no `results/certs/`); this session used an independent
  `tools/verify_s51.py` to the s49-brief spec.  The `1148 proved / 661 certified`
  cap numbers are adopted from the s49 brief, not re-derived here beyond the
  Hilbert functions of §1.
- Open: a closed **form** for the `r=5` syzygy (P4).  Its value is now lower, since
  §4b shows the rank condition it would build separates the wrong way regardless.
