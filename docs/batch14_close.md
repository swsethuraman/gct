# Batch 14 — close

**Twelve slots dispatched, twelve delivered, twelve merged, twelve reviewed.**
Dispatch base `batch14-base` = `9898e569`, tree `cb688cd3`, unmoved for the life of
the batch and kept as the historical anchor. Six slots ran as Claude (01, 02, 06,
07, 09, 12) and six as Astra / gpt-6 (03, 04, 05, 08, 10, 11).

Over the base: 27 commits on `integration/batch13`, 614 files changed, and the
citation index grew from **42 entries to 75** — sections F through M are this batch.

Reviews are `docs/b14_01_review.md` through `docs/b14_12_review.md` plus
`docs/b14_01_02_joint_review.md`. What the batch owes batch 15 is in
`docs/batch15_carry_forward.md`. The board, `docs/batch14_board.md` v0.4, is closed.

---

## 1. What the batch established

### `D ≤ −2` at LMR — the batch's main line

`D = 1 − i_pad(24)` with `a = 274`, `m_det = 273`. The batch moved
`D_LMR` from `[−4, +1]` to **`[−4, −2]`**, excluding `D = +1`, `0` and `−1`.

The chain, and it took two slots to close: **B14-01** reached 72 of the 73 mixed
degree-13 target members; the 73rd was already in **B14-02**'s delivery as source
row 15, at rung 13 with transport exponent 0, so its matrix row *is* `φ(F₁₅)`.
Joining them on identical columns gives rank 73 at both primes — a duplicate-row
control stays at 72 — and `a(21,17,2⁷;13) = 39` makes `i_red(13) = 3` exact rather
than `≥ 3`. `transport_lemma_T` carries all three directions to degree 24.
**`lmr_D_upper`**, CERTIFIED conditional on the ADOPTED `dim N₁₃ ≤ 73`.

**B14-07** corroborated the 3-space without being asked to: its degree-14 kernel,
restricted to the 39 degree-≤13 rows, spans exactly B14-02's 3-space, union rank 3.
Neither session arranged that.

### Lemma CI, proved twice from different directions

**B14-03**'s `complete_interpolation_kernel` and **B14-05**'s
`complete_interpolation` agree on the hypotheses that matter: the dimension
sandwich (`dim N ≤ h` suffices; the `h`-minor supplies the reverse) and source
completeness in the intended `M` (an incomplete source gives a subspace kernel, not
an ideal multiplicity). Corroboration, not redundancy.

**B14-05** also refuted, with an exact counterexample, the raw bracket-adjunction
identity I had requested unqualified — `raw_bracket_adjunction_false`. Requesting
it that way was my error and the refutation is the useful result.

### Three B13-06 targets closed

**B14-06**'s floor `mult_det ≥ 390` with **B14-08**'s ambient counts and multiplier
weights: `D((69,17,2⁷)₂₅) ≤ −2`, `D((73,17,2⁷)₂₆) ≤ −2`, `D((71,19,2⁷)₂₆) ≤ −1`.
`(69,21,2⁷)₂₆` stays open — `a = 531 < 533 = a_∞`, so that cell is not stable and no
stable-tail value transfers to it.

### The quartic region audited and 153 cells closed

**B14-11** enumerated the whole `n=4`, `δ ≤ 8`, `5 ≤ ℓ ≤ δ`, `λ₁ ≥ δ` region —
4,198 labels, 2,734 with `a > 0`, 667 at `a = 1` — proved the length and first-row
eligibility bounds directly on the quartic side, and closed **153** labels exactly
by pullback-zero. It also found that the programme had been closing `a = 1` cells by
citing BIP, whose theorem assumes `n ≥ m^25` and is silent at `(4,3)`; it corrected
37 passages across 15 documents accordingly. That *widens* the search: A1 cells are
open, not closed.

At intake the ledger closed 10 more by `peaked_quartic_ladders`, three of them in
B14-11's own queue including its top shortlist entry — a rule banked after its
dispatch base, which it could not have seen. **163 of 2,734 closed, 2,571 open.**

### Session 79's Q1 queue is complete

**B14-12** closed `(12,4,4,4,4,4)₈` at `N_S·δ = 2.16×10⁸`, the first cell built
above session 79's own stated build wall and 6.9× the largest cell s79 delivered.
With it, **all 123 cells of the frozen Q1 queue carry `i_det = 0`**: there is no
six-row determinant equation anywhere in Q1. The successor laboratory that queue was
built to find is not in it. `results/integrate/s79_q1_complete.json`.

That came from the slot the board deprioritised and mispriced by 2.4× on wall clock.

### Recovered, corrected and retired

- **B14-10** recovered `first_row_transport_bounds`, `stable_dimension_full_rank_closure`
  and `peaked_quartic_ladders` into the index and replaced eight absent B13-09 files.
- **B14-09** established the degree-10 six-row sizing; its `n_chi` is an exact
  character sum, never `N_S/|Stab|`.
- `length_bound`'s `, 9` clamp was **withdrawn** — the justification given for it does
  not support it. Nothing depended on it.
- `ladder_converse` gained the two `a ≥ 1` hypotheses it was missing. All 18 derived
  closures stand; 16 of 18 use `κ = (3)` at `δ = 1`, not "every", as I had written.
- `bip_blind_at_n4`'s span lemma was **false as stated** for arbitrary weight vectors
  — `c₍₃,₁₎((x+y)⁴) = 4` at a span-1 point refutes it. The isotypic form is true and
  is what the entry needed. Two further readings in `docs/bip_transfer.md` are
  withdrawn: the `chow6` zero is forced, not independent evidence, and the
  dimension-nine comparison does not hold as stated.

## 2. Verification the integrator performed

Every load-bearing claim was checked with my own code before merging. The
substantial ones:

- **the whole quartic census recounted** — 4,198 labels on the house Weyl-alternation
  route against B14-11's power-sum/Murnaghan–Nakayama route, **zero mismatches**
- **all 153 pullback-zero exclusions recomputed** from my own horizontal-strip
  enumeration, and the ten shortlist `h_pad` values reproduced exactly
- **all ten signed-Burnside sizes recomputed** by direct enumeration over every group
  element, including every shipped class representative's trace and sign
- **B14-12's cell rebuilt from scratch** on a second host with `fo='copy'` against
  the delivered `fo='inplace'` — every size, per-operator row and nonzero count, the
  cover, the nullity, `mult_det = 4` and `i_det = 0` at both primes identical
- **`n_χ = 244,454` and the pilot's 1,606,104** by my own Burnside orbit count
- `F_N` re-derived to `N = 35` and my own Murnaghan–Nakayama giving 274/392/533
- my own raising operator on 6 of B14-08's 61 witnesses; my own character sum on 18
  of B14-09's cells; four 8×8 integer determinants under `python-flint`; the
  trace-form Gram matrix rebuilt and all 15 leading minors confirmed
- **BIP read at the source**: v3 Theorem 1.4 does assume `n ≥ m^25`; Proposition 2.3
  with `♯` extending the first row yields exactly `(4)₁` and `(6,2)₂` at `n = 4` —
  the house's own `u` and `q62`, found independently in-house

Three cross-checks between sessions that neither arranged: B14-07's degree-14 kernel
and B14-02's 3-space; B14-08's rebuilt census against my banked reach table on all
239 records and every flag; B14-10's scanner replay reproducing my own 23/0/13/1.

## 3. The batch's defect record

**Mine.** Three attempts to state the delivery base before the tag worked. `&&` at a
PowerShell prompt, three times, until I wrote a script. Four defects in my own intake
gate, three of the same species — a check that could only fail in one direction — the
last of which failed a clean delivery. A board that never had the house wording scan
run on it. Slot 6's exclusion list omitting the module most likely to be copied from.
An unqualified request that B14-05 had to refute. Two filenames cited in my own joint
review that were never written, found by the artefact scanner at this close.

**Recurring, worker-side.** The packet's `..HEAD` bundle command (seven sessions).
No dispatch message carrying the expected commit and tree (**eleven of twelve**).
Garbled `bundle_prerequisites` (four of six Astra deliveries). `PROVED.md` section
collisions (six, every one "F").

**The field-naming family, four instances in four shapes** — `n_chi_lb`, `nchi_est`,
`i_pad`/`i_red`, `signed_uniqueness_verified`. A field whose name asserts a property
must ship the quantity that property is measured by. Now a rule in the index.

**Fixed at this close.** `wk13_b10_lean.raising_rows_lean` removed the caller's
scratch directory — it cost B14-12 a completed 47-minute build — and now removes only
what it wrote, with a test that fails on the old line. `exclusion_predicates.py`
implements the two predicate shapes B14-11 added, which had been *raising* rather than
skipping. `P13.json`'s six-prime defect is closed by a seven-prime sibling, the pinned
file left byte-identical. The artefact scanner learned one more absence marker.

## 4. State at the close

| | |
|---|---|
| `D_LMR` | `[−4, −2]`, both ends proved; `D = +1, 0, −1` excluded |
| quartic region `δ ≤ 8` | 163 of 2,734 positive labels closed, **2,571 open** |
| session 79 Q1 | **complete**, 123 of 123 at `i_det = 0` |
| session 79 Q2 | 9,952 of 10,513 open |
| index | 75 entries, sections A–M |
| dispatch anchor | `batch14-base` → `9898e569`, unmoved |

What is open, and what batch 15 owes, is `docs/batch15_carry_forward.md` §5.
