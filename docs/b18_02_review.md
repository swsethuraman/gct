# B18-02 review — the symmetry carrier

Integrator review. Report: `work/batch15_workers/B15-02/docs/b18_02_report.md`.
Started from commit `6f85b37b`, tree `b1531cf7`. Code `analysis/b18_02_carrier.py`,
certificates under `results/b18_02/`.

## Verdict

**ACCEPT.** The carrier is built, the cost of the real target is priced honestly and
stopped, and the slot volunteers the negative that matters most about its own control.
Its headline warning is correct — I reproduced both numbers exactly — and it needs one
condition added before Slot 06 acts on it.

## 1. What I verified independently

I recomputed the headline numbers from the characters of `S_12`, Murnaghan–Nakayama on
beta-numbers, written from the rule rather than from the slot's code.

| Claim | My result |
|---|---|
| `lambda = (6,3,1,1,1)`, `d = 3`: `g = 3`, `s = 1` | **g = 3, s = 1** — exact |
| `lambda = (5,3,2,1,1)`, `d = 3`: `g = 4`, `s = 2` | **g = 4, s = 2** — exact |
| — | skew part `g − s = 2` in both |

Controls on my own implementation: `sum_lambda g(mu,mu,lambda)·f^lambda = (f^mu)^2 =
213,444`; `g(mu,mu,(12)) = 1`; `f^(3,3,3,3) = 462`. All hold.

So the warning stands: **the transposition changes `s` by a factor of 3 and 2 in these
cells, already at `d = 3`.** Slot 06 must use the symmetric-square multiplicity. A gate
`b ≥ s − U + 1` written against the ordinary `g` is not conservative — it is a
different inequality.

## 2. The condition to add: the warning needs `a ≥ 1` beside it

Both cells the report cites are **ambient-empty**. I computed the ambient multiplicity
in `Sym^3(Sym^4 C^5)`:

```
(6,3,1,1,1)  a = 0        (5,3,2,1,1)  a = 0
```

and in fact **no** five-row `lambda ⊢ 12` has `a > 0` — consistent with B18-01's
Lemma 8.1, which puts the first five-row cell at `d = 5`.

The arithmetic illustration is valid and the g-versus-s gap is real. But as *cells*
these two hold nothing: `m_det ≤ a = 0` and `m_pad ≤ a = 0`, so `D = 0` identically,
whatever `s`, `b` or `U` say.

**The consequence for Slot 06 is concrete.** A selection rule phrased in `s`, `b` and
`U` alone can nominate cells that are empty in the ambient. The gate needs `a ≥ 1`
as a precondition, not as an afterthought. B18-02's warning and this condition should
travel together, because separately each is misleading: use `g` and the gate is the
wrong inequality; use `s` without `a` and the cell may not exist.

## 3. Convergence with B18-01, which is worth noting

B18-01 §8.6 stage 1 proposes computing `g` first and adds: "For cells with `g ≥ 1`,
compute the transposition-symmetric `s` … `s = 0` also certifies." B18-02 independently
establishes that `s` is strictly smaller than `g` in five-row cells and supplies the
machinery to compute it.

The two slots agree without having seen each other, and they are complementary: 01
supplies the finite list of cells where a hit would be a gap, 02 supplies the correct
multiplicity to screen them with. That is the batch working as intended.

## 4. Inference directions — checked, and correct

- **The modular certificate is used as a floor.** "A nonzero minor at one prime is a
  valid characteristic-zero floor `b`." Correct: a nonzero minor mod `p` forces a
  nonzero minor over `Q`, so `rank_Q ≥ rank_p`. This is the programme's standing rule
  (`rank_p ≤ rank_Q`) applied in the one direction it permits — a *floor*, never a
  ceiling, and never from a modular *zero*.
- **The weight lemma's arithmetic is self-consistent.** Weight `= 2d − skew degree`,
  weights in `[−d, 2d]`, so `C` is the projection onto negative weight, and the node
  count is `2d − (−d) + 1 = 3d + 1` against a naive `8d + 1`. At `d = 7` that is 22
  nodes versus 57. Arithmetic checks; the lemma itself I have not reproved.

## 5. The honest negative is the best thing in the delivery

> "Every measured cell has `m_det = a`, so this cannot distinguish 'arc criterion
> exact' from 'arc only reproduces the ceiling'."

Twenty cells certified with basis rank `= s`, and in all twenty `s − b = a`, so `B = a`
— and the slot says plainly that this means the control **cannot fail informatively**,
so it does not support the criterion. That is `check_must_be_able_to_fail` applied to
the slot's own evidence, unprompted. Recorded as the missing theorem in its §8 rather
than dressed as confirmation.

## 6. Pricing

A five-row `d = 7` cell at `s = 100` is about 6 hours and at `s = 300` about 57 hours,
**conditional on hypothesis H1 (the local family spans), which is not proved**. Random
pairings are a barrier at `d = 7`; explicit adapted-coordinate expansion is a barrier
everywhere including `d = 3`; ten-row LMR-type cells are a barrier for this carrier.

All correctly labelled as estimates on an unproved hypothesis, all far outside any
pilot, and the slot stopped rather than starting one. No heavy lease was used. Nothing
here should be converted into a lease request until H1 is either proved or measured.

## 7. The disclosure, and whose defect it is

The slot discloses one read-only `git status --porcelain` beyond the two authorised
`rev-parse` calls. It changed nothing and it is recorded in the report.

It was also **explicitly permitted** — `Bash(git status:*)` is on the allow list I gave
for these sessions. The preamble says "run no other git command"; the permission list
says `git status` is fine. Those two documents disagree, and the slot did the right
thing by disclosing rather than assuming.

My defect, and the fourth of this species in this batch: a document I issued that
contradicts another document I issued. The preamble should be amended to permit
`git status --porcelain` explicitly, which is what the permission list already does.

## 8. What enters the index

| id | statement | status |
|---|---|---|
| `transposition_changes_s` | The symmetric rectangular Kronecker `s = [S^lambda : Sym^2(S^(d^4))]` is strictly smaller than the ordinary `g` in five-row cells already at `d = 3`: `(6,3,1,1,1)` has `g = 3`, `s = 1`; `(5,3,2,1,1)` has `g = 4`, `s = 2`. A gate written in `g` is a different inequality, not a conservative one | MEASURED, exact; recomputed independently here |
| `s_gate_needs_ambient` | A cell selected by `s`, `b` and `U` alone may be empty in the ambient. Both cells above have `a = 0`, and no five-row `lambda ⊢ 12` has `a > 0`. `a ≥ 1` is a precondition of any five-row gate, not a refinement of it | PROVED; computed here |
| `carrier_without_the_big_tensor` | `M_lambda` is realised as full-H-invariant highest-weight polynomials on m-tuples of 4×4 matrices, spanned by symmetrised double-epsilon contractions `P_{pi,rho} + P_{rho,pi}`, with the transposition imposed by the symmetrisation. No `16^(4d)` tensor is formed | PROVED |
| `skew_weight_lemma` | On every invariant the gamma-weight of an adapted-coordinate monomial is `2d − (skew degree)`; weights lie in `[−d, 2d]`, the upper forbidden range is empty, and `C` is the projection onto skew degree `> 2d`. Interpolation nodes fall from `8d+1` to `3d+1` | PROVED; arithmetic checked here, lemma not reproved |
| `arc_control_cannot_discriminate` | In all 20 certified cells (`d = 2` complete, 15 cells at `d = 3`) the basis rank equals `s` and `s − b = a`, so `B = a` and `m_det = a`. The control therefore cannot separate "the arc criterion is exact" from "the arc reproduces the ambient ceiling". It is not evidence for the criterion | MEASURED, and recorded by the slot as its own missing theorem |

## 9. Carry-forward

1. Slot 06 must receive `transposition_changes_s` **and** `s_gate_needs_ambient`
   together. Either alone misleads.
2. Amend the preamble to permit `git status --porcelain`, matching the permission list.
3. H1 is unproved and every `d = 7` price rests on it. No lease against it.
