# Is the boundary deficit a separation obstruction?

Session 24, branch `s24-obstruction`, 2026-08-31.
Pre-registration: `results/PREREG_s24.md` (committed before any computation).
Session record and cross-checks: `docs/session_24.md`.

**Summary.** The decomposition
`mult_lam(B) - mult_lam(A) = [Peter-Weyl part] - [deficit part]` is proved as
Lemma 1 with its hypotheses.  The deficit part is *not* inert: Proposition 3
exhibits an explicit weight, verified four ways, where it alone produces a
multiplicity obstruction that the Peter-Weyl side cannot see.  But that witness
works by making the Peter-Weyl side degenerate — the two stabilisers are
*literally the same subgroup* — which is exactly the configuration
`per`/`det` is not in.  In the two worlds where this programme has closed-form
deficit data, an exhaustive census (World A: all 7 orbit closures, all 42
ordered pairs, all weights to `delta = 14`; World B: the Fermat hypersurface
against the generic Hesse member to `delta = 8`) finds **zero** deficit-driven
obstructions and **1345** weights where the classical side sees an obstruction
that the deficit destroys.  Proposition 4 explains why those two worlds could
not have answered the question either way.  Theorem 2 confines the deficit's
effect to a window whose width is the conductor — and the one determinant
conductor measured so far is 1.

---

## 1. The decomposition lemma

### Setup

Let `G` be a connected reductive group and `W` a finite-dimensional rational
`G`-module.  Assume the scalars `C^* ⊆ G` act on `W` by homothety, so that
`G`-stable closed subvarieties are cones and their coordinate rings are graded.
For `v ∈ W \ {0}` write `H = Stab_G(v)` (a closed, not necessarily reductive,
not necessarily finite subgroup), `O_v = G·v`, and `X = closure(O_v)` with its
reduced structure.  Let `lam` run over the dominant weights of the rational
irreducible representations `S_lam` of `G`.

Three standard facts, and nothing else, are used.

**(PW)** *Algebraic Peter–Weyl.*  `C[G] = ⊕_lam S_lam ⊗ S_lam^*` as a
`G × G`-module.  Taking invariants for right translation by `H`,
`C[G]^H = ⊕_lam S_lam ⊗ (S_lam^*)^H`.  Since `O_v ≅ G/H` as a variety and
`C[G/H] = C[G]^H`,

    mult_lam C[O_v] = dim (S_lam^*)^H =: m(lam).

*No reductivity of `H` is required.*  For non-reductive `H` the orbit `O_v` is
only quasi-affine; `C[O_v]` still means its ring of regular functions, and the
identification above is unaffected.  This matters here: the stabilisers of
`x^3 y`, `x^2 y^2`, `x^4` and of `det_n` are all positive-dimensional, and that
of `x^4` is not reductive.

**(RES)** *Restriction is injective.*  `O_v` is dense in the irreducible
reduced `X`, so `C[X] ↪ C[O_v]` is an injection of graded `G`-algebras.  Hence

    def(lam) := m(lam) - mult_lam C[X]  >=  0,

which is Definition 1 of the paper.

**(SUR)** *Containment surjects.*  If `Y ⊆ X` are `G`-stable closed cones then
`C[X] ↠ C[Y]`, so `mult_lam C[X] >= mult_lam C[Y]` for every `lam`.

### Lemma 1 (deficit decomposition)

*Let `v_A, v_B ∈ W \ {0}` with stabilisers `H_A, H_B` and orbit closures
`A, B ⊆ W`.  Write `m_A, m_B` for the Peter–Weyl counts of (PW) and
`def_A, def_B` for the deficits of (RES).  Then for every dominant weight
`lam`,*

    D(lam) :=  mult_lam C[B] - mult_lam C[A]
            =  [ m_B(lam) - m_A(lam) ]  -  [ def_B(lam) - def_A(lam) ]
            =: P(lam) - Def(lam) .

*All four quantities are finite integers.  `P` depends only on the pair of
subgroups `(H_A, H_B)` — no geometry.  `Def` depends only on the two boundaries.*

**Proof.**  Substitute `mult_lam C[X] = m_X(lam) - def_X(lam)`, valid for each
of `A` and `B` by (RES), into the left-hand side. ∎

The lemma is elementary; its content is the separation of variables.  `P` is
computable from branching/character data with no knowledge of the closures;
`Def` requires the closures and is what this programme computes.

### Definition 2

`lam` is a **multiplicity obstruction to `B ⊆ A`** if `D(lam) > 0`.  By (SUR)
this certifies `B ⊄ A`.  Call it **deficit-driven** if in addition
`P(lam) <= 0`: the classical side, on its own, sees nothing there.
Call it a **deficit-driven occurrence obstruction** if moreover
`mult_lam C[A] = 0`; that forces `def_A(lam) = m_A(lam)` exactly — *full
deficit*, the entire isotypic component living on the orbit and none of it
extending to the closure.

### Remark 3 (the theorem asked for in task 4 does not exist)

A statement of the form "the deficit difference is bounded by the Peter–Weyl
difference", i.e.

    def_A(lam) - def_B(lam)  <=  m_A(lam) - m_B(lam)   for all lam,          (*)

is, by Lemma 1, *literally equivalent* to "there is no multiplicity obstruction
to `B ⊆ A`".  It therefore holds automatically whenever `B ⊆ A`, and it cannot
be a theorem in general: proving (*) for all pairs would prove that
multiplicity obstructions never separate anything, which is false — Proposition
3 below exhibits a pair where they separate and where `P ≡ 0`, so that (*)
fails at a weight.  The honest form of the negative result is therefore not a
general bound but a *census* (Theorem 5) plus a *structural obstruction to the
mechanism* (Proposition 4) plus a *localisation* (Theorem 2).  This
reformulation is itself a deliverable: it says where to stop looking.

---

## 2. The conductor window

Suppose the boundary `X \ O_v` is cut set-theoretically by a semiinvariant
`Delta_X` of degree `e_X` and weight `det^{w_X}`, as in the paper's setup.
Since `Delta_X(v) ≠ 0` and `Delta_X(h·v) = det(h)^{w_X} Delta_X(v)` for
`h ∈ H_X`, the character `det^{w_X}` is trivial on `H_X`; hence

    m_X(lam + k w_X · 1) = m_X(lam)  for every k >= 0,                       (1)

because `S_{lam + k w 1} = S_lam ⊗ det^{kw}` and `det^{kw}|_{H_X} = 1`.
Multiplication by `Delta_X` embeds the `lam`-isotypic piece into the
`(lam + w_X·1)`-piece, so `mult` is nondecreasing along the ray and stabilises
at `m` (Ikenmeyer–Kandasamy Lem. 5.2; equivalently
`C[O_v] = C[X][1/Delta_X]`).  `c_X(lam)` is the least `k` with
`def_X(lam + k w_X 1) = 0`.

### Theorem 2 (conductor window)

*Let `A, B` be as in Lemma 1, both with boundary semiinvariants as above.  Put
`e = lcm(e_A, e_B)` and let `w` be the corresponding twist, so that
`lam_k = lam + k w · 1`, `delta_k = delta + k e` is a ray for both.  Then*

    D(lam_k) = P(lam)   for every  k >= max( c_A(lam), c_B(lam) ),

*a constant independent of `k`.  Consequently every deficit-driven obstruction
on this ray has index `k < max(c_A, c_B)`: the conductor is exactly the width
of the window in which the deficit part can act, and no deficit-driven
obstruction survives `Delta`-twisting.*

**Proof.**  For `k` at least both conductors, `def_A(lam_k) = def_B(lam_k) = 0`,
so `Def(lam_k) = 0` and `D(lam_k) = P(lam_k)`; and `P(lam_k) = P(lam)` by (1)
applied to each of `A` and `B`. ∎

Verified in World A along the `I`-ray of `{J = 0}` (`m` constant, `def`
falling monotonically to 0 and staying — table in `docs/session_24.md`).

**Why this bites.**  The programme's headline determinant result is
`c((2,2,2), 2) = 1`, ray-complete.  A conductor of 1 means a window of width
one: on that ray the deficit can act only at `k = 0`.  If conductors of
determinants are generally small — which is what the transport mechanism
predicts and what every measurement so far shows — then the deficit's entire
contribution to separation lives at the base of each ray, and the asymptotic
regime in which GCT usually works is pure Peter–Weyl.

---

## 3. The mechanism is not vacuous: an explicit deficit-driven obstruction

### Proposition 3

*Let `G = GL_2`, `W = Sym^8 C^2`, and `f_t = x^8 + t x^4 y^4 + y^8`.  For every
`t ≠ 0`,*

    Stab_G(f_t) = K = { diag(al, be) : al, be ∈ mu_8, al^4 = be^4 } ⋊ S_2,
    |K| = 64,

*the **same** subgroup, independent of `t`.  Take `A = closure(G·f_2)` — note
`f_2 = (x^4 + y^4)^2`, a perfect square — and `B = closure(G·f_1)`.  Then
`m_A = m_B` identically, so `P ≡ 0`, and at*

    lam = (26, 6),  delta = 4 :   m = 3,  mult_A = 2,  mult_B = 3,

*so `def_A = 1`, `def_B = 0`, `Def = -1`, `D = 1 > 0`.  This is a deficit-driven
obstruction; it certifies `closure(G·f_1) ⊄ closure(G·f_2)`.*

**Why the stabiliser is `t`-independent.**  A diagonal `diag(al,be)` fixes
`f_t` iff it fixes each of `x^8`, `x^4y^4`, `y^8` with the same scalar, i.e.
`al^8 = be^8 = (al be)^4 = 1`, which is `al, be ∈ mu_8` with `al^4 = be^4`;
`t` never enters.  The swap is a symmetry of every member.  For `t = 2` the
`PGL_2`-stabiliser is that of the harmonic 4-point set `{x^4 = -y^4}`,
of order 8; for generic `t` it is the same `D_4` (the 8 roots split into two
`mu_4`-orbits, and no Möbius map exchanges them: a scaling `z ↦ cz` with
`c^4 = om` sends the `om`-square to the `om^2`-square but the `om^2`-square to
the `1`-square, which is not in the set).  Both lift to order 64.

**Verification.**  `mult` computed as the rank of the substitution map
`Sym^delta(W^*) → C[a_1,a_2,b_1,b_2]` on each weight space, by four
independent routes agreeing exactly: fraction-free (Bareiss) elimination over
`Z`, elimination mod `2^31 - 1`, elimination mod `10^9 + 7`, and sympy's
rational `Matrix.rank`.  `m_K((26,6)) = 3` by two routes: eigenbasis count and
exact character averaging over all 64 elements in `Q(zeta_8)`.  The tool
reproduces all four World A closed forms independently (`Jz`, `tau`, `Q`, `D`,
`delta <= 5`).

### How special is it — the honest accounting

This is the section the brief asks for, and the answer is unfavourable.

1. **It relies on the two stabilisers being equal, not on their being
   different.**  `P ≡ 0` is *why* the obstruction is deficit-driven.  My
   pre-registered guess (H6) was that a witness would rely on *non-conjugate*
   stabilisers; that is refuted, and refuted in the direction that makes the
   witness weaker.  `H_{det_n}` has dimension `2n^2 - 1` and the stabiliser of
   the padded permanent is a different group of different dimension; they are
   not conjugate, `P ≢ 0`, and this mechanism is simply unavailable there.
2. **It does not rely on one closure being normal.**  Both `A` and `B` are
   deficient (both have `def = 1` at `lam = (8,0)`, `delta = 1`).  So this
   particular feature, which `per`/`det` also lacks a clean version of, is not
   what is doing the work.
3. **It does rely on codimension.**  Both closures have codimension 5 in `W`.
   Proposition 4 shows that in codimension 1 the mechanism cannot fire at all.
4. **It is not a GCT statement.**  It separates two members of a pencil of
   binary octics.  It shows only that the mechanism is not vacuous.  One
   example shows the mechanism exists; it does not show the deficit "gives new
   obstructions", and it is reported here as a proof of concept and nothing
   more.

---

## 4. Why the programme's two model worlds could not have answered this

### Proposition 4 (hypersurface blindness)

*Let `A = {F_A = 0}` and `B = {F_B = 0}` be orbit closures that are
hypersurfaces in `W`, with `deg F_A = deg F_B = e` and the same `GL`-weight
`det^w`.  Then `mult_lam C[A] = mult_lam C[B]` for every `lam`.  Hence there is
no multiplicity obstruction between them in either direction, and
`Def = P` identically.*

**Proof.**  `C[W]` is a domain, so `F_X` is a nonzerodivisor and
`0 → C[W]_{delta - e} ⊗ det^w → C[W]_delta → C[X]_delta → 0` is exact as
`GL`-modules.  The outer terms do not depend on `F_X`. ∎

### Corollary 4a

In `Sym^4 C^2` the orbit closures of the generic quartics form the pencil
`{ I^3 - c J^2 = 0 }`, `c ∈ C`, all of degree 6 and weight `det^12` — a
one-parameter family of *distinct varieties with identical multiplicity data*
(the discriminant hypersurface `c = 27` included).  In `Sym^3 C^3` the generic
Hesse members are the hypersurfaces `{ alpha S^3 + beta T^2 = 0 }`, all of
degree 12 and weight `det^12`, likewise.  Both verified computationally.

So in exactly those two worlds, the constant-stabiliser families — the
configuration that produced Proposition 3 — are hypersurface families, where
Proposition 4 forces `D ≡ 0`.  **The programme's two closed-form worlds are
structurally incapable of exhibiting a deficit-driven separation.**  The
`Sym^8` witness needed codimension 5 to exist at all.  This is the single most
important caveat on the census below: its negative result is partly a fact
about `Sym^4 C^2` and `Sym^3 C^3`, not only about the deficit.

---

## 5. The census

### Theorem 5 (World A, complete)

The nonzero `GL_2`-orbit closures in `W = Sym^4 C^2` are exactly seven
(the ambient `W` is not one: every nonzero binary quartic has a 4-dimensional
orbit):

| name | representative | dim | `C[X]` | `|H|` |
|---|---|---|---|---|
| `Gam` | `x^4` | 2 | cone over the rational normal quartic | ∞ (non-reductive) |
| `tau` | `x^3 y` | 3 | tangent developable | ∞ (1-dim torus) |
| `Q` | `x^2 y^2` | 3 | `{q^2}` | ∞ (1-dim) |
| `Iz` | equianharmonic | 4 | `{I = 0}`, deg 2 | 48 |
| `Jz` | `x^4 + y^4` | 4 | `{J = 0}`, deg 3 | 32 |
| `Ac` | generic `j` | 4 | `{I^3 - cJ^2 = 0}`, deg 6 | 16 |
| `D` | `x^2(x^2 - y^2)` | 4 | `{disc = 0}`, deg 6 | 8 |

*Over all 42 ordered pairs and all 224 weights with `delta <= 14` (9408 cells):*

- 2673 multiplicity obstructions, **every one of them Peter–Weyl** (`P > 0`);
- **0 deficit-driven obstructions**;
- 1183 cells where `P > 0` but `D <= 0` — the classical side sees an
  obstruction that does not exist, and the deficit is what destroys it;
- 0 obstructions violating a true containment (a hard consistency gate, which
  caught two errors during the session);
- the two invariants induce **the same preorder**: `mult_B > mult_A ⟹
  m_B > m_A` (0 failures in 2673 cells) *and* `m_B > m_A ⟹ mult_B >= mult_A`
  (0 failures in 3856 cells).

That last line is the mechanism.  In World A `mult` and `m` order the seven
closures identically at every weight, so `D` and `P` can never have opposite
signs.

### World B

`{S = 0}` (Fermat/Aronhold, deg 4) against the generic Hesse member
`{alpha S^3 + beta T^2 = 0}` (deg 12), `delta <= 8`: 19 multiplicity
obstructions, **0 deficit-driven**, 162 Peter–Weyl obstructions killed by the
deficit.

### The sign structure — why the negative is not an accident

Mean deficit per closure in World A over all weights `delta <= 14`:

    D   (|H| = 8) : 7.911      Ac  (|H| = 16) : 2.911
    Jz  (|H| = 32): 1.125      Iz  (|H| = 48) : 0.670
    tau : 0.062     Q : 0.004     Gam : 0.000

The deficit is inversely proportional to the size of the stabiliser — that is,
`def` tracks `m`, because `mult = m - def` is a property of the *embedded
variety* while `m` is a property of the *cover*.  `Def` and `P` are therefore
positively correlated by construction, and `D = P - Def` is a difference of
correlated quantities.  This, not luck, is why the deficit does not add power:
**it is largely a shadow of the Peter–Weyl count, not an independent signal.**

In the regime that matches `per`/`det` (`dim B < dim A`, the padded permanent
sitting inside a larger determinant closure) the sign *does* favour the
obstruction: `Def < 0` in 298 cells against `Def > 0` in 2.  But its magnitude
never sufficed.  Over the 1292 cells with `P <= 0` and `Def < 0` — the deficit
pushing exactly the right way — the maximum of `D` is **exactly 0**, attained
742 times, and never positive.  The deficit reaches the boundary and does not
cross it.

---

## 6. What it would take to carry the argument to `per` / `det`

Stated as a checklist, cheapest first.

1. **Both deficits, not one.**  The separating quantity is
   `Def = def_{per^pad} - def_{det}`.  This programme computes `def_{det}`.
   The permanent half has had no engineering at all: it needs its own boundary
   analysis, its own `Delta`, its own evaluation certificates.  Any `n = 4`
   determinant grind buys one term of a difference.
2. **Run the Peter–Weyl pre-screen first.**  A deficit-driven obstruction
   requires a weight with `m_{per^pad}(lam) <= m_{det}(lam)`.  Both are
   branching counts — `dim (S_lam^*)^H` — computable without any knowledge of
   either closure and cheap relative to a deficit.  If no such weight exists in
   the accessible range, the question is moot and no closure computation is
   needed.  **This screen has not been run and should be, before anything
   else.**
3. **The occurrence sub-case is already closed.**  A deficit-driven
   *occurrence* obstruction needs `def_{det}(lam) = m_{det}(lam)` (full
   deficit) together with `mult_{per^pad}(lam) > 0`; that is exactly an
   occurrence obstruction, and Bürgisser–Ikenmeyer–Panova rule those out for
   the padded permanent against the determinant.  So the deficit cannot help
   in the sub-case where it would be easiest to detect.
4. **Search inside the conductor window.**  By Theorem 2 the search space is
   `k < max(c_det, c_per)` on each ray.  The one determinant conductor measured
   is `c((2,2,2),2) = 1`, ray-complete: a window of width one.
5. **Then, and only then, the geometry.**  `n = 4` means `Sym^4 C^16`, of
   dimension `binom(19,4) = 3876` against 165 at `n = 3`, with the stabiliser
   jumping from dimension 17 to 31, and a boundary whose components are not
   classified.  None of that is worth starting before steps 2–4 return a
   live weight.

---

## 7. Recommendation

**Not a category error, but not worth the engineering cost of `n = 4` as a
separation programme.**  The decomposition is real and the mechanism is not
vacuous — Proposition 3 is an honest witness — but every structural feature we
can measure points the same way.  The deficit enters the obstruction with a
minus sign and, in 9408 World A cells plus the World B pair, it never once
created an obstruction while destroying 1345 that the classical side had
reported; the reason is that `def` tracks `m` (inversely with `|H|`), so the
deficit part and the Peter–Weyl part are positively correlated and their
difference is not a new signal; the one witness we could construct works only
by degenerating the Peter–Weyl side to zero via *equal* stabilisers, a
configuration `per`/`det` does not have; Theorem 2 confines whatever remains to
a window of width `max(c_A, c_B)`, and the only determinant conductor measured
is 1; and the occurrence sub-case is already closed by
Bürgisser–Ikenmeyer–Panova.  Against that, the honest counterweight is
Proposition 4: the two worlds with closed-form data are *hypersurface* worlds,
where a deficit-driven separation is structurally impossible, so the census is
weaker evidence than its size suggests, and the real case has the high
codimension the witness needed.  The proportionate response is therefore not
`n = 4` but the two cheap steps that would make the question live or dead:
run the `m_{per^pad}` vs `m_{det}` branching pre-screen, and compute the
*permanent's* deficit at `n = m = 3`, where the determinant's is already known.
Until one of those returns a weight with `m_{per} <= m_{det}` and
`def_{det} > def_{per}`, the deficit should be published as what it
demonstrably is — an exact measure of non-normality, with closed forms in two
worlds and a first determinant value — and not as a separation tool.
