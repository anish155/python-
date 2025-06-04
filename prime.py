'''def prime(num):
    if num<2:
        print("it is not a prime number.")
        return
    for i in range(2,int(num**0.5)+1):
        if num%i==0:
            print(num,"this is not prime number")
            return
    print(num,"this is a prime number.")
prime(12)'''

def Input():
    num=int(input("Enter the number:"))
    return num
def Check(num):
    if(num<2):
        print(num,"the number is not a prime number. ")
    for i in range(2,int(num**0.5)+1):
        if(num%i==0):
            print(num,"the number is not a prime.")
        else:
            print(num,"this number is a prime number.")
    return num
num=Input()
Check(num)
