"""Bounded, read-only B16 evidence receiver. Never runs inherited mathematics.

Use through inspected b15_bound.py on Windows. Portable payloads use only the
standard library; an equivalent external resource supervisor is required elsewhere.
The accepted trust root is the reviewed manifest/code, not a submitted observation.
"""
import argparse
import copy
import hashlib
import json
import os
from pathlib import Path
import time

SCHEMA = "b16-11-receiver/1"
MAX_FILE = 16 * 1024**2
MAX_TOTAL = 64 * 1024**2
THREAD_KEYS = ("OPENBLAS_NUM_THREADS", "OMP_NUM_THREADS", "MKL_NUM_THREADS",
               "NUMEXPR_NUM_THREADS", "VECLIB_MAXIMUM_THREADS")


def need(ok, message):
    if not ok:
        raise ValueError(message)


def digest(data):
    return hashlib.sha256(data).hexdigest()


def read_json(path):
    need(path.stat().st_size <= MAX_FILE, "file size budget")
    return json.loads(path.read_text(encoding="utf-8-sig"))


def below(root, relative):
    p = Path(relative)
    need(not p.is_absolute() and ".." not in p.parts and ":" not in relative,
         "portable relative path required")
    q = (root / p).resolve()
    need(q.is_relative_to(root.resolve()), "path escapes root")
    return q


def check_resources(r, legacy=False):
    need(r.get("exit_code") == 0, "resource receipt lacks successful exit")
    need(r.get("job_object_enforced") is True, "Job Object missing")
    need(r.get("workers") == r.get("blas_threads") == 1, "worker/thread count")
    need(0 <= r["wall_seconds"] <= r["wall_cap_seconds"], "wall overrun")
    need(r["job_memory"]["peak_job_memory"] <= r["memory_cap_mb"] * 1024**2,
         "job memory overrun")
    if not legacy:
        need(r["wall_cap_seconds"] <= 60 and r["memory_cap_mb"] <= 512,
             "small control requires lease for larger caps")


def cell_key(c):
    required = {"n", "degree", "lambda", "ambient_variables", "field",
                "representation", "padding", "space"}
    need(set(c) == required, "complete cell key required")
    need(c["n"] == 4 and c["ambient_variables"] == 16 and c["field"] == "Q",
         "unsupported context")
    need(c["representation"] == "positive_partition_coordinate_HWV" and
         c["padding"] == "independent_z_per3_ten_essential_variables" and
         c["space"] == "orbit_closures", "representation/padding/closure context")
    d, lam = c["degree"], c["lambda"]
    need(type(d) is int and d >= 0 and isinstance(lam, list) and 0 < len(lam) <= 16,
         "degree/partition shape")
    need(all(type(x) is int and x > 0 for x in lam) and
         lam == sorted(lam, reverse=True) and sum(lam) == 4*d,
         "quartic weight-degree mismatch")
    return json.dumps(c, sort_keys=True)


def positive_gate(claim, trusted):
    """Only a receiver-owned registry can admit premises. No self-authorization.

    This batch ships an empty positive registry. Synthetic registries below are
    controls only and cannot admit an external research claim.
    """
    key = cell_key(claim["cell"])
    values = []
    for label, kind in (("ambient", "finite_ambient_exact"),
                        ("q", "global_det_ideal_floor"),
                        ("r", "actual_padding_coordinate_floor")):
        ref = claim[label]
        need(type(ref) is str and ref in trusted, "unreviewed premise: " + str(ref))
        e = trusted[ref]
        need(e["kind"] == kind and cell_key(e["cell"]) == key, "bound kind/cell mismatch")
        need(e.get("reviewed") is True and bool(e.get("proof_sha256")), "unreviewed proof")
        need(type(e["value"]) is int and e["value"] >= 0, "integer bound required")
        values.append(e["value"])
    a, q, r = values
    need(q <= a and r <= a, "inconsistent bounds")
    need(q+r > a, "insufficient inequality; NOT an exclusion")
    return {"D_lower": q+r-a, "a": a, "q": q, "r": r}


def controls():
    c = dict(n=4, degree=23, **{"lambda": [61,15]+[2]*8}, ambient_variables=16,
             field="Q", representation="positive_partition_coordinate_HWV",
             padding="independent_z_per3_ten_essential_variables", space="orbit_closures")
    reg = {k: dict(kind=kind, value=v, cell=c, reviewed=True, proof_sha256="test-only")
           for k,kind,v in (("a","finite_ambient_exact",2),
                            ("q","global_det_ideal_floor",1),
                            ("r","actual_padding_coordinate_floor",2))}
    claim = dict(cell=c, ambient="a", q="q", r="r")
    need(positive_gate(claim, reg)["D_lower"] == 1, "positive synthetic control")
    outcomes = [{"name":"synthetic_same_cell_positive", "status":"PASS", "research_evidence":False}]
    mutations = []
    def mutate(name, action):
        x, y = copy.deepcopy(claim), copy.deepcopy(reg)
        action(x,y)
        mutations.append((name,x,y))
    mutate("source_ceiling_as_padding_rank", lambda x,y: y["r"].update(kind="source_upper"))
    mutate("sampled_zero_as_global_equation", lambda x,y: y["q"].update(kind="sampled_kernel_dimension"))
    mutate("stable_count_as_finite_ambient", lambda x,y: y["a"].update(kind="stable_ambient"))
    def different_cell(x,y):
        # deepcopy preserves aliases: replace the q cell before altering it.
        y["q"]["cell"] = copy.deepcopy(c)
        y["q"]["cell"].update(degree=24, **{"lambda":[65,15]+[2]*8})
    mutate("cross_degree_join", different_cell)
    mutate("unreviewed_global_proof", lambda x,y: y["q"].update(reviewed=False))
    mutate("inequality_equality_is_inconclusive", lambda x,y: y["r"].update(value=1))
    mutate("inside_variable_padding", lambda x,y: x["cell"].update(padding="inside_variable_per3"))
    mutate("equation_nonzero_alone", lambda x,y: x.update(r="missing_full_cell_rank"))
    for name, x, y in mutations:
        try:
            positive_gate(x,y)
        except (ValueError, KeyError) as exc:
            outcomes.append(dict(name=name, status="REJECTED_AS_REQUIRED", reason=str(exc)))
        else:
            raise ValueError("mutation admitted: " + name)
    try:
        positive_gate(claim, {})
    except ValueError:
        outcomes.append(dict(name="self_authorized_observation", status="REJECTED_AS_REQUIRED"))
    else:
        raise ValueError("observation self-authorized")
    return outcomes


def arithmetic(cubic_rows):
    expected = [1,1,2,3,5,6,9,11,14,16,19,21,24,26,29,31,34,36]
    need([r["b"] for r in cubic_rows] == list(range(2,20)), "cubic channel index")
    need([r["stable_cubic_upper"] for r in cubic_rows] == expected, "inherited channel mismatch")
    sums = {t:sum(expected[:t-1]) for t in (15,17,19)}
    need(sums == {15:158,17:218,19:288}, "channel addition")
    finite = []
    for d,t,q,U in ((23,15,1,158),(25,17,2,218),(26,17,2,218),(27,19,5,288)):
        lam = [4*d-t-16,t]+[2]*8
        # Checking the d26 channel inequalities extends the inherited d25
        # chart bound; it is not an exact cubic or quartic recount.
        channels = [[3*d-14-b,b]+[2]*7 for b in range(2,t+1)]
        need(all(sum(mu)==3*d and all(lam[i]>=mu[i]>=lam[i+1]
                 for i in range(9)) for mu in channels), "Pieri channel inequalities")
        finite.append(dict(degree=d, **{"lambda":lam}, det_ideal_floor=q,
                           padding_upper=U, ambient=None, required_padding_floor="a-q+1",
                           known_q_feasible_only_if_a_at_most=q+U-1,
                           complete_ideal_upper_11_excludes_if_a_at_least=U+11,
                           exclusion_condition="Requires reviewed finite-to-stable ideal injection and i_det<=11.",
                           status="INCONCLUSIVE_WITHOUT_FINITE_AMBIENT_AND_ACTUAL_PADDING_FLOOR"))
    return dict(channel_sums=sums, stable=dict(a=429,m_det=418,m_pad=[243,288],
                D=[243-418,288-418],i_det=429-418,i_pad=[429-288,429-243]),
                ci159=dict(target_dimension=159,target_rank_floor=158,target_nullity_upper=1,
                           source_dimension=93,sampled_source_rank=88,sampled_kernel_dimension=5,
                           global_reducible_ideal_interval=[(93-88)-(159-158),93-88],
                           exact_source_entries=93*158),
                nine_row_transport=dict(source_degree=14,source_weight=[25,17]+[2]*7,
                    multiplier_degree=2,multiplier_weight=[4,4],target_degree=16,
                    target_weight=[29,21]+[2]*7,i_pad_floor=4,i_det_upper=4,D_upper=0,
                    conditional_on="reviewed nonzero q44 multiplication and stable ideal injection"),
                ambient_two=dict(earliest_recorded_safe_degree=19,weight=[57,4,3]+[2]*6,
                    generic_minor=5040*720,a=2,det_rank_floor=0,pad_rank_floor=0),
                finite_cells=finite)


def verify(package, input_root=None):
    m = read_json(package / "INPUT_HASHES.json")
    need(m["schema"] == SCHEMA, "manifest schema")
    need(len(m["inputs"]) < 512, "file count budget")
    total = 0
    for e in m["inputs"]:
        p = below(package,e["copy"])
        need(p.stat().st_size == e["bytes"] <= MAX_FILE, "payload preflight size")
        data = p.read_bytes()
        total += len(data)
        need(len(data) == e["bytes"] <= MAX_FILE and total <= MAX_TOTAL, "payload size mismatch/budget")
        need(digest(data)==e["sha256"], "hash mismatch: " + e["source"])
        if input_root:
            original = below(input_root,e["source"])
            need(digest(original.read_bytes()) == e["sha256"], "live input drift: " + e["source"])
    index = {e["source"]:e for e in m["inputs"]}
    def get(source):
        return read_json(below(package,index[source]["copy"]))
    launch = get("Batch16/launch/INPUT_MANIFEST.json")
    for row in launch["inputs"]:
        rel = row["path"].replace("\\","/").split("/gct-gpt/",1)[1]
        need(index[rel]["sha256"].lower()==row["sha256"].lower(), "frozen launch hash")
    g = get("work/batch15_workers/B15-11/results/b16_11/git_audit.json")
    need(g["manifest_sha256"]==index["Batch16/launch/INPUT_MANIFEST.json"]["sha256"], "Git receipt manifest")
    need(len(g["worktrees"])==12, "twelve worktrees")
    for expected, actual in zip(launch["worktrees"],g["worktrees"]):
        need(actual["slot"] == expected["slot"] and actual["frozen_head"]==expected["head"]
             and actual["frozen_tree"] == expected["tree"] and actual["frozen_object_type"]=="commit", "frozen object mismatch")
    audit = get("work/batch15_workers/B15-11/results/b16_11/audit.json")
    git_bindings = {(e["slot"], e["path"]):e for e in g["source_bindings"]}
    for b in audit["source_bindings"]:
        e = index[b["source"]]
        data = below(package,e["copy"]).read_bytes()
        def git_blob(value):
            return hashlib.sha1(b"blob "+str(len(value)).encode()+b"\0"+value).hexdigest()
        need(b["git_blob"] in (git_blob(data),git_blob(data.replace(b"\r\n",b"\n"))), "frozen source blob mismatch")
        suffix = b["source"].split("/B15-",1)[1]
        slot, rel = suffix.split("/",1)
        need(git_bindings[(slot,rel)]["ls_tree"].split()[2] == b["git_blob"], "source receipt join")
    for row in audit["full_replay_input_hash_checks"]:
        need(row["sha256"].lower()==row["expected"].lower(), "inherited replay manifest mismatch")
        if row["packaged"]:
            need(index[row["source"]]["sha256"]==row["expected"].lower(), "packaged replay input mismatch")
    intake_root = "Batch15_Launch/native_20260913/"
    final_deliveries = {e["slot"]:e for e in get(intake_root+"git_closeout/SUMMARY.json")}
    final_deliveries.update({e["slot"]:e for e in get(intake_root+"git_closeout/COMPLETED_DELIVERIES.json")})
    for w in launch["worktrees"]:
        p = final_deliveries[w["slot"]]["packaging"]
        need(p["status"]=="PASS" and p["head"]==w["head"] and p["head_tree"]==w["tree"], "closeout frozen-head join")
    prefix = "Batch15_Launch/native_20260913/reviews_filesystem/"
    cubic = get(prefix+"Dream_Upper288/cubic_bound.json")
    proof_arithmetic = arithmetic(cubic["rows"])
    dream = get(prefix+"Dream_Upper288/integrator_review.json")
    need(dream["claim"]["gap_interval"]==proof_arithmetic["stable"]["D"], "gap sign")
    need(dream["claim"]["padded_ideal_interval"]==proof_arithmetic["stable"]["i_pad"], "ideal complement")
    full = get(prefix+"B15-01_full_replay/integrator_review.json")
    check_resources(full["resources"], legacy=True)
    hessian = get(prefix+"Hessian11_1631/integrator_review.json")
    check_resources(hessian["resource_outcome"])
    need(full["status"]=="PASS_FULL_INDEPENDENT_REPLAY", "B15-01 review status")
    return dict(status="PASS_METADATA_AND_CONDITIONAL_ARITHMETIC", mathematical_replays=0,
                payload_files=len(m["inputs"]),payload_bytes=total, source_hashes_verified=True,
                fresh_scope="SHA256 integrity, frozen Git receipt joins, bound arithmetic, rejection controls",
                inherited_scope="All cited B15 mathematical certificates, character counts and proof acceptance",
                arithmetic=proof_arithmetic, controls=controls(),positive_claim_admitted=False,
                live_inputs_verified=input_root is not None,
                git_scope="Observed read-only receipt; portable mode does not query Git",
                limitations=m["limitations"])


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument("--package",type=Path,required=True)
    parser.add_argument("--input-root",type=Path)
    parser.add_argument("--output",type=Path)
    args=parser.parse_args()
    need(all(os.environ.get(k)=="1" for k in THREAD_KEYS), "one-thread environment required")
    need("CI73_DEADLINE" in os.environ, "run under inspected resource supervisor")
    start=time.perf_counter()
    result=verify(args.package,args.input_root)
    result["receiver_wall_seconds"]=time.perf_counter()-start
    if args.output:
        args.output.write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8")
    print(json.dumps({k:result[k] for k in ("status","payload_files","payload_bytes","mathematical_replays","positive_claim_admitted","receiver_wall_seconds")}))


if __name__ == "__main__":
    main()
