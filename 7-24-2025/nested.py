def take_num():
    for _ in range (8):
        number=int(input("Enter the numbers:"))
    return number
def nesting(nums):
    main=[]
    big=[]
    mid=[]
    smol=[]
    if nums>=50:
        big.extend(nums)
    elif nums>=25 and nums<=35:
        mid.extend(nums)
    else:
        smol.extend(nums)
    structure=main.append(big.append(mid.append(smol)))
    return structure

nums=take_num()
nest=nesting(nums)
print(nest)