#!/usr/bin/env python3
"""Session 61: collect every polar-profile run into results/s61_profiles.json and print the
comparison table.  Reads results/s61_runs/*.json (written by wk9_s61_polar.py) and the
conormal-multidegree logs (results/logs/s61_conormal_*.log)."""
import glob, json, os, re, sys

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DET4 = [4, 12, 36, 68, 84, 60, 20, 0]

def main():
    runs = []
    for f in sorted(glob.glob(os.path.join(REPO, "results", "s61_runs", "*.json"))):
        r = json.load(open(f))
        runs.append(r)
    by_form = {}
    for r in runs:
        by_form.setdefault(r["form"], []).append(r)
    out = {"determinant_reference": DET4, "forms": {}}
    print(f"{'run':44s} {'engine':8s} {'sat':5s} profile")
    for form, rs in sorted(by_form.items()):
        profiles = {}
        for r in sorted(rs, key=lambda r: r["run"]):
            prof = {int(k): v for k, v in ((k, r["counts"][k]["degp"]) for k in r["counts"])}
            profiles[r["run"]] = prof
            ks = r["ks"]
            vec = [prof.get(k) for k in ks]
            chartsA = [r["counts"][str(k)]["vdA"] if str(k) in r["counts"] else None for k in ks]
            chartsB = [r["counts"][str(k)]["vdB"] if str(k) in r["counts"] else None for k in ks]
            g = [r["countg"].get(str(k), {}).get("degp") for k in ks] if r.get("countg") else None
            red = [r["radical"].get(str(k), {}).get("reduced") for k in ks] if r.get("radical") else None
            flags = []
            if chartsA != vec or chartsB != vec:
                flags.append(f"CHART MISMATCH A={chartsA} B={chartsB}")
            if g and any(x is not None for x in g) and g != vec:
                flags.append(f"single-g saturation differs: {g}")
            if red and any(x is not None for x in red) and not all(x in (True, None) for x in red):
                flags.append(f"non-reduced slots: {[k for k, x in zip(ks, red) if x is False]}")
            print(f"{r['run']:44s} {r.get('engine','singular'):8s} {r.get('sat_mode','-'):5s} k={ks[0]}..{ks[-1]}: {vec}" + (f"  rc={r['returncode']}" if r["returncode"] else "") + ("  " + "; ".join(flags) if flags else ""))
        # consensus per slot
        consensus = {}
        for run, prof in profiles.items():
            for k, v in prof.items():
                consensus.setdefault(k, set()).add(v)
        out["forms"][form] = {"runs": {run: {str(k): v for k, v in prof.items()} for run, prof in profiles.items()},
                              "consensus": {str(k): (sorted(v)[0] if len(v) == 1 else sorted(v)) for k, v in sorted(consensus.items())},
                              "description": rs[0]["form_description"]}
        cons = out["forms"][form]["consensus"]
        disagreement = [k for k, v in cons.items() if isinstance(v, list)]
        print(f"   -> {form} consensus: {[cons.get(str(k)) for k in range(max(consensus)+1)]}" + (f"   DISAGREEMENT at k={disagreement}" if disagreement else ""))
    # conormal multidegree logs
    out["conormal_multidegree"] = {}
    for f in sorted(glob.glob(os.path.join(REPO, "results", "logs", "s61_conormal_*.log"))):
        txt = open(f).read()
        m = re.search(r"TERMS (.*)", txt)
        fm = re.search(r"FORM (\S+) char=(\d+)", txt)
        if m and fm:
            terms = eval(m.group(1).replace("{", "[").replace("}", "]"))
            prof = {}
            for (e0, e1), c in terms:
                prof[e0 - 1] = c      # coefficient of T_0^(k+1) T_1^(8-k) is delta_k
            vec = [prof.get(k, 0) for k in range(8)]
            out["conormal_multidegree"][f"{fm.group(1)}_p{fm.group(2)}"] = vec
            print(f"conormal multidegree {fm.group(1)} p={fm.group(2)}: {vec}")
    # msolve (third engine, Rabinowitsch form) results
    out["msolve"] = {}
    for f in sorted(glob.glob(os.path.join(REPO, "results", "logs", "s61_*_msolve.log"))):
        for line in open(f):
            m = re.match(r"MSOLVE_RESULT form=(\S+) p=(\d+) seed=(\d+) k=(\d+) degree=(\S+) rc=(-?\d+)", line)
            if m:
                key = f"{m.group(1)}_p{m.group(2)}_s{m.group(3)}"
                out["msolve"].setdefault(key, {})[m.group(4)] = (int(m.group(5)) if m.group(5) != "None" else None)
    for key, prof in sorted(out["msolve"].items()):
        ks = sorted(int(k) for k in prof)
        print(f"msolve {key:36s} k={ks[0]}..{ks[-1]}: {[prof[str(k)] for k in ks]}")
    with open(os.path.join(REPO, "results", "s61_profiles.json"), "w") as fo:
        json.dump(out, fo, indent=1, sort_keys=True)
    return 0

if __name__ == "__main__":
    sys.exit(main())
