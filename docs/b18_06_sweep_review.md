# B18-06 sweep review — the degree-five family, retired

Report: `work/batch15_workers/B15-06/docs/b18_06_sweep.md`. Started from `8f7ab3bb`,
tree `f0428d81`.

## Verdict

**ACCEPT.** Nineteen cells, nineteen closed, and with the four already settled the
degree-five five-row family is complete. This closes the last live thread in batch 18.

**One correction to my own wording, caught on review of this review.** I first wrote
that all 23 cells close at `D = 0` exactly. That is true of 22. The rectangle `(4^5)`
is excluded by *padding vanishing* — B18-01 Prop 8.4 gives `i_pad = 1 = a`, hence
`m_pad = 0` and `D <= 0` — and says nothing about `m_det`, which remains undetermined.
The uniform statement across the family is `D <= 0`; `D = 0` holds in 22 of 23. Every
cell is excluded as a gap candidate either way, so the conclusion is unchanged and the
index entry is not.

The delivery is stronger than what was asked for in three ways, and its recorded failure
is the most valuable single item in the batch.

## 1. Verified independently

- **The set identity.** I recomputed the degree-five census from the plethysm and
  compared: the 19 swept plus the 4 settled are **exactly** my 23. No overlap, nothing
  missing, nothing extra. The slot's own set comparison is confirmed.
- **`a = 1` in all 23.** The slot recomputed `a` in-script by the Weyl alternant rather
  than trusting the census — discharging, on its own initiative, the dependency I had
  discharged for it after P1. Independent agreement.
- **`d = 6` has 105 five-row cells.** Confirmed; 38 of them have `a = 1`.
- **`s = 8` for `(12,2,2,2,2)`.** The slot's Kronecker routine matches the value I
  computed earlier from `S_20` characters.

## 2. `D = 0` exactly, which is more than the ladder required

The determinant evaluation alone gives `m_det = 1`, hence `i_det = 0`, hence `D <= 0`.
The slot ran the padding evaluation too and got `m_pad = 1`, so `i_pad = 0` and
**`D = 0` exactly** in all nineteen. Both legs are sampled *nonzeros*, the one direction
that certifies. Building `h_lambda` once and evaluating at both points cost nothing
extra and turned nineteen inequalities into nineteen equalities.

## 3. The method change was correct, and the inference chain is clean

P1's compressed elimination needs `O(K^2)` storage and would not have reached
`K = 11640`. The replacement — Casimir projector over `F_p`, lifted by CRT and rational
reconstruction, then **verified exactly over `Z`** by checking that all four simple
raising operators annihilate the integer vector — uses the modular step as a *search*
and the integer step as the *proof*. The slot states it plainly: "no modular inference
in the chain."

That is the correct use of `rank_p <= rank_Q`. A modular result never carries a
characteristic-zero conclusion here; it only proposes a vector that exact arithmetic then
confirms. Largest cell 14.0 s and 80 MiB, against elimination's 426 MiB at `K = 2825`.

## 4. The recorded failure, and why it is the batch's best item

> "My first prototype indexed each raising operator's targets in the same weight space. A
> raising operator changes the weight, so the operators came out empty and the
> verification passed vacuously."

A check that passes because it is testing nothing is the most dangerous object in this
programme, and far more dangerous than a check that fails. Every cell would have
"verified" and every closure would have been unfounded.

What makes this exemplary is not that it was caught — it is the fix. **Each certificate
now records the shifted-weight target dimensions, 354 to 11,640, so a vacuous pass is
visible in the artifact.** That does not repair one bug; it instruments against the whole
class, in a form a later reader can check without rerunning anything. That belongs in
the delivery contract.

Six controls declared, six passed, three of them rejections that had to be able to fail.
The corrupted vector and the rank-deficient point were rejected. The wrong raising
convention was rejected **at the lift stage rather than by the residue check** — a
control that passed for the wrong reason, disclosed rather than smoothed over. And the
non-self-referential one is a real external identity: `h_lambda` for `(12,2,2,2,2)`
reproduces `det Hess_5(f)(e_1)` at three points with ratio exactly 6.

The elimination path lost rank again on the first sketch (nullity 56 and 197) and the
**pre-declared** retry recovered it. Second time that discipline has paid in this slot.

## 5. The scope statement is exactly right

> "This retires one degree, not the five-row regime… The tally is 34 of 34 cells closed
> at the first point — **a prior, not a theorem**."

And it declines to request a `d = 6` sweep, with a reason rather than a preference: the
binding constraint is that no determinant equation of length 5–8 is known in any degree.
Closing 105 more cells would not move that constraint. Agreed, and I would not fund it.

One small bookkeeping note: the report says `d = 6` has "3 settled". I count four — the
three P1 cells `(15,3,2,2,2)`, `(11,9,2,1,1)`, `(14,4,2,2,2)`, plus `(16,2,2,2,2)` from
the `(4d−8, 2^4)` covariant family. Worth reconciling in the ledger, not a defect.

## 6. What enters the index

| id | statement | status |
|---|---|---|
| `degree_five_family_retired` | All 23 five-row cells at `d = 5` are excluded as gap candidates. **22 of them have `D = 0` exactly** — 19 by direct evaluation in the sweep, 3 previously — with `a = 1`, `m_det = 1` and `m_pad = 1`, so `i_det = i_pad = 0`. The 23rd, the rectangle `(4^5)`, has only `D <= 0`: it is excluded by padding vanishing (`i_pad = 1 = a`, so `m_pad = 0`), and **its determinant multiplicity `m_det` is undetermined**. The uniform statement across all 23 is `D <= 0`. The set identity 19 + 4 = 23 is confirmed independently | PROVED; census and set identity recomputed here |
| `exact_hwv_by_projector_and_lift` | A Casimir projector over `F_p`, lifted by CRT and rational reconstruction and then verified over `Z` by exact annihilation under all four simple raising operators, reaches `K = 11640` in 14.0 s and 80 MiB where compressed elimination needs `O(K^2)`. The modular step searches; the integer step proves | PROVED / MEASURED |
| `a_vacuous_pass_is_invisible` | A raising-operator check indexed in the source weight space instead of the shifted target space is **empty**, and passes vacuously in every cell. The remedy is not the fix but the instrument: record the shifted-weight target dimension in every certificate, so a vacuous pass is visible without rerunning | RECORDED defect and standing rule |
| `thirty_four_of_thirty_four` | 34 of 34 five-row cells tried across `d = 5, 6` closed at the first determinant point. **A prior, not a theorem.** It says nothing about an untested cell and excludes no length | RECORDED |

## 7. Carry-forward

1. `a_vacuous_pass_is_invisible` goes into `docs/delivery_contract.md`. Any check whose
   subject can be empty ships the size of what it checked.
2. The `d = 6` count of settled cells: three or four. Reconcile in the ledger.
3. No `d = 6` sweep. The binding constraint is upstream of it.
