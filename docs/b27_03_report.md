# B27-03 — A25-10's reopening condition at a nonsymmetric witness

**Producer: Claude Code (Opus 5.5), slot B27-03, branch `b27-03`. PRODUCER ONLY, pending R27-03.**

**Registered outcome: (4) obstruction with a price, together with (2) scoped containment on the
stated spaces. That containment is vacuous: the kernel is zero on every space tested.** Outcomes (1) and (3) were not obtained.
**Achievement level: none of the four.** No source condition, coefficient equation, separation on
padding or multiplicity gap is claimed. The binding constraint stands: "No five-row determinant
equation is known to be nonzero on padding."

| rung | result |
|---|---|
| 3a | Done. An explicit integer `T′` with a nonsymmetric block. `F_T′ ∉` A26-01's family or any `GL5` translate of it (HAND + COMPUTED). All 65 retained coefficients are computed exactly. |
| 3b | Certified negative for every *reducible* literal preimage. This covers A26-01-type pencils after any change of basis, block-triangular pencils, and Pfaffian-square and 2+2 pencils. `T′` is **not** rejected. No claim is made about `Y_5`. |
| 3c | The lowest degree with nonzero `ker Q_D` on the 65 coordinates is **not reached**. `ker Q_D = 0` in every degree ≤ 4 (whole ring), on A26-01's named degree-8 space, and along two peaked weight rays **in every degree**. The kernel basis is empty, so the evaluation at `π(P_T′)` is vacuous. |
| 3d | Priced (section 4). The next non-vacuous step first needs the onset of `I(D)` itself, which neither this session nor the programme record has observed. |

Labels: READ = committed text read (hashes in `results/b27_03/INPUT_BINDINGS.json`); HAND = my
derivation; COMPUTED = one of the seven runs logged in `results/b27_03/RESOURCE_RECEIPT.md`.

## 0. Preflight and setting

The brief hashes match `BATCH27_BOARD.md`. The branch is `b27-03` and HEAD is `fcff7eea`, equal to PART 25's setup commit
for this slot. The tree is clean and the output paths were absent. B27-01 had committed no `T*` (the remote `b27-01` tip is
still the setup commit `6dea55ec`, rechecked at 04:01Z), so `T′` is my own choice.

Notation (READ, A25-05 `STRUCTURAL_MAP.md`, `FIVE_CENTER_REDUCTION.md`):
- `W = Sym^4 (C^5)*`, `D = closure(im φ)` with `φ(B) = det(Σ x_i B_i)`, and `P` = the actual padding `closure{l·per3(A)}`.
- `E` = the 65 exponents `|α| = 4` with `max α ≥ 2`, `π` the retained projection, and `Y_5 = closure π(D)`.
- `K5 = span{q_i = Π_{j≠i} x_j}`.
- For a coefficient-weight space `H` (coefficient degree `k`, torus weight `w`), `Q_D : H → C[D]`. Its kernel is
  `I(Y_5) ∩ H = I(D) ∩ H`.

## 1. Rung 3a — the witness `T′`

**Definition (fixed before any evaluation).** Take `l = x1+x2+x3+x4+x5` and

    A′ = [ x1+x3     x2−x4    x5+2x1
           x3+x4     x1−x5    x2+x3
           x2+2x5    x4+x1    x3−x2 ].

So `T′` is the integer 10×5 matrix with rows `(z, y11, …, y33)` given in `results/b27_03/witness.json`.
Its actual padding is `F := F_T′ = l·C` with `C = per3(A′)`. The block is not symmetric in six positions
(COMPUTED, run 1). The cubic is

    C = 2x1²x2+4x1²x3+2x1²x4+4x1²x5+x1x2x4+2x1x3²+3x1x3x4+2x1x4²+x1x4x5−2x1x5²+x2³−2x2²x4
        +2x2²x5+x2x3²+2x2x3x4+3x2x3x5+x2x4²−2x2x4x5−x2x5²−x3²x5−x3x4²−x3x4x5+x4²x5−2x5³.

**COMPUTED facts (run 1, exact, GF(32003) Gröbner bases, grevlex):**
- (i) the five partials of `C` have only the trivial common zero over `GF(p)‾`;
- (ii) for 8 of the 10 coordinate 3-planes `V` (all except `{x1,x4,x5}` and `{x2,x4,x5}`), the three partials of `C|_V`
  have only the trivial common zero;
- (iii) all five coefficients of `l` are nonzero.

**Lemma 1 (HAND): smooth mod p implies smooth over `Q‾`.** Suppose `x ∈ Q‾^n \ 0` is a common zero of the integer partials. Pick
a prime `𝔭 | p` of `K = Q(x)` and scale `x` so that all its coordinates lie in the DVR `O_𝔭` and one is a unit. Its reduction is then a
nonzero common zero over `GF(p)‾`. By Euler's relation (`p ≠ 3`, char 0), a common zero of the partials is a singular point. Smooth
hypersurfaces of dimension ≥ 1 are irreducible. Hence `C` is a smooth, irreducible cubic threefold, and `C|_V` is a smooth,
irreducible plane cubic for the eight planes in (ii).

**Lemma 2 (HAND): every 3×3 linear determinant in five variables is singular.** Let `L : C^5 → Mat_3`
be linear. If `L` is injective, then `P(L(C^5))` (a `P^4`) meets the 4-dimensional rank-≤1 Segre variety inside `P^8`
(4+4 ≥ 8). At such an `x` every 2×2 minor vanishes, so `∇(det∘L)(x) = 0`. If `L` is not injective, `ker L` gives `M(x) = 0`.
Singular cubics form a closed set (proper projection of the incidence variety), so the whole closure `D_5^{det3}` consists of singular cubics.

**Proposition 3 (HAND, using READ of A26-01 identity (C), with its six terms re-expanded by hand): `F ∉ S_lit`, and `F` lies in no
`GL5` translate of `S_lit`.** A26-01 `PROOF.md` §2 (READ) gives `l′·per[a d e; d b f; e f c] = det diag(l′, M_√2)`.
Suppose `F = l′·per(A_sym)`. Since `C` is irreducible of degree 3, unique factorization forces `l′ ∝ l` and `per(A_sym) ∝ C`.
Then `C` is a literal 3×3 determinant (absorb the scalar into a row), which contradicts Lemma 2. `S_lit` is `GL5`-stable (its seven forms are
arbitrary), so the statement covers every linear change of variables that A26-01 covers. It also excludes A25-05's family (`z per` of a symmetric
block) and A25-04's `T`. (READ, standing convention: B17-01's smooth-cubic exclusion says `lC ∉ D` for smooth `C`, so `F ∉ D` as well.
B17-01 itself was not re-read in this session.)

**The 65 retained coefficients `π(P_T′)`** are exact integers, 58 of them nonzero, listed in descending lexicographic order in
`witness.json` (key `pi_PT_65`). The omitted `K5` coefficients are `(6,3,0,3,2)` for `q5,q4,q3,q2,q1`. Examples:
`c(3,1,0,0,0)=2`, `c(3,0,1,0,0)=4`, `c(2,1,1,0,0)=6`. Note that `c(4,0,0,0,0)=0`.

## 2. Rung 3b — projection test against certified constructions

**Theorem 4 (HAND, from COMPUTED facts (ii) and (iii)).** Let `K ∈ K5` and suppose `F+K = G1·G2` with `deg G1, deg G2 ≥ 1`. Then
`K = 0` and `{G1, G2} = {γl, γ⁻¹C}`.

*Proof.* Each `q_i` omits only one variable, so it vanishes on every coordinate 3-plane. Hence `(F+K)|_V = l|_V·C|_V ≠ 0`.
- **The degrees are 1 and 3.** For a good plane `V`, `C|_V` is irreducible of degree 3, so it cannot divide a factor of degree 2. The degrees are therefore
  (1,3), and a linear factor `l′` exists.
- **`l′` restricts to `l` on each good plane.** On each good `V`, the only linear factor of `l|_V C|_V` is `l|_V`, so `l′|_V = c_V·l|_V`.
- **The constants agree.** Any two 3-subsets of {1..5} meet, and `l` has all coefficients nonzero, so all the `c_V` are equal. The good planes cover all
  five coordinates, so `l′ = c·l`.
- **So `K = 0`.** Now `K = l·(c·G − C)` for the cofactor `G`. If `l·R ∈ K5` then `deg_i(lR) = 1 + deg_i R ≤ 1` for every `i`, so `R` is a
  constant of degree 3, i.e. `R = 0`. This is the fixed-factor kernel with `r = 5`, re-derived here (A25-05 `PADDING_FIBERS.md` §1, READ).
  Hence `K = 0`. ∎

**Corollary 5 (certified negative for literal preimages).** No literal completion `F+K` equals `det M` for any 4×4 linear pencil
`M` of the following kinds, over C, after any `M ↦ PMQ` with `P, Q ∈ GL4`:
- (a) **1+3 block-diagonal or block-triangular.** This includes every A26-01-type `diag(l′, M_u)` after a change of basis. By Theorem 4, `det M = F` and
  `det M3 ∝ C`, contradicting Lemma 2.
- (b) **2+2 block-diagonal or block-triangular, or finer.** Here the determinant has a factor of degree 2, or it has a linear factor with a reducible cofactor.
  Both contradict Theorem 4.
- (c) **Skew-symmetric (Pfaffian-square).** Here `det M = Pf(M)²`. Restricting to a good plane would give `l|_V·C|_V = (Pf|_V)²`, but `C|_V` occurs with
  multiplicity 1.

Also (READ, B17-01) `F` itself is not in `im φ`. Therefore **any literal preimage of `π(F)` in `im φ` is an irreducible quartic `F+K` with `K ≠ 0`**.
None of the certified constructions produces one. This is a failed search among named constructions, and it does not
rule out an irreducible determinant completion. **It is not a claim that `π(F) ∉ Y_5`.** A25-05 §1 (READ) shows that the closed set is
`closure(D+K5)`, and a literal-preimage search does not test it. **`T′` is not rejected (outcome 3 not obtained).**

## 3. Rung 3c — exact kernel of `Q_D` on bounded weight spaces

**Method (COMPUTED certificate, not a sampled nullspace).** For `H` with monomial basis `h_m`, take explicit integer pencils
`B^(j)` (a deterministic LCG with a stated seed; entries in `{−3..3}` or `{−5..5}`) and compute `det(Σ x_i B_i^(j))` exactly by a signed einsum over the
24 permutations. Then form `E[j,m] = h_m(π(det))`. If `rank_p E = dim H` with `p = 10^9+7`, then some `dim H` minor is nonzero mod `p`, hence nonzero over Z.
So no nonzero `h ∈ H` vanishes at these determinant points, and **`ker Q_D ∩ H = 0`**. A deficient rank at explicit points only
bounds the kernel from above and is never used as a claim.

**Lemma 6 (HAND, one weight certifies a whole degree).** `I(D)_k` is a `GL5`-submodule of `C[W]_k`, because `D` is `GL5`-stable. Let `μ0` be the balanced
partition of `4k` into 5 parts. It is the unique dominance minimum among partitions with at most 5 parts. *Proof:* write `4k = 5q + r`.
If `S_j(ν) < jq + min(j,r)` then `ν_j ≤ q`, so `4k ≤ S_j + (5−j)q < 4k`, a contradiction. Hence every `S_ν ⊆ I(D)_k` has a nonzero
`μ0`-weight space. So `I(D)_{k,μ0} = 0` implies `I(D)_k = 0`, and then `I(Y_5)_k = 0` because `I(Y_5) ⊆ I(D)`.

**Lemma 7 (HAND, stabilization along a peaked ray).** Let `w_k = (4k−s, w′)` with `|w′| = s`. For `k > s`, every monomial of `H_{k,w_k}` contains
`c(4,0,0,0,0)`, because the `k` factors share an `x2..x5`-degree of only `s`. So `h ↦ c(4,0,0,0,0)·h` maps `H_{k−1}` onto `H_k` bijectively.
Since `Y_5` is irreducible and `c(4,0,0,0,0) ≢ 0` on it (`x1^4 ∈ D`), `ker` at degree `k−1` is zero if and only if `ker` at degree `k` is zero. This holds in both rings.

**Certified results (COMPUTED; each is `rank = dim`):**

| space | ring | dim H | points | rank_p | run |
|---|---|---:|---:|---:|---|
| whole degree 2, `μ0 = (2,2,2,1,1)` | 70 | 13 | 29 | 13 | 2 |
| whole degree 3, `μ0 = (3,3,2,2,2)` | 70 | 167 | 183 | 167 | 2 |
| whole degree 4, `μ0 = (4,3,3,3,3)` | 70 | 1905 | 1921 | 1905 | 6 |
| A26-01's `H = (8,(24,2,2,2,2))` | 65 | 480 | 496 and 960 (two point sets) | 480 | 2, 3 |
| `(8,(24,2,2,2,2))` | 70 | 619 | 1238 | 619 | 3 |
| `(8,(23,3,2,2,2))` | 65 | 1018 | 2036 | 1018 | 3 |
| ray 1 `(4k−8,2,2,2,2)`, k = 3..7 | 65 and 70 | 105…618 | N+16 | full | 5 |
| ray 2 `(4k−9,3,2,2,2)`, k = 4..7 and 9 | 65 | 441…1019 | N+16 | full | 5, 7 |

**Consequences (HAND from these certificates and Lemmas 6–7):**
- **Low degrees.** `ker Q_D = 0` on the 65 coordinates (indeed `I(D)_k = 0`) for every `k ≤ 4`. This independently certifies the lower part of the
  onset window. `docs/det_onset.md` (READ) states the floor 8 for `I(D_5^det)`, and `CORRIGENDUM.md` (READ) records that floor as not audited.
- **Ray 1.** `ker Q_D = 0` on `w_k = (4k−8,2,2,2,2)` for **every k ≥ 2**, in both rings: `k = 2` by Lemma 6, `k = 3..8` COMPUTED, `k ≥ 9` by Lemma 7.
  This is A26-01's weight family, and it is also the record's "tightest" `(4δ−8,2,2,2,2)` family (READ, `det_onset.md` §2).
- **Ray 2.** `ker Q_D = 0` on `(4k−9,3,2,2,2)` for **every k ≥ 3** in the 65-coordinate ring: `k = 3` by Lemma 6, `k = 4..9` COMPUTED, `k ≥ 10` by Lemma 7.

**An observation that did not survive (recorded honestly).** In run 2 the 70-coordinate space `(8,(24,2,2,2,2))` gave rank 613 of 619 on
635 points with entries in `{−3..3}`. That was an upper bound only, and no claim was made. Run 3, on an independent set of 1238 points, gives rank 619, which certifies that the
kernel there is zero, in agreement with the record's `mult_det = a` at δ = 8. The deficiency came from the point set.

**Evaluation at `π(P_T′)`.** Every kernel computed above is `{0}`, so there is no basis to evaluate. The resulting "scoped containment" is
**vacuous**: these spaces carry no determinant equation at all, so they are dead for *every* `T′`, not just this one. That is outcome (2) in its
weakest form. It is progress only in that it certifies where equations cannot live.

## 4. Rung 3d — price of the next step (priced preregistration; nothing launched)

Measured cost model (runs 3, 5, 6): forward elimination mod `p` takes about `30 s × (N/1905)^3`, and memory is about `8·N·(N+16)` bytes (int64).

| next space | dim N | est. time | est. memory | within allowance? |
|---|---:|---:|---:|---|
| `(8,(22,4,2,2,2))`, 65 | 1971 | ~33 s | 31 MB | yes (1 run) |
| `(8,(22,3,3,2,2))`, 65 | 2243 | ~49 s | 40 MB | yes (1 run), borderline |
| ray 3 at its stable degree, e.g. `(10,(30,4,2,2,2))` or `(10,(30,3,3,2,2))`, 65 | ≈2000–2300 (the k=8 dims are 1971/2243; the k=10 dims were not computed) | ~35–55 s | ≤ 45 MB | yes; each run would close one more ray in all degrees |
| `(8,(20,3,3,3,3))`, 65 | 11554 | ~1.9 h | 1.07 GB | **no**: needs preregistration and >512 MB, or blocked storage |
| whole degree 5, `μ0 = (4,4,4,4,4)`, 70 | 19834 | ~9.4 h | 3.1 GB | **no** |
| degree 8, balanced `(7,7,6,6,6)` | 4.61M (65) / 9.48M (70) | dense: infeasible | ~10^14 B | **no**: only via the programme's isotypic/HWV pipeline, hours per cell (READ, `balanced_corner.md`) |

**The obstruction.** For every weight `w`, `I(Y_5)_{k,w} ⊆ I(D)_{k,w}`. So a reopening witness first needs a weight space where
`I(D)` is nonzero, and none has been observed:
- in this session: no nonzero kernel in any space tested;
- in the record: δ = 5–10 occurrence screen silent, δ = 8 reachable cells empty (READ, `det_onset.md` §0).

The cheap rows above are expected to return `{0}`. They would sharpen the no-go map, but they cannot yield outcome (1). A positive also needs an
**exact** membership proof for the candidate `h`. The dense route substitutes the 50-parameter normal form, which gives up to `binom(50+5k, 50)` monomials
(`≈ 5×10^19` at `k = 5`), so it is infeasible. The programme's existing certificates ("rank attains a") certify only emptiness.
So a positive requires a named exact method for an *upper* bound on `rank Q_D`, for example exact linear algebra in the
`SL4×SL4`-invariant model of `C[D]_k`. That method is **unpriced** here and would need its own preregistration and user approval.

Recommended (not launched): if the programme wants more no-go coverage, spend ≤ 4 allowance-sized runs on the rows marked "yes". If it wants
outcome (1), it first needs a preregistered onset search in the balanced corner with an exact kernel method. That exceeds this allowance by orders of magnitude.

## 5. Provenance, resources, delivery

- Seven runs, sequential, each under 60 s. Largest arrays were about 30 MB (memory was not instrumented; the bound is from array sizes). Commands,
  hashes and wall times are in `results/b27_03/RESOURCE_RECEIPT.md`.
- sympy 1.14.0 and numpy 2.4.6 were already installed. Sage is absent. Nothing was installed.
- One correction: the docstring of `analysis/b27_03_rays.py` says N+32 points, but the run used N+16 (the library constant). Its JSON records the actual value.
- Clock: first reading 03:52:44Z, last mathematical run 04:01:40Z, packet written afterwards. The session stayed well inside the 90-minute ceiling, and the
  45-minute checkpoint was not reached before the mathematics stopped.
- No subagents, messages, publication, or edits to papers, ledgers or seals. Only my own branch was touched.
- `results/b27_03/MANIFEST.json` binds every payload.
