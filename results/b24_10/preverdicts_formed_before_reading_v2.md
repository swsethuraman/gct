# B24-10 — verdicts formed before reading the deliverables (v2)

**This file supersedes `preverdicts_formed_before_reading.md`.** That stub is 561 bytes, sha256
`683d3880beca32330d79a482845792133f426f71099a28d3e07b3db27ae9dd3d`, truncated mid-sentence inside
its own state-check block, and carries **zero pre-formed verdicts**. It is the fragment of attempt
one. Per the relaunch addendum, Amendment 1, it is not edited, not deleted and not renamed; it is
bound in the manifest as a dead artifact. This is **attempt two**.

Written once, appended block by block as each verdict was formed, and never revised. Where the
report departs from this file, the report says so and points here. Method rule inherited verbatim
from B20-10 §0 / B21-10 §0 / B22-10 / B23-10 §0.

Author: Claude, **Opus 5 (1M context)**, exact model ID `claude-opus-5[1m]`, default permission
mode. Worktree `work/batch15_workers/B15-10`, branch `b15-10-portable-witness`.

```
git rev-parse HEAD          239dd6e84417ab04914a8d84cca02ddf754bf1fb
git rev-parse HEAD^{tree}   3008235a92bf10a108ae673564d879a5716b4a1d
git status --porcelain      results/b24_10/ (this slot, untracked)
                            results/logs/b15_10_runtime_native_20260913.pid          (pre-existing)
                            results/logs/b15_10_runtime_native_20260913_resources.json (pre-existing)
                            0 tracked changes
```

**What had been opened when the blocks below were written.** Only: (i) the PART 15 brief and its
relaunch addendum; (ii) `git cat-file` / `git ls-tree` metadata — commit subjects, byte counts,
sha256 of the pinned deliverables, and the B24-01 file list; (iii) `docs/b23_10_review.md` §0 and
its "Plain terms" list at `239dd6e8`, which is my own prior report and the source of the method
rules. **No B24 packet report, no paper file, no ledger, no manifest and not the Batch 25 board
had been opened.** The statements ruled on below are the statements as the brief prints them.

Q1 covers priority 1; Q2 priority 2; Q3 priority 3; Q4 priority 4; Q5 priority 5; Q6 priorities 7
and 8; Q7 priority 9. Each block is timestamped at the moment it was appended.

---

## Q1 — B24-04: the tail theorem, the sizing, the extrapolation, the basis
*appended 2026-09-20T16:15Z, before `docs/b24_04_report.md` was opened*

**Statement as the brief prints it:** if the tail `t` is less than the degree `d`, every weight
vector factors as `c_{n e1}^{d-t} * g` with `deg g = t`; since `I(D_r^{det_n})` is prime and `P_r`
irreducible, the separating property passes through; therefore every separating cell has tail
`>= D*`.

### Q1.1 The theorem — pre-formed: PROVED in shape

I reconstruct the descent independently, from the statement only:

- Let `f` be separating: `f` vanishes on `D_r^{det_n}`, and `f` does not vanish at the padding
  point. Suppose `tail(f) = t < d = deg f`, so `f = c^{d-t} * g` with `c = c_{n e1}`.
- `f` in `I` and `I` prime give `c` in `I` **or** `g` in `I`. That is the correct use of primality.
- A product is non-zero at a point only if **both** factors are non-zero there. So `c` and `g` are
  each non-zero at the padding point.
- Hence whichever of `c`, `g` lies in `I` is **itself separating**, and of strictly smaller degree.
  Descent.
- A separating form has degree at least the onset, by the definition of the onset. `deg g = t`.
  Therefore `t >= D*`.

The shape is right and I expect to confirm it. **Two places I predict the proof will be thin, named
in advance:**

- **(W1) the base case.** The descent terminates only if `c_{n e1}` is itself **not** separating.
  I predict this is asserted rather than proved. It is load-bearing, not decorative: were `c`
  separating, the theorem would be false.
- **(W2) the grading.** The factorisation is forced only if "tail" is measured in the same grading
  in which `c_{n e1}` is the extremal weight vector. If "tail" merely **bounds** the multiplicity
  of `c` rather than pinning it at `d-t`, then the exponent is wrong and `deg g = t` fails.

A third, weaker observation, recorded so that I notice if it matters: "`I` prime **and** `P_r`
irreducible" is very likely **redundant** — if `I = (P_r)` these are the same hypothesis. A
redundant hypothesis is not an error. I record it so that, if the proof turns out to use
irreducibility for something else, I see that rather than assume it.

**Predicted ruling: PROVED, or PROVED-with-correction if W1 is unproved. REJECTED only on a
counterexample.**

### Q1.2 The sizing `N_S ~ 0.060 * t^4` — pre-formed: MEASURED at best, constant over-precise

Two significant figures in `0.060` claims a 2% determination. A fit over a short range of `t` will
not support that. What decides the ruling is whether `t^4` is **derived** — a dimension count of
degree-`t` objects in four effective parameters, with only the constant fitted — or whether
exponent and constant are **both** fitted. If both, the label is MEASURED, the exponent carries its
own error bar, and I predict that error bar is not printed.

### Q1.3 The `~4e10` at tail 900 — pre-formed: the label EXTRAPOLATION is RIGHT, the range is not

First, an arithmetic point I can settle before reading, and which the brief does not make: the
figure is **not independent of Q1.2**.

```
0.060 * 900^4 = 0.060 * 6.561e11 = 3.94e10 ~ 4e10
```

It **is** the fitted law evaluated at 900, and nothing else. Its warrant is therefore exactly the
warrant of the fit, carried out to `t = 900`.

- If the fit was taken at small tails — which is what a slot named "small tail" would have measured
  — then `t = 900` is an extrapolation by a factor of order 15-30 in `t`, hence **five to six
  orders of magnitude in `N_S`** beyond the last measured point.
- So the label is correct but **insufficient by itself**. An extrapolation label discloses the
  *kind* of claim; it does not disclose the *distance*. **I will require the fitted range to be
  printed beside the figure**, and absent that I will rule the record's use of `4e10` as a price
  unsupported.
- **The asymmetry the brief names is real, and I endorse it in advance.** Striking `1e150` was
  right if `1e150` had no warrant. Installing `4e10` in its place is a second unwarranted number
  unless the range is printed — and it is the **more dangerous** of the two, because `4e10` is
  small enough to *invite* an attempt and `1e150` was not. A number that invites work must be
  better supported than a number that forbids it, not equally supported.

**Predicted ruling: label right; range unstated; `4e10` admissible as an order-of-magnitude
indication, not as a price.**

### Q1.4 The 70-pattern basis is a seeded greedy selection — pre-formed: CONFIRM, with a refinement

Greedy selection against a rank oracle, run to completion, yields a genuine basis, so neither the
existence nor the size is in doubt. But **the count is canonical and the set is not**: 70 is a
rank, and a rank does not depend on the seed; the 70 particular patterns are one arbitrary choice
among many bases.

Therefore the Missing Theorem is bespoke **exactly to the extent that it quantifies over the set
rather than the count**. If its statement can be rewritten to refer only to the rank, or to a
seed-independent property of the span, it is not bespoke at all. I expect to rule B24-04 Q3's
finding correct and to add this refinement, which sharpens it in the direction of repair rather
than of damage.
