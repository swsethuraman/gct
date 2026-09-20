# Pre-registration — B24-04 pilot 1 (`b24_04_p1_patterns`)

Written and hashed before the pilot was written or run. The pilot prints this file's sha256 in
its own output (G25). Slot B24-04, worktree `work/batch15_workers/B15-02`, branch
`b15-02-a1-probes`, HEAD `feed104ea865ed5f76809f6d77455060af01433c`.

## What is being asked (Question 3 of the launch prompt)

B22-01's Missing Theorem produced 70 typed `eps_3`-contraction patterns forming a certified basis
of `F^L_{-1}`. **(a)** Is that basis canonical? **(b)** Is there a statistic on the 70 whose graded
count has the Kostka-Foulkes shape (non-negative, unimodal, forced degree)?

## The operational criterion (fixed here, before any run)

A statistic `st` on patterns **grades** `F^L_{-1}` iff the subspaces
`V_{<=j} := span{ h : st(h) <= j }` form a **proper** filtration, i.e. `dim V_{<=j}` takes at least
two distinct values as `j` ranges over the values of `st`. Otherwise `st` is **trivial**: the
lowest class alone already spans, and the "grading" is empty.

`V_{<=j}` is the span over **all** patterns with `st <= j`, not over a sample. Therefore:

- a sampled rank that **reaches** the ambient dimension **proves** `V_{<=j}` is everything (a rank
  is a floor); the statistic is then trivial at that `j` — **PROVED negative**;
- a sampled rank that stays **below** is a **MEASURED** lower bound only, never a proof that the
  filtration is proper. It is a candidate, to be reported as such and not as a grading.

Ranks are modulo `P = 524287`. A modular rank is a floor for the rational rank, never a ceiling
(G27): "reaches the ambient dimension" is therefore safe in the direction used above.

## The instrument

Point evaluation at B22-01's 70 certificate points is **certified injective** on `F^L_{-1}`
(`det E != 0 mod P`, B22-01 §1.2, pinned below). So for any finite set of patterns,
`rank of their 70-point evaluation matrix = dim of their span`. No new certification is needed;
the certificate is replayed as control C1.

## Stages

- **S0 pins.** sha256 of the two pinned B22-01 artefacts against B22-01's `MANIFEST.json` at
  `53bdb31e3042acae9464f9025be355ae699a2485`. Rebuild the 70 certificate points from
  `rng(20260922)` and compare to the points recorded in `p2_basis.json` (control C0).
- **S1 replay (control C1).** Recompute `Xi_h` and `F_1^h` at the 80 recorded points for all 70
  selected degree-11 patterns with the pinned `b22_01_typed_v2.py`; require byte-equality with
  the recorded `vec80`. Recompute the `70 x 70` determinant mod `P`; require nonzero.
- **S2 the multidegree grading.** Per-block ranks of the selected patterns' 70-vectors; total
  rank. Targets `7, 31, 28, 4` and `70`. Equality of the sum with the total proves the four block
  spans are **independent**, hence a direct-sum decomposition, hence a grading.
- **S3 saturation (control C2, second lineage).** Fresh random patterns per block under a **new**
  seed `20260919`. No block rank may exceed its target. A block rank above target contradicts
  `b_L(11) = 70` and stops the pilot.
- **S4 the statistics.** For each statistic below and each block, the profile
  `(j, #patterns with st <= j, rank)` over the pooled selected + sampled patterns, and the verdict
  trivial / candidate by the criterion above.

## The statistics to be tried (fixed here; no others will be added after seeing results)

On a pattern `h` with columns `cols[0..3]` (non-`K` types; `K`-counts `2,3,3,3`) and ten leg
triples:

| name | definition | invariant under the symmetries of `h`? |
|---|---|---|
| `s_a` | `#a`, the multidegree label (`= 5 - #r`) | yes |
| `s_in` | number of triples whose three legs lie in **one** column | yes |
| `s_sp` | `sum over triples of (#distinct columns touched - 1)` | yes |
| `s_kk` | number of triples all three of whose legs are of type `K` | yes |
| `s_nk` | number of triples containing at least one non-`K` leg | yes |
| `s_rep` | number of columns whose non-`K` type multiset has a repeat | yes |
| `s_cr` | crossing number of the triple partition in the stored linear leg order | **no** |
| `s_inv` | inversions of the type word read column by column, `a<r<c<S<K` | **no** |

"Invariant" means: unchanged by permuting columns 1-3 (which carry equal `K`-counts and the same
argument `D`), and by reordering slots inside a column (the column is fully antisymmetrised, so
this changes `h` by a sign only). `s_cr` and `s_inv` are presentation-dependent; they are still
tested, because `span{st <= j}` is well defined for any statistic, but a grading found through
one of them would not be a grading of `F^L_{-1}` and will not be reported as one.

## What will be reported whatever happens

Every statistic's profile, including the trivial ones. A negative is the expected outcome and is
the deliverable. Nothing here is claimed about Kronecker coefficients, about any other weight
space, or about plethysm in general.

## Budget

One wrapped pilot, 60 s / 512 MiB, deadline-guarded at 55 s, JSON written after every stage.
No runner evaluation. Producer-only (G18).

## Pinned inputs (both bound by B22-01's `MANIFEST.json` at `53bdb31e`)

```
analysis/b22_01_typed_v2.py   93d739eda3afd8c0dbddf452de1e73e76470864fd8ece27171f683574eb326fc  13226 B
results/b22_01/p2_basis.json  7162d852b4490d2f22702b9b974979e403dd0dfb8794cef92b6be894d9a66e79 293596 B
```
