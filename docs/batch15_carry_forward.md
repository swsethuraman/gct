# Batch 15 — what batch 14 owes it

Collected at the batch-14 close from the twelve reviews, so the next board does not
have to read them. Every item names the review it came from and the slot that found
it. Nothing here is a mathematical result; `docs/PROVED.md` carries those.

**This is a list, not a board.** It says what to fix in the machinery and what the
open mathematics is. What batch 15 should *aim* at is a separate decision.

**For a worker session, `docs/delivery_contract.md` is the readable form of §1–§4
below**, with the check that catches each item and the one command to run. Items
1.4, 1.5, 1.8 and the whole of §2 are now enforced by
`tools/delivery/check_delivery.py`, so a session catches them itself.

---

## 1. Dispatch and delivery machinery

| # | fix | why | source |
|---|---|---|---|
| 1.1 | **Put the expected commit and tree in the tag annotation.** `git for-each-ref --format='%(contents)' refs/tags/<tag>` reads them in one command; the annotation is not part of the commit it names, so there is no self-reference problem | **Eleven of twelve sessions** reported that no dispatch message carrying those values reached them. The value kept moving — into the board header (wrong commit, twice), into `origin/main` (can advance mid-run), into a message that did not arrive | B14-07 D1, restated by B14-09 and B14-12 |
| 1.2 | **A committed dispatch file** — `results/b14_prep/dispatch.json` is the name B14-02 proposed; no such file exists yet — as the alternative, if the annotation route is not taken: it is neither the board nor the packet, so it has no self-reference problem either | B14-02's own recommendation, which I accepted | B14-02 D1 |
| 1.3 | **Board §5 must name the tag and the peel command**, not "the commit in your packet". The packet correctly cannot contain its own commit's hash, so with no dispatch message the chain had no terminal | B14-09 D3 | B14-09 |
| 1.4 | **The packet's bundle command must be the board's form:** `git bundle create <file> <base>..<branch> <branch>`. The `batch14-base..HEAD` form produces a HEAD-only bundle and `check_delivery.py` check 5 already rejects it, with the fix text | **Seven sessions** reported it | B14-02 D5, B14-12 D2 |
| 1.5 | **`bundle_prerequisites` must be a bare 40-hex string** in the manifest template | Four of six Astra deliveries captured the base commit's *subject line* alongside the hash | B14-04, B14-05, B14-08, B14-11 |
| 1.6 | **Add a `models: [(model, phase)]` field.** "Record the model that actually ran this session" assumes one model per session; B13-08 had two | B14-09 D6 | B14-09 |
| 1.7 | **A packet must say what a session should do when it starts with no repository.** B14-07 began with none; the laptop clone's 183 MB pack would not cross the device bridge and cloning the remote worked. The packet anticipated only "your clone predates the freeze" and said to stop, which would have been wrong | B14-07 D3 | B14-07 |
| 1.8 | **`PROVED.md` section letters must be assigned at dispatch, not chosen by the slot.** Six collisions in one batch, every one of them "F" | resolved to F–M by hand, six times | B14-03 onward |

## 2. Field naming — the batch's most repeated defect, four times in four shapes

A field whose name asserts a property must ship the quantity that property is
measured by. Four instances, none of which was caught by the session that shipped
it:

| field | what it said | what it was | source |
|---|---|---|---|
| `n_chi_lb` | a lower bound | not a bound at all — 135 of 222 values fell below it | `nchi_lb_field_is_false`, B13-05 |
| `nchi_est` | an estimate | `ceil(N_S/\|Stab\|)`, the quotient `nchi_2_21_guard` forbids, in **all 123** s79 queue entries, with nothing naming the estimator. Two documents quoted it as a measurement and both drew a sized conclusion from it | B14-12 D8 |
| `i_pad`, `i_red` | ideal multiplicities | **ceilings**, correctly labelled in the sibling `sides.*.status` and nowhere on the fields themselves | B14-12 D1 |
| `signed_uniqueness_verified` | uniqueness verified | true at 1.38x margin and equally true at 3e9 — the boolean cannot distinguish them | `boolean_without_its_margin`, batch-14 close |

**The rule, now in the index:** ceilings get `_ub`, floors get `_lb`, estimators name
their estimator, and a boolean that summarises an inequality ships the quantity too.
`values_are` is the existing house mechanism and it works — the files that carry one
were never misread.

## 3. Cost and sizing inputs a board may not use

| # | item | source |
|---|---|---|
| 3.1 | **Do not quote the `N_S·δ`-only build model.** `cost_model` says it is up to 21.7x low; batch 14's board used it anyway and under-priced slot 12's wall clock by 2.4x, on a slot whose only real risk was the window | B14-12 D4 |
| 3.2 | **Do not size `n_χ` from `N_S/\|Stab\|`.** Measured at both cells where the truth is now known, the quotient is low by 5.1 % and 8.6 %, and the error direction under-provisions | B14-12 D3 |
| 3.3 | **Do not carry a build ceiling quoted in `N_S·δ` alone.** Two measured points at `\|Stab\|` 12 and 120 show the peak is not a function of `N_S·δ`: a larger stabiliser means fewer rows, fewer nonzeros, a smaller peak and a longer build. Neither B13-10's `2.8e8` nor the `1.0e9` the same arithmetic now gives should be adopted. `stab_trade` in the index states the trade | B14-12, `stab_trade` |
| 3.4 | **Name what binds on the cell at hand.** "Budget for the kernel, not the builder" was right for the pilot and wrong for slot 12, where the builder took 95 % of the wall clock and the kernel ran in ten seconds | B14-12 D5 |
| 3.5 | **A third build point at `\|Stab\| = 1` or 2 near `10⁸`** would separate the two terms of the cost model and give the ceiling a shape in `(N_S·δ, \|Stab\|)`. About one hour, and it should come before any large Q2 spend | B14-12 §9 |

## 4. Inputs that need a warning in the packet

| # | item | source |
|---|---|---|
| 4.1 | **`P13.json` carries six primes.** Use `results/b14_prep/points/P13_seven_prime.json` for new degree-13 work: same 116 points, same bound, seven primes, 217-bit modulus, signed margin 2.97e9. The six-prime file stays pinned and unamended so B14-01's and B14-02's recorded verification still resolves | B14-02 D2, closed at the batch-14 close |
| 4.2 | **`source.json`'s field named `literal` is climbed to degree 24.** Right for no slot that used it: slot 2 needed 13, slot 7 needed 14. Recompute the climb from `native` | B14-02 D3 |
| 4.3 | **`blocks='disk'` with your own scratch directory is now safe** — the builder removed the directory it was handed, and that cost B14-12 a completed 47-minute build. Fixed at the close, with `tools/verify/scratch_not_removed.py` testing both directions | B14-12 D7, fixed |
| 4.4 | **A slot's OPEN set is a proposal.** The ledger may have advanced past a slot's dispatch base: B14-11's top shortlist entry was already closed by a rule banked after it dispatched. The integrator joins every OPEN set against the current ledger at intake, and the board should say so | B14-11 D1 |
| 4.5 | **A packet that appends to `inherited_exclusions.json` must add the `application_contract` entry in the same commit**, and must know the consumer fails closed by *raising* — a new predicate shape is an integrator deliverable, not something the legacy join skips | B14-11 D2 |

## 5. The mathematics that is open

Ordered by what would move the programme, not by cost.

1. **`i_pad(24) ≥ 4`, which would give `D = −4`.** `lmr_D_upper` has `i_pad(24) ≥ 3`
   and `D_LMR ∈ [−4,−2]`. The fourth direction needs a fourth independent relation
   at degree 13 or 14, and `transport_lemma_T` carries all `p` directions, so the
   work is at the source, not in transport.
2. **`i_red(13) ≥ 1` and `i_red(14) ≥ 1`.** Not reachable by evaluation — a sampled
   drop is a ceiling. Needs Lemma CI in full: `dim N = h` proved, `h` members
   exhibited, a nonzero `h × h` minor, exact source arithmetic. Slots 1–3 have the
   machinery and the degree-13 case is complete; degree 14 is where it stops.
3. **The ten A1 quartic candidates** from B14-11, less its entry 1 which the ledger
   already closes. Smallest open carrier is `(11,8,5,1,1,1,1)_7` at `n_chi = 1,576`.
   Each needs one bounded determinant-side HWV evaluation with a forced-zero control.
   An `a = 1` cell can separate only by an occurrence obstruction, and nothing in the
   literature excludes one at `(4,3)`.
4. **2,571 of the 2,734 positive quartic labels are open** after the 153 pullback-zero
   closures and the 10 peaked-ladder ones.
5. **Session 79's Q2:** 9,952 cells open of 10,513, median `N_S·δ` `2.44e9`, 7,386
   above s79's own `2e8` wall, 2,643 at or below slot 12's size — those 2,643 priced
   at ≈161 CPU-hours, and that is a model, not a measurement. Item 3.5 first.
6. **Compact certificates.** Two closed Q1 cells now sit above `certificate_ceiling`
   with results that are proved and cannot be certified: `(12,4,4,4,4,4)_8` at
   `N_S·a = 1.08e8` and B13-10's pilot at `1.8e8`. Two concrete targets.
7. **Does Kadish–Landsberg's `ℓ(λ) ≤ 9` transfer to the independent-padding model?**
   BIP pads with a variable already inside `per_m`, giving `m² = 9` essential
   variables against this programme's ten, and calls the difference irrelevant citing
   an appendix nobody here has read. Open, and one session would settle it.
8. **The protected-file errata from B14-11's audit** are still pending, and the first
   is consequential: `paper/det4-onset.tex` `thm:slab` asserts ambient fullness at
   length ≤ 4 **in every degree**, and its own proof discusses only the degrees
   computed. `docs/b14_11_protected_errata.md` gives frozen locations and replacement
   wording for all six. These are mine to write.

## 6. Debt recorded and deliberately not paid

- **Seven historical documents carry house wording-list words at the base:**
  `batch11_plan`, `n4_gate`, `s24_obstruction`, `s25_race`, `screen_results`,
  `session_24b`, `washout_threshold`. They pre-date the policy; editing them for
  vocabulary alone would obscure the audit trail. `intake_b14.py` now reports them as
  notes naming them integrator debt, and fails only on words a delivery *adds*.
- **`results/s79_cells.jsonl` was not extended** with B14-12's two rows. They carry
  `i_pad` and `i_red` as bare integers and both are ceilings; the completion is
  recorded in `results/integrate/s79_q1_complete.json` and in the index instead.
- **`docs/b14_strategy_memo.md`** is superseded by the board and now says so at its
  own head.
