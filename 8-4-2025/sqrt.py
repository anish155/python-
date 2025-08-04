from math import sqrt as sq
def take_num():
    number=int(input("Enter the number:"))
    return number

def square(num):
    squrt=sq(num)
    return squrt

num=take_num()
print(f"the square root of number {num} is: {int(square(num))}")

