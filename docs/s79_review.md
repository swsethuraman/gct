# Session 79 reviewed — Part 1 verified, Part 2 undelivered

**Delivery.**  The **final** bundle did not arrive: only
`s79_frontiers.bundle.part02` (7.7 MB) is here and it is not a git bundle by
itself — part 1 of the split is missing.  The **checkpoint** bundle is complete
and verifies (md5 `03aa29df…`, HEAD `616264c`, base `afb8c33`), and it carries
the pre-registration, both instruments, the length-6 calibration and **Part 1
complete**.  Merged at `ac0fdc3`.  Part 2 — the 682 six-row cells and the
cubic-side theorem — is *reported* but not yet *in the tree*, so it is reviewed
below as a report and not as a verified result.

One housekeeping detail: `s79_frontiers_checkpoint1.bundle.md5` records an
absolute container path rather than a bare filename, so `md5sum -c` fails on any
other machine.  Digests should name the file, not its path.

## 1. Part 1, verified — 60 of 60

`analysis/wk12_int_s79_stable_verify.py`.  The claim is a **theorem**, so it got
the theorem treatment: nothing from s79's engine, nothing from s79's own
checker, and nothing from the repository's stable instrument either.  This
script builds its own weight space, its own `a_∞`, its own raising operators,
its own point map and its own elimination.

| check, per block, both primes | result |
|---|---|
| my enumeration of the weight space equals the delivered one **as a set** | PASS (1 668 / 3 716 / 4 636 / 6 922 / 9 166) |
| my Weyl alternation over `S₅` gives `a_∞ = 4` | PASS on all five |
| the delivered kernel has dimension `a_∞` | PASS |
| `E·v = 0` for every kernel vector on **my** raising rows | PASS, nothing skipped |
| my `G = ev·K`, by principal minors, equals the delivered `G` | PASS, up to one global sign |
| rank of **my own** `G` is `4 = a_∞` | PASS |
| every pencil matrix is traceless | PASS |

So `i_det^∞(ρ) = 0` for all five, and with the eleven earlier blocks:

> `|ρ| = 13`, `ℓ(ρ) ≤ 5`, `a_∞(ρ) ≤ 4` ⟹ `i_det^∞(ρ) = 0`  — sixteen blocks,

and by Proposition S every cell `(4δ−13, ρ)` of those sixteen ladders has
`i_det = 0` at **every** degree.  **The theorem stands.**

**The global sign.**  s79's `y_{(d,·)}` are the characteristic-polynomial
coefficients `(−1)^d e_d`; mine are `e_d`.  Every monomial of an odd weight
`|ρ| = 13` carries an odd number of degree-3 generators, since 2 and 4 are even,
so the two conventions differ by a **global** sign on this weight space — which
cannot move a kernel or a rank.  Verified as such rather than assumed.

**Two faults in my own first pass, both worth recording.**

- **The `exps` ordering trap, third time.**  I built the 120 generators with the
  first exponent descending; s79 uses ascending.  My `a_∞` came out `−53 047`
  and the weight spaces differed as sets while agreeing in size.  The verifier
  now **detects** the ordering from the delivered monomials instead of assuming
  it.  My own preamble warns about exactly this and I still walked into it.
- **A vacuous `E·v = 0`.**  My first raising check looked each raised target up
  in the delivered basis and skipped anything it did not find — so under the
  wrong generator ordering it passed on all four vectors at both primes while
  computing nothing.  The image of `E_{i,i+1}` lives at weight `ρ + e_i − e_{i+1}`,
  a *different* weight space; targets are now collected by their multiset and
  nothing is ever skipped.  **A check that can silently drop its own terms is
  not a check**, and this one had been reporting PASS.

## 2. Part 2, as reported — and why it matters more than its own verdict

Not verified here (the bundle is incomplete).  Taking the report at its word:
682 six-row cells with `i_det = 0`, `mult_pad = mult_red` and `i_per4 = 0` at
every one; 63 tails closed for every degree by Proposition S; and, on the cubic
side, **`I(D₆^{per₃})₉ = 0`** — all 210 length-6 weights `μ ⊢ 27` with
`a(μ,9) ≥ 1` have `mult = a` at both primes — so by Prop. 8(1) of the transfer
lemma `mult_pad = mult_red` at **every** six-row weight of degree 9, a theorem
with no points in it.

**This is the same phenomenon the goal cell just showed, at a different length.**

| length | degree | finding | status |
|---|---|---|---|
| `r = 5` | — | `mult_pad = mult_red` | s64 |
| `r = 6` | `δ ≤ 9` | `mult_pad = mult_red` | **theorem** (s79, via `I(D₆^{per₃})₉ = 0`) |
| `r = 6` | `δ ≤ 12`, 682 cells | `mult_pad = mult_red` | measured |
| `r = 9` | `δ = 13` | the padded kernel **is** the reducible kernel | measured (integrator) |
| `r = 9` | `δ = 24` | `U_R = U_P`, `mult_pad = mult_red` | measured (s74, verified here) |

Three lengths, independent instruments, and the same answer: **the permanent is
invisible to this statistic wherever anyone has looked.**  And s79 supplies the
mechanism the goal cell was missing.  Prop. 8(2) says `mult_pad < mult_red` at a
degree-`δ` cell of length `r` **requires `I(D_r^{per₃})_δ ≠ 0`** — a condition on
the *cubic* side, with no padded points, no orbit closure and no `δ`-degree
quartic build in it.

So the screen I drew from the goal cell (`docs/s74_final_review.md` §1 — compute
`i_red` first) has a cheaper upstream form:

> **Compute `I(D_r^{per₃})_δ` first.  It is empty ⟹ no cell of that length and
> degree can carry a permanent-specific equation, whatever its weight.**

At `r = 6` that is one scan per degree for every weight at once, and s79 priced
it: `δ = 9` done (5 884 s), `δ = 10` at 296 of 402 weights, the remaining 106
priced from `N_S = 1.7·10⁶` to `2.7·10⁷`.  At `r = 9`, `δ = 13` is the question
my rung-13 measurement raises and is the same computation one length up.

## 3. Two defects s79 found in my code, both fixed here

**The census counted "open" against one instrument.**  `wk12_int_w13_census.py`
called `a_∞ = 4` "the first open frontier" without joining against the quartic
record, where Proposition S closes a tail whenever a recorded cell with
`a = a_∞` has `mult_det = a`.  Fixed: the census now reports what is closed by
the record and what is open **on both instruments**, at every `a_∞` level, and
the `a_∞ = 5` slot gets the cross-reference automatically.

**And the record itself is stale — a deeper version of the same defect.**
`wk9_s57_lib.negative_record()` reads the ledgers of sessions 36 through 54 and
stops there.  It holds 326 cells.  Sessions 57, 60, 63, 71 and 79 measured cells
it does not carry: of s79's four record-closed blocks it has `(19,6,2,2,2,1)₈`
and `(23,5,2,2,2,2)₉` from s43 but **not** `(19,6,3,3,1)₈` or `(19,4,4,3,2)₈`
from s60.  So every cross-reference against it understates what is closed, by
five sessions' worth.  The census now prints that warning; extending the ledger
list is a batch-13 task and it is cheap.

**The `nullspace(G^T)` defect in `wk11_s71_cell.py`**, which s79 hit on its first
padded drop: `G = ev·K` has rows = points and columns = kernel vectors, so ideal
elements are combinations of *kernel vectors* — `nullspace(G)`, not
`nullspace(G^T)`, which gives combinations of *points* and then multiplies a
`(K_pts − mult) × K_pts` matrix by an `a × n_χ` one.  The shapes agree only when
`K_pts = a`, and `K_pts = a + 8`.  It never ran in session 71 because no drop
occurred there.  Fixed in the length-5 driver too.

## 4. Status

| claim | status |
|---|---|
| the sixteen-block weight-13 stable theorem | **PROVED**, verified here 60/60 on an independent instrument |
| the five blocks' `a_∞ = 4` | **re-derived** by my own Weyl alternation |
| Part 2's 682 six-row cells, all three ideals empty | **reported**, not verified — bundle incomplete |
| `I(D₆^{per₃})₉ = 0`, hence `mult_pad = mult_red` at every six-row weight of degree 9 | **reported as a theorem**, not verified — bundle incomplete |
| `mult_pad = mult_red` at `r = 5, 6, 9` | three lengths, four instruments, no exception found |

**Needed:** `s79_frontiers.bundle.part01`.

Author: Swami Sethuraman, swsethuraman@beneficus.ai, Beneficus AI.
board_numbering: batch12
