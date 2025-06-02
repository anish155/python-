arr=["hello","hi","how"]

if not arr:
    print("")
else:
    check=""
for x in range(len(arr[0])):
    char=arr[0][x]
    for word in arr[1:]:
        if x>len(word) or word[x]!=char:
            
            exit()
    check+=char
    print("Common prefix:", check)