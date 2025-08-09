def take_list():
    lst=[]
    for _ in range(5):
        nums=int(input("Enter the numbers in the list:"))
        lst.append(nums)
    return lst

def second(lst):

    largest=second_largest=float('-inf')

    for num in lst:
        if num>largest:
            second_largest=largest
            largest=num
        
        elif largest>num>second_largest:
            second_largest=num
        
    return second_largest

lst=take_list()
print(f"Second largest number is: {second(lst)}")
