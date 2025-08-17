lst=[12,34,2,67]
min=lst[0]
max=lst[0]

for num in lst:
    if max>num:
        max=num
    
    if min<num:
        min=num
print (min,max)