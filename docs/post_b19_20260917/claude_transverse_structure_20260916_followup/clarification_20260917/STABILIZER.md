# The full stabilizer of the quadratic-square skew pencils, and why the jet counts stand

Claude session, 17 September 2026. Replaces the sealed Lemma 4.1 / §3.7 arguments (sealed report
`work/claude_transverse_structure_20260916/REPORT.md` §4.1, Cor. 4.5; follow-up `REPORT.md` §3.7,
`CORRIGENDUM.md` K6). The invalid step was "a double cover of a connected group is connected".
Everything below is PROVED unless labelled; the one MEASURED input is the commutant computation
of the sealed Check 1 (`A_K5_commutant_dimension = 1`).

## 1. The symmetry group and the character

Let `Gamma_full := GL_5 x GL_4 x GL_4 x <tau>` act on `W^5 = Mat_4 (x) C^5` by
`(g, A, B, 1) : Y_i -> sum_j g_ij A Y_j B` and `tau : Y_i -> Y_i^T`. Every `z in M = M_(4^5)` is a
semi-invariant:

    z(g.A.Y.B) = det(g)^4 det(A)^5 det(B)^5 z(Y),        z(Y^T) = z(Y).

(`GL_5`-weight `(4^5)`; `SL_4 x SL_4`-invariance plus total matrix-entry degree `20`: `A = a I`
gives `a^20 = det(A)^5`; `z(-Y) = z(Y)` is the case `g = -I_5`.) Write `chi` for this character.

Let `S := Stab_{Gamma_full}(K5)` (fixing the **tuple** `K5`, not just its span). For `gamma in S`
and any `n`, `z(gamma(K5 + n)) = z(K5 + gamma n)` (linear action), so `f_z(gamma n) = chi(gamma) f_z(n)`
for `f_z(n) := z(K5 + n)`. Two things must therefore be computed: `S` with its effective action
on `T = W^5` (hence on `N`), and `chi|_S`.

## 2. The `epsilon = 1` part

**Claim.** `(g, A, B, 1) in S` iff `B = c A^T` for some `c in C^*`, `A in GSp_4(omega)`, and
`g = R(A, c)^{-1}`, where `R(A, c)` is the matrix of `Y -> c A Y A^T` on `span(K5) = omega^perp` in
the basis `Y_1..Y_5`.

*Proof.* Fixing the tuple means `A Y_j B in span(K5)` for all `j`, in particular all `A Y B`,
`Y in omega^perp`, are skew. `A Y B` skew for all `Y in omega^perp` iff `Y D = D^T Y` for all such `Y`,
`D := B A^{-T}`, and the solution space is `C.I` (MEASURED, sealed Check 1). So `B = c A^T`.
Then `Y -> c A Y A^T` must preserve `omega^perp`, the `Pf`-orthogonal of the line `C.omega`; since
`Pf(A Y A^T) = det(A) Pf(Y)`, this holds iff `A omega A^T in C.omega`, i.e. `A in GSp_4(omega)`
with multiplier `mu(A)`: `A omega A^T = mu(A) omega`, `det A = mu(A)^2`. Finally `g` is forced:
`sum_j g_ij (c A Y_j A^T) = Y_i` says `g = R(A,c)^{-1}`. ∎

So the **parameter group** is `Pi := GSp_4(omega) x C^*` (connected: `GSp_4 = C^* . Sp_4` over
`C`, and `Sp_4` is connected), mapped bijectively onto `S^{(1)} := S ∩ {epsilon = 1}` by
`(A, c) -> (R(A,c)^{-1}, A, cA^T)`. There is **no** constraint `c^2 det A = 1` at this level: that
constraint only appears when one insists on `(A, B) in H^0` (`det A det B = 1`), which is
unnecessary once the character `chi` is carried along.

**Kernel of the action.** `(g, A, B)` acts trivially on `W^5` iff `A Y B = lambda Y` for all `Y` and
`g = lambda^{-1} I`, i.e. `A = a I`, `B = a^{-1} lambda I`. Inside `S^{(1)}`: `(A, c) = (a I, c)`,
`lambda = c a^2`. So the kernel is `K_0 = {(a I, c)} ≅ (C^*)^2 ⊂ Pi`, and the **effective group**
is `Pi / K_0 = GSp_4 / C^* = PGSp_4 = PSp_4 = Sp_4 / {±1}`, connected.

**The character on `S^{(1)}`.** For `(A, c) in Pi`: `det A = mu^2`, `det B = c^4 mu^2`,
`det R(A,c) = c^5 . det(Lambda^2 A |_{omega^perp}) = c^5 mu^5` (on `Lambda^2`, `det Lambda^2 A =
det(A)^3 = mu^6`; on the line `omega` it is `mu`; on `omega^perp` therefore `mu^5`), so
`det g = c^{-5} mu^{-5}` and

    chi(g, A, B) = (c^{-5} mu^{-5})^4 . mu^{10} . (c^4 mu^2)^5 = c^{-20} mu^{-20} mu^{10} c^{20} mu^{10} = 1.

So `chi ≡ 1` on `S^{(1)}`: `f_z` is genuinely invariant (not merely semi-invariant) under
`S^{(1)}`, for every `z in M`, without appeal to any nonvanishing value.

**Inside `Gamma = SL_5 x H^0` (the sealed setting).** Restricting to `det A det B = 1` with
`B = c A^T` gives `det A . c^4 det A = c^4 mu^4 = 1`, i.e. `c^2 det A = ±1` and `c mu in {±1, ±i}`:
**four** branches (the sealed "`c^2 det A = 1`" kept only two of them, `c mu = ±1`). The `SL_5`
condition on the induced row action is `det g = (c mu)^{-5} = 1`; together with `(c mu)^4 = 1` it
forces `c mu = 1` and **kills every other branch**. Hence
`Stab_Gamma(K5) = {(A, mu(A)^{-1} A^T, R^{-1}) : A in GSp_4} ≅ GSp_4`, connected, with kernel the
scalars `a I` (`c = a^{-2}`, `B = a^{-1} I`, `g = I`) and effective image again `PSp_4`. The sealed
"`Stab^0 = {… : c^2 det A = 1}`" described the set before the `SL_5` condition; the sealed
"connected double cover" sentence was not a proof. Neither affects the effective group.

## 3. Transpose and the remaining components

`(g, A, B, tau)` acts by `Y_i -> sum_j g_ij (A Y_j B)^T = sum_j g_ij B^T Y_j^T A^T`. On skew `Y_j` this
is `-sum_j g_ij B^T Y_j A^T`, i.e. the `epsilon = 1` element `(-g, B^T, A^T)`. Hence
`(g, A, B, tau) in S` iff `(-g, B^T, A^T, 1) in S`, and `S = S^{(1)} ∪ tau' S^{(1)}` with
`tau' := (-I_5, I, I, tau) : Y_i -> -Y_i^T`. `tau'` fixes `K5`, `chi(tau') = det(-I_5)^4 = 1`, and
`tau'` acts on `T` by `-1` on symmetric directions and `+1` on skew directions. It is **not** in
the effective image of `S^{(1)}`: an element of `S^{(1)}` acting as `+1` on all skew directions
`Lambda^2 (x) C^5` (30-dimensional) must have `c Lambda^2 A (x) g = 1`, forcing `A` scalar, hence
`+1` on symmetric directions too. So the effective full stabilizer is

    S_eff = PSp_4 ⋊ <tau'>,   exactly two components,

and `tau'` normalises `S^{(1)}` (conjugation by `tau` sends `(g, A, B)` to `(g, B^T, A^T)`).
No element with `epsilon = 1` outside the parametrisation exists (the Claim is an iff), and every
`epsilon = tau` element is `tau'` times one of them; this exhausts `S`.

## 4. Action on `N` and on `Sym^{even}(N^*)`

`Pi` acts on symmetric directions by `S_i -> sum_j g_ij c A S_j A^T`; the `c` cancels against
`g = R^{-1}`, and the scalars `a I` act trivially, so the action factors through `PSp_4` and is
`Sym^2(C^4) (x) (omega^perp)^*`, restricted to `Sp_4`: `10 (x) 5 = 35 + 10 + 5` (`5 = V(omega_2)` is
self-dual), with `-1 in Sp_4` acting trivially (even total degree). `N` is the `35` (sealed Lemma
4.2: unique complement to the orbit-tangent projection). `tau'` acts on all of `V_sym`, hence on
`N`, by `-1`, so `N` is stable under all of `S_eff`. Therefore

    C[N]^{S_eff} = (C[N]^{Sp_4})^{tau'} = ⊕_{m even} Sym^m(N^*)^{Sp_4},

and `f_z` (which is `S_eff`-invariant because `chi ≡ 1` on `S`) has `Phi_odd = 0` and
`Phi_{2m} in Sym^{2m}(N^*)^{Sp_4}`. The character counts `j_2(5) = 1`, `j_4(5) = 5`, `j_6(5) = 24`,
`j_8(5) = 127` of the sealed Check 1 (computed for `Sp_4`) are therefore the counts for the **full**
stabilizer, and `dim J_{<=4} = 1 + 1 + 5 = 7` stands. **Conclusion: counts and jet-space
dimensions remain valid; only the proof is replaced.**

## 5. Six variables, separately

`Gamma_full = GL_6 x GL_4 x GL_4 x <tau>`, `chi = det(g)^4 det(A)^6 det(B)^6` (degree `24`).
`(g, A, B, 1) in Stab(K6)` iff `B = c A^T` (the commutant of all skew `Y`, `Y D = D^T Y`, is
`C.I` — ADOPTED as classical: `Y D` skew for all skew `Y` forces `D` scalar) with `A in GL_4`
arbitrary (`Lambda^2 A` preserves `Lambda^2 C^4 = span(K6)`), and `g = (c Lambda^2 A)^{-1}`. Parameter
group `GL_4 x C^*`, connected; kernel `{(a I, c)}`; effective `PGL_4 = SL_4 / mu_4`, connected.
Character: `det g = c^{-6} det(A)^{-3}`, so `chi = c^{-24} det(A)^{-12} det(A)^6 c^{24} det(A)^6 = 1`.
Inside `Gamma = SL_6 x H^0`: `det A det B = c^4 det(A)^2 = 1` gives `c^2 det A = ±1`, and the
`SL_6` condition `det g = (c^2 det A)^{-3} = 1` keeps exactly `c^2 det A = 1`, so **both** branches
`c = ±(det A)^{-1/2}` survive; the parameter set is the pullback along
`det : GL_4 -> C^*` of the squaring cover of `C^*`. It is connected because `det_* : pi_1(GL_4) -> pi_1(C^*)`
is an isomorphism (`GL_4(C) ≃ U(4)`, `pi_1 = Z` detected by `det`), so the pullback of a connected
cover is connected — this is the correct argument, and it is immaterial: the two branches differ by
`(I, -I, -I_6)`, which acts trivially. `tau' = (-I_6, I, I, tau)` gives the second component;
effective full stabilizer `PGL_4 ⋊ <tau'>`. `N_6 = S_(3,1) C^4` is the unique `45` in `T`, stable
under `PGL_4` and under `tau'` (`-1` on `V_sym`); the centre `mu_4` acts trivially on `T`. Hence
`C[N_6]^{S_eff} = ⊕_{m even} Sym^m(N_6^*)^{SL_4}` and `j_2(6) = 0`, `j_4(6) = 2`, `j_6(6) = 6`,
`dim J_{<=4} = 3` stand.

## 6. What was and was not affected

- Affected: the sealed sentence "connected double cover, hence connected" (invalid argument);
  the sealed description of `Stab_Gamma(K5)^0` by `c^2 det A = 1` (correct set only before the
  `SL_5` condition; the `SL_5` condition removes the `c mu = -1` branch).
- Not affected: the effective group (`PSp_4 ⋊ <tau'>`, `PGL_4 ⋊ <tau'>`), the identification and
  stability of `N`, `chi ≡ 1` on the stabilizer (new, and needed for the invariance of `f_z` under
  elements outside `SL_r x H^0`), the parity of `f_z`, all invariant counts, `dim J_{<=4}`, and every
  downstream statement of the sealed report and the follow-up that used them.
- Remaining adopted input: the six-variable commutant statement (classical).
