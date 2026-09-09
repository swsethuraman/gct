# Batch 12 S5 — Sol scaling and successor economics

**Frozen bounded research result, 8 September 2026.** The exact S5 rank was not attempted. The ambient and precursor multiplicities, the complete horizontal-strip topology, circuit-state formulas, and implementation memory gates were computed. The present dense/streamed compact-recursion implementation is **KILL at this cell under a 7 GiB working-memory cap**; this is an implementation verdict, not a mathematical impossibility.

## 1. Outcome and inherited preregistration

The inherited working hypothesis was that compact architectures may remain useful at `n=5`, but that polynomial growth in growing `n` was unproved. I treated it as falsifiable as follows:

* accept the local architecture only if the 10-box recoupling data remain small;
* accept the full recursion only if exact `B`, a rigorous two-step lower bound, and the resulting streamed workspace fit 7 GiB;
* accept circuit evaluation only with an explicit width parameter and measured widths;
* accept rank work only after an evaluation-compatible source bridge passes the `n=4` control.

The result is split:

* **CERTIFIED:** `a_40=17,107` and the stable one-block precursor is `B_infinity=176,452`, by five-prime CRT with a modulus larger than explicit integer upper bounds.
* **PROVED:** the only finite-degree correction to that stable precursor is one, so `B_40=176,451`. Also `a_39=17,106` on the same-tail predecessor; the final ladder birth is exactly one.
* **EXACT:** 15 one-step channels, 250 two-step paths, 54 two-step endpoints, 42,533 DAG nodes including the root, 671,954 edges, and a peak of 1,661 shapes.
* **PROVED BOUNDS:** `335,795 <= C_residual <= 74,751,595,281,621,450,111,525,280,503,168,606,052` and `219,389 <= C_total <= 1,174,423,147,197,921,157,033,130,265,269,775,689,251`. The upper bounds are intentionally coarse stable-weight bounds.
* **KILL for the current implementation:** the lower bound alone forces at least 441.46 GiB for a full `C_residual by B` residual, or 231.97 GiB for the streamed `B^2` workspace. A dense `B by a` inclusion is 22.49 GiB. These exclude object overhead and a second prime.
* **MEASURED:** 325 deterministic random filling probes gave greedy open-edge widths `W=2,3,4` with counts 92, 201, 32. The evaluator's two main arrays therefore use 256 MiB, 512 MiB, or 1 GiB at `h=11`. Optimal pathwidth and runtime remain open.
* **OPEN:** exact `C_residual`, `C_total`, `C_peak`, weighted edge work, the compact arbitrary-permutation/evaluation bridge, and every determinant or padded-permanent rank at this cell.

The dominant cost is not the local 10-box block or a single circuit evaluation. It is global multiplicity-space recoupling, source conversion, and basis/rank enumeration.

The machine-readable ledger is [S5_cost_ledger.json](C:/Users/swami/Projects/gct-gpt/Batch12_Results/S5/S5_cost_ledger.json).

## 2. Inputs, authority, and execution boundary

The controlling brief, launch packet, and all four canonical sources were read. The final proposal's WordprocessingML paragraphs and tables were extracted with `python-docx`. The packaged renderer could not perform the optional visual render because LibreOffice/`soffice` was unavailable; no content was inferred from page appearance.

| Input | SHA256 | Status |
|---|---|---|
| [S5 brief](C:/Users/swami/Documents/Codex/2026-09-08/referenced-chatgpt-conversation-this-is-an-2/outputs/S5_Sol_Scaling.md) | `fbab9349f12775f368a9a8791c1408ca2fe0a0e83b3f30b241bc07225cccf7b6` | Read in full |
| [Launch packet](C:/Users/swami/Documents/Codex/2026-09-08/referenced-chatgpt-conversation-this-is-an-2/outputs/Batch12_Launch_Packet.md) | `0260544ac0617cbdcac64dfc0d61a63f1e678a12a4759703adc1605e9d4a64f2` | Read in full |
| [Final proposal](C:/Users/swami/Projects/gct-gpt/Batch12_Reconciled_Final_Proposal.docx) | `29420ce4daac421133c7d1abce9960ca2d6b1d8979426004e03986ea08726718` | Text and tables extracted |
| [Final stock-take](C:/Users/swami/Projects/gct-gpt/batch11_final_stocktake.md) | `896e1aacdeb9aa744f15a2f933f65c580703d7dd343878e697c3538ba330b4cd` | Read in full |
| [Detailed stock-take](C:/Users/swami/Projects/gct-gpt/stocktake_batch11.md) | `ba016a8ebbe8abd4a0da87a8c8da267bfe7d5d12e3624b46c3eee4dce1f157e6` | Read in full |
| [Comprehensive source](C:/Users/swami/Projects/gct-gpt/GCT_Comprehensive_Session_Source.md) | `09b535b717333c2b2540ddc38e56252abf09f776a23413af245263c2aaf6ba68` | Read in full; historical corrections applied |

The durable checkout [gct work](C:/Users/swami/Projects/gct/work) was read-only and clean at local `HEAD=main=cached origin/main=afb8c3319d3d1f3afc3d2578c8cb322f2b8a3b92`. A fresh `git ls-remote` failed because this environment could not connect to GitHub, so this run makes no live-remote PASS claim. The independent computations are new scripts in this isolated output and do not modify the checkout.

Later workspace reports were also incorporated:

* [S1 report](C:/Users/swami/Projects/gct-gpt/Batch12_Results/S1/S1_report.md): proves the birth quotient and supplies ten evaluation-ready target vectors, but no complete source or conversion.
* [S2 report](C:/Users/swami/Projects/gct-gpt/Batch12_Results/S2/S2_report.md): proves partial `r=5` geometry and exact chart fallbacks; global noncontainment remains open.
* [S3 report](C:/Users/swami/Projects/gct-gpt/Batch12_Results/S3/S3_report.md): proves and implements the compact spherical operator and the `31 -> 2` dimension control; the four control pairing coefficients and target evaluation bridge remain open.
* [S4 report](C:/Users/swami/Projects/gct-gpt/Batch12_Results/S4/S4_report.md): certifies only `rank(T_pad)>=12`; padded rank 274, determinant rank 273, and `D(24)` remain open.

The requested Documents destination is outside the writable roots and was absent. Results are staged in [this isolated S5 directory](C:/Users/swami/Projects/gct-gpt/Batch12_Results/S5). No canonical file, shared checkout, schedule, external message, rank state, or prior report was changed.

## 3. Exact cell and multiplicity definitions

Work over `Q`, extending scalars to `C` for representation-theoretic statements. Fix

\[
n=5,\qquad \delta=40,\qquad
\lambda=(151,31,2^9),\qquad |\lambda|=200=5\cdot40.
\]

Its length is 11 and its conjugate is

\[
\lambda'=(11,11,2^{29},1^{120}).
\]

Let `L_d` be the distinct partitions reached at degree `d` by recursively removing horizontal 5-strips from `lambda`. Put

\[
a_d(\mu)=\dim\operatorname{Hom}_{S_{5d}}
  ([\mu],\mathbf 1\!\uparrow_{S_5\wr S_d}^{S_{5d}}).
\]

The priced quantities are

\[
\begin{aligned}
a&=a_{40}(\lambda),\\
B&=\sum_{\lambda/\mu\in HS_5}a_{39}(\mu),\\
C_{\rm residual}&=\sum_{\lambda\to\mu\to\nu}a_{38}(\nu),\\
C_{\rm total}&=\sum_d\sum_{\mu\in L_d}a_d(\mu),\\
C_{\rm peak}&=\max_d\sum_{\mu\in L_d}a_d(\mu),\\
W_{\rm edge}&=\sum_{(\mu\to\nu)\text{ DAG edge}}a_{d-1}(\nu).
\end{aligned}
\]

`C_residual` counts a two-step endpoint once for every path through a one-step predecessor; it is not the distinct degree-38 layer total.

## 4. Certified `a` and `B`

Write `rho=(31,2^9)`, of size 49. The stable ambient coefficient is

\[
[S^\rho]\,\operatorname{Sym}
 (\operatorname{Sym}^2\oplus\operatorname{Sym}^3
  \oplus\operatorname{Sym}^4\oplus\operatorname{Sym}^5).
\]

The independent engine performs Weyl alternation over multiset weight multiplicities. It used five trial-division-verified primes

```text
2147483647, 2147483629, 2147483587, 2147483579, 2147483563
```

and returned residue 17,107 at every prime. Their product is

```text
45671921168693645933699105804560590380377589537
```

which exceeds the explicit ordered-sequence upper bound

```text
26661962020138904060787601545021881610.
```

The finite-degree audit checked 2,187 Jacobi-Trudi/Pieri truncation pairs. Its minimum factor-count slack is zero, so the stable coefficient is already exact at degree 40:

\[
\boxed{a=17,107}.
\]

The one-block stable precursor is the coefficient in

\[
R\otimes(h_0+h_1+\cdots+h_5),\qquad
R=\operatorname{Sym}(\operatorname{Sym}^2\oplus\cdots\oplus\operatorname{Sym}^5).
\]

The same five-prime calculation gives `B_infinity=176,452`. Fourteen of the fifteen one-step predecessors are finite-stable at degree 39. The sole failure is `(146,31,2^9)`. Its only excluded top-factor-count contribution is

\[
[S^{(2^9)}]\operatorname{Sym}^9(\operatorname{Sym}^2)=1,
\]

because `Sym^k(Sym^2)=direct_sum_(alpha partition k) S^(2 alpha)`. Therefore

\[
\boxed{B=176,452-1=176,451}.
\]

The same correction gives `a_39(146,31,2^9)=17,106`, hence the last birth `a_40-a_39` is exactly one. Detailed witnesses are in [n5_finite_boundary.json](C:/Users/swami/Projects/gct-gpt/Batch12_Results/S5/n5_finite_boundary.json).

This is an aggregate precursor certificate, not the launch packet's optional twelve-term `B24` second-engine preflight. That optional preflight was not claimed. As controls, the new topology engine recovers the reported `n=4` node/peak counts, and the multiplicity engine recovers `a24=274` and stable `B_infinity=2169`; the known single boundary correction returns `B24=2168`.

## 5. Exact combinatorial topology

| Quantity | `n=4,d=12` control | `n=4,d=24` target | `n=5,d=40` S5 |
|---|---:|---:|---:|
| one-step channels | 3 | 12 | **15** |
| two-step paths | 36 | 160 | **250** |
| two-step distinct endpoints | 23 | 42 | **54** |
| maximum paths per endpoint | 3 | 10 | **13** |
| nodes below root | 921 | 7,656 | **42,532** |
| nodes including root | 922 | 7,657 | **42,533** |
| total DAG edges | 7,790 | 88,302 | **671,954** |
| peak shapes | 189 | 585 | **1,661** |

The S5 shape peak begins at degree 30 and remains 1,661 through degree 16. The maximum edge count is 26,916 on a transition out of degree 30 and on the following plateau transitions. Relative to `n=4,d=24`, S5 has 5.56 times as many nonroot nodes and 7.61 times as many edges, but `a` rises by 62.43 times and `B` by 81.39 times. The topology alone therefore understates the weighted cost.

For the 10-box local recoupling spaces:

| Local quantity | Exact S5 value |
|---|---:|
| `sum c_nu^2`, where `c_nu` is path multiplicity | 1,664 |
| total standard tableaux across 54 skew shapes | 86,784 |
| largest local skew-tableau space | 8,400 |
| `sum t_nu c_nu` | 513,904 |
| conditional seminormal scalar-update upper `25 sum t_nu c_nu` | 12,847,600 |

Thus the local 10-box action remains compact. The 25 factor is the adjacent-swap length of a five-by-five block exchange. This operation count is conditional on generalizing S3's verified eight-box operator to ten boxes; that code was not implemented here.

The complete level and edge ledgers, path multiplicities, and coarse bounds are in [n5_d40_skeleton.json](C:/Users/swami/Projects/gct-gpt/Batch12_Results/S5/n5_d40_skeleton.json).

## 6. Weighted bounds and cost ledger

For the two-step restriction, only the symmetric-group constituents `(delta)`, `(delta-1,1)`, `(delta-2,2)`, and `(delta-2,1,1)` contribute. If their multiplicities are `a,b,c,e`, then

\[
B=a+b,\qquad C_{\rm residual}=a+2b+c+e\ge2B-a.
\]

Hence

\[
\boxed{C_{\rm residual}\ge335,795}.
\]

For a two-step endpoint with tail `x=(x_i)` and `T=sum x_i`, an explicit stable weight-space upper bound is

\[
U(x)=\sum_{k=\lceil T/5\rceil}^{\lfloor T/2\rfloor}
      \prod_i {x_i+k-1\choose k-1}.
\]

It forgets generator-degree constraints and orders each multiset, so it is rigorous but loose. Summing `path_count(nu) U(tail(nu))` gives

\[
\boxed{335,795\le C_{\rm residual}
\le74,751,595,281,621,450,111,525,280,503,168,606,052}.
\]

Five of 54 endpoints are not yet stable at degree 38; their total path weight is only nine. They are enumerated in the boundary artifact. Exact finite corrections at those five shapes, plus the 49 stable endpoint multiplicities, are the minimum data needed for exact `C_residual`.

Because path multiplicity is at most 13, the distinct degree-38 layer has multiplicity sum at least `ceil(335795/13)=25,831`. It follows that

\[
\begin{aligned}
219,389&\le C_{\rm total}
\le1,174,423,147,197,921,157,033,130,265,269,775,689,251,\\
176,451&\le C_{\rm peak}
\le47,764,766,037,916,480,298,686,861,694,550,709,443,\\
512,246&\le W_{\rm edge}
\le1,773,658,888,021,857,749,075,123,716,882,650,779,451.
\end{aligned}
\]

The lower edge-work bound is the exact top contribution `B` plus the two-step lower bound. These are counts of multiplicity coordinates touched, not wall-clock predictions.

The historical `C24 approximately 17,000` ratio would project S5 to about 1.38 million. Multiplying the 250 paths by the top multiplicity gives 4.28 million. These planning anchors disagree by more than threefold and neither is a bound. They are retained only to show why a direct measurement is necessary.

## 7. Recoupling, conversion, and memory

For a node `v`, S3's implemented architecture has operation/storage parameters

\[
\begin{aligned}
\text{local coefficients}&=O(n^2\sum_\nu t_{v\nu}c_{v\nu}),\\
\text{residual assembly}&=O(B_v\sum_\nu a_\nu c_{v\nu}^2),\\
\text{dense elimination}&=O(C_vB_v\min(C_v,B_v)),\\
\text{stored recursive inclusions}&=\sum_v B_va_v\text{ field entries}.
\end{aligned}
\]

Using one 64-bit modular residue per entry and only the proved lower bound for `C_residual`:

| Object | Minimum/exact entries | Bytes | GiB |
|---|---:|---:|---:|
| full top residual `C_residual by B` | 59,251,363,545 minimum | 474,010,908,360 | **441.46** |
| streamed elimination workspace `B^2` | 31,134,955,401 exact | 249,079,643,208 | **231.97** |
| dense inclusion `B by a` | 3,018,547,257 exact | 24,148,378,056 | **22.49** |
| dense source evaluation matrix `a^2` | 292,649,449 exact | 2,341,195,592 | **2.18** |

The current dense elimination formula already has a lower workload of

```text
10,454,962,348,878,795 field operations.
```

This is a lower bound for that implementation formula, not an algebraic complexity lower bound. It kills both full-residual and `B^2`-streamed variants under the 7 GiB cap. A future S5 implementation must be genuinely sparse, endpoint-blocked, black-box, or quotient-first; changing storage syntax while retaining a dense `B`-space is insufficient.

Conversion is a separate blocker. S3 proves the recursive operator and `31 -> 2` dimension control but leaves four arbitrary-permutation pairing coefficients open even at `n=4,d=12`. A sampled basis transform is circular unless the recursive vectors can already be evaluated. Consequently no finite S5 conversion runtime is reported. Before scaling, the four control pairings must be computed under S3's proposed 30-minute/256 MiB gate and checked against the direct circuit basis at both primes.

## 8. Circuit width and peak bytes

At S5, a bracket filling has two height-11 columns, 29 two-columns, and 120 one-columns. Literal coordinate expansion has

```text
(11!)^2 * 2^29 = 855423762759029882880000 terms per filling.
```

It is **KILL**. The mixed-discriminant evaluator would require

```text
2^29 * 2^11 = 2^40 = 1099511627776
```

size-11 determinants per evaluation, also **KILL**.

The exterior evaluator allocates two `uint64` arrays indexed by two height-`h` masks and `W` open-edge bits:

\[
\text{main bytes}=16\,2^{2h+W}.
\]

The deterministic width probe sampled 25 coupling graphs at every tall-column intersection `k=0,...,11` plus 25 unconstrained graphs, with seed 5040 and 50 heuristic restarts per graph:

| greedy width `W` | samples | main array bytes |
|---:|---:|---:|
| 2 | 92 | 256 MiB |
| 3 | 201 | 512 MiB |
| 4 | 32 | 1 GiB |

This is encouraging for evaluating one supplied filling. It is not a proof of optimal pathwidth, a guarantee that the sampled filling is nonzero, a bound on basis-discovery samples, or a runtime extrapolation. The input tensor table is at most about 1.2 MiB under the crude per-letter bound and does not change the conclusion that global source construction dominates.

The exact probe record is [n5_width_samples.json](C:/Users/swami/Projects/gct-gpt/Batch12_Results/S5/n5_width_samples.json).

## 9. Permanent admissibility and asymptotic scope

The S5 partition has 11 rows. Padded `per_3` has only `3^2+1=10` variables, so this cell cannot be a positive-multiplicity successor for that same padded model. The smallest admissible specified permanent is

\[
z\,\operatorname{per}_4,
\]

a degree-five form in 17 variables. Its variable budget admits an 11-row representation. This statement gives admissibility only; no permanent rank was computed.

For determinant size `N` and permanent size `m`, the same LMR row count imposes

\[
2N+1\le m^2+1,
\]

while standard padding `z^(N-m) per_m` also needs `m<=N`. The minimal budget is `m=ceil(sqrt(2N))`, equivalently `N<=m^2/2`. Therefore this family can probe a quadratic determinant-size scale, but its variable budget alone cannot reach `N=m^c` for arbitrary `c>2`. A finite obstruction here would be scientifically useful and could support a quadratic lower-bound programme; it would not establish Valiant-level superpolynomial quantifiers.

Nor does the fixed-`n` plateau of 1,661 shapes prove polynomial complexity in growing `n`: the local skew state bound grows through `(2n)!`, the circuit memory through `2^(2h+W)`, and the multiplicity dimensions have no uniform polynomial bound here.

## 10. Conditional successor ranking

The actual Batch 12 evidence still lies on the unresolved-rank branch: S1/S3 do not supply a complete evaluable source, and S4 proves only padded rank at least 12. No partial matrix rank justifies a scientific pivot.

| Rank state | Priority | Candidate and evidence gate | Budget/stop rule |
|---|---:|---|---|
| `D(24)` unresolved | 1 | Compute S3's four `n=4,d=12` pairing coefficients; verify the same recursive two-vector source by direct circuit evaluation and both primes. | **30 min, 256 MiB** for the first compact coefficient routine, as preregistered by S3. Stop and record width if either cap is reached; do not scale. |
| unresolved | 2 | Complete the `n=4` birth-quotient source/rank path in common coordinates. Accept determinant 273 or padded 274 only from valid minors; deficient samples are lower bounds. | **16 CPU-hours, 7 GiB**, one-prime screening with second-prime/fresh-point validation of any promotable minor. Stop target work if the control bridge is not complete. |
| unresolved | 3 | Stable `M_6`, weight-13 `a_infinity=4`, as an independent cheap equation search—not as a pivot away from rank. | Recount gives five blocks with raw spaces 1,668; 3,716; 4,636; 6,922; 9,166. **2 CPU-hours, 2 GiB**; stop at first certified nonzero ideal, otherwise close exactly these five. |
| unresolved | 4 | Continue the S2 exact `r=5` chart ideals independently. | No generic arc sweep. Run only the two generated representative chart jobs with exact elimination and retain ideals/certificates; global claims wait for both. |
| exact `D(24)>0` | 1 | Independently replay and bank the `n=4` obstruction, source normalization, determinant 273-minor, padded 274-minor, and point semantics. | No successor launch until both independent evaluation paths agree. |
| `D(24)>0` | 2 | Develop a sparse/endpoint-blocked S5 operator before any rank run; then price the admissible `z per_4` cell. | **2-hour prototype, 7 GiB**. Stop if the first full top block materializes `B^2`, exceeds 7 GiB, or lacks an evaluable inclusion. |
| `D(24)>0` | 3 | Exact S5 endpoint census: all 54 `a_38(nu)`, especially the five finite-boundary corrections, followed by exact `C_residual`. | **4 CPU-hours, 7 GiB** with checkpointed endpoints. Stop at cap and report rigorous partial sums/bounds only. |
| `D(24)>0` | 4 | Formulate the growing `m` family at `N<=m^2/2`; seek a uniform sparse recurrence with explicit `N,m,W,B,C` quantifiers. | Stop after one bounded theory session if the result is only a fixed-`N` plateau or an unquantified recurrence. Never label it Valiant-level. |
| exact `D(24)=0` | 1 | Compare determinant and padded kernel lines in the same 274 coordinates. Distinct lines may still carry geometric information. | Require exact source convention and identities, not modular kernels alone. |
| exact `D(24)<0` | 1 | Bank the negative multiplicity result and preserve kernel orientation data. Move first to the five stable `a_infinity=4` blocks. | Stop at first certified stable determinant ideal or after the exact five-block negative closure. |
| exact `D(24)<=0` | 2 | Consider length-six or other LMR-like cells only when a supplied circuit has measured width and an exact small source. | Gate each candidate on exact `a`, valid HWVs, two evaluators, `W<=4` on nonzero fillings, and projected peak below 7 GiB. Fail any gate: PARK. |
| exact `D(24)<=0` | 3 | Return to S5 `z per_4` only if the sparse recoupling and evaluation bridge pass; current dense architecture is killed. | No rank sampling from incomplete sources and no `n=4` timing extrapolation. |

The stable-frontier recount is [stable_m6_a4_frontier.json](C:/Users/swami/Projects/gct-gpt/Batch12_Results/S5/stable_m6_a4_frontier.json). Two independent current-code Weyl implementations give five `a_infinity=4` blocks and 47 nonzero weight-13 blocks overall, while the comprehensive source says 46. The five-block frontier agrees and is the only population used above; resolve the 46/47 discrepancy before making a global population claim.

## 11. Minimum next measurements and claim ledger

The minimum measurements that materially narrow S5 are, in order:

1. finish the four S3 control pairings; without them there is no evaluation-compatible recursive source;
2. compute the 54 exact degree-38 endpoint multiplicities, yielding exact `C_residual`;
3. implement multiplicity-weighted, level-streamed counts for all 42,533 nodes to obtain `C_total`, `C_peak`, and `W_edge`, recording peak bytes;
4. demonstrate a sparse or blockwise top residual whose peak is below 7 GiB—`B^2` storage is disallowed by the computed gate;
5. only then enumerate/evaluate a complete 17,107-dimensional source against determinant-5 and random 11-variable restrictions of `z per_4`.

| Claim | Status | Evidence |
|---|---|---|
| `a40=17107` | **CERTIFIED** | five-prime residues, CRT modulus above explicit upper bound, finite-equals-stable audit |
| `B40=176451` | **PROVED/CERTIFIED** | stable precursor certificate plus the sole multiplicity-one boundary correction |
| S5 DAG/path/local counts | **EXACT** | independent horizontal-strip and corner-removal enumerator; both `n=4` controls match |
| weighted cost intervals | **PROVED** | constituent lower bound, max-path argument, and explicit stable-weight upper bounds |
| `W=2..4` on 325 probes | **MEASURED** | deterministic seed/restarts; heuristic upper bounds only |
| current dense/streamed recursion exceeds 7 GiB | **KILL implementation** | rigorous lower sizes 441.46/231.97 GiB |
| one S5 circuit is cheap to evaluate | **CONDITIONAL** | state arrays fit at observed widths; runtime and nonzero source distribution unmeasured |
| exact S5 rank or obstruction | **OPEN** | no complete evaluable source and no qualifying minors |
| polynomial scaling in growing `n` | **OPEN** | no uniform recurrence/pathwidth/multiplicity theorem |

## 12. Reproduction and artifacts

Primary replay commands, from `C:/Users/swami/Projects/gct-gpt`, use the bundled Python recorded in the manifest:

```powershell
python Batch12_Results/S5/s5_scaling.py --n 5 --delta 40 --lambda 151,31,2,2,2,2,2,2,2,2,2 --out Batch12_Results/S5/n5_d40_skeleton.json
python Batch12_Results/S5/s5_ambient.py --n 5 --delta 40 --tail 31,2,2,2,2,2,2,2,2,2 --out Batch12_Results/S5/n5_d40_ambient.json
python Batch12_Results/S5/s5_precursor.py --n 5 --tail 31,2,2,2,2,2,2,2,2,2 --out Batch12_Results/S5/n5_stable_precursor.json
python Batch12_Results/S5/s5_boundary_audit.py
python Batch12_Results/S5/s5_width_probe.py --samples 25 --restarts 50 --seed 5040 --out Batch12_Results/S5/n5_width_samples.json
python Batch12_Results/S5/s5_stable_m6_frontier.py
python Batch12_Results/S5/s5_cost_ledger.py
```

The exact interpreter path and every input/output hash are frozen in [manifest.json](C:/Users/swami/Projects/gct-gpt/Batch12_Results/S5/manifest.json). Computed data are [n5_d40_ambient.json](C:/Users/swami/Projects/gct-gpt/Batch12_Results/S5/n5_d40_ambient.json), [n5_stable_precursor.json](C:/Users/swami/Projects/gct-gpt/Batch12_Results/S5/n5_stable_precursor.json), [n5_finite_boundary.json](C:/Users/swami/Projects/gct-gpt/Batch12_Results/S5/n5_finite_boundary.json), [n5_d40_skeleton.json](C:/Users/swami/Projects/gct-gpt/Batch12_Results/S5/n5_d40_skeleton.json), and [S5_cost_ledger.json](C:/Users/swami/Projects/gct-gpt/Batch12_Results/S5/S5_cost_ledger.json).

No result in this report changes the frozen `n=4` rank protocol: `lambda=(65,17,2^7)`, `delta=24`, `a=274`, determinant rank 273 OPEN, padded rank 274 OPEN, true padding `ell per_3`, and `D=rank(T_pad)-rank(T_det)` in common source coordinates.
