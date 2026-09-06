# Batch 10 — the next twelve sessions, with two reserves

Written at the batch boundary, after the history rewrite and the repository
split.  Base commit for every brief in this batch: **`226b4ef1`**.

Read `docs/stocktake_batch9.md` first, including its §6 correction.  This
document does not repeat it; it says what to do next and why, and it differs
from the stock-take's §4 in four places, each marked **[change]**.

---

## 0. The one sentence

Batch 9 produced twelve clean negatives and excellent instrumentation, and left
the programme with **no computable rank at any cell where a rank drop could
live**.  Everything below is organised around that single fact: two independent
attacks on it, four sessions that only run if one of them succeeds, four that
are worth running whatever happens, and two that ask — adversarially — whether
the programme's instruments can reach past the bound Landsberg–Manivel–Ressayre
already published.

---

## 1. The gate, attacked twice **[change]**

The stock-take made the gate a single session and everything else wait on it.
That is the wrong shape.  The gate is one obstacle with two unrelated ways
round, the two share no code, no method and no failure mode, and each is a
legitimate session on its own terms.  **Run them in parallel.**

| | route | owner | cost driver if it works |
|---|---|---|---|
| **C1** | tail-reduce the `Θ⁺` **rank**, as s58 tail-reduced the target dimension | Claude | `\|λ̄\|`, not `\|H_{4,δ}\|` |
| **S1** | compute stable `i_det` as an ideal multiplicity of `M_ℓ`, per Proposition S | Sol | `ℓ`, not `δ` or `N` |

C1 keeps the Foulkes formulation and tries to make it cheap.  S1 abandons rank
computation entirely and asks a commutative-algebra question about one small
explicit affine variety instead.  If either lands, Track II opens.  If neither
does, §5 says what the batch becomes.

---

## 2. The twelve

| # | owner | session | gated on | wave |
|---|---|---|---|---|
| **C1** | Claude | the tail reduction of the `Θ⁺` rank | — | 1 |
| **C5** | Claude | the length-5 closure walk, and the int64 widening | — | 1 |
| **S1** | Sol | Proposition S made computational: the ideal of `M_ℓ` | — | 1 |
| **S3** | Sol | the polar reach at `n = 5` — two integers | — | 1 |
| **C6** | Claude | the certificate gap: `gct-cert/1`, and the verifier defect | — | 2 |
| **C2** | Claude | the LMR predecessor, `δ = 23` | C1 **or** S1 | 2 |
| **S2** | Sol | the `r = 5` special fibre at the primitive family | — | 2 |
| **S6** | Sol | the Adams part at the LMR cell, independently | — | 2 |
| **C3** | Claude | the LMR cell itself | C2 inconclusive | 3 |
| **C4** | Claude | the padded side at the LMR cell | C2 **or** C3 | 3 |
| **S4** | Sol | the stable-range `D` search | S1 | 3 |
| **S5** | Sol | the `dc̄` reach audit | S3 | 3 |

Six each.  Waves are guidance, not a schedule: anything ungated may start at any
time.

---

## 3. The sessions

### C1 — the tail reduction of the `Θ⁺` rank

**Goal.**  s56 established `mult_det(λ,δ) = rank Hom_{S_N}([λ], Θ⁺_δ)` with
`Θ⁺_δ(π) = ε_π ⊗ ε_π`, calibrated 40/40 at `δ = 2, 3, 4`, and measured the wall:
the engine is quadratic in `|H_{4,δ}|`, and `|H_{4,5}| = 2 546 168 625`.  s58
showed the *target dimension* `sk(λ, 4×δ)` reduces — Jacobi–Trudi along `λ`'s own
first row, then Frobenius reciprocity on the rectangle — to class sums over
`S_{|λ̄|}`, with `N` absent from the cost, taking the LMR cell from
`p(96) = 1.18×10⁸` to 0.2 s.

The session is the obvious question and nobody has asked it: **does the Gram
kernel `K(π,π')` and its Hadamard square push through the same reduction?**

**Deliverable, either way.**  A rank algorithm whose cost is driven by `|λ̄|`,
calibrated against s56's forty cells and then against the `n = 3` LMR positive
control; *or* a written statement of the precise obstruction — which class
function fails to descend, and why — with the failure exhibited on the smallest
cell where it bites.

**Calibration, in this order and not negotiable.**  (i) s56's forty cells at
`δ = 2, 3, 4`.  (ii) The `n = 3` LMR cell `((19,7,2⁵), 12)`, `a = 6`,
`sk = 10`: **this must return rank ≤ 5.**  Every cell the programme has ever
measured is full rank; this is the first rank drop any engine would be shown,
and it costs a `6 × 10` matrix.  If it returns 6, the session stops and reports
that, and Track II does not open on this route.

**Stopping rule.**  If the descent is shown impossible before the halfway mark,
write the negative and stop.  A characterised failure is a full deliverable
here — it is what tells S1 it is carrying the batch.

### S1 — Proposition S made computational: the ideal of `M_ℓ`

**Goal.**  s57's Proposition S gives

    a_∞(λ̄)  =  [S_λ̄]  Sym(Sym² ⊕ Sym³ ⊕ Sym⁴)(C^{ℓ−1}),

reproduced here at 155 of 155 length-5 tails of weight `t ≤ 16`, and its
companion: **stable `i_det` is the multiplicity of `S_λ̄` in the ideal of `M_ℓ`**,
the variety of characteristic polynomials of traceless `(ℓ−1)`-pencils of `4×4`
matrices.  That converts "a rank drop somewhere up this ladder" into "an
equation of one explicit affine variety", and `M_ℓ` is small.  Singular, msolve
and Macaulay2 are all available now; s61 established the discipline for using
them.

**Deliverable.**  `M_ℓ` built explicitly for `ℓ = 3, 4, 5` and as far beyond as
the CAS reaches; its ideal computed and decomposed into `S_λ̄`-isotypics; a
stable-range `i_det` engine, or a characterised obstruction to one.

**Calibration.**  Use the peaked family.  For `λ = (4δ − 2(ℓ−1), 2^{ℓ−1})` the
tail has `t = 2(ℓ−1)`, so `δ ≥ 2(ℓ−1)` puts the cell **in the proved stable
range** (`λ₁ ≥ 3δ`), and s57's Theorem P gives `a_∞ = 1` with the unique
highest-weight vector the bordered discriminant
`c·det G₂ − (3/8) g₁ᵀ adj(G₂) g₁`, nonzero at a generic pencil — so
`i_det,∞ = 0`.  **The engine must return 0 at every member.**  This is a
genuine calibration set with a known answer and it is free; note that no length-5
*closing* cell is in the stable range (s60: 0 of 2 107), so the census cannot
supply one.

**The question that matters most, and it is second.**  Does the padded side
admit the same description?  `D = i_det − i_pad`, and an engine for `i_det`
alone produces no obstruction.  The ladder theorem was proved for `C[D_r]` and
`C[R_r]`; whether `u = e₁⁴` gives the same statement for the padded permanent,
and whether the padded analogue of `M_ℓ` exists and is computable, is the whole
value of the route.  Answer it even if the answer is no.

### S3 — the polar reach at `n = 5`: two integers **[change, new]**

**Goal.**  s61 proved the specialisation inequality
`P ∈ closure(GL₁₆·det₄) ⟹ δ_k(P) ≤ δ_k(det₄)` and measured

    det₄        4, 12, 36, 68, 84, 60, 20,  0
    per₃        3,  6, 12, 24, 48, 48, 30,  6
    x₀·per₃     4,  6, 12, 24, 48, 48, 30,  6, 0     (16 variables)

with the violation at slot 6 (`30 > 20`) and again at slot 7 (`6 > 0`).  That
certifies `x₀·per₃ ∉ closure(GL₁₆·det₄)`, hence `dc̄(per₃) ≥ 5` — exactly LMR's
bound, by an independent method.  **Nobody has asked what the same method gives
at `n = 5`,** and it is nearly free to ask, because the padded profile is
frozen: padding moves slot 0 to the new degree, leaves slots 1–7 at per₃'s
values, and appends zeros.

**The reduction.**  The dual of `det_n` is the rank-one locus, the Segre
`P^{n−1} × P^{n−1}`, of dimension `2n − 2` and degree `C(2n−2, n−1)`.  Polar
degrees vanish above `dim X^∨` and the top nonzero one is `deg X^∨`, which
reproduces `det₄`'s tail exactly: `δ₇ = 0` and `δ₆ = C(6,3) = 20`.  ✓  At
`n = 5` the dual has dimension 8, so `δ₈(det₅) = C(8,4) = 70` and `δ_k = 0` for
`k ≥ 9`.  **The support of the padded profile (slots 0–7) therefore sits strictly
inside `det₅`'s support (slots 0–8), and the slot-7 violation that worked at
`n = 4` is gone.**  What is left is one comparison:

> **is `δ₆(det₅) < 30`, and is `δ₇(det₅) < 6`?**

Two integers decide whether the conormal method reaches `dc̄(per₃) ≥ 6` or caps
at 5.  A *lower* bound of 30 on `δ₆(det₅)` closes the branch; no exact value is
needed to kill it.

**Deliverable.**  The two integers, or two-sided bounds sufficient to decide;
and the general statement for `n ≥ 5` — since `2n − 2 ≥ 8 > 7` always, the
route can never again win on support and needs a numerical violation every time.

**Health warning.**  The derivation in this section is the integrator's, from
the dual-variety identification, and is checked only against `det₄`'s measured
profile.  Re-derive it before relying on it.  Note also that
`x₀²·per₃` is non-reduced; state which conormal cycle is being compared and
whether the specialisation inequality applies to it as stated, before computing
anything.

### C5 — the length-5 closure walk, and the int64 widening

**Goal.**  s60 built the census and the ladder theorem gave it teeth: a
full-rank result at a tail's closing cell settles that tail for `D > 0` **in
every degree**.  `results/s60_tail_census.md` is sorted for exactly this.

    n_χ ≤ 30 000  : 127 tails, 517 census rungs
    n_χ ≤ 100 000 : 199 tails, 775 census rungs
    n_χ ≤ 300 000 : 289 tails, 1 058 census rungs

**Deliverable.**  Walk the queue by `n_χ` as far as the budget reaches, banking
per cell.  Plus the named engineering item: **widen the int64 multiset code** of
the s45 build, which is what confines the walk to `δ_close ≤ 18` and blocks 183
tails.  892 of 1 075 closing cells are buildable today; the widening is what
makes the census finishable rather than merely long.

**Why it is worth a slot even though it has never found anything.**  It is the
only line in the programme with low variance, and the ladder theorem converts
each result from one cell into a whole tail.  It also keeps the certificate
corpus growing while the gate sessions run.

### C6 — the certificate gap, and the verifier defect

**Goal.**  s60 reports `mult_det = a` at 419 cells, of which **264 carry no
checkable certificate** — their proof is algorithmic, by the sparse Wiedemann
route.  That is the largest body of unwitnessed claims in the programme and
nobody has proposed fixing it.

**Deliverable.**  A `gct-cert/1` kind for the sparse-route nonsingularity
certificate — seeds, levels, pinned evaluation rows, checked kernel candidates —
written into `docs/artifacts.md`, implemented in `tools/verify/verify.py`, and
back-filled across s60's 264 cells.  In the same pass, the verifier defect s56
flagged: large `nonvanishing_minor` determinants fail the `content` line on
Python's integer-to-string limit *after* the rank checks pass.  One
`sys.set_int_max_str_digits` call.

### C2 — the LMR predecessor at `δ = 23`  ·  gated on C1 or S1

`a₂₃ = 273`, `a₂₄ = 274`, `sk` already constant at 48 825 from `δ = 23`.  So the
predecessor `((61,17,2⁷), 23)` is `Θ⁺ : C²⁷³ → C⁴⁸ ⁸²⁵` — one column narrower,
identical target — and full rank there forces `i_det = 1` at the LMR cell
exactly, using only the two ambient values and ladder monotonicity.  Cheaper
than the goal cell and strictly more informative.

**Read S6 first.**  Manivel's reduction is unavailable at `δ = 23`
(`2δ = 46 < 48 = |ρ| + ρ₁`), so this cell's target dimension rests on s58's
reduction alone.  That is the single largest single-source dependency in the
programme and S6 exists to remove it.

### C3 — the LMR cell itself  ·  gated, and only if C2 is inconclusive

`C²⁷⁴ → C⁴⁸ ⁸²⁵`.  13.4 million entries dense, but the rank is at most 274, so
the target coordinates need not be materialised at once.  Skip this session
entirely if C2 settles the cell.

### C4 — the padded side at the LMR cell  ·  gated on C2 or C3

**This is the session the batch exists for.**  `i_det = 1` is not `D > 0`;
`D = i_det − i_pad` needs `i_pad` at the same cell.  Every other session in
Track II is preparation for this one.  Brief it early even though it runs last,
because the padded-side instrument does not exist yet and its construction is
the long pole — and because C1's and S1's answers determine what it can be built
on.

### S2 — the `r = 5` special fibre, at the primitive family **[change]**

**The re-scoping is the point.**  The Rees boundary audit proposed the
compression incidences and a four-dimensional transverse quotient.  **That four
is zero**: at `C₂₁ ∩ C₃₂` the two components' tangent spaces are 57-dimensional
each — not 50; the omitted 7 is the flag motion in `Gr(2,4) × Gr(1,4)` — and
they span the full 64-dimensional `ker dΦ`.  Same at `C₂₁` alone (57 = 57) and
at `ker ∩ coker` (75 = 75).  Every spanning vector was checked to annihilate
`dΦ`.  A session briefed on the transverse problem would be briefed on nothing.

What survives, and what the audit itself ranked third, is the right first
priority: **the primitive family and its incidences** — the analogue of the
`n = 3` skew-symmetric component that Hüttenhain–Lairez show compression
analysis provably misses, and the only base-locus type at `r = 5` where nobody
has looked.

**Deliverable.**  `dim F(J_C)`, or an upper bound on `dim(D₅ ∩ W)`.  Recall
`R₅ ⊆ D₅ ⟺ dim(D₅ ∩ W) = 35`, and `≥ 31` is certified over `Q`.  **An upper
bound below 35 is a theorem, not a measurement** — the only such route the
programme has.  s59 named this deliverable and said it needed a CAS; the CAS is
now available.

**A caution the audit earns.**  "The tangent cone spans" does not close the
loophole: a normal cone can carry components no tangent space sees.  The quadric
system in the 64-dimensional kernel and its minimal primes remain legitimate.
What is *not* available is the dramatic coordinate reduction the audit promised,
because there is no transverse complement to eliminate.

### S6 — the Adams part at the LMR cell, independently

**Goal.**  `sk = (g + T)/2` with `g = 92 000` and `T = A = 5 650`.  `g` is
confirmed by three routes.  **`A = 5 650` is single-source**: s58's reduction and
the external Manivel route, with s58's `A` column validated at thirteen smaller
cells but not at the goal cell, where the direct partition sum is out of reach
(`p(96) = 1.18×10⁸`).  C2 and C3 both rest on it, and at `δ = 23` Manivel is
unavailable, so there `A` rests on s58 alone.

**Deliverable.**  `A` at `((65,17,2⁷), 24)` and at `((61,17,2⁷), 23)` by a route
sharing no code with s58 — the natural candidate being the Adams operation on
the `sl₄` side, evaluated where Manivel's threshold does not reach.  A
disagreement here would invalidate Track II before it is run, which is precisely
why it is worth a slot that produces no new mathematics if it agrees.

### S4 — the stable-range `D` search  ·  gated on S1

If S1 lands, the programme gains an axis it has never had: search over **tails**
`λ̄` rather than over cells, with cost driven by `ℓ` and `|λ̄|` and independent
of `δ` and `N`.  The stable range is where the ladder theorem says nothing more
can change, so a stable `D > 0` is a `D > 0` at every degree above.  Scope: how
far in `ℓ` the CAS reaches, and whether `ℓ = 9` — the smallest length at which
any equation the programme knows is non-vacuous — is inside it.

### S5 — the `dc̄` reach audit  ·  uses S3

**Adversarial, and the batch's most useful session if the gate stays shut.**
Every obstruction the programme holds certifies `dc̄(per₃) ≥ 5`, which is LMR's
published bound.  Ask what would have to be true for **any** instrument now in
hand to reach 6 — the conormal method (S3 answers this concretely), the LMR
module family at `n = 5` and the census conditions that pinch it, the Foulkes
rank, the Rees route — and say plainly, per instrument, if the answer is that it
cannot.

**Read `docs/` and not the reports.**  Five of batch 9's corrections were to
statements that were right in a report and wrong in the summary of it.

---

## 4. Dependencies, drawn

    C1 ─┐                       C5   C6   S2   S3   S6      (ungated)
        ├──> C2 ──> C3 ──> C4                    │
    S1 ─┘                                        └──> S5
     └────> S4

`C4` will accept an opening from either gate.  `C3` runs only if `C2` is
inconclusive.  Nothing else waits on anything.

---

## 5. The decision point

If **both** C1 and S1 return negatives, Track II never runs and three Claude
slots come free.  Do not backfill them with more of C5.  The batch becomes:

1. **S5 delivers the verdict**, with C1's and S1's characterised failures as
   evidence rather than as absences.
2. **The write-up takes the free slots.**  `paper/det3-conductor.tex` and
   `paper/det4-onset.tex` are single-writer files that have waited across four
   batches.  The repository is public now.  Twelve dead routes, the ladder
   theorem, Theorem P, Proposition S, the specialisation inequality and the
   conormal certificates are a paper whether or not `D > 0` is ever found — and
   seven ambient-plethysm selectors carrying no signal is a result other people
   should not have to rediscover.

State this in advance so it is not read as retreat when it happens.

---

## 6. Why the split is 6/6 and not 5/5

Batch 9 was 5/5 and produced no implementation of the instrument everything else
was waiting on.  The stock-take corrected to 6/4 for that reason.  It is back at
6/6 here because S1 **is** implementation — it just happens to be CAS
implementation rather than repository implementation, and it belongs with the
side that has the CAS discipline and does not need the certificate format.

The dividing line is not theory versus practice.  It is: **does the session
write into the repository's certificate corpus?**  C1–C6 do and are briefed
against `226b4ef1` with pre-registration and bundle delivery.  S1–S6 deliver
prose, numbers and code that the integrator re-derives before anything enters
the record.

---

## 7. Reserves

**R1 — external critic, round 4.**  Only after S5.  A critic pointed at the
programme before the reach question is settled will re-litigate settled ground.

**R2 — the six-row and length-6 closure extension.**  `wk9_s60_tails.py`
generalises.  Worth having costed before it is needed, not before.

---

## 8. Standing conditions for every brief in this batch

- Base commit `226b4ef1`; every `PREREG` names it.  Old base hashes
  (`0960bd5` and the rest) resolve only in the private archive now.
- Pre-registration before any computation.  Bank per cell.
- `python-flint` for exact linear algebra; both house primes
  `2147483647` and `2147483629`.
- Any `D > 0` cell goes through the verification protocol before it is
  reported anywhere, including in conversation.
- `docs/brief_wording.md` §2 and §4 are binding, and §5 — the degeneracy
  direction pre-check at all three of `det₄` pencil, reducible `ℓ·c`, and the
  full ten-variable `ℓ·per₃` — applies to any new statistic S3 or S5 proposes.
- Bound every long run at launch with `timeout` and `ulimit -v`; write the run's
  process id to `results/logs/<run>.pid`; end a run only by that recorded id.
- Single-writer files are not touched by workers: `paper/det3-conductor.tex`,
  `paper/det4-onset.tex`, `PROJECT_NOTES.md`, `docs/boundary_deficit.html`.
- Delivery by bundle.  No file over 5 MB.  Logs under `results/logs/`.
- Commit messages carry `Co-Authored-By` only.  No session-link trailer, in
  commits or in any script that writes commits, and no such URL in any file —
  the history was rewritten once to remove 260 of them.
