# Pre-registration — Session 68 (C1): the ladder source, seed at δ=12 then births

Branch `s68-ladder` off `main` at `226b4ef121a674a47d949db0c3178f8264a67e27`
(ancestry gate `git merge-base --is-ancestor 226b4ef1 HEAD` — **PASS**).
Committed **before any new measurement** of the session. The batch-11 preamble
and plan the brief cites (`docs/batch11_worker_preamble.md`,
`docs/batch11_plan.md`) exist in no clone and were not on the connected laptop
tree at read time; this session works from the brief's own statement of §2.1,
§2.3, §5(iii), from `docs/s57_report.md` (Lemma L, Proposition S, the ladder
theorem), `docs/lmr_cell.md`, `docs/sparse_det_route.md` (the s45 engine) and
`docs/stabiliser_reduction.md`. Labels used throughout:
**proved** / **measured** / **adopted-from-literature** / **expectation**.

Container: 2 cores, ~7 GB RAM (same class as s63). Exact arithmetic throughout
(python-flint `nmod_mat`, two house primes `P1,P2`, CRT / rational
reconstruction where a characteristic-0 statement is claimed). Delivery by a
single-ref git bundle; nothing pushed. No single-writer file
(`paper/det3-conductor.tex`, `paper/det4-onset.tex`, `PROJECT_NOTES.md`,
`docs/boundary_deficit.html`) will be edited. Following the programme's standing
rule (s49, s59, s62, s63), no session-link trailer is added to commits.

---

## 0. The question, restated

Can the 274-dimensional LMR source `M_λ` at `λ = (65,17,2⁷)`, `δ = 24` be built
one ladder rung at a time — seed at `δ = 12`, then `M_δ = J(M_{δ−1}) ⊕ B_δ` —
without ever forming the full carrier `V_χ` (`n_χ ≈ 3.1×10⁷`)?

`M_λ = HWV_λ = ker E` on the χ-isotypic reduced weight space `V_χ`
(`docs/stabiliser_reduction.md`, `docs/sparse_det_route.md`), `dim = a`. The
ladder unit is fixed tail `t = (17,2⁷)` (`|t| = 31`), `λ_δ = (4δ − 31, t)`;
transport `J` is multiplication by the `s₁⁴`-coefficient `c = c_{(4,0,…,0)}`
(Lemma L, **proved** in s57), which injects `HWV` of weight `λ_{δ−1}` in degree
`δ−1` into `HWV` of weight `λ_δ` in degree `δ`. The ladder theorem gives
`dim J(M_{δ−1}) = a_{δ−1}` exactly, so `dim B_δ = a_δ − a_{δ−1}` (the birth
sequence `2,37,54,52,43,31,22,14,9,5,3,1,1` for `δ = 12..24`).

**Two objects the session produces are separately budgeted and separately
judged** — Part A (the seed) and Part B (the rungs). A seed failure is **not** a
ladder-algorithm failure and will be reported as such.

---

## Part A — the seed (budgeted and judged separately)

`M₁₂` at `λ₁₂ = (17,17,2⁷)` (`λ₁ = λ₂ = 17`, `|Stab| = 2!·7! = 10080`) is a
2-dimensional kernel inside `n_χ ≈ 5.10×10⁶` coordinates
(`N_S = 51,446,325,457`). It is the bottom of the ladder (`4δ−31 ≥ 17 ⇔ δ ≥ 12`),
so it has no predecessor to transport from and **must be built from scratch** —
the one point on the ladder where support restriction offers no saving.

**Task A.** Obtain the two `M₁₂` highest-weight vectors and certify them against
the full raising action (not support-restricted) with `dim = a₁₂ = 2` exactly, in
`V_χ` source coordinates, delivered as the `s63`-format `.npz` artefact template.
Any method admissible.

### Falsifiers / decision (Part A)

- **A-hit** — the two seed HWVs are materialised and certified (`E·v = 0` on the
  full `E` at both primes; `dim ker E₁₂ = 2` exact). Report the cost and proceed
  to Part B from the true seed.
- **A-wall (pre-registered expectation, ~0.9)** — the seed build and/or solve
  exceeds the container by the margins projected below. Then **stop Part A**,
  report the cost curve and where it goes out of reach, and record it as a
  **seed failure, explicitly not a ladder-algorithm failure**. The ladder
  algorithm is then tested on a reachable ladder instead (Part B).

**Pre-registered cost projection (expectation, to be confirmed by direct
sizing).** Using the s45 measured laws (`peak ≈ 159 bytes × N_S`;
`nnz ≈ 3.5 × N_S`; solve `≈ 10.6×10⁻⁹ × n_χ × nnz_c` s):

- monomial array `(N_S × δ)` int32 `= 51.4×10⁹ × 12 × 4 B ≈ 2.5 TB`; peak
  `≈ 8 TB` — vs 7 GB (wall ≈ 10³).
- `nnz(E) ≈ 1.8×10¹¹` → CSR `≈ 1.4 TB` (wall ≈ 200).
- one full solve `≈ 10.6×10⁻⁹ × 5.1×10⁶ × 1.8×10¹¹ ≈ 10¹⁰ s ≈ 300 yr` / prime
  (wall ≈ 10⁴–10⁵ even fully parallelised — block Wiedemann reduces latency, not
  the `~2 n_χ` matvecs of `O(nnz)` each).

**Confirm/refute of the projection.** A-wall is *confirmed* if the direct sizing
reproduces `N_S₁₂ = 51,446,325,457`, `|Stab| = 10080`, `n_χ~ = 5.10×10⁶` and the
build OOMs (or is projected past 7 GB by ≥ 10×) **and** the solve estimate
exceeds 30 days on 2 cores. It is *refuted* — an A-hit — if any admissible
method materialises and certifies the two vectors inside a 2-day / 7-GB budget.

The streaming-orbit-representative build named by s63 as the only opening is
**sized, not built** (reserve-class): it removes the monomial-array wall
(`n_χ × δ ≈ 0.26 GB`) but the reduced matrix `nnz ≈ 3.5 N_S` is set by
`|Stab| = 10080` and stays TB-scale, and the solve wall is untouched — so the
prediction is that streaming alone does not open the seed. (Confirm/refute:
compute `nnz/n_χ` vs `|Stab|` on the reachable cells; the fit `nnz/n_χ ≈ c·|Stab|`
with `c ≈ 3–3.5` confirms the projection.)

---

## Part B — the rungs (the ladder algorithm)

Because the LMR seed is expected to wall (A-wall), the **algorithm** is tested on
reachable ladders where every `M_δ` is independently computable as `ker_Q E_δ`
(flint, exact), so the transport+deflate construction can be checked against
ground truth at every rung. Chosen ladders (`n = 4`, sizes measured this
session, `a` = `dim ker_Q E` = ground truth):

- **L1 = tail `(6,4,2)`, `ℓ = 4`** — cells `(4δ−12,6,4,2)`, `|Stab| = 1`.
  Measured `a = 3,11,18,22` at `δ = 5,6,7,8`; `n_χ = 939,1626,2087,2318`.
  **Multi-dimensional seed `a = 3`** (the LMR seed is `a = 2`) and large births
  `8,7,4` — the closest reachable analogue of the LMR construction.
- **L2 = tail `(4,4,2)`, `ℓ = 4`** — cells `(4δ−10,4,4,2)`, `|Stab| = 2`.
  Measured `a = 1,3,5,6,6` at `δ = 4..8`; `n_χ = 160,312,416,463,479`. Birth
  sequence `1,2,2,1,0` and a **nontrivial stabiliser** (transport must commute
  with χ-projection).

**Task B (per rung `δ`).**
1. **Transport** `J`: multiply each `M_{δ−1}` vector by `u = c_{(4,0,…,0)}` →
   `a_{δ−1}` vectors in `V_χ(δ)`. Support of `J(M_{δ−1})` is known before any
   solve (transport preserves monomial-support size exactly).
2. **Deflate**: solve `ker[E_δ; R]`, `R` = `a_{δ−1}` generic dense rows, for a
   kernel `B_δ` of dimension `a_δ − a_{δ−1}`.
3. **Certify the rung** — all three required:
   (i) the `a_{δ−1}` transported vectors lie in `ker E_δ` (checked on the full
   `E_δ`, both primes);
   (ii) `dim ker[E_δ;R] = a_δ − a_{δ−1}` with `a_δ` independently known
   (`a_δ = dim ker_Q E_δ`), and `R|_{J(M_{δ−1})}` nonsingular (so `B_δ` is a
   genuine complement: `J(M_{δ−1}) ∩ B_δ = 0`);
   (iii) every new `B_δ` vector passes the **full** raising action including
   target rows outside the current support.
4. **Measure**: live support size / `n_χ`, wall clock, peak memory, found birth
   dim vs known `a_δ − a_{δ−1}`.

### Falsifiers / decision (Part B)

- **B-pass** — at every reachable rung the three-part certificate holds and
  `span(J(M_{δ−1}) ∪ B_δ) = ker_Q E_δ` (exact subspace equality vs ground truth,
  both primes). This validates the algorithm.
- **B-fail** — any of: transported vectors not in `ker E_δ` (Lemma L wrong as
  implemented); `dim ker[E_δ;R] ≠ a_δ − a_{δ−1}`; `R|_J` singular at a generic
  draw at both primes; or `span(J ∪ B_δ) ≠ ker E_δ`. Any B-fail is a bug or a
  refutation of the construction and is reported, not patched over.

Pre-registered expectation: **B-pass at every reachable rung** (confidence 0.9),
since Lemma L is proved and deflation is standard; the value is the *exhibited,
certified* construction and the honest cost/support curve.

---

## Part C — by-products (where reachable)

- **`i_pad(δ)`, `i_det(δ)`** on the reachable ladders:
  `mult_X = a − nullity([E; ev_X])`, `i_X = a − mult_X`, by the s45 pairing.
  Expectation: `i_det = 0` at all reachable determinant cells (the record is
  empty everywhere `r ≤ 6`), so these demonstrate the by-product computation and
  Lemma-L monotonicity of `i_X` (non-decreasing up the ladder), not a bite.
- **Support density** — the fraction of `n_χ` on which the `HWV` basis is
  supported, measured on every reachable ladder cell. The brief names this a
  deliverable in its own right (the `0.20–0.26` figure was measured at `δ = 4`,
  not on this family). Confirm/refute of "support restriction does the work":
  density well below 1 supports the deflation saving; density near 1 refutes it.
- **`i_pad` at LMR / `A₂₄`**: gated on the seed (A-wall) and therefore
  **not attempted**; sized only.

## Stopping rules (from the brief)

1. Seed unreachable in budget → stop Part A, report Part A only (as a seed
   failure, not a ladder-algorithm failure), then test the algorithm on the
   reachable ladders (Part B).
2. Live support at a rung with small `a_δ` grows to carrier scale → the support
   restriction does not do the work (the plan's stated risk); report the
   measured densities and stop that ladder.
3. **Do not** fall back to building the full carrier at any LMR rung. s63
   quantified that wall on all realisations; reconfirming it is not a use of the
   night.

## Deliverables

`results/PREREG_s68.md` (this file); `docs/s68_report.md`; the seed/rung bases as
machine-readable artefacts under `results/artefacts/`; per-rung cost+support
table `results/s68_rungs.md` and `.jsonl`; code `analysis/wk11_s68_*.py`; bundle
`s68_ladder.bundle` (+ `.md5`).
