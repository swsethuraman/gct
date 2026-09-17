# Corrigendum to `work/claude_transverse_structure_20260916/REPORT.md`

Claude session, 17 September 2026. The sealed report (SHA-256 `5342a929…`) and its manifest
(`2c42caa8…`) are preserved byte-for-byte; every item below cites the sealed file by section and
line and gives the replacement statement. Notation: `M = M_(4^5)`, `E ⊆ M` the determinant
coordinate subspace, `j : M -> J` the source jet map through order four, `V = j(M)`, `L = j(E)`,
`L_max` the target-compatible plane with the Hessian parameter left free; `L ⊆ L_max`, `L ⊆ V`.
Full proofs are in `REPORT.md` §3 of this follow-up.

## K1. The intersection error in Theorem 6.1(c) — sealed §6.2, lines 435–438

**Sealed text.** "The rank actually realised on `M_lambda` by all order-`<= 4` conditions at `K`
is `dim j(M_lambda) - dim L` (with `L` replaced by `L_max` for E-free conditions) …"

**Defect.** For the family annihilating `L_max` the correct quantity is `dim V − dim(V ∩ L_max)`;
replacing `V ∩ L_max` by `L_max` presumes `L_max ⊆ V`, which is not proved (and need not hold).

**Replacement.** *Let `Ann(X) ⊆ J^*` be the annihilator of a subspace `X ⊆ J`. The rank on `M` of
`{phi ∘ j : phi ∈ Ann(L_max)}` equals `dim V − dim(V ∩ L_max)`; the rank on `M` of
`{phi ∘ j : phi ∈ Ann(L)}` equals `dim V − dim L`, because `L ⊆ V`. Since `L ⊆ V ∩ L_max`, the
E-free rank is at most the E-using rank, with equality iff `V ∩ L_max = L`.*
(Proof: `{phi|_V : phi ∈ Ann(X)} = Ann_V(V ∩ X)`, and `j : M -> V` is surjective.) At `(5,(4^5))`
with `dim V = 5` (jet injectivity) the E-using rank is `4`; the E-free rank is `4` iff
`V ∩ L_max = L` and `3` iff `L_max ⊆ V`.

## K2. "Every E-free condition" — sealed §6.2 (a), lines 426–430; §0 line 29–37; §6.3 line 480; §6.5 line 527

**Sealed text.** "Every globally necessary linear condition … without using knowledge of
`A_{d,lambda}` beyond its covariance, factors through `j` and vanishes on `L_max`. The space of
such E-free conditions has dimension at most `dim J_{<=4} − 2` …"; "up to five E-free conditions
in total".

**Defect.** Not using an ambient basis does not force a condition to annihilate every formal
parameter choice in `L_max`; a condition obtained from an *evaluated* ambient generator (for
example `J_1(z) − (3/14) z(K)` in six rows, or `J_{S1}(z) − (13/21) z(K5)` in five) uses
ambient-image information (the Hessian ratio of `H6`, `H5`) and annihilates `L` but not `L_max`.
Also, "`dim J − 2`" is a dimension in `J^*`, not a rank on `M`; and a finite family of direction
evaluations need not span the annihilator it sits in.

**Replacement.** *Define the **E-free family** as `F_free := {phi ∘ j : phi ∈ Ann(L_max)}` — by
definition the conditions obtained by eliminating both target parameters `(F(u^2), kappa~)`
from the target-side identities (this is exactly how `C2` and the `C4_{S,S'}` were derived).
`dim Ann(L_max) = dim J − 2` (`= 1` for `r = 6`, `= 5` for `r = 5`). Its rank on `M` is
`dim V − dim(V ∩ L_max) ≤ dim V − dim L`. Define the **E-using family** as
`F_E := {phi ∘ j : phi ∈ Ann(L)}`, of dimension `dim J − dim L` in `J^*` and rank `dim V − dim L`
on `M`; its members use the adopted or verified Hessian ratio of the ambient generator and are
not independent of ambient-image information. A **tested family** `T` is a finite subset of
`span` of Taylor functionals; its rank on `M` is `≤` that of the family it sits in, with equality
only if its members span the corresponding annihilator restricted to `V` (see K4).*

## K3. "Vanishes exactly on the ambient line" — sealed §5.3, lines 365 and 372; §0 line 50–52

**Sealed text.** table header "value on the `H5` line"; "Each `C4_{S,S'}` is globally necessary on
`M_(4^5)` (it vanishes on `E` by construction, and the vanishing on the ambient line is checked
exactly)".

**Replacement.** *Each `C4_{S,S'}` evaluates to zero **exactly on the ambient generator**
`H5 ∘ phi` (integer arithmetic), hence on `E = C·(H5 ∘ phi)`; it is therefore globally necessary.
Its full kernel on `M` is not determined by this; in particular "kernel equals `E`" is not
claimed for any single condition.*

## K4. The missing lemma's scope — sealed §9.3, lines 659–676; §8.1 route 2, line 583

**Sealed text.** "Lemma (jet injectivity at `K5`) … Equivalently, the order-`<= 4` transverse
conditions at `K5` have rank exactly `4` on the source and their common kernel is `E`."

**Defect.** The "equivalently" conflates three statements: (i) `ker j = 0`; (ii) the E-using
family `F_E` has `ker = E`; (iii) a *tested* family `T` has `ker T = E`. It also leaves open which
family (E-free or E-using) is meant.

**Replacement.** *Jet injectivity means `ker j = 0`, equivalently `dim V = s = 5`. Then:
(a) `ker F_E = j^{-1}(L) = E + ker j = E` — so `F_E` has kernel `E` iff `ker j ⊆ E`, and since
`E ∩ ker j = 0` (`H5(u^2) ≠ 0`), iff `ker j = 0`. (b) `ker F_free = j^{-1}(V ∩ L_max)`, which equals
`E` iff `ker j = 0` **and** `V ∩ L_max = L`; injectivity alone does not discharge the intersection
condition. (c) For a tested family `T = {phi_1 ∘ j, …, phi_m ∘ j}` with `phi_i ∈ Ann(L)`:
`ker T = E` iff `ker j = 0` and `span{phi_i|_V} = Ann_V(L)` (i.e. `∩_i ker phi_i ∩ V = L`); with
`phi_i ∈ Ann(L_max)` additionally `V ∩ L_max = L`. Route 2 of §8.1 ("if the family reaches rank
`4` on `M` then `ker T = E`") is correct as stated, since `dim M = 5` and `E ⊆ ker T`; it is the
rank, not injectivity, that must be certified, and for an E-free `T` rank `4` implies
`V ∩ L_max = L`.* The lemma of the sealed §9.3 is henceforth read as statement (i) only.

## K5. The order-four Taylor coefficient — sealed Theorem 4.4, line 211

**Sealed text.** "`[t^4] z(K + tS) = z(K) alpha_4(S) + Phi_2(z)(S_N, n_3(S)) + Phi_2(z)(n_2(S), n_2(S))
+ Phi_4(z)(S_N^4)`".

**Defect.** The displayed coefficient omits the factor `2` on `Phi_2(n_1, n_3)`, the cross terms
coming from `c(t)`, and does not state the gauge in which `n_2 = 0`.

**Replacement.** With `c(t) = 1 + c_1 t + c_2 t^2 + …`, `c(t)^{4d} = 1 + g_1 t + g_2 t^2 + g_3 t^3 +
g_4 t^4 + …`, `n(t) = n_1 t + n_2 t^2 + n_3 t^3 + …`, `n_1 = S_N`, and `f_z = z(K) + Phi_2 + Phi_3 +
Phi_4 + …`:

    [t^0] = z(K)
    [t^1] = g_1 z(K)
    [t^2] = g_2 z(K) + Phi_2(n_1,n_1)
    [t^3] = g_3 z(K) + g_1 Phi_2(n_1,n_1) + 2 Phi_2(n_1,n_2) + Phi_3(n_1,n_1,n_1)
    [t^4] = g_4 z(K) + g_2 Phi_2(n_1,n_1) + 2 g_1 Phi_2(n_1,n_2) + Phi_2(n_2,n_2) + 2 Phi_2(n_1,n_3)
            + g_1 Phi_3(n_1^3) + 3 Phi_3(n_1,n_1,n_2) + Phi_4(n_1^4).

For symmetric `S` and the lift chosen through a `tau'`-stable complement of `Lie(Stab_K)` in
`Lie(Gamma)` (unique by the formal inverse function theorem), `c(−t) = c(t)` and `n(−t) = −n(t)`
(REPORT §3.6), so `g_1 = g_3 = 0`, `n_2 = 0`, and `Phi_odd = 0`, giving

    [t^2] = g_2 z(K) + Phi_2(n_1,n_1),
    [t^4] = g_4 z(K) + g_2 Phi_2(n_1,n_1) + 2 Phi_2(n_1,n_3) + Phi_4(n_1^4).

The valid conclusion of Theorem 4.4 — every Taylor coefficient is a universal linear function of
`(z(K), Phi_2(z), Phi_4(z), …)` — is unchanged; only the displayed coefficient was wrong.

## K6. Full-stabilizer statements — sealed Lemma 4.2 (line 189), Corollary 4.5 (line 232–234)

**Sealed text.** "`N` is the unique `Stab^0`-stable complement"; "The finite parts of `Stab`
(`tau'`, the centre `mu_4`, the sign `c = −1`) act trivially on `Sym^{even}(N^*)`, so these are the
counts for the full stabilizer."

**Replacement (justification supplied, statement unchanged).** *`Stab_Gamma(K) = {(A, cA^T, g_A) :
A ∈ G_r, c^2 det A = 1}` is **connected** (a connected double cover of the connected group
`G_r`), so it equals `Stab^0`, and `N` — the unique isotypic component of its type in `T` — is
stable under all of it. The extra symmetry `tau' : Y -> −Y^T` (outside `Gamma`, but preserving
every `z`) acts on all symmetric directions by `−1`, hence preserves `N ⊆ V_sym` and acts
trivially on `Sym^{even}(N^*)`. The image of `Stab^0` in `GL(T)` is `PGL_4` resp. `PGSp_4 = PSp_4`;
the centre acts trivially on `T` (total degree `4` in `C^4`), so the `SL_4`- resp. `Sp_4`-character
counts are the counts for the full symmetry group of `z` fixing `K`. The `r = 6` commutant
statement (`Y D = D^T Y` for all skew `Y` forces `D` scalar) is ADOPTED as classical; the `r = 5`
one was MEASURED.* Nothing here is left conditional except that adopted classical fact.

## K7. Six-row "at least seven invisible survivors" — sealed §6.3, lines 461–466

**Retained**, with the justification restated so that it needs no surjectivity of `j`: `dim V ≤
dim J_{<=4} = 3` and `dim L = 1` (`a = 1`, `H6(u^2) ≠ 0`), so the E-using family has rank
`dim V − 1 ≤ 2` on `M_(4^6)`; the E-free family has rank `dim V − dim(V ∩ L_max) ≤ 1`. Hence at
most two of the nine false directions can be removed by linear tests factoring through these
jets, whatever carrier is built. The sealed "(Tier C, OPEN) whether the second condition adds
rank" is the question `dim V = 3` versus `2`.

## K8. Ledger entries — sealed §10

| entry | sealed label | replacement |
|---|---|---|
| T9 | NOT REACHED | **PARTLY REACHED** (this follow-up): `C4_{S1,S2}` and `C4_{S1,S4}` are independent of `C2` over `Q` on `span(q_3, q_7)` (nonzero modular `2×2` minors `247396`, `197933`); hence `dim V − dim(V ∩ L_max) ≥ 2`, `dim V ≥ 3`. Distinctness on all of `M` and action on `ker C` remain open. |
| T9' | EXPECTED | **PROVED a posteriori**: a nonzero minor with `C2` forces a nonzero `Phi_4`-component of `C4_{S1,S2}` on `J` (REPORT §5.4). |
| T12 | "`<= 5` E-free conditions through order four, realised rank `<= 4`" | `dim Ann(L_max) = 5` in `J^*`; rank on `M` is `dim V − dim(V ∩ L_max) ≤ 4`. |
| T15 | OPEN | OPEN; scope fixed to `ker j = 0` (K4); reduction to a finite map in REPORT §4. |

## K9. Minor wording — sealed §6.1, line 402–406 (definition of `L`)

`L := {(f, f beta_0, f A' + kappa (N ∘ h_4)) : (f, kappa) = (F(u^2), kappa~_F)}` is the image of
`A_{d,lambda}`, which for `a = 1` is a line; the two-dimensional plane spanned by the two displayed
vectors is `L_max`. The sealed text says this, but then uses `L_max` as if it were the ambient
image in (c); see K1.
