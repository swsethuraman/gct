# gct — conductors and deficits of orbit closures

An anabelian↔GCT dictionary, made computational.

This repository contains the code, inputs, exact outputs, and full commit
history behind the paper *Conductors of orbit closures, and the fundamental
invariant of the 3×3 determinant* (`paper/det3-conductor.tex`).

Everything here is exact integer arithmetic. There is no floating point
anywhere in the pipeline.

---

## What is computed

For a form `v` with orbit closure `Ω̄ = closure(G·v)`, the **boundary deficit**

```
def(λ, δ) = dim S_λ^H  −  mult_λ ℂ[Ω̄]_δ  ≥ 0
```

measures the gap between the stabiliser's Peter–Weyl count and the coordinate
ring of the closure. The **conductor** `c(λ, δ)` is the depth of that gap along
the boundary, measured in multiplications by a boundary semiinvariant.

---

## Results

| | result | status |
|---|---|---|
| Binary quartics | `def = c = ⌊(a−3b)/8⌋⁺`; total deficit at degree δ is `⌊δ²/4⌋` | proved; verified δ ≤ 60 |
| Ternary cubics | `c(λ) = ⌊(λ₁−2λ₃)/6⌋ = ⌊μ_max/|w_N|⌋` (transport formula) | proved ≤; equality on all 254 weights, δ ≤ 10 |
| det₃ | `e(det₃) = 18 = 2n²`, invariant space 1-dimensional | proved |
| det₃ | `Φ₁₈(det₃) = −877,879,296,000 = −2¹⁶·3⁷·5³·7²` | exact |
| det₃ | `V(Φ₁₈) ∩ Ω̄ = ∂Ω̄`; `div(Φ₁₈) = 6P₁ + 9P₂` | proved |
| det₃ | invariant ring is a numerical semigroup ring | proved |
| perm₃ | `Φ₁₈(perm₃) = +50,536,120,320 = 2²⁰·3⁴·5·7·17`, hence `perm₃ ∉ Ω̄` | exact |
| det₃ | `def((2,2,2),2) = 1`, `c((2,2,2),2) = 1`, ray-complete | certified at two inequivalent points |
| gauge | `Ψ = 2u₁ − 4u₂ − D` is the unique det²-equivariant invariant in its bidegree | proved |
| gauge | `I₆(I,A,B) = −6·Ψ(A,B)` — Ψ *is* the Aronhold invariant | exact symbolic identity, 18 indeterminates |
| totals | `TOTAL(N) = Ψ(N)·1,152,144,000` | tested at Ψ = 1, 4, 0 only — **not proved** |

`e(det₃) = 18 = 2n²` is strictly above the Bürgisser–Ikenmeyer bound
`e(det_n) ≥ n²`, which they show is attained at `n = 2, 4`. The 3×3
determinant is the first determinant whose fundamental invariant does not
live in degree `n²`.

### The certification

`TOTAL = 1,152,144,000` was certified at two points `C` and `R` of the orbit
that are provably *H*-inequivalent: the intersection algebra
`𝔰(u) = 𝔥 ∩ Ad(u)𝔥` is 4-dimensional at both, but non-abelian at `C` and
abelian at `R`. No symmetry of the setup carries one to the other, so the
agreement is a check with content rather than the same computation in two
coordinate systems.

### What is *not* proved

The totals law `TOTAL(N) = Ψ(N)·1,152,144,000` is **empirical**. It has been
tested at `Ψ = 1` (C, R), `Ψ = 4` (X4), and `Ψ = 0` (P and four compression
points) — and at no other value. `X_{-3}`, where `Ψ = −3`, has not been
measured.

There is now a proof route with exactly one gap:

1. `TOTAL` is bidegree (2,2) — **proved**
2. `TOTAL` is constant on `Q·u·H` up to a character `χ`, and that coset is the
   H-orbit of the net *as a subspace* — **proved**
3. subspace-only dependence would make the third-slot basis change act
   trivially, so `TOTAL` would be a conjugation invariant with slab
   equivariance of character `χ` — **not verified**
4. if `χ = det²`, uniqueness forces `TOTAL = c·Ψ` with `c = 1,152,144,000`
   from C — **proved, conditional on 3**

The single unproved link is `χ ↔ det²`. Evidence: `χ = Ψ` on 120/120
same-coset pairs tested. Evidence, not proof.

Three pre-registered hypotheses were **refuted**, each by a single number, and
all three are kept in the record:

- per-σ values do **not** inherit GL₂-covariance — `f1X4_00 = −308,145,600`
  against a pre-registered `+434,851,200`
- per-σ values are **not** simultaneous-conjugation invariants — a rank-9
  parameter-free fit predicted `f1Y4_00 = +69,854,400`; the engine returned `0`
- both plane-cubic routes are dead, and the pencil cubic is insufficient

None of these touch the det₃ results: the conductor, the value at R, and the
ray closure use no covariance assumption anywhere. The refutations confine the
phenomenon to the totals level, which is where the law is stated.

---

## Layout

```
engine/      dp.c — exact streamed level DP (see below)
analysis/    sympy/python scripts, one per session, wk<N>_s<M>_*.py
inputs/      evaluation points, slab normal forms
results/     canonical value records with prediction ledgers
scripts/     regression suite, harvest, reproduction drivers
paper/       det3-conductor.tex  (arXiv source)
docs/        conductor.html      (working paper)
             boundary-deficit.html (companion log)
```

## The engine

`engine/dp.c` is an exact streamed level DP:

- level states packed into 54-bit masks in `u64`
- 2²⁶-slot open-addressing table
- delta-varint compressed spill runs (≈5.5× on the observed data)
- bounded shard passes, shard count auto-doubling at a 6 GB budget
- atomic `ck2` checkpoints written at every spill, so an interrupted run
  resumes at the last spill rather than the last level

Build and reproduce the regression suite (seconds, no long runs):

```sh
cc -O2 -o dp engine/dp.c
scripts/regress.sh
```

Expected regression values — any deviation aborts:

```
quad      = 24
quad0     = 0
quadq raw = 6×4 = 24

det3   L2 = 29 / 29 / 29
       ...
       L6 = 1818118 / 2336283 / 2686868

f1C_00 L7 = 54685987 / 100774838 / 141001840
       L8 = 128027708 / 422952740 / 603408404
```

The full `f1C` grind is long. It is checkpointed; restart with the same
command and it resumes.

## Anchors

The pipeline is pinned at both ends. On ℂ²⊗ℂ²⊗ℂ² the same code path
reproduces Cayley's hyperdeterminant exactly on the standard test points: 0 at
the two rank-one points, 0 at the W-state, 1 at GHZ, and
`9,572,836 = 3094²` at a generic rank-two point. At the classical end it reproduces the closed forms for
binary quartics and ternary cubics independently derived in the paper.

## Arithmetic signature

Every measured subvalue is an integer multiple of `75,600 = 2⁴·3³·5²·7`.
Ten of them — the leading value at `C`, `R`, `Q`, `T₄`, the eight orbit values
at `X₄`, and the leading value at `X₋₃` — are multiples of twice that,
`151,200`, with cofactors

```
719, −2038, 5907, −4372, 4338, 3567, 3843, −5188, −258, −4552
```

but that is a property of those ten and not of the functional. **This entry
previously claimed `151,200` for every subvalue and that was wrong.** The
three-cycle class in the degree-20 table at `C` is
`W(3-cycle) = +301,870,800 = 75,600 × 3993`, an *odd* multiple, and three of
the twelve orbit values at `X₋₃` are too. The gcd of all twenty-one subvalues
on record is exactly `75,600`. The correction is session 23's; see
`results/results_Xm3.md`.

The common factor is not imposed anywhere in the code. We have no proof of it.
It survived every reorganisation of the computation and every change of
evaluation point. Note it is a statement about evaluations at `det₃`:
`Φ₁₈(per₃)` and `Φ₂₄(per₃)` are not multiples of `75,600`.

---

## On the commit history

The history is not tidy, and that is deliberate: it is part of the evidence.

Predictions were committed to version control **before** the corresponding
values existed. For each result in the paper you can check what was predicted,
when, and whether it held. Two of the pre-registered hypotheses were refuted;
those commits are still here, in order, with the refutations that followed
them.

A rewritten history would be a better-looking repository and a worse
scientific record. If a claim in the paper is marked *pre-registered*, `git
log` is where you check it.

---

## Citing

```bibtex
@misc{sethuraman-gct,
  author = {Swami Sethuraman},
  title  = {Conductors of orbit closures, and the fundamental invariant
            of the $3\times 3$ determinant},
  year   = {2026},
  note   = {arXiv preprint}
}
```

## License

Code is MIT. Data and prose (results records, paper sources, documentation)
are CC BY 4.0. See `LICENSE`.

## Acknowledgement

The work reported here was carried out jointly with Claude (Anthropic), whose
contribution was that of a co-author. Responsibility for the correctness of
every statement rests with the named author.
