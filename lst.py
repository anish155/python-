'''lst=[]
for i in range(10):
    number=int(input("enter:"))
    lst.append(number)
unique=set(lst)

print(unique)'''

lst=[1,2,3,1,2,3,4,5,6,4,5,6,8,9,0,8,2,5]
num=set(lst)
number=sorted(num)
print(number)
