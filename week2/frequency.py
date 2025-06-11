number=[1,2,3,4,1,2,3,4,1,23,4]
num_count={}
for num in number:
    if num  in num_count:
        num_count[num]+=1
    else:
        num_count[num]=1
print(num_count)