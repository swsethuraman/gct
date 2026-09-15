# Expanded Cayley boundary repair: the linear relaxation survives

The expanded system is **consistent over the rationals**. Its 83 by 345
coefficient matrix has exact rank 81, and adjoining the right-hand side leaves
rank 81. The affine solution space therefore has dimension 264. An explicit
rational solution with A=0 and diagonal T of rank 28 satisfies every coefficient
of all four identities. The complete matrix, solution, and executable verifier
are retained beside this report.

This does not give a repair using the six available unused variables. That
requires total block rank at most six. The displayed solution has rank 28, and
the existence or impossibility of rank at most six remains unresolved. No
low-rank search was performed. The rank 28 is the rank of this particular
solution, not a lower bound on all solutions.

In fact, the explicit solution below works for any polynomial of degree one in
each of the three row groups. Consequently the unrestricted expanded linear
test cannot, by itself, distinguish the permanent from other such polynomials.

## Derivation and exact system

Let Y=(y_ij) be a 3 by 3 matrix, g=per_3(Y), and P=z*g. Consider the restricted
simple-pole boundary data

    f_t = P + t * sum_l w_l*k_l(Y) + higher terms,
    Q_t = partial_z*A(partial_Y)
          + t^(-1) * sum_l partial_(w_l)*H_l(partial_Y) + higher terms.

For the displayed terms, direct expansion of Q_t(f_t^s), followed by extraction
of t^0 and setting all w_l=0, gives

    s*z^(s-1) * [ A(partial)g^s
                 + sum_l H_l(partial)(k_l*g^(s-1)) ].

The normalized quartic Cayley polynomial is fixed:
b_4(s)=s(s+1)(s+2)(s+3). Dividing its boundary equality by s*z^(s-1), for the
positive integers s=1,2,3,4, gives the four reduced equations

    A(partial)g^s + sum_(alpha,beta) T_(alpha,beta)
       * partial^alpha(y^beta*g^(s-1))
       = (s+1)(s+2)(s+3)*g^(s-1).

A is supported on the six permutation monomials. Alpha and beta range over
all 165 cubic monomials, with equal row-degree and column-degree vectors.
The weight-space dimensions are 1 in 51 blocks, 2 in 36 blocks, 3 in 12 blocks,
and 6 in one block. Thus there are 100 blocks and 339 ordered pairs, yielding
6+339=345 unknowns. Alpha=beta is always allowed.

Every resulting monomial has row and column degrees (s-1,s-1,s-1). For s=1,2,3,4
the row counts are respectively 1,6,21,55, totaling 83. The code constructs the
sparse derivatives and checks that no output support lies outside these rows.
It independently checks each entry by the direct coefficient formula

    [y^e] partial^alpha(y^beta*g^(s-1))
      = product_i (e_i+alpha_i)!/e_i! * [y^(e+alpha-beta)]g^(s-1),

with the analogous formula for the A columns. All 28,718 entries of the
augmented integer matrix are checked. Exponents use integer tuples, so repeated
cubic powers cannot cause positional-encoding carries.

Exact rank uses integer Gaussian elimination with gcd normalization of rows.
The verifier recomputes the ranks from the retained matrix construction; its
integer row operations preserve rational row space. The rational solution is
checked against all 83 rows and checked again after the artifacts are read back
from disk. No floating-point tolerance or modular-only rank inference is used.

## An explicit solution and why it works

Write E_r for the Euler operator in the three variables of row r, and define

    R(r,d) = sum_(|alpha|=d, supported in row r)
             d!/alpha! * partial^alpha composed with multiplication by y^alpha.

On a monomial of row degree q, this operator acts by

    R(r,d) = (q+3)(q+4)...(q+d+2).

For completeness, its eigenvalue is
sum_(|alpha|=d) d!/alpha! * product_j (e_j+alpha_j)!/e_j!.
The generating function for this sum divided by d! is the coefficient of t^d
in product_j(1-t)^(-e_j-1)=(1-t)^(-q-3), proving the formula.

Each row of g^(s-1) has degree s-1. Put u=s+2. The operator

    (3/2)*R(1,2)*R(2,1) - (1/2)*R(1,3)

therefore acts on g^(s-1) by

    (3/2)*u^2*(u+1) - (1/2)*u*(u+1)*(u+2)
      = u^3-u = (s+1)(s+2)(s+3).

The two row operators in the product use disjoint variables. On normal
ordering, this expression is exactly a permitted diagonal cubic T and A=0.
There are 18 nonzero entries whose monomials have degree two in row 1 and one
in row 2, and 10 whose monomials have degree three in row 1. These supports
are disjoint. All 28 diagonal entries are nonzero, so the total tensor rank is
exactly 28. The executable separately computes and sums the 100 block ranks.

This operator proof establishes the reduced identity for every positive
integer s, although the recorded matrix test uses only s=1,2,3,4. It applies to
any g of row multidegree (1,1,1). It says nothing about higher coefficients in t
or the existence of a sixteen-variable arc.

## Controls and scope

Restricting T to the single balanced block reproduces the saved 83 by 43
augmented matrix entry for entry, in its original row and column order. Exact
elimination returns coefficient rank 36 and augmented rank 37. The original
rational left witness, with 19 nonzero entries, satisfies w*M=0 and w*rhs=1.
Thus the earlier balanced-only obstruction remains valid.

Three fixed integer choices of A,H,k, including repeated powers and unequal
weights, were tested at all four powers. Each test expands the full polynomial
(z*g+t*w*k)^s, applies the displayed Laurent operator, and extracts t^0 at w=0.
All 12 results equal the independently assembled reduced expression, including
the factor s*z^(s-1).

Determinant and permanent controls in dimensions two and three through s=4
also passed. In particular, the per_3 control at s=3 has exactly six residual
monomials, each with coefficient 12, while the determinant controls vanish.
A separate full control expands

    F_t = det([[Y, t*u], [t*v^T, z]])

and its transported dual determinant operator. The six operator terms with
no normal derivative have power t^0; the other 18 have two normal derivatives
and power t^(-2). All t coefficients of the full normalized Cayley identities
were checked for s=1,2,3,4. This is a determinant degeneration with its own
two-normal residue, not a permanent repair. Its largest power has 10,147 terms.

The inspected `check_claude_depth2.js` concerns a different regular-operator
problem: 165 cubic operator coefficients D and two free scalar values in
D(g^2)=b_2*g and D(g^3)=b_3*g^2. This follow-up instead fixes the normalized
quartic b_4(s) and permits Laurent normal residues. Its consistent boundary
system does not overturn a regular-operator obstruction with arbitrary b(s).
That JavaScript input was inspected and hashed, not rerun in this pilot.

Passing these necessary identities proves no full Cayley arc, no global
determinant equation nonzero on padding, no separator, and no multiplicity gap.
Rank at most six is a restriction of the specified equivariant residue ansatz;
it is not a necessary restriction on arbitrary arcs after unconstrained
averaging. The current rank-28 witness does not fit six normal variables.

The raw maximal-minor ideal still vanishes on padding. For f using at most ten
variables, T_f factors through fourth-order symbols in ten variables, a space
of dimension 715; adjoining c_f has rank at most 716, so every 3877-minor
vanishes. The candidate

    I_3877([T_f | c_f]) : I_3876(T_f)^infinity

remains unresolved. No element of that saturation, no saturation membership
certificate, and no ideal comparison or highest-weight multiplicity count was
produced here.

## Resources and retained evidence

Exactly one scientific execution ran in the existing B15-01 Python 3.12.10
runtime with `-B`, through the fully inspected `analysis/b15_bound.py` wrapper.
It used one scientific process, all five configured BLAS/thread environment
variables equal to one, a 60 second wall cap, and an enforced 512 MiB Windows
process/job memory cap. The wrapper's watchdog thread is separate from the
scientific worker count.

The run began at 2026-09-14 03:46:40 UTC (September 13 at 11:46:40 p.m. EDT),
exited successfully, and took 0.452152 seconds in the wrapper. Peak working set
was 29,761,536 bytes (about 28.4 MiB); peak job/process committed memory was
21,028,864 bytes (about 20.1 MiB). The largest measured elimination intermediate
used 31 bits, well below the predeclared 4096-bit stop. No second scientific
run, subprocess, dependency install, low-rank search, or heavy lease was used.

The wrapper retained its historical `board_numbering: batch15` and session
metadata; those are runtime provenance, not a Batch17 board update. Its owned
logs are `work/batch15_workers/B15-01/results/logs/b17_capelli_repair.pid` and
`b17_capelli_repair_resources.json`. A byte-for-byte copy of the resource record
is included here as `resources.json`.

The deliverables are:

- `matrix.json`: all 83 rows, 345 coefficient columns, the right-hand side,
  column exponents, row labels, cubic monomials, and all 100 weight blocks.
- `certificate.json`: the complete rational solution, nonzero entries, exact
  ranks, pivots, and ranks of the T blocks.
- `verify_expanded.py`: independent construction, coefficient checks, exact
  elimination, solution verification, and the controls in one executable.
- `controls.json` and `verification.json`: complete control inputs and outcomes.
- `input_hashes.json`: byte-exact and CRLF-to-LF SHA-256 hashes of all five
  experiment inputs, the wrapper, runtime executable, verifier, and preflight.
  The verifier's recorded relative path is relative to the B15-01 working
  directory used by the command below.
- `preflight.md`: support, intermediate-size, memory, and operation pricing
  recorded before the only pilot.
- `resources.json` and `artifact_hashes.json`: resource provenance and final
  byte-exact artifact hashes. The hash manifest excludes itself.

An independently authorized replay can use the following PowerShell command
from `work/batch15_workers/B15-01`. Omitting `--produce` verifies the saved
artifacts; the original production run used `--produce` and log name
`b17_capelli_repair`.

```powershell
& './.venv/python.exe' -B './analysis/b15_bound.py' --seconds 60 --memory-mb 512 --name b17_capelli_repair_replay --slot 01 '../../capelli_cayley_investigation/expanded_repair/verify_expanded.py'
```

## One next test

A separately authorized bounded test can use the saved matrix for 100 exact
linear feasibility checks, one per weight block: impose that block of T is
zero while leaving A and all other blocks free. Any block whose deletion makes
the equations inconsistent is necessarily nonzero in every solution and
contributes at least one to total block rank. Seven such blocks would rule out
rank at most six with exact left witnesses, without polynomial solving. Fewer
than seven would leave the low-rank question unresolved; this test is only a
sufficient obstruction and may give no useful lower bound. It has not been run.
