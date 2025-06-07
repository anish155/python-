arr=[1,2,3,4]
for i in range(len(arr)):
    for j in range(i,len(arr)):
        subarry=arr[i:j+1]
        print(subarry)
length=len(arr)
sum=int(length*(length+1)/2)
print("total number of subarray:",sum)