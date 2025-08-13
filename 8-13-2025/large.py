def take():
    lst=[]
    for _ in range(5):
        nums=int(input("Enter the numbers:"))
        lst.append(nums)

    return lst

def largest(num):
    
    return max(num)

num=take()
print(largest(num))