# B24-05 — Do `D`-module invariants escape the direction reversal? The gate, and the negative

20 September 2026 (UTC). Slot 05, Batch 24. Worktree `work/batch15_workers/B24-05`, branch
`b24-05-dmodule`. Author: Claude (Opus 5, 1M context), default permission mode. Producer only
(G18). Theory and literature only: the gate of §1 was not passed, so no pilot was priced or run.
Git read-only throughout (`rev-parse`, `status`, `show`, `log`, `cat-file`, `check-ignore`). No
commit, push, fetch, stash or checkout.

**Provenance, recorded before any write (2026-09-20T03:28:13Z):**

```
git rev-parse HEAD                82633a60893236fab4fbc317df416e1b8a349005   (= the launch prompt's pin)
git rev-parse HEAD^{tree}         e82fd3291d1a2adc8a577647314c251366ff5142
git rev-parse --abbrev-ref HEAD   b24-05-dmodule
git status --porcelain            empty (clean worktree; no untracked receipts)
```

**Notation (G13, G24).** `N` is the number of variables; the letter `L` is not used in this
packet. `delta_0` is not used. `D45` = closure of `{det_4(sum_{i<=5} x_i A_i)}` in `Sym^4 C^5`;
`D35` = the same for `3 x 3` in `Sym^3 C^5`; `P5 = closure{l·C}` with `l` linear and `C` a
quinary cubic; `C*` a smooth cubic threefold and `F* = l·C*` (B17-01-C, ADOPTED). `Det_n =
closure(GL_{n^2} · det_n)` inside `Sym^n C^{n^2}`, and the padding point there is
`x_0^{n-m} per_m`. `m` is the permanent size, `n` the determinant size. Every dimension is marked
**aff** or **proj** at the point of use. For a nonzero `F`, `b_F(s)` is the Bernstein–Sato
polynomial of `F` on `C^N`, in the normalisation `P · F^{s+1} = b_F(s) · F^s`;
`lct(F) := −(largest root of b_F)`; the **minimal exponent**
`alphatilde(F) := −(largest root of b_F/(s+1))`. `CC` is a characteristic cycle.

---

## 0. What this slot can and cannot establish

**What a positive would have been.** A polynomial `f` in the 70 coefficients of a quinary quartic
(or in the coefficients of an `n`-ic in `n^2` variables), PROVED to vanish on `D45` (resp. on
`Det_n`) and exhibited nonzero at an actual padding point. That is a **separation**: the **third**
of the programme's four achievements, **never the fourth**. It would not be a gap, it would not
select a cell, and it would not bound any multiplicity.

**What this slot delivers.** The literature pass (§1.1), then the negative. The gate was not
passed by either sub-candidate. No cell is nominated, no gap is claimed, no equation is produced,
and no `b`-function of any quinary quartic is computed, attempted or priced (explicitly out of
scope).

**The three findings a reader should take away.**

1. **The literature pass is a clean negative in both directions** (§1.1). I found no work
   applying Bernstein–Sato or `D`-module invariants to permanent-versus-determinant, or to orbit
   closures in GCT — so the idea has *not* been done and killed, and the cheap exit the brief
   allows was not available: the gate had to be run here. What the literature does supply is the
   exact sentence the candidate needed to survive and does not get: Ikenmeyer–Kandasamy, on
   orbits versus orbit closures (PRIMARY, quoted in §1.1).

2. **Sub-candidate A escapes B22-02's Lemmas 1.3 and 1.4 — and dies one step later, on the
   orbit/closure gap, which is the brief's own third named death.** The `b`-function is a
   `GL_N`-invariant, so it is constant on the *orbit* `GL_{n^2}·det_n`, where Cayley's identity
   gives `(s+1)(s+2)···(s+n)`. It is **not** inherited by the *closure*: `x_{11}^n` lies in
   `Det_n` (Lemma D2), and `b_{x^n}(s) = prod_{i=1}^{n}(s + i/n)` has `n−1` non-integral roots
   (Lemma D1, proved here from scratch). Per the brief's own instruction — *"if the distinction
   only holds on the orbit, the candidate is worthless here — say so and stop"* — that is where A
   stops. Four further independent kills are recorded in §1.3.

3. **Sub-candidate B escapes Lemmas 1.3 and 1.4 too, and dies on Lemma 1.1 itself** — the lemma
   the brief hoped it would sidestep. Characteristic-cycle multiplicities along the deeper strata
   *are* transverse Milnor numbers: upper-semicontinuous, and **larger** on padding, which is
   B22-02 §1.1's failing branch. The degree-type statistics of the same cycle (the polar
   multiplicities, whose alternating sum is the class) are lower-semicontinuous and **drop** on
   padding, which is row 4. There is no third kind of number in a characteristic cycle.

**The reusable by-product** is Corollary D2′: *every* `GL`-invariant, non-magnitude property of a
form that holds at `det_n` and fails at a pure power `x^n` is orbit-only and yields no closed
condition containing `Det_n`. That disposes in one line each of integrality of `b`-function roots,
prehomogeneity, rational/klt/canonical singularity type, reducedness and irreducibility of `X_F`,
and the dual variety being a hypersurface. It is a new exclusion of the same kind and scope as
B22-02's Lemmas 1.3–1.4, and it is what the integrator's idea, properly written down, actually
yields.

**What this does not establish.** It is not a theorem that no `D`-module construction exists. It
gives no equation, no degree, no gap, no cell, no carrier. It says nothing about `b_{per_m}` or
about the `b`-function of any member of `D45`. The literature finding is a *search* negative, not
a proof of absence.

---

## 1. The literature pass, then the gate

### 1.1 The literature (G14, G14′), before any argument

Four searches were run: Bernstein–Sato / `b`-function × GCT and orbit closures; `D`-module
characteristic cycle × permanent-versus-determinant; `b`-function of the permanent and of the
determinant; log canonical threshold / minimal exponent × padded permanent. **No work applying
`D`-module or Bernstein–Sato invariants to permanent-versus-determinant, or to orbit closures in
GCT, was found.** I read titles, abstracts, and — where quoted below — fetched text. I did not
reach a survey that asserts the gap, so this is a search negative and is labelled as one (M1).

| item | what was read, and what it says | label (G14′) |
|---|---|---|
| Ikenmeyer–Kandasamy, *Implementing geometric complexity theory: on the separation of orbit closures via symmetries*, arXiv **1911.03990v1** | Abstract page fetched this session, quoted verbatim: *"Understanding the difference between group orbits and their closures is a key difficulty in geometric complexity theory (GCT): While the GCT program is set up to separate certain orbit closures, many beautiful mathematical properties are only known for the group orbits, in particular close relations with symmetry groups and invariant spaces, while the orbit closures seem much more difficult to understand."* | **PRIMARY** (abstract level). Corroborative only: §1.3 death 3 is proved independently by Lemmas D1–D2 |
| Caracciolo–Sokal–Sportiello, *Algebraic/combinatorial proofs of Cayley-type identities for derivatives of determinants and pfaffians*, arXiv **1105.6270** | ar5iv rendering fetched. Theorem 2.1, verbatim: `det(∂)(det X)^s = s(s+1)···(s+n−1)(det X)^{s−1}`, presented there as a Bernstein–Sato pair with `b(s) = s(s+1)···(s+n−1)`. **Shift note.** That is the `f^s → f^{s−1}` normalisation. In the `f^{s+1} → f^s` normalisation used here and in the brief, substitute `s → s+1`: `b_{det_n}(s) = (s+1)(s+2)···(s+n)`. The brief's form is correct **after** the shift and only after it | **PRIMARY** (ar5iv HTML; ar5iv does not state which arXiv version it renders). Load-bearing for `alphatilde(det_n) = 2` in Lemma D3 |
| X. Lin, *The Bernstein–Sato polynomial of the Hankel determinant*, arXiv **2609.19763** | HTML fetched. Quoted verbatim from the proof of Thm 2.2: *"The global assertion follows because the global Bernstein–Sato polynomial is the least common multiple of the local polynomials."* Used for exactly that, and only that: it is how Lemma D3(ii) passes from one local normal-crossing point to the global `alphatilde` | **PRIMARY** for that one sentence |
| Lőrincz–Raicu–Walther(–Weyman), *Bernstein–Sato polynomials for maximal minors and sub-maximal Pfaffians*, arXiv 1601.06688 | Search-result level only. Reported statement: *"basic instances such as the b-functions for determinantal varieties are still not understood."* Recorded as corroboration that computing `b` for a member of `D45` is not cheap — consistent with the brief putting it out of scope | **UNREAD-SPECIALIST**; not load-bearing |
| Mulmuley–Sohoni, *GCT IV: nonstandard quantum group for the Kronecker problem*, arXiv cs/0703110 | Title and search-result level only. Recorded in §1.5: the field's `q`-analogue of the Kronecker problem runs through a nonstandard quantum group and Hecke algebra, **not** through a statistic on conjugacy classes | **UNREAD-SPECIALIST**; not load-bearing |
| Semicontinuity of `lct` / of the minimal exponent in families (Varchenko; Mustață–Popa and successors) | Search-result level only; no text fetched | **UNREAD-SPECIALIST**. **Explicitly not load-bearing**: Lemma D3's kill is by *values*, not by semicontinuity. Semicontinuity is cited only to name which closed condition one would extract, and that is B22-02 §1.1's framework in any case |
| Kashiwara (roots of `b_f` are negative rational), Malgrange, Lichtin; the index theorem for characteristic cycles | Not fetched | **UNREAD-CLASSICAL**. None is used in a PROVED row except the index theorem in M11/B3, whose kill survives any reasonable form of it (see §1.4) |

**PDF text extraction was unavailable in this environment.** Two attempted PDF reads (a
Bernstein–Sato survey; M. Popa's lecture notes) returned unparsed streams and were abandoned;
nothing from them is used anywhere. Every quoted sentence above comes from an HTML rendering
fetched this session.

**Consequence for this slot.** The candidate has not been done and killed, so the brief's cheap
exit did not apply and the gate below had to be run.

### 1.2 Three lemmas the kills rest on (PROVED; D1 and D2 entirely self-contained)

**Lemma D1 (the `b`-function of a pure power).** Let `N >= 1`, `k >= 1` and `f = x_1^k` in
`C[x_1, …, x_N]`. Then

> `b_f(s) = prod_{i=1}^{k} (s + i/k)`,  with roots `−1, −(k−1)/k, …, −1/k`.

In particular, for `k >= 2` exactly `k−1` of the roots are **not** integers, and for `k = 1`
the single root is `−1`, an integer.

*Proof.* Write a general element of the Weyl algebra with parameter as
`P = sum_{alpha, beta} c_{alpha beta}(s) · x^alpha ∂^beta`. Since `∂_j(x_1^{k(s+1)}) = 0` for
`j >= 2`, only `beta = (b, 0, …, 0)` contributes, and
`∂_1^b x_1^{k(s+1)} = [k(s+1)]_b · x_1^{k(s+1)−b}` with `[t]_b := t(t−1)···(t−b+1)`. Hence

```
P · f^{s+1}  =  sum_{b} sum_{alpha} c_{alpha b}(s) [k(s+1)]_b · x_1^{alpha_1 + k(s+1) − b} x_2^{alpha_2} ··· x_N^{alpha_N}.
```

Distinct `(alpha_2, …, alpha_N)` and distinct `alpha_1 − b` give distinct monomials, so there is
no cancellation across them. To obtain `b(s) · f^s = b(s) · x_1^{k(s+1)−k}` one therefore needs
`alpha_2 = ··· = alpha_N = 0` and `alpha_1 − b = −k`, i.e. `alpha_1 = b − k >= 0`, i.e. `b >= k`.
So the set of `b(s) ∈ C[s]` with `b(s) f^s ∈ D[s]·f^{s+1}` is the `C[s]`-ideal generated by
`{ [k(s+1)]_b : b >= k }`. For `b >= k` one has `[k(s+1)]_b = [k(s+1)]_k · [k(s+1)−k]_{b−k}`, so
that ideal is `([k(s+1)]_k)`, whose monic generator is

```
k^{−k} · [k(s+1)]_k  =  prod_{j=0}^{k−1} (s + 1 − j/k)  =  prod_{i=1}^{k} (s + i/k)      (i = k − j).  ∎
```

*Checks.* `k = 1` gives `s+1`. `k = 2` gives `(s+1)(s+1/2)`, the textbook value for `x^2`.

**Lemma D2 (pure powers lie in the determinantal orbit closures).**

(a) `x_1^4 ∈ D45` — and in the *image*, not merely the closure: take `A_1 = I_4` and
`A_2 = ··· = A_5 = 0`, so `det_4(sum_i x_i A_i) = det_4(x_1 I_4) = x_1^4`.

(b) `x_{11}^n ∈ End(C^{n^2}) · det_n ⊆ Det_n` for every `n >= 2`: the map `A : X ↦ x_{11} · I_n`
is linear in the entries of `X` and `det_n(A(X)) = x_{11}^n`; `GL` is dense in `End` and
`(A, f) ↦ f ∘ A` is continuous, so `f ∘ A ∈ closure(GL · f)`. ∎

**Corollary D2′ (what Lemma D2 excludes, in general).** Let `Q` be any property of forms that is
invariant under `GL_N` and holds at `det_n`. If `Q` fails at the pure power `x^n`, then `Q` fails
somewhere on `Det_n`; so `Q` is a property of the **orbit** and not of the orbit closure, and no
closed condition extracted from `Q` contains `Det_n`. Since `x^n ∈ Det_n` always, this disposes
at once of: integrality of the roots of `b_F` (by Lemma D1); prehomogeneity of the generic
stabiliser; `X_F` having rational, klt or canonical singularities; `X_F` being reduced or
irreducible; and `X_F^vee` being a hypersurface (for `F = x^n` the dual is a single point, `0`
proj). ∎

*Remark.* Corollary D2′ is the honest general form of the integrator's idea, and it is a genuine
addition to the record. B22-02's Lemma 1.3 excludes constructions that go through `r x r` minors
of a derivative matrix, and Lemma 1.4 excludes `SL_5`-covariants into a determinantal locus. D2′
excludes a class that goes through neither: every `GL`-invariant qualitative property that
distinguishes the smooth-ish determinant from a degenerate limit.

**Lemma D3 (the two magnitude statistics the `b`-function offers are both reversed).**

(i) **`lct` is vacuous, not merely reversed.** For every non-constant `F`, `lct(F) <= 1` (take a
log resolution; the strict transform of `div F` appears with coefficient `>= 1` and discrepancy
`0`). By Cayley, the largest root of `b_{det_n}` is `−1`, so `lct(det_n) = 1`. A closed condition
`{lct <= c}` containing `Det_n` therefore needs `c >= 1`, and `{lct <= 1}` is the whole space.

(ii) **The minimal exponent is reversed.** By Cayley, `b_{det_n}/(s+1) = (s+2)···(s+n)`, whose
largest root is `−2`, so `alphatilde(det_n) = 2`. At a padding point:

- for `x_0^{k} per_m` with `k := n−m >= 2`, at any point with `x_0 = 0` and `per_m ≠ 0` the germ
  is `x_0^k` times a unit, so by Lemma D1 the local reduced `b` has largest root `−(k−1)/k` and
  `alphatilde <= (k−1)/k < 1`;
- for `k = 1`, and for the record's `F* = l·C*`, at a generic point of `{l = 0} ∩ {C* = 0}` the
  germ is a normal crossing `uv`, whose local `b` is `(s+1)^2`, reduced `(s+1)`, so
  `alphatilde <= 1`.

Global `b` is the least common multiple of the local ones (Lin, PRIMARY, §1.1), so the global
`alphatilde` is the minimum of the local ones and the bounds above are global. Hence a closed
condition `{alphatilde <= c}` containing `Det_n` needs `c >= 2`, and **every padding point then
satisfies it**. ∎

*Note on what D3 uses.* The kill in (ii) is by **values only** — `2` against `<= 1` — not by
semicontinuity. Semicontinuity of `alphatilde` is cited (§1.1, UNREAD-SPECIALIST) solely to
identify `{alphatilde <= c}` as the closed condition one would extract. If it were withdrawn, the
candidate would have no closed condition at all, which is worse for it, not better.

### 1.3 Sub-candidate A — Bernstein–Sato root integrality: the gate

**The recipe, stated as a polynomial condition, as the gate demands.** Set
`Z_int := {F ∈ Sym^d C^N : every root of b_F lies in Z}` and `Z := closure(Z_int)`. The proposed
separating polynomials are the elements of `I(Z)` — an ideal in the `70` coefficients at
`(d, N) = (4, 5)`.

**Escape paragraph against B22-02 Lemma 1.1.** Granted, and stated precisely so a reviewer can
check it. The statistic is not an integer-valued `q`, and the condition is not a threshold
`{q >= c}` or `{q <= c}`; so **neither branch of Lemma 1.1 applies to integrality directly**.
`b_F` is also not a polynomial in `F` at all — it is a constructible function of `F` — so
Lemma 1.2 does not apply either. That much of the brief's hope is correct, and it is why A had to
be taken seriously rather than waved through.

**The three named deaths, addressed in turn. None is assumed past.**

**Death 2 first, because the brief called it the dangerous one, and because it is the one A
survives.** Lemma 1.3 concerns a matrix `M(F)` whose entries are polynomials in `F`, and
conditions built from its `r x r` minors. `b_F` is not such a minor: it is the monic generator of
the ideal `{ b(s) : b(s) F^s ∈ D[s] F^{s+1} }`, obtained by elimination in the Weyl algebra, whose
Gröbner data depend on `F` in no fixed-size, fixed-shape way. The argument *is* the gate, so here
it is in its weakest honest form: **I have no construction of `b_F` as a minor of a matrix
polynomial in `F`, and neither does any literature I reached** (§1.1 records the field describing
`b`-functions of determinantal varieties as not understood). Lemma 1.4 likewise does not reach
the candidate: `Z_int` is `GL_N`-stable, but `I(Z)` is not obtained by composing a covariant into
a determinantal locus. **Death 2 is survived, and so is Lemma 1.4.**

**Death 3 — prehomogeneity is about the orbit, not the closure — kills it.** [PROVED]
`b` is a `GL_N`-invariant, because a linear change of coordinates is an automorphism of the Weyl
algebra; so `b_{g·det_n} = b_{det_n} = (s+1)···(s+n)` for every `g ∈ GL_{n^2}`, and integrality
holds identically on the **orbit**. It fails on the **closure**, and not somewhere exotic —
already on `End · det_n`: by Lemma D2(b), `x_{11}^n ∈ Det_n`, and by Lemma D1 its `b`-function has
the `n−1` non-integral roots `−1/n, …, −(n−1)/n`. The brief's instruction applies verbatim:
*"If the distinction only holds on the orbit, the candidate is worthless here — say so and
stop."* **I say so, and stop.** Ikenmeyer–Kandasamy (PRIMARY, §1.1) is the field stating the same
obstacle in general; Lemmas D1–D2 are its proved instance here.

**Death 1 — the closure trap — is real too, and is why the obvious repair fails.** [ASSESSED]
The repair is to drop `Z_int` for its closure `Z`. Then `Det_n ⊆ Z` holds for free, since the
orbit is dense in `Det_n` and lies in `Z_int`. But the repair needs two things it does not have.

- **(i) `I(Z)` as a polynomial condition on the coefficients.** None exists on record or here. By
  death 2's own argument `b_F` is not a minor, so there is no resultant, Fitting or elimination
  construction in the coefficients; the only known computations of `b_F` are per-point Gröbner
  eliminations in the Weyl algebra, which do not assemble into an ideal of a family.
- **(ii) A proof that padding lies outside `Z`.** Since `Z ⊇ Det_n`, the statement "padding ∉ `Z`"
  is **strictly stronger** than "padding ∉ `Det_n`". A separation instrument must be an
  over-approximation that is *easier to test*; `Z` is a correct over-approximation that is
  **harder** to test, and nothing is known about it beyond `Z ⊇ Det_n` and
  `Z ⊇ closure{normal-crossing divisors}`. Deciding padding ∈ `Z` would require
  `b_{x_0^{n−m} per_m}`, hence `b_{per_m}`, which is unknown and whose determination is exactly
  the computation the brief puts out of scope.

**No recipe, no degree, no price.**

**Two further kills, independent of the above.**

**A-4 (the record's five-variable setting: the premise is absent, not merely orbit-bound).**
[PROVED] Cayley's identity computes `b` for `det_n` as a form in `n^2` variables. The record's
`D45` consists of **linear sections** `det_4(Λ(x))` with `Λ : C^5 → Mat_4`, and `b`-functions are
not preserved under restriction to a linear subspace. So the candidate has no premise at all on
`D45`: no point of `D45` is known to have integral roots, and `D45` demonstrably contains points
that do not — `x_1^4 ∈ D45` (Lemma D2(a)) has `b = prod_{i=1}^{4}(s + i/4)`, with the fractional
roots `−1/4, −1/2, −3/4` (Lemma D1). The `b`-function of a *generic* member of `D45` is **not
computed here** (out of scope) and is not needed: what is missing is the premise.

**A-5 (the arithmetic is empty at the record's cell).** [PROVED] The brief's mechanism is that
`l^{n−m}` contributes roots `−j/k` with `k = n−m`. By Lemma D1 that needs `k >= 2`, i.e.
`n >= m + 2`. At the programme's cell `(m, n) = (3, 4)` we have `k = 1` and `b_{x_0} = s + 1`:
**the fractional roots the candidate runs on do not exist there.** Where the mechanism does have
content — `m = 3`, `n >= 5` — B23-06 puts the instrument outside its own frontier (visible rows
exist iff `n <= m^2/2`, i.e. `n <= 4` at `m = 3`; B23-06 L18, PROVED), and puts the target itself
in the open: `5 <= dcbar(per_3) <= 7`, with *"Problem 2.4. Determine `dcbar(perm_3)`"* (Landsberg,
PRIMARY via B23-06 §1). So where the arithmetic bites, the target is unknown; where the target is
the record's cell, the arithmetic is empty.

**A-6 (the magnitude repairs).** [PROVED] Every repair that turns integrality into a number —
`lct`, the minimal exponent `alphatilde`, the lcm of the denominators of the roots, the count of
non-integral roots — is a magnitude statistic and lands back in Lemma 1.1's failing branches.
Lemma D3 disposes of `lct` (vacuous) and of `alphatilde` (reversed). The denominator and count
statistics are singularity-depth statistics: upper-semicontinuous and **larger** on the more
singular padding, which is Lemma 1.1's first branch.

#### A — the kill table

| # | form of the candidate | killing sentence | label |
|---|---|---|---|
| A1 | "All roots of `b_F` are integers", used on `Det_n` | `b` is `GL`-invariant, so integrality is an orbit property; `x_{11}^n ∈ Det_n` (D2) has roots `−i/n` (D1), so the orbit closure does not inherit it. The brief's death 3, realised | **PROVED-kill** |
| A2 | The same, used on the record's `D45 ⊂ Sym^4 C^5` | Cayley computes `b` in `n^2` variables, and `b` is not preserved by linear section. `x_1^4 ∈ D45` has roots `−1/4, −1/2, −3/4`. The premise is absent | **PROVED-kill** |
| A3 | The same, at the record's cell `(3, 4)` | `n − m = 1` and `b_{x_0} = s+1`: the fractional-root mechanism is vacuous. At `n >= 5` it is non-vacuous, and there both the instrument (B23-06 L18) and the target (`dcbar(per_3)` open) are out of reach | **PROVED-kill** |
| A4 | Repair: `I(closure(Z_int))` as an ideal in the coefficients | No construction of `I(Z)` exists — death 2's own argument forbids a minor/resultant recipe — and `Z ⊇ Det_n` makes "padding ∉ `Z`" strictly harder than the original question, needing `b_{per_m}`, which is unknown and out of scope | **ASSESSED-kill** (no recipe) |
| A5 | Repair: `lct` = `−`(largest root) | `lct <= 1` for every non-constant form and `lct(det_n) = 1`, so `{lct <= c} ⊇ Det_n` forces `c >= 1` and the condition is everything. Vacuous | **PROVED-kill** |
| A6 | Repair: minimal exponent `alphatilde` | `alphatilde(det_n) = 2` against `alphatilde(padding) <= 1`, so `{alphatilde <= c} ⊇ Det_n` forces `c >= 2 >= alphatilde(padding)`: Lemma 1.1, wrong direction | **PROVED-kill** |
| A7 | Repair: lcm of denominators, or the count of non-integral roots | Singularity-depth statistics: u.s.c. and larger on the more singular padding. Lemma 1.1, first branch | **PROVED-kill** |

### 1.4 Sub-candidate B — characteristic-cycle multiplicities: the gate

**The recipe, stated as the gate demands.** For `F ∈ Sym^4 C^5`, take the characteristic cycle
`CC = sum_Z m_Z [T^*_Z C^5]` of the perverse sheaf or `D`-module attached to `X_F`, and propose
closed conditions on the multiplicities `m_Z`.

**Escape paragraph against Lemmas 1.3 and 1.4.** Granted. `m_Z` is not a rank statistic of a
derivative matrix — it is a Lagrangian-cycle multiplicity — so L3 does not reach it; and it is
not an `SL_5`-covariant into a determinantal locus, so L4 does not reach it. The brief is right
about both. **It is Lemma 1.1 that kills it**, and that is what the brief did not anticipate.

**The escape paragraph against Lemma 1.1 does not exist, and here is why.** A characteristic
cycle contains exactly three kinds of number, and each is disposed of.

**B1 — the support.** The support of `CC` is a union of conormal varieties, and its dimension is
the `dim X_F^vee` statistic. That is B22-02 row 5 and Lemma 1.5(i); B23-06 L18 (PROVED) puts the
second fundamental form's blind zone at `N <= 2n`, with visible rows iff `n <= m^2/2` — the LMR
frontier, which at `m = 3` is `n <= 4`. Multiplicities change nothing here: the support is the
support. **PROVED-kill (record).**

**B2 — the multiplicity along the main component.** For `IC_{X_F}` the multiplicity along
`T^*_{X_reg}` is identically `1`. It carries no information about `F` and cannot separate
anything. **PROVED-kill.** (The value `1` is standard, UNREAD-CLASSICAL; the kill needs only that
it is independent of `F`, not that it is exactly `1`.)

**B3 — the multiplicities along the deeper strata.** By the index theorem these are, up to sign,
transverse Milnor numbers / local Euler obstructions of the strata. They are
**upper-semicontinuous** integer statistics, so the closed conditions they yield are
`{m_Z >= c}`, and by B22-02 §1.1 those separate only if padding is **smaller**. Padding is
larger, concretely and not merely in principle: a generic `F ∈ D45` has `Sing X_F` = 20 nodes
(`20` lines aff through the origin, `20` points proj), each of transverse type `A_1`, whereas the
padding point `F* = l·C*` is singular along the whole surface `{l = C* = 0}` (`3` aff / `2` proj),
with an `A_1` transverse type at its generic point **and** an origin where the multiplicity is
larger again. More strata, larger numbers. **PROVED-kill** — the direction reversal, wearing a
characteristic cycle.

**B4 — the degree-type statistics of the same cycle.** The polar multiplicities, whose
alternating sum is the class `deg X_F^vee`, are **lower-semicontinuous** and **drop** on padding:
`68` for a generic nodal member against `24` for `l·C` (B22-02 row 4, from B20-02 §4). Second
branch, fails. **PROVED-kill (record).**

**B5 — the recipe.** No polynomial condition on the 70 coefficients is exhibited by the
candidate, and the only route from a cycle multiplicity to a coefficient-side polynomial is a
semicontinuity threshold, i.e. B1–B4. **ASSESSED-kill** (no recipe).

**B6 — the restricted problem, recorded so nobody re-proposes it.** `D45 ∩ P5` contains
`{l·C : C ∈ D35}` (`32` aff; B22-02 §4), so any statistic separating `D45` from `l·C*` must
already separate `l·C_{det3}` from `l·C*` — that is, must separate on the cubic factor. There,
singularity statistics do run the **right** way, a smooth `C*` being less singular than a det3
cubic, exactly as B22-02 Lemma 1.6 records. Characteristic-cycle multiplicities are no exception
and no improvement: they inherit row 13's fate, which is that **no lift exists** — a covariant
lift sends `P5` into `D35` before one even asks the question (Lemma 1.4(c)), and the
Nullstellensatz lift is not constructive. **ASSESSED-kill (row 13, unchanged).**

*Consistency check on Corollary D2′.* At `x^n ∈ Det_n` the hypersurface `X_F` is a non-reduced
hyperplane and `X_F^vee` is a single point (`0` proj). So "the dual variety is a hypersurface"
already fails on `Det_n` — a second, independent reason the dual-variety family cannot supply a
closed condition containing `Det_n`, and one the record did not have before.

### 1.5 The already-excluded character-sum grading: the `z_rho` argument, re-derived

**The re-derivation (one paragraph, no pilot, as instructed).** Write

```
g(λ, μ, ν)  =  <χ^λ χ^μ, χ^ν>  =  (1/n!) · sum_{σ ∈ S_n} χ^λ(σ) χ^μ(σ) χ^ν(σ)
            =  sum_{ρ ⊢ n} χ^λ(ρ) χ^μ(ρ) χ^ν(ρ) / z_ρ,        z_ρ = n!/|C_ρ|.
```

The integrality of `g` is **not** a property of the summands — each is a rational number whose
denominator is `z_ρ`. It is a property of the **total**, and for one reason only: the total is an
inner product of characters, hence the multiplicity of `χ^ν` in `χ^λ χ^μ`, hence the dimension of
a `Hom`-space, hence a non-negative integer. Now let `st` be any statistic on conjugacy classes
and set `g_q := sum_ρ q^{st(ρ)} χ^λ(ρ) χ^μ(ρ) χ^ν(ρ) / z_ρ`. The coefficient of `q^j` is
`(1/n!) · sum_{σ : st(σ) = j} χ^λ(σ) χ^μ(σ) χ^ν(σ)`, a sum of the class function
`ψ := χ^λ χ^μ χ^ν` over a **union of classes that is a proper subset of `S_n`** unless `st` is
constant on the support of `ψ`. The operation "sum `ψ` over `S ⊆ S_n`, divide by `n!`" is an inner
product only for `S = S_n`; for a proper `S` it is not the multiplicity of anything, and no
mechanism clears the `z_ρ`. The denominators therefore survive in every piece. **That is the
whole argument, and it is correct.**

**What it does and does not prove — the overreach, recorded as instructed.** "No statistic on
conjugacy classes can work" is stronger than this argument proves, in two distinct ways.

1. **It is false as literally stated.** Take `st ≡ 0`: then `g_q = g · q^0`, with an integer
   coefficient. The claim must be quantified over statistics that are non-constant on the support
   of `ψ`.
2. **Even so quantified, the argument gives no impossibility proof.** It shows that *no mechanism
   forces* integrality; it does not show that *no* non-constant `st` produces it, whether by
   accident or by a structure invisible in this presentation. Establishing the universal claim
   needs an impossibility proof or an exhaustive characterisation, and neither is here.

**Provenance and label.** The four-statistics / 197-of-197 report comes from an exploratory
session of the user's that is **not on this record**: no pre-registration, no receipts, no
manifest. Under G9 and G9′ it is inadmissible as a premise of any PROVED or CERTIFIED claim, and
it is **not used** above — the paragraph is re-derived from scratch. The `z_ρ` argument is
**PROVED**; the universal claim is **ASSESSED** and is **not adopted**.

**One literature note.** The field does have `q`-analogues attached to the Kronecker problem, but
through a nonstandard quantum group and Hecke algebra (Mulmuley–Sohoni, GCT IV, arXiv
cs/0703110; UNREAD-SPECIALIST, title and abstract level), not through a statistic on conjugacy
classes. That is consistent with the paragraph above and is recorded as context, not as support.

### 1.6 Non-coverage, for the record

The brief asks why Lemmas 1.2–1.6, Fact 1.7, B20-02 Thm 6.4, Astra 8.1–8.3 and the onset cap do
not already cover each surviving sub-candidate. Neither survived, but the question has a real
answer here, and it is this slot's main structural finding.

- **A and B are the first two candidates on this record that genuinely escape Lemma 1.3 and
  Lemma 1.4.** Neither goes through `r x r` minors of a derivative matrix, and neither is an
  `SL_5`-covariant into a determinantal locus. Fact 1.7, B20-02 Thm 6.4 and the onset cap do not
  touch them either, and Lemma 1.2 does not apply to A at all, since `b_F` is not a polynomial in
  `F`.
- **B is killed by Lemma 1.1 itself** (rows B1, B3, B4) — the lemma the brief hoped
  characteristic-cycle multiplicities would sidestep. They do not: a characteristic cycle contains
  no number that is not a threshold on a semicontinuous integer statistic.
- **A is killed by something the record did not have**, namely Lemma D2 and Corollary D2′: a pure
  power `x^n` lies in every determinantal orbit closure, so every `GL`-invariant qualitative
  property of the determinant that fails at `x^n` is orbit-only. That is a **new exclusion**, of
  the same kind and scope as Lemmas 1.3 and 1.4, and it is what this slot adds to the record.

### 1.7 Price

No sub-candidate passed the gate, so **no construction is priced and no pilot is run**. Wrapped
launches **0 of 3**. The brief's rule applies: an empty slot beats a survey.

---

## 2–3. The pursuit

**None.** No numerical computation was run in this slot. No `b`-function of any quinary quartic
was computed, attempted or priced (explicitly out of scope). No characteristic cycle was computed.

---

## 4. Exact scope, and reopening conditions

**Established (PROVED, elementary, producer only).**

- **Lemma D1.** `b_{x_1^k} = prod_{i=1}^{k}(s + i/k)` in any number of variables. Derived from
  scratch in §1.2; uses no citation.
- **Lemma D2.** `x_1^4 ∈ D45` (in the image, not merely the closure) and `x_{11}^n ∈ Det_n` for
  every `n >= 2`.
- **Corollary D2′.** Every `GL_N`-invariant property that holds at `det_n` and fails at `x^n` is
  orbit-only and yields no closed condition containing `Det_n`.
- **Lemma D3.** `{lct <= c}` is vacuous once it contains `Det_n`; and `alphatilde(det_n) = 2`
  against `alphatilde(padding) <= 1`, so `{alphatilde <= c}` containing `Det_n` also contains
  padding. Conditional on Cayley's identity (PRIMARY, §1.1) and on the
  global-`b`-is-lcm-of-local sentence (PRIMARY, §1.1). **Not** conditional on any semicontinuity
  result.
- **§1.5.** The `z_ρ` argument, re-derived.

**Assessed, not proved.** Rows A4, B5 and B6: no recipe exists on record or here. These say that
no construction is available; they do not say the mechanism is impossible. The universal claim
"no statistic on conjugacy classes can give a `q`-analogue of the Kronecker coefficients" is
ASSESSED and **not adopted**; §1.5 states exactly how it overreaches its argument.

**Not established.** No equation of `D45` nonzero on padding. No `b`-function of any member of
`D45`, of `per_m`, or of any padded permanent. No theorem that no `D`-module construction exists.
No statement that the literature contains no such work — only that four searches did not find it.
No gap, no cell, no carrier, no degree bound. Nothing at `N = 16`.

**Reopening conditions.**

- **Sub-candidate A** reopens only if someone supplies **both**: (i) a construction of
  `I(closure(Z_int))`, or of the ideal of the closure of any `b`-function condition, as an
  explicit polynomial condition on the coefficients — which by §1.3 death 2 cannot be a
  minor/resultant recipe, so it must be something genuinely new; **and** (ii) a reason the value
  at `l·C*` (resp. at `x_0^{n−m} per_m`) is nonzero that does not reduce to knowing `b_{per_m}`.
- **Sub-candidate B** reopens only if someone exhibits a number in a characteristic cycle that is
  **not** a threshold on a semicontinuous integer statistic. B1–B4 assert there is none; that
  assertion is the thing to attack.
- The smallest concrete question either raises is the one B22-02 already named: determine
  `D45 ∩ P5` as a set. This slot adds one more, which nobody has asked: **does the `b`-function of
  a generic member of `D45` — that is, of `det_4 ∘ Λ` for generic `Λ : C^5 → Mat_4` — have any
  integral root beyond `−1`?** It is unpriced here and, on §1.1's evidence about determinantal
  `b`-functions, probably expensive. It is recorded because row A2 turns on it.

---

## 5. Labelled ledger (all rows producer only, G18)

| # | claim | status |
|---|---|---|
| M1 | Literature pass: four searches found no work applying `D`-module / Bernstein–Sato invariants to permanent-versus-determinant or to GCT orbit closures | MEASURED (search negative); **not** an absence proof |
| M2 | Ikenmeyer–Kandasamy quote on orbits versus orbit closures | PRIMARY (abstract fetched); corroborative only |
| M3 | Cayley: `b_{det_n}(s) = (s+1)(s+2)···(s+n)` in the `f^{s+1} → f^s` normalisation | PRIMARY (ar5iv, Caracciolo–Sokal–Sportiello Thm 2.1) **after the stated `s → s+1` shift** |
| M4 | Lemma D1: `b_{x_1^k} = prod_{i=1}^{k}(s + i/k)` | **PROVED** (self-contained, §1.2) |
| M5 | Lemma D2: `x_1^4 ∈ D45`; `x_{11}^n ∈ Det_n` | **PROVED** (self-contained) |
| M6 | Corollary D2′: `GL`-invariant properties failing at `x^n` are orbit-only | **PROVED** (from M4, M5) |
| M7 | Lemma D3(i): the `lct` condition is vacuous once it contains `Det_n` | **PROVED**, conditional on M3 |
| M8 | Lemma D3(ii): `alphatilde(det_n) = 2`, `alphatilde(padding) <= 1`, condition reversed | **PROVED**, conditional on M3 and on "global `b` = lcm of local `b`" (PRIMARY) |
| M9 | Rows A1, A2, A3, A5, A6, A7 of §1.3 | **PROVED-kill** |
| M10 | Row A4 | **ASSESSED-kill** (no recipe; not an impossibility) |
| M11 | Rows B1, B2, B3, B4 of §1.4 | **PROVED-kill**. B1 and B4 rest on record theorems (B22-02 L5(i) and rows 4–5; B23-06 L18); B3 rests on the index theorem (UNREAD-CLASSICAL) together with the two singular loci, and survives any reasonable form of it, since it needs only that deeper multiplicities are singularity-depth statistics |
| M12 | Rows B5, B6 | **ASSESSED-kill** (no recipe; B6 inherits B22-02 row 13 unchanged) |
| M13 | §1.5: the `z_ρ` argument | **PROVED** |
| M14 | §1.5: "no statistic on conjugacy classes can work" | **ASSESSED, not adopted**; false as literally stated (`st ≡ 0`), and unproved when quantified over non-constant `st` |
| M15 | A and B escape Lemmas 1.3 and 1.4; A dies on D2′, B dies on Lemma 1.1 | **PROVED** (escapes are the arguments of §1.3–§1.4; deaths are M9 and M11) |
| M16 | No equation produced; gate not passed; no cell nominated, no gap claimed | — |

**Literature at the point of use (G14, G14′).** PRIMARY and load-bearing: Cayley via
Caracciolo–Sokal–Sportiello (M3, M7, M8); "global `b` = lcm of local `b`" via Lin (M8). PRIMARY
and corroborative only: Ikenmeyer–Kandasamy (M2). UNREAD-SPECIALIST and **not** load-bearing:
Lőrincz–Raicu–Walther(–Weyman); Mulmuley–Sohoni GCT IV; the semicontinuity of `lct` and of
`alphatilde`. UNREAD-CLASSICAL: Kashiwara on rationality of the roots, Malgrange, Lichtin, and the
index theorem for characteristic cycles (used only in M11/B3, as qualified there). Lemmas D1 and
D2 need no citation at all.

---

## 6. Resources, receipts, manifest

**Numerical runs: none.** Wrapped launches **0 of 3**; wall `0 s` of `180 s`; no unwrapped
computation (G19). Before deciding not to run, I checked the batch's one-job rule at
2026-09-20T03:28Z: `..\B15-01\results\logs\b24_02_*.pid` **does not exist**, and
`..\B15-02\results\logs\b24_04_*.pid` **does not exist** — both directories were listed in full
and neither contains any `b24_*` receipt. No job was launched, so the rule was not exercised.

The session ran only reading, web search and fetch, hashing, and read-only git. Under G19 as
adopted (B21-10 R22), none of these is a numerical run.

| action | kind | receipt |
|---|---|---|
| `git rev-parse` / `status` / `show` / `log` / `cat-file` / `check-ignore` | read-only git | this section; the provenance block above |
| 6 web searches, 5 web fetches (2 PDFs returned unparsed streams and were discarded) | literature | §1.1 table |
| `sha256sum` of the five pinned inputs and of this report | hashing | `results/b24_05/MANIFEST.json` |

**Inputs read, hashed from the git object store (sha256):**

| input | pin | sha256 |
|---|---|---|
| `docs/b22_02_report.md` | `e22a41b1` | `b41e4265809a018750286d6eda416d62c4f4044b3fdb7cbac2cc51caf50593e4` |
| `docs/b23_02_report.md` | `68866e6d` | `664f3e52ee04b00cfe23d1019182804a4ce8825fb590715621efeaf6a478eff9` (matches B23-06's quoted value) |
| `docs/b23_03_report.md` | `3bcad666` | `0101f224327a61d1c14e480fbb0c6a4dca17c20b4e8191f44fe533b07b9e0a91` |
| `docs/b23_06_report.md` | `feed104e` | `a56d239467551cf9f197fb44094be8af41333a02570f94b71f99406308f4283a` |
| `docs/b23_10_review.md` | `239dd6e8` | `8bbc8d9eaee6962096af3f1ed6836e87ff1ffc250bea27789b82142fe014b5d9` |
| gate definitions, read in place | `6915ae6f` (G9, G10, G13, G14, G16, G18); `f7727cb7` (G19, G20′, G21–G23, G14′, G15′); `2efb7aaf` (G24, G25, G9′); `239dd6e8` (G27, G28) | read via `git show`; not re-hashed, since they are used only as definitions |

**Housekeeping (G10).** `.gitignore:51` is `results/logs/*.pid`, and the only negation present in
the file is `!results/logs/b15_*.pid`. So the **negation is missing for `b24_05_`**. It is moot
for this packet — no pilot was run and there is no `.pid` receipt to bind — and is reported here
only so that the next slot which does run one is not surprised. `docs/b24_05_report.md` and
`results/b24_05/MANIFEST.json` are not ignored: `git check-ignore` returns nothing for either.

**New files:** `docs/b24_05_report.md` and `results/b24_05/MANIFEST.json`. Nothing else in the
tree was touched. The worktree was clean at start and contains only these two new paths at end.
Git read-only; no commit.
