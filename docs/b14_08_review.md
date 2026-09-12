# Integrator review — B14-08

**Verdict: ACCEPT.** Its rebuilt census agrees with the banked one on all 239
records, its witness instrument checks out against my own raising operator, and
its own decision rule — applied with a floor it did not have — closes three of
the four LMR-reached targets rather than the one I had recorded.

Branch `b14-08-astra`, head `e504ddd9`, 4 commits over `9898e569`. Model
**gpt-6-astra**. sha256 on whole and `part00`, byte-identical, size 85058 and md5
as declared. Intake CLEAN. Pre-registration first.

## The rebuild came back clean

I told slot 8 to reconstruct all 717 target/source difference tests rather than
check the delivered table, because the delivered controls could not fail. It did,
importing neither the historical reachability script nor the house `a_weyl`
counter.

| | banked census | B14-08 rebuild |
|---|---|---|
| records | 239 | **239** |
| reach flags disagreeing | — | **0** |
| LMR-reached | 4 | **4** |
| reached at δ=25 / δ=26 | 5 / 26 | **5 / 26** |

Plus its own breakdown: 600 dominance failures, 51 exact ambient zeros, 66
positive pairs, 61 distinct witnesses. All 135 ten-row records unreached, with the
ninth/tenth-row argument checked rather than asserted.

## Its witness instrument works

I implemented the raising operator from its stated convention —
`E_ij c_α = (α_i + 1)·c_{α+e_i−e_j}` when `α_j > 0`, extended as a derivation —
and checked six sampled witnesses of the 61. Every one has the declared weight,
the declared degree, and is annihilated by **every** simple raising operator.

## Its decision rule closes three targets, and it said the floor was zero

Its Lemma T section states that the frozen inputs supply no positive certified
padded source floor, so the certified floor is zero for every record — true of
the base it worked from. `lmr_D_upper` certifies `p₂₄ = 3`. Its own rule is that a
determinant rank floor `k` with certified ambient `a` gives `U = a − k`, and
`U ≤ L` excludes `D > 0`:

| target | `a` | `a_∞` | stable | det floor | `U` | `L` | verdict |
|---|---:|---:|---|---:|---:|---:|---|
| `(69,17,2⁷)₂₅` | 274 | 274 | yes | 273 | 1 | 3 | **`D ≤ −2`** |
| `(73,17,2⁷)₂₆` | 274 | 274 | yes | 273 | 1 | 3 | **`D ≤ −2`** |
| `(71,19,2⁷)₂₆` | 392 | 392 | yes | 390 | 2 | 3 | **`D ≤ −1`** |
| `(69,21,2⁷)₂₆` | 531 | 533 | **no** | — | — | 3 | **OPEN** |

Each `a` is B14-08's own, and each equals the `a_∞` I reproduced from my own
derivation reviewing B14-04 — which is what makes the first three stable and lets
B14-06's stable-tail floors transfer. The multiplier weights are B14-08's too:
`u`, `u²`, `q62`, `q44`.

So the entry I recorded yesterday covered one target when the same argument
reaches three. Generalised to `b13_06_lmr_targets_closed`.

Its own synthetic exclusion cases test exactly this logic and **reject** both
insufficient bounds and product-image bounds, so the rule is validated
independently of the arithmetic I ran through it.

## Two distinctions it holds that this programme has previously collapsed

- **The maximum over reached sources, not the sum.** "Independent source images
  may overlap, so their dimensions cannot simply be added." Right, and easy to get
  wrong.
- **The tensor-domain multiplicity bounds the image of the LMR-generated product
  subspace and is not an upper bound on the whole determinant ideal.** That is the
  exact shape of error that would manufacture a false exclusion.

## The scalar-tail birth bound is a real contribution

A **proved** coarse integer upper bound on every one of the 239 ambient birth
increments: `M_ν/(u·M_pred)` injects into `(A/uA)_ν`, because every raising
operator kills `u` and `A` is a domain, so the increment is at most the count of
degree-`d` monomials of scalar tail weight `s` with no `u` factor. Four exact
increments were inherited; the other 235 stay OPEN **with certified bounds**
rather than blank. Funding 235 large ambient recounts was correctly out of scope.

## Defects

**`PROVED.md` section collision, fourth instance.** B14-08 also claimed F.
Resolved to I, after F, G and H. Every remaining Astra slot will do the same;
that is integration's job.

Its own note is fair: the scratch manifest's "4 of 30, 23 of 205 settled by
Lemma T alone" is too strong in its historical table, and "Lemma T exclusions" in
my packet text cannot promise exclusions without **both** kinds of ideal bound.
The packet also supplied too few ambient counts for exact Lemma B increments at
every row — hence the coarse bounds, which is the right response.

Its resolved packaging issue — Windows text-mode CRLF leaving a carriage return
in Git's alternates object path, fixed by writing bytes with literal LF — is
reported with both delivery-checker runs having already passed. Third Astra
session to hit a Windows encoding problem in packaging and the third to report it
cleanly.
