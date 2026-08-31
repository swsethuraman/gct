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

`m_det` is cheap (Kronecker); `m_{per^pad}` is the bottleneck.  Since a live
weight needs `m_{per^pad} > 0`, and a passing weight needs `m_det >= m_{per^pad} >= 1`,
it suffices to evaluate `m_{per^pad}` on the support of `m_det` intersected
with `ell(lam) <= m^2+1`; every weight outside that support has
`m_det = 0 < m_{per^pad}` and fails the screen automatically.  Both the
brute-force enumeration (all `lam`) and this optimised form were run, and agree.

| `(n,m,delta)` | `lam ⊢ N` | scanned | live weights | `P > 0` (screen fails) | **screen passes** |
|---|---|---|---|---|---|
| (4,3,1) | 4  | 5   | 2  | 1  | 1 — `lam=(4)`, vacuous |
| (5,3,1) | 5  | 7   | 1  | 0  | 1 — `lam=(5)`, vacuous |
| (6,3,1) | 6  | 11  | 1  | 0  | 1 — `lam=(6)`, vacuous |
| (4,3,2) | 8  | 22  | 19 | 19 | **0** |
| (5,3,2) | 10 | 42  | 24 | 24 | **0** |
| (6,3,2) | 12 | 77  | 7  | 7  | **0** |

Exhaustive, not sampled, over every `lam ⊢ n·delta` with `ell(lam) <= n^2`.
(At (6,3,2) two further weights, `(4,4,4)` and `(4,4,2,2)`, have `m_det = 1`
and `m_{per^pad} = 0`: they satisfy the inequality numerically but are dead —
`mult_B = 0`, so `D <= 0` regardless.)

**The one formal pass is vacuous.**  At `delta = 1` the only weight with
`m_det >= 1` is `lam = (n)`, where `m_det = m_{per^pad} = 1` and `P = 0`.  But
`W = Sym^n C^{n^2}` is an irreducible `GL_{n^2}`-module, so every nonzero orbit
spans it and restriction `W^* → C[X]_1` is injective for **both** closures:
`mult = 1` and `def = 0` on both sides, hence `D = 0` identically.  It is a
weight where nothing can happen, not a candidate.

**Sample of the margin** — `(n,m,delta) = (4,3,2)`, all 19 live weights:

    lam            m_det  m_perpad   P          lam            m_det  m_perpad  P
    (8)              1       3       2          (4,3,1)          0       7      7
    (7,1)            0       4       4          (4,2,2)          1      11     10
    (6,2)            1       9       8          (4,2,1,1)        0       3      3
    (6,1,1)          0       1       1          (4,1^4)          0       2      2
    (5,3)            0       6       6          (3,3,2)          0       2      2
    (5,2,1)          0       8       8          (3,3,1,1)        0       3      3
    (5,1,1,1)        0       1       1          (3,2,2,1)        0       6      6
    (4,4)            1       5       4          (3,2,1,1,1)      0       2      2
                                                (3,1^5)          0       1      1
                                                (2,2,2,2)        1       4      3
                                                (2,2,1^4)        0       1      1

The minimum margin over live weights is 1, and it does not approach 0.

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

**The line is closed in accessible range.**  Across every `(n,m,delta)` listed
in §3 — exhaustively, not by sampling — there is no weight at which a
deficit-driven obstruction to `closure(per_m^pad) ⊆ closure(det_n)` could
exist: every live weight has `m_{per^pad} > m_det`, so `P > 0` and any
obstruction there is one the classical Peter–Weyl side already sees, with the
deficit entering only as the subtraction that can destroy it; the single
formal pass, `lam = (n)` at `delta = 1`, is the weight where both closures span
the ambient and `D = 0` identically.  The unpadded `n = m = 3` model fails the
screen harder still, with the ratio of Peter–Weyl totals widening 1 : 5.7 :
28.9 : 131 through `delta = 4`.  For the line to reopen, one of three things
would have to change, and each is now a sharp and testable statement rather
than a hope: (i) the symmetric rectangular Kronecker coefficient `m_det` would
have to overtake the ten-variable monomial count `m_{per^pad}` at some larger
`delta` — the probe at the determinant-favourable weights nearest the rectangle
`(delta^n)` shows the margin *growing*, not shrinking, and at `delta = 3`,
`lam = (3,3,3,3)` the determinant's count is still 0 while the permanent's is
3; (ii) the row bound `ell(lam) <= m^2 + 1` would have to be evaded, which it
cannot be, since it is a theorem and not an artefact; or (iii) the relevant
weights would have to lie outside every range reachable by this method, in
which case the honest statement is that the question is undecidable by cheap
means and remains so — but that is not a reason to spend the `n = 4` budget,
because the `n = 4` deficit computes `def_det` alone and the separating
quantity is a *difference* of deficits whose permanent half would still be
missing.  On this evidence the deficit should be published as what session 24
concluded it is — an exact measure of non-normality, with closed forms in two
worlds, a first determinant value, and now a first permanent value
`def_{per_3}((2,2,2),2) = 4` — and not as a separation tool.
