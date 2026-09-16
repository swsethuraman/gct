# B18-10 review — the independent adversarial review

Review under review: `work/batch15_workers/B15-10/docs/b18_10_review.md`, 43 KB,
sections 0–8.

## Verdict

**ACCEPT in full.** I challenged one measurement; the challenge was wrong and the
measurement is right. See §2 — the defect is mine and it is recorded as such.

This is a strong review and it did the thing it was run to do: it reached every
substantive point independently, discharged a certificate the producer had only
measured, and it is the only document in the batch that separates "the theorem
survives" from "every use of it does not".

## 1. What I confirm

| Slot 10's finding | my check |
|---|---|
| `dim D45 = 50`, exact rank over `Q` at two points, stabiliser nullity 1 | agrees — my own Leibniz/`Fraction` implementation gives rank 50 and corank 30 at both certificate points |
| `dim R135 = 39`, exact | agrees — Jacobian rank of the `(linear, cubic) -> product` map is **39** |
| the report used the rank in the correct direction (lower bound) | agrees |
| Claim 2.3, that separation gives no sign for `D` | agrees, and it is the load-bearing one |
| `4^49` proved modulo refined Bézout; the pointer should be Fulton Ex. 8.4.6 / Thm 12.3 | agrees, and this closes the citation B18-01 could only reach through a secondary quotation |
| Claim 6.1 uses ordinary `g` where the ledger wants symmetric `s`; Claim 6.2's `U` is unclipped | agrees — and **B18-02 and B18-01 found both independently**, so three lineages converge on the same two relabels |
| the producer's `out/` pilot scripts do not exist in the tree | agrees, and that defect is mine |

**Three lineages now carry `dim D45 = 50`** — Slot 01, this seat, and Slot 10 — across
five points and two primes. It is the most solid result in the programme.

## 2. The measurement — I was wrong, Slot 10 was right

I challenged Slot 10's length sweep. **The challenge was mistaken and the sweep is
correct.** Recorded here in full, because a wrong challenge from this seat is more
dangerous than a wrong measurement from a slot.

**What I did.** I computed `dim R13L` — *all* quartics that factor as linear x cubic in
`L` variables, `L + C(L+2,3) - 1`, cubic in `L`. Against `dim D4L <= 16L - 30`, linear
in `L`, that gives a gap narrowing and reversing sign at `L = 7`. I then argued from
growth rates that no other answer was possible.

**What the argument actually needs.** The padding side is not all linear x cubic. It is

```
P_L = closure{ (z . per_3) o T  :  T in Hom(C^L, C^10) }
```

the nine permanent entries being linear forms in `L` variables (B17-03 Lemma 2). That is
parametrised by `Hom(C^L, C^10)`, so it is **linear in `L` with slope 10**, against the
determinant side's slope 16. The gap widens by 6 per length. No reversal.

`P_5 = R135` — and only at `L = 5` — because of B17-01-A's five-variable dominance:
`Hom(C^5, C^9)` has dimension 45 against `dim Sym^3(C^5) = 35`, so every five-variable
cubic *is* a 3x3 permanent of linear forms. At `L = 6` that fails, 54 < 56, and
`P_L` is strictly smaller than `R13L` from there on.

**I recomputed `dim P_L` myself**, Jacobian rank of that parametrisation at a random
integer `T`, and it reproduces Slot 10's column exactly:

| `L` | `dim P_L` (mine) | Slot 10 | `10L - 5` | `dim D4L` | gap |
|---:|---:|---:|---:|---:|---:|
| 5 | **39** | 39 | 45 | 50 | +11 |
| 6 | **55** | 55 | 55 | 66 | +11 |
| 7 | **65** | 65 | 65 | 82 | +17 |
| 8 | **75** | 75 | 75 | 98 | +23 |
| 9 | — | 85 | 85 | 114 | +29 |
| 10 | — | 95 | 95 | 130 | +35 |

From `L = 6` the gap is `6L - 25`: 11, 17, 23, 29, **35**. Exactly as the sweep said.

**So §5 is accepted in full**, and the rejection of v1's advice now rests on two
independent legs rather than one: Claim 2.3, and a length sweep showing the geometric
input singles out nothing.

**My defect, and it is the worst kind.** I took `R135 = {linear x cubic}` — B18-01's §2
definition, correct at `L = 5` — and carried it to every `L` without re-deriving it.
That the two coincide at `L = 5` is a *theorem* with a hypothesis that fails at `L = 6`,
and the hypothesis was in the tree. This is precisely the species of error I have
charged to others all batch: a quantity defined in one regime carried into another
without checking the regime. I then challenged a correct result on the strength of it,
and offered a growth-rate argument that felt decisive because I had the wrong object on
one side.

The process worked — the slot held its ground with a derivation rather than deferring to
the integrator, which is exactly what it should do. But it cost a round trip that a
minute of checking B17-01-A would have saved.

## 3. On the ruling itself

Slot 10's closing ruling is that where to look for `D > 0` remains open at every
length, and that "the programme's only cellwise separation evidence is at five rows."

Agreed, and worth putting beside what the batch has since produced. B18-01 found the 23
degree-five five-row cells, **all with `a = 1`** — the one regime where separation and a
positive gap are the same statement. B18-06 closed four of them and nominated nothing.
Nineteen are untested and a sweep is issued.

So "open at every length" and "the only cellwise evidence is at five rows" are both
right, and the second is where the cheap work is.

## 4. The gate criteria

G1–G7 in §7, with G3 — the direction of every rank — as the decisive one, and Slot 10
replaying one small rank per release itself. That is the correct design, and the offer
to replay is what makes it a gate rather than a checklist.

Nothing is released. Slots 03, 04 and 09 have no cell to take in any case, per B18-06.

Note for whoever reads the file: **§7 sits before §6 on disk**, disclosed by the slot.

## 5. What enters the index

| id | statement | status |
|---|---|---|
| `dim_r135_is_39` | `dim R135 = 39`, exact Jacobian rank, UFD upper bound checked | PROVED; recomputed here |
| `separation_gives_no_sign` | Separation of a point from a variety gives no sign for `D`. Every sentence turning the aggregate negativity claim into advice about where to look is withdrawn | PROVED |
| `bezout_route_overshoots` | In the four-variable control the refined-Bézout route overshoots the true degree by about fifteen orders of magnitude, so even the exact `deg P(D45)` would not rescue the bound. `deg P(D45)` is not "the" obstruction | MEASURED |
| `two_sufficient_conditions` | Forms (1) and (2) of §7.2 are two sufficient conditions; neither implies the other. They are not the same statement | PROVED |
| `padding_is_not_all_products` | The padding variety at length `L` is `P_L = closure{(z·per_3)∘T : T ∈ Hom(C^L,C^10)}`, of dimension `10L − 5` for `L >= 6` — **not** all linear × cubic. The two coincide only at `L = 5`, by B17-01-A's five-variable dominance, which fails at `L = 6` (`9L = 54 < 56 = dim Sym^3(C^6)`). The gap `dim D4L − dim P_L` is `6L − 25`, widening 11 → 35 over `L = 5…10`, so the geometric input singles out no length | PROVED; `dim P_L` recomputed independently here at `L = 5,6,7,8` |

## 6. Carry-forward

1. **Resolved: the integrator was wrong, the sweep is right.** Recorded as an
   integrator defect. Nothing is held.
2. Slot 12 may now transcribe §2a **from this review's own closing ledger**, in full.
3. The Fulton pointer is now pinned: Ex. 8.4.6 / Thm 12.3. B18-01's conditional entry
   can cite it, still flagged as verified against a secondary quotation only.
