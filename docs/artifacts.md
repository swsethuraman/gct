# Living documents

Two documents are maintained live and updated in place:

- **Conductors of Orbit Closures** — the working paper.
  Committed snapshot: `docs/conductor.html`
- **The Boundary Deficit** — the companion log, carrying all tables and the
  per-session records.
  Committed snapshot: `docs/boundary_deficit.html`

The live versions are private and their URLs are deliberately not recorded
here, since this repository is public. The committed snapshots are what a
reader should use; they are refreshed whenever the live documents change.

The arXiv version of the paper is `paper/det3-conductor.tex`.

# Machine-reproducible certificates

Every proved multiplicity claim the programme can witness is recorded as a
`gct-cert/1` certificate under `results/certs/` and checked by the independent
verifier `tools/verify/verify.py` (format: `tools/verify/FORMAT.md`).  The
verifier imports nothing from `analysis/` and re-derives each claim from the
certificate alone.

The kinds:

- **`hwv`** — highest-weight vectors and what they vanish on: an ideal vector
  exhibited over `Z` or mod `p`, with `(★)` support and evaluation points.  A
  **characteristic-zero** (`modulus: null`) `hwv` certificate is how a genuine
  bite (`i ≥ 1`, `mult < a`) is witnessed.
- **`matrix`** — an exact rank / minor / nullity claim on a serialised integer
  matrix (the Macaulay `cap(n)` matrices; session 56's `Θ⁺` Gram blocks `β` and
  `b^μ`).  A Gram-route rank claim (`matrix_role: "gram"`, `rank β = rank Θ⁺`)
  must declare `field: "Q"` — see below.
- **`full_rank`** — `mult_X(λ, δ) = a` by an explicit or recomputed
  highest-weight basis evaluated at points of `X`, full rank mod `p`.
- **`sparse_nullity`** (session 67) — `mult_X(λ, δ) = a` by the sparse route,
  `nullity_p([E; ev_X]) = 0`, recorded as a reproducible recipe (seeds, levels,
  pinned evaluation points, and — for a positive nullity — the checked kernel
  candidates).  This is the certificate the 264 algorithmic determinant-side
  proofs of session 60 were missing; they are back-filled under
  `results/certs/s60/`.

**The declared field, and why it is load-bearing (session 67, Part A4).**  Because
`rank_p ≤ rank_Q`, a **full column rank mod `p`** certifies characteristic zero
(`mult = a`), while a **kernel mod `p`** certifies only a bound (`i ≤ k`) and no
characteristic-zero ideal membership.  Session 62's Gram identity
`rank(Θ*Θ) = rank Θ` holds **only** over characteristic zero.  So every
certificate carries a `field` (`"Q"` or `"F_<p>"`): required for `sparse_nullity`
and for Gram matrices (which must be `"Q"`), optional and consistency-checked on
the older kinds.  This is what keeps a mod-`p` Gram rank from being read
downstream as `rank Θ`, and a mod-`p` kernel from being read as a bite.

**Coordination for batch 10 (Part A5).**  Every new `Θ⁺`, Gram and padded output
this batch produces must land as one of these kinds with a declared field:
session 63's `Θ⁺`/Gram ranks as `matrix` with `matrix_role: "gram"`,
`field: "Q"`; session 64's padded-side proofs as `full_rank`/`sparse_nullity`
with `variety: "padded_permanent"`.  The format and its enforcement exist before
those sessions run, which is why C6 (session 67) is wave 1.
