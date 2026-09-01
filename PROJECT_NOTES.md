# gct — project notes

## STATUS AT A GLANCE (2026-08-30 — read before anything below)
ESTABLISHED (no covariance assumption was ever used in any of these):
  World A solved; World B conductor transport (254/254).
  e(det3) = 18 = 2n^2; Phi18(det3) = -877,879,296,000; V(Phi18) ∩ closure
  = boundary exactly; div(Phi18) = 6P1 + 9P2; perm3 ∉ closure(det3).
  def((2,2,2),2) = 1; c((2,2,2),2) = 1, RAY-COMPLETE (def = 0 for all k>=1).
  TOTAL = 1,152,144,000 at C and at R (H-inequivalent, proven).
LEMMAS / METHODS that survive: displacement-cancellation lemma; integrality
  theorem (719); scheme-automorphism Klein lemma; taxonomy of the 15 balanced
  points; intersection-algebra double-coset invariant.
  The session-13 count m = 3 REMAINS VALID as a computation of that Hom-space;
  what is refuted is the premise that V^h_sigma lives in it.
RETRACTED 2026-08-29 (sessions 13-15 headers below are superseded):
  the rigidity theorem; V^h_sigma as a det^2-covariant; V^h_sigma as a
  simultaneous-conjugation invariant; TOTAL_G = 1,152,144,000 (G never run,
  value OPEN).
SESSION 21 (2026-08-30/31): 24 IS IN E. Phi_24(det_3) = -24,745,222,656,000
  = -2^12 3^7 5^3 7^2 . 11 . 41 != 0, so def((8^9),24) = 0,
  mult_{(8^9)} C[closure]_24 = 1, and E(det_3) contains <18,24> = 6.<3,4>.
  The ambient census (new, exact, cheap) is what collapsed it:
  dim C[Sym^3 C^9]^{SL_9}_delta = 0,0,0,0,0,1,0,1,1,4 for delta = 3..30 step 3,
  so the degree-24 ambient space is a LINE and a zero would have been as
  decisive as a nonzero. E/6 now omits at most {1,2,5} and contains 1,2 as
  gaps: EXACTLY ONE DEGREE UNDETERMINED, namely 30.
SESSION 19: Psi = -I_6^prim(I,A,B) EXACTLY — Psi is the Aronhold degree-6
  invariant of the net's tensor in slab normal form (symbolic identity, 18
  indeterminates).
SESSION 22: **the totals law TOTAL(N) = Psi(N) x 1,152,144,000 is a THEOREM.**
  The chi <-> det^2 gap closed: chi = det(q)^6 det(q|V/W)^2 = det(q|V/W)^2
  (8 = 6+2, det(t) = +-1 on BOTH cosets of H, 6 even), and
  det(q|V/W) = det(G)^{-1} with G the net's parameter change = the third tensor
  slot — so chi is det^2 in exactly the slot where Psi carries det^2. 58/58
  exact checks; the transpose coset is harmless twice over. Open problem (2) is
  SOLVED at the totals level. Per-sigma values remain refuted/unexplained.
  Untested prediction of the theorem: TOTAL_{X-3} = -3,456,432,000.
OPEN PHENOMENON (data, no mechanism): identical W-tables at C, R, Q, T4 —
  four points, three inequivalent pencil classes. Every value is
  75,600 x integer (the 151,200 claim is REFUTED, session 23; the ten
  enumerated cofactors 719 / -2038 / 5907 / -4372 ... are multiples of 151,200
  but W(3-cycle) and three X_-3 values are odd multiples of 75,600).


Programme: **conductors and deficits of orbit closures** (the anabelian↔GCT
dictionary, made computational). Swami & Claude. This file is the standing
context for the project: state of results, assets, infrastructure protocol,
and roadmap. Update it at the end of every working session.

## Living documents

- **Conductors of Orbit Closures** (working paper) — private artifact; the
  committed snapshot is `docs/conductor.html`.
- **The Boundary Deficit** (companion log, all tables + session records) —
  private artifact; the committed snapshot is `docs/boundary_deficit.html`.
- Repo: the canonical durable copy lives on the owner's machine; the cloud
  container is scratch — see Infrastructure below.  Artifact URLs and local
  paths are deliberately not recorded here, since this file is public.

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

**SESSION 14 (2026-08-28): RIGIDITY DETERMINED — rank 1, line 2v−D, whole
ambient space.** Full record: results/results_T4.md; pre-registrations
committed BEFORE every value (8e9f51e, 7af9d09); 5/5 predictions exact.
(1) Scheme-1 line measured at T4 = {x₃+=x₀,x₄+=x₁,x₇+=x₁,x₈+=x₂} (third
pencil class, invertible-containing): ratio = 1 uniform ⟹ Ψ ∝ 2v−D;
gate V(00)=V(35) exact. (2) LS runs: f2T4_00 and f3T4_00 hit the shared-
line predictions exactly ⟹ schemes 2,3 evaluate through the SAME
covariant — the full 3-dim ambient multiplicity space has rank 1 on
balanced pencils: V^h_σ(N) = W^h(σ)·(2v−D)(N). (3) Integrality theorem:
κ₂ = 1043/1438, κ₃ = 115/719 make σ-table proportionality non-integral ⟹
the three ambient HWVs are pairwise-independent functionals (amb = 3 basis
honest). (4) Ψ = 2v−D explains all banked structure: Ψ(C)=Ψ(R)=Ψ(T4)=1,
Ψ(rank-1)=0 (P), TOTAL_G = TC standing (un-run). Curiosity for the record:
T4's and R's scheme-1 DP L8 profiles coincide exactly (states/emitted/
sum|w|) — mask-reachability coincidence across distinct points. Theorem
now an exact target: composite Sym⁴W → ambient* has rank 1 with image
span{2v−D} on the balanced cone. Next: prove it (P_H-analysis of Φ₄), and
the scaling falsifier stays available as a cheap check.

**SESSION 15 (2026-08-28, math only): the rank-1 theorem PROVED on the
measured classes; two lemmas; the decisive off-locus runs designed.**
docs/rigidity_theorem.md is the deliverable. (1) Proof by interpolation:
slot theorem (s13) + invertible evaluation matrix at C/R/T4 (det 2) ⟹
V^h_σ = W^h(σ)·Ψ with Ψ = 2v−D EXACTLY, proven in full for (h₁, id) and
(h₁, (0 2)); other classes confined to explicit planes ∋ Ψ, each closed by
ONE pre-registered run: f1T4_01 = −21,772,800, f1T4_03 = +301,870,800,
f2R_00 = +78,850,800, f3R_00 = +17,388,000. (2) The suggested a-priori cut
provably cannot work: proportional AND rank-1-locus vanishing annihilate
the whole slot (symbolic). (3) NEW displacement-cancellation lemma:
content feasibility ⟺ ∃ 2+2 conversions with Σ(e_tgt − e_src) = 0
(proof via forced t=(2,2) + integral Birkhoff for 3×3); derives the 15/81
sweep and D/A/B/E/F structurally. (4) Ψ-locus: dichotomy FALSE — 48 values
in [−40,53] over the {0,1} cone; mod-4 lemma PROVED (Ψ ≡ 2s−s², s =
trAtrB−trAB). (5) DECISIVE pre-registered runs, verified feasible+SAT-live,
inputs banked f1X4_*/f1Xm3_*: X4 = {x₃+=x₀,x₇+=x₂,x₈+=x₁}, Ψ = 4,
TOTAL = 4,608,576,000, V_00 = +434,851,200; Xm3 = {x₃+=x₂,x₄+=x₁,x₇+=x₁,
x₈+=x₀}, Ψ = −3, SIGN-FLIPPED table, TOTAL = −3,456,432,000, V_00 =
−326,138,400. Next engine session: the 4 completing runs + X4 + Xm3
(~6 runs ≈ one overnight, closes the theorem and tests the quartic law
off the unit locus).

**SESSION 16 (2026-08-29): the rigidity theorem is RETRACTED — two
receiving-space hypotheses falsified by their own pre-registered tests.**
Full record: results/results_T4.md (session-16 addendum) and the RETRACTION
NOTICE atop docs/rigidity_theorem.md.
(1) Completing runs 4/4 HIT (f1T4_01, f1T4_03, f2R_00, f3R_00) — the
interpolation identity through C/R/T4 is confirmed for every measured class.
(2) **f1X4_00 = −308,145,600, gate-confirmed by f1X4_35** — vs the
pre-registered +434,851,200. The session-13 det²-slot is refuted: individual
matrix elements V^h_σ do not inherit GL₂-covariance (h is a GL₉-Borel HWV;
the scheme/σ choice breaks it). Input integrity was verified two independent
ways before concluding.
(3) f1Xm3_00 = +893,138,400 (vs −326,138,400): second refutation.
(4) Recovery fit over the 10-dim bidegree-(2,2) conjugation-invariant space
reached rank 9 (max on the feasible cone) and predicted, parameter-free,
f1Y4_00 = +69,854,400. **Engine returned 0** ⟹ that space is refuted too;
the full system is rank 9 / aug-rank 10, and the violated relation spreads
over nearly every point (residual −628,689,600), so it is not an outlier.
V^h_σ is NOT a simultaneous-conjugation invariant. (The relation C = Q is
satisfied exactly — the machinery is sound.)
(5) UNTOUCHED: c((2,2,2),2) = 1, TOTAL_R = 1,152,144,000 at an
H-inequivalent point, k=2 ray-closure — no covariance assumption was ever
used there. SURVIVING: the displacement-cancellation lemma; the integrality
theorem (factorization V_σ = W(σ)Ψ impossible at X4, via the prime 719 in
W(id)); the empirical universality itself (identical W-tables at C, R, Q, T4)
— now an unexplained regularity.
(6) **WITHDRAWN: TOTAL_G = 1,152,144,000** — it rested on the refuted fits.
G has never been run; its value is open.
(7) Leads for the next attempt: A ∝ I or B ∝ I ⟹ 0 (Y1/Y2/Y3); rank-1 ⟹ 0
(P, now needing an independent proof); Y4's complementary-projection zero
(AB = 0, A+B = I) — a third mechanism; and the arithmetic that every value
is 75,600 × an integer with cofactors (relative to 151,200) 719 / −2038 / 5907
— see session 23: the 151,200 form of this claim is refuted.
Engine note: V^h_σ is a bidegree-(2,2) polynomial in the 18 direction
coordinates (forced by the counting lemma's t = (2,2)) in a space of
dimension up to 2025 — sampling at ~2h/point cannot pin it; a structural
route is required.

**SESSION 17 (2026-08-29, math only): the evaluation's TRUE symmetry —
double cosets Q·u·H. Deliverable: docs/evaluation_symmetry.md.**
Conventions verified from scratch (Q = Levi GL3xGL6, 3-space = first row,
agreeing with the counting lemma's 24 = 3*8), with ONE refinement: Q is the
parabolic in which the weight-8 block RECEIVES from the weight-6 block
(binary-form check; the opposite orientation puts every u_N inside Q and
predicts V == 0, refuted instantly). THEOREM: V is constant on Q·u·H up to
chi; since Q = Stab(W), the double coset of u_N is the H-orbit of
Gamma_N = u_N^{-1}(W), i.e. of the 3-dim annihilator NET in M_3 under
X -> aXb (+transpose) — whose classical invariant is its determinantal plane
cubic. Convention pinned by HOMOGENEITY (V(2N) = 16 V(N) forces
V(N') = chi(q)V(N), chi = det(q|quotient)^8 det(q|W)^6 — returns exactly 16).
KEY CORRECTION made in-session: the theorem constrains TOTALS, not per-sigma
values (the sigma-decomposition is scheme bookkeeping, not Q- or H-stable);
testing it per-sigma produces a spurious contradiction.
CONFIRMED RETRODICTIONS: R and T4 are in the SAME coset with chi = 1 —
first structural explanation of any part of the universality; Q_pt = C
(H-conjugate, chi = 1); homogeneity.
HONEST NEGATIVE: **C and R are in DIFFERENT cosets** (vertex-rank invariant
[1,2,2] vs [1,1,1], transpose-stable) yet have equal totals — so the symmetry
does NOT explain the universality of the two certificate points. The group is
smaller than the phenomenon. Also died: the determinantal cubic's projective
type as the invariant (too coarse — C, R, T4, X4 are all triangles).
NEW EMPIRICAL CRITERION (independent of the symmetry, 5/5): **compression
=> 0** — every non-infeasible banked zero has a net of generic rank <= 2 with
a common left kernel; every nonzero point has generic rank 3. This UNIFIES
the three open vanishing leads from session 16 (rank-1 P; A or B ∝ I at
Y2/Y3; complementary projections at Y4) plus the base point N = 0.
**PRE-REGISTERED (banked, NOT run): TOTAL_X4 = 4 x 1,152,144,000 =
4,608,576,000.** R and X4 share a double coset with chi = 4 (explicit
connecting element, det(a)det(b) = -4). Risky: both known X4 sigma-values are
negative while the predicted total is positive; the six unmeasured orbit
values must contribute +8,485,344,000. Cost 6 runs (~1 overnight) — the
decisive next-session engine test. NOTE the convergence: the retracted
Psi = 2v-D theory predicted the SAME total; the theories disagree per-sigma
(which killed Psi) but agree on the total, so the test discriminates
"both wrong" from "both right about totals".

**SESSION 18 (2026-08-29/30): the totals-level law CONFIRMED, and Psi DERIVED.**
Two results, both first-of-kind for the programme.
(1) **TOTAL_X4 = +4,608,576,000 = 4 x 1,152,144,000 exactly** (ratio
4.000000 = Psi(X4)), from a complete 8-value orbit assembly. This is the
FIRST test of TOTAL(N) = Psi(N) x 1,152,144,000 at a point with Psi != 1 —
the audit showed only C and R had measured totals and both sat at Psi = 1.
Pre-registered in session 17 (67db6e8) before six of the eight values
existed; the intermediate constraint 4c03 + 2c16 = -10,136 was pre-registered
at eed6c05 with both runs live. Demanding by the end: after six values the
sum OVERSHOT (40,616 vs 30,480 cofactor units), so confirmation required the
last two to be strongly negative, which they were. Full ledger with honest
epistemics (the final forced value was committed 7s after it hit disk —
derived blind but not a clean pre-registration) in results/results_T4.md.
(2) **Psi is DERIVED, not fitted** (docs/psi_identification.md): the net has
closed form Gamma^perp = {[v; Av; Bv]}, whose 3x3x3 tensor slabs are exactly
(I, A, B); fixing slab0 = I collapses SL3xSL3 to conjugation; and Psi is the
UNIQUE (up to scale) bidegree-(2,2) conjugation invariant in the det^2-slot
that is slab-equivariant with character det^2 (D_A f + 2 tr(A) f = 0, likewise
D_B). The -4 coefficient is forced. Interpolation through C/R/T4 now only
fixes a normalisation. Corollaries: shift-invariance, compression => Psi = 0
(also proved as an identity: all compression points share slot coords
(2,0,4)), and chi = Psi on 120/120 same-coset pairs. Both plane-cubic routes
are dead (degree count: no degree-2 invariants of ternary cubics; plus three
triangles with Psi = 0, 1, 4), and the pencil cubic is insufficient too
(Psi needs the length-4 word u2). I6 is no longer needed to pin Psi.
STILL OPEN: per-sigma values (session 16's refutation stands — at X4 the
sigma-table reorganises, it does not rescale); why the evaluation should
follow this equivariant object at all (the I6 question, now well-posed);
and TOTAL_G, still un-run and un-predicted.

**SESSION 19 (2026-08-30, math only): Psi IS the Aronhold invariant. Open
problem (2) is REFRAMED, not solved. Deliverable: docs/i6_identification.md.**
ANCHOR FIRST (step 2, exact before anything else): the complete-epsilon-
contraction machinery was validated on 2x2x2, where the answer is known.
Reference cross-validated two ways (12-term Cayley polynomial == discriminant
of det(x S0 + y S1), symbolic); then rank of the 27-pattern span = 1;
SYMBOLIC IDENTITY contraction = -2 x Det_Cayley on the generic 8-variable
tensor; anchors rank-1 => 0 (x2), W-state (rank 3, tangent) => 0, GHZ => 1,
generic rank-2 => 9,572,836 = (det(u,u')det(v,v')det(w,w'))^2 = 3094^2 exact.
VERDICT (O1, in a stronger form than O1 was stated):
    **I_6( I , A , B )  =  -6 * Psi(A,B)**, an EXACT symbolic identity in all
18 pencil indeterminates. Not "Psi is the (2,2) component of the tensor
generator" -- the restriction HAS no other component. Proved lemma: each
slot-1 epsilon needs three DISTINCT slab indices, so each 3-block uses I, A, B
once each and the slab multidegree is forced to (2,2,2). Content of I_6 is 6,
so with the primitive integral normalisation **Psi = -I_6^prim(I,A,B),
coefficient 1** -- the -4 on u2 that session 18 derived from equivariance is
simply what the Aronhold invariant does.
Machinery/identity audit: fast 2-stage evaluator == naive 18-index contraction
(5 patterns); rank of the 100-pattern degree-6 span = 1; SL3 invariance in all
three slots; character det^2 confirmed (scaling a slot by 2 gives 64);
**I_6 has exactly 1152 monomials on the generic 3x3x3 tensor, matching
Bremner-Hu's Aronhold I_6** -- an independent identification of the object.
STEP 3 HONOURED: no census law was transported. The vanishing rule was
RE-DERIVED as a transposition lemma (identical copies + epsilon antisymmetry:
if two copies share a block in all three slots the pattern is fixed by that
transposition with sign -1). Proved; predicts exactly the 64 observed zeros of
100 (the converse is observed at 20 random points, not proved).
STEP 4 CITATION: Vinberg (1976), theta-group analysis of the Z/3-grading of
E6: the SL3^3 invariant algebra of 3x3x3 arrays is FREELY generated in degrees
6, 9, 12 -- hence dim(degree 6) = 1 exactly. Confirmed from Bremner, Hu &
Oeding, Math. Comput. Sci. 8 (2014) 147-156 (arXiv:1310.3257), which credits
Vinberg for precisely this and Nurmiev (2000) for the normal forms; explicit
generators in Bremner-Hu, Math. Comp. 82 (2013). Our rank-1 computation is an
independent confirmation.
STEP 5 was PRE-REGISTERED at c06ba3f before any comparison was computed, and
the pre-registration was strong: the character argument (I_6 is a GL3
semi-invariant with character det^2 in each factor; the induced condition
D_A f + 2 tr(A) f = 0 is bidegree-preserving) makes **O2 A-PRIORI IMPOSSIBLE**,
leaving only O1 (c != 0) and O3' (c = 0). Logged prediction: O1. It landed.
STEP 6: every banked value consistent, nothing adjusted --
Psi/I_6-over-(-6) = 1,1,1,1,4,-3,0,0,0,0 at C, R, T4, Q, X4, Xm3, P, Y2, Y4,
N=0; measured TOTALs 1,152,144,000 (C), 1,152,144,000 (R), 4,608,576,000 (X4),
0 (P + four compression points) all match Psi x TOTAL_C.
COROLLARIES: compression => 0 is now the classical degeneracy of the Aronhold
invariant; session 17's chi = Psi on 120/120 same-coset pairs is forced (a
tensor semi-invariant must transform by its character), not a coincidence.
**CORRECTION to session 18 (found while pre-registering; it STRENGTHENS the
theorem).** The bidegree-(2,2) simultaneous-conjugation space is 9-dimensional,
not 10: the ten trace words satisfy one relation (polarised Cayley-Hamilton for
3x3), and session 18's "second nullspace vector" IS that relation. In FUNCTION
space, **slab-equivariance alone leaves exactly 1 dimension, spanned by Psi** --
the det^2-slot was never needed for the characterisation.
**BOUNDARY, stated plainly (and in the deliverable): this does NOT prove the
totals law.** It says which canonical object Psi is; it says nothing about why
the h1 evaluation -- a GL9-Borel HWV in Sym^20 Sym^3 C^9, with no tensor in
sight -- should follow it. TOTAL(N) = Psi(N) x 1,152,144,000 remains EMPIRICAL
(tested at Psi = 1, 4, 0). Per-sigma values are untouched; session 16's
refutation stands.
**NEXT-STEP DESIGN (not a result).** The remaining step now has a candidate
proof with ONE named gap: (i) TOTAL is bidegree (2,2) [s15 counting lemma,
proved]; (ii) TOTAL is constant on Q.u.H up to chi and the coset is the H-orbit
of the net AS A SUBSPACE [s17, proved]; (iii) subspace-only dependence would
make the net's basis change (third tensor slot) act trivially, so TOTAL would be
a conjugation invariant with a slab equivariance of character chi [NOT verified
-- the transpose coset and the slot dictionary need checking]; (iv) IF chi is
det^2, session 19's uniqueness forces TOTAL = c.Psi with c = 1,152,144,000 from
C. The single unproved link is **chi <-> det^2** (s17's 120/120 is evidence,
not proof). Before: no proof route. Now: a route with one gap.


**SESSION 21 (2026-08-30/31): the degree-24 question is answered. 24 IS in E.**
Full record: results/results_deg24.md; pre-registration results/PREREG_deg24.md
(commit f9b4485, logged before any value existed); route-(i) analysis
docs/degree24_extension.md. Branch s21-degree24 (theory track was working main
in parallel; nothing here touches main).
(1) **THE VALUE.** Phi_24(det_3) = -24,745,222,656,000 = -2^12 3^7 5^3 7^2 .
11 . 41 != 0. Hence 24 in E(det_3), def((8^9),24) = 0,
mult_{(8^9)} C[closure]_24 = 1, and E contains <18,24>. Phi_24 is the SECOND
GENERATOR of the invariant semigroup ring - a new generator, not a product,
since there is no degree-6 invariant on the closure to multiply Phi_18 by. This
is the invariant whose existence Corollary 4.7 forces (gcd E = 6, min E = 18,
so E != 18N) and which had never been exhibited.
(2) **THE REDUCTION, which is the transferable part.** Restriction
C[Sym^3 C^9] -> C[closure] is surjective on SL_9-invariants (reductivity), so
C[closure]^{SL_9}_delta is the image of the AMBIENT invariant space. New tool
analysis/wk4_s21_census.py computes dim C[Sym^3 C^m]^{SL_m}_delta =
<h_delta[h_3], s_{((3delta/m)^m)}> by applying the adjoint power-sum operators
p_r^perp (rim-hook removal) to s_lambda, using
  sum_delta t^delta h_delta[h_3] = exp(sum_r (p_r^3+3p_r p_2r+2p_3r) t^r/(6r)).
Every intermediate partition is a subdiagram of lambda, so the ENTIRE state
space is the partitions inside the m x (3delta/m) box - 24310 for (8^9). Exact
rationals, seconds. Result for m = 9, delta = 3,6,...,30:
    0, 0, 0, 0, 0, 1, 0, 1, 1, 4.
Validated against ternary cubics (0,0,0,1,0,1,0,1,0,1,0,2,0,1 in degrees 1-14 =
Hilbert function of C[S,T], deg 4 and 6), cubic surfaces (1 at 8, 0 at 12, 2 at
16), and the banked delta=18 census. TWO SHARPENINGS FOR THE NOTES: delta = 21
is PERMITTED by the pigeonhole census (21 <= C(7,3) = 35) but the exact
multiplicity is 0 - the exact count is strictly sharper than the bound; and
delta = 30 is FOUR-dimensional, so the one-number collapse does not repeat
there.
(3) **ROUTE (i) IS DEAD, PROVABLY.** div(Phi_18) = 6P_1+9P_2 with
Phi_18|orbit = Phi_18(det_3).phi^3 gives ord_{P_1}(phi) = 2, ord_{P_2}(phi) = 3,
so div(phi) >= 0 and the divisorial argument would conclude 6 in E - FALSE.
"Effective divisor hence regular" is Serre's criterion and needs normality; the
closure is not normal and P_2 is where that sits. No divisor computation on the
closure can decide degree 24. **What survives is new and useful:** phi IS
regular on the normalisation, so C[closure^nu]^{SL_9} = C[phi] is a polynomial
ring with degree monoid exactly 6N, and C[closure]^{SL_9} is the semigroup ring
of S = E/6 inside it. The gaps of S are exactly the degrees at which the
non-normality is arithmetically visible on invariants, and the semigroup
conductor IS the conductor of the invariant ring in its normalisation.
(4) **NEW ENGINE: engine/br2.c** (do not confuse with dp.c). Bracket-monomial
evaluator for cubics supported on the six 3x3 permutation monomials. A
degree-24 bracket monomial is a 24-subset S of the 56 triples of [8] with every
bracket in exactly 9; B(S) = c_S . Phi_24. State = the 9-bit used-cell masks of
the PARTIALLY FILLED brackets only (empty -> 0, full -> 511 implicit), packed 9
bits each into a u64 - at most 7 partial in the orders used, so 63 bits, which
is why 8 epsilons fit at all (a naive state is 72 bits). Exact __int128
(|V| <= 36^24 = 2.2e37 < 2^127). Per level, P sharded passes over the previous
level file with P doubling on table overflow, so nothing depends on the shard
count. Peak 258,319,584 states at level 14; 6255 s at 2^27 slots (3.2 GB) and
~10 GB scratch. NOTE FOR THE NEXT SESSION: the letter ORDER is chosen to keep
the partial-bracket front <= 7 (analysis/wk4_s21_spec.py has the refined
state-count proxy - it uses the fact that every letter deposits exactly one
cell in each ROW and each COLUMN, so the per-bracket masks carry global margins;
that proxy is ~100x tighter than prod C(9,d) and is what made the run
plannable).
(5) **THE CHEAP CERTIFICATION TRICK, reusable.** On the 6-dim space U of cubics
sum_sigma u_sigma x_{1 sigma1}x_{2 sigma2}x_{3 sigma3} (which contains det_3 at
u = sgn and per_3 at u = 1), the torus weight condition
sum_sigma e_sigma M_sigma = 8J has exactly nine solutions
e = (a,a,a,8-a,8-a,8-a), so Phi_24|_U = sum_a K_a P^a Q^{8-a} is a BINARY OCTIC
in P = u_id u_c u_{c^2}, Q = u_t1 u_t2 u_t3. A row/column permutation of odd
total sign swaps P and Q and acts trivially on det^8, so K_a = K_{8-a}.
Restricting u to the even permutations returns K_8; to the odd, K_0. Those runs
cost 114 s against the main run's 6255 s (3 permutations per letter, tighter
masks) and they do two jobs: nonzero certifies c_S != 0 - which is exactly what
makes a ZERO in the main run decisive - and K_0 = K_8 is a symmetry gate.
Both landed at -1,428,295,680 at structure S, and at -203,212,800 at a second
structure S'.
(6) **PREDICTION LEDGER: 5 pre-registered, 5 hit.** (i) 24 in E, alternatives
ranked 30 then 42 [f9b4485]; (ii) K_a = K_{8-a}, so even-only = odd-only
[f9b4485]; (iii) that same symmetry pairs indices of EQUAL parity and therefore
cannot annihilate sum (-1)^a K_a, i.e. nothing forces vanishing [f9b4485];
(iv) c_S'/c_S = 35/246, logged at b0401a8 BEFORE either expensive run finished,
forcing V(det_3,S') = (35/246) V(det_3,S) - **HIT, -3,520,661,760,000, all
thirteen digits**, peak 535,918,500 states at level 16, 8888 s; (v) odd-only at
S' = even-only at S'. So Phi_24(det_3) != 0 is certified at TWO bracket
structures with Phi_24(det_3)/K_8 = 17325 at both. Bonus, SINGLE ROUTE
ONLY, flagged provisional (not reproduced by a second structure):
**Phi_24(per_3) = -4,016,526,151,680 = -2^12 3^3 5 . 7 . 41 . 25309** (25309
prime), ratio Phi_24(det_3)/Phi_24(per_3) = 155925/25309, Phi_24(per_3)/K_8 =
25309/9. NOTE it is NOT a multiple of 151,200 - and neither is Phi_18(per_3);
the arithmetic signature is about det_3 evaluations only. Do not quote the
permanent value as confirmed until a second bracket structure reproduces it.
S' was chosen with a different pair-degree profile ((1,1),(2,14),(3,5),(4,7))
from S's ((1,4),(2,10),(3,10),(4,2),(5,2)), so the two are provably not related
by any relabelling of the eight brackets.
(7) **REGRESSION, exact.** br2.c at delta = 18 (6 brackets, 18 letters, S_18 =
C(6,3) minus a complementary pair) reproduced BOTH banked integers to the last
digit from independent code on an independent bracket structure:
u = sgn -> -877,879,296,000; u = 1 -> +50,536,120,320; ratio -4725/272.
Peak 138,241,908 states at level 8, 1678 s.
(8) **NORMALISATION-FREE NUMBERS** (c_S cancels): Phi_24(det_3)/K_8 = 17325 =
3^2 5^2 7 . 11, identical at S and S'. At delta = 18 the same construction gives
Phi_18(det_3)/K'_6 = 4725 = 3^3 5^2 7 and Phi_18(per_3)/K'_6 = -272 = -2^4 . 17,
whose quotient IS the banked -4725/272 - so the two banked values are the
numerator and denominator of a single K'_6-normalised pair. Also:
Phi_24(det_3) = 75,600 x (-327,317,760) - the arithmetic signature survives
into a different degree on a different engine, still unproved. And
Phi_18 = -2^16 3^7 5^3 7^2, Phi_24 = -2^12 3^7 5^3 7^2 . 11 . 41 share the odd
part 3^7 5^3 7^2 exactly; ratio 451/16. No explanation.
(9) **WHERE THE SEMIGROUP STANDS. Exactly one degree is undetermined: 30.**
S = E/6 has multiplicity 3, contains 3 and 4, so contains <3,4> = N \ {1,2,5};
1 and 2 are known gaps. Either E = <18,24> or E = <18,24,30>. Every
two-generated numerical semigroup is symmetric, so the first holds iff
C[closure]^{SL_9} is Gorenstein - offered as the shape of the dichotomy, not as
evidence. Either way the answer names the last gap and hence the exact
conductor of the invariant ring in its normalisation: 36 or 24. Degree 30 is
NOT a one-number question (ambient dim 4): nonvanishing is still one
evaluation, but vanishing needs all four. **delta = 30 IS NOW SCOPED - see docs/degree30_scoping.md,
do not launch it blind.**

**SESSION 22 (2026-08-30, math only, branch `s22-chi`): STEP (iii) CLOSES —
TOTAL(N) = Psi(N) x 1,152,144,000 IS A THEOREM.** Deliverable:
docs/chi_det2.md (pre-registration 2545f1e, result b2569f1). No engine run.
PRE-REGISTERED FIRST: predictions P1-P5 with five named falsifiers (F1-F5);
none fired. THE TWO NAMED GAPS:
(1) **The character is a square, and the transpose coset cannot contribute.**
Since lambda' = (8,8,8,6^6) and 8 = 6+2,
    chi(q) = det(q|V/W)^8 det(q|W)^6 = det(q)^6 det(q|V/W)^2,
and q = u_{N'} t u_N^{-1} with both u's unipotent gives det(q) = det(t) = +-1
on H (det(aXb) = (det a det b)^3 = 1; transpose = -1 on M_3). Six is even, so
**chi = det(q|V/W)^2** on BOTH cosets. Same parity that closed the k=2 ray.
(2) **The slot dictionary.** Rebuilt from scratch (banked pencils and Psi values
reproduced 6/6 before anything else): Gamma_N = ker(first three rows of u_N), so
Gamma_N^perp = rowspan(those rows) and the j-th row IS the net element with rows
(e_j, A e_j, B e_j). Hence the canonical parameter v is the u_N-transported basis
of W^perp, (V/Gamma_N)* = Gamma_N^perp, and **det(q|V/W) = det(G)^{-1}** where G
is the induced change of the net's parameter — the THIRD TENSOR SLOT, the one H
does not act on. So **chi = det(G)^{-2}: the character is det^2 in the parameter
slot.** H acts only on slots 1 and 3 (rows and columns of the net matrix), with
(det a det b)^{-2} = 1, so Psi = -I_6^prim transforms by exactly the same factor.
VERIFIED 58/58 exact cases (seven checks each: q in Q; det q = det t; the 8=6+2
identity; the dictionary; chi; the Psi law; and the non-unimodular accounting
chi = m^18 det(G)^{-2} with evaluation factor m^{-20}chi = m^{-2}det(G)^{-2}),
across both cosets, banked and random pencils; plus the pure-scaling consistency
check (g = mu I_9 gives factor exactly 1) and the homogeneity calibration
(chi = s^4 for N -> sN, which is what pins the exponent's sign).
**THE TRANSPOSE IS HARMLESS TWICE OVER** — it cannot enter chi (det(t)^6 = 1),
and the slot-1<->3 swap acts on the 1-dim degree-6 invariant space by the
TRIVIAL character (two routes: all 29 transpose-coset cases satisfy the Psi law
with a + sign; and Psi does not vanish on the 9-parameter family of tensors
fixed by that swap, which it would have to under the sign character). This was
the single most dangerous check in the session (falsifier F4).
UNIQUENESS RE-VERIFIED INDEPENDENTLY (F5): dim of bidegree-(2,2) simultaneous-
conjugation invariants = **9** by an SL_3 character computation (multiplicity of
the trivial in Sym^2(gl_3) (x) Sym^2(gl_3); dim 45 and 2025 as sanity checks),
independent of the trace-word basis; imposing the two equivariances DERIVED HERE
leaves 2 dimensions of coefficients = **1 dimension in function space**, both
nullspace vectors constant multiples of Psi.
**CORRECTION to sessions 18/19 (changes nothing).** The slab renormalisation is
RIGHT multiplication, (A,B) -> (A(I+tA)^{-1}, B(I+tA)^{-1}), not the recorded
left version; the two differ by conjugation by (I+tA), so on conjugation-
invariant functions they impose the same condition and the recorded
characterisation of Psi stands verbatim.
**RESOLVED: session 17's honest negative.** C and R are in different double
cosets yet have equal totals — recorded since session 17 as an unexplained
coincidence ("the group is smaller than the phenomenon"). It is now forced: the
group is too small to connect the points, but the space of functions it
constrains is ONE-dimensional, so the law crosses cosets even though the group
does not. Session 18's chi = Psi on 120/120 same-coset pairs is likewise an
identity now, not agreement.
**WHY det^2, AND THE GENERALISATION (new, untested).** For a deficit weight
lambda' = (p,p,p,q^6) the same computation gives
chi = det(t)^q det(q|V/W)^{p-q}: the parameter-slot character is det^{p-q}, so
the governing object should be the SL_3^3 invariant of degree 3(p-q) — Aronhold's
I_6 here (p-q = 2), the degree-9 Vinberg generator at p-q = 3, degree-12 at 4.
And when q is ODD, chi acquires -1 on the transpose coset while any det^even
semi-invariant does not, FORCING TOTAL = 0 on every direction whose net is
H-equivalent to its own transpose. One evaluation would test that.
**STILL OPEN, unchanged:** per-sigma values (session 16's refutation stands
untouched; the sigma-table is scheme bookkeeping, stable under neither Q nor H);
TOTAL_G un-run; and the two consumed inputs — the counting lemma and the
double-coset theorem — were used as given, not re-derived.
**STANDING ENGINE HANDOFF (pre-registered, NOT run — for the engine track):**
X_{-3} = {x3+=x2, x4+=x1, x7+=x1, x8+=x0}, Psi = -3:
    **TOTAL_{X-3} = -3,456,432,000**, whole sigma-table sign-flipped.
Inputs banked (inputs/evalin/f1Xm3_*; measured V00 = +893,138,400). Eight orbit
reps, about one overnight on two workers. This is now a THEOREM's prediction and
the first test at a negative Psi; a miss would indict the counting lemma or the
double-coset theorem, since the chi identification is now an identity.
PAPER: revised on this branch — Theorem 5.5 is a theorem with a proof (two new
lemmas: the character is a square; the slot dictionary), inputs stated as a
lemma, abstract updated, Question 7.2 replaced by the other-weights question,
and the C = R remark now explains rather than marvels. Compiles clean, no
undefined references.
BRANCH DISCIPLINE: all work on `s22-chi`, pushed to `s22-chi` only; main
untouched, no write-back to any durable copy on the owner's machine.


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
   The durable copy on the owner's machine is the only one. Sync at session
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
12. **Launch each worker wrapper exactly ONCE, and verify the scratch
   directory is unowned before starting an engine** (session-16 incident: a
   duplicate `setsid ... wS16c.sh` put two engines on the same directory,
   both writing the same lev*.dat/ck.txt — caught within a minute, both
   killed by PID, state wiped, run restarted clean; no corrupted value
   entered the record). Before launching: `ps -o pid,ppid,cmd` and confirm no
   dp2g already owns that dir. After launching: confirm exactly one wrapper
   and one engine per dir. Count wrappers by PPID — a bare `pgrep -f wS16`
   also matches your own shell's command line (the read-only cousin of
   rule 4's footgun).

## Sync state

Sync baseline: the Projects\gct bundle tip advances with each write-back,
so the check is FAST-FORWARD, not string equality: stage the bundle,
`git bundle list-heads`, and verify the tip is an ANCESTOR of local HEAD
(`git merge-base --is-ancestor <tip> HEAD`). A tip that is an ancestor is a
previous write-back of ours; a tip that is NOT an ancestor means another
writer — STOP and ask, per rule 10. Session-17 start: aa3d0ff.
Session-18 mid-session write-back: from tip 67db6e8 (our own session-17
write-back) forward.
Session-19 start (2026-08-30): staged tip 97d26ec, ancestor test PASSED
(equal to local HEAD after clone; no divergence, no stale-writer alarm).
Session-19 write-back advances the tip to the commit recorded below; the next
session must ancestor-test against THAT.
Owner session: sessions 14-17, through 2026-08-29 (session id withheld)
Owner session (sessions 18-19, 2026-08-29/30): this session, SINGLE OWNER of
the durable repo per rule 9.
Session-21 (2026-08-30/31): worked entirely on branch s21-degree24 in the cloud
container, cloned fresh from the public GitHub repo (tip a5d461a at clone). It
did NOT own the durable folder and wrote nothing to it; the theory track was on
main in parallel. Push to origin was BLOCKED by the session's git proxy
(swsethuraman/gct not in the authorised repository set), so the branch was
delivered as a git bundle. Swami merges.

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

R1. **[COMPLETE — sessions 12-16.** Second-point certificate at R
    (H-inequivalent, TOTAL_R = 1,152,144,000) and the k=2 rung closed
    ray-complete; the rigidity follow-on was attempted and RETRACTED, see
    the status header. Nothing here remains open.]
    Harden the c((2,2,2),2) = 1 verdict: independent second evaluation
    point (another balanced substitution pair), then the k = 2 rung of the
    Φ₁₈-ray (does the deficit stay cleared — conductor exactly 1 confirmed
    ray-wise). The h-series inputs (h1A–D, h2A–D, h3A in evalin/) are the
    banked evaluation family — enumerate their exact contracts from
    wk3_s8_gen*.py; budget ~45 min each on the grind engine.
R1b. **[COMPLETE - session 21.** Degree 24: Phi_24(det_3) != 0, the second
    generator of the invariant semigroup ring exhibited. Successor: **degree
    30**, the single undetermined element of E, ambient dimension 4.]
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
