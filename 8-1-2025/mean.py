def take_nums():
    numbers=[]
    for _ in range(10):
        x=int(input("Enter the numbers:"))
        numbers.append(x)
    return numbers

def calc_mean(nums):
    mean=sum(nums)/len(nums)
    return mean

nums=take_nums()
result=calc_mean(nums)
print(f"The mean of given numbers are:{result}")