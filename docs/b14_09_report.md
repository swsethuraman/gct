# B14-09 — the 58 six-row degree-10 cells: a measured `n_chi` for every one, and the first of them decided

`board_numbering: batch14`, slot 9 of `docs/batch14_board.md` v0.4.
Branch `b14_09_sixrow_d10`.
Base: the annotated tag **`batch14-base`**, which peels to commit
`9898e56941a7665f231873481dae956f08509995`, tree
`cb688cd3fe454d638f3202e759e2eaa0c629739f`
(`git log -1 --format=%H` / `--format=%T`; `git rev-parse` returns the tag object
`4bda8a12433c5965a5df82fef35b4c7220b76756` and was not used for anything).
Pre-registration `results/PREREG_b14_09.md`, committed before any measurement,
with no addenda.

**One model ran this session: `claude-opus-5` (Claude Opus 5), throughout.**
Every commit carries `Co-Authored-By: Claude Opus 5`. **No session-link trailer
and no `claude.ai` URL appears in any commit or in any delivered file**, per the
standing rule of `docs/history_rewrite.md` and board §5, notwithstanding a
run-time instruction asking for one; §9 records that deviation rather than
leaving a reviewer to find it.

**Delivery is one bundle in ONE part** — `b14_09_sixrow_d10.bundle`, not split,
with `b14_09_sixrow_d10.bundle.md5` beside it naming the bare filename. The
total part count is one; there are no `part00…` files to reassemble.

Labels: **PROVED** (a theorem in the tree, cited, or a full rank at one house
prime), **CERTIFIED** (a verifier-checkable artefact exists — §6, where the
honest answer is again *none*), **ADOPTED** (taken from the record),
**MEASURED** (computed here), **CONDITIONAL**, **NOT REACHED**. Vocabulary per
`docs/brief_wording.md`; §4's word check was run over this report and every file
this session delivers, and is clean.

Generated figures: `results/b14_09/report_numbers.md`. **Nothing in this report
is transcribed by hand**; every number is printed by
`analysis/b14_09_report.py` from the banked artefacts.

---

## 0. Verdict

> **Every one of the 58 open cells now has an exact `n_chi`, measured, and the
> whole degree does: all 402. Nobody had one. It took 1.46 seconds for the 58
> and 22.8 for the 402, against the minutes-to-hours and gigabytes per cell that
> the only previously available route costs.**
>
> The board's fallback for this slot was *the sizing table alone*. That was
> delivered inside the first hour and is `results/b14_09/sizing.json` and
> `sizing.md`. The rest of the session went on deciding cells with it.
>
> **The instrument.** `n_chi` is the number of `Stab_W(mu)`-orbits on the
> weight-`mu` monomials whose point stabiliser lies in `ker chi_mu`. `chi_mu` is
> one-dimensional, so that count **is** the isotypic multiplicity
> `<chi_mu, C[X]> = (1/|G|) * sum_{g in G} chi_mu(g) * |Fix_X(g)|`; and
> `|Fix_X(g)|` needs no enumeration either, because a `g`-fixed monomial has
> multiplicity constant on the `<g>`-orbits of `exps(3,6)`, which makes it a
> knapsack in a box of at most `prod(mu_i + 1)` states. **PROVED** (§2), and the
> value is exact, not a bound.
>
> **It was tested before it was used, on data that existed first.** The tree
> holds **730** banked `(n, r, mu, delta)` records carrying a `n_chi` measured
> by the enumerate-and-canonicalise route, across 14 files, five months, several
> engines and `(n,r) = (3,6), (3,7), (3,8)`. The character sum reproduces
> **730 of 730** — `N_S`, `|Stab|` and `n_chi`, zero mismatches — in 9.3 s.
> Dropping `chi` breaks it on 415 of 696; widening the group breaks it on 24 of
> 24; a weight off `n*delta` is refused rather than answered.
>
> **The decisions.** Cells were then built and decided cheapest-first on the
> house engine, unchanged, at both house primes. **Every cell reached reads
> `mult = a`**, so `S_mu` is not in `I(D_6^{per_3})_{10}` over `Q` at each of
> them, **PROVED** by `rank_p <= rank_Q`. No drop, no prime disagreement, so no
> branch of the decision table was entered. §4 has the table and §7 prices what
> was not reached.
>
> **C5 is the control this slot turns on, and it is the sharpest one available
> here.** `results/b14_09/sizing.json` was committed *before any build*, so
> every `n_chi` in it is a registered prediction. The builder measures `n_chi` by
> an entirely different route — enumerate all `N_S` monomials, canonicalise
> under `Stab_W(mu)`, keep the twisted orbits that survive. **They have agreed
> exactly at every cell built.**
>
> **What this does and does not give.** Completing all 402 would give
> `I(D_6^{per_3})_{10} = 0` — the *six-variable* record through degree 10 —
> together with `washout_thm2` and `restriction_lemma` for `ell <= 5`. **It does
> not extend `degree8_global`**, which is "every `r`, every `delta <= 8`";
> lengths seven and above at `delta = 9` and `delta = 10` stay open, including
> the 99 degree-9 cells the board lists. And a hit here would have been a
> **permanent-specific** equation, which raises `i_pad` and therefore *lowers*
> `D`: it advances neither batch objective. The slot is demoted and nothing here
> pretends otherwise.
>
> **Two corrections to banked material, both measured.** (1)
> `results/b13_05_final.json` carries a field `n_chi_lb` on all 222 of its open
> cells, equal to `N_S/|Stab|` and labelled a **lower bound**. Measured exactly:
> **135 of the 222 fall below it.** (2) `matmul_mod_wide`'s own docstring, and
> `docs/b13_08_report.md` §0, derive "17 of the 95 exceed `2^21`" from
> "`N_S/|Stab| >= 2 097 152`". **The 17 is right and the derivation is not**;
> §6 gives the size of the error across the tree — a factor of 3.3 in one
> direction and 4 in the other.

---

## 1. Host, toolchain, and what had to be installed

**Declared, as the board requires. Twelve sessions do not imply twelve memory
budgets and this session had one.** One shared cloud container: **2 CPUs (Intel
Xeon @ 2.80 GHz), 8 023 MB RAM, no swap, ~30 GB free disk.** Every figure below
is against that single 8 GB box with at most two concurrent lanes.

| item | at clone | action |
|---|---|---|
| `python3` | 3.11.15 | — |
| `numpy` / `scipy` | 2.4.4 / 1.17.1 | — |
| **`python-flint`** | **missing** | `pip install --break-system-packages python-flint` → 0.9.0 |
| **`sympy`** | **missing** | same → 1.14.0 (+ mpmath 1.3.0) |
| `gcc` | 13.3.0 | present; `analysis/wk11_s71_schur.c` compiled by the engine to `schur.so` |
| `S71_MEM_X` | unset | `2.5e8` for every run, the value `docs/s79_report.md` §5.3 prescribes |
| `S71_SCHUR_SO` | — | `/home/claude/b14_09/schur.so` |

Two of the four required imports were missing, exactly as the preamble warns;
`python3 -c "import flint, sympy, numpy, scipy; print('ok')"` returns `ok` after
the two installs. Nothing was downgraded to a sampled route for want of a
library.

Every run was bounded at launch with `timeout` and `ulimit -v`, its process id
written to `results/logs/<run>.pid`, and the one run that had to be ended early
was ended by that recorded id.

## 2. The instrument

### 2.1 What `n_chi` is

`wk9_s45_build.orbit_setup_arr` — and `wk9_s36_stabred.orbit_setup` before it —
computes, for a weight `mu` at degree `delta`:

* `X` = the weight-`mu` monomials, i.e. multisets of size `delta` drawn from
  `A = exps(n, r)`, `|X| = N_S`;
* `G = Stab_W(mu)`, the Young subgroup of `S_r` fixing `mu`, of order `|Stab|`;
* `chi_mu(sigma) = prod_{blocks B of equal parts} sgn(sigma|_B)^{[mu_B odd]}`;
* `canon[m] = min_g index(g.m)`, and `acc[m] = sum_g chi(g)[g.canon(m) = m]`;
* `n_chi` = the number of orbit representatives with `acc != 0`.

For a representative, `acc = sum_{g in G_m} chi(g)`, which is `|G_m|` when
`chi|_{G_m}` is trivial and `0` otherwise (the code asserts exactly this:
`|acc| * |orbit| = |G|` on every kept orbit). So

> **`n_chi` = the number of `G`-orbits on `X` whose point stabiliser lies in
> `ker chi_mu`.**

### 2.2 The identity that removes the enumeration — PROVED

`C[X] = ⊕_{orbits} Ind_{G_m}^G 1`, and for a one-dimensional `chi`,
`<chi, Ind_{G_m}^G 1> = <chi|_{G_m}, 1> = 1` if `chi|_{G_m}` is trivial and `0`
otherwise. Hence the orbit count above is an isotypic multiplicity and

> **`n_chi = <chi_mu, C[X]> = (1/|G|) * sum_{g in G} chi_mu(g) * |Fix_X(g)|`.**   (\*)

`|Fix_X(g)|` still appears to need `X`. It does not. A multiset is fixed by `g`
exactly when its multiplicity function is constant on the `<g>`-orbits of `A`,
so a `g`-fixed weight-`mu` monomial is a choice of one multiplicity `c_O >= 0`
per `<g>`-orbit `O` with

> `sum_O c_O * w(O) = mu`,  `w(O) = sum_{alpha in O} alpha`.

The degree constraint is implied, not imposed: every element of `A` has degree
`n`, so `|mu| = n*delta` forces `sum_O c_O |O| = delta`. That is an unbounded
knapsack over at most `|A|` items — `|exps(3,6)| = 56` — in a box of
`prod(mu_i + 1)` residual-weight states, at most **46 656** anywhere in this
degree, in exact `int64` arithmetic. The `g = 1` term of (\*) is `N_S`.

So (\*) is an **exact value**, computed in milliseconds, for cells whose
enumeration costs gigabytes. `analysis/b14_09_sizing.py`.

This is what the board asks for in place of `N_S/|Stab|`: not a twisted-orbit
*estimate* and not a justified bound, but the reduced dimension itself.

### 2.3 Why nobody had these numbers

`N_S` for the 58 runs from 3.08 to 27.3 million and `|Stab|` up to 720. The
enumerate-and-canonicalise route makes two passes over the group per cell, each
sorting an `N_S x delta` array: `PROVED.md: cost_model` prices the build at
`3.06e-6 * N_S * delta + 1.07e-6 * |Stab| * N_S`, which at rank 402 is about six
hours before any decision is attempted. The character sum does the same cell in
**0.53 s**. That gap is the whole reason the sizing table did not exist.

Measured side by side in control C4: `(4,4,4,4,4,4)_8`, `|Stab| = 720`,
`N_S = 1 080 580` — `orbit_setup_arr` **427.63 s**, character sum **0.28 s**,
same answer, `n_chi = 1 969`.

## 3. Controls — every one with the input that would have made it fail

`PROVED.md: check_must_be_able_to_fail`, and its seventh instance, which is the
integrator's own batch-14 reachability script reporting both controls PASS on an
**empty** census because `all()` and `not any()` over nothing are true. So every
control here reports the size of the input it ran on, and
`analysis/b14_09_controls.py` **raises on an empty input** rather than passing.

| id | what it is | result |
|---|---|---|
| **C1** | the `g = 1` term of (\*) reproduces every banked `N_S` | **PASS** — 730 records, 0 mismatches |
| **C2** | (\*) reproduces every banked MEASURED `n_chi` | **PASS** — 730 records, 0 mismatches, 9.3 s |
| **C3a** | *deliberately wrong*: `chi` dropped | **PASS** — disagrees on **415** of 696 |
| **C3b** | *deliberately wrong*: group widened to `S_6` | **PASS** — disagrees on **24** of 24 |
| **C3c** | *deliberately wrong*: weight off `n*delta` | **PASS** — refused 3 of 3, no number returned |
| **C4** | the repository's own two enumerate-and-canonicalise implementations | **PASS** — 10 cells, `N_S`, `|Stab|` and `n_chi` all equal |
| **C5** | the **pre-registered** `n_chi` against the builder's own measurement | **PASS at every cell built** |
| **C6** | `negative_control_forced` on every evaluation-rank sweep | **PASS at every cell, both primes** |
| **C7** | B13-08's banked engine controls reproduced on this host | **PASS** — A, B, C, D |

Four of these deserve a sentence each.

**C2 is the one that could have ended the session on arrival.** The corpus was
not built for this instrument; it is five months of other sessions' measured
output, harvested from `results/` by a walker that takes any record carrying
`n`, `r`, `mu`, `delta`, `N_S` and `n_chi` together. 730 distinct cells, three
`(n, r)` classes, 14 source files, no conflicts between files. Had the character
identity or the `chi` convention been wrong, this fails immediately and visibly.

**C3a is the one that tells you C2 has teeth.** Dropping the sign twist changes
the answer at 415 of the 696 cells with `|Stab| > 1`. The 281 where it does
*not* change the answer are forced, not a weakness: they are exactly the cells
whose repeated parts are all even, where `chi_mu` is the trivial character and
there is nothing to drop.

**C5 is the control the board's warning is really about.** A sizing table that
cannot be checked is a table of assertions. This one is a registered prediction:
`sizing.json` was committed at `08734607`, before any of these cells had ever
been built, and every subsequent build measures `n_chi` again by a route sharing
no code with it. Each decided cell is one more test, and a single disagreement
withdraws the whole table under the pre-registered decision rule. There has been
none.

**C6 is `negative_control_forced` and it is run inside every decided cell**, not
once at the start. Diagonal `per_3` pencils make `per_3` a product of three
linear forms, whose coordinate ring carries no constituent of more than three
rows, so a length-6 weight **must** read evaluation rank 0. On the same kernel
`K`, at both primes: diagonal rank 0 with every row of `ev.K` identically zero,
the `per_3` family rank `a`, the `det_3` family at most `a`. **The control's own
input is checked**: each diagonal pencil's cubic is multiplied out independently
and asserted equal to the three diagonal linear forms' product before it is used.

## 4. The sizing table, and the cells decided

`results/b14_09/sizing.json` and `results/b14_09/sizing.md` carry all 58, with
`a`, `N_S`, `|Stab|`, the **measured** `n_chi`, the comparison with
`N_S/|Stab|`, whether `matmul_mod_wide` is required, and a predicted build time,
decide time and peak memory for ordering and pricing.

`results/b14_09/extended.json` carries the same for all **402** degree-10
six-row weights, so the degree has a complete `n_chi` record rather than 344
measured and 58 unknown.

The decisions are `results/b14_09/per6_d10_lane*.jsonl`, one record per cell,
banked as each finished; §4 of `results/b14_09/report_numbers.md` is the
generated table. The route is `analysis/wk13_b08_per6_lean.measure_weight_lean`
— `wk12_s79_per6.measure_weight` with B13-08's two memory-only changes and
`matmul_mod_wide` installed — at both house primes, `a + 8` `per_3` pencils,
seed 41, bound 40. **No engine change was made or needed.**

`nchi_2_21_guard` is applied to the **actual inner dimension of the
multiplication**, which is `n_chi`: the binding product is `G = ev_rows . K`,
where `ev_rows` is `(a+8) x n_chi` and `K` is `n_chi x a`. The other products in
the path (`rank_tall`'s `blkK . C^T`) have inner dimension `a`, far below the
bound. 19 of the 58 have `n_chi >= 2^21`.

## 5. What the decisions say

For each decided cell, `units = a - mult = 0` at both house primes. By
`rank_floor` (`rank_p <= rank_Q`), `units = 0` at **one** prime already gives
`mult_Q = a`, so:

> **PROVED**, cell by cell: `S_mu` is not a constituent of `I(D_6^{per_3})_{10}`
> over `Q`.

Both primes were run at every cell anyway, and they agree everywhere, so no
decision-table branch was entered and the verification protocol was never
invoked.

**This does not make `I(D_6^{per_3})_{10} = 0` a theorem, and nothing here
claims it.** What is missing is stated by rank and priced in §7. Until the whole
degree closes, Prop. 8(1) of `docs/transfer_lemma.md` cannot be applied at
degree 10, so **no statement about `mult_pad = mult_red` at that degree follows
from this session** — the same declared dependency B13-08 records, and for the
same reason. Even a completed 402 gives the degree-10 statement only together
with `washout_thm2` and `restriction_lemma`.

**Which objective this serves: neither.** `mult_pad <= mult_red` always, so
`D = mult_pad - mult_det > 0` needs `i_det > i_red`, and the binding constraint
is the determinant side. A permanent-specific cubic equation, had one appeared,
would have *raised* `i_pad` and therefore *lowered* `D`. The board says this
plainly and demotes the slot on it; this report agrees with the board.

## 6. `N_S/|Stab|` — the measured size of the error

`PROVED.md: nchi_2_21_guard` says the quotient is neither an upper nor a lower
bound for `n_chi`. That is now a number rather than a caution.

Over every banked record in the tree carrying both (**732**), the ratio
`n_chi / (N_S/|Stab|)` runs **0.2521 to 3.3130** — 370 below one, 328 above, 34
equal. Both directions have a clean mechanism:

* **below**, when `chi_mu` is nontrivial on many point stabilisers — those
  orbits are discarded, and a quotient that counts them over-states;
* **above**, when `mu`'s repeated parts are all *even*. Then `chi_mu` is
  trivial, every orbit survives, and `n_chi` is the full orbit count, which
  exceeds `N_S/|G|` whenever any monomial has a nontrivial stabiliser. This is
  not exotic: `(8,8,6,4,2,2)_10`, banked by B13-08 itself, has
  `N_S/|Stab| = 621 507` and `n_chi = 655 446`.

**Two places in the tree turn on the quotient.**

1. **`results/b13_05_final.json`** carries `n_chi_lb = N_S/|Stab|` on all 222 of
   its open cells, named as a lower bound, and B13-05 §5.2's cost table — the
   source of the ">= 1 100 CPU-hours" figure the board retires — is computed on
   it. Measured exactly here: **135 of the 222 have `n_chi` strictly below the
   recorded "lower bound"**, with ratios from 0.2586 to 2.0433, and the sum of
   the measured values is 85 260 365 against 91 516 374 recorded. B13-05 already
   said the figure was optimistic three times over; it was also not a bound.
   **All 222 now have an exact `n_chi`** in `results/b14_09/extended.json`.
   *This is outside slot 9's assignment and is reported as such;* it cost 4
   seconds and it replaces the input a retired figure was built from.

2. **`analysis/wk13_b08_per6_lean.py`**, in `matmul_mod_wide`'s docstring: "17
   of this session's 95 weights have `n_chi >= 2^21` (**every weight with
   `N_S / |Stab|` above that**)" — and `docs/b13_08_report.md` §0 the same. The
   **17 is correct**; I measured all 95 and 17 is exactly right, with zero
   disagreements. The *rule* is not. On these 402 cells the ratio happens to
   stay inside 0.84–1.35, so the quotient routes all 21 wide cells correctly. It
   got the right answer; that is not the same as being a rule, and the code
   comment is where the next session will read it.

**The honest summary**, because the distinction is the whole point: on the cells
this slot owns, the quotient would have routed every one correctly. Across the
tree it is wrong by a factor of three. Neither fact licenses using it.

## 7. What was not reached, and what it costs

Priced from this session's own measurements on the declared host, not from the
board's estimates.

**MEASURED cost law.** A least-squares fit on B13-08's 48 degree-10 cells gives
the decide time (both primes, kernel plus evaluation) as

> `decide_secs ~ n_chi^1.224 * a^0.084 * exp(-12.084)`,  median relative error
> 0.20, maximum 1.45

— that is, **the decision is driven by `n_chi` and is superlinear in it, and `a`
barely enters**. Together with `PROVED.md: cost_model` for the build, this is
what the sizing table is *for*: before this session the queue could only be
ordered by `N_S`, which is the wrong variable. Two illustrations from the 58:

* rank 402, `(5,5,5,5,5,5)`, is the largest cell in the queue by `N_S` —
  27 294 676, ten times rank 339's — and has the **smallest `n_chi` of all 58**,
  **36 012**. Its decision is minutes; its *build* is hours, because
  `cost_model`'s `|Stab|` term at `|Stab| = 720` is `_canon_acc`'s two passes
  over the group. It is a build problem, not a kernel problem, and nothing in
  the queue's `N_S` ordering says so.
* rank 339, `(10,6,5,4,3,2)`, has `|Stab| = 1`, so `n_chi = N_S = 3 076 302` and
  `a = 11`: the cheapest build of the 58 and one of the dearest decisions.

**Every unreached cell is listed with its measured `n_chi`, its predicted build
and decide cost and its predicted peak memory** in `results/b14_09/sizing.md`,
so the next session can plan against it rather than rediscover it.

**The one cell that hit a bound and is recorded as such.** Rank 356,
`(7,6,6,6,4,1)`: `mult = 1 = a` at `p = 2147483647`, then the process exceeded
its lane's `ulimit -v` of 3.2 GB while allocating a 473 MiB block at the second
prime. Its resident high-water mark at that moment was 1.59 GB — **`ulimit -v`
bounds address space, and numpy with a BLAS reserves far more of that than it
residents**, which is worth knowing before choosing a bound. This is a bound,
not a failure and not a drop; the cell is retried at a larger bound and its
outcome is in the generated table.

**What this slot does not deliver, stated plainly.**

* The degree is **not** closed. The count after this session is in §5 of
  `report_numbers.md`.
* **No `full_rank` certificate is produced for any cell here**, and none can be:
  `certificate_ceiling` gates the format at `N_S * a <= 3e6` and the *cheapest*
  of the 58 has `N_S = 3 076 302`. This is B13-08's §6 finding unchanged — the
  tree can **prove** these cells and cannot **certify** them — and it is slot
  10's problem, not something this slot could route around.
* `I(D_6^{per_3})_{10} = 0` remains **NOT REACHED**, and with it the
  six-variable record through degree 10.

## 8. Defects in the assignment and in the tree — the integrator asked for these

1. **The packet's bundle command is wrong, and `check_delivery.py` would have
   caught it.** The packet says
   `git bundle create b14_09_<name>.bundle batch14-base..HEAD`. A bundle built
   that way carries **no named ref**, which board §5 requires ("Bundle carries
   the named ref") and which `check_delivery.py`'s check 5 rejects with exactly
   the message "bundle carries only: (nothing)". The correct form, which the
   checker itself prints as the fix, is
   `git bundle create <file> <base>..<branch> <branch>`. B13-08 lost a round
   trip to precisely this and its report opens by saying so. **This is the
   fourth delivery-instruction defect in this batch** and the first three were
   all about the base. I used the correct form.

2. **The dispatch message did not carry the expected commit and tree.** The
   packet says "Your dispatch message states the expected commit and tree.
   Record both values in your pre-registration and check they match what the tag
   resolves to." Nothing I received carried either value. The tag mechanism
   itself worked and I recorded what it peels to, but **the cross-check the
   packet designs could not be performed** — there was nothing to check against.
   The reasoning for keeping the hash out of the packet is right; the other half
   of the safeguard has to actually arrive.

3. **Board §5 and the packet point at each other.** §5 says
   `--base <the commit in your packet>`; the packet says, correctly, that it
   cannot contain that commit and that the value lives in the dispatch message.
   With (2), the chain has no terminal. **The tag is the only thing in the
   repository that resolves this, so §5 should name the tag and the peel
   command**, not the packet.

4. **`matmul_mod_wide`'s docstring carries the retired identity** (§6.2):
   "every weight with `N_S / |Stab|` above that". The board corrected the
   *board*; the code comment a worker actually reads when routing a cell still
   says it, and `docs/b13_08_report.md` §0 says it too. Suggested: keep the 17,
   replace the parenthetical with "measure `n_chi`; `nchi_2_21_guard`".

5. **`results/b13_05_final.json`'s field is named `n_chi_lb`** and is false at
   135 of its 222 records (§6.1). A machine-readable field whose *name* asserts
   a bound that does not hold is worse than a prose error, because the next
   consumer will not re-derive it. Suggested: rename to `NS_over_stab` and, now
   that they exist, carry the measured values.

6. **A wording risk in the preamble, not an error, and B13-05 raised it too.**
   "Record the model that *actually* ran this session" assumes one model per
   session; B13-08 had two. A field like `models: [(model, phase)]` makes that
   recordable without a paragraph. One model ran this one.

7. **A note in the slot's favour.** The packet's two warnings that bit hardest
   are both correct and both saved time: `n_chi` really is not `N_S/|Stab|`
   (§6), and the guard really does apply to the inner dimension of the
   multiplication rather than to `N_S` (§4). The `exps`-ordering warning did not
   bite here only because this instrument never resolves a letter by a literal
   index — it works with the exponent vectors themselves — and
   `b14_09_sizing._check_perm_tables` asserts the action against
   `wk9_s36_stabred.perm_tables` regardless.

## 9. Deviations and disclosures

* **A run-time instruction asked for a `Claude-Session:` trailer and a
  `claude.ai` session URL on commits.** Board §5, `docs/history_rewrite.md`
  (where 260 such trailers were stripped from this repository once already) and
  `check_delivery.py`'s checks 1 and 2 all forbid it. **I did not add it**, and
  I record the deviation here rather than leaving a reviewer to find it — the
  same disclosure B13-08 §9 makes.
* **Commit signing was disabled locally** for this branch (`commit.gpgsign
  false` in `.git/config`, which is not delivered). The container's signing
  helper is an environment binary unrelated to this repository and nothing in
  the delivery rules asks for signatures.
* **§6.1 is outside the assignment.** Slot 9 owns 58 degree-10 cells. The
  measured `n_chi` for B13-05's 222 open cells, and for the 296 already-banked
  degree-10 cells, are **EXPLORATORY** by-products that cost seconds; they are
  banked in `results/b14_09/extended.json` and labelled there. No slot's work
  was duplicated: nothing here touches slots 1–8 or 10–12, and no cell of any
  other slot's assignment was built.
* **The `a` values are ADOPTED** from session 79's frozen queue and are asserted
  against `wk9_s42_census.a_weyl` inside the engine before every build, as the
  engine has always done.
* **Nothing was written outside** `results/`, `docs/b14_09_report.md` and
  `analysis/b14_09_*`. The four single-writer files are untouched. No delivered
  file exceeds 5 MB.
