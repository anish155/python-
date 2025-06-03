def prime(num):
    if num<2:
        print("it is not a prime number.")
        return
    for i in range(2,int(num**0.5)+1):
        if num%i==0:
            print(num,"this is not prime number")
            return
    print(num,"this is a prime number.")
prime(12)
