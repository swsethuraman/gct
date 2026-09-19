# B23-06 — Map the reachable neighbourhood: which `(m, n)` pairs can this programme enter?

18 September 2026 (UTC). Slot 06, batch 23, worktree `work/batch15_workers/B15-02`, branch
`b15-02-a1-probes`. Author: Claude (Opus 5). Scoping. One wrapped pricing pilot (of two
allowed).

**Provenance, recorded before any write (2026-09-18T21:12:01Z):**

```
git rev-parse HEAD           e22a41b1787ff5e8a284433d5d7e0d2a6a2d35b8   (= the starting HEAD in the launch prompt)
git rev-parse HEAD^{tree}    0d1a1cd3724b007cb2a1673a52b06fdbb2f0dcda
git status --porcelain       ?? docs/b23_02_report.md, ?? results/b23_02/ (B23-02's two uncommitted files),
                             and the four 2026-09-13 receipts under results/logs/
B23-02 files, sha256 at start and at end (untouched):
  docs/b23_02_report.md          664f3e52ee04b00cfe23d1019182804a4ce8825fb590715621efeaf6a478eff9
  results/b23_02/MANIFEST.json   e28c6ec07e10c9bedc1719eb2be98f96bd6ac30b5f27a7de44ee7fe5d6c159b4
```

Read-only git. No commit.

**Notation (G13, G24).**
- `m` is the permanent size and `n` the determinant size. The padded permanent is
  `x_0^{n-m} per_m`. `Det_n := closure(GL_{n^2} · det_n)` and
  `Pad_{n,m} := closure(GL_{n^2} · x_0^{n-m} per_m)`.
- `r` is the length (the number of rows of `λ`). `D_r^{det_n}` is the closure of
  `{det_n(sum_{i<=r} x_i A_i)}` inside `Sym^n C^r`, and `P_r` is the closure of the `r`-variable
  restrictions of `x_0^{n-m} per_m`.
- `N_S(λ)` is the dimension of the `λ`-weight space of `Sym^d(Sym^n C^r)` (the programme's
  cost driver). `a(λ)` is the multiplicity of `S_λ(C^r)` in it.
- The tail of `λ` is `λbar = (λ_2, λ_3, ...)`.
- `dc` is exact determinantal complexity: `f = det` of an affine-linear matrix. `dcbar` is the
  border version: the least `n` with `x_0^{n-m} per_m ∈ Det_n`.
- Every dimension is marked **aff** or **proj**. `delta_0` and the letter `L` are not used.

## 0. What this slot is and is not

**It is** a map with prices on it:
- which `(m, n)` pairs neighbour `(3, 4)`;
- what the length window and degree are at each;
- what one cell costs, in this programme's units;
- which instruments survive the move.

It checks four external facts at primary source, specifies (and prices) a negative control, and
confirms or corrects one integrator extrapolation.

**It is not** an obstruction, an equation, a separation, a gap, a cell nomination, a new
instrument or a batch recommendation. No hunt was started at any `(m, n)`. The board decides.

**The three findings a reader should take away**, each proved or sourced below:

1. **The premise that separation is known at `(3,5)` and `(3,6)` is misreported** (§1). ABV's
   `dc(per_3) = 7` is exact complexity. At the orbit-closure level the published state is
   `5 <= dcbar(per_3) <= 7` (Landsberg, PRIMARY), and determining it is a stated open problem.
   So at `n = 5, 6` it is **not known** whether `x_0^{n-3} per_3` lies in `Det_n`. A separating
   equation there would be a new theorem. The equation also might not exist.
2. **Blindness gets worse with `n` at fixed `m`, and this is exactly the LMR frontier** (§5).
   The second fundamental form of `X_det_n` has rank `2(n-1)`, so it sees nothing in `N <= 2n`
   variables. The padded support has `m^2 + 1` variables. Visible rows exist iff
   `m^2 + 1 > 2n`, i.e. `n <= m^2/2`, which is LMR's theorem. At `m = 3` that means `n <= 4`
   only. `(4, 5)` sits well inside the visible range, where separation is already proved by LMR.
3. **A cell's cost is set by its tail, not its degree** (§2.3, Lemma 2.3). Cheap cells exist at
   every degree: the cheapest five-row cell at `(3,5)`, `d = 5`, has `N_S = 621`, which is
   seconds of work. The *average* cell at the degree where the record's conjecture puts
   separating equations (`d >= cap(5) = 900`) has `N_S ≈ 10^150`. Whether a separating
   equation can sit in a small-tail cell is the unpriced question that decides which price is
   the real one.

## 1. The external facts, verified at source (G14, G14′)

All readings were made in this session by a delegated reader instructed to quote only fetched
text. I re-checked the three load-bearing quotes myself by text search in the fetched
renderings (ABV Cor. 1.4, BIP Thm 1.4, Landsberg §2). The ar5iv renderings do not state which
arXiv version they render. The PDFs were hashed at the stated version, but their text was not
extracted locally, so where it says PRIMARY below, the text read is the HTML rendering of the
hashed version. Files are in the session scratchpad under `lit/` (not in the tree; G9: hash and
reachable URL given).

| fact as the integrator reported it | what the source says | verdict | label |
|---|---|---|---|
| `dc(per_3) = 7`, `dc(per_4) >= 9` (Alper–Bogart–Velasco) | arXiv 1505.02205v1, **Cor. 1.4**: "Let k be a field with char(k)≠2. Then dc(perm_3)=7 and dc(perm_4)≥9." dc is **Def. 1.1**: smallest `m` with `f = det_m(L(x))`, `L` **affine** linear. Thm 1.2: `dc(f) >= codim Sing(f) + 1` when that codim is `> 4`. The paper never mentions border complexity, orbit closures or `closure(GL·det)`. It notes that `f ↦ dc(f)` "is not in general upper semicontinuous". | **CONFIRMED as exact dc. MISREPORTED as a statement about orbit closures.** "At `n <= 6` separation is known" is true for `End · det_n` and **not known** for `Det_n` | PRIMARY (ar5iv; PDF v1 sha256 `e6915a9f6ab7860f…`, https://arxiv.org/pdf/1505.02205v1) |
| — (the missing border fact) | Landsberg, *GCT: an introduction for geometers*, arXiv 1305.7387v3, §2: "it is known ([49] and [30]) that `5 <= dcbar(perm_3) <= dc(perm_3) <= 7`", and **"Problem 2.4. Determine `dcbar(perm_3)`."** No reachable source gives a border lower bound for `per_3` beyond LMR's `m^2/2`, rounded up to 5 | **The governing fact for §2**: `(3,5)` and `(3,6)` are open at the level this programme works at | PRIMARY (ar5iv; PDF v3 sha256 `cdcaaab95e9e4053…`) |
| Grenet: `dc(per_m) <= 2^m − 1` | Grenet, *An upper bound for the permanent versus determinant problem* (manuscript 2011, not on arXiv). Author-page abstract: "…the dimensions of M are at most 2^n–1", over characteristic `≠ 2`. ABV (1.1) cites it as holding in any characteristic | **CONFIRMED** at abstract level; the theorem body is unread | PRIMARY at abstract level only (PDF sha256 `a5254c74d37e061d…`, https://www-verimag.imag.fr/~grenetb/publis/Gre11.pdf, text not extracted); construction UNREAD-SPECIALIST |
| Bürgisser–Ikenmeyer–Panova, hypothesis `n >= m^25` | arXiv 1604.06431v3, **Thm 1.4**: "Let n,d,m be positive integers with `n ≥ m^25` and `λ ⊢ nd`. If λ occurs in `C[Z_{n,m}]`, then λ also occurs in `C[Ω_n]`." Here `Z_{n,m}` is the orbit closure of `X_11^{n−m} per_m` and `Ω_n = closure(GL_{n^2} · det_n)` | **CONFIRMED.** At `m = 3` the hypothesis is `n >= 3^25 ≈ 8.5·10^11`, vacuous at every `n` this programme will touch. The theorem concerns **occurrence**, not multiplicity, so it says nothing about multiplicity obstructions at any `n` | PRIMARY (arxiv.org/html v3; PDF v3 sha256 `b6d54e77f91579b0…`) |
| (context) Mignon–Ressayre `dc(per_m) > m^2/2`; LMR border version | MR, IMRN 2004: abstract via HAL hal-00818200 ("we prove that dc(perm_d) > d^2/2"); exact dc only. LMR arXiv 1004.4802v1, **Thm 1.0.1**: "`dcbar(perm_m) >= m^2/2`", with `dcbar` defined through `closure(GL_{n^2}·[det_n])` | CONFIRMED | MR: PRIMARY at abstract level (no full text reached). LMR: PRIMARY (ar5iv; PDF v1 sha256 `cfc28275a8c6b27f…`) |

**Consequences of §1 for the map.**
- At `m = 3`, orbit-closure separation is PROVED (LMR) for `n <= 4`, OPEN for `n = 5, 6`, and
  **containment holds** for `n >= 7`. Containment at 7 follows from Grenet alone: homogenising
  an affine `7 × 7` expression gives `x_0^4 per_3 ∈ End · det_7 ⊆ Det_7`.
- At `m = 4`, `dcbar(per_4) >= 8` (LMR) makes `(4, 5)`, `(4, 6)` and `(4, 7)` PROVED separations.

## 2. Question A — the remaining room at `m = 3`

### 2.1 The row window

**Upper end `m^2 + 1 = 10`, independent of `n`: CONFIRMED.** `x_0^{n-3} per_3` involves 10
variables, so `Pad_{n,3}` lies in the subspace variety `Sub_10`. The coordinate ring of `Sub_10`
contains `S_λ` only for `ℓ(λ) <= 10` (Cauchy decomposition, UNREAD-CLASSICAL). So every
highest-weight vector of length `> 10` vanishes on padding, whatever `n` is.

**Lower end: 5 at every `n >= 4`, degree-independent, but for a different reason than the
prompt gives.** The prompt's reason ("a generic form there is determinantal") is a statement
about `i_det`. It is degree-dependent: at `n = 5, 6` the locus `D_4^{det_n}` is a proper
subvariety, `2n^2 + 2` aff against `C(n+3,3)`, which is 52 vs 56 and 74 vs 84. So length-4
equations of `Det_n` *do* exist there, at some degree not on record. The right argument for
*separation* is on the padding side:

> **Lemma 2.1 (PROVED; input: every cubic surface is a `3×3` linear determinant up to closure,
> UNREAD-CLASSICAL, used on this record at `sweep62.md` l.175).** For `m = 3` and every
> `n >= 3`, `P_4 ⊆ D_4^{det_n}`, and `P_r ⊆ D_r^{det_n}` for `r <= 3`. Hence no equation of
> length `<= 4` is nonzero on padding, at any degree.
>
> *Proof.* A 4-variable restriction of `x_0^{n-3} per_3` is `l^{n-3} · C` with `C` a quaternary
> cubic. `C` lies in the closure of `{det_3 M}`, and
> `l^{n-3} · det_3 M = det_n diag(l, ..., l, M)`. For `r <= 3` the same argument applies with
> Dickson's theorem (every plane curve is linear determinantal, UNREAD-CLASSICAL). ∎

So **the separating window at `m = 3` is lengths 5–10 at every `n`**.
- At `n = 4` it coincides with the record's window.
- At `n = 5, 6` it is the same window. The length-4 part of `I(Det_n)` is nonempty but cannot
  separate.

### 2.2 The degree

**`cap(n) = 5n(n−1)^2(7n−8)/12`: arithmetic CONFIRMED.** `cap(4) = 300`, `cap(5) = 900`,
`cap(6) = 2125`, `cap(7) = 4305`. The integer division is exact for `n = 2..7`, emitted by the
pilot (C5).

**Scope of the theorem: general `n >= 3`.** Its four steps in `onset_conjecture.md` §2 (at
`82633a60`) are written for arbitrary `n`:
- Step 2: Kleiman transversality, for any `n`.
- Step 3(c): Gulliksen–Negård plus a polynomial identity in `n`, verified symbolically.
- Step 4: Dimca, with an index range `2n − 5 ∈ [0, 4n − 9]` checked for every `n >= 3`.

The record measured it at `n = 3..7`. So `cap(5)` and `cap(6)` are covered, CONDITIONAL on the
same three adopted inputs as `cap(4)`. The theorem concerns **length-5** equations only
(`D_5^{det_n}`). It says nothing about lengths 6–10.

**New here: at `n = 5, 6, 7` the cap minors vanish on padding outright (PROVED, elementary;
no GKZ theorem needed).** For `F = l^e C` with `e = n − 3 >= 2`, every partial derivative
`∂_i F = l^{e-1}(e C ∂_i l + l ∂_i C)` lies in `(l^{e-1})`. So
`rank M_k(F) <= dim S_{k-e+1}`, which at `k = 3n − 5` is `dim S_{2n-1}` in five variables.

| `n` | `dim S_{2n-1} = C(2n+3,4)` | `cap(n) − 1` (rank at generic `D_5^{det_n}`) | cap minors vanish on padding |
|---|---|---|---|
| 5 | 715 | 899 | yes |
| 6 | 1365 | 2124 | yes |
| 7 | 2380 | 4304 | yes |

So the cap construction supplies no separation at `(3,5)` or `(3,6)`. Under the record's
Conjecture 2 (onset of `I(D_5^{det_n})` = `cap(n)`, *expectation* on the record), any
length-5 separating equation at `(3,n)` has degree `>= cap(n)`: 900 at `n = 5`, 2125 at
`n = 6`. That is CONDITIONAL on the conjecture. The proved floor is the restriction lemma's
analogue: `C ↦ f(l^{n-3} C)` is a nonzero equation of `D35`, so `deg f >= onset I(D35) >= 8`
(B22-02 L6, whose proof transfers verbatim through
`l^{n-3} det_3 M = det_n diag(l, ..., l, M)`).

### 2.3 The price of one cell

**Cost driver.** Finding highest-weight vectors is linear algebra on the `λ`-weight space of
`Sym^d(Sym^n C^r)`, of dimension `N_S(λ)`. Evaluating them at a point costs about `N_S · d`
multiplications, which is negligible.

**Calibration on record.**
- B19-02 §8.1: `(4^5)` at `n = 4`, `d = 5`, with `N_S = 19834` and `a = 1`. It took one capped
  process of 19.7 s at 123 MiB.
- `det_onset.md`: the unreduced pipeline's memory wall is at `N_S ≈ 9000` for multi-vector cells.
- `lmr_cell.md`: the LMR cell has `N_S = 1.56·10^11`, out of reach.

So the programme's reach is **`N_S ≲ 2·10^4` per wrapped pilot**.

**Pilot 1** (`b23_06_p1_cellprice`, §8) computed `N_S` and `a` exactly for every five-row cell
at `d = 5`. All three rows pass controls C0 and C4. The `(4, 5, 5)` row additionally
reproduces the record: `N_S((4^5)) = 19834`, `a = 1`, and 23 five-row cells (C1–C3). Checks
passed 11/11.

| `(n, r, d)` | five-row cells with `a > 0` | non-rect `N_S` min / median / max | cheapest non-rectangular cell | cells with `N_S <= 2·10^4` |
|---|---|---|---|---|
| (4,5,5) — `(3,4)` control | 23 | 553 / 1860 / 11640 | `(12,2,2,2,2)`, `N_S = 553`, `a = 1` | 23 of 23 |
| (5,5,5) — `(3,5)` and `(4,5)` | 94 | 621 / 10075 / 92680 | `(17,2,2,2,2)`, `N_S = 621`, `a = 1` | 67 of 94 |
| (6,5,5) — `(3,6)` | 234 | 641 / 45271 / 1037971 | `(22,2,2,2,2)`, `N_S = 641`, `a = 1` | 78 of 234 |

(At `(5,5,5)` there is no rectangle: `(5^5)` has `a = 0`. At `(6,5,5)` the rectangle `(6^5)`
has `N_S = 1,398,547`.)

**Price of the cheapest cell in the window, `(3,5)` at `(17, 2^4)`, `d = 5`.** Well under one
wrapped pilot:
- a highest-weight vector on a 621-dimensional weight space, seconds by the B19-02 calibration;
- `mult_det`: exact if one evaluation at a `D_5^{det_5}` point is nonzero (`a = 1`);
- `mult_pad`: a floor from one evaluation at an actual padded point `l^2 · C` with a frame
  certificate (B17-01 style). It is exact only against a ceiling. The Pieri ceiling here is
  that `mult_pad > 0` needs `λ_1 >= (n−3)d = 10` (§2.4), which this cell meets, so the ceiling
  is not zero. It would have to come from the full `C[P_5]` decomposition, which is not on
  record.

In programme units that is one pilot, `<= 20 s`, `<= 150 MiB`, two to four evaluations.

**Cheap is not informative.** Under Conjecture 2 every length-5 cell below `cap(5) = 900` has
`i_det = 0`, so a separating equation cannot be there. At degree `>= 900` the *average* weight
space is `10^150.4` (pilot, `log10` of `dim Sym^900(Sym^5 C^5)` divided by the number of
weights; `10^289.0` at `(6, 5, 2125)`; `10^65.0` at `(4, 5, 300)`). But averages are not the
whole story:

> **Lemma 2.3 (PROVED, elementary).** For `λ = (nd − t, λbar)` with the tail `λbar ⊢ t` held
> fixed, `N_S(λ)` is nondecreasing in `d` and constant for `d >= t`.
>
> *Proof.* Every exponent vector other than `n e_1` contributes at least 1 to the tail. So a
> multiset of weight `λ` has at most `t` such vectors and the rest equal `n e_1`. `N_S` counts
> the multisets of at most `min(d, t)` non-`n e_1` vectors with tail sum `λbar`; their first
> coordinates are then forced. ∎

So **cells with small tails are cheap at every degree, including 900 and 2125**. The real
price of `(3,5)` turns on a question nobody has asked: **can a separating equation at `(3,n)`
lie in a cell with small tail?** The padding side allows it; the Pieri condition bounds the
tail *above* by `3d`, not below. Nothing on record bounds it below. Until someone does, the
honest price is "one pilot per cell if the answer is small tails; astronomically out of reach
if it is typical tails". Deciding it is a theory question, **unpriced**, and a prerequisite of
any hunt at `(3,5)`. For reference, the one theorem-guaranteed nonzero cell at `(3,4)`, the LMR
cell, has tail 31 and `N_S = 1.56·10^11`.

**Lengths 6–10 at `(3,5)`, `(3,6)`.**
- No cap theorem. LMR is blind there (§5). Nothing is on record.
- The average weight space at `d = r = 6` is `10^6.07` (`n = 5`) and `10^7.27` (`n = 6`).
- The minimum was not computed: the pilot's dense method needs `(5k+1)^6` layers, 887M entries
  at `k = 6`, which is beyond the cap. By Lemma 2.3, small-tail cells are cheap there too.

### 2.4 Two further scoping facts at `(3,5)`

- **Pieri ceiling (PROVED, UNREAD-CLASSICAL Pieri).** Functions on the cone of products
  `l^{n-3} C` in degree `d` lie in `Sym^{(n-3)d}(V) ⊗ Sym^d(Sym^3 V)`. So `S_λ` occurs only if
  `λ` contains a horizontal strip of `(n−3)d` boxes, which forces `λ_1 >= (n−3)d`. That gives
  `λ_1 >= d` at `n = 4`, `2d` at `n = 5` and `3d` at `n = 6`. Cells with shorter first rows
  cannot separate.
- **B17-01's non-containment method does not transfer (ASSESSED).** B17-01 proved
  `l·C* ∉ D45` by specialising ruledness: the generic member is rational via the kernel map,
  and the special member `l·C*` is reduced with a non-ruled component. At `(3,5)` the analogous
  statement `l^2 · C* ∉ D_5^{det_5}` would itself **prove `dcbar(per_3) >= 6`**, since
  restrictions of `Det_5` lie in `D_5^{det_5}`. But both of the method's hypotheses fail:
  - `l^2 C*` is **non-reduced**, which breaks the `R1` step;
  - for a `5 × 5` pencil in five variables the kernel map is square. It relates `X_F` to another
    determinantal quintic threefold, not to `P^3`, and rationality of the generic member is not
    on record.

  The statement is open. It is the cheapest-to-state first question at `(3,5)` and is priced
  here as one theory slot, outcome uncertain. **It is not a nomination.**

## 3. Question B — the next rung, `(m, n) = (4, 5)`

**Ambient dimensions: CONFIRMED** (pilot C5). `dim Sym^4 C^16 = C(19,4) = 3876` aff (3875 proj).
`dim Sym^5 C^25 = C(29,5) = 118755` aff (118754 proj). But the ambient is not the cost driver:
by the length reduction (`isotypic_rank.md` Prop. 5 / Thm 6′; B17-03 Lemma 2, 03-A), a
length-`r` cell is computed in `r` variables. Its cost is `N_S` of `Sym^d(Sym^5 C^r)`, not
anything in `C^{25}`.

**Row window.**
- **Upper end `m^2 + 1 = 17`: CONFIRMED** (subspace variety, as in §2.1).
- **Lower end: 4 or 5, UNDECIDED.** Length `<= 3` is empty by Dickson. At length 4, `P_4` is the
  closure of `{l · Q}` with `Q` a quaternary quartic (restriction dominance for `per_4` is not
  on record). Generic quartic surfaces are **not** `4 × 4` determinantal (`D44` is a
  hypersurface; LLV, CONDITIONAL on record), so the block-diagonal argument of Lemma 2.1 fails.
  Whether `l · Q* ∈ D_4^{det_5}` by another representation (compare B22-10's compression
  family) is open. The dimensions are `{l·Q}` 38 aff and `D_4^{det_5}` 52 aff in 56.

**Degree.** `cap(5) = 900` applies unchanged. The determinant side of `(4,5)` *is* the
determinant side of `(3,5)`, so every length-5 cell of `(4,5)` is the same object as in
§2.3's `(5,5,5)` row. Only the padding side differs: `l · Q` against `l^2 · C`. The elementary
`(l)`-argument of §2.2 does **not** apply (`e = 1`). Whether the cap minors vanish on `l·Q`
needs a `d_1` rank comparison of the Theorem B type at `n = 5`, which is not on record.

**Price of one cell.** At length 5 and `d = 5`: identical to §2.3, at `N_S = 621` for the
cheapest cell. At the top of the window the situation differs in kind. The second fundamental
form sees `N > 2n = 10` (§5), so rows 11–17 are *visible*. LMR (Thm 1.0.1, PRIMARY) gives
`dcbar(per_4) >= 8 > 5`: **the separation at `(4,5)` is already proved, by the dual-variety
equations**, which live at lengths `>= 11`. The LMR-type cell at `n = 4` needed
`N_S = 1.56·10^11`. At `n = 5` it is at least as large in length, and its size was not computed.

**Judgement: enterable at small degree; nothing specific breaks that was not already broken at
`(3,4)`; and the rung answers a different question.**
- **The multiplicity computation.** It works for cells with `N_S ≲ 2·10^4` (67 of the 94
  five-row cells at `d = 5`, pilot). It breaks where it already broke at `(3,4)`: typical cells
  at the informative degree, and the LMR-type cells.
- **The counting criterion.** It was already silent at `(3,4)` (B19-02 §6). At `(4,5)` it would
  need the 5-Kronecker semi-invariants at dimension vector `(5,5)`. That is not computed and not
  expected to fire any earlier.
- **Runner, carrier, arc.** Each is written for `4 × 4` matrices: the `Z^4 × Z^4` gradings, the
  B18-02 carrier on tuples of `4 × 4` matrices, and the B20-01 arc and Astra's block
  decomposition. Each would need re-derivation for `5 × 5`. I did not read them line by line,
  so this is ASSESSED, not a proof that they break.
- **The real difference.** At `(3,4)` the programme hunts short equations (lengths 5–8) where
  LMR is blind, in a pair LMR already separates at length 9. At `(4,5)` the blind part of the
  window is lengths 5–10 out of 5–17. The question "find a short separating equation" is the
  same kind of question, and still open. The *separation* is not in doubt. This rung
  therefore offers a second instance of the programme's existing question, not a new one.

## 4. Question C — the negative control at `(3,7)`

**Premise (§1).** `x_0^4 per_3 ∈ End · det_7 ⊆ Det_7` from Grenet's `2^3 − 1 = 7`. It is
independent of ABV. It is PRIMARY only at abstract level: Grenet's construction is unread, and
ABV and Landsberg cite it. Consequently `C[Pad_{7,3}]` is a quotient of `C[Det_7]`, so
`mult_pad(λ) <= mult_det(λ)` for every `λ`, and every equation of `Det_7` vanishes on padding.
**Any instrument output at `(3,7)` claiming `mult_pad > mult_det`, or an equation of `Det_7`
nonzero on padding, is a false positive.**

**Judgement: no instrument on the record can be meaningfully pointed at `(3,7)` at reachable
cost.** A control is informative only where the instrument *could* fail. At `(3,7)` every
instrument is in one of three states:

| instrument | state at `(3,7)` |
|---|---|
| Rank thresholds of `d_1` (cap minors; `N = 5`) | Passes by the `(l^3)`-argument of §2.2 (`J(l^4 C) ⊆ (l^3)`) before any code runs. Nothing is tested |
| Classical equations (second-fundamental-form/LMR; catalecticants) | Live at lengths `>= 2n + 1 = 15` (second fundamental form), `>= 30` (`k = 2` catalecticant) and `>= 19` (`k = 3`) (§5). All exceed the padded support of 10, so they vanish on padding by the subspace-variety lemma. Passes vacuously |
| B19-02 Theorem 7.1 certification (evaluation rank vs `min(a, s)`) | Certifies a nonzero `I(Det_7)`-part only in a cell with `a > s` or at the certified-rank ceiling with `i_det >= 1`. The only length-`<= 10` cells with a *known* `i_det >= 1` are the `cap(7) = 4305` Jacobian-minor cells (length 5), whose weight spaces were not computed. The rest is unknown. With no certified equation, there is nothing to evaluate at the padded point |

**Specification, for the day an instrument outputs anything at `(3,7)`.**
- *Premise check:* take Grenet's explicit `7 × 7` matrix `A_G`, homogenise it, and verify the
  polynomial identity `det_7(A_G^h(x_0, y)) = x_0^4 per_3(y)` exactly. This is a degree-7
  identity in 10 variables. Price: seconds, well inside one pilot. It needs Grenet's
  construction read first (UNREAD).
- *Control:* for any polynomial `h` certified (Thm 7.1, `rank E` equal to the ceiling) to lie in
  `I(D_r^{det_7})`, `r <= 10`, the instrument must return `h(P_Grenet) = 0` exactly. Here
  `P_Grenet` is the `r`-variable restriction of `x_0^4 per_3` through a certified frame.
- *False positive:* a nonzero exact value at `P_Grenet`. Since `P_Grenet` is by construction a
  point of `D_r^{det_7}`, a nonzero value means that either the certification or the evaluation
  (coordinates, normalisation, frame) is wrong. B21-10's O1 was of the second kind.
- *Price once an `h` exists:* one evaluation, negligible.

Until then the control has nothing to act on. That is the answer the next board should hear:
**the programme has no instrument that produces a certified equation of `Det_n` in the padded
support at any `n >= 5`**, so a negative control cannot yet be run. The positive control
(`n = 3`, LMR weight `(19,7,2^5)`) remains the only calibration available.

## 5. Question D — the integrator's extrapolation

**Second fundamental form: CONFIRMED.** At `A = diag(1, ..., 1, 0)`,
`det(A + B) = b_nn + sum_{i<n}(b_ii b_nn − b_in b_ni) + O(B^3)`. The tangent hyperplane is
`b_nn = 0`, and on it the quadratic part is `−sum_{i<n} b_in b_ni`: **rank `2(n−1)`**. This is
consistent with `dim X_det_n^vee = dim(P^{n-1} × P^{n-1}) = 2n − 2`. For `F = det_n ∘ Λ` in
`N` variables the space `T_x X_F / <x>` has dimension `N − 2`, so the bound is **vacuous iff
`N <= 2n`**. PROVED (the same argument as B22-02 L5(i), with `n` general).

**Catalecticant: the arithmetic is right, the label is not.** The `k`-th partials of `det_n` are
the `C(n,k)^2` complementary `(n−k)`-minors, with disjoint supports, so
`rank Cat_{k,n−k}(det_n) = C(n,k)^2`. The integrator's `(n(n−1)/2)^2` is the `k = 2` value. It
is the *middle* catalecticant only for `n = 4, 5`. For `n >= 6` the middle is `k = ⌊n/2⌋`:

| `n` | `k = 2` rank `C(n,2)^2` | vacuous (`k = 2`) iff `C(N+1,2) <= C(n,2)^2` | middle `k`, rank | vacuous (middle) iff `C(N+k−1,k) <= rank` |
|---|---|---|---|---|
| 4 | 36 | `N <= 8` (B22-02 L5(ii)) | `k = 2`, 36 | `N <= 8` |
| 5 | 100 | `N <= 13` | `k = 2`, 100 | `N <= 13` |
| 6 | 225 | `N <= 20` | `k = 3`, 400 | `N <= 12` |
| 7 | 441 | `N <= 29` | `k = 3`, 1225 | `N <= 18` |

(Ranks emitted by the pilot. The thresholds are exact integer arithmetic, done by hand from
those ranks.) The catalecticants are **reversed** statistics: padding has the smaller rank
(B22-02 L5(ii)). Their vacuity range is not what blinds the programme; the second fundamental
form's is.

**The consequence: CONFIRMED, and sharper than stated.**
- The second fundamental form sees padding only in the rows `2n + 1 .. m^2 + 1` of the padded
  support, which is nonempty iff `m^2 + 1 > 2n`, i.e. **`n <= m^2/2`**.
- That is exactly the LMR range `dcbar(per_m) >= m^2/2`. At `m = 3`:
  - `n = 4`: rows 9–10 are visible, which is the LMR cell at length 9 (`lmr_cell.md`).
  - `n = 5, 6, 7`: the whole support (`<= 10`) lies inside the blind zone (`<= 10, 12, 14`).

**So the blindness gets worse with `n` at fixed `m`: this sentence is PROVED and belongs in
Paper 3.** The companion sentence belongs next to it. Along the minimal-padding ladder
`(m, m+1)`, the visible part is rows `2m + 3 .. m^2 + 1`, which grows like `m^2`: 7 rows at
`(4,5)`, 14 at `(5,6)`. So "go bigger in `n`" makes the programme blinder, and "go up the
ladder" does not. Neither gives the programme's short-length instruments anything to see.

## 6. Exact scope — what a reader may and may not conclude

**May conclude:**
- The four external facts are as quoted, but the "known separation at `n <= 6`" is exact-dc
  only. At the orbit-closure level `(3,5)` and `(3,6)` are open (`5 <= dcbar(per_3) <= 7`).
- The separating window at `m = 3` is lengths 5–10 at every `n >= 4` (Lemma 2.1).
- The cap theorem covers `n = 5, 6` (conditional as recorded), and its minors vanish on padding
  there by an elementary argument.
- Cell cost depends on the tail, not the degree (Lemma 2.3). The cheapest `d = 5` cells cost
  seconds. The average cell at the conjectured separating degree is `10^150` (`n = 5`).
- `(4,5)` is a proved separation (LMR) and a second instance of the short-length question.
- No negative control can run until some instrument certifies an equation in the padded support.
- The second-fundamental-form blind zone is `N <= 2n`, which reproduces the LMR frontier.

**May not conclude:**
- that any pair is a good investment (no recommendation is made);
- that separating equations at `(3,5)` exist (open), or lie in large-tail cells (open), or in
  small-tail ones (open);
- that runner, carrier or arc break at `(4,5)` (ASSESSED only);
- anything about multiplicity obstructions at `n < m^25` from BIP (which is about occurrence);
- that `l^2 C* ∉ D_5^{det_5}` (open; it would prove `dcbar(per_3) >= 6`).

**Unpriced prerequisites named:**
1. A lower bound on the tail of any separating equation at `(3,n)`.
2. Whether `l^2 C* ∈ D_5^{det_5}` (one theory slot, outcome uncertain).
3. The lower end of the `(4,5)` window (`l · Q* ∈ D_4^{det_5}`?).
4. Reading Grenet's construction, the premise of any `(3,7)` control.

## 7. Labelled ledger (all rows producer only, G18)

| # | claim | status |
|---|---|---|
| L1 | ABV Cor. 1.4 (`dc(per_3) = 7`, `dc(per_4) >= 9`), exact affine dc, char `≠ 2` | PRIMARY (ar5iv; PDF v1 hashed); integrator's "separation known at `n <= 6`" **MISREPORTED** at the orbit-closure level |
| L2 | `5 <= dcbar(per_3) <= 7`; "determine `dcbar(per_3)`" is open | PRIMARY (Landsberg 1305.7387v3 §2, Problem 2.4) |
| L3 | Grenet `dc(per_m) <= 2^m − 1` | PRIMARY at abstract level; construction UNREAD-SPECIALIST |
| L4 | BIP Thm 1.4, `n >= m^25`, occurrence only | PRIMARY |
| L5 | LMR Thm 1.0.1 `dcbar(per_m) >= m^2/2`; MR `dc > m^2/2` | LMR PRIMARY; MR PRIMARY at abstract level |
| L6 | Upper end of window `m^2 + 1`, independent of `n` | PROVED given the Cauchy/subspace-variety decomposition (UNREAD-CLASSICAL) |
| L7 | Lemma 2.1: lower end 5 at `m = 3`, every `n >= 4`, degree-independent | PROVED (cubic surfaces determinantal; Dickson: UNREAD-CLASSICAL) |
| L8 | `cap(5) = 900`, `cap(6) = 2125`; the theorem's proof is general in `n` | arithmetic CERTIFIED (pilot C5); theorem ADOPTED as on record (Kleiman, Dimca, Gulliksen–Negård) |
| L9 | Cap minors vanish on `l^{n−3}C` at `n = 5, 6, 7` | PROVED (elementary rank bound, table §2.2) |
| L10 | `deg f >= onset I(D35) >= 8` for separating `f` at `(3,n)` | PROVED (B22-02 L6 transferred); `>= 8` ADOPTED record-internal |
| L11 | `N_S`, `a` and cell counts at `(4,5,5)`, `(5,5,5)`, `(6,5,5)`; controls C0–C5 | CERTIFIED (exact integer DP; 11/11 checks; `results/b23_06/p1_cellprice.json`) |
| L12 | `log10` average weight-space dimensions (`10^150.4` at `(5,5,900)`, etc.) | CERTIFIED arithmetic (pilot); an average, not a cell |
| L13 | Lemma 2.3: `N_S` depends on the tail, constant in `d >= t` | PROVED |
| L14 | Pieri ceiling `λ_1 >= (n−3)d` for `mult_pad > 0` | PROVED (Pieri, UNREAD-CLASSICAL) |
| L15 | B17-01's method does not transfer to `(3,5)`; `l^2 C* ∉ D_5^{det_5}` would imply `dcbar(per_3) >= 6` | implication PROVED; non-transfer ASSESSED |
| L16 | `(4,5)`: window upper end 17; lower end undecided; separation PROVED by LMR; runner/carrier/arc need re-derivation | 17 PROVED; lower end UNDECIDED; LMR PRIMARY; re-derivation ASSESSED (not read line by line) |
| L17 | No instrument on record can run a meaningful negative control at `(3,7)`; the control specified for when one can | ASSESSED; specification complete |
| L18 | Second fundamental form rank `2(n−1)`; blind iff `N <= 2n`; visible rows iff `n <= m^2/2` | PROVED |
| L19 | Catalecticant ranks `C(n,k)^2`; the integrator's `(n(n−1)/2)^2` is `k = 2`, the middle one only for `n <= 5` | PROVED (ranks certified by pilot); integrator **CORRECTED** in label, **CONFIRMED** in arithmetic |
| L20 | No obstruction, equation, cell nomination, instrument or recommendation | — |

## 8. Resources, receipts, manifest

**Literature reading.** A delegated reader in this session fetched arXiv, ar5iv, HAL and
author pages (network access, `curl`, `sha256sum`; no computation) into the session
scratchpad `lit/`. I re-verified the three load-bearing quotes by text search. The PDF hashes
match the reader's report:

- ABV `e6915a9f…`
- BIP `b6d54e77…`
- LMR `cfc28275…`
- Landsberg `cdcaaab9…`
- Grenet `a5254c74…`

**Pilot 1 — `b23_06_p1_cellprice`** (wrapped, `analysis/b15_bound.py --seconds 60 --memory-mb 512
--slot 02`, `.venv/python.exe`, `PYTHONDONTWRITEBYTECODE=1`, one BLAS thread).

- Pre-registration `results/b23_06/PREREG.md`, sha256
  `9082b7cc9b3a6b3e72edca61c3a4ab118504204ad8776510951411f893e8d6e9`, written before the launch
  and recorded as `prereg_sha256` inside the pilot's JSON (G25).
- Script `analysis/b23_06_p1_cellprice.py`, sha256
  `3629a4cfe5dca349464a0dc1294ea9b3a81a4b659432558d227f4c6e616bd2e1`.
- Before launch (21:19Z): `b23_01_p1_secondprime.pid` names pid 48188, which was not live; no
  `b23_03_*.pid` existed in any `B15-0*` checkout; `Get-Process python*` returned 0.

| run | started (UTC) | wall | peak job memory | exit | checks | outputs |
|---|---|---|---|---|---|---|
| `b23_06_p1_cellprice` | 21:19:53 | 4.59 s | 186.9 MB | 0 | 11/11 (emitted) | `results/b23_06/p1_cellprice.json`, `p1_console.log`; receipts `results/logs/b23_06_p1_cellprice.pid`, `_resources.json` |

Wrapped launches: 1 of 2. Wall 4.6 s. No unwrapped computation (G19). The prices in §2.3 and
§5 that are not in the pilot are hand arithmetic on emitted numbers.

**Receipts.** `git check-ignore -v` reports `.gitignore:51:results/logs/*.pid` for
`results/logs/b23_06_p1_cellprice.pid`: **negation missing for `b23_06_`**. The
`_resources.json` receipt is not ignored.

**Manifest.** `results/b23_06/MANIFEST.json`, holding the sha256 of:
- this report, the pre-registration, the script, the pilot JSON and console log, and the two
  receipts;
- the git-pinned inputs read;
- the literature PDFs.

New files of this slot:
- `docs/b23_06_report.md`
- `analysis/b23_06_p1_cellprice.py`
- `results/b23_06/`
- `results/logs/b23_06_p1_cellprice.{pid,_resources.json}`

B23-02's two files were not touched (hashes above, unchanged at the end). Git read-only; no
commit.
