"""Bounded, read-only historical audit plus slot-local deterministic catalogs."""
import collections
import hashlib
import json
from pathlib import Path
import re
import time

from b15_11_memory import ROOT, Memory, cell, digest, key, validate_cell

OUT = ROOT / "results/b15_11"
CONSUMED = {}


def read(path):
    raw = (ROOT/path).read_bytes()
    CONSUMED[path] = dict(sha256_lf=digest(raw), sha256_bytes=hashlib.sha256(raw).hexdigest(), bytes=len(raw))
    if path.endswith(".json"):
        return json.loads(raw)
    if path.endswith(".jsonl"):
        return [json.loads(s) for s in raw.decode("utf-8").splitlines() if s.strip()]
    return raw.decode("utf-8")


def write(name, data):
    p = OUT/name
    p.parent.mkdir(parents=True, exist_ok=True)
    raw = (json.dumps(data, indent=2, ensure_ascii=False)+"\n").encode("utf-8")
    if len(raw) >= 5_000_000:
        raise ValueError("split output before writing " + name)
    p.write_bytes(raw)


def jsonl(name, rows):
    p = OUT/name
    raw = ("\n".join(json.dumps(r, separators=(",", ":"), ensure_ascii=False) for r in rows)+"\n").encode("utf-8")
    if len(raw) >= 5_000_000:
        raise ValueError("split output before writing " + name)
    p.write_bytes(raw)


def explicit_keys(obj):
    """Only same-object n, degree, partition. No filename or parent inheritance."""
    found = []
    stack = [("", obj)]
    while stack:
        pointer, item = stack.pop()
        if isinstance(item, dict):
            for label in ("lambda", "lambda_", "lam", "mu"):
                lam = item.get(label)
                if type(item.get("n")) is int and type(item.get("delta")) is int and isinstance(lam, list):
                    c = dict(n=item["n"], delta=item["delta"], ell=len(lam), **{"lambda": lam})
                    try:
                        validate_cell(c)
                    except ValueError:
                        continue
                    found.append(dict(cell=c, pointer=pointer+"/"+label, method="explicit_same_object"))
            stack.extend((pointer+"/"+str(k).replace("~", "~0").replace("/", "~1"), v)
                         for k, v in item.items() if isinstance(v, (dict, list)))
        elif isinstance(item, list):
            stack.extend((pointer+"/"+str(i), x) for i, x in enumerate(item) if isinstance(x, (dict, list)))
    return sorted(found, key=lambda r: r["pointer"])


def key_audit():
    paths = read("results/b14_10/remaining_cell_keys.json")["paths"]
    source = read("results/s74/source.json")
    src = source["cell"]
    c24 = dict(n=src["n"], delta=src["delta"], ell=len(src["lam"]), **{"lambda": src["lam"]})
    validate_cell(c24)
    native_groups = {}
    for i, entry in enumerate(source["entries"]):
        native, literal = entry["native"], entry["literal"]
        nc = dict(n=native["n"], delta=native["delta"], ell=len(native["lam"]), **{"lambda": native["lam"]})
        lc = dict(n=literal["n"], delta=literal["delta"], ell=len(literal["lam"]), **{"lambda": literal["lam"]})
        validate_cell(nc); validate_cell(lc)
        assert lc == c24 and entry["rung"] == nc["delta"]
        assert entry["exponent"] == c24["delta"]-nc["delta"]
        assert entry["factorial_scalar"] == 24**entry["exponent"]
        group = native_groups.setdefault(nc["delta"], dict(cell=nc, entry_indices=[], source_pointer="results/s74/source.json#/entries"))
        group["entry_indices"].append(i)
    code = read("analysis/wk12_int_s74_verify.py")
    assert "columns_" in code and "decision_" in code and "literal" in code
    rows = []
    for path in paths:
        d = read(path)
        keys = explicit_keys(d)
        row = dict(path=path, status="RECORDED", key_disposition="UNRESOLVED",
                   keys=keys, bounds_admitted=False, variety_context="not inferred from a representation key")
        # These exact roles are explicitly linked to source.json by the banked
        # verifier. Native rows span degrees 12..24; literal rows are degree24.
        if re.fullmatch(r"results/s74/(columns_(det|pad|red|per4)|decision)_214748(3647|3629)\.json", path):
            if "columns_" in path:
                assert len(d["rows_native"]) == source["size"]
                assert isinstance(d["rows_native"], dict)
                assert set(d["rows_native"]) == {str(e["key"]) for e in source["entries"]}
                assert d["family"] == Path(path).stem.split("_")[1]
                assert d["prime"] == int(Path(path).stem.split("_")[-1])
                row["native_row_groups"] = list(native_groups.values())
                row["transport_normalization"] = dict(u="24*c_(4,0,...)", u_index=source["u_index"],
                    literal_scalar="24^(24-native_degree)", source_native_and_literal_cells_checked=274)
            else:
                assert d["source_size"] == source["size"]
            keys.append(dict(cell=c24, pointer="/", method="explicit_source_binding",
                             reference="results/s74/source.json#/cell",
                             verifier="analysis/wk12_int_s74_verify.py",
                             caveat="rows_native use each entry's native degree; only literal transported rows are degree24"))
            row["key_disposition"] = "RESOLVED_SOURCE_BINDING"
            row["priority"] = 0
        elif keys:
            row["key_disposition"] = "RESOLVED_EXPLICIT_KEY_LOCATIONS"
            row["priority"] = 1
            row["caveat"] = "Locations identified; no assertion that unrelated siblings share these keys."
        else:
            row["priority"] = 2
            row["next_sufficient_witness"] = "Source-specific role and cell/context binding; do not infer from filename or neighboring records."
        rows.append(row)
    assert len(rows) == 223 and len({r["path"] for r in rows}) == 223
    rows.sort(key=lambda r: (r["priority"], r["path"]))
    jsonl("key_reconciliation.jsonl", rows)
    return dict(total=len(rows), by_disposition=dict(collections.Counter(r["key_disposition"] for r in rows)),
                unresolved_paths=[r["path"] for r in rows if r["key_disposition"] == "UNRESOLVED"])


def hash_audit():
    manifest = read("results/s79_cert_manifest.json")
    expected = read("results/b14_10/digest_discrepancies.json")
    expected_paths = {r["path"] for r in expected["files"]}
    mismatch, unshipped_present = [], []
    count = collections.Counter()
    for row in manifest["files"]:
        p = ROOT/row["path"]
        count["listed"] += 1
        if not p.exists():
            count["missing"] += 1
            continue
        count["present"] += 1
        md5, sha = hashlib.md5(), hashlib.sha256()
        with p.open("rb") as f:
            while chunk := f.read(262144):
                md5.update(chunk); sha.update(chunk)
        if not row["shipped"]:
            unshipped_present.append(row["path"])
        if md5.hexdigest() != row["md5"]:
            mismatch.append(dict(path=row["path"], status="RECORDED", shipped=row["shipped"],
                historical_md5=row["md5"], current_md5=md5.hexdigest(), current_sha256=sha.hexdigest(),
                disposition="ACCOUNTED_PRESENT_UNSHIPPED", payload_equivalence="UNKNOWN",
                mathematical_use="No bound authorized by compressed digest reconciliation.",
                next_sufficient_witness="Native source/point replay or original uncompressed digest for payload equivalence."))
        else:
            count["md5_match"] += 1
    assert {r["path"] for r in mismatch} == expected_paths == set(unshipped_present)
    assert len(mismatch) == 29
    write("digest_reconciliation.json", dict(counts=dict(count), discrepancies=mismatch,
          attribution="B14-10 integrator review; set equality freshly checked", historical_payload_equivalence="UNKNOWN"))
    return dict(accounted=29, historical_payload_equivalence_unresolved=29, counts=dict(count))


def missing_map(memory):
    candidates = read("results/b14_10/recovery_queue.json")["candidates"]
    replacements = {r["original_path"]: r for r in read("results/b14_10/replacement_map.json")}
    registry = {r["path"]: r for r in read("results/b14_10/certificate_register.jsonl")}
    rows = []
    for old in candidates:
        c0 = old["cell"]
        validate_cell(c0)
        c = cell(c0["n"], c0["delta"], c0["lambda"])
        decision = memory.query(c)
        inherited = [r["id"] for r in decision["inherited_premises"]]
        role = registry[old["path"]]["kind_from_path"]
        role_dependencies = {
            "fullrank": ("m_per3_lb", "cubic_per3_rank_floor", "degree8_global or length6_record where scoped; otherwise the cubic frontier"),
            "fullrank_det": ("m_det_lb", "quartic_determinant_rank_floor", "r_det>=min(a,h_pad,a-i_pad_lb)"),
            "fullrank_pad": ("m_pad_lb", "independent_padded_rank_floor", "positive D also requires a global determinant upper bound"),
            "fullrank_per4": ("m_per4_lb", "unpadded_per4_control", "no direct bound on m_pad; per4 and independent z*per3 are distinct"),
            "hybrid": ("sampled_coordinate_rank_lb", "hybrid_source_and_geometric_evaluation", "rebuild integral/rational source and separate det/pad evaluations; sampled nullity only bounds ideals above")}
        bound_role, exact_dependency, sufficient = role_dependencies[role]
        replacement = replacements.get(old["path"])
        current_dep = ("cubic_degree8_closure_and_quartic_transfer" if c["n"] == 3 and c["delta"] <= 8 else
                       "cubic_length6_degree9_closure" if c["n"] == 3 and c["ell"] == 6 and c["delta"] <= 9 else
                       "cubic_degree9_frontier" if c["n"] == 3 else "quartic_coordinate_rank_frontier")
        resolved = decision["decision"] in ("IDEAL_ZERO", "EXCLUDED_D_POSITIVE")
        row = dict(path=old["path"], cell=c, status="RECORDED", original_present=(ROOT/old["path"]).exists(),
                   certificate_role=role, source_record=old.get("source_record"),
                   current_dependency=current_dep, inherited_premises=inherited,
                   mathematical_dependency=exact_dependency, bound_role_if_validly_replayed=bound_role,
                   sufficient_use=sufficient,
                   current_decision=decision["decision"], original_absence_changes_theorem=False if resolved else None,
                   dependency_priority=0 if replacement else 1 if not resolved else 2,
                   replacement_certificate=replacement["replacement_certificate"] if replacement else None,
                   replacement_possibility=("Replay existing integral catalecticant source and pencil." if replacement else
                       "Scoped inherited theorem already decides this cell; compact native source/point minor improves portability." if resolved else
                       "Reconstruct integral or rational-lifted HWVs and explicit family points; evaluate afresh and retain an exact nonzero minor. Hybrid sampled kernels remain rank floors only."),
                   next_sufficient_witness=decision["next_sufficient_witness"], historical_reason=old["historical_reason"])
        assert not row["original_present"]
        rows.append(row)
    assert len(rows) == 1005 and len({r["path"] for r in rows}) == 1005
    rows.sort(key=lambda r: (r["dependency_priority"], r["path"]))
    jsonl("missing_certificate_dependencies.jsonl", rows)
    return dict(total=1005, originals_restored=0, compact_replacement_paths=len(replacements),
                by_dependency=dict(collections.Counter(r["current_dependency"] for r in rows)),
                by_mathematical_role=dict(collections.Counter(r["mathematical_dependency"] for r in rows)),
                by_current_decision=dict(collections.Counter(r["current_decision"] for r in rows)))


def frontier(memory):
    queue = read("results/b14_11/cost_queue.json")
    preflight = read("results/b15_prep/candidate_preflight.json")
    sizing = read("results/b15_prep/small_panel_sizing.json")
    panel = {key(r["target"]): r for r in sizing["cells"]}
    rows = []
    for r in queue:
        c = cell(r["n"], r["delta"], r["lam"])
        d = memory.query(c)
        if key(c) in panel:
            s = panel[key(c)]["sizing"]
            d["sizing"] = {k: s[k] for k in ("N_S", "n_chi", "stabilizer_order", "signed_trace_sum")}
            assert s["signed_trace_sum"] == s["n_chi"]*s["stabilizer_order"]
        rows.append(d)
    excluded = [r for r in rows if r["decision"] == "EXCLUDED_D_POSITIVE"]
    deferred = [r for r in rows if r["decision"] == "UNRESOLVED" and r["recorded"]]
    assert len(queue)-len(excluded)-len(deferred) == preflight["remaining_queue"] == 1710
    for i in range(0, len(rows), 500):
        jsonl(f"frontier.part{i//500:02d}.jsonl", rows[i:i+500])
    transport = read("results/b15_prep/transport_overlay.json")
    transports = [memory.query(cell(4, r["degree"], r["lam"])) for r in transport["targets"]]
    jsonl("transport_frontier.jsonl", transports)
    q1 = read("results/b15_prep/Q1_coverage.json")
    jsonl("Q1_record_frontier.jsonl", [memory.query(cell(4, r["delta"], r["lam"])) for r in q1["cells"]])
    return dict(queue_input=len(queue), scoped_exclusions=len(excluded), operational_queue=1710,
                witness_strict_unresolved=len(queue)-len(excluded), recorded_deferrals=len(deferred),
                recorded_deferred_cells=[r["cell"] for r in deferred],
                excluded_cells=[r["cell"] for r in excluded], sizing_cells=len(sizing["cells"]),
                transport_cells=len(transports), transport_decisions=dict(collections.Counter(r["decision"] for r in transports)),
                Q1_record_labels=len(q1["cells"]))


def main():
    start = time.perf_counter()
    OUT.mkdir(parents=True, exist_ok=True)
    for p in sorted((ROOT/"docs").glob("b14_*_review.md")):
        read(p.relative_to(ROOT).as_posix())
    for p in sorted((ROOT/"results").glob("b14_*/input_manifest.json")):
        read(p.relative_to(ROOT).as_posix())
    for p in ("results/b14_10/reconciliation.json", "results/b14_11/inventory_summary.json",
              "results/b15_prep/TOOL_INDEX.json", "results/b15_prep/imported_input_manifest.json",
              "results/b15_prep/review_to_integrated_comparison.json"):
        read(p)
    tools = read("results/b15_prep/TOOL_INDEX.json")["tools"]
    tool_receipts = []
    for tool in tools:
        for source in tool["sources"]:
            path = source["path"]
            read(path)
            ok = CONSUMED[path]["sha256_lf"] == source["sha256"]
            tool_receipts.append(dict(tool=tool["name"], path=path, hash_match=ok,
                evidence_status="RECORDED", boundary=tool["boundary"], native_replayed_here=False))
            assert ok, "tool source pin mismatch: "+path
    write("tool_source_receipts.json", tool_receipts)
    memory = Memory()
    result = dict(status="EXACT", model="gpt-6-astra", heavy_lease_used=False,
                  tool_source_pins_verified=len(tool_receipts),
                  integrity=hash_audit(), key_reconciliation=key_audit(),
                  missing_certificates=missing_map(memory), frontier=frontier(memory))
    result["wall_seconds"] = time.perf_counter()-start
    write("audit_summary.json", result)
    write("consumed_inputs.json", CONSUMED)
    print(json.dumps({k:v for k,v in result.items() if k != "key_reconciliation"}, indent=2))
    print(json.dumps(result["key_reconciliation"]["by_disposition"]))


if __name__ == "__main__":
    main()
