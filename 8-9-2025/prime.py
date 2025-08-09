def take_num():
    number=int(input("Enter the number:"))
    return number

def prime(num):
    if(num<2):
        print(f"{num} is not a prime number.")
    
    for i in range(2,int(num**0.5)+1):
        if(num%i==0):
            print(f"{num} is not a prime number.")
        else:
            print(f"{num} is a prime number.")

num=take_num()
prime(num)