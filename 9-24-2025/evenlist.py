def Take():
    lst=[]
    print("Adding element for the list:")
    for _ in range(8):
        numbers=int(input("Enter the numbers:"))
        lst.append(numbers)
    return lst

def even(nums):
    even=[]
    for num in nums:
        if num%2==0:
            even.append(num)
            even.sort()
    print (even)



nums=Take()
even_lst=even(nums)
