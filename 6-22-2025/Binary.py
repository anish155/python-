lst=[10,20,30,40,50,60,70,80,90,100,110,120,130,140,150]
target=90
start=0
end=len(lst)-1
while start<=end:
    mid=(start+end)//2

    if lst[mid]==target:
        print(f"the number was found in index.{mid}")
        break
    elif lst[mid]<target:
        start=mid+1
    else:
        end=mid-1
else:
    print("target was not found.")