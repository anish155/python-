lst=[12,34,2,67]
min=lst[0]
max=lst[0]

for num in lst:
    if num>max:
        max=num
    
    if num<min:
        min=num
print (min,max)