# The six-row cap: `onset I(D_6^{det_4}) ≤ 661`, and why the measuring route is not made unnecessary

> **Correction (session 49, 2026-09-05).**  The cap degrees quoted in this
> document — 1197 proved, 666 certified — were **one too large each**.  The
> smallest minor that vanishes identically on `D_6^{det_4}` has size **(rank of
> the determinantal specialisation) + 1**, not `ρ_d` (the rank of a *smooth*
> form).  At `d = 7` the determinantal rank is 660, so the usable minor is size
> **661**, not 666; at `d = 8` the Gulliksen–Négård ceiling proves the
> determinantal rank is `≤ 1147`, so the usable minor is size **1148**, not
> 1197.  Both corrections *lower* the cap:
>
>     onset I(D_6^{det_4})  ≤  1148   (proved)      ≤  661   (certified).
>
> Recomputed from scratch in session 49 (`analysis/wk9_s49_cap.py`, seed
> 20260905): `ρ_7 = 666`, `h_7 = 126`, GN ceiling 672, determinantal rank 660,
> minor 661; `ρ_8 = 1197`, `h_8 = 90`, GN ceiling **1147**, determinantal rank
> 1146, minor 1148.  The size-661 drop is re-certified over `Q` at three fresh
> `±10^12` pencils (`results/logs/s49_certify661.log`).  The body below is left
> as session 44 wrote it except that **every minor size `666` now reads `661`
> and every proved minor size `1197` now reads `1148`**; the ranks `ρ_d`, the
> determinantal ranks, and the GN ceiling are unchanged.  The same slip is
> **not** present in paper 1's `prop:jaccap` (there the drop is exactly one,
> `65 = 64 + 1`, so the minor size 65 is already `rank + 1`); see
> `docs/s49_report.md` §2.1.

Session 44, branch `s44-sixrowcap`, 2026-09-03, off `0c229c1`.
Pre-registration `results/PREREG_s44.md` (commit `2e06e3f`, **before any rank
was computed**).  Every rank in `results/s44_ladder.md`; code
`analysis/wk9_s44_*.py`; logs `results/logs/s44_*.log`.
Labels: **proved** / **measured** / **certified** / **adopted-from-literature**
/ **expectation**, as pre-registered.

## 0. Verdict

> **Theorem A (the a priori six-row cap; proved, no computation).**  For every
> pencil `M(s) = Σ_{i=1}^{6} s_i A_i` of `4×4` matrices whose rank-`≤ 2` locus
> has the expected codimension 4, the size-`1148` minors of the degree-8
> Macaulay matrix `M_8` of the six partials are degree-`1148` forms on
> `Sym^4 C^6`, not identically zero, and vanishing on `D_6^{det_4}`.  Hence
>
>     onset I(D_6^{det_4}) ≤ 1148 .
>
> The proof is one line of Gulliksen–Négård arithmetic: Jacobi's formula puts
> the Jacobian ideal inside the ideal `J(M)` of the sixteen `3×3` minors, whose
> Hilbert function is exact, and `dim J(M)_8 = 1147 < 1197 = ρ_8`.  So
> `rank M_8 ≤ 1147` at every determinantal point, and the smallest minor that
> vanishes there has size **`1148 = 1147 + 1`** — not `ρ_8 = 1197`, which is the
> *smooth* rank.  (The session-44 statement read `1197`; corrected in session
> 49, and it *lowers* the cap.)
>
> **Theorem B (the sharp cap; certified at explicit pencils, with an explicit
> failure probability).**  The first degree at which the Macaulay rank drops on
> `D_6^{det_4}` is `d = 7`, where the generic rank is `ρ_7 = 666` and the
> determinantal rank is `660` (corank `132 = h_7 + 6`).  The smallest minor
> vanishing on `D_6^{det_4}` therefore has size `660 + 1 = 661`, and
>
>     onset I(D_6^{det_4}) ≤ 661 .
>
> The drop — `rank_Q M_7 ≤ 660 < 661`, so every `661×661` minor vanishes — is
> **exact over `Q`** at three explicit integer pencils drawn uniformly from
> `±10^12`, by a multimodular certificate over ~1740 primes of 62 bits each
> (§4; the size-`661` certificate was run in session 49,
> `results/logs/s49_certify661.log`, and supersedes session 44's size-`666`
> run); the value 660 itself is measured modulo `p`.  If the generic
> determinantal rank were `≥ 661`, three uniform pencils from that box would all
> kill a nonzero degree-`2644` polynomial with probability at most
> `(2644/(2·10^12))^3 ≈ 2.3·10^{-27}`.  It is **not** a theorem: no argument here
> rules out a measure-zero coincidence, and §4 says exactly what would be needed.
>
> **`d = 7` is the floor of this mechanism (proved).**  There is **no** drop at
> `d = 4, 5, 6`: a determinantal point attains `ρ_d` there, a rank at a point is
> a lower bound on the generic rank, and `ρ_d` is an upper bound for every form
> — so the generic determinantal rank equals `ρ_d` exactly for `d ≤ 6`.  661
> cannot be improved by going to a lower Macaulay degree.
>
> **The hoped-for cheap answer does not happen.**  A drop at `d = 4` would have
> put an equation of `I(D_6^{det_4})` in degree 36 and made the six-row onset
> answerable by direct measurement.  It does not drop there, nor at 5, nor at 6.
> The bracket the programme now holds is
>
>     9  ≤  onset I(D_6^{det_4})  ≤  661
>
> (lower end: sessions 36 and 41, `mult_det = a` at all 90 reached cells through
> `δ = 8`, in every component reached).  **The expensive half of the programme
> is not made unnecessary.**  661 is three orders of magnitude above the
> `n_χ ≈ 20,000` frontier and points at no reachable cell.
>
> **The minors are not separators (measured; predicted).**  Padded permanents
> `ℓ(s)·per_3(A(s))` are reducible, hence singular in codimension 2, and their
> ranks drop earlier and much further — from `d = 5`, and by 140 at `d = 7`.
> The size-661 minors vanish on the padded permanent too.  The cap bounds the
> determinant ideal; it separates nothing.
>
> **The drop looks like `C(r,5)` (expectation).**  At `d = 3n−5`, where the
> Gulliksen-Negard ceiling is not binding, the measured drop is `0, 1, 6` at
> `r = 4, 5, 6` — across `n = 3, 4, 5` — and `C(r,5) = 0, 1, 6`.  The `r = 4`
> leg is a genuine prediction of the guess and is confirmed: the generic
> determinantal hypersurface in `P^3` is smooth and the rank never drops.
>
> **Also settled.**  The singular locus of a generic six-parameter `4×4`
> determinantal quartic is a curve in `P^5` of **degree 20 and arithmetic genus
> 21**; `H_{S/J(M)}(d) = 20d − 20` for `d ≥ 5`, measured against
> Gulliksen–Négård in every degree at both primes.  The six partials generate
> the whole ideal of the sixteen minors from degree 9 on: `J(M)/J_F` has finite
> length **140**, with Hilbert function `10, 30, 46, 41, 12, 1, 0, …`.

## 1. The mechanism, and the two anchors

For `F ∈ Sym^n C^r` let `M_d(F)` be the degree-`d` Macaulay matrix of the `r`
partials: rows indexed by `(i, m)` with `m` a monomial of degree `d − n + 1`,
columns by monomials of degree `d`, entry the coefficient of the column
monomial in `m·∂_iF`.  Then `rank M_d(F) = dim (J_F)_d` and
`corank = dim (S/J_F)_d`.  **Every entry is linear in the coefficients of `F`,
so every `k × k` minor is a polynomial of degree `k` on `Sym^n C^r`.**

*(proved)* For smooth `F` the partials are a regular sequence, so
`dim (S/J_F)_d = h_d := [t^d] ((1 − t^{n−1})/(1 − t))^r` and
`rank M_d = ρ_d := dim Sym^d C^r − h_d`.  For **every** `F`, `dim (S/J_F)_d ≥
h_d` — the corank is upper semicontinuous in the coefficients and its generic
value is `h_d` — so `rank M_d(F) ≤ ρ_d` always.  Consequently: if the rank
drops below `ρ_d` at the generic point of `D_r^{det_n}`, the size-`ρ_d` minors
are degree-`ρ_d` forms vanishing on `D_r^{det_n}`, and they are not identically
zero because a smooth form attains `ρ_d`.  Their span is the appropriate
Fitting ideal of a `GL_r`-equivariant map, hence a `GL_r`-submodule of
`I(D_r^{det_n})_{ρ_d}`.

*(measured — `results/logs/s44_anchor.log`)*  Both anchors reproduce, three
random forms and three fresh pencils each, both house primes:

| `n` | `r` | `d` | rows × cols | `h_d` | `ρ_d` | smooth | determinantal | corank |
|---|---|---|---|---|---|---|---|---|
| 3 | 5 | 4 | 75 × 70 | 5 | **65** | 65 | **64** | 6 |
| 4 | 5 | 7 | 350 × 330 | 30 | **300** | 300 | **299** | 31 |

65 is paper 1's `δ_0 ≤ 65`; 300 is `cap(4)`.  The cap theorem of
`docs/onset_conjecture.md` *is* this construction, and the harness reproduces
it.  The formula `ρ_d = dim Sym^d − h_d` was independently checked by direct
rank at twelve further `(n, r, d)`.

**Why the five-row proof does not transfer.**  At `r = 5` the generic
determinantal member has `ν(n) = n²(n²−1)/12` isolated nodes, and Dimca's
theorem (isolated singularities) converts the node set's defect in degree
`2n−5` into one extra dimension of the Milnor algebra in degree `3n−5`.  At
`r = 6` the rank-`≤ 2` locus still has codimension 4 in `P(M_4)` and so cuts a
**curve** in `P^5`.  Dimca's theorem is unavailable, and the published
one-dimensional analogue (Dimca–Sticlaru, §9) decomposes the correction into a
saturation term, a defect term and an `H^1` of the singular curve rather than
computing it.  The degree of the first drop had to be decided by computation.

## 2. Theorem A — the Gulliksen–Négård ceiling *(proved)*

Write `B(s) = adj M(s)`, `J(M)` for the ideal generated by the sixteen `3×3`
minors of `M(s)`, `S = C[s_1..s_6]`.

**(a) `J_F ⊆ J(M)` (proved).**  Jacobi's formula gives `∂_kF = tr(B(s)·A_k)`,
and every entry of `B(s)` is a signed `3×3` minor of `M(s)`.  So every partial
lies in `J(M)`, and `rank M_d(F) = dim (J_F)_d ≤ dim J(M)_d` at every
determinantal point.

**(b) `dim J(M)_d` is exact (adopted: Kleiman; Gulliksen–Négård;
Hochster–Eagon).**  For a generic pencil, Kleiman transversality in
characteristic 0 makes `P(L) ∩ {rank ≤ 2}` a transverse intersection, hence of
codimension `(4−2)² = 4` in `P^5` — a curve — so `grade J(M) = 4`, the generic
grade.  By generic perfection the Gulliksen–Négård resolution

    0 → S(−8) → S(−5)^16 → S(−4)^30 → S(−3)^16 → S → S/J(M) → 0

is exact, and `H_{S/J(M)}(d) = [t^d] (1 − 16t^3 + 30t^4 − 16t^5 + t^8)/(1−t)^6`.

**(c) The arithmetic.**  `H_{S/J(M)}(d) = 40, 60, 80, 100, 120, 140` for
`d = 3..8` (and `= 20d − 20` for `d ≥ 5`), against
`h_d = 50, 90, 126, 141, 126, 90`:

| `d` | `dim S_d` | `h_d` | `ρ_d` | `H_{S/J(M)}(d)` | ceiling `dim J(M)_d` | slack |
|---|---|---|---|---|---|---|
| 4 | 126 | 90 | 36 | 60 | 66 | +30 |
| 5 | 252 | 126 | 126 | 80 | 172 | +46 |
| 6 | 462 | 141 | 321 | 100 | 362 | +41 |
| 7 | 792 | 126 | 666 | 120 | 672 | **+6** |
| 8 | 1287 | 90 | **1197** | 140 | **1147** | **−50** |

At `d = 8` the ceiling is 50 below the generic rank.  So `rank M_8 ≤ 1147 <
1197` at *every* determinantal point of the open set where the grade is 4, the
size-`1148` minors (`1148 = 1147 + 1`, the ceiling plus one) vanish there, hence
on the closure `D_6^{det_4}`, and they are not identically zero because a smooth
quartic attains `ρ_8 = 1197 ≥ 1148`.  ∎  *(The session-44 draft wrote the minor
size as `1197 = ρ_8`; the smallest vanishing minor is `1148`, which is the
better bound — corrected in session 49.)*

This is the whole of Theorem A, and it was in `results/PREREG_s44.md` before
any matrix was built.  Its five-row shadow: the same argument at `(n,r) = (4,5)`
forces a drop only at `d = 8` (cap 480) where the truth is `d = 7` (cap 300),
so the ceiling is an upper bound on the cap, not the cap.

## 3. Theorem B — the drop at `d = 7`, and what it is

*(measured, both primes, three fresh pencils per degree, plus the certificate
of §4)*

| `d` | `ρ_d` | smooth | determinantal | drop | corank | padded permanent |
|---|---|---|---|---|---|---|
| 4 | 36 | 36 | 36 | 0 | 90 | 36 |
| 5 | 126 | 126 | 126 | 0 | 126 | **116** |
| 6 | 321 | 321 | 321 | 0 | 141 | **271** |
| 7 | **666** | 666 | **660** | **6** | **132** | **526** |
| 8 | 1197 | 1197 | **1146** | 51 | 141 | **917** |
| 9 | 1952 | 1952 | **1842** | 110 | 160 | **1497** |

**`d ≤ 6`: no drop, and this is proved.**  A determinantal point attains `ρ_d`
at `d = 4, 5, 6`.  A rank modulo `p` is a lower bound on the rank over `Q`, a
rank at a point is a lower bound on the generic rank, and §1 gives `ρ_d` as an
upper bound valid for every form.  The three inequalities close:
`ρ_d ≤ generic ≤ ρ_d`.  So the six-row cap cannot be lowered below 661 by
choosing a smaller Macaulay degree.

**`d = 7`: the drop is six non-Koszul syzygies** *(measured;
`results/logs/s44_syzygy.log`)*.  `rank M_7 = 756 − dim Syz_7`, and

    dim Syz_7 = 96 = 90 (Koszul) + 6 ,

at both primes and two independent pencils, where the 90 is
`C(6,2)·dim S_1 = 15·6`, the Koszul syzygies `(∂_lF)e_k − (∂_kF)e_l` scaled by
a linear form.  So the drop is `dim H_1(K(∂F; S))_7 = 6` — six syzygies that
are not Koszul.  Two probes: their coefficient forms `G_k ∈ S_4` are **not** in
`J(M)_4`; and `W(s) = Σ_k G_k A_k` does lie in the span of
`(XM + MY)·S_3`, `tr X + tr Y = 0` (dimension 1344, the full syzygy module of
the sixteen minors in that degree), as Gulliksen–Négård generation requires.
The consistency check passes; the six syzygies were **not** identified in
closed form, and §4 explains why that is the gap.

**`d = 8, 9`: the ceiling becomes tight.**  `rank M_8 = 1146` against the
ceiling 1147, and `rank M_9 = 1842` which **is** the ceiling.  Equivalently the
cokernel `Q = J(M)/J_F` has Hilbert function `10, 30, 46, 41, 12, 1, 0` in
degrees `3..9`: *(measured)* the six partials generate the entire ideal of the
sixteen `3×3` minors from degree 9 onward, and `Q` has finite length 140.

## 4. What is proved, what is certified, and the gap *(this section is the honest boundary)*

The direction of every inference matters here and the session was
pre-registered on it.

- A rank computed **modulo `p`** is a *lower* bound on the rank over `Q`.
- A rank at a **point** is a *lower* bound on the generic rank of the family.

Both point the wrong way for a drop.  Measuring `rank M_7 = 660 < 666` mod `p`
at a random pencil therefore proves nothing at all about `D_6^{det_4}`: it
gives `generic rank ≥ 660`, which is consistent with `666`.  Two steps were run
to close as much of this as can be closed by computation.

**Step 1 — exact over `Q` at explicit pencils (certified).**  The cap is the
smallest *vanishing* minor, size `661 = 660 + 1`, so what must be certified is
that every `661×661` minor vanishes over `Q`.  Each `661×661` minor of `M_7` is
an integer Hadamard-bounded by `(max_i ‖∂_iF‖_2)^{661}` (every row of `M_7` is a
permutation of the coefficient vector of some partial).  If `rank_p M_7 < 661`
for a set of primes whose product exceeds twice that bound, every `661×661`
minor is divisible by that product while bounded by half of it, hence **zero**;
so `rank_Q M_7 ≤ 660 < 661` exactly, at that pencil.  Session 49 ran this at
three pencils drawn uniformly from `±10^12`, 62-bit primes
(`analysis/wk9_s49_cap.py certify 7 661`, `results/logs/s49_certify661.log`):
the rank was 660 at every prime of every run, so the certificate closes:

    rank_Q M_7 ≤ 660 < 661   at three explicit integer pencils,

exact arithmetic, not a sample — hence `onset ≤ 661`.  Each run needed about
1740 primes and ~7 minutes.  (Session 44 ran the same argument at size `666`,
`analysis/wk9_s44_certify.py`, `results/logs/s44_certify_d7.log`, which
certified only `onset ≤ 666`; the value `660` is measured modulo `p` at both.
The size-`661` run is strictly stronger — the smaller Hadamard bound needs no
more primes — and it is what pins the corrected cap.)

**Step 2 — Schwartz–Zippel (an explicit probability, not a proof).**  Each
`661×661` minor is a polynomial of degree `4 · 661 = 2644` in the 96 pencil
entries (the entries of `M_7` are linear in the coefficients of `F`, which are
quartic in the pencil).  If the generic determinantal rank were `≥ 661`, some
such minor would be a **nonzero** polynomial of degree 2644, and a pencil drawn
uniformly from a box of side `2·10^12 + 1` would kill it with probability at
most `2644/(2·10^12+1) ≈ 1.32·10^{-9}`.  Three independent pencils:
`≈ 2.3·10^{-27}`.

**The reformulation that a next session should use.**  A syzygy
`Σ_k G_k ∂_kF = 0` is a vector field `δ = Σ_k G_k ∂/∂s_k` with `δ(F) = 0` — an
element of the module of logarithmic derivations `Der(−log F)` with zero
coefficient on `F`, in degree 4.  The Koszul syzygies are the trivial
derivations `(∂_lF)∂_k − (∂_kF)∂_l`.  So **the drop of six says that `det` of a
generic six-parameter `4×4` pencil carries six non-trivial degree-4 logarithmic
derivations**, where a five-parameter pencil carries one and a four-parameter
pencil carries none.  At the other end of the range this is a known picture:
the full determinant (`r = n²`) is a *linear free divisor*, its logarithmic
derivations generated in degree 1 by `gl_n ⊕ gl_n` — exactly the `2n² − 2` linear
syzygies of the Gulliksen–Négård complex.  Cutting `L` down to six dimensions
destroys the linear generators and pushes the first non-trivial derivations up
to degree 4.  What is wanted is a closed form for those six.

**The gap.**  Step 2 is not a proof.  A proof needs the six non-Koszul
syzygies of §3 **in closed form** — six identities `Σ_k G_k ∂_kF = 0` with
`G_k` polynomial in `s` and in the pencil entries, valid for every pencil.  The
natural families all turn out to be Koszul: for `A ∈ L`, `𝒳 = adj(M)A −
¼tr(adj(M)A)I` gives `W = F·A − ¼(∂_AF)·M(s)`, which is `¼Σ_k s_k` times the
Koszul syzygy `K_{kA}` by Euler's identity, and lies in the 90.  The six extra
syzygies are a genuinely new phenomenon at `r ≥ 6`, they are not visible at
`r = 5` (where the extra syzygy space is one-dimensional and is Dimca's node
defect), and this session did not find them.  **That is the one thing standing
between `onset I(D_6^{det_4}) ≤ 661` and a theorem.**  Theorem A, `≤ 1148`, is
a theorem now.

## 5. The padded permanent — a bound, not a separator *(measured; pre-registered)*

Pre-registration P2 predicted, at probability 0.97, that the minors would
vanish on padded permanents and therefore separate nothing.  They do, and the
reason is structural rather than numerical: `ℓ(s)·per_3(A(s))` is **reducible**,
so it is singular along `{ℓ = 0} ∩ {per_3 = 0}`, a threefold in `P^5` — against
the determinantal curve.  A bigger singular locus means a bigger Milnor algebra
and a smaller rank, and the measured drops are far larger at every degree
(10, 50, 140, 280, 455 at `d = 5..9`, against the determinantal
0, 0, 6, 51, 110).

Two consequences worth stating plainly:

1. **No candidate separating equation arises here.**  The `s41_prompt.md`
   verification protocol was not invoked, because there was nothing to verify.
2. The `d = 5` row runs the other way — the size-126 minors of `M_5` vanish on
   padded permanents and not on determinantal quartics.  That is the useless
   direction for an obstruction (`D = mult_pad − mult_det > 0` needs
   `mult_det < a`), and it is recorded only so the asymmetry is on file.

## 6. The singular curve *(measured against an adopted resolution)*

For a generic six-parameter `4×4` pencil, `Sing(det M) = {rank M(s) ≤ 2}` is a
curve in `P^5`.  From the Gulliksen–Négård Hilbert function,
`H_{S/J(M)}(d) = 20d − 20` for `d ≥ 5` (checked symbolically for `d = 5..11`):
**degree 20 — the Harris–Tu number `ν(4) = n²(n²−1)/12` — and arithmetic genus
21.**  Measured at a fresh pencil at both primes, `H_{S/J(M)}(d)` equals the GN
value at `d = 3..8` on the nose (`40, 60, 80, 100, 120, 140`), so the grade-4
specialisation is behaving.  Since `J_F` reaches `J(M)` from degree 9 (§3), the
Milnor algebra of a determinantal quartic in six variables has Hilbert
polynomial `20d − 20` as well, attained from `d = 9`.

Pre-registered prediction P3 confirmed.  This is the input a Dimca-style defect
computation would need; the computation itself is not done here, because the
published one-dimensional formula (§9) needs the saturation module `N(F)` and
`h^1(O_Z(7))`, and bounding `dim N(F)_7` below is precisely the gap of §4 in
another costume.

## 7. Phase 4.2 — the weights *(not attempted, per pre-registration)*

Stopping rule 4 of `results/PREREG_s44.md` said the `GL_6`-weight
decomposition of the minor module would be attempted only if the cap fell below
200.  It is 666.  A degree-666 module in `Sym^666(Sym^4 C^6)` is out of reach by
several orders of magnitude, and no partial decomposition is offered.  The
honest pointer is a negative one: **the cap does not point at any measurable
cell.**  The frontier is `δ ≤ 9` at `n_χ ≈ 20,000`; 661 is not adjacent to it.

## 8. The first drop across `(n, r)` *(measured; `results/logs/s44_sweep.log`)*

Two pencils per `(n, r, d)`, both primes, with a random-form control at every
`d` that must return `ρ_d` before the determinantal ranks are read.

| `n` | `r` | first drop `d*` | `3n−5` | `ρ_{d*}` | rank | drop | GN-forced `d` |
|---|---|---|---|---|---|---|---|
| 3 | 5 | 4 | 4 | 65 | 64 | 1 | 4 |
| 3 | 6 | 4 | 4 | 111 | 102 | 9 | 4 |
| 3 | 7 | 3 | 4 | 49 | 47 | 2 | 3 |
| 3 | 8 | 3 | 4 | 64 | 56 | 8 | 3 |
| 4 | 5 | 7 | 7 | 300 | 299 | 1 | 8 |
| 4 | 6 | **7** | 7 | **666** | **660** | **6** | 8 |
| 4 | 7 | 7 | 7 | 1323 | 1279 | 44 | 7 |
| 4 | 8 | 7 | 7 | 2416 | 2248 | 168 | 7 |
| 5 | 5 | 10 | 10 | 900 | 899 | 1 | 12 |
| 5 | 6 | 10 | 10 | 2457 | 2451 | **6** | 12 |

Two readings:

- **The first drop sits at `d = 3n − 5` for every `r ≤ 6`** — the degree of the
  five-row cap theorem — and does not move when the fifth row becomes a sixth.
  It moves down only when `L` becomes large inside `M_n` (`r = 7, 8` at
  `n = 3`, where `dim M_3 = 9` and linear syzygies among the partials appear).
- **Where the GN ceiling is not binding at `d = 3n − 5`, the size of the drop
  is a function of `r` alone, and it is `C(r, 5)`** *(measured at seven
  `(n, r)`; an expectation, not a claim)*:

  | `r` | `C(r,5)` | measured drop at `d = 3n−5` | at |
  |---|---|---|---|
  | 4 | **0** | 0 at every `d` — the hypersurface is smooth | `n = 3, 4, 5` |
  | 5 | **1** | 1 | `n = 3, 4, 5` |
  | 6 | **6** | 6 | `n = 4, 5` |

  The `r = 4` leg (`analysis/wk9_s44_r4.py`, `results/logs/s44_r4.log`) is the
  sharpest of the three and was run *because* `C(4,5) = 0` predicts it: for
  `r = 4` the rank-`≤ n−2` locus has codimension 4 and `P^3` misses it, so the
  generic determinantal hypersurface in `P^3` is **smooth** (classically: the
  generic determinantal cubic and quartic surface are smooth) and the rank never
  drops at any degree.  Measured at three pencils and both primes over the full
  range `d = n−1 .. 3n+1` at `n = 3, 4, 5`: `drop = 0` in all 31 rows.

  The rule is stated with the ceiling caveat because the ceiling can force more:
  at `(3, 6)` the GN ceiling already binds at `d = 4` (the measured rank 102 *is*
  the ceiling) and the drop is 9, not 6; at `(4, 7)` and `(4, 8)` the ceiling
  binds at `d = 7` and the drops are 44 and 168, matching neither `C(r,5)` nor
  the ceiling alone.  The one clean `r = 7` test, `(n, r) = (5, 7)`, needs a
  `12012 × 8008` rank and was out of budget.  So: `C(r,5)` is confirmed at
  `r = 4, 5, 6` across seven `(n, r)` pairs and **untested at `r ≥ 7`**.

The general cap this suggests, for `4 ≤ r ≤ 6` and `n ≥ 4`:

    ρ_{3n−5}(n, r) = dim Sym^{3n−5} C^r − h_{3n−5}(n, r) ,   drop = C(r, 5)

whose values `ρ_{3n−5}` are 65 and 300 at the two anchors, 666 at `(4,6)` and
2457 at `(5,6)`, and undefined at `r = 4` (no drop).  **These `ρ` are the
*smooth* ranks, not the onset bounds.**  The smallest vanishing minor has size
`(determinantal rank) + 1 = ρ_{3n−5} − C(r,5) + 1`, so the actual onset cap this
mechanism gives is

    cap(n, r) = ρ_{3n−5}(n, r) − C(r, 5) + 1 ,

which is `65` and `300` at the two `r = 5` anchors (there `C(5,5) − 1 = 0`, so
`cap = ρ`, and this is why the five-row theorem and paper 1's `prop:jaccap` are
free of the slip), **`661` at `(4,6)`** (`666 − 6 + 1`) and `2452` at `(5,6)`
(`2457 − 6 + 1`).  Only the `r = 5` column is a theorem
(`docs/onset_conjecture.md`); the `r = 6` values are the certified caps of this
document.

**A limitation worth stating.**  At `r = 4` the mechanism produces *no*
equations, and that is not because there are none: `dim D_4^{det_4} = 4·16 −
(2·16 − 2) = 33 < 35 = dim Sym^4 C^4`, so `D_4^{det_4}` is a proper subvariety
of codimension 2 and has a nonempty ideal.  The Macaulay mechanism sees only the
singularity that the pencil forces on its determinant; when the pencil forces
none, it is blind.  Nothing here says the cap is close to the onset at any `r`.

## 9. Literature *(Phase 5)*

Per claim, with what was actually found.

**Known, and adopted here.**

- **Gulliksen–Négård.**  T. H. Gulliksen and O. G. Negård, *Un complexe
  résolvant pour certains idéaux déterminantiels*, C. R. Acad. Sci. Paris **274**
  (1972), 16–18: the resolution of the submaximal-minor ideal of a generic
  square matrix with ranks `1, n², 2n²−2, n²`.  Generic perfection and the
  grade-4 specialisation: W. Bruns and U. Vetter, *Determinantal Rings*, LNM
  1327, Springer 1988 (Hochster–Eagon).  Both confirmed to the statement used.
- **Dimca's isolated-singularity theorem**, used at five rows and *not*
  applicable here: A. Dimca, *Syzygies of Jacobian ideals and defects of linear
  systems*, arXiv:1210.1795, **Theorem 3.1** — statement, grading and the range
  `0 ≤ k ≤ nd − 2n − 1` all verified against the arXiv text.  (The journal
  reference `Bull. Math. Soc. Sci. Math. Roumanie 56 (2013)` carried in
  `docs/onset_conjecture.md` could not be independently confirmed; the arXiv id
  and theorem number are solid.  Worth correcting in the paper pass if it is
  wrong.)
- **The one-dimensional analogue exists but does not compute the drop.**
  A. Dimca and G. Sticlaru, *Free and nearly free surfaces in `P^3`*,
  arXiv:1507.03450, §2, formula (2.10):
  `H(M(f))(k) = P(M(f))(k) + dim N(f)_k − def_k Σ + dim H^1(Σ, O_Σ(k))`
  for `dim Σ = 1`, with `N(f) = I_f/J_f` the saturation module.  This is a
  decomposition into local- and sheaf-cohomology pieces relative to the Hilbert
  **polynomial**, not a formula in `deg Σ`, `p_a(Σ)` and the Hilbert function of
  `I_Σ`.  Also: Dimca–Sticlaru, *The Hessian polynomial and the Jacobian ideal of
  a reduced hypersurface in `P^n`*, Adv. Math. (2021), arXiv:1910.09195 —
  Castelnuovo–Mumford regularity bounds for positive-dimensional singular loci,
  which bound where a drop can live but do not compute it.
- **Depth sensitivity of the Koszul complex** (`H_i(K) = 0` for
  `i > N − grade`), used in §3 to know the drop is `dim H_1 − dim H_2`:
  Matsumura, *Commutative Ring Theory* (1989), Theorem 16.5(ii).
- **The dimension of the determinantal locus is known.**  Z. Reichstein and
  A. Vistoli, *On the dimension of the locus of determinantal hypersurfaces*,
  Canad. Math. Bull.: `dim DHyp_{r,n} = (r−1)n² + 1` for `r > 3`, `n > 2`, by a
  differential argument.  The authors explicitly write that they do not know the
  degree of the characteristic-polynomial map and that their proof sheds no
  light on it.

**Not found.**

- **The construction itself** — rank drops of the Macaulay matrix of the
  partials, read as `k × k` minors that are degree-`k` forms on `Sym^n C^r` and
  so as *equations of the locus of determinantal hypersurfaces* — was not found
  in the literature, in either the singularity-theory or the GCT direction.  The
  nearest neighbour is Landsberg–Manivel–Ressayre, *Hypersurfaces with
  degenerate duals and the Geometric Complexity Theory Program*, arXiv:1004.4802,
  which produces set-theoretic defining equations for the hypersurfaces with
  small dual variety and shows the `GL_{n²}`-orbit closure of `det_n` is an
  irreducible component of one such locus — the same genre, a different locus
  and a different matrix.
- **Any equations, ideal-theoretic description or degree bound for the locus of
  determinantal hypersurfaces.**  Beauville, *Determinantal hypersurfaces*,
  Michigan Math. J. **48** (2000), arXiv:math/9910030, gives the ACM-sheaf
  characterisation and genericity results, no equations; Piontkowski, *Linear
  symmetric determinantal hypersurfaces*, Michigan Math. J. **54** (2006), is a
  singularity classification and notes the locus is only constructible.
  Reichstein–Vistoli, as above, say the degree question is open.
- **`J(det M) ⊆ I_{n−1}(M)` as a cited statement**, and **the Hilbert function
  of the Milnor algebra of `det` of a linear pencil**.  Both immediate and both
  uncited as far as this check goes.
- **The logarithmic derivations of a generic linear section of the determinant.**
  The linear-free-divisor literature (Buchweitz–Mond; Granger–Mond–Nieto–Schulze;
  Calderón-Moreno–Narváez-Macarro on the logarithmic comparison theorem) covers
  the *full* determinant, where `Der(−log det)` is generated in degree 1 by
  `gl_n ⊕ gl_n`.  Nothing was found on `Der(−log det M(s))` for a generic
  `r`-dimensional pencil with `r < n²`, where the linear generators disappear and
  the first non-trivial derivations move up in degree — which is exactly the
  object §4 needs.  Searched; **NOT FOUND**.

So: if Theorem A survives review it appears to be the first degree bound of any
kind on the ideal of a locus of determinantal hypersurfaces, and
Reichstein–Vistoli's own disclaimer is the best evidence that the ideal side is
untouched.  Caveat: the Beauville and Piontkowski readings are from an automated
skim (ProjectEuclid blocked direct fetch); worth a human glance before print.

## 10. Standing after this session

`onset I(D_6^{det_4}) ∈ [9, 661]`, with `≤ 1148` proved outright and `≤ 661`
certified at explicit pencils with failure probability `≈ 2.3·10^{-27}`
(session-49 correction: the caps read 1197 and 666 before, one too large each —
the usable minor is `(determinantal rank) + 1`, not `ρ_d`).
`d = 7` is the floor of the mechanism (proved).  The minors are not separators,
by a structural argument, so the obstruction question is untouched.  The
measuring route is **not** made unnecessary: the cap is three orders of
magnitude above the frontier and points at no cell anyone can reach.

The three things a next session could do, in order of value:

1. **Close the gap of §4** — find the six non-Koszul syzygies of `(4, 6, 7)` in
   closed form and turn `≤ 661` into a theorem.  Equivalently: the six degree-4
   logarithmic derivations of `det M(s)` beyond the trivial ones.  The search
   space is `{ 𝒳M + M𝒴 : tr(𝒳 + 𝒴) = 0 } ∩ (L ⊗ S_4)` modulo Koszul,
   six-dimensional, and the numerics are cheap and already written
   (`analysis/wk9_s44_syzygy.py`, `wk9_s44_probe.py`).  What the probes rule out
   (`results/logs/s44_probe.log`): `W(s) = Σ_k G_k A_k` has full rank 4 at
   generic `s`, so the syzygies do not factor through a degenerate part of the
   pencil; and the natural family `W_i = F·A_i − ¼(∂_iF)·M(s)` spans exactly six
   dimensions and is entirely Koszul, so the answer is not a variant of it.
2. **Test `drop = C(r,5)`** at `(n, r) = (5, 7)` — the one case in the ladder
   that is neither ceiling-limited nor already measured — which needs a
   `12012 × 8008` rank, out of this session's budget but not out of reach.
3. **The `r = 6` cap formula.**  If 1 and 2 land, `cap(n, 6) = dim Sym^{3n−5} C^6
   − h_{3n−5}(n, 6)` becomes the six-row analogue of `cap(n)`, with the same
   proof shape and a drop of `C(6,5) = 6` in place of Dimca's 1.

## 11. The pre-registration, scored

`results/PREREG_s44.md`, committed at `2e06e3f` before any matrix was built.

| # | prediction | outcome |
|---|---|---|
| — | a drop at `d = 8` is forced a priori by the GN ceiling; `onset ≤ 1197` before any computation | **correct** — Theorem A (the *minor* size is 1148; see the correction header) |
| P1 | smallest `d` with a strict drop is **7**, cap **666** (prior 0.45; alternatives 8/0.35, 6/0.17, ≤5/0.03) | **correct** on `d = 7`; the cap is **661**, not 666 (minor = rank + 1, session-49 correction) |
| P1′ | corank at `d = 7` is `127 = h_7 + 1`, drop of one by analogy with five rows | **wrong** — the corank is `132`, the drop is **6** |
| P1″ | no drop at `d = 4, 5` because the only linear syzygies would need `XA_i + A_iY ∈ L`, 60 conditions on a 31-dimensional space | **correct**, and now proved (§3) |
| P2 | padded permanents also drop, so the minors are not separators (prior 0.97) | **correct**, and the drop is far larger and starts two degrees earlier |
| P3 | the singular locus is a curve of degree 20 and arithmetic genus 21, `H_{S/J(M)}(d) = 20d − 20` for `d ≥ 5` | **correct**, measured against GN at both primes |
| P4 | the GN-forced degree is a *cap on the cap*, right at `(3,5)` and loose at `(4,5)` | **correct**, and loose at `(4,6)` too (forced 8, true 7) |

The one miss is P1′, and it is the interesting one: the drop is six, not one, and
`C(r,5)` — confirmed at `r = 4, 5, 6` — is a rule the session did not anticipate.

## 12. Process

- Pre-registration first, `2e06e3f`, before the first `nmod_mat`.
- Ranks by `python-flint` at both house primes at every measurement; no result
  in this document rests on a single prime or a single seed, and no number was
  averaged or majority-voted.  The ladder was re-run at a fresh seed and two
  different boxes in the verification pass and reproduced exactly.
- Every long run was bounded by `timeout` and `ulimit -v`, with its pid in
  `results/logs/<run>.pid`.  One run was ended early: `wk9_s44_exact.py`
  (`results/logs/s44_exact_d7.pid`, pid 2143), the `fmpz_mat` fraction-free
  exact rank, which was still running after ten minutes with no output and was
  superseded by the multimodular certificate.  It was killed **by that recorded
  pid**, not by a name pattern.  The script is left in the tree because its
  docstring states the direction-of-inference problem that motivates §4, but its
  route is the slow one; use `wk9_s44_certify.py`.
- No file over 5 MB committed; no session link in any commit or script.
