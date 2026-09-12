# B14-12 — `(12,4,4,4,4,4)` at `δ = 8`: the last cell of session 79's Q1 queue is closed

board_numbering: batch14
session B14-12, branch `b14-12-q1-last-cell`, pre-registration
`results/PREREG_b14_12.md` committed at `1aed5506` before any measurement.
**Delivery is by git bundle in one part** — the bundle is a single file,
`b14_12_last_q1_cell.bundle`, with `b14_12_last_q1_cell.bundle.md5` naming the
bare filename; there is one part and it is the whole file, so no `.part00`
appears and the whole-file digest is also that part's digest. No push was
attempted.

**Base.** `batch14-base`, resolved with the two commands the packet names:

| | |
|---|---|
| `git log -1 --format=%H batch14-base` | `9898e56941a7665f231873481dae956f08509995` |
| `git log -1 --format=%T batch14-base` | `cb688cd3fe454d638f3202e759e2eaa0c629739f` |
| `git rev-parse batch14-base` (the **tag object** — not a base) | `4bda8a12433c5965a5df82fef35b4c7220b76756` |

All five required documents are present on that tree.

**Model.** The runtime reports the serving model as `claude-opus-5`; the packet
named "Claude". Every commit carries `Co-Authored-By: Claude Opus 5`. No part of
this session ran under a different model as far as the runtime disclosed; that
line is the runtime's report, not an independent observation.

**Host, declared.** **One cloud container — 7.84 GB (`MemTotal` 8,216,192 kB),
2 cores, 30 GB disk.** Not an independent twelfth of anything. `gcc` 13.3.0 was
present; **`python-flint` 0.9.0, numpy 2.4.4, scipy 1.17.1 and sympy 1.14.0 were
not preinstalled and were installed by this session.** Same class of box as
B13-10's and A1's, so their peaks transfer directly.

Labels: **PROVED** (a theorem, or a full rank at one prime, which proves the
statement over `ℚ` by `rank_p ≤ rank_ℚ`) / **CERTIFIED** (an exhibited object
re-checked here on the full operator) / **ADOPTED** (a convention or seed taken
from the tree) / **MEASURED** (computed here, exact mod both primes) /
**CONDITIONAL** / **NOT REACHED**.

---

## 0. Verdict

> **PROVED.** `mult_det((12,4,4,4,4,4), 8) = a = 4` at **both** house primes,
> hence over `ℚ`. So
>
>     i_det((12,4,4,4,4,4), 8) = 0,
>
> and therefore `D = mult_pad − mult_det ≤ 0` at this weight — the padded family
> is not needed for that conclusion, which is the whole economy of going
> determinant-first.
>
> **This completes session 79's Q1 queue.** `results/PREREG_s79.md` §2.4 freezes
> Q1 as 123 six-row cells ordered by `N_S·δ`, ending at this one at `2.16·10⁸`.
> Checked here against the frozen list: **121 of the 123 are in
> `results/s79_cells.jsonl` and every one has `i_det = 0`**; the 122nd is
> `(10,6,6,6,2,2)₈`, closed by B13-10's pilot; the 123rd is this cell. **All 123
> now carry `i_det = 0`.** There is no six-row determinant equation anywhere in
> Q1 — the "successor laboratory" that queue was built to find is not in it.
>
> **This is the first cell built above session 79's own stated build wall.**
> `results/PREREG_s79.md` §2.4: "Build wall: `N_S·δ > 2·10⁸` … is not attempted."
> The largest Q1 cell s79 actually delivered sits at `3.15·10⁷`; B13-10's pilot
> reached `1.47·10⁸`; this cell is `2.16·10⁸`.
>
> **MEASURED — the whole four-family row, as a stretch.** `mult_per4 = 4 = a`
> (**PROVED**, `i_per4 = 0`); `mult_pad = mult_red = 1` at both primes, so
> `D = D_R = −3` as measured, and `D ∈ [−3, 0]` with **both ends proved**.
> `mult_pad = mult_red`: no permanent-specific equation is detected here.
>
> **MEASURED — the cost, and it is not where the board put it.** `n_χ` is
> **244,454**, not the 225,081 the assignment inherited from a quotient the index
> forbids. The build is **2,838 s at 1.483 GB**, against the board's ≈20 minutes
> and ≈2.8 GB; the whole cell peaks at **2.231 GB** against the pilot's 4.53. The
> board budgeted "for the kernel, not the builder"; on this cell the **builder is
> 95 % of the wall time and the kernel never approaches the box**, and the
> reason is `|Stab| = 120` acting in *both* directions at once — a trade the
> index contains in two separate entries and nobody had put together.

---

## 1. What was done, in order

| | |
|---|---|
| pre-registration committed | `1aed5506`, before any measurement |
| input-and-control checkpoint | `994ce630` — all controls PASS, every deliberate-failure input fired |
| scratch/output separation after a tree defect | `d4e4fba4` |
| the cell, determinant column | `5e95b364` |
| the stretch: the other three families, and s79-schema rows | `f94a0cd4` |

Every long run was launched under `timeout` and `ulimit -v` with its own process
id written to `results/logs/<run>.pid` by the running script itself. §7.3 records
where that discipline was briefly wrong and how.

---

## 2. The controls, and the input that made each one fail

`analysis/b14_12_controls.py`, record `results/b14_12/controls.json`, log
`results/logs/b14_12_controls.log`. The packet's rule was taken literally: **each
control was run twice, once on the input it must accept and once on an input for
which its assertion is false**, and both runs are recorded.

| control | on its intended input | on the input that must make it fail |
|---|---|---|
| **T** — toolchain and frozen-queue contract | `a_weyl((12,4,4,4,4,4), 8, 4) = 4` **re-derived here, not inherited**, matching the queue; `L = |exps(4,6)| = 126`; entry bound `\|Stab\|·δ·(n+1) = 4800 < 2¹⁵` | (a disagreement would have stopped the session under S5) |
| **Nc** — rank machinery liveness | `rank_mod_p` returns 0, 7 and 31 on matrices of those ranks, both primes | a wrong asserted rank fires |
| **N.a** — the diagonal pencil *is* the product of its four linear forms | holds on **all** 12 diagonal pencils, by independent repeated multiplication | holds on **0 of 12** generic `det₄` pencils |
| **N.b** — `negative_control_forced` | diagonal `det₄` pencils read **rank 0** at both primes, every row zero | the **generic `det₄` family on the same kernel** reads 4 — so the evaluation-and-rank path is not returning 0 on everything |
| **R** — the `n_χ` **measurement** path | orbit-setup half of `(10,6,6,6,2,2)₈` only: `n_χ = 1,606,104` = banked, `N_S` and `\|Stab\|` also equal | the same comparison against the **queue's estimate** 1,528,114 fails; and an **empty** comparison fails |
| **S** — the driver against banked suite cells | B1 `(38,2,2,2,2,2)₁₂` (**`\|Stab\| = 120`, the target's own stabiliser order**) and A1 `(13,5,2,2,2)₆`: 7 size fields plus per-prime nullity, `\|U\|` and `mult_det` all equal | a **one-field mutation** of the banked record fails |
| **K** — kernel verification | all null vectors satisfy `E·v = 0` on the full `E`; `rank_tall = a` | a kernel with **one entry incremented** does not verify |
| **F** — the `fo='inplace'` deviation | agrees with `fo='copy'` in nullity, rank and `mult_det` on A1 | a mutated `fo='copy'` result fails |

Control R is the one that mattered, and it was designed against the board's
instruction to use `(10,6,6,6,2,2)₈` "as a reference check only — not as new
work": rebuilding that closed cell is 24 CPU-minutes and 4.53 GB, so **only its
orbit-setup half was re-run** — no raising rows, no kernel — because that is
exactly the code path that produces `n_χ`, and it is the one Q1 cell where the
true `n_χ` is banked. It cost 152 s at 1.0 GB and it reproduced 1,606,104.

Control N was then carried **inside the target run itself**, on the same kernel,
in the same process — not run separately and assumed to transfer.

---

## 3. The cell

`analysis/b14_12_cell.py` — B13-10's pilot driver (`wk13_b10_pilot.py`)
re-parametrised over `(λ, δ, n)` with three pre-registered changes:
`blocks='disk'`, `fo='inplace'`, and Control N carried in-process. Every routine
it calls is the tree's own; every letter is resolved through
`wk8_s30_core.exps(n, r)` **by index**, and `n` is passed explicitly to
`ev_rows_from_coeffs` rather than left to that module's default, because the two
`exps` orderings in this tree are opposite.

Records: `results/b14_12/b14_12.json`, `results/b14_12/b14_12_families.json`.
Logs: `results/logs/b14_12_build.log`, `b14_12_kernel.log`, `b14_12_families.log`.

### 3.1 Sizes (MEASURED)

| | measured here | frozen queue | note |
|---|---|---|---|
| `N_S` | **27,009,659** | 27,009,659 | exact agreement |
| `\|Stab\|` | **120** | 120 | `= 5!`, the five equal parts |
| `a` | **4** | 4 | re-derived by `a_weyl`, not inherited |
| **`n_χ`** | **244,454** | *estimate* 225,081 | **the estimate is `ceil(N_S/\|Stab\|)` and is 8.6 % low — §5** |
| rows | **16,480,713** | — | |
| `nnz(E)` | **56,094,024** | — | **half the pilot's 110,695,059**, at 1.47× the `N_S` |
| `nfixed` | 0 | — | |
| `E.data` | `int16`, **max entry 16** | — | against the asserted bound 4,800 |
| orbits dropped | 0 | — | |

`n_χ = 244,454 ≤ N_S` — the invariant that does hold — and `N_S/n_χ = 110.5`,
**not** `|Stab| = 120`. It is 8.6× under `2²¹ = 2,097,152`, so `matmul_mod`'s
correctness guard is nowhere near: `matmul_mod_wide` is **not** needed at this
cell, and that is now measured rather than inferred.

### 3.2 Cover and kernel (CERTIFIED)

Cover **244,444 of 244,454** columns by the `reversed` order — a CERTIFIED rank
floor of 244,444 on `E` at `O(nnz)` — leaving `|U| = 10` and an excess of **6**
over `a = 4` (15.0 s). The pilot's `|U|` was 280 with excess 270; this kernel is
a far easier one.

| prime | nullity | verified on full `E` | `rank_tall(K)` | `mult_det` | `i_det` | kernel s | ev+rank s | HWM GB |
|---|---|---|---|---|---|---|---|---|
| 2147483647 | 4 | **yes** | 4 | **4** | **0** | 9.8 | 50.9 | 1.986 |
| 2147483629 | 4 | **yes** | 4 | **4** | **0** | 11.2 | 48.5 | 2.225 |

`mult_det = a` at one prime already proves `mult_det = a` over `ℚ`; both primes
agree. **`i_det = 0` at `(12,4,4,4,4,4)₈` — PROVED.**

The determinant column was then computed a **second time**, in a separate process
from the stored operator during the stretch run, and agrees.

### 3.3 The forced negative, on this cell's own kernel (MEASURED)

| prime | diagonal `det₄` pencils | every row zero | generic `det₄` family on the same kernel |
|---|---|---|---|
| 2147483647 | **rank 0** | yes | 4 |
| 2147483629 | **rank 0** | yes | 4 |

`A_i = diag(d_{i0},…,d_{i3})` makes `det_4(Σ s_i A_i)` a product of four linear
forms, whose coordinate ring carries no constituent of more than four rows;
`ℓ(λ) = 6 > 4`, so rank 0 is forced by representation theory and needs no banked
history. The generic column beside it is what stops this from being a check that
cannot fail.

### 3.4 The other three families — stretch, reached (§8 of the pre-registration)

`analysis/b14_12_families.py`, on the operator already built, with session 79's
own families, seeds (det 11, red 29, pad 37, per4 47), bound 40 and `K = a + 8`.
`n_red = 234,064` of 244,454 columns; cover(`E_red`) 234,056 of 234,064, **not**
complete, so the sieve certifies nothing here and the `(★)` rank is the
instrument.

| family | `mult` at both primes | label |
|---|---|---|
| `det` | **4** `= a` | **PROVED** over `ℚ`: `i_det = 0` |
| `per4` | **4** `= a` | **PROVED** over `ℚ`: `i_per4 = 0` |
| `pad` | 1 | **MEASURED**; proves `mult_pad ≥ 1`, hence `i_pad ≤ 3` |
| `red` (point-free `(★)`) | 1 | **MEASURED**; proves `mult_red ≥ 1`, hence `i_red ≤ 3` |
| `red'` (sampled points) | 1 | **MEASURED**; `star_eq_pts` = true |

Derived:

- **`D = mult_pad − mult_det`. `D ≤ 0` is PROVED** (`mult_pad ≤ a = mult_det`),
  and **`D ≥ −3` is PROVED** (`rank_p ≤ rank_ℚ` gives `mult_pad ≥ 1`). So
  **`D ∈ [−3, 0]`, both ends proved**, with the measured value `−3` at both
  primes. `D_R` likewise.
- `mult_pad = mult_red = 1` at both primes: **no permanent-specific equation is
  detected at this weight.** That is a measurement of two modular ranks, **not**
  a proof that `mult_pad = mult_red` over `ℚ`.
- `monotone_ok` true; `refute` false; `halt` false.

**The measured `i_pad = i_red = 3` is a ceiling and is not read downward
anywhere in this report** (`PROVED.md: rank_floor`,
`evaluation_cannot_certify_i_ge_1`). This cell has no `complete_interpolation`
certificate and none was attempted, so the single exception to that rule does not
apply here.

---

## 4. Cost and memory — a measured point above `2·10⁸`, and what it does to the ceiling

### 4.1 The build

| phase | seconds | share |
|---|---|---|
| monomials | 25.5 | 1 % |
| **orbit setup** | **1,958.9** | **69 %** |
| raising rows (5 operators + assembly) | 853.8 | 30 % |
| **build total** | **2,838.1** (47.3 min) | peak **1.483 GB** |

Cover 15.0 s; kernel 9.8 / 11.2 s per prime; evaluation and rank 50.9 / 48.5 s
per prime. **Whole cell 2.231 GB.**

### 4.2 Against the two predictions that existed

| estimate | value | measured | error |
|---|---|---|---|
| B13-10 §5: "≈ 20 minutes", from scaling the pilot's wall time by `N_S·δ` | 1,196 s | 2,838 s | **2.4× LOW** |
| `PROVED.md: cost_model` (B13-09 §4), both terms | 4,129 s | 2,838 s | 1.45× high |
| B13-10 §5: "the build is ≈ 2.8 GB" | 2.8 GB | **1.483 GB** | 1.9× high |

The 20-minute figure is the `N_S·δ`-only model that `cost_model` says is "up to
21.7× low. **Do not quote it.**" It has no term for `|Stab|` at all, and
`|Stab|` is 69 % of this build. `cost_model` itself, which does have that term,
over-predicts here by 45 % — it under-predicts the pilot by 16 %, so it is not
biased one way, but it is the model to use and the one that was not used.

### 4.3 The `|Stab|` trade, stated

`|Stab| = 120` acts in **opposite directions** in the same cell, and the index
already contains both halves without putting them together:

- **it costs time** — `cost_model`'s second term is `_canon_acc`'s two passes
  over the group, "a deliberate memory-for-time trade, right at `|Stab| ≤ 120`,
  fatal at 5040". Here it is 1,959 s of a 2,838 s build.
- **it buys memory** — by compressing the target basis. Rows per monomial fall
  from the pilot's **1.47** (`|Stab| = 12`) to **0.61** here; `nnz` falls to
  **0.51×** the pilot's on 1.47× the `N_S`; `n_χ` to 0.15×.

So the lean build rate at this cell is **0.686 GB per `10⁸` of `N_S·δ`**, which
is **below B13-10's whole measured range of 0.99–2.48** and half its pilot rate
of 1.30. B13-10 said the rate "is flat in the range where it matters"; it is flat
*within its suite*, and this point is outside it in the good direction.

**The consequence for the ceiling is a shape change, not a number.** B13-10
extrapolated "a 7.0 GB build budget at the worst observed lean rate gives a build
ceiling near `N_S·δ ≈ 2.8·10⁸`". This cell is at `2.16·10⁸` and built at 1.483 GB
— **21 % of that budget**. Naively the same arithmetic now gives `≈ 1.0·10⁹`.
**Do not adopt that number.** What the two measured points actually show is that
the peak is not a function of `N_S·δ` alone: at fixed `N_S·δ` a larger `|Stab|`
means fewer rows, fewer nonzeros and a smaller peak, and a longer build. A
ceiling quoted in `N_S·δ` alone will be wrong in both directions depending on the
cell's stabiliser. B13-10 saw this coming for one cell — it flagged
`(5,5,5,5,5,5)` at `|Stab| = 720` as "the one to price carefully because `|Stab|`
makes its orbit setup, not its rows, the cost" — and then priced *this* cell by
the rate model anyway.

**On this box the builder was never near the wall and the kernel was never near
the wall.** The board's "budget for the kernel, not the builder" is right about
the pilot, where `n_χ = 1.6·10⁶` gave `|U| = 280`; it is the wrong advice for
this cell, where `|Stab| = 120` gave `|U| = 10` and the kernel ran in 10 s. What
binds here is **wall time in the orbit setup**, and nothing in the assignment
named it.

---

## 5. `n_χ` — the assignment's sizing rests on a quotient the index forbids

`PROVED.md: nchi_2_21_guard` and board §1 both say `n_χ` is **not**
`N_S/|Stab|`; that quotient "is neither an upper nor a lower bound"; the
invariant is `n_χ ≤ N_S`; "measure `n_χ` rather than deriving it".

**Every one of the 123 `nchi_est` values in `results/s79_queue.json` is exactly
`ceil(N_S/|Stab|)`** — 123 of 123, checked in Control T. B13-10 §5 quotes that
field for this cell ("Its `n_χ` is estimated at 225 081 … seven times *smaller*
than the pilot's — so on this evidence the cell is **cheaper downstream** than
the pilot"), and the board's slot-12 entry restates it as "`|Stab| = 120`
compresses `n_χ` sevenfold". Both are built on the forbidden quotient.

| cell | `ceil(N_S/\|Stab\|)` | measured `n_χ` | error |
|---|---|---|---|
| `(10,6,6,6,2,2)₈` (B13-10) | 1,528,114 | 1,606,104 | quotient **5.1 % low** |
| `(12,4,4,4,4,4)₈` (here) | 225,081 | **244,454** | quotient **8.6 % low** |

Two cells, two under-estimates, growing with `|Stab|`. The conclusion the board
drew happens to be **right** — this cell *is* much cheaper downstream than the
pilot — but it was drawn from a number the index forbids, the error is in the
direction that under-provisions, and "sevenfold" is 6.57×. Nothing structural
turned on it here (244,454 is still 8.6× under `2²¹`), which is luck rather than
margin: a cell whose quotient sat just under `2²¹` could be routed to
`matmul_mod` and then assert, and the guard binds on exactly this quantity.

---

## 6. What this does and does not establish

**Establishes.** No determinant equation and no `per₄` equation at
`(12,4,4,4,4,4)₈`; `D ≤ 0` there; and, with the other 122 cells, **`i_det = 0`
across the whole of session 79's frozen Q1 queue**. A first measured build point
above `N_S·δ = 2·10⁸`, and the `|Stab|` trade in §4.3.

**Does not establish.** Anything about `D_6^{per₃}`; anything about `i_red(13)`
or `i_red(14)`; any step toward `D = −4` at LMR. This slot is the board's own
deprioritised one and its result is a closed cell, not a move in the main line.
It does not extend `degree8_global` — that entry is "every `r`, every `δ ≤ 8`",
and this is one weight at `δ = 8` on the **quartic** side. It does not touch the
58 six-row degree-10 cubic cells (slot 9) or the 99 degree-9 cells.

**`i_pad ≥ 1` and `i_red ≥ 1` are NOT REACHED** and cannot be reached by this
instrument: the measured drop to 1 is a ceiling. Reaching them needs a
`complete_interpolation` certificate (Lemma CI), which is slots 1–3's work and
was not attempted here.

**No certificate exists for this cell, and cannot.** `PROVED.md:
certificate_ceiling` gates `full_rank` certificates at `N_S·a ≤ 3×10⁶`; here
`N_S·a = 1.08×10⁸`, thirty-six times over. **This tree can PROVE this result and
cannot CERTIFY it in the present formats** — the exact case that entry describes,
and a concrete instance for slot 3's compact-certificate work. B13-10's pilot is
another (`N_S·a = 1.8×10⁸`).

---

## 7. Defects

### 7.1 In the assignment (the integrator asked for these)

1. **No dispatch message stated the expected commit and tree.** The packet says
   "Your dispatch message states the expected commit and tree … Record both
   values in your pre-registration and check they match what the tag resolves
   to." No such message reached this session, so the cross-check the packet
   requires could not be performed as specified. Substituted: the tag-object hash
   in the second clone on the user's laptop
   (`…\Projects\gct\work\.git\refs\tags\batch14-base`) is
   `4bda8a12…`, identical to what this clone resolves from `origin`. That is
   agreement between two clones of one remote, which is **weaker** than agreement
   with a value fixed at dispatch, and is labelled as such. The batch has now
   been wrong about the delivery base three times by the packet's own count; this
   is a fourth shape — the value moved out of the file and into a message that
   did not arrive.

2. **The packet's own bundle command contradicts the board's delivery rule and
   would fail the gate.** The packet says
   `git bundle create b14_12_<name>.bundle batch14-base..HEAD`. That produces a
   **HEAD-only** bundle. Board §5 says "Bundle carries the named ref", and
   `tools/delivery/check_delivery.py` check 5 rejects exactly this, with the fix
   text `git bundle create <file> <base>..<branch> <branch>` — "a receiver doing
   `git fetch <bundle> <branch>:<branch>` fails against a HEAD-only bundle". The
   board's form was used here. The packet's form should be corrected.

3. **The slot's sizing rests on `N_S/|Stab|`** — §5 above. The quotient
   under-estimates `n_χ` at both cells where the truth is now known, by 5.1 % and
   8.6 %.

4. **The ≈20-minute / ≈2.8 GB budget used the `N_S·δ`-only model** that
   `cost_model` forbids quoting — §4.2. Measured 47.3 min and 1.483 GB. The
   direction that matters is the time: the assignment under-priced the wall clock
   by 2.4×, on a slot whose only real risk was the window.

5. **"Budget for the kernel, not the builder" is the wrong advice for this
   cell** — §4.3. It is drawn from the pilot, where `n_χ` is large and
   `|U| = 280`; here `|Stab| = 120` gives `|U| = 10` and a 10-second kernel,
   while the builder takes 95 % of the wall time. The pre-registration budgeted
   both and assumed neither.

6. **`build_no_longer_binding` is cited as an input and is an extrapolation
   above `1.47·10⁸`.** This cell sat in the extrapolated region. It is now a
   measured point there — and it shows the extrapolation's *shape* is wrong
   (§4.3), not just its constant.

### 7.2 In the tree (found here, reported not patched)

7. **`wk13_b10_lean.raising_rows_lean` removes the caller's scratch directory.**
   At line 501 a `blocks='disk'` run ends with `shutil.rmtree(scratch,
   ignore_errors=True)` on the directory the **caller passed**, not only on the
   `block_*.npz` files it wrote there. B13-10 never met this: its pilot ran
   `blocks='memory'` and its knob variants passed `scratch=None`, which takes the
   `tempfile.mkdtemp` branch the builder does own. **It destroyed a completed
   47-minute build here** — `np.savez` then failed with `FileNotFoundError` into
   the directory the builder had just removed
   (`results/logs/b14_12_build_attempt1.log`). The right fix is for the builder
   to remove what it created rather than the directory it was handed; that file
   is B13-10's and is not edited here. Worked around locally by keeping the
   blocks scratch (`~/b14_12_blocks/<tag>`) disjoint from this driver's outputs
   (`~/b14_12_out`). **Any batch-14 session that takes B13-10 §3's advice to use
   `blocks='disk'` with its own scratch directory will hit this.**

8. **`results/s79_queue.json`'s `nchi_est` is an unlabelled forbidden
   quotient.** The field name says "est" and nothing in the file says the
   estimator is `ceil(N_S/|Stab|)`, which is why two documents quoted it as if it
   were a measurement. A `values_are`-style field naming the estimator would have
   stopped both.

### 7.3 In this session's own conduct

9. **Two control runs were launched with a process id that did not name the live
   process.** The first launcher recorded `timeout`'s pid, not python's; when the
   harness's own tool-call timeout ended the wrapper, python continued as an
   orphan and the recorded id no longer named it — and a later such timeout
   ended a Control R run mid-flight. Fixed by having each script write its own
   `os.getpid()` to `results/logs/<run>.pid` at start, and launching under
   `setsid` so the run is in its own session. Every measurement reported here was
   produced after that fix. The rule was broken twice before it was; the
   preamble's "ended only by that recorded id" is stated here because it was not
   held.

10. **The rank-liveness control was wrong on its first run and the control
    caught it.** `(A @ B) % p` with entries near `p` overflows int64 before the
    mod, and `rank_mod_p` read 40 on a matrix of rank 7. Rewritten to go through
    the tree's own `matmul_mod`, which is also the composition the real rank path
    uses. Recorded because it is the one case in this session where a check
    failed on a true input, and the failure was mine.

11. **One build was run twice.** The 2,838 s build was paid for a second time
    after defect 7 destroyed the first. Both runs are recorded; the first is the
    log only. They agree on every size and to within 6 s on the wall clock, which
    is an unplanned reproduction of the whole build on this host but is not
    presented as a planned control.

---

## 8. Pre-registration scorecard

| id | pre-registered | outcome |
|---|---|---|
| **E1** (0.85) | the build completes inside `ulimit -v 7000000` | **hit** — 1.483 GB, 21 % of the bound |
| **E2** (0.70) | measured `n_χ` exceeds `ceil(N_S/\|Stab\|) = 225,081` | **hit** — 244,454, by 8.6 % |
| **E2′** (0.60) | `n_χ ∈ [225,081, 250,000]` | **hit** — 244,454 |
| **E3** (0.75) | `i_det = 0` | **hit** — at both primes |
| **E4** (0.95) | Control N reads 0 at both primes and all five failure inputs fire | **hit** |
| **E5** (0.55) | whole-cell peak below the pilot's 4.53 GB | **hit** — 2.231 GB |
| **E6** (0.50) | at least one stretch family reached | **hit** — all three, plus the s79-schema rows |
| **E7** (0.65) | `nnz(E)` exceeds the pilot's 110,695,059 | **MISS** — 56,094,024, **half** the pilot's on 1.47× the `N_S` |

**E7 is the informative miss.** The reasoning behind it — "`nnz` tracked `N_S`
across B13-10's suite and `N_S` is 1.47× larger here; `n_χ` bounds columns, not
nonzeros" — is exactly the `N_S`-only thinking §4.3 corrects. Rows and nonzeros
track the **target basis after canonicalisation**, so `|Stab|` divides them too.
That miss is the same error, in my own pre-registration, that defect 4 records in
the assignment.

---

## 9. Not done, and priced

| item | price, from this session's own measured rates |
|---|---|
| a `full_rank` or compact certificate for this cell | **impossible in the present formats**: `N_S·a = 1.08×10⁸` against the `3×10⁶` gate (`certificate_ceiling`). Two closed Q1 cells (this and B13-10's pilot) now sit above it with results that are proved and uncertifiable — concrete targets for slot 3 |
| `i_pad ≥ 1` / `i_red ≥ 1` at this weight | **NOT REACHED and not reachable by evaluation.** Needs Lemma CI: `dim N = h` proved, `h` members exhibited, a nonzero `h × h` minor, exact source arithmetic. Slots 1–3 |
| the remaining `(★)` certification | cover(`E_red`) reached 234,056 of 234,064 red columns — **8 short** of certifying `i_red = 0` by the sieve alone. A different cover order or a small targeted completion would decide it; not attempted, cost well under a minute |
| session 79's **Q2**, the next six-row frontier | **9,952 cells still open** of 10,513. Median `N_S·δ` is `2.44×10⁹`, an order of magnitude past this cell; **7,386 are above s79's `2·10⁸` wall**; **2,643 are at or below this cell's size**. `cost_model` puts those 2,643 builds at **≈ 161 CPU-hours** — a model, not a measurement, and on this host it would be ≈ 161 wall-hours since the box runs one build at a time |
| a re-measured build ceiling as a function of `(N_S·δ, \|Stab\|)` | two points now exist at `\|Stab\|` 12 and 120. A third at `\|Stab\| = 1` or 2 near `10⁸` would separate the terms; B13-10's suite has none above `3.2×10⁷`. One cell, ≈ 1 hour |
| merging these two rows into `results/s79_cells.jsonl` | the rows exist in `results/b14_12/s79_schema_rows.jsonl` in that file's own field set, with every field neither session produced set to null **and named** in `_absent_fields`. Not appended: that file is session 79's delivery and every row in it carries four families and certificates; merging rows with named gaps is an integration decision, not a worker's |

---

## 10. Files delivered

| path | what |
|---|---|
| `results/PREREG_b14_12.md` | the pre-registration, committed before any measurement |
| `analysis/b14_12_cell.py` | the driver: build, cover, kernel, determinant column, Control N in-process |
| `analysis/b14_12_controls.py` | the checkpoint — every control with the input that must make it fail |
| `analysis/b14_12_families.py` | the stretch: pad, per4, red (point-free and sampled) |
| `analysis/b14_12_s79_row.py` | s79-schema rows for this cell and for B13-10's pilot |
| `results/b14_12/controls.json` | the control record |
| `results/b14_12/b14_12.json` | the cell: sizes, phases, cover, kernel, `mult_det`, `i_det` |
| `results/b14_12/b14_12_families.json` | the four-family row |
| `results/b14_12/s79_schema_rows.jsonl` | both rows in `s79_cells.jsonl`'s field set, gaps named |
| `results/logs/b14_12_*.log` | build (and the lost first attempt), kernel, families, controls |
| `docs/b14_12_report.md` | this file |

No file exceeds 5 MB. Nothing was written to `paper/det3-conductor.tex`,
`paper/det4-onset.tex`, `PROJECT_NOTES.md` or `docs/boundary_deficit.html`.
Repository configuration was not modified. No push was attempted. No external
announcement or publication was made.

Author: B14-12, run under `claude-opus-5`.
