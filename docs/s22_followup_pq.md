**Your work is merged. New task below.**

`main` is now at `5cdc29c` on `https://github.com/swsethuraman/gct`, and it
contains your branch's full history — including the pre-registration commit
`2545f1e` with its original timestamp. `s22-chi` has been deleted locally
because it was fully merged. Theorem 5.5 is in the paper with your proof, and
your `docs/chi_det2.md` is the deliverable it points at.

Three notes on the merge, because the paper is not exactly what you left:

- Your abstract sentence was combined with a referee revision that landed while
  you were working. It now reads "several of whose natural symmetries we rule
  out, but whose totals we then determine exactly" — keeping both the refutations
  of Remark 5.11 and your result.
- **Remark 5.10, an arithmetic signature, was re-appended.** You branched before
  it existed and your §5 rewrite dropped it. It is the 151,200 divisibility with
  the checkable X₄ table.
- Section 4 has grown: `thm:ambient` (4.3), `def:phi18` (4.4), the degree-24
  theorem (4.10), and `prop:def222` (4.15). Renumber references accordingly.

Re-clone and branch fresh off current `main`:

```
git clone https://github.com/swsethuraman/gct.git
cd gct
git checkout -b s22-pq
```

Push only that branch. If the git proxy still refuses, commit locally and send a
`git bundle` at each milestone.

---

## The task: Question 7.2, the totals law at other weights

You wrote it, and it is the natural continuation. For a deficit weight
`λ' = (p,p,p,q^6)` your own computation gives

```
chi = det(t)^q · det(q|_{V/W})^{p-q}
```

so the character in the parameter slot is `det^{p-q}` and the transpose coset is
harmless precisely when `q` is even. At `λ' = (8,8,8,6^6)` we have `p-q = 2`,
which is why the governing object is Aronhold's degree-6 `I_6`. The
correspondence continues, and it is too clean to be accidental:

| `p-q` | governing invariant | multidegree | example weight |
|---|---|---|---|
| 2 | `I_6` (Aronhold) | (2,2,2) | `(8,8,8,6^6)` |
| 3 | degree-9 Vinberg generator | (3,3,3) | `(9,9,9,6^6)` |
| 4 | degree-12 Vinberg generator | (4,4,4) | `(10,10,10,6^6)` |

Vinberg's classification of the `C^3⊗C^3⊗C^3` θ-representation gives generators
in exactly degrees 6, 9, 12 (see `docs/i6_identification.md` and the
Bremner–Hu–Oeding reference in the paper).

**Two parts, and only the second needs the engine.**

**(a) Does the uniqueness step survive?** At `p-q = 3` and `4`, does the counting
lemma still force a balanced bidegree, so that the equivariance argument has a
one-dimensional space to land in? Your session-19 uniqueness was specific:
inside the 9-dimensional bidegree-(2,2) simultaneous-conjugation space,
slab-equivariance with character `det^2` leaves exactly one dimension. Establish
or refute the analogue at `det^3` and `det^4` — including what the relevant
space's dimension even is, and whether polarised Cayley–Hamilton still gives
exactly one relation.

**(b) The transpose-vanishing law.** When `q` is odd, `chi` acquires `−1` on the
transpose coset while any `det^{even}` semi-invariant does not, which forces
`TOTAL` to vanish on every direction whose net is `H`-equivalent to its own
transpose. **You have tested none of this.** Identify a concrete self-transpose
net at an odd-`q` weight, pre-register the prediction `TOTAL = 0`, and hand it to
the engine track. It is one evaluation and it is a clean falsifier.

---

## One thing you must know before building on this

**Your proof has an outstanding external test that has not been run.**
`TOTAL(X_-3) = -3,456,432,000` is pre-registered and unmeasured; the engine track
has it as top priority. Every falsifier you named (F1–F5) is *internal* to the
derivation. Ψ = −3 is the first *measurement* that can contradict it, because
every total ever measured sits at Ψ ∈ {0, 1, 4}, all non-negative, and your
argument is a parity argument.

The `p-q` generalisation rests on the same character computation. **If X₋₃
refutes Theorem 5.5, this task collapses with it.** So structure the work
accordingly: keep the parts that are independent of the character claim
separable, and say explicitly in your deliverable which conclusions survive a
retraction of Theorem 5.5 and which do not. A generalisation that degrades
gracefully under refutation is worth more than one that has to be thrown away
whole.

## Traps that have already cost this programme a session each

- **Totals, not per-σ.** The double-coset theorem constrains totals. The
  σ-decomposition is stable under neither Q nor H; testing per-σ produces a
  spurious contradiction. Session 16 refuted both that per-σ values inherit
  GL₂-covariance and that they are simultaneous-conjugation invariants.
- **The orientation of Q** — the weight-8 block receives from the weight-6 block.
  The opposite orientation predicts `V ≡ 0` and is refuted instantly.
- **Homogeneity pins conventions**: `V(2N) = 16·V(N)`. Use it, don't assume.
- **The group has been smaller than the phenomenon before.** C and R sit in
  different cosets with equal totals; you explained that, but the lesson stands —
  a symmetry argument that seems to explain a regularity may be explaining less
  than it appears.

## Discipline and deliverables

Pre-register predictions with named falsifiers before doing the work, as you did
at `2545f1e` — that commit is now the model. Exact arithmetic only. Honest
negatives are results here.

1. A pre-registration commit before any computation.
2. `docs/pq_weights.md` — the deliverable, in the style of `chi_det2.md`, with an
   explicit statement of what survives if Theorem 5.5 is retracted.
3. A session record in `PROJECT_NOTES.md` and an entry in
   `docs/boundary_deficit.html` before its `§5`.
4. If (a) closes: revise Question 7.2 and, if warranted, state the general
   theorem. If (b) yields a concrete falsifier: pre-register it and hand it to
   the engine track rather than running it.
