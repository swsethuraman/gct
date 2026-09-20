# B24-04 — Small tails, canonical bases, and whether 70 objects carry a charge

20 September 2026 (UTC). Slot 04, batch 24, worktree `work/batch15_workers/B15-02`, branch
`b15-02-a1-probes`. Author: Claude (Opus 5, 1M context). Theory first. Three wrapped pilots of the
three allowed.

**Provenance, recorded before any write (2026-09-20T03:18Z):**

```
git rev-parse HEAD      feed104ea865ed5f76809f6d77455060af01433c   (= the starting HEAD in the launch prompt)
git status --porcelain  ?? results/logs/b15_02_runtime_native_20260913.pid
                        ?? results/logs/b15_02_runtime_native_20260913_resources.json
                        ?? results/logs/b15_02_runtime_preflight_run_20260913T062637Z.pid
                        ?? results/logs/b15_02_runtime_preflight_run_20260913T062637Z_resources.json
```

The same two commands at the end of the session give the same HEAD and the same four pre-existing
receipts, plus only this slot's own new files (§7). Read-only git. No commit, no push, no stash.

**Notation (G13, G24).** As B23-06 at `feed104e`. `m = 3` throughout unless stated. `r` is the
length (number of rows of `λ`); `d` the degree of the equation; `n` the determinant size.
`D_r^{det_n}` and `P_r` are the `r`-variable determinantal locus and the `r`-variable restrictions
of `x_0^{n-3} per_3`, both closures, both irreducible, both cones. `λbar = (λ_2, λ_3, …)` is the
tail and `t = |λbar|`. `N_S(λ)` is the dimension of the `λ`-weight space of `Sym^d(Sym^n C^r)`.
Every dimension below is a **vector-space dimension** (affine); no projective dimension is used.

---

## 0. What this slot is and is not

**It is** three answers about structure rather than size:

- **§2** a theorem, with its arithmetic control, that settles Question 1 in the negative and
  replaces B23-06's open "which number is the real price" with a number;
- **§3** the Bläser–Dörfler–Ikenmeyer paper read at source and hashed, its two relevant theorems
  quoted, and a ruling on whether small treewidth is B23-06's small tail (it is not, and the place
  they part is itself a new priced question);
- **§4** the 70 patterns of B22-01's Missing Theorem enumerated, eight statistics tried on them,
  and one grading found — the one already latent in the record — with every other candidate killed.

**It is not** an obstruction, an equation, a separation, a gap, a cell nomination, a new instrument
or a batch recommendation. **No cell is nominated.** Nothing here is a statement about Kronecker
coefficients, about plethysm in general, or about any weight space other than the one named.

**The four findings a reader should take away.**

1. **A separating equation cannot live in a small-tail cell (§2, Theorem 1, PROVED).** If a cell's
   tail `t` is smaller than its degree `d`, every weight vector in it is `c_{n e_1}^{d-t}` times a
   weight vector of degree `t`, and the separating property passes intact through that factor. So
   the tail of any separating cell is at least `D*`, the onset degree of separation. The cheap
   cells are the old cells in disguise. **Question 1 is answered, negatively.**
2. **The real price is about `4·10^10`, not `621` and not `10^150` (§2.4, EXTRAPOLATION over a
   measured quartic).** B23-06 left two candidate prices. Neither is right: the minimum over the
   evaluated shapes grows like `t^4` and, at the tail `900` that Conjecture 2 forces, gives about
   `4·10^10`. The programme's reach is `N_S ≲ 2·10^4`, which in tail units is `t ≈ 24` (pilot 3,
   MEASURED).
3. **Small treewidth is not small tail (§3, Lemma 2 and the ruling).** Small tail *implies* small
   treewidth (`τ ≤ t + λ_2 − 1`, PROVED here); the converse fails outright, and treewidth depends on
   the *filling* while the tail depends only on `λ`. The published theorem prices one *evaluation*,
   never *existence*, so it does not price Question 1. It does leave one corner open, and that
   corner is new: large tail with small treewidth (§3.4).
4. **The 70 patterns carry exactly one grading, and it is the multidegree (§4).** `F^L_{-1}`
   decomposes as `7 ⊕ 31 ⊕ 28 ⊕ 4` by `#a`, and the decomposition is a genuine direct sum
   (PROVED, pilots 1 and 3). Seven further statistics were tried; ten of the eleven classes that
   could have refined it are PROVED trivial, one remains a MEASURED candidate of codimension 1 in a
   single 7-dimensional block. **The basis itself is not canonical** (§4.2). A negative, as
   expected.

---

## 1. Pre-registration

Three pre-registrations, each written and hashed **before** its pilot was written or run, each
asserted by its own pilot, whose output prints the hash (G25):

| file | sha256 | asserted in |
|---|---|---|
| `results/b24_04/PREREG_b24_04_p1.md` | `e77a79e1a36a03d8075606f01c27d1d987a2eeb766999ad986b2eec31b071519` | pilot 1's stdout and JSON |
| `results/b24_04/PREREG_b24_04_p2.md` | `c62d96141bcb0cd8e37786858c0932448e7d5006ab3f10d9ad9f1bd25e4a2d7f` | pilot 2's stdout and JSON |
| `results/b24_04/PREREG_b24_04_p3.md` | `7b52ea97be3732eb3a4166206bfa5ff13c3169d950dc0e45c4d9ab0078de46d8` | pilot 3's stdout and JSON |

Pilot 2 was written after pilot 1's output was read, and pilot 3 after pilot 2's; each pins its
predecessors' outputs by sha256 and asserts them (§7). The pre-registrations fix, before any run:
the operational criterion for "a statistic grades the space"; the list of statistics (pilot 1) and
of classes (pilots 2 and 3), with the explicit undertaking that no statistic and no class is added
after seeing results; and the direction in which a modular rank may be used (G27).

**The criterion, fixed in pre-registration 1.** A statistic `st` **grades** `F^L_{-1}` iff the
subspaces `V_{≤j} := span{h : st(h) ≤ j}` form a **proper** filtration. `V_{≤j}` is the span over
*all* patterns with `st ≤ j`, not over a sample. Hence a sampled rank that **reaches** the ambient
dimension **proves** the filtration is not proper there (a rank is a floor); a sampled rank that
stays **below** is MEASURED only and is never reported as a grading. This asymmetry is the whole
reason the negatives below are proved and the one survivor is not.

**Budget.** Three wrapped pilots, 60 s / 512 MiB each, 180 s in total; each priced in this report
before it was launched (§7). No unwrapped run of any size (G19). Producer-only (G18): one session,
one lineage, except where a value is cross-checked against an independently produced record number,
which is said at the point of use.

**The batch's one numerical job.** `..\B15-01\results\logs\b24_02_*.pid` and every sibling
checkout's `results/logs/b24_05_*.pid` were checked before each of the three launches. Before
pilot 1 no `b24_02_` or `b24_05_` pid existed at all; before pilots 2 and 3,
`b24_02_p1_n5_kleiman.pid` existed with pid 6052, whose receipt records `exit_code 0` after
0.198 s and whose pid was confirmed not running. No launch overlapped another job.

---

## 2. Question 1 — can a separating equation live in a small-tail cell?

### 2.1 The question, made precise

B23-06 §2.3 (at `feed104e`) proved **Lemma 2.3**: for `λ = (nd − t, λbar)` with the tail held
fixed, `N_S(λ)` is nondecreasing in `d` and **constant for `d ≥ t`**. So small-tail cells are cheap
at every degree, and B23-06 closed with: *"can a separating equation at `(3,n)` lie in a cell with
small tail? … The padding side allows it; the Pieri condition bounds the tail above by `3d`, not
below. Nothing on record bounds it below."*

Write

> `D* := min { deg f : f ∈ I(D_r^{det_n}), f|_{P_r} ≠ 0 }`

for the **onset of separation** at `(3, n)` in `r` variables (`D* = +∞` if no separating equation
exists — which at `n = 5, 6` is possible, B23-06 §1). "Small tail" is then only meaningful relative
to something, and the thing it must be relative to is `D*`. Question 1 is: **is there a separating
cell with `t` small while `d` is large?**

### 2.2 Theorem 1 (PROVED, elementary)

> **Theorem 1.** Let `λ ⊢ nd` with tail `t = |λbar|`, and suppose `t < d`. Then:
>
> **(i)** every element of the `λ`-weight space of `Sym^d(Sym^n C^r)` is of the form
> `c_{n e_1}^{\,d-t} · g` with `g` in the `μ`-weight space at degree `t`, where
> `μ = λ − (d−t)·n e_1 = (t(n−1), λbar)`; and `g ↦ c_{n e_1}^{d-t} g` is a bijection between the
> two monomial bases, so the two weight spaces have the same dimension;
>
> **(ii)** `f` is an equation of `D_r^{det_n}` nonzero on `P_r` **iff** `g` is;
>
> **(iii)** consequently `D* ≤ t`.
>
> **Corollary.** Every cell carrying a separating equation has `t ≥ D*`. Equivalently: for every
> `t < D*`, **no cell with tail `t` carries a separating equation, at any degree.** And every
> separating equation is `c_{n e_1}^{k}` times one whose cell has **tail exactly equal to its
> degree**.

*Proof.* Coordinates on `Sym^n C^r` are the `c_α`, `α` a degree-`n` exponent vector; the
`λ`-weight space at degree `d` has as basis the multisets `{α_1, …, α_d}` with `Σ α_i = λ`. Write
`ᾱ = (α_2, …, α_r)`. Then `Σ_i |ᾱ_i| = Σ_{j≥2} λ_j = t`, and `α = n e_1` exactly when `ᾱ = 0`, so
**at least `d − t` of the `α_i` equal `n e_1`**. Every basis monomial is therefore divisible by
`c_{n e_1}^{d-t}`, which gives the factorisation; deleting exactly `d − t` copies of `n e_1` is a
bijection onto the multisets of `t` vectors summing to `μ`, which gives (i). (This is B23-06's
Lemma 2.3 upgraded from a count to a map.)

For (ii): `D_r^{det_n}` and `P_r` are irreducible, so `I(D_r^{det_n})` is prime. The coefficient of
`x_1^n` vanishes identically on neither:
- on `D_r^{det_n}`, `F = det_n(Σ_{i≤r} x_i A_i)` has `c_{n e_1}(F) = det_n(A_1)`, nonzero at
  `A_1 = I`;
- on `P_r`, substituting `x_0 ↦ x_1` and the permanent's diagonal entries `↦ x_1`, the rest `↦ 0`,
  gives `x_1^{n-3} · x_1^3 = x_1^n`, so `c_{n e_1} = 1`.

Hence `c_{n e_1} ∉ I(D_r^{det_n})` and `c_{n e_1}|_{P_r} ≠ 0`. From `f = c_{n e_1}^{d-t} g`:
`f ∈ I` iff `g ∈ I` (primality), and `f|_{P_r} ≠ 0` iff `g|_{P_r} ≠ 0` (irreducibility of `P_r`).

(iii) is immediate: `g` separates and has degree `t`, so `D* ≤ t`. For the corollary, let `f`
separate in a cell of degree `d` and tail `t`. If `t ≥ d` then `t ≥ d ≥ D*` by the definition of
`D*`. If `t < d` then `D* ≤ t` by (iii). Either way `t ≥ D*`. And in the reduced object `g`, the
tail is still `t` while the degree is now `t`, so tail `=` degree. ∎

**Two remarks, kept separate from the theorem.**

- Theorem 1 is about arbitrary weight vectors, not only highest weight vectors, which is why it is
  stated that way. A cell `(λ, d)` carries a separating equation iff it carries a separating
  *highest* weight vector; the theorem then hands back a separating equation of degree `t`, whose
  own highest weight vector need not have weight `μ`. Only `D* ≤ t` is claimed, and only that is
  used.
- The map `g ↦ c_{n e_1}^{d-t} g` is **not** `GL_r`-equivariant (`c_{n e_1}` is a weight vector,
  not an invariant). The proof does not need equivariance; it needs primality and irreducibility
  only. Whether `a(λ)` at degree `d` equals `a(μ)` at degree `t` is **not** claimed here and is not
  used anywhere below.

### 2.3 What Theorem 1 does to B23-06's two numbers

B23-06 offered `621` (the cheapest five-row cell at `(3,5)`, `d = 5`, `λ = (17, 2^4)`) and
`10^150.4` (the average weight space at `d ≥ cap(5) = 900`) and said which is real "depends on
whether a separating equation can live in a small-tail cell, and nobody has asked."

**Neither is the real price.** By Theorem 1:

- The `621` cell itself has `t = 8 > d = 5`, so Theorem 1 does not reduce it; it is excluded by
  the floor already on record, `deg = 5 < 8 ≤ D*` (B23-06 §2.2, from B22-02 L6 transferred through
  `l^{n-3} det_3 M = det_n diag(l, …, l, M)`). What Theorem 1 excludes is the regime that made
  `621` look like a price at all: a *small tail carried to large degree*. Every such cell has
  `t < d`, so it reduces to a cell of degree `t`, and if `t < D*` that cell carries nothing.
  **The cheap cells are empty.**
- The `10^150.4` is an *average* over all cells at degree `900`, and averages were never the
  binding number. The binding number is the **minimum over cells that Theorem 1 does not exclude**,
  i.e. over cells with tail `≥ D*`.

So the question B23-06 left open is closed, and it is replaced by a different and answerable one:
*what is the cheapest cell with tail at least `D*`?* That is §2.4.

### 2.4 The price (pilot 3 part B)

By Theorem 1 the search may be confined to cells with tail `=` degree, where `N_S` is the value
Lemma 2.3 calls stable. Pilot 3 computes it by dynamic programming and, as control **C1**,
reproduces three values B23-06 produced independently at `feed104e` (§2.3 of that report):

| `n` | `λbar` | `d` | B23-06 | pilot 3 | |
|---|---|---|---|---|---|
| 4 | `(2,2,2,2)` | 5 | 553 | 553 | agree |
| 5 | `(2,2,2,2)` | 5 | 621 | 621 | agree |
| 6 | `(2,2,2,2)` | 5 | 641 | 641 | agree |

Control **C2** checks the counting half of Theorem 1 by *literal enumeration* of the weight-space
monomials, independently of the dynamic programme, at `(n,r,d,λbar) = (3,3,5,(1,1))` and
`(3,4,6,(1,1,1))`: in both, every monomial contains `n e_1` at least `d − t` times, and the count
at degree `d` equals the count at degree `t`. No counterexample.

**Control C3, the price.** Stable `N_S` at `n = r = 5`, minimised over four-part tails `λbar ⊢ t`
(all shapes for `t ≤ 16`; two shapes at `t = 18…24`, so those rows are a minimum **over the shapes
evaluated**, never a proved global minimum):

| `t` | min `N_S` | argmin | max `N_S` |
|---|---|---|---|
| 4 | 15 | `(1,1,1,1)` | 15 |
| 8 | 231 | `(5,1,1,1)` | 687 |
| 12 | 1 189 | `(9,1,1,1)` | 23 222 |
| 16 | 3 829 | `(13,1,1,1)` | 650 106 |
| 20 | 9 492 | `(17,1,1,1)` | 14 979 308 |
| 24 | 19 921 | `(21,1,1,1)` | 295 797 207 |

**The programme's reach, in tail units.** B23-06 calibrated the reach at `N_S ≲ 2·10^4` per wrapped
pilot. The table says that is `t ≈ 24` at the cheapest shape, and very much less at a typical one
(`t ≈ 11` at the maximum shape). **MEASURED.**

**The extrapolation.** The minimum grows like a quartic, and structurally so: the argmin
`(t−3,1,1,1)` puts almost all of the tail on one coordinate, where the count is governed by
partitions into parts of size `≤ n = 5`, which grow like `t^{n-1}/((n−1)!·n!)`. The measured
constant `min N_S / t^4` is `0.0573, 0.0584, 0.0593, 0.0600` at `t = 12, 16, 20, 24`. Taking
`0.060` at the tail `900` that Conjecture 2 forces gives

> **min `N_S` ≈ 4·10^10 at `t = 900`. EXTRAPOLATION** — a quartic fitted on `t = 12…24` and
> evaluated 37-fold outside that range. It is not MEASURED and it is not PROVED. It is offered
> because the two numbers on record were `621` and `10^150.4`, and the truth is neither.

Against a reach of `2·10^4`, the gap is about `10^6` — six orders, not a hundred and forty-six.
**CONDITIONAL** on Conjecture 2 (the onset of `I(D_5^{det_n})` at `cap(n)`, an *expectation* on the
record, not a theorem). Unconditionally, with only the proved floor `D* ≥ 8`, the corresponding
number is `min N_S ≥ 231`, which is inside the reach — so the unconditional statement is that
**Theorem 1 excludes every cell with tail below 8, and no more.**

### 2.5 Verdict on Question 1

**Answered, negatively, and priced.** A separating equation cannot lie in a cell whose tail is
below the onset degree; the cheapness of small-tail cells at high degree is exactly the cheapness
of the low-degree cells they are multiples of. The feasibility estimates at `(3, n ≥ 5)` that this
question governed should use the tail-`≥ D*` minimum, not the whole-cell average and not the
cheap-cell figure.

---

## 3. Question 2 — does the published tractability result price Question 1?

### 3.1 The source, read and hashed (G14, G14′)

The integrator supplied this item by web search, labelled SECONDARY until read. It is now read at
source.

> **Markus Bläser, Julian Dörfler, Christian Ikenmeyer, *On the complexity of evaluating highest
> weight vectors*, arXiv:2002.11594, CCC 2021.**
>
> - PDF **v2**, `https://arxiv.org/pdf/2002.11594v2`, sha256
>   `5371f3b62964f221b248334bec54d453a5bdcca4f2980c854cee41183f1317b6`, 513 636 bytes, 33 pages.
> - The text read is the **ar5iv HTML rendering**, sha256
>   `31c8a74500d961b8e60e29daf8a780917700a1ad2fa1f2a5f383b1b454cde23b`, 1 630 516 bytes, fetched
>   2026-09-20. As on previous slots, the ar5iv rendering does not state which arXiv version it
>   renders, and the local environment cannot extract text from the PDF; so **PRIMARY at the level
>   of the HTML rendering of a hashed paper whose PDF v2 is also hashed.** Both files are in the
>   session scratchpad under `lit/`, not in the tree (G9: hash and reachable URL given).
> - Version history from the abstract page, quoted: "[v1] Wed, 26 Feb 2020", "[v2] Mon, 15 Feb
>   2021"; "Comments: 32 pages, full version".
>
> Abstract, quoted in full where load-bearing: "…we prove the NP-hardness of the evaluation of HWVs
> in general, and we give efficient algorithms if the treewidth of the corresponding Young-diagram
> is small, where the point of evaluation is concisely encoded as a noncommutative algebraic
> branching program!"

**A correction made inside this session, recorded because it is exactly the failure mode G14′ is
for.** A delegated reader, asked to quote §7, returned the graph definition together with the
gloss *"Critical point: Edges depend on the shape only, not the filling."* I re-checked the
sentence myself in the fetched rendering. The text is:

> "Let `S` be an arbitrary Young tableau containing the numbers `{1,…,n}`. We can associate with
> `S` the undirected graph `G_S = (V_S, E_S)` where `V_S = {1,…,n}` and `{i,j} ∈ E_S` iff `i` and
> `j` are contained in some common column in `S`."

The vertices are the **entries** and the edges are read off the **filling**. The delegated gloss is
wrong, and it is wrong in the direction that would have made the ruling below come out the other
way. Every quotation in this section was re-checked by text search in the fetched rendering by me.

### 3.2 The two theorems, quoted

> **Theorem 7.2.** "The evaluation `f_T̂(p)` for a highest weight vector
> `f_T̂ ∈ Sym^n Sym^d ℂ^m` given by a Young tableau `T̂` with content `n × d` and a symmetric
> tensor `p ∈ Sym^d ℂ^m` given by an ncABP `A` of width `w` can be computed in time
> `w^{ω(τ+1)} poly(n,d,m,|𝒯|)` if a tree decomposition `𝒯` of `G_T̂` of width `τ` and size `|𝒯|`
> is given and given that we can multiply two matrices of size `≤ k × k` in time `O(k^ω)`."

> **Theorem 8.1.** "Deciding whether a highest weight vector `f_T̂` of `Sym^n Sym^d ℂ^m` given as a
> Young tableau `T̂` evaluates to zero at a point `p ∈ Sym^d ℂ^m` of Waring rank 3 is NP-hard for
> constant `d ≥ 8, m ≥ 2`. Assuming ETH no `2^{o(n)}` algorithm for this evaluation can exist."

Also used: **Definition 7.1** (tree decomposition, width = largest bag minus one); the ncABP
definition ("an acyclic directed graph with two distinguished nodes `s` and `t` and edges labeled
with elements from `V` and every path from `s` to `t` having the same length"; "The width of an
ncABP is the largest number of vertices in any layer"); **Corollary 6.10** (`W_{k,d} ⊆ W̄_{k,d} ⊆
B_{k,d} = B̄_{k,d}`, i.e. Waring rank `≤ k` implies ncABP width `≤ k`); **eq. (5.6)**
("`HWV_λ(Sym^n Sym^d ℂ^m)` is the linear span of the `f_T̂`, where `T̂` is semistandard of shape
`λ` with content `n × d`"); and **eq. (5.2)**, the evaluation formula
`f_T(p) = Σ_{proper ϑ} Π_{c=1}^{λ_1} det_{ϑ,c}`.

**One notational defect in the source, recorded, not load-bearing.** §5's definition line reads
"`f_T̂ ∈ Sym^d Sym^n ℂ^m` as the restriction of `f_T` to `Sym^n ℂ^m`", with `n` and `d` in the
opposite order to eq. (5.6) and Theorem 7.2, which agree with each other. I adopt Theorem 7.2's
convention. Nothing below turns on it.

**Translation to this programme's labels.** Their ambient `Sym^n Sym^d ℂ^m` is our
`Sym^d(Sym^n C^r)`: **their `n` is our `d`** (the degree of the equation), **their `d` is our `n`**
(the degree of `det_n` and of the padded permanent), their `m` is our `r`. So `G_T̂` has **one
vertex per unit of the equation's degree** — at `d = 900`, nine hundred vertices — and the point
`p` is our `det_n` or `x_0^{n-3}per_3` restricted to `r` variables.

### 3.3 Lemma 2 — small tail implies small treewidth (PROVED, elementary, mine)

> **Lemma 2.** For every filling `T̂` of shape `λ`, `τ(G_T̂) ≤ λ_2 + |λbar| − 1 ≤ 2|λbar| − 1`.

*Proof.* A column of `λ` of length 1 is a single box and contributes no edge, so every non-isolated
vertex is an entry of some column of length `≥ 2`, i.e. of one of the first `λ_2` columns. The
number of boxes in those columns is `Σ_{j≤λ_2} λ'_j = |λ| − (λ_1 − λ_2) = |λbar| + λ_2`, so at most
that many vertices are non-isolated. Treewidth is the maximum over connected components, isolated
vertices contribute 0, and a graph on `k` vertices has treewidth `≤ k − 1`. Finally `λ_2 ≤ |λbar|`.
∎

> **The converse fails, and badly.** Take `λ = (k, k)` with content `d × n`, `n = 2`, `d = k`, so
> each of the `k` values occupies two boxes. A column with a repeated entry makes `f_T̂ = 0`
> (their Lemma 5.5), so each column holds two distinct values and each value lies in two distinct
> columns: `G_T̂` is 2-regular, a disjoint union of cycles, and `τ = 2`. Meanwhile `|λbar| = k` is
> unbounded. **Large tail with treewidth 2.**

Their own hardness instance runs the same way: Theorem 8.1 builds `T̂` from a graph of maximum
degree `≤ 4` by adding "two columns of the form `u / v`" per edge, so `λ_2 = 2|E|` and the tail is
large. Consistent with Lemma 2: hardness cannot occur at small tail.

### 3.4 Ruling

**Small treewidth is NOT the same phenomenon as B23-06's small tail.** They part in three places,
each of which matters:

1. **Direction.** Small tail `⟹` small treewidth (Lemma 2). Small treewidth `⇏` small tail (the
   cycle example). Small tail is strictly the stronger condition.
2. **Argument.** `τ` is a function of the **tableau**; the tail is a function of `λ` alone. Two
   highest weight vectors in the same cell can have different `τ`. The tail grades cells; treewidth
   grades basis vectors inside a cell. They are not functions of the same thing, so they cannot be
   the same phenomenon whatever the inequalities say.
3. **What is priced.** Theorem 7.2 prices **one evaluation of one HWV at one point**. `N_S` prices
   **the dimension of the space the programme must do linear algebra on**. Neither bounds the
   other. And nothing in either prices **existence**, which is what Question 1 asks.

**So Theorem 7.2 does not price Question 1.** It prices a subroutine of the test, not the question.
Question 1 is priced by §2 instead, and by a different mechanism.

**The interlock, and what it leaves open.** §2 proves separating equations need tail `≥ D*`;
Lemma 2 proves the regime where Theorem 7.2's exponent is small is contained in the small-tail
regime. So **the corner where the published algorithm is fast is exactly the corner §2 proves is
empty.** Taken naively that closes the matter. It does not, and saying so would be the mistake
Lemma 2's converse warns against:

> **Reopening condition (new, this slot).** Lemma 2 is one-directional. A cell with tail `≥ 900`
> may still contain tableaux of small treewidth — the cycle example shows the tail places no lower
> bound on `τ` at all. For such a tableau, Theorem 7.2 evaluates the HWV in
> `w^{ω(τ+1)} poly(d, n, r, |𝒯|)`, i.e. **polynomially in the degree**, at a point `p` of small
> ncABP width (Corollary 6.10 makes small Waring rank sufficient). **Whether the separating cells
> forced by §2 contain small-treewidth tableaux is open, is not priced by anything on record, and
> is the one genuinely live thing this section found.** It is a question about fillings, and the
> record has never asked one.

Two things that reopening condition does **not** license, stated so they are not read into it: a
cheap evaluation does not shrink `N_S`, which is what the programme's linear algebra costs; and the
number of generators in BDI's own basis (eq. 5.6) is a Kostka number, a third quantity, which this
slot did not measure and makes no claim about.

---

## 4. Question 3 — do the 70 patterns carry a charge?

### 4.1 The 70, enumerated

B22-01's Missing Theorem (PROVED in all parts, two lineages, B23-10 §1) produced 70 typed
`ε_3`-contraction patterns forming a basis of `F^L_{-1}`, with a certified 70-point evaluation set.
A pattern types the 20 slots (4 columns × 5 positions) of `D = Y_1 ∧ … ∧ Y_5` by `{a, r, c, S, K}`
(legs 0, 1, 1, 2, 2) and partitions the 30 legs into ten triples contracted with `ε_{ijk}`. The
`K`-counts are `(2,3,3,3)`, so column 0 carries three non-`K` slots and columns 1–3 two each.

Pilot 1 re-derived all 70 from B22-01's sealed packet (pinned by sha256 against its `MANIFEST.json`
at `53bdb31e`) and **replayed** them: `Ξ_h` and `F_1^h` recomputed at the 80 recorded points for
every one of the 70, **all 70 agreeing with the recorded `vec80`**, and the `70 × 70` determinant
recomputed nonzero mod `P` (`132757`). Controls C0 (the 70 certificate points rebuilt from
`rng(20260922)` equal the recorded ones) and C1 both pass. The instrument is therefore sound in
this session's hands: evaluation at the 70 points is injective on `F^L_{-1}`, so **a rank of
evaluation vectors is the dimension of a span**, with no new certification needed.

**The arithmetic that pins the four blocks.** The 20 slots carry `#a + #r + #c + #S + #K = 20` with
`#K = 11`, and the 30 legs give `#r + #c + 2#S + 2#K = 30`. With `#r = #c = k` this forces
`#S = 4 − k` and `#a = 5 − k`. Two `a`-slots in one column antisymmetrise to zero (the column is a
full antisymmetrisation and `a` is a scalar), so `#a ≤ 4`, i.e. `k ≥ 1`; and `#S ≥ 0` gives
`k ≤ 4`. **So `#a ∈ {1,2,3,4}` and both ends are forced by structure** — the top by the number of
columns, the bottom by the leg count.

Distribution of all eight pre-registered statistics over the 70 (pilot 1, `s4_the_70`):

| statistic | distribution over the 70 | range |
|---|---|---|
| `s_a` (`#a`) | 1:7, 2:31, 3:28, 4:4 | 1–4 |
| `s_in` | 0:49, 1:17, 2:3, 3:1 | 0–3 |
| `s_sp` | 11:8, 12:13, 13:10, 14:13, 15:12, 16:8, 17:5, 18:1 | 11–18 |
| `s_kk` | 2:4, 3:16, 4:29, 5:21 | 2–5 |
| `s_nk` | 5:21, 6:29, 7:16, 8:4 | 5–8 |
| `s_rep` | 0:29, 1:22, 2:19 | 0–2 |
| `s_cr` | spread over 19–41, modal 27 | 19–41 |
| `s_inv` | spread over 6–23, modal 14 and 19 | 6–23 |

### 4.2 (a) Is the basis canonical? **No.**

**The 70 are a greedy random selection, not a distinguished set.** B22-01 obtained them by drawing
random typed patterns under a seed and keeping one iff it raised the rank, stopping at each block's
proved target. The spanning set is the set of *all* typed patterns, which is astronomically larger
(the ten triples alone are a partition of 30 legs); the 70 are one basis extracted from it by a
procedure that depends on `numpy.random.default_rng(20260925)`. A different seed gives a different
70. **Nothing distinguishes these 70 among the patterns.** So they are not a crystal or canonical
basis, and they are not the image of one under an explicit map — not because such a thing is ruled
out, but because these particular objects carry no property that would make them it.

**What obstructs canonicity, named.** Two things, and they are different in kind:

1. **The spanning set is not a basis and has no distinguished sub-basis.** Canonical and crystal
   bases are indexed by combinatorial objects in bijection with a basis (tableaux of a shape,
   paths in a crystal). Here the indexing objects — patterns — vastly outnumber the dimension, the
   map pattern `↦` function is enormously non-injective, and the record has no rule that picks 70
   of them. Producing such a rule is exactly the content that is missing.
2. **The construction is per-cell.** The multidegree blocks, their targets `7, 31, 28, 4`, and the
   `ε_3` contraction scheme are all specific to `λ = (4^5)`, `d = 5`, `W = Mat_4`, `L` as in
   B18-02. Nothing in it is stated for a family.

**The consequence for the record, which is the useful half of a negative.** The Missing Theorem is
**bespoke and must be re-proved per cell.** The next cell does not cost nothing; it costs a
theorem. Any feasibility estimate that assumed the `F^L_{-1}` construction transfers should be
corrected.

### 4.3 (b) Do they carry a grading? **Exactly one, and it is the multidegree.**

**The grading that is there.** `F^L_{-1} = V_1 ⊕ V_2 ⊕ V_3 ⊕ V_4` by `#a`, with

> **graded dimensions `7, 31, 28, 4`, summing to 70.**

This is a **direct sum**, PROVED in the operational sense the pre-registration fixed: pilot 1 found
the four block ranks to be `7, 31, 28, 4` and the total rank of all 70 to be `70`, so
`Σ dim V_i = dim ΣV_i` and the four spans are independent. Pilot 1 then sampled **466 further
patterns under a new seed** (`20260919`, a second lineage) and **no block rank exceeded its
target**, with every block saturating at its value — so `7, 31, 28, 4` are the block dimensions,
not merely lower bounds (MEASURED for the ceiling, which is all a sample can give; the targets
themselves are PROVED in `arc_target` §5.1 via `b_L(11) = 70`).

**It is a genuine grading of the space, and here is why.** `L` acts by `Y ↦ AYB` with
`A = diag(α, g)`, `B = diag(β, c g^T)`, giving `a ↦ αβ a`, `r ↦ αc·g r`, `c ↦ β·g c`,
`E ↦ c·g E g^T` with `S` and `K` separately stable. **`L` acts diagonally on the type decomposition
`W = C_a ⊕ C_r^3 ⊕ C_c^3 ⊕ Sym ⊕ Skew`**, so the multidegree grading of the coordinate ring is
`L`-stable and restricts to `F^L_{-1}`. It is **not** a character grading: substituting
`#a = 5−k, #r = #c = k, #S = 4−k, #K = 11` into the character `α^{#a+#r} β^{#a+#c} c^{#r+#S+#K}`
gives `α^5 β^5 c^{15}` for **all four** blocks, which is precisely why they all sit in `F^L_{-1}`.
So the statistic is extra data not visible to the group — the same situation as charge, which is
also not a character.

**Does it have the Kostka–Foulkes shape?** Partly, and the honest accounting is:

| property | `7 q + 31 q² + 28 q³ + 4 q⁴` |
|---|---|
| non-negative | yes |
| unimodal | yes (`7 ≤ 31 ≥ 28 ≥ 4`) |
| degree range forced | **yes**, and by structure: top `4` = the number of columns (two `a`'s in a column antisymmetrise to zero), bottom `1` = `5 − #S_max` with `#S ≤ 4` from the leg count (§4.1) |
| symmetric / a known product formula | no, and none is claimed |

**Unimodality here is weak evidence and is reported as such.** Four positive numbers in a random
order are unimodal a third of the time. The forced degree range is the stronger of the two
observations, because it has a proof rather than a count behind it.

### 4.4 Seven further statistics: ten PROVED trivial, one MEASURED candidate

The remaining question is whether anything **refines** the multidegree — in particular whether
anything splits the 31-dimensional block. Pilot 1 profiled all eight statistics; pilots 2 and 3
then decided every class that pilot 1 could not.

**The one PROVED negative available directly from pilot 1**: `s_in` (triples inside a single
column). 385 sampled patterns with `s_in = 0` have rank **70** — the lowest class alone spans the
whole of `F^L_{-1}`. `s_in` is trivial, outright.

**Pilot 1's other profiles were sample-limited, not gradings**, and pilot 2 was written to say so
or refute it. Of its eleven pre-registered classes, **ten reached the full block dimension** and
are therefore **PROVED trivial** (a modular rank is a floor, so "reaches the ambient dimension" is
the safe direction, G27):

| block (dim) | class | pilot 1 saw | pilot 2 | verdict |
|---|---|---|---|---|
| `2,3,3,1` (31) | `s_inv ≤ 11` | 46 → 27 | 110 accepted → **31** | trivial, PROVED |
| `2,3,3,1` (31) | `s_inv ≤ 13` | 61 → 29 | 61 → **31** | trivial, PROVED |
| `2,3,3,1` (31) | `s_cr ≤ 27` | 29 → 28 | 31 → **31** | trivial, PROVED |
| `2,3,3,1` (31) | `s_sp ≤ 11` | 15 → 15 | 32 → **31** | trivial, PROVED |
| `3,2,2,2` (28) | `s_inv ≤ 12` | 37 → 25 | 39 → **28** | trivial, PROVED |
| `3,2,2,2` (28) | `s_nk ≤ 5` | 18 → 18 | 38 → **28** | trivial, PROVED |
| `3,2,2,2` (28) | `s_sp ≤ 11` | 7 → 7 | 29 → **28** | trivial, PROVED |
| `1,4,4,0` (7) | `s_sp ≤ 11` | 10 → 6 | 10 → **7** | trivial, PROVED |
| `4,1,1,3` (4) | `s_cr ≤ 20` | 4 → 4 | 4 → **4** | trivial, PROVED |
| `4,1,1,3` (4) | `s_sp ≤ 10` | 3 → 3 | 4 → **4** | trivial, PROVED |
| `1,4,4,0` (7) | `s_rep ≤ 0` | 8 → 6 | 126 accepted → **6** | stalled |

**The survivor, and pilot 3's attempt on it.** `s_rep = 0` in block `(1,4,4,0)` is rigid: with
`#a = 1, #r = #c = 4, #S = 0`, a column with no repeated type cannot be `(r,r)` or `(c,c)`, and a
three-slot column drawn from `{r,c}` alone must repeat — so `cols[0]` is a permutation of
`(a, r, c)` and each of `cols[1..3]` a permutation of `(r, c)`, 48 column assignments with the ten
triples free. Pilot 3 sampled that family **directly**, with no rejection, under a fourth seed:

> **400 accepted patterns, rank 6 of 7, no rise over the last ~394.**

**Verdict: MEASURED candidate, not a grading.** A sampled rank below the ambient dimension is never
a proof that the filtration is proper — that is the asymmetry the pre-registration fixed, and it
binds here as much as it bound the negatives. What is proved is `dim ≥ 6`; what is not proved is
`dim < 7`.

**And even if it is real, it is not a grading and does not have the Kostka–Foulkes shape.** `s_rep`
would be non-trivial at one threshold in one block of four and trivial in the other three; its
graded count is `(6, 1, 0)` in a 7-dimensional block and `(dim, 0, 0)` elsewhere. That is a
codimension-1 subspace, not a statistic that grades `F^L_{-1}`.

### 4.5 Verdict on Question 3

**(a) Not canonical**, and the obstruction is named: the spanning set has no distinguished
sub-basis and the construction is per-cell. The Missing Theorem must be re-proved per cell.

**(b) One grading, the multidegree, `7 ⊕ 31 ⊕ 28 ⊕ 4`**, non-negative, unimodal, with both ends of
the degree range forced by structure — and it was already latent in the record (`arc_target` §5.1's
block targets); what is new here is that it is a direct sum, that it is `L`-stable but not a
character, and that its range is forced. **Every other statistic tried is trivial**, ten classes
PROVED so, with one codimension-1 MEASURED candidate that would not be a grading even if confirmed.

**This is the negative the launch prompt expected, and it is the informative kind**: the 70 objects
exist, they can be graded, and the grading they carry is the one the group already sees the shadow
of. Nothing here says anything about Kronecker coefficients; it says something about this weight
space, which is more than the record had.

---

## 5. Exact scope, and reopening conditions

**What is PROVED.**

- Theorem 1 and its corollary (§2.2): every separating cell has tail `≥ D*`; every separating
  equation is `c_{n e_1}^k` times one whose cell has tail equal to its degree. Elementary, one
  lineage, controlled by C2's literal enumeration at two small cells.
- Lemma 2 (§3.3): `τ(G_T̂) ≤ λ_2 + |λbar| − 1`, for every filling. Elementary.
- The converse of Lemma 2 fails (§3.3, the cycle example).
- `F^L_{-1} = V_1 ⊕ V_2 ⊕ V_3 ⊕ V_4` with dimensions `7, 31, 28, 4` (§4.3), and `#a ∈ {1,2,3,4}`
  with both ends forced (§4.1).
- Eleven classes of statistics are trivial: `s_in` at `j = 0` on the whole space, and the ten
  classes of §4.4.

**What is MEASURED only.** The block dimensions as *ceilings* (466 + samples, two seeds); the
`s_rep = 0` candidate at rank 6 of 7; the programme's reach as `t ≈ 24`; the C3 minima, which are
minima over the shapes evaluated and, at `t = 18…24`, over two shapes of many.

**What is EXTRAPOLATION.** The `≈ 4·10^10` at `t = 900` (§2.4): a quartic fitted on `t = 12…24`
and evaluated 37-fold outside that range. Not MEASURED, not PROVED.

**What is CONDITIONAL.** Every statement that puts a number on `D*` beyond the proved floor `8`
depends on the record's Conjecture 2 (onset of `I(D_5^{det_n})` at `cap(n)`), which is an
expectation, not a theorem. Theorem 1 itself is unconditional.

**What is not claimed, stated explicitly.**

- Nothing about Kronecker coefficients. The grading of §4 is a grading of one weight space.
- Nothing about plethysm or Kronecker combinatorics in general — the known wall, and not this
  slot's business.
- Nothing about `a(λ)` versus `a(μ)` under Theorem 1's reduction (§2.2, second remark).
- No cell is nominated, and no equation is produced.
- No "iff" is drawn from modular data (G27): every modular rank above is used only in the
  direction "a rank is a floor".

**Reopening conditions.**

1. **Large tail, small treewidth (§3.4).** The one live thing §3 found. Do the cells that Theorem 1
   forces (tail `≥ D*`) contain tableaux of small treewidth? Lemma 2 gives no lower bound on `τ`,
   and the cycle example shows there is none in general. If yes, Theorem 7.2 evaluates those HWVs
   in time polynomial in the degree. This is a question about **fillings**, which the record has
   never asked. It does not shrink `N_S`.
2. **The `s_rep = 0` candidate (§4.4).** Settled either by a proof that the rigid family spans a
   hyperplane of `V_1` — the `r ↔ c` involution induced by `Y ↦ Y^T` (which sends `a ↦ a`,
   `r ↔ c`, `S ↦ S`, `K ↦ −K`, hence acts by a sign `(−1)^{#K} = −1` here) is the first thing to
   look at — or by a sample large enough to reach 7. It would not be a grading either way.
3. **Theorem 1's equivariant refinement.** Whether `a(λ)` at degree `d` equals `a(μ)` at degree
   `t`. Not needed for anything above; it would sharpen §2.4's price from weight spaces to
   multiplicities.
4. **The C3 minima at `t ≥ 18`** were taken over two shapes. A full minimisation would replace the
   extrapolation's base points with exact ones; it is a few seconds of work and was not done
   because the budget was spent.

---

## 6. Ledger

| # | statement | label | where |
|---|---|---|---|
| L1 | Every cell carrying a separating equation has tail `≥ D*`; a separating equation cannot lie in a small-tail cell | **PROVED** | §2.2 Thm 1 |
| L2 | Every separating equation is `c_{n e_1}^k` times one whose cell has tail `=` degree | **PROVED** | §2.2 Cor. |
| L3 | For `t < d` the `λ`-weight space is `c_{n e_1}^{d-t}·(μ`-weight space at degree `t)`, bijectively on monomial bases | **PROVED** | §2.2 (i) |
| L4 | `c_{n e_1}` vanishes identically on neither `D_r^{det_n}` nor `P_r` | **PROVED** | §2.2 |
| L5 | The DP reproduces B23-06's `N_S = 553, 621, 641` | **CONTROL, agrees** (independent lineage) | §2.4 C1 |
| L6 | The factorisation holds by literal enumeration at `(3,3,5,(1,1))` and `(3,4,6,(1,1,1))` | **CONTROL, agrees** | §2.4 C2 |
| L7 | Programme reach `N_S ≲ 2·10^4` is `t ≈ 24` at the cheapest evaluated shape | **MEASURED** | §2.4 C3 |
| L8 | min `N_S ≈ 4·10^10` at `t = 900` | **EXTRAPOLATION**, and **CONDITIONAL** on Conjecture 2 | §2.4 |
| L9 | B23-06's `621` and `10^150.4` are both the wrong price | **PROVED** (that `621`'s cell class is empty) + **EXTRAPOLATION** (the replacement) | §2.3–2.4 |
| L10 | BDI arXiv:2002.11594, Thm 7.2 and Thm 8.1, as quoted | **PRIMARY** (ar5iv HTML `31c8a745…`; PDF v2 `5371f3b6…`) | §3.1–3.2 |
| L11 | `G_T̂` is built from the tableau's **entries**, i.e. depends on the filling | **PRIMARY, quoted**; corrects a delegated reader's gloss inside this session | §3.1 |
| L12 | `τ(G_T̂) ≤ λ_2 + |λbar| − 1 ≤ 2|λbar| − 1` | **PROVED** | §3.3 Lem. 2 |
| L13 | The converse fails: `λ = (k,k)` admits fillings with `τ = 2` and unbounded tail | **PROVED** | §3.3 |
| L14 | Small treewidth is **not** the same phenomenon as small tail; Thm 7.2 does **not** price Question 1 | **RULING**, on L10–L13 | §3.4 |
| L15 | Large tail with small treewidth is open and unpriced | **OPEN**, new this slot | §3.4 |
| L16 | The 70 patterns replay exactly (all 70 `vec80`), `det ≠ 0 mod P` | **CONTROL, agrees**, replay of B22-01 | §4.1 |
| L17 | `F^L_{-1} = 7 ⊕ 31 ⊕ 28 ⊕ 4` by `#a`, a direct sum, `L`-stable, not a character grading | **PROVED** (direct sum, `L`-stability); block dims as ceilings **MEASURED** | §4.3 |
| L18 | `#a ∈ {1,2,3,4}`, both ends forced by structure | **PROVED** | §4.1 |
| L19 | The 70-pattern basis is **not** canonical; the Missing Theorem is bespoke and must be re-proved per cell | **ASSESSED**, with the obstruction named | §4.2 |
| L20 | `s_in` is trivial on the whole space; ten further classes are trivial | **PROVED** (rank reaches the dimension; G27-safe direction) | §4.4 |
| L21 | `s_rep = 0` in block `(1,4,4,0)` spans `≥ 6` of 7 after 400 direct samples | **MEASURED** candidate; not a grading either way | §4.4 |
| L22 | No statistic other than `#a` grades `F^L_{-1}` among those tried | **ASSESSED**, on L20–L21 | §4.5 |

---

## 7. Resources, receipts, manifest

**Pilots, priced before each launch, three of three allowed.**

| pilot | price given before launch | actual | receipt |
|---|---|---|---|
| `b24_04_p1_patterns` | ~600 sampled patterns at ~0.015 s each plus the 70-pattern replay ≈ 25 s; tensors at most `3^8` int64, ≈150 MiB | **21.40 s, 151.9 MiB peak job, exit 0** | `results/logs/b24_04_p1_patterns_resources.json` |
| `b24_04_p2_saturate` | 11 classes × ~4.4 s, same tensor sizes ≈150 MiB, ≈50 s | **13.23 s, 150.5 MiB, exit 0** | `results/logs/b24_04_p2_saturate_resources.json` |
| `b24_04_p3_close` | part A ~26 s of direct sampling, part B a DP with the size counter dropped, ≈150 MiB | **15.84 s, 150.4 MiB, exit 0** | `results/logs/b24_04_p3_close_resources.json` |

Total **50.47 s of 180 s**, every run under the 60 s / 512 MiB cap, every one wrapped by
`analysis/b15_bound.py` (`ca001081…`) with the Job Object enforced. No unwrapped run of any size
(G19); no symbolic computation was done outside a wrapper.

**Receipts.** `results/logs/b24_04_p1_patterns.pid`, `…_p2_saturate.pid`, `…_p3_close.pid` exist on
disk and are matched by `results/logs/*.pid` in `.gitignore`, for which there is
**negation missing for `b24_04_`**. The three `_resources.json` files are untracked and visible.

**Pinned inputs**, both bound by B22-01's `results/b22_01/MANIFEST.json` at
`53bdb31e3042acae9464f9025be355ae699a2485` and extracted read-only into the session scratchpad
(neither is present at HEAD `feed104e`):

```
analysis/b22_01_typed_v2.py   93d739eda3afd8c0dbddf452de1e73e76470864fd8ece27171f683574eb326fc  13226 B
results/b22_01/p2_basis.json  7162d852b4490d2f22702b9b974979e403dd0dfb8794cef92b6be894d9a66e79 293596 B
```

Read-only inputs consulted: B23-06 at `feed104e` (`docs/b23_06_report.md`); B22-01's report and
packet at `53bdb31e`; B23-10 at `239dd6e84417ab04914a8d84cca02ddf754bf1fb` (§1 for Theorem M's
status, §10.2 item (a) for where this slot sits); the archive at `82633a60893236fab4fbc317df416e1b8a349005`.

**Literature**, in the session scratchpad under `lit/`, not in the tree:

```
bdi_2002.11594v2.pdf  5371f3b62964f221b248334bec54d453a5bdcca4f2980c854cee41183f1317b6   513636 B
bdi_ar5iv.html        31c8a74500d961b8e60e29daf8a780917700a1ad2fa1f2a5f383b1b454cde23b  1630516 B
```

**Chain of pins across the three pilots.** Pilot 2 asserts pilot 1's output
`e43e7412cf92970e1a290854f350368621bb7a652be4f31d33c4bc4a07a12421`; pilot 3 asserts pilot 1's and
pilot 2's (`1819b8f3fbed9938092a7be83924c8dd2f361f6f9d0fc2e7d3f1b11f44246c5c`). Pilots 2 and 3 take
the statistics and the modular linear algebra from pilot 1's own file by executing only its
function-definition prefix, so the definitions are provably the ones pilot 1 ran with.

**New files, all untracked; nothing under `results/b23_*` touched; read-only git.**

```
analysis/b24_04_p1_patterns.py      analysis/b24_04_p2_saturate.py      analysis/b24_04_p3_close.py
analysis/b24_04_seal.sh             docs/b24_04_report.md
results/b24_04/PREREG_b24_04_p1.md  results/b24_04/PREREG_b24_04_p2.md  results/b24_04/PREREG_b24_04_p3.md
results/b24_04/p1_patterns.json     results/b24_04/p2_saturate.json     results/b24_04/p3_close.json
results/b24_04/MANIFEST.json        results/b24_04/SEAL_LOG.txt
results/logs/b24_04_p{1,2,3}_*_resources.json   (+ the three .pid files, gitignored)
```

`results/b24_04/MANIFEST.json` hashes every file of this packet except itself and `SEAL_LOG.txt`,
and is produced by `analysis/b24_04_seal.sh` (hashing and listing only; not a numerical run under
G19).

**Honest negatives.**

1. The `s_rep` candidate is unresolved and I spent the last pilot on it without closing it.
2. The C3 minima at `t = 18…24` rest on two shapes each, so the extrapolation's base points are
   themselves upper bounds on the true minima. The extrapolation is 37-fold out of range.
3. §3's reading is of an HTML rendering whose arXiv version is unstated, against a hashed PDF v2.
   A delegated reader's gloss on the one load-bearing definition was wrong and had to be corrected
   by hand; other delegated glosses in that fetch were not individually re-checked, and nothing
   below §3.2 relies on them.
4. Everything is producer-only (G18) except L5, L6 and L16, which agree with independently produced
   record values.
