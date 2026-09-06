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

**`g = 92,000` is confirmed here by a third route** (§3).  `T = 5,650` is not
reachable independently here; it rests on session 58's reduction and the Manivel
route, with session 58's `A` column validated at all thirteen cells of
`docs/s58_review.md` §1.

**Session 58 settled the direct-versus-extrapolated question.**  Its reduction —
Jacobi–Trudi along `λ`'s first row, then Frobenius reciprocity on the rectangle —
computes `sk(λ, 24⁴)` *at* `δ = 24`, with the rectangle entering only through the
box condition `β₁ ≤ 24`; **no stability hypothesis enters anywhere**.  So the two
routes are independent in the way that matters: one does not use stability at
all, the other uses it at exact equality, and the first validates the second.
Session 58 also reports `sk` constant from `δ = 23` and reproduces nineteen cells
of the boundary family, twelve of which are re-verified independently in
`docs/s58_review.md` §1.

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

## 3a. The `δ = 23` predecessor is the sharper and cheaper experiment

`a₂₃ = 273`, `a₂₄ = 274`, and `sk` is already constant at `48 825` from
`δ = 23`.  So the predecessor cell `(61, 17, 2⁷)` at `δ = 23` is
`Θ⁺ : C²⁷³ → C⁴⁸ ⁸²⁵` — one column narrower, identical target — and it decides
the goal cell:

    rank Θ⁺ at δ = 23  =  273     (full rank)
      ⟹  mult_det,24 ≥ mult_det,23 = 273        (ladder monotonicity)
      ⟹  i_det,24 = 274 − mult_det,24 ≤ 1
      ⟹  i_det,24 = 1                            (LMR gives i_det,24 ≥ 1)

The deduction uses only the two ambient values and monotonicity — no stability,
no `sk`.  Both `a` values are confirmed in §3.  Note that the Manivel reduction
is **not available at `δ = 23`** (`2δ = 46 < 48 = |ρ| + ρ₁`); its target
dimension comes from session 58's reduction alone.

## 3b. A free positive control at `n = 3`

The LMR weight at `n = 3` is `λ = (19,7,2⁵)`, `δ = 12`, `ℓ = 7`, with
`a = 6` (LMR's own value, reproduced here at inner degree 3) and `sk = 10`
(session 58, reproduced here by the direct partition sum).  The LMR module is
non-vacuous there, so `i_det ≥ 1` and

    rank Θ⁺_{n=3} at ((19,7,2⁵), 12)  must be  ≤ 5,  not 6.

This is a **`6 × 10` positive control** for the Foulkes engine and it is
essentially free.  It belongs in the s56 calibration set ahead of the `δ = 3`
blocks: those are `C → C²` maps of rank one and test the plumbing, whereas this
one tests whether the engine can see a rank drop at all.

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

## 6. Where the 274th vector comes from

The question "what event creates the final LMR copy at `δ = 24`?" has a precise
form.  By the ladder theorem, multiplication by `u = e_1^4` is **injective** from
the `λ_{δ−1}`-highest-weight space into the `λ_δ` one, so

    a_δ − a_{δ−1}  =  dim coker(M_u)  =  the number of genuinely new directions,

and every new direction is represented in the **`u`-free** part of the weight
space — the monomials with no `e_1^4` factor.  That part is computable: it has
dimension `N_S(λ_δ, δ) − N_S(λ_{δ−1}, δ−1)`, `N_S` the raw weight-space
dimension.  For the LMR ladder:

| `δ` | `λ_1` | `a` | new HWVs | `N_S` | `u`-free monomials |
|---|---|---|---|---|---|
| 12 | 17 | 2 | 11 | 51 446 325 457 | 51 446 325 457 |
| 14 | 25 | 93 | **54** | 106 429 467 326 | 25 508 045 258 |
| 18 | 41 | 241 | 22 | 151 601 110 197 | 4 853 208 876 |
| 21 | 53 | 269 | 5 | 156 124 593 451 | 576 668 236 |
| 22 | 57 | 272 | 3 | 156 346 649 229 | 222 055 778 |
| 23 | 61 | 273 | 1 | 156 419 279 221 | 72 629 992 |
| **24** | **65** | **274** | **1** | 156 438 903 314 | **19 624 093** |
| 25 | 69 | 274 | **0** | 156 443 174 266 | 4 270 952 |
| 26 | 73 | 274 | 0 | 156 443 907 591 | 733 325 |
| 28 | 81 | 274 | 0 | 156 444 014 936 | 9 824 |
| 30 | 89 | 274 | 0 | 156 444 015 695 | 36 |
| 31 | 93 | 274 | 0 | 156 444 015 696 | **1** |
| 32 | 97 | 274 | 0 | 156 444 015 696 | **0** |

The endpoint is a closed-form check on the whole computation: at `δ = t = 31`
every monomial has 31 factors and tail weight 31, so each factor has tail degree
exactly 1 and the unique `u`-free monomial is `(e_1^3 e_2)^{17} ∏_{j=3}^{9}
(e_1^3 e_j)^2`; at `δ = 32` there is none, which is the counting argument behind
the stability half of the ladder theorem.

**The reading.**  Saturation at `δ = 24` is **not** the counting phenomenon that
the `δ ≥ t` bound describes.  At `δ = 25` the `u`-free part of the weight space
still has 4.3 million monomials and produces **zero** new highest weight
vectors; the same at 26, 27, 28.  So the right question is not "why does a new
copy appear at 24" but

> why does a `u`-free space of ten million dimensions stop carrying **any** new
> highest weight vector after `δ = 24`, seven degrees before it empties?

The birth profile is also worth recording as data rather than a scalar: the new
directions per degree run `11, 37, 54, 52, 43, 31, 22, 14, 9, 5, 3, 1, 1` from
`δ = 12` to `24` — unimodal, peaking at `δ = 14`, with a long thin tail.  The
final `1` is the least remarkable entry in it.

## 7. The LMR degree is the closing degree — for the whole family, not just LMR

The observation that the LMR equation appears exactly where the ambient ladder
saturates is a property of the **weight family**, checked at 16 members.  For

    λ(k, m) = (3k + 2m, k, 2^m)   at   δ = k + m,   ρ = (k, 2^m),   t = k + 2m

— the family on which `2δ = |ρ| + ρ_1` holds with equality and of which LMR at
`n = 4` is `(k, m) = (17, 7)` — the first degree at which `a_δ = a_∞` is
**exactly `k + m` at every member tested**:

    (k,m) = (2,1) (3,1) (2,2) (3,2) (4,2) (4,3) (5,3) (5,4) (6,4)
            (7,4) (8,4) (7,5) (9,5) (6,5) (8,6) (10,6)      — 16 / 16

with `a_∞ = 1, 1, 1, 1, 3, 3, 4, 4, 9, 12, 21, 12, 28, 9, 22, 46`.  The `n = 3`
LMR cell behaves the same way in its own (inner-degree-3) ladder: `ρ = (7,2^5)`,
`a = 0, 2, 4, 5, 6, 6, …` from `δ = 8`, so `δ_close = 12`, which is the LMR
degree at `n = 3`.

So this is structural, not a coincidence of one cell, and it has a practical
consequence: **an LMR-type equation sits at a closing cell**, which is exactly
where the length-5 closure queue already points.  What it does *not* do is
select: every tail has a closing degree, and among the 2 107 live length-5 tails
42 % have the same final increment of 1 and LMR's "lateness"
`(δ_close − δ_min)/(t − δ_min) = 0.632` sits just above the mean of 0.530 — while
the `n = 3` LMR cell has lateness 0.444, *below* it.  Final-jump size and
lateness are both refuted as selectors; the family identity is what carries the
information.
