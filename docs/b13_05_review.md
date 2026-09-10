# B13-05 review — finite-range padded/reducible equality

board_numbering: batch13
session_id: B13-05
models recorded by the session: **`Claude Fable 5.1`** (every computation, and
every commit through `671e2e5`), then **`Claude Opus 5`** (report and delivery
commits). No computation was re-run across the change.
bundle: `b13_05_fable.bundle` (one part)
base: `00495110c62acfbbbc951e82cc218ed091563b3f`
head: `896b4326670ae9e1cadc5fa42f729a90685410a7` (`refs/heads/b13_05_fable`)
status claimed: **success — the bounded equality theorem, plus a characterised
negative and a resumable degree-8 prefix**
integrator verdict: **accept the mathematics — this is the batch's first
completed theorem. Same mechanical fix as B13-04 before merge: nine
session-link trailers. One numerical error found, and it cuts the session's own
way.**

Stock-take. Arithmetic here is closed-form or run against the session's own
delivered JSON.

---

## 1. Zero-cost checks

| check | result |
|---|---|
| md5 | `496663903ef6f87c7c12f81e16a942c4` — matches |
| `git bundle verify` | "is okay"; one ref `refs/heads/b13_05_fable` |
| declared base | `0049511` — equals `origin/main` and my tip |
| applies | clean; 33 files, 133,030 insertions, **0 deletions** |
| single-writer files | **none touched** |
| 5 MB rule | none close; largest is the census at 170 KB |
| `claude.ai` URL in any delivered **file** | **none** |
| `Claude-Session:` trailer in commit messages | **present in all nine — see §7** |
| pre-registration | `e675cb8` before any computation, addenda A/B/C each before the measurements they govern |
| run discipline | workers ended at handoff by recorded pid; the report states explicitly that no run was ended by name-pattern matching |

Counts, all reproduced:

| stated | recomputed | agrees |
|---|---|---|
| census 161 / 371 / 797 at `δ = 7,8,9`, naive total 1329 | column sums exact; `161+371+797 = 1329` | yes |
| 1444 census rows, 1222 closed, **222 open** | `1444 − 1222 = 222`, and the `open` array has exactly **222** entries | yes |
| open split 25 / 141 / 56 | `(δ8,ℓ7) = 25`, `(δ9,ℓ7) = 141`, `(δ9,ℓ8) = 56` from the JSON | yes |
| top cells = strict partitions, `1,1,2,2,3,4,5,6,8` at `δ = 1..9`, 32 total | `q(δ)` reproduces the sequence; sum 32; 5+6+8 = 19 at `δ = 7,8,9` | yes |
| the top-cell shapes | all five at `δ = 7` and six at `δ = 8` have `\|μ\| = 3δ` and `ℓ(μ) = δ` | yes |
| Frobenius construction `μ = (ν\|ν−1) + (1^δ)` | `ν = (7) → (8,1⁶)+(1⁷) = (9,2⁶)` ✓; `ν = (4,3) → (5,5,2,2)+(1⁷) = (6,6,3,3,1,1,1)` ✓ | yes |
| `dim D_r^{per₃} = 9r − 4` at `r = 7,8,9` | `59, 68, 77` against `C(r+2,3) = 84, 120, 165`; codims `25, 52, 88` | yes |
| build cost ~32 CPU-hours over the 197 | `Σ N_S = 6.249×10⁸`, `× 1.8371×10⁻⁴ s = 31.9 h` | yes |
| decision cost ≥ ~1100 CPU-hours | `Σ n_χ(lb) = 8.95×10⁷`, `× 45 s / 10³ = 1119 h` | yes |

**The subordination claim, checked cell by cell.** The report says the 25 open
degree-8 cells are subordinate — each closed by its ladder successor `μ + 3e₁`
at degree 9. Run against the delivered JSON: **all 25 successors are present
among the open degree-9 set. 25 of 25, none missing.** The residual really does
collapse onto a single degree.

---

## 2. The result — the batch's first completed theorem

**`I(D_r^{per₃})_δ = 0` for every `r` and every `δ ≤ 7`** (PROVED). By
Prop. 8(1), `mult_pad = mult_red` at every weight, of every length, in every
degree `δ ≤ 7`. The record's global floor stopped at `δ ≤ 6`. **The permanent
cannot be felt below degree 8, at any length.**

The proof is short because the structure does the work:

- **Theorem A** stratifies the whole problem by length: `6 ≤ ℓ(μ) ≤ min(r,δ,9)`.
  Below 6 the ideal is empty by Theorem 2 and the restriction lemma; above 9 there
  is nothing new because the family pulls back along `Cʳ → C⁹`. So the cubic
  equation problem is *one finite object* stratified by length, and a length-7
  constituent is the same constituent at `r = 7`, `r = 8` or `r = 9`. This is
  the proof that the board's "lengths seven and eight" framing was right.
- At `δ = 7` that leaves only lengths 6 and 7. Length 6 is closed by s43. Length
  7 forces `ℓ(μ) = δ` — the **top cells**, of which there are exactly five.
- **Theorem C** identifies them: via Littlewood's `e_δ[h₂] = Σ_{ν strict}
  s_{(ν|ν−1)}`, each top cell has `a = 1` and its highest-weight space is spanned
  by a **`δ × δ` maximal minor of the second catalecticant**. So `i(μ,δ) = 0`
  iff one exact integer determinant is nonzero at one point of `D_δ^{per₃}`.

That last step is the batch's best cost move. **An `N_S`-sized rank computation
becomes a single determinant, 0.01 s per cell.** All nineteen top cells at
`δ = 7, 8, 9` are certified empty by exact integer determinants at nine `per₃`
pencils each — and since a nonzero integer is nonzero over `ℚ`, one pencil would
have sufficed; nine is redundancy.

It is the same *kind* of move as B13-04's Lemma B(4) support test (a reducible-
ideal membership is a support condition, no pullback to expand) and B13-03's
retained fixed-factor slice. Three sessions have independently found that the way
past the cost wall is a structural identification, not a bigger machine.

---

## 3. Instrument discipline

The top-cell instrument was validated against pre-registered checks before
deciding anything, and the third one answers the programme's recurring trap
directly: `h_μ` expanded in the house monomial basis is killed by **every** house
raising row, exactly over `ℤ`, at all nine cells with `δ ≤ 5` — and the check
**asserts that every monomial it produces lies in the weight-`μ` basis before
testing**. It cannot silently drop a target. That is the correct answer to both
the `exps`-ordering trap and the "a check that cannot fail is not a check" class.

Two genuine cross-session reproductions:

- `(17,2⁵)₉` — s79's own cell — rebuilt from scratch on a different driver,
  same `a`, same `mult`.
- `(11,2⁵)` recomputed at `r = 7, δ = 7` where s41 banked it at `r = 6`, and it
  agrees — the restriction lemma behaving as Theorem A says it must.

And the census independently reproduces **four** sessions' length-6 enumerations
(s37's 4, s41+s43's 27, s41+s43+s47's 91, s79's 210), with `a` computed by two
unrelated routes asserted equal at all 1444 rows, and s79's `Σa = 1213` matched.

**Theorem F's predictions were checked on the numerical instrument**, not merely
restated: `(12,2⁶)₈ = (9,2⁶)₇·(3)₁` and `(15,2⁶)₉ = (9,2⁶)₇·(6)₂` both measure
`mult = a = 1` at both primes. A theorem with a numerical control on it.

---

## 4. Two findings that change my planning premises

**(a) The wall is the kernel, not the builder — and this inverts my own
stocktake.** `docs/stocktake_batch12.md` §7 puts the raising-row builder in
front. That is right for the six-row *quartic* cells that motivated it, where
s79 hit 4 GB of rows. On the *cubic* queue the builder is comfortable — peak
0.32 GB at `N_S = 8.4×10⁵` — and the decision costs twenty times more. **So
B13-10's leaner builder, valuable as it is, does not unblock the degree-9 cubic
queue.** What would is a faster kernel: block Wiedemann, or a better-conditioned
cover. That is a board-level correction and I accept it.

**(b) The queue is sorted by the wrong key.** s79 ordered by `N_S·δ`, the build
cost. On this queue the size that matters is `n_χ`. `(15,2⁶)₉` has
`N_S = 65,416` but `n_χ = 301` and decided in 6 s; cells with a large
`|Stab_W(μ)|` are enormously cheaper than `N_S` suggests. The session learned
this the expensive way — its first campaign launch set `--nchi-cap 60000` and
both workers died on 2.18 GiB and 31.1 GiB allocation requests. Reported openly,
nothing banked from it, twenty minutes lost.

---

## 5. The error I found, and it cuts their way

§5.2 says the residual's `n_χ` lower bounds "reach `4.1·10⁵` — **seventeen
times** the dearest cell measured here."

That figure is the **degree-8** maximum. §7.2 quotes it correctly there for the
25 remaining degree-8 cells. But §5.2 is discussing the 197 **degree-9** cells,
and their maximum is

    n_chi_lb = 4,251,922 = 4.25×10⁶   at μ = (7,6,4,3,3,2,1,1), ℓ = 8, a = 1, N_S = 1.70×10⁷

— ten times what §5.2 states, and **138×** the dearest cell actually measured
(`n_χ = 30,704`), not 17×. A figure was transposed between two sections.

The consequence is not cosmetic. The session's own superlinearity table shows a
2.8× rise in `n_χ` buying a **74×** rise in time, because Wiedemann costs
`O(n_χ · nnz)`. With the top of the queue at 138× rather than 17× the dearest
measured cell, **the 1,100-hour figure is a far weaker lower bound than the
report claims.**

A second data point in the same direction: the report says measured `n_χ`
overshoots the `N_S/|Stab|` lower bound by "5 % to 20 %", but its own table has
`(8,4,4,2,2,2,2)₈` at `n_χ = 23,896` against a bound of 17,582 — a **36 %**
overshoot.

**Both corrections strengthen the session's own recommendation**: fund degree 8,
defer degree 9 behind a faster kernel. I would state the degree-9 price in the
board as "≥ 1,100 CPU-hours, realistically several times that, with a handful of
cells each capable of exceeding everything B13-05 ran."

Minor and separate: §5.1 reads "197 are at degree 9 and 25 at degree 8 — and the
26 are subordinate". §0 has 25, the JSON has 25, and 25 is right.

---

## 6. The negative, properly closed

The orbit-stabiliser bound `mult ≤ dim S_μ(C⁹)^{H'}` — the natural cheap
invariant-theoretic screen, and it bounds `mult` from *above*, so a bite would be
a PROVED membership statement with no sampling. **It is silent at every one of
4,517 weights**, `δ ≤ 9`, every length, by margins of 4 to 691.

What makes this a closed negative rather than a report of failure:

- **Why it fails is structural**, not accidental: `b` counts `H'`-invariants in
  `S_μ(C⁹)`, whose dimension grows like the representation, while `a` counts
  plethysm multiplicities, which grow far more slowly.
- **Where it could bite is identified**: the margin shrinks sharply with
  *length* — 4 at `ℓ = 9` against 691 at `ℓ = 7` at the same degree — so the
  live region is `ℓ = 9`, `δ ≥ 10`, outside batch 13.
- **The obvious rescue is excluded**: extending `H'` to the full
  `Stab_{GL₉}(per₃)` cannot help, because the remaining factors are finite so `b`
  falls by at most a bounded factor, and the margins are orders of magnitude.
- Four pre-registered instrument checks, all passed, including a global sum rule
  exact at all nine degrees and a brute-force cross-check with exact `ℚ` nullity
  *and* both primes. The seven cells skipped under the brute-force cap are named,
  and all seven have `a = 0`, so nothing depends on them.

Theorem D (the ideal ladder) gets the same honest treatment: it closes nothing
that was not already closed, and the session records that — *"at these degrees
the ladder is not a pruning tool, it is an ordering tool."*

And the boundary of the whole thing is stated where it belongs: §7 is a prefix,
not a theorem. **"The remaining 25 could still contain the first
permanent-specific equation the programme has ever seen. Nothing in this report
excludes that."** Every cell decided came back full rank with no candidate drop
at either prime.

---

## 7. The trailer breach — now twice, and it looks environmental

**All nine commits carry `Claude-Session: https://claude.ai/code/session_01Hw…`.**
Same breach as B13-04, same confinement: **no delivered file contains the URL**
(checked across all 33 changed files), so
`tools/rewrite/message_callback.py` fixes it before merge, as it did for 260
commits at `docs/history_rewrite.md`.

Worth noting rather than just recording: of the five batch-13 sessions delivered,
**exactly the two that ran partly as Claude Opus 5 carry the trailer**, and in
both cases *all* their commits carry it — including the ones made in the Fable
phase, and B13-05 states its history was not rewritten. B13-01 (Fable
throughout) declined it explicitly; B13-03 (Astra) does not have it. That
correlation is worth one look at how those two containers were configured,
because if it is environmental then telling sessions to decline it is not enough
— the preamble needs to say the trailer must be stripped before bundling, and
name the tool.

**Model handling is otherwise exemplary**, as in B13-04: the swap is recorded
with the phase boundary named to the commit, no computation re-run across it,
and no result attributed to the model that did not produce it. Both sessions
independently raised the same preamble defect — "record the model that actually
ran this session" assumes one model per session. **Two of five sessions have now
hit it; the preamble needs a `models: [(model, phase)]` field.**

---

## 8. Defects against my board — six, two of them urgent

1. **The brief names only half the inheritance, and B13-09's entry repeats the
   wording.** At `δ = 9`, `ℓ ≤ 5` removes 365 of 797 — but `ℓ = 6` removes a
   further **210**, a quarter of the census, excluded not by Theorem 2 but by the
   certified length-6 record. B13-09's entry says "account for shorter components
   explicitly — by citing Theorem 2 and the restriction lemma", and **a session
   reading that literally could recompute s79's 210 weights.** B13-09 has not run
   yet. Fix the entry to cite Theorem 2 **and** `results/s79_per6_d9.md`.
   **Actionable before B13-09 starts.**
2. **`analysis/wk9_s43_inject.py` is hardcoded to `r = 6`** — confirmed against
   the tree, line 75: `n, r = 3, 6`. The programme's only memory-lean decision
   route cannot be pointed at length 7 or 8 as it stands. B13-09's brief says
   "use the existing builder"; the builder is fine, the **decider** is not.
   B13-05 wired the same criterion to the s45 build in
   `wk13_b13_05_validate.py::run_inject` and B13-09 should be told to use it.
   Related and equally practical: session 42's Wiedemann binary is not in the
   tree and its default paths are not writable here; `gcc -O3 -o <path>
   analysis/wk9_s42_wied.c` builds it in a second, but `WIED_BIN` and `WIED_WORK`
   must both be set. *"Two minutes if you know it and a dead end if you do not."*
   Belongs in the preamble's toolchain paragraph beside `python-flint`.
3. **Length 9 belongs to no batch-13 entry.** The `δ = 9` census contains 8
   length-9 cells; B13-05 computed them (they are top cells, closed) and labels
   them exploratory. The board should decide whether length 9 is B13-09's,
   batch 14's, or nobody's.
4. A scope call, declared: validating instrument I5 *decides* 19 cells at 0.01 s
   each. Declared rather than hidden, and the theorem stands either way.
5. The preamble assumes one model per session — see §7.
6. No rule for who owns *finishing a degree* when a cell is cheap for the
   theorem's owner and dear for the queue's owner. A one-line rule would settle
   it: the theorem's owner may complete the degree the theorem is about, and says
   so.

---

## 9. The strategic question the session puts to me, and my answer

B13-05 asks it plainly and it deserves a plain answer. The cubic screen was
adopted (`stocktake_batch12.md` §5) as "one computation per `(length, degree)`".
True of the statement; **not true of the cost** — one `(length, degree)` at
`r = 7,8`, `δ = 9` is 197 weights and at least 1,100 CPU-hours, realistically
several times that after §5's correction. And `batch13_corrections.md` §1 says
objective 2 is not on the path to `D > 0` at all: the binding constraint is
`i_det`.

**Fund degree 8; defer degree 9.** Degree 8 is 60–100 CPU-hours, closes a clean
theorem (`I(D_r^{per₃})_8 = 0` for every `r`, Theorem B up to `δ ≤ 8`), closes 9
degree-9 cells free by Theorem F, and is **fully set up** — cell list, driver and
compiled tool all in the bundle, banking per cell and skipping what is banked.
It is the cheapest theorem left on the board. Degree 9 buys a negative that does
not gate the obstruction, at a price that would dominate the batch, and it should
wait behind a faster kernel.

---

## 10. Actions

1. **Strip the nine `Claude-Session:` trailers** with
   `tools/rewrite/message_callback.py` before merging — as for B13-04.
2. **Fix B13-09's board entry before it starts**: cite the length-6 record
   (`results/s79_per6_d9.md`) alongside Theorem 2, and point at
   `wk13_b13_05_validate.py::run_inject` rather than `wk9_s43_inject.py`.
3. **Correct the degree-9 price in the board** to reflect the `4.25×10⁶`
   maximum: "≥ 1,100 CPU-hours, realistically several times that."
4. **Correct `stocktake_batch12.md` §7's builder-first framing** for the cubic
   queue, and note that the sort key is `n_χ`, not `N_S·δ`.
5. **Add `models: [(model, phase)]` to the preamble front matter**, and say
   plainly that the session-link trailer must be stripped before bundling, naming
   the tool.
6. **Fund the 25 remaining degree-8 cells** as the cheapest theorem on the board.
7. Add the Wiedemann build recipe (`gcc`, `WIED_BIN`, `WIED_WORK`) to the
   preamble's toolchain paragraph.
8. Decide who owns length 9.
9. On the deferred verification pass: replay two of the nineteen top-cell
   determinants independently from the stored pencils (exact integers — cheap and
   decisive), and re-derive the strict-partition ↔ top-cell correspondence at
   `δ = 8` from Littlewood's identity.
