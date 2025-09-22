# lst=[12,34,2,67]
# min=lst[0]
# max=lst[0]

# for num in lst:
#     if num>max:
#         max=num
    
#     if num<min:
#         min=num
# print (min,max)

def Take():
    lst=[]
    print("Entering the data")
    for _ in range(5):
        elements=int(input("Enter the numbers:"))
        lst.append(elements)
    return lst

def Max(nums):
    max=nums[0]
    for num in nums:
        if num>max:
            max=num
    print(max)

def Min(nums):
    min=nums[0]
    for num in nums:
        if num<min:
            min=num
    print(min)

nums=Take()
Max(nums)
Min(nums)
