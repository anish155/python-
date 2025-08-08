def take():
    alpha_num=int(input("Enter the number you want to see multiple of:"))
    return alpha_num

def multi_table(num):
    print(f"Multiplication Table of {num}:")
    for n in range(1,11):
        print(f"{num}X{n}={num*n}")
    
num=take()
multi_table(num)
