# B24-10 — pre-formed verdicts, v3

**Reviewer model:** Opus 5 (1M context), model id `claude-opus-5[1m]`.
**Slot:** B24-10, worktree `C:\Users\swami\Projects\gct-gpt\work\batch15_workers\B15-10`, branch
`b15-10-portable-witness`.
**HEAD at first write:** `239dd6e84417ab04914a8d84cca02ddf754bf1fb`, tree
`3008235a92bf10a108ae673564d879a5716b4a1d`.
**`git status --porcelain` at first write:** `?? results/b24_10/`,
`?? results/logs/b15_10_runtime_native_20260913.pid`,
`?? results/logs/b15_10_runtime_native_20260913_resources.json`.

**Rule of this file.** Every section below is written **before** the corresponding deliverable, its
proof, or its defence is opened, and before `preverdicts_formed_before_reading_v2.md` is opened.
Each section is appended when it is formed and is **never edited afterwards**. Corrections,
agreements and disagreements with what the packets actually say belong in `docs/b24_10_review.md`,
not here. Where a pre-verdict is later overturned by the bytes, the overturning is recorded there
and this file keeps the wrong reading visible.

Order of writing (append log, UTC):
- §1 appended 2026-09-20T16:44Z — before opening `v2` or `docs/b24_04_report.md`.

---

## §1 — Priority 1: B24-04's tail theorem (pre-formed, statement only)

**Method label:** PRE-FORMED, from the statement as printed in the B24-10 brief. No packet file, no
`v2`, no `GAPS.md`, no ledger consulted. I have not read `docs/b24_04_report.md`.

### §1.0 The statement as given

> if the tail `t` is less than the degree `d`, every weight vector factors as
> `c_{n e_1}^{d-t} * g` with `deg g = t`; since `I(D_r^{det_n})` is prime and `P_r` irreducible,
> the separating property passes through; therefore every separating cell has tail >= `D*`.

### §1.1 The reading I am ruling on

I do not have the packet's definitions, so I record the reading under which I rule, and I will say
in the review whether the packet's definitions match it.

- `d` is the degree of a weight vector; `t` its **tail**; `c_{n e_1}` a distinguished coordinate of
  extremal weight `n e_1` in the coordinate ring being used.
- **tail** is the part of the degree not carried by `c_{n e_1}`, so that `d - t` is the exponent of
  `c_{n e_1}`. I flag immediately that if `tail` is *defined* as `d - (exponent of c_{n e_1})`, then
  the factorization clause is a definitional unwinding and carries no content; if `tail` is defined
  independently (by a partition shape, a weight, or a pattern index), the factorization clause is a
  **lemma requiring proof** and is the load-bearing step. I cannot tell which from the statement.
- **separating** = vanishes identically on one of the two loci and not on the other; the cell is
  separating if it contains such a vector.
- `D*` is the **onset**: the least degree at which a separating vector exists.

### §1.2 Step-by-step pre-verdict

**Step A — the factorization.** `c_{n e_1}^{d-t} * g` with `deg g = t`.

A weight vector is in general a **sum** of monomials of a common weight, not a monomial. For the sum
to factor, every monomial in its support must be divisible by `c_{n e_1}^{d-t}`. That is not
automatic from "each monomial individually has `c`-exponent at least `d-t`" unless the weight
genuinely forces the exponent, which in turn needs `c_{n e_1}` to be the **unique** coordinate of
its weight and the weight arithmetic to admit no other decomposition in degree `d`. **This is a real
lemma and it is where I expect a gap if there is one.** I pre-register the exact question: *does the
proof establish the exponent bound monomial-by-monomial and then observe it is uniform over the
support, or does it argue only about a single monomial and silently extend to the span?*

**Step B — the descent.** From `f = c^{d-t} * g` separating, conclude `g` separating.

Two directions, and they are **not symmetric**:

- *Vanishing side.* `f in I` with `I` prime gives `c in I` or `g in I`. To land on `g in I` one needs
  `c_{n e_1} notin I(D_r^{det_n})` — i.e. the extremal coordinate does **not** vanish identically on
  the locus. The statement as printed does **not** say this. Primality is invoked; the side
  condition that makes primality useful is not. **This is a named omission in the statement.** It is
  almost certainly true and almost certainly checkable in one line (the extremal coordinate is
  generically nonzero on an orbit closure containing a point where it is nonzero), but a proof that
  invokes primality without stating the non-membership is incomplete as printed.
- *Non-vanishing side.* `f notin J` gives `g notin J` **for free**, because an ideal absorbs
  multiplication: `g in J` would force `f = c^{d-t} g in J`. **No primality and no irreducibility of
  `P_r` are needed here.** So the appeal to "`P_r` irreducible" is either (i) how the packet
  establishes that the *other* ideal is prime, (ii) redundant, or (iii) doing something I cannot see
  from the statement. I pre-register that **one of the two hypotheses invoked in the statement is
  doing no work in the direction it appears to be invoked for**, and that the statement is therefore
  over-hypothesised or under-explained.

**Step C — the conclusion.** `g` separating of degree `t` implies `t >= D*`.

This is immediate **iff** `D*` is the onset minimised over the *whole* class that `g` belongs to. It
**fails** if `D*` is weight-specific or cell-specific: `g` has a different weight from `f` (it has
lost `d-t` copies of weight `n e_1`), so a weight-indexed onset `D*(lambda)` would give
`t >= D*(weight of g)`, which is not `t >= D*(weight of f)` unless the onset is uniform. **This is
the second named risk.** I pre-register the question: *is `D*` a single number, minimised over all
weights, or is it indexed?*

Note also that no induction is required — one descent suffices — so I do **not** expect a
well-foundedness problem, and I will not count the absence of an induction as a gap.

### §1.3 Pre-formed ruling

**CONDITIONAL**, on exactly three conditions, in decreasing order of how much I expect them to bite:

1. **(C1)** The factorization of Step A is proved for weight vectors (spans), not merely for
   monomials — or `tail` is defined so that it is a tautology, in which case the content moves
   entirely into whether the cell-to-tail assignment is well defined.
2. **(C2)** `c_{n e_1} notin I(D_r^{det_n})` is established, not assumed. Without it the primality
   appeal in Step B is inert.
3. **(C3)** `D*` is a degree-onset minimised over the whole class, not a weight-indexed quantity.

If all three are met by the committed bytes, my ruling converts to **PROVED**; if (C2) or (C3) is
merely missing from the write-up but true and one line away, **PROVED-with-correction**; if (C1)
fails on the span, or (C3) is genuinely indexed, **REJECTED as stated**.

I expect, from the shape of the argument alone, to land on **PROVED-with-correction**: the argument
is the right argument, and the statement as printed omits a side condition that the proof probably
supplies.

### §1.4 What would change my mind, pre-registered

- Finding that the proof treats a *general element of a cell* rather than a *weight vector*, without
  saying the cell is spanned by weight vectors — that would be a genuine gap.
- Finding that "tail" is defined via the 70-pattern basis of B22-01 rather than intrinsically. Then
  the theorem's scope is only as canonical as that basis, which priority 1's third question already
  puts in doubt, and my ruling would go to CONDITIONAL-on-a-bespoke-basis and stay there.

---

## §2 — Priority 1, the two things that are not the theorem (pre-formed)

Appended 2026-09-20T16:47Z. Still before opening `v2` or `docs/b24_04_report.md`.
**Method label:** PRE-FORMED. The arithmetic in §2.2 is my own, done by hand from the two numbers
printed in the brief, with no packet open.

### §2.1 The sizing law `N_S ~ 0.060 * t^4`

**Pre-formed ruling: MEASURED at best, and I expect to rule it a FIT, not a law.**

A pure-number coefficient given to two significant figures (`0.060`) in front of an integer power
(`t^4`) is the signature of a regression on a finite sample, not of a derivation. Three things decide
the label, and I pre-register them:

1. **Is the exponent 4 derived or fitted?** If some counting argument forces a quartic and only the
   constant is measured, the object is a derivation with a measured constant, and `t^4` may be
   extended outside the sample range. If the exponent is itself the output of a log-log slope, then
   *nothing* about the law survives outside the fitted range, including the exponent.
2. **What is the fitted range of `t`?** Not printed in the brief. Without it the law is unusable as
   a predictor and I cannot rule on the extrapolation at all except to reject it.
3. **Is `0.060` a rounded `3/50`, a rounded `1/16.67`, or a raw regression coefficient?** Two
   significant figures on a leading constant caps the accuracy of any evaluation at ~2 s.f.,
   which matters for §2.2.

I expect to rule the sizing **MEASURED (fit), valid only on its fitted range**, and to require the
range be printed wherever the law is.

### §2.2 The figure `~ 4 x 10^10` at tail 900 — arithmetic done before reading

The brief asks whether the figure is independent of the sizing law or is that law evaluated at
`t = 900`. **I can settle this from the two printed numbers, by hand, before opening the packet:**

    900^2 = 810,000
    900^4 = 810,000^2 = 656,100,000,000 = 6.561 x 10^11
    0.060 * 6.561 x 10^11 = 3.9366 x 10^10  ~  4 x 10^10

**The match is exact to every digit printed.** `0.060 * t^4` at `t = 900` *is* `3.94 x 10^10`, which
is what `~ 4 x 10^10` rounds to.

**Pre-formed ruling: the figure is NOT independent of the sizing law. It is the sizing law evaluated
at `t = 900`, and nothing more.** I would need the packet to show a second, disjoint route to
`4 x 10^10` to overturn this, and I pre-register that if the packet presents the figure as though it
were corroboration of the law, or the law as though it were corroboration of the figure, that is a
**circularity** to be named. I will look specifically for that.

Consequences I pre-form now:

- **The `EXTRAPOLATION` label is NOT sufficient on its own.** `EXTRAPOLATION` says the value is off
  the sample; it does not say *how far* off. `t = 900` against an unprinted fitted range is an
  unbounded claim. The label is sufficient **only** when the fitted range of `t` is printed beside
  the figure every time the figure is used. If the fitted range is, say, `t <= 40`, then `t = 900`
  is a >20x extrapolation of a quartic, and the honest statement of the result is not a number at
  all but "larger than anything we sampled, by a quartic fit whose exponent we did not derive".
- **On use as a price: pre-formed NO, with one exception.** A price is a number a decision is made
  against. `3.9 x 10^10` carries two significant figures inherited from `0.060` and an unknown
  systematic from a >20x extrapolation; its true uncertainty is orders of magnitude, not percent.
  The record may use it **only** as an order-of-magnitude floor phrased as such ("at least ~10^10,
  by quartic extrapolation from `t <= [range]`"), never as `4 x 10^10`, and never as a figure to
  compare against another price to two digits.
- **On superseding `10^150`.** Superseding a figure of `10^150` by one of `4 x 10^10` is a change of
  140 orders of magnitude, and the superseding figure is the weaker-provenance of the two if
  `10^150` came from a derivation and `4 x 10^10` comes from a fit. I pre-register: **the
  supersession is only legitimate if `10^150` is shown to be wrong, not merely to be larger.** A fit
  does not supersede a bound. I will check which `10^150` was. If `10^150` was itself an unfounded
  guess, both should be withdrawn rather than one replacing the other.
- **Carry-forward item 6** should therefore be amended to carry the fitted range and the
  order-of-magnitude phrasing, not the two-digit figure. That is my pre-formed recommendation to the
  integrator.

### §2.3 B24-04 Q3 — the 70-pattern basis is a seeded greedy selection

**Pre-formed ruling: if the finding is as described, it stands, and the consequence is the harsher
half.**

A seeded greedy selection is basis-like in exactly one respect (it spans / is independent) and
canonical in none. Two distinct defects follow and I pre-register both, because they are often
conflated:

1. **Seed-dependence.** A different seed gives a different 70 patterns. Any statement whose content
   is "these 70" rather than "some 70" is then an artefact of the seed, and is not reproducible
   except by republishing the seed. The seed must be in the manifest.
2. **Greedy-dependence.** Greedy selection does not in general find a canonical or even an extremal
   object; the count 70 is an upper bound on nothing and a lower bound on nothing unless a separate
   argument pins the number.

**On "which makes the Missing Theorem bespoke":** I pre-form that this is correct and is the right
word. A theorem stated over a non-canonical basis is a theorem about that basis. It can still be
true and useful; what it cannot be is basis-free. My pre-formed ruling is that the Missing Theorem
must carry the seed and the selection procedure in its statement, or be restated in a basis-free
way, and that until one of those happens its scope label is **CONDITIONAL on the seeded basis**, not
OPEN and not PROVED.

I note the interaction with §1.4: **if the tail theorem's `tail` is defined through this same
70-pattern basis, the tail theorem inherits the bespokeness**, and my §1 ruling would have to move.
I pre-register that as the single most consequential thing I will check in the B24-04 bytes.

---

## §3 — Priority 2: Corollary D2' and its two lemmas (pre-formed)

Appended 2026-09-20T16:51Z. Before opening `docs/b24_05_report.md` or `results/b24_05/`.
**Method label:** PRE-FORMED, from the statements in the brief plus standard `D`-module facts I hold
independently. I have not read the packet.

### §3.1 Lemma D1 — `b_{x_1^k}(s) = prod_{i=1..k} (s + i/k)`

**Pre-formed ruling: PROVED, and classical — this is not B24-05's result.** The Bernstein-Sato
polynomial of a pure power in one variable is textbook. I check it at the ends from my own
knowledge: `k = 1` gives `s + 1`, which is the b-function of a coordinate; `k = 2` gives
`(s + 1/2)(s + 1)`, which is the b-function of `x^2`. Both are right. Adding dummy variables does
not change a b-function, so reading `x_1^k` inside `C[x_1..x_{n^2}]` is harmless.

**On the Cayley convention, pre-registered.** The roots printed are `-i/k`, all in `[-1, -1/k]`, and
`b(-1) = 0` at `i = k`. That is the **standard** convention `b(s) f^s = P(s) f^{s+1}`, under which
`(s+1)` always divides `b_f`. A sign-flipped or shifted convention would print roots `+i/k`, or
would print `(s)` rather than `(s+1)` as a factor. **The formula as printed is self-certifying on
this point**: `(s + k/k) = (s + 1)` appears in the product, which is the marker of the standard
convention. So the convention used in D1 is the standard one, and I pre-form that the integrator's
recorded Cayley-convention error does **not** infect D1 as stated. What I must still check in the
bytes is whether the *application* of D1 keeps the same convention, since a convention error
typically appears at the join, not in the quoted formula.

**Pre-registered caution:** if the packet claims D1 as its own contribution rather than as a cited
classical fact, that is an attribution defect, not a mathematical one, but it is one I will name.

### §3.2 Lemma D2 — `x_1^4 in D45` in the image, and `x_{11}^n in End(C^{n^2}) . det_n` in `Det_n`

**Pre-formed ruling on the second clause: PROVED, and trivially so.** Take the linear map
`A : C^{n^2} -> C^{n^2}` sending the matrix variable to `x_{11} . I_n`, the scalar matrix. It is
linear in the entries. Then `det_n(A(X)) = det(x_{11} I_n) = x_{11}^n`. So `x_{11}^n` is in the
`End`-orbit of `det_n`. And `End(C^{n^2}) . det_n` is inside `Det_n` because `End` is the Zariski
closure of `GL`, so the `End`-orbit lies in the closure of the `GL`-orbit. Both halves are one line.
`n >= 2` is not needed for the construction; presumably it is there to make `Det_n` interesting.

**Pre-formed ruling on the first clause (`x_1^4 in D45`, "in the image"): CONDITIONAL, pending the
meaning of "in the image".** The qualifier is doing work and I cannot evaluate it blind. It reads
like a hedge distinguishing membership in a variety from membership in the image of a specific
parametrising map, which are different statements when the map is not proper. I pre-register: *is
`D45` here a closed set, or the image of a morphism? If the latter, is the image closed?* If the
first clause is only about a constructible image, then any downstream use of it as a **closed**
condition is invalid, and that would be the defect in this lineage.

### §3.3 Corollary D2' itself

> every `GL_N`-invariant property that holds at `det_n` and fails at a pure power `x^n` is a
> property of the orbit, not the orbit closure, and yields no closed condition containing `Det_n`.

**Pre-formed ruling: PROVED, and it follows from D2 alone.**

The proof I reconstruct without the packet: let `P` be `GL_N`-invariant, `P(det_n)` true,
`P(x^n)` false. By D2, `x^n` lies in `Det_n`. If the locus of `P` were closed and contained
`det_n`, then being `GL_N`-invariant it contains the orbit `GL_N . det_n`, hence its closure
`Det_n`, hence `x^n` — contradicting that `P` fails at `x^n`. So the locus of `P` is not a closed
invariant condition containing `Det_n`.

**Two pre-formed observations, both of which I expect to matter more than the ruling:**

1. **D1 is not a premise of D2'.** The corollary needs one fact only: that some pure power lies in
   `Det_n`. D1 is a premise of the *application* — it is what exhibits a particular `D`-module
   invariant as failing at `x^n`. The brief's "its premises are Lemma D1 and Lemma D2" therefore
   **over-attributes**. This is worth saying because a corollary that appears to need a b-function
   computation looks deeper and narrower than it is; stated correctly it needs no `D`-module theory
   at all. I pre-register that I expect to rule D2' **cheaper than advertised in its dependencies
   and narrower than advertised in its scope** — see below.
2. **The hypothesis "fails at a pure power" must be closure-honest.** The argument needs the locus
   closed. If `P` is a constructible or open condition the conclusion does not follow in the stated
   form, though the weaker "the locus does not contain `Det_n`" still does, unconditionally. I
   expect the packet to need the closed case only, but the statement should say `closed`.

### §3.4 The proposed placement beside Lemma 1.3 and Lemma 1.4

**Pre-formed ruling: NARROWER. The placement is not justified as "of the same kind and scope".**

My reason, formed without seeing 1.3 or 1.4: D2' is a **single-witness** exclusion. Its entire force
comes from one point, `x^n`, that happens to lie in `Det_n`. It excludes exactly those properties
that fail at that one point and is silent on every property that happens to hold there. That is a
**sieve with one hole**, and it is cheap to apply precisely because it is narrow. A general exclusion
of the same kind and scope as a structural lemma would have to quantify over the boundary of
`Det_n` minus the orbit, or over a family of witnesses, not over one.

This does not diminish it — a one-line test that kills candidate obstructions is worth having, and
the record already shows it killing two sub-candidates in B24-05. It means the honest framing is
**"exclusion test", not "general exclusion"**, and the honest placement is as a remark or a
proposition with its witness named in the statement, adjacent to but not among the structural
lemmas. I pre-register that I will overturn this only if 1.3 and 1.4 turn out themselves to be
witness-based, in which case the placement is consistent and I will say so.

---

## §4 — Priority 3: the C45 chain (pre-formed)

Appended 2026-09-20T16:54Z. Before opening `docs/b24_02_report.md` or `docs/b24_02b_report.md`.
**Method label:** PRE-FORMED.

### §4.1 (a) ceiling vs floor

The claim: `i_det = nullity_Q`, while `nullity_p >= nullity_Q`, so measurement gives a **ceiling**
and the floor can come only from LMR.

**Pre-formed ruling: PROVED, elementary.** For an integer matrix, reduction mod `p` can only drop
rank: `rank_{F_p} <= rank_Q`, since a `Q`-independent set may become dependent mod `p` but never the
reverse. Hence `nullity_p >= nullity_Q = i_det`. A measured `nullity_p` is therefore an **upper
bound** on `i_det` — a ceiling — and no amount of modular measurement at any number of primes can
produce a lower bound, because every prime independently over-reports. The only escape would be a
certificate of the opposite direction — an explicit set of `Q`-independent rows, or a nonzero minor
lifted to `Z` — which is a floor obtained by exhibition, not by nullity measurement.

This is the right way round and I expect the packet to have it right. I pre-register the one way it
could be wrong: **if `i_det` is defined as the nullity of a matrix whose entries themselves depend
on `p`**, the inequality need not hold. I will check that the matrix is an integer matrix
independent of `p`.

### §4.2 (b) the `(*)` qualification at the boundary

**Pre-formed ruling: I separate two issues that the brief's phrasing merges, and I expect the
second, not the first, to be load-bearing.**

- *The boundary issue.* Using a premise at the exact boundary of its stated range is **sound if and
  only if the range is stated closed at that end.** `l(lambda) = 7` against a reduction stated for
  `l(lambda) <= 7` is legitimate and unremarkable; against one stated for `l(lambda) < 7`, or for
  "`l(lambda)` small", or proved by an argument that needs slack, it is not. This is a
  bytes-checkable question with a yes/no answer, and I pre-register that it is **not** where the
  risk is: a closed range is a closed range.
- *The transport issue, which is the real one.* LMR's numbers are at `N = 9`; the record's `D_7` is
  at `N = 7`. A statement established at `N = 9` does not transfer to `N = 7` merely because `N` is
  smaller — smaller `N` is the more degenerate regime, and inequalities of this kind typically fail
  first at small `N`. The bridge is "the programme's own reduction". **So the premise actually used
  at its boundary is the programme's reduction, and the thing being transported across it is
  someone else's theorem from a different `N`.** Two approximations compose here, and the brief's
  `(*)` names only one of them.

**Pre-formed ruling: CONDITIONAL, and I expect to keep it conditional.** The chain is sound only if
(i) the reduction's range is closed at `l(lambda) = 7`, (ii) the reduction is proved, not adopted,
at that value, and (iii) the reduction's conclusion is exactly the hypothesis LMR's theorem needs,
with no residual gap in `N`. If any one of these is adopted rather than proved, the C45 floor is
**ADOPTED, not PROVED**, and must be labelled so wherever it is used. A result whose floor rests on
a premise at its boundary should not be described as closed unless the qualification travels with it
in the same sentence.

### §4.3 (c) the recommendation against taking `i_det = 1` from LMR

**Pre-formed ruling: the recommendation is CORRECT and I expect to endorse it.**

The asymmetry is the whole point, and it is a matter of evidential hygiene rather than taste: one
half is proved in the printed source and the other is asserted there. Adopting an asserted half
because it travels in the same paper as a proved half is exactly the error this review series exists
to catch, and it is the error that would be hardest to detect later, because by then the two halves
would carry the same citation. A packet that declines to take the free half, and says why, is
behaving correctly. **I pre-register that I will endorse the refusal, and that if the record has
already used `i_det = 1` anywhere, that use must be relabelled, not grandfathered.**

### §4.4 (d) the pre-registration hash and the three negative controls

Nothing to pre-form mathematically. Two mechanical checks, and I record in advance what each would
mean:

- **Hash before `import flint`.** The point of pre-registration is that the prediction cannot have
  been informed by the result. If the hash is written after the library that computes the result is
  imported, the guarantee is weakened but not destroyed; if it is written after the computation, it
  is worthless. I will read the byte order in the committed output, not a description of it.
- **`D(7), D(8), D(9) = -17, -11, -2`.** These are negative controls: all three negative, and
  **strictly increasing toward zero**, which is a pattern worth noting rather than three independent
  nulls. I pre-register that if the three values are monotone by construction, or are three values
  of one smooth function of `N`, they are **one** control and not three, and the packet should not
  count them as three.
