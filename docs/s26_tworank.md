# Session brief — the a = 2 lemma, and the first live cells

**Branch `s26-tworank`, cloned fresh from public `origin/main`.**
Successor to session 23. Mathematics first, then an exact computation on a
handful of cells. **No engine, no checkpoints.** The paper's one-bit argument,
generalised and then used.

---

## 0. Standing orders

- You do **not** own `Projects\gct` (rule 9). Fresh clone, container only.
- Record the tip at clone time. `main` **should** be at `c9240f3`; if it is
  not, say so at the top of your record and branch from what is actually there.
- Write **only new files** where you can. Do not append to `PROJECT_NOTES.md`
  or `docs/boundary_deficit.html`. If you touch `paper/det3-conductor.tex`,
  flag it loudly for the integrator, as session 23 correctly did.
- Push will likely be refused by the git proxy; deliver a bundle.

---

## 1. Why this session exists

Both closure rings are quotients of the same ambient, so with `a(lam,delta)` the
multiplicity of `S_lam` in `Sym^delta(Sym^3 C^9)`, `mult <= a` on both sides.
Verified: `a = 0` for 61 of 73 weights at `delta = 4`, and **`a >= 2` first
occurs at `delta = 5`, at the single weight `lam = (9,4,2)`.**

That has a consequence for the paper worth stating plainly: **every deficit
number currently in §4 sits at a weight with `a <= 1`.** At `a = 0` the deficit
equals `m` by arithmetic; at `a = 1` it is a single bit. The programme has never
measured a closure multiplicity where the answer could be anything other than
`0`, `1`, or forced.

This session measures the first ones.

---

## 2. The mathematics — do this before any computation

**The a = 1 lemma (known, the paper's "one bit").** When `a(lam,delta) = 1` the
`lam`-isotypic component of `Sym^delta(W*)` is one irreducible `G`-submodule
`M`. The ideal `I(closure of x)` is a `G`-submodule, so it contains `M` or meets
it trivially, and it contains `M` exactly when every `f in M` has `f(x) = 0`.
Hence `mult_lam C[closure]_delta = 1` iff the projection of the evaluation
functional `ev_x` onto that component is nonzero.

**The generalisation to arbitrary `a` — prove this properly.** The isotypic
component is `S_lam (x) C^a`, with `C^a` the multiplicity space carrying trivial
`G`-action. Then `I` meets it in `S_lam (x) U` for a subspace `U <= C^a`, and
`S_lam (x) u <= I` iff `ev_x` kills `S_lam (x) u`. Writing the restriction of
`ev_x` to the component as `sum_k phi_k (x) e_k^*` with `phi_k in S_lam^*`:

        mult_lam C[closure of x]_delta  =  dim span{ phi_1, ..., phi_a } .

At `a = 1` this is "`phi_1 != 0`", recovering the one-bit statement. At `a = 2`
it is a **rank**: the two functionals are both zero (`mult = 0`), proportional
(`mult = 1`), or independent (`mult = 2`).

**The practical form.** Let `h_1, ..., h_a` be highest-weight vectors of weight
`lam` spanning the multiplicity space. `sum_k u_k h_k` lies in `I` iff it
vanishes identically on the orbit `G.x` (its `G`-translates span `S_lam (x) u`).
So

        mult = rank of the matrix  [ h_k(g_j . x) ]_{k,j}

over enough random `g_j in GL_9`. For `a = 2` that is a rank-2 question on two
explicit polynomials. Exact arithmetic; random `g_j` over a large finite field or
over `Q` with a certified nonzero minor.

**Watch the orientation.** Session 23's honest boundary flagged that the
`tau`-grading orientation was pinned by consistency rather than by tracking
`V <-> V*` through Peter–Weyl. The same dualisation bookkeeping appears here in
`S_lam` versus `S_lam^*`. Pin it, and say how.

---

## 3. The cells

`m_det` recomputed as a symmetric Kronecker and calibrated against the measured
easy counts (sums `3, 11, 43` and supports `3, 10, 34` at `delta = 2,3,4`).
`mult_det <= min(m_det, a)`.

| lam | delta | a | m_det | rows | note |
|---|---|---|---|---|---|
| **(12,6)** | 6 | 2 | 2 | **2** | cheapest: two-row weight, two bits |
| **(15,6)** | 7 | 2 | 2 | **2** | two-row, two bits |
| (9,4,2) | 5 | 2 | 3 | 3 | the first live weight anywhere |
| (12,4,2) | 6 | 2 | 3 | 3 | |
| (13,6,2) | 7 | 3 | 4 | 3 | first `a = 3` |

Start with `(12,6)` and `(15,6)`. Two-row weights in a plethysm of a cubic are
the classical transvectant/bracket case, and the highest-weight vectors are
constructible by hand rather than by a general algorithm.

Compute, for each cell: `mult_det`, hence `def_det = m_det - mult_det`, and
`mult_per_3` alongside as calibration.

**Be clear what the permanent number does and does not mean here.** Unpadded,
`dim closure(per_3) = 77 > 65 = dim closure(det_3)`, so `per_3` is outside for
dimension reasons and no obstruction is needed or expected. `mult_per_3` here is
a calibration of the method, **not** a GCT measurement. Do not report it as one.
The GCT-relevant version is padded at `n = 4`, and is not this session.

The payoff of this session is for the **paper**: the first deficit of a
determinant measured at a weight where the ambient had room, and therefore the
first one that is about boundary geometry rather than about the plethysm.

---

## 4. Pre-registration — commit before computing

`results/PREREG_s26.md`, committed first:

1. Predicted `mult_det` at `(12,6)` and `(15,6)` — `0`, `1` or `2` — with
   reasoning, and a falsifier for each.
2. Predicted `def_det` at those cells, and whether you expect it nonzero.
3. Whether you expect the `a = 2` rank lemma to need `a` random points or
   fewer, and what would show your bound is not tight.

The integrator has **no confident prior** on `mult_det` here and will not
pretend otherwise: `closure(det_3)` has dimension 65 inside a 165-dimensional
ambient, so its ideal is large and `mult_det < a` is entirely possible; but the
determinant has filled every ambient slot available to it so far. That is the
whole reason the cell is worth measuring.

---

## 5. Kill criteria

- **If `mult_det = 2` at both two-row cells** — the determinant filling the room
  — the `a = 2` stratum at `n = 3` is closed; report that and move the search to
  `a >= 3` or to `n = 4`.
- **If the rank method disagrees with the paper at any `a = 1` weight** where
  `mult` is already known, stop: the lemma or its orientation is wrong, and
  everything downstream of it is void.
- **If `mult_det = 0` while `m_det = 2`** — a full deficit with ambient room
  available — that is the first genuine (non-forced) full deficit in the
  programme and should be reported immediately; it bears directly on §4.

---

## 6. Deliverables

    results/PREREG_s26.md        pre-registration, committed FIRST
    docs/isotypic_rank.md        the lemma, its proof, the orientation argument,
                                 and the practical algorithm
    docs/live_cells.md           the measured cells: mult, def, both sides
    docs/session_26.md           session record, prediction ledger, honest boundary
    analysis/wk6_s26_*.py        highest-weight vectors, the rank computation

Every number twice. If the lemma turns out to need a hypothesis you did not
anticipate, state the hypothesis and where it fails, in session 23's style —
that session's value came from refuting its own Theorem 3.1, not from confirming
it.
