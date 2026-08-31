# Pre-registration — session 24: can the deficit separate?

Written **before** any computation of this session. Nothing below has been
checked; every number quoted from earlier sessions is cited, not re-derived.

Date: 2026-08-31. Branch `s24-obstruction`.

## 0. The question, made precise

For an orbit closure $\cO=\overline{G\cdot v}\subset W=\Sym^d\bC^N$ with
$H=\mathrm{Stab}_G(v)$, write $m(\lambda)=\dim(S_\lambda^*)^H$ and
$\mathrm{def}(\lambda)=m(\lambda)-\mult_\lambda\bC[\cO]_\delta$.  For two orbit
closures $A,B$ in the same $W$:

    mult_lam(B) - mult_lam(A) = [ m_B(lam) - m_A(lam) ]  -  [ def_B(lam) - def_A(lam) ]
                                  P(lam)  (Peter-Weyl)      Def(lam)  (deficit)

A **multiplicity obstruction to $B\subseteq A$** is a weight with
`mult(B) > mult(A)`, i.e. `D := P - Def > 0`.

**Definition (the object of this session).**  A **deficit-driven obstruction**
is a weight $\lambda$ with

    D(lam) > 0   AND   P(lam) <= 0,

i.e. an obstruction that the Peter-Weyl (orbit / stabiliser-count) side does
not see.  Equivalently `def_A - def_B > m_A - m_B >= 0`.

Sub-case worth naming separately: a **deficit-driven occurrence obstruction**
is one with `mult_A(lam)=0`; it requires `def_A(lam) = m_A(lam)` exactly
("full deficit": the whole isotypic component lives on the orbit and none of
it extends to the closure).

## 1. What will be computed

World A, $W=\Sym^4\bC^2$, $G=\GL_2$.  The complete list of nonzero
$\GL_2$-orbit closures is (dimension in brackets):

  Gam  = closure(x^4)                        [2]
  tau  = closure(x^3 y)   tangent developable [3]
  Q    = closure(x^2y^2) = {q^2}              [3]
  Jz   = closure(x^4+y^4) = {J=0}   deg 3     [4]   <- the paper's World A
  Iz   = closure(equianharmonic) = {I=0} deg 2[4]
  A_c  = closure(generic j) = {I^3-cJ^2=0} deg 6 [4]
  D    = closure(l1^2 l2 l3) = {disc=0} = A_27 deg 6 [4]

(The ambient $W$ itself is NOT an orbit closure: every nonzero binary quartic
has a 4-dimensional orbit.)

For each, `mult_lam` and `m(lam)` will be computed exactly, by two independent
routes, for all $\lambda$ with $\delta \le 12$; then all $7\times 6$ ordered
pairs will be searched for deficit-driven obstructions.

## 2. Pre-registered hypotheses and their falsifiers

**H1 (main, expected TRUE).**  In World A there is no deficit-driven
obstruction: for every ordered pair $(A,B)$ of the seven closures and every
$\lambda$ with $\delta\le 12$, `mult_B > mult_A` implies `m_B > m_A`.
*Falsifier:* one explicit $(A,B,\lambda)$ with `mult_B > mult_A` and
`m_B <= m_A`.  A single such triple refutes H1.

**H2 (expected TRUE).**  The deficit part is nevertheless not inert: there
exist pairs and weights where `Def != 0`, and where `Def` exactly cancels a
nonzero `P`.  Concretely I predict: for $A=D$ (discriminant hypersurface) and
$B=A_c$ ($c\ne 27$), `mult_A(lam) = mult_B(lam)` for **all** $\lambda$ (both
are degree-6 weight-$\det^{12}$ hypersurfaces, so their Hilbert series as
$\GL_2$-representations agree), while `m_D(lam) = dim S_lam` (since
$H_D=\mu_4\cdot\mathrm{Id}$) is strictly larger than `m_{A_c}(lam)` for
most $\lambda$; hence `Def = P != 0` and `D = 0`.
*Falsifier:* any $\lambda$ with `mult_D != mult_{A_c}`, or with
`m_D != dim S_lam`.

**H3 (expected TRUE, structural).**  *Conductor-window theorem.*  Along any
$\Delta$-ray common to $A$ and $B$, `D(lam_k) = P(lam)` for every
$k \ge \max(c_A(lam), c_B(lam))$; hence every ray carries at most
$\max(c_A,c_B)$ deficit-driven obstructions and none beyond the conductor.
*Falsifier:* a deficit-driven obstruction at ray index $k\ge\max(c_A,c_B)$;
or a failure of $m(\lambda+kw\mathbf 1)=m(\lambda)$ along the ray.

**H4 (expected TRUE).**  `def_Q = 0` identically ($Q\cong\bC^3/\pm$ is normal),
and `def_tau(lam) = [b=1]` (the single $S_{(4\delta-1,1)}$ non-normality gap
recorded in the paper's Remark after Thm 2.1).
*Falsifier:* any $\lambda$ where the computed deficit differs.

**H5 (expected TRUE).**  `m_{Jz}(a,b) = N(a,b)` and
`def_{Jz}(a,b) = max(0, floor((a-3b)/8))` as in Theorem 2.1, reproduced here
by two routes independent of the paper (character averaging over
$H=\mu_4^2\rtimes S_2$; and $\mult$ from the hypersurface quotient
$\bC[W]/(J)$).  *Falsifier:* any disagreement at $\delta\le 12$.
This is a calibration check on my pipeline, not a new result.

**H6 (conditional prediction, about specialness).**  *If* H1 is falsified,
I predict the witnessing pair will have $H_A$ and $H_B$ non-conjugate in $G$
and of different dimension, and $B$ normal while $A$ is not — features the
$\per_m^{\mathrm{pad}}$ / $\det_n$ pair does **not** have (there both closures
are non-normal for $n>2$ and both stabilisers are positive-dimensional).
Such an example would therefore be reported as a negative result dressed as a
positive one.
*Falsifier:* a witnessing pair with conjugate stabilisers, or with both
closures non-normal.

**H7 (World B, weaker confidence).**  The same search in $\Sym^3\bC^3$
(Fermat/Aronhold quartic hypersurface $\{S=0\}$ against other orbit closures)
returns no deficit-driven obstruction either.  Confidence lower because the
World B rings are harder and the search will be less complete.
*Falsifier:* one explicit triple, as in H1.

## 3. What I expect the recommendation to be

Negative-leaning.  My prior before computing: the identity
`D = P - Def` is an accounting identity, not a source of new power, because
`Def` is bounded by `m_A` and is supported on the conductor window; the cost
of computing `def` at $n=4$ is enormous and the payoff is a correction term
that vanishes along every ray.  I expect to recommend against engineering
$n=4$ *for this purpose*, while noting that the deficit remains interesting as
a measure of non-normality.  If the computation surprises me I will say so.

## 4. Discipline

Exact arithmetic only (Python integers / Fraction). Every reported
multiplicity computed twice by independent routes. No claim enters
`docs/obstruction_power.md` without its cross-check recorded in
`docs/session_24.md`.
