def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

def prime_factorial(n):
    result = 1
    primes = []

    for i in range(2, n+1):
        if is_prime(i):
            primes.append(i)
            result *= i

    
    if primes:
        print("Prime factorial format:")
        print(" × ".join(map(str, primes)), "=", result)
    else:
        print("No primes found up to", n)


prime_factorial(10)

