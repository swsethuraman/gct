# B19-02 — One explicit equation construction for the five-variable determinant locus

15 September 2026. Slot 02, batch 19, worktree `work/batch15_workers/B15-02`.
Author: Claude (Opus 5). Theory first; two declared bounded pilots in §5.

**Provenance, recorded before any write:**

```
git rev-parse HEAD          ba1ec94ab94cb84aec36b1386bd9a5b9c73bcce3
git rev-parse HEAD^{tree}   44f159394a3748920d7e9fa0a7f954d909ff7918
git status --porcelain      only untracked B15 runtime logs under results/logs/
```

No other git command was run.

## 0. Plain terms, and the verdict up front

B17 proved that some determinant equation with exactly five rows fails on the
padded permanent. Nobody has written one down. This slot picks **one**
construction, states it explicitly, and pushes it until it either produces the
equation or provably cannot.

The construction I chose is the **invariant-theoretic one**: `I(D45)` is the
kernel of the pullback along the parametrisation `phi(B) = det(sum_k x_k B_k)`,
and the image of that pullback lands inside the ring of `SL4 x SL4`
semi-invariants of five `4x4` matrices — the semi-invariant ring of the
5-Kronecker quiver at dimension vector `(4,4)`. Counting dimensions in that ring
gives a **rigorous, explicit, closure-correct existence criterion**: if the
invariant ring is smaller than the ambient space in some degree, a determinant
equation exists in that degree. No elimination is involved; the criterion is a
comparison of two computable integers.

**The verdict is negative, and it is quantified.** In the four-variable case,
where the truth is known — the determinantal locus is a hypersurface of degree
320112 — the criterion **provably cannot fire below degree 320112**, and the
measured gap at the degrees I can compute is growing, not shrinking: at `d = 12`
the invariant ring is already **75.8 times larger** than the ambient space, and
that factor rises with every degree I computed. The same computation in five
variables shows the same behaviour. So this construction cannot produce the
missing equation at any reachable degree, and I say so plainly rather than
reporting the criterion as progress.

What survives is worth keeping, and it is stated as theorems rather than hopes:

1. the criterion itself, PROVED and cheap, together with exactly what makes it
   weak — the semi-invariants of weight `>= 2`, which lie in the target ring but
   not in the coordinate ring of `D45`;
2. a **certification scheme** (§7): the one rigorous way the programme has to
   promote a *sampled* rank drop into a *proved* determinant equation, with its
   exact hypothesis;
3. the precise **missing lemma** that certification needs (§7.3);
4. a corollary tightening the programme's own bound: combining the batch-18
   degree-five sweep with the four-variable literature, `I(D45)_d = 0` for
   `d <= 5`, so **the first five-variable determinant equation has degree at
   least six** (§8).

Plan: §1 intake and conventions; §2 the construction, explicitly; §3 why its
consequences vanish on the entire closure; §4 the counting theorem; §5 the two
declared pilots and the measurements; §6 the verdict; §7 what survives, and the
missing lemma; §8 the lower bound; §9 the padded example and which lemma
excludes it; §10 the smallest linear-algebra problem, priced before computing;
§11 claims, negatives, one next test.

## 1. Intake, conventions, and what is ADOPTED

Read in full or in the named sections: `B15-01/docs/b18_01_report.md` (revision 2,
§§3, 5, 6), `B15-10/docs/b18_10_review.md` (§§4.1–4.5, 9),
`B15-03/docs/b17_03_report.md`, `B15-01/docs/b17_01_report.md`, the B19 preamble
and the B19 board.

Conventions are the preamble's, unchanged: forms in `Sym^4(V*)`, coefficient
ring `Sym(Sym^4 V)`, **ordinary** coefficients `c_alpha = [x^alpha] F` with
positive weights, and `E_ij c_alpha = (alpha_i + 1) c_(alpha + e_i - e_j)` when
`alpha_j > 0`. Where a Kronecker number appears I say every time which one: `g`
is the **ordinary** rectangular Kronecker coefficient `g(lambda, (d^4), (d^4))`
and `s` is the **symmetric** one, transposition included, with `s <= g`.

Five-variable objects, as in B18-01 §2 and B18-10 §9:

- `W5 = Sym^4((C^5)*)`, of dimension 70; `A(d) := dim Sym^d(W5*) = binom(69+d, d)`.
- `phi : (Mat_4)^5 -> W5`, `phi(B) = det(sum_{k=1..5} x_k B_k)`; 80 parameters.
- `D45 = closure(im phi)`, `dim D45 = 50` (ADOPTED, B18 settled).
- `P_5 = closure{(z per_3) o T : T in Hom(C^5, C^10)}`, the honest five-variable
  restriction of `X_pad`, `dim P_5 = 39`; at length five and **only** there,
  `P_5 = R135 = {l C}` by B17-01-A dominance (ADOPTED, B18-10 §9). I use `P_5`
  language everywhere and never evaluate on a product above five variables.
- `F* = x_0 · C*` with `C*` a smooth cubic threefold: an actual padding point
  outside `D45` (ADOPTED, B17-01-C, with its smoothness and frame certificates).

ADOPTED inputs, each with the justification that travels with it:

| label | statement | justification carried | holds in my regime? |
|---|---|---|---|
| 03-A | for `ell(lambda) <= r`, highest-weight spaces and restriction kernels identify between `GL_r` and `GL16` | B17-03 Lemma 2 (arbitrary `T`, not just frames) | yes: I work at `r = 5` only |
| 01-C | `F* not in D45` | B17-01, smooth cubic threefold + frame certificate | yes, used only as a point test |
| Prop 5.2 | `I(D45) = ker phi^*`, degreewise | B18-01 §5.2, elementary | yes, and it is the core of §3 |
| LLV | the four-variable linear determinantal locus `D44` is a hypersurface of degree 320112 | Leal–Lozano Huerta–Vite, arXiv:2303.09028, Table 2 / Theorem 2; secondary quotation, **not verified against the primary text in this session** | used only as a calibration control and in §8, flagged CONDITIONAL both times |

The `MN = F·I_4` criterion is **not** used anywhere: it was withdrawn in B18-01
§5.1 and rejected in B18-10 §4.4, and the reason — it forces only
`det M · det N = F^4`, so `M = l·I_4` is a false witness — is exactly why the
construction below never quantifies over auxiliary matrices. I also make no claim
that `deg P(D45)` is the only route; that was withdrawn in B18-01 §6.1.

## 2. The construction, explicitly

**Variables.** Two sets, and nothing else.

- Coefficient variables `c_alpha`, one for each `alpha in N^5` with
  `|alpha| = 4`: **70** of them. A quartic is `F = sum_alpha c_alpha x^alpha`.
- Parameter variables `b^{(k)}_{ij}`, `k = 1..5`, `i,j = 1..4`: **80** of them,
  the entries of the five matrices `B_k`.

**Equations of the construction.** The graph of `phi`, in the 150 variables:

    c_alpha = phi_alpha(B) := [x^alpha] det( sum_k x_k B_k ),    |alpha| = 4.

Each `phi_alpha` is a polynomial of degree 4 in the `b`, and — this is used in
§10 — of degree **at most one in each individual entry** `b^{(k)}_{ij}`, because
the determinant is multilinear in the rows of the matrix of linear forms.

**The object.** `I(D45) = ker phi^*` where `phi^*(c_alpha) = phi_alpha`
(B18-01 Prop 5.2). Degreewise, `I(D45)_d = ker(phi^*_d)`, so a determinant
equation of degree `d` is exactly a polynomial relation of degree `d` among the
70 polynomials `phi_alpha`.

**The target ring, which is where the construction gets its leverage.** For
`P, Q in GL_4` with `det P · det Q = 1` we have

    det( sum_k x_k (P B_k Q) ) = det P · det Q · det( sum_k x_k B_k ) = phi(B),

so every `phi_alpha` — hence every element of `im phi^*` — is invariant under
`SL_4 x SL_4` acting by `B_k -> P B_k Q`, and also under the transposition
`B_k -> B_k^T`. Therefore

    im phi^*_d  ⊆  R_d := ( C[(Mat_4)^5]_{4d} )^{SL_4 x SL_4} ,

the weight-`d` piece of the semi-invariant ring of the 5-Kronecker quiver at
dimension vector `(4,4)`. Its first fundamental theorem (Derksen–Weyman;
Schofield–Van den Bergh; Domokos–Zubkov; the degree bound in Derksen–Makam) says
`R` is spanned by the coefficients of `det(sum_k X_k ⊗ B_k)` for `X_k` of size
`t x t`, `t <= 3`, with `t = 1` giving exactly our 70 functions `phi_alpha`.
**None of my proved statements below depends on that theorem**; it is quoted to
explain *why* the construction is weak (§6), and is a secondary quotation, not
verified against a primary text in this session.

So the construction is: the subalgebra `A_1 ⊆ R` generated by the 70 weight-one
semi-invariants is `C[D45]`, and `I(D45)` is the kernel of the presentation of
that subalgebra. No auxiliary matrix is quantified over, no `N = adj M` appears,
and there is no existential quantifier anywhere — which is what the withdrawn
criterion got wrong.

## 3. Why the consequences vanish on the entire closure, not on a sample

This is the point on which the withdrawn criterion failed, so I state it as a
lemma with its proof rather than a remark.

**Lemma 3.1 (PROVED; = B18-01 Prop 5.2, restated for this construction).**
Let `h in Sym^d(W5*)` satisfy `phi^*(h) = 0` as a polynomial in the 80 entries.
Then `h` vanishes at **every** point of `D45`, including every boundary point not
of the form `det(sum x_k B_k)` for any finite `B`.

*Proof.* `phi^*(h) = h ∘ phi`, so `phi^*(h) = 0` says `h` vanishes on `im phi`.
The zero set of `h` is Zariski closed, so it contains `closure(im phi) = D45`. ∎

Three consequences, each of which is exactly what an incidence-style criterion
has to get right:

- **Limits are free.** No separate argument about boundary points is needed. The
  limits B17-01 warns about, "whose matrix entries cannot be specialized to
  finite matrices", satisfy `h` because vanishing propagates to the closure by
  continuity of `h`, not by any property of `B`.
- **No false witness is possible.** The failure of `MN = F·I_4` was that a pair
  `(l·I_4, C·I_4)` satisfies the condition while `det(l·I_4) = l^4 != F`. Here
  there is nothing to witness: a point `F` is tested by *evaluating* `h` at `F`.
  `F* = x_0 C*` fails whichever `h` we produce, or it does not, and that is a
  number, not an existential.
- **The converse holds too**, so nothing is lost: `I(D45)_d = ker phi^*_d`
  exactly, so this construction reaches *every* determinant equation, not a
  sub-family. Any equation the programme is missing is in this kernel.

The price of Lemma 3.1 is that `phi^*(h) = 0` is a polynomial identity in 80
variables. §5 is about avoiding that identity, and §10 prices what it costs when
it cannot be avoided.

## 4. The counting criterion

**Notation.** `A(d) = binom(69+d, d) = dim Sym^d(W5*)`, and

    R_d = ( C[(Mat_4)^5]_{4d} )^{SL_4 x SL_4},    r(d) = dim R_d .

**Lemma 4.1 (PROVED).** `r(d) = sum_{rho ⊢ 4d} 5^{ell(rho)} chi_{(d^4)}(rho)^2 / z_rho`,
a finite sum of rationals whose value is a nonnegative integer.

*Proof.* Cauchy: `Sym^{4d}(C^16 ⊗ C^5) = ⊕_{mu ⊢ 4d, ell(mu) <= 5} S_mu(C^16) ⊗ S_mu(C^5)`.
For each `mu`, `S_mu(C^4 ⊗ C^4) = ⊕_{alpha,beta} g(mu,alpha,beta) S_alpha(C^4) ⊗ S_beta(C^4)`,
and `S_alpha(C^4)` is `SL_4`-trivial iff `alpha` is the rectangle `(d^4)`, when it
is one-dimensional. Hence
`r(d) = sum_{mu} g(mu,(d^4),(d^4)) · dim S_mu(C^5)`. Substituting
`g(mu,R,R) = sum_rho chi_mu(rho) chi_R(rho)^2 / z_rho` and using Schur–Weyl in the
form `sum_{mu, ell(mu) <= 5} chi_mu(rho) dim S_mu(C^5) = 5^{ell(rho)}` gives the
stated formula. ∎

**Theorem 4.2 (PROVED — the criterion).** If `r(d) < A(d)` then
`I(D45)_d != 0`: a determinant equation of degree `d` exists.

*Proof.* `C[D45]_d ≅ im phi^*_d ⊆ R_d` by §2, so
`A(d) - dim I(D45)_d = dim C[D45]_d <= r(d)`. If `I(D45)_d = 0` this reads
`A(d) <= r(d)`. ∎

**Corollary 4.3 (CONDITIONAL on LLV and 03-A).** If in addition `d < 320112`,
then `I(D45)_d` contains a highest-weight vector of length **exactly five**.

*Proof.* `I(D45)_d` is a nonzero `GL5`-submodule, so it has a highest-weight
vector of some type `lambda ⊢ 4d` with `ell(lambda) <= 5`. If `ell(lambda) <= 4`,
then by 03-A it restricts to a nonzero element of `I(D44)_d` in four variables.
`I(D44)` is generated by one polynomial of degree 320112 (LLV), so
`I(D44)_d = 0` for `d < 320112`, a contradiction. ∎

**Theorem 4.4 (PROVED — the cell-level form).** In a cell `(d, lambda)` with
`ell(lambda) <= 5`, `m_det(d,lambda) <= s(lambda) <= g(lambda)`, where
`g(lambda) = g(lambda,(d^4),(d^4))` is the **ordinary** rectangular Kronecker
coefficient and `s` its transposition-symmetric refinement. Hence
`a(lambda) > g(lambda)` implies `i_det(d,lambda) >= a - g >= 1`.

*Proof.* The `S_lambda(C^5)`-multiplicity of `R_d` is `g(lambda)` by the proof of
Lemma 4.1; `C[D45]_d` is a submodule of `R_d`; the transposition invariance of
`phi^*` puts the image in the `Z_2`-fixed part, of multiplicity `s`. ∎
(This is B18-01's Claim 6.1 with the labelling correction B18-10 §4.1 requires:
the displayed bound is `g`; only the refined form is `s`; `m_det <= s <= g`.)

The criterion has the two properties the slot asks for: it is **explicit** — two
computable integers — and it is **closure-correct**, because Theorem 4.2 is
proved through Lemma 3.1 and not through any property of individual matrices.
What remains is whether it ever fires at a reachable degree. That is §5 and §6.

## 5. Two declared pilots, and the measurements

**Why a computation was necessary.** Theorem 4.2 is only useful if `r(d) < A(d)`
happens at a reachable degree. That is a question about two integers, and no
amount of theory answers it. Both pilots are one process, one BLAS thread, under
`analysis/b15_bound.py --seconds 60 --memory-mb 512`. Script
`analysis/b19_02_counting.py`, SHA-256
`05c2d6a1fe091d9f2fe94667bada4111db8f80a214b33fcffb7d5825988e3023`, unchanged
after the runs. All arithmetic is exact (`Fraction`/`int`).

**Controls first** (`results/b19_02/controls.json`, 0.05 s). Six, all passed,
two of which had to fail:

| control | required | outcome |
|---|---|---|
| `r_5(1) = 70`, `r_4(1) = 35` | equals `dim Sym^4(C^n)` | pass — the weight-one invariants are exactly the determinant's own coefficients |
| `S_m` row orthogonality, `m <= 8` | 1 | pass |
| `rho`-sum vs `mu`-sum, `n = 4,5`, `d <= 3` | equal | pass — two independent routes to `r(d)` |
| **wrong rectangle `(d^3)`** | **must not** give 70 | **rejected** (it gives a different number), so the formula really tests the `SL4 x SL4` rectangle condition |
| **corrupted character value** | **must** break integrality or the value | **rejected** |

**Pilot 1 — the object, `n = 5`** (`results/b19_02/sweep_n5_*.json`):

| `d` | `A(d)` | `r(d)` | `r/A` | fires? |
|---:|---:|---:|---:|---|
| 1 | 70 | 70 | 1.000 | no |
| 2 | 2485 | 3585 | 1.443 | no |
| 3 | 59640 | 156080 | 2.617 | no |
| 4 | 1088430 | 5639705 | 5.182 | no |
| 5 | 16108764 | 166330074 | 10.33 | no |
| 6 | 201359550 | 4021730350 | 19.97 | no |
| 7 | 2186189400 | 80842488650 | 36.98 | no |
| 8 | 21042084900 | 1373270443700 | 65.26 | no |
| 9 | 182364537500 | 20029899534800 | 109.8 | no |
| 10 | 1440680682000 | 254512930716340 | 176.7 | no |
| 11 | 10477677064000 | 2854036242078350 | 272.4 | no |
| 12 | 70724320184250 | 28567510572002850 | 403.9 | no |

**Pilot 2 — the calibration control, `n = 4`, where the answer is known**
(`results/b19_02/sweep_n4_*.json`): `r_4/A_4` runs 1.000, 1.222, 1.739, 2.695,
4.321, 6.938, 10.98, 16.98, 25.63, 37.69, 54.09, **75.82** at `d = 12`.

In both cases the ratio `r/A` is **increasing at every step computed**, so the
criterion is moving away from firing, not towards it.

Local exponents make the shape explicit. Writing `growth = X(d+1)/X(d)` and
`K_X = (growth - 1)·d`, the ambient has `K_A = 69` exactly for `n = 5`
(`A(d+1)/A(d) = (70+d)/(d+1)`) and `K_A = 34` for `n = 4`. The invariant ring has
`K_r` measured at 142.5, 139.1, 133.7, 127.9, 122.3, 117.1, 112.4, **108.1** for
`n = 5` at `d = 5..12`, and 57.5 … **52.5** for `n = 4`. Since `R` has Krull
dimension `80 - 30 = 50` (resp. `64 - 30 = 34`), `K_r` must fall to 49 (resp. 33)
eventually, and only then can `A` overtake `r`. At `d = 12` it is still 108
against 69.

**Cap record.** `d >= 13` did not fit: the two runs attempting `d = 1..12` in one
process both died with `MemoryError` under the 512 MiB Job Object (receipts
`b19_02_n5`, `b19_02_n4`, exit code 1, 440 MiB peak). Splitting `d = 11, 12` into
their own processes succeeded (246 and 486 MiB peaks). A cap hit is recorded as a
cap hit: it is not a mathematical statement about `d >= 13`.

## 6. The verdict: this construction cannot produce the equation

**Claim 6.1 (PROVED, conditional on LLV).** In four variables the criterion
cannot fire at any degree below 320112.

*Proof.* The four-variable analogue of Theorem 4.2 has the same proof:
`r_4(d) < A_4(d)` implies `I(D44)_d != 0`. By LLV, `I(D44)` is generated by one
polynomial of degree 320112, so `I(D44)_d = 0` for `d < 320112`. Contrapositive:
`r_4(d) >= A_4(d)` for every `d < 320112`. ∎

This is the decisive measurement of the construction's strength, and it is not an
extrapolation. In the **one case where the answer is known**, the criterion is
provably silent across 320111 degrees, and the measured ratio at the top of my
computed range (`r_4/A_4 = 75.8` at `d = 12`, rising) shows it is nowhere near
firing there. Whether it fires *at* 320112, where the first equation actually
appears, is not decidable by any computation I can run; the trend says it does
not, because `r_4/A_4` must first climb down from 75.8 and it is still climbing.

**Claim 6.2 (MEASURED inputs, HEURISTIC output — NOT PROVED).** Fitting
`K_r(d) = K_inf + c·d^(-alpha)` to the last four computed local exponents, with
`K_inf` the Krull-dimension value (49 for `n = 5`, 33 for `n = 4`), and
integrating `d log(r/A) / d log d = K_r - K_A`, gives
(`analysis/b19_02_extrapolate.py`, `results/b19_02/extrapolation.json`):

| case | fitted `alpha` | crossover estimate | truth |
|---|---:|---:|---|
| `n = 5` (the object) | 0.746 | `7.0·10^2` | unknown |
| `n = 4` (control) | 0.558 | `1.3·10^18` | **320112** |

The four-variable line is the one that matters: **the procedure overshoots the
known answer by a factor of `4.1·10^12`**, twelve to thirteen orders of
magnitude. That is the same failure mode, and the same order of unreliability,
as the refined-Bézout route this programme already discounted (which the preamble
records as fourteen to fifteen orders in the same control). I therefore attach no
weight to the five-variable figure of 703 and do **not** report it as a degree
bound of any kind. It is recorded only so the reviewer can see that the procedure
which would produce it is untrustworthy exactly where it can be checked.

**Why it is weak, structurally.** `im phi^* = C[D45]` is the subalgebra of `R`
generated by the 70 weight-one semi-invariants. `R` also contains the
semi-invariants of weight 2 and 3 — the coefficients of `det(sum_k X_k ⊗ B_k)`
for `X_k` of size 2 and 3 (FFT, cited in §2) — and their products. Every one of
those inflates `r(d)` without inflating `C[D45]_d`. The criterion compares `A(d)`
with the whole of `R_d` and so pays for all of them. At `d = 2` in five
variables the overpayment is already `3585 - 2485 = 1100` dimensions, and by
`d = 12` the target ring is 404 times the ambient space.

**Verdict.** As an instrument for producing the missing five-row equation, the
construction **fails**, for a reason that is quantified rather than guessed. I
record that plainly, as the assignment permits. What it does establish is stated
next, and it is not nothing.

## 7. What survives, and the exact missing lemma

### 7.1 The certification scheme

The construction does deliver one thing the programme needs: the only rigorous
way it has to promote a *sampled* rank drop into a *proved* equation.

**Theorem 7.1 (PROVED).** Fix a cell `(d, lambda)`, `ell(lambda) <= 5`. Let
`h_1..h_a` be a basis of the highest-weight space `H_lambda`, let
`B^(1)..B^(N)` be points of `(Mat_4)^5`, and let `E` be the `a x N` matrix
`E_{ji} = h_j(phi(B^(i)))`. Let `B := min(a, s(lambda))` be the ceiling of
Theorem 4.4. Then

    rank E  <=  rank phi^*_lambda  <=  B ,

and **if `rank E = B` then `ker E = ker phi^*_lambda = K_det(d,lambda)` exactly**:
every vector of `ker E` is a determinant equation vanishing on the whole of
`D45`, and `i_det(d,lambda) = a - B`.

*Proof.* `E` factors as evaluation after `phi^*_lambda`, giving the two
inequalities, the second by Theorem 4.4. If `rank E = B` then
`rank phi^*_lambda = B`, so `dim ker phi^*_lambda = a - B = dim ker E`, and
`ker phi^*_lambda ⊆ ker E` forces equality. Vanishing on the closure is
Lemma 3.1. ∎

Two directions of use, and only these:

- **`a <= s`** (every cell the programme has measured): the ceiling is `a`, so
  the scheme can only certify `rank = a`, i.e. `i_det = 0` — it **closes** cells.
  That is exactly what the batch-18 degree-five sweep did, 23 cells for 23.
- **`a > s`**: the scheme certifies `i_det = a - s >= 1` **and hands over the
  equations explicitly**. No cell with `a > s` is known; §5 shows why — the
  totals run the other way by a factor of 404 at `d = 12` and rising.

A sampled rank drop *below* the ceiling certifies nothing, in either direction.
That is not a limitation of this scheme; it is the programme's standing rule.

### 7.2 What the programme's `b` actually is

The programme writes `B = min(a, s - b)` and has never certified a useful `b`
("`s - b = a` in all twenty certified controls"; "a usable `b` needs `b = s`").
The construction identifies that quantity exactly.

**Proposition 7.2 (PROVED).** In a cell `(d, lambda)`, write `A_1 = C[D45]` for
the subalgebra of `R` generated by the 70 weight-one semi-invariants. Then

    m_det(d,lambda) = mult( S_lambda , (A_1)_d ),
    s(lambda) - m_det(d,lambda) = mult( S_lambda , (R_d / (A_1)_d) )   [transposition-fixed part],

so the boundary loss `b` the programme is trying to certify **is** the
`S_lambda`-multiplicity of the quotient of the semi-invariant ring by the
subalgebra generated by the determinant's own coefficients.

*Proof.* Both are restatements of `im phi^*_d = (A_1)_d` (§2) and Theorem 4.4. ∎

This is a definition-level identification, not a deep theorem, and I flag it as
such. Its value is that it replaces an analytic question — how much of the
orbit's function space fails to extend across the boundary — with an explicit
algebraic one whose generators are known: the weight-`>= 2` semi-invariants
`det(sum_k X_k ⊗ B_k)`, `X_k` of size 2 and 3. Those are written down, finite,
and testable.

### 7.3 The missing lemma, stated exactly

> **Missing Lemma.** Exhibit one cell `(d, lambda)` with `ell(lambda) = 5` and a
> subspace `V ⊆ R_{d,lambda}` of dimension `m` such that `V ∩ (A_1)_{d,lambda} = 0`
> and `s(lambda) - m < a(d,lambda)`.

Such a `V` gives `b >= m`, hence `B = min(a, s - b) <= s - m < a`, hence
`i_det >= a - (s - m) >= 1` **with an explicit equation module**, by Theorem 7.1
applied with the improved ceiling. The natural candidate for `V` is the image in
`R_{d,lambda}` of the products of weight-`>= 2` generators with weight-one ones;
what is missing is a proof that any such image direction is *not* already a
polynomial in the weight-one generators. Nothing in the tree, and nothing here,
proves a single such direction is new.

This is the same wall the boundary-arc route hits, reached from the other side.
Stating it this way makes the obstruction explicit rather than atmospheric: it is
not that the boundary is hard to analyse, it is that no one has exhibited one
semi-invariant direction provably outside `C[D45]` in a named cell.

## 8. A lower bound the programme did not have

**Corollary 8.1 (PROVED, conditional on LLV and 03-A).** `I(D45)_d = 0` for
every `d <= 5`. Equivalently, **the first five-variable determinant equation has
degree at least six**.

*Proof.* Let `0 != h in I(D45)_d`, `d <= 5`, and take a highest-weight vector of
type `lambda ⊢ 4d`, `ell(lambda) <= 5`. If `ell(lambda) <= 4` then by 03-A it
restricts to a nonzero element of `I(D44)_d`, which is zero for `d < 320112`
(LLV). So `ell(lambda) = 5`. Five-row cells do not occur for `d <= 4`
(B18-01 §8.1, ADOPTED), so `d = 5`. Batch 18's degree-five sweep settled all 23
five-row cells at `d = 5`: 22 have `m_det = a` — certified by exact nonzero
integer evaluations of the unique highest-weight vector at actual determinant
points — and the rectangle `(4^5)` had `m_det` undetermined, its inherited exclusion
being by padding vanishing, which bounds `m_pad` and says nothing about `m_det`.
So `h` would have to live in `(4^5)`. **That cell is closed in §8.1 below.** ∎

### 8.1 The last degree-five cell, closed here (MEASURED / PROVED)

`analysis/b19_02_rect.py`, SHA-256
`26f66bc4b592cc37b84b43254bf61c2df499402a97cb7575556b50d61d9de805`, one capped
process, 19.7 s, 123 MiB peak, exit 0; certificate
`results/b19_02/rect_4_4_4_4_4.json`.

| quantity | value |
|---|---|
| `a`, by the Weyl alternant computed in-script | **1** |
| weight-space dimension `K` | 19834 |
| Casimir factors used | 85 |
| raising operators `E_12, E_23, E_34, E_45` | source weight `(4,4,4,4,4)` dim 19834, target weights `(5,3,4,4,4)` etc., each **target dim 17329, 51723 nonzero entries** |
| exact highest-weight vector | primitive integer, 19834 nonzeros, max abs 41472, reconstructed from 2 primes |
| exact raising residues | all zero over `Z` |
| exact values at three determinant points | `-481390358496125537`, `6830962538921450404`, `4457433896125063706` |

The operator census is reported because a vacuous check is the failure mode the
preamble names: these operators have nonempty targets **and** 51723 nonzero
entries each, so annihilation is a real condition. The first prime left the
rational reconstruction undetermined; that attempt is recorded in the
certificate's `lift_attempts`, and the second prime completed it.

A nonzero exact integer value at an actual determinant point gives
`m_det >= 1 = a`, hence `i_det = 0` in `(4^5)`. The three padding values were
all zero, which I use for **nothing**: a sampled zero proves nothing, and the
inherited padding ceiling `U = 0` already gives `m_pad = 0` in this cell.

So Corollary 8.1 holds with no exception: **`I(D45)_d = 0` for all `d <= 5`.**

Paired with B18-01's Theorem 3.5 (`d <= 4^49`), the bracket on the first
five-variable equation is now `6 <= d_5 <= 4^49`, with the lower end certified
and the upper end an existence statement that the preamble already instructs us
never to treat as a budget.
