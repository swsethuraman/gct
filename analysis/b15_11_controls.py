"""Liveness, scope, arithmetic, cross-model and semantic-defect controls."""
import copy
import importlib.util
import json
from pathlib import Path
import tempfile
import time

from b15_11_memory import (ROOT, Memory, canonical_digest, cell, close_intervals, digest,
                           coordinate_transport, normalize_record, verify_native)


def main():
    start = time.perf_counter()
    out = ROOT/"results/b15_11"
    checks = []
    def check(name, condition):
        if not condition:
            raise AssertionError(name)
        checks.append(dict(name=name, passed=True))
    memory = Memory()
    fixtures = {
        "LMR": cell(4, 24, [65, 17]+[2]*7),
        "tail19": cell(4, 25, [67, 19]+[2]*7),
        "tail21": cell(4, 26, [69, 21]+[2]*7),
        "peaked": cell(4, 7, [16]+[2]*6),
        "session12": cell(4, 8, [12, 4, 4, 4, 4, 4]),
        "historical_pilot": cell(4, 8, [10, 6, 6, 6, 2, 2]),
        "open_a1": cell(4, 7, [11, 8, 5, 1, 1, 1, 1]),
        "open_a_gt1": cell(4, 8, [13, 11, 3, 2, 1, 1, 1]),
    }
    results = {name: memory.query(c) for name, c in fixtures.items()}
    for name, c in fixtures.items():
        (out/("cell_"+name+".json")).write_text(json.dumps(c, indent=2)+"\n", encoding="utf-8")
    check("LMR accepted arithmetic [-4,-2]", [results["LMR"]["bounds"][k] for k in ("D_lb", "D_ub")] == [-4, -2])
    check("tail19 reviewed D<=-1", results["tail19"]["bounds"]["D_ub"] == -1)
    check("tail21 unresolved finite U_pad528", results["tail21"]["decision"] == "UNRESOLVED" and results["tail21"]["bounds"]["U_pad_ub"] == 528)
    check("peaked applies", results["peaked"]["decision"] == "EXCLUDED_D_POSITIVE")
    check("session12 missing portable witness stays recorded", results["session12"]["status"] == "RECORDED" and results["session12"]["decision"] == "UNRESOLVED")
    check("historical pilot missing portable witness stays recorded", results["historical_pilot"]["status"] == "RECORDED")
    for name, a in (("open_a1", 1), ("open_a_gt1", 2)):
        check(name+" no inferred determinant rank", results[name]["decision"] == "UNRESOLVED" and results[name]["bounds"]["a_ub"] == a and results[name]["bounds"]["m_det_lb"] == 0)

    bad = copy.deepcopy(fixtures["open_a1"]); bad["delta"] = 8
    check("wrong key refuses bounds", memory.query(bad)["bounds"] == {})
    bad = copy.deepcopy(fixtures["open_a1"]); del bad["ambient_variables"]
    check("incomplete key refuses bounds", memory.query(bad)["status"] == "RECORDED")
    bad = copy.deepcopy(fixtures["open_a1"]); bad["point_family"] = "nine_variable_clamp"
    check("independent padding convention required", memory.query(bad)["bounds"] == {})
    bad = copy.deepcopy(fixtures["open_a1"]); bad["geometry"] = "orbit"
    check("orbit not silently closure", memory.query(bad)["bounds"] == {})

    # Exact role-specific source replay, including a square transpose whose
    # determinant would pass a stored-matrix-only verifier.
    certs = sorted((ROOT/"results/b14_10/recovered").glob("*.json"))
    certs = [p for p in certs if not p.name.endswith(".validation.json")]
    check("four native replacements present", len(certs) == 4)
    for path in certs:
        cert = json.loads(path.read_text(encoding="utf-8"))
        check("native polynomial liveness "+path.stem, verify_native(cert)["m_per3_lb"] == 1)
    cert = json.loads(certs[0].read_text(encoding="utf-8"))
    cc = cell(3, 8, cert["cell"]["lambda"])
    replay = memory.query(cc, certificates=[cert])
    check("consumer admits fresh native floor", replay["status"] == "REPLAYED_RANK_FLOOR")
    mutations = {}
    b = copy.deepcopy(cert); b["matrix"]["values"] = list(map(list, zip(*b["matrix"]["values"])))
    mutations["transpose square matrix with determinant unchanged"] = b
    b = copy.deepcopy(cert); b["normalization"] = "ordinary cubic coefficients"
    mutations["swap factorial coefficient convention"] = b
    b = copy.deepcopy(cert); b["point"]["pencil"][0][0] += 1
    b["point_sha256"] = canonical_digest(b["point"])
    mutations["changed point and updated checksum"] = b
    b = copy.deepcopy(cert); b["polynomial_terms_sha256"] = "0"*64
    mutations["altered source polynomial"] = b
    b = copy.deepcopy(cert); b["determinant_Z"] = str(-int(b["determinant_Z"]))
    mutations["changed determinant sign"] = b
    for name, b in mutations.items():
        result = memory.query(cc, certificates=[b])
        check(name, result["decision"] == "UNRESOLVED" and result["bounds"] == {} and bool(result["rejected"]))

    # Mutate source bytes while retaining the versioned review pins. Merely
    # putting a new checksum into the evidence cannot change the trust root.
    with tempfile.TemporaryDirectory(prefix="b15_11_scope_", dir=out) as td:
        root = Path(td)
        for name in memory.pins:
            p = root/name; p.parent.mkdir(parents=True, exist_ok=True)
            p.write_bytes((ROOT/name).read_bytes())
        p = root/"results/b15_11/trusted_inputs.json"; p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(json.dumps(memory.pins), encoding="utf-8")
        idx = json.loads((root/"results/integrate/inherited_exclusions.json").read_text(encoding="utf-8"))
        next(r for r in idx["exclusions"] if r["id"] == "n4_gate_containment")["predicate"]["r_max"] = 16
        (root/"results/integrate/inherited_exclusions.json").write_text(json.dumps(idx), encoding="utf-8")
        check("mutated theorem scope refused", Memory(root).query(fixtures["open_a1"])["bounds"] == {})

    raw = {"rank": 1, "status": "EXACT", "witness": None}
    for model in ("gpt-6-astra", "claude-opus-5"):
        record = normalize_record(raw, model, fixtures["open_a1"], "synthetic_negative_control")
        decision = memory.query(fixtures["open_a1"], [record])
        check(model+" recorded rank cannot exclude", decision["decision"] == "UNRESOLVED" and decision["bounds"]["m_det_lb"] == 0)
    astra = json.loads((ROOT/"results/astra/S1/transported_det_lower_bound_2.json").read_text(encoding="utf-8"))
    claude = json.loads((ROOT/"results/b14_12/s79_schema_rows.jsonl").read_text(encoding="utf-8").splitlines()[0])
    adapters = [normalize_record(astra, "gpt-6-astra", fixtures["LMR"], "results/astra/S1/transported_det_lower_bound_2.json"),
                normalize_record(claude, "claude-opus-5", fixtures["session12"], "results/b14_12/s79_schema_rows.jsonl#1")]
    check("both native model envelopes load", all(memory.query(r["cell"], [r])["recorded"] for r in adapters))
    b = copy.deepcopy(adapters[1]); b["usable_for_bounds"] = True
    check("record cannot self-authorize", memory.query(b["cell"], [b])["bounds"] == {})
    b = copy.deepcopy(adapters[1]); b["raw"]["mult_det"] = 1000
    check("record content digest enforced", memory.query(b["cell"], [b])["bounds"] == {})

    positive = dict(a_lb=4, a_ub=4, i_det_lb=3, m_det_lb=0, i_pad_lb=0, m_pad_lb=2)
    close_intervals(positive)
    check("strict positive implication synthetic", positive["D_lb"] == 1)
    boundary = dict(a_lb=4, a_ub=4, i_det_lb=2, m_det_lb=0, i_pad_lb=0, m_pad_lb=2)
    close_intervals(boundary)
    check("equality not positive", boundary["D_lb"] == 0)
    try:
        close_intervals(dict(a_lb=1, a_ub=1, m_det_lb=2, i_det_lb=0))
    except ValueError:
        check("inconsistent bounds rejected", True)
    else:
        check("inconsistent bounds rejected", False)

    ident = [[int(i == j) for j in range(4)] for i in range(4)]
    args = dict(ring="det", irreducibility_proof="GL_orbit_closure_irreducible",
                multiplier_witness=dict(ring="det", first_variable_matrix=ident),
                source_floor_lb=2, evaluated_multiplier=24)
    check("coordinate transport nonzero native u", coordinate_transport(**args) == 2)
    for name, change in (("no irreducibility", {"irreducibility_proof": None}),
                         ("zero on variety", {"evaluated_multiplier": 0}),
                         ("nonzero metadata without point", {"multiplier_witness": {"ring": "det", "verification": "native_exact_evaluation"}}),
                         ("wrong variety", {"multiplier_witness": {"ring": "pad", "first_variable_matrix": ident}})):
        try:
            coordinate_transport(**(args | change))
        except ValueError:
            check("transport refuses "+name, True)
        else:
            check("transport refuses "+name, False)
    data = dict(status="EXACT", model="gpt-6-astra", checks=checks, count=len(checks),
                fixtures=results, native_replay=replay, synthetic_positive=positive,
                input_sha256_lf={p.relative_to(ROOT).as_posix(): digest(p.read_bytes()) for p in certs +
                    [ROOT/"analysis/b14_10/recover.py", ROOT/"results/astra/S1/transported_det_lower_bound_2.json", ROOT/"results/b14_12/s79_schema_rows.jsonl"]},
                wall_seconds=time.perf_counter()-start)
    (out/"controls.json").write_text(json.dumps(data, indent=2)+"\n", encoding="utf-8")
    (out/"model_adapters.json").write_text(json.dumps(adapters, indent=2)+"\n", encoding="utf-8")
    print(json.dumps(dict(status="PASS", checks=len(checks), wall_seconds=data["wall_seconds"])))


if __name__ == "__main__":
    main()
