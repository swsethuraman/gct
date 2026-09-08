# Batch-12 S1 — integrator review

Astra's S1, read against the report itself and against the banked tree.  Short
version: **the stock-take's reading is right**, the theorem is correct, and it
carries one consequence neither the report nor the stock-take draws — which I
have now proved and checked on banked data, and which changes what s74 is for.

---

## 1. The theorem checks out

I verified the proof line by line rather than accepting it.

`u = c_{(n,0,…,0)}` is a highest-weight vector: `E_{ij} c_α = (α_i + 1)
c_{α + e_i − e_j}` for `i < j` vanishes when `α_j = 0`, and `u`'s exponent is
zero in every coordinate past the first.  So `E(uG) = uE(G)`, and since `R` is a
domain, `uG ∈ M_d ⟺ G ∈ M_{d−1}`.  Conversely `F|_{u=0} = 0` means every monomial
of `F` carries `u`, so `F = uG` with `G` unique and — by weight homogeneity — of
the predecessor weight.  Hence `ker ρ_d = uM_{d−1}` and
`M_d / uM_{d−1} ≅ ρ_d(M_d)`.

Two things I checked beyond the proof:

- **`uM_{d−1}` really is the ladder transport.**  Lemma L (s57) uses the same
  `u = c_{(4,0,…,0)}`, so the quotient is the birth space and its dimension is
  `b_d = a_d − a_{d−1}`, the banked birth profile.
- **The report's ladder is our ladder.**  `ρ = (17, 2^7)`, `|ρ| = 31`, weight
  `(4d − 31, 17, 2^7)` — identical to `analysis/wk11_int_bdelta.lam_of`, and at
  `d = 24` it is `(65, 17, 2^7)`.  Its `b_d` column matches
  `results/s63_aladder.json` entry for entry and sums to 274.

## 2. What follows that neither document states

**Proposition.**  Let `I` be a **prime** ideal with `u ∉ I`.  Then

    (I ∩ M_d) ∩ uM_{d−1} = u (I ∩ M_{d−1}).

*Proof.*  `⊇` is clear.  For `⊆`: if `v = uw ∈ I` with `w ∈ M_{d−1}`, primality
and `u ∉ I` give `w ∈ I`. ∎

Both hypotheses hold on both sides of the programme.  `I(Det₄)` and
`I(ℓ·per₃)` are ideals of orbit closures, hence irreducible, hence prime; and
`u ∉ I` because the coefficient of `s₁ⁿ` is `det(A₁)` on a determinant pencil and
`a₁ · per(B₁)` on a padded one, both generically nonzero.

Two consequences, and they are the reason this session matters more than its
headline:

1. **The ideal grows only by births.**  `i_X(d) − i_X(d−1)` counts births *inside*
   the ideal, and an ideal vector born at rung `d` is nonzero mod `u`.  So the
   obstruction — the thing the whole programme is looking for — can be found and
   certified entirely inside the birth quotient.  It never has to be separated
   from the transported source.

2. **`i_X(d) − i_X(d−1) ≤ b_d`.**  At the goal cell `b₂₄ = 1`, so

       i_det(24) = i_det(23) + ε,      ε ∈ {0, 1},

   with `ε = 1` exactly when the determinant ideal contains a vector of nonzero
   `u`-restriction at `δ = 24`.  Together with LMR's `i_det(24) ≥ 1`: **either
   `i_det(23) ≥ 1`, or `i_det(23) = 0` and the single `δ = 24` birth direction
   *is* the determinant ideal vector.**

   And on the transported source the rank is pinned exactly:
   `ker(T_det |_{uM₂₃}) = u·(I ∩ M₂₃)`, so

       rank T_det |_{uM₂₃} = 273 − i_det(23).

   So `i_det(23) = 0` alone gives `rank T_det = 273` **on the δ = 23 source
   transported up**, with no `δ = 24` candidate needed at all — and then
   consequence 2 forces `i_det(24) = 1` exactly.  That is the rank-273 rule of
   the reconciled proposal, upgraded from a stopping rule to a structural
   statement about which rung the work actually lives on.

**Checked on banked data.**  At the `n = 3` cell where the determinant ideal
vector is known exactly (s62 via s69, `λ = (19,7,2^5)`, `δ = 12`, `b₁₂ = 1`), the
proposition predicts it is not divisible by `u`.  Run here
(`analysis/wk12_int_birth_quotient.py`):

    N_S = 1,155,302;  chi coordinates 17,047
    u-free chi coordinates                        729   (4.3%)
    banked ideal vector support                 3,900
      of which u-free                              54   -> restriction NONZERO

So it is a birth direction, as the proposition requires.

A second economy falls out that nobody has stated: **only 729 of 17,047
coordinates survive `u = 0`**.  The restriction compresses the coordinate space
**23-fold** as well as shrinking the rank matrix.  On the determinant side that
is a second multiplicative saving on every evaluation, not just on the
elimination.

## 3. Where I would qualify the stock-take

Agreement first: original goal RETIRED, unexpected theorem PROVED, practical
consequence MAJOR KEEP, candidate hitting OPEN.  That ledger is right.  Three
qualifications.

**The endgame is not coupon collecting any more, and the stock-take still frames
it that way.**  At `δ = 23` and `δ = 24` the birth quotient is a *line*.  So there
is no specific rare direction to hit: **any** candidate whose restriction to
`u = 0` is nonzero completes the rung.  Existence is guaranteed — fillings span
`M_d` and `b_d = 1 ≠ 0`, so such a filling exists.  And the report's own rule 3
gives a free syntactic filter: a filling with a letter occupying only its `n`
singleton columns is `n!·u·(something)` and dies in the quotient, which is
exactly what ladder-transported candidates look like.  So the endgame is a
*first-hit search on a filtered stream*, not a coupon-collector tail.  What
remains genuinely open is the hit rate on that stream, which nobody has measured.

**The retirement is narrower than "straightening is dead."**  The report is careful and
the stock-take hardens it slightly.  What died is *unrestricted Plücker expansion
as the route to the 274-vector basis at the goal cell, at a deliberately
small 64-term cap*.  The real
obstruction is not the cap — it is that **there is no independence theorem after
the umbral contraction and identical-letter symmetrization**.  Raising the cap
would not revive it; that theorem would.  This matters for the board: my `s77`
asks for the Pieri-to-circuit bridge, which is a different construction, and if
it yields a triangularity statement it revives this route rather than repeating
it.  The brief will say so explicitly, so that retiring the route does not also
retire the adjacent question.

**One correction the report makes, and it is right.**  A ladder step adds `n`
singleton columns, not one.  `λ'_δ = (9, 9, 2^15, 1^{4δ−48})`, so the `1`-column
run lengthens by 4 at `n = 4` and by 3 at the `n = 3` control.  The
implementation was always right — a step appends the `n` singleton columns of a
fresh letter, which is multiplication by `u` — so nothing computed is affected.
`docs/compact_circuit.md` line 58 said "one `1`-column per degree" and is now
corrected.

## 4. Two bookkeeping notes on the run itself

- **Astra read the tree at `c984e2c`**, before the three pre-batch commits.  So
  its preflight ledger is one range stale: the s67/s71 certifier reconciliation
  it lists as not replayed *has* been done (40 comparisons, every order agreeing),
  and the weight-13 recount it lists as outstanding is done (47 stands;
  `a_∞ = 4` is five blocks).  `split_rank` and `hybrid_kernel` are still
  RECORDED, correctly reported.  `origin/main` is now `b8d8241`.
- **`ModuleNotFoundError: flint` is an environment gap on the Windows host, not a
  repository defect.**  `python-flint` is a house dependency for exact linear
  algebra.  No self-test case ran there; the twelve cases pass here.  Nothing
  should be recorded as a calibration failure on that basis.
- The report's warning that the 113-vector goal-cell checkpoint and the ladder-source
  checkpoint are different collections whose ranks must not be added is correct
  and goes into the s74 brief verbatim.

## 5. What this does to the board

`s74` changes shape and gets cheaper.  It is no longer "sample, then eliminate
against a source climbing to 274."  It is, per rung:

    fix b_d + 8 coefficient points with u = 0
    replay the saved native candidates for that rung first
    reject pure-u fillings syntactically, before any evaluation
    evaluate on the u = 0 points, in the 729-of-17,047-style compressed coordinates
    retain a candidate only when a recorded nonzero minor raises the birth rank
    stop the rung at b_d; keep the original source rows, not the echelon rows

with a worst retained matrix of `55 × 62` at `d = 14` and `2 × 9` at the last two
rungs.  And it gains a new first move, from §2: **measure `i_det(23)`** — that
is, the determinant rank on the transported `δ = 23` source.  Zero finishes the
determinant side outright, at `rank T_det = 273`, without any `δ = 24` candidate.

No other session changes.  `s75`/`s76` are untouched — S1 says plainly that
`B₂₄ = 2168` is a dimension and not an evaluable map, which is exactly why those
two exist.  `s77` gains the paragraph above about what would revive straightening.

## 6. Ledger

| claim | status |
|---|---|
| `ker(M_d → R/(u)) = uM_{d−1}` | **PROVED** (S1), proof checked here |
| ideal growth is a birth phenomenon; `i_X(d) − i_X(d−1) ≤ b_d` for prime `I` with `u ∉ I` | **PROVED** (here), checked on the banked `n = 3` vector |
| `rank T_det|_{uM₂₃} = 273 − i_det(23)` | **PROVED** (here) |
| coordinate compression `17,047 → 729` at the `n = 3` control | **MEASURED** |
| ten evaluation-ready goal-cell vectors | **CERTIFIED**, and 264 short of a source |
| unrestricted Plücker straightening as the route to the goal-cell basis | **RETIRED**, for want of an independence theorem after umbral contraction — not for want of a larger term cap |
| candidate hitting / stream hit rate | **OPEN** — and now the only thing between the programme and `D(24)` |
