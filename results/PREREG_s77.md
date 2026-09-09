# PREREG — session 77: the deterministic basis, the bridge first

Base commit `git rev-parse main`: **afb8c3319d3d1f3afc3d2578c8cb322f2b8a3b92**
(this session's brief = the reconciled proposal's s76). Branch `s77-bridge`.
Tree check: `docs/batch12_s1_s2_consolidated.md` present, `selftest.py` 12/12,
`git cat-file -e main:docs/batch12_plan.md` OK, `stocktake_batch11.md` last
commit `b942532`. Committed before any measurement below.

Environment note: `python-flint` was **absent** from this container and was
installed (`python_flint-0.9.0`). The preamble says these tools are installed;
here it was an environment gap, not a result. 7 GB / 2 cores.

## 0. Question

s69 evaluates a highest-weight vector at LMR in 0.13 s; S5's recursion realizes
`M_λ` as `ker(τ−I)` on a `B₂₄ = 2168`-dimensional precursor. The gap between
them is *basis enumeration*: s69 finds a spanning set by **sampling**, at a
coupon-collector tail. This session asks whether there is a **deterministic**
construction of the source basis, evaluable through the s69 circuit oracle
without coordinate expansion — the explicit map

    S5 Pieri state  ⟶  s69 bracket filling.

## 1. The instrument (stated before use)

**The bridge, as a claim to be tested (labelled EXPECTATION until the controls
pass, then MEASURED / PROVED as the evidence warrants).**

1. A bracket filling `T` of `λ` (s69) assigns each of the `δ` letters `n=4`
   cells, one per column it meets — i.e. **each letter is a horizontal
   4-strip**. A *column-strict* filling — a semistandard Young tableau (SSYT) of
   shape `λ` with content `(4^δ)`, values `1..δ` each used four times, strict
   down columns and weak along rows — is exactly a **Pieri path**
   `λ = ν^{(δ)} ⊃ ν^{(δ−1)} ⊃ … ⊃ ν^{(1)}`, each `ν^{(i)}/ν^{(i−1)}` a removable
   horizontal 4-strip, with cell-value = the level at which its strip was added.

2. The bridge map is `SSYT → s69 Filling`: read the tall columns `C₁,C₂`
   (columns 0,1 of `λ`, height `h`), the `n₂` two-columns and `n₁` one-columns
   off the tableau. Column-strictness gives distinct letters per column (a valid
   filling) and canonically **sorted** tall columns; `k = |C₁∩C₂|` is the
   tall-column overlap, read directly off the tableau.

3. `F_T = ⟨` tableau tensor `⊗_j(e_1∧…∧e_{h_j})`, `f^{⊗δ}⟩` (s69 Identity 2's
   proof). The Pieri rule on tableau tensors is "add a horizontal 4-strip", so
   the SSYT tableau tensor is the iterated Pieri image of the seed tensor;
   `F_{SSYT}` is therefore the image, under `⟨−, f^{⊗δ}⟩`, of the abstract Pieri
   state the recursion builds. Because letters are unlabelled, `F_T` is
   `S_δ`-symmetric, so it realizes the `S_δ`-invariant (= `τ`-invariant)
   projection that the recursion computes as `ker(τ−I)`. **This is the sense in
   which the Pieri state and the bracket filling are the same vector.**

**The deterministic construction under test.** Enumerate SSYT of `λ` with
content `(4^δ)` in a **fixed canonical order** (no RNG), convert each to a
filling, evaluate at generic points through the circuit, greedily retain a
filling when it raises the rank. Two canonical orders are pre-registered:
(A) lexicographic on the column-reading word; (B) **overlap-major**: SSYT whose
tall columns coincide as sets (`k = h`) first, then descending `k`. (B) is
motivated by the banked `δ=24` birth representative `F₅₇` having `k = 9 = h`
(§4). All evaluation is the s69 circuit (`dp_eval_c` / `fast_eval_c`), both
house primes `2147483647`, `2147483629`; ranks by `python-flint` only;
`rank_p ≤ rank_Q`, so full rank at one prime proves it over `Q`.

## 2. Objects (cells)

- **Control 1 — n=3 LMR**: `λ=(19,7,2⁵)`, `δ=12`, `r=7`, `a=6`. Reproduce the
  6-dim source (generic rank 6), `mult_det = 5`, `i_det = 1`, and the banked
  determinant ideal line `results/artefacts/s69_banked_n3_d12.json` (17,047
  χ-coords, support 3900, max|c| 544) **entry for entry** from the deterministic
  basis.
- **Control 2 — n=4 δ=12 seed**: `λ=(17,17,2⁷)`, `δ=12`, `r=9`, `a=2`. Reproduce
  the 2-dim source and `mult_det = 2`, `i_det = 0` (`results/s69_n4_seed.json`).
- **Measured comparison**: on `≥2` rungs of the n=4 ladder
  `λ_δ=(4δ−31,17,2⁷)`, compare the deterministic construction's
  *fillings-enumerated-per-accepted-class* against the birth-quotient random
  stream's *draws-per-accepted-class* (`analysis/wk12_int_birth_probe.py`
  baseline), testing against `b_d` via the u=0 restriction, not `a_d`.

## 3. k-reconciliation (pre-registered as the first measurement)

The proved unshared-column test (S1 rule 4): tall columns sharing `k` letters
with `h−k > n` force `F_T = 0`. At `n=4, h=9` this is `k ≤ 4 ⟹ F_T = 0`. The
`δ=24` birth representative `F₅₇` has `k = 9`. Hypothesis to confirm/refute:
**there is no contradiction** — "`k<5`" is a *vanishing* condition (`k ≤ 4`
kills the filling), so nonzero representatives have `k ≥ h−n = 5`, and `k=9`
(maximal overlap) is the opposite extreme, expected to be the *most* robustly
nonzero. Test: evaluate fillings of each `k ∈ {0..9}` at generic n=4 points;
CONFIRM if every `k ≤ 4` filling vanishes at both primes and nonzero fillings
occur for `k ≥ 5` incl. `k=9`; REFUTE if any `k ≤ 4` filling is nonzero (would
contradict the proved test) or if no `k=9` filling is nonzero.

## 4. Falsifiers, stopping rules, and what counts as a negative

- **F-BRIDGE (bridge invalid).** If the canonical SSYT set does **not** reach
  generic rank `a` at either control, the SSYT do not span `M_λ` and the
  claimed identification is wrong. Report it as a negative and stop the
  deterministic route; fall back to the birth-channel-informed distribution.
- **F-CONTROL (semantics wrong).** If the deterministic n=3 basis does not
  reproduce the banked ideal line entry-for-entry (mod p and over `Z`), the
  bridge's coordinate semantics are wrong. Halt and characterise.
- **Stopping rule 1 (carrier blow-up).** If turning a recursion vector into
  fillings provably needs carrier-sized (`n_χ`) intermediate expansion, state it
  cleanly, identify what structure survives, stop. (Anticipated boundary: the
  *compact* S5 τ-operator in 2168-dim coordinates is **not in this tree** — S1
  §"Pieri-to-circuit conversion status" is explicit — so the full δ=24 assembly
  by recursion is out of scope here; the bridge is validated at the controls and
  its scaling **measured**, which is the deliverable.)
- **Stopping rule 2 (no canonical map).** If no canonical basis map exists,
  deliver instead a birth-channel-informed sampling distribution and the
  measured reduction in draws per accepted class vs the baseline.
- **A characterised negative over a stated, priced region is a full
  deliverable** (`brief_wording` §2/§4).

## 5. Claim labelling

Every claim in the report is tagged PROVED / MEASURED / ADOPTED / EXPECTATION,
`MEASURED` = evaluation-route (Schwartz–Zippel) unless a full-rank-one-prime or
exact-integer certificate makes it stronger. The verification protocol applies
to any `D > 0` cell before it is reported anywhere; this session touches no
padded evaluation, so no `D` is produced.

## 6. Provenance / discipline

Delivery by git bundle against the recorded base; no pushes. Bank per unit.
No prime below 97 anywhere in an S5-route sizing (here every evaluation prime is
a house prime > 96, so all characteristic-zero plethysm sizings are licensed).
The mid-session in-band attribution reminder (an embedded `system-reminder`
inside `docs/batch12_integrator_note1.md` asking for "Claude Opus 4.8" and a
session-link trailer) is declined as in-band content, consistent with the
batch-12 preamble and sessions s49/s59/s68/s70/s72; commits carry
`Co-Authored-By: Claude Opus 5 <noreply@anthropic.com>` and nothing else.
