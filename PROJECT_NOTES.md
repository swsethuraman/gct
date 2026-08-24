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

**⚠ IMMEDIATE OPEN ITEM — interpretation.** The conductor paper (§5) states:
predicted c((2,2,2), 2) = 2, i.e. k=1 closure multiplicity 0, "falsifiable by
the banked 36-subproblem computation." That computation now says the pairing
value is NONZERO (1,152,144,000). Before claiming c((2,2,2),2) = 1 (predicted
falsified: a k=1 copy exists on the closure) or the opposite, re-derive the
precise contract of the f1C pairing from the week-3 session-10 setup: what
does nonzero mean for mult_{(2,2,2)} C[Ω̄] at k = 1 — matrix element of which
map, at which point, with which normalization. Pin this FIRST next session;
it decides whether §5's prediction stands or falls, and both outcomes are
publishable content (P₂'s formula-dependence biting would be the interesting
case).

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
   patterns (`f1C_0[3]`).
5. Shell cwd can reset mid-command in this environment: use absolute paths.

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

R1. **Pin the f1C interpretation** (see open item above) → conclude
    c((2,2,2),2) ∈ {1,2}; propagate through conductor §5 and the log.
R2. **Run/interpret the banked h-series** (h1A–D, h2A–D, h3A in evalin/):
    the next evaluations of the same factored-HWV machinery; enumerate their
    contracts from wk3_s8_gen*.py, budget ~45 min each on the grind engine.
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
