# Exact toy calculations and reproduction notes

## A. Signed row/column compatibility is not multiplicity separation

For P,Q∈S3, the transformations X→diag(P,sgn P) X diag(Q,sgn Q)^T fix det4 and multiply x44*per3 by sgn(P)sgn(Q). The padding character in degree d is its d-th power. At d=1 both orbit closures have multiplicity one in the sole ambient module S_(4)C16. This is an exact counterexample to “different stabilizer characters imply a multiplicity gap.”

No computation is needed: the ambient degree-one module is irreducible, and a nonzero vector in its dual generates the full dual module under GL16.

## B. Every proper 3×3 entry-support probe is signable

For independent symbols a,b,c,d,e,f,g,h,

```
per([[a,b,c],[d,e,f],[g,h,0]])
 = a*f*h + b*f*g + c*d*h + c*e*g
 = det([[-a,b,c],[d,-e,f],[g,h,0]]).
```

Substitute arbitrary linear forms into these symbols and append the 1×1 block z. The resulting 4×4 determinant equals the proposed padded probe. Moving any missing entry to the bottom right by row and column permutations covers every proper entry support, including supports with multiple missing entries.

For the full support, list the six permutation parities:

| σ(1)σ(2)σ(3) | Parity mod 2 |
|---|---:|
| 123 | 0 |
| 132 | 1 |
| 213 | 1 |
| 231 | 0 |
| 312 | 0 |
| 321 | 1 |

The six sign equations sum to 0=1: every edge occurs twice while the parity sum is odd. This proves the full symbolic permanent is not converted to determinant by entry signs. It does not prove a multiplicity obstruction, nor prevent a larger determinant representation.

## C. An actual padding multiplicity control

Both det4 and z*per3 specialize to l1*l2*l3*l4 for arbitrary linear forms l_i. Every binary quartic splits in this fashion over C. Consequently the full subspace variety of binary quartics is contained in both closures. No two-row highest-weight polynomial can vanish there unless it is the zero polynomial, so m_det=m_pad=a in every two-row cell.

The exact character table contains d=5, λ=(16,4), with a=2, g=2, s=2 and U=2. Thus the actual coordinate multiplicities, not merely orbit bounds, equal 2 in this example. This also explains why diagonal permanent degenerations cannot furnish the desired gap.

## D. Machine calculation

`toy_character_screen.py` contains no third-party imports and performs no network requests. The hard maximum degree is 6. The source coefficient calculation is

\[
h_d[h_n]=\sum_{\alpha\vdash d}\frac1{z_\alpha}
\prod_{j\in\alpha}\left(\sum_{\beta\vdash n}\frac{p_{j\beta}}{z_\beta}\right),
\qquad a_\lambda=\langle s_\lambda,h_d[h_n]\rangle.
\]

Characters use the beta-number form of Murnaghan–Nakayama: a length-k rim hook is a move b→b−k to an unoccupied nonnegative position; its sign is (−1) to the number of beta numbers strictly between those positions. Character sums compute connected and symmetric rectangular Kronecker coefficients. The padding source sums cubic plethysm multiplicities over horizontal strips, retaining the essential-dimension≤9 restriction. At these tiny degrees length≤d already enforces that core restriction.

Checks performed in both runs:

* Complete character row orthogonality for symmetric groups S1 through S6.
* S4 controls: for R=(3,1), the trivial constituent has (g,t,s,alternating)=(1,1,1,0), while λ=(2,1,1) has (1,−1,0,1).
* Sym²(Sym⁴)=S_(8)⊕S_(6,2)⊕S_(4,4).
* Full ambient dimension reconstruction in 16 variables at every computed degree.
* Integrality/nonnegativity of every multiplicity, and integrality of every transpose trace.

These are reproducible exact arithmetic calculations, not an independent formal verification of the program. The symbolic proofs in A–C do not depend on a sampled rank.

Run in the Astra directory, using the existing, inspected wrapper:

```powershell
& 'C:/Users/swami/Projects/gct-gpt/work/batch15_workers/B15-01/.venv/python.exe' -B 'C:/Users/swami/Projects/gct-gpt/work/batch15_workers/B15-01/analysis/b15_bound.py' --slot astra-dream --name toy_character_screen --seconds 60 --memory-mb 512 'toy_character_screen.py'
& 'C:/Users/swami/Projects/gct-gpt/work/batch15_workers/B15-01/.venv/python.exe' -B 'C:/Users/swami/Projects/gct-gpt/work/batch15_workers/B15-01/analysis/b15_bound.py' --slot astra-dream --name toy_character_screen_d5_d6 --seconds 60 --memory-mb 512 'toy_character_screen.py' 5 6
```

The script was extended after the first run to accept the range 5–6; the mathematical routines and controls were unchanged. The final file reproduces either range. The wrapper enforces aggregate process/Job Object committed memory, a wall-clock deadline, and one thread in the standard BLAS environment variables. It writes its logs relative to the current directory, so the closed worker tree is read only. `-B` suppresses Python bytecode writes. Its inherited session-prefix text has no scheduling effect.

| Range | Wall seconds | Peak Job Object committed bytes | Exit status |
|---|---:|---:|---:|
| 1–4 | 0.103368 | 16,134,144 | 0 |
| 5–6 | 6.0928214 | 158,150,656 | 0 |

Saved results: `toy_character_screen.json`, `toy_character_screen_d5_d6.json`; resource receipts: `results/logs/toy_character_screen_resources.json`, `results/logs/toy_character_screen_d5_d6_resources.json`.

There were no other research computations. File reads, hashing and report assembly are not mathematical worker runs. No closed-batch scripts were dispatched apart from using the read-only generic resource wrapper to run our local toy script.
