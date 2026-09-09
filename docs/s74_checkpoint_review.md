# Session 74's checkpoint, reviewed

**What arrived.** `s74_births_checkpoint.bundle`, md5 `abff5f92…d4a6` matching
both delivered digests, 5.7 MB, 21 commits on `afb8c33`.  A **complete
274-dimensional source** at the LMR goal cell — every rung of the ladder filled,
`2, 37, 54, 52, 43, 31, 22, 14, 9, 5, 3, 1, 1` — with determinant, padded and
generic evaluation columns at both house primes.  This is the object the
programme has been trying to build since batch 9, and it exists.

Everything below was re-derived here from the delivered **raw** material — the
native row values, the integer points, and the source fillings — by
`analysis/wk12_int_s74_verify.py`, `analysis/wk12_int_transport_check.py` and
`analysis/wk12_int_s74_freshpad.py`, which are mine.  s74's decision files were
read only afterwards, to compare.  **47 of 47 checks pass.**

## 1. What I actually recomputed

The delivered `rows_native` holds the values of the **native** fillings; the
transported row is `row_i(f) = F_{T_i}(f) · msym_u(f)^{24−d_i}` with
`msym_u = 4! [s₁⁴] f`.  My first pass took the stored values as the rows and got
rank 274 on the determinant side — which contradicts LMR, and was my error, not
s74's: I had not applied the scaling.  With the transport applied by my own code:

| | mine, P1 | mine, P2 | s74 |
|---|---|---|---|
| `rank T_det` on 274 rows | **273** | **273** | 273 |
| `rank T_det` on the 273 transported δ=23 rows | **273** | **273** | 273 |
| `rank T_pad` on 274 rows | **269** | **269** | 269 |
| `rank T_pad` on the 273 transported δ=23 rows | **268** | **268** | 268 |

with an explicitly exhibited nonzero minor of the stated size at each prime,
rows and columns chosen by my elimination, not s74's.

Three structural checks that are not ranks:

- **Every literal row is its native filling with `4(24−d)` extra singleton
  letters** — structurally `u^{24−d}` times the native one — on all 274 rows.
- **`msym_u = 4! [s₁⁴] f` recomputed exactly over `Z`** from each point's own
  integer pencil (`4!·det A₁`) or linear forms (`4!·ℓ₁·per B₁`) agrees with
  s74's stored `u_symbol` at **all 282 points on both sides at both primes**,
  and is **nonzero at every one of them**.  This matters: the transport is
  column scaling by `msym_u^{24−d}`, so a single `u`-zero point silently voids
  every transported row in that column.  There are none.
- **My own expansion of `ℓ·per₃(B)`** into `exps(4,9)` coordinates reproduces
  s74's `points_cv` for padded point 0 entry for entry, so my reading of the
  point format is confirmed independently of the `u_symbol` agreement.

## 2. The determinant column is closed, and it is closed by a proof

`rank T_det` on the transported δ=23 rows is 273 = `dim uM₂₃`, certified by a
nonzero 273×273 minor at both primes.  So `T_det` is **injective on `uM₂₃`**.
By the birth-quotient proposition (`docs/s1_batch12_review.md` §2:
`ker T_det ∩ uM₂₃ = u·(I(Det) ∩ M₂₃)`, valid because `I(Det)` is prime and
`u ∉ I(Det)`),

    i_det(23) = 0        exactly, not as a sampled ceiling.

`b₂₄ = 1`, so `i_det(24) = i_det(23) + ε_det = ε_det ∈ {0,1}`; LMR gives
`i_det(24) ≥ 1`; therefore

    i_det(24) = 1,   rank T_det(24) = 273,   exactly.

Independently: s74's determinant kernel vector has coefficient **1** on the
δ=24 native row, so it is not in `uM₂₃` and `ε_det = 1` directly.  The two
routes agree.

**This is the first exact statement about either column at the goal cell**, and
it needed no `δ = 24` candidate: the transported δ=23 source settles it.  That
is precisely the shortcut written down in the S1 review, now realised.

And because `dim ker(sampled T_det) = 1` while `I(Det) ∩ M₂₄` also has dimension
1, the two coincide: s74's kernel vector **is** the LMR equation `y`, exactly,
not merely a vector containing it.  `y` is nonzero at 282/282 padded points at
both primes, so `y ∈ I(Det) \ I(pad)` — the LMR separation reproduced inside
this model as a statement about one identified equation.  s74's argument for
this (`y(f) ≡ c_p·(k_p·row(f)) mod p`, no rational reconstruction needed)
is sound and I checked the residues.

## 3. The padded column, and what the numbers are allowed to mean

`rank T_pad(24) ≥ 269` is certified.  Everything past that is a ceiling read off
one point family, and the report's `D = −4, no multiplicity obstruction` does
not follow from it.  Five sampled kernel vectors are five candidate relations,
not five proved padded equations.  s74 has already accepted this correction and
banked the floor instead; I confirm it independently.  The justified statement is

    rank T_det = 273 exactly,    269 ≤ rank T_pad ≤ 274,    −4 ≤ D ≤ +1.

The same reading applies to the whole `i_pad` ladder `0, 3, 5, 5, …, 5`: those
are ceilings.  `i_pad(13) ≤ 3` and `i_pad(14…24) ≤ 5`.

## 4. What the delivered data prove that nobody has stated

**All five padded kernel vectors have coefficient 0 on the δ=24 native row**, at
both primes.  So `ker(sampled T_pad) ⊆ uM₂₃`.  Since `I(pad) ∩ M₂₄` is contained
in the sampled kernel, `I(pad) ∩ M₂₄ ⊆ uM₂₃`, and the proposition then gives

    I(pad) ∩ M₂₄ = u·(I(pad) ∩ M₂₃),   so   ε_pad = 0   and   i_pad(24) = i_pad(23).

That is a **proof**, not a sample: it uses only the containment
`I(pad) ∩ M₂₄ ⊆ ker(sampled)`, which holds for any point set, together with the
computed fact that the sampled kernel misses the birth direction.  Combining it
with §2:

    D = i_det(24) − i_pad(24) = 1 − i_pad(23).

**The LMR decision is now identically the question of whether the padded ideal
is zero at rung 23.**  The δ=24 birth line is settled on both sides — it carries
the determinant ideal and it does not carry the padded one — and nothing at
rung 24 remains to be built or measured.

Two consequences worth carrying forward:

- `i_pad` is nondecreasing along the ladder (`u·(I ∩ M_{d−1}) ⊆ I ∩ M_d` and `u`
  is a nonzerodivisor).  So **one certified padded ideal element at any rung
  `d ≤ 23` gives `i_pad(23) ≥ 1` and `D ≤ 0`**, settling the cell against a
  multiplicity obstruction.  The cheapest place to look is the cheapest rung.
- `D = +1` needs `i_pad(23) = 0`, that is a nonzero **273×273** padded minor on
  the transported δ=23 rows.  It stands at 268.  Five short.

The cost asymmetry the programme banked in batch 12 is now in force at the goal
cell in its sharpest form: **`D = +1` is the only value that evaluation alone
can prove.**  Every other value needs `i_pad ≥ 1`, which is a membership
statement about an ideal and cannot be read off any number of points.

## 5. Three routes, in cost order

**(a) Rung 13, on fresh points — 39 rows, no transport, running here.**
`i_pad(13) ≤ 3` on a 39-dimensional source is the cheapest number in the
programme.  A rung-13 source vector is evaluated at the same degree-4 padded
points as everything else, so no transport enters.  If the rank reaches 39 the
ladder's `3` was an artefact of the point family and the padded column has to be
redone from rung 13 up; if it stalls at 36 over an independent stream, the
rung-13 relation is probably real, and one certified rung-13 padded ideal
element settles the cell.  `analysis/wk12_int_pad13.py`, 150 fresh points at
bound 11 from my own stream, both primes.

**(b) The reducible screen, which has never been run against a complete
source.** `docs/batch11_plan.md` C3 pre-registered it: `mult_pad ≤ mult_red =
rank S`, so `rank S < 274` gives `i_pad ≥ 1` and `D ≤ 0` **with no padded points
at all**.  `rank S` is the rank of the 274×521 reducible-normalisation split —
an exact rank of a structural matrix, not a sampled evaluation.  Until this
bundle there was no source to apply it to.  There is now.  This is the cheapest
possible settlement of the cell and it should be run first.

**(c) The exact route, S4's factorization.**  `M_λ →^S ⊕_μ M^{(3)}_μ →^Q ⊕_μ N_μ`
gives `rank T_pad = rank S − dim(S(M_λ) ∩ ker Q)`.  That computes `i_pad`
**exactly**, from finite linear algebra over `Q`, with no points and no
membership argument left over.  It is the only route that can prove `D ≤ 0`, and
it subsumes (b).  S4 delivered the factorization and a 12-minor that s74
reproduced 144/144; what it has never had is a source to feed it.

**(d) More padded points at rung 24**, which can only ever prove `D = +1`.  Worth
running in the background — `analysis/wk12_int_s74_freshpad.py` tests the five
kernel directions against a fresh stream at bound 17 — but it is not a route to
a decision unless it reaches 274.

## 6. Smaller things

- `skipped_points: [243, 263]` in both padded columns, yet columns 243 and 263
  are fully populated and have nonzero `u_symbol`.  The field currently reads as
  if two delivered columns are invalid when they are not.  Ranks are unaffected
  either way — I computed mine including both and got s74's numbers — but the
  field should say what it records.
- The generic column was banked before the source was complete and does not
  cover all 274 rows, so it cannot yet certify that the 274 source vectors are
  independent.  The determinant minor does that (rank 273 needs 273 independent
  rows) and the padded minor adds a 274th independent row, so independence is
  not in doubt; the generic column should still be finished for the record.
- `secs = 2688` on the determinant column against a stated budget.  Recorded
  openly by s74, and it bears on scheduling, not on the certificates.

## 7. Status

| claim | status |
|---|---|
| a complete 274-row source at the goal cell | **DELIVERED**, structure verified here |
| `rank T_det(24) = 273`, `i_det(24) = 1` | **PROVED** (transported 273-minor + the proposition + LMR) |
| `i_det(23) = 0` | **PROVED** |
| `y = ` the LMR equation, `y ∉ I(pad)` | **PROVED** on the delivered residues |
| `rank T_pad(24) ≥ 269` | **CERTIFIED** (nonzero 269-minor, both primes) |
| `i_pad(24) = i_pad(23)`, `ε_pad = 0` | **PROVED** (the sampled kernel misses the birth line) |
| `D = 1 − i_pad(23)`, so `−4 ≤ D ≤ +1` | **PROVED**; `D` remains **OPEN** |
| `D = −4`, "no multiplicity obstruction" | **NOT ESTABLISHED**; withdrawn by s74, confirmed withdrawn here |

Author: Swami Sethuraman, swsethuraman@beneficus.ai, Beneficus AI.
board_numbering: batch12
