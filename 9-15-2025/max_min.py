def Take():
    array=[]
    print("INSERTING DATA")
    for i in range(5):
        element=int(input("Enter the numbers:"))
        array.append(element)
    return array
    
def Max(nums):
    num=nums[0]
    for n in nums:
        if n>num:
            num=n

    print(f"The greatest element in array is: {num}")

def Min(nums):
    num=nums[0]
    for n in nums:
        if n<num:
            num=n
        
    print(f"The lowest element in array is: {num}")
            
nums=Take()
Max(nums)
Min(nums)

