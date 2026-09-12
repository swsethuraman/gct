# Batch 14 — the board, v0.3

**Supersedes the twelve-slot board committed at `325bf521`**, Astra's proposal
v0.1 and v0.2, and the strategy memo at `docs/b14_strategy_memo.md`. Where those
disagree with this file, this file governs. Change log in §6.

Base: **`2ef766cd`** on `main` = `integration/batch13`. Every session branches
from it and delivers by bundle against it.

---

## 1. Read this first

### Figures that are retired

A session quoting any of these is working from a withdrawn number.

| retired | replacement |
|---|---|
| `ℓ(μ) ≤ min(r, δ, 9)` | **`min(r, δ)`** — the `9` was never proved |
| lean builder "1.77–2.64× less memory" | **1.00–2.30×, cell-dependent**; holds on 2 of 12 A1 cells, and 2 save nothing |
| "≥ 1,100 CPU-hours" for the degree-9 remainder | **no figure** |
| 197 degree-9 cells | **99** (47 at `ℓ=7`, 52 at `ℓ=8`) |
| "`a = 1` cells are closed by BIP" | **excluded by convention, not by theorem** — `bip_blind_at_n4` |

### `PROVED.md` entries that changed status

- **`ladder_converse`** now carries `a(κ,p) ≥ 1` and `a(ν,q) ≥ 1`. Without them
  `i(κ,p) = 0` holds vacuously and the product argument has no vectors. All 18
  existing closures stand; a new closure must check the hypothesis.
- **`orbit_stabiliser_silent`** dropped to **MEASURED**. The measurement stands;
  *"not rescued by the full stabiliser"* is withdrawn, because invariants under a
  larger group are an intersection of eigenspaces and a finite extension can
  annihilate them.
- **`bip_blind_at_n4`** is new, and it is why slot 11 is small: the BIP mechanism
  is blind at `n = 4` because its reach is in weight *length* (`≤ 4`) while
  permanent-sensitivity begins at `ℓ = 6`.

### Two rules, both learned the hard way

**Cite `PROVED.md` by id.** Batch 13's largest single waste was three sessions
re-deriving one uncited lemma. Batch-14 *planning* then proposed re-deriving
`bip_blind_at_n4`, which had been proved and measured for two batches. The index
only works if entries are named.

**Every measurement carries a control that can fail.** A1's first pass ran eleven
cells that all returned rank `= a`; nothing in it could have distinguished a
working rank computation from one that had stopped computing. Use
`negative_control_forced` on any evaluation-rank sweep. Astra's v0.1 put the same
rule in its own words — *"a test must actually reach its assertions and must fail
on a deliberately wrong input"* — and two boards arriving at it independently is
why it is stated twice.

### The input contract, as git blob ids

Working-tree checksums differ between hosts by line endings alone; that has now
bitten three times, most recently on the source contract itself. **Blob ids are
identical on every platform. Use these.**

| file | blob |
|---|---|
| `results/b14_prep/points/P13.json` | `76e1f2ed7be8ba85e14ba74cae5be76504f67072` |
| `results/b14_prep/points/P14.json` | `ebb595c0e61b85bbb1d380caa58d90d80ad133f2` |
| `results/s74/source.json` | `ca17e74393228d9c3d9729e7839f0157cb1e21eb` |

**Use a seventh prime at degree 13.** The six-prime product is 186 bits and
`2·H₁₃` is also 186 — sufficient at 1.38× headroom, which is too thin for a
derivation running through the Leibniz definition, the `u`-transport and the `α!`
bound. The seventh prime costs ~13 minutes and takes the margin to ~3×10⁹.
Degree 14 already carries 2.5 million× on seven.

---

## 2. The objective, and why the batch is shaped this way

`D = m_pad − m_det = i_det − i_pad`. At LMR `a = 274`, `m_det = 273` exactly,
`m_pad ≥ 269`, so `D ∈ [−4, +1]`.

**Lemma T changes the priority order** and is the reason eight of these twelve
slots point one way. Multiplication by a highest-weight vector is injective on
each ideal, so **every genuine padded relation at LMR survives to both B13-06
targets** — not three of five. Two consequences:

- the product-image thresholds (391, 529) are **moot** unless `i_pad(24) ≤ 1`
  or `≤ 2`. If `i_pad(24) = 5`, a positive gap at target A needs *four*
  determinant equations at `(63,19,2⁷)₂₄`, where no known module lives;
- so everything turns on one number, `i_red` at rung 13 and then rung 14, and
  that number is certifiable by complete interpolation (Lemma CI).

**Be clear about what this buys.** The route's best outcome is `i_red(14) = 5`,
giving `D_LMR = −4` exactly — a **negative** decision that closes the only cell
with an established determinant equation. `i_red(13) = 0` leaves LMR open. We are
spending the batch's centre of mass on killing our own main candidate, because
killing it cheaply is worth more than sampling around it indefinitely, and
because Lemma T makes the alternatives conditional on the same number.

---

## 3. The twelve

Six need `gcc` + `python-flint` + SciPy together; six do not. Batch 13 found that
split nine-for-nine. Allocate on that line first.

### 1 — flint — mixed-letter evaluator, and a nonzero 73-minor at `P13`

**Inputs** `analysis/wk11_s69_circuit.py`, `analysis/wk12_s74_dpc.c`,
`analysis/wk12_s74_dp.py`, `docs/b13_01_report.md`, `results/b13_01_hpad.json`,
`P13.json` by blob.

Implement initial-column bracket contraction with two letter types — `ℓ` of
valence 1 and `c` of valence 3 — on shape `(9,9,2¹⁵,1⁴)`, which is already in the
evaluator's class. Define the symmetry and coefficient convention for each letter
type separately; the C core may be reused only if the mixed packing is *proved*
compatible, not if it merely runs.

**Success** explicit mixed HWVs and a nonzero `73 × 73` minor on `P13` at both
house primes, with every input definition saved and independently checked.
**Controls that can fail** exact small in-class expansions; weight and raising
checks; a deliberately wrong tensor normalisation must be rejected; multiple
independent directions — a one-dimensional test cannot fail and does not count.
**Budget stop** after the pre-registered directed search plus one deterministic
semistandard pass, record the partial rank without claiming the target complete.
**Fallback** a validated mixed evaluator, the brackets found, and the measured
cost of further spanning directions.

### 2 — flint — exact degree-13 source matrix at `P13`

**Inputs** `results/s74/source.json` by blob, `analysis/wk12_s74_columns.py`,
`analysis/wk11_s69_circuit.py`, `P13.json` by blob.

The 39 native rows with rung `≤ 13`, transported by `msym_u^(13−native_degree)`,
giving the full `39 × 96` integer matrix. **Re-derive the height bound yourself**
— do not inherit it — evaluate at **seven** primes, reconstruct signed integers
only once the modulus exceeds twice your own bound, then compute an exact
rational kernel.

**Success** the exact matrix, rank witnesses, and exact annihilation identities
`A·K = 0` over `ℚ`. **This is a source-matrix result** until slot 1's target
minor and slot 4's recount are accepted; do not label it `i_red(13)`.
**Controls that can fail** a small exact integer evaluator independent of the
fast modular path, agreeing on selected entries; a fresh modular check alone is
not an integer identity proof. **Kill** wrong transport, failed signed
reconstruction, or a failed independent entry check stops that calculation.

### 3 — any — the `complete_interpolation` certificate kind, and a verifier

**Inputs** `docs/b13_03_report.md`, `analysis/b13_03_exact.py`,
`results/b13_03/primary_source.json`, `tools/verify/FORMAT.md`,
`certificate_ceiling`.

Write the certificate specification for Lemma CI and an independent checker.
Establish the target-membership convention and the source pullback inclusion.
Start on B13-03's exact `(8,8,8)₆` control where `h = 1`.

**Success** a checker that accepts the complete control and **rejects** wrong
points, wrong source scaling, invalid target membership, a rank-deficient target,
an insufficient CRT modulus, and a single altered integer entry. It must
reconstruct target entries from bracket specifications, not trust a delivered
matrix. **Fallback** the proved format and a working control checker. No `PASS`
when a required input is absent.

### 4 — stdlib — second-method recounts

**Inputs** `results/b13_01_hpad.json`, `analysis/wk13_b13_01_hpad.py`,
`analysis/wk9_s42_census.py`, `docs/s57_report.md`, `docs/b14_strategy_memo.md`,
`results/b14_prep/ladder_recount.json`.

Four quantities are load-bearing and each rests on **one method and one
implementation**:

| quantity | value | current route |
|---|---|---|
| `dim N₁₃` | 73 | Weyl alternation only |
| `h_pad((25,17,2⁷),14)` | **159** | B13-01's counter, degree generalised |
| `a_∞(19,2⁷)`, `a_∞(21,2⁷)` | 392, 533 | one stable-slice implementation |

Recount each by a **genuinely different** method — character inner products,
cycle-index plethysm, or another explicitly justified route. A second
implementation of the same Weyl formula is cross-checking, not method diversity,
and does not discharge this.

**159 is the priority**: it is the target dimension at rung 14, where `D = −4`
would be decided. **Already done, do not repeat**: the integrator reproduced
390, 391 and 532 on the house `a_weyl`, calibrated against three banked values
(`results/b14_prep/ladder_recount.json`) — but that is reproduction, not method
diversity, and is recorded as such.

### 5 — stdlib — Lemma T, Lemma CI, and bracket adjunction

**Inputs** `docs/s57_report.md` (Lemma L, Prop. S), `docs/b14_strategy_memo.md`,
`docs/b13_06_report.md`, `results/b13_06/components.json`.

Write Lemma T and Lemma CI properly, with hypotheses, into the tree, and add them
to `PROVED.md` — they are currently one session's prose and the batch is built on
them. Then prove **bracket adjunction**: for a horizontal strip `ν/λ`, adjoining
one letter in the strip boxes gives `F_{T′} = Φ_ν(F_T)`.

**The two existing hand checks cannot fail** — both land in one-dimensional
spaces. Validation needs a case where **both spaces have dimension ≥ 2**
(s62/s73's exact `n = 3` determinant vector). Also produce the reachability and
Lemma B bound table over B13-06's 239 components with at most ten rows.

**Success** both lemmas stated and indexed; adjunction proved and validated at
dimension `≥ 2`; the closure table. **Fallback** the lemmas and the combinatorial
table, with adjunction's exact obstruction named.

### 6 — flint — stable bracket evaluator; reproduce 274 / 273 / 269

**Inputs** `docs/s57_report.md` Proposition S, `analysis/wk12_s79_stable.py`,
`docs/b13_07_report.md`, `results/s74/certified.json`.

A stable bracket evaluator: two height-8 columns plus singletons, no 2-columns
and no `u`-tower, letters `Q₂, Q₃, Q₄` of valence 2, 3, 4.

**The decisive step is the reproduction, and it must be able to fail.**
Reproduce generic rank 274, determinant floor 273 and padded floor 269 at the
LMR tail `(17,2⁷)` — **sharing no code with s69/s74**. New code on the same
reformulation is not independent verification of the reformulation. **Kill** the
reproduction fails. **Stretch** the determinant rank on `(19,2⁷)`; a floor of
`392 − p` closes B13-06's best target, `p` being the certified lower bound on
`i_pad(24)`. **Fallback** the evaluator and a complete small control.

### 7 — flint — exact degree-14 source matrix at `P14`

**Inputs** as slot 2; `P14.json` by blob; `results/s74/ladder_ranks.json`.

The `93 × 192` integer matrix from rows born by degree 14, transport exponent
`14 − native_degree`, seven-prime signed CRT on a bound you re-derive.

**This does not wait on slots 1 or 2.** The source half is independent of the
target half; begin with one exact block and measure it. The memo's indicative
seven hours across seven primes is *not* a validated timing and the rung-13 rate
is not a rung-14 rate. **Success** the exact matrix and rational kernel, or a
certified prefix with a reproducible completion plan. **Kill** a bound violation
or a source-control inconsistency stops the arithmetic. A partial matrix's
nullity remains a **ceiling**.

### 8 — stdlib — transport census, the combinatorial half

**Inputs** `results/b13_06/components.json`, `docs/b13_06_report.md`, Lemma T and
Lemma B as slot 5 states them (use the memo's statements if slot 5 has not
delivered — **do not wait**).

All 239 components with at most ten rows: 31 at `δ = 25` and 208 at `δ = 26`.
Deliver reachability, Lemma T exclusions and Lemma B bounds for every one.
Start with the 16 ten-row components at `δ = 25`, which no Cartan product from a
nine-row source reaches.

**Success** the complete combinatorial table. **Stretch**, only if adjunction is
validated: rank comparisons on `U_D ⊕ U_P` at `δ = 25`. **Kill for the stretch**
at every target where the `f`-image survives, a padded image of at least equal
rank survives too. **Zero images from ten sampled points are unresolved**, not
zero.

### 9 — flint — the 58 six-row degree-10 cells

**Inputs** `degree8_global`, `length_bound`, `nchi_2_21_guard`, B13-08's 344
closures, `results/integrate/batch13_reconciliation.json`.

**Demoted, and honestly so.** A permanent-specific equation *raises* `i_pad` and
therefore *lowers* `D`, so a hit here does not advance either objective. The
value is the expected outcome: all 58 empty extends `degree8_global` to degree
10, which is a real theorem and the good direction for `D`. 344 of 402 are
already closed.

**Size before you build.** These 58 have never been built and no `n_χ` is
recorded. B13-08 reports 17 of its 95 degree-10 weights exceed `2²¹`, and two
measured cells in this family sit at 2,422,004 and 2,287,905. At or above the
ceiling you must use `matmul_mod_wide`. `n_χ = N_S/|Stab|` is a lower bound, not
the exact reduced dimension. **Fallback** the sizing table alone is worth the
slot; nobody has one.

### 10 — any — the evidence base

**Inputs** `results/integrate/astra_reconciliation/review_only/results/integration/`,
`unstaged_artefacts.json`, `tools/integrate/scan_unstaged.py`,
`results/b13_09/cert_manifest.json`.

Two counted gaps, one job. **874 uninterpreted result files** — register each as
result / metadata / superseded with its cell key, and fold exact identities,
containment and stability rules and negative results into `PROVED.md` **and**
`inherited_exclusions.json`; a result that excludes a family belongs in both.
**837 absent s79 certificates** — of 2,066 listed, 1,229 are present; classify
each absence as never written, dropped by a size guard, or superseded.
Regenerate what is cheap; record an explicit missing status for the rest. **A
record is not a replay.**

### 11 — any — exclusion audit and the quartic shortlist

**Inputs** `bip_blind_at_n4`, `docs/bip_transfer.md`, `docs/dip_transfer.md` §3,
`docs/n4_gate.md`, `results/integrate/inherited_exclusions.json`.

**Much smaller than the proposals assumed.** `bip_blind_at_n4` is now indexed,
and `inherited_exclusions.json` carries no occurrence predicate at all — its
predicates are length and containment — so the machine ledger never depended on
the convention. The exposure is in prose only.

So: confirm the s37/s52 relabelling reached every prose claim, then build the
deduplicated quartic shortlist at `δ ≤ 8`, `a > 0`, `5 ≤ ℓ ≤ δ`, `λ₁ ≥ δ`, at
most ten survivors with costs. Justify the length bound directly from the
embedding in `(Sym⁴V)^{⊗δ}` and Pieri — **not** by importing a cubic-side
theorem. **Kill** a cell dies only by a valid theorem or certificate; *no known
family lives there* is a funding preference, never an exclusion.

### 12 — flint — `(12,4,4,4,4,4)₈`, the last Q1 cell

**Inputs** `docs/s79_part2_review.md`, `docs/b13_10_report.md`,
`results/b13_10/pilot.json`, `results/b14_a1/report.md`, `build_no_longer_binding`.

The last open cell of s79's Q1 queue, determinant-first on the integrated engine.
`|Stab| = 120` compresses `n_χ` sevenfold.

**Kept deliberately.** The strategy memo abandons it because "no known family
lives there" — that is an absence of mechanism treated as a bound, the same error
class as the withdrawn Theorem E dismissal. Deprioritised, not retired.

**Budget for the kernel, not the builder.** The ≈2.8 GB figure scales from
B13-10's *measured* 1.96 GB build peak, but B13-10 also records the whole cell at
4.53 GB with the **kernel phase binding**. **Control** the already-closed
`(10,6,6,6,2,2)₈` as a reference check only — not as new work.

---

## 4. Why all twelve launch together

**No slot waits on another.** Checked. The strategy memo's allocation had five
slots waiting (07 after 01+02, 08 after 03+01, 09 after 01/02/05, 10 after 06 or
08); Astra caught that and rebuilt every job with an independent core, which is
the standing rule and is why slots 7 and 8 here keep those targets but take the
work that starts from frozen inputs.

**There is no integrator slot.** Integration is continuous and is not a twelfth
of the batch's research capacity.

The final mathematical decisions *do* have genuine dependencies, and those are
integration's problem, not a session's: exact `i_red(13)` combines slots 2, 1, 4
and 3. Exact `i_red(14)` combines slot 7 with a target-14 certificate, the
recount and the verifier. A session that does not receive a handoff finishes and
reports its core artifact rather than idling or promoting a conditional.

## 5. Delivery rules

- **Pre-register before computing** — question, instrument, decision table,
  falsifiers, stopping rules, labelled expectations, committed first.
- **`python3 tools/delivery/check_delivery.py --branch … --base 2ef766cd
  --bundle …` before building the bundle.**
- **Bundle carries the named ref**, with the other workers' tips as negatives.
- **Checksums after the file is in the repository, or ship binary.** Blob ids for
  contracts.
- `Co-Authored-By:` only, in messages and in any script that writes commits.
- Never touch `paper/det3-conductor.tex`, `paper/det4-onset.tex`,
  `PROJECT_NOTES.md`, `docs/boundary_deficit.html`.
- No file over 5 MB; gzip with a README giving original name, size, both
  checksums and the decompression command.
- Bound every run with `timeout` and `ulimit -v`; pid to
  `results/logs/<run>.pid`; **end runs only by recorded id.**
- Distinguish PROVED, CERTIFIED, ADOPTED, MEASURED, CONDITIONAL, NOT REACHED.
- Record the model that actually ran the session.

## 6. Change log from the three inputs

| from | change |
|---|---|
| my `325bf521` board | Tier C was over-built: C1's 521-conversion is not a prerequisite and C2's Pieri coupling is replaced by mixed brackets. The degree-10 frontier drops from slot 1 to slot 9, demoted on the memo's argument. The product-image job is dropped — Lemma T makes its thresholds conditional on the number slots 1–4 certify. |
| strategy memo | Five in-batch dependencies removed. The integrator slot removed. `(12,4,4,4,4,4)₈` restored — its abandonment was an absence of mechanism treated as a bound. The recount widened from 73 to 73, 159, 533 and `a_∞`, since all four are single-method. |
| Astra v0.1 / v0.2 | The BIP audit shrinks to prose-checking now that `bip_blind_at_n4` is indexed. The five-variable elimination and the boundary-regularity slot stay parked. The point contract moves into the tree as blob ids. A seventh prime is added at degree 13. |

## 7. What would make this batch a success

Two of these four would change the position more than another broad collection of
partial searches:

1. **A certified `i_red(13)`** — slots 1, 2, 3, 4 together. `≥ 1` gives `D ≤ 0`.
2. **A certified `i_red(14)` = 5** — adds slot 7, and gives `D_LMR = −4` exactly.
3. **A reproduction of 274 / 273 / 269 by independent code** — slot 6. It is the
   only check that could falsify the stable reformulation the programme leans on.
4. **An independently checkable certificate for a large result** — slot 3, then
   applied. Without it every result above `N_S·a = 3×10⁶` stays producer-attested.

**There is no justified promise of a positive obstruction in this batch.** The
strongest likely outcome is a certified negative at LMR. That is progress: it
converts the programme's central open question from sampled to exact.
