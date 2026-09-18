# B22-01 — The Missing Theorem, and the decision of the five-row identity

Batch 22, slot 01. Worktree `work/batch15_workers/B15-01`, branch `b15-01-ci159`. Claude Code (Opus 5,
1M context), default permission mode. Starting `HEAD = d5e9d8858ca917aa87985b684f3ba68d5b086286`, tree
`e3cf7292ce39450292a17283682dc7fe18648bfe`, recorded 2026-09-18T02:21Z before any write; `git status
--porcelain` showed no tracked change (the known untracked `results/` residue only). Read-only git; no
commit, no push, no stash.

Inputs, read-only and hash-checked at session start: `docs/b20_01_report.md` `e5f42641…` (bound by
`results/b20_01/MANIFEST.json` `0e5fd026…`); `docs/b21_01_report.md` `fdc709e0…` at `d5e9d885` (manifest
`1944b24d…`, equal on disk and at the commit); `B15-10/docs/b21_10_review.md` at `f7727cb7…`
(`ce2814c7…`); `arc_target_dimension_followup/REPORT.md` `041c2ae1…` and `CORRIGENDUM.md` `36a77547…` at
archive `82633a60`; `p6_basis.json` `aaee6ec0…` at `82633a60`; the pinned runner/carrier as bound by B20-01's
manifest. Corrigenda were read before parents. B21-10 R3 (`det(g)^{-4}`), R6–R7 (15 evaluations per full
functional; `1050` carries the degree-12 rows, `840` does not), R10 (floor `55,440`) are applied.

## 0. What this slot can and cannot establish (written before any computation)

**The four achievements.** A necessary source condition, a coefficient equation, a separation, and a
positive multiplicity gap are four different things. In this cell `lambda = (4^5)`, `d = 5`,
`m_det = 1`, `D = -1`: no positive multiplicity gap is possible in either branch of the outcome. This
slot touches the first achievement only.

**What it can establish.**

1. *The Missing Theorem* (B20-01 §5.1): an explicit spanning set of `F^L_{-1}` and a 70-point set on the
   flag locus whose evaluation is injective on `V_70`. PROVED if (a) every element of the spanning set
   is shown to lie in `F^L_{-1}` by construction, (b) the spanning family is shown to span by a proof
   (not by sampling), and (c) a `70 x 70` evaluation matrix has nonzero determinant modulo
   `P = 524287`. (c) is a finite computation; a nonzero modular determinant of an integer matrix is
   nonzero over `Q`, so it certifies injectivity over `Q` and over `F_P`.
2. *The decision.* With the certified set, ≈ 1050 runner evaluations give the `70 x 3` degree-11 and
   `70 x 3` degree-12 rows of `(q_3, q_7, n02)`.
   - A nonzero `3 x 3` minor modulo `P` of these integer rows proves `rank(C|_U) = 3` over `Q`
     (a floor). The diagnostic closes **negatively**; the identity is false.
   - If every `3 x 3` minor vanishes modulo `P`, what is proved is **the identity modulo `P`**: with
     `(alpha, beta) = (265391, 275398)`, `F_1^{n02} - alpha F_1^{q_3} - beta F_1^{q_7} = 0` and the same for the tops,
     **as polynomial identities over `F_P`**, i.e. `rank(C|_U (x) F_P) = 2`. The label is
     **CERTIFIED-modular**. It is not a floor on anything over `Q` beyond the known `rank >= 2`:
     a modular rank is a floor for the rational rank, never a ceiling, and rational rank 3 remains
     possible exactly when `P` divides every `3 x 3` minor of the exact integer rows. One prime cannot
     exclude that; exact (or bounded multi-prime) arithmetic can, and the runner computes modulo `P`
     only.
3. *What the `= 2` branch then says about sources.* `arc_target` Prop. 7.1 has the hypothesis
   `rank C|_S = 2` **over `Q`**. Under that hypothesis it gives: an exact `n* = n02 - alpha* q_3 - beta* q_7`
   with `alpha*, beta* in Q` spanning `ker C ∩ S`, reducing modulo `P` to the displayed candidate
   `n̄ = n02 - 265391 q_3 - 275398 q_7`, with `C4_{S1,S2}(n*) != 0` and `C4_{S1,S4}(n*) != 0` over `Q`.
   **This is an existence statement about a source condition** — there is an element of `ker C` on
   which the transverse `C4` conditions are nonzero — **not a gap, not an equation nonzero on padding,
   not a separation.** A CERTIFIED-modular outcome proves the `F_P` form of it (`n̄ in ker(C (x) F_P)` with
   `C4(n̄) = 499917, 487898 != 0` in `F_P`) and leaves the `Q` form **conditional on the lift**. I will
   not write the `Q` form as proved unless the rank is certified over `Q`.
4. *What it cannot establish.* Anything about `m_pad`, a cell, an equation, a separation or a gap;
   anything about `rank C` on all of `M` (only on `U = S = span(q_3, q_7, n02)`); anything at a second
   prime. Everything here is producer-only (G18): one session, one lineage.

## 1. Pre-registration (saved before any computation)

### 1.1 The construction I will attempt for the spanning set

**Setting** (B18-02 §1, `arc_target` §2.2–3.2). `W = Mat_4`; adapted coordinates of `Y`: `a = Y_00`,
`r_j = Y_{0,1+j}` (a `B'`-leg), `c_i = Y_{1+i,0}` (an `A'`-leg), block `E_{ij} = Y_{1+i,1+j}` (an `A'`-leg and a
`B'`-leg) split as `E = S + K`, `S` symmetric, `K` skew. `L = {(diag(alpha, g), diag(beta, c g^T))}` with
`alpha beta c^3 det(g)^2 = 1` acts by `Y -> A Y B`, so `r -> alpha c g r`, `c -> beta g c`, `E -> c g E g^T`: every
`A'`- and `B'`-leg is a copy of `std = C^3` under `g`, and `S`, `K` are `L`-stable.

**Typed contraction patterns.** A pattern `h` assigns to each of the 20 slots (4 columns x 5 positions)
of `D = Y_1 ^ ... ^ Y_5` a type in `{a, r, c, S, K}` (legs: 0, 1, 1, 2, 2), with adapted multidegree
`(#a, #r, #c, #S; #K)` one of `(1,4,4,0; 11)`, `(2,3,3,1; 11)`, `(3,2,2,2; 11)`, `(4,1,1,3; 11)` (degree 11)
or `(2,3,3,0; 12)`, `(3,2,2,1; 12)`, `(4,1,1,2; 12)` (degree 12), and partitions the 30 legs into ten
triples, each contracted with `eps_{ijk}` of `C^3`. Then `h(Y) := T_h(D, D, D, D)`, `T_h` the resulting
multilinear form on `(Λ^5 W)^{(x)4}` (each column is the full antisymmetrisation of its five typed slots).

**Claim S (to be proved in §2, not sampled).** (i) Every pattern of `nu`-degree 11 lies in `F^L_{-1}`;
(ii) the patterns span `F^L_{-1}`; (iii) `F_1^h = 0` unless the per-column `K`-counts are `{2, 3, 3, 3}`;
for such `h`, with the 2-`K` column first,
`F_1^h(Z_1, Z_2, Z) = <Xi_h, gamma(Z_1,Z_2,Z) (x) beta_1(Z_1,Z_2) (x) beta_2 (x) beta_3>`, where `Xi_h` is a fixed
8-leg integer tensor (the ten `eps` contracted with the constant `nu`-parts of the four columns),
`beta_k` the typed antisymmetrised pair `Z_1 ^ Z_2` in column `k`'s two non-`K` types, and `gamma` the typed
`Z_1 ^ Z_2 ^ Z` in column 0's three non-`K` types. The analogue for the tops (four 3-`K` columns, a
6-leg `Xi`). Tools: the FFT for `SL_3` (products of `eps` span the invariants of `V^{(x)30}`),
reductivity of `L` (invariants of a quotient are images of invariants), the Plücker/FFT-for-`SL_5`
identification of `S_lambda W^*` with quartic forms in `D` (Prop. C's premise, ADOPTED classical), and the
`L`-character computation of `arc_target` §3.2. Each external theorem will be labelled at its point of use.

**Search.** For each of the seven multidegree blocks, random patterns (seeded) are generated, `Xi_h`
computed exactly, and `F_1^h` (or the top) evaluated at 80 points: the 70 certificate points (below) and
the 10 recorded flag-locus points of B20-01 pilot 3 (5) and B21-01 (5). A pattern is kept iff it raises
the rank modulo `P`. Targets per block: `7, 31, 28, 4` (degree 11), `1, 2, 1` (degree 12), from
`arc_target` §5.1 (`b_L(11) = 70`, `b_L(12) = 4`, PROVED there). **A block rank above its target is
impossible if Claim S and `b_L` are right: if it happens I stop, do not run step 4, and report the
contradiction.**

### 1.2 The certification I will use

- **Points.** `p_1 .. p_70`: `(Z_1, Z_2, Z) in W'^3` with all 39 coordinates drawn uniformly modulo `P`
  from `numpy.random.default_rng(20260922)` (the symmetric block drawn upper-triangular and
  symmetrised, exactly as B20-01 pilot 3's `wprime_random`); integer entries in `[0, P)`. The runner
  tuple at `p_i` is `(Z_1, Z_2, Z + u nu_1, u nu_2, u nu_3)` with `nu_k` from `analysis/b20_01_flag.py`.
- **Certificate.** The `70 x 70` integer matrix `E_{ij} = F_1^{h_j}(p_i)` (reduced mod `P`), with
  `det E != 0 mod P`, computed twice (two eliminations). This proves the 70 `h_j` independent, hence
  (with `dim F^L_{-1} = 70`) a basis, and point evaluation at `p_1..p_70` injective on `V_70` over `Q` and,
  since the coordinates of any integer `F_1^z` in this basis are then `P`-integral, over `F_P`.
- **Degree 12.** The `70 x 4` matrix of the four top patterns has rank 4 mod `P` (a nonzero `4 x 4`
  minor), so the same points are injective on the tops as well; `C` restricted to `F^L` is then
  evaluated injectively by the 140 rows.
- **Controls inside the pilot (no runner).** (1) Claim S(iii) checked numerically: for three patterns,
  `F_1^h` and the top by the structured formula versus a brute-force evaluation of the full network
  at five `u`-nodes of the full tuple, with Vandermonde extraction (G22: nodes `1..5` determine
  `u^8..u^12`, nothing left free). (2) `L`-invariance of two patterns at a general 5-tuple under a
  random element of `L` (random `g`, `alpha`, `c`, and `beta` solved from the character), brute-force route.
  (3) Block ranks never above target. (4) The determinant by two eliminations.
- **Budget.** One wrapped pilot `b22_01_p1_basis` (60 s / 512 MiB); two spare launches for a crash or
  a cap hit, each under a new name. No runner evaluation before step 4.

### 1.3 The decisive run, as it will be executed if §§2–3 land

Pieces of ≤ 60 s / 512 MiB, `b22_01_p4_decide_<piece>`, `.pid` of `..\B15-02\results\logs\b22_02_*`
checked for a live pid before each launch. Piece `00` (controls, before any new point): the six sealed
values at P6 point 0 by the runner at the slice form (`F_1 + F_2 + F_3` and the top, 45 evaluations),
normalised by `det(g)^{-4}` as the identity `slice = det(g)^4 · full` states it (G21); one recorded flag
point of B20-01 pilot 3 replayed by the runner (15 evaluations); the relation residuals at all 19
recorded points recomputed from their recorded rows (arithmetic, no runner). Pieces `01..`: the 70
certified points, 15 evaluations each, JSON written after every point. Final piece: ranks, minors,
coordinates in the certified basis, and the **span control** — the coordinates of `F_1^{q}` and the top
determined by the 70 new points must predict the recorded values at the 10 recorded flag points; a
failed prediction means the certified basis does not span the space the runner's functions live in, and
voids the certificate whatever the rank says.

### 1.4 The three transcription sentences (one will be copied verbatim into §2)

1. **Theorem proved and set certified.** *The typed `eps`-contraction patterns lie in `F^L_{-1}` and span it
   (PROVED, §2); seventy of them, listed as data, have a `70 x 70` evaluation matrix at seventy listed
   flag-locus points with nonzero determinant modulo `P`, so they are a basis and the points are an
   injective evaluation set on `V_70` over `Q` and over `F_P` (CERTIFIED). The Missing Theorem of B20-01 §5.1
   holds; the identity is decidable by the run of §1.3.*
2. **Theorem fails for a structural reason.** *A block rank exceeded its proved target, or stalled below
   it with a reason that is structural rather than a budget limit; the reason is: [named exactly —
   which inherited count, which step of Claim S, or which property of the flag restriction]. No decisive
   run is launched.*
3. **Inconclusive within budget.** *The spanning set is PROVED but the search did not reach rank 70
   within the pilots allowed; missing: [blocks and ranks reached]; what the next pilot must do: [stated].
   No decisive run is launched, because without a certified set no finite evaluation decides anything.*
