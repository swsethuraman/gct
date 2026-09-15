B17-05 priced finite pilot, 2026-09-13

Target: multiplication Hom_GL16(S_(69,19,2^8), E24 tensor A2) ->
Hom_GL16(S_(69,19,2^8), A26), where A=Sym(Sym^4 V) and
E24 is the one accepted flag copy S_(65,17,2^7) in A24. This is Jflag,
not the full degree24 ordinary remainder module J24 and not a saturation.

The quadratic multiplier decomposition is S8 + S62 + S44, with target
LR multiplicities 1+3+1. Five explicit contraction/transvection circuits
are derived before execution; only their image is evaluated. The upper
bound is five by representation theory. The full target determinant ideal
dimension ten is inherited from B16-04, accepted via Batch16/INTAKE.json.

Price: 14 fixed ambient jet points, 21 Hessian nodes at each point;
294 modular inverses/determinants of size10, one size21 interpolation
inverse, 14 products of size21 by21 and21 by101, plus inherited small
rational Hessian controls. Parameter series have exactly five slots
(orders0..4); every matrix has at most100 entries. Final image matrix14x5;
quotient matrix at most14x15. No coefficient-carrier expansion, padding
rank hunt, determinant orbit evaluation or symbolic elimination.

Estimated wall time 5-30 seconds; estimated peak committed memory below
128 MiB. These are pre-run estimates, not measurements. Related accepted
B16-06 complete receiver: 1.449 seconds, 64,737,280 committed bytes.
Hard cap60 seconds /512 MiB, existing inspected analysis/b15_bound.py,
existing .venv/python.exe -B, one process and one BLAS thread. Exactly one
scientific computation is allowed in this task; no retry if it fails or
hits the cap. The wrapper uses its existing timer thread for its deadline.
It does not spawn a subprocess. No heavy lease is requested or issued.

Success gate: five-column minor nonzero modulo2147483647, matching LR
upper five, and inherited P25/P26_62/P26_44 controls at every point. This
proves an exact characteristic-zero image dimension without interpreting
a sampled nullity as an equation. An independent augmented minor can then
certify representatives of the five-dimensional finite ideal quotient.
A smaller sampled rank remains a floor unless supported by a separately
proved identity; a cap hit is uncomputed. Full degree27 Jflag and full
J24 images are outside this pilot.

Exact command:

```powershell
.venv/python.exe -B analysis/b15_bound.py --slot 05 --name b17_05_image --seconds 60 --memory-mb 512 analysis/b17_05_verify.py
```
