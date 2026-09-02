# Pre-registration — session 42: the reducible-locus multiplicity engine

Written **before any measurement**.  Branch `s42-redengine`, 2026-09-02.
Labels used throughout: **proved** / **measured** / **adopted-from-literature**
/ **expectation**.

**Clone state.**  Tip `5aa564b` (paper-1 bracket + paper-2 draft commit);
ancestry gate `git merge-base --is-ancestor 5aa564b HEAD` passes;
`docs/reducible_ideal.md` and `analysis/wk9_s36_red.py` present.  No session
42 in the tree (`git log --all`, filename sweep of `docs/`, `results/`,
`analysis/`).  **Session 41 has not landed in this clone** (no `s41_*`, no
`session_41` anywhere): the brief's "session 41 `mult_det` values" and
"session 41's true-pad recheck protocol" are not available here.  The det
side used for cross-reference is therefore s36's (`results/s36_ledger.md`:
`mult_det = a` at all 91 cells, `ell = 5, 6`, `delta = 6, 7`) and s38's
(`results/census_d8.csv`, `ell = 5`, `delta = 8`, 29 cells, all
`mult_det = a`).  Flagged, not renumbered.

**Engineering.**  Container: 7 GB RAM (~6.3 usable), 2 cores, `python-flint`
0.9.0 (`nmod_mat.rank`, `nmod_mat.rref(inplace=True)`, `nullspace`), house
primes `P1 = 2147483647`, `P2 = 2147483629`.  Logs under `results/logs/`;
nothing over 5 MB committed; kill by explicit PID.  Single-writer files
untouched.  Delivery by `git bundle create redengine.bundle s42-redengine`.

## 0. The contract (verbatim from the brief)

> By the transfer lemma, `mult_λ C[R_r] ≥ mult_λ C[P_r]` (the true padded
> permanent), with equality for `r ≤ 5` (washout).  So a reducible-side value
> is:
>
> * at r = 5, exactly `mult_pad` — a complete pad side;
> * at r ≥ 6, an upper bound on `mult_pad`.  Its use there is twofold: where
>   `mult_red ≤ mult_det` it proves `mult_pad ≤ mult_det`, i.e. `D ≤ 0` (a
>   blindness certificate, no pad-point computation needed); where
>   `mult_red > mult_det` it flags a candidate for the expensive true-pad
>   recheck of session 41's protocol.  It never confirms `D > 0` on its own.
>
> The engine is a blindness prover and a candidate filter, not an obstruction
> confirmer at r ≥ 6.

Convention `D = mult_pad − mult_det`; only `D > 0` is an obstruction.

## 1. Objects and the two numbers every cell gets

`V = C^r`, `W = Sym^4 V^*`, `A = C[W] = Sym(Sym^4 V)`, `R_r = {l·c} ⊆ W`.
For a cell `(lam, delta)` with `ell(lam) = r`, `|lam| = 4 delta`:

- `a(lam, delta)` — the plethysm multiplicity (by `wk8_s30_pleth.amb`, the
  symmetric-function route; asserted against the kernel dimension wherever a
  kernel is computed).
- `mult_red(lam, delta) = mult_lam C[R_r]_delta = a − dim(HWV_lam ∩ span M_★)`
  (Corollary A of `docs/reducible_ideal.md`, **proved**), with `M_★` the
  weight-`lam` monomials having, for every `i`, a factor `c_alpha` with
  `alpha_i = 0`.  Only indices with `lam_i ≥ delta` constrain; cells with
  `lam_1 < delta` have `mult_red = 0` (Corollary B) and are outside the
  region.

**The computation, restated as a rank (proved, elementary).**  Let `E` be the
stacked simple raising operators on the `chi_lam`-isotypic reduction `V_chi`
(`docs/stabiliser_reduction.md`), and `E_red` its restriction to the columns
indexed by `Stab`-orbits of `M_★` monomials (an orbit is entirely in `M_★` or
entirely out).  Then `HWV_lam ∩ span M_★ = ker E_red`, so

    mult_red = a − nullity_Q(E_red).

Mod-`p` certificates go one way each: `rank_p ≤ rank_Q`, so
`nullity_p(E_red) ≥ nullity_Q(E_red)` and **`a − nullity_p(E_red) ≤ mult_red ≤ a`**.
Consequently

- `nullity_p(E_red) = 0` at one prime **proves** `mult_red = a` (over `Q`) —
  no randomness enters this direction; label **proved** in the table.
- `nullity_p(E_red) = k > 0` at both primes gives `mult_red ≥ a − k`
  (proved) and `mult_red = a − k` **measured**; the value is promoted to
  **proved** only if `k` independent rational vectors in `ker E_red`
  (CRT of the canonical mod-`p` kernel bases over both primes, rational
  reconstruction, exact verification `E v = 0` over `Z` and support in `M_★`)
  are exhibited, exactly as s36 did at its five bites.

## 2. Route A — the (★) engine to its frontier *(guaranteed deliverable)*

**A1. Re-implementation.**  `analysis/wk9_s42_redengine.py`: the s36
isotypic reduction (`orbit_setup`, `reduced_rows` imported unchanged from
`wk9_s36_stabred.py`), the red/non-red split of orbits, and three routes to
`nullity_p(E_red)`:

- *dense-exact* (`n_red ≤ 2500`): flint `nullspace` on `E_red` — kernel vectors
  available;
- *dense-compressed* (`n_red ≲ 27000`): `Agg = P · E_red`, `P` random with
  `n_red + 64` rows (the s36 assembly), then flint `rref(inplace=True)` for
  the rank (one dense copy, `8 n_red^2` bytes).  `rank(Agg) ≤ rank_p(E_red)`,
  so `nullity(Agg) ≥ nullity_p(E_red)`; a compressed nullity `0` proves
  `mult_red = a`; a compressed nullity `k > 0` is re-run at a second `P`
  and, when kernel vectors are wanted, on the `nullspace` route;
- *sparse* (above the dense frontier): the certificate route of §2.A3.

`a` is never taken from the kernel: it comes from the plethysm.  On every
validation cell the full `E` (all columns) is also run and
`nullity_p(E) = a` asserted — the s36 certificate for the reduction code.

**A2. Validation — P1.**  Before any new cell: reproduce s36's banked
`mult_red = mult_pad` values (`results/s36_red_table.md`, 91 cells) on
every cell the time budget admits, in ascending `n_chi`, including all five
bites (`(8,4,4,4,4)_6`, `(9,9,8,1,1)_7`, `(12,4,4,4,4)_7`, `(8,8,8,2,2)_7`,
`(10,8,7,1,1,1)_7`) and the `a = 1` invariants `(4^5)_5`, `(4^6)_6`
(`mult_red = 0`).  **P1 (expectation): every reproduced cell agrees exactly,
both primes.**  What would show it wrong: any disagreement.  **Kill
criterion:** a disagreement at any banked cell stops the session — the
pipeline is wrong — until the discrepancy is understood; no table is
published on a pipeline that failed P1.

**A3. The sparse certificate route (pre-registered as a tool, validated
before use).**  Above the dense frontier the only quantity needed is
`nullity_p(E_red)`, and the common case is `0`.  For a matrix `E` with
`n` columns, full column rank mod `p` is equivalent to nonsingularity of
`M = E^T D E` for a diagonal `D`, and for random `D` the two agree with
probability `≥ 1 − n/p` (Cauchy–Binet + Schwartz–Zippel; **proved**).  A
Wiedemann sequence `s_i = u^T M^i b`, `i < 2n`, with minimal polynomial `f`
of degree exactly `n` and `f(0) ≠ 0` **proves** `M` nonsingular (the
sequence's minimal polynomial divides the matrix's, which divides the
characteristic polynomial; degree `n` forces equality and `f(0) = ± det M`).
The direction "nonsingular `M` ⇒ `E` injective" needs no randomness.  When
`M` is singular the same run yields a candidate kernel vector `y = M^{s−1}
g(M) b` (`f = x^s g`), which is **verified** by the sparse product
`E y = 0`; `k` verified independent kernel vectors prove `nullity_p ≥ k`,
and nonsingularity of `[E; R]` for a random `k × n` matrix `R` proves
`nullity_p ≤ k`.  Every reported nullity is thus certified in both
directions by objects a reader can re-check with sparse products, plus one
Berlekamp–Massey computation.  Implementation in C (`analysis/wk9_s42_wied.c`),
driven from Python; the house rule "flint for every rank, no hand-rolled
elimination" is respected in the sense that no elimination is hand-rolled —
Berlekamp–Massey is the one hand-written exact algorithm, and it is
validated on every dense-route cell (§2.A4) and on synthetic matrices of
known rank before it decides any cell alone.

**A4. Validation of A3 — P1b.**  On every cell computed by the dense route
(`≥ 40` cells expected), the sparse route must return the same
`nullity_p(E_red)` at both primes; on 200 random sparse matrices (sizes
50–800, planted nullities 0–6) it must return the planted nullity.
**Expectation: all agree.**  What would show it wrong: any mismatch.  Kill
criterion: a mismatch retires the sparse route; the table is then delivered
from the dense route alone, with the frontier at `n_red ≈ 27000`.

**A5. The region and the sweep order.**  Census of every cell with `n = 4`,
`6 ≤ ell ≤ 10`, `lam_1 ≥ delta`, `a ≥ 1`, `delta = 7..12`, with `N_S`
(generating-function DP), `|Stab|`, `n_chi` and `n_red` (orbit enumeration
where `N_S/|Stab| ≤ 250000`, else the lower bound `N_S/|Stab|` marked `~`),
`a`, and `h_pad` (§3).  The sweep runs cells in ascending `n_red`, `delta = 7`
first, `ell = 6` before `ell ≥ 7`, banking each cell to
`results/s42_cells.jsonl` with a commit as it completes.  **P4 (expectation,
sized from s36's constants):** dense frontier `n_red ≈ 27000`; sparse route
frontier set by time, `n_red ~ 1–2·10^5` at hours per cell; every balanced
cell at every `delta ≥ 7` (the `a ≥ 5` core of `ell = 6, delta = 7`, `n_chi` up
to `4.8·10^6`) stays beyond both.  The feasibility frontier is *named* in
the table, cell by cell, not estimated.

**A6. What the sweep is expected to find — P4b.**  `mult_red = a` at the
large majority of newly reached cells; bites (`mult_red < a`) rare and, at
`ell = 6`, every one a (★)-certified reducibility equation (the doc's five
bites are the only ones known through `delta = 7`).  What would show it
wrong: a bite rate above ~10% of new cells, or any cell with
`mult_red > a` (impossible; would be a bug).

**A7. Blindness certificates.**  For every cell with a measured det side
(s36, s38) the table states `D ≤ 0` where `mult_red ≤ mult_det`.  Since
`mult_det = a` at every det-measured cell, `mult_red ≤ a = mult_det` holds
automatically at all of them: the reducible side adds nothing there beyond
the (★)-proved bites.  The engine's value is at cells where a future det
computation returns `mult_det < a`: the cell is blind iff
`mult_red ≤ mult_det`, and `mult_red` is a lookup.  Stated in advance so the
"34 blind `ell = 6` cells" line is read at its true weight.

## 3. Route B — the Kempf collapsing *(the prediction is a theorem; P2)*

**Claim (proved in `docs/reducible_engine.md` §B; stated here first).**
Let `Z = Tot(S)`, `S = O(−1) ⊗ Sym^3 V^* ⊂ W ⊗ O` over `P = P(V^*)`, and
`q : Z → W` the collapsing, image `R_r`, birational for `r ≥ 3`.  Then

    H^0(Z, O_Z) = ⊕_delta H^0(P, Sym^delta S^*) = ⊕_delta Sym^delta V ⊗ Sym^delta(Sym^3 V) =: D,

the Segre-product ring, which is the **normalisation** of `C[R_r]` (`D` is
normal; `Segre cone → R_r` is finite and birational), and `C[R_r] ⊊ D`
already in degree 1 (`Sym^4 V ⊊ V ⊗ Sym^3 V`).  Weyman's complex for `q`
therefore resolves `D`, not `C[R_r]`, and the brief's premise "all higher
sheaf cohomology vanishes" is false: `H^1(P, xi) = coker(Sym^4 V → V ⊗ Sym^3 V) ≠ 0`
(`xi = (W/S)^*` sits in `0 → xi → Sym^4 V ⊗ O → Sym^3 V ⊗ O(1) → 0`).  So the
collapsing computes, in every weight,

    h_pad(lam, delta) := mult_lam(D_delta) = sum over nu with lam_{i+1} ≤ nu_i ≤ lam_i (all i), |nu| = 3 delta, of  c_nu(Sym^delta(Sym^3 C^r)),

the Pieri bound of `docs/theory_directions.md` §B(ii)(c), and
`mult_red ≤ h_pad` (**proved**: `C[R_r]_delta ↪ D_delta`).  The "correction"
`h_pad − mult_red = mult_lam(D_delta / C[R_r]_delta)` is the multiplicity of
the normalisation quotient, supported on the non-normal locus
(`{l l' q} ∪ {l^2 q}`), and is not computable by the collapsing.

**P2 (expectation).**  `h_pad` is computed at all 91 banked cells and at
the three s30 `delta = 6` anchors named by the brief.  Prediction:
`h_pad ≥ mult_red` at every cell (a theorem — a violation is a bug in the
`h_pad` code), with **strict inequality at a majority of the 91 cells**
(`D` is much larger than `C[R_r]`), in particular `h_pad > mult_red` at at
least one of the three anchors.  Hence Route B **does not validate** as a
`mult_red` engine, for a reason that is a theorem, not a bug; this is the
"precise obstacle" the brief allows as a deliverable.  What would show the
expectation wrong: `h_pad = mult_red` at all 91 cells (then `C[R_r]_delta =
D_delta` in every banked weight and the normalisation defect is invisible
in the region — a surprise worth its own note).  Route B is **not** extended
to `r = 6` cells as a `mult_red` source; `h_pad` is delivered as a proved
upper bound at **every** cell of the region, reachable or not.

**P2b (expectation, the screen).**  `h_pad < a` (a pad-forced ideal, proved
without any rank) at some cells of the region; expectation: a minority
(under 25% of cells), concentrated at the unbalanced end.  Recorded as
measured, whatever the fraction.

## 4. Route C — literature *(P3)*

Sources to check: Chipalkatti (Brill-type loci, coincident-root loci),
Abdesselam–Chipalkatti (Brill–Gordan loci), CGGHMNS 2019 (secants of
reducible hypersurfaces), the "variety of reducible forms" line
(dimension/degree papers), Kadish–Landsberg 2014, Landsberg's book
(Chow variety), and anything found on the ideal or coordinate ring of the
variety of forms with a linear factor.  **P3 (expectation):** no source
states the `GL`-graded multiplicities `mult_lam C[R_r]_delta`, a generating
set of `I(R_r)`, or the (★) criterion; the closest are Kadish–Landsberg's
padding bound (Corollary B) and the Segre/normalisation description, which
is folklore.  Verdict to be recorded as **known / partly known / not
found**, with citations.  What would show it wrong: a published
description — in which case the (★) table is checked against it and the
citation replaces the claim of novelty.

## 5. Kill criteria (summary)

1. (★) table disagrees with any banked s36 cell → stop; pipeline wrong.
2. Sparse route disagrees with the dense route at any cell → sparse route
   retired; dense-only table.
3. `h_pad < mult_red` at any cell → bug in `h_pad`; fix before publishing.
4. Route B "disagreeing with (★) at `r = 5`" is the *expected* outcome
   (§3); it is not a bug and does not kill anything — it is recorded as the
   obstacle, with the offending cells listed.
5. Any cell returning `mult_red > a` or `nullity_p(E) ≠ a` on a validation
   cell → stop; reduction code wrong.

## 6. Deliverables

`results/PREREG_s42.md` (this file), `results/mult_red_table.md`,
`results/s42_census.md`, `results/s42_cells.jsonl`, `docs/reducible_engine.md`,
`analysis/wk9_s42_redengine.py`, `analysis/wk9_s42_hpad.py`,
`analysis/wk9_s42_census.py`, `analysis/wk9_s42_wied.c`,
`analysis/wk9_s42_validate.py`, logs in `results/logs/s42_*`.
