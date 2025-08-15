def take():
    lst=[]
    for _ in range(5):
        nums=int(input("Enter the numbers:"))
        lst.append(nums)

    return lst

def removing(l):
    result=[]
    for num in l:
        if num not in result:
            result.append(num)
    
    return result

l=take()
print(removing(l))