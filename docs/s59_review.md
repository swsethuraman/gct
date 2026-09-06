# Integrator review — session 59, the higher-order Rees exceptional image at `r = 5`

**Accepted.**  The anchors are reproduced here independently; the new
measurement is not, and §3 says exactly what that leaves open.  The session's
own verdict is correctly scoped and I would not soften it, but one qualifier in
the headline needs to travel with it everywhere the result is quoted (§2).

## 1. Reproduced independently

My own parametrisation, my own dual-number Jacobian, my own random points,
sharing no code with the session (`/root/work/s61v/s59v.py`; `p = 2147483647`):

| object | measured here | session |
|---|---|---|
| `dim D_5` (Jacobian rank at a generic determinantal point) | **50** | 50 |
| exact reducible locus, common-kernel space | **29** | 29 |
| exact reducible locus, common-cokernel space | **29** | 29 |
| exact reducible locus, `(2,1)` compression space | **31** | 31 |
| exact reducible locus, `(3,2)` compression space | **31** | 31 |

Method for the second block: `A_1, …, A_4 = P B_k Q` with `B_k` in the standard
compression space (10-dimensional for `c21` and `c32`, 12 for the kernel and
cokernel types) and `P, Q` free `4×4`, `A_5` free; the map to the 70 coefficients
of `det(Σ_{i=1}^5 s_i A_i)`; Jacobian rank at a random point.  **`31` is the
maximum over the four types**, exactly as s32 Theorem 5 and the session both
report, and it is the load-bearing lower bound `dim(D_5 ∩ W) ≥ 31`.

The reformulation is confirmed as well: for every one of the four families the
quartic has exactly 35 nonzero coefficients and **no `s_5`-free monomial**, so
the image lies in `W = ker π` by construction, not by accident.  `dim W = 35`
is `dim Sym^3 C^5 = C(7,3)`, and `dim D_4^{det_4} = 34` makes the generic fibre
`50 − 34 = 16` against the jump to `≥ 31` — the arithmetic of §1 of the report
holds.

**Not reproduced here:** the session's own new measurement, the contact-order
invariance `29, 29, 28, 28, 24` at `q = 1, 2, 3, 4`.  Rebuilding the arc/jet
construction would be a reimplementation rather than a check, and the risk of a
spurious disagreement from a differently-set-up V-point is high.  What I can say
is that the machinery producing it is calibrated against the two anchors I did
reproduce, that the session halts on anchor failure and the anchors did not
fail, and that every value it reports is *below* the 31 I confirmed — so no
reported number is in tension with anything independently established.

## 2. The qualifier that must travel with the headline

"Contact order does not climb" is true as measured and false as stated without
its scope.  The correct form is:

> **at a generic `M_0`, through `q = 4`**, the reducible exceptional image is
> invariant of contact order.

The reason to insist is in the session's own §0 and it is sharper than a
generic caveat: **the known 31-dimensional exact locus is itself a component
that sits over special `M_0`**, so generic-`M_0` sampling demonstrably misses
geometry we already know is there.  A method that cannot see the component we
have is not evidence about components we do not.  This does not weaken what was
measured — the specific mechanism s54 hypothesised is eliminated — but it means
extending `q = 5, 6, 10` at generic points has close to zero value, and the
session says so.

## 3. The blocker is gone

The report closes: *a proof of the negative needs an upper bound on
`dim(D_5 ∩ W)` — the full special-fibre algebra `F(J_C)` (a Gröbner/elimination
object) or a length-5 equation of `I(D_5)` at degree `> 9`.  Neither is
reachable in this container (no CAS…)*.

**A CAS is reachable.**  `Singular 4.3.2` and `msolve 0.6.5` install from the
distribution repositories in about a minute, and `Macaulay2 1.22` is packaged
too; `docs/s61_review.md` §7 records this and every number in that review was
computed with them.  The programme's `python-flint`-only rule was a description
of what was available, not a policy, and it should be relaxed to: *exact linear
algebra stays in `python-flint`; Gröbner, saturation, primary decomposition and
elimination may use Singular or Macaulay2, with the generated script and every
random draw committed* — which is the discipline s61 already followed.

So the deliverable this pilot specified is now briefable.  The next session on
this track should be a **special-fibre computation over the special `M_0` loci**,
with `dim F(J_C)` or an upper bound on `dim(D_5 ∩ W)` as its deliverable, and
`det_3`'s known Hüttenhain–Lairez boundary as its calibration — *not* another
generic jet sweep.  That is also where the four-dimensional gap will be closed
or not.

## 4. On the ledger

The order-3 solvability probe is a pre-registered miss recorded as one: the guess
was that `tr(adj M_0 M_2) = −e_2(M_0; M_1)` would generically fail to be
solvable and halt the order-by-order route, and it is solvable at codimension 0.
That miss is *why* the invariance is visible through `q = 4` at all, which makes
it the productive kind.  Marked correctly.

## 5. Hygiene and verdict

Pre-registration `5ae85ae` precedes the higher-order measurement; the machinery
commit `ea8183e` and the anchor commit `0d3d627` precede it too and are
correctly labelled as reproducing known numbers rather than measuring the open
question.  No single-writer file touched, no blob over the limit, no session
link in any of the six commits, `Co-Authored-By` on each.  The exact-31
certificate passes `tools/verify`.

Accepted and merged.  The direction of the evidence is unchanged — `R_5 ⊄ D_5`
— and the session's refusal to call it proved is right.
