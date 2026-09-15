# Bounded expanded Cayley repair pilot

Prepared before the only scientific execution. Output ownership is confined to
this directory, plus `b17_capelli_repair*` logs under the existing B15-01 runner.
No input script is executed or modified. All five experiment inputs and the
entire runtime wrapper were inspected. No applicable AGENTS.md was found in the
workspace ancestry or these work directories.

Use existing `work/batch15_workers/B15-01/.venv/python.exe -B` and the inspected
`analysis/b15_bound.py`, with a 60 second wall deadline, 512 MiB process/job cap,
one scientific process and one configured BLAS thread. The wrapper has a
watchdog thread, enforces its Windows Job Object cap, and records its own peak
memory. There is no dependency installation or subprocess creation.

Support pricing: degree-three monomials in nine variables number C(11,3)=165.
The weight blocks have dimensions 1 (51 blocks), 2 (36), 3 (12), and 6 (1), so
there are 100 blocks and 51+144+108+36=339 ordered equal-weight pairs. The powers
g^0 through g^4 have at most 1,6,21,55,120 distinct balanced monomials. The four
equations therefore have 1+6+21+55=83 rows and 345 unknowns. Construction visits
339*83 + 6*(6+21+55+120)=29,349 sparse input terms, each with nine exponents.
The retained augmented matrix has 28,718 integer cells. The exact echelon
calculation uses at most 83 pivots and roughly 2.4 million cell updates; it
normalizes integer rows by gcd, and aborts if an intermediate exceeds 4096 bits.
A second coefficient formula checks all cells independently of the sparse
derivative construction. This is an operation/support bound, not a measured
runtime guarantee.

The explicit candidate uses A=0 and 28 diagonal T entries. Put
R(r,d)=sum_{|alpha|=d, supported in row r} d!/alpha! partial^alpha y^alpha.
For any polynomial of row degree s-1, R(r,d) acts by the rising factorial
(s+2)...(s+d+1). Thus (3/2)R(1,2)R(2,1)-(1/2)R(1,3) acts by
(s+1)(s+2)(s+3). This finite formula will be checked, without searching for a
rank-six tensor. Its diagonal tensor has rank 28; rank at most six is unresolved.

Controls: reconstruct the saved balanced matrix and its rational left witness;
recompute exact ranks 36 and 37; directly expand (z*g+t*w*k)^s for three fixed
integer choices of A,H,k including repeated powers and extract t^0 at w=0;
check determinant/permanent differentiation through s=4 in dimensions 2 and 3;
check the full 4x4 block determinant Cayley identity with off-diagonal blocks
scaled by t. The latter has 24 determinant terms and at most C(27,4)=17,550
power terms, and at most 24*17,550 operator/term visits at the largest power.
Sparse polynomial dictionaries are capped at 30,000 terms. The direct normal
controls use at most ten input terms, with at most C(13,4)=715 fourth-power
terms. Conservative planned process memory is below 128 MiB; the enforced cap
is 512 MiB. A deadline check accompanies major stages. No low-rank search,
unbounded polynomial solve, larger-degree expansion, or second pilot is planned.
