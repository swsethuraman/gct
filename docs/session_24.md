# Session 24 — is the deficit a separation obstruction?

Branch `s24-obstruction`.  2026-08-31.  Cloud container, fresh clone of the
public GitHub repo (tip `5cdc29c` at clone).  This session did **not** own the
durable folder and wrote nothing to it (rule 9).  Per the changed
record-keeping instruction, nothing was appended to `PROJECT_NOTES.md` or
`docs/boundary_deficit.html`.

Deliverables: `results/PREREG_s24.md` (commit `99b0c7b`, before any
computation), `docs/obstruction_power.md`, this file.

## 1. What was asked and what came back

Asked: can the deficit part of

    mult_lam(B) - mult_lam(A) = [m_B - m_A] - [def_B - def_A]

ever exceed the Peter–Weyl part in the direction that gives an obstruction?

Came back:

- **Lemma 1** (decomposition, with hypotheses) and **Remark 3**: the "strong
  negative theorem" of task 4 is not available — the inequality it proposes is
  *equivalent* to the absence of a multiplicity obstruction, hence not a
  theorem about the deficit at all.  The honest negative has to be a census
  plus a structural obstruction plus a localisation, and that is what was done.
- **Theorem 2** (conductor window): the deficit part can only act at ray index
  `k < max(c_A, c_B)`; beyond that `D = P` exactly.  Proved; verified in World A.
- **Proposition 3**: an explicit deficit-driven obstruction in `Sym^8 C^2` at
  `lam = (26,6)`, `delta = 4`.  Verified four ways.  It works by making the
  Peter–Weyl side vanish identically (equal stabilisers) — reported as a
  negative dressed as a positive, per the brief's task 3.
- **Proposition 4** (hypersurface blindness) — the reason World A and World B
  could not have answered the question either way.
- **Theorem 5**: complete World A census, 0 deficit-driven obstructions in 9408
  cells; World B pair likewise, 0 in the range tested.
- A quantitative mechanism: `def` tracks `m` inversely with `|H|`, so `Def` and
  `P` are positively correlated and their difference is not a new signal.
- Recommendation: do **not** engineer `n = 4` for this purpose; run the two
  cheap steps (Peter–Weyl branching pre-screen; the *permanent's* deficit at
  `n = m = 3`) that would make the question live or dead.

## 2. Pre-registration outcomes

| | prediction | outcome |
|---|---|---|
| H1 | no deficit-driven obstruction in World A | **CONFIRMED**, `delta <= 14`, all 42 ordered pairs, 9408 cells |
| H2 | `mult_D = mult_{A_c}` for all `lam`; `Def = P` for that pair | **CONFIRMED** for the conclusion; the stated *reason* was **WRONG** — see §4 |
| H3 | conductor window | **CONFIRMED** (and proved as Theorem 2) |
| H4 | `def_Q = 0` identically; `def_tau = [b=1]` | `def_tau` **CONFIRMED**; `def_Q = 0` **REFUTED** — see §4 |
| H5 | Theorem 2.1 reproduced by two independent routes | **CONFIRMED**, `delta <= 14` |
| H6 | a witness, if found, would rely on *non-conjugate* stabilisers and on one closure being normal | **REFUTED, both clauses.** The witness relies on the stabilisers being *literally equal*, and both closures are deficient |
| H7 | no deficit-driven obstruction in World B | **CONFIRMED** for the pair tested, `delta <= 8` |

Two clean refutations (H4a, H6) and one wrong-reason-right-answer (H2), all
kept in the record.

## 3. Verification protocol — every number twice

| quantity | route 1 | route 2 | route 3 / 4 |
|---|---|---|---|
| `Sym^delta(Sym^4 C^2)` multiplicities | monomial weight count + `GL_2` differencing | — | (used as the base of everything else) |
| `mult` for hypersurface closures | Koszul quotient `C[W]/(F)` | — | |
| `mult` for `Gam`, `tau`, `Q` | exact substitution rank (Bareiss over `Z`) | closed forms | general orbit tool, `delta <= 5` |
| `m` for `H_{Jz}` (order 32) | eigenbasis count `N(a,b)` | ray stabilisation of `mult` | exact character average in `Q(zeta_8)` |
| `m` for `H_{A_c}` (order 16) | eigenbasis count | ray stabilisation | exact character average |
| `m` for `H_D` (order 8) | eigenbasis count | exact character average | (`def >= 0` gate) |
| `def_{J=0}` | `m - mult` from the above | paper Thm 2.1 closed form `max(0, floor((a-3b)/8))` | agreement for all `delta <= 14` |
| `def_tau` | substitution rank | paper's non-normality remark (one `S_(4δ-1,1)` per degree) | |
| World B `def_{S=0}` | `GL_3` plethysm + Weyl alternation, `m` by ray | **paper's 254 deficit-positive weights through `delta = 10` reproduced exactly** | |
| `Sym^8` witness `mult` | Bareiss over `Z` | mod `2^31-1` | mod `10^9+7`; sympy `Matrix.rank` over `Q` |
| `Sym^8` witness `m_K` (order 64) | eigenbasis count | exact character average over all 64 elements | |

**Global gates, both passed after the fixes of §4:**
`def >= 0` for every closure at every weight (1568 World A entries, all World B
weights `delta <= 10`); and **no multiplicity obstruction may violate a true
containment** — checked against the verified orbit poset.

Conductor-window data (World A, `I`-ray of `{J=0}`, entries `(m, def)`):

    lam=(11,1) d= 3 : (1,1) (1,0) (1,0) (1,0) (1,0) ...
    lam=(18,2) d= 5 : (2,1) (2,0) (2,0) (2,0) (2,0) ...
    lam=(25,3) d= 7 : (3,2) (3,1) (3,0) (3,0) (3,0) ...
    lam=(24,0) d= 6 : (4,3) (4,2) (4,1) (4,0) (4,0) ...

`m` constant along the ray, `def` falling by at most one per step to 0 and
staying — exactly Theorem 2.

## 4. Two errors caught in-session, and what caught them

**(a) `C[{q^2}]` was wrong.**  I asserted `C[Q]_delta = Sym^{2delta}(Sym^2 V)`,
which gives `mult = [b even]` and `def_Q = 0`.  The containment gate flagged
it: `Q ⊆ D` yet the tables reported `mult_Q(2,2) = 1 > 0 = mult_D(2,2)` at
`delta = 1`.  The exact substitution rank shows `C[Q]_1` is the 5-dimensional
image of `W^*`, not the 6-dimensional `Sym^2(Sym^2 V)`: the cone `{q^2}` is the
Veronese `P^2 → P^5` composed with a linear projection, and is **not
projectively normal**.  So `def_Q = 1` at `lam = (2,2)`, `delta = 1`, and 0
elsewhere for `delta <= 10`.  **H4a refuted.**

**(b) `|H_D|` was wrong.**  I wrote `H_D = mu_4 · Id` of order 4, on the
grounds that the `PGL_2`-stabiliser of a marked triple is trivial.  It is not:
the unique Möbius map fixing the double root and exchanging the two simple
roots is an involution, so the `PGL_2`-stabiliser has order 2 and
`|H_D| = 8`.  In the model `x^2(x^2 - y^2)` that involution is `diag(-1,1)`, so
`H_D = { diag(al,be) : al^4 = 1, (al be)^2 = 1 }` — exactly the diagonal part of
`H_{A_c}`, whence `H_{A_c} = H_D ⋊ S_2`.  Caught by re-deriving the `PGL_2`
stabiliser while designing the Proposition 3 construction, not by a gate.  The
error inflated `m_D` by roughly a factor of two and could have *hidden*
deficit-driven obstructions with `B = D`; all tables were rebuilt and the
census re-run.  Conclusions unchanged.

Both errors were in hand-derived closed forms, both were caught, and the
lesson is the one rule 8 already states in another form: **a screen that only
checks internal consistency does not see a wrong group.**  The containment gate
is the cheap external check and should be standard in any future
multiplicity work here.

## 5. Files added

    results/PREREG_s24.md          pre-registration (committed first)
    docs/obstruction_power.md      the mathematical deliverable
    docs/session_24.md             this record
    analysis/wk5_s24_worldA.py     World A tables (mult, m, def) for 7 closures
    analysis/wk5_s24_param.py      exact substitution rank for Gam, tau, Q
    analysis/wk5_s24_orbit.py      general exact orbit-ring tool (binary forms)
    analysis/wk5_s24_char.py       exact character averaging in Q(zeta_8)
    analysis/wk5_s24_checks.py     the validation gates
    analysis/wk5_s24_search.py     the pair search
    analysis/wk5_s24_stats.py      what the deficit part does
    analysis/wk5_s24_mech.py       co-monotonicity + conductor window
    analysis/wk5_s24_sign.py       sign/magnitude analysis
    analysis/wk5_s24_sym8.py       the Sym^8 witness
    analysis/wk5_s24_verify8.py    four-route verification of the witness
    analysis/wk5_s24_worldB.py     GL_3 plethysm, World B calibration + pair

All scripts are pure Python with exact integer / `Fraction` / sympy-rational
arithmetic; no engine runs, no grind, nothing that needed a checkpoint.  Total
runtime of the whole pipeline is a few minutes.

## 6. Open, and what a successor should do first

1. **The Peter–Weyl pre-screen for `per`/`det`.**  Weights with
   `m_{per^pad}(lam) <= m_{det}(lam)`.  Pure branching, no closure geometry, and
   it decides whether the whole question is live.  Nothing in this programme
   requires `n = 4` to attempt it.
2. **The permanent's deficit at `n = m = 3`.**  The determinant's is known; the
   difference is what separates, and the other half has never been computed.
   `per_3` in `Sym^3 C^9` is a labelled model problem, not GCT — say so — but
   it is the first place where `Def` itself becomes a measured quantity rather
   than a formal one.
3. **Codimension.**  Proposition 4 says the phenomenon needs codimension `> 1`.
   The programme's worlds are hypersurface worlds.  A third world of higher
   codimension with computable rings — e.g. the `Sym^8 C^2` pencil of
   Proposition 3, where everything is exact and cheap — would be the honest
   test-bed, and would say whether the `Sym^8` witness is isolated or the tip
   of a family.
4. **Is `c` really small for determinants?**  Theorem 2 makes the conductor the
   width of the window in which the deficit can act.  `c((2,2,2),2) = 1` is one
   data point.  A second determinant conductor, at any weight, is worth more to
   this question than another degree of `E(det_3)`.

## 7. Delivery

Push to `origin` was attempted from this container.  The branch is
`s24-obstruction`; if the git proxy refuses, the branch is delivered as a git
bundle alongside this file, exactly as session 21 was.  Swami merges.
