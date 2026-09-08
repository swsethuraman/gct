# Session 73 (batch 11, C6) — the decision table, and the `D`-ladder at `n = 3`

Branch `s73-dladder` off `main` at `226b4ef1` (ancestry gate passed on a fresh
clone).  Pre-registration `results/PREREG_s73.md` at `bc7a3b0`, committed
before any cell was built.  Container only, no pushes; delivery by
`s73_decision.bundle` + `.md5`.  Labels: **proved** / **measured** /
**adopted** / **expectation**.  Mode: **B** (the default); the Mode A gate is
recorded in §9.

**Missing inputs, recorded up front.**  The brief's `docs/batch11_worker_preamble.md`,
`docs/batch11_plan.md`, `docs/s65_prompt.md`, `docs/stocktake_batch10.md`,
`analysis/wk11_int_p0a.py`, `results/wk11_int_p0a.json`,
`analysis/wk10_s63_n3control.py`, the `19_7_2_2_2_2_2_d12_n3_permanent_*`
certificates and the `n ∈ {3,4}` verifier exist neither at `226b4ef1`, nor in
any branch of the public repository, nor in the integrator tree on the laptop
(`Projects/gct/work`, also at `226b4ef1`); the s63 bundle is not in
`Projects/gct` either.  The s62, s64 and s66 bundles were fetched from the
laptop (`refs/bundles/*`), and session 62's independent `n = 3` control
(`analysis/wk10_s62_n3.py`, `results/s62_n3_*.json`) is the anchor this
session reproduces.  The verifier extension (§7) was therefore made here,
minimally, and is flagged for reconciliation.

## 0. Verdict

> **The obstruction persists, and it persists for a reason that is a theorem,
> not a measurement.**  On the `n = 3` ladder `λ_δ = (3δ − 17, 7, 2^5)` the
> ambient multiplicity is `a(δ) = 0, 2, 4, 5` at `δ = 8, 9, 10, 11` and
> **`a(δ) = 6` for every `δ ≥ 12`** (two independent plethysm engines at
> `δ = 8 … 40`, and the stable value `a_∞((7,2^5)) = 6` by a third, from-scratch
> computation; Proposition S makes `a(δ) = a_∞` for `δ ≥ 17` and Lemma L makes
> the ladder monotone, so it is flat from 12 on).  Lemma L then forces
> `i_det(δ) = i_det(12) = 1` and `i_per(δ) = i_per(12) = 0` for every `δ ≥ 12`:
>
>     D(δ) = i_det(δ) − i_per(δ) = +1   for all δ ≥ 12,      D = 0 at δ = 9, 10, 11.
>
> The brief's three cases were `1,1,1,…` / `1,0,0,…` / `1,2,…`; the first holds,
> and the ladder carries **exactly one** ideal highest-weight vector at every
> rung — the LMR vector born at `δ = 12`, transported by `c_{(3,0,…,0)}` — and
> **no** highest-weight vector of `I(P_7)` at any rung.  Every rung is a
> multiplicity obstruction (both multiplicities nonzero), and the orientation
> is one-sided: `U_D ⊄ U_P` (an equation of `D_7` that does not vanish on
> `P_7`, exhibited over `Z`), `U_P = 0`.
>
> **The rungs were measured anyway, and they agree with the theorem at every
> point** — `δ = 12, 13, 14, 15, 16` directly at both house primes on fresh evaluation
> families, the transported vector reproduced by an independent build at each
> step, `δ = 9, 10, 11` on both sides, with certificates for every full-rank
> claim and every exhibited kernel vector (§4–§6).  A run whose answer is
> predicted is the sharpest instrument test available, and both engines
> (the cell builder at new degrees, and the transport between two independent
> builds) passed it.

## 1. Objects and conventions

`n = 3`, `r = ℓ(λ) = 7`.  `D_7 = closure{det_3(Σ s_i A_i)}` and
`P_7 = closure{per_3(Σ s_i A_i)}` in `Sym^3 C^7`, `A_i ∈ C^{3×3}` — the
`7`-pencil slices of the `GL_9` orbit closures of `det_3` and `per_3`
in `Sym^3 C^9`; by the programme's (★) reduction the `λ`-isotypic part of
`C[GL_9·f]` is that of `C[X_7]` for `ℓ(λ) ≤ 7`.  For a rung `(λ_δ, δ)`:
`a` = multiplicity of `S_λ(C^7)` in `Sym^δ(Sym^3 C^7)`; `HWV_λ` the `a`-dimensional
space of highest-weight vectors; `U_D = HWV_λ ∩ I(D_7)`, `U_P = HWV_λ ∩ I(P_7)`;
`i_X = dim U_X`, `mult_X = a − i_X`;

    D = i_det − i_per = mult_per − mult_det.

`P_7 ⊆ D_7 ⟹ I(D_7) ⊆ I(P_7) ⟹ U_D ⊆ U_P ⟹ D ≤ 0` (the functorial direction,
`docs/brief_wording.md` §7); `D > 0` refutes the containment, and so does the
finer `U_D ⊄ U_P`.  Both multiplicities are nonzero at every rung with `a > 0`
(`mult_det ≥ 5`, `mult_per = a`), so every `D > 0` here is a **multiplicity
obstruction**, not an occurrence obstruction.  The refutation itself is not
news (`dim P_7 = 59 > 47 = dim D_7`); the certificate is.

Coordinates: the `χ_λ`-isotypic reduction `V_χ` of the weight-`λ` monomial
space (`docs/stabiliser_reduction.md`; `|Stab_W(λ)| = 5! = 120` on the five
equal parts), `E` the stacked simple raising operators on `V_χ`
(`analysis/wk9_s45_build.build_cell`, `n = 3`), so `HWV_λ = ker E`;
`mult_X = a − nullity[E; ev_X]` (Lemma 1 of `docs/sparse_det_route.md`) with
`ev_X` the pinned evaluation rows at `K = a + 8` integer pencils, the nullity
by the session-42/45 Wiedemann certificates at both house primes.  Kernel
vectors are reported in these `χ`-coordinates (coefficient of a monomial `m`
in the vector `v` is `v[col_of[m]]·sgn[m]`), the representatives of the
`n_χ` columns being banked per rung in `results/artefacts/s73_chi_basis_d<δ>.npz`.

## 2. The theorem: the ladder is flat from `δ = 12`, so `D = +1` persists

**(a) The `a`-ladder (proved: two independent engines, plus the stable value).**

    δ :   8   9  10  11  12  13  14  15  16  17  18  19  20 … 40
    a :   0   2   4   5   6   6   6   6   6   6   6   6   6 …  6

`tools/verify/pleth.py` (from-scratch box DP over weight multiplicities,
Weyl alternation) and `analysis/wk9_s42_census.a_weyl` (the house Kostant tail
DP) agree at every `δ = 8 … 20`; the house engine continues `6` through
`δ = 40` (`results/logs/s73_aladder.log`).  Independently, the stable value of
Proposition S at `n = 3` — the multiplicity of `S_{(7,2^5)}(C^6)` in
`Sym(Sym^2 C^6 ⊕ Sym^3 C^6)`, computed as `Σ_w sgn(w) K_∞(w(tail + ρ') − ρ')`
with `K_∞` the number of multisets of monomials of degree 2 or 3 in six
variables with a given exponent sum — is **`a_∞((7,2^5)) = 6`**
(`analysis/wk11_s73_ainf.py`).

**(b) Lemma L and Proposition S at `n = 3` (adopted from s57; the proofs
transfer verbatim).**  With `c = c_{(3,0,…,0)}` (the `s_1^3` coefficient, a
highest-weight vector of weight `(3,0,…,0)`), multiplication by `c` is
injective on `C[W]`, maps `I(X)` into `I(X)`, and is injective on `C[X]` for
every irreducible `GL_7`-stable cone `X ⊄ {c = 0}` — `D_7` and `P_7` qualify,
since `det_3(A_1) ≠ 0` and `per_3(A_1) ≠ 0` for a generic pencil.  Restricted
to highest-weight vectors:

    a(δ+1) ≥ a(δ),   mult_X(δ+1) ≥ mult_X(δ),   i_X(δ) ≤ i_X(δ+1) ≤ i_X(δ) + [a(δ+1) − a(δ)],

so **`a(δ+1) = a(δ)` forces `i_X(δ+1) = i_X(δ)` and `mult_X(δ+1) = mult_X(δ)`**.
Proposition S (dehomogenise at `c`; `Z = Sym^2 V'^* ⊕ Sym^3 V'^*`; a monomial
of tail weight `|tail| = 17` has at most 17 factors) gives `a(δ) ≤ a_∞` with
equality for `δ ≥ 17`.  Hence `6 = a(12) ≤ a(δ) ≤ a_∞ = 6` for `12 ≤ δ ≤ 17`
and `a(δ) = 6` beyond: flat from `δ = 12` on, in agreement with (a).

**(c) The anchors at `δ = 12` (this session, §4; s62/s63/P0-A).**
`i_det(12) ≥ 1` is LMR's theorem at this cell (adopted); `i_det(12) ≤ 1` is
the measured nullity `1` at both primes (`rank_p ≤ rank_Q`); `i_per(12) = 0`
is a nullity-`0` certificate at one prime, so **proved over `Q`** (at two
primes and two evaluation families here).

**(d) Consequence (proved, given (a)–(c)).**  For every `δ ≥ 12`:
`i_det(δ) = 1`, `mult_det(δ) = 5`, `i_per(δ) = 0`, `mult_per(δ) = 6`, `D(δ) = +1`,
`U_D(δ) = c^{δ−12}·U_D(12)` (a line: the transport is injective with equal
dimensions on both ends) and `U_P(δ) = 0`.  Downward, `i_per` is
non-decreasing and bounded by `i_per(12) = 0`, so `i_per(9) = i_per(10) = i_per(11) = 0`
(the det side there is `0` by s62/s63, re-read here at both primes).  So the
whole ladder reads

    δ     :  9  10  11  12  13  14  15 …
    i_det :  0   0   0   1   1   1   1 …
    i_per :  0   0   0   0   0   0   0 …
    D     :  0   0   0  +1  +1  +1  +1 …

and the highest-weight part of `I(D_7)` along this ladder is the single
transported line of the LMR vector; `I(P_7)` has no highest-weight vector of
any weight `(3δ − 17, 7, 2^5)`.

**(e) What this does and does not say.**  It says the `n = 3` LMR obstruction
is a *persistent family*, and that its persistence is the generic mechanism
of Lemma L, not a coincidence of degree 12; on this ladder nothing else is
ever born on either side.  It does not say anything about `D_7 ⊆ P_7`
(`U_P = 0` carries no information), nothing about other tails, and nothing
about `n = 4`, where the padded model changes the varieties (§8).

## 3. The instruments, and what each measurement proves

| step | instrument | status of the number it returns |
|---|---|---|
| `a` | `tools/verify/pleth.py` **and** `wk9_s42_census.a_weyl`, asserted equal at every rung | proved |
| build | `wk9_s45_build.build_cell(λ, δ, n=3)`: `N_S` weight-`λ` monomials → `V_χ` (`n_χ` columns), `E` (`nrows_E × n_χ`) | validated by s62 at `n = 3` against the dense engine on small cells; the raising rule and the reduction are the house conventions (adopted) |
| `nullity_p [E; ev_X]` | `wk9_s45_cell.nullity_stacked` (Wiedemann, levels `(12,2)` then uncompressed, `ev` rows pinned), both house primes on the two cores | `0` at one prime ⟹ `mult_X = a` over `Q` (**proved**, Lemma 2); `k > 0` ⟹ `mult_X ≥ a − k` proved, `= a − k` **measured** at each prime |
| kernel vectors | rational reconstruction from `P1`; `E v = 0` over `Z`; reduction mod `P2` lies in the `P2` kernel; exact evaluation over `Z` at 12 fresh pencils of the same family (must vanish), 12 of the other family and 4 generic cubics (must not) | an exhibited element of `I(X)^{HWV}` over `Z` (finite-point vanishing is Schwartz–Zippel evidence; the rigorous `v ∈ I(D_7)` at `δ = 12` is LMR, and at `δ > 12` it is Lemma L applied to the `δ = 12` vector) |
| `M_δ = ker E` | the full-`E` nullity solve at `δ = 12` (`P1`), six kernel vectors, count closed by a nonsingularity certificate with six pinned rows | `nullity_p(E) = 6 = a` (**measured**, equal to the plethysm value: stopping rule R3 not triggered) |
| transport `J` | multiply every monomial by `c_{(3,0,…,0)}` at the monomial level and contract to the next rung's `χ`-coordinates (`wk11_s73_lib.transport`); checked by `E_{δ+1} J(v) = 0` (mod `p` for bases, over `Z` for the integer lines) and by rank | proved per instance |
| `dim(U_D ∩ U_P)` | `dim U_D + dim U_P − rank[U_D; U_P]` mod each prime | measured (trivial here: `U_P = 0`) |

Seeds (pre-registered): pencils `random.Random(20260908)` (det) and
`random.Random(20260908 + 1000)` (per), entries in `[−40, 40]`, `K = a + 8`;
the verification-protocol family `+2000 / +3000` with `K = a + 20`; fresh
integer pencils for the over-`Z` checks `+4000 / +5000 / +6000`; Wiedemann
`seed0 = 1`.  The P0-A / s62 / s63 runs used `seed = 11`, so every evaluation
family here is independent of the banked ones.

## 4. The rungs, measured — the `D`-ladder and the decision table

Full table with wall times and the transport column: `results/s73_dladder.md`
(rendered from `results/s73_dladder.jsonl`, one record per rung).  Every rung
below was measured at **both** house primes on the pre-registered fresh
evaluation families (`K = a + 8` pencils, entries in `[−40, 40]`), and the two
primes agree everywhere (stopping rule R2 never triggered).

| δ | λ | a | `N_S` | `n_χ` | `i_det` | `mult_det` | `i_per` | `mult_per` | `D` | `dim(U_D ∩ U_P)` | orientation |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 9 | `(10,7,2^5)` | 2 | 809 508 | 11 425 | 0 (proved) | 2 | 0 (proved) | 2 | 0 | 0 | `U_D = U_P = 0` |
| 10 | `(13,7,2^5)` | 4 | 1 017 919 | 14 598 | 0 (proved) | 4 | 0 (proved) | 4 | 0 | 0 | `U_D = U_P = 0` |
| 11 | `(16,7,2^5)` | 5 | 1 118 518 | 16 318 | 0 (proved) | 5 | 0 (proved) | 5 | 0 | 0 | `U_D = U_P = 0` |
| **12** | `(19,7,2^5)` | 6 | 1 155 302 | 17 047 | **1** (measured; `≥ 1` LMR) | 5 | **0** (proved) | 6 | **+1** | 0 | `U_D ⊄ U_P`, `U_P = 0` |
| **13** | `(22,7,2^5)` | 6 | 1 165 249 | 17 306 | **1** | 5 | **0** (proved) | 6 | **+1** | 0 | `U_D ⊄ U_P`, `U_P = 0` |
| **14** | `(25,7,2^5)` | 6 | 1 167 156 | 17 379 | **1** | 5 | **0** (proved) | 6 | **+1** | 0 | `U_D ⊄ U_P`, `U_P = 0` |
| **15** | `(28,7,2^5)` | 6 | 1 167 408 | 17 399 | **1** | 5 | **0** (proved) | 6 | **+1** | 0 | `U_D ⊄ U_P`, `U_P = 0` |
| **16** | `(31,7,2^5)` | 6 | 1 167 429 | 17 403 | **1** | 5 | **0** (proved) | 6 | **+1** | 0 | `U_D ⊄ U_P`, `U_P = 0` |
| `≥ 17` | `(3δ−17,7,2^5)` | 6 | — | — | 1 | 5 | 0 | 6 | +1 | 0 | by Lemma L (§2) |

`i_det = 1` at `δ = 12, 13, 14, 15, 16` is the nullity `1` of `[E; ev_det]` at both
primes with the kernel vector exhibited over `Z` (a lower bound `mult_det ≥ 5`
proved, `= 5` measured; `i_det ≥ 1` proved by LMR at 12 and by transport
above).  `i_per = 0` is a nullity-`0` certificate at each prime: `mult_per = a`
**proved over `Q`** at every rung.

**The decision table (session 65's three outcomes, applied at each rung with
`i_det` measured, not assumed):**

| case | condition | reading | at `δ = 12, 13, 14` |
|---|---|---|---|
| (i) | `i_per < i_det` | `D > 0`: multiplicity obstruction; `P_7 ⊄ D_7` re-certified by this cell | **this case** at 12, 13, 14, 15, 16: `D = +1`, both primes |
| (ii) | `i_per = i_det` | `D = 0`; the orientation decides: `U_D = U_P` (silent) or `U_D ≠ U_P` (an equation each way) | — |
| (iii) | `i_per > i_det` | `D < 0`; `U_P ⊄ U_D` would refute `D_7 ⊆ P_7` | — |

At `δ = 9, 10, 11` both kernels vanish (`D = 0`, case (ii) with `U_D = U_P = 0`,
silent).  The orientation at every `δ ≥ 12` is one-sided: `U_D` is the LMR
line, which does not vanish at per pencils (exhibited exactly over `Z`: the
values at the 12 fresh integer per pencils are nonzero 50–58-digit integers,
`results/s73_crosscheck.json`), so `U_D ⊄ U_P`; and `U_P = 0`, so
`U_P ⊆ U_D` holds vacuously and the ladder says nothing about `D_7 ⊆ P_7`.

**`i_pad`.**  The brief asks for `i_pad` on the same source.  At `n = 3` the
padded model is `x_0·per_2` in `Sym^3 C^5`, concise in five variables, so
`P^{pad}_7 ⊆ Sub_5` and every weight of length `7 > 5` has `mult_pad = 0`,
`i_pad = a`: **proved** (the washout), `i_pad = 6` at every rung from 12 on,
`U_pad = HWV_λ ⊇ U_D`.  It was not measured separately (a nullity-`a` solve
would only re-derive `M_δ`, which the full-`E` solve did at 12).  As
`docs/stocktake_batch10.md` §6 says, the padded `n = 3` cell can never carry
an obstruction; the unpadded comparison is the one with content.

**Cost.**  Build 280–350 s per rung (`N_S ≈ 1.16·10^6`, `|Stab| = 120`,
`n_χ` from 17 047 to 17 379; the ladder's `n_χ` saturates because the added
weight goes into `c_{(3,0,…,0)}` factors), one stacked Wiedemann sequence
150–190 s at level `(12,2)` (`≈ 1.0·10^5` rows), two sequences per positive
nullity; a rung with both sides at both primes is 27–30 min on the two cores.
The full-`E` solves (needed at 9–12 for the explicit bases) run on the
uncompressed matrix (`5–7·10^5` rows: the `(12,2)` sample of `E` alone has a
spurious kernel at every rung, caught by the full-matrix check and escalated as
designed) at 400–800 s per sequence, `a + 1` sequences each — 93 min at 12.
Whole session: ten rung runs (nine rungs plus the second family at 12),
`≈ 7` core-hours, peak resident under 1 GB.

## 5. Transport: the same line on both engines

`J = ·c_{(3,0,…,0)}` is implemented at the monomial level (multiply every
monomial by the `s_1^3` coefficient functional, look the product up in the
next rung's weight-`λ` basis, contract to its `χ`-coordinates), so it uses
nothing from the Wiedemann side and is applied to the vectors of one build and
checked against the operators of the other (`analysis/wk11_s73_transport.py`;
records in `results/s73_transport.jsonl`).

| step | what was transported | checks |
|---|---|---|
| `11 → 12` | (from the explicit `M_12`) `dim J(M_11) = 5`, birth `1` | rank of `M_12` on the 729 `u`-free columns is **1** `= a(12) − a(11)` (the `u`-free part is the cokernel of `J`), so `dim J(M_11) = 5`; the LMR vector has **nonzero `u`-free part** (54 of the 729 columns): it is **born at 12**, not transported from 11 — consistent with `i_det(11) = 0` |
| `12 → 13` | the six basis vectors of `M_12` and the integer line `v_12` | all six `J(v)` are highest-weight at 13 (`E_13 J(v) = 0` mod `P1`), rank 6 = `a(12)` (injective), and since `a(13) = 6`, `M_13 = J(M_12)`: **birth `0` at 13**; `E_13 J(v_12) = 0` over `Z`; `J(v_12) = ± v_13` **exactly over `Z`** (primitive vectors equal), `U_D(13) = J(U_D(12))` mod both primes |
| `13 → 14` | the integer line `v_13` | `E_14 J(v_13) = 0` over `Z`; `J(v_13) = ± v_14` exactly over `Z`; `U_D(14) = J(U_D(13))` mod both primes |
| `12 (s62) → 13 (s73)` | session 62's exhibited integer vector | `E_13 J(v_62) = 0` over `Z` and `J(v_62) = ± v_13`: two sessions, two drivers, two evaluation families, one line |
| `9 → 10 → 11 → 12` | the explicit bases `M_9, M_10, M_11, M_12` (full-`E` solves at every rung `≤ 12`, nullities `2, 4, 5, 6 = a`) | `J(M_9) ⊆ M_10` with rank 2 (birth 2), `J(M_10) ⊆ M_11` with rank 4 (birth 1), `J(M_11) ⊆ M_12` with rank 5 (birth 1: the LMR direction); at every step the `u`-free rank of the upper basis equals the birth dimension (`2, 1, 1`), i.e. the increment `a(δ) − a(δ−1)` — the cokernel of `J` is exactly the `u`-free part, as the integrator's note on the 274th LMR vector (`6d92c60`) says it must be |

So the direct Wiedemann measurement at each new rung and the transport of the
previous rung's vector produce the **same integer vector** — support 3900 of
`n_χ`, largest coefficient 544 at every rung, because `J` preserves both — and
the cross-session comparison with s62 closes the loop on the `δ = 12` line
(`results/s73_crosscheck.json`).  P3, P4 and P5 of the pre-registration hold.

## 6. The verification protocol for `D > 0` (run in full at `δ = 12`, and at 13, 14)

1. **Second prime.**  Both house primes at every rung; nullities agree.
2. **Independent evaluation family.**  The pre-registered seeds are new
   (`20260908 (+1000)`), independent of s62/s63/P0-A (`seed = 11`); the
   verifier's fresh points are a third family (`seed 20260908`, box `1000`);
   and the pre-registered second family (`seeds +2000 / +3000`, `K = a + 20 = 26`
   pencils) was run at `δ = 12`: nullity `1` (det) and `0` (per) at both
   primes again, and its reconstructed integer vector **equals the primary
   one up to sign** (`results/s73_crosscheck.json`).
3. **Characteristic zero.**  The kernel vector is rationally reconstructed to
   an integer vector (support 3900, largest coefficient 544), `E v = 0` holds
   over `Z`, `v mod P2` lies in the `P2` kernel, `v` vanishes exactly at 12
   fresh integer det pencils and is nonzero at 12 fresh per pencils and 4
   generic cubics.  `i_per = 0` needs no such step: a nullity-`0` certificate
   at one prime is a proof over `Q`.
4. **Independent source.**  `tools/verify` re-derives the vector's properties
   with its own raising operators over `Z` and its own forms (nothing imported
   from `analysis/`): PASS at 12, 13, 14 (§7).  The `δ = 13, 14` vectors were
   obtained two ways (direct measurement on an independent build, transport).
5. **Degeneracy pre-check** (`brief_wording.md` §5/§7).  The statistic is the
   coordinate-ring multiplicity — functorial in the right direction (row 1 of
   the §7 table), so `D > 0` refutes containment by the surjection
   `C[D] ↠ C[P]` and needs no further "why".  The direction agrees with the
   known `dim P_7 = 59 > 47 = dim D_7`.  The evaluation family is the unpadded
   `per_3` pencil, which *is* the generic point of the `GL_9` orbit closure of
   `per_3` restricted to seven variables (no padding, no length reduction of
   some other form): the concern of §5 (accidental vanishing manufactured by a
   restriction) does not arise, and the exhibited vector is in any case
   **nonvanishing** there — the failure mode §5 guards against is a false
   vanishing, and the per side shows none.

Nothing in the protocol changed a number.

## 7. Certificates and the verifier

`results/certs/s73/` — 46 files in `gct-cert/1`, **46 PASS, 0 FAIL** under `tools/verify`
(`results/logs/s73_verify_all.md`):

| file | kind | what it certifies |
|---|---|---|
| `s73_<λ>_d<δ>_n3_det_kernel_vec0_int.json.gz` (δ = 12, 13, 14; 240 510 terms, 1.45 MB each) | `hwv`, integer | the LMR line: annihilated by every `E_{i,i+1}` over `Z`; vanishes at the 14 recorded det pencils and 6 fresh ones; nonzero (rank 1) at the 14 recorded per pencils, 6 fresh per pencils and 6 generic cubics — an equation of `D_7` not vanishing on `P_7`, checked from scratch |
| `s73_<λ>_d<δ>_n3_det_p<p>_sparse_nullity.json` (δ = 12, 13, 14; both primes) | `sparse_nullity` | `nullity_p[E; ev_det] = 1`: the closing Berlekamp–Massey record (degree `n_χ`, `f(0) ≠ 0`, one pinned row) and the companion `hwv` certificate |
| `s73_<λ>_d<δ>_n3_permanent_p<p>_sparse_nullity.json` (δ = 12, 13, 14; both primes) | `sparse_nullity` | `nullity_p[E; ev_per] = 0`: `mult_per = a` over `Q` (modulo re-running the recorded sequence) |
| `s73_19_7_2_2_2_2_2_d12_n3_fullE_p2147483647_sparse_nullity.json` | `sparse_nullity`, variety `none` | `nullity_p(E) = 6 = a` at 12 (the explicit basis is the artefact `s73_M_basis_d12_p1.npz`) |
| `s73_<λ>_d<δ>_n3_{det,permanent}_p<p>_sparse_nullity.json` (δ = 9, 10, 11; both primes) | `sparse_nullity` | both sides full rank: `mult_det = mult_per = a` over `Q` at the three rungs below the LMR degree |
| `s73_<λ>_d<δ>_n3_det_kernel_vec0_int.json.gz` and the four `sparse_nullity` files (δ = 15, 16) | `hwv`, `sparse_nullity` | the same at rungs 15 and 16 |
| `s73_<λ>_d<δ>_n3_fullE_p2147483647_sparse_nullity.json` (δ = 9, 10, 11) | `sparse_nullity`, variety `none` | `nullity_p(E) = a` (2, 4, 5); bases banked as artefacts |
| `s73_19_7_2_2_2_2_2_second_d12_n3_*` (5 files) | `hwv`, `sparse_nullity` | the verification-protocol family at 12 (`K = 26`): the same nullities, the same integer vector |

**The verifier extension (flagged for reconciliation).**  The brief says the
verifier "now accepts `n ∈ {3,4}` and has a `permanent` point family"; that
version was not reachable, so `tools/verify` was extended here, minimally:
`n ∈ {3,4}` in `check_cell` and all forms of degree `n`; a `permanent_pencil`
point type (`per_n(Σ s_i A_i)`, `n×n` integer matrices, appended to `FAMILIES`
so the older fresh-point seed offsets are unchanged); `det_pencil` with `n×n`
matrices; and the `sparse_nullity` kind (documented in `FORMAT.md`: cell,
points by substitution data, reduction sizes, the closing Berlekamp–Massey
record, the claim, companion `hwv` files; the verifier states in its own
report line that it does **not** re-run the `χ`-build or the Wiedemann
sequence).  The self-test and all 59 pre-existing certificates still pass.  If
the integrator's version names the family differently (`permanent` vs
`permanent_pencil`) the certificates here need a one-word rename and nothing
else.

## 8. Honest boundary

- **What is proved and by what.**  `a(δ) = 6` for `δ ≥ 12`: two engines to
  20, the house engine to 40, the stable value `a_∞ = 6` from scratch, and
  Proposition S for the tail (proved at `n = 4` in s57; the proof is
  degree-generic, adopted at `n = 3`).  `i_per(δ) = 0` for all `δ ≥ 9`:
  one-sided certificates at 9–16 and Lemma L beyond (given `a` flat).
  `i_det(δ) = 1` for `δ ≥ 12`: `≥ 1` is LMR at 12 and transport above;
  `≤ 1` is the measured nullity at 12 (`rank_p ≤ rank_Q`) and Lemma L.
  `D = +1` for every `δ ≥ 12` therefore rests on: LMR (literature), Lemma L
  and Proposition S (s57, proofs re-read here), two plethysm engines, and the
  `δ = 12` nullity certificates of this session (and s62/s63/P0-A).
- **What is measured, not proved.**  That the exhibited integer vector lies in
  `I(D_7)` is Schwartz–Zippel evidence (32 det pencils across the producer and
  the verifier, exact over `Z`); the rigorous statement is LMR's.  That the
  nullity of `[E; ev_det]` is exactly `1` at each prime is closed by a
  Berlekamp–Massey nonsingularity certificate with one pinned row — the
  standard one-sided certificate, re-runnable but not re-run by the verifier.
- **Independence of the source basis.**  Every session so far (62, 63, P0-A,
  73) builds `V_χ` and `E` with `wk9_s45_build`.  The from-scratch check of
  the kernel vector by `tools/verify` (its own raising operators on the
  monomial basis, no `χ`-reduction) is independent of that build for the
  *positive* claims; the *full-rank* claims (`i_per = 0`) still rest on the
  build's `E` (validated by s62 at `n = 3` on small cells against the dense
  engine, and here by `nullity(E) = a` at 9, 10, 11 and 12, with the bases
  transporting into each other exactly as Lemma L requires).  A
  fully independent full-rank certificate would need an explicit
  highest-weight basis in monomial terms (`full_rank` with `basis`), which at
  `n_χ ≈ 17 000` and `N_S ≈ 1.2·10^6` does not fit the 5 MB rule.
- **What the ladder does not say.**  Nothing about `D_7 ⊆ P_7`; nothing about
  other tails at `n = 3` (the LMR cell is still the only `n = 3` cell with
  `i_det > 0` in the record); nothing about `n = 4`, where the comparison is
  with the *padded* `per_3` and a different mechanism (the `ℓ ≤ 10`
  washout, the LMR cell at `δ = 24`) governs — the persistence mechanism here
  (a flat `a`-ladder) is however exactly the s57 regularity that the LMR cell
  is the first stable cell of its ladder, which s57 measured at `n = 4` for
  `k = 3..6`, so the same conclusion `D(δ) = D(24)` for all `δ ≥ 24` holds
  on the `n = 4` LMR ladder once `D(24)` is known: the `n = 4` question is
  one cell, not a ladder.
- **The `a + 8` points, the seeds and the levels** are the house conventions;
  a degenerate draw can only lower a measured rank (a false positive nullity),
  and the positive nullities here are confirmed at two primes, two families
  (three with the verifier's), two sessions and by transport.

## 9. Mode A checkpoint

Pre-registered checkpoint 2026-09-08 04:30 UTC.  At the checkpoint the
session's link to the laptop was down (it had been down since about 02:00 UTC,
with brief reconnections at 04:08 and later that did not survive a call), so
`Projects/gct` could not be listed for an s68/s69/S5 bundle; nothing carrying
an LMR source basis was delivered into the conversation either.  As
pre-registered, the session stayed in **Mode B** and did not wait.  The Mode A
tasks (`i_det`, `i_pad`, `i_{per_4}` at LMR from a source, `U_D`, `U_P`, the
three-outcome table at LMR) remain exactly session 65's, unchanged; the one
structural remark this session adds to them is in §8: by the same Lemma-L
argument, once `D(24)` is known on the `n = 4` LMR ladder it is known at every
`δ ≥ 24` (s57 measured that the LMR cell is the first stable cell of its
ladder), so Mode A is one cell, not a ladder.

## 10. Deliverables

- `results/PREREG_s73.md` (`bc7a3b0`, before any build);
- `docs/s73_report.md` (this), `docs/session_73.md` (project note);
- `results/s73_dladder.md` + `.jsonl` (one record per rung), `results/s73_transport.jsonl`,
  `results/s73_aladder.json`, `results/s73_crosscheck.json`;
- artefacts `results/artefacts/`: `s73_chi_basis_d<δ>.npz` (the `χ`-column
  representatives and signs, the `u`-free columns), `s73_kernels_d<δ>_primary.json.gz`
  (`U_D`, `U_P` mod both primes and over `Z`, with the pencils), `s73_M_basis_d<δ>_p1.npz`
  (explicit highest-weight bases mod `P1` at δ = 9, 10, 11, 12);
- certificates `results/certs/s73/` (§7) and the verifier report `results/logs/s73_verify_all.md`;
- code `analysis/wk11_s73_{lib,cell,transport,certs,table,crosscheck,ainf}.py`;
  logs `results/logs/s73_*.log`;
- `tools/verify` extended (§7), `FORMAT.md` updated;
- bundle `s73_decision.bundle` + `.md5` (single ref `s73-dladder`).
