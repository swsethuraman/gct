# B16-03: degree-23 Hessian equation, independent receiver

13 September 2026. gpt-6-astra, xhigh. Assigned existing worktree B15-03;
frozen HEAD `fde81352a5868a1d152a73716f47ecd4b285adbe` was confirmed by
read-only Git. All new artifacts have the owned B16-03 prefixes.

**Certified result.** The polynomial circuit below exports the nonzero global
determinant equation `P = c^23 S7`, in coefficient degree 23 and highest weight
`(61,15,2,2,2,2,2,2,2,2)`. On a newly generated invertible substitution of the
ten independent variables of `z*per3`, its exact integer value is

    -26743148924112014067635076791795712.

The input map has determinant **-248434** and leading quartic coefficient
**c=2**. All Hessian coefficients were freshly recomputed; no saved B15 raw
Hessian coefficient, generic evaluation, source vector, or minor was used as
arithmetic input. The receiver exports the full map, quartic, Hessian, complete
interpolation values, remainder, and symbolic pole-clearing recurrence.

**Finite-cell result, with explicit inherited premises.** Slot02's new census
reports `a23=189`. Combining that count, accepted padding coordinate upper
bound 158, and the accepted stable determinant ideal upper bound 11 with the
injection proved below gives `D23 <= -20`. This receiver does not independently
recount slot02's ambient multiplicity. The equation separates the two orbit
closures, but its cell cannot yield a positive multiplicity gap under those
premises. This conclusion uses the full ideal upper bound, rather than failure
of a sufficient inequality.

## 1. Conventions and executable export

Work over Q or a characteristic-zero extension. Use ten variables
`y=(t,x1,...,x9)` and ordinary, unnormalized monomial coefficients of a
homogeneous quartic G. Let `e=(1,0,...,0)` in the nine x variables and set

    g(t)=G(t,e)=c*t^4+a1*t^3+a2*t^2+a3*t+a4,
    H_G(t)=Hess_y G(t,e),
    D_G(t)=det H_G(t)=sum(k=0..20) D_k*t^k.

Each `D_k` is a degree-10 polynomial in the coefficients of G, since H has
linear coefficient entries and quadratic dependence on t. On c nonzero let
`q=g/c` and `R=D_G mod q^2`, the unique remainder of degree at most seven.
Division by g squared gives the same remainder, since c squared is a unit on
this chart. The export is

    P(G)=c^13 * [t^7] R.

The following circuit evaluates this expression without division and therefore
defines it on c=0 as well. Put `a0=c`, and define

    B1 = 2*a1,
    Bi = c^(i-2) * sum(a_u*a_v : 0<=u,v<=4, u+v=i),  2<=i<=8;
    T0=...=T6=0, T7=1;
    Tk = -sum(i=1..8, k-i>=7) Bi*T_(k-i),  8<=k<=20;
    P = sum(k=7..20) D_k*c^(20-k)*Tk.                       (1)

For example `B2=a1^2+2*c*a2`, `B3=2*c*(c*a3+a1*a2)`,
`T8=-2*a1`, and `T9=3*a1^2-2*c*a2`. All powers in (1) are nonnegative.
The exported symbolic lists contain all **194** nonzero monomials across
`T7,...,T20`, with 39 at T20. They are small binary-coefficient expressions;
the degree-23 polynomial in 715 quartic coefficients is never densely expanded.

**Proof of polynomiality and degree.** If `b_i=[t^(8-i)]q^2`, then
`B_i=c^i*b_i`. The top coefficient `r_k=[t^7](t^k mod q^2)` satisfies
`r_7=1`, `r_0=...=r_6=0`, and the same companion recurrence with b in place
of B. Induction gives `T_k=c^(k-7)*r_k` for k at least seven. Substituting
into (1) proves `P=c^13*[t^7]R`. Every B_i has coefficient degree i,
and every T_k has coefficient degree k-7. Thus every summand in (1) has
degree `10+(20-k)+(k-7)=23`. This is an identity in the universal coefficient
ring localized at c, followed by an explicit extension in the original
polynomial ring. No sampled cancellation is used.

The executable function `exported_value(g,D)` in `analysis/b16_03_equation.py`
implements (1). The function `equation(G)` takes the full sparse quartic,
differentiates it, computes the complete degree-at-most-20 Hessian determinant,
and returns both the circuit and independent rational long-division values.

## 2. Equality with the assigned depressed c^23 S7 recipe

Write the coefficient of t cubed in G as the entire linear form `a1(x)`.
Define the determinant-one shear

    F(t,x)=G(t-a1(x)/(4c),x)/c.

Then F is monic and depressed in t. Write `p(t)=F(t,e)`, and
`S7=[t^7](det Hess F(t,e) mod p(t)^2)` as in the inherited Hessian11 report.
With `h=a1(e)/(4c)`, Hessian congruence gives

    det Hess F(t,e)=c^(-10)*D_G(t-h),
    p(t)=q(t-h).

Translation commutes with remainders under the translated monic divisor;
the top coefficient of a remainder of degree at most seven is translation
invariant. Therefore `S7=c^(-10)*[t^7]R`, and (1) is exactly `c^23*S7`,
with no sign or factorial change. Full linear-form depression is necessary
for the Hessian congruence, and is checked in all nine x directions by the
receiver. No assumption of tracelessness of a general input is made.

## 3. Highest weight, proved for the universal polynomial

The positive coefficient-coordinate convention is
`C[Sym^4 V*]=Sym(Sym^4 V)`. Under the variable substitution
`(t,x1,x2,...,x9) -> (alpha*t,beta*x1,gamma2*x2,...,gamma9*x9)`,
Hessian congruence and the degree-20 homogeneity of its determinant give

    D_G'(t)=alpha^2*beta^22*product(gamma_j^2)*D_G(alpha*t/beta).

Also `c'=alpha^4*c` and `q'(t)=(beta/alpha)^4*q(alpha*t/beta)`.
Uniqueness of division shows the top remainder transforms by
`alpha^9*beta^15*product(gamma_j^2)`. Multiplication by c to the power 13
then gives weight `(61,15,2^8)`. Its sum is 92=4*23. The receiver separately
checks this weight for every exported T monomial.

For upper unipotent invariance, consider substitutions `y_i -> y_i+u*y_j`
with i<j, where y0=t and y1=x1. If i>=1, the substitution fixes every point
`(t,e)` and has determinant one; g and the Hessian determinant are unchanged.
If i=0, the substitution either fixes that line (j>=2) or translates t
(j=1). In both cases c is fixed, and the top degree-seven remainder
coefficient is unchanged. Hence P is invariant under all these root
subgroups. The torus weight is dominant, so the nonzero P is a highest-weight
vector. This is a universal covariance proof, independent of the numerical
simple-root tests.

Extend P to quartics in sixteen variables by first restricting to the first
ten variables. The additional upper-root substitutions leave those
coefficients unchanged; the weight extends by six zeros. Thus this is the
required sixteen-variable highest-weight equation.

## 4. Global determinant vanishing, including all boundary points

At a rank-three 4-by-4 matrix, reduce by invertible left/right changes to
`diag(0,I3)`. For a tangent matrix `[[a,r],[b,E]]`, the quadratic Taylor term
of determinant is `a*tr(E)-r*b`. Its Hessian pairs a with tr(E) and the three
r entries with the three b entries, so has rank eight. By congruence this
holds at every rank-three matrix. All 9-by-9 minors of the matrix-entry
Hessian vanish there; polynomial continuity on the singular-matrix variety
extends rank at most eight to every singular matrix.

For an arbitrary linear pencil `M(y)=sum y_i*A_i`, the coefficient quartic
is `G(y)=det M(y)`. Its ten-variable Hessian is a linear pullback of that
matrix-entry Hessian. At a root alpha of g, its rank is therefore at most
eight. A ten-by-ten polynomial matrix with rank at most eight at alpha has
determinant divisible by `(t-alpha)^2`: constant invertible row operations
make at least two rows zero at alpha, and every entry in those two rows is
divisible by t-alpha. Multilinearity of determinant proves the multiplicity.

On the nonempty dense open set of pencil coefficients where c is nonzero
and g has four distinct roots, these four squared factors show `g^2 | D_G`.
This open set is nonempty, for example with leading matrix I4 and the x1
matrix diagonal with distinct entries. Thus P vanishes there. Formula (1)
is polynomial in the entries of all A_i, so it vanishes on every pencil,
including c=0, repeated roots, and dependent directions. The same polynomial
then vanishes on the sixteen-variable determinant orbit closure. This is
the global ideal proof. The receiver's noncommuting-pencil zero controls
are implementation checks and play no role in this argument.

## 5. Fresh full-support padding witness and independent arithmetic

Use independent source variables `(z,X11,X12,X13,X21,X22,X23,X31,X32,X33)`.
The retained 10-by-10 integer matrix L sends `(t,x1,...,x9)` to those source
coordinates. It is displayed in `results/b16_03/certificate.json` at
`padding.map`. Its determinant -248434 proves full support: all ten source
linear forms are independent. The six permanent terms, multiplied by z,
give G; there is no identification of z with a matrix entry. The substitution
extends to GL16 by adjoining an identity block on the six unused variables.

For this witness,

    g(t)=2*t^4+22*t^3-28*t^2-10*t+14,
    [t^7](D_G mod g^2)=-3264544546400392342240609959936,
    P=2^13*[t^7](D_G mod g^2)
     =-26743148924112014067635076791795712.

After full depression,

    p(t)=t^4-(475/8)*t^2+(1907/8)*t-65715/256,
    S7=-3188031783594133146719345664,
    2^23*S7=P.

The fresh seed sequence 160303..160306 was fixed before arithmetic and
capped at four maps. The first three maps were invertible but had c=0 and
circuit value zero; all these outcomes are preserved and are not interpreted
as global padding identities. The fourth map provides the displayed nonzero.

Two exact routes were implemented independently of the B15 producer:

1. Expand the six products into ordinary quartic coefficients; differentiate
   them directly; recover D from its 21 values at t=0,...,20.
2. Differentiate the permanent in its nine matrix-entry variables, build
   `H_(zC)=[[0,grad(C)^T],[grad(C),z*H_C]]`, and compute determinant at
   t=-10,...,10 in the source variables. Multiply by det(L) squared and
   interpolate completely at these different nodes. Direct congruence of
   all 100 Hessian entries is also checked at three nodes.

These two routes recover the same entire degree-at-most-20 polynomial D,
not just one matching value. The source route also verifies the Euler
relation `H_C*X=2*grad(C)` and the polynomial identity
`2*det H_(zC)=-3*z^8*C*det H_C`. All numbers are rational or integer; no
prime reduction, CRT inference, or approximate arithmetic occurs.

Additional exact controls check all nine adjacent upper unipotent generators,
an opposite-direction shear that changes the value, a torus scaling,
coefficient scaling by 2 with exponent 23, full depression, and a D7 mutation
that is rejected. A complete 24-node interpolation in the leading coefficient
checks the division-free value at c=0. The proofs in Sections 1--4, rather
than these finite controls, establish polynomiality, highest weight, and
global vanishing.

Nonvanishing proves both ambient nonzeroness and a padded coordinate
multiplicity floor one in this finite cell. It does not identify either
complete ideal or coordinate multiplicity.

## 6. Finite comparison received from slot02

The external census `B15-02/results/b16_02/census.json` reports the exact
finite ambient multiplicity 189 in `(23,(61,15,2^8))`, obtained using its
finite hook criterion and exact character arithmetic. The count is an input
to this receiver; it is not recomputed here. Its raw SHA256 is recorded.
The integrator independently accepted the finite count and exclusion at
17:58:30 UTC, with complete rational-series and independent connected-rim-hook
replay. That acceptance, `Batch16/reviews/02/integrator_review.json`, is also
read and hashed. The degree-23 exclusion therefore uses accepted batch inputs.

Here is the needed ideal injection, to make the scope of the inherited
stable upper bound precise. Restrict a finite homogeneous highest-weight
polynomial to c=1 and zero t-cubic linear coefficient. First-row unipotent
invariance, full depression, and homogeneity recover it on c nonzero.
Thus this restriction is injective. Determinant pencils depress to
determinant pencils, so ideal membership is preserved. In the slice, multiply
by `s2^2`; this is a nonzero highest-weight polynomial of tail increment
`(4,0^8)`, so multiplication is injective in the ambient polynomial ring
and preserves the determinant ideal. It takes tail `(15,2^8)` into
`(19,2^8)`.

The accepted stable ambient 429 and determinant rank floor 418 therefore
give `i_det(23,(61,15,2^8)) <= 429-418 = 11`. This uses ideal multiplicities;
it never inserts stable coordinate rank 418 into the finite cell.

The accepted split-cubic source argument gives `m_pad23<=158`, so with
slot02's a23=189,

    i_pad23 >= 189-158 = 31,
    m_det23 >= 189-11 = 178,
    D23 = i_det23-i_pad23 <= 11-31 = -20.

With only the equation floor q=1, the sufficient positive threshold would
be r>=189; even with q=11 it would be r>=179, above the source ceiling158.
The rigorous exclusion is the displayed full ideal comparison. Source size
is used solely as an upper bound on padding image rank.

There is no remaining positive-gap witness in this cell under the received
premises. A next sufficient *positive* witness must move to a different,
nonexcluded finite cell and prove q+r>a there. Slot02's finite count/criterion
has already been independently accepted by the integrator; the equation and
padding nonzero do not depend on that count.

Since a homogeneous ideal generated in coefficient degree 24 has zero
degree-23 part, P is outside that specified degree-24-generated ideal.
No assertion of novelty relative to all LMR constructions, their saturation,
or the general Hessian mechanism is made; minimum lift degree is not proved.

## 7. Attribution, resources, and delivery

The equation recipe and corank-two divisibility come from the frozen
`Hessian11_1631/REPORT.md` and its source `verify_small.py` (earlier Astra
work). Relevant original Slot05 reports and the Astra reconstruction source
were read through the B15 intake. Their underlying B14 bracket conventions
retain Claude Opus 5 attribution. The present direct unnormalized circuit,
universal covariance proof, independent coefficient/source arithmetic,
fresh padding map, controls, and receiver were produced in B16-03.

The finite ambient count belongs to B16-02. Stable 429/418 and padding
ceiling158 are accepted B15 premises, with statuses from the frozen B16
board; older pending-review labels inside archived B15 reports are historical.
The receiver does not repeat the accepted B15-01 replay or claim a merged base.

All numerical work used the worktree `.venv/python.exe -B` and the inspected,
unchanged `analysis/b15_bound.py`, one process and one numerical thread,
60 seconds and 512 MiB enforced by Windows Job Object plus deadline timer.
The timer is a guard thread, not a numerical worker. Preflight limited
quartic support to 715 monomials, Hessians to 10 by 10, and interpolation to
21 nodes; estimated 20 seconds/100 MiB preceded the measured run.

Successful production took **0.7525832 s**, with **20,901,888 bytes** peak
Job Object memory and **33,775,616 bytes** peak working set. Fresh receiver
replay took **0.7493143 s**. Both exited 0. Final portable-package replay
including received finite-comparison arithmetic took **0.6874623 s**, with
**19,832,832 bytes** peak Job memory and exit0. The preflight took 0.0626997 s.
Two earlier subsecond controls exited 1 because the deterministic random
determinant leading matrix was singular and the fixture had asserted c
nonzero; the diagnostic confirmed c=0 and P=0. That boundary control was
retained, and an explicitly invertible leading matrix was used for the
chart control. There was no resource overrun or mathematical contradiction.
All failed and successful receipts are preserved.

No heavy lease was requested or held. The release receipt confirms every
recorded B16-03 numerical PID has exited; no process was duplicated after
resume. WMI process inspection was denied, so ordinary read-only Get-Process
was used successfully. No permission escalation, Git mutation, trust change,
subagent, other worktree, push, or publication was needed.

Replay from the assigned worktree, choosing a fresh owned receipt name:

```powershell
& .venv/python.exe -B analysis/b15_bound.py --slot 03 --name b16_03_receiver_fresh --seconds 60 --memory-mb 512 analysis/b16_03_receiver.py verify
```

The receiver rebuilds the arithmetic and compares every retained certificate
field. It does not import B15 mathematics implementations or read saved raw
Hessian coefficients as inputs. SHA256 input and delivery manifests, resource
receipts, and the portable receiver instructions accompany this proof.
