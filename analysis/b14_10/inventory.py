"""Frozen-file accounting. No producer rank claim is promoted by this inventory."""
import argparse, ast, collections, gc, gzip, hashlib, json, pathlib, re, subprocess

BASE = '9898e56941a7665f231873481dae956f08509995'
TREE = 'cb688cd3fe454d638f3202e759e2eaa0c629739f'
ROOT = pathlib.Path(__file__).resolve().parents[2]
OLD = 'results/integrate/astra_reconciliation/review_only/results/integration/'
OUT = ROOT / 'results/b14_10'
MANIFESTS = ['results/s79_cert_manifest.json', 'results/b13_09/cert_manifest.json']
BASE_OVERRIDES = {}

def git(*args):
    return subprocess.check_output(['git', *args], cwd=ROOT).decode('utf-8')

def read(path):
    if path in BASE_OVERRIDES:
        text=BASE_OVERRIDES[path].decode('utf-8-sig')
        return [json.loads(s) for s in text.splitlines() if s.strip()] if path.endswith('.jsonl') else json.loads(text)
    p = ROOT / path
    if path.endswith('.gz'):
        with gzip.open(p, 'rt', encoding='utf-8') as f: return json.load(f)
    if path.endswith('.jsonl'):
        return [json.loads(line) for line in p.read_text(encoding='utf-8-sig').splitlines() if line.strip()]
    return json.loads(p.read_text(encoding='utf-8-sig'))

def write(name, value):
    OUT.mkdir(exist_ok=True)
    (OUT/name).write_text(json.dumps(value, indent=2, ensure_ascii=False)+'\n', encoding='utf-8')

def jsonl(name, rows):
    chunks=[]; current=bytearray()
    for row in rows:
        line=(json.dumps(row, ensure_ascii=False, separators=(',', ':'))+'\n').encode('utf-8')
        if len(line)>4_500_000: raise ValueError('one JSONL record exceeds part ceiling')
        if current and len(current)+len(line)>4_500_000: chunks.append(bytes(current));current=bytearray()
        current.extend(line)
    if current: chunks.append(bytes(current))
    if len(chunks)==1: (OUT/name).write_bytes(chunks[0])
    else:
        parts=[]
        for i,data in enumerate(chunks):
            part=name.replace('.jsonl',f'.part{i:02d}.jsonl'); (OUT/part).write_bytes(data)
            parts.append(dict(path=part,bytes=len(data),md5=hashlib.md5(data).hexdigest(),sha256=sha(data)))
        whole=b''.join(chunks)
        write(name+'.parts.json',dict(original_name=name,bytes=len(whole),md5=hashlib.md5(whole).hexdigest(),
              sha256=sha(whole),parts=parts,reconstruct='concatenate parts in numbered order as binary bytes'))
        if (OUT/name).exists(): (OUT/name).unlink()  # only this script's previous generated file

def sha(data): return hashlib.sha256(data).hexdigest()

def require_unique_paths(paths):
    if not paths or len(paths)!=len(set(paths)): raise ValueError('empty or duplicate path inventory')

def frozen():
    assert git('log','-1','--format=%H','batch14-base').strip() == BASE
    assert git('log','-1','--format=%T','batch14-base').strip() == TREE
    records = {}
    for line in git('ls-tree','-r','-l',BASE).splitlines():
        meta, path = line.split('\t',1); mode, kind, blob, size = meta.split()
        if kind == 'blob': records[path] = {'git_blob': blob, 'git_bytes': int(size)}
    for path in git('diff','--name-only',BASE,'--').splitlines():
        if path in records:
            BASE_OVERRIDES[path]=subprocess.check_output(['git','show',BASE+':'+path],cwd=ROOT)
    return records

def capture(blobs, historical):
    snapshot=OUT/'input_manifest.json'
    if snapshot.exists():
        previous=json.loads(snapshot.read_text())
        assert previous['base_commit']==BASE and previous['base_tree']==TREE
        return {r['path']:r for r in previous['files']}
    # Hash all frozen machine-readable results and all source code/docs used by replay.
    paths = {p for p in blobs if p.startswith('results/') and p.endswith(('.json','.jsonl','.json.gz'))}
    paths |= {p for p in blobs if p.startswith(('tools/verify/', OLD))}
    paths |= set(historical) | set(MANIFESTS)
    paths |= {p for p in blobs if p.startswith('analysis/wk12_s79') or p.startswith('analysis/b13_09')}
    paths |= {'docs/batch14_board.md','docs/PROVED.md','docs/brief_wording.md',
              'docs/batch14_reconciliation.md','docs/b14_claude_scratch_code.md','docs/dispatch/B14-10_packet.md',
              'docs/s57_report.md','docs/b13_05_report.md','analysis/wk13_b13_05_topcells.py',
              'tools/integrate/scan_unstaged.py','tools/integrate/reconcile_cells.py','tools/delivery/check_delivery.py'}
    rows = []
    for p in sorted(paths):
        row = dict(path=p, **blobs.get(p, {}), present=(ROOT/p).is_file())
        if row['present']:
            data=BASE_OVERRIDES.get(p,(ROOT/p).read_bytes()); row.update(bytes=len(data), sha256=sha(data),
                bytes_origin='frozen Git blob' if p in BASE_OVERRIDES else 'working bytes at first input capture')
        rows.append(row)
    write('input_manifest.json', dict(board_numbering='batch14', actual_model='gpt-6-astra',
         base_commit=BASE, base_tree=TREE, files=rows,
         note='Working byte SHA256 and frozen blob differ by line endings; all measured inputs frozen before inventory.'))
    return {r['path']:r for r in rows}

def cell(n, delta, lam):
    if type(n) is not int or n<1 or type(delta) is not int or delta<1:
        raise ValueError('unknown or invalid n/delta')
    if not isinstance(lam,(list,tuple)) or not lam or any(type(x) is not int for x in lam):
        raise ValueError('partition not an integer list')
    lam=list(lam)
    while lam and lam[-1]==0: lam.pop()
    if not lam or any(x<=0 for x in lam) or lam!=sorted(lam,reverse=True) or sum(lam)!=n*delta:
        raise ValueError('invalid partition or degree mismatch')
    return dict(n=n, ell=len(lam), delta=delta, **{'lambda':lam})

def keys_in(obj, path=''):
    """Carry explicit n/delta context only; infer n from degree identity, never from rank names."""
    found={}; issues=[]; families={}
    def walk(x, ptr='', inherited=None):
        ctx=dict(inherited or {})
        if isinstance(x,dict):
            for k in ('n','delta'):
                if type(x.get(k)) is int: ctx[k]=x[k]
            if 'delta' not in x:
                for alias in ('d','degree'):
                    if type(x.get(alias)) is int: ctx['delta']=x[alias]; break
            # 'mu' is cubic weight; a simultaneous 'lam' often indexes its quadratic diagram.
            names=('mu','lambda','lambda_','lam','weight','partition')
            if path.startswith('results/s76_c24/shape_'): names=names+('nu',)
            k=next((k for k in names if isinstance(x.get(k),list)
                    and x[k] and all(type(v) is int for v in x[k])), None)
            if k:
                lam=x[k]; n=ctx.get('n'); d=ctx.get('delta'); method='explicit'
                if n is None and d and sum(lam)%d==0 and sum(lam)//d>0:
                    n=sum(lam)//d; method='n derived from sum(lambda)/delta'
                if d is None and n and sum(lam)%n==0:
                    d=sum(lam)//n; method='delta derived from sum(lambda)/n'
                try:
                    c=cell(n,d,lam); key=json.dumps(c,sort_keys=True)
                    found.setdefault(key,dict(key=c, pointer=ptr+'/'+k, key_method=method,
                       variety_context=x.get('variety', x.get('context','unknown'))))
                except ValueError as e:
                    issues.append(dict(pointer=ptr+'/'+k,reason=str(e)))
            for tail_key in ('rho','tail'):
                if isinstance(x.get(tail_key),list) and x[tail_key] and all(type(v) is int and v>=0 for v in x[tail_key]):
                    tail=list(x[tail_key])
                    while tail and tail[-1]==0: tail.pop()
                    if tail and tail==sorted(tail,reverse=True):
                        fam=dict(n=ctx.get('n'),tail=tail,coefficient_degree='not_fixed',pointer=ptr+'/'+tail_key,
                                 context='stable/ladder family; not a single cell')
                        families.setdefault(json.dumps([ctx.get('n'),tail]),fam)
            for k,v in x.items():
                if isinstance(v,(dict,list)):
                    if k=='degrees' and isinstance(v,dict):
                        for degree,contents in v.items():
                            if str(degree).isdigit(): walk(contents,ptr+'/degrees/'+str(degree),dict(ctx,delta=int(degree)))
                        continue
                    # Skip coefficient tensors, points and term arrays; they contain no cell objects.
                    if k not in ('terms','matrix','basis','kernel_chi','pencil','points','coefficients','entries','values','vectors'):
                        walk(v,ptr+'/'+str(k).replace('~','~0').replace('/','~1'),ctx)
        elif isinstance(x,list):
            for i,v in enumerate(x):
                if isinstance(v,dict): walk(v,ptr+'/'+str(i),ctx)
                elif isinstance(v,list) and any(isinstance(z,(dict,list)) for z in v): walk(v,ptr+'/'+str(i),ctx)
    seed={}
    m=re.search(r'(?:^|_)n(\d+)_d(\d+)(?:_|\.)',pathlib.PurePosixPath(path).name)
    if m: seed={'n':int(m[1]),'delta':int(m[2])}
    walk(obj,inherited=seed)
    # Matrix certificates often record their cell only in the human-readable title.
    if isinstance(obj,dict) and isinstance(obj.get('title'),str):
        title=obj['title']; m=re.search(r'lambda=(\([^)]*\)).*?n=(\d+).*?delta=(\d+)',title)
        if m:
            try:
                c=cell(int(m[2]),int(m[3]),ast.literal_eval(m[1])); found.setdefault(json.dumps(c,sort_keys=True),
                    dict(key=c,pointer='/title',key_method='explicit title tuple with n/delta',variety_context=obj.get('matrix_role','unknown')))
            except (ValueError,SyntaxError): issues.append(dict(pointer='/title',reason='invalid cell in title'))
    return list(found.values()), issues, list(families.values())

META = re.compile(r'(manifest|registry|unparsed_sources|parsed_sources|artifacts|input_hash|resource|timing|points|nodes|queue|census|source|basis|config|seed|pencil|delivery|inventory|status|plan|checksums)',re.I)
RESULT_FIELDS = {'rank','rank_Q','rank_mod_p','mult','mult_det','mult_pad','D','i','i_det','i_pad','det',
                 'passed','pass','ok','verified','nonzero','checks','claims','identity','identities','proof','conclusion','verdict'}

def classify(path,obj,known_keys):
    if path.startswith('results/logs/') or pathlib.PurePosixPath(path).name in ('cert_manifest.json','s79_cert_manifest.json','s79_certificate_availability.part00.jsonl'):
        return 'metadata','process/resource log or certificate inventory; not a rank replay'
    result_fields=set()
    def walk(x):
        if isinstance(x,dict):
            result_fields.update(set(x)&RESULT_FIELDS)
            for k,v in x.items():
                if k not in ('points','basis','terms','coefficients','pencil','matrix','kernel_chi') and isinstance(v,(dict,list)): walk(v)
        elif isinstance(x,list):
            for v in x:
                if isinstance(v,dict): walk(v)
    walk(obj)
    if result_fields:
        return 'result','recorded result fields: '+', '.join(sorted(result_fields))
    if META.search(pathlib.PurePosixPath(path).name):
        return 'metadata','support/input/census/manifest role; no recognized result assertion'
    return 'result','banked data artifact; numerical/proof semantics not independently replayed'

def recorded_claims(obj):
    claims=[];references=[]
    def walk(x,ptr=''):
        if isinstance(x,dict):
            for k,v in x.items():
                pointer=ptr+'/'+str(k)
                if k in ('status','conclusion','claim','field_note','field','instrument','meaning','verdict') and isinstance(v,(str,int,bool)):
                    claims.append(dict(pointer=pointer,source_text=str(v)[:700],validation='RECORDED_ONLY'))
                if k in ('source','source_path','certificate','path','file','input') and isinstance(v,str) and v.startswith('results/'):
                    candidate=v.split(':',1)[0]
                    references.append(dict(pointer=pointer,path=candidate,present=(ROOT/candidate).is_file(),status='reference only'))
                if isinstance(v,(dict,list)) and k not in ('points','basis','terms','vectors','matrix','values','entries','kernel_chi','R','G','A','E'):
                    walk(v,pointer)
        elif isinstance(x,list):
            for i,v in enumerate(x):
                if isinstance(v,dict):walk(v,ptr+'/'+str(i))
    walk(obj)
    return claims[:40],references[:40],len(claims),len(references)

def inventories(blobs, inputs, historical):
    parsed=read(OLD+'parsed_sources.json')
    require_unique_paths(historical)
    # Old parser joined source rows; use these as attributed key hints, never as verification.
    catalog=collections.defaultdict(dict)
    for p in sorted(q for q in blobs if q.startswith(OLD+'cells.part') and q.endswith('.jsonl')):
        for row in read(p):
            try: c=cell(row.get('n'),row.get('delta'),row.get('lam'))
            except ValueError: continue
            for obs in row.get('observations',[]):
                src=obs['source'].rsplit(':',1)[0]
                catalog[src][json.dumps(c,sort_keys=True)]=dict(key=c,pointer='historical catalog:'+row['id'],
                    key_method='attributed old catalog',variety_context='see historical observation')
    scope=sorted({p for p in blobs if p.startswith('results/') and p.endswith(('.json','.jsonl'))
                  and not p.startswith(('results/certs/',OLD))} | set(historical))
    rows=[]; profiles=[]
    for p in scope:
        row=dict(path=p, historical_unparsed=p in historical, previously_parsed=p in parsed,
                 frozen_blob=blobs.get(p,{}).get('git_blob'), sha256=inputs.get(p,{}).get('sha256'),
                 status='RECORDED', independent_replay=False, superseded_by=None)
        if not (ROOT/p).is_file():
            row.update(classification='metadata',classification_reason='missing referenced input; no artifact to interpret',
                       presence='missing',cell_keys=[],cell_key_status='unknown_missing_input',parse_status='missing')
        else:
            try:
                obj=read(p); keys,issues,families=keys_in(obj,p)
                unique={json.dumps(v['key'],sort_keys=True):v for v in keys}
                for ck,value in catalog.get(p,{}).items(): unique.setdefault(ck,value)
                cls,why=classify(p,obj,list(unique.values()))
                claims,refs,claimcount,refcount=recorded_claims(obj)
                row.update(classification=cls,classification_reason=why,presence='present',parse_status='parsed',family_keys=families,
                           recorded_claim_samples=claims,recorded_claim_count=claimcount,explicit_reference_samples=refs,explicit_reference_count=refcount,
                           cell_keys=list(unique.values()),cell_key_status='resolved' if unique else
                           ('family_only' if families else 'not_applicable_metadata' if cls=='metadata' else
                            'not_applicable_geometry' if p.startswith(('results/astra/S2/','results/b13_12/')) else 'unknown_no_complete_cell_schema'),
                           cell_key_issues=issues[:25],cell_key_issue_count=len(issues))
                profiles.append(dict(path=p,classification=cls,keys=len(unique),
                                     schema=list(obj)[:30] if isinstance(obj,dict) else 'list:'+str(len(obj))))
            except (ValueError,UnicodeError,OSError) as e:
                row.update(classification='result',classification_reason='unreadable banked result',presence='present',
                           cell_keys=[],cell_key_status='unknown_parse_failure',parse_status='failed',error=str(e))
        rows.append(row)
    # Byte-identical duplicates are provenance links, never automatic supersession.
    groups=collections.defaultdict(list)
    for r in rows:
        if r.get('frozen_blob'):groups[r['frozen_blob']].append(r['path'])
    for r in rows:
        r['identical_frozen_blob_paths']=[p for p in groups.get(r.get('frozen_blob'),[]) if p!=r['path']]
    jsonl('file_register.jsonl',rows); write('schema_profiles.json',profiles)
    oldrows=[r for r in rows if r['historical_unparsed']]
    assert {r['path'] for r in oldrows}==set(historical)
    return dict(historical_listed=len(historical),historical_present=sum(r['presence']=='present' for r in oldrows),
                historical_classes=dict(collections.Counter(r['classification'] for r in oldrows)),
                historical_cell_key_status=dict(collections.Counter(r['cell_key_status'] for r in oldrows)),
                current_frozen_json_jsonl_scope=len(rows),current_classes=dict(collections.Counter(r['classification'] for r in rows)),
                newly_encountered_since_old_lists=sum(not r['historical_unparsed'] and not r['previously_parsed'] for r in rows),
                current_without_old_observation_parser=sum(not r['previously_parsed'] for r in rows),
                scope_excludes='the review-only integration mirror itself, compressed certificates (counted separately), non-JSON/JSONL files',
                parse_failures=[r['path'] for r in rows if r['parse_status']!='parsed'],
                meaning='File/role registration complete; unknown cell identities and proof/replay backlog remain explicit.')

def certificate_key(path):
    name=pathlib.PurePosixPath(path).name
    match=re.match(r'(?:per\d+_)?([\d_]+)_d(\d+)_(.+)_p(\d+)\.json.gz$',name)
    if not match: raise ValueError('unrecognized certificate filename')
    lam=[int(x) for x in match[1].split('_')]; d=int(match[2]); n=sum(lam)//d
    return cell(n,d,lam),match[3],int(match[4])

def certs(blobs):
    rows=[]; summaries={}; records={}
    for p in ['results/s79_calibration6.jsonl','results/s79_cells.jsonl','results/s79_per6.jsonl'] + sorted(
            q for q in blobs if re.match(r'results/b13_09/per_r\d+_d\d+\.jsonl$',q)):
        for i,r in enumerate(read(p)):
            for c in r.get('certs',[]):
                path=c[0] if isinstance(c,list) else c
                records[path]=dict(source=p,line=i+1,producer_bytes=c[1] if isinstance(c,list) else None,
                                  N_S=r.get('N_S'),n_chi=r.get('n_chi'),a=r.get('a'),secs=r.get('secs'),
                                  hwm_gb=r.get('hwm_gb'),seeds=r.get('seeds'),bound=r.get('bound'))
    for manpath in MANIFESTS:
        man=read(manpath); entries=man.get('files',man.get('cert_files'))
        require_unique_paths([x['path'] for x in entries])
        group=[]
        for idx,entry in enumerate(entries):
            path=entry['path']; c,kind,prime=certificate_key(path)
            present=(ROOT/path).is_file() and path in blobs
            cut=man.get('size_cut_bytes'); shipped=entry.get('shipped',entry.get('shipped_in_bundle'))
            reason='not_absent' if present else 'unknown'
            explanation='present in frozen tree' if present else 'no supported historical cause'
            if not present and shipped is False and cut is not None and entry['bytes']>cut and str(pathlib.PurePosixPath(path).parent) not in man.get('keep_all_in',[]):
                reason='size_guard'; explanation=f'recorded shipping cut {cut} bytes; manifest bytes={entry["bytes"]}, shipped=false; not a producer expansion guard'
            elif not present and manpath.endswith('b13_09/cert_manifest.json') and shipped is False:
                explanation='manifest records written file omitted from shipped chronological prefix/total bundle size; no per-file size guard proved'
            row=dict(manifest=manpath,manifest_index=idx,path=path,cell_key=c,kind_from_path=kind,prime=prime,
                     expected_bytes=entry['bytes'],expected_md5=entry['md5'],declared_shipped=shipped,
                     present=present,presence='present' if present else 'missing',historical_reason=reason,
                     reason_evidence=explanation,producer_record=records.get(path),superseded_by=None,
                     independent_replay=False,replay_status='NOT_REPLAYED' if present else 'MISSING',
                     recovery_status='not_attempted',frozen_blob=blobs.get(path,{}).get('git_blob'))
            if present:
                raw=(ROOT/path).read_bytes(); actual=hashlib.md5(raw).hexdigest()
                row.update(actual_bytes=len(raw),actual_md5=actual,sha256=sha(raw),
                           bytes_match=len(raw)==entry['bytes'],md5_match=actual==entry['md5'])
                try:
                    # Large compressed bases expand into hundreds of MB of Python lists.
                    # Hash the full stream, but materialize only bounded payloads.
                    h=hashlib.sha256(); head=bytearray(); payload_bytes=0
                    with gzip.open(ROOT/path,'rb') as stream:
                        for block in iter(lambda:stream.read(65536),b''):
                            h.update(block); payload_bytes+=len(block)
                            if len(head)<1024*1024+1: head.extend(block[:1024*1024+1-len(head)])
                    row.update(payload_sha256=h.hexdigest(),payload_bytes=payload_bytes)
                    row['native_verifier_capability']='record consistency only; no rank re-derivation' if kind=='hybrid' else 'full-rank re-derivation supported; not run here'
                    wrong_direction=b'a kernel mod p bounds i from below only' in head
                    row['semantic_cautions']=['producer field_note reverses ideal-nullity inequality; correct direction is i_Q<=nullity_p, not a lower bound'] if wrong_direction else []
                    if payload_bytes>1024*1024:
                        row.update(parse_status='DEFERRED_SIZE_LIMIT',payload_kind=('hybrid_kernel' if kind=='hybrid' else 'full_rank' if 'fullrank' in kind else 'unknown'),
                                   payload_kind_provenance='filename inference only; full payload not decoded',
                                   replay_status='NOT_REPLAYED_SIZE_LIMIT')
                        if not row['md5_match']: row['digest_disposition']='compressed bytes differ; historical payload digest unavailable; equivalence unknown'
                        group.append(row); rows.append(row); continue
                    obj=json.loads(head)
                    row.update(canonical_json_sha256=sha(json.dumps(obj,sort_keys=True,separators=(',',':')).encode()),
                               payload_kind=obj.get('kind'),parse_status='json_decoded',payload_cell=obj.get('cell'),
                               replay_status='NOT_REPLAYED_RECORD_ONLY_KIND' if obj.get('kind')=='hybrid_kernel' else 'NOT_REPLAYED')
                    row['payload_cell_matches']=obj.get('cell') is not None and all(obj['cell'].get(k)==v for k,v in
                         [('n',c['n']),('r',c['ell']),('delta',c['delta']),('lambda',c['lambda'])])
                    if not row['md5_match']:
                        row['digest_disposition']='compressed bytes differ; historical uncompressed digest unavailable; semantic equivalence unknown'
                    del obj; gc.collect()
                except (ValueError,OSError) as e: row.update(parse_status='failed',error=str(e),replay_status='UNPARSEABLE')
            group.append(row); rows.append(row)
        summaries[manpath]=dict(listed=len(group),present=sum(x['present'] for x in group),
            missing=sum(not x['present'] for x in group),missing_reasons=dict(collections.Counter(x['historical_reason'] for x in group if not x['present'])),
            present_md5_matches=sum(x.get('md5_match',False) for x in group),present_md5_mismatches=sum(x.get('md5_match') is False for x in group),
            present_kinds=dict(collections.Counter(x.get('payload_kind','unknown') for x in group if x['present'])))
    jsonl('certificate_register.jsonl',rows)
    queue=sorted([r for r in rows if not r['present']],key=lambda r:((r.get('producer_record') or {}).get('N_S') or 10**20,r['expected_bytes'],r['path']))
    write('recovery_queue.json',dict(limit='up to four cheapest eligible cells; 90 s/768 MiB each, 360 s total',
          producer_dependencies='numpy, scipy, python-flint; scipy/flint absent in this runtime',
          candidates=[dict(path=r['path'],cell=r['cell_key'],kind=r['kind_from_path'],bytes=r['expected_bytes'],
                 source_record=r['producer_record'],historical_reason=r['historical_reason']) for r in queue]))
    return summaries

def controls():
    results=[]
    for name,fn in [
        ('wrong_cell_degree',lambda:cell(4,8,[3,3,3])),
        ('bad_partition_order',lambda:cell(3,2,[2,4])),
        ('empty_inventory',lambda:require_unique_paths([])),
        ('missing_certificate',lambda:read('results/b14_10/definitely_missing_certificate.json'))]:
        try: fn()
        except (ValueError,FileNotFoundError): results.append(dict(control=name,rejected=True))
        else: raise AssertionError(name+' incorrectly accepted')
    return results

def main():
    OUT.mkdir(parents=True,exist_ok=True)
    blobs=frozen(); historical=read(OLD+'unparsed_sources.json')
    inputs=capture(blobs,historical)
    summary=dict(board_numbering='batch14',base=BASE,tree=TREE,actual_model='gpt-6-astra')
    summary['files']=inventories(blobs,inputs,historical)
    summary['certificates']=certs(blobs); summary['controls']=controls()
    write('inventory_summary.json',summary); print(json.dumps(summary,indent=2))

if __name__=='__main__': main()
