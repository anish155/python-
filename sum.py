arr=[2,3,4,5,6,7]
target=9
for x in range(0,len(arr)):
    for y in range(arr[x]+1,len(arr)):
        if arr[x]+arr[y]==target:
            print("sum:",arr[x],arr[y])
    break


