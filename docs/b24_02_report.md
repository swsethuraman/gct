# B24-02 — Two lineage gaps closed, and row 1 made unconditional at `N = 5`

**Slot:** B24-02, Batch 24 phase 1. **Worktree:** `work/batch15_workers/B15-01`, branch
`b15-01-ci159`. **Starting HEAD:** `cc14e88cca7860b4a666ecf2bc18701ac8a05584`, confirmed by
`git rev-parse HEAD`. `git status --porcelain` at start: **10 383 entries, all untracked**, none
of them tracked modifications (`git status --porcelain --untracked-files=no` is empty); the
untracked set is the `results/logs/b15_01_*` receipt pile, `results/b15_01/cache/`,
`results/b15_01/verification_cache/` and `results/b18_01/literature/`. **Read-only git; nothing
committed, nothing staged, no sealed packet edited.**

All dimensions in this report are **affine** dimensions of graded pieces of a polynomial ring
(G24). No projective dimension appears anywhere in this slot, and none is implied.

---

## Plain terms, up front

Three things were asked for. All three are delivered.

1. **C45, the `n = 3` positive control, replayed — and the LMR dependency settled.** The
   structural half of the control replays exactly by hand: LMR's own highest weight `Ω(4,3)`
   expands to the partition `(19,7,2⁵)`, the degree formula gives `δ = 12`, and `ℓ(λ) = 7`. What
   does **not** replay away is the dependency. `i_det((19,7,2⁵), 12) >= 1` is LMR's theorem and
   **nothing in the record can replace it**, because the direction of the inequality is wrong for
   the instrument: a modular nullity at an integer point bounds `i_det` from **above**, never
   from below. The measurement alone gives `0 <= D <= 1`. **The whole sign of the programme's only
   positive result rests on LMR.** And at that point of use the source's read-status is
   **UNREAD** — the only labels on record are `UNREAD-SPECIALIST` for a different statistic
   (B22-02) and `PRIMARY` for a different theorem (B23-06 read Thm 1.0.1, the `dc̄ >= m²/2`
   bound). The statement actually used is **Thm 2.3.1** plus the paper's printed worked instance.
2. **C24, the Astra five-block theorem, replayed independently — PROVED, no correction.** I
   re-derived Lemma 7.1, the weight identity (7.2), Theorem 8.1, Theorem 8.2 and Corollary 8.3
   from the definitions, and reproduced the old arc's five parameters `β = 2, u = 0, h = −1,
   m = 0, L = 2` from scratch as a cross-check. Every step holds. Its verbatim scope limit is
   carried forward in §3.4.
3. **The `N = 5` Kleiman pilot: PASS, in one pilot.** Row 1 is now a **PROVED-kill on elementary
   premises across the whole window `N = 5..8`**. Kleiman is discharged from row 1. Every
   pre-registered prediction hit, including the three negative controls.

The honest shape of the batch: **one gap closed, one gap sharpened into a harder finding than it
was filed as, and one theorem upgraded.** C24 is closed. C45 is not closed by this slot and
cannot be closed by replay — §2.5 says what would close it.

---

## 0. What this slot can and cannot establish

**A replay gives a lineage, not a new result.** Tasks 1 and 2 add a second, independent
derivation of results already on the record. If a replay agrees, the claim gains a lineage and
its label is unchanged. It does not become more true, and the original producer keeps priority.

**What a replay cannot do.** It cannot repair a dependency on an external source. Task 1 is the
case in point: I can replay every internal step of C45 and still leave `i_det >= 1` resting
exactly where it rested. That is why §2 spends more space on read-status than on arithmetic —
the brief is explicit that the labels are the deliverable, and it is right.

**What the pilot can establish.** A modular rank at an explicit integer point of `D45` is a
**floor** on the generic rank (rank mod `p` <= rank over `Q`, and the rank at one point <= the
maximum over the variety). A padding ceiling derived from `J_{lP} ⊆ (l, P)` is an **upper** bound
valid at every padding point. A floor strictly above a ceiling is therefore a **proof**, not a
measurement — the numbers are one-sided and the inequality survives any sharpening. This is
B23-03's method and its logic is unchanged here.

**What this slot does not do.** It nominates no cell, claims no gap, and edits no sealed packet.
Where a replay disagrees with its source it is reported as a finding (§2.5 has one such note,
about labelling rather than arithmetic).

---

## 1. Pre-registration

The pilot's pre-registration is `results/b24_02/p1_prereg.md`, sha256
`b0b4b66054d41f583d53d1341648d67cf130732b60e6e66cd8819a6d85c70d2b`. It was written and hashed
**before** the pilot ran, and **G25 is satisfied**: that hash is the **first field** of
`results/b24_02/p1_n5_kleiman.json`, written before `import flint` and before any computation, with
the run aborting on mismatch. The recorded `match` is `true` and
`recorded_at_elapsed_s` is `0.0`.

The pre-registration fixed, before the run: the closed forms `h_5(k) = (3k²+3k+2)/2`,
`A(a) = 6a−2`, `H(k) = 18k−24` and `D(k) = (3k²−33k+50)/2`; the seven padding ceilings; the
Newton coefficients `e = 10, 15, 3, 0, …` at `k_1 = 10`; the prediction of **ties** at
`k = 3, 4, 5` and **strict** margins at `k = 6, 7, 8, 9`; the seed `20260919`; the modulus
`2^31 − 1`; and the PASS/FAIL rule in full. It also pre-registered three **negative controls** —
that `D(k) < 0` at `k = 7, 8, 9`, i.e. that the tail point `F_0` fails exactly where the random
point is needed. All of these are checked against the run in §4.3.

Tasks 1 and 2 are replays and hand re-derivations. Per the brief they are **not pilots** and
carry no wrapper: neither computes. Every number in §2 and §3 was produced by hand and is shown
in full so that it can be checked without running anything.

---

## 2. Task 1 — C45, the `n = 3` positive control (ranked 1)

### 2.1 What C45 claims, and where it is written

`CLAIMS.md` @ `ce43cdb7` (sha256 `2b7ba688…`) row **C45**, against draft Thm. 8.1:

> `n = 3` unpadded ladder `(3δ−17, 7, 2^5)`: `a = 0,2,4,5` at `δ = 8..11`, `a = 6` for `δ >= 12`;
> `D = +1` ∀ `δ >= 12`, `D = 0` at 9–11; base rung `m_per = 6 > 5 = m_det`
>
> **PROVED** (record: "a theorem, not a measurement"; Prop. S + Lemma L); rungs 12–16 MEASURED at
> two primes; `i_per = 0` proved over `Q`; base `i_det(12) >= 1` **from LMR (read-status for this
> use not on record, G-15)**

Sources: `docs/s73_report.md` (sha256 `f40783ba…`), `docs/lmr_cell.md` (sha256 `0ab35e4e…`),
`docs/equation_census.md` (sha256 `ba7b20f9…`), all at the archive pin `82633a60`.

### 2.2 The replay — the structural half, by hand

The conventions are s73 §1: `a` = multiplicity of `S_λ(C^7)` in `Sym^δ(Sym^3 C^7)`;
`U_X = HWV_λ ∩ I(X)`; `i_X = dim U_X`; `mult_X = a − i_X`; `D = i_det − i_per`.

**(a) The weight and the degree replay exactly from LMR's own formula.** `equation_census.md`
§2.1 records LMR's highest weight

    Ω(k,d) = (d−1)(d−2)(k+2)·ω_1 + (d(k+2) − 2k − 5)·ω_2 + 2·ω_{k+3}.

At `k = 4, d = 3` the three coefficients are

    ω_1 : (3−1)(3−2)(4+2) = 2·1·6 = 12
    ω_2 : 3·6 − 2·4 − 5   = 18 − 8 − 5 = 5
    ω_7 : 2

Converting fundamental weights to a partition (`λ_j = Σ_{i>=j} c_i`):

    λ_1 = 12 + 5 + 2 = 19,  λ_2 = 5 + 2 = 7,  λ_3 = … = λ_7 = 2

so **`λ = (19, 7, 2⁵)`** — and `ℓ(λ) = k + 3 = 7`. The census's general form
`λ = (a_1+a_2+2, a_2+2, 2^{k+1})` gives the same with `a_1 = 12, a_2 = 5`. The degree follows
from `|λ| = δ·d`:

    |λ| = 19 + 7 + 10 = 36 = (k+2)d(d−1) = 6·3·2,   δ = |λ|/d = 12 = (k+2)(d−1) = 6·2.

**All four numbers — `λ`, `ℓ = 7`, `|λ| = 36`, `δ = 12` — replay exactly.** This is an
independent second lineage for the cell's identification, and it is worth having: it is derived
from the printed highest weight without using the paper's own printed degree, which
`equation_census.md` §2.1 notes is **inconsistent** with it (LMR's printed Thm 1.0.2 says
`n(n−1)`, giving 12 at `n = 4` where the weight gives 24). The record already resolved that in
favour of the weight; I confirm the resolution at `n = 3`, where it gives 12 either way and so is
not a discriminating test — the discriminating instance is `n = 4`.

**(b) The `D`-ladder's arithmetic replays.** With `a = 6` and `i_per = 0`, `mult_per = 6`; with
`i_det = 1`, `mult_det = 5`; `D = i_det − i_per = 1 = mult_per − mult_det = 6 − 5`. The row
`mult_det = 5 < 6 = mult_per` is exactly `D = +1`. Consistent throughout.

**(c) Lemma L replays as stated.** `c = c_{(3,0,…,0)}` is a nonzero ambient HWV; multiplication
by it is injective on `C[W]`, preserves `I(X)`, and is injective on `C[X]` for an irreducible
`GL_7`-stable cone `X ⊄ {c = 0}` — which `D_7` and `P_7` satisfy because `det_3` and `per_3` are
nonzero at a generic pencil. Restricting to highest-weight vectors gives
`i_X(δ) <= i_X(δ+1) <= i_X(δ) + [a(δ+1) − a(δ)]`, so **a flat `a`-ladder pins `i_X`**. Given
`a(δ) = 6` for `δ >= 12`, `i_det(12) = 1` and `i_per(12) = 0` propagate to every `δ >= 12`. The
step is correct and the hypotheses are checked in the source.

**(d) What I did not replay, and why.** `a(δ) = 6` for `δ >= 12`, the nullity certificates at
`δ = 12..16`, and Proposition S are **plethysm and rank computations**. Replaying them is a
numerical job, and the batch has exactly one, which task 3 spends (§4). They are **not** replayed
here and I do not claim them. The record carries three independent lineages for `a` already (two
plethysm engines to `δ = 20`, the house engine to `δ = 40`, and a from-scratch stable value
`a_∞((7,2⁵)) = 6`), which is the best-supported number in the cell.

### 2.3 The LMR dependency — what exactly is used

**The dependency is real, and it is load-bearing in the strongest sense.** The record says so
itself. s73 §2(c), verbatim:

> `i_det(12) >= 1` is LMR's theorem at this cell (adopted); `i_det(12) <= 1` is the measured
> nullity `1` at both primes (`rank_p <= rank_Q`)

and s73 §8, verbatim:

> `D = +1` for every `δ >= 12` therefore rests on: LMR (literature), Lemma L and Proposition S
> (s57, proofs re-read here), two plethysm engines, and the `δ = 12` nullity certificates of this
> session (and s62/s63/P0-A).

**Why no instrument on the record can replace it.** This is the part worth stating plainly,
because it is sharper than "no second lineage". `i_det = nullity_Q[E; ev_det]`, and a modular
nullity satisfies `nullity_p >= nullity_Q`. So the measurement `nullity_p = 1` proves

    i_det(12) <= 1     — a CEILING.

`D = i_det − i_per` and `i_per = 0` is genuinely proved over `Q` (a nullity-`0` certificate at one
prime forces `nullity_Q = 0`, the direction that does work). Hence `D = i_det`, and **the
measurement alone establishes only `0 <= D <= 1`** — which is not a positive result at all. The
entire sign comes from the LMR floor `i_det >= 1`. No sharpening of the numerics, no extra prime,
no fresh evaluation family can supply it; the inequality runs the wrong way for the instrument.
Only an **exact** rank over `Q`, or a proof of ideal membership, or LMR, can.

**The record-internal alternative is incomplete, and the record says so.** The exhibited integer
vector `U_D` is checked to vanish at 32 determinant pencils exactly over `Z`. s73 §3 labels this
honestly — "finite-point vanishing is Schwartz–Zippel evidence; the rigorous `v ∈ I(D_7)` at
`δ = 12` is LMR" — and s62 §206 says the same in its own words ("finite-point vanishing is
Schwartz–Zippel evidence of ideal membership, not a…"). So membership is **not** proved
internally.

**What is used, precisely.** Not `dc̄(perm_m) >= m²/2`. The statement in play is LMR
**Theorem 2.3.1**, which `equation_census.md` §2.1 and its row 1 identify as giving the equations
of `Dual_{k,d,N}` as a copy of the `SL_N`-module of highest weight `Ω(k,d)` — non-vacuous exactly
when `N >= ℓ(λ) = k+3`, which at `n = 3` is `7 = r`, the pinch. Together with the containment of
the determinant orbit closure in the dual-degenerate locus, a nonzero element of that module is a
weight-`λ` highest-weight vector in `I(D_7)`, i.e. `i_det >= 1`. The census also records that
**`λ(4,3) = (19,7,2⁵)` at `δ = 12` is LMR's own worked instance, "the partition printed in the
paper"** — so the cell is not an extrapolation of the family but the paper's stated example.
`lmr_cell.md` §3b calls `a = 6` "LMR's own value".

### 2.4 The read-status finding — stated plainly, as the brief asks

**At the point of use, the source is UNREAD.**

| what | where used | read-status on record |
|---|---|---|
| LMR **Thm 2.3.1** + the printed instance `λ(4,3) = (19,7,2⁵)`, `δ = 12` — **the statement C45 needs** | `equation_census.md` §2.1; `lmr_cell.md` §3b; s73 §2(c) | **none. No label, no file, no hash, anywhere in the record.** |
| LMR **Thm 1.0.1** (`dc̄(perm_m) >= m²/2`) — a *different* theorem | B23-06 §L5 | **PRIMARY** (ar5iv; arXiv 1004.4802v1 PDF sha256 `cfc28275a8c6b27f…`) |
| LMR, "the dual-defect statistic" — a *different* use | B22-02 §5 | **UNREAD-SPECIALIST**, and there explicitly *not load-bearing* |

I verified this directly: `equation_census.md` (sha256 `ba7b20f9…`) contains **zero** occurrences
of `PRIMARY`, `SECONDARY`, `UNREAD`, `read-status`, `ar5iv`, or any `sha256`. It is a session-55
document and predates the G14/G14′ convention. No local copy of arXiv 1004.4802 exists in this
worktree (`results/b18_01/literature/` holds only 1411.0777 and 2303.09028); nothing was fetched
in this slot.

**The nuance, stated in fairness to session 55.** The census's §2.1 shows strong internal
evidence of a genuine reading: it quotes the paper's printed `Ω(k,d)` verbatim, cites the printed
Thm 1.0.2 and its `n(n−1)`, identifies the printed partition, and flags an inconsistency
*between two printed statements* — none of which is obtainable from an abstract or a secondary
source. So the honest label is not "nobody looked". It is that **the reading was never recorded**,
and under G14′ an unlabelled, unhashed, un-filed reading cannot be certified PRIMARY after the
fact. **UNREAD at the point of use** is the correct label today, and the fix is cheap (§2.5).

**Consequence for Paper 3.** `CLAIMS.md` labels C45 **PROVED**. On the record as it stands, the
accurate label is **PROVED modulo LMR Thm 2.3.1 at this cell, whose read-status is UNREAD**. This
is not a new defect — `CLAIMS.md` names it in the row itself and `GAPS.md` G-15 files it — but
the draft presents C45 as its worked evidence that the instruments work, and §2.3 shows the
dependency carries the *sign*, not a detail. **That is the finding, and it matters more than the
replay.**

### 2.5 What would close C45, priced

- **Cheapest, and it does close it: one reviewer-hour.** Fetch arXiv 1004.4802v1, read
  **Thm 2.3.1** and the worked instance, and record PRIMARY with file and sha256 at the point of
  use. The paper is already known reachable and hashed — B23-06 reached it and recorded
  `cfc28275a8c6b27f…` for exactly this PDF. Two things must be confirmed in the text, not
  assumed: (i) the module is non-vacuous at `N = 7`, and (ii) `D_7` lies in the dual-degenerate
  locus the theorem is about at `k = 4`. **This is the recommended route** and it needs no pilot.
- **Record-internal, and it is not cheap.** Prove `U_D ∈ I(D_7)` outright. Schwartz–Zippel
  evidence must be replaced by an injective evaluation set — B22-01-sized, one or two pilots.
  B23-10 §7 prices it the same way. Worth doing only if the reading route fails.

**Status after this slot: C45 stays OPEN.** The structural half has a second lineage (§2.2); the
dependency is now named exactly (Thm 2.3.1, not Thm 1.0.1), its read-status is settled (UNREAD at
the point of use), and its load is characterised (it carries the sign). The gap is *sharper* than
G-15 filed it, and cheaper to close than B23-10 priced it, because the target theorem is now
identified and the PDF is already hashed on the record.

---

## 3. Task 2 — C24, the Astra five-block theorem (ranked 2)

### 3.1 What was replayed, and against what

`CLAIMS.md` C24, against draft Thm. 4.12: Astra Thms. 8.1, 8.2, Cor. 8.3, labelled **PROVED**,
lineage "producer (Astra); recorded, not replayed (GKZ corrigendum); tabulated by B20-10 §10
(R21, READ). No reviewer re-derivation on record (G-23)."

Source: the archived Astra `REPORT.md` at `82633a60`, sha256
`c79145e0077beeb05527a970529d9822e5c331043dd977827b7ef38459563c5c`. **This matches byte-for-byte
the hash the GKZ corrigendum C12 recorded when it read the packet**, so the archived bytes are the
bytes C12 saw. C12 itself states "Recorded, not replayed and not broadened" — it is a READ, not a
lineage. The replay below is therefore the **second lineage**, and it is independent: I did not
run `pilot_exact.py` (which would not be independent) and I wrote no code at all — every step is
by hand from the definitions in §§3–7.

### 3.2 The re-derivation, step by step

**Setup (§3).** `X = [[a, r],[c, S + K(v)]]` in `Mat_4`, sixteen coordinates
`a` (1), `r` (3), `c` (3), `S` symmetric (6), `v` (3). `M` is a finite source subspace of
degree-`4d` polynomials on `W^k` with `z(PYQ) = (det P det Q)^d z(Y)` and `z(Y^T) = z(Y)`.

**Lemma 7.1 replays.** Take `Q = I` and `P = diag(p_1..p_4)`. A monomial with total row-`i`
degree `R_i` (summed over pencil indices) transforms by `∏ p_i^{R_i}`, and `(det P)^d = ∏ p_i^d`,
so `R_i = d` for every `i`; likewise `C_j = d` by columns. The adapted change of coordinates
touches only the lower-right `3 × 3` block, so it preserves the first row and first column counts.
Row 1 is `(a, r_1, r_2, r_3)`, giving **`α + ρ = d`**; column 1 is `(a, c_1, c_2, c_3)`, giving
**`α + κ = d`**. Total degree is `4d`, so

    α + ρ + κ + σ + ν = 4d  ⟹  (d−α) + (d−α) + α + σ + ν = 4d  ⟹  σ = 2d + α − ν.

That is (7.1) in full, with `0 <= α <= d` and `ν >= 0`. **Correct.**

**The weight identity (7.2) replays, and is a consequence of 7.1.** If `D_w(t)` scales the five
blocks by `t^{e_a}, t^{e_r}, t^{e_c}, t^{e_S}, t^{e_v}`, a monomial's exponent is
`e_aα + e_rρ + e_cκ + e_Sσ + e_vν`; substituting `ρ = κ = d − α` and `σ = 2d + α − ν` collapses it
to

    d(e_r + e_c + 2e_S) + α(e_a − e_r − e_c + e_S) + ν(e_v − e_S)  =  dβ + uα + hν,

which is exactly the claimed form, with `β, u, h` read off. **Numerical cross-check on the old
arc.** `w_old = (−1,−1,1,1,0)` gives `β = −1 + 1 + 2 = 2`, `u = −1 + 1 − 1 + 1 = 0`,
`h = 0 − 1 = −1` — **all three match the report's `beta=2, u=0, h=−1` exactly.** And
`m_w = min_A(β + up + hq)`, `L_w = max − min`: over
`A = {(0,0),(1,0),(0,1),(0,2),(1,2)}` the values `2 − q` are `2,2,1,0,0`, so `m = 0` and
`L = 2` — **both match**. Finally the report's `C z = projection onto ν > 2d` replays: the
exponent is `2d − ν`, and `2d − ν ∉ [0, 2d]` with `ν >= 0` means exactly `ν > 2d`. **Five
parameters and the identification of `C`, all reproduced from scratch.**

**Theorem 8.1 replays.** If `Cz = 0` then no component has `ν > 2d`, so with (7.1)'s
`0 <= α <= d` and `ν >= 0` the `(α,ν)`-support lies in `[0,d] × [0,2d] = dP`. A linear functional
on the polytope `P` attains its extremes at vertices, and `A` contains all four vertices of
`P = [0,1] × [0,2]` while `A ⊆ P`, so `min_P = min_A` and `max_P = max_A`. Hence
`dβ + uα + hν ∈ [d·m_w, d·m_w + d·L_w]`, i.e. **no forbidden component survives**, so `N_w z = 0`.
For the identity: every forbidden `(α,ν)` must fail `(α,ν) ∈ dP`, hence must have `ν > 2d`, hence
already appears in `Cz`; so `N_w` is "select and regroup the components of `Cz`", an **exact
factorization `N_w = L_w C`**, not an inclusion seen on samples. Since `w_old` is in the family
and `N_{w_old} = C`, the simultaneous kernel of all `N_w` equals `ker C`. **Correct, both halves.**

**Theorem 8.2 replays, including the sumset (8.1).** `A_d`, the `d`-fold sumset of `A`: choosing
`p` factors with first coordinate 1 (from `{(1,0),(1,2)}`, each contributing 0 or 2 to `q`) and
`d − p` from `{(0,0),(0,1),(0,2)}` (each contributing 0, 1 or 2):
- `p = d`: `q` is a sum of `d` terms from `{0,2}`, so `q` is **even** and every even `q ∈ [0,2d]`
  occurs.
- `p < d`: the reachable set is `⋃_{j=0}^{p} [2j, 2j + 2(d−p)]`. Since `d − p >= 1`, consecutive
  intervals overlap (`2j + 2 <= 2j + 2(d−p)`), so the union is **all** integers in `[0, 2d]`.

That is exactly `A_d = {(p,q) : 0<=p<=d, 0<=q<=2d, p<d or q even}`. **The covering step, which
the report states in one line, checks out.** Then for `z ∈ ker C`: on the slice `α = d` we get
`ρ = κ = 0`, and transposition sends `X = [[a,r],[c,S+K(v)]]` to `[[a,c],[r,S−K(v)]]` — it swaps
`r ↔ c`, fixes `a` and `S`, and sends `v ↦ −v`. With `ρ = κ = 0` it acts by `v ↦ −v` alone, so
`z(Y^T) = z(Y)` kills every **odd**-`ν` component there. Hence `supp(z) ⊆ A_d` and
`N_w^support z = 0`. The report's remark that transpose invariance is **essential** is correct:
without it the `α = d`, odd-`ν` slice is not excluded and the strengthened test is not implied.

**Corollary 8.3 replays** immediately: all rows of `N` lie in the row space of `C`, so
`rank(C,T,N) = rank(C,T)` and `ker(C,T,N) = ker(C,T)`.

### 3.3 Ruling

**PROVED, with two lineages. No correction required.** Every step of §§7–8 is correct as written;
the two places where the report compresses an argument to a single sentence — the vertex argument
in 8.1 and the interval-covering in 8.2 — both survive being written out. The independent
reproduction of `β, u, h, m, L` for the old arc and of the identification `C = ` projection onto
`ν > 2d` is a numerical check that the weight bookkeeping is right, done by hand and independent
of `pilot_exact.py`. **G-23 is closed.**

One observation, not a defect: the theorem needs `A` to contain the vertices of `P` and to be
contained in `P`. Both hold for this `A`, and the report's proof relies on it implicitly when it
equates the extremes over `P` with those over the exponent set. Worth stating explicitly if the
result is ever transported to another block decomposition, since it is the one hypothesis that a
different configuration could break.

### 3.4 The verbatim scope limit, carried forward

The brief requires this to travel with the theorem. From the Astra `REPORT.md` §1, verbatim:

> The conclusion concerns universal coefficient-support tests along the specified family. It does
> not cover equations among allowed jets, descent between different parameter points of a limit
> fiber, special-locus cancellations followed by stronger normalization, anisotropic weights
> inside a block, or different matrix-coordinate bases. None of those are ruled out.

And the hypotheses, from Cor. 8.3 verbatim: "The statement is over characteristic zero on the
complete `M`. It is not a restricted four-column rank assertion, a sampled-kernel claim, or a new
rank measurement." Also §3: "It is essential that polynomial descent is assumed only for `E`, not
for arbitrary `z` in `M`" — and the interval theorem needs only the two diagonal-torus
symmetries, while the **exact-support** theorem additionally needs transposition. **That scope is
what makes the theorem honest, and my replay confirms each hypothesis is actually used.**

---

## 4. Task 3 — the `N = 5` Kleiman pilot

### 4.1 The question

Row 1 (rank thresholds of `d_1`) is a PROVED-kill at `N = 6, 7, 8` for every `k` on elementary
premises (B23-03 Thm 3.2, sha256 `0101f224…`; reproduced by B23-10 §3.2, 8/8 floors, 8/8
ceilings, 3/3 Newton certificates). At `N = 5` B23-03 leans on GKZ Theorem B, which for `k >= 7`
adopts **Kleiman** (GKZ corrigendum C2: "Kleiman remains the only adopted input for `k >= 7`").
B23-10 §3.2 sketched the discharge by hand for the `k >= 10` tail and left `k = 7, 8, 9` to a
pilot. This is that pilot.

### 4.2 The three ingredients

**Padding ceiling (elementary).** Every padding point is a product `lP`, so `J_{lP} ⊆ (l,P)` and
`rank M_k(lP) <= dim S_k − h_5(k)` with `h_5(k) = C(k+3,3) − C(k,3)`. By hand,
`[(k+3)(k+2)(k+1) − k(k−1)(k−2)]/6 = (9k² + 9k + 6)/6 = (3k² + 3k + 2)/2`. Universal ceilings for
any quartic: `5·dim S_{k−3}` at `k = 3,4,5` and `5·dim S_3 − C(5,2) = 165` at `k = 6`.

**Tail point.** `F_0 = x_1x_2x_3x_4 − x_5^4`, i.e. B23-03's cyclic matrix with every `o_i = x_5`.
The pilot verifies symbolically that it is the determinant of
`[[x1,0,0,x5],[x5,x2,0,0],[0,x5,x3,0],[0,0,x5,x4]]`, so **`F_0 ∈ D45`**; the expansion returned
exactly `{x1x2x3x4: +1, x5^4: −1}`. Its Jacobian ideal `(x2x3x4, x1x3x4, x1x2x4, x1x2x3, x5^3)`
is **monomial**, so `S/J` factors as `A ⊗ B` and its Hilbert function is exact for every `k`.
By hand: `A(a)` counts degree-`a` monomials in four variables with support of size `<= 2`, namely
`4 + 6(a−1) = 6a − 2` for `a >= 1`; `B(j) = 1` for `j = 0,1,2`; so
`H(k) = A(k)+A(k−1)+A(k−2) = 18k − 24` for `k >= 3`.

**Margin.** `D(k) = h_5(k) − H(k) = (3k² + 3k + 2)/2 − (18k − 24) = (3k² − 33k + 50)/2`, whose
roots are `(33 ± √489)/6 ≈ 1.81` and `9.19`, so **`D(k) > 0` exactly for integer `k >= 10`**.

### 4.3 Results — every pre-registered prediction hit

`results/b24_02/p1_n5_kleiman.json`, one wrapped run, **0.194 s**, peak job memory well under the
512 MiB cap, exit code 0.

| `k` | padding ceiling (proved) | det floor (mod `2^31−1`) | **margin** | predicted |
|---|---|---|---|---|
| 3 | 5 | 5 | **0** (tie) | tie ✓ |
| 4 | 25 | 25 | **0** (tie) | tie ✓ |
| 5 | 75 | 75 | **0** (tie) | tie ✓ |
| 6 | 146 | 165 | **+19** | strict ✓ |
| 7 | 245 | 299 | **+54** | strict ✓ |
| 8 | 386 | 475 | **+89** | strict ✓ |
| 9 | 579 | 695 | **+116** | strict ✓ |
| `>= 10` | `dim S_k − h_5(k)` | `F_0`: `dim S_k − H(k)` | **`>= 10`** (Newton at `k_1 = 10`: `e = 10, 15, 3, 0, …`) | ✓ |

Checks, all passing:
- `h_5(k)` at `k = 3..9` = `19, 31, 46, 64, 85, 109, 136` — **as pre-registered**; closed form
  verified for `k = 0..39`.
- Padding ceilings `5, 25, 75, 146, 245, 386, 579` — **as pre-registered**.
- `A(a) = 6a − 2` reproduced by brute-force enumeration, `a = 0..12`, **13/13**.
- `H(k) = 18k − 24` reproduced by brute-force enumeration, `k = 3..12`, **10/10**.
- `rank M_k(F_0) = dim S_k − H(k)` at `k = 3..7`, **5/5** — an independent confirmation that the
  monomial Hilbert function really is the Macaulay rank.
- `D(k)` closed form verified for `k = 3..39`; Newton coefficients `e = 10, 15, 3, 0, 0, 0, 0, 0`,
  all `>= 0`, `e_0 = 10 > 0` — **as pre-registered**.
- **The three negative controls fired exactly as predicted:** `D(7), D(8), D(9) = −17, −11, −2`.
  The tail point `F_0` **fails** at `k = 7, 8, 9`, which is precisely why the random-point floors
  are needed there and why the pilot could not have been replaced by hand arithmetic alone. A
  pre-registered prediction of failure that comes true is the sharpest check available on the
  instrument, and it is the reason this pilot is informative rather than confirmatory.

**One unpredicted number, noted:** the floor at `k = 9` is `695 = 715 − 20`. The `20` is the
degree of the rank-`<= 2` locus of a `4 × 4` matrix (codimension 4, Giambelli degree
`6 · 10/3 = 20`), i.e. the determinantal quartic in `P^4` has exactly 20 isolated singular points
and `H(k) → 20`. The measured floor is consistent with that and with nothing else; it was not
pre-registered and is reported as an observation, not a claim.

### 4.4 Verdict — PASS

**Coverage is complete over `k`:**
- `k <= 2`: `M_k` has no columns (`dim S_{k−3} = 0`); rank 0 on both sides.
- `k = 3, 4, 5`: the determinant floor **equals** the universal ceiling, so
  `r_k(P_5) <= ceiling = floor <= r_k(D_5)`. A tie: padding cannot exceed the determinant and no
  equation separates. This is exactly the `N = 6,7,8` pattern.
- `k = 6, 7, 8, 9`: certified modular floor **strictly above** the proved padding ceiling.
- `k >= 10`: `F_0 ∈ D45` with an exact monomial Hilbert function and the Newton certificate,
  margin `>= 10`.

**Theorem (B24-02.1, PROVED).** For `N = 5` and every `k >= 0`, `r_k(P_5) <= r_k(D_5)`. Hence
every `(r_det(k) + 1)`-minor of `M_k` vanishes on padding at `N = 5`.

**The premises are: the elementary padding ceiling, a certified modular floor at an explicit
integer point, the combinatorial Hilbert function of `F_0` with a brute-force cross-check, and
the Newton certificate. No Kleiman. No Dimca, no Gulliksen–Negård, no depth sensitivity.**

**Consequence, in one sentence for Paper 3:** *row 1 of B22-02 is a PROVED-kill on elementary
premises for every `k` across the whole window `N = 5..8`.* B23-10 §3.2's required qualifier —
"PROVED at `N = 6..8`, and PROVED at `N = 5` modulo Kleiman at `k >= 7`" — **is discharged**;
B23-03's original "PROVED-kill in the whole window `N = 5..8`" is now correct as written, though
for a reason B23-03 did not have.

The pilot cost 0.194 s of a 300 s budget. **The other two pilots were not spent** and no second
pilot was needed.

---

## 5. Exact scope and residues

**What is now closed.**
- **G-23 / C24**: CLOSED. Two lineages. PROVED, no correction, scope carried verbatim (§3.4).
- **Row 1 at `N = 5`**: CLOSED. Unconditional, elementary, every `k` (§4.4).

**What is not closed, and stays OPEN.**
- **G-15 / C45**: **OPEN.** The structural half has a second lineage (§2.2). The dependency is now
  named (LMR **Thm 2.3.1** and the printed instance, *not* Thm 1.0.1), its read-status at the
  point of use is **UNREAD**, and it carries the **sign** of `D`, not a detail. Closing it costs
  one reviewer-hour with a PDF already hashed on the record (§2.5).
- **C45's computational half**: not replayed here (`a`-ladder, nullity certificates, Prop. S).
  Three lineages already exist for `a`; the nullity certificates have one.

**Scope limits on this slot's own results.**
- §4's theorem is about **row 1 only** — rank thresholds of `d_1`. It says nothing about row 2
  (`d_j`, `j >= 2`), which B23-03 §3.3 leaves open, and nothing about `D45 ∩ P5` or G-A1.
- It discharges Kleiman **from row 1 at `N = 5` only**. Every other adopted use of Kleiman in the
  record is untouched; in particular GKZ Theorem B itself is not reproved, only bypassed for this
  one consequence.
- The determinant floors are at **one** random integer point, **one** prime. That is sufficient
  and not a weakness: a floor is one-sided, so a second prime or a second point could only raise
  it, never lower it, and the margins are proved inequalities either way.
- §3's ruling covers Astra Thms 8.1, 8.2 and Cor. 8.3 only. §§4–6 of that report (the arc
  classification, the nine initial-form classes) were **read for context, not replayed**.
- §2.2's weight derivation confirms LMR's printed weight is self-consistent at `n = 3`; it does
  **not** re-adjudicate the `n = 4` factor-of-two question, which is where the printed Thm 1.0.2
  and the printed weight actually disagree.

**A labelling note, reported not fixed (G13).** `CLAIMS.md` C45 carries the bare label **PROVED**
in its status column, with the LMR condition stated in the same cell. Given §2.3 — that the
dependency supplies the sign and not a refinement — a reader scanning the label column alone will
over-read it. This is a finding about presentation, **not** an error in the row's content, which
is accurate and complete. **No sealed file is edited by this slot.**

---

## 6. Labelled ledger

Producer-only (G18). Every row is this slot's own work; nothing is transcribed from another
producer as if it were mine.

| # | statement | label | lineage | where |
|---|---|---|---|---|
| B24-02.1 | For `N = 5` and every `k >= 0`, `r_k(P_5) <= r_k(D_5)`; row 1 is a PROVED-kill at `N = 5` on elementary premises | **PROVED** | this slot (pilot 1), by B23-03's method | §4.4 |
| B24-02.2 | Row 1 is a PROVED-kill on elementary premises across the whole window `N = 5..8`; Kleiman discharged from row 1 | **PROVED** | B24-02.1 + B23-03 Thm 3.2 (replayed by B23-10 §3.2) | §4.4 |
| B24-02.3 | Astra Thms 8.1, 8.2, Cor. 8.3 are correct as written | **PROVED**, second lineage | this slot, INDEPENDENT (hand); no code, `pilot_exact.py` not run | §3.2–3.3 |
| B24-02.4 | `β = 2, u = 0, h = −1, m = 0, L = 2` for `w_old`, and `C =` projection onto `ν > 2d` | **REPLAY**, INDEPENDENT (hand) | this slot | §3.2 |
| B24-02.5 | `Ω(4,3)` expands to `λ = (19,7,2⁵)`; `ℓ = 7`, `|λ| = 36`, `δ = 12` | **REPLAY**, INDEPENDENT (hand) | this slot, from the printed weight | §2.2 |
| B24-02.6 | `i_det(12) >= 1` is not obtainable from any modular nullity on the record: the measurement bounds `i_det` from above, so the numerics alone give only `0 <= D <= 1` | **PROVED** (elementary, `nullity_p >= nullity_Q`) | this slot; consistent with s73 §2(c), §8 | §2.3 |
| B24-02.7 | The statement C45 uses is LMR **Thm 2.3.1** plus the printed instance `λ(4,3)`, not Thm 1.0.1 | **READ** (source check of the record) | this slot, from `equation_census.md` §2.1 row 1 | §2.3 |
| B24-02.8 | At that point of use LMR's read-status is **UNREAD**: no label, file or hash anywhere; the only labels on record are for a different theorem (PRIMARY, B23-06) and a different use (UNREAD-SPECIALIST, B22-02) | **FINDING** | this slot, verified by exhaustive search of the cited documents | §2.4 |
| B24-02.9 | `F_0 = x_1x_2x_3x_4 − x_5^4` is the determinant of the displayed cyclic matrix, so `F_0 ∈ D45` | **PROVED** (symbolic, in-pilot) | this slot | §4.2 |
| B24-02.10 | `A(a) = 6a − 2` (`a >= 1`) and `H(k) = 18k − 24` (`k >= 3`) for `F_0` at `N = 5` | **PROVED** (monomial ideal; brute-force cross-check 13/13 and 10/10) | this slot | §4.2–4.3 |
| B24-02.11 | The 20-point singular locus reading of the `k = 9` floor `695 = 715 − 20` | **OBSERVATION**, not pre-registered, not load-bearing | this slot | §4.3 |
| B24-02.12 | C45 stays OPEN; C24 and row 1 at `N = 5` close | **RULING** | this slot | §5 |

G14/G14′ labels at the point of use, for this slot: **no external source was read in this slot.**
Nothing was fetched, and §2.4's finding is a statement about the record, not a new reading. The
elementary facts used in §§3–4 (lower semicontinuity of rank, `rank_p <= rank_Q`, Hilbert function
of a complete intersection, extremes of a linear functional on a polytope at its vertices,
Giambelli's determinantal degree in §4.3's observation) are **UNREAD-CLASSICAL**.

---

## 7. Resources, receipts, manifest

**Numerical runs: 1 of 3 wrapped launches.** Wall `0.194 s` of a `300 s` cap; memory cap 512 MiB,
job object enforced, 1 worker, 1 BLAS thread, exit code 0. Started `2026-09-20T03:22:56Z`. Peak
job memory well inside the cap. Tasks 1 and 2 computed nothing and used no launch.

**G19: no unwrapped numerical run of any size.** The single computation ran under
`analysis/b15_bound.py`. Outside it, this slot used `git show`, `sha256sum`, `grep`, `sed`, `ls`
and `find`. **Five interpreter launches were made outside the wrapper.** Each is disclosed here
with its **full text**, per the disclosure standard B23-10 §8 proposes — a standard under which
B23-01 was faulted for not quoting its text, so the texts are given rather than characterised:

    python -c "import flint,sys;print('flint',flint.__version__);print(sys.version)"
    python -c "import json;print(json.load(open('results/logs/b24_02_p1_n5_kleiman_resources.json'))['exit_code'])"
    python -c "import json;d=json.load(open('results/b24_02/MANIFEST.json'));print('slot',d['slot'],'| files',len(d['files']),'| pinned',len(d['pinned_inputs']),'| external',len(d['external_sources']))"
    python -c "import json;d=json.load(open('results/b24_02/p1_n5_kleiman.json'));print('prereg match:',d['preregistration']['match']);print('verdict:',d['decision']['verdict'])"
    python -c "
    import json,hashlib
    d=json.load(open('results/b24_02/MANIFEST.json'))
    bad=[f for f in d['files'] if hashlib.sha256(open(f['path'],'rb').read()).hexdigest()!=f['sha256']]
    print('manifest files:',len(d['files']),'| rehash mismatches:',len(bad))
    print('pinned:',len(d['pinned_inputs']),'| external:',len(d['external_sources']))
    print('report sha256:',[f['sha256'][:16] for f in d['files'] if f['path'].endswith('report.md')][0])
    "

The first is a version probe (flint 0.9.0, Python 3.12.10); the other four are JSON field
inspections and a manifest re-hash of this slot's own outputs (0 mismatches on 7 files). None
computes anything on the objects under study.
**One qualification, stated rather than glossed:** B23-10 §8's proposed sentence exempts an
invocation "which imports nothing beyond the standard library", and the first launch imports
`flint`. It computes nothing — it reads two version strings — but on a strict reading of that
proposed wording it is not automatically exempt, and I record it as a disclosed launch rather
than claim the exemption. The other three import only `json`.

A fifth probe was attempted and **failed to run** on a shell quoting error, so no interpreter was
launched by it; it would have been an `ast.parse` syntax check of the pilot source.

**The batch's one numerical job.** Before launching I checked `..\B15-02\results\logs\b24_04_*.pid`
(absent) and searched every `B15-*` checkout for `b24_05_*.pid` and for any `b24_*.pid` (none
found). The slot was clear to launch and has now spent the job.

**Files written by this slot** (new sibling directory `results/b24_02/`; nothing under any
`b23_*` or earlier results directory was touched, and no sealed packet was edited):

| path | what |
|---|---|
| `docs/b24_02_report.md` | this report |
| `analysis/b24_02_p1_n5_kleiman.py` | pilot 1 |
| `analysis/b24_02_seal.sh` | seal step (hashing and listing only; not a numerical run) |
| `results/b24_02/p1_prereg.md` | pre-registration snapshot, hashed into the pilot output (G25) |
| `results/b24_02/p1_n5_kleiman.json` | pilot 1 output |
| `results/b24_02/MANIFEST.json` | manifest (not self-bound) |
| `results/b24_02/SEAL_LOG.txt` | seal log |
| `results/logs/b24_02_p1_n5_kleiman.pid` | receipt |
| `results/logs/b24_02_p1_n5_kleiman_resources.json` | receipt |

**Receipts.** `results/logs/b24_02_p1_n5_kleiman.pid` is matched by `.gitignore:51`
(`results/logs/*.pid`) and there is no negation for this slot: **negation missing for `b24_02_`**.
The `_resources.json` receipt is not ignored. No `-f` was used and nothing was staged or
committed; this slot is read-only on git as the brief requires.

**Pinned inputs**, bound in `results/b24_02/MANIFEST.json` with full sha256 (short forms here):

| commit | path | sha256 |
|---|---|---|
| `239dd6e8` | `docs/b23_10_review.md` | `8bbc8d9e…` |
| `3bcad666` | `docs/b23_03_report.md` | `0101f224…` |
| `3bcad666` | `results/b23_03/p2_certificates_and_thresholds.json` | (manifest) |
| `ce43cdb7` | `papers/det4-blindness/CLAIMS.md` | `2b7ba688…` |
| `ce43cdb7` | `papers/det4-blindness/GAPS.md` | `6753c9e2…` |
| `feed104e` | `docs/b23_06_report.md` | `a56d2394…` |
| `82633a60` | `docs/s73_report.md` | `f40783ba…` |
| `82633a60` | `docs/lmr_cell.md` | `0ab35e4e…` |
| `82633a60` | `docs/equation_census.md` | `ba7b20f9…` |
| `82633a60` | `docs/s62_report.md`, `docs/s63_report.md` | (manifest) |
| `82633a60` | Astra `REPORT.md` | `c79145e0…` |
| `82633a60` | GKZ `scope_corrigendum/CORRIGENDUM.md` | (manifest) |

`CLAIMS.md` at `2b7ba688…` matches the hash B23-10 §6.1 recorded, and the Astra `REPORT.md` at
`c79145e0…` matches the hash GKZ corrigendum C12 recorded — so in both cases the bytes I read are
the bytes the earlier reviews read.

**External sources: none.** No PDF or HTML was fetched in this slot. **G9′: tool memory is not an
input** — nothing in this report is taken from session memory; every fact is either derived here
in full or quoted from a hashed, pinned file.

**G9/G10.** No pin or receipt was overwritten. **G21–G23** observed: no cell nominated, no gap
claimed, no sealed packet edited.
