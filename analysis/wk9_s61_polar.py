#!/usr/bin/env python3
"""Session 61 -- polar profiles of hypersurfaces by saturated polar ideals (Singular).

    python3 analysis/wk9_s61_polar.py --form det4 --prime 2147483647 --seed 61 \
        [--ks 0,1,2,3] [--radical 1] [--range 99] [--timeout 7200] [--mem-kb 6000000]

Writes the Singular script to results/s61_sing/<run>.sing, the raw Singular output to
results/logs/s61_<run>.log, the process id to results/logs/s61_<run>.pid, and the parsed
results to results/s61_runs/<run>.json.  The run name is <form>_p<prime>_s<seed>.

Every random choice (the basis of Lambda, the k combinations of partials, the second
chart, and for the seeded forms lc / detpencil10 / cubic9 the form itself) is drawn from
random.Random with the seeds printed in the log, so every count is reproducible.

Convention: results/PREREG_s61.md section 0a.  Method: analysis/wk9_s61_polar.lib.
"""
import argparse, itertools, json, os, random, re, resource, subprocess, sys, time

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(HERE)
P1, P2 = 2147483647, 2147483629

# ---------------------------------------------------------------- the forms
def det_expr(M):
    """Leibniz expansion of det of a square matrix of Singular expressions."""
    n = len(M)
    terms = []
    for perm in itertools.permutations(range(n)):
        sgn = 1
        p = list(perm)
        for i in range(n):
            for j in range(i + 1, n):
                if p[i] > p[j]:
                    sgn = -sgn
        mon = "*".join(M[i][perm[i]] for i in range(n))
        terms.append(("+" if sgn > 0 else "-") + mon)
    return "0" + "".join(terms)

def per_expr(M):
    n = len(M)
    return "+".join("*".join(M[i][perm[i]] for i in range(n))
                    for perm in itertools.permutations(range(n)))

def random_form_expr(nvars, degree, rng, lo=-99, hi=99):
    """A random form of the given degree in x(0..nvars-1), all monomials, integer coeffs."""
    terms = []
    for expo in itertools.combinations_with_replacement(range(nvars), degree):
        c = rng.randint(lo, hi)
        if c == 0:
            continue
        mon = "*".join(f"x({i})" for i in expo)
        terms.append(f"({c})*{mon}")
    return "+".join(terms) if terms else "0"

def build_form(name, seed):
    """Return (nvars, singular_expression, description)."""
    rng = random.Random(10_000 + seed)   # form seed, independent of the per-k draws
    if name == "det4":
        M = [[f"x({4*i+j})" for j in range(4)] for i in range(4)]
        return 16, det_expr(M), "det_4 of the generic 4x4 matrix, 16 variables"
    if name == "det3":
        M = [[f"x({3*i+j})" for j in range(3)] for i in range(3)]
        return 9, det_expr(M), "det_3 of the generic 3x3 matrix, 9 variables (control: profile (3,6,12,12,6,0,0,0))"
    if name == "per3":
        M = [[f"x({3*i+j})" for j in range(3)] for i in range(3)]
        return 9, per_expr(M), "per_3 of the generic 3x3 matrix, 9 variables"
    if name == "pad":
        M = [[f"x({1+3*i+j})" for j in range(3)] for i in range(3)]
        return 10, f"x(0)*({per_expr(M)})", "the full ten-variable padded permanent x_0 * per_3(x_1..x_9)"
    if name == "pad16":
        M = [[f"x({1+3*i+j})" for j in range(3)] for i in range(3)]
        return 16, f"x(0)*({per_expr(M)})", "the padded permanent x_0 * per_3(x_1..x_9) as a quartic in all 16 variables (x_10..x_15 unused): the actual GCT object"
    if name == "perdual":
        # the dual hypersurface of per_3, found by implicitisation in analysis/wk9_s61_dual.m2 and
        # verified over Q in results/logs/s61_dual_identity.log:  4 per(BoB) - 2 per(B)^2 - det(B)^2
        M = [[f"x({3*i+j})" for j in range(3)] for i in range(3)]
        perBB = "+".join("*".join(f"x({3*i+p[i]})^2" for i in range(3)) for p in itertools.permutations(range(3)))
        return 9, f"4*({perBB}) - 2*({per_expr(M)})^2 - ({det_expr(M)})^2", "the dual sextic of per_3: 4 per(BoB) - 2 per(B)^2 - det(B)^2 (control: by biduality its profile must be the reversed profile of per_3)"
    if name == "lc":
        lin = "+".join(f"({rng.randint(-99,99)})*x({i})" for i in range(10))
        cub = random_form_expr(10, 3, rng)
        return 10, f"({lin})*({cub})", f"reducible l*c, l and c random in 10 variables (form seed {10_000+seed})"
    if name == "detpencil10":
        A = [[[rng.randint(-9, 9) for _ in range(4)] for _ in range(4)] for _ in range(10)]
        M = [[ "+".join(f"({A[a][i][j]})*x({a})" for a in range(10)) for j in range(4)] for i in range(4)]
        M = [[f"({e})" for e in row] for row in M]
        return 10, det_expr(M), f"det_4(sum_a x_a A_a), ten random integer 4x4 matrices (form seed {10_000+seed})"
    if name == "cubic9":
        return 9, random_form_expr(9, 3, rng), f"a random cubic in 9 variables (control: smooth, profile 3*2^k; form seed {10_000+seed})"
    raise SystemExit(f"unknown form {name}")

# ---------------------------------------------------------------- the script
def singular_script(form, nvars, Fexpr, prime, seed, ks, do_radical, rng_range, sat_mode):
    N = nvars - 1
    char = prime if prime > 0 else 0
    lines = []
    lines.append(f'LIB "{HERE}/wk9_s61_polar.lib";')
    lines.append(f'int rt0 = rtimer;')
    lines.append(f'ring R = {char}, (x(0..{N})), dp;')
    lines.append(f'poly F = {Fexpr};')
    lines.append(f'ideal J = jacob(F);')
    lines.append(f'print("FORM {form} nvars={nvars} char={char} seed={seed} degF=" + string(deg(F)) + " npartials=" + string(ncols(J)));')
    for k in ks:
        rng = random.Random(seed * 1_000_003 + k * 1009 + prime % 1_000_003)
        V = [[rng.randint(-rng_range, rng_range) for _ in range(nvars)] for _ in range(k + 2)]
        C = [[rng.randint(-rng_range, rng_range) for _ in range(nvars)] for _ in range(k)]
        ellB = [rng.randint(-rng_range, rng_range) for _ in range(k + 2)]
        gcomb = [rng.randint(-rng_range, rng_range) for _ in range(nvars)]
        lines.append(f'// ---- slot k = {k}')
        lines.append(f'ring S{k} = {char}, (t(0..{k+1})), dp;')
        imgs = []
        for i in range(nvars):
            imgs.append("+".join(f"({V[j][i]})*t({j})" for j in range(k + 2)))
        lines.append(f'ideal images = {", ".join(imgs)};')
        lines.append(f'map phi = R, images;')
        lines.append(f'poly G = phi(F);')
        lines.append(f'ideal Jt = phi(J);')
        if k > 0:
            entries = ", ".join(str(C[i][a]) for i in range(k) for a in range(nvars))
            lines.append(f'matrix C[{k}][{nvars}] = {entries};')
        else:
            lines.append(f'matrix C[1][{nvars}];')
        lines.append(f'poly ellA = t(0);')
        lines.append(f'poly ellB = ' + "+".join(f"({ellB[j]})*t({j})" for j in range(k + 2)) + ';')
        lines.append(f'poly g = ' + "+".join(f"({gcomb[a]})*Jt[{a+1}]" for a in range(nvars)) + ';')
        lines.append(f'int rt1 = rtimer;')
        lines.append(f'int rt2;')
        lines.append(f'int rt3;')
        lines.append(f'int degE = -1;')
        lines.append(f'int dimE = -2;')
        lines.append(f'int degp_g = -1;')
        lines.append(f'int dim_g = -2;')
        lines.append(f'int degr = -1;')
        lines.append(f'int vdB = -1;')
        lines.append(f'ideal E = std(Jt);')
        lines.append(f'dimE = dim(E); if (dimE >= 1) {{ degE = mult(E); }}')
        lines.append(f'print("EXCESS k={k} dim=" + string(dimE) + " deg=" + string(degE));')
        lines.append(f'ideal Is = polar_sat(G, Jt, C, {k});')
        lines.append(f'list L = list(dim(Is), 0, -1);')
        lines.append(f'if (L[1] >= 0) {{ L[2] = mult(Is); }}')
        lines.append(f'if (L[1] == 1) {{ L[3] = vdim(std(Is + (ellA - 1))); vdB = vdim(std(Is + (ellB - 1))); }}')
        lines.append(f'if (L[1] == -1) {{ L[3] = 0; vdB = 0; }}')
        lines.append(f'rt2 = rtimer;')
        lines.append(f'print("COUNT form={form} p={char} seed={seed} k={k} dim=" + string(L[1]) + " degp=" + string(L[2]) + " vdA=" + string(L[3]) + " vdB=" + string(vdB) + " excess_dim=" + string(dimE) + " excess_deg=" + string(degE) + " sec=" + string(rt2 - rt1));')
        if sat_mode in ("both", "g"):
            lines.append(f'list Lg = polar_count_g(G, Jt, C, ellA, g, {k});')
            lines.append(f'print("COUNTG form={form} p={char} seed={seed} k={k} dim=" + string(Lg[1]) + " degp=" + string(Lg[2]));')
        if do_radical:
            lines.append(f'if (L[1] == 1) {{ ideal Ir = std(radical(Is)); degr = mult(Ir); }}')
            lines.append(f'if (L[1] == -1) {{ degr = 0; }}')
            lines.append(f'rt3 = rtimer;')
            lines.append(f'print("RADICAL form={form} p={char} seed={seed} k={k} degp=" + string(L[2]) + " degr=" + string(degr) + " reduced=" + string(L[2] == degr) + " sec=" + string(rt3 - rt2));')
        lines.append(f'kill S{k};')
        lines.append(f'setring R;')
    lines.append(f'print("DONE form={form} p={char} seed={seed} total_sec=" + string(rtimer - rt0));')
    lines.append('quit;')
    return "\n".join(lines) + "\n"

def m2_script(form, nvars, Fexpr, prime, seed, ks, do_radical, rng_range):
    """The same computation for Macaulay2 (independent engine), with the SAME random
    draws as the Singular script for the same (form, prime, seed, k), so the two engines
    are handed the same scheme.  x(i) -> x_i, t(j) -> t_j in the expressions."""
    N = nvars - 1
    kk = "QQ" if prime == 0 else f"ZZ/{prime}"
    Fm2 = re.sub(r"x\((\d+)\)", r"x_\1", Fexpr)
    lines = []
    lines.append(f'R = {kk}[x_0..x_{N}];')
    lines.append(f'F = {Fm2};')
    lines.append(f'J = ideal apply(gens R, v -> diff(v, F));')
    lines.append(f'print("FORM {form} nvars={nvars} char={0 if prime == 0 else prime} seed={seed} degF=" | toString(first degree F) | " npartials=" | toString(numgens J));')
    for k in ks:
        rng = random.Random(seed * 1_000_003 + k * 1009 + prime % 1_000_003)
        V = [[rng.randint(-rng_range, rng_range) for _ in range(nvars)] for _ in range(k + 2)]
        C = [[rng.randint(-rng_range, rng_range) for _ in range(nvars)] for _ in range(k)]
        ellB = [rng.randint(-rng_range, rng_range) for _ in range(k + 2)]
        gcomb = [rng.randint(-rng_range, rng_range) for _ in range(nvars)]
        lines.append(f'-- ---- slot k = {k}')
        lines.append(f'S = {kk}[t_0..t_{k+1}];')
        imgs = ["+".join(f"({V[j][i]})*t_{j}" for j in range(k + 2)) for i in range(nvars)]
        lines.append(f'phi = map(S, R, {{{", ".join(imgs)}}});')
        lines.append(f'G = phi F;')
        lines.append(f'Jt = phi J;')
        lines.append(f'Jl = flatten entries gens Jt;')
        combos = []
        for i in range(k):
            combos.append("+".join(f"({C[i][a]})*Jl#{a}" for a in range(nvars)))
        lines.append(f'I = ideal(G)' + ("".join(f" + ideal({c})" for c in combos)) + ';')
        lines.append(f'ellA = t_0;')
        lines.append(f'ellB = ' + "+".join(f"({ellB[j]})*t_{j}" for j in range(k + 2)) + ';')
        lines.append(f'tm = cpuTime();')
        lines.append(f'E = Jt;')
        lines.append(f'dimE = dim E; degE = if dimE >= 1 then degree E else -1;')
        lines.append(f'Is = saturate(I, Jt);')
        lines.append(f'd = dim Is;')
        lines.append(f'degp = if d >= 0 then degree Is else 0;')
        lines.append(f'vdA = if d == 1 then degree(Is + ideal(ellA - 1)) else (if d == -1 then 0 else -1);')
        lines.append(f'vdB = if d == 1 then degree(Is + ideal(ellB - 1)) else (if d == -1 then 0 else -1);')
        lines.append(f'print("COUNT form={form} p={0 if prime == 0 else prime} seed={seed} k={k} dim=" | toString d | " degp=" | toString degp | " vdA=" | toString vdA | " vdB=" | toString vdB | " excess_dim=" | toString dimE | " excess_deg=" | toString degE | " sec=" | toString floor(cpuTime() - tm));')
        if do_radical:
            lines.append(f'tm2 = cpuTime();')
            lines.append(f'degr = if d == 1 then degree radical Is else (if d == -1 then 0 else -1);')
            lines.append(f'print("RADICAL form={form} p={0 if prime == 0 else prime} seed={seed} k={k} degp=" | toString degp | " degr=" | toString degr | " reduced=" | (if degp == degr then "1" else "0") | " sec=" | toString floor(cpuTime() - tm2));')
    lines.append(f'print("DONE form={form} p={0 if prime == 0 else prime} seed={seed}");')
    return "\n".join(lines) + "\n"

# ---------------------------------------------------------------- running
def run(args):
    nvars, Fexpr, desc = build_form(args.form, args.seed)
    ks = [int(s) for s in args.ks.split(",")] if args.ks else list(range(nvars - 1))
    run_name = f"{args.form}_p{args.prime}_s{args.seed}" + (f"_k{args.ks.replace(',', '-')}" if args.ks else "") + ("_m2" if args.engine == "m2" else "") + (args.tag or "")
    os.makedirs(os.path.join(REPO, "results", "s61_sing"), exist_ok=True)
    os.makedirs(os.path.join(REPO, "results", "s61_runs"), exist_ok=True)
    os.makedirs(os.path.join(REPO, "results", "logs"), exist_ok=True)
    script_path = os.path.join(REPO, "results", "s61_sing", run_name + (".m2" if args.engine == "m2" else ".sing"))
    log_path = os.path.join(REPO, "results", "logs", "s61_" + run_name + ".log")
    pid_path = os.path.join(REPO, "results", "logs", "s61_" + run_name + ".pid")
    json_path = os.path.join(REPO, "results", "s61_runs", run_name + ".json")
    with open(script_path, "w") as f:
        if args.engine == "m2":
            f.write(m2_script(args.form, nvars, Fexpr, args.prime, args.seed, ks, args.radical, args.range))
        else:
            f.write(singular_script(args.form, nvars, Fexpr, args.prime, args.seed, ks,
                                    args.radical, args.range, args.sat))
    cmd = ["timeout", str(args.timeout)] + (["M2", "--script", script_path] if args.engine == "m2" else ["Singular", "-q", script_path])
    def limits():
        resource.setrlimit(resource.RLIMIT_AS, (args.mem_kb * 1024, args.mem_kb * 1024))
    t0 = time.time()
    with open(log_path, "w") as log:
        log.write(f"# session 61 polar profile run {run_name}\n# form: {desc}\n# engine={args.engine} ks={ks} prime={args.prime} seed={args.seed} range={args.range} radical={args.radical} sat={args.sat}\n# timeout {args.timeout}s, ulimit -v {args.mem_kb} kB\n")
        log.flush()
        proc = subprocess.Popen(cmd, stdout=log, stderr=subprocess.STDOUT, preexec_fn=limits)
        time.sleep(0.5)
        # record the wrapper pid and the engine's own pid (child of `timeout`)
        kids = ""
        try:
            with open(f"/proc/{proc.pid}/task/{proc.pid}/children") as cf:
                kids = cf.read().strip()
        except OSError:
            pass
        with open(pid_path, "w") as pf:
            pf.write(f"{proc.pid} {kids}\n".strip() + "\n")
        rc = proc.wait()
    elapsed = time.time() - t0
    results = {"run": run_name, "engine": args.engine, "form": args.form, "form_description": desc, "nvars": nvars,
               "prime": args.prime, "seed": args.seed, "ks": ks, "range": args.range,
               "sat_mode": args.sat, "timeout_s": args.timeout, "mem_kb": args.mem_kb,
               "returncode": rc, "elapsed_s": round(elapsed, 1), "counts": {}, "countg": {},
               "radical": {}, "excess": {}}
    with open(log_path) as log:
        for line in log:
            m = re.match(r"COUNT form=\S+ p=(\d+) seed=(\d+) k=(\d+) dim=(-?\d+) degp=(-?\d+) vdA=(-?\d+) vdB=(-?\d+) excess_dim=(-?\d+) excess_deg=(-?\d+) sec=(\d+)", line)
            if m:
                k = int(m.group(3))
                results["counts"][k] = {"dim": int(m.group(4)), "degp": int(m.group(5)),
                                        "vdA": int(m.group(6)), "vdB": int(m.group(7)), "sec": int(m.group(10))}
                results["excess"][k] = {"dim": int(m.group(8)), "deg": int(m.group(9))}
            m = re.match(r"COUNTG form=\S+ p=(\d+) seed=(\d+) k=(\d+) dim=(-?\d+) degp=(-?\d+)", line)
            if m:
                results["countg"][int(m.group(3))] = {"dim": int(m.group(4)), "degp": int(m.group(5))}
            m = re.match(r"RADICAL form=\S+ p=(\d+) seed=(\d+) k=(\d+) degp=(-?\d+) degr=(-?\d+) reduced=(\d) sec=(\d+)", line)
            if m:
                results["radical"][int(m.group(3))] = {"degp": int(m.group(4)), "degr": int(m.group(5)),
                                                       "reduced": bool(int(m.group(6))), "sec": int(m.group(7))}
    prof = [results["counts"].get(k, {}).get("degp") for k in ks]
    results["profile"] = prof
    with open(json_path, "w") as f:
        json.dump(results, f, indent=1, sort_keys=True)
    print(f"{run_name}: rc={rc} {elapsed:.0f}s profile={prof}")
    return rc

if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--form", required=True)
    ap.add_argument("--prime", type=int, default=P1, help="0 for QQ")
    ap.add_argument("--seed", type=int, default=61)
    ap.add_argument("--ks", default="")
    ap.add_argument("--radical", type=int, default=1)
    ap.add_argument("--range", type=int, default=99)
    ap.add_argument("--sat", default="both", choices=["full", "g", "both"])
    ap.add_argument("--timeout", type=int, default=7200)
    ap.add_argument("--mem-kb", type=int, default=6_000_000)
    ap.add_argument("--tag", default="")
    ap.add_argument("--engine", default="singular", choices=["singular", "m2"])
    sys.exit(run(ap.parse_args()))
