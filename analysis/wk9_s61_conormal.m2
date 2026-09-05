-- Session 61: the conormal variety of {per_3 = 0} in P^8 x P^8*, and its multidegree,
-- as a methodologically independent route to the whole polar profile at once
-- (PREREG_s61.md section 2, "third route").  Also det_3 as the control, whose profile
-- (3,6,12,12,6,0,0,0) is classical.
--
-- Bigraded ring: x_0..x_8 of degree {1,0}, y_0..y_8 of degree {0,1}.  The conormal
-- ideal is (F, 2x2 minors of [y ; grad F]) saturated by the Jacobian ideal (grad F),
-- which removes the excess component Sing(X) x P^8*.  `multidegree' returns
-- sum_k delta_k T_0^(k+1) T_1^(8-k) (up to the convention on which factor is which,
-- fixed by the control), so the coefficient list is the profile.
--
-- usage: M2 --script analysis/wk9_s61_conormal.m2 <form> <prime>
--   form in {per3, det3}, prime 0 for QQ.
form = if #scriptCommandLine > 1 then scriptCommandLine#1 else "det3";
p = if #scriptCommandLine > 2 then value scriptCommandLine#2 else 32003;
kk = if p == 0 then QQ else ZZ/p;
R = kk[x_0..x_8, y_0..y_8, Degrees => join(toList(9:{1,0}), toList(9:{0,1}))];
M = genericMatrix(R, x_0, 3, 3);
F = if form == "per3" then (
        sum apply(permutations 3, s -> product apply(3, i -> M_(i, s#i)))
    ) else det M;
grad = matrix{apply(9, i -> diff(x_i, F))};
Y = matrix{toList(y_0..y_8)};
C = ideal(F) + minors(2, grad || Y);
Jac = ideal grad;
tm = cpuTime();
Csat = saturate(C, Jac);
stderr << "saturation done in " << floor(cpuTime() - tm) << " s" << endl;
print("FORM " | form | " char=" | toString p);
print("dim (affine, bigraded cone) = " | toString dim Csat | "  expected 9 (= dim C(X) + 2 = 7 + 2)");
md = multidegree Csat;
print("MULTIDEGREE " | toString md);
-- coefficient extraction: multidegree lives in ZZ[T_0, T_1]; delta_k is the coefficient of
-- T_0^(9-1-k+1)... we simply list (exponent pair, coefficient) and let the report read it.
A = ring md;
print("TERMS " | toString apply(listForm md, t -> {t#0, t#1}));
print("DONE");
