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
**Certificate grind relaunched at Q = (x₄+=x₀, x₆+=x₁)** — rank-2,
sources {x₀,x₁}, targets (r1,c1),(r2,c0), 11 monomials (C-sized,
~61 min/run), SAT-live, point symmetry ρ = (0 1), 8 orbits with weights
{00:4, 01:8, 02:4, 03:8, 04:4, 05:4, 07:2, 09:2}, duplicates 14 = pre(00),
06 = swap(01), 34 = post(02).
    TOTAL_Q = 4·V00 + 8·V01 + 4·V02 + 8·V03 + 4·V04 + 4·V05 + 2·V07 + 2·V09
Gates: three duplicate matches + (states 1 or exact-zero (0,0)) per run.
Assembly: scripts/assembleQ.py (computes orbits itself, no hardcoding).
Launched 16:45Z 2026-08-25; ~23:30Z ETA with negD + phi tails. Tail add-ons: f1D_00 engine zero (resumes
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
