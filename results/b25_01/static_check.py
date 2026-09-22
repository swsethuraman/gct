"""Administrative static check of det4-blindness.tex (not a compile, not a mathematical computation)."""
import re, sys, collections
path = sys.argv[1]
t = open(path, encoding="utf-8").read()
body = "\n".join(l.split("%")[0] if not l.lstrip().startswith("%") else "" for l in t.splitlines())
out = []
cids = re.findall(r"\\cid\{(C\d+)\}", body)
cnt = collections.Counter(cids)
heading = re.findall(r"\\begin\{\w+\}\[\\cid\{(C\d+)\}", body)
caption = re.findall(r"\\caption\{[^}]*\\cid\{(C\d+)\}", body)
ids = sorted(set(cids), key=lambda s: int(s[1:]))
expected = [f"C{i:02d}" for i in range(1, 52)]
out.append(f"claim IDs distinct: {len(ids)}; expected C01..C51 present: {ids == expected}")
out.append(f"IDs on a result heading: {len(heading)} (distinct {len(set(heading))}); on a caption: {caption}")
dup_head = [k for k, v in collections.Counter(heading).items() if v > 1]
out.append(f"duplicate heading IDs: {dup_head}")
labels = re.findall(r"\\label\{([^}]*)\}", body)
lc = collections.Counter(labels)
refs = set(re.findall(r"\\(?:ref|eqref|pageref)\{([^}]*)\}", body))
out.append(f"labels: {len(labels)}; duplicated: {[k for k,v in lc.items() if v>1]}")
out.append(f"refs: {len(refs)} distinct; undefined: {sorted(refs - set(labels))}")
lits = set(re.findall(r"\\lit\{([^}]*)\}", body)) | set(re.findall(r"\\cite\{([^}]*)\}", body))
bibs = set(re.findall(r"\\bibitem\{([^}]*)\}", body))
out.append(f"cited keys without bibitem: {sorted(lits - bibs)}; bibitems never cited: {sorted(bibs - lits)}")
begins = collections.Counter(re.findall(r"\\begin\{([^}]*)\}", body))
ends = collections.Counter(re.findall(r"\\end\{([^}]*)\}", body))
out.append(f"environment imbalance: {({k: begins[k]-ends[k] for k in set(begins)|set(ends) if begins[k]!=ends[k]})}")
b = body.replace("\\{", "").replace("\\}", "")
out.append(f"brace balance (open - close): {b.count('{') - b.count('}')}")
nprov = body.count("\\prov{") - body.count("\\newcommand{\\prov}")
out.append(f"provenance lines (\\prov uses, excluding its definition): {nprov}")
out.append("note: '#1' above is the parameter inside the \\lit macro definition, not a citation")
out.append(f"$ count parity (even expected): {(body.replace(chr(92)+'$','').count('$')) % 2 == 0}")
print("\n".join(out))
