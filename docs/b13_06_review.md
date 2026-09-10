# B13-06 review — positive gap beyond the LMR cell

board_numbering: batch13
session_id: B13-06
model recorded by the session: `gpt-6-astra`, reasoning effort `xhigh`
bundle: `b13_06_lmr_products.bundle` (one part, `part00` byte-identical)
base: `00495110c62acfbbbc951e82cc218ed091563b3f`
head: `34b58e3e40f39efc3ad270e3444eb8a79679f753` (`b13-06`)
status claimed: **finite reduction completed; no positive gap claimed**
integrator verdict: **accept. A clean structural reduction with two real
negatives, delivered without overclaiming. Nothing blocks merge.**

Stock-take. Arithmetic here is hand-checkable or closed-form; one independent
recount of the two new ambient counts is running separately.

---

## 1. Zero-cost checks

| check | result |
|---|---|
| md5 | `f1b7f930f6fca74003b27e3ec2e88229` — matches, whole and `part00` |
| sha256 | `b8e3ff9a…9992fee9` — matches, whole and `part00` |
| `part00` vs whole | **byte-identical** (`cmp` clean) at 556,186 B |
| declared base | `0049511` — equals `origin/main` and my tip |
| `git bundle verify` | "is okay" |
| applies | clean; 40 files, 203,622 insertions, **0 deletions**; 12 commits |
| single-writer files | **none touched** |
| 5 MB rule | none close |
| `Claude-Session:` trailer / `claude.ai` URL | **none** — clean |
| `Co-Authored-By` trailer | **absent on all 12** (see §6) |
| pre-registration | `07b808e` first commit, before any computation |
| run bounds | Windows Job Objects, 768 MiB/process, 300 s or 1,200 s watchdogs, pid + resources JSON per run |

Hand-checked, no machine needed beyond three lines of arithmetic:

**The two quadratic highest-weight vectors are correct.** With
`E₁₂c_j = (5−j)c_{j−1}`:

- `E₁₂(8c₀c₂ − 3c₁²) = 8·3c₀c₁ − 3·8c₀c₁ = 0` ✓
- `E₁₂(12c₀c₄ − 3c₁c₃ + c₂²) = 12c₀c₃ − 3(2c₁c₂ + 4c₀c₃) + 6c₁c₂ = 0` ✓

Weights: `c₄₀c₂₂` and `c₃₁²` both `(6,2)`; `c₄₀c₀₄`, `c₃₁c₁₃`, `c₂₂²` all
`(4,4)`. So `(65,17,2⁷) + (6,2) = (71,19,2⁷)` and `+ (4,4) = (69,21,2⁷)` ✓,
and the `u`-ladder gives `(69,17,2⁷)` at degree 25 and `(73,17,2⁷)` at 26 ✓.

Everything else reproduces: census `15+16 = 31` and `89+119+97 = 305`; degree-26
channel sums `109+501+189 = 799`; candidates `30 + 207 = 237` with `31−1 = 30`
and `305−97−1 = 207`; the binary control's `9+7+5+3+1 = 25 = 5²` splitting as
`15` (even) and `10` (odd); `dim Sym²(Sym⁴C^d) = 15, 120, 630` at `d = 2,3,4`;
and the sufficient minor sizes `392−2+1 = 391`, `531−3+1 = 529`.

The certification threshold is stated correctly. `rank T_det ≤ a − j` from `j`
independent product equations, so a nonzero padded minor of size `a − j + 1`
gives `mult_pad > mult_det`, i.e. `D > 0`. And the caveat is right too:
`j > i_red` establishes `i_det > i_red` but **not** `D > 0`, because
`i_pad ≥ i_red` always.

---

## 2. The cross-confirmation with B13-04

`8c₀c₂ − 3c₁²` and `12c₀c₄ − 3c₁c₃ + c₂²` are, in the `q_β` notation,
`8q₄₀q₂₂ − 3q₃₁²` and `12q₄₀q₀₄ − 3q₃₁q₁₃ + q₂₂²`.

**Those are exactly B13-04's Model A highest-weight vectors** — the second is
the classical degree-2 invariant of binary quartics, which B13-04 uses at
`λ = (4,4)`, and the first is the `(6,2)` vector whose fixed-factor restriction
`8c₃₀c₁₂ − 3c₂₁²` refutes the converse of Prop. 8(2).

Two sessions, two different assignments, two different models, arriving
independently at the same pair of quadratic highest weights in `Sym²(Sym⁴)` —
B13-04 to build a counterexample, B13-06 to build new determinant equations. I
verified both `E₁₂ = 0` computations by hand in each review and they agree.

---

## 3. What was delivered

**A complete finite census** of the tensor-domain support of `E ⊗ A_k` for
`E = S_{(65,17,2⁷)}V` at coefficient degrees 25 and 26: 31 and 305 distinct
constituents, tensor multiplicities summing to 31 and 799, with every partition,
channel multiplicity, image-rank interval and decision question banked. All
2,196 channel coefficients agree between two unrelated routes — Pieri via
`s_{(a,b)} = h_a h_b − h_{a+1}h_{b−1}`, and direct semistandard LR tableau
enumeration with lattice-word checking that never calls the Pieri code. Eight
Weyl-dimension sums agree with `dim(E)·dim(A_k)` at `r = 9,10,11,16`. 0.11 s,
20.3 MB.

**Two guaranteed new determinant equations**, `f·(8c₀c₂ − 3c₁²)` at
`(71,19,2⁷)` and `f·(12c₀c₄ − 3c₁c₃ + c₂²)` at `(69,21,2⁷)`, both degree 26.
Nonzero because polynomial multiplication in a domain is injective; highest
weight by the raising rule above; in `I(D)` by the ideal property. **This is a
mechanism for `i_det > 0` outside the LMR ladder**, and the session says
plainly what it is not: it does not show the padded or reducible multiplicity is
smaller.

**Two exact transport limitations**, and these are the substance:

1. **The Cartan ladder cannot help.** Multiplying by `u = c_{(4,0,…)}` injects
   on ambient highest-weight spaces, on `I(X)` and on `Q[X]` for `X = D,P,R`;
   with `a_d = 274` saturated for all `d ≥ 24`, the injection is an isomorphism,
   and `uf ∈ I(X) ⟺ f ∈ I(X)` because `Q[X]` is a domain. So
   `i_X((65+4k,17,2⁷), 24+k) = i_X((65,17,2⁷),24)` for **every** `k ≥ 0`:
   `mult_det = 273`, `mult_pad ≥ 269`, `D = 1 − i_pad(24)`, unchanged forever
   along that ladder. The most obvious route out of the LMR cell is structurally
   closed, and closed without any degree-23 equality.
2. **Ninety-seven components are settled.** The full padded form `ℓ·per₃` has
   ten essential variables, so its orbit closure lies in the ten-variable
   subspace variety whose coordinate ring carries no constituent of length > 10.
   Hence `mult_pad = 0` at all 97 eleven-row entries, and `D ≤ 0` there **with no
   sampled deficiency anywhere in the argument**.

**A minimal control that earns its place.** For `Sym⁴C² ⊗ Sym⁴C²` the five
components `(8),(7,1),(6,2),(5,3),(4,4)` have dimensions `9,7,5,3,1`; explicit
highest-weight tensors multiply nontrivially in the three even channels and to
**zero** in the two odd ones, giving image 15 and kernel 10. So **a positive
LR coefficient alone does not give a product equation in that isotypic
component.** That is the same discipline point B13-04 made about Pieri
compatibility, in its smallest possible form, verified over `ℤ`.

---

## 4. This is B13-01's shape, on the other side of the problem

B13-01 proved that the instrument the board designated for `i_red ≥ 1` — an
evaluation — cannot in principle certify a lower bound on `i`. B13-06 proves
that the route the board designated for going beyond LMR — Cartan powers of the
highest coefficient — cannot in principle change the gap.

**Two sessions have now returned priced negatives that close a natural route
rather than failing at it**, and in both cases the negative redirects: B13-01 to
the coupled 73-dimensional target, B13-06 to the two non-ladder quadratic
weights. Neither is a session that ran out of budget.

The continuation B13-06 leaves is concrete and small: the `392 × 2` and
`531 × 3` product-image maps. Prove maximal rank 2 and 3 and the sufficient
padded minors drop to 391 and 529; prove only the guaranteed one copy and they
stay at 392 and 531. It also says exactly what it did not do — no non-Cartan
`B_ν`, no `S_ν`, no padded rank at degree 25 or 26, and no rational LMR
generator reconstructed in the 274-filling coordinates.

---

## 5. Discipline

The ADOPTED/MEASURED boundary is drawn where the programme's corrections put it,
without being asked twice:

- `mult_det = 273` exactly and `mult_pad ≥ 269` are ADOPTED; the sampled 269,
  the five-dimensional sampled kernels and `D = −4` are labelled **MEASURED and
  explicitly not adopted as identities**. `i_pad(24) = i_pad(23)` is **not**
  inferred — which is precisely the claim I withdrew.
- The nonvanishing of the LMR line on `P` and `R` is justified through the
  nonzero 273-minor plus a modular annihilating vector, and the session
  **distinguishes that from lifting a modular containment of a
  higher-dimensional kernel**, naming the latter as the unresolved
  degree-23/24 issue. That is the exact distinction the withdrawal turned on,
  stated by a session that was not assigned it.
- "No `D > 0` or nonzero cubic-permanent ideal is reported, so no
  positive-candidate verification protocol is asserted to have been completed."
- `lr_audit.json` includes **zero** channels, so completeness was checked even
  for constituents removed by cancellation. Auditing the absences is the right
  instinct.
- The ambient `a = 274` control at degree 24 reproduces the record on a brand-new
  integer Weyl/DP implementation with overflow detection at every addition, and
  all five cells report the same `nonzero_aggregated_weights = 1262`.

An independent recount of `a(71,19,2⁷;26) = 392` and `a(69,21,2⁷;26) = 531` by
the house `wk9_s42_census.a_weyl` is running under
`results/logs/wk13_int_b1306_ambient.{log,pid}`; those two numbers are what the
whole continuation plan is priced against, so they are worth confirming from a
second implementation.

---

## 6. Attribution, and the pattern now completes

Twelve commits, **no `Co-Authored-By` trailer and no session-link**. The model
is recorded as `gpt-6-astra` (`xhigh`) in the report front matter, the delivery
manifest and the run summary — the material requirement, satisfied.

Across the six sessions delivered, attribution now falls into three clean groups:

| session | model | `Co-Authored-By` | session-link |
|---|---|---|---|
| B13-02, B13-03, **B13-06** | Astra | absent | absent |
| B13-01 | Fable 5.1 | present | absent (declined explicitly) |
| B13-04, B13-05 | Fable → **Opus 5** | present | **present on every commit** |

The session-link appears on exactly the two sessions that ran partly as Opus 5,
and on all of their commits including the Fable-phase ones. Three Astra
controls and one Fable-only control carry none. That is as clean a correlation
as six data points can give, and it says the trailer is an environment
property, not a session's judgement. **The preamble should require stripping it
before bundling and name `tools/rewrite/message_callback.py`**, rather than
relying on sessions to decline it.

---

## 7. The toolchain gap is now three for three, and it is Astra-only

B13-06 reports Python 3.12.14 and numpy present; **flint, sympy, scipy and
psutil missing, with local installation blocked by WinError 10013** — the same
socket permission refusal as B13-02 and B13-03. Its host is Windows (33.75 GB
total, 7.43 GB free, Job Objects for the memory cap), which fits.

| | toolchain |
|---|---|
| B13-02, B13-03, B13-06 — **Astra** | blocked, WinError 10013, 3 of 3 |
| B13-01, B13-04, B13-05 — **Fable/Opus** | `python-flint 0.9.0` + `sympy` installed without trouble, 3 of 3 |

**Six for six, cleanly split.** My original post-B13-03 action — warn the whole
batch — was wrong in scope, and the B13-01 correction is now confirmed twice
over. The three remaining Astra slots should be told; the Claude-side sessions
need nothing.

B13-06 routed around it honestly: its exact decomposition and coefficient work
needs none of the missing packages, and it says so — but it also records
"fresh python-flint rank replays remain unperformed", which is the right way to
leave a gap.

---

## 8. Board defects

1. **The B13-06 entry names conceptual inputs but no exact paths and no ambient
   variable count.** The session resolved it itself from `lmr_cell.md`,
   `s74_final_review.md`, `compact_circuit.md`, the s74 source/columns/
   certificates, `s63_aladder.json` and the batch-10/11 stocktakes, and used s57
   Lemma L / Proposition S for the stable-range argument. Those tier-3 additions
   should go into the entry.
2. **The preamble's clone instructions assume `main` exists.** This session got
   a frozen checkout where `main` is absent and HEAD already equals the required
   base. It handled that correctly and changed no shared checkout or global Git
   configuration, but the preamble's check should accommodate the frozen-checkout
   case rather than requiring a paragraph of explanation.
3. A useful warning banked: **do not run the historical s63 driver** — it writes
   to the old session's paths.

---

## 9. Actions

1. **Merge-ready.** No trailer surgery needed, unlike B13-04 and B13-05.
2. **Warn the three remaining Astra sessions** about WinError 10013 and the
   absent exact-LA libraries. The Claude-side sessions need nothing — this is
   now six-for-six evidence.
3. **Put the session-link stripping requirement in the preamble**, with the tool
   named, rather than relying on sessions to decline it.
4. **Fill in the B13-06 board entry's paths and ambient variable count**, and
   make the preamble's clone check tolerate a frozen checkout.
5. **The continuation is worth funding and is small**: the `392 × 2` and
   `531 × 3` product-image maps. B13-06 specifies the pilot shape — one 1,200 s
   / 768 MiB run per `B` column, bank an exact prefix and measured entry costs,
   stop before any full weight-space allocation. Note the standing constraint it
   names: the LMR weight space has 156,438,903,314 monomials, so small
   multiplicity-space dimensions do not remove the expansion cost, and that
   domain must not be materialized.
6. On the deferred verification pass: confirm `392` and `531` from the second
   implementation (running now), and replay two of the 2,196 LR channel
   coefficients by hand from the skew shapes.
