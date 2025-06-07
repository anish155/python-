def merging(a,b):
    i=j=0
    merged=[]
    while i<len(a) and j<len(b):
        if a[i]<b[j]:
            merged.append(a[i])
            i+=1
        else:
            merged.append(b[j])
            j+=1

    merged.extend(a[i:])
    merged.extend(b[j:])        
    return merged

first=[1,2,4,6,3,8,5,9]
second=[7,0,4,2,9,1,8,3]
first.sort()
second.sort()
result=merging(first,second)
print(result)