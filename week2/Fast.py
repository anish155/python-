def Input():
    arr=[]
    for i in range(10):
        num=int(input("enter the numbers:"))
        arr.append(num)
    print(arr)
    return arr
def Check(arr):
    target=90
    arr.sort()
    start=0
    end=len(arr)-1
    for number in range(len(arr)):
        mid=(start+end)//2
        if(arr[mid]==target):
            print(f"{target} found at index {mid} in sorted list.")
            return mid
        elif(arr[mid]<target):
            start=mid+1
        else:
            end=mid-1
    print(f"{target} not found in the list.")
    return -1
nums=Input()
Check(nums)