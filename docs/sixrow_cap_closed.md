# The six-row cap: what closes it, what does not, and the `(5,7)` verdict

Session 48, branch `s48-theorems`, 2026-09-04, off `9aa6a9c`.
Pre-registration `results/PREREG_s48.md` (commit `902cccd`, **before any rank
or nullspace was computed**).  Code `analysis/wk9_s48_syz.py`,
`analysis/wk9_s48_syzfam.py`, `analysis/wk9_s48_syzprobe.py`,
`analysis/wk9_s48_ladder57.py`; logs `results/logs/s48_syz*.log`,
`results/logs/s48_ladder57_d10.log`; raw ranks `results/s48_ladder57.md`,
`results/s48_syzygy.md`.
Labels: **proved** / **measured** / **certified** / **expectation**.

## 0. Verdict

> **Target A — the six-row cap is still not closed, but the search is now
> narrowed to a proved boundary.**  `onset I(D_6^{det_4}) <= 666` remains
> *certified, not proved* (s44 §4).  Two new **proved identities** produce
> closed-form families of syzygies of the six partials, and both families turn
> out to be entirely Koszul.  More: the **complete** span of every
> `GL_4 x GL_4`-equivariant matrix word of `s`-degree 4 containing **one**
> adjugate factor — 822 words, spanning the six shapes that exist — yields
> **zero** new syzygies modulo the 90 Koszul, at two pencils and both house
> primes.  So the six extra syzygies are not of that shape, and the next
> shape up is vacuous: `q(s)·A_a ADJ(A_b,M,M) A_c` already spans all of
> `M_4 (x) S_4`.  **The one-adjugate word ansatz is exhausted and ruled out.**
>
> **Identity (I) (proved).**  For any pencil `M(s) = sum s_k A_k` of `4x4`
> matrices,
>
>     tr( adj(M) A_a adj(M) A_b )  =  (d_a F)(d_b F) − F · d_a d_b F ,
>
> `F = det M`.  The right side is **symmetric in `(a,b)`**, so every
> antisymmetric combination `sum_{a<b,c} x_{abc} s_c (A_a adj(M) A_b −
> A_b adj(M) A_a)` satisfies `tr(adj(M) W) ≡ 0` **identically, for every `x`
> and every pencil** — the whole 90-dimensional family lies in the
> Gulliksen–Négård kernel with no condition imposed.
>
> **Identity (II) (proved).**  With `P_B(M) = d/dt adj(M + tB)|_{t=0}`,
> `tr(P_B(M) M) = 3 d_B F`, and since `adj(M) M = F I`,
>
>     V_B  :=  M P_B(M) M  −  3 F B      has   tr( adj(M) V_B ) ≡ 0
>
> for **every** `B in M_4` and every pencil.  This is the branch s44 did not
> test — s44 ruled out only `𝒳 = B adj(M)`, giving `F·B − ¼(d_BF)M`.
>
> **Both are Koszul (measured, two pencils, both primes).**  Family (I) meets
> `L (x) S_4` in exactly a 6-dimensional space — the right *number*, which is
> why it had to be checked — and all six are Koszul.  Family (II) meets
> `L (x) S_4` in `0`.
>
> **The six are structurally confirmed and re-measured.**  `dim Syz_7 = 96 =
> 90 + 6`; the coefficient forms `G_k` lie in `J(M)_4` in **0** of 36 cases
> (`dim J(M)_4 = 66`), re-confirming s44; and `W(s) = sum G_k A_k` has full
> rank 4 at a generic `s` for all six.
>
> **What is now ruled out, permanently.**  A closed form for the six cannot be
> written as any linear combination of `l(s)·A_a adj(M) A_b`,
> `M P_B(M) M`, `F·B`, `phi_X(s)·M`, `l(s)·A_a P_{A_b}(M) M`,
> `l(s)·M P_{A_a}(M) A_b`, or `l(s)·M ADJ(A_a,A_b,M) M`.  Any closed form must
> use **at least two adjugate factors**, or leave the equivariant-word ansatz.
>
> **Target B — `C(r,5)` survives; `(r−4)(2r−9)` is refuted (certified).**
> At `(n, r, d) = (5, 7, 10)`, `rho_10 = 5880` and the determinantal rank is
> **5859** at three independent pencils and both house primes:
>
>     drop at (5,7)  =  **21**  =  C(7,5) ,     not 15 .
>
> The random-quintic control returned `rho_10 = 5880` at three seeds and both
> primes before any determinantal rank was read.  The Gulliksen–Négård ceiling
> at `d = 10` is `6173`, which is `293` **above** `rho_10`, so the ceiling does
> not bind and the test is clean.  Hence `C(r,5) = dim Λ^5 C^r` is confirmed at
> `r = 4, 5, 6, 7`, and
>
>     cap(n, r)  =  dim Sym^{3n−5} C^r − h_{3n−5}(n, r) ,   drop = C(r, 5)
>
> is statable as a general conjecture with the same proof shape as `cap(n)`.

## 1. Target B — the discriminating rank *(certified at explicit pencils)*

`d = 3n − 5 = 10`, `n = 5`, `r = 7`.  Matrix shape **6468 x 8008**:
rows `r · dim S_{d−n+1} = 7 · C(12,6) = 6468`, columns `dim S_10 C^7 = C(16,6)
= 8008`.  The brief's `12012 x 8008` mixes two degrees: `12012 = 7 · C(13,6)`
is the row count at `d = 11` (whose column count is 12376).  Pre-registered
prediction **B3** at prior 0.85, confirmed.

**Ceiling check, run before any determinantal rank (proved).**  For `n = 5`
the `(n−1)`-minor ideal is codim 4 and generically perfect, with the
Gulliksen–Négård resolution
`0 -> S(−10) -> S(−6)^25 -> S(−5)^48 -> S(−4)^25 -> S`, giving
`H_{S/J(M)}(10) = 1835` and ceiling `dim J(M)_10 = 8008 − 1835 = 6173`.
`6173 − 5880 = +293`: the ceiling is **not** binding, so — unlike `(3,6)`,
`(4,7)`, `(4,8)` — the measured drop is the mechanism's own and not forced.

| stage | seed | `p` | shape | rank | `rho_10` | drop |
|---|---|---|---|---|---|---|
| random quintic control | 0 | 2147483647 | 6468 x 8008 | 5880 | 5880 | 0 |
| random quintic control | 0 | 2147483629 | 6468 x 8008 | 5880 | 5880 | 0 |
| random quintic control | 1 | both | 6468 x 8008 | 5880 | 5880 | 0 |
| random quintic control | 2 | both | 6468 x 8008 | 5880 | 5880 | 0 |
| **determinantal** | 0 | 2147483647 | 6468 x 8008 | **5859** | 5880 | **21** |
| **determinantal** | 0 | 2147483629 | 6468 x 8008 | **5859** | 5880 | **21** |
| **determinantal** | 1 | both | 6468 x 8008 | **5859** | 5880 | **21** |
| **determinantal** | 2 | both | 6468 x 8008 | **5859** | 5880 | **21** |

Also read, and consistent: at `d = 9` (`3234 x 5005`, `rho_9 = 3087`) the
determinantal rank is `3087` — **no drop below `d = 3n−5`**, as at every other
`(n,r)` in the ladder.

**Direction of inference, and the label.**  A rank modulo `p` at a point is a
*lower* bound on the generic rank, so `rank = 5859` gives
`generic determinantal rank >= 5859` and, with `rho_10 = 5880` as the universal
upper bound, `drop <= 21`.  The drop being **at least** 21 — i.e. the rank
really falling below 5880 generically — is certified only in the s44 sense: it
is the reading at three independent pencils and two primes, not a multimodular
certificate.  Pre-registered **B4** predicted no certificate would be
affordable, at prior 0.80, and that is the outcome: the s44 `d = 7` certificate
at size 666 cost 7.6 minutes per pencil over ~1790 primes; at size 5880 the
Hadamard exponent is 8.8x larger and the matrix 60x bigger, which is days.  So
this row is labelled **certified at explicit pencils modulo `p`** — one label
weaker than s44's `d = 7`, exactly as pre-registered.

The Schwartz–Zippel reading is the same shape as s44's: each `5880 x 5880`
minor is a polynomial of degree `5 · 5880 = 29400` in the pencil entries, so a
uniform pencil from `±10^6` kills a nonzero one with probability at most
`1.5·10^{-2}` per pencil — which is why three pencils and two primes, not one,
and why the label is *certified* and not *proved*.

**The formula this selects.**  `C(r,5) = 0, 1, 6, 21` at `r = 4, 5, 6, 7`
against measured `0, 1, 6, 21`.  `(r−4)(2r−9) = 0, 1, 6, 15` — **refuted at
`r = 7`**.  `C(r−3,2) = 0, 1, 3, 6` was already out at `r = 6`.  Pre-registered
**B1** put `P(21) = 0.55`; confirmed.

`C(r,5) = dim Λ^5 C^r` is the reading that survives, and it gets the `r = 4` leg
for a reason — `Λ^5 C^4 = 0`, and the generic determinantal hypersurface in
`P^3` is smooth, so the rank never drops at any degree (s44, 31 rows).  Whether
the drop *is* `Λ^5 L` as a `GL(L)`-module is the content of Target A and is
**not** settled here.

## 2. Target A — the two new identities *(proved)*

Write `M = M(s)`, `F = det M`, `d_k = d/ds_k`.  A syzygy
`sum_k G_k d_kF = 0` with `G_k in S_4` is the same thing as
`W = sum_k G_k A_k in L (x) S_4` with `tr(adj(M) W) ≡ 0`, since
`d_kF = tr(adj(M) A_k)` (Jacobi).

**Identity (I).**  For `M` invertible, `adj(M) = F M^{-1}`, so

    d_l ( F M^{-1} )  =  (d_lF) M^{-1} − F M^{-1} A_l M^{-1} ,

whence `d_k d_l F = d_l tr(adj(M) A_k) = (d_lF)(d_kF)/F − F tr(M^{-1}A_l M^{-1}A_k)`
and, clearing `F` (both sides are polynomials, so the identity extends from the
open set),

    tr( adj(M) A_a adj(M) A_b )  =  (d_aF)(d_bF) − F · d_a d_b F .        (I)

The right side is symmetric in `(a,b)` — the first term visibly, the second by
symmetry of the Hessian.  Therefore, for **any** `x_{abc}` antisymmetric in
`(a,b)`,

    W  =  sum_{a<b, c} x_{abc} · s_c · ( A_a adj(M) A_b − A_b adj(M) A_a )

has `tr(adj(M) W) = sum x_{abc} s_c (T_{ab} − T_{ba}) = 0` identically. ∎

**Identity (II).**  Let `P_B(M) = d/dt adj(M + tB)|_{t=0}`.  Differentiating
`tr(adj(X) X) = 4 det X` at `X = M` in direction `B` gives
`tr(P_B(M) M) + tr(adj(M) B) = 4 d_BF`, i.e. `tr(P_B(M) M) = 3 d_BF`.  Since
`adj(M) M = F I`,

    tr( adj(M) · M P_B(M) M )  =  F · tr( P_B(M) M )  =  3 F d_BF
    tr( adj(M) · F B )         =  F d_BF ,

so `V_B := M P_B(M) M − 3 F B` satisfies `tr(adj(M) V_B) ≡ 0` for every
`B in M_4`. ∎

(I) explains, structurally, why s44's family was Koszul: `F·A_i − ¼(d_iF)M` is
the `𝒳 = B adj(M)` branch, and (I) says the whole *other* branch collapses to a
symmetry statement.  (II) is that other branch, made explicit.

## 3. What the families actually give *(measured — two pencils, both primes)*

For each family the two conditions **(i)** `W in L (x) S_4` and **(ii)**
`tr(adj(M)W) = 0` are solved simultaneously, and the solution is compared with
the 90 Koszul syzygies.  `analysis/wk9_s48_syzfam.py`;
`results/logs/s48_syzfam.log`.

| family | words | syzygies found | **new mod Koszul** |
|---|---|---|---|
| `l(s) · A_a adj(M) A_b` (contains all of (I)) | 216 | **6** | **0** |
| `M P_B(M) M` (identity (II)) | 16 | 0 | 0 |
| `F · B` | 16 | 0 | 0 |
| `phi_X(s) · M`, `phi_X = tr(adj(M)X)` | 16 | 0 | 0 |
| `l(s)·A_a P_{A_b}(M) M`, `l(s)·M P_{A_a}(M) A_b` | 432 | 222 | 0 |
| `l(s) · M ADJ(A_a,A_b,M) M` | 126 | 0 | 0 |
| **all six together** | **822** | **432** | **0** |

The first row is the striking one and the reason (I) had to be tested at all:
the family meets `L (x) S_4` in a space of dimension exactly **6**, the size of
the answer — 1260 conditions on 90 unknowns having a 6-dimensional kernel is
not an accident — and yet all six are Koszul.

**The ansatz is exhausted.**  The equivariance constraint is sharp: under
`M |-> PMQ` one has `L |-> PLQ`, `adj(M) |-> det(PQ) Q^{-1} adj(M) P^{-1}`,
`F |-> det(PQ) F`, so a matrix word transforms as `W |-> det(PQ)^a P W Q` —
which is what `tr(adj(M)W) = 0` requires — **exactly** when it alternates
`L`-elements and adjugates, beginning and ending with an `L`-element.  At
`s`-degree 4 with one adjugate factor there are precisely the six shapes above
(sorted by how many of the five slots `X adj(Y_1,Y_2,Y_3) Z` are `M` rather
than a constant `A_a`, times the complementary monomial in `s`), and the table
covers all of them.  The next shape, `q(s)·A_a ADJ(A_b,M,M) A_c` (4536 words),
was built and its span measured: **2016 of 2016**, i.e. all of `M_4 (x) S_4`.
It imposes nothing and is not an ansatz.  So one-adjugate words are finished:
they do not contain the six, and there is no informative one-adjugate family
left to try.

## 4. The six themselves *(measured; `analysis/wk9_s48_syzprobe.py`)*

At a fresh pencil, both primes:

| quantity | value |
|---|---|
| `dim Syz_7` (left kernel of `M_7`, `756 x 792`) | **96** |
| `dim Koszul` (`C(6,2)·dim S_1`) | **90** |
| non-Koszul | **6** |
| `dim J(M)_4` (ideal of the sixteen `3x3` minors) | 66 of 126 |
| coefficient forms `G_k` lying in `J(M)_4` | **0** of 36 |
| `rank W(s)` at a random `s`, over the six | `4, 4, 4, 4, 4, 4` |

Both s44 probes reproduce exactly: the `G_k` are outside `J(M)_4`, and `W(s)`
does not factor through a degenerate part of the pencil.

## 5. Status of the cap, and where a next session should push

`onset I(D_6^{det_4}) <= 1197` is a theorem (s44 Theorem A).
`onset I(D_6^{det_4}) <= 666` is **certified, not proved**, exactly as s44 left
it; nothing in this session weakens or strengthens that label.  The bracket is
unchanged:

    9  <=  onset I(D_6^{det_4})  <=  666 .

Pre-registered **A1** (find all six in closed form) was given prior 0.30 and is
**not** achieved.  **A4** (the `𝒳 = adj(M)B` branch contains them) was given
prior 0.40 and is **refuted** — that branch is identity (II), and it meets
`L (x) S_4` in zero.  **A2/A3** (the `GL(L)`-equivariance type) were not
settled: the honest reason is that the type is not detectable by transporting
one pencil, because the syzygy space transports canonically
(`W'(s) = W(gs)` under a basis change `g` of `L`), so deciding between `L` and
`Λ^5 L` needs a *construction*, which is precisely what is missing.  The
`Λ^5` reading does, however, gain independent support from Target B: the drop
is `C(r,5) = dim Λ^5 C^r` at `r = 4, 5, 6, 7`.

**Three concrete leads for the next session, in order.**

1. **Two adjugate factors.**  §3 proves the six are not one-adjugate words.
   The smallest two-adjugate equivariant shapes at `s`-degree 4 are
   `A_a ADJ(A_b,A_c,M) A_d ADJ(A_e,A_f,M) A_g` times a linear form and its
   relatives; the search space is large but the shape is now forced, and the
   span dimension should be measured *first* to discard the vacuous ones (the
   §3 discipline).
2. **Do `r = 5` first.**  There the extra syzygy is **unique up to scale**
   (drop 1), hence canonically attached to the pencil, and it is Dimca's node
   defect: the 20 nodes of the generic five-parameter determinantal quartic fail
   by exactly 1 to impose independent conditions on cubics in `P^4`
   (`35` cubics, 20 nodes, only 19 conditions).  A closed form for *one*
   syzygy in a `350 x 330` problem is a far smaller target than six in
   `756 x 792`, and any formula found there is the thing to generalise.
3. **Test `Λ^5 L` at `r = 7`.**  Target B now supplies a 21-dimensional space
   at `(5,7)`.  If the six at `(4,6)` are `Λ^5 L`, the 21 at `(5,7)` are
   `Λ^5 C^7`, and the two must be related by the same construction — a
   consistency test no single `r` can provide.
