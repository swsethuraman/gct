# Session 68 (C1) — the ladder source: the seed wall, and the construction validated

2026-09-08. Branch `s68-ladder` off `main` at
`226b4ef121a674a47d949db0c3178f8264a67e27` (ancestry gate
`git merge-base --is-ancestor 226b4ef1 HEAD` — **PASS**). Pre-registration
`results/PREREG_s68.md` committed at `81f70fd` **before any measurement**.
Deliverables: this report; `results/s68_rungs.md` + `results/s68_rungs.jsonl`
(per-rung cost/support/by-products); `results/s68_seed_sizing.json` (Part A);
`results/s68_idx0free.json`; `results/s68_vcheck.json` (V1 a cross-check, V2
chained climb, V3 u-free quotient); artefacts under `results/artefacts/`; code
`analysis/wk11_s68_ladder.py`, `wk11_s68_run.py`, `wk11_s68_seed.py`,
`wk11_s68_verify.py`. Exact
arithmetic throughout (python-flint, two house primes; exact `Q` for the seed
artefact). Container: 2 cores, ~7 GB. Nothing pushed; no single-writer file
touched; no session-link trailer (standing rule). Labels
**proved / measured / adopted-from-literature / expectation**.

---

## 0. Verdict

> **Two results, exactly as the brief separates them.**
>
> **Part A (the seed): the ladder cannot start in this container.** `M₁₂` at
> `λ = (17,17,2⁷)`, `δ = 12` — the bottom rung — is walled on *both* the build
> and the solve, independently, each by ≥ 100×. The seed sizing is reproduced
> exactly (`N_S = 51,446,325,457`, `|Stab| = 2!·7! = 10080`, `n_χ~ = 5.10×10⁶`;
> `a = 2` adopted from s57/s63). The monomial array alone is **2.47 TB** (353×;
> peak build ≈ **8.18 TB**, 1168×); the reduced raising matrix is
> `nnz ≈ 0.5–1.8×10¹¹` (**≈ 0.6–2.2 TB** CSR, 88–309×, depending on the nnz
> constant, §4); one Wiedemann solve is `≈ 2.8–9.7×10⁹ s` per sequence
> (**≈ 90–310 years / prime**, ≳ 10⁴× a days budget). The build (353×) and solve
> (≳ 10⁴×) walls are robust to every plausible constant. This is a **seed
> failure**, reported as such and **not** a failure of the ladder
> algorithm — which is tested separately and passes. It extends s63 (which
> walled `δ = 24`) to the cheapest point on the ladder: the ladder is out of
> reach *from the bottom*, and the seed is the hardest rung precisely because it
> is the one rung that cannot use the ladder's saving.
>
> **The s63 streaming-orbit-representative opening does not open the seed
> (fit, extrapolated).** The fit `nnz/n_χ ≈ |Stab|` on reachable cells shows the
> *reduced* matrix has `nnz ≈ N_S` — so streaming removes the monomial array but
> leaves a ≈ 0.6 TB matrix and the ≈ 90-year solve untouched (and under the s45
> `3.5 N_S` law, ≈ 2.2 TB and ≈ 310 yr). Either way streaming alone is necessary
> but nowhere near sufficient; the fit extrapolates from `|Stab| ≤ 48` to
> `10080` and the exact constant is not load-bearing for the verdict.
>
> **Part B (the algorithm): transport + deflate + certify is correct, exhibited
> and validated to the last vector.** On two reachable `n = 4` ladders — L1 tail
> `(6,4,2)` (multi-dimensional seed `a = 3`, births `8,7,4`) and L2 tail
> `(4,4,2)` (births `1,2,2,1,0`) — every rung's three-part certificate holds at
> **both house primes**, the recovered births equal `a_δ − a_{δ−1}` exactly, and
> `span(J(M_{δ−1}) ⊕ B_δ) = ker E_δ` as subspaces against the directly computed
> kernel (verified at P1 and P2; the nullity matches the exact plethysm `a_of`,
> so no rank is lost mod p and the mod-p kernel faithfully carries `ker_Q E_δ`).
> A **genuine end-to-end chained climb** — carrying the *assembled* predecessor
> forward, never the recomputed ground truth — reproduces `ker E_8` on L1 at both
> primes (`results/s68_vcheck.json`, V2). The seed is built from scratch and its
> HWVs certified over `Q` (`E·v = 0` over `Z`). Every `a` is confirmed by two
> routes — flint nullity and the plethysm `a_of`, 9/9 (V1).
>
> **Part C (support): the saving the plan needs is not there on the reachable
> analogues (measured).** The highest-weight space is **dense** — support
> fraction `0.91–1.00` of `n_χ`, uniformly high with no thinning across the
> ladder, nowhere near the `0.20–0.26` the brief saw at `δ = 4`. The u-free
> ("idx0-free") column fraction *does* shrink up
> the ladder (`69% → 10%`, matching lmr_cell §6), but **restricting the raising
> system to those columns yields kernel 0** — births are represented in the
> u-free part only as a *quotient* (projection injective, rank = birth), not as
> u-free-supported kernel vectors. So the correct deflation is the
> generic-complement solve `ker[E;R]`, which needs the full carrier at every
> rung. Support restriction, as a column restriction, does not do the work here;
> the exact sequence that does hold is recorded below for the integrator.

The honest one-line consequence: **the incremental build does not avoid the
carrier.** The seed is doubly walled, and the rungs, though the *construction* is
exact and cheap once a predecessor is in hand, still each require a full-carrier
solve because the births are dense and not u-free-supported. All of this is a
real result and none of it is an obstruction: no `D` is reported; `i_det = i_pad
= 0` at every reachable cell.

---

## 1. What `M_λ` is, and what a rung does

`M_λ = HWV_λ = ker E` on the χ-isotypic reduced weight space `V_χ`
(`docs/stabiliser_reduction.md`, `docs/sparse_det_route.md`); `dim = a`. The
ladder fixes the tail `t` and runs `λ_δ = (4δ − |t|, t)`. Transport `J` is
multiplication by the `s₁⁴`-coefficient `c = c_{(4,0,…,0)}` (Lemma L, **proved**
in s57): a `U`-invariant of `T`-weight `(4,0,…)`, so `J` carries `HWV`s of weight
`λ_{δ−1}` in degree `δ−1` to `HWV`s of weight `λ_δ` in degree `δ`, injectively.
The ladder theorem gives `dim J(M_{δ−1}) = a_{δ−1}`, so

    M_δ = J(M_{δ−1}) ⊕ B_δ ,     dim B_δ = a_δ − a_{δ−1}   (the birth).

`J` is implemented at the χ level (`transport_matrix`): a source orbit-rep
monomial `m` maps to `sort(m ∪ {c})`; "has a `c`-factor" is constant on each
`Stab(t)`-orbit (`Stab(t)` fixes position 1), so this is well-defined per column,
and the transport sign is checked consistent across every monomial of each target
orbit. Deflation (`deflate`): `B_δ = ker[E_δ; R]` with `R` a block of `a_{δ−1}`
generic dense rows, which has dimension `a_δ − a_{δ−1}` and is a complement to
`J(M_{δ−1})` when `R|_{J(M_{δ−1})}` is nonsingular.

---

## 2. Part A — the seed, budgeted and judged separately

`M₁₂` sits at `λ₁₂ = (17,17,2⁷)` (`4·12 − 31 = 17 = λ₂`, so `λ₁ = λ₂` and
`|Stab| = 2!·7! = 10080`), the **bottom** of the ladder (`4δ − 31 ≥ 17 ⇔ δ ≥ 12`).
Having no predecessor, it must be built from scratch — the one rung with no
transport and no u-free saving.

**Sizing, reproduced exactly** (`wk11_s68_seed.py`, `results/s68_seed_sizing.json`):

| quantity | value | source |
|---|---|---|
| `N_S(λ₁₂,12)` | 51,446,325,457 | exact two-prime DP (`N_S_mod`); **= lmr_cell §6** |
| `\|Stab\|` | 10,080 | `stab_group` order `= 2!·7!`; **= brief** |
| `n_χ~ = N_S/\|Stab\|` | 5.10×10⁶ | **= brief** |
| `a₁₂` | 2 | Weyl route (`a_weyl_mod`); **= s57/s63** |

**The two walls** (s45 measured cost laws; the constants cross-checked by a direct
fit, §4):

| resource | seed estimate | container | wall |
|---|---|---|---|
| monomial array `(N_S × δ)` int32 | **2.47 TB** | 7 GB | ≈ 350× |
| peak build (`≈ 159 B × N_S`) | **8.18 TB** | 7 GB | ≈ 1170× |
| reduced matrix CSR, `nnz ≈ N_S`–`3.5 N_S` | **≈ 0.6–2.2 TB** (`nnz ≈ 0.5–1.8×10¹¹`) | 7 GB | 88–309× |
| one Wiedemann solve `≈ 10.6×10⁻⁹ · n_χ · nnz` | **≈ 2.8–9.7×10⁹ s ≈ 90–310 yr / prime** | days | ≈ 10⁴–10⁵ |

The build wall (2.47 TB monomial array, 353×) and the solve wall (90–310 yr,
≳ 10⁴× a days budget) are independent and each fatal, and robust to the nnz
constant; the matrix wall is 88–309× depending on it (§4). Block Wiedemann
reduces latency, not the `~2 n_χ` matvecs of `O(nnz)` each, so it does not close
the solve wall.

**Does the s63 streaming-orbit-rep build open it? No (measured).** The fit of
`nnz/n_χ` against `|Stab|` on eight reachable cells (§4) gives `nnz/n_χ ≈ |Stab|`
for large `|Stab|` (e.g. `|Stab| = 48 → nnz/n_χ = 48.4`; `24 → 25.8`). So the
*reduced* matrix already has `nnz ≈ |Stab|·n_χ = N_S`-scale nonzeros: streaming
the build removes the `2.47 TB` monomial array (down to `n_χ × δ ≈ 0.26 GB`) but
the matrix itself stays at `≈ 10¹¹` nonzeros (`≈ 0.5–2 TB`) and the solve stays at
decades–centuries. **Streaming is necessary but nowhere near sufficient**; the
seed needs streaming *and* a ≥ 10⁴ solve speedup, and there is no candidate for
the latter.

Per the pre-registered stopping rule, Part A stops here. This is a **seed
failure**; the ladder algorithm is untested by it and is tested in Part B. No LMR
carrier was built (stopping rule 3).

---

## 3. Part B — the ladder algorithm, validated

Because the LMR seed walls, the *algorithm* is validated where every `M_δ` is
independently computable as `ker E_δ`, so the construction is checked against
ground truth at every rung (over F_p at both house primes; the nullity matches the
exact plethysm `a_of`, so no rank is lost mod p and the mod-p kernel faithfully
carries `ker_Q E_δ`). Two `n = 4` ladders, chosen to stress the LMR-shaped
features (`results/s68_rungs.md`, `results/s68_rungs.jsonl`):

- **L1, tail `(6,4,2)`, `|Stab| = 1`** — `λ_δ = (4δ−12,6,4,2)`,
  `a = 3, 11, 18, 22` at `δ = 5..8`, `n_χ = 939..2318`. **Multi-dimensional seed
  `a = 3`** (the LMR seed is `a = 2`) and large births **8, 7, 4**.
- **L2, tail `(4,4,2)`, `|Stab| = 2`** — `λ_δ = (4δ−10,4,4,2)`,
  `a = 1, 3, 5, 6, 6` at `δ = 4..8`, `n_χ = 160..479`. Births **1, 2, 2, 1, 0**
  and a **nontrivial stabiliser** (transport must commute with χ-projection).

**Result: B-pass at every reachable rung, both primes.** For each rung the
three-part certificate holds identically:

- **(i)** the `a_{δ−1}` transported vectors lie in `ker E_δ` on the **full** `E_δ`,
  and `J` is injective: `rank J = n_χ(δ−1)`, `rank J(M_{δ−1}) = a_{δ−1}`;
- **(ii)** `dim ker[E_δ; R] = a_δ − a_{δ−1}` (birth, independently known), and
  `R|_{J(M_{δ−1})}` nonsingular (so `B_δ` is a genuine complement);
- **(iii)** `span(J(M_{δ−1}) ⊕ B_δ) = ker E_δ` (subspace equality at both primes
  against the directly computed kernel; adding `ker E_δ` to the span does not
  raise its rank). At this validation scale `E·B_δ = 0` holds by construction
  (`B_δ = ker[E_δ;R] ⊆ ker E_δ`), so the operative content of (iii) is the span
  equality; the "raising on target rows outside the current support" that would
  carry (iii) at LMR scale is untested because those cells are unbuilt (§6).

The seed of each ladder is built from scratch (`ker E`); the L1 seed's three
integer HWVs are certified over `Q` — `E·v = 0` over `Z`, max `|coeff| = 82944`,
nnz per vector `662/648/861` of `939`
(`results/artefacts/s68_L1_seed_exact.npz`, the s63 `.npz` template). Every `a` is
confirmed by two routes — flint nullity of `E` and the plethysm `a_of`, all nine
cells match (`results/s68_vcheck.json` V1). A **genuine end-to-end chained climb**
that carries the *assembled* predecessor `M_{δ−1} = J(M_{δ−2}) ⊕ B_{δ−1}` forward
(never the recomputed ground-truth kernel) reproduces `ker E_8` on L1 at both
primes, births `3;8,7,4` (`results/s68_vcheck.json` V2) — so the construction
chains, it does not merely reassemble one rung from an oracle predecessor.

The birth sequences the construction recovers — L1 `3;8,7,4` and L2 `1;2,2,1,0` —
are exactly `a_δ − a_{δ−1}`, the same shape as the LMR birth sequence
`2;37,54,52,43,31,22,14,9,5,3,1,1`. The construction is thus exhibited to do at
`ℓ = 4` precisely what the brief asks it to do at the LMR cell; what it cannot do
is start (Part A) or avoid the carrier per rung (Part C). (`build_one` recomputes
the full `ker E_δ` at each rung for the ground-truth comparison; that recomputation
is the *check*, not part of the construction, which uses only transport +
deflation — see the chained climb V2.)

---

## 4. Part C — support, and why the deflation still needs the carrier

**Two distinct "support" notions, both measured** (`results/s68_rungs.md`,
`results/s68_idx0free.json`):

1. **HWV support** — the fraction of `n_χ` the highest-weight space touches
   (basis-independent). Measured **0.91–1.00** on every reachable cell (L1
   `0.950, 0.999, 0.997, 0.992`; L2 `1.000, 0.974, 1.000, 0.937, 0.906`) —
   uniformly high, with no thinning as `δ` grows. The exact L1 seed vectors have
   `662–861` nonzeros of `939`. **The highest-weight space is dense**; this is far
   from the `0.20–0.26` the brief measured at `δ = 4` (a different family and a
   much lower degree), and nowhere near sparse enough for a column-support saving.

2. **u-free ("idx0-free") column fraction** — the columns whose orbit monomials
   carry no `c = (4,0,…)` factor. This *does* shrink up the ladder
   (L1: `69% → 42% → 22% → 10%`; L2: `79% → 49% → 25% → 10% → 3%`), matching the
   u-free monomial shrinkage of lmr_cell §6.

**The structural fact that decides the deflation cost (measured, both notions
above reconciled).** At every rung the exact sequence

    0 → J(M_{δ−1}) → M_δ → π(M_δ) → 0 ,   π = projection to u-free columns

holds at the χ level: `π(J(M_{δ−1})) = 0` (rank 0, verified — the transport image
is supported entirely on `c`-containing columns) and `π|_{B_δ}` is **injective**
(`rank π(B_δ) = birth`, verified at every L1 rung, `results/s68_vcheck.json` V3).
So the u-free part faithfully
represents the *new directions as a quotient* — the reading of lmr_cell §6 that is
correct. **But** restricting the raising system to the u-free columns and taking
its kernel gives **0** at every rung (`deflate_restricted`, measured): births are
*not* u-free-supported kernel vectors, so one cannot read them off a u-free
sub-solve. The deflation that is correct — `ker[E_δ; R]` in a generic complement —
touches all `n_χ` columns, and the births it returns are dense
(`supp(B_δ) ≈ 0.99`). **Column-support restriction therefore yields no saving on
the reachable ladders**, and the two facts together (dense HWVs; births not
u-free-supported) explain why: the saving the plan hoped for is a quotient
phenomenon, not a support phenomenon.

**By-products.** `i_det = i_pad = 0` at every reachable cell, both primes
(`mult_X = a − nullity([E; ev_X])`, the s45 pairing) — consistent with the empty
record at `ℓ ≤ 6`, demonstrating the by-product computation and the Lemma-L
monotonicity of `i_X` (non-decreasing up the ladder, here constant at 0). No `D`
is reported. The LMR by-products `i_pad(12)`, `i_det(12)` are gated on the seed
(Part A) and were not attempted (sized only).

**nnz–|Stab| fit** (`results/s68_seed_sizing.json`), used in §2:

| `\|Stab\|` | 1 | 1 | 1 | 2 | 6 | 6 | 24 | 48 |
|---|---|---|---|---|---|---|---|---|
| `nnz/n_χ` | 7.0 | 7.0 | 7.0 | 11.3 | 17.9 | 29.7 | 25.8 | 48.4 |

`nnz/n_χ` rises with `|Stab|` (`≈ |Stab|` at the large end), so the reduced
matrix at the seed (`|Stab| = 10080`) has `nnz` of order `N_S`, the input to §2.

---

## 5. Pre-registration scorecard

| # | pre-registered | outcome |
|---|---|---|
| A-wall (0.9) | seed exceeds container on build and/or solve by the projected margins | **confirmed**: build 2.47 TB (353×), solve ≈ 90–310 yr/prime (≳ 10⁴×); each ≥ 100×, robust to the nnz constant |
| A: sizing reproduces | `N_S = 51,446,325,457`, `\|Stab\| = 10080`, `n_χ~ = 5.10e6` | **confirmed** exactly (`a = 2` adopted from s57/s63, not re-derived here) |
| A: streaming insufficient | `nnz/n_χ ≈ c·\|Stab\|` ⟹ reduced matrix stays TB-scale | **confirmed on the fit** (`nnz/n_χ ≈ \|Stab\|`, `nnz ≈ N_S`); extrapolated from `\|Stab\| ≤ 48` |
| B-pass (0.9) | three-part certificate at every reachable rung; `span(J ⊕ B) = ker E` | **confirmed** on L1 and L2, both primes, seed from scratch, chained end-to-end (V2) |
| B: births exact | recovered birth `= a_δ − a_{δ−1}` | **confirmed**: L1 `8,7,4`; L2 `2,2,1,0` (V1 cross-check, 9/9) |
| C: support density | measure it on this family | **measured**: HWV support `0.91–1.00` (dense); u-free fraction `69%→3%`; **stopping-rule-2 direction** — support restriction does not do the work |
| C: by-products | `i_det`, `i_pad` where reachable | **measured** `= 0` everywhere (both primes); LMR gated, sized only |

Two things were established during the session and are flagged as such: the exact
sequence `0 → J(M_{δ−1}) → M_δ → π(M_δ) → 0` and the negative
`ker(E|_{u-free}) = 0` (§4) were measured after the pre-registration; both are
checked at every L1 rung and neither is load-bearing for the A/B verdicts.

---

## 6. Honest boundary

- **The LMR seed and every LMR rung are unbuilt.** Part B is validated at `ℓ = 4`,
  not at the LMR cell; the claim proved is that the *construction* is correct and
  exact, not that it runs at LMR scale (it does not — Part A).
- **Support density is family- and degree-dependent.** The `0.91–1.00` is measured
  on `ℓ = 4` tails `(6,4,2)`, `(4,4,2)` at `δ ≤ 8`; the LMR family (`ℓ = 9`, tail
  `(17,2⁷)`) is not measurable in-container, and the density does not extrapolate
  (it is uniformly high here but that is one family). What *is* family-independent
  is the structural reason the deflation needs the carrier — the exact sequence
  `0 → J(M_{δ−1}) → M_δ → π(M_δ) → 0` with births dense and represented in the
  u-free part only as a quotient, not as u-free-supported kernel vectors.
- **The solve-cost constant is extrapolated.** `10.6×10⁻⁹ s / (n_χ·nnz)` and
  `nnz ≈ 3.5 N_S` are s45's measured laws; the `nnz/n_χ ≈ |Stab|` fit extrapolates
  from `|Stab| ≤ 48` to `10080`. Every plausible constant leaves both seed walls
  ≥ 100×; the qualitative verdict is robust, the exact year-count is not.
- **No obstruction.** No rank drop was sought or found at `n = 4`; `i_det = i_pad
  = 0` throughout. The one theorem-guaranteed `i_det > 0` cell (LMR) is exactly
  the one that is out of reach.
- **Certificate soundness.** The completeness check is done over F_p at both house
  primes, not symbolically over `Q`; because rank only drops mod p and the observed
  nullity equals the exact `a_of`, the mod-p kernel faithfully carries `ker_Q E_δ`,
  so the check is sound in the binding direction. At validation scale
  `E·B_δ = 0` is automatic (`B_δ ⊆ ker[E;R]`), so condition (iii)'s operative
  content is the span equality; its LMR-scale content ("target rows outside the
  current support") is untested because the cells are unbuilt.
- **`a` at the reachable cells is proved over `Q`** (two primes agree and the
  independent plethysm `a_of` agrees, 9/9, `results/s68_vcheck.json` V1); the seed
  artefact is exact over `Z`.
- **Adversarial audit folded in.** A subagent audit confirmed no logic bug and
  reproduced the seed arithmetic, the exact-`Z` seed and all nine `a`; it flagged
  report-level over-claims (an nnz/solve numeric inconsistency, "over Q" where it
  is two primes, the `a_of`/π-injectivity checks needing a delivered artefact, and
  a false "density → 1" trend). All are corrected above, and the `a_of`,
  chained-climb and π-injectivity checks are now backed by `results/s68_vcheck.json`.

---

## 7. Notes for the integrator

1. **The seed is the wall, not the top of the ladder.** s63 walled `δ = 24`; this
   session walls `δ = 12`, the cheapest rung, on both build and solve. The ladder
   cannot be started in a 7 GB / 2-core container, and the seed is *structurally*
   the hardest rung (no predecessor ⟹ no transport ⟹ no u-free saving), so no
   amount of rung cleverness reaches it. A machine with `≳ 10 TB` RAM would clear
   the build wall; the solve wall (`~300 yr / prime`) needs a different algorithm,
   not a bigger box.
2. **Streaming orbit-reps is not enough (measured).** `nnz ≈ N_S` for the *reduced*
   matrix (`nnz/n_χ ≈ |Stab|`), so the s63 streaming opening removes only the
   monomial array; the matrix and the solve stay out of reach. A genuine opening
   needs both streaming *and* a structurally cheaper solve.
3. **The u-free part is a quotient, not a subspace of the kernel.** The exact
   sequence `0 → J(M_{δ−1}) → M_δ → π(M_δ) → 0` holds (verified), but
   `ker(E|_{u-free}) = 0`: births cannot be read off a u-free sub-solve, so the
   plan's "restrict the raising system to a complement of `J(M_{δ−1})`" must mean
   the generic-complement solve `ker[E;R]` (full carrier), not a column
   restriction. If a future plan wants a genuine per-rung saving it needs a way to
   compute the *quotient* `M_δ / J(M_{δ−1})` without the full `E_δ` — an open
   problem this session did not solve.
4. **The algorithm is banked and reusable.** `analysis/wk11_s68_ladder.py`
   (transport, deflation, three-part certificate, support and by-product
   measurements) is validated at `ℓ = 4` and is the tool a larger machine would
   run at LMR scale; the seed artefact format matches s63's `.npz`.
5. **Not touched:** `paper/*.tex`, `PROJECT_NOTES.md`, `docs/boundary_deficit.html`.
