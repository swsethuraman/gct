# Degree 30: scoping, not launching

Session 23, 2026-08-31.  Requested as a scoping document explicitly, because
launching before the packing question is settled repeats the week-3 disk
failure.  **Recommendation: do not launch anything at degree 30 with the
present engine.  Two changes are needed first, and only one of them is small.**

## Why the answer matters more than usual

`E(det_3) contains <18,24> = {0, 18, 24, 36, 42, 48, ...}` — every multiple of 6
from 18 up *except 30*.  So `30 in E` is not one question among many: it is the
**only** undetermined element of the whole invariant semigroup.  Either

    E = <18,24>          (S/6 = <3,4>,   gaps of S/6 = {1,2,5},  conductor 36)
    E = <18,24,30>       (S/6 = <3,4,5>, gaps of S/6 = {1,2},    conductor 24)

and by the normalisation corollary (`docs/degree24_extension.md`,
Remark `rem:notdivisor`) the answer names the exact conductor of
`C[Omega-bar]^{SL_9}` inside its normalisation `C[phi]`.  Also: every
two-generated numerical semigroup is symmetric, so the first alternative holds
if and only if `C[Omega-bar]^{SL_9}` is Gorenstein.  We know no reason for
Gorensteinness; it is the shape of the dichotomy, not evidence for either side.

## Why degree 30 is not the degree-24 computation again

Three things are worse, and they are independent.

**(a) The ambient space is 4-dimensional, not 1.**  Exact ambient census
(`analysis/wk4_s21_census.py`):

| delta | 18 | 21 | 24 | 27 | 30 |
|---|---|---|---|---|---|
| `dim C[Sym^3 C^9]^{SL_9}_delta` | 1 | 0 | 1 | 1 | 4 |

At `delta = 24` one-dimensionality made a zero as decisive as a nonzero.  At
`delta = 30` that collapse does not happen.  Nonvanishing is still cheap in
principle — one bracket monomial with `B(S)(det_3) != 0` proves `30 in E` —
but **vanishing requires the full 4-dimensional space**: one must exhibit a
basis of `C[Sym^3 C^9]^{SL_9}_30` (four bracket monomials whose images are
independent) and show all four evaluate to zero at `det_3`.  Independence of
four bracket monomials is itself a computation nobody in this programme has
done; it needs either a straightening/Plücker argument in the bracket algebra
or four independent evaluations at auxiliary points where the values are known
to be independent.

**(b) The state does not fit.**  A degree-30 bracket monomial is 30 letters over
`k = 10` brackets.  `engine/br2.c` packs 9 bits per *partially filled* bracket
into a `u64`, which caps the front at 7 brackets (63 bits).  Measured over
randomly generated 9-regular structures with a greedy front-minimising order,
**every ordering tried leaves at least 8 brackets partially filled at some
level**, and the best seen was 8; one trial reached 9.  So `>= 72` bits are
required.

**(c) The state count is ~300x the degree-24 peak.**  The refined proxy in
`analysis/wk4_s21_spec.py` — which uses the fact that each letter deposits
exactly one cell in each row and each column of the `3x3` grid, so the
per-bracket masks carry global margins `sum_b rowcount(b) = (L,L,L)` and
likewise for columns — predicted the two degree-24 peaks as `2.58e8` and
`5.36e8` against measured `258,319,584` and `535,918,500`.  It is, empirically,
essentially exact.  At degree 30 it gives:

| structure | front | proxy peak |
|---|---|---|
| best of the trials | 8 | `1.59e11` |
| second | 9 | `8.74e11` |

Against the degree-24 peak of `5.4e8`, that is **~300x**, i.e. about **3.8 TB
per level file** at 24 bytes a state, on a container with ~40 GB.

## The two changes, and what each costs

**Change 1 — a wider state.  Small, and worth doing anyway.**
Replace the `u64` key with `unsigned __int128` (or two `u64` words) and lift the
front cap from 7 to 14 brackets.  This is a mechanical edit to `br2.c`:
key type, the pack/unpack loops, and the hash `mix`.  Cost: memory per slot
goes from 24 to 32 bytes, so the table holds 3/4 as many states.  Half a day
including a full re-validation against the `delta = 18` gates
(`-877,879,296,000` and `+50,536,120,320`) and the two degree-24 values.
**This is necessary but nowhere near sufficient** — it addresses (b) and does
nothing about (c).

**Change 2 — a factoring.  This is the real work.**
The `delta = 20` grind solved exactly this problem by splitting one evaluation
into 36 checkpointed subproblems indexed by `(sigma_6, sigma_7)`.  The
analogue here is to fix part of one bracket's cell assignment and sum over the
cases.  Three candidates, in increasing cost and decreasing risk:

1. *Fix one bracket's row-partition.*  Choose a bracket `b` and fix which 3 of
   its 9 letters take each row: `9!/(3!)^3 = 1680` cases.  Bracket `b`'s state
   then collapses from `C(9,d)` to `prod_r C(3, n_r) <= 27`, removing roughly a
   factor of 126 from the front at the peak — but multiplying the run count by
   1680.  Net: ~1680 runs of ~`1.3e9` states each.  Too many runs.
2. *Fix one bracket's full bijection.*  `9! = 362880` cases, each cheap.  Far
   too many runs, but it is the cleanest to implement and the cases are
   embarrassingly parallel; on a machine with real parallelism this is the
   obvious route.
3. *Meet in the middle on a cut.*  Split the 30 letters into two halves,
   enumerate the level-15 states of each half, and join on the shared masks.
   This is what the streamed DP already does implicitly; the gain would come
   from sharding the join by a hash of the shared state, which bounds memory
   without multiplying work.  This is the right shape, and it is the one that
   needs design rather than typing.

There is also a **fourth option that avoids the engine entirely** and should be
tried first, because it is cheap: the `U`-restriction trick that made degree 24
affordable.  Restricting to the six permutation monomials, the even-only and
odd-only runs at degree 24 cost 114 s against the main run's 6255 s.  The
same restriction at degree 30 gives `Phi|_U = sum_a K_a P^a Q^{10-a}`, and the
even-only run is a much smaller DP (3 permutations per letter, tighter masks).
**If any degree-30 bracket monomial has a nonzero even-only value, that alone
does not prove `30 in E`** — it certifies `c_S != 0` for that monomial, not
that the monomial is nonzero *at det_3*.  But it is the cheap first probe, and
at degree 24 it was the step that made the main run decisive.

## Recommended order of work

1. Widen `br2.c` to a 128-bit key; re-validate against all four banked values.
   (Necessary for anything at degree 30, and cheap.)
2. Run the even-only probe at degree 30 on two or three bracket structures, to
   learn the true state counts rather than the proxy's, and to find structures
   with `c_S != 0`.
3. Only then decide between factoring routes, with measured numbers in hand.
4. Treat the vanishing direction as a separate project: it needs a basis of the
   4-dimensional ambient space, and that question — independence of bracket
   monomials at `delta = 30` — should be settled on paper before any engine
   time is spent on it.

**Do not launch a full degree-30 evaluation until step 2 has produced measured
state counts.**  The proxy is reliable but it is a proxy, and 3.8 TB of
predicted level file is not a margin anyone should trust to a model.
