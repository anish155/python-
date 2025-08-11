def search(target):
    lst=[1,2,3,4,5,6,7,8,9,10]
    smol=0
    big=len(lst)-1
    mid=(smol+big)//2

    while smol <= big:
        mid = (smol + big) // 2  
        if lst[mid] == target:   
            return mid
        elif target < lst[mid]:
            big = mid - 1
        else:
            smol = mid + 1

    return "Out of bounds"

print(search(7))  











