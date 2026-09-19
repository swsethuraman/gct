# B23-02 — Row 10: does a determinantal-sheaf containment separate padding?

18 September 2026 (UTC). Slot 02, batch 23 (Phase 2), worktree `work/batch15_workers/B15-02`,
branch `b15-02-a1-probes`. Author: Claude (Opus 5). Theory only. The gate of §1 is decided
without computation, and no pilot is run (§1.6).

**Provenance, recorded before any write (2026-09-18T18:44:45Z):**

```
git rev-parse HEAD           e22a41b1787ff5e8a284433d5d7e0d2a6a2d35b8   (= the starting HEAD in the launch prompt)
git rev-parse HEAD^{tree}    0d1a1cd3724b007cb2a1673a52b06fdbb2f0dcda
git status --porcelain       only the four untracked 2026-09-13 receipts under results/logs/ (pre-existing residue)
```

Read-only git throughout (`git show`, `git rev-parse`, `git status`, `git check-ignore`). No
commit, no push, no stash.

**Notation (G13, G24).** `N` = number of variables (the launch prompt's `L`; the letter `L` is
not used here). `delta_0` is not used. Every dimension is marked **aff** (affine cone) or
**proj** (projective variety or parameter space) at the point of use. `S = C[x_1..x_N]`,
`S_k` its degree-`k` part. `D45` = closure of `{det(sum x_i A_i)}` ⊂ `Sym^4 C^5` (50 aff /
49 proj). `P5 = R135` = closure of `{l·C}` (39 aff). `D35` as in B22-10 §7 (29 aff / 28 proj).
`φ` is the parametrisation `(Mat_4)^5 -> Sym^4`. A *3×4 matrix* always means a `3 × 4`
matrix `B` of linear forms on `C^N`. `Δ_j(B)` (`j = 1..4`) are its signed maximal minors
(cubics), and `I_3(B) = (Δ_1..Δ_4)`.

## 0. What this slot can and cannot establish

**What a positive would have been.** A polynomial `f` in the coefficients of an `N`-ary quartic
(`N = 5..8`), **PROVED** to vanish on the determinant locus, with an exhibited actual-padding
point where it is nonzero, and the value and point in a certificate. That is a
**separation**: the third of the programme's four achievements, not the fourth. It is not a
gap, not a cell and not a multiplicity bound. A sampled vanishing would be MEASURED, never
PROVED.

**What this slot delivers.** The gate's two questions are answered, and the answer closes row 10
by a route the launch prompt did not anticipate:

1. **The hyperplane question (§1.2).** It is decided for every *genuine* member of the Bordiga
   family, that is, every surface cut out by the maximal minors of a 3×4 matrix in the expected
   codimension. No genuine member lies in a hyperplane. More strongly, **a padding point
   contains a genuine member only if it already lies in `D45`** (Proposition 1.1(c), PROVED).
   Genuine members therefore never put a padding point outside `D45` into the containment
   locus. That locus can gain padding points only through non-genuine limit members, and for
   those the question stays **undecided**. §1.5 shows that deciding it cannot change the
   verdict.
2. **The recipe and escape paragraph (§1.3–§1.5).** Proposition 1.1: for a genuine member `S`,
   the quartics containing `S` are exactly the `4 × 4` determinants `det[B; m]` obtained by
   appending a fourth row of linear forms. So the containment condition, on its dense part,
   *is* the parametrisation `φ`. Its escape paragraph survives, and it is empty: the statistic
   is upper-semicontinuous and smaller on padding (§1.1's right-way direction). But it
   escapes the reversal only because it restates the definition of `D45`. Its polynomial form
   is the elimination of `φ`, which is row 11. The one ingredient not already in row 11, an
   elimination over the closure of the Bordiga family instead of over pencils, has no degree
   on record. §1.6 prices it as infeasible: 300 times the memory cap for a single vector at the proved degree floor of 8, and astronomically worse at the conjectured onset.

So **row 10 moves from ASSESSED-kill to PROVED-merge into row 11** for the Bordiga,
Ulrich-sheaf and rational-parametrisation sub-candidates. It becomes a PROVED-kill at `N = 5`
for the non-Cartier-divisor sub-candidate. Row 10 was the last non-rank door that had been
named, and it opens onto the same room as row 11.

**What it does not establish.** It gives no equation and no degree bound beyond the record's.
It does not decide whether padding lies in the boundary contribution `W` (§1.2(b)). It does not
classify `D45 ∩ P5`: that is B23-03's, it is not duplicated, and no argument here needs it.
Nothing about `N = 16`. The rank-threshold kills are cited as PROVED only at `N = 5` and the
stated `N = 16` gradings (B22-10 §6), and are nowhere cited as closed at `N = 6..8`.

## 1. The gate

### 1.1 The structural fact everything rests on

**Proposition 1.1 (PROVED; classical input: Hilbert–Burch, UNREAD-CLASSICAL).** Let `B` be a
3×4 matrix of linear forms on `C^N` (`N >= 4`) with `ht I_3(B) = 2`. Call `S_B := V(I_3(B))`
a *genuine member*. Then:

(a) `I_3(B)` is saturated, unmixed and perfect of grade 2, with minimal resolution
`0 -> S(-4)^3 --B^T--> S(-3)^4 --(Δ_j)--> I_3(B) -> 0`. In particular `I_3(B)` has no linear
or quadratic element: `h^0(I_{S_B}(1)) = h^0(I_{S_B}(2)) = 0`.

(b) `(I_{S_B})_4 = S_1 · I_3(B)_3 = { sum_j m_j Δ_j(B) : m_j in S_1 } = { det[B; m] : m in S_1^{1×4} }`,
where `[B; m]` is the `4 × 4` linear matrix with `B` on top and `m` as its fourth row. Its
dimension is `4N - 3` aff (17 at `N = 5`).

(c) If `S_B ⊆ X_F` scheme-theoretically for a quartic `F`, then `F = det[B; m]` for some `m`.
In particular `F` lies in the `N`-variable determinant locus, and for `N = 5`, **`F ∈ D45`**.

(d) The closure of `{ F : S_B ⊆ X_F for some genuine S_B }` equals the `N`-variable determinant
locus (for `N = 5`, `D45`).

*Proof.* (a) Hilbert–Burch in the Eagon–Northcott form for a `3 × 4` matrix: the complex is
exact exactly when `grade I_3(B) = 2`. Here `grade = ht` (Cohen–Macaulay ring; (T2) of
B20-02, UNREAD-CLASSICAL). A perfect ideal is unmixed, so it has no embedded component at the
irrelevant ideal, so it is saturated. The generators have degree 3 and form a minimal
system, so there is nothing in degrees 1 and 2. (b) An ideal generated in degree 3 has its
degree-4 part equal to `S_1` times its degree-3 part. Laplace expansion along the fourth row
gives `det[B; m] = sum_j ± m_j Δ_j(B)`, and the signs are absorbed in the convention for
`Δ_j`. The dimension is `4N` minus the `3` linear syzygies, which are the rows of `B` by the
resolution. (c) Scheme containment means `F ∈ (I_{S_B})_4`; apply (b). (d) `⊆` is (c) plus
closure. For `⊇`: a generic 4-tuple `(A_1..A_N)` has top-three-row block `B` with
`ht I_3(B) = 2`, which is an open condition, nonempty by the example of a generic linear
section. So a dense subset of `im φ` lies in the set, and closures agree. ∎

*Two readings (G23: one ambient throughout, the space of quartics `Sym^4 C^N`, affine).*
`Z_gen` := the set in (d), whose closure is `D45`. `Z_Σ` := `{ F : S ⊆ X_F for some S in Σbar }`,
where `Σbar` is the closure of the genuine members in the Hilbert scheme. `Z_Σ` is closed: the
incidence is closed, `Σbar` is proper, and projection from a proper factor is closed. We have
`Z_Σ = D45 ∪ W`, where `W` collects quartics containing a boundary member but containing no
genuine one.

### 1.2 Question (i): does the closure of the family contain members inside a hyperplane?

**(a) Genuine members: no, and more than no (PROVED).** By Proposition 1.1(a), a genuine member
has `h^0(I_S(1)) = 0`, so it lies in no hyperplane scheme-theoretically. It can lie in one
*set-theoretically*. The example is the triple structure `V((y_1, y_2)^3)` on a plane, which is
genuine: take `B` a generic `3 × 4` pencil in `y_1, y_2`, whose four minors span all binary
cubics. But that does not put padding in: by Proposition 1.1(c) a padding point `l·C`
containing a genuine member already lies in `D45 ∩ P5`. So genuine members add no padding
point outside `D45` to the containment locus, whatever `D45 ∩ P5` turns out to be.

This accounts for B22-10's second family without needing its classification. The
compression-type points `l·C` (`C` through a plane) are in `D45` and may contain genuine
members. The points outside `D45` contain none. B23-03's classification is not used.

**(b) Boundary members: undecided here.** A flat limit `S_0` of genuine members can acquire
`h^0(I_{S_0}(1)) > 0`, since semicontinuity allows the jump. Whether `Σbar` contains such an
`S_0`, and more to the point whether it contains an `S_0 ⊆ H ∪ Y` for a generic padding
`X_{l·C} = H ∪ Y`, is a question about the boundary of a 36-dimensional (proj, §1.6) component
of the Hilbert scheme. It is not on the record and I did not settle it.

What is known about it:

- The candidate `S_0` must have degree 6.
- Any component of `S_0` inside the smooth cubic `Y` is a Cartier divisor of `Y` (Lefschetz,
  UNREAD-CLASSICAL), so it is a hyperplane or quadric section of `Y`.
- The one degeneration I computed through produces a limit `R ∪ T`: a cubic scroll `R`
  together with a cubic surface `T ⊂ H`. The degeneration is `B_t` with first row `(l, 0, 0, 0)`
  at `t = 0`. Its limit ideal contains `Δ_1'` and `l·I_2(B')`, where `B'` is the lower `2 × 3`
  block. For generic choices `R` spans `P^4`, so it is not in `H`, and it is not a Cartier divisor of `Y`, so it is not in `Y`. `R` is irreducible, so this limit does not lie in `H ∪ Y`.

That is one degeneration, not a proof about all of them. §1.3 explains why the answer to (b),
either way, does not change the gate's outcome.

### 1.3 Question (ii): the recipe

A geometric property is not a construction. The polynomial forms of the containment condition
are these:

- **(R1) From `Z_gen`.** The ideal is `I(closure Z_gen) = I(D45) = ker φ^*` (Proposition 1.1(d);
  B19-02 Lemma 3.1). The elimination is: eliminate `(B, m)` from `F = det[B; m]`. That is
  `φ`, with the pencil read as "three rows plus one". **It is row 11's elimination, not a new
  one.** Its degree is the degree of the first separating element of `I(D45)`: `>= 8` PROVED
  (B22-02 Lemma 1.6, strengthened by B22-10 §7 to `onset I(D35 ∪ {cubics ⊃ plane})`), and
  `> 300` only CONJECTURALLY (onset conjecture).
- **(R2) From `Z_Σ`.** Set up the elimination as follows. Embed `Σbar` in `Gr(4, S_3)` by
  `S ↦ (I_S)_3`, using the Plücker space `Λ^4 C^35` of dimension 52360 at `N = 5`. The incidence
  is `{ (W, F) : W ∈ Σbar, rank[ S_1 ⊗ W | F ] <= 17 }`, the 18-minors of a `70 × 21` matrix
  that is linear in the Plücker coordinates of `W` and in `F`. Then eliminate `W`. The output
  ideal is `I(Z_Σ) ⊆ I(D45)`, because `Z_Σ ⊇ D45`. Two inputs are missing: the equations of
  `Σbar` inside `Gr(4, 35)`, for which no presentation is on record, and a degree bound for the
  elimination. **No degree is on record.** Any separating output has degree at least the
  separating onset of (R1), since it is an element of `I(D45)`.
- **(R3) A thresholded variant.** Let `q(F) := dim{ S ∈ Σbar : S ⊆ X_F }` and
  `Z^{(3)} := { q >= 3 }`. This is closed by upper semicontinuity of fibre dimension for the
  proper incidence projection (UNREAD-CLASSICAL), and `Z^{(3)} ⊇ D45` by §1.4. Its ideal is
  obtained by the same elimination as (R2) plus a fibre-dimension condition, which is strictly
  harder. The output is again inside `I(D45)`.

### 1.4 The escape paragraph, against B22-02 §1.1

**Statistic.** `q(F) = dim{ S ∈ Σbar : S ⊆ X_F }` (proj). It is **upper**-semicontinuous, so
its closed conditions are `{q >= c}`.

**Value on `D45`.** For generic `F = det A ∈ D45`, `q(F) >= 3`: the row-type members (3-row
subspaces of the row space of `A`) form a `P^3`, and the column-type members (via `A^T`) form
another. This is PROVED by Proposition 1.1(b), since each such `F` is `det[B; m]`. Equality is
not claimed; it would need finiteness of determinantal representations, which is not on
record and not used.

**Value on padding.** Genuine members contribute nothing (Proposition 1.1(c)). So `q(l·C*)` is
the dimension of the boundary members inside `X_{l·C*}`, possibly `−∞` (none). It is undecided
(§1.2(b)).

**Direction.** Right-way. §1.1 of B22-02 needs a u.s.c. quantity that is *smaller* on padding,
and `q` is smaller on padding as far as genuine members go. It is the only named non-rank
candidate on the record whose direction is right-way on its dense part.

**Why it escapes, and why the escape is empty.** It escapes for exactly one reason: by
Proposition 1.1(c)–(d), `{q >= 0}` restricted to genuine members *is* membership in `D45`. A
closed condition that restates the definition of `D45` is trivially right-way, since padding is
not in `D45` (B17-01-C). This is the same escape `ker φ^*` has, and it has no more content. The
paragraph survives my reading as a *direction*. It does not survive as a *construction*,
because the construction it names is (R1) = row 11, or (R2)/(R3), which are strictly harder
eliminations whose outputs lie inside `I(D45)`.

### 1.5 Non-coverage, and what does cover it

**Not covered by** Lemmas 1.2–1.6 or Fact 1.7 (B22-02), Theorem 6.4 (B20-02), Astra 8.1–8.3,
or the onset cap. Each is checked against (R1)–(R3):

- **Lemma 1.3.** It needs extraction through `r_det`-minors of a derivative matrix. Here the
  matrix `[S_1 ⊗ W | F]` involves `W`, not only derivatives of `F`, and `W` is eliminated. B22-10
  §5 already records that Lemma 1.3 does not cover source-side kernels.
- **Lemma 1.4.** No `SL_5`-covariant into a determinantal locus is used. The one case where an
  `SL_5`-invariant arises, the rectangular cells of `I(Z_Σ) ⊆ I(D45)`, vanishes on `P5` by
  Lemma 1.4(a).
- **Fact 1.7.** Not a section discriminant.
- **Lemma 1.5.** Not a local differential statistic.
- **Lemmas 1.2 and 1.6.** They constrain any separating polynomial and therefore constrain
  these outputs too (degree `>= 8`), but they kill nothing here.
- **Theorem 6.4 and the cap.** Rank thresholds of Koszul/Macaulay matrices of `F`, which these
  are not.
- **Astra 8.1–8.3.** Source-side tests on `M`; (R1) is coefficient-side.

**Covered by row 11 (B19-02 §§2–7): PROVED.** `I(closure Z_gen) = ker φ^*` exactly
(Proposition 1.1(d)), and `I(Z_Σ), I(Z^{(3)}) ⊆ ker φ^*`. Row 10 is therefore not an
independent mechanism: every polynomial it can produce is an element of `ker φ^*`, the object
of row 11. Its separating elements are exactly the separating elements of `ker φ^*` that also
vanish on `W`. They are never more, and fewer if `W` meets padding.

**Sub-candidates of row 10 named in B22-02:**

| sub-candidate | killing sentence | label |
|---|---|---|
| 10a Bordiga-type containment (3×4-minor surfaces) | Proposition 1.1: on genuine members the quartics containing `S_B` are exactly `det[B; m]`, so the condition is `φ` read as three rows plus one. Its ideal is `ker φ^*` (row 11). The boundary variant (R2) outputs a subset of `ker φ^*` through an elimination with no degree on record | **PROVED-merge into row 11** (Prop. 1.1, Hilbert–Burch UNREAD-CLASSICAL); as a separation recipe, ASSESSED as row 11 is |
| 10b Rank-one ACM/Ulrich sheaf with linear resolution | A sheaf `coker(O(-1)^4 --A--> O^4)` on `X_F` exists iff `F = det A`, i.e. `F ∈ im φ` by definition. Its closure is `D45`, and any moduli compactification adds only a boundary locus, as `Z_Σ` adds `W`. It is the same elimination as 10a with the whole matrix instead of three rows | **PROVED-merge into row 11** |
| 10c Non-Cartier Weil divisor (class group / defect) | For isolated singularities, the extra class is the defect, which the record (`onset_conjecture.md` §0, Dimca at statement level) turns into the degree-7 Milnor jump. Its closed polynomial form is the rank threshold of `M_7`, whose ideal lies in `I(P5)` (GKZ Theorem B, `N = 5`). Padding, being reducible, has a non-Cartier divisor automatically | **PROVED-kill at `N = 5`**; ASSESSED at `N = 6..8` (B22-10 §6 scope) |
| 10d Rational parametrisation `P^3 -> X_F` by the 4×4 minors of a 4×5 linear matrix `N'(v)` | With `N'(v)_{:,i} = A_i v` it is the same tensor `(A_1..A_5)` flattened the other way. `x = Δ(N'(v))` gives `N'(v) x = A(x) v = 0`, so the image lies in `{det A(x) = 0}`, with equality when the kernel map is birational. "`F` is the implicit equation of a minors-parametrised threefold" is membership in `im φ` | **PROVED-merge into row 11** (containment of the image PROVED; birationality for generic `A` is the kernel-map fact of B22-02's non-candidate paragraph, UNREAD-CLASSICAL, used only for "equality") |

### 1.6 Price

**Of a construction: none possible within the defaults.** (R1) is row 11's elimination, which
the record already assesses (B19-02 §6: the counting criterion is silent below 320112 at
`N = 4` and moving away from firing at `N = 5`; certification needs a cell with `a > s`, none
known). (R2)/(R3) additionally need equations of `Σbar ⊂ Gr(4, 35)`, and these are not on
record.

Any linear-algebra search for a separating element at the proved floor, degree 8, ranges over
`dim Sym^8(C^70) = 21,042,084,900` (B19-02 §5 table, `A(8)`; aff dimension of the space of
degree-8 polynomials). At 8 bytes per coefficient that is 1.7 × 10^11 bytes for a single
vector, which is 300 times the 512 MiB cap before any matrix exists. At the conjectured onset
(`> 300`) the space is astronomically larger. Restricting to one five-row isotypic cell (row
11's method) is the only known reduction, and the record prices and assesses it there.

**Of deciding §1.2(b): one theory slot, no pilot.** The boundary of the 36-dimensional (proj)
Bordiga component, restricted to degree-6 schemes inside `H ∪ Y`, is the question. The count
behind "36" is: 60 aff parameters for `B` at `N = 5`, minus the 24-dimensional effective
action of `GL_3 × GL_4`. It relies on Hilbert–Burch uniqueness of `B` up to that action
(UNREAD-CLASSICAL), and it is not load-bearing. I do **not** recommend funding it. Either
answer leaves row 10 inside row 11 (§1.5). A "no" would make `Z_Σ` a closed separating set
whose ideal is inside `ker φ^*` and harder to compute. A "yes" would kill (R2) outright.

**Pilots: 0 of 3.** No computation can make an admissible claim here. Proposition 1.1 is
proved. A pilot on `(I_S)_4` at a sampled `B` would be MEASURED and would add nothing. The
separation question is not a finite computation within the cap. G25 does not arise, since no
pilot means no pre-registration to pin.

## 2–3. The pursuit

None. The gate was decided by Proposition 1.1 before any computation was priced.

## 4. Exact scope and reopening conditions

**Established.**
- Proposition 1.1 (a)–(d) for every `N >= 4`, in particular `N = 5..8`: PROVED, given
  Hilbert–Burch and `grade = ht` (UNREAD-CLASSICAL).
- Genuine members lie in no hyperplane, and a padding point contains one only if it lies in
  `D45`: PROVED.
- Row 10's sub-candidates 10a, 10b and 10d are PROVED-merged into row 11 at every `N`; 10c is
  a PROVED-kill at `N = 5`.
- The escape paragraph for `q` holds as a direction (u.s.c., smaller on padding), and it is
  PROVED to be the direction of `ker φ^*` itself.

**Assessed.** The Σbar-elimination (R2)/(R3) has no recipe beyond elimination, no degree on
record, and is priced infeasible (§1.6). 10c at `N = 6..8`.

**Undecided.** Whether any boundary member of `Σbar` lies in `H ∪ Y` for a generic padding
(§1.2(b)), i.e. whether `W` meets `P5`.

**Not established.** No equation. No separation. No classification of `D45 ∩ P5` (B23-03's).
Nothing at `N = 16`. No closure of rows 1–2 at `N = 6..8`.

**Reopening conditions.** Row 10 reopens only as row 11. It needs either (a) a presentation of
`Σbar` in `Gr(4, S_3)` together with a degree bound for the elimination (R2), shown to be
cheaper than implicitising `φ`, or (b) row 11's own reopening conditions (a cell with `a > s`,
or B19-02's Missing Lemma). The §1.2(b) boundary question matters only under (a).

**Consequence for the programme's list of doors.** After this slot, every named candidate
mechanism for an equation of length 5–8 nonzero on padding is one of three things:

- a rank statistic of a derivative matrix: rows 1–3, 7–9, 10c. These are PROVED-kills at
  `N = 5` and ASSESSED at `N = 6..8`.
- a covariant, invariant or dual-geometric construction: rows 4–6, 11a and 13a, all
  PROVED-kills.
- `ker φ^*` itself, in some presentation: rows 10a/b/d, 11b, 12, 13b.

The last class is the original problem, not a mechanism for it. This is an ASSESSED summary of
the ledger, not a theorem that no other mechanism exists.

## 5. Labelled ledger (all rows producer only, G18)

| # | claim | status |
|---|---|---|
| L1 | Proposition 1.1(a): `I_3(B)` perfect, saturated, no linear or quadratic elements, when `ht = 2` | PROVED given Hilbert–Burch/Eagon–Northcott and `grade = ht` (both UNREAD-CLASSICAL) |
| L2 | Proposition 1.1(b): `(I_{S_B})_4 = { det[B; m] }`, dimension `4N - 3` aff | PROVED |
| L3 | Proposition 1.1(c): `S_B ⊆ X_F` ⇒ `F = det[B; m]` ⇒ `F ∈ D45` (`N = 5`) | PROVED |
| L4 | Proposition 1.1(d): closure of `Z_gen` = `D45`; hence `I = ker φ^*` | PROVED |
| L5 | §1.2(a): no genuine member lies in a hyperplane scheme-theoretically; genuine members add no padding point outside `D45` | PROVED |
| L6 | §1.2(b): whether a boundary member lies in `H ∪ Y` | UNDECIDED (one degeneration computed; it does not) |
| L7 | §1.4: `q(generic D45) >= 3` (proj); `q` is u.s.c.; direction right-way on genuine members | PROVED (lower bound); equality not claimed |
| L8 | §1.5: rows 10a, 10b, 10d merge into row 11; every output lies in `ker φ^*` | PROVED-merge |
| L9 | Row 10c | PROVED-kill at `N = 5` (GKZ Theorem B via the record's defect → Milnor-jump mechanism; Dimca PRIMARY at statement level per B21-10); ASSESSED at `N = 6..8` |
| L10 | (R2)/(R3): no degree on record; infeasible within the defaults (degree-8 search space `2.1 × 10^10` coefficients, B19-02 §5) | ASSESSED / PRICED |
| L11 | `dim Σbar = 36` (proj) | count, not load-bearing (Hilbert–Burch uniqueness UNREAD-CLASSICAL; generic stabiliser not verified) |
| L12 | No equation of length 5–8 nonzero on padding produced; no separation | — |

Literature at the point of use (G14/G14′). Hilbert–Burch / Eagon–Northcott, `grade = ht`,
Lefschetz for divisors on a smooth cubic threefold, and upper semicontinuity of fibre
dimension are all UNREAD-CLASSICAL. Dimca (defect → Milnor jump) is PRIMARY at statement level
per B21-10, used only in row 10c. No specialist text is load-bearing.

## 6. Resources, receipts, manifest

**Numerical runs: none.** Wrapped launches 0 of 3; wall 0 s of 180 s; no unwrapped computation
(G19). Batch one-job check at 18:53Z:

- `..\B15-01\results\logs\b23_01_p1_secondprime.pid` names pid 48188, which is **not live**
  (`Get-Process -Id`).
- No `b23_03_*.pid` exists in any `B15-0*` checkout.
- `Get-Process python*` returned 0.

The session ran only reading, text search, hashing and read-only git.

**Receipts.** None produced. For the record, as a housekeeping item: `.gitignore:51`
(`results/logs/*.pid`) would ignore any `results/logs/b23_02_*.pid`, so there is a
**negation missing for `b23_02_`**. It affects nothing in this slot.

**Inputs read, hashed from the git object store (sha256):**

| input | pin | sha256 |
|---|---|---|
| `docs/b22_02_report.md` | `e22a41b1` | `b41e4265809a018750286d6eda416d62c4f4044b3fdb7cbac2cc51caf50593e4` (= the hash in `results/b22_02/MANIFEST.json`; bytes preserved) |
| `docs/b22_10_review.md` (§§5–10a) | `2efb7aaf` | `86d8caf98a1c088a890bab5d3676ac40c5f9bfdd591c1af95d7a4981073ec092` |
| `docs/b20_02_report.md` | `7de65d7c` | `15ef389b5eb84074e77f2bd88c2dd5e98b14399a394d150b05f2b1b3f2baeda2` |
| `docs/b19_02_report.md` | `7de65d7c` | `52a9e47409acef8294cf79c2795d50ff97432d0a84758abb016ccc5e2dddb62e` |
| `docs/b20_10_review.md` | `6915ae6f` | `021be68f748e8f05e0c8efcd7c50bd58bede1a34b420c2632f3006612fb3a5fa` |
| `docs/b21_10_review.md` | `f7727cb7` | `ce2814c74be173b8569e7c5aec5670a34e2bc2911c90d1fe6426e65a03de28e5` |
| `docs/onset_conjecture.md` | `82633a60` | `e43237da22f4f1f9260a01e5d5fd4bd41828c29aa6cdf0f8b6ac7c282214f49f` |

B20-02b and the Astra report were not re-read in this slot. Their content enters only through
B22-02 and B22-10 as pinned above. No tool memory is an input (G9′).

**New files:** `docs/b23_02_report.md` and `results/b23_02/MANIFEST.json`. Nothing under
`results/b22_02/` or `results/b20_02*/` was touched. Git read-only; no commit.
