# S1 relay to the integrator for s76 / s74 / s75

**Ready for independent review; no message has been dispatched.**

Replace old-span elimination during source birth selection with direct circuit evaluation on **u=c_(4,0,...,0)=0**. The report proves `ker(restriction|M_d)=u M_(d-1)`. A nonzero birth minor certifies new classes, and old vectors need no reevaluation on those points. Use the corrected births `2,37,54,52,43,31,22,14,9,5,3,1,1`.

Use pure-u factor detection before evaluation: a letter occupying only four singleton columns contributes exactly `24*u`. It is zero in the birth quotient and is transported, not zero, in the full source. Preserve the original filling, source coefficient, column signs and degree of origin. The proven global zero test is `h-k>n`; stronger empirical overlap exclusions are not licensed.

The matched 64-candidate n=3 control retains the same 22 nonzero birth classes as a seven-point old-span residual test, reducing 448 evaluator calls to 37 after the exact pure-u sieve. This does not establish a better candidate hit rate, and it is not a measured n=4 end-to-end speedup. See `run_results.md` for timing qualifications.

Replay the 34-vector n=4 ladder checkpoint rather than restart it: two native degree-12 vectors and 32 degree-13 candidates are present. Only eight of the 32 degree-13 classes were freshly checked here, using 8x10 u=0 matrices at both primes. Five degree-13 classes remain missing if all 32 saved classes replay successfully. Later births remain unfilled. The separate 113-vector target source must not be added numerically to these counts.

Ten independent target source vectors, normalized as `u^(24-d)*F_native`, are supplied in `partial_source_10.json`. Literal lifted fillings have an additional `24^(24-d)` factor; the artifact supplies its reciprocal explicitly. Maintain these same source coordinates on det/red/true-pad evaluation. The transported seed determinant minor gives only rank >=2 at the target. Rank 273 / padded rank 274 remain OPEN.

The short-column Plucker identity is proved and implemented, but full expansion hit the 64-term cap on all 113 archived target fillings. Retain it only as a bounded local relation, not as a target basis engine. Complete tall-column relations and a noncircular candidate-hitting bound remain the scientific residue.

Suggested first implementation trial: b+8 points on u=0, streaming matrices at most (b+1)x(b+8), and a fixed 256-candidate per-rung budget. Stop at b certified births. On a stall, return the exact saved candidate list, residual rank, seeds, points and minors. Do not increase the census automatically. Replacing the remaining random candidate discovery requires a new theorem or measured evidence; S1 does not authorize that replacement.

For s75: the post-construction coefficient solve `x=y A^(-1)` converts an evaluable Pieri vector to a certified circuit basis. It cannot be used to assume that missing basis. The compact Pieri embeddings, recoupling coefficients, and evaluator are still needed; B24=2168 does not supply them.

Before promotion, review the polynomial proof, the shared normalization packer and the independent minor paths. The native house selftest could not run because flint is missing. The n=3 exact archived chi-vector comparison was recomputed, but literal expansion and the raising matrix were not rebuilt. Frozen artifacts and all corresponding qualifications are in the report and manifests.
