# def in_num():
#     number=int(input("Enter the number:"))
#     return number
# def convert_binary(num):
#     binary=bin(num)[2:]
#     return binary

# num=in_num()
# result=convert_binary(num)
# print(f"the binary number for {num} is {result}")

def in_num():
    number = int(input("Enter the number: "))
    return number

def convert_binary(num):
    if num == 0:
        return "0"
    
    binary = ""
    while num > 0:
        remainder = num % 2
        binary = str(remainder) + binary  
        num = num // 2
    return binary

num = in_num()
result = convert_binary(num)
print(f"The binary number for {num} is {result}")
