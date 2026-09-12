# B14-11 — proofs and conventions

**PROVED.** Work over a characteristic-zero field, with form space
`Sym^4 V*` and coefficient ring `A_delta=Sym^delta(Sym^4 V)`.
Labels are descending partitions of `4 delta`. Use `P` for the closure of
pullbacks of `x0 per3` with an independent padding variable, `R` for the
closure of all `l c`, and `D` for determinant pullbacks. Then `P subset R`.
The gap is `mult_P-mult_D`; a positive gap would disprove `P subset D`.

## 1. Direct quartic support and eligibility bounds

**PROVED: quartic_length_and_eligibility.** If `a_lambda(delta)>0`, then
`length(lambda)<=min(dim V,delta)`. If `mult_P(lambda,delta)>0`, then also
`lambda_1>=delta`.

For the length statement, averaging over factor permutations gives the
injection

`Sym^delta(Sym^4 V) -> (Sym^4 V)^{tensor delta}`.

The averaging requires only `delta!` invertible. A constituent of the right
side is obtained from the empty partition by successively multiplying by
`s_(4)`. Pieri adds a horizontal four-strip at each step. Such a strip creates
at most one new row: boxes in two new rows would share column one, contradicting
horizontalness. After `delta` steps the diagram has at most `delta` rows.
Submodules and quotient coordinate rings cannot introduce another constituent.
This proof concerns quartics directly; it uses no cubic-ideal theorem and no
essential-variable nine-row clamp.

For the first-row statement, the polynomial map `(l,c) -> l c` gives an
injective pullback from `C[R]_delta` into

`B_delta = Sym^delta V tensor Sym^delta(Sym^3 V)`.

Indeed its kernel on `A_delta` is exactly the ideal of the image closure.
If `S_lambda` occurs in `B_delta`, Pieri gives a partition `nu` of `3 delta`
such that `lambda/nu` is a horizontal `delta`-strip. Its `delta` boxes occupy
distinct columns, so the outer diagram has at least `delta` columns:
`lambda_1>=delta`. Since `C[R]` surjects onto `C[P]`, the necessity passes
to `P`. No normalisation theorem or literature-padding identification is
needed for this argument.

**PROVED.** At `length(lambda)<=4` the existing `n4_gate_containment`
excludes a positive padded gap, under its ADOPTED generic determinantal-cubic
input. It does not assert `mult_D=a`. Its failure to prove containment at
length five is not a noncontainment certificate there. The direct length bound
also makes the requested interval empty for `delta<=4`.

## 2. Exact pullback-zero exclusions

**PROVED: quartic_pullback_zero.** Put

`h_lambda(delta) = sum_{lambda/nu horizontal delta-strip} [s_nu]h_delta[h_3]`.

The injection above proves `0<=mult_P<=mult_R<=h_lambda`. Thus an exact
`h_lambda=0` proves `mult_P=0` and `mult_P-mult_D<=0`, independently of
determinant measurements. Merely `h_lambda<a` proves a reducible ideal
multiplicity lower bound; it does not exclude a positive padded gap.
Positive `h_lambda` is an upper bound and does not prove `mult_P>0`.

**CERTIFIED, finite combinatorics.** The delivered 153 explicit keys have
positive quartic ambient multiplicity and `h_lambda=0`. Every horizontal-strip
channel and its exact cubic coefficient is saved. The verifier checks the
complete channel sets against a second interlacing enumeration and recomputes
the coefficients. This is a finite exclusion certificate, not an evaluation
rank certificate. No absence-of-equation or deficient sampled rank is used.

## 3. Exact coefficient computation

**PROVED formula; CERTIFIED finite evaluation.** The power-sum expansion is

`h_d[h_n] = sum_{rho |- d} (1/z_rho) product_{r in rho}
             (sum_{sigma |- n} p_(r sigma)/z_sigma)`.

Here `z_rho=product_j j^{m_j} m_j!`. The scalar product with `s_lambda` is
`sum_tau c_tau chi_lambda(tau)`. The banked Murnaghan–Nakayama routine moves
a beta number `b` to an unoccupied nonnegative `b-r` and assigns the rim-hook
sign by the number of beta numbers strictly between. This is exactly the
rim-hook character recurrence. All sums use Python integers and reduced
`Fraction` arithmetic; nonintegrality or negativity raises an error.

The census enumerates every partition with the requested sum, length and
first row, including coefficients that turn out zero. Small positive and
zero coefficients agree with a separate coefficient-monomial DP followed
by Weyl alternation. Corrupting each control's result is rejected. The full
census is replayable, not a random sample. Agreement with the old census
is reproduction of its character method, not a second lineage for every cell.

**CERTIFIED denominator compatibility.** Common quartic power-sum denominators
at degrees 5,6,7,8 are respectively `955514880`, `137594142720`,
`23115815976960`, `4438236667576320`; each is coprime to both house primes.
The same is checked for the cubic coefficient sums. The underlying coefficient
monomial lattice is over Z; the calculation computes its characteristic-zero
character. No modular rank is compared with a rational rank in this session.

## 4. Signed Burnside sizing

**PROVED: quartic_signed_burnside_size.** Let `M_lambda` be the coefficient
monomials of degree `delta` and weight `lambda`, and let
`G_lambda=product_b S_{m_b}` permute coordinates having equal weight part `b`.
The HWV transforms on each equal-part block by `det^b`, hence under this
permutation subgroup by the one-dimensional character
`epsilon(g)=product_b sign(g_b)^b`. The reduced carrier dimension is

`n_chi = (1/|G_lambda|) sum_g epsilon(g) |Fix_{M_lambda}(g)|`.

This follows by taking the trace of the character idempotent on the permutation
representation with basis `M_lambda`. It is also the number of monomial orbits
whose stabilisers have trivial restriction of `epsilon`. Thus
`0<=n_chi<=N_S=|M_lambda|`; no quotient `N_S/|G_lambda|` is substituted.

For each representative `g`, it permutes quartic exponent letters. A fixed
monomial uses each letter in an orbit `O` equally often; that orbit contributes
the factor `(1-t^{|O|}x^{sum_{alpha in O}alpha})^{-1}`. The coefficient
of `t^delta x^lambda` in the product is its fixed-monomial trace. Since each
letter has total degree four, the first exponent is determined by the
degree and the remaining exponents, which justifies the small tail DP.
The DP uses arbitrary-size integer objects; it has no int64 overflow path.
Conjugacy classes suffice, with class size `m!/z_type` on each block.

**CERTIFIED.** Every selected size ships representatives, class sizes,
character signs and integer traces. Explicit monomial-orbit enumeration checks
four small weights, including odd repeated parts. At `(3,3,1,1)_2` the correct
dimension is 2, whereas suppressing the sign gives 4. A banked quartic control
`(14,2,2,2,2,2)_6` reproduces `N_S=7508`, `n_chi=171`.
The ten selected sizes are replayed in validation. These dimensions are carrier
sizes, not highest-weight multiplicities or ranks on a variety.

## 5. BIP audit boundaries

**ADOPTED, source checked.** BIP v3 Theorem 1.4 assumes `n>=m^25`; it
supplies no A1 exclusion at `(4,3)`. Its page-2 padded model uses an existing
permanent variable. That model's nine-variable support bound is not the
independent-padding ten-variable support bound used here. Its `sharp` notation
extends the existing first row; at `n=4` Proposition 2.3 gives `(4)_1` and
`(6,2)_2`, with at most two rows. Source: https://arxiv.org/pdf/1604.06431.

**PROVED corrections.** The corrected Schur-support lemma and its elementary
counterexample to arbitrary-weight wording are in `docs/bip_transfer.md`.
Changing coordinates does not preserve an arbitrary torus weight character.
The polynomial `(x+y)^4` has essential span one and coefficient of `x^3 y`
equal to 4, so the old weight-only lemma was false. The HWV conclusion survives.
A product of four linear forms has essential span at most four even when all
six named coordinates occur, so a `chow6` sample is not a full-span-six control.
