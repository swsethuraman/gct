# B15-02 proof fragment

## Claim and scope

**EXACT.** For n=4, degree 7, ambient variable dimension 16, each partition
listed in results/b15_02/proposed_exclusions.json has m_det=1 and D<=0.
These are precisely the nine original a=1 cells retained in the launch panel.
No claim extends this finite list to other partitions or degrees.

Work over Q or C. The form space is Sym^4(V*), and the polynomial coefficient
ring in degree 7 is Sym^7(Sym^4 V). Let D_det be the closure of the GL(V)
orbit of det4. Let P be the closure of the orbit of z*per3, where z is
independent of all nine permanent entries, embedded in sixteen variables.
Write a for ambient multiplicity, i_X for ideal multiplicity and m_X=a-i_X
for coordinate multiplicity. The numerical gap is D=m_P-m_det.

## Exact source and point argument

For each cell, cell_NN_polynomial.json records the whole integer polynomial
as indexed quartic coefficient monomials, an explicit exponent alphabet,
and an integer determinant pencil. Each monomial has coefficient degree 7
and weight lambda. The coordinate c_alpha means the ordinary coefficient
of s^alpha in a quartic, with raising action

E_(i,i+1)c_alpha=(alpha_i+1)c_(alpha+e_i-e_(i+1)).

The standalone verifier expands the alphabet indices, checks every monomial
weight, and applies this derivation by the product rule over Z to the entire
polynomial. All six simple raising derivatives vanish identically. The source
is thus a highest-weight vector in seven variables. Viewed in sixteen
variables, its other simple raising derivatives vanish because each source
exponent in variables 8 through 16 is zero. No source orientation, factorial
rescaling, or u multiplication changes this construction.

The seven matrices in the recorded pencil are linearly independent. The
verifier extends them with nine standard matrix units to a sixteen-element
integer basis of the 4x4 matrix space. The determinant of this row-major
frame is 50100, so substitution by that frame is invertible over Q. It gives
a point of the determinant orbit. Restricting to the first seven variables
preserves every coefficient used by the source polynomial. Direct polynomial
expansion and integer evaluation give the nonzero values recorded in the
standalone files. These are fresh geometric evaluations from actual integer
matrices, not elimination on stored value matrices.

Therefore the source has nonzero image in the determinant coordinate ring,
and m_det>=1. Exact rational power-sum plethysm with integer symmetric-group
characters gives a=1 in all nine cells. Consequently m_det=1, i_det=0 and
m_P<=a=1. Hence D=m_P-1<=0. The tighter recorded pullback upper bounds h_pad
are unnecessary to this final implication. Padded multiplicities were not
measured, and D remains in {-1,0} for each cell.

## Modular search and lifting audit

The search used p=65521 and the S45 signed orbit carrier. Its character on
an equal-part block b is sign(g)^b. The original signed Burnside sizes were
freshly recomputed before allocating carriers. E is the integral raising
matrix on that carrier. The S71 triangular cover and locally implemented
NumPy/SciPy residual computation provide rank_Fp(E)>=n_chi-1, and a verified
nonzero kernel vector provides the opposite inequality. All vectors were
checked on every row. A projected residual was accepted only when its full
lift satisfied E*K=0; projection randomness does not enter soundness.

Since the characteristic-zero highest-weight dimension is also one, an
invertible modular maximal minor provides the usual Z_(p) kernel base change.
The normalized modular source therefore has a rational lift. This argument
is additionally checked by construction: solve the one- or two-column
residual over Q, clear denominators, divide by the coefficient gcd, and
check the resulting integer vector on every row. Its reduction is proportional
to the original modular source by the recorded normalization coordinate.
The standalone integer polynomial proof above makes a modular lifting premise
unnecessary for the final nonvanishing claim.

## Evidence, verifier and dependencies

Evidence status: EXACT, worker checked. Integrator acceptance remains separate.
Verifier: analysis/b15_02_replay.py, using tools/verify/hwv.py and
tools/verify/points.py with tools/verify/forms.py. It loads the standalone
integer polynomial and explicit points, so no source reconstruction, numerical
search or Schur backend is needed for receiver replay. The recorded mutation
of one literal coefficient makes a simple raising derivative nonzero.

Fresh checks: integer HWV identities, exact determinant evaluations, complete
orbit-frame rank and determinant, exact ambient multiplicities, signed
Burnside sizes, modular kernel/source consistency and scoped screening.
The original h_pad values and theorem ledger are inherited inputs, explicitly
identified in the report. They are not needed to prove these nine exclusions.
General dependencies are highest-weight theory in characteristic zero and the
coordinate-ring quotient bound m_X<=a. Existing implementation attribution is
preserved: S30 plethysm/coefficient conventions, S45 builder, S71 cover method,
S79 point/evaluation driver and the repository's separately written verifier.
No live Claude phase was used; gpt-6-astra performed every new phase.
