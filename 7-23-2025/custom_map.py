def my_map(func,iterate):
    result=[]
    for items in iterate:
        result.append(func(items))
    return result

def sq_numbers(nums):
    return nums*nums

nums=[1,2,3,4]
squaring=my_map(sq_numbers,nums)
print(squaring)