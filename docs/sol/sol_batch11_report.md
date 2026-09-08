<!-- Provenance: this is the Sol side of batch 11, delivered as a single
consolidated report (Word) on 8 September 2026 and converted to markdown here
without editing the content.  It is committed because the batch-10 housekeeping
found that no Sol report had ever entered the repository, so every Sol result
survived only through an integrator assessment that attributed corrections to
memos a reader could not consult.  The integrator's independent review of this
report is docs/s1_s6_batch11_review.md; where the two disagree, the review
carries the checked number and says so. -->

BATCH 11 SOL
Six-Session Comprehensive Research Report
S1–S6: determinant equations, wreath transport, r=5 geometry, stable frontier, intrinsic source compression, and adversarial audit
Consolidated 8 September 2026
Research objective
Determine whether the permanent-versus-determinant programme can be advanced by a cheaper determinant equation, a transport/intertwining mechanism, an r=5 geometric obstruction, a stable determinant-ideal equation, or an intrinsic representation-theoretic source construction—and prune dead routes rigorously.

# Executive synthesis
Batch 11 leaves three primary live research objects: (1) LMR source compression, (2) r=5 normal-cone exhaustion, and (3) the stable M6 determinant-ideal frontier. Everything else is either a support task, a parked route, or killed.
| Session | Core question | Result | Programme consequence |
|---|---|---|---|
| S1 | Is there a dramatically cheaper explicit det4 orbit-closure equation than LMR? | No known cheap equation found. A genuine r=5 discriminant equation exists, but at coefficient degree 405. | LMR remains the cheapest known explicit mechanism; keep discovery efforts rather than literature retrieval. |
| S2 | Can q=2 wreath/plethystic functoriality transport determinant kernels? | Standard Adams, wreath deflation/induction and block-diagonal determinant maps fail structurally. | Kill general-q replication based on standard functorial operations; only a determinant-specific intertwiner remains open. |
| S3 | Can the r=5 boundary problem be exhausted theoremically? | Reduced to four finite normal-cone/Rees-algebra residues; closure non-containment not yet proved. | Stop higher-order arc sweeps; compute localized special fibres/normal cones. |
| S4 | Do weight-13 stable tails with a∞=2 or 3 contain determinant equations? | All five a∞=2 and both a∞=3 tails are determinant-full; together with prior a∞=1, all a∞≤3 are dead. | Stable engine remains attractive, but first possible weight-13 equation has a∞≥4. |
| S5 | Can the wreath source be built intrinsically near multiplicity scale? | Direct partition-algebra/JM routes fail, but a 12-channel Pieri predecessor recursion plus one block swap is exact and promising. | Compute live precursor dimensions Bδ immediately; if small, this may solve the LMR source wall. |
| S6 | Which conclusions survive an adversarial repository audit? | Three live objects remain; several stale assumptions corrected; F4 numerology killed. | Batch 12 should concentrate on state counts/block swap, r=5 Rees residues, stable a∞=4, and decisive LMR ranks. |

## Integrated status
PROVED  Smooth-point higher contact in the r=5 base scheme is inert; standard q=2 functorial mechanisms do not give the required determinant-kernel transport; weight-13 stable tails with a∞≤3 are determinant-full; the twelve-channel predecessor identity for the wreath source is exact.
VERIFIED  LMR remains the cheapest known explicit determinant-orbit-closure equation mechanism among the audited families; old carrier realizations are computationally unusable; the stable M6 engine is dramatically smaller than the LMR carrier.
OPEN  The four residual r=5 normal-cone supports; the live-state dimensions Bδ and compact block-swap implementation; LMR determinant/padded ranks at δ=24; stable a∞=4 and above.
KILL  Classical cheap-equation retrieval as a shortcut; standard q=2 replication; brute carrier enumeration; generic higher-order r=5 arcs; low stable multiplicity as an equation selector; F4 numerology.
## Central quantitative picture
LMR cell: (r, δ, λ) = (9, 24, (65,17,2^7)), with source multiplicity a24=274 and a 273-dimensional transported predecessor block plus one birth direction.
Stable frontier: weight 13 has no determinant equation in any block with a∞≤3; the first possible nonzero stable ideal therefore requires a∞≥4.
r=5 geometry: every visible exceptional fixed-factor image is well below 35, but a theorem requires checking four singular normal-cone residues rather than extrapolating from orders 1–3.
Intrinsic source: for generic LMR rungs there are exactly 12 horizontal-4-strip predecessor channels; the unknown is the total precursor dimension Bδ, not the number of channels.

# S1 — Cheaper determinant equation
Verdict: VERIFIED. No published or immediately constructible determinant-orbit-closure equation was found in a dramatically cheaper computational cell than LMR. The only genuine lower-r explicit equation surfaced by the audit is the r=5 quartic discriminant, but its coefficient degree is 405 and therefore unusable for the present programme.
## 1.1 Baseline and cost-indexed candidates
| Mechanism | r | δ | λ / module | aδ | nχ / expected support | Status |
|---|---|---|---|---|---|---|
| LMR dual/Hessian | 9 | 24 | (65,17,2^7) | 274 | nχ≈31,039,465; measured HWV support ≈6–8×10^6 | KEEP / baseline |
| Middle catalecticant minors | 9 | 37 | 37×37 minor modules | — | 45×45 catalecticant, det4 rank ≤36 | KILL: δ>24 |
| Quartic discriminant | 5 | 405 | (324^5), one-dimensional character | ≥1 | Explicit resultant; enormous coefficient degree | KILL computationally |
| Discriminant r=6,7,8 | 6–8 | 1458, 5103, 17496 | rectangular characters | — | Strictly worse | KILL |
| Koszul/Young flattenings | varies | rank+1, large | flattening-minor modules | — | Useful for secant/Waring rank, not a cheap det-orbit ideal | KILL as shortcut |
| Apolar/syzygy conditions | varies | no known <24 extraction | — | — | Returns to catalecticant/kernel/syzygy rank conditions | OPEN low priority |
| Conductor/non-normality | — | — | — | — | Measures normalization defect, not whole-closure vanishing | KILL |
| Boundary-component equations | — | — | — | — | Vanish on boundary, not dense determinant orbit | KILL |
| Larger determinant specializations | — | ≥ source degree | — | — | No degree reduction; wrong functorial target | KILL |

## 1.2 Why LMR naturally begins at r=9 and δ=24
The Landsberg–Manivel–Ressayre construction gives equations for hypersurfaces whose dual variety has dimension at most k, with coefficient degree (k+2)(d−1). For det_n, d=n and k=2n−2, so the equation degree is 2n(n−1). At n=4 this is 24.
δ_LMR = (2n)(n−1) = 24  for n=4.
The row/variable threshold is also geometrically forced. A hypersurface in P^(r−1) has dual dimension at most r−2. The determinant dual-dimension condition k=6 is therefore automatic when r≤8 and becomes nontrivial only at r=9. Thus the length-9 LMR partition is not accidental representation theory; it reflects the first nonvacuous dual-variety condition.
## 1.3 Classical flattenings: exact cost obstruction
For a quartic determinant, the middle derivative/catalecticant rank is the dimension of the complementary 2×2 minors: C(4,2)^2=36. At r≤8, dim Sym^2 C^r≤36, so the condition is vacuous. At r=9, dim Sym^2 C^9=45, and the first nontrivial equations are 37×37 minors, hence coefficient degree 37. This is thirteen degrees worse than LMR.
rank Cat_2(det_4)=36;  first nontrivial minor at r=9 has δ=37.
## 1.4 A real r=5 equation: the discriminant
Every five-dimensional linear pencil L≅P^4 inside P(M_4)=P^15 intersects the rank≤2 determinantal locus, whose projective dimension is 11. Since 4+11=15, every quartic in D5 obtained from such a pencil is singular. Hence the quartic discriminant vanishes on D5.
Disc(f)=0 for all f∈D5;   degree(Disc)=r(d−1)^(r−1)=5·3^4=405.
This is conceptually useful because it corrects the statement “there are no equations at r<9.” The right statement is: no known cheap equations at r<9.
## 1.5 Other audited mechanisms
Apolarity/syzygies: the determinant has rich quadratic apolar structure, but converting it into ambient coefficient equations returns to catalecticant-rank conditions unless a new nonlinear syzygy invariant is found.
Nonnormality/conductor: nonnormality is geometry of the coordinate ring and its normalization; a conductor element is not automatically an element of the ambient ideal I(D).
Boundary equations: a polynomial defining a boundary divisor is typically nonzero on the open determinant orbit, so it cannot define the whole orbit closure.
Larger determinant equations: restriction or block specialization preserves or worsens coefficient degree and typically lands on products/padded forms rather than the det4 orbit closure.
Recent flattening literature: new tensor-rank and secant-variety flattenings do not furnish a cheaper polynomial equation for closure(GL·det4).
## 1.6 Exact theorem gap and implementation consequence
OPEN  S1 does not prove I(D_r)_δ=0 for every r≤8 or δ<24. That would require a representation-theoretic vanishing theorem or an exhaustive computation of all relevant blocks.
KILL  Do not allocate implementation effort to a literature-derived “forgotten classical equation.” None survived the cost screen.
The only sensible follow-up is a direct finite minimality search in r=6,7,8 and δ<24 if existing census machinery makes those blocks cheap. That would be new discovery, not retrieval.

# S2 — Wreath/Theta intertwiner at q=2
Verdict: KILL in the standard natural functorial categories. Natural q=2 operations exist at the character, wreath, and power-map levels, but none supplies an injective multiplicity-space map that also transports determinant evaluation with controlled row growth.
## 2.1 Required object
At degree δ, the source Sym^δ(Sym^n V) has Frobenius characteristic h_δ[h_n], and the multiplicity block is M^(n,δ)_λ=[λ]^(S_n wr S_δ). The hoped-for mechanism is an actual map
R₂ : M^(n,δ)_λ → M^(2n,δ′)_λ′
together with S₂ on the determinant-evaluation target, satisfying S₂ Θ⁺_(n,δ)=Θ⁺_(2n,δ′) R₂, with R₂ injective on at least one relevant multiplicity block. The economically attractive dream is λ′=2λ and δ′=δ, which doubles row lengths without increasing the number of rows.
## 2.2 Adams operation: character identity, not a representation embedding
The second Adams operation ψ² is the natural degree-doubling ring endomorphism p_k↦p_2k. It has the correct total weight growth, but in general ψ²(s_λ)≠s_(2λ); it is a signed virtual Schur combination. The smallest example already fails:
ψ²(s_(1)) = p₂ = s_(2) − s_(1,1).
Therefore Adams doubling cannot define a positive injective map [λ]→[2λ]. The failure occurs before determinant evaluation enters.
## 2.3 Adams also misses the Foulkes source
ψ²(h_δ[h_n]) ≠ h_δ[h_(2n)].
Thus Adams does not even send the S_n wr S_δ invariant source to the S_2n wr S_δ invariant source. Projecting onto a desired Schur summand destroys the natural multiplicative structure needed for the commutative square.
## 2.4 Wreath deflation and induction
Canonical wreath-product deflation restricts a large symmetric-group representation to S_m wr S_n and takes base-group invariants. This naturally points from the large group toward the small one. The programme needs the reverse direction n→2n while preserving a selected determinant kernel. Induction reverses group direction but yields a broad induced representation rather than a distinguished injective copy of the desired target multiplicity block.
VERIFIED  Wreath deflation is still potentially valuable computationally for S5, because it naturally extracts invariant multiplicity information.
KILL  It is not the q=2 determinant-kernel replication map.
## 2.5 Geometric block doubling targets det_n², not det_2n transport
The most concrete n→2n map is block diagonal: (A,B)↦diag(A,B). But
det_(2n)(diag(A,B)) = det_n(A) det_n(B);  on A=B this is det_n(A)^2.
Hence the natural pullback lands on a power variety. A degree-δ′ polynomial on the 2n side becomes effective determinant degree 2δ′ on the n side, and the logical direction is wrong for transporting a known equation upward.
## 2.6 A genuine square exists for the wrong variety
For the power map f↦f², there is a perfectly natural coordinate-ring map and a commutative evaluation square. This proves that the missing ingredient is not plethysm itself. The missing ingredient would have to bridge det_n² to det_2n, which no standard operation does.
## 2.7 Row-growth economics and final classification
The row-growth economics would be excellent for the nonexistent pure stretch λ↦2λ: row count stays fixed. Actual Adams and induction images spread across many partitions, losing both positivity and row control.
| Item | Status | Reason |
|---|---|---|
| Power-map square f↦f² | PROVED | Natural and exact, but targets the wrong variety. |
| Adams ψ² / wreath character operations | VERIFIED | Natural character-level operations exist. |
| ψ² as R₂ | KILL | ψ²(s_λ) is virtual and not s_2λ. |
| Wreath deflation as R₂ | KILL | Canonical direction is large→small; no canonical inverse. |
| Block-diagonal determinant replication | KILL | Pulls det_2n to det_n². |
| Determinant-specific intertwiner | OPEN | No construction known; would be genuinely new. |

Implementation consequence: do not spend a session coding q=2 replication. Transfer only the useful invariant/deflation ideas to S5. The finite source problem must be solved directly unless a determinant-specific intertwiner appears independently.

# S3 — r=5 exhaustion theorem
Verdict: OPEN, but reduced to a finite normal-cone problem. The banked evidence does not yet prove R5 is not contained in D5. What is proved is that every remaining potentially dangerous exceptional component is supported over four explicit singular residues that can be settled by localized Rees/special-fibre computations.
## 3.1 Correct global object
Let X=M4⊗C^5 (dimension 80), R=C[X], and let J be the ideal generated by the 70 coefficients of det M(s). The base scheme is B=V(J). All contact orders are encoded simultaneously by the exceptional divisor / normal cone
E = Proj gr_J R.
For a fixed linear factor s5, the relevant fixed-factor space is W=s5 Sym^3 C^5, with dim W=35. For each irreducible normal-cone component F, let A_F be the algebra generated by the 35 fixed-factor leading coefficients. The desired exhaustion statement is dim A_F<35 for every F.
## 3.2 What is already closed
Smooth base-scheme support: the contact-order lemma implies that higher-order exceptional directions have the same projectivized image as dΦ. Hence hidden components cannot arise by merely increasing contact order at a smooth point.
Generic points of the eight known base components: primitive, semi-primitive, transposed and compression components have no unrecorded first-order transverse quotient at generic points.
Measured generic incidences: through the available order-2/order-3 decompositions, fixed-factor images stay at or below 29.
Rank≤2 compression leading forms: the leading forms in the known compression cases are honest 4×4 determinants, keeping those branches inside the exact determinant fixed-factor locus.
Padded-skew generic branches: the quadratic factorization produces branch images 28,28,26,26, unchanged at the next measured order.
## 3.3 Why reduced singular-locus geometry is insufficient
The ideal J is generically reduced along individual base components but nonreduced along incidences. Therefore an exhaustion theorem must quantify over irreducible components of Proj gr_J R, including components supported over proper closed subloci, embedded/nonreduced structure, and rank-drop incidence strata. Checking only generic points of the reduced singular locus is logically insufficient.
## 3.4 Four residual supports
| Residual support | Known evidence | Exact finite task | Kill / success criterion |
|---|---|---|---|
| R1: P∩c21 | dim support 33; first-order fixed-factor image 10; no exotic first-order quotient | Localize gr_J R at generic prime; impose non-W coordinates=0; compute minimal/associated components and dim A_F | All dim A_F≤34 closes R1; any 35 is a boundary mechanism. |
| R2: rank-drop strata at ker∩coker | Generic exceptional image 29; lower-rank strata of bilinear matrix unclassified | Stratify by rank j via minors/saturation; compute localized normal cone and fixed-factor dimensions | All <35 closes R2; 35 is decisive. |
| R3: extra quadratic branches at P∩c32 and SP∩c21 | Observed order-2/3 branch images ≤28 | Localize/saturate full Rees ideal along each extra Q2 branch; determine whether it survives full normal cone | If branch dies or image≤34, close; if 35, breakthrough. |
| R4: deeper rank≤2 incidences | Generic compression/padded-skew pieces controlled and ≤31 / ≤28 | Build incidence poset among (2,0),(4,2),(3,1), padded-skew; compute one local normal cone per stratum | All <35 closes R4; 35 reverses expectation. |

## 3.5 Finite-exhaustion theorem obtained
Let Z_res be the union of R1–R4. Then every exceptional component not already controlled by the banked smooth/generic analysis is supported over Z_res. Therefore the r=5 closure question is equivalent to the finite statement that every irreducible component of E restricted to Z_res has fixed-factor algebra dimension at most 34.
R5 ⊄ D5 follows if  dim A_F ≤ 34  for every F ⊂ E|_(Z_res).
## 3.6 What cannot be inferred
OPEN  The actual bound dim A_F≤34 on all residual components has not yet been proved.
Two tempting inferences are invalid: (i) a proper sublocus cannot have larger exceptional fibres; and (ii) because orders 1–3 are small, all higher orders are small. Normal-cone fibres can jump upward exactly on proper singular subloci, and only the smooth-support contact lemma licenses higher-order extrapolation.
## 3.7 Implementation consequence
KILL  Generic q=4/q=5 arc sweeps, random higher-contact experiments, and analyses restricted to the reduced singular locus.
C5 should compute localized Rees algebras/special fibres directly, in the order P∩c21, extra branch at P∩c32, extra branch at SP∩c21, rank strata at ker∩coker, then the rank≤2 incidence poset. One integer per irreducible component—dim A_F—is the decisive output.

# S4 — Stable M6 frontier
Verdict: PROVED within the session’s exact modular certificate framework. Every weight-13 stable tail with a∞≤3 is determinant-full. The low-multiplicity selector is killed, while the direct stable M6 engine remains computationally attractive.
## 4.1 Stable model
The stable M6 model is expressed through the characteristic-polynomial coefficients of five traceless 4×4 matrices. For A(s), the key generators are
g₂=−½ tr A(s)²,   g₃=−⅓ tr A(s)³,   g₄=⅛(tr A(s)²)²−¼ tr A(s)^4.
The stable determinant-ideal question becomes an explicit pullback in Sym(Sym²U ⊕ Sym³U ⊕ Sym⁴U) for U=C^5, avoiding the giant Foulkes/HWV carrier.
## 4.2 Complete a∞=2 and a∞=3 results
| Tail ρ | a∞ | Raw ρ-weight space | Pullback rank | Stable determinant ideal |
|---|---|---|---|---|
| (11,1,1) | 2 | 36 | 2 | 0 |
| (9,2,1,1) | 2 | 276 | 2 | 0 |
| (6,3,2,1,1) | 2 | 3,513 | 2 | 0 |
| (5,4,2,1,1) | 2 | 4,419 | 2 | 0 |
| (4,3,2,2,2) | 2 | 12,479 | 2 | 0 |
| (5,5,3) | 3 | 758 | 3 | 0 |
| (4,4,2,2,1) | 3 | 7,927 | 3 | 0 |

The three previously closed a∞=1 tails at weight 13 were (7,2,2,1,1), (5,5,1,1,1), and (5,3,3,1,1). Combining them with the seven new cases yields the stable dead-region theorem:
|ρ|=13 and a∞(ρ)≤3  ⇒  i_det^∞(ρ)=0.
Equivalently, if a weight-13 stable determinant equation exists, its ambient stable multiplicity must be at least 4.
## 4.3 Certificate mechanism
For each tail, the monomial basis of its weight space in the 120 generators y_(d,α), d=2,3,4, was formed. The four raising maps use E_(i,i+1) y_(d,α)=α_(i+1) y_(d,α+e_i−e_(i+1)). The common raising kernel had exactly the independently predicted dimension a∞. Evaluation at genuine random M6 points over two large primes increased rank by the full kernel dimension in every case.
This is the favorable modular direction: a full-rank minor over F_p certifies nonvanishing/injectivity in characteristic zero when the integral raising-kernel dimension is already controlled. No probabilistic Schwartz–Zippel conclusion is needed once an explicit full-rank evaluation submatrix exists.
## 4.4 Complexity insight
The largest raw weight space in the completed frontier is only 12,479, versus millions or tens of millions of coordinates for the LMR source carrier. This validates the stable reduction as a computational research platform even though low multiplicity itself failed as a selector.
## 4.5 Kill criterion and next frontier
KILL  “Very low stable multiplicity is likely to reveal the first determinant equation.” Ten consecutive weight-13 blocks with a∞=1,2,3 are determinant-full.
KEEP  The direct stable M6 computation. It is compact, exact, and can stream higher multiplicities cheaply relative to LMR.
Next: enumerate a∞=4 blocks in increasing raw weight-space size and stop at the first nonzero stable ideal. If all a∞=4 blocks die, raise the theorem threshold to a∞≥5 rather than performing an indiscriminate census.

# S5 — Intrinsic wreath source
Verdict: OPEN, with a concrete new route. Direct partition-algebra and wreath-Jucys–Murphy realizations are hopeless or structurally wrong, but the LMR source multiplicity space admits an exact recurrence from at most twelve horizontal-4-strip predecessor multiplicity spaces followed by one block-swap symmetry condition.
## 5.1 Why direct partition-algebra realization fails
The ramified/partition-algebra description gives a finite basis indexed by nested set partitions. For the LMR tail depth r=31 with m=4, the natural diagram basis has size approximately 3.6×10^33 at δ=12,14,16,18. Even the obvious top-depth quotient with block sizes 2,3,4 contains roughly 1.1×10^23 diagrams. These are vastly worse than the already-unusable native carrier.
| δ | aδ | Natural partition-algebra basis | Top-depth diagrams |
|---|---|---|---|
| 12 | 2 | ≈3.5965×10^33 | ≈1.1051×10^23 |
| 14 | 93 | ≈3.6052×10^33 | ≈1.1321×10^23 |
| 16 | 188 | ≈3.6053×10^33 | ≈1.1322×10^23 |
| 18 | 241 | ≈3.6053×10^33 | ≈1.1322×10^23 |

KILL  Enumerating the partition/ramified-partition algebra carrier, including the top-depth diagram quotient.
## 5.2 Orbit-type compression is informative but not a source basis
At top depth, an S31-orbit is determined only by block counts m2,m3,m4 with 2m2+3m3+4m4=31. There are only 24 such types, with 18,23,24,24 admissible under the δ=12,14,16,18 block-count caps. This enormous symmetry compression is useful for character calculations, but one orbit type can contain many copies of the target Specht module. Therefore 24 orbit types do not mean a 24-dimensional multiplicity carrier.
## 5.3 Why wreath Jucys–Murphy does not separate multiplicity copies
The target is M_λ=(S^λ)^H with H=S4 wr Sδ. Every vector in M_λ transforms trivially under H. Hence elements of C[H], including wreath Jucys–Murphy operators, act through the same trivial character on all 274 copies and cannot resolve their multiplicity. The useful operator algebra would have to lie in the commutant / spherical Hecke algebra, for which no small separating JM-like family is presently available.
KILL  Wreath JM elements as a multiplicity basis.
## 5.4 Exact one-block recursion
Let Hδ=S4 wr Sδ and distinguish the last 4-element block. Put Kδ=H_(δ−1)×S4. Then Hδ is generated by Kδ and one adjacent block transposition τ. Restrict S^(λδ) to S_(4δ−4)×S4. Taking invariants under the final S4 retains exactly the horizontal-4-strip Littlewood–Richardson channels:
(S^(λδ))^(Kδ)  ≅  ⊕_(λδ/μ horizontal 4-strip) (S^μ)^(H_(δ−1)).
The full Hδ-invariant source is then the +1 fixed space of the single block swap:
M_(λδ) = ker(τ−I | Wδ),   where Wδ=⊕_μ M_(δ−1,μ).
This is an intrinsic construction: no native HWV carrier, no Foulkes orbit enumeration, and no 31-million-dimensional representation realization is required if the predecessor spaces themselves can be maintained compactly.
## 5.5 LMR shape gives at most twelve channels
For λδ=(4δ−31,17,2^7), horizontal-4-strip removal produces only 3 predecessor shapes at δ=12 (because of the first-row coincidence), and exactly 12 predecessor shapes for the generic tested rungs δ=14,16,18,24. At δ=24 the predecessor list is:
(61,17,2^7)
(62,16,2^7), (62,17,2^6,1)
(63,15,2^7), (63,16,2^6,1), (63,17,2^6)
(64,14,2^7), (64,15,2^6,1), (64,16,2^6)
(65,13,2^7), (65,14,2^6,1), (65,15,2^6)
## 5.6 Birth spaces and the decisive live-state count
The recurrence clarifies the “birth” phenomenon: the single same-shape predecessor used by the old ladder is only one of twelve Pieri channels. The other eleven channels are natural sources of new birth directions. Define
Bδ = dim (S^(λδ))^(Kδ) = Σ_(λδ/μ∈HS4) a_(δ−1)(μ).
Equivalently Bδ=[s_(λδ)] h4 h_(δ−1)[h4]. The source dimension aδ is the +1 eigenspace dimension of τ inside this Bδ-dimensional precursor. The entire computational viability of S5 now rests on whether Bδ stays small.
## 5.7 Pre-registered economics
| δ | Target aδ | Pieri channels | Unknown live precursor | Decision gate |
|---|---|---|---|---|
| 12 | 2 | 3 | B12 | Control rung; must recover dim 2 exactly. |
| 14 | 93 | 12 | B14 | Measure before coding. |
| 16 | 188 | 12 | B16 | Measure before coding. |
| 18 | 241 | 12 | B18 | Measure before coding. |
| 24 | 274 | 12 | B24 | Decisive LMR viability gate. |

Bδ≤10^4: GO immediately.
10^4<Bδ≤10^5: GO with sparse matrices.
10^5<Bδ≤10^6: conditional; benchmark block-swap cost.
Bδ>10^6: KILL as the practical source engine for the current programme.
## 5.8 Exact theorem gap and implementation consequence
PROVED  The Kδ precursor decomposes into at most twelve horizontal-4-strip predecessor multiplicity spaces, and Mλδ is obtained by one further block-swap invariance condition.
OPEN  Whether Bδ remains near multiplicity scale and whether τ can be applied efficiently in compact Pieri/LR coordinates.
Implementation order: compute B12,B14,B16,B18,B24 and all predecessor multiplicities first; if the counts survive, implement the δ=12 three-channel control and recover the known two-dimensional source; only then scale the block-swap construction. This should precede block Wiedemann or other heroic carrier methods.

# S6 — Adversarial repository and programme audit
Verdict: the programme is narrower and healthier than the planning prose suggests. Three primary live research objects remain: LMR source compression, r=5 normal-cone exhaustion, and the stable M6 frontier. Several “missing” components were already implemented, and several negative routes were being described too loosely.
## 6.1 Machinery already present
Padded evaluation: substantial ev_pad instrumentation and tractable shared-kernel experiments already existed. The LMR bottleneck is not defining the padded evaluator; it is constructing a usable 274-dimensional source basis.
Factorized padded architecture: the source→48 cubic blocks→permanent-kernel factorization and a target ceiling around 521 were already specified. The load-bearing rank identity still requires calibration/proof.
Length-5 closing cells: the integer-encoding wall was already repaired; all 1,075 cells are buildable and the initial-term certifier is sound in the full-rank direction.
Stable model: direct M6 machinery is functioning and should be treated as a first-class engine, not a speculative side branch.
## 6.2 Implementation-dead versus mathematically-dead
| Category | Routes | Meaning |
|---|---|---|
| Mathematically dead | Standard q=2 Adams/wreath replication; boundary equations as equations of D; conductor/nonnormality as ambient equations; generic smooth higher-contact rescue; F4 numerology | Do not allocate another implementation session unless a genuinely new theorem changes the object. |
| Implementation dead | Native LMR HWV carrier; explicit Foulkes enumeration; Gram/support carrier; full partition-algebra diagram basis | The mathematics may be valid, but the representation is computationally wrong. Resurrect only after changing representation. |
| Empirically dead selectors | Low multiplicity alone; birth morphology; skewness/rectangularity heuristics; low stable a∞≤3 | Do not use as prioritization rules, but they are not universal mathematical no-go theorems. |

## 6.3 Critical correction: exact image versus orbit closure at r=5
An earlier result showed that a general reducible quartic is not an exact 4×4 determinant pencil. That is an image statement. The current target D5 is the closure of the determinant-pencil image. Therefore the statement R5 not contained in D5 is still OPEN. This distinction is precisely why the normal-cone work in S3 remains load-bearing.
PROVED  General reducible quartics are not all exact determinant pencils.
OPEN  Whether every reducible quartic is a limit of determinant pencils—i.e. whether R5⊆D5.
## 6.4 LMR decision algebra
At δ=24, the source multiplicity is a=274. If the transported 273×273 determinant block A24 is nonsingular, then the determinant ideal multiplicity is i_det=1. The obstruction quantity is D=mult_pad−mult_det=i_det−i_pad. Under i_det=1, the desired positive obstruction occurs in exactly one case: i_pad=0.
| i_det | i_pad | D=i_det−i_pad | Interpretation |
|---|---|---|---|
| 1 | 0 | +1 | Desired multiplicity obstruction. |
| 1 | 1 | 0 | No separation at this cell. |
| 1 | ≥2 | <0 | Padded side loses even more multiplicity; no desired D>0. |
| ≥2 | < i_det | >0 | Reopens only if A24 is singular and determinant kernel is larger than expected. |

Therefore a source-independent rank deficit in the padded split map Sλ,24 can be decisive before permanent evaluation: if rank S<274 then i_pad≥1; combined with i_det=1, D≤0.
## 6.5 F4 falsifier
The numerical coincidence 274=273+1 was audited against the actual source construction. There is no canonical 26-dimensional object, no Albert algebra, no F4 root datum, no natural f4 operator algebra, and no F4-equivariant action/intertwiner. The multiplicity ladder itself passes through 2,39,93,145,188,219,241,255,264,269,272,273,274; 273 appears simply because the last increment to stable multiplicity is one.
KILL  The 274=273+1 / F4 coincidence. Do not revisit unless an F4 action arises independently and canonically from the source construction.
## 6.6 Final integrated programme status
Primary live object 1 — LMR source compression: measure Bδ, implement the 12-channel block swap if viable, then settle A24 and the padded ranks.
Primary live object 2 — r=5 normal-cone exhaustion: compute the four localized Rees residues. Stop generic arc experimentation.
Primary live object 3 — stable M6 frontier: move to a∞=4 in cost order and stop at the first nonzero stable determinant ideal.
Insurance — length-5 closure falsifier walk: continue only as a bounded, cost-ordered falsifier because a negative census cannot prove containment.

# Cross-session insights
## A. The programme has shifted from “find a clever invariant” to “represent the right finite object”
S1 makes it unlikely that a forgotten low-degree classical equation will collapse the problem. S2 removes the hope that a standard q=2 functorial trick will replicate kernels upward. S5 then isolates the real bottleneck: the relevant 274-dimensional source exists, but almost every obvious realization inflates it to millions, billions, or astronomically many states. The decisive research question is therefore representation compression, not abstract existence.
## B. Two independent routes now avoid the giant LMR carrier
Stable route: works directly in the M6 characteristic-polynomial model; weight spaces through a∞=3 are at most 12,479 in the completed frontier.
Intrinsic source route: rewrites the LMR multiplicity space as the +1 eigenspace of one block swap on a direct sum of at most twelve predecessor multiplicity spaces.
These routes are complementary. The stable route searches for a new determinant equation family; the intrinsic source route attempts to compute the existing LMR equation in the right coordinates.
## C. The r=5 route is now theorem-seeking rather than experimental
The important advance is not another small exceptional-image number. It is the change in quantifier. Higher contact over smooth support is closed theoremically, so the only possible rank-35 jump must occur over a finite singular normal-cone residue. The correct next object is Proj gr_J R localized over four supports, not another list of arcs.
## D. “Negative” results have different epistemic strength
Batch 11 sharply separates mathematical kills from engineering deaths and heuristic failures. This prevents the programme from repeatedly re-implementing structurally impossible ideas while still allowing mathematically valid methods to be resurrected in better representations.
## E. The most valuable cheap experiment is Bδ, not another giant rank
The 12-channel recurrence is exact, but its practicality is entirely controlled by Bδ=Σ a_(δ−1)(μ). Those integers can be computed before building vectors. Measuring B12,B14,B16,B18,B24 therefore has exceptional expected value: a small B24 opens a path to the entire LMR cell; a large B24 kills the idea cheaply.
## F. A first stable determinant equation would be strategically transformative
After ten consecutive weight-13 blocks with a∞≤3 proved determinant-full, the first a∞=4 positive cell—if one exists—would be an independently discovered determinant equation outside the LMR mechanism and a much cheaper laboratory for understanding how determinant kernels are born. Conversely, closing a∞=4 would itself strengthen a stable dead-region theorem.
# Exact theorem and implementation gaps
| Gap | What is known | What must be shown/computed | Decision consequence |
|---|---|---|---|
| Cheaper equation minimality | No audited explicit family beats LMR; r=5 discriminant exists at δ=405 | Either a vanishing theorem for r≤8/δ<24 or a finite direct search | Could replace LMR only if a truly cheaper cell is discovered. |
| q=2 transport | Standard natural operations fail | A determinant-specific intertwiner with genuine kernel transport | No compute until an explicit formula exists. |
| r=5 closure | All generic/smooth routes controlled; residual support finite | For every residual normal-cone component F, prove dim A_F≤34 or find 35 | All ≤34 proves R5⊄D5; 35 finds the missing boundary mechanism. |
| Stable frontier | All |ρ|=13, a∞≤3 are full | Test a∞=4 blocks in increasing cost | First nonzero becomes new determinant equation; otherwise threshold rises. |
| Intrinsic source | Exact ≤12-channel precursor recurrence | Compute Bδ and implement τ in compact Pieri coordinates | Small Bδ may solve LMR source; large Bδ kills route. |
| LMR δ=24 decision | a24=274; expected room-one determinant picture | Certify A24; determine padded split/evaluation ranks | Exact sign of D and viability of central obstruction. |

# Kill ledger
| Route / hypothesis | Status | Reason / resurrection condition |
|---|---|---|
| Forgotten cheap classical det4 equation | KILL as shortcut | No audited family yields a cheaper viable cell than LMR. Resurrect only with an explicit new module/cost. |
| Middle catalecticant minors | KILL | First nontrivial degree 37 at r=9. |
| Conductor/nonnormality as ambient equation source | KILL | Wrong geometric object. |
| Boundary-divisor equations as equations of D | KILL | Vanish on boundary, not dense orbit. |
| Standard q=2 Adams/wreath replication | KILL | Character identities do not transport determinant kernels. |
| Generic higher-order r=5 arcs | KILL | Smooth support inert; singular residue should be handled by normal cone. |
| Direct partition-algebra diagrams | KILL | ~10^33 states; top-depth still ~10^23. |
| Wreath Jucys–Murphy multiplicity basis | KILL | Acts through trivial H-character on the invariant multiplicity space. |
| Native LMR/HWV/Foulkes/Gram carriers | KILL implementation | Valid mathematics, wrong representation scale; resurrect only through compression. |
| Low stable multiplicity as selector | KILL heuristic | All weight-13 a∞≤3 blocks are determinant-full. |
| F4 coincidence 274=273+1 | KILL | No canonical F4 structure; 273 is simply the penultimate multiplicity rung. |

# Prioritized Batch 12 board
The board below follows the S6 audit: prioritize decisive cheap gates, keep independent theorem routes alive, and avoid dependents that become useless if a preceding experiment fails.
| Priority | Session | Mission | Gate | Success / kill criterion |
|---|---|---|---|---|
| 1 | B12-1 — 12-channel state count | Compute Bδ and predecessor multiplicities at δ=12,14,16,18,24. | None | B24>10^6 kills recurrence as current source engine; B24≤10^5 triggers implementation. |
| 2 | B12-2 — block-swap control | Implement δ=12 three-channel Pieri basis and τ; recover exact 2D M12. | B12-1 viability | Failure to recover a12=2 kills implementation; success validates compact source construction. |
| 3 | B12-3 — local Rees R1 | Localized fixed-factor special fibre at P∩c21, including associated/minimal primes. | None | Any dim A_F=35 is breakthrough; all ≤34 closes R1. |
| 4 | B12-4 — extra Q2 branches | Saturate full Rees ideal along P∩c32 and SP∩c21 extra branches. | None | Determine survival in full normal cone and image dimension. |
| 5 | B12-5 — stable a∞=4 | Stream weight-13 a∞=4 blocks by raw source size. | None | Stop on first nonzero ideal; if all full, threshold becomes a∞≥5. |
| 6 | B12-6 — LMR split rank | Determine whether Sλ,24 is source-independent and compute rank if possible. | None | rank<274 can kill D>0 under i_det=1; rank=274 keeps permanent route alive. |
| 7 | B12-7 — determinant room-one block | Certify A24 nonsingular/singular using compact source. | Source available | Nonsingular gives i_det=1; singular gives stronger new determinant information. |
| 8 | B12-8 — LMR decision table | Compute i_pad, i_per4, U_D, U_P, and intersection. | Source available | Return exact D; no partial-credit stopping. |
| 9 | B12-9 — rank-drop normal cone | Exhaust rank strata at ker∩coker. | None | All <35 closes R2; 35 finds boundary mechanism. |
| 10 | B12-10 — rank≤2 incidence poset | Compute remaining local normal cones among compression/padded-skew types. | None | Closes R4 or finds rank 35. |
| 11 | B12-11 — closure falsifier walk | Continue 1,075 length-5 cells in certified cost order. | None | Stop on i_det>i_red; negative census is not containment proof. |
| 12 | B12-12 — external theorem audit | Adversarially verify whichever branch produces new positive evidence. | Positive result | No speculative new branch generation. |

# Highest-value decision points
Compute B24. This is the cheapest binary gate on the most promising new source representation.
Run the δ=12 block-swap control if the state counts survive. It tests the entire S5 construction on a rung whose answer is known exactly.
Compute the r=5 localized Rees residue at P∩c21. A single dimension-35 component would immediately reverse the current geometric expectation; all components below 35 remove the largest named residue.
Stream stable a∞=4 blocks. This is the cheapest independent opportunity to discover a new determinant equation family.
Only after a compact source exists, spend the cost to settle the LMR room-one determinant block and padded rank.
## What would be a major surprise
B24≤10^4: the twelve-channel recurrence would likely become the practical solution to the LMR source wall.
A residual r=5 component with dim A_F=35: this would uncover a previously hidden boundary mechanism and overturn the current expectation R5⊄D5.
A nonzero stable a∞=4 determinant ideal: this would create a new, cheap determinant-equation laboratory independent of LMR.
A24 singular: this would show the determinant ideal at the LMR cell is larger than the expected room-one picture and reopen several D>0 possibilities.
# Provenance and interpretation note
This document consolidates the six Batch 11 Sol session outputs in this conversation into one coherent research report. Statements labeled PROVED, VERIFIED, OPEN, and KILL preserve the epistemic status assigned in those sessions. Primary-source literature and repository citations were consulted and cited in the individual session outputs; this consolidation emphasizes the results, mechanisms, quantitative economics, theorem gaps, and programme decisions rather than reproducing a full bibliography. Where a session result was based on an exact modular or computational certificate, this report records that certificate logic as part of the session result rather than independently rerunning the computation.

— End of Batch 11 S1–S6 consolidated report —