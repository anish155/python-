word='the man who is the young is the the the the'
count=0
for x in word.split(" "):
    if x=='the':
        count+=1
print(count)