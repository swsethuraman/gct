# S1 and S2 together — what the two theory sessions changed

Integrator consolidation, 8 September 2026, written before the six Claude briefs
and superseding nothing in `docs/batch12_integrator_note1.md` or `note2.md`
except where it says so.

---

## 0. The shape of it

Both sessions failed at their headline and succeeded at something better, and
they failed and succeeded in **the same way**.

|  | headline goal | outcome | what replaced it |
|---|---|---|---|
| S1 | a deterministic 274-vector basis | not reached; unrestricted Plücker expansion retired | an exact birth quotient that turns source construction into one small rank problem per rung |
| S2 | the r = 5 completeness theorem | not reached; the coverage shortcut is *disproved* | two explicit chart eliminations that decide noncontainment with no support enumeration at all |

In both cases a *structural* goal was replaced by a *specified computation*.  And
in both cases the specified computation is one this environment can run —
I ran S1's, and Singular and msolve are installed here for S2's.

**So batch 12 is now an implementation batch, not a theory batch.**  That is the
single most consequential thing to carry into the briefs.

The counterpoint, and it must be said as plainly: **each session also removed a
claim the programme had been leaning on.**  S1 removed "a deterministic basis is
coming, and it will collapse the sampling cost."  S2 removed "`31 < 35` is a
theorem, so only completeness remains."  The programme stands on firmer ground
than it did this morning, and on narrower ground.

---

## 1. S1 — banked, added, withdrawn, measured

**Banked.**  The birth-quotient theorem: `ker(M_d → R/(u)) = uM_{d−1}`, so
`M_d/uM_{d−1} ≅ ρ_d(M_d)` and the quotient is the ladder birth space of dimension
`b_d`.  Proof checked line by line here.  With it, S1's local identities — signed
column normalization, pure-`u` removal, the proved unshared-column vanishing test
(`k < 5` at `n = 4`), and the short-column Plücker rule with its strictly
decreasing energy `E(T) = Σ (b−a)²` — all preserve the represented polynomial and
all terminate.  These are tools, and the briefs use them.

**Retired, and narrowly.**  Unrestricted Plücker expansion as the route to the
goal-cell basis.  Not for want of a larger term cap: for want of an
**independence theorem after the umbral contraction and identical-letter
symmetrization**.  Producing that theorem revives the route; raising the cap does
not.  s77's brief says so, so that retiring the route does not also retire the
adjacent question.

**Added here.**  For a prime ideal `I` with `u ∉ I` — true of `I(Det₄)` and
`I(ℓ·per₃)`, both orbit closures, with `u`'s value `det(A₁)` resp. `a₁·per(B₁)` —
`(I ∩ M_d) ∩ uM_{d−1} = u(I ∩ M_{d−1})`.  Hence `i_X(d) − i_X(d−1) ≤ b_d`, and

    rank T_det |_{uM₂₃} = 273 − i_det(23).

**So certifying determinant rank 273 at degree 23 settles it at degree 24 without
the final birth.**  This is a sufficient source, not a new mechanism, and
building the `δ = 23` source is still the work.

**Withdrawn.**  "The birth direction *is* the determinant ideal vector" — true of
the class, false of the representative; an ideal element differs from a
representative by a transported `uw`.  And the 23-fold coordinate compression is
a saving for coordinate implementations only, not a circuit speedup.

**Measured.**  The birth test, run here on real candidates
(`analysis/wk12_int_birth_probe.py`):

    saved delta=24 fillings: 108 with a pure-u letter, 5 without
    filling 57 nonzero mod u at BOTH primes, 24/24 points each
      -> M_24 = u M_23 (+) <F_57>, an explicit delta=24 birth representative
    20 pure-u controls: 0 nonzero, as the identity F_T = n! u F' requires

    fresh streams:  delta 23  b=1   1/1    33 draws   5.9 s
                    delta 22  b=3   3/3   142 draws  31.8 s
                    delta 21  b=5   5/5   131 draws  41.5 s
                    delta 20  b=9   9/9    41 draws  31.0 s
                    delta 17  b=31 17/31   39 draws  time-capped
                    delta 14  b=54 14/54   15 draws  time-capped, every filtered draw scored

Eighteen of the 274 directions, the four top rungs, in under two minutes.  **The
sampling tail was never a coupon-collector problem in the usual sense**: almost
every candidate lay in the transported source, and a pure-`u` letter *is*
transport.  The filter removes it syntactically and the quotient tests what is
left against `b_d`, not against `a_d`.

What that does **not** settle: assembly (the `(n!)^{D−d}u^{D−d}` normalization is
where a silent error would live), and both evaluation columns.  Discovery is no
longer the binding constraint; those two are.

---

## 2. S2 — banked, disproved, and the claim it took away

**Banked.**  On the ker/coker locus with irreducible restricted cubic
`det(B|_{s₅=0})`: reduced ranks are exactly 0 and 9, parameter kernel dimension
3; every order-two fixed-factor leading form is `s₅ ×` an honest `3×3` linear
determinant; affine image dimension ≤ 29, uniformly on that locus.  The bound
comes from a structural parametrization, not sampled Jacobian ranks — which is
precisely what the programme has been short of.

**Disproved.**  The unqualified 0/9 rank dichotomy.  A genuine five-dimensional
base pencil with reduced rank exactly 3, and an actual arc with

    det M(t) = t² s₅ s₄ (s₂ + s₅)(s₃ + s₅).

Intermediate ranks 1–8 cannot be discarded globally.  The nuance matters and I
adopt it: **that leading form is itself an exact determinant**, so the example
does not contradict the desired noncontainment or exhibit an image above the old
bounds.  It disproves a coverage shortcut, nothing more — and that is enough to
make it a mandatory control for the geometry session.

**The vertex correction.**  The exceptional fibre over the zero pencil already
contains `P(D₅)`, so bounding it as an independently understood deep-rank residue
restates the original problem.  Projectivizing the source removes the
circularity and keeps the projective limiting directions.

**What it took away.**  s72's interior value **31 was obtained by a probabilistic
protocol** — pointwise Jacobian ranks as lower bounds plus a Schwartz–Zippel
argument against a missed higher minor — not an exact identity over `Q`.  I have
been quoting `dim(D₅ ∩ W) = 31 < 35` as the batch's second-likeliest theorem.  It
is source-recorded evidence.  **The r = 5 session must now deliver an exact image
bound as well as coverage**, and the sufficient global bound is 34.

**What it supplied instead.**  Two explicit projective-source chart elimination
ideals that decide noncontainment, covering all schemes and all contact orders
with no support enumeration, complete rational inputs generated — and not run,
for want of a CAS on that host.

    Singular and msolve are both installed and working in the worker
    environment; sympy and python-flint are present.

I agree with the caution: 149 variables in lex is potentially enormous, and
generating equations is not evidence an elimination finishes.  The briefs treat
the two jobs as a **reference specification against which smaller reductions are
justified**, with a bounded pilot and the exact residual preserved on failure.

---

## 3. Three things that are now different from the finalized proposal

1. **s74 is not a sampler any more.**  It is a per-rung birth construction with a
   syntactic pre-filter, four rungs already banked, and a new first move —
   measure `i_det(23)`, because zero there finishes the determinant column at
   rank 273 with no `δ = 24` candidate at all.
2. **The r = 5 session is not a completeness proof.**  It is a bounded-pilot
   elimination with a mandatory rank-3 control, using the irreducible-cubic
   theorem as a lever and concentrating on the reducible and identically-zero
   restricted-cubic strata and higher contact.
3. **Nothing may promote a probabilistic bound.**  The interior 31, the recorded
   19 on `P ∩ C21`, and every other sampled image value stay labelled.  A slice
   dimension with a few reconstructed points is not a component certificate.

---

## 4. The board, final

Mission names, with the mapping to the finalized proposal's numbering on the
first page of every brief.

| | mission | what S1/S2 changed |
|---|---|---|
| **s74** | the LMR source by births, then the decision | rebuilt around the birth quotient; four rungs banked; `i_det(23)` first |
| **s75** | the `δ = 12` compact control | unchanged; `C₁₂ = 239` pre-registered, no prime below 97 |
| **s76** | scale the recursion to `δ = 24`, exact `C₂₄` | unchanged; S1 confirms `B₂₄` is a dimension and not a map |
| **s77** | deterministic basis: the bridge, then straightening | S1's identities are tools; the retired route is named so it is not re-run |
| **s78** | r = 5 by bounded elimination | completely respecified by S2 |
| **s79** | the two independent frontiers | unchanged; `a_∞ = 4` is five blocks |

**Priority**, expected value per unit effort:

    s74  >  s78  >  s75  >  s77  >  s76  >  s79

`s74` first because the constraint that made it expensive is gone and it carries
the decision.  `s78` second, and up from where I had it, because S2 turned it
from an open-ended proof into a specified computation on a host that has the
tools.

## 5. Ledger carried into the briefs

| | status |
|---|---|
| birth quotient `M_d/uM_{d−1} ≅ ρ_d(M_d)` | PROVED (S1), checked |
| `i_X(d) − i_X(d−1) ≤ b_d` for prime `I`, `u ∉ I`; `rank T_det|_{uM₂₃} = 273 − i_det(23)` | PROVED (here) |
| `M₂₄ = uM₂₃ ⊕ ⟨F₅₇⟩`, explicit representative | CERTIFIED, both primes |
| birth ranks complete at `δ = 20, 21, 22, 23` | MEASURED, single prime, seeds recorded |
| irreducible-cubic 0/9 theorem, order-two image ≤ 29 | PROVED (S2), replay reproduced |
| rank-3 counterexample and its arc | CERTIFIED (S2); disproves a coverage shortcut only |
| `E₀ = P(D₅)`, the vertex correction | PROVED (S2) |
| global 0/9 rank dichotomy | **DISPROVED** |
| unrestricted Plücker expansion as the basis route | RETIRED, for want of an independence theorem |
| `dim(D₅ ∩ W) = 31` as a deterministic bound | **NOT ESTABLISHED** — probabilistic protocol |
| a birth representative is an ideal element | **FALSE** |
| global exceptional-image bound below 35; `R₅ ⊄ D₅` | OPEN |
| `rank T_det = 273`, `rank T_pad = 274`, `D(24)` | OPEN |
