# Batch 14 strategy — Claude: exact feasibility and reuse of banked work

**Baseline.** All claims are made against commit `7a47e2b`. `main` has since moved to `7e69506`, which records the A1 pass. Two capability facts below are quoted from it and are flagged *post-baseline*. No mathematical claim depends on it.

**Labels.** PROVED, CERTIFIED, ADOPTED as in `PROVED.md`; MEASURED = sampled; EXACT-here = a bounded exact computation run in this session (scratch, uncommitted, one implementation unless stated).

**Scope.** No avenue forms a modular product with inner dimension n_χ or needs an N_S-sized certificate, and all inputs are at the baseline (the missing s76 DAG and S3 per-node files are not needed).

## 0. Where an obstruction could be hiding

**Below degree 24, the determinant has no equations wherever it has been measured, so D ≤ 0 there.** LMR's family — the only known family of separating equations — is provably empty at eight rows or fewer (`lmr_cell.md` §1), and all 682 measured six-row cells are certified full rank. One gap remains: seven- and eight-row quartic cells have never been measured on the determinant side.

**So the only known source of equations puts candidates at nine or ten rows, in degree ≥ 24.** That region is the neighbourhood of the LMR line f and whatever f generates.

**That neighbourhood is weaker than the roadmap assumes, and this can be proved.** The five sampled padded relations at LMR are reducible relations, born at rungs 13–14. Multiplication by a fixed highest-weight vector is injective on each ideal. So every genuine padded relation reaches every Cartan product of the cell intact, including both B13-06 targets. At those targets the determinant gains only one transported equation, plus whatever the product image adds.

If the five relations are genuine, D > 0 near LMR requires one of three things:

- at a single-channel target, a transport that kills the padded relations but not f;
- at a multi-channel target, a product image of f of *higher rank* than the transported padded image;
- a determinant equation that LMR does not generate.

**Everything therefore turns on one number: i_red at rung 13, then at rung 14.** Sampled evaluation cannot certify it. Evaluation combined with a *certified uniqueness set for the 73-dimensional normalisation target* can. Every ingredient except that target basis is already banked.

**Top recommendation: settle this number.** The expected outcome is D ≤ 0 at LMR; once certified, later judgements about the neighbourhood become exact rather than sampled — and if the rung-13 relations are not genuine, LMR itself reopens.

## 1. Three lemmas and new exact numbers

**Lemma T (transport; PROVED).** This is s57's Lemma L argument, with any highest-weight vector w ∈ A_k of weight μ in place of u.

- Multiplication by w maps I(X) ∩ M_{λ,δ} injectively into I(X) ∩ M_{λ+μ,δ+k}, for X = D, P, R. No projection is involved.
- Hence i_X(λ+μ) ≥ i_X(λ). If also w ∉ I(X), then mult_X(λ+μ) ≥ mult_X(λ).
- Applied with w = q₆₂ and w = q₄₄: both B13-06 targets have i_pad ≥ i_pad(24). Every genuine LMR relation survives there — not "three of five".

**Lemma B (birth bound; s57 Lemma L, restated).** Along a u-ladder, i_X(δ+1) ≤ i_X(δ) + (a_{δ+1} − a_δ).

**Lemma CI.** Stated under Avenue 1.

**EXACT-here computations.**

| Quantity | Value | Route |
|---|---|---|
| (19,2⁷) ladder, a at δ = 24, 25 | 390, 391 | house `a_weyl`; the value 392 at δ = 26 is banked |
| a_∞(19,2⁷) | 392 | own stable-slice code |
| (21,2⁷) ladder, a at δ = 27 | 532 | house `a_weyl`; the value 531 at δ = 26 is banked |
| a_∞(21,2⁷) | 533 | own stable-slice code |
| LMR tail (17,2⁷): a_∞, h_∞ | 274, 521 | own code; both match banked values |
| Raw stable weight space at LMR | 7.21×10⁹ | own count; agrees with s57's ≈1.4×10⁶ orbit classes |
| h_pad((25,17,2⁷), 14) | 159 | B13-01's counter with the degree generalised; it reproduces 73 at rung 13 |

So (71,19,2⁷)₂₆ is a stable cell, while (69,21,2⁷)₂₆ is not (531 < 533).

**Consequence (PROVED, given the table).**

1. u does not divide q₆₂ = 8c₀c₂ − 3c₁².
2. u does not divide f either: otherwise f/u would be a determinant equation at δ = 23, contradicting the certified full rank there.
3. So q₆₂f spans the single birth at δ = 26 on the (19,2⁷) ladder.
4. Hence i_det(71,19,2⁷; 26) = i_det(67,19,2⁷; 25) + 1 ≤ i_det(63,19,2⁷; 24) + 2.
5. If i_pad(24) = 5, then D > 0 at B13-06's best target needs **four** determinant equations at the degree-24 weight (63,19,2⁷). No known module lives there.

## 2. Ranked avenues

### Avenue 1 — Settle LMR by complete interpolation (rung 13, then rung 14)

**Target.**

- λ₁₃ = (21,17,2⁷), with the complete 39-dimensional source in `results/s74/source.json`.
- Then λ₁₄ = (25,17,2⁷), with a 93-dimensional source.

**Mechanism — Lemma CI (PROVED here).** Let N = HWV_λ(C[V ⊕ Sym³V]_{(δ,δ)}), with h = dim N. The load-bearing input is h = h_pad: 73 at rung 13, 159 at rung 14.

1. The pullback F ↦ F(ℓ·c) maps M_λ into N, with kernel I(R) ∩ M_λ (B13-03 §1; S4).
2. Suppose g₁,…,g_h ∈ N have a nonzero h-minor at points (ℓ_k, c_k). Then evaluation at those points is injective on N.
3. Hence F ∈ I(R) exactly when every F(ℓ_k c_k) is 0.
4. Therefore i_red = a − rank_Q[F_i(ℓ_k c_k)].

Both halves are certified:

- the target half by a modular h-minor, which is a rank floor;
- the source half by an exact integer matrix and its exact rational kernel.

This is the complete-interpolation exception that qualification 5 allows. `PROVED.md` already admits "a carrier or a coupled target", and B13-01 §5 named this separation step; that entry's absolute wording should be amended.

**What the certificates decide.**

| Certified outcome | Consequence |
|---|---|
| i_red(13) ≥ 1 | i_pad(24) ≥ 1 (via u¹¹ and Lemma L), so **D ≤ 0** |
| i_red(14) = 5 (the sampled value) | With the certified floor of 269: i_pad(24) = 5, so **D = −4 exactly** |
| i_red(14) < 5 | i_pad(24) ∈ [i_red(14), 5] stays open, because sampled supports do not lift (`eps_pad_inference_dead`) |

**What is reused.** The s74 source; the compact evaluator `wk12_s74_dpc.c`; B13-01's reducible points; h_pad = 73 (B13-01; reconciled by B13-04 and the integrator's audit); the pullback-kernel theorem; Lemma L.

**The one missing interface.** A bracket evaluator with two letter types — ℓ (valence 1) and c (valence 3) — on the column shape (9,9,2¹⁵,1⁴). That shape is already in the evaluator's class.

Mixed brackets lie in N because every column is an initial minor (the evaluator must compute the symmetrised polynomial, as s69's does); the rank certificate proves they span N. This **replaces** C2's strip coupling: no Pieri coefficients are needed.

**Classification.** Engineering (the evaluator); bounded exact computation (spanning search, CRT source values from a derived height bound, one 39-column nullspace); one short lemma; no open research.

**Decisive experiment.** Pre-register a seeded set P13 of 96 reducible points with u ≠ 0, so that the two transported rung-12 rows are not trivially zero. Use one row convention on both sides.

1. Logic check on B13-03's exact (8,8,8)₆ control (h = 1): accept F₀, reject F₁ (value 729). Use expanded polynomials, since (3⁸) is outside the evaluator's class.
2. Evaluator check against exact expansion on small in-class shapes.
3. A nonzero 73-minor at P13, at both primes.
4. The exact source matrix and its nullspace. Steps 3 and 4 can run in parallel sessions sharing the seed.

**Criteria.** *Success:* a certified i_red(13). *Control that can fail:* at 20 extra points the source rows must lie in the target row space. *Kill (budget only):* rank below 73 after the pre-registered draws plus one deterministic semistandard pass. *Fallback:* deliver the evaluator, the partial rank and the exact source matrix.

**Resources.** gcc and python-flint (present Claude-side, flint confirmed by the post-baseline A1; absent on the Astra host). Source evaluation is measured at about 0.2 s per row per point (`rung13_reducible.md`) — about 13 minutes per prime — times the number of CRT primes the height bound requires. The spanning search is **UNCERTAIN**: s74 needed 1,500 draws for 37 rung-13 births.

**Why this beats B1.** By Lemma T, B1's thresholds (391, 529) matter only if i_pad(24) ≤ 1 (respectively ≤ 2). Avenue 1 gives an exact lower bound on i_pad(24), and fixes it if i_red(14) = 5. B1 can do neither.

### Avenue 2 — Transport census of the LMR product region

**Target.** B13-06's 239 components with at most ten rows: 31 at δ = 25 and 208 at δ = 26.

- EXACT-here: single-vector Cartan products of the rung-13/14 relations reach only 4 of the 30 non-ladder components at δ = 25, and 23 of the 205 non-Cartan components at δ = 26.
- Start with the 16 ten-row components at δ = 25. No Cartan product from a nine-row source reaches any of them.

**Mechanism.** D(ν) > 0 needs dim I(D)_ν > dim I(P)_ν. The known part of I(D)_ν is the image of the LMR module; I(P)_ν contains the images of the rung-13/14 relations. At a single-channel target both pass through one map Φ_ν, and a nominee needs U_P ⊆ ker Φ_ν but f ∉ ker Φ_ν. At a multi-channel target (up to 10 channels at δ = 26), compare the total ranks of the f-images and the padded images. These ranks must be computed; tensor multiplicities do not determine them.

**What is reused.** B13-06's exact channel census; s74's U_D and U_P (sampled now, exact after Avenue 1); Lemma T; the compact evaluator.

**What is missing: bracket adjunction.** For a horizontal strip ν/λ, adjoining one letter in the strip boxes should give F_{T′} = Φ_ν(F_T).

Two binary hand checks agree (u ↦ (8c₀c₂ − 3c₁²)/24; the (6,2) covariant ↦ the catalecticant), but both land in one-dimensional spaces and could not have failed. Adjunction needs a general proof and a validation where both spaces have dimension ≥ 2 (s62/s73's exact n = 3 determinant vector); the evaluator also needs height-3 columns and unequal tall columns (10,9).

*Classification:* a small new theorem, engineering, and rank computations on images of dimension at most 6 per channel.

**Decisive experiment.** Validate adjunction. Then run the 30 components at δ = 25 on U_D ⊕ U_P, at one prime and 10 points each.

**Criteria.**

- **Success:** a nominee.
- **Kill:** at every target where the f-image survives, a padded image of at least equal rank survives too. Given Avenue 1, degree 25 is then closed except to determinant equations that LMR does not generate.
- **Fallback:** the combinatorial half for all 239 components — reachability, Lemma T exclusions, Lemma B bounds.

**Resources.** gcc and flint; about 274 bracket evaluations per point. Total cost is **UNCERTAIN** until the new shapes exist.

**Why this beats one full measurement at a Cartan target.** Lemma T predicts that such a target loses whenever the relations are genuine.

### Avenue 3 — A determinant-side instrument at nine and ten rows: the stable slice

**Target rule.** Stable tails of weight 31–35 with eight or nine parts, in this order:

1. (19,2⁷);
2. Avenue 2's nominees;
3. tails not containing (17,2⁷), which LMR cannot reach.

**Mechanism.** Proposition S (s57; audited by B13-07) localises at u, so every cell at or above its closing degree becomes a GL₈/GL₉ covariant question: the determinant is the characteristic-polynomial image of traceless pencils, the reducible locus is {Q₄ = aQ₃ − a²Q₂ − a⁴}, and the padded locus is explicit. One stable measurement decides every rung from the closing degree upward. Once transports are closed, a determinant equation that LMR does not generate is the only remaining route to D > 0, and this is the cheapest place to look for one.

**What is reused.** Proposition S; s79's verified stable instrument (hard-wired to five tail variables); the traceless-pencil point map; s57's slice sizing. Explicit kernels are out of reach: the raw spaces are 7.2×10⁹ at LMR and 8.0×10⁸ at (9,2⁷).

**What is missing.** A stable bracket evaluator: two height-8 columns plus singletons, with no 2-columns and no u-tower, and letters Q₂, Q₃, Q₄ of valence 2, 3, 4.

*Classification:* engineering on a proved reformulation, applied to an empirical question.

**Decisive experiment.**

1. Reproduce ranks 274/273/269 at the LMR tail. This shares no code with s69/s74.
2. Measure the determinant rank on (19,2⁷).

**Criteria.**

- **Success:** a certified determinant floor on (19,2⁷). A floor of 392 − p closes B13-06's best target, where p is the certified lower bound on i_pad(24) (389 after rung 13; 387 once rung 14 certifies 5). The LMR module supplies at most 2 equations there, so a sampled nullity above 2 would nominate new determinant equations for exact proof.
- **Kill:** the reproduction fails.
- **Fallback:** the s74 route at (63,19,2⁷)₂₄. There q₆₂·M₂₂ gives 272 directions free and 118 are new; with Lemma B, this bounds the same ladder.

**Resources.** gcc and flint; new code; cost **UNCERTAIN**.

**Why this beats the alternatives.** Cubic sweeps can only lower D, and (12,4⁵)₈ is a six-row cell outside every known family.

## 3. SPECULATIVE — a padding-penalty theorem

**Conjecture.** On the ladder of any LMR weight Ω(k,d), the reducible relations born on the low rungs at least match the determinant's contribution at the closing cell. The sampled evidence here: 3 relations at rung 13, against 1 equation at rung 24.

If true, degenerate-dual equations never yield a *padded* multiplicity obstruction — a no-go for the only separating family we have. **Route:** in the stable slice the rung-13 relations are low-degree SL₈-covariants vanishing on {Q₄ = aQ₃ − a²Q₂ − a⁴}; seek closed forms from Avenue 1's exact vectors by the symbolic method, then test small (k,d). A proof redirects the programme away from LMR; a counterexample says where to look.

## 4. Two activities to stop

1. **The cubic-ideal sweeps** (99 degree-9 cells, 58 degree-10 cells, the 15 degree-13 predecessors). A permanent-specific equation raises i_pad, so an objective-2 hit can only lower D; the sweeps never gated objective 1, and the LMR transfer is handled by Avenue 1.
2. **B1 as specified, and C1 as a conversion project.** B1's thresholds are moot unless i_pad(24) ≤ 1 (or ≤ 2), and its second target is not stable. C1's purpose is met at rungs 13–14; B13-02 priced exhaustive extraction at 156–2,811 serial years.

## 5. Strongest objection to Avenue 1

**The objection.** Avenue 1 spends the top slot on a probable negative, closing the only cell with an established determinant equation. Its decisive step is a spanning search. The last one took 1,500 draws for 37 births; this one needs 73 directions with a new letter type, and it could stall and yield only an evaluator.

**Reply.** The negative is cheap, gates every target near LMR through Lemma T, and its artifacts make Avenues 2–3 exact. Semistandard fillings span by theorem, so a deterministic pass bounds any stall, and the exact source matrix is useful on its own.

**One remaining single-method input: dim N = 73.** Every confirmation of it uses Weyl alternation. Slot 04 must recount it by a *different method* — for example, plethysm by character inner products — before anything is certified.

## 6. Twelve-session allocation

**Hosts, by measured capability:** *gcc+flint* = C compiler plus python-flint (present Claude-side; absent on the Astra host, where installs fail with WinError 10013); *stdlib* = Python and numpy.

Slots 01–06 and 11 start together; none of them waits on another.

| # | Job | Av. | Host | Starts | Releasing artifact | Fallback |
|---|---|---|---|---|---|---|
| 01 | Mixed-letter evaluator; controls; 73-minor at P13 | 1 | gcc+flint | wave 1 | `target13` + evaluator commit | partial rank |
| 02 | Exact source matrix at P13; nullspace | 1 | gcc+flint | wave 1 (shared seed) | `source13_exact` | — |
| 03 | Lemma CI write-up; adjunction proof and validation; closure table | 1–2 | stdlib | wave 1 | `docs/b14_transport.md` | — |
| 04 | Second-method recounts (73, 159, ladders, a_∞, h_∞) | 1–3 | stdlib | wave 1 | `recounts.json` | — |
| 05 | `complete_interpolation` certificate kind; independent verifier | 1 | any | wave 1 | verifier commit | — |
| 06 | Stable bracket evaluator; reproduce 274/273/269 | 3 | gcc+flint | wave 1 | reproduction record | s74 route at (63,19,2⁷)₂₄ |
| 07 | Rung 14 (target 159, source 93) | 1 | gcc+flint | after 01 + 02 | `target14`, `source14_exact` | source half only |
| 08 | Transport census, δ = 25 then 26 | 2 | gcc+flint | after 03 + 01's shapes | nominee list | combinatorial half |
| 09 | Big-integer replay of the rung-13 certificate | 1 | stdlib | after 01, 02, 05 | verification record | run 04 |
| 10 | Determinant rank on (19,2⁷) or an 08 nominee; reserve for any D > 0 | 2–3 | gcc+flint | after 06 or 08 | ranks + certificates | s74 route at (63,19,2⁷)₂₄ |
| 11 | Speculative: closed-form rung-13 covariants | spec. | any | wave 1 | note | — |
| 12 | Integrator: merge, PROVED.md, A1 acceptance, stock-take | — | — | continuous | — | — |

## 7. Previous roadmap: retain, narrow, abandon

| Item | Verdict | Reason |
|---|---|---|
| A1 | Retain; done post-baseline | Accept after review, and adopt its corrected memory figure of 1.00–1.89×. |
| A2 | Narrow | Only the artifacts the new certificates need. |
| A3 | Abandon for now | Objective 2 can only lower D. |
| A4 | Abandon | Six-row cell; no known family lives there. |
| B1 | Fold into slot 08 | Dominated by i_pad(24), via Lemma T. |
| B2 | Retain, sharpened | Now bounded, via Lemma CI. |
| B3 | Abandon | It would decide ε_pad, not D. |
| C1 | Not a prerequisite | If ever needed, Lemma CI at δ = 24. |
| C2 | Retain, redefined | Mixed brackets; no Pieri coefficients. |
| C3 | Narrow | Complete-interpolation kind first. |
| D1, D2 | Park | No bearing on D > 0 in range. |

**Research disguised as implementation** in the previous roadmap: C1 as a coefficient export, and D1's global elimination. Both are dropped or parked above.

**Compact conversions: milestone versus completion.**

| Conversion | Milestone | Completion |
|---|---|---|
| Degree 13 (73) | Both controls pass, and the rank climbs at P13 | A nonzero 73-minor at the pre-registered P13 at both primes, with the row-space control passing |
| Degree 24 (521) | A matched coefficient only; B13-02 already has 1,127 | 521 certified-independent (ℓ,c)-brackets plus an exact 274-column source matrix at the same points; unneeded if rung 14 succeeds |

## References (baseline paths)

**Documents**

- `docs/PROVED.md`
- `docs/stocktake_batch13.md` §§4–5, 8
- `docs/b13_01_report.md` §§3, 5
- `docs/b13_02_report.md`
- `docs/b13_03_report.md` §§1–3
- `docs/b13_04_report.md` (Prop. C)
- `docs/b13_06_report.md`
- `docs/b13_07_report.md`
- `docs/lmr_cell.md` §§1, 6–7
- `docs/rung13_reducible.md`
- `docs/s57_report.md` (Lemma L, Prop. S)
- `docs/s74_report.md`

**Data and code**

- `results/s74/`
- `results/b13_06/components.json`
- `analysis/wk12_s74_dpc.c`
- `analysis/wk12_s79_stable.py`
- `analysis/wk9_s42_census.py`
- `analysis/wk13_b13_01_hpad.py` and `analysis/wk13_b13_01_mcount.c`

**Post-baseline:** `results/b14_a1/report.md`.

**This session's scratch computations**

- A stable raw-space counter with Weyl alternation, calibrated to s79's raw sizes (5 of 5) and to a_∞ = 4 at two s79 blocks.
- House `a_weyl` runs at four nine-row cells.
- A degree-general copy of `mcount.c`.
- An adversarial audit by a subagent: no algebraic errors; its twelve scope and label corrections are folded in.
