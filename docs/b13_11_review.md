# B13-11 review — reconciled research ledger and control semantics

board_numbering: batch13
session_id: B13-11
model recorded by the session: `gpt-6-astra`, reasoning effort `xhigh`
bundle: `b13_11_research_ledger.bundle` (one part, `part00` byte-identical)
base: `00495110c62acfbbbc951e82cc218ed091563b3f`
head: `39d22e3d8847d0d74619b125d09bc919a57c1feb` (`b13-11`)
status claimed: bounded ledger/control assignment completed
integrator verdict: **accept — it closes a frontier I named and proves a control
I had demoted to an assumption. It is also the only session in the batch to edit
shared code, so read §7 before merging.**

---

## 1. Zero-cost checks

| check | result |
|---|---|
| md5 / sha256 | `d3019c48…` / `9804f4e1…` — both match, whole and `part00` |
| `part00` vs whole | **byte-identical**; 1,232,220 B, matching the manifest |
| declared base | `0049511` — equals `origin/main` and my tip |
| `git bundle verify` | "is okay" |
| applies | clean; 50 files, 29,467 insertions, **51 deletions** — the only deletions in the batch |
| single-writer files | **none touched** |
| 5 MB rule | none close |
| `Claude-Session:` / `Co-Authored-By` | **neither** — the Astra pattern; model recorded in front matter and both manifests |
| pre-registration | committed with its dated addendum before the computations they govern |
| **shared code edited** | **three files** — see §7 |

All arithmetic reproduces: `10 + 47 = 57`; `26 + 2 = 28` and `47 − 28 = 19`;
`326 + 1195 = 1521`; `1521 + LMR = 1522`; `9952 − 74 = 9878`; `95 + 11 = 106`;
`1200 + 29 + 837 = 2066`.

Two cross-session confirmations fall out of those numbers. The 57 shapes with
10 zero blocks **independently match B13-05's count** of the partitions of 13
into at most five parts and its `a_inf = 0` bucket. And the s79 manifest split —
1,200 shipped and matching, 29 differing, 837 absent — is **exactly B13-07's
audit**, from a different session on the same evidence.

---

## 2. It closes a frontier I named

The headline: **the complete weight-13 census of tails with at most five parts
has 57 shapes; 28 of the 47 positive blocks are closed by the reconciled quartic
record plus the sixteen replayed stable blocks; the remaining 19 all have at most
three tail parts, hence quartic length ≤ 4, where `docs/n4_gate.md` §1's
containment theorem excludes a positive padded gap. So zero blocks in this
census remain open for `D > 0`.**

The scope is stated correctly and I want it on the record: this asserts neither
full determinant rank on the nineteen, nor anything at larger tail weights or
lengths, nor anything about the LMR cell.

But it is not a small thing. The docstring of `analysis/wk12_int_w13_census.py`
— which I wrote — said *"the first open frontier `a_inf = 4` is exactly FIVE
blocks. That is the size of the next stable determinant-equation test, and
neither board had the number."* **Those five are now closed**, and the file's new
docstring says so: *"The five `a_inf = 4` blocks are all closed; they are no
longer a frontier."*

The containment argument is the right kind: generic four-variable cubics have a
3×3 determinantal representation, so `ℓ·c = det diag(ℓ, M)` puts the reducible
locus — and hence the padded locus — inside the determinant closure. **A
containment exclusion, not an empty-determinant-ideal assertion**, and the report
draws that distinction itself.

---

## 3. My `n = 3` padded control is now proved

This is the item I most wanted from this session. I had demoted the `n = 3`
padded control to a documented assumption: `ℓ·per₂` uses at most five essential
variables, so a seven-row weight has zero padded multiplicity — **asserted, not
proved**, and my s87 session had rested on it unchecked.

B13-11 proves it, and I verified the argument by hand:

    per₂([[a,b],[c,d]]) = ad + bc,   ℓ = z   ⟹   z(ad + bc)

    ∂/∂a = zd,  ∂/∂b = zc,  ∂/∂c = zb,  ∂/∂d = za,  ∂/∂z = ad + bc

The five first derivatives have **nonempty, pairwise disjoint monomial
supports**, so the form has *exactly* five essential variables — not at most
five. Every pullback therefore lies in the closed subspace variety `Sub_5`,
whose coordinate ring carries no Schur constituent of length greater than five.
At the seven-row weight `(19,7,2⁵)`: `mult_pad = 0`, `i_pad = a = 6`, padded gap
**−5**.

The consequence the session draws is the one that matters: **the unpadded
positive example supplies no padded test at this weight.** Its `+1` gap is
`mult_per₃ − mult_det = 6 − 5`, an unpadded statement; the padded gap at the
same weight is −5. Those are different objects and the record should not blur
them.

---

## 4. A reversed inequality in a banked artefact — verified

`results/s63_n3control.json` carries:

> `rank_p <= rank_Q so mult_det <= 5 over Q at both primes; rank G = 5 gives
> mult_det >= 5; hence mult_det = 5 exactly, i_det = 1.`

**`rank_p ≤ rank_Q` gives `mult_det ≥ 5`, not `≤ 5`.** A modular rank is a floor
on the rational rank. The note derives both bounds from the same inequality used
in opposite directions, and the upper bound has to come from elsewhere — from
LMR, as `docs/s63_report.md` §3 correctly explains.

The *conclusion* is right and the report says so; the *derivation banked beside
it* is not, and anyone quoting that note as the upper-bound argument would be
reasoning backwards. **This is the batch's discipline point — a sampled rank is a
floor on the rank and a ceiling on `i` — appearing as a reversed inequality in an
artefact rather than in prose.** It should be corrected in place, not merely
noted.

---

## 5. A silent join failure in my own code

*"The old census stripped zero padding from record tails while its census
dictionary retained five-part padding; this lost shorter-tail joins."*

That is `record_closed_tails()` in `wk12_int_w13_census.py` — mine. The join
compared padded keys against unpadded ones and silently matched nothing for the
shorter tails, so the cross-reference **understated what was closed** without
failing. I had noticed the *symptom* and papered it with a warning
(*"this cross-reference UNDERSTATES what is closed… Extending the ledger list is
a batch-13 task"*); B13-11 found the *cause* and fixed it, and correctly removed
my warning because it did the task the warning deferred.

**A join that silently drops rows is the same class as a check that cannot
fail** — the sixth appearance of that class in this batch, and the first in code
I wrote rather than in a check I ran.

---

## 6. The `negative_record()` redesign is the right shape

The change I most approve of, because it makes the dangerous default impossible
rather than documenting it:

- `negative_record()` keeps its historical tuple contract and now returns the
  reconciled full-rank quartic view — **only full-rank exclusions**;
- the original 326-cell snapshot is preserved as `legacy_negative_record()`;
- the complete record, including LMR and the `n = 3` controls, lives in
  `b13_11_ledger.load_record()`.

The docstring states the reason: *"Old callers treat every key as an exclusion.
Deficient records, including LMR, and cubic controls therefore live in
`load_record()`."* **So an existing caller cannot accidentally treat LMR as a
negative result** — and nothing was deleted to achieve it. That is how to change
a shared API.

Likewise `open_on_both_instruments` (absent from the two rank records) is
separated from `open_on_all_instruments` (which additionally applies the
inherited containment rule). Rank-record openness and gap openness are now
different fields, which is exactly the confusion that produced the nineteen
"open candidates" that are not open.

The verification is real: **all sixteen stable blocks pass 192/192 independent
checks** on my own `wk12_int_s79_stable_verify.py` — exact weight-space
enumeration, exact ambient multiplicity, every kernel vector on independent
raising operators, principal-minor evaluation, agreement up to the declared
global sign, full rank at both primes, tracelessness of every point, *"no term
silently discarded."* Plus 28/28 controls and 25/25 semantic regressions.

The LMR replay reproduces det 273, padded 269, generic 274 at both primes, with
`msym_u` recomputed from the delivered points and every `u`-value checked for
zeros — and labels itself honestly: *"a replay of banked matrix arithmetic; the
native filling evaluations were not regenerated."* `D = 1 − i_pad(24) ∈ [−4,+1]`,
the −4 stays MEASURED, and the `ε_pad` lift stays unresolved. Consistent with
B13-07's counterexample.

---

## 7. Read this before merging: the only session that edits shared code

B13-11 changed three tracked files outside its namespace, with 51 deletions:

| file | change | mine? |
|---|---|---|
| `analysis/wk9_s57_lib.py` | `negative_record()` → `legacy_negative_record()`, new reconciled `negative_record()` | shared |
| `analysis/wk12_int_w13_census.py` | join fixed; source-splitting on `;`; `a_inf` swapped to `b13_11_math.a_inf_exact` | **mine** |
| `analysis/wk12_int_s79_stable_verify.py` | 8 lines, wrapper additions | **mine** |

Every change I read is correct and well-motivated. Two things to weigh anyway:

1. **The counting routine was substituted.** The census now calls
   `b13_11_math.a_inf_exact` where it called `wk9_s57_stable.a_inf` — exact
   integer counting in place of Weyl alternation at both primes plus CRT. The
   headline 57/10/47 is therefore no longer produced by the routine that
   produced it before. It agrees with the old value and with B13-05's
   independent count, so I am satisfied — but the substitution deserves a line
   in the file rather than passing silently.
2. **A correction's provenance was deleted.** My docstring recorded that the
   batch-11 review's 46 was wrong and 47 right, that the discrepancy was one
   shape in the `a_inf = 0` count, and that `(5,3,3,2)` was the tail no session
   of either batch had tested. That history now lives nowhere in the file. The
   new docstring supersedes the *claim* correctly; it should also keep the
   *correction*.

Neither is a reason to hold the merge. Both are reasons to read the diff, which
is what a session touching shared code should expect.

---

## 8. Two of its three queue rows are already stale

The reconciliation table is a snapshot, and the batch moved under it:

| queue | B13-11 says | after the rest of batch 13 |
|---|---|---|
| s79 Q1 | 123 cells, 121 closed, **2 open** | **1 open** — B13-10's pilot closed `(10,6,6,6,2,2)₈` with `i_det = 0`, leaving `(12,4,4,4,4,4)₈` |
| s79 Q2 | 10,513 / 635 / 9,878 | unchanged |
| cubic δ=10, ℓ=6 | 402 / 296 / **106** | **58 open** — B13-08 closed 48 more (344 closed) |

Not a defect — B13-11 could not see deliveries that landed after it — but the
ledger it produces is the batch's canonical record, so it must be updated with
B13-08's and B13-10's results before anyone plans against it. **That is the merge
step, and it is mine.**

---

## 9. Environment and board defects

**Fifth Astra session, fifth toolchain block.** Python 3.12.14 and NumPy 2.3.5
present; FLINT, SymPy, SciPy absent; local installation blocked by restricted
network socket access; Singular and msolve absent. The split is now **eight for
eight**: five Astra sessions blocked, three Claude-side sessions fine. It routed
around with exact object-integer counting and small independent arithmetic, and
states plainly that **no exact computation was downgraded to sampling**.

Run discipline: one worker, one BLAS thread, a 1 GiB process cap and 600 s wall
cap on every computation, PIDs and resource observations logged, nothing near a
limit (stable replay 15.1 s, controls 20.5 s, census under 0.5 s). Early adapter
errors and tracebacks retained.

**Board defects:**

1. **The board did not name the length-≤4 containment source.** Locating
   `docs/n4_gate.md` was *necessary* to avoid reporting the nineteen
   rank-record omissions as open padded candidates. Without it this session's
   headline result does not exist and its opposite gets written down instead.
   **That omission is mine and it was nearly expensive.**
2. `s57` and `s63`'s quartic files carry dimensions and prices rather than the
   additional rank measurements the board implied.
3. The prepared checkout has the frozen HEAD but no `main` ref — the same
   friction B13-06 reported. The preamble's clone check needs to tolerate it.
4. *"The batch-12 stocktake and reviews retain older overstatements; the
   controlling board and corrections govern all claims here."* Fifth session to
   say something like this about `stocktake_batch12.md`.

---

## 10. Actions

1. **Update the ledger with B13-08's and B13-10's results before it is used** —
   s79 Q1 to 1 open, the cubic degree-10 queue to 58 open. The ledger is the
   canonical record from here, so a stale row is worse than no row.
2. **Correct the note in `results/s63_n3control.json` in place.** The inequality
   is reversed; cite `docs/s63_report.md` §3 for the LMR upper bound.
3. **Promote the `n = 3` padded control from assumption to theorem** in
   `docs/det4-onset.tex` and wherever s87 depended on it. It is proved, the
   proof is three lines, and I verified it.
4. **Cite `docs/n4_gate.md` §1 in the board** wherever the length-≤4 containment
   is load-bearing.
5. **Retain the deleted provenance** in `wk12_int_w13_census.py`'s docstring —
   the batch-11 46-vs-47 correction and the `(5,3,3,2)` note — and add a line
   recording the `a_inf` routine substitution.
6. **Rewrite `docs/stocktake_batch12.md`.** Fifth session to flag it; it has
   taken corrections on the `N_S` range, the builder-first framing, the cost
   model and now its general overstatements.
7. On the deferred verification pass: re-run the 57/10/47 census through the
   *old* `wk9_s57_stable.a_inf` to confirm the substituted routine agrees, and
   replay two of the sixteen stable blocks independently.
