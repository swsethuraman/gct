# Session 45 — the determinant side at O(nnz) memory: a sparse certificate, and the first balanced six-row cells

You are session 45 of the gct programme, working for the integrator.  Date your
work 2026-09-03 onward.  This session removes the memory wall that has bounded
every determinant-side measurement the programme has made.  If the repository
already shows a session 45, do not renumber; flag it and carry on.

## Why this session exists

At `n = 4`, `ℓ(λ) = 6`, an obstruction requires `mult_det < a`, and 90 measured
cells through `δ = 8` all have `mult_det = a`.  The cells where the determinant
ideal would plausibly first appear are the **balanced** ones (parts close
together), and they are unreachable for a structural reason: the stabiliser
reduction of `docs/stabiliser_reduction.md` divides the weight space by
`|Stab_W(λ)|`, which is `1` when the parts of `λ` are distinct — so balanced
cells get no reduction at all.  Session 41 reached `n_χ = 19,985` at 4.68 GB
using a dense in-place `rref`; cost grows as `8 n_χ^2` bytes, so the smallest
balanced cell in the region (`n_χ ≈ 91,834`) needs of order 100 GB and is out of
reach on any container we have.

But the quantity wanted is only the **nullity of a sparse matrix**, and the
common answer is `0`.  Nullity of a sparse matrix does not need `O(n^2)` memory.
This session builds that route and uses it.

## The construction, stated so you can implement it from here

Fix a cell `(λ, δ)`, `n = 4`, `r = ℓ(λ)`.  Let `V_χ` be the `χ_λ`-isotypic
reduction of the `λ`-weight space of `C[Sym^4 C^r]_δ`
(`analysis/wk9_s36_stabred.py`, `orbit_setup` / `reduced_rows`, used unchanged),
of dimension `n_χ`, and let `E` be the stacked simple raising operators on it,
so `HWV_λ = ker E` and `dim ker E = a` (the plethysm value — assert it, never
read `a` off a kernel).  For points `P_1, …, P_K` let `ev_j` be the row that
evaluates a weight vector at `P_j`, contracted to `χ`-coordinates.  Then

    mult_det(λ, δ) = a − dim ker [ E ; ev_1 ; … ; ev_K ]      (K ≥ a + 8 det points)

so **`nullity([E; ev]) = 0` ⟺ `mult_det = a`**, and likewise on the pad side with
true padded-permanent points.  Over `F_p`, `rank_p ≤ rank_Q`, hence
`nullity_p ≥ nullity_Q`, hence

    a − nullity_p([E; ev])  ≤  mult_det  ≤  a .

So **`nullity_p = 0` at a single prime is a proof** that `mult_det = a` — no
randomness in that direction.  `nullity_p = k > 0` only *suggests*
`mult_det = a − k`: it must be promoted by exhibiting `k` independent kernel
vectors and verifying them exactly (integer arithmetic, or exact evaluation at
the points).  **An onset claim is never a mod-`p` nullity alone.**

### Deciding nullity without dense linear algebra (Wiedemann, with certificates)

Let `F = [E; ev]`, `m × n` over `F_p`, held as a sparse structure (CSR); `D_1,
D_2` diagonal with entries uniform in `F_p^*`; `M = D_2 F^T D_1 F D_2`
(never formed — only its action `x ↦ D_2 (F^T (D_1 (F (D_2 x))))`).

- *Lemma (preconditioner).*  `rank(F^T D F) = rank F` with probability
  `≥ 1 − n/p`.  (Cauchy–Binet expands `det((F^T D F)_{S,S})` as a nonzero
  polynomial of degree `ρ` in the `d_i`; Schwartz–Zippel.)
- *Lemma (the certificate).*  Take `u, b ∈ F_p^n`, form `s_i = u^T M^i b` for
  `0 ≤ i < 2n`, and let `f` be the minimal polynomial of that sequence
  (Berlekamp–Massey).  If `deg f = n` and `f(0) ≠ 0` then `M` is nonsingular and
  `F` has full column rank.  (The sequence's minimal polynomial divides that of
  `b` under `M`, which divides that of `M`, which divides the characteristic
  polynomial of degree `n`; equality forces `f = charpoly` and
  `f(0) = ± det M ≠ 0`.)  **No randomness enters this implication** — `D_1, D_2,
  u, b` only decide whether a run is conclusive.
- *Kernel direction.*  If `f = x^s g` with `g(0) ≠ 0`, then
  `y = D_2 M^{s-1} g(M) b` is a candidate kernel vector; **verify it** by the
  sparse product `F y = 0` before reporting it.  `k` verified independent
  vectors prove `nullity_p ≥ k`; a certificate for `[F ; R]` with `R` a random
  `k × n` block proves `nullity_p ≤ k`.
- *Row compression.*  Sampling and `±1`-grouping the rows of `E` into `~12 n`
  rows can only lose rank, so a nonsingularity certificate for the compressed
  matrix still proves `F` injective; a kernel vector that fails on the full `E`
  escalates to the full matrix.
- *Cost.*  `O(n · nnz)` field operations per sequence, `O(nnz + n)` memory —
  against `O(n^3)` time and `8 n^2` bytes dense.  Write the inner loop in C
  (one file under `analysis/`, compiled with `gcc -O3`); Berlekamp–Massey is the
  one hand-written exact routine, so validate it hard (below).  Every rank that
  is *reported as a multiplicity* still goes through `python-flint` wherever the
  cell is small enough for that to be possible.

Note the `ev` rows are dense (one entry per column), but there are only `K` of
them, so `nnz` stays dominated by `E`.

**Session 42 has delivered this machinery for the reducible side** and it will
be in your clone: `analysis/wk9_s42_sparse.py` and `analysis/wk9_s42_wied.c`
(the Wiedemann certificates), `analysis/wk9_s42_redengine.py` (the isotypic
build and the routes), `analysis/wk9_s42_orbits.py` (the vectorised orbit
setup), and `analysis/wk9_s42_detcert.py` — a det-side demonstration that
already reproduced five session-36 cells, including `a = 21` at `n_χ = 13,100`
in about 70 seconds where session 36 needed seven minutes.  **Use them; do not
rewrite them.**  Read `docs/reducible_engine.md` §A for the contract they
implement.  Your work is: the `ev` rows at scale, the det side proper, the
memory-lean build (below), the validation battery, and the sweep.  If any of
those files is missing from your clone, implement from the specification above
and say so in your report.

**The build is now the binding constraint, not the rank.**  Session 42 found the
process group capped near 4 GB and the monomial enumeration hitting it around
`N_S ~ 10^6`; the sparse solve itself needs only `O(nnz + n)`.  For balanced
`λ` the stabiliser is trivial, so `n_χ = N_S` and the build is the whole cost.
Make the enumeration streaming: generate weight-`λ` monomials in a canonical
order without materialising the full list where you can, build `E` directly as
CSR (`int32` indices), and never hold a dense copy of anything of size `n_χ^2`.
Report the measured build memory and time as a function of `N_S` — a curve, not
one number — since it determines what a successor session can reach.

## Validation — the part that decides whether this session is worth anything

A route that answers "full column rank" unconditionally would pass every
determinant-side test in the repository, because `mult_det = a` at every cell
ever measured.  **So the validation must be dominated by cells where the answer
is NOT full rank.**  Required, all at both house primes:

1. The `l^3 m` witness: `a = 1`, kernel `∝ (12, −3, 1)`, `mult = 0`
   (`analysis/wk8_s30_calib.py` as-is, which also runs the 48-cell battery in
   which 41 are discriminating).
2. Every pad-side bite the programme has: `(8,4,4,4,4)` `δ=6` (`a=2`,
   `mult_pad=1`), `(9,9,8,1,1)` `δ=7` (`a=2`, `mult_pad=1`), `(8,8,8,2,2)`
   `δ=7` (`a=3`, `mult_pad=2`), `(12,4,4,4,4)` `δ=7` (`a=4`, `mult_pad=3`),
   `(10,8,7,1,1,1)` `δ=7` (`a=3`, `mult_pad=2`) from `results/s36_ledger.md`,
   and `(13,10,6,1,1,1)` `δ=8` (`a=9`, `mult_pad=8`) from
   `results/s41_ledger.md`.  The sparse route must return the drop, and the
   exhibited kernel vectors must satisfy `E v = 0` and (★).
3. At least eight `D = 0` rows of `results/s41_ledger.md` reproduced on the det
   side, spanning `n_χ` from small to the frontier, sparse against the banked
   dense answer.
4. Berlekamp–Massey on 200 synthetic sparse matrices with planted nullities
   0–6, checked against `python-flint`.

If any of these fails, stop and report; nothing downstream is worth anything
without them.

## The sweep

Then measure six-row cells (`n = 4`, `ℓ(λ) = 6`, `a ≥ 1`, `λ_1 ≥ δ`) on the
**determinant side**, ascending in `n_χ` from 20,000 upward, `δ = 7` then
`δ = 8`, taking the most balanced cell available at each size.  Publish the
ordered list with sizes and predicted cost before you start.  Expect hours per
cell at `n_χ ~ 10^5` (one sequence is roughly `4 n · nnz` field operations);
one or two cells above 90,000 in a night is a good night, and **the first
balanced six-row cell ever measured is itself the result** — do not trade it for
breadth.

Per cell record: `a` (plethysm, asserted against the full-`E` nullity where
that is affordable), `n_χ`, `nnz`, `nullity_p([E; ev])` at both primes, the
route used, wall time, peak memory, and the verdict `mult_det = a` (proved) or
`mult_det ≤ a − k` (with exhibited, verified vectors).  Bank each cell with a
commit before starting the next.

**If `mult_det < a` appears** — the six-row onset — do not treat a mod-`p`
nullity as the answer.  Exhibit the kernel vectors, verify them exactly, re-run
at a fresh preconditioner, a fresh seed and a second prime, and check the
vectors are nonzero at 20 fresh determinant pencils' worth of independent
evaluations.  Then measure the pad side at that cell (`mult_pad`, true
padded-permanent points, and the point-free `mult_red` by (★)).  If the result
is `D = mult_pad − mult_det > 0`, halt the sweep; the verification protocol of
`docs/s41_prompt.md` takes over, and the session ends with
`docs/OBSTRUCTION_CANDIDATE.md` rather than a sweep table.

## Rules (standing)

- Fresh clone of `github.com/swsethuraman/gct`, branch `s45-sparsedet`,
  container only.  **Clone check**: `analysis/wk9_s36_stabred.py`,
  `analysis/wk8_s30_calib.py`, `results/s36_ledger.md`, `results/s41_ledger.md`,
  `docs/sixrow_frontier.md` must exist (absence ⇒ stale clone; stop and report).
- Single-writer files — never edit: `paper/det3-conductor.tex`,
  `paper/det4-onset.tex`, `PROJECT_NOTES.md`, `docs/boundary_deficit.html`.
- Delivery by git bundle (`git bundle create sparsedet.bundle s45-sparsedet`,
  single ref).  Do not push.  Checkpoint bundle every few hours.
- **Commit messages carry `Co-Authored-By` only** — no session-link trailer, in
  commits or in any script that commits.  No `claude.ai/...` URL in any file.
- No file over 5 MB committed; logs under `results/logs/`; append-only config.
- Bound long runs with `timeout` and `ulimit -v`; record each run's process id
  in `results/logs/<run>.pid` and end a run only by that recorded id, never by
  name-pattern matching.  One heavy cell at a time.
- `results/PREREG_s45.md` first: the validation list above with your predicted
  outcomes, your predicted `n_χ` frontier and cost curve, your prediction for
  whether any measured cell shows `mult_det < a` (with reasoning and regime),
  and stopping rules.

## Deliverables

`results/PREREG_s45.md`, `results/s45_validation.md`, `results/s45_ledger.md`,
`docs/sparse_det_route.md` (house style: the construction and its two lemmas
with proofs, the validation table, the measured cost curve and the frontier it
buys, coverage of the balanced corner as you leave it, honest boundary),
code `analysis/wk9_s45_*.py` and the C helper.  End with the frontier as you
leave it and the bundle head hash.
