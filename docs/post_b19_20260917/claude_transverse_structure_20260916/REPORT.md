# Transverse compatibility at a quadratic-square skew pencil: local representation theory, a selection rule, and what transfers from six to five variables

Claude session, started 16 September 2026 (finished 17 September 2026). Fresh directory
`work/claude_transverse_structure_20260916/` (did not exist at session start; created by this
session). Every historical file, the sealed consolidated packet, the addendum of the active
sparse-evaluator session, and all shared ledgers are read-only here. Written incrementally: §0–§3
were written before any check ran; the status line is replaced at the end.

Status: **COMPLETE** (the §0 verdict stands; final numbers and the three-tier separation are in §3a–§11; the closing status line is at the end).

## 0. Opening verdict (written before computation; confirmed or amended in §9)

The question is: which cells can support new transverse compatibility constraints at a skew
determinant pencil `K` with `det K = u^2`, beyond what the determinant-stabilizer symmetry already
forces? The answer developed here is a **counting rule**, proved for rectangular cells
`lambda = (4k)^r`, `r in {5, 6}`, from two independent local computations:

- **Source side.** For any `z` in the full-stabilizer source `M_lambda`, the Taylor jets of `z` at
  `K` in every direction are determined by the jets along one *normal space* `N` of the
  `SL_r x H`-orbit of `K`, and the order-`m` normal jet is an element of
  `Sym^m(N^*)^{Stab(K)}`. `N` is an irreducible module of `Stab(K)^0`: for `r = 6` it is
  `S_(3,1) C^4` (dimension 45, not self-dual, `Stab^0 = SL_4`); for `r = 5` it is the `Sp_4`-module
  of highest weight `2 omega_1 + omega_2` (dimension 35, orthogonal, `Stab^0 = Sp_4`).
  Everything else — odd orders in symmetric directions, jets along orbit directions, and the
  order-two jet when `r = 6` — is **forced on every source invariant** and carries no test.
- **Target side.** For an extendable `z = F o phi`, the same jets are the derivatives of `F` at the
  quartic `u^2`, which is fixed by `SO_r`; through order four these derivatives carry exactly one
  free parameter (`kappa_F`, the `H_4`-component of the Hessian) beyond the value `F(u^2)`.
- **Rule.** The number of linearly independent, globally necessary transverse conditions of order
  at most `2m` at `K` is at most `1 + sum_{j<=m} dim Sym^{2j}(N^*)^{Stab} - (target parameters
  through order 2m)`, and a condition of order `2j` exists only if `Sym^{2j}(N^*)^{Stab} != 0`.
  This predicts, before any carrier is built, (i) the six-row silence at order two and the
  existence of at most `j_4(6) - 1` order-four conditions, one of which is the verified
  `J2 - 108 J1 + 14 z(K)`; (ii) that in five variables a **single** order-two condition exists
  (because `N_5` is orthogonal), that it is the verified `C2`, and that **every other order-two
  direction is redundant with it** (a theorem, §6.3); (iii) the number of further order-four
  five-row conditions is `j_4(5) - 1`, computed in §5.
- What the rule cannot do: it bounds the number of conditions from above and locates the orders
  where they can live; a lower bound (a condition that is actually nonzero on the source) always
  needs one explicit source vector, and independence from the old arc `C` always needs either an
  exact arc-kernel vector or a rank-four arc certificate (§7). No positive gap is claimed, and
  none is possible in any cell touched (§8).

**Confirmation after the two checks (added at the end; the text above is the pre-computation
verdict, unchanged).** Check 1 measured `dim N_6 = 45`, `dim N_5 = 35`, `j_2(6) = 0`,
`j_4(6) = 2`, `j_2(5) = 1`, `j_4(5) = 5` (all controls passing), so: six variables carry
exactly one E-free condition through order four (the known one) and five variables carry one
order-two condition (`C2`, unique in all directions) plus at most four further E-free
order-four conditions. Check 2 verified the target-side constants in both variable counts
(`108`, `-14`, `kappa~ = 3/896` in six; a single `kappa~ = 1/224` across five directions in
five) and produced explicit integer order-four five-row conditions that vanish exactly on the
ambient line. What remains unproved is Tier C (§3a): whether those conditions are nonzero and
distinct from `C2` on the source, and whether anything acts on `ker C`; §9 gives the one test.

## 1. Provenance, session state, and what is read-only

Workspace `C:/Users/swami/Projects/gct-gpt`. Process check at start (`tasklist`): no `python`
process running; live processes were editor/agent shells (`codex.exe`, `node.exe`). The active
sparse-evaluator session's directory `work/descent_followup_claude_20260916_addendum/` (last
written 21:23 local on 16 September; `FEASIBILITY.md`, `CORRIGENDUM.md`, `pilots/q1_price.*`)
is **not modified, not continued, and its planned Stage B is not run here**. Nothing in this
directory evaluates a full-`H` contraction of `M_(4^5)` at any point.

Inputs read (SHA-256, first 16 hex; full values in `MANIFEST.json`):

| file | sha256 (prefix) | used for |
|---|---|---|
| `Claude_Handover_B15_B18/CLAUDE_DESCENT_FOLLOWUP_20260916.md` | `acbe8a73bed00eee` | assignment, historical context only |
| `work/descent_followup_claude_20260916/REPORT.md` (sealed) | `80e90c1b31357c19` | six-row order-four replay (E11), five-row `C2` (E3–E6), certified partial results |
| `…_addendum/CORRIGENDUM.md` | `d0463d99ff0ff103` | corrections A–F, in particular C (no unchanged `k=1` transfer) and D (redundancy needs the whole kernel) |
| `…_addendum/FEASIBILITY.md` | `05602f27de97898d` | scope of the active session, to avoid overlap |
| `…/pilots/p3_c2_derivation.json` | `604b3967edbedb04` | five-row constants: `Delta^2 u^2 = 280`, `Delta^2 v = 48`, `H5` values |
| `…/pilots/p9_sixrow_replay.json` | `4ea8c234963a52aa` | six-row constants: `c = 1/6, 1/3`, `[t^4]/[t^0]` on `E`, `-12` |
| `work/extension_descent_20260916/REPORT.md` | `0d8c52f96a6c9b49` | row model, `Q`, `K`, `L`, interpolation theorem |
| `work/fiber_compatibility_20260916/REPORT.md` | `ecf2688aa46977377` | partial-transpose blindness, `Sp_4`/`SO_4` remarks |
| `work/batch15_workers/B15-01/docs/b19_01_report.md` | `aa136106c54eccaf` | arc weights (Prop. 3.1), silence theorem (4.1), Levi (6.1) |
| `work/batch15_workers/B15-02/analysis/b15_bound.py` | `ca001081f49e0048` | the inspected Job Object wrapper (read in full before use) |
| attachment `515d31fd…/pasted-text.txt` | `cd1177211fe4c5f2` | six-row order-four derivation (chat-only) |
| attachment `43761221…/pasted-text.txt` | `e9130c3865a34e15` | quadratic-square family, `SL_4`-decomposition `sl_4 + V_45` (chat-only) |

Labels used below: **PROVED** (argument written here), **VERIFIED** (re-derived here from the
inputs), **MEASURED** (computed here, receipts in `results/logs/`), **ADOPTED** (taken from a
reviewed input, location cited), **CONDITIONAL**, **OPEN**.

## 2. Scope, conventions, and rules adopted

Row model of the Astra/B18-02 reports: `W = Mat_4`, `H = Stab(det_4)` including transpose,
`H^0 = {(A, B) : det A det B = 1}` acting by `Y -> A Y B`; `M_lambda = (S_lambda W)^H` realised as
polynomials `z(Y_1, ..., Y_r)` of `GL_r`-highest weight `lambda`; `phi(Y) = det(sum x_i Y_i)`;
`A_{d,lambda}` = ambient highest-weight coefficient polynomials; `E_lambda = phi^* A_{d,lambda}`;
`m_det = dim E_lambda`. For `lambda = (4k)^r` (with `r` rows) every `z in M_lambda` is
`SL_r`-invariant and `F in A_{d,lambda}` satisfies `F(q o A) = det(A)^{4k} F(q)`, `d = rk`.
Coefficient degree `d`, matrix-entry degree `4d`. "Order" of a jet always means order in the
curve parameter `t` of `z(K + tS)`.

Rules: no agents; no changes to dependencies, sandbox, Git trust or ownership; nothing committed
or published; no census; no heavy computation. At most two numerical checks, each prepriced,
one process, one BLAS thread, `60 s / 512 MiB` under `b15_bound.py` (run from this directory so
its receipts land in `results/logs/`), interpreter
`work/batch15_workers/B15-02/.venv/python.exe` (Python 3.12.10, sympy 1.14.0). A failed check is
recorded, not retried.

## 3. Plan and prices (written before any check ran)

**Check 1 — character counts and the normal space (symbolic, priced).** Computes
`j_m(r) := dim Sym^m(N_r)^{Stab^0}` for `m = 2, 4, 6` and `r = 5, 6`, from torus weights (SSYT
enumeration for `S_(3,1) C^4`; `Sym^2 (x) Lambda^2_0` minus `10 + 5` for the `Sp_4` module), with
`Sym^m` characters by the Newton recursion on sparse weight dictionaries and the trivial
multiplicity by the Weyl alternant. Controls: `dim N_6 = 45`, `dim N_5 = 35`, `j_2(6) = 0`
(non-self-duality), `j_2(5) = 1` (orthogonal irreducible). Also verifies the orbit-tangent
dimension at `K5` and `K6` by the rank of `Lie(SL_r x H^0) -> T_K W^r` (a `(r^2-1+31) x 16r`
integer matrix) and that the symmetric normal part has dimension `35` resp. `45`.
ESTIMATE: at most `10^6` dictionary operations, `< 10 s`, `< 100 MiB`.

**Check 2 — five-variable order-four constants (symbolic, priced).** For `r = 5`, `k = 1`
(`d = 5`, covariance `det^4`): harmonic decomposition of `v(S) = [t^2] det(K5 + tS)` and
`w(S) = [t^4] det(K5 + tS)` for three directions `S = ell(x) I_4`; the covariance constants of
`d^2 F_{u^2}` on `u H_2` and `u^2` derived from `F(u_Q^2) = F(u^2) (det Q / det Q_0)^2`; the
resulting universal quartic `A_5(S)` and pairing `N(h_4(S))`; the explicit E-free condition
`C4` by elimination of `kappa` between two directions; and the control that `C4` vanishes
**exactly** on the ambient line `H5 o phi` (values of `H5` at `K5 + tS`, `t = 0, 1, 2`,
independently recomputed with the same five-row alternant as the sealed `p3`). A third direction
gives a second, independent elimination as a second control. ESTIMATE: sympy on quartics in five
variables plus five `H5` evaluations per direction, `< 20 s`, `< 200 MiB`.

Neither check evaluates any full-`H` source contraction; neither overlaps the active sparse
session. If either check fails its cap, it is reported as failed and the corresponding statement
is downgraded to CONDITIONAL.

## 3a. How to read this report: three tiers

Everything below is one of three kinds of statement, and the ledger in §10 tags each claim:

- **Tier A — character counts.** Dimensions of local invariant spaces (`dim N`, `j_m(r)`,
  `Sym^2(H_4)^{inv}`, LR multiplicities). Exact, MEASURED in Check 1. They are *room*: upper
  bounds on how many jet data a source vector can have. They are not statements about
  `M_lambda`.
- **Tier B — globally necessary jet identities.** Linear relations satisfied by every
  `z in M_lambda` (forced by the stabilizer; §4) or by every `z in E_lambda` (forced by
  covariance; §5), with their constants. PROVED, and VERIFIED numerically where an exact control
  existed (the `H5` and `H6` lines). These are valid without any carrier.
- **Tier C — realisation and independence.** Whether a Tier-B condition is nonzero on the
  source, whether two of them are distinct on the source, and whether they act on `ker C`.
  UNPROVED here except where the sealed packet certifies it (`C2 != 0` on `M_(4^5)`; `C_2(Q^2) =
  -12` on `M_(4^6)`). Deciding Tier C needs source vectors; §9 designs the test and does not run it.

## 4. Source side: what the stabilizer of `K` forces on every full-`H` invariant

### 4.1 Base points and stabilizers

`K6` is the generic skew pencil of `extension_descent §3` (six variables, `det K6 = u_6^2`,
`u_6 = x1 x6 - x2 x5 + x3 x4`, the Pfaffian); `K5` is the assignment's five-variable pencil
(`det K5 = u_5^2`, `u_5 = x1^2 - x2 x5 + x3 x4`). In both cases the tuple `K = (Y_1..Y_r)` consists of
skew matrices, `span(Y_i)` is all of `Lambda^2 C^4` (`r = 6`) or the hyperplane `omega^perp`
for the nondegenerate form `omega = E12 - E21 - E34 + E43` (`r = 5`; the pencil repeats `x1` at
positions `(1,2)` and `(3,4)`), and `u = Pf|_span`, nondegenerate in both cases
(`det Q_0 = 1/16` for `r = 5`, MEASURED in Check 2).

Let `Gamma := SL_r x H^0`. Every `z in M_(4k)^r` is `Gamma`-invariant (its `GL_r`-weight is
`det^{4k}`), homogeneous of matrix-entry degree `4d = 4rk`, and satisfies `z(-Y^T) = z(Y)`.

**Lemma 4.1 (stabilizer; PROVED, dimensions MEASURED — Tier A/B).** `Stab_Gamma(K)^0 =
{(A, cA^T, g_A) : A in G_r, c^2 det A = 1}` with `G_6 = GL_4`, `G_5 = GSp_4(omega)`, and
`g_A in SL_r` the inverse of the action induced on `span(Y_i)`. Its image in `GL(T_K)` is
`SL_4/mu_2 = SO_6` (`r = 6`) resp. `Sp_4/mu_2 = SO_5` (`r = 5`), acting on `C^r = span(Y_i)`
through `Lambda^2` and preserving `u` up to the scalar `det A`.
*Proof.* `A Y B` is skew for every `Y` in the span iff `Y D = D^T Y` for all such `Y`, where
`D = B A^{-T}`; the solution space is `C.I` (for `r = 5` MEASURED in Check 1,
`A_K5_commutant_dimension = 1`; for `r = 6` it is the classical statement for all of
`Lambda^2`). So `B = cA^T`, and `Y -> cAYA^T` acts on `Lambda^2` by `c Lambda^2 A`, which
preserves `omega^perp` iff `A` preserves the line `[omega]`, i.e. `A in GSp_4(omega)`. The
`SL_r` component is forced. Dimensions `16` and `11` give orbit dimensions `66 - 16 = 50` and
`55 - 11 = 44`, which Check 1 confirms directly. `Lambda^2 : SL_4 -> SO(Pf)` is the standard
isogeny; restricted to `Sp_4` it lands in `SO(omega^perp)`. ∎

The element `tau' : Y -> -Y^T` fixes `K` (`K^T = -K`), preserves every `z`, acts on symmetric
tangent directions by `-1` and on skew ones by `+1`.

**Lemma 4.2 (tangent decomposition; MEASURED exactly, Check 1 Part A — Tier A).**
`T_K W^r = T_orb (+) C.K (+) N`, where `T_orb = Lie(Gamma).K` has dimension `50` (`r = 6`) resp.
`44` (`r = 5`), the radial line `C.K` is not in `T_orb`, **every skew direction lies in
`T_orb + C.K`**, and `N` is the unique `Stab^0`-stable complement, contained in the symmetric
directions `V_sym = Sym^2 C^4 (x) C^r`:

| `r` | `dim T` | `dim T_orb` | `dim(T_orb + C.K)` | `dim V_sym` | `dim(V_sym ∩ (T_orb + C.K))` | `dim N` | `N` as `Stab^0`-module |
|---|---|---|---|---|---|---|---|
| 6 | 96 | 50 | 51 | 60 | 15 | **45** | `S_(3,1) C^4` (`V_sym = 45 + 15`, LR multiplicities `1, 1`; not self-dual: `S_(3,1)^* = S_(3,3,2)`) |
| 5 | 80 | 44 | 45 | 50 | 15 | **35** | `V(2 omega_1 + omega_2)` of `Sp_4` (`V_sym = 35 + 10 + 5`, multiplicities `1, 1, 1`; orthogonal) |

The identification of `N` uses only that `V_sym` is multiplicity-free with a unique
15-dimensional submodule (`15 = S_(2,1,1)`, resp. `10 + 5`). `tau'` acts on `N` by `-1`.

**Lemma 4.3 (formal slice; PROVED — Tier B).** For every `S in T` there are formal curves
`gamma(t) in Gamma`, `c(t) in 1 + t C[[t]]`, `n(t) in t N[[t]]` with
`K + tS = c(t) . gamma(t) . (K + n(t))`, and `n(t) = t S_N + O(t^2)` with `S_N` the
`N`-component of `S`. *Proof.* The map `(gamma, c, n) -> c gamma (K + n)` has differential
`Lie(Gamma) (+) C (+) N -> T_orb + C.K + N = T` at `(e, 1, 0)`, surjective by Lemma 4.2; apply
the formal inverse function theorem to lift the curve `K + tS`. ∎

**Theorem 4.4 (automatic jets; PROVED — Tier B).** For `z in M_(4k)^r` let `f_z(n) := z(K + n)`,
a `Stab(K)`-invariant polynomial on `N`. Write `f_z = z(K) + Phi_2(z) + Phi_3(z) + ...` with
`Phi_m(z) in Sym^m(N^*)^{Stab^0}`. Then `Phi_odd(z) = 0` (by `tau'`), and for every `S in T`

    z(K + tS) = c(t)^{4d} . f_z(n(t)).

Consequently every Taylor coefficient of `z(K + tS)`, in every direction, is a linear function
of the **transverse jet data** `(z(K), Phi_2(z), Phi_4(z), ...)` with coefficients that depend
only on `S`, `r`, `k` (through `c(t)`, `n(t)`), not on `z`. In particular:

- `[t^2] z(K + tS) = z(K) alpha_2(S) + Phi_2(z)(S_N, S_N)`;
- `[t^4] z(K + tS) = z(K) alpha_4(S) + Phi_2(z)(S_N, n_3(S)) + Phi_2(z)(n_2(S), n_2(S)) + Phi_4(z)(S_N^4)`,
  where `n_2, n_3` are the higher coefficients of `n(t)` (universal);
- jets in skew (orbit) directions and mixed jets carry nothing beyond the same data.

*Proof.* `z` is `Gamma`-invariant and homogeneous, so `z(c gamma Y) = c^{4d} z(Y)`; insert Lemma
4.3. `f_z` is `Stab`-invariant because `Stab` preserves `K + N`. `tau'` acts on `N` by `-1` and
fixes `z`, so the odd parts vanish. ∎

**Corollary 4.5 (the counts; MEASURED, Check 1 Part B, all controls passing — Tier A).**
`j_m(r) := dim Sym^m(N_r)^{Stab^0}`:

| `r` | `j_2` | `j_4` | `j_6` | `j_8` | reason for `j_2` |
|---|---|---|---|---|---|
| 6 | **0** | **2** | 6 | not computed | `N_6` irreducible and not self-dual: no invariant bilinear form at all (`Lambda^2` invariants also `0`) |
| 5 | **1** | **5** | 24 | 127 | `N_5` irreducible and orthogonal (`Sym^2` invariant `1`, `Lambda^2` invariant `0`) |

Controls: `Sym^2(sl_4)^{SL_4} = 1`, `Sym^2(C^4)^{SL_4} = 0`, `Sym^2(C^4)^{Sp_4} = 0`,
`Sym^2(5)^{Sp_4} = 1`, `Sym^2(10)^{Sp_4} = 1`, `dim H_4(C^6) = 105 = S_(4,4)C^4`,
`dim H_4(C^5) = 55`, `Sym^2(H_4)^{inv} = 1` in both cases. The finite parts of `Stab` (`tau'`,
the centre `mu_4`, the sign `c = -1`) act trivially on `Sym^{even}(N^*)`, so these are the
counts for the full stabilizer.

**Corollary 4.6 (what is forced on every source invariant — Tier B).** For `z in M_(4k)^r` and
symmetric `S`:

1. `z(K + tS)` is even in `t` (all `r`); for `S = ell(x) M` (a rank-one tuple update) it has
   degree `<= 4k` because `z` has degree `4k` in the Plücker coordinates of `span(Y_i)` and
   the wedge changes linearly in `t` (`M ∧ M = 0`).
2. `r = 6`: `[t^2] z(K + tS) = z(K) alpha_2(S)` for **every** `z` and every symmetric `S`
   (`j_2(6) = 0`). This is the attachment's "order two is silent", now proved from Lemma 4.2:
   there is no order-two transverse datum at all in six variables.
3. `r = 5`: `[t^2] z(K + tS) = z(K) alpha_2(S) + beta_z B(S_N, S_N)` where `B` is the unique
   (up to scale) `Sp_4`-invariant quadratic form on `N_5` and `beta_z` is **one** scalar per
   `z`. So the order-two jets in all symmetric directions together span at most a
   two-dimensional space of functionals on `M_(4k)^5`, namely `span(z -> z(K), z -> beta_z)`.
4. Order four: `Phi_4(z)` lives in a space of dimension `2` (`r = 6`) resp. `5` (`r = 5`).
   The full order-`<= 4` jet data at `K` of a source vector lie in `J_{<=4} := C (+)
   Sym^2(N^*)^{inv} (+) Sym^4(N^*)^{inv}` of dimension **3** (`r = 6`) resp. **7** (`r = 5`).

None of this uses the ambient space, `a`, `m_det`, or any carrier.

### 4.7 Local versus global: precisely what the normal-space calculation constrains

The normal-space calculation produces two different things, and only the first is a
constraint on global source functions:

1. **Identities (Tier B).** For every global `z in M_lambda`, the map `j : z -> (z(K), Phi_2(z),
   Phi_4(z), ...)` exists and every Taylor coefficient of `z` at `K` in every direction is a
   *fixed* linear function of `j(z)` (Theorem 4.4). Hence any linear combination of Taylor
   coefficients that vanishes on `J` (for example every odd coefficient in a symmetric
   direction; every order-two coefficient when `r = 6`; the difference of two order-two
   coefficients in different directions scaled by `B(S_N)/B(S'_N)` when `r = 5`) vanishes on
   all of `M_lambda`. These are theorems about the global space because they are theorems
   about every polynomial that is `Gamma`-invariant and homogeneous, and every `z in
   M_(4k)^r` is one.
2. **Room (Tier A).** `J_{<=4}` is the space in which `j(M_lambda)` lives, not a description of
   it. An element of `Sym^m(N^*)^{Stab}` is a jet of a local `Stab`-invariant function on the
   slice; it need not be the jet of any global `Gamma`-invariant polynomial, and even when it
   is, that polynomial need not lie in the single graded piece `M_lambda` (degree `4d`, weight
   `det^{4k}`). Luna's étale slice theorem, where it applies (closed orbit — not checked for
   `K`), identifies the *completed* global invariant ring with the *completed* local one only
   in the direct limit over all degrees; inside one cell `j(M_lambda)` can be a proper
   subspace of `J_{<=4}`, and `dim j(M_lambda) <= min(s, dim J_{<=4})`. The rank of `j` on
   `M_lambda` is a global question (Tier C).

So: the counting rule of §6 bounds the number of transverse conditions from above and says at
which orders they can exist; it never asserts that a predicted condition is nonzero on the
source. The sealed packet supplies the only Tier-C facts used: `C2 != 0` on `M_(4^5)` and
`C_2(Q^2) = -12` on `M_(4^6)`.

## 5. Target side: what a genuine quartic-coefficient function must additionally satisfy

### 5.1 Derivatives at the quartic `u^2` (Tier B)

Let `F in A_{d,lambda}`, `lambda = (4k)^r`, so `F(q o A) = det(A)^{4k} F(q)` for `A in GL_r`. The
point `u^2 in Sym^4 C^r` is fixed by `SO(u)` and scaled by the conformal group. Hence
`d^j F_{u^2}` is an `SO_r`-invariant `j`-linear form on `Sym^4 C^r = H_4 (+) u H_2 (+) C u^2`
(harmonic decomposition; the three summands are pairwise non-isomorphic, irreducible and
self-dual, dimensions `105, 20, 1` for `r = 6` and `55, 14, 1` for `r = 5`).

- **Order one (jet order two).** `dF_{u^2}` is `SO_r`-invariant, so it factors through the
  `u^2`-component: `dF_{u^2}(q) = d . c(q) . F(u^2)`, `c(q) = Delta^2 q / Delta^2(u^2)`, with
  `Delta` the `Q_0^{-1}`-Laplacian (`Delta^2(u^2) = 2r(4r + 8) = 384, 280`). **No free
  parameter.** (VERIFIED; this is the sealed §C.2 and attachment 515d31fd §1.)
- **Order two (jet order four).** `d^2 F_{u^2} in Sym^2(Sym^4 C^r)^{*, SO_r}` is
  three-dimensional (`Sym^2(H_4)^{inv} = Sym^2(H_2)^{inv} = 1`, `Sym^2(u^2)`, no cross terms;
  MEASURED controls in Check 1). Covariance along the quadratic-square family fixes two of the
  three: for a quadratic `a` with matrix `Q_a` and `M := Q_0^{-1} Q_a`, expanding
  `F((u + eps a)^2) = F(u^2) det(I + eps M)^{2k}` gives

      dF_{u^2}(u a) = k tr(M) F(u^2),
      dF_{u^2}(a^2) + 2 d^2F_{u^2}(u a, u a) = k [2k tr(M)^2 - tr(M^2)] F(u^2),

  which by polarisation determines `d^2F_{u^2}` on `(u . Sym^2) x (u . Sym^2)`, i.e. on the
  `u H_2` and `u^2` summands and their cross term. The only free parameter is
  `kappa_F` with `d^2F_{u^2}(h, h') = 2 kappa_F N(h, h')` for `h, h' in H_4`, `N(h, h') :=
  h(Q_0^{-1} d) h'` the invariant pairing. **One free parameter through order four.** (PROVED;
  the six-variable specialisation is attachment 515d31fd §1, VERIFIED below.)

### 5.2 The universal quartic and the order-four jet on `E` (Tier B)

For a symmetric tuple `S`, `det(K + tS) = u^2 + t^2 v(S) + t^4 w(S)` (even in `t` by transposition;
`t`-support `{0, 2, 4}` MEASURED for all seven directions used). Decompose
`v = h_4 + u h_2 + c_v u^2` and put `a := h_2 + c_v u`, `M_a := Q_0^{-1} Q_a`. Then for
`z = F o phi`:

    [t^2] z(K + tS) = d . c_v(S) . z(K),
    [t^4] z(K + tS) = z(K) . A_{r,k}(S) + kappa~ . N(h_4(S), h_4(S)),      kappa~ = kappa_F / 2 ... (one scalar per F),
    A_{r,k}(S) = d c(w) + (1/4) [ k (2k tr(M_a)^2 - tr(M_a^2)) - d c(a^2) ],      d = rk.

(PROVED from §5.1 by the chain rule; `dF(w)` and `(1/2) d^2F(v, v)` split by Schur into the
`H_4` term and the `u`-multiple terms.) Both `A_{r,k}` and `N o h_4` are **universal**: they
depend on `(r, k, S)` only.

**Check 2 (MEASURED, 3.4 s, receipt `results/logs/c2_fivevar_order4_resources.json`).**

Six variables, `k = 1`, control against attachment 515d31fd and the sealed `p9`:

| direction | `c_v` | `A_{6,1}` | `N(h_4)` | `[t^4]/[t^0]` on `E` (sealed p9) | `kappa~` |
|---|---|---|---|---|---|
| `S1 = x1 I` | `1/6` | `3/20` | `96/5` | `3/14` | `3/896` |
| `S2 = (x1+x6) I` | `1/3` | `11/5` | `10368/5` | `64/7` | `3/896` |

`N(S2)/N(S1) = 108`, `A(S2) - 108 A(S1) = -14`, a **single** `kappa~ = 3/896` fits both sealed
values (the sealed E11 records the same `3/896`). The attachment's table is reproduced exactly
by an independent route (trace formulas instead of its `J(h_2)` bookkeeping). **VERIFIED.**

Five variables, `k = 1` (`d = 5`), five directions, with `H5` (the unique `(4^5)` invariant,
integral convention `T_alpha = alpha! c_alpha`) recomputed at `K5 + tS`, `t = 0..4`:

| direction | `c_v` | `A_{5,1}` | `N(h_4)` | `H5` polynomial support | `[t^2]/[t^0]` (= `5 c_v`?) | `[t^4]/[t^0]` | `kappa~` |
|---|---|---|---|---|---|---|---|
| `S1 = x1 I` | `6/35` | `89/441` | `5888/63` | `{0,2,4}` | `6/7` ✓ | `13/21` | `1/224` |
| `S2 = x2 I` | `8/35` | `32/147` | `320/21` | `{0,2,4}` | `8/7` ✓ | `2/7` | `1/224` |
| `S3 = (x1+x2) I` | `2/5` | `43/63` | `832/9` | `{0,2,4}` | `2` ✓ | `23/21` | `1/224` |
| `S4 = x1 diag(1,1,0,0)` | `3/35` | `-2/49` | `64/7` | `{0,2}` | `3/7` ✓ | `0` | `1/224` |
| `S5 = (x1+x3) I` | `2/5` | `43/63` | `832/9` | `{0,2,4}` | `2` ✓ | `23/21` | `1/224` |

`H5(K5) = 322560` (agrees with the sealed P3). All five `H5` restrictions are even quartics; the
three-point extraction of `[t^2]` and `[t^4]` agrees with the five-point interpolation; the
order-two ratio equals `5 c_v` in every direction (the target-side order-two statement is
direction-independent, as §5.1 says); and one `kappa~ = 1/224` fits all five directions —
**four independent consistency checks of `A_{5,1}` and `N`**, including a non-scalar
symmetric direction. **VERIFIED.**

### 5.3 The explicit E-free order-four five-row condition (`k = 1`) — Tier B

Eliminating `kappa~` between two directions `S, S'` (with `J_S(z) := [t^4] z(K5 + tS)
= (z(K5+2S) - 4 z(K5+S) + 3 z(K5))/12` for `k = 1`):

    C4_{S,S'}(z) := N(h_4(S')) [J_S(z) - z(K5) A(S)] - N(h_4(S)) [J_{S'}(z) - z(K5) A(S')].

In integer form on the value vector `(z(K5), z(K5+S), z(K5+2S), z(K5+S'), z(K5+2S'))`:

| pair | integer coefficients | value on the `H5` line |
|---|---|---|
| `(S1, S2)` | `(-27, -60, 15, 368, -92)` | `0` |
| `(S1, S3)` | `(3711, -2548, 637, 2576, -644)` | `0` |
| `(S1, S4)` | `(-2211, -252, 63, 2576, -644)` | `0` |
| `(S1, S5)` | identical to `(S1, S3)` (`x2 <-> x3` is a stabilizer symmetry of `K5`) | `0` |

Each `C4_{S,S'}` is **globally necessary** on `M_(4^5)` (it vanishes on `E` by construction, and
the vanishing on the ambient line is checked exactly). Whether any of them is nonzero on the
source, and whether it differs from `C2` there, is Tier C (§6.6): no full-`H` source vector was
evaluated (the certified `q_3, q_7` values exist only at `K5, K5+S1, K5+2S1`, sealed
`p7_arc_S0.json`).

### 5.4 Dependence on `k` (requirement 5) — Tier B, checked at `k = 1` only

For `lambda = (4k)^5`, `d = 5k`: the source-side structure of §4 (`N_5`, `j_m(5)`, Theorem 4.4)
is **independent of `k`**; the target-side constants are not:

- `[t^2] z(K5 + tS) = 5k c_v(S) z(K5)` on `E`; for `S = x1 I`, `c_v = 6/35`, so the order-two
  condition is `C2^{(k)}(z) = [t^2] z(K5 + t x1 I) - (6k/7) z(K5)` (the sealed `112, -7, -177`
  form is the `k = 1` three-node evaluation of this).
- `z(K5 + tS)` is even of degree `<= 4k` for rank-one updates `S = ell(x) M`, so `[t^2]` and
  `[t^4]` need `2k + 1` even nodes (`t = 0, 1, ..., 2k`), not three.
- `A_{5,k}` changes through `d = 5k` and the covariance exponent `2k` (formula in §5.2);
  `N o h_4` does not.
- The stopping rule "a nonzero `4 x 4` forbidden minor proves exactness" is specific to
  `s = 5`, `m_det = 1` at `k = 1`.

The `k >= 2` formulas are PROVED from §5.1–5.2 but have no numerical control here.

## 6. Comparison map, its position, and the selection rule

### 6.1 The two jet maps

Let `J_{<=4} := C (+) Sym^2(N^*)^{Stab} (+) Sym^4(N^*)^{Stab}` (dimension `3` for `r = 6`, `7` for
`r = 5`). The **source jet map** is `j : M_lambda -> J_{<=4}`, `z -> (z(K), Phi_2(z), Phi_4(z))`.
The **ambient jet map** is `j_A : A_{d,lambda} -> J_{<=4}`, `F -> j(F o phi)`; its image is

    L := { ( f,  f . beta_0,  f . A' + kappa . (N o h_4) ) : (f, kappa) = (F(u^2), kappa~_F) },

a subspace of the two-dimensional space `L_max` spanned by `(1, beta_0, A')` and
`(0, 0, N o h_4)`. Here `A'` and `beta_0` are the universal elements of `Sym^4(N^*)^{Stab}` and
`Sym^2(N^*)^{Stab}` obtained by rewriting §5.2 in the normal coordinates of §4 (for `r = 6`,
`beta_0 = 0` since `j_2 = 0`). `j(E) = j_A(A_{d,lambda}) = L`, and `E subset M_lambda`, so
`L subset j(M_lambda)`.

**What determines the position of `L` inside `J_{<=4}`** (requirement 2): (i) the universal
constants of the group geometry, `c(t)` and `n(t)` of Lemma 4.3, equivalently `alpha_2, alpha_4`
and the `Phi_2`-coefficients in Theorem 4.4 — these are functions of `S` only; (ii) the
`Stab`-equivariant quadratic map `h_4 : N -> H_4(C^r)` (the `H_4`-component of `v(S)`) and the
invariant pairing `N` on `H_4`; (iii) the universal quartic `A_{r,k}` and the scalar
`d c_v`, i.e. the covariance exponent `2k` and the degree `d`; (iv) the ambient data
`(F(u^2), kappa~_F)` for `F in A_{d,lambda}`, in particular the ratio `kappa~_H / H(u^2)` when
`a = 1` (`3/896` for `(6,(4^6))`, `1/224` for `(5,(4^5))` in the normalisations of Check 2).
Items (i)–(iii) are computable from `(r, k, S)` alone; only (iv) needs the ambient space, and
the **E-free** conditions do not need it at all.

### 6.2 The selection rule (Theorem — Tier B for (a),(b); Tier C enters only through `dim j(M)` in (c))

**Theorem 6.1 (PROVED).** Let `lambda = (4k)^r`, `r in {5, 6}`, `K` as above.

(a) Every globally necessary linear condition on `M_lambda` that is built from Taylor
coefficients of order `<= 4` of `z(K + tS)` at `K`, in any finite set of directions `S`
(symmetric or not) and without using knowledge of `A_{d,lambda}` beyond its covariance,
factors through `j` and vanishes on `L_max`. The space of such **E-free** conditions has
dimension at most `dim J_{<=4} - 2`, i.e. **`1` for `r = 6` and `5` for `r = 5`**.

(b) Conditions that also use the actual ambient image (a known `E`) are the annihilator of
`j(E) = L`: at most `dim J_{<=4} - dim L`, i.e. `2` for `r = 6` and `6` for `r = 5` when
`a = m_det = 1`.

(c) The **rank actually realised** on `M_lambda` by all order-`<= 4` conditions at `K` is
`dim j(M_lambda) - dim L` (with `L` replaced by `L_max` for E-free conditions), hence at most
`min(dim J_{<=4}, s) - m_det` in case (b). A condition of order `2m` can exist only if
`Sym^{2m}(N^*)^{Stab} != 0`.

*Proof.* (a), (b): Theorem 4.4 says every such Taylor coefficient is a fixed linear functional
on `J_{<=4}` composed with `j`; §5.2 says the image of `E` lies in `L subset L_max`; necessity
means vanishing on `E`. (c): rank of a family of functionals on `M_lambda` vanishing on a
subspace equals `dim j(M) - dim(j(M) ∩ L)` and `L subset j(M)`. ∎

### 6.3 Consequences, cell by cell

**Six variables, `(6k, (4k)^6)`.**

- Order two: **no condition exists** for any `z`, any direction (Cor. 4.6.2). The attachment's
  silence claim is a theorem. (Tier B, PROVED)
- Order four: `dim J_{<=4} = 3`, so there is **exactly one E-free condition** (up to scale),
  and it is the verified `C_2 = J_2 - 108 J_1 + 14 z(K)` (nonzero on `Q^2`, sealed E11,
  reproduced in Check 2). **No second pair of directions, no non-scalar symmetric direction,
  and no mixed jet can add an E-free condition of order `<= 4` at `K6`.** (Tier B, PROVED;
  nonzeroness Tier C, sealed)
- With `E` known (`a = 1`, `kappa~_H6 = 3/896`): at most **two** conditions, the second being
  e.g. `J_1(z) - (3/14) z(K)` (value `1/4 - 3/14 = 1/28 != 0` on `Q^2`); whether it is
  independent of `C_2` on `M_(4^6)` is the question whether `j(M_(4^6)) = J_{<=4}` (rank 3),
  which needs a third source vector with jet outside `span(j(H6 o phi), j(Q^2))`. (Tier C, OPEN)
- Hence **at least `9 - 2 = 7` of the nine false survivors of `(6,(4^6))` are invisible to every
  jet condition of order `<= 4` at `K6`**, whatever carrier is built. Detecting them needs order
  `>= 6` (`j_6(6) = 6`; the target-side count at order six is not derived here) or other base
  points (the two-pencil test `q(K) - 1120 q(L)` is a 0-jet at the second point `L`, whose
  stabilizer is much smaller and where far less is forced — its counting is OPEN).

**Five variables, `(5k, (4k)^5)`.**

- Order two: `dim J_{<=2} = 2`, `dim L_{<=2} = 1`, so there is **exactly one E-free order-two
  condition**, and it is `C2` (nonzero on the source at `k = 1`: sealed E6). **Theorem 6.2
  (redundancy of all other order-two directions; PROVED — Tier B).** For every symmetric tuple
  `S'`,

      [t^2] z(K5 + tS') - d c_v(S') z(K5)  =  ( B(S'_N, S'_N) / B(S_N, S_N) ) . C2^{S}(z)

  identically on `M_(4k)^5`, where `S = x1 I` and `B` is the invariant form on `N_5`; the ratio
  is computable from `S'` alone, and it is `0` exactly when `S'_N` is `B`-isotropic. (Cor. 4.6.3
  plus §5.1; `B(S_N, S_N) != 0` because `C2^{S} != 0` on the source.) So the active session's
  `C2` is *the* order-two transverse test at `K5`, in every direction and for every `k`.
- Order four: `dim J_{<=4} = 7`, `dim L_max = 2`: **up to five E-free conditions in total**, one
  of them `C2`, hence **up to four genuinely new order-four conditions** (`C4_{S,S'}` of §5.3
  are explicit members; five independent 4-jet directions are needed to realise all four, and
  the scalar-matrix family `ell(x) I` alone may not suffice — its 4-jet evaluations span an
  unknown part of `(Sym^4 N_5^*)^{inv, *}`; non-scalar directions such as `S4` should be
  included).
- Realised rank: at most `s - m_det = 4` at `k = 1`. Whether the order-`<= 4` transverse
  conditions at `K5` reach rank 4 on `M_(4^5)` is exactly the **missing lemma** of §9.

**Non-rectangular cells.** The proof of Theorem 6.1 uses `SL_r`-invariance of `z`. For general
`lambda` the source is only `U_r`-invariant and the stabilizer of `K` in the relevant group is
not reductive, so the counting must be replaced by a branching problem: source-side jets of
order `m` live in `Hom_{Stab^0}(V_lambda^*|_{Stab^0}, Sym^m(N^*))`, target-side in the
corresponding branching of `Sym^d(Sym^4)`-covariants restricted to `SO_r`. This is stated, not
proved (OPEN). All five-row cells with `d <= 5` are excluded anyway (`D <= 0`), so the first
non-rectangular candidates are at `d = 6`.

### 6.4 Can the mismatch predict constraints before a carrier is built? (requirement 3)

Yes for **upper bounds and for where to look**; no for **lower bounds**:

- The rule decides, from `(r, m)` alone, whether order `2m` has *room*: none at order two for
  six variables, one at order two for five variables, `j_4 - 1` E-free at order four. This is
  what makes five variables cheaper than six (§7).
- It bounds the total number of order-`<= 4` conditions at `K` (`1` E-free / `2` total for
  `r = 6`; `5` E-free / `6` total for `r = 5`), hence bounds what any carrier can deliver from
  this base point and jet order, e.g. the "at least seven invisible survivors" statement.
- It cannot certify that a predicted condition is nonzero on the source: `j` may fail to be
  surjective (§4.7). One explicit source vector with a nonzero value settles that (as `Q^2` did
  in six variables and `q_3, q_7` did for `C2`). That is a one-vector certificate, far cheaper
  than a complete carrier, and it is the first stage of the test in §9.

### 6.5 Joint elimination of the target-side parameters, and dependencies

Take `D` symmetric rank-one directions `S^(1), ..., S^(D)` at `k = 1`. The raw data per `z` are
`1 + 2D` numbers: `z(K5)` and, per direction, `[t^2]_i`, `[t^4]_i` (each from three points).
The target side has **two** unknowns per extendable `z`: `f = z(K5)` and `kappa~`. Eliminating
them jointly gives `2D - 1` E-free linear identities:

- `D` order-two identities `[t^2]_i = 5 c_v(S^(i)) f`;
- `D - 1` order-four identities `N_j ([t^4]_i - A_i f) = N_i ([t^4]_j - A_j f)` (the `C4`'s).

Dependencies among them **on the source** (Tier B, from Theorem 4.4 and Cor. 4.5):

1. The `D` order-two identities define **one** functional up to scale (Theorem 6.2): jointly
   they have rank `<= 1`, whatever `D`. Adding order-two directions never adds rank.
2. The order-four identities, together with `C2`, are functionals on `J_{<=4}` vanishing on
   `L_max`, a space of dimension `<= 5`; so `rank{C2, C4_{ij}} <= min(D, 5)` on the jet space,
   and `<= 4` on `M_(4^5)` (`E` is in every kernel). Hence at most **four** of the `D - 1`
   order-four identities can be independent, and adding directions beyond five is pointless.
3. Each `[t^4]_i` contains, by Theorem 4.4, the term `Phi_2(z)(S_N, n_3) + Phi_2(z)(n_2, n_2) =
   beta_z gamma_4(S^(i))`. So a `C4_{ij}` evaluated on a source vector mixes in the
   **order-two datum** `beta_z`. `C4_{ij}` is a new functional on the jet space exactly when its
   `Phi_4`-component, `Phi -> N_j Phi(S^(i)_N) - N_i Phi(S^(j)_N)` on the five-dimensional space
   `Sym^4(N_5^*)^{Sp_4}`, is nonzero; otherwise it is a combination of `z(K5)` and `beta_z`, i.e.
   a multiple of `C2` on the source, however different the formula looks. The
   `Phi_4`-component vanishes iff the two evaluation functionals at `S^(i)_N, S^(j)_N` on the
   invariant quartics are proportional with the ratio `N_i : N_j`; this happens in particular if
   `S^(j)_N` is a conformal `Stab`-translate of `S^(i)_N`. For `(S1, S2)` this is not expected —
   `x1` is `u`-anisotropic and `x2` is `u`-isotropic, so the two directions are of different
   orbit type — but **it is not proved here**: deciding it needs the five invariant quartics on
   `N_5` evaluated at the two normal components, a finite invariant-theory computation that was
   not run (no additional numerical work was authorised). Until then, "`C4_{S1,S2}` is a
   different functional from `C2` on the jet space" is a Tier-C expectation, not a theorem.
4. Independently of 3, `C4_{ij}` is a different functional from `C2` **on the source** only if
   `j(M_(4^5))` is not contained in the subspace where the `Phi_4`-component of `C4_{ij}`
   vanishes — the realisation question (§4.7). This is what stage 1 of the test in §9 decides.
5. Elimination of `kappa~` requires `N(h_4(S^(i))) != 0` for the directions used: true for all
   five directions of Check 2 (`h4_nonzero = true`, `N != 0`).

## 7. What transfers from six variables to five (requirement 4)

| item | six variables | five variables | transfers? |
|---|---|---|---|
| base point | generic skew pencil, `det = u^2`, `u` nondegenerate in 6 vars | hyperplane skew pencil `K5`, `det = u^2`, `u` nondegenerate in 5 vars | yes (both are "skew pencil with quadratic-square determinant") |
| `Stab^0` image | `SO_6 = SL_4/mu_2` | `SO_5 = Sp_4/mu_2` | yes, as "the conformal orthogonal group of `u`" |
| normal space `N` | `45 = S_(3,1)C^4`, not self-dual | `35 = V(2w_1+w_2)`, orthogonal | the *mechanism* transfers; the *module* changes, and with it the lowest nontrivial order |
| lowest order with room | 4 (`j_2 = 0`) | 2 (`j_2 = 1`) | **no**: five variables admit an order-two test, six do not |
| E-free conditions through order 4 | exactly 1 | up to 5 | no |
| target-side free parameters through order 4 | `F(u^2), kappa~` | `F(u^2), kappa~` | yes (harmonic decomposition has the same shape) |
| universal constants | `A_{6,1}`, `N`, `108`, `-14` | `A_{5,1}`, `N`, tables in §5.2–5.3 | **no**: every constant must be recomputed; Check 2 does this for `k = 1` |
| evenness and degree `<= 4k` in `t` | yes (Plücker argument) | yes | yes |
| three-point extraction | `k = 1` only | `k = 1` only | yes at `k = 1`; `2k+1` nodes otherwise |
| arc `C` | `C = 0` (silent band) | `2 <= rank C <= 4` | no: independence from `C` is automatic in six variables and open in five |
| the restriction-only (quadratic-square family) obstruction | one scalar survives | one scalar survives | yes: only the value `z(K)` is seen; jets are indispensable in both |

## 8. Independence from the old arc, and the three distinctions

### 8.1 Route to nonzero action on `ker C` (requirement 6)

- `(6,(4^6))`: `C = 0` on the source (B19-01 Thm 4.1), so every nonzero necessary functional acts
  nonzero on `ker C = M`. Independence is automatic; `C_2` is one certified additional
  constraint (sealed). **PROVED.**
- `(5,(4^5))`: `E subset ker C`, `dim E = 1`, so `rank C <= 4`, and `E` lies in the kernel of every
  transverse condition too, so `rank [C; T] <= 4` for the transverse family `T`. Therefore

      increment := rank [C; T] - rank C  in {0, 1, 2}  with  rank C in {2, 3, 4},

  and the increment is positive **iff** `rank C < 4` and some transverse condition does not
  vanish on `ker C`. Three routes, in order of cost:
  1. **Rank-four arc certificate** (a nonzero `4 x 4` minor of actual forbidden coefficients on
     four certified independent vectors): then `ker C = E`, and *every* necessary condition —
     `C2`, all `C4`, anything else — is redundant. A theorem of redundancy, not a witness.
  2. **Transverse-first**: if the order-`<= 4` transverse family reaches rank `4` on `M_(4^5)`
     (the missing lemma), then `ker T = E` and the increment equals `4 - rank C`; independence
     from `C` is then equivalent to non-exactness of the arc, and a single exact arc-kernel
     vector `n` with `T n != 0` follows automatically from `rank C < 4`. This route needs the
     complete carrier once (five vectors, `1 + 2 x (number of directions)` points each) and no
     exact forbidden-coefficient verification beyond what route 1 already needs.
  3. **Witness**: an exact `n in ker C` (all forbidden coefficient polynomials verified zero,
     sealed §C step 4) with `C2(n) != 0` or `C4(n) != 0`. Cheapest if the carrier and the exact
     kernel are already in hand; this is the active session's target.
  A **redundancy theorem** without computation is not available: `C` is equivariant for the
  Levi `L` of B19-01 Prop. 6.1 and `T` for `Stab(K5)`, and these groups have no common
  reductive subgroup acting on `M_(4^5)` that could force `T subset rowspace(C)` by Schur's
  lemma. Redundancy can only be established as in route 1, or by `T` vanishing on a certified
  spanning set of `ker C` (corrigendum D).

### 8.2 The three distinctions (requirement 7)

- **Improved source bound** = `rank [C; T] > rank C`: the surviving source `s - rank` shrinks.
  Possible in `(4^5)` (unknown) and already realised in `(4^6)` (by one).
- **Bound below `a`** = `s - rank [C; T] < a`. Since `E` lies in every kernel,
  `rank <= s - m_det`, so `B >= m_det`, and `B < a` requires `m_det < a`, i.e. a determinant
  equation in the cell. In every cell touched here `m_det = a = 1`; **no transverse condition
  can lower the clipped bound below `a` there**, and none can anywhere unless an equation
  exists.
- **`D > 0`** additionally needs a certified actual-padding rank floor `r > B`. Nothing here
  produces a padding floor; the transverse programme is a determinant-side tool only.

## 9. Final deliverables

### 9.1 The representation-based selection rule (one sentence)

At a skew pencil `K` with `det K = u^2` and rectangular `lambda = (4k)^r`, the globally
necessary transverse conditions of order `<= 2m` number at most
`1 + sum_{j <= m} dim Sym^{2j}(N_r^*)^{Stab(K)} - (target parameters through order 2m)`, with
`N_6 = S_(3,1)C^4` (no order-two room, one E-free order-four condition, exactly the known one)
and `N_5 = V(2w_1 + w_2)` of `Sp_4` (one order-two condition, `C2`, unique up to scale in all
directions and all `k`; up to four further E-free conditions at order four). Tier A supplies the
numbers, Tier B the identities; realisation is Tier C.

### 9.2 The smallest meaningful ambient-nonempty test, and the one three-way test (NOT run)

Cell `(5, (4^5))`, `a = m_det = 1`, `s = 5`. Directions `S1 = x1 I`, `S2 = x2 I`,
`S4 = x1 diag(1,1,0,0)`; transverse rows `T = [C2; C4_{S1,S2}; C4_{S1,S4}]` with the integer
coefficients of §5.3 and the sealed `C2 = (112, -7, -177)`. Points: `K5, K5 + S1, K5 + 2S1`
(sealed values exist for `q_3, q_7`) plus `K5 + S2, K5 + 2S2, K5 + S4, K5 + 2S4` (new).

**Stage 1 — distinguishes outcome (1), redundancy with `C2`.** Evaluate `q_3, q_7` at the four
new points (`2 x 4 = 8` dense evaluations with the sealed `paired_runner.py`, measured `0.55 s`
each, peak job memory `219 MB` in the sealed P7; about `5 s`, one wrapped process). Compute the
`3 x 2` matrix `T [q_3 q_7]` exactly (integers) and modulo `524287`. A nonzero `2 x 2` minor
involving a `C4` row proves `rank T >= 2` over `Q`: the order-four family is **not** a multiple
of `C2` on the source (outcome (1) excluded, and the `Phi_4`-component question of §6.5 item 3
answered positively as a by-product). All `2 x 2` minors zero (exactly) proves only that the
three functionals are proportional on `span(q_3, q_7)`; outcome (1) is then not excluded and
the stage must be repeated on a larger certified subspace.

**Stage 2 — distinguishes outcomes (2) and (3), given the carrier.** With a certified basis
`q_1..q_5` of `M_(4^5)` (the active session's target) and the arc rows `C` on it:
- if a nonzero `4 x 4` forbidden minor certifies `rank C = 4`: **outcome (2)** for every
  transverse condition, by the theorem `ker C = E` (redundant with the arc, whatever `rank T`
  is);
- otherwise, with an exact kernel matrix `N_C` (all forbidden coefficient polynomials verified
  zero, sealed §C step 4): `T N_C = 0` exactly gives **outcome (2)** (independent of `C2` if
  stage 1 said so, yet redundant with the arc); `T N_C != 0` gives **outcome (3)**, a certified
  additional condition on the arc kernel, with increment `rank(T N_C) in {1, 2}`.
Stage 2 needs `5 x 4 = 20` further evaluations at the new points (dense: about `11 s`; sparse:
to be priced by the active session) plus the arc work that session already plans.

**Not run here.** Stage 1 evaluates the same certified vectors at `K5`-type points that the
active sparse-evaluator session (`…_addendum/FEASIBILITY.md`, Stage B) uses for its own
verification; running it would duplicate that session's point family with a different
evaluator. It should be attached to that session's continuation by adding the four points to
its list. No source-carrier computation was started here.

### 9.3 The exact missing lemma

**Lemma (jet injectivity at `K5`, OPEN — Tier C).** *For `z in M_(4^5)`: if `z(K5) = 0`,
`Phi_2(z) = 0` and `Phi_4(z) = 0`, then `z = 0`.* Equivalently, the source jet map
`j : M_(4^5) -> J_{<=4} = C^7` is injective, i.e. the order-`<= 4` transverse conditions at `K5`
have rank exactly `4` on the source and their common kernel is `E`.

If true, the transverse family alone certifies the determinant coordinate subspace in this
cell, the arc is redundant with it, and "independence from `C`" reduces to `rank C < 4`. If
false, there is a nonzero full-`H` invariant flat to order four at `K5` in every normal
direction, and order six (`j_6(5) = 24`) or a second base point is required. The six-variable
analogue (`j : M_(4^6) -> C^3` surjective?) decides whether the second, `E`-using order-four
condition adds rank there. A complete carrier of `M_(4^5)` is needed to decide the lemma; five
independent 4-jet directions (including non-scalar symmetric tuples) give `5 x (1 + 2 x 5) =
55` evaluations at `k = 1`.

A second, purely local lemma would settle §6.5 item 3 without any source vector: *the
evaluation functionals at `S1_N` and `S2_N` on `Sym^4(N_5^*)^{Sp_4}` are not proportional.* It
is a finite invariant-theory computation on a 35-dimensional module and was not run.

## 10. Claim ledger

| # | claim | tier | label | evidence |
|---|---|---|---|---|
| T1 | `Stab_Gamma(K)^0` as in Lemma 4.1; image `SO_6` / `SO_5` | B | PROVED (commutant MEASURED for `K5`) | §4.1, `c1…json: A_K5_commutant_dimension = 1` |
| T2 | `T_K = T_orb (+) C.K (+) N`, dims `50/51/45` and `44/45/35`; all skew directions in `T_orb + C.K` | A | MEASURED (exact rank) | `c1…json: A_tangent_K6/K5` |
| T3 | `N_6 = S_(3,1)C^4` (not self-dual), `N_5 = V(2w_1+w_2)` (orthogonal) | A | PROVED given T2 + MEASURED LR multiplicities | `c1…json: B_characters` |
| T4 | formal slice and automatic-jets theorem (4.3, 4.4) | B | PROVED | §4 |
| T5 | `j_2(6)=0, j_4(6)=2, j_6(6)=6; j_2(5)=1, j_4(5)=5, j_6(5)=24, j_8(5)=127` | A | MEASURED, eight controls passing | `c1…json` |
| T6 | target-side: no free parameter at order two, one (`kappa~`) at order four; covariance formulas | B | PROVED | §5.1 |
| T7 | `A_{r,k}`, `N o h_4`, the `[t^4]` formula on `E` | B | PROVED; VERIFIED at `(r,k) = (6,1)` against p9 (`108, -14, 3/896`) and at `(5,1)` on five directions (`kappa~ = 1/224`) | `c2…json` |
| T8 | explicit `C4_{S,S'}` integer conditions, globally necessary on `M_(4^5)` | B | PROVED (necessity) + VERIFIED (exact zero on `H5` line) | `c2…json: five_variables.C4` |
| T9 | `C4` nonzero on the source; `C4` distinct from `C2` on the source | C | NOT REACHED (no source vector evaluated) | §6.5, §9.2 stage 1 |
| T9' | `C4_{S1,S2}` has nonzero `Phi_4`-component on the jet space | C (local) | EXPECTED, not proved | §6.5 item 3 |
| T10 | six-row: no order-two condition; exactly one E-free order-`<=4` condition; `>= 7` survivors invisible at `K6` through order four | B | PROVED (given T5) | §6.3 |
| T11 | five-row order-two redundancy theorem (all directions ∝ `C2`) | B | PROVED (given T5) | §6.3, Thm 6.2 |
| T12 | five-row: `<= 5` E-free conditions through order four, realised rank `<= 4` | B | PROVED | §6.3, §6.5 |
| T13 | `k`-dependence formulas for `(4k)^5` | B | PROVED, checked only at `k = 1` | §5.4 |
| T14 | non-rectangular counting as a branching problem | — | OPEN (stated only) | §6.3 |
| T15 | jet-injectivity lemma at `K5` | C | OPEN | §9.3 |
| T16 | `rank[C;T] <= 4` at `(4^5)`; increment iff `rank C < 4` and `T` nonzero on `ker C`; no Schur-type redundancy theorem available | B | PROVED | §8.1 |
| T17 | no transverse condition lowers `B` below `a` where `m_det = a`; no padding content | B | PROVED | §8.2 |
| T18 | sealed inputs used: `C2` necessity and nonzeroness (E3, E6), `-12` witness (E11), `3/896` | C (sealed) | ADOPTED from the sealed packet, VERIFIED where recomputed (T7) | §1 |

## 11. Honest negatives and limits

1. No source vector was evaluated; every "realised rank" statement about the five-row
   order-four family is open (Tier C). The numbers `j_m` are room, not rank (§4.7).
2. Whether `C4_{S1,S2}` is even locally distinct from `C2` (nonzero `Phi_4`-component) is not
   proved; it is expected from the different orbit types of `x1` and `x2` under `SO_5`.
3. The target-side count beyond order four (how many of the `j_6` source parameters are matched
   by `d^3 F_{u^2}` invariants) was not derived; "order six" statements are about room only.
4. Non-rectangular cells are not covered by the theorem.
5. The `k >= 2` formulas have no numerical control.
6. The six-row question whether the second (`E`-using) order-four condition adds rank is open.
7. Nothing here produces a padding floor, an equation, or a gap; every cell touched is a known
   no-gap cell.
8. Check 1's Sym-power characters were truncated at order six (`r = 6`) and eight (`r = 5`) for
   cost; higher orders are not tabulated. Closedness of the `Gamma`-orbit of `K` (relevant only
   to the local-global remark in §4.7) was not checked.

## 12. Files and receipts

- `checks/c1_normal_space_counts.py/.json` — Check 1 (wall `1.01 s`, exit `0`, Job Object
  receipt `results/logs/c1_normal_space_counts_resources.json`).
- `checks/c2_fivevar_order4.py/.json` — Check 2 (wall `3.44 s`, exit `0`, receipt
  `results/logs/c2_fivevar_order4_resources.json`).
- Total numerical wall time: about `4.5 s` in the two allowed checks; no failures, no retries;
  no source contraction evaluated; the active session's files untouched.
- `drafts/REPORT_body_draft.md` — the first draft of §4–§12, kept as the incremental record;
  superseded by this file.
- `MANIFEST.json` — SHA-256 of every input listed in §1 and of every file written here; the
  report was finalised before hashing.

Status: **COMPLETE — one developed route (the transverse jet selection rule, Theorem 6.1) with
two bounded checks; five-row order-two uniqueness and six-row order-four uniqueness proved;
realisation and arc-independence left as the stated Tier-C lemma and the one three-way test,
not run.**
