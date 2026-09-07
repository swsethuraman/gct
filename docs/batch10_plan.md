# Batch 10 — the twelve, final

Base commit for every brief in this batch: **`226b4ef1`**.

**Supersedes** three documents, and consolidates all of them: the integrator's
first `docs/batch10_plan.md` (commit `a3d2949`), Sol's `next_12_session_roadmap`
and its revision, and `sol_insights` and its revision.  Where they disagreed,
the disagreements were settled by computation and the settlements are in §1
and §5.  Read `docs/stocktake_batch9.md` §6 for what batch 9 left behind.

---

## 0. The phase change

At `(per_3, det_4)` the programme no longer has a separator-discovery problem.
Two independent geometric routes already separate `x_0·per_3` from the `det_4`
orbit closure: the LMR degree-24 dual-defect construction, and the conormal
slot-6 violation `δ_6(x_0·per_3) = 30 > 20 = δ_6(det_4)`.  The open question is
narrower and sharper:

> **Can the multiplicity statistic see a separation that geometry already knows
> is there?**

That is `D(λ,δ) = mult_pad − mult_det = i_det − i_pad > 0` at some cell, and the
LMR cell `λ = (65,17,2⁷)`, `δ = 24` is the canonical place to ask, because it is
the one cell where a determinant equation is known to exist and the ambient
multiplicity is small: `a_24 = 274`, `a_23 = 273`, `sk_24 = 48 825`.  The
determinant side is therefore not an astronomical multiplicity problem.  It is a
finite rank problem, `C²⁷⁴ → C⁴⁸ ⁸²⁵`.

Batch 9's lesson, stated once: **search for the mechanism of rank loss, not for
a rare ambient shape.**  Every scalar selector read off ambient plethysm data
has now died.

---

## 1. Pre-batch checks — both closed before the batch starts

### P0 — birth-sequence morphology.  **Done.  Retire it.**

Run here on all 2 107 live length-5 tails (`tailcensus5.json`), not the 1 075
of `results/s60_tail_census.json`:

| observable | full census | s60 subset |
|---|---|---|
| room-one (final birth = 1) | **885 / 2 107 = 42.0 %** | 481 / 1 075 = 44.7 % |
| birth sequence unimodal | **2 107 / 2 107 = 100.0 %** | 1 075 / 1 075 |
| birth sequence log-concave | **2 000 / 2 107 = 94.9 %** | 1 024 / 1 075 = 95.3 % |
| … log-concave given room-one | 789 / 885 = 89.2 % | 433 / 481 = 90.0 % |

LMR's births are `2, 37, 54, 52, 43, 31, 22, 14, 9, 5, 3, 1, 1` — unimodal like
every other tail, and non-log-concave by three marginal misses
(`14² = 196 < 198`, `5² = 25 < 27`, `1² = 1 < 3`), which puts it in a 5.1 %
class of 107 tails.

**`ε_final = 1/a_∞` is worse than useless: it points the wrong way.**  LMR's
`1/274 = 0.00365` ranks **632 of 885** room-one tails, against a median of
`0.00052`.  So the typical room-one tail has `a_∞ ≈ 1 900` and LMR's 274 is on
the *small* side — and small `a_∞` is already a dead selector (s60: 99 closed
tails, `a_∞` 1…56, all full rank).  `ε` is dead twice over.

**Decision: birth morphology is retired.**  E6, if ever activated, compares
determinant-specific invariants of the last-born line, never ambient sequence
shape.

### P1 — C1 sizing.  What s56 gives, and what it does not.

The s56 engine avoids highest-weight vectors, so it does not record the support
sizes C1 needs.  What it does give:

    tensor-row support 24^δ          δ=3 → 13 824 ;  δ=4 → 331 776
    δ=4 weight route                 64 passes, Σ n_b = 5 709, max n_b = 465
    example δ=3 Gram sizes           8, 15, 23
    example δ=4 certified block      51 × 51 at (8,4,4)
    full δ=4 old-engine runtime      ≈ 2.1 h

So C1 is not obviously walled at small degree.  But **C1 must measure the new
last-born and source-vector supports itself** before anything is extrapolated
to `δ = 23, 24`.  That measurement is task 1 of C1 and it gates the rest of the
Gram route.

---

## 2. The twelve

| wave | # | owner | session | gate |
|---|---|---|---|---|
| 1 | **C1** | Claude | Gram/`Θ⁺` positive control and support sizing | — |
| 1 | **C6** | Claude | certification, degeneration certifier, verifier fix, int64 widening | — |
| 1 | **S1** | Sol | Proposition S computational: the stable ideal of `M_ℓ` | — |
| 1 | **S2** | Sol | the noncommutative orbital commutant and the last-born scalar | — |
| 1 | **S3** | Sol | the exact padded multiplicity-space map — **critical path** | — |
| 2 | **C2** | Claude | the LMR determinant multiplicity | C1 |
| 2 | **C3** | Claude | padded map implementation and calibration | S3 |
| 2 | **S4** | Sol | the `r = 5` primitive/compression theorem route | — |
| 2 | **S6** | Sol | the LMR isotypic and Adams independent audit | — |
| 3 | **C4** | Claude | the LMR padded rank **and orientation** | C2 + C3 |
| 3 | **C5** | Claude | the `r = 5` special normal cone, at the primitive family | S4 |
| 3 | **S5** | Sol | the `n = 5` polar check, then replication and reach | — |

Six each.  Seven of the twelve are ungated.

**One change from Sol's revision, with a reason: C6 moves from wave 3 to wave 1.**
It is ungated infrastructure, and its Part A defines the certificate kind that
C2's LMR claims will need.  Landing it after those claims are produced means
back-filling certificates for the batch's most load-bearing result.

**And the scheduling correction stands: S3 launches in wave 1.**  `S3 → C3 → C4`
is the longest chain in the batch, `C4` additionally waits on `C2`, and S3's
head is ungated.  Nothing about it belongs in a later phase.

---

## 3. Dependency graph

    C1 ──> C2 ─┐
               ├──> C4          (the batch's resolving session)
    S3 ──> C3 ─┘

    S4 ──> C5

    C6   S1   S2   S5   S6      (ungated throughout)

`S2` feeds `C1`/`C2` opportunistically — if it produces a block-local formula
for the last-born scalar, `C2` uses it; if not, `C2` proceeds on `C1`'s direct
implementation.  It is a force multiplier, not a gate.

---

## 4. The sessions

### C1 — Gram/`Θ⁺` positive control and support sizing  ·  Claude  ·  wave 1

**Question.** Can a room-one determinant birth be detected by the exact
Schur-complement scalar, starting from the `n = 3` LMR positive control?

**The mechanism.**  At a room-one closing cell whose predecessor is full rank,
`M_δ = u·M_{δ−1} ⊕ ⟨v_ρ⟩` and, writing `G = Θ*Θ` in that splitting,

        ⎡ A  b ⎤
    G = ⎢      ⎥ ,    det G = det A · s ,    s = c − bᵀA⁻¹b ,
        ⎣ bᵀ c ⎦

with `A` nonsingular exactly because the predecessor is full rank.  Then

> **a new determinant kernel is born ⟺ `s = 0`.**

**Tasks.**
1. Measure the source / HWV / last-born support sizes at `δ = 2, 3, 4` in the
   new implementation.  This is the number that decides whether the route
   reaches LMR; measure it before promising anything.
2. Build the exact rational `G = Θ*Θ` on tiny controls.
3. Reproduce every `δ = 2` and `δ = 3` full-rank calibration.
4. **Reproduce the `n = 3` LMR rank drop as an exact `6 × 6` Schur complement,
   `s = 0`.**  `((19,7,2⁵), 12)`, `a = 6`, `sk = 10`, `i_det ≥ 1` by theorem, and
   its `a`-sequence `0,2,4,5,6,6` makes it room-one — so the mechanism above
   applies verbatim.  This is the first rank drop any engine in this programme
   would ever be shown.
5. Record exactly which pair-orbital / block-intersection data suffices to
   compute a Gram entry.
6. Smith normal forms and determinantal divisors as cheap diagnostics only —
   not a congruence programme (see §5).

**Success.**  `s = 0` at the `n = 3` cell; `s ≠ 0` at every known negative
control; a measured cost curve rather than an estimated one.

**Stopping rule and pivot.**  Any mismatch with a banked rank stops the implementation, not
the theorem.  If Gram-entry construction explodes by `δ = 4`, keep the Schur
complement result and switch C2 to a direct `λ`-block `Θ⁺` implementation.

**Field caveat, binding.**  `rank(Θ*Θ) = rank Θ` is **not** a safe finite-field
identity.  The Gram route is exact-characteristic-zero.  Ordinary mod-`p` full
rank of the *original* map remains a valid characteristic-zero lower bound and
is unaffected.

### C6 — certification, degeneration, verifier, widening  ·  Claude  ·  wave 1

**Part A — certificates.**  Add a `gct-cert/1` kind for the sparse/Wiedemann
full-rank route (seeds, levels, pinned evaluation rows, checked kernel
candidates) and back-fill s60's **264 uncertified cells** — the largest body of
unwitnessed claims in the programme.  Ensure every new `Θ⁺`/Gram/padded output
is machine-reproducible.  **Separate finite-field full-rank certificates from
characteristic-zero kernel certificates in the format itself**, so the C1 caveat
cannot be lost downstream.  Fix the `tools/verify/verify.py` defect s56 flagged:
large `nonvanishing_minor` determinants fail the `content` line on Python's
integer-to-string limit after the rank checks pass — one
`sys.set_int_max_str_digits` call.

**Part B — degeneration as a full-rank certifier, one direction only.**
`rank(in Θ) ≤ rank Θ`, so full rank of the initial map certifies full rank of
the original.  Test it on known negative blocks.  **A rank drop in the
degeneration is never evidence of an obstruction** — the inequality runs the
wrong way, and this is the whole reason the Rogers–Ramanujan framing was
dropped.

**Part C.**  Widen the int64 monomial encoding of the s45 build, which is what
confines tail closure to `δ_close ≤ 18` and blocks 183 of 1 075 closing cells.

### S1 — Proposition S computational: the stable ideal of `M_ℓ`  ·  Sol  ·  wave 1

**Question.** Can the stable determinant ideal be reached directly through
`M_ℓ`, the variety of characteristic polynomials of traceless `(ℓ−1)`-pencils of
`4×4` matrices, producing the first nonzero stable `i_det` independently of any
`Θ` implementation?

**Tasks.** Re-derive the stable `M_ℓ` model in implementation-ready form.
Identify the smallest tail weights where `I(M_ℓ)` could first carry a
highest-weight vector, **respecting the banked closure `m_0(6) ≥ 13`**
(`docs/s57_report.md`).  Produce **one** exact finite test for the first
plausible stable ideal copy.  Separate theorem from computational conjecture
throughout.

**Calibration.**  The peaked family gives a free calibration set with a known
answer: `λ = (4δ − 2(ℓ−1), 2^{ℓ−1})` has `t = 2(ℓ−1)`, so `δ ≥ 2(ℓ−1)` puts it
in the proved stable range `λ_1 ≥ 3δ`, and s57's Theorem P gives `a_∞ = 1` with
the bordered discriminant as unique highest-weight vector, nonzero at a generic
pencil — hence `i_det,∞ = 0`.  The engine must return 0 at every member.  Note
no length-5 closing cell is in the stable range (s60: 0 of 2 107), so the census
cannot supply one.

**Success.**  An explicit nonzero stable determinant ideal copy, **or** a theorem
pushing the stable dead region further out.

**Stopping rule.**  If the first tractable range is provably beyond exact access, report
the obstruction.  Do not turn this into a broad census.

### S2 — the noncommutative orbital commutant and the last-born scalar  ·  Sol  ·  wave 1

**Measured input, not hypothesis.**  `Sym^δ(Sym⁴)` is **not** multiplicity-free:

    δ = 2 :  3 constituents, max multiplicity 1, Σ a² =  3
    δ = 3 :  9 constituents, max multiplicity 1, Σ a² =  9
    δ = 4 : 28 constituents, max multiplicity 2, Σ a² = 43
            multiplicity 2 at (12,4), (10,6), (10,4,2), (8,6,2), (8,4,4)

so the `δ = 4` commutant is `23·(1×1) ⊕ 5·(2×2)`, dimension 43, and it is
**noncommutative**.  Those `Σ a²` values equal the orbital counts computed
independently (3, 9, 43 pair-orbitals over `|H_{4,δ}| = 35`, `5 775`,
`2 627 625`), so the identity `Σ_λ a_λ² = #orbitals` validates both
computations.  Sol's falsifier fired at the first `δ` where it could.

**Tasks.**  Formalise the orbital invariance of `G` — `G_{P,Q} = ⟨ε_P,ε_Q⟩²` is
`S_{4δ}`-invariant, hence a function of the block-intersection type alone.  Use
coherent-configuration / centralizer language, **not** global Bose–Mesner
commutativity.  Derive the room-one Schur complement in `λ`-block coordinates.
Determine whether `s_ρ` can be evaluated without constructing the full target.
Identify any block-local character-sum or product structure.

**What survives and what died.**  Surviving: orbital constancy of the entries;
coherent-configuration compression (which needs no commutativity, so closure
under the Hadamard product still holds and the *squaring* — the step that makes
this the determinant problem rather than the Foulkes problem — is free); the
`a_λ × a_λ` block; and, decisively, **the room-one Schur complement is a scalar
whether or not the commutant is commutative.**  Dead: a global diagonalisation
or product formula resting on commutativity.

**Stopping rule.**  If symmetry gives no reduction beyond the already-small `a × a` block,
keep the Schur-complement result and park the spectral programme.

### S3 — the exact padded multiplicity-space map  ·  Sol  ·  wave 1, critical path

**Question.**  What is the correct finite polarised map for `f = ℓ·per_3(A)` on
**the same source multiplicity space** `M_λ` the determinant side uses?

**Why this is the batch's most important derivation.**  `Θ⁺` exists for the
determinant.  For the padded permanent there is nothing — no finite equivariant
model, no target module, no evaluator.  `D = i_det − i_pad` cannot be measured
at LMR or anywhere else until this exists, and C3 and C4 cannot be briefed
without it.

**Tasks.**  Derive the degree-`δ` coordinate pullback.  Polarise it into an
`S_{4δ}`-equivariant finite model if one exists.  Identify the target module, or
a rigorously equivalent source-basis evaluation scheme.  State exactly how
`mult_pad` is computed as a rank.  **Preserve common source coordinates with the
determinant side**, so that C4 can compare kernels and not merely dimensions.
Specify the tiny and `r = 5` calibration cases.

**Stopping rule — and it is a soft one.**  If no compact target decomposition exists, do
not abandon the route: reduce to source-basis evaluation.  `a_LMR = 274` is
small enough that a generic-evaluation rank test is viable.

### C2 — the LMR determinant multiplicity  ·  Claude  ·  wave 2  ·  gate: C1

**Goals, in cost order.**

    A.  predecessor  (61,17,2⁷), δ = 23, source 273
    B.  goal cell    (65,17,2⁷), δ = 24, source 274

**Either of two results settles it.**  `rank_23 = 273` forces `i_det,24 = 1` by
ladder monotonicity and the known degree-24 equation.  Or, directly at `δ = 24`,
`rank_24 ≥ 273` suffices — the known equation already gives `rank_24 ≤ 273`, so
the two together pin `rank_24 = 273` and `i_det = 1`.

**Do not insist on materialising all 48 825 target rows.**  The rank is at most
274.

**Read S6 before relying on the `δ = 23` target dimension.**  Manivel's
reduction is unavailable there (`2δ = 46 < 48 = |ρ| + ρ_1`), so at `δ = 23` the
target dimension rests on s58's reduction alone.

**Inconclusive.**  Preserve the partial compressed operators and move direct
degree-24 completion to reserve E1.  Do not burn the batch on it.

### C3 — padded map implementation and calibration  ·  Claude  ·  wave 2  ·  gate: S3

Implement S3's `T_pad` or common-source evaluator.  Calibrate at low degree.
Calibrate on the `r = 5` cells where `P_5 = R_5` and s60 supplies exact
multiplicities.  Verify rank agreement across at least two independent
constructions or seeds.  Preserve explicit kernel coordinates in `M_λ` — C4
needs them.

**Stopping rule.**  Any unexplained mismatch with a banked pad or reducible multiplicity
stops LMR use immediately.  A padded engine that disagrees anywhere is not
usable at the one cell that matters.

### C4 — the LMR padded rank and orientation  ·  Claude  ·  wave 3  ·  gates: C2 + C3

**This is the session the batch exists for.**  In the same `M_λ ≅ C²⁷⁴`, compute
`U_D = ker T_det`, `U_P = ker T_pad`, `i_pad`, `dim(U_D ∩ U_P)`, and whether the
known LMR determinant kernel line lies in `U_P`.

| outcome | reading |
|---|---|
| `i_pad = 0` | `D = +1` — **the first multiplicity obstruction in the programme** |
| `i_pad = 1` | `D = 0`; then test orientation, and `U_D ≠ U_P` is a clean demonstration that multiplicity loses orientation where geometry does not |
| `i_pad ≥ 2` | `D < 0` — the multiplicity statistic points the wrong way despite a known geometric separator |

**Success is any one of the three, exactly established.**  Do not define success
as `D > 0`.  All three resolve the LMR cell and all three are publishable; the
second and third are results about the *limits* of the multiplicity statistic,
which is what a GCT programme is ultimately obliged to report.

### S4 — the `r = 5` primitive/compression theorem route  ·  Sol  ·  wave 2

**Corrected input — this is the correction that matters most in the batch.**
There is **no four-dimensional transverse quotient**:

| point | `dim ker dΦ` | tangent span | transverse quotient |
|---|---|---|---|
| `C_21 ∩ C_32` | 64 | 57 + 57 → 64 | **0** |
| `C_21` alone | 57 | 57 | **0** |
| `ker ∩ coker` | 75 | 75 | **0** |

The erroneous 60 came from counting fixed-flag tangents (5 × 10 = 50 each); the
flag motion in `Gr(2,4) × Gr(1,4)` supplies the missing 7 per component.  Every
spanning vector was verified to annihilate `dΦ`
(`docs/rees_boundary_audit.md`).

**Tasks.**  Formulate the primitive family and its compression incidences — the
genuine analogue of the `n = 3` skew-symmetric component that Hüttenhain–Lairez
show compression analysis provably misses, and the only base-locus type at
`r = 5` where nobody has looked.  Identify the finite normal-cone or
special-fibre algebra that could raise the fixed-factor image.  Seek either a
universal degeneration proving `R_5 ⊆ D_5`, or an upper bound excluding 35.
Hand C5 a finite CAS goal, not a request for more Rees order.

**Why it earns a slot.**  `R_5 ⊆ D_5 ⟺ dim(D_5 ∩ W) = 35`, and `≥ 31` is
certified over `Q`.  **An upper bound below 35 is a theorem, not a
measurement** — the only such route the programme has.

**A caution the audit earns.**  "The tangent cone spans" does not close the
loophole: a normal cone can carry components no tangent space sees.  The quadric
system and its minimal primes remain legitimate.  What is *not* available is a
coordinate reduction eliminating a transverse complement, because there is none.

### S6 — the LMR isotypic and Adams independent audit  ·  Sol  ·  wave 2

**Question.**  Can every representation-theoretic step between "the LMR family
separates" and "the `(65,17,2⁷)` multiplicity block carries a determinant
kernel" be independently certified?

**Tasks.**  Verify the exact lowest LMR irreducible and its multiplicity.
Reconcile the LMR module with the common 274-dimensional source.  **Independently
recheck the Adams/transposition contribution behind `sk = 48 825`** — `sk =
(g + T)/2` with `g = 92 000` confirmed by three routes, while `T = A = 5 650` is
single-source (s58's reduction plus the external Manivel route), validated at
thirteen smaller cells but not at the goal cell, where the direct partition sum
is out of reach at `p(96) = 1.18 × 10⁸`.  C2 and C4 both rest on it.  If C2
produces a kernel vector, identify it representation-theoretically.  Look for a
formula generalising the `n = 3 → n = 4` pattern, without assuming commutativity.

**Success.**  Remove the last "standard identification" caveat from the LMR
multiplicity statement, and provide an independent audit of C2.  A disagreement
here invalidates Track II before it is run, which is precisely why it is funded
even though agreement produces no new mathematics.

### C5 — the `r = 5` special normal cone, at the primitive family  ·  Claude  ·  wave 3  ·  gate: S4

**Explicitly not the obsolete 60 + 4 transverse calculation.**  See S4.

Instantiate S4's nominated primitive/compression algebra.  Compute radicals,
minimal primes and special-fibre components as appropriate.  Measure reducible
image dimensions against the certified 31 and the target 35.  If the nominated
locus is exhausted, move to S4's next-ranked incidence.  **No generic `q > 4`
sweep** — s59 showed `29,29,28,28,24` invariant in `q` at `q = 2,3,4` — and no
broad brute-force Rees algebra.

**Success.**  A dangerous hidden component found, or this special-normal-cone
loophole rigorously closed.

### S5 — the `n = 5` polar check, then replication and reach  ·  Sol  ·  wave 3

**Opening bounded check — one integer.**  s61 proved
`P ∈ closure(GL_16·det_4) ⟹ δ_k(P) ≤ δ_k(det_4)` and measured

    det_4        4, 12, 36, 68, 84, 60, 20,  0
    x_0·per_3    4,  6, 12, 24, 48, 48, 30,  6, 0

with violations at slots 6 (`30 > 20`) and 7 (`6 > 0`).  The padded profile is
*frozen* under further padding — padding moves slot 0 to the new degree, leaves
slots 1–7 at `per_3`'s values, and appends zeros — while `det_n`'s dual is the
Segre `P^{n−1} × P^{n−1}`, of dimension `2n − 2` and degree `C(2n−2, n−1)`.
That reproduces `det_4`'s tail exactly (`δ_7 = 0`, `δ_6 = C(6,3) = 20`), and at
`n = 5` predicts `δ_8(det_5) = C(8,4) = 70` with `δ_k = 0` for `k ≥ 9`.  So the
padded support (slots 0–7) sits strictly **inside** `det_5`'s support (0–8), the
slot-7 violation that worked at `n = 4` is gone, and what remains is:

> **is `δ_6(det_5) < 30`?**  A lower bound of 30 closes the branch; no exact
> value is needed to retire it.

If yes, audit immediately whether the padded 30 improves the geometric border
bound past LMR's `dc̄(per_3) ≥ 5`.  If no, bank the negative and continue into
the main task without consuming the session.

**Provenance warning.**  The paragraph above is the integrator's derivation from
the dual-variety identification, checked only against `det_4`'s measured
profile.  s61 computed nothing at `n = 5`.  Re-derive before relying on it, and
settle which conormal cycle the specialisation inequality applies to, since
`x_0²·per_3` is non-reduced.

**Main task — replication and asymptotic reach.**  The programme already has one
replication operator: `u = e_1⁴` transports kernels up the ladder, moving `δ`
while fixing `ℓ` and `n`.  The Valiant-relevant demand is different: the padded
side imposes `ℓ(λ) ≤ m² + 1`, while `n` must eventually exceed every polynomial
in `m`.  LMR's own family fails this — `ℓ(λ(k,n)) = k + 3` and the census forces
`k ≥ min(6, r−2)`, so rows grow with `n`.

Audit Adams operations, plethysm, wreath induction and restriction, induction
products, and any natural intertwiner of `Θ`.  For each, compute how `m`, `n`,
`δ` and `ℓ(λ)` transform.  **Keep only operators that provably transport kernel
information.**  Rank the survivors by `n`-growth against row-growth.

**Stopping rule.**  Purely formal scaling of `λ` and `δ` at fixed `n` does not count.

---

## 5. Corrections carried into this batch — do not let these reappear

1. **"Four transverse directions at `C_21 ∩ C_32`."**  It is zero.  Measured
   three ways (§4, S4).  It has now surfaced in three separate documents after
   being corrected once; every `r = 5` brief must be searched for it.
2. **"The orbital algebra is a commutative association scheme."**  False from
   `δ = 4` on (§4, S2).  Multiplicity-freeness holds only at `δ ≤ 3`.
3. **Birth morphology as a selector.**  Retired by P0.  Unimodality is
   2 107/2 107; `ε` puts LMR at rank 632 of 885 and on the wrong side.
4. **The `n = 5` polar demotion attributed to s61.**  s61 computed nothing at
   `n = 5`; the support argument is from this batch's planning discussion and is
   unchecked (§4, S5).
5. **Old base-commit hashes.**  `0960bd5` and its generation resolve only in the
   private `gct-archive` now.  Every `PREREG` in this batch names `226b4ef1`.

---

## 6. Reserves

**E1 — direct degree-24 completion.**  Trigger: C2's predecessor inconclusive.
`rank_24 ≥ 273` is enough.

**E2 — the length-5 closure walk.**  Trigger: spare compute, or a
determinant-specific selector nominating tails.  Background falsification now,
not the intellectual programme: 99 tails closed, no determinant kernel.  The
int64 widening it needs is already C6 Part C.

**E3 — retired.**  Birth morphology; done as P0.

**E4 — the stable-range `D` search.**  Trigger: S1 finds a nonzero stable
`i_det`.  Search over tails with cost driven by `ℓ` and `|λ̄|`, independent of
`δ` and `N`.

**E5 — the `K(q)` series ladder.**  Trigger: *multiple* nonzero stable
determinant kernels.  Escalation discipline, in order:
rational → `q`-holonomic → `η`-quotient → theta/false theta → mock modular.
**Do not fit a modular form to zero data.**

**E6 — the room-one mechanism ensemble.**  Trigger: C1 and S2 make the last-born
scalar cheap.  885 naturally normalised one-dimensional probes of `Θ⁺`, with the
`n = 3` LMR line as the one known dier.  Compare determinant-specific invariants
of `v_ρ` — tableau coordinates, `Θ*Θ` block position, Jucys–Murphy content,
leading standard monomial — never ambient shape statistics, which P0 retired.

**E8 — a second determinant-equation mechanism.**  Trigger: LMR turns out
multiplicity-invisible or asymptotically non-scalable.  Must nominate an
explicit `(λ, δ)` with a rank-loss mechanism.  No broad survey.

**E9 — the slot-6 toy saturation experiment.**  Quantify saturation degree
inflation in a small model.  s61's own numbers are the better starting point
than a fresh toy: the `P⁴`-section's 20 nodes correct `4·27 = 108` to 68, and
the `P⁵`-section's degree-20 curve of `A_1` points corrects `4·81 = 324` to 84 —
37 % and 74 % inflation at the exact object of interest.

**E10 — external critic, round 4.**  Trigger: after C2/C4, or a theorem-level
`r = 5` result.  Audit the new load-bearing conclusion, not the whole project.

---

## 7. Batch success criteria

The batch succeeds if **any** of the following happens:

1. `D_LMR > 0` is proved.
2. `D_LMR = 0` but `U_D ≠ U_P` is proved.
3. `D_LMR < 0` is proved exactly.
4. A determinant-specific last-born scalar algorithm or formula is derived.
5. A nonzero stable determinant ideal copy is found through `M_ℓ`.
6. The `r = 5` containment question is settled, or a major primitive loophole is
   closed.
7. The `n = 5` polar check improves the geometric lower bound.
8. A credible row-efficient replication operator is found.

**The batch is not judged by cells measured.**  The metric is how many
load-bearing unknowns were converted into exact finite statements, theorems, or
clean negatives.

---

## 8. House rules for this batch

1. Distinguish mechanism score from information score.
2. Do not fund a scalar selector that a one-command census can retire.
3. Positive rank-drop claims require characteristic zero, or a rigorous lifting.
4. Mod-`p` full rank of the original map is a safe characteristic-zero lower
   bound; a mod-`p` Gram kernel is not a characteristic-zero kernel.
5. Treat any commutant as noncommutative unless multiplicity-freeness is proved.
6. The `n = 3` LMR cell is the mandatory first positive rank-drop calibration.
7. Build determinant and padded maps in common source coordinates.
8. At LMR, `rank ≥ 273` at `δ = 24` is enough.
9. Length-5 closure walking is background falsification.
10. Every asymptotic idea states its row-budget economics explicitly.
11. Ambient morphology is retired; ensembles compare determinant-specific
    invariants.
12. Every `r = 5` brief is searched for the stale transverse-direction claim
    before it goes out.
13. **Provenance.**  Attribute a result to the session that produced it.  A
    derivation made in planning discussion is unchecked until a session checks
    it, and is labelled as such — three of this batch's planning corrections
    were to claims that had drifted from their source.

---

## 9. Standing conditions

- Base commit `226b4ef1`; every `PREREG` names it.
- Pre-registration before any computation.  Bank per cell.
- `python-flint` for exact linear algebra; both house primes `2147483647` and
  `2147483629`.  Where a route is characteristic-zero by nature (C1, C4), say so
  in the pre-registration and certify accordingly.
- Any `D > 0` cell goes through the verification protocol before it is reported
  anywhere, including in conversation.
- `docs/brief_wording.md` §2 and §4 are binding; §5's degeneracy-direction
  pre-check — evaluate at a `det_4` pencil, at a reducible `ℓ·c`, and at the full
  ten-variable `ℓ·per_3` — applies to any new statistic S5 proposes.
- Bound every long run at launch with `timeout` and `ulimit -v`; write the run's
  process id to `results/logs/<run>.pid`; end a run only by that recorded id.
- Single-writer files are not touched by workers: `paper/det3-conductor.tex`,
  `paper/det4-onset.tex`, `PROJECT_NOTES.md`, `docs/boundary_deficit.html`.
- Delivery by bundle.  No file over 5 MB.  Logs under `results/logs/`.
- Commit messages carry `Co-Authored-By` only.  No session-link trailer, in
  commits or in any script that writes commits, and no such URL in any file.
