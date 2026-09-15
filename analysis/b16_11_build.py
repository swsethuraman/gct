"""Snapshot only inspected B16-11 inputs and audit hashes; no research replay."""
import hashlib
import json
import os
from pathlib import Path
import sys
import time

ROOT=Path(__file__).resolve().parents[4]
OWN=Path(__file__).resolve().parents[1]
OUT=OWN/"results/b16_11"
PACKAGE=OWN/"delivery/b16_11"
PREFIX="Batch15_Launch/native_20260913/"
REVIEW=PREFIX+"reviews_filesystem/"
rows={}
MAX_TOTAL=64*1024**2
total=0


def need(ok,msg):
    if not ok: raise ValueError(msg)


def sha(data): return hashlib.sha256(data).hexdigest()


def relative(path): return path.resolve().relative_to(ROOT).as_posix()


def take(path, expected=None, role="inherited_evidence"):
    global total
    p=ROOT/path
    need(p.is_file(),"missing input: "+path)
    need(p.stat().st_size<=16*1024**2,"unpriced input: "+path)
    data=p.read_bytes()
    actual=sha(data)
    if expected: need(actual.lower()==expected.lower(),"input hash mismatch: "+path)
    if path not in rows:
        total+=len(data)
        need(total<=MAX_TOTAL,"snapshot budget")
        target=PACKAGE/"evidence"/path
        target.parent.mkdir(parents=True,exist_ok=True)
        target.write_bytes(data)
        rows[path]=dict(source=path,copy="evidence/"+path,bytes=len(data),sha256=actual,role=role)
    else:
        need(rows[path]["sha256"]==actual,"input changed mid-audit: "+path)
    return data


def obj(path, **kw): return json.loads(take(path,**kw).decode("utf-8-sig"))


def write(name,value):
    p=OUT/name
    p.write_text(json.dumps(value,indent=2)+"\n",encoding="utf-8")
    return relative(p)


def blob(data):
    return hashlib.sha1(b"blob "+str(len(data)).encode()+b"\0"+data).hexdigest()


def main():
    need("CI73_DEADLINE" in os.environ,"resource wrapper required")
    OUT.mkdir(parents=True,exist_ok=True)
    PACKAGE.mkdir(parents=True,exist_ok=True)
    start=time.perf_counter()
    launch=obj("Batch16/launch/INPUT_MANIFEST.json",role="frozen_launch")
    for p in ("Batch16/BOARD.md","Batch16/launch/B16-11.md"):
        take(p,role="dispatch_instruction")
    for e in launch["inputs"]:
        take(relative(Path(e["path"])),e["sha256"],role="frozen_launch_input")
    git=obj(relative(OUT/"git_audit.json"),role="fresh_read_only_git_receipt")
    bindings=[]
    for e in git["source_bindings"]:
        p="work/batch15_workers/B15-"+e["slot"]+"/"+e["path"]
        data=take(p,role="original_worker_source")
        tokens=e["ls_tree"].split()
        need(len(tokens)>=4 and tokens[1]=="blob","missing frozen source blob")
        raw,lf=blob(data),blob(data.replace(b"\r\n",b"\n"))
        need(tokens[2] in (raw,lf),"original source does not bind to frozen commit: "+p)
        bindings.append(dict(source=p,frozen_head=e["frozen_head"],git_blob=tokens[2],
                             raw_git_blob=raw,lf_git_blob=lf,
                             binding="raw" if raw==tokens[2] else "CRLF_to_LF_only"))
    replay=REVIEW+"B15-01_full_replay/"
    original_manifest=obj(replay+"INPUT_MANIFEST.json")
    full_checks=[]
    for e in original_manifest:
        p=replay+e["path"].replace("\\","/")
        if "__pycache__/" in p:
            # Incidental bytecode is checked in place, never delivered or run.
            data=(ROOT/p).read_bytes()
            actual=sha(data)
            need(actual==e["sha256"].lower(),"incidental cache drift: "+p)
            full_checks.append(dict(source=p,bytes=len(data),sha256=actual,expected=e["sha256"].lower(),
                                    pass_hash=True,packaged=False,role="incidental_cache_hash_only"))
        else:
            take(p,e["sha256"],role="inherited_full_replay_input_not_executed")
            full_checks.append(dict(source=p,sha256=rows[p]["sha256"],expected=e["sha256"].lower(),pass_hash=True,packaged=True))
    take(replay+"results/b15_01/integrator_report.md")
    for p in (ROOT/replay/"results/b15_01").glob("*"):
        if p.is_file() and p.suffix in (".json",".gz",".md"):
            take(relative(p),role="inherited_replay_output")
    extra=["Dream_Upper288/cubic_bound.json","Dream_Upper288/cubic_bound.py",
           "Dream_Upper288/verify_cubic_and_lift.py","Dream_Upper288/DELIVERY_MANIFEST.json",
           "Hessian11_1631/integrator_review.json","Hessian11_1631/MANIFEST.json",
           "Hessian11_1631/input_receipt.json","Hessian11_1631/resource_summary.json",
           "Hessian11_1631/SHORTLIST.json","Hessian11_1631/verify_small.py",
           "B15-08_0256ed256196/integrator_review.json",
           "B15-11_c40546038506/integrator_review.json"]
    for p in extra: take(REVIEW+p)
    for p in ("SUMMARY.json","COMPLETED_DELIVERIES.json","DIFFERENCE_CLASSIFICATION.json"):
        take(PREFIX+"git_closeout/"+p)
    intake=obj(PREFIX+"INTAKE.json")
    closeout=obj(PREFIX+"git_closeout/SUMMARY.json")
    completed=obj(PREFIX+"git_closeout/COMPLETED_DELIVERIES.json")
    effective={e["slot"]:e for e in closeout}
    effective.update({e["slot"]:e for e in completed})
    joins=[]
    for w in launch["worktrees"]:
        p=effective[w["slot"]]["packaging"]
        need(p["status"]=="PASS" and p["head"]==w["head"] and p["head_tree"]==w["tree"],
             "closeout binding mismatch slot "+w["slot"])
        joins.append(dict(slot=w["slot"],head=p["head"],tree=p["head_tree"],status=p["status"],
                          delivery_source="COMPLETED_DELIVERIES" if w["slot"] in ("08","12") else "SUMMARY"))
    precedence=[
        dict(id="historical_statuses",severity="resolved_history",detail="Per-entry PENDING_GIT_BINDING labels are historical. Later git_closeout validates committed deliveries, while filesystem followups retain separate uncommitted status."),
        dict(id="slot06_head",severity="resolved_history",detail="Intake entry head4067e2eb is the prelease delivery; production_followup head41e03e17 equals the frozen launch head."),
        dict(id="slot01_entry",severity="resolved_structure",detail="No slot01 row in entries; top-level slot01_full_review supplies acceptance, superseding slot01_partial_review."),
        dict(id="slots08_12_delivery",severity="resolved_history",detail="Use _completed bundles selected by exact head, not stale _final folders."),
        dict(id="hessian_pending_claims",severity="resolved_history",detail="Hessian report predates later slot06 production and slot01 full review. Preserve author-relative fresh labels; they are inherited in B16-11."),
        dict(id="global_raw_hessian",severity="open_proof_boundary",detail="Dream degree23 padding checker inherits saved raw Hessian coefficients. It cannot be called a fresh Hessian evaluation; B16-03 must rebuild them."),
        dict(id="finite_unknowns",severity="open_input",detail="Frozen launch lacks exact finite quartic ambient counts at23/25/26/27, a complete eleven-space finite filtration, and sufficient actual padding floors. No positive cell is accepted."),
        dict(id="finite26_ceiling",severity="derived_extension",detail="218 at degree26 follows the same reviewed cubic chart injection and checked Pieri channels. The Dream summary explicitly listed only23/25/27; this is a B16 conditional deduction, not a saved exact count."),
        dict(id="legacy_resource_scope",severity="scope_note",detail="B15-01 accepted replay used5400s/1536MiB and measured2296.626s. B16 small-control caps are not applied retroactively, nor does that receipt grant a B16 heavy lease."),
        dict(id="wrapper_labels",severity="scope_note",detail="Inspected b15_bound.py writes legacy batch15/B15-11 metadata; command/name and ownership identify the new B16 run. workers=1 is declared, not an ActiveProcessLimit; this receiver launches no child."),
    ]
    audit=write("audit.json",dict(schema="b16-11-audit/1",frozen_input_checks=6,
        worktrees_checked=12,source_bindings=bindings,full_replay_input_hash_checks=full_checks,
        closeout_joins=joins,findings=precedence,missing_required_launch_files=[],
        irreconcilable_claims=[],fresh_mathematical_replays=0,heavy_lease_used=False))
    take(audit,role="fresh_provenance_audit")
    runtime=write("runtime.json",dict(python=sys.version,executable=sys.executable,
        executable_sha256=sha(Path(sys.executable).read_bytes()),platform=sys.platform,
        blas_env={k:os.environ.get(k) for k in ("OPENBLAS_NUM_THREADS","OMP_NUM_THREADS","MKL_NUM_THREADS","NUMEXPR_NUM_THREADS","VECLIB_MAXIMUM_THREADS")},
        runtime_inputs_scope="Interpreter executable hash recorded; standard library is identified by Python version, not individually snapshotted."))
    take(runtime,role="fresh_runtime_identity")
    for path in ("analysis/b15_bound.py","results/logs/b16_11_runtime_resources.json",
                 "analysis/b16_11_build.py","analysis/b16_11_receiver.py","analysis/b16_11_git_audit.ps1",
                 "docs/b16_11_receiver_spec.md"):
        take(relative(OWN/path),role="receiver_code_or_control")
    manifest=dict(schema="b16-11-receiver/1",created_utc=time.strftime("%Y-%m-%dT%H:%M:%SZ",time.gmtime()),
        frozen_launch_sha256=rows["Batch16/launch/INPUT_MANIFEST.json"]["sha256"],
        inputs=list(rows.values()), incidental_hash_only_inputs=[e for e in full_checks if not e["packaged"]],
        limitations=["Hash/source-head checks do not replay mathematical proofs.",
            "No unified merged base is claimed. Working-tree followups are separately hashed.",
            "Legacy incidental bytecode is hash-checked in place and omitted from delivery.",
            "All character counts, global proof acceptance, and geometric minors remain inherited.",
            "The positive admission registry is empty; external observations cannot authorize their own bounds.",
            "B16 mathematical outputs of other slots are outside this frozen-launch audit."])
    (PACKAGE/"INPUT_HASHES.json").write_text(json.dumps(manifest,indent=2)+"\n",encoding="utf-8")
    for name in ("b16_11_receiver.py","b15_bound.py"):
        (PACKAGE/name).write_bytes((OWN/"analysis"/name).read_bytes())
    # Core replays find their payload at the explicit package root; no absolute
    # author path is used by the portable receiver.
    print(json.dumps(dict(status="SNAPSHOT_AND_AUDIT_PASS",files=len(rows),bytes=total,
         full_replay_hashes=len(full_checks),source_bindings=len(bindings),seconds=time.perf_counter()-start)))


if __name__=="__main__": main()
