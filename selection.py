def sort(nums):
    for i in range(6):
        min=i
        for j in range(i,7):
            if nums[j]<nums[min]:
                min=j

        temp=nums[i]
        nums[i]=nums[min]
        nums[min]=temp

nums=[5,4,7,9,1,0,2]
sort(nums)
print(nums)