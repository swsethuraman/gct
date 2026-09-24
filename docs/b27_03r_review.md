# R27-03 — independent review of B27-03

**READ claims; HAND + COMPUTED review verdict: ACCEPT the mathematics of 3a–3c in the scopes below; REPAIR 3d and the reproducibility wording.** Registered outcome (4), obstruction with an indicative price, and outcome (2), vacuous scoped containment, survive. Outcomes (1), a reopening equation, and (3), rejection of the padding point by a determinant preimage, were not obtained. The first nonzero kernel degree remains unresolved.

**Achievement level: scoped exclusions and COMPUTED zero-kernel certificates, with HAND consequences.** None of the four programme achievements (source condition, coefficient equation, separation on padding, positive multiplicity gap) is newly obtained. The application of the already accepted smooth-cubic exclusion gives full-form geometric nonmembership, separately from the unresolved projected question. No asymptotic bound follows.

**Binding constraint:** "No five-row determinant equation is known to be nonzero on padding."

## 1. Preflight and byte bindings

**READ / administrative:** The common instructions were read before the review brief. This is a fresh Astra review with no prior exposure to the packet during production. Branch `b27-03r`, worktree `work/batch27/b27-03r`, and HEAD `fcff7eeaa491aab4a3b1d1ba1161c24a89dae818` matched PART 25. The worktree was clean; `docs/b27_03r_review.md` and `results/b27_03r/` were absent. No existing untracked files were changed. No applicable `AGENTS.md` was found in the searched ancestors/worktree.

**READ / administrative:** Raw instruction-file SHA-256 values:

| File | SHA-256 of raw file bytes |
|---|---|
| B27_COMMON.md | `891e3ca872bc795b6f943ac89f55112573803f006e0208940dd6cad1f750d6ee` |
| R27-REVIEWS.md | `916de53ab8c31c3d4242a84d8a894ce9ceecc75d76ef83dea8d4d87b3edddaa9` |
| BATCH27_BOARD.md | `b0bc2501aba62d49b91862d821232ac1b9904480057a8dcdb4cbc03fbd86efec` |

**READ / administrative:** `ls-remote` confirmed the producer had pushed `7c36a52ddf338eb390a9bcd491cb9c50cf9e2a19`; the reviewer remote was still the expected setup commit. The producer manifest is `results/b27_03/MANIFEST.json`, **2,954 bytes**, raw SHA-256 **`463d9dfcc04a7782476f4854ef3714264227ee59fe21765ab9124e00cbcf2c0d`**. All **18 payloads**, their byte counts, and all **12 producer input bindings** match. The manifest plus those payloads accounts for the exact producer commit changes. See `results/b27_03r/INPUT_BINDINGS.json`.

**READ / administrative:** Every producer premise and executable was read with `git show <commit>:<path>`, never from the producer worktree. Exact source copies delivered under `analysis/b27_03r_source_*` retain the committed bytes. Initial Git ownership and network restrictions were resolved with a per-command `safe.directory` setting and approved read-only remote access; no global Git setting changed. Installed Python 3.12.10, SymPy 1.14.0 and NumPy 2.4.6 were located after the sandbox PATH/runtime lacked SymPy. Nothing was installed. These access issues exposed no branch, output-path or input-binding mismatch.

## 2. Rung 3a — ACCEPT

**READ:** The committed witness fixes `l=x1+x2+x3+x4+x5` and

```text
A' = [ x1+x3    x2-x4    x5+2x1
       x3+x4    x1-x5    x2+x3
       x2+2x5   x4+x1    x3-x2 ].
```

**COMPUTED, replay 1 and independent run 8:** All 65 retained ordinary coefficients agree exactly, including their descending-lexicographic order; 58 are nonzero. The omitted coefficients are `(6,3,0,3,2)` in the producer's `q5,q4,q3,q2,q1` order. The independent code uses sparse integer multiplication of the six permanent summands from the committed 10-by-5 substitution, without importing producer mathematics. The six off-diagonal asymmetries also replay exactly. These establish an actual rational padding point, not an arbitrary cubic declared to be a permanent.

**COMPUTED, independent run 8:** A separate smoothness certificate uses the 350-by-210 integer matrix of `x^beta partial_i(C)`, `|beta|=4`, in the degree-six monomial basis. An explicitly indexed 210-square minor has determinant **3123 modulo 32003**. Its matrix hash, row indices and construction are in `replays/independent_run8.json`. For the eight good coordinate planes, the analogous degree-four matrices have rank 15. In lexicographic plane order their nonzero minor residues are `7306,20885,17961,31531,18211,28547,11631,12706`. The excluded triples are `{1,4,5}` and `{2,4,5}`; no inference about characteristic-zero singularity is made from their deficient modular ranks.

**HAND:** A nonzero modular minor is a nonzero integer minor. Thus the five partials generate every degree-six monomial over Q, so they have no nonzero common zero over C. The same argument in degree four certifies the eight smooth plane cubics. This independently proves the required smoothness facts, without relying on the producer's Gröbner-basis implementation or on an unrecorded numerical test. Smooth positive-dimensional projective hypersurfaces are irreducible: distinct positive-degree components intersect and make the product singular.

**HAND:** The producer's good-reduction lemma is also sound. Normalize an algebraic singular point at a prime over 32003 so one coordinate is a unit and all are integral. Reduction would give a nonzero common zero of the reduced partials, contrary to their homogeneous zero-dimensional ideal. A complex solution would imply an algebraic solution because the equations are over Q.

**HAND:** Every five-variable 3-by-3 linear determinant is singular. An injective pencil embeds P4 into P8, where it meets the rank-at-most-one Segre variety of dimension four; all cofactors vanish there. A noninjective pencil has a nonzero kernel vector, also with all cofactors zero. Singular cubics form a closed locus. Independently expanding A26-01's matrix gives `abc+be^2+cd^2+(u^2-1)af^2+2def`, so at `u^2=2` every symmetric-block permanent is such a determinant. If `l C=l' per(A_sym)`, unique factorization forces `l'` proportional to `l` and `per(A_sym)` proportional to the irreducible smooth `C`, a contradiction. Arbitrary linear forms already make that family GL5-stable. Thus the witness lies outside its literal family and every covered variable change.

**READ + HAND:** The full-form consequence `F=lC notin D` uses the accepted B17-01 smooth-cubic exclusion. I read its committed report at `01c49022c2a222254884c8c96611dd0e9f302892:docs/b17_01_report.md`, specifically the componentwise ruledness lemma and smooth-cubic consequence, and applied the newly verified smoothness hypothesis. This is an application of the standing accepted theorem, not a new independent audit of its external literature. Those external sources are **UNREAD** in this review. The producer's `READ, B17-01` labels should instead say that it relied on the standing convention; its own input ledger expressly says the packet was not read.

## 3. Rung 3b — ACCEPT

**HAND:** Each omitted squarefree quartic vanishes on every coordinate three-plane. Therefore any factorization `F+K=G1 G2` restricts on a good plane to the nonzero product of a linear form and an irreducible cubic. Nonzero homogeneous restrictions preserve factor degrees, excluding a 2+2 factorization. In a 1+3 factorization the linear factor restricts to a scalar multiple of `l` on each good plane. Every pair of three-subsets intersects, and every coefficient of `l` is nonzero, so those scalars agree. The eight planes cover all coordinates; the linear factor is globally proportional to `l`.

**HAND:** Consequently `K=lR`. For nonzero `R`, degree in each variable satisfies `deg_i(lR)=1+deg_i(R)`. But `K` is multiaffine, forcing `R` to be independent of every variable, incompatible with its homogeneous degree three. Thus `K=0`. The only reducible completion is the original `lC`, with its unique irreducible factors up to scaling.

**HAND:** This excludes the named constructions exactly as claimed: a 1+3 triangular pencil would give a 3-by-3 determinant for the smooth cubic; 2+2 or finer products have the wrong factors; a Pfaffian square has even factor multiplicities. Invertible left/right matrix multiplication changes only an overall nonzero scalar, so it does not evade these arguments. **READ + HAND:** B17-01 further excludes `F` itself, and hence every reducible literal determinant completion.

**HAND:** An irreducible completion with nonzero `K` is still possible on this evidence. Furthermore, A25-05's committed splitting `W=J5 direct-sum K5` gives `pi^-1(Y5)=closure(D+K5)`. Literal non-solvability alone cannot exclude membership in that closed saturation. Therefore the point is **not rejected**, and no statement `pi(F) notin Y5` is accepted or claimed.

## 4. Rung 3c — ACCEPT within the tested scopes

**HAND, code audit:** The recursive monomial enumeration lists each nondecreasing multiset of coefficient exponents with the requested degree/weight exactly once. The determinant evaluator expands all 24 signed permutations and collects all variable assignments into ordinary quartic coefficients. Evaluation is at explicitly reconstructible integer pencils. A full column rank modulo a prime supplies a nonzero integer minor, and hence injectivity of the polynomial restriction on the stated coefficient space. This is a finite certificate, not a sampled nullspace. The deficient 613/619 run supports no kernel assertion and was correctly not used as one.

**HAND + COMPUTED:** Modular arithmetic is safe in signed int64: each product of reduced residues is at most `(1000000006)^2 < 2^63`; subtraction and the small integer determinant expansion also stay in range. Run 8 checked primality of both 32003 and 1000000007 by exhaustive trial division. The two rank routines implement valid row elimination. Dimension-count DP multiplies the factors `(1-t x^alpha)^-1` with increasing coefficient degree, correctly allowing repeated variables. All seven scripts, including their shared library, replayed with identical mathematical JSON data.

**COMPUTED:** The key full ranks are 13/13, 167/167, 1905/1905 at balanced weights in degrees 2, 3, 4 of the 70-coordinate ring; 480/480 at A26-01's 65-coordinate H; 619/619 at its 70-coordinate counterpart; and 1018/1018 at `(8,(23,3,2,2,2))` in the 65-coordinate ring. All additional finite ray ranks reproduce. The raw replay files preserve every dimension, point count, skip and rank.

**HAND:** For a partition of `4k`, the balanced partition `mu=(q+1 repeated r times,q repeated 5-r times)` is dominated by every partition with at most five parts. If a partial sum were below `jq+min(j,r)`, its last part would be at most q and the remaining parts could not bring the total up to `5q+r`. Independently, the needed weight-existence assertion has a root-string proof: in any nonzero polynomial GL5-submodule choose a weight minimizing the sum of squares of its entries. If two entries differ by at least two, the lowering operator of their sl2 has positive weight and is injective there (on each finite sl2 string); it produces a weight with smaller sum of squares. Thus a minimal weight has entries differing by at most one. Permutation matrices reorder it to mu. Consequently any nonzero `I(D)_k` contains the balanced weight, and vanishing of that whole weight space forces `I(D)_k=0`. This argument is applied to the **70-coordinate** ring; it does not assume that the retained ring is GL5-stable. Lower degrees 0 and 1 follow by multiplication into degree 2 in the ambient polynomial domain. Hence `I(D)_k=0`, and therefore `ker Q_D=0` in the retained ring, for every `k<=4`.

**HAND:** For fixed tail sum s, any degree-k coefficient monomial with weight `(4k-s,w')` has a pure `c_(4,0,0,0,0)` factor whenever `k>s`. Removing that factor gives exactly the previous weight space. The closed determinant image, and its projected closure, are irreducible; the pure coefficient is not identically zero because `x1^4` is a determinant. Thus multiplication by this coefficient preserves and reflects kernel vanishing. This proves the stabilization lemma in both rings.

**HAND from COMPUTED:** Ray 1 has no kernel for every `k>=2` in either ring: k=2 follows from whole-degree vanishing, k=3 through 8 from the certificates, and k>8 from stabilization. Ray 2 has no kernel for every `k>=3` in the retained ring: k=3 follows from whole-degree vanishing, k=4 through 9 from the certificates, and k>9 from stabilization. The finite coverage has no missing endpoint.

**HAND:** Each accepted kernel is `{0}`, so evaluation of its empty basis on the witness is vacuous. This accepts outcome (2) only in that explicit weak sense. The lowest degree carrying a nonzero kernel was not determined; the literal 3c target remains **DEFERRED**, without weakening the accepted no-go statements. No degree-five-through-seven whole-ring conclusion is imported from the unaudited historical floor.

## 5. Rung 3d — REPAIR

**READ + HAND:** The obstruction is real: the tested spaces contain no equation, and a separating candidate needs exact global kernel membership plus an actual-padding nonzero value. However, the statement that a nonzero `I(D)` weight has not been observed in the programme must be restricted to the reported low-degree rank tests. The producer's own bound input `CORRIGENDUM.md` C10 explicitly records degree-300 five-row determinant equations, with its stated dependencies, and explains that they also vanish on padding. Smallest true replacement: **"No nonzero kernel was found in the spaces tested here; the first nonzero degree in the retained ring was not identified, and known full-ring equations do not supply a retained-ring separator."** Finding a separating equation does not logically require first settling the exact onset.

**COMPUTED + HAND:** Replay 4 confirms the tabulated dimension counts. Independent run 8 gives the previously uncomputed stable dimensions **1982** at `(10,(30,4,2,2,2))` and **2254** at `(10,(30,3,3,2,2))`, within the producer's approximate range. The stated dense parameter count at degree 5 is exactly `binom(75,25)=52588547141148893628`, so its order-of-magnitude assessment is sound.

**HAND:** The formula `8N(N+16)` prices one int64 evaluation array, not peak process memory or complete computation. Forward elimination additionally holds the original array, a reduced copy, advanced-indexing arrays, products and remainder temporaries; basis generation and determinant evaluation also cost time and storage. The reviewer measured about **191 MB** peak job memory on the degree-four run, although its main matrix is about 29 MB. Thus a largest-array bound alone does not certify the producer's original resource claim.

**HAND:** The cubic timing extrapolation is an estimate tied to forward elimination, not a bound and not a guarantee for the slower all-row library routine. Repair the table's "within allowance: yes" to **"estimated to fit with forward elimination, subject to an enforced 60-second/512-MB cap; incomplete runs yield no certificate."** For the two newly counted stable spaces, one matrix needs about 31.7 MB and 40.9 MB respectively; these are storage components, not peak-memory promises. The large rows remain clearly outside the stated dense allowance.

**HAND:** Repair "the cheap rows ... cannot yield outcome (1)" to **"they are expected to have zero kernel; that expectation is unproved. A deficient evaluation rank would be inconclusive and would require a separately priced exact membership method."** Likewise, a stable-degree run closes its whole ray **if** it attains full column rank; execution alone supplies no such guarantee. A positive method in the invariant model remains **DEFERRED / unpriced**. Outcome (4) is accepted as an obstruction with indicative estimates, not as a complete executable positive preregistration. No next job is launched or authorized by this review.

## 6. Replay, provenance and disposition

**COMPUTED / administrative:** Eight mathematical runs were used, sequentially: seven unchanged producer replays and one independent verification. All finished successfully below 60 seconds; the maximum measured peak job memory was 191,000,576 bytes. `RESOURCE_RECEIPT.md` and `run1_receipt.json` through `run8_receipt.json` bind exact commands, script/input hashes, output/log hashes, elapsed times and process limits. The manager scripts are administrative supervisors, not extra mathematical runs.

**READ + COMPUTED / administrative — REPAIR:** None of the seven raw replay output hashes matches, because every producer output embeds `wall_s`. Removing **only** those timing keys yields exact equality of all seven parsed JSON objects. The resource receipt's claim that the output files are deterministic must therefore be narrowed to the mathematical payload. No hash match is asserted after silently normalizing bytes; original raw hashes, replay raw hashes and explicit comparison semantics are all recorded.

**READ / administrative:** The first recorded clock was 04:11:29 UTC after initial intake; mathematical verification ended before the 04:18:41 UTC checkpoint on 2026-09-23. Intake was not separately timestamped. Final packet administration is timestamped in the receipt. There were no subagents, other sessions, messages to tasks, installations, paper/ledger/seal edits, publication or automatic continuation. Only this review's output paths and `analysis/b27_03r_*` were written. The report provides the smallest true repairs without editing the producer packet.

**Final disposition:** 3a **ACCEPT**; 3b **ACCEPT**; 3c **ACCEPT** for the certified empty spaces and their hand consequences, with nonzero-kernel onset **DEFERRED**; 3d **REPAIR** as above. The programme remains **no construction ready**. The binding constraint and all standing achievement distinctions remain unchanged.
