#!/usr/bin/env python3
"""Session 61: a third engine for the polar counts — msolve on the Rabinowitsch form.

The polar scheme of slot k on the chart t_0 = 1, with the excess removed by the trick
s*g - 1 = 0 (g a random combination of the restricted partials, which vanishes on the
excess Sing meet Lambda and, with probability about #points/p, at a legitimate point —
a disagreement with the saturation count would show that):

    G(1, t_1..t_{k+1}) = m_1 = ... = m_k = 0,   s * g(1, t) = 1        in  F_p[t_1..t_{k+1}, s].

This is a zero-dimensional system with no saturation step at all; msolve's F4 + FGLM
reports its degree (the number of solutions with multiplicity), which must equal
delta_k.  The polynomials are produced by Singular from the SAME random draws as the
saturation runs (same seed -> same Lambda, m_i, g).

    python3 analysis/wk9_s61_msolve.py --form det4 --prime 2147483647 --seed 61 --k 6
"""
import argparse, os, re, resource, subprocess, sys, time
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import random
from wk9_s61_polar import build_form, HERE, REPO

def make_polys(form, nvars, Fexpr, prime, seed, k, rng_range=99):
    """Run Singular to expand G, the k combinations m_i and g on the chart t(0)=1; return strings."""
    N = nvars - 1
    rng = random.Random(seed * 1_000_003 + k * 1009 + prime % 1_000_003)
    V = [[rng.randint(-rng_range, rng_range) for _ in range(nvars)] for _ in range(k + 2)]
    C = [[rng.randint(-rng_range, rng_range) for _ in range(nvars)] for _ in range(k)]
    ellB = [rng.randint(-rng_range, rng_range) for _ in range(k + 2)]
    gcomb = [rng.randint(-rng_range, rng_range) for _ in range(nvars)]
    lines = [f'ring R = {prime}, (x(0..{N})), dp;', f'poly F = {Fexpr};', 'ideal J = jacob(F);',
             f'ring S = {prime}, (t(0..{k+1}), s), dp;']
    imgs = ["+".join(f"({V[j][i]})*t({j})" for j in range(k + 2)) for i in range(nvars)]
    lines.append(f'ideal images = {", ".join(imgs)};')
    lines.append('map phi = R, images;')
    lines.append('poly G = subst(phi(F), t(0), 1);')
    lines.append('ideal Jt = phi(J);')
    lines.append('print("MSOLVE_POLY " + string(G));')
    for i in range(k):
        comb = "+".join(f"({C[i][a]})*Jt[{a+1}]" for a in range(nvars))
        lines.append(f'poly m{i} = subst({comb}, t(0), 1); print("MSOLVE_POLY " + string(m{i}));')
    gexpr = "+".join(f"({gcomb[a]})*Jt[{a+1}]" for a in range(nvars))
    lines.append(f'poly g = subst({gexpr}, t(0), 1); poly rab = s*g - 1; print("MSOLVE_G " + string(rab));')
    lines.append('quit;')
    script = "\n".join(lines) + "\n"
    out = subprocess.run(["Singular", "-q"], input=script, capture_output=True, text=True, timeout=600).stdout
    polys = [l.split(" ", 1)[1] for l in out.splitlines() if l.startswith("MSOLVE_POLY ")]
    g = [l.split(" ", 1)[1] for l in out.splitlines() if l.startswith("MSOLVE_G ")][0]   # expanded s*g - 1
    fix = lambda s: re.sub(r"t\((\d+)\)", r"t\1", s)
    return [fix(p) for p in polys], fix(g)

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--form", required=True)
    ap.add_argument("--prime", type=int, default=2147483647)
    ap.add_argument("--seed", type=int, default=61)
    ap.add_argument("--k", type=int, required=True)
    ap.add_argument("--timeout", type=int, default=7200)
    ap.add_argument("--mem-kb", type=int, default=6_000_000)
    ap.add_argument("--threads", type=int, default=1)
    a = ap.parse_args()
    nvars, Fexpr, desc = build_form(a.form, a.seed)
    polys, g = make_polys(a.form, nvars, Fexpr, a.prime, a.seed, a.k)
    run = f"{a.form}_p{a.prime}_s{a.seed}_k{a.k}_msolve"
    os.makedirs(os.path.join(REPO, "results", "s61_sing"), exist_ok=True)
    inp = os.path.join(REPO, "results", "s61_sing", run + ".ms")
    log = os.path.join(REPO, "results", "logs", "s61_" + run + ".log")
    pidf = os.path.join(REPO, "results", "logs", "s61_" + run + ".pid")
    with open(inp, "w") as f:
        f.write(",".join([f"t{j}" for j in range(1, a.k + 2)] + ["s"]) + "\n")
        f.write(f"{a.prime}\n")
        allp = polys + [g]   # g here is the expanded Rabinowitsch polynomial s*g - 1 (msolve does not parse parentheses)
        f.write(",\n".join(allp) + "\n")
    def limits():
        resource.setrlimit(resource.RLIMIT_AS, (a.mem_kb * 1024, a.mem_kb * 1024))
    t0 = time.time()
    with open(log, "w") as lf:
        lf.write(f"# msolve run {run}: {desc}; slot k={a.k}, chart t0=1, Rabinowitsch variable s for g\n")
        lf.flush()
        proc = subprocess.Popen(["timeout", str(a.timeout), "msolve", "-v", "2", "-t", str(a.threads), "-f", inp, "-o", inp + ".out"],
                                stdout=lf, stderr=subprocess.STDOUT, preexec_fn=limits)
        time.sleep(0.3)
        kids = ""
        try:
            kids = open(f"/proc/{proc.pid}/task/{proc.pid}/children").read().strip()
        except OSError:
            pass
        with open(pidf, "w") as pf:
            pf.write(f"{proc.pid} {kids}".strip() + "\n")
        rc = proc.wait()
    txt = open(log).read()
    m = re.search(r"dimension of quotient\s*:?\s*(\d+)|degree of ideal\s*:?\s*(\d+)|#solutions\s*[:=]?\s*(\d+)|\bdegree\s*[:=]\s*(\d+)", txt, re.I)
    deg = next((g for g in m.groups() if g), None) if m else None
    if deg is None and re.search(r"No solution", txt):
        deg = "0"
    print(f"{run}: rc={rc} {time.time()-t0:.0f}s degree={deg}")
    with open(log, "a") as lf:
        lf.write(f"MSOLVE_RESULT form={a.form} p={a.prime} seed={a.seed} k={a.k} degree={deg} rc={rc} sec={time.time()-t0:.0f}\n")
    return 0

if __name__ == "__main__":
    sys.exit(main())
