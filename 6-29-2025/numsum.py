def take_num():
    num=input("Enter the number:")
    return num
def add(n):
    total=0
    for x in n:
        if x.isdigit():
            total+=int(x)
    print("Sum is:", total)

num=take_num()
add(num)