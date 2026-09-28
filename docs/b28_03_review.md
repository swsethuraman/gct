# B28-03 — cross-lineage check of R27-K4's any-degree lemma

**Registered outcome: ACCEPT.** **HAND:** R27-K4's transfer lemma is valid over C for every integer form degree `d>=1`, every `1<=r<=N`, every coefficient degree `delta>=0`, and every partition `lambda` of `d*delta` with at most `r` parts. No new hypothesis on the form is needed. The verdict rests on the hand derivation below; finite exact checks are labelled **COMPUTED**.

| Rung | Outcome | Evidence and scope |
|---|---|---|
| 3a — bindings | PASS | **READ:** the stipulated manifest and all five payloads match their raw committed bytes, and are unchanged at the merge |
| 3b — locate and state | COMPLETE | **READ:** exact quotations and the complete section 2.2 extract; every `eq:lengthred` occurrence in the prescribed Paper 2 revision inventoried |
| 3c — check | ACCEPT | **HAND:** R1–R6 hold at every positive form degree; **COMPUTED:** original support replayed byte for byte, and explicit quartic/cubic symbolic tests pass |

**HAND — achievement level:** transfer of highest-weight spaces, ideal multiplicity spaces, and coordinate-ring multiplicities only. This yields no new determinant source condition, determinant coefficient equation, separation on padding, positive multiplicity gap, geometric noncontainment witness, cell-existence result, or asymptotic bound. **READ — standing constraint:** "No five-row determinant equation is known to be nonzero on padding." **READ — programme decision:** "no construction ready."

## 0. Preflight and provenance

**READ — administrative observations:** fresh Astra session, with no prior exposure to R27-K4's production; no subagents or other sessions. Branch `b28-03` had clean tracked and untracked status at `b0863403798832668d114f177e672738f1e8be57`, exactly its PART 27 setup commit. The three output patterns were absent before work. No applicable `AGENTS.md` was found in the worktree or its ancestor chain. `PREFLIGHT.json` records these observations.

**READ — raw administrative file hashes:** these hashes name complete filesystem bytes, including their original line endings, not Git blobs or parsed text.

| File | Raw SHA-256 |
|---|---|
| B28_COMMON.md | `06799a9e404fc45a0944f7fcae88d8dd5511f7721f704ebe69872dd3061c87b9` |
| B28-03.md | `57adf8a3937f01dfdebd46e2223b878b66c9b45932f36ca00f854e92cda2ef59` |
| BATCH28_BOARD.md | `c635ac1a73e5e0c855c9bc1b75809c447e3b7184d707af75d49bad6c14ba96af` |

**READ — bindings:** `results/b28_03/INPUT_BINDINGS.json` contains resolved commits, Git blob IDs, byte counts, raw SHA-256 values, EOL counts and read scopes. All mathematical source text used here is from the pinned committed blobs. No third-party source was obtained or committed.

| Input | Raw SHA-256 of committed blob |
|---|---|
| `53206b43:results/b27_k4/MANIFEST.json` (998 bytes) | `d63c535f68c35f5e0a959be8fcd88c78db9a3501d69c48c8d51269cb2ac4555e` |
| `53206b43:docs/b27_k4_review.md` (14578 bytes) | `4d801f0836320b0910eaddb352066d20fa14ca6ea7feb7749a24a5117699468e` |
| `53206b43:analysis/b27_k4_hwv_check.py` (5659 bytes) | `6597670d3a68af2dbca8bedb970aca95115703ee167318ddf2664da1a75de928` |
| Each archived run output (9166 bytes, CRLF) | `cae16ecf22d1f63cf0f7b526559ebd726609df8629afe18a1a9f89a8948e03ab` |
| `53206b43:results/b27_k4/resource_receipt.json` (1548 bytes) | `4f31bf1e916a02d3bdf2e96795ee4cf9c7f239cf9e17122472681b209959a5c6` |
| `21816b3c:docs/b26_10a_review.md` | `9fa55d57c501c8e65275732563f42d4eb9e1eae76ad0d09956844b0576b7eb1d` |
| `f8326974:paper/det4-onset.tex` | `36bcce5f8c79ab4ea55e24b67fdd19a1f15e932a7b46e77fc9438fbe1254bd4a` |
| `96a8074d:docs/batch_closes/BATCH27_CLOSE.md` | `0e55ca6bc2152a77c3e882a35395a2eaaf6cc128dd0cf5c6e63678da7678bd35` |

**READ — rung 3a:** the manifest hash is the brief's exact value. Every listed payload's SHA-256 and byte count matches `git show 53206b43:<path>`; the manifest and five payloads are byte-identical at `96a8074d`. The replay source is an unchanged copy of the committed script, under this slot's authorized script prefix.

## 1. Exact object under review — rung 3b

**READ — R27-K4 section 1, conventions (verbatim):**

> - Forms `F ∈ W_N = Sym^d((C^N)*)`, with `(g·F)(v)=F(g⁻¹v)`.
> - The coefficient functional is `c_α(F)=[y^α]F`, with `|α|=d`.
> - Functions carry the dual action.

**READ — section 2.1 supplies the statement that section 2.2 extends (verbatim):**

> The claim covers any `f ∈ Sym⁴((C¹⁶)*)`, any `1≤r≤16`, `δ≥0` and `λ⊢4δ` with `ℓ(λ)≤r`. Write `X=closure(GL₁₆·f)`, `X_r=closure{f∘T : T∈Hom(C^r,C¹⁶)}` and `ρ` for restriction.
>
> The claim is that pullback `ρ*` does three things:
> - it identifies the highest-weight spaces of weight `(λ,0)` and `λ`;
> - it identifies their ideal subspaces;
> - so `mult_λ C[X]_δ = mult_λ C[X_r]_δ`.

**READ — section 2.2 opening, hypotheses and degree range (verbatim):**

> I prove the degree-`d` form, which contains the degree-four statement. Let `f ∈ Sym^d((C^N)*)`, `d≥1`, `1≤r≤N` and `λ⊢dδ` with `ℓ(λ)≤r`.

**READ — section 2.2 conclusions and endpoints (verbatim):**

> - So `HWV^N_{(λ,0)} = ρ* HWV^r_λ`, with no boundary loss at `ℓ(λ)=r`.

> 5. **R5: ideal kernels.** For `h=ρ*h̄`: `h∈I(X)` ⇔ `h` vanishes on `GL_N·f` ⇔ (by R3) `h̄` vanishes on `ρ(GL_N·f)` ⇔ (by R4) `h̄∈I(X_r)`. By R2, every highest-weight vector of weight `(λ,0)` has this form, so `ρ*` restricts to `HWV(I(X_r)_δ)_λ ≅ HWV(I(X)_δ)_{(λ,0)}`.

> - Complete reducibility in characteristic 0 gives `mult_λ C[·]_δ = dim HWV(ambient) − dim HWV(ideal)` on each side.
> - Both terms agree by R2 and R5.

> For `δ=0` the claim is trivial. `f=0` is allowed; both sides are then `{0}`.

> **Conclusion.** B26-10A's degree-four statement is correct as stated. Every step also holds verbatim for any degree `d`, which §4.1 needs. B26-10A's R6 uses fourth roots, and the degree-`d` form uses `d`-th roots. **ACCEPT.**

**READ:** the complete section 2.2, without edits or omissions, is also included as `results/b28_03/R27_K4_SECTION_2_2_EXACT.md`, extracted directly from the committed bytes. The assertion is presented through section 2.1's statement and section 2.2's generalization, rather than as a separately numbered theorem. The coefficient-degree range `delta>=0` is inherited explicitly from section 2.1; section 2.2 separately treats `delta=0`. "Any degree" means every positive form degree `d`, and every nonnegative coefficient degree `delta`.

**HAND — consolidated accepted statement:** put `V_m=C^m`, `W_m=Sym^d(V_m*)`, `A_m=C[W_m]`, and use the above dual action on coefficient functions. Let `iota:V_r -> V_N` be the first-coordinate inclusion and `rho(F)=F∘iota`. For any homogeneous `f` of degree `d>=1`, set

`X=closure(GL_N·f)`, `X_r=closure{f∘T : T in Hom(V_r,V_N)}`.

**HAND:** for `delta>=0`, `lambda ⊢ d*delta`, `length(lambda)<=r<=N`, pullback gives isomorphisms of the ambient highest-weight spaces and their ideal subspaces, with zero-padding of `lambda` to `N` coordinates, and therefore equality of the same-partition coordinate-ring multiplicities. This concerns highest-weight/multiplicity spaces, not an isomorphism of full irreducible representations of groups of different ranks. All closures here are affine Zariski closures over C.

## 2. Independent hand check — rung 3c

### R1 and R2: coefficient support and raising kernels

**HAND:** for diagonal `t`, the dual action on `c_alpha` is `t^alpha c_alpha`. Thus `A_m,delta = Sym^delta(Sym^d V_m)` has coefficient-monomial weights equal to sums of nonnegative multi-indices. A monomial of weight `(lambda,0^(N-r))` cannot involve a coefficient with a positive tail exponent: no negative factor exponent exists to cancel it. This proves equality of the weight bases under `rho*`. The map is injective because it includes a polynomial subring.

**HAND:** for `g=I+tE_ij`, the dual action reads the coefficient of `y^alpha` in `F(gy)`. A term with exponent `beta` contributes to the derivative only when `beta=alpha+e_i-e_j`, and its coefficient is `beta_i=alpha_i+1`. Hence

`E_ij c_alpha = (alpha_i+1)c_(alpha+e_i-e_j)` if `alpha_j>0`, and `0` otherwise.

**HAND:** this uses ordinary coefficients, not divided-power coefficients. For each simple positive root `E_(i,i+1)` with `i<r`, the operator intertwines with pullback. For `r<=i<N`, it kills each included generator because its `(i+1)`st exponent is zero, and it kills every product by the derivation rule. Consequently all raising kernels agree, including the boundary root `i=r` when `r<N`. Equality remains valid at `length(lambda)=r`; no extra zero part inside the first `r` coordinates is assumed. The simultaneous kernels in the dominant-weight spaces are precisely the highest-weight spaces.

### R3 and R4: evaluation and closure

**HAND:** `c_alpha(rho(F))=c_(alpha,0)(F)` is an identity of coordinate functions. It extends multiplicatively and linearly to every coefficient polynomial: `(rho*h)(F)=h(rho(F))`.

**HAND:** `rho(g·f)=f∘(g^{-1}iota)`. As `g` varies, `g^{-1}iota` ranges over exactly the injective linear maps `V_r -> V_N`: an independent `r`-tuple can be extended to an `N`-element basis. This is where `r<=N` is used. Full-rank matrices form a nonempty dense open subset of the irreducible affine space `Hom(V_r,V_N)`.

**HAND:** the map `Phi(T)=f∘T` is polynomial. If a coefficient polynomial `q` vanishes on `Phi(T)` for injective `T`, then the polynomial `q∘Phi` vanishes on a dense subset of an affine space, hence identically. Thus

`closure(rho(GL_N·f)) = closure(Phi(Hom(V_r,V_N))) = X_r`.

**HAND:** also `closure(rho(X))=X_r`. One can check this without an assertion that images of closed sets are closed: `q` vanishes on `rho(X)` exactly when `q∘rho` vanishes on `X`, exactly when it vanishes on its dense orbit. Thus the two images have the same vanishing ideal and the same closure. In particular, no dense orbit in `X_r` is assumed.

### R5 and R6: ideal kernels, grading and multiplicities

**HAND:** for every `h` in `A_r`, R3–R4 give

`rho*h in I(X) <=> h in I(X_r)`.

**HAND:** this equality holds before restricting to highest weights; restricting it using R2 gives the required ideal highest-weight-space isomorphism. Injectivity ensures that a nonzero transferred highest-weight vector stays nonzero.

**HAND:** since `d>=1`, scalar matrices act on forms by `t^{-d}`, and the nonzero `d`th powers cover `C*`. Hence `X` is invariant under nonzero scalar multiplication; being nonempty and closed, it contains zero and is a cone. Similarly `Phi(tT)=t^d Phi(T)`, and `T=0` gives zero. Precomposition `T -> Th^{-1}` for `h in GL_r` shows that `X_r` is `GL_r`-stable. Both ideals are homogeneous, so each coefficient-degree quotient is a finite-dimensional polynomial representation.

**HAND:** over C these representations are completely reducible. In each degree and each group, the multiplicity of the irreducible of highest weight `lambda` equals the dimension of its highest-weight space. Applied to the ambient representation and its homogeneous ideal, this gives

`mult_lambda C[X]_delta = dim HWV_lambda(A_N,delta) - dim HWV_lambda(I(X)_delta)`,

and the analogous formula for `X_r`. Both terms match by R2 and R5. This proves the asserted multiplicity equality. It does not assume reduced orbit boundaries beyond the usual reduced closed variety and its vanishing ideal.

### Hypothesis audit and edge cases

| Question | Finding |
|---|---|
| Hidden use of four? | **HAND:** none. The size of each exponent multi-index is `d`, and the only root extraction is a `d`th root in C. No fourth-order identity enters. |
| Hidden property of det4? | **HAND:** none. No matrix realization, irreducibility, smoothness, stabilizer, essential-variable count, or special orbit dimension is used. Any homogeneous `f`, including zero, is allowed. |
| Degree one? | **HAND:** a nonzero linear form has orbit all nonzero linear forms and closure `W_N`; the restricted closure is `W_r`. Degree-`delta` coordinate rings have only the one-row highest weight `(delta)`, as required. |
| Coefficient degree zero? | **HAND:** both varieties are nonempty; their degree-zero rings are C and their degree-zero ideal parts are zero. The empty partition is allowed. |
| f=0? | **HAND:** both varieties are `{0}`. Their positive-degree coordinate rings vanish; ambient and ideal highest-weight spaces agree. |
| r=N or r=1? | **HAND:** for `r=N` restriction is the identity and the invertible substitutions are dense; for `r=1` all additional raising operators kill the one-coordinate coefficients. |
| Beyond stated hypotheses? | **HAND:** no extension to positive characteristic, nonhomogeneous forms, `r>N`, or form degree zero is asserted. For nonzero constant forms, the ordinary cone/grading step in this statement fails. |
| GL versus SL? | **HAND:** fix the polynomial GL representative of size `d*delta`; the length condition applies to this representative. An arbitrary determinant twist of an SL label is not interchangeable. |

**HAND — verdict on the proof:** every step R1–R6 is valid in the stated range. No repair of the any-degree lemma is required.

## 3. Quartic specialization and one further case

**READ:** B26-10A section 2.3 states the general quartic result for `N=16`, all `1<=r<=16`, all `delta>=0`, and all eligible `lambda`, with arbitrary quartic `f`. **HAND:** substituting `d=4,N=16` in section 2 above gives exactly that result, including the ideal-kernel statement. At its principal determinant cell, `r=9`, `delta=24`, `lambda=(65,17,2,2,2,2,2,2,2)`, the size is `65+17+7*2=96=4*24` and the length is nine. Thus the accepted quartic case is recovered without changing conventions.

**HAND — explicit non-determinant tests:** choose `N=3,r=2,delta=2,f=x_1^d`, first `d=4` and then `d=3`. These also test the boundary `length(lambda)=r` and a form with fewer essential variables than `N`. Its orbit consists of nonzero `d`th powers of linear forms; equations vanishing on these extend to the orbit closure. On restriction, `f∘T=(a x_1+b x_2)^d` with `a,b` arbitrary.

**HAND:** let `c_j` denote the coefficient of `x_1^(d-j)x_2^j`. At weight `lambda=(2d-2,2)`, the only coefficient-degree-two monomials are `c_0 c_2` and `c_1^2`. The raising map on their span is the one-row matrix `[d-1,2d]`, so the highest-weight space is one-dimensional, generated by

`h_d = 2d c_0 c_2 - (d-1)c_1^2`.

**HAND:** this polynomial is nonzero, and substituting `c_0=a^d`, `c_1=d a^(d-1)b`, `c_2=binom(d,2)a^(d-2)b^2` gives zero identically. Hence the entire highest-weight line is in the restricted ideal. The same expression in the first two variables, with all tail exponents zero, is a nonzero highest-weight equation of the ambient power locus. On each side the ambient multiplicity is one, the ideal multiplicity is one, and the coordinate-ring multiplicity is zero. This tests a nontrivial ideal kernel without random evaluation or sampled nullspaces.

| Form degree | Weight | Explicit equation | Result |
|---|---|---|---|
| 4 | `(6,2)` | `8 c_0 c_2 - 3 c_1^2` | **HAND:** nonzero HWV, in both corresponding ideals |
| 3 | `(4,2)` | `6 c_0 c_2 - 2 c_1^2` | **HAND:** nonzero HWV, in both corresponding ideals |

**COMPUTED:** `analysis/b28_03_cases.py` checks the raising residual, the symbolic substitution residual, the exact rational one-dimensional kernel and a nonzero-polynomial control for both cases. Both residuals are zero in both cases. `cases_output.json` records the exact matrices and vectors. The general theorem and ideal interpretation remain **HAND**; these finite identities are corroboration only.

## 4. Paper 2 coverage at the requested revision

**READ:** this inventory uses `f8326974a1454ac83a925860635e29bbfaf5d5c7:paper/det4-onset.tex`, with lines counted on the committed CRLF blob. Its four `eqref{eq:lengthred}` references occur at 712, 867, 895 and 1067; the equation label occurs at 257. R27-K4's older line numbers are not silently reused.

| Paper 2 locator | READ: use | HAND: coverage of the accepted lemma |
|---|---|---|
| 251–262; equation 257–259 | Equality for a 16-variable quartic orbit closure and its restrictions, with determinant and padded-permanent identifications | `d=4,N=16`, any `delta`, `length(lambda)<=r<=16`. Taking `f=det4` or `x0 per3` gives the two named families. |
| 712–713 (formerly 705–706) | Cap-proof ending carries the GL5-stable minor span into `I(O)` | At every `n>=3`, take `d=n,N=n^2,r=5`; then `5<=n^2`. The ideal-kernel transfer lifts each nonzero highest-weight line, preserving its coefficient degree `cap(n)`. |
| 867–868 (formerly 860–861) | Both reduced multiplicities equal their 16-variable orbit-closure versions | Quartic case for each admissible `k=length(lambda)<=16`; applies to both named forms. |
| 895–901 (formerly 888–894) | Short-slab transport to `P_k,D_k` | Quartic case for `k<=4`. The ensuing containment and washout inputs are separate. |
| 1067–1073 (formerly 1060–1063 plus later inserted explanation) | Transfer the LMR copy to `D_9` | `d=4,N=16,r=9,delta=24,lambda=(65,17,2^7)`. Conditional on the stated nonzero orbit-ideal copy, its transfer remains nonzero. |

**HAND:** the new reach beyond the accepted quartic result is precisely the cap-proof transfer for `n=3` and `n>=5`. At `n=2`, `N=4<5`, so this lemma does not apply with `r=5`; **READ:** the proof has already treated `n=2` separately at lines 671–675, before the branch containing lines 712–713. Thus this is not an uncovered use of the lemma in that paragraph.

**READ:** `O` in section 2 is a quartic object; the last clause of the cap proof still writes `I(O)`. **HAND:** the unambiguous any-degree target is `I(closure(GL_(n^2)·det_n))`, for `n>=3`. A precise statement of the accepted transfer there is: each highest-weight vector in the indicated GL5 ideal submodule pulls back to a nonzero highest-weight vector in that orbit-closure ideal. Its GL_(n^2)-span lies in that ideal. There is no assertion that full GL5 and GL_(n^2) irreducibles have equal dimensions.

**HAND — editorial implication only:** L2's mathematical review condition is satisfied for this lemma. A future editorial pass may cite its accepted positive-degree form and name the general orbit closure explicitly instead of restricting that clause to `n=4`. This slot edits no paper, ledger, or seal and makes no independent ruling on other cap-theorem inputs. **READ:** the theorem statement at 663–667 concerns `I(D_5)`, not this concluding orbit-ideal clause.

**READ/HAND:** the introductory transfer summary at 105–122 is also covered. The later claims at 1090–1097 use the transferred LMR ideal copy as one input; accepting the lemma clears only that transfer. It does not certify the existence of the external LMR copy, rank 273, the ambient count 274, the one-dimensional-kernel conclusion, or any padded residues. These claims require their own evidence.

**HAND:** for the two quartic family identifications, an arbitrary map into `M_4` specifies all pencil matrices, and an arbitrary map into the 16-coordinate padded-permanent space specifies its ten relevant linear forms independently as choices. The density argument includes rank-deficient substitutions. No arbitrary cubic is substituted for the permanent factor by this lemma.

**READ/HAND — incidental wording, outside the any-degree verdict:** R27-K4 section 3 says that the ten linear forms are necessarily dependent "including `r≥10`". Necessary linear dependence is for `r<10`; at `r>=10` they can be independent or dependent. This sentence is not used by R1–R6 or by the family-identification argument, which allows all choices. It does not require a repair of the transfer lemma.

## 5. Exact replay and resource scope

**READ — code audit:** the original script exhaustively enumerates coefficient exponent vectors and monomials in its listed small cells. Check A uses symbolic differentiation of the coefficient action. Check B uses integer raising matrices and SymPy exact rank, not a floating-point rank or sampled nullspace. Its omission of raising blocks for zero tail weight is justified by R1–R2, not independent evidence for that step. Its main routine reports failures rather than raising on them; this slot's runner additionally requires the entire replay to match the archived successful output hash.

**COMPUTED — run 1:** the unchanged source replay gives zero mismatches in all three Check A cases `(N,d)=(3,4),(3,3),(2,5)`, and `123/123` Check B cells pass. The complete raw stdout is byte-identical to both original outputs: SHA-256 `cae16ecf22d1f63cf0f7b526559ebd726609df8629afe18a1a9f89a8948e03ab`. This replay covers all distinct COMPUTED support in R27-K4, including its cubic and quintic cells. It does not establish a general theorem by extrapolation.

**COMPUTED — run 2:** the two explicit symbolic tests in section 3 pass. Raw stdout SHA-256 is `c3fa11d246f6c779aec6cf9a3eee5efe3cdc0ad22c4dbfbb8beeeb16b54306bc`.

**READ — resource administration:** two mathematical runs were used, sequentially, with existing Python 3.12.10 and SymPy 1.14.0. No installations occurred. The runner applies a Windows Job Object with a 512 MiB hard process/job memory cap before executing the mathematical script; the supervising process enforces a 60-second timeout. Both runs stayed well below the limits. `results/b28_03/resource_receipt.json` logs commands, individual source hashes, aggregate input hashes, output hashes, wall times and memory readings. Wall-clock and peak-memory fields appear only in the receipt, never in certificate stdout. The administrative binding/sealing script performs no mathematical computation.

**READ — delivery scope:** all new scripts are `analysis/b28_03_*`; all other outputs are this review and `results/b28_03/`. The manifest binds all payload raw bytes and byte counts, excluding itself. Only these explicit paths are staged for the single slot commit; filter parity is checked before staging. Delivery follows the authorized common instructions on `b28-03` alone.

**UNREAD:** Companion Proposition 4.19, the external LMR proofs, and the cap theorem's external inputs were not re-read in this slot and supply no premise for the hand proof above. **HAND:** this acceptance is limited to the transfer lemma and its identified uses, with no change to the binding constraint or programme decision.
