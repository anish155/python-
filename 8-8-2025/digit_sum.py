def take_num():
    num=int(input("Enter the number:"))
    return num

def sum_digit(num):
    total=0
    for n in str(num):
        total+=int(n)
    return total

num=take_num()
print(f"The sum of digits is: {sum_digit(num)}")
