def take_num():
    numbers=[]
    for _ in range(10):
        nums=int(input("Enter the numbers:"))
        numbers.append(nums)
    return numbers

def median(nums):
    nums.sort()
    n=len(nums)
    if n%2==0:
        mid1 = nums[n // 2 - 1]
        mid2 = nums[n // 2]
        return (mid1 + mid2) / 2
    else:
        return nums[n//2]
    
nums=take_num()
result=median(nums)
print(f"the median is: {result}")