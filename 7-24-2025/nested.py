def take_num():
    numbers = []
    for _ in range(8):
        number = int(input("Enter the number: "))
        numbers.append(number)
    return numbers

def nesting(nums):
    big = []
    mid = []
    smol = []

    for num in nums:
        if num >= 50:
            big.append(num)
        elif 25 <= num <= 35:
            mid.append(num)
        else:
            smol.append(num)

    nested = [big, [mid, [smol]]]
    return nested

nums = take_num()
nest = nesting(nums)
print("Nested List:", nest)
