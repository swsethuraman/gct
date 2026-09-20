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

## 8.13 PART 14 housekeeping, transcribed (2026-09-20, ~10:55 local)

**COMPLETE. All seven Batch 24 packets and both ledgers are committed and pushed.** 13 commits
(5 rules, 8 content) across **seven branches** and six checkouts, 52 content paths.

**Receipts verified by the integrator, not relayed.** `B24_COMMIT_RECEIPTS.json` =
`d37b8924e9e63fd1772048c82b3f3fd3cdd6ba6a1d74a6209028ed010e447f0e` (35,532 bytes);
`B24_COMMIT_REPORT.md` = `aa0e3c7640f091e4cc077c0d6147b36514b09260dbdeca07e4b34c6de48f7d0b`
(7,403 bytes). Commits read from the receipts, not from the relay.

| slot | branch | rules commit | content commit |
|---|---|---|---|
| B24-01 | `b23-05-paper1` | none (see below) | `bc7e62b714632c20d2405e54030224a2549c242d` |
| B24-02 | `b15-01-ci159` | `adff2b564f9a467a2ad65d2bd202d4ef91c1d532` | `f8273c3b5542fe085c596e3814c45621d3608ca7` |
| B24-02b | `b15-01-ci159` | (same) | `5a97317e7e28753261cf6e8dcece180a0e71b718` ← branch tip |
| B24-03 | `b23-04-paper3` | none (confirmed, not assumed) | `f95742aed4dd22d3f04ac1313ce3d78e6e0bc87c` |
| B24-04 | `b15-02-a1-probes` | `fc0b9fe94e70c9c93ae1e054277992cf165a559a` | `aafcbb692375f0a968881dbf18963a74d62ab557` |
| B24-05 | `b24-05-dmodule` | `c14b0d75…` | `5c5ba86edd318d349b858c5c99df27b6be9355c2` |
| B24-06 | `b24-06-paper2` | `43f901a0…` | `0019b2e2359eeabe065dad4271b89f06e2553896` |
| B24-12 | `b15-12-padding-orbit-bounds` | `733cc436…` | `744eb77b70cbb237d26c945695b264d4a4b9b402` |

**Verification, as recorded:** all seven HEADs matched the brief exactly, including B15-12's full
forty; **28/28 manifest-bound files matched on disk before staging**; after committing **52/52
blobs verify** (50 raw, 2 LF-normalised) and the 28 bound ones equal their manifests; sweep over
59 entries returned **0 hits, 0 trailer deviations**; `results/b24_02/` peaks at 4,917 B and
`results/b24_04/` at 52,323 B, **checked explicitly rather than assumed**, as the brief asked.
Push: fetch first, all seven 0 behind, seven fast-forward pushes, `ls-remote` confirms every tip,
**all 18 branches level with origin**, tags unchanged, stash empty, all seven worktrees end with
zero tracked modifications.

**Byte preservation, and the two branches that took no rules commit.** 0 of 40 `b24_*` paths were
`-text` beforehand and filtered/raw disagreed on 17; after the five rules commits all agree.
`b23-05-paper1` repeats PART 12's exception — LF blobs at HEAD against CRLF working copies, so a
`-text` rule would have rewritten every line and buried the real edit (diff 508/80, not 2,352).
`b23-04-paper3` is the mirror image resolved the other way **because note B required the compiled
bytes**: `det4-blindness.tex` commits **raw** at `ab69ccbe…` / 96,414 B — **the exact bytes the
integrator compiled** — with git reporting 1,998 changed lines against a real edit of +341/−73,
recorded in the commit body. The note worked as intended.

**`.pid` negations** added for `b24_02_` and `b24_04_`; **correctly declined** for `b24_02b_` and
`b24_05_`, which report the gap in the standing form but sealed no receipt. No `-f` anywhere, and
no producer wrote it — the B22-10 template sentence continues to hold.

### The twelfth integrator error, and the lineage gap behind it

**D1 and D2 are both mine.** My PART 14a row 1 asserted a B24-01 packet at
`docs/b24_01_report.md` and `results/b24_01/**`, with Paper 1 under `papers/det3-conductor/`.
**None of that exists.** There is no report and no results directory anywhere in the checkout, and
Paper 1 lives at the branch root — `paper/det3-conductor.tex` with `CHANGES.md`, `GAPS.md`,
`READINESS.md` and `README.md` beside it. My own §4 says so; I wrote the row from the shape of the
other six slots rather than from the record. **Note A governed and the pass was not damaged** —
the working tree was committed as found and the commit subject taken from the ledger and
`READINESS.md` rather than from a packet §0. D2 is the same cluster: I wrote "six branches" in
§14d where the table's own seven rows give seven. Six is the checkout count.

**The consequence is larger than the error, and it is for B24-10.** All six of B24-01's committed
paths are `manifest_bound: false`. **B24-01 is the only Batch 24 slot with no report, no manifest
and no seal.** Everything the record carries from it — the readiness statement that Paper 1 awaits
one signature, and the second prior-art finding that LMR Prop. 3.5.1 constructs `P_2` — rests on
**the integrator's transcription of a relay**, with no committed report to check it against.
That is precisely the lineage gap G18 and G26 exist to prevent, and it is the kind B23-10 ranked.
**It is recorded here as OPEN and is carry-forward item 18.** No claim sourced from B24-01 should
be upgraded until B24-10 rules.

**D3 — note C worked.** B24-06 has no manifest, so its add list is path-derived from G-32's four
paths, stated in the report as a visible deviation, and its rules pattern is `PAPER2_*.md` because
none of the `b24_NN` patterns match root-level deliverables.

**D4 — E9 is confirmed from the bytes and closed.** PART 13's reported departure was right: the
committed `b23_12_ledger.md` blob was 57,215 B against 58,796 B locally, missing §8.11, the struck
duplicate row (E6) and the B23-10 completion row. Those three land in this pass together with the
new `T2 ≠ Σ_Π` correction. **The housekeeper again committed the file as found rather than fixing
it**, which is correct and is the second pass in a row where that discipline held.

**G26 is discharged.** The four held-back edits now have commits to cite:
**G-30** `f8273c3b…`, **G-31** `5a97317e…`, **G-32** `0019b2e2…`, **G-36** `5c5ba86e…`.
This pass edited no paper file, no packet and no ledger. **B24-10 not launched; `B15-10` untouched
at `239dd6e84417ab04914a8d84cca02ddf754bf1fb`**, which is its starting HEAD.

## 8.14 B24-10, transcribed from its closing ledger §11 only (2026-09-20, ~13:13 local)

**Packet staged and hashed by the integrator, not relayed** — the relay was garbled in three
places. `docs/b24_10_review.md` =
`da1528ba7b19d314698c804fed696e4aa4058245efb3ec9737a9092ba11c2bf3` (130,445 bytes);
`results/b24_10/MANIFEST.json` = `ba6aea5122c152fafb98491a0a0c49be25c196ed1d3c2c6df6336b32fc05eafe`
(9 files, 29 pinned inputs, 2 `verified_absent` entries). Sealed `2026-09-20T17:12:49Z`, HEAD
`239dd6e8` unchanged, tree `3008235a…`, git read-only throughout, **1 of 3 pilots** (0.003 s,
exact rational arithmetic, no network), two unspent. **Reviewer model: `claude-opus-5[1m]`.**

**Method note that matters for the record:** the review ran on **the same configuration that had
halted repeatedly**. The variable that changed was the brief, not the model — the four amendment
files, whose content was largely about classifiers and halting, were dropped and replaced by one
clean brief. **The integrator's hypothesis is supported and the four amendment files are the
probable cause of its own tooling failure.**

**All rulings below are from §11 and nowhere else**, as the method requires.

### The headline rulings

- **The tail theorem is PROVED** (11.1.1), pre-formed CONDITIONAL on three named conditions, all
  three met. The factorisation holds on **spans, not only monomials** (11.1.2) — the place the
  reviewer pre-registered as the likeliest gap, and it is not one. `c_{n e₁} ∉ I` is **proved with
  two explicit witnesses** rather than assumed (11.1.3). `D*` is **un-indexed**, a minimum over all
  separating `f`, so the descent cannot leak across weights (11.1.4).
- **Theorem 1 does NOT inherit the 70-pattern basis's bespokeness** (11.1.19) — `tail = |λ̄|` is a
  function of the partition alone. The reviewer calls this the single most consequential thing it
  pre-registered to check. **The batch's strongest result is basis-independent.**
- **Corollary D2′ PROVED** (11.2.6) and follows from **D2 alone**. Lemma D2(a)'s "in the image"
  **strengthens** rather than weakens the claim (11.2.5), overturning the reviewer's own
  pre-verdict.
- **C45 is PROVED modulo `(★)`** (11.3.7). The `(★)`-at-the-boundary use is **SOUND** (11.3.3) —
  the range is stated **closed** at `ℓ(λ) ≤ 7` and an included endpoint is not an approximation,
  which answers the integrator's specific question against its own worry.
- **Theorem 9.1 of Paper 2 is REJECTED as stated** (11.5.1) — confirmed against the paper's own
  Prop. 2.1. **The highest-severity item in Batch 24, and cheap to fix**; the repair is on the
  record and the headline survives (11.5.2).
- **The cap-theorem label is ruled** (11.5.10), a ruling reserved to this review: `PROVED modulo
  Kleiman (SECONDARY), Dimca (PRIMARY, statement level) and Gulliksen–Negård (SECONDARY)` — the
  source wording, **which neither paper currently carries**. Paper 2's flat "we prove" drops the
  dependency and must be corrected before circulation; C11's "ADOPTED modulo" misdescribes
  provenance but errs conservatively. **G-32 closes on this.**

### The extrapolation — and carry-forward item 6 is amended, as promised

The reviewer derived `0.060 · 900⁴ = 3.9366 × 10¹⁰` **by hand before opening the packet**, as `v2`
had independently (11.1.11). Four findings the packet does not state:

- **The constant has not converged** (11.1.8): `c(t)` rises monotonically across the whole fitted
  range; Richardson limit `c_∞ = 10409/165888 ≈ 0.062747`, within 0.4 % of `1/16`.
- **The drift runs upward** (11.1.9): `c_∞ · 900⁴ = 4.117 × 10¹⁰`, **4.6 % above** the report's
  figure — so the figure is conservative on its own fit's terms.
- **The cited closed form does not carry the constant** (11.1.10): `1/((n−1)!n!) = 1/2880` against
  a measured `0.060` — **ratio 172.9**. Read as a law it gives `2.28 × 10⁸` at `t = 900`, wrong by
  173× **and in the direction that makes the programme look reachable**. It supports the
  **exponent only**.
- **"Supersede" is the wrong verb and the record must stop using it** (11.1.15). `10^150.4` was an
  **average** over all cells; `4 × 10¹⁰` is a conditional **minimum** over non-excluded cells —
  different statistics of different sets. `621` was never reduced by Theorem 1 either; it was
  already excluded by `D* ≥ 8`. **Neither of B23-06's numbers is refuted or superseded; both
  answer questions that are no longer the question.**

**And the number that actually matters is not `4 × 10¹⁰`.** The *unconditional* statement is
**`min N_S ≥ 231`** (11.1.14) — **inside the programme's reach.** `4 × 10¹⁰` may be used only as
an order of magnitude, only carrying Conjecture 2, and **never to two significant figures**.

**Carry-forward item 6 is amended below on this ruling (11.1.16), as the integrator committed in
advance to doing rather than defending.**

One correction the other way: the packet **already** prints the fitted range and fold factor
correctly (11.1.13). **The risk was in the record's transcription, not the packet** — that is, in
this ledger.

### Rulings that land on the integrator's record

- **The brief's one-sentence summary of Theorem 1 must not be quoted in place of the theorem**
  (11.1.6): it invokes primality without the non-membership and does not say `D*` is un-indexed.
  **Fourteenth integrator error.** The same defect appears at 11.2.7 — the brief attributed
  Lemma D1 to D2′ as a premise when it is a premise of one *application*; **the packet states the
  dependency correctly and the over-attribution is the brief's.**
- **The tenth integrator error is UN-BOOKED** (11.2.3). `(s+1)···(s+n)` and Caracciolo–Sokal–
  Sportiello's `s(s+1)···(s+n−1)` are **the same identity in two conventions** (`s → s+1`). The
  right label is *"convention not stated"*, not *"error"*, and D3's Cayley usage is the same
  convention and arithmetically consistent. The reviewer's reason is adopted verbatim:
  **"an integrator that over-counts its own errors degrades the error count as an instrument."**
  Applied here as faithfully as the rulings that run the other way.
- **The handling of the phantom B24-01 packet was INCOMPLETE** (11.7.1). Disclosing it was right
  and to the integrator's credit; **the claims were then transcribed at full strength anyway.**
  **"A disclosure not followed by a consequence leaves the record where it was."** Both claims take
  the producer-relay-only label at 11.4.2–.3 and the carry-forward list is corrected accordingly.
- **The `T2` → `Σ_Π` correction is right, and the cubic-side reading is CONFIRMED** (11.7.2–.3) —
  verified from `det4-blindness.tex` rather than from this ledger: **Lemma 6.1 is titled
  "restriction to the cubic factor" and defines `Σ_Π` inline in the displayed formula.** Writing
  `T2` there would have been a genuine error. The reviewer's words on the handling:
  **"Stopping at the boundary of the actual error, and asking rather than assuming, is the right
  handling."**
- **"Value has migrated into the negative" is DISPUTED in its premise** (11.9.6), accepted in its
  conclusion. **Batch 24 produced two genuine positives** — B24-02 made row 1 unconditional across
  `N = 5..8` on elementary premises, discharging K5; B24-02b closed C45. **"What is exhausted is
  the candidate pipeline, not the record"**, and the write-up should say so. The integrator accepts
  the correction.

### B24-01, and the finding the integrator did not make

- **No packet, confirmed from the committed tree** (11.4.1); the manifest carries two
  `verified_absent` entries.
- **"Paper 1 awaits one signature"** splits (11.4.2): the patch-pending state is **CERTIFIED from
  bytes**; the word **"one"** is **PRODUCER-RELAY-ONLY**.
- **"LMR Prop. 3.5.1 constructs `P_2`" is PRODUCER-RELAY-ONLY and should not be carried at any
  strength** (11.4.3) — a prior-art finding against the programme's own paper, resting on a
  relayed sentence with no quote, hash or read-status. **B24-02b set the standard inside this same
  batch and B24-01 does not meet it.**
- **A re-run producing a packet is required, and it is narrow** (11.4.4): bind the six paths with
  before/after hashes, state what was checked to reach "awaits one signature", and read LMR
  Prop. 3.5.1 to B24-02b's standard or withdraw the claim. **A half-slot.**
- **`ATTRIBUTION_PATCH.md` is not applied, CONFIRMED three ways** (11.4.5), and its wording
  **matches B23-10 §4.4 verbatim** on all three requirements (11.4.6).
- **But its binding hash `b911a151…` resolves to NOTHING** (11.4.7). The reviewer hashed **every**
  version of `paper/det3-conductor.tex` in the branch's history; the digest appears nowhere. The
  patch is **usable** — the two target passages are intact at `bc7e62b7` — **but its binding is
  not.** Label **UNBOUND**. The reviewer calls this the clearest single case for G29.

### Gates

- **G29 ACCEPTED** (11.9.1) with two additions and one limit. **(b)** every printed sha256 must
  resolve to a committed object or be labelled as naming an uncommitted state — *G29 as I drafted
  it would not have caught `b911a151…`*. **(c)** a brief or ledger may not assert a packet's
  existence; it cites the commit and manifest hash or states that none exists — *the PART 14
  failure was upstream of the producer*. **And it must NOT require a full manifest from an
  edits-only slot** (11.9.4): bindings, not ceremony, with B24-03 as the model.
- **G9′ AMENDED** (11.7.4): it needs a **reporting** clause as well as a use clause.
  **"A use clause is enforced at the moment of use by the person least able to notice it; a
  reporting clause is enforced at the moment of writing, when the act is visible."** Two batches,
  two slots, two producers, both caught by an integrator reading a relay rather than by any gate.
- **All other gates stand** (11.9.5).
- **Gate defect found in this slot** (11.10.1): `.gitignore:51` ignores `results/logs/*.pid` and
  the negations run `!…b16_10_*.pid` … `!…b23_10_*.pid` and **stop at `b23_10`**. This slot's
  `b24_10_p1_arith.pid` is ignored; `_resources.json` is not. Verified with `git check-ignore -v`.
  **The reviewer did not edit `.gitignore`** — one line is needed in PART 15's rules commit before
  the receipts are staged.

### The Batch 25 slate, as ruled — which reorders the integrator's proposed board

| order | slot | note |
|---|---|---|
| **1** | **The Paper 3 edits** (9.7) | Fully unblocked, no prerequisite remaining. Carry the three corrections at 11.6.9/.10/.12. **Plus a fifth edit this review unblocks: C11 → `PROVED modulo …`, closing G-32** |
| **2** | **Paper 2's repair, B2 first** (9.8) | then B3, B4, B1-at-source. **Cheaper than B24-06 priced it** — B24-02b partly discharges B5. Add the cap label to Thm 7.1 and the abstract. **Read Beauville first** |
| **3** | **B24-04 Q2 — large tail, small treewidth** (9.9) | "the best live mathematics on the table"; a negative worth as much as a positive; no prerequisite, Theorem 1 supplies the constraint |
| **4** | **The equivariance half-slot, and settle `(★)`'s label** (9.10) | the latter small, a reading task, **the most consequential unlabelled thing in the review** |
| **5** | **G-A1** (9.11) | **do it, but it gates nothing.** Paper 3 is true whichever way it resolves (11.6.6), so the risk is to the programme's ambitions, not the paper's correctness. **"An open question named in a published paper is a commitment"** |
| — | **row 2 NOT FUNDED** (9.12) | `CLAIMS.md` C23 describes it in its own words as *"a statement that nothing is known"* |
| — | **`s_rep = 0` NOT FUNDED pending a one-line test** (9.13) | **apply D2′ to it first** — if it fails at a pure power it dies for the cost of a sentence, the best immediate demonstration of D2′'s value |
| — | **"nothing more" REJECTED** (9.14) | — |

**The integrator's proposed board put Paper 2 first and G-A1 in Phase 2. Both are overruled**, and
the reviewer's reasoning is better than mine on both counts: the Paper 3 edits are fully unblocked
and ship a paper, and G-A1 cannot damage a paper whose every claim is already scoped.

### The two threads, and one honest negative

- **The rational candidate: the reviewer declines to certify it real** (11.8.1) — two-prime
  agreement is evidence, not a `Q`-proof, **"the same category error as taking a floor from a
  ceiling"**. **Not funded as a Batch 25 item** (11.8.2), because *payoff, not cost, is the
  obstacle*. **Recorded as an opportunistic rider** (11.8.3): seconds of exact arithmetic, for any
  slot already running exact rational arithmetic nearby.
- **The equivariance constraint earns a half-slot, for a better reason than the integrator gave**
  (11.8.4): not "a second lineage" but **the first route to the C45 floor that passes through
  neither `(★)` nor LMR**. **"A question whose negative answer costs a paragraph and whose positive
  answer discharges a premise is the ideal half-slot."** The reviewer makes **no finding on the
  mathematics** (11.8.5) and says so.
- **`(★)`'s own label is OPEN** (11.3.8) — `s73` was outside the reviewer's pinned commits and it
  declined to rule from a description. **"The single most consequential unlabelled thing I found."**
  If `(★)` is ADOPTED, the programme's only positive result rests on an adopted internal reduction
  **as well as** an external theorem, and the label must say so. **The pinning was the
  integrator's and this gap is the integrator's to answer for.**

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
6. **AMENDED 2026-09-20 on B24-10's ruling (11.1.14–.16), exactly as the integrator committed in
   advance to doing rather than defending.** The item as written said: *"Strike `10¹⁵⁰` from the
   record wherever the cost at the forced tail is quoted; the figure is `≈ 4 × 10¹⁰`,
   EXTRAPOLATION. Six orders from reach, not one hundred and forty-six."* **Every part of that is
   wrong in a different way.**
   - **"Supersede" and "strike" are both wrong verbs.** `10^150.4` was an **average** over all
     cells; `4 × 10¹⁰` is a conditional **minimum** over non-excluded cells. Different statistics
     of different sets, so neither refutes the other. Both are **reclassified, not struck**, and
     both answer questions that are no longer the question. `621` was never reduced by Theorem 1
     either — it was already excluded by `D* ≥ 8`.
   - **"Six orders from reach" compares the two directly and is therefore meaningless.**
   - **`4 × 10¹⁰` may be used only as an order of magnitude, only carrying Conjecture 2, and never
     to two significant figures** — and wherever it appears, the fitted range `t = 12…24` and the
     fold factor travel with it. B24-04's own packet already does this correctly; **the defect was
     in this ledger's transcription of it.**
   - **The number that actually matters is `min N_S ≥ 231`** — the *unconditional* statement, and
     **inside the programme's reach**. It was in the packet and this ledger did not carry it.
   - **The cited closed form `1/((n−1)!n!) = 1/2880` supports the exponent only**: it is 173×
     below the measured constant and would give `2.28 × 10⁸` at `t = 900`, wrong in the direction
     that makes the programme look reachable. Any use of it must say "exponent only".
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

18. **RULED 2026-09-20 by B24-10 (11.4.1–.7). B24-01 has no packet, confirmed from the committed
    tree.** The rulings, now in force: the patch-pending state is **CERTIFIED from bytes**; the
    word **"one"** in "awaits one signature" is **PRODUCER-RELAY-ONLY**; **"LMR Prop. 3.5.1
    constructs `P_2`" is PRODUCER-RELAY-ONLY and is not to be carried at any strength**, since a
    prior-art finding against the programme's own paper cannot rest on a relayed sentence with no
    quote, hash or read-status. **A narrow re-run producing a packet is required** — bind the six
    paths with before/after hashes, state what was checked to reach "awaits one signature", and
    read LMR Prop. 3.5.1 to B24-02b's standard or withdraw it. **A half-slot, and a Batch 25
    item.** Separately: **`ATTRIBUTION_PATCH.md`'s binding hash `b911a151…` resolves to nothing**
    in the branch's entire history — the patch is usable, its binding is **UNBOUND**, and the
    re-run rebinds it. **The integrator's handling of this was ruled INCOMPLETE (11.7.1):
    disclosure without consequence left the record where it was.**

19. **The targeted exact check on the rational candidate, dropped since Batch 23.** B23 ledger
    §8.3 said that if B23-10 judged the candidate real, an exact check of **two rational numbers**
    would be a far smaller job than the ≈10⁴-evaluation re-run, and *that* was the version worth
    pricing. B23-10 scoped the height-2000 claim (per coefficient false; under a common
    denominator true; candidate height 2842) but **never ruled on whether the candidate is real
    or whether the targeted check should be priced**. The integrator did not notice at
    transcription time. It may be worth nothing — it would upgrade one label in a `D = −1` cell —
    but it should be decided rather than forgotten. Put to B24-10.

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

- 2026-09-20, ~13:13 local: **B24-10 DELIVERED. Batch 24 is complete.** 130 KB review, 9 files,
  29 pinned inputs, 1 of 3 pilots, HEAD unchanged, git read-only. Packet staged and hashed by the
  integrator (`da1528ba…`, `ba6aea51…`) because the relay was garbled in three places.
  **The tail theorem is PROVED and does not inherit the basis's bespokeness. Corollary D2′ is
  PROVED from D2 alone. C45 is PROVED modulo `(★)`, whose boundary use is SOUND. Paper 2's
  Theorem 9.1 is REJECTED as stated — the highest-severity item in the batch. The cap-theorem
  label is ruled, and neither paper currently carries the right one.**
  **Five rulings land on this ledger.** Carry-forward item 6 **amended, not defended**, as
  committed in advance: "supersede" and "strike" are both wrong verbs — an average and a
  conditional minimum over different sets — and **`min N_S ≥ 231` is the unconditional number, and
  it is inside the programme's reach**. The **tenth integrator error is UN-BOOKED** (the Cayley
  forms are one identity in two conventions) on the reviewer's principle that *over-counting one's
  own errors degrades the error count as an instrument*. A **fourteenth is booked**: the brief's
  one-sentence summary of Theorem 1 must not be quoted in its place. The B24-01 **handling was
  ruled incomplete** — disclosure without consequence — and item 18 now carries the
  producer-relay-only labels. The **cubic-side reading is CONFIRMED** from the paper's source.
  And **"value has migrated into the negative" is disputed in its premise**: Batch 24 produced two
  genuine positives, and what is exhausted is the candidate pipeline, not the record.
  **The Batch 25 slate is reordered against the integrator's proposed board** — Paper 3's edits
  first, Paper 2 second, Q2 third, the equivariance half-slot and `(★)`'s label fourth, G-A1 fifth
  and gating nothing. Row 2 not funded; `s_rep = 0` not funded pending a one-line D2′ test.
  **G29 accepted with (b) and (c) added and its scope limited; G9′ amended to add a reporting
  clause; one gate defect found — `.gitignore`'s `.pid` negations stop at `b23_10`.**
  **Method note:** the review ran on `claude-opus-5[1m]`, the same configuration that had halted
  repeatedly. **The variable that changed was the brief, not the model** — which supports the
  integrator's hypothesis that its own four amendment files, whose content was largely about
  classifiers and halting, were the probable cause of the tooling failure.
- 2026-09-20, ~12:30 local: **B24-10 attempt two is running and halting intermittently — and the
  incremental-write mitigation is working.** The 12:15 halt came **after** the Q1 append landed:
  `results/b24_10/preverdicts_formed_before_reading_v2.md` is 124 lines / 7,438 B, sha256
  `bd5ea24252c7a8ca231ff939c2076804f844e815443a520a7239942496666f93`, Q1.1–Q1.4 complete, staged
  and hashed by the integrator. Attempt one lost a file to a halt; this cost one turn.
  **`B24-10-HALT-PROTOCOL.md` written** (`923fbb50972a66e696faac91ab888a1aaa08fa7519da5eb23dd4a0307bf50797`):
  Amendment 4 was written about *one passage halted repeatedly* and does not cover *intermittent
  halts at different points*, so the gap is closed — a halt after a flush costs one turn and the
  slot resumes; two consecutive pre-flush halts on one item skip that item with the fact recorded;
  two consecutive failed items invoke Amendment 5; **a halt count with locations goes in §0**; and
  no passage is ever reworded to get past a halt.

- 2026-09-20, ~12:30 local: **Q1.3 has already found something, and it lands on this ledger.** The
  reviewer establishes *before reading* that `4 × 10¹⁰` is **not independent** of the sizing law —
  it is `0.060 × 900⁴ = 3.937 × 10¹⁰`, the fitted law evaluated at 900 and nothing else — so its
  warrant is exactly the warrant of the fit carried out to `t = 900`, five to six orders beyond
  any plausible measured point. The integrator has re-computed this and confirms it.
  **Carry-forward item 6 uses `≈ 4 × 10¹⁰` as a price and is therefore overstated.** If the
  predicted ruling holds — label right, range unstated, admissible as an order-of-magnitude
  indication only — **item 6 is amended on the reviewer's ruling and not defended.** The
  reviewer's sentence is adopted into the record whatever else it rules: *a number that invites
  work must be better supported than a number that forbids it, not equally supported.* Striking
  `10¹⁵⁰` may have been right; installing `4 × 10¹⁰` in its place without the fitted range was the
  integrator repeating the error it had just corrected, in the more dangerous direction.
- 2026-09-20, ~11:55 local: **B24-10 attempt one ABORTED — tooling, not mathematics.** The
  session read the method rules, confirmed the worktree state, and died inside its own sealed
  pre-verdict file. **CAUSE CORRECTED 2026-09-20 ~12:20 by the session itself, against this
  entry as first written:** the integrator recorded repeated `[reasoning_extraction]` safeguard
  errors as the cause, taking it from error lines further down a relayed transcript. The session
  states that its response was **halted by a safety classifier mid-output** and that the `Write`
  carrying the pre-verdict text was truncated by that halt — which is how a 561-byte file ending
  mid-sentence came to exist. **The session is the primary source on its own failure and its
  account governs.** The `[reasoning_extraction]` errors are real but are not the proximate
  cause. **Second producer correction of the integrator's record this batch.** The distinction
  matters against the integrator's interest: a content-triggered halt is *stable*, so it is
  **more** likely to recur at the same step than a random infrastructure error would be.
  **It formed no verdicts.** Recovered and usable: HEAD `239dd6e84417ab04914a8d84cca02ddf754bf1fb`
  matching the brief, tree `3008235a92bf10a108ae673564d879a5716b4a1d`, and **two pre-existing
  untracked 2026-dated items in `B15-10`** (residue, stay out). Left behind:
  `results/b24_10/preverdicts_formed_before_reading.md`, **561 B**, sha256
  `683d3880beca32330d79a482845792133f426f71099a28d3e07b3db27ae9dd3d`, truncated mid-line, whose
  own first line claims it is written once and never edited — **an empty file asserting it is a
  sealed record, which is the hazard.** `B24-10-RELAUNCH.md` written: the stub is neither edited
  nor deleted nor renamed; the relaunch writes `..._v2.md` and **binds the stub in its manifest as
  a dead artifact**. Relaunch must run on a different model, name it, and say in its closing
  ledger where the choice could matter — **B25-10 then re-examines anything attempt two rules
  PROVED**. A third attempt is forbidden: if it dies in the same place it writes
  `docs/b24_10_partial_report.md` and stops. **Third duplicate/aborted-session event on this
  record** (the competing integrator fill 2026-09-17; B23-10's predecessor that left no report;
  this).
- 2026-09-20, ~12:20 local: **Thirteenth integrator error — Amendment 2 was defective twice, and
  is superseded.** (a) It told a slot to change its own model, which no slot can do: that is a
  harness choice at launch and the instruction was addressed to the wrong party. (b) It conflated
  **stability** with **capability**. Only stability was ever at issue; `claude-opus-5[1m]` is the
  strongest configuration available and its capability was never in question, so the amendment's
  own fallback prescribed the wrong remedy for the wrong reason. **In force:** the slot proceeds on
  `claude-opus-5[1m]`, names it in §0 and the manifest, and **does not flag the tail theorem,
  Corollary D2′ or the C45 chain for B25-10 on model grounds** — only its own reasoning can earn a
  flag. `B24-10-AMENDMENT2.md` written (sha256
  `2a09786fa9b07f6fcd72c5c55b30774d92d7fdd0abe753895595c0a764c1a97e`); **`B24-10-RELAUNCH.md` is
  not edited** and stands as written, the same treatment the relaunch prescribes for the aborted
  stub. The mitigation becomes central rather than incidental: **write incrementally and flush**,
  since attempt one lost everything by composing one large file. And the limit on it is explicit —
  **a repeatedly halted passage is never reworded until it passes**; the slot stops, writes a
  partial report naming what it could not emit, and says so. Working around a safety system is out
  of scope for this slot under any circumstances, and the record will say which kind of review it
  received.
- 2026-09-20, ~10:55 local: **PART 14 COMPLETE. All seven Batch 24 packets and both ledgers
  committed and pushed** — 13 commits, seven branches, six checkouts, 52 paths, 52/52 blobs
  verified, sweep clean, all 18 branches level with origin. **G26 discharged**: the four held-back
  Paper 3 edits now have commits to cite. `det4-blindness.tex` committed raw at the exact bytes
  the integrator compiled. **Twelfth integrator error:** my row 1 described a B24-01 packet that
  does not exist, and the deeper finding is that **B24-01 has no report, manifest or seal at
  all** — the batch's one unsealed slot, now carry-forward item 18 and a question for B24-10.
  E9 confirmed from the bytes and closed. Receipts staged and hashed by the integrator
  (`d37b8924…`, `aa0e3c76…`) rather than taken from the relay.
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
  error recorded (the Cayley convention) — **UN-BOOKED 2026-09-20 by B24-10 §11.2.3: the two
  forms are the same identity in two conventions, so the right label is “convention not stated”,
  not “error”. The error count runs to fourteen with this one removed and 11.1.6 added.** §4 and §8.0b written from the staged packet
  (`e13ad0f1…`).
- ~23:45 B24-02 reported COMPLETE, outcome (2). §4 and §8.0 written from the staged packet
  (`cf09c536…`). **C45 is the headline: the positive control's sign rests on LMR Thm 2.3.1, whose
  read-status at the point of use is UNREAD.** B24-03 unblocked. Row 1 unconditional at `N = 5`.
- ~22:00 Ledger opened with criteria for all six slots **before any fired** — the rule broken
  three times in Batch 23. Board shaped by the user: six producers; attribution prepared, not
  applied.
