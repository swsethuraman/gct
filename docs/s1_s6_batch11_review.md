# Batch 11, Sol side — independent review of S1–S6

The report is `docs/sol/sol_batch11_report.md`, committed unedited.  Everything
below was checked here with the repository's own code before being believed.
Labels: **confirmed** (I reproduced it), **corrected** (I found it wrong or
incomplete), **relayed** (I could not check it), **new** (measured here, not in
the report).

---

## 0. Verdict

> **S5 is the session that matters, and it is better than its own report
> claims.**  The one-block recursion is correct — I checked the group theory and
> the Pieri branching — and its economics are not merely acceptable, they are
> the first realisation of `M_λ` in the programme's history that is small.  The
> precursor at the control rung is **31-dimensional** against a native carrier
> of `5.10×10⁶`, and the whole memoised recursion from the LMR cell down to
> `δ = 1` touches **7 656 distinct shapes, peaking at 585 per level**.  That is
> the answer to the diagnosis the batch opened with.
>
> **S4's theorem is true but its enumeration was incomplete.**  There is an
> eleventh weight-13 block with `a_∞ ≤ 3` that the session did not test:
> `ρ = (5,3,3,2)`, with `a_∞ = 1`.  I ran it here and it is dead, so the
> statement stands — but it stood on ten blocks out of eleven until now.
>
> S1, S2, S3 and S6 are sound.  S2's closures are correct and structural.  S6's
> exact-image-versus-closure correction independently reaches the same
> conclusion the batch-10 housekeeping reached from the geometry side, which is
> worth something on its own.

---

## 1. Confirmed

**All ten stable multiplicities, recomputed here** with
`analysis/wk9_s57_stable.py:a_inf` (Kostant alternation, two primes, CRT):

| `ρ` | S4's `a_∞` | mine |
|---|---|---|
| `(11,1,1)` | 2 | 2 |
| `(9,2,1,1)` | 2 | 2 |
| `(6,3,2,1,1)` | 2 | 2 |
| `(5,4,2,1,1)` | 2 | 2 |
| `(4,3,2,2,2)` | 2 | 2 |
| `(5,5,3)` | 3 | 3 |
| `(4,4,2,2,1)` | 3 | 3 |
| `(7,2,2,1,1)` | 1 | 1 |
| `(5,5,1,1,1)` | 1 | 1 |
| `(5,3,3,1,1)` | 1 | 1 |

Ten of ten.  **And the `a_∞ = 2` and `a_∞ = 3` rows are complete**: enumerating
all 57 partitions of 13 into at most five parts and computing `a_∞` for each
gives exactly five with `a_∞ = 2` and exactly two with `a_∞ = 3`, and they are
S4's.  The `a_∞ = 1` row is not complete — see §2.

**S5's Pieri channel counts, and the exact predecessor list.**  Enumerating
horizontal 4-strips removable from `λ_δ = (4δ−31, 17, 2⁷)`
(`analysis/wk11_int_bdelta.py:horiz_strips`): **3 channels at `δ = 12`** — the
first-row coincidence `λ₁ = λ₂ = 17` is indeed what collapses it — and **12 at
every other rung tested**, `δ = 13, 14, 16, 18, 24`.  My twelve shapes at
`δ = 24` are S5's twelve, one for one.

**S5's recursion itself.**  Not a numerical check but a structural one, and it
holds.  `H_δ = S_4 ≀ S_δ = (S_4)^δ ⋊ S_δ` and `K_δ = H_{δ−1} × S_4 = (S_4)^δ ⋊
S_{δ−1}`; adjoining one adjacent block transposition generates `S_δ` from
`S_{δ−1}`, so `K_δ` and `τ` generate `H_δ` and
`M_{λ_δ} = ker(τ − I)` on `(S^{λ_δ})^{K_δ}` is exact.  The precursor
decomposition is Pieri: restricting `S^λ` to `S_{4δ−4} × S_4` and taking
`S_4`-invariants keeps only the `ν = (4)` component, and `c^λ_{μ,(4)} = 1`
exactly when `λ/μ` is a horizontal 4-strip.  **The construction is correct.**

**S1's arithmetic.**  `deg Disc = r(d−1)^{r−1} = 5·3⁴ = 405`; `rank Cat_2(det_4)
= C(4,2)² = 36` against `dim Sym²C⁹ = 45`, so the first nontrivial minor is
`37 × 37` and the coefficient degree 37 is thirteen worse than LMR; and the LMR
degree `(k+2)(d−1)` with `k = 2n−2`, `d = n` gives `2n(n−1) = 24` at `n = 4`.
That last one is a pleasing cross-check: it *derives* the family degree formula
`δ_n = 2n(n−1)` that S6 found empirically in batch 10.

**S2's closed routes.**  `ψ²(s_{(1)}) = p_2 = s_{(2)} − s_{(1,1)}` is standard and is
enough on its own: Adams doubling is not a positive map `[λ] → [2λ]`, so it
cannot be `R_2`.  The block-diagonal map gives
`det_{2n}(diag(A,B)) = det_n(A)det_n(B)`, which lands on a power variety — also
correct, and the right reason.  I did not check the wreath deflation argument in
detail; it is **relayed**, but the direction claim (canonical maps go large to
small) is standard.

---

## 2. Corrected — an eleventh weight-13 block, and it was never tested

S4 states

> `|ρ| = 13` and `a_∞(ρ) ≤ 3` ⟹ `i_det^∞(ρ) = 0`

on the strength of three `a_∞ = 1` tails from batch 10 plus seven new ones.
**There are four `a_∞ = 1` tails at weight 13, not three.**  The enumeration
above gives

    a_∞ = 1 :  (7,2,2,1,1)   (5,5,1,1,1)   (5,3,3,2)   (5,3,3,1,1)

and `(5,3,3,2)` appears in no session, in either batch.  It is not exotic — four
parts instead of five, and it sits between two tails that were tested.

**Run here, with the batch-10 instrument** (`analysis/wk10_int_stable_hwv.py`
then `wk10_int_stable_subst.py`):

    ρ = (5,3,3,2,0)
    raw weight space 3246;  a_∞ = dim ker = 1  (26.5 s);  HWV support 680 of 3246
    substituted polynomial at three random M_6 pencils: all three nonzero
    highest-weight check (invariance under A_{i+1} → A_{i+1} + ε A_i,
      all four raisings, three ε values): PASS

One nonzero point certifies it exactly, so **`i_det^∞((5,3,3,2)) = 0`** and the
block is dead.  **S4's theorem now holds as stated**, on eleven blocks rather
than ten.

The covariance check is the one that caught S1's normalisation error in batch 10
and it is the reason this result can be trusted: a non-highest-weight vector
evaluates nonzero generically, so without it a wrong convention produces an
unfalsifiable negative.

**A smaller count correction.**  The record has said "47 weight-13 shapes" since
batch 10.  I get 57 partitions of 13 into at most five parts, of which 11 have
`a_∞ = 0`, leaving **46** with a nonempty stable block.  The difference is one
and I have not chased it; whoever next quotes the number should recount rather
than inherit it.

---

## 3. New — the economics of S5, including the number S5 did not name

S5 nominates `B_δ = Σ_{λ_δ/μ horiz 4-strip} a_{δ−1}(μ)` as the decisive number
and asks for it before any coding.  Computed here with the repository's own
census alternation (`analysis/wk11_int_bdelta.py`, independent of anything S5
ran):

    δ = 12:   a = 2,  3 channels,  B = 31      (a_11 = 12, 11, 8)

against a native carrier of `n_χ(12) ≈ 5.10×10⁶` at the same rung.  **A factor
of 165 000.**  Higher rungs are in flight and are recorded in
`results/wk11_int_bdelta.json` as they land.

**But `B_δ` measures one level, and an implementation is recursive.**  Each
predecessor multiplicity space must itself be built before the level above it
can be formed, so what an implementation actually pays is the size of the
memoised DAG of distinct `(shape, δ)` pairs reachable from the top rung down to
the base.  That is pure combinatorics and costs seconds
(`analysis/wk11_int_s5_dag.py`, output in `results/wk11_int_s5_dag.txt`):

| from | peak distinct shapes at one level | total nodes to `δ = 1` |
|---|---|---|
| `λ_12 = (17,17,2⁷)` | 189 | **921** |
| `λ_24 = (65,17,2⁷)` | 585 | **7 656** |

Seven and a half thousand nodes, peaking at 585 shapes per level, with the count
flat at 585 across `δ = 12…16` and falling away on both sides.  **This is the
first realisation of the LMR source in the programme's history whose size is not
astronomical.**  It should replace `B_δ` as the pre-registered economic number,
because it is the one that scales with the work.

The storage cost is `Σ a_δ(μ)` over those 7 656 nodes, which the recursion
computes as a by-product — so implementing it *is* the measurement, and the
`δ = 12` sub-DAG at 921 nodes is a control small enough to run in an afternoon.

---

## 4. Where I push back

**A compressed source is worth nothing until it evaluates.**  The recursion
produces `M_λ` as a kernel inside an abstract `S_n`-representation.  The
programme needs `Θ`: those vectors evaluated at determinant and permanent
points, which lives in the monomial coordinates `c_α`.  A representation that
supports `τ` cheaply and `Θ` not at all has moved the wall rather than removed
it — and that is exactly the failure mode of every realisation the programme has
already discarded.  S5 names the risk in one clause ("whether `τ` can be applied
efficiently in compact Pieri/LR coordinates") and then prices the route without
it.

So the `δ = 12` control must be **two** tests, not one:

1. recover `dim M_12 = 2` exactly from the three-channel precursor; and
2. **evaluate those two vectors** against determinant points and reproduce the
   value the native engine gives at the same cell.

Only the second one proves the coordinates are usable.  A control that passes
(1) and skips (2) tells us the recursion is correct, which I have already
checked on paper, and nothing about whether it can be used.

**Two smaller ones.**  S1's discriminant is a genuine correction — "no equations
at `r < 9`" is false, and `Disc` vanishes on `D_5` at degree 405 — but it also
sharpens a phrasing of mine that was loose.  `docs/stocktake_batch10.md` asks for
"a length-5 equation of `I(D₅)` above degree 9"; that is now satisfied trivially
and settles nothing, because every reducible quartic is singular too, so
`Disc ∈ I(R₅)` as well.  The correct target, which the session-71 brief already
states, is an equation of `I(D₅)` that is **not** in `I(R₅)`.  The stock-take
phrasing should be read as superseded.

And S6 §6.3 — exact image versus orbit closure at `r = 5` — reaches from the
algebra side the same conclusion the batch-10 housekeeping reached from the
geometry side, that the `r = 5` non-containment is open and the paper's
"unconditional" overstates it.  Two independent routes to the same correction is
the strongest form this kind of finding takes.

---

## 5. What this does to the board

**S5 moves to the front.**  It was ranked level with C6 on expected value.  With
the recursion checked and the DAG measured it is no longer a theory bet: it is a
specified, sized construction with a control that fits in an afternoon.  The
next unit of work on the LMR source should be the `δ = 12` two-part control of
§4, ahead of any further carrier or black-box effort.

**S4's engine is validated and its frontier moves to `a_∞ = 4`.**  Eleven blocks
dead, the largest raw weight space in the completed frontier 12 479, and the
enumeration now complete at `a_∞ ≤ 3`.

**S1, S2 and S6's closures stand** and should be carried into the dead-route ledger:
classical cheap-equation retrieval, standard `q = 2` replication, partition-algebra
diagram bases, wreath Jucys–Murphy as a multiplicity basis, and the `F₄`
coincidence — the last with the audit Sol was asked for, and a clean negative.

**S3's four residues are already session 72's target list**, written into its
brief before the report arrived, which is the reconciliation working as designed.
