# Pre-registration — session 33: pin `e`, the degree of the determinantal-quartic hypersurface at `r = 4`

Written **before** any Phase-1 number exists.  Branch `s33-e4`, 2026-09-01.

**Clone state.**  Tip `29bea5f` — which *is* the s30 integrator review; the
ancestry gate `git merge-base --is-ancestor 29bea5f HEAD` passes (ancestry, not
equality — the tip being the named commit satisfies it).  `7d93449` is an
ancestor, so `docs/isotypic_rank.md` §1 carries the corrected raising rule in
this clone.  **No session-33 collision**: `git log --all` and a filename sweep
show no prior claim to 33.

**Engineering.**  Container: 7 GB RAM (~6.5 usable), 2 cores.  `python-flint`
0.9.0 installed and `nmod_mat` verified.  House primes `(2147483647,
2147483629)`.  Standing rule honoured: **no hand-rolled elimination** — every
rank and nullspace in this session is a flint `nmod_mat` call; python/numpy do
assembly and integer counting only.

**The convention, restated as I will implement it**

    E_ij . c_alpha = (alpha_i + 1) . c_{alpha + e_i - e_j}

## 0. Phase 0 record — the literature pass, made before anything was computed

**P1 — the literature value: `e = 320112`.**  Source: R. Leal, C. Lozano
Huerta, M. Vite, *The Noether–Lefschetz locus of surfaces in P^3 formed by
determinantal surfaces*, Math. Nachr. **297** (2024) 4671–4688;
arXiv:2303.09028, Theorem 2 and its table.  Smooth determinantal quartics form
a divisor in `|O(4)| = P^34` with **five prime components**, one per matrix
shape; the `4x4` all-linear component `F_1` — the one whose smooth members
carry the ACM curve of degree 6, genus 3, i.e. **our `D_4`** — has degree
**320112**.  (`D_4` is irreducible of dim 34 and contains the smooth
determinantal quartics as a dense subset, so `D_4 = closure(F_1)`.)

*Why the source is believed.*  Two of the five sibling components carry
independent anchors: `F_4` (the `2x2` shape whose curve is a line) has degree
**320**, the classical count of quartics containing a line; `F_3` (elliptic
quartic curve) has degree **38475**, which Cukierman–Lopez–Vainsencher
(arXiv:1209.3335) obtained by Bott-formula excess intersection — a completely
different method, and their `d = 4` case explicitly handles the pencil
contraction that makes quartics delicate.  Two independent corroborations of
the same table.

*The caveat, named in advance.*  A determinantal quartic carries the conjugate
curve pair `C` and `C' = 3H − C`, both of degree 6 and genus 3, so
incidence-style counts see each surface twice; whether a stated degree is the
reduced divisor degree or an incidence pushforward is exactly the bookkeeping
that must be right.  LLV state their result as *prime divisors with these
degrees* — the reduced claim — and their NL-divisor decomposition is the
mechanism that handles it.  I adopt 320112 as P1 and I do **not** claim this
session certifies it; at that scale no rung-climb can.

*Searches run* (recorded per the brief): "degree of the hypersurface of
determinantal quartic surfaces P^34"; "determinantal quartic surface locus
degree Noether-Lefschetz genus 3 sextic"; ""320112" determinantal quartic
surfaces Noether-Lefschetz"; full fetches of arXiv:2303.09028 (v3) and
arXiv:1209.3335.  Beauville (Michigan Math. J. 48 (2000), math/9910030)
surfaced and supplies the characterisation, not the degree.  **Symmetroid
caution honoured**: `F_1` is the general (not symmetric) `4x4` linear locus;
quartic symmetroids have much higher codimension and never enter.

## 1. Pre-registered predictions

**P2 — committed value: `e = 320112`**, i.e. **far beyond any measurable
rung**.  Operationally for this session: **every rung within reach returns
`mult = a`**; in particular the deciding rung of the standing dispute returns
`mult((6^4), 6) = 1 = a`, refuting the integrator's `e = 6` and resolving
session 29's `e >= 7` in the strong form.  *Regime statement:* P1/P2 come from
the Noether–Lefschetz / modular-form degree theory of quartic K3s (LLV),
anchored classically (320) and by excess intersection (38475) — a regime
disjoint from the isotypic-rank machinery used here, so agreement carries
information.  Session 29's heuristic ("NL divisors have no reason to be cut by
the unique degree-6 invariant") pointed the same way; it now has a number.
*Falsifier:* any measured rung with `mult < a` — which would kill P1/P2
together and be reported loudly, since it would mean the LLV degree is not `e`.

**P3 — every rung below `e` returns `mult = a` exactly.**  Under P2 this is
every rung this session can reach.  A `mult < a` triggers the sceptical
protocol (§2) before it is believed.

**P4 — structure above `e`, stated in advance** (this is the "state what you
expect before measuring" required by the brief, though under P2 it is
unreachable): the ideal is principal, so the deficiency at rung `delta` is
`a(delta − e)` with `a(0) = 1: `exactly 1` at `delta = e`; **0** at `e+1, e+2,
e+3, e+5` (since `a(1) = a(2) = a(3) = a(5) = 0` — the ideal is *invisible* in
the rectangular ladder just above its onset); 1 at `e+4, e+6, e+7`; 3 at
`e+8`.  A first deficiency different from 1 violates principality → K2.

**P5 — ladder self-checks, the falsifiers for Phase 1 itself.**
`a(1) = a(2) = a(3) = 0` (structural: `h_delta[h_4]` has at most `delta` rows,
and a 4-row rectangle needs `delta >= 4`); the s29-published anchors
`a((delta^4), delta) = 0,0,0,1,0,1,1,3` for `delta = 1..8` must reproduce;
`a(10) >= 1` (the degree-10 catalecticant `det(Sym^2 V^* -> Sym^2 V)` is an
`SL_4`-invariant); `N_S((6^4)) = 12652` and `N_S((7^4)) = 57232` (s29's
recorded dimensions) must reproduce from my enumeration; the DP route must
agree with `analysis/wk8_s30_pleth.py` wherever both run, and with naive
brute-force enumeration at `delta <= 4`.  Any failure stops Phase 1.

## 2. Method commitments, before any Phase-2 number

**Witness gate first** (kill criterion K1): binary quartics, `closure{l^3 m}`,
`lam = (4,4)`, `delta = 2`, run through the **unreduced s30 pipeline**
(`analysis/wk8_s30_core.py`, reused verbatim): must give `mult = 0` with
kernel `∝ (12, −3, 1)` on `(c40c04, c31c13, c22^2)`.  Wrong-rule signature:
`(1, −4, 3)` and `mult = 1`.

**The rectangular-weight reduction (new this session, registered before use).**
For `lam = (delta^4)` the Weyl module `S_lam` is `det^delta` —
one-dimensional — so every highest-weight vector of weight `(delta^4)` *is* an
`SL_4`-invariant.  Consequently: (i) each such vector lies in the
`sign^delta`-isotypic part `V_chi` of the `S_4` variable-permutation action on
the weight-`(delta^4)` monomial basis (permutation matrices, odd ones composed
with `diag(−1,1,1,1) ∈ SL_4`, act on it by `sign(sigma)^delta`); (ii) since
`E_23 = Ad(P_(123)) E_12` and `E_34 = Ad(P_(13)(24)) E_12` with both
conjugators even, a vector of `V_chi` killed by `E_12` is killed by every
simple raising.  Hence

    a = dim ker( E_12 |_{V_chi} ),   and the kernel IS the invariant space,

which shrinks the elimination from `N_S` columns to `~N_S/24`.  This is a
proved reduction, not a numerical trick; it will be written up in
`docs/e4_hunt.md`.  **Validation battery, all before any new rung** (kill
criterion K4): V1 the witness gate above; V2 rung `delta = 4` measured by
*both* pipelines — same `a = 1`, same `mult`, same kernel vector after orbit
expansion (up to scale); V3 `N_S` from basis enumeration equals the DP weight
dimension at every rung; V4 `delta = 5` (odd, so the *sign* branch runs):
reduced kernel dimension must be `0 = a(5)`; V5 rung 6 at both primes.

**Per-rung protocol.**  Rungs in ascending order `delta = 4, 5, 6, 7, 8`, no
rung skipped (`a = 0` rungs recorded as excluded-for-free).  At each live rung:
`a` by reduced-kernel dimension must equal Phase 1's plethysm; evaluation at
`npts = a + 8` random 4-tuples of `4x4` matrices (entries in `[−40, 40]`,
s30's `restrict`/`eval_row` reused verbatim, `det_form(4)`); `mult` = flint
rank of the kernel-invariants-at-points matrix; both primes at `delta <= 7`;
at `delta = 8`, first prime fully and the second as budget allows (a rank
attaining `a` is already a one-sided certificate: `rank_p <= rank_Q <= a`).
Each rung banked to `results/e4_ledger.md` and committed before the next
starts, because the container resets.

**Sceptical protocol at any `mult < a`** (verbatim from the brief): re-run at
3× evaluation points on the second prime and a fresh seed; exhibit the kernel
vector; verify it vanishes at 10 fresh determinantal points and does **not**
vanish at several random non-determinantal quartics; if it vanishes everywhere
tested, something is wrong — investigate before reporting.

## 3. Kill criteria

- **K1** — witness gate fails: stop, report, touch nothing.
- **K2** — deficiencies at two rungs inconsistent with P4's principal-ideal
  sequence: the codimension-1 premise is in question; re-run
  `analysis/wk8_s30_dims.py` at `r = 4` with fresh points before believing
  anything.
- **K3** — memory wall: report the bracket `e > delta_reached` honestly, with
  the exact wall (`N_S`, `n_chi`, predicted vs measured GB).  A bracket is a
  result; heroics are not.
- **K4** — any reduced-vs-unreduced disagreement in V1–V5: stop Phase 2 and
  report; the unreduced s30 pipeline is authoritative.

## 4. Budget model, stated in advance

House unreduced model `5.6e-8 · N_S^2` GB: rung 6 (`N_S = 12652`) predicts
**9.0 GB against 6.5 usable — the deciding rung is out of reach of the
unreduced pipeline in this container**.  That is why the reduction above is
registered as the production method rather than found mid-run.  Reduced-model
dominant cost is the `N' × n_chi` flint matrix (`N'` the adjacent weight
space, `n_chi ~ N_S/24`), predicted per rung in the ledger from Phase-1 exact
dimensions **before** any rank is run; rung 8 is attempted only if those
numbers and a timing pilot at rungs 6–7 say it fits; otherwise K3 applies and
the wall is stated.
