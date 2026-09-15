# B16-08 delivery

**Exact result:** On the shared three-direction determinant root chart,
there is no nonzero relation of ordinary coefficient degree at most two
among its 34 Taylor coefficients. All 630 candidate monomials are
independent, proved by 165 nonzero modular minors after an exact
multigrading decomposition. The largest minor is 10-by-10. The same
blocks a,r,c,E are retained across orders 1 through 4.

The universal block formula was independently expanded in all sixteen
unrestricted matrix entries, with zero symbolic residual. This is a
realization-variable identity, not a new equation in quartic
coefficients. No global sixteen-variable equation, highest-weight module,
new ideal floor or positive multiplicity gap is claimed.

The producer saved ten explicit integer triples of matrices, all 340
integer jet values, all 3072 entries of the square block matrices, their
determinants modulo 2147483647, and the 49 universal entry monomials.
The receiver rebuilt them with direct 24-term determinant expansion and
rejected cubic-coefficient and duplicated-row mutations. Proof and scope
are in `docs/b16_08_proof.md`; certificate, prices and receiver result
are in `results/b16_08/`.

Fresh mathematical runs, all with enforced 60s/512MiB caps:

| Run | Wall seconds | Peak working set bytes | Peak Job bytes | Exit |
|---|---:|---:|---:|---:|
| Preflight | 0.05525 | 30158848 | 17231872 | 0 |
| Initial fixed-row selection | 0.06816 | 30838784 | 17870848 | 1 |
| Pivoted elimination | 0.07614 | 31993856 | 19042304 | 0 |
| Direct coefficient receiver | 0.06822 | 30650368 | 17858560 | 0 |

The failed selection is retained: a zero first-point linear coefficient
made a chosen 1-by-1 minor zero. Selecting independent rows among the
same ten points resolved this without expanding the sample budget or
inferring an equation. The successful proof uses explicit nonzero minors.

No heavy lease was acquired or used; none remains held. All listed
processes exited, and exit checks are recorded in delivery. No old B15
computation was repeated. Read-only Git verified the frozen head; no
staging, commit, configuration change, push or publication occurred.
Input hashes and exact fresh/inherited boundaries accompany the delivery.

**Next sufficient witness:** An exact nonzero eliminant of degree at
least three in this chart, with complete substitution-zero proof, then
root/basepoint and normalization removal yielding a nonzero polynomial
in sixteen-variable quartic coefficients. Prove its arbitrary determinant
substitution identity, finite weight and LMR-image comparison, and pair
its ideal floor with an actual independent z*per3 coordinate floor in
one finite cell. No heavy extension is requested for this completed
bounded experiment.
