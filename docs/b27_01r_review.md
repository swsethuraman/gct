# R27-01 — cross-lineage review of B27-01 (Claude reviewer; Astra producer)

**Verdict in one line:** every rung is **ACCEPTED** at the level the producer assigned. There is
one wording nit and no REPAIR, DEFER or REJECT. The achieved level is **geometric noncontainment
at one explicit actual-padding point `T*`**. That point is the committed B17-01 witness, which is
now replayed and independently re-certified. B27-01 gives no coefficient equation, no separation
on padding and no multiplicity gap. The binding constraint stands unchanged: "No five-row
determinant equation is known to be nonzero on padding."

## 0. Preflight and exposure

- **Administrative, raw SHA-256.** These match the board.
  - `B27_COMMON.md`: `891e3ca8…d6ee`
  - `R27-REVIEWS.md`: `916de53a…aaa9`
  - `BATCH27_BOARD.md`: `b0bc2501…efec`, which matches PART 25's receipt.
- **Branch and outputs.** Branch `b27-01r`, worktree `work/batch27/b27-01r`. HEAD is
  `6dea55ec926c1618cc60ad71209795528705bf61`, PART 25's setup commit. The working tree was clean,
  and none of the output paths existed.
- **Prior exposure: none.** This session did not produce the B27-01 packet and did not see it
  during production.
  - Disclosure: my auto-memory holds a one-line note, from another session's R27-02 work, that
    "p4 lies in D". That note is **not used as evidence**. §2.4 below re-derives the fact
    independently.

## 1. Bindings

- **Producer tip.** `b27-01` is at `01f78eb2a585599378727253e1906b8314f2adb2`, confirmed by
  `ls-remote`. Its single parent is `6dea55ec`, the setup commit. The diff from the parent touches
  only `docs/b27_01*`, `results/b27_01/**` and `analysis/b27_01_*`.
- **Manifest.** `results/b27_01/MANIFEST.json` has blob SHA-256
  `580aa717efd424fd89619f8bde5dd16c4e1a7a5b902ad9629d6c5e9c882f3863`.
- **Payloads (COMPUTED, administrative).** All **39/39** manifest payloads match
  `git show 01f78eb2:<path>` in raw SHA-256, byte count and Git blob OID.
  - No slot file is missing from the manifest, and no manifest entry is missing from the tree.
- **Mathematical input.** `01c49022:results/b17_01/certificate.json` has blob SHA-256
  `03585015…8e9c`. This equals the producer's snapshot `results/b27_01/inputs/b17_certificate.json`.

## 2. Claim check

### 2.1 Replay of the producer's COMPUTED runs

I re-ran all three runs on the committed tip bytes, sequentially, with the installed CPython
3.12 (interpreter SHA-256 `4d6f5f81…859a`). This is a different interpreter from the producer's.

| run | script | outcome | wall s | output hashes vs manifest |
|---|---|---|---:|---|
| 1 | `b27_01_verify.py` | PASS: residue 61614, 569-digit integer minor, frame 2562 | 3.02 | `T_STAR.json` `671e7868…9bd2` and `SMOOTHNESS_CERTIFICATE.json` `67392878…6c42`: **identical** |
| 2 | `b27_01_boundary.py` | retained negative, rank 203 | 0.04 | `BOUNDARY_CERTIFICATE.json` `9afaa64a…73b1`: **identical** |
| 3 | `b27_01_tangent.py` | PASS: rank 209, node, rank 35 | 7.30 | `TANGENT_CERTIFICATE.json` `6e39942c…a1b8`: **identical** |

### 2.2 Independent re-derivation of the certificates

I used my own code, with no producer routine: SymPy builds the polynomials, and I reduce each
matrix by full Gaussian elimination with **no fixed row set**. I worked modulo the primes
1000003 and 2147483647, both different from the producer's 65521. Rank modulo p is a lower bound
for rank over Q. See `results/b27_01r/RANKS.json`.

**T\*.** These results are COMPUTED.
- The report's displayed 10×5 table equals `T_STAR.json`.
- `per₃` recomputed with SymPy matches all 35 stored coefficients.
- `rank T* = 5` over Q.
- `M₆(C*)` is 350×210 and has rank **210** modulo both primes, so its rank over Q is 210.
  - HAND: the Jacobian ideal therefore contains all of `S₆`, so `C*` is smooth over `C`. This is
    a second, row-set-free certificate that agrees with B17 and B27-01.
- Controls: `rank M₄(C*) = 65`, which is the cap note's n=3 figure for a smooth cubic, and
  `rank M₇(x₀C*) = 244` modulo both primes.
  - HAND: this lies under the proved ceiling of 245, and it kills every 299-minor and every
    300-minor.

**A†.** These results are COMPUTED.
- I rebuilt A† from the formulas in `MAP_AND_BOUNDARY_PROOF.md` §3:
  - `per(q) = 0`;
  - the cofactors equal the stated `g`;
  - `g·V_r = 0` for r = 1..4;
  - the cubic's coefficients match the certificate.
- The `x₀⁶` column is identically zero, and `M₆` has rank **209** modulo both primes. Over Q the
  rank is therefore exactly 209.
- The gradient at `e₀` is 0.
- The Hessian determinant is `-863583313736999047506762240`, exact and equal to the producer's
  value.
- The 45×35 parameter differential has rank **35**.
- HAND:
  - The ideal contains every degree-6 monomial except `x₀⁶`, so the only singular point is
    `[1:0:0:0:0]`, and that point is an ordinary node.
  - The rank-five argument in §4 of the proof is correct: if A† used at most 4 directions, the
    parameter differential would have rank at most 20+10 = 30 < 35.

**Controls for the exclusion from K.** These are COMPUTED at one explicit point each and serve as
sanity checks, not proofs.
- A 3×3 determinant cubic has `rank M₆ = 204`.
- `a·Q₁ + b·Q₂`, whose restriction to the plane is `(x₀²−x₂², x₁²−x₂²)`, has `rank M₆ = 206`.

Both agree with the HAND ceilings of 204 and 206 in §4 of the proof. I checked those ceilings by
hand as well:
- six distinct points impose independent conditions on sextics;
- the conditions are closed in coefficient space;
- two conics in `P²` always meet, so `Σ_Π` is singular.

### 2.3 Exact identities (COMPUTED, symbolic; `IDENTITIES.json`)

All four hold identically in fully generic symbols:
- the `A₃₃ = 0` lift `per = det` with two sign flips, which equals `afh+bfg+cdh+ceg`;
- A26-01's symmetric lift `det diag(l, M_u) = l·per₃(A)`, modulo `u² − 2`;
- the p4 Laurent pencil `z·det N_s = z(w + s²z)Q`, whose limit as `s → 0` is exactly
  `zw(zw + uv + t²)`;
- `det[[kw,a,b],[−c,w,0],[−d,0,w]] = w(kw² + ac + bd)`.

### 2.4 Hand audit of the arguments

**1a map.**
- The partition (i)/(ii)/(iii) is disjoint and exhaustive.
  - `K = D35 ∪ Σ_Π` consists of singular cubics, including 0, so (i) and (ii) are disjoint.
  - The alternative-factorization lemma is correct: if `l′` divides `C`, then `C` contains a
    hyperplane, so `C ∈ K`. The criterion therefore does not depend on which factor is taken as
    padding.
- READ against B23-03 at `3bcad666`, Theorem 2.1: `closure(D45° ∩ P5) = T1 ∪ T2` with
  `T1 = l·D35` and `T2 = l·Σ_Π`, and every direct point falls into T1 or T2. This supports class
  (i) and the "no literal point" statement for class (iii) exactly as used.
- Dimensions (HAND):
  - class (i) lies between 45 and 49, from the `A₃₃ = 0` family, the `l = 0` family and the
    complement of (ii);
  - class (ii) is open dense, dimension 50;
  - class (iii) has dimension 49. The lower bound comes from the one-node discriminant being
    smooth, plus the submersion `dΦ` of rank 35, minus the closed set `Φ⁻¹(K)`.
- The producer correctly leaves class (iii)'s *closure* membership open and does not claim
  noncontainment there.

**1b.**
- The smoothness certificate is an exact spanning certificate for the Jacobian ideal. Here it is
  replayed, and independently re-certified with two fresh primes and no fixed rows.
- READ: A26-02R at `6dea55ec` accepts the smooth-cubic exclusion "for every smooth complex cubic
  threefold and every nonzero linear form". It also says explicitly that it "does not validate
  B17-01's actual-padding witness". Together, B27-01 and this review now supply that validation.
  `F* = x₀·C* ∉ D₄,₅`.
- Genericity: a nonzero minor is a Zariski-open condition, so a general permanental cubic is
  smooth. ACCEPT.

**1c.**
- READ, checked against source:
  - B19-02 §8.1: `I(D45)_d = 0` for d ≤ 5, so `d(T*) ≥ 6`.
  - B18-01 Theorem 3.5: Lemma A is pointwise at any `[F] ∉ P(D45)`. It applies at `F*`, with C1
    in place of 01-C, and gives `d(T*) ≤ δ₄₅ ≤ 4⁴⁹`, conditional on refined Bézout.
  - Paper 3 C12/C34: `δ₀ ≥ 8` only given the batch-13 identity; the unconditional bound is 6.
  - Cap note table: n=3 has minor size 65 on `M₄`; n=4 has 300 on `M₇`.
  - Application 3: ceiling 245, proved; floor 299, CERTIFIED-modular.
- HAND: the restriction argument `g(C) = h(x₀C)` gives `d(T*) ≥ onset I(K) ≥ onset I(D35)`.
- HAND: the 245 proof is correct. `J_{lC} ⊆ (l, C)`, and `dim(S/(l,C))₇ ≥ 120 − 35 = 85`.
- The table separates what applies at `T*` from what does not: 65, 245, 299 and 300 are not upper
  bounds on `d(T*)`. ACCEPT.

**p4.**
- Class (i) through `Σ_Π` holds, because `wQ` contains a hyperplane.
- The explicit pencil is verified in §2.3.
- The reading of B26-02 ("neither" means neither smooth nor a literal symmetric permanent) is
  READ-confirmed at `cdf6839c` §4, which says "I do not decide whether p₄ ∈ D".

## 3. Verdicts

| claim | producer level | verdict |
|---|---|---|
| 1a: certified three-way map; dim(i) ∈ [45,49], dim(ii) = 50, dim(iii) = 49; closure membership of (iii) left open | READ+HAND+COMPUTED | **ACCEPT** |
| 1a: `A₃₃ = 0` literal family (45 parameters); symmetric family (35) | HAND/READ | **ACCEPT** (identities COMPUTED, §2.3) |
| 1a: A† is a one-node, irreducible cubic outside K; rank-five frame | COMPUTED+HAND | **ACCEPT** (independent 2-prime re-certification) |
| 1a/§6: `p4 = zw(zw+uv+t²) ∈ D45` in closure; every `l·w·Q ∈ D45` | READ+HAND | **ACCEPT** |
| 1b: `C* = per₃(A*)` smooth over Q and `F̄₆₅₅₂₁`; `T*` rank 5; `F* ∉ D₄,₅` via C1; general permanental cubic smooth | READ+COMPUTED+HAND | **ACCEPT** |
| 1c: `6 ≤ d(T*) ≤ 4⁴⁹` (upper bound conditional on refined Bézout); `[8, 4⁴⁹]` given batch-13; 65/245/299/300 are not upper bounds | READ+HAND | **ACCEPT** |
| Run 2 retained negative (rank 203, `A₃₃ = 0` input in class (i)) | COMPUTED+HAND | **ACCEPT** as recorded |

**Nit (wording only; no verdict change).** Report §1a says "the B27 acceptance of C1". C1 is
listed in `B27_COMMON.md` as "Accepted, cross-lineage (**Batch 26**)". "The acceptance of C1
recorded in B27_COMMON" would be exact.

## 4. Achievement level and limits

- **Four achievements.**
  - No source condition.
  - No coefficient equation.
  - No separation on padding.
  - No positive multiplicity gap.
- **Further label.** Geometric noncontainment at an explicit actual-padding point is **accepted**.
  - It is not new: it is the B17-01 witness combined with C1, now validated at witness level.
- **Degree window.** The window is bookkeeping, not an asymptotic bound.
- **Binding constraint.** Unchanged: "No five-row determinant equation is known to be nonzero on
  padding."
- **A25-10.** "No construction ready" stands.

**Compute.** I used 5 of the 10 allowed runs, all sequential and each under 60 s and 512 MB; see
`results/b27_01r/RESOURCE_RECEIPT.md`. Everything computed here is labelled **COMPUTED**, never
PROVED.

**What this review did not do.** No equation search, subagent, installation, or edit to any paper,
ledger or seal. No other branch was touched.
