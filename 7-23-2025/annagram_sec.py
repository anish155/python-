words=["bat","tab", "cat", "act", "tac"]

grp={}

for word in words:
    sorted_wrd=''.join(sorted(word))
    if sorted_wrd in grp:
        grp[sorted_wrd].append(word)
    else:
        grp[sorted_wrd]=[word]

result = list(grp.values())
print(result)