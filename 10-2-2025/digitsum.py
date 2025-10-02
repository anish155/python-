def Take():
    print("Enter the digit:")
    num=int(input("Enter the numbers:"))
    return num


def digi_sum(nums):
    total=0
    while nums>0:
        total+=nums%10
        nums//=10
    print("Sum of digits:", total)

num=Take()
digi_sum(num)


