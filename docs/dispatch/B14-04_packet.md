# B14-04 — session packet

**You are B14-04.** `board_numbering: batch14`. Intended model: **Astra**.
Record the model that *actually* ran this session in your commit trailer and your
report, not the one this preamble names — truthful attribution wins.

Host class: **stdlib**. No `python-flint` or SciPy required. Do not add a heavy dependency without saying why in your pre-registration.

## Your base — one commit, and it does not move

    git fetch origin --tags
    git log -1 --format=%H batch14-base      (the commit)
    git log -1 --format=%T batch14-base      (the tree)
    git checkout batch14-base

**`batch14-base` is an annotated tag, not a branch.** Check out that exact commit,
run the delivery check against it, and cut your bundle against it. Do not
substitute `origin/main`: it can advance while you are running, and a base that
moves under a session is how a worker delivers against a tree it never read. Two
earlier versions of this rule were wrong — a stamped hash that named the commit
before the board, then a moving ref — and the tag is the third and last answer.

**Use the two commands above exactly.** `git rev-parse batch14-base` returns the
**tag object**, not the commit — an annotated tag is its own object,
and feeding that hash to `check_delivery.py --base` or to a diff will not do what
you expect. `git log -1 --format=%H` peels it for you and contains no `^` or `{}`,
which some shells treat specially. The integrator shipped a draft of this packet
telling you to run the wrong one.

**Your dispatch message states the expected commit and tree.** Record both values
in your pre-registration and check they match what the tag resolves to. They are
deliberately not written into this file: a packet that names its own commit's
hash cannot exist, because committing the packet changes the hash. That mistake
has now been made three times on this batch — in the board header, in the
delivery rule, and in a draft of this packet — so the tag is the name and the
message carries the value.

If the tag is absent, your clone predates the freeze: stop and say so rather than
guessing a base.

## Before anything else

1. Confirm the tree carries `docs/batch14_board.md` (v0.4 or later),
   `docs/PROVED.md`, `docs/brief_wording.md`, `docs/b14_claude_scratch_code.md`
   and `docs/batch14_reconciliation.md`. **If any is missing, stop and say so.**
2. Read, in full, before writing any code: `docs/batch14_board.md` — the whole
   of §1 and §2, not only your own entry — then `docs/PROVED.md`,
   `docs/brief_wording.md`, and `docs/batch14_reconciliation.md`.
3. Write `results/PREREG_b14_04.md` — question, instrument, objects, decision
   table, falsifiers, stopping rules, labelled expectations — **commit it, then
   compute.** Anything not pre-registered is reported as exploratory. Dated
   addenda are fine and are committed before the measurements they govern.
4. Check your toolchain rather than assuming it, and record what you installed:
   `python3 -c "import numpy; print('ok')"`.

## The two objectives, so you know which one you serve

    1.  a positive multiplicity obstruction      D = mult_pad - mult_det > 0
    2.  permanent-specific equations             mult_pad < mult_red

**The second is not necessary for the first.** `P` inside `D` forces
`mult_pad <= mult_det` at every weight, so `mult_pad > mult_det` refutes
containment whether or not the equation is permanent-specific.

At LMR, `a = 274`, `m_det = 273` exactly and `m_pad >= 269`, so `D` lies in
`[-4, +1]`. The batch's centre of mass is spent on closing our own main
candidate, because closing it cheaply is worth more than sampling around it, and
because Lemma T makes the alternatives conditional on the same number.

## Your assignment, verbatim from the board

### 4 — stdlib — second-method recounts

**Inputs** `results/b13_01_hpad.json`, `analysis/wk13_b13_01_hpad.py`,
`analysis/wk9_s42_census.py`, `docs/s57_report.md`, `docs/b14_strategy_memo.md`,
`results/b14_prep/ladder_recount.json`, `docs/b14_claude_scratch_code.md` and the
`analysis/b14_claude_*` scripts it indexes.

**The scratch code is the thing you must not reuse.** `b14_claude_hpad.py` and
`b14_claude_stable_count.py` are where 159, 533 and the `a_∞` values came from;
they are banked so the numbers can be replayed, not so they can be confirmed.
Replaying them is not a recount.

**The independent route exists and is cheap — it is not yours to invent.** Astra
piloted it before dispatch: `analysis/wk8_s30_pleth`'s `pleth_p` and `chi`
(power-sum plethysm and Murnaghan–Nakayama characters, banked at s30), with a
fresh interlacing enumeration of the horizontal strips and
`p_r[h₃] = (p_r³ + 3·p_r·p_{2r} + 2·p_{3r})/6`. Do **not** call `amb`, which
decomposes the whole ambient degree for nothing. On the integration machine this
returned **73 in 11.8 s and 159 in 38.4 s**, with all 15 and all 27 channels
matching the Weyl route *partition by partition*, importing neither `a_weyl` nor
any `b14_claude_*` counter. Astra's pilot script and outputs are banked at
`results/b14_prep/astra_slot04_pilot/`.

That is method diversity and it discharges the 73/159 half at a cost of under a
minute. **The values are therefore already observed — do not present them as
blind predictions.** Your core is to formalise the route, state and control its
conventions, and pre-register it properly. The two stable coefficients are the
part still open: take the degree-33 and degree-35 parts of
`∏_{j∈{2,3,4}} (Σ_{k≥0} h_k[h_j])` and a character scalar product with the tail.
That runtime is unmeasured — bound it.

Four quantities are load-bearing. Two now have a second route; two do not:

| quantity | value | routes | status |
|---|---|---|---|
| `dim N₁₃` | 73 | Weyl alternation **and** power-sum/MN characters | **two methods agree, channel by channel** |
| `h_pad((25,17,2⁷),14)` | **159** | Weyl alternation **and** power-sum/MN characters | **two methods agree, channel by channel** |
| `a_∞(19,2⁷)` | 392 | one stable-slice implementation | **single method — your priority** |
| `a_∞(21,2⁷)` | 533 | one stable-slice implementation | **single method — your priority** |

So the priority has moved. 73 and 159 need formalising and controlling, not
discovering; **392 and 533 are the open ones.** Recount those by a **genuinely
different** method — character inner products,
cycle-index plethysm, or another explicitly justified route. A second
implementation of the same Weyl formula is cross-checking, not method diversity,
and does not discharge this.

**159 was the priority and no longer is** — Astra's pilot settled it before
dispatch. It remains the target dimension at rung 14, where `D = −4` would be
decided, so formalise it properly; but the open single-method values are 392 and
533. **Already done, do not repeat**: the integrator reproduced
390, 391 and 532 on the house `a_weyl`, calibrated against three banked values
(`results/b14_prep/ladder_recount.json`), and re-ran `b14_claude_hpad.py` on the
integration machine — control `h_pad(21,17,2⁷;13) = 73` PASS with B13-01's
fifteen per-strip `a3`, then `h_pad((25,17,2⁷),14) = 159` over 27 strips
(`results/logs/b14_claude_hpad_verify.log`). Both are reproduction, not method
diversity, and are recorded as such — the character pilot above is what gave 159
its second lineage, not these.

## The rules that have each cost this programme a session

- **A nonzero minor is a rank FLOOR.** It proves `i <= a - k`. A sampled deficient
  rank bounds `i` from above and **never** establishes `i >= 1` on its own. The
  single exception is `complete_interpolation`, and it needs all four conditions:
  `dim N = h` proved, `h` members exhibited, a nonzero `h x h` minor at `P`, and
  exact source arithmetic. `PROVED.md: evaluation_cannot_certify_i_ge_1` carries
  the corrected statement; an earlier wording denied the exception outright.
- **A check that cannot fail is not a check.** `PROVED.md:
  check_must_be_able_to_fail` lists six instances in batch 13. There is now a
  seventh, and it is the integrator's: the batch-14 reachability script reported
  both controls PASS on an **empty** census, because `all()` and `not any()` over
  nothing are vacuously true, and the integrator replayed it and certified the
  controls without testing that either could fail. **Feed every control an input
  that must make it fail, and report that you did.**
- **Two `exps` orderings exist and they are opposite.** `wk8_s30_core.exps` runs
  the first exponent up from 0; other modules run it down from `n`. Resolve a
  letter by `E.index(...)` in the ordering of the module you are calling, never by
  a literal. Three sessions have paid for this.
- **A transported certificate ships its points and its `u`-values**, and records
  `u(P_j) != 0` at each. One `u`-zero voids every transported row in its column,
  silently.
- **Stored value matrices carry a `values_are` field** naming any transform,
  beside the numbers and not only in a sibling string.
- **`n_chi` is not `N_S/|Stab|`.** That quotient is neither an upper nor a lower
  bound. `FORMAT.md` records `N_S = 211636`, `|Stab| = 2`, `n_chi = 82004`. The
  invariant is `n_chi <= N_S`; measure `n_chi` rather than deriving it.
- Both house primes, `2147483647` and `2147483629`. `rank_p <= rank_Q`.
- `python-flint` for exact linear algebra. Pre-registration before computation.
- Runs bounded at launch with `timeout` and `ulimit -v`, pid written to
  `results/logs/<run>.pid`, ended only by that recorded id.
- Files over 5 MB are not committed. Logs under `results/logs/`. Repository
  configuration is append-only.
- Never touch `paper/det3-conductor.tex`, `paper/det4-onset.tex`,
  `PROJECT_NOTES.md`, `docs/boundary_deficit.html` — the integrator is the only
  writer of those four.

## Delivery

**Deliver by bundle; do not push.**

Branch named for this session; bundle against the tag:

    git bundle create b14_04_<name>.bundle batch14-base..HEAD

with a `.md5`. Parts are numbered from `part00`, contiguously; your report states
the total part count in its first paragraph; the `.md5` names bare filenames and
carries a digest for the whole file and one per part.

Run `python3 tools/delivery/check_delivery.py --branch <your branch> --base
<the commit from `git log -1 --format=%H batch14-base`>` before creating the
bundle, then rerun it **with** `--bundle <file>` once the file exists. Use that
command, **not** `git rev-parse batch14-base`, which returns the tag object.

## Report

`docs/b14_04_report.md`. Label every statement **PROVED** / **CERTIFIED** /
**ADOPTED** / **MEASURED** / **CONDITIONAL** / **NOT REACHED**. Say what you did
not do, and price what you did not reach so the next batch can plan against it. A
negative characterised over a stated, priced region is a deliverable; an unstated
gap is not.

**Report defects in this assignment — the integrator wants them.** Every round of
this batch's planning, the sharpest corrections came from a session or a reviewer
correcting its own brief. The integrator has been wrong about the delivery base
three times, about a control that could not fail, and about four entries in the
index you are being told to read.

## Checkpoints

An early input-and-control checkpoint; a substantive update partway; a usable
report or a resumable handoff by the end of your window.

**Declare your actual host resources.** Twelve sessions do not imply twelve
independent memory budgets.

No external announcement or publication is part of this assignment.
