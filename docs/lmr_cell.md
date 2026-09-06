# The LMR cell — what is known, and why it is the programme's first positive control

`λ = (65, 17, 2⁷)`, `δ = 24`, `ℓ(λ) = 9`, `|λ| = 96 = 4δ`.  This is the weight
`Ω(k, d)` of Landsberg–Manivel–Ressayre at `n = 4`, `k = 6`.

## 1. Why r = 9 and not less

`docs/equation_census.md` (session 55) establishes two conditions on the LMR
family at `n = 4`.  Containment of the orbit closure in the dual-defective locus
forces `k ≥ min(6, r−2)`; non-vacuity of the module forces `k ≤ r−3`, because
`ℓ(λ(k,4)) = k + 3` and a weight longer than `r` carries no `S_λ(C^r)`.  For
`r ≤ 8` the two are incompatible and the family is empty.  At `r = 9` they
pinch: `k ≥ 6` and `k ≤ 6`, so `k = 6` exactly and `ℓ(λ(6,4)) = 9 = r`.

**`r = 9` is therefore the smallest length at which any equation the programme
knows of is non-vacuous.**  Every cell measured to date has `r ≤ 6`, where the
family is empty by the above — which is the structural reason the record reads
`i_det = 0` at all 210 six-row cells rather than a sign that something is wrong.

## 2. The two numbers

**Source dimension `a = 274`.**  `a((65,17,2⁷), 24) = 274`, computed by the
integrator (session 50 review) with the Kostant-alternation plethysm engine at
nine variables, using multiplicity stability in the variable count (the value is
independent of `N` once `N ≥ ℓ(λ) = 9`).  This retired session 50's estimate
that the cell was "~10²⁰ and out of reach"; it is a two-minute computation.

**Target dimension `sk((65,17,2⁷), 24⁴) = 48,825`**, with `g = 92,000` and the
transpose part `T = 5,650`, so `sk = (g + T)/2`.  Reported independently by two
external routes: a first-row Jacobi–Trudi reduction whose cost is driven by the
tail `|λ̄| = 31` rather than by `N = 96`, and a Manivel rectangular-stability
reduction to `dim S_ρ(sl_4)^{GL_4}` at `ρ = (17, 2⁷)`.

**`g = 92,000` is confirmed here by a third route** (§3).  `T = 5,650` is not;
it rests on the two external routes, so `sk = 48,825` is `g` at three routes
plus `T` at two.

So the determinant block is `Θ⁺_LMR : C²⁷⁴ → C^{48825}` — 13.4 million entries
dense, but the rank is at most 274, so the target coordinates need not all be
materialised at once.

## 3. The boundary question, and its answer

Manivel's reduction

    g((4δ − |ρ|, ρ), (δ⁴), (δ⁴))  =  dim S_ρ(sl_4)^{GL_4}          (2δ ≥ |ρ| + ρ_1)

is stated with a weak inequality, and **the LMR cell sits at exact equality**:
`ρ = (17, 2⁷)`, `|ρ| = 31`, `ρ_1 = 17`, `|ρ| + ρ_1 = 48 = 2δ`.  Every cell used
to calibrate either external route sits in the interior (slack 2, 5, 6, 8).  A
method calibrated in the interior and applied on the boundary is exactly the
kind of thing that fails silently, so the boundary was tested here directly.

The LMR cell belongs to a family that lies on the boundary identically:

    λ = (3k + 2m, k, 2^m)   at   δ = k + m,   ρ = (k, 2^m),
    |ρ| + ρ_1 = 2k + 2m = 2δ.                    LMR is k = 17, m = 7.

Ground truth for the small members was computed by the direct `p(4δ)` character
sum — no stability hypothesis anywhere — and compared against Manivel's formula
evaluated by a plethysm on the adjoint of `sl_4`:

| `k` | `m` | `δ` | `λ` | `g` (character sum) | `dim S_ρ(sl_4)^{GL_4}` | `sk` |
|---|---|---|---|---|---|---|
| 4 | 2 | 6 | `(16,4,2,2)` | 20 | **20** | 18 |
| 4 | 3 | 7 | `(18,4,2,2,2)` | 61 | **61** | 47 |
| 5 | 3 | 8 | `(21,5,2,2,2)` | 110 | **110** | 77 |
| 5 | 4 | 9 | `(23,5,2⁴)` | 311 | **311** | 197 |
| 6 | 4 | 10 | `(26,6,2⁴)` | 657 | **657** | 410 |

**Five out of five, on the boundary.  The weak inequality is the right one and
the LMR cell is inside the hypothesis.**  `sl_4` is also the right algebra, not
`gl_4`: the `gl_4` invariants give 55, 187, 418, 1241, 2744 and match nothing.

The same engine at `ρ = (17, 2⁷)` returns **`dim S_ρ(sl_4)^{GL_4} = 92,000`**
in 267 s (35,470 prefix nodes, modular arithmetic at `p = 2³¹ − 1`, the answer
far below the modulus).  That is `g` at the LMR cell, by a route independent of
both external ones.

The cell cannot be reached by descending in `δ`: the same tail at `δ = 12, 13,
14` gives `g = 5241, 29326, 50660` and `sk = 2714, 15383, 26654`, still
climbing, exactly as a cell below its stability threshold should.

## 4. Why this cell is worth the 274 × 48,825

The Foulkes identification is `mult_det = rank Hom_{S_{4δ}}([λ], Θ⁺_δ)`, so
`i_det = a − mult_det = 274 − rank`.  By §1, the LMR module is non-vacuous at
this cell and only at lengths `r ≥ 9`, which means

    i_det ≥ 1  at the LMR cell, by theorem.

**No other cell in the programme has a theorem-guaranteed `i_det > 0`.**  Every
measured cell has `i_det = 0`, and a rank engine that has only ever been shown
full-rank data has never been tested against a rank drop.  Running `Θ⁺` at the
LMR cell must return `rank < 274`.  If it returns 274, the engine or the
identification is wrong, and we learn that before trusting the engine anywhere
else.  This is the programme's first available positive control and it is the
reason to build the block, not the hope of a separation.

`D > 0` at the cell is a further and separate question: `D = i_det − i_pad`, and
the LMR vector shows only `I(D_9) ⊄ I(P_9)`, which is an occurrence statement.
Whether the multiplicities also separate needs `i_pad` measured at the same
cell.  Ikenmeyer–Panova is the relevant caution: multiplicity obstructions are
strictly stronger than occurrence obstructions, so the second measurement is not
implied by the first.

## 5. Provenance

`a = 274`: `/root/work/ple2.py`, integrator, session 50 review.
Boundary family ground truth: the direct character sum in `sk.py`
(Murnaghan–Nakayama, no stability), integrator.
Manivel side and `g = 92,000`: plethysm `s_ρ[ch sl_4]` expanded over partitions
of `|ρ|`, weights read off as `{x_i/x_j}_{i≠j} ∪ {1,1,1}`, trivial multiplicity
extracted as the coefficient of `x^{(3,2,1,0)}` in (character × Vandermonde);
prefix-shared DFS over partitions, `numpy` shift-adds mod `2³¹ − 1`.
Calibrated 5/5 against the ground truth above before use.
