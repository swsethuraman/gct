# The onset degree `e` at `r = 4`: measured to `e >= 10`, and the top end has a name — 320112

Session 33, branch `s33-e4`, 2026-09-01.  Clone tip `29bea5f` (the s30
integrator review itself; ancestry gate passed).  Pre-registration:
`results/PREREG_s33.md`, committed before any Phase-1 number.  Per-rung
record: `results/e4_ledger.md`, banked as completed.  Code:
`analysis/wk9_s33_ladder.py`, `analysis/wk9_s33_rungs.py` (both reuse
`wk8_s30_core.py` / `wk8_s30_pleth.py` rather than rewrite them).  No
session-33 collision found in the record.

**Verdict in one line.**  The ideal of the determinantal-quartic hypersurface
`D_4 ⊆ Sym^4 C^4` is **zero through degree 9** — measured with certificates at
every live rung (4, 6, 7, 8; degrees 1, 2, 3, 5, 9 are empty of invariants
outright), so **`e >= 10`** — the standing `e = 6` prediction is **refuted**
and s29's `e >= 7` confirmed; meanwhile Phase 0 found the degree in the 2024
literature: **`e = 320112`** (Leal–Lozano Huerta–Vite), which this session
adopts as the working value and could never have reached by climbing.

---

## 1. The object, and what was on the record

`D_4 = closure{det_4(s_1 A_1 + ... + s_4 A_4)} ⊆ Sym^4 C^4` has codimension
exactly 1 (`docs/sweep62.md` §4: Jacobian lower bound 34 meets the stabiliser
upper bound `16·4 − 30 = 34`; upgraded to a sandwich in `docs/s30_review.md`
§3).  Its ideal is therefore principal: one irreducible polynomial `h` of
degree `e`, necessarily an `SL_4`-invariant of quartic surfaces, of weight
`(e,e,e,e)`.  On the record before this session: `e >= 6` (s29: no invariants
in degrees 1, 2, 3, 5; `mult((4^4), 4) = 1 = a` rules out 4), and an
unresolved dispute — the integrator's `e = 6` against s29's `e >= 7`, with the
deciding cell `mult((6^4), 6)` costed at `N_S = 12652` and abandoned twice.

## 2. Phase 0 — the literature has the number *(adopted, not certified)*

**`e = 320112`.**  R. Leal, C. Lozano Huerta, M. Vite, *The Noether–Lefschetz
locus of surfaces in P^3 formed by determinantal surfaces*, Math. Nachr.
**297** (2024) 4671–4688 (arXiv:2303.09028), Theorem 2: smooth determinantal
quartics form a divisor with five prime components, one per matrix shape; the
`4x4` all-linear component — smooth members carry the ACM sextic of genus 3;
this is `D_4` — has degree **320112**, by expressing the component classes in
Noether–Lefschetz divisors and extracting coefficients of the associated
modular form.

Two sibling components carry independent anchors, which is why the table is
believed: the line component's **320** is the classical count, and the
elliptic-quartic component's **38475** was obtained independently by
Cukierman–Lopez–Vainsencher (arXiv:1209.3335) via Bott-formula excess
intersection, with the quartic case's contracted pencils handled explicitly.
Named caveat (pre-registered): each determinantal quartic carries the
conjugate curve pair `C, C' = 3H − C` with identical invariants `(6, 3)`, so
incidence-style counts see each surface twice; LLV's statement is *prime
divisors with these degrees* — the reduced claim — and their NL-divisor
bookkeeping is the mechanism that carries it.  Adopted as P1/P2; nothing this
session can reach `delta = 320112`, so it is a working value with two external
corroborations, not an in-house certificate.

Searches recorded in the prereg.  Symmetroid caution honoured throughout:
quartic *symmetroids* (symmetric `4x4`) are a different, higher-codimension
object and never enter.

## 3. Phase 1 — the ladder *(exact; three independent routes on the overlap)*

`a(delta) = <h_delta[h_4], s_{(delta^4)}>`, `delta = 1..24`, by a weight-space
DP with the 24-term signed Weyl sum, cross-checked against
`wk8_s30_pleth.py` (`delta <= 9`) and brute-force enumeration
(`delta <= 4`), with s29's anchors and `N_S` records reproduced exactly:

    delta :  1  2  3  4  5  6  7  8  9  10  11  12 ...
    a     :  0  0  0  1  0  1  1  3  0   5   2  11 ...

**Free exclusions: `e ∉ {1, 2, 3, 5, 9}`** — no `SL_4`-invariant exists there
at all, and — new this session — the **degree-9 gap** means rung 9 never needs
to be measured.  By-product banked: this row is the Poincaré series of the
invariant ring of quartic surfaces through degree 24 (`results/e4_ledger.md`),
with the `a(8) = 3 = {I4^2} + two new generators` structure visible.

## 4. Two pieces of machinery *(proved)*, and why rung 6 cost 7 seconds

**The rectangular-weight reduction.**  For `lam = (delta^4)` the Weyl module
`S_lam = det^delta` is one-dimensional, so the highest-weight space *is* the
invariant space.  Two consequences: (i) every such vector lies in the
`sign^delta`-isotypic part `V_chi` of the `S_4` variable-permutation action on
the weight-`(delta^4)` monomial basis — a permutation matrix `P_sigma` acts on
a weight-`(delta^4)` invariant by `sign(sigma)^delta` (odd `sigma` enters
`SL_4` after composing with `diag(-1,1,1,1)`, which scales the weight space by
`(-1)^delta`); (ii) on `V_chi`, killing `E_12` kills every raising operator,
because `E_23 = Ad(P_{(123)}) E_12` and `E_34 = Ad(P_{(13)(24)}) E_12` with
*even* conjugators.  Hence

    a = dim ker( E_12 |_{V_chi} ),  and the kernel is the invariant space —

an elimination on `n_chi ≈ N_S/24` columns instead of `N_S`.  Row side:
column values obey `v_{swap34(t)} = (-1)^delta v_t`, so `(34)`-swap-redundant
rows are dropped, and for odd `delta` the swap-fixed rows vanish identically —
asserted exactly in-run, a free correctness check.  This is why the deciding
cell that was `N_S = 12652` (9.0 GB unreduced, twice abandoned) became a
`5930 x 661` problem that runs in seconds.

**The certified compressed kernel.**  For rung 8 (`113942 x 10738` after
dedup, 500k nonzeros) even the reduced matrix is 9.7 GB dense, so the kernel
is taken from `Agg = P·M` with `P` random over `F_p` (assembled sparsely in
numpy int64, every product reduced mod `p` before accumulation; all
elimination stays in flint).  The certificate is an inequality chain, not a
hope: `rank(Agg) <= rank_p(M) <= rank_Q(M) = n_chi − a(plethysm)`, so the
pre-registered assert `dim ker(Agg) = a` **forces equality throughout** and
`ker(Agg)` *is* the reduction of the rational invariant kernel.  Validated
(V6) against the exact blocked-rref route at rungs 6 and 7: same `a`, same
`mult`, identical kernel span, both primes.

## 5. Phase 2 — the rungs *(measured, with one-sided certificates)*

Gate first: the binary-quartic witness (`closure{l^3 m}`, `lam = (4,4)`,
`delta = 2`) through the unreduced s30 pipeline gave `mult = 0` with kernel
`(12, -3, 1)` at both primes — the corrected-rule signature — and the full
validation battery V1–V6 passed before any new rung (ledger, gate table).

| rung | `a` | `mult` | consequence |
|---|---|---|---|
| 4 | 1 | 1 | `e != 4` re-certified, both pipelines agreeing on the kernel vector itself |
| 6 | 1 | **1** | **`e != 6` — the dispute rung**: the unique degree-6 invariant does not vanish on `D_4` |
| 7 | 1 | **1** | `e != 7` |
| 8 | 3 | **3** | `e != 8`: all three degree-8 invariants independent on `D_4` |

Every measurement is a rank *attaining* `a`: `rank_p <= rank_Q <= a`, so each
row is a certificate that `a` specific polynomials are independent on `D_4`,
exhibited at explicit integer points — bad luck can only lower a rank, never
raise it, so no probabilistic step survives in the `mult = a` direction.  Both
house primes at every rung; the sceptical `mult < a` branch was never entered.

**Therefore `e >= 10`** — and with the ladder's degree-9 gap, the first rung
this programme cannot reach is `delta = 10` (`n_chi = 146206`: the reduced
echelon alone is ~171 GB against 6.5 usable; the unreduced model is ~1e5x over
budget).  K3 applies: the wall is stated, and heroics were not attempted.

## 6. Honest boundary

- **Proved:** the reduction lemma and the compressed-route certificate chain
  (§4); the ladder values (exact integer computation, three routes agreeing on
  every overlap); the free exclusions `{1, 2, 3, 5, 9}`.
- **Measured, certified one-sidedly:** `mult = a` at rungs 4, 6, 7, 8 — these
  are unconditional linear-independence certificates over `F_p`, hence over
  `Q`.  They do not depend on the evaluation points being generic.
- **Premise inherited, one soft link:** "first deficient rung = `e`" reads
  the measurements through principality, i.e. codim exactly 1, whose one soft
  link (`docs/s30_review.md` §3) is the finite-stabiliser hypothesis for
  generic 4-tuples — one page to write, not written here.  The measurements
  themselves are premise-free statements about `mult`; only their *reading* as
  a bracket on `e` uses it.
- **Adopted, not certified:** `e = 320112`.  Two external corroborations on
  sibling components (320 classical; 38475 by an independent method), the
  reduced-vs-incidence caveat named in §2.  Everything measured here is
  consistent with it, and nothing reachable could certify it.
- **Regime warning for reuse:** `D_4` is an NL *divisor*; its onset scale
  (`~3e5`) belongs to the codimension-1 regime.  The `r = 5` strata have
  codimension 20 and 31 — more equations, typically earlier onsets — so this
  number does **not** transfer as a bound on the `r = 5` onset degrees.  What
  transfers is the direction: onset degrees of these determinantal loci are
  not small, and `delta = 6, 7` sweeps finding empty ideals is what "too
  early" looks like (the same lesson as sweep62, now with a named top end).
- Also inherited: `mult = a` at every rung is what P2 predicted, so this
  session never tested its own sceptical branch — the protocol exists on
  paper (prereg §2) and in code, but has still never fired in this programme.

## 7. What it buys, and what next

1. **The dispute is closed**: `e != 6`, by measurement, both primes, in
   7 seconds — the cell s29 costed at 12652 columns and two sessions
   abandoned.  `e >= 10` measured; `e = 320112` adopted with named sources.
2. **The calibration the brief wanted:** at `r = 4` the ideal is invisible at
   every degree this programme's containers can sweep — by five orders of
   magnitude if LLV is right.  The `delta = 7, ell = 5` recommendation stands,
   but with expectations set: empty ideals there would not be news for a long
   way up the degree axis.
3. **Tooling transfer:** the reduction (§4) applies at any full-rectangle
   weight `(delta^r)` — at `r = 5` it divides by up to `|S_5| = 120` — and the
   compressed certificate applies at *every* weight: it removes the 3-stacked
   raising rows and the build-list overhead, moving the general-weight model
   from `5.6e-8·N_S^2` GB toward `~2.4e-8·N_S^2` GB (measured 2.89 GB peak at
   `n_chi = 10738`), i.e. the sweep62 frontier `N_S ~ 9900` moves to
   `~ 16000` on the same container.  If the programme ever wants `e`
   in-house, the object to reproduce is LLV's modular-form coefficient
   extraction — a literature-reproduction session, not a rank computation.
