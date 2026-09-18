# B21-10 — verdicts formed before reading the deliverable's own defence

Byte-preserved. Nothing below is edited after the corresponding defence is opened; corrections,
if any, appear only in `docs/b21_10_review.md` with an explicit pointer back to the entry here.

Session start state (read-only git, recorded before any write):

```
git rev-parse HEAD          6915ae6fea04c446da5042fad4c43c1667230602
git rev-parse HEAD^{tree}   7052fbfdfd1e6619149420a0405be49a241bbf6c
git status --porcelain      ?? results/logs/b15_10_runtime_native_20260913.pid
                            ?? results/logs/b15_10_runtime_native_20260913_resources.json
recorded at                 2026-09-18T00:23:22Z
```

---

## P1 — Theorem A, B20-01 §4.2, parts (i)–(v)

**Written 2026-09-18T00:26:57Z.** Formed from `docs/b20_01_report.md` §§4.1–4.2 only, at
`b15-01-ci159` @ `878258f295dd5a6b306137fadaab816ce0deb3df` (file sha256
`e5f426410f6e5dff4037dc0d837826fb09cca173f7da420dbeb41bb15eb35c89`). At the moment of writing I
have **not** opened §11 of that report, `results/b20_01/p2_reduction.json`, any B20-01c artifact,
the B20-02 reports, or the integrator ledger. The only facts about pilot 2 in my possession are
the four numbers quoted in my own brief (`theorem_A_passed: false`; deg-11 `q_3` `300999` vs
`86170`; deg-12 `n02` `279654` vs `41046`; the internal checks passing).

Method: **READ**, with every step re-derived by hand on paper (no arithmetic, no code).

### P1.1 The five parts

**(i) — correct.** The `nu`-grading is the weight decomposition of the one-parameter subgroup
`sigma_u in GL(W)` that scales `W_0` by `u` and fixes `W'`, applied diagonally to all five tuple
entries. `sigma_u` commutes with the `GL_5` action on the tuple index, because the latter takes
`C`-linear combinations of the `Y_m` with the *same* map applied to each. Hence
`z(sigma_u(g.Y)) = z(g.(sigma_u Y)) = det(g)^4 z(sigma_u Y)`, and comparing coefficients of `u^n`
gives `z^{[n]}(g.Y) = det(g)^4 z^{[n]}(Y)`. The report's own one-line proof says exactly this.

**(ii) — correct.** `v` is `3x5`; for `u in C^5`, the `nu_k`-coordinate of `(g.Y)_i = sum_m g_{im} Y_m`
is `(v u_i)_k` where `u_i` is the `i`-th row of `g`. Rows `u_1, u_2` spanning `ker v` give
`Z_1, Z_2 in W'`; `v u_{k+2} = e_k` gives `Z_{k+2} + nu_k`. `det g != 0` because `u_3, u_4, u_5` are
independent modulo `ker v` (their images `e_1, e_2, e_3` are independent) and `u_1, u_2` span it.

**(iii) — correct.** `D_3 = Z_1^Z_2^nu_1^nu_2^nu_3` and
`D_2 = Z_1^Z_2^(Z_3^nu_2^nu_3 + nu_1^Z_4^nu_3 + nu_1^nu_2^Z_5)` are right: on the slice only slots
3,4,5 carry a `nu`, one each, so `nu`-degree 3 forces all three `nu`'s and `nu`-degree 2 forces
exactly one slot to contribute its `Z`. `D` has `nu`-degrees `0..3`, so `11 = 3+3+3+2` is the only
partition into four parts each `<= 3`, and symmetry of `z~` gives the multiplicity 4; hence
`z^{[11]}|slice = 4 z~(D_3, D_3, D_3, D_2)`, linear in `D_2`, hence a sum of three terms `G_k`, the
`k`-th linear in `Z_{k+2}` and otherwise depending only on `Z_1, Z_2`. Setting the other two `Z`'s
to zero kills the other two terms **because each is linear in its own `Z`**, and returns `G_k`,
which is the theorem's `F_k`. So `z^{[11]}|slice = 0` iff every `F_k = 0`.
*Wording defect, not a proof defect:* the proof writes "a sum of functions of disjoint variable
groups vanishes iff each does". The three groups are **not** disjoint — all three share `Z_1, Z_2`.
The conclusion survives untouched by the mechanism the same sentence supplies (set the other
groups to zero), which works precisely because of the linearity just noted. The sentence as
written is a false general principle; the specialisation used is true.

**(iv) — correct, including the sign.** I re-derived the three ingredients.
`(P M P^T)_{ij} = M_{sigma^{-1}(i) sigma^{-1}(j)}`, so
`(P nu_k P^T)_{ij} = -eps_{sigma^{-1}(i) sigma^{-1}(j) k}`; substituting `k = sigma^{-1}(sigma(k))` and
using total antisymmetry, `eps_{sigma^{-1}(i) sigma^{-1}(j) sigma^{-1}(sigma(k))} = sgn(sigma) eps_{i j sigma(k)}`,
so `P nu_k P^T = sgn(sigma) nu_{sigma(k)}`. The report's displayed identity is the same one.
Conjugation by `diag(1, sigma)` preserves the block splitting and skew-symmetry of the `3x3` block,
so it preserves `W'`, `W_0` and therefore `nu`-degree.
The two `GL_5` moves then bookkeep correctly: applying `P(-)P^T` to the `F_1`-tuple
`(Z_1, Z_2, Z + nu_1, nu_2, nu_3)` gives slot `k+2` equal to `delta_{k1} P Z P^T + s nu_{sigma(k)}`
with `s = sgn(sigma)`; the tuple permutation `pi` sending slot `k+2` to slot `sigma(k)+2` has
`det = sgn(sigma) = s` and contributes `det^4 = s^4 = 1`; scaling the last three entries by `s`
has `det = s^3` and contributes `s^12 = 1`, and turns slot `j+2` into
`delta_{j, sigma(1)} (s P Z P^T) + nu_j`. That is the `F_{sigma(1)}`-tuple at
`(P Z_1 P^T, P Z_2 P^T, s P Z P^T)`, and linearity in the third argument pulls out `s`. Hence
`F_1^z(Z_1,Z_2,Z) = sgn(sigma) F_{sigma(1)}^z(P Z_1 P^T, P Z_2 P^T, P Z P^T)`, exactly as stated, and
since `sigma(1)` ranges over `{1,2,3}`, `F_1 = 0` iff all `F_k = 0`.
*Micro-slip:* the proof labels the second factor `s^4`; the determinant of `diag(1,1,s,s,s)` is
`s^3` and the factor is `s^12`. Both equal 1 for `s = +-1`, so nothing moves.

**(v) — correct.** Forward is specialisation. Backward: `F_1 = 0` gives all `F_k = 0` by (iv),
hence `z^{[11]} = 0` on every rank-`v`-3 slice by (iii), hence on the dense open set `{rank v = 3}`
by (ii) together with the covariance (i), hence identically. `39 = 3 x dim W' = 3 x 13`. The node
count is right: on the `F_1`-tuple,
`D(sigma_u T_1) = u^2 (Z_1^Z_2^Z^nu_2^nu_3 + u Z_1^Z_2^nu_1^nu_2^nu_3) = u^2(D_2' + u D_3)`, so `z`
has `u`-degrees `8..12` — five unknowns, five nodes, against thirteen at a general point, and
`[u^{11}] = 4 z~(D_3,D_3,D_3,D_2') = F_1` and `[u^{12}] = z~(D_3^4)`.

**Ruling P1: Theorem A (i)–(v) is PROVED as stated.** Method READ, pre-formed. I find no error in
the mathematics of any of the five parts. The two slips above are wording.

### P1.2 Two defects I do find, both outside (i)–(v)

**P1.2a — the stated numerical control is mis-specified, and in a way that is invisible to every
internal consistency check.** The "Status of Theorem A" paragraph tells the pilot to reproduce the
sealed full rows `full_P6pt0_d11` and `full_P6pt0_d12` **from `det(g)^4 (F_1 + F_2 + F_3)`** and
`det(g)^4 [u^{12}]`. This is the covariance of (i) applied in the wrong direction. The sealed rows
are `z^{[n]}(Y)` at the general point `Y`; the `F_k` live on the slice, which is `g.Y`, not `Y`; and
(i) reads `z^{[n]}(g.Y) = det(g)^4 z^{[n]}(Y)`. Therefore

    z^{[11]}(Y) = det(g)^{-4} (F_1 + F_2 + F_3),   z^{[12]}(Y) = det(g)^{-4} [u^{12}],

and the recipe as printed is wrong by a factor `det(g)^8` — **the same factor in both degree
families**, since both rows carry the same `det(g)^4` weight. It is worse than wrong by a constant:
`g` is built from an arbitrary basis `u_1, u_2` of `ker v` and arbitrary preimages `u_{k+2}`, so
`det(g)^8 != 1` is not even a fixed number — the printed recipe's output depends on choices the
theorem was designed to quotient out. The correct recipe is `g`-independent, as it must be.

**Prediction recorded before I look.** If pilot 2 implemented the paragraph as printed, then
(a) all six reconstructions fail while every *internal* check passes — the `S_3` signs of (iv), the
equality of the top across `k`, and the sign convention all compare slice quantities with slice
quantities and are blind to a `det(g)` power; and (b) the six failures share a single ratio
`reported / sealed = det(g)^8`, one rational number common to both degree families at the same
point. Item (a) is exactly the pattern my brief reports. Item (b) is testable and I will test it
first. If the six ratios are **not** all equal, a second, degree-dependent factor is present as
well — the natural candidate being a `nu` scale `s` entering as `s^n` at `nu`-degree `n`, which
would make the deg-11 and deg-12 ratios differ by one factor of `s`; that is the alternative I will
weigh against the `adapted_scale_u` / `nu`-sign hint.

**P1.2b — Corollary A.1 over-claims the cheap variant.** "both give, in addition, the degree-12
value at the same point" is false for the four-node option. Writing
`P(u) = u^8 (c_8 + c_9 u + c_10 u^2 + c_11 u^3 + c_12 u^4)`, the nodes `u = +-1, +-2` give four
equations in five unknowns; the odd part isolates `c_9, c_11` exactly (two equations, two unknowns),
so `F_1 = c_11` is recovered, but the even part leaves `c_8 + c_10 + c_12` and `c_8 + 4c_10 + 16c_12`
— two equations in three unknowns — so `c_12`, the degree-12 value, is **not** determined. Only the
five-node variant returns both rows. **The `15`-evaluation figure of C3 is therefore the correct
price for the full degree-11-plus-degree-12 functional, and the `12`-evaluation variant buys degree
11 alone.** C3's headline number survives; its parenthesis does not.

### P1.3 Notation, recorded not charged

The theorem statement writes the symmetry as `Y -> A Y A^{-T}`, the proof of (iv) as `Y -> P Y P^T`.
For a permutation matrix `A`, `A^{-T} = A`, so the two expressions are literally different maps
unless `sigma` is an involution. They agree once `A Y A^{-T}` is read as naming the *pair*
`(A, A^{-T}) in SL(A) x SL(B)` — whose action on `A (x) B = Mat` is
`Y -> A Y (A^{-T})^T = A Y A^{-1} = A Y A^T = P Y P^T` — which is plainly what is meant, and is what
the adjacent gloss "`det A det A^{-T} = 1`, `L`-invariance" is about. Notation only.

---

## P2 — the C9 counting, B20-01 §5.2

**Written 2026-09-18T00:32:43Z.** Formed from the *claim* only. At the moment of writing I have read
`b20_01_report.md` §§0–3, §§4.1–4.5, §5.1 and the first paragraph of §5.2 (through "For the degree-11
parts this fails on"), and nothing further. I have **not** read §5.2's derivation, §§6–8, §11, or any
pilot output. The claim as my brief states it: *any transversal slice of the flag cone carries a
function space of dimension `>= 17,640`, against the 70 of `F^L_{-1}`; and `U_-` mixes `z_{-1}` with
`z_{-2}`.*

Method: **INDEPENDENT (hand)** — every number below is derived here from the definitions and checked
by exact integer arithmetic done by hand, before the producer's derivation is opened.

### P2.1 What the relevant function space is

From Corollary A.2, `F_1^z` depends on `(Z_1, Z_2, Z)` only through `beta = Z_1^Z_2 in Lambda^2 W'` and
`gamma = Z_1^Z_2^Z in Lambda^3 W'`, with **bidegree `(3, 1)`** — three factors of `D_3 = beta^nu_1^nu_2^nu_3`
and one factor of `gamma^nu_2^nu_3`. So the ambient object is the multicone over the two-step flag
variety `Fl(2, 3; U)`, and "all functions of the relevant type" on it means the bidegree-`(3,1)` part of
its coordinate ring.

Dimension bookkeeping, re-derived: `dim Fl(2,3;U) = dim Gr(2,u) + dim Gr(1, u-2) = 2(u-2) + (u-3) = 3u-7`
for `u = dim U`; the multicone adds the two scalings, `3u - 5`. At `u = dim W' = 13` this is
`3·13 - 5 = 34`, which is the report's own `23 + 11 = 34`. Good — my reading of the object matches the
producer's.

By Borel–Weil (equivalently, the standard multi-cone coordinate-ring decomposition), the bidegree-`(a,b)`
part of the coordinate ring of the multicone over `Fl(2,3;U)` is the irreducible `GL(U)` module
`S_lambda(U^*)` with `lambda = (a+b, a+b, b, 0, ...)`. For `(a,b) = (3,1)`: **`lambda = (4,4,1)`.**

### P2.2 The number, derived independently

`dim S_{(4,4,1)}(C^u)` by the hook-content formula, `dim = prod_cells (u + j - i) / prod_cells hook(i,j)`.

Contents `j - i` of `lambda = (4,4,1)`: row 1 `0,1,2,3`; row 2 `-1,0,1,2`; row 3 `-2`.
Conjugate `lambda' = (3,2,2,2)`; hooks `lambda_i - j + lambda'_j - i + 1`:
row 1 `6,4,3,2`; row 2 `5,3,2,1`; row 3 `1`. Hook product `= (6·4·3·2)(5·3·2·1)(1) = 144 · 30 = 4320`.

At `u = 7`: numerator `= (7·8·9·10)(6·7·8·9)(5) = 5040 · 3024 · 5 = 76,204,800`, and
`76,204,800 / 4320 = 17,640` (check: `4320 · 17,640 = 73,440,000 + 2,764,800 = 76,204,800`). ✔

**So `17,640 = dim S_{(4,4,1)}(C^7)` exactly — the bidegree-`(3,1)` functions on the multicone over
`Fl(2,3; U)` for a *seven*-dimensional `U`.** I reproduce the producer's number on the nose, and I
therefore believe I have identified the object the producer counted. Two neighbouring values, for the
comparison I will want when I read the derivation: at `u = 8`, numerator `= (8·9·10·11)(7·8·9·10)(6) =
7920 · 5040 · 6 = 239,500,800`, dimension **`55,440`**; at `u = 13` (no slice at all), numerator
`= (13·14·15·16)(12·13·14·15)(11) = 43,680 · 32,760 · 11 = 15,740,524,800`, dimension **`3,643,640`**.

**Ruling P2 (a): the number 17,640 is CORRECT** as the dimension of the bidegree-`(3,1)` function space
on the flag multicone over a 7-dimensional subspace, and the comparison "against 70" is the right
comparison to make: `F^L_{-1}` is 70-dimensional (Prop. C), the slice method certifies vanishing of
*every* function of the type on the slice and never uses `L`-covariance, so it must control 17,640
dimensions where the covariant argument controls 70. The ratio is 252. The conclusion — that the
transversal-slice density method cannot substitute for an explicit basis of the 70-dimensional target —
**follows**, and follows a fortiori: the number is a floor only if no transversal slice is smaller than
`u = 7`, and every larger slice is worse (`55,440` at `u = 8`, `3,643,640` with no slice at all).

### P2.3 The one thing I will check against the derivation, flagged in advance

The claim is quantified "**any** transversal slice", so `17,640` is asserted as a **lower bound**. My
own arithmetic says the bound is attained at `u = 7` and grows with `u`; so the derivation must supply
the reason no transversal slice is smaller than `u = 7`. The obvious reason is a dimension count against
the group: `G' = L~ x| U_-` has 17 effective dimensions and the flag cone has 34, so a slice transversal
to the `G'`-orbits needs dimension `>= 34 - 17 = 17`. But the multicone over `Fl(2,3;U)` has dimension
`3u - 5`, which is `16` at `u = 7` and `19` at `u = 8` — **`u = 7` is one dimension short of 17**.
I therefore expect one of three things in §5.2, and I record the expectation now so that my agreement
cannot be retro-fitted: (a) the slice is not required to be of "flag cone over a subspace" shape, and
`17,640` is a genuine floor over a wider class of 17-dimensional slices; (b) the effective dimension of
`G'` on the *flag* cone is 18, not the 17 quoted for `S*`, making `u = 7` exactly transversal; or (c) the
`>=` is loose, `17,640` is quoted as the smallest number of the family rather than a proved infimum, and
the true floor is `55,440`. **In every one of the three, the conclusion of §5.2 stands**, because the
smallest candidate already exceeds 70 by a factor of 252. So I expect to rule the counting PROVED in
substance whatever the derivation says, and I am recording in advance that any defect I find here will
be a defect in the *justification of the "any"*, not in the load-bearing conclusion.

### P2.4 `U_-` mixes `z_{-1}` with `z_{-2}` — pre-formed reading

I expect this to be right and to be the real obstruction, for a reason I can state before reading it.
The grading in play is the `nu`-degree, i.e. the weight decomposition under the one-parameter subgroup
that defines the parabolic; `z_{-1}` is the `nu`-degree-11 piece and `z_{-2}` the `nu`-degree-10 piece,
one and two below the top `z_0 = z^{[12]}`. The Levi `L` preserves that grading — that is what makes
`F^L_{-1}` a well-defined 70-dimensional space and what Theorem A(i)–(iv) relies on. The unipotent
radical `U_-` does **not**: it strictly lowers the grading, so for `x in u_-`, `x · z_{-1}` has components
in `z_{-2}` and below. The previous session's degree-12 method could ignore this because `z_0` is the
**top** piece: `U_-` cannot move anything into it, so the top is `G'`-stable and a dense `G'`-orbit
argument closes on it. At `z_{-1}` the top-ness is gone, the `G'`-orbit of a degree-11 statement leaks
into degree 10, and a density argument on a `G'`-swept slice is no longer certifying the degree-11
statement alone. **Pre-formed ruling P2 (b): the `U_-` mixing claim is CORRECT and is the structural
reason the method does not transfer — not merely a cost problem.** If §5.2 presents the 17,640 as the
*only* obstruction, that is an understatement of its own case.

---
