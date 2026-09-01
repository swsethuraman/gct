# Length 5 at n=4: the containment fails in every standard branch

Integrator, 2026-08-31.  Answer to session 27's successor item 2 ("ask whether
the containment survives at length 5 by another route — deciding it would close
or open the whole length-5 stratum at a stroke").

## 1. The question

Session 27's containment theorem closes length 4: every restriction of
`x_0.per_3` to a 4-plane is `ell.c` with `c` a 4-ary cubic, every 4-ary cubic
is `3x3`-determinantal, and `ell.c = det_4 diag(ell, M)`.  At length 5 the
block construction breaks (5-ary cubics are not all `3x3`-determinantal), but
`dim D_5^pad = 39 < 50 = dim D_5^{det_4}`, so containment remained possible by
some other representation.  If it held, `D <= 0` at every length-5 weight and
the 71 open cells at `delta = 6` close a priori — as the nine measured ones
(all `D = 0`) seemed to hint.

Since `per_3` is dense in the 5-ary cubics, `D_5^pad` is the full reducible
locus, so the question is exactly:

> is `s_1 . c` a `4x4` determinant of linear forms, for **generic** cubic `c`?

## 2. The method

`det(sum s_i A_i)` is divisible by `s_1` iff `det(sum_{i>=2} s_i A_i) = 0`
identically — iff `span(A_2..A_5)` is a 4-dimensional vector space of singular
`4x4` matrices.  Such spaces come in the standard compression branches.  For
each branch: parametrise, write `det M = s_1 . G`, and measure the dimension of
the reachable cubic family as the exact Jacobian rank of
`params -> coefficients of G` (35 = all 5-ary cubics means containment).

Internal checks, all passing: the branch determinant and **every** first-order
derivative along the branch are divisible by `s_1` (asserted, not assumed);
ranks taken mod `2^61 - 1` at three independent integer points, max reported.

## 3. The result

| branch (span A_2..A_5) | rank | of 35 |
|---|---|---|
| common kernel  `A(V_1) = 0`        | **29** | the `3x3`-determinantal cubics exactly |
| compression `A(V_2) <= W_1`        | **31** | |
| compression `A(V_3) <= W_2`        | **31** | |
| common cokernel `im A <= W_3`      | **29** | |

**Maximum 31 of 35.  No standard branch is dense.**  The common-kernel value
is its own consistency check: expanding along the killed column reduces `G` to
a `3x3` determinant of linear forms in 5 variables, and `dim D_5^{det_3} = 29`
— the measured rank, exactly.

## 4. What this means, stated with its one soft joint

Modulo the classification of 4-dimensional singular subspaces of `M_4(C)` —
i.e. provided every such space lies in a compression space —

> **`D_5^{per_3^pad}` is NOT contained in `D_5^{det_4}`.**  The generic
> reducible quartic `ell.c` in five variables is not a `4x4` determinant of
> linear forms; the shortfall is 4 dimensions in the best branch.

The soft joint is real and must be closed before this is a theorem: exceptional
(non-compression) maximal singular subspaces exist already for `3x3` (the skew
example), so completeness at `4x4` needs a citation (Atkinson; Eisenbud–Harris,
*Vector spaces of matrices of low rank*; de Seguins Pazzis) or a direct
argument.  One family is already ruled out here: a 4-dimensional singular space
inside the skew `4x4` matrices would be a 4-dimensional isotropic subspace of
the Pfaffian quadric, which has rank 6, so its isotropics have dimension at
most 3.

Two consequences if it stands:

1. **The nine `D = 0` cells at length 5 are unexplained.**  No containment
   forces them.  The pattern that closed length 4 survives at length 5 without
   the theorem that produced it — either a second, different theorem exists, or
   the 9 of 71 were unrepresentative.
2. **The 62 unmeasured cells at `delta = 6` are now the most informative
   computation in the programme** — genuinely open, with the foreclosure
   argument gone.

And one caution the other way: non-containment does **not** by itself produce
an obstruction.  It removes the argument that `D <= 0`; it does not give
`D > 0` anywhere.  The ideals `I(D_5^det)_delta` and `I(D_5^pad)_delta` can
differ as subspaces while having equal dimensions at every weight — in which
case every `D` is still 0 and the separation is invisible to multiplicities.
That distinction — *equal multiplicities with different ideals* — is exactly
what the nine measured cells would look like, and is worth testing directly:
at one length-5 weight, compute both `U_det` and `U_pad` (the ideal's
multiplicity-space slices, not just their dimensions) and check whether they
are the same subspace.  If they differ, the closures are provably different in
a way multiplicities cannot see — the sharpest possible statement of *why* the
multiplicity method is failing, from data already in hand.

## 5. Files

    analysis/l5contain.py    the branch parametrisations and Jacobian ranks
