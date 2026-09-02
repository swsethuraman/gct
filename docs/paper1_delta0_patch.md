# Patch for paper 1: the bracket `8 ≤ δ_0 ≤ 80` becomes `8 ≤ δ_0 ≤ 65`

Session 40 (2026-09-02).  For the integrator to place in
`paper/det3-conductor.tex` (not touched on this branch).  The mathematics is
`docs/onset_conjecture.md` (Theorem 1 at `n = 3`, Theorem 3); the exact
checks are `analysis/wk9_s40_jacobian.py` (`results/logs/s40_jacobian_n34.log`)
and `analysis/wk9_s40_frame.py` (`results/logs/s40_frame.log`).  Everything
below is in the paper's notation (`\cO`, `D_5`, `\mult`, `a(\lambda,\delta)`,
`\dfc`) and voice.  Labels for the record: the cap is **proved** modulo
Kleiman's transversality theorem (adopted, characteristic 0) and Dimca's
Theorem 3.1 (adopted); the six-nodes-in-general-position statement is
**proved** with one exact witness; the conjecture is **expectation**.

The bracket appears in exactly two places: the closing paragraph of the
subsection "Short weights: the length theorem" (after Remark `rem:crossover`)
and Question `q:delta0`.  The introduction mentions "degree 80" once
without the bracket; an optional one-line change is given in §4.

## 1. Insert before the closing paragraph of "Short weights: the length theorem" (after Remark `rem:crossover`)

```latex
\begin{proposition}[The Jacobian cap]\label{prop:jaccap}
For $F\in\Sym^{3}\bC^{5}$ let $M_4(F)$ be the $75\times70$ matrix of the
multiplication map $(\Sym^{2}\bC^{5})^{\oplus5}\to\Sym^{4}\bC^{5}$,
$(m_i)_i\mapsto\sum_i m_i\,\partial F/\partial s_i$, whose entries are linear
in the coefficients of $F$.  For smooth $F$ its rank is $65$; for $F\in D_5$
it is at most $64$.  Consequently the $65\times65$ minors of $M_4(F)$ are
nonzero polynomials of degree $65$ in the coefficients of $F$, they span a
$\GL_5$-stable subspace of $I(D_5)_{65}$, and $I(\cO)$ contains a
length-five component in degree $65$.
\end{proposition}

\begin{proof}
Write $J_F=(\partial_1F,\dots,\partial_5F)$.  For smooth $F$ the partials
form a regular sequence, so $\dim(\bC[s]/J_F)_4=[t^4](1+t)^5=5$ and the rank
is $70-5=65$; since the entries of $M_4(F)$ are linear in $F$, a
$65\times65$ minor is a polynomial of degree $65$, and at least one is
nonzero.  Now let $F=\det(\sum_is_iA_i)$ for a generic pencil, and let
$X\subset\mathbb{P}^{4}$ be the cubic threefold it defines.  By the proof of
Theorem \ref{thm:sharp}, $F$ is singular at every point where the pencil
meets the rank-one locus.  That these six points are the only singular
points of $X$, that there are exactly six of them, and that each is an
ordinary double point is the one step we take from the literature rather
than prove: Kleiman's transversality theorem \cite{Kleiman} (characteristic
zero), applied to the rank strata of $\mathbb{P}(M_3)$, gives that a generic
$\mathbb{P}^{4}$ misses the origin stratum, meets the rank-one stratum
transversally in $\deg(\mathbb{P}^{2}\times\mathbb{P}^{2})=6$ reduced points
(the rank-one locus is the Segre variety), and meets the smooth locus of the determinant hypersurface
transversally, so that $X$ is smooth elsewhere; and at a transverse
rank-one point a Schur-complement expansion $\det M=\det P\cdot\det(S-RP^{-1}Q)$
exhibits $F$ as a rank-four quadric in the four entries of the $2\times2$
block $S$ plus higher-order terms, i.e.\ a node.  Six points impose at most
five conditions on the five-dimensional space of linear forms, so the nodes
fail to impose independent conditions on forms of degree $2\cdot3-5=1$ by
at least one.  By Dimca's theorem on syzygies of Jacobian ideals
\cite[Thm.~3.1]{Dimca13}, for a hypersurface of degree $d$ in
$\mathbb{P}^{4}$ with isolated singularities the dimension of
$(\bC[s]/J_F)_{3d-5}$ exceeds its smooth value by exactly the failure of the
singular scheme to impose independent conditions on forms of degree $2d-5$;
at $d=3$ this reads $\dim(\bC[s]/J_F)_4\ge5+1$, i.e.\ $\operatorname{rank}
M_4(F)\le64$.  This holds on the dense subset of $D_5$ swept out by generic
pencils, hence on $D_5$.  The span of the $65\times65$ minors is the ideal
of maximal minors of a $\GL_5$-equivariant matrix of linear forms in $F$,
hence $\GL_5$-stable; Proposition \ref{prop:lengthred} carries the
corresponding highest-weight vectors, all of length five by Remark
\ref{rem:crossover}, into $I(\cO)_{65}$.
\end{proof}
```

Exact arithmetic supporting the proposition (for the data-availability
section, not for the text): at three fresh integer pencils the corank of
$M_4$ is $6$ at both primes, against $5$ for random cubics and for cubics
with five nodes at general points, and $6$ for cubics with six nodes at
general points (`results/logs/s40_jacobian_n34.log`); the whole Milnor row
of a determinantal cubic is $10,10,6,6,6,6$ in degrees $2,\dots,7$ against
the smooth $10,10,5,1,0,0$ (`results/logs/s40_jacobian_n3t.log`).

## 2. Replace the closing paragraph of the subsection

Current text begins "What the two theorems do not determine is the least
degree $\delta_0$ ..." and ends "... Question \ref{q:delta0} records what
remains open."  Replace it by:

```latex
What the two theorems do not determine is the least degree $\delta_0$ at
which a length-$5$ component actually appears in $I(\cO)$.  Direct
computation certifies $\mult=a$ at every weight of every length for
$\delta\le5$ --- each certificate a rank attaining $a$, with $\mult\le a$
the converse bound --- so $I(\cO)_\delta=0$ there: the orbit closure of
$\det_3$ has \emph{no equations at all} below degree $6$.  Beyond that, the
total-deficit identity
\[
  \sum_\lambda\dfc(\lambda,\delta)
  \;=\;\sum_\lambda\big(m(\lambda)-a(\lambda,\delta)\big)
  \;=\;1,\ 6,\ 31,\ 141,\ 618,\ 2488
  \qquad(\delta=2,\dots,7),
\]
in which the left side is measured by the streamed algorithm of Section
\ref{sec:method} and the right side is exact plethysm and branching
arithmetic, forces $\mult=a$ at every weight through $\delta=7$, since the
two sums agree while $\mult\le a$ holds term by term; direct certificates
independently cover all but $3$ ambient units at $\delta=6$ and all but $80$
at $\delta=7$.  Hence
\[
  6\;\le\;\delta_0\;\le\;65\ \ \text{unconditionally},
  \qquad
  8\;\le\;\delta_0\;\le\;65\ \ \text{given the measured totals},
\]
where $65$ is the Jacobian cap of Proposition \ref{prop:jaccap}: the
discriminant of Theorem \ref{thm:sharp} vanishes on $D_5$ because the
generic member is singular, the cap vanishes because it is singular at six
points that fail linear forms by one, and the second mechanism is the
cheaper of the two.  We conjecture that it is the cheapest of all, i.e.\
that $\delta_0=65$ (Question \ref{q:delta0}).  The first pieces of $I(\cO)$
pinned exactly appear at $\delta=10$: the three weights $(13,3,2^{7})$,
$(12,5,2^{6},1)$ and $(9,9,2^{6})$ have $a=1$ and $m=0$, so each isotypic
component lies in the ideal outright --- at lengths $8$ and $9$, by the
cheapest mechanism available, and carrying no deficit, since
$\dfc=m-\mult=0-0$ there.  Question \ref{q:delta0} records what remains
open.
```

(Only the display and the two sentences after it change; the rest of the
paragraph is the current text, kept so the replacement can be pasted
whole.)  If the integrator wants the degree-$8$ evidence in the paper, one
optional sentence may follow the display: "A direct sweep of the sixty
cheapest of the $107$ length-five weights of degree $8$ with ambient room
(the pipeline of Section \ref{sec:method} with the stabiliser reduction of
[paper 2]) again finds $\mult=a$ at every one; the balanced weights of
degree $8$ were not reached, so the lower end stays at $8$."

## 3. Replace Question `q:delta0`

```latex
\begin{question}[The first equation of length five]\label{q:delta0}
Theorem \ref{thm:length}, Proposition \ref{prop:jaccap} and the
computations of Section \ref{sec:det} bracket the least degree $\delta_0$
of a length-$5$ component of $I(\cO)$ between $6$ and $65$ (between $8$ and
$65$ given the measured totals).  The two ends have different characters:
the lower end is where measurement stopped; the upper end is one specific
mechanism --- the six nodes fail linear forms by one, and degree $4$ of the
Milnor algebra sees it --- whose cost, $65$, is the rank of the matrix that
detects it.  Every covariant we know how to write down that vanishes on
$D_5$ is of this kind (a minor of a matrix linear in $F$, costing its size:
the Jacobian matrices in degrees $5$ and $6$ cost $121$ and $205$, the
discriminant $80$), and we conjecture that there is no other kind below the
cap: $\delta_0=65$.  Two remarks bear on this.  First, $D_5$ is a classical
object seen from its nodes: the six nodes of a generic determinantal cubic
threefold are in linearly general position, and conversely the cubic
threefolds singular at six points in linearly general position form an
irreducible family of dimension $28$ whose closure is $D_5$ --- six such
points are a projective frame, unique up to $\PGL_5$; the cubics singular
at a fixed frame form a $\mathbb{P}^{4}$; $24+4=28=\dim\mathbb{P}(D_5)$; and the
frame condition on the nodes is open and holds at an explicit pencil.  So
$D_5$ is an irreducible component of the closure of the six-nodal locus,
the generic six-nodal cubic threefold with nodes in general position is
determinantal, and the hunt for $\delta_0$ is the hunt for the first
covariant vanishing on the cubics singular at a fixed frame.  Second,
$\delta_0$ cannot be found by counting.  $\bC[D_5]$ is the subalgebra of the
$\SL_3\times\SL_3$ semi-invariant ring of $(M_3)^{5}$ generated in bidegree
$(1,1)$, and the dimension of that ring in bidegree $(\delta,\delta)$ (more
precisely of its transpose-symmetric part), which bounds
$\dim\bC[D_5]_\delta$ from above, stays above
$\dim\Sym^{\delta}\Sym^{3}\bC^{5}$ until past degree $100$ --- so no
equation is forced by dimension comparison anywhere in the bracket, and
the route to $\delta_0$ must produce the equation itself.
\end{question}
```

The first sub-question of the current Question ("Is $D_5$ a component of
the closure of the six-nodal locus --- that is, is the generic six-nodal
cubic threefold determinantal?") is answered by the first remark and is
therefore removed; if the integrator prefers to keep it as a question, the
honest residual form is "Does the closure of the six-nodal locus have
components other than $D_5$, with nodes in special position?".

## 4. Optional: the introduction

Current: "... the ideal of $\cO$ contains the discriminant of quinary cubics
as a length-five highest weight vector in degree $80$ (Theorem
\ref{thm:sharp}), while below degree $6$ it contains nothing at all."

Optional replacement: "... the ideal of $\cO$ contains length-five
highest weight vectors in degree $65$ --- the maximal minors of the
Jacobian matrix of a six-nodal cubic threefold (Proposition
\ref{prop:jaccap}) --- and the discriminant of quinary cubics in degree $80$
(Theorem \ref{thm:sharp}), while below degree $6$ it contains nothing at
all."

The abstract's "this is sharp at five rows, witnessed by the discriminant
of quinary cubics" remains true and need not change.

## 5. Bibliography entries

```latex
\bibitem{Dimca13}
A.~Dimca,
\emph{Syzygies of Jacobian ideals and defects of linear systems},
Bull. Math. Soc. Sci. Math. Roumanie (N.S.) \textbf{56(104)} (2013), no.~2, 191--203;
arXiv:1210.1795.

\bibitem{Kleiman}
S.~L. Kleiman,
\emph{The transversality of a general translate},
Compositio Math. \textbf{28} (1974), 287--297.
```

(Dimca's Theorem 3.1 was re-read this session from arXiv:1210.1795 to the
statement quoted; the journal pagination should be checked against the
published version before submission.)

## 6. What is deliberately not in the patch

- The general-$n$ theorem (`cap(n) = 5n(n−1)²(7n−8)/12`) and the `n = 5`
  anomaly: paper 2 material.
- Any claim about the pad side or the obstruction question: the cap is a
  det-side, permanent-independent statement.
- The degree-$8$ sweep beyond the optional sentence of §2: its coverage is
  partial (60 of 107 cells), which is why the lower end of the bracket does
  not move.
