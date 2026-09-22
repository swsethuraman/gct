import re, sys
t = sys.stdin.read()
sec = 0; cnt = 0
envs = "theorem|proposition|lemma|corollary|fact|definition|ruling|record|question|remark"
for m in re.finditer(r"\\section\{|\\begin\{(" + envs + r")\}(\[[^\n]*)?", t):
    if m.group(0).startswith("\\section"):
        sec += 1; cnt = 0; continue
    cnt += 1
    rest = m.group(2) or ""
    cid = re.search(r"\\cid\{(C\d+)\}", rest); lab = re.search(r"\\label\{([^}]*)\}", rest)
    print(f"{cid.group(1) if cid else '-'}\t{m.group(1)} {sec}.{cnt}\t{lab.group(1) if lab else '-'}")
