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

## 2. The Missing Theorem — PROVED (written after pilots 1–2, before any runner evaluation)

**Transcription sentence 1 of §1.4, verbatim:**

> **Theorem proved and set certified.** *The typed `eps`-contraction patterns lie in `F^L_{-1}` and span it
> (PROVED, §2); seventy of them, listed as data, have a `70 x 70` evaluation matrix at seventy listed
> flag-locus points with nonzero determinant modulo `P`, so they are a basis and the points are an
> injective evaluation set on `V_70` over `Q` and over `F_P` (CERTIFIED). The Missing Theorem of B20-01 §5.1
> holds; the identity is decidable by the run of §1.3.*

### 2.1 Statement

Notation as in §1.1. `F^L_{-1}` is the space of `L`-invariant functions of `nu`-degree 11 in
`S_lambda(W^*) (x) det^4 ⊂ C[W (x) C^5]`: the space containing `z^{[11]}` for `z in M` (B20-01 §4.4). Its
dimension `b_L(11) = 70` is `arc_target` §5.1 (PROVED there, inherited; `arc_target` §2.1 identifies the
count in `S_lambda W` with the count in the function space). `F^L_{-2}` likewise, with `b_L(12) = 4`.

**Theorem M.** (i) Every typed pattern `h` of one of the four degree-11 multidegrees lies in `F^L_{-1}`,
and every pattern of one of the three degree-12 multidegrees lies in `F^L_{-2}`. (ii) The degree-11
patterns span `F^L_{-1}` and the degree-12 patterns span `F^L_{-2}`. (iii) `F_1^h = 0` unless the column
`K`-counts are `{2, 3, 3, 3}`. When they are (2-`K` column first),
`F_1^h(Z_1, Z_2, Z) = <Xi_h, gamma (x) beta_1 (x) beta_2 (x) beta_3>`, exactly as in §1.1. Likewise
`top^h = 0` unless all four `K`-counts are 3, and then `top^h = <Xi_h, beta_1 (x) ... (x) beta_4>`.
(iv) The seventy degree-11 patterns `h_1..h_70` and the four degree-12 patterns `t_1..t_4` recorded in
`results/b22_01/p2_basis.json` (`selected`) are bases of `F^L_{-1}` and `F^L_{-2}`. The seventy points
`p_1..p_70` recorded there (`points[0..69]`) are an injective evaluation set on `V_70 = F_1(F^L_{-1})` and
on the tops `top(F^L_{-2})`, over `Q` and over `F_P`.

### 2.2 Proof of (i): membership by construction (no external theorem beyond Cauchy)

*Form.* `h(Y) = T_h(D(Y)^{(x)4})` with `T_h` multilinear on `(Λ^5 W)^{(x)4}`. Each column is a
Plücker-linear function of `D`, and `D(gY) = det(g) D(Y)`, so `h(gY) = det(g)^4 h(Y)` for `g in GL_5`
acting on the tuple index. By the Cauchy decomposition `C[W (x) C^5] = ⊕_mu S_mu(W^*) (x) S_mu(C^{5*})`,
the `det^4`-semi-invariants of `GL_5` are exactly `S_{(4^5)}(W^*) (x) det^4`. (Cauchy: UNREAD-CLASSICAL, G14′.)

*Grading.* `W = W' ⊕ W_0`, where `W_0` is the skew block. The `K`-component of `Y` is its
`W_0`-component, and `a, r, c, S` read `W'`. Scaling `W_0` by `u` multiplies a pattern with eleven `K`
slots by `u^{11}`, so `h` is homogeneous of `nu`-degree 11.

*Invariance.* Take `(A, B) = (diag(alpha, g), diag(beta, c g^T)) in L`. Then `A Y B` has
`a -> alpha beta a`, `r -> alpha c g r`, `c -> beta g c`, `S -> c g S g^T` and `K -> c g K g^T` (there are
no cross terms, because `A` and `B` are block-diagonal). Every leg transforms by `g`, so the ten `eps`
give `det(g)^{10}`, and the scalars give `alpha^{#a+#r} beta^{#a+#c} c^{#r+#S+#K}`. For all seven
multidegrees, `#a + #r = #a + #c = 5` and `#r + #S + #K = 15`, checked row by row
(`4+0+11, 3+1+11, 2+2+11, 1+3+11; 3+0+12, 2+1+12, 1+2+12`). So the factor is
`(alpha beta c^3 det(g)^2)^5 = 1`, and `h in F^L_{-1}` (resp. `F^L_{-2}`). ∎

### 2.3 Proof of (ii): spanning (proved, not sampled)

Let `z in F^L_{-1}`. Let `T_ad` be the torus that scales `a, r, c, S, K` independently. It lies in
`GL(W)`, commutes with `L` (both act block-diagonally, `T_ad` by a scalar on each block), and preserves
the space above. So `z` is a sum of `L`-invariant multihomogeneous components, and by `arc_target` §3.2
only the four listed multidegrees carry `L`-invariants. Fix one, `m`, and take `z` multihomogeneous of
type `m`.

1. *Plücker.* `z = Q ∘ D` for a quartic form `Q` on `Λ^5 W`, because the degree-4 part of the Plücker
   coordinate ring of `Gr(5, W)` is `S_{(4^5)}(W^*)`: the Plücker coordinates generate. This is Prop. C's
   premise, ADOPTED; UNREAD-CLASSICAL, G14′.
2. *Reductivity, twice.* The map `Q -> Q ∘ D` is `L x T_ad`-equivariant, and `L x T_ad` is reductive
   (`L` is the kernel of a primitive character of `GL_3 x (C*)^3`, `arc_target` §3.2). Averaging
   (Reynolds), `Q` may be taken `L`-invariant of weight `m`. Since `Sym^4(Λ^5 W^*)` is an equivariant
   quotient of `(W^*)^{(x)20}`, `Q` is the image of an `L`-invariant weight-`m` multilinear form `Theta`
   on `W^{(x)20}`. (Complete reducibility in characteristic 0: UNREAD-CLASSICAL.)
3. *Types.* `W = Ca ⊕ R ⊕ C_c ⊕ Sym^2 ⊕ Λ^2` is `L x T_ad`-stable. So `Theta = Σ_tau Theta_tau`, summed over
   type assignments `tau` (slot -> type) with the counts of `m`, and each `Theta_tau` is invariant on
   `⊗_s W_{tau(s)}`. Compose with the `SL_3`-equivariant projections `std^{(x)2} -> Sym^2` and
   `std^{(x)2} -> Λ^2` to get an `SL_3`-invariant multilinear form on `std^{(x)30}` (the `a` slots are
   one-dimensional).
4. *FFT for `SL_3` (tensor form).* `SL(V)`-invariant multilinear forms on `V^{(x)3k}` are spanned by
   products of `k` determinants over partitions of the factors into triples (Weyl; UNREAD-CLASSICAL).
   Restricting back to `⊗ W_{tau(s)}` (where the projections are the identity), `Theta_tau` is a
   combination of `eps`-products restricted to typed slots, i.e. of typed patterns' multilinear forms.
5. *Back to functions.* `z(Y) = Theta(D^{(x)4})`. Write `D = Σ_pi sgn(pi) w_{pi(1)} (x) ... (x) w_{pi(5)}`.
   Evaluating a typed `eps`-product on `D^{(x)4}` gives exactly `T_h(D, D, D, D)`, with the columns
   antisymmetrised as in `typed_wedge`. So `z` is a combination of patterns. ∎

The degree-12 case is the same word for word. What the proof uses: no sampling and no search; three
classical theorems at the level of their textbook statements, each labelled; and the multidegree list
from `arc_target` §3.2 (PROVED there). **Label: (ii) PROVED** (given the three UNREAD-CLASSICAL inputs).

### 2.4 Proof of (iii): the structured formula

On the tuple `(Z_1, Z_2, Z + u nu_1, u nu_2, u nu_3)` we have `D(u) = u^2 D_2' + u^3 D_3`, where
`D_2' = Z_1^Z_2^Z^nu_2^nu_3` and `D_3 = Z_1^Z_2^nu_1^nu_2^nu_3` (Theorem A(v)). The `nu`'s have only `K`
components and the `Z`'s have none. So a column with `k` `K`-slots is nonzero on `D_3` only if `k = 3`,
and on `D_2'` only if `k = 2`. Since `h(u) = T_h(D(u)^{(x)4})`, the coefficient `[u^{11}]` needs exactly
one column on `D_2'` and three on `D_3`: the `K`-counts are `{2,3,3,3}`, and the 2-`K` column takes
`D_2'`. The coefficient `[u^{12}]` needs all four columns on `D_3`.

Take a 3-`K` column with slots `(K,K,K,t,t')` and vectors `(Z_1, Z_2, nu_1, nu_2, nu_3)`. The nonzero terms
of `Σ_pi sgn(pi)` send the `K` slots to the `nu`'s and `t, t'` to `Z_1, Z_2`. Each such `pi` factors as the
fixed permutation `(0,1,2,3,4) -> (2,3,4,0,1)` times the two block permutations. The fixed permutation
is a 5-cycle, hence even, so the column is exactly `Omega (x) beta_{t,t'}`. For the 2-`K` column the fixed
permutation is `(3,4,0,1,2)`, also a 5-cycle, and the column is `Omega' (x) gamma`. Contracting the ten
`eps` with the constant tensors `Omega` and `Omega'` gives `Xi_h`. ∎ Moreover `h(u) = u^{11} F_1^h`
exactly for a degree-11 pattern, and `h(u) = u^{12} top^h` for a degree-12 one.

Two consequences are used below. By (ii) and (iii), `V_70` is spanned by the `F_1^h` of
`{2,3,3,3}`-patterns, which is exactly the family the search draws from. And evaluating a pattern at a
flag point costs one 8-leg contraction (`3^8 = 6561` entries), not a runner call.

### 2.5 Proof of (iv) from the certificate

Since `b_L(11) = 70`, any seventy elements of `F^L_{-1}` whose `F_1`-images are linearly independent
form a basis (Prop. C: `z -> F_1^z` is injective, B21-10 R8). `det E != 0 mod P` for the integer matrix
`E_{ij} = F_1^{h_j}(p_i)` gives two things at once: the `F_1^{h_j}` are independent, so the `h_j` are a
basis; and evaluation at `p_1..p_70` is injective on their span `V_70`.

Over `F_P`: let `z in F^L_{-1}` be an integer polynomial (every source vector is one). Its coordinates
`c = E^{-1}(F_1^z(p_i))_i` are `P`-integral, because `det E` is a `P`-unit. So
`F_1^z mod P = Σ (c_j mod P)(F_1^{h_j} mod P)` as polynomials over `F_P`, and `F_1^z ≡ 0 mod P` iff
`F_1^z(p_i) ≡ 0 mod P` for all `i`. (The typed components use `1/2`, so everything lies in
`Z[1/2] ⊂ Z_(P)`.) For the tops: `z^{[12]} = 0` iff `top^z = 0` on `W'^2` (Theorem A(i)–(ii) with
`n = 12`, B20-01 Cor. A.2), and a nonzero `4 x 4` minor of `[top^{t_j}(p_i)]` gives the same two
conclusions. ∎

**A by-product.** The certificate proves `dim F^L_{-1} >= 70` and `dim F^L_{-2} >= 4` without
`arc_target`'s Littlewood–Richardson arithmetic. That is a second lineage for the lower half of
`b_L = 74`. The upper half (`<= 70`, `<= 4`) still rests on `arc_target` alone. The saturation probes
(§3.3) are consistent with it but prove nothing about it.

## 3. The certification

### 3.1 Two wrapped pilots: one search crippled by my bug, one certificate

| run | exit | wall | peak job memory | result |
|---|---|---|---|---|
| `b22_01_p1_basis` | 0 | `38.17 s` | `26.6 MiB` (27918336 B) | **not certified**: rank 57 of 70 (degree 11), 2 of 4 (tops) |
| `b22_01_p2_basis` | 0 | `5.36 s` | `135.1 MiB` (141692928 B) | **certified**: rank 70, rank 4 |

Pilot 1 failed on my code, not on the mathematics. `mod_einsum` followed numpy's greedy contraction
path and asserted that every step joins at most two operands. Numpy's greedy path does emit steps that
name more; the assertion fired, and the pilot's guard skipped the pattern. **About 22,000 pattern
attempts were skipped this way** (`guard_skips`, summed over the seven blocks, in
`results/b22_01/p1_basis.json`), so the ranks pilot 1 reached (57 and 2) are those of the biased
remainder. Nothing it computed is wrong: the 59 patterns it kept are valid and were resumed. But the
degree-11 Claim S(iii) check and the `L`-invariance check hit the same assertion and did not run.

The fix is in `analysis/b22_01_typed_v2.py`. A step naming `m > 2` operands is now executed as `m - 1`
pairwise contractions, each overflow-checked, and the `a` slots are placed in distinct columns directly
instead of by rejection sampling. The mathematics (typed components, `Omega`, `Omega'`, `Xi`,
evaluation, brute route) is byte-identical. I restored `analysis/b22_01_typed.py` to pilot 1's bytes
(`068a42bf…`, equal to pilot 1's own record), so that its receipt still binds the code that ran. Two of
the three launches were used; the third was not needed.

### 3.2 The certificate (`results/b22_01/p2_basis.json`, sha256 `7162d852…`)

| quantity | value | label |
|---|---|---|
| degree-11 basis `h_1..h_70` | blocks `(1,4,4,0)`: 7, `(2,3,3,1)`: 31, `(3,2,2,2)`: 28, `(4,1,1,3)`: 4, each exactly at `arc_target`'s target | explicit data (`selected`) |
| `det E mod P`, `E = [F_1^{h_j}(p_i)]_{70 x 70}` | **`132757`** by my row elimination and **`132757`** by B20-01's `det_mod`; `rank_mod = 70` | **CERTIFIED** (nonzero modular determinant of an integer matrix) |
| degree-12 basis `t_1..t_4` | `(2,3,3,0)`: 1, `(3,2,2,1)`: 2, `(4,1,1,2)`: 1 | explicit data |
| `4 x 4` top minor, rows `p_1..p_4` | **`136525`** (both eliminations) | **CERTIFIED** |
| points `p_1..p_70` | `rng(20260922)` through B20-01 pilot 3's `wprime_random`; integers in `[0, P)`; block symmetric (asserted) | data (`points[0..69]`) |
| the 10 recorded flag points | B20-01 pilot 3 (5) and B21-01 (5), with their recorded rows; every basis function is evaluated there too | data (`points[70..79]`), for the span control of §4 |

An example basis element, as stored (block `(1,4,4,0)`): columns `[K,K | r,c,a]`, `[K,K,K | r,r]`,
`[K,K,K | c,c]`, `[K,K,K | c,r]`, with legs numbered in that order, and the ten `eps` triples
`[1,15,25] [9,10,16] [12,13,26] [11,20,29] [8,21,28] [0,3,7] [4,19,22] [5,6,23] [2,18,27] [14,17,24]`.

### 3.3 Controls (all in pilot 2; no runner)

| control | outcome |
|---|---|
| Claim S(iii), degree 11: brute-force full network at the five `u`-nodes of `p_1`'s tuple, Vandermonde in `u^8..u^12` (the nodes `1..5` determine all five coefficients and leave none free, G22) | `[u^11] = 177727` = structured value; `u^8, u^9, u^10, u^12` all `0`: **passes** |
| Claim S(iii), degree 12 (a `(2,3,3,0)` pattern) | `[u^12] = 65671` = structured value; the others `0`: **passes** (it also passed in pilot 1, on a `(3,2,2,1)` pattern: `175390`) |
| `L`-invariance of a `(1,4,4,0)` pattern at a general 5-tuple; random `g, alpha, c`, with `beta` solved from the character (checked `= 1`) | `h(Y) = h(lY) = 222787`: **invariant**. Teeth: doubling `beta` gives `313453 = 32 · 222787 = 2^{#a+#c} h(Y)`, so **the test bites** |
| two contraction orders | pilot 1's 59 kept 80-point vectors reproduced by the fixed code, **59 of 59** |
| block ranks never above target | across the search and **85** further nonzero saturation patterns, no block exceeded `7, 31, 28, 4 / 1, 2, 1` |
| determinant | the two eliminations agree |

Label of the whole: **Theorem M PROVED; the 70-point set CERTIFIED; producer-only (G18).** One session,
one lineage. The evaluator of the patterns is mine, and the decisive run's span control (§4) is its only
contact with the runner.

## 4. The decisive run (pre-approved exceedance O4; launched only after §§2–3 were on disk)

§§2–3 were saved (report sha256 `243d8132…`) before the first runner evaluation of step 4. Before every
launch, `..\B15-02\results\logs\b22_02_*.pid` was checked (none existed at any launch) and the
`python.exe` process list was checked (empty at every launch).

### 4.1 G21 controls, before any new point (`b22_01_p4_decide_00`, 60 runner evaluations)

| control | outcome |
|---|---|
| **Six sealed values** at P6 point 0: the runner at the slice form (`F_1 + F_2 + F_3` and the top, 45 evaluations), stated as the identity `slice = det(g)^4 · full` and solved in the script (`det g = 199728`, `det(g)^{-4} = 252079`) | identity true for all six; `det(g)^{-4} ·` slice = `86170, 71919, 226580; 376209, 469277, 41046`: **6 of 6** sealed values; the top is equal across `k` for all three vectors |
| B20-01 pilot 3's flag point 0, replayed by the runner (15 evaluations) | `d11 = 24031, 249985, 378539`, `d12 = 355435, 346433, 410128`: **6 of 6** equal to the record |
| relation residual `n02 - alpha q_3 - beta q_7` on every recorded row (arithmetic, no runner) | **30 of 30 rows zero**: the 10 inherited rows of `f1_new_point_minor.py` (5 settings × 2 degrees), B20-01 pilot 3's 10 rows (5 points), and B21-01's 10 rows (5 points) |

On "the 19 recorded points": the handover documents (`BATCH21_CLOSE.md`, `BATCH22_PROPOSED_BOARD.md`)
say "nineteen concordant points" without listing them. The count that fits is 10 inherited rows + 5
pilot-3 points + 4 new B21-01 points. I replayed every recorded row I could locate, which is a superset
(30 rows at 15 settings). Two of the settings were also replayed by the runner itself.

### 4.2 The run (`b22_01_p4_decide_01..12`, 1050 runner evaluations; `_final`, no runner)

The run covered seventy certified points, 15 evaluations each (`[u^11]` and `[u^12]` of `q_3, q_7, n02`
from the nodes `u = 1..5`, which determine `u^8..u^12`, G22), in twelve pieces of 6 points (4 in the
last), with the JSON written after every point. `_final` hash-checks the certificate and the twelve
piece files, recomputes `det E = 132757`, and computes (all numbers from
`results/b22_01/decide/piece_final.json`):

| quantity | value |
|---|---|
| rank mod `P` of the `140 x 3` rows (70 degree-11, 70 degree-12) | **2** (degree-11 rows alone: 2; degree-12 rows alone: 1) |
| a nonzero `3 x 3` minor | **none** (rank 2) |
| relation residual `n02 - 265391 q_3 - 275398 q_7`, per row | **0 on all 140 rows** |
| the same relation on the coordinates `X = E^{-1} N_{11}` in the certified basis | **0 in all 70 coordinates** |
| degree-12 ratios `q_7/q_3`, `n02/q_3` | `(101007, 295818)` at **all 70 points** |
| **span control**: coordinates fitted on the 70 new points predict the recorded values at the 10 recorded flag points | degree 11: **30 of 30**; degree 12: **30 of 30** |
| top consistency: the 4-coordinate fit on rows `p_1..p_4` reproduces all 70 degree-12 rows | **70 of 70** |

The span control matters most. It is where the certified basis — built by my evaluator, never by
the runner — meets the runner's functions at points it was never fitted to: 60 independent
predictions, 60 hits. Had my patterns spanned some other 70-dimensional space, the fitted coordinates
would have missed the recorded values.

### 4.3 Transcription

The `= 2` branch landed. **The identity is CERTIFIED-modular, not CERTIFIED (exact).** Stated precisely:

1. **Proved (over `F_P`, `P = 524287`).** With `f = n02 - 265391 q_3 - 275398 q_7` and
   `(alpha, beta) = (265391, 275398)`: `F_1^f ≡ 0` and `top^f ≡ 0` as polynomials over `F_P`, by §2.5 and the
   140 zero residuals. Theorem A holds over `F_P`, because its proof is covariance plus density over an
   infinite field and applies over `F_P`-bar. So `f^{[11]} ≡ 0` and `f^{[12]} ≡ 0` mod `P` as polynomials
   in the 80 variables, i.e. **`rank(C|_U (x) F_P) = 2` exactly**, and the five-row mixed-pairing
   identity
   `4B(t_1,s_1) = 2a[B(t_1,s_2) + B(s_1,t_2)] + 2b[B(t_3,s_2) + B(s_3,t_2)]` holds as a polynomial identity
   modulo `P`. The tops are proportional mod `P` with ratios `101007`, `295818` — also a polynomial
   identity mod `P`, where before it was sampled.
2. **Not proved (over `Q`).** A modular rank is a lower bound on the rational rank, never an upper bound;
   here it gives `rank(C|_U) >= 2`, which was already known. `rank(C|_U) = 3` over `Q` is not excluded,
   but it would require `P` to divide every `3 x 3` minor of the exact integer rows at these 70 points.
   The runner computes modulo `P` only, so this run cannot see that. I attach **no probability** to it:
   `P` was fixed long before these vectors were chosen, and nothing here is random in the relevant
   sense.
3. **The source condition (`arc_target` Prop. 7.1), in the form this result supports.**
   - *`F_P` form, PROVED:* `n̄ = n02 - 265391 q_3 - 275398 q_7` lies in `ker(C (x) F_P)`, and the transverse
     rows are nonzero on it: `C4_{S1,S2}(n̄) = 499917`, `C4_{S1,S4}(n̄) = 487898` in `F_P` (parent
     certificates, as used in Prop. 7.1's proof). So the reduction modulo `P` of the arc, restricted to
     `S`, has a kernel vector on which the transverse `C4` conditions do not vanish.
   - *`Q` form, CONDITIONAL on `rank C|_S = 2` over `Q` (not delivered):* there is an exact
     `n* = n02 - alpha* q_3 - beta* q_7` with `alpha*, beta* in Q` spanning `ker C ∩ S`, reducing to `n̄` mod `P`, with
     `C4(n*) != 0` over `Q`.
   - Either way, **this is an existence statement about a source condition — not a gap, not an equation
     nonzero on padding, not a separation.** In this cell `D = -1`, and no positive multiplicity gap is
     possible in either branch.
4. **What would make it exact** (a reopening condition, not attempted). One route: the exact integer
   values of the 140 rows, or bounded multi-prime values, followed by a check that every `3 x 3` minor
   vanishes over `Z`. The injective set is already certified over `Q`, so the points need not change.
   With the runner, that means a carrier at other primes (its `P` is a module constant in pinned bytes),
   plus a proved height bound on the values, which sets the number of primes. At points with entries in
   `[0, P)` the bound is enormous. With small-integer points (a fresh certificate, one cheap pilot as
   above) it drops sharply, and I would expect on the order of ten or more primes. At about `1050`
   evaluations per prime, that is ≈ 10^4 evaluations. **This is an estimate, not a priced plan.** The
   other route: exact rational coordinates of `q_3, q_7, n02` in the certified basis. The `eps_4`-blocks
   of the source vectors expand into typed `eps_3`-patterns, which is exactly the form of §2, so this
   route needs no runner at all. It is untested, and I do not price it.

## 5. Ledger

| id | statement | label | basis |
|---|---|---|---|
| B22-01.1 | Session state as recorded; HEAD `d5e9d885`, tree `e3cf7292`; read-only git; no commit | VERIFIED | §header |
| B22-01.2 | Pre-registration (§§0–1) saved before any computation (sha256 `014aa002…`, snapshot kept) and byte-identical at the end | VERIFIED | `results/b22_01/preregistration_snapshot.md`; prefix check |
| B22-01.3 | Theorem M(i): every typed pattern of the listed multidegrees lies in `F^L_{-1}` / `F^L_{-2}` | **PROVED** (Cauchy: UNREAD-CLASSICAL) | §2.2 |
| B22-01.4 | Theorem M(ii): the typed patterns span `F^L_{-1}` / `F^L_{-2}` | **PROVED** (Plücker generation, complete reducibility, FFT for `SL_3`: UNREAD-CLASSICAL; multidegrees from `arc_target` §3.2) | §2.3 |
| B22-01.5 | Theorem M(iii): structured formula; `F_1^h = 0` unless the `K`-counts are `{2,3,3,3}`; `h(u) = u^{11} F_1^h` | **PROVED**; numerically replayed against the brute-force network, degree 11 and degree 12 | §2.4, §3.3 |
| B22-01.6 | 70 explicit patterns with `det[F_1^{h_j}(p_i)] = 132757 ≠ 0 mod P` (two eliminations); 4 top patterns with a `4 x 4` minor `136525` | **CERTIFIED** | `p2_basis.json` `7162d852…` |
| B22-01.7 | **The Missing Theorem (B20-01 §5.1) holds**: explicit basis of `F^L_{-1}` (and `F^L_{-2}`); `p_1..p_70` injective on `V_70` and on the tops, over `Q` and `F_P` | **PROVED + CERTIFIED** (on inherited `b_L = 70, 4`, and Prop. C) | §2.5 |
| B22-01.8 | `dim F^L_{-1} >= 70`, `dim F^L_{-2} >= 4` independently of `arc_target` | **CERTIFIED** (a second lineage for the lower half of `b_L`) | §2.5 |
| B22-01.9 | No block rank above target across the search and 85 saturation patterns | MEASURED consistency only; proves nothing about the upper half | §3.3 |
| B22-01.10 | `L`-invariance of a pattern at a general tuple, with a test that bites (`2^{#a+#c}`) | PASSES | §3.3 |
| B22-01.11 | G21 controls: six sealed values 6 of 6 via `slice = det(g)^4 · full`; a recorded flag point replayed 6 of 6; 30 of 30 recorded rows with relation residual 0 | PASSES | §4.1 |
| B22-01.12 | 70 certified points × 15 runner evaluations: rank 2 mod `P` on 140 rows, relation residual 0 on all rows and all coordinates; degree-12 ratios constant | MEASURED (the data) | §4.2 |
| B22-01.13 | Span control 60 of 60; top consistency 70 of 70 | PASSES — the certified basis spans the runner's functions | §4.2 |
| B22-01.14 | **The five-row mixed-pairing identity holds modulo `P` as a polynomial identity; `rank(C|_U (x) F_P) = 2`; the tops are proportional mod `P`** | **CERTIFIED-modular** | §4.3 item 1 |
| B22-01.15 | `rank(C|_U) = 2` over `Q` | **OPEN**: not excluded to be 3; would need `P` to divide every `3 x 3` minor of the exact rows | §4.3 item 2 |
| B22-01.16 | `F_P` form of `arc_target` Prop. 7.1: `n̄ in ker(C (x) F_P)` with `C4(n̄) = 499917, 487898 ≠ 0` | **PROVED** (existence over `F_P`, about a source condition) | §4.3 item 3 |
| B22-01.17 | `Q` form of Prop. 7.1: exact `n* in ker C` with `C4(n*) ≠ 0`, lifting `n̄` | **CONDITIONAL** on B22-01.15 | §4.3 item 3 |
| B22-01.18 | Nothing here is a gap, a cell, an equation nonzero on padding, or a separation; `D = -1` | standing | §0 |
| B22-01.19 | Pilot 1 did not certify: my `mod_einsum` rejected numpy's multi-operand path steps and about 22,000 attempts were skipped; fixed in `_v2`, the mathematics byte-identical, and 59 of 59 vectors reproduced | honest negative | §3.1 |
| B22-01.20 | Everything is producer-only | G18 | — |

## 6. Resources, receipts, manifest

Interpreter `..\B15-02\.venv\python.exe` (Python 3.12.10, numpy 2.4.6); wrapper
`..\B15-02\analysis\b15_bound.py`; `PYTHONDONTWRITEBYTECODE=1` in every launch shell;
`job_object_enforced: true` in every receipt. The figures below are copied from
`results/logs/b22_01_*_resources.json`.

| run | exit | wall | peak job memory | runner evaluations |
|---|---|---|---|---|
| `b22_01_p1_basis` | 0 | 38.169 s | 26.6 MiB (27918336 B) | 0 |
| `b22_01_p2_basis` | 0 | 5.358 s | 135.1 MiB (141692928 B) | 0 |
| `b22_01_p4_decide_00` | 0 | 29.404 s | 244.8 MiB (256675840 B) | 60 |
| `b22_01_p4_decide_01` … `_11` | 0 (all) | 39.157 – 42.827 s each, 450.882 s total | ≤ 277.9 MiB (max 291438592 B, piece 07) | 90 each |
| `b22_01_p4_decide_12` | 0 | 27.540 s | 278.0 MiB (291504128 B) | 60 |
| `b22_01_p4_decide_final` | 0 | 0.154 s | 22.8 MiB (23904256 B) | 0 |

- **Default-limit budget (steps 2–3).** Two of three wrapped pilots were used, 43.53 s of 180 s. No cap
  was hit, and no runner evaluation was made.
- **The exceedance (step 4).** 14 launches, 507.98 s wall in total, 1110 runner evaluations (1050 at the
  new points, 60 in the controls). Every piece was ≤ 60 s and ≤ 512 MiB (largest wall 42.8 s, largest
  peak 278.0 MiB, i.e. 71% and 54% of the caps). No cap was hit, and no receipt was overwritten.
- **Unwrapped, non-numerical (G19 as B21-10 R22 defines it).** Read-only `git show` / `rev-parse` /
  `status`; `sha256sum`; `tasklist`; file listings; Python-`ast` parse checks of the new scripts; JSON
  inspection of recorded outputs (reading and printing fields, no computation on the objects); the
  seal script. **No unwrapped numerical run.**
- **Write footprint (all new).** `docs/b22_01_report.md`; `analysis/b22_01_typed.py`,
  `b22_01_typed_v2.py`, `b22_01_p1_basis.py`, `b22_01_p2_basis.py`, `b22_01_p4_decide.py`;
  `results/b22_01/` (pre-registration snapshot, `p1_basis.json`, `p2_basis.json`, `decide/piece_*.json`,
  `pinned/` with the runner/carrier bytes, patched runner `e7ba4ff7…` equal to B20-01's); and
  `results/logs/b22_01_*` (16 receipts + 16 `.pid`). **Nothing under `results/b20_01/` or
  `results/b21_01/` was written** (the pilots only read three files there, against their manifest
  hashes).
- **For the housekeeping session (B21-10 R27).** The 16 `.pid` receipts match `.gitignore`'s
  `results/logs/*.pid` and must be force-added at commit, or the manifest will bind files that a fresh
  checkout lacks.

`results/b22_01/MANIFEST.json` binds every file above with its sha256 and byte count, plus the pinned
inputs' hashes. `results/b22_01/SEAL_LOG.txt` prints every count it writes. Neither file binds itself,
and this report does not name its own hash.

**Deviations.** (1) Two basis pilots, not one: the first was crippled by my own bug (§3.1). (2) The
pre-registration promised the Claim S(iii) brute check "for three patterns" and `L`-invariance "of two
patterns". What ran: Claim S(iii) on three patterns across the two pilots (degree 12 in pilot 1;
degree 11 and degree 12 in pilot 2), and `L`-invariance on one pattern, with a teeth check instead of
a second pattern. (3) "The 19 recorded points" were replayed as a 30-row superset (§4.1). (4) Step 4
used 1110 runner evaluations against "≈ 1050": the extra 60 are the controls the prompt placed before
the new points. (5) The step-4 transcription is CERTIFIED-modular. The prompt offered
"CERTIFIED-modular-floor"; I do not use the word "floor", because over `F_P` the rank is exact and over
`Q` the modular rank bounds nothing new (§4.3 item 2).
