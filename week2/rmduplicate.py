'''number=[1,1,1,2,2,2,3,3,3,4,4,4]
unique=[]
for num in number:
    if num not in unique:
        unique.append(num)
print(unique)'''
number=[1,1,1,1,2,2,2,2,3,3,3,4,4,4]
print(list(set(number)))