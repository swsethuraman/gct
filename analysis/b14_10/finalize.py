"""Small deterministic roll-up of completed B14-10 artifacts."""
import collections, json, pathlib, sys
sys.path.insert(0,str(pathlib.Path(__file__).resolve().parent))
from validate import load_register
from inventory import OUT, ROOT, write

def main():
    files=load_register('file_register.jsonl');certs=load_register('certificate_register.jsonl')
    a=json.loads((OUT/'reconciliation.json').read_text())
    b=json.loads((ROOT/'results/integrate/batch13_reconciliation.json').read_text())
    baseline={k.replace(' r=',' ell='):v for k,v in b['frontiers'].items()}
    assert a['cells']==b['cells']==1846 and a['frontiers']==baseline
    unknown=[r for r in files if r['historical_unparsed'] and r['cell_key_status']=='unknown_no_complete_cell_schema']
    write('remaining_cell_keys.json',dict(status='OPEN',count=len(unknown),
        meaning='Classification exists; a complete representation-cell identity is not extracted. Some may be non-cell geometry or global metadata; no guessed key.',
        estimated_work='223 bounded schema/reference reviews; analyst time unmeasured. No large arithmetic prerequisite.',
        paths=[r['path'] for r in unknown]))
    write('new_frozen_inputs.json',[r['path'] for r in files if not r['historical_unparsed'] and not r['previously_parsed']])
    mismatch=[r for r in certs if r.get('md5_match') is False]
    write('digest_discrepancies.json',dict(status='OPEN',count=len(mismatch),
        meaning='Historical compressed MD5 differs from current frozen bytes. Uncompressed historical digests absent; equivalence unknown.',
        files=[{k:r.get(k) for k in ('path','expected_bytes','actual_bytes','expected_md5','actual_md5','sha256','payload_sha256','frozen_blob')} for r in mismatch]))
    res={p.stem:json.loads(p.read_text()) for p in (ROOT/'results/logs').glob('b14_10_*.resource.json')}
    summ=dict(board_numbering='batch14',actual_model='gpt-6-astra',
        outcome='SUBSTANTIVE_FALLBACK: complete file/certificate accounting; four exact replacements and indexed proof rules; partial semantic keys and historical replay remain open',
        file_classifications=dict(collections.Counter(r['classification'] for r in files)),
        whole_file_supersessions=0,unresolved_historical_cell_keys=len(unknown),
        certificate_entries=len(certs),original_files_missing=sum(not r['present'] for r in certs),
        new_exact_replacement_files=4,original_manifest_entries_with_replacement=sum(r['recovery_status']=='EXACT_REPLACEMENT_CERTIFIED' for r in certs),
        present_digest_mismatches=len(mismatch),payload_parse_status=dict(collections.Counter(r.get('parse_status','missing') for r in certs)),
        producer_wrong_direction_field_notes=sum(bool(r.get('semantic_cautions')) for r in certs),
        hybrid_verifier_scope='hybrid_kernel is recognized but native verifier records consistency only; it does not rederive ranks',
        missing_s79_rows_without_matching_producer_record=sum(not r['present'] and r['producer_record'] is None and r['manifest']=='results/s79_cert_manifest.json' for r in certs),
        frontier_comparison=dict(status='PASS',normalization='legacy r label -> ell; same integer cell keys',cells=1846,
           all_frontier_sets_identical=True,open_degree9_length7=47,open_degree9_length8=52,open_degree10_length6=58),
        resource_log_statuses={k:v['status'] for k,v in res.items()},
        resource_limit_events=[dict(log=k,**v) for k,v in res.items() if v['status']!='completed'],
        current_run_resource_seconds=sum(v['elapsed_seconds'] for v in res.values()),
        note='Summed instrument wall seconds exclude agent/read/packaging time and any scheduler pause; not CPU-hours.')
    write('audit_summary.json',summ);print(json.dumps(summ,indent=2))

if __name__=='__main__':main()
