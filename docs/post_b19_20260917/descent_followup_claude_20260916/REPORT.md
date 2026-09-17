# Descent, transverse compatibility, and the coefficient algebra: consolidated review and one five-row diagnostic

Claude session, 16 September 2026. Fresh directory `work/descent_followup_claude_20260916/`
(did not exist before this session). Historical files read-only. Written incrementally;
the status line below is replaced at the end.

Status: **COMPLETE — inconclusive within budget on five-row arc exactness; certified partial results, repaired claims, one recommendation.** (This line replaced the IN PROGRESS marker after §F was written; the opening verdict of §0 stands as confirmed by §D.)

## 0. Opening verdict (written before computation; confirmed in §D)

Three inputs are reviewed here: the Astra descent/interpolation stream, the Astra
equal-quartic fibre stream, and the Claude coefficient-algebra note of 15 September.
What they establish, in plain terms, as far as this session can tell before its own
checks:

- **Six rows, `(6,(4^6))`.** An explicit full-stabilizer invariant `Q` of type `(2^6)` and
  its square `Q^2` of type `(4^6)` are exhibited; a two-pencil descent test
  `q(K) - 1120 q(L)` is globally necessary and is nonzero on `Q^2`. This removes one of
  nine false arc survivors; the clipped determinant bound stays `1`. The early
  cone-vertex projector reached the same rank-nine conclusion by *using* the known
  ambient line and is therefore not an independent mechanism. A fourth-order transverse
  condition with claimed witness value `-12` is reviewed in §A.4.
- **Five rows, fibre family.** At `(3,(4,2,2,2,2))`, `a = 0`, `s = 2`, a nonzero partial-
  transpose functional exists but the arc already has rank two, so the increment is zero;
  the 2+2 partial-transpose family is provably blind on every even five-row rectangle.
- **Coefficient algebra (Claude note).** The restriction bound is valid as a necessary
  condition, but the note overstated several things; corrections are in §B.
- **The one authorized diagnostic (§C):** `d = 5`, `lambda = (4^5)`, `s = 5`, `a = 1`,
  `m_det = 1`. Either the old arc is already exact there (rank four certified), or an
  exact arc-kernel vector is evaluated on the chat-only transverse map `C2`, or the
  session stops inconclusive within budget.

No positive gap is claimed anywhere in this document, and none can be: every cell
touched is a known no-gap cell.

## 1. Provenance and session state

Workspace `C:/Users/swami/Projects/gct-gpt`. No git command is run by this session in
any worktree; the output directory is outside every worktree and is not a git
repository. Process state at start: no `python` process was running (checked with
`tasklist`); the only live processes were editor/agent shells. The Astra directories
`work/extension_descent_20260916/` and `work/fiber_compatibility_20260916/` were last
written at 07:36 and 08:07 local time and carry PID records of finished runs; nothing
in them is active. No other session has written a five-row `(4^5)` transverse test:
no file in the workspace mentions `K5`, `112 z(K5+S)` or the values `52/21`, `301/21`
outside the assignment itself (checked by grep before this file was created).

Input pins (SHA-256) are listed in `MANIFEST.json` at the end; the two attachments
`ccc1abb3…` and `d4a38184…` are compared byte-wise with the two on-disk reports in
§A.0.

## 2. Resource rules adopted for this session

- Each numerical pilot: one process, one BLAS thread, 60 s wall, 512 MiB, through the
  existing Windows Job Object wrapper (located in §2.1; if it cannot be located, the
  fallback `timeout 60` with `OMP_NUM_THREADS=1` is used and **stated as not a memory
  cap**, per the assignment).
- Total numerical pilot budget: 10 minutes of measured wall time including failures.
  A running total is kept in §C.7.
- No census, no degree-six sweep, no ten-vector six-row carrier.

## 3. Test plan for §C (written before any computation)

Cell `d = 5`, `lambda = (4,4,4,4,4)`, conjugate heights `(5,5,5,5)`: four columns of
height five, twenty slots.

1. **Dimensions.** Recompute `s` and `g` from the Murnaghan–Nakayama formula of B18-02
   (§3.1 there) with the historical `s_and_g`; expected `s = 5`, `g = 6`. Recompute
   `a = 1` from the Weyl alternant (B19-02's `weyl_multiplicity`). Record inherited and
   recomputed values separately.
2. **Price before running.** Use `plan_only` (label-only contraction planning) for the
   epsilon-contraction carriers `q_{pi,rho} = P_{pi,rho} + P_{rho,pi}` with four
   height-five columns: maximum intermediate entries and flop units for random and
   local block partitions. Reject anything above `4^12` intermediate entries; if every
   plan is above the guard, the dense route stops there and only sparse-point
   evaluation is attempted.
3. **Carrier.** Build five vectors `q_1..q_5 in M_(4^5)` as symmetrised epsilon
   contractions (membership by construction: four full five-wedges give type `(4^5)`;
   five row-epsilons and five column-epsilons give `(det A det B)^5`; symmetrisation
   gives transposition invariance). Certify independence by a nonzero `5 x 5` modular
   evaluation minor at five explicit integer tuples. With `s = 5` this is a basis.
4. **Old arc, rank-four floor first.** Skew degree `j` runs to `lambda_1+lambda_2+lambda_3
   = 12`; forbidden degrees `j = 11, 12` (`2d + 1 = 11`). For each of two or more
   integer tuples and thirteen nodes `u = 0..12`, evaluate each `q_i` with the skew part
   scaled by `u`, interpolate exactly, and take the `u^11, u^12` coefficients. A nonzero
   `4 x 4` minor of the stacked forbidden rows certifies `rank C >= 4`. Since the
   extendable line `H5 ∘ phi` lies in `ker C`, `rank C <= 4`; so `rank C = 4` and the
   old arc is exact in this cell. **Stop there.**
5. **Otherwise** (no rank-four minor within budget): inconclusive unless an exact
   arc-kernel vector can be certified within the remaining cap, in which case `C2` is
   evaluated on it.
6. **Independent check of the `C2` derivation** (§C.2): verify `det(K5 + tS)`,
   `Delta^2(u^2) = 280`, `Delta^2 v = 48`, and the chain-rule constant `6/7`, and the
   even-degree-four structure of the restriction, before any use.

Stop conditions: any single pilot over 60 s or 512 MiB; running total over 10 minutes;
a dense plan over the guard with no sparse alternative.

## A. Review of the two Astra streams

Labels: **VERIFIED** = independently replayed or re-derived here; **PRODUCER-CERTIFIED** =
exhibited by the producer with a certificate this session inspected but did not replay;
**ADOPTED**; **CONDITIONAL**; **REJECTED**; **NOT REACHED**.

### A.0 Attachments versus reports

The attachments `ccc1abb3…` and `d4a38184…` are byte-identical to
`work/extension_descent_20260916/REPORT.md` and `work/fiber_compatibility_20260916/REPORT.md`
respectively after CRLF normalisation (`diff` empty; the SHA-256 values differ only by line
endings). The other three attachments (`e95184a7…` cone-vertex projector, `43761221…`
quadratic-square condition, `515d31fd…` fourth-order transverse condition) have **no
on-disk artifact**: no script, JSON or manifest in either Astra directory records the
`Omega det Q = 315/4` check, the `-12` witness, or the `175/36` contraction. Their claims
are chat-only and are labelled accordingly below.

### A.1 The explicit six-row witness and the two-pencil descent test

- **`Q in M_(2^6)`, `Q^2 in M_(4^6)` (membership).** The epsilon-contraction argument
  (two six-slot alternating columns give `det(g)^2` under mixing; three row and three
  column epsilons give `(det A det B)^3`; `pi <-> rho` under transpose) is correct.
  **VERIFIED (re-derived).**
- **Values `Q(K) = -86400`, `Q(L) = -720`, `H6(F_K) = 1290240`, `H6(F_L) = 1152`,
  ratio `1120`, descent minor `-7,930,773,504,000`.** Producer certificate
  `sixrow_witness.json` plus the producer's own second path `verify_witness.py`
  (direct epsilon products). This session **replayed `Q(K) = -86400` and
  `H6(F_K) = 1290240`** through the producer's evaluator in P9 (§C.6), which is an
  execution check of their code, not a third arithmetic path. **PRODUCER-CERTIFIED,
  execution replayed.**
- **Necessity of `C2(q) = q(K) - 1120 q(L)` on `E_(4^6)`.** Given `a = 1`
  (B19-01, MEASURED there; not recomputed here) every extendable vector is a multiple of
  `H6 ∘ phi_6`, and the two evaluations fix the ratio. **VERIFIED given `a = 1`.**
- **`C(Q^2) = 0`.** Silence criterion `lambda_1+lambda_2+lambda_3 = 12 = 2d`, B19-01
  Theorem 4.1, which is about `S_lambda W` and hence about the invariant source.
  **ADOPTED (PROVED in B19-01).**
- **Increment.** `rank[C; C2] = 0 + 1`. One false survivor removed; clipped bound stays
  `min(1, 9) = 1`. **VERIFIED as stated; no bound improvement, no gap.**
- **The early cone-vertex projector (`e95184a7…`)** defines `C2(z) = z - L(z) e` with
  `e` the *known* ambient line. It is circular as a discovery device (it needs `E` to
  define the map) but it is a correct statement that `ker = E` once `a = 1` and a nonzero
  ambient value are known. Its `F(q_*) = 175/36` is the `5!`-scaled four-epsilon contraction
  in the `T' = c_alpha alpha!/24` convention (the same convention issue is measured
  exactly in five variables in P3). **Kept distinct from the two-pencil test, as the
  assignment requires. The projector is REJECTED as an independent mechanism and
  ACCEPTED as a restatement.**

### A.2 The complete-carrier interpolation theorem

Statement reviewed: if `q_1..q_s` is a certified basis of `M_lambda` and the `s x s`
evaluation matrix `S_T` is invertible, then exact rational relations among the ambient
evaluation columns `A_T` are polynomial identities, so `ker T_lambda = ker A_T` over `Q`.
**VERIFIED as a theorem**, with the hypotheses exactly as the assignment states: (i)
membership of every `q_i` in `M_lambda` (by construction, epsilon contractions);
(ii) completeness, i.e. `rank = s` with `s` from the character formula; (iii) an *exact*
rational relation, not a modular zero or a sampled plateau. The bottleneck is (ii): §C
shows that in the smallest five-row rectangle the affordable contraction family reaches
rank 2 of 5 and that every cheap random contraction vanishes identically at five points.
**Carrier construction cost is the bottleneck, as the assignment anticipated; this session
measured it.**

The degree-six pilot `(12,8,2,1,1)`: 230-term ambient vector with exact zero raising
residues (four operators, target dimensions 927/493/556/730, nonzeros 3954/1776/1121/1121),
nonzero determinant value `-222,071,593,284,381,720`. **PRODUCER-CERTIFIED** with the
producer's independent verifier `verify_five_row.py`; not replayed here. It proves
`I(D45)_{6,(12,8,2,1,1)} = 0` and nothing about `D` there (no padding evidence).
`a = 1`, `s = 24` are inherited from the character census, not recomputed.

### A.3 The quadratic-square derivative control (`43761221…`)

- `Omega det Q = prod_{j=0}^5 (1 + j/2) = 315/4` in the half-off-diagonal normalisation:
  this is the symmetric Cayley identity (Caracciolo–Sokal–Sportiello, Theorem 2.2, arXiv:1105.6270)
  with `s = 1`. **ADOPTED (standard); not recomputed** — the 388-monomial check has no
  artifact.
- `C2(P) = -5040 P(K)` at `d = 3`: an `a = 0` control (three-row constituents only).
  **CONDITIONAL on the `(3,2,1)` exterior-Cauchy nonvanishing argument**, which was not
  checked here.
- The obstruction for `d = 6`: restriction to the quadratic-square family
  `Q -> u_Q^2` retains a single scalar `P(Y_*) (det Q / det Q_0)^2` from the ten-dimensional
  source, already filled by the extendable line. **VERIFIED (the covariance argument is
  correct):** no linear condition factoring through that family, of any jet order, sees
  the nine missing dimensions. Transverse information is required.

### A.5 The equal-quartic fibre test

- Whole transpose is `tau`-redundant; partial transpose of a `2+2` block pencil is a
  genuinely different point of the quotient (the nonzero difference proves the two tuples
  are not `H`-related). **VERIFIED.**
- `(3,(4,2,2,2,2))`: `g = s = 2` **VERIFIED** (P1 control, `s_and_g` gives `(2,2)`);
  `a = 0` by row count. Values `(-496, 224)`, `(816, -624)`, `C2 = (-720, 1440)`:
  **PRODUCER-CERTIFIED** (`exact_pair.json`, cross-checked by the producer's modular
  network in `verify.py`). Arc `2 x 2` minor `61631 mod 524287` **PRODUCER-CERTIFIED**;
  the direction (nonzero modular minor of actual forbidden coefficient rows is a
  characteristic-zero floor) is correct. Increment zero. **VERIFIED as a conclusion.**
- Rectangular obstruction: the odd-sector argument (HMSV Lemma 6.6: reflection-odd
  `SO_4` invariants of `Mat_2` have exactly four odd parts) plus the Pieri/Schur-lemma
  complement argument for `(m^5)`, `m` even. **VERIFIED (re-derived): `D_(4k)^5 = 0`
  on the full source.** The HMSV pointer itself was not fetched here.
- The filter is necessary, not sufficient. No new fibre pilot was run: no nonrectangular
  `a > 0` cell with a certified arc-kernel vector exists.
- **This blindness is about the `2+2` partial-transpose family only.** The `K5`
  transverse map of §C is a different map on the same source, and P7 shows it is nonzero
  on both certified vectors of `M_(4^5)`, so the two must not be conflated.

## B. Corrections to the Claude coefficient-algebra note (15 September)

The historical note `work/batch15_workers/B15-12/docs/b18_12_coefficient_algebra.md` is not
edited. The replacement statements below supersede it.

| # | Location in the note | Defect | Replacement statement |
|---|---|---|---|
| B1 | §3, Theorem 3.1 | Stated with "`u_L = a` for the whole pencil space"; the exact image multiplicity there is `m_det`, so substituting `a` only gives the trivial bound. Locus hypotheses vague. | **Theorem.** Let `L subset (Mat4)^5` be Zariski-closed, `G`- and `GL5`-stable, and homogeneous. Let `S = R^tau_{4d,lambda}^{hw}` (dim `s`), `rho_L = rank(S -> C[L])`, `u_L = mult_lambda C[closure(phi(L))]_d`. Then `m_det <= min(a, s - rho_L + u_L)`. Any certified floor `rho_0 <= rho_L` and any certified ceiling `u_0 >= u_L` give a valid bound. For `L` the whole space, `u_L = m_det` exactly. Proof: `A_{d,lambda} subset S`; `A|_L = phi^* C[phi(L)]_d`; dimension count. |
| B2 | §0 item 4, §5, §6 | Uses `u_0 = U` (the padding ceiling) for the `1+3` locus and reads the result as a possible gap route. | With `u_0 = U`: `min(a, s - rho_0 + U) >= U >= r` for every padding floor `r`, since `rho_0 <= s` and `U <= a`. **This version can never yield a gap.** It can still lower an ambient bound `a` when `rho_0 - U > s - a`, which is a determinant-side statement only. A gap through this route needs a strictly sharper image ceiling `u_0 < U - (s - rho_0)`. |
| B3 | §0 item 2, §3 "What this is" | Claims fibre-constant regular functions are the largest target containment "that uses only `A = pi^* C[D45]`", suggesting sufficiency. | Fibre-constancy is **necessary only**. Counterexample: `t -> (t^2, t^3)` is injective with singleton fibres, yet `t` is not a polynomial in `t^2, t^3`. The restriction theorem needs necessity only; the sufficiency wording is withdrawn. |
| B4 | §0 items 1, 5; §2 "There is no third kind"; §9 negative 1 | "`dim A = m_det`" is used to assert that no cheaper computation exists and that any target-side criterion costs the same as the boundary method. | `dim A_{d,lambda} = m_det` is a definition, not a complexity theorem. What is established: (i) multiplication/Pieri gives a valid recursion `m_det(d,lambda) <= sum_mu m_det(d-1,mu)`, which unwinds to lift counting; (ii) the restriction theorem trades the ambient pullback for source evaluations plus an image ceiling. Neither statement classifies all algorithms. "No cheaper reformulation" and "same price" are withdrawn. |
| B5 | §0 item 4 versus §4.1 and §8 | The opening advertises nonzero block-triangular fibre differences; the body and the degree-8 receipt prove they vanish. The displayed torus `(diag(t I_p, I_q), diag(t^{-1} I_p, I_q))` is not in `SL4 x SL4`. | Block-triangular fibres are **vacuous** (body is right, opening is wrong). Determinant-one version: `P = diag(t^q I_p, t^{-p} I_q)`, `Q = P^{-1} = diag(t^{-q} I_p, t^{p} I_q)`, `det P = det Q = 1`; then `P [[M1,N],[0,M2]] Q = [[M1, t^{p+q} N],[0, M2]] = [[M1, t^4 N],[0, M2]]`, so the off-diagonal block scales by `t^4` and the block-diagonal tuple is a torus limit inside the same `G`-orbit closure. |
| B6 | §4.2, Claim 4.2.3 and "Consequence" | The linear-kernel proof covers only surjective `kappa`; the "primitive dimension `<= 4`" reading is identified with the stronger compression/semistability conclusion without proof; H-EH is used as if settled. | Claim 4.2.3 is **PROVED only for surjective `kappa`**. A primitive-dimension bound does not by itself give compression or instability. The literature step is recorded in §B.6 below as **CONDITIONAL / open**; the route "Z contributes nothing to `>= 5` rows" stays conditional. |
| B7 | §4.3 dimension bookkeeping and the reading "`rho_L - u_L` measures non-normality plus map degree" | Asserts an interpretation without the quotient, finiteness and birationality hypotheses; calls block points polystable without proof. | `rho_L - u_L` is **a number bounded by the restriction theorem, not a measurement of non-normality or of a map degree**. The counts `dim L_(1,3)//G = 33 = dim pi(L)` are heuristic (they assume generic finite stabilisers and that generic block-diagonal tuples have closed orbits, neither checked). Withdrawn as interpretation; retained as an unverified dimension count. |
| B8 | §7.2 the `(4^6)` pilot | With `s = 10, a = 1, u_0 = 1` the clipped bound is `min(1, 11 - rho_0) = 1` for every `rho_0 <= 10`; sampled rank zero cannot prove `rho_L = 0`; no ten-vector B19-01 basis exists to reuse. | The proposed `(4^6)` pilot **cannot improve the determinant bound** and is withdrawn. B19-01 computed `s = 10` by characters and `b = 0` by the silence theorem; it built no carrier. |
| B9 | §7.3 the `(8,4,4,4,4)` candidate | Proposed a two-vector rank computation. | **Excluded symbolically**, §B.9 below. |
| B10 | §4.3 and §6 | Uses the padding ceiling `U` for the `2+2` product image; blurs raw product parametrisations with their Zariski closures. | For `pi(L_(2,2)) = closure{q_1 q_2}` no inclusion in `{l·C}` holds, so `U` does not bound `u_L` there; a separate ceiling is required. Throughout, `pi(L)` means the Zariski closure of the image of the raw parametrisation; the restriction theorem uses `C[closure]`, and `phi(L)` itself need not be closed. A sharpened `u_L` for the `1+3` determinantal-product image is a research direction, not a mechanism. |

### B.9 The `(8,4,4,4,4)` exclusion at `d = 6` (PROVED, premises listed)

Premises: (P1) `a(6,(8,4,4,4,4)) = 2` — **MEASURED** on 15 September
(`analysis/b18_12_ambient_table.py`, control sums matching `binom(75,6)`); (P2) the unique
`(4^5)` degree-five invariant `H5` is nonzero on the determinant closure — B19-02
certificate (reviewed) and **independently here**: `H5(det K5) = 322560 != 0` in the
`T = alpha! c_alpha` convention at the actual pencil `K5` (P3); (P3) `H5` vanishes on all
of `{l·C}` — **PROVED by Pieri**: `Sym^5(C^5) (x) Sym^5(Sym^3 C^5)` contains `S_(4^5)` only if
`(4^5)/nu` is a horizontal 5-strip for some `nu`, but a horizontal strip removed from a
rectangle with four columns has at most four boxes; hence `T(5,(4^5)) = 0`, `U = 0`
(B19-02 §8.1 records the same). Then:

- `h := c_(4,0,0,0,0) · H5` has weight `(4,0,0,0,0) + (4^5) = (8,4,4,4,4)` and is a
  highest-weight vector (raising operators are derivations, both factors are highest
  weight vectors).
- `h` is nonzero on `D45`: `C[D45]` is a domain (`D45` irreducible), `H5|_{D45} != 0`
  by (P2), and `c_(4,0,0,0,0)|_{D45} != 0` (the `x_1^4` coefficient of `det(sum x_k B_k)`
  is `det B_1`). So `m_det(6,(8,4^4)) >= 1`.
- `h` vanishes on `R135 = closure{l·C}` by (P3), so `i_pad >= 1` and
  `m_pad <= a - 1 = 1`.
- Hence `D = m_pad - m_det <= 1 - 1 = 0`. **The cell is excluded for a positive gap
  without any two-vector rank computation.** Normalisation of `H5` is irrelevant
  (nonzero is scale-free).

### B.6 The Eisenbud–Harris classification (time-boxed literature step)

See the entry in the claim ledger (§E); the outcome of the fifteen-minute lookup is
recorded there verbatim, with the source used. Whatever it found, the note's route
remains **CONDITIONAL**: the surjective-`kappa` case is the only part proved in this
programme.

## C. The one authorized five-row diagnostic: `d = 5`, `lambda = (4,4,4,4,4)`

### C.1 Dimensions (P1; MEASURED, controls passing)

| quantity | inherited (assignment) | recomputed here | method |
|---|---|---|---|
| `s` | 5 | **5** | `s_and_g` (Murnaghan–Nakayama, B18-02 formula 3.1) |
| `g` | 6 | **6** | same |
| `a` | 1 | **1** | Weyl alternant on `Sym^5(Sym^4 C^5)` weight multiplicities |
| `m_det` | 1 | **1** | `H5(det K5) = 322560 != 0` at the actual pencil `K5` (P3), independently of B19-02's three points |

Character controls: `(4), d=1 -> (s,g) = (1,1)`; `(6,3,1,1,1), d=3 -> (1,3)`;
`(5,3,2,1,1), d=3 -> (2,4)`; `(4,2,2,2,2), d=3 -> (2,2)`, all matching the B19 preamble and
the fibre report. Column heights `(5,5,5,5)`, twenty slots.

### C.2 The transverse condition `C2`, verified (P3; VERIFIED)

Conventions: ordinary coefficients; `H5` in the integral convention `T_alpha = alpha! c_alpha`
(B15-10); the producer's `T'` convention (`q = sum T' x_i x_j x_k x_l`) is `T' = T/24`, and
the producer's `F` is the full four-epsilon contraction, i.e. `5! · H5` in the `T'`
convention. All of the following are exact:

- `det K5 = u^2`, `u = x1^2 - x2 x5 + x3 x4`; `det(K5 + t x1 I4) = u^2 + t^2 v + t^4 x1^4`
  with `v = x1^2(2x1^2 + x2^2 + x3^2 + x4^2 + x5^2)`; `t`-support `{0, 2, 4}`.
- `Delta = d1^2 - 4 d2 d5 + 4 d3 d4` is exactly the `Q0^{-1}`-Laplacian of `u`;
  `Delta^2(u^2) = 280`, `Delta^2 v = 48`.
- Necessity derivation: on the extendable line `z = F ∘ phi` with `F` the `(4^5)`
  invariant, `F(q ∘ A) = det(A)^{±4} F(q)`, so `dF_{u^2}` is an `O(Q0)`-invariant
  functional on quartics; `Sym^4 = H_4 ⊕ u H_2 ⊕ C u^2` with `H_4, H_2` nontrivial
  irreducibles, so `dF_{u^2}(v) = 5 c F(u^2)` with `c` the `u^2`-component, and
  `Delta^2` kills `H_4` and `u H_2`, giving `c = Delta^2 v / Delta^2(u^2) = 48/280`.
  Hence `[t^2] z / z(K5) = 5c = 6/7`. **Independently confirmed by direct evaluation**:
  `H5(det(K5 + tS)) = 322560 + 276480 t^2 + 199680 t^4`, ratio `[t^2]/[t^0] = 6/7`.
- Even, degree `<= 4`: every `z in M_(4^5)` has degree `lambda_1 = 4` in `Y_1`, and
  `S` changes only `Y_1`; transpose invariance with `K5^T = -K5`, `S^T = S` and total
  degree 20 gives `z(K5 + tS) = z(K5 - tS)`. **PROVED.** So three values determine the
  restriction, and `[t^2] z = (16 z(K5+S) - z(K5+2S) - 15 z(K5))/12`.
- Therefore `C2(z) = 112 z(K5+S) - 7 z(K5+2S) - 177 z(K5)` vanishes on `E`:
  **directly checked, `112·798720 - 7·4623360 - 177·322560 = 0`.** Normalised values
  `1, 52/21, 301/21` (= `43/3`) agree with the producer; the producer's base value
  `175/36` equals `5! · 322560 / 24^5`, i.e. the same number in the `T'` convention
  with the `5!` factor. **VERIFIED.**
- The `Sp4` decomposition `50 = 5 + 10 + 35` was not used; nothing here relies on it.

### C.3 Pricing before running (P1, P5; MEASURED)

Greedy planner on random block partitions: intermediates `4^10` to `4^14`, flop units
`2·10^9` to `3·10^11` per orientation — unaffordable. Column-local partitions: `4^6`,
`4–7·10^6` — affordable. Same-column-pairing partitions with the hand order of
`paired_runner.py`: `4^10` entries (8 MiB), `1.7·10^8` flop units per orientation,
**measured 0.55 s per symmetrised evaluation** (both orientations, one point).

### C.4 Carrier construction: what was reached (P2, P4, P6, P8; MEASURED)

| family | candidates evaluated | result |
|---|---|---|
| column-local (19 cyclic shifts) | 19 at 7 points | **all identically zero at the points** |
| random partitions under the guard | 0 of 400 met the cost guard | none evaluated |
| same-pairing, paired blocks | 16 at 5 points | 2 nonzero, **independent (rank 2)**; 14 zero |
| priced random + pair-block (cheapest 65 of 4000) | 19 at the same 5 points | **all identically zero**; rank stays 2 |

Certified: **two independent vectors `q_3, q_7 in M_(4^5)`** (slot lists in
`pilots/p6_basis.json`, `pi`/`rho` fields; membership by construction; independence by the
`2 x 5` value matrix of rank 2 mod `524287`, hence over `Q`). **Not certified:** a basis.
The affordable contraction family (every intermediate `<= 4^10`) spans at most two of the
five dimensions in the samples taken; the remaining three dimensions appear to need
epsilon blocks linking three or more columns, whose cheapest observed plans carry
`4^14`-entry intermediates (2 GiB), above the 512 MiB cap. One such plan was executed by
mistake in the first P7 attempt and was killed by the allocator at 2 GiB (exit code 1,
0.6 s, recorded). **This is the resource receipt for "carrier not certified".**

### C.5 The arc and `C2` on the certified subspace (P7; MEASURED)

At points with all symmetric parts zero, Lemma 4.1 (`#Sigma = 2d + #alpha - #nu`) forces
`#nu = 10 + #alpha`, and `#nu <= lambda_1+lambda_2+lambda_3 = 12` (B19-01 Prop. 3.1)
leaves `#alpha in {0,1,2}`; scaling `a -> t a` gives `q(t) = q_10 + t q_11 + t^2 q_12`
with `q_11, q_12` the two forbidden components. Three nodes suffice; a fourth node
`t = 3` was predicted exactly at all three points (**degree control passed**), which also
re-confirms the skew-degree bound in this cell on these vectors. The runner reproduced
the stored P6 values at a P6 point (`260975, 301718`) exactly (**consistency control
passed**).

Forbidden rows (mod `524287`), columns `(q_3, q_7)`:

| point | `j = 11` | `j = 12` |
|---|---|---|
| 0 | `(34725, 239889)` | `(176113, 112168)` |
| 1 | `(163934, 316261)` | `(190461, 231336)` |
| 2 | `(395778, 379744)` | `(232316, 28953)` |

Rank of the six rows: **2**. So `rank C >= 2` over `Q` (characteristic-zero floor from
a nonzero modular `2 x 2` minor of actual forbidden coefficients), and `C` is injective on
`span(q_3, q_7)`: **no arc-kernel vector lies in the certified subspace.**

`C2` on the same vectors: values at `(K5, K5+S, K5+2S)` are `(94237, 458787, 323691)` and
`(491460, 393135, 229099)`; `C2` row `(456851, 3402)`, rank 1; stacked `[C; C2]` rank 2.
On this subspace the increment is zero, as it must be where `C` is already injective.

### C.6 Verdict for §C

- **Old arc exact here?** Not decided. Needed `rank C >= 4`; certified `rank C >= 2`.
  Upper bound `rank C <= 4` holds (`E = span(H5 ∘ phi) subset ker C`, `m_det = 1`).
- **Certified additional five-row constraint?** No. `C2` is nonzero on the source
  (rank 1 on the certified subspace) and vanishes on `E`, so it is a genuinely nonzero
  necessary condition, but no arc-kernel vector was available to test it on.
- **Outcome: INCONCLUSIVE WITHIN BUDGET**, with the carrier as the certified bottleneck.

### C.7 Resource ledger (all under the B15-02 `.venv` Python 3.12.10; P1, P3, P5 under
`timeout 60` with `OMP_NUM_THREADS=1`; P2, P4, P6, P7, P8, P9 under `analysis/b15_bound.py`,
the Windows Job Object wrapper, 60 s / 512 MiB, one worker, one BLAS thread)

| pilot | purpose | wall (s) | peak job memory (bytes) | exit |
|---|---|---|---|---|
| P1 | dimensions, pricing | 27.5 | not wrapped | 0 |
| P3 | `C2` derivation, `H5` | 0.8 | not wrapped | 0 |
| P2 | local carrier + arc attempt | 4.2 | 165,031,936 | 0 (basis rank 0) |
| P4 | paired candidates (filter too strict) | 0.8 | 143,368,192 | 0 (0 candidates) |
| P5 | plan diagnostic (label-only) | 0.5 | not wrapped | 0 |
| P6 | same-pairing basis | 44.5 | 142,606,336 | 0 (rank 2) |
| P8 | priced random/pair-block basis | 43.9 | 135,888,896 | 0 (rank 2) |
| P7 (first) | arc, wrong plan | 0.6 | 94,101,504 | 1 (2 GiB allocation refused) |
| P7 | arc + `C2` on two vectors | 17.5 | 219,455,488 | 0 |
| P9 | six-row replay | 6.4 | 165,720,064 | 0 |
| **total** | | **≈ 147 s** of the 600 s budget | | |

No heavy lease was requested. No historical file was modified. The `ulimit -v` shell
setting is not relied on; the Job Object receipts are the memory evidence.

## D. Board decision, and one recommendation

### D.1 Plain-language summary of what was actually established

- **Astra, six rows.** A genuine, explicit false survivor `Q^2` at `(6,(4^6))`, detected
  by two independent globally necessary conditions (two-pencil descent, ratio 1120; and
  the fourth-order transverse condition `J2 - 108 J1 + 14 z(K)`), both replayed here. Each
  has rank one on the ten-dimensional source; neither lowers the clipped bound below `1`;
  the other eight missing dimensions are not exhibited. The cone-vertex projector is the
  same fact restated with the ambient line known.
- **Astra, five rows.** Interpolation in a complete carrier is a correct certification
  theorem whose bottleneck is the carrier. One negative degree-six pilot
  `(12,8,2,1,1)`: no determinant equation there. The `2+2` partial-transpose family gives a
  nonzero necessary functional at an `a = 0` five-row cell but zero increment, and is
  provably blind on even five-row rectangles.
- **Claude note.** The restriction theorem survives as a necessary-condition bound with the
  strict-image-ceiling bottleneck (B2); its opening overclaimed in five places (B3–B7); its
  two proposed pilots are withdrawn, one by arithmetic (B8) and one by a symbolic exclusion
  (B9).
- **This session's diagnostic.** In `(5,(4^5))`: `s = 5`, `g = 6`, `a = 1`, `m_det = 1`
  recomputed; the chat-only transverse map `C2` verified to be globally necessary and
  nonzero on the source; two independent full-`H` vectors certified; `rank C >= 2` and
  `C2` rank 1 on them; the full carrier not reached within the cap.

### D.2 The decision

**INCONCLUSIVE WITHIN CAP** for the exactness question in `(5,(4^5))`. Not "five-row arc
exact here" (needs `rank C >= 4`, have `>= 2`); not "certified additional five-row
constraint" (no arc-kernel vector was available). No positive-gap claim anywhere; every cell
touched is a known no-gap cell.

What would settle it, and the price: three more independent vectors of `M_(4^5)`. The
affordable contraction family has been exhausted twice (rank 2 both times, with 33
identically-vanishing candidates); the next family needs `4^14`-entry intermediates
(2 GiB) per contraction with the present dense evaluator, i.e. a heavy lease, **or** a
different evaluator. The decisive alternative is cheaper than a lease: a **sparse
column-tensor evaluator** that keeps only the nonzero wedge assignments (7680 at `K5`-type
points versus `16^5` dense) and a dynamic programme over the twenty slots with the
epsilon blocks' partial-fill states. Its cost is bounded by (assignments per column) times
(reachable states) and has not been priced; that pricing is the first step of any
continuation.

### D.3 One recommendation (structural, falsifiable)

**Question.** Is the arc exact on the five-row rectangles `(4k)^5`, i.e. is
`ker C = E` there, and if not, does the `K5`-type transverse map detect a survivor?

**Why this and not a census.** The rectangles are the only five-row cells where (i) the
full-`H` source is `SL5`-invariant, so carrier vectors are quartic-in-Plücker invariants of
a single 5-space of matrices and no highest-weight bookkeeping is needed; (ii) the
transverse map is fully verified (§C.2) and the even-degree-four structure removes all
interpolation; (iii) `a = 1` at `k = 1` makes `E` explicit; (iv) the `2+2` fibre family is
provably blind, so any detection would be genuinely new information about the arc.

**Inputs.** The two certified vectors and their slot lists (`p6_basis.json`); the S0-point
trick of §C.5 (three nodes per point); the three `C2` evaluation points; a sparse evaluator
as described in D.2, priced first on `K5` (7680 assignments per column).

**Expected output.** Either a `4 x 4` forbidden minor (arc exact at `k = 1`: then no
necessary condition, `C2` included, can add anything there, and the recommendation is
closed with a certified negative), or an exact arc-kernel vector `n` with all ten forbidden
coefficient polynomials verified zero and the single number `C2(n)`.

**Falsification.** A nonzero `4 x 4` minor from actual forbidden coefficients at any
points kills the "false survivor" hypothesis in this cell in one modular computation.
Conversely `C2(n) = 0` on an exact kernel vector kills the transverse map as a detector in
this cell (not in general).

**Price.** Unknown until the sparse evaluator is priced; the dense route is a heavy lease
and is not recommended.

## E. Claim ledger

| # | Claim | Label | Evidence |
|---|---|---|---|
| E1 | `s = 5`, `g = 6`, `a = 1` at `(5,(4^5))` | MEASURED (four controls pass) | P1 |
| E2 | `m_det(5,(4^5)) = 1` | VERIFIED independently (`H5(det K5) = 322560`) and PRODUCER-CERTIFIED (B19-02, reviewed) | P3; `rect_4_4_4_4_4.json` |
| E3 | `C2(z) = 112 z(K5+S) - 7 z(K5+2S) - 177 z(K5)` is globally necessary on `M_(4^5)` | VERIFIED (derivation re-derived; direct vanishing on `E`; even-degree-4 structure proved) | P3, §C.2 |
| E4 | Producer's `175/36`, `52/21`, `301/21` | VERIFIED as convention-scaled values (`5!` and `T' = T/24`) | P3 |
| E5 | Two independent vectors `q_3, q_7 in M_(4^5)` | CERTIFIED (membership by construction; `2 x 5` modular rank 2) | `p6_basis.json` |
| E6 | `rank C >= 2` over `Q` in `(5,(4^5))`; `C` injective on `span(q_3,q_7)` | CERTIFIED (nonzero modular `2 x 2` minor of actual forbidden coefficients; two controls passed) | `p7_arc_S0.json` |
| E7 | `rank C <= 4` | PROVED (`E subset ker C`, `dim E = m_det = 1`) | §C.6 |
| E8 | `rank C = 4` (old arc exact here) | NOT REACHED | — |
| E9 | An exact arc-kernel vector and `C2` on it | NOT REACHED | — |
| E10 | Full basis of `M_(4^5)` by affordable contractions | NOT REACHED; 33 cheap candidates vanish identically, family rank 2 | P2, P6, P8 |
| E11 | Six-row: `P^2` values `1, 9/4, 9, 4, 25`; `C2 = 0` on `E`; `C2(P^2) = -12`; `c = 1/6, 1/3`; `[t^2]/[t^0] = 6c`; single `kappa = 3/896` fits both fourth-order values | VERIFIED (independent script driving the producer's evaluator; symbolic constants recomputed) | P9 |
| E12 | Six-row two-pencil values and minor | PRODUCER-CERTIFIED, execution replayed (`Q(K)`, `H6(F_K)`) | P9, `verification.json` |
| E13 | Interpolation theorem | VERIFIED as a theorem; carrier completeness is the bottleneck (measured here) | §A.2 |
| E14 | `(12,8,2,1,1)` no-equation pilot | PRODUCER-CERTIFIED (own verifier); `a, s` inherited | `five_row_verification.json` |
| E15 | Fibre test: `s = g = 2`, values, arc rank 2, zero increment | `s, g` VERIFIED; rest PRODUCER-CERTIFIED; conclusion VERIFIED | P1, `verification.json` |
| E16 | Rectangular blindness of `2+2` partial transpose | VERIFIED (re-derived); HMSV pointer not fetched | §A.5 |
| E17 | `Omega det Q = 315/4`; `C2(P) = -5040 P(K)` at `d = 3` | ADOPTED (standard identity) / CONDITIONAL (`(3,2,1)` nonvanishing not checked); no artifact | §A.3 |
| E18 | Restriction theorem `m_det <= min(a, s - rho_L + u_L)` with closed homogeneous `G x GL5`-stable `L` | PROVED (corrected statement) | §B1 |
| E19 | With `u_0 = U` the bound can never give a gap | PROVED | §B2 |
| E20 | Block-triangular fibres vacuous; determinant-one torus | PROVED | §B5 |
| E21 | `(8,4,4,4,4)` at `d = 6` has `D <= 0` | PROVED on (P1) MEASURED, (P2) VERIFIED, (P3) PROVED by Pieri | §B.9 |
| E22 | Singular-locus route (`Z`) blind to `>= 5` rows | CONDITIONAL: surjective-`kappa` case PROVED; classification step OPEN (§B.6 outcome below) | §B6 |
| E23 | `rho_L - u_L` measures non-normality / map degree | REJECTED as interpretation | §B7 |
| E24 | `(4^6)` fibre pilot improves the bound | REJECTED (clipped bound is 1 for all `rho_0`) | §B8 |
| E25 | Cone-vertex projector as an independent mechanism | REJECTED (circular); ACCEPTED as restatement | §A.1 |

**§B.6 outcome (time-boxed, about fifteen minutes).** The primary text (Eisenbud–Harris,
Adv. Math. 70 (1988) 135–155; a copy was fetched from `eisenbud.github.io/papers/pdfs/1988-004.pdf`,
SHA-256 prefix `6b10d8fea80396a7`, kept outside the delivery tree) could not be read in
this environment: no PDF text extraction tool is installed, and the two secondary pages
reached (EUDML record of Ballico's addendum; the search summary) give only the abstract-level
statement that "the characterization of vector spaces of matrices of rank `<= 3` due to
M. D. Atkinson follows from" the Eisenbud–Harris results, without the list. **The exact
theorem, its numbering and its hypotheses were not verified.** The Claude note's implication
("every singular subspace of `Mat4` of dimension `>= 5` is a compression space") therefore
stays **CONDITIONAL / open**, and the route is left open, not closed.
One secondary source was readable: Huang–Landsberg, *On linear spaces of matrices of
bounded rank*, arXiv:2306.14428 (HTML version, review section), which restates Atkinson's
1983 classification as: for bounded rank `r = 3` "the only primitive examples are Example
1.3 and its projections", where Example 1.3 is the wedge space `e -> (v -> e ∧ v)` on
`C^a` (bounded rank `a - 1`), and "imprimitive" means the space or its transpose restricts
to a hyperplane with bounded rank `r - 1`. For `a = 4` the wedge space and its projections
to `C^4` are precisely the note's `X_Lambda = {Lambda(x, ·)}`, of dimension `4`. **What
this does and does not give:** it supports "primitive rank-3 spaces of `4 x 4` matrices
have dimension `<= 4`", but "imprimitive" is a restriction-to-hyperplane condition, not the
compression (semistability) condition the note needs; a five-dimensional imprimitive
singular space with no compression subspace is not excluded by this paraphrase, and the
primary theorem was not read. **Status: CONDITIONAL, pointer recorded, not closed.**

## F. Honest negatives

1. No five-row rank increment and no five-row exactness certificate: the cell's carrier was
   not completed within the cap. The certified content is `rank C >= 2` and a verified,
   nonzero, globally necessary transverse map.
2. The affordable contraction family is degenerate in this cell (33 of 35 cheap candidates
   vanish identically at five points). Whether that is a theorem about pair-closable
   contractions on `(4^5)` or an artifact of the sampled slot splits is not known.
3. The first P7 run executed a `4^14` plan by mistake; the Job Object environment refused
   the 2 GiB allocation and the run exited with code 1 in 0.6 s. Its resource log was then
   overwritten by the successful run of the same name; the console record is kept in §C.7.
4. The literature step for the singular-locus route did not complete.
5. `a, s` for `(12,8,2,1,1)` and `a = 1, s = 10` for `(4^6)` were inherited, not recomputed.
6. Nothing here bounds `m_pad`, produces `r`, or nominates a cell.

Status: **COMPLETE — inconclusive within budget on the exactness question; certified
partial results and repaired claims delivered.** Total numerical pilot wall time
about 147 s of the 600 s budget. `MANIFEST.json` pins inputs and outputs; the report was
finalised before hashing.
