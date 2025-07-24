def missing(nums):
    n=len(nums)+1
    total=n*(n+1)//2
    actual=sum(nums)
    return total-actual

nums=[1,2,3,4,5,6,7,8,9,]
print("Missing number is:", missing(nums))