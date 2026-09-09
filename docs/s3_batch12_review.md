# Batch-12 S3 — integrator review

## 1. What it delivered

**The operator exists, is proved, and passed its dimension control.**  Five
things, in order of what they change:

1. **A sharper identity than `P_K τ P_K`.**  On the K-invariant precursor,

       I + (d − 1) T  =  d · P_{H_d}|_{W_d}

   so `ker(T − I) = V^H` exactly, `(T − I)((d−1)T + I) = 0`, and the only
   characteristic-zero eigenvalues are `1` and `−1/(d−1)` with multiplicities
   `a` and `B − a`.  At the goal cell that predicts spectrum `1^274`,
   `(−1/23)^1894` — conditional on the inherited dimensions.  This is cleaner
   than the operator my brief asked for and it makes the fixed-space equivalence
   an identity rather than an argument.
2. **The recurrence is implementable and local.**  All recoupling is an
   eight-box seminormal calculation; the residual is `R_λ = (F_big − I)J` with
   `J` built only from stored predecessor bases, and `U_λ = Nullspace(R_λ)`.
   **No unknown global Littlewood–Richardson coefficient is needed.**  The local
   tables are at most `8! = 40,320` states regardless of `N`.
3. **The `31 → 2` control, certified at both primes.**  A `239 × 31` residual of
   rank 29 with a displayed two-column kernel.
4. **`C₁₂ = 239` reproduced by a genuinely different engine** — representation
   recursion rather than Weyl alternation — term by term across all 23
   endpoints.
5. **The remaining gap named to four scalars.**  §7 specifies the conversion
   completely: `A_{αi} = g_{t_c}[e_{t_c}]ρ(π_i^{-1})v_α`, `C = G_M^{-1}A`,
   `ev_recursive = (Cᵗ)^{-1} ev_circuit`, with both permutations, the Gram, and
   the global norm `g_{t_c}` supplied.  What is missing is computing four
   arbitrary-permutation matrix coefficients from the compact DAG without
   expanding the ambient Specht basis.

It did **not** build a 274-vector source, evaluate the recursive basis, or
produce any target rank.  It says so throughout.

## 2. Verified here

- **The `31 → 2` control reproduces.**  My own elimination on S3's stored `R`
  gives rank 29 at both primes, kernel dimension 2, `R·U = 0` exactly, `rank U = 2`,
  free columns `[25, 26]` — matching every recorded value.
- **`F² = I`** on the worked `d = 12` block, in exact rationals, trace 1.
- **`C_total = 950`, `C_peak = 203`** from the weighted layer totals, and 948
  excluding the root — all three consistent.
- **`C₂₄ ≥ 4062` re-derived.**  The argument is right: only `(d)`, `(d−1,1)`,
  `(d−2,2)`, `(d−2,1,1)` meet `Ind_{S_{d−2}}^{S_d} 1 = h_{d−2}h_1h_1`, with
  Kostka numbers 1, 2, 1, 1, giving `B = a + b`, `C = a + 2b + c + e ≥ 2B − a`,
  and `2·2168 − 274 = 4062`.

And one thing worth pointing out that S3 does not: **their residual is `239 × 31`**
— the row count *is* `C₁₂` and the column count *is* `B₁₂`.  The map
`R : W_δ → Z_δ` lands exactly in the recoupling space I introduced, so the two
descriptions are the same object reached from opposite directions.  That is the
strongest available check on both.

## 3. Where S3 corrects me

**The good-reduction lemma.**  I banked: `p > |λ| = 96` ⟹ `F_p[S_96]` semisimple
by Maschke ⟹ everything transfers.  S3 does it properly and says why mine is not
the right tool: the requirement is a **free `Z_(p)`-lattice, stable under `S_N`,
on which the averaging operators over `H_d`, `K_d`, `L_d` are idempotents over
`A`** — their orders `24^d d!`, `24^d (d−1)!`, `24^d (d−2)!` being units — so
images and kernels are direct summands of free modules, hence free, and
invariants commute with base change.

The conditions coincide (`p > N = 4d = |λ|`), so my rule "no prime below 97" is
sound and merely conservative at the control.  But S3 adds a hypothesis mine
does not contain and cannot supply:

> "provided the stored columns really are a basis of the K-invariant lattice
> modulo p"

which is not implied by semisimplicity and which S3 proves inductively through
the recursion.  **My lemma was necessary and not sufficient**, and the note is
amended to say so.

**The DAG node counts.**  921 and 7,656 are the counts *below the root*; with the
root they are 922 and 7,657.  The driver's own output line says "below the top";
my prose did not carry that.  Fixed.

## 4. `C₂₄`, honestly

My `≈ 1.7 × 10⁴` came from two one-level ratios and was labelled an estimate.
S3 is right that its loose upper bound validates nothing, and right to say "do
not extrapolate a one-level ratio."  What it now has is a **rigorous floor**:

    4062  ≤  C₂₄  ≤  2.24 × 10¹²

Calibrating that floor against the one `δ` where `C` is known exactly is
informative, though, and I record it as a second estimate rather than as
evidence: at `δ = 12`, `C₁₂ / (2B − a) = 239/60 = 3.98`, and the same ratio at
`δ = 24` gives `≈ 16,180`.  So two extrapolations by unrelated routes — a
one-level multiplicity ratio, and a representation-theoretic floor scaled by its
own slack — land within 5% of each other.  That is worth more than either alone
and still less than a measurement.  **Exact `C₂₄` stays OPEN**, and S3's partial
run is the honest datum: 123.7 s, 2,237 nodes, and **zero of the 42 requested
degree-22 endpoint multiplicities completed**.

## 5. Does anything go to s77?  Yes — this is the most valuable relay of the batch

s77's first task is the Pieri-to-circuit bridge.  **S3's §7 is that bridge,
reduced to four scalars with every input supplied**: the intertwiner `Φ`
normalized by `Φ(e_{t_c}) = q_λ`, the slot permutation `π_i` per filling, the
identification `u_i = P_H ρ(π_i) e_{t_c}` of the banked circuits, the house
polynomial `F_v(f) = (4!)^{12}⟨Φ(v), f̃^{⊗12}⟩`, the Gram, and `g_{t_c}` as an
explicit 69-digit integer.

Three things in it that s77 could not have known and would have cost it the night:

- **The naive route is unpriced, not impossible.**  `2^579` and `2^640` are
  *algorithmic upper bounds on support doubling*, not measured supports.  s77
  should not conclude the permutation route is dead, nor assume it is cheap.
- **The circular trap is named.**  "Merely solving for a basis transform from
  sampled values assumes that evaluator already exists and is circular here."
  s77's brief offers a sampling fallback; this says why that fallback cannot
  substitute for the bridge.
- **The alternative primitive**: an evaluator for `i_{λμ}(v_{μα})` on form
  tensors with controlled contraction width.  Either that, or the four
  coefficients.

There is a collision worth stating plainly: **the four coefficients are
simultaneously s75's missing control half and s77's bridge at the control cell.**
Same problem, two sessions.  Whichever reaches it first, the other consumes the
result — the relay rule.

## 6. Ledger

| claim | status |
|---|---|
| `I + (d−1)T = d·P_H|_W`, `ker(T−I) = V^H`, spectrum `{1, −1/(d−1)}` | PROVED (S3) |
| `R_λ = (F_big − I)J`, no global LR coefficient needed | PROVED / implemented (S3) |
| `31 → 2` at both primes | **CERTIFIED, re-derived here** (rank 29, `R·U = 0`) |
| `C₁₂ = 239` by an independent engine | **CERTIFIED**, and its residual is literally `239 × 31` |
| 42 target local swap blocks, `F² = I` | exact artefacts; the worked block re-checked here |
| good reduction at `p > 4d`, with the lattice-basis hypothesis | PROVED (S3); **supersedes my Maschke lemma**, which was necessary and not sufficient |
| DAG counts 922 / 7,657 including root | correction accepted, prose fixed |
| `4062 ≤ C₂₄ ≤ 2.24 × 10¹²` | PROVED (S3); exact `C₂₄` **OPEN** |
| my `C₂₄ ≈ 1.7 × 10⁴` | ESTIMATE, unrefuted, now corroborated to 5% by an unrelated route — still not a measurement |
| evaluation of the recursive basis; 274-vector source; any target rank | OPEN |
