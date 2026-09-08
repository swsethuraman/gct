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

**How batch 10 actually complied, and what the integrator fixed afterwards.**
Honest scorecard, because the rule above was only partly followed.

- Session 62's 44 Gram certificates were produced in wave 1, *before* the format
  landed, and carried neither `matrix_role` nor `field`.  They verified, but as
  plain ranks of the matrices — which is exactly the reading that stops an
  unlabelled Gram from being taken for `rank Θ⁺`, so their titles asserted more
  than they certified.  Relabelled `matrix_role: "gram"`, `field: "Q"` in the
  batch-11 housekeeping pass (`analysis/wk11_int_s62_relabel.py`); all 44
  re-verify `PASS`, and now certify what they claim.  The rank is over `Q` with
  an integer minor exhibited, so the characteristic-zero Gram identity applies.
- **Sessions 63, 64 and 66 shipped no certificates at all.**  The 48-cell padded
  calibration — including the two kernel witnesses the integrator independently
  re-verified — is uncertified.  This is a real shortfall and is recorded rather
  than repaired: back-filling it needs the producing session's artefacts.

**`PASS` versus `RECORDED` is a standing convention, not a batch-10 detail.**  A
certificate whose cell exceeds the checker's re-derivation budget is reported
`RECORDED`: schema, cell, independently recomputed `a`, declared field and every
evaluation point rebuilt from substitution data are all checked, and only the
rank or nullity itself is left reproducible on demand at the cost of the
original measurement.  That is inherent to an algorithmic certificate and is not
a weaker claim about the mathematics — it is a statement about this run's budget.

**Cells with `n = 3` (batch 11).**  The verifier accepts `n ∈ {3, 4}`: pencil
points carry `n × n` matrices, an explicit form has degree `n`, and there is a
`permanent` point family for the **unpadded** `per_n` pencil.  That family is a
different variety from `padded_permanent` (`x_0 · per_3`, the programme's model,
refused at `n ≠ 4`) and is never a substitute for it.  `n = 4` behaviour is
unchanged and the existing corpus re-verifies.  First `n = 3` certificates:
`results/certs/19_7_2_2_2_2_2_d12_n3_permanent_p*.json.gz`, the permanent half
of the `D = +1` at `(19,7,2⁵)₁₂`, both `RECORDED`.


## Batch 11: the corpus, and what the merge did to it

**1 082 certificates, six kinds, all schema-valid**, and the self-test passes:
`hwv`, `matrix`, `full_rank`, `sparse_nullity`, and — registered at the
batch-11 merge — `split_rank` (session 70) and `hybrid_kernel` (session 71).
`tools/verify/FORMAT.md` carries the two new schemas.

**Compliance was much better than batch 10's.**  Session 73 shipped 46
certificates for its `D`-ladder and all 46 pass; session 71 shipped 302
`hybrid_kernel` records; session 70 shipped three `split_rank` records.  The
gap batch 10 recorded — sessions 63, 64 and 66 shipping none — has no batch-11
equivalent.

**Two things the merge had to reconcile, both caused by the tree not being
pushed.**  Session 73 wrote a second dialect of `sparse_nullity` and a second
`n ∈ {3,4}` extension, and session 71 re-implemented session 67's certifier,
because neither could see the merged tree.  Both dialects are now accepted with
no check weakened; unifying them to one is session 78's job.  The unpadded
family is named `permanent_pencil` and **appended** to `FAMILIES`, which is
session 73's naming and ordering, not the integrator's first version — inserting
it in the middle shifts the fresh-point seed offsets of every later family.

**Recorded honestly:** `split_rank` and `hybrid_kernel` report `RECORDED`, not
`PASS`.  Their cells, fields and the internal consistency of every claim are
checked; the ranks themselves are not re-derived, because each needs the cell's
build — and for `split_rank`, the quartic source session 70 proved the
construction requires.
