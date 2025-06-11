def Input():
    num=int(input("enter a number:"))
    return num
def Check(num):
    if(num<2):
        return False
    for i in range(2,int(num**0.5)+1):
        if(num%i==0):
            return False
        else:
            print(num,"this is a prime number.")
            Factor(num)
def Factor(num):
    for i in range(1,num+1):
        if num%i==0:
            print(i)
num=Input()
Check(num)