# Integrator review — session 33 (pin `e` at `r = 4`)

2026-09-01.  Branch `s33-e4`, tip `0ca8d499` onto `29bea5f`.  Everything below
was re-verified independently before this review was written.

## 1. Verification — all checks pass

**The ladder, 24/24, by a disjoint route.**  I recomputed
`a(delta) = mult((delta^4), Sym^delta(Sym^4 C^4))` for `delta = 1..24` by
Kostant alternation over weight multiplicities (numpy DP over the 35 degree-4
monomials, signed 24-term Weyl sum) — a method sharing no code and no
mathematical route with the session's three.  All 24 values match, including
the load-bearing `a(9) = 0` exclusion and the live-rung set `{6, 7, 8}`.  The
session's size claims reproduce exactly: `N_S(6) = 12652`, `N_S(8) = 240481`,
`N_S(10) = 3428138` all agree with my weight-count DP.  The memory arithmetic
coheres throughout: rung 8's dense matrix is `8·N'·n_chi = 19.4` GB, blocked
echelon resident `8·n_chi^2 = 0.92` GB (measured peak 2.89 GB), and the
rung-10 wall figure is exactly `8·146206^2 = 171` GB.

**The citation, verified to the component.**  arXiv:2303.09028 (Leal–Lozano
Huerta–Vite, Math. Nachr. 297 (2024)) is real; its Theorem 2 gives five prime
NL components for determinantal quartics with degrees
`320, 2508, 136512, 38475, 320112`; and the degree-`320112` component `F_1`
is the `4x4` all-linear one — admissible pair `a = (5,5,5,5)`,
`b = (6,6,6,6)`, entry degrees all `1`, ACM sextic of genus 3 — i.e. exactly
our `D_4`.  The two sibling anchors check as the session stated: `320` is the
line component, `38475` the elliptic-quartic (complete intersection of two
quadrics) component with the independent Cukierman–Lopez–Vainsencher
Bott-formula computation.  A first summariser pass attributed 320 to the
all-linear component; a verbatim pass at the theorem's table resolved it as
above — worth recording that the confusion is easy to make ("linear
determinantal" vs "contains a line") and the session did not make it.

**The prereg discipline.**  `f31a3f4` (the pre-registration, with P1 = 320112,
the `C, C' = 3H − C` reduced-vs-incidence caveat named in advance, the
searches recorded, and the symmetroid trap explicitly avoided) is the first
s33 commit, before any Phase-1 number.  The compressed kernel route was
V6-validated against the exact route at rungs 6–7 *before* being trusted at
rung 8 — validate-then-use, in the right order, in the commit history.

**The verdict stands.**  `mult((delta^4), delta) = a` certified at rungs
4, 6, 7, 8 (both primes, rank-attaining one-sided certificates), `a(9) = 0`
free, hence `e >= 10`; `e = 320112` adopted from LLV with the caveat carried,
not certified — correctly labelled at every occurrence.

## 2. The reduction lemma is sound, and it is a keeper — with one porting warning

For `lam = (delta^4)` the highest-weight vectors are exactly the
`SL_4`-invariants; a permutation matrix `P_sigma` has determinant
`sgn(sigma)`, so invariants sit in the `sign^delta`-isotypic part of the
`S_4` action on the weight space.  On a character-isotypic subspace,
`ker E_12` alone suffices: conjugating `E_12` by *even* permutations reaches
every raising operator, because `A_4` is 2-transitive on `{1,2,3,4}`.  Both
halves check.  **Porting warning**: the 2-transitivity of the alternating
group holds for `n >= 4` variables and *fails* for 3 — do not carry the
one-operator shortcut into a three-variable context without adding the second
operator.  The practical effect is large (12652 → 661 columns at the deciding
rung) and the `n_chi` fractions at rungs 8 and 10 (~1/22 of `N_S`) are
consistent with the isotypic projection.

## 3. My `e = 6` is dead, and the failure has a name

I predicted the determinantal-quartic hypersurface would be cut by the unique
degree-6 invariant.  Rung 6 refutes it: that invariant does not vanish on
`D_4`.  Session 29's Q2 heuristic — *an NL divisor has no reason to be cut by
the lowest-lying invariant* — was the better prior, and now has a number
attached: the generator lives near degree `3.2 x 10^5`, five orders of
magnitude above the invariants I was reasoning about.  Failure class, for the
house ledger: **lowest-invariant bias** — assuming the geometrically
distinguished locus is cut out by the first invariant available.  It joins
regime transfer, quotient-blindness, and shared-spec correlation.

## 4. What `320112` does and does not mean for the hunt — and a cap from three lines of geometry

The astronomical degree is a *codimension-one* phenomenon: a principal ideal
carries its entire locus in a single generator, so the onset degree IS the
degree of the hypersurface.  It does not transfer to `r = 5`, where the
strata have codimension 20 and 31 — and there the onset is in fact **capped
low**.  Observe: every quartic threefold with a `4x4` linear determinantal
representation is singular.  (If the `A_i` are dependent the quartic is a
cone; otherwise the pencil spans a `P^4` in `P^15 = P(M_4)`, the rank-`<= 2`
locus has projective dimension 11, and `4 + 11 >= 15` forces a meeting; at a
rank-`<= 2` point the adjugate vanishes, so by Jacobi's formula every partial
`dF/ds_k = tr(adj M(s) A_k)` vanishes.)  This is the `n = 4` twin of session
28's singularity lemma, and consistent with the known fact that determinantal
hypersurfaces in `P^m`, `m >= 4`, are singular.  Consequence: the
discriminant of quartic threefolds — degree `5 · 3^4 = 405`, weight
`(324^5)` — lies in `I(D_5^{det_4})`.  The padded members `l · c` are also
always singular (along `l = 0` meet `c = 0`), so the discriminant separates
nothing; what it does is **bound the det-side onset**:

    7  <=  onset of I(D_5^{det_4})  <=  405

(lower end: s30 + the sweep record, empty through `delta = 6`).  The `r = 5`
hunt window is finite and sane.  `320112` says the `r = 4` codim-1 door is
closed; it says nothing pessimistic about `r = 5`, and the 405 cap says the
optimistic reading has a theorem behind it.

## 5. The tooling dividend, with one condition

The certified compressed kernel route moves the general-weight frontier from
`N_S ~ 9,900` to `~ 16,000` on the same container (model `2.4e-8 N_S^2` GB,
measured 2.89 GB at `n_chi = 10738`).  Condition before anyone spends budget
on it: V6 validated the route at *rectangular* rungs only.  Its first
general-weight use should re-validate against three banked s30 cells (same
kernel span, both primes) before any new cell is trusted — one cheap pass,
same validate-then-use ordering s33 itself honoured.  When session 34's
census lands, its feasibility line should be re-read under the new constant.

## 6. Standing after session 33

`e >= 10` certified; `e = 320112` named by verified literature, adopted with
the reduced-vs-incidence caveat still open; the `r = 4` codim-1 chapter is
closed (no rung-climb reaches `3 x 10^5`, and none should try).  The `r = 5`
onset window is `[7, 405]`.  Session 34's census-then-sweep at `delta = 7` is
exactly the right next probe, and its interpretation rule (pad bites are
expected and are not obstructions; only `D > 0` is the prize) is unchanged.
Process: the session refused a push it was nudged toward, citing the standing
delivery rules — correct, and worth a line of praise in the record.

*(Filed one commit after the s33 merge: the original copy into `docs/` failed
on a missing download and commit `63fe705` carried only the two briefs; this
file is the review that commit's message referred to.)*
