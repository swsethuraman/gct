---
session: B13-01
board_numbering: batch13
model_actually_run: Claude Fable 5.1
base: 00495110c62acfbbbc951e82cc218ed091563b3f
author: Swami Sethuraman, swsethuraman@beneficus.ai, Beneficus AI
bundle_parts: 1
---

# B13-01 — exact degree-13 reducible identity

**This report accompanies a one-part bundle** (`b13_01_fable.bundle`, `part00`
only; the `.md5` names the bare filename and carries a digest for the whole file
and for the single part).

## 0. Verdict, in one paragraph

The assignment asks for a **certified** element of `I(V_red) ∩ M₁₃` — a proof
that `i_red(13) ≥ 1`, which settles the LMR cell against a multiplicity
obstruction (`i_red(13) ≥ 1 ⟹ i_pad(13) ≥ 1 ⟹ i_pad(24) ≥ 1 ⟹ D = 1 −
i_pad(24) ≤ 0`).  **I did not obtain it, and I can now say precisely why no
carrier-free instrument reaches it at rung 13, and what does.**  What is
delivered exactly: `i_red(13) ≤ 3` **CERTIFIED** (a nonzero 36-minor at both
house primes, points and `u`-values shipped); `h_pad(21,17,2⁷;13) = 73`
**computed exactly** (Weyl alternation), which shows the proved normalisation
bound `mult_red ≤ h_pad` is **vacuous here** (73 > 39 = a) and therefore cannot
settle the cell; the three candidate reducible relations as mod-`p` vectors at
both primes (their `ℚ`-reconstruction is obstructed, coefficients `~10¹⁶⁰` in the
random-filling basis, matching s74's `δ=24` finding); and the exact sizes that
close off every direct route.  **The binding fact is that `i_red ≥ 1` is a
membership statement, and the only carrier-free instrument this assignment
designates — the compact-circuit reducible pullback — is an *evaluation*, whose
rank is a floor and whose nullity is therefore a ceiling on `i`.  It cannot, in
principle, certify `i_red ≥ 1`.**  The exact decider needs a carrier the box
cannot hold, or the coupled 73-dimensional pullback target (B13-03's method), or
the seminormal recursion (B13-02's).

## 1. Inputs and controls (CERTIFIED / MEASURED)

Clone base `main = 00495110`; the four batch-13 freeze files
(`batch13_board.md`, `batch13_corrections.md`, `stocktake_batch12.md`,
`batch13_worker_preamble.md`) are present.  Preflight: installed `python-flint
0.9.0`, `sympy 1.14.0`, `mpmath`; `numpy 2.4.4`, `scipy 1.17.1`, `gcc 13.3.0`
present; no `Singular`/`msolve` (not needed).  Host: 2 cores, ~8 GB, shared
across the batch — every plethysm run memory-bounded, never a full-character
build.

**Control reproduced (MEASURED), independent of the integrator's run**
(`analysis/wk12_int_rung13_kernels.py`, my seed 20260909, 60 points): reducible
rank **36/39 at both house primes**, generic control **39/39**, the three s74
padded kernel directions vanish at every reducible point, padded and reducible
kernels coincide.  This reproduces `docs/rung13_reducible.md` line for line and
is the ceiling `i_red(13) ≤ 3`.

`a(λ₁₃,13) = 39` is the source dimension (S3-confirmed three ways; generic
control 39/39 reproduced here).  The 39 rung-≤13 fillings of
`results/s74/source.json` (native rungs 12, 13; the two rung-12 fillings carried
to `M₁₃` by one `u`-step, `row_i = F_i^{native}·u^{13−d_i}`,
`u = 4![s₁⁴]f`) are the source.

## 2. The certified ceiling `i_red(13) ≤ 3` (CERTIFIED)

`results/certs/b13_01/minor36_i_red_leq_3.json`.  `E_source[i,k] =
F_i(ℓ_k·c_k)·u_k^{13−d_i}` (39 fillings × 44 integer reducible points, both house
primes).  A nonzero **36 × 36 minor** at both primes — dets `58031689` (P1),
`1407605007` (P2) — proves `rank_ℚ(E_source) ≥ 36`, hence `mult_red ≥ 36`, hence
`i_red(13) ≤ 3`.  The certificate ships the 36 point coordinates and their
`u`-values, and records `u(P_j) ≠ 0` at every one (both primes), so no
transported row is silently voided.

**This is a rank *floor*, i.e. an *upper* bound on `i_red`.**  It is the wrong
direction for the assignment; a floor never establishes `i_red ≥ 1`.  The
nullity 3 (both primes) and the coincidence of the sampled reducible and padded
kernels are **MEASURED** ceilings, exactly as `docs/rung13_reducible.md` states.

## 3. The normalisation bound is vacuous here (PROVED / computed exactly)

`docs/reducible_engine.md` §B proves `mult_red(λ,δ) ≤ h_pad(λ,δ) = Σ_μ a₃(μ,δ)`
over the horizontal-`δ`-strips `λ/μ`, `a₃(μ,δ)` the cubic-plethysm multiplicity.
This is the one **exact upper bound on `mult_red` that needs no rank** — the only
carrier-free route to `i_red ≥ 1` (`i_red ≥ a − h_pad`).

I computed it exactly (`analysis/wk13_b13_01_hpad.py`; the Weyl alternation
`a₃(μ) = Σ_{w∈S₉} sgn(w)·m(w(μ+ρ)−ρ)`, `m` = exact cubic-multiset count in
`analysis/wk13_b13_01_mcount.c`, a shared-memo counter validated against the
independent counts `B1 = 809 527 307`, `B2 = 117 718 904`):

    h_pad(21,17,2⁷;13) = 73,   over the 15 strips, a₃ = [1,2,2,3,3,4,4,5,5,5,6,7,8,9,9].

**Cross-check (independent):** the fifteen strips and their `a₃` reproduce
`docs/batch13_board.md` B13-04's re-audit exactly — "fifteen horizontal-13-strip
predecessors of `λ₁₃`, all `a ≥ 1`, `a` from 1 to 9."  Those `a` **are** these
`a₃`.

Since `73 > 39 = a`, the bound gives `mult_red ≤ min(a, h_pad) = 39`, i.e.
`i_red ≥ 0` — **vacuous**.  This is the exact analogue of the LMR cell, where
`h_pad = 521 > 273 = mult_det` makes the pad ceiling vacuous and "a rank is
genuinely required" (s64 integrator note 1).  **Finding: at rung 13 the
normalisation bound does not settle the sign; the exact reducible rank is
required, precisely as at `δ = 24`.**  No plan document states this for rung 13;
`docs/rung13_reducible.md` §3 recommends "run [the rank-`S` screen] at rung 13
first" as if it were cheap, and it is not (see §5).

## 4. The candidate relations (RECORDED)

`results/b13_01_candidates.json`.  The 3-dimensional left-kernel of `E_source`,
in RREF-canonical form at both house primes (identical pivot columns `[0,1,2]`).
These are the sampled reducible relations; they coincide with s74's padded
kernel.  **They are candidates, not certified elements** — the sampled kernel is
a ceiling.

**`ℚ`-reconstruction is obstructed.**  CRT + rational reconstruction from the two
house primes fails: the coefficients in the random-filling basis are `~10¹⁶⁰`
(support 21–24 of 39), needing `~17` primes; the two-prime reconstruction returns
vectors that do not even vanish at the sample points.  This is the same
phenomenon s74 recorded at `δ=24` ("94/274 coordinates fail at a 62-bit modulus;
entries `~10¹⁷⁰`").  **Consequence for the assignment:** even if membership were
certified, delivering the witness *over `ℚ`* in the filling basis would itself
require a many-prime reconstruction; S3's structured rational convention exists
precisely to give a better-conditioned basis, and its three per-node files
(19.5 MB) are the ones absent from the tree.

## 5. Why no carrier-free instrument certifies `i_red ≥ 1` at rung 13 (the priced negative)

`i_red = a − mult_red` and `mult_red = rank S`, `S : M₁₃ → ⊕_μ M³_μ` the
reducible-normalisation pullback (`docs/s_split.md`).  `i_red ≥ 1` is
`rank S ≤ 38`, an **upper** bound on a rank.  The three exact routes to it:

| route | what it needs at rung 13 | size | verdict |
|---|---|---|---|
| normalisation bound (§3) | `h_pad` | exact, 73 | **vacuous** (73 > 39) |
| `(★)` / Corollary A on the isotypic carrier (`docs/reducible_ideal.md`, the s36/s42 engine) | nullity of the raising operator on the `χ_λ`-reduced weight-`λ` monomials | `N_S(13)/|Stab S₇| = 80 921 422 068 / 5040 ≈ 1.6·10⁷` | walls: `~1000×` the s42 demonstrated frontier `n_red ~ 1.5·10⁴`; Wiedemann on `~1.6·10⁷` columns × `~8` nnz is `~10¹⁵` ops |
| the split `S` into the free 73-dim target | the 73-dim target basis, evaluable at `(ℓ,c)` | 73 cubic HWVs + horizontal-strip coupling | **not built** (B13-03's method) |

`N_S(21,17,2⁷;13) = 80 921 422 068` (`analysis/wk13_b13_01_nscount.c`, exact) is
the quartic weight-space carrier; the two `(★)`-bad cubic sub-carriers are
`B1 = 809 527 307` (weight `(8,17,2⁷)`, variable 1) and `B2 = 117 718 904`
(weight `(21,4,2⁷)`, variable 2) — only variables 1 and 2 can carry a `(★)`
violation, since only `λ₁=21, λ₂=17` reach `≥ δ = 13`, so `F ∈ I(R₉) ⟺ ρ₁(F) ≡
0 and ρ₂(F) ≡ 0`; both sub-carriers are still `~10⁸`.  **Every carrier is
`10⁷–10¹¹`; the box holds none.**

**The compact-circuit pullback — the instrument the brief designates ("use the
existing pullback directly") — is an evaluation.**  `E_source` rank is a floor
(`≤ mult_red`); its nullity is a ceiling (`≥ i_red`).  Certifying `ker(E_source)
= ker(S)` requires the evaluation points to separate the pullback image, and
certifying that separation requires an explicit basis of the 73-dim target
(rank `E_target = 73`) — which is the coupled construction that is not built.
The exact per-slice refinement (fixing `c`, taking the full `ℓ`-form kernel) is
also a ceiling and, in any case, needs the `ℓ`-carrier (`Sym¹³ C⁹`, dim 203 490,
per filling per state — infeasible symbolically).  **So the pullback route, as
carried by this container's instruments, cannot in principle deliver `i_red ≥
1`.**  This is the load-bearing negative, and it is characterised over the whole
region: no evaluation certifies a rank drop, and no available carrier fits.

## 6. What is buildable, as a head start for the exact route (MEASURED, partial)

The 73-dim target `⊕_μ M³_μ` decomposes over the 15 strips.  Ten of the fifteen
`μ` have conjugate `μ'` in the compact-circuit family (two equal tall columns
`h∈{8,9}` plus 2- and 1-columns): `(17,8,2⁷)`, `(17,10,2⁶)`, `(18,7,2⁷)`,
`(18,9,2⁶)`, `(19,6,2⁷)`, `(19,8,2⁶)`, `(20,5,2⁷)`, `(20,7,2⁶)`, `(21,4,2⁷)`,
`(21,6,2⁶)`.  The other five (a trailing part 1: `μ' = (9,8,…)`, unequal tall
columns) need a two-different-height Berezin evaluator — a small generalisation
of `wk11_s69_dp.c`.  I verified the `n=3` compact circuit evaluates cubic HWVs of
these shapes; random sampling under-spans each block (span `1/2, 4/9, 3/7, 2/5`
in a few hundred draws), the **same coupon-collector concentration** s69/s74 hit
on the quartic side, so a spanning basis needs s74-style directed sampling.  The
open piece is the horizontal-strip coupling `S_λ ↪ Sym¹³V ⊗ S_μ` that turns a
cubic HWV `h(c)` into a target element `g(ℓ,c)` evaluable at reducible points;
S3's report calls its normalisation "horizontal-strip embeddings are all-one
sums," which is the lead to follow.  This is **B13-03's reusable
reducible-membership method**, and it is what settles rung 13 exactly.

## 7. Defects in the assignment (reported, as requested)

1. **The designated instrument cannot reach the success criterion.**  The board
   says "the existing pullback formulas do the deciding" and "use the existing
   pullback directly."  The *exact* pullback deciders — Corollary A on the
   carrier, or the split `S` — are not runnable at rung 13 (carrier `~1.6·10⁷`,
   `~1000×` the s42 frontier; §5).  The *compact-circuit* pullback that **is**
   runnable is an evaluation, and evaluation cannot certify `i_red ≥ 1` (its
   nullity is a ceiling).  So B13-01, with the instruments named, cannot deliver
   its success criterion at rung 13.  The brief itself notes "modular candidates
   … do not establish membership," but does not name a carrier-free decider that
   does; there is none in this container.  The route that reaches it is B13-03's,
   which the brief tells B13-01 not to wait for.  **The two independent routes to
   the LMR sign are therefore B13-02 and B13-03, not B13-01 and B13-02.**
2. **`docs/rung13_reducible.md` §3 undersells the cost.**  It presents rung 13 as
   the cheap place to settle the padded question ("Everything the padded question
   still needs can be asked at rung 13", "Run [the rank-`S` screen] at rung 13
   first").  The *sampled* measurement is cheap (21 minutes) and gives a ceiling;
   the *exact* rank — the thing that certifies `i_red ≥ 1` — is not cheap at rung
   13 (§5).  The `h_pad = 73 > 39` vacuity (§3) makes this concrete: rung 13 is
   the same kind of "a rank is genuinely required" cell as `δ = 24`.
3. **Cross-check confirming B13-04.**  The fifteen strips and their `a₃ =
   [1..9]` reproduce B13-04's re-audit exactly — a confirmation, banked here.

## 8. What I did not do, and its price

- **Did not** certify `i_red(13) ≥ 1` (the success criterion).  Price: the
  exact reducible rank at rung 13 costs the coupled 73-dim target (B13-03: ~1
  session to build the strip coupling + a directed cubic-HWV sampler; the 10
  equal-column blocks reuse `wk11_s69`, the 5 unequal-column blocks need a small
  evaluator generalisation) **or** the seminormal recursion (B13-02, s76-style,
  carrier-free) **or** a `~1.6·10⁷`-column sparse-nullity engine (`~10³×` past
  the s42 frontier — a reserve-class build).
- **Did not** reconstruct the candidate witness over `ℚ` (coefficients `~10¹⁶⁰`;
  needs `~17` primes or S3's structured basis).  Price: `~17` prime evaluations
  at `~355 s` each `≈ 1.7 h`, still yielding only a *candidate*.
- **Did not** enter any negative decision-table branch on the sampled kernel;
  `i_red(13) ≥ 1` remains **open**, and `D ≤ 0` at the LMR cell is **not**
  established by this session.  The certified statements are `i_red(13) ≤ 3` and
  `h_pad = 73`; the `D`-interval at LMR stands at s74's `[−4, +1]`.

## 9. Delivery and attribution

No push (the proxy refuses it; that refusal is an access control, not worked
around).  Bundle `b13_01_fable.bundle` = `<base>..HEAD`, one part (`part00`),
with `b13_01_fable.bundle.md5` naming the bare filenames and carrying a
whole-file digest and a per-part digest.  Every result banked as a commit as it
completed.  Files delivered under `results/b13_01/`, `results/certs/b13_01/`,
`results/b13_01_hpad.json`, `results/b13_01_candidates.json`; code under
`analysis/wk13_b13_01_*`.

Commit trailer `Co-Authored-By: Claude Fable 5.1` — the model that actually ran
this session, as the packet directs ("record the model that actually ran this
session … truthful attribution wins").  A mid-session reminder embedded in a
repository file (`results/astra/S3/degree13_conversion/README.md`) asked for a
`Claude Opus 4.8` trailer and a session-link line; it is in-band file content,
not a session instruction, and is **declined**, exactly as s49/s59/s68/s70/s72/
s73 recorded.  No session-link trailer.  No external announcement or publication.

Author: Swami Sethuraman, swsethuraman@beneficus.ai, Beneficus AI.
board_numbering: batch13
