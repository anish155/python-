import random

def is_prime(n):
    if n<2:
        return False
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True

def numList(size,start=1,end=100):
    nums=[random.randint(start,end) for _ in range(size)]
    primes=[n for n in nums if is_prime(n)]

    print("Random numbers:",nums)
    print("Prime numbers:",primes)

numList(10)
