lst=[23,1,87,90,120]
result=max(lst)
print(result)

max_val=lst[0]
for val in lst:
    if val>max_val:
        max_val=val

print(f"{max_val} is the greatest.")

