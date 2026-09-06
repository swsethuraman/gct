# Integrator assessment — the external Rees boundary audit

The audit's computed ranks all reproduce here.  Its **headline structural
claim does not**: the "four transverse directions" at `C_{21} ∩ C_{32}` are an
artefact of an undercounted tangent space, and the correct number is **zero**.
That makes the negative result stronger than the audit states and removes the
cheap CAS target it proposes in its §11.

## 1. Reproduced exactly

At a generic point of `C_{21} ∩ C_{32}` (five matrices drawn at random from the
8-dimensional intersection space; two seeds, `p = 2147483647`):

| quantity | audit | here |
|---|---|---|
| `rank dΦ_{M_0}` | 16 | **16** |
| `dim ker dΦ_{M_0}` | 64 | **64** |
| `rank(π dΦ_{M_0})` | 12 | **12** |

`π` is the projection to the 35 quartic coefficients of `s_5`-degree zero, as in
session 59's reformulation `W = ker π`.  Nothing to correct here.

## 2. The correction — the tangent spaces fill the kernel

The audit computes `dim TC_{21} = dim TC_{32} = 50`, `dim(TC_{21} ∩ TC_{32}) = 40`,
hence `dim(TC_{21} + TC_{32}) = 60` and a transverse quotient of `64 − 60 = 4`.

50 is the dimension of the **fixed-flag** directions only: five matrices moving
inside one 10-dimensional compression space.  A compression component also moves
its flag.  For `C_{21}` the flag is `(U, V) ∈ Gr(2,4) × Gr(1,4)`, contributing
`4 + 3 = 7` further tangent directions, and `50 + 7 = 57`.  Measured here, by the
rank of the Jacobian of the full parametrisation `A_i = P B_i Q` with `B_i` in
the standard space and `P, Q` free:

| | audit | here |
|---|---|---|
| `dim T_{M_0} C_{21}` | 50 | **57** |
| `dim T_{M_0} C_{32}` | 50 | **57** |
| `dim(T C_{21} ∩ T C_{32})` | 40 | **50** |
| `dim(T C_{21} + T C_{32})` | 60 | **64** |
| **transverse quotient** | **4** | **0** |

Both seeds give the same.  Every one of the 82 spanning vectors of each tangent
space was checked to lie in `ker dΦ` — 0 outside — so the two subspaces really
are inside the kernel and the ranks measure what they should.

So at a generic point of `C_{21} ∩ C_{32}`

    ker dΦ_{M_0}  =  T_{M_0}C_{21} + T_{M_0}C_{32}      exactly.

Two further checks, same method:

- **Generic point of `C_{21}` alone**: `rank dΦ = 23`, `dim ker = 57`,
  `dim T C_{21} = 57`.  The kernel *is* the tangent space; transverse quotient 0.
  (This also confirms `dim C_{21} = 57 = 4 + 3 + 5·10` independently.)
- **Generic point of `ker ∩ coker`**: `rank dΦ = 5`, `dim ker = 75`,
  `dim T(ker) = dim T(coker) = 63`, `dim(sum) = 75`.  Transverse quotient 0
  again.

## 3. What this changes

**Stronger, not weaker.**  At every incidence tested, the first-order kernel is
exactly the span of the tangent spaces of the base components through the point.
There is no exotic first-order direction anywhere tested — which is a sharper
negative than "the exotic part is only four-dimensional".

**But the proposed next calculation loses its scoping.**  The audit's §11 asks
for the 23 quadrics in the 64-dimensional kernel and recommends a change of
coordinates `K = (TC_{21} + TC_{32}) ⊕ T` with `dim T = 4`, eliminating 60
tangential variables before primary decomposition.  **There is no `T`.**  The
quadric system and its minimal primes remain a legitimate object — a normal cone
can carry components that no tangent space sees, so "the tangent cone spans"
does not by itself close the loophole — but the dramatic reduction the audit
promises is not available, and a brief written around it would be written around
a number that is not there.

**The audit's §10 priority order should be rewritten.**  Its first priority is
`C_{21} ∩ C_{32}` *because* the transverse quotient is small; its second is
`ker ∩ coker` because its first-order reducible dimension 29 is closest to 31.
The first reason is void.  The second survives, but its transverse quotient is
also 0.  What is left, and what the audit itself ranks third, is the right first
priority: **the primitive family and its incidences**, which is the genuine
analogue of the `n = 3` skew-symmetric component that Hüttenhain–Lairez show
compression analysis misses.  Nothing in the compression world has produced a
transverse direction at any point tested.

## 4. Unaffected

The audit's other results stand as computed: the pencil-span degeneration table
(`28, 20, 18, 13, 5`), the first-order reducible dimensions at the four
intersections (`18, 18, 18, 29`), the `C_{21}` calibration `q = 1 = q = 2 = 28`
reproducing s54/s59, and the second-order mixed direction giving a local
reducible image of 27 at both house primes.  Note only that with
`ker dΦ = TC_{21} + TC_{32}`, the "genuinely mixed" `M_1 = u + v` is not a
special direction — *every* kernel direction is such a sum — so 27 is the value
at a generic second-order-solvable point of the incidence, not at an exotic one.
That reading makes it a better number, not a worse one.

Its `n = 3` calibration argument is the most valuable part of the audit and is
untouched by any of this: generic compression analysis provably misses a real
boundary component at `n = 3`, and that is the reason to fund the primitive
track rather than more compression work.

## 5. Method

`/root/work/s61v/rees_check.py`.  Base point: five matrices with random entries
in the 8-dimensional space `{columns 1,2 supported in row 1; column 3 in rows
1,2; column 4 free}`, the nested configuration `U ⊂ U'`, `V ⊂ V'`.  `dΦ` by
dual numbers on the 70 coefficients of `det(Σ s_i A_i)`, exact mod
`p = 2147483647`.  Tangent spans as the images of `δP·B_i + B_i·δQ + δB_i` with
`δB_i` in the relevant standard space — 82 spanning vectors per component, each
verified to annihilate `dΦ`.
