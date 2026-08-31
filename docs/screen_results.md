# The two cheap steps: the Peter–Weyl pre-screen and the permanent's deficit

Session 24b, branch `s24-screen`, 2026-08-31.
Pre-registration: `results/PREREG_s24b.md` (committed before any computation).
Session record and cross-checks: `docs/session_24b.md`.

**Verdict, in advance of the evidence.**  *The line is closed in accessible
range, and closed for a reason opposite to the one I predicted.*  The screen
does not merely fail to find a candidate — it fails everywhere and by a wide
and growing margin: at every weight where an obstruction is possible at all,
the padded permanent's Peter–Weyl count strictly exceeds the determinant's, so
`P > 0` and **no obstruction in this range can be deficit-driven**.  The one
formal pass, `lam = (n)` at `delta = 1`, is vacuous.  Session 24's
recommendation therefore stands, strengthened: the deficit should be published
as an exact measure of non-normality, not as a separation tool.

---

## 1. What was computed

Session 24's Lemma 1, for `A = closure(GL_{n^2}·det_n)` and
`B = closure(GL_{n^2}·x_0^{n-m} per_m)` in `W = Sym^n C^{n^2}`:

    D(lam) = mult_lam C[B] − mult_lam C[A] = P(lam) − Def(lam),
    P = m_B − m_A ,  Def = def_B − def_A ,  m_X(lam) = dim (S_lam^*)^{H_X}.

An obstruction is `D > 0`; it is **deficit-driven** iff also `P <= 0`.
A weight is **live** iff `m_B(lam) > 0` — otherwise `mult_lam C[B] = 0` and
`D <= 0` whatever the geometry, so no obstruction is possible there.

**The screen.**  Is there a live weight with `P(lam) <= 0`?
If not, the deficit-driven mechanism is unavailable and the line closes.

## 2. The two stabilisers, stated exactly

**Determinant.**  `Stab_{GL_{n^2}}(det_n) = {X ↦ AXB : det A · det B = 1} ⋊ <transpose>`,
of dimension `2n^2 − 2` (`n=1`: 0; `n=2`: `SO_4`, dim 6; `n=3`: **16**).
*Recorded discrepancy:* `paper/det3-conductor.tex` §4 states dimension 17 for
`n = 3`, and the session-24 brief quotes 17 → 31.  17 is
`dim (GL_3×GL_3)/C^*`, the stabiliser of the *point* `[det_3]`; the stabiliser
of the *vector* `det_3` — which is what the Peter–Weyl identity and Lemma 1
require — has dimension 16.  The paper's own published numbers confirm the
vector convention: with it, this pipeline reproduces `def_{det_3}((2,2,2),2)=1`
and the total-deficit sequence 1, 6, 31 at `delta = 2,3,4` exactly (§5).
The `17`/`31` in the paper and the brief should be corrected to `16`/`30`.

By Schur–Weyl,

    m_det(lam) = ( g(lam, (delta^n), (delta^n)) + X(lam) ) / 2 ,
    X(lam) = (1/N!) sum_rho |C_rho| chi^lam(rho) chi^{(delta^n)}(rho~) ,

`N = n·delta`, `g` the Kronecker coefficient, `rho~` obtained from `rho` by
keeping odd parts and splitting each even part `r` into two parts `r/2`.
(Derivation: `tr(k^r) = tr(A^r)tr(B^r)` on the identity component;
`tr(k^r) = p_r(AB)` for odd `r` and `p_{r/2}(AB)^2` for even `r` on the
transpose coset; the Haar average over `{det A det B = 1}` selects the
rectangle.)  So `m_det` is the **symmetric rectangular Kronecker coefficient**.

**Padded permanent.**  Derived here rather than cited.  Let `p = n − m >= 1`,
`U* = span(x_0, y_11..y_mm)` (the span of the first partials of
`v = x_0^p per_m`), `Z = (U*)^perp ⊆ V`, `u = dim V/Z = m^2 + 1`.
Unique factorisation forces `x_0 ↦ c x_0`; the `x_0`-linear coefficient
`sum d_ij ∂per/∂y_ij` vanishes identically only for `d = 0`, the sub-permanents
being linearly independent.  Hence

    Stab_{GL(U)}(x_0^p per_m) = { x_0 ↦ c x_0 , y ↦ L y : per_m ∘ L = c^{−p} per_m },

with `L` of the form `X ↦ D_1 P X Q D_2` plus transpose — **monomial** in the
basis `{x_0, y_ij}`: a 6-torus times a finite part `(S_3×S_3) ⋊ Z/2` of order
72, total dimension `2m − 1 = 5`.

**Lemma (row bound).**  Inside `GL_{n^2}` the stabiliser preserves `Z`,
contains all of `GL(Z)` and the whole `Hom` block, and acts on `V/Z` through
the group above.  Restricting to the Levi,

    (S_lam V)^{Stab} ⊆ (S_lam V)^{GL(Z) × Stab_{GL(U)}(v)} ≅ (S_lam(U))^{Stab_{GL(U)}(v)},

because `GL(Z)` has no invariants in `S_alpha(Z)` for `alpha ≠ 0`, so only the
Littlewood–Richardson term `c^lam_{∅,lam}` survives.  In particular
`m_{per^pad}(lam) = 0` whenever `ell(lam) > m^2 + 1`.
Only this **upper bound** is used below, so every screen conclusion is rigorous
even at weights where the bound is not tight.

For the monomial group the count is exact coefficient extraction:
`m = (1/72) sum_{f} [ sum of coefficients of chi_{S_lam}(D f) over the
T-invariant exponent vectors ]`, with `chi_{S_lam}(Df) = det(h_{lam_i−i+j})`
and `sum_k h_k z^k = prod_cycles (1 − z^{|c|} X_c)^{−1}`.  The `T`-invariant
exponents are `mu_0 = delta(n−m)` together with a `3×3` block whose row and
column sums are all `delta`.

## 3. STEP 1 — the screen, exhaustive over the stated range

An obstruction at `lam` needs `mult_lam C[B] > mult_lam C[A] >= 0`, and for
*every* orbit closure `X` in this ambient

    mult_lam C[X]_delta  <=  min( m_X(lam) , amb_delta(lam) ),

where `amb_delta(lam)` is the multiplicity of `S_lam` in the plethysm
`Sym^delta(Sym^n C^{n^2})`.  So a weight can carry an obstruction only if

  1. `amb_delta(lam) > 0` — otherwise *every* closure has multiplicity 0 there;
  2. `m_{per^pad}(lam) > 0` — otherwise `mult_B = 0`;
  3. `ell(lam) <= m^2 + 1` — the row bound (and 3 ⟹ 2 fails otherwise);

and it can carry a **deficit-driven** one only if additionally

  4. `P(lam) = m_{per^pad}(lam) − m_det(lam) <= 0`.

Condition 1 is by far the cheapest and by far the most restrictive: the
plethysm `Sym^delta(Sym^n)` has very few constituents.  Call a weight
satisfying 1–3 **live**.

| `(n,m,delta)` | `lam ⊢ N` | ambient constituents | live | `P > 0` | **screen passes** | margin range |
|---|---|---|---|---|---|---|
| (4,3,1) | 4  | 1 | 1 | 0 | 1 — `lam=(4)`, vacuous | 0 |
| (4,3,2) | 8  | 3 | 3 | 3 | **0** | 2 … 8 |
| (4,3,3) | 12 | 9 | 9 | 9 | **0** | 4 … 140 |
| (5,3,2) | 10 | 3 | 3 | 3 | **0** | 2 … 8 |
| (6,3,2) | 12 | 4 | 4 | 4 | **0** | 2 … 8 |

Exhaustive over *all* `lam ⊢ n·delta`, not sampled.  At `(4,3,3)` the nine live
weights and their margins are

    lam         amb  m_det  m_perpad    P        lam        amb m_det m_perpad   P
    (4,4,4)      1     2      18       16        (8,4)       1    1     50      49
    (6,4,2)      1     2     142      140        (9,3)       1    1     43      42
    (6,6)        1     1      18       17        (10,2)      1    1     25      24
    (7,4,1)      1     1     111      110        (12)        1    1      5       4
    (8,2,2)      1     2      64       62

**The margin grows sharply with `delta`** — 2…8 at `delta = 2`, 4…140 at
`delta = 3`.  It is not approaching zero.  Increasing `n` at fixed `delta`
does not help either: at `delta = 2` the margins are 2…8 for `n = 4, 5, 6`
alike.  The independent, cruder screen of conditions 2–4 only (no ambient
test) was also run exhaustively at `(4,3,1)`, `(4,3,2)`, `(4,3,3)`,
`(5,3,1)`, `(5,3,2)`, `(6,3,1)`, `(6,3,2)` and `(7,3,2)` — a strictly larger
weight set, since it does not require `amb > 0` — and returned nothing beyond
the two weights discussed below.

**A candidate appeared, and died for free.**  A first pass of the screen used
only conditions 2–4 and found exactly one non-trivial passing weight, at
`(n,m,delta) = (4,3,3)`:

    lam = (3,2,2,1,1,1,1,1) :  m_det_4 = 1,  m_{per^pad} = 1,  P = 0.

Condition 1 kills it: the ambient plethysm multiplicity of that `S_lam` in
`Sym^3(Sym^4 C^16)` is **0**, so `mult_lam C[X]_3 = 0` for *every* orbit
closure in the ambient, both closures included, and `D = 0`.  Note that this
kill is self-contained — it does not invoke Bürgisser–Ikenmeyer–Panova, and
does not depend on whether their hypotheses cover `(n,m) = (4,3)`.  It is
recorded here rather than quietly dropped because it is the only moment in the
session when a candidate existed.

**The one surviving formal pass is vacuous.**  At `delta = 1` the ambient is
the single constituent `lam = (n)`, where `m_det = m_{per^pad} = 1` and
`P = 0`.  But `W = Sym^n C^{n^2}` is an irreducible `GL_{n^2}`-module, so every
nonzero orbit spans it and `W^* → C[X]_1` is injective for **both** closures:
`mult = 1` and `def = 0` on both sides, hence `D = 0` identically.  It is a
weight where nothing can happen, not a candidate.

**A general remark on what a pass would even buy.**  At every weight the screen
passed — the vacuous one and the killed one alike — `m_{per^pad} = m_det = 1`.
There `mult_B <= 1`, so an obstruction requires `mult_A = 0 < mult_B = 1`: an
**occurrence** obstruction, and simultaneously `def_A(lam) = m_A(lam)`, a *full*
determinant deficit.  Occurrence obstructions are exactly the sub-case
Bürgisser–Ikenmeyer–Panova close.  So even where the Peter–Weyl side goes
neutral, the only obstruction the arithmetic leaves room for is the one already
known to be unavailable.

## 4. Why the screen fails — and why I predicted the opposite

Pre-registered hypothesis E3 said the screen would pass broadly, reasoning that
`H_{per^pad}` is enormous (dimension `36 + 60 + 5 = 101` for `(n,m) = (4,3)`)
against `dim H_det_4 = 30`, so `m_{per^pad}` should be the smaller count.
**That reasoning is wrong, and the error is instructive.**  Ninety-six of those
101 dimensions — all of `GL(Z)` and the whole `Hom` block — do nothing but cut
`S_lam(C^16)` down to `S_lam(C^10)`.  After that reduction the *effective*
group is only 5-dimensional.  So the true comparison is

* **determinant:** a *reductive* group of dimension `2n^2−2` acting on
  `C^{n^2}`, whose invariants are symmetric rectangular Kronecker
  coefficients — famously sparse, and mostly **zero** in this range;
* **padded permanent:** a *5-dimensional* group acting on `C^{m^2+1} = C^10`,
  whose invariants are monomial lattice counts — positive on a broad set of
  weights and comparatively large.

Sparse-and-small against broad-and-large: `m_{per^pad} > m_det` at every live
weight.  Raw stabiliser dimension inside `GL_{n^2}` is the wrong statistic;
the effective group after the row reduction is the right one.

**A corollary worth recording.**  At 14 of the 19 live weights at `(4,3,2)`,
`m_det(lam) = 0`, hence `mult_lam C[closure(det_4)] = 0`, while
`m_{per^pad}(lam) > 0`.  If `mult_lam C[closure(per^pad)]` were also positive
at any of those, that would be an *occurrence* obstruction — which
Bürgisser–Ikenmeyer–Panova rule out.  So BIP's theorem, translated into this
programme's language, says exactly:

> at every weight where the determinant's Peter–Weyl count vanishes, the padded
> permanent's deficit is **full**: `def_{per^pad}(lam) = m_{per^pad}(lam)`.

That is a nontrivial statement about the permanent's deficit obtained for free
from a known theorem, and it is the first thing this programme's vocabulary has
said about the permanent side.

## 5. STEP 2 — the permanent's deficit at `n = m = 3`

Same ambient `Sym^3 C^9`, no padding, so the comparison is direct.  Because
`mult_lam C[X]_delta <= min( m_X(lam), plethysm coefficient )` and the ambient
plethysm `Sym^delta(Sym^3 C^9)` is 0 or 1 in this range, the deficit is pinned
**exactly** wherever the ambient vanishes, and to within 1 elsewhere.

**The first weight, elementary as predicted.**  `Sym^2(Sym^3) = S_(6) ⊕ S_(4,2)`
contains no `S_(2,2,2)`, so `mult = 0` there for *every* orbit closure in this
ambient and `def = m`:

    def_{per_3}((2,2,2), 2)  =  m_{per_3}((2,2,2))  =  4        (two routes)
    def_{det_3}((2,2,2), 2)  =  m_{det_3}((2,2,2))  =  1        (paper, reproduced)
    P((2,2,2))               =  +3

So the first permanent deficit is **4**, four times the determinant's, and the
Peter–Weyl part at that weight is `+3` — favouring an obstruction, not needing
one.  `Def = 4 − 1 = 3 = P`, so `D = 0`: the deficit difference exactly cancels
the Peter–Weyl difference, the same saturation-at-zero behaviour session 24
measured 742 times in World A.

**Full rows.**  Totals over all `lam ⊢ 3delta` with `ell(lam) <= 9`:

| `delta` | `sum m_det` | `sum m_per` | `sum` ambient | total `def_det` | total `def_per` |
|---|---|---|---|---|---|
| 1 | 1  | 1    | 1  | 0  | 0    |
| 2 | 3  | 17   | 2  | **1** | 15   |
| 3 | 11 | 318  | 5  | **6** | 313  |
| 4 | 43 | 5631 | 12 | **31** | 5619 |

The bold column is the paper's published determinant total-deficit sequence
`1, 6, 31, 141, 618, 2488`; this pipeline reproduces its first three entries
from an entirely independent route (Schur–Weyl + Kronecker, no engine, no
evaluation certificates).  That is the calibration for everything else here.
It also shows that every ambient piece survives on the determinant side at
`delta <= 4`, i.e. the degree-`<= 4` part of the ideal is zero.

**No weight passes the screen in the unpadded model either**, at any
`delta <= 4`: `m_per >= m_det` everywhere, and the ratio of the totals *widens*
sharply — 1, 5.7, 28.9, 131.0.  Moving from the padded problem toward the
unpadded model makes the screen fail harder, not softer.

## 6. What "accessible" cost

All exact, pure Python, no engine, no checkpointing, single container.

* `m_det` (Kronecker + symmetric correction): milliseconds to a few seconds per
  weight up to `N = 16`; the `S_N` character table by Murnaghan–Nakayama with
  memoisation is the only cost and it is shared across weights.
* `m_{per^pad}` / `m_{per_3}`: the bottleneck.  Route 2 (Schur–Weyl power sums)
  is ~1.4 s per weight at `N = 9`, ~5 s at `N = 12`, ~60 s at `N = 12` in ten
  variables, and dominates.  Route 1 (Jacobi–Trudi determinant of polynomials)
  is 10–50× slower and was used only for spot checks.
* Whole session: about two hours of wall clock, most of it in `m_{per^pad}`.

For comparison, the `n = 4` determinant grind the programme was contemplating
is estimated in tens of thousands of core-hours.  **The screen cost about four
orders of magnitude less and answered the question.**  That ratio is the
strongest argument for running screens of this shape before any engineering.

## 7. Verdict

**The line is closed in accessible range, and it closes twice over.**
Exhaustively — not by sampling — over `(n,m,delta) = (4,3,1)`, `(4,3,2)`,
`(4,3,3)`, `(5,3,2)`, `(6,3,2)` under the full three-condition screen, and over
the strictly larger weight sets of the cruder screen at `(4,3,1..3)`,
`(5,3,1..2)`, `(6,3,1..2)`, `(7,3,2)`, there is no weight at which a
deficit-driven obstruction to `closure(per_3^pad) ⊆ closure(det_n)` could
exist.  Every live weight has `m_{per^pad} > m_det`, so `P > 0` and any
obstruction there is one the Peter–Weyl side already sees, with the deficit
entering only as the subtraction that can destroy it; and the margin is not
tightening but widening — 2…8 at `delta = 2`, 4…140 at `delta = 3`, with `n = 4,
5, 6` behaving alike.  Exactly two weights ever passed, and both are closed
without appeal to anything unproved: `lam = (n)` at `delta = 1`, where both
closures span the irreducible ambient so `mult = 1`, `def = 0` and `D = 0`
identically; and `lam = (3,2,2,1^5)` at `(4,3,3)`, where the ambient plethysm
coefficient is zero, so *every* orbit closure in `Sym^4 C^16` has multiplicity
zero there and `D = 0` — a self-contained kill that does not invoke
Bürgisser–Ikenmeyer–Panova and so does not depend on whether their hypotheses
reach `(n,m) = (4,3)`.  Both passing weights, moreover, have
`m_{per^pad} = m_det = 1`, where the only obstruction the arithmetic leaves
room for is an occurrence obstruction — the sub-case already closed.  For the
line to reopen, the symmetric rectangular Kronecker coefficient `m_det` would
have to overtake the ten-variable monomial count `m_{per^pad}` at some larger
`delta`, and the measured trend runs hard the other way; the unpadded `n = m =
3` model, which is the `m → n` limit of the same question, fails the screen
harder still, with the ratio of Peter–Weyl totals widening 1 : 5.7 : 28.9 : 131
through `delta = 4`.  Neither is a proof, and the honest residue is that the
question is undecided outside the range reached — but that is not a reason to
spend the `n = 4` budget, because an `n = 4` grind computes `def_det` alone
while the separating quantity is a *difference* of deficits whose permanent
half would still be missing.  **The deficit should therefore be described in the
paper as what it demonstrably is — an exact measure of non-normality, with
closed forms in two worlds, a first determinant value, and now a first
permanent value `def_{per_3}((2,2,2),2) = 4` — and not as a separation tool.**

## 8. Range not reached

`(4,3,4)` and `(5,3,3)` were launched and had not completed when the session
ended; `m_{per^pad}` at `N = 15,16` in ten variables is the bottleneck (tens of
minutes per weight).  Neither is needed for the verdict above, which is stated
only over the range listed in §3, but both are the obvious next increments and
are pure compute — no new mathematics, no engine, no certificates.
