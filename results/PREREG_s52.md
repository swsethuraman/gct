# Pre-registration — session 52, the `a = 1` census

Written and committed **before any computation of this session**.  Branch
`s52-aone` off `eb8cecb` (`main`), which is the sync baseline recorded in §8.
Labels used throughout the session and the report: **proved** / **measured** /
**adopted-from-literature** / **expectation**, per `docs/brief_wording.md`.

Brief: `docs/s52_prompt.md`.

---

## 0. A wording correction to the brief, recorded here first

The brief's §0 says "run the degeneracy-direction pre-check in
`docs/brief_wording.md` **§6**".  In the committed `docs/brief_wording.md` the
degeneracy-direction pre-check is **§5**; §6 is the two citation corrections and
§7 is the functoriality pre-check.  Both §5 and §7 are answered in §6 of this
pre-registration.

---

## 1. Scope, fixed before anything runs

The census region is the one the integrator's counts refer to, and it is fixed
now so that a reproduction can be scored:

* `n = 4` (the determinant `det_4`), length-reduced model at `r = 6` variables.
* `ℓ(λ) = 6` exactly; `λ ⊢ 4δ`.
* **obstruction-eligible** means `λ_1 ≥ δ` (Corollary B of
  `docs/reducible_ideal.md`: `λ_1 < δ ⇒ mult_pad = 0`).  `λ_1 < δ` cells are
  onset-only and are counted separately, never merged.
* `a = a(λ,δ)` = multiplicity of `S_λ` in `Sym^δ Sym^4 C^6` (the ambient
  plethysm).
* `h_pad(λ,δ) = mult_λ(Sym^δ V ⊗ Sym^δ Sym^3 V)`, session 42's free
  normalisation bound, with `mult_red ≤ h_pad` **proved**
  (`docs/reducible_engine.md` §B).
* `i_X = dim I(X)^{HWV}_{λ,δ}`, `mult_X = a − i_X`,
  `D = mult_pad − mult_det = i_det − i_pad`.

Degrees: `δ = 7, 8` (reproduction), `δ = 9` (new), `δ = 10` if affordable.

---

## 2. A free lemma, stated before the census so it cannot be fitted to it

**Lemma A (proved, no computation).**  At a cell with `a = 1`:

1. `h_pad < a` ⟺ `h_pad = 0`.  (`h_pad` is a non-negative integer and `a = 1`.)
2. `h_pad = 0 ⟹ mult_red = 0 ⟹ mult_pad = 0 ⟹ i_pad = 1 ⟹ D = i_det − 1 ≤ 0`.
3. Hence **`D > 0` at an `a = 1` cell requires `h_pad ≥ 1`, and in fact requires
   `mult_pad = 1`, i.e. the pad ideal empty at that weight, together with
   `mult_det = 0`, i.e. the determinant ideal containing the whole line.**

*Proof.*  `P_6 ⊆ R_6` gives `I(R_6) ⊆ I(P_6)` hence `mult_pad ≤ mult_red`;
`mult_red ≤ h_pad` is Corollary B2.  With `a = 1` all four quantities lie in
`{0,1}` and the chain collapses. ∎

Consequences fixed now:

* The **informative** `a = 1` cells are exactly those with `h_pad ≥ 1`.  Cells
  with `h_pad = 0` are excluded from every count of evidence in the report, as
  the brief requires — at `a = 1` they are killed by Lemma A, with no
  measurement, and counting them would repeat session 47's error in the opposite
  direction.
* At `a = 1` the "bound fires" language of sessions 42/47 means exactly
  `h_pad = 0`, so the exactness question that session 47 refuted **cannot arise
  at `a = 1`**: `mult_red ≤ h_pad = 0` forces equality.  Nothing in this
  session's census is evidence for or against exactness.

---

## 3. Task 0 — the BIP question

Two determinations, in order.

**T0a (reading).**  Confirm from the paper that Bürgisser–Ikenmeyer–Panova,
*No occurrence obstructions in geometric complexity theory* (arXiv:1604.06431;
FOCS 2016; J. Amer. Math. Soc. **32** (2019), 163–193), Theorem 1.4 carries the
hypothesis `n ≥ m^25`, and that `(n,m) = (4,3)` fails it.

*Logged before the check is written up:* prior **0.97** that the hypothesis is
`n ≥ m^25` as the brief states.  `3^25 = 847,288,609,443`, so if the reading
holds the hypothesis fails at `n = 4` by eleven orders of magnitude and the
theorem is silent — this arithmetic is fixed now so it cannot be adjusted later.

**T0b (mechanism).**  Decide whether the *mechanism* — the argument that
produces a determinant-side occurrence from every padded-permanent-side weight —
survives at `(n,m) = (4,3)` in any form, or depends essentially on heavy padding.

*Logged prediction:* **P1 — the mechanism does not transfer.  Prior 0.85.**
Reason to be tested: the padding hypothesis enters as a bound on the number of
boxes of `λ` outside the first row, of the shape `|λ| − λ_1 ≤ δm`, equivalently
`λ_1 ≥ |λ|(1 − m/n)`.  At `n ≥ m^25` that says `λ` is one very long row with a
body of relative size `≤ m^{-24}`; at `(n,m) = (4,3)` it says only
`λ_1 ≥ |λ|/4`, which is close to vacuous for `ℓ(λ) = 6`.  If the whole
combinatorial regime the argument works in is "long row plus tiny body", it is
absent here.

*What would refute P1:* an argument, valid at `n = 4`, that produces a
determinant-side highest-weight vector non-vanishing at a determinant pencil
from the mere fact that `λ` occurs on the pad side.  Such an argument is the
brief's "negative worth having" and would close the occurrence route outright.

**T0c (the cost, stated whether or not P1 holds).**  Ikenmeyer–Panova /
Dörfler–Ikenmeyer–Panova, *Multiplicity obstructions are stronger than occurrence
obstructions* (ICALP 2019; SIAM J. Appl. Algebra Geom. **4** (2020);
arXiv:1901.04576).  At `a = 1` a multiplicity obstruction **is** an occurrence
obstruction, so the `a = 1` restriction gives up exactly the strength gap that
paper establishes.  This is to be stated in the report as the price of the prior,
not buried.

---

## 4. The census — what will be produced, and the reproduction gate

`results/s52_census.md`, per cell: `λ`, `δ`, `ℓ(λ)`, `a`, `h_pad`, `N_S`,
`n_χ`, eligibility, and the `h_pad ≥ 1` informative flag.

`a` by **two independent routes** asserted equal at every cell (Frobenius
plethysm `wk8_s30_pleth.amb`, and the Weyl-alternation route
`wk9_s42_census.a_weyl`); `h_pad` by two independent routes asserted equal
(`wk9_s42_hpad.h_pad`, `wk9_s42_census.h_pad_weyl`), with the third fresh-DP
route `wk9_s47_hpadcheck.h_pad_route3` run on a sample.

**Reproduction gate (this is the validation, and it is scored):**

| | prediction | prior |
|---|---|---|
| **P2** | `δ = 7`: my independent enumeration returns **258** obstruction-eligible `ℓ = 6` cells and **64** of them with `a = 1` | 0.80 |
| **P3** | `δ = 8`: **591** eligible, **45** with `a = 1` | 0.80 |

The priors are below 0.95 not because the plethysm is in doubt but because
"eligible" and "`a = 1` among eligible vs. among all `ℓ = 6`" are definitional
choices that the integrator's count may have made differently.  **A disagreement
is a finding and is reported as one, with both definitions evaluated**, exactly
as session 43 handled its work-list re-derivation.

| | prediction | prior |
|---|---|---|
| **P4** | the `δ = 9` census (`λ ⊢ 36`, `ℓ = 6`) completes inside the container within a 30-minute bound, using `\|ν\| = \|λ\| − δ` pruning before the alternation | 0.85 |
| **P5** | `δ = 10` (`λ ⊢ 40`, `ℓ = 6`) also completes | 0.55 |
| **P6** | the `a = 1` count is a **decreasing** fraction of eligible cells as `δ` grows (64/258 = 25% at `δ = 7`, 45/591 = 7.6% at `δ = 8`, so **< 5%** at `δ = 9`) | 0.70 |
| **P7** | **at least half** of the `a = 1` eligible cells at each of `δ = 7, 8, 9` have `h_pad = 0` and are therefore non-informative by Lemma A | 0.45 |

P7 is logged deliberately at a prior below one half: I do not know which way it
goes, and the point of logging it is that the informative-cell count is the
number that matters and it must not be reported as a surprise afterwards.

---

## 5. The measurements

At every `a = 1` eligible cell with `h_pad ≥ 1` that fits the container, decide
`i_det ∈ {0,1}` and `i_pad ∈ {0,1}`.

Protocol, unchanged from the six-row record so the rows are comparable:

* determinant points are true `det_4` pencils `det_4(Σ s_i A_i)`;
* pad points are the true padded-permanent restriction `l(s)·per_3(A(s))`,
  **never** `l·(random cubic)`;
* both house primes;
* `a` re-derived by kernel dimension inside the cell process and asserted equal
  to the census value;
* every exhibited kernel vector multiplied against the uncompressed
  raising-operator rows and asserted to vanish.

**Cheap direction first**, as the brief directs: at `a = 1`, `mult_det = 1`
(i.e. `i_det = 0`) is certified by injectivity of `[M ; Ev_det]`, and a mod-`p`
rank equal to `n_χ` proves injectivity over `ℚ`.  That is a one-sided
certificate and it is the only direction taken cheaply; `i_det = 1` is never
concluded from a mod-`p` computation.

| | prediction | prior |
|---|---|---|
| **P8** | `i_det = 0` at every `a = 1` cell measured this session | 0.93 |
| **P9** | no cell reports `D > 0` | 0.94 |
| **P10** | every measured cell reproduces `a` by kernel dimension | 0.97 |

P8's prior is 0.93 and not higher only because the census reaches `δ = 9`, one
degree above most of the record.  **The `a = 1` restriction is not a reason to
expect a firing cell** — as the brief says, it is a reason for a firing cell to
be worth more if one appears.  Stated plainly so the report cannot drift: the
prior on a separation at these cells is *lower*, not higher, than at a generic
cell, because `D > 0` here requires an occurrence obstruction, the strictly
weaker notion.

**Re-measurement gate.**  Three cells already banked in `results/s36_aone.md`
(`ℓ = 6`, `δ = 7`) will be re-measured from scratch before any new cell, and
every field asserted identical.  Which three is fixed now: the smallest, the
largest and the median by `n_χ` of that file's six `δ = 7` rows.

---

## 6. The two house pre-checks

**`docs/brief_wording.md` §5, the degeneracy-direction pre-check.**  This
session develops no new statistic.  `D = i_det − i_pad` is the programme's
existing multiplicity statistic; `a = 1` is a *selection of cells*, not a new
invariant.  The check is nonetheless run and recorded, in the form it has here:
each exhibited highest-weight vector is evaluated at (1) a `det_4` pencil, (2) a
reducible point `ℓ·c` with `c` generic, and (3) the true `ℓ·per_3` — the last
being the pad points of §5, which are the ten-variable object restricted to the
`r = 6` model, and the report will say so rather than claim the unrestricted
check. A vector at least as degenerate at (3) as at (1) is what `D > 0` *means*
here, so unlike the two refuted external statistics the direction is the point
of the measurement, not an accident of it.

**`docs/brief_wording.md` §7, the functoriality pre-check.**  `P_6 ⊆ D_6^{det_4}`
would give `I(D) ⊆ I(P)` and `mult_pad ≤ mult_det` for every `λ`, so `D > 0`
refutes containment.  The statistic is functorial in the right direction under
closed immersion by construction.  This is the first row of the §7 table and it
is the reason the census is worth running at all.

---

## 7. Stopping rules

1. **Any cell reporting `D > 0` halts the sweep**; the verification protocol
   takes over.  Verification here is: (i) re-measure at fresh points and both
   primes; (ii) exhibit the highest-weight vector and check it against the
   uncompressed raising-operator rows; (iii) exact arithmetic over `ℤ`;
   (iv) the (★) monomial-level check; (v) the independent second route.  A
   `D > 0` claim is written down only after all five.
2. If T0b resolves to "the mechanism transfers", the census does not proceed
   beyond the reproduction gate; the session's deliverable is the argument.
3. A cell that exceeds a 20-minute bound or the memory budget is banked as
   `DEFER` with its measured peak, never as a verdict.
4. Every run bounded by `timeout` and `ulimit -v`, process id written to
   `results/logs/<run>.pid`, runs ended only by that recorded id.
5. Per-cell banking: each cell's row is written and committed before the next
   cell starts.

---

## 8. Sync baseline

Session 52 clone baseline: **`eb8cecb37b0ee30d5be76ccbd816ee142618882c`** on
`main` (from `Projects\gct\work\.git`; no bundle in `Projects\gct` contains this
commit — the three newest bundles are `s47-exactness` `4b8047d`,
`s48-theorems` `ec2d3c9` and `s46-balanced` `bb47bbf`, all ancestors of it).
Delivery is a bundle of `s52-aone` off that baseline.  No push.
