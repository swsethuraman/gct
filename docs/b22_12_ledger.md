# B22-12 — Batch 22 integrator ledger

**Opened:** 2026-09-18, by the integrator session that ran Batches 20 and 21. **Lives at:**
`work\batch15_workers\B15-12\docs\b22_12_ledger.md`, untracked until the next housekeeping
pass. **Governing:** `BATCH22_PROPOSED_BOARD.md` (shaped by the user: slot 1 = the Missing
Theorem and the decisive run; slot 2 = one construction of a length-5–8 equation nonzero on
padding; reviewer last). Same six boxes, same rules.

---

## 1. What this batch cannot produce

No positive multiplicity gap (B22-01's cell is `D = −1`, two lineages). No asymptotic
improvement over LMR. B22-02 *may* produce an equation nonzero on padding — the third of four
achievements, a separation, never the fourth. "No five-row determinant equation known to be
nonzero on padding" stays the phrasing until a certificate exists.

---

## 2. Independently reviewed

Nothing in Batch 22 yet. B22-10 reviews both producers after they report. Everything below in
§§3–4 is producer-only (G18).

---

## 3. Plausible, unproved — who leans on it

| item | status | who leans |
|---|---|---|
| `rank(C|_U) = 2` over `Q` (B22-01.15) | **OPEN** — rank 3 not excluded; would need `P = 524287` to divide every `3x3` minor of the exact integer rows, invisible to a mod-`P` runner | the `Q` form of `arc_target` Prop. 7.1 (B22-01.17, CONDITIONAL) |
| Theorem M's classical inputs: Cauchy, Plücker generation, complete reducibility of `L`, FFT for `SL_3` | UNREAD-CLASSICAL (labelled at the point of use, G14′) | B22-01.3–.4 |
| `b_L(11) = 70`, `b_L(12) = 4` upper halves (inherited from `arc_target`) | the lower halves now have a second lineage (B22-01.8); upper halves still `arc_target` only | Theorem M(ii)'s "spanning = basis" step |
| (T2), EH C1/C3, Ballico | unchanged | as Batch 21 |
| `D45 ∩ P5 = {l·C : C ∈ D35}`? (B22-02 §4) | **OPEN** — the containment `⊇` is proved (block-diagonal identity); equality undetermined | the only constructive route B22-02 left standing (row 13, Nullstellensatz lift) |
| `onset I(D35) ∈ [8, 65]` | ADOPTED record-internal; source "paper 1" UNREAD | B22-02 L6's degree bound |
| Cap theorem at `n = 3` (`cap(3) = 65`) | ADOPTED, modulo Kleiman / Dimca / Gulliksen–Negård | B22-02 L6's right-way clause |

---

## 4. Exact numbers — additions this batch (all producer-only)

**The Missing Theorem holds** (B22-01.7): explicit basis of `F^L_{-1}` (70 typed `ε_3`-contraction
patterns; slots labelled `a, r, c, S, K`; ten `ε`'s closing thirty legs) and of `F^L_{-2}` (4);
`det[F_1^{h_j}(p_i)] = 132757 ≠ 0 mod P` at 70 seeded flag-locus points (two independent
eliminations), top `4x4` minor `136525` — so the 70 points are injective **over `Q` and `F_P`**
(a nonzero modular determinant is nonzero over `Q`). By-product: `dim F^L_{-1} ≥ 70`,
`dim F^L_{-2} ≥ 4` independently of `arc_target` (B22-01.8). On the flag locus each pattern is
one 8-leg contraction — no runner call needed for the basis.

**The decisive run** (B22-01.12–.14): 1050 runner evaluations at the certified points plus 60
controls; G21 controls 6/6, 6/6, 30/30; span control 60/60 (coordinates fitted on the new points
predict 10 held-out recorded values); rank of the 140 rows mod `P` = 2; relation residual 0 on
every row with `(α, β) = (265391, 275398)`; degree-12 ratios `(101007, 295818)` at all 70 points.
**Transcribed label: CERTIFIED-modular.** The five-row mixed-pairing identity holds modulo `P`
as a polynomial identity; `rank(C|_U ⊗ F_P) = 2`; the tops are proportional mod `P`. The `F_P`
form of Prop. 7.1 is PROVED (`n̄ ∈ ker(C ⊗ F_P)`, `C4(n̄) = 499917, 487898 ≠ 0`). **Over `Q`:
OPEN** (B22-01.15). The producer did not use the word "floor" for the rank and said why; the
existence statement was written in §0 before the run, in both forms.

Reopening for the `Q` statement (B22-01 §4.3): exact or multi-prime rows at the already-certified
points, ≈ 10⁴ evaluations, **not priced**; or an untested runner-free alternative — exact
coordinates of `q_3, q_7, n02` by expanding their `ε_4` blocks into typed `ε_3` patterns.

**B22-02 — no equation, no run; six elementary lemmas, all producer-only** (B22-02 L1–L11):

- **Semicontinuity form of the reversal** (L1, PROVED from definitions): a closed condition
  from an integer statistic separates `D45` from a padding point only if the statistic is
  lower-semicontinuous and *larger* on padding, or upper-semicontinuous and *smaller*; every
  singularity-driven statistic fails the applicable test. The prompt's "increases with the
  singularity" clause is satisfiable only by an l.s.c. quantity, and the one on record
  (`dim X_F^∨`) is LMR at `N = 16`, vacuous at `N = 5`.
- **Kernel covariants** (L3, PROVED): anything extracted from a derivative matrix by `r×r` minors
  at the determinant's generic rank `r` vanishes where the rank is lower — padding, at every
  `k = 5..10` computed (instance: `M_7`, ranks 244 padding / 299 P2 pencil, B20-02 §7.3 exact).
  Covers the defect syzygy, the twenty nodes' ideal, the Chow form of the nodes.
- **Nullcone** (L4, PROVED; plethysm row bound UNREAD-CLASSICAL): `l·C` is `SL_5`-unstable
  (`λ(s) = diag(s^{-4}, s, s, s, s)`), so every positive-degree `SL_5`-invariant vanishes on
  `P5` — the uniform form of B19-02's "padding ceiling `U = 0` in `(4^5)`", now for every
  rectangle `((4d/5)^5)`. A covariant `Sym^4 → Sym^t` of degree `e` sends `l·C` to a multiple
  of `l^{⌈(t+e)/5⌉}`; cubic-valued covariants have `e ≥ 7` and send `P5` into `D35`.
- **The window is exactly `N ≤ 8`** (L5, PROVED, self-contained): the rank-6 bound on the second
  fundamental form of a linear section of `det_4` (the LMR right-way statistic) and the rank-36
  bound on the middle catalecticant are vacuous iff `N − 2 ≤ 6` and `N(N+1)/2 ≤ 36`; both bite
  from `N = 9`. The 5–8 window of B18 F2 is not an accident of the record.
- **Restriction to the cubic factor** (L6, PROVED; right-way clause CONDITIONAL on the cap
  theorem at `n = 3`): any separating `f ∈ I(D45)_d` restricts along `l` to a nonzero element
  of `I(D35)_d`, so `d ≥ onset I(D35) ≥ 8` (weaker than the onset conjecture's `> 300`; recorded
  because proved, not because informative). On the cubic side the separation runs the **right
  way**: the size-65 cap minors vanish on `D35` and are nonzero at every smooth cubic. What is
  missing is a lift to quartics; covariant lifts die by L4(c); the Nullstellensatz lift is
  non-constructive and needs `D45 ∩ P5`, undetermined (contains `{l·C : C ∈ D35}`, dim 32).
- **Section discriminant** (L7, PROVED; Bertini UNREAD-CLASSICAL): `Δ_{l·C} ≡ 0`, `Δ_F ≠ 0`
  generically on `D45`.

Kill labels: rows 1, 2, 5, 6, 8, 9 PROVED-kill (record theorems or L2–L7); row 4 PROVED-kill
given the two class values (68 nodal / 24 for `l·C`, B20-02 §4; Teissier SECONDARY); rows 3,
10, 12, the type-specific part of 7, the non-invariant part of 11, the Nullstellensatz part of
13 ASSESSED-kill — *no recipe on record or here; not an impossibility*. Two non-candidates
recorded so nobody re-proposes them: rationality / intermediate Jacobian (separates in fact,
not a polynomial condition); Hessian and polar-map degrees (l.s.c., drop or tie on padding).

**Label-collision note (G-label, PARTIAL on the Batch 20 board):** B22-02 row 1's "Theorems
A/B" are the rank-threshold theorems of the B19-02/B20-02 lineage, not B20-01's Theorem A
(the five-row reduction). B22-10 should read them so.

---

## 5. Gates and slots

| slot | gated on | met? | state |
|---|---|---|---|
| B22-01 | pre-registration before computation (B22-01.2, snapshot hashed `014aa002…`, byte-identical at end); theorem before certificate before run; exceedance pre-approved on handover | all met; the run launched only after §§2–3 were on disk | COMPLETE |
| B22-02 | the gate paragraph (construction + escape from the reversal + non-coverage + price) **before any computation**, or the negative | the negative delivered: 13 candidates, each with its killing sentence, none "unassessed"; 0 of 3 pilots; one-job rule checked before deciding not to run | COMPLETE |
| B22-10 | both producers reported and committed | reported: yes (both); committed: no — PART 10 first | NOT LAUNCHED |

**Housekeeping note, again:** B22-01 §6 says its 16 `.pid` receipts "need `git add -f`". They do
not; PART 8/9 added `!results/logs/bNN_*.pid` negations, and PART 10 does the same for
`b22_*`. `-f` stays forbidden.

**Governance note:** B22-01's session reports "wrote 2 memories" (its own tool memory). Nothing
in the record consumes them; the record is the committed packet. B22-10 should ignore them as
inputs; the successor handover should say producer memories are not part of the record.

---

## 6. Costs

| item | priced | measured |
|---|---|---|
| B22-01 theory + certificate | ≤ 3 pilots | 2 of 3 wrapped launches (pilot 1 failed to certify — the producer's own `mod_einsum` rejected multi-operand path steps, ≈ 22,000 patterns skipped; `_v2` fixed, mathematics byte-identical, 59/59 vectors reproduced; receipt kept) |
| B22-01 decisive run (O4 exceedance) | ≈ 1050 evaluations, ~10 min | **14 wrapped pieces, 507.98 s wall, 1110 evaluations (1050 + 60 controls); largest piece 42.8 s / 278.0 MiB (71% / 54% of caps); no cap hit; no receipt overwritten; no unwrapped numerical run** |
| `Q`-form follow-up | ≈ 10⁴ evaluations, unpriced; or the runner-free expansion, untested | — |
| B22-02 | ≤ 3 pilots, 180 s | **0 launches, 0 s, no unwrapped computation**; reading, text search, hashing, read-only git only (G19 needs no wrapper for these); one-job rule checked (`b22_01_*.pid` absent, 0 python processes, 02:21Z). Ran on Opus 5 (user's choice, Fable credit), not "the strongest model available" as the prompt asked; the reviewer should weigh that where a kill is ASSESSED rather than PROVED |

---

## 7. Completion states

| slot | state | on disk |
|---|---|---|
| B22-01 | **COMPLETE** — CERTIFIED-modular; `Q` OPEN; producer-only | `B15-01\docs\b22_01_report.md` `e2adc0f9adfa98e3…`; `results\b22_01\MANIFEST.json` `1931ab8f45ffe7a9…` (57 files); both sibling packets re-hashed 0 mismatches; HEAD `d5e9d885` unchanged |
| B22-02 | **COMPLETE — outcome (3), gate not passed, the honest negative; producer-only** | `B15-02\docs\b22_02_report.md` `b41e4265809a0187…`; `results\b22_02\MANIFEST.json` `b19d12cdb2ef59e0…` (report + 8 pinned inputs; `numerical_runs: 0`); HEAD `7de65d7c` unchanged; 4 pre-existing 2026-09-13 receipts, nothing new under `results/logs/` |
| B22-10 | NOT LAUNCHED — waits on PART 10 (commits of both producer packets) | — |
| B22-12 | OPEN | this file |

---

## 8. Decisions

### 8.1 Criteria for B22-02, written before it reports (2026-09-18, ~07:30 UTC)

Transcribe only from B22-02's §1 and §5. Four outcomes, one of which is copied:

1. **Gate passed and equation certified** — a polynomial `f` PROVED (not sampled) to vanish on
   `D45` (or the `L`-variable determinant locus, `L ≤ 8`), with its construction and escape
   paragraph in §1, and a certificate of `f ≠ 0` at one exhibited *actual-padding* point
   (`l · C` at `L = 5`; `(z per_3) ∘ T` above). Label: **SEPARATION, producer-only**; the first
   of its kind on the record. The binding constraint changes wording, not status, until B22-10
   confirms. Not a gap. Reviewer next.
2. **Gate passed, pursuit inconclusive** — construction and escape paragraph written and
   priced; three pilots spent without a certificate, or vanishing on `D45` only MEASURED.
   Label: OPEN with a named construction; carry the construction forward as the first item of
   the next board.
3. **Gate not passed — the honest negative** — each candidate considered and the one sentence
   that kills it, in §1. Label: a scoped negative, producer-only; the doors it closes enter the
   next board's "not supported" list by name. This is a complete deliverable.
4. **Cap hit or crash** — recorded as such; not (3).

Any "escape paragraph" that is a survey, or that relies on "unassessed" as a reason, fails the
gate by the board's own rule and is transcribed as (3) regardless of what the report calls it.

### 8.2 B22-01, transcribed (2026-09-18, ~07:15 UTC)

**Outcome: theorem PROVED, set CERTIFIED, identity CERTIFIED-modular, `Q` OPEN.** The
pre-registered sentences: the theorem-proved-and-set-certified sentence applies to §§2–3; for §4
the producer transcribed the modular outcome with the `Q` caveat stated exactly, not the exact
one. Both Prop. 7.1 forms stated in §0 before the run. Everything as §4 above.

**What this is, in one sentence each:** the diagnostic that was PAUSED for seven sessions is now
*decided modulo one prime* — the identity holds there and the candidate survives there; over `Q`
the same statement is one exact computation away and is not made. The `F_P` existence statement
about a source condition is PROVED. Nothing is a gap, a cell, an equation nonzero on padding, or
a separation.

### 8.2b B22-02, transcribed against §8.1 (2026-09-18, ~11:10 UTC)

**Outcome (3): gate not passed — the honest negative. A complete deliverable, producer-only.**
Transcribed from §1 and §5 only. Thirteen candidates, each with its killing sentence, each
labelled PROVED-kill or ASSESSED-kill; no row says "unassessed"; no escape paragraph was
offered, so the survey-escape clause of §8.1 was never engaged. Every candidate the prompt
named appears (rows 3, 4, 5, 7, 8, 9, 12) plus the obvious neighbours (1, 2, 6, 10, 11, 13).
No pilot priced, none run (§1.5, §6). §0 states separation ≠ gap before anything else.

**The doors it closes, by name, for the next board's "not supported" list:** rank thresholds
of any `d_j` (rows 1–2, record); the class and the dimension of `X_F^∨` in the window (4–5);
the hyperplane-section discriminant and anything polynomial in it (6); Milnor-number tangency
loci (7, first half); the Chow form of the nodes or of the surface part of `Sing` (8);
Fitting-ideal and syzygy-covariant forms of `H_1(F)` (9); all `SL_5`-invariants (11, first
half); every covariant lift of a cubic equation (13, first half); the two non-candidates.

**What it leaves open, by name (the residue a future slot may reopen, §4):** row 3 (minors of
size `≤ ρ_j(k)` vanishing for non-rank reasons — still the same open door as B20-02 §8), the
type-specific tangency loci (7), the determinantal-sheaf containment forms (10), Astra's
source-side exclusions routed through `ker φ*` (12), and the Nullstellensatz lift of the
cubic-side cap minors (13) — whose smallest concrete question is whether `D45 ∩ P5` equals
`{l·C : C ∈ D35}`. A reopening needs (i) a membership proof for `I(D45)` avoiding
`r_det`-minors, `SL_5`-covariants into a determinantal locus, and `Δ_F`; and (ii) a stated
reason the value at `l·C*` is nonzero.

**The finding worth keeping (L6):** restricted to padding the separation problem runs the right
way — the reversal is a property of the quartic-side *mechanisms*, not of the problem. Nothing
in this changes the binding constraint's wording: "no five-row determinant equation known to be
nonzero on padding" stands, now with a proved lower bound of 8 on the degree of any such
equation that is trivially below the conjectured `> 300`.

**One-sentence version:** the slot was asked to name one construction that could see padding
as *less* determinantal than the determinant, found that every named or neighbouring
construction either provably cannot (six lemmas) or has no recipe, and stopped without
spending a pilot — which is what the board asked for if that was the truth.

### 8.3 Open for the user

- **The `Q` form.** Two routes: (i) exact or multi-prime rows at the 70 certified points,
  ≈ 10⁴ evaluations, unpriced — an exceedance; (ii) the runner-free route (exact coordinates of
  `q_3, q_7, n02` via `ε_4 → ε_3` pattern expansion), untested, possibly cheap. Recommendation:
  price (ii) first, as a bounded task inside B22-10 or a tiny B22-01b; fund (i) only if (ii)
  fails. Either way the answer is an existence statement in a `D = −1` cell.
- **`D45 ∩ P5`.** B22-02's producer asks whether to fund its determination. Recommendation: not
  as a slot of its own. It is worth one question to B22-10 (is the equality plausible, and is
  the containment `⊇` correctly proved?) and, if the reviewer says the equality is the natural
  expectation, one bounded pilot in a later batch. Even settled, it yields an equation only
  through a non-constructive lift; it is a prerequisite, not a construction.
- **Order of the rest of the batch:** PART 10 housekeeping (commit `b22_01`, `b22_02`, this
  ledger; `!results/logs/b22_*.pid` negation; no `-f`) → B22-10 with pins from
  `B22_COMMIT_RECEIPTS.json` → transcribe → close → a second housekeeping pass for the review
  and the closed ledger.

---

## 9. Observation log (2026-09-18, UTC)

- ~07:10 B22-01 reported COMPLETE; report and manifest staged, hashed; §8.2 transcribed;
  §8.1 criteria for B22-02 written before its report. `.pid` premise corrected again.
- ~11:00 ledger committed to the device (new file, no collision).
- ~11:10 B22-02 reported (02:23Z on its clock); report `b41e4265…` and manifest `b19d12cd…`
  staged and hashed; the manifest's 8 input hashes match the values already on this record for
  `b20_02`, `b20_02b`, `b21_10`, `b20_10`; §8.2b transcribed as outcome (3). Both producers
  complete; the batch waits on PART 10.
