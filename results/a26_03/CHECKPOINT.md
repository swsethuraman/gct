# Early checkpoint, exclusion checks and hand-only price

UNCOMMITTED / PRODUCER ONLY. Checkpoint and mathematical stop:
2026-09-23T01:35:25Z, before the 45-minute checkpoint was due.
Registered outcome 3, REJECTION. All new mathematical statements below are
**hand derivation**; references marked READ are committed text actually read.

## 1. The four checkpoint items

| Required item | Result |
|---|---|
| One explicit redesign, content, shape, normalization, nonzero HWV | PROOF.md section 1: n=4, d=50, shape (68,68,22,22,20), one local column-pair merge. Nonzero by section 2. |
| Exact visibility | PROOF.md (3)--(6): f(q0+s B^2)=C0+C1 s+C2 s^2, each coefficient specified by a finite exact sum and certified strictly positive. |
| Escape statement | Section 2 below gives exact scope; an unconditional escape from the symbolic D* bound is not established. No blanket clearance is claimed. |
| Priced hand-only plan for both sides | Section 3 below. Determinant rejection is completed; padding work is canceled under the one-failure stop rule. |

The four-item success gate is not claimed as a positive outcome: the candidate
has already failed a necessary determinant-side requirement. Closing early with
registered outcome 3 requires no speculative second candidate or extra padding
evaluation. No 45-minute clock observation is invented.

## 2. Exclusions, with their exact scope

READ sources: B25-04 sections 3--4 at 92a7d054... plus scope erratum at
9e12d789...; B22-02 sections 1.1--1.2 and ledger L1--L6 at cdf6839c...;
A25-02 APPLICATIONS and SCOPE_MATRIX at ab4f5271...; corrected GKZ verdict and
scope table at that same pinned commit. Complete bindings are in INPUT_BINDINGS.json.

### Component theorem plus erratum

The original graph on 50 half-edge labels is connected: each old star is a
clique, the a_ij--b_ij edges connect the stars according to K5,5. The merge
retains both replaced pair edges inside its four-label clique and adds edges.
There is still exactly one component, of size 50. This is only a graph statement;
no algebraic irreducibility is inferred.

READ: the corrected theorem excludes a single tableau all of whose components
have fewer than D* vertices, where D* is the separating onset in the same regime.
Thus our candidate is in that excluded family **iff 50<D***. If D*<=50 it is on
the large-component side, which that theorem does not exclude. We do not know
which numerical alternative holds, and do not assert D*<=50. The record's
same-regime floor D*>=8 does not settle this. Tail 132>d=50 cannot be reduced to
degree 132 by the t<d factorization; the erratum explicitly preserves that limit.

This is an honest conditional scope check, not a certified escape. The
determinant certificate rejects the candidate irrespective of D*.

### B22-02 L1--L6

* L1 (semicontinuous thresholds): no statistic or threshold construction defines
  this f. A newly arranged contraction is not itself a direction comparison.
* L2 (nonvanishing is open): f(q0)>0 supplies its required ambient nonempty open
  set. We do not try to support a polynomial only on a singular locus.
* L3 (polynomial extraction from rank minors): no derivative matrix or kernel
  extraction defines this contraction. This is not a proof that f avoids every
  possible minor ideal; no such universal claim is made.
* L4 (nullcone and cubic-valued covariants): lambda is nonrectangular, and is not
  of the cubic-output form (3+k,k,k,k,k). We use neither a positive-degree SL5
  invariant nor a cubic-valued covariant lift. A nonrectangular weight supplies
  no padding certificate.
* L5 (second-fundamental-form and catalecticant bounds): at five variables the
  quoted rank-6 and rank-36 bounds are vacuous; neither defines the redesign.
* L6 (restriction to a cubic factor): its determinant-ideal hypothesis fails
  here by PROOF.md section 3. No smooth-cubic result or numerical onset theorem
  is used to construct f.

Historical claims in B22-02 equating actual padding with all products, and its
B17-01 smooth-cubic premise, are not adopted here.

### GKZ rank-threshold theorem

READ: the corrected theorem puts its specified rank-threshold ideals in the
common determinant/padding ideal. It is not a theorem about all contractions,
all incidence constructions or all minors. Our f is outside each of those
determinant-vanishing ideals because f(Q^2)>0 at a literal determinant.
This explains non-applicability of that particular route; it does not turn f
into a viable separator. No old dependency status is promoted by this reading.

### A25-02 Application 3

READ: M7 has linear quartic-coefficient entries; the size-299 minors generate
a homogeneous ideal with no nonzero part in coefficient degree below 299.
Our nonzero degree-50 f therefore does not belong to that ideal. This is a
degree argument, without numerical replay. The recorded comparison retains its
precise status: the padding ceiling 245 is proved; the determinant floor 299 is
CERTIFIED-modular at one prime. We do not call the comparison premise-free or
assume the maximum determinant rank is exactly 299.

### Old common pair

READ: B26-02 proves equality on (p4,D4) for all old members and their linear
combinations. Our equation (3) proves that the new f is not globally blind to
Sym^4(V), so that global blindness argument no longer applies. It does **not**
prove f(p4)!=f(D4). We do not reuse (p4,D4) as a separation pair or claim that
this particular pair is distinguished. q0 is an ambient visibility point and
Q^2 is a different, explicitly specified determinant rejection point.

## 3. Price and stopping conditions

These are hand-proof budgets and symbolic operation/storage bounds, not measured
compute timings. No pilot or mathematical program is proposed or run.

| Check | Exact manual object and budget | Where cheap work stops |
|---|---|---|
| Admissibility/visibility | 200 boxes; three specified color assignments; Vandermonde factors 288,12,420,270,2; 10-minute hand-review allowance | Gives the exact polynomial dependence through finite coefficient sums. It does not evaluate actual padding. Completed. |
| Determinant side | One 4-by-4 skew pencil, five scalar moments, and the elementary Cartesian-grid lemma; 10-minute hand-review allowance | Formula (8) gives f(Q^2)>=1/(3^50 12^250)>0. Rejection completed; universal identity work is unnecessary. |
| Padding side, had the candidate survived | Use only the literal substitution p4=A(A+B) with Y and padding coordinate from audited note 2 section 2. First hand check its nine matrix entries and l=z (5 minutes); then allow 15 minutes to find a contraction reduction for this exact merged pattern | The old cycle formula does not apply after the merge. Without a new reduction or an exact signed evaluation, mark survival unresolved. This stage is canceled after rejection, rather than silently inheriting the old positive value. |

For precision, the padding fallback is fully finite. The direct epsilon
contraction has at most

    N = (5!)^20 (4!)^2 (2!)^46

signed terms. Each contains 50 entries of the p4 tensor; those entries lie in
{0,1,1/3,1/6}. A streamed sum needs at most 50N rational arithmetic operations
plus O(N) additions; a common denominator 6^50 suffices, with numerator
bit length at most 1+ceil(log2(N*6^50+1)). Storing the 200-box pattern and at
most 70 independent tensor coordinates is small, but enumerating N terms is
not a cheap hand certificate. We do not run, authorize or recommend that
enumeration. A reduction of this sum, or another exact actual-padding value,
would be the missing padding certificate.

For determinant membership in the counterfactual absence of (8), one would
need the full identity

    f(det(x1 I4+x2 A2+x3 A3+x4 A4+x5 A5))=0

as a polynomial in 64 matrix entries, of total degree at most 200. A grid with
201 values in each of 64 entries would suffice, requiring 201^64 evaluations
and their exact certificates. This is a completeness bound, not an affordable
plan or a proposed program. Dense coefficient storage has upper bound
binom(264,64) entries before coefficient bit costs. A structural identity would
be needed for an economical positive. A few zero evaluations would not suffice.
The invertible x1 chart extends by homogeneity and density to all pencils;
here a nonzero value already lies on that chart.

## 4. Feasibility boundary

This packet demonstrates that recovering B^2 visibility can coexist with a
decisive determinant failure. Within the paired quartic construction in
PROOF.md, the positive finite-moment representation is the exact obstruction.
A future separately authorized proposal must evade that positivity obstruction
and supply its own visibility and actual-padding certificates. No second
pattern, signed combination, new degree or candidate family is nominated here.

A25-10's READ programme decision remains "no construction ready."
