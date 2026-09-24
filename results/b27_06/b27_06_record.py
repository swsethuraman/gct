"""Read-only Git provenance and record retrieval; not a mathematical run."""
import argparse, collections, datetime, gzip, hashlib, io, json, pathlib, re, subprocess, time, zipfile, zlib

OUT = pathlib.Path(__file__).resolve().parent
REPO = pathlib.Path('C:/Users/swami/Projects/gct-gpt/work/batch15')
C = '7c36a52ddf338eb390a9bcd491cb9c50cf9e2a19'

def git(*args, **kw):
    return subprocess.check_output(['git', '-C', str(REPO), *args], **kw)

def save(name, obj):
    (OUT / name).write_text(json.dumps(obj, indent=2, ensure_ascii=False) + '\n', encoding='utf-8')

def digest(data):
    return hashlib.sha256(data).hexdigest()

def snapshot(paths):
    (OUT / 'inputs').mkdir(exist_ok=True)
    fn = OUT / 'INPUT_BINDINGS.json'
    entries = json.loads(fn.read_text(encoding='utf-8')) if fn.exists() else []
    for path in paths:
        commit = C
        if ':' in path:
            commit, path = path.split(':', 1)
            commit = git('rev-parse', commit).decode().strip()
        data = git('show', f'{commit}:{path}')
        name = 'inputs/' + ('' if commit == C else commit[:8] + '__') + path.replace('/', '__')
        (OUT / name).write_bytes(data)
        ent = dict(commit=commit, path=path, git_blob=git('rev-parse',f'{commit}:{path}').decode().strip(),
                   sha256=digest(data), bytes=len(data), snapshot=name, convention='raw git blob content')
        entries = [e for e in entries if (e['commit'],e['path']) != (commit,path)]
        entries.append(ent)
        save('INPUT_BINDINGS.json', entries)
        print(f'{path}: {len(data)} bytes {ent["sha256"]}')
    save('INPUT_BINDINGS.json', entries)

def inventory():
    refs = git('for-each-ref', '--format=%(refname) %(objectname)')
    (OUT/'GIT_REFS.txt').write_bytes(refs)
    raw = git('rev-list', '--objects', '--all')
    (OUT/'GIT_REACHABLE_OBJECTS.txt').write_bytes(raw)
    paths = dict(line.decode('utf-8').split(' ',1) if b' ' in line else (line.decode(),'') for line in raw.splitlines())
    p=subprocess.run(['git','-C',str(REPO),'cat-file','--batch-check=%(objectname) %(objecttype) %(objectsize)'],
                     input=('\n'.join(paths)+'\n').encode(),capture_output=True,check=True)
    (OUT/'GIT_OBJECT_SIZES.txt').write_bytes(p.stdout)
    rows=[]
    for line in p.stdout.decode().splitlines():
        oid,typ,size=line.split()
        if typ=='blob': rows.append(dict(oid=oid,path=paths[oid],bytes=int(size)))
    save('RECORD_INVENTORY.json', dict(utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),
        refs_sha256=digest(refs),reachable_objects_sha256=digest(raw),blobs=rows))
    ex=collections.Counter(pathlib.Path(r['path']).suffix for r in rows)
    print(json.dumps(dict(blobs=len(rows),bytes=sum(r['bytes'] for r in rows),extensions=ex.most_common(),
                          largest=sorted(rows,key=lambda r:r['bytes'],reverse=True)[:12]),indent=2))

def search():
    start=time.monotonic()
    rows=json.loads((OUT/'RECORD_INVENTORY.json').read_text())['blobs']
    patterns=[re.compile(rb'(?<![0-9])12[\s,;_|:\[\]()"\']+8[\s,;_|:\[\]()"\']+6[\s,;_|:\[\]()"\']+4[\s,;_|:\[\]()"\']+2(?![0-9])'),
              re.compile(rb'(?<![0-9])14[\s,;_|:\[\]()"\']+10[\s,;_|:\[\]()"\']+6[\s,;_|:\[\]()"\']+4[\s,;_|:\[\]()"\']+2(?![0-9])')]
    matches=[]; binary=[]; errors=[]; scanned=0; decoded=0
    p=subprocess.Popen(['git','-C',str(REPO),'cat-file','--batch'],stdin=subprocess.PIPE,stdout=subprocess.PIPE)
    def scan(data,row,member=None):
        nonlocal decoded
        decoded+=len(data)
        hits=[]
        for i,pat in enumerate(patterns):
            for m in pat.finditer(data):
                lo=max(data.rfind(b'\n',0,m.start())+1,m.start()-350)
                hi=data.find(b'\n',m.end())
                if hi<0: hi=len(data)
                hits.append(dict(cell=i,offset=m.start(),line=data.count(b'\n',0,m.start())+1,
                                 excerpt=data[lo:min(hi,m.end()+700)].decode('utf-8',errors='replace')))
        if hits:
            matches.append(dict(**row,member=member,searched_content_sha256=digest(data),hits=hits))
    for row in rows:
        p.stdin.write((row['oid']+'\n').encode()); p.stdin.flush()
        hdr=p.stdout.readline().split(); data=p.stdout.read(int(hdr[2])); assert p.stdout.read(1)==b'\n'
        assert len(data)==row['bytes']
        scanned+=1
        if scanned%1000==0: print('scanned',scanned,'of',len(rows),flush=True)
        if data[:2]==b'\x1f\x8b':
            try: expanded=gzip.decompress(data)
            except (EOFError,zlib.error,gzip.BadGzipFile) as e:
                errors.append(dict(**row,error=str(e)))
                expanded=zlib.decompressobj(16+zlib.MAX_WBITS).decompress(data)
            scan(expanded,row,'gzip-decompressed')
        elif data[:4]==b'PK\x03\x04':
            z=zipfile.ZipFile(io.BytesIO(data))
            members=[]
            for n in z.namelist():
                if n.endswith('/'): continue
                d=z.read(n); members.append(n)
                if b'\0' not in d: scan(d,row,n)
            binary.append(dict(**row,kind='zip',members=members))
        elif b'\0' in data or data[:4]==b'%PDF':
            binary.append(dict(**row,kind='binary'))
        else: scan(data,row)
    p.stdin.close(); p.wait()
    save('RECORD_SEARCH_MATCHES.json',matches)
    save('RECORD_SEARCH_BINARY.json',binary)
    save('RECORD_SEARCH_ERRORS.json',errors)
    summary=dict(search='all unique blobs reachable from all local refs at inventory time; text plus gzip plus text zip members',
                 blob_count=scanned,raw_bytes=sum(r['bytes'] for r in rows),decoded_search_bytes=decoded,
                 patterns=[p.pattern.decode() for p in patterns],matched_blobs_or_members=len(matches),
                 hits=sum(len(m['hits']) for m in matches),binary_objects=len(binary),wall_seconds=time.monotonic()-start)
    save('RECORD_SEARCH_SUMMARY.json',summary)
    print(json.dumps(summary,indent=2))
    for row in binary:
        if pathlib.Path(row['path']).suffix in ['.pdf','.pkl','.dat']:
            print('BINARY_REVIEW',row['path'],row['oid'])

if __name__=='__main__':
    ap=argparse.ArgumentParser(); ap.add_argument('mode'); ap.add_argument('paths',nargs='*'); a=ap.parse_args()
    if a.mode=='snapshot': snapshot(a.paths)
    elif a.mode=='inventory': inventory()
    elif a.mode=='search': search()
    else: raise ValueError(a.mode)
