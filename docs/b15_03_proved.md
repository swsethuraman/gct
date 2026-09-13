# B15-03 proof fragment: the first two-dimensional cell

Model: gpt-6-astra, xhigh. Status: **EXACT**. This is a per-slot proposal;
the canonical theorem index and exclusion ledger are unchanged.

## Claim

For n=4, degree 8, ambient variable count 16 and
lambda=(13,11,3,2,1,1,1), with Det the closure of the GL(16) orbit of det_4
and Pad the closure of the GL(16) orbit of z*per_3 with independent z,

\[
a=2,\qquad m_{\rm Det}=m_{\rm Pad}=2,\qquad
i_{\rm Det}=i_{\rm Pad}=0,\qquad D=0.
\]

Here a is the ambient highest-weight multiplicity in degree eight;
i_X and m_X are respectively the ideal and coordinate-ring multiplicities.
The pullback-space multiplicity h_pad=2 is a separate exact count, not an
assertion that its whole space is the image of restriction.

## 1. Ambient and pullback counts

The verifier analysis/b15_03_counts.py independently forms integer weight
multiplicities K(mu) as coefficients of

\[
\prod_{|\alpha|=n}(1-tx^\alpha)^{-1}.
\]

For r rows it evaluates the Weyl alternating sum
sum_(sigma in S_r) sign(sigma) K(lambda_i+sigma(i)-i), collecting equal
permuted weights. All counts use Python integers. The ambient result is two.
It agrees with a separate rational power-sum/Murnaghan-Nakayama computation
using the inherited wk8_s30_pleth.py implementation. Neither route uses
sampled ranks or fixed-width CRT reconstruction.

The pullback of quartics l*c has bidegree (8,8) in a linear form and a cubic.
By Pieri, its degree-eight multiplicity ceiling is
sum_nu a_3(nu,8), where lambda/nu is a horizontal eight-strip. There are
24 such nu. Exactly two have nonzero cubic multiplicity, both one:
(11,6,3,2,1,1) and (12,5,3,2,1,1). Since z*per_3 belongs to the reducible
family, m_pad <= min(a,h_pad)=2. This argument needs no assertion of cubic
orbit fullness and no equality between padded and reducible multiplicities.

The fresh signed Burnside count is
(519879 - 3*93167 + 2*9903)/6 = 43364.
The character is the sign character on the three equal rows of length one.
The quotient 519879/6 would not be the correct dimension.

Evidence: results/b15_03/counts_primary.json and count_controls.json.
Verifier: analysis/b15_03_counts.py, modes controls and primary.
Dependencies: Weyl character formula, Frobenius plethysm formula, Pieri rule;
the banked character implementation is a cross-check, not the only count.

## 2. Explicit integral highest-weight sources

Let c_alpha=[x^alpha]f denote ordinary quartic coefficients, not factorial
symbols. The polynomial representation on these generators has simple raising
rule E_(i,i+1)c_alpha=(alpha_i+1)c_(alpha+e_i-e_(i+1)) when alpha_(i+1)>0,
and zero otherwise. The action extends by the Leibniz rule.

The complete native definition of two integer polynomials is:

\[
P_j(f)=\sum_{m:\,\mathrm{col}[m]\ge0}
\mathrm{sgn}[m]\,K_{\mathrm{col}[m],j}
\prod_{k=0}^{7}c_{\alpha(M_{m,k})}(f),\quad j=0,1.
\]

The file native_carrier.npz supplies M, col_of and sgn. Its SHA-256 is
7f81aa647098e45650b2f53355b20349d913320fda397e7ce339d52618e89213.
The coefficient file integral_source.json supplies 6105 nonzero rows of K;
all other rows are zero. There are 36630 active native monomials in their
combined support. Letter alpha(k) is specified by the explicit ascending
recursive exponent enumeration in analysis/b15_03_exact.py; it is not inferred
from a historical literal. The formula defines the polynomials even without
the discovery algorithm or any assertion about the full carrier basis.

Discovery used two modular kernels and rational reconstruction from the first
prime. Denominators 48 and 192 were cleared. Reconstruction is only a means
of obtaining these explicit integer coefficients. The following independent
checks establish their membership directly over Q:

* Every source monomial has quartic coefficient degree eight and weight lambda.
* Each of all six simple raising operators gives the zero polynomial over Z.
  The verifier forms all monomial images, with no stabilizer quotient or
  inherited raising-row code, and combines them by an injective combinadic.
* The absolute sum bound on every integer accumulation is 72534720, below
  2^63 by the explicitly recorded signed margin. The monomial combinadic
  also lies below 2^63. Geometric values use unbounded Python integers.

Consequently each P_j is a highest-weight polynomial. Extending coefficient
indices by nine zeros gives the corresponding weight in C^16. The additional
simple raising operators vanish because no letter uses the new coordinates.
The two source vectors are independent by the determinant minor below.

Evidence: integral_source.json, native_carrier.npz, exact_certificate.json.
Verifier: analysis/b15_03_exact.py. Its final membership proof does not require
modular lifting, a modular uniqueness bound, or completeness of the sparse
raising matrix used during discovery. The source file's CANDIDATE status
describes reconstruction before verification; exact_certificate.json records
the subsequent exact evidence.

## 3. Points and rank certificates

All frames and pencils are explicit integer arrays in points.json. There are
seven restriction variables. Det points are det_4(sum_i x_i A_i) with A_i
integral 4-by-4 matrices. Pad points use an integral 7-by-10 frame V:
the independent padding form is sum_i V_(i,0)x_i, and the permanent matrix
entry (a,b) is sum_i V_(i,1+3a+b)x_i. These are restrictions of the full
ten-essential-variable independently padded permanent, embedded in C^16.

The discovery pass verified that every determinant 7-by-16 frame and padded
7-by-10 frame has rank seven modulo each prime, hence over Q. Each extends
to an invertible ambient frame. Evaluating an HWV that uses the first seven
coordinates therefore gives a value on an ambient orbit point. Even a rank
deficient frame would give a point of the polynomially parameterized closure;
no different seven-variable orbit is substituted for the ambient variety.

The exact verifier rebuilds det_4 coefficients by the 24 signed permutations,
and z*per_3 coefficients by the six unsigned permutations with the independent
linear factor. It then evaluates the two source polynomials by scalar integer
multiplication. For the first two points of each family, rows are points and
columns are P_0,P_1. The determinant values are

```
-209240041026114257696   105105215636725381024
 323482128062169539664  -107464023673882496136
```

Their 2-by-2 minor is
**-11513882102246656749727216917727852673280**, which is nonzero.
The padded values are

```
-17641872916969840  35728228008240944
    30743196993792    434564738567424
```

Their minor is **-8764935843899184496923422711808**, also nonzero.
Thus the restriction maps on the two-dimensional ambient highest-weight
space both have rank two. This proves the claim, including D=0.

The diagonal-pencil family is independently rebuilt as determinants and gives
zero on both polynomials at both saved points. A changed source coefficient
is rejected by exact raising; changing an ordinary quartic coefficient changes
the exact evaluation. Separate small known liveness and normalization controls
were performed before discovery. The research cell's determinant rank was
never required to be nonzero for a control to pass.

Evidence: exact_certificate.json and standalone_replay.json. The second pass
loads the saved integer source and regenerates the geometric coefficients and
values; it is not elimination on saved evaluation matrices. Both passes ran
inside the one authorized follow-up process.

## 4. Scope and next witness

No canonical exclusion or shared theorem record was edited. The scoped ledger
and accepted-state overlay had no prior closure for this cell. The proof uses
no inherited numerical rank, cubic transfer, LMR result, or other worker result.
The mathematical conventions and standard representation-theoretic rank
interpretation are inherited premises, separately identified above.

The primary cell has no missing witness: its exact multiplicities are settled.
For the separately sized cell (11,8,8,2,1,1,1), degree eight, the independent
counts give a=4 and h_pad=2. No geometric rank was measured there. Two valid
determinant directions would exclude positive D; padded rank two together
with three global independent determinant equations would certify positive D.
