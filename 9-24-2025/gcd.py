def Take():
    print("Entering two numbers:")
    a=int(input("Enter the first number:"))
    b=int(input("Enter the second number:"))
    return a,b

def GCD(a,b):
    while b!=0:
        temp=b
        b=a%b
        a=temp
    return a

a,b=Take()
result=GCD(a,b)
print(result)