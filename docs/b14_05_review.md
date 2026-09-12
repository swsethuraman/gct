# Integrator review — B14-05

**Verdict: ACCEPT.** It refutes a board request I wrote, with a counterexample I
reproduced from my own code, and it independently proves the step the `D ≤ −2`
result had been leaning on my own argument for.

Branch `b14-05-astra`, head `54584452`, 5 commits over `9898e569`. Model
**gpt-6-astra**. sha256 on whole and `part00`, byte-identical, size 54125 and md5
as declared. Intake CLEAN. Pre-registration first.

## The counterexample, reproduced here

I wrote the column-bracket sum from the definition — independent per-column index
permutations, sign, letter symbols `α!·c_α` — and computed:

| | result |
|---|---|
| `F_T` and `F_U` at six random coefficient vectors | **both `576·H²`**, `H = 8c₀c₂ − 3c₁²` |
| `F_T′` at `f = s₁⁴ + s₁s₂³` | **0** |
| `F_U′` at the same `f` | **497664** |
| their hand derivation `6²·24³` | **497664** |

Equal source polynomials, unequal images. **The identity `F_{T′} = Φ_ν(F_T)` that
board slot 5 asked to be PROVED is false**, and the board asked for it
unqualified. That is my defect. The session delivered exactly the substantive
fallback the board's own text allowed for — an exact obstruction rather than an
absence of evidence.

Two observations in it are worth more than the refutation. Both images remain
genuine highest-weight members, so **a highest-weight check cannot detect the
failure**. And the space is two-dimensional at both ends — I verified the
multiplicities, `5 − 3 = 2` at `(d,b) = (4,4)` and `8 − 6 = 2` at `(5,6)` — so a
one-dimensional test cannot either, and no scalar normalisation repairs it. That
is the board's own warning about one-dimensional validation turned back on the
board's own request.

**The correction checks out.** Their general `Ψ_k` reduces at `n = 4, k = 2` to
the stated `F·c₂ − (3/8)(DF)·c₁ + (3/28)(D²F)·c₀`; those coefficients satisfy the
raising recurrence `a_{i+1}(i+1)(m−i) + a_i(n−k+1+i) = 0` with `a₀ = 1`; and
`(n−k)!·k! = 4`, as the averaging identity needs.

## `transport_lemma_T` proves what my `D` chain argued for itself

`lmr_D_upper` step (6) needs three independent equations at rung 13 to remain
three after multiplication by `msym_u¹¹`. I argued that from injectivity in an
integral domain. Lemma T states it as an indexed result:

> multiplying an actual ideal subspace of dimension `p` carries all `p`
> directions injectively, not just a selected number of them

with ideal preservation and **no** nonvanishing-modulo-`I` hypothesis. Its §1
also records `P_r ⊆ R_r` as a geometric fact about the two closures — both are
irreducible closures of polynomial images — rather than a sampled containment,
which is step (7).

B14-05 derived all of this without knowing the chain existed. Its own §6 states
only the weaker `i_red(13) ≥ 1 ⟹ D ≤ 0`, because it had no certificate in hand
and correctly refused to assume one. `lmr_D_upper` now cites the lemma.

Its Lemma T is also careful where it matters: the quotient injection needs a
regular residue, and it gives the counterexample for why a nonzero residue alone
is insufficient — multiplication by `x` in `ℚ[x,y]/(xy)` kills `y`. The two ideal
injections need no such hypothesis, and those are the ones my chain uses.

## Conventions worth carrying

`u = c₍ₙ,₀,…,₀₎` and `msym_u = n!·u` are **distinct conventions**, and a stored
matrix must say which it used. My chain is unaffected — both are nonzero, so
either is injective — but the entry now says which. Similarly: the banked native
row born at `t` becomes a degree-`d` row as `F_native·(24u)^{d−t}`, and a
transported certificate must carry its points and `u`-values.

Its point audit recomputed `u` for all 116 `P13` and all 212 `P14` points from
explicit exponent tuples, all nonzero at both primes. That corroborates B14-01's
and B14-02's independent `u`-checks on the same files.

## Two statements of Lemma CI now sit in the index

B14-03's `complete_interpolation_kernel` and B14-05's `complete_interpolation`.
That is corroboration, not redundancy: two sessions proved the same lemma from
different directions and agree on the hypotheses that matter — the dimension
sandwich (`dim N ≤ h` suffices, the minor supplies the reverse) and the
source-completeness requirement (an incomplete source gives a subspace kernel,
not an ideal multiplicity). Both are the conditions `lmr_D_upper` names.

## Defects

**PROVED.md section collision, third instance.** B14-03 took F, B14-04 G, B14-05
also claimed F. Resolved to H. Slots 08, 10 and 11 will do the same.

**Manifest `bundle_prerequisites` garbled**, same as B14-04: the base commit's
*subject line* captured alongside the hash. Second session with this; it is a
shared packaging habit, not an isolated slip.

Its own reported packaging failure — a `git show` decode under Windows cp1252,
fixed by requesting UTF-8, with the first attempt's log retained — is the right
way to report a non-mathematical stumble.

## Open, correctly

No degree-13/14 target minor, no LMR source matrix, no CI certificate, and the
non-Cartan coupled operators remain unimplemented. The report says first-row
validation at dimension six does not validate any other strip, and refuses to
estimate the higher-rank runtime from it. All correct.
