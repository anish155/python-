words=["bat","tab", "cat", "act", "tac"]
sort1=sorted(words[0])
sort2=sorted(words[1])
sort3=sorted(words[2])
sort4=sorted(words[3])
sort5=sorted(words[4])

grp=[]
g1=[]
if sort1==sort2:
    g1.extend([words[0],words[1]])
if g1 not in grp:
    grp.append(g1)

g2=[]
if sort3==sort4==sort5:
    g2.extend([words[2],words[3],words[4]])
if g2 not in grp:
    grp.append(g2)

print(grp)