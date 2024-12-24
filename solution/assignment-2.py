def sieve_of_eratosthenes(limit):
    primes = [True] * (limit + 1)
    primes[0], primes[1] = False, False  # 0 and 1 are not prime
    
    for i in range(2, int(math.sqrt(limit)) + 1):
        if primes[i]:
            for j in range(i * i, limit + 1, i):
                primes[j] = False
    return primes

def is_prime_4(n):
    primes = sieve_of_eratosthenes(n)
    return primes[n]

# Example usage:
num = int(input("Enter a number: "))
if is_prime_4(num):
    print(f"{num} is a prime number.")
else:
    print(f"{num} is not a prime number.")

