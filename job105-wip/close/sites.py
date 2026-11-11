import difflib, sys
SP=sys.argv[1]
old=open("/tmp/job105-work/BOOK2-20261102.md",encoding="utf-8").read().split("\n\n")
new=open(SP+"/close/BOOK2-20261111.md",encoding="utf-8").read().split("\n\n")
sm=difflib.SequenceMatcher(None,old,new,autojunk=False)
labels=[]; c="front matter"; s=""
for p in new:
    for l in p.split("\n"):
        if l.startswith("# ") or l.startswith("## "): c=l.lstrip("# ").strip(); s=""
        elif l.startswith("### "): s=l[4:].strip()
    labels.append((c,s))
rows=[]; gone=[]
for op,i1,i2,j1,j2 in sm.get_opcodes():
    if op=="equal": continue
    for j in range(j1,j2):
        c,s=labels[j]
        kind="new" if op=="insert" else "changed"
        rows.append(f"- {c}{' / '+s if s else ''} — {kind}: {new[j].strip().split(chr(10))[0][:80]}")
    if op=="delete":
        for i in range(i1,i2): gone.append("- out: "+old[i].strip().split(chr(10))[0][:80])
open(SP+"/close/sites.md","w",encoding="utf-8").write("\n".join(rows)+"\n\nWholly removed paragraphs:\n"+"\n".join(gone)+"\n")
print(len(rows),"rows;",len(gone),"removed")
