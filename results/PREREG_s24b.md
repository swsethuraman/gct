# Pre-registration — session 24b: the two cheap steps

Written **before** any computation of this session.  Branch `s24-screen`,
2026-08-31.  Nothing below has been checked.

**Sync alarm, recorded first.**  `origin/main` is at `5cdc29c`; commit
`99b0c7b` (session 24's pre-registration) is not present, and
`docs/obstruction_power.md`, `docs/session_24.md`, `results/PREREG_s24.md`,
`analysis/wk5_s24_*.py` are all absent from the clone.  Session 24's branch has
**not** landed on GitHub.  This session therefore branches from `origin/main`
and writes only NEW files, so that nothing here conflicts when the real merge
lands.  Session 24 results are cited below as established-but-unmerged, never
re-derived and re-presented as new (rule 9's rollback discipline).

## 0. What is being computed, and why the two steps are the right two

Session 24's Lemma 1: for two orbit closures `A`, `B` in the same ambient,

    D(lam) := mult_lam C[B] - mult_lam C[A]  =  P(lam) - Def(lam),
    P   = m_B - m_A         (Peter-Weyl / stabiliser side, no geometry)
    Def = def_B - def_A     (deficit side, needs both closures)

with `m_X(lam) = dim (S_lam^*)^{H_X}`.  An obstruction to `B ⊆ A` is
`D > 0`; it is **deficit-driven** if also `P <= 0`.

For GCT take `A = closure(GL_{n^2} · det_n)`, `B = closure(GL_{n^2} · x_0^{n-m} per_m)`
in `W = Sym^n C^{n^2}`.  **Step 1** asks whether any `lam` has
`m_B(lam) <= m_A(lam)`; if none does, no obstruction can be deficit-driven and
the line closes.  **Step 2** computes the permanent's deficit at `n = m = 3`,
where the determinant's is known and no padding is involved.

## 1. What `m` is, precisely, on each side

**Determinant.**  `Stab_{GL_{n^2}}(det_n) = {X ↦ AXB : det A det B = 1} ⋊ <transpose>`,
of dimension `2n^2 - 2` (n=1: 0; n=2: SO_4, dim 6 = 2·4−2; n=3: **16**).
*Note a discrepancy to be recorded, not silently fixed*: `paper/det3-conductor.tex`
§4 states dimension 17 for `n = 3` and the session-24 brief quotes 17 → 31.
17 is `dim (GL_3 × GL_3)/C^*`, i.e. the stabiliser of the *point* `[det_3]`;
the stabiliser of the *vector* `det_3`, which is what Lemma 1 and the
Peter–Weyl identity require, has dimension 16.  I will compute with the vector
stabiliser and calibrate against the paper's own numbers.

By Schur–Weyl I will use

    m_det(lam) = (1/2) [ g(lam, (delta^n), (delta^n))  +  X(lam) ],
    X(lam)     = (1/N!) sum_rho |C_rho| chi^lam(rho) chi^{(delta^n)}(rho~),

where `N = n·delta`, `g` is the Kronecker coefficient, and `rho~` is the
partition built from `rho` by keeping each odd part and replacing each even
part `r` by two parts `r/2`.  (Derivation: `tr(k^r) = tr(A^r) tr(B^r)` on the
identity component and `tr(k^r) = p_r(AB)` for odd `r`, `p_{r/2}(AB)^2` for
even `r`, on the transpose coset; the Haar average over `{det A det B = 1}`
picks the rectangle.)

**Padded permanent.**  I derive the stabiliser rather than cite it, and will
record the derivation.  Let `U* = span(x_0, y_11..y_mm)`, `dim U = m^2+1`, and
`Z = (U*)^perp ⊆ V`.  Unique factorisation of `x_0^p per_m(y)` (`p = n−m ≥ 1`)
forces any stabiliser element to preserve `U*`; the `x_0`-linear coefficient
`sum d_ij ∂per/∂y_ij` vanishes only for `d = 0` because the sub-permanents are
linearly independent.  Hence

    Stab(x_0^p per_m) = { x_0 ↦ c x_0 , y ↦ L y : per_m ∘ L = c^{-p} per_m },

`L` monomial-of-monomial (`X ↦ D_1 P X Q D_2`) plus transpose, so the whole
group is MONOMIAL in the basis `{x_0, y_ij}`: a 6-torus (for `m = 3`) times a
finite part `(S_3 × S_3) ⋊ Z/2` of order 72.  Its dimension is `2m − 1 = 5`.
Inside `GL_{n^2}` the stabiliser is this, extended by all of `GL(Z)` and the
`Hom(V/Z, Z)` block, so

    m_{per^pad}(lam) = 0 unless ell(lam) <= m^2 + 1,
    and otherwise = dim (S_lam(C^{m^2+1}))^{Stab(x_0^p per_m)} .

(`GL(Z)`-invariance kills every term of the `gr` decomposition with a nonzero
`Z`-part.)  I will verify this row bound computationally rather than assume it.

For the monomial groups the count is exact and elementary:
`m = (1/|F|) sum_{f in F} [ sum of coefficients of chi_{S_lam}(D f) over the
T-invariant weights ]`, with `chi_{S_lam}(Df) = det( h_{lam_i−i+j} )` and
`sum_k h_k z^k = prod_cycles (1 − z^{|c|} X_c)^{-1}`.  The `T`-invariant
weights are: for `per_3` (n = m = 3), the 3×3 exponent matrices with all row
and column sums `delta`; for the padded case, the same plus `mu_0 = delta(n−3)`.

## 2. Pre-registered hypotheses and named falsifiers

**E1 (step 2, the first weight).**  `m_{per_3}((2,2,2)) > 1 = m_{det_3}((2,2,2))`.
Since `Sym^2(Sym^3) = S_(6) + S_(4,2)` contains no `S_(2,2,2)`, `mult = 0` for
every orbit closure in `Sym^3 C^9` at that weight, so
`def_{per_3}((2,2,2),2) = m_{per_3}((2,2,2))`.  I predict the value is **2**.
*Falsifiers:* any value `<= 1`; or a value `≠ 2` (which refutes the point
prediction but not the inequality — I will score these separately).

**E2 (step 2, the unpadded model).**  At `n = m = 3` the permanent's stabiliser
(dim 4 as a subgroup of `GL_9`, once the 1-dimensional kernel is quotiented) is
far smaller than the determinant's (dim 16), so `m_per >= m_det` at every
weight, and **no weight passes the screen** in the unpadded model: every
multiplicity obstruction there is Peter–Weyl and the deficit is not needed.
*Falsifier:* one `lam` with `m_{per_3}(lam) < m_{det_3}(lam)`.

**E3 (step 1, the real padded shape) — the prediction I expect to matter.**
For `n > m` the padded permanent's stabiliser is *huge* (it contains `GL(Z)`
and the whole `Hom(V/Z,Z)` block; for `(n,m) = (4,3)`, `dim Z = 6` and the
group has dimension `36 + 60 + 5 = 101` against `dim H_det_4 = 30`).  I
therefore predict the screen **passes broadly**: `m_{per^pad}(lam) <= m_{det_n}(lam)`
for all, or nearly all, `lam` in accessible range — including at every `lam`
where `m_{per^pad} = 0` for row reasons.  *Falsifier:* a `lam` in range with
`m_{per^pad}(lam) > m_{det_n}(lam)`.

**E4 (the consequence, if E3 holds).**  If `P(lam) <= 0` for every `lam` in
range, then in that range **no multiplicity obstruction to `per^pad ⊆ det` can
be Peter–Weyl**: every one, if any exists, must be deficit-driven.  That
reverses the tone of session 24's recommendation — it would make the deficit
the *only* available mechanism rather than a useless correction — and I log
now that I expect to have to say so.  *Falsifier:* same as E3.

**E5 (support).**  `m_{per^pad}(lam) = 0` whenever `ell(lam) > m^2 + 1`.
*Falsifier:* a nonzero value with more rows.

**E6 (calibration, must pass or the pipeline is wrong).**
(a) `m_{det_3}(lam)` for `lam ⊢ 6` is nonzero exactly at `(6)`, `(4,2)`,
`(2,2,2)`, with value 1 each — this is forced by the paper's `delta = 2` row
`(0,0,1)` and total deficit 1.
(b) `def_{det_3}((2,2,2),2) = 1`.
(c) the ambient plethysm `Sym^delta(Sym^3 C^9)` reproduces
`dim Sym^delta(Sym^3 C^9)^{SL_9} = 0,0,0,0,0,1,...` for `delta = 3,6,...,18`
(session 21's census).
*Falsifier:* any disagreement.  If E6 fails I stop and fix rather than report.

**E7 (verdict).**  I expect the honest verdict to be **"the line is not closed
— it is live, and for an uncomfortable reason"**: not because a candidate
weight was found, but because the Peter–Weyl side is structurally unable to
separate in the padded setting, which is exactly the regime where the deficit
would have to do all the work.  I expect to have to revise session 24's closing
paragraph rather than confirm it.  *Falsifier:* E3 fails, i.e. the padded
screen finds `m_per > m_det` somewhere, in which case Peter–Weyl obstructions
are available and the deficit line closes as session 24 predicted.

## 3. Scope, declared in advance

Exhaustive over: all partitions `lam ⊢ n·delta` with `ell(lam) <= n^2`, for
`(n,m,delta)` in a range fixed by cost, which I will state exactly in
`docs/screen_results.md` together with what "accessible" cost.  Anything
sampled rather than exhausted will be labelled sampled.

Exact arithmetic only (Python integers / `Fraction`).  Two independent routes
for every reported number: for the monomial groups, Jacobi–Trudi coefficient
extraction versus the Schur–Weyl class-function average; for `m_det`, the
Kronecker route versus the same class-function average; plus the E6
calibrations against already-published values.
