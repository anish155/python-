def lst():
    container=[]
    for i in range(10):
        num=int(input("Enter the numbers:"))
        container.append(num)
    return container

def largest_1and2(number):
    first=second=float("-inf")
    for num in number:
        if num>first:
            second=first
            first=num
        elif num>second and num!=first:
            second=num
    
    return first,second
nums=lst()
largest,second_largest=largest_1and2(nums)
print("the largest number is:",largest)
print("the second largest number is:",second_largest)
