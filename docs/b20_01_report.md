# B20-01 — Resolve the mixed-pairing identity

Batch 20, slot 01. Worktree `work/batch15_workers/B15-01`, branch `b15-01-ci159`.
Starting `HEAD = 6b16151328d38dc0ce39bcfab51e83459a035d79`, `HEAD^{tree} = 42daad6d08fe78daa7bbf2a06200ee2154ed7663`,
recorded at 2026-09-17T20:37:57Z before any write; `git status --porcelain` showed no tracked change
(the known untracked `results/` residue only). Read-only git throughout; no commit, no push.

**Status: PAUSED with the missing theorem stated (§5), plus a proved reduction that cuts every further
price by a factor of about three (§4). No numerical work ran in this session: the harness's auto-mode
safety classifier blocked every command execution after the inputs were read (§2.2). G8 is therefore
NOT discharged: the definition certificates for `q_3`, `q_7` are specified and their emitting script is
written and dry-run-ready, but no certificate with an ordering hash exists yet (§3).**

## 0. What this slot can and cannot establish

No positive multiplicity gap is possible in this cell, in either branch of the outcome. `lambda = (4^5)`
at `d = 5` has `m_pad = 0`, `m_det = 1`, `D = -1` (B20-10 R6–R8, two lineages), and the degree-five
five-row family is 22 cells at `D = 0` and one at `D = -1`. A necessary source condition, a coefficient
equation, a separation and a positive multiplicity gap are four different achievements; this slot
touches the first only. Its value is that it closes a paused diagnostic; the `rank(C|_U) = 2` branch
yields an existence result (a kernel vector of the arc on which the transverse `C4` conditions are
nonzero, `arc_target` Prop. 7.1), the `rank(C|_U) = 3` branch closes the diagnostic negatively. Neither
gives an equation, a separation or a gap.

## 1. Plain terms

Three source vectors `q_3, q_7, n02` of the five-dimensional space `M` are known exactly (as contraction
patterns). The arc functional `C` extracts their skew-degree-12 and skew-degree-11 parts. On fourteen
sampled functionals the three images look linearly dependent (one relation, with coefficients that are
residues modulo `P = 524287` and have no small rational lift). The degree-12 parts are proportional
(exactly rank 1 on all recorded rows). The open question is whether the degree-11 parts satisfy the same
relation as polynomials — the "mixed-pairing identity". The previous session reduced the degree-12
parts to functions on a 23-dimensional locus and certified statements there with 50 evaluations; it
could not do the same for the degree-11 parts, and asked for "a density argument on a product locus".

This report proves that the degree-11 question lives on a locus of triples `(Z_1, Z_2, Z)` of matrices
with zero skew block (Theorem A), which makes each degree-11 functional three times cheaper and removes
one of the two open conditions from the previous formulation. It then shows why a density argument on
that locus cannot be made affordable without an explicit basis of the 70-dimensional Levi-invariant
target, states the missing theorem exactly, and rules out the relabelling-sign mechanism as the source
of the identity (§4.5). The three pilots that would (1) discharge G8, (2) check Theorem A numerically and
(3) run the cheaper negation route are written and unrun.

## 2. Provenance, inputs, and the execution block

### 2.1 Inputs read (pinned; read-only `git show` from the shared object store)

All packet inputs were read at archive commit `82633a60893236fab4fbc317df416e1b8a349005`
(`docs/post_b19_20260917/…`); the B15-02 carrier and wrapper at `75ddb900a0b47b911c53f941885bac73b358eacb`.
Hashes verified at session start with `git show … | sha256sum` (these commands ran before the block):

| input | pin (sha256 prefix) | verified |
|---|---|---|
| `descent_followup_claude_20260916/pilots/paired_runner.py` | `33c81c96…` | full hash equal (archive and original) |
| `B15-02/analysis/b18_02_carrier.py` (commit `75ddb900`) | `8670040e…` | full hash equal (commit and working tree) |
| `B15-02/analysis/b15_bound.py` | `ca001081…` (working tree, CRLF) / `1f73ad8d…` (committed LF blob) | both as recorded in B20-10 R25 |
| `descent_followup_claude_20260916/pilots/p6_basis.json` | `aaee6ec0…` | full hash equal |
| `B15-10/docs/b20_10_review.md` | `021be68f748e8f05…` | full hash equal |
| `routeA_signfilter_20260917/certificates/n02_definition.json` | `ffeead803eba…` | read, prefix as pinned in the launch prompt |
| the four scripts carrying the `q_3`/`q_7` orderings | `81d3ee7a…`, `ac6c3a23…`, `b03dab82…`, `b531cfb1…` | read at the archive commit; literal at s1:69, s2:83, s3:68, f1:51 |
| `CURRENT_DIAGNOSTIC_STATE.md`, `direct_arc` REPORT + CORRIGENDUM + code + results, `arc_target` REPORT + CORRIGENDUM, `STABILIZER.md`, `SOURCE_HANDOFF.md`, `routeA` REPORT §3/§5 + `autfilter.py`, `b18_10_review.md` §7, `b20_10_review.md` §§8–9, §12 | as listed in the launch prompt | read; corrigenda before parents |

Corrigenda govern: `direct_arc/CORRIGENDUM.md` C1–C3 and `arc_target/CORRIGENDUM.md` C1–C4 were read
first. B20-10 R3 (cite the scalar subtorus of `L`, not Prop 3.1, for `|mu| = d`), R5, R9, R10, R11–R12,
R16 are applied as instructed; nothing below uses the 10,505 / 424,193,140 counts as `b`, the
singular-locus theorem, or any chat-only constant.

**Provenance note (new, READ).** The sealed generator `p6_basis.py` (archive line 45) calls
`pr.qval(cand['pi'], cand['rho'], T, cand['pairing'])`, passing the *pairing* as the fourth argument,
whereas the sealed runner's `qval(pi, rho, T, order)` iterates `for j in order` over column indices;
with a pairing such as `((0,1),(2,3))` in that slot the sealed runner's final assertion fails. So the
runner bytes pinned at `33c81c96…` are not the bytes that produced `p6_basis.json`'s values as the
script stands. This does not move any label: the `q_3`, `q_7` values at the P6 points were replayed by
`s1`'s runner-consistency control (P7 point 0) and by `direct_arc` pilot 3's factorization control
(P6 point 0, `260975`, `301718`) with the pinned runner and the hand-plan orders. It is a reason G8
matters: the orders `(0,1,2,3)` and `(0,2,1,3)` must ship as data, which pilot 1 does.

### 2.2 The execution block (honest negative, first)

After the inputs were read and the first pilot script was written, every Bash command that executes a
program was refused by the auto-mode safety classifier with the message "Auto mode could not evaluate
this action and is blocking it for safety — a safety check separate from auto mode blocked this request
because of earlier conversation content — it isn't about the action itself … it will keep firing for
the rest of this conversation." Two probes confirmed the scope: `python -c "print('exec ok')"` was
refused; `git status --porcelain` (read-only) was allowed; a read-only pipeline containing `jq` and
`sha256sum` was refused. I did not try to route around the block (no subagent, no rewording).
Consequences, each stated at the point where it bites: no pilot ran; no receipt exists; no sha256 of any
new file was computed; no ordering hash was computed; no sealed manifest exists. The user must run the
three scripts outside auto mode (commands in §9) — each is pre-bounded to the 60 s / 512 MiB wrapper.

## 3. G8 — the definition certificates for `q_3` and `q_7` (specified, script written, NOT emitted)

**What the certificates are.** `results/b20_01/certificates/q3_definition.json` and `q7_definition.json`,
in the format of the sealed `n02_definition.json` (`ffeead80…`), each carrying:

- `pi_ordered_blocks`, `rho_ordered_blocks`: the five ordered epsilon blocks of `p6_basis.json: basis[0]`
  (index 3, pairing `((0,1),(2,3))`) and `basis[1]` (index 7, pairing `((0,2),(1,3))`), transcribed in
  §3.1 below from the pinned bytes;
- `hand_plan_column_order` and `hand_plan_column_order_transposed`: `(0,1,2,3)` for `q_3`, `(0,2,1,3)` for
  `q_7`, both orientations — the literal `zip(p6['basis'], ((0, 1, 2, 3), (0, 2, 1, 3)))` read in all four
  scripts (s1:69, s2:83, s3:68, f1:51; in each the zip pairs `basis[0]` = index 3 with `(0,1,2,3)` and
  `basis[1]` = index 7 with `(0,2,1,3)`), and `SOURCE_HANDOFF.md` §2.1;
- `ordering_hash` with its scheme stated in the file: sha256 of the canonical JSON
  (`sort_keys=True`, separators `(",", ":")`) of the object with exactly the four keys
  `hand_plan_column_order`, `hand_plan_column_order_transposed`, `pi_ordered_blocks`, `rho_ordered_blocks`;
- `evaluation_points`: the five P6 points (`p6_basis.json: points_entries`) and P7 S0 point 0 with its
  `a -> 0` scaling; `values`: the sealed values (`260975, 509003, 336756, 260012, 342025` for `q_3`;
  `301718, 423302, 275526, 317892, 384` for `q_7`; S0 point 0 at `t = 0`: `185448`, `288291`);
- the pins (commit, path, full sha256, byte count) of every input the script read, the runner and
  carrier pins, and the replayed values with match flags.

**Verification the script performs** (`analysis/b20_01_p1_definitions.py`): (i) regex-extracts the
literal from the four pinned script byte strings and asserts all four equal `((0,1,2,3),(0,2,1,3))`;
(ii) regenerates all 30 P6 candidates and the five P6 points from seed `20260916` with the pinned
`paired_partition` (label-only) and asserts the blocks and points of indices 3 and 7 are equal to the
sealed record; (iii) asserts `paired_runner.hand_plan` returns exactly the literal orders in both
orientations with max intermediate `<= 4^10`; (iv) replays the five P6 values and the S0 value with the
pinned runner (12 symmetrised evaluations, about 7 s); (v) writes the two certificates and a sibling
`n02_ordering_hash.json` that cross-checks the sealed `n02_definition.json` against
`candidates_selected.json` (blocks and orders) and records n02's ordering hash under the same scheme —
the sealed certificate is not touched. A `--dry` mode does (i)–(iii) and (v) without the runner.

**What was verified by reading (READ, not executed).** Items (i) and the block transcription: the four
literals were read in the pinned bytes and are identical; the blocks in §3.1 were copied from the
pinned `p6_basis.json` and agree with `SOURCE_HANDOFF.md` §2.1 line by line. Items (ii)–(v) did not run.

**Label.** G8: OPEN — not discharged in this session. The certificates cannot be hand-written as
CERTIFIED-portable because the ordering hash is a computation the harness refused. Nothing in §§4–5
consumes the `q_3`/`q_7` certificates as data: the theory uses only the contraction form (2.1) and the
pinned block lists; the pilots consume the pinned `p6_basis.json` record and the literal orders, exactly
as the four sealed scripts did, and record the pins in their outputs (G10).

### 3.1 The definitions (transcribed from the pinned bytes; slots `[column, position]`)

```
q3  pairing ((0,1),(2,3))   hand plan (0,1,2,3) both orientations
    pi  = [[0,1],[0,4],[1,3],[1,0]] [[0,0],[0,3],[1,2],[1,1]] [[2,3],[2,4],[3,3],[3,1]] [[2,2],[2,1],[3,0],[3,2]] [[0,2],[1,4],[2,0],[3,4]]
    rho = [[0,4],[0,2],[1,0],[1,4]] [[0,3],[0,1],[1,3],[1,2]] [[2,1],[2,4],[3,2],[3,1]] [[2,0],[2,3],[3,4],[3,0]] [[0,0],[1,1],[2,2],[3,3]]
q7  pairing ((0,2),(1,3))   hand plan (0,2,1,3) both orientations
    pi  = [[0,1],[0,3],[2,3],[2,0]] [[0,4],[0,0],[2,4],[2,2]] [[1,1],[1,4],[3,4],[3,2]] [[1,2],[1,0],[3,0],[3,1]] [[0,2],[2,1],[1,3],[3,3]]
    rho = [[0,4],[0,1],[2,2],[2,0]] [[0,3],[0,0],[2,3],[2,4]] [[1,3],[1,0],[3,3],[3,2]] [[1,2],[1,4],[3,0],[3,4]] [[0,2],[2,1],[1,1],[3,1]]
n02 pairing ((0,2),(1,3))   hand plan (0,2,1,3) both orientations   (sealed n02_definition.json; equal to candidates_selected.json, READ)
```

Conventions as in `SOURCE_HANDOFF.md` §1: `pi` blocks contract row indices, `rho` blocks column indices,
`eps(0,1,2,3) = +1`, `q = P_{pi,rho} + P_{rho,pi}`, column tensor `D[c_0..c_4] = det[(Y_i)_{c_k}]`.

## 4. Theory (PROVED unless labelled)

### 4.1 Setting and the exact question

`W = A (x) B = Mat_4`; adapted coordinates per matrix `a, r, c, Sigma, nu` (B18-02 §1; `SOURCE_HANDOFF.md`
§1); `W' := W_{-1} (+) W_{+1} = {nu = 0}` (dim 13), `W_0 = <nu_1, nu_2, nu_3>`, `nu_k := A(e_k)`, i.e.
`(nu_k)_{ij} = -eps_{ijk}` on the 3x3 block. For a tuple `Y = (Y_1..Y_5)` write `v` for the `3x5` matrix of
skew coordinates, `v_{km} := nu_k`-coordinate of `Y_m`, and `Y'_m := Y_m - sum_k v_{km} nu_k in W'`.

Each of `q_3, q_7, n02` is, by its definition (2.1), a quartic polynomial in the column tensor
`D(Y) = Y_1 ^ ... ^ Y_5 in Lambda^5 W`: `q(Y) = q~(D, D, D, D)` with `q~` the symmetric four-linear form
read off (2.1) (each of the four columns is a copy of the same 5-wedge). The skew grading
`q = sum_n q^{[n]}` is the grading by `nu`-degree; `C(q) = (q^{[12]}, q^{[11]})`.
The question: with `f := n02 - alpha q_3 - beta q_7` for the `(alpha, beta)` fixed by the recorded
degree-12 and degree-11 rows, is `f^{[11]} = 0` as a polynomial (given `f^{[12]} = 0`, sampled-true)?
`rank(C|_U) = 2` iff some `(alpha, beta) in Q^2` makes both vanish.

### 4.2 Theorem A — reduction of the degree-11 parts to the flag locus

**Theorem A.** Let `z` be any polynomial of the form `z(Y) = z~(D(Y), D(Y), D(Y), D(Y))` that is invariant
under `Y -> A Y A^{-T}` for permutation matrices `A = diag(1, sigma)`, `sigma in S_3` (every element of
`M` is: `det A det A^{-T} = 1`, `L`-invariance). Then:

(i) *(GL_5 covariance of the graded pieces)* for every `g in GL_5` acting on the tuple index,
`z^{[n]}(g.Y) = det(g)^4 z^{[n]}(Y)` for every `n`.

(ii) *(slice form)* if `rank v = 3`, there is `g in GL_5` with `g.Y = (Z_1, Z_2, Z_3 + nu_1, Z_4 + nu_2, Z_5 + nu_3)`,
`Z_i in W'`: take rows `u_1, u_2` spanning `ker v` and `u_{k+2}` with `v u_{k+2} = e_k`.

(iii) *(decomposition)* on the slice, `z^{[11]} = F_1 + F_2 + F_3` with
`F_k(Z_1, Z_2, Z_{k+2}) := z^{[11]}` evaluated at the tuple that keeps only `Z_{k+2}` among `Z_3, Z_4, Z_5`
(i.e. at `(Z_1, Z_2, delta_{k1} Z + nu_1, delta_{k2} Z + nu_2, delta_{k3} Z + nu_3)`), and `F_k` is linear in
`Z_{k+2}`. Consequently `z^{[11]} = 0` on the slice iff `F_1 = F_2 = F_3 = 0` on `W'^3`.

(iv) *(S_3)* for `sigma in S_3`, `P := diag(1, sigma)`: `F_1^z(Z_1, Z_2, Z) = sgn(sigma) F_{sigma(1)}^z(P Z_1 P^T, P Z_2 P^T, P Z P^T)`.
Hence `F_1^z = 0` iff `F_k^z = 0` for all `k`.

(v) *(conclusion)* `z^{[11]} = 0` as a polynomial in the 80 variables iff `F_1^z = 0` as a polynomial in the
39 coordinates of `(Z_1, Z_2, Z) in W'^3`; and at such a tuple, scaling the three `nu`'s by `u` gives
`z(Z_1, Z_2, Z + u nu_1, u nu_2, u nu_3) = sum_{n=8}^{12} u^n z^{[n]}`, so **five nodes** (or the four-node odd
extraction `[u^{11}]` from `u = +-1, +-2` after removing `u^8`) recover `F_1^z = [u^{11}]` and the top
`z^{[12]} = [u^{12}]`, instead of thirteen.

*Proof.* (i) `D(g.Y) = det(g) D(Y)` (5x5 minors of `g` times the `5x16` matrix `Y`), so `z(g.Y) = det(g)^4 z(Y)`;
the skew-part projection is linear and the same on each `Y_m`, so scaling all skew parts by `u` commutes
with `g`; comparing `u`-coefficients gives the graded statement. (ii) `v` has rank 3 on a dense open set;
with `g` as stated, `(g.Y)_i = sum_m g_{im} Y_m` has skew coordinates `v u_i`, which is `0` for `i = 1, 2`
and `e_k` for `i = k + 2`. `det g != 0` because `u_1, u_2` span `ker v` and `v u_{k+2}` are independent.
(iii) On the slice `D = Z_1^Z_2^(Z_3+nu_1)^(Z_4+nu_2)^(Z_5+nu_3)`; its `nu`-degree-3 part is
`D_3 = Z_1^Z_2^nu_1^nu_2^nu_3` and its degree-2 part is
`D_2 = Z_1^Z_2^(Z_3^nu_2^nu_3 + nu_1^Z_4^nu_3 + nu_1^nu_2^Z_5)`. Degree 11 from four factors of degree
`<= 3` arises only as `4 z~(D_3, D_3, D_3, D_2)`, which is linear in `D_2`, hence a sum of three terms each
linear in exactly one of `Z_3, Z_4, Z_5`; the `k`-th term is what `z^{[11]}` reduces to when the other two
are set to zero, i.e. `F_k`. A sum of functions of disjoint variable groups vanishes iff each does (set
the other groups to zero). (iv) `z` is invariant under `Y -> P Y P^T`; this map preserves `W'` and sends
`nu_k` to `sgn(sigma) nu_{sigma(k)}` (from `eps_{sigma^{-1}(i) sigma^{-1}(j) k} = sgn(sigma) eps_{i j sigma(k)}`), and
it preserves `nu`-degree. Apply it to the `F_1`-tuple, then permute the tuple entries so that
`nu_{sigma(k)}` sits in slot `sigma(k) + 2` (a GL_5 permutation, factor `(+-1)^4 = 1`), then scale those
three entries by `s = sgn(sigma)` (factor `s^4 = 1`): the result is the `F_{sigma(1)}`-tuple at
`(P Z_1 P^T, P Z_2 P^T, s P Z P^T)`; linearity in the third argument gives the sign. (v) Combine (i)–(iv); the
degree count at an `F_1`-tuple is `D = u^2 (u D_3 + D_2')`, so `z` has `u`-degrees `8..12` only. QED

**Corollary A.1 (price).** A full degree-11 functional on `(q_3, q_7, n02)` costs `3 x 5 = 15` symmetrised
runner evaluations at a point of the flag locus (`3 x 4 = 12` with the odd-part extraction), against
`3 x 13 = 39` at a general point; both give, in addition, the degree-12 value at the same point. Every
price below is quoted with this factor.

**Corollary A.2 (what the degree-11 part is).** `F_1^z(Z_1, Z_2, Z) = 4 z~(D_3, D_3, D_3, Z_1^Z_2^Z^nu_2^nu_3)`
depends on `(Z_1, Z_2, Z)` only through `beta := Z_1^Z_2 in Lambda^2 W'` and `gamma := Z_1^Z_2^Z in Lambda^3 W'`:
it is the restriction to the cone `S^ := {(beta, gamma) : beta = Z_1^Z_2, gamma = beta^Z}` over the partial
flag variety `Fl(2, 3; W')` (`dim S^ = 23 + 11 = 34`) of a polynomial of bidegree `(3, 1)`; in the 39
coordinates of `(Z_1, Z_2, Z)` it has total degree `3·2 + 3 = 9`. The degree-12 part is the previous
session's `t`-locus statement: `z^{[12]}(Z_1, Z_2, nu_1, nu_2, nu_3) = z~(D_3^4)`, a function of `beta` alone on
`S* = cone(Gr(2, W'))`, degree 4 in `beta`.

**Status of Theorem A.** PROVED (the argument above). Its numerical control — reproduce the sealed full
rows `full_P6pt0_d11 = (86170, 71919, 226580)` and `full_P6pt0_d12 = (376209, 469277, 41046)` from
`det(g)^4 (F_1 + F_2 + F_3)` and `det(g)^4 [u^{12}]`, and the `S_3` sign relation of (iv) — is pilot 2
(`analysis/b20_01_p2_reduction.py`, 60 evaluations, about 30 s), **not run** (§2.2). Until it runs the
theorem is PROVED but "producer only" (G18): no second lineage, no evaluation has exercised the
bookkeeping (signs of `nu_k`, the kernel construction, the node extraction).

### 4.3 Proposition B — transposition anti-invariance of the degree-11 parts

**Proposition B.** Let `tau'` be the involution of `W^5` that swaps `r <-> c` in every `Y_m` and fixes
`a, Sigma, nu`. For every `z in M`: `z^{[12]} o tau' = z^{[12]}` and `z^{[11]} o tau' = - z^{[11]}`.

*Proof.* `z(Y^T) = z(Y)`, and `Y -> Y^T` is `tau'` followed by `nu -> -nu`, which multiplies the `nu`-degree-`n`
piece by `(-1)^n`; `tau'` preserves `nu`-degree. QED

So `C(M)_{-1}` lies in the `tau'`-anti-invariant part of `F^L_{-1}` (`tau'` normalises `L` and preserves the
multidegree pieces with `#r = #c`, `arc_target` §6.2), and `z^{[11]}` vanishes on the fixed locus `r = c`.
This is a genuine, previously unstated constraint — it halves the target in expectation — but it does not
decide the identity, and `dim (F^L_{-1})^{tau' = -1}` is not computed here (it needs the explicit basis of
§5). Label: PROVED; the dimension OPEN.

### 4.4 Proposition C — the degree-11 target on the flag locus is exactly 70-dimensional

**Proposition C.** The linear map `z_{-1} -> F_1^{z}` (restriction to the `F_1`-tuples) is injective on
`F^L_{-1} = ((S_lambda W)_{#v = 11})^L`, whose dimension is `b_L(11) = 70` (`arc_target` §5.1, PROVED there).
Hence `V_70 := {F_1^z : z in F^L_{-1}}` has dimension exactly 70, and the mixed-pairing identity is the
statement that three explicit vectors of `V_70` — `F_1^{q_3}, F_1^{q_7}, F_1^{n02}` — satisfy one specific
linear relation.

*Proof.* Elements of `F^L_{-1}` are `GL_5`-semi-invariant of weight `(4^5)` (they lie in the `S_lambda W`
isotypic highest-weight space), are polynomials in the Plücker coordinates of `D` (first fundamental
theorem for `SL_5` on `W (x) C^5`; ADOPTED, classical; for the three source vectors it is (2.1) itself),
and are `L`-invariant, in particular invariant under `diag(1, sigma)`; so Theorem A (i)–(iv) applies to
each of them and gives `z_{-1} = 0 <=> F_1^{z} = 0`. QED

### 4.5 The symmetry search (the half-session the board asked for) — three mechanisms, none decisive

**(a) Relabelling signs cannot be the mechanism (PROVED, negative).** The sign-filter theorem (`routeA` §3)
produces, from one `g in S_5 wr S_4` with `g(pi) = pi`, `g(rho) = rho`, the identity `P_{pi,rho} = sign(g) P_{pi,rho}`;
any relabelling argument on the mixed pairing `B(t_i, s_j)` produces identities whose coefficients are
signs, or small integers from summing over an orbit of patterns. The identity at stake has coefficients
`(alpha, beta)` whose residues `(265391, 275398)` admit no rational lift of height `<= 2000`
(`routeA` §5.3, replayed in `arc_target` C3). A relabelling identity `f^{[11]} = 0` with `f = n02 - alpha q_3 - beta q_7`
would force `alpha, beta` to be ratios of small integers (the coefficients of the finitely many
relabelled patterns), contradicting the height search. So either the identity is false, or it holds for
a reason that is not a relabelling symmetry of the patterns. This closes the board's first question with
a reason, not with a search.

**(b) Transposition (Proposition B).** A valid constraint; halves the target; not decisive.

**(c) Isotropic type structure of `B` (PROVED structure; consequence untested).** With `A = C e_0 (+) A'`,
`B = C f_0 (+) B'`, `Lambda^2 A = (e_0 ^ A') (+) Lambda^2 A'` and the same for `B`; the pairing
`Lambda^2 A x Lambda^2 A -> Lambda^4 A` is zero on `(e_0^A') x (e_0^A')` and on `Lambda^2 A' x Lambda^2 A'` (`dim A' = 3`),
and nondegenerate between the two summands. Writing the four type components `X_{11}, X_{12}, X_{21}, X_{22}`
of `X in Lambda^2 A (x) Lambda^2 B` (first index: `e_0`-type or not in `A`; second: `f_0`-type or not in `B`),
`B(X, X') = <X_{11}, X'_{22}> + <X_{22}, X'_{11}> + <X_{12}, X'_{21}> + <X_{21}, X'_{12}>`. Under `L`, `X_{11}` is a
`3x3` matrix (`std (x) std'`), `X_{22}` its dual type, `X_{12}, X_{21}` mixed. The degree-12 rank-1 phenomenon
and a degree-11 rank-2 phenomenon would both be explained if the tops `t(Phi)` and the mixed parts
`s(Phi)` of the four covariants had only one or two nonzero type components on the loci, so that the
pairings `B(t, t')` and `B(t, s') + B(s, t')` factor through a one- or two-dimensional space of functions.
This is a cheap numerical question (the `half_tensor` routine of `direct_arc` pilot 3 evaluates a
covariant at a locus point in about `0.1 s`; the 256-vectors were not stored in the sealed results),
which this session could not run; it is listed as reopening condition (c) in §8. Label: structure
PROVED; mechanism OPEN.

## 5. The missing theorem, and why the selected approach cannot reach it

### 5.1 What a certificate of the identity needs

By Proposition C, certifying `F_1^{n02} = alpha F_1^{q_3} + beta F_1^{q_7}` in `V_70` needs 70 linear
functionals on `V_70` whose evaluation matrix on a basis of `V_70` is invertible (a nonzero modular minor
suffices: it proves the 70 functionals independent over `Q`, hence injective), plus the three vectors'
values on those functionals. The functionals available are point evaluations on the flag locus; the
basis is the obstacle.

**Missing Theorem (stated exactly).** *An explicit spanning set `{h_1, ..., h_N}` (`N >= 70`) of `F^L_{-1}`
by polynomials that can be evaluated, together with 70 points `p_1, ..., p_70` of the flag locus
(tuples `(Z_1, Z_2, Z + nu_1, nu_2, nu_3)`, `Z_i in W'`, entries integers) such that the `70 x N` matrix
`[F_1^{h_j}(p_i)]` has a nonzero `70 x 70` minor modulo a prime.* With it: 70 rows on `(q_3, q_7, n02)` at
the `p_i` (`70 x 3 x 5 = 1050` runner evaluations, or `840` with the odd-part extraction; about `7–9`
minutes at `0.5 s` each) decide the identity exactly (the relation holds in `V_70` iff it holds on the
70 rows), and the degree-12 rows come free at the same points.

**Where the spanning set comes from.** `arc_target` §6.4 item 1 gives the recipe: by the first
fundamental theorem for `SL_3` and reductivity of `L`, `F^L_{-1}` is spanned by complete `GL_3`-contractions
(`delta`, `eps`) of adapted-coordinate slots of the multidegrees `(#a, #r, #c, #Sigma) in {(1,4,4,0), (2,3,3,1), (3,2,2,2), (4,1,1,3)}`
with `#v = 11`, arranged in four `5x5` determinants; the count `7 + 31 + 28 + 4 = 70` per multidegree is
the target for the minor. This is a new typed evaluator (indices of dimension 3, about 300 lines) and a
candidate search of about `200` patterns at `80` points (`~35 s` there), then the `70 x 70` minor. It is
the same object the previous session priced at "2,700 evaluations"; Theorem A brings the source-vector
part to `840–1050` and removes the 13-node interpolation from the basis evaluation as well (the `h_j` are
evaluated directly at `F_1`-tuples). It remains above this slot's 180 s.

### 5.2 Why the transversal-slice density method cannot substitute for the basis (PROVED counting)

The previous session certified statements about tops with 50 evaluations because (a) the group
`G' = L~ x| U_-` (17 effective dimensions) has dense orbit closure on `S*` (dim 23) together with a
5-dimensional linear slice `V`, and (b) *all* functions of the relevant type on `cone(V)` form the
50-dimensional `S_{22}(V^*)`. The method never uses `L`-covariance of the function space; it certifies
vanishing of every function of the given degree on the slice. For the degree-11 parts this fails on
both counts:

1. **`U_-` does not act on `F_1` alone.** Left multiplication by `I + E_{k0}` adds `r_n`-multiples to the
   block entries `(k, n)`, i.e. adds `W_0`-components to `Z_1, Z_2, Z`. On `S*` this is harmless
   (`nu_1^nu_2^nu_3 ^ Z_1 ^ Z_2` kills them). On an `F_1`-tuple it is not: `Z_1 = Z_1' + lambda nu_1` gives
   `D = D_3(Z_1', Z_2) + D_2(Z_1', Z_2, Z) + lambda nu_1 ^ Z_2 ^ Z ^ nu_2 ^ nu_3`, a *top-type* term at the 2-plane
   `(Z_2, Z)`; `U_-` mixes `z_{-1}` with `z_{-2}`. These are exactly the "pure equations" of `arc_target` §6.1.
   So only the Levi part `L_1 = (GL_1 x GL_2) . (C*)^3` (7 effective dimensions: it must preserve the line
   `C nu_1` and the plane `<nu_2, nu_3>`) acts on `F_1` with stable zero set.
2. **The slice is too large for its function space.** `dim S^ = 34`. With the Levi part only, a slice
   `cone(V^3)` with `V` of dimension `m` can be transversal only if `7 + 3m >= 34`, i.e. `m >= 9`; even
   granting the full `G'` on a joint `(z_{-2}, z_{-1})` locus (`17 + 3m >= 34`, `m >= 6`; `m = 7` for a margin),
   the space of bidegree-`(3, 1)` functions on the flag cone of a 7-dimensional `V` is the `GL_7`-irreducible
   `S_{(4,4,1)}(V^*)`, of dimension (Weyl formula, hand computation)

       prod_{i<j} (lambda_i - lambda_j + j - i)/(j - i)  for lambda = (4,4,1,0,0,0,0):
       row 1: 1 · 5/2 · 7/3 · 2 · 9/5 · 5/3 = 35;  row 2: 4 · 3 · 7/3 · 2 · 9/5 = 504/5;  row 3: 2 · 3/2 · 4/3 · 5/4 = 5;
       dim = 35 · 504/5 · 5 = 17,640.

   A poised set of 17,640 points at 15 evaluations each is about `2.6 x 10^5` runner evaluations
   (`~36 h`), against 70 rows with the basis. For `m = 9` (Levi only) the number is larger still.
   So the density route trades the unknown basis for a function space 250 times bigger than the
   target: it cannot be made affordable at any slice dimension that is transversal.

**Structural reason, in one sentence.** The degree-12 problem was cheap because the top lives on the
Grassmannian cone `S*` in bidegree `(2,2)` with a 5-dimensional transversal slice; the degree-11 problem
lives on the flag cone `S^` in bidegree `(3,1)`, where the mixing group is smaller (the unipotent part
mixes degrees) and every transversal slice carries a function space of size `>= 17,640`, so only the
`L`-invariant target (`70`) is small — and that target has no explicit basis in the record.

### 5.3 What would change the picture

- An explicit basis of `F^L_{-1}` (the Missing Theorem) makes the identity decidable in about 9 minutes
  (two to three sessions of pilots, or one approved long run).
- `dim F''` (`arc_target` §6.3–6.4): if the pure equations plus Proposition B cut the joint target to
  dimension 2, `rank C = 2` follows for all of `M` without any source-vector evaluation. Its price is
  the same evaluator plus about 100 s of constraint rows (about four wrapped pilots).
- The type mechanism of §4.5(c): if the `s`-parts of the four covariants have a single nonzero type
  component on the flag locus, `z^{[11]} o B` factors through a small space and the identity would follow
  from a rank computation of at most `10 x 2` numbers (cheap; not run).

## 6. Route 2 at the reduced price (pilot 3, written, NOT run)

`analysis/b20_01_p3_flag_rows.py` evaluates, at five seeded points `(Z_1, Z_2, Z) in W'^3` with all 39
coordinates uniform modulo `P` (seed `20260917`; the tuple `(Z_1, Z_2, Z + u nu_1, u nu_2, u nu_3)`, nodes
`u = 1..5`), the degree-11 and degree-12 values of `q_3, q_7, n02` (`15` evaluations per point, `75` in all,
about 40 s), and searches every `3x3` minor with at least two degree-11 rows among the new rows and the
ten inherited rows of `f1_new_point_minor.py` (whose two inherited `2x2` minors `104967`, `171205` are
replayed as a control). Stop rule: the first nonzero minor certifies `rank(C|_U) = 3` (a nonzero modular
minor of integer evaluations is a floor over `Q`; G5' condition 4). If every minor vanishes: because
`F_1^{f}` restricted to the flag locus is a polynomial of degree `<= 9` in the 39 coordinates (Cor. A.2),
a point uniform modulo `P` has `F_1^{f}(p) = 0` with probability `<= 9/P ~ 1.7 x 10^{-5}` when `F_1^{f} != 0`
(Schwartz–Zippel); five concordant generic rows are strong MEASURED evidence, reported as such and never
as a ceiling. This is the first evidence of that kind: the fourteen recorded functionals were at points
with entries in `[-3, 3]` or on the `Sigma = 0` slice, where no such bound applies. The pilot also records
the degree-12 ratios against `101007`, `295818` at generic points. Not run (§2.2); no receipt.

## 7. Claim ledger

| id | statement | label | basis |
|---|---|---|---|
| C1 | `D = -1` in this cell; no positive multiplicity gap is possible in either branch; this slot concerns a necessary source condition only | PROVED / CERTIFIED (inherited) | B20-10 R6–R8 |
| C2 | Theorem A (i)–(v): the degree-11 identity for `f = n02 - alpha q_3 - beta q_7` holds as a polynomial iff `F_1^f = 0` on `W'^3`; five nodes extract `F_1` and the top | PROVED; **producer only** (pilot 2 unrun) | §4.2 |
| C3 | Corollary A.1: a full degree-11 functional costs 15 (or 12) runner evaluations instead of 39 | PROVED (from C2) | §4.2 |
| C4 | Proposition B: `z^{[11]} o tau' = -z^{[11]}`, `z^{[12]} o tau' = z^{[12]}` on `M` | PROVED | §4.3 |
| C5 | Proposition C: `z_{-1} -> F_1^z` is injective on `F^L_{-1}`; `dim V_70 = 70` | PROVED (uses `b_L(11) = 70` PROVED in `arc_target`; FFT for `SL_5` ADOPTED, classical) | §4.4 |
| C6 | A relabelling-sign identity cannot produce the mixed-pairing identity with the recorded residues | PROVED (negative) conditional on the recorded height search to 2000 (`routeA` §5.3, CERTIFIED arithmetic) | §4.5(a) |
| C7 | Isotropic decomposition of `B` on `Lambda^2 A (x) Lambda^2 B`; four-term type formula | PROVED | §4.5(c) |
| C8 | The Missing Theorem as stated in §5.1 suffices to decide the identity with `840–1050` evaluations | PROVED (given C2, C5) | §5.1 |
| C9 | The transversal-slice density method needs a function space of dimension `>= 17,640` on any transversal slice of the flag cone; `U_-` mixes `z_{-1}` with `z_{-2}` | PROVED (hand Weyl-dimension computation; single lineage, **producer only**) | §5.2 |
| C10 | `q_3`, `q_7` definition certificates with ordering hashes (G8) | **OPEN — not emitted** (execution blocked); script ready; literals verified by READ | §3 |
| C11 | Degree-12 rows rank 1 with ratios `101007`, `295818`; relation residues `265391`, `275398` | SAMPLED (inherited; unchanged) | `direct_arc` C2, `arc_target` C3 |
| C12 | `rank(C|_U) in {2, 3}` | OPEN (unchanged) | — |
| C13 | Provenance note: `p6_basis.py` as archived calls the runner with the pairing in the order slot; the values rest on the `s1` and `direct_arc` replays | READ; no label moves | §2.1 |

Superseded: nothing in this report supersedes a prior statement. The "record correction" of
`PRE_AUDIT_FINDINGS.md` §4D/§7.5 and `CURRENT_CLAIM_LEDGER.md` L24 is not carried (B20-10 R9; L21 governs).

## 8. Honest negatives and reopening conditions

1. **No pilot ran; no receipt; no hash; no manifest** (§2.2). Every numerical statement above is either
   inherited (with its pin) or a hand computation. The three scripts are untested code: pilot 1 has a
   `--dry` mode that exercises everything but the runner; pilots 2 and 3 have deadline guards and save
   after every stage/point; a first run may surface a bookkeeping error (sign of `nu_k`, kernel
   construction), which pilot 2's reconstruction checks are designed to catch before anything is claimed.
2. **G8 not discharged.** Phase 2 may not consume the `q_3`/`q_7` certificates until pilot 1 has run and
   the emitted files carry their hashes; this report consumes only the pinned block lists and the literal
   orders (as the four sealed scripts do).
3. **The identity is neither certified nor refuted.** The symmetry search closed one mechanism (C6) and
   opened one testable mechanism (§4.5(c)); the density route is priced out (C9); the exact missing
   theorem is stated (§5.1).
4. **Single lineage.** Theorem A, Proposition C and the counting in §5.2 are producer-only until an
   independent replay (pilot 2 for Theorem A; a second hand computation or a Weyl-dimension routine for
   the 17,640).
5. **Nothing here is an equation, a separation, or a gap** (§0).

Reopening conditions: (a) the Missing Theorem of §5.1 (explicit spanning set of `F^L_{-1}` with a certified
injective 70-point set on the flag locus), then one approved long run of `~1050` evaluations; (b) a
nonzero minor from pilot 3 (closes negatively at once); (c) the type test of §4.5(c) (one pilot: the four
covariants' `t` and `s` parts at a few flag-locus points, 256-vectors kept, type components reported);
(d) `dim F''` as in `arc_target` §6.4 with Proposition B added.

## 9. Resources

Filled from the wrapper receipts `results/logs/b20_01_*_resources.json` and `.pid` (session B20-01c,
default permission mode, 2026-09-17). Wall and peak memory are copied from those files, never typed
from memory; peak memory is `job_memory.peak_job_memory` (Windows job object), shown in MiB to one
decimal alongside the raw byte count.

| run | wrapped | exit | wall | peak memory | purpose | receipt |
|---|---|---|---|---|---|---|
| `b20_01_p1_definitions` | yes (60 s / 512 MiB) | 0 | `6.524 s` | `165.1 MiB` (173121536 B) | G8 certificates; replay of 12 values | `results/logs/b20_01_p1_definitions_resources.json`, `.pid` (pid 28620) |
| `b20_01_p2_reduction` | yes (60 s / 512 MiB) | 0 | `28.887 s` | `393.9 MiB` (412991488 B) | numerical control of Theorem A; `S_3` sign | `results/logs/b20_01_p2_reduction_resources.json`, `.pid` (pid 25520) |
| `b20_01_p3_flag_rows` | yes (60 s / 512 MiB) | 0 | `35.546 s` | `263.1 MiB` (275927040 B) | Route 2 rows at generic points, 75 evaluations | `results/logs/b20_01_p3_flag_rows_resources.json`, `.pid` (pid 47196) |
| unwrapped | no | 0 | `< 5 s` total | — | read-only `git show`, `sha256sum` of pinned inputs, `git status` at session start (§2.1); plus, in session B20-01c, read-only `git rev-parse`/`git status`, `Get-Process`, `Get-FileHash`, and the manifest/seal script | disclosed here |

Wrapped budget used: `70.96 s` of `180 s`; `3` of 3 pilots; the granted pilot-1 retry was **not** used
(no fourth launch). Exit code `0` on all three; **no cap hit** — no run approached either the 60 s wall
cap or the 512 MiB memory cap (largest peak `393.9 MiB`, 77% of cap, in pilot 2). The `--dry`
invocation printed in §10 was **not** run: it is unwrapped, and no unwrapped run of any size is
permitted (ledger §8.5). No source-vector search. No random point sampling beyond pilot 3's five
seeded points.

No process of this session imported from a sealed tree: the loader `analysis/b20_01_pinned.py`
materialises the pinned runner and carrier bytes under `results/b20_01/pinned/` (the runner with one
path line patched; both hashes recorded in every pilot output) and imports from there; sealed
directories were read with `git show` only, so no re-hash at session end is owed (G11).

**G9/G10 compliance, as executed.** Every input each pilot read was fetched by commit and path and
hash-pinned in its output (`inputs` field, full sha256 and byte count) — all three pilots pinned
`p6_basis.json` at `aaee6ec0…` and pilots 1–3 pinned `n02_definition.json` at `ffeead80…`, both at
commit `82633a60893236fab4fbc317df416e1b8a349005`; run names were unique (no `results/logs/b20_01_*`
existed at session start, verified); receipts were written by the wrapper and **none was overwritten**.

## 10. Files, and how to complete the slot outside auto mode

New files (all untracked; hashes NOT computed — the classifier refused `sha256sum`):

| path | role |
|---|---|
| `docs/b20_01_report.md` | this report |
| `analysis/b20_01_pinned.py` | pinned-input loader (git show + sha256 checks; materialises runner/carrier copies) |
| `analysis/b20_01_flag.py` | Theorem A utilities: `nu` matrices, skew coordinates, `GL_5` slice form, `F_k` tuples, node extraction, modular linear algebra |
| `analysis/b20_01_p1_definitions.py` | pilot 1 (G8): emits `results/b20_01/certificates/{q3,q7}_definition.json`, `n02_ordering_hash.json`, `results/b20_01/p1_definitions.json` |
| `analysis/b20_01_p2_reduction.py` | pilot 2: Theorem A control at P6 point 0 → `results/b20_01/p2_reduction.json` |
| `analysis/b20_01_p3_flag_rows.py` | pilot 3: Route 2 rows at generic points → `results/b20_01/p3_flag_rows.json` |
| `results/b20_01/certificates/` | created, empty until pilot 1 runs |

Commands (from this worktree, default permission mode, one numerical job at a time across the batch —
check `Get-Process python` and the sibling worktrees' `results/logs/b20_0*_*.pid` first):

```
$env:PYTHONDONTWRITEBYTECODE = "1"
python analysis/b20_01_p1_definitions.py --dry
python ../B15-02/analysis/b15_bound.py --seconds 60 --memory-mb 512 --name b20_01_p1_definitions --slot 01 analysis/b20_01_p1_definitions.py
python ../B15-02/analysis/b15_bound.py --seconds 60 --memory-mb 512 --name b20_01_p2_reduction  --slot 01 analysis/b20_01_p2_reduction.py
python ../B15-02/analysis/b15_bound.py --seconds 60 --memory-mb 512 --name b20_01_p3_flag_rows  --slot 01 analysis/b20_01_p3_flag_rows.py
Get-ChildItem -Recurse results/b20_01, analysis/b20_01_*.py, docs/b20_01_report.md | Get-FileHash -Algorithm SHA256
```

Expected outcomes: pilot 1 — all checks `true`, two certificates with 64-hex `ordering_hash` fields;
pilot 2 — `theorem_A_passed: true`, `top_equal_across_k` all `true`, `S3_control[*].sign = -1`; pilot 3 —
either `STOP_nonzero_minor` (the diagnostic closes: `rank(C|_U) = 3`) or five concordant rows with
`relation_residual_d11 = 0` and degree-12 ratios `101007`, `295818`. If pilot 2 fails, Theorem A's
bookkeeping (not its proof) is the first suspect: check `sign_convention_reconstruction` and the `nu`
sign in `b20_01_flag.nu_matrices` against `b18_02_carrier.adapted_scale_u`.

After the runs, the manifest to seal is the table above plus the emitted certificates and receipts;
the report's §9 table must then be filled from the receipts, never typed.

## 11. Completion log (session B20-01c, 2026-09-17)

This section is written by the execution session that ran the three pilots §10 specifies. It changes
nothing in §§0–8; §9 was filled from the receipts. Where a pilot result contradicts a §4–§7 claim, the
claim is **left exactly as written** and the contradiction is recorded here (item C1), with the ledger
row standing and a pointer to this section.

### 11.1 Session start state

| item | value |
|---|---|
| worktree | `C:\Users\swami\Projects\gct-gpt\work\batch15_workers\B15-01` |
| branch | `b15-01-ci159` |
| `git rev-parse HEAD` | `6b16151328d38dc0ce39bcfab51e83459a035d79` (matches the brief) |
| `git status --porcelain` | no tracked modifications; 10389 untracked entries — B20-01's files (`docs/b20_01_report.md`, `analysis/b20_01_*.py`, `results/b20_01/`) plus pre-existing B15-era residue |
| `results/b20_01/` at start | `certificates/` and `pinned/` present, **both empty** (0 files under `results/b20_01/`) |
| `results/logs/b20_01_*` at start | none — run names unique (G10) |
| git usage this session | read-only throughout (`rev-parse`, `status`); **no commit, no push, no stash** |

**Concurrency check (step 2).** `Get-Process python*` returned nothing. Six sibling `.pid` files were
present — `..\B15-02\results\logs\{b20_02b_p1_d8_blockwise, b20_02_p1r_koszul5_k3_12,
b20_02_p1_koszul5_k3_10, b20_02_p3_price16_and_koszul5_k3_12}.pid` and
`..\B15-10\results\logs\{b20_10_p1_independent_invariant, b20_10_p2_spot_replay_certificates}.pid` —
holding pids 16276, 32200, 45784, 1680, 2136, 39396. Each was probed individually with `Get-Process
-Id`: **all six dead**, i.e. the files are stale residue, not live jobs. One numerical job at a time
across the batch was therefore honoured; the three pilots also ran strictly sequentially.

### 11.2 The launches

`$env:PYTHONDONTWRITEBYTECODE = "1"` was set in each launch shell. Every launch used the wrapper
`python ..\B15-02\analysis\b15_bound.py --seconds 60 --memory-mb 512 --name <name> --slot 01 <script>`.
**Three launches; no fourth.** Timestamps are local (UTC−04:00); the wrapper's own `started_utc` is
in the receipts.

| # | run name | launched | returned | exit | wall (receipt) |
|---|---|---|---|---|---|
| 1 | `b20_01_p1_definitions` | 2026-09-17T17:54:26.759−04:00 | 17:54:33.954−04:00 | 0 | `6.524 s` |
| 2 | `b20_01_p2_reduction` | 2026-09-17T17:54:41.446−04:00 | 17:55:11.000−04:00 | 0 | `28.887 s` |
| 3 | `b20_01_p3_flag_rows` | 2026-09-17T17:55:26.491−04:00 | 17:56:02.720−04:00 | 0 | `35.546 s` |

The granted **pilot-1 retry was not used**: pilot 1 passed on its first wrapped launch, so no fix was
made to `b20_01_p1_definitions.py` and no fourth launch exists. All five `analysis/b20_01_*.py` files
are byte-identical to what session B20-01 wrote (no edit was made to any of them this session).

### 11.3 Pilot 1 — G8: **discharged**

Headline, copied from `results/b20_01/p1_definitions.json` (`status: "done"`):

- `four_literals_agree: true` — the orders `[[0,1,2,3],[0,2,1,3]]` agree across all four pinned scripts
  (`s1_screen_arc.py`, `s2_certify_n02_and_new.py`, `s3_full_forbidden_rows.py`, `f1_new_point_minor.py`).
- `regeneration`: `q3` and `q7` each `pi_equal: true`, `rho_equal: true`, `pairing_equal: true`;
  `P6_points_equal: true`.
- `hand_plan_orders_match_literals: true`.
- `n02_definition_vs_candidates_selected`: `pi_equal: true`, `rho_equal: true`, `order_equal: true`;
  `hand_plan_recomputed: [[0,2,1,3],[0,2,1,3]]`.
- `replay` (12 evaluations, `eval_wall_s: 5.440`): `q3` `P6_points_0_to_4 = [260975, 509003, 336756,
  260012, 342025]` = sealed, `P6_match: true`; `P7_S0_point0_t0 = 185448` = sealed, `P7_match: true`.
  `q7` `P6_points_0_to_4 = [301718, 423302, 275526, 317892, 384]` = sealed, `P6_match: true`;
  `P7_S0_point0_t0 = 288291` = sealed, `P7_match: true`.

Three certificates emitted, each carrying a 64-hex `ordering_hash`:

| certificate | `ordering_hash` |
|---|---|
| `results/b20_01/certificates/q3_definition.json` | `ae832e3d7e1dc80befba2e79bd0aa5bc1abe84a2f0b0a6cc9d3c4cdef07f4060` |
| `results/b20_01/certificates/q7_definition.json` | `17b7d324c5af5743e4237ec833556f18b1cf10f1ef430040bea06ece5a4fb17b` |
| `results/b20_01/certificates/n02_ordering_hash.json` | `61505bd5a571ace8cfb67b6ae79c66effc5d008ddd9e7794088ee5cf625408b4` |

Every check in the pilot is `true` and every replayed value equals its sealed counterpart. **G8 is
discharged** on the terms §3 sets.

### 11.4 Pilot 2 — **did not pass**; recorded, not repaired

`results/b20_01/p2_reduction.json`, `status: "done"`, exit 0, 60 evaluations — but
**`theorem_A_passed: false`**. Per the session brief, the failure was **not** fixed and **not**
re-run. What passed and what failed, copied from the JSON:

**Passed:**
- `sign_convention_reconstruction: true`
- `top_equal_across_k`: `q3: true`, `q7: true`, `n02: true`
- `S3_control` — all three of `q3`, `q7`, `n02` give `equal_up_to_sign: true` and **`sign = -1`**, the
  expected value, with `top_at_permuted_point` equal to `top` in each case (`462650`, `139666`,
  `319220`).

**Failed** — `theorem_A_passed` is the conjunction of the degree-11 and degree-12 reconstructions
(`analysis/b20_01_p2_reduction.py:72`), and **all six comparisons disagree**:

| family | quantity | computed | sealed |
|---|---|---|---|
| deg 11 | `q3` `det_g4_times_sum_F` | `300999` | `86170` |
| deg 11 | `q7` `det_g4_times_sum_F` | `497738` | `71919` |
| deg 11 | `n02` `det_g4_times_sum_F` | `126141` | `226580` |
| deg 12 | `q3` `det_g4_times_top` | `491631` | `376209` |
| deg 12 | `q7` `det_g4_times_top` | `329212` | `469277` |
| deg 12 | `n02` `det_g4_times_top` | `279654` | `41046` |

`sealed_rows_source: "final_arc_diagnostic/code/f1_new_point_minor.py INH full_P6pt0
(s3_full_forbidden_rows.json)"`. Slice form recorded: `det_g_mod_P = 199728`, `det_g4 = 471465`.

**Open item for the integrator (O1).** §10's diagnostic hint is that Theorem A's *bookkeeping*, not
its proof, is the first suspect: check `sign_convention_reconstruction` and the `nu` sign in
`b20_01_flag.nu_matrices` against `b18_02_carrier.adapted_scale_u`. The run **partly discharges the
first half of that hint**: `sign_convention_reconstruction` came back `true`, and the `S_3` control
returned the expected `sign = -1` on all three functionals, so the sign convention as the pilot
reconstructs it is not visibly the fault. The unexamined half is the `nu` sign against
`adapted_scale_u`, and, beyond the hint, the `det_g4` normalisation itself: the failure is a scalar
mismatch in *both* degree families simultaneously while `top_equal_across_k` holds across `k`, which
is the shape of a single wrong normalising factor rather than a wrong functional. That reading is a
**conjecture stated for the integrator, not a result of this session** — no run tested it, and no
change was made to any script to test it.

### 11.5 Pilot 3 — ran; the **second** §10 branch landed

Pilot 3 was run after pilot 2's failure only because it does not consume pilot 2's output: by
inspection of `analysis/b20_01_p3_flag_rows.py`, its only reads are the pinned `p6_basis.json` and
`n02_definition.json` (via `b20_01_pinned`), and its only write is `results/b20_01/p3_flag_rows.json`.
There is no path from `p2_reduction.json` into it.

`results/b20_01/p3_flag_rows.json`, `status: "done"`, exit 0, 75 evaluations, `eval_wall_s: 33.699`.

- Verdict, verbatim: `"no nonzero 3x3 minor among 20 rows; 5 new degree-11 functionals concordant
  (MEASURED only, not a ceiling)"`.
- `minors`: `rows: 20`, `tested_with_two_d11: 570`, **`first_nonzero: null`**, `rank_mod_P_all_rows: 2`,
  `rank_mod_P_d11_rows: 2`.
- Inherited controls reproduced: `inherited_2x2_minors` `S0_P7pt0 = 104967`, `full_P6pt0 = 171205`,
  both equal to `expect`; all ten `inherited_relation_residuals` are `0`.
- All five seeded points: `relation_residual_d11 = 0` **and** `relation_residual_d12 = 0`, with
  `d12_ratios` `q7_over_q3 = 101007` and `n02_over_q3 = 295818` at **every** point — exactly the two
  degree-12 ratios §10 names.

So the outcome is §10's **second** branch: five concordant rows, not `STOP_nonzero_minor`. The
negative diagnostic did **not** close: `rank(C|_U) = 2`, not the `3` that a `STOP_nonzero_minor` would
have reported. This is recorded as it landed. It is a **measurement at 20 rows and five seeded
points**, not a ceiling and not a proof that no nonzero 3×3 minor exists — the pilot's own verdict
string says so, and nothing here upgrades it.

### 11.6 Contradictions with §§4–7

**C1 — pilot 2 vs. Theorem A's numerical control.** `theorem_A_passed: false` (§11.4) contradicts the
expected outcome §10 states for pilot 2 and sits against the Theorem A material in §4 and its ledger
row in §7. Per the brief, **no §4–§7 text was edited**: the claim and the ledger row stand exactly as
session B20-01 wrote them, and this item is the pointer. What the run establishes is narrow and
negative: the pilot's *numerical reconstruction* of the degree-11 and degree-12 identities disagrees
with the sealed values by a scalar in all six comparisons. It does **not** establish that Theorem A is
false — the first suspect named in §10 is bookkeeping, and §11.4's evidence (`top_equal_across_k` true
across `k`, `sign_convention_reconstruction` true, `S_3` sign `-1`) is consistent with bookkeeping
rather than with the theorem. The integrator decides; this session did not.

No other pilot result contradicts §§0–8. Pilot 1 confirms §3's specification in full. Pilot 3's
outcome is one of the two branches §6/§10 anticipate.

### 11.7 Hash table

`Get-FileHash -Algorithm SHA256`, taken after §9 and §11 were final. **The report does not name its own
hash**; `docs/b20_01_report.md` is bound in `results/b20_01/MANIFEST.json` only. `MANIFEST.json` and
`SEAL_LOG.txt` were written after this table and are, necessarily, not bound by themselves — the
table below is the complete pre-seal state of the three hashed sets.

| path | sha256 | bytes |
|---|---|---|
| `results/b20_01/p1_definitions.json` | `e7e49a19f38d6729c58c560ffd0aea26dcf9141c19213009ab5dc1d3708fd4e6` | 5920 |
| `results/b20_01/p2_reduction.json` | `6aa3e283f5d0bf39515656dc16375104530a8d651d2b809973c8028083beb812` | 7014 |
| `results/b20_01/p3_flag_rows.json` | `73c3be3c0789d26001953f940792c9086ce19fc72d758566f5bea2c86ece66ee` | 9237 |
| `results/b20_01/certificates/q3_definition.json` | `ac93ff59113a1aca83a3a8a2d5a2cd90b2de216be70c793ea5f242c887e8428e` | 13673 |
| `results/b20_01/certificates/q7_definition.json` | `07d066b8f6aada7472e892801cbfd6f1a2708a3d592e18592d9996341af3a252` | 13664 |
| `results/b20_01/certificates/n02_ordering_hash.json` | `34900ea600da8b9a20535988f0a0a6cd901d866cd90ae74699e2ba60de845166` | 1496 |
| `results/b20_01/pinned/b18_02_carrier.py` | `8670040e2a980026563d1a265f8d32e5749a47f61a0c100e82be9ffa0c75a154` | 23388 |
| `results/b20_01/pinned/paired_runner.py` | `e7ba4ff7ab676a0fb259dd662397d3a52bdbbcc12604f16e292fe005fce210fc` | 4987 |
| `analysis/b20_01_flag.py` | `3236c78700872975497c8ef37d5eefde17f617a0dfdac302d6558c85454ae27a` | 6367 |
| `analysis/b20_01_p1_definitions.py` | `52664d4dfd50b2d35e9fccaeb53cf0b84d0da7550d1e62624d208da15ee4b848` | 11489 |
| `analysis/b20_01_p2_reduction.py` | `5124cf7d928b2f81122438b39af5418c80d9d80fe5687db20a152d85fdbbac90` | 6136 |
| `analysis/b20_01_p3_flag_rows.py` | `924537f74a0a45d5a69ad1c078193a4eed0c0aba2161386468026fad6f980fed` | 6530 |
| `analysis/b20_01_pinned.py` | `a7e164e369ec4f9b49f886595f95c4274f0b52a5326ea03df06947cbbc7f74a1` | 3877 |
| `results/logs/b20_01_p1_definitions_resources.json` | `2347d94015497c93fc40379bb79f508cdc381cac5576dd4e8e704bbaf887c8a0` | 813 |
| `results/logs/b20_01_p1_definitions.pid` | `6ecac95a2d8aa9e62a5806244c78f877e96961e3b156c30850da19a5fe1b7df7` | 7 |
| `results/logs/b20_01_p2_reduction_resources.json` | `e09a33fdd29c120e38bd4b25d78830700a4e612b18164403728a1a005e59aca5` | 813 |
| `results/logs/b20_01_p2_reduction.pid` | `e2b1bb0038d02bad3ca27d5b51b64dac861ba29ffd193c14d8cfcd7d30b6169a` | 7 |
| `results/logs/b20_01_p3_flag_rows_resources.json` | `40722fef633d4c0efa23749e135bd7a4c30122df0eaa452e7e7977637ff4f226` | 814 |
| `results/logs/b20_01_p3_flag_rows.pid` | `1d5da42fa7ae17cd43d826bac0a3fe8fa7191a75fb3e2f45a69d728b16aac7b8` | 7 |

`results/b20_01/pinned/paired_runner.py` hashes to `e7ba4ff7…`, which is exactly the
`runner_patched_sha256` every pilot recorded in its `code_pins` — the materialised copy and the pilots'
own record of it agree. Sealed trees were read with `git show` only and were **not** re-hashed (G11).

### 11.8 Deviations

| # | deviation | reason |
|---|---|---|
| D1 | The unwrapped `python analysis/b20_01_p1_definitions.py --dry` printed in §10 was **not** run. | Ledger §8.5: no unwrapped run of any size. The session brief directs the skip. §10's command block is left as written. |
| D2 | Pilot 2 failed and was **not** fixed or re-run. | Brief: record the failure and the §10 hint as an open item (O1, §11.4) for the integrator. |
| D3 | Pilot 3 was run despite pilot 2's failure. | Permitted because pilot 3 does not depend on pilot 2's output; the independence was checked by inspection before launching (§11.5). |
| D4 | The granted pilot-1 retry was not used; only three wrapped launches exist. | Pilot 1 passed first time. |
| D5 | `MANIFEST.json` binds the six `results/logs/b20_01_*` receipts in addition to the step-4 set. | §10: "the manifest to seal is the table above plus the emitted certificates **and receipts**". |
| D6 | `MANIFEST.json` and `SEAL_LOG.txt` are not bound by `MANIFEST.json`. | A manifest cannot bind itself or a log written after it; stated in both files. |
| D7 | §§0–8 unchanged; §9 rewritten from receipts; §11 added. | The brief. Nothing in §§0–8 was edited, including where C1 sits against it. |
| D8 | The seal script that writes `MANIFEST.json`/`SEAL_LOG.txt` lives in this session's scratchpad, **not** in `analysis/`. | A `analysis/b20_01_seal.py` would fall inside the `analysis/b20_01_*.py` hash set of §11.7 and could not hash itself. Its own sha256 and full text-length are recorded in `SEAL_LOG.txt` and in the manifest's `generator` field. |
