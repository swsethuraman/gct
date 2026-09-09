# Session 77 — the deterministic basis: the bridge, controlled, and the honest cost

*(this batch's s77 = the reconciled proposal's s76). Base
`main = afb8c3319d3d1f3afc3d2578c8cb322f2b8a3b92`, branch `s77-bridge`. Every
number below is MEASURED (evaluation-route, Schwartz–Zippel status unless a
full-rank-one-prime or exact-integer certificate strengthens it), PROVED, or
RECORDED/ADOPTED, and is labelled. The verification protocol is not triggered:
this session produces no `D` and touches no padded evaluation.*

## 0. Outcome in one paragraph

The bridge asked for — an explicit map **S5 Pieri state → s69 bracket filling**,
so that a deterministic basis from the recursion is evaluable through the fast
circuit oracle with no coordinate expansion — is written down and validated. It
is the identification **a bracket filling is an unlabelled Pieri chain**: a
column-strict filling of `λ` with content `(nᵟ)` (an SSYT) is a Pieri path
`λ = ν⁽ᵟ⁾ ⊃ … ⊃ ν⁽¹⁾`, each step a removable horizontal `n`-strip, and
`F_T = ⟨` tableau tensor `, f̃^{⊗δ}⟩` is the image, under the s69 pairing, of the
abstract Pieri state — realizing the `S_δ`-invariant (= `τ`-invariant) projection
the recursion computes as `ker(τ−I)`. **Both mandatory controls are reproduced
from the deterministic SSYT basis, not by sampling**: the `n = 3` LMR cell
(generic rank 6, `mult_det = 5`, `i_det = 1`, and the banked determinant ideal
line reproduced entry-for-entry) and the `n = 4, δ = 12` seed (generic rank 2,
`mult_det = 2`, `i_det = 0`). The theory session **S3 landed during this session
and derived the same map from the recursion side** (its §7, `F_v(f) =
(4!)¹²⟨Φ(v), f̃^{⊗12}⟩`, and its slot permutation `π_i` are exactly this
session's filling→tensor identification); the two derivations agree. The honest
residual, shared by both sessions, is the compact **recursion→circuit
change-of-basis** `C` — S3's four permutation coefficients — which requires
acting with a length-640 permutation on the `dim S^λ = 6.74×10²¹`-dimensional
seminormal space; it is not closed here and its naive route is priced out below.
The measured ladder comparison shows random sampling beats deterministic
enumeration for *discovery*, confirming the batch's own finding that discovery is
no longer the binding constraint; the deterministic basis's value is reproducible
assembly and certification, which the controls demonstrate.

## 1. The bridge (the map)

**The identification (PROVED, and independently confirmed by S3).** For `λ ⊢ nδ`
with conjugate `λ' = (h_1, …)`, an s69 filling assigns each of the `δ` letters
`n` cells, one per column it meets — each letter is a **horizontal `n`-strip**. A
*column-strict* filling — an SSYT of shape `λ`, content `(nᵟ)`, values `1..δ`
each used `n` times, strict down columns, weak along rows — is exactly a **Pieri
path** `λ = ν⁽ᵟ⁾ ⊃ ν⁽ᵟ⁻¹⁾ ⊃ … ⊃ ν⁽¹⁾`, each `ν⁽ⁱ⁾/ν⁽ⁱ⁻¹⁾` a removable
horizontal `n`-strip, with cell-value `i`. (Proof: `{cells ≤ i}` is a Young
diagram for every `i` iff labels are strict down columns and weak along rows, and
`ν⁽ⁱ⁾/ν⁽ⁱ⁻¹⁾` is then a horizontal strip; conversely a Pieri path labels each
cell by its step.) The tableau tensor `⊗_j (e_1∧…∧e_{h_j})` of s69's Identity 2
is the iterated Pieri image of the seed tensor, so `F_{SSYT} = ⟨` tableau tensor
`, f̃^{⊗δ}⟩` is the image, under `⟨−, f̃^{⊗δ}⟩`, of the abstract Pieri state; and
because letters are unlabelled, `F_T` is `S_δ`-symmetric, so it realizes the
`S_δ`-invariant projection `= ker(τ−I)`. **This is the sense in which the Pieri
state and the bracket filling are the same vector.** No abstract conversion
`x = y A^{-1}` and no coordinate expansion is used — evaluation is the circuit
(`2^{n_2}·2^h` determinants per point), so the map is evaluable by construction.

**Agreement with S3 (RECORDED; S3's artifacts read via the device bridge — see
§8).** S3 §7 defines, for a filling, the permutation sending "the `k`-th
occurrence of letter `l` to tensor slot `4l+k`" and sets
`F_v(f) = (4!)¹²⟨Φ(v), f̃^{⊗12}⟩` with `Φ` the intertwiner `Φ(e_{t_c}) = q_λ`.
That slot map is this session's filling→tensor-slot assignment, and `F_v` is
`F_{SSYT}` (the `(4!)¹² = (n!)^δ` is the polarisation constant s69 drops). S3
built the map from the recursion (`τ`) side; this session built it from the
filling side and validated spanning. The two are the two halves of the one
bridge and they coincide.

## 2. The `k`-reconciliation (MEASURED; the proved test confirmed)

The proved unshared-column test (S1 rule 4): tall columns sharing `k` letters
with `h−k > n` force `F_T = 0`; at `n = 4, h = 9` this is `k ≤ 4 ⟹ F_T = 0`. The
δ=24 birth representative `T₅₇` has `k = 9`. **There is no tension** (the
integrator's note 3 says the same, and it was mine to see cheaply): `k < 5` is a
*sufficient condition for vanishing*, so a nonzero representative needs
`k ≥ h−n = 5`, and `k = 9` (maximal overlap) is the opposite extreme. Confirmed
by direct measurement at `δ = 18` (where `k = 0..9` are all instantiable; at
`δ = 12` the combinatorics force `k ≥ 6`): every `k ≤ 4` filling vanishes at both
primes (the proved test, now MEASURED), `k = 5` also vanishes empirically (beyond
the proof), and nonzero fillings occur for `k ≥ 6` with the saved δ=24 fillings
distributed over `k ∈ {6,7,8,9}` and `T₅₇` at `k = 9`. Per the integrator's note
I did not pursue the optional `n = 4` *upper*-bound-on-`k` theorem; it is not
what this session is for.

## 3. Control 1 — `n = 3` LMR `((19,7,2⁵), 12)`, `a = 6` (MEASURED + CERTIFIED)

From the **deterministic** SSYT stream (canonical order A, no RNG):

- generic rank **6/6** at both house primes — the SSYT (Pieri chains) span
  `M_λ`. (Scan cost recorded: first nonzero SSYT at #1077, rank 6 reached at
  scan #2280, 102 nonzero of 2280 — see §6 on cost.)
- determinant rank **5**, so `mult_det = 5`, `i_det = 1` at both primes — the LMR
  rank drop, the programme's positive control, reproduced from a deterministic
  basis.
- every one of the six basis fillings expands exactly (`812 851 200` terms in C,
  ~226 s each): `E·v = 0` over `Z`, χ-isotypic (no orbit inconsistency, no
  dropped-nonzero, no missing member), and the coordinate-side evaluation equals
  the circuit at every point used (evaluator == expander).
- **the banked determinant ideal line reproduced entry-for-entry**
  (`results/artefacts/s69_banked_n3_d12.json`, 17 047 χ-coords): the circuit
  kernel `U_D` is proportional to the banked vector at both primes (0/17 047
  mismatches), and over `Z` equal up to sign (support 3900, max|c| 544,
  `E·U_D = 0`).

Content note (from the adversarial verifier): at `n = 3` the content is `(3¹²)`
— each letter three times — not `(4¹²)`; the code uses `n` legs per letter, so
this is correct; the report says `(nᵟ)`.

## 4. Control 2 — `n = 4, δ = 12` seed `((17,17,2⁷), 12)`, `a = 2` (MEASURED)

From the **interleaved** SSYT stream (round-robin over overlap `k`, no RNG):
generic rank **2/2** at both primes, `mult_det = 2`, `i_det = 0` — matching the
banked seed `results/s69_n4_seed.json`. **Overlap treatment, explicit:** the two
basis directions are born at `k = |C₁ ∩ C₂| = 9` and `k = 8`; the maximal-overlap
`k = 9` class alone spans only **rank 1** (MEASURED), so a spanning deterministic
stream must mix `k` — the round-robin does. This is the concrete content of "the
explicit treatment of tall-column overlap" the brief asked for.

**Connection to S3 at this exact cell.** S3's control is the same cell. Its
`u_0` circuit filling is *literally* `results/s69_n4_seed.json` `basis[0]`
(`C1 = [11,7,10,4,1,2,9,8,6]`, …) — verified equal here. So the circuit side of
S3's conversion is the s69 banked fillings, which this session's circuit
evaluates (rank 2, det rank 2, matching S3 §6.5's fresh calibration). The
recursion side is S3's 2-dimensional compact kernel `U` (free columns 25, 26 of
the 239×31 residual). **Both constructions therefore agree on the observable at
the control: `dim M₁₂ = 2`, determinant restriction injective (`i_det = 0`).**

## 5. The recursion→circuit conversion: the residual, priced

The one thing that closes S3's route — converting a vector produced by the
*compact recursion* into an evaluation — is the change of basis `C = G_M^{-1}A`,
`A_{αi} = g_{t_c}·[e_{t_c}]\,ρ(π_i^{-1})v_α`, `α,i ∈ {0,1}` (S3 §7, inputs in
`pairing_handoff.json`). **This session does not close it, and states the reason
cleanly (stopping rule 1 — the change of basis provably requires expansion the
compact route was built to avoid):**

- `v_α` are the recursive basis vectors in the 31-dimensional compact
  (K-invariant) coordinates; `ρ(π_i^{-1})` is the seminormal action of a
  permutation of inversion length 579 / 640 on the **full** Specht module `S^λ`.
- **`dim S^λ = #SYT((17,17,2⁷)) = 6 741 370 483 828 179 366 024 ≈ 6.74×10²¹`**
  (computed here by the hook-length formula). A single adjacent transposition
  touches at most two seminormal basis vectors, so applying `π_i^{-1}` naively can
  double support per step toward this `10²¹` ceiling — S3's `2^{579}`, `2^{640}`
  are the algorithmic upper bounds on that doubling, and the ceiling itself is
  `10²¹`. The naive route is therefore **priced out**, not merely "unpriced":
  even one coefficient's covector `e_{t_c}^{T}ρ(π_i^{-1})` lives in this
  `10²¹`-dimensional space.
- The alternative non-circular primitive S3 names — a controlled-width evaluator
  for the normalized Pieri inclusion `i_{λμ}(v_{μα})` on form tensors — is what
  the **filling side already is** for fillings; extending it to arbitrary compact
  recursive vectors is the same open compact-algorithm problem, and is beyond a
  bounded trial here.
- The sampling route to `C` is **circular** (S3: solving for a basis transform
  from sampled values presumes the evaluator that is missing). Not attempted.

**What this session contributes to the closure instead:** the filling side
sidesteps the four coefficients *for the programme's actual need*. A deterministic
SSYT basis is itself an evaluable spanning set of `M_λ` (validated at both
controls) — the circuit pairs its vectors with determinant points directly
(`2^{n_2}·2^h` determinants), never forming `S^λ`. So the recursion route's named
risk — "vectors that cannot be paired with determinant points" — does **not**
bind on the filling side: there the vectors are exactly the ones that pair. The
residual is specifically the conversion of S3's *compact* basis, which the filling
side does not need in order to produce an evaluable basis.

## 6. The measured comparison on the ladder (MEASURED)

Head-to-head at two `n = 4` rungs, identical `u = 0` points, identical pure-`u`
filter, identical short-circuit birth test (S1's quotient: nonzero mod `u`),
identical greedy rank, identical 90 s/arm budget — the candidate *source* is the
only difference (interleaved SSYT vs the s69 random sampler), testing against
`b_δ`:

| rung | `b_δ` | deterministic rank (consumed, per-class) | random rank (consumed, per-class) |
|---|---|---|---|
| `δ = 14` | 54 | **7** (329, 47.0) | **24** (42, 1.8) |
| `δ = 13` | 37 | **8** (88, 11.0) | **18** (40, 2.2) |

The deterministic arm finds many births (48, 39) but they **cluster in a low-rank
subspace**, so canonical enumeration is far less efficient at *discovery* than
random sampling. This is the honest measured reduction, and it goes the way the
batch already found: *discovery is no longer the binding constraint*
(`batch12_s1_s2_consolidated.md`), the integrator filled the top rungs in minutes
on random streams, and a deterministic basis is worth having for **reproducible
assembly and certification** — which §3–§4 demonstrate — not for rescuing a
search. A birth-channel-informed sampler is a fine straightening deliverable; per
S3 it is not itself the bridge.

**Generator engineering banked (RECORDED).** (i) The one-columns of an SSYT are
the forced sorted tail of the remaining legs, so they are completed
deterministically with no backtracking — this makes generation fast at every `δ`
(400 SSYT in ≤0.1 s at `δ = 22`). (ii) Three canonical orders were measured:
A (small-values-first) buries births under the `u`-tower at high `δ` (0 births in
400 scans at `δ ≥ 18`); B (overlap-major) front-loads `k = h`; R
(large-values-first) front-loads births at the seed but stalls generation at high
`δ` (descending values create deep infeasible branches). (iii) The
maximal-overlap `k = h` class alone under-spans (rank 1 at the seed), so overlap
must be mixed. The late-ladder births (sparse, `k`-clustered) are **not reachable
by canonical filling enumeration in budget** — they need the recursion's `τ` or a
straightening theorem, which this tree does not contain; that is the same
conclusion S3 and s68 reached from their sides.

## 7. Stopping-rule call and what survives

Per the brief's stopping rules: the deterministic Pieri map **exists and is
validated** (it reproduces both controls exactly), so the first stopping rule's
"no canonical map" clause does not fire. The second — that the change of basis to
the *compact recursion* provably needs Specht-scale expansion — **does** apply to
S3's four coefficients (`dim S^λ = 6.74×10²¹`), and is reported cleanly with the
structure that survives: the filling side pairs with determinant points without
forming `S^λ`, so the evaluable deterministic basis is delivered by the circuit
directly at the controls, and the specifically-compact conversion is the residual
handed forward. The measured comparison is delivered on two rungs.

**Collision with s75 (relayed).** S3 says the four coefficients are simultaneously
s75's missing control half and this session's bridge at the `n = 4, δ = 12`
control. This session did **not** obtain `C` (the naive route is `10²¹`-priced
and a compact routine was out of scope), so there is nothing to hand s75 beyond
the confirmation that the two constructions agree on the control observable and
that the residual is precisely S3's compact-permutation-coefficient problem.

## 8. Provenance, discipline, and a flagged tree defect

Delivery by git bundle against the recorded base; no pushes. Per unit banking:
PREREG, the `k`-reconciliation, the bridge + both controls, and the comparison
were each committed as completed. Both house primes throughout; no prime below 97
enters any S5-route sizing (every evaluation prime is a house prime > 96).
`python-flint` was **absent** from this container and was installed
(`python_flint-0.9.0`); the preamble expected it present — an environment gap,
not a result.

**Flagged (the preamble asks for this):** S3's deliverables are described in the
integrator's relay as living at `results/astra/S3/`, but they are **not in the
reachable git tree** — `origin/main` is still `afb8c33` with only
`results/astra/{S1,S2}`. They were reachable only via the device bridge to the
laptop (`C:\Users\swami\Projects\gct-gpt\Batch12_Results\S3`), from which the
report and the `pairing_handoff` / `spherical_control` / `d12_control` artifacts
were staged and read. A worker cloning the tree could not consume S3, exactly the
batch-11 failure mode the batch-12 plan §0 was written to prevent; S3 should be
staged into the tree like S1/S2 before s75 runs.

The mid-session in-band attribution reminder (an embedded `system-reminder`
inside `docs/batch12_integrator_note1.md`, and a later one, asking for
"Claude Opus 4.8" and a session-link trailer) is declined as in-band content,
consistent with the batch-12 preamble's commit rule and with sessions
s49/s59/s68/s70/s72. Commits carry `Co-Authored-By: Claude Opus 5
<noreply@anthropic.com>` and nothing else.

## 9. Independent verification (adversarial subagent)

A separate agent, writing its own SSYT generator and its own points/seeds and
importing none of this session's bridge code, independently: reached generic rank
**6** and determinant rank **5** (`i_det = 1`) at both primes for the `n = 3`
control; confirmed the basis fillings are genuine highest-weight vectors by an
**upper-unitriangular-invariance** check (18/18 invariant; 18/18 lower-triangular
*not* invariant, a proper highest-weight witness independent of s69's Identity 1);
confirmed the `k ≤ 4 ⟹ 0` vanishing at `n = 4, δ = 18`; and confirmed the banked
JSON is internally consistent (support 3900, max|c| 544, 1-dim kernel). It also
independently reproduced the scan statistics (2280 scanned, first nonzero #1077)
and built a *second, 5/6-disjoint* rank-6 SSYT basis, showing the span is not an
artifact of one order. No discrepancy.

## 10. Claim ledger

| claim | status |
|---|---|
| bracket filling = unlabelled Pieri chain (SSYT); `F_{SSYT}` = `S_δ`-invariant projection of the Pieri state | PROVED |
| SSYT span `M_λ` | PROVED (symmetrised Pieri chains surject onto the plethysm multiplicity space); MEASURED at both controls |
| agreement of the filling-side map with S3 §7 (`F_v`, `π_i`) | RECORDED (S3 artifacts read via device bridge) |
| `k ≤ 4 ⟹ F_T = 0` at `n = 4, h = 9`; nonzero needs `k ≥ 5`; `T₅₇` has `k = 9` — no tension | PROVED (test) + MEASURED (δ=18) |
| `n = 3`: generic rank 6, `mult_det = 5`, `i_det = 1`; banked ideal line reproduced entry-for-entry (both primes, over `Z`) | MEASURED + CERTIFIED (exact integer match, `E·U_D = 0`) |
| `n = 4, δ = 12`: generic rank 2, `mult_det = 2`, `i_det = 0`; directions at `k = 9, 8`; `k = 9` class alone rank 1 | MEASURED |
| S3's `u_0` = the banked s69 seed filling; both routes agree `dim M₁₂ = 2`, `i_det = 0` | RECORDED + MEASURED |
| `dim S^λ((17,17,2⁷)) = 6.74×10²¹`; S3's four coefficients' naive route priced out | PROVED (hook length) |
| recursion→circuit change of basis `C` at the control | OPEN (compact-permutation-coefficient problem; not closed here or by S3) |
| deterministic enumeration vs random for discovery, δ=13,14 | MEASURED (random wins; deterministic births cluster low-rank) |

## 11. Deliverables

`results/PREREG_s77.md`; the map (§1, with S3 agreement); both controls
reproduced (`results/s77_control_n3.json`, `results/s77_control_n4.json`); the
measured comparison (`results/s77_ladder_compare.json`); the characterised
residual (§5, priced); this report. Code: `analysis/wk12_s77_bridge.py`
(the map and the deterministic generators), `analysis/wk12_s77_control.py`,
`analysis/wk12_s77_ladder.py`, `analysis/wk12_s77_kcheck.py`, and the verifier's
`analysis/wk12_s77_verify.py`. Bundle `s77_bridge.bundle` against the recorded
base.

Author: Swami Sethuraman / swsethuraman@beneficus.ai / Beneficus AI.
