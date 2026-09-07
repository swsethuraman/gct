# Session 64 — the padded side, measured on the same source multiplicity space as the determinant

Branch `s64-padded` off `main` at `226b4ef1` (ancestry gate passed). Labels:
**proved** / **measured** / **adopted** / **expectation**. Pre-registration
`results/PREREG_s64.md` committed before the calibration sweep. Two integrator
notes arrived mid-session; their findings are folded in below and attributed.

## 0. Verdict

`mult_pad` is measurable on the **same** `chi_lam`-isotypic source space, the same
raising operators `E`, and the same dense highest-weight kernel that the
determinant and reducible sides already use. The kernels themselves — not merely
their dimensions — are comparable in the shared `M_lam` coordinates.

    mult_det = a − nullity_Q [E; ev_det],   ev_det at det_4 pencils
    mult_red = a − nullity_Q [E; ev_red],   ev_red at l·(generic cubic)
    mult_pad = a − nullity_Q [E; ev_pad],   ev_pad at l(s)·per_3(A(s))    (the padded permanent)

**48 calibration cells, all PASS; 12 discriminating** (`mult_pad = mult_red <
mult_det`). At every `r ≤ 5` cell `mult_pad = mult_red` exactly (both primes),
matching the session-60 banked record, including all eight `r = 5` discriminating
cells and the `r = 3` onset cell `(8,8,8)_6`; the containment
`mult_pad ≤ mult_red ≤ mult_det` holds everywhere, and `mult_pad ≤ mult_red ≤
h_pad` (the proved chain) holds at every cell with `h_pad` matching the banked
session-42 value. Because `P_r = R_r` at `r ≤ 5` makes the padded and reducible
sides agree by theorem, an **r ≥ 6 separation test** was added (integrator note
2): the variety `ev_pad` samples has dimension `55 < 61 = dim R_6`, so the engine
provably measures the padded side, not the reducible side. The degeneracy-direction
pre-check on the full ten-variable `l·per_3` reproduces the known wrong-direction
result for the Macaulay statistic, confirming why the (functorial) multiplicity
route is the one used. Kernel bases are preserved for session 65. **No LMR cell
was attempted; calibration is the deliverable.**

## 1. The architecture reading, confirmed (Task 1)

The batch plan gated C3 on a Sol derivation of a compact equivariant padded
model. **That gate is unnecessary: the model and the padded evaluation family
were already in the repository.** Confirmed in the first hour:

- **(A1) `E` carries over — by construction.** `E` depends only on `(lam, delta,
  r)`, never on the evaluation family. `wk10_s64_cell` reads **one** dense kernel
  of `E` per prime and forms three point matrices against it, so det, red and pad
  share the identical kernel and coordinates.
- **(A2) The padded points are in the right ambient — verified.**
  `restrict(PAD34, 10, 4, r, V) = l(s)·per_3(A(s))`, `PAD34 = per_padded(3,4) =
  x_0·per_3(x_1..x_9)` in `Sym^4 C^10`. Checked against a from-scratch permanent
  at `r = 3..6` (`wk10_s64_pad.py`); at `r = 10` with the identity frame `ev_pad`
  **is** the committed `tools/verify/testset/padded_permanent.json` point.
- **(A3) The family already existed.** `wk9_s36_stabred.measure_reduced` runs
  `sides = ('det','pad')`; `wk9_s45_cell` and `wk9_s41_kernel` (line 134) both
  carry `forms['pad'] = (PAD34, N_PAD)`. Session 60's dense engine wired only det
  and red. So this session is a bounded extension — one coefficient-dict producer
  plus wiring — needing no new equivariant model, and note 1's instruction to
  "implement `ev_pad`" is superseded: it existed; this session **validated** it.

This is the **third** batch-10 item described as missing that was in fact banked
(after the Gram double-coset observation, session 56, and the `h_pad` Pieri
identity, session 42). The common cause, as the integrator notes, is that the
batch was planned from documents rather than from the code, and each time the
code was ahead — worth recording as a lesson, not three coincidences.

## 2. `ev_pad`, in the same coordinates and the same `E` (Task 2)

`analysis/wk10_s64_pad.py`: `pad_frames` draws `r` source vectors in `C^10`;
`pad_coeffs(V) = restrict(PAD34, 10, 4, r, V)` is `l(s)·per_3(A(s))` in
`Sym^4 C^r`, shape-identical to `det_coeffs`/`red_coeffs`.
`analysis/wk10_s64_cell.py`: one `build_cell`, one flint kernel of `E` per prime
(exact ≤ 2500 columns, else the certified random compression, s41 semantics;
every kernel vector verified on the full sparse `E`), then
`mult_side = rank(ev_side · kern^T)`, `i_side = a − mult_side`,
`U_side = ker T_side` in the shared `a`-coordinates on `M_lam = span(kern)`.
Large cells go on the sparse route (`analysis/wk10_s64_sparse.py`, the s45
Wiedemann certificates on `[E; ev_pad]` — the instrument s60 uses for det and
red). `python-flint` `nmod_mat`; primes `2147483647, 2147483629`.

## 3. Containment, `P_r = R_r`, and `h_pad` (Tasks 3–4)

`R_r = {l·c}` contains the padded orbit closure since `per_3` is one cubic, so
**(proved)** `I(R_r) ⊆ I(pad) ⟹ mult_pad ≤ mult_red`. This is the primary
calibration.

**`P_r = R_r`, with the reason (measured, `results/s64_paramrank.md`; integrator
note 2).** The permanental cubics `{per_3(A(s))}` fill all cubics for `r ≤ 5` and
are strictly smaller for `r ≥ 6`. The differential of `M ↦ per_3(M(s))` has a
generic fibre of dimension `4` — the projective torus of `per(D_1 M D_2)`,
`(3−1)+(3−1) = 4` — so `dim image = min(9r − 4, C(r+2,3))`, dominant `⟺ 9r − 4 ≥
C(r+2,3) ⟺ r ≤ 5` (`41 ≥ 35` at `r = 5`, `50 < 56` at `r = 6`). Measured ranks
match at both primes: `35,35` at `r=5`; `50 = 54−4` at `r=6`; `59 = 63−4` at
`r=7`. Hence `mult_pad = mult_red` **exactly** at `r ≤ 5`, and only
`mult_pad ≤ mult_red` at `r ≥ 6` — the transfer lemma's split, from the cubic side.

**`h_pad` (provenance: the identity is session 42's; the factorization is S3's —
house rule 13).** `h_pad(λ,δ) = Σ_{λ/μ horiz δ-strip} a_3(μ,δ)` is
`analysis/wk9_s42_hpad.py`, proved in `docs/reducible_engine.md` §B (Kempf
collapsing; `H^0(Z,O_Z)` is the Segre-product ring, the normalisation of
`C[R_r]`), whence `mult_pad ≤ mult_red ≤ h_pad`. Recomputed here across all 48
cells (`wk9_s42_census.h_pad_weyl`): matches the banked ledger at every cell, and
the chain `mult_pad ≤ mult_red ≤ h_pad` holds everywhere. S3's padded Gram at
`δ = 2` was reproduced independently from the formula alone
(`analysis/wk10_s64_padgram.py`): the three orbital values `20736, 2592, 1152`
match exactly, so `mult_pad = a` at all three `δ = 2` constituents by a route
sharing no code with the evaluation engine.

**Calibration result** (`results/s64_calibration.md`, `.jsonl`). Every measured
`r = 5` cell has `mult_pad = mult_red` (both primes), matching the banked value;
every cell satisfies `mult_pad ≤ mult_red ≤ mult_det`. The discriminating cells —
`mult_red < a`, the only cells that can tell a correct padded engine from one
silently measuring the determinant at `r ≤ 5` — all confirm
`mult_pad = mult_red < mult_det`:

  | r | δ | λ | a | h_pad | mult_det | mult_red | mult_pad | D | route |
  |---|---|---|---|---|---|---|---|---|---|
  | 3 | 6 | (8,8,8) | 2 | — | 2 | 1 | **1** | −1 | indep |
  | 5 | 6 | (8,4,4,4,4) | 2 | 1 | 2 | 1 | **1** | −1 | dense |
  | 5 | 7 | (9,9,8,1,1) | 2 | 1 | 2 | 1 | **1** | −1 | dense |
  | 5 | 9 | (15,15,4,1,1) | 9 | 12 | 9 | 8 | **8** | −1 | dense |
  | 5 | 7 | (8,8,8,2,2) | 3 | 2 | 3 | 2 | **2** | −1 | sparse |
  | 5 | 7 | (12,4,4,4,4) | 4 | 4 | 4 | 3 | **3** | −1 | sparse |
  | 5 | 8 | (11,11,8,1,1) | 8 | 8 | 8 | 7 | **7** | −1 | sparse |
  | 5 | 8 | (12,9,9,1,1) | 7 | 6 | 7 | 5 | **5** | −2 | sparse |
  | 5 | 8 | (16,4,4,4,4) | 7 | 10 | 7 | 6 | **6** | −1 | sparse |
  | 5 | 8 | (13,9,8,1,1) | 15 | 21 | 15 | 13 | **13** | −2 | sparse |
  | 5 | 9 | (20,4,4,4,4) | 9 | 13 | 9 | 8 | **8** | −1 | sparse |
  | 5 | 9 | (13,13,8,1,1) | 19 | 17 | 19 | 15 | **15** | −4 | sparse |

The `(8,4,4,4,4)_6` cell is pinned by `P_5 = R_5` to `mult_pad = 1` **exactly**
(a genuine kernel in a two-dimensional source, `a = 2`): an engine returning 0 or
2 is defective; mine returns 1 (integrator note 2 §3). In every discriminating
cell the padded engine returns the reducible value strictly below the
determinant's — it measures the padded side and does not echo the determinant.

## 4. Rank agreement across seeds and primes (Task 5)

Random evaluation gives a **lower** bound on the true rank, so seeds and margins
are explicit. Dense route: `mult_pad, mult_red, mult_det` at **two independent
seeds** and **both primes**, all agreeing, with `mult` at least `6` below the
point count `K = a + 8` at every cell (margin ≥ 6). Sparse route: the nullity is
**certified exact** per prime (a nonsingularity certificate for `[F; k random
rows]` gives `nullity ≤ k`; `k` exhibited independent kernel vectors give
`nullity ≥ k`), and both primes agree. A **second, independent implementation**
(`analysis/wk10_s64_indep.py` — full weight-`lam` basis, session-30 raising rows,
exact flint nullspace, sharing no code with the isotypic/Wiedemann engine and
r-generic) reproduces `mult_det, mult_red, mult_pad` and the banked
`(mult_det, mult_red)` at every `r = 3, 4` cell and six `r = 5` cross-checks.

## 5. The degeneracy-direction pre-check (Task 6)

`tools/verify/testset/degeneracy_check.py` on the committed full ten-variable set:

    det_pencil        (615, 1452, 2996, 5720)
    reducible         (615, 1488, 3174, 6276)
    padded_permanent  (620, 1538, 3395, 6881)

**WRONG DIRECTION for the Macaulay corank**: the padded permanent is strictly
more degenerate than the determinant in every component (session 51's Proposition
D), and on the full ten-variable object the reducible and padded points
**disagree** — the six-variable restriction hides this (`red = pad` there),
confirming the brief's warning about length-reduced restrictions. This is the
pre-check working: the rank/Macaulay route separates the wrong way, which is
exactly why this session measures the **multiplicity**, which is functorial
(`brief_wording.md` §7: `P ⊆ D ⟹ I(D) ↠ I(P) ⟹ mult_pad ≤ mult_det`). For the
multiplicity, `i_pad ≥ i_det` is not a defect but the containment being tested;
the engine's own directional invariant `i_det ≤ i_red ≤ i_pad` holds at every
cell. `ev_pad`'s full ten-variable object is verified to be exactly the committed
`padded_permanent.json` point.

## 5b. The r ≥ 6 separation test (integrator note 2 §4)

`P_r = R_r` at `r ≤ 5` means **no `r ≤ 5` multiplicity calibration can
distinguish a correct padded engine from one that silently implemented the
reducible side** — they agree by theorem. Worse, session 47 proved
`mult_pad = mult_red` at every reachable `r = 6` cell too (the permanent-specific
ideal is empty until the LMR degree), so the *multiplicities* coincide in reach
even at `r = 6`; reproduced here at `(18,2,2,2,2,2)_7`, `(15,5,5,1,1,1)_7`,
`(16,4,2,2,2,2)_7` with the reduced pad engine (`mult_pad = mult_red` at each).

The separation available in reach is at the level of the **sample variety**, and
it is not linear (the permanental cubics linearly span all of `Sym^3 C^6`). The
right invariant is the dimension of the variety `ev_pad` samples — the Jacobian
rank of its own parametrisation (`analysis/wk10_s64_separation.py`, both primes):

    r | dim P_r (ev_pad) | dim R_r (ev_red)
    5 |       39         |       39          (equal — why no r<=5 test separates)
    6 |       55         |       61          (deficit 6)
    7 |       65         |       90          (deficit 25)

`dim P_6 = 55 < 61 = dim R_6`, matching `dim P_r = r + min(9r−4, C(r+2,3)) − 1`.
An engine that had silently implemented `ev_red` would return `61`; mine returns
`55`. So `ev_pad` provably samples the padded variety, not the reducible one —
the separation the `r ≤ 5` suite cannot provide. The coincidence
`mult_pad = mult_red` at `r ≤ 6` is thus a theorem about the varieties (deficit
invisible below the LMR degree), not an artefact of the two engines being the
same code.

## 6. Kernel coordinates preserved (Task 7)

`results/s64_kern/kern_<cell>.json.gz` (39 cells): dense cells save the `a`
kernel HWVs `kern` (`E·kern = 0`) and the ideal-slice bases `U_det, U_red, U_pad`
in the shared `a`-coordinates on `M_lam = span(kern)`, each expanded to
verifier-checkable monomial terms; sparse cells save the exhibited kernel vectors
of `[E; ev_pad]` in monomial coordinates. Session 65 compares `U_D = ker T_det`
against `U_P = ker T_pad` directly. Spot-verified: at `(9,9,8,1,1)_7`,
`U_red = U_pad` as subspaces of `span(kern)` (both 1-dim, union 1-dim), the shared
vector vanishing on fresh reducible **and** padded points while nonzero on
determinant pencils — the `D = −1` witness; at `(13,13,8,1,1)_9` the four `U_pad`
vectors each vanish on padded points and are nonzero on determinant pencils — the
`D = −4` witness.

## 7. Cost curve and LMR reachability (Task 8)

`results/s64_cost.md`. Dense (`n_chi ≤ 4600`): `≈ 0.6–3 s` below `n_chi = 2500`
(exact nullspace), `14–30 s` at `n_chi ≈ 4000–4600` (compression). Sparse:
`≈ 285–520 s` at `n_chi ≈ 10^4`, up to `1560 s` at `n_chi = 20099` (`a = 19`,
four kernel vectors). Scales as the s60 curve `≈ 10^{-8}·n_chi^2·(14.5 + a)` s per
Wiedemann sequence, one per prime and one per exhibited kernel vector.

**LMR reachability (measured input from integrator note 1 + expectation).** The
cheap `h_pad` screen does **not** exclude LMR: `h_pad((65,17,2^7), 24) = 521 >
273 = mult_det`, and since `mult_pad ≤ h_pad` always, the pad-side ceiling is
entirely vacuous at LMR (`521 > 274 = a`). **A rank is genuinely required** —
which is the strongest argument that sessions 63/64 are worth their cost. Two
routes to that rank:

- **The factorized route (successor's primary architecture).**
  `M^(4)_λ →S→ ⊕_{μ} M^(3)_μ →⊕Θ→ ⊕_μ M^(3)_μ / ker Θ^{per_3}_{μ,δ}`, the split
  map factoring each quartic into linear × cubic, target `h_pad`-dimensional, so
  at LMR the work list is **48 blocks** (`wk9_s42_hpad.pieri_strips`,
  `results/logs/hpad_lmr.log`) — each an `Sym^3` problem, smaller than the single
  `n_chi ≈ 1.4·10^6` `Sym^4` solve. Its load-bearing identity
  `mult_pad = rank[(⊕_μ Θ^{per_3}_{μ,δ}) ∘ S_{λ,δ}]` is **unchecked and
  unbanked** (integrator note 1 §5); the `r = 5` calibrations in §3 are its
  testbed, and now they test it as an **equality** (`mult_pad = mult_red`
  exactly). This session provides that validated testbed; it does not build the
  `Θ∘S` machinery (that is session 65's, and S5 forbids the LMR attempt here).
- **The `ev_pad` fast branch (this session's instrument).** Evaluating the LMR
  common-source vectors at padded points; a full modular rank gives `i_pad = 0`
  and, with session 63's `i_det = 1`, `D_LMR = 1` with no exact machinery — but it
  is gated on the **same wall** as session 63 (building/evaluating the common
  source at `r = 9, δ = 24`). It removes the exact padded machinery from the
  critical path; it does not remove the bottleneck. A deficient modular rank
  proves nothing and returns to the factorized route.

So `mult_pad` is exactly as reachable as `mult_det` at LMR by the fast branch,
and potentially cheaper by the factorized route; the padded side is not the
bottleneck. This session does not attempt LMR (S5); the calibration certifies the
instrument.

## 8. Independent verification and scorecard

Second implementation (`wk10_s64_indep`, §4) agrees everywhere; `P_r = R_r`
verified from the cubic side at both primes with the closed-form reason; the Gram
`δ = 2` values reproduced from the formula; `h_pad` reproduced from the
session-42 identity; the golden cell's kernel membership verified against fresh
points; the base engine reproduced the banked golden cell before extension; the
r ≥ 6 separation confirms `ev_pad ≠ ev_red`.

Scorecard vs `results/PREREG_s64.md`: A1–A3 **confirmed**; containment held at
every cell (F1 not fired); `P_r = R_r` at `r ≤ 5`, `⊊` at `r ≥ 6` **measured**
with the closed form; `mult_pad = mult_red` at every measured `r = 5` cell (F2
not fired); prime/seed agreement with margin ≥ 6 (F3 not fired); degeneracy
pre-check recorded, Macaulay wrong-direction as expected, multiplicity route
exempt by functoriality (F4 handled); r ≥ 6 separation added and passed; no LMR
attempt (S5 respected). No stopping rule fired. **Unchecked and handed to session
65:** the factorized composite-rank identity `mult_pad = rank[(⊕Θ)∘S]`.

## 9. Deliverables

`results/PREREG_s64.md`; this report; `results/s64_calibration.md` +
`results/s64_calibration_unified.jsonl` (raw `results/s64_calibration.jsonl`);
`results/s64_paramrank.md`/`.jsonl`; `results/s64_separation.json`;
`results/s64_cost.md`; `results/logs/s64_degeneracy.log`,
`results/logs/s64_padgram.log`; kernel bases under `results/s64_kern/`; code
`analysis/wk10_s64_pad.py`, `wk10_s64_cell.py`, `wk10_s64_sparse.py`,
`wk10_s64_indep.py`, `wk10_s64_paramrank.py`, `wk10_s64_padgram.py`,
`wk10_s64_separation.py`, `wk10_s64_calibrate.py`, `wk10_s64_table.py`; bundle
`s64_padded.bundle` + `.md5`.
