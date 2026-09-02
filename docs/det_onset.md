# The onset of `I(D_5^det)` — the occurrence route is silent; δ=8 empty in reach

Session 38, branch `s38-onset`, 2026-09-02. Clone tip `5367c75` (s35 review);
ancestry gate `git merge-base --is-ancestor c02cee8 HEAD` passes and
`docs/s35_review.md` present. Pre-registration `results/PREREG_s38.md`, committed
before any computation. No session-38 collision in the record.

**A required-reading dependency is missing and is flagged, not papered over.**
The brief names `docs/s36_prompt.md` for a stabiliser reduction lemma to be
"implemented independently." Neither that file nor any session-36/37 material
exists in the repository (latest prompt on record is `docs/s35_prompt.md`; no
s36/s37 commit or code). There is thus no shared spec and no sibling
implementation. Handling, per `PREREG_s38.md` §0: the *rectangular* reduction
that is on the record (`docs/s33_review.md` §2) is reimplemented and re-validated
here; for general length-5 weights that argument does not port, and rather than
invent an uncertified reduction the Phase-1 measurements use the exact
**unreduced** pipeline within its memory reach. Nothing banked is unproved or
uncertified.

---

## 0. Verdict

1. **The occurrence route is silent across the whole window it can see.** Of the
   2585 length-5 cells at δ=5–10 (exhaustive) **not one has `a > m_det`**, and
   δ=11, 12 are clean at both fire-risk extremes (§2). So the onset of
   `I(D_5^det)`, wherever it lies, is a **genuine
   multiplicity phenomenon** (`mult_det < a ≤ m_det`), invisible to arithmetic
   and requiring a rank to detect. Pre-registered P2 (silence expected) is
   **confirmed**.
2. **δ=8 is empty on every reachable cell measured.** All 29 length-5 cells at
   δ=8 with `N_S ≤ 5531` measure `mult_det = a` (`det_units = 0`), two primes,
   each a rank-attains-`a` certificate. No bite. 14 further reachable cells
   (`5531 < N_S ≤ 9000`) and 392 cells past the unreduced memory wall
   (`N_S > 9000`) were not measured (named in §3).
3. **Validation battery passes** (P1): the K1 witness, the rectangular `D_4^det`
   ladder rungs 4–8 (both odd-block sign tests), and the nine banked δ=6 length-5
   cells all reproduce on this container.

**The window is left at `[8, 405]`.** The floor is not raised: δ=8 is excluded
only on the measured corner (27 of 435 cells), so the onset could still be 8 on
an unreached cell. The ceiling (405, the discriminant; s35's labelled ~300) is
untouched. What the session *does* pin is the **character** of the onset: not an
occurrence obstruction, but a multiplicity drop.

---

## 1. The object and the identification

`D_5^det = closure{ det_4(s_1 A_1 + … + s_5 A_5) } ⊆ Sym^4 C^5`, the quinary
quartics with a 4×4 linear determinantal representation. `dim Sym^4 C^5 = 70`,
`dim D_5^det = 50` (`docs/n4_gate.md` §4: Jacobian rank `16·5 − 30`), **codim 20**
— a 20-nodal non-factorial locus in miniature (`docs/theory_directions.md` §C).

By the length reduction (`docs/isotypic_rank.md` Prop. 5 / Thm 6′), for
`ell(lam)=5`,

    mult_lam C[closure(GL_16·det_4)]_delta = mult of S_lam(C^5) in C[D_5^det]_delta .

`I(D_5^det)` is concentrated at **length exactly 5** in the window: length ≤3
sees only ternary quartics (`det_4|_{3-plane}` dense), and length 4 sees
`D_4^det`, whose ideal is principal of degree `e = 320112` — far above 405
(`docs/e4_hunt.md`). So the onset lives at `ell=5`, and the screen is over
`ell=5` weights.

Two arithmetic counts bound every cell (`mult_det ≤ min(a, m_det)`):
`a(lam,δ) = ⟨h_δ[h_4], s_lam⟩` (ambient plethysm) and `m_det(lam)` = the
symmetric rectangular Kronecker coefficient (rectangle `(δ^4)`, `N=4δ`; the
Peter–Weyl bound). A cell with `a > m_det` would carry an equation with no
geometry — the s28 `n=3` mechanism.

---

## 2. Phase 0 — the occurrence screen (the headline)

Full table and method: `results/occurrence_screen.md`; data
`results/occurrence_screen.csv`, `results/screen_d1{0,1,2}*.csv`; code
`analysis/wk9_s38_screen.py`.

| δ | cells (a≥1) | `a>m_det` | largest-`a` cell (`a`/`m_det`) | tightest (`a`/`m_det`/margin) |
|---|---|---|---|---|
| 5 | 23 | **0** | (4,4,4,4,4) 1/5 | (4,4,4,4,4) 1/5/**4** |
| 6 | 105 | **0** | (11,6,4,2,1) 7/375 | (16,2,2,2,2) 1/8/7 |
| 7 | 239 | **0** | (12,8,5,2,1) 26/1529 | (20,2,2,2,2) 1/8/7 |
| 8 | 435 | **0** | (12,8,6,4,2) 109/27257 | (24,2,2,2,2) 1/8/7 |
| 9 | 708 | **0** | (14,10,6,4,2) 437/104544 | (28,2,2,2,2) 1/8/7 |
| 10 | 1075 | **0** | (16,11,7,4,2) 1421/389644 | (32,2,2,2,2) 1/8/7 |
| 11 | 1602 (spot) | **0** | balanced a≪m_det | (36,2,2,2,2) 1/8/7 |
| 12 | 1900+ (spot) | **0** | balanced a≪m_det | (40,2,2,2,2) 1/8/7 |

δ=5–10 are **exhaustive** (2585 cells); δ=11,12 are **spot-checked at both
fire-risk extremes** (full `m_det` enumeration over partitions of 44,48 exceeded
the character budget — the brief's "as far as budget allows"). Peaked end: the
`(4δ−8,2,2,2,2)` family holds `a=1, m_det=8` at 11,12, and the more-peaked
`m_det∈{0,1}` cells have `a=0` (no `n=3`-style `a≥1,m_det=0` fire). Balanced end:
`a` in tens–hundreds vs `m_det` in thousands+, as at δ≤10.

**`m_det` outruns `a` everywhere and the gap widens** — at the largest-`a` cell
of each degree the margin explodes (δ=10: 1421 vs 389644). The tightest cell is
a stable family `(4δ−8, 2,2,2,2)`, `a=1`, `m_det=8`, **margin 7 at every δ≥6**;
it never closes. The single closest approach anywhere is `(4,4,4,4,4)` at δ=5
(margin 4). δ=5,6,7 zero fires ⇒ the emptiness through 7 is a multiplicity fact,
not occurrence — the required consistency check.

**Regime note (P2's demand).** The `n=3` mirror "fired at δ=10" but at lengths
8,9 by the degenerate `m_det=0` route — a different length regime; at length 5
the `n=3` route was silent too. That precedent does not transfer, and this
screen's silence is the honest, pre-registered finding.

---

## 3. Phase 1 — validation, then δ=8 rank measurements

**Validation battery (P1) — PASS** (`results/s38_validation.md`):

- K1 witness (binary quartics `closure{l^3 m}`, `lam=(4,4)`, δ=2): `a=1`,
  `mult=0`, kernel `(12,−3,1)` both primes — the corrected raising rule.
- Rectangular `D_4^det` ladder rungs 4–8: `a = 1,0,1,1,3`, `mult_det = 1,–,1,1,3`,
  `rank(R)=n_chi−a`, and the **odd-block swap-fixed rows cancel exactly** at the
  odd rungs 5,7. All match `docs/n4_gate.md` §5 / `results/e4_ledger.md`.
- The nine banked δ=6 length-5 cells (`docs/n4_gate.md` §6): `mult_det = a` at
  each, unreduced pipeline, `N_S` matching the record.

**δ=8 census** (`results/census_d8.csv`, `analysis/wk9_s38_census.py`): 435
length-5 cells with `a≥1`; capped `N_S` counter (verified against `monomials()`).
**43 are reachable unreduced** (`N_S ≤ 9000`, the `7.5e-8·N_S²` GB wall).

**δ=8 measurements** (`results/onset_ledger.md`): 29 reachable cells with
`N_S ≤ 5531`, ascending in `N_S` — **every one `mult_det = a`, `det_units = 0`**,
two primes, `a` matched to the plethysm, `rank(R)=N_S−a` asserted (each a
certificate, not a sample). No bite. Spanning `a = 1..9`, `m_det = 8..299`.

Not measured: 14 reachable cells `5531 < N_S ≤ 9000` (unreduced `O(N_S²)` cost,
banked as reachable-but-deferred), and 392 cells `N_S > 9000` past the wall (no
certified length-5 reduction; see §0/§4).

---

## 4. The missing reduction, honestly

The rectangular reduction (`docs/s33_review.md` §2) works because `S_{(δ^4)}`
is one-dimensional (`det^δ`), so its highest-weight vectors are Weyl
eigenvectors and `A_4` 2-transitivity collapses the four raising operators to
one. For a general length-5 weight `S_lam(C^5)` is not one-dimensional, the
highest-weight vectors are not Weyl eigenvectors, and that collapse is
unavailable. Session 36's brief (which would have specified a general
"stabiliser-isotypic reduction") is absent from the repository, so no vetted
general reduction exists to reimplement. Rather than bank results from an
uncertified home-grown reduction — exactly the shared-spec/regime-transfer trap
the house has been burned by — the δ=8 measurements use the exact unreduced
pipeline within its memory reach. Extending past `N_S ≈ 9000` (the balanced,
large-`a` cells, where the onset — if low — is most likely to hide) needs a
correct length-5 reduction; that is the first thing a successor session should
build, and it should be validated against the banked δ=6 length-5 cells and the
rectangular ladder before any new cell, as here.

---

## 5. Honest boundary

- **Measured with certificates (both primes, rank attains `a`):** `mult_det = a`
  at all 27 reachable δ=8 cells (`N_S ≤ 5000`); the rectangular ladder
  rungs 4–8; the nine δ=6 length-5 cells. Each is a rigorous `det_units = 0`.
- **Computed exactly (two routes for `a`; `m_det` batched == reference):** the
  occurrence table, δ=5–10 (δ=11,12 §2), 2585 cells, zero `a > m_det`.
- **Not reached:** 16 reachable δ=8 cells (`5000 < N_S ≤ 9000`); all 392 δ=8
  cells past the memory wall; δ≥9 rank measurements. None is claimed either way.
- **Not proved, only observed:** that `a ≤ m_det` at every length-5 cell (it is
  a theorem at length ≤4, Cor. 7; here it is measured, δ≤10+). The onset's
  *existence* below 405 is guaranteed by codim 20 > 0; its *degree* is not
  pinned by this session.
- **Sign discipline:** `det_units ≥ 0` throughout; a positive value is a det-side
  equation (an onset witness), not the pad-side `D>0` obstruction — which this
  session does not touch (per the brief, ℓ=5 is permanent-washed, det-side only).

---

## 6. The window as left, and the next probe

Onset window: **`[8, 405]`** (unchanged in bracket). The session's product is
the **character** of the onset — a multiplicity drop, not an occurrence bite —
and a clean negative at δ=8 across the reachable corner. The occurrence screen,
being cheap and decisive, has now retired the arithmetic route for the entire
window: no successor need re-run it.

Next probe, in order: (1) a **correct length-5 stabiliser reduction** (the
absent s36 lemma), validated against the banked δ=6 cells and the rectangular
ladder; (2) with it, the balanced large-`a` δ=8 cells (`N_S > 9000`) where a low
onset would most plausibly sit, then δ=9; (3) failing a reduction, an
abstract-HWV evaluation (theory_directions Direction 7) to reach the same cells.
Bundle head: see `docs/session_38.md`.
