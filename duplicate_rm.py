lst=[1,2,4,2,6,1,8,8,2,1]
lst.sort()
i=0
while i<len(lst)-1:
    if(lst[i]==lst[i+1]):
        lst.remove(lst[i+1])
    else:
        i+=1
print(lst)