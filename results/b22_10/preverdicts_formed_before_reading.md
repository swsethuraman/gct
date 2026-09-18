# B22-10 — verdicts formed before reading the deliverable's own defence

Byte-preserved. Nothing below is edited after the corresponding defence is opened; corrections
appear only in `docs/b22_10_review.md`, with a pointer back to the entry here.

Session start state (read-only git, recorded before any write):

```
git rev-parse HEAD          f7727cb731ee7e3f474e0985ed8e1227100a8f0a
git rev-parse HEAD^{tree}   1c09cdda36cd78db8b69002fd2d107bbcd4e0f73
git status --porcelain      ?? results/logs/b15_10_runtime_native_20260913.pid
                            ?? results/logs/b15_10_runtime_native_20260913_resources.json
recorded at                 2026-09-18T16:14:34Z
```

---

## P1 — Theorem M (B22-01 §2.1), from the statement

**Written 2026-09-18T16:16:37Z.** Formed from `docs/b22_01_report.md` at `53bdb31e…` (sha256
`e2adc0f9adfa98e322baa0e5093b598a554b7bc3a9cb13ec18f2fd5cb7b2ac2e`), §§0–1 (pre-registration) and
§2 through the end of §2.1 (the statement) only. Not yet opened: §§2.2–2.5 (the proofs), §§3–6,
any `results/b22_01/` data file, the B22-02 report, the B22-12 ledger. Method: **READ**, with the
checks below derived by hand.

### P1.1 The multidegree list is derivable, and I derive it

Legs: `a` 0, `r` 1, `c` 1, `S` 2, `K` 2. Character of a slot under
`L = {(diag(alpha,g), diag(beta, c g^T))}` (Y -> A Y B): `a` `alpha beta`; `r` `alpha c`; `c` `beta`;
`S`, `K` `c`; ten `eps_3` contractions of the 30 legs give `det(g)^10`. A pattern of multidegree
`(#a,#r,#c,#S;#K)` therefore transforms by
`alpha^{#a+#r} beta^{#a+#c} c^{#r+#S+#K} det(g)^{10}`, and is `L`-invariant iff this is a power of
`alpha beta c^3 det(g)^2` — the only characters trivial on `L`. That forces `#r = #c`,
`#a + #r = t`, `#r + #S + #K = 3t`, `2t = 10`, so `t = 5`. With `#a + 2#r + #S + #K = 20`:
`#a = 5 - r`, `#S = 4 - r` (`#K = 11`) or `3 - r` (`#K = 12`). Each column is an antisymmetrisation
over five positions, and `a` is one coordinate, so a column carries at most one `a`: `#a <= 4`,
hence `r >= 1`. Result: `(4,1,1,3;11), (3,2,2,2;11), (2,3,3,1;11), (1,4,4,0;11)` and
`(4,1,1,2;12), (3,2,2,1;12), (2,3,3,0;12)` — **exactly the report's seven blocks**. So the list is
derived, not chosen; I will check whether §2 says so.

### P1.2 Parts (i)–(iii), from the statement

**(i) membership — expect PROVED.** `L`-invariance is the character count above plus the easy
direction of invariant theory (an `eps`-product is `SL_3`-invariant); no FFT is needed for it.
`GL_5`-semi-invariance of weight `det^4` is immediate from `D(g.Y) = det(g) D(Y)`. Landing in
`S_lambda(W^*) (x) det^4` needs the Cauchy decomposition identifying the `det^4`-isotypic part of
`C[W (x) C^5]_{20}` with `S_{(4^5)}(W^*) (x) det^4` — **load-bearing, classical**.
**(ii) spanning — expect PROVED, on three classical inputs, all load-bearing:** (a) every
`det^4`-semi-invariant of degree 20 is a quartic form in `D` (Plücker generation / FFT for `SL_5`);
(b) complete reducibility of `L`, so the invariants of the typed-multilinear-form space are the image
of a Reynolds projection of a spanning set; (c) FFT for `SL_3`: invariants of `std^{(x)30}` are spanned
by products of ten `eps` (no dual legs occur, so no `delta`). Plus the multidegree derivation of P1.1
for the torus part. **Cauchy** enters (i), not (ii).
**(iii) the structured formula — expect PROVED.** On an `F_1`-tuple `D = u^2 (D_2' + u D_3)`
(B21-10 §2.1), so each column sees only `nu`-degree 2 or 3; four column `K`-counts summing to 11 with
each in `{2,3}` is forced to `{2,3,3,3}`, and the top needs `{3,3,3,3}`. The 2-`K` column's
non-`K` slots see `Z_1 ^ Z_2 ^ Z` (gamma), the 3-`K` columns' see `Z_1 ^ Z_2` (beta). Consistent with
B20-01 Cor. A.2's bidegree `(3,1)`.

### P1.3 Part (iv) — expect CONDITIONAL, and the condition is named

The determinant certifies **dim >= 70** (lower half) independently of `arc_target`. "Are bases"
needs **dim <= 70**, the upper half of `b_L(11) = 70` (and of `b_L(12) = 4`), which only `arc_target`
§5.1 supplies (single lineage). **The upper half is load-bearing for the decision, not only for the
word "basis":** if `dim F^L_{-1} > 70`, seventy points cannot be injective on `V_70`, and a relation
holding at them would not be a polynomial identity. The §1.3 span control (coordinates from the 70
points predicting 10 recorded points) is **MEASURED** evidence for the upper half as it bears on the
three runner functions, not a proof. Expected ruling: **Theorem M (i)–(iii) PROVED; (iv) CERTIFIED
for the lower half, CONDITIONAL on `arc_target`'s upper halves for "basis" and for injectivity**, unless
§2 or the data supply a second lineage for the upper halves. **The count 70 is matched, not derived:**
§1.1 says the search keeps patterns until the block reaches `arc_target`'s target and stops; the
blocks' targets `7, 31, 28, 4` and `1, 2, 1` are inputs. What would convert "matched" into "derived"
is an independent upper bound — e.g. extra random patterns never raising a block above target
(MEASURED), or an independent character computation (PROVED).

### P1.4 The `F_P` inference, from the statement

Valid as pre-registered in §1.2, given the upper half: integer points and integer `Xi_h` make `E` an
integer matrix, so `det E != 0 mod P` gives `det E != 0` over `Q`; `det E` a `P`-unit makes the
coordinates of any integer `F_1^z` in the basis `P`-integral (Cramer), so the `F_P` statement follows.
**Without the upper half, neither the `Q` nor the `F_P` injectivity follows.**

---

## P2 — B22-02 Lemmas 1.2–1.6 and Fact 1.7, from their statements

**Written 2026-09-18T16:19:20Z.** Formed from `docs/b22_02_report.md` at `e22a41b1…` (sha256
`b41e4265809a018750286d6eda416d62c4f4044b3fdb7cbac2cc51caf50593e4`): §1.1 and the statements at
lines 94–98, 101–106, 117–134, 144–161, 162–167, 181–186. Not yet opened: the proofs at lines
107–116, 135–143, 168–180, the table §1.3, §§1.4–6. Two disclosures: a `grep` for the word "Proof"
displayed line 99, Lemma 1.2's one-line proof, before I pre-formed; and Lemma 1.5 and Fact 1.7
carry their arguments inside the statement, so for those two I pre-formed on the argument too.
Method: **READ**, each check re-derived by hand.

**Lemma 1.2 — expect PROVED** (trivial; open nonempty subset of an irreducible space).

**Lemma 1.3 — expect PROVED as stated, with a scope caveat.** Every polynomial without constant
term in the `r x r` minors vanishes where the rank is `< r`; Plücker coordinates of `ker M` and
`im M`, computed from a fixed choice of `r` rows/columns, are `r x r` minors. **Caveat:** the rational
map `F -> ker M(F)` may extend across the rank-drop locus once a common factor of all the minors on
`D45` is divided out; covariants built from that *normalised* kernel are not polynomials in the minors
and are not covered. The lemma is right; its use as a kill must not claim those.

**Lemma 1.4 — expect PROVED, all three parts.** (a) weight `t - 5 beta_1 <= -1` on `x_1 C`, so
`P5` is in the `SL_5`-nullcone and every positive-degree invariant — in particular every equation of
`D45` in a rectangular cell — vanishes on it. (b) `Psi(lambda(s)F)` has all `s`-exponents `<= -e`; matching
monomials of `lambda(s)Psi(F)` gives `t - 5 beta_1 <= -e`, i.e. `x_1^{ceil((t+e)/5)} | Psi(x_1 C)`. (c)
`4e = 3 + 5k`; the row bound — constituents of `Sym^e(Sym^4 V)` have at most `e` rows, true because
`Sym^e(Sym^4 V) ⊂ (Sym^4 V)^{(x) e}` and by Pieri/Kostka `h_4^e` has only constituents of length `<= e` —
gives `e >= 5`; `4e ≡ 3 mod 5` gives `e ≡ 2 mod 5`, so `e >= 7`; (b) with `t = 3` gives `l^2 | Psi(l C)`, so
`Psi(l C) = l^2 m ∈ D35`. I find no gap.

**Lemma 1.5 — expect PROVED; both numbers replayed by hand.** (i) At `A = diag(1,1,1,0)`,
`det(A+B) = sum_{S ∋ 4} det B[S,S] · prod_{i∉S} a_i`: the linear term is `b_44`, and on `b_44 = 0` the
quadratic term is `-sum_{i<=3} b_{i4} b_{4i}`, three hyperbolic pairs, **rank 6**, with `A` in the
radical. Pull-back along linear `Lambda` preserves this, so `rank II_F <= 6` on a space of dimension
`N - 2`. (ii) Second partials of `det_4` are the 36 signed `2 x 2` minors, pairwise disjoint in monomial
support, so **rank 36**; `Cat(F) = (Sym^2 Lambda)^T Cat(det_4) (Sym^2 Lambda)`. Vacuous iff `N <= 8`
(`N - 2 <= 6`; `N(N+1)/2 <= 36`). The direction remarks are right: rank is l.s.c., `{rank II <= 6}` is
closed and padding's is larger (right way); `z per_3`'s second partials span at most `9 + 9 = 18 < 36`
(reversed).

**Lemma 1.6 — expect the containment and the restriction PROVED; the "right-way" clause to be
checked.** `l · det_3 M(x) = det_4 diag(l, M(x))`, so `{l·C : C ∈ D35} ⊆ D45` (closure included), and
`C -> f(l·C)` is a nonzero element of `I(D35)_d`. The size-65 minors of `M_4(C)` (`75 x 70`): at a
smooth cubic the partials are a regular sequence, rank `75 - 10 = 65`, cokernel `5 = [t^4](1+t)^5`. On a
generic `C ∈ D35` (six nodes, `P^4 ∩ Seg(P^2 x P^2)`), Dimca's formula with `nd - 2n - 1 = 3` gives
`c_4 = mu_4 + def_1(N) = 5 + (6 - 5) = 6` if the six nodes span `P^4`, so rank `64` and the 65-minors
vanish on `D35`. **I expect this derivation, or an equivalent, to be needed; if the proof instead rests
on an unread "cap theorem at `n = 3`", that clause is CONDITIONAL.** Note that the clause, even if
proved, is about the *restricted* problem (`D35` against all cubics) and does not produce an element of
`I(D45)` nonzero on padding: restriction goes one way only.

**Fact 1.7 — expect PROVED.** The degree `4 · 3^3 = 108` is right for quartics in four variables; the
section of `l·C` by `H ≠ {l=0}` is reducible and singular along a curve, and `H = {l=0}` gives `0`;
Bertini gives `Delta_F ≠ 0` for generic `F ∈ D45`. Reversed direction; a correct kill.

---
