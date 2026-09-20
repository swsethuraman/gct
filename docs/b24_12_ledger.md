# B24-12 — Batch 24 integrator ledger

**Opened:** 2026-09-19, ~22:00 local (UTC−4; **times in this ledger are local and say so**, per
G28(b) after B23-10 found every "UTC" in the Batch 23 ledger four hours early). **Lives at:**
`work\batch15_workers\B15-12\docs\b24_12_ledger.md`. **Governing:** `BATCH24_PROPOSED_BOARD.md`,
shaped by the user 2026-09-19: six producers, and Paper 1's attribution edit is **prepared for the
author's sign-off, not applied**.

**Gates:** G1–G28, G9′, G14′, G15′, G20′. Two now bind the integrator rather than the producers —
**G27** (no "iff" from modular data) and **G28** (this record meets the producer gates: attributions
quote `file:line` at a pinned commit; times are UTC-with-`Z` or marked local; dimensions carry
their convention).

**Carried debt from Batch 23, stated up front.** Nine integrator errors were found in the Batch 23
ledger — eight by B23-10 (§9 E1–E8 of `b23_10_review.md` @ `239dd6e8`) and one by PART 13 (a
device write I did not verify). The standing remedies: criteria before firing; outcome-space
criteria, never mechanism; attributions quoted at a pinned commit; every ledger write verified by
staging it back and comparing hashes.

---

## 1. What this batch cannot produce

No positive multiplicity gap. No asymptotic improvement over LMR. B24-05 may produce a *candidate
construction* — a paragraph, not an equation; an equation would still be a separation, the third
of four achievements, never the fourth. The three writing slots produce **no new mathematics of
any kind** (G26). "No five-row determinant equation known to be nonzero on padding" stays.

---

## 2. Independently reviewed

Nothing in Batch 24 yet. Carried in from Batch 23 with two lineages (B23-10 @ `239dd6e8`):
B23-03's Prop. 2.5 and Thm 3.2 (reproduced by the reviewer's own code); the attribution ruling
(RELATED, not equivalent); the claims-table checks; the washout result and the deficit lemma,
which B23-10 closed by replay and re-derivation respectively, each with named residues.

---

## 3. Open, carried forward

| item | status | who leans |
|---|---|---|
| Row 1 at `N = 5`, `k ≥ 7` | leans on **Kleiman**; one cheap pilot removes it (B23-10 §3.2) | Paper 3's "unconditional across the window" sentence |
| C45 — the `n = 3` positive control's dependence on LMR, **no read-status recorded for that use** | **OPEN**, ranked 1 of the remaining lineage gaps | Paper 3's evidence that the instruments work |
| C24 — the Astra five-block theorem | **OPEN**, ranked 2 | Paper 3 |
| G-A1 — the boundary of `D45°` meeting `P5` | **OPEN**; a smooth `l·C*` there kills the right-way corner | the cubic-side lift. Deferred to Batch 25 |
| Row 2, `2 ≤ j ≤ N−4` | **OPEN**, priced by B23-03 §3.3 | deferred to Batch 25 |
| `dc̄(per_3) ∈ [5, 7]` | OPEN in the published literature | whether `(3,5)`, `(3,6)` hold anything |
| Small-tail cells | **OPEN, unpriced** | every feasibility estimate |
| Can the three-kinds summary be a theorem? | ASSESSED-only, producer-labelled "not a theorem" | deferred to Batch 25 |

---

## 4. Exact numbers — additions this batch

**B24-04 — all three questions answered; the small-tail door is shut by a theorem**
(producer-only; three pilots, three pre-registrations, sealed manifest; **50.5 s of 180 s**, all
wrapped, under 152 MiB against the 512 MiB cap; HEAD `feed104e` unchanged, zero tracked changes;
one-job rule checked before each launch):

**Question 1 — ANSWERED, negatively, by a theorem.** I rated this the most important unpriced
question on the board. It is now closed, and it was not close.

> If a cell's tail `t` is below its degree `d`, then at least `d − t` of the `d` exponent vectors
> in every weight-`λ` monomial must equal `n·e₁`, so **every weight vector factors as
> `c_{n e₁}^{d−t} · g` with `deg g = t`**. Since `I(D_r^{det_n})` is prime, `P_r` is irreducible,
> and `c_{n e₁}` vanishes identically on neither, **the separating property passes intact through
> the factor.** Hence every separating cell has tail `≥ D*`, the onset degree, and every
> separating equation is `c_{n e₁}^k` times one whose cell has tail equal to its degree.

**The cheap small-tail cells are the old low-degree cells in disguise, and they are empty.** No
separating equation can live in one. The hope was that structure might beat size; it does not,
because the structure is a disguise.

**It also replaces B23-06's two candidate prices — neither was right.** The minimum `N_S` grows
structurally like `0.060·t⁴` (partitions into parts `≤ n`). The programme's reach of
`N_S ≲ 2 × 10⁴` is `t ≈ 24`; at the tail 900 that Conjecture 2 forces, the figure is
**≈ 4 × 10¹⁰ — six orders of magnitude from reach, not the 10¹⁵⁰ the record has been carrying**.
Labelled **EXTRAPOLATION**, correctly: it evaluates a fitted quartic 37-fold outside its measured
range. Six orders is still out of reach, but it is a different kind of out of reach, and the
record should stop quoting `10¹⁵⁰`.

**Question 2 — the published result does *not* price Question 1.** Bläser–Dörfler–Ikenmeyer
Thm 7.2 prices **one evaluation of one HWV, never existence**. Small tail *does* imply small
treewidth (`τ ≤ λ₂ + |λ̄| − 1`, proved here), but **the converse fails outright** — `λ = (k,k)`
admits fillings with `τ = 2` and unbounded tail — and their graph is built from the **tableau's
entries**, so treewidth depends on the *filling*, not on `λ`. So the two phenomena are not the
same, and my hoped-for equivalence was wrong.

**A delegated reader returned a wrong gloss, in the direction that would have flipped the
ruling** — "edges depend on the shape only, not the filling". The producer re-checked and caught
it. **Governance point for the next board:** a delegated read is not a read; B23-10 used three
helper agents and checked their findings by hand, and this slot shows why that check is not
optional.

**The live corner that remains is new:** **large tail with small treewidth** — unpriced, and a
question about *fillings* that the record has never asked.

**Question 3 — the expected negative, with exactly one grading, and a verdict on the basis.**
The 70 patterns carry one grading only: the multidegree, `F^L_{-1} = 7 ⊕ 31 ⊕ 28 ⊕ 4`, a genuine
`L`-stable direct sum — **but all four blocks share `α⁵β⁵c¹⁵`, and both ends of the range are
forced by structure**, so it is not a charge in the Kostka–Foulkes sense. Seven further statistics
tried; **ten of eleven candidate classes PROVED trivial**, one survives as MEASURED and would not
be a grading even if confirmed.

**And the basis is not canonical.** It is a **seeded greedy selection from a vastly larger
spanning set**. So the Missing Theorem is **bespoke and must be re-proved per cell** — the
uniformity I hoped for is not there. Unresolved and honestly flagged: the `s_rep = 0` candidate
(400 directly-sampled patterns span 6 of 7), with the `Y ↦ Yᵀ` involution named as the first thing
to try. Housekeeping: "negation missing for `b24_04_`".

**B24-06 — Paper 2 assessed: sixteen blockers, four of them mathematical errors**
(producer-only; `PAPER2_BLOCKERS.md` `00e3ebbeccfda6d2…`; paper `7c2bc7365c3aacc7…` **byte-identical
to HEAD** — no repair, as instructed; HEAD `82633a60` unchanged, nothing committed; 3 h 10 m).

**My stocktake's six candidates, verified against the source: four real, one already fixed, one
misdescribed — and nothing invented.** Better than the Paper 1 brief, where three items were
wrong. The garbled Prop. 2.1 formula is real (**and there is a second garbled clause in Lemma 3.3
that I missed**); the "empty `\cite`" is really `\cite[\S]{Companion2}`, a locator with no number;
"second author" is real but in §1, not the abstract; the Thm 6.2 / Rem. 6.3 tension is genuine;
the LMR range does need `[−4,−2]`; and the `n = 3` positive control **is already absorbed**.
**The stocktake itself is unreachable from that worktree**, so the six were checked against the
paper rather than against my document — which is the right way round.

**Four mathematical blockers my stocktake could not have known:**

- **B1 — Corollary 5.3 states the Kadish–Landsberg bound backwards**, where the record and the
  paper's *own* Cor. 5.2 give 0.
- **B2 — Theorem 9.1 is false as stated.** It quantifies over *every* degree, but
  `dim D^det_4 = 34` in `dim W_4 = 35` (the paper's own Prop. 2.1 table), so `I(D^det_4)` is
  principal and **nonzero**, and `mult_det < a` at and above its generator's degree. The paper's
  own proof knows this — it says "for the degrees in question", which is not the statement's
  quantifier. `blindness_slab.md` Theorem A splits it correctly at `e = onset I(D_4^{det_4})`,
  `e ≥ 10` certified, `e = 320112` ADOPTED. **The conclusion `Δ ≤ 0` survives** via the paper's
  Prop. 6.1, which is a containment and therefore degree-free.
- **B3 — "length `≥ 6`" is the wrong gate and contradicts the record.** At `r = 5` the paper's own
  Thm 3.1 gives `P_5 = R_5`, so `Δ = Δ_R` there and **a positive `Δ_R` at `ℓ = 5` is an
  obstruction**. The record's gate is `ℓ ≥ 5`, and that is exactly where the open region lives:
  of 2,734 labels with `a > 0`, **2,571 are still open**. The washout's real content is about
  *interpretation*, not existence.
- **B4 — `Δ ∈ [−4, +1]` is stale** against the committed `[−4, −2]` (CERTIFIED, conditional on
  ADOPTED `dim N₁₃ = 73`). The substantive loss: the paper leaves `Δ = +1` on the table **at the
  one cell where the programme has excluded it**.

**And the Paper 1 failure mode again, twice over (B5, B6).** LMR is load-bearing **four times**,
and **Beauville has no read-status anywhere on the record** while being the standard source for
Prop. 2.1, Thm 7.1 Step 2 and Thm 7.3. Eleven further blockers are corrections and stale labels.

**Overlap with Paper 3, reported not resolved — and the sharpest item is a coherence defect:**
the cap theorem is carried **flatly** as Paper 2's Thm 7.1 and as **ADOPTED modulo Kleiman, Dimca,
Gulliksen–Negård** in Paper 3's C11. *The same theorem is shipping under two different labels in
two companion papers.*

**The integrator compiled it, which closes the slot's one unfillable hole — and found two more
defects.** With TeX Live here: **12 pages**, citations resolve on a third pass (all 16 `\bibitem`s
present and used — the undefined-citation warnings were an artefact of the first pass aborting),
**but two genuine `! Double superscript` errors remain**, at source lines **144** and **874**, both
`$I(\Ddet_r^{\per_3})...$` — `\Ddet` expands to `D^{\det}`, so the `^{\per_3}` is a second
superscript. **The paper does not compile cleanly.** These are separate from B9's two garbled
formulas and should be added to the blocker list.

**B24-01 — Paper 1's five blockers cleared or prepared, and a second piece of prior art found**
(producer-only; HEAD `bbd1d12e80ae162feb368f75c9c270ccf79747f8` unchanged, clean at start,
nothing committed; session ran 3 h 32 m):

**The three contradictions, with the direction of each error settled from the record — and in
both decidable cases the *paper* was wrong, not the record.**

- **Line 617 (G-S1):** the totals law became a theorem in session 22 (`PROJECT_NOTES.md` L422);
  the "verified and not proved" sentence predates it. Now reads as a theorem whose proof consumes
  Lemma 5.6's two inputs as given.
- **`m_2 = 9` (G-S3):** the paper said the Hüttenhain–Lairez derivation "is the obvious next step
  and we have not carried it out"; **session 10 of `boundary_deficit.html` ran it.** The paper now
  reports what was run *and why it does not upgrade the label*: the degeneration pins only the
  product `m_2 · c = 18`, and the observed contact `c = 2` is exactly what that product forces
  from `m_2 = 9` — **the two determinations lock each other**. `m_2 = 9` stays *computed*, not
  proved, and G-A6 records that the HL route is spent.
- **The refutation count (G-S2):** counted, not hedged. The two numerals were **measuring
  different things**, which is why they never reconciled: Remark 5.11's scope is the functional,
  where the answer is **two** — (c) was never pre-registered, it was killed by a degree count —
  and §7's scope is every pre-registration, where it is **five**. `README.md` matches both. K10
  ("(b)" → "(a)") applied alongside.

**Blocker 5 — all four read, all four decided, none dropped. Two turned up more than expected.**

- **LMR is prior art for a second thing.** Beyond being the "other means" after Cor. 4.13 — where
  "classical" was simply wrong, since Mignon–Ressayre is for `dc` and the best prior `dc̄` bound
  was *linear* — **their Prop. 3.5.1 already constructs the paper's boundary component `P_2`, for
  every odd `n`**, and the Hüttenhain thesis says so itself. Now cited in both places. **This is
  the second unattributed construction found in this paper, and both surfaced only because someone
  read the source in full.**
- **The Hüttenhain thesis contains no invariant computation for the `det_3` orbit closure at
  all**, so the collision B23-05 feared is not there. Its `det_3` chapter is the CRAS paper plus
  two extras; now cited rather than gestured at.
- **IK Lem. 5.2** was right in substance and **missing a hypothesis** — the odd-`D` side condition
  `C(2(D−1), D−1) ≥ 2(m−1)`, now stated.
- **Kumar (Compositio)** cited in §1: his results assume `n` even and Alon–Tarsi, and `n = 3` is
  odd — the excluded case.

**Left open and not edited (G-P4):** Remark 4.14 credits the product-of-variables statement to
`\cite{KumarCMH,KL}`, but IK credit it to the Compositio paper. Resolving it needs a read this
pass did not do. Correctly left alone rather than guessed.

**Blocker 1 — prepared, unapplied, as the user directed.** `ATTRIBUTION_PATCH.md` carries
B23-10 §4.4's wording **verbatim**, the exact current and proposed text for all three passages,
the ruling with its commit, and a diff that **`git apply --check` confirms applies cleanly**.
`paper/det3-conductor.tex` contains none of it.

**Verification:** 12 `.tex` hunks and 4 `README` hunks, one ledger row each; braces balanced, `$`
parity even, every `\ref` and `\cite` resolves, every `\bibitem` cited, and **the theorem counter
is byte-identical to HEAD (52 environments)** — so no cross-reference in the record moves. Not
compiled: no LaTeX toolchain on that machine, and `READINESS.md` says a `pdflatex` run is owed
before posting. **The integrator has a toolchain and has compiled it; see §8.0c.**

**B24-05 — the `D`-module strand: both sub-candidates dead, and one new exclusion gained**
(producer-only; report `e13ad0f1d8cab936e…`, staged and hashed here; **0 of 3 pilots — no
numerical job launched**; HEAD `82633a60` unchanged, git read-only, nothing committed).

**The idea was the integrator's, and it is refuted.** Not softened — refuted, with the mechanism
named. Both sub-candidates **did** clear the bar I set them, and then died elsewhere.

**Sub-candidate A — `b`-function root integrality.** It **survives death 2**: `b_F` genuinely is
*not* an `r × r` minor of a matrix polynomial in `F`, so it escapes Lemma 1.3, and it is not an
`SL_5`-covariant into a determinantal locus, so it escapes Lemma 1.4. Lemma 1.2 does not even
apply, since `b_F` is not a polynomial in `F`. **It dies on death 3, provably** — the one I named
as "prehomogeneity is about the orbit, not the closure". The `b`-function is a `GL`-invariant, so
integrality is an *orbit* property, and the closure does not inherit it: `x_{11}^n ∈ Det_n`, and
**Lemma D1** (derived from scratch, no citation) gives `b_{x_1^k} = Π_{i=1}^{k}(s + i/k)` — the
fractional roots are already inside the closure. Four further independent kills follow, of which
the sharpest: the record's `D45` is a **five-variable section**, so Cayley computes the wrong
object, and `x_1^4 ∈ D45` already carries roots `−1/4, −1/2, −3/4`.

**Sub-candidate B — characteristic-cycle multiplicities.** It escapes Lemmas 1.3 and 1.4 exactly
as I hoped, and **dies on Lemma 1.1 — the very lemma I claimed it would sidestep.** The reason is
clean and I should have seen it: the multiplicities *are* transverse Milnor numbers
(upper-semicontinuous, **larger** on padding) and polar degrees (lower-semicontinuous, **drop**;
their alternating sum is the class, 68 against 24). **"A characteristic cycle contains no number
that is not a threshold on a semicontinuous integer statistic."**

**The by-product, which is worth more than the idea was — Corollary D2′ (PROVED):**

> Every `GL_N`-invariant property that holds at `det_n` and **fails at a pure power `x^n`** is
> **orbit-only**, and yields no closed condition containing `Det_n`.

It follows from **Lemma D2** (`x_1^4 ∈ D45`, in the image not merely the closure; `x_{11}^n ∈
Det_n` for every `n ≥ 2`). It disposes in one line each of integrality, prehomogeneity,
rational/klt/canonical singularity conditions, and "`X_F^∨` is a hypersurface". **This is a new
exclusion of the same kind and scope as Lemmas 1.3 and 1.4**, and it is what the integrator's idea
actually yields once written down properly. It belongs in Paper 3.

Also **Lemma D3** (PROVED, conditional only on Cayley and the global-`b`-is-lcm-of-local sentence,
both PRIMARY): `{lct ≤ c}` is vacuous once it contains `Det_n`; and the minimal exponent is 2 on
the determinant against `≤ 1` on padding, so `{α̃ ≤ c}` containing `Det_n` contains padding too —
Lemma 1.1, wrong direction.

**The literature pass found nothing**, so the cheap exit was unavailable and the gate had to run.
It did supply the sentence the candidate needed and never got — Ikenmeyer–Kandasamy (PRIMARY,
fetched): *"Understanding the difference between group orbits and their closures is a key
difficulty in geometric complexity theory."* **Stated limit:** four queries is not an absence
proof, and PDF text extraction was unavailable, so every quote came from HTML renderings.

**A correction to my brief (G16).** Caracciolo–Sokal–Sportiello state Cayley's identity as
`b(s) = s(s+1)···(s+n−1)` in the `f^s → f^{s−1}` convention. **My brief's `(s+1)···(s+n)` is
correct only after the convention shift**, which the report makes explicit. Tenth integrator
error; a convention I asserted without checking.

**The `z_ρ` argument, re-derived — and the universal claim is false as literally stated.** The
producer re-derived it as instructed, recorded the universal claim ASSESSED, and **did not adopt
it**: the statistic `st ≡ 0` trivially returns `g` itself, so "no statistic on conjugacy classes
can work" overreaches its own argument. The unverified session is cited nowhere as a premise
(G9/G9′). I flagged the overreach; the producer found the counterexample.

**B24-02 — C24 closed, row 1 made unconditional, and C45 turned into a much sharper problem**
(producer-only; report `cf09c536cf1fb4ab6…`, staged and hashed by me because the relay was
truncated at the finding; 7 files, 13 pinned inputs, 0 mismatches; HEAD `cc14e88c` unchanged,
read-only git, nothing committed).

### The finding: the programme's only positive result rests on an unread theorem, and it rests on it for the *sign*

The `n = 3` positive control — the unpadded cell `(19,7,2⁵)` at `δ = 12` with `D = +1` — is what
Paper 3 offers as evidence that the instruments work at all. B24-02 replayed its **structural**
half exactly by hand (LMR's printed weight `Ω(4,3)` expands to `(19,7,2⁵)`, `ℓ = 7`, `|λ| = 36`,
`δ = 12`). The rest cannot be replayed away, and the reason is sharper than "no second lineage":

- `i_det = nullity_Q`, and a modular nullity satisfies **`nullity_p ≥ nullity_Q`**. So the
  measured `nullity_p = 1` proves `i_det ≤ 1` — **a ceiling**.
- `i_per = 0` *is* genuinely proved over `Q` (a nullity-0 certificate at one prime forces
  `nullity_Q = 0` — the direction that does work), so `D = i_det`.
- Therefore **the numerics alone give only `0 ≤ D ≤ 1`**, which is not a positive result at all.
  **The entire sign comes from LMR's floor `i_det ≥ 1`.** No extra prime, no sharper numerics, no
  fresh evaluation family can supply it: the inequality runs the wrong way for the instrument.
  Only an exact rank over `Q`, a proof of ideal membership, or LMR can.
- The record-internal alternative is **incomplete and the record says so**: `U_D` vanishing at 32
  determinant pencils exactly over `Z` is Schwartz–Zippel evidence, not membership (s73 §3;
  s62 §206, in their own words).

**And the statement in play is not the one anyone thought.** It is **LMR Theorem 2.3.1** plus the
paper's printed worked instance — *not* Thm 1.0.1 (`dc̄(perm_m) ≥ m²/2`). Read-status at the point
of use: **none. No label, no file, no hash anywhere in the record.** `equation_census.md`
(sha256 `ba7b20f9…`) contains zero occurrences of PRIMARY, SECONDARY, UNREAD, read-status, ar5iv
or any sha256 — it is a session-55 document predating G14/G14′. The two LMR labels that *do*
exist are for **different theorems**: B23-06 has PRIMARY for Thm 1.0.1 (arXiv 1004.4802v1 PDF
sha256 `cfc28275a8c6b27f…`), and B22-02 has UNREAD-SPECIALIST for the dual-defect statistic,
explicitly not load-bearing there.

**In fairness to session 55**, the producer notes the census shows strong internal evidence of a
genuine reading — it quotes the printed `Ω(k,d)`, cites the printed Thm 1.0.2 and its `n(n−1)`,
identifies the printed partition, and flags an inconsistency *between two printed statements*,
none of which is obtainable from an abstract. The honest label is not "nobody looked" but **the
reading was never recorded**, and under G14′ it cannot be certified PRIMARY after the fact.

**Accurate label for C45 today: PROVED modulo LMR Thm 2.3.1 at this cell, read-status UNREAD.**

**Price to close: one reviewer-hour, no pilot.** Fetch arXiv 1004.4802v1 — already hashed on the
record by B23-06 — read Thm 2.3.1 and the worked instance, record PRIMARY at the point of use, and
confirm two things in the text rather than assuming them: (i) the module is non-vacuous at
`N = 7`; (ii) `D_7` lies in the dual-degenerate locus the theorem concerns at `k = 4`.

### C24 — the Astra five-block theorem: **PROVED, two lineages. G-23 closed.**

Lemma 7.1, (7.2), Thms 8.1/8.2 and Cor. 8.3 re-derived from the definitions by hand; `β = 2`,
`u = 0`, `h = −1`, `m = 0`, `L = 2` reproduced from scratch for the old arc. The two steps the
original report compresses to one line each — including the interval-covering in the sumset —
both survive being written out. Verbatim scope limit carried forward.

### Task 3 — the `N = 5` Kleiman pilot: **PASS**, one pilot, 0.194 s of 300 s

Padding ceiling against determinant floor at `N = 5`: ties `5 / 25 / 75` at `k = 3,4,5`; then
ceiling `146 / 245 / 386 / 579` against floor `165 / 299 / 475 / 691` at `k = 6,7,8,9`; `F_0`
beyond. **Every pre-registered prediction hit, including three negative controls**
(`D(7,8,9) = −17, −11, −2`), which is what makes the pilot informative rather than confirmatory.

**Row 1 is now a PROVED-kill on elementary premises across the whole window `N = 5..8`** — no
Kleiman, no Dimca, no Gulliksen–Negård, no depth sensitivity. **Paper 3 can write that sentence.**

---

## 5. Slots, gates and state

| slot | worktree | gated on | state |
|---|---|---|---|
| **B24-01** Paper 1 blockers | `B23-05` | met — patch prepared and unapplied; `git apply --check` clean; paper untouched | **COMPLETE — outcome (1)** |
| **B24-02** C45, C24, and the `N = 5` Kleiman pilot | `B15-01` | met; G25 satisfied — the prereg hash is the first thing written, before `import flint`, with abort-on-mismatch | **COMPLETE** |
| **B24-03** Paper 3 corrections | `B23-04` | **unblocked 2026-09-19** — B24-02 reported. Two of its instructions now resolve: row 1 **is** unconditional at `N = 5`, and C45's label must become "PROVED modulo LMR Thm 2.3.1, read-status UNREAD", with the note that the dependency carries the **sign** | READY |
| **B24-04** small tail, crystal basis, charge | `B15-02` | met; three pre-registrations, three wrapped pilots | **COMPLETE — outcome (1), all three answered** |
| **B24-05** the `D`-module strand | `B24-05` | gate run in full; literature pass first, as instructed; 0 of 3 pilots | **COMPLETE — outcome (2), the honest negative, plus one new exclusion** |
| **B24-06** Paper 2 assessed | `B24-06` | met — paper byte-identical to HEAD; 16 blockers, claims table, gaps, readiness | **COMPLETE — outcome (1)** |
| **B24-10** review | `B15-10` | all producers reported and committed | NOT LAUNCHED |

One numerical job across the batch. Only B24-02 certainly has one; B24-04 and B24-05 may.

---

## 6. Costs

| slot | priced | measured |
|---|---|---|
| B24-01 | no computation | none; 3 h 32 m. A `pdflatex` run is owed before posting and was done by the integrator (§8.0c) |
| B24-03, B24-06 | no computation | — |
| B24-02 | 2 replays + 1 pilot | **1 pilot, 0.194 s of 300 s, exit 0, no cap hit.** "Negation missing for `b24_02_`". Two self-corrections disclosed: a `head -6` pipe silently truncated the first seal via SIGPIPE (caught, re-run clean); and the count of interpreter launches was understated twice as verification grew — now all five listed with full text, with the flint version probe flagged because it imports beyond stdlib. **Judgment call disclosed:** Task 1's a-ladder and nullity computations would have consumed the batch's single numerical job, so it went to Task 3 per the brief's ranking, and §2.2(d) states what was not replayed |
| B24-04 | ≤ 3 pilots, after the gate | **3 of 3, 50.5 s of 180 s, under 152 MiB of 512 MiB.** "Negation missing for `b24_04_`" |
| B24-05 | ≤ 3 pilots, after the gate | **0 of 3 — no numerical job launched.** No `b`-function computed, attempted or priced (out of scope by the brief). Housekeeping: `.gitignore:51` negation moot — no receipt exists. Session ran 3 h 22 m |

---

## 7. Completion states

*(all NOT LAUNCHED; filled as slots report)*

---

## 8. Criteria, written before any slot fires (2026-09-19, ~22:00 local)

**Written as outcome spaces, never as mechanisms** — the lesson of Batch 23 §§8.5, 8.7.

### 8.0 B24-02, transcribed against §8.2 (2026-09-19, ~23:45 local)

**Outcome (2), exactly as pre-written: "closed with residue, or one of the two needs new
mathematics… a gap that cannot be closed by replay is a finding, not a failure."** C24 closed with
two lineages; C45 not closed but **sharpened and cheapened**; the pilot passed, which is
outcome (1) for that task.

**What makes this the batch's most consequential result so far.** The gap was filed as "no second
lineage". It is worse and better than that. Worse: the dependency carries the **sign** of the
programme's only positive result, and no instrument on the record can replace it, because a
modular nullity is a ceiling and the sign needs a floor. Better: the target is now identified
exactly (Thm 2.3.1, not Thm 1.0.1), and the PDF is already hashed on the record, so the fix is
one reviewer-hour rather than the B22-01-sized job B23-10 priced.

**The convergence to exploit immediately.** B24-01's blocker 5 already sends it to **arXiv
1004.4802** — the same paper. If it is still running it can record PRIMARY for Thm 2.3.1 at the
point of use and close C45 at zero marginal cost; if it has finished, this is a half-slot, not a
slot. Either way **C45 should not wait for Batch 25**.

**Discipline worth noting.** The producer disclosed a SIGPIPE truncation it caught and fixed, and
corrected its own count of interpreter launches twice as verification grew rather than letting the
first number stand. It also stated plainly which computations it did *not* replay and why. That is
the behaviour the gates exist to produce.

### 8.0b B24-05, transcribed against §8.5 (2026-09-20, ~03:00 local)

**Outcome (2): the honest negative, with each sub-candidate and the sentence that kills it.**
Outcome (3) was unavailable — the literature pass found no prior work, so the gate had to run in
full. Exactly the shape §8.5 anticipated, and the criteria's warning held: *"the idea is the
integrator's and unassessed; a slot that adopts it uncritically has failed the gate."* It did not
adopt it. It refuted it.

**What I got right and what I got wrong, since this was my idea.** Right: both sub-candidates
genuinely escape Lemmas 1.3 and 1.4 — the first candidates on the record to do so — and death 3
was the real risk for A, as I named it. Wrong: I claimed B would sidestep Lemma 1.1, and it is
killed by Lemma 1.1, for a reason I should have seen without a slot — a characteristic cycle is
built from Milnor numbers and polar degrees, and both are semicontinuous integer statistics
pointing the wrong way. And I asserted Cayley's identity in a convention I had not checked.

**The slot converted a dead idea into a live lemma.** Corollary D2′ is the deliverable: a pure
power lies in every determinantal orbit closure, so any `GL`-invariant property that holds at the
determinant and fails at `x^n` is orbit-only and can never give a closed condition containing
`Det_n`. That is a general exclusion of the same scope as Lemmas 1.3 and 1.4, it kills four named
families in one line each, and **it exists because the idea was wrong in an instructive way.**
**Route it to B24-03 for Paper 3** — it strengthens the blindness chapter rather than merely
adding another dead candidate to the table.

### 8.0c B24-01, transcribed against §8.1 (2026-09-20, ~03:30 local)

**Outcome (1): all five cleared or prepared.** Paper 1 is **submission-ready pending the author's
signature on one patch**, plus two citation decisions (G-P4, G-P5) and two offered framing
additions (G-P2 and a new G-P3). The open mathematics — Remark 3.3, attainment, `m_2 = 9`,
primitivity — is untouched, as the brief required.

**Element of outcome (3) too, and it is the one to notice.** §8.1 said *"a blocker turns out to be
wrong — transcribe the correction first; B23-05 and B23-10 are both fallible and so is my brief."*
Two of the three contradictions resolved **against the paper**, which is the direction that
matters: the record was right both times and the paper carried the stale sentence. And the
refutation count was not a contradiction at all — two numerals measuring two different scopes.
That is a better answer than either "fix it" or "hedge it".

**The second prior-art finding changes how I read the first.** LMR Prop. 3.5.1 already constructs
the paper's boundary component `P_2`. With the bracket census, that is **two** results presented
as the paper's own that were already published, and **both were invisible until someone read the
source rather than the abstract**. The lesson is not about this paper; it is that G14′'s
read-status labels are doing real work, and that "cited" and "read" have been different things on
this record more often than anyone assumed.

**Still owed on C45, and it is smaller than it was.** B24-01 read LMR — but for Cor. 4.13 and
Prop. 3.5.1, and the report does not say it read **Thm 2.3.1**, which is the statement C45's sign
depends on (§4, B24-02). So the convergence I hoped for is **partial**: the paper is now on the
record as PRIMARY for two other results in it, which makes the remaining job smaller still.
**Recommend a half-slot B24-02b**: read Thm 2.3.1 and the printed worked instance, record PRIMARY
at the point of use, confirm the module is non-vacuous at `N = 7` and that `D_7` lies in the
dual-degenerate locus at `k = 4`. One reviewer-hour, no pilot.

### 8.0e B24-04, transcribed against §8.4 (2026-09-20, ~09:30 local)

**Outcome (1), and beyond it.** §8.4's best case was *"a price, a structural answer, or both"*.
Question 1 was not priced — it was **settled by a theorem**, which is better than the criteria
allowed for. Questions 2 and 3 came back negative, as §8.4 anticipated in outcome (3), and both
negatives are informative rather than empty.

**The door I ranked first is shut, and I was wrong about it in a specific way.** I argued that
cost depends on structure rather than size, so a separating equation might hide in a cheap
small-tail cell. The theorem says the cheap cells are the expensive cells multiplied by a power of
a coordinate — the structure was a *disguise*, not an escape. That is a clean close, and it
removes the item I had put at the top of the Batch 25 research list.

**Two corrections to the record follow, and both are mine to carry.** The `10¹⁵⁰` figure I have
quoted for the cost at the forced tail is superseded by `≈ 4 × 10¹⁰` — **six orders from reach,
not a hundred and forty-six** — labelled EXTRAPOLATION. And the treewidth equivalence I proposed
in the B24-04 brief is **false**: the implication runs one way only, and their parameter depends
on the filling rather than the shape.

**The Missing Theorem is bespoke.** The basis is a seeded greedy selection, not canonical, so
every future cell needs its own theorem. That closes the other half of what I hoped the Kashiwara
strand might give, and it should be said plainly in Paper 3 wherever Theorem M's generality is
implied.

**What remains live from this slot:** large tail with small treewidth — a question about fillings
nobody has asked — and the `s_rep = 0` candidate with its named next step.

### 8.0d B24-06, transcribed against §8.6 (2026-09-20, ~09:15 local)

**Outcome (1): a blocker list and a claims table, no repair.** With a strong element of
outcome (3) — *"the paper is in better or worse shape than the record says; the stocktake's
description of it is mine and unverified."* It is in **worse** shape: four mathematical blockers,
one of them a theorem that is false as stated.

**My stocktake came out better here than it did for Paper 1** — four of six real, one already
fixed, one misdescribed, nothing invented — but it still missed a second garbled formula, and the
four real mathematical errors were entirely outside its reach. The decision to assess rather than
repair was right for the second time running.

**Three things to carry forward.**

1. **B2 is the one to act on first.** A theorem false as stated is the defect that survives into
   print and is caught by a referee. The repair is known and the conclusion survives, so it is
   cheap — but it must be done before this paper goes anywhere.
2. **The label collision with Paper 3 is a Batch 25 item in its own right.** The cap theorem
   cannot ship flat in one paper and conditional in its companion. Whichever is right, both must
   say it.
3. **Beauville joins LMR as an unread load-bearing source.** That is now **three** papers
   (LMR twice, Beauville once) where "cited" and "read" came apart, all found by reading rather
   than by inspection. G14′ is earning its place.

**Repair is Batch 25**, from this list. The `[AUTHOR]` items — including whether an uncommitted
Batch-15 result narrowing `D_LMR` to `[−4, −3]` may be cited — are yours, not a slot's.

### 8.0f B24-02b, transcribed against the brief's three outcomes (2026-09-20, ~09:40 local)

**Outcome (1) — it checks out — with the small qualification of outcome (2) attached.** The
producer's own framing, and the integrator accepts it: the qualification is `(★)`, a premise the
record already held, not a newly discovered hypothesis. **C45 closes. The programme's only
positive result is supported.**

**Packet verified by the integrator, not relayed.** Staged from `B15-01` and hashed:
`docs/b24_02b_report.md` = `3ecb611a3893323223e12e78a484f861e14fb6f1e8e2ab853c5ac5e481fa5438`
(29,511 bytes), `results/b24_02b/MANIFEST.json` =
`edbf598b4e89a5c273f1e2dea11876e6b20d6147cbf605a595f5eca12fdb4ed3` (3,947 bytes). Manifest
declares `head cc14e88c…`, `tree 2ceceb8c…`, `numerical_runs 0`, `interpreter_launches 0`,
`proofs_audited false`, and binds three files plus eight pinned inputs and four external sources.

**Transcribed from the closing ledger (§5, thirteen rows), not from the prose:**

- **The bytes are the bytes.** The fetched PDF of arXiv 1004.4802v1 hashes to
  `cfc28275a8c6b27f0ad6946d495ed4f889f7617df479be943d8d35718dbf2d79`, all sixty-four digits
  matching what `results/b23_06/MANIFEST.json` recorded at `feed104e`. arXiv carries only v1, so
  the ar5iv text actually read is the same version as the hashed PDF. **VERIFIED (bytes).**
- **LMR §3.2 prints the cell outright.** *"when n = 3, the module with highest weight
  12ω₁ + 5ω₂ + 2ω₇ occurs with multiplicity six in S¹²(S³C⁹), but only one copy of it is in the
  ideal."* One sentence carrying the weight `(19,7,2⁵)`, the degree `12`, `a = 6` as
  `lmr_cell.md` §3b's "LMR's own value", and `i_det = 1`. **PRIMARY READ.**
- **Both other confirmations hold.** Non-vacuity needs `N ≥ k+3` because §2.3 prints
  *"F ⊂ W is a subspace of dimension k+3"*; at `k = 4` that is `N ≥ 7`, the pinch exactly.
  `det_n`'s dual is the Segre of dimension `2n−2 = 4`, so `k = 4` is right, and LMR asserts the
  ideal membership for `closure(GL(W)·[det_n])` directly, so the containment need not be
  constructed. **No unrecorded hypothesis appeared at the step the brief flagged as riskiest** —
  which was the brief's own stated worry, and it did not materialize.
- **`(★)` must be named and is.** LMR's numbers are at `N = 9`; the record's `D_7` is at `N = 7`.
  The bridge is the programme's own `(★)` reduction at `ℓ(λ) = 7` — **exactly its boundary**. The
  producer named it rather than absorbing it. Labelled FINDING, "a named condition, not a new one".
- **A free external cross-check.** s73 computed `a = 6` at `N = 7` by three engines; LMR prints
  six at `N = 9`. **CORROBORATION** of the stability step, which until now had no external
  corroboration at all.
- **The record uses only the proved half, and that is the right half.** "Multiplicity six" and
  "only one copy" are asserted in LMR without printed proof; `i_det ≥ 1` follows from Thm 2.3.1 +
  Thm 3.1.1, which are proved. Since the record takes the **floor** from LMR and measures the
  **ceiling** itself, the close is robust even if the unproved assertion were wrong: `i_det` could
  only be larger and `D > 0` would still hold. **The producer recommends against rewriting the
  record to take `i_det = 1` from LMR, and the integrator transcribes that recommendation as the
  slot's, to be ruled on by B24-10.**
- **The citation trap, confirmed and sharpened.** Thm 1.0.2's printed `ω₁` coefficient **and**
  degree are both halved and mutually inconsistent, and the same `ω₁` typo recurs in §3.2's
  opening sentence. Citing Thm 1.0.2 for this cell yields `(13,7,2⁵)` at degree 6 — **the wrong
  cell**. This *confirms and sharpens* `equation_census.md` §2.1, which had already flagged Thm
  1.0.2's `n(n−1)`; the sharpening is that the corruption is on the **weight** side and is **not
  confined to Thm 1.0.2**. Cite Thm 2.3.1 + §3.1 + §3.2, never Thm 1.0.2.
- **G-15 discharged.** §3.2 of the report tabulates **ten** record sentences the PRIMARY label now
  attaches to, across `equation_census.md`, `lmr_cell.md`, `s73_report.md` and `CLAIMS.md`; six of
  the ten carry `(★)`. §3.4 gives replacement wording for C45's status cell **for the author to
  apply** — no sealed file edited (G13 respected).

**Housekeeping as reported and as the manifest confirms.** HEAD unchanged at `cc14e88c`, 0 tracked
modifications, 0 staged; B24-02's packet byte-untouched (`cf09c536…`). Zero interpreter launches,
kept literally true by validating the manifest through brace/bracket balance and full inspection
rather than running Python — the integrator notes this is the correct reading of the constraint
and not a dodge. No receipts produced, so *"negation missing for `b24_02b_`"* is a statement about
`.gitignore` coverage, not an ignored file — the B22-10 template sentence used correctly, fourth
occurrence and the first that is purely hypothetical. `b24_04_*.pid` checked as instructed.
**One tool error disclosed rather than hidden:** `pdftoppm`/poppler is absent, so the PDF was
hashed but not rendered; the slot drew **no inference** from that and re-verified the version
question against the host rather than trusting a memory note. External sources are hashed in the
manifest but held in the scratchpad cache, outside the delivery tree.

**G9′ — the one thing the integrator flags.** The slot reports saving a memory on the LMR citation
trap. **A producer's tool memory is not part of the record and is not an admissible input to
anything.** The close does not depend on it: the trap is in the committed bytes at §2.5 and at
ledger rows B24-02b.10 and .11, which the integrator has read in the staged packet. The memory is
therefore harmless here, but it is the second batch running in which a producer has written one,
and **B24-10 should say whether G9′ needs a reporting clause** rather than only a use clause.

**What this does not establish.** Not a separation, not a gap, not a multiplicity obstruction.
C45 is a **positive control at `n = 3`, unpadded** — it shows the instrument registers a signal
where the literature says there is one. It says nothing about five rows and nothing about padding,
and **no five-row determinant equation is known to be nonzero on padding** after it, exactly as
before it. `proofs_audited: false` stands in the manifest: LMR's proofs were not audited, only its
statements read.

### 8.0g B24-03, transcribed against §8.3 (2026-09-20, ~09:56 local)

**Outcome (1) with named residue — so (1) shading into (2), and the residue is the finding.**
All corrections applied, claims table current, `papers/det4-blindness/` now current against the
**committed** record, with `DIFF_NOTES.md` added. Session state as reported: HEAD `ce43cdb7…`,
branch `b23-04-paper3`, `status --porcelain` empty before the first write; read-only git, no
commit, no computation, no pilot, no `.pid`.

**The finding, which the producer put first and which the integrator endorses as the right call.**
**All four Batch-24 items that had reported are uncommitted on every ref** — B24-02 and B24-02b
(untracked in `B15-01`), B24-05 and B24-06. Under **G26 nothing may cite them**, so the draft
cites none of them. Rather than leave that invisible, the slot recorded in `GAPS.md` §E exactly
what each would change — **G-30** (B24-02), **G-31** (B24-02b), **G-32** (B24-06), **G-36**
(B24-05) — each naming the claim and the label it would move. **This makes PART 14 the
rate-limiting step for the paper, and converts four reconstructions into four one-edit updates.**

**It cuts against the paper twice, and the slot applied G26 anyway.** Transcribed as the producer
stated them:
- **Row 1.** The draft writes B23-10's corrigendum **K5**, which governs and which the corrected
  integrator ledger at `7d9839e7` restates: PROVED-kill at `N = 6,7,8` with no adopted input; at
  `N = 5`, GKZ Theorem B modulo Kleiman at `k ≥ 7`. **The window claim is not weakened** — row 1
  is a PROVED-kill for every `k` across `N = 5..8` on committed bytes, and Ruling **C48** says so.
  Only *"on elementary premises across the whole window"* waits on B24-02.
- **Corollary D2′.** The producer accepts the integrator's judgement that it belongs in the body
  beside Lemmas 1.3 and 1.4, and calls it *"the omission I most regret"*. It is stated in full at
  **G-36** with both self-contained premises, so committing B24-05 makes it an **insertion**
  rather than a reconstruction.

**C11's label is unchanged**, deliberately; the companion-paper divergence with Paper 2's flat
Theorem 7.1 is recorded at **G-32** only. The integrator notes that this is the slot declining to
make a mathematical ruling it has no authority for — the correct behaviour, and it leaves
carry-forward item 3 exactly where it was.

**Stale count is five, checked against `68866e6d` and `3bcad666` rather than taken on faith:**
C23, C30, C35, C36, C37 — matching §8.3's criterion 1 exactly. Two further rows carry a
**superseded** clause rather than a stale one (C34's *"64 on a cubic through a plane"*, K3; and
the "in flight" lineage notes); marked, not counted. The integrator accepts the distinction.

**Three corrections, and the first is mine — the eleventh integrator error.**
1. **`T2` is not `Σ_Π`.** My B24-03 brief §1 named the two families `T1` and `Σ_Π` and attached
   35 affine / 34 projective to `Σ_Π`. In B23-03 the second family is `T2 = {l·C : C ∈ Σ_Π}` at
   35 / 34, while `Σ_Π` **itself** is the cubics-through-a-plane locus in `Sym³C⁵` at **31 / 30**;
   `T3` and the skew-bordered type lie in `T2`. The draft used the packet's names and was
   unaffected. **Corrected in place in `b23_12_ledger.md`** (whose classification table carried
   the same conflation), with a note that the cubic-side statement
   `deg f ≥ onset I(D35 ∪ Σ_Π)` is **not** touched — `D35` and `Σ_Π` are both cubic-side — and
   that **B24-10 should confirm that reading**, since the error being corrected is precisely a
   failure to keep the two sides apart.
2. **`GAPS.md` G-17's *"rank measured mod 2³¹ − 1"* was wrong** — that rank was exact over `Q`
   (K8). Fixed in the entry, not in the packet. Correct: a sealed packet is not edited (G13).
3. **The draft had `M_4(C)` as `75 × 70`; B23-03's convention is `70 × 75`.** The producer
   identifies this as the draft's own typo rather than a packet error and fixed it; no rank or
   claim changes. G24 working as intended.

**Substantive additions, all within scope.** **G-A1 is now the paper's named open question**
(Question 6.5, and item 1 of §9), with the right-way corner scoped to the **determinant part**
throughout, as B23-10 required. The two lineage gaps B23-10 itself closed are recorded with their
residues (**C04**: Lemma 1 and (SUR) only; **C32**: Theorem 6's exactness and **C33** still open).
Blindness-worsens-with-`n` is in the body as **Lemma C50**, carrying the reviewer's precision that
**LMR's inequality is not strict at `n = m²/2`**.

**Static check by the producer, with no TeX toolchain:** 0 undefined `\ref`, 0 duplicate labels,
50 IDs C01–C50 with no gaps, every `\lit` key present as a `\bibitem` and conversely,
environments and braces balanced. **Not compiled** — the producer says so plainly rather than
implying the paper builds.

**Compiled by the integrator, which the producer could not do.** Source staged from `B23-04` and
hashed: `det4-blindness.tex` =
`ab69ccbe6cc79decccb3a2a3798e08e3d3a97412d79a6d095b12f3a68678455b` (96,414 bytes, 1,133 lines).
Three `pdflatex` passes on a CRLF-stripped **scratch copy only** — the source on the user's machine
is untouched. **Result: clean. Zero errors, zero undefined references, zero undefined citations,
zero LaTeX warnings. 22 pages.** The only diagnostics are cosmetic: one font-shape substitution
(`OMS/cmss/m/n`) and three overfull `\hbox`es at source lines 348, 432–434 and 603–608, none of
which affect correctness. PDF sha256
`1958badea27965d1e1a6ec0cafbdac50d6ace688a9dd03a3f0c4e296e521e1f5`.
**This is the first of the three papers to compile clean on the first attempt** — Paper 2 aborted
on `Double superscript` and Paper 1 needed a pass. The "uncompiled" hole in Paper 3's readiness
statement is closed.

**What this does not establish.** A writing slot produces **no new mathematics**, and this one did
not: every addition traces to a committed packet or to a reviewer's requirement. Paper 3 remains a
paper about **why the instruments are blind**. It contains no separation and no gap, and **no
five-row determinant equation is known to be nonzero on padding**.

### 8.1 B24-01 — Paper 1 blockers
1. **All five cleared or prepared** — the attribution patch written with its diff and *not
   applied*; the three internal contradictions fixed; the four papers read and each citation
   decided. Label: Paper 1 **submission-ready pending the author's sign-off on one patch**.
2. **Partly cleared, with named residue** — any blocker left open and why. Complete and
   acceptable; the residue enters the next board by name.
3. **A blocker turns out to be wrong** — a "contradiction" that is not one, or a citation that
   does not need reading. **Transcribe the correction first**; B23-05 and B23-10 are both fallible
   and so is my brief.
4. **Scope breach** — the slot applies the attribution edit, or proves something. Recorded as a
   deviation regardless of quality.

### 8.2 B24-02 — the two lineage gaps and the pilot
1. **Both closed by replay, pilot passes** — C45 and C24 gain a second lineage; row 1 becomes
   unconditional at `N = 5`. Label: two lineages each, named residues.
2. **Closed with residue, or one of the two needs new mathematics** — say which and what it would
   cost. A gap that cannot be closed by replay is a **finding**, not a failure: it means Paper 3
   leans on something nobody has re-derived.
3. **The pilot fails or the Kleiman dependency does not lift** — row 1 stays conditional at
   `N = 5` and Paper 3 says so.
4. **Cap hit or crash** — recorded as such.

### 8.3 B24-03 — Paper 3 corrections
1. **All corrections applied, claims table current** — the 5 stale rows, the scope sentences from
   B23-02/03, the three-kinds framing with its producer-only caveat intact.
2. **Applied with named residue.**
3. **A correction is refused with a reason** — e.g. a "stale" row that is in fact right.
   Transcribe the refusal first.
4. **Scope breach** — new mathematics, or a label upgraded. A deviation regardless of quality.

### 8.4 B24-04 — small tail, crystal basis, charge
1. **A price, a structural answer, or both** — the small-tail question priced (or shown to be
   priced by the published treewidth result); the 70-pattern basis ruled canonical or not; a
   charge statistic found or shown not to exist on 70 objects.
2. **Partial** — any of the three answered, the others with a stated obstruction.
3. **All three negative** — complete and useful: it would say the basis is bespoke, the treewidth
   link is not the same phenomenon, and no natural grading exists.
4. **Cap hit, crash, or the slot drifts into general plethysm.** A deviation.

### 8.5 B24-05 — the `D`-module strand
1. **A construction with its escape paragraph, non-coverage and price** — label OPEN with a named
   construction; first item of the next board.
2. **The honest negative** — each sub-candidate (`b`-function root integrality;
   characteristic-cycle multiplicities) with the sentence that kills it. Complete.
3. **Already done in the literature** — the cheapest good outcome; the slot stops and cites.
4. **Cap hit, crash, or a `b`-function computation attempted.** Out of scope by the brief.

Any escape paragraph that is a survey, or that leans on "unassessed" as a reason, is transcribed
as (2) whatever the report calls it. **The idea is the integrator's and unassessed**; a slot that
adopts it uncritically has failed the gate.

### 8.6 B24-06 — Paper 2 assessed
1. **A blocker list and claims table** — as B23-05 produced for Paper 1. Label: assessment,
   producer-only. **No repair.**
2. **Assessment with holes**, named.
3. **The paper is in better or worse shape than the record says** — either direction is the
   finding; the 2026-09-17 stocktake's description of it is **mine and unverified**.
4. **Scope breach** — any repair applied. A deviation.

---

## 8.12 Concurrency decision, and the correction it books into Batch 25 (2026-09-20)

**B24-02b and B24-03 were fired together**, rather than sequenced so that Paper 3 could cite a
closed C45. Recorded as a deliberate choice, not a slip, with its consequence priced now so the
next board does not have to rediscover it.

**No contention:** different worktrees (`B15-01`, `B23-04`), B24-02b runs no pilot and B24-03 runs
no computation, so the one-job rule is not engaged.

**The consequence is asymmetric, and only one branch is cheap.**

- **If B24-02b closes C45** (its outcomes 1 or 2 — the theorem checks out, with or without a
  stated hypothesis): B24-03 will have written the caveat *"PROVED modulo LMR Thm 2.3.1,
  read-status UNREAD"* where the record then says PRIMARY. **The Batch 25 correction is one
  sentence**, plus the matching `CLAIMS.md` row. Trivial.
- **If B24-02b returns outcome 3** (the theorem does not give the floor at this cell, or the
  containment fails, or the printed instance is not what the census says): then B24-03's caveat
  is **understated, not overstated**. The positive control would be unsupported, and Paper 3's
  §8 — the section whose whole purpose is to show the instruments work where there is something
  to see — needs rethinking rather than a sentence. **That is a Batch 25 section, not a Batch 25
  edit.**

**Booked for Batch 25 either way:** re-read B24-03's C45 passage against B24-02b's outcome and
correct it. Added to the carry-forward list below so it survives this ledger.

**RESOLVED 2026-09-20, ~09:40 local: the cheap branch obtained.** B24-02b returned outcome (1),
so B24-03's caveat *"PROVED modulo LMR Thm 2.3.1, read-status UNREAD"* is **overstated**, not
understated, and Paper 3's §8 stands. The correction is an edit, not a section. It is, however,
**three sentences rather than one**, because the close carries two things the concurrency pricing
did not anticipate: the `(★)` transfer from `N = 9` to `N = 7` must be named in the paper as well
as the ledger, and the **do-not-cite-Thm-1.0.2** ruling has to reach the bibliography. The
replacement wording is written for the author in `b24_02b_report.md` §3.4; the integrator has
**not** applied it, and will not — it is a slot's edit or the author's, not the record-keeper's.

## 9. Decisions open for the user

- **Paper 1's attribution wording**, once B24-01 prepares the patch. Your credit line.
- Nothing else. G-A1, row 2, the three-kinds theorem and Paper 2's *repair* are Batch 25.

**Carry-forward to Batch 25, accumulated this batch:**

1. **The C45 passage in Paper 3**, corrected against B24-02b's outcome (§8.12). **Now settled:
   an edit, not a section** — outcome (1). Three parts, all with wording already written in
   `b24_02b_report.md` §3.4: replace the G-15 parenthesis in `CLAIMS.md` C45 with the PRIMARY
   citation; name the `(★)` transfer at `ℓ(λ) = 7` in the paper's own text, not only in the
   ledger; and put **"cite Thm 2.3.1, never Thm 1.0.2"** where the bibliography can enforce it.
   The nine other record sentences in §3.2's table are `equation_census.md`, `lmr_cell.md` and
   `s73_report.md` — **not** paper sources, so they need no edit, only the label, which this
   ledger now carries.
2. **Paper 2's repair**, from B24-06's sixteen blockers — **B2 first**, the theorem that is false
   as stated. Plus the two `Double superscript` errors at source lines 144 and 874 that the
   integrator's compile found and the blocker list does not yet carry.
3. **The cap-theorem label collision**: flat in Paper 2's Thm 7.1, ADOPTED modulo Kleiman, Dimca,
   Gulliksen–Negård in Paper 3's C11. Decide which is right; both papers then say it.
4. **Corollary D2′ into Paper 3's body** if B24-03 could not cite it (B24-05's packet may not be
   committed when B24-03 runs).
5. Deferred from the Batch 24 board: **G-A1** (the boundary), **row 2** at `2 ≤ j ≤ N−4`, and the
   **three-kinds theorem**.
6. **Strike `10¹⁵⁰` from the record** wherever the cost at the forced tail is quoted; the figure
   is `≈ 4 × 10¹⁰`, EXTRAPOLATION (B24-04 Q1). Six orders from reach, not one hundred and
   forty-six.
7. **Say in Paper 3 that Theorem M is bespoke** — the 70-pattern basis is a seeded greedy
   selection, not canonical, so each new cell needs its own theorem (B24-04 Q3).
8. **New and unpriced: large tail with small treewidth** — a question about *fillings* the record
   has never asked (B24-04 Q2). The only live corner that slot left.
9. **The `s_rep = 0` candidate** (B24-04 Q3), with the `Y ↦ Yᵀ` involution named as the first
   thing to try.
10. **Governance:** a delegated read is not a read. B24-04's helper returned a gloss that was
    wrong in the direction that would have flipped its ruling; the producer caught it by
    re-checking. Worth a gate if B24-10 agrees.

11. **Eleventh integrator suggestion, UNASSESSED — an equivariance constraint on the C45 nullity.**
    Source: the user's 2009 PhD thesis (Sethuraman, *Volumes of Certain Loci of Polynomials and
    Their Applications*, Texas A&M, chair Rojas), staged to the container by the user on
    2026-09-20; sha256 of the staged copy recorded in the observation log. Status is exactly that
    of the `D`-module idea before B24-05: **integrator speculation, no weight until a slot writes
    it down and a reviewer checks it.** The integrator has *not* verified the equivariance group
    of the C45 map or its decomposition, and says so here so that no later reader takes this as a
    finding.

    *Outcome space for whichever slot takes it — three outcomes, no mechanism prescribed:*
    (a) the C45 map is equivariant for a group whose decomposition constrains its nullity to a
    sum `Σ_λ (dim V_λ)·ν_λ`, the constraint is strong enough to pin the value inside the measured
    range, and **the sign no longer depends on LMR Thm 2.3.1's floor**; (b) the map is equivariant
    but the constraint is vacuous in the measured range, and the slot says why in one sentence;
    (c) the map is not equivariant in the relevant sense, or the integrator has misread the
    shape of the problem, and the suggestion is refuted — the eleventh, as the tenth was.

    *Read alongside:* B24-02b's outcome and carry-forward item 1. **Settled 2026-09-20: the floor
    stands** (B24-02b, outcome 1, §8.0f), so this item is **not** on the critical path — it is a
    second lineage for a result that now has one solid one, and should be priced as such. The
    integrator notes without pressing it that a second lineage is worth more here than usual,
    because the first one rests on statements LMR prints **without proof of the instance** and on
    a `(★)` transfer sitting exactly at the boundary of its range.

    *Caution the slot must carry:* the thesis's own use of this argument (Lemmas 18–19) is easy
    because `SO(n)`-harmonics are **multiplicity-free**, so the intertwiner acts as a scalar with
    an explicit constant. The programme's coordinate rings are not multiplicity-free — that is the
    subject matter — so the reduction is to an `m_λ × m_λ` block per `λ`, not to a scalar. Any
    slot that quotes the scalar form has misapplied it.

12. **Twelfth integrator suggestion, UNASSESSED — basis discipline in rank and nullity slots.**
    Same source and same status as item 11. The differential (apolar) metric and `L²` differ
    componentwise by a factor the thesis computes as a ratio of Gamma functions, bounded below by
    `k!/(n/2 + k)^k`. Catalecticants are the matrix of the apolar pairing, so B22-02 Lemma 1.5's
    ranks live in it. **The proposal is a reporting requirement, not a mathematical claim:** any
    future rank or nullity slot states which basis it computed in (monomial, harmonic/isotypic, or
    other) and whether the metric is `L²` or apolar. Outcome space: (a) B24-10 or a Batch 25
    reviewer agrees and it becomes a gate; (b) it is judged already covered by existing gates;
    (c) it is judged noise. This bears on the exact-over-`Q` direction B23-01 left open — a
    candidate account of coefficient growth — but that account is **conjecture by the integrator
    and is not to be written into any draft.**

13. **Thirteenth integrator suggestion, UNASSESSED and lowest confidence — parametrization over
    ideals for the `D45 ∩ P5` components.** Same source and status. B23-03's `T2 = {l·C : C ∈ Σ_Π}` and
    B22-02's Fact 1.7 are discriminant loci; the thesis (Ch. V, Lemmas 35–37) uses Horn
    uniformization to parametrize the *univariate* discriminant and reduce membership to two
    linear conditions. The multivariate object the programme would need is the `A`-discriminant
    theory in GKZ, **already cited in the record for other reasons**. Outcome space: (a) a
    parametrization of one component is cheaper than its ideal and the slot produces it; (b) the
    GKZ machinery does not reach this case and the slot says at what point it fails; (c) the
    record already contains this and the item is struck. The integrator flags this as the weakest
    of the three and would not object to it being dropped by the reviewer without a slot.

15. **PART 14 is the rate-limiting step, not housekeeping.** B24-03 (§8.0g) established that all
    four reported Batch-24 packets are uncommitted, so under G26 Paper 3 cites none of them, and
    recorded at `GAPS.md` **G-30/G-31/G-32/G-36** exactly what each would change. Once PART 14
    commits them, four reconstructions become four **one-edit** updates, three of which are
    already drafted verbatim in the record: row 1's unconditional form (G-30), C45's PRIMARY
    citation with its three travelling conditions (G-31, and `b24_02b_report.md` §3.4), and
    **Corollary D2′ inserted beside Lemmas 1.3 and 1.4** (G-36). This supersedes the framing in
    carry-forward item 4, which assumed D2′ might have to be reconstructed.

16. **Confirm the cubic-side reading of `deg f ≥ onset I(D35 ∪ Σ_Π)`** (B24-10 or Batch 25). Not
    a doubt about the mathematics; a check demanded by the fact that the eleventh integrator
    error was exactly a cubic-side/quartic-side conflation. The integrator's reading is that
    `D35` and `Σ_Π` are both cubic-side loci in `Sym³C⁵` and the sentence stands.

17. **Paper 3's three overfull `\hbox`es**, at source lines 348, 432–434 and 603–608 of
    `det4-blindness.tex` at `ab69ccbe…`. Cosmetic, and named only so the typesetting pass has a
    list rather than a search.

14. **The LMR citation trap, as a record-level hazard.** From B24-02b (§8.0f): Thm 1.0.2's
    printed `ω₁` coefficient and degree are both halved and mutually inconsistent, and the same
    `ω₁` typo recurs in §3.2's opening sentence, so the corruption is not confined to one theorem.
    Anyone citing this paper for this cell must cite **Thm 2.3.1 + §3.1 + §3.2**. This belongs in
    the record and in every paper's bibliography discipline — **not** in a session's tool memory,
    where B24-02b also put it and where G9′ makes it inadmissible. Batch 25 should check Papers 1,
    2 and 3 for any surviving citation of Thm 1.0.2 or of "LMR" unqualified at this cell.

**Not carried forward, recorded so it is not re-proposed:** the thesis's volume machinery itself
— Barvinok's orbit-dimension bound, Blaschke–Santaló, Rogers–Shephard, the gauge/polar apparatus
— does **not** transfer. It measures real convex cones under a compact group; `Det_N` and the
padded permanent's orbit closure are complex projective varieties, and the objects needing
separation are ideals and isotypic multiplicities, not convex bodies. Further, **a volume or
measure gap would not be any of the four achievements** even if one were proved. The integrator
considered and rejected constructing a bridge, and records the rejection so a later session does
not spend a slot rediscovering it.

---

## 10. Observation log (2026-09-19, local UTC−4)

- 2026-09-20, ~09:56 local: **B24-03 reported COMPLETE, outcome (1) with named residue. Batch 24's
  producer board is finished — all six slots plus the half-slot.** Paper 3 is current against the
  committed record with `DIFF_NOTES.md` added. **The finding is about the record, not the paper:
  all four reported Batch-24 packets are uncommitted, G26 forbids citing them, and the slot
  recorded at `GAPS.md` §E what each would change — so PART 14 now gates the paper.** The slot
  applied G26 against its own interest twice (row 1's qualified form; Corollary D2′ held out) and
  declined to re-label C11 to match Paper 2, which was the correct refusal. **Eleventh integrator
  error: I conflated `T2` with `Σ_Π`** and put the quartic-side dimensions on the cubic-side
  object; corrected in place in `b23_12_ledger.md`, with the cubic-side statement flagged for
  B24-10 rather than silently changed. **Integrator compiled Paper 3: clean on the first attempt,
  22 pages, zero errors, zero undefined references or citations, zero warnings** — the first of
  the three papers to do so. PDF `1958bade…`.
- 2026-09-20, ~09:40 local: **B24-02b reported COMPLETE, outcome (1). C45 is closed and the
  programme's only positive result is supported.** LMR §3.2 prints the cell outright — weight,
  degree, `a = 6` and `i_det = 1` in one sentence — and the bytes match `b23_06`'s recorded hash
  in all sixty-four digits. `(★)` at `ℓ(λ) = 7` is named rather than absorbed; s73's `a = 6` at
  `N = 7` gains external corroboration; the Thm 1.0.2 citation trap is confirmed and **sharpened**
  beyond what `equation_census.md` §2.1 had. G-15 discharged across ten record sentences. The
  integrator staged and hashed the packet rather than relaying it (`3ecb611a…`, `edbf598b…`).
  **Flagged:** a producer tool memory again (G9′) — harmless here, the trap is in the committed
  bytes, but B24-10 should rule on a reporting clause.
- 2026-09-20, ~10:30 local: the user staged his 2009 PhD thesis (Texas A&M, chair Rojas;
  93 pages) and asked whether anything in it transfers. The integrator read it and recorded
  **three unassessed suggestions (items 11-13 above) and one explicit rejection.** Item 11 — an
  equivariance/Schur constraint on the C45 nullity — is the only one the integrator would defend
  as worth a slot, and it is worth it chiefly because **C45's sign currently rests on a single
  unread floor**. Nothing here is a finding; the status is the one the `D`-module idea carried
  into B24-05, where it was refuted and returned only its by-product. Staged copy sha256
  `3f383c2c5ca5fab5aa04e9001badf11f11fd22cec4782045276149c01d866815`.
- 2026-09-20, ~09:30 local: B24-04 reported COMPLETE, outcome (1). **The small-tail question is
  closed by a theorem — no separating equation can live in a small-tail cell.** The `10¹⁵⁰` cost
  figure is superseded by `≈ 4 × 10¹⁰` (EXTRAPOLATION). The 70-pattern basis is **not** canonical,
  so the Missing Theorem is bespoke. A delegated reader's wrong gloss was caught by the producer.
- 2026-09-20, ~09:15 local: B24-06 reported COMPLETE, outcome (1). **Paper 2 has four
  mathematical blockers, one a false theorem.** Integrator compiled it — two `Double superscript`
  errors at lines 144 and 874, to be added to the blocker list. Label collision with Paper 3 on
  the cap theorem flagged for Batch 25.
- 2026-09-20, ~03:30 local: B24-01 reported COMPLETE, outcome (1). Paper 1 awaits one signature.
  **Second prior-art finding (LMR Prop. 3.5.1 constructs `P_2`).** C45 still needs LMR Thm 2.3.1
  specifically — half-slot B24-02b recommended.
- 2026-09-20, ~03:00 local: B24-05 reported COMPLETE, outcome (2). The integrator's `D`-module
  idea is refuted; **Corollary D2′ is the by-product and belongs in Paper 3**. Tenth integrator
  error recorded (the Cayley convention). §4 and §8.0b written from the staged packet
  (`e13ad0f1…`).
- ~23:45 B24-02 reported COMPLETE, outcome (2). §4 and §8.0 written from the staged packet
  (`cf09c536…`). **C45 is the headline: the positive control's sign rests on LMR Thm 2.3.1, whose
  read-status at the point of use is UNREAD.** B24-03 unblocked. Row 1 unconditional at `N = 5`.
- ~22:00 Ledger opened with criteria for all six slots **before any fired** — the rule broken
  three times in Batch 23. Board shaped by the user: six producers; attribution prepared, not
  applied.
