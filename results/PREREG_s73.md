# Pre-registration — session 73 (batch 11, C6): the decision table, and the `D`-ladder at `n = 3`

Branch `s73-dladder` off `main` at `226b4ef1` (ancestry gate passed on a fresh
clone: `git merge-base --is-ancestor 226b4ef1 HEAD`).  Container only, no
pushes; delivery by single-ref bundle `s73_decision.bundle` + `.md5`.  Written
and committed **before any cell is built or any rank is read**.  Labels:
**proved** / **measured** / **adopted** / **expectation**.

Written 2026-09-08 01:15 UTC.

## 0. Inputs that could not be found, recorded up front

The brief names `docs/batch11_worker_preamble.md`, `docs/batch11_plan.md`,
`docs/s65_prompt.md`, `docs/stocktake_batch10.md`, `analysis/wk11_int_p0a.py`,
`results/wk11_int_p0a.json`, `analysis/wk10_s63_n3control.py`, the certificate
family `results/certs/19_7_2_2_2_2_2_d12_n3_permanent_*`, and a verifier that
accepts `n ∈ {3,4}` with a `permanent` point family.  None of these exists at
`226b4ef1`, in any branch of the public repository, or in the integrator tree
on the laptop (`Projects/gct/work`, at the same `226b4ef1`); the s63 bundle is
not in `Projects/gct` either.  What *is* reachable: the s62, s64 and s66
bundles (fetched into this clone as `refs/bundles/*`; md5
`680de0d9…`, `c0eb9b6f…`, `5bb2e351…`).  Session 62's `analysis/wk10_s62_n3.py`
is an independent driver of the same `n = 3` control (`i_det = 1`, `mult_det = 5`
at both primes; two-sided ladder `2, 4, 5` full at `δ = 9, 10, 11`) and its
records are used as the banked anchors below.  As in batch 10, the session
runs from the brief; the verifier extension (§7) is made here, minimally, and
flagged for reconciliation with the integrator's.

## 1. Object and question

`n = 3`, `r = ℓ(λ) = 7`, the unpadded comparison of `det_3` and `per_3` in
`Sym^3 C^9`, measured on the `7`-pencil slices `D_7 = closure{det_3(Σ s_i A_i)}`
and `P_7 = closure{per_3(Σ s_i A_i)}` in `Sym^3 C^7` (the (★) reduction: the
`λ`-isotypic part of the coordinate ring of the `GL_9` orbit closure is that of
the `r`-pencil variety for `r ≥ ℓ(λ)`).  The ladder is

    λ_δ = (3δ − 17, 7, 2^5),   |λ_δ| = 3δ,   δ ≥ 8 (λ_1 ≥ λ_2 needs δ ≥ 8).

For each rung: `a(δ)` = mult of `S_{λ_δ}` in `Sym^δ(Sym^3 C^7)`;
`i_det = dim (I(D_7) ∩ HWV_λ)`, `i_per = dim (I(P_7) ∩ HWV_λ)`;
`mult_X = a − i_X`; and the decision quantity

    D(δ) = i_det(δ) − i_per(δ) = mult_per(δ) − mult_det(δ).

`D > 0` refutes `P_7 ⊆ D_7` (functoriality, `docs/brief_wording.md` §7, row 1:
`P ⊆ D ⟹ I(D) ⊆ I(P) ⟹ U_D ⊆ U_P ⟹ i_det ≤ i_per`).  Both multiplicities are
nonzero at every rung with `a > 0`, so any `D > 0` here is a **multiplicity
obstruction**, not an occurrence obstruction.  The separation itself is not
news (`dim P_7 = 59 > 47 = dim D_7`); the content is the certificate and the
ladder behaviour.

Also carried at every rung, in the same `χ`-coordinates: `U_D = ker T_det`,
`U_P = ker T_per` (kernels of the evaluation pairings on `HWV_λ`), and
`dim(U_D ∩ U_P)`.  The finer statements `U_D ⊄ U_P` (an equation of `D_7` not
vanishing on `P_7`, refuting `P_7 ⊆ D_7` even when `D = 0`) and `U_P ⊄ U_D`
(refuting `D_7 ⊆ P_7`) are recorded as the *orientation* of the rung.

## 2. Banked anchors (adopted; to be reproduced before anything new)

| rung | `a` | `i_det` | `mult_det` | `i_per` | `mult_per` | source |
|---|---|---|---|---|---|---|
| `δ = 9`,  `(10,7,2^5)` | 2 | 0 | 2 | — | — | s62 (`P1`), s63 |
| `δ = 10`, `(13,7,2^5)` | 4 | 0 | 4 | — | — | s62 (`P1`), s63 |
| `δ = 11`, `(16,7,2^5)` | 5 | 0 | 5 | — | — | s62 (`P1`), s63 |
| `δ = 12`, `(19,7,2^5)` | 6 | 1 | 5 | 0 | 6 | s62, s63 (both primes); P0-A (brief) |

`i_det(12) ≥ 1` is LMR's theorem at this cell (**adopted**); `i_det(12) ≤ 1`
and `i_per(12) = 0` are one-sided mod-`p` certificates (`rank_p ≤ rank_Q ≤ a`),
so `i_per(12) = 0` and `D(12) = +1` hold over `Q` given the brief's P0-A
run — which this session re-derives on its own driver at both primes before
relying on it (§5, R1).

## 3. What is already forced, stated before the runs

**(proved, this session, from two independent plethysm engines)**  The
`a`-ladder, computed by `tools/verify/pleth.py` (from-scratch box DP) and by
`analysis/wk9_s42_census.a_weyl` (the house Kostant tail DP), which agree at
every `δ = 8 … 20`:

    δ :  8  9  10 11 12 13 14 15 16 17 18 19 20
    a :  0  2   4  5  6  6  6  6  6  6  6  6  6

**(adopted from s57, Lemma L and Proposition S; both proofs are verbatim at
`n = 3` with `c = e_1^3`, `Z = Sym^2 V'^* ⊕ Sym^3 V'^*`, stability from
`δ ≥ |tail| = 17`.)**  Lemma L: multiplication by `c = c_{(3,0,…,0)}` injects
`(C[W])^{hw}`, `(I(X))^{hw}` and `(C[X])^{hw}` up the ladder for every
irreducible `GL_7`-stable cone `X ⊄ {c = 0}` (`D_7` and `P_7` qualify:
`det_3(A_1) ≠ 0`, `per_3(A_1) ≠ 0` generically), so `a`, `mult_X`, `i_X` are
non-decreasing, and `a(δ+1) = a(δ)` forces `i_X(δ+1) = i_X(δ)`.  Proposition S:
`a(δ) ≤ a_∞(tail)` with equality for `δ ≥ 17`; hence `a(17) = 6 = a_∞`, and
`6 = a(12) ≤ a(δ) ≤ 6` for all `δ ≥ 12`.

**Consequence (proved, conditional only on the `δ = 12` anchors of §2):**

    for every δ ≥ 12:   i_det(δ) = 1,   i_per(δ) = 0,   mult_det = 5,   mult_per = 6,   D(δ) = +1,

and, since the transport is injective with equal dimensions,
`U_D(δ) = c^{δ−12} · U_D(12)` (one line, the transported LMR vector) and
`U_P(δ) = 0`.  Downward: `i_per(9) = i_per(10) = i_per(11) = 0` (monotone,
bounded by `i_per(12) = 0`).

So the brief's three cases (`1,1,1,…` / `1,0,0,…` / `1,2,…`) are not open: the
first holds by theory.  This session therefore states the theorem, and then
**measures the rungs anyway** — a run whose answer is predicted is the sharpest
instrument test available, on both engines (the cell builder at a new degree
and the transport map between two independently built cells).  Every rung is
still a measurement in its own right, at both primes, with certificates.

## 4. Pre-registered predictions

| # | prediction | status if it fails |
|---|---|---|
| P1 | `δ = 12` reproduces §2 on this driver at both house primes with a fresh evaluation family (§6 seeds) | halt (R1) |
| P2 | `i_det(13) = i_det(14) = 1`, `i_per(13) = i_per(14) = 0`, both primes | instrument or theory defect: halt (R4) |
| P3 | the `δ = 13` (resp. `14`) kernel vector of `[E; ev_det]` is proportional mod `p` to `c · v_12` (resp. `c^2 · v_12`) | instrument defect in one of the two builds: halt (R4) |
| P4 | `dim J(M_11) = 5`, birth space at `δ = 12` of dimension `1`; `v_12 ∉ J(M_11)` (its `u`-free part is nonzero) | report as a finding, not a halt |
| P5 | `dim J(M_12) = 6 = a(13)`: `M_13 = c·M_12`, birth space `0` at `δ = 13` and `14` | instrument defect: halt (R4) |
| P6 | `i_per = 0` at `δ = 9, 10, 11` (one prime suffices) | contradicts monotonicity: halt (R4) |
| P7 | `dim(U_D ∩ U_P) = 0` at every rung (`U_P = 0`) | follows from P2; a nonzero `U_P` halts (R4) |
| P8 | `i_pad = a` at every rung (the padded `n = 3` model `x_0·per_2` is concise in 5 variables, `ℓ(λ) = 7 > 5`, so `mult_pad = 0`: **proved**, the washout) | not measured separately; stated |

Confidence that P1–P7 all hold: 0.9 (the residual is engine failure at a new
degree, not mathematics).

## 5. Stopping rules (house wording)

- **R1** — `δ = 12` does not reproduce §2 at both primes: halt, report the
  disagreement; nothing further is run.
- **R2** — the two house primes disagree on `i_per` (or `i_det`) at a rung:
  that rung halts; the disagreement is reported.
- **R3** — the nullity of `E` (when computed) or the `a` the build implies
  disagrees with the Weyl-alternation value: halt — instrument defect.
- **R4** — any rung contradicts §3 (P2, P3, P5, P6, P7): halt that rung,
  diagnose which engine is wrong (transport vs direct build), report.
- **R5** — any `D > 0` at any rung goes through the verification protocol
  (§8) **before** it is reported anywhere, including in conversation.
- **R6** — the Mode A checkpoint (§9) is honoured at its stated time and not
  waited past.

## 6. Seeds, primes, points (banked here, before any run)

- Primes: the house pair `P1 = 2147483647`, `P2 = 2147483629`.
- Points: `K = a + 8` pencils per family per rung, entries in `[−40, 40]`
  (house convention), drawn from `random.Random(seed)`:
  `seed_det = 20260908`, `seed_per = 20260908 + 1000` (fresh: independent of
  the s62/s63/P0-A stream `seed = 11`).  Verification-protocol families:
  `seed_det2 = 20260908 + 2000`, `seed_per2 = 20260908 + 3000`, `K = a + 20`;
  fresh integer pencils for the over-`Z` checks `seed = 20260908 + 4000`
  (det), `+ 5000` (per), `+ 6000` (generic cubics), entries in `[−40, 40]`.
- Wiedemann: `seed0 = 1` (as in `wk9_s45_cell`; randomness decides only
  conclusiveness, never correctness), levels `((12,2), (None,1))` — the s45
  rule for `n_rows/n_χ ≳ 10` (here `≈ 42`).
- Certificate fresh points (verifier): `seed = 20260908`, `count = 6`.

## 7. What is measured, and how (the instruments)

- Build: `analysis/wk9_s45_build.build_cell(lam, delta, n=3)` (unchanged;
  s62 validated it at `n = 3` against the dense engine on small cells).
- Nullities: `analysis/wk9_s45_cell.nullity_stacked` (unchanged) on
  `[E; ev_det]` and `[E; ev_per]`, the `ev` rows pinned, both primes, kernel
  vectors wanted; `ev` rows by `wk9_s45_build.ev_rows_arr` with
  `det_form(3)` / `per_form(3)` from `wk8_s30_core`.
- `M_12 = ker E` explicitly (the full-`E` nullity solve at `δ = 12`, one
  prime), for the transport checks; `M_13 = c·M_12`, `M_14 = c^2·M_12`.
- Transport `J`: computed at the monomial level (multiply every term by
  `c_{(3,0,…,0)}`, contract to the next rung's `χ`-coordinates); checked by
  `E_{δ+1} J(v) = 0` and by rank.
- Over `Q`: kernel vectors rationally reconstructed to integer vectors,
  `E v = 0` over `Z`, vanishing at fresh integer det pencils over `Z`,
  nonvanishing at fresh integer per pencils and generic cubics over `Z`
  (Schwartz–Zippel evidence; the rigorous `i_det ≥ 1` is LMR + transport).
- Certificates (`results/certs/s73/`): a `sparse_nullity` record for every
  full-rank claim (cell, prime, points by substitution data, reduction sizes,
  level, seeds, Berlekamp–Massey degree and constant term, claimed nullity),
  and an `hwv` certificate (integer, `modulus: null`) for every exhibited kernel
  vector with `vanishes_at` det pencils and `nonvanishing_at` permanent
  pencils, plus fresh points.  `tools/verify` is extended minimally to
  `n ∈ {3,4}`, a `permanent_pencil` point family, and the `sparse_nullity` kind
  (structural checks; the Wiedemann step is re-runnable from the recorded
  seeds).  The extension is documented in `tools/verify/FORMAT.md` and flagged
  for reconciliation with the integrator's version, which this session could
  not obtain.

## 8. Verification protocol for `D > 0` (applies to every rung; run at `δ = 12` in full)

1. second house prime (both primes at every rung);
2. independent evaluation family: fresh seeds, `K = a + 20`;
3. characteristic zero: integer kernel vector exhibited and checked over `Z`
   (raising operators, vanishing at fresh det pencils, nonvanishing at fresh
   per pencils and generic cubics);
4. independent source: the kernel vector re-verified by the from-scratch
   `tools/verify` (its own raising operators over `Z`, its own forms) with no
   import from `analysis/`; and the `δ = 13, 14` vectors obtained two ways
   (direct Wiedemann on an independently built cell, and transport of `v_12`);
5. degeneracy pre-check (`brief_wording.md` §5/§7): the statistic is the
   coordinate-ring multiplicity, functorial in the right direction; the sign
   of the separation agrees with the known `dim P_7 > dim D_7`; the evaluation
   family is the unpadded `per_3` pencil, i.e. the generic point of the `GL_9`
   orbit closure itself, not a length-reduced restriction of something else.

## 9. Mode A checkpoint

**Checkpoint time: 2026-09-08 04:30 UTC.**  At that time the laptop folder
`Projects/gct` is listed for a new bundle from session 68, 69 or Sol's S5
delivering an LMR source basis (`λ = (65,17,2^7)`, `δ = 24`).  If one is
present, the session switches to the Mode A tasks of the brief (`i_det`,
`i_pad`, `i_{per_4}` at LMR from that source, `U_D`, `U_P`, the three-outcome
table).  If none is present the session stays in Mode B, which is its default
deliverable, and does not wait.

## 10. Rung order and banking

`δ = 12` (calibration, both sides, both primes, `M_12`), then `13`, `14`; then
`15`, `16` if the night allows; then `9, 10, 11` on the per side (and the det
side re-read).  Each rung is committed as it completes (`results/s73_dladder.jsonl`
is append-only), logs under `results/logs/`, nothing over 5 MB committed;
checkpoint bundles to the conversation every few hours.
