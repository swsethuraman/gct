# gct — project notes

Programme: **conductors and deficits of orbit closures** (the anabelian↔GCT
dictionary, made computational). Swami & Claude. This file is the standing
context for the project: state of results, assets, infrastructure protocol,
and roadmap. Update it at the end of every working session.

## Living documents

- **Conductors of Orbit Closures** (working paper):
  https://claude.ai/code/artifact/f760534b-e2a3-4329-aafb-4d2cbc18204b
- **The Boundary Deficit** (companion log, all tables + session records):
  https://claude.ai/code/artifact/261ce77d-09ef-42a0-90f7-853bbbb9d842
- Repo: `C:\Users\swami\Projects\gct` (canonical durable copy; the cloud
  container is scratch — see Infrastructure below).

## Mathematical state (results bank — all machine-verified, exact arithmetic)

**Central object.** For v characterized by its symmetries, H = stab(v),
Ω̄ = closure of G·v: def(λ,δ) = dim S_λ^H − mult_λ C[Ω̄]_δ ≥ 0 (the boundary
deficit); conductor c(λ,δ) = stabilization index along the Δ-ray = pole order
of missing functions along the boundary. Ray stabilization: Ikenmeyer–
Kandasamy Lemma 5.2; everything below concerns the exact minimal index.

**World A — σ₂(v₄), binary quartics (solved).** def = c = max(0, ⌊(a−3b)/8⌋)
for every weight; support law b ≤ δ−2; max conductor ⌊δ/2⌋; total deficit
⌊δ²/4⌋. Verified δ ≤ 60; closed-form proofs (Sylvester model + collapse
argument). Tower ⌊(a−3b)/8⌋⁺ → [b=1] → 0; non-normality gap = one S_(4δ−1,1)
per degree.

**World B — Aronhold/Fermat cubic.** Conductor transport theorem:
c(λ) = ⌊(λ₁−2λ₃)/6⌋ = ⌊μ_max(λ)/|w_N|⌋ on all 254/254 deficit-positive
weights δ ≤ 10 (upper bound proved; attainment machine-verified). Orphan
weights (10,1,1), (13,1,1): contraction shadow reports pole 1 but Young
projection kills the top (deficit 0). Level-2 tower is wild: non-reductive
conic-tangent stabilizer (torus diag(1,−2,4) + nilpotent), no floor law.

**det₃ (week 3 headline).** e(det₃) = 18 = 2n², NOT n²: answers
Bürgisser–Ikenmeyer for n = 3 (first determinant whose fundamental invariant
misses degree n²). Census: dim Sym^δ(Sym³C⁹)^{SL₉} = 0 for δ < 18, = 1 at 18
(combinatorial proof + Murnaghan–Nakayama plethysm census). The value:
Φ₁₈(det₃) = −877,879,296,000 = −2¹⁶·3⁷·5³·7² ≠ 0 (quadruply cross-checked:
reversed-order DP, transpose pairing, n=2 anchor e(det₂)=4, 36-subproblem
decomposition). Φ₁₈(perm₃) = +50,536,120,320 = 2²⁰·3⁴·5·7·17; ratio
−4725/272; ⟹ perm₃ ∉ Ω̄(det₃) by invariant evaluation.
Discriminant corollary: V(Φ₁₈) ∩ Ω̄ = ∂Ω̄ exactly (both boundary components
in the null cone; direct evaluation 0 at both representatives).
div(Φ₁₈) = 6P₁ + 9P₂ (session 9: Ω̄ smooth along generic P₁, ramification 6;
P₂ wild/non-normal, m₂ = 9 by torus integrality). Deficit calculus:
def((2,2,2),2) = 1 (first determinant deficit); totals 1, 6, 31, 141, 618,
2488 through δ = 7; δ=2 row exact (0,0,1); deficit class indecomposable.

**NEW — the banked 36-subproblem computation is COMPLETE (2026-08-24).**
    TOTAL_f1C = 2 × 576,072,000 = 1,152,144,000
Factored HWV evaluation (wk3_s8_gen3.py pipeline) at point C (the unipotent
translate of det₃: x₅ → x₅+x₁, x₇ → x₇+x₂), scheme 1, 36 subproblems
(σ₆,σ₇) ∈ S₃×S₃ reduced to 18 orbit reps by the proven symmetry
π = (1 2)(3 6)(4 8)(5 7) (sign +1). Full table in results/results_f1C.md.
Validations: independent duplicate pair 00 = 07 exact; all final-states 1;
19/19 values fit V = W(σ₆⁻¹σ₇) with W(id) = +108,712,800,
W((0 1)) = W((1 2)) = −21,772,800, W((0 2)) = −476,884,800,
W(3-cycle) = +301,870,800 — 8 of these were blind predictions that hit
exactly; signs = sgn(σ₆)sgn(σ₇) throughout.

**VERDICT (pinned by the log's session-10 criterion): c((2,2,2), 2) = 1 —
the first conductor of a determinant.** Session 10 corrected session 9's
prediction (2 → 1: the divisorial transport says one Φ₁₈-step clears both
components, ⌈2/6⌉ = ⌈2/9⌉ = 1; c ≥ 2 would require divisorial extension to
FAIL, i.e. non-normality arithmetically active at the first deficit weight)
and stated the criterion verbatim: "Zero means the wild component's pathology
is arithmetically active from the very first class; nonzero means the
divisorial calculus rules and c = 1." The grind returned NONZERO
(1,152,144,000), so: the k=1 slot is filled, divisorial transport rules on
its first test on a determinant, and non-normality does not bite at (2,2,2).
The k=1 evaluation is the λ' = (8,8,8,6⁶), δ = 20 HWV at the balanced-
substitution orbit point C (session 8's counting lemma forces evaluation off
det₃ itself onto such points). Both documents updated with the verdict on
2026-08-24. Follow-ups: independent second-point confirmation (another
balanced substitution point), and the k = 2 rung of the ray.

**SESSION-12 VERDICT (2026-08-26 03:20Z): R1 COMPLETE ON BOTH LEGS.**
(1) **Second-point certificate: TOTAL_R = 1,152,144,000 ≠ 0** at
R = (x₃+=x₀, x₇+=x₁), PROVEN H-inequivalent to C (intersection-algebra
double-coset invariant: 𝔰(u_C) non-abelian vs 𝔰(u_R) abelian, exact).
11 runs, all final-states valid, all three relation gates matched, every
pre-logged prediction hit. Full record: results/results_R.md.
(2) **k=2 closed ray-complete** (product certificate + even-parity
transport; see below): def(λ_k, 2+18k) = 0 ∀k ≥ 1 — the first fully
resolved ray of a determinant. **c((2,2,2),2) = 1 stands, hardened.**
(3) **Universality discovered (11/11 + 36 + 2 empirical)**: the W-table
{+108,712,800; −21,772,800; +301,870,800; −476,884,800} and hence the
total 1,152,144,000 are point-independent across BOTH live H-classes of
balanced points — the certificate value is an invariant of the ray class,
not of C. Rigidity theorem = next-session target (formulation logged
below; amb(λ′,20) = 3 caveat).
(4) Companions: P-point exact vanishing (rank-1, results_P.md); Q = C
conjugate (validation); f1D_00 engine zero; taxonomy of the 15 feasible
balanced points into rank-1/cyclic/diagonal.
(5) **Φ₁₈(h1gen) provenance: PARKED.** The plain evalfile path hit a
deterministic "RUN OVERFLOW" crash loop at L6 (NEW ENGINE LIMIT for the
notes: the non-ck2 do_level has a fixed spill-run cap; h1gen's density
gives 699,485,585 states at level 5 of 18 — an evalopts-scale problem).
If ever wanted: build a det3cal-style FACTORED/evalopts input for
Φ₁₈ at h1gen's monomials (checkpointed, sharded) — est. several hours.
h1gen remains provenance-open and computationally irrelevant (dead as an
evaluation point either way).

**Session 12 (2026-08-25, R1 hardening) — grind in flight.**
Regression: full suite exact on the fresh container, including a COMPLETE
f1C_00 rerun → VALUE +108,712,800, final states 1, 61 min (new per-
subproblem time baseline; old estimate was 45).
h-series contracts enumerated (wk3_s8_gen2.py): h{s}{P} = scheme s ∈ {1,2,3},
evalfile2 format (8 cols, widths 9⁶3², 60-bit state), at unipotent translates
A: x₅+=x₁; B: x₇+=x₂; C: both (the grind point); D: x₃+=x₀ & x₈+=x₁.
h1gen = a 28-monomial dense translate, generator NOT in repo (provenance
gap; Φ₁₈ SL₉-invariance check queued — expect −877,879,296,000 if orbit).
**Weight-support feasibility (wk3_s8_feas DFS, demand (8,8,8,6⁶)): A, B, D,
E, F are INFEASIBLE — h1A/h1B/h1D are lemma-forced ZEROS (negative
controls, NOT certificate points). Feasible: C, G, h1gen-point.** Full sweep
of all 81 balanced two-transvection points (x_{3+j}+=x_a, x_{6+k}+=x_b):
exactly 15 feasible, including three 10-monomial column-uniform points
(x₃+=x₀,x₆+=x₀), (x₄+=x₁,x₇+=x₁), (x₅+=x₂,x₈+=x₂).
Unfactored h-runs measured at ~14× a factored subproblem (short columns
stay open to L19–20; ~6B-state peaks, ~42 GB concurrent disk) — killed at
L7; see Infrastructure rule 7. Factored route instead: wk3_s12_genD.py
generates 36-subproblem evalopts sets from a raw monomial list
(VALIDATED: regenerates the banked f1C set byte-identically 0/36; af
anchors −8/−24 exact). Profiles vs f1C_00: f1gen 56× (dead), f1G 2.4×
(~44h — rejected), **f1P 1.7–1.9× (chosen)**.
**Second certificate point P = (x₃+=x₀, x₆+=x₀)** — column-0-uniform,
disjoint from C's transvections, 10 monomials. Signed symmetries fixing
{x₀,x₁,x₂} setwise form a Klein 4-group: row-swap (3 6)(4 7)(5 8) (s=−1,
ρ=id), col-swap (1 2)(4 5)(7 8) (s=−1, ρ=(1 2)), and their product
(1 2)(3 6)(4 8)(5 7) (s=+1, ρ=(1 2)) — the SAME permutation as point C's π.
Derived sign calculus (to be validated by the duplicate pair): for ANY
signed point-symmetry here, V(ρσ₆, ρσ₇) = +V(σ₆,σ₇), since s²⁰ = +1
(even copies), sgn(π)⁶ = +1 (even wide-column count), sgn(ρ)² = +1 (two
short columns). ⟹ 18 orbit pairs, no fixed points, TOTAL_P = 2·Σ(18 reps).
**LEMMA (derived 2026-08-25 mid-grind; retroactive mechanism of session
11's observed law).** Scheme 1's automorphism group is a Klein 4-group:
θ_b = (1 2)(3 4)·[6↔7] (subproblem action: swap (σ₆,σ₇) ↦ (σ₇,σ₆), i.e.
rel ↦ rel⁻¹) and θ_d = reversal (0 5)(1 4)(2 3) (action: post-composition
by ω = (0 2), rel ↦ ωrelω); with the pre-ρ point symmetry these generate
an order-8 action on the 36 subproblems with 8 orbits (sizes 4,4,8,4,8,4,
2,2), and V is constant on each orbit with sign +1 throughout (validated
36/36 against the banked C table — the W-class structure W(rel)=W(rel⁻¹),
W((0 1)) = W((1 2)) ≠ W((0 2)) is exactly ⟨swap, post-ω⟩-invariance).
The REMAINING cross-orbit equalities (the rel-only refinement: V const on
{orb0,orb6}, {orb1,orb2}, {orb3,orb4}, {orb5,orb7}) stay UNPROVEN — logged
as blind predictions for P below. Referee-shape: proven part vs predicted
part. (Hindsight accounting: the 19-run C grind was ~2.4× the orbit
minimum; the surplus bought the empirical law that became this lemma.)
Grind (TRIMMED to the extended-orbit design): 11 runs = 8 orbit reps
{00,01,02,03,04,05,14,16} + per-relation duplicates {07 = pre(00),
06 = swap(01), 34 = post(02)} — each relation type empirically confirmed
on P before its orbit weight is trusted; the weighted total uses ONLY
orbit-constancy, never the unproven rel-law.
    TOTAL_P = 4·V00 + 4·V01 + 8·V02 + 4·V03 + 8·V04 + 4·V05 + 2·V14 + 2·V16
Blind predictions, logged BEFORE any P value exists: (i) V00 = V14,
(ii) V05 = V16, (iii) V01 = V02, (iv) V03 = V04 [the rel-only law at P].
**OUTCOME (P grind, 4 runs completed then stopped): V(00) = V(07) =
V(01) = V(02) = 0 — every one by EXACT TERMINAL CANCELLATION at level 19**
(L18 still carries ~10⁹-scale weights in 100+ states; the final short-
column-7 closure emits 56–76 transitions and every accumulated state
weight cancels to exactly 0; zero-weight states are dropped, hence "final
states 0"). NOT structural absence: the SAT screen (analysis/
wk3_s12_satfeas.py, validated vs C) shows completing paths exist at every
checked P-assignment. Pair gate 00 = 07 matched (at zero) — pre-relation
validated. Orbits 0, 1, 2 (16/36 subproblems) dead; grind stopped, 03/04
checkpoints preserved in gct-run/p1,p2 for optional later resume.
**Mechanism hypothesis (logged as conjecture): P is RANK-1** — both
transvections source the same variable x₀ (u = I + (e₃₀+e₆₀), rank-1
nilpotent). Content forces every completing path to use exactly 4
substituted legs, so h₁(u_t·det₃) = t⁴·(single coefficient): a pure 4th
directional derivative along a rank-1 direction, which evidently vanishes.
The sweep's three column-uniform points are exactly its rank-1 points —
conjecture: h₁ vanishes identically on all three; certificates need
rank 2 (C was rank 2). None of the (π,θ)-symmetry relations can force
these zeros (their signs are point-independent and C's values are
nonzero) — this is a NEW vanishing mechanism, worth a lemma if proved
(candidate route: sign-pairing on the 4 substituted legs' column choices).
**Q-episode (17:00–18:10Z): Q = (x₄+=x₀, x₆+=x₁) is C IN DISGUISE.**
Its first two runs returned V(00) = +108,712,800 and V(01) = −21,772,800 —
EXACTLY C's W-values. Proved: p_Q = colperm(0 2 1)·p_C with the column
3-cycle ∈ stab(det₃) (sympy-exact), and the Levi character on h₁ is +1,
so all Q-values must equal C's. Grind stopped; the two runs are banked as
the strongest pipeline validation yet (banked W-values reproduced through
entirely different input files at a conjugate point).
**THE INDEPENDENCE INVARIANT (lesson + classification).** A balanced
two-transvection point is N = E₁₀⊗F + E₂₀⊗F′; its H-orbit is classified
by the pencil span{F,F′} ⊂ gl₃ up to conjugation (+ a-side GL₂ rebasing,
transpose). The 15 feasible points fall into exactly THREE classes:
rank-1 (span{F} 1-dim; the 3 column-uniform points; VANISHING — engine
evidence + conjecture), CYCLIC (non-commuting pencil, e.g. {F₂₁,F₁₂};
6 points, ALL H-conjugate to C), and DIAGONAL/DD (commuting pencil
{F_ii,F_jj}, i≠j; 6 points, all mutually conjugate, provably NOT conjugate
to C — pencil commutativity is conjugation-invariant; finite signed-
stabilizer search also empty). ⟹ exactly TWO live H-classes; the genuine
second point is any DD representative.
Banked reading (Swami, mid-grind): Q's two runs are a genuine independent
RECOMPUTATION of h₁(C) ≠ 0 (different input files, option tables,
σ-indexings) — the weaker independence bar (recomputation) is now cleared
twice over (original grind + Q's H-translate; plus today's f1C_00 rerun);
R chases the stronger bar (nonvanishing at an H-inequivalent point).
For R, logged BEFORE values land: predictable — orbit-constancy under the
point-independent scheme automorphisms (dups 14/06/34 test it) and, IF the
scheme-intrinsic reading of C's structure is right, the 6/12/12/6
class-weight profile echo. OPEN QUESTION (not a prediction): whether R's
four W-values relate to C's four at all — DD substitutions preserve column
mass individually (same-column trades), a different feasibility arithmetic
from C's cross-column trades.
Endgame tree: R nonzero → certificate complete at a provably inequivalent
point + first DD data. R zero by cancellation → h₁ vanishes on every
balanced point outside C's own H-class (a remarkable structural fact — the
k=1 class as a near-delta function on balanced points) and the certificate
routes through G (three-transvection, 2.4×) next.
**Certificate grind: R = (x₃+=x₀, x₇+=x₁), DD-class, launched 18:10Z.**
11 monomials, SAT-live, point symmetry π = (1,0,2,7,6,8,4,3,5) sign +1,
ρ = (0 1) → 8 orbits, weights {00:4, 01:8, 02:4, 03:8, 04:4, 05:4, 07:2,
09:2}, duplicates 14 = pre(00), 06 = swap(01), 34 = post(02).
    TOTAL_R = 4·V00 + 8·V01 + 4·V02 + 8·V03 + 4·V04 + 4·V05 + 2·V07 + 2·V09
Gates: three duplicate matches + (states 1 or exact-zero (0,0)) per run.
Assembly: scripts/assembleR.py (computes orbits itself). R's W-values are
the first genuinely new data since C. ETA ~01:30Z with negD + phi tails.
**R vs C: INEQUIVALENCE PROVEN (exact).** The intersection algebra
𝔰(u) = 𝔥 ∩ Ad(u)𝔥 transports by Ad(h₁) along double cosets H·u·H, so its
Lie type is a point-equivalence invariant. Exact rational computation:
𝔰(u_C) = 4-dim NON-abelian (bracket span 2); 𝔰(u_R) = 4-dim ABELIAN;
(𝔰(u_P) = 8-dim). ⟹ p_R ∉ H·p_C. [Correction to rule 8's first draft:
pencil-conjugacy is also not the right invariant — point-equivalence is
the DOUBLE COSET; 𝔰(u)'s Lie type is the clean computable obstruction.]
**UNIVERSALITY (upgraded from curiosity to primary hypothesis, per Swami:
the per-subproblem functional N ↦ V_{σ₆,σ₇}((I+N)·det₃) as a degree-4
H-covariant on the direction space plausibly spans a 1-dim covariant
space: value = universal W(σ₆,σ₇) × Ψ(N), Ψ an H-invariant ~ function of
Λ²N — vanishing iff rank 1 (P's death), constant on live classes (Q, R
echoes), rel-only law = property of W alone).** Engine record at R so far
(6 runs, all final-states 1): V(00) = +108,712,800 [id], V(01) =
−21,772,800 [(1 2)], V(02) = −21,772,800 [(0 1)], V(03) = V(04) =
+301,870,800 [3-cycles], V(05) = −476,884,800 [(0 2)] — ALL FOUR
W-classes equal C's exactly, including both designated hard discriminators.
**Predictions logged 23:20Z 2026-08-25, BEFORE the last five runs land
(testing universality + orbit-constancy):** V(07) = +108,712,800;
V(09) = −476,884,800; gates V(14) = V(00), V(06) = V(01), V(34) = V(02);
TOTAL_R = 6·W_id + 12·W_small + 12·W_3cyc + 6·W_(02) = 1,152,144,000
= TOTAL_C exactly (the 6/12/12/6 profile echo).
**Rigidity formulation (next-session theorem target; subtlety found).**
Ψ_σ(N) = V_σ((I+N)·det₃) is degree-4 in N ∈ W = C²⊗gl₃ (content forces
exactly 4 substituted legs) but is a MATRIX ELEMENT, not a naive covariant:
Ψ_σ(N) = ⟨h₁-functional, Φ₄(N)⟩ with Φ₄: Sym⁴W → (λ′-isotypic of
Sym²⁰Sym³C⁹) equivariant along the W-preserving parabolic P_H ⊂ H.
Computed tonight (wk3_s7_ray, 627 outer partitions / 94,167 power-sum
classes): **amb(λ′,20) = 3** — the ambient λ′-HWV space is 3-dimensional
(schemes 1/2/3 = hwv1-3 are the natural candidate basis; independence
unverified). So rigidity = a statement about the rank of the composite
on balanced directions, not multiplicity-1 for free; the theorem needs
either the P_H-branching computation dim Hom_{P_H}(Sym⁴W, Res 3·S_λ′)
or an empirical rank probe (scheme-2/3 evaluations at C and R — banked
h2C/h3C contracts, factorable the same way). NOTE: amb = 3 is the ambient
ceiling; closure mult = 1 = dim S^H_{λ₁} stands (session-10 verdict
unaffected). Tail add-ons: f1D_00 engine zero (resumes
banked checkpoint); Φ₁₈(h1gen) provenance. NOTE: f1G_*/f1gen_* input sets
are NOT banked (dead routes; regenerate via wk3_s12_genD.py in one command).
**k=2 rung: CLOSED ALGEBRAICALLY (2026-08-25) — no grind, and the whole
ray with it.** Two halves:
(i) Floor (mult ≥ 1): F = Φ₁₈·h₁ is a HWV of weight λ₂ = λ₁+(6⁹), degree 38
(multiplication by the boundary equation IS the ray step); F(C-point) =
Φ₁₈(det₃)·h₁(C-point) = (−877,879,296,000)·(1,152,144,000) =
**−1,011,443,363,610,624,000,000 = −2²³·3¹¹·5⁶·7³·127 ≠ 0**, using
Φ₁₈(u·det₃) = Φ₁₈(det₃) (SL₉-invariance, u unipotent). Banked integers only.
(ii) Ceiling (dim S^H = 1 transports): S_{λ+6·1⁹} ≅ S_λ ⊗ det₉⁶ exactly, and
det₉|_H is trivial on H⁰ (det₉(u,v) = (det u · det v)³ = 1) and −1 on the
transpose coset (τ: 3 off-diagonal 2-cycles ⟹ det₉(τ) = (−1)³ = −1); the
ray twist det₉⁶ is an EVEN power ⟹ trivial on ALL of H ⟹
dim S_{λ_k}^H = dim S_{(2,2,2)}^H = 1 for EVERY k ≥ 0. Verified explicitly
this session (the parity of the transpose was the one place a surprise
could hide). Combined with def ≥ 0: def(λ_k, 2+18k) = 0 for all k ≥ 1
(inductively, Φ₁₈^{k−1}·h₁ ≠ 0 in the domain C[Ω̄]).
**Corollary (log next to the certificate): the full ray profile of the
first deficit weight of det₃ is exact — def = 1 at k=0, def = 0 for all
k ≥ 1: the first fully-resolved ray of a determinant, c((2,2,2),2) = 1
ray-complete.** (The (2,2,2) rung escaped session-8 indecomposability only
because one factor is the invariant itself — the "trivial" decomposition
that is the ray; the δ=3 nontrivial weights do not.)
**δ=3-row engine scope (week-4 target, where the engine investment
belongs).** Ray points
λ+6·1⁹ at δ′=21 for λ ⊢ 9: raw state is ALWAYS 63 bits (54+9) with
NE = 6+λ₁ up to 15; after factoring out height-≤3 extra columns
(S_h-assignment subproblems, h! each): 24/30 shapes fit the CURRENT engine
(NEf ≤ 8, ≤ 60 bits; subproblem counts 1–216, worst (3,3,3) at 216);
the 6 breaches — (3,2,2,2) 62b, (3,1⁶) 61b, (2,2,2,2,1) 63b, (2,2,1⁵) 61b,
(2,1⁷) 62b, (1⁹) 63b — exceed ONLY the `off > 60` guard, never NE=8, and
the spill codec is general LEB128 varint: the next-engine spec is a
one-line guard relaxation 60 → 63 plus full-regression revalidation (verify
no hidden tag bits in key high bits; ADD AN EXPLICIT ASSERT that no
deposited state has an all-zero mask — key = 0 is the hash table's
empty-slot sentinel, an invariant that today holds by accident of every
level-≥1 state carrying a bit and must be made explicit at 63 bits;
mix() is full-width, shard_of top-10-bit extraction fine for KB ≤ 63,
int64 value headroom ample at 21 copies), NOT a two-word rewrite. k=2-style
direct eval (12 wide columns, 108 factored bits) stays out of reach and
stays unnecessary.

**SESSION 13 (2026-08-27): the rigidity slot is 3-dimensional — P explained,
universality sharpened to a measurable rank statement.** After resync to
4999fb0 (stale-snapshot incident resolved; rules 9–10 below), the n=3
covariant-space count is COMPLETE (docs/rigidity_formulation.md,
analysis/wk3_s13_covcount.py; validation-first: 7 exact brute-force
branching cross-checks, Sym⁴W dimension audit 5985, transpose-side
double-computation of the key multiplicity):
    m = 3 = [mult 3 of (ρ=(2,2), triv-GL₃ᵇ) in Sym⁴W] ×
            [mult 1 of S_(24,18,18)⊗S_(20,20,20) in S_λ′(C³⊗C³)];
    all other α-blocks (24,19,17), (24,20,16) pair to ZERO.
So: every scheme/subproblem functional is a det²_{GL₂}⊗triv_{GL₃} pencil
covariant in span{u₁, u₂, D} (basis in the doc; the naive third generator
(trAtrB−trAB)² is NOT in the slot — machine check caught it); rank-1
vanishing is now a LEMMA (P's zeros = representation theory, not accident);
substituted legs are forced balanced t=(2,2); universality is NOT free
(m > 1) — it is the statement that all (h,σ) select one line, confined by
the C=R data to span{u₁−2u₂, D}. Free prediction logged: TOTAL_G =
1,152,144,000 (implied, not discriminating). The discriminating probe is
the feasible 11-monomial four-transvection point T4 = {x₃+=x₀, x₄+=x₁,
x₇+=x₁, x₈+=x₂} with (v,D) = (3,5) vs C's (1,1): its total, plus
scheme-2/3 runs at C, measure the actual line — next engine session.
n=4: framework in the doc; the numeric count is gated on e(det₄) and
det₄'s first deficit weight (both open).

## Computational assets (repo layout)

    engine/dp.c        exact streamed level DP (the workhorse; see below)
    engine/bit.c, bit3.c   earlier bitmask evaluators (anchors/cross-checks)
    scripts/           w1.sh w2.sh resume.sh (grind workers), assemble.py,
                       deficit.py
    analysis/          wk1_*.py (World A), wk2_*.py (World B),
                       wk3_*.py (det₃; s8_gen3 = factored-HWV input generator,
                       s9_p1 = P₁ transport, s11_sym = symmetry search)
    inputs/evalin/     72 evaluation inputs: det3cal (calibration), f1C_00..35
                       (the completed grind), h1A–h1D / h2A–h2D / h3A / h1gen
                       (banked h-series evaluations, NOT yet run — enumerate
                       their exact meaning from wk3_s8_gen*.py next session),
                       a42_* / af_* (S(4,2) anchors, Fermat/cusp/random pts)
    results/           results_f1C.md (canonical grind record), ASSEMBLY.md
    docs/              artifact URLs, this file

**Engine (dp.c).** Modes: quad|quad0|quadq (validation), det3/perm3 [maxlev],
det3sub c, evalfile, evalopts (grind mode: checkpointed + sharded).
State = packed per-ε 9-bit used-variable masks (54 bits in u64); levels
stream from disk; 2^26-slot open-addressing table; sorted spill runs,
delta-varint compressed (~5.5×, ~3.2 B/rec); bounded shard passes
(P auto-doubles when 6 GB scratch budget trips; DPBUDGET env overrides);
atomic ck2 checkpoints at every spill (kill-9/OOM/suspension-safe, ~5 min
granularity). Canonical regression (must match exactly after any change):
quad=24, quad0=0, quadq raw 6 ×4=24; det3 6 → L2 29/29/29, L3 623/656/656,
L4 13595/13595/14314, L5 197501/224542/235558, L6 1818118/2336283/2686868;
f1C_00 profile L7 54685987/100774838/141001840, L8 128027708/422952740/
603408404. Grind cost: ~45 min/subproblem, 2 cores, 7 GB RAM, 30 GB disk.

## Infrastructure protocol (hard-won; do not relearn)

1. **The cloud container is scratch.** It suspends on ~7–10 min idle (killing
   all processes), can silently ROLL BACK hours of filesystem state (it ate
   the grind outputs once), and is reclaimed between sessions. The repo at
   C:\Users\swami\Projects\gct is the only durable copy. Sync at session
   start (stage repo in), commit + write back at every milestone.
2. **Keepalive**: long-running compute survives only while the session is
   active — run `sleep 540`-then-status bash cycles in-turn. Recurring
   scheduled tasks fire into FRESH EMPTY containers (never use them to babysit
   container state); `send_later` DOES deliver back into the same session and
   container — it is the correct dead-man's switch.
3. **Workers**: launch via setsid (`resume.sh`); wrappers retry-until-VALUE
   (never advance past an unfinished subproblem); everything resumes from
   ck2 checkpoints. Never run extra compute beside two workers (RAM budget).
4. **pkill -f self-match footgun**: a `-f` pattern matching your own shell's
   command line kills the shell. Use `pkill -x` exact names, or bracket-trick
   patterns (`f1C_0[3]`) — and remember the pattern can match OTHER text in
   your own compound command (a later pgrep string bit us on 2026-08-25).
   Killing by explicit PID is the only fully safe form.
5. Shell cwd can reset mid-command in this environment: use absolute paths.
6. **Permission-gate rule (added 2026-08-25).** The client prompts for
   approval (Alt+Enter) the first time a session issues a new command shape;
   an unattended session waiting on that prompt does nothing, idles, and the
   container suspends mid-turn (7.4h frozen on 2026-08-25 — dead-man's switch
   recovered it). Before any unattended stretch, exercise every command shape
   the babysit loop will need — one sleep cycle, one worker (re)launch, one
   status check, one commit + bundle write-back — while a human is still at
   the keyboard. Never introduce a new command shape into the loop right
   before walking away.
7. **evalfile/evalfile2 modes are NOT checkpointed** (no ck2): only evalopts
   is grind-safe. Unfactored h-series runs measured ~14× a factored
   subproblem in states (short columns stay open to L19–20; ~6B-state peak
   levels, ~42 GB concurrent disk vs ~30 available) — unfactored λ'-evals are
   disk-infeasible on this container. Factor first.
8. **Independence is H-conjugacy, not novelty of slots/sources** (2026-08-25,
   the Q lesson): a "different-looking" substitution can be a stabilizer
   translate — vet a candidate second point by the H-orbit invariant (here:
   the nilpotent pencil span{F,F′} up to conjugation; commutativity, rank,
   cycle structure), never by surface features. Screens don't see conjugacy,
   the way they don't see signs (P) or cancellation (SAT).
9. **Exactly one session owns Projects\gct at a time** (added 2026-08-27
   after the stale-snapshot incident: a rolled-back container re-derived
   already-certified work and nearly overwrote the true bundle). Ownership
   is granted by Swami explicitly; a session that has not been told it is
   the owner reads but never writes the folder. On any clock jump,
   container restart, or restore, assume rollback: reconcile against the
   folder's bundle and the project docs BEFORE trusting the local tree —
   and treat "rediscovering" a result as a rollback alarm, not a finding.
10. **HEAD verification before write-back** (same incident). At session
   start, record the staged bundle's HEAD here as the sync baseline. Before
   ANY write-back, re-stage Projects\gct\gct.bundle and verify its HEAD
   still equals that baseline (`git bundle list-heads`); on mismatch STOP
   and ask — someone else has written. After writing back, the new HEAD
   becomes the next session's expected baseline. Record the baseline at
   every sync.
11. **The laptop's work/ clone is canonical; bundles are transport**
   (added session 14). Projects\gct\work is the durable repository;
   gct.bundle/gct.zip are the transport artifacts sessions read and write.
   Updates land in work/ by `git -C work pull ..\gct.bundle main` as
   --ff-only merges ONLY — a bundle whose head does not fast-forward
   work/ means divergence: stop and reconcile, never force.

## Sync state

Sync baseline (bundle HEAD this session cloned from): 921bb60
Owner session: claude.ai/code/session_01LZn1KGnc3bAMqWUPoSkuRn (session 14, 2026-08-28)

## Conventions

- Exact arithmetic only (int64 / sympy Rational); every numerical claim
  machine-checked in-session before it enters a document.
- Adversarial validation habit: independent second routes, symmetry pairs,
  anchors, blind predictions. A number without a cross-check is a draft.
- The two artifacts are updated IN PLACE at their existing URLs (version
  history preserves the trail). PDFs are print snapshots, not sources.
- Session numbering continues the boundary-deficit log (last: session 10 +
  the grind session of 2026-08-24).

## Roadmap (refreshed 2026-08-24)

R1. **Harden the c((2,2,2),2) = 1 verdict**: independent second evaluation
    point (another balanced substitution pair), then the k = 2 rung of the
    Φ₁₈-ray (does the deficit stay cleared — conductor exactly 1 confirmed
    ray-wise). The h-series inputs (h1A–D, h2A–D, h3A in evalin/) are the
    banked evaluation family — enumerate their exact contracts from
    wk3_s8_gen*.py; budget ~45 min each on the grind engine.
R2. **Publishable statement**: "the first conductor of a determinant is 1"
    with the divisorial-transport mechanism and the nonzero certificate;
    fold into conductor §5 (done 2026-08-24) and the paper narrative.
R3. **Which boundary component(s)**: evaluate Φ₁₈ at Hüttenhain's
    representatives (traceless determinant, universal quadric) — §7(3).
R4. **World B level-2 law**: increments as unipotent invariants of the
    non-reductive conic-tangent stabilizer; full Ogg–Shafarevich sum — §7(1).
R5. **Orphan characterization**: which empty-support weights kill the shadow
    maximum — §7(2).
R6. **The general conjecture**: c = ⌊μ_max/w_N⌋ for all symmetry-characterized
    forms with dense boundary orbit, smooth point, 1-dim stabilizer torus —
    §7(4).
R7. **Write-up**: promote the conductor draft toward submission (deficit
    tables from the log as ancillary files; MathSciNet prior-art pass);
    dc(perm₃) = 7 comparison for the det-world discriminant story.
