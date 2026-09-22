# B25-04 — Large tail with small treewidth: disconnected fillings never separate

21 September 2026 (UTC). Slot B25-04, worktree `work/batch15_workers/B15-02`, branch
`b15-02-a1-probes`. Author: Claude (Opus 5, 1M context). Producer only; nothing here is
independently accepted. **UNCOMMITTED** until a separately authorised delivery pass.

**Outcome selected from the registered space: (2) — proof of a no-go for one precisely defined
family**, with the surviving corner priced and one next certificate named (§6–§7).

---

## 0. Provenance, read-only, recorded before any write

```
first UTC in session       2026-09-21T03:38:39Z
git rev-parse HEAD         aafcbb692375f0a968881dbf18963a74d62ab557   (= launch baseline)
git branch --show-current  b15-02-a1-probes
git status --short         ?? results/logs/b15_02_runtime_native_20260913.pid
                           ?? results/logs/b15_02_runtime_native_20260913_resources.json
                           ?? results/logs/b15_02_runtime_preflight_run_20260913T062637Z.pid
                           ?? results/logs/b15_02_runtime_preflight_run_20260913T062637Z_resources.json
```

HEAD equals the baseline, so every pinned input resolves. Read-only Git only; no commit, stash,
reset or `.gitignore` edit. The four pre-existing receipts are untouched.

**Timeline.** Theory gate written by 03:43:24Z (`results/b25_04/THEORY_GATE.md`), i.e. within
5 minutes of the first recorded time, far inside the 45-minute gate. Pilot 1 preregistered 03:44:20Z,
run 03:45:18Z; pilot 2 preregistered 03:46:11Z, run 03:46:35Z. Report written afterwards.

**Notation (project variables, used consistently).** Form degree `n` (the determinant size; the
points are forms in `Sym^n C^r`), equation degree `d`, variable count `r`. `D_r^{det_n}` and `P_r`
as in B24-04 §0 (closures of the `r`-variable restrictions of `det_n` and of `x_0^{n-3} per_3`;
irreducible cones). `λ ⊢ nd`, `ℓ(λ) ≤ r`, tail `t = |λ̄| = nd − λ_1`.
`D* := min{deg f : f ∈ I(D_r^{det_n}), f|_{P_r} ≠ 0}` (B24-04 §2.1). **BDI's
`Sym^{n_B} Sym^{d_B} ℂ^m` is our `Sym^d(Sym^n C^r)`: `n_B = d`, `d_B = n`, `m = r`.** A tableau
`T̂` has shape `λ` and content `d × n` (entries `1..d`, each `n` times); `f_T̂` is BDI's tableau
function; `G_T̂` has vertex set `{1,…,d}` and an edge `{a,b}` iff `a` and `b` share a column.

---

## 1. Inputs, bound

| input | locator | SHA-256 | status of use |
|---|---|---|---|
| B24-04 report | `aafcbb69:docs/b24_04_report.md`, blob `87d12b43a8a743ed245b1d60d6e40f344ad30f04` | `3d24884a…6eee4b` (committed blob content = raw working copy, both CRLF) | READ in full |
| B24-04 manifest | `aafcbb69:results/b24_04/MANIFEST.json`, blob `8413f7a33aeae905846434687d16185293b05101` | `c2151d38…bc79e1` (blob = raw) | READ |
| B24-10 review | `ab2f8a40:docs/b24_10_review.md` (worktree B15-10), blob `46edbcb023a9997b9288630f13198bdbe44a53ef` | blob content `da1528ba…11c2bf3` | READ §1, §11.1, §11.9 (+ §11.10) |
| B24-10 manifest | `ab2f8a40:results/b24_10/MANIFEST.json`, blob `d9124cb7…` | `ba6aea5122c152fafb98491a0a0c49be25c196ed1d3c2c6df6336b32fc05eafe` — **matches SOURCE_INDEX** | hash verified only |
| BDI, arXiv:2002.11594v2 PDF | `https://arxiv.org/pdf/2002.11594v2` | `5371f3b62964f221b248334bec54d453a5bdcca4f2980c854cee41183f1317b6`, 513 636 B | hashed; not text-read (no PDF text extraction locally) |
| BDI, ar5iv HTML rendering | ar5iv of 2002.11594 | `31c8a74500d961b8e60e29daf8a780917700a1ad2fa1f2a5f383b1b454cde23b`, 1 630 516 B | **PRIMARY at the HTML-rendering level**: I read §5 (Def. 5.1, eq. (5.2), Lemmas 5.4–5.5, eq. (5.6), Rem. 5.7), §6 (Def. 6.1, Thm 6.2 statement, Lemmas 6.5–6.6, Prop. 6.8 with proof, Cor. 6.10), §7 (graph definition, Def. 7.1, **Thm 7.2 and its full proof**, Rem. 7.16) |
| wrapper | `analysis/b15_bound.py` working copy | raw `ca001081…a41f854` (CRLF; blob content `1f73ad8d…`) | inspected, used |

**Where the BDI bytes came from.** The two files were not re-downloaded: they were copied from
B24-04's session scratchpad (`…/36df5f81-…/scratchpad/lit/`) into this session's scratchpad, and
their SHA-256 values equal those B24-04 recorded (§3.1 there). The text I read is my own tag-stripped
extraction of the hashed HTML (`bdi_mytext.txt`, scratchpad only); B24-04's derived text file was
not used. The limitation B24-04 recorded stands: ar5iv does not state which arXiv version it
renders, so the reading is PRIMARY for the hashed HTML against a hashed PDF v2.

**Tool memory.** The session loaded my auto-memory index, which includes a B24-04 outcome note and a
"PDF text extraction unavailable" note. The latter was used only as an operational hint (read the
HTML); no memory entry is a premise of any claim here. One new memory entry is created at the end
of this session (§9).

---

## 2. The two published statements this slot uses, quoted

### 2.1 B24-04 Theorem 1 — full statement (PROVED; B24-10 §11.1 row 1.1)

Quoted from `aafcbb69:docs/b24_04_report.md` §2.2, not from any brief:

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

Its proof establishes `c_{ne_1} ∉ I(D_r^{det_n})` with the witness `A_1 = I` and
`c_{ne_1}|_{P_r} ≠ 0` with an explicit substitution, and then uses primality of
`I(D_r^{det_n})`. B24-10 §1.1 adds that the used direction of (ii) needs only primality plus
`c_{ne_1} ∉ I`. B24-04 Lemma 2 (`τ(G_T̂) ≤ λ_2 + t − 1`) is **one direction only**; its converse
fails (B24-04 §3.3), and nothing below claims that a large tail forces a large treewidth.

### 2.2 BDI Theorem 7.2 and its actual input model (PRIMARY, HTML)

> **7.2 Theorem.** "The evaluation `f_T̂(p)` for a highest weight vector
> `f_T̂ ∈ Sym^n Sym^d ℂ^m` given by a Young tableau `T̂` with content `n × d` and a symmetric
> tensor `p ∈ Sym^d ℂ^m` given by an ncABP `A` of width `w` can be computed in time
> `w^{ω(τ+1)} poly(n,d,m,|𝒯|)` if a tree decomposition `𝒯` of `G_T̂` of width `τ` and size `|𝒯|`
> is given and given that we can multiply two matrices of size `≤ k × k` in time `O(k^ω)`."

What the proof actually does, and hence the exact dependencies (checked by me in the proof text):

- **Inputs, all given:** the tableau; the point **as an ncABP** (not as coefficients, not as a
  Waring decomposition); **a tree decomposition — its computation is not part of the theorem**.
- A leaf is attached for every column (so the working tree has at least `λ_1 = nd − t` leaves in
  our variables), the tree is binarised, and a DP runs over matrices indexed by
  `𝓕_t^{X_v} ⊆ Π_i L_{κ_t(i)}`, fixed outside the bag `X_v`; hence each matrix has side
  `≤ w^{|X_v|} ≤ w^{τ+1}` and each internal node costs one product of such matrices. Leaves cost
  one `ν × ν` determinant of the **top** `ν` coordinates of the edge labels, `ν ≤ m`.
- In project variables: **cost `w^{ω(τ+1)} · poly(d, n, r, |𝒯|)`**.
- **Width of our points.** Prop. 6.8: a minimal ncABP for `p` has exactly `dim ∂^{=k}(p)`
  vertices in layer `k`. Since `k`-th partials of `p ∈ Sym^n C^r` lie in `Sym^{n−k} C^r` and the
  catalecticant rank is symmetric in `k ↔ n−k`,
  `w ≤ W(n,r) := max_k min( C(k+r−1, k), C(n−k+r−1, n−k) )`. **`W(5,5) = 15`**, `W(4,5) = 15`,
  `W(6,5) = 35`, `W(5,4) = 10` (arithmetic, PROVED). This bounds every point of `Sym^n C^r`,
  so in particular every point of `D_r^{det_n}` and `P_r`: **`w` is a constant at fixed `(n,r)`.**
- The naive alternative (Rem. 5.7) is `O(WR(p)^d · poly)` and needs a Waring decomposition, whose
  rank BDI note is NP-hard to determine; the ncABP is instead obtained from catalecticant ranks
  (Prop. 6.8's proof), a constant-size computation at fixed `(n,r)`. Its exact cost is not stated
  in BDI and is **not priced** here beyond "constant at fixed `(n,r)`".

### 2.3 The formula the proof below rests on (BDI eq. (5.2), PRIMARY)

For `p = Σ_{i=1}^R ℓ_i^{n}` (every `p ∈ Sym^n C^r` has such a finite decomposition, BDI Lemma 5.4's
proof), BDI's definition reads, in project variables,

> `f_T̂(p) = Σ_{φ : [d] → [R]} Π_{columns c of T̂} det( top ν_c × ν_c block of [ ℓ_{φ(a)} ]_{a ∈ c} )`,

columns taken top to bottom, `ν_c` the column length. BDI state that this "yields a well-defined
polynomial" (classical; **ADOPTED** from BDI, not re-proved), and eq. (5.6) that the `f_T̂` with
`T̂` semistandard of shape `λ`, content `d × n`, **span** `HWV_λ(Sym^d Sym^n C^r)`. A semistandard
`T̂` does **not** guarantee `f_T̂ ≠ 0` (see pilot 1's incidental observation, §5).

---

## 3. Definitions

- **Component tableau.** For a connected component `C` of `G_T̂`, let `T̂_C` be the multiset of
  columns of `T̂` whose entries lie in `C`. Each column is a clique of `G_T̂`, so each column lies
  in exactly one component and the `T̂_C` partition the columns. Relabel `C` as `1..|C|` and sort
  the columns by decreasing length (column order does not change (5.2), which is a product over
  columns; within-column order is kept). Then `T̂_C` is a BDI tableau of shape `μ_C ⊢ n|C|`,
  content `|C| × n`, and `f_{T̂_C}` is a polynomial of degree `|C|` on `Sym^n C^r`, a highest
  weight vector of weight `μ_C` if nonzero.
- **The family.** For an integer `k ≥ 2`,
  `𝔉_{<k} := { f_T̂ : every connected component of G_T̂ has fewer than k vertices }`,
  single tableau functions (not their spans). Members have `τ(G_T̂) ≤ k − 2`, and the tail is
  additive over components, so it is unbounded.

---

## 4. Results

### 4.1 Lemma A (Component factorisation) — PROVED (from BDI (5.2), PRIMARY; well-definedness ADOPTED)

> **Lemma A.** For every tableau `T̂` with content `d × n`,
> `f_T̂ = Π_{C} f_{T̂_C}` as polynomials on `Sym^n C^r`, the product over the connected components
> `C` of `G_T̂`. An isolated vertex `a` contributes the factor `c_{ne_1}`, the coefficient of
> `x_1^n`.

*Proof.* Fix `p = Σ_{i≤R} ℓ_i^n`. In (5.2) the factor of column `c` depends on `φ` only through
`φ|_c`, and `c ⊆ C` for a unique component `C`. The components partition `[d]`, so
`φ ↦ (φ|_C)_C` is a bijection `[R]^{[d]} → Π_C [R]^C`, and
`Σ_φ Π_c det_c = Π_C ( Σ_{φ_C : C → [R]} Π_{c ⊆ C} det_c ) = Π_C f_{T̂_C}(p)`.
For an isolated vertex `a`, its `n` occurrences are `n` columns of length 1, whose factor is the
first coordinate of `ℓ_{φ(a)}`; summing, `Σ_i (ℓ_i)_1^n`, the coefficient of `x_1^n` in
`Σ_i (ℓ_i · x)^n = p`. The identity holds at every `p`, hence as polynomials. ∎

Isolated vertices are therefore exactly Theorem 1's factor, seen on the filling. The two results
overlap but neither contains the other: Theorem 1 covers every weight vector (spans) but only the
factor `c_{ne_1}`; Lemma A covers only single tableau functions but factors out every component.

### 4.2 Theorem B (no-go for disconnected fillings) — PROVED modulo primality of `I(D_r^{det_n})`

> **Theorem B.** If a single tableau function `f_T̂` is separating — `f_T̂ ∈ I(D_r^{det_n})` and
> `f_T̂|_{P_r} ≠ 0` — then `G_T̂` has a connected component `C` such that `f_{T̂_C}` is itself
> separating. Consequently `|C| ≥ D*` and the tail of `μ_C` is `≥ D*`.
>
> **Corollary B.** **No member of `𝔉_{<D*}` is separating, at any degree and any tail.** With
> only the record's unconditional floor `D* ≥ 8`, **no single tableau function whose tableau
> graph has all components on at most 7 vertices is separating** — whatever its tail, and although
> its treewidth is at most 6.

*Proof.* By Lemma A, `f_T̂ = Π_C f_{T̂_C}`. `D_r^{det_n}` is irreducible, so `I(D_r^{det_n})` is
prime (the same premise Theorem 1 uses; B24-04 §2.2, accepted B24-10 §1.1); a product in a prime
ideal has a factor in it, so some `f_{T̂_C} ∈ I(D_r^{det_n})`. Since `f_T̂|_{P_r} ≠ 0`, there is
a point of `P_r` where the product is nonzero, and there **every** factor is nonzero; in particular
`f_{T̂_C}|_{P_r} ≠ 0`. So `f_{T̂_C}` is separating of degree `|C|`, whence `|C| ≥ D*` by the
definition of `D*` (un-indexed; B24-10 §1.1 (C3)). `f_{T̂_C}` is a weight vector of weight `μ_C`
at degree `|C|` carrying a separating equation, so by Theorem 1's corollary its tail is `≥ D*`.
The corollary is the contrapositive with `k = D*`, and `k = 8` under the floor. ∎

**Premises consumed, stated exactly.** Primality of `I(D_r^{det_n})` (irreducibility of
`D_r^{det_n}`); the definition of `D*`; BDI (5.2) with its adopted well-definedness; Theorem 1
(only for the tail clause). Irreducibility of `P_r` is **not** used. The floor `D* ≥ 8` is the
record's (B24-04 §2.3–2.4, from B23-06 §2.2 via B22-02 L6); I READ it there and did not re-derive
it, so Corollary B's "at most 7" is **PROVED modulo that floor**.

### 4.3 The family is nonzero, legal and of small width — PROVED (nonvanishing also CERTIFIED by exact evaluation, producer-only)

- **Nonzero members of every tail.** For any `n ≥ 2`, the unique semistandard tableau `T̂_g` of
  shape `(2n−2, 2)`, content `2 × n` (row 2 forced to be `2 2`) spans `HWV_{(2n−2,2)}(Sym^2 Sym^n)`
  by (5.6). That space is 1-dimensional by the classical `Sym^2 Sym^n = ⊕_{j even} S_{(2n−j,j)}`
  (**ADOPTED**, classical, not re-proved here). So `g := f_{T̂_g} ≠ 0`. At `n = 5` this is also
  **CERTIFIED by exact evaluation**: pilot 1 found `g = −8, −656, −13068` at three integer points
  (a nonzero exact value proves nonvanishing, given the implementation). Likewise `h`, shape
  `(6,4)`, content `2 × 5`: pilot 2 found it nonzero at 4 of 5 points. The coordinate ring is a
  domain, so `g^j h^{j′}` is nonzero; by Lemma A it is the tableau function of the column
  concatenation, whose graph is `j + j′` disjoint edges: **weight `(8j+6j′, 2j+4j′)`, tail
  `2j + 4j′` (unbounded), `τ = 1`, member of `𝔉_{<3}`**.
- **Legal weights.** Concatenating the columns of tableaux on disjoint entry sets and sorting
  them by length gives a partition shape of `n·d` with at most `max ℓ(μ_C) ≤ r` rows.
- **Width.** `τ(G_T̂) = max_C τ(G_{T̂_C}) ≤ k − 2` on `𝔉_{<k}`; `w ≤ W(n,r)`; decomposition
  given by construction (bags = components). So every member is evaluable in
  `W(n,r)^{ω(k−1)} poly(d,n,r)` — **cheap, large-tail, nonzero, and never separating.**
- **Scope of the nonvacuity.** The members exhibited have **two rows**. A nonzero member of
  `𝔉_{<8}` with five rows (which needs a nonzero single five-row tableau function of degree
  `5..7`) is **not established** here; the no-go does not need one.

### 4.4 What Theorem B does **not** exclude — the surviving corner (OPEN)

1. **Spans.** The argument is about a product in a prime ideal and has no analogue for sums: in
   the prime ideal `(xy − zw) ⊂ C[x,y,z,w]` the element `xy − zw` is a sum of products none of
   whose factors lies in the ideal. So a linear combination of members of `𝔉_{<D*}` is **not**
   excluded. Whether `I(D_r^{det_n}) ∩ span 𝔉_{<D*}` (in some cell) contains an element nonzero
   on `P_r` is OPEN.
2. **Connected fillings of small treewidth.** A connected component on `≥ D*` vertices can have
   small treewidth (a chain of length-2 columns gives a path, `τ = 1`; B24-04's cycle example is
   connected). The only lower bounds on record for a separating single `f_T̂` are
   `τ(G_T̂) ≥ ℓ(λ) − 1` (the tallest column is a clique; `≥ 4` at five rows) and
   `τ(G_T̂) ≥ τ(G_{T̂_C}) ≥ ℓ(μ_C) − 1` for the separating component, which need not contain the
   tallest column.
   Nothing here shows that bounded-treewidth connected components cannot separate. OPEN.

Compatibility with the tail theorem: every separating single `f_T̂` has a component of tail
`≥ D*` (Theorem B) and so `t ≥ D*` (Theorem 1 also gives this directly). Nothing in this slot
converts large tail into large treewidth; B24-04 Lemma 2 remains one-directional.

---

## 5. Pilots (two of three allowed; controls, not proofs)

| pilot | preregistration | price given before launch | actual | receipt |
|---|---|---|---|---|
| `b25_04_p1_factor` | `PREREG_b25_04_p1.md` `101c086e…6516` | < 5 s, < 100 MiB | **0.019 s, peak job 31.6 MiB, exit 0** | `results/logs/b25_04_p1_factor_resources.json` (`ac95ab09…1d4b`) |
| `b25_04_p2_nonvacuous` | `PREREG_b25_04_p2.md` `d67ff534…f5a4` | < 2 s, < 100 MiB | **0.013 s, exit 0** | `results/logs/b25_04_p2_nonvacuous_resources.json` |

Total mathematical wall time **≈ 0.03 s of 180 s**. Both wrapped by `analysis/b15_bound.py`
(`ca001081…`, Job Object enforced, `--seconds 60 --memory-mb 512`, one process, BLAS threads 1).
Each script prints and asserts its preregistration hash before any mathematics; pilot 2 also asserts
pilot 1's output hash and executes only pilot 1's function-definition prefix, so both use the same
evaluator. Both are exact integer computations of (5.2) at seeded integer Waring points, `n = 5`,
`r = 3`.

**Lease.** Before each run: the lease directory was empty, no `python.exe` was running, and no
batch resource receipt was newer than 2026-09-21T00:00Z. The lease was acquired with
`os.open(…, O_CREAT | O_EXCL | O_WRONLY)` at 03:45:12Z and 03:46:34Z, copied to
`results/b25_04/lease_acquired_copy.json` and `lease_acquired_copy_p2.json`, and removed by me only
after the job had exited, the receipt was written, and a byte comparison confirmed it was still my
record (released 03:45:26Z and 03:46:35Z).

**Results.**

- **Pilot 1, all assertions passed.** K1: `g ≠ 0` (values above). K3: `g` invariant under three
  lower-unitriangular substitutions and scaling as `α_1^8 α_2^2` under a torus element — this
  confirms the "top square submatrix" orientation I use. Controls: a column with a repeated entry
  gives 0 (BDI Lemma 5.5); `g(x_1^5) = 0`; weighted and repeated Waring decompositions give equal
  values. Isolated-vertex check: `f = g · c_{5e_1}` at 5 points with both factors nonzero.
- **Pilot 1's K2 was vacuous, reported as such.** Its three-vertex factor (columns
  `(1,2,3),(1,2)`, shape `(12,2,1)`) was `0` at all five points, so the component product was
  checked only as `0 = 0`. Incidentally this is a semistandard tableau whose function vanished at
  every sampled point — MEASURED only; not claimed identically zero, and not used.
- **Pilot 2 replaced K2 non-vacuously.** `f_T = g · h` (components `{1,2},{3,4}`, `λ = (14,6)`)
  and `f_{T5} = g · h · c_{5e_1}` (plus an isolated vertex, `λ = (19,6)`) at 5 points, with all
  factors nonzero at 4 of them. Component sets were computed and asserted.

These checks confirm that I read (5.2) correctly. They do not prove Lemma A (the hand proof does),
and finite agreement proves no polynomial identity.

---

## 6. Cost accounting (the question's six quantities, kept separate)

For the family `𝔉_{<D*}` the total certification cost is moot: its members are never separating
(Corollary B). The accounting below applies to the **surviving corner** (§4.4) and is a price,
not a claim that anything there exists.

| quantity | value, with its basis |
|---|---|
| **Evaluation** (one `f_T̂` at one point) | `W(n,r)^{ω(τ+1)} poly(d,n,r,|𝒯|)`, BDI Thm 7.2 as read. At five rows `τ ≥ 4`, so with `W(5,5) = 15` the matrix side bound is `15^5 = 759 375` and the bound per product is `15^{5ω}`: `≈ 10^{13.9}` at `ω = 2.371`, `4.4·10^{17}` at `ω = 3`. These are **upper bounds** from the theorem; they are not measured, and the sparsity of (7.14) is not exploited in them. They are polynomial in `d`, and exponential only in `τ`. |
| **Construction / storage** | Tableau: `nd` boxes. Point: a width-`≤ W(n,r)` ncABP with `n` layers and edge labels in `C^r`, built from catalecticant ranks (Prop. 6.8). Constant at fixed `(n,r)`, exact constant unpriced. |
| **Graph / decomposition** | `G_T̂` in `O(Σ_c ν_c^2) ≤ O(ndr)`. **BDI assume the decomposition is given.** For a designed family it comes with the construction (e.g. bags = components, or consecutive column-cliques for a chain) at `O(λ_1)` cost. For an arbitrary tableau, finding an optimal decomposition is a separate problem that BDI do not address; the general hardness and fixed-`τ` algorithms are **UNREAD** here and not relied on. |
| **Number of generators** | By (5.6), the semistandard tableaux of shape `λ`, content `d × n`: the Kostka number `K_{λ,(n^d)}`. Restricting to `τ ≤ τ_0` gives a subset `S_{τ_0}(λ)` of unknown size. |
| **Independent functions** | `dim span S_{τ_0}(λ) ≤ a_λ := mult(S_λ, Sym^d Sym^n) ≤ K_{λ,(n^d)}`. **None of these is `N_S(λ)`.** By the standard weight-multiplicity identity (ADOPTED), `N_S(λ) = Σ_{μ ⊵ λ} a_μ K_{μ,λ} ≥ a_λ`. B24-04's `min N_S ≥ 231` (unconditional, at `t ≥ 8`, `n = r = 5`) is a weight-space count, not a count of tableaux or of HWVs. |
| **Rank / kernel** | For a span candidate: evaluate `|S|` functions at `M` points of `D_r^{det_n}`: `|S|·M` evaluations plus `O(|S|·M·min(|S|,M)^{ω−2})` field operations. A sampled rank is a **floor** (G27). The sampled kernel contains `I ∩ span S` and need not equal it. |
| **Membership certificate** | Kernel vectors from samples are **not** proved to lie in `I(D_r^{det_n})`. A proof is the identity `F(A) := f(det_n(x_1 I + Σ_{i≥2} x_i A_i)) ≡ 0` (homogeneity plus `A_1` invertible on a dense set reduces to `A_1 = I`), a polynomial of degree `≤ dn` in `(r−1)n^2` variables. Deterministic grid certificate: `(dn+1)^{(r−1)n^2}` points — **`41^{100} ≈ 10^{161}` at `n = r = 5`, `d = 8`**. Schwartz–Zippel with `k` random points has error `≤ (dn/s)^k` for a sample set of size `s`, so it is cheap, but it is a probabilistic certificate, not a proof. |
| **Nonvanishing on `P_r`** | One exact nonzero value at one point of `P_r` **proves** `f|_{P_r} ≠ 0`. `|S|` evaluations for a combination, one for a single tableau. |

**Total, for a single connected tableau candidate** (`|S| = 1`): `(k + 1) · C_eval(τ)` for a
probabilistic certificate (k Schwartz–Zippel points plus one point of `P_r`), or
`((dn+1)^{(r−1)n^2} + 1) · C_eval(τ)` for a deterministic one. **For a span candidate:**
`|S|·(M + k + 1)·C_eval(τ_0) + C_rank(|S|, M)` probabilistic, with the deterministic membership
term again `|S|·(dn+1)^{(r−1)n^2}·C_eval`. In both, the cheapness BDI provides is the evaluation.
It supplies neither the independent functions nor a proof of membership.

---

## 7. Verdict, reopening condition, and the single next certificate

**Answer to the exact question.** Yes, there is a large nonzero family of highest-weight
constructions with unbounded tail and bounded treewidth: disconnected fillings, `𝔉_{<k}`. But
**no member with `k ≤ D*` is separating (Theorem B, PROVED modulo primality; at `k ≤ 8` modulo the
record's floor)**, so this family's cheap evaluation certifies nothing useful. The mechanism that
makes treewidth small without making the tail small (splitting the filling into many small
components) is exactly the one that factors the function, and a factored function separates only
through one factor of degree `≥ D*`. **Outcome (2).**

**What remains open, precisely.** (a) Connected fillings: a single `f_T̂` whose separating
component has `≥ D*` vertices and small treewidth (paths, cycles, trees of cliques). (b) Linear
combinations of members of `𝔉_{<D*}` or of bounded-treewidth tableaux.

**Reopening condition.** This negative stops binding if either (a) or (b) acquires a candidate.
That requires a nominated cell, which this slot is not funded to search for.

**Single next required certificate.** For one nominated cell with `t ≥ D*`: a **connected**
tableau `T̂` with `τ(G_T̂) ≤ τ_0` together with (i) one exact nonzero value of `f_T̂` at a point of
`P_r`, and (ii) a proof of the identity `f_T̂(det_n(x_1 I + Σ x_i A_i)) ≡ 0`. The price is
(i) one BDI evaluation, and for (ii) either `(dn+1)^{(r−1)n^2}` evaluations deterministically or
a structural proof. A Schwartz–Zippel run gives only a probabilistic certificate for (ii) at
`k + 1` evaluations. Until a cell is nominated by a funded slot, this certificate cannot be
executed, and no search is proposed here.

---

## 8. Ledger

| # | statement | label | method |
|---|---|---|---|
| L1 | Lemma A: `f_T̂ = Π_C f_{T̂_C}` over components of `G_T̂`; isolated vertices give `c_{ne_1}` | **PROVED** from BDI (5.2) (PRIMARY, HTML); well-definedness ADOPTED from BDI | hand proof; pilots 1–2 MEASURED consistency (pilot 1 K2 vacuous, pilot 2 non-vacuous) |
| L2 | Theorem B: a separating single `f_T̂` has a separating component `C`, `|C| ≥ D*`, tail(`μ_C`) `≥ D*` | **PROVED modulo** primality of `I(D_r^{det_n})` (as Theorem 1) | hand proof |
| L3 | Corollary B: no member of `𝔉_{<D*}` separates; none with all components `≤ 7` vertices separates | **PROVED modulo** L2's premise; the "`≤ 7`" form also modulo the record's floor `D* ≥ 8` (READ, not re-derived) | hand proof |
| L4 | `𝔉_{<3}` has nonzero members of unbounded tail with `τ = 1` (`g^j h^{j′}`, two rows) | **PROVED** modulo the classical `Sym^2 Sym^n` decomposition (ADOPTED); `g, h ≠ 0` also **CERTIFIED by exact evaluation** at `n = 5` (producer-only) | hand + pilots 1–2 |
| L5 | A five-row nonzero member of `𝔉_{<8}` | **not established** | — |
| L6 | The no-go does not transfer to spans (`xy − zw` example) | **PROVED** (the argument does not transfer); whether spans separate is **OPEN** | hand |
| L7 | Connected small-treewidth fillings are not excluded | **OPEN** | — |
| L8 | Thm 7.2 input model: tableau, ncABP and decomposition all **given**; cost `w^{ω(τ+1)} poly(d,n,r,|𝒯|)` in project variables | **PRIMARY**, read in statement and proof | READ |
| L9 | `w ≤ W(n,r)`; `W(5,5) = 15` | **PROVED** (Prop. 6.8 PRIMARY + arithmetic) | hand |
| L10 | The deterministic membership grid is `(dn+1)^{(r−1)n^2}`, `≈ 10^{161}` at `n = r = 5`, `d = 8` | **PROVED** (arithmetic on a standard grid bound) | hand |
| L11 | Evaluation bounds `≈ 10^{13.9}` (`ω = 2.371`) / `4.4·10^{17}` (`ω = 3`) per internal node at `τ = 4`, `w = 15` | upper bounds from Thm 7.2, **not MEASURED** | arithmetic |
| L12 | `(12,2,1)` semistandard tableau function vanished at 5 sampled points | **MEASURED** only; not used | pilot 1 |
| L13 | `N_S`, `K_{λ,(n^d)}`, `a_λ` are distinct; `a_λ ≤ K`, `a_λ ≤ N_S` | **PROVED** modulo the standard weight-multiplicity identity (ADOPTED) | hand |

No cell is nominated; no equation, separation, padding statement or gap is claimed; no finite
sample is read as membership; the 70-pattern basis and B24-04's extrapolation are not used.

---

## 9. Files, hashes, limitations

**Created by this slot (all UNCOMMITTED, untracked):**

```
docs/b25_04_report.md
analysis/b25_04_p1_factor.py              cee1d087c3b3c68366539738ddffab434a47319f57a9f041fd2532e05a5a76a5
analysis/b25_04_p2_nonvacuous.py          be3cb85bce4177a114e61d4b35d3c546b429d428666df51931cc0db847e8059f
results/b25_04/THEORY_GATE.md             a86e41d65a40bd9c1e3e42e216d4b5db6aab605bad678a9d2e2b24644545518e
results/b25_04/PREREG_b25_04_p1.md        101c086e9916f5280d78db5397c6ddbc889a13ebf0a1a11316e58688fbfb6516
results/b25_04/PREREG_b25_04_p2.md        d67ff53405d7e438e5c1cb42c0989e2e5488d0ece271e1701acb07407a8cf5a4
results/b25_04/p1_factor.json             cc6031c8ed9fe6a354e53676fc03e21426feae661fbbfa70e5581e2f1ed40ce5
results/b25_04/p1_stdout.txt              a99d8cab50baaee75f5dfa9d60cafd57bc790ef0b3126556376126fcac697a9f
results/b25_04/p2_nonvacuous.json, p2_stdout.txt, lease_acquired_copy.json, lease_acquired_copy_p2.json,
results/b25_04/STATUS.md, results/b25_04/MANIFEST.json
results/logs/b25_04_p1_factor_resources.json, results/logs/b25_04_p2_nonvacuous_resources.json
results/logs/b25_04_p1_factor.pid, results/logs/b25_04_p2_nonvacuous.pid   (gitignored: .gitignore:51
    `results/logs/*.pid`, no `b25_04_` negation — already recorded by B25-12 as D1; not edited here)
```

The complete hash list, including this report, is in `results/b25_04/MANIFEST.json`. The
manifest does not hash itself. All digests name **UNCOMMITTED** states. No existing file was
modified. The shared lease file was created and deleted twice by this slot (§5) and does not exist
now.

**Limitations.**

1. The no-go concerns **single** tableau functions. Spans and connected fillings are open (§4.4).
2. Nonvacuity is shown with two-row members only.
3. BDI is read from a hashed HTML rendering whose arXiv version ar5iv does not state; the PDF v2 is
   hashed but not text-read.
4. BDI's well-definedness of (5.2) and the classical `Sym^2 Sym^n` decomposition are ADOPTED.
   The floor `D* ≥ 8` is the record's and was READ, not re-derived.
5. Producer only (G18). The pilots replay my own evaluator; the only external cross-check is that
   the torus weight and Lemma 5.5 controls come out as BDI's text predicts.
6. **Tool memory:** one new memory entry records this outcome for future sessions. It is not
   evidence.
